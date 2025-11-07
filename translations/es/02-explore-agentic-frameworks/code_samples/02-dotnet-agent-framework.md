<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:30:38+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "es"
}
-->
# 🔍 Explorando Marcos Agénticos - Agente Básico (.NET)

## 📋 Objetivos de Aprendizaje

Este cuaderno explora los conceptos fundamentales del Marco de Agentes de Microsoft a través de una implementación básica de un agente en .NET. Aprenderás patrones agénticos esenciales y comprenderás cómo funcionan los agentes inteligentes detrás de escena utilizando C# y el ecosistema .NET.

**Lo que descubrirás:**
- 🏗️ **Arquitectura de Agentes**: Comprender la estructura básica de los agentes de IA en .NET
- 🛠️ **Integración de Herramientas**: Cómo los agentes utilizan funciones externas para ampliar capacidades  
- 💬 **Flujo de Conversación**: Gestionar conversaciones de múltiples turnos y contexto con manejo de hilos
- 🔧 **Patrones de Configuración**: Mejores prácticas para la configuración y gestión de agentes en .NET

## 🎯 Conceptos Clave Cubiertos

### Principios del Marco Agéntico
- **Autonomía**: Cómo los agentes toman decisiones independientes utilizando abstracciones de IA en .NET
- **Reactividad**: Responder a cambios en el entorno y entradas del usuario
- **Proactividad**: Tomar la iniciativa basada en objetivos y contexto
- **Habilidad Social**: Interactuar mediante lenguaje natural con hilos de conversación

### Componentes Técnicos
- **AIAgent**: Orquestación central del agente y gestión de conversaciones (.NET)
- **Funciones de Herramientas**: Ampliar las capacidades del agente con métodos y atributos de C#
- **Integración con OpenAI**: Aprovechar modelos de lenguaje a través de APIs estandarizadas de .NET
- **Gestión del Entorno**: Configuración segura y manejo de credenciales con DotNetEnv

## ⚙️ Requisitos Previos y Configuración

**Dependencias Requeridas:**
- SDK de .NET 9.0 o superior
- Visual Studio 2022 o VS Code con extensión de C#

**Paquetes NuGet:**
- `Microsoft.Extensions.AI` - Abstracciones principales de IA
- `Microsoft.Extensions.AI.OpenAI` - Integración con OpenAI (versión preliminar)
- `DotNetEnv` - Gestión de variables de entorno

**Configuración del Entorno (archivo .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Stack Técnico

**Tecnologías Principales:**
- Marco de Agentes de Microsoft (.NET)
- Integración con API de Modelos de GitHub
- Patrones de cliente compatibles con OpenAI
- Configuración basada en entorno con DotNetEnv

**Capacidades del Agente:**
- Comprensión y generación de lenguaje natural
- Llamadas a funciones y uso de herramientas con atributos de C#
- Respuestas conscientes del contexto con hilos de conversación
- Arquitectura extensible con patrones de inyección de dependencias

## 📚 Comparación de Marcos

Este ejemplo demuestra el enfoque del Marco de Agentes de Microsoft en .NET en comparación con otras plataformas:

| Característica | Marco de Agentes en .NET | Equivalentes en Python |
|----------------|--------------------------|-------------------------|
| **Seguridad de Tipos** | Tipado fuerte con C# | Tipado dinámico |
| **Integración** | Ecosistema nativo de .NET | Compatibilidad variada |
| **Rendimiento** | Código compilado | Ejecución interpretada |
| **Preparado para Empresas** | Diseñado para aplicaciones de producción en .NET | Varía según el marco |
| **Herramientas** | Integración con Visual Studio | Dependiente del IDE |

## 🚀 Comenzando

Sigue las celdas a continuación para construir tu primer agente básico en .NET y comprender los conceptos agénticos fundamentales.

## 📦 Instalación y Configuración

Este ejemplo está disponible como una aplicación ejecutable de archivo único en .NET. Consulta el archivo `02-dotnet-agent-framework.cs` adjunto para la implementación completa.

Para ejecutar este ejemplo:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

O utilizando la CLI de dotnet:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Recorrido por el Código

La implementación completa incluye:

### 1. Dependencias de Paquetes

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

### 2. Importaciones Esenciales

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Configuración del Entorno

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definición de Funciones de Herramientas

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

### 5. Configuración y Cliente

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

### 6. Configuración del Agente

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

### 7. Inicialización del Agente

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

### 8. Gestión de Conversaciones

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Conclusiones Clave

1. **Arquitectura de Agentes**: El Marco de Agentes de Microsoft proporciona un enfoque limpio y seguro para construir agentes de IA en .NET
2. **Integración de Herramientas**: Las funciones decoradas con atributos `[Description]` se convierten en herramientas disponibles para el agente
3. **Contexto de Conversación**: La gestión de hilos permite conversaciones de múltiples turnos con plena conciencia del contexto
4. **Gestión de Configuración**: Las variables de entorno y el manejo seguro de credenciales siguen las mejores prácticas de .NET
5. **Compatibilidad con OpenAI**: La integración con Modelos de GitHub funciona perfectamente a través de APIs compatibles con OpenAI

## 🔗 Recursos Adicionales

- [Documentación del Marco de Agentes de Microsoft](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [Marketplace de Modelos de GitHub](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [Aplicaciones de Archivo Único en .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.