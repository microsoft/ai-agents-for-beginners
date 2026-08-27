# Kurso parengimas

## Įvadas

Ši pamoka apžvelgs, kaip vykdyti šio kurso kodo pavyzdžius.

## Prisijunkite prie kitų besimokančiųjų ir gaukite pagalbos

Prieš pradėdami kopijuoti savo repozitoriją, prisijunkite prie [AI Agents For Beginners Discord kanalo](https://aka.ms/ai-agents/discord), kad gautumėte pagalbą dėl parengimo, atsakymus į klausimus apie kursą arba susisiektumėte su kitais besimokančiaisiais.

## Kopijuokite arba šaknykite šią repozitoriją

Norėdami pradėti, prašome nukopijuoti arba šaknyti GitHub Repozitoriją. Tai sukurs jūsų versiją kursų medžiagos, kad galėtumėte vykdyti, testuoti ir koreguoti kodą!

Tai galite padaryti paspaudę nuorodą <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">šeimyniniam repo</a>

Dabar turėtumėte turėti savo šaknį šios medžiagos kurso šioje nuorodoje:

![Forked Repo](../../../translated_images/lt/forked-repo.33f27ca1901baa6a.webp)

### Paviršutiniškas klonas (rekomenduojama dirbtuvėms / Codespaces)

  > Visa repozitorija gali būti didelė (~3 GB), kai atsisiunčiate visą istoriją ir visus failus. Jei lankysite tik dirbtuves arba reikalingos tik kelios pamokų bylos, paviršutiniškas klonas (arba retas klonas) atsisiunčia daug mažiau.

#### Greitas paviršutiniškas klonas — minimaliai istorijos, visi failai

Pakeiskite `<your-username>` žemiau esančiuose komandose su savo šakninės nuorodos URL (arba aukštesniojo URL, jei norite).

Norėdami nukopijuoti tik naujausią pateiktos istorijos įrašą (mažas atsisiuntimas):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Norėdami nukopijuoti tam tikrą šaką:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Dalinis (retas) klonas — minimalūs blobai + tik pasirinkti aplankai

Šis metodas naudoja dalinį kopijavimą ir retą peržiūrą (reikalingas Git 2.25+ ir rekomenduojamas modernus Git su dalinio klonavimo palaikymu):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Eikite į repozitorijos aplanką:

```bash
cd ai-agents-for-beginners
```

Tada nurodykite, kuriuos aplankus norite (žemiau pateiktame pavyzdyje yra du aplankai):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonavimo ir failų patikrinimo, jei jums reikalingi tik failai ir norite atlaisvinti vietos (be git istorijos), prašome ištrinti repozitorijos metaduomenis (💀negrįžtama — prarasite visas Git funkcijas):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Naudojantis GitHub Codespaces (rekomenduojama, kad išvengtumėte didelių vietinių atsisiuntimų)

- Sukurkite naują Codespace šiai repozitorijai per [GitHub UI](https://github.com/codespaces).  

- Naujoje sukurtoje Codespace terminale įvykdykite vieną iš anksčiau nurodytų paviršutiniškų arba retų kopijų komandų, kad atsisiųstumėte tik norimus pamokų aplankus į Codespace darbo aplinką.
- Pasirinktinai: po klonavimo Codespaces viduje pašalinkite .git, kad atlaisvintumėte papildomą vietą (žr. aukščiau nurodytas pašalinimo komandas).
- Pastaba: jei norite atidaryti repozitoriją tiesiogiai Codespaces (be papildomo klonavimo), žinokite, kad Codespaces sukurs devcontainer aplinką ir gali vis tiek įdiegti daugiau nei reikia.

#### Patarimai

- Visada pakeiskite klonavimo URL savo šaknine versija, jei norite redaguoti/ar įsipareigoti.
- Jei vėliau reikės daugiau istorijos ar failų, galite juos gauti ar pakeisti rare-checkout, kad įtrauktumėte papildomus aplankus.

## Kodo vykdymas

Šis kursas siūlo seriją Jupyter sąsiuvinių, kuriuos galite vykdyti, kad įgytumėte praktinės patirties kuriant AI agentus.

Kodo pavyzdžiai naudoja **Microsoft Agent Framework (MAF)** su `FoundryChatClient`, kuris jungiasi prie **Microsoft Foundry Agent Service V2** (Atsakymų API) per **Microsoft Foundry**.

Visi Python sąsiuviniai žymimi `*-python-agent-framework.ipynb`.

## Reikalavimai

- Python 3.12+
  - **PASTABA**: Jei neturite įdiegto Python 3.12, įsitikinkite, kad jį įdiegiate. Tada sukurkite savo venv naudodami python3.12, kad užtikrintumėte teisingas versijas iš requirements.txt failo.
  
    >Pavyzdys

    Sukurkite Python virtualios aplinkos katalogą:

    ```bash
    python -m venv venv
    ```

    Tada aktyvuokite venv aplinką:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Kad naudotumėte pavyzdinius .NET kodus, įsitikinkite, kad įdiegėte [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ar naujesnį. Tada patikrinkite įdiegtos .NET SDK versiją:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — reikalinga autentifikacijai. Įdiekite iš [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure prenumerata** — prieiga prie Microsoft Foundry ir Microsoft Foundry Agent Service.
- **Microsoft Foundry projektas** — projektas su įdiegtu modeliu (pvz., `gpt-5-mini`). Žr. [1 žingsnį](#1-žingsnis-sukurkite-microsoft-foundry-projektą) žemiau.

Šiame repozitorijos šaknyje įtraukėme `requirements.txt` failą, kuriame yra visi reikalingi Python paketai kodo pavyzdžiams vykdyti.

Juos galite įdiegti vykdydami šią komandą savo terminale repozitorijos šaknyje:

```bash
pip install -r requirements.txt
```

Rekomenduojame sukurti Python virtualią aplinką, kad išvengtumėte konfliktų ir klaidų.

## VSCode parengimas

Įsitikinkite, kad VSCode naudojate tinkamą Python versiją.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ir Microsoft Foundry Agent Service parengimas

### 1 žingsnis: Sukurkite Microsoft Foundry projektą

Norėdami vykdyti sąsiuvinius, jums reikalingas Microsoft Foundry **hub** ir **projektas** su įdiegtu modeliu.

1. Eikite į [ai.azure.com](https://ai.azure.com) ir prisijunkite naudodami savo Azure paskyrą.
2. Sukurkite **hub** (arba naudokite jau esamą). Žr.: [Hub resursų apžvalga](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Hub viduje sukurkite **projektą**.
4. Įdiekite modelį (pvz., `gpt-5-mini`) per **Models + Endpoints** → **Deploy model**.

### 2 žingsnis: Gaukite savo projekto endpoint ir modelio diegimo pavadinimą

Iš savo projekto Microsoft Foundry portale:

- **Projekto endpoint** — eikite į **Overview** puslapį ir nukopijuokite endpoint URL.

![Project Connection String](../../../translated_images/lt/project-endpoint.8cf04c9975bbfbf1.webp)

- **Modelio diegimo pavadinimas** — eikite į **Models + Endpoints**, pasirinkite įdiegtą modelį ir užsirašykite **Deployment name** (pvz., `gpt-5-mini`).

### 3 žingsnis: Prisijunkite prie Azure su `az login`

Dauguma sąsiuvinių autentifikuojasi per jūsų **Azure CLI prisijungimą** — naudojant `AzureCliCredential` arba `DefaultAzureCredential` (abu paima jūsų `az login` sesiją) iš `azure-identity` paketo — todėl nereikia API raktų. Keletas pamokų ir pasirenkamų integracijų naudoja API raktus; patikrinkite kiekvienos pamokos išankstinius reikalavimus dėl papildomų aplinkos kintamųjų. Tam reikia būti prisijungus per Azure CLI.

1. **Įdiekite Azure CLI**, jei dar neturite: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prisijunkite** vykdydami:

    ```bash
    az login
    ```

    Arba jei esate nuotolinėje/Codespace aplinkoje be naršyklės:

    ```bash
    az login --use-device-code
    ```

3. **Pasirinkite savo prenumeratą**, jei prašoma — pasirinkite tą, kurioje yra jūsų Foundry projektas.

4. **Patikrinkite**, ar esate prisijungę:

    ```bash
    az account show
    ```

> **Kodėl `az login`?** Sąsiuviniai autentifikuojasi naudodami `AzureCliCredential` (arba `DefaultAzureCredential`, kuris taip pat paima jūsų Azure CLI prisijungimą) iš `azure-identity` paketo. Tai reiškia, kad jūsų Azure CLI sesija suteikia prisijungimo duomenis — jokie API raktai ar slapti žodžiai nenaudojami `.env` faile. Tai yra [geriausia saugumo praktika](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### 4 žingsnis: Sukurkite savo `.env` failą

Nukopijuokite pavyzdinį failą:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Atidarykite `.env` ir užpildykite šias dvi reikšmes:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Kintamasis | Kur rasti |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portalas → jūsų projektas → **Overview** puslapis |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portalas → **Models + Endpoints** → jūsų įdiegto modelio pavadinimas |

Tai tiek daugumai pamokų! Sąsiuviniai automatiškai autentiškuosis per jūsų `az login` sesiją.

### 5 žingsnis: Įdiekite Python priklausomybes

```bash
pip install -r requirements.txt
```

Rekomenduojame vykdyti tai virtualioje aplinkoje, kurią sukūrėte anksčiau.

## Pasirinktinai: Azure AI Search parengimas (Pamokos 5 ir 16)

Pamokos 5 (Agentic RAG) ir pamokos 16 sąsiuviniai veikia tiesiogiai su **atminties pagrindu veikiančia žinių baze** — nereikia papildomų Azure resursų. Jei norite naudoti tikrą **Azure AI Search** indeksą, atkreipkite dėmesį, kad **pamoka 16 šiuo metu naudoja autentifikaciją su raktu**: ji pereina nuo atminties pagrindo paieškos prie Azure AI Search tik jei **abu** `AZURE_SEARCH_SERVICE_ENDPOINT` **ir** `AZURE_SEARCH_API_KEY` yra nustatyti, kitu atveju lieka prie atminties pagrindo paieškos — taigi, kad paleistumėte su tikru indeksu, turite nurodyti ir administratoriaus raktą. Be rakto autentifikacija su Microsoft Entra ID (RBAC) yra rekomenduojamasis būdas jūsų pačių produkciniam kodui, suderintas su `az login` srautu, naudojamu visur kitur šiame kurse.

Toliau pateikti RBAC žingsniai taikomi šios parengimo vadovo pavyzdžiams ir jūsų pačių kodui. Jie neįjungia autentifikacijos be rakto pamokoje 16; pamoka 16 vis dar reikalauja tiek endpoint, tiek administratoriaus rakto Azure AI Search naudojimui.

1. **Įjunkite vaidmenimis pagrįstą prieigą** savo paieškos paslaugoje:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Priskirkite sau reikiamus vaidmenis** (kurkite/kraukite indeksus ir užklausas):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Pridėkite endpoint** į savo `.env` failą:

| Kintamasis | Kur rasti |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portalas → jūsų **Azure AI Search** resursas → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Reikalinga (su endpoint) Azure AI Search įjungimui pamokoje 16, kuri naudoja autentifikaciją su raktu. Azure portalas → **Settings** → **Keys** → pagrindinis administratoriaus raktas |

> **Kodėl be rakto?** Administratoriaus raktai suteikia pilną rašymo prieigą prie jūsų paieškos paslaugos ir gali nutekėti per `.env` failus. Naudojantis RBAC, vietoje to yra naudojamas jūsų `az login` identitetas — tas pats be rakto Entra ID modelis, kurį naudoja kurso sąsiuviniai (naudojant `AzureCliCredential` / `DefaultAzureCredential`). Žr. [Prisijungimas prie Azure AI Search naudojant vaidmenis](https://learn.microsoft.com/azure/search/search-security-rbac).

Pilnas indekso kūrimo pavyzdžių Python ir .NET rasite [Azure AI Search parengimo vadove](./AzureSearch.md).

## Papildomas parengimas pamokoms, kurios tiesiogiai kviečia Azure OpenAI (Pamokos 6 ir 8)

Kai kurie sąsiuviniai pamokose 6 ir 8 tiesiogiai kviečia **Azure OpenAI** (naudodami **Responses API**) vietoje Microsoft Foundry projekto. Šie pavyzdžiai anksčiau naudojo GitHub Modelius, kurie yra pasenę ir nepalaiko Responses API. Pridėkite šiuos kintamuosius į savo `.env` failą:

| Kintamasis | Kur rasti |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portalas → jūsų **Azure OpenAI** resursas → **Keys and Endpoint** → Endpoint (pvz., `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Įdiegto modelio pavadinimas (pvz., `gpt-5-mini`), palaikantis Responses API |
| `AZURE_OPENAI_API_KEY` | Pasirinktinai — tik jei naudojate autentifikaciją su raktu vietoje `az login` / Entra ID |

> Responses API naudoja stabilų `/openai/v1/` endpointą, todėl nereikia `api-version`. Prisijunkite su `az login`, kad naudotumėte autentifikaciją be rakto per Entra ID.

## Alternatyvus tiekėjas: MiniMax (OpenAI suderinamas)

[MiniMax](https://platform.minimaxi.com/) teikia didelės apimties kontekstinius modelius (iki 204K žetonų) per OpenAI suderinamą API. Kadangi Microsoft Agent Framework `OpenAIChatClient` veikia su bet kuriuo OpenAI suderinamu endpointu, galite naudoti MiniMax kaip alternatyvą pamokose, kuriose naudojamas `OpenAIChatClient`.

Pridėkite šiuos kintamuosius į savo `.env` failą:

| Kintamasis | Kur rasti |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platforma](https://platform.minimaxi.com/) → API raktai |
| `MINIMAX_BASE_URL` | Naudokite `https://api.minimax.io/v1` (numatytoji reikšmė) |
| `MINIMAX_MODEL_ID` | Modelio pavadinimas naudoti (pvz., `MiniMax-M3`) |

**Pavyzdiniai modeliai**: `MiniMax-M3` (rekomenduojama), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (greitesnės reakcijos). Modelių pavadinimai ir prieinamumas gali keistis, o prieiga prie tam tikro modelio gali priklausyti nuo jūsų paskyros.

Kodo pavyzdžiai, naudojantys `OpenAIChatClient` (pvz., pamokos 14 viešbučių užsakymo darbo eiga) automatiškai aptiks ir naudos jūsų MiniMax konfigūraciją, kai bus nustatytas `MINIMAX_API_KEY`.


## Alternatyvus teikėjas: Foundry Local (Modelių vykdymas įrenginyje)

[Foundry Local](https://foundrylocal.ai) yra lengvas veikimo laikas, kuris atsisiunčia, valdo ir aptarnauja kalbos modelius **visiškai jūsų pačių mašinoje** per OpenAI suderinamą API — nereikia debesies.

Kadangi Microsoft Agent Framework `OpenAIChatClient` veikia su bet kuriuo OpenAI suderinamu tašku, Foundry Local yra vietinė alternatyva Azure OpenAI.

**1. Įdiekite Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Atsisiųskite ir paleiskite modelį** (tai taip pat paleidžia vietinę paslaugą):

```bash
foundry model list          # peržiūrėti prieinamus modelius
foundry model run phi-4-mini
```

**3. Įdiekite Python SDK** skirtą vietiniam taškui atrasti:

```bash
pip install foundry-local-sdk
```

**4. Nustatykite Microsoft Agent Framework naudoti jūsų vietinį modelį:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Atsisiunčia (jei reikalinga) ir aptarnauja modelį vietoje, tada aptinka galinį tašką/prievadą.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # pvz. http://localhost:<port>/v1
    api_key=manager.api_key,        # visada "nereikalinga" Foundry Local atveju
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Pastaba:** Foundry Local suteikia OpenAI suderinamą **Chat Completions** galinį tašką. Naudokite jį vietiniam kūrimui ir neprisijungus. Norėdami pilno **Responses API** funkcionalumo (būseniškos pokalbių seka ir kt.), naudokite Azure OpenAI arba Microsoft Foundry projektą.

## Papildomas pasirengimas 8 pamokai (Bing žemėlapio darbas)

Sąlyginio darbo knyga 8 pamokoje naudoja **Bing grounding** per Microsoft Foundry. Jei planuojate paleisti šį pavyzdį, pridėkite šį kintamąjį į savo `.env` failą:

| Kintamasis | Kur rasti |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portalas → jūsų projektas → **Management** → **Connected resources** → jūsų Bing jungtis → nukopijuokite jungties ID |

## Problemų šalinimas

### SSL sertifikato patvirtinimo klaidos macOS

Jei naudojatės macOS ir gaunate tokią klaidą:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Tai žinoma problema su Python macOS, kai sistemos SSL sertifikatai nėra automatiškai patikimi. Išbandykite šiuos sprendimus tvarka:

**1 variantas: Paleiskite Python Install Certificates scenarijų (rekomenduojama)**

```bash
# Pakeiskite 3.XX savo įdiegta Python versija (pvz., 3.12 arba 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**2 variantas: Naudokite `connection_verify=False` savo darbo knygoje (tik GitHub Models knygoms)**

6 pamokos darbo knygoje (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) jau yra pažymėtas sprendimas. Išskirkite `connection_verify=False`, kai susiduriate su sertifikato klaidomis:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Išjunkite SSL patvirtinimą, jei susiduriate su sertifikato klaidomis
)
```

> **⚠️ Įspėjimas:** Išjungti SSL patvirtinimą (`connection_verify=False`) sumažina saugumą, nes praleidžiama sertifikato patikrą. Naudokite tai tik kaip laikinas kūrimo metu. Niekada nenaudokite gamyboje.

**3 variantas: Įdiekite ir naudokite `truststore`**

```bash
pip install truststore
```

Tada pridėkite tai savo darbo knygos ar scenarijaus pradžioje prieš atliekant bet kokius tinklo kvietimus:

```python
import truststore
truststore.inject_into_ssl()
```

## Užstrigote kur nors?

Jei turite kokių nors problemų paleisdami šį pasirengimą, prisijunkite prie mūsų <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI bendruomenės Discord</a> arba <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">sukurkite problemą</a>.

## Kita pamoka

Dabar esate pasiruošę paleisti šio kurso kodą. Sėkmės mokantis apie AI agentų pasaulį!

[Įvadas į AI agentus ir agentų naudojimo atvejus](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->