---
name: azure-openai-to-responses
license: MIT
---
# Migrer les applications Python des Azure OpenAI Chat Completions vers l’API Responses

> **GUIDANCE AUTORITAIRE — SUIVRE EXACTEMENT**
>
> Cette compétence migre les bases de code Python utilisant Azure OpenAI Chat Completions
> vers l’API unifiée Responses. Suivez ces instructions précisément.
> Ne pas improviser les correspondances de paramètres ni inventer de formes d’API.

---

## Déclencheurs

Activez cette compétence lorsque l’utilisateur souhaite :
- Migrer une application Python d’Azure OpenAI Chat Completions vers l’API Responses
- Mettre à jour l’usage du SDK OpenAI Python vers la forme d’API la plus récente contre Azure OpenAI
- Préparer du code Python pour GPT-5 ou modèles plus récents nécessitant Responses sur Azure
- Passer de `AzureOpenAI`/`AsyncAzureOpenAI` au client standard `OpenAI`/`AsyncOpenAI` avec le point de terminaison v1
- Corriger les avertissements de dépréciation liés aux constructeurs `AzureOpenAI` ou `api_version`

---

## ⚠️ Compatibilité modèle — VÉRIFIER D’ABORD

> **Avant de migrer, vérifiez que votre déploiement Azure OpenAI supporte l’API Responses.**

### 1. Test rapide de votre déploiement (le plus rapide)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **Note** : `max_output_tokens` a un **minimum de 16** sur Azure OpenAI. Les valeurs inférieures à 16 renvoient une erreur 400. Utilisez 50+ pour les tests rapides.

Si cela renvoie une 404, le modèle du déploiement ne supporte pas encore Responses — consultez la référence ci-dessous ou redéployez avec un modèle pris en charge.

### 2. Vérifier les modèles disponibles dans votre région (recommandé)

Lancez l’outil intégré de compatibilité des modèles pour voir ce qui est disponible avec le support de l’API Responses dans votre région spécifique :

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Cette requête interroge Azure ARM en direct et présente une matrice de compatibilité — quels modèles supportent Responses, la sortie structurée, les outils, etc. Utilisez `--filter gpt-5.1,gpt-5.2` pour restreindre les résultats ou `--json` pour du script.

### 3. Référence complète du support des modèles

- **Requête en direct** : `python migrate.py models` (voir ci-dessus — spécifique à la région, toujours à jour)
- **Consultez disponibilité** : [Tableau récapitulatif des modèles et disponibilité par région](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Démarrage rapide & guide** : **https://aka.ms/openai/start**

### ⚠️ Limitations des anciens modèles

> **ATTENTION** : Les anciens modèles (antérieurs à `gpt-4.1`) ne supportent peut-être pas toutes les fonctionnalités de l’API Responses pleinement.
>
> Limitations connues avec les anciens modèles :
> - **Paramètre `reasoning`** : Non supporté sur de nombreux modèles non orientés raisonnement. Ne migrez `reasoning` que s’il était déjà présent dans le code original.
> - **Paramètre `seed`** : Pas du tout supporté dans l’API Responses — retirez-le de toutes les requêtes.
> - **Sortie structurée via `text.format`** : Les anciens modèles peuvent ne pas appliquer les schémas JSON en `strict: true` de façon fiable.
> - **Orchestration d’outils** : GPT-5+ orchestre les appels aux outils comme partie intégrante du raisonnement interne. Les anciens modèles Responses fonctionnent toujours mais sans cette intégration profonde.
> - **Contraintes de température** : Lors de la migration vers `gpt-5`, la température doit être omise ou fixée à `1`. Les anciens modèles n’ont pas cette contrainte.

### Modèles reasoning série O (o1, o3-mini, o3, o4-mini)

Les modèles O-series ont des contraintes paramétriques uniques. Lors de la migration d’applications ciblant les modèles de la série O :

- **`temperature`** : Doit être `1` (ou omis). Les modèles O-series n’acceptent pas d’autres valeurs.
- **`max_completion_tokens` → `max_output_tokens`** : Les apps utilisant le paramètre spécifique Azure `max_completion_tokens` doivent passer à `max_output_tokens`. Mettez des valeurs élevées (4096+) car les tokens de raisonnement comptent dans la limite.
- **`reasoning_effort`** : Si l’app utilise `reasoning_effort` (low/medium/high), conservez-le — l’API Responses supporte ce paramètre pour les modèles de la série O.
- **Comportement du streaming** : Les modèles O-series peuvent bufferiser la sortie jusqu’à ce que le raisonnement soit terminé avant d’émettre les événements texte delta. Le streaming fonctionne toujours, mais le premier `response.output_text.delta` peut arriver avec un délai plus long qu’avec les modèles GPT.
- **`top_p`** : Non supporté sur la série O — supprimez-le s’il est présent.
- **Utilisation des outils** : Les modèles O-series supportent les outils via l’API Responses de la même façon que les modèles GPT, mais la qualité d’orchestration des appels aux outils varie selon le modèle.

**Action — conseil proactif sur le modèle** : Pendant la phase de scan, vérifiez quel modèle l’app cible (noms de déploiement, variables d’environnement, configuration). Si le modèle est antérieur à `gpt-4.1` (pas gpt-4.1+), informez proactivement l’utilisateur :
- La migration fonctionnera pour le texte de base, le chat, le streaming, et les outils sur leur modèle actuel.
- Les modèles plus récents (`gpt-5.1`, `gpt-5.2`) offrent une meilleure orchestration des outils, une application stricte de la sortie structurée, le raisonnement, et une disponibilité inter-régions.
- Ils devraient envisager de mettre à jour leur déploiement quand ils seront prêts — cela ne bloque pas la migration.

Ne bloquez pas ni ne refusez la migration en fonction de la version du modèle. Le conseil est informatif.

### Les GitHub Models ne supportent PAS l’API Responses

> **Les GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) ne supportent pas l’API Responses.**

