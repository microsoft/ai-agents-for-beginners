---
name: testing-course-samples
description: Tumia wakati unapoombwa kuthibitisha, kujaribu, kufanya mtihani wa haraka,
  au kuendesha daftari la kozi na mifano ya msimbo dhidi ya usanidi hai wa Microsoft
  Foundry / Azure OpenAI. Inajumuisha usanidi wa mazingira (.env, az login, vifurushi),
  mchezaji wa scripts/validate-notebooks.ps1, kutafsiri matokeo ya PASS/FAIL, na ni
  masomo yapi yanayohitaji rasilimali za ziada (Azure AI Search, GitHub MCP, Foundry
  Local, Playwright).
---
# Kupima Sampuli za Kozi

Thibitisha kuwa daftari za mafunzo na sampuli za msimbo zinafanya kazi dhidi ya
usanidi wa Microsoft Foundry / Azure OpenAI unaoishi. Hifadhidata inaendesha
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) ambayo
inaendesha kila daftari la Python bila kichwa na inachapisha matriki ya PASS/FAIL.

## Wakati wa kutumia
- "Thibitisha daftari zote / sampuli dhidi ya usajili wangu wa Azure."
- "Fanya mtihani mdogo wa kozi baada ya kusasisha vifurushi au kubadilisha mifano."
- "Ni masomo gani bado yanapita / kushindwa kuishi?"

Usitumie hii kwa AI Smoke Test GitHub Action (ambayo inathibitisha mawakala waliowekwa *wazi*
— angalia [`tests/README.md`](../../../tests/README.md)). Ujuzi huu unaendesha daftari
kiasili.

## Masharti ya awali (angalia kwanza)
1. **Python 3.12+** pamoja na tegemezi za kozi: `python -m pip install -r requirements.txt`
   pamoja na mtekelezaji: `python -m pip install nbconvert ipykernel`.
2. **`.env` kwenye mizizi ya hifadhidata** (nakili kutoka [`.env.example`](../../../../../.env.example)) kwa angalau:
   - `AZURE_AI_PROJECT_ENDPOINT` — kiungo cha mradi wa Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — usambazaji usioharibika (mfano `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) na `AZURE_OPENAI_DEPLOYMENT`
     kwa masomo yanayopiga Azure OpenAI moja kwa moja (Somo 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** imekamilika — sampuli zinathibitishwa na `AzureCliCredential` (Entra ID, bila funguo).
4. Thibitisha usambazaji wa mfano uko:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Kuendesha uthibitisho
```powershell
# Vitabu vyote vya Python (huacha .NET, .venv, site-packages, tafsiri, mali za ujuzi)
pwsh scripts/validate-notebooks.ps1

# Somo moja tu, na muda mrefu wa kusubiri kwa kila seli
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Orodhesha tu kile kitakachotekelezwa (bila kuendesha)
pwsh scripts/validate-notebooks.ps1 -List

# Mfasiri waziwazi (ikiwa `python` haipo PATH, mfano lahaja ya Duka la Windows)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skripti inaandika nakala zilizotekelezwa, rekodi za kila daftari, na `results.json` kwenye
`$env:TEMP\aiab-nbval` na inatoka kwa idadi ya kushindwa.

Kushindwa kwa muda mfupi (vizuizi vya kiwango cha HTTP 429 vya usajili wa pamoja, tatizo la
`AzureCliCredential` mara moja kwa wakati, au muda wa kusubiri) hurudishwa moja kwa moja
(`-Retries`, chaguo-msingi 2, na `-RetryDelaySeconds` kwa kuchelewesha, chaguo-msingi 20). Ikiwa
usambazaji wa mfano unapata mara kwa mara 429, angalia malipo ya TPM ya GlobalStandard ya usajili (`az cognitiveservices usage list -l <region>`) —
kuongeza uwezo wa usambazaji mmoja haifai wakati kiwango cha *usajili* kimeisha.


## Kufasiri matokeo
- `PASS` — daftari liliendesha vizuri bila kosa katika seli.
- `FAIL` — mstari wa kwanza wa `*Error` / `*Exception` unaonyeshwa; fungua
  `log_*.txt` inayolingana katika saraka ya matokeo kwa urambazaji kamili.
- Kushindwa kwa daftari moja kuna kikomo cha `-Timeout` (kila seli), hivyo seli inayosumbua
  na mtu anayeingilia inaonyesha kama `StdinNotImplementedError` badala ya kusimamisha.

## Masomo yanayohitaji rasilimali za ziada (inayotarajiwa kushindwa bila hizo)
| Somo | Hitaji Ziada |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, ufunguo) — ina njia mbadala ya kumbukumbu ndani |
| 11 MCP / GitHub | Seva ya MCP ya GitHub + PAT |
| 13 memory (cognee) | `cognee` imewekwa na mwanzilishi wa mfano |
| 15 browser-use | Vivinjari vya Playwright vimewekwa (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + mfano wa Qwen aliyopakuliwa (kifaa, si wingu) |
| daftari za `*-dotnet-*` | Kernel ya .NET Interactive (haijajumuishwa kwa chaguo-msingi; tumia `-IncludeDotnet`) |

## Kuripoti nyuma
Fupisha kama jedwali la PASS/FAIL lililoainishwa kwa somo. Tambua tofauti za kweli
(viholela vya msimbo/usanidi vya kurekebisha) dhidi ya mapungufu ya mazingira (kutokuwepo kwa Search/Foundry Local/PAT),
na taja `log_*.txt` zinazoshindwa kwa kila kushindwa halisi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->