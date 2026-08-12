---
name: azure-openai-to-responses
license: MIT
description: 'Shift Python apps dem from Azure OpenAI Chat Completions go Responses
  API. E cover AzureOpenAI/AsyncAzureOpenAI client shift go v1 endpoint, streaming,
  tools, structured output, multi-turn, EntraID auth, plus model compatibility checks.
  Na Python-focused, Azure OpenAI-specific. USE FOR: shift go responses API, change
  from chat completions, openai responses, upgrade openai SDK, responses API migration,
  move from completions go responses, gpt-5 migration, azure openai python migration,
  chat completions go responses, AzureOpenAI go OpenAI client, python azure openai
  upgrade. DO NOT USE FOR: build new apps from scratch (start with responses directly),
  Node/TypeScript/C#/Java/Go migrations (dis skill na Python-only), Azure infrastructure
  setup (use azure-prepare), deploy models (use microsoft-foundry).'
---
# Migrate Python Apps from Azure OpenAI Chat Completions to Responses API

> **AUTHORITATIVE GUIDANCE — FOLLOW EXACTLY**
>
> Dis skill dey migrate Python code wey dey use Azure OpenAI Chat Completions
> come use di unified Responses API. Abeg follow dis instructions sharply.
> No try do your own mapping of parameters or create new API shapes.

---

## Triggers

Activate dis skill wen user want:
- Migrate a Python app from Azure OpenAI Chat Completions to Responses API
- Upgrade Python OpenAI SDK usage to di latest API shape for Azure OpenAI
- Prepare Python code for GPT-5 or newer models wey need Responses on Azure
- Switch from `AzureOpenAI`/`AsyncAzureOpenAI` go standard `OpenAI`/`AsyncOpenAI` client with di v1 endpoint
- Fix deprecation warnings wey concern `AzureOpenAI` constructors or `api_version`

---

## ⚠️ Model Compatibility — CHECK FIRST

> **Before you migrate, make sure say your Azure OpenAI deployment support Responses API.**

### 1. Smoke-test your deployment (fastest)

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

> **Note**: `max_output_tokens` get **minimum 16** for Azure OpenAI. If value less than 16, e go return 400 error. Use 50+ for smoke tests.

If e return 404, e mean say di deployment model no de support Responses yet — check di reference down or redeploy with correct model.

### 2. Check models wey dey your region (recommended)

Run di built-in model compatibility tool to see wetin dey available with Responses API support for your region:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Dis one dey query Azure ARM live and show compatibility matrix — which models dey support Responses, structured output, tools, etc. Use `--filter gpt-5.1,gpt-5.2` to narrow results or `--json` for scripting.

### 3. Full model support reference

- **Live query**: `python migrate.py models` (see am above — region-specific, always updated)
- **Browse availability**: [Model summary table and region availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Quickstart & guidance**: **https://aka.ms/openai/start**

### ⚠️ Older model limitations

> **WARNING**: Older models (before `gpt-4.1`) fit no fit support all Responses API features fully.
>
> Known limitations with older models:
> - **`reasoning` parameter**: No support for many non-reasoning models. Only migrate `reasoning` if e already dey for original code.
> - **`seed` parameter**: No dey support at all for Responses API — remove from all requests.
> - **Structured output via `text.format`**: Older models no sure to enforce `strict: true` JSON schemas well.
> - **Tool orchestration**: GPT-5+ dey manage tool calls as part of internal reasoning. Older models for Responses still dey work but dem no get dis deep integration.
> - **Temperature constraints**: Wen you dey migrate to `gpt-5`, temperature gats be blank or set to `1`. Older models no get dis kind limit.

### O-series reasoning models (o1, o3-mini, o3, o4-mini)

O-series models get them own special parameter limits. If your app dey target o-series models during migration:

- **`temperature`**: Gats be `1` (or no include am). O-series no fit take other values.
- **`max_completion_tokens` → `max_output_tokens`**: Apps wey dey use Azure-specific `max_completion_tokens` must switch go `max_output_tokens`. Set am high (4096+) because reasoning tokens dey count against limit.
- **`reasoning_effort`**: If app dey use `reasoning_effort` (low/medium/high), keep am — Responses API support this for o-series models.
- **Streaming behavior**: O-series models fit hold output till reasoning finish before e dey send text delta events. Streaming still work, but first `response.output_text.delta` fit show late than GPT models.
- **`top_p`**: No support for o-series — remove if e dey.
- **Tool use**: O-series models support tools via Responses API same as GPT, but tool call orchestration quality depend on model.

**Action — proactive model advisory**: During scan, check which model app dey target (deployment names, env vars, config). If model before `gpt-4.1` (no be gpt-4.1+), tell user beforehand:
- Migration go work for basic text, chat, streaming, and tools for their current model.
- Newer models (`gpt-5.1`, `gpt-5.2`) get better tool orchestration, structured output enforcement, reasoning, and cross-region availability.
- Dem suppose think about upgrading deployment when dem ready — e no go block migration.

No block or refuse migrate based on model version. Dis advisory be just info.

### GitHub Models no support Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) no support Responses API.**

If codebase get GitHub Models path (look for `base_url` wey point to `models.github.ai` or `models.inference.ai.azure.com`), **remove am completely** during migration. Responses API need Azure OpenAI, OpenAI, or compatible local endpoint (e.g., Ollama with Responses support).

Action during scan:
- Flag any GitHub Models code paths for removal.

---

## Framework Migration

Plenty apps dey use higher-level frameworks on top of OpenAI. When you dey migrate dem, the framework own API go change — no be only the underlying OpenAI calls.

### Microsoft Agent Framework (MAF)

**Check your MAF version first** — migration depends on whether you dey on MAF 1.0.0+ or before 1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **dey use Responses API already** — no migration needed. If codebase dey use old `OpenAIChatCompletionClient` (we dey use `chat.completions.create`), switch am to `OpenAIChatClient`.

| Before | After |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

To check your version: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc releases)

