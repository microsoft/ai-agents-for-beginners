---
name: azure-openai-to-responses
license: MIT
---
# Python ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು Azure OpenAI ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳಿಂದ Responses API ಗೆ ಸ್ಥಳಾಂತರಿಸಿ

> **ಅಧಿಕೃತ ಮಾರ್ಗದರ್ಶನ — ನಿಖರವಾಗಿ ಅನುಸರಿಸಿ**
>
> ಈ ಕೌಶಲ್ಯವು Python ಕೋಡ್ಬೇಸ್ಗಳನ್ನು Azure OpenAI ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳಿಂದ
> ಏಕೀಕೃತ Responses API ಗೆ ಸ್ಥಳಾಂತರಿಸುತ್ತದೆ. ಈ ಅನುಸರಿಸಿ ನಿಯಮಗಳನ್ನು ನಿಖರವಾಗಿ.
> ಪರಿಮಾಣ ನಕ್ಷೆಗಳನ್ನೂ ಅಥವಾ API ಆಕಾರಗಳನ್ನು ಕಲ್ಪಿಸಬೇಡಿ.

---

## ಪ್ರೇರಣಾಕಾರಕರು

ಬಳಕೆದಾರರು ಕೆಳಗಿನವರಾಗಿದ್ದಾಗ ಈ ಕೌಶಲ್ಯವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ:
- Python ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು Azure OpenAI ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳಿಂದ Responses API ಗೆ ಸ್ಥಳಾಂತರಿಸಿ
- Python OpenAI SDK ಬಳಕೆ ಹೊಸತಾದ API ಆಕಾರಕ್ಕೆ ಅಪ್ಗ್ರೇಡ್ ಮಾಡುವುದು Azure OpenAI ವಿರುದ್ಧ
- Python ಕೋಡ್ ಅನ್ನು GPT-5 ಅಥವಾ ಹೆಚ್ಚಿನ ಮಾದರಿಗಳಿಗೆ Responses API ಬಳಕೆಗಾಗಿ ಸಿದ್ಧಪಡಿಸಿ Azure ನಲ್ಲಿ
- `AzureOpenAI`/`AsyncAzureOpenAI` ನಿಂದ ವಿ1ಎಂಡ್ ಪಾಯಿಂಟ್ ಹೊಂದಿರುವ ಸಾಮಾನ್ಯ `OpenAI`/`AsyncOpenAI` ಕ್ಲೈಯಿಂಟ್‌ಗೆ ಬದಲಾವಣೆಮಾಡಿ
- `AzureOpenAI` ಕಾಂಸ್ಟ್ರಕ್ಟರ್‌ಗಳು ಅಥವಾ `api_version` ನೊಂದಿಗೆ ಸಂಬಂಧಪಟ್ಟ ಅಗತ್ಯಾಚರಣೆ ಎಚ್ಚರಿಕೆಗಳನ್ನು ಸರಿಪಡಿಸಿ

---

## ⚠️ ಮಾದರಿ ಹೊಂದಿಕೆಯಾಗುವಿಕೆ — ಮೊದಲು ಪರಿಶೀಲಿಸಿ

> **ಸ್ಥಳಾಂತರಿಸುವ ಮೊದಲು ನಿಮ್ಮ Azure OpenAI ನಿಯೋಜನೆ Responses API ನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ ಎಂದು ಪರಿಶೀಲಿಸಿ.**

### 1. ನಿಮ್ಮ ನಿಯೋಜನೆಯನ್ನು ವೇಗವಾಗಿ ಪರೀಕ್ಷಿಸಿ (ಶ್ರೇಷ್ಟ)

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

> **ಟಿಪ್ಪಣಿ**: Azure OpenAI ನಲ್ಲಿ `max_output_tokens` ಕನಿಷ್ಟ 16 ಇದೆ. 16 ಕೆಳಗಿನ ಮೌಲ್ಯಗಳು 400 ದೋಷವನ್ನು ಕೊಡುತ್ತವೆ. ತಪಾಸಣೆಗಾಗಿ 50+ ಬಳಸಿರಿ.

ಇದು 404 ಕೆಳಗೌರವ ನೀಡಿದರೆ, ನಿಯೋಜನೆಯ ಮಾದರಿ Responses ನ್ನು ಇನ್ನೂ ಬೆಂಬಲಿಸುವುದಿಲ್ಲ — ಕೆಳಗಿನ ರೆಫರೆನ್ಸ್ ವೀಕ್ಷಿಸಿ ಅಥವಾ ಬೆಂಬಲಿತ ಮಾದರಿಯನ್ನು ಮರುನಿಯೋಜಿಸಿ.

### 2. ನಿಮ್ಮ ಪ್ರದೇಶದಲ್ಲಿ ಲಭ್ಯವಿರುವ ಮಾದರಿಗಳನ್ನು ಪರಿಶೀಲಿಸಿ (ಅನುಕೂಲಕರ)

Responses API ಬೆಂಬಲದೊಂದಿಗೆ ನಿಮ್ಮ ವಿಶೇಷ ಪ್ರದೇಶದಲ್ಲಿ ಲಭ್ಯವಿರುವ ಮಾದರಿಗಳನ್ನು ನೋಡಲು ಒಳಗೊಂಡ ಮಾದರಿ ಹೊಂದಿಕೆಯಾಗುವಿಕೆ ಯಂತ್ರವನ್ನು ಚಾಲನೆಮಾಡಿ:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

ಇದು Azure ARM ನ್ನು ನೇರವಾಗಿ ವಿಚಾರಿಸಿ ಹೊಂದಿಕೆಯಾಗುವಿಕೆ ಮ್ಯಾಟ್ರಿಕ್ಸ್ ತೋರಿಸುತ್ತದೆ — ಯಾವ ಮಾದರಿಗಳು Responses, ರಚನೆಯಾದ output, ಉಪಕರಣ ಮತ್ತು ಇತರವನ್ನೂ ಬೆಂಬಲಿಸುತ್ತವೆ. ಫಲಿತಾಂಶಗಳನ್ನು ಸಂಕೀರ್ಣಗೊಳಿಸಲು `--filter gpt-5.1,gpt-5.2` ಬಳಸಬಹುದು ಅಥವಾ ಬರಹಿಗಾಗಿ `--json` ಬಳಸಿ.

### 3. ಸಂಪೂರ್ಣ ಮಾದರಿ ಬೆಂಬಲ ಸಂಧಾನಿಕೆ

