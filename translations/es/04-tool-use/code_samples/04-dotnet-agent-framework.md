<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:20:41+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "es"
}
-->
# 🛠️ Uso Avanzado de Herramientas con Modelos de GitHub (.NET)

## 📋 Objetivos de Aprendizaje

Este cuaderno demuestra patrones de integración de herramientas de nivel empresarial utilizando el Microsoft Agent Framework en .NET con Modelos de GitHub. Aprenderás a construir agentes sofisticados con múltiples herramientas especializadas, aprovechando la tipificación fuerte de C# y las características empresariales de .NET.

**Capacidades Avanzadas de Herramientas que Dominarás:**
- 🔧 **Arquitectura Multi-Herramienta**: Construcción de agentes con múltiples capacidades especializadas
- 🎯 **Ejecución de Herramientas con Tipos Seguros**: Aprovechando la validación en tiempo de compilación de C#
- 📊 **Patrones de Herramientas Empresariales**: Diseño de herramientas listas para producción y manejo de errores
- 🔗 **Composición de Herramientas**: Combinación de herramientas para flujos de trabajo empresariales complejos

## 🎯 Beneficios de la Arquitectura de Herramientas en .NET

### Características de Herramientas Empresariales
- **Validación en Tiempo de Compilación**: La tipificación fuerte asegura la corrección de los parámetros de las herramientas
- **Inyección de Dependencias**: Integración de contenedores IoC para la gestión de herramientas
- **Patrones Async/Await**: Ejecución de herramientas sin bloqueo con gestión adecuada de recursos
- **Registro Estructurado**: Integración de registro incorporado para monitoreo de la ejecución de herramientas

### Patrones Listos para Producción
- **Manejo de Excepciones**: Gestión integral de errores con excepciones tipadas
- **Gestión de Recursos**: Patrones adecuados de eliminación y gestión de memoria
- **Monitoreo de Rendimiento**: Métricas incorporadas y contadores de rendimiento
- **Gestión de Configuración**: Configuración con tipos seguros y validación

## 🔧 Arquitectura Técnica

### Componentes Principales de Herramientas en .NET
- **Microsoft.Extensions.AI**: Capa de abstracción unificada para herramientas
- **Microsoft.Agents.AI**: Orquestación de herramientas de nivel empresarial
- **Integración con Modelos de GitHub**: Cliente API de alto rendimiento con agrupación de conexiones

### Pipeline de Ejecución de Herramientas
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Categorías y Patrones de Herramientas

### 1. **Herramientas de Procesamiento de Datos**
- **Validación de Entrada**: Tipificación fuerte con anotaciones de datos
- **Operaciones de Transformación**: Conversión y formato de datos con tipos seguros
- **Lógica Empresarial**: Herramientas de cálculo y análisis específicas del dominio
- **Formato de Salida**: Generación estructurada de respuestas

### 2. **Herramientas de Integración**
- **Conectores API**: Integración de servicios RESTful con HttpClient
- **Herramientas de Base de Datos**: Integración de Entity Framework para acceso a datos
- **Operaciones de Archivos**: Operaciones seguras en el sistema de archivos con validación
- **Servicios Externos**: Patrones de integración con servicios de terceros

### 3. **Herramientas Utilitarias**
- **Procesamiento de Texto**: Utilidades de manipulación y formato de cadenas
- **Operaciones de Fecha/Hora**: Cálculos de fecha/hora sensibles a la cultura
- **Herramientas Matemáticas**: Cálculos de precisión y operaciones estadísticas
- **Herramientas de Validación**: Validación de reglas empresariales y verificación de datos

## ⚙️ Prerrequisitos y Configuración

**Entorno de Desarrollo:**
- SDK de .NET 9.0 o superior
- Visual Studio 2022 o VS Code con extensión de C#
- Acceso a la API de Modelos de GitHub

**Paquetes NuGet Requeridos:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuración de Entorno (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

¿Listo para construir agentes de nivel empresarial con capacidades de herramientas potentes y seguras en .NET? ¡Vamos a diseñar soluciones de nivel profesional! 🏢⚡

## 💻 Implementación de Código

La implementación completa en C# está disponible en el archivo complementario `04-dotnet-agent-framework.cs`. Esta aplicación de archivo único en .NET demuestra:

- Carga de variables de entorno para la configuración de Modelos de GitHub
- Definición de herramientas personalizadas utilizando métodos de C# con atributos
- Creación de un agente de IA con integración de herramientas
- Gestión de hilos de conversación
- Ejecución de solicitudes del agente con invocación de herramientas

Para ejecutar el ejemplo:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

O utilizando la CLI de .NET:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.