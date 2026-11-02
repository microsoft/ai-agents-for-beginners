---
name: local-ai-agents
license: MIT
---
# Creación de Agentes de IA Locales con Foundry Local y Qwen

> Habilidad complementaria para [Lección 17 – Creación de Agentes de IA Locales](../../../17-creating-local-ai-agents/README.md).
> Úsala para ayudar a un aprendiz a construir un agente que razone, llame a herramientas y busque
> documentación completamente en su propia máquina — sin inferencia en la nube. Fundamenta cada
> recomendación en el contenido de la lección y el cuaderno ejecutable.

## Desencadenantes

Activa esta habilidad cuando un aprendiz quiera:
- Ejecutar un agente **totalmente en el dispositivo** por razones de privacidad, costo o funcionamiento sin conexión.
- Servir un modelo localmente con **Foundry Local** y conectarse mediante el endpoint compatible con OpenAI.
- Usar un modelo **Qwen con llamadas a funciones** para realizar llamadas confiables a herramientas locales.
- Agregar **RAG local** (Chroma) o un **servidor MCP local**.
- Diseñar una estrategia de enrutamiento **híbrida** local/nube.

## Modelo mental central

Un SLM cambia amplitud por privacidad, costo y operación sin conexión. La estrategia ganadora: **dejar que el SLM orqueste y que las herramientas hagan el trabajo pesado.** El
modelo no necesita *conocer* la base de código — necesita saber cuándo llamar a
`read_file` y `search_docs`. Esto juega a la fortaleza de un SLM (decisiones limitadas
como selección de herramientas) y evita su debilidad (conocimiento amplio, razonamiento en múltiples saltos).



## Por qué estas piezas específicas

- **Foundry Local** expone un **endpoint HTTP compatible con OpenAI**, por lo que el código del agente en la nube se transfiere solo cambiando `base_url` (y usando una clave API local ficticia). Además, selecciona automáticamente la mejor compilación (CPU/GPU/NPU) para la máquina.
- Los modelos **Qwen** están entrenados para llamadas a funciones y emiten llamadas a herramientas bien formadas de manera consistente — esto es lo que convierte un modelo de *chat* local en un *agente* local.
- **Chroma** funciona en proceso y almacena vectores en disco, por lo que todo el pipeline RAG (incrustar → almacenar → recuperar → razonar) se mantiene local.
- **MCP** es un transporte, no un servicio en la nube: un servidor MCP puede ejecutarse localmente sobre `stdio`.

## Esenciales de configuración

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # marcador de posición local
```

~8 GB de RAM es un mínimo realista; una GPU/NPU ayuda pero no es obligatoria.

## Patrones clave para reproducir

Dirige al aprendiz al cuaderno
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Herramientas en sandbox**: cada herramienta de archivo resuelve rutas y rechaza cualquier cosa fuera de una única raíz de proyecto — incluso localmente, una herramienta se ejecuta con los permisos del usuario.
- **Bucle de llamadas a herramientas**: registra las herramientas con el esquema de herramientas OpenAI, ejecuta localmente las herramientas solicitadas, retroalimenta resultados, repite hasta una respuesta final.
- **RAG local**: inserta documentos en una colección Chroma; `search_docs` devuelve los fragmentos top-k.
- **MCP local**: conéctate a un servidor local sobre `stdio`; delimítalo a un directorio de proyecto y valida sus salidas.

## Enrutamiento híbrido (local como uno de los modelos)

| Situación | Dónde se ejecuta |
|-----------|---------------|
| Datos sensibles / sin conexión | SLM local |
| Tarea simple y acotada | SLM local (barato, rápido) |
| Razonamiento complejo en múltiples saltos sobre datos no sensibles | Modelo en la nube |
| Caída de la nube | SLM local (degradación elegante) |

Esto refleja la idea de enrutamiento de modelos de la Lección 16, con la estación de trabajo como una de
las rutas. Prefiere diseños que recurran a local para que el agente degrade en
calidad antes que fallar por completo.

## Barreras para el asistente

- Mantén toda operación de archivos/herramientas limitada a un directorio de proyecto en sandbox.
- No envíes código o datos a la nube cuando el objetivo declarado del aprendiz sea privacidad/sin conexión — mantén todo el pipeline local.
- Establece expectativas realistas para la calidad del SLM; apóyate en herramientas y RAG más que en el conocimiento memorizado del modelo.
- Ten en cuenta que la Lección 17 **no** tiene un endpoint de Respuestas Foundry, por lo que la acción de prueba de humo en la nube no aplica — valida ejecutando el cuaderno localmente.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->