# Migration de l'infrastructure de test

Lors de la migration d'une base de code de Chat Completions vers l'API Responses, **les tests cassent de manière prévisible**. Cette référence explique ce qu'il faut corriger.

---

## Simulation des réponses en streaming (Python pytest)

### Classes mock principales

```python
class MockResponseEvent:
    """Simulates a Responses API streaming event."""
    def __init__(self, event_type: str, delta: str | None = None):
        self.type = event_type
        self.delta = delta

class AsyncResponseIterator:
    """Async iterator that yields Responses API streaming events from a string answer."""
    def __init__(self, answer: str):
        self.event_index = 0
        self.events = []
        for i, word in enumerate(answer.split(" ")):
            # Préserver les espaces : ajouter un espace avant tous les mots sauf le premier
            if i > 0:
                word = " " + word
            self.events.append(MockResponseEvent("response.output_text.delta", delta=word))
        self.events.append(MockResponseEvent("response.completed"))

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.event_index < len(self.events):
            event = self.events[self.event_index]
            self.event_index += 1
            return event
        raise StopAsyncIteration
```

### Routage des réponses mock selon le contenu du message

Les applications réelles retournent différentes réponses selon le prompt. Routez par `input` (pas par `messages`) :

```python
async def mock_acreate(*args, **kwargs):
    # L'API Responses utilise 'input' et non 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Chemins de monkeypatch

| Type de client | Chemin du monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **Avant** (Chat Completions) : `openai.resources.chat.AsyncCompletions.create`
> **Après** (Responses) : `openai.resources.responses.AsyncResponses.create`

### Exemple complet de fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Classes MockResponseEvent et AsyncResponseIterator ici ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Mettre à jour les mocks de fixtures

Remplacez les mocks basés sur `ChatCompletionChunk` par le pattern `MockResponseEvent` / `AsyncResponseIterator` ci-dessus. Changements clés :

| Avant (mock Chat Completions) | Après (mock Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` dans un chunk | `event.type == "response.completed"` |
| Chunk spécifique Azure `prompt_filter_results` | Supprimer entièrement |
| `content_filter_results` spécifique Azure par choix | Supprimer entièrement |
| `kwargs.get("messages")` dans le mock | `kwargs.get("input")` dans le mock |

---

## 2. Mettre à jour les snapshots / fichiers golden

Si la suite de test utilise du snapshot testing (ex. `pytest-snapshot`, syrupy, ou snapshots JSONL maison), la structure attendue change :

**Avant** (Chat Completions streaming JSONL) :
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Après** (Responses API streaming JSONL) :
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

La nouvelle structure est beaucoup plus simple — plus de champs `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` ou `content_filter_results`. Mettez à jour ou régénérez tous les fichiers snapshot.

> **Astuce** : Lancez les tests avec `--snapshot-update` (pytest-snapshot) ou `--update-snapshots` (syrupy) après la migration pour auto-régénérer.

---

## 3. Mettre à jour les assertions des tests

Cassures d'assertions fréquentes :

| Ancienne assertion | Problème | Nouvelle assertion |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` n'a pas d'attribut `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` et `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Pas de `api_version` sur `OpenAI`/`AsyncOpenAI` | Supprimer entièrement |
| `isinstance(client, AsyncAzureOpenAI)` | Type de client changé | `isinstance(client, AsyncOpenAI)` |

---

## 4. Mettre à jour les variables d'environnement dans les fixtures de test

Les tests définissent souvent des variables d'env via `monkeypatch.setenv`. Mettez-les à jour :

| Ancienne var env | Nouvelle var env | Remarques |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Convention standard du SDK Azure Identity |
| `AZURE_OPENAI_VERSION` | Supprimer | Pas besoin de `api_version` |
| `AZURE_OPENAI_API_VERSION` | Supprimer | Pas besoin de `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | À garder (toujours nécessaire pour `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | À garder (nom du déploiement pour le paramètre `model`) |

---

## 5. Recherchez le code de test nécessitant une migration

```bash
# Modèles hérités spécifiques aux tests
rg "ChatCompletionChunk" tests/
rg "AsyncCompletions\.create" tests/
rg "chat\.completions" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results" tests/
rg "content_filter_results" tests/
rg "AZURE_OPENAI_VERSION|AZURE_OPENAI_API_VERSION" tests/
rg "AZURE_OPENAI_CLIENT_ID" tests/
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->