# Desarrollo del servicio Microsoft Foundry Agent

En este ejercicio, usas las herramientas de Microsoft Foundry Agent Service en el [portal Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) para crear un agente para Reserva de Vuelos. El agente podrá interactuar con los usuarios y proporcionar información sobre vuelos.

## Requisitos previos

Para completar este ejercicio, necesitas lo siguiente:
1. Una cuenta de Azure con una suscripción activa. [Crea una cuenta gratis](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Necesitas permisos para crear un hub de Microsoft Foundry o que te lo creen.
    - Si tu rol es Colaborador o Propietario, puedes seguir los pasos en este tutorial.

## Crear un hub de Microsoft Foundry

> **Nota:** Microsoft Foundry era anteriormente conocido como Azure AI Studio.

1. Sigue estas directrices del artículo del blog de [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) para crear un hub de Microsoft Foundry.
2. Cuando tu proyecto esté creado, cierra cualquier sugerencia que se muestre y revisa la página del proyecto en el portal Microsoft Foundry, que debería verse similar a la imagen siguiente:

    ![Microsoft Foundry Project](../../../translated_images/es/azure-ai-foundry.88d0c35298348c2f.webp)

## Desplegar un modelo

1. En el panel izquierdo de tu proyecto, en la sección **Mis recursos**, selecciona la página **Modelos + puntos de conexión**.
2. En la página **Modelos + puntos de conexión**, en la pestaña **Despliegues de modelo**, en el menú **+ Desplegar modelo**, selecciona **Desplegar modelo base**.
3. Busca el modelo `gpt-4.1-mini` en la lista, luego selecciónalo y confirma.

    > **Nota**: Reducir el TPM ayuda a evitar usar en exceso la cuota disponible en la suscripción que estás utilizando.

    ![Model Deployed](../../../translated_images/es/model-deployment.3749c53fb81e18fd.webp)

## Crear un agente

Ahora que has desplegado un modelo, puedes crear un agente. Un agente es un modelo de IA conversacional que se puede usar para interactuar con los usuarios.

1. En el panel izquierdo de tu proyecto, en la sección **Construir y personalizar**, selecciona la página **Agentes**.
2. Haz clic en **+ Crear agente** para crear un nuevo agente. En el cuadro de diálogo **Configuración del agente**:
    - Ingresa un nombre para el agente, como `FlightAgent`.
    - Asegúrate de que el despliegue del modelo `gpt-4.1-mini` que creaste anteriormente esté seleccionado.
    - Establece las **Instrucciones** según el prompt que quieras que el agente siga. Aquí hay un ejemplo:
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> Para un prompt detallado, puedes consultar [este repositorio](https://github.com/ShivamGoyal03/RoamMind) para más información.
    
> Además, puedes agregar **Base de conocimientos** y **Acciones** para mejorar las capacidades del agente para proporcionar más información y realizar tareas automáticas según las solicitudes de los usuarios. Para este ejercicio, puedes omitir estos pasos.
    
![Agent Setup](../../../translated_images/es/agent-setup.9bbb8755bf5df672.webp)

3. Para crear un nuevo agente multi-IA, simplemente haz clic en **Nuevo agente**. El agente recién creado entonces se mostrará en la página de Agentes.


## Probar el agente

Después de crear el agente, puedes probarlo para ver cómo responde a las consultas de los usuarios en el entorno de pruebas del portal Microsoft Foundry.

1. En la parte superior del panel **Configuración** para tu agente, selecciona **Probar en entorno de pruebas**.
2. En el panel **Entorno de pruebas**, puedes interactuar con el agente escribiendo consultas en la ventana de chat. Por ejemplo, puedes pedir al agente que busque vuelos de Seattle a Nueva York para el día 28.

    > **Nota**: El agente puede no proporcionar respuestas exactas, ya que no se usan datos en tiempo real en este ejercicio. El propósito es probar la capacidad del agente para entender y responder a las consultas de los usuarios según las instrucciones proporcionadas.

    ![Agent Playground](../../../translated_images/es/agent-playground.dc146586de715010.webp)

3. Después de probar el agente, puedes personalizarlo más agregando más intenciones, datos de entrenamiento y acciones para mejorar sus capacidades.

## Limpiar recursos

Cuando hayas terminado de probar el agente, puedes eliminarlo para evitar incurrir en costos adicionales.
1. Abre el [portal de Azure](https://portal.azure.com) y revisa el contenido del grupo de recursos donde desplegaste los recursos del hub usados en este ejercicio.
2. En la barra de herramientas, selecciona **Eliminar grupo de recursos**.
3. Ingresa el nombre del grupo de recursos y confirma que deseas eliminarlo.

## Recursos

- [Documentación de Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Portal Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Introducción a Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Fundamentos de agentes de IA en Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->