# Construyendo Agentes de Uso de Computadora (CUA)

Los agentes de uso de computadora pueden interactuar con sitios web de la misma manera que lo haría una persona: abriendo un navegador, inspeccionando la página y tomando la mejor acción siguiente basándose en lo que ven. En esta lección, construirás un agente de automatización de navegador que busca en Airbnb, extrae datos estructurados de listados e identifica la estadía más barata en Estocolmo.

La lección combina Browser-Use para navegación impulsada por IA, Playwright y el Protocolo DevTools de Chrome (CDP) para el control del navegador, Azure OpenAI para razonamiento habilitado por visión y Pydantic para extracción estructurada.

## Introducción

Esta lección cubrirá:

- Entender cuándo los agentes de uso de computadora son una mejor opción que la automatización solo por API
- Combinar Browser-Use con Playwright y CDP para una gestión confiable del ciclo de vida del navegador
- Usar la visión de Azure OpenAI y la salida estructurada de Pydantic para extraer datos de listados de páginas web dinámicas
- Decidir cuándo usar un flujo de trabajo de automatización de navegador basado en agente, actor o híbrido

## Objetivos de Aprendizaje

Después de completar esta lección, sabrás cómo:

- Configurar Browser-Use con Azure OpenAI y Playwright
- Construir un flujo de automatización de navegador que navegue por un sitio web real y maneje elementos dinámicos de la interfaz de usuario
- Extraer resultados tipados del contenido visible de la página y convertirlos en lógica empresarial descendente
- Elegir entre patrones de agente y actor basado en cuán predecible es la tarea del navegador

## Ejemplo de Código

Esta lección incluye un tutorial en notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Lanza una sesión de Chrome sobre CDP, busca listados en Airbnb para Estocolmo, extrae precios con la visión de Browser-Use y devuelve la opción más barata como datos estructurados.

## Requisitos Previos

- Python 3.12+
- Implementación de Azure OpenAI configurada en tu entorno
- Chrome o Chromium instalado localmente
- Dependencias de Playwright instaladas
- Familiaridad básica con Python asíncrono

## Configuración

