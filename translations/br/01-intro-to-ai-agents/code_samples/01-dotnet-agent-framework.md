<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "23afd9be7b6ba5b69a44c3b6a78e07f6",
  "translation_date": "2025-11-06T10:03:42+00:00",
  "source_file": "01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.md",
  "language_code": "br"
}
-->
# 🌍 Agente de Viagem com Microsoft Agent Framework (.NET)

## 📋 Visão Geral do Cenário

Este notebook demonstra como criar um agente inteligente de planejamento de viagens usando o Microsoft Agent Framework para .NET. O agente pode gerar automaticamente roteiros personalizados de viagens de um dia para destinos aleatórios ao redor do mundo.

**Principais Capacidades:**
- 🎲 **Seleção Aleatória de Destinos**: Utiliza uma ferramenta personalizada para escolher locais de férias
- 🗺️ **Planejamento Inteligente de Viagens**: Cria roteiros detalhados dia a dia
- 🔄 **Streaming em Tempo Real**: Suporta respostas imediatas e em streaming
- 🛠️ **Integração de Ferramentas Personalizadas**: Demonstra como ampliar as capacidades do agente

## 🔧 Arquitetura Técnica

### Tecnologias Principais
- **Microsoft Agent Framework**: Implementação mais recente do .NET para desenvolvimento de agentes de IA
- **Integração com Modelos do GitHub**: Utiliza o serviço de inferência de modelos de IA do GitHub
- **Compatibilidade com API OpenAI**: Aproveita as bibliotecas cliente da OpenAI com endpoints personalizados
- **Configuração Segura**: Gerenciamento de chaves de API baseado em ambiente

### Componentes Principais
1. **AIAgent**: O orquestrador principal do agente que gerencia o fluxo de conversação
2. **Ferramentas Personalizadas**: Função `GetRandomDestination()` disponível para o agente
3. **Cliente de Chat**: Interface de conversação baseada em modelos do GitHub
4. **Suporte a Streaming**: Capacidades de geração de respostas em tempo real

### Padrão de Integração
```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 Primeiros Passos

**Pré-requisitos:**
- .NET 10.0 ou superior
- Token de acesso à API de Modelos do GitHub
- Variáveis de ambiente configuradas no arquivo `.env`

**Variáveis de Ambiente Necessárias:**
```env
GITHUB_TOKEN=your_github_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Execute o exemplo de código abaixo em sequência para ver o agente de viagem em ação!

---

## Aplicativo Único .NET: Exemplo de Agente de Viagem com IA

Veja `01-dotnet-agent-framework.cs` para o exemplo completo de código executável.

```bash
dotnet run 01-dotnet-agent-framework.cs
```

### Código de Exemplo

```csharp
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

// Extract configuration from environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI Client Options
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Create AI Agent with Travel Planning Capabilities
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip (Non-Streaming)
Console.WriteLine(await agent.RunAsync("Plan me a day trip"));

// Execute Agent: Plan a Day Trip (Streaming Response)
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    Console.Write(update);
}
```

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.