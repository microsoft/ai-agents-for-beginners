# 🎯 Planificación y Patrones de Diseño con Azure OpenAI (Responses API) (.NET)

## 📋 Objetivos de Aprendizaje

Este cuaderno demuestra patrones de planificación y diseño de grado empresarial para construir agentes inteligentes usando el Microsoft Agent Framework en .NET con Azure OpenAI (Responses API). Aprenderás a crear agentes que pueden descomponer problemas complejos, planificar soluciones en múltiples pasos y ejecutar flujos de trabajo sofisticados con las características empresariales de .NET.

## ⚙️ Requisitos Previos y Configuración

**Entorno de Desarrollo:**
- SDK .NET 9.0 o superior
- Visual Studio 2022 o VS Code con la extensión de C#
- Una suscripción de Azure con un recurso de Azure OpenAI y un despliegue de modelo
- La CLI de Azure — inicia sesión con `az login`

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
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## Ejecutando el Código

Esta lección incluye una implementación de una aplicación de archivo único de .NET. Para ejecutarla:

```bash
# Hacer el archivo ejecutable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Ejecutar la aplicación
./07-dotnet-agent-framework.cs
```

O usa el comando dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementación del Código

La implementación completa está disponible en `07-dotnet-agent-framework.cs`, que demuestra:

- Cargar la configuración del entorno con DotNetEnv
- Configurar el cliente Azure OpenAI y crear un agente de IA usando `GetChatClient().AsAIAgent()`
- Definir modelos de datos estructurados (Plan y TravelPlan) con serialización JSON
- Crear un agente de IA con salida estructurada usando esquema JSON
- Ejecutar solicitudes de planificación con respuestas tipo seguro

## Conceptos Clave

### Planificación Estructurada con Modelos Tipo Seguro

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

### Instrucciones para el Agente de Planificación

El agente actúa como coordinador, delegando tareas a subagentes especializados:

- FlightBooking: Para reservar vuelos y proporcionar información de vuelos
- HotelBooking: Para reservar hoteles y proporcionar información de hoteles
- CarRental: Para alquilar coches y proporcionar información de alquiler de coches
- ActivitiesBooking: Para reservar actividades y proporcionar información de actividades
- DestinationInfo: Para proporcionar información sobre destinos
- DefaultAgent: Para manejar solicitudes generales

## Salida Esperada

Cuando ejecutes el agente con una solicitud de planificación de viaje, analizará la petición y generará un plan estructurado con asignaciones de tareas apropiadas a los agentes especializados, formateado como JSON conforme al esquema TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->