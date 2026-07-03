# Nastavenie kurzu

## Úvod

Táto lekcia bude pokrývať, ako spustiť ukážkové kódy tohto kurzu.

## Pridajte sa k ostatným študentom a získajte pomoc

Predtým, než začnete klonovať svoje úložisko, pridajte sa do [AI Agents For Beginners Discord kanála](https://aka.ms/ai-agents/discord), kde môžete získať pomoc s nastavením, položiť otázky týkajúce sa kurzu alebo sa spojiť s ostatnými študentmi.

## Klonovanie alebo fork tohto úložiska

Na začiatok si, prosím, sklonujte alebo forknite GitHub úložisko. Tým si vytvoríte vlastnú verziu kurzových materiálov, aby ste mohli spúšťať, testovať a upravovať kód!

Toto môžete urobiť kliknutím na odkaz <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forknúť úložisko</a>.

Teraz by ste mali mať svoju vlastnú forknutú verziu tohto kurzu na nasledujúcom odkaze:

![Forked Repo](../../../translated_images/sk/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (odporúčané pre workshop / Codespaces)

  >Celé úložisko môže byť veľké (~3 GB), ak stiahnete celú históriu a všetky súbory. Ak sa zúčastňujete len workshopu alebo potrebujete len niekoľko priečinkov lekcií, shallow clone (alebo sparse clone) vám ušetrí väčšinu sťahovania tým, že skráti históriu a/alebo vynechá blob-y.

#### Rýchly shallow clone — minimálna história, všetky súbory

Nahraďte `<your-username>` v nasledujúcich príkazoch URL vášho forku (alebo upstream URL, ak preferujete).

Ak chcete sklonovať len najnovšiu históriu commitov (malé sťahovanie):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Ak chcete klonovať konkrétnu vetvu:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Čiastočný (sparse) clone — minimálne blob-y + len vybrané priečinky

Používa čiastočný klon a sparse-checkout (vyžaduje Git 2.25+ a odporúča sa moderný Git s podporou čiastočného klonu):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Prejdite do priečinka úložiska:

```bash|powershell
cd ai-agents-for-beginners
```

Potom určite, ktoré priečinky chcete (príklad nižšie zobrazuje dva priečinky):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonovaní a overení súborov, ak potrebujete len súbory a chcete uvoľniť miesto (bez git histórie), prosím, vymažte metadata úložiska (💀 nevratné – stratíte všetku Git funkcionalitu: žiadne commity, pully, pushy ani prístup k histórii).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Použitie GitHub Codespaces (odporúčané pre vyhnutie sa veľkým lokálnym stahovaniam)

- Vytvorte nový Codespace pre toto úložisko cez [GitHub UI](https://github.com/codespaces).

- V termináli novovytvoreného codespace spustite jeden z príkazov na shallow/sparse klonovanie vyššie, aby ste do Codespace pracovného priestoru priniesli len potrebné priečinky lekcií.
- Voliteľné: po klonovaní v Codespaces odstráňte .git, aby ste získali viac miesta (pozrite príkazy na odstránenie vyššie).
- Poznámka: Ak radšej otvoríte úložisko priamo v Codespaces (bez extra klonovania), buďte si vedomí, že Codespaces nakonfiguruje devcontainer prostredie a môže stále nasadiť viac, než potrebujete. Klonovanie shallow kópie vo fresh Codespace vám dáva väčšiu kontrolu nad využitím disku.

#### Tipy

- Vždy nahraďte klonovacie URL vaším forkom, ak chcete upravovať/commitovať.
- Ak budete neskôr potrebovať viac histórie alebo súborov, môžete ich stiahnuť alebo upraviť sparse-checkout tak, aby zahŕňal ďalšie priečinky.

## Spúšťanie kódu

Tento kurz ponúka sériu Jupyter Notebookov, ktoré môžete spúšťať, aby ste získali praktické skúsenosti s tvorbou AI agentov.

Ukážkové kódy používajú **Microsoft Agent Framework (MAF)** s poskytovateľom `AzureAIProjectAgentProvider`, ktorý sa pripája k **Azure AI Agent Service V2** (Responses API) prostredníctvom **Microsoft Foundry**.

Všetky Python notebooky sú označené ako `*-python-agent-framework.ipynb`.

## Požiadavky

- Python 3.12+
  - **POZNÁMKA**: Ak nemáte nainštalovaný Python 3.12, uistite sa, že ho nainštalujete. Potom vytvorte vaše virtuálne prostredie pomocou python3.12, aby sa správne nainštalovali verzie z requirements.txt.
  
    >Príklad

    Vytvorte adresár virtuálneho prostredia Pythonu:

    ```bash|powershell
    python -m venv venv
    ```

    Potom aktivujte virtuálne prostredie pre:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Pre ukážkové kódy využívajúce .NET, uistite sa, že máte nainštalovaný [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) alebo novší. Potom skontrolujte verziu nainštalovaného .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — vyžadované pre autentifikáciu. Nainštalujte zo [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure predplatné** — pre prístup k Microsoft Foundry a Azure AI Agent Service.
- **Microsoft Foundry projekt** — projekt s nasadeným modelom (napr. `gpt-4o`). Pozrite [Krok 1](#krok-1-vytvorte-microsoft-foundry-projekt) nižšie.

Do koreňového adresára tohto repozitára sme vložili súbor `requirements.txt`, ktorý obsahuje všetky potrebné Python balíky na spustenie kódov.

Môžete ich nainštalovať spustením nasledujúceho príkazu v termináli v koreňovom adresári repozitára:

```bash|powershell
pip install -r requirements.txt
```

Odporúčame vytvoriť Python virtuálne prostredie, aby ste sa vyhli konfliktom a problémom.

## Nastavenie VSCode

Uistite sa, že v VSCode používate správnu verziu Pythonu.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavenie Microsoft Foundry a Azure AI Agent Service

### Krok 1: Vytvorte Microsoft Foundry projekt

Na spustenie notebookov potrebujete Azure AI Foundry **hub** a **projekt** s nasadeným modelom.

1. Choďte na [ai.azure.com](https://ai.azure.com) a prihláste sa pomocou svojho Azure účtu.
2. Vytvorte **hub** (alebo použite existujúci). Pozrite: [Prehľad zdrojov hubu](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Vo vnútri hubu vytvorte **projekt**.
4. Nasadíte model (napr. `gpt-4o`) cez **Models + Endpoints** → **Deploy model**.

### Krok 2: Získajte koncový bod projektu a názov nasadenia modelu

Vo vašom projekte v Microsoft Foundry portáli:

- **Koncový bod projektu** — Choďte na stránku **Overview** a skopírujte URL koncového bodu.

![Project Connection String](../../../translated_images/sk/project-endpoint.8cf04c9975bbfbf1.webp)

- **Názov nasadenia modelu** — Choďte na **Models + Endpoints**, vyberte nasadený model a zapíšte si **Deployment name** (napr. `gpt-4o`).

### Krok 3: Prihláste sa do Azure cez `az login`

Všetky notebooky používajú **`AzureCliCredential`** na autentifikáciu — nie je potrebné spravovať API kľúče. Vyžaduje sa byť prihlásený pomocou Azure CLI.

1. **Nainštalujte Azure CLI**, ak ho ešte nemáte: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prihláste sa** spustením:

    ```bash|powershell
    az login
    ```

    Alebo, ak ste v remote/Codespace prostredí bez prehliadača:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vyberte predplatné**, ak budete vyzvaní — zvoľte to, ktoré obsahuje váš Foundry projekt.

4. **Overte**, že ste prihlásený:

    ```bash|powershell
    az account show
    ```

> **Prečo `az login`?** Notebooky sa autentifikujú pomocou `AzureCliCredential` z balíka `azure-identity`. To znamená, že vaša Azure CLI relácia poskytuje poverenia — nie sú potrebné API kľúče alebo tajomstvá v súbore `.env`. Toto je [bezpečnostný odporúčaný postup](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Krok 4: Vytvorte `.env` súbor

Skopírujte príkladový súbor:

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Premenná | Kde ju nájsť |
|----------|--------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portál → váš projekt → stránka **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portál → **Models + Endpoints** → názov vášho nasadeného modelu |

To je všetko pre väčšinu lekcií! Notebooky sa budú autentifikovať automaticky cez vašu reláciu `az login`.

### Krok 5: Nainštalujte Python závislosti

```bash|powershell
pip install -r requirements.txt
```

Odporúčame toto spustiť vo virtuálnom prostredí, ktoré ste si vytvorili skôr.

## Dodatočné nastavenie pre Lekciu 5 (Agentic RAG)

Lekcia 5 používa **Azure AI Search** pre retrieval-augmented generation. Ak plánujete spustiť túto lekciu, pridajte do svojho `.env` tieto premenné:

| Premenná | Kde ju nájsť |
|----------|--------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portál → váš **Azure AI Search** zdroj → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portál → váš **Azure AI Search** zdroj → **Settings** → **Keys** → primárny administrátorský kľúč |

## Dodatočné nastavenie pre Lekcie 6 a 8 (GitHub Models)

Niektoré notebooky v lekciách 6 a 8 používajú **GitHub Models** namiesto Azure AI Foundry. Ak plánujete spustiť tieto príklady, pridajte do svojho `.env` tieto premenné:

| Premenná | Kde ju nájsť |
|----------|--------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Použite `https://models.inference.ai.azure.com` (predvolená hodnota) |
| `GITHUB_MODEL_ID` | Názov modelu na použitie (napr. `gpt-4o-mini`) |

## Alternatívny poskytovateľ: MiniMax (kompatibilný s OpenAI)

[MiniMax](https://platform.minimaxi.com/) poskytuje modely s veľkým kontextom (až 204K tokenov) cez OpenAI-kompatibilné API. Keďže `OpenAIChatClient` v Microsoft Agent Framework funguje s akýmkoľvek OpenAI-kompatibilným endpointom, môžete použiť MiniMax ako náhradu za GitHub Models alebo OpenAI.

Pridajte do svojho `.env` tieto premenné:

| Premenná | Kde ju nájsť |
|----------|--------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Použite `https://api.minimax.io/v1` (predvolená hodnota) |
| `MINIMAX_MODEL_ID` | Názov modelu na použitie (napr. `MiniMax-M3`) |

**Príklad modelov**: `MiniMax-M3` (odporúčané), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (rýchlejšie odpovede). Názvy modelov a ich dostupnosť sa môžu časom meniť, a prístup k danému modelu môže závisieť od vášho účtu alebo regiónu — pozrite si [MiniMax Platform](https://platform.minimaxi.com/) pre aktuálny zoznam. Ak `MiniMax-M3` nie je pre váš účet dostupný, nastavte `MINIMAX_MODEL_ID` na model, ku ktorému máte prístup (napr. `MiniMax-M2.7`).

Ukážkové kódy používajúce `OpenAIChatClient` (napr. workflow rezervácie hotela v lekcii 14) automaticky detegujú a použijú vašu MiniMax konfiguráciu, keď je nastavený `MINIMAX_API_KEY`.

## Dodatočné nastavenie pre Lekciu 8 (Bing Grounding Workflow)

Podmienený workflow notebook v lekcii 8 používa **Bing grounding** cez Azure AI Foundry. Ak plánujete spustiť tento príklad, pridajte do svojho `.env` túto premennú:

| Premenná | Kde ju nájsť |
|----------|--------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portál → váš projekt → **Management** → **Connected resources** → vaše Bing pripojenie → skopírujte ID pripojenia |

## Riešenie problémov

### Chyby overenia SSL certifikátu na macOS

Ak používate macOS a zobrazí sa vám chyba ako:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Toto je známy problém s Pythonom na macOS, kde systémové SSL certifikáty nie sú automaticky dôveryhodné. Vyskúšajte tieto riešenia v poradí:

**Možnosť 1: Spustite Python skript na inštaláciu certifikátov (odporúčané)**

```bash
# Nahraďte 3.XX vašou nainštalovanou verziou Pythonu (napr. 3.12 alebo 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnosť 2: Použite `connection_verify=False` vo svojom notebooku (len pre GitHub Models notebooky)**

V lekčnom notebooku 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je už zahrnutý zakomentovaný obchádzkový spôsob. Odkomentujte `connection_verify=False` pri vytváraní klienta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Vypnite overovanie SSL, ak narazíte na chyby certifikátu
)
```

> **⚠️ Upozornenie:** Zakázanie overenia SSL (`connection_verify=False`) znižuje bezpečnosť tým, že obchádza validáciu certifikátu. Používajte to iba ako dočasné riešenie vo vývojových prostrediach, nikdy nie v produkcii.

**Možnosť 3: Nainštalujte a používajte `truststore`**

```bash
pip install truststore
```

Potom pridajte nasledujúce na začiatok vášho notebooku alebo skriptu pred vykonaním sieťových volaní:

```python
import truststore
truststore.inject_into_ssl()
```

## Máte niekde problém?

Ak máte akékoľvek problémy s týmto nastavením, pridajte sa do nášho <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> alebo <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">vytvorte issue</a>.
## Ďalšia lekcia

Teraz ste pripravení spustiť kód pre tento kurz. Prajeme veľa šťastia pri ďalšom spoznávaní sveta AI Agentov!

[Úvod do AI Agentov a prípadov použitia agentov](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->