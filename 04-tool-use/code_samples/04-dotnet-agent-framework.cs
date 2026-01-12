#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Extensions.AI.OpenAI@10.*-*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System.ClientModel;
using System.ComponentModel;
using System.Text.Json;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

// ============================================================================
// TOOL USE DESIGN PATTERN DEMONSTRATION
// ============================================================================
// This sample demonstrates the key concepts from the Tool Use lesson:
// 1. FUNCTION SCHEMAS: Clear descriptions and typed parameters
// 2. MULTIPLE TOOLS: Agent selects the right tool for each task
// 3. TOOL COMPOSITION: Tools can work together to solve complex requests
// 4. PARAMETER HANDLING: Functions with different parameter types
// ============================================================================

// ----------------------------------------------------------------------------
// TOOL 1: Random Destination Generator (No Parameters)
// ----------------------------------------------------------------------------
// Demonstrates: Simple tool with no parameters
[Description("Provides a random vacation destination when the user hasn't specified one.")]
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
    
    Console.WriteLine($"\n[Tool Called] GetRandomDestination() -> {destinations[index]}");
    return destinations[index];
}

// ----------------------------------------------------------------------------
// TOOL 2: Weather Lookup (Single Parameter)
// ----------------------------------------------------------------------------
// Demonstrates: Tool with a required parameter - the LLM must extract
// the location from the user's message and pass it to this function
[Description("Gets the current weather conditions for a specified location. Use this when planning activities or packing suggestions.")]
static string GetWeather(
    [Description("The city and country to get weather for, e.g., 'Paris, France'")] string location)
{
    // Simulated weather data for demonstration
    var weatherConditions = new Dictionary<string, (string condition, int tempC, int tempF)>
    {
        { "paris", ("Partly Cloudy", 18, 64) },
        { "tokyo", ("Sunny", 24, 75) },
        { "new york", ("Rainy", 15, 59) },
        { "sydney", ("Sunny", 28, 82) },
        { "rome", ("Clear", 22, 72) },
        { "barcelona", ("Sunny", 26, 79) },
        { "cape town", ("Windy", 19, 66) },
        { "rio", ("Hot and Humid", 32, 90) },
        { "bangkok", ("Tropical", 33, 91) },
        { "vancouver", ("Overcast", 12, 54) }
    };

    var locationLower = location.ToLower();
    foreach (var (key, weather) in weatherConditions)
    {
        if (locationLower.Contains(key))
        {
            var result = $"Weather in {location}: {weather.condition}, {weather.tempC}°C ({weather.tempF}°F)";
            Console.WriteLine($"\n[Tool Called] GetWeather(\"{location}\") -> {result}");
            return result;
        }
    }

    var defaultResult = $"Weather in {location}: Mild conditions, around 20°C (68°F)";
    Console.WriteLine($"\n[Tool Called] GetWeather(\"{location}\") -> {defaultResult}");
    return defaultResult;
}

// ----------------------------------------------------------------------------
// TOOL 3: Destination Information (Multiple Parameters)
// ----------------------------------------------------------------------------
// Demonstrates: Tool with multiple parameters including an enum-like category
[Description("Gets detailed information about a destination including attractions, cuisine, and travel tips. Use this after selecting a destination to provide rich details.")]
static string GetDestinationInfo(
    [Description("The destination city to get information about")] string destination,
    [Description("The category of information: 'attractions', 'cuisine', 'tips', or 'all'")] string category = "all")
{
    Console.WriteLine($"\n[Tool Called] GetDestinationInfo(\"{destination}\", \"{category}\")");
    
    // Simulated destination data
    var info = new Dictionary<string, Dictionary<string, string>>
    {
        { "paris", new() {
            { "attractions", "Eiffel Tower, Louvre Museum, Notre-Dame, Champs-Élysées" },
            { "cuisine", "Croissants, French onion soup, Coq au vin, Macarons" },
            { "tips", "Metro is efficient, book museums in advance, tip 10-15%" }
        }},
        { "tokyo", new() {
            { "attractions", "Senso-ji Temple, Shibuya Crossing, Tokyo Tower, Akihabara" },
            { "cuisine", "Sushi, Ramen, Tempura, Wagyu beef" },
            { "tips", "Get a Suica card, bow when greeting, shoes off indoors" }
        }},
        { "rome", new() {
            { "attractions", "Colosseum, Vatican, Trevi Fountain, Pantheon" },
            { "cuisine", "Pasta Carbonara, Pizza al taglio, Gelato, Tiramisu" },
            { "tips", "Book Vatican early, carry water bottle, siesta 1-4pm" }
        }}
    };

    var destLower = destination.ToLower();
    foreach (var (key, data) in info)
    {
        if (destLower.Contains(key))
        {
            if (category.ToLower() == "all")
            {
                return JsonSerializer.Serialize(data, new JsonSerializerOptions { WriteIndented = true });
            }
            if (data.TryGetValue(category.ToLower(), out var value))
            {
                return $"{category} in {destination}: {value}";
            }
        }
    }

    return $"Information about {destination}: A wonderful destination with rich culture and experiences.";
}

