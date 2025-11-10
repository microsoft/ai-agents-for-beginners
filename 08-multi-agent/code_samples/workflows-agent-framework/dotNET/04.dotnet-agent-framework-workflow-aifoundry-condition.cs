#!/usr/bin/dotnet run
#:package Microsoft.Extensions.AI@9.9.1
#:package Azure.AI.Agents.Persistent@1.2.0-beta.5
#:package Azure.Identity@1.15.0
#:package System.Linq.Async@6.0.3
#:package DotNetEnv@3.1.1
#:package OpenTelemetry.Api@1.0.0
#:package Microsoft.Agents.AI.Workflows@1.0.0-preview.251001.3
#:package Microsoft.Agents.AI.AzureAI@1.0.0-preview.251001.3

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading.Tasks;
using Azure.AI.Agents.Persistent;
using Azure.Identity;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using Microsoft.Extensions.Logging;
using Microsoft.Agents.AI.Workflows;
using Microsoft.Agents.AI.Workflows.Reflection;
using DotNetEnv;

// Load environment variables from .env file
Env.Load("../../../.env");

// Configure Azure AI Foundry endpoint and credentials
var azure_foundry_endpoint = Environment.GetEnvironmentVariable("AZURE_AI_PROJECT_ENDPOINT") ?? throw new InvalidOperationException("AZURE_AI_PROJECT_ENDPOINT is not set.");
var azure_foundry_model_id = "gpt-4o-mini";
var bing_conn_id = Environment.GetEnvironmentVariable("BING_CONNECTION_ID");

// Agent Instructions for Content Production Workflow
const string EvangelistInstructions = @"
You are a technology evangelist who creates first drafts for technical tutorials.
1. Each knowledge point in the outline must include a link. Follow the link to access the content related to the knowledge point in the outline. Expand on that content.
2. Each knowledge point must be explained in detail.
3. Rewrite the content according to the entry requirements, including the title, outline, and corresponding content. It is not necessary to follow the outline in full order.
4. The content must be more than 200 words.
4. Output draft as Markdown format. set 'draft_content' to the draft content.
5. return result as JSON with fields 'draft_content' (string).";

const string ContentReviewerInstructions = @"
You are a content reviewer and need to check whether the tutorial's draft content meets the following requirements:

1. If the draft content is less than 200 words, set 'review_result' to 'No' and 'reason' to 'Content is too short'. If the draft content is more than 200 words, set 'review_result' to 'Yes' and 'reason' to 'The content is good'.
2. set 'draft_content' to the original draft content.
3. return result as JSON with fields 'review_result' ('Yes' or  'No' ) and 'reason' (string) and 'draft_content' (string).";

const string PublisherInstructions = @"
You are the content publisher who runs code to save the tutorial's draft content as a Markdown file. Saved file's name is marked with current date and time, such as yearmonthdayhourminsec. Note that if it is 1-9, you need to add 0, such as  20240101123045.md.
";

// Sample content outline for tutorial generation
string OUTLINE_Content = @"
# Introduce AI Agent

## What's AI Agent
https://github.com/microsoft/ai-agents-for-beginners/tree/main/01-intro-to-ai-agents

***Note*** Don't create any sample code 

## Introduce Azure AI Foundry Agent Service 
https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview

***Note*** Don't create any sample code 

## Microsoft Agent Framework 
https://github.com/microsoft/agent-framework/tree/main/docs/docs-templates

***Note*** Don't create any sample code 
";

// Configure Bing Grounding for web search capabilities
var bingGroundingConfig = new BingGroundingSearchConfiguration(bing_conn_id);
BingGroundingToolDefinition bingGroundingTool = new(
    new BingGroundingSearchToolParameters([bingGroundingConfig])
);

// Create persistent agents client with Azure CLI authentication
var persistentAgentsClient = new PersistentAgentsClient(azure_foundry_endpoint, new AzureCliCredential());

// Create the three specialized agents in Azure AI Foundry
var evangelistMetadata = await persistentAgentsClient.Administration.CreateAgentAsync(
    model: azure_foundry_model_id,
    name: "Evangelist",
    instructions: EvangelistInstructions,
    tools: [bingGroundingTool]
);

var contentReviewerMetadata = await persistentAgentsClient.Administration.CreateAgentAsync(
    model: azure_foundry_model_id,
    name: "ContentReviewer",
    instructions: ContentReviewerInstructions
);

var publisherMetadata = await persistentAgentsClient.Administration.CreateAgentAsync(
    model: azure_foundry_model_id,
    name: "Publisher",
    instructions: PublisherInstructions,
    tools: [new CodeInterpreterToolDefinition()]
);

// Extract agent IDs for later use
string evangelist_agentId = evangelistMetadata.Value.Id;
string contentReviewer_agentId = contentReviewerMetadata.Value.Id;
string publisher_agentId = publisherMetadata.Value.Id;

// Get AI Agent instances with JSON schema response formatting
AIAgent evangelistagent = await persistentAgentsClient.GetAIAgentAsync(evangelist_agentId, new() { });
AIAgent contentRevieweragent = await persistentAgentsClient.GetAIAgentAsync(
    contentReviewer_agentId,
    new()
    {
        ResponseFormat = ChatResponseFormat.ForJsonSchema(
            AIJsonUtilities.CreateJsonSchema(typeof(ReviewResult)),
            "ReviewResult",
            "Review Result From DraftContent"
        )
    }
);
AIAgent publisheragent = await persistentAgentsClient.GetAIAgentAsync(publisher_agentId);