Instala los paquetes utilizados en el notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Configura las variables de entorno de Azure OpenAI utilizadas por el notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opcional: por defecto usa la versión más reciente de la API si se omite
AZURE_OPENAI_API_VERSION=...
```

## Descripción General de la Arquitectura

El notebook demuestra un flujo de trabajo híbrido de automatización de navegador:

1. Chrome se inicia con CDP habilitado para que tanto Playwright como Browser-Use puedan compartir la misma sesión del navegador.
2. Un agente Browser-Use maneja tareas abiertas de navegación como abrir Airbnb, descartar ventanas emergentes y buscar Estocolmo.
3. La página activa es inspeccionada con un esquema estructurado de Pydantic para extraer títulos de listados, precios por noche, valoraciones y URLs.
4. La lógica de Python compara los listados extraídos y resalta el resultado más barato.

Este enfoque mantiene el razonamiento flexible basado en visión que Browser-Use hace bien, mientras te da control determinista del navegador cuando lo necesitas.

## Puntos Clave y Mejores Prácticas

### Cuándo Usar Agente versus Actor

| Escenario | Usar Agente | Usar Actor |
|----------|--------------|-----------|
| Diseños dinámicos | Sí, la IA puede adaptarse a cambios en la página | No, los selectores frágiles pueden romperse |
| Estructura conocida | No, un agente es más lento que el control directo | Sí, rápido y preciso |
| Encontrar elementos | Sí, el lenguaje natural funciona bien | No, se requieren selectores exactos |
| Control de tiempos | No, menos predecible | Sí, control total sobre esperas e intentos |
| Flujos de trabajo complejos | Sí, maneja estados inesperados de la UI | No, requiere ramificación explícita |

### Mejores Prácticas de Browser-Use

1. Comienza con un agente para exploración y navegación dinámica.
2. Cambia a control directo de página cuando la interacción sea predecible.
3. Usa modelos de salida estructurados para que los datos extraídos sean validados y con tipos seguros.
4. Agrega retrasos estratégicos después de acciones que provocan cambios visibles en la UI.
5. Captura capturas de pantalla mientras iteras para que los fallos sean más fáciles de depurar.
6. Espera que los sitios web cambien y diseña estrategias de respaldo para ventanas emergentes y cambios en el diseño.
7. Combina patrones de agente y actor para obtener flexibilidad y precisión.

### Salvaguardas de Seguridad para Agentes de Navegador

Los agentes de navegador operan en sitios web en vivo, por lo que necesitan límites más estrictos que un script que solo llame a una API conocida. Antes de pasar de una demostración en notebook a un flujo real, define los controles sobre lo que el agente puede ver, hacer clic y enviar.

1. **Delimita el entorno de navegación.** Ejecuta el agente en un perfil de navegador dedicado o en un sandbox, y limítalo a los dominios necesarios para la tarea.
2. **Separa la observación de la acción.** Deja que el agente busque, lea y extraiga datos primero; requiere un paso explícito de aprobación antes de que envíe formularios, envíe mensajes, reserve viajes, haga compras, elimine registros o cambie configuraciones de cuenta.
3. **Mantén secretos fuera de indicaciones y registros.** No pongas contraseñas, detalles de pago, cookies de sesión o datos personales sin procesar en el contexto del modelo. Deja que el usuario tome el control para autenticación y redacte campos sensibles de los registros.
4. **Trata el contenido de la página como entrada no confiable.** Un sitio web puede contener instrucciones destinadas al agente, no al usuario. El agente debe ignorar texto en la página que le pida cambiar su objetivo, revelar datos, deshabilitar salvaguardas o visitar sitios no relacionados.
5. **Usa verificaciones deterministas en pasos riesgosos.** Verifica la URL actual, título de la página, elemento seleccionado, precio, destinatario y resumen de la acción con código antes de pedir al usuario aprobar el paso final.
6. **Establece presupuestos y condiciones de detención.** Limita el número de acciones, reintentos, pestañas y minutos que el agente puede usar. Detente cuando el estado de la página sea ambiguo en vez de seguir haciendo clic.
7. **Registra evidencia útil, no todo.** Guarda resúmenes de acciones, sellos de tiempo, URLs, descripciones de elementos seleccionados y referencias a capturas de pantalla para que los fallos puedan revisarse sin almacenar contenido sensible innecesario de la página.

En el ejemplo de Airbnb, la opción segura por defecto es buscar listados y extraer precios. Iniciar sesión, contactar a un anfitrión o completar una reserva debe ser una acción separada aprobada por el usuario.

### Aplicaciones en el Mundo Real

- Reservas de viaje y monitoreo de precios
- Comparación de precios y comprobación de disponibilidad en comercio electrónico
- Extracción estructurada de sitios web dinámicos
- Pruebas y verificación de UI conscientes de visión
- Monitoreo y alertas de sitios web
- Rellenado inteligente de formularios en flujos de varios pasos

## Ejemplo Real: Microsoft Project Opal

El agente que construyes en esta lección es una versión pequeña y local de un **agente de uso de computadora (CUA)** — un programa que maneja un navegador de la misma manera que una persona. Microsoft está llevando esta misma idea a las empresas con **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, una capacidad en Microsoft 365 Copilot.

Con Project Opal, describes una tarea y el agente trabaja en tu nombre usando **uso de computadora en un Windows 365 Cloud PC seguro**, operando a través de las aplicaciones, sitios y datos basados en navegador de tu organización. Funciona **de manera asíncrona en segundo plano**, y puedes guiar el trabajo o tomar control en cualquier momento. Ejemplos de trabajos incluyen:

- Gestionar solicitudes de membresía de grupos de seguridad
- Recopilar y validar evidencia de auditoría para revisiones de cumplimiento
- Clasificar incidentes de TI (actualizar estado de ticket, asignar responsables, cerrar duplicados)
- Compilar datos de Excel para un informe financiero de cierre

Opal es una referencia útil para cómo se ve un agente de uso de computadora **de grado producción y confiable** — y refuerza conceptos de lecciones anteriores:

| Concepto en este curso | Cómo Project Opal lo aplica |
|---------------------|----------------------------|
| **Humano en el ciclo** (Lección 06) | Opal pausa para credenciales de inicio de sesión, datos sensibles o instrucciones ambiguas, y nunca ingresa contraseñas ni envía formularios sin confirmación explícita. Puedes *Tomar Control* y *Devolver Control* en mitad de la tarea. |
| **Agentes confiables y seguros** (Lecciones 06 y 18) | Funciona en un Windows 365 Cloud PC aislado, es solo para navegador por defecto (acceso a otras computadoras bloqueado, aplicado vía Intune), usa *tu* identidad para acceder solo a lo autorizado y registra cada acción para auditoría. |
| **Planificación y metacognición** (Lecciones 07 y 09) | Opal genera un plan para el trabajo primero, luego supervisa su propio razonamiento en cada paso y se pausa si detecta actividad sospechosa. |
| **Capacidades / herramientas reutilizables** (Lección 04) | Las **Skills** te permiten escribir instrucciones para trabajos repetibles (importadas desde un archivo `.md` o creadas con Opal) y reutilizarlas en conversaciones. |

> **Disponibilidad:** Project Opal está actualmente disponible para usuarios en el [programa de acceso anticipado Frontier](https://adoption.microsoft.com/copilot/frontier-program/) con una suscripción a Microsoft 365 Copilot, y tu administrador debe completar la configuración. Como es una característica experimental de Frontier, las capacidades pueden cambiar con el tiempo.

## Recursos Adicionales

- [Comenzar con Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Plantilla de integración Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parámetros de actor Browser-Use y extracción de contenido](https://docs.browser-use.com/customize/actor/all-parameters)
- [Configuración del curso](../00-course-setup/README.md)

## Lección Anterior

[Explorando Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Próxima Lección

[Desplegando Agentes Escalables](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->