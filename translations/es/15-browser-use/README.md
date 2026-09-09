# Creación de Agentes de Uso de Computadora (CUA)

Los agentes de uso de computadora pueden interactuar con los sitios web de la misma manera que una persona: abriendo un navegador, inspeccionando la página y tomando la mejor acción siguiente basada en lo que ven. En esta lección, construirás un agente de automatización de navegador que busca en Airbnb, extrae datos estructurados de listados e identifica la estadía más barata en Estocolmo.

La lección combina Browser-Use para navegación impulsada por IA, Playwright y el Protocolo de DevTools de Chrome (CDP) para control del navegador, Azure OpenAI para razonamiento habilitado por visión, y Pydantic para extracción estructurada.

## Introducción

Esta lección cubrirá:

- Comprender cuándo los agentes de uso de computadora son más adecuados que la automatización solo por API
- Combinar Browser-Use con Playwright y CDP para un manejo confiable del ciclo de vida del navegador
- Utilizar la visión de Azure OpenAI y la salida estructurada de Pydantic para extraer datos de listados de páginas web dinámicas
- Decidir cuándo usar un flujo de trabajo de automatización de navegador basado en agentes, actores o híbrido

## Objetivos de Aprendizaje

Después de completar esta lección, sabrás cómo:

- Configurar Browser-Use con Azure OpenAI y Playwright
- Construir un flujo de trabajo de automatización de navegador que navegue un sitio web real y maneje elementos de UI dinámicos
- Extraer resultados tipados del contenido visible de la página y convertirlos en lógica empresarial descendente
- Elegir entre patrones de agente y actor según la predictibilidad de la tarea en el navegador

## Ejemplo de Código

Esta lección incluye un tutorial en notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Inicia una sesión de Chrome vía CDP, busca listados en Airbnb para Estocolmo, extrae precios con la visión de Browser-Use y devuelve la opción más barata como datos estructurados.

## Requisitos Previos

- Python 3.12+
- Despliegue de Azure OpenAI configurado en tu entorno
- Chrome o Chromium instalado localmente
- Dependencias de Playwright instaladas
- Familiaridad básica con Python async

## Configuración

