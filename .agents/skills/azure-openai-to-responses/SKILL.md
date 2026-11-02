---
name: azure-openai-to-responses
description: >-
  Migrate Python apps from Azure OpenAI Chat Completions to the Responses API.
  Covers AzureOpenAI/AsyncAzureOpenAI client migration to the v1 endpoint,
  streaming, tools, structured output, multi-turn, EntraID auth, and model
  compatibility checks. Python-focused, Azure OpenAI-specific.
  USE FOR: migrate to responses API, switch from chat completions, openai responses,
  upgrade openai SDK, responses API migration, move from completions to responses,
  gpt-5 migration, azure openai python migration, chat completions to responses,
  AzureOpenAI to OpenAI client, python azure openai upgrade.
  DO NOT USE FOR: building new apps from scratch (start with responses directly),
  Node/TypeScript/C#/Java/Go migrations (this skill is Python-only),
  Azure infrastructure setup (use azure-prepare), deploying models (use microsoft-foundry).
license: MIT
---

# Migrate Python Apps from Azure OpenAI Chat Completions to Responses API

> **AUTHORITATIVE GUIDANCE — FOLLOW EXACTLY**
>
> This skill migrates Python codebases using Azure OpenAI Chat Completions
> to the unified Responses API. Follow these instructions precisely.
> Do not improvise parameter mappings or invent API shapes.

---

## Triggers

Activate this skill when user wants to:
- Migrate a Python app from Azure OpenAI Chat Completions to Responses API
- Upgrade Python OpenAI SDK usage to the latest API shape against Azure OpenAI
- Prepare Python code for GPT-5 or newer models that require Responses on Azure
- Switch from `AzureOpenAI`/`AsyncAzureOpenAI` to standard `OpenAI`/`AsyncOpenAI` client with the v1 endpoint
- Fix deprecation warnings related to `AzureOpenAI` constructors or `api_version`

---

## ⚠️ Model Compatibility — CHECK FIRST

> **Before migrating, verify your Azure OpenAI deployment supports the Responses API.**

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

> **Note**: `max_output_tokens` has a **minimum of 16** on Azure OpenAI. Values below 16 return a 400 error. Use 50+ for smoke tests.

If this returns a 404, the deployment's model doesn't support Responses yet — check the reference below or redeploy with a supported model.

### 2. Check available models in your region (recommended)

Run the built-in model compatibility tool to see what's available with Responses API support in your specific region:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

This queries Azure ARM live and shows a compatibility matrix — which models support Responses, structured output, tools, etc. Use `--filter gpt-5.1,gpt-5.2` to narrow results or `--json` for scripting.

### 3. Full model support reference

- **Live query**: `python migrate.py models` (see above — region-specific, always up to date)
- **Browse availability**: [Model summary table and region availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Quickstart & guidance**: **https://aka.ms/openai/start**

### ⚠️ Older model limitations

> **WARNING**: Older models (those predating `gpt-4.1`) may not support all Responses API features fully.
>
> Known limitations with older models:
> - **`reasoning` parameter**: Not supported on many non-reasoning models. Only migrate `reasoning` if it was already present in the original code.
> - **`seed` parameter**: Not supported in Responses API at all — remove from all requests.
> - **Structured output via `text.format`**: Older models may not enforce `strict: true` JSON schemas reliably.
> - **Tool orchestration**: GPT-5+ orchestrates tool calls as part of internal reasoning. Older models on Responses still work but lack this deep integration.
> - **Temperature constraints**: When migrating to `gpt-5`, temperature must be omitted or set to `1`. Older models have no such constraint.

### O-series reasoning models (o1, o3-mini, o3, o4-mini)

O-series models have unique parameter constraints. When migrating apps that target o-series models:

- **`temperature`**: Must be `1` (or omitted). O-series models do not accept other values.
- **`max_completion_tokens` → `max_output_tokens`**: Apps using the Azure-specific `max_completion_tokens` must switch to `max_output_tokens`. Set high values (4096+) because reasoning tokens count against the limit.
- **`reasoning_effort`**: If the app uses `reasoning_effort` (low/medium/high), keep it — the Responses API supports this parameter for o-series models.
- **Streaming behavior**: O-series models may buffer output until reasoning completes before emitting text delta events. Streaming still works, but the first `response.output_text.delta` may arrive after a longer delay than with GPT models.
- **`top_p`**: Not supported on o-series — remove if present.
- **Tool use**: O-series models support tools via the Responses API the same as GPT models, but tool call orchestration quality varies by model.

**Action — proactive model advisory**: During the scan phase, check which model the app targets (deployment names, env vars, config). If the model predates `gpt-4.1` (not gpt-4.1+), proactively tell the user:
- The migration will work for basic text, chat, streaming, and tools on their current model.
- Newer models (`gpt-5.1`, `gpt-5.2`) offer better tool orchestration, structured output enforcement, reasoning, and cross-region availability.
- They should consider upgrading their deployment when ready — it's not blocking the migration.

Do not block or refuse to migrate based on model version. The advisory is informational.

### GitHub Models does NOT support the Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) does not support the Responses API.**

If the codebase has a GitHub Models code path (look for `base_url` pointing to `models.github.ai` or `models.inference.ai.azure.com`), **remove it entirely** during migration. The Responses API requires Azure OpenAI, OpenAI, or a compatible local endpoint (e.g., Ollama with Responses support).

Action during scan:
- Flag any GitHub Models code paths for removal.

---

## Framework Migration

Many apps use higher-level frameworks on top of OpenAI. When migrating these, the framework's own API changes — not just the underlying OpenAI calls.

### Microsoft Agent Framework (MAF)

**Check your MAF version first** — the migration depends on whether you are on MAF 1.0.0+ or a pre-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **already uses the Responses API** — no migration needed. If the codebase uses the legacy `OpenAIChatCompletionClient` (which uses `chat.completions.create`), replace it with `OpenAIChatClient`.

| Before | After |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

To check your version: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc releases)

