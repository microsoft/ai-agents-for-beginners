# Resumo da API Responses (Python + Azure OpenAI)

> Todos os exemplos abaixo pressupõem `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` e que o `client` já está inicializado (ver configuração do cliente).

## Pedido básico
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Configuração do cliente — EntraID (recomendado)
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

## Configuração do cliente — chave API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Configuração async do cliente — EntraID
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

## Configuração async do cliente — EntraID com tenant explícito (multi-tenant)

Quando o recurso Azure OpenAI estiver num **tenant diferente** do padrão, passe `tenant_id` explicitamente para a credencial. Isto é comum em cenários de desenvolvimento/teste onde o tenant principal do desenvolvedor difere do tenant do recurso.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential para produção (Azure Container Apps, App Service, etc.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # identidade gerida atribuída pelo utilizador
)
# AzureDeveloperCliCredential para desenvolvimento local — tenant_id explícito é fundamental
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Cadeia: tentar a identidade gerida primeiro, recorrer ao azd CLI em fallback
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migração async do cliente — antes/depois

Antes (obsoleto):
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

Depois:
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

## Migração síncrona completa — antes/depois

Antes (legado — Chat Completions Azure OpenAI):
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

Depois (Responses API — endpoint Azure OpenAI v1):
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

## Streaming (sync)
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
        print()  # nova linha no fim
```

## Streaming (async)
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

## Streaming em app web — formato backend para frontend

Ao migrar uma app web que transmite SSE/JSONL para o frontend, o **formato da serialização no backend** muda. Projete a saída nova do backend para preservar os padrões de acesso existentes do frontend, assim, o frontend não precisa ser alterado.

**Antes** — O backend do Chat Completions normalmente serializava o dicionário `choices[0]` de cada fragmento:
```python
# Antigo: dicionário completo de escolhas serializado por segmento
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Leitura do frontend: `response.delta.content` (caminho profundo no objeto choice).

**Depois** — O backend da Responses API emite uma forma minimalista preservando o mesmo caminho de acesso no frontend:
```python
# Novo: emitir apenas o que o frontend necessita
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
O frontend continua a ler `response.delta.content` — **nenhuma alteração no frontend é necessária**.

> **Insight chave**: A forma de streaming da Responses API (`event.type` + `event.delta`) é fundamentalmente diferente da Chat Completions (`chunk.choices[0].delta.content`). Mas o contrato backend-frontend é algo que você define. Formate a saída do backend para corresponder ao que o frontend já espera.

## Sequência de eventos no streaming

Quando `stream: true`, a API emite eventos nesta ordem:
1. `response.created` – objeto resposta inicializado
2. `response.in_progress` – geração iniciada
3. `response.output_item.added` – item de saída criado
4. `response.content_part.added` – parte do conteúdo iniciada
5. `response.output_text.delta` – fragmentos de texto (múltiplos, cada um com `delta: string`)
6. `response.output_text.done` – geração de texto terminada
7. `response.content_part.done` – parte do conteúdo terminada
8. `response.output_item.done` – item de saída terminado
9. `response.completed` – resposta completa terminada

Para streaming básico de texto, trate apenas `response.output_text.delta` (para fragmentos de texto) e `response.completed` (para conclusão).

## Tratamento de erros no streaming em apps web

Durante o streaming numa app web, envolva a iteração async em `try/except` e produza erros em JSON para que o frontend possa exibi-los de forma elegante (ex.: limites de taxa, falhas temporárias):

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

> **Por que isto importa**: Azure OpenAI retorna `429 Too Many Requests` durante limitação de taxa. Sem o `try/except`, a resposta em streaming termina silenciosamente. Com ele, o frontend recebe `{"error": "Too Many Requests"}` e pode mostrar um prompt para tentar novamente.

## Tipos de eventos de streaming (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Formato da conversa
```python
# A API de Respostas suporta o formato de conversação através de um array de entrada
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