- **ನೇರ ವಿಚಾರಣೆ**: `python migrate.py models` (ಮೇಲಿನಂತೆ — ಪ್ರದೇಶ-ನಿರ್ದಿಷ್ಟ, ಸದಾ ನವೀಕೃತ)
- **ಲಭ್ಯತೆಯನ್ನು ನೋಡಿರಿ**: [ಮಾದರಿ ಸಾರಾಂಶವೂ ಹಾಗೂ ಪ್ರದೇಶ ಲಭ್ಯತೆ](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **ತ್ವರಿತಪ್ರಾರಂಭ ಮತ್ತು ಮಾರ್ಗದರ್ಶನ**: **https://aka.ms/openai/start**

### ⚠️ ಹಳೆಯ ಮಾದರಿಗಳ ನಿರ್ಬಂಧಗಳು

> **ಎಚ್ಚರಿಕೆ**: ಹಳೆಯ ಮಾದರಿಗಳು (ಉದಾ: `gpt-4o`, `gpt-4`) Responses API ಎಲ್ಲಾ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಪೂರ್ಣವಾಗಿ ಬೆಂಬಲಿಸದಿರಬಹುದು.
>
> ಹಳೆಯ ಮಾದರಿಗಳಲ್ಲಿನ ತಿಳಿದಿರುವ ನಿರ್ಬಂಧಗಳು:
> - **`reasoning` ಪ್ಯಾರಾಮೀಟರ್**: `gpt-4o-mini`, `gpt-4o`, ಮತ್ತು ಬಹಳಷ್ಟು ನಿರ್ಲೇಜಿಕೆ ಮೋಡಲ್ಗಳಲ್ಲಿ ಬೆಂಬಲಿತವಲ್ಲ. ಮೂಲ ಕೋಡ್ ಈಗಾಗಲೇ ಹೊಂದಿದ್ದಲ್ಲಿ ಮಾತ್ರ `reasoning` ನ್ನು ಸ್ಥಳಾಂತರಿಸಿ.
> - **`seed` ಪ್ಯಾರಾಮೀಟರ್**: Responses API ನಲ್ಲಿ ಬೆಂಬಲಿಸಲ್ಪಡುವುದಿಲ್ಲ — ಎಲ್ಲಾ ವಿನಂತಿಗಳಿಂದ ತೆಗೆದುಹಾಕಿ.
> - **`text.format` ಮೂಲಕ ರಚನೆಯಾದ output**: ಹಳೆಯ ಮಾದರಿಗಳು JSON ಸ್ಕೀಮಾಗಳಲ್ಲಿ `strict: true` ವಿಧಾನದ ಮೇಲೆ ನಂಬಿಕೆಯಾಗದೆ ಇರಬಹುದು.
> - **ಉಪಕರಣ ಸಂಯೋಜನೆ**: GPT-5+ ಒಳಗಿನ ನಿರ್ಲೇಜಿಕೆಯಲ್ಲಿ ಉಪಕರಣ ಕರೆಗೆ ಯೋಜನೆ ಮಾಡುತ್ತದೆ. ಹಳೆಯ ಮಾದರಿಗಳು Responses ನಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತವೆ ಆದರೆ ಆ ಗಾಢ ಸಂಯೋಜನೆ ಇಲ್ಲ.
> - **ತಾಪಮಾನ ನಿರ್ಬಂಧಗಳು**: `gpt-5` ಗೆ ಸ್ಥಳಾಂತರಿಸುವಾಗ ತಾಪಮಾನ ಮೌಲ್ಯವನ್ನು ಹೊರತುಪಡಿಸಬೇಕು ಅಥವಾ `1` ಗಾಗಿ ನಿಗದಿಪಡಿಸಬೇಕು. ಹಳೆಯ ಮಾದರಿಗಳಿಗೆ ಇಂತಹ ನಿರ್ಬಂಧ ಇಲ್ಲ.

### O-ಸಿರೀಸ್ ನಿರ್ಲೇಜಿಕೆ ಮಾದರಿಗಳು (o1, o3-mini, o3, o4-mini)

O-ಸಿರೀಸ್ ಮಾದರಿಗಳಿಗೆ ವಿಶೇಷ ಪ್ಯಾರಾಮೀಟರ್ ನಿರ್ಬಂಧಗಳಿವೆ. O-ಸಿರೀಸ್ ಮಾದರಿಗಳನ್ನು ಗುರಿಯಾಗಿಸಿಕೊಂಡ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ಸ್ಥಳಾಂತರಿಸುವಾಗ:

- **`temperature`**: ಅದು `1` ಆಗಿರಬೇಕು (ಅಥವಾ ಸದರಿ). O-ಸಿರೀಸ್ ಮೂರಿಗಳು ಇತರ ಮೌಲ್ಯಗಳನ್ನು ಅಂಗೀಕರಿಸುವುದಿಲ್ಲ.
- **`max_completion_tokens` → `max_output_tokens`**: Azure-ನಿರ್ದಿಷ್ಟ `max_completion_tokens` ಬಳಕೆದಾರ ಅಪ್ಲಿಕೇಶನ್ ಗಳು ಈಗ ಹಿಯೋಮಾಡಿ `max_output_tokens` ಗೆ ಬದಲಾಯಿಸಬೇಕು. reasoning tokens ಲಿಮಿಟ್‌ ವಿರುದ್ಧವಿದ್ದು, ಹೆಚ್ಚಿನ ಮೌಲ್ಯಗಳನ್ನು (4096+) ನಿಗದಿ ಮಾಡಿರಿ.
- **`reasoning_effort`**: ಅಪ್ಲಿಕೇಶನ್ `reasoning_effort` (ತಗ್ಗು/ಮಧ್ಯಮ/ಹೆಚ್ಚು) ಬಳಸುತ್ತಿದ್ದರೆ, ಉಳಿಸಿ — Responses API ಇದನ್ನು o-ಸಿರೀಸ್ ಮಾದರಿಗಳಿಗಾಗಿ ಬೆಂಬಳಿಸುತ್ತದೆ.
- **ಸ್ಟ್ರೀಮಿಂಗ್ ವರ್ತನೆ**: O-ಸಿರೀಸ್ ಮಾದರಿಗಳು reasoning ಪೂರ್ಣಗೊಳ್ಳುವವರೆಗೆ output ಬಫರ್ ಮಾಡಬಹುದು ಆದಾಗ್ಯೂ ಸ್ಟ್ರೀಮಿಂಗ್ ಅಮಲು ಮಾಡುತ್ತದೆ, ಆದರೆ ಮೊದಲ `response.output_text.delta` GPT ಮಾದರಿಗಳಿಗಿಂತ ಹೆಚ್ಚು ಸಮಯ ತೆಗೆದುಕೊಳ್ಳಬಹುದು.
- **`top_p`**: O-ಸಿರೀಸ್ ನಲ್ಲಿ ಬೆಂಬಲಿಸಲ್ಪಡುವುದಿಲ್ಲ — ಇದ್ದರೆ ತೆಗೆದುಹಾಕಿ.
- **ಉಪಕರಣ ಬಳಕೆ**: O-ಸಿರೀಸ್ ಮಾದರಿಗಳು Responses API ಮೂಲಕ ಉಪಕರಣಗಳನ್ನು GPT ಮಾದರಿಗಳಂತೆ ಬೆಂಬಲಿಸುತ್ತವೆ, ಆದರೆ ಉಪಕರಣ ಕರೆ ಯೋಜನೆಯ ಗುಣಮಟ್ಟ ಮಾದರಿ ಬಗ್ಗೆ ವ್ಯತ್ಯಾಸ ಇದೆ.

**ಕ್ರಿಯೆ — ವ್ಯಾಪಕ ಮಾದರಿ ಸಲಹೆ**: ಸ್ಕ್ಯಾನ್ ಹಂತದಲ್ಲಿ ಅಪ್ಲಿಕೇಶನ್ ಗುರಿಯಾಗಿಸಿರುವ ಮಾದರಿಯನ್ನು ಪರಿಶೀಲಿಸಿ (ನಿಯೋಜನೆ ಹೆಸರಿಗಳು, ಪರಿಸರ ಚರಗಳು, ಸಂರಚನೆ). ಮಾದರಿ `gpt-4o` ಅಥವಾ ಹಳೆಯದಾದರೆ (gpt-4.1+ ಅಲ್ಲ) ಬಳಕೆದಾರರಿಗೆ ಮುಂಚಿತವಾಗಿ ತಿಳಿಸಿ:
- ಸ್ಥಳಾಂತರಣೆ ಅಸ್ಥಾಯಿಯಾಗಿ ಪಠ್ಯ, ಚಾಟ್, ಸ್ಟ್ರೀಮಿಂಗ್, ಮತ್ತು ಉಪಕರಣಗಳಿಗೆ ಅವರ ಪ್ರಸ್ತುತ ಮಾದರಿಯಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತದೆ.
- ಹಳೆಯ ಮಾದರಿಗಿಂತ `gpt-5.1`, `gpt-5.2` ಹೊಸ ಮಾದರಿಗಳು ಉತ್ತಮ ಉಪಕರಣ ಸಂಯೋಜನೆ, ರಚನೆಯಾದ output ಅನುಷ್ಠಾನ, reasoning ಹಾಗೂ ಪ್ರादेशಿಕ ಲಭ್ಯತೆ ಹೊಂದಿವೆ.
- ಅಗತ್ಯವಿದ್ದರೆ ನಿಯೋಜನೆಯನ್ನು ಅಪ್ಗ್ರೇಡ್ ಮಾಡಲು ಪರಿಗಣಿಸಬೇಕು — ಇದು ಸ್ಥಳಾಂತರಣೆಯಲ್ಲಿ ಅಡ್ಡಿ ಅಲ್ಲ.

ಮಾದರಿ ಆವೃತ್ತಿಯ ಆಧಾರದ ಮೇಲೆ ಸ್ಥಳಾಂತರಣೆಯನ್ನು ತಡೆಹಿಡಿಯಬೇಡಿ ಅಥವಾ ನಿರಾಕರಿಸಬೇಡಿ. ಸಲಹೆ ಮಾಹಿತಿಮೂಲಕವು ಮಾತ್ರ.

### GitHub ಮಾದರಿಗಳು Responses API ಬೆಂಬಲಿಸುವುದಿಲ್ಲ

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) Responses API ನ್ನು ಬೆಂಬಲಿಸುವುದಿಲ್ಲ.**

