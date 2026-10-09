# Nastavenie kurzu

## Úvod

Táto lekcia pokryje, ako spustiť kódové príklady tohto kurzu.

## Pridajte sa k ostatným študentom a získajte pomoc

Pred tým, než začnete klonovať svoj repozitár, pripojte sa k [AI Agents For Beginners Discord kanálu](https://aka.ms/ai-agents/discord) a získajte pomoc s nastavením, odpovede na otázky o kurze alebo sa spojte s ostatnými študentmi.

## Klonovanie alebo fork tohto repozitára

Na začiatok prosím klonujte alebo forknete GitHub repozitár. Tým si vytvoríte vlastnú verziu materiálov ku kurzu, aby ste mohli spúšťať, testovať a upravovať kód!

Toto môžete urobiť kliknutím na odkaz na <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repozitára</a>

Teraz by ste mali mať svoju vlastnú forknutú verziu tohto kurzu na nasledujúcom odkaze:

![Forknutý repozitár](../../../translated_images/sk/forked-repo.33f27ca1901baa6a.webp)

### Plytké klonovanie (odporúčané pre workshop / Codespaces)

  >Celý repozitár môže byť veľký (~3 GB) pri stiahnutí celého histórie a všetkých súborov. Ak sa zúčastňujete iba workshopu alebo potrebujete len pár zložiek lekcií, plytké klonovanie (alebo sparse klonovanie) stiahne výrazne menej.

#### Rýchle plytké klonovanie – minimálna história, všetky súbory

Nahraďte `<your-username>` v nasledujúcich príkazoch vašou URL forku (alebo upstream URL, ak preferujete).

Na klonovanie iba najnovšej histórie commitov (malé stiahnutie):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Na klonovanie konkrétnej vetvy:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Čiastočné (sparse) klonovanie – minimálne blob-y + len vybrané zložky

Toto využíva partial clone a sparse-checkout (vyžaduje Git 2.25+ a odporúča sa moderný Git s podporou partial clone):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Prejdite do zložky repozitára:

```bash
cd ai-agents-for-beginners
```

Potom určte, ktoré zložky chcete (príklad nižšie ukazuje dve zložky):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonovaní a overení súborov, ak potrebujete iba súbory a chcete uvoľniť miesto (bez histórie git), odstráňte prosím metadata repozitára (💀nezvratné – stratíte všetky funkcie Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Použitie GitHub Codespaces (odporúčané, aby ste sa vyhli veľkým lokálnym sťahovaniam)

- Vytvorte nový Codespace pre tento repozitár cez [GitHub UI](https://github.com/codespaces).  

- V termináli novovytvoreného Codespace spustite jeden z príkazov pre shallow/sparse clone vyššie, aby ste do pracovného priestoru Codespace dostali len potrebné zložky lekcií.
- Voliteľné: po klonovaní v Codespaces odstráňte .git pre uvoľnenie ďalšieho miesta (pozrite príkazy na odstránenie vyššie).
- Poznámka: Ak preferujete priamo otvoriť repozitár v Codespaces (bez ďalšieho klonovania), vedzte, že Codespaces vytvorí devcontainer prostredie a môže stále nainštalovať viac, než potrebujete.

#### Tipy

- Vždy nahraďte URL klonovania vašim forkom, ak chcete upravovať/commitovať.
- Ak neskôr potrebujete viac histórie alebo súborov, môžete ich stiahnuť alebo upraviť sparse-checkout pre zahrnutie ďalších zložiek.

## Spúšťanie kódu

Tento kurz ponúka sériu Jupyter Notebookov, ktoré môžete spúšťať a získať praktické skúsenosti s tvorbou AI agentov.

Kódové príklady používajú **Microsoft Agent Framework (MAF)** s `FoundryChatClient`, ktorý sa pripája na **Microsoft Foundry Agent Service V2** (Responses API) cez **Microsoft Foundry**.

Všetky Python notebooky sú označené `*-python-agent-framework.ipynb`.

## Požiadavky

- Python 3.12+
  - **POZNÁMKA**: Ak nemáte nainštalovaný Python3.12, uistite sa, že ho nainštalujete. Potom vytvorte svoje virtuálne prostredie pomocou python3.12, aby ste mali správne verzie nainštalované z requirements.txt.
  
    >Príklad

    Vytvorenie adresára pre Python venv:

    ```bash
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

- .NET 10+: Pre ukážkové kódy používajúce .NET, uistite sa, že máte nainštalovaný [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) alebo novší. Potom skontrolujte svoju nainštalovanú verziu .NET SDK:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Vyžaduje sa na autentifikáciu. Nainštalujte z [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Na prístup k Microsoft Foundry a Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Projekt s nasadeným modelom (napr. `gpt-5-mini`). Pozri [Krok 1](#krok-1-vytvorenie-microsoft-foundry-projektu) nižšie.

V koreňovom adresári tohto repozitára nájdete súbor `requirements.txt`, ktorý obsahuje všetky potrebné balíky Python na spustenie kódových príkladov.

Môžete ich nainštalovať spustením nasledujúceho príkazu v termináli v koreňovom adresári repozitára:

```bash
pip install -r requirements.txt
```

Odporúčame vytvoriť Python virtuálne prostredie, aby ste sa vyhli konfliktom a problémom.

## Nastavenie VSCode

Uistite sa, že používate správnu verziu Pythonu vo VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavenie Microsoft Foundry a Microsoft Foundry Agent Service

### Krok 1: Vytvorenie Microsoft Foundry projektu

Na spustenie notebookov potrebujete Microsoft Foundry **hub** a **projekt** s nasadeným modelom.

1. Prejdite na [ai.azure.com](https://ai.azure.com) a prihláste sa so svojim Azure účtom.
2. Vytvorte **hub** (alebo použite existujúci). Pozri: [Prehľad zdrojov hubu](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Vo vnútri hubu vytvorte **projekt**.
4. Nasadte model (napr. `gpt-5-mini`) z **Models + Endpoints** → **Deploy model**.

### Krok 2: Získanie endpointu projektu a názvu nasadenia modelu

Z vášho projektu v Microsoft Foundry portáli:

- **Project Endpoint** — Prejdite na stránku **Overview** a skopírujte URL endpointu.

![Project Connection String](../../../translated_images/sk/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Prejdite do **Models + Endpoints**, vyberte svoj nasadený model a zapíšte si **Deployment name** (napr. `gpt-5-mini`).

### Krok 3: Prihlásenie do Azure pomocou `az login`

Väčšina notebookov sa autentifikuje prostredníctvom vášho **Azure CLI prihlásenia** — použitie `AzureCliCredential` alebo `DefaultAzureCredential` (oba získavajú vašu `az login` reláciu) z balíka `azure-identity` — preto nevyžadujú API kľúče. Niektoré lekcie a voliteľné integrácie používajú API kľúče; skontrolujte požiadavky každej lekcie pre ďalšie premenné prostredia. Vyžaduje to, aby ste boli prihlásení cez Azure CLI.

1. **Nainštalujte Azure CLI**, ak ešte nemáte: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prihláste sa** spustením:

    ```bash
    az login
    ```

    Alebo ak ste v remote/Codespace prostredí bez prehliadača:

    ```bash
    az login --use-device-code
    ```

3. **Vyberte svoj subscription**, ak sa zobrazí výzva — vyberte ten, ktorý obsahuje váš Foundry projekt.

4. **Overte**, že ste prihlásení:

    ```bash
    az account show
    ```

> **Prečo `az login`?** Notebooky sa autentifikujú pomocou `AzureCliCredential` (alebo `DefaultAzureCredential`, ktorý tiež získava Azure CLI prihlásenie) z balíka `azure-identity`. To znamená, že vaša Azure CLI relácia poskytuje prihlasovacie údaje — žiadne API kľúče alebo tajomstvá v `.env` súbore. Toto je [najlepšia bezpečnostná prax](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Krok 4: Vytvorenie súboru `.env`

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Premenná | Kde ju nájsť |
|----------|--------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portál → váš projekt → stránka **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portál → **Models + Endpoints** → názov nasadeného modelu |

To je všetko pre väčšinu lekcií! Notebooky sa automaticky autentifikujú cez vašu `az login` reláciu.

### Krok 5: Inštalácia Python závislostí

```bash
pip install -r requirements.txt
```

Odporúčame spustiť tento príkaz vo vnútri virtuálneho prostredia, ktoré ste si vytvorili.

## Voliteľné nastavenie: Azure AI Search (lekcie 5 a 16)

Notebooky lekcie 5 (Agentic RAG) a lekcie 16 fungujú ihneď s **in-memory knowledge base** — nie sú potrebné žiadne extra Azure zdroje. Ak ich chcete podporiť skutočným indexom **Azure AI Search**, majte na pamäti, že **notebook lekcie 16 momentálne používa autentifikáciu pomocou kľúčov**: prepína z in-memory vyhľadávania na Azure AI Search iba keď sú nastavené **obidve** premenné `AZURE_SEARCH_SERVICE_ENDPOINT` **a** `AZURE_SEARCH_API_KEY`, inak zostáva na in-memory vyhľadávaní — na použitie so skutočným indexom preto musíte nastaviť tiež administrátorský kľúč. Bezklúčová autentifikácia cez Microsoft Entra ID (RBAC) je odporúčaný spôsob pre vlastný produkčný kód, konzistentný s `az login` tokom použitým inde v kurze.

Kroky RBAC nižšie platia pre ukážkové vzory v príručke a váš vlastný kód. Neaktivujú bezkľúčovú autentifikáciu v notebooku lekcie 16; lekcia 16 stále vyžaduje endpoint aj administrátorský kľúč na využitie Azure AI Search.

1. **Povoľte riadený prístup podľa roly** pre vašu službu vyhľadávania:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Priraďte si požadované roly** (vytváranie/nahrávanie indexov a dotazovanie):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Pridajte endpoint** do súboru `.env`:

| Premenná | Kde ju nájsť |
|----------|--------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portál → váš zdroj **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Vyžaduje sa (spolu s endpointom) na aktiváciu Azure AI Search v notebooku lekcie 16, ktorý používa autentifikáciu pomocou kľúčov. Azure portál → **Settings** → **Keys** → primárny administrátorský kľúč |

> **Prečo bez kľúčov?** Administrátorské kľúče poskytujú plný zápisný prístup k vašej vyhľadávacej službe a môžu sa vyzradiť v `.env` súboroch. S RBAC sa namiesto toho používa vaša identita z `az login` — rovnaký bezkľúčový vzor Entra ID, ktorý používajú notebooky kurzu (cez `AzureCliCredential` / `DefaultAzureCredential`). Pozrite [Pripojenie k Azure AI Search pomocou rolí](https://learn.microsoft.com/azure/search/search-security-rbac).

Pozrite si [sprievodcu nastavením Azure AI Search](./AzureSearch.md) pre plné príklady vytvárania indexov v Pythone a .NET.

## Ďalšie nastavenie pre lekcie, ktoré volajú Azure OpenAI priamo (lekcie 6 a 8)

Niektoré notebooky v lekciách 6 a 8 volajú **Azure OpenAI** priamo (používajúc **Responses API**) namiesto Microsoft Foundry projektu. Tieto príklady predtým používali GitHub Models, ktoré sú zastarané a nepodporujú Responses API. Pridajte tieto premenné do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|--------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portál → váš zdroj **Azure OpenAI** → **Keys and Endpoint** → Endpoint (napr. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Meno vášho nasadeného modelu (napr. `gpt-5-mini`), ktorý podporuje Responses API |
| `AZURE_OPENAI_API_KEY` | Voliteľné — len ak používate autentifikáciu pomocou kľúčov namiesto `az login` / Entra ID |

> Responses API používa stabilný endpoint `/openai/v1/`, takže nie je potrebná `api-version`. Prihláste sa pomocou `az login` pre použitie bezkľúčovej autentifikácie Entra ID.

## Alternatívny poskytovateľ: MiniMax (kompatibilný s OpenAI)

[MiniMax](https://platform.minimaxi.com/) poskytuje veľko-kontextové modely (až do 204K tokenov) cez API kompatibilné s OpenAI. Keďže Microsoft Agent Framework `OpenAIChatClient` funguje s akýmkoľvek OpenAI-kompatibilným endpointom, môžete použiť MiniMax ako náhradu pre lekcie používajúce `OpenAIChatClient`.

Pridajte tieto premenné do vášho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|--------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API kľúče |
| `MINIMAX_BASE_URL` | Použite `https://api.minimax.io/v1` (predvolená hodnota) |
| `MINIMAX_MODEL_ID` | Názov modelu na použitie (napr. `MiniMax-M3`) |

**Príklad modelov**: `MiniMax-M3` (odporúčané), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (rýchlejšie odpovede). Názvy modelov a dostupnosť sa môžu časom meniť, a prístup k danému modelu závisí od vášho účtu.

Kódové príklady používajúce `OpenAIChatClient` (napr. pracovný tok rezervácie hotela v lekcii 14) automaticky rozpoznajú a použijú vašu konfiguráciu MiniMax, keď je nastavená premenná `MINIMAX_API_KEY`.


## Alternatívny poskytovateľ: Novita AI (Kompatibilné s OpenAI)

[Novita AI](https://novita.ai/llm-api) poskytuje API kompatibilné s OpenAI pre open-source a frontier LLM (DeepSeek, Llama, Qwen a ďalšie). Keďže `OpenAIChatClient` z Microsoft Agent Framework funguje s akýmkoľvek endpointom kompatibilným s OpenAI, môžete použiť Novita AI ako alternatívu namiesto Azure OpenAI alebo OpenAI.

Pridajte tieto premenné do svojho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | Použite `https://api.novita.ai/openai/v1` (predvolená hodnota) |
| `NOVITA_MODEL_ID` | Názov modelu na použitie (napr. `moonshotai/kimi-k3`) |

**Príklad modelov**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI tiež hosťuje množstvo ďalších rodín open-source modelov (Llama, Qwen, GLM a ďalšie) — pozrite si [Novita AI modelovú knižnicu](https://novita.ai/llm-api) pre aktuálny zoznam dostupných modelov a ich modelových identifikátorov.

Aktuálne príklady automaticky nevyužívajú premenné `NOVITA_*`. Ak chcete použiť Novita AI, pri vytváraní `OpenAIChatClient` v spúšťanom príklade tieto hodnoty explicitne odovzdajte.

## Alternatívny poskytovateľ: Foundry Local (Spúšťanie modelov lokálne)

[Foundry Local](https://foundrylocal.ai) je ľahké runtime prostredie, ktoré sťahuje, spravuje a poskytuje jazykové modely **úplne na vašom vlastnom zariadení** cez API kompatibilné s OpenAI — bez potreby cloudu.

Pretože `OpenAIChatClient` z Microsoft Agent Framework funguje s akýmkoľvek endpointom kompatibilným s OpenAI, Foundry Local je lokálna alternativa namiesto Azure OpenAI.

**1. Nainštalujte Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Stiahnite a spustite model** (tým sa spustí aj lokálna služba):

```bash
foundry model list          # pozrite si dostupné modely
foundry model run phi-4-mini
```

**3. Nainštalujte Python SDK** používané na zistenie lokálneho endpointu:

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

> **Poznámka:** Foundry Local poskytuje OpenAI-kompatibilný endpoint pre **Chat Completions**. Používajte ho na lokálny vývoj a offline scenáre. Pre plnú sadu funkcií **Responses API** (stavové konverzácie atď.) používajte Azure OpenAI alebo Microsoft Foundry projekt.

## Ďalšie nastavenie pre lekciu 8 (Bing grounding workflow)

Podmienený workflow notebook v lekcii 8 používa **Bing grounding** cez Microsoft Foundry. Ak plánujete spustiť tento príklad, pridajte túto premennú do svojho `.env` súboru:

| Premenná | Kde ju nájsť |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portál → váš projekt → **Management** → **Connected resources** → vaša Bing konekcia → skopírujte ID konekcie |

## Riešenie problémov

### Chyby overenia SSL certifikátu na macOS

Ak používate macOS a vyskytnú sa vám chyby ako:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Toto je známy problém s Pythonom na macOS, kde systémové SSL certifikáty nie sú automaticky dôveryhodné. Vyskúšajte nasledujúce riešenia v poradí:

**Možnosť 1: Spustite Pythonovský skript na inštaláciu certifikátov (odporúčané)**

```bash
# Nahraďte 3.XX vašou nainštalovanou verziou Pythonu (napr. 3.12 alebo 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnosť 2: Použite `connection_verify=False` vo vašom notebooku (len pre GitHub Models notebooky)**

V notebooku z Lekcie 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je už zahrnutý zakomentovaný obchádzajúci postup. Odkomentujte `connection_verify=False`, keď narazíte na chyby certifikátu:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Vypnite overovanie SSL, ak narazíte na chyby certifikátu
)
```

> **⚠️ Varovanie:** Vypnutie overenia SSL (`connection_verify=False`) znižuje bezpečnosť tým, že preskakuje validáciu certifikátu. Používajte to len ako dočasný obchádzajúci postup v prostrediach vývoja. Nikdy to nepoužívajte v produkcii.

**Možnosť 3: Nainštalujte a používajte `truststore`**

```bash
pip install truststore
```

Potom pridajte nasledujúci riadok na začiatok vášho notebooku alebo skriptu pred vykonaním akýchkoľvek sieťových volaní:

```python
import truststore
truststore.inject_into_ssl()
```

## Niekde ste zaseknutý?

Ak máte akékoľvek problémy s nastavením, pripojte sa do nášho <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> alebo <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">vytvorte issue</a>.

## Ďalšia lekcia

Ste teraz pripravení spustiť kód pre tento kurz. Prajeme veľa šťastia pri objavovaní sveta AI Agentov! 

[Úvod do AI Agentov a prípadov ich použitia](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->