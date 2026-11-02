# Resolução de Problemas, Tabela de Riscos e Armadilhas

## Resolução de Problemas em Erros 400

| Erro | Correção |
|-------|-----|
| `missing_required_parameter: tools[0].name` | A definição da ferramenta usa o formato antigo aninhado de Chat Completions | Aplanar de `{"type": "function", "function": {"name": ...}}` para `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters vão no nível superior |
| `unknown_parameter: input[N].tool_calls` | Resultados de ferramenta multi-turno usando o formato antigo de Chat Completions | Substituir `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` por itens `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Ferramenta com `strict: true` faltando array `required` | Quando `strict: true`, todas as propriedades devem estar listadas em `required` e `additionalProperties: false` deve ser definido |
| `invalid_function_parameters: 'additionalProperties' is required` | Ferramenta com `strict: true` faltando `additionalProperties: false` | Adicionar `"additionalProperties": false` ao objeto parameters |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID da chamada de função few-shot com prefixo errado | Os IDs de chamadas de função devem começar com `fc_` (ex.: `fc_example1`), não `call_` |
| `missing_required_parameter: text.format.name` | Adicionar a chave `"name"` ao dict format (ex.: `"name": "Output"`) |
| `invalid_type: text.format` | Garantir que `text.format` seja um dict com chaves `type`, `name`, `strict`, `schema` — não uma string |
| `invalid input content type` | Usar tipos de conteúdo `input_text`/`output_text` em vez de Chat `text` |
| `invalid input content type` (image) | Conteúdo de imagem ainda usa `"type": "image_url"` | Alterar para `"type": "input_image"` |
| `Expected object, got string` em `image_url` | `image_url` ainda é um objeto aninhado `{"url": "..."}` | Aplanar para uma string simples: `"image_url": "https://..."` ou `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` para `max_output_tokens` | Mínimo é **16** na Azure OpenAI. Use 50+ para testes, 1000+ para produção. |
| `429 Too Many Requests` durante streaming | Limite de taxa atingido. Envolver streaming em `try/except`, enviar JSON de erro para frontend, implementar recuo/retry. |
| `KeyError: 'innererror'` em erro de filtro de conteúdo | Estrutura do corpo de erro do filtro de conteúdo mudou na Responses API | Chat Completions usava `error.body["innererror"]["content_filter_result"]`; Responses API usa `error.body["content_filters"][0]["content_filter_results"]` (plural, dentro de um array). Reescrever todo acesso a `innererror`. |

---

## Tabela de Riscos da Migração

