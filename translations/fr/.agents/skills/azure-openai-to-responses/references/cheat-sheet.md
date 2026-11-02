# Fiche technique de l’API Responses (Python + Azure OpenAI)

> Tous les extraits ci-dessous supposent que `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` et que `client` est déjà initialisé (voir configuration du client).

## Requête basique
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Configuration du client — EntraID (recommandé)
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Configuration du client — clé API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Configuration asynchrone du client — EntraID
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AsyncOpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Configuration asynchrone du client — EntraID avec locataire explicite (multi-locataire)

Lorsque la ressource Azure OpenAI est dans un **locataire différent** du locataire par défaut, passez explicitement `tenant_id` à l’accréditation. Ceci est courant dans les scénarios de dev/test où le locataire principal du développeur diffère de celui de la ressource.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential pour la production (Azure Container Apps, App Service, etc.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # identité gérée attribuée par l'utilisateur
)
# AzureDeveloperCliCredential pour le développement local — l'ID de locataire explicite est crucial
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Chaîne : essayer d'abord l'identité gérée, revenir à azd CLI en cas d'échec
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migration asynchrone du client — avant/après

Avant (obsolète) :
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

Après :
```python
from openai import AsyncOpenAI

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)

resp = await client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Migration complète synchronisée — avant/après

Avant (ancien — Complétions de chat Azure OpenAI) :
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

Après (API Responses — point de terminaison Azure OpenAI v1) :
```python
from openai import OpenAI
import os

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Streaming (synchronisé)
```python
stream = client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()  # nouvelle ligne à la fin
```

## Streaming (asynchrone)
```python
stream = await client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
async for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()
```

## Streaming d’application web — backend vers frontend

Lors de la migration d’une application web qui stream SSE/JSONL vers un frontend, le **format de sérialisation backend** change. Concevez la nouvelle sortie backend pour préserver les modèles d’accès existants du frontend afin qu’il n’ait pas besoin de modifications.

**Avant** — Le backend Chat Completions sérialisait généralement le dictionnaire `choices[0]` de chaque fragment :
```python
# Ancien : dictionnaire complet de choix sérialisé par segment
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Lecture frontend : `response.delta.content` (chemin profond dans l’objet choice).

**Après** — Le backend Responses API émet une forme minimale préservant le même chemin d’accès frontend :
```python
# Nouveau : émettre uniquement ce dont le frontend a besoin
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Le frontend lit toujours `response.delta.content` — **aucune modification frontend nécessaire**.

> **Insight clé** : La forme de streaming de l’API Responses (`event.type` + `event.delta`) est fondamentalement différente de Chat Completions (`chunk.choices[0].delta.content`). Mais votre contrat backend-vers-frontend vous appartient. Façonnez la sortie backend pour correspondre à ce que le frontend attend déjà.

## Séquence des événements de streaming

Quand `stream: true`, l’API émet les événements dans cet ordre :
1. `response.created` – objet réponse initialisé
2. `response.in_progress` – génération démarrée
3. `response.output_item.added` – élément de sortie créé
4. `response.content_part.added` – partie de contenu commencée
5. `response.output_text.delta` – fragments de texte (multiples, chacun avec `delta : string`)
6. `response.output_text.done` – génération de texte terminée
7. `response.content_part.done` – partie de contenu terminée
8. `response.output_item.done` – élément de sortie terminé
9. `response.completed` – réponse complète terminée

Pour le streaming texte basique, ne gérez que `response.output_text.delta` (pour les fragments de texte) et `response.completed` (pour la fin).

## Gestion des erreurs de streaming dans les applications web

Lors du streaming dans une application web, encapsulez l’itération asynchrone dans un `try/except` et émettez les erreurs en JSON afin que le frontend puisse les afficher proprement (par exemple, limites de débit, échecs transitoires) :

```python
@stream_with_context
async def response_stream():
    chat_coroutine = client.responses.create(
        model=deployment,
        input=all_messages,
        max_output_tokens=1000,
        stream=True,
        store=False,
    )
    try:
        async for event in await chat_coroutine:
            if event.type == "response.output_text.delta":
                yield json.dumps({"delta": {"content": event.delta}}) + "\n"
            elif event.type == "response.completed":
                yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
    except Exception as e:
        current_app.logger.error(e)
        yield json.dumps({"error": str(e)}) + "\n"
```

