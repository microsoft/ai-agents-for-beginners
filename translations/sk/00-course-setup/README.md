# Nastavenie kurzu

## Úvod

Táto lekcia pokrýva, ako spustiť ukážkové kódy v tomto kurze.

## Pridajte sa k ostatným študentom a získajte pomoc

Pred tým, než začnete klonovať svoj repozitár, pridajte sa na [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord), aby ste získali pomoc pri nastavení, odpovede na otázky ohľadne kurzu alebo sa spojili s ďalšími študentmi.

## Klonovanie alebo vytvorenie forku tohto repozitára

Na začiatok prosím naklonujte alebo vytvorte fork GitHub repozitára. Tým získate vlastnú verziu materiálov kurzu, aby ste mohli kód spúšťať, testovať a upravovať!

Toto môžete urobiť kliknutím na odkaz na <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">vytvoriť fork repozitára</a>

Teraz by ste mali mať vlastnú fork-ovanú verziu tohto kurzu na nasledujúcom odkaze:

![Forknutý repozitár](../../../translated_images/sk/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (odporúčané pre workshop / Codespaces)

  >Plný repozitár môže byť pri stiahnutí s celou históriou a všetkými súbormi veľký (~3 GB). Ak sa zúčastňujete len na workshope alebo potrebujete len niekoľko priečinkov s lekciami, shallow clone (alebo sparse clone) sa vyhne väčšine sťahovania tým, že skráti históriu a/alebo preskočí blob-y.

#### Rýchly shallow clone — minimálna história, všetky súbory

Nahradiť `<your-username>` v príkazoch nižšie vašou URL forku (alebo upstream URL, ak preferujete).

Na klonovanie len najnovšej histórie commitov (malé sťahovanie):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Na klonovanie konkrétnej vetvy:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Čiastočný (sparse) clone — minimálne blob-y + iba vybrané priečinky

Toto používa partial clone a sparse-checkout (vyžaduje Git 2.25+ a odporúča sa moderný Git s podporou partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Prejdite do priečinka repozitára:

```bash|powershell
cd ai-agents-for-beginners
```

Potom určte, ktoré priečinky chcete (príklad nižšie zobrazuje dva priečinky):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po sklonovaní a overení súborov, ak potrebujete len súbory a chcete uvoľniť miesto (bez histórie git), vymažte metadáta repozitára (💀nevratné — stratíte všetku funkcionalitu Gitu: žiadne commity, pulls, pushes alebo prístup k histórii).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Použitie GitHub Codespaces (odporúčané na vyhnutie sa veľkému lokálnemu sťahovaniu)

- Vytvorte nový Codespace pre tento repozitár cez [GitHub UI](https://github.com/codespaces).  

- V termináli novo vytvoreného Codespace spustite jeden z vyššie uvedených shallow/sparse clone príkazov, aby ste do pracovného priestoru Codespace priniesli len priečinky s lekciami, ktoré potrebujete.
- Voliteľné: po klonovaní v Codespaces odstráňte .git, aby ste uvoľnili miesto (pozrite príkazy na odstránenie vyššie).
- Poznámka: Ak preferujete otvoriť repozitár priamo v Codespaces (bez ďalšieho klonovania), buďte si vedomí, že Codespaces zostaví devcontainer prostredie a môže stále pripraviť viac, než potrebujete. Klonovanie shallow kópie v rámci nového Codespace vám dáva väčšiu kontrolu nad využitím disku.

#### Tipy

- Vždy nahraďte URL klonovania vaším forkom, ak chcete upravovať/commitovať.
- Ak neskôr potrebujete viac histórie alebo súborov, môžete ich stiahnuť alebo upraviť sparse-checkout, aby ste zahrnuli ďalšie priečinky.

## Spustenie kódu

Tento kurz ponúka sériu Jupyter notebookov, ktoré môžete spustiť, aby ste získali praktické skúsenosti s budovaním AI agentov.

Ukážky kódu používajú **Microsoft Agent Framework (MAF)** s `AzureAIProjectAgentProvider`, ktorý sa pripája k **Azure AI Agent Service V2** (Responses API) prostredníctvom **Microsoft Foundry**.

Všetky Python notebooky sú označené `*-python-agent-framework.ipynb`.

## Požiadavky

- Python 3.12+
  - **POZNÁMKA**: Ak nemáte nainštalovaný Python 3.12, nainštalujte ho. Potom vytvorte svoje venv pomocou python3.12, aby sa nainštalovali správne verzie z requirements.txt.
  
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

- .NET 10+: Pre ukážkové kódy používajúce .NET sa uistite, že máte nainštalovaný [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) alebo novší. Potom skontrolujte nainštalovanú verziu .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Vyžaduje sa pre autorizáciu. Nainštalujte z [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Pre prístup k Microsoft Foundry a Azure AI Agent Service.
- **Microsoft Foundry Project** — Projekt s nasadeným modelom (napr. `gpt-4o`). Pozri [Krok 1](../../../00-course-setup) nižšie.

V koreňovom adresári tohto repozitára sme zahrnuli súbor `requirements.txt`, ktorý obsahuje všetky požadované Python balíky na spustenie ukážkových kódov.

Môžete ich nainštalovať spustením nasledujúceho príkazu v termináli v koreňovom adresári repozitára:

```bash|powershell
pip install -r requirements.txt
```

Odporúčame vytvoriť Python virtuálne prostredie, aby ste predišli akýmkoľvek konfliktom a problémom.

## Nastavenie VSCode

Uistite sa, že vo VSCode používate správnu verziu Pythonu.

![obrázok](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavenie Microsoft Foundry a Azure AI Agent Service

### Krok 1: Vytvorte Microsoft Foundry projekt

Na spustenie notebookov potrebujete Azure AI Foundry **hub** a **projekt** s nasadeným modelom.

1. Prejdite na [ai.azure.com](https://ai.azure.com) a prihláste sa so svojim Azure účtom.
2. Vytvorte **hub** (alebo použite existujúci). Pozri: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. V rámci hubu vytvorte **projekt**.
4. Nasadte model (napr. `gpt-4o`) cez **Models + Endpoints** → **Deploy model**.

### Krok 2: Získajte koncový bod projektu a názov nasadenia modelu

Z vášho projektu v portáli Microsoft Foundry:

- **Project Endpoint** — Prejdite na stránku **Overview** a skopírujte URL koncového bodu.

![Reťazec pripojenia projektu](../../../translated_images/sk/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Prejdite na **Models + Endpoints**, vyberte váš nasadený model a zaznamenajte **Deployment name** (napr. `gpt-4o`).

### Krok 3: Prihláste sa do Azure pomocou `az login`

Všetky notebooky používajú **`AzureCliCredential`** na overovanie — žiadne API kľúče na spravovanie. To vyžaduje, aby ste boli prihlásení cez Azure CLI.

1. **Nainštalujte Azure CLI**, ak ho ešte nemáte: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prihláste sa** spustením:

    ```bash|powershell
    az login
    ```

    Alebo ak ste v remote/Codespace prostredí bez prehliadača:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vyberte svoj subscription**, ak budete vyzvaní — zvoľte ten, ktorý obsahuje váš Foundry projekt.

4. **Overte**, že ste prihlásení:

    ```bash|powershell
    az account show
    ```

> **Prečo `az login`?** Notebooky sa overujú pomocou `AzureCliCredential` z balíka `azure-identity`. To znamená, že vaša relácia v Azure CLI poskytuje poverenia — žiadne API kľúče alebo tajomstvá vo vašom `.env` súbore. Toto je [bezpečnostná najlepšia prax](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | portál Foundry → váš projekt → stránka **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | portál Foundry → **Models + Endpoints** → názov vášho nasadeného modelu |

To je všetko pre väčšinu lekcií! Notebooky sa budú automaticky overovať cez vašu reláciu `az login`.

### Krok 5: Nainštalujte Python závislosti

```bash|powershell
pip install -r requirements.txt
```

Odporúčame spustiť to v rámci virtuálneho prostredia, ktoré ste vytvorili skôr.

## Dodatočné nastavenie pre Lekciu 5 (Agentic RAG)

Lekcia 5 používa **Azure AI Search** pre retrieval-augmented generation. Ak plánujete túto lekciu spustiť, pridajte tieto premenné do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → váš **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → váš **Azure AI Search** resource → **Settings** → **Keys** → primárny admin kľúč |

## Dodatočné nastavenie pre Lekciu 6 a Lekciu 8 (GitHub Models)

Niektoré notebooky v lekciách 6 a 8 používajú **GitHub Models** namiesto Azure AI Foundry. Ak plánujete tieto ukážky spustiť, pridajte tieto premenné do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Použite `https://models.inference.ai.azure.com` (predvolená hodnota) |
| `GITHUB_MODEL_ID` | Názov modelu, ktorý chcete použiť (napr. `gpt-4o-mini`) |

## Dodatočné nastavenie pre Lekciu 8 (Bing Grounding Workflow)

Podmienený workflow notebook v lekcii 8 používa **Bing grounding** cez Azure AI Foundry. Ak plánujete túto ukážku spustiť, pridajte túto premennú do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portál → váš projekt → **Management** → **Connected resources** → vaše Bing pripojenie → skopírujte connection ID |

## Riešenie problémov

### Chyby overenia SSL certifikátu na macOS

Ak používate macOS a narazíte na chybu ako:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Toto je známy problém s Pythonom na macOS, kde systémové SSL certifikáty nie sú automaticky dôveryhodné. Vyskúšajte nasledujúce riešenia v poradí:

**Možnosť 1: Spustiť Python skript Install Certificates (odporúčané)**

```bash
# Nahraďte 3.XX nainštalovanou verziou Pythonu (napr. 3.12 alebo 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnosť 2: Použiť `connection_verify=False` vo vašom notebooku (len pre GitHub Models notebooky)**

V notebooku Lekcie 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je už zahrnuté zakomentované obchádzanie. Odkomentujte `connection_verify=False` pri vytváraní klienta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Vypnite overovanie SSL, ak narazíte na chyby certifikátu
)
```

> **⚠️ Upozornenie:** Vypnutie SSL overenia (`connection_verify=False`) znižuje bezpečnosť tým, že preskočí validáciu certifikátu. Používajte to len ako dočasné obchádzanie v vývojovom prostredí, nikdy v produkcii.

**Možnosť 3: Nainštalujte a použite `truststore`**

```bash
pip install truststore
```

Potom pridajte nasledujúce na začiatok vášho notebooku alebo skriptu pred vykonaním akýchkoľvek sieťových volaní:

```python
import truststore
truststore.inject_into_ssl()
```

## Uviazli ste niekde?

Ak máte akékoľvek problémy so spustením tohto nastavenia, pripojte sa do našej <a href="https://discord.gg/kzRShWzttr" target="_blank">komunity Azure AI na Discorde</a> alebo <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">vytvorte issue</a>.

## Ďalšia lekcia

Teraz ste pripravení spúšťať kód pre tento kurz. Prajeme veľa úspechov pri spoznávaní sveta AI agentov! 

[Úvod do AI agentov a prípadov použitia agentov](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vyhlásenie o vylúčení zodpovednosti:
Tento dokument bol preložený pomocou automatizovanej prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho originálnom jazyku treba považovať za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny preklad vykonaný človekom. Nie sme zodpovední za žiadne nedorozumenia ani nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->