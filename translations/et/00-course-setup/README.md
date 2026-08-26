# Kursuse seadistamine

## Sissejuhatus

See õppetund käsitleb, kuidas käivitada selle kursuse koodinäiteid.

## Liitu teiste õppuritega ja saa abi

Enne kui hakkad oma hoidlat kloonima, liitu [AI Agents For Beginners Discordi kanaliga](https://aka.ms/ai-agents/discord), et saada abi seadistamisel, esitada kursuse kohta küsimusi või suhelda teiste õppuritega.

## Klooni või hargne see hoidla

Alustamiseks palun klooni või hargne GitHubi hoidla. See loob sinu enda versiooni kursuse materjalidest, nii saad koodi käivitada, testida ja muuta!

Seda saab teha, klikkides lingile <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forkida hoidlat</a>

Sul peaks nüüd olema sinu enda harunenud versioon sellest kursusest järgmise lingi alt:

![Forked Repo](../../../translated_images/et/forked-repo.33f27ca1901baa6a.webp)

### Pealiskaudne kloon (soovitatav töötoale / Codespacesile)

  >Täielik hoidla võib olla suur (~3 GB), kui laadid alla kogu ajaloo ja kõik failid. Kui osaled ainult töötoas või vajad vaid mõne õppetüki kausta, siis pealiskaudne kloon (või hajutatud kloon) laadib alla palju vähem.

#### Kiire pealiskaudne kloon — minimaalne ajalugu, kõik failid

Asenda allolevates käskudes `<your-username>` oma hargnemise URL-iga (või eelistusel originaalhoidla URL-iga).

Kloonimiseks ainult viimase commit'i ajalugu (väike allalaadimine):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Kindla haru kloonimiseks:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Osaline (hajutatud) kloon — minimaalsed plokid + ainult valitud kaustad

See kasutab osalist klooni ja sparse-checkout'i (nõuab Git 2.25+ ja soovitatav kaasaegne Git osalise klooni toetusega):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Liigu hoidla kausta:

```bash
cd ai-agents-for-beginners
```

Seejärel määra, milliseid kaustu soovid (allolev näide näitab kahte kausta):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Pärast kloonimist ja failide kontrollimist, kui vajad vaid faile ja soovid vabaneda ruumist (ilma git ajaloo säilitamiseta), siis palun kustuta hoidla metaandmed (💀tagasipöördumatu — kaotad kogu Git funktsionaalsuse):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespacesi kasutamine (soovitatav, et vältida suuri lokaalseid allalaadimisi)

- Loo uus Codespace selle hoidla jaoks läbi [GitHub UI](https://github.com/codespaces).  

- Käivita uue Codespace terminalis üks ülaltoodud pealis- või hajutatud klooni käskudest, et tuua ainult vajalikud õppekohad Codespace tööruumi.
- Valikuline: pärast kloonimist Codespace'is eemalda .git, et vabastada ruumi (vt eemaldamiskäsud ülal).
- Märkus: kui soovid hoidlat avada otse Codespaces (ilma täiendava kloonita), siis tea, et Codespaces loob devcontainer keskkonna ning võib endiselt seadistada rohkem, kui vajad.

#### Näpunäited

- Asenda klooni URL alati oma hargenemisega, kui soovid redigeerida või commit'e teha.
- Kui vajad hiljem rohkem ajalugu või faile, saad need alla tõmmata või sparse-checkouti seadistust muuta, et lisada rohkem kaustu.

## Koodi käivitamine

See kursus pakub sarja Jupyteri märkmikke, mida saad käivitada, et saada praktiline kogemus AI agentide loomisel.

Koodinäited kasutavad **Microsoft Agent Frameworki (MAF)** koos `FoundryChatClient`-iga, mis ühendub **Microsoft Foundry Agent Service V2** (Response API) kaudu **Microsoft Foundry'ga**.

Kõik Python märkmikud on märgistatud kui `*-python-agent-framework.ipynb`.

## Nõuded

- Python 3.12+
  - **MÄRKUS**: Kui sul pole Python3.12 paigaldatud, paigalda see kindlasti. Seejärel loo oma venv kasutades python3.12, et tagada nõutud versioonide paigaldamine requirements.txt failist.
  
    >Näide

    Loo Python venv kataloog:

    ```bash
    python -m venv venv
    ```

    Seejärel aktiveeri venv keskkond:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Näidiskoodide .NET versiooni jaoks paigalda [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) või uuem. Kontrolli oma paigaldatud .NET SDK versiooni:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Vajalik autentimiseks. Paigalda [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure tellimus** — Microsoft Foundry ja Microsoft Foundry Agent Service ligipääsuks.
- **Microsoft Foundry projekt** — Projekt koos juurutatud mudeliga (nt `gpt-5-mini`). Vt [Samm 1](#1-samm-microsoft-foundry-projekti-loomine) allpool.

Oleme lisanud selle hoidla juurkausta `requirements.txt` faili, mis sisaldab kõiki vajalikke Python pakette koodi näidete käivitamiseks.

Sa saad need paigaldada, käivitades järgmise käsu terminalis hoidla juurkaustas:

```bash
pip install -r requirements.txt
```

Soovitame luua Python virtuaalkeskkonna, et vältida konflikte ja probleeme.

## VSCode seadistamine

Veendu, et VSCode'is kasutad õiget Python versiooni.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ja Microsoft Foundry Agent Service seadistamine

### 1. samm: Microsoft Foundry projekti loomine

Sul on vaja Microsoft Foundry **keskust** ja **projekti** koos juurutatud mudeliga, et käivitada märkmikke.

1. Mine aadressile [ai.azure.com](https://ai.azure.com) ja logi sisse oma Azure kontoga.
2. Loo **keskus** (või kasuta olemasolevat). Vaata: [Keskuse ressursside ülevaade](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Keskuses loo **projekt**.
4. Juuruta mudel (nt `gpt-5-mini`) alt **Models + Endpoints** → **Deploy model**.

### 2. samm: Projekti lõpp-punkti ja mudeli juurutamise nime leidmine

Oma projektist Microsoft Foundry portaalis:

- **Projekti lõpp-punkt** — Mine lehele **Ülevaade** ja kopeeri lõpp-punkti URL.

![Project Connection String](../../../translated_images/et/project-endpoint.8cf04c9975bbfbf1.webp)

- **Mudeli juurutamise nimi** — Mine **Models + Endpoints**, vali oma juurutatud mudel ja märgi üles **Deployment name** (nt `gpt-5-mini`).

### 3. samm: Sisselogimine Azuresse käsuga `az login`

Enamik märkmikke autentib läbi **Azure CLI sisselogimise** — kasutades `AzureCliCredential` või `DefaultAzureCredential` (mõlemad kasutavad `az login` seanssi) paketist `azure-identity` — seega API võtmeid pole vaja. Mõned õppetükid ja valikulised integratsioonid kasutavad API võtmeid; vaata iga õppetüki eeltingimusi lisamuutujate kohta. Selleks pead olema sisse logitud Azure CLI kaudu.

1. **Paigalda Azure CLI**, kui sul seda veel pole: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Logi sisse** käivitades:

    ```bash
    az login
    ```

    Või kui oled kaug- / Codespace keskkonnas ilma brauserita:

    ```bash
    az login --use-device-code
    ```

3. **Vali tellimus**, kui küsitakse – vali see, mis sisaldab sinu Foundry projekti.

4. **Kontrolli**, et oled sisse loginud:

    ```bash
    az account show
    ```

> **Miks `az login`?** Märkmikud autentivad `AzureCliCredential` (või `DefaultAzureCredential`, mis samuti kasutab sinu Azure CLI sisselogimise seanssi) abil paketist `azure-identity`. See tähendab, et sinu Azure CLI sessioon annab volitused — API võtmeid ega salasõnu `.env` failis pole vaja. See on [turvalisuse hea tava](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### 4. samm: Loo oma `.env` fail

Kopeeri näidfail:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Ava `.env` ja täida need kaks väärtust:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Muutuja | Kus seda leida |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portaal → sinu projekt → **Ülevaade** leht |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portaal → **Models + Endpoints** → sinu juurutatud mudeli nimi |

See ongi enamiku õppetükkide jaoks! Märkmikud autentivad automaatselt sinu `az login` seansi kaudu.

### 5. samm: Paigalda Python sõltuvused

```bash
pip install -r requirements.txt
```

Soovitame seda käivitada oma varem loodud virtuaalkeskkonnas.

## Valikuline seadistamine: Azure AI Search (õppetükid 5 ja 16)

Õppetükk 5 (Agentic RAG) ja 16 märkmikud töötavad koheselt **mälus paikneva teadmistebaasiga** — täiendavad Azure ressursid pole vajalikud. Kui soovid päris **Azure AI Search** indeksit kasutada, siis tuleks tähele panna, et **Õppetükk 16 märkmik kasutab praegu võtme-põhist autentimist**: see lülitub mälus otsingult Azure AI Searchile alles siis, kui on määratud nii `AZURE_SEARCH_SERVICE_ENDPOINT` kui ka `AZURE_SEARCH_API_KEY`; muul juhul töötleb mälus otsingut — seega reaalse indeksi käitamiseks pead määrama ka administraatori võtme. Võtmeta autentimine Microsoft Entra ID abil (RBAC) on soovitatav klassikaline viis su oma tootmiskoodi jaoks, sobides hästi selle kursuse üldise `az login` vooguga.

Allolevad RBAC sammud kehtivad seadistusjuhiste näidete ja su enda koodi puhul. Need ei aktiveeri võtmeta autentimist Õppetüki 16 märkmikus; see vajab ikka nii lõpp-punkti kui admin võtme kasutamist Azure AI Searchiks.

1. **Luba rollipõhine ligipääs** oma otsinguteenusel:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Määra endale vajalikud rollid** (indeksite loomine/laadimine ja päringud):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Lisa lõpp-punkt** oma `.env` faili:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portaal → sinu **Azure AI Search** ressurss → **Ülevaade** → URL |
| `AZURE_SEARCH_API_KEY` | Vajalik (lõpp-punktiga koos) Azure AI Searchi lubamiseks Õppetüki 16 märkmikus, mis kasutab võtme-põhist autentimist. Azure portaal → **Seaded** → **Võtmed** → peamine admin võti |

> **Miks võtmeta?** Admin võtmed annavad täis kirjutusõiguse otsinguteenusele ja võivad lekkida `.env` failidest. RBAC abil kasutad hoopis `az login` identiteeti — sama võtmeta Entra ID mudelit, mida kursuse märkmikud kasutavad (`AzureCliCredential` / `DefaultAzureCredential`). Vaata [Ühendu Azure AI Searchiga rollide kaudu](https://learn.microsoft.com/azure/search/search-security-rbac).

Vaata täispikka Azure AI Search seadistusjuhendit [AzureSearch.md](./AzureSearch.md) Python ja .NET indeksi loomise näidete jaoks.

## Täiendav seadistus märkmikele, mis kutsuvad Azure OpenAI otse (õppetükid 6 ja 8)

Mõned 6 ja 8 õppetüki märkmikud kutsuvad **Azure OpenAI** otse (kasutades **Responses API**), mitte Microsoft Foundry projekti kaudu. Need näited kasutasid varem GitHubi mudeleid, mis on aegunud ja ei toeta Responses API-t. Lisa need muutujad oma `.env` faili:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portaal → sinu **Azure OpenAI** ressurss → **Võtmed ja lõpp-punkt** → Lõpp-punkt (nt `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Sinu juurutatud mudeli nimi (nt `gpt-5-mini`), mis toetab Responses API-t |
| `AZURE_OPENAI_API_KEY` | Valikuline — ainult juhul kui kasutad võtme-põhist autentimist, mitte `az login` / Entra ID |

> Responses API kasutab stabiilset `/openai/v1/` lõpp-punkti, seega pole `api-version` vajalik. Kasuta võtmeta Entra ID autentimist, logides sisse `az login` kaudu.

## Alternatiivne pakkuja: MiniMax (OpenAI-ga ühilduv)

[MiniMax](https://platform.minimaxi.com/) pakub suuri kontekstimudeleid (kuni 204K tokenit) OpenAI-ga ühilduva API kaudu. Kuna Microsoft Agent Frameworki `OpenAIChatClient` töötab iga OpenAI-ga ühilduva lõpp-punktiga, võid kasutada MiniMaxi otse selle asemel õppetükkides, mis kasutavad `OpenAIChatClient`-i.

Lisa need muutujad oma `.env` faili:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax platvorm](https://platform.minimaxi.com/) → API võtmed |
| `MINIMAX_BASE_URL` | Kasuta `https://api.minimax.io/v1` (vaikimisi väärtus) |
| `MINIMAX_MODEL_ID` | Mudeli nimi (nt `MiniMax-M3`) |

**Näidismudelid**: `MiniMax-M3` (soovitatav), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (kiirem tagasiside). Mudelitenimed ja saadavus võivad aja jooksul muutuda, ning juurdepääs mudelile sõltub su kontost.

Koodinäited, mis kasutavad `OpenAIChatClient`-i (nt õppetükk 14 hotelli broneerimise töövoo näide), tuvastavad automaatselt ja kasutavad su MiniMaxi seadistust, kui `MINIMAX_API_KEY` on määratud.


## Alternatiivne pakkuja: Foundry Local (Mudelid töötavad seadmes)

[Foundry Local](https://foundrylocal.ai) on kergekaaluline käitusaeg, mis laadib alla, haldab ja pakub keelemudeleid **täielikult sinu enda masinas** läbi OpenAI-ga ühilduva API – pilve pole vaja.

Kuna Microsoft Agent Frameworki `OpenAIChatClient` töötab mis tahes OpenAI-ga ühilduva sihtpunktiga, on Foundry Local otsene lokaalne alternatiiv Azure OpenAI-le.

**1. Paigalda Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Lae alla ja käivita mudel** (see käivitab ka lokaalse teenuse):

```bash
foundry model list          # näita saadaolevaid mudeleid
foundry model run phi-4-mini
```

**3. Paigalda Python SDK**, mida kasutatakse lokaalse sihtpunkti avastamiseks:

```bash
pip install foundry-local-sdk
```

**4. Suuna Microsoft Agent Framework oma kohaliku mudeli poole:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Laeb alla (kui vaja) ja teenindab mudelit kohapeal, seejärel avastab lõpp-punkti/pordi.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # nt http://localhost:<port>/v1
    api_key=manager.api_key,        # alati "mitte-nõutav" Foundry Local'i puhul
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Märkus:** Foundry Local pakub OpenAI-ga ühilduvat **Chat Completions** sihtpunkti. Kasuta seda lokaalseks arenduseks ja võrguühenduseta stsenaariumides. Täieliku **Responses API** funktsioonikomplekti jaoks (olemuslikud vestlused jne) kasuta Azure OpenAI-d või Microsoft Foundryt.

## Täiendav seadistus 8. õppetöö jaoks (Bing Grounding töövoog)

Tingimuslik töövooga märkmik 8. õppetöös kasutab **Bing grounding** Microsoft Foundry kaudu. Kui plaanid seda näidist käivitada, lisa see muutuja oma `.env` faili:

| Muutuja | Kust leida |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portaal → su projekt → **Haldus** → **Ühendatud ressursid** → sinu Bingi ühendus → kopeeri ühenduse ID |

## Tõrkeotsing

### SSL sertifikaadi kinnituse vead macOS-is

Kui kasutad macOS-i ja saad veateate nagu:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

See on teadaolev probleem Pythoniga macOS-is, kus süsteemi SSL sertifikaate ei usaldata automaatselt. Proovi järgnevaid lahendusi selles järjekorras:

**Valik 1: Käivita Pythoni Install Certificates skript (soovitatav)**

```bash
# Asendage 3.XX teie paigaldatud Pythoni versiooniga (nt 3.12 või 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Valik 2: Kasuta `connection_verify=False` oma märkmikus (ainult GitHubi Models märkmikele)**

6. õppetöö märkmikus (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) on juba kommentaaridega lahendus. Eemalda kommentaar `connection_verify=False`, kui tekib sertifikaadivigu:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Keela SSL-kinnitamine, kui tekivad sertifikaadi vead
)
```

> **⚠️ Hoiduge:** SSL kinnituse väljalülitamine (`connection_verify=False`) vähendab turvalisust, jättes vahele sertifikaadi valideerimise. Kasuta seda ainult ajutise lahendusena arenduskeskkonnas. Ära kunagi kasuta tootmises.

**Valik 3: Paigalda ja kasuta `truststore`-i**

```bash
pip install truststore
```

Seejärel lisa see oma märkmiku või skripti algusesse enne võrguühenduse loomist:

```python
import truststore
truststore.inject_into_ssl()
```

## Jäädud kuskile kinni?

Kui sul tekib selle seadistusega probleeme, tule meie <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI kogukonna Discordi</a> või <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">loo probleem</a>.

## Järgmine õppetöö

Oled nüüd valmis selle kursuse koodi käivitama. Rõõmsat AI agentide maailma avastamist! 

[Sissejuhatus AI agentidesse ja agentide kasutusjuhtudesse](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->