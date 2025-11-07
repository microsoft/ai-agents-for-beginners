#!/usr/bin/dotnet run
#:package Microsoft.Extensions.AI@9.9.1
#:package Microsoft.Agents.AI.OpenAI@1.0.0-preview.251001.3
#:package Microsoft.Agents.AI@1.0.0-preview.251001.3
#:package DotNetEnv@3.1.1

using System;
using System.ComponentModel;
using System.ClientModel;

using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;

using DotNetEnv;

Env.Load("../../../.env");

[Description("Provides a random vacation destination.")]
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

var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? throw new InvalidOperationException("GITHUB_TOKEN is not set.");

var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions).GetChatClient(github_model_id).CreateAIAgent(
    instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations", tools: [AIFunctionFactory.Create(GetRandomDestination)]);

AgentThread thread = agent.GetNewThread();

Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
