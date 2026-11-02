---
name: testing-course-samples
---
# ಕೋರ್ಸ್ ಮಾದರಿಗಳನ್ನು ಪರೀಕ್ಷಿಸುವುದು

ಪಾಠದ ನೋಟ್‌ಬುಕುಗಳು ಮತ್ತು ಕೋಡ್ ಮಾದರಿಗಳು ಲೈವ್ Microsoft Foundry / Azure OpenAI ಸೆಟ್‌ಅಪ್ ವಿರುದ್ಧ ಚಾಲನೆಯಲ್ಲಿವೆ ಎಂದು
ಮಾನ್ಯವಿಡಿ. ರೆಪೋದಲ್ಲಿ
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) ನಲ್ಲಿ ಒಂದು ರನ್ನರ್ ಕಳುಹಿಸಲಾಗಿದೆ
ಅದು ಪ್ರತೀ ಪೈಥಾನ್ ನೋಟ್‌ಬುಕ್ ಅನ್ನು ಹೆಡ್‌ಲೆಸ್ ಆಗಿ ಕಾರ್ಯಗತಗೊಳಿಸಿ PASS/FAIL ಮ್ಯಾಟ್ರಿಕ್ಸ್ ಅನ್ನು ಮುದ್ರಿಸುತ್ತದೆ.

## ಯಾವಾಗ ಬಳಸುವುದು
- "ನನ್ನ Azure ಸಬ್ಸ್ಕ್ರಿಪ್‌ಷನ್ ವಿರುದ್ಧ ಎಲ್ಲಾ ನೋಟ್‌ಬುಕ್‌ಗಳು / ಮಾದರಿಗಳನ್ನು ಮಾನ್ಯವಿಡಿ."
- "ಪ್ಯಾಕೇಜುಗಳನ್ನು ಅಪ್‌ಗ್ರೇಡ್ ಮಾಡಿದ ನಂತರ ಅಥವಾ ಮಾದರಿಗಳನ್ನು ಬದಲಾಯಿಸಿದ ನಂತರ ಕೋರ್ಸ್‌ನ್ನು ಸ್ಮೋಕ್-ಟೆಸ್ಟ್ ಮಾಡಿ."
- "ಯಾವ ಪಾಠಗಳು ಇನ್ನೂ ಲೈವ್‌ನಲ್ಲಿ ಪಾಸ್ / ಫೇಲಾಗಿವೆ?"

AI ಸ್ಮೋಕ್ ಟೆಸ್ಟ್ GitHub ಕ್ರಿಯೆ (deploy ಆದುದನ್ನು ಮಾನ್ಯ ಮಾಡುವಂತೆ)ಗಾಗಿ ಇದನ್ನು **ಬಳಸಬೇಡಿ**.
ಹೋಸ್ಟ್ ಮಾಡಿದ ಏಜೆಂಟ್ಗಳು — ನೋಡಿ [`tests/README.md`](../../../tests/README.md)). ಈ ಕೌಶಲ್ಯವು
ನೋಟ್‌ಬುಕ್‌ಗಳನ್ನು ಸ್ಥಳೀಯವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ.

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು (ಮೊದಲು ಪರಿಶೀಲಿಸಿ)
1. **Python 3.12+** ಕೋರ್ಸ್ ಅವಲಂಬನೆಗಳೊಂದಿಗೆ: `python -m pip install -r requirements.txt`
   ಜೊತೆಗೆ ಎಕ್ಸಿಕ್ಯೂಟರ್: `python -m pip install nbconvert ipykernel`.