ಕೋಡ್‌ಬೇಸ್‌ನಲ್ಲಿ GitHub Models ಕೋಡ್ ಪಾತ್ (ಉದಾ: `base_url` `models.github.ai` ಅಥವಾ `models.inference.ai.azure.com` ಗೆ ಸೂಚಿಸುವದಾದರೆ), **ಸ್ಥಳಾಂತರಿಸುವಾಗ ಅದನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ತೆಗೆದುಹಾಕಿ**. Responses API ಪ್ರಮಾಣಿತವಾಗಿ Azure OpenAI, OpenAI ಅಥವಾ ಅನುಕೂಲಕರ ಸ್ಥಳೀಯ ಎಂಡ್‌ಪಾಯಿಂಟ್ (ಉದಾ: Responses ಬೆಂಬಲಿಸುವ Ollama) ಅನ್ನು ಅಗತ್ಯವಿರುತ್ತದೆ.

ಸ್ಕ್ಯಾನ್ ವೇಳೆ ಕಾರಿ:
- GitHub Models ಕೋಡ್ ಪಾತ್‌ಗಳನ್ನು ತೊರೆದಂತಾಗಿ ಗುರುತಿಸಿ.

---

## ಫ್ರೇಮ್‌ವರ್ಕ್ ಸ್ಥಳಾಂತರಣೆ

ಅನೇಕ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು OpenAI ಮೇಲಿನ ಮೇಲ್ದರ್ಜೆಯ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳನ್ನು ಬಳಸುತ್ತವೆ. ಅವುಗಳನ್ನು ಸ್ಥಳಾಂತರಿಸುವಾಗ, ಫ್ರೇಮ್‌ವರ್ಕ್ ಅದೇನೂ ಆಧಾರಿತ OpenAI ಕರೆಗಳಲ್ಲ; ಫ್ರೇಮ್‌ವರ್ಕ್ ಸಾಫ್ಟ್‌ವೇರ್‌ನದೇ API ಬದಲಾವಣೆ ಮಾಡಬೇಕು.

### Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ (MAF)

**ನೀವು MAF ಆವೃತ್ತಿ ಮೊದಲು ಪರಿಶೀಲಿಸಿ** — ನೀವು MAF 1.0.0+ ಅಥವಾ 1.0.0 ಹಿಂದಿನ ಬೇಟಾ/ಆರ್‌ಸಿ ಆವೃತ್ತಿಯಲ್ಲಿದ್ದೀರಿ ಎಂದು ಅವಲಂಬಿಸಿರುತ್ತದೆ.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ಈಗಾಗಲೇ Responses API ಬಳಕೆಮಾಡುತ್ತಿದೆ** — ಸ್ಥಳಾಂತರಣೆಯ ಅಗತ್ಯವಿಲ್ಲ. Legacy `OpenAIChatCompletionClient` (ಅದು `chat.completions.create` ಬಳಸುತ್ತದೆ) ಇದ್ದರೆ, ಅದನ್ನು `OpenAIChatClient` ಆಗಿ ಬದಲಾಯಿಸಿ.

| ಹಿಂದಿನದು | ನಂತರದದು |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

ನಿಮ್ಮ ಆವೃತ್ತಿಯನ್ನು ಪರಿಶೀಲಿಸಲು: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"` 

#### MAF pre-1.0.0 (ಬೇಟಾ/ಆರ್‌ಸಿ ಬಿಡುಗಡೆಗಳು)

pre-1.0.0 MAF ನಲ್ಲಿ, `OpenAIChatClient` ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳನ್ನು ಬಳಸುತ್ತಿತ್ತು. `agent-framework-openai>=1.0.0` ಗೆ ಅಪ್ಗ್ರೇಡ್ ಮಾಡಿ; ಇಲ್ಲಿ `OpenAIChatClient` Responses API ಅಡಿಯಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ.

ಇತರೆ ಬದಲಾವಣೆಗಳ ಅಗತ್ಯವಿಲ್ಲ — `Agent` ಮತ್ತು ಉಪಕರಣ API ಗಳು ಅದೇನೂ ಇರುತ್ತವೆ.

### LangChain (`langchain-openai`)

`ChatOpenAI()` ಗೆ `use_responses_api=True` ಸೇರಿಸಿ. ಪ್ರತಿಕ್ರಿಯೆ ಪ್ರವೇಶವನ್ನು `.content` ಇಂದ `.text` ಗೆ ಬದಲಾಯಿಸಿ.

| ಹಿಂದಿನದು | ನಂತರದದು |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

ಪೂರ್ಣ ಹಿಂದಿನ/ನಂತರದ ಕೋಡ್ ಉದಾಹರಣೆಗಾಗಿ, [cheat-sheet.md](./references/cheat-sheet.md) ನೋಡಿ.

---

## ಮುಂಭಾಗದ ಸ್ಥಳಾಂತರ ಮಾರ್ಗದರ್ಶನ

> **Responses API серверಪ್ಪಕ್ಕ ಸಂಬಂಧಿಸಿದ ವಿಚಾರವಾಗಿದೆ.** ನಿಮ್ಮ Python ಬ್ಯಾಕೆಂಡ್ನ್ನು ಸ್ಥಳಾಂತರಿಸಿ; ಮುಂಭಾಗದ HTTP ಒಪ್ಪಂದವು ಬದಲಿಯಬೇಕು ಎಂದುಿಲ್ಲ, ನಿಮ್ಮ ಬ್ಯಾಕೆಂಡ್ ತೂಕದಿಲ್ಲದ ಪಾಸ್-ಥ್ರೂ ಆಗಿದ್ದರೆ Responses ವಿನಂತಿ ಆಕಾರವನ್ನು ಅಂಗೀಕರಿಸುವ ಬಗ್ಗೆ ಪರಿಗಣಿಸಿ. ಮುಂಭಾಗ OpenAI ನೇರವಾಗಿ ಕ್ಲೈಯಿಂಟ್-ಪಾಸ್ವರ್ಡ್‌ಗಳೊಂದಿಗೆ ಕರೆಸಿದಲ್ಲಿ, ಮೊದಲು ಬ್ಯಾಕೆಂಡ್ ಗೆ ಕರೆ ಮಾಡಿ.

### `@microsoft/ai-chat-protocol` ವಿಲುಪ್ತತೆ

`@microsoft/ai-chat-protocol` npm ಪ್ಯಾಕೇಜ್ ವಿಲುಪ್ತವಾಗಿದೆ, ಅದನ್ನು [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) ನೊಂದಿಗೆ ಬದಲಾಯಿಸಬೇಕು. ಮುಂಭಾಗದಲ್ಲಿ ಇದ್ದರೆ:

