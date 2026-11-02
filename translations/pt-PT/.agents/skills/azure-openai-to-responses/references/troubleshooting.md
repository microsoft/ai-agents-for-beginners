# Resolução de Problemas, Tabela de Riscos & Armadilhas

## Resolução de Problemas 400s

| Erro | Correção |
|-------|-----|
| `missing_required_parameter: tools[0].name` | A definição da ferramenta usa o formato aninhado antigo do Chat Completions | Achatar de `{"type": "function", "function": {"name": ...}}` para `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters vão ao nível superior |
| `unknown_parameter: input[N].tool_calls` | Resultados de múltiplas interações com ferramentas usam o formato antigo do Chat Completions | Substituir `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` por itens `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Ferramenta com `strict: true` sem array `required` | Quando `strict: true`, todas as propriedades devem estar listadas em `required` e `additionalProperties: false` deve ser definido |
| `invalid_function_parameters: 'additionalProperties' is required` | Ferramenta com `strict: true` sem `additionalProperties: false` | Acrescentar `"additionalProperties": false` ao objeto dos parâmetros |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | O ID do function_call do Few-shot tem prefixo errado | Os IDs dos chamados de função devem começar com `fc_` (ex.: `fc_example1`), e não com `call_` |
| `missing_required_parameter: text.format.name` | Acrescentar a chave `"name"` ao dicionário format (ex.: `"name": "Output"`) |
| `invalid_type: text.format` | Garantir que `text.format` é um dicionário com as chaves `type`, `name`, `strict`, `schema` — não uma string |
| `invalid input content type` | Usar tipos de conteúdo `input_text`/`output_text` em vez de Chat `text` |
| `invalid input content type` (imagem) | Tipo de conteúdo da imagem ainda usa `"type": "image_url"` | Alterar para `"type": "input_image"` |
| `Expected object, got string` em `image_url` | `image_url` ainda é um objeto aninhado `{"url": "..."}` | Achatar para uma string simples: `"image_url": "https://..."` ou `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` para `max_output_tokens` | Mínimo é **16** no Azure OpenAI. Use 50+ para testes, 1000+ para produção. |
| `429 Too Many Requests` durante stream | Limitação de taxa (rate limited). Envolver stream em `try/except`, emitir JSON de erro para frontend, implementar backoff/tentativas. |
| `KeyError: 'innererror'` no erro do content filter | A estrutura do corpo do erro do content filter mudou na API Responses | Chat Completions usava `error.body["innererror"]["content_filter_result"]`; API Responses usa `error.body["content_filters"][0]["content_filter_results"]` (plural, dentro de array). Reescrever todo acesso a `innererror`. |

---

## Tabela de Riscos da Migração

