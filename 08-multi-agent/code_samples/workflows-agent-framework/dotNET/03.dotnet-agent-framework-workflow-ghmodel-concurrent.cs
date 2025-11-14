#!/usr/bin/dotnet run
#:package Microsoft.Extensions.AI@9.9.1
#:package System.ClientModel@1.6.1.0
#:package Azure.Identity@1.15.0
#:package System.Linq.Async@6.0.3
#:package OpenTelemetry.Api@1.0.0
#:package Microsoft.Agents.AI.Workflows@1.0.0-preview.251001.3
#:package Microsoft.Agents.AI.OpenAI@1.0.0-preview.251001.3
#:package DotNetEnv@3.1.1

using System;
using System.ComponentModel;
using System.ClientModel;
using OpenAI;
using Azure.Identity;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;
using Microsoft.Agents.AI.Workflows.Reflection;
using DotNetEnv;

// Load environment variables from .env file
Env.Load("../../../.env");

// Configure GitHub Models endpoint and credentials
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = "gpt-4o";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client options with GitHub Models endpoint
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Create OpenAI client with API key credential
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Define Researcher Agent for concurrent execution
const string ResearcherAgentName = "Researcher-Agent";
const string ResearcherAgentInstructions = "You are my travel researcher, working with me to analyze the destination, list relevant attractions, and make detailed plans for each attraction.";

// Define Planner Agent for concurrent execution
const string PlanAgentName = "Plan-Agent";
const string PlanAgentInstructions = "You are my travel planner, working with me to create a detailed travel plan based on the researcher's findings.";

// Create AI agents for concurrent workflow
AIAgent researcherAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name: ResearcherAgentName, instructions: ResearcherAgentInstructions);
AIAgent plannerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name: PlanAgentName, instructions: PlanAgentInstructions);

// Create custom executor instances
var startExecutor = new ConcurrentStartExecutor();
var aggregationExecutor = new ConcurrentAggregationExecutor();

// Build concurrent workflow with Fan-Out/Fan-In pattern
var workflow = new WorkflowBuilder(startExecutor)
    .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
    .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
    .WithOutputFrom(aggregationExecutor)
    .Build();

// Execute concurrent workflow with streaming
StreamingRun run = await InProcessExecution.StreamAsync(workflow, "Plan a trip to Seattle in December");

// Watch for workflow events and display final output
await foreach (WorkflowEvent evt in run.WatchStreamAsync().ConfigureAwait(false))
{
    if (evt is WorkflowOutputEvent output)
    {
        Console.WriteLine($"Workflow completed with results:\n{output.Data}");
    }
}

/// <summary>
/// Custom executor that starts concurrent processing by broadcasting to all agents.
/// This implements the "Fan-Out" pattern where one input triggers multiple parallel operations.
/// </summary>
public class ConcurrentStartExecutor() :
    ReflectingExecutor<ConcurrentStartExecutor>("ConcurrentStartExecutor"),
    IMessageHandler<string>
{
    /// <summary>
    /// Starts the concurrent processing by sending messages to the agents.
    /// </summary>
    /// <param name="message">The user message to process</param>
    /// <param name="context">Workflow context for accessing workflow services and adding events</param>
    /// <returns>A task representing the asynchronous operation</returns>
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Broadcast the message to all connected agents. Receiving agents will queue
        // the message but will not start processing until they receive a turn token.
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Broadcast the turn token to kick off the agents.
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

/// <summary>
/// Custom executor that aggregates results from concurrent agents.
/// This implements the "Fan-In" pattern where multiple parallel results are merged into one output.
/// </summary>
public class ConcurrentAggregationExecutor() :
    ReflectingExecutor<ConcurrentAggregationExecutor>("ConcurrentAggregationExecutor"),
    IMessageHandler<ChatMessage>
{
    private readonly List<ChatMessage> _messages = [];

    /// <summary>
    /// Handles incoming messages from the agents and aggregates their responses.
    /// </summary>
    /// <param name="message">The message from the agent</param>
    /// <param name="context">Workflow context for accessing workflow services and adding events</param>
    /// <returns>A task representing the asynchronous operation</returns>
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);

        // Wait for both agents to complete before aggregating
        if (this._messages.Count == 2)
        {
            var formattedMessages = string.Join(Environment.NewLine, this._messages.Select(m => $"{m.AuthorName}: {m.Text}"));
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