| Sintoma | Erro Provável | Correção |
|---------|---------------|-----|
| `output_text` vazio / resposta truncada | `max_output_tokens` muito baixo para modelos de raciocínio | Definir `max_output_tokens=1000` ou mais — tokens de raciocínio contam contra o limite |
| `400 invalid_type: text.format` | Passou string `response_format` em vez de dict `text.format` | Usar `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` em `/openai/v1/responses` | `base_url` incorreto — falta sufixo `/openai/v1/` | Garantir `base_url=f"{endpoint}/openai/v1/"` (com barra final) |
| `401 Unauthorized` após trocar para `OpenAI()` | `api_key` não setado ou token provider não passado corretamente | Para EntraID: `api_key=token_provider` (callable). Para chave API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Modelo retorna `deployment not found` | param `model` não corresponde ao nome do deployment Azure | Usar `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — este é o nome do deployment, não do modelo |
| `json.loads(resp.output_text)` lança `JSONDecodeError` | Schema não aplicado ou modelo não suporta JSON estrito | Garantir `"strict": True` no schema e verificar que o modelo suporta saída estruturada |
| Streaming não produz eventos `delta` | Verificando tipo errado de evento | Filtrar por `event.type == "response.output_text.delta"`, não o `chat.completion.chunk` do Chat |
| Erro `400` em entrada de imagem após migração | Tipo de conteúdo da imagem não atualizado | Trocar `"type": "image_url"` → `"type": "input_image"` e aplanar `"image_url": {"url": "..."}` → `"image_url": "..."` (string simples) |
| Chamadas de ferramenta em loop infinito | Falta o resultado da ferramenta no `input` da requisição seguinte | Após executar uma ferramenta, adicionar item `{"type": "function_call_output", "call_id": ..., "output": ...}` ao `input` na próxima requisição |
| Erro `temperature` com GPT-5 ou série o | Valor explícito de `temperature` diferente de 1 | Remover `temperature` ou definir como `1` para modelos GPT-5 e séries o (o1, o3-mini, o3, o4-mini) |
| Erro `top_p` com série o | `top_p` não suportado | Remover `top_p` ao usar modelos da série o |
| `max_completion_tokens` não reconhecido | Usando parâmetro específico da Azure | Substituir `max_completion_tokens` por `max_output_tokens`. Definir para 4096+ para série o (tokens de raciocínio contam contra o limite). |
| Saída vazia/truncada em série o | `max_output_tokens` muito baixo | Série o usa tokens de raciocínio internamente. Definir `max_output_tokens=4096` ou mais — não 500–1000. |
| `400 integer_below_min_value` para `max_output_tokens` | Valor abaixo de 16 | Azure OpenAI exige `max_output_tokens >= 16`. Usar 50+ para testes simples, 1000+ para produção. |
| `429 Too Many Requests` durante streaming | Limitado pela Azure OpenAI | Stream quebra silenciosamente sem tratamento de erro. Sempre envolver `async for event in await coroutine:` em `try/except` e enviar `{"error": str(e)}` para frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Tenant errado ou não logado | Passar `tenant_id=os.getenv("AZURE_TENANT_ID")` explicitamente. Executar `azd auth login --tenant <tenant-id>` localmente. |
| `404 Not Found` usando GitHub Models (`models.github.ai`) | GitHub Models não suporta Responses API | Remover totalmente o caminho de código dos GitHub Models. Usar Azure OpenAI, OpenAI, ou um endpoint local compatível (ex.: Ollama com suporte a Responses). |
| MAF `OpenAIChatCompletionClient` ainda usa Chat Completions | Usando cliente MAF legado em 1.0.0+ | Em MAF 1.0.0+, `OpenAIChatClient` usa Responses API por padrão. Substituir `OpenAIChatCompletionClient` por `OpenAIChatClient`. Para versões pré-1.0.0, atualizar para `agent-framework-openai>=1.0.0`. |
| Agente LangChain retorna vazio ou falha com chamadas de ferramenta | `ChatOpenAI` não usando Responses API | Adicionar `use_responses_api=True` para `ChatOpenAI(...)`. Também alterar `.content` → `.text` nas mensagens da resposta. |
| `KeyError: 'innererror'` no handler de erro de filtro de conteúdo | Estrutura do corpo de erro mudou na Responses API | Reescrever `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. O wrapper `innererror` desapareceu; detalhes do filtro de conteúdo agora ficam em um array top-level `content_filters` com `content_filter_results` (plural) dentro de cada entrada. |
| Chamada HTTP bruta para `/openai/deployments/.../chat/completions` retorna 404 | Endpoint REST antigo do Chat Completions | Reescrever URL para `/openai/v1/responses`. Alterar corpo da requisição: `messages` → `input`, adicionar `max_output_tokens` + `store: false`, remover parâmetro query `api-version`. Alterar parsing da resposta: `choices[0].message.content` → `output[0].content[0].text` (nota: `output_text` é propriedade de conveniência do SDK, não está no JSON bruto REST). |

---

## Armadilhas

