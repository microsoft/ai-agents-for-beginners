<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-05-21T09:35:30+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "es"
}
-->
# Lección 11: Integración del Model Context Protocol (MCP)

## Introducción al Model Context Protocol (MCP)

El Model Context Protocol (MCP) es un marco innovador diseñado para estandarizar las interacciones entre modelos de IA y aplicaciones cliente. MCP funciona como un puente entre los modelos de IA y las aplicaciones que los utilizan, proporcionando una interfaz consistente sin importar la implementación subyacente del modelo.

Aspectos clave de MCP:

- **Comunicación Estandarizada**: MCP establece un lenguaje común para que las aplicaciones se comuniquen con los modelos de IA
- **Gestión Mejorada del Contexto**: Permite pasar información contextual a los modelos de IA de manera eficiente
- **Compatibilidad Multiplataforma**: Funciona con varios lenguajes de programación como C#, Java, JavaScript, Python y TypeScript
- **Integración Fluida**: Facilita a los desarrolladores integrar distintos modelos de IA en sus aplicaciones

MCP es especialmente valioso en el desarrollo de agentes de IA, ya que permite que los agentes interactúen con diversos sistemas y fuentes de datos mediante un protocolo unificado, haciendo que los agentes sean más flexibles y potentes.

## Objetivos de Aprendizaje
- Comprender qué es MCP y su papel en el desarrollo de agentes de IA
- Configurar y poner en marcha un servidor MCP para integración con GitHub
- Construir un sistema multi-agente usando herramientas MCP
- Implementar RAG (Retrieval Augmented Generation) con Azure Cognitive Search

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
   - Crear un recurso de Azure Cognitive Search
   - Configurar el servicio Azure OpenAI
   - Establecer variables de entorno en `.env`

3. **Configuración del Servidor MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Estructura del Proyecto

```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## Componentes Principales

### 1. Sistema Multi-Agente
- GitHub Agent: Análisis de repositorios
- Hackathon Agent: Recomendaciones de proyectos
- Events Agent: Sugerencias de eventos tecnológicos

### 2. Integración con Azure
- Cognitive Search para indexación de eventos
- Azure OpenAI para inteligencia de agentes
- Implementación del patrón RAG

### 3. Herramientas MCP
- Análisis de repositorios GitHub
- Inspección de código
- Extracción de metadatos

## Recorrido por el Código

El ejemplo muestra:
1. Integración del servidor MCP
2. Orquestación multi-agente
3. Integración con Azure Cognitive Search
4. Implementación del patrón RAG

Características clave:
- Análisis en tiempo real de repositorios GitHub
- Recomendaciones inteligentes de proyectos
- Coincidencia de eventos usando Azure Search
- Respuestas en streaming con Chainlit

## Ejecución del Ejemplo

Para instrucciones detalladas de configuración y más información, consulta el [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Iniciar el servidor MCP:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Lanzar la aplicación:
   ```bash
   chainlit run app.py -w
   ```

3. Probar la integración:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Solución de Problemas

Problemas comunes y soluciones:
1. Problemas de conexión MCP
   - Verificar que el servidor esté activo
   - Comprobar disponibilidad del puerto
   - Confirmar los tokens de GitHub

2. Problemas con Azure Search
   - Validar cadenas de conexión
   - Verificar existencia del índice
   - Confirmar la carga de documentos

## Próximos Pasos
- Explorar herramientas MCP adicionales
- Implementar agentes personalizados
- Mejorar capacidades de RAG
- Añadir más fuentes de eventos

## Recursos
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.