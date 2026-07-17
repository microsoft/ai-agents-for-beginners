[![Explorando Frameworks de Agentes de IA](../../../translated_images/es/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Explorar Frameworks de Agentes de IA

Los frameworks de agentes de IA son plataformas de software diseñadas para simplificar la creación, implementación y gestión de agentes de IA. Estos frameworks proporcionan a los desarrolladores componentes preconstruidos, abstracciones y herramientas que agilizan el desarrollo de sistemas de IA complejos.

Estos frameworks ayudan a los desarrolladores a centrarse en los aspectos únicos de sus aplicaciones al proporcionar enfoques estandarizados para los desafíos comunes en el desarrollo de agentes de IA. Mejoran la escalabilidad, accesibilidad y eficiencia en la construcción de sistemas de IA.

## Introducción 

Esta lección cubrirá:

- ¿Qué son los Frameworks de Agentes de IA y qué permiten lograr a los desarrolladores?
- ¿Cómo pueden los equipos usar estos para prototipar rápidamente, iterar y mejorar las capacidades de su agente?
- ¿Cuáles son las diferencias entre los frameworks y herramientas creados por Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> y el <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- ¿Puedo integrar directamente mis herramientas existentes del ecosistema Azure, o necesito soluciones independientes?
- ¿Qué es Microsoft Foundry Agent Service y cómo me está ayudando?

## Objetivos de aprendizaje

Los objetivos de esta lección son ayudarte a entender:

- El papel de los Frameworks de Agentes de IA en el desarrollo de IA.
- Cómo aprovechar los Frameworks de Agentes de IA para construir agentes inteligentes.
- Capacidades clave habilitadas por los Frameworks de Agentes de IA.
- Las diferencias entre Microsoft Agent Framework y Microsoft Foundry Agent Service.

## ¿Qué son los Frameworks de Agentes de IA y qué permiten hacer a los desarrolladores?

Los Frameworks tradicionales de IA pueden ayudarte a integrar IA en tus aplicaciones y mejorar estas aplicaciones de las siguientes maneras:

- **Personalización**: La IA puede analizar el comportamiento y preferencias del usuario para proporcionar recomendaciones, contenido y experiencias personalizadas.
Ejemplo: Servicios de streaming como Netflix usan IA para sugerir películas y programas basados en el historial de visualización, mejorando el compromiso y la satisfacción del usuario.
- **Automatización y eficiencia**: La IA puede automatizar tareas repetitivas, optimizar flujos de trabajo y mejorar la eficiencia operativa.
Ejemplo: Las aplicaciones de atención al cliente usan chatbots impulsados por IA para manejar consultas comunes, reduciendo tiempos de respuesta y liberando agentes humanos para problemas más complejos.
- **Mejora de la experiencia del usuario**: La IA puede mejorar la experiencia general del usuario ofreciendo funciones inteligentes como reconocimiento de voz, procesamiento de lenguaje natural y texto predictivo.
Ejemplo: Asistentes virtuales como Siri y Google Assistant usan IA para entender y responder comandos de voz, facilitando la interacción de los usuarios con sus dispositivos.

### Todo eso suena genial, ¿entonces por qué necesitamos el Framework de Agentes de IA?

Los frameworks de agentes de IA representan algo más que simples frameworks de IA. Están diseñados para habilitar la creación de agentes inteligentes que pueden interactuar con usuarios, otros agentes y el entorno para alcanzar objetivos específicos. Estos agentes pueden exhibir comportamiento autónomo, tomar decisiones y adaptarse a condiciones cambiantes. Veamos algunas capacidades clave habilitadas por los frameworks de agentes de IA:

- **Colaboración y coordinación de agentes**: Permitir la creación de múltiples agentes de IA que puedan trabajar juntos, comunicarse y coordinarse para resolver tareas complejas.
- **Automatización y gestión de tareas**: Proporcionar mecanismos para automatizar flujos de trabajo de múltiples pasos, delegación de tareas y gestión dinámica de tareas entre agentes.
- **Comprensión contextual y adaptación**: Equipar a los agentes con la capacidad de entender el contexto, adaptarse a entornos cambiantes y tomar decisiones basadas en información en tiempo real.

En resumen, los agentes te permiten hacer más, llevar la automatización al siguiente nivel, crear sistemas más inteligentes que pueden adaptarse y aprender de su entorno.

## ¿Cómo prototipar rápidamente, iterar y mejorar las capacidades del agente?

Este es un campo en rápido movimiento, pero hay algunas cosas comunes en la mayoría de los Frameworks de Agentes de IA que pueden ayudarte a prototipar e iterar rápidamente, principalmente componentes modulares, herramientas colaborativas y aprendizaje en tiempo real. Vamos a profundizar en estos aspectos:

- **Usar Componentes Modulares**: Los SDK de IA ofrecen componentes preconstruidos como conectores de IA y memoria, llamadas a funciones usando lenguaje natural o complementos de código, plantillas de indicaciones y más.
- **Aprovechar Herramientas Colaborativas**: Diseñar agentes con roles y tareas específicas, permitiéndoles probar y perfeccionar flujos de trabajo colaborativos.
- **Aprender en Tiempo Real**: Implementar bucles de retroalimentación donde los agentes aprenden de las interacciones y ajustan su comportamiento dinámicamente.

### Usar Componentes Modulares

SDKs como Microsoft Agent Framework ofrecen componentes preconstruidos como conectores de IA, definiciones de herramientas y gestión de agentes.

**Cómo pueden usar esto los equipos**: Los equipos pueden armar rápidamente estos componentes para crear un prototipo funcional sin empezar desde cero, permitiendo una experimentación e iteración rápidas.

**Cómo funciona en la práctica**: Puedes usar un parser preconstruido para extraer información de la entrada del usuario, un módulo de memoria para almacenar y recuperar datos, y un generador de indicaciones para interactuar con los usuarios, todo sin necesidad de construir estos componentes desde cero.

**Código de ejemplo**. Veamos un ejemplo de cómo usar Microsoft Agent Framework con `FoundryChatClient` para que el modelo responda a la entrada del usuario mediante llamadas a herramientas:

``` python
# Ejemplo de Python del Marco de Agente de Microsoft

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definir una función de herramienta de muestra para reservar viajes
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Salida de ejemplo: Su vuelo a Nueva York el 1 de enero de 2025 ha sido reservado con éxito. ¡Buen viaje! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Lo que se observa en este ejemplo es cómo puedes aprovechar un parser preconstruido para extraer información clave de la entrada del usuario, como origen, destino y fecha de una solicitud de reserva de vuelo. Este enfoque modular te permite enfocarte en la lógica de alto nivel.

### Aprovechar Herramientas Colaborativas

Frameworks como Microsoft Agent Framework facilitan la creación de múltiples agentes que pueden trabajar en conjunto.

**Cómo pueden usar esto los equipos**: Los equipos pueden diseñar agentes con roles y tareas específicas, permitiéndoles probar y perfeccionar flujos de trabajo colaborativos y mejorar la eficiencia del sistema global.

**Cómo funciona en la práctica**: Puedes crear un equipo de agentes donde cada agente tenga una función especializada, como recuperación de datos, análisis o toma de decisiones. Estos agentes pueden comunicarse y compartir información para alcanzar un objetivo común, como responder a una consulta de usuario o completar una tarea.

**Código de ejemplo (Microsoft Agent Framework)**:

```python
# Creando múltiples agentes que trabajan juntos usando el Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Agente de Recuperación de Datos
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agente de Análisis de Datos
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Ejecutar agentes en secuencia en una tarea
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Lo que ves en el código anterior es cómo puedes crear una tarea que involucra múltiples agentes trabajando juntos para analizar datos. Cada agente realiza una función específica, y la tarea se ejecuta coordinando a los agentes para lograr el resultado deseado. Creando agentes dedicados con roles especializados, puedes mejorar la eficiencia y el rendimiento de las tareas.

### Aprender en Tiempo Real

Frameworks avanzados proporcionan capacidades para comprensión contextual y adaptación en tiempo real.

**Cómo pueden usar esto los equipos**: Los equipos pueden implementar bucles de retroalimentación donde los agentes aprenden de las interacciones y ajustan su comportamiento dinámicamente, conduciendo a una mejora y refinamiento continuo de las capacidades.

**Cómo funciona en la práctica**: Los agentes pueden analizar la retroalimentación del usuario, datos ambientales y resultados de tareas para actualizar su base de conocimientos, ajustar algoritmos de toma de decisiones y mejorar el rendimiento con el tiempo. Este proceso iterativo de aprendizaje permite a los agentes adaptarse a condiciones cambiantes y preferencias de los usuarios, mejorando la efectividad general del sistema.

## ¿Cuáles son las diferencias entre Microsoft Agent Framework y Microsoft Foundry Agent Service?

Hay muchas formas de comparar estos enfoques, pero veamos algunas diferencias clave en términos de diseño, capacidades y casos de uso objetivo:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework proporciona un SDK simplificado para construir agentes de IA usando `FoundryChatClient`. Permite a los desarrolladores crear agentes que aprovechan modelos de Azure OpenAI con llamadas integradas a herramientas, gestión de conversaciones y seguridad de nivel empresarial mediante identidad Azure.

**Casos de uso**: Construcción de agentes de IA listos para producción con uso de herramientas, flujos de trabajo de múltiples pasos y escenarios de integración empresarial.

Aquí algunos conceptos clave del Microsoft Agent Framework:

- **Agentes**. Un agente se crea mediante `FoundryChatClient` y se configura con un nombre, instrucciones y herramientas. El agente puede:
  - **Procesar mensajes de usuario** y generar respuestas usando modelos Azure OpenAI.
  - **Llamar herramientas** automáticamente según el contexto de la conversación.
  - **Mantener el estado de la conversación** a lo largo de múltiples interacciones.

  Aquí hay un fragmento de código que muestra cómo crear un agente:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Herramientas**. El framework soporta definir herramientas como funciones Python que el agente puede invocar automáticamente. Las herramientas se registran al crear el agente:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Coordinación Multi-Agente**. Puedes crear múltiples agentes con diferentes especializaciones y coordinar su trabajo:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Integración de Identidad Azure**. El framework usa `AzureCliCredential` (o `DefaultAzureCredential`) para autenticación segura sin clave, eliminando la necesidad de gestionar claves API directamente.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service es una adición más reciente, introducida en Microsoft Ignite 2024. Permite el desarrollo y despliegue de agentes de IA con modelos más flexibles, como llamadas directas a LLMs de código abierto como Llama 3, Mistral y Cohere.

Microsoft Foundry Agent Service ofrece mecanismos más robustos de seguridad empresarial y métodos de almacenamiento de datos, haciéndolo adecuado para aplicaciones empresariales.

Funciona listo para usarse con Microsoft Agent Framework para construir y desplegar agentes.

Este servicio está actualmente en Vista Previa Pública y soporta Python y C# para construir agentes.

Usando el SDK Python de Microsoft Foundry Agent Service, podemos crear un agente con una herramienta definida por el usuario:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definir funciones de herramientas
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Conceptos clave

Microsoft Foundry Agent Service tiene los siguientes conceptos clave:

- **Agente**. Microsoft Foundry Agent Service se integra con Microsoft Foundry. Dentro de Foundry, un Agente de IA actúa como un microservicio "inteligente" que puede usarse para responder preguntas (RAG), realizar acciones o automatizar flujos de trabajo completos. Logra esto combinando el poder de modelos generativos de IA con herramientas que le permiten acceder e interactuar con fuentes de datos del mundo real. Aquí un ejemplo de un agente:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    En este ejemplo, un agente es creado con el modelo `gpt-4.1-mini`, un nombre `my-agent`, y las instrucciones `Eres un agente útil`. El agente está equipado con herramientas y recursos para realizar tareas de interpretación de código.

- **Hilo y mensajes**. El hilo es otro concepto importante. Representa una conversación o interacción entre un agente y un usuario. Los hilos pueden usarse para rastrear el progreso de una conversación, almacenar información de contexto y gestionar el estado de la interacción. Aquí un ejemplo de un hilo:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Pídale al agente que realice trabajo en el hilo
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Recupere y registre todos los mensajes para ver la respuesta del agente
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    En el código anterior, se crea un hilo. Luego, se envía un mensaje al hilo. Al llamar a `create_and_process_run`, se le pide al agente realizar trabajo en el hilo. Finalmente, se recuperan y registran los mensajes para ver la respuesta del agente. Los mensajes indican el progreso de la conversación entre el usuario y el agente. También es importante entender que los mensajes pueden ser de diferentes tipos como texto, imagen o archivo, que es el resultado del trabajo de los agentes, por ejemplo una imagen o una respuesta de texto. Como desarrollador, puedes usar esta información para procesar la respuesta o presentarla al usuario.

- **Se integra con Microsoft Agent Framework**. Microsoft Foundry Agent Service funciona perfectamente con Microsoft Agent Framework, lo que significa que puedes construir agentes usando `FoundryChatClient` y desplegarlos a través del Agent Service para escenarios de producción.

**Casos de uso**: Microsoft Foundry Agent Service está diseñado para aplicaciones empresariales que requieren despliegue de agentes de IA seguro, escalable y flexible.

## ¿Cuál es la diferencia entre estos enfoques?
 
Parece que hay solapamiento, pero hay diferencias clave en términos de diseño, capacidades y casos de uso:
 
- **Microsoft Agent Framework (MAF)**: Es un SDK listo para producción para construir agentes de IA. Proporciona una API simplificada para crear agentes con llamadas a herramientas, gestión de conversaciones e integración de identidad Azure.
- **Microsoft Foundry Agent Service**: Es una plataforma y servicio de despliegue en Microsoft Foundry para agentes. Ofrece conectividad incorporada a servicios como Azure OpenAI, Azure AI Search, Bing Search y ejecución de código.
 
¿Aún no sabes cuál elegir?

### Casos de Uso
 
Veamos si podemos ayudarte repasando algunos casos comunes:
 
> P: Estoy construyendo aplicaciones de agentes IA para producción y quiero empezar rápido
>

>R: Microsoft Agent Framework es una excelente opción. Proporciona una API sencilla y Pythonica vía `FoundryChatClient` que permite definir agentes con herramientas e instrucciones en solo unas pocas líneas de código.

>P: Necesito despliegue de nivel empresarial con integraciones Azure como Search y ejecución de código
>
> R: Microsoft Foundry Agent Service es la mejor opción. Es un servicio de plataforma que ofrece capacidades integradas para múltiples modelos, Azure AI Search, Bing Search y Azure Functions. Facilita construir tus agentes en el Portal Foundry y desplegarlos a escala.
 
> P: Aún estoy confundido, solo dame una opción
>
> R: Comienza con Microsoft Agent Framework para construir tus agentes y luego usa Microsoft Foundry Agent Service cuando necesites desplegarlos y escalarlos en producción. Este enfoque te permite iterar rápido en la lógica de tu agente mientras tienes un camino claro hacia el despliegue empresarial.
 
Resumamos las diferencias clave en una tabla:

| Framework | Enfoque | Conceptos Clave | Casos de Uso |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK simplificado con llamadas a herramientas | Agentes, Herramientas, Identidad Azure | Construcción de agentes IA, uso de herramientas, flujos multi-paso |
| Microsoft Foundry Agent Service | Modelos flexibles, seguridad empresarial, generación de código, llamada a herramientas | Modularidad, Colaboración, Orquestación de procesos | Despliegue seguro, escalable y flexible de agentes IA |

## ¿Puedo integrar directamente mis herramientas existentes del ecosistema Azure, o necesito soluciones independientes?


La respuesta es sí, puede integrar sus herramientas existentes del ecosistema Azure directamente con Microsoft Foundry Agent Service especialmente, ya que ha sido construido para trabajar perfectamente con otros servicios de Azure. Por ejemplo, podría integrar Bing, Azure AI Search y Azure Functions. También existe una integración profunda con Microsoft Foundry.

El Microsoft Agent Framework también se integra con los servicios de Azure a través de `FoundryChatClient` e identidad de Azure, lo que le permite llamar a los servicios de Azure directamente desde sus herramientas de agente.

## Códigos de muestra

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## ¿Tiene más preguntas sobre AI Agent Frameworks?

Únase a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrarse con otros aprendices, asistir a horas de oficina y obtener respuestas a sus preguntas sobre los Agentes de IA.

## Referencias

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Lección anterior

[Introducción a Agentes de IA y Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

## Próxima lección

[Comprendiendo los Patrones de Diseño Agentes](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->