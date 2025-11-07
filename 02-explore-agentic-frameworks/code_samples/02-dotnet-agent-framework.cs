#!/usr/bin/dotnet run
#:package Microsoft.Extensions.AI@9.9.1
#:package Microsoft.Agents.AI.OpenAI@1.0.0-preview.251001.3
#:package Microsoft.Agents.AI@1.0.0-preview.251001.3
#:package DotNetEnv@3.1.1

// 📚 Import Essential Namespaces for Agent Development
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;

// 🔧 Load Environment Configuration from .env File
// Load configuration from a .env file located 3 directories up from current location
// This loads: GITHUB_ENDPOINT, GITHUB_TOKEN, GITHUB_MODEL_ID
// Ensures secure handling of API credentials and configuration settings
Env.Load("../../../.env");

// 🎲 Tool Function: Random Destination Generator (.NET Implementation)
// This static method demonstrates how to create tools for agents in .NET
// The [Description] attribute helps the AI understand when and how to use this function
// This showcases the .NET approach to extending agent capabilities with custom tools
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
    // Curated list of popular vacation destinations worldwide
    // The agent will randomly select from these options when users need destination suggestions
    var destinations = new List<string>
    {
        "Paris, France",         // European cultural capital
        "Tokyo, Japan",          // Asian modern metropolis  
        "New York City, USA",    // American urban experience
        "Sydney, Australia",     // Oceanic coastal beauty
        "Rome, Italy",           // Historical European city
        "Barcelona, Spain",      // Mediterranean cultural hub
        "Cape Town, South Africa", // African scenic destination
        "Rio de Janeiro, Brazil",  // South American beach city
        "Bangkok, Thailand",        // Southeast Asian cultural center
        "Vancouver, Canada"         // North American natural beauty
    };

    // Generate random index using System.Random and return selected destination
    // This demonstrates simple random selection in .NET
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// 🔑 Extract and Validate Configuration from Environment Variables
// Retrieve GitHub Models API endpoint - throws exception if not configured
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
// Get the AI model ID - defaults to gpt-4o-mini if not specified
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
// Retrieve GitHub authentication token - throws exception if missing
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// ⚙️ Configure OpenAI Client Options for GitHub Models Integration
// Create configuration options to redirect OpenAI client calls to GitHub Models endpoint
// This enables using OpenAI-compatible APIs with GitHub's model inference service
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)  // Set custom endpoint for GitHub Models API
};

// 🔌 Initialize OpenAI Client with GitHub Models Configuration
// Create OpenAI client instance using GitHub token for authentication
// Configure it to use GitHub Models endpoint instead of OpenAI directly
// This client will handle all communication with the AI model
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// 🤖 Define Agent Identity and Comprehensive Instructions
// Agent name for identification and logging purposes
const string AGENT_NAME = "TravelAgent";

// Detailed instructions that define the agent's personality, capabilities, and behavior
// This system prompt shapes how the agent responds and interacts with users
const string AGENT_INSTRUCTIONS = @"You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
""Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?""

Always prioritize user preferences. If they mention a specific destination like ""Bali"" or ""Paris,"" focus your planning on that location rather than suggesting alternatives.
";

// 🤖 Create AI Agent with Advanced Travel Planning Capabilities
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions)
    .GetChatClient(github_model_id)  // Get chat client for the specified AI model
    .CreateAIAgent(
        name: AGENT_NAME,             // Set agent identifier for logging and tracking
        instructions: AGENT_INSTRUCTIONS,  // Comprehensive behavior and personality instructions
        tools: [AIFunctionFactory.Create((Func<string>)GetRandomDestination)]  // Register tool functions
    );

// 🧵 Create New Conversation Thread for Context Management
// Initialize a new conversation thread to maintain context across multiple interactions
// Threads enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentThread thread = agent.GetNewThread();

// 🚀 Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the thread parameter maintains conversation context for subsequent interactions
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// 🔄 Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation threads and contextual understanding in .NET agents
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
