---
name: azure-openai-to-responses
license: MIT
---
# Migrar Apps Python de Azure OpenAI Chat Completions para Responses API

> **ORIENTAÇÃO AUTORITATIVA — SIGA EXATAMENTE**
>
> Esta funcionalidade migra bases de código Python a usar Azure OpenAI Chat Completions
> para a API unificada Responses. Siga estas instruções de forma precisa.
> Não improvise mapeamentos de parâmetros nem invente formatos de API.

---

## Gatilhos

Ative esta funcionalidade quando o utilizador quiser:
- Migrar uma app Python de Azure OpenAI Chat Completions para Responses API
- Atualizar utilização do SDK OpenAI em Python para o formato mais recente da API com Azure OpenAI
- Preparar código Python para modelos GPT-5 ou superiores que requerem Responses na Azure
- Trocar `AzureOpenAI`/`AsyncAzureOpenAI` pelo cliente padrão `OpenAI`/`AsyncOpenAI` com o endpoint v1
- Corrigir avisos de descontinuação relacionados com construtores `AzureOpenAI` ou `api_version`

---

## ⚠️ Compatibilidade de Modelo — VERIFIQUE PRIMEIRO

> **Antes de migrar, verifique se o seu deployment Azure OpenAI suporta a Responses API.**

### 1. Teste rápido do deployment (mais rápido)

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

> **Nota**: `max_output_tokens` tem um **mínimo de 16** na Azure OpenAI. Valores abaixo de 16 causam erro 400. Use 50+ para testes rápidos.

Se isto devolver 404, o modelo do deployment não suporta Responses ainda — verifique a referência abaixo ou redeploy com um modelo suportado.

### 2. Verifique modelos disponíveis na sua região (recomendado)

Execute a ferramenta incorporada de compatibilidade de modelos para ver o que está disponível com suporte Responses API na sua região:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Esta consulta ao vivo Azure ARM mostra uma matriz de compatibilidades — quais modelos suportam Responses, output estruturado, ferramentas, etc. Use `--filter gpt-5.1,gpt-5.2` para filtrar resultados ou `--json` para scripting.

### 3. Referência completa de suporte a modelos

