# Kurso paruošimas

## Įvadas

Ši pamoka paaiškins, kaip vykdyti šio kurso kodo pavyzdžius.

## Prisijunkite prie kitų mokinių ir gaukite pagalbos

Prieš pradėdami kopijuoti savo repozitoriją, prisijunkite prie [AI Agents For Beginners Discord kanalo](https://aka.ms/ai-agents/discord), kad gautumėte pagalbos su paruošimu, užduotumėte klausimus apie kursą ar susisiektumėte su kitais mokiniais.

## Nukopijuokite arba šakninę šią repozitoriją

Norėdami pradėti, nukopijuokite arba atšakinkite GitHub repozitoriją. Tai sukurs jūsų kopiją kurso medžiagos, kad galėtumėte vykdyti, testuoti ir koreguoti kodą!

Tai galite padaryti spustelėję nuorodą <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">atšakinti repozitoriją</a>

Dabar turėtumėte turėti savo atšakintą šios kursų versiją šioje nuorodoje:

![Forked Repo](../../../translated_images/lt/forked-repo.33f27ca1901baa6a.webp)

### Paviršutiniškas klonas (rekomenduojama dirbtuvių / Codespaces atvejams)

  > Pilna repozitorija gali būti didelė (~3 GB), kai atsisiunčiate visą istoriją ir visus failus. Jei dalyvausite tik dirbtuvėse arba norite tik keletos pamokų aplankų, paviršutiniškas klonas (arba ribotas klonas) leidžia išvengti didžiojo atsisiuntimo, apribojant istoriją ir/arba apeinant blob'us.

#### Greitas paviršutiniškas klonas — minimali istorija, visi failai

Pakeiskite `<your-username>` žemiau pateiktose komandose savo fork URL (arba uprstream URL, jei norite).

Norėdami nukopijuoti tik naujausią įsipareigojimą (mažas atsisiuntimas):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Norėdami nukopijuoti konkretų šaką:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Dalinis (ribotas) klonas — minimalūs blob'ai + tik pasirinkti aplankai

Tai naudoja dalinį kloną ir sparse-checkout (reikalauja Git 2.25+ ir rekomenduojama moderni Git versija su dalinio klono palaikymu):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pereikite į repozitorijos aplanką:

```bash|powershell
cd ai-agents-for-beginners
```

Tada nurodykite, kuriuos aplankus norite (žemiau pavyzdyje du aplankai):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonavimo ir failų patvirtinimo, jei jums reikia tik failų ir norite atlaisvinti vietos (be git istorijos), ištrinkite repozitorijos metadata (💀negrįžtamai — prarasite visas Git funkcijas: jokių įsipareigojimų, gaudymų, išsiuntimų ar istorijos prieigos).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces naudojimas (rekomenduojama vengti didelių vietinių atsisiuntimų)

- Sukurkite naują Codespace šiai repozitorijai per [GitHub UI](https://github.com/codespaces).  

- Naujo sukurto Codespace terminale paleiskite vieną iš aukščiau pateiktų paviršutiniško/riboto klono komandų, kad į Codespace darbinę vietą atsineštumėte tik reikalingus pamokų aplankus.
- Papildomai: po klonavimo Codespaces pašalinkite .git, kad sutaupytumėte vietos (žr. aukščiau pateiktas pašalinimo komandas).
- Pastaba: jei norite tiesiogiai atidaryti repozitoriją Codespaces (be papildomo klono), atkreipkite dėmesį, kad Codespaces sukurs devcontainer aplinką ir gali sumodeliuoti daugiau, nei reikia. Paviršutiniško klono kopija šviežiame Codespace suteikia daugiau kontrolės disko naudojimui.

#### Patarimai

- Visada pakeiskite klono URL savo fork, jei norite redaguoti/įsipareigoti.
- Jei vėliau reikės daugiau istorijos ar failų, galite juos atsisiųsti arba pakoreguoti sparse-checkout, kad įtrauktumėte papildomus aplankus.

## Kodo vykdymas

Šis kursas siūlo seriją Jupyter užrašų knygelių, kurias galite vykdyti norėdami įgyti praktinės patirties statant AI agentus.

Kodo pavyzdžiai naudoja **Microsoft Agent Framework (MAF)** su `FoundryChatClient`, kuris jungiasi prie **Microsoft Foundry Agent Service V2** (Atsakymų API) per **Microsoft Foundry**.

Visi Python užrašų knygelės pažymėti kaip `*-python-agent-framework.ipynb`.

## Reikalavimai

- Python 3.12+
  - **PASTABA**: Jei neturite įdiegto Python3.12, įsitikinkite, kad jį įdiegėte. Tada sukurkite venv naudodami python3.12, kad būtų įdiegtos tinkamos versijos iš requirements.txt failo.
  
    >Pavyzdys

    Sukurkite Python venv katalogą:

    ```bash|powershell
    python -m venv venv
    ```

    Tada aktyvuokite venv aplinką skirtai platformai:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Jei naudojate .NET pavyzdžius, įsitikinkite, kad įdiegėte [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ar naujesnę versiją. Tada patikrinkite savo įdiegtą .NET SDK versiją:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Reikalinga autentifikacijai. Įdiekite iš [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure prenumerata** — Norint prieiti prie Microsoft Foundry ir Microsoft Foundry Agent Service.
- **Microsoft Foundry projektas** — Projektas su paleistu modeliu (pvz., `gpt-5-mini`). Žr. [1 žingsnis](#1-žingsnis-sukurkite-microsoft-foundry-projektą) žemiau.

Šios repozitorijos šaknyje yra `requirements.txt` failas, kuriame pateikti visi reikalingi Python paketai kodo pavyzdžiams vykdyti.

Juos galite įdiegti vykdydami šią komandą savo terminale repo šaknyje:

```bash|powershell
pip install -r requirements.txt
```

Rekomenduojame sukurti Python virtualią aplinką, kad išvengtumėte konfliktų ir problemų.

## VSCode paruošimas

Įsitikinkite, kad VSCode naudojate tinkamą Python versiją.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ir Microsoft Foundry Agent Service nustatymas

### 1 žingsnis: Sukurkite Microsoft Foundry projektą

Norint vykdyti užrašų knygeles, jums reikia Microsoft Foundry **hub'o** ir **projekto** su paleistu modeliu.

1. Eikite į [ai.azure.com](https://ai.azure.com) ir prisijunkite su savo Azure paskyra.
2. Sukurkite **hub'ą** (arba naudokite jau esantį). Žr.: [Hub išteklių apžvalga](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Hube sukurkite **projektą**.
4. Iš **Models + Endpoints** → **Deploy model** įdiekite modelį (pvz., `gpt-5-mini`).

### 2 žingsnis: Gaukite projekto galutinę taško URL ir modelio įdiegimo pavadinimą

Savo projekte Microsoft Foundry portale:

- **Projekto galinis taškas** — Eikite į **Overview** puslapį ir nukopijuokite galutinę taško URL.

![Project Connection String](../../../translated_images/lt/project-endpoint.8cf04c9975bbfbf1.webp)

- **Modelio įdiegimo pavadinimas** — Eikite į **Models + Endpoints**, pasirinkite įdiegtą modelį ir pažymėkite **Deployment name** (pvz., `gpt-5-mini`).

### 3 žingsnis: Prisijunkite prie Azure su `az login`

Visos užrašų knygelės naudoja **`AzureCliCredential`** autentifikacijai — nereikia valdyti API raktų. Tai reikalauja būti prisijungus per Azure CLI.

1. Jei dar neturite, **įdiekite Azure CLI**: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. Prisijunkite paleisdami:

    ```bash|powershell
    az login
    ```

    Arba jei esate nuotolinėje/Codespace aplinkoje be naršyklės:

    ```bash|powershell
    az login --use-device-code
    ```

3. Jei bus prašoma, **pasirinkite savo prenumeratą** — tą, kurioje yra jūsų Foundry projektas.

4. Patikrinkite, ar esate prisijungę:

    ```bash|powershell
    az account show
    ```

> **Kodėl `az login`?** Užrašų knygelės autentifikuojasi naudodamos `AzureCliCredential` iš `azure-identity` paketo. Tai reiškia, kad jūsų Azure CLI sesija suteikia prisijungimo duomenis — nereikia API raktų ar slaptų duomenų `.env` faile. Tai yra [geriausia saugumo praktika](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portalas → **Models + Endpoints** → jūsų įdiegtas modelis |

Tai viskas daugumai pamokų! Užrašų knygelės automatiškai autentifikuosis per jūsų `az login` sesiją.

### 5 žingsnis: Įdiekite Python priklausomybes

```bash|powershell
pip install -r requirements.txt
```

Rekomenduojame tai vykdyti virtualioje aplinkoje, kurią sukūrėte anksčiau.

## Papildomas paruošimas 5 pamokai (Agentic RAG)

5 pamoka naudoja **Azure AI Search** paieškos-nesustiprintai generacijai. Jei planuojate vykdyti šią pamoką, pridėkite šiuos kintamuosius į savo `.env` failą:

| Kintamasis | Kur rasti |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portalas → jūsų **Azure AI Search** išteklius → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portalas → jūsų **Azure AI Search** išteklius → **Settings** → **Keys** → pirminis administratoriaus raktas |

## Papildomas paruošimas pamokoms, kurios tiesiogiai kviečia Azure OpenAI (6 ir 8 pamokos)

Kai kurios 6 ir 8 pamokų užrašų knygelės tiesiogiai kviečia **Azure OpenAI** (naudodamos **Responses API**), o ne per Microsoft Foundry projektą. Šie pavyzdžiai anksčiau naudojo GitHub Models, kurie yra pasenę (bus nutraukti 2026 m. liepos mėn.) ir nepalaiko Responses API. Jei planuojate vykdyti tuos pavyzdžius, pridėkite šiuos kintamuosius į savo `.env` failą:

| Kintamasis | Kur rasti |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portalas → jūsų **Azure OpenAI** ištekliai → **Keys and Endpoint** → Galinis taškas (pvz. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Įdiegto modelio pavadinimas (pvz., `gpt-5-mini`), kuris palaiko Responses API |
| `AZURE_OPENAI_API_KEY` | Pasirinktinai — tik jei naudojate raktų pagrindu autentifikaciją vietoje `az login` / Entra ID |

> Responses API naudoja stabilų `/openai/v1/` galinį tašką, todėl `api-version` nereikia. Prisijunkite su `az login`, kad naudotumėte saugią, be raktų, Entra ID autentifikaciją.

## Alternatyvus tiekėjas: MiniMax (OpenAI suderinamas)

[MiniMax](https://platform.minimaxi.com/) teikia didelės apimties modelius (iki 204 tūkst. žetonų) per OpenAI suderinamą API. Kadangi Microsoft Agent Framework `OpenAIChatClient` veikia su bet kuriuo OpenAI suderinamu galu, galite naudoti MiniMax kaip tiesioginę alternatyvą Azure OpenAI ar OpenAI.

Pridėkite šiuos kintamuosius į savo `.env` failą:

| Kintamasis | Kur rasti |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API raktais |
| `MINIMAX_BASE_URL` | Naudokite `https://api.minimax.io/v1` (numatytoji reikšmė) |
| `MINIMAX_MODEL_ID` | Naudojamo modelio pavadinimas (pvz., `MiniMax-M3`) |

**Pavyzdiniai modeliai**: `MiniMax-M3` (rekomenduojamas), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (greitesni atsakymai). Modelių pavadinimai ir prieinamumas gali keistis, o prieiga prie konkretaus modelio gali priklausyti nuo jūsų paskyros ar regiono — žiūrėkite [MiniMax Platform](https://platform.minimaxi.com/) aktualų sąrašą. Jei `MiniMax-M3` nėra prieinamas jūsų paskyrai, nustatykite `MINIMAX_MODEL_ID` modeliui, prie kurio turite prieigą (pvz., `MiniMax-M2.7`).

Kodo pavyzdžiai, kuriuose naudojamas `OpenAIChatClient` (pvz., 14 pamokos viešbučio užsakymo darbo eiga), automatiškai atpažins ir naudos jūsų MiniMax konfigūraciją, jei `MINIMAX_API_KEY` yra nustatytas.

## Alternatyvus tiekėjas: Foundry Local (Modelių paleidimas vietoje)

[Foundry Local](https://foundrylocal.ai) yra lengvas vykdymo variklis, kuris atsisiunčia, valdo ir tiekia kalbos modelius **visiškai savo kompiuteryje** per OpenAI suderinamą API — be debesies, be Azure prenumeratos ir be API raktų. Tai puikus pasirinkimas offline vystymui, eksperimentams nepatiriant debesies išlaidų ar duomenų laikymui vietoje.

Kadangi Microsoft Agent Framework `OpenAIChatClient` veikia su bet kuriuo OpenAI suderinamu galu, Foundry Local yra vietinė alternatyva Azure OpenAI.

**1. Įdiekite Foundry Local**

```bash
# Windows operacinė sistema
winget install Microsoft.FoundryLocal

# macOS operacinė sistema
brew install foundrylocal
```

**2. Atsisiųskite ir paleiskite modelį** (tai taip pat paleidžia vietinę paslaugą):

```bash
foundry model list          # žiūrėti turimus modelius
foundry model run phi-4-mini
```

**3. Įdiekite Python SDK** skirtą vietiniam galutiniam taškui atrasti:

```bash
pip install foundry-local-sdk
```

**4. Nustatykite Microsoft Agent Framework naudoti savo vietinį modelį:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Atsisiunčia (jei reikia) ir paleidžia modelį vietoje, tada suranda galinį tašką/prievadą.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # pvz. http://localhost:<port>/v1
    api_key=manager.api_key,        # visada "neprivaloma" Foundry Local atveju
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Pastaba:** Foundry Local pateikia OpenAI suderinamą **Chat Completions** galinį tašką. Naudokite jį vietiniam vystymui ir offline scenarijams. Pilną **Responses API** funkcionalumo rinkinį (valstybines pokalbių grandines, gilų įrankių valdymą, agentų stiliaus vystymą) naudokite **Azure OpenAI** arba **Microsoft Foundry** projektą, kaip parodyta pamokose. Žr. [Foundry Local dokumentaciją](https://foundrylocal.ai) su esamų modelių katalogu ir platformos palaikymu.

## Papildomas paruošimas 8 pamokai (Bing integravimo eiga)


Sąlyginio veikimo užrašų knyga 8 pamokoje naudoja **Bing grounding** per Microsoft Foundry. Jei planuojate vykdyti tą pavyzdį, pridėkite šią kintamąją į savo `.env` failą:

| Kintamasis | Kur jį rasti |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portalas → jūsų projektas → **Management** → **Connected resources** → jūsų Bing jungtis → nukopijuokite jungties ID |

## Trikčių šalinimas

### SSL sertifikato patikros klaidos macOS

Jei naudojate macOS ir gaunate klaidą panašią į:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Tai žinoma Python problema macOS, kai sistemos SSL sertifikatai nėra automatiškai patikimi. Išbandykite šiuos sprendimus eilės tvarka:

**1 variantas: Paleiskite Python „Install Certificates“ scenarijų (rekomenduojama)**

```bash
# Pakeiskite 3.XX į jūsų įdiegtą Python versiją (pvz., 3.12 arba 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**2 variantas: Naudokite `connection_verify=False` savo užrašų knygoje (tik GitHub Models užrašų knygoms)**

6 pamokos užrašų knygoje (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) yra jau įtrauktas užkomentuotas sprendimo būdas. Atkomentuokite `connection_verify=False`, kai kuriate klientą:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Išjunkite SSL patvirtinimą, jei susiduriate su sertifikato klaidomis
)
```

> **⚠️ Įspėjimas:** SSL patikros išjungimas (`connection_verify=False`) sumažina saugumą, nes praleidžiama sertifikato patikra. Naudokite tai tik kaip laikiną sprendimą kūrimo aplinkose, niekada ne gamyboje.

**3 variantas: Įdiekite ir naudokite `truststore`**

```bash
pip install truststore
```

Tada pridėkite tai savo užrašų knygos arba skripto viršuje prieš atlikdami bet kokius tinklo kvietimus:

```python
import truststore
truststore.inject_into_ssl()
```

## Užstrigote?

Jei kyla problemų vykdant šią sąranką, prisijunkite prie mūsų <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> arba <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">sukurkite problemą</a>.

## Kitoji pamoka

Dabar esate pasirengę vykdyti šio kurso kodą. Smagaus mokymosi apie AI Agentų pasaulį!

[Įvadas į AI Agentus ir agentų naudojimo atvejus](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->