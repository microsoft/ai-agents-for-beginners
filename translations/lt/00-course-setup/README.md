# Kursų diegimas

## Įvadas

Ši pamoka apims, kaip paleisti šio kurso kodo pavyzdžius.

## Prisijunkite prie kitų besimokančiųjų ir gaukite pagalbą

Prieš pradėdami klonuoti savo saugyklą, prisijunkite prie [AI Agents For Beginners Discord kanalo](https://aka.ms/ai-agents/discord), kad gautumėte pagalbą diegiant, atsakymus į klausimus apie kursą arba susisiektumėte su kitais besimokančiaisiais.

## Klonuokite arba šakotę šią saugyklą

Norėdami pradėti, prašome klonuoti arba šakoti GitHub saugyklą. Tai leis turėti savo kurso medžiagos versiją, kad galėtumėte paleisti, testuoti ir redaguoti kodą!

Tai galima atlikti paspaudus nuorodą <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a>

Dabar turėtumėte turėti savo fork'intą šio kurso versiją šiuo adresu:

![Forked Repo](../../../translated_images/lt/forked-repo.33f27ca1901baa6a.webp)

### Seklus klonavimas (rekomenduojama dirbtuvėms / Codespaces)

  > Pilna saugykla gali būti didelė (~3 GB), jeigu atsisiunčiate visą istoriją ir visus failus. Jei lankotės tik dirbtuvėse arba reikia tik keletos pamokų aplankų, seklaus klonavimo (arba išskaidyto klonavimo) metu atsisiunčiama žymiai mažiau.

#### Greitas seklius klonavimas — minimali istorija, visi failai

Pakeiskite `<your-username>` toliau pateiktose komandose savo forko URL (arba gaunamoje saugykloje URL, jei pageidaujate).

Norėdami klonuoti tik naujausią komitų istoriją (nedidelis atsisiuntimas):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Norėdami klonuoti tam tikrą šaką:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Dalinis (išskaidytas) klonavimas — minimalūs blobai + tik pasirinkti aplankai

Tai naudoja dalinį klonavimą ir sparse-checkout (reikalauja Git 2.25+ ir rekomenduojama šiuolaikinį Git su dalinio klonavimo palaikymu):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pereikite į saugyklos aplanką:

```bash
cd ai-agents-for-beginners
```

Tada nurodykite, kuriuos aplankus norite (žemiau pateiktas pavyzdys rodo du aplankus):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonavimo ir failų patikrinimo, jei jums reikia tik failų ir norite atlaisvinti vietos (be git istorijos), ištrinkite saugyklos metaduomenis (💀 negrįžtama – prarasite visą Git funkcionalumą):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Naudojant GitHub Codespaces (rekomenduojama, kad būtų išvengta didelių vietinių atsisiuntimų)

- Sukurkite naują Codespace šiai saugyklai naudodami [GitHub sąsają](https://github.com/codespaces).  

- Naujo sukurtos Codespace terminale paleiskite vieną iš aukščiau nurodytų seklus/išskaidyto klonavimo komandų, kad į Codespace darbo sritį atneštumėte tik reikalingus pamokų aplankus.
- Papildomai: po klonavimo Codespaces pašalinkite .git, kad susigrąžintumėte papildomos vietos (žr. pašalinimo komandas aukščiau).
- Pastaba: jei norite atidaryti saugyklą tiesiogiai Codespaces (be papildomo klonavimo), žinokite, kad Codespaces sukurs devcontainer aplinką ir gali paruošti daugiau nei jums reikia.

#### Patarimai

- Visada pakeiskite klonavimo URL į savo forką, jei norite redaguoti/arba įsipareigoti.
- Vėliau, jei reikės daugiau istorijos ar failų, galite juos atsisiųsti arba pakeisti sparse-checkout, kad būtų įtraukti papildomi aplankai.

## Kodo paleidimas

Šis kursas siūlo kelių Jupyter užrašinių seriją, kurias galite paleisti, kad praktikuotumėte kūrimą AI agentų.

Kodo pavyzdžiai naudoja **Microsoft Agent Framework (MAF)** su `FoundryChatClient`, kuris jungiasi prie **Microsoft Foundry Agent Service V2** (Responses API) per **Microsoft Foundry**.

Visi Python užrašiniai pažymėti `*-python-agent-framework.ipynb`.

## Reikalavimai

- Python 3.12+
  - **PASTABA**: Jei neturite įdiegto Python3.12, įsitikinkite, kad jį įdiegiate. Tuomet sukurkite savo venv naudodami python3.12, kad būtų įdiegtos tinkamos versijos iš requirements.txt failo.
  
    >Pavyzdys

    Sukurkite Python venv katalogą:

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

- .NET 10+: Jei naudojate pavyzdinius kodus su .NET, įsitikinkite, kad įdiegėte [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) arba naujesnę versiją. Tuomet patikrinkite savo įdiegtos .NET SDK versiją:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — reikalinga autentifikacijai. Įdiekite iš [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure prenumerata** — prieigai prie Microsoft Foundry ir Microsoft Foundry Agent Service.
- **Microsoft Foundry projektas** — projektas su diegta modeliu (pvz., `gpt-5-mini`). Žr. [1 žingsnį](#1-žingsnis-sukurkite-microsoft-foundry-projektą) žemiau.

Šioje saugyklos šaknyje yra failas `requirements.txt`, kuriame yra visi reikalingi Python paketai kodo pavyzdžiams vykdyti.

Juos galite įdiegti vykdydami šią komandą terminale saugyklos šaknyje:

```bash
pip install -r requirements.txt
```

Rekomenduojame sukurti Python virtualią aplinką, kad išvengtumėte konfliktų ir problemų.

## VSCode konfigūravimas

Įsitikinkite, kad VSCode naudojate tinkamą Python versiją.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ir Microsoft Foundry Agent Service nustatymas

### 1 žingsnis: Sukurkite Microsoft Foundry projektą

Kad paleistumėte užrašinius, jums reikia Microsoft Foundry **hub** ir **projekto** su diegtu modeliu.

1. Eikite į [ai.azure.com](https://ai.azure.com) ir prisijunkite su savo Azure paskyra.
2. Sukurkite **hub** (arba naudokite jau egzistuojantį). Žr.: [Hub išteklių apžvalga](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Hub viduje sukurkite **projektą**.
4. Išdiegiama modelis (pvz., `gpt-5-mini`) per **Models + Endpoints** → **Deploy model**.

### 2 žingsnis: Gaukite projekto endpointą ir modelio diegimo pavadinimą

Iš savo projekto Microsoft Foundry portale:

- **Projekto endpointas** — eikite į **Overview** puslapį ir nukopijuokite endpoint URL.

![Project Connection String](../../../translated_images/lt/project-endpoint.8cf04c9975bbfbf1.webp)

- **Modelio diegimo pavadinimas** — eikite į **Models + Endpoints**, pasirinkite įdiegtą modelį, pažymėkite **Deployment name** (pvz., `gpt-5-mini`).

### 3 žingsnis: Prisijunkite prie Azure su `az login`

Dauguma užrašinių autentifikuoja per jūsų **Azure CLI prisijungimą** — naudodami `AzureCliCredential` arba `DefaultAzureCredential` (abu gauna jūsų `az login` seansą) iš `azure-identity` paketo — todėl jiems nereikia API raktų. Keletas pamokų ir neprivalomų integracijų naudoja API raktus; patikrinkite kiekvienos pamokos reikalavimus dėl papildomų aplinkos kintamųjų. Tai reiškia, kad turite būti prisijungę per Azure CLI.

1. **Įdiekite Azure CLI**, jei dar neįdiegėte: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prisijunkite** paleisdami:

    ```bash
    az login
    ```

    Arba jei esate nuotolinėje/Codespace aplinkoje be naršyklės:

    ```bash
    az login --use-device-code
    ```

3. **Pasirinkite savo prenumeratą**, jei paprašys — pasirinkite tą, kurioje yra jūsų Foundry projektas.

4. **Patikrinkite**, kad esate prisijungę:

    ```bash
    az account show
    ```

> **Kodėl `az login`?** Užrašiniai autentifikuoja naudodami `AzureCliCredential` (arba `DefaultAzureCredential`, kuris taip pat paima jūsų Azure CLI prisijungimą) iš `azure-identity` paketo. Tai reiškia, kad jūsų Azure CLI seansas teikia prisijungimo duomenis – nereikia naudoti API raktų ar paslapčių `.env` faile. Tai yra [saugumo geriausia praktika](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

| Kintamasis | Kur jį rasti |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portalas → jūsų projektas → **Overview** puslapis |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portalas → **Models + Endpoints** → jūsų diegto modelio pavadinimas |

Tai viskas daugumai pamokų! Užrašiniai automatiškai autentifikuos per jūsų `az login` seansą.

### 5 žingsnis: Įdiekite Python priklausomybes

```bash
pip install -r requirements.txt
```

Rekomenduojame tai vykdyti virtualioje aplinkoje, kurią sukūrėte anksčiau.

## Neprivalomas nustatymas: Azure AI paieška (5 ir 16 pamokos)

5 pamokos (Agentic RAG) ir 16 pamokos užrašiniai veikia iš karto su **atmintyje esančia žinių baze** — nereikia papildomų Azure išteklių. Jei norite naudoti tikrą **Azure AI Search** indeksą, atkreipkite dėmesį, kad 16 pamokos užrašinis šiuo metu naudoja klavišo pagrindu veikiančią autentifikaciją: jis perjungiamas nuo atmintyje esančios paieškos prie Azure AI Search tik tada, kai nustatomi tiek `AZURE_SEARCH_SERVICE_ENDPOINT`, tiek `AZURE_SEARCH_API_KEY`; kitaip lieka atminties paieškoje — kad jį naudotumėte su tikru indeksu, būtina nustatyti administravimo raktą. Be raktų autentifikacija su Microsoft Entra ID (RBAC) yra rekomenduojamas būdas jūsų gamybinėse programose, suderintas su `az login` srautu, naudojamu visame šiame kurse.

Toliau pateikti RBAC žingsniai taikomi diegimo pavyzdžiams ir jūsų kodui. Jie neįgalina be raktų autentifikacijos 16 pamokos užrašinyje; 16 pamoka vis dar reikia tiek endpoint, tiek administravimo rakto, kad naudotų Azure AI Search.

1. **Įjunkite vaidmenų pagrindu pagrįstą prieigą** savo paieškos paslaugoje:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Priskirkite sau reikalingus vaidmenis** (kurti / užkrauti indeksus ir atlikti užklausas):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Pridėkite endpoint į savo `.env` failą**:

| Kintamasis | Kur jį rasti |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portalas → jūsų **Azure AI Search** išteklius → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Reikalinga (kartu su endpoint) įjungti Azure AI Search 16 pamokos užrašinyje, kuris naudoja klavišo pagrindu veikiančią autentifikaciją. Azure portalas → **Settings** → **Keys** → pagrindinis administravimo raktas |

> **Kodėl be raktų?** Administratoriniai raktai suteikia visišką rašymo prieigą prie jūsų paieškos paslaugos ir gali nutekėti per `.env` failus. Su RBAC vietoje to naudojamas jūsų `az login` tapatybė — tas pats be raktų Entra ID modelis, kurį naudoja kurso užrašiniai (naudojant `AzureCliCredential` / `DefaultAzureCredential`). Žr. [Prisijungimas prie Azure AI Search naudojant vaidmenis](https://learn.microsoft.com/azure/search/search-security-rbac).

Žr. [Azure AI Search diegimo vadovą](./AzureSearch.md) dėl pilnų indeksų kūrimo pavyzdžių Python ir .NET.

## Papildomas nustatymas pamokoms, kurios tiesiogiai naudoja Azure OpenAI (6 ir 8 pamokos)

Kai kurie 6 ir 8 pamokų užrašiniai tiesiogiai kreipiasi į **Azure OpenAI** (naudodami **Responses API**), o ne per Microsoft Foundry projektą. Šie pavyzdžiai anksčiau naudojo GitHub modelius, kurie yra pasenę ir nepalaiko Responses API. Pridėkite šiuos kintamuosius į savo `.env` failą:

| Kintamasis | Kur jį rasti |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portalas → jūsų **Azure OpenAI** išteklius → **Keys and Endpoint** → Bendrasis URL (pvz., `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Jūsų diegto modelio pavadinimas (pvz., `gpt-5-mini`), kuris palaiko Responses API |
| `AZURE_OPENAI_API_KEY` | Pasirinktinai — tik jei naudojate klavišo pagrindu veikiančią autentifikaciją vietoje `az login`/Entra ID |

> Responses API naudoja stabilų `/openai/v1/` endpointą, taigi `api-version` nenurodoma. Prisijunkite su `az login`, kad naudotumėte be raktų Entra ID autentifikaciją.

## Alternatyvus tiekėjas: MiniMax (OpenAI suderinamas)

[MiniMax](https://platform.minimaxi.com/) teikia didelės apimties konteksto modelius (iki 204K žetonų) per OpenAI suderinamą API. Kadangi Microsoft Agent Framework `OpenAIChatClient` veikia su bet kuriuo OpenAI suderinamu endpointu, galite naudoti MiniMax kaip alternatyvą pamokoms, kurios naudoja `OpenAIChatClient`.

Pridėkite šiuos kintamuosius į savo `.env` failą:

| Kintamasis | Kur jį rasti |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax platforma](https://platform.minimaxi.com/) → API raktai |
| `MINIMAX_BASE_URL` | Naudokite `https://api.minimax.io/v1` (numatytoji reikšmė) |
| `MINIMAX_MODEL_ID` | Modelio pavadinimas naudoti (pvz., `MiniMax-M3`) |

**Pavyzdiniai modeliai**: `MiniMax-M3` (rekomenduojamas), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (greitesni atsakymai). Modelių pavadinimai ir prieinamumas gali keistis, o prieiga prie tam tikro modelio gali priklausyti nuo paskyros.

Kodo pavyzdžiai, kurie naudoja `OpenAIChatClient` (pvz., 14 pamokos viešbučio užsakymų darbo eigos pavyzdys), automatiškai aptiks ir naudosis jūsų MiniMax konfigūracija, kai nustatytas `MINIMAX_API_KEY`.


## Alternatyvus tiekėjas: Novita AI (suderinama su OpenAI)

[Novita AI](https://novita.ai/llm-api) teikia OpenAI suderinamą API atvirojo kodo ir pažangiems LLM (DeepSeek, Llama, Qwen ir kiti). Kadangi Microsoft Agent Framework `OpenAIChatClient` veikia su bet kuria OpenAI suderinama galine taško adreso dalimi, galite naudoti Novita AI kaip pakaitalą Azure OpenAI arba OpenAI.

Pridėkite šiuos kintamuosius į savo `.env` failą:

| Kintamasis | Kur rasti |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI valdymo skydelis](https://novita.ai/settings/key-management) → API raktai |
| `NOVITA_BASE_URL` | Naudokite `https://api.novita.ai/openai/v1` (numatytoji reikšmė) |
| `NOVITA_MODEL_ID` | Naudojamo modelio pavadinimas (pvz., `moonshotai/kimi-k3`) |

**Pavyzdiniai modeliai**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI taip pat talpina daug kitų atvirojo kodo modelių šeimų (Llama, Qwen, GLM ir kt.) — žiūrėkite [Novita AI modelių biblioteką](https://novita.ai/llm-api) dabartinei prieinamų modelių ir jų ID listei.

Dabartiniai pavyzdžiai automatiškai nepanaudoja `NOVITA_*` kintamųjų. Norėdami naudoti Novita AI, perduokite šias reikšmes aiškiai, kai konstratuojate `OpenAIChatClient` pavyzdyje, kurį vykdote.

## Alternatyvus tiekėjas: Foundry Local (vykdykite modelius vietoje)

[Foundry Local](https://foundrylocal.ai) yra lengvas vykdymo laikotarpis, kuris atsisiunčia, valdo ir teikia kalbos modelius **visiškai jūsų pačių įrenginyje** per OpenAI suderinamą API — nereikia debesies.

Kadangi Microsoft Agent Framework `OpenAIChatClient` veikia su bet kuria OpenAI suderinama galine taško adreso dalimi, Foundry Local yra vietinis pakaitalas Azure OpenAI.

**1. Įdiekite Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Atsisiųskite ir paleiskite modelį** (tai taip pat paleidžia vietinę paslaugą):

```bash
foundry model list          # žiūrėti prieinamus modelius
foundry model run phi-4-mini
```

**3. Įdiekite Python SDK** naudojamą vietinio galinio taško paieškai:

```bash
pip install foundry-local-sdk
```

**4. Nukreipkite Microsoft Agent Framework į savo vietinį modelį:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Atsisiunčia (jei reikia) ir aptarnauja modelį lokaliai, tada aptinka galinį tašką/portą.
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

> **Pastaba:** Foundry Local pateikia OpenAI suderinamą **Chat Completions** galinį tašką. Naudokite jį vietiniam vystymui ir neprisijungus. Pilnai **Responses API** funkcijoms (būsenos palaikymas pokalbiuose ir kt.) naudokite Azure OpenAI arba Microsoft Foundry projektą.

## Papildoma nustatymai 8 pamokai (Bing pagrindimas)

8 pamokos sąlyginio darbo eiga naudoja **Bing pagrindimą** per Microsoft Foundry. Jei ketinate vykdyti tą pavyzdį, pridėkite šį kintamąjį į `.env` failą:

| Kintamasis | Kur rasti |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portalas → jūsų projektas → **Valdymas** → **Prijungtos ištekliai** → jūsų Bing prijungimas → nukopijuokite prijungimo ID |

## Problemų sprendimas

### SSL sertifikato patikros klaidos macOS

Jei naudojate macOS ir gaunate klaidą panašią į:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Tai žinoma Python problema macOS, kai sistemos SSL sertifikatai nėra automatiškai patikimi. Išbandykite šiuos sprendimus paeiliui:

**1 variantas: Paleiskite Python Sertifikatų diegimo skriptą (rekomenduojama)**

```bash
# Pakeiskite 3.XX į jūsų įdiegtą Python versiją (pvz., 3.12 arba 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**2 variantas: naudokite `connection_verify=False` savo užrašuose (tik GitHub Models užrašams)**

6 pamokos užraše (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) jau yra įkomentuotas sprendimas. Atkomentuokite `connection_verify=False`, jei gaunate sertifikato klaidas:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Išjunkite SSL patvirtinimą, jei susiduriate su sertifikato klaidomis
)
```

> **⚠️ Įspėjimas:** SSL patikros išjungimas (`connection_verify=False`) sumažina saugumą, nes praleidžiama sertifikato patikra. Naudokite tai tik kaip laikiną sprendimą kūrimo aplinkoje. Niekada nenaudokite gamyboje.

**3 variantas: Įdiekite ir naudokite `truststore`**

```bash
pip install truststore
```

Tada pridėkite šį kodą į užrašo ar skripto pradžią prieš bet kokius tinklo kvietimus:

```python
import truststore
truststore.inject_into_ssl()
```

## Užstrigote kur nors?

Jei turite problemų su šia nustatymo eiga, prisijunkite prie mūsų <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI bendruomenės Discord</a> arba <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">sukurkite problemą</a>.

## Kitoji pamoka

Dabar esate pasiruošę paleisti šio kurso kodą. Sėkmės mokantis apie AI agentų pasaulį!

[Įvadas į AI agentus ir agentų naudojimo atvejus](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->