2. **`.env` ರೆಪೊ ಮೂಲದಲ್ಲಿ** (ನಕಲು ಮಾಡಿ [`.env.example`](../../../../../.env.example)) ಕನಿಷ್ಠ:
   - `AZURE_AI_PROJECT_ENDPOINT` — ಫೌಂಡರಿ ಪ್ರಾಜೆಕ್ಟ್ ಎಂಡ್ಪಾಯಿಂಟ್
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — ಡಿಪ್ರೆಶಿಯೇಟ್ ಆಗದ ನಿಯೋಜನೆ (ಉದಾ: `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) ಮತ್ತು `AZURE_OPENAI_DEPLOYMENT`
     ಆಜೂರ್ ಓಪನ್‌ಎಐ ನೇರವಾಗಿ ಕರೆಮಾಡುವ ಪಾಠಗಳಿಗಾಗಿ (ಪಾಠ 06, 02-azure-openai, 14 ಹ್ಯಾಂಡ್‌ಆಫ್/ಹ್ಯೂಮನ್ಲೂಪ್).
3. **`az login`** പൂರ್ಣಗೊಂಡಿದೆ — ನಮೂನೆಗಳು `AzureCliCredential` (ಎಂಟ್ರಾ ಐಡಿ, ಕೀವಿಲ್ಲದ) ಮೂಲಕ ಪ್ರಮಾಣೀಕರಿಸಿ.
4. ಮಾದರಿ ನಿಯೋಜನೆ ಇರುತ್ತದೆ ಎಂದು ಪರಿಶೀಲಿಸಿ:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## ಮಾನ್ಯತೆ ಚಲಾಯಿಸುವುದು
```powershell
# All Python notebooks (skips .NET, .venv, site-packages, translations, skill assets)
pwsh scripts/validate-notebooks.ps1

# A single lesson, with a longer per-cell timeout
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Just list what would run (no execution)
pwsh scripts/validate-notebooks.ps1 -List

# Explicit interpreter (if `python` is not on PATH, e.g. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
ಸ್ಕ್ರಿಪ್ಟ್ ನಿರ್ವಹಿಸಲಾದ ಪ್ರತಿಗಳನ್ನು, ಪ್ರತಿನೋಟ್‌ಬುಕ್ ಲಾಗ್‌ಗಳನ್ನು ಮತ್ತು `results.json` ಅನ್ನು
`$env:TEMP\aiab-nbval` ಗೆ ಬರೆಯುತ್ತದೆ ಮತ್ತು ವಿಫಲತೆಗಳ ಸಂಖ್ಯೆಯಿಂದ ನಿರ್ಗಮಿಸುತ್ತದೆ.

ತಾತ್ಕಾಲಿಕ ವಿಫಲತೆಗಳು (ಹಂಚಿಕೆಯಾಗಿರುವ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್ HTTP 429 ದರ ಮಿತಿ, ಕೆಲವೊಂದು
`AzureCliCredential` ಟೋಕನ್ ತೊಂದರೆ, ಅಥವಾ ಟೈಮೌಟ್) ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪುನರಾರಂಭವಾಗುತ್ತವೆ
(`-Retries`, ಡೀಫಾಲ್ಟ್ 2, `-RetryDelaySeconds` ಬ್ಯಾಕ್ಓಫ್, ಡೀಫಾಲ್ಟ್ 20). ಒಂದು ಮಾದರಿ ನಿಯೋಜನೆ ನಿಯಮಿತವಾಗಿ 429 ಆಗಿದ್ದರೆ,
ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್‌ನ GlobalStandard TPM ಕ್ವೋಟಾವನ್ನು ಪರಿಶೀಲಿಸಿ (`az cognitiveservices usage list -l <region>`) — ಒಬ್ಬ
ನಿಯೋಜನೆಯ ಸಾಮರ್ಥ್ಯವನ್ನು ಹೆಚ್ಚಿಸುವುದು ಸಹಾಯ ಮಾಡುವುದಿಲ್ಲ, *ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್* ಕ್ವೋಟা ಮುಗಿದಾಗ.


- `PASS` — ನೋಟ್‌ಬುಕ್ ಆರಂಭದಿಂದ ಅಂತಿಮ ತನಕ ದೋಷವಿಲ್ಲದೆ ಓಡಿತು.
- `FAIL` — ಮೊದಲ `*Error` / `*Exception` ಸಾಲು ತೋರಿಸಲಾಗಿದೆ; ಹೊಂದಾಣಿಕೆಯ
  `log_*.txt` ಅನ್ನು ಪೂರ್ಣ ಟ್ರೇಸ್‌ಬ್ಯಾಕ್‌ಗೆ ಔಟ್‌ಪುಟ್ ಡೈರಲ್ಲಿ ತೆರೆಯಿರಿ.
- ಒಬ್ಬ ನೋಟ್‌ಬುಕ್‌ನ одна ವಿಫಲತೆ `-Timeout` (ಪ್ರತಿ ಸೆಲ್) ಮೂಲಕ ಮಿತಿಮೀರುತ್ತದೆ, ಆದ್ದರಿಂದ ಹಂಗ್
  ಮನುಷ್ಯ-ಇನ್-ದ-ಲೂಪ್ ಸೆಲ್ `StdinNotImplementedError` ಆಗಿ ಕಾಣುತ್ತದೆ ಹ್ಯಾಂಗ್ ಆಗುವುದಕ್ಕೆ ಬದಲು.


| ಪಾಠ | ಹೆಚ್ಚುವರಿ ಅವಶ್ಯಕತೆ |
|--------|-------------------|
| 05 ಏಜೆಂಟಿಕ್ RAG | ಆಜೂರ್ AI ಶೋಧನೆ (`AZURE_SEARCH_SERVICE_ENDPOINT`, ಕೀ) — ಈ_MEMORY ಫಾಲ್‌ಬ್ಯಾಕ್ ಮಾರ್ಗವನ್ನು ಹೊಂದಿದೆ |
| 11 MCP / GitHub | GitHub MCP ಸರ್ವರ್ + PAT |
| 13 ಮೆಮೊರಿ (ಕೊಗ್ನಿ) | `cognee` ಮಾದರಿ ಒದಗಿಸುವವರೊಂದಿಗೆ ಸಂರಚಿಸಲಾಗಿದೆ |
| 15 ಬ್ರೌಸರಿನ ಬಳಕೆ | ಪ್ಲೈರೈಟ್ ಬ್ರೌಸರ್‌ಗಳು ಸ್ಥಾಪಿತ (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 ಸ್ಥಳೀಯ ಏಜೆಂಟ್ | ಫೌಂಡರಿ ಸ್ಥಳೀಯ ರನ್‌ಟೈಮ್ + ಡೌನ್‌ಲೋಡ್ ಮಾಡಲಾದ ಕ್ವೆನ್ ಮಾದರಿ (ಡಿವೈಸ್ ಮೇಲೆ, ಕ್ಲೌಡ್ ಇಲ್ಲ) |
| `*-dotnet-*` ನೋಟ್ಬುಕ್‌ಗಳು | .NET ಇಂಟರಾಕ್ಟಿವ್ ಕಣೆಲ್ (ಡೀಫಾಲ್ಟ್‌ನಲ್ಲಿ ಹೊರತುಪಡಿಸಲಾಗಿದೆ; ಉಪಯೋಗಿಸಿ `-IncludeDotnet`) |


## ವರದಿ ಮರುಪಡೆಯುವುದು
ಪಾಠದ ಮೂಲಕ ಗುಂಪುಗೊಳಿಸಿದ PASS/FAIL ಪಟ್ಟಿಯಾಗಿ ಸಾರಾಂಶ ಕೊಡಿ. ನಿಜವಾದ ಹಿಂಬಾಲನೆಗಳನ್ನು ವಿಭಜಿಸಿ  
(ಕೊಡ್/ಕಾನ್ಫಿಗರೇಷನ್ ದೋಷಗಳನ್ನು ಸರಿಪಡಿಸಲು) ಪರಿಸರ ಗಣಕದ ಕೊರತೆಗಳಿಂದ (ಹೊಂದಿಕೆ ಇಲ್ಲದ Search/Foundry Local/PAT),  
ಮತ್ತು ಪ್ರತಿ ನಿಜವಾದ ವಿಫಲತೆಗಾಗಿ ವಿಫಲವಾಗುವ `log_*.txt` ಅನ್ನು ಉಲ್ಲೇಖಿಸಿ.  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->