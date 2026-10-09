# Nastavitev tečaja

## Uvod

Ta lekcija bo zajemala, kako zagnati vzorce kode iz tega tečaja.

## Pridružite se drugim udeležencem in pridobite pomoč

Preden začnete s kloniranjem svojega repozitorija, se pridružite [AI Agents For Beginners Discord kanalu](https://aka.ms/ai-agents/discord), da dobite pomoč pri nastavitvi, odgovore na vprašanja o tečaju ali povezovanje z drugimi udeleženci.

## Klonirajte ali naredite forka tega repozitorija

Za začetek, prosim klonirajte ali naredite fork GitHub repozitorija. Tako boste ustvarili svojo različico gradiva tečaja, da lahko izvajate, preizkušate in prilagajate kodo!

To lahko storite tako, da kliknete povezavo do <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repozitorija</a>

Zdaj bi morali imeti svojo forkan različico tega tečaja na naslednji povezavi:

![Forked Repo](../../../translated_images/sl/forked-repo.33f27ca1901baa6a.webp)

### Plitki klon (priporočeno za delavnice / Codespaces)

  >Celoten repozitorij je lahko velik (~3 GB), če prenesete celotno zgodovino in vse datoteke. Če se udeležujete samo delavnice ali potrebujete samo nekaj lekcijskih map, plitki klon (ali redek klon) prenese veliko manj.

#### Hiter plitki klon — minimalna zgodovina, vse datoteke

Zamenjajte `<your-username>` v spodnjih ukazih z URL vašega forka (ali z upstream URL, če želite).

Za kloniranje samo najnovejše zgodovine potrditev (majhen prenos):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Za kloniranje določene veje:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delni (redeki) klon — minimalni blobi + samo izbrane mape

To uporablja delni klon in sparse-checkout (zahteva Git 2.25+ in priporočljivo moderno verzijo Gita s podporo delnih klonov):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Vstopite v mapo repozitorija:

```bash
cd ai-agents-for-beginners
```

Nato določite, katere mape želite (primer spodaj prikazuje dve mapi):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po kloniranju in preverjanju datotek, če potrebujete samo datoteke in želite sprostiti prostor (brez zgodovine Git), prosim izbrišite metapodatke repozitorija (💀nepovratno — izgubili boste vso funkcionalnost Gita):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Uporaba GitHub Codespaces (priporočeno za izogibanje velikim lokalnim prenosom)

- Ustvarite nov Codespace za ta repozitorij preko [GitHub UI](https://github.com/codespaces).  

- V terminalu novega codespace-a zaženite enega od zgornjih ukazov za plitki/redeki klon, da prenesete samo potrebne lekcijske mape v delovno okolje Codespace-a.
- Izbirno: po kloniranju znotraj Codespaces, odstranite .git, da sprostite dodaten prostor (glejte ukaze za odstranitev zgoraj).
- Opomba: če želite odpreti repozitorij neposredno v Codespaces (brez dodatnega kloniranja), vedite, da bo Codespaces konfiguriral razvojno okolje devcontainer in lahko še vedno pripravi več kot potrebujete.

#### Namigi

- Vedno zamenjajte URL klona s svojim forkom, če želite urejati/zapisovati.
- Če pozneje potrebujete več zgodovine ali datotek, jih lahko pridobite ali prilagodite sparse-checkout, da vključite dodatne mape.

## Zagon kode

Ta tečaj ponuja serijo Jupyter Notebookov, ki jih lahko zaženete za praktično izkušnjo gradnje AI agentov.

Vzorci kode uporabljajo **Microsoft Agent Framework (MAF)** s `FoundryChatClient`, ki se poveže z **Microsoft Foundry Agent Service V2** (Responses API) preko **Microsoft Foundry**.

Vsi Python noteboki so označeni kot `*-python-agent-framework.ipynb`.

## Zahteve

- Python 3.12+
  - **OPOMBA**: Če nimate nameščenega Python 3.12, ga prosim namestite. Nato ustvarite svoj venv z uporabo python3.12, da zagotovite pravilne verzije, namestitvene iz datoteke requirements.txt.
  
    >Primer

    Ustvarite Python venv mapo:

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

- .NET 10+: Za vzorčno kodo s .NET, poskrbite, da imate nameščen [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ali novejši. Nato preverite svojo naloženo verzijo .NET SDK:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Za avtentikacijo obvezno. Namestite ga iz [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure naročnina** — Za dostop do Microsoft Foundry in Microsoft Foundry Agent Service.
- **Microsoft Foundry projekt** — Projekt z nameščenim modelom (npr. `gpt-5-mini`). Glejte [Korak 1](#korak-1-ustvarite-microsoft-foundry-projekt) spodaj.

V tem repozitoriju je vključena datoteka `requirements.txt`, ki vsebuje vse potrebne Python pakete za zagon vzorcev kode.

Namestite jih lahko z izvajanjem naslednjega ukaza v terminalu na korenu repozitorija:

```bash
pip install -r requirements.txt
```

Priporočamo uporabo Python virtualnega okolja, da preprečite konflikte in težave.

## Nastavitev VSCode

Preverite, da uporabljate pravo verzijo Pythona v VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavitev Microsoft Foundry in Microsoft Foundry Agent Service

### Korak 1: Ustvarite Microsoft Foundry projekt

Potrebujete Microsoft Foundry **hub** in **projekt** z nameščenim modelom za zagon notebokov.

1. Pojdite na [ai.azure.com](https://ai.azure.com) in se prijavite s svojim Azure računom.
2. Ustvarite **hub** (ali uporabite obstoječega). Glejte: [Pregled virov hub-a](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Znotraj hub-a ustvarite **projekt**.
4. Namestite model (npr. `gpt-5-mini`) iz **Models + Endpoints** → **Deploy model**.

### Korak 2: Pridobite URL končne točke projekta in ime nameščenega modela

Iz vašega projekta v Microsoft Foundry portalu:

- **Project Endpoint** — Pojdite na stran **Overview** in skopirajte URL končne točke.

![Project Connection String](../../../translated_images/sl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Pojdite na **Models + Endpoints**, izberite nameščen model in zabeležite **Deployment name** (npr. `gpt-5-mini`).

### Korak 3: Prijavite se v Azure z `az login`

Večina notebokov se avtenticira preko vaše **Azure CLI prijave** — z uporabo `AzureCliCredential` ali `DefaultAzureCredential` (oba uporabita vašo `az login` sejo) iz paketa `azure-identity` — zato ne zahtevajo API ključev. Nekaj lekcij in izbirnih integracij uporablja API ključe; zaželite preveriti predpogoje posamezne lekcije za dodatne okoljske spremenljivke. Zahteva, da ste prijavljeni preko Azure CLI.

1. **Namestite Azure CLI**, če ga še nimate: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prijavite se** z zagonom:

    ```bash
    az login
    ```

    Ali če ste v oddaljenem/Codespace okolju brez brskalnika:

    ```bash
    az login --use-device-code
    ```

3. **Izberite naročnino**, če ste pozvani — izberite tisto, ki vsebuje vaš Foundry projekt.

4. **Preverite** svojo prijavo:

    ```bash
    az account show
    ```

> **Zakaj `az login`?** Noteboki se avtenticirajo z uporabo `AzureCliCredential` (ali `DefaultAzureCredential`, ki prav tako uporabi vašo Azure CLI prijavo) iz `azure-identity` paketa. To pomeni, da vaš Azure CLI session zagotavlja poverilnice — brez API ključev ali skrivnosti v datoteki `.env`. To je [najboljša varnostna praksa](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

To je vse za večino lekcij! Noteboki se bodo samodejno avtenticirali preko vaše `az login` seje.

### Korak 5: Namestite Python odvisnosti

```bash
pip install -r requirements.txt
```

Priporočamo, da ta ukaz zaženete znotraj virtualnega okolja, ki ste ga prej ustvarili.

## Izbirna nastavitev: Azure AI Search (Lekcije 5 in 16)

Lekcija 5 (Agentic RAG) in Lekcija 16 noteboki delujejo brez dodatnih Azure virov z **vzporednim pomnilniškim podatkovnim registrom** — brez dodatnih Azure virov. Če jih želite podpreti z resničnim **Azure AI Search** indeksom, opazite, da **Lekcija 16 trenutni uporablja avtentikacijo na podlagi ključev**: preklopi iz iskanja v pomnilniku na Azure AI Search samo takrat, ko sta nastavljena **oba** `AZURE_SEARCH_SERVICE_ENDPOINT` **in** `AZURE_SEARCH_API_KEY`, sicer ostane na iskanju v pomnilniku — za zagon proti resničnemu indeksu morate torej nastaviti tudi administratorski ključ. Avtentikacija brez ključev z Microsoft Entra ID (RBAC) je priporočeni pristop za vašo lastno produkcijsko kodo, v skladu s tokom `az login`, ki se uporablja drugod v tem tečaju.

Koraki RBAC spodaj veljajo za vzorčne primere v vodiču in vašo lastno kodo. Ne omogočajo brezključne avtentikacije v Lekciji 16 noteboku; Lekcija 16 še vedno zahteva oba, končno točko in administratorski ključ, za uporabo Azure AI Search.

1. **Omogočite dostop na podlagi vlog** za vašo storitev za iskanje:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Dodelite sebi zahtevane vloge** (ustvarjanje/nalaganje indeksov in poizvedbe):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Dodajte končno točko** v vašo datoteko `.env`:

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → vaš **Azure AI Search** vir → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Obvezno (z endpoint) za omogočanje Azure AI Search v Lekciji 16 noteboku, ki uporablja avtentikacijo na podlagi ključev. Azure portal → **Settings** → **Keys** → primarni administratorski ključ |

> **Zakaj brez ključev?** Administratorski ključi omogočajo popoln zapisni dostop do vaše storitve za iskanje in se lahko razkrijejo prek `.env` datotek. Z RBAC se namesto tega uporablja vaša identiteta `az login` — isti brezključni vzorec Entra ID, ki ga uporabljajo noteboki tečaja (prek `AzureCliCredential` / `DefaultAzureCredential`). Glejte [Povezava do Azure AI Search z uporabo vlog](https://learn.microsoft.com/azure/search/search-security-rbac).

Oglejte si [vodnik za nastavitev Azure AI Search](./AzureSearch.md) za popolne primere ustvarjanja indeksov v Pythonu in .NET.

## Dodatna nastavitev za lekcije, ki kličejo Azure OpenAI neposredno (Lekcije 6 in 8)

Nekateri noteboki v lekcijah 6 in 8 kličejo **Azure OpenAI** neposredno (prek **Responses API**) namesto preko Microsoft Foundry projekta. Ti vzorci so prej uporabljali modele GitHub, ki so zastareli in ne podpirajo Responses API. Dodajte te spremenljivke v vašo datoteko `.env`:

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → vaš **Azure OpenAI** vir → **Keys and Endpoint** → Endpoint (npr. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Ime vašega nameščenega modela (npr. `gpt-5-mini`), ki podpira Responses API |
| `AZURE_OPENAI_API_KEY` | Izbirno — samo če uporabljate avtentikacijo na podlagi ključev namesto `az login` / Entra ID |

> Responses API uporablja stabilno `/openai/v1/` končno točko, zato `api-version` ni potreben. Prijavite se z `az login` za uporabo brezključne avtentikacije Entra ID.

## Alternativni ponudnik: MiniMax (kompatibilen z OpenAI)

[MiniMax](https://platform.minimaxi.com/) ponuja modele z velikim kontekstom (do 204K tokenov) preko OpenAI-kompatibilnega API. Ker Microsoft Agent Framework-ov `OpenAIChatClient` deluje z vsako OpenAI-kompatibilno končno točko, lahko MiniMax uporabite kot vstavno alternativo za lekcije, ki uporabljajo `OpenAIChatClient`.

Dodajte te spremenljivke v vašo datoteko `.env`:

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API ključi |
| `MINIMAX_BASE_URL` | Uporabite `https://api.minimax.io/v1` (privzeta vrednost) |
| `MINIMAX_MODEL_ID` | Ime modela za uporabo (npr. `MiniMax-M3`) |

**Primer modelov**: `MiniMax-M3` (priporočeno), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (hitrejši odzivi). Imena modelov in razpoložljivost se lahko sčasoma spreminjata, dostop do določenega modela je odvisen od vašega računa.

Vzorci kode, ki uporabljajo `OpenAIChatClient` (npr. Lekcija 14, potek rezervacije hotela), bodo samodejno zaznali in uporabili vašo MiniMax konfiguracijo, ko je nastavljen `MINIMAX_API_KEY`.


## Alternativni ponudnik: Novita AI (združljiv z OpenAI)

[Novita AI](https://novita.ai/llm-api) ponuja API, združljiv z OpenAI, za odprtokodne in najnovejše LLM-je (DeepSeek, Llama, Qwen in druge). Ker Microsoft Agent Frameworkov `OpenAIChatClient` deluje z vsakim vmesnikom, združljivim z OpenAI, lahko Novita AI uporabljate kot neposredno alternativo Azure OpenAI ali OpenAI.

Dodajte te spremenljivke v vašo `.env` datoteko:

| Spremenljivka | Kje jo najti |
|--------------|-------------|
| `NOVITA_API_KEY` | [Novita AI Nadzorna plošča](https://novita.ai/settings/key-management) → API ključi |
| `NOVITA_BASE_URL` | Uporabite `https://api.novita.ai/openai/v1` (privzeta vrednost) |
| `NOVITA_MODEL_ID` | Ime modela za uporabo (npr. `moonshotai/kimi-k3`) |

**Primeri modelov**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI prav tako gosti številne druge družine odprtokodnih modelov (Llama, Qwen, GLM in več) — preverite [knjižnico modelov Novita AI](https://novita.ai/llm-api) za trenutni seznam razpoložljivih modelov in njihovih ID-jev.

Trenutni primeri ne uporabljajo samodejno spremenljivk `NOVITA_*`. Za uporabo Novita AI te vrednosti explicitno posredujte pri ustvarjanju `OpenAIChatClient` v primeru, ki ga izvajate.

## Alternativni ponudnik: Foundry Local (zaženite modele na napravi)

[Foundry Local](https://foundrylocal.ai) je lahka izvedba, ki prenese, upravlja in streže jezikovne modele **popolnoma na vašem računalniku** preko vmesnika, združljivega z OpenAI — oblak ni potreben.

Ker Microsoft Agent Frameworkov `OpenAIChatClient` deluje z vsakim vmesnikom, združljivim z OpenAI, je Foundry Local lokalna alternativa za Azure OpenAI.

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

**3. Namestite Python SDK**, ki omogoča odkrivanje lokalne točke:

```bash
pip install foundry-local-sdk
```

**4. Usmerite Microsoft Agent Framework na vaš lokalni model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Prenese (če je potrebno) in lokalno streže model ter nato odkrije končno točko/vrata.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # npr. http://localhost:<port>/v1
    api_key=manager.api_key,        # vedno "ni zahtevano" za Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Opomba:** Foundry Local omogoča vmesnik OpenAI, združljiv z **Chat Completions**. Uporabite ga za lokalni razvoj in primere brez povezave. Za celoten nabor funkcij **Responses API** (stanje pogovorov itd.) uporabite Azure OpenAI ali Microsoft Foundry projekt.

## Dodatna nastavitev za lekcijo 8 (delovni tok Bing Grounding)

Pogojevalni delovni zvezek v lekciji 8 uporablja **Bing grounding** preko Microsoft Foundry. Če nameravate zagnati ta primer, dodajte to spremenljivko v vašo `.env` datoteko:

| Spremenljivka | Kje jo najti |
|--------------|-------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → vaš projekt → **Upravljanje** → **Povezani viri** → vaša Bing povezava → kopirajte ID povezave |

## Reševanje težav

### Napake pri preverjanju SSL certifikatov na macOS

Če uporabljate macOS in naletite na napako, kot je:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

To je znana težava s Python na macOS, kjer sistemski SSL certifikati niso samodejno zaupanja vredni. Poskusite naslednje rešitve v tem vrstnem redu:

**Možnost 1: Zaženite Pythonov skript za namestitev certifikatov (priporočeno)**

```bash
# Zamenjajte 3.XX z vašo nameščeno različico Pythona (npr. 3.12 ali 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnost 2: Uporabite `connection_verify=False` v vašem zvezku (samo za GitHub Models zvezke)**

V zvezku lekcije 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je že vključen komentar za začasno rešitev. Odkomentirajte `connection_verify=False`, ko naletite na napake certifikatov:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Onemogoči preverjanje SSL, če naletiš na napake s certifikatom
)
```

> **⚠️ Opozorilo:** Onemogočanje preverjanja SSL (`connection_verify=False`) zmanjša varnost, saj preskoči validacijo certifikatov. To uporabite samo kot začasno rešitev v razvojnih okoljih. V produkciji nikoli ne uporabljajte.

**Možnost 3: Namestite in uporabite `truststore`**

```bash
pip install truststore
```

Nato dodajte naslednje na začetek vašega zvezka ali skripte pred izvajanjem omrežnih klicev:

```python
import truststore
truststore.inject_into_ssl()
```

## Ste zataknjeni?

Če imate kakršnekoli težave pri zagonu te nastavitve, se pridružite našemu <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ali <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ustvarite zahtevek</a>.

## Naslednja lekcija

Sedaj ste pripravljeni zagnati kodo tega tečaja. Veselo učenje več o svetu AI agentov!

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->