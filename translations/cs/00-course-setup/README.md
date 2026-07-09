# Nastavení kurzu

## Úvod

Tato lekce vás provede tím, jak spustit ukázky kódu tohoto kurzu.

## Připojte se k ostatním studentům a získejte pomoc

Než začnete klonovat své repo, připojte se na [kanál AI Agents For Beginners na Discordu](https://aka.ms/ai-agents/discord), kde získáte pomoc s nastavením, odpovědi na dotazy týkající se kurzu nebo se můžete spojit s ostatními studenty.

## Klonujte nebo Forkujte toto Repo

Začněte, prosím, klonováním nebo forkováním GitHub repozitáře. Tím si vytvoříte vlastní verzi materiálů kurzu, abyste mohli kód spouštět, testovat a upravovat!

To lze provést kliknutím na odkaz <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forkujte repo</a>

Nyní byste měli mít vlastní forkovanou verzi tohoto kurzu na následujícím odkazu:

![Forked Repo](../../../translated_images/cs/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (doporučeno pro workshop / Codespaces)

  >Celé repozitáře může být velké (~3 GB), pokud stáhnete kompletní historii a všechny soubory. Pokud se účastníte pouze workshopu nebo potřebujete jen několik lekčních složek, shallow clone (nebo sparse clone) vynechá většinu historie a/nebo blobů a sníží tak objem stahování.

#### Rychlý shallow clone — minimální historie, všechny soubory

Nahraďte `<your-username>` v příkazech níže URL vašeho forku (nebo upstream URL, pokud preferujete).

Pro klonování pouze nejnovější historie commitu (malé stažení):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pro klonování specifické větve:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Částečný (sparse) clone — minimální blob + jen vybrané složky

Používá se zde partial clone a sparse-checkout (vyžaduje Git 2.25+ a doporučuje se moderní Git s podporou partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Přejděte do složky repozitáře:

```bash|powershell
cd ai-agents-for-beginners
```

Pak určete, které složky chcete (příklad níže ukazuje dvě složky):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonování a ověření souborů, pokud potřebujete jen soubory a chcete uvolnit místo (bez git historie), smažte metadata repozitáře (💀nevratné — ztratíte veškerou git funkcionalitu: žádné commity, pull, push nebo přístup k historii).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Použití GitHub Codespaces (doporučeno pro vyhnutí se velkým lokálním stažením)

- Vytvořte nový Codespace pro toto repo přes [GitHub UI](https://github.com/codespaces).  

- V terminálu nově vytvořeného codespace spusťte jeden z příkazů shallow/sparse clone výše, abyste dostali do Codespace pracovní plochy pouze lekční složky, které potřebujete.
- Volitelné: po klonování uvnitř Codespaces odstraňte `.git` pro uvolnění místa (viz příkazy pro odstranění výše).
- Poznámka: Pokud preferujete otevřít repo přímo v Codespaces (bez dalšího klonování), mějte na paměti, že Codespaces vytvoří devcontainer prostředí a může přesto připravit více věcí, než potřebujete. Klonování shallow kopie uvnitř nového Codespace vám dává větší kontrolu nad využitím disku.

#### Tipy

- Vždy nahraďte URL klonu vaším forkem, pokud chcete upravovat/commitovat.
- Pokud později potřebujete více historie nebo souborů, můžete je stáhnout nebo upravit sparse-checkout pro zahrnutí dalších složek.

## Spuštění kódu

Tento kurz nabízí sérii Jupyter Notes, které můžete spustit a získat tak praktické zkušenosti s tvorbou AI Agentů.

Ukázky kódu používají **Microsoft Agent Framework (MAF)** s `FoundryChatClient`, který se připojuje k **Microsoft Foundry Agent Service V2** (Responses API) přes **Microsoft Foundry**.

Všechny Python noteboky jsou označeny `*-python-agent-framework.ipynb`.

## Požadavky

- Python 3.12+
  - **POZNÁMKA**: Pokud nemáte nainstalovaný Python 3.12, nezapomeňte jej nainstalovat. Poté vytvořte `venv` s python3.12, aby se nainstalovaly správné verze z `requirements.txt`.
  
    >Příklad

    Vytvoření adresáře Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    Poté aktivujte venv prostředí pro:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Pro ukázkové kódy využívající .NET, instalujte [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) nebo novější. Pak zkontrolujte instalovanou verzi .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — požadováno pro autentizaci. Instalujte z [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Pro přístup k Microsoft Foundry a Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Projekt s nasazeným modelem (např. `gpt-4o`). Viz [Krok 1](#krok-1-vytvořte-microsoft-foundry-projekt) níže.

V kořenovém adresáři tohoto repozitáře je soubor `requirements.txt`, který obsahuje všechny požadované Python balíčky pro spuštění ukázek kódu.

Můžete je nainstalovat spuštěním následujícího příkazu v terminálu v kořenovém adresáři repozitáře:

```bash|powershell
pip install -r requirements.txt
```

Doporučujeme vytvořit Python virtuální prostředí, aby nedocházelo ke konfliktům a problémům.

## Nastavení VSCode

Ujistěte se, že ve VSCode používáte správnou verzi Pythonu.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavení Microsoft Foundry a Microsoft Foundry Agent Service

### Krok 1: Vytvořte Microsoft Foundry projekt

Potřebujete Microsoft Foundry **hub** a **projekt** s nasazeným modelem, aby se daly spustit notebooky.

1. Přejděte na [ai.azure.com](https://ai.azure.com) a přihlaste se se svým Azure účtem.
2. Vytvořte **hub** (nebo použijte existující). Viz: [Přehled zdrojů hubu](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Uvnitř hubu vytvořte **projekt**.
4. Nasadíte model (např. `gpt-4o`) přes **Models + Endpoints** → **Deploy model**.

### Krok 2: Získejte Endpoint projektu a název nasazení modelu

Ve vašem projektu v Microsoft Foundry portálu:

- **Project Endpoint** — Přejděte na stránku **Overview** a zkopírujte URL endpointu.

![Project Connection String](../../../translated_images/cs/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Přejděte na **Models + Endpoints**, vyberte svůj nasazený model a zapište si **Deployment name** (např. `gpt-4o`).

### Krok 3: Přihlaste se do Azure pomocí `az login`

Všechny notebooky používají pro autentizaci **`AzureCliCredential`** — žádné API klíče ke správě. To vyžaduje, abyste byli přihlášeni přes Azure CLI.

1. **Nainstalujte Azure CLI**, pokud jej ještě nemáte: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Přihlaste se** spuštěním:

    ```bash|powershell
    az login
    ```

    Nebo pokud jste v remote/Codespace prostředí bez prohlížeče:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vyberte svou subscription**, pokud budete vyzváni — vyberte tu, která obsahuje váš Foundry projekt.

4. **Ověřte**, že jste přihlášeni:

    ```bash|powershell
    az account show
    ```

> **Proč `az login`?** Notebooky autentizují pomocí `AzureCliCredential` z balíčku `azure-identity`. To znamená, že vaše Azure CLI relace poskytuje přihlašovací údaje — žádné API klíče nebo tajemství v `.env` souboru. Je to [bezpečná osvědčená praxe](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Krok 4: Vytvořte svůj `.env` soubor

Zkopírujte příkladový soubor:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Otevřete `.env` a vyplňte tyto dvě hodnoty:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Proměnná | Kde ji najít |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portál → váš projekt → stránka **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portál → **Models + Endpoints** → název vašeho nasazeného modelu |

To je vše pro většinu lekcí! Notebooky se přihlásí automaticky přes vaši `az login` relaci.

### Krok 5: Nainstalujte Python závislosti

```bash|powershell
pip install -r requirements.txt
```

Doporučujeme tento příkaz spustit uvnitř virtualního prostředí, které jste dříve vytvořili.

## Další nastavení pro lekci 5 (Agentic RAG)

Lekce 5 využívá **Azure AI Search** pro retrieval-augmented generation. Pokud plánujete tuto lekci spustit, přidejte do vašeho `.env` souboru tyto proměnné:

| Proměnná | Kde ji najít |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portál → váš **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portál → váš **Azure AI Search** resource → **Settings** → **Keys** → primární admin klíč |

## Další nastavení pro lekce, které volají Azure OpenAI přímo (leckce 6 a 8)

Některé notebooky v lekcích 6 a 8 volají **Azure OpenAI** přímo (pomocí **Responses API**) místo použití Microsoft Foundry projektu. Tyto ukázky dříve používaly GitHub Models, které jsou zastaralé (ukončení v červenci 2026) a nepodporují Responses API. Pokud plánujete tyto ukázky spustit, přidejte do `.env` tyto proměnné:

| Proměnná | Kde ji najít |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portál → váš **Azure OpenAI** resource → **Keys and Endpoint** → Endpoint (např. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Název vašeho nasazeného modelu (např. `gpt-4o-mini`), který podporuje Responses API |
| `AZURE_OPENAI_API_KEY` | Volitelné — jen pokud používáte autentizaci na bázi klíče místo `az login` / Entra ID |

> Responses API používá stabilní `/openai/v1/` endpoint, takže není potřeba `api-version`. Přihlaste se pomocí `az login` pro bezklíčovou autentizaci Entra ID.

## Alternativní poskytovatel: MiniMax (OpenAI-kompatibilní)

[MiniMax](https://platform.minimaxi.com/) nabízí modely s dlouhým kontextem (až 204K tokenů) prostřednictvím OpenAI-kompatibilního API. Protože `OpenAIChatClient` Microsoft Agent Frameworku funguje s jakýmkoli OpenAI-kompatibilním endpointem, můžete MiniMax používat jako náhradu Azure OpenAI nebo OpenAI.

Přidejte tyto proměnné do vašeho `.env` souboru:

| Proměnná | Kde ji najít |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API klíče |
| `MINIMAX_BASE_URL` | Použijte `https://api.minimax.io/v1` (výchozí hodnota) |
| `MINIMAX_MODEL_ID` | Název modelu k použití (např. `MiniMax-M3`) |

**Příklad modelů**: `MiniMax-M3` (doporučeno), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (rychlejší odpovědi). Název a dostupnost modelů se může měnit a přístup k určitým modelům může záviset na vašem účtu nebo regionu — ověřte aktuální seznam na [MiniMax Platform](https://platform.minimaxi.com/). Pokud `MiniMax-M3` není dostupný vašemu účtu, nastavte `MINIMAX_MODEL_ID` na model, ke kterému máte přístup (např. `MiniMax-M2.7`).

Ukázky kódu, které používají `OpenAIChatClient` (např. lekce 14 workflow rezervace hotelu) automaticky rozpoznají a použijí konfiguraci MiniMax, pokud je nastaven `MINIMAX_API_KEY`.

## Alternativní poskytovatel: Foundry Local (spouštění modelů lokálně)

[Foundry Local](https://foundrylocal.ai) je lehké runtime, které stahuje, spravuje a poskytuje jazykové modely **přímo na vašem zařízení** přes OpenAI-kompatibilní API — bez cloudu, Azure subscription a API klíčů. Je to skvělá volba pro offline vývoj, experimentování bez nákladů na cloud nebo pro uchování dat lokálně.

Protože `OpenAIChatClient` Microsoft Agent Frameworku funguje s jakýmkoli OpenAI-kompatibilním endpointem, Foundry Local je lokální alternativou k Azure OpenAI.

**1. Nainstalujte Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Stáhněte a spusťte model** (tím se také spustí lokální služba):

```bash
foundry model list          # zobrazit dostupné modely
foundry model run phi-4-mini
```

**3. Nainstalujte Python SDK** používané k objevování lokálního endpointu:

```bash
pip install foundry-local-sdk
```

**4. Nastavte Microsoft Agent Framework na váš lokální model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Stáhne (pokud je potřeba) a lokálně poskytne model, poté zjistí koncový bod/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # např. http://localhost:<port>/v1
    api_key=manager.api_key,        # vždy "nevyžadováno" pro Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Poznámka:** Foundry Local vystavuje OpenAI-kompatibilní **Chat Completions** endpoint. Používejte ho pro lokální vývoj a offline scénáře. Pro plnou funkcionalitu **Responses API** (stavové konverzace, hluboká orchestrace nástrojů a agentní vývoj) cílujte na **Azure OpenAI** nebo **Microsoft Foundry** projekt, jak je ukázáno v lekcích. Viz [Foundry Local dokumentace](https://foundrylocal.ai) pro aktuální katalog modelů a podporu platforem.

## Další nastavení pro lekci 8 (Bing Grounding Workflow)


Podmíněný pracovní postup v sešitu v lekci 8 používá **Bing grounding** přes Microsoft Foundry. Pokud plánujete spustit tento příklad, přidejte tuto proměnnou do vašeho souboru `.env`:

| Proměnná | Kde ji najít |
|----------|-------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portál → váš projekt → **Správa** → **Připojené zdroje** → vaše Bing připojení → zkopírujte ID připojení |

## Řešení problémů

### Chyby ověřování SSL certifikátu na macOS

Pokud používáte macOS a narazíte na chybu jako:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Jedná se o známý problém s Pythonem na macOS, kde systémové SSL certifikáty nejsou automaticky důvěryhodné. Vyzkoušejte následující řešení v pořadí:

**Možnost 1: Spusťte skript Install Certificates v Pythonu (doporučeno)**

```bash
# Nahraďte 3.XX svou nainstalovanou verzí Pythonu (např. 3.12 nebo 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnost 2: Použijte `connection_verify=False` ve vašem sešitu (pouze pro sešity GitHub Models)**

V sešitu Lekce 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je již zahrnutá zakomentovaná alternativa. Odkomentujte `connection_verify=False` při vytváření klienta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Zakázat ověřování SSL, pokud narazíte na chyby certifikátu
)
```

> **⚠️ Upozornění:** Vypnutí ověřování SSL (`connection_verify=False`) snižuje zabezpečení tím, že přeskočí validaci certifikátů. Používejte to pouze jako dočasné řešení ve vývojových prostředích a nikdy ne v produkci.

**Možnost 3: Nainstalujte a používejte `truststore`**

```bash
pip install truststore
```

Poté přidejte následující na začátek vašeho sešitu nebo skriptu ještě před provedením síťových volání:

```python
import truststore
truststore.inject_into_ssl()
```

## Někam jste uvízli?

Pokud máte jakékoli problémy s nastavením, připojte se do naší <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> nebo <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">vytvořte issue</a>.

## Další lekce

Nyní jste připraveni spustit kód tohoto kurzu. Přejeme příjemné učení o světě AI Agentů!

[Úvod do AI agentů a použití agentů](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->