# Kurso paruošimas

## Įvadas

Šiame pamokoje aptarsime, kaip paleisti šio kurso kodo pavyzdžius.

## Prisijunkite prie kitų mokinių ir gaukite pagalbos

Prieš pradėdami klonuoti savo repozitoriją, prisijunkite prie [AI Agents For Beginners Discord kanalo](https://aka.ms/ai-agents/discord), kad gautumėte pagalbą dėl paruošimo, užduotumėte klausimus apie kursą ar susisiektumėte su kitais mokiniais.

## Klonuokite arba forkuokite šią repozitoriją

Pradėkite klonuodami arba forkuodami GitHub repozitoriją. Tai leis sukurti savo kurso medžiagos kopiją, kad galėtumėte paleisti, testuoti ir keisti kodą!

Tai galima padaryti paspaudus nuorodą <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a>

Dabar turėtumėte turėti savo forkinę šio kurso versiją šiame lange:

![Forked Repo](../../../translated_images/lt/forked-repo.33f27ca1901baa6a.webp)

### Paviršutiniškas klonavimas (rekomenduojama dirbtuvėms / Codespaces)

  > Pilna repozitorija gali užimti daug vietos (~3 GB), jei atsisiunčiate visą istoriją ir visus failus. Jei dalyvaujate tik dirbtuvėse arba jums reikia tik kelių pamokų aplankų, paviršutiniškas klonavimas (arba retas klonavimas) sumažina atsisiuntimą sutrumpindamas istoriją ir/arba praleisdamas blobus.

#### Greitas paviršutiniškas klonavimas — minimali istorija, visi failai

Pakeiskite `<your-username>` žemiau pateiktose komandose į savo fork URL (arba į upstream URL, jei norite).

Norėdami klonuoti tik naujausią pakeitimų istoriją (mažas atsisiuntimas):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Norėdami klonuoti konkretų šakos variantą:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Dalinis (retas) klonavimas — minimalūs blobai + tik pasirinkti aplankai

Tai naudoja dalinį klonavimą ir sparse-checkout (reikalauja Git 2.25+ ir rekomenduojamas šiuolaikinis Git su dalinio klonavimo palaikymu):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Eikite į repozitorijos aplanką:

```bash|powershell
cd ai-agents-for-beginners
```

Tuomet pasirinkite, kuriuos aplankus norite (žemiau pavyzdyje rodomi du aplankai):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonavimo ir failų patikrinimo, jei jums reikia tik failų ir norite atlaisvinti vietos (be git istorijos), ištrinkite repozitorijos metaduomenis (💀negrįžtama – prarasite visas Git funkcijas: jokio commit, pull, push ar istorijos prieigos).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Naudojant GitHub Codespaces (rekomenduojama išvengti didelių vietinių atsisiuntimų)

- Sukurkite naują Codespace šiai repozitorijai per [GitHub UI](https://github.com/codespaces).

- Naujojo codespace terminale paleiskite vieną iš aukščiau pateiktų paviršutiniško arba reto klonavimo komandų, kad įtrauktumėte tik reikalingus pamokų aplankus į Codespace darbo aplinką.
- Pasirinktinai: po klonavimo Codespaces pašalinkite .git, kad atlaisvintumėte daugiau vietos (žr. aukščiau pateiktas pašalinimo komandas).
- Pastaba: jei norite tiesiogiai atidaryti repozitoriją Codespaces (be papildomo klonavimo), žinokite, kad Codespaces sukonstruos devcontainer aplinką ir gali paruošti daugiau nei jums reikia. Paviršutiniška klonavimo kopija šviežioje Codespace suteikia daugiau kontrolės disko naudojimui.

#### Patarimai

- Visada pakeiskite klonavimo URL į savo fork, jei norite redaguoti/commituoti.
- Jei vėliau prireiks daugiau istorijos ar failų, galite juos atsisiųsti arba koreguoti sparse-checkout, kad įtrauktumėte papildomus aplankus.

## Kodo paleidimas

Šis kursas siūlo eilę Jupyter bloknotų, kuriuos galite paleisti, kad įgytumėte praktinės patirties kuriant AI agentus.

Kodo pavyzdžiai naudoja **Microsoft Agent Framework (MAF)** kartu su `FoundryChatClient`, kuris jungiasi prie **Microsoft Foundry Agent Service V2** (Responses API) per **Microsoft Foundry**.

Visi Python bloknotai pažymėti pavadinimu `*-python-agent-framework.ipynb`.

## Reikalavimai

- Python 3.12+
  - **PASTABA**: Jei neturite įdiegto Python3.12, būtinai jį įdiekite. Tada kurkite savo virtualią aplinką naudodami python3.12, kad būtų įdiegtos tinkamos versijos iš requirements.txt failo.
  
    >Pavyzdys

    Sukurkite Python venv katalogą:

    ```bash|powershell
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

- .NET 10+: Norint paleisti pavyzdžių kodus naudojant .NET, būtinai įdiekite [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ar naujesnę versiją. Tada patikrinkite įdiegtą .NET SDK versiją:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Reikalinga autentifikacijai. Įdiekite iš [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure prenumerata** — Norint pasiekti Microsoft Foundry ir Microsoft Foundry Agent Service.
- **Microsoft Foundry projektas** — Projektas su išdiegta modeliu (pvz., `gpt-4.1-mini`). Žr. [1 žingsnį](#1-žingsnis-sukurkite-microsoft-foundry-projektą) žemiau.

Šios repozitorijos šaknyje yra `requirements.txt` failas, kuriame pateikti visi reikalingi Python paketai kodo pavyzdžiams paleisti.

Juos galite įdiegti paleidę šią komandą terminale repozitorijos šaknyje:

```bash|powershell
pip install -r requirements.txt
```

Rekomenduojame sukurti Python virtualią aplinką, kad išvengtumėte konfliktų ir problemų.

## VSCode paruošimas

Įsitikinkite, kad VSCode naudojate tinkamą Python versiją.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ir Microsoft Foundry Agent Service paruošimas

### 1 žingsnis: sukurkite Microsoft Foundry projektą

Norėdami naudoti bloknotus, jums reikia Microsoft Foundry **hub'o** ir **projekto** su išdiegta modeliu.

1. Eikite į [ai.azure.com](https://ai.azure.com) ir prisijunkite su savo Azure paskyra.
2. Sukurkite **hub'ą** (arba naudokite esamą). Žr.: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Hub'e sukurkite **projektą**.
4. Išdiekite modelį (pvz., `gpt-4.1-mini`) iš **Models + Endpoints** → **Deploy model**.

### 2 žingsnis: gaukite savo projekto galutinį tašką ir modelio diegimo pavadinimą

Savo projekte Microsoft Foundry portale:

- **Project Endpoint** — Eikite į **Overview** puslapį ir nukopijuokite galutinio taško URL.

![Project Connection String](../../../translated_images/lt/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Eikite į **Models + Endpoints**, pasirinkite savo išdiegtą modelį ir užsirašykite **Deployment name** (pvz., `gpt-4.1-mini`).

### 3 žingsnis: prisijunkite prie Azure su `az login`

Visi bloknotai naudoja **`AzureCliCredential`** autentifikacijai – nereikia valdyti API raktų. Tai reikalauja, kad būtumėte prisijungę per Azure CLI.

1. **Įdiekite Azure CLI**, jei dar neturite: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prisijunkite** paleisdami:

    ```bash|powershell
    az login
    ```

    Arba, jei esate nuotolinėje/Codespace aplinkoje be naršyklės:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Pasirinkite prenumeratą**, jei bus paprašyta – pasirinkite tą, kurioje yra jūsų Foundry projektas.

4. **Patikrinkite**, ar esate prisijungę:

    ```bash|powershell
    az account show
    ```

> **Kodėl `az login`?** Bloknotai autentifikuojasi naudodami `AzureCliCredential` iš `azure-identity` paketo. Tai reiškia, kad jūsų Azure CLI sesija suteikia kredencialus – nereikia API raktų ar slaptų duomenų `.env` faile. Tai yra [saugaus naudojimo praktika](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### 4 žingsnis: sukurkite `.env` failą

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Kintamasis | Kur rasti |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → jūsų projektas → **Overview** puslapis |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → jūsų išdiegtas modelio pavadinimas |

Tai tiek daugumai pamokų! Bloknotai automatiškai autentifikuosis per jūsų `az login` sesiją.

### 5 žingsnis: įdiekite Python priklausomybes

```bash|powershell
pip install -r requirements.txt
```

Rekomenduojame tai paleisti virtualioje aplinkoje, kurią sukūrėte anksčiau.

## Papildomas paruošimas 5 pamokai (Agentic RAG)

5 pamoka naudoja **Azure AI Search** retrieval-augmented generation (paieškos papildytą generavimą). Jei planuojate vykdyti tą pamoką, pridėkite šiuos kintamuosius į `.env` failą:

| Kintamasis | Kur rasti |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portalas → jūsų **Azure AI Search** išteklius → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portalas → jūsų **Azure AI Search** išteklius → **Settings** → **Keys** → pagrindinis administratoriaus raktas |

## Papildomas paruošimas pamokoms, kurios naudoja tiesiogiai Azure OpenAI (pamokos 6 ir 8)

Kai kurie 6 ir 8 pamokų bloknotai tiesiogiai kviečia **Azure OpenAI** (naudodami **Responses API**), o ne eina per Microsoft Foundry projektą. Šie pavyzdžiai anksčiau naudojo GitHub Models, kurie yra atsisakomi (išeina 2026 m. liepos mėn.) ir nepalaiko Responses API. Jei planuojate vykdyti tuos pavyzdžius, pridėkite šiuos kintamuosius į `.env` failą:

| Kintamasis | Kur rasti |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portalas → jūsų **Azure OpenAI** išteklius → **Keys and Endpoint** → Endpoint (pvz., `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Išdiegtas modelio pavadinimas (pvz., `gpt-4.1-mini`), palaikantis Responses API |
| `AZURE_OPENAI_API_KEY` | Pasirinktinai — tik jei naudojate raktų autentifikaciją vietoje `az login` / Entra ID |

> Responses API naudoja stabilų `/openai/v1/` galutinį tašką, todėl nereikia `api-version`. Prisijunkite su `az login`, kad naudotumėte be rakto Entra ID autentifikaciją.

## Alternatyvus teikėjas: MiniMax (OpenAI suderinamas)

[MiniMax](https://platform.minimaxi.com/) teikia didelės apimties kontekstinius modelius (iki 204K žetonų) per OpenAI suderinamą API. Kadangi Microsoft Agent Framework `OpenAIChatClient` veikia su bet kuriuo OpenAI suderinamu galiniu tašku, galite naudoti MiniMax kaip tiesioginę alternatyvą Azure OpenAI ar OpenAI.

Pridėkite šiuos kintamuosius į savo `.env` failą:

| Kintamasis | Kur rasti |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API raktai |
| `MINIMAX_BASE_URL` | Naudokite `https://api.minimax.io/v1` (numatytoji reikšmė) |
| `MINIMAX_MODEL_ID` | Modelio pavadinimas (pvz., `MiniMax-M3`) |

**Pavyzdiniai modeliai**: `MiniMax-M3` (rekomenduojamas), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (greitesni atsakymai). Modelių pavadinimai ir prieinamumas gali kisti laikui bėgant, o tam tikram modeliui prieiga gali priklausyti nuo jūsų paskyros ar regiono — patikrinkite [MiniMax Platform](https://platform.minimaxi.com/) dėl dabartinio sąrašo. Jei `MiniMax-M3` nėra pasiekiamas jūsų paskyroje, nustatykite `MINIMAX_MODEL_ID` į modelį, prie kurio turite prieigą (pvz., `MiniMax-M2.7`).

Kodo pavyzdžiai, naudojantys `OpenAIChatClient` (pvz., 14 pamokos viešbučių užsakymo srautas), automatiškai atpažins ir naudos jūsų MiniMax konfigūraciją, kai nustatytas `MINIMAX_API_KEY`.

## Alternatyvus teikėjas: Foundry Local (modelių vykdymas įrenginyje)

[Foundry Local](https://foundrylocal.ai) yra lengvas vykdymo variklis, kuris atsisiunčia, valdo ir tiekią kalbos modelius **visiškai jūsų pačių įrenginyje** per OpenAI suderinamą API – be debesų, be Azure prenumeratos ir be API raktų. Tai puikus sprendimas offline kūrimui, eksperimentams be debesijos sąnaudų arba duomenų laikymui įrenginyje.

Kadangi Microsoft Agent Framework `OpenAIChatClient` veikia su bet kuriuo OpenAI suderinamu galiniu tašku, Foundry Local yra tiesioginė vietinė alternatyva Azure OpenAI.

**1. Įdiekite Foundry Local**

```bash
# "Windows"
winget install Microsoft.FoundryLocal

# "macOS"
brew install foundrylocal
```

**2. Atsisiųskite ir paleiskite modelį** (tai taip pat paleidžia vietinį servisą):

```bash
foundry model list          # peržiūrėti galimus modelius
foundry model run phi-4-mini
```

**3. Įdiekite Python SDK**, kuri naudojama vietinio galutinio taško aptikimui:

```bash
pip install foundry-local-sdk
```

**4. Nurodykite Microsoft Agent Framework naudoti jūsų vietinį modelį:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Parsisiunčia (jei reikia) ir vietoje paleidžia modelį, tada nustato galinį tašką/prievadą.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # pavyzdžiui http://localhost:<port>/v1
    api_key=manager.api_key,        # visada "nereikia" Foundry Local atveju
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Pastaba:** Foundry Local pateikia OpenAI suderinamą **Chat Completions** galutinį tašką. Naudokite tai vietiniam kūrimui ir offline scenarijams. Pilnai **Responses API** funkcijoms (būsena pagrįstos pokalbiai, gilios įrankių orchestracijos ir agentų kūrimas) naudokite **Azure OpenAI** arba **Microsoft Foundry** projektą, kaip parodyta pamokose. Žr. [Foundry Local dokumentaciją](https://foundrylocal.ai) dėl dabartinio modelių katalogo ir platformos palaikymo.


## Papildomas nustatymas 8 pamokai (Bing pagrindimo darbo eiga)

Sąlyginės darbo eigos užrašų knyga 8 pamokoje naudoja **Bing pagrindimą** per Microsoft Foundry. Jei planuojate paleisti tą pavyzdį, pridėkite šią kintamąją į savo `.env` failą:

| Kintamasis | Kur rasti |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portalas → jūsų projektas → **Valdymas** → **Jungtinis ištekliai** → jūsų Bing jungtis → nukopijuokite jungties ID |

## Gedimų šalinimas

### SSL sertifikato patvirtinimo klaidos macOS

Jei naudojatės macOS ir susiduriate su klaida, panašia į:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Tai žinoma problema su Python macOS, kai sistemos SSL sertifikatai nėra automatiškai patikimi. Išbandykite šiuos sprendimus iš eilės:

**1 variantas: paleiskite Python Diegimo sertifikatų skriptą (rekomenduojama)**

```bash
# Pakeiskite 3.XX į jūsų įdiegtą Python versiją (pvz., 3.12 arba 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**2 variantas: naudokite `connection_verify=False` savo užrašų knygoje (tik GitHub Models užrašų knygoms)**

6 pamokos užrašų knygoje (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) jau yra įtrauktas komentarams skirtas sprendimas. Atkomentuokite `connection_verify=False` kuriant klientą:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Išjunkite SSL patvirtinimą, jei susiduriate su sertifikato klaidomis
)
```

> **⚠️ Įspėjimas:** SSL patikros išjungimas (`connection_verify=False`) sumažina saugumą praleidžiant sertifikatų patikrinimą. Naudokite tai tik laikinu sprendimu kūrimo aplinkose, niekada gamybos aplinkoje.

**3 variantas: įdiekite ir naudokite `truststore`**

```bash
pip install truststore
```

Tada pridėkite šią eilutę užrašų knygos arba skripto viršuje, prieš atliekant bet kokius tinklo skambučius:

```python
import truststore
truststore.inject_into_ssl()
```

## Užstringote?

Jei kyla problemų šio nustatymo metu, prisijunkite prie mūsų <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI bendruomenės Discord</a> arba <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">pateikite problemos pranešimą</a>.

## Kitoji pamoka

Dabar esate pasiruošę vykdyti šio kurso kodą. Sėkmės mokantis daugiau apie Dirbtinio intelekto agentų pasaulį!

[Įvadas į DI agentus ir agentų naudojimo atvejus](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->