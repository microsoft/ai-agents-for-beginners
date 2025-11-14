<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:13:10+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "es"
}
-->
# 🤝 Sistemas de flujo de trabajo multiagente para empresas (.NET)

## 📋 Objetivos de aprendizaje

Este cuaderno demuestra cómo construir sistemas multiagente sofisticados de nivel empresarial utilizando el Microsoft Agent Framework en .NET con Modelos de GitHub. Aprenderás a orquestar múltiples agentes especializados trabajando juntos a través de flujos de trabajo estructurados, aprovechando las características empresariales de .NET para soluciones listas para producción.

**Capacidades multiagente empresariales que desarrollarás:**
- 👥 **Colaboración entre agentes**: Coordinación de agentes con validación en tiempo de compilación
- 🔄 **Orquestación de flujos de trabajo**: Definición declarativa de flujos de trabajo con patrones asincrónicos de .NET
- 🎭 **Especialización de roles**: Personalidades de agentes fuertemente tipadas y dominios de especialización
- 🏢 **Integración empresarial**: Patrones listos para producción con monitoreo y manejo de errores

## ⚙️ Requisitos previos y configuración

**Entorno de desarrollo:**
- SDK de .NET 9.0 o superior
- Visual Studio 2022 o VS Code con la extensión de C#
- Suscripción a Azure (para agentes persistentes)

**Paquetes NuGet requeridos:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Ejemplo de código

El código completo para esta lección está disponible en el archivo C# adjunto: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Para ejecutar el ejemplo:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

O utilizando la CLI de .NET:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Qué demuestra este ejemplo

Este sistema de flujo de trabajo multiagente crea un servicio de recomendaciones de viajes para hoteles con dos agentes especializados:

1. **Agente FrontDesk**: Un agente de viajes que proporciona recomendaciones de actividades y ubicaciones
2. **Agente Concierge**: Revisa las recomendaciones para garantizar experiencias auténticas y no turísticas

Los agentes trabajan juntos en un flujo de trabajo donde:
- El agente FrontDesk recibe la solicitud inicial de viaje
- El agente Concierge revisa y refina la recomendación
- El flujo de trabajo transmite respuestas en tiempo real

## Conceptos clave

### Coordinación entre agentes
El ejemplo demuestra la coordinación de agentes con validación en tiempo de compilación utilizando el Microsoft Agent Framework.

### Orquestación de flujos de trabajo
Utiliza la definición declarativa de flujos de trabajo con patrones asincrónicos de .NET para conectar múltiples agentes en una canalización.

### Respuestas en tiempo real
Implementa la transmisión en tiempo real de respuestas de agentes utilizando enumerables asincrónicos y arquitectura basada en eventos.

### Integración empresarial
Muestra patrones listos para producción, incluyendo:
- Configuración de variables de entorno
- Gestión segura de credenciales
- Manejo de errores
- Procesamiento de eventos asincrónicos

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.