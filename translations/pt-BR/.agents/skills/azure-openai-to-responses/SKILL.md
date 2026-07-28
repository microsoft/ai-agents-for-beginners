---
name: azure-openai-to-responses
license: MIT
---
# Migrar Aplicativos Python de Azure OpenAI Chat Completions para Responses API

> **ORIENTAÇÃO AUTORITATIVA — SIGA EXATAMENTE**
>
> Esta habilidade migra bases de código Python que usam Azure OpenAI Chat Completions
> para a Responses API unificada. Siga estas instruções com precisão.
> Não improvise mapeamentos de parâmetros nem invente formatos de API.

---

## Gatilhos

Ative esta habilidade quando o usuário quiser:
- Migrar um app Python de Azure OpenAI Chat Completions para Responses API
- Atualizar o uso do SDK Python OpenAI para o formato mais recente da API contra Azure OpenAI
- Preparar código Python para modelos GPT-5 ou mais recentes que requerem Responses na Azure
- Mudar de `AzureOpenAI`/`AsyncAzureOpenAI` para o cliente padrão `OpenAI`/`AsyncOpenAI` com o endpoint v1
- Corrigir avisos de depreciação relacionados a construtores `AzureOpenAI` ou `api_version`

---

## ⚠️ Compatibilidade de Modelo — VERIFIQUE PRIMEIRO

> **Antes de migrar, verifique se sua implantação Azure OpenAI suporta a Responses API.**

### 1. Teste simples da implantação (mais rápido)

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

> **Nota**: `max_output_tokens` tem um **mínimo de 16** na Azure OpenAI. Valores abaixo de 16 retornam erro 400. Use 50+ para testes simples.

Se isto retornar 404, o modelo da implantação ainda não suporta Responses — consulte a referência abaixo ou reimplemente com um modelo suportado.

### 2. Verifique os modelos disponíveis na sua região (recomendado)

Execute a ferramenta embutida de compatibilidade de modelos para ver o que está disponível com suporte à Responses API em sua região específica:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Esta consulta à Azure ARM ao vivo mostra uma matriz de compatibilidade — quais modelos suportam Responses, saída estruturada, ferramentas, etc. Use `--filter gpt-5.1,gpt-5.2` para filtrar resultados ou `--json` para script.

### 3. Referência completa de suporte a modelos