1. Se você usava Chat Completions para gerenciamento de estado da conversa, gerencie seu próprio estado explicitamente com Responses.
2. Prefira `max_output_tokens` em vez do legado `max_tokens`.
3. Ao migrar para `gpt-5`, assegure-se de que `temperature` não seja especificado ou seja definido como `1`.
4. Substitua Chat `content[].type: "text"` por Responses `content[].type: "input_text"` para entradas de usuário/sistema.
5. Para `text.format`, forneça um dict adequado (ex.: `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), não uma string simples.
6. O parâmetro `seed` não é suportado em Responses; remova-o das requisições.
7. **Raciocínio**: Inclua `reasoning` somente se o código original já usava. Não adicione `reasoning` a chamadas API que não o tinham — muitos modelos sem raciocínio não suportam este parâmetro.
8. **Dimensionamento de `max_output_tokens`**: Para modelos de raciocínio (GPT-5-mini, GPT-5, série o), use `max_output_tokens=4096` ou mais — não 50–1000. O modelo usa tokens de raciocínio internamente antes de gerar saída visível; limites baixos causam respostas truncadas ou vazias.
9. **`max_completion_tokens` na série o**: Se o código original usava `max_completion_tokens` (específico da Azure para série o), substitua por `max_output_tokens`. Responses API não aceita `max_completion_tokens`.
10. **`reasoning_effort` na série o**: Se o código usa `reasoning_effort` (baixo/médio/alto), migre para `reasoning={"effort": "<valor>"}` na chamada Responses API.
11. **Atraso no streaming na série o**: Modelos da série o executam raciocínio interno antes de gerar saída. No streaming, espere atraso maior antes do primeiro evento `response.output_text.delta`. Isso é normal — o modelo está raciocinando, não travado.
9. **`_azure_ad_token_provider` sumiu**: `AsyncOpenAI` / `OpenAI` não têm atributo `_azure_ad_token_provider`. Testes ou código que acessam esse atributo falharão com `AttributeError`. O token provider é passado como `api_key` e não é inspecionável no objeto cliente.
10. **Arquivos Snapshot / golden files**: Se o suite de testes usa snapshot testing, **todos** os snapshots contendo formas de streaming Chat Completions (`choices[0]`, `content_filter_results`, `function_call` etc.) devem ser atualizados para a nova forma Responses. Isso é fácil de perder e causa falha nas assertivas de snapshot.
11. **Caminho do monkeypatch no mock**: O alvo do monkeypatch muda de `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (ou `Responses.create` para sync). Usar o caminho antigo não dispara o mock silenciosamente — ele não intercepta, e testes atingem a API real ou falham.
12. **`input`, não `messages`**: Funções mock devem ler `kwargs.get("input")` e não `kwargs.get("messages")`. Responses API usa `input` para histórico da conversa.
13. **Nomenclatura de variáveis de ambiente**: Azure Identity SDK usa `AZURE_CLIENT_ID` (não `AZURE_OPENAI_CLIENT_ID`) para `ManagedIdentityCredential(client_id=...)`. Renomeie em testes, arquivos `.env`, configurações de app e Bicep/infraestrutura.
14. **Mínimo de `max_output_tokens` é 16**: Azure OpenAI rejeita valores abaixo de 16 com `400 integer_below_min_value`. Use `50` para testes rápidos, `1000`+ para produção. O antigo `max_tokens` não tinha mínimo assim.
15. **`tenant_id` para `AzureDeveloperCliCredential`**: Quando o recurso Azure OpenAI está em tenant diferente, você **deve** passar `tenant_id` explicitamente — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Sem isso, a credencial usa silenciosamente o tenant errado e retorna `401`.
16. **Limites de taxa aparecem diferente no streaming**: Com Chat Completions, um 429 normalmente impedia o início do stream. Com Responses API streaming, um 429 pode ocorrer **no meio do stream** — o iterador async lança exceção. Sempre envolver o loop de streaming em `try/except` e enviar linha JSON de erro para frontend tratar graciosamente.

17. **O tratamento de erros em streaming é obrigatório para aplicativos web**: O padrão `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` é crucial. Sem ele, o stream SSE/JSONL morre silenciosamente em qualquer erro do lado do servidor e a interface trava.
18. **Definições de ferramentas devem usar formato plano**: A API Responses espera `{"type": "function", "name": ..., "parameters": ...}` — não o formato aninhado das Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Este é o erro de migração mais comum para código que chama funções.
19. **`pydantic_function_tool()` é incompatível**: O helper `openai.pydantic_function_tool()` ainda gera o formato aninhado antigo. Não o use com `responses.create()`. Defina os schemas das ferramentas manualmente ou achate a saída.
20. **Resultados de ferramentas usam `function_call_output`, não `role: tool`**: Após executar uma ferramenta, adicione `{"type": "function_call_output", "call_id": ..., "output": ...}` — não `{"role": "tool", "tool_call_id": ..., "content": ...}`. Para a requisição da ferramenta pelo assistente, use `messages.extend(response.output)` — não um dicionário manual `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` requer `required` + `additionalProperties: false`**: Ao usar `strict: true` em uma ferramenta, cada propriedade deve estar listada no array `required` e `additionalProperties` deve ser `false`. Faltar algum causa erro 400.
22. **IDs de chamadas de função têm prefixos específicos**: Ao fornecer itens `function_call` few-shot em `input`, o campo `id` deve começar com `fc_` e o campo `call_id` deve começar com `call_` (ex: `"id": "fc_example1", "call_id": "call_example1"`). Usar o prefixo antigo `call_` para `id` das Chat Completions é rejeitado.
23. **GitHub Models não suporta Responses API**: Se o app contém um caminho para GitHub Models (`base_url` apontando para `models.github.ai` ou `models.inference.ai.azure.com`), remova-o completamente. Não há caminho de migração — migre para Azure OpenAI, OpenAI ou um endpoint local compatível.
24. **Estrutura do corpo de erros do filtro de conteúdo mudou**: Erros nas Chat Completions usavam `error.body["innererror"]["content_filter_result"]` (singular). A Responses API usa `error.body["content_filters"][0]["content_filter_results"]` (plural, dentro de um array). A chave `innererror` não existe mais. Código que acessa `innererror` diretamente causará `KeyError` em tempo de execução — fácil de passar despercebido na migração pois só aparece quando o filtro realmente dispara. Faça sempre uma busca por `innererror` na migração.
25. **Chamadas HTTP brutas precisam reescrever URL + corpo**: Apps que chamadas REST diretas à Azure OpenAI (via `requests`, `httpx`, `aiohttp`) usando `/openai/deployments/{name}/chat/completions?api-version=...` devem mudar para `/openai/v1/responses`. O corpo da requisição usa `input` em vez de `messages`, requer `max_output_tokens` e `store`, e o parâmetro de consulta `api-version` é removido. O texto da resposta está em `output[0].content[0].text` — **não** em `output_text`, que é uma propriedade de conveniência do SDK não presente no JSON REST cru.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->