| Sintoma | Erro Provável | Correção |
|---------|---------------|-----|
| `output_text` vazio / resposta truncada | `max_output_tokens` demasiado baixo para modelos de raciocínio | Definir `max_output_tokens=1000` ou superior — tokens de raciocínio contam para o limite |
| `400 invalid_type: text.format` | Passado string `response_format` em vez de dicionário `text.format` | Usar `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` em `/openai/v1/responses` | `base_url` errado — falta sufixo `/openai/v1/` | Garantir `base_url=f"{endpoint}/openai/v1/"` (com barra final) |
| `401 Unauthorized` após mudar para `OpenAI()` | `api_key` não definido ou token provider passado incorretamente | Para EntraID: `api_key=token_provider` (a callable). Para chave API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Modelo retorna `deployment not found` | Parâmetro `model` não corresponde ao nome do seu deployment Azure | Usar `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — este é o nome do deployment, não o do modelo |
| `json.loads(resp.output_text)` lança `JSONDecodeError` | Schema não aplicado ou modelo não suporta JSON rígido | Garantir `"strict": True` no schema e verificar suporte do modelo para saída estruturada |
| Streaming não produz eventos `delta` | Verificar tipo de evento errado | Filtrar por `event.type == "response.output_text.delta"`, não por Chat `chat.completion.chunk` |
| Erro `400` em input de imagem após migração | Tipo de conteúdo da imagem não atualizado | Alterar `"type": "image_url"` → `"type": "input_image"` e achatar `"image_url": {"url": "..."}` → `"image_url": "..."` (string simples) |
| Chamadas de ferramentas em loop infinito | Falta resultado da ferramenta no `input` seguinte | Após executar uma ferramenta, adicionar item `{"type": "function_call_output", "call_id": ..., "output": ...}` ao `input` da próxima requisição |
| Erro `temperature` com GPT-5 ou série o | Valor explícito de `temperature` diferente de 1 | Remover `temperature` ou definir para `1` nos modelos GPT-5 e da série o (o1, o3-mini, o3, o4-mini) |
| Erro `top_p` com série o | `top_p` não suportado | Remover `top_p` quando usar modelos da série o |
| `max_completion_tokens` não reconhecido | Uso de parâmetro específico Azure | Substituir `max_completion_tokens` por `max_output_tokens`. Definir em 4096+ para série o (tokens de raciocínio contam para o limite). |
| Saída vazia/truncada da série o | `max_output_tokens` demasiado baixo | Série o usa tokens de raciocínio internamente. Definir `max_output_tokens=4096` ou superior — não 500–1000. |
| `400 integer_below_min_value` para `max_output_tokens` | Valor inferior a 16 | Azure OpenAI exige `max_output_tokens >= 16`. Usar 50+ para testes rápidos, 1000+ para produção. |
| `429 Too Many Requests` a meio do stream | Limitação de taxa pela Azure OpenAI | O stream cai silenciosamente sem tratamento de erro. Envolver sempre `async for event in await coroutine:` em `try/except` e emitir `{"error": str(e)}` para o frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Tenant errado ou sessão não iniciada | Passar explicitamente `tenant_id=os.getenv("AZURE_TENANT_ID")`. Executar `azd auth login --tenant <tenant-id>` localmente. |
| `404 Not Found` usando GitHub Models (`models.github.ai`) | GitHub Models não suporta API Responses | Remover completamente o caminho de código GitHub Models. Usar Azure OpenAI, OpenAI ou endpoint local compatível (ex.: Ollama com suporte a Responses). |
| MAF `OpenAIChatCompletionClient` ainda usa Chat Completions | Uso do cliente MAF legado em 1.0.0+ | Em MAF 1.0.0+, `OpenAIChatClient` usa por defeito a API Responses. Substituir `OpenAIChatCompletionClient` por `OpenAIChatClient`. Para versões pré-1.0.0, atualizar para `agent-framework-openai>=1.0.0`. |
| Agente LangChain retorna vazio ou falha com chamadas de ferramentas | `ChatOpenAI` não usa Responses API | Acrescentar `use_responses_api=True` a `ChatOpenAI(...)`. Também alterar `.content` → `.text` nas mensagens de resposta. |
| `KeyError: 'innererror'` no handler do erro do content filter | Estrutura do corpo do erro mudou na API Responses | Reescrever `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. O wrapper `innererror` desapareceu; detalhes do filtro de conteúdo estão agora num array de topo `content_filters` com `content_filter_results` (plural) dentro de cada item. |
| Chamada HTTP direta a `/openai/deployments/.../chat/completions` retorna 404 | Antigo endpoint REST do Chat Completions | Reescrever URL para `/openai/v1/responses`. Alterar corpo do pedido: `messages` → `input`, adicionar `max_output_tokens` + `store: false`, remover query param `api-version`. Ajustar parsing da resposta: `choices[0].message.content` → `output[0].content[0].text` (nota: `output_text` é propriedade de conveniência do SDK, não está no JSON REST bruto). |

---

## Armadilhas

