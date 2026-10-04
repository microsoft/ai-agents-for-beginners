#!/usr/bin/dotnet run

#:package OpenAI@2.14.0

using System.ClientModel;
using System.ComponentModel;
using OpenAI;
using OpenAI.Chat;

// Tool Function: Random Destination Generator
// This static method will be available to the agent as a callable tool
// The [Description] attribute helps the AI understand when to use this function
// This demonstrates how to create custom tools for AI agents
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
    // List of popular vacation destinations around the world
    // The agent will randomly select from these options
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

    // Generate random index and return selected destination
    // Uses System.Random for simple random selection
    var index = Random.Shared.Next(destinations.Count);
    return destinations[index];
}

var getRandomDestinationTool = ChatTool.CreateFunctionTool(
    functionName: nameof(GetRandomDestination),
    functionDescription: "Provides a random vacation destination."
);

var openAIEndpoint = new Uri("https://openrouter.ai/api/v1");
var model = "openrouter/free";
var apiKey = Environment.GetEnvironmentVariable("OPENROUTER_API_KEY") ?? throw new InvalidOperationException("OPENROUTER_API_KEY is not set.");

ChatClient client = new(
    model: model,
    credential: new ApiKeyCredential(apiKey),
    options: new OpenAIClientOptions()
    {
        Endpoint = openAIEndpoint
    });


// Create AI Agent with Travel Planning Capabilities
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, instructions, and available tools
// The agent can now plan trips using the GetRandomDestination function
List<ChatMessage> messages = [
    new SystemChatMessage("You are a helpful AI Agent that can help plan vacations for customers at random destinations."),
    new UserChatMessage("Plan me a day trip"),
];

Console.WriteLine("System: You are a helpful AI Agent that can help plan vacations for customers at random destinations.");
Console.WriteLine("User: Plan me a day trip");

ChatCompletionOptions options = new()
{
    Tools = { getRandomDestinationTool },
};

bool requiresAction;

do
{
    requiresAction = false;

    ChatCompletion completion = await client.CompleteChatAsync(messages, options);
    
    switch (completion.FinishReason)
    {
        case ChatFinishReason.Stop:
            {
                Console.WriteLine($"Assistant: {completion.Content[0].Text}");
                // Add the assistant message to the conversation history.
                messages.Add(new AssistantChatMessage(completion));
                break;
            }

        case ChatFinishReason.ToolCalls:
            {
                // First, add the assistant message with tool calls to the conversation history.
                messages.Add(new AssistantChatMessage(completion));

                // Then, add a new tool message for each tool call that is resolved.
                foreach (var toolCall in completion.ToolCalls)
                {
                    Console.WriteLine($"ToolCall: {toolCall.FunctionName} with {toolCall.FunctionArguments}");
                    switch (toolCall.FunctionName)
                    {
                        case nameof(GetRandomDestination):
                            {
                                var toolResult = GetRandomDestination();
                                messages.Add(new ToolChatMessage(toolCall.Id, toolResult));
                                break;
                            }

                        default:
                            {
                                // Handle other unexpected calls.
                                throw new NotImplementedException();
                            }
                    }
                }

                requiresAction = true;
                break;
            }

        case ChatFinishReason.Length:
            throw new NotImplementedException("Incomplete model output due to MaxTokens parameter or token limit exceeded.");

        case ChatFinishReason.ContentFilter:
            throw new NotImplementedException("Omitted content due to a content filter flag.");

        case ChatFinishReason.FunctionCall:
            throw new NotImplementedException("Deprecated in favor of tool calls.");

        default:
            throw new NotImplementedException(completion.FinishReason.ToString());
    }
} while (requiresAction);
