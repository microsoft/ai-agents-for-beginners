<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:54:15+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "es"
}
-->
# 🎯 Planificación y Patrones de Diseño con Modelos de GitHub (.NET)

## 📋 Objetivos de Aprendizaje

Este cuaderno demuestra patrones de planificación y diseño de nivel empresarial para construir agentes inteligentes utilizando el Microsoft Agent Framework en .NET con Modelos de GitHub. Aprenderás a crear agentes que puedan descomponer problemas complejos, planificar soluciones de múltiples pasos y ejecutar flujos de trabajo sofisticados con las características empresariales de .NET.

## ⚙️ Prerrequisitos y Configuración

**Entorno de Desarrollo:**
- SDK de .NET 9.0 o superior
- Visual Studio 2022 o VS Code con la extensión de C#
- Acceso a la API de Modelos de GitHub

**Dependencias Requeridas:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuración del Entorno (archivo .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Ejecución del Código

Esta lección incluye una implementación de aplicación de archivo único en .NET. Para ejecutarla:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

O utiliza el comando dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementación del Código

La implementación completa está disponible en `07-dotnet-agent-framework.cs`, que demuestra:

- Carga de configuración del entorno con DotNetEnv
- Configuración del cliente OpenAI para Modelos de GitHub
- Definición de modelos de datos estructurados (Plan y TravelPlan) con serialización JSON
- Creación de un agente de IA con salida estructurada utilizando un esquema JSON
- Ejecución de solicitudes de planificación con respuestas de tipo seguro

## Conceptos Clave

### Planificación Estructurada con Modelos de Tipo Seguro

El agente utiliza clases de C# para definir la estructura de las salidas de planificación:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### Esquema JSON para Salidas Estructuradas

El agente está configurado para devolver respuestas que coincidan con el esquema TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Instrucciones del Agente de Planificación

El agente actúa como coordinador, delegando tareas a sub-agentes especializados:

- FlightBooking: Para reservar vuelos y proporcionar información sobre vuelos
- HotelBooking: Para reservar hoteles y proporcionar información sobre hoteles
- CarRental: Para reservar autos y proporcionar información sobre alquiler de autos
- ActivitiesBooking: Para reservar actividades y proporcionar información sobre actividades
- DestinationInfo: Para proporcionar información sobre destinos
- DefaultAgent: Para manejar solicitudes generales

## Salida Esperada

Cuando ejecutes el agente con una solicitud de planificación de viaje, analizará la solicitud y generará un plan estructurado con asignaciones de tareas apropiadas a agentes especializados, formateado como JSON conforme al esquema TravelPlan.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.