## Tratamento de erro do filtro de conteúdo

A estrutura do corpo de erro mudou de Chat Completions para Responses API.

Antes (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Depois (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Diferenças chave:
- O invólucro `innererror` **desapareceu** — os detalhes do filtro de conteúdo estão agora ao nível superior de `error.body`.
- `content_filter_result` (singular) → `content_filters` (plural, array) contendo `content_filter_results` (plural) dentro de cada entrada.
- Cada entrada em `content_filters` inclui `blocked`, `source_type`, e `content_filter_results` com detalhes por categoria (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Forma completa do corpo de erro do filtro de conteúdo da Responses API:
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

## Migração HTTP raw (requests/httpx)

Se a app chamar diretamente a REST do Azure OpenAI em vez de usar o SDK:

Antes (Chat Completions):
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

Depois (Responses API):
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

> **Nota**: `output_text` é uma propriedade de conveniência no objeto `Response` do SDK Python. A resposta JSON REST bruta não tem um campo `output_text` ao nível superior — o texto está em `output[0].content[0].text`.

## Conversas com múltiplos turnos
```python
# Construir uma conversa com a API de Respostas
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Adicionar a resposta do assistente à conversa
messages.append({"role": "assistant", "content": response.output_text})

# Continuar a conversa
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Múltiplos turnos com tipo de conteúdo (explícito `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Multi-turn com `previous_response_id` (alternativa)

Em vez de gerir você próprio a array de conversação, pode encadear respostas
no servidor usando `previous_response_id`. A API armazena cada resposta e
adiciona automaticamente os turnos anteriores.

```python
# Primeira jogada
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Jogadas subsequentes — apenas envie a nova mensagem do utilizador + ID da resposta anterior
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Quando usar cada abordagem:**

| Abordagem | Vantagens | Desvantagens |
|---|---|---|
| Array `input` (manual) | Controlo total sobre o histórico; pode podar/resumir; não necessita armazenamento no servidor (`store=False`) | Mais código; você gere a array |
| `previous_response_id` | Código mais simples; encadeamento automático | Requer `store=True` (padrão); conversa armazenada no servidor; não pode modificar o histórico entre turnos |

> **Nota de migração:** A maioria das apps Chat Completions já gerem a sua própria array de mensagens, por isso converter para array `input` é uma migração 1:1 mais direta. Use `previous_response_id` para código novo ou quando não precisar manipular o histórico da conversa.

## Modelos de raciocínio da série O (o1, o3-mini, o3, o4-mini)

Os modelos da série O têm restrições de parâmetros únicas ao migrar para Responses API.

### Correspondência de parâmetros para série O

| Chat Completions (série o) | Responses API | Notas |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Defina alto (4096+) — os tokens de raciocínio contam para o limite |
| `reasoning_effort` | `reasoning.effort` | Mantenha como está se presente (baixo/médio/alto) |
| `temperature` | Remova ou defina para `1` | Série O só aceita `1` |
| `top_p` | Remova | Não suportado na série O |
| `seed` | Remova | Não suportado na Responses API |

### Exemplo antes/depois na série O

Antes (Chat Completions com série O):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Depois (Responses API):
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

> **Nota**: Modelos da série O podem armazenar saída durante o raciocínio antes de emitir deltas de texto. O streaming funciona, mas o primeiro evento `response.output_text.delta` pode chegar após um atraso maior do que nos modelos GPT.

## Aceder tokens de raciocínio
```python
# Os modelos de raciocínio utilizam raciocínio interno — pode ver quantos tokens de raciocínio foram usados
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

> **Importante**: Use `max_output_tokens=1000` (não 50–200) para contabilizar o processo interno de raciocínio dos modelos. O modelo usa tokens de raciocínio internamente antes de gerar a saída final.

## Saída estruturada — JSON Schema
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

## Uso de ferramentas

- Defina funções em `tools` com o formato **flat da Responses API** — `name`, `description` e `parameters` ao nível superior (não aninhados sob `function`).
- Quando o modelo pedir para chamar uma ferramenta, execute-a na app e inclua o resultado da ferramenta no próximo pedido como um item `function_call_output` dentro do `input`.
- Mantenha os esquemas mínimos; valide entradas antes da execução.
- Ao usar `strict: true`, todas as propriedades devem estar listadas em `required` e `additionalProperties: false` é obrigatório.

> **⚠️ `pydantic_function_tool()` é incompatível**: O auxiliar `openai.pydantic_function_tool()` ainda gera o formato aninhado antigo do Chat Completions (`{"type": "function", "function": {"name": ...}}`). Não o use com `responses.create()`. Defina os esquemas de ferramentas manualmente ou escreva um wrapper para achatar a saída.

### Formato da definição de ferramenta

A Responses API usa um formato **flat** para ferramentas — `name`, `description`, `parameters` são chaves ao nível superior (não aninhadas sob `function`).

**Antes (Chat Completions — aninhado):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Depois (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Exemplo completo:
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

Com `strict: true` (imposição de esquema):
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
            "required": ["city_name"],       # Todas as propriedades DEVEM ser listadas
            "additionalProperties": False,   # Obrigatório para o modo estrito
        },
    }
]
```

### Ciclo de chamada de ferramenta (executar e retornar resultados)

Quando o modelo solicitar a chamada de uma ferramenta, use os itens `response.output` + `function_call_output` — **não** o padrão Chat Completions `role: assistant` + `role: tool`.

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
    # Adicionar os itens function_call do modelo à conversa
    messages.extend(response.output)

    # Executar cada ferramenta e adicionar os resultados
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Obter a resposta final com os resultados das ferramentas
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Exemplos few-shot de chamadas de ferramenta

Ao fornecer exemplos few-shot de chamadas de ferramenta em `input`, use os itens `function_call` e `function_call_output`. Os IDs devem começar com `fc_`.

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
# Exemplo integrado de pesquisa web
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Input de imagem

Os itens de conteúdo de imagem mudam o tipo de `image_url` para `input_image`, e o URL muda de objeto aninhado para string plana.

### Input de imagem — antes (Chat Completions)
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

### Input de imagem — depois (Responses API, URL)
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

### Input de imagem — depois (Responses API, base64)
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

> **Mudanças chave**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (objeto aninhado) → `"image_url": "..."` (string plana — URL HTTPS ou URI de dados `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Migração do Microsoft Agent Framework (MAF)

**Verifique primeiro a sua versão MAF** — a migração depende se está no MAF 1.0.0+ ou numa beta/rc pré-1.0.0.

Para verificar: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

No MAF 1.0.0+, `OpenAIChatClient` **já usa a Responses API** — não é necessária migração.

Se o código usar o legado `OpenAIChatCompletionClient` (que usa `chat.completions.create`), substitua por `OpenAIChatClient`:

Antes:
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

Depois:
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

### MAF pré-1.0.0 (versões beta/rc)

No MAF pré-1.0.0, `OpenAIChatClient` usava Chat Completions. Atualize para `agent-framework-openai>=1.0.0` onde o `OpenAIChatClient` usa por padrão a Responses API.

> **Nota**: As APIs `Agent`, `MCPStreamableHTTPTool` e outras do MAF permanecem inalteradas — só mudam o import e a instanciação da classe cliente.

## Migração LangChain (`langchain-openai`)

Adicione `use_responses_api=True` ao `ChatOpenAI()`. Atualize também o acesso ao conteúdo da mensagem de `.content` para `.text`.

Antes:
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

# ... invocação do agente ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Depois:
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

# ... invocação do agente ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Mudanças chave**: (1) `use_responses_api=True` no construtor, (2) `.content` → `.text` nas mensagens de resposta.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->