# Guia Rápido da API Responses (Python + Azure OpenAI)

> Todos os exemplos abaixo assumem `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` e `client` já está inicializado (veja a configuração do client).

## Solicitação básica
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Configuração do client — EntraID (recomendado)
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

## Configuração do client — chave API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Configuração async do client — EntraID
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

## Configuração async do client — EntraID com tenant explícito (multi-tenant)

Quando o recurso Azure OpenAI está em um **tenant diferente** do padrão, passe `tenant_id` explicitamente para a credencial. Isso é comum em cenários de dev/test onde o tenant principal do desenvolvedor difere do tenant do recurso.

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
    client_id=os.getenv("AZURE_CLIENT_ID")  # identidade gerenciada atribuída ao usuário
)
# AzureDeveloperCliCredential para desenvolvimento local — tenant_id explícito é crítico
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Cadeia: tente a identidade gerenciada primeiro, volte para o CLI azd em caso de falha
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migração async do client — antes/depois

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

## Migração completa sincronizada — antes/depois

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
        print()  # nova linha no final
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

## Streaming em app web — formato backend-para-frontend

Ao migrar um app web que transmite SSE/JSONL para o frontend, o **formato de serialização no backend** muda. Projete a saída do backend para preservar os padrões de acesso existentes no frontend para que não haja necessidade de mudanças no frontend.

**Antes** — O backend de Chat Completions geralmente serializava o dicionário `choices[0]` de cada chunk:
```python
# Antigo: dicionário completo de escolha serializado por bloco
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Leitura do frontend: `response.delta.content` (caminho profundo no objeto choice).

**Depois** — O backend da Responses API emite uma forma mínima preservando o mesmo caminho de acesso do frontend:
```python
# Novo: emitir apenas o que o frontend precisa
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
O frontend ainda lê `response.delta.content` — **nenhuma mudança no frontend necessária**.

> **Insight chave**: O formato de streaming da Responses API (`event.type` + `event.delta`) é fundamentalmente diferente do Chat Completions (`chunk.choices[0].delta.content`). Mas o contrato backend-para-frontend é definido por você. Modele a saída do backend para coincidir com o que o frontend já espera.

## Sequência de eventos de streaming

Quando `stream: true`, a API emite eventos nesta ordem:
1. `response.created` – objeto de resposta inicializado
2. `response.in_progress` – geração iniciada
3. `response.output_item.added` – item de saída criado
4. `response.content_part.added` – parte do conteúdo iniciada
5. `response.output_text.delta` – pedaços de texto (múltiplos, cada um com `delta: string`)
6. `response.output_text.done` – geração do texto finalizada
7. `response.content_part.done` – parte do conteúdo finalizada
8. `response.output_item.done` – item de saída finalizado
9. `response.completed` – resposta completa finalizada

Para streaming básico de texto, trate apenas `response.output_text.delta` (para os pedaços de texto) e `response.completed` (para o término).

## Tratamento de erros de streaming em apps web

Ao fazer streaming em um app web, envolva a iteração async em `try/except` e envie erros como JSON para que o frontend possa exibi-los de forma elegante (ex.: limites de taxa, falhas transitórias):

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

> **Por que isso é importante**: Azure OpenAI retorna `429 Too Many Requests` durante limitação de taxa. Sem o `try/except`, o streaming morre silenciosamente. Com ele, o frontend recebe `{"error": "Too Many Requests"}` e pode mostrar uma opção para tentar novamente.

## Tipos de eventos de streaming (SDK Python)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Formato de conversa
```python
# A API de Respostas suporta formato de conversa via array de entrada
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

## Tratamento de erro no filtro de conteúdo

A estrutura do corpo de erro mudou do Chat Completions para Responses API.

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
- O wrapper `innererror` **sumiu** — os detalhes do filtro de conteúdo agora estão no nível superior de `error.body`.
- `content_filter_result` (singular) → `content_filters` (array plural) contendo `content_filter_results` (plural) dentro de cada item.
- Cada item em `content_filters` inclui `blocked`, `source_type`, e `content_filter_results` com detalhes por categoria (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

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

## Migração HTTP bruta (requests/httpx)

Se o app fizer chamadas REST do Azure OpenAI diretamente em vez de usar o SDK:

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

> **Nota**: `output_text` é uma propriedade de conveniência no objeto `Response` do SDK Python. A resposta JSON REST bruta não tem campo `output_text` no topo — o texto está em `output[0].content[0].text`.

## Conversa multi-turno
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

Multi-turno com tipo de conteúdo (explícito `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Multi-turno via `previous_response_id` (alternativa)

Em vez de gerenciar o array de conversa você mesmo, você pode encadear respostas
no servidor usando `previous_response_id`. A API armazena cada resposta e
pré-pende automaticamente as rodadas anteriores.

