---
name: azure-openai-to-responses
license: MIT
description: 'Move Python apps from Azure OpenAI Chat Completions go Responses API.
  E cover AzureOpenAI/AsyncAzureOpenAI client move go di v1 endpoint, streaming, tools,
  structured output, multi-turn, EntraID auth, and model compatibility checks. E dey
  Python-focused, Azure OpenAI-specific. USE FOR: move to responses API, switch from
  chat completions, openai responses, upgrade openai SDK, responses API migration,
  shift from completions to responses, gpt-5 migration, azure openai python migration,
  chat completions to responses, AzureOpenAI to OpenAI client, python azure openai
  upgrade. NO USE FOR: building new apps from scratch (start with responses directly),
  Node/TypeScript/C#/Java/Go migrations (dis skill na Python-only), Azure infrastructure
  setup (use azure-prepare), deploying models (use microsoft-foundry).'
---
# Migrate Python Apps from Azure OpenAI Chat Completions to Responses API

> **AUTHORITY GUIDE — FOLLOW SHARP-SHARP**
>
> Dis skill dey migrate Python codebases wey dey use Azure OpenAI Chat Completions
> go the unified Responses API. Follow all dis tins correct-correct.
> No make you dey waka for road dey add parameter mappings or invent new API shapes.

---

## Triggers

Activate dis skill when user wan:
- Migrate Python app from Azure OpenAI Chat Completions go Responses API
- Upgrade Python OpenAI SDK usage to the latest API shape for Azure OpenAI
- Prepare Python code for GPT-5 or newer models wey need Responses for Azure
- Change from `AzureOpenAI`/`AsyncAzureOpenAI` to standard `OpenAI`/`AsyncOpenAI` client with the v1 endpoint
- Fix any warnings about `AzureOpenAI` constructors or `api_version` wey don old

---

## ⚠️ Model Compatibility — CHECK FIRST

> **Before you start to migrate, make sure say your Azure OpenAI deployment dey support Responses API.**

### 1. Do small test (fastest)

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

> **Note**: `max_output_tokens` get **minimum of 16** for Azure OpenAI. If e less than 16, e go cause 400 error. Use 50+ tokens for the small test.

If dis one waka give you 404, e mean say the deployment model never support Responses yet — check the link wey dey below or redeploy with model wey support am.

### 2. Check which models dey available for your area (recommended)

Run the model compatibility tool wey dey built-in to check which models get Responses API support for your region:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

This one dey query Azure ARM live and e go show compatibility matrix — which models support Responses, structured output, tools, etc. You fit use `--filter gpt-5.1,gpt-5.2` to limit the results or `--json` to do scripting.

### 3. Full model support check list

