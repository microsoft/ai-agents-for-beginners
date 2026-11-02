---
name: microsoft-docs
description: Consultar la documentación oficial de Microsoft para encontrar conceptos,
  tutoriales y ejemplos de código en Azure, .NET, Agent Framework, Aspire, VS Code,
  GitHub y más. Utiliza Microsoft Learn MCP como predeterminado, con Context7 y Aspire
  MCP para contenido que se encuentra fuera de learn.microsoft.com.
---
# Microsoft Docs

Habilidad de investigación para el ecosistema tecnológico de Microsoft. Cubre learn.microsoft.com y la documentación que está fuera de este (VS Code, GitHub, Aspire, repositorios de Agent Framework).

---

## Predeterminado: Microsoft Learn MCP

Usa estas herramientas para **todo en learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows y más. Esta es la herramienta principal para la gran mayoría de consultas sobre documentación de Microsoft.

| Herramienta | Propósito |
|------|---------|
| `microsoft_docs_search` | Busca en learn.microsoft.com — conceptos, guías, tutoriales, configuración |
| `microsoft_code_sample_search` | Encuentra fragmentos de código funcionales en los documentos de Learn. Pasa `language` (`python`, `csharp`, etc.) para mejores resultados |
| `microsoft_docs_fetch` | Obtiene el contenido completo de la página desde una URL específica (cuando los extractos de búsqueda no son suficientes) |

Usa `microsoft_docs_fetch` después de buscar cuando necesites tutoriales completos, todas las opciones de configuración o cuando los extractos de búsqueda estén truncados.

---

## Excepciones: Cuándo Usar Otras Herramientas

Las siguientes categorías están **fuera de** learn.microsoft.com. Usa la herramienta especificada en su lugar.

### Aspire — Usa Aspire MCP Server (preferido) o Context7

La documentación de Aspire está en **aspire.dev**, no en Learn. La mejor herramienta depende de tu versión de Aspire CLI:

**CLI 13.2+** (recomendado) — El servidor Aspire MCP incluye herramientas de búsqueda de documentación integradas:

| Herramienta MCP | Descripción |
|----------|-------------|
| `list_docs` | Lista toda la documentación disponible de aspire.dev |
| `search_docs` | Búsqueda léxica ponderada a través del contenido de aspire.dev |
| `get_doc` | Recupera un documento específico por slug |

Estas vienen incluidas en Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Para actualizar: `aspire update --self --channel daily`.

**CLI 13.1** — El servidor MCP proporciona búsqueda de integraciones (`list_integrations`, `get_integration_docs`) pero **no** búsqueda en la documentación. Usa Context7:

| ID de Biblioteca | Usar para |
|---|---|
| `/microsoft/aspire.dev` | Principal — guías, integraciones, referencia CLI, despliegue |
| `/microsoft/aspire` | Fuente de tiempo de ejecución — API internas, detalles de implementación |
| `/communitytoolkit/aspire` | Integraciones comunitarias — Go, Java, Node.js, Ollama |

### VS Code — Usa Context7

La documentación de VS Code está en **code.visualstudio.com**, no en Learn.

| ID de Biblioteca | Usar para |
|---|---|
| `/websites/code_visualstudio` | Documentación de usuario — configuraciones, características, depuración, desarrollo remoto |
| `/websites/code_visualstudio_api` | API de extensiones — webviews, TreeViews, comandos, puntos de contribución |

### GitHub — Usa Context7

La documentación de GitHub está en **docs.github.com** y **cli.github.com**.

| ID de Biblioteca | Usar para |
|---|---|
| `/websites/github_en` | Actions, API, repositorios, seguridad, administración, Copilot |
| `/websites/cli_github` | Comandos y flags de GitHub CLI (`gh`) |

### Agent Framework — Usa Learn MCP + Context7

Los tutoriales de Agent Framework están en learn.microsoft.com (usa `microsoft_docs_search`), pero el **repositorio de GitHub** tiene detalles a nivel API que a menudo están por delante de la documentación publicada — particularmente la referencia REST API de DevUI, opciones CLI e integración .NET.

| ID de Biblioteca | Usar para |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriales — guías DevUI, trazado, orquestación de flujos de trabajo |
| `/microsoft/agent-framework` | Detalles de API — puntos finales REST de DevUI, flags CLI, autenticación, .NET `AddDevUI`/`MapDevUI` |

**Consejo DevUI:** Consulta la fuente del sitio Learn para guías prácticas, luego la fuente del repositorio para detalles a nivel API (esquemas de endpoints, configuración de proxy, tokens de autenticación).

---

## Configuración de Context7

Para cualquier consulta en Context7, resuelve primero el ID de biblioteca (una vez por sesión):

1. Llama a `mcp_context7_resolve-library-id` con el nombre de la tecnología
2. Llama a `mcp_context7_query-docs` con el ID de biblioteca retornado y una consulta específica

---

## Cómo Escribir Consultas Efectivas

Sé específico — incluye versión, intención y lenguaje:

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

Incluye contexto:
- **Versión** cuando sea relevante (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Intención de la tarea** (`inicio rápido`, `tutorial`, `visión general`, `límites`, `referencia API`)
- **Lenguaje** para documentación poliglota (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->