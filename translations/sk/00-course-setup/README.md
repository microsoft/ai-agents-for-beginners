# Course Setup

## Introduction

Táto lekcia pokryje, ako spustiť ukážkové kódy z tohto kurzu.

## Join Other Learners and Get Help

Predtým, než začnete klonovať svoje repo, pripojte sa na [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord), aby ste získali pomoc pri nastavení, položili otázky o kurze alebo sa spojili s ostatnými študentmi.

## Clone or Fork this Repo

Na začiatok prosím klonujte alebo fork‑nite GitHub repozitár. Tým si vytvoríte vlastnú verziu kurzového materiálu, aby ste mohli kód spúšťať, testovať a upravovať!

Toto môžete urobiť kliknutím na odkaz <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a>

Teraz by ste mali mať vlastnú fork‑nutú verziu tohto kurzu na nasledujúcom odkaze:

![Forked Repo](../../../translated_images/sk/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (recommended for workshop / Codespaces)

  >Celý repozitár môže byť veľký (~3 GB), ak si stiahnete celú históriu a všetky súbory. Ak sa zúčastňujete len workshopu alebo potrebujete iba niekoľko lekcií, shallow clone (alebo sparse clone) sa vyhnete väčšine toho sťahovania skrátením histórie a/alebo vynechaním blobov.

#### Quick shallow clone — minimal history, all files

Nahradiť `<your-username>` v nasledujúcich príkazoch vaším URL forku (alebo upstream URL, ak preferujete).

Ak chcete klonovať iba najnovšiu históriu (malé stiahnutie):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Ak chcete klonovať konkrétnu vetvu:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal blobs + only selected folders

Toto používa partial clone a sparse-checkout (vyžaduje Git 2.25+ a odporúčaný moderný Git s podporou partial clone):

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

Po klonovaní a overení súborov, ak potrebujete iba súbory a chcete uvoľniť miesto (bez git histórie), prosím odstráňte metadáta repozitára (💀nevratné — stratíte všetku funkcionalitu Gitu: žiadne commity, pulls, pushes ani prístup k histórii).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Using GitHub Codespaces (recommended to avoid local large downloads)

- Vytvorte nový Codespace pre tento repozitár cez [GitHub UI](https://github.com/codespaces).  

- V termináli novo vytvoreného codespace spustite jeden z vyššie uvedených shallow/sparse clone príkazov, aby ste do Codespace pracovného priestoru priniesli len lekcie, ktoré potrebujete.
- Voliteľné: po klonovaní v Codespaces odstráňte .git, aby ste získali viac miesta (pozri príkazy na odstránenie vyššie).
- Poznámka: Ak preferujete otvoriť repozitár priamo v Codespaces (bez extra klonu), majte na pamäti, že Codespaces zostaví devcontainer prostredie a môže stále provisionovať viac, než potrebujete. Klonovanie shallow kópie vnútri nového Codespace vám dáva väčšiu kontrolu nad využitím disku.

#### Tips

- Vždy nahraďte clone URL svojim forkom, ak chcete upravovať/commitovať.
- Ak neskôr potrebujete viac histórie alebo súborov, môžete ich načítať (fetch) alebo upraviť sparse-checkout a zahrnúť ďalšie priečinky.

## Running the Code

Tento kurz ponúka sériu Jupyter Notebookov, ktoré môžete spustiť, aby ste získali praktické skúsenosti s budovaním AI agentov.

Ukážkové kódy používajú **Microsoft Agent Framework (MAF)** s `AzureAIProjectAgentProvider`, ktorý sa pripája k **Azure AI Agent Service V2** (Responses API) cez **Microsoft Foundry**.

Všetky Python notebooky sú označené `*-python-agent-framework.ipynb`.

## Requirements

- Python 3.12+
  - **POZNÁMKA**: Ak nemáte nainštalovaný Python 3.12, uistite sa, že ho nainštalujete. Potom vytvorte svoje venv pomocou python3.12, aby sa nainštalovali správne verzie zo súboru requirements.txt.
  
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

- .NET 10+: Pre príkladové kódy používajúce .NET, uistite sa, že máte nainštalovaný [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) alebo novší. Potom skontrolujte nainštalovanú verziu .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Požadované na autentifikáciu. Inštalujte z [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Pre prístup k Microsoft Foundry a Azure AI Agent Service.
- **Microsoft Foundry Project** — Projekt s nasadeným modelom (napr. `gpt-4o`). Pozri [Krok 1](../../../00-course-setup) nižšie.

Do koreňa tohto repozitára sme zahrnuli súbor `requirements.txt`, ktorý obsahuje všetky potrebné Python balíčky na spustenie ukážkových kódov.

Môžete ich nainštalovať spustením nasledujúceho príkazu v termináli v koreňovom adresári repozitára:

```bash|powershell
pip install -r requirements.txt
```

Odporúčame vytvoriť Python virtuálne prostredie, aby ste sa vyhli konfliktom a problémom.

## Setup VSCode

Uistite sa, že vo VSCode používate správnu verziu Pythonu.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Set Up Microsoft Foundry and Azure AI Agent Service

### Step 1: Create a Microsoft Foundry Project

Potrebujete Azure AI Foundry **hub** a **projekt** s nasadeným modelom, aby ste mohli spúšťať notebooky.

1. Prejdite na [ai.azure.com](https://ai.azure.com) a prihláste sa so svojím Azure účtom.
2. Vytvorte **hub** (alebo použite existujúci). Pozri: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. V rámci hubu vytvorte **projekt**.
4. Nasadte model (napr. `gpt-4o`) v sekcii **Models + Endpoints** → **Deploy model**.

### Step 2: Retrieve Your Project Endpoint and Model Deployment Name

Z vášho projektu v portáli Microsoft Foundry:

- **Project Endpoint** — Prejdite na stránku **Overview** a skopírujte URL endpointu.

![Project Connection String](../../../translated_images/sk/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Prejdite do **Models + Endpoints**, vyberte nasadený model a poznamenajte si **Deployment name** (napr. `gpt-4o`).

### Step 3: Sign in to Azure with `az login`

Všetky notebooky používajú **`AzureCliCredential`** na autentifikáciu — žiadne API kľúče na správu. To vyžaduje, aby ste boli prihlásení cez Azure CLI.

1. **Nainštalujte Azure CLI**, ak ho ešte nemáte: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prihláste sa** spustením:

    ```bash|powershell
    az login
    ```

    Alebo ak ste v remote/Codespace prostredí bez prehliadača:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vyberte svoj subscription**, ak ste vyzvaní — zvoľte ten, ktorý obsahuje váš Foundry projekt.

4. **Overte**, že ste prihlásení:

    ```bash|powershell
    az account show
    ```

> **Prečo `az login`?** Notebooky sa autentifikujú pomocou `AzureCliCredential` z balíčka `azure-identity`. To znamená, že vaša Azure CLI relácia poskytuje poverenia — žiadne API kľúče alebo tajomstvá v `.env` súbore. Toto je [bezpečnostná osvedčená postupnosť](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Step 4: Create Your `.env` File

Skopírujte ukážkový súbor:

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

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → váš projekt → **Overview** stránka |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → názov vášho nasadeného modelu |

To je všetko pre väčšinu lekcií! Notebooky sa budú autentifikovať automaticky cez vašu `az login` reláciu.

### Step 5: Install Python Dependencies

```bash|powershell
pip install -r requirements.txt
```

Odporúčame spustiť toto vo vnútri virtuálneho prostredia, ktoré ste si vytvorili skôr.

## Additional Setup for Lesson 5 (Agentic RAG)

Lekcia 5 používa **Azure AI Search** pre retrieval-augmented generation. Ak plánujete spustiť túto lekciu, pridajte tieto premenné do vášho `.env` súboru:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → váš **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → váš **Azure AI Search** resource → **Settings** → **Keys** → primárny admin kľúč |

## Additional Setup for Lesson 6 and Lesson 8 (GitHub Models)

Niektoré notebooky v lekciách 6 a 8 používajú **GitHub Models** namiesto Azure AI Foundry. Ak plánujete spustiť tieto ukážky, pridajte tieto premenné do vášho `.env` súboru:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Názov modelu na použitie (napr. `gpt-4o-mini`) |

## Additional Setup for Lesson 8 (Bing Grounding Workflow)

Podmienený workflow notebook v lekcii 8 používa **Bing grounding** cez Azure AI Foundry. Ak plánujete spustiť tento príklad, pridajte túto premennú do vášho `.env` súboru:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → váš projekt → **Management** → **Connected resources** → vaša Bing connection → skopírujte connection ID |

## Troubleshooting

### SSL Certificate Verification Errors on macOS

Ak ste na macOS a narazíte na chybu typu:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Toto je známy problém s Pythonom na macOS, kde systémové SSL certifikáty nie sú automaticky dôveryhodné. Skúste nasledujúce riešenia v poradí:

**Možnosť 1: Spustite Python skript Install Certificates (odporúčané)**

```bash
# Nahraďte 3.XX nainštalovanou verziou Pythonu (napr. 3.12 alebo 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnosť 2: Použite `connection_verify=False` v notebooku (len pre GitHub Models notebooky)**

V Lesson 6 notebooku (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je už zahrnuté zakomentované riešenie. Odkomentujte `connection_verify=False` pri vytváraní klienta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Vypnite overovanie SSL, ak narazíte na chyby certifikátu
)
```

> **⚠️ Warning:** Zakázanie SSL overenia (`connection_verify=False`) znižuje bezpečnosť tým, že preskočí validáciu certifikátov. Používajte to len ako dočasné riešenie v vývojových prostrediach, nikdy v produkcii.

**Možnosť 3: Inštalujte a používajte `truststore`**

```bash
pip install truststore
```

Potom pridajte nasledovné na začiatok vášho notebooku alebo skriptu pred vykonaním sieťových volaní:

```python
import truststore
truststore.inject_into_ssl()
```

## Stuck Somewhere?

Ak máte nejaké problémy s týmto nastavením, skočte do nášho <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> alebo <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">create an issue</a>.

## Next Lesson

Teraz ste pripravení spustiť kód pre tento kurz. Prajeme veľa úspechov pri ďalšom spoznávaní sveta AI agentov! 

[Úvod do AI agentov a prípadov použitia agentov](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vylúčenie zodpovednosti**:
Tento dokument bol preložený pomocou služby automatického prekladu založenej na umelej inteligencii [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, berte prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za rozhodujúci zdroj. Pre dôležité informácie sa odporúča profesionálny preklad vykonaný ľudským prekladateľom. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->