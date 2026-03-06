# Agentes de IA para Principiantes - Guía de Estudio y Resumen del Curso

Esta guía ofrece un resumen del curso "Agentes de IA para Principiantes" y explica conceptos clave, frameworks y patrones de diseño para construir agentes de IA.

## 1. Introducción a los Agentes de IA

**¿Qué son los Agentes de IA?**  
Los agentes de IA son sistemas que amplían las capacidades de los Modelos de Lenguaje Extenso (LLMs) al darles acceso a **herramientas**, **conocimiento** y **memoria**. A diferencia de un chatbot LLM estándar que solo genera texto basado en datos de entrenamiento, un agente de IA puede:  
- **Percibir** su entorno (a través de sensores o entradas).  
- **Razonar** sobre cómo resolver un problema.  
- **Actuar** para cambiar el entorno (mediante actuadores o ejecución de herramientas).

**Componentes Clave de un Agente:**  
- **Entorno**: El espacio donde el agente opera (por ejemplo, un sistema de reservas).  
- **Sensores**: Mecanismos para recopilar información (por ejemplo, leer una API).  
- **Actuadores**: Mecanismos para realizar acciones (por ejemplo, enviar un correo electrónico).  
- **Cerebro (LLM)**: El motor de razonamiento que planifica y decide qué acciones tomar.

## 2. Frameworks de Agentes

El curso utiliza **Microsoft Agent Framework (MAF)** con **Azure AI Foundry Agent Service V2** para construir agentes:

| Componente | Enfoque | Mejor Para |
|------------|---------|------------|
| **Microsoft Agent Framework** | SDK unificado de Python/C# para agentes, herramientas y flujos de trabajo | Construir agentes con herramientas, flujos multi-agente y patrones de producción. |
| **Azure AI Foundry Agent Service** | Tiempo de ejecución gestionado en la nube | Despliegue seguro y escalable con administración de estado integrada, observabilidad y confianza. |

## 3. Patrones de Diseño para Agentes

Los patrones de diseño ayudan a estructurar cómo los agentes operan para resolver problemas de manera confiable.

### **Patrón de Uso de Herramientas** (Lección 4)  
Este patrón permite a los agentes interactuar con el mundo exterior.  
- **Concepto**: Al agente se le proporciona un "esquema" (una lista de funciones disponibles y sus parámetros). El LLM decide *qué* herramienta llamar y con *qué* argumentos según la solicitud del usuario.  
- **Flujo**: Solicitud del Usuario -> LLM -> **Selección de Herramienta** -> **Ejecución de Herramienta** -> LLM (con salida de la herramienta) -> Respuesta Final.  
- **Casos de Uso**: Recuperar datos en tiempo real (clima, precios de acciones), realizar cálculos, ejecutar código.

### **Patrón de Planificación** (Lección 7)  
Este patrón permite a los agentes resolver tareas complejas de múltiples pasos.  
- **Concepto**: El agente descompone un objetivo de alto nivel en una secuencia de subtareas más pequeñas.  
- **Enfoques**:  
  - **Descomposición de Tareas**: Dividir "Planificar un viaje" en "Reservar vuelo", "Reservar hotel", "Alquilar coche".  
  - **Planificación Iterativa**: Reevaluar el plan basado en los resultados de pasos anteriores (p. ej., si el vuelo está lleno, elegir otra fecha).  
- **Implementación**: A menudo involucra un agente "Planificador" que genera un plan estructurado (por ejemplo, JSON) que luego ejecutan otros agentes.

## 4. Principios de Diseño

Al diseñar agentes, considera tres dimensiones:  
- **Espacio**: Los agentes deben conectar personas y conocimiento, ser accesibles pero no intrusivos.  
- **Tiempo**: Los agentes deben aprender del *Pasado*, ofrecer impulsos relevantes en el *Ahora* y adaptarse para el *Futuro*.  
- **Núcleo**: Aceptar la incertidumbre pero establecer confianza a través de la transparencia y el control del usuario.

## 5. Resumen de Lecciones Clave

- **Lección 1**: Los agentes son sistemas, no solo modelos. Perciben, razonan y actúan.  
- **Lección 2**: Microsoft Agent Framework abstrae la complejidad de llamar a herramientas y gestionar estado.  
- **Lección 3**: Diseña con transparencia y control del usuario en mente.  
- **Lección 4**: Las herramientas son las "manos" del agente. La definición del esquema es crucial para que el LLM entienda cómo usarlas.  
- **Lección 7**: La planificación es la "función ejecutiva" del agente, permitiéndole abordar flujos de trabajo complejos.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos responsabilizamos por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->