Si la base de code utilise une voie GitHub Models (cherchez `base_url` pointant vers `models.github.ai` ou `models.inference.ai.azure.com`), **retirez-la entièrement** lors de la migration. L’API Responses nécessite Azure OpenAI, OpenAI, ou un point de terminaison local compatible (ex : Ollama avec support Responses).

Action lors du scan :
- Signalez tout chemin GitHub Models à supprimer.

---

## Migration des frameworks

De nombreuses applications utilisent des frameworks de haut niveau par-dessus OpenAI. Lors de leur migration, l’API du framework change — pas seulement les appels OpenAI sous-jacents.

### Microsoft Agent Framework (MAF)

**Vérifiez d’abord votre version MAF** — la migration dépend si vous êtes sur MAF 1.0.0+ ou une beta/rc pré-1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **utilise déjà l’API Responses** — pas de migration nécessaire. Si la base de code utilise l’ancien `OpenAIChatCompletionClient` (qui utilise `chat.completions.create`), remplacez-le par `OpenAIChatClient`.

| Avant | Après |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Pour vérifier votre version : `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pré-1.0.0 (versions beta/rc)

Dans MAF pré-1.0.0, `OpenAIChatClient` utilisait Chat Completions. Mettez à jour vers `agent-framework-openai>=1.0.0` où `OpenAIChatClient` utilise l’API Responses par défaut.

Pas d’autres changements nécessaires — les APIs `Agent` et des outils restent identiques.

### LangChain (`langchain-openai`)

Ajoutez `use_responses_api=True` à `ChatOpenAI()`. Mettez aussi à jour l’accès à la réponse de `.content` à `.text`.

| Avant | Après |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Pour des exemples complets avant/après, consultez [cheat-sheet.md](./references/cheat-sheet.md).

---

## Conseils de migration Frontend

> **L’API Responses est une préoccupation côté serveur.** Migrez votre backend Python ; le contrat HTTP du frontend doit rester inchangé sauf si votre backend est un simple relais — dans ce cas, envisagez d’adopter la forme de requête Responses pour éliminer une couche de traduction. Si le frontend appelle OpenAI directement avec une clé côté client, déplacez ces appels d’abord vers un backend.

### Dépréciation de `@microsoft/ai-chat-protocol`

Le paquet npm `@microsoft/ai-chat-protocol` est déprécié et doit être remplacé par [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Si vous le rencontrez dans un frontend :

1. Remplacez la balise script CDN :
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Supprimez l’instanciation de `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Remplacez `client.getStreamedCompletion(messages)` par un appel direct `fetch()` au point de terminaison backend en streaming.
4. Remplacez `for await (const response of result)` par `for await (const chunk of readNDJSONStream(response.body))`.
5. Mettez à jour l’accès aux propriétés de `response.delta.content` / `response.error` vers `chunk.delta.content` / `chunk.error`.

---

## Objectifs

