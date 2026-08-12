# Nastavenie Kurzu

## Úvod

Táto lekcia pokryje, ako spustiť ukážky kódu tohto kurzu.

## Pridajte sa k ostatným študentom a získajte pomoc

Predtým, než začnete klonovať váš repozitár, pridajte sa do [AI Agents For Beginners Discord kanálu](https://aka.ms/ai-agents/discord), aby ste získali pomoc s nastavením, otázky k ​​kurzu alebo aby ste nadviazali kontakt s ostatnými študentmi.

## Klonovanie alebo Forknutie tohto repozitára

Pre začiatok, prosím klonujte alebo forknete GitHub repozitár. Tým si vytvoríte svoju vlastnú verziu materiálov kurzu, aby ste mohli spúšťať, testovať a upravovať kód!

Toto môžete urobiť kliknutím na odkaz <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forknúť repozitár</a>

Teraz by ste mali mať svoju vlastnú fork-linkovanú verziu tohto kurzu na nasledujúcom odkaze:

![Forked Repo](../../../translated_images/sk/forked-repo.33f27ca1901baa6a.webp)

### Plytké Klonovanie (odporúčané pre workshop / Codespaces)

  >Celý repozitár môže byť veľký (~3 GB), keď si stiahnete celú históriu a všetky súbory. Ak sa zúčastňujete iba workshopu alebo potrebujete len niekoľko lekčných priečinkov, plytké klonovanie (alebo sparse clone) vám pomôže vyhnúť sa väčšine toho sťahovania tým, že orezáva históriu a/alebo preskočí bloby.

#### Rýchle plytké klonovanie — minimálna história, všetky súbory

Nahraďte `<your-username>` v nižšie uvedených príkazoch URL adresou vášho forku (alebo upstream URL, ak to preferujete).

Ak chcete klonovať iba najnovšiu históriu commitov (malé stiahnutie):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Ak chcete klonovať konkrétnu vetvu:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Čiastočné (sparse) klonovanie — minimálne bloby + iba vybrané priečinky

Toto používa čiastočné klonovanie a sparse-checkout (vyžaduje Git 2.25+ a odporúča sa moderný Git s podporou partial clone):

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

Po klonovaní a overení súborov, ak potrebujete len súbory a chcete uvoľniť miesto (bez git histórie), prosím zmažte metadáta repozitára (💀nevratné — stratíte všetku funkčnosť Git: žiadne commity, pull, push ani prístup k histórii).

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

- V termináli novo vytvoreného codespace spustite jeden z vyššie uvedených príkazov na plytké/sparse klonovanie, aby ste si stiahli iba lekčné priečinky, ktoré potrebujete do pracovného priestoru Codespaces.
- Voliteľne: po klonovaní v Codespaces odstráňte .git pre uvoľnenie miesta (pozrite príkazy na odstránenie vyššie).
- Poznámka: Ak radšej otvoríte repozitár priamo v Codespaces (bez ďalšieho klonovania), buďte si vedomí, že Codespaces vytvorí vývojové kontajnerové prostredie a môže stále nasadiť viac, než potrebujete. Klonovanie plytkej kópie v čerstvom Codespace vám dáva väčšiu kontrolu nad využitím disku.

#### Tipy

- Vždy nahraďte URL adresu klonu URL svojho forku, ak chcete upravovať/commitovať.
- Ak neskôr budete potrebovať viac histórie alebo súborov, môžete si ich stiahnuť alebo upraviť sparse-checkout, aby ste zahrnuli ďalšie priečinky.

## Spúšťanie Kódu

Tento kurz ponúka sériu Jupyter Notebookov, ktoré môžete spúšťať a získať tak praktické skúsenosti s tvorbou AI Agentov.

Ukážky kódu používajú **Microsoft Agent Framework (MAF)** s `FoundryChatClient`, ktorý sa pripája na **Microsoft Foundry Agent Service V2** (Responses API) cez **Microsoft Foundry**.

Všetky Python notebooky sú označené názvom `*-python-agent-framework.ipynb`.

## Požiadavky

- Python 3.12+
  - **POZNÁMKA**: Ak nemáte nainštalovaný Python 3.12, zabezpečte jeho inštaláciu. Potom vytvorte virtuálne prostredie pomocou python3.12, aby ste mali správne verzie podľa súboru requirements.txt.
  
    >Príklad

    Vytvorenie adresára pre Python venv:

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

- .NET 10+: Pre ukážkové kódy využívajúce .NET si zabezpečte inštaláciu [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) alebo novší. Potom si skontrolujte nainštalovanú verziu .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Potrebný pre autentifikáciu. Inštalujte z [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Pre prístup k Microsoft Foundry a Microsoft Foundry Agent Service.
- **Microsoft Foundry Projekt** — Projekt s nasadeným modelom (napr. `gpt-5-mini`). Pozri [Krok 1](#krok-1-vytvorenie-microsoft-foundry-projektu) nižšie.

V koreňovom adresári repozitára je zahrnutý súbor `requirements.txt`, ktorý obsahuje všetky potrebné Python balíčky na spustenie ukážok kódu.

Môžete ich nainštalovať spustením nasledujúceho príkazu v termináli v koreňovom adresári repozitára:

```bash|powershell
pip install -r requirements.txt
```

Odporúčame vytvoriť si Python virtuálne prostredie, aby ste predišli konfliktom a problémom.

## Nastavenie VSCode

Uistite sa, že používate správnu verziu Pythonu vo VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavenie Microsoft Foundry a Microsoft Foundry Agent Service

### Krok 1: Vytvorenie Microsoft Foundry Projektu

Potrebujete Microsoft Foundry **hub** a **projekt** s nasadeným modelom na spúšťanie notebookov.

1. Prejdite na [ai.azure.com](https://ai.azure.com) a prihláste sa so svojím Azure účtom.
2. Vytvorte **hub** (alebo použite existujúci). Viac: [Prehľad zdrojov Hubu](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. V rámci hubu vytvorte **projekt**.
4. Nasadíte model (napr. `gpt-5-mini`) cez **Models + Endpoints** → **Deploy model**.

### Krok 2: Získajte Váš projektový Endpoint a Názov nasadenia modelu

Z Vášho projektu v portáli Microsoft Foundry:

- **Project Endpoint** — Prejdite na stránku **Overview** a skopírujte URL endpointu.

![Project Connection String](../../../translated_images/sk/project-endpoint.8cf04c9975bbfbf1.webp)

- **Názov nasadenia modelu** — Prejdite na **Models + Endpoints**, vyberte nasadený model a poznamenajte si **Deployment name** (napr. `gpt-5-mini`).

### Krok 3: Prihláste sa do Azure príkazom `az login`

Všetky notebooky používajú na autentifikáciu **`AzureCliCredential`** — nie je potrebné spravovať API kľúče. Vyžaduje to, aby ste boli prihlásení cez Azure CLI.

1. **Nainštalujte Azure CLI**, ak ho ešte nemáte: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prihláste sa** spustením:

    ```bash|powershell
    az login
    ```

    Alebo ak ste v remote/Codespace prostredí bez prehliadača:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vyberte svoj subscription**, ak vás o to systém požiada — vyberte ten obsahujúci váš Foundry projekt.

4. **Overte**, že ste prihlásení:

    ```bash|powershell
    az account show
    ```

> **Prečo `az login`?** Notebooky používajú autentifikáciu `AzureCliCredential` z balíka `azure-identity`. To znamená, že vaša relácia v Azure CLI poskytuje poverenia — nie sú potrebné API kľúče ani tajomstvá vo vašom `.env` súbore. Toto je [bezpečnostná najlepšia prax](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Krok 4: Vytvorte váš `.env` súbor

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portál → váš projekt → stránka **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portál → **Models + Endpoints** → názov vášho nasadeného modelu |

To je všetko pre väčšinu lekcií! Notebooky sa autentifikujú automaticky cez vašu `az login` reláciu.

### Krok 5: Inštalácia závislostí Pythonu

```bash|powershell
pip install -r requirements.txt
```

Odporúčame spustiť tento príkaz vo virtuálnom prostredí, ktoré ste si vytvorili vyššie.

## Dodatočné nastavenie pre Lekciu 5 (Agentic RAG)

Lekcia 5 používa **Azure AI Search** pre retrieval-augmented generation. Ak plánujete spustiť túto lekciu, pridajte tieto premenné do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portál → váš **Azure AI Search** zdroj → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portál → váš **Azure AI Search** zdroj → **Settings** → **Keys** → primárny admin kľúč |

## Dodatočné nastavenie pre lekcie, ktoré volajú Azure OpenAI priamo (Lekcie 6 a 8)

Niektoré notebooky v lekciách 6 a 8 volajú **Azure OpenAI** priamo (používajúc **Responses API**) namiesto prechodu cez Microsoft Foundry projekt. Tieto ukážky predtým používali GitHub Models, ktoré sú zastarané (končia v júli 2026) a nepodporujú Responses API. Ak plánujete spustiť tieto ukážky, pridajte tieto premenné do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portál → váš **Azure OpenAI** zdroj → **Keys and Endpoint** → Endpoint (napr. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Názov vášho nasadeného modelu (napr. `gpt-5-mini`), ktorý podporuje Responses API |
| `AZURE_OPENAI_API_KEY` | Voliteľné — len ak používate autentifikáciu cez kľúč namiesto `az login` / Entra ID |

> Responses API používa stabilný `/openai/v1/` endpoint, takže nie je potrebný parameter `api-version`. Prihláste sa pomocou `az login` pre využitie autentifikácie Entra ID bez kľúčov.

## Alternatívny poskytovateľ: MiniMax (kompatibilný s OpenAI)

[MiniMax](https://platform.minimaxi.com/) poskytuje modely s veľkým kontextom (až 204K tokenov) cez API kompatibilné s OpenAI. Keďže Microsoft Agent Framework `OpenAIChatClient` funguje s akýmkoľvek endpointom kompatibilným s OpenAI, môžete použiť MiniMax ako alternatívu ku Azure OpenAI alebo OpenAI.

Pridajte tieto premenné do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Použite `https://api.minimax.io/v1` (predvolená hodnota) |
| `MINIMAX_MODEL_ID` | Názov modelu na použitie (napr. `MiniMax-M3`) |

**Príklad modelov**: `MiniMax-M3` (odporúčaný), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (rýchlejšie odpovede). Názvy modelov a ich dostupnosť sa môžu meniť, prístup k modelu závisí na vašom účte alebo regióne — skontrolujte [MiniMax Platform](https://platform.minimaxi.com/) pre aktuálny zoznam. Ak model `MiniMax-M3` nie je dostupný pre váš účet, nastavte `MINIMAX_MODEL_ID` na model, ku ktorému máte prístup (napr. `MiniMax-M2.7`).

Ukážky kódu používajúce `OpenAIChatClient` (napr. Lekcia 14 workflow rezervácie hotela) automaticky rozpoznajú a použijú vašu MiniMax konfiguráciu, keď je nastavený `MINIMAX_API_KEY`.

## Alternatívny poskytovateľ: Foundry Local (spustenie modelov lokálne)

[Foundry Local](https://foundrylocal.ai) je ľahký runtime, ktorý sťahuje, spravuje a poskytuje jazykové modely **úplne na vašom počítači** cez API kompatibilné s OpenAI — bez cloudu, bez Azure subscription a bez API kľúčov. Je to skvelá možnosť na offline vývoj, experimentovanie bez cloudových nákladov alebo uchovávanie dát lokálne.

Keďže Microsoft Agent Framework `OpenAIChatClient` funguje s akýmkoľvek endpointom kompatibilným s OpenAI, Foundry Local je lokálna alternatíva k Azure OpenAI.

**1. Nainštalujte Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Stiahnite a spustite model** (tým spustíte aj lokálnu službu):

```bash
foundry model list          # pozrite si dostupné modely
foundry model run phi-4-mini
```

**3. Nainštalujte Python SDK** používané na objavenie lokálneho endpointu:

```bash
pip install foundry-local-sdk
```

**4. Nasmerujte Microsoft Agent Framework na váš lokálny model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Stiahne (ak je potrebné) a spustí model lokálne, potom zistí koncový bod/port.
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

> **Poznámka:** Foundry Local vystavuje OpenAI-kompatibilný endpoint pre **Chat Completions**. Používajte ho pre lokálny vývoj a offline scenáre. Pre plnú funkcionalitu **Responses API** (stavové konverzácie, hlbokú orchestráciu nástrojov a agentový vývoj) cielte na **Azure OpenAI** alebo **Microsoft Foundry** projekt, ako je ukázané v lekciách. Viac pozrite v [Foundry Local dokumentácii](https://foundrylocal.ai) pre aktuálny katalóg modelov a podporované platformy.

## Dodatočné nastavenie pre Lekciu 8 (Bing Grounding Workflow)


Podmienený pracovný tok v poznámkovom bloku v lekcii 8 používa **Bing grounding** cez Microsoft Foundry. Ak plánujete spustiť tento príklad, pridajte túto premennú do svojho súboru `.env`:

| Premenná | Kde ju nájsť |
|----------|--------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portál → váš projekt → **Manažment** → **Pripojené zdroje** → vaše Bing spojenie → skopírujte ID spojenia |

## Riešenie problémov

### Chyby overovania SSL certifikátu na macOS

Ak ste na macOS a narazíte na chybu ako:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Toto je známy problém s Pythonom na macOS, kde systémové SSL certifikáty nie sú automaticky dôveryhodné. Vyskúšajte nasledujúce riešenia v tomto poradí:

**Možnosť 1: Spustiť Python skript na inštaláciu certifikátov (odporúčané)**

```bash
# Nahraďte 3.XX vašou nainštalovanou verziou Pythonu (napr. 3.12 alebo 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnosť 2: Použiť `connection_verify=False` v poznámkovom bloku (iba pre GitHub Models poznámkové bloky)**

V poznámkovom bloku z Lekcie 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je už zahrnutý zakomentovaný obchádzkový postup. Odkomentujte `connection_verify=False` pri vytváraní klienta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Vypnite overovanie SSL, ak sa vyskytnú chyby certifikátu
)
```

> **⚠️ Varovanie:** Vypnutie overovania SSL (`connection_verify=False`) znižuje bezpečnosť, pretože preskakuje validáciu certifikátu. Používajte to iba ako dočasné riešenie v testovacích prostrediach, nikdy nie v produkcii.

**Možnosť 3: Nainštalujte a používajte `truststore`**

```bash
pip install truststore
```

Potom pridajte nasledovné na začiatok svojho poznámkového bloku alebo skriptu pred vykonaním akýchkoľvek sieťových volaní:

```python
import truststore
truststore.inject_into_ssl()
```

## Niekde zaseknutý?

Ak máte akékoľvek problémy s nastavením, vstúpte do <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> alebo <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">vytvorte issue</a>.

## Ďalšia lekcia

Teraz ste pripravení spustiť kód pre tento kurz. Prajeme veľa úspechov pri učení o svete AI agentov! 

[Úvod do AI agentov a prípadov použitia agentov](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->