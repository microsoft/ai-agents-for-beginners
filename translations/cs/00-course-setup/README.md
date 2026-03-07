# Course Setup

## Introduction

Tato lekce vysvětlí, jak spustit ukázkové kódy z tohoto kurzu.

## Join Other Learners and Get Help

Než začnete klonovat svůj repozitář, připojte se k [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord), kde můžete získat pomoc s nastavením, zeptat se na cokoliv ohledně kurzu nebo se spojit s ostatními studenty.

## Clone or Fork this Repo

Pro začátek prosím naklonujte nebo vytvořte fork repozitáře na GitHubu. Tím získáte vlastní verzi materiálů kurzu, abyste mohli kód spouštět, testovat a upravovat!

To lze provést kliknutím na odkaz <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">vytvořit fork repozitáře</a>

Nyní byste měli mít vlastní forkovanou verzi tohoto kurzu na následujícím odkazu:

![Forked Repo](../../../translated_images/cs/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (recommended for workshop / Codespaces)

  >Plné úložiště může být při stažení celé historie a všech souborů velké (~3 GB). Pokud se účastníte pouze workshopu nebo potřebujete jen několik složek s lekcemi, shallow clone (nebo sparse clone) vám ušetří většinu stahování zkrácením historie a/nebo přeskočením blobů.

#### Quick shallow clone — minimal history, all files

Nahraďte `<your-username>` v následujících příkazech URL svého forku (nebo upstream URL, pokud dáváte přednost tomu).

Pro naklonování pouze posledního commitu (malé stahování):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pro naklonování konkrétní větve:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal blobs + only selected folders

To využívá partial clone a sparse-checkout (vyžaduje Git 2.25+ a doporučujeme moderní Git s podporou partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Přejděte do složky repozitáře:

```bash|powershell
cd ai-agents-for-beginners
```

Poté určete, které složky chcete (příklad níže ukazuje dvě složky):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonování a ověření souborů, pokud potřebujete jen soubory a chcete uvolnit místo (bez historie git), smažte metadata repozitáře (💀nevratné — ztratíte veškerou funkcionalitu Gitu: žádné commity, pull, push ani přístup k historii).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Using GitHub Codespaces (recommended to avoid local large downloads)

- Vytvořte nový Codespace pro tento repozitář přes [GitHub UI](https://github.com/codespaces).  

- V terminálu nově vytvořeného Codespace spusťte jeden z výše uvedených shallow/sparse clone příkazů, aby se do pracovního prostoru Codespace dostaly jen potřebné složky s lekcemi.
- Volitelné: po klonování uvnitř Codespaces odstraňte .git, abyste uvolnili místo (viz příkazy pro odstranění výše).
- Poznámka: Pokud dáte přednost otevření repozitáře přímo v Codespaces (bez extra klonování), mějte na paměti, že Codespaces vytvoří devcontainer prostředí a může stále poskytnout více, než potřebujete. Naklonování shallow kopie uvnitř čerstvého Codespace vám dává lepší kontrolu nad využitím disku.

#### Tips

- Vždy nahraďte URL klonování URL svého forku, pokud chcete upravovat/commitovat.
- Pokud budete později potřebovat více historie nebo souborů, můžete je stáhnout nebo upravit sparse-checkout tak, aby zahrnoval další složky.

## Running the Code

Tento kurz nabízí řadu Jupyter notebooků, které můžete spustit, abyste získali praktickou zkušenost s vytvářením AI agentů.

Ukázkové kódy používají **Microsoft Agent Framework (MAF)** s `AzureAIProjectAgentProvider`, který se připojuje k **Azure AI Agent Service V2** (Responses API) přes **Microsoft Foundry**.

Všechny Python notebooky jsou označeny `*-python-agent-framework.ipynb`.

## Requirements

- Python 3.12+
  - **POZNÁMKA**: Pokud nemáte nainstalovaný Python3.12, nainstalujte ho. Poté vytvořte své virtuální prostředí pomocí python3.12, aby se nainstalovaly správné verze z requirements.txt.
  
    >Příklad

    Vytvořte adresář pro Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    Poté aktivujte virtuální prostředí pro:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Pro ukázkové kódy používající .NET si nainstalujte [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) nebo novější. Poté zkontrolujte verzi nainstalovaného .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Vyžadováno pro autentizaci. Nainstalujte z [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Pro přístup k Microsoft Foundry a Azure AI Agent Service.
- **Microsoft Foundry Project** — Projekt s nasazeným modelem (např. `gpt-4o`). Viz [Krok 1](../../../00-course-setup) níže.

V kořenovém adresáři tohoto repozitáře je soubor `requirements.txt`, který obsahuje všechny potřebné Python balíčky pro spuštění ukázkových kódů.

Nainstalujete je spuštěním následujícího příkazu v terminálu v kořeni repozitáře:

```bash|powershell
pip install -r requirements.txt
```

Doporučujeme vytvořit Python virtuální prostředí, abyste se vyhnuli konfliktům a problémům.

## Setup VSCode

Ujistěte se, že ve VSCode používáte správnou verzi Pythonu.

![obrázek](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Set Up Microsoft Foundry and Azure AI Agent Service

### Step 1: Create a Microsoft Foundry Project

Potřebujete hub a projekt v Azure AI Foundry s nasazeným modelem, abyste mohli spouštět notebooky.

1. Přejděte na [ai.azure.com](https://ai.azure.com) a přihlaste se svým Azure účtem.
2. Vytvořte **hub** (nebo použijte existující). Viz: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. V rámci hubu vytvořte **project**.
4. Nasadťe model (např. `gpt-4o`) přes **Models + Endpoints** → **Deploy model**.

### Step 2: Retrieve Your Project Endpoint and Model Deployment Name

Z vašeho projektu v portálu Microsoft Foundry:

- **Project Endpoint** — Přejděte na stránku **Overview** a zkopírujte URL endpointu.

![Připojovací řetězec projektu](../../../translated_images/cs/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Přejděte na **Models + Endpoints**, vyberte nasazený model a poznamenjte si **Deployment name** (např. `gpt-4o`).

### Step 3: Sign in to Azure with `az login`

Všechny notebooky používají pro autentizaci **`AzureCliCredential`** — není potřeba spravovat API klíče. To vyžaduje, abyste byli přihlášeni přes Azure CLI.

1. **Nainstalujte Azure CLI**, pokud jste tak ještě neučinili: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Přihlaste se** spuštěním:

    ```bash|powershell
    az login
    ```

    Nebo pokud jste v remote/Codespace prostředí bez prohlížeče:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vyberte svůj subscription**, pokud budete vyzváni — zvolte ten, který obsahuje váš Foundry projekt.

4. **Ověřte**, že jste přihlášeni:

    ```bash|powershell
    az account show
    ```

> **Proč `az login`?** Notebooky se autentizují pomocí `AzureCliCredential` z balíčku `azure-identity`. To znamená, že vaše relace v Azure CLI poskytuje pověření — žádné API klíče nebo tajné údaje v souboru `.env`. Toto je [bezpečnostní doporučení](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Step 4: Create Your `.env` File

Zkopírujte ukázkový soubor:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Otevřete `.env` a doplňte tyto dvě hodnoty:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portál Foundry → váš projekt → stránka **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portál Foundry → **Models + Endpoints** → název vašeho nasazeného modelu |

To je vše pro většinu lekcí! Notebooky se budou autentizovat automaticky pomocí vaší relace `az login`.

### Step 5: Install Python Dependencies

```bash|powershell
pip install -r requirements.txt
```

Doporučujeme spouštět tento příkaz uvnitř virtuálního prostředí, které jste vytvořili dříve.

## Additional Setup for Lesson 5 (Agentic RAG)

Lekce 5 používá **Azure AI Search** pro retrieval-augmented generation. Pokud plánujete spouštět tuto lekci, přidejte do svého `.env` souboru tyto proměnné:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → vaše **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → vaše **Azure AI Search** resource → **Settings** → **Keys** → primární admin klíč |

## Additional Setup for Lesson 6 and Lesson 8 (GitHub Models)

Některé notebooky v lekcích 6 a 8 používají místo Azure AI Foundry **GitHub Models**. Pokud plánujete spouštět tyto ukázky, přidejte do svého `.env` souboru tyto proměnné:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Použijte `https://models.inference.ai.azure.com` (výchozí hodnota) |
| `GITHUB_MODEL_ID` | Název modelu k použití (např. `gpt-4o-mini`) |

## Additional Setup for Lesson 8 (Bing Grounding Workflow)

Podmíněný workflow notebook v lekci 8 používá **Bing grounding** přes Azure AI Foundry. Pokud plánujete spouštět tento příklad, přidejte do svého `.env` souboru tuto proměnnou:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portál Azure AI Foundry → váš projekt → **Management** → **Connected resources** → vaše Bing připojení → zkopírujte connection ID |

## Troubleshooting

### SSL Certificate Verification Errors on macOS

Pokud používáte macOS a narazíte na chybu podobnou:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Toto je známý problém s Pythonem na macOS, kde systémové SSL certifikáty nejsou automaticky důvěryhodné. Vyzkoušejte následující řešení v uvedeném pořadí:

**Option 1: Run Python's Install Certificates script (recommended)**

```bash
# Nahraďte 3.XX verzí Pythonu, kterou máte nainstalovanou (např. 3.12 nebo 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Option 2: Use `connection_verify=False` in your notebook (for GitHub Models notebooks only)**

V notebooku z Lekce 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je již zahrnuto řešení jako zakomentovaný workaround. Odkomentujte `connection_verify=False` při vytváření klienta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Vypněte ověřování SSL, pokud narazíte na chyby certifikátu
)
```

> **⚠️ Upozornění:** Vypnutí ověřování SSL (`connection_verify=False`) snižuje bezpečnost tím, že přeskočí validaci certifikátů. Používejte to pouze jako dočasné řešení ve vývojovém prostředí, nikdy v produkci.

**Option 3: Install and use `truststore`**

```bash
pip install truststore
```

Poté přidejte následující na začátek svého notebooku nebo skriptu před provedením jakýchkoli síťových volání:

```python
import truststore
truststore.inject_into_ssl()
```

## Stuck Somewhere?

Pokud budete mít nějaké problémy s tímto nastavením, připojte se na náš <a href="https://discord.gg/kzRShWzttr" target="_blank">komunitní Discord Azure AI</a> nebo <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">vytvořte issue</a>.

## Next Lesson

Nyní jste připraveni spustit kód pro tento kurz. Přejeme hodně zábavy při dalším objevování světa AI agentů! 

[Úvod do AI agentů a jejich použití](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vyloučení odpovědnosti:
Tento dokument byl přeložen pomocí služby pro automatický překlad založené na umělé inteligenci Co-op Translator (https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj je považován originální dokument v jeho původním jazyce. Pro zásadní informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za žádná nedorozumění nebo chybné výklady vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->