1. CDN ಸ್ಕ್ರಿಪ್ಟ್ ಟ್ಯಾಗ್ ಬದಲಾಯಿಸಿ:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` ಸ್ಥಾಪನೆಯನ್ನು ತೆಗೆದುಹಾಕಿ (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. `client.getStreamedCompletion(messages)` ಅನ್ನು ನೇರ `fetch()` ಬ್ಯಾಕೆಂಡ್ ಸ್ಟ್ರೀಮಿಂಗ್ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗೆ ಬದಲಾಯಿಸಿ.
4. `for await (const response of result)` ನ್ನು `for await (const chunk of readNDJSONStream(response.body))` ಗೆ ಬದಲಾಯಿಸಿ.
5. `response.delta.content` / `response.error` ನಿಂದ `chunk.delta.content` / `chunk.error` ಗೆ ಗುಣಲಕ್ಷಣ ಪ್ರವೇಶವನ್ನು ನವೀಕರಿಸಿ.

---

## ಗುರಿಗಳು

- Azure OpenAI ವಿರುದ್ಧ ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ ಅಥವಾ legacy ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳನ್ನು ಬಳಸುವ ಎಲ್ಲಾ Python ಕರೆ ಸ್ಥಳಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ.
- Python ಕೋಡ್ಬೇಸ್ ನ ಸ್ಥಳಾಂತರ ಪ್ಲಾನ್ ಮತ್ತು ಕ್ರಮವನ್ನು ಸೂಚಿಸಿ.
- Responses API ಗೆ ಬದಲಾಯಿಸಲು ಸುರಕ್ಷಿತ, ಕನಿಷ್ಠ ಸಂಪಾದನೆಗಳನ್ನು ಅನುಸರಿಸಿ.
- Responses output ಸ್ರ್ಕಿಮಾ ಬಳಸಲು ಕರೆಕೋರಿಗಳನ್ನು ನವೀಕರಿಸಿ; ಹಿಂದೆಹೋಗುವ ಅನುವುಳಿಕೆ ವ್ರಾಪ್‌ಪರ್‌ಗಳನ್ನು ಬಳಸಬೇಡಿ.
- ಪರೀಕ್ಷೆಗಳು/ಲಿಂಟ್ಸ್ ಚಾಲನೆ ಮಾಡಿ; ಸ್ಥಳಾಂತರದಿಂದಂಟಾದ ಸೂಕ್ಷ್ಮ ದೋಷಗಳನ್ನು ಸರಿಪಡಿಸಿ.
- ಸಣ್ಣ ಬದಲಾವಣೆಗಳ ಸಂಗ್ರಹಗಳನ್ನು ಸಿದ್ಧಪಡಿಸಿ ಮತ್ತು ಅಂತರಗಳನ್ನುಸಹ ತುದಿಗೊಟ್ಟು ಸಾರಾಂಶ ನೀಡಿ (ಕಮಿಟ್ ಮಾಡಬೇಡಿ).

---

## ರಕ್ಷಣೆ ನಿಯಮಗಳು

- ಗಿಟ್ ವರ್ಕ್‌ಸ್ಪೇಸ್ ಒಳಗಿನ ಫೈಲ್‌ಗಳನ್ನಷ್ಟೇ ಬದಲಿಸಿ. ಬಾಹ್ಯ ಪ್ರದೇಶದಲ್ಲಿ ಬರೆಯಬೇಡಿ.
- ಹಿಂದಿನ ಬದಲಾವಣೆಗಳು ಉಳಿಸಬೇಡಿ; ಕೋಡ್ ನವೀನ API ಆಕಾರಕ್ಕೆ ಸ್ಥಳಾಂತರಿಸಿ.
- ಟುಂಬ್‌ಸ್ಟೋನ್/ಸ್ಥಳಾಂತರ ಟಿಪ್ಪಣಿಗಳು ಅಥವಾ ಬ್ಯಾಕಪ್ ಫೈಲ್‌ಗಳನ್ನು ಬಿಟ್ಟುಬಿಡಬೇಡಿ.
- ಮೊದಲು ಬಳಕೆಯಾದಲ್ಲಿ ಸ್ಟ್ರೀಮಿಂಗ್ ವ್ಯವಹಾರವನ್ನು ಕಾಪಾಡಿ; ಇಲ್ಲದಿದ್ದರೆ ಅ-ಸ್ಟ್ರೀಮಿಂಗ್ ಉಪವಿಧಾನ ಬಳಸಿರಿ.
- ಅನುಮೋದನ ಮೋಡ್‌ನಲ್ಲಿದ್ದರೆ, ಆಜ್ಞೆಗಳ ತಂಡಕ್ಕೆ ಮೊದಲು ಅನುಮತಿ ಕೇಳಿ.
- `git add`/`git commit`/`git push` ಚಾಲನೆ ಮಾಡಬೇಡಿ; ಕೆಲಸ ನಿರ್ವಹಿಸುವ ಮರೆಯನ್ನು ಮಾತ್ರ ನೀಡಿರಿ.

---

## ಹಂತ 0: Azure OpenAI ಕ್ಲೈಯಿಂಟ್ ಸ್ಥಳಾಂತರಣೆ (ಅಗತ್ಯವು)

ಕೋಡ್ಬೇಸ್ ನಲ್ಲಿ `AzureOpenAI` ಅಥವಾ `AsyncAzureOpenAI` ಕಾಂಸ್ಟ್ರಕ್ಟರ್ ಗಳನ್ನು ಬಳಸಿದರೆ, ಮೊದಲು ಸಾಮಾನ್ಯ `OpenAI` / `AsyncOpenAI` ಕಾಂಸ್ಟ್ರಕ್ಟರ್ ಗಳಿಗೆ ಸ್ಥಳಾಂತರಿಸು. `openai>=1.108.1` ನಲ್ಲಿ Azure-ನಿರ್ದಿಷ್ಟ ಕಾಂಸ್ಟ್ರಕ್ಟರ್‌ಗಳು ವಿಲುಪ್ತಗೊಂಡಿವೆ.

### ಏಕೆ v1 API ಮಾರ್ಗ?

ಹೊಸ `/openai/v1` ಎಂಡ್‌ಪಾಯಿಂಟ್ ಸಾಮಾನ್ಯ `OpenAI()` ಕ್ಲೈಯಿಂಟ್ ಬಳಸುತ್ತದೆ `AzureOpenAI()` ಬದಲಿಗೆ, `api_version` ಪ್ಯಾರಾಮೀಟರ್ ಅಗತ್ಯವಿಲ್ಲ, ಮತ್ತು OpenAI ಹಾಗೂ Azure OpenAI ಎರಡೂ ಸಮಾನವಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತದೆ. ಇದೇ ಕ್ಲೈಯಿಂಟ್ ಕೋಡ್ ಭವಿಷ್ಯ-ರಕ್ಷಿತ — ಆವೃತ್ತಿ ನಿರ್ವಹಣೆ ಅಗತ್ಯವಿಲ್ಲ.

### ಪ್ರಮುಖ ಬದಲಾವಣೆಗಳು

| ಹಿಂದಿನದು | ನಂತರದದು |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | ಸಂಪೂರ್ಣ ತೆಗೆಯಿರಿ |

### ಶುದ್ಧೀಕರಣ ಪರಿಶೀಲನಾ ಪಟ್ಟಿ

- ಕ್ಲೈಯಿಂಟ್ ರಚನೆಯಿಂದ `api_version` ಪಾತ್ರ ತೆಗೆಯಿರಿ.
- `.env`, ಅಪ್ಲಿಕೇಶನ್ ಸೆಟ್ಟಿಂಗ್ಗಳು ಮತ್ತು Bicep/ಇಂಫ್ರಾ ಫೈಲ್‌ಗಳಿಂದ `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` ಪರಿಸರ ಚರಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.
- `.env`, ಅಪ್ಲಿಕೇಶನ್ ಸೆಟ್ಟಿಂಗ್ಗಳು, Bicep/ಇಂಫ್ರಾ ಮತ್ತು ಪರೀಕ್ಷಾ ಫಿಕ್ಸ್‌ಚರ್‌ಗಳಲ್ಲಿ `AZURE_OPENAI_CLIENT_ID` ನ್ನು `AZURE_CLIENT_ID` ಗೆ ಮರುಹೆಸರಿಸಿ (ತ್ರೈಪುಣಿ Azure Identity SDK ಪದ್ಧತಿ).
- `requirements.txt` ಅಥವಾ `pyproject.toml` ನಲ್ಲಿ `openai>=1.108.1` ನ್ನು ಖಚಿತಪಡಿಸಿ.

### ಪರಿಸರ ಚರ ಸ್ಥಳಾಂತರಣೆ

| ಹಳೆಯ env var | ಕ್ರಮ | ಟಿಪ್ಪಣಿಗಳು |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **ತೆಗೆಯಿರಿ** | v1 ಎಂಡ್‌ಪಾಯಿಂಟ್‌ನಲ್ಲಿ `api_version` ಬೇಕಾಗಿಲ್ಲ |
| `AZURE_OPENAI_API_VERSION` | **ತೆಗೆದುಕೊಳ್ಳಿ** | ಮೇಲಿನಂತೆ |
| `AZURE_OPENAI_CLIENT_ID` | **ಹೆಸರು ಬದಲಿಸಿ** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` ಗೆ ನಿಮಿತ್ತವಾದ ಸರಳ Azure Identity SDK ಪದ್ಧತಿ |
| `AZURE_OPENAI_ENDPOINT` | **ಉಳಿಸು** | `base_url` ರಚನೆಗೆ ಇನ್ನೂ ಬೇಕು |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **ಉಳಿಸು** | `responses.create` ನಲ್ಲಿ `model` ಪ್ಯಾರಾಮೀಟರ್ ಆಗಿ ಬಳಸಲಾಗುತ್ತದೆ |
| `AZURE_OPENAI_API_KEY` | **ಉಳಿಸು** | ಕೀಲಿಗೆ ಆಧಾರಿತ ಪ್ರಾಮಾಣಿಕತೆಗಾಗಿ `api_key` ಆಗಿ ಬಳಸಲಾಗುತ್ತದೆ |