- **Live query**: `python migrate.py models` (see above — region specific, always up to date)
- **Browse availability**: [Model summary table and region availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Quickstart & guidance**: **https://aka.ms/openai/start**

### ⚠️ Older model yawa

> **WARNING**: Older models (example: `gpt-4o`, `gpt-4`) no fit support all Responses API features complete.
>
> Known wahala with older models:
> - **`reasoning` parameter**: No support for `gpt-4o-mini`, `gpt-4o`, and plenty non-reasoning models. Only move `reasoning` if e dey for your original code.
> - **`seed` parameter**: E no support Responses API at all — make sure say you commot am from all requests.
> - **Structured output using `text.format`**: Older models no too dey follow `strict: true` JSON schemas well-well.
> - **Tool control**: GPT-5+ dey do tool calls as part of internal reasoning. Older models dey work for Responses but dem no get this deep style.
> - **Temperature levels**: If you dey migrate to `gpt-5`, temperature must be commot or e suppose be `1`. Older models no get this kind limit.

### O-series reasoning models (o1, o3-mini, o3, o4-mini)

O-series models get their own special rules for parameters. If your app dey use o-series models:

- **`temperature`**: E suppose be `1` (or commot am). O-series no dey accept any other value.
- **`max_completion_tokens` → `max_output_tokens`**: Apps wey dey use Azure `max_completion_tokens` must change go `max_output_tokens`. Put high value (4096+) because reasoning tokens dey count.
- **`reasoning_effort`**: If app dey use `reasoning_effort` (low/medium/high), make e dey — Responses API dey support am for o-series models.
- **Streaming behavior**: O-series fit dey keep output until reasoning finish before e start to send text delta events. Streaming go still work, but the first `response.output_text.delta` fit delay pass GPT models.
- **`top_p`**: O-series no support dis — commot if e dey.
- **Tool use**: O-series support tools through Responses API same way as GPT models, but the way dem organize tool calls fit differ by model.

**Action — proactive model advice**: When you dey scan, check which model the app dey use (deployment names, env vars, config). If the model na `gpt-4o` or older (no be gpt-4.1+), advise the user:
- Migration go work for basic text, chat, streaming, and tools on their current model.
- Newer models (`gpt-5.1`, `gpt-5.2`) get better tool control, structured output enforcement, reasoning, and dey available for more regions.
- Dem suppose plan to upgrade their deployment when dem ready — e no dey block the migration.

No make you block or reject migration because of model version. Na just advice be dis.

### GitHub Models no support Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) no support Responses API.**

If your codebase get GitHub Models path (look for `base_url` weh point `models.github.ai` or `models.inference.ai.azure.com`), **remove am finish** during migration. Responses API need Azure OpenAI, OpenAI, or local compatible endpoint (like Ollama with Responses support).

Action during scan:
- Mark any GitHub Models code path for removal.

---

## Framework Migration

Many apps dey use higher-level frameworks on top of OpenAI. When you dey migrate these, the framework API go change — no be only OpenAI calls knnknn.

### Microsoft Agent Framework (MAF)

**Check your MAF version first** — di migration depend on if you dey use MAF 1.0.0+ or pre-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **dey use Responses API now** — no migration needed. If your code use old `OpenAIChatCompletionClient` (wey use `chat.completions.create`), change am go `OpenAIChatClient`.

| Before | After |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

To check version: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc releases)

For pre-1.0.0 MAF, `OpenAIChatClient` still use Chat Completions. Upgrade to `agent-framework-openai>=1.0.0` make `OpenAIChatClient` dey use Responses API by default.

No other change needed — `Agent` and tool APIs remain same.

### LangChain (`langchain-openai`)

Add `use_responses_api=True` for `ChatOpenAI()`. Change response get from `.content` to `.text`.

| Before | After |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

