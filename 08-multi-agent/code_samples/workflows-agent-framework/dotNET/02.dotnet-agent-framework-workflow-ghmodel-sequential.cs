#!/usr/bin/dotnet run
#:package Microsoft.Extensions.AI@10.*
#:package Azure.AI.OpenAI@2.1.0
#:package Azure.Identity@1.15.0
#:package System.Linq.Async@6.0.3
#:package OpenTelemetry.Api@1.*
#:package Microsoft.Agents.AI.Workflows@1.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*
#:package DotNetEnv@3.1.1

using System;
using System.ComponentModel;
using System.IO;
using Azure.AI.OpenAI;
using Azure.Identity;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;
using OpenAI.Chat;
using ChatMessage = Microsoft.Extensions.AI.ChatMessage;
using DotNetEnv;

// Load environment variables from .env file
Env.Load("../../../.env");

// Azure OpenAI with the Responses API (stable v1 endpoint). Sign in with `az login`.
var azureEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

// Path to furniture image for analysis
var imgPath = "../imgs/home.png";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Define Sales Agent (Stage 1) - Furniture Analysis
const string SalesAgentName = "Sales-Agent";
const string SalesAgentInstructions = "You are my furniture sales consultant, you can find different furniture elements from the pictures and give me a purchase suggestion";

// Define Price Agent (Stage 2) - Pricing Specialist
const string PriceAgentName = "Price-Agent";
const string PriceAgentInstructions = @"You are a furniture pricing specialist and budget consultant. Your responsibilities include:
        1. Analyze furniture items and provide realistic price ranges based on quality, brand, and market standards
        2. Break down pricing by individual furniture pieces
        3. Provide budget-friendly alternatives and premium options
        4. Consider different price tiers (budget, mid-range, premium)
        5. Include estimated total costs for room setups
        6. Suggest where to find the best deals and shopping recommendations
        7. Factor in additional costs like delivery, assembly, and accessories
        8. Provide seasonal pricing insights and best times to buy
        Always format your response with clear price breakdowns and explanations for the pricing rationale.";

// Define Quote Agent (Stage 3) - Quote Document Generator
const string QuoteAgentName = "Quote-Agent";
const string QuoteAgentInstructions = @"You are an assistant that creates a quote for furniture purchase.
        1. Create a well-structured quote document that includes:
        2. A title page with the document title, date, and client name
        3. An introduction summarizing the purpose of the document
        4. A summary section with total estimated costs and recommendations
        5. Use clear headings, bullet points, and tables for easy readability
        6. All quotes are presented in markdown form";

// Helper function to load image as byte array
async Task<byte[]> OpenImageBytesAsync(string path)
{
    return await File.ReadAllBytesAsync(path);
}

// Load furniture image for analysis
var imageBytes = await OpenImageBytesAsync(imgPath);

// Create AI agents for the sequential workflow
AIAgent salesAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name: SalesAgentName, instructions: SalesAgentInstructions);
AIAgent priceAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name: PriceAgentName, instructions: PriceAgentInstructions);
AIAgent quoteAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name: QuoteAgentName, instructions: QuoteAgentInstructions);

// Build sequential workflow: Sales → Price → Quote
var workflow = new WorkflowBuilder(salesAgent)
    .AddEdge(salesAgent, priceAgent)
    .AddEdge(priceAgent, quoteAgent)
    .Build();

// Create user message with image and instructions
ChatMessage userMessage = new ChatMessage(ChatRole.User, [
    new DataContent(imageBytes, "image/png"),
    new TextContent("Please find the relevant furniture according to the image and give the corresponding price for each piece of furniture. Finally output generates a quotation")
]);

// Execute workflow with streaming
StreamingRun run = await InProcessExecution.RunStreamingAsync(workflow, userMessage);

// Process workflow events and collect results
await run.TrySendMessageAsync(new TurnToken(emitEvents: true));
string id = "";
string messageData = "";
await foreach (WorkflowEvent evt in run.WatchStreamAsync().ConfigureAwait(false))
{
    if (evt is AgentResponseUpdateEvent executorComplete)
    {
        if (id == "")
        {
            id = executorComplete.ExecutorId;
        }
        if (id == executorComplete.ExecutorId)
        {
            messageData += executorComplete.Data?.ToString();
        }
        else
        {
            id = executorComplete.ExecutorId;
        }
    }
}

// Display final workflow results (complete quote document)
Console.WriteLine(messageData);
