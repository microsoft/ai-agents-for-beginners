# Kursuse seadistamine

## Sissejuhatus

Selles õppetükis käsitletakse, kuidas käivitada selle kursuse koodinäited.

## Liitu teiste õppijatega ja saa abi

Enne oma repositooriumi kloonimise alustamist liitu [AI Agents For Beginners Discordi kanaliga](https://aka.ms/ai-agents/discord), et saada abi seadistamisel, esitada küsimusi kursuse kohta või suhelda teiste õppijatega.

## Klooni või tee sellele repositooriumile fork

Alustamiseks klooni või tee GitHubi repositooriumile fork. See võimaldab sul teha kursuse materjalidest oma isikliku versiooni, kus saad koodi käivitada, testida ja muuta!

Seda saab teha, klõpsates lingil <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forkida repositoorium</a>

Nüüd peaks sul olema kursuse oma forkitud versioon järgmise lingi all:

![Forked Repo](../../../translated_images/et/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (soovitatav töötubadele / Codespaces)

  >Täielik repositoorium võib olla suur (~3 GB), kui laadid alla kogu ajaloo ja kõik failid. Kui osaled ainult töötubades või vajad ainult mõnda õppetüki kausta, väldib shallow clone (või sparse clone) enamikku sellest allalaadimisest, lühendades ajalugu ja/või jättes blobid vahele.

#### Kiire shallow clone — minimaalne ajalugu, kõik failid

Asenda allolevates käskudes `<your-username>` oma fork URL-iga (või eelistatud upstream URL-iga).

Ainult viimase commit ajaloo kloonimiseks (väike allalaadimine):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Konkreetse haru kloonimiseks:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Osaline (sparse) kloon — minimaalsed blobid + valitud kaustad

See kasutab osalist klooni ja sparse-checkouti (nõuab Git 2.25+ ja soovitatavalt uuemat Git versiooni osalise klooni toega):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Mine repositooriumi kausta:

```bash|powershell
cd ai-agents-for-beginners
```

Seejärel määra, millised kaustad soovid (alltoodud näide näitab kahte kausta):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Pärast kloonimist ja failide kontrollimist, kui vajad ainult faile ja soovid ruumi vabastada (ilma git ajalool), palun kustuta repositooriumi metaandmed (💀 pöördumatu — kaotad kogu Git funktsionaalsuse: ei commite, ei pulli, ei pushi ega ajalugu).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces'i kasutamine (soovitatav suurt lokaalset allalaadimist vältimiseks)

- Loo selle repositooriumi jaoks uus Codespace läbi [GitHub UI](https://github.com/codespaces).  

- Käivita uue Codespace'i terminalis üks ülaltoodud shallow/sparse clone käskudest, et tuua Codespace tööruumi vaid vajalikud õppetüki kaustad.
- Valikuline: pärast kloonimist Codespaces sisemuses eemalda .git, et vabastada lisaruumi (vt ülaltoodud eemaldamiskäsud).
- Märkus: Kui eelistad avada repositooriumi otse Codespaces (ilma lisakloonimiseta), pea meeles, et Codespaces loob devcontainer keskkonna ja võib siiski ette valmistada rohkem, kui vajad. Shallow copy kloonimine uues Codespaces annab suurema kontrolli ketta kasutuse üle.

#### Näpunäited

- Asenda klooni URL alati oma forkiga, kui soovid redigeerida/commitida.
- Kui hiljem vajad rohkem ajalugu või faile, saad need hankida või sparse-checkouti muuta, lisades täiendavaid kaustu.

## Koodi käivitamine

See kursus pakub seeria Jupyter Notebook'e, mida saad käivitada, et saada praktilist kogemust AI agentide loomisel.

Koodinäited kasutavad **Microsoft Agent Frameworki (MAF)** koos `AzureAIProjectAgentProvider`-ga, mis ühendub **Azure AI Agent Service V2** (Responses API) kaudu **Microsoft Foundryga**.

Kõik Python notebookid on märgistatud kui `*-python-agent-framework.ipynb`.

## Nõuded

- Python 3.12+
  - **MÄRKUS**: Kui sul ei ole Python 3.12 installitud, veendu, et paigaldad selle. Seejärel loo oma virtuaalne keskkond, kasutades python3.12, et tagada õigete versioonide installimine requirements.txt failist.

    >Näide

    Loo Python virtuaalne keskkond kaust:

    ```bash|powershell
    python -m venv venv
    ```

    Seejärel aktiveeri virtuaalne keskkond:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Näidiskoodide jaoks, mis kasutavad .NET-i, veendu, et oled paigaldanud [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) või uuema. Seejärel kontrolli installitud .NET SDK versiooni:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — nõutav autentimiseks. Paigalda aadressilt [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure tellimus** — Microsoft Foundry ja Azure AI Agent Service ligipääsuks.
- **Microsoft Foundry projekt** — projekt, kus on juurutatud mudel (nt `gpt-4o`). Vaata [1. sammu](../../../00-course-setup) allpool.

Selles repositooriumis on olemas `requirements.txt` fail, mis sisaldab kõiki vajalikke Python pakette koodinäidete jooksutamiseks.

Sa saad need paigaldada, käivitades alloleva käsu terminalis repositooriumi juurest:

```bash|powershell
pip install -r requirements.txt
```

Soovitame luua Pythoni virtuaalse keskkonna, et vältida konflikte ja probleeme.

## VSCode seadistamine

Veendu, et kasutad VSCode-s õiget Pythoni versiooni.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ja Azure AI Agent Service seadistamine

### Samm 1: Loo Microsoft Foundry projekt

Sul peab olema Azure AI Foundry **hub** ja **projekt** juurutatud mudeliga, et notebooke käivitada.

1. Mine aadressile [ai.azure.com](https://ai.azure.com) ja logi sisse oma Azure kontoga.
2. Loo **hub** (või kasuta olemasolevat). Vaata: [Hub ressurside ülevaade](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Hubi sees loo **projekt**.
4. Juuruta mudel (nt `gpt-4o`) valides **Models + Endpoints** → **Deploy model**.

### Samm 2: Hangi oma projekti endpoint ja mudeli juurutuse nimi

Microsoft Foundry portaali projektist:

- **Project Endpoint** — Mine **Overview** lehele ja kopeeri endpoint URL.

![Project Connection String](../../../translated_images/et/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Mine **Models + Endpoints** lehele, vali juurutatud mudel ja pane tähele **Deployment name** (nt `gpt-4o`).

### Samm 3: Logi sisse Azure'i käsureal `az login`

Kõik notebookid kasutavad autentimiseks **`AzureCliCredential`** — API võtit pole vaja hallata. See nõuab, et oled Azure CLI kaudu sisse loginud.

1. **Paigalda Azure CLI**, kui see pole veel tehtud: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Logi sisse** käsuga:

    ```bash|powershell
    az login
    ```

    Või kui oled kaugekeskkonnas/Codespace'is ilma brauserita:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vali oma tellimus**, kui seda küsitakse — vali see, kus on sinu Foundry projekt.

4. **Kontrolli**, et oled sisse logitud:

    ```bash|powershell
    az account show
    ```

> **Miks `az login`?** Notebookid kasutavad autentimiseks `azure-identity` paketist `AzureCliCredential`-i. See tähendab, et Azure CLI seanss annab vajaliku mandaadi — .env faili ei ole vaja lisada API võtmeid ega salajasi andmeid. See on turvalisuse parim tava [keyless connections](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Samm 4: Loo oma `.env` fail

Kopeeri näidiskaust:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Ava `.env` ja täida järgmised kaks väärtust:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Muutuja | Kus seda leida |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portaali su projekti **Overview** lehelt |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portaali **Models + Endpoints** alt su juurutatud mudeli nimi |

Enamus õppetundide jaoks on see kõik! Notebookid autentivad automaatselt läbi sinu `az login` seansi.

### Samm 5: Paigalda Python sõltuvused

```bash|powershell
pip install -r requirements.txt
```

Soovituslik on seda teha loodud virtuaal-keskkonnas.

## Täiendav seadistus õppetükiks 5 (Agentic RAG)

Õppetükk 5 kasutab **Azure AI Search** päringul põhineva genereerimise jaoks. Kui plaanid seda õppetundi teha, lisa oma `.env` faili järgmised muutujad:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portaali **Azure AI Search** ressursi **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portaali **Azure AI Search** ressursi **Settings** → **Keys** → peamine administraatori võti |

## Täiendav seadistus  õppetükkideks 6 ja 8 (GitHub mudelid)

Mõned notebookid õppetundides 6 ja 8 kasutavad **GitHub mudeleid** Azure AI Foundry asemel. Kui plaanid neid näiteid käivitada, lisa oma `.env` faili järgmised muutujad:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Kasuta `https://models.inference.ai.azure.com` (vaikimisi väärtus) |
| `GITHUB_MODEL_ID` | Kasutatava mudeli nimi (nt `gpt-4o-mini`) |

## Täiendav seadistus õppetüki 8 jaoks (Bing Grounding Workflow)

Õppetüki 8 tingimuslik workflow notebook kasutab **Bing grounding'ut** läbi Azure AI Foundry. Kui plaanid seda näidet jooksutada, lisa oma `.env` faili järgmine muutuja:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portaali su projekti **Management** → **Connected resources** → su Bing ühendus → kopeeri ühenduse ID |

## Tõrkeotsing

### SSL sertifikaadi valideerimise vead macOS-is

Kui sa kasutad macOS-i ja saa veateate nagu:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

See on teadaolev probleem Pythoniga macOS-is, kus süsteemi SSL sertifikaate ei usaldata automaatselt. Proovi järgmist lahendust järjekorras:

**Valik 1: Käivita Python'i Install Certificates skript (soovitatav)**

```bash
# Asendage 3.XX oma paigaldatud Pythoni versiooniga (nt 3.12 või 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Valik 2: Kasuta `connection_verify=False` oma notebookis (ainult GitHub Models notebookide jaoks)**

Õppetüki 6 notebookis (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) on juba kommentaarina lahendus olemas. Tühista `connection_verify=False` kommentaar, kui lood klienti:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Keela SSL-i kontroll, kui tekivad sertifikaadi vead
)
```

> **⚠️ Hoiatus:** SSL valideerimise keelamine (`connection_verify=False`) vähendab turvalisust, jättes sertifikaadi valideerimise vahele. Kasuta seda ainult ajutise lahendusena arenduskeskkonnas, mitte tootmises.

**Valik 3: Paigalda ja kasuta `truststore`**

```bash
pip install truststore
```

Seejärel lisa see oma notebooki või skripti algusesse enne ükskõik millise võrgukõne tegemist:

```python
import truststore
truststore.inject_into_ssl()
```

## Jäädud kuskile kinni?

Kui sul on probleeme seadistuse käivitamisega, tule meie <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discordi</a> või <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">loo viga</a>.

## Järgmine õppetükk

Nüüd oled valmis kursuse koodi käivitama. Head õppimist AI agentide maailma avastamisel!

[Juhtimine AI Agentide ja Agentide kasutusjuhtumite juurde](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüame tagada täpsust, pidage palun meeles, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma algkeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tekkida võivate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->