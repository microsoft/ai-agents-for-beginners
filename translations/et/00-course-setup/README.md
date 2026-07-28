# Kursuse seadistamine

## Sissejuhatus

See õppetund käsitleb, kuidas käivitada selle kursuse koodinäiteid.

## Liitu teiste õppijatega ja saa abi

Enne oma repoga kloonimise alustamist liitu [AI Agents For Beginners Discord kanaliga](https://aka.ms/ai-agents/discord), et saada abi seadistamisel, esitada küsimusi kursuse kohta või suhelda teiste õppijatega.

## Kloneeri või loo selle repo fork

Alustamiseks palun kloonige või looge selle GitHubi repositooriumi fork. See teeb sinule oma versiooni kursuse materjalist, et saaksite koodi jooksutada, testida ja kohandada!

Seda saab teha, klõpsates lingil <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">loo repo fork</a>

Nüüd peaks sul olema oma fork sellest kursusest järgneva lingi all:

![Forkitud Repo](../../../translated_images/et/forked-repo.33f27ca1901baa6a.webp)

### Shallow kloon (soovitatav töötubade / Codespaces jaoks)

 > Täielik repositoorium võib olla suur (~3 GB), kui laed alla kogu ajaloo ja kõik failid. Kui osaled ainult töötubades või vajad vaid mõnda õppetunni kausta, siis shallow kloon (või sparse kloon) väldib suure osa allalaadimisest, kärpides ajalugu ja/või vahele jättes blob’e.

#### Kiire shallow kloon — minimaalne ajalugu, kõik failid

Asenda järgneva käskluse `<your-username>` oma fork URL-iga (või upstream URL-iga, kui eelistad).

Käsk lõpp-punktide kloonimiseks ainult viimase commit ajalooga (väike allalaadimine):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Konkreetse haru kloonimiseks:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Osaline (sparse) kloon — minimaalsed blobid + ainult valitud kaustad

Kasutab osalist klooni ja sparse-checkout’i (nõuab Git 2.25+ ja soovitatav on kaasaegne Git osalise klooni toega):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Mine repo kausta:

```bash|powershell
cd ai-agents-for-beginners
```

Seejärel määrake, milliseid kaustu soovite (allolev näide näitab kahte kausta):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Pärast kloonimist ja failide kontrollimist, kui vajad vaid faile ning soovid vabastada ruumi (ilma git ajaloo säilitamiseta), palun kustuta repositooriumi metaandmed (💀 pöördumatu - kaotad kogu Git funktsionaalsuse: ei commite, pulli, pushi ega ajaloo ligipääsu).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces kasutamine (soovitatav, et vältida suurt kohaliku allalaadimist)

- Loo uus Codespace selle repo jaoks läbi [GitHub UI](https://github.com/codespaces).  

- Käivita uue Codespace terminalis mõni ülaltoodud shallow/sparse klooni käsklus, et tuua ainult vajalikud õppetundide kaustad Codespace tööruumi.
- Valikuline: Pärast kloonimist Codespaces eemalda .git, et vabastada lisaruumi (vaata ülespoole eemaldamiskäske).
- Märkus: Kui eelistad avada repo otse Codespaces (ilma lisakloonita), pea meeles, et Codespaces loob devcontainer keskkonna ja võib ikkagi käivitada rohkem funktsioone kui vajad. Shallow klooni tegemine värskes Codespaces annab sulle parema kontrolli ketta kasutuse üle.

#### Näpunäited

- Asenda alati klooni URL oma forkiga, kui soovid redigeerida/commitida.
- Kui vajad hiljem rohkem ajalugu või faile, saad need alla laadida või sparse-checkout’i kaudu lisakaustu lisada.

## Koodi jooksutamine

See kursus pakub rea Jupyter märkmikke, millega saad praktilist kogemust AI Agentide loomisel.

Koodinäited kasutavad **Microsoft Agent Framework’i (MAF)** koos `FoundryChatClient`-iga, mis ühendub **Microsoft Foundry Agent Service V2**-ga (Responses API) läbi **Microsoft Foundry**.

Kõik Python märkmikud kannavad nimetust `*-python-agent-framework.ipynb`.

## Nõuded

- Python 3.12+
  - **MÄRGE**: Kui sul pole Python 3.12 installitud, siis palun tee see. Seejärel loo oma venv kasutades python3.12, et kindlustada õige versioonide paigaldus requirements.txt failist.
  
    >Näide

    Loo Python venv kataloog:

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

- .NET 10+: Näidiskoodide jaoks kasutades .NET, veendu, et oled installinud [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) või uuema. Seejärel kontrolli oma .NET SDK versiooni:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Nõutav autentimiseks. Installi link [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure tellimus (Subscription)** — Microsoft Foundry ja Microsoft Foundry Agent Service ligipääsuks.
- **Microsoft Foundry projekt** — Projekt koos väljalastud mudeliga (nt `gpt-5-mini`). Vaata [1. samm](#1-samm-loo-microsoft-foundry-projekt) allpool.

Meie repositooriumi juurkataloogis on `requirements.txt` fail, mis sisaldab kõiki vajalikke Python pakette koodi näidete jooksutamiseks.

Sa saad need paigaldada, käivitades järgmise käsu oma terminalis repositooriumi juurest:

```bash|powershell
pip install -r requirements.txt
```

Soovitame luua Python virtuaalkeskkonna, et vältida konflikte ja probleeme.

## Seadista VSCode

Veendu, et VSCode-s kasutad õiget Python versiooni.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Sea üles Microsoft Foundry ja Microsoft Foundry Agent Service

### 1. samm: Loo Microsoft Foundry projekt

Selleks vajad Microsoft Foundry **huba** ja **projekti** koos väljalastud mudeliga, et käivitada märkmikke.

1. Mine [ai.azure.com](https://ai.azure.com) ja logi sisse oma Azure kontoga.
2. Loo **hub** (või kasuta olemasolevat). Vaata: [Hub ressursi ülevaade](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Hubs loo **projekt**.
4. Lase mudel kasutusele (nt `gpt-5-mini`) valides **Models + Endpoints** → **Deploy model**.

### 2. samm: Hangi oma projekti lõpp-punkt ja mudeli väljalaske nimi

Oma projekti Microsoft Foundry portaalist:

- **Project Endpoint** — Mine **Overview** lehele ja kopeeri lõpp-punkti URL.

![Project Connection String](../../../translated_images/et/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Mine **Models + Endpoints**, vali oma väljalastud mudel ja märgi üles **Deployment name** (nt `gpt-5-mini`).

### 3. samm: Logi Azure keskkonda sisse `az login` abil

Kõik märkmikud kasutavad autentimiseks **`AzureCliCredential`** — API võtmeid hallata ei ole vaja. See eeldab, et oled sisse logitud Azure CLI kaudu.

1. **Paigalda Azure CLI**, kui pole veel paigaldatud: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Logi sisse** käivitades:

    ```bash|powershell
    az login
    ```

    Või kui oled kaugses/Codespace keskkonnas ilma brauserita:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vali tellimus (subscription)**, kui küsitakse — võta see, milles on sinu Foundry projekt.

4. **Kontrolli**, et oled sisse logitud:

    ```bash|powershell
    az account show
    ```

> **Miks `az login`?** Märkmikud kasutavad autentimiseks `AzureCliCredential`-i, mis tuleb `azure-identity` paketist. See tähendab, et Azure CLI sessioon annab mandaadid — pole vaja API võtmeid ega saladusi `.env` failis. See on [turvalisuse parim tava](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### 4. samm: Loo oma `.env` fail

Kopeeri näidisskoor:

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

| Variable | Kust leida |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portaal → sinu projekt → **Overview** leht |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portaal → **Models + Endpoints** → sinu väljalastud mudeli nimi |

Enamikuks õppetundideks ongi see kõik! Märkmikud autentivad automaatselt sinu `az login` sessiooni kaudu.

### 5. samm: Paigalda Pythonile sõltuvused

```bash|powershell
pip install -r requirements.txt
```

Soovitame seda teha äsja loodud virtuaalkeskkonnas.

## Täiendav seadistus õppetunnile 5 (Agentic RAG)

Õppetund 5 kasutab **Azure AI Search** andmete otsimiseks (retrieval-augmented generation). Kui plaanid seda õppetundi teha, lisa järgmised muutujaid oma `.env` faili:

| Variable | Kust leida |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portaal → sinu **Azure AI Search** ressurss → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portaal → sinu **Azure AI Search** ressurss → **Settings** → **Keys** → põhihaldusvõti |

## Täiendav seadistus õppetundidele, mis kasutavad otse Azure OpenAI-d (õppetunnid 6 ja 8)

Mõned märkmikud õppetundides 6 ja 8 kutsuvad otse esile **Azure OpenAI** (kasutades **Responses API-t**) ilma Microsoft Foundry projekti kaudu. Need näited kasutasid varem GitHub Mudelite teenust, mis on aegunud (väljajõudmine juulis 2026) ja ei toeta Responses API-d. Kui plaanid neid näiteid jooksutada, lisa need muutujaid oma `.env` faili:

| Variable | Kust leida |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portaal → sinu **Azure OpenAI** ressurss → **Keys and Endpoint** → Lõpp-punkt (nt `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Sinu väljalastud mudeli nimi (nt `gpt-5-mini`), mis toetab Responses API-t |
| `AZURE_OPENAI_API_KEY` | Valikuline — ainult juhul, kui kasutad võtme-põhist autentimist az login / Entra ID asemel |

> Responses API kasutab stabiilset `/openai/v1/` lõpp-punkti, seega pole `api-version` parameetrit vaja. Logi sisse `az login` abil, et kasutada võtmevaba Entra ID autentimist.

## Alternatiivne pakkuja: MiniMax (OpenAI-ühilduv)

[MiniMax](https://platform.minimaxi.com/) pakub suurkontekstilisi mudeleid (kuni 204K tokenit) OpenAI-ga ühilduva API kaudu. Kuna Microsoft Agent Framework’i `OpenAIChatClient` töötab mis tahes OpenAI-ühilduva lõpp-punktiga, saad kasutada MiniMax-i kui Azure OpenAI või OpenAI asendajat.

Lisa need muutujad oma `.env` faili:

| Variable | Kust leida |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platvorm](https://platform.minimaxi.com/) → API võtmed |
| `MINIMAX_BASE_URL` | Kasuta `https://api.minimax.io/v1` (vaikimisi väärtus) |
| `MINIMAX_MODEL_ID` | Kasutatava mudeli nimi (näiteks `MiniMax-M3`) |

**Näidismudelid**: `MiniMax-M3` (soovitatav), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (kiirem vastus). Mudelid ja saadavus võivad aja jooksul muutuda ning ligipääs mudelile sõltub kontost või regioonist — vaata [MiniMax Platvorm](https://platform.minimaxi.com/) praegust nimekirja. Kui `MiniMax-M3` pole sinu kontoga saadaval, määra `MINIMAX_MODEL_ID` mudelile, millele sul ligipääs on (nt `MiniMax-M2.7`).

Koodinäited, mis kasutavad `OpenAIChatClient` (nt õppetund 14 hotelli broneeringute töövoog), tuvastavad automaatselt ja kasutavad sinu MiniMax konfiguratsiooni, kui `MINIMAX_API_KEY` on määratud.

## Alternatiivne pakkuja: Foundry Local (Käivita mudeleid kohapeal)

[Foundry Local](https://foundrylocal.ai) on kerge jooksutuskeskkond, mis alla laadib, haldab ja pakub keelemudeleid **täielikult sinu enda masinas** OpenAI-ühilduva API kaudu — pole vaja pilve, Azure tellimust ega API võtmeid. Hea valik võrguühenduseta arenduseks, katsetamiseks ilma pilvekuludeta või andmete hoidmiseks lokaalselt.

Kuna Microsoft Agent Framework’i `OpenAIChatClient` töötab mis tahes OpenAI-ühilduva lõpp-punktiga, on Foundry Local kohalik alternatiiv Azure OpenAI-le.

**1. Paigalda Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Laadi mudel alla ja käivita see** (käivitab ka kohaliku teenuse):

```bash
foundry model list          # nähtavad mudelid
foundry model run phi-4-mini
```

**3. Paigalda Python SDK**, mida kasutatakse kohaliku lõpp-punkti avastamiseks:

```bash
pip install foundry-local-sdk
```

**4. Suuna Microsoft Agent Framework oma kohalikule mudelile:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Laadib (vajadusel) alla ja teenindab mudelit kohapeal, seejärel leiab lõpp-punkti/pordi.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # nt http://localhost:<port>/v1
    api_key=manager.api_key,        # alati "pole vajalik" Foundry Locali puhul
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Märkus:** Foundry Local pakub OpenAI-ühilduvat **Chat Completions** lõpp-punkti. Kasuta seda kohalikuks arenduseks ja võrguühenduseta juhtudeks. Täieliku **Responses API** funktsioonide komplekti jaoks (seisundipõhised vestlused, sügav tööriistade orkestreerimine ja agent-tüüpi arendus) kasuta **Azure OpenAI** või **Microsoft Foundry** projekti nagu näidetes. Vaata [Foundry Local dokumentatsiooni](https://foundrylocal.ai) praeguse mudelitekataloogi ja platvormi toe kohta.

## Täiendav seadistus õppetunnile 8 (Bing Grounding töövoog)


Tingimusliku töövoo märkmik õppetükis 8 kasutab **Bing grounding** Microsoft Foundry kaudu. Kui plaanite seda näidet käivitada, lisage see muutuja oma `.env` faili:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portaal → teie projekt → **Halduse** → **Ühendatud ressursid** → teie Bing ühendus → kopeerige ühenduse ID |

## Tõrkeotsing

### SSL sertifikaadi kontrolli vead macOS-il

Kui kasutate macOS-i ja ilmneb selline viga:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

See on tuntud probleem Pythonil macOS-il, kus süsteemi SSL sertifikaate ei usaldata automaatselt. Proovige järjekorras järgmisi lahendusi:

**Valik 1: Käivitage Pythoni Install Certificates skript (soovitatav)**

```bash
# Asenda 3.XX oma paigaldatud Pythoni versiooniga (nt 3.12 või 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Valik 2: Kasutage oma märkmikus `connection_verify=False` (ainult GitHub Models märkmike puhul)**

Õppetüki 6 märkmikus (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) on juba olemas kommenteeritud lahendus. Tühistage kommentaar `connection_verify=False` juures, kui loote kliendi:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Keela SSL-i kontroll, kui ilmnevad sertifikaadivead
)
```

> **⚠️ Hoiduge:** SSL kontrolli väljalülitamine (`connection_verify=False`) vähendab turvalisust, jättes sertifikaatide valideerimise vahele. Kasutage seda vaid ajutise lahendusena arenduskeskkonnas, mitte kunagi tootmiskeskkonnas.

**Valik 3: Paigaldage ja kasutage `truststore`-i**

```bash
pip install truststore
```

Seejärel lisage see järgnev osa oma märkmiku või skripti algusesse enne mis tahes võrgukõnesid:

```python
import truststore
truststore.inject_into_ssl()
```

## Hulkudes kinni?

Kui teil tekib selle seadistuse käivitamisel probleeme, tulge jutule meie <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI kogukonna Discordi</a> või <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">looge probleemiraport</a>.

## Järgmine õppetükk

Olete nüüd valmis selle kursuse koodi käivitama. Edu AI agentide maailma avastamisel!

[Sissejuhatus AI agentidesse ja agentide kasutusjuhtudesse](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->