#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*
#:package Azure.AI.OpenAI@2.1.0
#:package Azure.Identity@1.13.1

using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using Azure.AI.OpenAI;
using Azure.Identity;
using OpenAI.Chat;

// ============================================================================
// AGENTIC DESIGN PRINCIPLES DEMONSTRATION
// ============================================================================
// This sample demonstrates the three key design principles from the lesson:
// 1. TRANSPARENCY: The agent explains what it's doing and why
// 2. CONTROL: Users can customize preferences and the agent respects them
// 3. CONSISTENCY: The agent uses a predictable, standardized interaction pattern
// ============================================================================

// Tool Function: Random Destination Generator
// TRANSPARENCY: Clear description helps users understand this tool's purpose
[Description("Provides a random vacation destination. Returns a city and country.")]
static string GetRandomDestination()
{
    var destinations = new List<string>
    {
        "Paris, France",
        "Tokyo, Japan",
        "New York City, USA",
        "Sydney, Australia",
        "Rome, Italy",
        "Barcelona, Spain",
        "Cape Town, South Africa",
        "Rio de Janeiro, Brazil",
        "Bangkok, Thailand",
        "Vancouver, Canada"
    };

    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Tool Function: User Preference Storage (Demonstrates CONTROL principle)
// CONTROL: This tool allows users to set and manage their preferences
[Description("Saves user preferences for trip planning. Use this when the user specifies preferences like budget level (budget/moderate/luxury), trip style (adventure/relaxation/cultural), or duration preference.")]
static string SaveUserPreference(
    [Description("The type of preference being saved, e.g., 'budget', 'style', 'duration'")] string preferenceType,
    [Description("The value of the preference")] string preferenceValue)
{
    // In a real application, this would persist to a database
    Console.WriteLine($"\n[TRANSPARENCY] Saving preference: {preferenceType} = {preferenceValue}");
    return $"Preference saved: {preferenceType} is now set to '{preferenceValue}'. I will remember this for future suggestions.";
}

// Azure OpenAI with the Responses API (stable v1 endpoint). Sign in with `az login`.
var azureEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Agent Identity
var AGENT_NAME = "TravelAgent";

// ============================================================================
// AGENT INSTRUCTIONS - Demonstrating Design Principles
// ============================================================================
// These instructions embed the three design principles directly into the agent's behavior
var AGENT_INSTRUCTIONS = """
You are a helpful AI Agent that demonstrates the Agentic Design Principles.

## Your Core Principles

**TRANSPARENCY**: Always explain what you're doing and why.
- When using a tool, briefly explain which tool you're calling and why
- Share your reasoning process with the user
- Be honest about limitations or uncertainties

**CONTROL**: Respect user preferences and allow customization.
- Ask about preferences before making assumptions
- Use the SaveUserPreference tool to remember user choices
- Always prioritize explicit user requests over defaults

**CONSISTENCY**: Use a predictable, standardized interaction pattern.
- Start every conversation with a friendly greeting
- Structure responses in a clear, organized format
- Use similar phrasing for similar actions

## Initial Greeting (CONSISTENCY)

When the conversation begins, always introduce yourself with this message:
"Hello! I'm TravelAgent, your AI vacation planning assistant.

🔍 **Transparency**: I'll always explain my reasoning and the tools I use.
🎮 **Control**: Tell me your preferences, and I'll remember them.
🔄 **Consistency**: I follow a predictable pattern to make planning easy.

What kind of trip would you like me to help you plan today?"

## Guidelines
- When users specify a destination, plan for that location
- Only suggest random destinations when the user hasn't specified one
- Always confirm before making changes to preferences
""";

// Create AI Agent with Design Principles
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [
            AIFunctionFactory.Create(GetRandomDestination),
            AIFunctionFactory.Create(SaveUserPreference)
        ]
    );

// Create Conversation Session for Context Management
var session = await agent.CreateSessionAsync();

// ============================================================================
// DEMONSTRATION: Start with "Hello" to trigger the greeting (Issue #402 fix)
// ============================================================================
Console.WriteLine("=== Demonstrating Agentic Design Principles ===\n");
Console.WriteLine("User: Hello\n");
Console.WriteLine("Agent Response:");

await foreach (var update in agent.RunStreamingAsync("Hello", session))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine("\n");

// ============================================================================
// DEMONSTRATION: User sets a preference (CONTROL principle)
// ============================================================================
Console.WriteLine("---");
Console.WriteLine("User: I prefer luxury travel and cultural experiences.\n");
Console.WriteLine("Agent Response:");

await foreach (var update in agent.RunStreamingAsync("I prefer luxury travel and cultural experiences.", session))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine("\n");

// ============================================================================
// DEMONSTRATION: Agent uses tools with transparency
// ============================================================================
Console.WriteLine("---");
Console.WriteLine("User: Suggest a destination for me.\n");
Console.WriteLine("Agent Response:");

await foreach (var update in agent.RunStreamingAsync("Suggest a destination for me.", session))
{
    await Task.Delay(10);
    Console.Write(update);
}
