# 🔍 Explorando o Microsoft Agent Framework - Agente Básico (.NET)

## 📋 Objetivos de Aprendizagem

Este exemplo explora os conceitos fundamentais do Microsoft Agent Framework através de uma implementação básica de agente em .NET. Vai aprender os padrões centrais dos agentes e entender como os agentes inteligentes funcionam internamente usando C# e o ecossistema .NET.

### O Que Vai Descobrir

- 🏗️ **Arquitetura do Agente**: Compreender a estrutura básica dos agentes de IA em .NET
- 🛠️ **Integração de Ferramentas**: Como os agentes usam funções externas para ampliar capacidades  
- 💬 **Fluxo da Conversa**: Gerir conversas com múltiplas interações e contexto através da gestão de threads
- 🔧 **Padrões de Configuração**: Melhores práticas para configuração e gestão de agentes em .NET

## 🎯 Conceitos Chave Abordados

### Princípios do Framework Agente

- **Autonomia**: Como os agentes tomam decisões independentes usando abstrações de IA em .NET
- **Reatividade**: Responder a mudanças ambientais e inputs do utilizador
- **Proatividade**: Tomar iniciativa baseada em objetivos e contexto
- **Capacidade Social**: Interagir através da linguagem natural com threads de conversação

### Componentes Técnicos

- **AIAgent**: Orquestração central do agente e gestão de conversas (.NET)
- **Funções de Ferramentas**: Extender capacidades do agente com métodos e atributos em C#
- **Integração Azure OpenAI**: Aproveitar modelos de linguagem através da API Azure OpenAI Responses
- **Configuração Segura**: Gestão de endpoints com base no ambiente

## 🔧 Stack Técnica

### Tecnologias Principais

- Microsoft Agent Framework (.NET)
- Integração Azure OpenAI (API Responses)
- Padrões cliente Azure.AI.OpenAI
- Configuração baseada em ambiente com DotNetEnv

### Capacidades do Agente

- Compreensão e geração de linguagem natural
- Chamadas de funções e uso de ferramentas com atributos em C#
- Respostas contextualmente conscientes com sessões de conversação
- Arquitetura extensível com padrões de injeção de dependências

## 📚 Comparação de Frameworks

Este exemplo demonstra a abordagem do Microsoft Agent Framework comparada com outros frameworks de agentes:

| Característica | Microsoft Agent Framework | Outros Frameworks |
|---------|-------------------------|------------------|
| **Integração** | Ecossistema Microsoft nativo | Compatibilidade variada |
| **Simplicidade** | API limpa e intuitiva | Configuração muitas vezes complexa |
| **Extensibilidade** | Integração fácil de ferramentas | Dependente do framework |
| **Pronto para Empresas** | Construído para produção | Varia conforme framework |

## 🚀 Começar

### Pré-requisitos

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ou superior
- Uma [subscrição Azure](https://azure.microsoft.com/free/) com um recurso Azure OpenAI e uma implantação de modelo
- A [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — faça login com `az login`

### Variáveis de Ambiente Necessárias

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Depois, inicie sessão para que o AzureCliCredential possa obter um token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Depois, inicie sessão para que o AzureCliCredential possa obter um token
az login
```

### Código de Exemplo

Para executar o exemplo de código,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Ou usando a CLI dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Veja [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) para o código completo.

```csharp
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

// Azure OpenAI with the Responses API (stable v1 endpoint). Sign in with `az login`.
var azureEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

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
// Get the Responses client for the deployment and create the AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Session for Context Management.
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentSession session = await agent.CreateSessionAsync();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the session parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", session))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation sessions and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", session))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Principais Aprendizagens

1. **Arquitetura do Agente**: O Microsoft Agent Framework oferece uma abordagem limpa e segura em tipos para construir agentes de IA em .NET
2. **Integração de Ferramentas**: Funções decoradas com atributos `[Description]` tornam-se ferramentas disponíveis para o agente
3. **Contexto da Conversação**: A gestão de sessões permite conversas com múltiplas interações e consciência total do contexto
4. **Gestão de Configuração**: Variáveis de ambiente e gestão segura de credenciais seguem as melhores práticas .NET
5. **API Azure OpenAI Responses**: O agente usa a API Azure OpenAI Responses através do SDK Azure.AI.OpenAI

## 🔗 Recursos Adicionais

- [Documentação Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI na Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->