- **Consulta ao vivo**: `python migrate.py models` (veja acima — específico por região, sempre atualizado)
- **Navegue disponibilidade**: [Tabela resumo de modelos e disponibilidade regional](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Início rápido e orientações**: **https://aka.ms/openai/start**

### ⚠️ Limitações de modelos antigos

> **AVISO**: Modelos antigos (anteriores a `gpt-4.1`) podem não suportar totalmente todos os recursos da Responses API.
>
> Limitações conhecidas com modelos antigos:
> - **Parâmetro `reasoning`**: Não suportado em muitos modelos sem raciocínio. Migrar `reasoning` só se já estiver presente no código original.
> - **Parâmetro `seed`**: Não suportado na Responses API — remova de todas as requisições.
> - **Saída estruturada via `text.format`**: Modelos antigos podem não aplicar esquemas JSON `strict: true` de forma confiável.
> - **Orquestração de ferramentas**: GPT-5+ orquestra chamadas de ferramentas como parte do raciocínio interno. Modelos antigos no Responses funcionam, mas sem essa integração profunda.
> - **Restrições de temperatura**: Ao migrar para `gpt-5`, a temperatura deve ser omitida ou definida como `1`. Modelos antigos não têm essa restrição.

### Modelos de raciocínio da série O (o1, o3-mini, o3, o4-mini)

Modelos da série O têm restrições exclusivas de parâmetros. Ao migrar apps que usam modelos da série O:

- **`temperature`**: Deve ser `1` (ou omitido). Modelos da série O não aceitam outros valores.
- **`max_completion_tokens` → `max_output_tokens`**: Apps usando o específico `max_completion_tokens` do Azure devem mudar para `max_output_tokens`. Defina valores altos (4096+) pois tokens de raciocínio contam no limite.
- **`reasoning_effort`**: Se o app usa `reasoning_effort` (baixo/médio/alto), mantenha — a Responses API suporta esse parâmetro para modelos da série O.
- **Comportamento de streaming**: Modelos da série O podem armazenar saída até o raciocínio finalizar antes de emitir eventos de delta de texto. Streaming ainda funciona, mas o primeiro `response.output_text.delta` pode chegar com delay maior que em modelos GPT.
- **`top_p`**: Não suportado na série O — remova se presente.
- **Uso de ferramentas**: Modelos da série O suportam ferramentas pela Responses API igual aos modelos GPT, mas a qualidade da orquestração varia com o modelo.

**Ação — aviso proativo de modelo**: Durante a fase de análise, verifique qual modelo o app usa (nomes de implantação, variáveis de ambiente, config). Se o modelo for anterior a `gpt-4.1` (não gpt-4.1+), informe proativamente ao usuário:
- A migração funcionará para texto básico, chat, streaming e ferramentas no modelo atual.
- Modelos mais novos (`gpt-5.1`, `gpt-5.2`) oferecem melhor orquestração de ferramentas, aplicação de saída estruturada, raciocínio e disponibilidade cross-region.
- Ele deve considerar atualizar a implantação quando quiser — não bloqueia a migração.

Não bloqueie nem recuse a migração por versão do modelo. O aviso é informativo.

### GitHub Models NÃO suporta a Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) não suporta a Responses API.**

Se a base de código tiver um caminho de código GitHub Models (procure `base_url` apontando para `models.github.ai` ou `models.inference.ai.azure.com`), **remova completamente** durante a migração. A Responses API requer Azure OpenAI, OpenAI, ou endpoint local compatível (ex: Ollama com suporte a Responses).

Ação durante a análise:
- Identifique qualquer caminho de código GitHub Models para remoção.

---

## Migração de Framework

Muitos apps usam frameworks de nível superior sobre OpenAI. Ao migrar, alteram-se também as APIs do framework — não apenas as chamadas subjacentes OpenAI.

### Microsoft Agent Framework (MAF)

**Verifique sua versão do MAF primeiro** — a migração depende se você está no MAF 1.0.0+ ou numa beta/rc pré-1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **já usa Responses API** — não precisa migrar. Se o código usa o legado `OpenAIChatCompletionClient` (que usa `chat.completions.create`), substitua por `OpenAIChatClient`.

| Antes | Depois |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Para checar sua versão: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pré-1.0.0 (lançamentos beta/rc)

No MAF pré-1.0.0, `OpenAIChatClient` usava Chat Completions. Atualize para `agent-framework-openai>=1.0.0` onde `OpenAIChatClient` usa Responses API por padrão.

Nenhuma outra mudança necessária — as APIs `Agent` e de ferramentas permanecem iguais.

### LangChain (`langchain-openai`)

Adicione `use_responses_api=True` a `ChatOpenAI()`. Também atualize o acesso à resposta de `.content` para `.text`.

| Antes | Depois |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Para exemplos completos de código antes/depois, veja [cheat-sheet.md](./references/cheat-sheet.md).

---

## Orientação para Migração do Frontend

> **A Responses API é uma preocupação do lado servidor.** Migre seu backend Python; o contrato HTTP do frontend deve permanecer inalterado, a menos que seu backend seja uma passagem fina — nesse caso, considere adotar o formato Requests Responses para eliminar uma camada de tradução. Se o frontend chama OpenAI diretamente com chave no cliente, mova essas chamadas para o backend primeiro.

### Depreciação do `@microsoft/ai-chat-protocol`

O pacote npm `@microsoft/ai-chat-protocol` está depreciado e deve ser substituído por [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Se encontrá-lo em um frontend:

1. Substitua a tag script CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Remova a instanciação `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Substitua `client.getStreamedCompletion(messages)` por uma chamada `fetch()` direta ao endpoint de streaming do backend.
4. Substitua `for await (const response of result)` por `for await (const chunk of readNDJSONStream(response.body))`.
5. Atualize o acesso a propriedades de `response.delta.content` / `response.error` para `chunk.delta.content` / `chunk.error`.

---

## Objetivos

- Enumerar todos os pontos de chamadas Python que usam Chat Completions ou Completions legadas contra Azure OpenAI.
- Propor um plano de migração e sequenciamento para a base de código Python.
- Aplicar edições seguras e mínimas para mudar à Responses API.
- Atualizar chamadores para consumir o esquema de saída do Responses; sem wrappers de retrocompatibilidade.
- Rodar testes/lints; corrigir quebras triviais causadas pela migração.
- Preparar pequenos conjuntos de mudanças revisáveis e fornecer um resumo final com diffs (não commite).

---

## Limites de Segurança

- Modifique apenas arquivos dentro da workspace git. Nunca escreva fora.
- Não preserve shims de retrocompatibilidade; migre código para o novo formato da API.
- Não deixe comentários de transição/tombstone ou arquivos de backup.
- Preserve semântica de streaming se usada antes; senão use não streaming.
- Peça aprovação antes de executar comandos ou chamadas de rede se estiver em modo de aprovação.
- Não execute `git add`/`git commit`/`git push`; produza apenas edições na working tree.

---

## Passo 0: Migração do Cliente Azure OpenAI (Pré-requisito)

Se a base de código usar construtores `AzureOpenAI` ou `AsyncAzureOpenAI`, migre primeiro para os construtores padrão `OpenAI` / `AsyncOpenAI`. Os construtores específicos Azure estão depreciados em `openai>=1.108.1`.

### Por que o caminho v1 da API?

O novo endpoint `/openai/v1` usa o cliente padrão `OpenAI()` em vez de `AzureOpenAI()`, não requer parâmetro `api_version`, e funciona exatamente igual em OpenAI e Azure OpenAI. O mesmo código cliente é à prova de futuro — não precisa gerenciar versões.

### Mudanças principais

| Antes | Depois |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Remova completamente |

### Checklist de limpeza

- Remova argumento `api_version` da construção do cliente.
- Remova variáveis de ambiente `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` de `.env`, configurações do app e arquivos Bicep/infra.
- Renomeie `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` em `.env`, configurações do app, Bicep/infra, e fixtures de teste (convenção padrão SDK Azure Identity).
- Garanta `openai>=1.108.1` em `requirements.txt` ou `pyproject.toml`.

### Migração de variáveis de ambiente

| Variável antiga | Ação | Notas |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Remover** | Não precisa de `api_version` com endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **Remover** | Igual acima |
| `AZURE_OPENAI_CLIENT_ID` | **Renomear** → `AZURE_CLIENT_ID` | Convenção padrão SDK Azure Identity para `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Manter** | Ainda necessário para construção de `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Manter** | Usado como parâmetro `model` em `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Manter** | Usado como `api_key` para autenticação por chave |

Para exemplos de configuração de cliente (sync, async, EntraID, chave API, multi-tenant), veja [cheat-sheet.md](./references/cheat-sheet.md).

---

## Passo 1: Detectar Pontos de Chamadas Legadas

Execute o script [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) para encontrar todos os pontos de chamada que precisam migrar:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Ou faça buscas manuais — cada correspondência é um alvo de migração:

```bash
# Chamadas de API legadas (precisa reescrever)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Construtores de cliente Azure obsoletos (precisa substituir)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Padrões de acesso à forma da resposta (precisa atualizar)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definições de ferramentas em formato antigo aninhado (precisa achatar)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Resultados da ferramenta em formato antigo (precisa converter para function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Parâmetros obsoletos (precisa remover ou renomear)
rg "response_format"
rg "max_tokens\b"        # renomear para max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Variáveis de ambiente obsoletas (limpar)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # deveria ser AZURE_CLIENT_ID

# Endpoints de Modelos do GitHub (precisa remover — API de Respostas não suportada)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Padrões legados no nível do framework (precisa atualizar)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: substituir por OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: precisa de use_responses_api=True

# Infraestrutura de teste (precisa atualizar)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Acesso ao corpo de erro do filtro de conteúdo (precisa atualizar — estrutura mudou)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # forma singular antiga — agora content_filter_results (plural) dentro do array content_filters

# Chamadas HTTP brutas para o endpoint de Chat Completions (precisa atualizar URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heurísticas (detectar e reescrever)

- **Cliente Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Construtores de cliente Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Ferramentas**: converta definições de ferramentas com chamada de função do formato aninhado (`{"type": "function", "function": {"name": ...}}`) para o formato plano do Responses (`{"type": "function", "name": ...}`); use `tool_choice`; retorne resultados das ferramentas como itens `{"type": "function_call_output", "call_id": ..., "output": ...}` (não `{"role": "tool", ...}`).
- **Ciclo das ferramentas**: quando o modelo retornar chamadas de funções, anexe os itens `response.output` à conversa (não um dicionário manual `{"role": "assistant", "tool_calls": [...]}`), depois anexe os itens `function_call_output` para cada resultado.
- **Exemplos de ferramentas few-shot**: se a conversa incluir exemplos embutidos de chamadas de ferramentas, converta-os em itens `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. IDs devem começar com `fc_`.
- **`pydantic_function_tool()`**: esse auxiliar ainda gera o formato aninhado antigo e **não é compatível** com `responses.create()`. Substitua por definições manuais de ferramentas ou um wrapper de achatamento.
- **Multi-turn**: mantenha o histórico da conversa na aplicação; passe turnos anteriores via itens `input`.
- **Formatação**: substitua o `response_format` do nível superior do Chat por `text.format` no Responses. Forma canônica: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Itens de conteúdo**: substitua Chat `content[].type: "text"` por Responses `content[].type: "input_text"` para turnos de usuário/sistema.
- **Itens de conteúdo de imagem**: substitua Chat `content[].type: "image_url"` por Responses `content[].type: "input_image"`. O campo `image_url` muda de um objeto aninhado `{"url": "..."}` para uma string simples. Veja a folha de dicas para exemplos antes/depois.
- **Esforço de raciocínio**: **migre `reasoning` somente se ele já existir no código original**.
- **Tratamento de erro do filtro de conteúdo**: a estrutura do corpo do erro mudou. Chat Completions usava `error.body["innererror"]["content_filter_result"]` (singular); a API Responses usa `error.body["content_filters"][0]["content_filter_results"]` (plural, dentro de um array). Código que acessa `innererror` levantará `KeyError`. Reescreva para usar o novo caminho.
- **Chamadas HTTP brutas**: se o app chama a API REST Azure OpenAI diretamente (via `requests`, `httpx`, etc.) usando `/openai/deployments/{name}/chat/completions?api-version=...`, reescreva para `/openai/v1/responses`. O corpo da requisição muda: `messages` → `input`, adicione `max_output_tokens` e `store: false`, remova o parâmetro de query `api-version`. O corpo da resposta muda: `choices[0].message.content` → `output[0].content[0].text` (nota: `output_text` é uma propriedade de conveniência do SDK não presente no JSON REST cru).

---

## Etapa 2: Aplicar Migração

### Notas de migração (Chat Completions → Responses)

- **Por que migrar**: Responses é a API unificada para texto, ferramentas e streaming; Chat Completions é legado. Com GPT-5, Responses é obrigatório para melhor desempenho.
- **HTTP**: o endpoint Azure muda de `/openai/deployments/{name}/chat/completions` para `/openai/v1/responses`.
- **Campos**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` permanece.
- **Formatação**: `response_format` → `text.format` com objeto adequado.
- **Itens de conteúdo**: substitua Chat `content[].type: "text"` por Responses `content[].type: "input_text"` para turnos de sistema/usuário.
- **Itens de conteúdo de imagem**: substitua Chat `content[].type: "image_url"` por Responses `content[].type: "input_image"`. Achate o campo `image_url` de `{"image_url": {"url": "..."}}` para `{"image_url": "..."}` (uma string simples — URL HTTPS ou URI de dados `data:image/...;base64,...`).

### Referência de mapeamento de parâmetros

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array de itens) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objeto) |
| `temperature` | `temperature` (sem mudanças) |
| `stop` | `stop` (sem mudanças) |
| `frequency_penalty` | `frequency_penalty` (sem mudanças) |
| `presence_penalty` | `presence_penalty` (sem mudanças) |
| `tools` / chamada de função | `tools` (sem mudanças) |
| `seed` | **Remover** (não suportado) |
| `store` | `store` (definido como `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (string simples) |

Para exemplos completos antes/depois de código, veja [cheat-sheet.md](./references/cheat-sheet.md).

Para migração de infraestrutura de teste (mocks, snapshots, assertions), veja [test-migration.md](./references/test-migration.md).

Para solução de problemas e armadilhas, veja [troubleshooting.md](./references/troubleshooting.md).

---

## Retenção de Dados & Estado

- Defina `store: false` em todas as requisições Responses.
- Não confie em IDs de mensagens anteriores ou contexto armazenado no servidor; mantenha o estado gerenciado pelo cliente e minimize metadados.

---

## Critérios de Aceitação

### Barreiras de nível de código (todas devem passar)

- [ ] Zero correspondências para `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` nos arquivos migrados.
- [ ] Zero correspondências para `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — todos os construtores usam `OpenAI`/`AsyncOpenAI` com o endpoint v1.
- [ ] Zero correspondências para `rg "models\.github\.ai|models\.inference\.ai\.azure"` — caminhos de código dos modelos do GitHub removidos.
- [ ] Zero correspondências para `rg "OpenAIChatCompletionClient"` — código MAF 1.0.0+ usa `OpenAIChatClient` (que usa Responses API). Em versões pré-1.0.0, atualize para `agent-framework-openai>=1.0.0`.
- [ ] Todas chamadas `ChatOpenAI(...)` incluem `use_responses_api=True`.
- [ ] Zero correspondências para `rg "choices\[0\]"` — todo acesso a respostas usa `resp.output_text` ou o esquema de saída Responses.
- [ ] Nenhum `response_format` no nível superior; toda saída estruturada usa `text={"format": {...}}`.
- [ ] `openai>=1.108.1` e `azure-identity` em `requirements.txt` ou `pyproject.toml`; dependências reinstaladas.
- [ ] `store=False` definido em toda chamada `responses.create`.
- [ ] Nenhum `api_version` na construção do cliente; `AZURE_OPENAI_API_VERSION` removido de arquivos e infraestrutura de ambiente.

### Barreiras da infraestrutura de teste (todas devem passar)

- [ ] Zero correspondências para `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Zero correspondências para `rg "_azure_ad_token_provider" tests/` — asserções atualizadas para verificar `isinstance(client, AsyncOpenAI)` ou `base_url`.
- [ ] Zero correspondências para `rg "prompt_filter_results|content_filter_results" tests/` — mocks do filtro específicos do Azure removidos.
- [ ] Mocks usam `kwargs.get("input")` e não `kwargs.get("messages")`.
- [ ] Arquivos snapshot / golden atualizados para a forma de streaming Responses (sem `choices[0]`, `function_call`, `logprobs`, etc.).
- [ ] `pytest` passa sem falhas após todas as atualizações de testes.

### Barreiras comportamentais (verificar manualmente ou via suíte de testes)

- [ ] **Completion básica**: `responses.create` não-streaming retorna `output_text` não vazio.
- [ ] **Paridade de streaming**: se o código original usava streaming, o código migrado também faz streaming e emite eventos `response.output_text.delta` com deltas não vazios.
- [ ] **Saída estruturada**: se usa `text.format` com `json_schema`, `json.loads(resp.output_text)` funciona e corresponde ao esquema.
- [ ] **Loop de chamada de ferramentas**: se ferramentas são usadas, o modelo emite chamadas, o app executa, e a requisição subsequente retorna um `output_text` final (sem loop infinito).
- [ ] **Paridade assíncrona**: se usava `AsyncAzureOpenAI`, o equivalente `AsyncOpenAI` funciona com `await`.
- [ ] **Taxa de erro**: não há novos erros 400/401/404 comparados ao baseline pré-migração.

### Entregáveis

- O resumo inclui arquivos editados, contagens antes/depois dos pontos de chamadas legadas e próximos passos.
- As mudanças são edições na árvore de trabalho apenas (sem commits).

---

## Requisitos de Versão do SDK

| Pacote | Versão Mínima |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Última (para autenticação EntraID) |

---

## Referências

- [Folha de Dicas — todos os trechos de código](./references/cheat-sheet.md)
- [Migração de Testes — mocks, snapshots, assertions](./references/test-migration.md)
- [Resolução de Problemas — erros, tabela de riscos, armadilhas](./references/troubleshooting.md)
- [detect_legacy.py — scanner automatizado](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Kit Inicial Azure OpenAI](https://aka.ms/openai/start)
- [Documentação Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Ciclo de vida da versão da API Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Referência da API OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->