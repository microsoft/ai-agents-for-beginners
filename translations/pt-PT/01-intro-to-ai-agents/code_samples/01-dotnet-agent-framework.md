# 🌍 Agente de Viagens IA com Microsoft Agent Framework (.NET)

## 📋 Visão Geral do Cenário

Este exemplo demonstra como construir um agente inteligente de planeamento de viagens usando o Microsoft Agent Framework para .NET. O agente pode gerar automaticamente roteiros personalizados de excursões de um dia para destinos aleatórios em todo o mundo.

### Capacidades Principais:

- 🎲 **Seleção Aleatória de Destinos**: Utiliza uma ferramenta personalizada para escolher locais de férias
- 🗺️ **Planeamento Inteligente de Viagens**: Cria itinerários detalhados dia a dia
- 🔄 **Streaming em Tempo Real**: Suporta respostas imediatas e em streaming
- 🛠️ **Integração de Ferramentas Personalizadas**: Demonstra como ampliar as capacidades do agente

## 🔧 Arquitetura Técnica

### Tecnologias Principais

- **Microsoft Agent Framework**: Implementação mais recente para desenvolvimento de agentes IA em .NET
- **Azure OpenAI (API de Respostas)**: Usa a API de Respostas do Azure OpenAI para inferência de modelos
- **Azure Identity**: Autenticação segura via `AzureCliCredential` (`az login`)
- **Configuração Segura**: Gestão de endpoints baseada no ambiente

### Componentes-Chave

1. **AIAgent**: O orquestrador principal que gere o fluxo da conversa
2. **Ferramentas Personalizadas**: Função `GetRandomDestination()` disponível para o agente
3. **Cliente de Respostas**: Interface de conversação baseada em Azure OpenAI Responses
4. **Suporte a Streaming**: Capacidades de geração de respostas em tempo real

### Padrão de Integração

```mermaid
graph LR
    A[Pedido do Utilizador] --> B[Agente de IA]
    B --> C[Azure OpenAI (API de Respostas)]
    B --> D[Ferramenta GetRandomDestination]
    C --> E[Itinerário de Viagem]
    D --> E
```

## 🚀 Começar

### Pré-requisitos

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ou superior
- Uma [subscrição Azure](https://azure.microsoft.com/free/) com um recurso Azure OpenAI e um deployment de modelo
- O [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — iniciar sessão com `az login`

### Variáveis de Ambiente Necessárias

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Em seguida, inicie sessão para que o AzureCliCredential possa obter um token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Depois inicie sessão para que o AzureCliCredential possa obter um token
az login
```

### Código de Exemplo

Para executar o exemplo de código,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Ou usar o dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Veja [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) para o código completo.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.4.1
#:package Microsoft.Agents.AI.OpenAI@1.1.0
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip
// Run the agent with streaming enabled for real-time response display
// Shows the agent's thinking and response as it generates the content
// Provides better user experience with immediate feedback
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Conclusões Principais

1. **Arquitetura do Agente**: O Microsoft Agent Framework oferece uma abordagem limpa e tipada para construir agentes IA em .NET
2. **Integração de Ferramentas**: Funções decoradas com atributos `[Description]` tornam-se ferramentas disponíveis para o agente
3. **Gestão de Configuração**: Variáveis de ambiente e tratamento seguro de credenciais seguem as melhores práticas .NET
4. **Azure OpenAI Responses API**: O agente usa a API Azure OpenAI Responses através do SDK Azure.AI.OpenAI

## 🔗 Recursos Adicionais

- [Documentação do Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI no Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Aplicações .NET de Ficheiro Único](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->