# 🎨 Padrões de Design Agentic com Azure OpenAI (Responses API) (.NET)

## 📋 Objetivos de Aprendizagem

Este exemplo demonstra padrões de design de nível empresarial para construir agentes inteligentes usando o Microsoft Agent Framework em .NET com integração Azure OpenAI (Responses API). Aprenderá padrões profissionais e abordagens arquitetónicas que tornam os agentes prontos para produção, fáceis de manter e escaláveis.

### Padrões de Design Empresariais

- 🏭 **Padrão Factory**: Criação de agentes padronizada com injeção de dependências
- 🔧 **Padrão Builder**: Configuração e montagem fluente de agentes
- 🧵 **Padrões Thread-Safe**: Gestão concorrente de conversações
- 📋 **Padrão Repository**: Gestão organizada de ferramentas e capacidades

## 🎯 Benefícios Arquitetónicos Específicos do .NET

### Funcionalidades Empresariais

- **Tipagem Forte**: Validação em tempo de compilação e suporte IntelliSense
- **Injeção de Dependências**: Integração com contentor DI incorporado
- **Gestão de Configuração**: Padrões IConfiguration e Options
- **Async/Await**: Suporte de primeira classe para programação assíncrona

### Padrões Prontos para Produção

- **Integração de Logging**: ILogger e suporte a logging estruturado
- **Health Checks**: Monitorização e diagnósticos incorporados
- **Validação de Configuração**: Tipagem forte com data annotations
- **Tratamento de Erros**: Gestão estruturada de exceções

## 🔧 Arquitetura Técnica

### Componentes Principais do .NET

- **Microsoft.Extensions.AI**: Abstrações unificadas de serviços AI
- **Microsoft.Agents.AI**: Framework empresarial de orquestração de agentes
- **Azure OpenAI (Responses API)**: Padrões de clientes API de alta performance
- **Sistema de Configuração**: appsettings.json e integração ambiental

### Implementação do Padrão de Design

```mermaid
graph LR
    A[IServiceCollection] --> B[Construtor de Agentes]
    B --> C[Configuração]
    C --> D[Registo de Ferramentas]
    D --> E[Agente de IA]
```

## 🏗️ Padrões Empresariais Demonstrados

### 1. **Padrões Criacionais**

- **Agent Factory**: Criação centralizada de agentes com configuração consistente
- **Padrão Builder**: API fluente para configuração complexa de agentes
- **Padrão Singleton**: Gestão de recursos e configuração partilhados
- **Injeção de Dependências**: Baixo acoplamento e testabilidade

### 2. **Padrões Comportamentais**

- **Padrão Strategy**: Estratégias intercambiáveis de execução de ferramentas
- **Padrão Command**: Operações do agente encapsuladas com undo/redo
- **Padrão Observer**: Gestão de ciclo de vida do agente dirigida por eventos
- **Template Method**: Fluxos de trabalho de execução do agente padronizados

### 3. **Padrões Estruturais**

- **Padrão Adapter**: Camada de integração Azure OpenAI (Responses API)
- **Padrão Decorator**: Melhoria das capacidades do agente
- **Padrão Facade**: Interfaces simplificadas de interação com o agente
- **Padrão Proxy**: Lazy loading e caching para performance

## 📚 Princípios de Design do .NET

### Princípios SOLID

- **Single Responsibility**: Cada componente tem uma finalidade clara
- **Open/Closed**: Extensível sem modificação
- **Liskov Substitution**: Implementações de ferramentas baseadas em interfaces
- **Interface Segregation**: Interfaces focadas e coesas
- **Dependency Inversion**: Dependência de abstrações, não de concretizações

### Clean Architecture

- **Domain Layer**: Abstrações centrais de agente e ferramentas
- **Application Layer**: Orquestração do agente e fluxos de trabalho
- **Infrastructure Layer**: Integração Azure OpenAI (Responses API) e serviços externos
- **Presentation Layer**: Interação do utilizador e formatação de respostas

## 🔒 Considerações Empresariais

### Segurança

- **Gestão de Credenciais**: Gestão segura de chaves API com IConfiguration
- **Validação de Entrada**: Tipagem forte e validação com data annotations
- **Sanitização de Saída**: Processamento e filtro seguro das respostas
- **Logging de Auditoria**: Rastreio abrangente das operações

### Performance

- **Padrões Async**: Operações I/O não bloqueantes
- **Connection Pooling**: Gestão eficiente do cliente HTTP
- **Caching**: Cache das respostas para melhorar performance
- **Gestão de Recursos**: Padrões adequados de descarte e limpeza

### Escalabilidade

- **Thread Safety**: Suporte à execução concorrente de agentes
- **Pooling de Recursos**: Utilização eficiente de recursos
- **Gestão de Carga**: Limitação de taxa e gestão de backpressure
- **Monitorização**: Métricas de performance e health checks

## 🚀 Implementação em Produção

- **Gestão de Configuração**: Definições específicas para o ambiente
- **Estratégia de Logging**: Logging estruturado com IDs de correlação
- **Tratamento de Erros**: Gestão global de exceções com recuperação adequada
- **Monitorização**: Application insights e contadores de performance
- **Testes**: Testes unitários, integração e de carga

Pronto para construir agentes inteligentes de nível empresarial com .NET? Vamos arquitetar algo robusto! 🏢✨

## 🚀 Começar

### Pré-requisitos

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ou superior
- Uma [assinatura Azure](https://azure.microsoft.com/free/) com um recurso Azure OpenAI e um deployment de modelo
- A [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — iniciar sessão com `az login`

### Variáveis de Ambiente Necessárias

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Depois inicie sessão para que o AzureCliCredential possa obter um token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Em seguida, inicie sessão para que o AzureCliCredential possa obter um token
az login
```

### Código de Exemplo

Para executar o exemplo de código,

```bash
# zsh/bash
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

Ou usando a CLI dotnet:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

Veja [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) para o código completo.

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

// Create New Conversation Session for Context Management
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
var session = await agent.CreateSessionAsync();

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->