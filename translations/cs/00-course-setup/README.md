# Nastavení kurzu

## Úvod

Tato lekce pokryje, jak spustit ukázky kódu tohoto kurzu.

## Připojte se k ostatním studentům a získejte pomoc

Než začnete klonovat svůj repozitář, připojte se k [AI Agents For Beginners Discord kanálu](https://aka.ms/ai-agents/discord), kde můžete získat pomoc s nastavením, odpovědi na otázky ohledně kurzu, nebo se spojit s ostatními studenty.

## Naklonujte nebo Forkněte tento repozitář

Nejprve prosím naklonujte nebo forknete GitHub Repozitář. Tím získáte vlastní verzi materiálu kurzu, kterou můžete spouštět, testovat a upravovat kód!

To lze provést kliknutím na odkaz pro <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forknutí repozitáře</a>

Nyní byste měli mít vlastní forknutou verzi tohoto kurzu na následujícím odkazu:

![Forknutý repozitář](../../../translated_images/cs/forked-repo.33f27ca1901baa6a.webp)

### Mělký klon (doporučeno pro workshop / Codespaces)

  >Plný repozitář může být velký (~3 GB), pokud stáhnete celou historii a všechny soubory. Pokud se účastníte jen workshopu nebo potřebujete jen několik složek lekcí, mělký klon (nebo řídký klon) vynechá většinu stahování tím, že zkrátí historii a/nebo přeskočí blobs.

#### Rychlý mělký klon — minimální historie, všechny soubory

Nahraďte `<your-username>` v níže uvedených příkazech URL vašeho forku (nebo upstream URL, pokud dáváte přednost).

Pro naklonování pouze nejnovější historie commitu (malé stahování):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pro klonování specifické větve:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Částečný (řídký) klon — minimální blobs + pouze vybrané složky

Používá částečný klon a sparse-checkout (vyžaduje Git 2.25+ a doporučuje se moderní Git s podporou částečného klonování):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Přejděte do složky repozitáře:

```bash|powershell
cd ai-agents-for-beginners
```

Pak specifikujte, které složky chcete (příklad níže ukazuje dvě složky):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonování a ověření souborů, pokud potřebujete pouze soubory a chcete uvolnit místo (bez git historie), prosím odstraňte metadata repozitáře (💀nevratné – ztratíte veškerou Git funkcionalitu: žádné commity, pully, pushy ani přístup k historii).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Použití GitHub Codespaces (doporučeno pro vyhnutí se velkým lokálním stahováním)

- Vytvořte nový Codespace pro tento repozitář přes [GitHub UI](https://github.com/codespaces).  

- V terminálu nově vytvořeného codespace spusťte jeden z výše uvedených příkazů pro mělký/řídký klon, abyste do Codespace pracovního prostoru přinesli pouze potřebné složky lekcí.
- Nepovinné: po klonování uvnitř Codespaces odstraňte .git pro uvolnění místa (viz výše uvedené příkazy pro odstranění).
- Poznámka: Pokud dáváte přednost otevření repozitáře přímo v Codespaces (bez dodatečného klonování), mějte na paměti, že Codespaces sestaví prostředí devcontainer a může stále provisionovat více, než potřebujete. Klonování mělké kopie uvnitř nového Codespace vám dává větší kontrolu nad využitím disku.

#### Tipy

- Vždy nahraďte URL klonu vaším forkem, pokud chcete editovat/commitovat.
- Pokud pak budete potřebovat více historie nebo souborů, můžete je stáhnout nebo upravit sparse-checkout tak, aby zahrnoval další složky.

## Spuštění kódu

Tento kurz nabízí sérii Jupyter Notebooků, které můžete spustit, abyste získali praktické zkušenosti s tvorbou AI agentů.

Ukázky kódu používají **Microsoft Agent Framework (MAF)** s `FoundryChatClient`, který se připojuje k **Microsoft Foundry Agent Service V2** (Responses API) přes **Microsoft Foundry**.

Všechny Python notebooky jsou označeny `*-python-agent-framework.ipynb`.

## Požadavky

- Python 3.12+
  - **POZNÁMKA**: Pokud nemáte nainstalovaný Python3.12, ujistěte se, že jej nainstalujete. Poté vytvořte své virtuální prostředí pomocí python3.12, aby se nainstalovaly správné verze dle souboru requirements.txt.
  
    >Příklad

    Vytvoření Python venv adresáře:

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

- .NET 10+: Pro ukázkové kódy používající .NET, ujistěte se, že máte nainstalovaný [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) nebo novější. Pak ověřte nainstalovanou verzi .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Požadováno pro autentizaci. Nainstalujte z [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Pro přístup k Microsoft Foundry a Microsoft Foundry Agent Service.
- **Microsoft Foundry Projekt** — Projekt s nasazeným modelem (např. `gpt-5-mini`). Viz [Krok 1](#krok-1-vytvoření-microsoft-foundry-projektu) níže.

V kořenovém adresáři tohoto repozitáře je soubor `requirements.txt`, který obsahuje všechny požadované Python balíčky pro spuštění ukázek kódu.

Můžete je nainstalovat spuštěním následujícího příkazu ve vašem terminálu v kořenovém adresáři repozitáře:

```bash|powershell
pip install -r requirements.txt
```

Doporučujeme vytvořit Python virtuální prostředí, aby nedošlo ke konfliktům a problémům.

## Nastavení VSCode

Ujistěte se, že ve VSCode používáte správnou verzi Pythonu.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavení Microsoft Foundry a Microsoft Foundry Agent Service

### Krok 1: Vytvoření Microsoft Foundry projektu

Potřebujete Microsoft Foundry **hub** a **projekt** s nasazeným modelem, abyste mohli spustit notebooky.

1. Přejděte na [ai.azure.com](https://ai.azure.com) a přihlaste se ke svému Azure účtu.
2. Vytvořte **hub** (nebo použijte existující). Viz: [Přehled zdrojů hubu](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. V rámci hubu vytvořte **projekt**.
4. Nasadte model (např. `gpt-5-mini`) z **Models + Endpoints** → **Deploy model**.

### Krok 2: Získání EndPointu projektu a jména nasazení modelu

Ve vašem projektu v Microsoft Foundry portálu:

- **Project Endpoint** — Přejděte na stránku **Overview** a zkopírujte URL endpointu.

![Řetězec připojení projektu](../../../translated_images/cs/project-endpoint.8cf04c9975bbfbf1.webp)

- **Název nasazení modelu** — Přejděte do **Models + Endpoints**, vyberte nasazený model a poznamenejte si **Deployment name** (např. `gpt-5-mini`).

### Krok 3: Přihlášení do Azure pomocí `az login`

Všechny notebooky používají k autentizaci **`AzureCliCredential`** — není potřeba spravovat API klíče. Vyžaduje to být přihlášený přes Azure CLI.

1. **Nainstalujte Azure CLI**, pokud jej ještě nemáte: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Přihlaste se** spuštěním příkazu:

    ```bash|powershell
    az login
    ```

    Nebo pokud jste v remote/Codespace prostředí bez prohlížeče:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vyberte předplatné**, pokud budete vyzváni — vyberte to, které obsahuje váš Foundry projekt.

4. **Ověřte**, že jste přihlášení:

    ```bash|powershell
    az account show
    ```

> **Proč `az login`?** Notebooky autentizují pomocí `AzureCliCredential` z balíčku `azure-identity`. To znamená, že vaše Azure CLI relace zajišťuje přihlašovací údaje — žádné klíče API nebo tajemství ve vašem `.env` souboru. Toto je [nejlepší bezpečnostní praxe](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Krok 4: Vytvoření vašeho `.env` souboru

Zkopírujte ukázkový soubor:

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

To je vše pro většinu lekcí! Notebooky se autentizují automaticky přes vaši `az login` relaci.

### Krok 5: Instalace Python závislostí

```bash|powershell
pip install -r requirements.txt
```

Doporučujeme toto spustit uvnitř virtuálního prostředí, které jste dříve vytvořili.

## Dodatečné nastavení pro Lekci 5 (Agentic RAG)

Lekce 5 používá **Azure AI Search** pro retrieval-augmented generování. Pokud plánujete tuto lekci spustit, přidejte tyto proměnné do vašeho `.env` souboru:

| Proměnná | Kde ji najít |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portál → vaše **Azure AI Search** zdroje → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portál → vaše **Azure AI Search** zdroje → **Settings** → **Keys** → primární admin klíč |

## Dodatečné nastavení pro lekce, které volají přímo Azure OpenAI (Lekce 6 a 8)

Některé notebooky v lekcích 6 a 8 volají **Azure OpenAI** přímo (používají **Responses API**) místo Microsoft Foundry projektu. Tyto ukázky dříve používaly GitHub Models, které jsou zastaralé (bude ukončeno v červenci 2026) a nepodporují Responses API. Pokud plánujete tyto ukázky spustit, přidejte tyto proměnné do vašeho `.env` souboru:

| Proměnná | Kde ji najít |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portál → váš **Azure OpenAI** zdroj → **Keys and Endpoint** → Endpoint (např. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Název vašeho nasazeného modelu (např. `gpt-5-mini`), který podporuje Responses API |
| `AZURE_OPENAI_API_KEY` | Nepovinné — jen pokud používáte autentizaci klíčem místo `az login` / Entra ID |

> Responses API používá stabilní `/openai/v1/` endpoint, takže není potřeba `api-version`. Přihlaste se pomocí `az login` pro bezklíčovou autentizaci Entra ID.

## Alternativní poskytovatel: MiniMax (kompatibilní s OpenAI)

[MiniMax](https://platform.minimaxi.com/) nabízí modely s velkým kontextem (až 204K tokenů) přes OpenAI-kompatibilní API. Protože Microsoft Agent Framework `OpenAIChatClient` funguje s jakýmkoli OpenAI-kompatibilním endpointem, můžete MiniMax použít jako náhradu za Azure OpenAI nebo OpenAI.

Přidejte tyto proměnné do vašeho `.env` souboru:

| Proměnná | Kde ji najít |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platforma](https://platform.minimaxi.com/) → API klíče |
| `MINIMAX_BASE_URL` | Použijte `https://api.minimax.io/v1` (výchozí hodnota) |
| `MINIMAX_MODEL_ID` | Název modelu k použití (např. `MiniMax-M3`) |

**Příklad modelů**: `MiniMax-M3` (doporučeno), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (rychlejší odpovědi). Názvy modelů a dostupnost se mohou časem měnit a přístup k modelu může záviset na vašem účtu nebo regionu — zkontrolujte [MiniMax Platformu](https://platform.minimaxi.com/) pro aktuální seznam. Pokud `MiniMax-M3` není dostupný pro váš účet, nastavte `MINIMAX_MODEL_ID` na model, ke kterému máte přístup (např. `MiniMax-M2.7`).

Ukázky kódu používající `OpenAIChatClient` (např. Lekce 14 workflow rezervace hotelu) automaticky detekují a použijí vaši MiniMax konfiguraci, pokud je nastaven `MINIMAX_API_KEY`.

## Alternativní poskytovatel: Foundry Local (spuštění modelů přímo na zařízení)

[Foundry Local](https://foundrylocal.ai) je lehký runtime, který stahuje, spravuje a poskytuje jazykové modely **zcela na vašem vlastním počítači** přes OpenAI-kompatibilní API — žádný cloud, žádné Azure předplatné a žádné API klíče. Je to skvělá volba pro offline vývoj, experimentování bez nákladů na cloud nebo uchování dat lokálně.

Protože Microsoft Agent Framework `OpenAIChatClient` funguje s jakýmkoli OpenAI-kompatibilním endpointem, Foundry Local je plnohodnotná lokální alternativa k Azure OpenAI.

**1. Instalujte Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Stáhněte a spusťte model** (tím se také spustí lokální služba):

```bash
foundry model list          # podívejte se na dostupné modely
foundry model run phi-4-mini
```

**3. Nainstalujte Python SDK** používané k objevení lokálního endpointu:

```bash
pip install foundry-local-sdk
```

**4. Nasměrujte Microsoft Agent Framework na váš lokální model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Stáhne (pokud je potřeba) a poskytuje model lokálně, poté zjistí koncový bod/port.
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

> **Poznámka:** Foundry Local vystavuje OpenAI-kompatibilní endpoint **Chat Completions**. Použijte jej pro lokální vývoj a offline scénáře. Pro plnou funkcionalitu **Responses API** (stavové konverzace, hlubokou orchestrace nástrojů a vývoj stylu agentů) cílujte na **Azure OpenAI** nebo **Microsoft Foundry** projekt, jak je ukázáno v lekcích. Viz [dokumentaci Foundry Local](https://foundrylocal.ai) pro aktuální katalog modelů a podporu platformy.

## Dodatečné nastavení pro Lekci 8 (Bing Grounding Workflow)


V podmíněném pracovním postupu v lekci 8 se používá **Bing grounding** přes Microsoft Foundry. Pokud plánujete tento příklad spustit, přidejte tuto proměnnou do svého souboru `.env`:

| Proměnná | Kde ji najít |
|----------|--------------|
| `BING_CONNECTION_ID` | Portál Microsoft Foundry → váš projekt → **Management** → **Připojené zdroje** → vaše Bing připojení → zkopírujte ID připojení |

## Řešení problémů

### Chyby ověřování SSL certifikátu na macOS

Pokud používáte macOS a narazíte na chybu, jako je:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Jedná se o známý problém s Pythonem na macOS, kde systémové SSL certifikáty nejsou automaticky důvěryhodné. Vyzkoušejte následující řešení postupně:

**Možnost 1: Spusťte Python skript pro instalaci certifikátů (doporučeno)**

```bash
# Nahraďte 3.XX vaší nainstalovanou verzí Pythonu (např. 3.12 nebo 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnost 2: Použijte `connection_verify=False` ve svém notebooku (platí pouze pro notebooky GitHub Models)**

V notebooku Lekce 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je již zahrnuto zakomentované řešení. Odkomentujte `connection_verify=False` při vytváření klienta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Zakázat ověřování SSL, pokud narazíte na chyby certifikátu
)
```

> **⚠️ Upozornění:** Vypnutí ověřování SSL (`connection_verify=False`) snižuje bezpečnost přeskočením validace certifikátu. Používejte toto řešení pouze jako dočasné v testovacím prostředí, nikdy ne v produkci.

**Možnost 3: Nainstalujte a použijte `truststore`**

```bash
pip install truststore
```

Pak přidejte následující na začátek svého notebooku nebo skriptu před jakýmkoliv síťovým voláním:

```python
import truststore
truststore.inject_into_ssl()
```

## Někde se zasekáváte?

Pokud máte nějaké problémy s tímto nastavením, připojte se do naší <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> nebo <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">vytvořte issue</a>.

## Další lekce

Nyní jste připraveni spustit kód tohoto kurzu. Přejeme hodně úspěchů při dalším poznávání světa AI agentů!

[Úvod do AI agentů a případy jejich použití](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->