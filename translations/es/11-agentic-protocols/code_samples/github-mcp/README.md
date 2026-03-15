# Ejemplo de Servidor MCP de Github

## Descripción

Esta fue una demostración creada para el Hackathon de Agentes de IA organizado a través del Microsoft Reactor.

La herramienta se utiliza para recomendar proyectos de hackathon basados en los repositorios de Github de un usuario.
Esto se realiza mediante:

1. **Agente de Github** - Usando el Servidor MCP de Github para recuperar repositorios e información sobre esos repositorios.
2. **Agente de Hackathon** - Toma los datos del Agente de Github y propone ideas creativas de proyectos para hackathon basadas en los proyectos, los lenguajes usados por el usuario y las categorías de proyecto para el hackathon de Agentes de IA.
3. **Agente de Eventos** - Basado en la sugerencia del agente de hackathon, el agente de eventos recomendará eventos relevantes de la serie Hackathon de Agentes de IA.

## Ejecutando el código 

### Variables de Entorno

Esta demostración usa el Microsoft Agent Framework, Azure OpenAI Service, el Servidor MCP de Github y Azure AI Search.

Asegúrate de tener las variables de entorno adecuadas configuradas para usar estas herramientas:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## Ejecutando el Servidor Chainlit

Para conectarse al servidor MCP, esta demostración utiliza Chainlit como interfaz de chat.

Para ejecutar el servidor, usa el siguiente comando en tu terminal:

```bash
chainlit run app.py -w
```


Esto debería iniciar tu servidor Chainlit en `localhost:8000` así como llenar tu índice de Azure AI Search con el contenido de `event-descriptions.md`.

## Conectándose al Servidor MCP

Para conectarte al Servidor MCP de Github, selecciona el icono de "enchufe" debajo del cuadro de chat "Escribe tu mensaje aquí..":

![MCP Connect](../../../../../translated_images/es/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Desde allí puedes hacer clic en "Connect an MCP" para añadir el comando que conecta con el Servidor MCP de Github:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


Reemplaza "[YOUR PERSONAL ACCESS TOKEN]" con tu Token de Acceso Personal real.

Después de conectarte, deberías ver un (1) junto al icono del enchufe confirmando que está conectado. Si no, intenta reiniciar el servidor chainlit con `chainlit run app.py -w`.

## Usando la Demostración 

Para iniciar el flujo de trabajo del agente para recomendar proyectos de hackathon, puedes escribir un mensaje como:

"Recomienda proyectos de hackathon para el usuario de Github koreyspace"

El Agente Router analizará tu solicitud y determinará qué combinación de agentes (GitHub, Hackathon y Eventos) es la más adecuada para manejar tu consulta. Los agentes trabajan juntos para proporcionar recomendaciones comprensivas basadas en el análisis de repositorios de GitHub, ideación de proyectos y eventos tecnológicos relevantes.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->