ಕ್ಲೈಯಿಂಟ್ ಸೆಟ್‌ಅಪ್ ಕೋಡ್ ಉದಾಹರಣೆಗಳು (ಸಿಂಕ್, ಆಸಿಂಕ್, EntraID, API ಕೀ, ಮಲ್ಟಿ-ಟೆನಂಟ್)ಗಾಗಿ [cheat-sheet.md](./references/cheat-sheet.md) ನೋಡಿ.

---

## ಹಂತ 1: ಲೆಗಸಿ ಕರೆ ಸ್ಥಳಗಳನ್ನು ಪತ್ತೆಮಾಡಿ

ಸ್ಥಳಾಂತರಣೆಗೆ ಬೇಕಾದ ಎಲ್ಲ ಕರೆ ಸ್ಥಳಗಳನ್ನು ಪತ್ತೆಮಾಡಲು [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) ಸ್ಕ್ರಿಪ್ಟ್ ಅನ್ನು ಓಡಿಸಿ:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

ಅಥವಾ ಈ ಹುಡುಕಾಟಗಳನ್ನು ಕೈಯಿಂದ ಮಾಡಿ — ಪ್ರತಿಯೊಂದು ಹೊಂದಿಕೆ ಸ್ಥಳಾಂತರಣೆಯ ಗುರಿಯಾಗಿದೆ:

