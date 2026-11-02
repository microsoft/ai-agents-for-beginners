# Nastavení kurzu

## Úvod

Tato lekce bude pokrývat, jak spustit ukázkové kódy z tohoto kurzu.

## Připojte se k ostatním studentům a získejte pomoc

Než začnete klonovat váš repozitář, připojte se do [AI Agents For Beginners Discord kanálu](https://aka.ms/ai-agents/discord), kde získáte pomoc se setupem, odpovědi na dotazy ohledně kurzu nebo kde se můžete spojit s ostatními studenty.

## Klonování nebo Forknutí tohoto repozitáře

Pro začátek, prosím, klonujte nebo forknete GitHub repozitář. Tím získáte vlastní verzi materiálů kurzu, abyste mohli spouštět, testovat a upravovat kód!

To můžete udělat kliknutím na odkaz <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forknout repozitář</a>

Nyní byste měli mít vlastní forknutou verzi tohoto kurzu na následujícím odkazu:

![Forknutý Repo](../../../translated_images/cs/forked-repo.33f27ca1901baa6a.webp)

### Příkaz Shallow Clone (doporučeno pro workshop / Codespaces)

  >Celý repozitář může být velký (~3 GB), pokud stáhnete celou historii a všechny soubory. Pokud se účastníte pouze workshopu nebo potřebujete jen několik lekcí, shallow clone (nebo sparse clone) stáhne mnohem méně.

#### Rychlý shallow clone — minimální historie, všechny soubory

V příkazech níže nahraďte `<your-username>` vaší URL fokrnu (nebo upstream URL, pokud preferujete).

Pro klonování pouze nejnovější historie commitu (malé stažení):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pro klonování konkrétní větve:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Částečný (sparse) clone — minimální blob data + pouze vybrané složky

Používá se částečný clone a sparse-checkout (vyžaduje Git 2.25+ a doporučuje moderní Git s podporou partial clone):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Přesuňte se do složky repozitáře:

```bash
cd ai-agents-for-beginners
```

Pak vyberte, které složky chcete stáhnout (příklad níže ukazuje dvě složky):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonování a ověření souborů, pokud potřebujete jen soubory a chcete uvolnit místo (bez git historie), smažte prosím metadata repozitáře (💀nevratné — ztratíte veškerou funkčnost Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Použití GitHub Codespaces (doporučeno k vyhnutí se velkým lokálním stažením)

- Vytvořte nový Codespace pro tento repozitář přes [GitHub UI](https://github.com/codespaces).  

- V terminálu nově vytvořeného codespace spusťte jeden z příkazů shallow/sparse clone výše, abyste stáhli jen potřebné složky kurzu do workspace Codespace.
- Volitelně: po klonování uvnitř Codespaces můžete odstranit .git, abyste uvolnili další místo (viz příkazy pro odstranění výše).
- Poznámka: Pokud chcete repozitář otevřít přímo v Codespaces (bez dalšího klonování), mějte na paměti, že Codespaces vytvoří devcontainer prostředí a může stále nakonfigurovat více věcí, než potřebujete.

#### Tipy

- Vždy nahraďte URL klonu vaším forkem, pokud chcete upravovat / commitovat.
- Pokud později budete potřebovat více historie nebo souborů, můžete je stáhnout nebo upravit sparse-checkout pro přidání dalších složek.

## Spuštění kódu

Tento kurz nabízí řadu Jupyter Notebooků, které můžete spouštět a získat praktické zkušenosti s tvorbou AI Agentů.

Ukázkové kódy používají **Microsoft Agent Framework (MAF)** s `FoundryChatClient`, který se připojuje k **Microsoft Foundry Agent Service V2** (API odpovědí) přes **Microsoft Foundry**.

Všechny Python noteboooky jsou označeny `*-python-agent-framework.ipynb`.

## Požadavky

- Python 3.12+
  - **POZNÁMKA**: Pokud nemáte Python 3.12 nainstalovaný, nainstalujte jej. Pak vytvořte své virtuální prostředí pomocí python3.12, aby byly správně nainstalovány verze z requirements.txt.
  
    >Příklad

    Vytvoření adresáře Python venv:

    ```bash
    python -m venv venv
    ```

    Pak aktivujte venv prostředí pro:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Pro ukázkové kódy používající .NET, zajistěte, že máte nainstalovaný [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) nebo novější. Pak zkontrolujte verzi nainstalovaného .NET SDK:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Požadováno pro autentizaci. Nainstalujte z [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Pro přístup k Microsoft Foundry a Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Projekt s nasazeným modelem (např. `gpt-5-mini`). Viz [Krok 1](#krok-1-vytvoření-microsoft-foundry-projektu) níže.

V kořenovém adresáři tohoto repozitáře je soubor `requirements.txt`, který obsahuje všechny požadované Python balíčky pro spuštění kódů.

Nainstalujete je pomocí příkazu, který spusťte ve vašem terminálu v kořenovém adresáři repozitáře:

```bash
pip install -r requirements.txt
```

Doporučujeme vytvořit si Python virtuální prostředí, aby nedocházelo ke konfliktům a problémům.

## Nastavení VSCode

Ujistěte se, že ve VSCode používáte správnou verzi Pythonu.

![obrázek](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavení Microsoft Foundry a Microsoft Foundry Agent Service

### Krok 1: Vytvoření Microsoft Foundry projektu

Potřebujete Microsoft Foundry **hub** a **projekt** s nasazeným modelem pro spuštění notebooků.

1. Jděte na [ai.azure.com](https://ai.azure.com) a přihlaste se pomocí svého Azure účtu.
2. Vytvořte **hub** (nebo použijte existující). Viz: [Přehled zdrojů hubu](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. V rámci hubu vytvořte **projekt**.
4. Nasadíte model (např. `gpt-5-mini`) přes **Models + Endpoints** → **Deploy model**.

### Krok 2: Získání koncového bodu projektu a jména nasazení modelu

Ve vašem projektu v Microsoft Foundry portálu:

- **Koncový bod projektu** — Jděte na stránku **Overview** a zkopírujte URL koncového bodu.

![Řetězec připojení projektu](../../../translated_images/cs/project-endpoint.8cf04c9975bbfbf1.webp)

- **Jméno nasazení modelu** — Jděte do **Models + Endpoints**, vyberte nasazený model a poznamenejte si **deployment name** (např. `gpt-5-mini`).

### Krok 3: Přihlášení do Azure pomocí `az login`

Většina notebooků se autentizuje přes váš **Azure CLI login** — pomocí `AzureCliCredential` nebo `DefaultAzureCredential` (které obě vidí vaši `az login` relaci) z balíčku `azure-identity` — takže nepotřebují API klíče. Několik lekcí a volitelných integrací používá API klíče; zkontrolujte požadavky pro každou lekci kvůli přidaným proměnným prostředí. Vyžaduje to být přihlášen přes Azure CLI.

1. **Nainstalujte Azure CLI** pokud ještě není nainstalováno: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Přihlaste se** tímto příkazem:

    ```bash
    az login
    ```

    Nebo pokud jste v vzdáleném Codespace prostředí bez prohlížeče:

    ```bash
    az login --use-device-code
    ```

3. **Vyberte si předplatné** pokud je vyžadováno — vyberte to, které obsahuje váš Foundry projekt.

4. **Ověřte**, že jste přihlášeni:

    ```bash
    az account show
    ```

> **Proč `az login`?** Notebooky se autentizují pomocí `AzureCliCredential` (nebo `DefaultAzureCredential`), které také vidí vaši Azure CLI přihlášení z balíčku `azure-identity`. To znamená, že vaše Azure CLI relace poskytuje přihlašovací údaje — žádné API klíče nebo tajné údaje v `.env` souboru. To je [doporučený bezpečnostní postup](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Krok 4: Vytvořte svůj `.env` Soubor

Zkopírujte příklad:

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Proměnná | Kde ji najít |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portál → váš projekt → stránka **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portál → **Models + Endpoints** → jméno vašeho nasazeného modelu |

To je vše pro většinu lekcí! Notebooky se autentizují automaticky skrz vaši `az login` relaci.

### Krok 5: Instalace Python závislostí

```bash
pip install -r requirements.txt
```

Doporučujeme spustit to uvnitř vámi vytvořeného virtuálního prostředí.

## Volitelné nastavení: Azure AI Search (Lekce 5 a 16)

Notebooky Lekce 5 (Agentic RAG) a Lekce 16 běží ihned s **in-memory knowledge base** — bez potřeby dalších Azure zdrojů. Pokud chcete používat místo toho skutečný **Azure AI Search** index, uvědomte si, že **notebook Lekce 16 aktuálně používá autentizaci pomocí klíče**: přepíná z in-memory vyhledávání na Azure AI Search pouze pokud jsou nastaveny **současně** `AZURE_SEARCH_SERVICE_ENDPOINT` **a** `AZURE_SEARCH_API_KEY`, jinak zůstává u in-memory vyhledávání — pro použití skutečného indexu tedy musíte nastavit i admin klíč. Bezkřídlová autentizace pomocí Microsoft Entra ID (RBAC) je doporučený přístup pro vlastní produkční kód, v souladu s `az login` přihlašovacím procesem používaným v ostatních částech kurzu.

Níže uvedené RBAC kroky se vztahují na ukázkové příklady setup guide a váš vlastní kód. Neaktivují bezklíčovou autentizaci v notebooku Lekce 16; Lekce 16 stále vyžaduje zároveň endpoint a admin klíč pro použití Azure AI Search.

1. **Povolte role-based access** na vaší search službě:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Přiřaďte si potřebné role** (vytváření/nahrávání indexů a dotazy):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Přidejte endpoint** do vašeho `.env` souboru:

| Proměnná | Kde ji najít |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portál → vaše **Azure AI Search** služba → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Nutné (spolu s endpoint) pro povolení Azure AI Search v notebooku Lekce 16, který používá autentizaci pomocí klíče. Azure portál → **Nastavení** → **Klíče** → primární admin klíč |

> **Proč bez klíče?** Admin klíče dávají plný zápisový přístup do vaší search služby a mohou být ztraceny přes `.env` soubory. Pomocí RBAC je používána vaše `az login` identita — stejný bezklíčový Entra ID vzor, který také používají notebooky kurzu (pomocí `AzureCliCredential` / `DefaultAzureCredential`). Viz [Připojení k Azure AI Search pomocí rolí](https://learn.microsoft.com/azure/search/search-security-rbac).

Viz také [Azure AI Search setup guide](./AzureSearch.md) pro kompletní příklady vytváření indexů v Pythonu a .NET.

## Dodatečné nastavení pro lekce, které volají Azure OpenAI přímo (Lekce 6 a 8)

Některé notebooky v lekcích 6 a 8 volají **Azure OpenAI** přímo (pomocí **Responses API**) místo Microsoft Foundry projektu. Tyto ukázky dříve používaly GitHub Models, což je zastaralé a nepodporuje Responses API. Přidejte tyto proměnné do vašeho `.env` souboru:

| Proměnná | Kde ji najít |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portál → vaše **Azure OpenAI** služba → **Keys and Endpoint** → Endpoint (např. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Jméno vašeho nasazeného modelu (např. `gpt-5-mini`), který podporuje Responses API |
| `AZURE_OPENAI_API_KEY` | Volitelné — pokud používáte autentizaci pomocí klíče místo `az login` / Entra ID |

> Responses API používá stabilní `/openai/v1/` endpoint, takže není potřeba `api-version`. Přihlaste se pomocí `az login` pro bezklíčovou Entra ID autentizaci.

## Alternativní poskytovatel: MiniMax (kompatibilní s OpenAI)

[MiniMax](https://platform.minimaxi.com/) poskytuje modely s velkým kontextem (až 204K tokenů) přes API kompatibilní s OpenAI. Protože Microsoft Agent Framework `OpenAIChatClient` funguje s jakýmkoliv OpenAI-kompatibilním endpointem, můžete MiniMax použít jako alternativu v lekcích, které využívají `OpenAIChatClient`.

Přidejte tyto proměnné do souboru `.env`:

| Proměnná | Kde ji najít |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Klíče |
| `MINIMAX_BASE_URL` | Použijte `https://api.minimax.io/v1` (výchozí hodnota) |
| `MINIMAX_MODEL_ID` | Jméno modelu k použití (např. `MiniMax-M3`) |

**Příklad modelů**: `MiniMax-M3` (doporučeno), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (rychlejší odpovědi). Jména modelů a dostupnost se časem mohou měnit a přístup závisí na vašem účtu.

Ukázky kódů používající `OpenAIChatClient` (např. pracovní postup pro rezervaci hotelu v Lekci 14) automaticky detekují a použijí vaši MiniMax konfiguraci, pokud je nastavena `MINIMAX_API_KEY`.


## Alternativní poskytovatel: Novita AI (kompatibilní s OpenAI)

[Novita AI](https://novita.ai/llm-api) poskytuje API kompatibilní s OpenAI pro open-source a průkopnické LLM (DeepSeek, Llama, Qwen a další). Protože `OpenAIChatClient` z Microsoft Agent Framework funguje s libovolným endpointem kompatibilním s OpenAI, můžete používat Novita AI jako přímou alternativu k Azure OpenAI nebo OpenAI.

Přidejte tyto proměnné do svého souboru `.env`:

| Proměnná | Kde ji najít |
|----------|--------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | Použijte `https://api.novita.ai/openai/v1` (výchozí hodnota) |
| `NOVITA_MODEL_ID` | Název modelu k použití (např. `moonshotai/kimi-k3`) |

**Příklad modelů**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI také hostuje mnoho dalších rodin open-source modelů (Llama, Qwen, GLM a další) — zkontrolujte [knihovnu modelů Novita AI](https://novita.ai/llm-api) pro aktuální seznam dostupných modelů a jejich ID modelů.

Aktuální vzory automaticky nepoužívají proměnné `NOVITA_*`. Pro použití Novita AI explicitně předáte tyto hodnoty při konstrukci `OpenAIChatClient` ve vzoru, který spouštíte.

## Alternativní poskytovatel: Foundry Local (spouštění modelů lokálně)

[Foundry Local](https://foundrylocal.ai) je lehké runtime, které stahuje, spravuje a poskytuje jazykové modely **zcela na vašem vlastním počítači** prostřednictvím API kompatibilního s OpenAI — bez potřeby cloudu.

Protože `OpenAIChatClient` z Microsoft Agent Framework funguje s libovolným endpointem kompatibilním s OpenAI, Foundry Local je přímá lokální alternativa k Azure OpenAI.

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

**3. Nainstalujte Python SDK**, které se používá k nalezení lokálního endpointu:

```bash
pip install foundry-local-sdk
```

**4. Nastavte Microsoft Agent Framework na váš lokální model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Stáhne (pokud je to potřeba) a poskytne model lokálně, poté zjistí endpoint/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # např. http://localhost:<port>/v1
    api_key=manager.api_key,        # vždy "not-required" pro Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Poznámka:** Foundry Local zpřístupňuje endpoint **Chat Completions** kompatibilní s OpenAI. Používejte ho pro lokální vývoj a offline scénáře. Pro plnou sadu funkcí **Responses API** (stavové konverzace atd.) používejte Azure OpenAI nebo projekt Microsoft Foundry.

## Dodatečné nastavení pro lekci 8 (Bing grounding workflow)

Podmíněný workflow notebook v lekci 8 používá **Bing grounding** přes Microsoft Foundry. Pokud plánujete spustit tento vzor, přidejte tuto proměnnou do svého souboru `.env`:

| Proměnná | Kde ji najít |
|----------|--------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portál → váš projekt → **Management** → **Connected resources** → vaše připojení k Bingu → zkopírujte ID připojení |

## Řešení problémů

### Chyby ověření SSL certifikátu na macOS

Pokud jste na macOS a narazíte na chybu jako:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Jedná se o známý problém s Pythonem na macOS, kde systémové SSL certifikáty nejsou automaticky důvěryhodné. Vyzkoušejte tato řešení v pořadí:

**Možnost 1: Spusťte Python skript Install Certificates (doporučeno)**

```bash
# Nahraďte 3.XX vaší nainstalovanou verzí Pythonu (např. 3.12 nebo 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnost 2: Použijte `connection_verify=False` ve vašem notebooku (pouze pro GitHub Models notebooky)**

V notebooku lekce 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je již zahrnuto zakomentované řešení. Odkomentujte `connection_verify=False`, pokud narazíte na chyby certifikátu:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Zakázat ověřování SSL, pokud narazíte na chyby certifikátu
)
```

> **⚠️ Varování:** Vypnutí ověřování SSL (`connection_verify=False`) snižuje bezpečnost tím, že přeskočí validaci certifikátů. Používejte to pouze jako dočasné řešení ve vývojovém prostředí. Nikdy to nepoužívejte v produkci.

**Možnost 3: Nainstalujte a použijte `truststore`**

```bash
pip install truststore
```

Poté přidejte následující na začátek vašeho notebooku nebo skriptu před jakýmikoliv síťovými voláními:

```python
import truststore
truststore.inject_into_ssl()
```

## Máte problém?

Pokud máte nějaké problémy při této instalaci, připojte se na náš <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> nebo <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">vytvořte issue</a>.

## Další lekce

Nyní jste připraveni spustit kód tohoto kurzu. Přejeme vám hodně zábavy při dalším objevování světa AI agentů! 

[Úvod do AI agentů a případy použití agentů](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->