For pre-1.0.0 MAF, `OpenAIChatClient` dey use Chat Completions. Upgrade to `agent-framework-openai>=1.0.0` so that `OpenAIChatClient` go use Responses API by default.

No other changes dey needed — `Agent` and tools API still the same.

### LangChain (`langchain-openai`)

Add `use_responses_api=True` to `ChatOpenAI()`. Change response access from `.content` to `.text`.

| Before | After |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

For complete before/after code examples, see [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontend Migration Guidance

> **Responses API na server-side matter.** Migrate your Python backend; frontend HTTP contract suppose no change unless your backend na thin pass-through — if na so, consider use Responses request shape to drop translation layer. If frontend dey call OpenAI directly with client-side key, make dem move those calls to backend first.

### `@microsoft/ai-chat-protocol` deprecation

The `@microsoft/ai-chat-protocol` npm package don deprecate, make you replace am with [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). If you see am for frontend:

1. Replace di CDN script tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Remove `AIChatProtocolClient` instantiation (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Replace `client.getStreamedCompletion(messages)` with direct `fetch()` call to backend streaming endpoint.
4. Replace `for await (const response of result)` with `for await (const chunk of readNDJSONStream(response.body))`.
5. Change property access from `response.delta.content` / `response.error` to `chunk.delta.content` / `chunk.error`.

---

## Goals

- List all Python call sites wey dey use Chat Completions or old Completions for Azure OpenAI.
- Propose migration plan and sequence for Python codebase.
- Apply safe, small edits to switch to Responses API.
- Update callers to use Responses output schema; no backcompat wrappers.
- Run tests/lints; fix small breaks introduced by migration.
- Prepare small, reviewable change sets and give final summary with diffs (no commit).

---

## Guardrails

- Only change files inside git workspace. No write outside.
- No preserve backward-compatibility shims; migrate code to new API shape.
- No leave tombstone/transition comments or backup files.
- Keep streaming semantics if e dey before; otherwise use non-streaming.
- Ask approval before run commands or network calls if approval mode dey.
- No run `git add`/`git commit`/`git push`; only produce working-tree edits.

---

## Step 0: Azure OpenAI Client Migration (Prerequisite)

If your codebase dey use `AzureOpenAI` or `AsyncAzureOpenAI` constructors, migrate to standard `OpenAI` / `AsyncOpenAI` constructors first. Azure-specific constructors don deprecate for `openai>=1.108.1`.

### Why the v1 API path?

The new `/openai/v1` endpoint dey use standard `OpenAI()` client instead of `AzureOpenAI()`, no need `api_version` parameter, and e dey work the same for OpenAI and Azure OpenAI. Di same client code dey future-proof — no version management needed.

### Key changes

| Before | After |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Remove completely |

### Cleanup checklist

- Remove `api_version` argument from client construction.
- Remove `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` environment variables from `.env`, app settings, and Bicep/infra files.
- Rename `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` for `.env`, app settings, Bicep/infra, and test fixtures (standard Azure Identity SDK convention).
- Ensure `openai>=1.108.1` in `requirements.txt` or `pyproject.toml`.

### Environment variable migration

| Old env var | Action | Notes |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Remove** | No need `api_version` with v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Remove** | Same as above |
| `AZURE_OPENAI_CLIENT_ID` | **Rename** → `AZURE_CLIENT_ID` | Standard Azure Identity SDK convention for `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Keep** | Still need for `base_url` construction |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Keep** | Use as `model` param in `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Keep** | Use as `api_key` for key-based auth |

For client setup code examples (sync, async, EntraID, API key, multi-tenant), see [cheat-sheet.md](./references/cheat-sheet.md).

---

## Step 1: Detect Legacy Call Sites

Run the [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) script to find all call sites wey need migration:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Or run these searches manually — every match be migration target:

```bash
# Ol API calls (gats rewrite)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Old Azure client constructors (gats change)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# How responses path dem dey access (gats update)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Tool definitions wey dey old inside nested form (gats flatten)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Tool results for old form (gats change to function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Old parameters (gats remove or change name)
rg "response_format"
rg "max_tokens\b"        # change name to max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Old environment variables (gats clean)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # e suppose be AZURE_CLIENT_ID

# GitHub Models endpoints (gats remove — Responses API no dey support)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Framework level old patterns (gats update)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: change to OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: need use_responses_api=True

# Test setup (gats update)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Content filter error body access (gats update — structure don change)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # Old singular form — now content_filter_results (multiple) inside content_filters array

# Raw HTTP calls go Chat Completions endpoint (gats update URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristics (detect and rewrite)

- **Chat Completions client**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure client constructors**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Tools**: change function-calling tool definitions from nested style (`{"type": "function", "function": {"name": ...}}`) go flat Responses style (`{"type": "function", "name": ...}`); use `tool_choice`; return tool results as `{"type": "function_call_output", "call_id": ..., "output": ...}` items (no be `{"role": "tool", ...}`).
- **Tool round-trips**: wen model return function calls, add `response.output` items join the conversation (no be manual `{"role": "assistant", "tool_calls": [...]}` dict), den add `function_call_output` items for each result.
- **Few-shot tool examples**: if conversation get hardcoded tool call examples, change dem to `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` items. IDs suppose start with `fc_`.
- **`pydantic_function_tool()`**: dis helper still dey make old nested style and no **go good** wit `responses.create()`. Replace am wit manual tool definitions or flatten wrapper.
- **Multi-turn**: keep conversation history for the app; pass earlier turns through `input` items.
- **Formatting**: change Chat top-level `response_format` to `text.format` for Responses. Correct shape: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Content items**: change Chat `content[].type: "text"` to Responses `content[].type: "input_text"` for user or system turns.
- **Image content items**: change Chat `content[].type: "image_url"` to Responses `content[].type: "input_image"`. The `image_url` field switch from nested object `{"url": "..."}` to flat string. Check cheat sheet for before and after examples.
- **Reasoning effort**: **ONLY migrate `reasoning` if e already dey for original code**.
- **Content filter error handling**: error body structure don change. Chat Completions used `error.body["innererror"]["content_filter_result"]` (singular); Responses API use `error.body["content_filters"][0]["content_filter_results"]` (plural inside array). Code wey dey use `innererror` go raise `KeyError`. Change am to use di new path.
- **Raw HTTP calls**: if app dey call Azure OpenAI REST API directly (like `requests`, `httpx`, etc.) wen dem dey use `/openai/deployments/{name}/chat/completions?api-version=...`, change dem to `/openai/v1/responses`. Request body change: `messages` → `input`, add `max_output_tokens` and `store: false`, remove `api-version` param. Response body change: `choices[0].message.content` → `output[0].content[0].text` (note: `output_text` na SDK convenience property wey no dey raw REST JSON).

---

## Step 2: Apply Migration

### Migration notes (Chat Completions → Responses)

- **Why migrate**: Responses na one API wey dey handle text, tools, and streaming well-well; Chat Completions don old. Wit GPT-5, Responses dey needed for beta performance.
- **HTTP**: Azure endpoint change from `/openai/deployments/{name}/chat/completions` to `/openai/v1/responses`.
- **Fields**: change `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` no change.
- **Formatting**: change `response_format` to `text.format` wit correct object.
- **Content items**: change Chat `content[].type: "text"` to Responses `content[].type: "input_text"` for system or user turns.
- **Image content items**: change Chat `content[].type: "image_url"` to Responses `content[].type: "input_image"`. Flatten `image_url` field from `{"image_url": {"url": "..."}}` to `{"image_url": "..."}` (plain string — e fit be HTTPS URL or `data:image/...;base64,...` data URI).

### Parameter mapping reference

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array of items) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (object) |
| `temperature` | `temperature` (no change) |
| `stop` | `stop` (no change) |
| `frequency_penalty` | `frequency_penalty` (no change) |
| `presence_penalty` | `presence_penalty` (no change) |
| `tools` / function-calling | `tools` (no change) |
| `seed` | **Remove am** (no support) |
| `store` | `store` (set am to `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (flat string) |

For complete before/after code examples, see [cheat-sheet.md](./references/cheat-sheet.md).

For test infrastructure migration (mocks, snapshots, assertions), see [test-migration.md](./references/test-migration.md).

For troubleshooting errors and gotchas, see [troubleshooting.md](./references/troubleshooting.md).

---

## Data Retention & State

- Make sure `store: false` dey for all Responses requests.
- No rely on previous message IDs or server-stored context; keep state client side and minimize metadata.

---

## Acceptance Criteria

### Code-level gates (all must pass)

- [ ] No find `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` for migrated files.
- [ ] No find `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — all constructors use `OpenAI`/`AsyncOpenAI` with v1 endpoint.
- [ ] No find `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub Models code paths don remove.
- [ ] No find `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ uses `OpenAIChatClient` (wey dey use Responses API). For pre-1.0.0, upgrade to `agent-framework-openai>=1.0.0`.
- [ ] All `ChatOpenAI(...)` calls get `use_responses_api=True`.
- [ ] No find `rg "choices\[0\]"` — all response reading dey use `resp.output_text` or Responses output format.
- [ ] No `response_format` at top level; all structured output use `text={"format": {...}}`.
- [ ] `openai>=1.108.1` and `azure-identity` dey `requirements.txt` or `pyproject.toml`; dependencies don reinstall.
- [ ] `store=False` set for every `responses.create` call.
- [ ] No `api_version` for client build; remove `AZURE_OPENAI_API_VERSION` from env and infra.

### Test infrastructure gates (all must pass)

- [ ] No find `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] No find `rg "_azure_ad_token_provider" tests/` — assertions update to check `isinstance(client, AsyncOpenAI)` or `base_url`.
- [ ] No find `rg "prompt_filter_results|content_filter_results" tests/` — Azure-specific filter mocks don remove.
- [ ] Mock fixtures use `kwargs.get("input")` no be `kwargs.get("messages")`.
- [ ] Snapshot / golden files don update to Responses streaming shape (no `choices[0]`, `function_call`, `logprobs`, etc.).
- [ ] `pytest` pass well wit zero failures after test update.

### Behavioral gates (verify manually or with test harness)

- [ ] **Basic completion**: non-streaming `responses.create` return non-empty `output_text`.
- [ ] **Stream parity**: if original code use streaming, migrated code streams and yield `response.output_text.delta` events wit non-empty deltas.
- [ ] **Structured output**: if you dey use `text.format` wit `json_schema`, `json.loads(resp.output_text)` go succeed and match the schema.
- [ ] **Tool-call loop**: if you dey use tools, model go issue tool calls, app go run dem, then follow-up request go return final `output_text` (no infinite loop).
- [ ] **Async parity**: if you use `AsyncAzureOpenAI` before, `AsyncOpenAI` equivalent go work wit `await`.
- [ ] **Error rate**: no new 400/401/404 errors compared to pre-migration baseline.

### Deliverables

- Summary go show edited files, before/after counts of old call sites, and next steps.
- Changes go be working-tree edits only (no commits).

---

## SDK Version Requirements

| Package | Minimum Version |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Latest (for EntraID auth) |

---

## References

- [Cheat Sheet — all code snippets](./references/cheat-sheet.md)
- [Test Migration — mocks, snapshots, assertions](./references/test-migration.md)
- [Troubleshooting — errors, risk table, gotchas](./references/troubleshooting.md)
- [detect_legacy.py — automated scanner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API docs](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->