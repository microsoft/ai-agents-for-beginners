#!/usr/bin/dotnet run
#:package Microsoft.Extensions.AI.Abstractions@10.*
#:package Azure.AI.Agents.Persistent@1.2.0-beta.10
#:package Azure.AI.OpenAI@2.1.0
#:package Azure.Identity@1.15.0
#:package System.Linq.Async@6.0.3
#:package Microsoft.Extensions.AI@10.*
#:package DotNetEnv@3.1.1
#:package OpenTelemetry.Api@1.*
#:package Microsoft.Agents.AI.Workflows@1.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System;
using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;
using Azure.AI.OpenAI;
using Azure.Identity;
using ChatMessage = Microsoft.Extensions.AI.ChatMessage;
using OpenAI.Chat;
using DotNetEnv;

// Load environment variables
Env.Load("../../.env");

// Azure OpenAI with the Responses API (stable v1 endpoint). Sign in with `az login`.
var azureEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Define agent roles and instructions
const string REVIEWER_NAME = "Concierge";
const string REVIEWER_INSTRUCTIONS = @"""
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers.
    The goal is to determine if the front desk travel agent has recommended the best non-touristy experience for a traveler.
    If so, state that it is approved.
    If not, provide insight on how to refine the recommendation without using a specific example. 
    """;

const string FRONTDESK_NAME = "FrontDesk";
const string FRONTDESK_INSTRUCTIONS = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity as you deal with many customers.
    The goal is to provide the best activities and locations for a traveler to visit.
    Only provide a single recommendation per response.
    You're laser focused on the goal at hand.
    Don't waste time with chit chat.
    Consider suggestions when refining an idea.
    """;

// Create agent options
ChatClientAgentOptions frontdeskAgentOptions = new()
{
    Name = FRONTDESK_NAME,
    Description = FRONTDESK_INSTRUCTIONS,
};
ChatClientAgentOptions reviewerAgentOptions = new()
{
    Name = REVIEWER_NAME, 
    Description = REVIEWER_INSTRUCTIONS
};

// Create agents
AIAgent reviewerAgent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(reviewerAgentOptions);
AIAgent frontdeskAgent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(frontdeskAgentOptions);

// Build workflow with agent coordination
var workflow = new WorkflowBuilder(frontdeskAgent)
            .AddEdge(frontdeskAgent, reviewerAgent)
            .Build();

// Execute workflow with streaming
StreamingRun run = await InProcessExecution.RunStreamingAsync(workflow, new ChatMessage(ChatRole.User, "I would like to go to Paris."));

await run.TrySendMessageAsync(new TurnToken(emitEvents: true));

string strResult = "";

// Process streaming events
await foreach (WorkflowEvent evt in run.WatchStreamAsync().ConfigureAwait(false))
{
    if (evt is AgentResponseUpdateEvent executorComplete)
    {
        strResult += executorComplete.Data;
        Console.WriteLine($"{executorComplete.ExecutorId}: {executorComplete.Data}");
    }
}

// Display final result
Console.WriteLine("\nFinal Result:");
Console.WriteLine(strResult);