> **Pourquoi c’est important** : Azure OpenAI retourne `429 Too Many Requests` lors du throttling. Sans le `try/except`, la réponse en streaming meurt silencieusement. Avec cela, le frontend reçoit `{"error": "Too Many Requests"}` et peut afficher une demande de reprise.

## Types d’événements de streaming (SDK Python)

- `ResponseTextDeltaEvent` : `type='response.output_text.delta'`, `delta : str`
- `ResponseCompletedEvent` : `type='response.completed'`, `response : Response`

## Format de conversation
```python
# L'API de réponses prend en charge le format de conversation via un tableau d'entrée
response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are an Azure cloud architect."},
        {"role": "user", "content": "Design a scalable web application architecture."},
    ],
    max_output_tokens=1000,
)
print(response.output_text)
```

## Gestion des erreurs filtre de contenu

La structure du corps d’erreur a changé de Chat Completions à Responses API.

Avant (Chat Completions) :
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Après (Responses API) :
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Différences clés :
- L’enveloppe `innererror` a **disparu** — les détails du filtre de contenu sont maintenant au niveau supérieur de `error.body`.
- `content_filter_result` (singulier) → `content_filters` (tableau pluriel) contenant `content_filter_results` (pluriel) dans chaque entrée.
- Chaque entrée de `content_filters` inclut `blocked`, `source_type`, et `content_filter_results` avec détails par catégorie (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Forme complète du corps d’erreur filtre de contenu Responses API :
```json
{
  "message": "The response was filtered...",
  "type": "invalid_request_error",
  "param": "prompt",
  "code": "content_filter",
  "content_filters": [
    {
      "blocked": true,
      "source_type": "prompt",
      "content_filter_results": {
        "jailbreak": { "detected": true, "filtered": true },
        "hate": { "filtered": false, "severity": "safe" },
        "sexual": { "filtered": false, "severity": "safe" },
        "violence": { "filtered": false, "severity": "safe" },
        "self_harm": { "filtered": false, "severity": "safe" }
      }
    }
  ]
}
```

## Migration HTTP brute (requests/httpx)

Si l’application appelle directement Azure OpenAI REST au lieu d’utiliser le SDK :

Avant (Chat Completions) :
```python
endpoint = f"{azure_endpoint}/openai/deployments/{deployment}/chat/completions?api-version=2024-03-01-preview"
data = {
    "messages": [{"role": "user", "content": query}],
    "model": model_name,
    "temperature": 0,
}
response = requests.post(endpoint, headers=headers, json=data)
message = response.json()["choices"][0]["message"]["content"]
```

Après (Responses API) :
```python
endpoint = f"{azure_endpoint}/openai/v1/responses"
data = {
    "model": deployment,
    "input": [{"role": "user", "content": query}],
    "temperature": 0,
    "max_output_tokens": 1000,
    "store": False,
}
response = requests.post(endpoint, headers=headers, json=data)
output_text = response.json()["output"][0]["content"][0]["text"]
```

> **Note** : `output_text` est une propriété de commodité de l’objet `Response` du SDK Python. La réponse JSON REST brute n’a pas de champ `output_text` au niveau supérieur — le texte est à `output[0].content[0].text`.

## Conversation multi-tours
```python
# Construire une conversation avec l'API Responses
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Ajouter la réponse de l'assistant à la conversation
messages.append({"role": "assistant", "content": response.output_text})

# Continuer la conversation
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Multi-tours typé contenu (avec `input_text`/`output_text` explicite) :
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Multi-tours via `previous_response_id` (alternative)

Au lieu de gérer vous-même le tableau de conversation, vous pouvez chaîner les réponses
côté serveur avec `previous_response_id`. L’API stocke chaque réponse et
préfixe automatiquement les tours précédents.

```python
# Premier tour
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Tours suivants — il suffit de transmettre le nouveau message utilisateur + l'ID de la réponse précédente
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Quand utiliser quoi :**

| Approche | Avantages | Inconvénients |
|---|---|---|
| Tableau `input` (manuel) | Contrôle total de l’historique ; possible de tronquer/résumer ; pas besoin de stockage côté serveur (`store=False`) | Plus de code ; vous gérez le tableau |
| `previous_response_id` | Code plus simple ; chaînage automatique | Nécessite `store=True` (par défaut) ; conversation stockée côté serveur ; impossible de modifier l’historique entre les tours |

> **Note migration :** La plupart des applications Chat Completions gèrent déjà leur propre tableau de messages, donc passer au tableau `input` est une migration 1:1 plus directe. Utilisez `previous_response_id` pour le code nouveau ou quand la manipulation de l’historique n’est pas nécessaire.

## Modèles de raisonnement série O (o1, o3-mini, o3, o4-mini)

Les modèles série O ont des contraintes de paramètre uniques lors de la migration vers Responses API.

### Correspondance des paramètres pour la série O

| Chat Completions (série O) | Responses API | Notes |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Régler haut (4096+) — les tokens de raisonnement comptent dans la limite |
| `reasoning_effort` | `reasoning.effort` | Conserver tel quel si présent (low/medium/high) |
| `temperature` | Supprimer ou mettre à `1` | La série O accepte uniquement `1` |
| `top_p` | Supprimer | Non supporté sur la série O |
| `seed` | Supprimer | Non supporté dans Responses API |

### Série O avant/après

Avant (Chat Completions avec série O) :
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Après (Responses API) :
```python
resp = client.responses.create(
    model=deployment,
    input="Solve this step by step: 2x + 5 = 13",
    max_output_tokens=4096,
    reasoning={"effort": "medium"},
    store=False,
)
print(resp.output_text)
```

> **Note** : Les modèles série O peuvent tamponner la sortie lors du raisonnement avant d’émettre des deltas de texte. Le streaming fonctionne toujours mais le premier événement `response.output_text.delta` peut arriver avec un délai plus long qu’avec les modèles GPT.

## Accéder aux tokens de raisonnement
```python
# Les modèles de raisonnement utilisent le raisonnement interne — vous pouvez voir combien de jetons de raisonnement ont été utilisés
response = client.responses.create(
    model=deployment,
    input="Explain quantum computing in simple terms",
    max_output_tokens=1000,
)
print(response.output_text)
print(f"Status: {response.status}")
print(f"Reasoning tokens: {response.usage.output_tokens_details.reasoning_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
```

> **Important** : Utilisez `max_output_tokens=1000` (pas 50–200) pour tenir compte du processus interne de raisonnement des modèles de raisonnement. Le modèle utilise des tokens de raisonnement en interne avant de générer la sortie finale.

## Sortie structurée — JSON Schema
```python
resp = client.responses.create(
    model=deployment,
    input="What is the capital of France?",
    max_output_tokens=500,
    text={
        "format": {
            "type": "json_schema",
            "name": "Output",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {"answer": {"type": "string"}},
                "required": ["answer"],
                "additionalProperties": False,
            },
        }
    },
    store=False,
)
import json
data = json.loads(resp.output_text)
print(data["answer"])
```

## Utilisation d’outils

- Définissez les fonctions dans `tools` avec le **format plat de l’API Responses** — `name`, `description`, et `parameters` au niveau supérieur (pas imbriqués sous `function`).
- Quand le modèle demande d’appeler un outil, exécutez-le dans votre application et incluez le résultat de l’outil dans la requête suivante en tant qu’élément `function_call_output` dans `input`.
- Gardez les schémas minimaux ; validez les entrées avant exécution.
- En utilisant `strict: true`, toutes les propriétés doivent être listées dans `required` et `additionalProperties: false` est obligatoire.

> **⚠️ `pydantic_function_tool()` est incompatible** : Le helper `openai.pydantic_function_tool()` génère encore l’ancien format imbriqué Chat Completions (`{"type": "function", "function": {"name": ...}}`). Ne l’utilisez pas avec `responses.create()`. Définissez les schémas d’outils manuellement ou écrivez un wrapper pour aplatir la sortie.

### Format de définition d’outil

L’API Responses utilise un format d’outil **plat** — `name`, `description`, `parameters` sont des clés au niveau supérieur (pas imbriquées sous `function`).

**Avant (Chat Completions — imbriqué) :**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Après (Responses API — plat) :**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Exemple complet :
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are a weather chatbot."},
        {"role": "user", "content": "What's the weather in Berkeley?"},
    ],
    tools=tools,
    tool_choice="auto",
    store=False,
)
```

Avec `strict: true` (application stricte du schéma) :
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],       # Toutes les propriétés DOIVENT être listées
            "additionalProperties": False,   # Requis pour le mode strict
        },
    }
]
```