```python
# Primeiro turno
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Turnos subsequentes — basta passar a nova mensagem do usuário + ID da resposta anterior
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Quando usar qual:**

| Abordagem | Vantagens | Desvantagens |
|---|---|---|
| Array `input` (manual) | Controle total do histórico; pode cortar/resumir; não precisa armazenar no servidor (`store=False`) | Mais código; você gerencia o array |
| `previous_response_id` | Código mais simples; encadeamento automático | Requer `store=True` (padrão); conversa armazenada no servidor; não pode alterar histórico entre turnos |

> **Nota de migração:** A maioria dos apps Chat Completions já gerenciam seu próprio array de mensagens, então converter para array `input` é uma migração 1:1 mais direta. Use `previous_response_id` para código novo ou quando não precisar manipular histórico de conversa.

## Modelos de raciocínio da série O (o1, o3-mini, o3, o4-mini)

Modelos da série O têm restrições únicas de parâmetros ao migrar para Responses API.

### Mapeamento de parâmetros para série O

| Chat Completions (série O) | Responses API | Notas |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Configure alto (4096+) — tokens de raciocínio contam contra o limite |
| `reasoning_effort` | `reasoning.effort` | Mantenha como está se presente (low/medium/high) |
| `temperature` | Remova ou defina como `1` | Série O só aceita `1` |
| `top_p` | Remova | Não suportado na série O |
| `seed` | Remova | Não suportado na Responses API |

### Série O antes/depois

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

> **Nota**: Modelos da série O podem reter saída durante o raciocínio antes de emitir deltas de texto. Streaming ainda funciona, mas o primeiro evento `response.output_text.delta` pode chegar após uma demora maior que com modelos GPT.

## Acessando tokens de raciocínio
```python
# Modelos de raciocínio usam raciocínio interno — você pode ver quantos tokens de raciocínio foram usados
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

> **Importante**: Use `max_output_tokens=1000` (não 50–200) para levar em conta o processo interno de raciocínio dos modelos. O modelo usa tokens de raciocínio internamente antes de gerar a saída final.

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

- Defina funções em `tools` com o **formato plano da Responses API** — `name`, `description` e `parameters` no nível superior (não aninhados em `function`).
- Quando o modelo pedir para chamar uma ferramenta, execute-a em seu app e inclua o resultado na próxima requisição como um item `function_call_output` dentro de `input`.
- Mantenha schemas mínimos; valide inputs antes da execução.
- Ao usar `strict: true`, todas as propriedades devem estar listadas em `required` e `additionalProperties: false` é obrigatório.

> **⚠️ `pydantic_function_tool()` é incompatível**: O helper `openai.pydantic_function_tool()` ainda gera o antigo formato aninhado do Chat Completions (`{"type": "function", "function": {"name": ...}}`). Não o use com `responses.create()`. Defina schemas de ferramentas manualmente ou crie um wrapper para achatar a saída.

### Formato de definição de ferramenta

A Responses API usa formato **plano** para ferramentas — `name`, `description`, `parameters` são chaves no nível superior (não aninhadas dentro de `function`).

**Antes (Chat Completions — aninhado):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Depois (Responses API — plano):**
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

Com `strict: true` (validação do schema):
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
            "additionalProperties": False,   # Obrigatório para modo estrito
        },
    }
]
```

### Ciclo de chamada da ferramenta (executar e retornar resultados)

Quando o modelo solicitar uma chamada de ferramenta, use os itens `response.output` + `function_call_output` — **não** o padrão Chat Completions `role: assistant` + `role: tool`.

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
    # Adicione os itens function_call do modelo à conversa
    messages.extend(response.output)

    # Execute cada ferramenta e adicione os resultados
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Obtenha a resposta final com os resultados das ferramentas
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Exemplos few-shot de chamadas de ferramentas

Ao fornecer exemplos few-shot de chamadas de ferramentas em `input`, use itens `function_call` e `function_call_output`. IDs devem começar com `fc_`.

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
# Exemplo embutido de busca na web
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Input de imagem

Itens de conteúdo de imagem mudam o tipo de `image_url` para `input_image`, e a URL muda de objeto aninhado para string plana.

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

> **Mudanças chave**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (objeto aninhado) → `"image_url": "..."` (string plana — ou URL HTTPS ou URI de dados `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Migração do Microsoft Agent Framework (MAF)

**Verifique sua versão do MAF primeiro** — a migração depende se você está no MAF 1.0.0+ ou em uma beta/rc pré-1.0.0.

Para verificar: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

No MAF 1.0.0+, `OpenAIChatClient` **já usa a Responses API** — nenhuma migração necessária.

Se o código usa o legado `OpenAIChatCompletionClient` (que usa `chat.completions.create`), substitua por `OpenAIChatClient`:

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

### MAF pré-1.0.0 (lançamentos beta/rc)

No MAF pré-1.0.0, `OpenAIChatClient` usava Chat Completions. Atualize para `agent-framework-openai>=1.0.0` onde `OpenAIChatClient` usa a Responses API por padrão.

> **Nota**: As APIs `Agent`, `MCPStreamableHTTPTool` e outras do MAF permanecem inalteradas — apenas a importação da classe client e sua instanciação mudam.

## Migração LangChain (`langchain-openai`)

Adicione `use_responses_api=True` em `ChatOpenAI()`. Também atualize o acesso ao conteúdo da mensagem de `.content` para `.text`.

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
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->