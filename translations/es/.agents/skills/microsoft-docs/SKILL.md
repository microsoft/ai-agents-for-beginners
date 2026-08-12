---
name: microsoft-docs
description: Consulta la documentación oficial de Microsoft para encontrar conceptos,
  tutoriales y ejemplos de código en Azure, .NET, Agent Framework, Aspire, VS Code,
  GitHub y más. Utiliza Microsoft Learn MCP como predeterminado, con Context7 y Aspire
  MCP para contenido que se encuentra fuera de learn.microsoft.com.
---
# Documentación de Microsoft

Habilidad de investigación para el ecosistema tecnológico de Microsoft. Cubre learn.microsoft.com y la documentación que vive fuera de él (repositorios de VS Code, GitHub, Aspire, Agent Framework).

---

## Predeterminado: Microsoft Learn MCP

Use estas herramientas para **todo en learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, y más. Esta es la herramienta principal para la gran mayoría de consultas sobre documentación de Microsoft.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Buscar en learn.microsoft.com — conceptos, guías, tutoriales, configuración |
| `microsoft_code_sample_search` | Encontrar fragmentos de código funcionales de la documentación de Learn. Pase `language` (`python`, `csharp`, etc.) para mejores resultados |
| `microsoft_docs_fetch` | Obtener el contenido completo de una página desde una URL específica (cuando los extractos de búsqueda no son suficientes) |

Use `microsoft_docs_fetch` después de la búsqueda cuando necesite tutoriales completos, todas las opciones de configuración, o cuando los extractos de búsqueda estén truncados.

---

## Excepciones: Cuándo usar otras herramientas

Las siguientes categorías residen **fuera** de learn.microsoft.com. Utilice la herramienta especificada en su lugar.

### .NET Aspire — Usar Aspire MCP Server (preferido) o Context7

La documentación de Aspire vive en **aspire.dev**, no en Learn. La mejor herramienta depende de la versión de Aspire CLI:

**CLI 13.2+** (recomendado) — El servidor Aspire MCP incluye herramientas integradas de búsqueda de documentación:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Lista toda la documentación disponible en aspire.dev |
| `search_docs` | Búsqueda léxica ponderada en el contenido de aspire.dev |
| `get_doc` | Recupera un documento específico por slug |

Estas se incluyen en Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Para actualizar: `aspire update --self --channel daily`. Referencia: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — El servidor MCP proporciona búsqueda de integraciones (`list_integrations`, `get_integration_docs`) pero **no** búsqueda de documentación. Recurra a Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Principal — guías, integraciones, referencia de CLI, despliegue |
| `/dotnet/aspire` | Fuente de tiempo de ejecución — internos de la API, detalles de implementación |
| `/communitytoolkit/aspire` | Integraciones de la comunidad — Go, Java, Node.js, Ollama |

### VS Code — Usar Context7

La documentación de VS Code está en **code.visualstudio.com**, no en Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Documentación de usuario — ajustes, características, depuración, desarrollo remoto |
| `/websites/code_visualstudio_api` | API de extensiones — webviews, TreeViews, comandos, puntos de contribución |

### GitHub — Usar Context7

La documentación de GitHub está en **docs.github.com** y **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repositorios, seguridad, administración, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) comandos y opciones |

### Agent Framework — Usar Learn MCP + Context7

Los tutoriales de Agent Framework están en learn.microsoft.com (use `microsoft_docs_search`), pero el **repositorio de GitHub** tiene detalles a nivel de API que a menudo están por delante de la documentación publicada — particularmente la referencia REST de DevUI, opciones del CLI y la integración .NET.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriales — guías de DevUI, trazado, orquestación de flujos de trabajo |
| `/microsoft/agent-framework` | Detalles de API — endpoints REST de DevUI, opciones del CLI, autenticación, .NET `AddDevUI`/`MapDevUI` |

**Consejo DevUI:** Consulte la fuente del sitio Learn para guías prácticas, luego la fuente del repositorio para detalles a nivel de API (esquemas de endpoints, configuración de proxy, tokens de autenticación).

---

## Configuración de Context7

Para cualquier consulta a Context7, resuelva primero el ID de la biblioteca (una vez por sesión):

1. Llame a `mcp_context7_resolve-library-id` con el nombre de la tecnología
2. Llame a `mcp_context7_query-docs` con el ID de biblioteca devuelto y una consulta específica

---

## Cómo redactar consultas efectivas

Sea específico — incluya versión, intención y lenguaje:

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

Incluya contexto:
- **Versión** cuando sea relevante (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Intención de la tarea** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Lenguaje** para documentación poliglota (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma de origen debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por un traductor humano. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->