```bash
# ಹಳೆಯ API ಕಾಲ್‌ಗಳು (ಮತ್ತೆ ಬರೆಯಬೇಕು)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# ಹಳೆಯ Azure ಕ್ಲೈಂಟ್ ನਿਰ್ಮಾಣಕಾರರು (ಬದಲಾಯಿಸಬೇಕು)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# ಪ್ರತಿಕ್ರಿಯೆ ಸ್ವರೂಪ ಪ್ರವೇಶ نمೂನೆಗಳು (ನವೀಕರಣ ಅಗತ್ಯವಿದೆ)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# ಹಳೆಯ ನೆಸ್ಟೆಡ್ ಸ್ವರೂಪದಲ್ಲಿ tools ವ್ಯಾಖ್ಯಾನಗಳು (ಸರಳಗೊಳಿಸಬೇಕು)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# ಹಳೆಯ ಸ್ವರೂಪದಲ್ಲಿ tool ಫಲಿತಾಂಶಗಳು (function_call_output ಗೆ ಪರಿವರ್ತನೆ ಮಾಡಬೇಕು)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# ಹಳೆಯ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು (ಅಳಿಸಬೇಕು ಅಥವಾ ಮರುನಾಮಕರಣ ಮಾಡಬೇಕು)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens ಎಂದು ಮರುನಾಮಕರಣ ಮಾಡಿ
rg "['\"]seed['\"]"      # remove entirely

# ಹಳೆಯ पर्यावरण 변수ಗಳು (ಶೋಧಿಸಿ ಸ್ವಚ್ಛಗೊಳಿಸಬೇಕು)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID ಆಗಿರಬೇಕು

# GitHub Models ಕಡೆಯಕರೆಗಳ (ಅಳಿಸಬೇಕು — Responses API ಬೆಂಬಲಿಸುವುದಿಲ್ಲ)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# ಫ್ರೇಮ್‌ವರ್ಕ್ ಮಟ್ಟದ ಹಳೆಯ نمೂನೆಗಳು (ನವೀಕರಿಸಬೇಕು)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient ಗೆ ಬದಲಾಯಿಸಿ
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True ಆಗಿರಬೇಕು

# ಪರೀಕ್ಷಾ ಮೂಲಭೂತಗಳನ್ನು (ನವೀಕರಿಸಬೇಕು)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# ವಿಷಯ ಫಿಲ್ಟರ್ ದೋಷ ದೇಹ ಪ್ರವೇಶ (ನವೀಕರಿಸಬೇಕು — ಸಂರಚನೆ ಬದಲಾಗಿದೆ)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # ಹಳೆಯ ಏಕವಚನ ಸ್ವರೂಪ — ಈಗ content_filter_results (ಬಹುವಚನ) content_filters ಅರೇನಲ್ಲಿ

# Chat Completions ಕಡೆಯಕರೆಗೆ ನೇರ HTTP ಕರೆಗಳು (URL ನವೀಕರಿಸಬೇಕು)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### ಹ್ಯೂರಿಸ್ಟಿಕ್ (ಪತ್ತೆಮಾಡಿ ಮತ್ತು ಮರುಬರೆಯಿರಿ)

- **ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ ಕ್ಲೈಯಿಂಟ್**: `client.chat.completions.create` → `client.responses.create(...)`.

- **ಅಜ್ಯೂರ್ ಕ್ಲಯಿಂಟ್ ರಚನೆಗಳು**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **ಟೂಲ್ಸ್**: ಫಂಕ್ಷನ್-ಕಾಲಿಂಗ್ ಉಪಕರಣ ವ್ಯಾಖ್ಯಾನಗಳನ್ನು ನೆಸ್ಟೆಡ್ ಫಾರ್ಮ್ಯಾಟ್ (`{"type": "function", "function": {"name": ...}}`) ರಿಂದ ಫ್ಲಾಟ್ Responses ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ (`{"type": "function", "name": ...}`) ಪರಿವರ್ತಿಸಿ; `tool_choice` ಬಳಸಿ; ಟೂಲಿನ ಫಲಿತಾಂಶಗಳನ್ನು `{"type": "function_call_output", "call_id": ..., "output": ...}` ವಿಷಯಗಳಾಗಿ ಹಿಂತಿರುಗಿಸಿ (`{"role": "tool", ...}` ಅಲ್ಲ).
- **ಟೂಲ್ ರೌಂಡ್-ಟ್ರಿಪ್‌ಗಳು**: ಮಾದರಿ ಫಂಕ್ಷನ್ ಕರೆಗಳನ್ನು ವಾಪಸ್ ಮಾಡಿದಾಗ, ಸಂವಾದಕ್ಕೆ `response.output` ವಿಷಯಗಳನ್ನು ಸೇರಿಸಿ (`{"role": "assistant", "tool_calls": [...]}` ಡಿಕ್‌ಟ್ ಕೈಯಿಂದ ಇಲ್ಲದೇ), ನಂತರ ಪ್ರತಿ ಫಲಿತಾಂಶದ `function_call_output` ವಿಷಯಗಳನ್ನು ಸೇರಿಸಿ.
- **ಸ್ವಲ್ಪ-ಶಾಟ್ ಟೂಲ್ ಉದಾಹರಣೆಗಳು**: ಸಂವಾದದಲ್ಲಿ ಹಾರ್ಡ್‌ಕೋಡೆಡ್ ಉಪಕರಣ ಕರೆ ಉದಾಹರಣೆಗಳು ಇದ್ದರೆ ಅವುಗಳನ್ನು `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` ವಿಷಯಗಳಾಗಿ ಪರಿವರ್ತಿಸಿ. IDs ಮೊದಲುದಾಗಿ `fc_` ಇರಬೇಕು.
- **`pydantic_function_tool()`**: ಈ ಸಹಾಯಕವು ಈಗಲಿನ ನೆಸ್ಟೆಡ್ ಫಾರ್ಮ್ಯಾಟ್ ಅನ್ನು ನಿರ್ಮಿಸುತ್ತದೆ ಮತ್ತು `responses.create()` ಜೊತೆ **ಸಮ್ಮಿಲನವಾಗುವುದಿಲ್ಲ**. ಕೈಯಿಂದ ಟೂಲ್ ವ್ಯಾಖ್ಯಾನಗಳು ಅಥವಾ ಫ್ಲ್ಯಾಟನ್ ಮಾಡುವ ರಾಪರ್‌ ಬಳಸಿರಿ.
- **ಮಲ್ಟಿ-ಟರ್ನ್**: ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ ಸಂವಾದ ಇತಿಹಾಸವನ್ನು ನಿರ್ವಹಿಸಿ; ಹಿಂದಿನ ಟರ್ನ್‌ಗಳನ್ನು `input` ವಿಷಯಗಳ ಮೂಲಕ ಹಿಂತೆಗೆ.
- **ರೂಪರೇಖೆ**: ಚಾಟ್‌ನ ಟಾಪ್-ಲೆವೆಲ್ `response_format` ಅನ್ನು Responses ನಲ್ಲಿ `text.format` ರಿಂದ ಬದಲಾಯಿಸಿ. ಕನಾನಿಕಲ್ ಆಕಾರ: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **ವಿಷಯದ ಐಟಂಗಳು**: ಚಾಟ್ `content[].type: "text"` ಅನ್ನು Responses ನಲ್ಲಿ ಬಳಕೆದಾರ/ಸಿಸ್ಟಮ್ ಟರ್ನ್‌ಗಳಿಗೆ `content[].type: "input_text"` ಗೆ ಬದಲಾಯಿಸಿ.
- **ಚಿತ್ರ ವಿಷಯದ ಐಟಂಗಳು**: ಚಾಟ್ `content[].type: "image_url"` ಅನ್ನು Responses ನಲ್ಲಿ `content[].type: "input_image"` ಗೆ ಬದಲಾಯಿಸಿ. `image_url` ಕ್ಷೇತ್ರವು ನೆಸ್ಟೆಡ್ ಆಬ್ಜೆಕ್ಟ್  `{"url": "..."}` ನಿಂದ ಫ್ಲಾಟ್ ಸ್ಟ್ರಿಂಗ್ ಆಗಿ ಬದಲಾಯಿಸಿದೆ. ಮೊದಲು/ನಂತರ ಉದಾಹರಣೆಗಳಿಗಾಗಿ ಚೀಟ್ ಶೀಟ್ ನೋಡಿ.
- **ಕಾರಣದ ಪ್ರಯತ್ನ**: **ಮೂಲ ಕೋಡ್ ನಲ್ಲಿ ಈಗಾಗಲೇ ಅಸ್ತಿತ್ವದಲ್ಲಿದ್ದರೆ ಮಾತ್ರ `reasoning` ಅನ್ನು ಸ್ಥಳಾಂತರಿಸಿ**.
- **ವಿಷಯ ಶೋಧಕ ದೋಷ ನಿರ್ವಹಣೆ**: ದೋಷ ಬಾಡಿ ರಚನೆ ಬದಲಾಗಿದೆ. ಚಾಟ್ ಪೂರ್ಣಗೊಂಡುಗಳು `error.body["innererror"]["content_filter_result"]` (ಏಕವಚನ) ಬಳಸುತ್ತಿತ್ತು; Responses API `error.body["content_filters"][0]["content_filter_results"]` (ಬಹುವಚನ, ಒಂದು ಸಂರಚನೆಯಲ್ಲಿ) ಬಳಸುತ್ತದೆ. `innererror` ಗೆ ಪ್ರವೇಶಿಸುವ ಕೋಡ್ `KeyError` ಅನ್ನು ಎರುವದು. ಹೊಸ ಮಾರ್ಗವನ್ನು ಬಳಸಲು ಮರುಬರೆ.
- **ರಾ HTTP ಕರೆಗಳು**: ಅಪ್ಲಿಕೇಶನ್ ನಿಲ್ಲದೆಗೆ Azure OpenAI REST API ನೇರವಾಗಿ ಕರೆ ಮಾಡುತ್ತಿದ್ದರೆ (`requests`, `httpx` ಮುಂತಾದ್ವರ್ಗಳ ಮೂಲಕ) `/openai/deployments/{name}/chat/completions?api-version=...` χρήση,  `/openai/v1/responses` ಗೆ ಮರುಬರೆಯಿರಿ. ವಿನಂತಿ ಬಾಡಿ ಬದಲಾಗುತ್ತದೆ: `messages` → `input`, `max_output_tokens` ಮತ್ತು `store: false` ಸೇರಿಸುವುದು, `api-version` ಪ್ರಶ್ನೆ ಪರಿಮಿತಿ ತೆಗೆದುಹಾಕುವುದು. ಪ್ರತಿಕ್ರಿಯೆ ಬಾಡಿ ಬದಲಾಗುತ್ತದೆ: `choices[0].message.content` → `output[0].content[0].text` (ಸೂಚನೆ: `output_text` SDK ಸೌಲಭ್ಯ ಗುಣಲಕ್ಷಣವಾಗಿದ್ದು ರಾ REST JSON ನಲ್ಲಿ ಇಲ್ಲ).

---

## ಹಂತ 2: ಸ್ಥಳಾಂತರವನ್ನು ಅನ್ವಯಿಸಿ

### ಸ್ಥಳಾಂತರ ಟಿಪ್ಪಣಿಗಳು (ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಯಿಂದ → Responses)

- **ಏಕೆ ಸ್ಥಳಾಂತರ**: Responses ಪಠ್ಯ, ಉಪಕರಣಗಳು, ಮತ್ತು ಸ್ಟ್ರೀಮಿಂಗ್‌ಗಾಗಿ ಏಕೀಕೃತ API ಆಗಿದೆ; ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ ಹಳೆಯದು. GPT-5 ಜೊತೆ Responses ಅತ್ಯುತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆಗೆ ಅವಶ್ಯಕ.
- **HTTP**: ಅಜ್ಯೂರ್ ಎಂಡ್ಪಾಯಿಂಟ್ `/openai/deployments/{name}/chat/completions` ನಿಂದ `/openai/v1/responses` ಗೆ ಬದಲಾಗುತ್ತದೆ.
- **ಕ್ಷೇತ್ರಗಳು**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` ಉಳಿಯುತ್ತದೆ.
- **ರೂಪರೇಖೆ**: `response_format` → ಸರಿಯಾದ ಆಬ್ಜೆಕ್ಟ್ ಇರುವ `text.format` ಗೆ ಬದಲಾಗುತ್ತದೆ.
- **ವಿಷಯದ ಐಟಂಗಳು**: ಚಾಟ್ `content[].type: "text"` ಅನ್ನು Responses ನಲ್ಲಿ ಸಿಸ್ಟಮ್/ಬಳಕೆದಾರ ಟರ್ನ್ಗಳಿಗೆ `content[].type: "input_text"` ಗೆ ಬದಲಾಯಿಸಿ.
- **ಚಿತ್ರ ವಿಷಯದ ಐಟಂಗಳು**: ಚಾಟ್ `content[].type: "image_url"` ಅನ್ನು Responses ನಲ್ಲಿ `content[].type: "input_image"` ಗೆ ಬದಲಾಯಿಸಿ. `image_url` ಕ್ಷೇತ್ರವನ್ನು `{"image_url": {"url": "..."}}` ನಿಂದ `{"image_url": "..."}` (ಸರಳ ಸ್ಟ್ರಿಂಗ್ — HTTPS URL ಅಲ್ಲದಿದ್ದರೆ `data:image/...;base64,...` ಡೇಟಾ URI ಆಗಿರಬಹುದು) ಗೆ ಫ್ಲಾಟ್ ಮಾಡಿ.