For full before/after code examples, see [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontend Migration Guide

> **Responses API na server-side matter.** Migrate your Python backend; frontend HTTP contract no suppose change unless your backend na thin pass-through — then consider use Responses request shape to remove translation layer. If frontend dey call OpenAI directly with client key, move calls go backend first.

### `@microsoft/ai-chat-protocol` deprecated

The `@microsoft/ai-chat-protocol` npm package don old and e suppose be replaced with [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). If you see am for frontend:

1. Replace the CDN script tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Remove the `AIChatProtocolClient` instance (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Replace `client.getStreamedCompletion(messages)` with direct `fetch()` call to backend streaming endpoint.
4. Replace `for await (const response of result)` with `for await (const chunk of readNDJSONStream(response.body))`.
5. Change property access from `response.delta.content` / `response.error` to `chunk.delta.content` / `chunk.error`.

---

## Goals

- Make list of all Python call sites wey dey use Chat Completions or old Completions for Azure OpenAI.
- Suggest migration plan and correct order for Python codebase.
- Do safe, small edits to switch go Responses API.
- Update callers to use Responses output structure; no shim for back compatibility.
- Run tests/lints; fix small breaks wey migration cause.
- Prepare small, reviewable change sets and give final summary with diffs (no commit).

---

## Guardrails

- Only change files inside git workspace. No write outside.
- No keep old backward-compatibility shims; migrate well to new API shape.
- No leave tombstone/transition comments or backup files.
- Keep streaming semantics if e dey before; else use non-streaming.
- Ask for approval before you run commands or network calls if in approval mode.
- No run `git add`/`git commit`/`git push`; only make working-tree edits.

---

## Step 0: Azure OpenAI Client Migration (Prerequisite)

If your code dey use `AzureOpenAI` or `AsyncAzureOpenAI` constructors, migrate first to standard `OpenAI` / `AsyncOpenAI` constructors. Azure specific constructors don become old for `openai>=1.108.1`.

### Why di v1 API path?

The new `/openai/v1` endpoint dey use standard `OpenAI()` client not `AzureOpenAI()`, no need `api_version` parameter, and e fit work same for OpenAI and Azure OpenAI. The client code na future-proof — no need manage version.

### Key changes

| Before | After |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Remove everything |

### Cleanup checklist

- Remove `api_version` argument from client construction.
- Remove `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` environment variables from `.env`, app settings, and Bicep/infra files.
- Rename `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` in `.env`, app settings, Bicep/infra, and test fixtures (standard Azure Identity SDK style).
- Make sure `openai>=1.108.1` dey for `requirements.txt` or `pyproject.toml`.

### Environment variable migration

| Old env var | Action | Notes |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Remove** | No `api_version` needed for v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Remove** | Same as above |
| `AZURE_OPENAI_CLIENT_ID` | **Rename** → `AZURE_CLIENT_ID` | Standard Azure Identity SDK convention for `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Keep** | Still needed for `base_url` construction |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Keep** | Used as `model` param in `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Keep** | Used as `api_key` for key-based auth |

For client setup code examples (sync, async, EntraID, API key, multi-tenant), check [cheat-sheet.md](./references/cheat-sheet.md).

---

## Step 1: Detect Old Call Sites

Run [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) script to find all call sites wey need migration:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Or run these searches by hand — every match na migration target:

```bash
# Old API calls (gats rewrite)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Old Azure client constructors (gats change)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# How we dey access response shape (gats update)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Tool definitions wey still old nested format (gats make am flat)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Tool results wey old format (gats convert to function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Old parameters (gats remove or change name)
rg "response_format"
rg "max_tokens\b"        # change name to max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Old environment variables (gats clean)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # e suppose be AZURE_CLIENT_ID

# GitHub Models endpoints (gats remove — Responses API no dey supported)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Framework-level old patterns (gats update)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: change to OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: need use_responses_api=True

# Test setup (gats update)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# How to access content filter error body (gats update — structure don change)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # Old singular form — now content_filter_results (plural) inside content_filters array

# Raw HTTP calls to Chat Completions endpoint (gats update URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### How to identify and rewrite

- **Chat Completions client**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure client constructors**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Tools**: convert function-calling tool definitions from nested format (`{"type": "function", "function": {"name": ...}}`) to flat Responses format (`{"type": "function", "name": ...}`); use `tool_choice`; return tool results as `{"type": "function_call_output", "call_id": ..., "output": ...}` items (not `{"role": "tool", ...}`).
- **Tool round-trips**: when the model returns function calls, append `response.output` items to the conversation (not a manual `{"role": "assistant", "tool_calls": [...]}` dict), then append `function_call_output` items for each result.
- **Few-shot tool examples**: if the conversation includes hardcoded tool call examples, convert them to `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` items. IDs must start with `fc_`.
- **`pydantic_function_tool()`**: this helper still generates the old nested format and is **not compatible** with `responses.create()`. Replace with manual tool definitions or a flattening wrapper.
- **Multi-turn**: maintain conversation history in the app; pass prior turns via `input` items.
- **Formatting**: replace Chat's top-level `response_format` with `text.format` in Responses. Canonical shape: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Content items**: replace Chat `content[].type: "text"` with Responses `content[].type: "input_text"` for user/system turns.
- **Image content items**: replace Chat `content[].type: "image_url"` with Responses `content[].type: "input_image"`. The `image_url` field changes from a nested object `{"url": "..."}` to a flat string. See the cheat sheet for before/after examples.
- **Reasoning effort**: **only migrate `reasoning` if it already exists in the original code**.
- **Content filter error handling**: the error body structure changed. Chat Completions used `error.body["innererror"]["content_filter_result"]` (singular); Responses API uses `error.body["content_filters"][0]["content_filter_results"]` (plural, inside an array). Code that accesses `innererror` will raise `KeyError`. Rewrite to use the new path.
- **Raw HTTP calls**: if the app calls the Azure OpenAI REST API directly (via `requests`, `httpx`, etc.) using `/openai/deployments/{name}/chat/completions?api-version=...`, rewrite to `/openai/v1/responses`. The request body changes: `messages` → `input`, add `max_output_tokens` and `store: false`, remove `api-version` query param. The response body changes: `choices[0].message.content` → `output[0].content[0].text` (note: `output_text` is an SDK convenience property not present in raw REST JSON).

---

## Step 2: Apply Migration

### Migration notes (Chat Completions → Responses)

- **Why migrate**: Responses na di unified API for text, tools, and streaming; Chat Completions na old one. Wit GPT-5, Responses na di one wey you need for best performance.
- **HTTP**: Azure endpoint change from `/openai/deployments/{name}/chat/completions` to `/openai/v1/responses`.
- **Fields**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` still dey the same.
- **Formatting**: `response_format` → `text.format` wit correct object.
- **Content items**: Replace Chat `content[].type: "text"` wit Responses `content[].type: "input_text"` for system/user turns.
- **Image content items**: Replace Chat `content[].type: "image_url"` wit Responses `content[].type: "input_image"`. Flatten the `image_url` field from `{"image_url": {"url": "..."}}` to `{"image_url": "..."}` (na plain string — fit be HTTPS URL or `data:image/...;base64,...` data URI).

### Parameter mapping reference

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array of items) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (object) |
| `temperature` | `temperature` (unchanged) |
| `stop` | `stop` (unchanged) |
| `frequency_penalty` | `frequency_penalty` (unchanged) |
| `presence_penalty` | `presence_penalty` (unchanged) |
| `tools` / function-calling | `tools` (unchanged) |
| `seed` | **Remove** (no support for am) |
| `store` | `store` (set to `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (flat string) |

For complete before/after code examples, see [cheat-sheet.md](./references/cheat-sheet.md).

For test infrastructure migration (mocks, snapshots, assertions), see [test-migration.md](./references/test-migration.md).

For troubleshooting errors and gotchas, see [troubleshooting.md](./references/troubleshooting.md).

---

## Data Retention & State

- Set `store: false` on all Responses requests.
- No rely on old message IDs or server-stored context; keep state client-dey manage and minimize metadata.

---

## Acceptance Criteria

### Code-level gates (all must pass)

- [ ] Zero matches for `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` for migrated files.
- [ ] Zero matches for `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — all constructors use `OpenAI`/`AsyncOpenAI` wit v1 endpoint.
- [ ] Zero matches for `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub Models code paths don remove.
- [ ] Zero matches for `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ code dey use `OpenAIChatClient` (wey dey use Responses API). If na before 1.0.0, upgrade to `agent-framework-openai>=1.0.0`.
- [ ] All `ChatOpenAI(...)` calls include `use_responses_api=True`.
- [ ] Zero matches for `rg "choices\[0\]"` — all response access dey use `resp.output_text` or the Responses output schema.
- [ ] No `response_format` for top level; all structured output dey use `text={"format": {...}}`.
- [ ] `openai>=1.108.1` and `azure-identity` dey inside `requirements.txt` or `pyproject.toml`; dependencies dey reinstalled.
- [ ] `store=False` set for every `responses.create` call.
- [ ] No `api_version` for client construction; `AZURE_OPENAI_API_VERSION` remove for env files and infra.

### Test infrastructure gates (all must pass)

- [ ] Zero matches for `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Zero matches for `rg "_azure_ad_token_provider" tests/` — assertions don update to check `isinstance(client, AsyncOpenAI)` or `base_url`.
- [ ] Zero matches for `rg "prompt_filter_results|content_filter_results" tests/` — Azure-specific filter mocks don remove.
- [ ] Mock fixtures dey use `kwargs.get("input")` no be `kwargs.get("messages")`.
- [ ] Snapshot / golden files update to Responses streaming shape (no `choices[0]`, `function_call`, `logprobs`, etc.).
- [ ] `pytest` pass wit zero failures after all test updates.

### Behavioral gates (man go check or use test harness)

- [ ] **Basic completion**: non-streaming `responses.create` dey return non-empty `output_text`.
- [ ] **Stream parity**: if original code use streaming, migrated code go stream and yield `response.output_text.delta` events wit non-empty deltas.
- [ ] **Structured output**: if you dey use `text.format` wit `json_schema`, `json.loads(resp.output_text)` go succeed and e go match the schema.
- [ ] **Tool-call loop**: if tools dey used, model go issue tool calls, app go execute dem, and follow-up request go return final `output_text` (no infinite loop).
- [ ] **Async parity**: if `AsyncAzureOpenAI` dey used, `AsyncOpenAI` equivalent go work wit `await`.
- [ ] **Error rate**: no new 400/401/404 errors compared to pre-migration baseline.

### Deliverables

- Summary go include edited files, before/after counts of legacy call sites, and next steps.
- Changes na working-tree edits only (no commits).

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