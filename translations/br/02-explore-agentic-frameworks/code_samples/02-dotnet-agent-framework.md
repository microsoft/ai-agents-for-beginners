<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T12:14:06+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "br"
}
-->
# 🔍 Explorando o Microsoft Agent Framework - Agente Básico (.NET)

## 📋 Objetivos de Aprendizagem

Este exemplo explora os conceitos fundamentais do Microsoft Agent Framework por meio de uma implementação básica de agente em .NET. Você aprenderá padrões essenciais de agentes e entenderá como agentes inteligentes funcionam nos bastidores usando C# e o ecossistema .NET.

### O que Você Vai Descobrir

- 🏗️ **Arquitetura de Agentes**: Compreendendo a estrutura básica de agentes de IA em .NET  
- 🛠️ **Integração de Ferramentas**: Como os agentes utilizam funções externas para ampliar suas capacidades  
- 💬 **Fluxo de Conversação**: Gerenciando conversas de múltiplas etapas e contexto com gerenciamento de threads  
- 🔧 **Padrões de Configuração**: Melhores práticas para configuração e gerenciamento de agentes em .NET  

## 🎯 Conceitos-Chave Abordados

### Princípios do Framework de Agentes

- **Autonomia**: Como os agentes tomam decisões independentes usando abstrações de IA do .NET  
- **Reatividade**: Respondendo a mudanças no ambiente e entradas do usuário  
- **Proatividade**: Tomando iniciativa com base em objetivos e contexto  
- **Habilidade Social**: Interagindo por meio de linguagem natural com threads de conversação  

### Componentes Técnicos

- **AIAgent**: Orquestração central de agentes e gerenciamento de conversação (.NET)  
- **Funções de Ferramentas**: Ampliando as capacidades do agente com métodos e atributos em C#  
- **Integração com OpenAI**: Aproveitando modelos de linguagem por meio de APIs padronizadas do .NET  
- **Configuração Segura**: Gerenciamento de chaves de API baseado em ambiente  

## 🔧 Stack Técnico

### Tecnologias Principais

- Microsoft Agent Framework (.NET)  
- Integração com API de Modelos do GitHub  
- Padrões de cliente compatíveis com OpenAI  
- Configuração baseada em ambiente com DotNetEnv  

### Capacidades do Agente

- Compreensão e geração de linguagem natural  
- Chamadas de função e uso de ferramentas com atributos em C#  
- Respostas sensíveis ao contexto com threads de conversação  
- Arquitetura extensível com padrões de injeção de dependência  

## 📚 Comparação de Frameworks

Este exemplo demonstra a abordagem do Microsoft Agent Framework em comparação com outros frameworks de agentes:

| Recurso         | Microsoft Agent Framework | Outros Frameworks       |
|------------------|---------------------------|--------------------------|
| **Integração**   | Ecossistema nativo da Microsoft | Compatibilidade variada |
| **Simplicidade** | API limpa e intuitiva     | Configuração frequentemente complexa |
| **Extensibilidade** | Integração fácil de ferramentas | Dependente do framework |
| **Pronto para Empresas** | Projetado para produção | Varia conforme o framework |

## 🚀 Começando

### Pré-requisitos

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ou superior  
- [Token de acesso à API de Modelos do GitHub](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Variáveis de Ambiente Necessárias

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```
  
```powershell
# PowerShell
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```
  

### Código de Exemplo

Para executar o exemplo de código,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
Ou usando o CLI do dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
Veja [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) para o código completo.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System.ClientModel;
using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

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
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Extract configuration from environment variables
// Retrieve the GitHub Models API endpoint, defaults to https://models.github.ai/inference if not specified
// Retrieve the model ID, defaults to openai/gpt-5-mini if not specified
// Retrieve the GitHub token for authentication, throws exception if not specified
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// Configure OpenAI Client Options
// Create configuration options to point to GitHub Models endpoint
// This redirects OpenAI client calls to GitHub's model inference service
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
// Create OpenAI client using GitHub token for authentication
// Configure it to use GitHub Models endpoint instead of OpenAI directly
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Define Agent Identity and Comprehensive Instructions
// Agent name for identification and logging purposes
var AGENT_NAME = "TravelAgent";

// Detailed instructions that define the agent's personality, capabilities, and behavior
// This system prompt shapes how the agent responds and interacts with users
var AGENT_INSTRUCTIONS = """
You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
"Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?"

Always prioritize user preferences. If they mention a specific destination like "Bali" or "Paris," focus your planning on that location rather than suggesting alternatives.
""";

// Create AI Agent with Advanced Travel Planning Capabilities
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Thread for Context Management
// Initialize a new conversation thread to maintain context across multiple interactions
// Threads enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentThread thread = agent.GetNewThread();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the thread parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation threads and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}
```
  

## 🎓 Principais Conclusões

1. **Arquitetura de Agentes**: O Microsoft Agent Framework oferece uma abordagem limpa e segura para construir agentes de IA em .NET  
2. **Integração de Ferramentas**: Funções decoradas com atributos `[Description]` tornam-se ferramentas disponíveis para o agente  
3. **Contexto de Conversação**: O gerenciamento de threads permite conversas de múltiplas etapas com total consciência de contexto  
4. **Gerenciamento de Configuração**: Variáveis de ambiente e manipulação segura de credenciais seguem as melhores práticas do .NET  
5. **Compatibilidade com OpenAI**: A integração com Modelos do GitHub funciona perfeitamente por meio de APIs compatíveis com OpenAI  

## 🔗 Recursos Adicionais

- [Documentação do Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)  
- [Marketplace de Modelos do GitHub](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->