### Aller-retour d’appel d’outil (exécuter et retourner les résultats)

Quand le modèle demande un appel d’outil, utilisez les éléments `response.output` + `function_call_output` — **pas** le pattern Chat Completions `role: assistant` + `role: tool`.

```python
import json

messages = [
    {"role": "system", "content": "You are a weather chatbot."},
    {"role": "user", "content": "Is it sunny in Berkeley?"},
]

response = client.responses.create(
    model=deployment, input=messages, tools=tools, store=False,
)

tool_calls = [item for item in response.output if item.type == "function_call"]
if tool_calls:
    # Ajouter les éléments function_call du modèle à la conversation
    messages.extend(response.output)

    # Exécuter chaque outil et ajouter les résultats
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Obtenir la réponse finale avec les résultats des outils
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Exemples d’appels d’outil few-shot

Lorsque vous fournissez des exemples few-shot d’appels d’outil dans `input`, utilisez les éléments `function_call` et `function_call_output`. Les IDs doivent commencer par `fc_`.

```python
messages = [
    {"role": "system", "content": "You are a product search assistant."},
    {"role": "user", "content": "Find climbing gear for outdoors"},
    {
        "type": "function_call",
        "id": "fc_example1",
        "call_id": "call_example1",
        "name": "search_database",
        "arguments": '{"search_query": "climbing gear outdoor"}',
    },
    {
        "type": "function_call_output",
        "call_id": "call_example1",
        "output": "Results: ...",
    },
    {"role": "user", "content": "Now find shoes under $50"},
]
```

```python
# Exemple de recherche web intégrée
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Entrée image

