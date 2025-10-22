<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T14:50:22+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "es"
}
-->
# Ejemplo de Servidor MCP de Github

## Descripción

Esta es una demostración creada para el Hackathon de Agentes de IA organizado a través de Microsoft Reactor.

La herramienta se utiliza para recomendar proyectos de hackathon basados en los repositorios de Github de un usuario. Esto se logra mediante:

1. **Agente de Github** - Utiliza el Servidor MCP de Github para recuperar repositorios e información sobre esos repositorios.
2. **Agente de Hackathon** - Toma los datos del Agente de Github y genera ideas creativas de proyectos de hackathon basadas en los proyectos, los lenguajes utilizados por el usuario y las categorías del hackathon de Agentes de IA.
3. **Agente de Eventos** - Basándose en las sugerencias del agente de hackathon, el agente de eventos recomendará eventos relevantes de la serie de hackathons de Agentes de IA.

## Ejecutando el código 

### Variables de entorno

Esta demostración utiliza Azure Open AI Service, Semantic Kernel, el Servidor MCP de Github y Azure AI Search.

Asegúrate de tener configuradas las variables de entorno necesarias para usar estas herramientas:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Ejecutando el Servidor Chainlit

Para conectarse al servidor MCP, esta demostración utiliza Chainlit como interfaz de chat.

Para ejecutar el servidor, utiliza el siguiente comando en tu terminal:

```bash
chainlit run app.py -w
```

Esto debería iniciar tu servidor Chainlit en `localhost:8000` y también poblar tu Índice de Búsqueda de Azure AI con el contenido de `event-descriptions.md`.

## Conectándose al Servidor MCP

Para conectarte al Servidor MCP de Github, selecciona el ícono de "enchufe" debajo del cuadro de texto "Escribe tu mensaje aquí...":

![Conexión MCP](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.es.png)

Desde allí, puedes hacer clic en "Conectar un MCP" para agregar el comando que conecta al Servidor MCP de Github:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Sustituye "[YOUR PERSONAL ACCESS TOKEN]" por tu Token de Acceso Personal real.

Después de conectarte, deberías ver un (1) junto al ícono de enchufe para confirmar que está conectado. Si no, intenta reiniciar el servidor Chainlit con `chainlit run app.py -w`.

## Usando la Demostración 

Para iniciar el flujo de trabajo del agente para recomendar proyectos de hackathon, puedes escribir un mensaje como:

"Recomienda proyectos de hackathon para el usuario de Github koreyspace"

El Agente Router analizará tu solicitud y determinará qué combinación de agentes (GitHub, Hackathon y Eventos) es la más adecuada para manejar tu consulta. Los agentes trabajan juntos para proporcionar recomendaciones completas basadas en el análisis de repositorios de Github, la ideación de proyectos y eventos tecnológicos relevantes.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.