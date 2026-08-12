---
name: azure-openai-to-responses
license: MIT
---
# ಅಜೂರ್ ಓಪನ್‌ಎಐ ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳಿಂದ ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಗೆ પાયથોન ಅಪ್ಲಿಕೇಶನ್ಗಳನ್ನು ವರ್ಗಾಯಿಸಿ

> **ಅಧಿಕೃತ ಮಾರ್ಗದರ್ಶನ — ನಿಖರವಾಗಿ ಅನುಸರಿಸಿ**
>
> ಈ ಕೌಶಲ್ಯವು ಪೈಥಾನ್ ಕೋಡ್‌ಬೇಸ್‌ಗಳನ್ನು ಅಜೂರ್ ಓಪನ್‌ಎಐ ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳಿಂದ
> ಏಕೀಕೃತ ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಗೆ ವರ್ಗಾಯಿಸುತ್ತದೆ. ಈ ಸೂಚನೆಗಳನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಅನುಸರಿಸಿ.
> ನಿಯಮಾವಳಿ ಮಾನದಂಡಗಳನ್ನು ಅಥವಾ API ರೂಪಗಳನ್ನು ಉಂಟುಮಾಡಬೇಡಿ.

---

## ಪ್ರೇರಕಗಳು

ಬಳಕೆದಾರರು ಈ ಕೆಳಗಿನ ಕಾರ್ಯಗಳನ್ನು ಆಚರಿಸಲು ಆಕಾಂಕ್ಷಿಸುವಾಗ ಈ ಕೌಶಲ್ಯ ಸಕ್ರಿಯಗೊಳ್ಳುತ್ತದೆ:
- ಅಜೂರ್ ಓಪನ್‌ಎಐ ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳಿಂದ ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಗೆ ಪೈಥಾನ್ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ವರ್ಗಾಯಿಸುವುದು
- ಅಜೂರ್ ಓಪನ್‌ಎಐ ವಿರುದ್ಧ ಇತ್ತೀಚಿನ API ರೂಪಕ್ಕೆ ಪೈಥಾನ್ ಓಪನ್‌ಎಐ SDK ಬಳಕೆಯನ್ನು ನವೀಕರಿಸುವುದು
- ಅಜೂರ್‌ನಲ್ಲಿ ಪ್ರತಿಕ್ರಿಯೆಗಳು ಬೇಕಾದ GPT-5 ಅಥವಾ ಹೊಸ ಮಾದರಿಗಾಗಿ ಪೈಥಾನ್ ಕೋಡ್ ತಯಾರಿಸುವುದು
- `AzureOpenAI`/`AsyncAzureOpenAI` ನಿಂದ ಸಾಂಪ್ರದಾಯಿಕ `OpenAI`/`AsyncOpenAI` ಕ್ಲೈಂಟ್ ಮತ್ತು v1 ಎಂಡ್ಪಾಯಿಂಟ್‌ಗೆ ಪರಿವರ್ತಿಸುವುದು
- `AzureOpenAI` ಕಾನ್ಸ್‌ಟ್ರಕ್ಟರ್‌ಗಳು ಅಥವಾ `api_version` ಗೆ ಸಂಬಂಧಿಸಿದ ಹಳೇ ಎಚ್ಚರಿಕೆಗಳನ್ನು ಸರಿಪಡಿಸುವುದು

---

## ⚠️ ಮಾದರಿ ಹೊಂದಾಣಿಕೆ — ಮೊದಲು ಪರಿಶೀಲಿಸಿ

> **ವರ್ಗಾವಣೆ ಮಾಡಲು ಮೊದಲು, ನಿಮ್ಮ ಅಜೂರ್ ಓಪನ್‌ಎಐ ನಿಯೋಜನೆ ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆಯೆ ಎಂಬುದನ್ನು ಪರಿಶೀಲಿಸಿ.**

### 1. ನಿಮ್ಮ ನಿಯೋಜನೆಯನ್ನು ಸ್ಮೋಕ್ ಟೆಸ್ಟ್ ಮಾಡಿ (ತ್ವರಿತ)

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

> **ಸೂಚನೆ**: ಅಜೂರ್ ಓಪನ್‌ಎಐನಲ್ಲಿ `max_output_tokens` ಗೆ ಕನಿಷ್ಠ ಮೌಲ್ಯ 16 ಇರುತ್ತದೆ. 16 ಕ್ಕಿಂತ ಕಡಿಮೆ ಮೌಲ್ಯಗಳು 400 ದೋಷವನ್ನು ಕೊಡುವವು. ಸ್ಮೋಕ್ ಟೆಸ್ಟ್‌ಗಾಗಿ 50+ ಬಳಸಿ.

ಇದು 404 ವಾಪಸಿ ನೀಡಿದರೆ, ನಿಯೋಜನೆಯ ಮಾದರಿ ಇನ್ನೂ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ಬೆಂಬಲಿಸುವುದಿಲ್ಲ — ಕೆಳಗಿನ ಉಲ್ಲೇಖವನ್ನು ಪರಿಶೀಲಿಸಿ ಅಥವಾ ಬೆಂಬಲಿತ ಮಾದರಿಯೊಂದಿಗೆ ಮರುನಿಯೋಜಿಸಿ.

### 2. ನಿಮ್ಮ ಪ್ರದೇಶದಲ್ಲಿ ಲಭ್ಯವಿರುವ ಮಾದರಿಗಳನ್ನು ಪರಿಶೀಲಿಸಿ (ಶಿಫಾರಸು)

ನಿಮ್ಮ ನಿರ್ದಿಷ್ಟ ಪ್ರದೇಶದಲ್ಲಿ ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಬೆಂಬಲ ಇರುವುದನ್ನು ನೋಡಲು ಒಳನಿರ್ಮಿತ ಮಾದರಿ ಹೊಂದಾಣಿಕೆ ಉಪಕರಣವನ್ನು ಚಾಲನೆ ಮಾಡಿ:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

ಇದು ಅಜೂರ್ ARM ಸಜೀವ ಪ್ರಶ್ನೆಯನ್ನು ನಡೆಸುತ್ತದೆ ಮತ್ತು ಹೊಂದಾಣಿಕೆ ಮ್ಯಾಟ್ರಿಕ್ಸ್ ಅನ್ನು ತೋರಿಸುತ್ತದೆ — ಯಾವ ಮಾದರಿಗಳು ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು, ರಚನೆಗೊಂಡ ಔಟ್‌ಪುಟ್, ಸರಂಜಾಮುಗಳು ಇತ್ಯಾದಿಗಳನ್ನು ಬೆಂಬಲಿಸುವುದನ್ನು. ಫಲಿತಾಂಶಗಳನ್ನು ಸೀಮಿತಗೊಳಿಸಲು `--filter gpt-5.1,gpt-5.2` ಬಳಸಿರಿ ಅಥವಾ ಸ್ಕ್ರಿಪ್ಟಿಂಗ್‌ಗೆ `--json` ಬಳಸಿ.

### 3. ಸಂಪೂರ್ಣ ಮಾದರಿ ಬೆಂಬಲ ಉಲ್ಲೇಖ