/// <summary>
/// Creates a condition function for workflow routing based on review results.
/// </summary>
Func<object?, bool> GetCondition(string expectedResult) =>
    reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// Create executor instances
var draftExecutor = new DraftExecutor(evangelistagent);
var contentReviewerExecutor = new ContentReviewExecutor(contentRevieweragent);
var publishExecutor = new PublishExecutor(publisheragent);
var sendReviewerExecutor = new SendReviewExecutor();

// Build conditional workflow with routing based on review results
var workflow = new WorkflowBuilder(draftExecutor)
    .AddEdge(draftExecutor, contentReviewerExecutor)
    .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
    .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
    .Build();

// Create user prompt with content outline
string prompt = @"You need to write a draft based on the following outline and the content provided in the link corresponding to the outline. 
After draft create, the reviewer check it, if it meets the requirements, it will be submitted to the publisher and save it as a Markdown file, 
otherwise need to rewrite draft until it meets the requirements.
The provided outline content and related links is as follows:" + OUTLINE_Content;

Console.WriteLine(prompt);

// Execute conditional workflow
var chat = new ChatMessage(ChatRole.User, prompt);
StreamingRun run = await InProcessExecution.StreamAsync(workflow, chat);

// Process workflow events and display results
await run.TrySendMessageAsync(new TurnToken(emitEvents: true));
string id = "";
string messageData = "";
await foreach (WorkflowEvent evt in run.WatchStreamAsync().ConfigureAwait(false))
{
    if (evt is AgentRunUpdateEvent executorComplete)
    {
        if (id == "")
        {
            id = executorComplete.ExecutorId;
        }
        if (id == executorComplete.ExecutorId)
        {
            messageData += executorComplete.Data.ToString();
        }
        else
        {
            id = executorComplete.ExecutorId;
        }
    }
}

Console.WriteLine(messageData);

// Define result models for structured JSON responses
public class ContentResult
{
    [JsonPropertyName("draft_content")]
    public string DraftContent { get; set; } = string.Empty;
}

public class ReviewResult
{
    [JsonPropertyName("review_result")]
    public string Result { get; set; } = string.Empty;
    
    [JsonPropertyName("reason")]
    public string Reason { get; set; } = string.Empty;
    
    [JsonPropertyName("draft_content")]
    public string DraftContent { get; set; } = string.Empty;
}

/// <summary>
/// Custom executor that creates content drafts from outlines.
/// </summary>
public class DraftExecutor : ReflectingExecutor<DraftExecutor>, IMessageHandler<ChatMessage, ContentResult>
{
    private readonly AIAgent _evangelistAgent;

    public DraftExecutor(AIAgent evangelistAgent) : base("DraftExecutor")
    {
        this._evangelistAgent = evangelistAgent;
    }

    public async ValueTask<ContentResult> HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        Console.WriteLine($"DraftExecutor .......loading \n" + message.Text);
        
        var response = await this._evangelistAgent.RunAsync(message);
        
        Console.WriteLine($"DraftExecutor response: {response.Text}");
        
        ContentResult contentResult = new ContentResult { DraftContent = Convert.ToString(response) ?? "" };
        
        Console.WriteLine($"DraftExecutor generated content: {contentResult.DraftContent}");
        
        return contentResult;
    }
}

/// <summary>
/// Custom executor that reviews content quality and determines approval.
/// </summary>
public class ContentReviewExecutor : ReflectingExecutor<ContentReviewExecutor>, IMessageHandler<ContentResult, ReviewResult>
{
    private readonly AIAgent _contentReviewerAgent;

    public ContentReviewExecutor(AIAgent contentReviewerAgent) : base("ContentReviewExecutor")
    {
        this._contentReviewerAgent = contentReviewerAgent;
    }

    public async ValueTask<ReviewResult> HandleAsync(ContentResult content, IWorkflowContext context)
    {
        Console.WriteLine($"ContentReviewExecutor .......loading");
        
        var response = await this._contentReviewerAgent.RunAsync(content.DraftContent);
        var reviewResult = JsonSerializer.Deserialize<ReviewResult>(response.Text);
        
        Console.WriteLine($"ContentReviewExecutor review result: {reviewResult.Result}, reason: {reviewResult.Reason}");
        
        return reviewResult;
    }
}

/// <summary>
/// Custom executor that publishes approved content.
/// </summary>
public class PublishExecutor : ReflectingExecutor<PublishExecutor>, IMessageHandler<ReviewResult>
{
    private readonly AIAgent _publishAgent;

    public PublishExecutor(AIAgent publishAgent) : base("PublishExecutor")
    {
        this._publishAgent = publishAgent;
    }

    public async ValueTask HandleAsync(ReviewResult review, IWorkflowContext context)
    {
        Console.WriteLine($"PublishExecutor .......loading");
        
        var response = await this._publishAgent.RunAsync(review.DraftContent);
        
        Console.WriteLine($"Response from PublishExecutor: {response.Text}");
        
        await context.YieldOutputAsync($"Publishing result: {response.Text}");
    }
}

/// <summary>
/// Custom executor that handles rejected content.
/// </summary>
public class SendReviewExecutor : ReflectingExecutor<SendReviewExecutor>, IMessageHandler<ReviewResult>
{
    public SendReviewExecutor() : base("SendReviewExecutor")
    {
    }

    public async ValueTask HandleAsync(ReviewResult message, IWorkflowContext context) =>
        await context.YieldOutputAsync($"Draft content sent for revision: {message.Result}");
}
