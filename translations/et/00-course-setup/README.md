# Kursuse seadistamine

## Sissejuhatus

See õppetund käsitleb, kuidas käivitada selle kursuse koodinäited.

## Liitu teiste õppijatega ja saa abi

Enne kui hakkad kloonima oma hoidlat, liitu [AI Agents For Beginners Discordi kanaliga](https://aka.ms/ai-agents/discord), et saada abi seadistamisel, esitada küsimusi kursuse kohta või suhelda teiste õppijatega.

## Klooni või hargi see hoidla

Alustamiseks palun klooni või hargi GitHubi hoidla. See loob sulle kursuse materjali enda versiooni, et saaksid koodi käivitada, testida ja kohandada!

Seda saab teha, klõpsates lingil <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">hargne hoidla</a>

Sul peaks nüüd olema selle kursuse enda hargnenud versioon järgmisel lingil:

![Forked Repo](../../../translated_images/et/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (soovitatav töötoa / Codespaces jaoks)

  > Täielik hoidla võib olla suur (~3 GB), kui laadid alla kogu ajaloo ja kõik failid. Kui osaled ainult töökojas või vajad ainult mõningaid õppetundide kaustu, siis lähedane kloon (või hõre kloon) laadib alla palju vähem.

#### Kiirlähenemine — minimaalne ajalugu, kõik failid

Asenda alltoodud käskudes `<your-username>` oma hargi URL-iga (või ülemise hoidla URL-iga, kui eelistad).

Klooni ainult viimase kinnituse ajalugu (väike allalaadimine):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Konkreetse haru kloonimiseks:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Osaline (hõre) kloon — minimaalne hulknurkade + ainult valitud kaustad

See kasutab osalist klooni ja hõreda kontrolli meetodit (nõuab Git 2.25+ ning soovitatav on kaasaegne Git osalise klooni toetusega):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Liigu hoidla kausta:

```bash
cd ai-agents-for-beginners
```

Seejärel määra, milliseid kaustu soovid (alltoodud näites on kaks kausta):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Pärast kloonimist ja failide kontrolli, kui vajad ainult faile ja soovid ruumi vabastada (mitte mingit git ajalugu), siis palun kustuta hoidla metaandmed (💀 pöördumatu — sa kaotad kõik Git funktsioonid):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces kasutamine (soovitatav, et vältida suuri kohapealseid allalaadimisi)

- Loo uus Codespace selle hoidla jaoks [GitHubi kasutajaliidese kaudu](https://github.com/codespaces).  

- Käivita loodud Codespace terminalis üks ülevalmainitud lähenemistest, et tuua ainult vajalikud õppetundide kaustad Codespace tööruumi.
- Valikuline: pärast kloonimist Codespaces eemalda .git, et vabastada lisaruumi (vt kustutamise käske eespool).
- Märkus: kui eelistad avada hoidla otse Codespaces (ilma lisakloonita), siis ole teadlik, et Codespaces koostab devcontainer keskkonna ja võib siiski ette valmistada rohkem, kui vajad.

#### Näpunäited

- Asenda klooni URL alati oma hargnega, kui soovid muuta/commitida.
- Kui vajad hiljem rohkem ajalugu või faile, saad need tuua või kohandada hõre-kontrolli lisakaustu kaasamaks.

## Koodi käivitamine

See kursus pakub rea Jupyter Notebooke, mida saad käivitada, et saada praktilist kogemust AI agentide loomisel.

Koodinäited kasutavad **Microsoft Agent Frameworki (MAF)** koos `FoundryChatClient`-iga, mis ühendub **Microsoft Foundry Agent Service V2** (Responses API) kaudu **Microsoft Foundryga**.

Kõik Python märkmikud on märgistatud `*-python-agent-framework.ipynb`.

## Nõuded

- Python 3.12+
  - **MÄRKUS**: Kui sul ei ole Python3.12 paigaldatud, paigalda see kindlasti. Loo siis oma virtuaalne keskkond kasutades python3.12, et tagada õigete versioonide paigaldamine requirements.txt failist.
  
    >Näide

    Loo Python virtuaalkeskkonna kaust:

    ```bash
    python -m venv venv
    ```

    Seejärel aktiveeri virtuaalkeskkond:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Näidiskoodide jaoks, mis kasutavad .NETi, veendu, et oled installinud [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) või uuema. Kontrolli oma installitud .NET SDK versiooni:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Nõutav autentimiseks. Paigalda aadressilt [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure tellimus** — Microsoft Foundry ja Microsoft Foundry Agent Service ligipääsuks.
- **Microsoft Foundry projekt** — Projekt, kus on kasutusel mudeleid (nt `gpt-5-mini`). Vaata [Samm 1](#samm-1-loo-microsoft-foundry-projekt) allpool.

Oleme lisanud `requirements.txt` faili selle hoidla juurkausta, mis sisaldab kõiki vajalikke Python pakette koodinäidete käivitamiseks.

Saad need paigaldada, käivitades oma terminalis hoidla juurkaustas järgmise käsu:

```bash
pip install -r requirements.txt
```

Soovitame luua Python virtuaalse keskkonna, et vältida konflikte ja probleeme.

## VSCode seadistamine

Veendu, et kasutad VSCode-s õiget Python versiooni.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ja Microsoft Foundry Agent Service seadistamine

### Samm 1: Loo Microsoft Foundry projekt

Sul peab olema Microsoft Foundry **keskus** ja **projekt** koos kasutusele võetud mudeliga, et käivitada märkmikke.

1. Mine aadressile [ai.azure.com](https://ai.azure.com) ja logi sisse oma Azure kontoga.
2. Loo **keskus** (või kasuta olemasolevat). Vt: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Loo keskuses **projekt**.
4. Vii mudelit välja (nt `gpt-5-mini`) lehelt **Models + Endpoints** → **Deploy model**.

### Samm 2: Hangi projekti lõpp-punkti ja mudeli väljalaske nimi

Oma projekti Microsoft Foundry portaalis:

- **Project Endpoint** — Mine **Overview** lehele ja kopeeri lõpupunkti URL.

![Project Connection String](../../../translated_images/et/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Mine **Models + Endpoints** ja vali oma kasutusele võetud mudel, märgi üles **Deployment name** (nt `gpt-5-mini`).

### Samm 3: Logi sisse Azure'i kasutades `az login`

Enamik märkmikke autentib läbi sinu **Azure CLI sisselogimise** — kasutades `AzureCliCredential` või `DefaultAzureCredential` (mõlemad tuvastavad sinu `az login` seansi) `azure-identity` paketi kaudu — seega ei vaja nad API võtmeid. Mõned õppetunnid ja valikulised integratsioonid kasutavad API võtmeid; kontrolli iga õppetunni eeltingimusi täiendavate keskkonnamuutujate kohta. Selleks pead olema Azure CLI kaudu sisse logitud.

1. **Paigalda Azure CLI**, kui seda veel pole: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Logi sisse**, käivitades:

    ```bash
    az login
    ```

    Või kui oled kauges/Codespace keskkonnas ilma brauserita:

    ```bash
    az login --use-device-code
    ```

3. **Vali tellimus**, kui küsitakse — vali see, mille sees on sinu Foundry projekt.

4. **Kontrolli**, kas oled sisse logitud:

    ```bash
    az account show
    ```

> **Miks `az login`?** Märkmikud autentivad kasutades `AzureCliCredential` (või `DefaultAzureCredential`, mis ka tuvastab sinu Azure CLI sisselogimise) `azure-identity` paketi kaudu. See tähendab, et sinu Azure CLI seanss annab õigused — pole vaja API võtmeid ega salasid `.env` failis. See on [turvalisuse parim tava](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Samm 4: Loo oma `.env` fail

Kopeeri näidisfail:

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
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portaal → su projekt → **Overview** leht |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portaal → **Models + Endpoints** → sinu kasutusele võetud mudeli nimi |

Enamik õppetunde selles osas! Märkmikud autentivad automaatselt sinu `az login` seansi kaudu.

### Samm 5: Paigalda Python sõltuvused

```bash
pip install -r requirements.txt
```

Soovitame seda käivitada loodud virtuaalkeskkonnas.

## Valikuline seadistamine: Azure AI Search (õppetunnid 5 ja 16)

Õppetunni 5 (Agentic RAG) ja õppetunni 16 märkmikud töötavad kohe välja kastist koos **mälupõhise teadmistebaasiga** — lisa Azure ressursse pole vaja. Kui soovid need tegeliku **Azure AI Search** indeksiga katta, siis märgi, et **õppetunni 16 märkmik kasutab praegu võtme-põhist autentimist**: see lülitub mälupõhisest otsingust Azure AI Search-i alles siis, kui nii `AZURE_SEARCH_SERVICE_ENDPOINT` **kui** `AZURE_SEARCH_API_KEY` on määratud, muidu jääb see mälupõhisele otsingule. Seega, et seda kasutada reaalse indeksiga, pead seadistama administraatori võtme. Võtmevaba autentimine Microsoft Entra ID kaudu (RBAC) on soovitatud lähenemine sinu enda tootmiskoodis, vastavuses ülejäänud kursuses kasutatava `az login` vooga.

RBAC sammud allpool kehtivad juhendinäidiste ja sinu enda koodi seadistamisele. Need ei võimalda võtmevaba autentimist õppetunni 16 märkmikus; õppetund 16 vajab ikkagi nii lõpp-punkti kui ka administraatori võtit Azure AI Search kasutamiseks.

1. **Luba rollipõhine juurdepääs** oma otsinguteenusele:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Määra endale vajalikud rollid** (indeksite loomine/laadimine ja päringute tegemine):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Lisa lõpp-punkt** oma `.env` faili:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portaal → sinu **Azure AI Search** ressurss → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Vajalik (lõpp-punkti kõrval), et lubada Azure AI Search kasutamine õppetunni 16 märkmikus, mis kasutab võtme-põhist autentimist. Azure portaal → **Seaded** → **Võtmed** → põhijuhiloa võti |

> **Miks võtmevaba?** Admin võtmestid annavad täisõigused kirjutamiseks otsinguteenusele ja võivad lekkida `.env` failide kaudu. RBAC kasutamisel kasutatakse selle asemel sinu `az login` identiteeti — sama võtmevaba Entra ID mudelit, mida kursuse märkmikud kasutavad (`AzureCliCredential` / `DefaultAzureCredential`). Vaata [Ühenda Azure AI Search rollidega](https://learn.microsoft.com/azure/search/search-security-rbac).

Täielike indeksite loomise näidete jaoks pythoni ja .NETis vaata [Azure AI Search seadistusjuhendit](./AzureSearch.md).

## Täiendav seadistamine õppetundide jaoks, mis kutsuvad Azure OpenAI otse (õppetunnid 6 ja 8)

Mõned õppetundide 6 ja 8 märkmikud kutsuvad otse **Azure OpenAI** (kasutades **Responses API-t**) ilma Microsoft Foundry projektita. Need näited kasutasid varem GitHub Mudelite, mis nüüd on aegunud ega toeta Responses API-t. Lisa need muutujad oma `.env` faili:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portaal → sinu **Azure OpenAI** ressurss → **Keys and Endpoint** → Endpoint (nt `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Sinu kasutusele võetud mudeli nimi (nt `gpt-5-mini`), mis toetab Responses API-t |
| `AZURE_OPENAI_API_KEY` | Valikuline — ainult juhul, kui kasutad võtme-põhist autentimist `az login` / Entra ID asemel |

> Responses API kasutab stabiilset `/openai/v1/` lõpp-punkti, nii et `api-version` päringut pole vaja. Logi sisse `az login` abil, et kasutada võtmevaba Entra ID autentimist.

## Alternatiivne pakkuja: MiniMax (OpenAI-ga ühilduv)

[MiniMax](https://platform.minimaxi.com/) pakub suure konteksti mudeleid (kuni 204K tokenit) OpenAI-ga ühilduva API kaudu. Kuna Microsoft Agent Frameworki `OpenAIChatClient` töötab iga OpenAI-ga ühilduva lõpp-punktiga, võid MiniMaxi kasutada plug-and-play alternatiivina õppetundides, mis kasutavad `OpenAIChatClient`-i.

Lisa need muutujad oma `.env` faili:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax platvorm](https://platform.minimaxi.com/) → API võtmed |
| `MINIMAX_BASE_URL` | Kasuta `https://api.minimax.io/v1` (vaikimisi väärtus) |
| `MINIMAX_MODEL_ID` | Mudeli nimi kasutamiseks (nt `MiniMax-M3`) |

**Näidismudelid**: `MiniMax-M3` (soovitatav), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (kiiremad vastused). Mudelinimed ja saadavus võivad ajas muutuda ning juurdepääs mudelile võib sõltuda sinu kontost.

Koodinäited, mis kasutavad `OpenAIChatClient`-i (nt õppetunni 14 hotelli broneerimise töövoog) tuvastavad ja kasutavad automaatselt sinu MiniMax seadistust, kui `MINIMAX_API_KEY` on määratud.


## Alternatiivne teenusepakkuja: Novita AI (OpenAI-ühilduv)

[Novita AI](https://novita.ai/llm-api) pakub OpenAI-ühilduvat API-t avatud lähtekoodiga ja tipptasemel LLM-ide jaoks (DeepSeek, Llama, Qwen ja palju muud). Kuna Microsoft Agent Frameworki `OpenAIChatClient` töötab mis tahes OpenAI-ühilduva lõpp-punktiga, saate Novita AI-d kasutada Azure OpenAI või OpenAI aseainena.

Lisage need muutujad oma `.env` faili:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI juhtpaneel](https://novita.ai/settings/key-management) → API võtmed |
| `NOVITA_BASE_URL` | Kasutage `https://api.novita.ai/openai/v1` (vaikimisi väärtus) |
| `NOVITA_MODEL_ID` | Kasutatava mudeli nimi (näiteks `moonshotai/kimi-k3`) |

**Näidismudelid**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI majutab ka palju teisi avatud lähtekoodiga mudeliperekondi (Llama, Qwen, GLM ja palju muud) — vaadake [Novita AI mudelite raamatukogu](https://novita.ai/llm-api) praegust saadavate mudelite ja nende mudelinimede nimekirja.

Praegused näidised ei tarbi automaatselt `NOVITA_*` muutujaid. Novita AI kasutamiseks edastage need väärtused selgesõnaliselt `OpenAIChatClient` loomisel näidises, mida käitate.

## Alternatiivne teenusepakkuja: Foundry Local (Käivita mudelid seadmes)

[Foundry Local](https://foundrylocal.ai) on kergekaaluline jooksutuskeskkond, mis laadib alla, haldab ja teenindab keelemudeleid **täielikult teie enda masinas** OpenAI-ühilduva API kaudu — pilve ei ole vaja.

Kuna Microsoft Agent Frameworki `OpenAIChatClient` töötab mis tahes OpenAI-ühilduva lõpp-punktiga, on Foundry Local hea lokaalne asendus Azure OpenAI-le.

**1. Paigaldage Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Laadige alla ja käivitage mudel** (see käivitab ka kohaliku teenuse):

```bash
foundry model list          # saadaolevad mudelid
foundry model run phi-4-mini
```

**3. Paigaldage Python SDK**, mida kasutatakse kohaliku lõpp-punkti avastamiseks:

```bash
pip install foundry-local-sdk
```

**4. Määrake Microsoft Agent Framework suunama teie kohalikule mudelile:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Laadib alla (vajadusel) ja teenindab mudelit kohapeal, seejärel leiab lõpp-punkti/pordi.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # nt http://localhost:<port>/v1
    api_key=manager.api_key,        # alati "ei ole vajalik" Foundry Local'i jaoks
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Märkus:** Foundry Local pakub OpenAI-ühilduvat **Chat Completions** lõpp-punkti. Kasutage seda kohaliku arenduse ja võrguühenduseta stsenaariumides. Täieliku **Responses API** funktsioonide komplekti (olemuslikud vestlused jms) jaoks kasutage Azure OpenAI või Microsoft Foundry projekti.

## Lisa seadistamine õppetükile 8 (Bing Grounding töövoog)

Õppetüki 8 tingimuslikus töövoo märkmikus kasutatakse **Bing groundingut** Microsoft Foundry kaudu. Kui plaanite seda näidist käivitada, lisage see muutuja oma `.env` faili:

| Muutuja | Kus seda leida |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portaal → teie projekt → **Haldus** → **Ühendatud ressursid** → teie Bing ühendus → kopeerige ühenduse ID |

## Tõrkeotsing

### SSL-sertifikaadi kontrolli vead macOS-il

Kui kasutate macOS-i ja satute vea peale nagu:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

See on teadaolev probleem Pythoniga macOS-il, kus süsteemi SSL-sertifikaate ei usaldata automaatselt. Proovige järgnevaid lahendusi selles järjekorras:

**Variant 1: Käivitage Pythoni Install Certificates skript (soovitatav)**

```bash
# Asenda 3.XX oma paigaldatud Python'i versiooniga (nt 3.12 või 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Variant 2: Kasutage `connection_verify=False` oma märkmikus (ainult GitHubi mudelite märkmike puhul)**

Õppetüki 6 märkmikus (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) on kommenteeritud lahendus juba olemas. Eemaldage kommentaar `connection_verify=False` juurest, kui tekib sertifikaadivigu:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Keela SSL-kontroll, kui tekivad sertifikaadivead
)
```

> **⚠️ Tähelepanu:** SSL-sertifikaadi kontrolli keelamine (`connection_verify=False`) vähendab turvalisust, jättes sertifikaadi valideerimise vahele. Kasutage seda ainult ajutise lahendusena arenduskeskkondades. Ärge kunagi kasutage seda tootmises.

**Variant 3: Paigaldage ja kasutage `truststore`**

```bash
pip install truststore
```

Seejärel lisage järgnevad read oma märkmiku või skripti algusesse enne võrguühenduste tegemist:

```python
import truststore
truststore.inject_into_ssl()
```

## Jäägid kuskile kinni?

Kui teil esineb probleeme selle seadistuse käivitamisel, liituge meie <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI kogukonna Discordiga</a> või <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">looge probleem GitHubis</a>.

## Järgmine õppetükk

Olete nüüd valmis käivitama selle kursuse koodi. Head AI agentide maailma avastamist!

[Sissejuhatus AI agentidesse ja nende kasutusjuhtumitesse](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->