In pre-1.0.0 MAF, `OpenAIChatClient` used Chat Completions. Upgrade to `agent-framework-openai>=1.0.0` where `OpenAIChatClient` uses the Responses API by default.

No other changes needed — the `Agent` and tool APIs remain the same.

### LangChain (`langchain-openai`)

Add `use_responses_api=True` to `ChatOpenAI()`. Also update response access from `.content` to `.text`.

| Before | After |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

For complete before/after code examples, see [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontend Migration Guidance

> **The Responses API is a server-side concern.** Migrate your Python backend; the frontend's HTTP contract should stay unchanged unless your backend is a thin pass-through — in that case, consider adopting the Responses request shape to eliminate a translation layer. If the frontend calls OpenAI directly with a client-side key, move those calls to a backend first.

### `@microsoft/ai-chat-protocol` deprecation

The `@microsoft/ai-chat-protocol` npm package is deprecated and should be replaced with [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). If you encounter it in a frontend:

1. Replace the CDN script tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Remove the `AIChatProtocolClient` instantiation (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Replace `client.getStreamedCompletion(messages)` with a direct `fetch()` call to the backend streaming endpoint.
4. Replace `for await (const response of result)` with `for await (const chunk of readNDJSONStream(response.body))`.
5. Update property access from `response.delta.content` / `response.error` to `chunk.delta.content` / `chunk.error`.

---

## Goals

- Enumerate all Python call sites using Chat Completions or legacy Completions against Azure OpenAI.
- Propose a migration plan and sequencing for the Python codebase.
- Apply safe, minimal edits to switch to Responses API.
- Update callers to consume the Responses output schema; no backcompat wrappers.
- Run tests/lints; fix trivial breakages introduced by the migration.
- Prepare small, reviewable change sets and provide a final summary with diffs (do not commit).

---

## Guardrails

- Only modify files inside the git workspace. Never write outside.
- Do not preserve backward-compatibility shims; migrate code to the new API shape.
- Do not leave tombstone/transition comments or backup files.
- Preserve streaming semantics if previously used; otherwise use non-streaming.
- Ask for approval before running commands or network calls if in approval mode.
- Do not run `git add`/`git commit`/`git push`; produce working-tree edits only.

---

## Step 0: Azure OpenAI Client Migration (Prerequisite)

If the codebase uses `AzureOpenAI` or `AsyncAzureOpenAI` constructors, migrate to the standard `OpenAI` / `AsyncOpenAI` constructors first. The Azure-specific constructors are deprecated in `openai>=1.108.1`.

### Why the v1 API path?

The new `/openai/v1` endpoint uses the standard `OpenAI()` client instead of `AzureOpenAI()`, requires no `api_version` parameter, and works identically across OpenAI and Azure OpenAI. The same client code is future-proof — no version management needed.

### Key changes

| Before | After |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Remove entirely |

### Cleanup checklist

- Remove `api_version` argument from client construction.
- Remove `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` environment variables from `.env`, app settings, and Bicep/infra files.
- Rename `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` in `.env`, app settings, Bicep/infra, and test fixtures (standard Azure Identity SDK convention).
- Ensure `openai>=1.108.1` in `requirements.txt` or `pyproject.toml`.

### Environment variable migration

| Old env var | Action | Notes |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Remove** | No `api_version` needed with v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Remove** | Same as above |
| `AZURE_OPENAI_CLIENT_ID` | **Rename** → `AZURE_CLIENT_ID` | Standard Azure Identity SDK convention for `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Keep** | Still needed for `base_url` construction |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Keep** | Used as `model` param in `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Keep** | Used as `api_key` for key-based auth |

For client setup code examples (sync, async, EntraID, API key, multi-tenant), see [cheat-sheet.md](./references/cheat-sheet.md).

---

## Step 1: Detect Legacy Call Sites

Run the [detect_legacy.py](./scripts/detect_legacy.py) script to find all call sites that need migration:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Or run these searches manually — every match is a migration target:

```bash
# Legacy API calls (must rewrite)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Deprecated Azure client constructors (must replace)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Response shape access patterns (must update)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Tool definitions in old nested format (must flatten)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Tool results in old format (must convert to function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Deprecated parameters (must remove or rename)
rg "response_format"
rg "max_tokens\b"        # rename to max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Deprecated env vars (clean up)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # should be AZURE_CLIENT_ID

# GitHub Models endpoints (must remove — Responses API not supported)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Framework-level legacy patterns (must update)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: replace with OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: needs use_responses_api=True

# Test infrastructure (must update)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Content filter error body access (must update — structure changed)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # old singular form — now content_filter_results (plural) inside content_filters array

# Raw HTTP calls to Chat Completions endpoint (must update URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristics (detect and rewrite)

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

- **Why migrate**: Responses is the unified API for text, tools, and streaming; Chat Completions is legacy. With GPT-5, Responses is required for best performance.
- **HTTP**: Azure endpoint switches from `/openai/deployments/{name}/chat/completions` to `/openai/v1/responses`.
- **Fields**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` remains.
- **Formatting**: `response_format` → `text.format` with a proper object.
- **Content items**: Replace Chat `content[].type: "text"` with Responses `content[].type: "input_text"` for system/user turns.
- **Image content items**: Replace Chat `content[].type: "image_url"` with Responses `content[].type: "input_image"`. Flatten the `image_url` field from `{"image_url": {"url": "..."}}` to `{"image_url": "..."}` (a plain string — either an HTTPS URL or a `data:image/...;base64,...` data URI).

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
| `seed` | **Remove** (not supported) |
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
- Do not rely on previous message IDs or server-stored context; keep state client-managed and minimize metadata.

---

## Acceptance Criteria

### Code-level gates (all must pass)

- [ ] Zero matches for `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` in migrated files.
- [ ] Zero matches for `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — all constructors use `OpenAI`/`AsyncOpenAI` with the v1 endpoint.
- [ ] Zero matches for `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub Models code paths removed.
- [ ] Zero matches for `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ code uses `OpenAIChatClient` (which uses Responses API). In pre-1.0.0, upgrade to `agent-framework-openai>=1.0.0`.
- [ ] All `ChatOpenAI(...)` calls include `use_responses_api=True`.
- [ ] Zero matches for `rg "choices\[0\]"` — all response access uses `resp.output_text` or the Responses output schema.
- [ ] No `response_format` at top level; all structured output uses `text={"format": {...}}`.
- [ ] `openai>=1.108.1` and `azure-identity` in `requirements.txt` or `pyproject.toml`; dependencies reinstalled.
- [ ] `store=False` set on every `responses.create` call.
- [ ] No `api_version` in client construction; `AZURE_OPENAI_API_VERSION` removed from env files and infra.

### Test infrastructure gates (all must pass)

- [ ] Zero matches for `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Zero matches for `rg "_azure_ad_token_provider" tests/` — assertions updated to check `isinstance(client, AsyncOpenAI)` or `base_url`.
- [ ] Zero matches for `rg "prompt_filter_results|content_filter_results" tests/` — Azure-specific filter mocks removed.
- [ ] Mock fixtures use `kwargs.get("input")` not `kwargs.get("messages")`.
- [ ] Snapshot / golden files updated to Responses streaming shape (no `choices[0]`, `function_call`, `logprobs`, etc.).
- [ ] `pytest` passes with zero failures after all test updates.

### Behavioral gates (verify manually or via test harness)

- [ ] **Basic completion**: non-streaming `responses.create` returns non-empty `output_text`.
- [ ] **Stream parity**: if the original code used streaming, the migrated code streams and yields `response.output_text.delta` events with non-empty deltas.
- [ ] **Structured output**: if using `text.format` with `json_schema`, `json.loads(resp.output_text)` succeeds and matches the schema.
- [ ] **Tool-call loop**: if tools are used, the model issues tool calls, the app executes them, and the follow-up request returns a final `output_text` (no infinite loop).
- [ ] **Async parity**: if `AsyncAzureOpenAI` was used, `AsyncOpenAI` equivalent works with `await`.
- [ ] **Error rate**: no new 400/401/404 errors compared to the pre-migration baseline.

### Deliverables

- Summary includes edited files, before/after counts of legacy call sites, and next steps.
- Changes are working-tree edits only (no commits).

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
- [detect_legacy.py — automated scanner](./scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API docs](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses)
