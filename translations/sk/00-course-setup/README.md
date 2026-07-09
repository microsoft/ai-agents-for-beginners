# Nastavenie kurzu

## Úvod

Táto lekcia pokryje, ako spustiť ukážky kódu tohto kurzu.

## Pripojte sa k iným študentom a získajte pomoc

Pred začatím klonovania vášho repozitára sa pripojte do [AI Agents For Beginners Discord kanála](https://aka.ms/ai-agents/discord), aby ste získali pomoc s nastavením, odpovede na otázky týkajúce sa kurzu alebo sa spojili s inými študentmi.

## Klonujte alebo forkajte tento repozitár

Pre začiatok, prosím, naklonujte alebo forknite GitHub repozitár. Tým si vytvoríte vlastnú verziu materiálov kurzu, aby ste mohli spúšťať, testovať a upravovať kód!

Toto môžete urobiť kliknutím na odkaz na <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forknutie repozitára</a>

Teraz by ste mali mať vlastnú fork-d verziu tohto kurzu na nasledujúcom odkaze:

![Forknutý repozitár](../../../translated_images/sk/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (odporúčané pre workshop / Codespaces)

  >Celý repozitár môže byť veľký (~3 GB), ak si stiahnete celú históriu a všetky súbory. Ak sa zúčastňujete iba workshopu alebo potrebujete len niekoľko lekčných priečinkov, shallow clone (alebo sparse clone) vám ušetrí väčšinu sťahovania obmedzením histórie a/alebo vynechaním blobov.

#### Rýchly shallow clone — minimálna história, všetky súbory

Nahraďte `<your-username>` v nasledujúcich príkazoch URL adresou vášho forku (alebo upstream URL, ak preferujete).

Na naklonovanie iba najnovšej histórie commitov (malé stiahnutie):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Na naklonovanie špecifickej vetvy:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Čiastočný (sparse) clone — minimálne bloby + len vybrané priečinky

Toto používa partial clone a sparse-checkout (vyžaduje Git 2.25+ a odporúča sa moderný Git s podporou partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Prejdite do priečinka repozitára:

```bash|powershell
cd ai-agents-for-beginners
```

Potom zadajte, ktoré priečinky chcete (príklad nižšie ukazuje dva priečinky):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonovaní a overení súborov, ak potrebujete iba súbory a chcete uvoľniť miesto (bez git histórie), vymažte metadáta repozitára (💀nezvratné — stratíte všetku funkcionalitu Gitu: žiadne commity, pull, push, ani prístup k histórii).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Použitie GitHub Codespaces (odporúčané na vyhnutie sa veľkým lokálnym sťahovaniam)

- Vytvorte nový Codespace pre tento repozitár cez [GitHub UI](https://github.com/codespaces).  

- V termináli novovytvoreného Codespace spustite jeden z shallow/sparse clone príkazov vyššie, aby ste dostali len potrebné lekčné priečinky do pracovného priestoru Codespaces.
- Voliteľné: po klonovaní v Codespaces odstráňte .git na uvoľnenie priestoru (pozri príkazy na odstránenie vyššie).
- Poznámka: Ak preferujete otvoriť repozitár priamo v Codespaces (bez ďalšieho klonovania), majte na pamäti, že Codespaces vytvorí devcontainer prostredie a môže poskytnúť viac, než potrebujete. Klonovanie shallow kópie v novom Codespace vám dáva väčšiu kontrolu nad použitím disku.

#### Tipy

- Vždy nahraďte klonovaciu URL URL vaším forkom, ak chcete upravovať alebo commitovať.
- Ak neskôr potrebujete viac histórie alebo súborov, môžete ich stiahnuť alebo upraviť sparse-checkout tak, aby zahŕňal ďalšie priečinky.

## Spúšťanie kódu

Tento kurz ponúka sériu Jupyter Notebookov, ktoré môžete spúšťať, aby ste získali praktické skúsenosti s budovaním AI agentov.

Ukážky kódu používajú **Microsoft Agent Framework (MAF)** s `FoundryChatClient`, ktorý sa pripája k **Microsoft Foundry Agent Service V2** (Responses API) cez **Microsoft Foundry**.

Všetky Python notebooky sú označené `*-python-agent-framework.ipynb`.

## Požiadavky

- Python 3.12+
  - **POZNÁMKA**: Ak nemáte nainštalovaný Python3.12, uistite sa, že ho nainštalujete. Potom vytvorte virtuálne prostredie pomocou python3.12, aby ste mali správne verzie podľa súboru requirements.txt.
  
    >Príklad

    Vytvorte adresár Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    Potom aktivujte venv prostredie pre:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Pre ukážkové kódy používajúce .NET, uistite sa, že ste nainštalovali [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) alebo novšiu verziu. Potom skontrolujte vašu verziu nainštalovaného .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Vyžaduje sa pre autentifikáciu. Nainštalujte z [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Pre prístup k Microsoft Foundry a Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Projekt s nasadeným modelom (napr. `gpt-4o`). Pozri [Krok 1](#krok-1-vytvorte-microsoft-foundry-projekt) nižšie.

V koreňovom adresári tohto repozitára sme zahrnuli súbor `requirements.txt`, ktorý obsahuje všetky potrebné Python balíky na spustenie ukážok kódu.

Môžete ich nainštalovať spustením nasledujúceho príkazu vo vašom termináli v koreňovom adresári repozitára:

```bash|powershell
pip install -r requirements.txt
```

Odporúčame vytvoriť Python virtuálne prostredie, aby ste sa vyhli konfliktom a problémom.

## Nastavenie VSCode

Uistite sa, že používate správnu verziu Pythonu vo VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavenie Microsoft Foundry a Microsoft Foundry Agent Service

### Krok 1: Vytvorte Microsoft Foundry projekt

Potrebujete Microsoft Foundry **hub** a **projekt** s nasadeným modelom na spustenie notebookov.

1. Choďte na [ai.azure.com](https://ai.azure.com) a prihláste sa so svojím Azure účtom.
2. Vytvorte **hub** (alebo použite existujúci). Pozrite: [Prehľad zdrojov hubu](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Vnútri hubu vytvorte **projekt**.
4. Nasadte model (napr. `gpt-4o`) cez **Models + Endpoints** → **Deploy model**.

### Krok 2: Získajte URL koncového bodu projektu a názov nasadenia modelu

Z vášho projektu v Microsoft Foundry portáli:

- **Project Endpoint** — Prejdite na stránku **Overview** a skopírujte URL koncového bodu.

![Reťazec pripojenia projektu](../../../translated_images/sk/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Prejdite na **Models + Endpoints**, vyberte nasadený model a zapíšte si **Deployment name** (napr. `gpt-4o`).

### Krok 3: Prihláste sa do Azure s `az login`

Všetky notebooky používajú **`AzureCliCredential`** na autentifikáciu — bez API kľúčov na správu. Vyžaduje to prihlásenie cez Azure CLI.

1. **Nainštalujte Azure CLI**, ak ešte nemáte: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prihláste sa** spustením:

    ```bash|powershell
    az login
    ```

    Alebo ak ste v remote/Codespace prostredí bez prehliadača:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vyberte svoju predplatné** ak budete vyzvaní — vyberte to obsahujúce váš Foundry projekt.

4. **Overte**, že ste prihlásený:

    ```bash|powershell
    az account show
    ```

> **Prečo `az login`?** Notebooky autentifikujú pomocou `AzureCliCredential` z balíka `azure-identity`. Znamená to, že vaša Azure CLI relácia poskytuje poverenia — žiadne API kľúče alebo tajomstvá v `.env` súbore. Toto je [bezpečnostná najlepšia prax](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Krok 4: Vytvorte svoj `.env` súbor

Skopírujte príkladový súbor:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Otvorte `.env` a vyplňte tieto dve hodnoty:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Premenná | Kde ju nájsť |
|----------|--------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portál → váš projekt → stránka **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portál → **Models + Endpoints** → názov nasadeného modelu |

To je všetko pre väčšinu lekcií! Notebooky sa budú automaticky autentifikovať cez vašu reláciu `az login`.

### Krok 5: Nainštalujte Python závislosti

```bash|powershell
pip install -r requirements.txt
```

Odporúčame toto spustiť vo virtuálnom prostredí, ktoré ste vytvorili.

## Dodatočné nastavenie pre Lekciu 5 (Agentic RAG)

Lekcia 5 používa **Azure AI Search** na retrieval-augmented generation. Ak plánujete túto lekciu spustiť, pridajte tieto premenne do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|--------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portál → váš zdroj **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portál → váš zdroj **Azure AI Search** → **Settings** → **Keys** → primárny administrátorský kľúč |

## Dodatočné nastavenie pre lekcie, ktoré volajú Azure OpenAI priamo (Lekcie 6 a 8)

Niektoré notebooky v lekciách 6 a 8 volajú **Azure OpenAI** priamo (používajú **Responses API**) namiesto prechodu cez projekt Microsoft Foundry. Tieto ukážky predtým používali GitHub Models, ktoré sú zastarané (ukončené v júli 2026) a nepodporujú Responses API. Ak plánujete spúšťať tieto ukážky, pridajte tieto premenne do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|--------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portál → váš zdroj **Azure OpenAI** → **Keys and Endpoint** → Endpoint (napr. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Názov vášho nasadeného modelu (napr. `gpt-4o-mini`), ktorý podporuje Responses API |
| `AZURE_OPENAI_API_KEY` | Voliteľné — len ak používate autentifikáciu pomocou kľúča namiesto `az login` / Entra ID |

> Responses API používa stabilný `/openai/v1/` endpoint, takže nie je potrebné `api-version`. Prihláste sa pomocou `az login` pre použitie autentifikácie bez kľúčov cez Entra ID.

## Alternatívny poskytovateľ: MiniMax (kompatibilný s OpenAI)

[MiniMax](https://platform.minimaxi.com/) poskytuje modely s veľkým kontextom (až 204K tokenov) cez OpenAI-kompatibilné API. Keďže Microsoft Agent Framework `OpenAIChatClient` funguje s akýmkoľvek OpenAI-kompatibilným endpointom, môžete použiť MiniMax ako plug-and-play alternatívu k Azure OpenAI alebo OpenAI.

Pridajte tieto premenne do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|--------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API kľúče |
| `MINIMAX_BASE_URL` | Použite `https://api.minimax.io/v1` (predvolená hodnota) |
| `MINIMAX_MODEL_ID` | Názov modelu na použitie (napr. `MiniMax-M3`) |

**Príklad modelov**: `MiniMax-M3` (odporúčané), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (rýchlejšie odpovede). Názvy modelov a dostupnosť sa môžu meniť v čase a prístup k danému modelu môže závisieť od vášho účtu alebo regiónu — skontrolujte [MiniMax Platform](https://platform.minimaxi.com/) pre aktuálny zoznam. Ak nie je `MiniMax-M3` dostupný pre váš účet, nastavte `MINIMAX_MODEL_ID` na model, ku ktorému máte prístup (napr. `MiniMax-M2.7`).

Ukážky kódu, ktoré používajú `OpenAIChatClient` (napr. pracovný tok rezervácie hotela v Lekcii 14) automaticky rozpoznajú a použijú vašu MiniMax konfiguráciu, keď je nastavený `MINIMAX_API_KEY`.

## Alternatívny poskytovateľ: Foundry Local (spúšťanie modelov na zariadení)

[Foundry Local](https://foundrylocal.ai) je ľahké runtime, ktoré sťahuje, spravuje a poskytuje jazykové modely **úplne na vašom vlastnom zariadení** cez OpenAI-kompatibilné API — žiadny cloud, žiadne predplatné Azure a žiadne API kľúče. Je to skvelá voľba pre offline vývoj, experimentovanie bez nákladov na cloud alebo pre uchovávanie dát priamo na zariadení.

Pretože Microsoft Agent Framework `OpenAIChatClient` funguje s akýmkoľvek OpenAI-kompatibilným endpointom, Foundry Local je plug-and-play lokálna alternatíva k Azure OpenAI.

**1. Nainštalujte Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Stiahnite a spustite model** (týmto sa tiež spustí lokálna služba):

```bash
foundry model list          # pozrieť dostupné modely
foundry model run phi-4-mini
```

**3. Nainštalujte Python SDK** používané na zistenie lokálneho endpointu:

```bash
pip install foundry-local-sdk
```

**4. Nastavte Microsoft Agent Framework na váš lokálny model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Stiahne (ak je to potrebné) a spustí model lokálne, potom zistí koncový bod/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # napr. http://localhost:<port>/v1
    api_key=manager.api_key,        # vždy "nie je vyžadovaný" pre Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Poznámka:** Foundry Local poskytuje OpenAI-kompatibilný endpoint pre **Chat Completions**. Použite ho pre lokálny vývoj a offline scenáre. Pre plnú funkcionalitu **Responses API** (stavové konverzácie, hlboká orchestrácia nástrojov a vývoj v štýle agenta) použite **Azure OpenAI** alebo **Microsoft Foundry** projekt ako je ukázané v lekciách. Viac informácií nájdete v [Foundry Local dokumentácii](https://foundrylocal.ai) o aktuálnom katalógu modelov a podpore platforiem.

## Dodatočné nastavenie pre Lekciu 8 (Bing Grounding Workflow)


Podmienený pracovný tok v notebooku lekcie 8 používa **Bing grounding** cez Microsoft Foundry. Ak plánujete spustiť tento príklad, pridajte túto premennú do vášho súboru `.env`:

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portál → váš projekt → **Správa** → **Pripojené zdroje** → vaše Bing pripojenie → skopírujte ID pripojenia |

## Riešenie problémov

### Chyby overenia SSL certifikátu na macOS

Ak používate macOS a narazíte na chybu ako:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Toto je známy problém s Pythonom na macOS, kde systémové SSL certifikáty nie sú automaticky dôveryhodné. Vyskúšajte nasledujúce riešenia v uvedenom poradí:

**Možnosť 1: Spustite skript Inštalácie certifikátov v Pythone (odporúčané)**

```bash
# Nahraďte 3.XX vašou nainštalovanou verziou Pythonu (napr. 3.12 alebo 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnosť 2: Použite `connection_verify=False` vo vašom notebooku (len pre GitHub Models notebooky)**

V notebooku Lekcie 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je už zahrnutý zakomentovaný obchádzajúci kód. Odkomentujte `connection_verify=False` pri vytváraní klienta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Vypnite overovanie SSL, ak narazíte na chyby v certifikáte
)
```

> **⚠️ Varovanie:** Vypnutie overenia SSL (`connection_verify=False`) znižuje bezpečnosť tým, že preskakuje validáciu certifikátu. Používajte to iba ako dočasné riešenie v prostredí vývoja, nikdy nie v produkcii.

**Možnosť 3: Nainštalujte a používajte `truststore`**

```bash
pip install truststore
```

Potom pridajte nasledovné na začiatok vášho notebooku alebo skriptu pred vykonaním akýchkoľvek sieťových volaní:

```python
import truststore
truststore.inject_into_ssl()
```

## Zasekli ste sa niekde?

Ak máte problémy so spustením tejto konfigurácie, vstúpte do nášho <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> alebo <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">vytvorte issue</a>.

## Ďalšia lekcia

Teraz ste pripravení spustiť kód pre tento kurz. Prajeme veľa radosti pri ďalšom spoznávaní sveta AI agentov!

[Úvod do AI agentov a prípadov použitia agentov](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->