#!/usr/bin/dotnet run
#:package Microsoft.Extensions.AI@10.*
#:package Azure.AI.OpenAI@2.*
#:package Azure.Identity@1.15.0
#:package System.Linq.Async@6.0.3
#:package OpenTelemetry.Api@1.*
#:package Microsoft.Agents.AI.Workflows@1.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*
#:package DotNetEnv@3.1.1

using Azure.AI.OpenAI;
using Azure.Identity;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;
using ChatMessage = Microsoft.Extensions.AI.ChatMessage;
using OpenAI.Chat;
using DotNetEnv;
using System.Text;

// Load environment variables from .env file
Env.Load("../../../.env");

// Azure OpenAI with the Responses API (stable v1 endpoint). Sign in with `az login`.
var azureEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Define Researcher Agent for concurrent execution
const string ResearcherAgentName = "Researcher-Agent";
const string ResearcherAgentInstructions = "You are my travel researcher, working with me to analyze the destination, list relevant attractions, and make detailed plans for each attraction.";

// Define Planner Agent for concurrent execution
const string PlanAgentName = "Plan-Agent";
const string PlanAgentInstructions = "You are my travel planner, working with me to create a detailed travel plan based on the researcher's findings.";

// Create AI agents for concurrent workflow
AIAgent researcherAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name: ResearcherAgentName, instructions: ResearcherAgentInstructions);
AIAgent plannerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name: PlanAgentName, instructions: PlanAgentInstructions);

// Create custom executor instances
var startExecutor = new ConcurrentStartExecutor();
var aggregationExecutor = new ConcurrentAggregationExecutor();

// Build concurrent workflow with Fan-Out/Fan-In pattern
var workflow = new WorkflowBuilder(startExecutor)
    .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
    .AddFanInBarrierEdge(sources: [researcherAgent, plannerAgent], aggregationExecutor)
    .WithOutputFrom(aggregationExecutor)
    .Build();

// Execute concurrent workflow with streaming
StreamingRun run = await InProcessExecution.RunStreamingAsync(workflow, "Plan a trip to Seattle in December");

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
[SendsMessage(typeof(ChatMessage))]
[SendsMessage(typeof(TurnToken))]
public class ConcurrentStartExecutor() : Executor<string>("ConcurrentStartExecutor")
{
    /// <summary>
    /// Starts the concurrent processing by sending messages to the agents.
    /// </summary>
    /// <param name="message">The user message to process</param>
    /// <param name="context">Workflow context for accessing workflow services and adding events</param>
    /// <returns>A task representing the asynchronous operation</returns>
    [MessageHandler]
    public override async ValueTask HandleAsync(string message, IWorkflowContext context, CancellationToken cancellationToken = default)
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
[YieldsOutput(typeof(string))]
public class ConcurrentAggregationExecutor() : Executor<List<ChatMessage>>("ConcurrentAggregationExecutor")
{
    private readonly List<ChatMessage> _messages = [];

    /// <summary>
    /// Handles incoming messages from the agents and aggregates their responses.
    /// </summary>
    /// <param name="message">The message from the agent</param>
    /// <param name="context">Workflow context for accessing workflow services and adding events</param>
    /// <returns>A task representing the asynchronous operation</returns>
    public ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.AddRange(message);
    }

    protected override ValueTask OnMessageDeliveryFinishedAsync(IWorkflowContext context, CancellationToken cancellationToken = default)
    {
        StringBuilder resultBuilder = new();
        foreach (ChatMessage m in this._messages)
        {
            var formattedMessages = string.Join(Environment.NewLine, this._messages.Select(m => $"{m.AuthorName}: {m.Text}"));
            return context.YieldOutputAsync(formattedMessages);
        }

        return ValueTask.CompletedTask;
    }
}