- Énumérer tous les sites d’appel Python utilisant Chat Completions ou Completions legacy contre Azure OpenAI.
- Proposer un plan de migration et un ordonnancement pour la base de code Python.
- Appliquer des modifications sûres et minimales pour passer à l’API Responses.
- Mettre à jour les consommateurs pour utiliser le schéma de sortie Responses ; pas de wrappers rétrocompatibles.
- Exécuter tests/lints ; corriger les cassures triviales introduites par la migration.
- Préparer des ensembles de modifications petits et révisables et fournir un résumé final avec diffs (ne pas committer).

---

## Garde-fous

- Ne modifier que les fichiers à l’intérieur de l’espace git. Ne jamais écrire à l’extérieur.
- Ne pas conserver de shim de rétrocompatibilité ; migrez le code vers la nouvelle forme d’API.
- Ne pas laisser de commentaires tombstones/de transition ou fichiers de sauvegarde.
- Préserver la sémantique streaming si utilisée précédemment ; sinon utiliser non-streaming.
- Demander l’approbation avant d’exécuter commandes ou appels réseau si en mode approbation.
- Ne pas exécuter `git add`/`git commit`/`git push` ; produire uniquement des modifications dans l’arbre de travail.

---

## Étape 0 : Migration du client Azure OpenAI (prérequis)

Si la base de code utilise les constructeurs `AzureOpenAI` ou `AsyncAzureOpenAI`, migrez d’abord vers les constructeurs standard `OpenAI` / `AsyncOpenAI`. Les constructeurs spécifiques Azure sont dépréciés dans `openai>=1.108.1`.

### Pourquoi le chemin API v1 ?

Le nouveau point de terminaison `/openai/v1` utilise le client standard `OpenAI()` au lieu de `AzureOpenAI()`, ne requiert pas de paramètre `api_version`, et fonctionne de façon identique sur OpenAI et Azure OpenAI. Le même code client est pérenne — pas de gestion de version nécessaire.

### Changements clés

| Avant | Après |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Supprimé totalement |

### Liste de nettoyage

- Supprimer l’argument `api_version` de la construction client.
- Supprimer les variables d’environnement `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` du `.env`, paramètres d’app, et fichiers Bicep/infra.
- Renommer `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` dans `.env`, paramètres d’app, Bicep/infra, et fixtures de test (convention standard SDK Azure Identity).
- Assurer `openai>=1.108.1` dans `requirements.txt` ou `pyproject.toml`.

### Migration des variables d’environnement

| Ancienne var env | Action | Notes |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Supprimer** | Pas d’`api_version` requis avec le point de terminaison v1 |
| `AZURE_OPENAI_API_VERSION` | **Supprimer** | Idem ci-dessus |
| `AZURE_OPENAI_CLIENT_ID` | **Renommer** → `AZURE_CLIENT_ID` | Convention standard SDK Azure Identity pour `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Conserver** | Toujours nécessaire pour construire `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Conserver** | Utilisé comme paramètre `model` dans `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Conserver** | Utilisé comme `api_key` pour l’authentification par clé |

Pour des exemples de configuration client (sync, async, EntraID, clé API, multi-tenant), voir [cheat-sheet.md](./references/cheat-sheet.md).

---

## Étape 1 : Détecter les sites d’appel legacy

Exécutez le script [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) pour trouver tous les sites d’appel qui nécessitent une migration :

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Ou exécutez ces recherches manuellement — chaque correspondance est une cible de migration :

```bash
# Appels API hérités (doivent être réécrits)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Constructeurs clients Azure obsolètes (doivent être remplacés)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Modèles d'accès à la forme de réponse (doivent être mis à jour)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Définitions d'outils dans l'ancien format imbriqué (doivent être aplaties)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Résultats d'outils dans l'ancien format (doivent être convertis en function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Paramètres obsolètes (doivent être supprimés ou renommés)
rg "response_format"
rg "max_tokens\b"        # renommer en max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Variables d'environnement obsolètes (nettoyage)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # devrait être AZURE_CLIENT_ID

# Points de terminaison des modèles GitHub (doivent être supprimés — API de réponses non prise en charge)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Modèles hérités au niveau cadre (doivent être mis à jour)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+ : remplacer par OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain : nécessite use_responses_api=True

# Infrastructure de test (doit être mise à jour)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Accès au corps d'erreur du filtre de contenu (doit être mis à jour — structure modifiée)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # ancienne forme singulière — maintenant content_filter_results (pluriel) dans le tableau content_filters

# Appels HTTP bruts au point de terminaison Chat Completions (doivent mettre à jour l'URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristiques (détection et réécriture)

- **Client Chat Completions** : `client.chat.completions.create` → `client.responses.create(...)`.

