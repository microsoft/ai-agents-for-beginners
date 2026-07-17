# Nastavenie kurzu

## Úvod

Táto lekcia pokrýva, ako spustiť ukážkové kódy tohto kurzu.

## Pripojte sa k ďalším študentom a získajte pomoc

Pred tým, ako začnete klonovať svoj repozitár, pripojte sa k [kanálu AI Agents For Beginners na Discorde](https://aka.ms/ai-agents/discord), aby ste získali pomoc pri nastavení, odpovede na otázky týkajúce sa kurzu alebo sa spojili s ostatnými študentmi.

## Klonovanie alebo Forknutie tohto repozitára

Na začiatok prosím klonujte alebo forkňte GitHub repozitár. Tým si vytvoríte vlastnú verziu materiálu kurzu, aby ste mohli spúšťať, testovať a upravovať kód!

To môžete spraviť kliknutím na odkaz na <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forknutie repozitára</a>

Teraz by ste mali mať vlastnú fork danej verzie kurzu na tomto odkaze:

![Forknutý repozitár](../../../translated_images/sk/forked-repo.33f27ca1901baa6a.webp)

### Povrchové klonovanie (odporúčané pre workshop / Codespaces)

  > Celý repozitár môže byť veľký (~3 GB), keď si stiahnete celú históriu a všetky súbory. Ak sa zúčastňujete iba workshopu alebo potrebujete len niekoľko lekčných priečinkov, povrchové klonovanie (alebo čiastočné klonovanie) sa vyhne veľkej väčšine sťahovania obmedzením histórie a/alebo preskočením blobov.

#### Rýchle povrchové klonovanie — minimálna história, všetky súbory

Nahradiť `<your-username>` v nižšie uvedených príkazoch URL vašej forknutej verzie (alebo upstream URL, ak preferujete).

Na naklonovanie iba najnovšej histórie commitov (malé sťahovanie):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Na naklonovanie konkrétnej vetvy:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Čiastočné (sparse) klonovanie — minimálne bloby + iba vybrané priečinky

Toto používa čiastočné klonovanie a sparse-checkout (vyžaduje Git 2.25+ a odporúča sa moderný Git s podporou čiastočného klonovania):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Prejdite do priečinka repozitára:

```bash|powershell
cd ai-agents-for-beginners
```

Potom špecifikujte, ktoré priečinky chcete (príklad nižšie ukazuje dva priečinky):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po sklonovaní a overení súborov, ak potrebujete iba súbory a chcete uvoľniť miesto (bez histórie git), odstráňte metadáta repozitára (💀nerozchoditeľné — stratíte celú funkčnosť Gitu: žiadne commity, pull, push ani prístup k histórii).

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

- V termináli novo vytvoreného codespace spustite jeden z príkazov pre povrchové/čiastočné klonovanie vyššie, aby ste do pracovného priestoru Codespace priniesli iba potrebné lekčné priečinky.
- Voliteľné: po klonovaní v Codespaces odstráňte priečinok .git, aby ste získali viac miesta (pozrite si príkazy na odstránenie vyššie).
- Poznámka: Ak preferujete otvoriť repozitár priamo v Codespaces (bez ďalšieho klonovania), vedzte, že Codespaces vytvorí prostredie devcontainer a môže stále pripraviť viac než potrebujete. Klonovanie povrchovej kópie v novom Codespace vám dáva väčšiu kontrolu nad využitím disku.

#### Tipy

- Vždy nahraďte URL klonu vašim fork, ak chcete editovať/commitovať.
- Ak neskôr potrebujete viac histórie alebo súborov, môžete ich načítať alebo upraviť sparse-checkout na zahrnutie ďalších priečinkov.

## Spúšťanie kódu

Tento kurz ponúka sériu Jupyter notebookov, ktoré môžete spustiť na získanie praktických skúseností s tvorbou AI agentov.

Ukážkové kódy používajú **Microsoft Agent Framework (MAF)** s `FoundryChatClient`, ktorý sa pripája na **Microsoft Foundry Agent Service V2** (Responses API) prostredníctvom **Microsoft Foundry**.

Všetky Python notebooky sú označené ako `*-python-agent-framework.ipynb`.

## Požiadavky

- Python 3.12+
  - **POZNÁMKA**: Ak nemáte nainštalovaný Python 3.12, uistite sa, že ho nainštalujete. Potom vytvorte venv pomocou python3.12, aby ste mali správne verzie z requirements.txt.
  
    >Príklad

    Vytvorte priečinok pre Python venv:

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

- .NET 10+: Pre ukážkové kódy používajúce .NET, uistite sa, že máte nainštalovaný [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) alebo novší. Potom skontrolujte verziu nainštalovaného .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Povinné pre autentifikáciu. Nainštalujte z [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Pre prístup k Microsoft Foundry a Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Projekt s nasadeným modelom (napr. `gpt-4.1-mini`). Pozri [Krok 1](#krok-1-vytvorte-microsoft-foundry-projekt) nižšie.

V koreňovom priečinku repozitára nájdete súbor `requirements.txt`, ktorý obsahuje všetky potrebné Python balíčky na spustenie ukážkových kódov.

Môžete ich nainštalovať spustením nasledujúceho príkazu v termináli v koreňovom priečinku repozitára:

```bash|powershell
pip install -r requirements.txt
```

Odporúčame vytvoriť Python virtuálne prostredie, aby ste sa vyhli konfliktom a problémom.

## Nastavenie VSCode

Uistite sa, že vo VSCode používate správnu verziu Pythonu.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavenie Microsoft Foundry a Microsoft Foundry Agent Service

### Krok 1: Vytvorte Microsoft Foundry Projekt

Na spustenie notebookov potrebujete Microsoft Foundry **hub** a **projekt** s nasadeným modelom.

1. Choďte na [ai.azure.com](https://ai.azure.com) a prihláste sa so svojim Azure účtom.
2. Vytvorte **hub** (alebo použite existujúci). Pozrite: [Prehľad zdrojov Hubu](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Vnútri hubu vytvorte **projekt**.
4. Nasadte model (napr. `gpt-4.1-mini`) cez **Models + Endpoints** → **Deploy model**.

### Krok 2: Získajte URL endpointu projektu a názov nasadeného modelu

Z vášho projektu v portále Microsoft Foundry:

- **Project Endpoint** — Choďte na stránku **Prehľad (Overview)** a skopírujte URL endpointu.

![Project Connection String](../../../translated_images/sk/project-endpoint.8cf04c9975bbfbf1.webp)

- **Názov nasadenia modelu** — Choďte na **Models + Endpoints**, vyberte nasadený model a zaznamenajte si **Deployment name** (napr. `gpt-4.1-mini`).

### Krok 3: Prihláste sa do Azure cez `az login`

Všetky notebooky používajú na autentifikáciu **`AzureCliCredential`** — nie je potrebné spravovať API kľúče. Vyžaduje to vaše prihlásenie cez Azure CLI.

1. **Nainštalujte Azure CLI**, ak ho ešte nemáte: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prihláste sa** spustením:

    ```bash|powershell
    az login
    ```

    Alebo ak ste v remote/Codespace prostredí bez prehliadača:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vyberte svoj subscription**, ak ste vyzvaní – vyberte ten, v ktorom je váš Foundry projekt.

4. **Overte**, že ste prihlásení:

    ```bash|powershell
    az account show
    ```

> **Prečo `az login`?** Notebooky sa autentifikujú pomocou `AzureCliCredential` z balíka `azure-identity`. To znamená, že vaša Azure CLI relácia poskytuje poverenia — nie sú potrebné API kľúče alebo tajomstvá v `.env` súbore. Toto je [najlepšia bezpečnostná prax](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Krok 4: Vytvorte svoj `.env` súbor

Skopírujte príklad súboru:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Otvorte `.env` a doplňte tieto dve hodnoty:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → váš projekt → stránka **Prehľad (Overview)** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → názov vášho nasadeného modelu |

To je všetko pre väčšinu lekcií! Notebooky sa automaticky autentifikujú cez vašu reláciu `az login`.

### Krok 5: Nainštalujte závislosti Pythonu

```bash|powershell
pip install -r requirements.txt
```

Odporúčame spustiť toto vo vnútri virtuálneho prostredia, ktoré ste si vytvorili.

## Dodatočné nastavenie pre Lekciu 5 (Agentic RAG)

Lekcia 5 používa **Azure AI Search** pre retrieval-augmented generation. Ak plánujete spustiť túto lekciu, pridajte tieto premenne do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portál → váš zdroj **Azure AI Search** → **Prehľad (Overview)** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portál → váš zdroj **Azure AI Search** → **Nastavenia (Settings)** → **Kľúče (Keys)** → primárny admin kľúč |

## Dodatočné nastavenie pre lekcie, ktoré volajú Azure OpenAI priamo (Lekcie 6 a 8)

Niektoré notebooky v lekciách 6 a 8 volajú **Azure OpenAI** priamo (pomocou **Responses API**), namiesto toho, aby išli cez Microsoft Foundry projekt. Tieto vzory predtým používali GitHub Models, ktoré sú zastarané (ukončenie júla 2026) a nepodporujú Responses API. Ak chcete spustiť tieto vzory, pridajte tieto premenne do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portál → váš zdroj **Azure OpenAI** → **Kľúče a Endpointy (Keys and Endpoint)** → Endpoint (napr. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Názov vášho nasadeného modelu (napr. `gpt-4.1-mini`), ktorý podporuje Responses API |
| `AZURE_OPENAI_API_KEY` | Voliteľné — len ak používate autentifikáciu na základe kľúča namiesto `az login` / Entra ID |

> Responses API používa stabilný endpoint `/openai/v1/`, preto nie je potrebné `api-version`. Prihláste sa pomocou `az login` pre použitie bezklúčovej autentifikácie Entra ID.

## Alternatívny poskytovateľ: MiniMax (kompatibilný s OpenAI)

[MiniMax](https://platform.minimaxi.com/) poskytuje modely s veľkým kontextom (až 204 tisíc tokenov) cez API kompatibilné s OpenAI. Pretože Microsoft Agent Framework `OpenAIChatClient` funguje s akýmkoľvek endpointom kompatibilným s OpenAI, môžete použiť MiniMax ako náhradnú alternatívu k Azure OpenAI alebo OpenAI.

Pridajte tieto premenne do svojho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API kľúče |
| `MINIMAX_BASE_URL` | Použite `https://api.minimax.io/v1` (predvolená hodnota) |
| `MINIMAX_MODEL_ID` | Názov modelu na použitie (napr. `MiniMax-M3`) |

**Príklad modelov**: `MiniMax-M3` (odporúčaný), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (rýchlejšie odpovede). Názvy modelov a ich dostupnosť sa môžu v priebehu času meniť a prístup k danému modelu môže závisieť od vášho účtu alebo regiónu — pozrite si aktuálny zoznam na [MiniMax Platform](https://platform.minimaxi.com/). Ak nie je `MiniMax-M3` pre váš účet dostupný, nastavte `MINIMAX_MODEL_ID` na model, ku ktorému máte prístup (napr. `MiniMax-M2.7`).

Ukážkové kódy používajúce `OpenAIChatClient` (napr. pracovný tok rezervácie hotela v Lekcii 14) automaticky rozpoznajú a použijú vašu konfiguráciu MiniMax po nastavení `MINIMAX_API_KEY`.

## Alternatívny poskytovateľ: Foundry Local (prevádzka modelov na zariadení)

[Foundry Local](https://foundrylocal.ai) je ľahké runtime prostredie, ktoré sťahuje, spravuje a poskytuje jazykové modely **úplne na vašom vlastnom zariadení** cez OpenAI kompatibilné API — žiadny cloud, žiadne Azure predplatné a žiadne API kľúče. Je to skvelá možnosť pre offline vývoj, experimentovanie bez cloudových nákladov alebo uchovávanie dát lokálne.

Pretože Microsoft Agent Framework `OpenAIChatClient` funguje s akýmkoľvek OpenAI kompatibilným endpointom, Foundry Local je lokálna drop-in alternatíva k Azure OpenAI.

**1. Inštalujte Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Stiahnite a spustite model** (tým sa tiež spustí lokálna služba):

```bash
foundry model list          # pozrieť dostupné modely
foundry model run phi-4-mini
```

**3. Nainštalujte Python SDK** používaný na zistenie lokálneho endpointu:

```bash
pip install foundry-local-sdk
```

**4. Nastavte Microsoft Agent Framework na váš lokálny model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Stiahne (ak je potrebné) a spustí model lokálne, potom nájde koncový bod/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # napr. http://localhost:<port>/v1
    api_key=manager.api_key,        # vždy "nie je potrebné" pre Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Poznámka:** Foundry Local poskytuje OpenAI-kompatibilný endpoint pre **Chat Completions**. Použite ho pre lokálny vývoj a offline scenáre. Pre plnú funkcionalitu **Responses API** (stavové konverzácie, hlboká orchestrácia nástrojov a vývoj štýlu agentov) cielite na **Azure OpenAI** alebo **Microsoft Foundry** projekt, ako je ukázané v lekciách. Pozrite si [Foundry Local dokumentáciu](https://foundrylocal.ai) pre aktuálny katalog modelov a podporu platforiem.


## Dodatočné nastavenie pre lekciu 8 (Bing Grounding Workflow)

Podmienený pracovný tok v lekcii 8 používa **Bing grounding** cez Microsoft Foundry. Ak plánujete spustiť tento príklad, pridajte túto premennú do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|--------------|
| `BING_CONNECTION_ID` | Portál Microsoft Foundry → váš projekt → **Management** → **Connected resources** → vaše Bing pripojenie → skopírujte ID pripojenia |

## Riešenie problémov

### Chyby overovania SSL certifikátu na macOS

Ak používate macOS a narazíte na chybu ako:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Toto je známy problém s Pythonom na macOS, kde systémové SSL certifikáty nie sú automaticky dôveryhodné. Vyskúšajte nasledujúce riešenia postupne:

**Možnosť 1: Spustite Python script na inštaláciu certifikátov (odporúčané)**

```bash
# Nahraďte 3.XX vašou nainštalovanou verziou Pythonu (napr. 3.12 alebo 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnosť 2: Použite `connection_verify=False` vo vašom notebooku (platí len pre GitHub Models notebooky)**

V notebooku Lekcia 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je už zahrnutý zakomentovaný obchádzkový spôsob. Odkomentujte `connection_verify=False` pri vytváraní klienta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Vypnite overovanie SSL, ak narazíte na chyby certifikátu
)
```

> **⚠️ Varovanie:** Vypnutie SSL overovania (`connection_verify=False`) znižuje bezpečnosť tým, že preskočí validáciu certifikátu. Používajte to iba ako dočasné riešenie vo vývojovom prostredí, nikdy v produkcii.

**Možnosť 3: Nainštalujte a používajte `truststore`**

```bash
pip install truststore
```

Potom pridajte nasledujúce na začiatok vášho notebooku alebo skriptu pred vykonaním akejkoľvek sieťovej komunikácie:

```python
import truststore
truststore.inject_into_ssl()
```

## Zasekli ste sa niekde?

Ak máte nejaké problémy pri spustení tohto nastavenia, vstúpte do našej <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> alebo <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">vytvorte issue</a>.

## Ďalšia lekcia

Teraz ste pripravení spustiť kód pre tento kurz. Prajeme veľa úspechov pri ďalšom spoznávaní sveta AI agentov!

[Úvod do AI Agentov a prípadov použitia agentov](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->