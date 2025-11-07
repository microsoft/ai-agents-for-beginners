#!/usr/bin/dotnet run
#:package Microsoft.Extensions.AI.Abstractions@9.9.1
#:package Azure.AI.Agents.Persistent@1.2.0-beta.4
#:package Azure.Identity@1.15.0
#:package System.Linq.Async@6.0.3
#:package Microsoft.Extensions.AI@9.9.1
#:package DotNetEnv@3.1.1
#:package OpenTelemetry.Api@1.12.0
#:package Microsoft.Agents.AI.Workflows@1.0.0-preview.251001.3
#:package Microsoft.Agents.AI.OpenAI@1.0.0-preview.251001.2

using System;
using System.ClientModel;
using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;
using OpenAI;
using DotNetEnv;

// Load environment variables
Env.Load("../../../.env");

// Get configuration from environment
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client for GitHub Models
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Define agent roles and instructions
const string REVIEWER_NAME = "Concierge";
const string REVIEWER_INSTRUCTIONS = @"""
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers.
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
ChatClientAgentOptions frontdeskAgentOptions = new(name: FRONTDESK_NAME, instructions: FRONTDESK_INSTRUCTIONS);
ChatClientAgentOptions reviewerAgentOptions = new(name: REVIEWER_NAME, instructions: REVIEWER_INSTRUCTIONS);

// Create agents
AIAgent reviewerAgent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions).GetChatClient(github_model_id).CreateAIAgent(
    reviewerAgentOptions);
AIAgent frontdeskAgent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions).GetChatClient(github_model_id).CreateAIAgent(
    frontdeskAgentOptions);

// Build workflow with agent coordination
var workflow = new WorkflowBuilder(frontdeskAgent)
            .AddEdge(frontdeskAgent, reviewerAgent)
            .Build();

// Execute workflow with streaming
StreamingRun run = await InProcessExecution.StreamAsync(workflow, new ChatMessage(ChatRole.User, "I would like to go to Paris."));

await run.TrySendMessageAsync(new TurnToken(emitEvents: true));

string strResult = "";

// Process streaming events
await foreach (WorkflowEvent evt in run.WatchStreamAsync().ConfigureAwait(false))
{
    if (evt is AgentRunUpdateEvent executorComplete)
    {
        strResult += executorComplete.Data;
        Console.WriteLine($"{executorComplete.ExecutorId}: {executorComplete.Data}");
    }
}

// Display final result
Console.WriteLine("\nFinal Result:");
Console.WriteLine(strResult);