- **Constructeurs client Azure** : `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Outils** : convertir les définitions d’outils d’appel de fonction du format imbriqué (`{"type": "function", "function": {"name": ...}}`) au format plat Responses (`{"type": "function", "name": ...}`) ; utiliser `tool_choice` ; renvoyer les résultats d’outil sous forme d’éléments `{"type": "function_call_output", "call_id": ..., "output": ...}` (et non `{"role": "tool", ...}`).
- **Allers-retours d’outils** : lorsque le modèle retourne des appels de fonctions, ajouter les éléments `response.output` à la conversation (pas un dictionnaire manuel `{"role": "assistant", "tool_calls": [...]}`), puis ajouter les éléments `function_call_output` pour chaque résultat.
- **Exemples d’outils few-shot** : si la conversation contient des exemples codés en dur d’appels d’outils, les convertir en éléments `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. Les IDs doivent commencer par `fc_`.
- **`pydantic_function_tool()`** : cet assistant génère toujours l’ancien format imbriqué et **n’est pas compatible** avec `responses.create()`. Remplacer par des définitions manuelles ou un wrapper d’aplatissement.
- **Multi-tours** : conserver l’historique de conversation dans l’application ; transmettre les tours précédents via `input` items.
- **Formatage** : remplacer le `response_format` de premier niveau de Chat par `text.format` dans Responses. Forme canonique : `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Éléments de contenu** : remplacer le `content[].type: "text"` de Chat par `content[].type: "input_text"` dans Responses pour les tours utilisateur/système.
- **Éléments de contenu image** : remplacer le `content[].type: "image_url"` de Chat par `content[].type: "input_image"` dans Responses. Le champ `image_url` change d’un objet imbriqué `{"url": "..."}` à une chaîne plate. Voir la fiche mémo pour les exemples avant/après.
- **Effort de raisonnement** : **migrer `reasoning` uniquement s’il existe déjà dans le code original**.
- **Gestion des erreurs de filtre de contenu** : la structure du corps d’erreur a changé. Chat Completions utilisait `error.body["innererror"]["content_filter_result"]` (singulier) ; l’API Responses utilise `error.body["content_filters"][0]["content_filter_results"]` (pluriel, dans un tableau). Le code accédant à `innererror` lèvera une `KeyError`. Réécrire pour utiliser le nouveau chemin.
- **Appels HTTP bruts** : si l’application appelle directement l’API REST Azure OpenAI (via `requests`, `httpx`, etc.) avec `/openai/deployments/{name}/chat/completions?api-version=...`, réécrire en `/openai/v1/responses`. Le corps de la requête change : `messages` → `input`, ajouter `max_output_tokens` et `store: false`, supprimer le paramètre de requête `api-version`. Le corps de la réponse change : `choices[0].message.content` → `output[0].content[0].text` (note : `output_text` est une propriété pratique du SDK absente du JSON REST brut).

---

## Étape 2 : Appliquer la migration

### Notes de migration (Chat Completions → Responses)

- **Pourquoi migrer** : Responses est l’API unifiée pour texte, outils et streaming ; Chat Completions est obsolète. Avec GPT-5, Responses est requis pour la meilleure performance.
- **HTTP** : le point de terminaison Azure passe de `/openai/deployments/{name}/chat/completions` à `/openai/v1/responses`.
- **Champs** : `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` reste inchangé.
- **Formatage** : `response_format` → `text.format` avec un objet approprié.
- **Éléments de contenu** : remplacer le `content[].type: "text"` de Chat par `content[].type: "input_text"` dans Responses pour les tours système/utilisateur.
- **Éléments de contenu image** : remplacer le `content[].type: "image_url"` de Chat par `content[].type: "input_image"` dans Responses. Aplatir le champ `image_url` de `{"image_url": {"url": "..."}}` à `{"image_url": "..."}` (une chaîne simple — une URL HTTPS ou une URI de données `data:image/...;base64,...`).

### Référence de correspondance des paramètres

| Chat Completions | API Responses |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (tableau d’items) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objet) |
| `temperature` | `temperature` (inchangé) |
| `stop` | `stop` (inchangé) |
| `frequency_penalty` | `frequency_penalty` (inchangé) |
| `presence_penalty` | `presence_penalty` (inchangé) |
| `tools` / appels de fonction | `tools` (inchangé) |
| `seed` | **Supprimer** (non supporté) |
| `store` | `store` (mis à `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (chaîne plate) |

Pour des exemples complets avant/après, voir [cheat-sheet.md](./references/cheat-sheet.md).

