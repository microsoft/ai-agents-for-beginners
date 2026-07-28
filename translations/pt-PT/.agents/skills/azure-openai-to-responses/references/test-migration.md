# Migração da Infraestrutura de Testes

Ao migrar uma base de código de Chat Completions para Responses API, **os testes quebram de maneiras previsíveis**. Esta referência cobre o que corrigir.

---

## Simulação de Respostas em Streaming (Python pytest)

### Classes principais de mock

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
            # Preservar espaços em branco: adicionar espaço antes de todas as palavras exceto a primeira
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

### Direcionar respostas simuladas pelo conteúdo da mensagem

Aplicações reais fornecem respostas diferentes com base no prompt. Direcione por `input` (não por `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # A API de Respostas usa 'input' e não 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Caminhos para monkeypatch

| Tipo de cliente | Caminho do monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sincrónico) | `openai.resources.responses.Responses.create` |

> **Antes** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Depois** (Responses): `openai.resources.responses.AsyncResponses.create`

### Exemplo completo de fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Classes MockResponseEvent e AsyncResponseIterator aqui ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Atualizar fixtures de mock

Substitua os mocks baseados em `ChatCompletionChunk` pelo padrão `MockResponseEvent` / `AsyncResponseIterator` acima. Alterações principais:

| Antes (mock de Chat Completions) | Depois (mock de Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` no chunk | `event.type == "response.completed"` |
| Chunk específico Azure `prompt_filter_results` | Remover completamente |
| `content_filter_results` por escolha específico Azure | Remover completamente |
| `kwargs.get("messages")` no mock | `kwargs.get("input")` no mock |

---

## 2. Atualizar ficheiros snapshot / golden

Se a suíte de testes usa snapshot testing (por exemplo, `pytest-snapshot`, syrupy, ou snapshots JSONL feitos à mão), a forma esperada de saída muda:

**Antes** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Depois** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

A nova forma é dramaticamente mais simples — sem campos `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, ou `content_filter_results`. Atualize ou regenere todos os ficheiros snapshot.

> **Dica**: Execute os testes com `--snapshot-update` (pytest-snapshot) ou `--update-snapshots` (syrupy) após a migração para auto-regenerar.

---

## 3. Atualizar afirmações nos testes

Quebras comuns em asserções:

| Afirmação antiga | Problema | Nova afirmação |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` não tem atributo `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` e `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Sem `api_version` em `OpenAI`/`AsyncOpenAI` | Remover completamente |
| `isinstance(client, AsyncAzureOpenAI)` | Tipo de cliente alterado | `isinstance(client, AsyncOpenAI)` |

---

## 4. Atualizar variáveis ambientais em fixtures de teste

Os testes frequentemente definem variáveis ambientais via `monkeypatch.setenv`. Atualize estas:

| Variável ambiental antiga | Variável ambiental nova | Notas |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Convenção padrão do SDK Azure Identity |
| `AZURE_OPENAI_VERSION` | Remover | Não é necessário `api_version` |
| `AZURE_OPENAI_API_VERSION` | Remover | Não é necessário `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Manter (ainda necessário para `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Manter (nome do deployment para parâmetro `model`) |

---

## 5. Procure por código de teste que precisa de migração

```bash
# Padrões legados específicos para testes
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
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->