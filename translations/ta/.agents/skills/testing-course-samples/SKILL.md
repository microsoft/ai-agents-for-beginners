---
name: testing-course-samples
---
# பாடநெறி மாதிரிகளை சோதனை செய்தல்

Microsoft Foundry / Azure OpenAI அமைப்பின் மீது பாடக் குறிப்புகள் மற்றும் குறியீட்டு மாதிரிகள் இயங்குகிறதா என்றதை சரிபார்க்கவும். ரெப்போவின்
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) இல் ஓர் ரன்னர் உள்ளது,
இது
ஒவ்வொரு Python பாடக் குறிப்பையும் தலைவிதல் இல்லாமல் இயக்கி PASS/FAIL மட்ரிக்ஸை அச்சிடுகிறது.

## எப்போது பயன்படுத்தவேண்டும்
- "எனது Azure சந்தாவுக்குஅனைத்துப் பாடக் குறிப்புகளையும் / மாதிரிகளையும் சரிபார்க்க."
- "பேக்கேஜ்களை மேம்படுத்திய பிறகு அல்லது மாதிரிகளை மாற்றிய பிறகு பாடநெறியை சிகிச்சைச் சோதனை செய்ய."
- "எந்த பாடங்கள் இப்பொழுது உயிருடன் / தோல்வியடைகின்றன?"

AI Smoke Test GitHub செயலிக்கு இதை **பயன்படுத்த வேண்டாம்** (இது *நிகழ்நிலை*
ஹோஸ்ட் செய்யப்பட்ட எஜென்ட்களை சரிபார்க்கிறது — பார்க்க [`tests/README.md`](../../../tests/README.md)). இந்த திறன்
பாடக் குறிப்புகளை உள்ளூர் நடைபெறும் முறையில் இயக்குகிறது.

## முன் தேவைகள் (முதலில் சரிபார்க்கவும்)
1. **Python 3.12+** பாடநெறி சார்புகளில்: `python -m pip install -r requirements.txt`
   கூடுதல் வடிவேலை: `python -m pip install nbconvert ipykernel`.
2. **ரெப்போவின் ரூட்டில் `.env`** (நகலெடுக்க: [`.env.example`](../../../../../.env.example)) குறைந்தது:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry திட்ட முகவரி
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — சலுகையில்லாத வழங்கல் (எ.கா `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) மற்றும் `AZURE_OPENAI_DEPLOYMENT`
     நேரடியாக Azure OpenAI உரையாடும் பாடங்களுக்கு (பாடம் 06, 02-azure-openai, 14 ஹாண்ட்ஓவ்/ஹியூமன்-லூப்).
3. **`az login`** முடிக்கப்பட்டுள்ளது — மாதிரிகள் `AzureCliCredential` (Entra ID, கைமுறையில்லாமல்) மூலம் அங்கீகரிக்கின்றன.
4. மாதிரி வழங்கல் இருக்குமொ என்பதை சரிபார்க்கின்றது:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## சரிபார்ப்பை இயக்குதல்
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
ஸ்கிரிப்ட் இயக்கிய நகல்களை, பாடக்குறிப்புகள் பதிவு கோப்புகளை, மற்றும் `results.json` இனை
`$env:TEMP\aiab-nbval` இல் எழுதுகிறது மற்றும் தோல்விகளின் எண்ணிக்கையுடன் வெளியேறுகிறது.

தற்காலிக தோல்விகள் (பகிர்ந்துள்ள சந்தா HTTP 429 விகித வரம்புகள், சில மற்றும்
`AzureCliCredential` டோக்கன் பிரச்சனைகள், அல்லது காலாவதி) தானாக மீண்டும் முயலப்படுகின்றன
(`-Retries`, இயல்பானது 2, `-RetryDelaySeconds` விலக்கு காலம் உடன், இயல்பானது 20). எதுவும்
மாதிரி வழங்கல் மாற்றமாக 429-இல் இருக்குமானால், சந்தாவின் GlobalStandard
TPM அளவுகோல் (`az cognitiveservices usage list -l <region>`) ஐ சரிபார்க்கவும் — தனிப்பட்ட
வழங்கலின் திறன் உயர்த்துவது சந்தா அளவுகோல் முடங்கும் போது உதவாது.

## முடிவுகளை விளக்குதல்
- `PASS` — பாடக் குறிப்பு முழுமையாக இடையூறு இல்லாமல் ஓடியது.
- `FAIL` — முதலாவது `*Error` / `*Exception` வரி காட்டப்படுகிறது; முழு பின்விசாரணைக்கு பொருத்தமான
  `log_*.txt` ஐ வெளியீடு அடைவில் திறக்கவும்.
- ஒரே பாடக் குறிப்பின் தோல்வி `-Timeout` (ஒரு செல்லுக்கு) மூலம் கட்டுப்படுத்தப்படுகிறது, ஆகவே அடைத்தும்கொள்ளும்
  மனித-மூலமாக இருக்கும் செல்லை `StdinNotImplementedError` போல காட்டுகிறது இடர்பு ஏற்படுத்தாமல்.

## கூடுதல் வளங்கள் தேவையான பாடங்கள் (அவற்றின் இல்லாமல் தோல்வி அடைவினால்)
| பாடம் | கூடுதல் தேவைகள் |
|--------|-------------------|
| 05 ஏஜென்டிக் RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, விசை) — இந்த மனச் சேமிப்பில் தள்ளுபடி பாதை உள்ளது |
| 11 MCP / GitHub | GitHub MCP சேவையகம் + PAT |
| 13 நினைவு (cognee) | `cognee` மாதிரி வழங்குனருடன் அமைக்கப்பட்டது |
| 15 உலாவி பயன்பாடு | Playwright உலாவிகள் நிறுவப்பட்டுள்ளன (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 உள்ளூர் முகவர் | Foundry உள்ளூர் இயக்கி + பதிவிறக்கம் செய்யப்பட்ட Qwen மாதிரி (சாதனத்தில், மேகமல்ல) |
| `*-dotnet-*` பாடக் குறிப்புகள் | .NET Interactive கர்னல் (இயல்புநிலை தவிர்க்கப்படுகிறது; பயன்படுத்த `-IncludeDotnet`) |

## மீளாய்வு அறிக்கை
பாடங்கள் மூலம் குழுவாக்கப்பட்ட PASS/FAIL அட்டவணையாக சுருக்கவும். உண்மையான
சரி செய்ய வேண்டிய பிழைகள் மற்றும் சூழல் குறைவுகளை (Search/Foundry Local/PAT இல்லாமை),
ஒவ்வொரு உண்மையான தோல்விக்கும் தோல்வியடைய `log_*.txt` குறிப்பிடவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->