Pour la migration de l’infrastructure de test (mocks, snapshots, assertions), voir [test-migration.md](./references/test-migration.md).

Pour la résolution des erreurs et pièges, voir [troubleshooting.md](./references/troubleshooting.md).

---

## Conservation des données et état

- Définir `store: false` sur toutes les requêtes Responses.
- Ne pas s’appuyer sur les IDs de messages précédents ou le contexte stocké côté serveur ; garder l’état géré côté client et minimiser les métadonnées.

---

## Critères d’acceptation

### Vérifications au niveau du code (toutes doivent réussir)

- [ ] Zéro correspondance pour `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` dans les fichiers migrés.
- [ ] Zéro correspondance pour `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — tous les constructeurs utilisent `OpenAI`/`AsyncOpenAI` avec le point de terminaison v1.
- [ ] Zéro correspondance pour `rg "models\.github\.ai|models\.inference\.ai\.azure"` — chemins de code GitHub Models supprimés.
- [ ] Zéro correspondance pour `rg "OpenAIChatCompletionClient"` — Le code MAF 1.0.0+ utilise `OpenAIChatClient` (qui utilise l’API Responses). En pré-1.0.0, faire la mise à jour vers `agent-framework-openai>=1.0.0`.
- [ ] Tous les appels `ChatOpenAI(...)` incluent `use_responses_api=True`.
- [ ] Zéro correspondance pour `rg "choices\[0\]"` — tout accès aux réponses utilise `resp.output_text` ou le schéma de sortie Responses.
- [ ] Pas de `response_format` au premier niveau ; toutes les sorties structurées utilisent `text={"format": {...}}`.
- [ ] `openai>=1.108.1` et `azure-identity` dans `requirements.txt` ou `pyproject.toml` ; dépendances réinstallées.
- [ ] `store=False` défini sur chaque appel `responses.create`.
- [ ] Pas de `api_version` dans la construction du client ; `AZURE_OPENAI_API_VERSION` retiré des fichiers d’environnement et de l’infra.

### Vérifications de l’infrastructure de test (toutes doivent réussir)

- [ ] Zéro correspondance pour `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Zéro correspondance pour `rg "_azure_ad_token_provider" tests/` — assertions mises à jour pour vérifier `isinstance(client, AsyncOpenAI)` ou `base_url`.
- [ ] Zéro correspondance pour `rg "prompt_filter_results|content_filter_results" tests/` — mocks de filtres spécifiques à Azure supprimés.
- [ ] Les fixtures mock utilisent `kwargs.get("input")` et non `kwargs.get("messages")`.
- [ ] Fichiers Snapshot / golden mis à jour à la forme de streaming Responses (pas de `choices[0]`, `function_call`, `logprobs`, etc.).
- [ ] `pytest` passe sans aucune erreur après toutes les mises à jour des tests.

### Vérifications comportementales (vérification manuelle ou via testeur)

- [ ] **Complétion basique** : `responses.create` sans streaming retourne un `output_text` non vide.
- [ ] **Parité de flux** : si le code original utilisait le streaming, le code migré stream et produit des événements `response.output_text.delta` avec des deltas non vides.
- [ ] **Sortie structurée** : si `text.format` avec `json_schema` est utilisé, `json.loads(resp.output_text)` réussit et correspond au schéma.
- [ ] **Boucle d’appels d’outils** : si des outils sont utilisés, le modèle effectue des appels d’outils, l’application les exécute, et la requête suivante retourne un `output_text` final (pas de boucle infinie).
- [ ] **Parité Async** : si `AsyncAzureOpenAI` était utilisé, l’équivalent `AsyncOpenAI` fonctionne avec `await`.
- [ ] **Taux d’erreur** : pas de nouvelles erreurs 400/401/404 comparé à la baseline pré-migration.

### Livrables

- Le résumé inclut les fichiers édités, les comptages avant/après des sites d’appel legacy, et les prochaines étapes.
- Les modifications sont uniquement des éditions dans l’arbre de travail (sans commits).

---

## Exigences de version du SDK

| Package | Version minimale |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Dernière (pour auth EntraID) |

---

## Références

- [Fiche Mémo — tous les extraits de code](./references/cheat-sheet.md)
- [Migration de tests — mocks, snapshots, assertions](./references/test-migration.md)
- [Dépannage — erreurs, tableau de risques, pièges](./references/troubleshooting.md)
- [detect_legacy.py — scanner automatisé](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Kit de démarrage Azure OpenAI](https://aka.ms/openai/start)
- [Docs Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Cycle de vie des versions Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Référence API OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->