### ಪ್ಯಾರಾಮೀಟರ್ ನಕ್ಷೆ ಉಲ್ಲೇಖ

| ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (ಐಟಂಗಳ ಶ್ರೇಣಿ) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (ಆಬ್ಜೆಕ್ಟ್) |
| `temperature` | `temperature` (ಬದಲಾವಣೆ ಇಲ್ಲ) |
| `stop` | `stop` (ಬದಲಾವಣೆ ಇಲ್ಲ) |
| `frequency_penalty` | `frequency_penalty` (ಬದಲು ಇಲ್ಲ) |
| `presence_penalty` | `presence_penalty` (ಬದಲಾವಣೆ ಇಲ್ಲ) |
| `tools` / ಫಂಕ್ಷನ್-ಕಾಲಿಂಗ್ | `tools` (ಬದಲಾವಣೆ ಇಲ್ಲ) |
| `seed` | **ತೆಗೆದುಹಾಕಿ** (ಬೆಂಬಲವಿಲ್ಲ) |
| `store` | `store` (`false` ಗೆ ಸೆಟ್‌ಮಾಡಿ) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (ಫ್ಲಾಟ್ ಸ್ಟ್ರಿಂಗ್) |

ಸಂಪೂರ್ಣ ಮೊದಲು/ನಂತರ ಕೋಡ್ ಉದಾಹರಣೆಗಳಿಗಾಗಿ, [cheat-sheet.md](./references/cheat-sheet.md) ನೋಡಿ.

ಪರೀಕ್ಷಾ ಮೂಲಸೌಕರ್ಯ ಸ್ಥಳಾಂತರ (ಮಾಕ್ಸ್, ಸ್ನ್ಯಾಪ್‌ಶಾಟ್‌ಗಳು, ದೃಢೀಕರಣಗಳು)ಗಾಗಿ [test-migration.md](./references/test-migration.md) ನೋಡಿ.

ದೋಷ ಹಾಗೂ ಸಮಸ್ಯೆಗಳ ಪರಿಹಾರಕ್ಕಾಗಿ [troubleshooting.md](./references/troubleshooting.md) ನೋಡಿ.

---

## ಡೇಟಾ ಉಳಿಕೆ ಮತ್ತು ಸ್ಥಿತಿ

- ಎಲ್ಲಾ Responses ವಿನಂತಿಗಳಿಗೆ `store: false` ಸೆಟ್‌ ಮಾಡಿ.
- ಹಳೆಯ ಸಂದೇಶ ಐಡಿಗಳಿಗೆ ಅಥವಾ ಸರ್ವರ್-ಸಂಗ್ರಹಿತ ಸಂಧರ್ಭಕ್ಕೆ ಅವಲಂಬನೆ ಇಡಬೇಡಿ; ಸ್ಥಿತಿಯನ್ನು ಕ್ಲಿಯಂಟ್-ನಿಯಂತ್ರಿತವಾಗಿ ಇಡಿ ಮತ್ತು ಮೆಟಾಡೇಟಾವನ್ನು ಕನಿಷ್ಠ ಮಾಡಿ.

---

## ಸ್ವೀಕೃತಿ ಮಾನದಂಡಗಳು

### ಕೋಡ್ ಮಟ್ಟದ ಗೇಟುಗಳು (ಎಲ್ಲವು ಪಾಸಾಗಬೇಕು)

- [ ] `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` ಗೆ ಸ್ಥಳಾಂತರಗೊಂಡ ಕಡತಗಳಲ್ಲಿ ಶೂನ್ಯ ಸರಿ ಸಾಧನೆ.
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` ಗೆ ಶೂನ್ಯ ಸರಿ ಸಾಧನೆ — ಎಲ್ಲಾ ರಚನೆಗಳು v1 ಎಂಡ್ಪಾಯಿಂಟ್ ಜೊತೆ `OpenAI`/`AsyncOpenAI` ಬಳಸುತ್ತವೆ.
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` ಗೆ ಶೂನ್ಯ ಸರಿ ಸಾಧನೆ — GitHub ಮಾದರಿ ಕೋಡ್ ಮಾರ್ಗಗಳನ್ನು ತೆಗೆದುಹಾಕಲಾಗಿದೆ.
- [ ] `rg "OpenAIChatCompletionClient"` ಗೆ ಶೂನ್ಯ ಸರಿ ಸಾಧನೆ — MAF 1.0.0+ ಕೋಡ್ `OpenAIChatClient` (Responses API ಬಳಸುತ್ತದೆ) ಬಳಸುತ್ತದೆ. 1.0.0 ಮೊದಲು, `agent-framework-openai>=1.0.0` ಗೆ ಅಪ್‌ಗ್ರೇಡ್ ಮಾಡಿ.
- [ ] ಎಲ್ಲಾ `ChatOpenAI(...)` ಕರೆಗಳು `use_responses_api=True` ಅನ್ನು ಒಳಗೊಂಡಿವೆ.
- [ ] `rg "choices\[0\]"` ಗೆ ಶೂನ್ಯ ಸರಿ ಸಾಧನೆ — ಎಲ್ಲ ಪ್ರತಿಕ್ರಿಯೆ ಪ್ರವೇಶ `resp.output_text` ಅಥವಾ Responses ಔಟ್‌ಪುಟ್ ಭಾಷಾವಿಧಾನದ ಮೂಲಕ.
- [ ] ಟಾಪ್ ಲೆವೆಲ್‌ನಲ್ಲಿ `response_format` ಇಲ್ಲ; ಎಲ್ಲಾ ಸಂರಚಿತ ಔಟ್‌ಪುಟ್ `text={"format": {...}}` ಬಳಕೆ.
- [ ] `requirements.txt` ಅಥವಾ `pyproject.toml` ನಲ್ಲಿ `openai>=1.108.1` ಮತ್ತು `azure-identity`; ಅವಲಂಬನೆಗಳನ್ನು ಮರುಸ್ಥಾಪಿಸಲಾಗಿದೆ.
- [ ] ಪ್ರತಿಯೊಂದು `responses.create` ಕರೆಗೆ `store=False` ಸೆಟ್ ಮಾಡಲಾಗಿದೆ.
- [ ] ಕ್ಲಿಯಂಟ್ ರಚನೆಗಳಲ್ಲಿ ಯಾವುದೇ `api_version` ಇಲ್ಲ; `AZURE_OPENAI_API_VERSION` ಪರಿಸರ ಫೈಲ್‌ಗಳು ಮತ್ತು ಮೂಲಸೌಕರ್ಯದಿಂದ ತೆಗೆದುಹಾಕಲಾಗಿದೆ.

