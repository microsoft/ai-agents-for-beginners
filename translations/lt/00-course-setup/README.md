# Kurso paruošimas

## Įvadas

Ši pamoka apims, kaip paleisti šio kurso kodo pavyzdžius.

## Prisijunkite prie kitų besimokančiųjų ir gaukite pagalbą

Prieš pradėdami klonuoti savo saugyklą, prisijunkite prie [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord), kad gautumėte pagalbą dėl sąrankos, turėtumėte klausimų apie kursą arba susisiektumėte su kitais besimokančiaisiais.

## Klonuoti arba padaryti fork šią saugyklą

Pradėdami, klonuokite arba sukurkite fork GitHub saugyklos. Tai sukurs jūsų pačių versiją kurso medžiagos, kad galėtumėte paleisti, testuoti ir koreguoti kodą!

Tai galite padaryti spustelėdami nuorodą į <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">sukurti forką</a>

Dabar turėtumėte turėti savo forkinę šio kurso versiją šioje nuorodoje:

![Forkinta saugykla](../../../translated_images/lt/forked-repo.33f27ca1901baa6a.webp)

### Paviršinis klonas (rekomenduojama dirbtuvėms / Codespaces)

  > Pilna saugykla gali būti didelė (~3 GB), kai atsisiunčiate visą istoriją ir visus failus. Jei dalyvaujate tik dirbtuvėse arba jums reikia tik kelių pamokų katalogų, paviršinis klonas (arba sparse klonas) išvengs didesnės dalies atsisiuntimo sumažindamas istoriją ir/ar praleisdamas blob'us.

#### Greitas paviršinis klonas — minimali istorija, visi failai

Pakeiskite `<your-username>` žemiau esančiuose komandose savo forko URL (arba upstream URL, jei pageidaujate).

Norint klonuoti tik naujausią commit istoriją (mažas atsisiuntimas):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Norint klonuoti konkretų šaką:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Dalinis (sparse) klonavimas — minimalūs blob'ai + tik pasirinktų aplankų

Tai naudoja partial clone ir sparse-checkout (reikalauja Git 2.25+ ir rekomenduojama moderni Git versija su partial clone palaikymu):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pereikite į saugyklos aplanką:

```bash|powershell
cd ai-agents-for-beginners
```

