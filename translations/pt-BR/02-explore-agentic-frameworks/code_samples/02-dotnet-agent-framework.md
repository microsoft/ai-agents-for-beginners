# 🔍 Explorando o Microsoft Agent Framework - Agente Básico (.NET)

## 📋 Objetivos de Aprendizagem

Este exemplo explora os conceitos fundamentais do Microsoft Agent Framework por meio de uma implementação básica de agente em .NET. Você aprenderá padrões centrais agenticos e entenderá como agentes inteligentes funcionam internamente usando C# e o ecossistema .NET.

### O que Você Vai Descobrir

- 🏗️ **Arquitetura do Agente**: Entendendo a estrutura básica dos agentes de IA em .NET
- 🛠️ **Integração de Ferramentas**: Como agentes usam funções externas para ampliar capacidades  
- 💬 **Fluxo de Conversação**: Gerenciando conversas multi-turno e contexto com gerenciamento de threads
- 🔧 **Padrões de Configuração**: Melhores práticas para configuração e gerenciamento do agente em .NET

## 🎯 Conceitos Principais Abordados

### Princípios do Framework Agentico

- **Autonomia**: Como agentes tomam decisões independentes usando abstrações de IA em .NET
- **Reatividade**: Respondendo a mudanças ambientais e entradas do usuário
- **Proatividade**: Tomando iniciativa com base em objetivos e contexto
- **Habilidade Social**: Interagindo por meio de linguagem natural com threads de conversação

### Componentes Técnicos

- **AIAgent**: Core de orquestração do agente e gerenciamento de conversação (.NET)
- **Funções de Ferramentas**: Ampliando capacidades do agente com métodos e atributos C#
- **Integração Azure OpenAI**: Aproveitando modelos de linguagem via API Azure OpenAI Responses
- **Configuração Segura**: Gerenciamento de endpoints baseado em ambiente

## 🔧 Pilha Técnica

### Tecnologias Principais

- Microsoft Agent Framework (.NET)
- Integração Azure OpenAI (API Responses)
- Padrões do cliente Azure.AI.OpenAI
- Configuração baseada em ambiente com DotNetEnv

### Capacidades do Agente

- Compreensão e geração de linguagem natural
- Chamadas de funções e uso de ferramentas com atributos C#
- Respostas cientes do contexto com sessões de conversação
- Arquitetura extensível com padrões de injeção de dependência

## 📚 Comparação de Frameworks

Este exemplo demonstra a abordagem do Microsoft Agent Framework em comparação com outros frameworks agenticos:

| Recurso | Microsoft Agent Framework | Outros Frameworks |
|---------|-------------------------|------------------|
| **Integração** | Ecossistema Microsoft nativo | Compatibilidade variada |
| **Simplicidade** | API limpa e intuitiva | Configuração frequentemente complexa |
| **Extensibilidade** | Integração fácil de ferramentas | Depende do framework |
| **Pronto para Empresas** | Construído para produção | Varia conforme o framework |

## 🚀 Começando

### Pré-requisitos

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ou superior
- Uma [assinatura Azure](https://azure.microsoft.com/free/) com um recurso Azure OpenAI e implantação de modelo
- O [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — faça login com `az login`

### Variáveis de Ambiente Necessárias

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Então faça login para que o AzureCliCredential possa obter um token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Em seguida, faça login para que o AzureCliCredential possa obter um token
az login
```

### Código de Exemplo

Para executar o exemplo de código,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Ou usando a CLI do dotnet:

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

## 🎓 Principais Conclusões

1. **Arquitetura do Agente**: O Microsoft Agent Framework fornece uma abordagem limpa e com segurança de tipos para construir agentes de IA em .NET
2. **Integração de Ferramentas**: Funções decoradas com atributos `[Description]` se tornam ferramentas disponíveis para o agente
3. **Contexto da Conversação**: O gerenciamento de sessões permite conversas multi-turno com total consciência do contexto
4. **Gerenciamento de Configuração**: Variáveis de ambiente e tratamento seguro de credenciais seguem as melhores práticas do .NET
5. **API Azure OpenAI Responses**: O agente usa a API Azure OpenAI Responses através do SDK Azure.AI.OpenAI

## 🔗 Recursos Adicionais

- [Documentação Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI na Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->