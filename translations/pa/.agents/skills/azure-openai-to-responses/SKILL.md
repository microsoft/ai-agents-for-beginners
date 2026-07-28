---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI ਚੈਟ ਕੰਪਲੀਸ਼ਨਸ ਤੋਂ Responses API ਵਿੱਚ Python ਐਪਸ ਮਾਈਗ੍ਰੇਟ ਕਰੋ

> **ਅਧਿਕਾਰਤ ਮਾਰਗਦਰਸ਼ਨ — ਬਿਲਕੁਲ ਠੀਕ ਅਨੁਸਰਣ ਕਰੋ**
>
> ਇਹ ਸਕਿਲ ਉਹ Python ਕੋਡਬੇਸ ਮਾਈਗ੍ਰੇਟ ਕਰਦਾ ਹੈ ਜੋ Azure OpenAI ਚੈਟ ਕੰਪਲੀਸ਼ਨਸ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ
> Unified Responses API ਵੱਲ। ਇਹ ਨਿਰਦੇਸ਼ਾਂ ਨੂੰ ਬਿਲਕੁਲ ਸੁਚੱਜੇ ਤੌਰ 'ਤੇ ਫਾਲੋ ਕਰੋ।
> ਪੈਰਾਮੀਟਰ ਮੈਪਿੰਗਸ ਚੇਤਰ ਕਰਨ ਜਾਂ API ਸ਼ੇਪ ਵਿਚ ਬਦਲਾਵ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਨਾ ਕਰੋ।

---

## ਟ੍ਰਿਗਰ

ਇਸ ਸਕਿਲ ਨੂੰ ਐਕਟੀਵੇਟ ਕਰੋ ਜਦੋਂ ਯੂਜ਼ਰ ਚਾਹੁੰਦਾ ਹੈ:
- Azure OpenAI ਚੈਟ ਕੰਪਲੀਸ਼ਨਸ ਤੋਂ Responses API ਵੱਲ Python ਐਪ ਮਾਈਗ੍ਰੇਟ ਕਰਨੀ
- Python OpenAI SDK ਵਰਤੋਂ ਨੂੰ Azure OpenAI ਲਈ ਨਵੀਨਤਮ API ਸ਼ੇਪ ਨਾਲ ਅੱਪਗਰੇਡ ਕਰਨਾ
- Python ਕੋਡ ਨੂੰ GPT-5 ਜਾਂ ਵਧੀਕ ਨਵੇਂ ਮਾਡਲਾਂ ਲਈ ਤਿਆਰ ਕਰਨਾ ਜੋ Azure ਉੱਤੇ Responses ਦੀ ਲੋੜ ਰੱਖਦੇ ਹਨ
- `AzureOpenAI`/`AsyncAzureOpenAI` ਤੋਂ ਸਮਾਨv1 ਇੰਡੀਪੌਇਂਟ ਵਾਲੇ ਮਿਆਰੀ `OpenAI`/`AsyncOpenAI` ਕਲਾਇੰਟ ਤੇ ਸਵਿੱਚ ਕਰਨਾ
- `AzureOpenAI` ਕੰਸਟਰਕਟਰ ਜਾਂ `api_version` ਨਾਲ ਜੁੜੀਆਂ ਡੀਪ੍ਰੀਕੇਸ਼ਨ ਚੇਤਾਵਨੀਆਂ ਸਹੀ ਕਰਨਾ

---

## ⚠️ ਮਾਡਲ ਸਮਰਥਨਤਾ — ਪਹਿਲਾਂ ਜਾਂਚੋ

> **ਮਾਈਗ੍ਰੇਸ਼ਨ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡਾ Azure OpenAI ਡਿਪਲੋਇਮੈਂਟ Responses API ਨੂੰ ਸਮਰਥਨ ਕਰਦਾ ਹੈ।**

### 1. ਆਪਣੀ ਡਿਪਲੋਇਮੈਂਟ ਦੀ ਸੁਤੰਤਰ ਜਾਂਚ ਕਰੋ (ਸਭ ਤੋਂ ਤੇਜ਼)

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

> **ਨੋਟ**: `max_output_tokens` ਦੇ Azure OpenAI ਤੇ ਘੱਟੋ-ਘੱਟ 16 ਟੋਕਨ ਲਾਜ਼ਮੀ ਹਨ। 16 ਤੋਂ ਘੱਟ ਮੁੱਲ 400 ਐਰਰ ਵਾਪਸ ਕਰਦਾ ਹੈ। smoke ਟੈਸਟ ਲਈ 50+ ਵਰਤੋ।

ਜੇ ਇਹ 404 ਦਿੰਦਾ ਹੈ, ਤਾ ਡਿਪਲੋਇਮੈਂਟ ਦਾ ਮਾਡਲ ਹੁਣ ਤੱਕ Responses ਦਾ ਸਮਰਥਨ ਨਹੀਂ ਕਰਦਾ — ਹੇਠਾਂ ਦਿੱਤਾ ਰੈਫਰੈਂਸ ਜਾਂਚੋ ਜਾਂ ਸਹਾਇਕ ਮਾਡਲ ਨਾਲ ਮੁੜ ਡਿਪਲੋਇ ਕਰਵਾਓ।

### 2. ਆਪਣੇ ਖੇਤਰ ਵਿੱਚ ਉਪਲੱਬਧ ਮਾਡਲਾਂ ਦੀ ਜਾਂਚ ਕਰੋ (ਸਿਫਾਰਸ਼ੀ)

Responses API ਸਮਰਥਿਤ ਉਪਲੱਬਧਤਾ ਵੇਖਣ ਲਈ ਬਣੀਆ ਮਾਡਲ ਕੰਪੈਟਬਿਲਟੀ ਟੂਲ ਚਲਾਓ:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

ਇਹ Azure ARM ਲਾਈਵ ਨੂੰ ਕੈਵੇਰੀ ਕਰਦਾ ਹੈ ਅਤੇ ਇਕ ਕੰਪੈਟਬਿਲਟੀ ਮੈਟਰਿਕਸ ਦਿਖਾਉਂਦਾ ਹੈ — ਜਿਸ ਤੋਂ ਪਤਾ ਲੱਗدا ਹੈ ਕਿਹੜੇ ਮਾਡਲ Responses, ਸੰਰਚਿਤ آਉਟਪੁੱਟ, ਟੂਲ ਆਦਿ ਸਮਰਥਨ ਕਰਦੇ ਹਨ। ਨਤੀਜੇ ਸੰਕੁਚਿਤ ਕਰਨ ਲਈ `--filter gpt-5.1,gpt-5.2` ਜਾਂ ਸਕ੍ਰਿਪਟਿੰਗ ਲਈ `--json` ਵਰਤੋ।

### 3. ਪੂਰਾ ਮਾਡਲ ਸਮਰਥਨ ਰੈਫਰੈਂਸ

