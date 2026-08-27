# Nastavitev tečaja

## Uvod

Ta lekcija bo zajemala, kako zagnati primere kode tega tečaja.

## Pridružite se drugim učencem in prejmite pomoč

Preden začnete s kloniranjem vašega repozitorija, se pridružite [kanalu AI Agents For Beginners Discord](https://aka.ms/ai-agents/discord), da prejmete pomoč pri nastavitvi, odgovore na vprašanja o tečaju ali da se povežete z drugimi učenci.

## Klonirajte ali razvejajte ta repozitorij

Za začetek prosimo klonirajte ali naredite fork GitHub repozitorija. Tako boste imeli svojo verzijo gradiva tečaja, da boste lahko zagnali, testirali in spreminjali kodo!

To lahko storite s klikom na povezavo za <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repozitorija</a>

Zdaj bi morali imeti svojo verzijo forkanega tečaja na naslednji povezavi:

![Forked Repo](../../../translated_images/sl/forked-repo.33f27ca1901baa6a.webp)

### Plitki klon (priporočeno za delavnico / Codespaces)

  >Celoten repozitorij je lahko velik (~3 GB), če prenesete polno zgodovino in vse datoteke. Če boste prisotni le na delavnici ali potrebujete le nekaj map lekcij, plitki klon (ali redki klon) prenese mnogo manj.

#### Hiter plitki klon — minimalna zgodovina, vse datoteke

Nadomestite `<your-username>` v spodnjih ukazih z URL-jem vašega forka (ali z nadrejenim URL-jem, če želite).

Za kloniranje samo najnovejše zgodovine commitov (majhen prenos):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Za kloniranje določene veje:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delni (redki) klon — minimalni blobi + le izbrane mape

To uporablja delni klon in sparse-checkout (zahteva Git 2.25+ in priporočamo sodoben Git s podporo za delni klon):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pojdite v mapo repozitorija:

```bash
cd ai-agents-for-beginners
```

Nato določite, katere mape želite (primer spodaj prikazuje dve mapi):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po kloniranju in preverjanju datotek, če potrebujete samo datoteke in želite sprostiti prostor (brez git zgodovine), prosim izbrišite metapodatke repozitorija (💀nepopravljivo — izgubili boste vso git funkcionalnost):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Uporaba GitHub Codespaces (priporočeno za izogib lokalnim velikim prenosom)

- Ustvarite nov Codespace za ta repozitorij preko [GitHub UI](https://github.com/codespaces).  

- V terminalu novo ustvarjenega codespace zaženite enega od zgornjih ukazov za plitki/sparse klon, da pripeljete samo tiste mape lekcij, ki jih potrebujete v delovno okolje Codespace.
- Opcijsko: po kloniranju znotraj Codespaces, odstranite .git, da sprostite dodatni prostor (glejte ukaze za odstranjevanje zgoraj).
- Opomba: Če raje odprete repozitorij neposredno v Codespaces (brez dodatnega kloniranja), se zavedajte, da bo Codespaces sestavil okolje devcontainer in morda boste še vedno dobili več, kot potrebujete.

#### Nasveti

- Vedno zamenjajte URL kloniranja z vašim forkom, če želite urejati/commitati.
- Če kasneje potrebujete več zgodovine ali datotek, jih lahko pridobite ali prilagodite sparse-checkout za vključitev dodatnih map.

## Zagon kode

Ta tečaj ponuja vrsto Jupyter zvezkov, ki jih lahko zaženete za praktične izkušnje pri gradnji AI agentov.

Primeri kode uporabljajo **Microsoft Agent Framework (MAF)** s `FoundryChatClient`, ki se povezuje na **Microsoft Foundry Agent Service V2** (Responses API) preko **Microsoft Foundry**.

Vsi Python zvezki so označeni z `*-python-agent-framework.ipynb`.

## Zahteve

- Python 3.12+
  - **OPOMBA**: Če nimate nameščenega Pythona 3.12, ga namestite. Nato ustvarite virtualno okolje z python3.12, da zagotovite pravilne različice, nameščene iz datoteke requirements.txt.
  
    >Primer

    Ustvarite imenik za Python venv:

    ```bash
    python -m venv venv
    ```

    Nato aktivirajte venv okolje za:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Za primerne kode, ki uporabljajo .NET, poskrbite, da imate nameščen [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ali novejši. Nato preverite svojo nameščeno različico .NET SDK:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Zahtevano za preverjanje pristnosti. Namestite ga s [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure naročnina** — Za dostop do Microsoft Foundry in Microsoft Foundry Agent Service.
- **Microsoft Foundry projekt** — Projekt z nameščenim modelom (npr. `gpt-5-mini`). Glejte [Korak 1](#korak-1-ustvarite-projekt-microsoft-foundry) spodaj.

Vključili smo datoteko `requirements.txt` v root tega repozitorija, ki vsebuje vse zahtevane Python pakete za zagon primerov kode.

Namestite jih z zagonom naslednjega ukaza v terminalu v root repozitorija:

```bash
pip install -r requirements.txt
```

Priporočamo ustvarjanje virtualnega Python okolja, da se izognete konfliktnim težavam.

## Nastavitev VSCode

Prepričajte se, da uporabljate pravo različico Pythona v VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavitev Microsoft Foundry in Microsoft Foundry Agent Service

### Korak 1: Ustvarite projekt Microsoft Foundry

Potrebujete Microsoft Foundry **hub** in **projekt** z nameščenim modelom za zagon zvezkov.

1. Pojdite na [ai.azure.com](https://ai.azure.com) in se prijavite z vašim Azure računom.
2. Ustvarite **hub** (ali uporabite že obstoječega). Glejte: [Pregled virov Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Znotraj huba ustvarite **projekt**.
4. Namestite model (npr. `gpt-5-mini`) iz **Models + Endpoints** → **Deploy model**.

### Korak 2: Pridobite naslov vašega projekta in ime nameščenega modela

Iz vašega projekta v Microsoft Foundry portalu:

- **Project Endpoint** — Obiščite stran **Overview** in kopirajte URL končne točke.

![Project Connection String](../../../translated_images/sl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Ime implementacije modela** — Pojdite na **Models + Endpoints**, izberite vaš nameščen model in zabeležite **Deployment name** (npr. `gpt-5-mini`).

### Korak 3: Prijava v Azure z `az login`

Večina zvezkov preveri pristnost preko vaše **Azure CLI prijave** — z uporabo `AzureCliCredential` ali `DefaultAzureCredential` (oba uporabita vašo `az login` sejo) iz paketa `azure-identity` — zato ne zahtevajo API ključev. Nekaj lekcij in opcijskih integracij uporablja API ključe; preverite predpogoje vsake lekcije za dodatne spremenljivke okolja. Za to morate biti prijavljeni preko Azure CLI.

1. **Namestite Azure CLI**, če še niste: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prijavite se** z naslednjim ukazom:

    ```bash
    az login
    ```

    Ali če ste v oddaljenem/Codespaces okolju brez brskalnika:

    ```bash
    az login --use-device-code
    ```

3. **Izberite svojo naročnino**, če vas sistem vpraša — izberite tisto, ki vsebuje vaš Foundry projekt.

4. **Preverite**, da ste prijavljeni:

    ```bash
    az account show
    ```

> **Zakaj `az login`?** Zvezki se preverijo z `AzureCliCredential` (ali `DefaultAzureCredential`, ki prav tako vzame vašo Azure CLI prijavo) iz paketa `azure-identity`. To pomeni, da vaša seja Azure CLI zagotavlja poverilnice — brez API ključev ali skrivnosti v vaši `.env` datoteki. To je [najboljša praksa za varnost](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Korak 4: Ustvarite svojo `.env` datoteko

Kopirajte primer datoteke:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Odprite `.env` in izpolnite ti dve vrednosti:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → vaš projekt → stran **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → ime vašega nameščenega modela |

To je za večino lekcij! Zvezki se bodo samodejno avtorizirali preko vaše `az login` seje.

### Korak 5: Namestite Python odvisnosti

```bash
pip install -r requirements.txt
```

Priporočamo, da to zaženete znotraj virtualnega okolja, ki ste ga ustvarili prej.

## Dodatna nastavitev: Azure AI Search (Lekcije 5 in 16)

Lekcija 5 (Agentic RAG) in lekcija 16 zvezki delujejo takoj s **podatkovno bazo v pomnilniku** — brez dodatnih Azure virov. Če želite uporabiti pravi **Azure AI Search** indeks, upoštevajte, da lekcija 16 trenutno uporablja avtentikacijo preko ključa: preklopi iz iskanja v pomnilniku na Azure AI Search le, če sta nastavljena oba `AZURE_SEARCH_SERVICE_ENDPOINT` in `AZURE_SEARCH_API_KEY`, sicer ostane v iskanju v pomnilniku — zato morate za zagon na pravem indeksu nastaviti tudi skrbniški ključ. Avtentikacija brez ključa z Microsoft Entra ID (RBAC) je priporočeni pristop za vašo lastno produkcijsko kodo, skladen z `az login` tokom, ki se uporablja po celotnem tečaju.

Koraki RBAC spodaj veljajo za primere v vodiču po nastavitvi in vašo kodo. Ne omogočajo avtentikacije brez ključa v lekciji 16; lekcija 16 še vedno zahteva tako endpoint kot skrbniški ključ za uporabo Azure AI Search.

1. **Omogočite dostop na osnovi vlog** na vaši storitvi za iskanje:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Dodelite sebi zahtevane vloge** (ustvarjanje/nalaganje indeksov in poizvedbe):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Dodajte endpoint** v vašo `.env` datoteko:

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → vaš **Azure AI Search** vir → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Potreben (z endpointom) za omogočanje Azure AI Search v lekciji 16, ki uporablja avtentikacijo na osnovi ključa. Azure portal → **Nastavitve** → **Ključi** → primarni skrbniški ključ |

> **Zakaj brez ključa?** Skrbniški ključi omogočajo poln dostop za pisanje vaši storitvi za iskanje in lahko uidejo preko `.env` datotek. Z RBAC je uporabljena vaša `az login` identiteta — isti vzorec brez ključev Entra ID, ki ga uporabljajo zvezki (prek `AzureCliCredential` / `DefaultAzureCredential`). Glej [Povezovanje z Azure AI Search z uporabo vlog](https://learn.microsoft.com/azure/search/search-security-rbac).

Oglejte si [vodnik za nastavitve Azure AI Search](./AzureSearch.md) za polne primere ustvarjanja indeksov v Python in .NET.

## Dodatna nastavitev za lekcije, ki neposredno kličejo Azure OpenAI (lekcije 6 in 8)

Nekateri zvezki v lekcijah 6 in 8 kličejo **Azure OpenAI** neposredno (prek **Responses API**), namesto preko Microsoft Foundry projekta. Ti primeri so prej uporabljali GitHub Models, ki je zastarel in ne podpira Responses API. Dodajte te spremenljivke v vašo `.env` datoteko:

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → vaš **Azure OpenAI** vir → **Keys and Endpoint** → Endpoint (npr. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Ime vašega nameščenega modela (npr. `gpt-5-mini`), ki podpira Responses API |
| `AZURE_OPENAI_API_KEY` | Opcijsko — le če uporabljate avtentikacijo na osnovi ključa namesto `az login` / Entra ID |

> Responses API uporablja stabilen `/openai/v1/` endpoint, zato ni potrebna `api-version`. Prijavite se z `az login` za uporabo avtentikacije brez ključa Entra ID.

## Alternativni ponudnik: MiniMax (kompatibilen z OpenAI)

[MiniMax](https://platform.minimaxi.com/) nudi modele z velikim kontekstom (do 204K tokenov) preko API-ja, kompatibilnega z OpenAI. Ker Microsoft Agent Framework-ov `OpenAIChatClient` deluje z vsakim endpointom, kompatibilnim z OpenAI, lahko uporabite MiniMax kot zamenjavo za lekcije, ki uporabljajo `OpenAIChatClient`.

Dodajte te spremenljivke v vašo `.env` datoteko:

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API ključi |
| `MINIMAX_BASE_URL` | Uporabite `https://api.minimax.io/v1` (privzeta vrednost) |
| `MINIMAX_MODEL_ID` | Ime modela, ki ga želite uporabiti (npr. `MiniMax-M3`) |

**Primeri modelov**: `MiniMax-M3` (priporočeno), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (hitrejši odgovori). Imena modelov in razpoložljivost se lahko s časom spreminjajo, dostop pa je lahko odvisen od vašega računa.

Primeri kode, ki uporabljajo `OpenAIChatClient` (npr. delovni tok za rezervacijo hotela v lekciji 14), bodo samodejno zaznali in uporabili vašo MiniMax konfiguracijo, ko je nastavljen `MINIMAX_API_KEY`.


## Alternativni ponudnik: Foundry Local (zagon modelov na napravi)

[Foundry Local](https://foundrylocal.ai) je lahek runtime, ki prenese, upravlja in streže jezikovne modele **popolnoma na vašem računalniku** preko API-ja združljivega z OpenAI — brez potrebe po oblaku.

Ker Microsoft Agent Frameworkov `OpenAIChatClient` deluje z vsakim OpenAI-združljivim končnim točko, je Foundry Local lokalna alternativa Azure OpenAI, ki jo lahko preprosto zamenjate.

**1. Namestite Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Prenesite in zaženite model** (s tem se tudi zažene lokalna storitev):

```bash
foundry model list          # oglejte si razpoložljive modele
foundry model run phi-4-mini
```

**3. Namestite Python SDK**, ki se uporablja za odkrivanje lokalne končne točke:

```bash
pip install foundry-local-sdk
```

**4. Usmerite Microsoft Agent Framework na vaš lokalni model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Prenese (če je potrebno) in lokalno streže model, nato odkrije končno točko/vrata.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # npr. http://localhost:<port>/v1
    api_key=manager.api_key,        # vedno "ni potrebno" za Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Opomba:** Foundry Local ponuja OpenAI-združljivo končno točko za **Chat Completions**. Uporabite jo za lokalni razvoj in brez internetnih povezav. Za celoten nabor funkcij **Responses API** (npr. stanje pogovorov) uporabite Azure OpenAI ali Microsoft Foundry projekt.

## Dodatne nastavitve za Lekcijo 8 (Postopek Bing Grounding)

Kondicionalni zvezek v lekciji 8 uporablja **Bing grounding** preko Microsoft Foundry. Če nameravate zagnati ta primer, dodajte to spremenljivko v vašo `.env` datoteko:

| Spremenljivka | Kje jo najti |
|-------------|--------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → vaš projekt → **Management** → **Connected resources** → vaša Bing povezava → kopirajte ID povezave |

## Odpravljanje težav

### Napake preverjanja SSL potrdila na macOS

Če uporabljate macOS in naletite na napako, kot je:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Gre za znano težavo s Pythonom na macOS, kjer sistemska SSL potrdila niso samodejno zaupanja vredna. Poskusite naslednje rešitve v navedenem vrstnem redu:

**Možnost 1: Zaženite Pythonov skript za namestitev potrdil (priporočeno)**

```bash
# Zamenjajte 3.XX z vašo nameščeno različico Pythona (npr. 3.12 ali 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnost 2: Uporabite `connection_verify=False` v vašem zvezku (samo za GitHub Models zvezke)**

V zvezku Lekcije 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je že vključen zakomentiran zaobidni način. Odkomentirajte `connection_verify=False`, ko naletite na napake potrdil:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Onemogoči preverjanje SSL, če naletiš na napake s certifikatom
)
```

> **⚠️ Opozorilo:** Onemogočanje SSL preverjanja (`connection_verify=False`) zmanjša varnost, saj preskoči validacijo potrdila. Uporabljajte to le kot začasno rešitev v razvojnih okoljih. Nikoli ne uporabljajte v produkciji.

**Možnost 3: Namestite in uporabite `truststore`**

```bash
pip install truststore
```

Nato dodajte sledeče na začetek vašega zvezka ali skripte pred izvajanjem klicev omrežja:

```python
import truststore
truststore.inject_into_ssl()
```

## Se kje zataknete?

Če imate težave pri zagonu te nastavitve, se pridružite naši <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ali <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ustvarite novo težavo</a>.

## Naslednja lekcija

Zdaj ste pripravljeni za zagon kode za ta tečaj. Srečno pri učenju več o svetu AI agentov! 

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->