### ಪರೀಕ್ಷಾ ಮೂಲಸೌಕರ್ಯ ಗೇಟುಗಳು (ಎಲ್ಲವು ಪಾಸಾಗಬೇಕು)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` ಗೆ ಶೂನ್ಯ ಸರಿ ಸಾಧನೆ.
- [ ] `rg "_azure_ad_token_provider" tests/` ಗೆ ಶೂನ್ಯ ಸರಿ ಸಾಧನೆ — ದೃಢೀಕರಣಗಳು `isinstance(client, AsyncOpenAI)` ಅಥವಾ `base_url` ಅನ್ನು ಪರಿಶೀಲಿಸುತ್ತವೆ.
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` ಗೆ ಶೂನ್ಯ ಸರಿ ಸಾಧನೆ — ಅಜ್ಯೂರ್-ನಿರ್ದಿಷ್ಟ ಶೋಧಕ ಮಾಕ್‌ಗಳು ತೆಗೆದುಹಾಕಲಾಗಿದೆ.
- [ ] ಮಾಕ್ ಫಿಕ್ಸ್ಚರ್ಸ್ ನಲ್ಲಿ `kwargs.get("input")` ಬಳಸಲಾಗಿದೆ ಆದರೆ `kwargs.get("messages")` ಅಲ್ಲ.
- [ ] ಸ್ನ್ಯಾಪ್‌ಶಾಟ್ / ಗೋಲ್ಡನ್ ಕಡತಗಳು Responses ಸ್ಟ್ರೀಮಿಂಗ್ ಆಕಾರಕ್ಕೆ ಅಂತರ್ಗತವಾಗಿ ( `choices[0]`, `function_call`, `logprobs` ಮೊದಲಾದವು ಇಲ್ಲ ) ನವೀಕರಿಸಲಾಗಿದೆ.
- [ ] `pytest` ಎಲ್ಲಾ ತೊಂದರೆಗಳಿಲ್ಲದೆ ಪಾಸ್ ಆಗಿದೆ ಎಲ್ಲಾ ಪರೀಕ್ಷಾ ನವೀಕರಣಗಳ ನಂತರ.

### ನಡೆವಿಕೆಯ ಗೇಟುಗಳು (ಮೆನುಷ್ಯ ಅಥವಾ ಪರೀಕ್ಷಾ ಹಾರ್ನೆಸ್ ಮೂಲಕ ಪರಿಶೀಲಿಸಿ)

- [ ] **ಮೂಲ್ಯದ ಪೂರಕತೆ**: ನಾನ್-ಸ್ಟ್ರೀಮಿಂಗ್ `responses.create` ಖಾಲಿ ಅಲ್ಲದ `output_text` ಅನ್ನು ನೀಡುತ್ತದೆ.
- [ ] **ಸ್ಟ್ರೀಮ್ ಸಸ್ಯತೆ**: ಮೂಲ ಕೋಡ್ ಸ್ಟ್ರೀಮಿಂಗ್ ಬಳಸಿದರೆ, ಸ್ಥಳಾಂತರಿತ ಕೋಡ್ ಸ್ಟ್ರೀಮಿಂಗ್ ಮಾಡುತ್ತದೆ ಮತ್ತು ಶೂನ್ಯವಲ್ಲದ ಡೆಲ್ಟಾ ಘಟನೆಗಳೊಂದಿಗೆ `response.output_text.delta` ಅನ್ನು ನೀಡುತ್ತದೆ.
- [ ] **ಸಂರಚಿತ ಔಟ್‌ಪುಟ್**: `text.format` ಜೊತೆಗೆ `json_schema` ಬಳಸದಿದ್ದರೆ, `json.loads(resp.output_text)` ಯಶಸ್ವಿಯಾಗಿ ಚಲಿಸುತ್ತದೆ ಮತ್ತು schemas ಗೆ ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ.
- [ ] **ಟೂಲ್-ಕಾಲ್ ಲೂಪ್**: ಟೂಲ್ಸ್ ಬಳಕೆಯಾದರೆ, ಮಾದರಿ ಟೂಲ್ ಕರೆಗಳನ್ನು ಮಾಡುತ್ತದೆ, ಅಪ್ಲಿಕೇಶನ್ ಅವುಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ ಮತ್ತು ನಂತರದ ವಿನಂತಿ ಅಂತಿಮ `output_text` ಅನ್ನು ನೀಡುತ್ತದೆ (ಅನಂತ ಲೂಪ್ ಇಲ್ಲ).
- [ ] **ಅಸಿಂಕ್ ಸಮಾನತೆ**: `AsyncAzureOpenAI` ಬಳಸಿದ್ದರೆ, `AsyncOpenAI` ಸಮಾನತೆ await ಜೊತೆಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ.
- [ ] **ದೋಷ ದರ**: ಸ್ಥಳಾಂತರ ಮುಂಚೆಯೂಪದ ಮಟ್ಟದ 400/401/404 ದೋಷಗಳಲ್ಲಿ ಯಾವುದೇ ಹೊಸದಿಲ್ಲ.

### ನೀಡಬೇಕಾದವುಗಳು

- ಸಂಕ್ಷೇಪದಲ್ಲಿ ಸಂಪಾದಿತ ಫೈಲ್‌ಗಳು, ಹಳೆಯ/ಹೊಸ ಕಾಲ್ ಸೈಟ್‌ಗಳ ಎಣಿಕೆ, ಮತ್ತು ಮುಂದಿನ ಹಂತಗಳ ವಿವರಣೆ.
- ಬದಲಾವಣೆಗಳು ಕಾರ್ಯಪರ ಪಾಟಿಯಲ್ಲಿ ಮಾತ್ರ (ಕಮಿಟ್‌ಗಳಿಲ್ಲ).

---

## SDK ಆವೃತ್ತಿ ಅಗತ್ಯಗಳು

| ಪ್ಯಾಕೇಜ್ | ಕನಿಷ್ಠ ಆವೃತ್ತಿ |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | ಇತ್ತೀಚಿಗದ (ಎಂಟ್ರಾID ಪ್ರಾಮಾಣಿಕತೆಗಾಗಿ) |

---

## ಉಲ್ಲೇಖಗಳು

- [ಚೀಟ್ ಶೀಟ್ — ಎಲ್ಲಾ ಕೋಡ್ ಉದಾಹರಣೆಗಳು](./references/cheat-sheet.md)
- [ಪರೀಕ್ಷೆ ಸ್ಥಳಾಂತರ — ಮಾಕ್‌ಗಳು, ಸ্ন್ಯಾಪ್‌ಶಾಟ್‌ಗಳು, ದೃಢೀಕರಣಗಳು](./references/test-migration.md)
- [ಸಮಸ್ಯೆಗಳ ಪರಿಹಾರ — ದೋಷಗಳು, რಿಸ್ಕ್ ಟೇಬಲ್, ಗೋಧೆಗಳು](./references/troubleshooting.md)
- [detect_legacy.py — ಸ್ವಯಂಚಾಲಿತ ಸ್ಕ್ಯಾನರ್](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [ಅಜ್ಯೂರ್ OpenAI ಪ್ರಾರಂಭ ಕಿಟ್](https://aka.ms/openai/start)
- [ಅಜ್ಯೂರ್ OpenAI Responses API ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [ಅಜ್ಯೂರ್ OpenAI API ಆವೃತ್ತಿ ಜೀವನಚಕ್ರ](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API ಉಲ್ಲೇಖ](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->