Tada nurodykite, kuriuos aplankus norite (žemiau esantis pavyzdys rodo du aplankus):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonavimo ir failų patikrinimo, jei jums reikalingi tik failai ir norite atlaisvinti vietos (be git istorijos), ištrinkite saugyklos metaduomenis (💀negrįžtama — prarasite visą Git funkcionalumą: jokių commit'ų, pull'ų, push'ų ar prieigos prie istorijos).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Naudojant GitHub Codespaces (rekomenduojama vengti didelių vietinių atsisiuntimų)

- Sukurkite naują Codespace šiai saugyklai per [GitHub UI](https://github.com/codespaces).  

- Naujo Codespace terminale vykdykite vieną iš aukščiau pateiktų shallow/sparse klonavimo komandų, kad į Codespace darbinę aplinką atkeltumėte tik reikiamus pamokų katalogus.
- Pasirinktinai: po klonavimo Codespaces viduje pašalinkite .git, kad atgautumėte papildomos vietos (žr. ištrynimo komandas aukščiau).
- Pastaba: jei norite atidaryti saugyklą tiesiogiai Codespaces (be papildomo klonavimo), atkreipkite dėmesį, kad Codespaces sukurs devcontainer aplinką ir gali vis tiek paruošti daugiau nei jums reikia. Klonavimas paviršiniu kopijuotu viduje naujo Codespace suteikia daugiau kontrolės dėl disko naudojimo.

#### Patarimai

- Visada pakeiskite klono URL į savo forką, jei norite redaguoti/commit'inti.
- Jei vėliau jums reikės daugiau istorijos ar failų, galite juos parsisiųsti arba pakoreguoti sparse-checkout, kad įtrauktumėte papildomus aplankus.

## Kodo paleidimas

Šis kursas siūlo keletą Jupyter Notebook failų, kuriuos galite paleisti, kad įgytumėte praktinės patirties kuriant AI agentus.

Kodo pavyzdžiai naudoja **Microsoft Agent Framework (MAF)** su `AzureAIProjectAgentProvider`, kuris jungiasi prie **Azure AI Agent Service V2** (Responses API) per **Microsoft Foundry**.

Visi Python notebook'ai yra pažymėti `*-python-agent-framework.ipynb`.

## Reikalavimai

- Python 3.12+
  - **PASTABA**: Jei neturite įdiegto Python 3.12, įsitikinkite, kad jį įdiegėte. Tada sukurkite savo venv naudodami python3.12, kad būtų įdiegtos teisingos versijos iš requirements.txt failo.
  
    >Pavyzdys

    Sukurkite Python venv katalogą:

    ```bash|powershell
    python -m venv venv
    ```

    Tada suaktyvinkite venv aplinką:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Jei pavyzdžių kodai naudoja .NET, įdiekite [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) arba naujesnę versiją. Tada patikrinkite įdiegtą .NET SDK versiją:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — reikalinga autentifikacijai. Įdiekite iš [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — prieigai prie Microsoft Foundry ir Azure AI Agent Service.
- **Microsoft Foundry Project** — projektas su diegimu modeliu (pvz., `gpt-4o`). Žr. [1 žingsnį](../../../00-course-setup) žemiau.

Šioje saugykloje šakniniame kataloge yra `requirements.txt` failas, kuriame pateikti visi reikalingi Python paketai kodo pavyzdžiams paleisti.

Juos galite įdiegti paleidę šią komandą terminale, būdami saugyklos šakniniame kataloge:

```bash|powershell
pip install -r requirements.txt
```

Rekomenduojame sukurti Python virtualią aplinką, kad išvengtumėte konfliktų ir problemų.

## VSCode nustatymas

Įsitikinkite, kad VSCode naudojate tinkamą Python versiją.

![paveikslėlis](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ir Azure AI Agent Service nustatymas

### 1 žingsnis: Sukurkite Microsoft Foundry projektą

Norint paleisti notebook'us, jums reikia Azure AI Foundry **hub** ir **project** su įdiegtu modeliu.

1. Eikite į [ai.azure.com](https://ai.azure.com) ir prisijunkite su savo Azure paskyra.
2. Sukurkite **hub** (arba naudokite esamą). Žr.: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Hub viduje sukurkite **project**.
4. Iš **Models + Endpoints** → **Deploy model** diegkite modelį (pvz., `gpt-4o`).

### 2 žingsnis: Gaukite savo projekto Endpoint ir modelio diegimo vardą

Iš savo projekto Microsoft Foundry portale:

- **Project Endpoint** — Eikite į **Apžvalga** puslapį ir nukopijuokite endpoint URL.

![Projekto prisijungimo eilutė](../../../translated_images/lt/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Eikite į **Models + Endpoints**, pasirinkite savo įdiegtą modelį ir atkreipkite dėmesį į **Deployment name** (pvz., `gpt-4o`).

### 3 žingsnis: Prisijunkite prie Azure su `az login`

Visi notebook'ai naudoja **`AzureCliCredential`** autentifikacijai — nereikia valdyti API raktų. Tam reikalinga prisijungti per Azure CLI.

1. **Įdiekite Azure CLI**, jei dar to nepadarėte: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prisijunkite** vykdydami:

    ```bash|powershell
    az login
    ```

    Arba, jei esate nuotolinėje/Codespace aplinkoje be naršyklės:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Pasirinkite prenumeratą** jei būsite paprašyti — pasirinkite tą, kuriame yra jūsų Foundry projektas.

4. **Patikrinkite**, ar esate prisijungę:

    ```bash|powershell
    az account show
    ```

> **Kodėl `az login`?** Notebook'ai autentifikuojasi naudodami `AzureCliCredential` iš `azure-identity` paketo. Tai reiškia, kad jūsų Azure CLI sesija suteikia kredencialus — nėra API raktų ar slaptų duomenų jūsų `.env` faile. Tai yra [saugumo geriausia praktika](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### 4 žingsnis: Sukurkite savo `.env` failą

Kopijuokite pavyzdinį failą:

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Kintamasis | Kur jį rasti |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portale → jūsų projektas → **Apžvalga** puslapis |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portale → **Models + Endpoints** → jūsų įdiegtas modelis → **Deployment name** |

Tai viskas daugumai pamokų! Notebook'ai automatiškai autentifikuosis per jūsų `az login` sesiją.

### 5 žingsnis: Įdiekite Python priklausomybes

```bash|powershell
pip install -r requirements.txt
```

Rekomenduojame tai vykdyti virtualioje aplinkoje, kurią sukūrėte anksčiau.

## Papildoma sąranka 5 pamokai (Agentic RAG)

5 pamoka naudoja **Azure AI Search** retrieval-augmented generation. Jei ketinate paleisti tą pamoką, pridėkite šiuos kintamuosius į savo `.env` failą:

| Kintamasis | Kur jį rasti |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portale → jūsų **Azure AI Search** išteklius → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portale → jūsų **Azure AI Search** išteklius → **Settings** → **Keys** → pagrindinis administratoriaus raktas |

## Papildoma sąranka 6 ir 8 pamokoms (GitHub Models)

Kai kurie 6 ir 8 pamokų notebook'ai naudoja **GitHub Models** vietoje Azure AI Foundry. Jei ketinate paleisti tuos pavyzdžius, pridėkite šiuos kintamuosius į savo `.env` failą:

| Kintamasis | Kur jį rasti |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Naudokite `https://models.inference.ai.azure.com` (numatytoji reikšmė) |
| `GITHUB_MODEL_ID` | Naudojamo modelio pavadinimas (pvz., `gpt-4o-mini`) |

## Papildoma sąranka 8 pamokai (Bing Grounding Workflow)

8 pamokos sąlyginės eigos notebook'as naudoja **Bing grounding** per Azure AI Foundry. Jei ketinate paleisti tą pavyzdį, pridėkite šį kintamąjį į savo `.env` failą:

| Kintamasis | Kur jį rasti |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portale → jūsų projektas → **Management** → **Connected resources** → jūsų Bing ryšys → nukopijuokite connection ID |

## Trikčių šalinimas

### SSL sertifikato tikrinimo klaidos macOS sistemoje

Jei naudojate macOS ir susiduriate su klaida kaip:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Tai yra žinoma problema su Python macOS, kai sistemos SSL sertifikatams automatiškai nėra suteikiamas pasitikėjimas. Išbandykite šiuos sprendimus eilės tvarka:

**1 variantas: Paleiskite Python Install Certificates skriptą (rekomenduojama)**

```bash
# Pakeiskite 3.XX į savo įdiegtą Python versiją (pvz., 3.12 arba 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**2 variantas: Naudokite `connection_verify=False` savo notebook'e (tik GitHub Models notebookams)**

Pamokoje 6 esančiame notebook'e (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) jau yra įtrauktas komentaru pažymėtas sprendimas. Atkomentuokite `connection_verify=False`, kai kuriate klientą:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Išjunkite SSL patikrinimą, jei susiduriate su sertifikato klaidomis
)
```

> **⚠️ Įspėjimas:** SSL tikrinimo išjungimas (`connection_verify=False`) sumažina saugumą praleidžiant sertifikatų patikrinimą. Naudokite tai tik kaip laikino pobūdžio sprendimą vystymo aplinkoje, niekada gamyboje.

**3 variantas: Įdiekite ir naudokite `truststore`**

```bash
pip install truststore
```

Tada pridėkite šį kodą savo notebook'o arba skripto pradžioje prieš vykdant bet kokius tinklo kvietimus:

```python
import truststore
truststore.inject_into_ssl()
```

## Užstrigote kažkur?

Jei kyla kokių nors problemų vykdant šią sąranką, prisijunkite prie mūsų <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI bendruomenės Discord</a> arba <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">pateikite problemos pranešimą</a>.

## Kita pamoka

Dabar esate pasirengę paleisti šio kurso kodą. Sėkmės mokantis apie AI agentų pasaulį!

[Įvadas į AI agentus ir naudojimo atvejai](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas pagrindiniu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus, žmogaus atliktas vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->