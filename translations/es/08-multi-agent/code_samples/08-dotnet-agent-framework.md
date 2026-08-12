# 🤝 Sistemas de Flujo de Trabajo Multiagente Empresariales (.NET)

## 📋 Objetivos de Aprendizaje

Este cuaderno demuestra cómo construir sistemas multiagente sofisticados de nivel empresarial usando el Microsoft Agent Framework en .NET con Azure OpenAI (API de respuestas). Aprenderás a orquestar múltiples agentes especializados trabajando juntos mediante flujos de trabajo estructurados, aprovechando las características empresariales de .NET para soluciones listas para producción.

**Capacidades Multiagente Empresariales que Construirás:**
- 👥 **Colaboración de Agentes**: Coordinación de agentes con tipado seguro y validación en tiempo de compilación
- 🔄 **Orquestación de Flujos de Trabajo**: Definición declarativa de flujos de trabajo con patrones async de .NET
- 🎭 **Especialización de Roles**: Personalidades de agentes fuertemente tipadas y dominios de experiencia
- 🏢 **Integración Empresarial**: Patrones listos para producción con monitoreo y manejo de errores

## ⚙️ Requisitos y Configuración

**Entorno de Desarrollo:**
- SDK de .NET 9.0 o superior
- Visual Studio 2022 o VS Code con extensión de C#
- Suscripción de Azure (para agentes persistentes)

**Paquetes NuGet Requeridos:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Ejemplo de Código

El código completo y funcional para esta lección está disponible en el archivo C# adjunto: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Para ejecutar el ejemplo:

```bash
# Hacer el archivo ejecutable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Ejecutar el ejemplo
./08-dotnet-agent-framework.cs
```

O usando la CLI de .NET:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Qué Demuestra Este Ejemplo

Este sistema de flujo de trabajo multiagente crea un servicio de recomendación de viajes para hoteles con dos agentes especializados:

1. **Agente de Recepción**: Un agente de viajes que proporciona recomendaciones de actividades y ubicaciones
2. **Agente Concierge**: Revisa las recomendaciones para asegurar experiencias auténticas y no turísticas

Los agentes trabajan juntos en un flujo de trabajo donde:
- El agente de Recepción recibe la solicitud de viaje inicial
- El agente Concierge revisa y refina la recomendación
- El flujo de trabajo transmite respuestas en tiempo real

## Conceptos Clave

### Coordinación de Agentes
El ejemplo demuestra la coordinación de agentes con tipado seguro usando el Microsoft Agent Framework con validación en tiempo de compilación.

### Orquestación de Flujos de Trabajo
Usa definición declarativa de flujos de trabajo con patrones async de .NET para conectar múltiples agentes en un pipeline.

### Transmisión de Respuestas
Implementa transmisión en tiempo real de respuestas de agentes usando enumerables async y arquitectura orientada a eventos.

### Integración Empresarial
Muestra patrones listos para producción incluyendo:
- Configuración mediante variables de entorno
- Gestión segura de credenciales
- Manejo de errores
- Procesamiento asíncrono de eventos

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->