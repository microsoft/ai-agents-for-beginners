<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:34:53+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "br"
}
-->
# 🔍 Explorando Frameworks de Agentes - Agente Básico (.NET)

## 📋 Objetivos de Aprendizado

Este notebook explora os conceitos fundamentais do Microsoft Agent Framework por meio de uma implementação básica de agente em .NET. Você aprenderá padrões essenciais de agentes e entenderá como agentes inteligentes funcionam internamente usando C# e o ecossistema .NET.

**O que você vai descobrir:**
- 🏗️ **Arquitetura de Agentes**: Compreendendo a estrutura básica de agentes de IA em .NET
- 🛠️ **Integração de Ferramentas**: Como os agentes utilizam funções externas para ampliar suas capacidades  
- 💬 **Fluxo de Conversação**: Gerenciando conversas de múltiplas etapas e contexto com gerenciamento de threads
- 🔧 **Padrões de Configuração**: Melhores práticas para configuração e gerenciamento de agentes em .NET

## 🎯 Conceitos-Chave Abordados

### Princípios do Framework de Agentes
- **Autonomia**: Como os agentes tomam decisões independentes usando abstrações de IA do .NET
- **Reatividade**: Respondendo a mudanças no ambiente e entradas do usuário
- **Proatividade**: Tomando iniciativas com base em objetivos e contexto
- **Habilidade Social**: Interagindo por meio de linguagem natural com threads de conversação

### Componentes Técnicos
- **AIAgent**: Orquestração central de agentes e gerenciamento de conversação (.NET)
- **Funções de Ferramentas**: Ampliando as capacidades do agente com métodos e atributos em C#
- **Integração com OpenAI**: Aproveitando modelos de linguagem por meio de APIs padronizadas do .NET
- **Gerenciamento de Ambiente**: Configuração segura e manipulação de credenciais com DotNetEnv

## ⚙️ Pré-requisitos e Configuração

**Dependências Necessárias:**
- SDK .NET 9.0 ou superior
- Visual Studio 2022 ou VS Code com extensão C#

**Pacotes NuGet:**
- `Microsoft.Extensions.AI` - Abstrações principais de IA
- `Microsoft.Extensions.AI.OpenAI` - Integração com OpenAI (preview)
- `DotNetEnv` - Gerenciamento de variáveis de ambiente

**Configuração de Ambiente (arquivo .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Stack Técnico

**Tecnologias Principais:**
- Microsoft Agent Framework (.NET)
- Integração com API de Modelos do GitHub
- Padrões de cliente compatíveis com OpenAI
- Configuração baseada em ambiente com DotNetEnv

**Capacidades do Agente:**
- Compreensão e geração de linguagem natural
- Chamadas de função e uso de ferramentas com atributos em C#
- Respostas sensíveis ao contexto com threads de conversação
- Arquitetura extensível com padrões de injeção de dependência

## 📚 Comparação de Frameworks

Este exemplo demonstra a abordagem do Microsoft Agent Framework em .NET em comparação com outras plataformas:

| Recurso | Framework de Agente .NET | Equivalentes em Python |
|---------|--------------------------|------------------------|
| **Segurança de Tipos** | Tipagem forte com C# | Tipagem dinâmica |
| **Integração** | Ecossistema nativo do .NET | Compatibilidade variada |
| **Desempenho** | Desempenho de código compilado | Execução interpretada |
| **Pronto para Empresas** | Construído para aplicativos .NET de produção | Varia conforme o framework |
| **Ferramentas** | Integração com Visual Studio | Dependente de IDE |

## 🚀 Começando

Siga as células abaixo para construir seu primeiro agente básico em .NET e entender os conceitos fundamentais de agentes!

## 📦 Instalação e Configuração

Este exemplo está disponível como um aplicativo executável de arquivo único em .NET. Veja o arquivo `02-dotnet-agent-framework.cs` que acompanha para a implementação completa.

Para executar este exemplo:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Ou usando o CLI do dotnet:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Passo a Passo do Código

A implementação completa inclui:

### 1. Dependências de Pacotes

```csharp
// Core AI abstraction layer for .NET applications
#r "nuget: Microsoft.Extensions.AI, 9.9.1"

// Microsoft Agent Framework OpenAI integration
#r "nuget: Microsoft.Agents.AI.OpenAI, 1.0.0-preview.251001.3"

// Core Microsoft Agent Framework library
#r "nuget: Microsoft.Agents.AI, 1.0.0-preview.251001.3"

// Environment variable management
#r "nuget: DotNetEnv, 3.1.1"
```

### 2. Importações Essenciais

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Configuração de Ambiente

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definição de Funções de Ferramentas

```csharp
// Random destination generator tool
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
```

### 5. Configuração e Inicialização do Cliente

```csharp
// Extract environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? 
    throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? 
    throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client for GitHub Models
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI client
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);
```

### 6. Configuração do Agente

```csharp
const string AGENT_NAME = "TravelAgent";

const string AGENT_INSTRUCTIONS = @"You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
""Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?""

Always prioritize user preferences. If they mention a specific destination like ""Bali"" or ""Paris,"" focus your planning on that location rather than suggesting alternatives.
";
```

### 7. Inicialização do Agente

```csharp
// Create AI agent with travel planning capabilities
AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions)
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create((Func<string>)GetRandomDestination)]
    );
```

### 8. Gerenciamento de Conversação

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Principais Lições

1. **Arquitetura de Agentes**: O Microsoft Agent Framework oferece uma abordagem limpa e com segurança de tipos para construir agentes de IA em .NET
2. **Integração de Ferramentas**: Funções decoradas com atributos `[Description]` tornam-se ferramentas disponíveis para o agente
3. **Contexto de Conversação**: O gerenciamento de threads permite conversas de múltiplas etapas com total consciência de contexto
4. **Gerenciamento de Configuração**: Variáveis de ambiente e manipulação segura de credenciais seguem as melhores práticas do .NET
5. **Compatibilidade com OpenAI**: A integração com Modelos do GitHub funciona perfeitamente por meio de APIs compatíveis com OpenAI

## 🔗 Recursos Adicionais

- [Documentação do Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [Marketplace de Modelos do GitHub](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [Aplicativos de Arquivo Único .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.