---
name: microsoft-docs
description: Interroger la documentation officielle de Microsoft pour trouver des
  concepts, des tutoriels et des exemples de code couvrant Azure, .NET, Agent Framework,
  Aspire, VS Code, GitHub, et plus encore. Utilise Microsoft Learn MCP par défaut,
  avec Context7 et Aspire MCP pour le contenu qui se trouve en dehors de learn.microsoft.com.
---
# Microsoft Docs

Compétence de recherche pour l'écosystème technologique Microsoft. Couvre learn.microsoft.com et la documentation qui vit en dehors de celui-ci (VS Code, GitHub, Aspire, dépôts Agent Framework).

---

## Default: Microsoft Learn MCP

Utilisez ces outils pour **tout ce qui se trouve sur learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, et plus encore. C'est l'outil principal pour la grande majorité des requêtes concernant la documentation Microsoft.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Rechercher sur learn.microsoft.com — concepts, guides, tutoriels, configuration |
| `microsoft_code_sample_search` | Trouver des extraits de code fonctionnels provenant des docs Learn. Fournir `language` (`python`, `csharp`, etc.) pour de meilleurs résultats |
| `microsoft_docs_fetch` | Obtenir le contenu complet d'une page à partir d'une URL spécifique (lorsque les extraits de recherche ne suffisent pas) |

Utilisez `microsoft_docs_fetch` après la recherche lorsque vous avez besoin de tutoriels complets, de toutes les options de configuration, ou lorsque les extraits de recherche sont tronqués.

---

## Exceptions: Quand utiliser d'autres outils

Les catégories suivantes se trouvent **en dehors** de learn.microsoft.com. Utilisez plutôt l'outil spécifié.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

La documentation d'Aspire se trouve sur **aspire.dev**, pas sur Learn. Le meilleur outil dépend de votre version de l'Aspire CLI :

**CLI 13.2+** (recommandé) — Le serveur Aspire MCP inclut des outils de recherche de documentation intégrés :

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Liste toute la documentation disponible sur aspire.dev |
| `search_docs` | Recherche lexicale pondérée dans le contenu d'aspire.dev |
| `get_doc` | Récupère un document spécifique par slug |

Ils sont fournis dans Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Pour mettre à jour: `aspire update --self --channel daily`. Réf: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — Le serveur MCP fournit la recherche d'intégrations (`list_integrations`, `get_integration_docs`) mais **pas** la recherche de docs. Revenir à Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Principal — guides, intégrations, référence CLI, déploiement |
| `/dotnet/aspire` | Source runtime — éléments internes de l'API, détails d'implémentation |
| `/communitytoolkit/aspire` | Intégrations communautaires — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

La documentation de VS Code se trouve sur **code.visualstudio.com**, pas sur Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Docs utilisateur — paramètres, fonctionnalités, débogage, développement distant |
| `/websites/code_visualstudio_api` | API d'extension — webviews, TreeViews, commandes, points de contribution |

### GitHub — Use Context7

La documentation GitHub se trouve sur **docs.github.com** et **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, dépôts, sécurité, administration, Copilot |
| `/websites/cli_github` | Commandes et options du GitHub CLI (`gh`) |

### Agent Framework — Use Learn MCP + Context7

Les tutoriels Agent Framework sont sur learn.microsoft.com (utilisez `microsoft_docs_search`), mais le **dépôt GitHub** contient des détails au niveau de l'API souvent en avance sur les docs publiés — en particulier la référence DevUI REST API, les options CLI, et l'intégration .NET.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriels — guides DevUI, traçage, orchestration de flux de travail |
| `/microsoft/agent-framework` | Détails API — endpoints REST DevUI, options CLI, authentification, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Interrogez la source du site Learn pour les guides pratiques, puis la source du dépôt pour les spécificités au niveau de l'API (schémas d'endpoint, configuration du proxy, jetons d'authentification).

---

## Context7 Setup

Pour toute requête Context7, résolvez d'abord l'ID de la bibliothèque (une fois par session) :

1. Appelez `mcp_context7_resolve-library-id` avec le nom de la technologie
2. Appelez `mcp_context7_query-docs` avec l'ID de bibliothèque retourné et une requête spécifique

---

## Writing Effective Queries

Soyez précis — incluez la version, l'intention et le langage :

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

Include context:
- **Version** lorsque pertinent (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Objectif de la tâche** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Langage** pour la documentation polyglotte (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Clause de non-responsabilité :
Ce document a été traduit à l'aide du service de traduction par IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un traducteur humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->