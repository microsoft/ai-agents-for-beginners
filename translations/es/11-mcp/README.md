<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T07:34:45+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "es"
}
-->
# Lección 11: Integración del Protocolo de Contexto de Modelo (MCP)

## Introducción al Protocolo de Contexto de Modelo (MCP)

El Protocolo de Contexto de Modelo (MCP) es un marco innovador diseñado para estandarizar las interacciones entre modelos de IA y aplicaciones cliente. MCP actúa como un puente entre los modelos de IA y las aplicaciones que los utilizan, proporcionando una interfaz consistente sin importar la implementación subyacente del modelo.

Aspectos clave de MCP:

- **Comunicación Estandarizada**: MCP establece un lenguaje común para que las aplicaciones se comuniquen con los modelos de IA.
- **Gestión Mejorada del Contexto**: Permite el paso eficiente de información contextual a los modelos de IA.
- **Compatibilidad Multiplataforma**: Funciona en varios lenguajes de programación, incluidos C#, Java, JavaScript, Python y TypeScript.
- **Integración Sin Esfuerzo**: Facilita a los desarrolladores la integración de diferentes modelos de IA en sus aplicaciones.

MCP es especialmente valioso en el desarrollo de agentes de IA, ya que permite a los agentes interactuar con diversos sistemas y fuentes de datos a través de un protocolo unificado, haciendo que los agentes sean más flexibles y potentes.

## Objetivos de Aprendizaje
- Comprender qué es MCP y su papel en el desarrollo de agentes de IA.
- Configurar y configurar un servidor MCP para la integración con GitHub.
- Construir un sistema multiagente utilizando herramientas MCP.
- Implementar RAG (Generación Aumentada por Recuperación) con Azure Cognitive Search.

## Requisitos Previos
- Python 3.8+
- Node.js 14+
- Suscripción a Azure
- Cuenta de GitHub
- Conocimientos básicos de Semantic Kernel

## Instrucciones de Configuración

1. **Configuración del Entorno**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configurar Servicios de Azure**
   - Crear un recurso de Azure Cognitive Search.
   - Configurar el servicio Azure OpenAI.
   - Configurar las variables de entorno en `.env`.

3. **Configuración del Servidor MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Estructura del Proyecto

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## Componentes Principales

### 1. Sistema Multiagente
- Agente de GitHub: Análisis de repositorios.
- Agente de Hackathon: Recomendaciones de proyectos.
- Agente de Eventos: Sugerencias de eventos tecnológicos.

### 2. Integración con Azure
- Cognitive Search para indexación de eventos.
- Azure OpenAI para inteligencia de agentes.
- Implementación del patrón RAG.

### 3. Herramientas MCP
- Análisis de repositorios de GitHub.
- Inspección de código.
- Extracción de metadatos.

## Recorrido por el Código

El ejemplo demuestra:
1. Integración del servidor MCP.
2. Orquestación de múltiples agentes.
3. Integración con Azure Cognitive Search.
4. Implementación del patrón RAG.

Características clave:
- Análisis en tiempo real de repositorios de GitHub.
- Recomendaciones inteligentes de proyectos.
- Emparejamiento de eventos utilizando Azure Search.
- Respuestas en tiempo real con Chainlit.

## Ejecución del Ejemplo

Para obtener instrucciones detalladas de configuración y más información, consulta el [README del Ejemplo del Servidor MCP en GitHub](./code_samples/github-mcp/README.md).

1. Inicia el servidor MCP:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Lanza la aplicación:
   ```bash
   chainlit run app.py -w
   ```

3. Prueba la integración:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Resolución de Problemas

Problemas comunes y soluciones:
1. Problemas de Conexión MCP
   - Verifica que el servidor esté en ejecución.
   - Comprueba la disponibilidad del puerto.
   - Confirma los tokens de GitHub.

2. Problemas con Azure Search
   - Valida las cadenas de conexión.
   - Verifica la existencia del índice.
   - Confirma la carga de documentos.

## Próximos Pasos
- Explorar herramientas adicionales de MCP.
- Implementar agentes personalizados.
- Mejorar las capacidades de RAG.
- Agregar más fuentes de eventos.
- **Avanzado**: Consulta [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) para ejemplos de comunicación entre agentes.

## Recursos
- [MCP para Principiantes](https://aka.ms/mcp-for-beginners)  
- [Documentación de MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Documentación de Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Guías de Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.