// ----------------------------------------------------------------------------
// TOOL 4: Trip Cost Estimator (Numeric Parameters)
// ----------------------------------------------------------------------------
// Demonstrates: Tool with numeric parameters for calculations
[Description("Estimates the total trip cost based on destination, duration, and budget level. Returns a cost breakdown.")]
static string EstimateTripCost(
    [Description("The destination city")] string destination,
    [Description("Number of days for the trip")] int days,
    [Description("Budget level: 'budget', 'moderate', or 'luxury'")] string budgetLevel = "moderate")
{
    Console.WriteLine($"\n[Tool Called] EstimateTripCost(\"{destination}\", {days}, \"{budgetLevel}\")");
    
    var dailyRates = new Dictionary<string, int>
    {
        { "budget", 100 },
        { "moderate", 250 },
        { "luxury", 500 }
    };

    var rate = dailyRates.GetValueOrDefault(budgetLevel.ToLower(), 250);
    var accommodation = rate * days;
    var food = (rate / 2) * days;
    var activities = (rate / 3) * days;
    var total = accommodation + food + activities;

    return $"""
        Trip Cost Estimate for {destination} ({days} days, {budgetLevel}):
        - Accommodation: ${accommodation}
        - Food & Dining: ${food}
        - Activities: ${activities}
        - Estimated Total: ${total}
        """;
}

// Extract configuration from environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// Configure OpenAI Client Options
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Agent Identity
var AGENT_NAME = "TravelAgent";

// ============================================================================
// AGENT INSTRUCTIONS - Tool Use Expert
// ============================================================================
var AGENT_INSTRUCTIONS = """
You are a travel planning AI Agent with access to multiple specialized tools.

## Available Tools

You have access to these tools - use them appropriately:

1. **GetRandomDestination**: Suggests a random destination (no parameters needed)
2. **GetWeather**: Gets weather for a location (requires: location)
3. **GetDestinationInfo**: Gets attraction/cuisine/tips (requires: destination, optional: category)
4. **EstimateTripCost**: Calculates costs (requires: destination, days; optional: budgetLevel)

## Tool Usage Guidelines

- **Chain tools together** for comprehensive responses (e.g., destination → weather → info → cost)
- **Extract parameters** from the user's message to pass to tools
- **Choose the right tool** based on what the user is asking
- When the user asks for a "complete trip plan", use multiple tools

## Response Format

After using tools, synthesize the information into a helpful, well-organized response.
Always mention which tools you used so users understand the agent's capabilities.
""";

// Create AI Agent with Multiple Tools
// This demonstrates the Tool Use Design Pattern with a variety of tool types
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .AsIChatClient()
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [
            AIFunctionFactory.Create(GetRandomDestination),
            AIFunctionFactory.Create(GetWeather),
            AIFunctionFactory.Create(GetDestinationInfo),
            AIFunctionFactory.Create(EstimateTripCost)
        ]
    );

// Create Conversation Thread
AgentThread thread = agent.GetNewThread();

// ============================================================================
// DEMONSTRATION 1: Tool Selection - Agent picks the right tool
// ============================================================================
Console.WriteLine("=== Tool Use Design Pattern Demonstration ===\n");
Console.WriteLine("--- Demo 1: Tool Selection ---");
Console.WriteLine("User: What's the weather like in Tokyo?\n");
Console.WriteLine("Agent Response:");

await foreach (var update in agent.RunStreamingAsync("What's the weather like in Tokyo?", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine("\n");

// ============================================================================
// DEMONSTRATION 2: Parameterized Tool Calling
// ============================================================================
Console.WriteLine("--- Demo 2: Parameterized Tool with Multiple Parameters ---");
Console.WriteLine("User: How much would a 5-day luxury trip to Rome cost?\n");
Console.WriteLine("Agent Response:");

await foreach (var update in agent.RunStreamingAsync("How much would a 5-day luxury trip to Rome cost?", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine("\n");

// ============================================================================
// DEMONSTRATION 3: Tool Composition - Multiple tools for complex requests
// ============================================================================
Console.WriteLine("--- Demo 3: Tool Composition ---");
Console.WriteLine("User: Plan me a complete trip - suggest a destination and give me all the details including weather and costs for a 3-day moderate budget trip.\n");
Console.WriteLine("Agent Response:");

await foreach (var update in agent.RunStreamingAsync(
    "Plan me a complete trip - suggest a destination and give me all the details including weather and costs for a 3-day moderate budget trip.", 
    thread))
{
    await Task.Delay(10);
    Console.Write(update);
}
