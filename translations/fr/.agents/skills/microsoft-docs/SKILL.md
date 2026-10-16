---
name: microsoft-docs
---
# Microsoft Docs

Compétence de recherche pour l'écosystème technologique Microsoft. Couvre learn.microsoft.com et la documentation qui se trouve en dehors (VS Code, GitHub, Aspire, dépôts Agent Framework).

---

## Par défaut : Microsoft Learn MCP

Utilisez ces outils pour **tout sur learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, et plus encore. C'est l'outil principal pour la grande majorité des recherches de documentation Microsoft.

| Outil | But |
|------|---------|
| `microsoft_docs_search` | Recherche sur learn.microsoft.com — concepts, guides, tutoriels, configuration |
| `microsoft_code_sample_search` | Trouve des extraits de code fonctionnels dans les docs Learn. Passez `language` (`python`, `csharp`, etc.) pour de meilleurs résultats |
| `microsoft_docs_fetch` | Récupère le contenu complet de la page à partir d'une URL spécifique (lorsque les extraits de recherche ne suffisent pas) |

Utilisez `microsoft_docs_fetch` après la recherche lorsque vous avez besoin de tutoriels complets, de toutes les options de configuration, ou lorsque les extraits de recherche sont tronqués.

---

## Exceptions : quand utiliser d'autres outils

Les catégories suivantes vivent **en dehors** de learn.microsoft.com. Utilisez l'outil spécifié à la place.

### Aspire — Utilisez Aspire MCP Server (préféré) ou Context7

La documentation Aspire se trouve sur **aspire.dev**, pas sur Learn. Le meilleur outil dépend de votre version Aspire CLI :

**CLI 13.2+** (recommandé) — Le serveur Aspire MCP inclut des outils intégrés de recherche de docs :

| Outil MCP | Description |
|----------|-------------|
| `list_docs` | Liste toute la documentation disponible depuis aspire.dev |
| `search_docs` | Recherche lexicale pondérée sur le contenu d'aspire.dev |
| `get_doc` | Récupère un document spécifique par slug |

Ceux-ci sont fournis dans Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Pour mettre à jour : `aspire update --self --channel daily`.

**CLI 13.1** — Le serveur MCP fournit une recherche d'intégration (`list_integrations`, `get_integration_docs`) mais **pas** de recherche de docs. Revenir à Context7 :

| ID de bibliothèque | Utilisé pour |
|---|---|
| `/microsoft/aspire.dev` | Principale — guides, intégrations, référence CLI, déploiement |
| `/microsoft/aspire` | Source runtime — détails internes API, détails d'implémentation |
| `/communitytoolkit/aspire` | Intégrations communautaires — Go, Java, Node.js, Ollama |

### VS Code — Utilisez Context7

La documentation VS Code se trouve sur **code.visualstudio.com**, pas sur Learn.

| ID de bibliothèque | Utilisé pour |
|---|---|
| `/websites/code_visualstudio` | Documentation utilisateur — paramètres, fonctionnalités, débogage, développement à distance |
| `/websites/code_visualstudio_api` | API des extensions — webviews, TreeViews, commandes, points de contribution |

### GitHub — Utilisez Context7

La documentation GitHub se trouve sur **docs.github.com** et **cli.github.com**.

| ID de bibliothèque | Utilisé pour |
|---|---|
| `/websites/github_en` | Actions, API, dépôts, sécurité, administration, Copilot |
| `/websites/cli_github` | Commandes et options GitHub CLI (`gh`) |

### Agent Framework — Utilisez Learn MCP + Context7

Les tutoriels Agent Framework sont sur learn.microsoft.com (utilisez `microsoft_docs_search`), mais le **dépôt GitHub** contient des détails au niveau API souvent plus à jour que la documentation publiée — en particulier la référence REST API DevUI, les options CLI, et l'intégration .NET.

| ID de bibliothèque | Utilisé pour |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriels — guides DevUI, traçage, orchestration des workflows |
| `/microsoft/agent-framework` | Détails API — points de terminaison REST DevUI, options CLI, authentification, .NET `AddDevUI`/`MapDevUI` |

**Astuce DevUI :** Interrogez d'abord la source du site Learn pour les guides pratiques, puis la source du dépôt pour les détails au niveau API (schémas des points de terminaison, configuration proxy, jetons d'authentification).

---

## Configuration Context7

Pour toute requête Context7, résolvez d'abord l'ID de bibliothèque (une fois par session) :

1. Appelez `mcp_context7_resolve-library-id` avec le nom de la technologie
2. Appelez `mcp_context7_query-docs` avec l'ID de bibliothèque retourné et une requête spécifique

---

## Rédaction de requêtes efficaces

Soyez précis — incluez la version, l'intention et la langue :

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

Incluez le contexte :
- **Version** quand pertinent (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Intention de la tâche** (`démarrage rapide`, `tutoriel`, `aperçu`, `limites`, `référence API`)
- **Langue** pour la documentation polyglotte (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->