1. Se usava anteriormente Chat Completions para o estado da conversa, gere o seu estado explicitamente com Responses.
2. Prefira `max_output_tokens` em vez do legado `max_tokens`.
3. Ao migrar para `gpt-5`, garantir que `temperature` não está especificado ou está definido para `1`.
4. Substituir Chat `content[].type: "text"` por Responses `content[].type: "input_text"` para inputs de utilizador/sistema.
5. Para `text.format`, fornecer um dicionário adequado (ex.: `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), não uma string simples.
6. O parâmetro `seed` não é suportado em Responses; removê-lo dos pedidos.
7. **Raciocínio**: Incluir `reasoning` apenas se o código original já o usasse. Não adicionar `reasoning` a chamadas API que não o tivessem — muitos modelos não de raciocínio não suportam este parâmetro.
8. **Dimensionamento de `max_output_tokens`**: Para modelos de raciocínio (GPT-5-mini, GPT-5, série o), usar `max_output_tokens=4096` ou superior — não 50–1000. O modelo usa tokens de raciocínio internamente antes de gerar saída visível; limites baixos causam respostas truncadas ou vazias.
9. **`max_completion_tokens` da série o**: Se o código original usava `max_completion_tokens` (específico Azure para série o), substituir por `max_output_tokens`. A API Responses não aceita `max_completion_tokens`.
10. **`reasoning_effort` da série o**: Se o código original usa `reasoning_effort` (low/medium/high), migrar para `reasoning={"effort": "<valor>"}` na chamada API Responses.
11. **Atraso no streaming da série o**: Modelos da série o realizam raciocínio interno antes de gerar saída. No streaming, esperar atraso maior antes do primeiro evento `response.output_text.delta`. Isto é normal — o modelo está a raciocinar, não está bloqueado.
9. **`_azure_ad_token_provider` desapareceu**: `AsyncOpenAI` / `OpenAI` não têm atributo `_azure_ad_token_provider`. Testes ou código que acedem a este atributo falharão com `AttributeError`. O token provider é passado como `api_key` e não é inspecionável no objeto cliente.
10. **Ficheiros Snapshot / golden**: Se o conjunto de testes usar snapshot testing, **todos** os ficheiros snapshot com formas de streaming Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, etc.) devem ser atualizados para a nova forma Responses. É fácil esquecer e causa falhas nas asserções de snapshot.
11. **Caminho do monkeypatch no mock**: O alvo do monkeypatch mudou de `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (ou `Responses.create` para síncrono). Usar o caminho antigo não tem efeito — o mock não intercepta e os testes alcançam a API real ou falham.
12. **`input`, não `messages`**: Funções de mock devem ler `kwargs.get("input")`, não `kwargs.get("messages")`. A API Responses usa `input` para o histórico da conversa.
13. **Nomeação da variável de ambiente**: Azure Identity SDK usa `AZURE_CLIENT_ID` (não `AZURE_OPENAI_CLIENT_ID`) para `ManagedIdentityCredential(client_id=...)`. Renomear em testes, ficheiros `.env`, definições da app e Bicep/infra.
14. **Mínimo de `max_output_tokens` é 16**: Azure OpenAI rejeita valores abaixo de 16 com erro `400 integer_below_min_value`. Usar `50` para testes rápidos, `1000`+ para produção. O antigo `max_tokens` não tinha esse mínimo.
15. **`tenant_id` para `AzureDeveloperCliCredential`**: Quando o recurso Azure OpenAI está num tenant diferente, deve-se passar `tenant_id` explicitamente — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Sem ele, a credencial usa silenciosamente o tenant errado e retorna `401`.
16. **Limites de taxa aparecem de forma diferente no streaming**: Com Chat Completions, um 429 geralmente impedia o stream de começar. Com streaming da API Responses, um 429 pode ocorrer **a meio do stream** — o iterador async lança exceção. Envolver sempre o loop de streaming em `try/except` e emitir uma linha JSON de erro para que o frontend possa gerir graciosamente.

17. **O tratamento de erros em streaming é obrigatório para aplicações web**: O padrão `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` é crítico. Sem ele, o fluxo SSE/JSONL morre silenciosamente em qualquer erro do lado do servidor e o frontend fica bloqueado.
18. **As definições de ferramentas devem usar o formato plano**: A API Responses espera `{"type": "function", "name": ..., "parameters": ...}` — e não o formato aninhado do Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Este é o erro de migração mais comum no código de chamada de funções.
19. **`pydantic_function_tool()` é incompatível**: O auxiliar `openai.pydantic_function_tool()` ainda gera o formato aninhado antigo. Não o use com `responses.create()`. Defina os esquemas de ferramentas manualmente ou achate a saída.
20. **Os resultados da ferramenta usam `function_call_output`, não `role: tool`**: Após executar uma ferramenta, anexe `{"type": "function_call_output", "call_id": ..., "output": ...}` — e não `{"role": "tool", "tool_call_id": ..., "content": ...}`. Para a requisição da ferramenta do assistente, use `messages.extend(response.output)` — e não um dicionário manual `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` requer `required` + `additionalProperties: false`**: Ao usar `strict: true` numa ferramenta, todas as propriedades devem estar listadas no array `required` e `additionalProperties` deve ser `false`. Falhar em um destes causa erro 400.
22. **Os IDs de chamadas de função têm prefixos específicos**: Ao fornecer itens few-shot `function_call` em `input`, o campo `id` deve começar com `fc_` e o campo `call_id` deve começar com `call_` (por exemplo, `"id": "fc_example1", "call_id": "call_example1"`). Usar o prefixo antigo do Chat Completions `call_` para `id` é rejeitado.
23. **GitHub Models não suporta a API Responses**: Se a aplicação tiver uma rota de código GitHub Models (`base_url` apontando para `models.github.ai` ou `models.inference.ai.azure.com`), remova-a completamente. Não há caminho de migração — mude para Azure OpenAI, OpenAI ou um endpoint local compatível.
24. **Mudou a estrutura do corpo do erro do filtro de conteúdo**: Os erros do Chat Completions usavam `error.body["innererror"]["content_filter_result"]` (singular). Os erros da API Responses usam `error.body["content_filters"][0]["content_filter_results"]` (plural, dentro de um array). A chave `innererror` deixou de existir. Código que acessa `innererror` diretamente vai lançar `KeyError` em tempo de execução — isto é fácil de passar despercebido na migração porque só aparece quando o filtro de conteúdo é realmente acionado. Sempre faça grep por `innererror` durante a migração.
25. **Chamadas HTTP brutas precisam de reescrita de URL + corpo**: Aplicações que chamam diretamente o REST Azure OpenAI (via `requests`, `httpx`, `aiohttp`) usando `/openai/deployments/{name}/chat/completions?api-version=...` devem mudar para `/openai/v1/responses`. O corpo da requisição usa `input` em vez de `messages`, requer `max_output_tokens` e `store`, e o parâmetro de query `api-version` é removido. O texto do corpo da resposta está em `output[0].content[0].text` — **não** em `output_text`, que é uma propriedade de conveniência do SDK não presente no JSON bruto do REST.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->