Les items de contenu image changent de type `image_url` à `input_image`, et l’URL change d’un objet imbriqué à une chaîne plate.

### Entrée image — avant (Chat Completions)
```python
resp = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

### Entrée image — après (Responses API, URL)
```python
resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": "https://example.com/image.jpg",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

### Entrée image — après (Responses API, base64)
```python
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("path_to_your_image.jpg")

resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

> **Changements clés** : (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (objet imbriqué) → `"image_url": "..."` (chaîne plate — soit URL HTTPS soit URI de données `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Migration Microsoft Agent Framework (MAF)

**Vérifiez d’abord votre version de MAF** — la migration dépend si vous êtes sur MAF 1.0.0+ ou une bêta/rc pré-1.0.0.

Pour vérifier : `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Dans MAF 1.0.0+, `OpenAIChatClient` **utilise déjà l’API Responses** — pas besoin de migration.

Si la base de code utilise l’ancien `OpenAIChatCompletionClient` (qui utilise `chat.completions.create`), remplacez-le par `OpenAIChatClient` :

Avant :
```python
from agent_framework.openai import OpenAIChatCompletionClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatCompletionClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

Après :
```python
from agent_framework.openai import OpenAIChatClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

### MAF pré-1.0.0 (versions beta/rc)

Dans MAF pré-1.0.0, `OpenAIChatClient` utilisait Chat Completions. Mettez à jour vers `agent-framework-openai>=1.0.0` où `OpenAIChatClient` utilise par défaut l’API Responses.

> **Note** : Les APIs `Agent`, `MCPStreamableHTTPTool`, et autres de MAF restent inchangées — seul le import et l’instanciation de la classe client changent.

## Migration LangChain (`langchain-openai`)

Ajoutez `use_responses_api=True` à `ChatOpenAI()`. Mettez aussi à jour l’accès au contenu des messages de `.content` à `.text`.

Avant :
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
)

# ... invocation d'agent ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Après :
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
    use_responses_api=True,
)

# ... invocation d'agent ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Changements clés** : (1) `use_responses_api=True` dans le constructeur, (2) `.content` → `.text` sur les messages de réponse.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->