- **ಲೈವ್ ಕ್ವೇರಿ**: `python migrate.py models` (ಮೇಲ್ಗಡೆ ನೋಡಿರಿ — ಪ್ರದೇಶ-ನಿರ್ದಿಷ್ಟ, ಸದಾ ನವೀಕರಿತ)
- **ಲಭ್ಯತೆ ವೀಕ್ಷಣೆ**: [ಮಾದರಿ ಸಾರಾಂಶ ಪಟ್ಟಿ ಮತ್ತು ಪ್ರದೇಶ ಲಭ್ಯತೆ](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **ಕ್ವಿಕ್‌ಸ್ಟಾರ್ಟ್ ಮತ್ತು ಮಾರ್ಗದರ್ಶನ**: **https://aka.ms/openai/start**

### ⚠️ ಹಳೆಯ ಮಾದರಿ ನಿರ್ಬಂಧಗಳು

> **ಎಚ್ಚರಿಕೆ**: ಹಳೆಯ ಮಾದರಿಗಳು (`gpt-4.1` ಕ್ಕೆ ಮುಂಚಿತ) ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಯ ಎಲ್ಲಾ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಬೆಂಬಲಿಸದಿರಬಹುದು.
>
> ಹಳೆಯ ಮಾದರಿಗಳಲ್ಲಿನ ತಿಳಿದಿರುವ ನಿರ್ಬಂಧಗಳು:
> - **`reasoning` ನಿಯಮಾವಳಿ**: ಬಹುತೇಕ ನಿರ್ಧಾರಾತ್ಮಕ ಮಾದರಿಗಳಲ್ಲಿ ಬೆಂಬಲಿಸುವುದಿಲ್ಲ. ಮೂಲ ಕೋಡಿನಲ್ಲಿ ಇದಿದ್ದರೆ ಮಾತ್ರ ವರ್ಗಾಯಿಸಿ.
> - **`seed` ನಿಯಮಾವಳಿ**: ಪ್ರತಿಕ್ರಿಯೆಗಳ API ನಲ್ಲಿ ಯಾವುದೇ ಬೆಂಬಲವಿಲ್ಲ — ಎಲ್ಲಾ ವಿನಂತಿಗಳಿಂದ ತೆಗೆದುಹಾಕಿ.
> - **`text.format` ಮುಖಾಂತರ ರಚನೆಗೊಂಡ ಔಟ್‌ಪುಟ್**: ಹಳೆಯ ಮಾದರಿಗಳು `strict: true` JSON ಸ್ಕೀಮಾಗಳನ್ನು ನಿಖರವಾಗಿ ಅನುಸರಿಸದಿರಬಹುದು.
> - **ಸರಂಜಾಮು ಸಂಯೋಜನೆ**: GPT-5+ ಆಂತರಿಕ ನಿರ್ಧಾರದ ಭಾಗವಾಗಿ ಸರಂಜಾಮು ಕರೆಗಳನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ. ಹಳೆಯ ಮಾದರಿಗಳು ಪ್ರತಿಕ್ರಿಯೆಗಳಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ, ಆದರೆ ಆಳವಾದ ಸಂಯೋಜನೆ ಇಲ್ಲ.
> - **ತೆಂಪರೆಚರ್ ನಿರ್ಬಂಧಗಳು**: `gpt-5` ಗೆ ವರ್ಗಾಯಿಸುವಾಗ ತೆಂಪರೆಚರ್ ತೆಗೆದುಹಾಕಬೇಕು ಅಥವಾ `1` ಕ್ಕೆ ಹೊಂದಿಸಬೇಕು. ಹಳೆಯ ಮಾದರಿಗಳಲ್ಲಿ ಈ ನಿರ್ಬಂಧ ಇಲ್ಲ.

### ಓ-ಸೀರೀಸ್ ನಿರ್ಧಾರಾತ್ಮಕ ಮಾದರಿಗಳು (o1, o3-mini, o3, o4-mini)

ಓ-ಸೀರೀಸ್ ಮಾದರಿಗಳಿಗೆ ವಿಶಿಷ್ಟ ನಿಯಮಾವಳಿಗಳಿವೆ. ಓ-ಸೀರೀಸ್ ಮಾದರಿಗಳನ್ನು ಗುರಿಯಾಗಿಟ್ಟಿರುವ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ವರ್ಗಾಯಿಸುವಾಗ:

- **`temperature`**: `1` ಇರಬೇಕು (ಅಥವಾ ಕೈಗೆಡದಿರಬೇಕು). ಓ-ಸೀರೀಸ್ ಮಾದರಿಗಳು ಇತರ ಮೌಲ್ಯಗಳನ್ನು ಸ್ವೀಕರಿಸುವುದಿಲ್ಲ.
- **`max_completion_tokens` → `max_output_tokens`**: ಅಜೂರ್-ನಿರ್ದಿಷ್ಟ `max_completion_tokens` ಬಳಕೆದಾರರು `max_output_tokens` ಗೆ ಬಿಡಬೇಕು. reasoning tokens ಲಿಮಿಟ್‌ಗೆ ಸೇರಿಸಬೇಕು ಆದ್ದರಿಂದ ಹೆಚ್ಚಿನ ಮೌಲ್ಯಗಳನ್ನು (4096+) ನಿಗದಿಪಡಿಸಿ.
- **`reasoning_effort`**: ಅಪ್ಲಿಕೇಶನಿನಲ್ಲಿ `reasoning_effort` (low/medium/high) ಇದ್ದರೆ ಅದನ್ನು ಕಾಯ್ದುಕೊಳ್ಳಿ — ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಓ-ಸೀರೀಸ್ ಮಾದರಿಗಳಿಗೆ ಈ ನಿಯಮಾವಳಿಯನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ.
- **ಸ್ಟ್ರೀಮಿಂಗ್ ವರ್ತನೆ**: ಓ-ಸೀರೀಸ್ ಮಾದರಿಗಳು ಪೂರ್ಣ reasoning ನಂತ್ರ ಆ.utput ಅನ್ನು ಬಫರ್ ಮಾಡಿ ನಂತರ ಪಠ್ಯ ಡೆಲ್ಟಾ ಘಟನೆಗಳನ್ನು ಹರಡುತ್ತವೆ. ಸ್ಟ್ರೀಮಿಂಗ್ ಸರಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವುದು, ಆದರೆ ಮೊದಲ `response.output_text.delta` ಗರಿಷ್ಟ ವಿಳಂಬೊಂದಿಗೆ ಬರಬಹುದು.
- **`top_p`**: ಓ-ಸೀರೀಸ್‌ನಲ್ಲಿ ಬೆಂಬಲಿಸುವುದಿಲ್ಲ — ಇದ್ದರೆ ತೆಗೆದು ಹಾಕಿ.
- **ಸರಂಜಾಮು ಬಳಕೆ**: ಓ-ಸೀರೀಸ್ ಮಾದರಿಗಳು ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಮೂಲಕ ಸರಂಜಾಮುಗಳನ್ನು GPT ಮಾದರಿಗಳಂತೆ ಬೆಂಬಲಿಸುತ್ತವೆ, ಆದರೆ ಸರಂಜಾಮು ಕರೆ ನಿರ್ವಹಣೆಯ ಗುಣಮಟ್ಟ ಮಾದರಿ ಪ್ರಕಾರ ವ್ಯತ್ಯಾಸವಿದೆ.

**ಕ್ರಿಯೆ — ಸಕ್ರಿಯ ಮಾದರಿ ಸಲಹೆ**: ಸ್ಕ್ಯಾನ್ ಹಂತದಲ್ಲಿ ಅಪ್ಲಿಕೇಶನ್ ಗುರಿಯಾಗಿರುವ ಮಾದರಿಯನ್ನು (ನಿಯೋಜನೆ ಹೆಸರುಗಳು, ಪರಿಸರ ಚರ, ವಿನ್ಯಾಸ) ಪರಿಶೀಲಿಸಿ. ಮಾದರಿ `gpt-4.1` ಕ್ಕಿಂತ ಹಳೆಯದಾಗಿದ್ದರೆ (gpt-4.1+ ಅಲ್ಲ) ಬಳಕೆದಾರನಿಗೆ ಮುಂಚಿತವಾಗಿ ತಿಳಿಸಿ:
- ವರ್ಗಾಯಿಸುವಿಕೆ ಮೂಲ ಪಠ್ಯ, ಚಾಟ್, ಸ್ಟ್ರೀಮಿಂಗ್ ಮತ್ತು ಸರಂಜಾಮುಗಳಿಗಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ.
- ಹೊಸ ಮಾದರಿಗಳು (`gpt-5.1`, `gpt-5.2`) ಉತ್ತಮ ಸರಂಜಾಮು ನಿರ್ವಹಣೆ, ರಚನಾತ್ಮಕ ಔಟ್‌ಪುಟ್ ಜಾರಿ, ನಿರ್ಧಾರಶೀಲತೆ, ಮತ್ತು ಪ್ರದೇಶಾಂತರ ಲಭ್ಯತೆ ನೀಡುತ್ತವೆ.
- ತಯಾರಾದಾಗ ತಮ್ಮ ನಿಯೋಜನೆಯನ್ನು ನವೀಕರಿಸುವ ಬಗ್ಗೆ ಯೋಚಿಸಬೇಕು — ಇದು ವರ್ಗಾಯಿಯನ್ನು ತಡೆ ಹಾಕುವುದಕ್ಕೆ ಕಾರಣವಲ್ಲ.

ಮಾದರಿ ಆವೃತ್ತಿಯ ಆಧಾರದ ಮೇಲೆ ವರ್ಗಾಯಿಸುವಿಕೆಯನ್ನು ತಡೆಯಬೇಡಿ ಅಥವಾ ನಿರಾಕರಿಸಬೇಡಿ. ಸಲಹೆ ಮಾಹಿತಿ ಮಾತ್ರ.

### GitHub ಮಾದರಿಗಳು ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಅನ್ನು ಬೆಂಬಲಿಸುವುದಿಲ್ಲ

> **GitHub ಮಾದರಿಗಳು (`models.github.ai`, `models.inference.ai.azure.com`) ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಅನ್ನು ಬೆಂಬಲಿಸುವುದಿಲ್ಲ.**

ಕೋಡ್‌ಬೇಸಿನಲ್ಲಿ GitHub ಮಾದರಿಗಳ ಕೋಡ್ ಮಾರ್ಗಗಳಿದ್ದರೆ (`base_url` ಅನ್ನು `models.github.ai` ಅಥವಾ `models.inference.ai.azure.com` ತಿರುವಾಗ), ವರ್ಗಾಯಿಸುವಾಗ ಅದನ್ನು **ಸಂಪೂರ್ಣವಾಗಿ ತೆಗೆದುಹಾಕಿ**. ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಅಜೂರ್ ಓಪನ್‌ಎಐ, ಓಪನ್‌ಎಐ, ಅಥವಾ ಸಮಾನ ಅವಕಾಶ ಇರುವ ಸ್ಥಳೀಯ ಎಂಡ್ಪಾಯಿಂಟ್ (ಉದಾ: Ollama ಪ್ರತಿಕ್ರಿಯೆಗಳ ಬೆಂಬಲದೊಂದಿಗೆ) ಅಗತ್ಯವಿದೆ.

ಸ್ಕ್ಯಾನ್ ಹಂತದಲ್ಲಿ ಕಾರ್ಯ:
- ಯಾವುದೇ GitHub ಮಾದರಿ ಕೋಡ್ ಮಾರ್ಗಗಳನ್ನು ತೆಗೆದುಹಾಕಲು ಧ್ವಜಿಸಿ.

---

## ಫ್ರೇಮ್ವರ್ಕ್ ವರ್ಗಾವಣೆ

ಅನೇಕ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು OpenAI ಮೇಲೆ ಮೇಲ್ಮಟ್ಟದ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳನ್ನು ಬಳಸುತ್ತವೆ. ಅವುಗಳನ್ನು ವರ್ಗಾಯಿಸುವಾಗ, ಫ್ರೇಮ್ವರ್ಕ್‌ನ ಸ್ವಂತ API ಬದಲಾವಣೆ—ಕೆಲವೊಮ್ಮೆ ಮಾತ್ರ ಮೂಲ OpenAI ಕರೆಗಳು ಅಲ್ಲ.

### ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ (MAF)

**ನೀವು MAF ಆವೃತ್ತಿಯನ್ನು ಮೊದಲು ಪರಿಶೀಲಿಸಿ** — ವರ್ಗಾವಣೆ ನಿಮ್ಮ MAF 1.0.0+ ಅಥವಾ ಪೀಠಿಕೆಯ ಮುನ್ನ.beta/rc ಆವೃತ್ತಿ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿದೆ.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಅನ್ನು ಈಗಾಗಲೆ ಬಳಸುತ್ತಿದೆ** — ಬೇರೆ ವರ್ಗಾವಣೆ ಅಗತ್ಯವಿಲ್ಲ. ಹಳೇ `OpenAIChatCompletionClient` (“chat.completions.create” ಬಳಕೆ) ಅಪ್ಲಿಕೇಶನ್ಗಳಲ್ಲಿ ಅದನ್ನು `OpenAIChatClient` ಗೆ ಬದಲಾಯಿಸಿ.

| ಮೊದಲ | ನಂತರ |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

ನಿಮ್ಮ ಆವೃತ್ತಿ ಪರಿಶೀಲಿಸಲು: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"` ಬಳಸಿ

#### MAF pre-1.0.0 (beta/rc ಬಿಡುಗಡೆಯಾಗಿರುವ ಆವೃತ್ತಿಗಳು)

pre-1.0.0 MAF ನಲ್ಲಿ, `OpenAIChatClient` ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳನ್ನು ಬಳಸುತ್ತಿತ್ತು. `agent-framework-openai>=1.0.0` ಗೆ ನವೀಕರಿಸಿ, ಅಲ್ಲಿ `OpenAIChatClient` ಸ್ವತಃ ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಅನ್ನು ಬಳಸುತ್ತದೆ.

ಬೇರೆ ಬದಲಾವಣೆಗಳು ಅಗತ್ಯವಿಲ್ಲ — `Agent` ಮತ್ತು ಸರಂಜಾಮು API ಗಳು ಅಷ್ಟೇ ಹಾಗೆಯೇ ಇರುತ್ತವೆ.

### ಲಾಂಗ್‌ಚೈನ್ (`langchain-openai`)

`ChatOpenAI()` ಕ್ಕೆ `use_responses_api=True` ಸೇರಿಸಿ. ಪ್ರತಿಕ್ರಿಯೆ ಪ್ರವೇಶ `.content` ನಿಂದ `.text` ಗೆ ಬದಲಿಸಿ.

| ಮೊದಲ | ನಂತರ |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

ಸಂಪೂರ್ಣ ಮೊದಲ/ನಂತರ ಕೋಡ್ ಉದಾಹರಣೆಗಳಿಗಾಗಿ, [cheat-sheet.md](./references/cheat-sheet.md) ನೋಡಿ.

---

## ಮುಂಭಾಗ ವರ್ಗಾವಣೆ ಮಾರ್ಗದರ್ಶನ

> **ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಒಂದು ಸರ್ವರ್-ಬದಿಯ ವಿಷಯ.** ನಿಮ್ಮ ಪೈಥಾನ್ ಬ್ಯಾಕೆಂಡ್ ಅನ್ನು ವರ್ಗಾಯಿಸಿ; ಮುಂಭಾಗದ HTTP ಒಪ್ಪಂದ ಬದಲಿಸಬೇಡಿ, ಬೇರೆ ಇಲ್ಲದಿದ್ದಲ್ಲಿ, ಪ್ರತಿಕ್ರಿಯೆಗಳ ವಿನಂತಿ ರೂಪವನ್ನು ಅಳವಡಿಸುವುದನ್ನು ಪರಿಗಣಿಸಿ. ಮುಂಭಾಗದಲ್ಲಿ ಒಬ್ಬ ಗ್ರಾಹಕ-ಪಕ್ಷೀಯ ಕೀಲಿಯನ್ನು ಬಳಸಿಕೊಂಡು OpenAI ಕಾಲ್ ಇದ್ದರೆ, ಅವುಗಳನ್ನು ಮೊದಲು ಬ್ಯಾಕೆಂಡಿಗೆ ಹೊರಡಿಸಿ.

### `@microsoft/ai-chat-protocol` ನಿಷ್ಕ್ರಿಯತೆ

`@microsoft/ai-chat-protocol` npm ಪ್ಯಾಕೇಜ್ ಅನ್ನು ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಲಾಗಿದೆ ಮತ್ತು ಅದನ್ನು [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) ಗೆ ಬದಲಾಯಿಸಬೇಕು. ಮುಂಭಾಗದಲ್ಲಿ ಇದನ್ನು ಕಂಡುಹಿಡಿದರೆ:

1. CDN ಸ್ಕ್ರಿಪ್ಟ್ ಟ್ಯಾಗ್ ಬದಲಾಯಿಸಿ:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` ರಚನೆಯನ್ನು ತೆಗೆದುಹಾಕಿ (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. `client.getStreamedCompletion(messages)` ಅನ್ನು ನೇರ `fetch()` ಕರೆ ಆಗಿ ಬ್ಯಾಕೆಂಡ್ ಸ್ಟ್ರೀಮಿಂಗ್ ಎಂಡ್ಪಾಯಿಂಟ್‌ಗೆ ಬದಲಾಯಿಸಿ.
4. `for await (const response of result)` ಅನ್ನು `for await (const chunk of readNDJSONStream(response.body))` ಗೆ ಬದಲಾಯಿಸಿ.
5. ಪ್ರಾಪರ್ಟಿ ಪ್ರವೇಶವನ್ನು `response.delta.content` / `response.error` ನಿಂದ `chunk.delta.content` / `chunk.error` ಗೆ ಬದಲಾಯಿಸಿ.

---

## ಗುರಿಗಳು

- ಅಜೂರ್ ಓಪನ್‌ಎಐ ವಿರುದ್ಧ ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳು ಅಥವಾ ಹಳೆಯ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳು ಬಳಸಿದ ಎಲ್ಲಾ ಪೈಥಾನ್ ಕಾಲ್ ಸೈಟ್ ಅನ್ನು ಗುರುತಿಸಿ.
- ಪೈಥಾನ್ ಕೋಡ್‌ಬೇಸ್‌ಗೆ ವರ್ಗಾವಣೆ ಯೋಜನೆ ಮತ್ತು ಕ್ರಮವನ್ನು đề proposta ಮಾಡಿ.
- ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಗೆ ಬದಲಾಯಿಸಲು ಸುರಕ್ಷಿತ, ಕನಿಷ್ಠ ಸಂಪಾದನೆಗಳು ಅನ್ವಯಿಸಿ.
- ಕರೆ ಮಾಡಿದವರು ಪ್ರತಿಕ್ರಿಯೆಗಳ ಔಟ್‌ಪುಟ್ ಸ್ಕೀಮಾ ಬಳಕೆ ಮಾಡಿಕೊಳ್ಳುವಂತೆ ನವೀಕರಿಸಿ; ಹಿಂದೆಗಿನ ಹೊಂದಾಣಿಕೆಯ ರಾಪರ್ಸ್ ಬೇಡ.
- ಪರೀಕ್ಷಾ/ಲಿಂಟ್ ಗಳನ್ನ ನಡಿಸಿ; ವರ್ಗಾವಣೆಯಿಂದ ಉಂಟಾದ ಸಣ್ಣ ಬ್ರೇಕ್‌ವೈಸ್‌ಗಳನ್ನು ಸರಿಪಡಿಸಿ.
- ಸಣ್ಣ, ಪರಿಶೀಲಿಸಲು সহজ ಬದಲಾವಣೆಗಳ ಸೆಟ್ ತಯಾರಿಸಿ ಮತ್ತು ಕೊನೆಯಲ್ಲಿ ವ್ಯತ್ಯಾಸಗಳೊಂದಿಗೆ ಸಾರಾಂಶ ನೀಡಿ (ಕಮಿಟ್ ಮಾಡಬೇಡಿ).

---

## ಗೇರ್ಡ್ರೈಲುಗಳು

- ಗಿಟ್ ಕಾರ್ಯಕ್ಷೇತ್ರದೊಳಗಿನ ಫೈಲ್‌ಗಳನ್ನು ಮಾತ್ರ ಬದಲಾಯಿಸಿ. ಹೊರಗಿನವುಗಳನ್ನು ಬರೆಯಬೇಡಿ.
- ಹಿಂದಿನ ಹೊಂದಾಣಿಕೆಯ ಶಿಮ್‌ಗಳನ್ನು ಉಳಿಸಬೇಡಿ; ಹೊಸ API ರೂಪಕ್ಕೆ ಕೋಡ್ ಅನ್ನು ವರ್ಗಾಯಿಸಿ.
- ಶವಸ್ಮರಣೆ/ಉಪಕ್ರಮ ಕಾಮೆಂಟ್‌ಗಳು ಅಥವಾ ಬ್ಯಾಕಪ್ ಫೈಲ್‌ಗಳನ್ನು ಉಳಿಸಬೇಡಿ.
- ಹಿಂದಿನಂತೆ ಸ್ಟ್ರೀಮಿಂಗ್ ಬಳಕೆಯಿದ್ದರೆ ಅದು ಉಳಿಸಬೇಕು; ಇಲ್ಲದಿದ್ದಲ್ಲಿ ಸ್ಟ್ರೀಮಿಂಗ್ ಇಲ್ಲದ ವಿಧಾನ ಬಳಸಿರಿ.
- ಅನುಮೋದನಾ ಮೋಡ್‍ನಲ್ಲಿ ಇರುವಾಗ ಆಜ್ಞೆಗಳು ಅಥವಾ ಜಾಲ ಸಂವಾದಗಳಿಗೆ ಅನುಮೋದನೆ ಕೇಳಿ.
- `git add`/`git commit`/`git push` ನಡಿಸಲು ಬಿಡಬೇಡಿ; ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಮರೆಯನ್ನು ಮಾತ್ರ ತಯಾರಿಸಿ.

---

## ಹಂತ 0: ಅಜೂರ್ ಓಪನ್‌ಎಐ ಕ್ಲೈಂಟ್ ವರ್ಗಾವಣೆ (ಮುನ್ಸೂಚನೆ)

ಕೋಡ್‌ಬೇಸ್ `AzureOpenAI` ಅಥವಾ `AsyncAzureOpenAI` ನಿರ್ಮಾಪಕರನ್ನು ಬಳಸಿದರೆ, ಮೊದಲು ಸಾಂಪ್ರದಾಯಿಕ `OpenAI` / `AsyncOpenAI` ಕಾನ್ಸ್‌ಟ್ರಕ್ಟರ್‌ಗಳಿಗೆ ವರ್ಗಾಯಿಸಿ. ಅಜೂರ್-ನಿರ್ದಿಷ್ಟ ನಿರ್ಮಾಪಕರು `openai>=1.108.1` ನಲ್ಲಿ ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಲಾಗಿದೆ.

### ಏಕೆ v1 API ಮಾರ್ಗ?

ಹೊಸ `/openai/v1` ಎಂಡ್ಪಾಯಿಂಟ್ ಸಾಂಪ್ರದಾಯಿಕ `OpenAI()` ಕ್ಲೈಂಟ್ ಅನ್ನು ಬಳಸುತ್ತದೆ, `AzureOpenAI()` ಅಲ್ಲ, `api_version` ನಿಯಮಾವಳಿ ಅಗತ್ಯವಿಲ್ಲ ಮತ್ತು ಇದು OpenAI ಹಾಗೂ ಅಜೂರ್ ಓಪನ್‌ಎಐ ಮರುಬಳಕೆ ಸಮಾನ. ಅದೇ ಕ್ಲೈಂಟ್ ಕೋಡ್ ಭವಿಷ್ಯ-ಪ್ರೂಫ್ — ಆವೃತ್ತಿ ನಿರ್ವಹಣೆ ಅಗತ್ಯವಿಲ್ಲ.

### ಪ್ರಮುಖ ಬದಲಾವಣೆಗಳು

| ಮೊದಲ | ನಂತರ |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | ಸಂಪೂರ್ಣ ತೆಗೆದುಹಾಕಿ |

### ಸ್ವಚ್ಛತೆ ಪರಿಶೀಲನೆ

- ಗ್ರಾಹಕ ನಿರ್ಮಾಣದಿಂದ `api_version` ಅರ್ಗುಮೆಂಟ್ ತೆಗೆದುಹಾಕಿ.
- `.env`, ಅಪ್ಲಿಕೇಶನ್ ಸೆಟ್ಟಿಂಗ್ಸ್, ಮತ್ತು ಬಿಸೆಪ/ಇನ್‌ಫ್ರಾ ಫೈಲ್‌ಗಳಿಂದ `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` ಪರಿಸರ ಚರಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.
- `.env`, ಅಪ್ಲಿಕೇಶನ್ ಸೆಟ್ಟಿಂಗ್ಸ್, ಬಿಸೆಪ/ಇನ್‌ಫ್ರಾ, ಮತ್ತು ಪರೀಕ್ಷಾ ಫಿಕ್ಸ್ಚರ್‍ಗಳಲ್ಲಿ `AZURE_OPENAI_CLIENT_ID` ಅನ್ನು `AZURE_CLIENT_ID` ಗೆ ಮರುನಾಮಕರಣ ಮಾಡಿ (ಪ್ರಮಾಣಿತ ಅಜೂರ್ ಗುರುತಿನ SDK ಸಂಪ್ರದಾಯ).
- `requirements.txt` ಅಥವಾ `pyproject.toml` ನಲ್ಲಿ `openai>=1.108.1` ಇದೆ ಎಂದು ಖಚಿತಪಡಿಸಿ.

### ಪರಿಸರ ಚರ ವರ್ಗಾವಣೆ

| ಹಳೆಯ ಪರಿಸರ ಚರ | ಕ್ರಿಯೆ | ಟಿಪ್ಪಣಿಗಳು |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **ತೆಗೆದುಹಾಕಿ** | v1 ಎಂಡ್ಪಾಯಿಂಟ್‌ಗೆ `api_version` ಅಗತ್ಯವಿಲ್ಲ |
| `AZURE_OPENAI_API_VERSION` | **ತೆಗೆದುಹಾಕಿ** | ಮೇಲಿನಂತೇ |
| `AZURE_OPENAI_CLIENT_ID` | **ಮರುನಾಮಕರಿಸಿ** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)`ಗೆ ಪ್ರಾಮಾಣಿಕ ಅಜೂರ್ ಗುರುತಿನ SDK ಸಂಪ್ರದಾಯ |
| `AZURE_OPENAI_ENDPOINT` | **ಉಳಿಸಿ** | `base_url` ರಚನೆಗೆ ಇನ್ನೂ ಅಗತ್ಯವಿದೆ |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **ಉಳಿಸಿ** | `responses.create` ನಲ್ಲಿ ಮಾದರಿ ಪ್ಯಾರಾಮ್ ಆಗಿ ಬಳಕೆ |
| `AZURE_OPENAI_API_KEY` | **ಉಳಿಸಿ** | ಕೀ ಆಧಾರಿತ ಪ್ರಮಾಣೀಕರಣಕ್ಕೆ `api_key` ಆಗಿ ಬಳಕೆ |

ಗ್ರಾಹಕ ಸೆಟ್‌ಅಪ್ ಕೋಡ್ ಉದಾಹರಣೆಗಳಿಗಾಗಿ (ಸಿಂಕ್, ಅಸಿಂಕ್, ಎಂಟ್ರಾID, API ಕೀ, ಬಹು-ಟೆನಂಟ್), [cheat-sheet.md](./references/cheat-sheet.md) ನೋಡಿ.

---

## ಹಂತ 1: ಹಳೆಯ ಕಾಲ್ ಸೈಟ್‌ಗಳನ್ನು ಪತ್ತೆ ಮಾಡಿ

ವರ್ಗಾವಣೆಯ ಅಗತ್ಯ ಇರುವ ಎಲ್ಲಾ ಕಾಲ್ ಸೈಟ್‌ಗಳನ್ನು ಕಂಡುಹಿಡಿಯಲು [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) ಸ್ಕ್ರಿಪ್ಟ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

ಅಥವಾ ಈ ಹುಡುಕುಗಡೆಗಳನ್ನು ಕೈಯಿಂದ ನಡೆಸಿ — ಪ್ರತಿ ಹೊಂದಾಣಿಕೆ ವರ್ಗಾವಣೆ ಗುರಿಯಾಗಿರುತ್ತದೆ:

```bash
# ಲೆಗಸಿ API ಕಾಲ್‌ಗಳು (ಮತ್ತೆ ಬರೆಯಬೇಕು)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# ಹಳೆಯದು ಆದ.azure ಕ್ಲೈಂಟ್ ನಿರ್ಮಾಪಕರು (ಬದಲಾಯಿಸಬೇಕು)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# ಪ್ರತಿಕ್ರಿಯಾ ಆಕಾರ ಪ್ರವೇಶ ಮಾದರಿಗಳು (ನವೀಕರಣ ಅಗತ್ಯವಿದೆ)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# ಹಳೆಯ ನೆಸ್ಟೆಡ್ ಫಾರ್ಮ್ಯಾಟ್‌ನಲ್ಲಿ ಟೂಲ್ ವ್ಯಾಖ್ಯಾನಗಳು (ಸಮನ್ವಯಗೊಳ್ಳಬೇಕು)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# ಹಳೆಯ ಫಾರ್ಮ್ಯಾಟ್‌ನಲ್ಲಿನ ಟೂಲ್ ಫಲಿತಾಂಶಗಳು (function_call_output ಗೆ ಪರಿವರ್ತನೆ ಮಾಡಬೇಕು)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# ಹಳೇ ಪರಿಮಾಣಗಳು (ತೆಗೆದುಕೊಳ್ಳಬೇಕು ಅಥವಾ ಹೆಸರು ಬದಲಾಯಿಸಬೇಕು)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens ಗೆ ಹೆಸರು ಬದಲಾಯಿಸು
rg "['\"]seed['\"]"      # remove entirely

# ಹಳೇ ಪರಿಸರ ಚರಗಳು (ವೆಚ್ಚ ಕಡಿಮೆ ಮಾಡು)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID ಆಗಿರಬೇಕು

# GitHub ಮಾದರಿಗಳ ವಿಳಾಸಗಳು (ತೆಗೆದುಹಾಕಬೇಕು — Responses API ಬೆಂಬಲಿಸುವುದಿಲ್ಲ)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# ಫ್ರೇಮ್ವರ್ಕ್-ಮಟ್ಟದ ಲೆಗಸಿ ಮಾದರಿಗಳು (ನವೀಕರಣ ಅಗತ್ಯವಿದೆ)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient ನಿಂದ ಬದಲಾಯಿಸು
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True ಬೇಕು

# ಪರೀಕ್ಷಾ ಮೂಲಸೌಕರ್ಯ (ನವೀಕರಣ ಅಗತ್ಯವಿದೆ)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# ವಿಷಯ ಫಿಲ್ಟರ್ ದೋಷ ಬಾಡಿ ಪ್ರವೇಶ (ನವೀಕರಿಸು — ನಿರ್ವಹಣೆ ಬದಲಾಯಿಸಲಾಗಿದೆ)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # ಹಳೆಯ ಏಕವಚನ ರೂಪ — ಈಗ content_filter_results (ಬಹುವಚನ) content_filters ಸರಣಿಯಲ್ಲಿ ಇದೆ

# Chat Completions ಎಂಡ್ಪಾಯಿಂಟ್ ಗೆ ನೇರ HTTP ಕಾಲ್‌ಗಳು (URL ನವೀಕರಿಸಬೇಕು)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### ನಿಯಮಾವಳಿಗಳು (ಪತ್ತೆ ಮತ್ತು ಮರುಬರಹ)

- **ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ ಕ್ಲೈಂಟ್**: `client.chat.completions.create` → `client.responses.create(...)`.

- **ಏಜರ್ ಕ್ಲಯಿಂಟ್ ಕನಸ್ಟ್ರಕ್ಟರ್ಸ್**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **ಟೂಲ್ಸ್**: ಫಂಗ್ಶನ್-ಕಾಲಿಂಗ್ ಟೂಲ್ ವ್ಯಾಖ್ಯಾನಗಳನ್ನು ನೆಸ್ಟೆಡ್ ಫಾರ್ಮ್ಯಾಟ್ (`{"type": "function", "function": {"name": ...}}`) ನಿಂದ ಫ್ಲಾಟ್ Responses ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ (`{"type": "function", "name": ...}`) ಪರಿವರ್ತಿಸು; `tool_choice` ಬಳಸಿ; ಟೂಲ್ ಫಲಿತಾಂಶಗಳನ್ನು `{"type": "function_call_output", "call_id": ..., "output": ...}` ಐಟಮ್‌ಗಳಾಗಿ ಹಿಂದಿರುಗಿಸಿ (`{"role": "tool", ...}` ಅಲ್ಲ).
- **ಟೂಲ ರೌಂಡ್-ಟ್ರಿಪ್ಸ್**: ಮಾದರಿ ಫಂಗ್ಶನ್ ಕಾಲ್‌ಗಳನ್ನು ಹಿಂತಿರುಗಿಸುವಾಗ, ಸಂಭಾಷಣೆಗೆ `response.output` ಐಟಮ್‌ಗಳನ್ನು ಜೋಡಿಸಿ (ಮ್ಯಾನ್ಯುವಲ್ `{"role": "assistant", "tool_calls": [...]}` ಡಿಕ್ಷನರಿ ಅಲ್ಲ), ನಂತರ ಪ್ರತಿ ಫಲಿತಾಂಶಕ್ಕಾಗಿ `function_call_output` ಐಟಮ್‌ಗಳನ್ನು ಸೇರಿಸಿ.
- **ಫ್ಯೂ-ಶಾಟ್ ಟೂಲ್ ಉದಾಹರಣೆಗಳು**: ಸಂಭಾಷಣೆಯಲ್ಲಿ ಹಾರ್ಡ್‌ಕೋಡಡ್ ಟೂಲ್ ಕಾಲ್ ಉದಾಹರಣೆಗಳಿದ್ದರೆ, ಅವುಗಳನ್ನು `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` ಐಟಮ್‌ಗಳಾಗಿ ಪರಿವರ್ತಿಸಿ. IDs `fc_` ಸಂಧಿಯಿಂದ ಆರಂಭವಾಗಬೇಕು.
- **`pydantic_function_tool()`**: ಈ ಸಹಾಯಕ ಈಜ್ಞಾನ ಇನ್ನೂ ಹಳೆಯ ನೆಸ್ಟೆಡ್ ಫಾರ್ಮ್ಯಾಟ್ ಅನ್ನು ರಚಿಸುತ್ತಿದೆ ಮತ್ತು `responses.create()` ಜೊತೆಗೆ **ಅನುಕೂಲವಿಲ್ಲ**. ಕೈಯಿಂದ ಟೂಲ್ ವ್ಯಾಖ್ಯಾನಗಳೊಂದಿಗೆ ಅಥವಾ ಫ್ಲ್ಯಾಟನ್ ಮಾಡಬಹುದಾದ ರ್ಯಾಪರ್‌ನೊಂದಿಗೆ ಬದಲಾಯಿಸಿ.
- **ಮಲ್ಟಿ-ಟರ್ನ್**: ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ ಸಂಭಾಷಣಾ ಇತಿಹಾಸವನ್ನು ಕಾಯ್ದುಕೆಳ್ಳಿ; ಮುಂಚಿನ ಟರ್ನ್‌ಗಳನ್ನು `input` ಐಟಮ್‌ಗಳ ಮೂಲಕ ಪಾಸ್ ಮಾಡಿ.
- **ಫಾರ್ಮ್ಯಾಟಿಂಗ್**: ಚಾಟ್‌ನ ಟಾಪ್- ಲೆವೆಲ್ `response_format` ಅನ್ನು Responses ನಲ್ಲಿ `text.format` ಮೂಲಕ ಬದಲಾಯಿಸಿ. ಕಾನಾನಿಕಲ್ ರೂಪ: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **ಕಂಟೆಂಟ್ ಐಟಮ್‌ಗಳು**: Chats ನಲ್ಲಿ `content[].type: "text"` ಅನ್ನು Responses ನಲ್ಲಿ `content[].type: "input_text"` ಗೆ ಬದಲಾಯಿಸಿ (ಬಳಕೆದಾರ/ಸಿಸ್ಟಮ್ ಟರ್ನ್ಗಳಿಗಾಗಿ).
- **ಇಮೇಜ್ ಕಂಟೆಂಟ್ ಐಟಂಗಳು**: Chats ನಲ್ಲಿ `content[].type: "image_url"` ಅನ್ನು Responses ನಲ್ಲಿ `content[].type: "input_image"` ಗೆ ಬದಲಾಯಿಸಿ. `image_url` ಫೀಲ್ಡ್ ನೆಸ್ಟೆಡ್ ಆಬ್ಜೆಕ್ಟ್ `{"url": "..."}` ನಿಂದ ಫ್ಲಾಟ್ ಸ್ಟ್ರಿಂಗ್ ಆಗಿದೆ. ಮೇ್ಲಿ/ಕೀಳಿಗೆ ಉದಾಹರಣೆಗಳಿಗೆ ಚೀಟ್ ಶೀಟ್ ನೋಡಿ.
- **ಕಾರಣ ಮಾಡಲು ಪ್ರಯತ್ನ**: **ಇದು ಮೂಲ ಕೋಡ್‌ನಲ್ಲಿ ಈಗಾಗಲೇ ಇದ್ದರೆ ಮಾತ್ರ `reasoning` ಅನ್ನು ಸ್ಥಳಾಂತರಿಸಿ**.
- **ಕಂಟೆಂಟ್ ಫಿಲ್ಟರ್ ದೋಷ ನಿರ್ವಹಣೆ**: ದೋಷ ಬಾಡಿ ರಚನೆ ಬದಲಾಗಿದೆ. Chat Completions `error.body["innererror"]["content_filter_result"]` (ಏಕವಚನ) ಬಳಸುತಿದ್ದ; Responses API `error.body["content_filters"][0]["content_filter_results"]` (ಬಹುವಚನ, ಅರೇಯ್ ಒಳಗೆ) ಬಳಸುತ್ತದೆ. `innererror`ಗೆ ಪ್ರವೇಶಿಸುವ ಕೋಡ್ `KeyError` ಉಂಟುಮಾಡುತ್ತದೆ. ಹೊಸ ಹಾದಿಯನ್ನು ಬಳಸಿ ಮರುಬರೆಯಿರಿ.
- **ರಾ HTTP ಕಾಲ್‌ಗಳು**: ಅಪ್ಲಿಕೇಶನ್ ನೇರವಾಗಿ `/openai/deployments/{name}/chat/completions?api-version=...` ಮೂಲಕ ಏಜರ್ OpenAI REST API-ಯನ್ನು ಕರೆ ಮಾಡುವಲ್ಲಿ (requests, httpx ಇತ್ಯಾದಿ ಬಳಸಿಕೊಂಡು), ಇದನ್ನು `/openai/v1/responses` ಗೆ ಮರುಬರೆಯಿರಿ. ವಿನಂತಿ ಬಾಡಿ ಬದಲಾವಣೆ: `messages` → `input`, `max_output_tokens` ಮತ್ತು `store: false` ಸೇರಿಸಿ, `api-version` ಕೇಳಿಕೆ ಪ್ಯಾರಾಮ್ನ್ನು ತೆಗೆದುಹಾಕಿ. ಪ್ರತಿಕ್ರಿಯೆ ಬಾಡಿ ಬದಲಾವಣೆ: `choices[0].message.content` → `output[0].content[0].text` (ಗಮನಿಸಿ: `output_text` SDK ಅನುಕೂಲದ ಸ್ವತ್ತು, ರಾ REST JSON ನಲ್ಲಿ ಇಲ್ಲ).

---

## ಹಂತ 2: ಸ್ಥಳಾಂತರವನ್ನು ಅನ್ವಯಿಸು

### ಸ್ಥಳಾಂತರ ಟಿಪ್ಪಣಿಗಳು (ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ → Responses)

- **ಏಕೆ ಸ್ಥಳಾಂತರ ಮಾಡಬೇಕು**: Responses ಪಠ್ಯ, ಟೂಲ್ಸ್ ಮತ್ತು ಸ್ಟ್ರೀಮಿಂಗ್‌ಗಾಗಿ ಏಕೀಕೃತ API ಆಗಿದ್ದು; Chat Completions ಹಳೆಯದು. GPT-5 සමತೆ, ಉತ್ತಮ ಕಾರ್ಯದಕ್ಷತೆಗೆ Responses ಅಗತ್ಯ.
- **HTTP**: ಏಜರ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ `/openai/deployments/{name}/chat/completions` ನಿಂದ `/openai/v1/responses` ಗೆ ಬದಲಾದಿತ್ತು.
- **ಕ್ಷೇತ್ರಗಳು**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` ಮುಂದೆಯೇ ಇದೆ.
- **ಫಾರ್ಮ್ಯಾಟಿಂಗ್**: `response_format` → `text.format` ಸಮರ್ಪಕ ಆಬ್ಜೆಕ್ಟ್‌ಗಾಗಿ.
- **ಕಂಟೆಂಟ್ ಐಟಂಗಳು**: ಚಾಟ್‌ನ `content[].type: "text"` ಅನ್ನು Responses ನಲ್ಲಿ `content[].type: "input_text"` ಗೆ ಬದಲಾಯಿಸಿ (ಸಿಸ್ಟಮ್/ಬಳಕೆದಾರ ಟರ್ನ್ಗಳಿಗಾಗಿ).
- **ಇಮೇಜ್ ಕಂಟೆಂಟ್ ಐಟಂಗಳು**: ಚಾಟ್‌ನ `content[].type: "image_url"` ಅನ್ನು Responses ನಲ್ಲಿ `content[].type: "input_image"` ಗೆ ಬದಲಾಯಿಸಿ. `image_url` ಕ್ಷೇತ್ರವನ್ನು `{"image_url": {"url": "..."}}` ನಿಂದ `{"image_url": "..."}` ಗೆ ಫ್ಲಾಟನ್ ಮಾಡಿ (ಸರಳ ಸ್ಟ್ರಿಂಗ್ — HTTPS URL ಅಥವಾ `data:image/...;base64,...` ಡೇಟಾ URI).

### ಪರಾಮಿತಿಯ ನಕ್ಷೆ ಸಂಗ್ರಹ

| ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (ಐಟಂಗಳ ಸರಣಿ) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (ಆಬ್ಜೆಕ್ಟ್) |
| `temperature` | `temperature` (ಬದ್ಲಾಗಿಲ್ಲ) |
| `stop` | `stop` (ಬದ್ಲಾಗಿಲ್ಲ) |
| `frequency_penalty` | `frequency_penalty` (ಬದ್ಲಾಗಿಲ್ಲ) |
| `presence_penalty` | `presence_penalty` (ಬದ್ಲಾಗಿಲ್ಲ) |
| `tools` / function-calling | `tools` (ಬದ್ಲಾಗಿಲ್ಲ) |
| `seed` | **ತೆಗೆದುಹಾಕಿ** (ಬೆಂಬಲವಿಲ್ಲ) |
| `store` | `store` (`false` ಗೆ ಹೊಂದಿಸಲಾಗಿದೆ) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (ಫ್ಲಾಟ್ ಸ್ಟ್ರಿಂಗ್) |

ಸಂಪೂರ್ಣ ಹಿಮ್ಮುಖ/ಮುಂಭಾಗದ ಕೋಡ್ ಉದಾಹರಣೆಗಳಿಗೆ, ನೋಡಿ [cheat-sheet.md](./references/cheat-sheet.md).

ಟೆಸ್ಟ್ ಇન્ફ್ರಾಸ್ಟ್ರಕ್ಚರ್ ಸ್ಥಳಾಂತರ (ಮಾಕ್ಸ್, ಸ್ನ್ಯಾಪ್‌ಶಾಟ್‌ಗಳು, ದೃಢೀಕರಣಗಳು)ಗಾಗಿ, ನೋಡಿ [test-migration.md](./references/test-migration.md).

ದೋಷಗಳು ಮತ್ತು ಸಮಸ್ಯೆಗಳು ಕುರಿತು, ನೋಡಿ [troubleshooting.md](./references/troubleshooting.md).

---

## ಡೇಟಾ ಸಂಗ್ರಹಣೆ ಮತ್ತು ಸ್ಥಿತಿ

- Responses ಎಲ್ಲಾ ವಿನಂತಿಗಳ ಮೇಲೆ `store: false` ಅನ್ನು ಹೊಂದಿಸಿ.
- ಹಿಂದಿನ ಸಂದೇಶ IDಗಳು ಅಥವಾ ಸರ್ವರ್-ಸಂಗ್ರಹಿತ ಪರಿಸರಕ್ಕೆ ನಂಬಿಕೆ ಇಡಬೇಡಿ; ಸ್ಥಿತಿಯನ್ನು ಕ್ಲೈಂಟ್ ನಿರ್ವಹಿಸಬೇಕು ಮತ್ತು ಮೆಟಾಡೇಟಾವನ್ನು ಕನಿಷ್ಠಗೊಳಿಸಬೇಕು.

---

## ಸ್ವೀಕೃತಿ ಮಾನದಂಡಗಳು

### ಕೋಡ್-ಮಟ್ಟದ ಗೇಟ್‌ಗಳು (ಎಲ್ಲಾ ಉಲ್ಲೇಖಗಳು ಪಾಸಾಗಬೇಕು)

- [ ] ಸ್ಥಳಾಂತರಿಸಿದ ಕಡತಗಳಲ್ಲಿ `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` ಗೆ ಶೂನ್ಯ ಹೊಂದಾಣಿಕೆ.
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` ಗೆ ಶೂನ್ಯ ಹೊಂದಾಣಿಕೆ — ಎಲ್ಲಾ ಕನಸ್ಟ್ರಕ್ಟರ್ಸ್ v1 ಎಂಡ್‌ಪಾಯಿಂಟ್‌ggಳನ್ನು ಬಳಸುತ್ತಿವೆ `OpenAI`/`AsyncOpenAI`.
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` ಗೆ ಶೂನ್ಯ ಹೊಂದಾಣಿಕೆ — GitHub ಮಾದರಿ ಕೋಡಿನ ದಾರಿಗಳನ್ನು ತೆಗೆದುಹಾಕಲಾಗಿದೆ.
- [ ] `rg "OpenAIChatCompletionClient"` ಗೆ ಶೂನ್ಯ ಹೊಂದಾಣಿಕೆ — MAF 1.0.0+ ಕೋಡ್ `OpenAIChatClient` (Responses API ಬಳಕೆ ಮಾಡುತ್ತದೆ) ಬಳಸುತ್ತದೆ. 1.0.0 ಮುಂಚಿನಲ್ಲಿ, `agent-framework-openai>=1.0.0` ಗೆ ನವೀಕರಣ ಮಾಡಿ.
- [ ] ಎಲ್ಲಾ `ChatOpenAI(...)` ಕರೆಗಳಿಗೆ `use_responses_api=True` ಸೇರಿಸಲಾಗಿದೆ.
- [ ] `rg "choices\[0\]"` ಗೆ ಶೂನ್ಯ ಹೊಂದಾಣಿಕೆ — ಪ್ರತಿಕ್ರಿಯೆ ಪ್ರವೇಶ ಎಲ್ಲಾ `resp.output_text` ಅಥವಾ Responses output schema ನ್ನು ಬಳಸುತ್ತದೆ.
- [ ] ಟಾಪ್ ಲೆವೆಲ್‌ನಲ್ಲಿ `response_format` ಇಲ್ಲ; ಎಲ್ಲಾ ರಚಿತ आउट್ಪುಟ್ `text={"format": {...}}` ಬಳಕೆ ಮಾಡುತ್ತದೆ.
- [ ] `requirements.txt` ಅಥವಾ `pyproject.toml` ನಲ್ಲಿ `openai>=1.108.1` ಮತ್ತು `azure-identity`; ಅವಲಂಬನೆಗಳು ಮರುಸ್ಥಾಪಿತಗೊಂಡಿವೆ.
- [ ] ಪ್ರತಿ `responses.create` ಕರೆಗೆ `store=False` ಹೊಂದಿಸಲಾಗಿದೆ.
- [ ] ಕ್ಲಯಿಂಟ್ ಕನಸ್ಟ್ರಕ್ಷನ್‌ನಲ್ಲಿ `api_version` ಇಲ್ಲ; `AZURE_OPENAI_API_VERSION` ಪರಿಸರ ಫೈಲ್‌ಗಳು ಮತ್ತು ಮೂಲಸೌಕರ್ಯದಿಂದ ತೆಗೆದುಹಾಕಲಾಗಿದೆ.

### ಟೆಸ್ಟ್ ಮೂಲಸೌಕರ್ಯ ಗೇಟ್‌ಗಳು (ಎಲ್ಲಾ ಪಾಸಾಗಬೇಕು)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` ಗೆ ಶೂನ್ಯ ಹೊಂದಾಣಿಕೆ.
- [ ] `rg "_azure_ad_token_provider" tests/` ಗೆ ಶೂನ್ಯ ಹೊಂದಾಣಿಕೆ — ದೃಢೀಕರಣಗಳು `isinstance(client, AsyncOpenAI)` ಅಥವಾ `base_url` ಪರಿಶೀಲಿಸುತ್ತವೆ.
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` ಗೆ ಶೂನ್ಯ ಹೊಂದಾಣಿಕೆ — ಏಜರ್-ನಿರ್ದಿಷ್ಟ ಫಿಲ್ಟರ್ ಮಾಕ್‌ಗಳನ್ನು ತೆಗೆದುಹಾಕಲಾಗಿದೆ.
- [ ] ಮಾಕ್ ಫಿಕ್ಸ್ಚರ್‌ಗಳು `kwargs.get("input")` ಬಳಸುತ್ತವೆ, `kwargs.get("messages")` ಅಲ್ಲ.
- [ ] ಸ್ನ್ಯಾಪ್‌ಶಾಟ್ / ಗೋಲ್ಡನ್ ಫೈಲ್‌ಗಳು Responses ಸ್ಟ್ರೀಮಿಂಗ್ ರೂಪಕ್ಕೆ ನವೀಕರಿಸಲಾಗಿದೆ (`choices[0]`, `function_call`, `logprobs` ಮುಂತಾದವಿಲ್ಲ).
- [ ] ಎಲ್ಲಾ ಪರೀಕ್ಷಾ ಅಪ್‌ಡೇಟರ ನಂತರ `pytest` ಶೂನ್ಯ ವೈಫಲ್ಯಗಳೊಂದಿಗೆ ಪಾಸಾಗಿದೆ.

### ವರ್ತನೆ ಗೇಟ್‌ಗಳು (ಮಾನವೀಯವಾಗಿ ಪರಿಶೀಲಿಸಬೇಕು ಅಥವಾ ಟೆಸ್ಟ್ ಹಾರ್ನೆಸ್ ಮೂಲಕ)

- [ ] **ಮೂಲ‌ಭೂತ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ**: ನಾನ್-ಸ್ಟ್ರೀಮಿಂಗ್ `responses.create` ಖಾಲಿ ಅಲ್ಲದ `output_text` ಅನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ.
- [ ] **ಸ್ಟ್ರೀಮ್ ಸಮಾನತೆ**: ಮೂಲ ಕೋಡ್ ಸ್ಟ್ರೀಮಿಂಗ್ ಬಳಕೆ ಮಾಡಿತಾದರೆ, ಸ್ಥಳಾಂತರಿತ ಕೋಡ್ ಸ್ಟ್ರೀಮ್ ಮಾಡಿ, ಮತ್ತು ಖಾಲಿ ಇಲ್ಲದ ಡೆಲ್ಟಾಗಳೊಂದಿಗೆ `response.output_text.delta` ಇವೆಂಟ್ಸ್ ನೀಡುತ್ತದೆ.
- [ ] **ರಚಿತ ಔಟ್‌ಪುಟ್**: `text.format` ಮತ್ತು `json_schema` ಬಳಕೆ ಮಾಡಿತಾದರೆ, `json.loads(resp.output_text)` ಯಶಸ್ವಿಯಾಗುತ್ತದೆ ಮತ್ತು ಸ್ಕೀಮಾ ಜೊತೆಗೆ ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ.
- [ ] **ಟೂಲಾ-ಕಾಲ್ ಲೂಪ್**: ಟೂಲ್ಗಳು ಬಳಕೆಯಲ್ಲಿದ್ದರೆ, ಮಾದರಿ ಟೂಲ್ ಕಾಲ್‌ಗಳನ್ನು ಹೊರಹಾಕುತ್ತದೆ, ಅಪ್ಲಿಕೇಶನ್ ಅವುಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ, ಮತ್ತು ನಂತರದ ಕೋರಿಕೆಯಲ್ಲಿ ಅಂತಿಮ `output_text` (ಅನಂತ ಲೂಪ್ ಇಲ್ಲ) ಹಿಂತಿರುಗುತ್ತದೆ.
- [ ] **Async ಸಮಾನತೆ**: `AsyncAzureOpenAI` ಬಳಸಿತಾದರೆ, `AsyncOpenAI` ಸಮಾನವಾದುದು `await` ಜೊತೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ.
- [ ] **ದೋಷ ದರ**: ಸ್ಥಳಾಂತರಕ್ಕೂ ಮುಂಚಿನ ಮೂಲ ಕಡೆಗಾಣಿಕೆಯ ಹೋಲಿಕೆಯಲ್ಲಿ ಯಾವುದೇ ಹೊಸ 400/401/404 ದೋಷಗಳಿಲ್ಲ.

### ವಿತರಣೆಗಳು

- ಸಂಕ್ಷೇಪದಲ್ಲಿ ಸಂಪಾದಿತ ಕಡತಗಳು, ಹಳೆಯ ಮತ್ತು ಹೊಸ legacy ಕால் ಸೈಟ್‌‌ಗಳ ಎಣಿಕೆ, ಮತ್ತು ಮುಂದಿನ ಹಂತಗಳು ಸೇರಿರುತ್ತವೆ.
- ಬದಲಾವಣೆಗಳು ಕಾರ್ಯದ ವೃಕ್ಷ ಸಂಪಾದನೆಗಳಾಗಿವೆ (ಕಮಿಟ್‌ಗಳಲ್ಲ).

---

## SDK ಆವೃತ್ತಿ ಅಗತ್ಯಗಳು

| ಪ್ಯಾಕೇಜ್ | ಕನಿಷ್ಠ ಆವೃತ್ತಿ |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | ಇತ್ತೀಚಿನ (EntraID ಪ್ರಮಾಣೀಕರಣಕ್ಕಾಗಿ) |

---

## ಉಲ್ಲೇಖಗಳು

- [ಚೀಟ್ ಶೀಟ್ — ಎಲ್ಲಾ ಕೋಡ್ ಉದಾಹರಣೆಗಳು](./references/cheat-sheet.md)
- [ಟೆಸ್ಟ್ ಸ್ಥಳಾಂತರ — ಮಾಕ್ಸ್, ಸ್ನ್ಯಾಪ್‌ಶಾಟ್‌ಗಳು, ದೃಢೀಕರಣಗಳು](./references/test-migration.md)
- [ಸಮಸ್ಯೆಗಳ ಪರಿಹಾರ — ದೋಷಗಳು, ಅಪಾಯ ಪಟ್ಟಿ, ಗೊತ್ತುಮಾಡಿಕೆಗಳು](./references/troubleshooting.md)
- [detect_legacy.py — ಸ್ವಯಂಚಾಲಿತ ಸ್ಕ್ಯಾನರ್](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [ಏಜರ್ OpenAI ಪ್ರಾರಂಭಿಕ ಕಿಟ್](https://aka.ms/openai/start)
- [ಏಜರ್ OpenAI Responses API ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [ಏಜರ್ OpenAI API ಆವೃತ್ತಿ ಜೀವಚಕ್ರ](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API ರೆಫರೆನ್ಸ್](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->