- **ਲਾਈਵ ਕੈਵੇਰੀ**: `python migrate.py models` (ਉੱਤੇ ਵੇਖੋ — ਖੇਤਰ-ਨਿਰਧਾਰਿਤ, ਹਮੇਸ਼ਾ ਤਾਜ਼ਾ)
- **ਉਪਲੱਬਧਤਾ ਵੇਖੋ**: [ਮਾਡਲ ਸਰੰਸ਼ ਟੇਬਲ ਅਤੇ ਖੇਤਰ ਉਪਲੱਬਧਤਾ](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **ਕੁਇਕਸਟਾਰਟ ਅਤੇ ਮਾਰਗਦਰਸ਼ਨ**: **https://aka.ms/openai/start**

### ⚠️ ਪੁਰਾਣੇ ਮਾਡਲ ਸੀਮਾਵਾਂ

> **ਚੇਤਾਵਨੀ**: ਪੁਰਾਣੇ ਮਾਡਲ (ਜੋ `gpt-4.1` ਤੋਂ ਪਹਿਲਾਂ ਦੇ ਹਨ) Responses API ਦੀਆਂ ਸਾਰੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਸਮਰਥਿਤ ਨਹੀਂ ਕਰ ਸਕਦੇ।
>
> ਪੁਰਾਣੇ ਮਾਡਲਾਂ ਨਾਲ ਜਾਣੀਆਂ ਸੀਮਾਵਾਂ:
> - **`reasoning` ਪੈਰਾਮੀਟਰ**: ਬਹੁਤ ਸਾਰੇ ਗੈਰ-ਰੀਜ਼ਨਿੰਗ ਮਾਡਲਾਂ ਤੇ ਸਮਰਥਿਤ ਨਹੀਂ। ਕੇਵਲ ਉਹਨਾਂ ਮਾਡਲਾਂ ਲਈ `reasoning` ਮਾਈਗ੍ਰੇਟ ਕਰੋ ਜੇ ਉਹ ਮੁਢਲੇ ਕੋਡ ਵਿੱਚ ਪਹਿਲਾਂ ਤੋਂ ਮੌਜੂਦ ਸੀ।
> - **`seed` ਪੈਰਾਮੀਟਰ**: Responses API ਵਿੱਚ ਨਹੀਂ ਚੱਲਦਾ — ਸਾਰੇ ਅਨੁਰੋਧਾਂ ਤੋਂ ਹਟਾਓ।
> - **`text.format` ਰਾਹੀਂ ਸੰਰਚਿਤ ਆਉਟਪੁੱਟ**: ਪੁਰਾਣੇ ਮਾਡਲ ਜ਼ਿਆਦਾਤਰ `strict: true` JSON ਸਕੀਮਾਂ ਨੂੰ ਭਰੋਸੇਯੋਗ ਤਰੀਕੇ ਨਾਲ ਲਾਗੂ ਨਹੀਂ ਕਰਦੇ।
> - **ਟੂਲ ਸੰਚਾਲਨ**: GPT-5+ ਅੰਦਰੂਨੀ ਰੀਜ਼ਨਿੰਗ ਹਿੱਸੇ ਵਜੋਂ ਟੂਲ ਕਾਲਾਂ ਦਾ ਆਯੋਜਨ ਕਰਦਾ ਹੈ। Responses ਤੇ ਪੁਰਾਣੇ ਮਾਡਲ ਕੰਮ ਕਰਦੇ ਹਨ ਪਰ ਇਹ ਡੂੰਘਾ ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਨਹੀਂ ਹੈ।
> - **ਤਾਪਮਾਨ ਸੀਮਾਵਾਂ**: `gpt-5` ਲਈ ਮਾਈਗ੍ਰੇਟ ਕਰਦਿਆਂ, ਤਾਪਮਾਨ ਨੂੰ ਛੱਡਣਾ ਜਾਂ 1 ਸੈੱਟ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ। ਪੁਰਾਣੇ ਮਾਡਲਾਂ ਉੱਤੇ ਕੋਈ ਐਸਾ ਨਿਯੰਤਰਣ ਨਹੀਂ।

### O-ਸੀਰੀਜ਼ ਰੀਜ਼ਨਿੰਗ ਮਾਡਲ (o1, o3-mini, o3, o4-mini)

O-ਸੀਰੀਜ਼ ਮਾਡਲਾਂ ਦੇ ਖਾਸ ਪੈਰਾਮੀਟਰ ਸੀਮਾਵਾਂ ਹਨ। ਐਸੇ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੀ ਮਾਈਗ੍ਰੇਸ਼ਨ ਕਰਦਿਆਂ ਜੋ ਐਸੇ ਮਾਡਲਾਂ ਨੂੰ ਨਿਯਤ ਕਰਦੀਆਂ ਹਨ:

- **`temperature`**: `1` ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ (ਜਾਂ ਛੱਡ ਦੇਣਾ). O-ਸੀਰੀਜ਼ ਮਾਡਲ ਹੋਰ ਮੁੱਲ ਕਬੂਲ ਨਹੀਂ ਕਰਦੇ।
- **`max_completion_tokens` → `max_output_tokens`**: Azure ਖਾਸ `max_completion_tokens` ਵਰਤ ਰਹੇ ਐਪ ਨੂੰ `max_output_tokens` 'ਤੇ ਸਵਿੱਚ ਕਰਨਾ ਲਾਜ਼ਮੀ। ਉੱਚੀ ਕੀਮਤ (4096+) ਸੈੱਟ ਕਰੋ ਕਿਉਂਕਿ reasoning ਟੋਕਨ ਹੱਦ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੇ ਹਨ।
- **`reasoning_effort`**: ਜੇ ਐਪ `reasoning_effort` (low/medium/high) ਵਰਤਦਾ ਹੈ, ਤਾਂ ਇਹ ਰੱਖੋ — Responses API ਇਸ ਪੈਰਾਮੀਟਰ ਨੂੰ o-ਸੀਰੀਜ਼ ਮਾਡਲਾਂ ਲਈ ਸਮਰਥਨ ਕਰਦਾ ਹੈ।
- **ਸਟ੍ਰੀਮਿੰਗ ਵਿਹਾਰ**: O-ਸੀਰੀਜ਼ ਮਾਡਲ ਰੀਜ਼ਨਿੰਗ ਸਮਾਪਤ ਹੋਣ ਤੱਕ ਆਉਟਪੁੱਟ ਨੂੰ ਬਫਰ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਫਿਰ ਟੈਕਸਟ ਡੈਲਟਾ ਇਵੈਂਟਸ ਜਾਰੀ ਕਰਦੇ ਹਨ। ਸਟ੍ਰੀਮਿੰਗ ਚੱਲਦੀ ਰਹਿੰਦੀ ਹੈ, ਪਰ ਪਹਿਲਾ `response.output_text.delta` GPT ਮਾਡਲਾਂ ਨਾਲੋਂ ਲੰਮੀ ਦੇਰੀ ਨਾਲ ਆ ਸਕਦਾ ਹੈ।
- **`top_p`**: O-ਸੀਰੀਜ਼ 'ਤੇ ਸਮਰਥਿਤ ਨਹੀਂ — ਜੇ ਮੌਜੂਦ ਹੈ ਤਾਂ ਹਟਾਓ।
- **ਟੂਲ ਵਰਤੋਂ**: O-ਸੀਰੀਜ਼ ਮਾਡਲ Responses API ਰਾਹੀਂ ਟੂਲਾਂ ਨੂੰ GPT ਮਾਡਲਾਂ ਵਾਂਗ ਸਮਰਥਨ ਕਰਦੇ ਹਨ, ਪਰ ਟੂਲ ਕਾਲ ਆਯੋਜਨ ਗੁਣਵੱਤਾ ਮਾਡਲ ਦੁਆਰਾ ਵੱਖਰੀ ਹੁੰਦੀ ਹੈ।

**ਕਿਰਿਆ — ਤਤਕਾਲ ਮਾਡਲ ਸਲਾਹ**: ਸਕੈਨ ਫੇਜ਼ ਵਿਚ ਜਾਂਚ ਕਰੋ ਕਿ ਐਪ ਕਿਹੜੇ ਮਾਡਲ ਨੂੰ ਨਿਸ਼ਾਨਾ ਬਣਾਉਂਦਾ ਹੈ (ਡਿਪਲੋਇਮੈਂਟ ਨਾਂ, env ਵਰ, ਕੰਫਿਗ)। ਜੇ ਮਾਡਲ `gpt-4.1` ਤੋਂ ਪਹਿਲਾਂ ਦਾ ਹੈ (gpt-4.1+ ਨਹੀਂ), ਜਾਂਚਕਾਰ ਨੂੰ ਬਤਾਓ:
- ਮਾਈਗ੍ਰੇਸ਼ਨ ਉਨ੍ਹਾਂ ਦੇ ਮੌਜੂਦਾ ਮਾਡਲ ਉੱਤੇ ਬੁਨਿਆਦੀ ਟੈਕਸਟ, ਚੈਟ, ਸਟ੍ਰੀਮਿੰਗ ਅਤੇ ਟੂਲਾਂ ਲਈ ਕੰਮ ਕਰੇਗੀ।
- ਨਵੇਂ ਮਾਡਲ (`gpt-5.1`, `gpt-5.2`) ਬਿਹਤਰ ਟੂਲ ਆਯੋਜਨ, ਸੰਰਚਿਤ ਆਉਟਪੁੱਟ ਲਾਗੂ ਕਰਨ, reasoning, ਅਤੇ ਖੇਤਰਾਂ ਵਿਚ ਲਭਾਉਂ ਦਾ ਆਫ਼ਰ ਕਰਦੇ ਹਨ।
- ਉਹ ਆਪਣੀ ਡਿਪਲੋਇਮੈਂਟ ਅੱਪਗਰੇਡ ਕਰਨ 'ਤੇ ਵਿਚਾਰ ਕਰਨ — ਇਹ ਮਾਈਗ੍ਰੇਸ਼ਨ ਵਿੱਚ ਰੁਕਾਵਟ ਨਹੀਂ ਪੈਂਦਾ।

ਮਾਡਲ ਵਰਜ਼ਨ ਦੇ ਆਧਾਰ ਤੇ ਮਾਈਗ੍ਰੇਟ ਕਰਨ ਤੋਂ ਮਨ ਨਾ ਕਰੋ ਜਾਂ ਰੋਕੋ। ਸਲਾਹ ਜਾਣਕਾਰੀ ਲਈ ਹੈ।

### GitHub ਮਾਡਲ Responses API ਨੂੰ ਸਮਰਥਿਤ ਨਹੀਂ ਕਰਦੇ

> **GitHub ਮਾਡਲ (`models.github.ai`, `models.inference.ai.azure.com`) Responses API ਨੂੰ ਸਮਰਥਿਤ ਨਹੀਂ ਕਰਦੇ।**

ਜੇ ਕੋਡਬੇਸ ਵਿੱਚ GitHub ਮਾਡਲ ਕੋਡ ਰਾਹ ਹੈ (ਜਾਂਚੋ ਕਿ `base_url` `models.github.ai` ਜਾਂ `models.inference.ai.azure.com` ਤੇ ਦਿਸਦਾ ਹੈ), ਮਾਈਗ੍ਰੇਸ਼ਨ ਦੌਰਾਨ ਇਸਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਹਟਾ ਦਿਓ। Responses API ਲਈ Azure OpenAI, OpenAI ਜਾਂ ਮਿਲਦੇ-ਝੁਲਦੇ ਲੋਕਲ ਇੰਡੀਪੌਇੰਟ (ਜਿਵੇਂ Ollama Responses ਸਮਰਥਨ ਨਾਲ) ਲਾਜ਼ਮੀ ਹੈ।

ਸਕੈਨ ਦੌਰਾਨ ਕਿਰਿਆ:
- ਕਿਸੇ ਵੀ GitHub ਮਾਡਲ ਕੋਡ ਰਾਹ ਨੂੰ ਹਟਾਉਣ ਲਈ ਨਿਸ਼ਾਨ ਲਗਾਓ।

---

## ਫਰੇਮਵਰਕ ਮਾਈਗ੍ਰੇਸ਼ਨ

ਬਹੁਤ ਸਾਰੀਆਂ ਐਪਸ OpenAI ਦੇ ਉੱਪਰ ਵਧੇਰੇ ਪੱਧਰੀ ਫਰੇਮਵਰਕ ਵਰਤਦੀਆਂ ਹਨ। ਇਨ੍ਹਾਂ ਦੀ ਮਾਈਗ੍ਰੇਸ਼ਨ ਦੌਰਾਨ ਫਰੇਮਵਰਕ ਦੀ ਆਪਣੀ API ਬਦਲਦੀ ਹੈ — ਸਿਰਫ ਹੀ OpenAI ਕਾਲਾਂ ਨਹੀਂ।

### ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ (MAF)

**ਪਹਿਲਾਂ ਆਪਣੀ MAF ਵਰਜ਼ਨ ਜਾਂਚੋ** — ਮਾਈਗ੍ਰੇਸ਼ਨ ਇਸ ਗੱਲ ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ ਕਿ ਤੁਸੀਂ MAF 1.0.0+ ਜਾਂ 1.0.0 ਤੋਂ ਪੂਰਵ ਬੀਟਾ/ਰਿਲੀਜ਼ ਕੈਂਡਿਡੇਟ ਤੇ ਹੋ।

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ਹਾਲੇ ਹੀ Responses API ਵਰਤਦਾ ਹੈ** — ਕੋਈ ਮਾਈਗ੍ਰੇਸ਼ਨ ਲੋੜੀਂਦਾ ਨਹੀਂ। ਜੇ ਕੋਡਬੇਸ ਪ੍ਰਾਚੀਨ `OpenAIChatCompletionClient` (ਜੋ `chat.completions.create` ਵਰਤਦਾ ਹੈ) ਵਰਤਦਾ ਹੈ, ਤਾ ਇਸ ਨੂੰ `OpenAIChatClient` ਨਾਲ ਬਦਲੋ।

| ਪਹਿਲਾਂ | ਬਾਅਦ |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

ਆਪਣਾ ਵਰਜ਼ਨ ਜਾਂਚਣ ਲਈ: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`  

#### MAF pre-1.0.0 (ਬੀਟਾ/ਰਿਲੀਜ਼ ਕੈਂਡਿਡੇਟ)

pre-1.0.0 MAF ਵਿੱਚ, `OpenAIChatClient` ਚੈਟ ਕੰਪਲੀਸ਼ਨਸ ਵਰਤਦਾ ਸੀ। `agent-framework-openai>=1.0.0` ਵਿੱਚ ਅੱਪਗਰੇਡ ਕਰੋ ਜਿਥੇ `OpenAIChatClient`Responses API ਨੂੰ ਡਿਫਾਲਟ ਵਜੋਂ ਵਰਤਦਾ ਹੈ।

ਹੋਰ ਕੋਈ ਬਦਲਾਅ ਦੀ ਲੋੜ ਨਹੀਂ — `Agent` ਅਤੇ ਟੂਲ API ਇੱਕੋ ਜਿਹੇ ਹੀ ਰਹਿੰਦੇ ਹਨ।

### ਲਾਂਗਚੇਨ (`langchain-openai`)

`ChatOpenAI()` ਵਿੱਚ `use_responses_api=True` ਸ਼ਾਮਲ ਕਰੋ। ਨਾਲ ਹੀ `.content` ਤੋਂ `.text` ਤੱਕ Responses ਐਕਸੈੱਸ ਅਪਡੇਟ ਕਰੋ।

| ਪਹਿਲਾਂ | ਬਾਅਦ |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

ਪੂਰੇ ਪਹਿਲਾਂ/ਬਾਅਦ ਕੋਡ ਉਦਾਹਰਨਾਂ ਲਈ, [cheat-sheet.md](./references/cheat-sheet.md) ਵੇਖੋ।

---

## ਫਰੰਟਐਂਡ ਮਾਈਗ੍ਰੇਸ਼ਨ ਮਾਰਗਦਰਸ਼ਨ

> **Responses API ਸਰਵਰ-ਸਾਈਡ ਮੁੱਦਾ ਹੈ।** ਆਪਣਾ Python ਬੈਕਐਂਡ ਮਾਈਗ੍ਰੇਟ ਕਰੋ; ਫਰੰਟਐਂਡ ਦਾ HTTP ਕਿਰਾਰਦਾਰ ਬਦਲੇ ਬਗੈਰ ਰਹਿਣਾ ਚਾਹੀਦਾ ਹੈ ਜੇਕਰ ਬੈਕਐਂਡ ਇੱਕ ਸੁਤੰਤਰ ਪਾਸ-ਥਰੂ ਨਾ ਹੋਵੇ — उस स्थिति में, Responses ਕੋਲ ਰਿਕਵੇਸਟ ਸ਼ੇਪ ਅਪਣਾਉਣ ਤੇ ਵਿਚਾਰ ਕਰੋ ਤਾਂ ਜੋ ਬਦਲਾਵ ਲੇਅਰ ਹਟਾਈ ਜਾ ਸਕੇ। ਜੇ ਫਰੰਟਐਂਡ ਸਿੱਧਾ OpenAI ਨੂੰ ਕਲੀਐਂਟ-ਸਾਈਡ ਕੀ ਨਾਲ ਕਾਲ ਕਰਦਾ ਹੈ, ਤਾ ਉਹਨਾਂ ਕਾਲਾਂ ਨੂੰ ਪਹਿਲਾਂ ਬੈਕਐਂਡ ਵਿੱਚ ਸਥਾਨਾਂਤਰਿਤ ਕਰੋ।

### `@microsoft/ai-chat-protocol` ਡੀਪ੍ਰੀਕੇਸ਼ਨ

`@microsoft/ai-chat-protocol` npm ਪੈਕੇਜ ਡੀਪ੍ਰੀਕੇਟਡ ਹੈ ਅਤੇ ਇਸ ਨੂੰ [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) ਨਾਲ ਬਦਲਣਾ ਚਾਹੀਦਾ ਹੈ। ਜੇ ਤੁਸੀਂ ਇਸਨੂੰ ਕਿਸੇ ਫਰੰਟਐਂਡ ਵਿੱਚ ਵੇਖਦੇ ਹੋ:

1. CDN ਸਕ੍ਰਿਪਟ ਟੈਗ ਬਦਲੋ:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` ਦੀ ਇੰਸਟੈਂਸੀਏਸ਼ਨ ਹਟਾਓ (`new ChatProtocol.AIChatProtocolClient("/chat")`)।
3. `client.getStreamedCompletion(messages)` ਦੀ ਥਾਂ ਬੈਕਐਂਡ ਸਟ੍ਰੀਮਿੰਗ ਇੰਡੀਪੌਇੰਟ ਲਈ ਸਿੱਧੀ `fetch()` ਕਾਲ ਕਰੋ।
4. `for await (const response of result)` ਨੂੰ `for await (const chunk of readNDJSONStream(response.body))` ਨਾਲ ਬਦਲੋ।
5. ਪ੍ਰਾਪਰਟੀ ਐਕਸੈੱਸ ਨੂੰ `response.delta.content` / `response.error` ਤੋਂ `chunk.delta.content` / `chunk.error` ਵੱਲ ਅਪਡੇਟ ਕਰੋ।

---

## ਲਕਸ਼

- ਸਾਰੇ Python ਕਾਲ ਸਾਈਟਾਂ ਦੀ ਗਿਣਤੀ ਕਰੋ ਜੋ Azure OpenAI ਖਿਲਾਫ਼ ਚੈਟ ਕੰਪਲੀਸ਼ਨਸ ਜਾਂ ਪ੍ਰਾਚੀਨ ਕੰਪਲੀਸ਼ਨਸ ਵਰਤਦੇ ਹਨ।
- Python ਕੋਡਬੇਸ ਲਈ ਮਾਈਗ੍ਰੇਸ਼ਨ ਯੋਜਨਾ ਅਤੇ ਕ੍ਰਮ ਦੇਣ।
- Responses API 'ਤੇ ਸਵਿੱਚ ਕਰਨ ਲਈ ਸੁਰੱਖਿਅਤ, ਘੱਟੋ-ਘੱਟ ਸੋਧਾਂ ਲਾਗੂ ਕਰੋ।
- Responses ਆਉਟਪੁੱਟ ਸਕੀਮਾ ਖਪਤ ਕਰਨ ਲਈ ਕਾਲਰਜ਼ ਨੂੰ ਅਪਡੇਟ ਕਰੋ; ਕੋਈ ਬੈਕਕਾਮਪੈਟ ਰੈਪਰ ਨਹੀਂ।
- ਟੈਸਟ/ਲਿੰਟ ਚਲਾਓ; ਮਾਈਗ੍ਰੇਸ਼ਨ ਨਾਲ ਆਏ ਛੋਟੇ ਤੂਟੇ ਦੁਰੁਸਤ ਕਰੋ।
- ਛੋটা, ਸਮੀਖਿਆ ਯੋਗ ਬਦਲਾਅ ਸੈੱਟ ਤਿਆਰ ਕਰੋ ਅਤੇ ਅੰਤੀਮ ਸਾਰ ਸਣੇ diff ਦਿਓ (ਕਮੇਟ ਨਾ ਕਰੋ)।

---

## ਸੁਰੱਖਿਆ ਨਿਯਮ

- ਸਿਰਫ Git ਵਰਕਸਪੇਸ ਦੇ ਅੰਦਰ ਫਾਈਲਾਂ ਸੋਧੋ। ਕਿੰਨੇ ਵੀ ਬਾਹਰ ਨਾ ਲਿਖੋ।
- ਪਿੱਛਲੇ-ਅਨੁਕੂਲਤਾ ਸਿਮ ਜੋੜੋ ਨਾ; ਕੋਡ ਨੂੰ ਨਵੇਂ API ਸ਼ੇਪ 'ਤੇ ਮਾਈਗ੍ਰੇਟ ਕਰੋ।
- ਕੋਈ ਟੋਮਸਟੋਨ/ਸੰਕਰਮਣ ਕਮੈਂਟ ਜਾਂ ਬੈਕਅੱਪ ਫਾਈਲਾਂ ਨਾ ਛੱਡੋ।
- ਜੇ पहਲਾਂ ਸਟ੍ਰੀਮਿੰਗ ਵਰਤੀ ਗਈ ਹੋਵੇ ਤਾਂ ਸਟ੍ਰੀਮਿੰਗ ਸੈਮੀਟਿਕਸ ਰੱਖੋ; ਨਹੀਂ ਤਾਂ ਗੈਰ-ਸਟ੍ਰੀਮਿੰਗ ਵਰਤੋ।
- ਅਨੁਮਤੀ ਮੋਡ ਵਿੱਚ ਕਮਾਂਡ ਜਾਂ ਨੈੱਟਵਰਕ ਕਾਲਾਂ ਦੌੜਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਮਨਜ਼ੂਰੀ ਲਓ।
- `git add`/`git commit`/`git push` ਨਾ ਚਲਾਓ; ਸਿਰਫ ਵਰਕਿੰਗ-ਟਰੀ ਸੋਧਾਂ ਬਣਾਓ।

---

## ਕਦਮ 0: Azure OpenAI ਕਲਾਇੰਟ ਮਾਈਗ੍ਰੇਸ਼ਨ (ਪ੍ਰਧਾਨ ਸ਼ਰਤ)

ਜੇ ਕੋਡਬੇਸ `AzureOpenAI` ਜਾਂ `AsyncAzureOpenAI` ਕੰਸਟਰਕਟਰ ਵਰਤਦਾ ਹੈ, ਤਾਂ ਪਹਿਲਾਂ ਮਿਆਰੀ `OpenAI` / `AsyncOpenAI` ਕੰਸਟਰਕਟਰ ਵੱਲ ਮਾਈਗ੍ਰੇਟ ਕਰੋ। Azure ਖਾਸ ਕੰਸਟਰਕਟਰ `openai>=1.108.1` ਵਿੱਚ ਡੀਪ੍ਰੀਕੇਟਡ ਹਨ।

### ਵ1 API ਪਥ ਕਿਉਂ?

ਨਵਾਂ `/openai/v1` ਇੰਡੀਪੌਇੰਟ ਮਿਆਰੀ `OpenAI()` ਕਲਾਇੰਟ ਵਰਤਦਾ ਹੈ ਨਾ ਕਿ `AzureOpenAI()`; `api_version` ਪੈਰਾਮੀਟਰ ਦੀ ਲੋੜ ਨਹੀਂ, ਅਤੇ ਇਹ OpenAI ਅਤੇ Azure OpenAI ਦੋਹਾਂ 'ਤੇ ਇਕੋ ਜਿਹਾ ਕੰਮ ਕਰਦਾ ਹੈ। ਇੱਕੋ ਕਲਾਇੰਟ ਕੋਡ ਭਵਿੱਖ-ਸੁਰੱਖਿਅਤ ਹੈ — ਵਰਜਨ ਪ੍ਰਬੰਧਨ ਦੀ ਲੋੜ ਨਹੀਂ।

### ਮੁੱਖ ਬਦਲਾਅ

| ਪਹਿਲਾਂ | ਬਾਅਦ |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | ਪੂਰੀ ਤਰ੍ਹਾਂ ਹਟਾਓ |

### ਸਫਾਈ ਦੀ ਸੂਚੀ

- ਕਲਾਇੰਟ ਕਨਸਟਰਕਸ਼ਨ ਤੋਂ `api_version` ਪੈਰਾਮੀਟਰ ਹਟਾਓ।
- `.env`, ਐਪ ਸੈਟਿੰਗਜ਼, ਅਤੇ Bicep/ਇੰਫਰਾ ਫਾਈਲਾਂ ਵਿੱਚੋਂ `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` ਏਨਵਾਇਰਨਮੈਂਟ ਵੈਰੀਏਬਲ ਹਟਾਓ।
- `.env`, ਐਪ ਸੈਟਿੰਗਜ਼, Bicep/ਇੰਫਰਾ ਅਤੇ ਟੈਸਟ ਫਿਕਸਚਰਜ਼ ਵਿੱਚ `AZURE_OPENAI_CLIENT_ID` ਨੂੰ `AZURE_CLIENT_ID` ਵੱਲ ਰੀਨੇਮ ਕਰੋ (ਸਧਾਰਣ Azure Idendity SDK ਪ੍ਰਣਾਲੀ)।
- `requirements.txt` ਜਾਂ `pyproject.toml` ਵਿੱਚ `openai>=1.108.1` ਯਕੀਨੀ ਬਣਾਓ।

### ਏਨਵਾਇਰਨਮੈਂਟ ਵੈਰੀਏਬਲ ਮਾਈਗ੍ਰੇਸ਼ਨ

| ਪੁਰਾਣਾ env var | ਕਿਰਿਆ | ਨੋਟਸ |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **ਹਟਾਓ** | v1 ਇੰਡੀਪੌਇੰਟ ਨਾਲ `api_version` ਦੀ ਲੋੜ ਨਹੀਂ |
| `AZURE_OPENAI_API_VERSION` | **ਹਟਾਓ** | ਉਪਰੋਕਤ ਵਰਗੀ ਹੀ |
| `AZURE_OPENAI_CLIENT_ID` | **ਰੀਨੇਮ ਕਰੋ** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` ਲਈ ਸਧਾਰਣ Azure Idendity SDK ਪ੍ਰਣਾਲੀ |
| `AZURE_OPENAI_ENDPOINT` | **ਰੱਖੋ** | `base_url` ਬਣਾੳ਼ਣ ਲਈ ਹਾਲੇ ਲੋੜੀਂਦਾ ਹੈ |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **ਰੱਖੋ** | `responses.create` ਵਿੱਚ ਮਾਡਲ ਪੈਰਾਮੀਟਰ ਵਜੋਂ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ |
| `AZURE_OPENAI_API_KEY` | **ਰੱਖੋ** | ਕੁੰਜੀ ਅਧਾਰਿਤ ਪ੍ਰਮਾਣਿਕਤਾ ਲਈ `api_key` ਵਜੋਂ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ |

ਕਲਾਇੰਟ ਸੈਟਅੱਪ ਕੋਡ (ਸਿੰਕ, ਅਸਿੰਕ, EntraID, API ਕੁੰਜੀ, ਮਲਟੀ-ਟੇਨੈਂਟ) ਲਈ ਉਦਾਹਰਨਾਂ [cheat-sheet.md](./references/cheat-sheet.md) ਵਿੱਚ ਹਨ।

---

## ਕਦਮ 1: ਪ੍ਰਾਚੀਨ ਕਾਲ ਸਾਈਟਾਂ ਦੀ ਪਹਿਚਾਣ

ਸਾਰੇ ਕਾਲ ਸਾਈਟਾਂ ਲੱਭਣ ਲਈ [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) ਸਕ੍ਰਿਪਟ ਚਲਾਓ ਜੋ ਮਾਈਗ੍ਰੇਸ਼ਨ ਦੀ ਲੋੜ ਹੈ:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

ਜਾਂ ਇਹ ਖੋਜਾਂ ਮੈਨੂਅਲੀ ਕਰੋ — ਹਰ ਇੱਕ ਮਿਲਾਪ ਇੱਕ ਮਾਈਗ੍ਰੇਸ਼ਨ ਟਾਰਗੇਟ ਹੈ:

```bash
# ਲੈਗਸੀ API ਕਾਲਸ (ਮੁੜ ਲਿਖਣਾ ਲਾਜ਼ਮੀ ਹੈ)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# ਪੁਰਾਣੇ ਹੋ ਚੁੱਕੇ Azure ਕਲਾਇੰਟ ਕੰਸਟ੍ਰਕਟਰ (ਬਦਲਣਾ ਲਾਜ਼ਮੀ ਹੈ)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# ਜਵਾਬ ਆਕਾਰ ਪਹੁੰਚ ਪੈਟਰਨ (ਅੱਪਡੇਟ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# ਪੁਰਾਣੇ ਨੇਸਟਿਡ ਫਾਰਮੈਟ ਵਿੱਚ ਟੂਲ ਪਰਿਭਾਸ਼ਾਵਾਂ (ਫਲੈਟ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# ਪੁਰਾਣੇ ਫਾਰਮੈਟ ਵਿੱਚ ਟੂਲ ਨਤੀਜੇ (function_call_output ਵਿੱਚ ਤਬਦੀਲ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# ਪੁਰਾਣੇ ਹੋ ਚੁੱਕੇ ਪੈਰਾਮੀਟਰ (ਹਟਾਉਣਾ ਜਾਂ ਨਾਂ ਬਦਲਣਾ ਲਾਜ਼ਮੀ ਹੈ)
rg "response_format"
rg "max_tokens\b"        # ਨਾਂ ਬਦਲ ਕੇ max_output_tokens ਕਰੋ
rg "['\"]seed['\"]"      # remove entirely

# ਪੁਰਾਣੇ ਹੋ ਚੁੱਕੇ env ਵੈਰੀਅਬਲ (ਸਾਫ਼ ਕਰੋ)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ

# GitHub ਮਾਡਲ ਐਂਡਪോയਿੰਟ (ਹਟਾਉਣਾ ਲਾਜ਼ਮੀ - Responses API ਸਮਰਥਿਤ ਨਹੀਂ ਹੈ)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# ਫਰੇਮਵਰਕ-ਸਤਹ ਦੇ ਲੈਗਸੀ ਪੈਟਰਨ (ਅੱਪਡੇਟ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient ਨਾਲ ਤਬਦਿਲ ਕਰੋ
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True ਦੀ ਲੋੜ ਹੈ

# ਟੈਸਟ ਢਾਂਚਾ (ਅੱਪਡੇਟ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# ਸਮੱਗਰੀ ਫਿਲਟਰ ਦੀ ਗਲਤੀ ਬਾਡੀ ਪਹੁੰਚ (ਅੱਪਡੇਟ ਕਰਨਾ ਲਾਜ਼ਮੀ - ਢਾਂਚਾ ਬਦਲ ਗਿਆ ਹੈ)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # ਪੁਰਾਣਾ ਇਕਵਚਨ ਰੂਪ - ਹੁਣ content_filter_results (ਬਹੁਵਚਨ) content_filters ਅਰੇ ਦੇ ਅੰਦਰ ਹੈ

# Chat Completions ਐਂਡਪോയਿੰਟ ਨੂੰ ਰਾ HTTP ਕਾਲ (URL ਅੱਪਡੇਟ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### ਸੰਕੇਤਕ (ਪਤਾ ਲਗਾਓ ਅਤੇ ਦੁਬਾਰਾ ਲਿਖੋ)

- **ਚੈਟ ਕੰਪਲੀਸ਼ਨਸ ਕਲਾਇੰਟ**: `client.chat.completions.create` → `client.responses.create(...)`।

- **ਐਜ਼ਰ ਕਲਾਇੰਟ ਨਿਰਮਾਤਾ**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **ਟੂਲਜ਼**: ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਟੂਲ ਪਰਿਭਾਸ਼ਾਵਾਂ ਨੂੰ ਨੇਸਟਡ ਫਾਰਮੈਟ (`{"type": "function", "function": {"name": ...}}`) ਤੋਂ ਫਲੈਟ Responses ਫਾਰਮੈਟ (`{"type": "function", "name": ...}`) ਵਿੱਚ ਬਦਲੋ; `tool_choice` ਵਰਤੋ; ਟੂਲ ਨਤੀਜੇ `{"type": "function_call_output", "call_id": ..., "output": ...}` ਆਈਟਮਾਂ ਵਜੋਂ ਵਾਪਸ ਕਰੋ (ਨਾ ਕਿ `{"role": "tool", ...}`).
- **ਟੂਲ ਰਾਊਂਡ-ਟ੍ਰਿਪਸ**: ਜਦੋਂ ਮਾਡਲ ਫੰਕਸ਼ਨ ਕਾਲ ਵਾਪਸ ਕਰਦਾ ਹੈ, ਤਾਂ ਗੱਲਬਾਤ ਵਿੱਚ `response.output` ਆਈਟਮ ਸ਼ਾਮਿਲ ਕਰੋ (ਹੱਥੋਂ ਬਣਾਈ ਗਈ `{"role": "assistant", "tool_calls": [...]}` ਡਿਕਸ਼ਨਰੀ ਨਾ ਪਾਓ), ਫਿਰ ਹਰ ਨਤੀਜੇ ਲਈ `function_call_output` ਆਈਟਮ ਜੋੜੋ।
- **ਕੁਝ-ਸ਼ਟ ਟੂਲ ਉਦਾਹਰਨਾਂ**: ਜੇ ਗੱਲਬਾਤ ਵਿੱਚ ਹਾਰਡਕੋਡ ਕੀਤੇ ਟੂਲ ਕਾਲ ਉਦਾਹਰਨ ਸ਼ਾਮਿਲ ਹਨ, ਤਾਂ ਉਨ੍ਹਾਂ ਨੂੰ `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` ਆਈਟਮਾਂ ਵਿੱਚ ਬਦਲੋ। IDs ਨੂੰ `fc_` ਨਾਲ ਸ਼ੁਰੂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।
- **`pydantic_function_tool()`**: ਇਹ ਹੈਲਪਰ ਅਜੇ ਵੀ ਪੁਰਾਣੇ ਨੇਸਟਡ ਫਾਰਮੈਟ ਨੂੰ ਜਨਰੇਟ ਕਰਦਾ ਹੈ ਅਤੇ `responses.create()` ਨਾਲ **ਸਮਰਥਕ ਨਹੀਂ** ਹੈ। ਨੂੰ ਮੈਨੂਅਲ ਟੂਲ ਪਰਿਭਾਸ਼ਾਵਾਂ ਜਾਂ ਫਲੈਟਨਿੰਗ ਰੈਪਰੇ ਨਾਲ ਬਦਲੋ।
- **ਮਲਟੀ-ਟਰਨ**: ਐਪ ਵਿੱਚ ਗੱਲਬਾਤ ਇਤਿਹਾਸ ਨੂੰ ਬਣਾਈ ਰੱਖੋ; ਪਹਿਲਾਂ ਦੇ ਟਰਨ `input` ਆਈਟਮਾਂ ਰਾਹੀਂ ਪਾਸ ਕਰੋ।
- **ਫਾਰਮੈਟਿੰਗ**: Chat ਦੇ ਟੌਪ-ਲੇਵਲ `response_format` ਨੂੰ Responses ਵਿੱਚ `text.format` ਨਾਲ ਬਦਲੋ। ਕੈਨਾਨੀਕਲ ਆਕਾਰ: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **ਸਮੱਗਰੀ ਆਈਟਮ**: Chat ਦੇ `content[].type: "text"` ਨੂੰ Responses ਦੇ `content[].type: "input_text"` ਨਾਲ ਬਦਲੋ ਜਦੋਂ ਵਰਤੋਂਕਾਰ/ਸਿਸਟਮ ਟਰਨ ਹੋਣ।
- **ਚਿੱਤਰ ਸਮੱਗਰੀ ਆਈਟਮ**: Chat ਦੇ `content[].type: "image_url"` ਨੂੰ Responses ਦੇ `content[].type: "input_image"` ਨਾਲ ਬਦਲੋ। `image_url` ਫੀਲਡ ਨੇਸਟਡ ਓਬਜੈਕਟ `{"url": "..."}` ਤੋਂ ਫਲੈਟ ਸਟਰਿੰਗ ਵਿੱਚ ਬਦਲ ਜਾਂਦਾ ਹੈ। ਪਹਿਲਾਂ/ਬਾਅਦ ਦੇ ਉਦਾਹਰਨਾਂ ਲਈ ਚੀਟ ਸ਼ੀਟ ਵੇਖੋ।
- **ਸੋਚ-ਵਿਚਾਰ ਯਤਨ**: **ਸਿਰਫ਼ ਜੇ ਪਹਿਲਾਂ ਹੀ ਮੂਲ ਕੋਡ ਵਿੱਚ `reasoning` ਮੌਜੂਦ ਹੈ ਤਾਂ ਹੀ ਇਸ ਨੂੰ ਮਾਈਗਰੇਟ ਕਰੋ**।
- **ਸਮੱਗਰੀ ਫਿਲਟਰ ਤਰੁੱਟੀ ਹੈਂਡਲਿੰਗ**: ਤਰੁੱਟੀ ਬਾਡੀ ਢਾਂਚਾ ਬਦਲ ਗਿਆ ਹੈ। Chat Completions ਨੇ `error.body["innererror"]["content_filter_result"]` (ਇਕਵਚਨ) ਵਰਤਿਆ; Responses API `error.body["content_filters"][0]["content_filter_results"]` (ਬਹੁਵਚਨ, ਇੱਕ ਐਰੇ ਵਿੱਚ) ਵਰਤਦਾ ਹੈ। ਜੋ ਕੋਡ `innererror` ਤੱਕ ਪਹੁੰਚਦਾ ਹੈ, ਉਹ `KeyError` ਦੇਵਗਾ। ਨਵਾਂ ਰਾਸ਼ਤਾ ਵਰਤਣ ਲਈ ਦੁਬਾਰਾ ਲਿਖੋ।
- **ਕੱਚੇ HTTP ਕਾਲਜ਼**: ਜੇ ਐਪ Azure OpenAI REST API ਨੂੰ ਸਿੱਧਾ `/openai/deployments/{name}/chat/completions?api-version=...` ਵਰਤ ਕੇ ਕਾਲ ਕਰਦੀ ਹੈ, ਤਾਂ ਇਸਨੂੰ `/openai/v1/responses` ਵਿੱਚ ਬਦਲੋ। ਬੇਨਤੀ ਬਾਡੀ ਬਦਲਦੀ ਹੈ: `messages` → `input`, `max_output_tokens` ਜੋੜੋ ਅਤੇ `store: false` ਜੋੜੋ, `api-version` ਕ੍ਵੈਰੀ ਪੈਰਾਮ ਹਟਾਓ। ਜਵਾਬ ਬਾਡੀ ਬਦਲਦੀ ਹੈ: `choices[0].message.content` → `output[0].content[0].text` (ਨੋਟ: `output_text` ਇੱਕ SDK ਸਹੂਲਤ ਪ੍ਰਾਪਰਟੀ ਹੈ ਜੋ ਕੱਚੇ REST JSON ਵਿੱਚ ਨਹੀਂ ਹੁੰਦੀ)।

---

## ਕਦਮ 2: ਮਾਈਗ੍ਰੇਸ਼ਨ ਲਾਗੂ ਕਰੋ

### ਮਾਈਗ੍ਰੇਸ਼ਨ ਨੋਟਸ (Chat Completions → Responses)

- **ਕਿਉਂ ਮਾਈਗ੍ਰੇਟ ਕਰਨਾ**: Responses ਪਾਠ, ਟੂਲਜ਼ ਅਤੇ ਸਟ੍ਰੀਮਿੰਗ ਲਈ ਇਕੱਤਰ API ਹੈ; Chat Completions ਪੁਰਾਣਾ ਹੈ। GPT-5 ਦੇ ਨਾਲ, Responses ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ ਲਈ ਜ਼ਰੂਰੀ ਹੈ।
- **HTTP**: ਐਜ਼ਰ ਏਂਡਪੌਇੰਟ `/openai/deployments/{name}/chat/completions` ਤੋਂ `/openai/v1/responses` 'ਤੇ ਬਦਲਦਾ ਹੈ।
- **ਫੀਲਡਜ਼**: `messages` → `input`, `max_tokens` → `max_output_tokens`। `temperature` ਜਿਵੇਂ ਦਾ ਤਿਵੇਂ ਹੈ।
- **ਫਾਰਮੈਟਿੰਗ**: `response_format` → `text.format` ਇਕ ਢੰਗ ਦਾ ਆਬਜੈਕਟ।
- **ਸਮੱਗਰੀ ਆਈਟਮ**: Chat ਦੇ `content[].type: "text"` ਨੂੰ Responses ਦੇ `content[].type: "input_text"` ਨਾਲ ਬਦਲੋ ਜਦੋਂ ਸਿਸਟਮ/ਉਪਭੋਗਤਾ ਟਰਨ ਹੋਣ।
- **ਚਿੱਤਰ ਸਮੱਗਰੀ ਆਈਟਮ**: Chat ਦੇ `content[].type: "image_url"` ਨੂੰ Responses ਦੇ `content[].type: "input_image"` ਨਾਲ ਬਦਲੋ। `image_url` ਫੀਲਡ ਨੂੰ `{"image_url": {"url": "..."}}` ਤੋਂ `{"image_url": "..."}` (ਸਧਾਰਣ ਸਟਰਿੰਗ — https URL ਜਾਂ `data:image/...;base64,...` ਡੇਟਾ ਯੂਆਰਆਈ) ਵਿੱਚ ਫਲੈਟ ਕਰੋ।

### ਪੈਰਾਮੀਟਰ ਮੇਪਿੰਗ ਰੇਫਰੰਸ

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (ਆਈਟਮਾਂ ਦਾ ਐਰੇ) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (ਆਬਜੈਕਟ) |
| `temperature` | `temperature` (ਬਦਲਾਅ ਬਿਨਾਂ) |
| `stop` | `stop` (ਬਦਲਾਅ ਬਿਨਾਂ) |
| `frequency_penalty` | `frequency_penalty` (ਬਦਲਾਅ ਬਿਨਾਂ) |
| `presence_penalty` | `presence_penalty` (ਬਦਲਾਅ ਬਿਨਾਂ) |
| `tools` / function-calling | `tools` (ਬਦਲਾਅ ਬਿਨਾਂ) |
| `seed` | **ਹਟਾਓ** (ਸਮਰਥਿਤ ਨਹੀਂ) |
| `store` | `store` (`false` ਤੇ ਸੈਟ) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (ਫਲੈਟ ਸਟਰਿੰਗ) |

ਪੂਰੇ ਪਹਿਲਾਂ/ਬਾਅਦ ਕੋਡ ਉਦਾਹਰਨਾਂ ਲਈ, [cheat-sheet.md](./references/cheat-sheet.md) ਵੇਖੋ।

ਟੈਸਟ ਢਾਂਚਾ ਮਾਈਗ੍ਰੇਸ਼ਨ (ਮਾਕ, ਸਨੈਪਸ਼ਾਟ, ਦਾਵੇ) ਲਈ [test-migration.md](./references/test-migration.md) ਵੇਖੋ।

ਤਰੁੱਟੀਆਂ ਅਤੇ ਗੋਚਾਸ਼ ਲਈ [troubleshooting.md](./references/troubleshooting.md) ਵੇਖੋ।

---

## ਡੇਟਾ ਰੀਟੈਂਸ਼ਨ ਅਤੇ ਸਥਿਤੀ

- ਸਾਰੀਆਂ Responses ਬੇਨਤੀਆਂ ਤੇ `store: false` ਸੈਟ ਕਰੋ।
- ਪਿਛਲੇ ਸੁਨੇਹੇ IDs ਜਾਂ ਸਰਵਰ-ਸਟੋਰ ਕੀਤੀ ਸੰਦਰਭ ਤੇ ਨਿਰਭਰ ਨਾ ਕਰੋ; ਰਾਜ ਕਲਾਇੰਟ-ਪ੍ਰਬੰਧਿਤ ਰੱਖੋ ਅਤੇ ਮੈਟਾਡੇਟਾ ਘਟਾਓ।

---

## ਸੁਵੀਕਾਰਤਾ ਮਾਪਦੰਡ

### ਕੋਡ-ਸਤਰੀ ਦਰਵਾਜੇ (ਸਾਰੇ ਪਾਸ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ)

- [ ] `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` ਲਈ ਮਾਈਗ੍ਰੇਟ ਕੀਤੇ ਫਾਇਲਾਂ ਵਿੱਚ ਜ਼ੀਰੋ ਮੇਲ।
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` ਲਈ ਜ਼ੀਰੋ ਮੇਲ — ਸਾਰੇ ਨਿਰਮਾਤਾ `OpenAI`/`AsyncOpenAI` ਵਰਤਦੇ ਹਨ v1 ਏਂਡਪੌਇੰਟ ਨਾਲ।
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` ਲਈ ਜ਼ੀਰੋ ਮੇਲ — GitHub ਮਾਡਲ ਕੋਡ ਰਾਹ ਹਟਾਏ ਗਏ।
- [ ] `rg "OpenAIChatCompletionClient"` ਲਈ ਜ਼ੀਰੋ ਮੇਲ — MAF 1.0.0+ ਕੋਡ `OpenAIChatClient` ਵਰਤਦਾ ਹੈ (ਜੋ Responses API ਵਰਤਦਾ ਹੈ)। ਪਹਿਲਾਂ ਦੇ ਵਰਜਨ ਵਿੱਚ, `agent-framework-openai>=1.0.0` ਤੱਕ ਅਪਗ੍ਰੇਡ ਕਰੋ।
- [ ] ਸਾਰੇ `ChatOpenAI(...)` ਕਾਲ `use_responses_api=True` ਸ਼ਾਮਿਲ ਕਰਦੇ ਹਨ।
- [ ] `rg "choices\[0\]"` ਲਈ ਜ਼ੀਰੋ ਮੇਲ — ਸਾਰਾ ਜਵਾਬ `resp.output_text` ਜਾਂ Responses ਆਉਟਪੁੱਟ schema ਵਰਤਦਾ ਹੈ।
- [ ] ਉੱਪਰਲੇ ਪੱਧਰ 'ਤੇ ਕੋਈ `response_format` ਨਹੀਂ; ਸਾਰਾ ਸੰਰਚਿਤ ਨਤੀਜਾ `text={"format": {...}}` ਵਰਤਦਾ ਹੈ।
- [ ] `openai>=1.108.1` ਅਤੇ `azure-identity` ਨੂੰ `requirements.txt` ਜਾਂ `pyproject.toml` ਵਿੱਚ ਸ਼ਾਮਿਲ ਕੀਤਾ ਅਤੇ ਡਿਪੇਂਡੈਂਸੀਜ਼ ਦੁਬਾਰਾ ਇੰਸਟਾਲ ਕੀਤੀਆਂ।
- [ ] ਹਰ `responses.create` ਕਾਲ 'ਤੇ `store=False` ਸੈਟ ਕੀਤਾ।
- [ ] ਕਲਾਇੰਟ ਨਿਰਮਾਣ ਵਿੱਚ ਕੋਈ `api_version` ਨਹੀਂ; `AZURE_OPENAI_API_VERSION` ਨੂੰ env ਫਾਇਲਾਂ ਅਤੇ ਇੰਫਰਾ ਤੋਂ ਹਟਾਇਆ ਗਿਆ।

### ਟੈਸਟ ਢਾਂਚਾ ਦਰਵਾਜੇ (ਸਾਰੇ ਪਾਸ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` ਲਈ ਜ਼ੀਰੋ ਮੇਲ।
- [ ] `rg "_azure_ad_token_provider" tests/` ਲਈ ਜ਼ੀਰੋ ਮੇਲ — ਦਾਅਵੇ ਨਵੀਨ ਕੀਤੇ ਗਏ ਹਨ ਤਾਂ ਜੋ ਜਾਂਚ ਹੋਵੇ `isinstance(client, AsyncOpenAI)` ਜਾਂ `base_url`।
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` ਲਈ ਜ਼ੀਰੋ ਮੇਲ — Azure-ਵਿਸ਼ੇਸ਼ ਫਿਲਟਰ ਮਾਕ ਹਟਾਏ ਗਏ।
- [ ] ਮੌਕ ਫਿਕਸਚਰਜ਼ ਵਿੱਚ `kwargs.get("input")` ਵਰਤਿਆ ਗਿਆ ਹੈ ਨਾ ਕਿ `kwargs.get("messages")`।
- [ ] ਸਨੈਪਸ਼ਾਟ / ਗੋਲਡਨ ਫਾਇਲਾਂ Responses ਸਟ੍ਰੀਮਿੰਗ ਆਕਾਰ ਲਈ ਅਪਡੇਟ ਕੀਤੀਆਂ (ਕੋਈ `choices[0]`, `function_call`, `logprobs` ਆਦਿ ਨਹੀਂ)।
- [ ] ਸਾਰੇ ਟੈਸਟ ਅਪਡੇਟਾਂ ਤੋਂ ਬਾਅਦ `pytest` ਕਿਸੇ ਵੀ ਫੇਲਿਊਰ ਦੇ ਬਿਨਾਂ ਪਾਸ ਹੁੰਦਾ ਹੈ।

### ਵਿਹਾਰਕ ਦਰਵਾਜੇ (ਮੈਨੂਅਲ ਜਾਂ ਟੈਸਟ ਹਰਨੇਸ ਰਾਹੀਂ ਸੱਚਿਤ ਕਰੋ)

- [ ] **ਮੂਲ ਸਪੂਰਨਤਾ**: ਨਾਨ-ਸਟ੍ਰੀਮਿੰਗ `responses.create` ਖਾਲੀ ਨਾ ਹੋਣ ਵਾਲਾ `output_text` ਵਾਪਸ ਕਰਦਾ ਹੈ।
- [ ] **ਸਟ੍ਰੀਮ ਗੁਣਵੱਤਾ**: ਜੇ ਮੂਲ ਕੋਡ ਸਟ੍ਰੀਮਿੰਗ ਵਰਤਦਾ ਸੀ, ਤਾਂ ਮਾਈਗ੍ਰੇਟ ਕੀਤਾ ਕੋਡ ਸਟ੍ਰੀਮ ਕਰਦਾ ਹੈ ਅਤੇ ਕੋਡੈਲਟਸ ਨਾਲ `response.output_text.delta` ਘਟਨਾਵਾਂ ਦਿੰਦਾ ਹੈ।
- [ ] **ਸੰਰਚਿਤ ਆਉਟਪੁੱਟ**: ਜੇ `text.format` `json_schema` ਨਾਲ ਵਰਤ ਰਿਹਾ ਹੈ, ਤਾਂ `json.loads(resp.output_text)` ਕਾਮਯਾਬ ਹੁੰਦਾ ਹੈ ਅਤੇ ਸਕੀਮਾ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ।
- [ ] **ਟੂਲ-ਕਾਲ ਲੂਪ**: ਜੇ ਟੂਲ ਵਰਤੇ ਜਾਂਦੇ ਹਨ, ਤਾਂ ਮਾਡਲ ਟੂਲ ਕਾਲ ਜਾਰੀ ਕਰਦਾ ਹੈ, ਐਪ ਉਹਨਾਂ ਨੂੰ ਚਲਾਉਂਦਾ ਹੈ, ਅਤੇ ਫਾਲੋ-ਅਪ ਬੇਨਤੀ ਅੰਤਿਮ `output_text` ਵਾਪਸ ਕਰਦੀ ਹੈ (ਅਨੰਤ ਲੂਪ ਨਹੀਂ)।
- [ ] **ਐਸਿੰਕ ਗੁਣਵੱਤਾ**: ਜੇ `AsyncAzureOpenAI` ਵਰਤਿਆ ਗਿਆ ਸੀ, ਤਾਂ `AsyncOpenAI` ਸਮਕਾਲੀ `await` ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ।
- [ ] **ਤਰੁੱਟੀ ਦਰ**: ਮਾਈਗ੍ਰੇਸ਼ਨ ਤੋਂ ਪਹਿਲਾਂ ਦੇ ਮੂਲ ਦਰਜੇ ਨਾਲੋਂ ਕੋਈ ਇੱਕ 400/401/404 ਤਰੁੱਟੀ ਨਹੀਂ ਆਈ।

### ਡਿਲਿਵਰੇਬਲਜ਼

- ਸੰਖੇਪ ਵਿੱਚ ਸੋਧੇ ਹੋਏ ਫਾਇਲਾਂ, ਲੇਗਸੀ ਕਾਲ ਸਾਈਟਾਂ ਦੀ ਗਿਣਤੀ ਪਹਿਲਾਂ/ਬਾਅਦ, ਅਤੇ ਅਗਲੇ ਕਦਮ ਸ਼ਾਮਿਲ ਹਨ।
- ਬਦਲਾਅ ਕੰਮ ਕਰ ਰਹੇ ਟ੍ਰੀ ਸੋਧ ਹਨ (ਕੋਈ ਕਮੇਟ ਨਹੀਂ)।

---

## SDK ਵਰਜਨ ਦੀਆਂ ਜ਼ਰੂਰਤਾਂ

| ਪੈਕੇਜ | ਘੱਟੋ-ਘੱਟ ਵਰਜਨ |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | ਤਾਜ਼ਾ (EntraID ਅਥੇਂਟੀਕੇਸ਼ਨ ਲਈ) |

---

## ਹਵਾਲੇ

- [ਚੀਟ ਸ਼ੀਟ — ਸਾਰੇ ਕੋਡ ਸਨਿੱਪੇਟ](./references/cheat-sheet.md)
- [ਟੈਸਟ ਮਾਈਗ੍ਰੇਸ਼ਨ — ਮਾਕ, ਸਨੈਪਸ਼ਾਟ, ਦਾਵੇ](./references/test-migration.md)
- [ਤਰੁੱਟੀ ਸੰਭਾਲ — ਤਰੁੱਟੀਆਂ, ਖਤਰਾ ਟੇਬਲ, ਗੋਚਾਸ਼](./references/troubleshooting.md)
- [detect_legacy.py — ਸੁਆਰੰਭਿਕ ਸਕੈਨਰ](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI ਸਟਾਰਟਰ ਕਿਟ](https://aka.ms/openai/start)
- [Azure OpenAI Responses API ਡੌਕਸ](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API ਵਰਜਨ ਲਾਈਫਸਾਈਕਲ](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API ਸੰਦਰਭ](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->