- **Consulta ao vivo**: `python migrate.py models` (veja acima — específico de região, sempre atualizado)
- **Navegar disponibilidades**: [Tabela resumo de modelos e disponibilidade por região](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Arranque rápido & orientação**: **https://aka.ms/openai/start**

### ⚠️ Limitações de modelos antigos

> **AVISO**: Modelos mais antigos (anteriores a `gpt-4.1`) podem não suportar totalmente todas as funcionalidades da Responses API.
>
> Limitações conhecidas com modelos antigos:
> - **Parâmetro `reasoning`**: Não suportado em muitos modelos sem capacidade de raciocínio. Apenas migre `reasoning` se já existia no código original.
> - **Parâmetro `seed`**: Não suportado na Responses API — remova de todos os pedidos.
> - **Output estruturado via `text.format`**: Modelos antigos podem não impor esquemas JSON `strict: true` de forma fiável.
> - **Orquestração de ferramentas**: GPT-5+ orquestra chamadas a ferramentas como parte do raciocínio interno. Modelos antigos em Responses ainda funcionam mas sem esta integração profunda.
> - **Restrições de temperatura**: Ao migrar para `gpt-5`, a temperatura deve ser omitida ou definida para `1`. Modelos antigos não têm esta restrição.

### Modelos de raciocínio da série O (o1, o3-mini, o3, o4-mini)

Modelos da série O têm restrições específicas de parâmetros. Ao migrar apps para modelos da série O:

- **`temperature`**: Deve ser `1` (ou omitido). Modelos série O não aceitam outros valores.
- **`max_completion_tokens` → `max_output_tokens`**: Apps que usam `max_completion_tokens` específico Azure devem mudar para `max_output_tokens`. Use valores altos (4096+) pois tokens de raciocínio contam para o limite.
- **`reasoning_effort`**: Se usar `reasoning_effort` (baixo/médio/alto), mantenha — Responses API suporta este parâmetro para modelos da série O.
- **Comportamento streaming**: Modelos da série O podem armazenar output internamente até o raciocínio concluir antes de emitir eventos delta de texto. Streaming funciona, mas o primeiro `response.output_text.delta` pode demorar mais que em modelos GPT.
- **`top_p`**: Não suportado na série O — remova se presente.
- **Uso de ferramentas**: Modelos da série O suportam ferramentas via Responses API como GPT, mas a qualidade da orquestração varia por modelo.

**Ação — aviso proativo ao modelo**: Durante a fase de análise, verifique qual modelo a app usa (nomes de deployment, variáveis de ambiente, configuração). Se o modelo for anterior a `gpt-4.1` (não gpt-4.1+), informe proativamente o utilizador:
- A migração funcionará para texto básico, chat, streaming, e ferramentas no modelo atual.
- Modelos mais recentes (`gpt-5.1`, `gpt-5.2`) oferecem melhor orquestração de ferramentas, aplicação de output estruturado, raciocínio, e disponibilidade cross-region.
- Devem considerar atualizar o deployment quando prontos — não bloqueia a migração.

Não bloqueie nem recuse a migração por versão do modelo. O aviso é informativo.

### GitHub Models NÃO suporta a Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) não suporta a Responses API.**

Se a base de código tiver um caminho para GitHub Models (procure por `base_url` a apontar para `models.github.ai` ou `models.inference.ai.azure.com`), **remova-o completamente** na migração. A Responses API requer Azure OpenAI, OpenAI ou endpoint local compatível (ex.: Ollama com suporte a Responses).

Ação durante a análise:
- Identifique e marque todos os caminhos de código GitHub Models para remoção.

---

## Migração de Frameworks

Muitas apps usam frameworks de nível superior sobre OpenAI. Ao migrar estes, mudam as APIs do próprio framework — não só as chamadas OpenAI subjacentes.

### Microsoft Agent Framework (MAF)

**Verifique primeiro a sua versão MAF** — a migração depende se está na versão 1.0.0+ ou numa beta/rc pré-1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **já usa a Responses API** — não há migração necessária. Se o código usar o legado `OpenAIChatCompletionClient` (usando `chat.completions.create`), troque-o por `OpenAIChatClient`.

| Antes | Depois |
|--------|---------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Para verificar a versão: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pré-1.0.0 (beta/rc)

No MAF pré-1.0.0, `OpenAIChatClient` usava Chat Completions. Atualize para `agent-framework-openai>=1.0.0` onde `OpenAIChatClient` usa a Responses API por padrão.

Não são necessárias outras mudanças — as APIs do `Agent` e das ferramentas mantêm-se.

### LangChain (`langchain-openai`)

Adicione `use_responses_api=True` ao `ChatOpenAI()`. Também atualize o acesso à resposta de `.content` para `.text`.

| Antes | Depois |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Para exemplos completos de código antes/depois, veja [cheat-sheet.md](./references/cheat-sheet.md).

---

## Orientações para Migração Frontend

> **A Responses API é uma preocupação do servidor.** Migre o backend Python; o contrato HTTP no frontend deve manter-se inalterado, a menos que o backend seja um simples passthrough — nesse caso, considere adotar o formato de pedido Responses para eliminar uma camada de tradução. Se o frontend chama OpenAI diretamente com chave no cliente, mova essas chamadas para o backend primeiro.

### Descontinuação do `@microsoft/ai-chat-protocol`

O pacote npm `@microsoft/ai-chat-protocol` está descontinuado e deve ser substituído por [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Se o encontrar num frontend:

1. Substitua a tag script CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Remova a criação de `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Substitua `client.getStreamedCompletion(messages)` por uma chamada `fetch()` direta ao endpoint backend de streaming.
4. Substitua `for await (const response of result)` por `for await (const chunk of readNDJSONStream(response.body))`.
5. Atualize acessos a propriedades: de `response.delta.content` / `response.error` para `chunk.delta.content` / `chunk.error`.

---

## Objetivos

- Enumerar todos os locais de chamadas Python usando Chat Completions ou Completions legados contra Azure OpenAI.
- Propor um plano de migração e sequência para a base de código Python.
- Aplicar edições seguras e mínimas para mudar para Responses API.
- Atualizar os callers para consumirem o esquema de output Responses; sem wrappers de retrocompatibilidade.
- Executar testes/lints; corrigir rupturas triviais introduzidas pela migração.
- Preparar conjuntos de mudanças pequenos e revisáveis e providenciar um sumário final com diffs (não commitar).

---

## Regras

- Modificar apenas ficheiros dentro da workspace git. Nunca escrever fora.
- Não preservar shims de retrocompatibilidade; migre para o novo formato de API.
- Não deixar comentários de transição ou ficheiros de backup.
- Preservar semântica streaming se usada anteriormente; senão usar sem streaming.
- Pedir aprovação antes de executar comandos ou chamadas de rede se em modo aprovação.
- Não executar `git add`/`git commit`/`git push`; apenas edite working-tree.

---

## Passo 0: Migração do Cliente Azure OpenAI (Pré-requisito)

Se a base de código usar os construtores `AzureOpenAI` ou `AsyncAzureOpenAI`, migre para os construtores padrão `OpenAI` / `AsyncOpenAI` primeiro. Os construtores específicos Azure estão descontinuados em `openai>=1.108.1`.

### Porquê o endpoint API v1?

O novo endpoint `/openai/v1` usa o cliente padrão `OpenAI()` em vez de `AzureOpenAI()`, não requer parâmetro `api_version`, e funciona igual em OpenAI e Azure OpenAI. O mesmo código cliente é à prova de futuro — sem necessidade de gerir versões.

### Principais mudanças

| Antes | Depois |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Remover completamente |

### Lista de limpeza

- Remover argumento `api_version` da construção do cliente.
- Remover variáveis ambiente `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` de `.env`, definições da app, e ficheiros Bicep/infra.
- Renomear `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` em `.env`, definições da app, Bicep/infra, e fixtures de teste (convenção SDK Azure Identity padrão).
- Garantir `openai>=1.108.1` no `requirements.txt` ou `pyproject.toml`.

### Migração de variáveis de ambiente

| Variável antiga | Ação | Notas |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Remover** | Não é necessário `api_version` com endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **Remover** | Igual acima |
| `AZURE_OPENAI_CLIENT_ID` | **Renomear** → `AZURE_CLIENT_ID` | Convenção padrão SDK Azure Identity para `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Manter** | Ainda necessário para construir `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Manter** | Usado como `model` no `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Manter** | Usado como `api_key` para autenticação por chave |

Para exemplos de configuração cliente (sync, async, EntraID, chave API, multi-tenant), veja [cheat-sheet.md](./references/cheat-sheet.md).

---

## Passo 1: Detectar Locais de Chamadas Legadas

Execute o script [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) para localizar todos os locais de chamadas que precisam de migração:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Ou execute estas pesquisas manualmente — cada correspondência é alvo de migração:

```bash
# Chamadas API legadas (deve reescrever)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Construtores do cliente Azure obsoletos (deve substituir)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Padrões de acesso à estrutura de resposta (deve atualizar)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definições de ferramentas em formato antigo aninhado (deve achatar)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Resultados da ferramenta em formato antigo (deve converter para function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Parâmetros obsoletos (deve remover ou renomear)
rg "response_format"
rg "max_tokens\b"        # renomear para max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Variáveis de ambiente obsoletas (limpar)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # deveria ser AZURE_CLIENT_ID

# Endpoints dos Modelos GitHub (deve remover — API de Respostas não suportada)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Padrões legados ao nível do framework (deve atualizar)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: substituir por OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: necessita de use_responses_api=True

# Infraestrutura de testes (deve atualizar)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Acesso ao corpo de erro do filtro de conteúdo (deve atualizar — estrutura alterada)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # Forma singular antiga — agora content_filter_results (plural) dentro do array content_filters

# Chamadas HTTP brutas ao endpoint Chat Completions (deve atualizar URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heurísticas (detetar e reescrever)

- **Cliente Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Construtores de cliente Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Ferramentas**: converta definições de ferramentas para chamada de função do formato aninhado (`{"type": "function", "function": {"name": ...}}`) para o formato plano Responses (`{"type": "function", "name": ...}`); utilize `tool_choice`; retorne resultados de ferramentas como itens `{"type": "function_call_output", "call_id": ..., "output": ...}` (não `{"role": "tool", ...}`).
- **Ciclos de ferramentas**: quando o modelo retornar chamadas de função, anexe os itens `response.output` à conversa (não um dicionário manual `{"role": "assistant", "tool_calls": [...]}`), depois anexe itens `function_call_output` para cada resultado.
- **Exemplos de ferramentas few-shot**: se a conversa incluir exemplos fixos de chamadas de ferramentas, converta-os em itens `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. IDs devem começar com `fc_`.
- **`pydantic_function_tool()`**: este auxiliar ainda gera o formato aninhado antigo e **não é compatível** com `responses.create()`. Substitua por definições manuais de ferramentas ou um wrapper de achatamento.
- **Multi-turn**: mantenha o histórico da conversa na aplicação; passe os turnos anteriores via itens `input`.
- **Formatos**: substitua `response_format` de nível superior do Chat por `text.format` nas Responses. Forma canónica: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Itens de conteúdo**: substitua Chat `content[].type: "text"` por Responses `content[].type: "input_text"` para os turnos do utilizador/sistema.
- **Itens de conteúdo de imagem**: substitua Chat `content[].type: "image_url"` por Responses `content[].type: "input_image"`. O campo `image_url` muda de um objeto aninhado `{"url": "..."}` para uma string simples. Veja o cheat sheet para exemplos antes/depois.
- **Esforço de raciocínio**: **migre apenas `reasoning` se já existir no código original**.
- **Tratamento de erros do filtro de conteúdo**: a estrutura do corpo do erro mudou. Chat Completions usava `error.body["innererror"]["content_filter_result"]` (singular); Responses API usa `error.body["content_filters"][0]["content_filter_results"]` (plural, dentro de um array). Código que acede a `innererror` lançará um `KeyError`. Reescreva para usar o novo caminho.
- **Chamadas HTTP brutas**: se a aplicação usar diretamente a REST API Azure OpenAI (via `requests`, `httpx`, etc.) com `/openai/deployments/{name}/chat/completions?api-version=...`, reescreva para `/openai/v1/responses`. O corpo do pedido muda: `messages` → `input`, adicionar `max_output_tokens` e `store: false`, remover o parâmetro de consulta `api-version`. O corpo da resposta muda: `choices[0].message.content` → `output[0].content[0].text` (nota: `output_text` é uma propriedade de conveniência do SDK não presente no JSON REST bruto).

---

## Passo 2: Aplicar Migração

### Notas de Migração (Chat Completions → Responses)

- **Porquê migrar**: Responses é a API unificada para texto, ferramentas e streaming; Chat Completions é legado. Com o GPT-5, Responses é obrigatório para melhor desempenho.
- **HTTP**: o endpoint Azure muda de `/openai/deployments/{name}/chat/completions` para `/openai/v1/responses`.
- **Campos**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` mantém-se.
- **Formatos**: `response_format` → `text.format` com um objeto apropriado.
- **Itens de conteúdo**: substitua Chat `content[].type: "text"` por Responses `content[].type: "input_text"` para os turnos do sistema/utilizador.
- **Itens de conteúdo de imagem**: substitua Chat `content[].type: "image_url"` por Responses `content[].type: "input_image"`. Achate o campo `image_url` de `{"image_url": {"url": "..."}}` para `{"image_url": "..."}` (uma string simples – pode ser um URL HTTPS ou um URI de dados `data:image/...;base64,...`).

### Referência de mapeamento de parâmetros

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array de itens) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objeto) |
| `temperature` | `temperature` (inalterado) |
| `stop` | `stop` (inalterado) |
| `frequency_penalty` | `frequency_penalty` (inalterado) |
| `presence_penalty` | `presence_penalty` (inalterado) |
| `tools` / chamada de função | `tools` (inalterado) |
| `seed` | **Remover** (não suportado) |
| `store` | `store` (definido para `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (string simples) |

Para exemplos completos de código antes/depois, veja [cheat-sheet.md](./references/cheat-sheet.md).

Para migração de infraestruturas de teste (mocks, snapshots, assertions), veja [test-migration.md](./references/test-migration.md).

Para resolução de problemas e armadilhas, veja [troubleshooting.md](./references/troubleshooting.md).

---

## Retenção de Dados e Estado

- Defina `store: false` em todos os pedidos Responses.
- Não confie em IDs de mensagens anteriores ou contexto armazenado no servidor; mantenha estado gerido pelo cliente e minimize metadados.

---

## Critérios de Aceitação

### Portões a nível de código (todos devem passar)

- [ ] Nenhuma correspondência para `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` nos ficheiros migrados.
- [ ] Nenhuma correspondência para `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — todos os construtores usam `OpenAI`/`AsyncOpenAI` com o endpoint v1.
- [ ] Nenhuma correspondência para `rg "models\.github\.ai|models\.inference\.ai\.azure"` — caminhos de código de GitHub Models removidos.
- [ ] Nenhuma correspondência para `rg "OpenAIChatCompletionClient"` — código MAF 1.0.0+ usa `OpenAIChatClient` (que usa Responses API). Em versões anteriores a 1.0.0, atualize para `agent-framework-openai>=1.0.0`.
- [ ] Todas as chamadas `ChatOpenAI(...)` incluem `use_responses_api=True`.
- [ ] Nenhuma correspondência para `rg "choices\[0\]"` — todo o acesso a respostas usa `resp.output_text` ou o esquema de saída Responses.
- [ ] Sem `response_format` ao nível superior; toda saída estruturada usa `text={"format": {...}}`.
- [ ] `openai>=1.108.1` e `azure-identity` em `requirements.txt` ou `pyproject.toml`; dependências reinstaladas.
- [ ] `store=False` definido em cada chamada `responses.create`.
- [ ] Sem `api_version` na construção do cliente; `AZURE_OPENAI_API_VERSION` removido de ficheiros env e infra.

### Portões da infraestrutura de teste (todos devem passar)

- [ ] Nenhuma correspondência para `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Nenhuma correspondência para `rg "_azure_ad_token_provider" tests/` — as asserts foram atualizadas para verificar `isinstance(client, AsyncOpenAI)` ou `base_url`.
- [ ] Nenhuma correspondência para `rg "prompt_filter_results|content_filter_results" tests/` — mocks de filtros específicos Azure removidos.
- [ ] Fixtures de mocks usam `kwargs.get("input")` e não `kwargs.get("messages")`.
- [ ] Ficheiros snapshot / golden atualizados para a forma de streaming Responses (sem `choices[0]`, `function_call`, `logprobs`, etc.).
- [ ] `pytest` passa sem falhas após todas as atualizações de teste.

### Portões comportamentais (verificação manual ou via harness de teste)

- [ ] **Completação básica**: `responses.create` não-streaming retorna `output_text` não vazio.
- [ ] **Paridade no streaming**: se o código original usava streaming, o código migrado transmite streaming e produz eventos `response.output_text.delta` com deltas não vazios.
- [ ] **Saída estruturada**: se usar `text.format` com `json_schema`, `json.loads(resp.output_text)` faz parse com sucesso e corresponde ao esquema.
- [ ] **Loop de chamada de ferramentas**: se for usadas ferramentas, o modelo emite chamadas a ferramentas, a aplicação executa e o pedido de seguimento retorna um `output_text` final (sem ciclo infinito).
- [ ] **Paridade assíncrona**: se foi usado `AsyncAzureOpenAI`, o equivalente `AsyncOpenAI` funciona com `await`.
- [ ] **Taxa de erro**: sem novos erros 400/401/404 comparados à linha base pré-migração.

### Entregáveis

- O sumário inclui ficheiros editados, contagens antes/depois dos locais de chamada legado, e próximos passos.
- As alterações são apenas edições da árvore de trabalho (sem commits).

---

## Requisitos de Versão do SDK

| Pacote | Versão Mínima |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Mais recente (para autenticação EntraID) |

---

## Referências

- [Cheat Sheet — todos os excertos de código](./references/cheat-sheet.md)
- [Test Migration — mocks, snapshots, assertions](./references/test-migration.md)
- [Troubleshooting — erros, tabela de riscos, armadilhas](./references/troubleshooting.md)
- [detect_legacy.py — scanner automatizado](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Documentação da API Azure OpenAI Responses](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Ciclo de vida das versões da API Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Referência da API OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->