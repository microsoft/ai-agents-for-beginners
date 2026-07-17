# Kursuse seadistamine

## Sissejuhatus

See õppetund käsitleb, kuidas käivitada selle kursuse koodinäiteid.

## Liitu teiste õppijatega ja saa abi

Enne kui hakkad oma reposid kloonima, liitu [AI Agents For Beginners Discord kanaliga](https://aka.ms/ai-agents/discord), et saada abi seadistamisel, esitada küsimusi kursuse kohta või suhelda teiste õppijatega.

## Klooni või hargne see repo

Alustamiseks palun klooni või hargne GitHubi hoidla. See loob sinu enda versiooni kursuse materjalist, et saaksid koodi käivitada, testida ja kohandada!

Seda saab teha, klõpsates lingil <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">hargneda repot</a>

Teil peaks nüüd olema selle kursuse oma hargnenud versioon järgmises lingis:

![Hargnenud Repo](../../../translated_images/et/forked-repo.33f27ca1901baa6a.webp)

### Madal kloon (soovitatav töötubade / Codespaces jaoks)

  >Täielik hoidla võib olla suur (~3 GB), kui laadite alla kogu ajaloo ja kõik failid. Kui osaled ainult töötoas või vajad vaid mõnda õppetunni kausta, siis madal kloon (või hõre kloon) väldib enamikku sellest allalaadimisest, piirates ajalugu ja/või jättes blobid vahele.

#### Kiire madal kloon — minimaalne ajalugu, kõik failid

Asenda alljärgnevates käskudes `<your-username>` oma hargne URL-iga (või ülemvoolu URL-iga, kui soovid).

Kloonimiseks ainult viimase commit ajalugu (väike allalaadimine):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Konkreetse haru kloonimiseks:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Osaline (hõre) kloon — minimaalne blobide arv + ainult valitud kaustad

See kasutab osalist klooni ja hõredat kontrolli (nõuab Git 2.25+ ning soovitatav on kaasaegne Git osalise klooni toega):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Liigu hoidla kausta:

```bash|powershell
cd ai-agents-for-beginners
```

Seejärel määra, milliseid kaustu soovid (näide allpool näitab kahte kausta):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Pärast kloonimist ja failide kontrollimist, kui vajad ainult faile ja soovid ruumi vabastada (ilma git ajaloo ligipääsuta), palun kustuta hoidla metaandmed (💀 pöördumatu — kaotad kogu Git funktsionaalsuse: pole commit'e, pull'e, push'e ega ajaloo ligipääsu).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces kasutamine (soovitatav, et vältida suuri kohalikke allalaadimisi)

- Loo uus Codespace selle hoidla jaoks läbi [GitHub UI](https://github.com/codespaces).  

- Uue loodud codespace terminalis käivita üks ülaltoodud madala/hõreda klooni käske, et tuua Codespace tööruumi ainult vajalikud õppetunni kaustad.
- Valikuline: pärast kloonimist Codespaces eemalda .git, et vabastada täiendavat ruumi (vt eemaldamiskäsud ülal).
- Märkus: Kui soovid avat repot otse Codespaces (ilma lisakloonita), pea meeles, et Codespaces ehitab devcontainer keskkonna ning võib ikka varustada rohkem, kui sul vaja on. Madala klooni tegemine värskes Codespace's annab rohkem kontrolli kettaruumikasutuse üle.

#### Näpunäited

- Asenda klooni URL alati oma hargnenud URL-iga, kui soovid redigeerida/commit'ida.
- Kui hiljem vajad rohkem ajalugu või faile, saad neid alla tõmmata või kohandada hõredat kontrolli, et lisada täiendavaid kaustu.

## Koodi käivitamine

See kursus pakub rea Jupyter Notebooke, mida saad käivitada, et saada praktilist kogemust AI agentide loomisel.

Koodinäited kasutavad **Microsoft Agent Framework'i (MAF)** koos `FoundryChatClient`-iga, mis ühendub **Microsoft Foundry Agent Service V2** (Responses API) kaudu **Microsoft Foundry'ga**.

Kõik Python notebookid on tähistatud `*-python-agent-framework.ipynb`.

## Nõuded

- Python 3.12+
  - **MÄRKUS**: Kui sul pole Python 3.12 installitud, veendu, et selle paigaldad. Seejärel loo oma venv kasutades python3.12, et tagada nõutud versioonide paigaldamine requirements.txt failist.
  
    >Näide

    Loo Python venv kaust:

    ```bash|powershell
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

- .NET 10+: Näidiskoodide jaoks, mis kasutavad .NET-i, veendu, et paigaldate [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) või uuema. Seejärel kontrolli paigaldatud .NET SDK versiooni:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Autentimiseks vajalik. Installeeri aadressilt [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure tellimus** — Microsoft Foundry ja Microsoft Foundry Agent Service'i ligipääsuks.
- **Microsoft Foundry projekt** — Projekt koos juurutatud mudeliga (nt `gpt-4.1-mini`). Vaata [Samm 1](#samm-1-loo-microsoft-foundry-projekt) allpool.

Oleme lisanud selle hoidla juurkausta faili `requirements.txt`, mis sisaldab kõiki vajalikke Python pakette koodinäidete käivitamiseks.

Saad need installida, käivitades oma terminalis hoidlakaustas järgmise käsu:

```bash|powershell
pip install -r requirements.txt
```

Soovitame luua Python virtuaalsesse keskkonda, et vältida konflikte ja probleeme.

## VSCode seadistamine

Veendu, et kasutad VSCode's õiget Python versiooni.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ja Microsoft Foundry Agent Service seadistamine

### Samm 1: Loo Microsoft Foundry projekt

Sul on vaja Microsoft Foundry **hub'i** ja **projekti** koos juurutatud mudeliga, et käivitada notebook'id.

1. Mine lehele [ai.azure.com](https://ai.azure.com) ja logi sisse oma Azure kontoga.
2. Loo **hub** (või kasuta olemasolevat). Vaata: [Hubi ressursside ülevaade](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Hub'i sees loo **projekt**.
4. Juuruta mudel (nt `gpt-4.1-mini`) **Models + Endpoints** → **Deploy model** kaudu.

### Samm 2: Hangi oma projekti lõpp-punkt ja mudeli juurutuse nimi

Oma projekti Microsoft Foundry portaali kaudu:

- **Projekti lõpp-punkt** — Mine **Overview** lehele ja kopeeri lõpp-punkti URL.

![Projekti ühendamise string](../../../translated_images/et/project-endpoint.8cf04c9975bbfbf1.webp)

- **Mudeli juurutuse nimi** — Mine **Models + Endpoints** juurde, vali oma juurutatud mudel ja märgi üles **Deployment name** (nt `gpt-4.1-mini`).

### Samm 3: Logi Azure'i sisse `az login` abil

Kõik notebookid kasutavad autentimiseks **`AzureCliCredential`** — pole API võtmeid vaja hallata. Selleks tuleb olla sisse logitud Azure CLI kaudu.

1. **Installeeri Azure CLI**, kui pole veel paigaldatud: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Logi sisse** käsuga:

    ```bash|powershell
    az login
    ```

    Või kui oled eemal/ Codespace keskkonnas ilma brauserita:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vali oma tellimus**, kui küsitakse — vali see, kus asub sinu Foundry projekt.

4. **Kontrolli**, et oled sisse logitud:

    ```bash|powershell
    az account show
    ```

> **Miks `az login`?** Notebook'id autentivad kasutades `AzureCliCredential` `azure-identity` paketist. See tähendab, et sinu Azure CLI sessioon annab mandaadid — pole vaja API võtmeid või saladusi `.env` failis. See on [turvalisuse parim tava](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Samm 4: Loo oma `.env` fail

Kopeeri näidiskood:

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Muutuja | Kus seda leida |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portaali projekt → **Overview** leht |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portaali **Models + Endpoints** → juurutatud mudeli nimi |

Enamikuks õppetundideks on see kõik! Notebookid autentivad automaatselt sinu `az login` sessiooni kaudu.

### Samm 5: Paigalda Python sõltuvused

```bash|powershell
pip install -r requirements.txt
```

Soovitame seda käivitada oma varem loodud virtuaalkeskkonnas.

## Täiendav seadistus õppetunni 5 jaoks (Agentic RAG)

Õppetund 5 kasutab **Azure AI Search'i** täiendatud genereerimise jaoks. Kui kavatsed seda õppetundi teha, lisa need muutujad oma `.env` faili:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portaal → sinu **Azure AI Search** ressurss → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portaal → sinu **Azure AI Search** ressurss → **Settings** → **Keys** → põhivõti |

## Täiendav seadistus õppetundidele, mis kutsuvad Azure OpenAI otse (õppetunnid 6 ja 8)

Mõned 6. ja 8. õppetunni notebookid kutsuvad otse **Azure OpenAI'd** (kasutades **Responses API't**) ilma Microsoft Foundry projekti kaudu. Need näited kasutasid varem GitHub mudeleid, mis on aegunud (vabrik lõpetab töö 2026. aasta juulis) ja ei toeta Responses API't. Kui kavatsed neid näiteid käivitada, lisa need muutujad oma `.env` faili:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portaal → sinu **Azure OpenAI** ressurss → **Keys and Endpoint** → Lõpp-punkt (nt `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Sinu juurutatud mudeli nimi (nt `gpt-4.1-mini`), mis toetab Responses API't |
| `AZURE_OPENAI_API_KEY` | Valikuline — ainult kui kasutad võtmepõhist autentimist `az login` / Entra ID asemel |

> Responses API kasutab stabiilset `/openai/v1/` lõpp-punkti, seega pole `api-version`'i vaja. Logi sisse `az login` abil, et kasutada võtmeteta Entra ID autentimist.

## Alternatiivne pakkuja: MiniMax (OpenAI-ga ühilduv)

[MiniMax](https://platform.minimaxi.com/) pakub suurte kontekstidega mudeleid (kuni 204K tokenit) OpenAI-ga ühilduva API kaudu. Kuna Microsoft Agent Framework'i `OpenAIChatClient` töötab iga OpenAI-ga ühilduva lõpp-punktiga, saad kasutada MiniMax'i otse Azure OpenAI või OpenAI asemel.

Lisa need muutujad oma `.env` faili:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platvorm](https://platform.minimaxi.com/) → API võtmeks |
| `MINIMAX_BASE_URL` | Kasuta `https://api.minimax.io/v1` (vaikimisi väärtus) |
| `MINIMAX_MODEL_ID` | Mudeli nimi, mida kasutada (nt `MiniMax-M3`) |

**Näidismudelid**: `MiniMax-M3` (soovitatav), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (kiirem vastus). Mudelite nimed ja kättesaadavus võivad aja jooksul muutuda ning ligipääs konkreetsele mudelile sõltub sinu kontost või regioonist — vaata [MiniMax Platvormi](https://platform.minimaxi.com/) ajakohast nimekirja. Kui `MiniMax-M3` ei ole sinu kontol saadaval, määra `MINIMAX_MODEL_ID` mudelile, millele sul on ligipääs (nt `MiniMax-M2.7`).

Näidiskoodid, mis kasutavad `OpenAIChatClient`i (nt 14. õppetunni hotelli broneerimise töökäik), tuvastavad ja kasutavad automaatselt sinu MiniMaxi konfiguratsiooni, kui `MINIMAX_API_KEY` on määratud.

## Alternatiivne pakkuja: Foundry Local (mudelite käitamine seadmes)

[Foundry Local](https://foundrylocal.ai) on kergekaaluline käitusaeg, mis laadib alla, haldab ja teenindab keelemudeleid **täielikult sinu enda arvutis** OpenAI-ga ühilduva API kaudu — pole pilve, pole Azure tellimust, ega API võtmeid. See on suurepärane valik võrguühenduseta arendamiseks, katsetamiseks ilma pilvekuludeta või andmete hoidmiseks seadmes.

Kuna Microsoft Agent Framework'i `OpenAIChatClient` töötab iga OpenAI-ga ühilduva lõpp-punktiga, on Foundry Local mugav kohalik alternatiiv Azure OpenAI'le.

**1. Paigalda Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Laadi alla ja käivita mudel** (see käivitab ka kohaliku teenuse):

```bash
foundry model list          # vaadake saadaolevaid mudeleid
foundry model run phi-4-mini
```

**3. Paigalda Python SDK**, mida kasutatakse kohaliku lõpp-punkti leidmiseks:

```bash
pip install foundry-local-sdk
```

**4. Suuna Microsoft Agent Framework oma kohaliku mudeli poole:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Laeb (vajadusel) alla ja teenindab mudelit lokaalselt, seejärel leiab endpointi/pordi.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # nt http://localhost:<port>/v1
    api_key=manager.api_key,        # alati "ei ole nõutav" Foundry Local'i puhul
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Märkus:** Foundry Local pakub OpenAI-ga ühilduvat **Chat Completions** lõpp-punkti. Kasuta seda kohalikuks arenduseks ja võrguühenduseta olukordades. Täieliku **Responses API** funktsionaalsuse (seisunditevestlused, sügav tööriistade orkestreerimine ja agentstiilis arendus) jaoks sihita **Azure OpenAI** või **Microsoft Foundry** projekti, nagu näidatud õppetundides. Vaata [Foundry Local dokumentatsiooni](https://foundrylocal.ai) ajakohast mudelikataloogi ja platvormi tuge.


## Täiendav seadistamine 8. õppetunniks (Bingi alusvoog)

Tingimuslikus töövoo märkmikus 8. õppetunnis kasutatakse **Bingi alustamist** Microsoft Foundry kaudu. Kui plaanite seda näidist käivitada, lisage see muutuja oma `.env` faili:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portaal → teie projekt → **Management** → **Connected resources** → teie Bing ühendus → kopeerige ühenduse ID |

## Tõrkeotsing

### SSL-sertifikaadi kontrolli vead macOS-is

Kui olete macOS-is ja saate veateate nagu:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

See on tuntud probleem Pythoniga macOS-il, kus süsteemi SSL-sertifikaate ei usaldata automaatselt. Proovige järgmisi lahendusi järjekorras:

**Valik 1: Käivitage Pythoni Install Certificates skript (soovitatav)**

```bash
# Asendage 3.XX oma paigaldatud Pythoni versiooniga (nt 3.12 või 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Valik 2: Kasutage oma märkmikus `connection_verify=False` (ainult GitHub Models märkmikud)**

6. õppetunni märkmikus (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) on juba lisatud kommenteeritud lahendus. Võtke `connection_verify=False` kasutusele kliendi loomisel:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Lülita SSL-i kontroll välja, kui kohtad sertifikaadivigu
)
```

> **⚠️ Hoiatus:** SSL-kontrolli väljalülitamine (`connection_verify=False`) vähendab turvalisust, jättes sertifikaadi valideerimise vahele. Kasutage seda ainult ajutise lahendusena arenduskeskkondades, mitte tootmises.

**Valik 3: Installige ja kasutage `truststore`**

```bash
pip install truststore
```

Seejärel lisage oma märkmiku või skripti algusesse enne võrgukõnede tegemist järgmine kood:

```python
import truststore
truststore.inject_into_ssl()
```

## Jääd kuskile kinni?

Kui teil on selle seadistusega probleeme, liituge meie <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI kogukonna Discordiga</a> või <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">loonud vea</a>.

## Järgmine õppetund

Nüüd olete valmis selle kursuse koodi käivitama. Head AI agentide maailma õppimist!

[Sissejuhatus AI agentidesse ja Agentide kasutusjuhtumitesse](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->