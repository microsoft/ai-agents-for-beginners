#!/usr/bin/dotnet run
#:package Microsoft.Extensions.AI@9.9.1
#:package Azure.AI.Agents.Persistent@1.2.0-beta.5
#:package Azure.Identity@1.15.0
#:package System.Linq.Async@6.0.3
#:package Microsoft.Agents.AI.AzureAI@1.0.0-preview.251001.3
#:package Microsoft.Agents.AI@1.0.0-preview.251001.3
#:package DotNetEnv@3.1.1

using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using Azure.AI.Agents.Persistent;
using Azure.Identity;
using Microsoft.Agents.AI;
using DotNetEnv;

// Load environment variables
Env.Load("../../../.env");

// Get Azure AI Foundry configuration
var azure_foundry_endpoint = Environment.GetEnvironmentVariable("AZURE_AI_PROJECT_ENDPOINT") ?? throw new InvalidOperationException("AZURE_AI_PROJECT_ENDPOINT is not set.");
var azure_foundry_model_id = Environment.GetEnvironmentVariable("AZURE_AI_MODEL_DEPLOYMENT_NAME") ?? "gpt-4.1-mini";

// Define document path
string pdfPath = "./document.md";

// Helper function to open file stream
async Task<Stream> OpenImageStreamAsync(string path)
{
    return await Task.Run(() => File.OpenRead(path));
}

// Open document stream
var pdfStream = await OpenImageStreamAsync(pdfPath);

// Create Persistent Agents Client
var persistentAgentsClient = new PersistentAgentsClient(azure_foundry_endpoint, new AzureCliCredential());

// Upload file
PersistentAgentFileInfo fileInfo = await persistentAgentsClient.Files.UploadFileAsync(pdfStream, PersistentAgentFilePurpose.Agents, "demo.md");

// Create vector store
PersistentAgentsVectorStore fileStore =
    await persistentAgentsClient.VectorStores.CreateVectorStoreAsync(
        [fileInfo.Id],
        metadata: new Dictionary<string, string>() { { "agentkey", bool.TrueString } });

// Create RAG agent
PersistentAgent agentModel = await persistentAgentsClient.Administration.CreateAgentAsync(
    azure_foundry_model_id,
    name: "DotNetRAGAgent",
    tools: [new FileSearchToolDefinition()],
    instructions: """
        You are an AI assistant designed to answer user questions using only the information retrieved from the provided document(s).

        - If a user's question cannot be answered using the retrieved context, **you must clearly respond**: 
        "I'm sorry, but the uploaded document does not contain the necessary information to answer that question."
        - Do not answer from general knowledge or reasoning. Do not make assumptions or generate hypothetical explanations.
        - Do not provide definitions, tutorials, or commentary that is not explicitly grounded in the content of the uploaded file(s).
        - If a user asks a question like "What is a Neural Network?", and this is not discussed in the uploaded document, respond as instructed above.
        - For questions that do have relevant content in the document (e.g., Contoso's travel insurance coverage), respond accurately, and cite the document explicitly.

        You must behave as if you have no external knowledge beyond what is retrieved from the uploaded document.
        """,
    toolResources: new()
    {
        FileSearch = new()
        {
            VectorStoreIds = { fileStore.Id },
        }
    },
    metadata: new Dictionary<string, string>() { { "agentkey", bool.TrueString } });

// Get AI Agent
AIAgent agent = await persistentAgentsClient.GetAIAgentAsync(agentModel.Id);

// Create new thread
AgentThread thread = agent.GetNewThread();

// Run query
Console.WriteLine(await agent.RunAsync("Can you explain Contoso's travel insurance coverage?", thread));