Instala los paquetes usados en el notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Configura las variables de entorno de Azure OpenAI usadas por el notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opcional: por defecto usa la última versión de la API cuando se omite
AZURE_OPENAI_API_VERSION=...
```

## Visión General de la Arquitectura

El notebook demuestra un flujo de trabajo híbrido de automatización de navegador:

1. Chrome se inicia con CDP habilitado para que tanto Playwright como Browser-Use puedan compartir la misma sesión del navegador.
2. Un agente de Browser-Use maneja tareas abiertas de navegación como abrir Airbnb, descartar ventanas emergentes y buscar Estocolmo.
3. La página activa se inspecciona con un esquema Pydantic estructurado para extraer títulos de listados, precios por noche, calificaciones y URLs.
4. La lógica en Python compara los listados extraídos y destaca el resultado más barato.

Este enfoque mantiene el razonamiento flexible basado en visión que es bueno en Browser-Use mientras te brinda control determinista del navegador cuando lo necesitas.

## Puntos Clave y Mejores Prácticas

### Cuándo Usar Agente vs Actor

| Escenario | Usar Agente | Usar Actor |
|----------|-------------|-----------|
| Diseños dinámicos | Sí, la IA puede adaptarse a cambios en la página | No, los selectores frágiles pueden romperse |
| Estructura conocida | No, un agente es más lento que control directo | Sí, rápido y preciso |
| Encontrar elementos | Sí, el lenguaje natural funciona bien | No, se requieren selectores exactos |
| Control del tiempo | No, menos predecible | Sí, control total sobre esperas e intentos |
| Flujos de trabajo complejos | Sí, maneja estados UI inesperados | No, requiere ramificaciones explícitas |

### Mejores Prácticas de Browser-Use

1. Comienza con un agente para exploración y navegación dinámica.
2. Cambia a control directo de la página cuando la interacción sea predecible.
3. Usa modelos de salida estructurados para que los datos extraídos sean validados y con tipos seguros.
4. Añade retrasos estratégicos después de acciones que provocan cambios visibles en UI.
5. Captura capturas de pantalla durante la iteración para facilitar la depuración de fallos.
6. Espera que los sitios cambien y diseña estrategias de respaldo para ventanas emergentes y cambios de diseño.
7. Mezcla patrones de agente y actor para obtener flexibilidad y precisión.

### Dispositivos de Seguridad para Agentes de Navegador

Los agentes de navegador operan en sitios web en vivo, por lo que necesitan límites más estrictos que un script que solo llama a una API conocida. Antes de pasar de un demo en notebook a un flujo de trabajo real, define los controles sobre lo que el agente puede ver, hacer clic y enviar.

1. **Delimita el entorno de navegación.** Ejecuta el agente en un perfil de navegador dedicado o sandbox, y limita a los dominios necesarios para la tarea.
2. **Separa observación de acción.** Deja que el agente busque, lea y extraiga datos primero; requiere un paso explícito de aprobación antes de enviar formularios, enviar mensajes, reservar viajes, hacer compras, borrar registros o cambiar configuraciones de cuenta.
3. **Mantén secretos fuera de prompts y registros.** No pongas contraseñas, detalles de pago, cookies de sesión o datos personales sin procesar en el contexto del modelo. Deja que el usuario tome control para autenticación y redacte campos sensibles de los registros.
4. **Trata el contenido de la página como entrada no confiable.** Un sitio web puede contener instrucciones destinadas al agente, no al usuario. El agente debe ignorar texto de página que le pida cambiar su objetivo, revelar datos, deshabilitar salvaguardas o visitar sitios no relacionados.
5. **Usa verificaciones determinísticas en pasos riesgosos.** Verifica la URL actual, título de la página, elemento seleccionado, precio, destinatario y resumen de acción con código antes de pedir aprobación del usuario para el paso final.
6. **Establece presupuestos y condiciones de parada.** Limita el número de acciones, reintentos, pestañas y minutos que el agente puede usar. Detente cuando el estado de la página sea ambiguo en vez de seguir haciendo clic.
7. **Registra evidencias útiles, no todo.** Conserva resúmenes de acción, marcas de tiempo, URLs, descripciones de elementos seleccionados y referencias de capturas para revisar fallos sin almacenar contenido innecesario y sensible.

En el ejemplo de Airbnb, el comportamiento seguro por defecto es buscar listados y extraer precios. Iniciar sesión, contactar a un anfitrión o completar una reserva debe ser una acción separada aprobada por el usuario.

### Aplicaciones del Mundo Real

- Reservas de viajes y monitoreo de precios
- Comparación de precios y verificación de disponibilidad en comercio electrónico
- Extracción estructurada de sitios web dinámicos
- Pruebas y verificación de UI con reconocimiento visual
- Monitoreo de sitios web y alertas
- Relleno inteligente de formularios en flujos multi-pasos

## Ejemplo Real: Microsoft Project Opal

El agente que construyes en esta lección es una versión pequeña y local de un **agente de uso de computadora (CUA)** — un programa que maneja un navegador como lo haría una persona. Microsoft está llevando esta misma idea a la empresa con **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, una capacidad en Microsoft 365 Copilot.

Con Project Opal, describes una tarea y el agente trabaja en tu nombre usando **uso de computadora en un PC en la nube Windows 365 seguro**, operando a través de las aplicaciones basadas en navegador, sitios y datos de tu organización. Funciona **asíncronamente en segundo plano**, y puedes guiar el trabajo o tomar control en cualquier momento. Trabajos de ejemplo incluyen:

- Gestionar solicitudes de membresía en grupos de seguridad
- Recopilar y validar evidencias de auditoría para revisiones de cumplimiento
- Clasificar incidentes de TI (actualizar estado del ticket, asignar responsables, cerrar duplicados)
- Compilar datos de Excel en un informe de cierre financiero

Opal es una referencia útil para cómo lucen agentes de uso de computadora **confiables y en producción** — y refuerza conceptos de lecciones anteriores:

| Concepto en este curso | Cómo lo aplica Project Opal |
|--------------------|-----------------------------|
| **Humano en el bucle** (Lección 06) | Opal pausa para credenciales de inicio de sesión, datos sensibles o instrucciones ambiguas, y nunca ingresa contraseñas o envía formularios sin confirmación explícita. Puedes *Tomar Control* y *Devolver Control* en mitad de la tarea. |
| **Agentes confiables y seguros** (Lecciones 06 y 18) | Se ejecuta en un PC en la nube Windows 365 aislado, es solo navegador por defecto (acceso a otras partes de la computadora bloqueado, aplicado vía Intune), usa *tu* identidad para acceder solo a lo que estás autorizado, y registra cada acción para auditoría. |
| **Planificación y metacognición** (Lecciones 07 y 09) | Opal genera un plan para la tarea primero, luego supervisa su propio razonamiento en cada paso y pausa si detecta actividad sospechosa. |
| **Capacidades/herramientas reutilizables** (Lección 04) | Las **Habilidades** te permiten escribir instrucciones para tareas repetibles (importadas desde un archivo `.md` o creadas con Opal) y reutilizarlas en conversaciones. |

> **Disponibilidad:** Project Opal está disponible actualmente para usuarios en el [programa de acceso temprano Frontier](https://adoption.microsoft.com/copilot/frontier-program/) con suscripción a Microsoft 365 Copilot, y tu administrador debe completar la configuración. Al ser una función experimental de Frontier, sus capacidades pueden cambiar con el tiempo.

## Chequeo de Conocimientos

Pon a prueba tu entendimiento antes de avanzar a la próxima lección.

**1. ¿Cuándo es un agente de uso de computadora basado en navegador una mejor opción que un flujo solo por API?**

<details>
<summary>Respuesta</summary>

Usa un agente de navegador cuando la tarea depende de lo que es visible en una UI web, el sitio no expone la API necesaria, o la página cambia lo suficiente como para que la lógica fija de API o selectores sea frágil. Si existe una API estable para la misma tarea, prefiere la API porque usualmente es más rápida, fácil de probar y segura.
</details>

**2. En un flujo híbrido, ¿qué partes debería manejar el agente y qué partes debería manejar el código Playwright directo?**

<details>
<summary>Respuesta</summary>

Deja que el agente maneje la navegación abierta y estados dinámicos de UI, como encontrar la página correcta o descartar ventanas emergentes inesperadas. Cambia a control directo Playwright cuando la estructura de la página sea conocida y la acción requiera precisión, reintentos, esperas o validación determinista.
</details>

**3. El ejemplo de Airbnb encuentra un listado que el usuario podría querer reservar. ¿Qué debería pasar antes de que el flujo inicie sesión, contacte a un anfitrión o complete una reserva?**

<details>
<summary>Respuesta</summary>

El flujo debería pausar y pedir aprobación explícita del usuario. Antes de pedirla, debería mostrar un resumen claro del listado seleccionado, URL actual, precio, fechas y acción planeada. Buscar y extraer precios puede ser autónomo; acceso a cuenta, mensajes, compras y reservas deben ser aprobados por el usuario.
</details>

**4. Una página web le dice al agente que ignore sus instrucciones originales, visite otro sitio y revele credenciales guardadas. ¿Cómo debería tratar el agente ese texto?**

<details>
<summary>Respuesta</summary>

Trátalo como contenido no confiable de la página, no como instrucción de desarrollador o usuario. El agente debe permanecer dentro del dominio y alcance de la tarea permitidos, negarse a revelar secretos y evitar seguir texto de página que cambie el objetivo, deshabilite salvaguardas o lo envíe a sitios no relacionados.
</details>

**5. ¿Qué evidencias son útiles conservar cuando un agente de navegador se ejecuta, y qué debería evitarse?**

<details>
<summary>Respuesta</summary>

Conserva resúmenes de acción, marcas de tiempo, URLs, descripciones de elementos seleccionados, resultados de validación y referencias de capturas para que la ejecución pueda revisarse. Evita almacenar contraseñas, datos de pago, cookies de sesión, datos personales sin procesar o contenido completo de páginas a menos que exista una razón específica de retención y privacidad.
</details>

## Recursos Adicionales

- [Comienza con Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Plantilla de integración Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parámetros de actor Browser-Use y extracción de contenido](https://docs.browser-use.com/customize/actor/all-parameters)
- [Configuración del curso](../00-course-setup/README.md)

## Lección Anterior

[Explorando Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Próxima Lección

[Despliegue de Agentes Escalables](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->