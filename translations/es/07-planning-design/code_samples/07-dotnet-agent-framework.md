# 🎯 Planificación y Patrones de Diseño con Azure OpenAI (API de Respuestas) (.NET)

## 📋 Objetivos de Aprendizaje

Este cuaderno demuestra patrones de planificación y diseño de nivel empresarial para construir agentes inteligentes utilizando el Microsoft Agent Framework en .NET con Azure OpenAI (API de Respuestas). Aprenderás a crear agentes que pueden descomponer problemas complejos, planificar soluciones de múltiples pasos y ejecutar flujos de trabajo sofisticados con las características empresariales de .NET.

## ⚙️ Prerrequisitos y Configuración

**Entorno de Desarrollo:**
- SDK .NET 9.0 o superior
- Visual Studio 2022 o VS Code con la extensión de C#
- Una suscripción a Azure con un recurso Azure OpenAI y un despliegue de modelo
- La CLI de Azure — iniciar sesión con `az login`

**Dependencias Requeridas:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuración del Entorno (archivo .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Ejecución del Código

Esta lección incluye una implementación de aplicación de archivo único en .NET. Para ejecutarla:

```bash
# Haz el archivo ejecutable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Ejecuta la aplicación
./07-dotnet-agent-framework.cs
```

O usa el comando dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementación del Código

La implementación completa está disponible en `07-dotnet-agent-framework.cs`, la cual demuestra:

- Carga de la configuración del entorno con DotNetEnv
- Configuración del cliente Azure OpenAI y creación de un agente AI usando `GetChatClient().AsAIAgent()`
- Definición de modelos de datos estructurados (Plan y TravelPlan) con serialización JSON
- Creación de un agente AI con salida estructurada usando esquema JSON
- Ejecución de solicitudes de planificación con respuestas tipadas de forma segura

## Conceptos Clave

### Planificación Estructurada con Modelos Tipados

El agente usa clases de C# para definir la estructura de las salidas de planificación:

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

El agente está configurado para devolver respuestas que coinciden con el esquema TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
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

El agente actúa como coordinador, delegando tareas a subagentes especializados:

- FlightBooking: Para reservar vuelos y proporcionar información de vuelos
- HotelBooking: Para reservar hoteles y proporcionar información de hoteles
- CarRental: Para reservar coches y proporcionar información de alquiler de coches
- ActivitiesBooking: Para reservar actividades y proporcionar información de actividades
- DestinationInfo: Para proporcionar información sobre destinos
- DefaultAgent: Para manejar solicitudes generales

## Resultado Esperado

Cuando ejecutes el agente con una solicitud de planificación de viaje, analizará la solicitud y generará un plan estructurado con asignaciones de tareas apropiadas a agentes especializados, formateado en JSON conforme al esquema TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->