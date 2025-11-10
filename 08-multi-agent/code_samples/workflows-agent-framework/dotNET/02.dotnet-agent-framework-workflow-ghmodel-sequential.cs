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
using System.IO;
using OpenAI;
using Azure.Identity;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;
using DotNetEnv;

// Load environment variables from .env file
Env.Load("../../../.env");

// Configure GitHub Models endpoint and credentials
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = "gpt-4o";  // Using GPT-4o for vision capabilities
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Path to furniture image for analysis
var imgPath = "../imgs/home.png";

// Configure OpenAI client options with GitHub Models endpoint
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Create OpenAI client with API key credential
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

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
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name: SalesAgentName, instructions: SalesAgentInstructions);
AIAgent priceagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name: PriceAgentName, instructions: PriceAgentInstructions);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name: QuoteAgentName, instructions: QuoteAgentInstructions);

// Build sequential workflow: Sales → Price → Quote
var workflow = new WorkflowBuilder(salesagent)
    .AddEdge(salesagent, priceagent)
    .AddEdge(priceagent, quoteagent)
    .Build();

// Create user message with image and instructions
ChatMessage userMessage = new ChatMessage(ChatRole.User, [
    new DataContent(imageBytes, "image/png"),
    new TextContent("Please find the relevant furniture according to the image and give the corresponding price for each piece of furniture. Finally output generates a quotation")
]);

// Execute workflow with streaming
StreamingRun run = await InProcessExecution.StreamAsync(workflow, userMessage);

// Process workflow events and collect results
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

// Display final workflow results (complete quote document)
Console.WriteLine(messageData);
