<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86273689a010b5efecaf7fa23104e0fb",
  "translation_date": "2025-11-07T08:46:24+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "cs"
}
-->
# Nastavení kurzu

## Úvod

Tato lekce se zaměřuje na spuštění ukázkového kódu tohoto kurzu.

## Připojte se k ostatním studentům a získejte pomoc

Než začnete klonovat svůj repozitář, připojte se na [Discord kanál AI Agents For Beginners](https://aka.ms/ai-agents/discord), kde můžete získat pomoc s nastavením, odpovědi na otázky ohledně kurzu nebo se spojit s ostatními studenty.

## Klonování nebo forkování tohoto repozitáře

Začněte klonováním nebo forkováním GitHub repozitáře. Tím si vytvoříte vlastní verzi materiálů kurzu, abyste mohli spouštět, testovat a upravovat kód!

To můžete udělat kliknutím na odkaz <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repozitáře</a>.

Nyní byste měli mít svou vlastní forkovanou verzi tohoto kurzu na následujícím odkazu:

![Forkovaný repozitář](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.cs.png)

### Shallow Clone (doporučeno pro workshop / Codespaces)

  >Celý repozitář může být velký (~3 GB), pokud stáhnete celou historii a všechny soubory. Pokud se účastníte pouze workshopu nebo potřebujete jen několik složek z lekcí, shallow clone (nebo sparse clone) vám umožní vyhnout se většině tohoto stahování tím, že zkrátí historii a/nebo přeskočí některé soubory.

#### Rychlé shallow clone — minimální historie, všechny soubory

Nahraďte `<your-username>` v níže uvedených příkazech URL vašeho forku (nebo upstream URL, pokud preferujete).

Pro klonování pouze nejnovější historie commitů (malé stahování):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pro klonování konkrétní větve:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Částečné (sparse) klonování — minimální soubory + pouze vybrané složky

Toto využívá částečné klonování a sparse-checkout (vyžaduje Git 2.25+ a doporučuje se moderní Git s podporou částečného klonování):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Přejděte do složky repozitáře:

```bash|powershell
cd ai-agents-for-beginners
```

Poté specifikujte, které složky chcete (příklad níže ukazuje dvě složky):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonování a ověření souborů, pokud potřebujete pouze soubory a chcete uvolnit místo (bez historie git), smažte metadata repozitáře (💀nevratné — ztratíte veškerou funkčnost Git: žádné commity, pull, push nebo přístup k historii).

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

- V terminálu nově vytvořeného Codespace spusťte jeden z příkazů pro shallow/sparse klonování výše, abyste přinesli pouze složky lekcí, které potřebujete, do workspace Codespace.
- Volitelné: po klonování uvnitř Codespaces odstraňte .git pro uvolnění místa (viz příkazy pro odstranění výše).
- Poznámka: Pokud preferujete otevřít repozitář přímo v Codespaces (bez dalšího klonování), mějte na paměti, že Codespaces vytvoří prostředí devcontainer a může stále zahrnovat více, než potřebujete. Klonování shallow kopie uvnitř nového Codespace vám dává větší kontrolu nad využitím disku.

#### Tipy

- Vždy nahraďte URL klonování URL vašeho forku, pokud chcete upravovat/commitovat.
- Pokud později potřebujete více historie nebo souborů, můžete je stáhnout nebo upravit sparse-checkout pro zahrnutí dalších složek.

## Spuštění kódu

Tento kurz nabízí sérii Jupyter Notebooků, které můžete spustit, abyste získali praktické zkušenosti s budováním AI Agentů.

Ukázky kódu používají buď:

**Vyžaduje GitHub účet - zdarma**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Označeno jako (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Označeno jako (autogen.ipynb)

**Vyžaduje Azure předplatné**:
3) Azure AI Foundry + Azure AI Agent Service. Označeno jako (azureaiagent.ipynb)

Doporučujeme vyzkoušet všechny tři typy příkladů, abyste zjistili, který vám nejlépe vyhovuje.

Kteroukoliv možnost si vyberete, určí, které kroky nastavení budete muset následovat níže:

## Požadavky

- Python 3.12+
  - **POZNÁMKA**: Pokud nemáte nainstalovaný Python 3.12, ujistěte se, že jej nainstalujete. Poté vytvořte svůj venv pomocí python3.12, abyste zajistili správné verze instalované z requirements.txt souboru.
  
    >Příklad

    Vytvořte adresář Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    Poté aktivujte prostředí venv:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Pro ukázkový kód využívající .NET, ujistěte se, že máte nainstalovaný [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) nebo novější. Poté zkontrolujte verzi nainstalovaného .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- GitHub účet - Pro přístup k GitHub Models Marketplace
- Azure předplatné - Pro přístup k Azure AI Foundry
- Azure AI Foundry účet - Pro přístup k Azure AI Agent Service

V kořenovém adresáři tohoto repozitáře jsme zahrnuli soubor `requirements.txt`, který obsahuje všechny požadované Python balíčky pro spuštění ukázkového kódu.

Můžete je nainstalovat spuštěním následujícího příkazu ve vašem terminálu v kořenovém adresáři repozitáře:

```bash|powershell
pip install -r requirements.txt
```

Doporučujeme vytvořit Python virtuální prostředí, abyste se vyhnuli konfliktům a problémům.

## Nastavení VSCode

Ujistěte se, že používáte správnou verzi Pythonu ve VSCode.

![obrázek](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavení pro ukázky využívající GitHub Models 

### Krok 1: Získání vašeho GitHub Personal Access Token (PAT)

Tento kurz využívá GitHub Models Marketplace, který poskytuje bezplatný přístup k modelům velkých jazykových modelů (LLMs), které budete používat k budování AI Agentů.

Pro použití GitHub Models budete muset vytvořit [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

To lze provést přechodem na <a href="https://github.com/settings/personal-access-tokens" target="_blank">nastavení Personal Access Tokens</a> ve vašem GitHub účtu.

Postupujte podle [Principu minimálních oprávnění](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) při vytváření tokenu. To znamená, že byste měli tokenu dát pouze oprávnění, která potřebuje ke spuštění ukázkového kódu v tomto kurzu.

1. Na levé straně obrazovky vyberte možnost `Fine-grained tokens` přechodem do **Developer settings**.

   ![Developer settings](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.cs.png)

   Poté vyberte `Generate new token`.

   ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.cs.png)

2. Zadejte popisný název pro váš token, který odráží jeho účel, aby bylo snadné jej později identifikovat.

    🔐 Doporučení pro trvání tokenu

    Doporučené trvání: 30 dní
    Pro větší bezpečnost můžete zvolit kratší období—například 7 dní 🛡️
    Je to skvělý způsob, jak si nastavit osobní cíl a dokončit kurz, zatímco vaše učební motivace je vysoká 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.cs.png)

3. Omezte rozsah tokenu na váš fork tohoto repozitáře.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.cs.png)

4. Omezte oprávnění tokenu: V sekci **Permissions** klikněte na záložku **Account** a poté na tlačítko "+ Add permissions". Zobrazí se rozbalovací nabídka. Vyhledejte **Models** a zaškrtněte políčko.

    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.cs.png)

5. Ověřte požadovaná oprávnění před vytvořením tokenu. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.cs.png)

6. Před vytvořením tokenu se ujistěte, že jste připraveni uložit token na bezpečné místo, například do trezoru správce hesel, protože po jeho vytvoření již nebude zobrazen. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.cs.png)

Zkopírujte svůj nový token, který jste právě vytvořili. Nyní jej přidáte do svého `.env` souboru zahrnutého v tomto kurzu.

### Krok 2: Vytvoření `.env` souboru

Pro vytvoření `.env` souboru spusťte následující příkaz ve vašem terminálu.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Tím zkopírujete příkladový soubor a vytvoříte `.env` ve vašem adresáři, kde vyplníte hodnoty pro proměnné prostředí.

S vaším zkopírovaným tokenem otevřete `.env` soubor ve vašem oblíbeném textovém editoru a vložte váš token do pole `GITHUB_TOKEN`.

![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.cs.png)

Nyní byste měli být schopni spustit ukázkový kód tohoto kurzu.

## Nastavení pro ukázky využívající Azure AI Foundry a Azure AI Agent Service

### Krok 1: Získání vašeho Azure Project Endpoint

Postupujte podle kroků pro vytvoření hubu a projektu v Azure AI Foundry, které najdete zde: [Přehled zdrojů hubu](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)

Jakmile vytvoříte svůj projekt, budete muset získat připojovací řetězec pro váš projekt.

To lze provést přechodem na stránku **Overview** vašeho projektu v portálu Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.cs.png)

### Krok 2: Vytvoření `.env` souboru

Pro vytvoření `.env` souboru spusťte následující příkaz ve vašem terminálu.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Tím zkopírujete příkladový soubor a vytvoříte `.env` ve vašem adresáři, kde vyplníte hodnoty pro proměnné prostředí.

S vaším zkopírovaným tokenem otevřete `.env` soubor ve vašem oblíbeném textovém editoru a vložte váš token do pole `PROJECT_ENDPOINT`.

### Krok 3: Přihlášení do Azure

Jako bezpečnostní nejlepší praxi použijeme [autentizaci bez klíče](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) pro autentizaci do Azure OpenAI pomocí Microsoft Entra ID. 

Dále otevřete terminál a spusťte `az login --use-device-code` pro přihlášení do vašeho Azure účtu.

Jakmile se přihlásíte, vyberte vaše předplatné v terminálu.

## Další proměnné prostředí - Azure Search a Azure OpenAI 

Pro lekci Agentic RAG - Lekce 5 - jsou zde ukázky, které využívají Azure Search a Azure OpenAI.

Pokud chcete spustit tyto ukázky, budete muset přidat následující proměnné prostředí do vašeho `.env` souboru:

### Stránka přehledu (Projekt)

- `AZURE_SUBSCRIPTION_ID` - Zkontrolujte **Project details** na stránce **Overview** vašeho projektu.

- `AZURE_AI_PROJECT_NAME` - Podívejte se na vrchol stránky **Overview** vašeho projektu.

- `AZURE_OPENAI_SERVICE` - Najděte to na záložce **Included capabilities** pro **Azure OpenAI Service** na stránce **Overview**.

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - Přejděte na **Project properties** na stránce **Overview** v **Management Center**.

- `GLOBAL_LLM_SERVICE` - Pod **Connected resources**, najděte název připojení **Azure AI Services**. Pokud není uveden, zkontrolujte **Azure portal** pod vaší skupinou zdrojů pro název zdroje AI Services.

### Stránka Models + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Vyberte svůj embedding model (např. `text-embedding-ada-002`) a poznamenejte si **Deployment name** z detailů modelu.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Vyberte svůj chat model (např. `gpt-4o-mini`) a poznamenejte si **Deployment name** z detailů modelu.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Najděte **Azure AI services**, klikněte na něj, poté přejděte na **Resource Management**, **Keys and Endpoint**, sjeďte dolů na "Azure OpenAI endpoints" a zkopírujte ten, který říká "Language APIs".

- `AZURE_OPENAI_API_KEY` - Ze stejné obrazovky zkopírujte KEY 1 nebo KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Najděte svůj **Azure AI Search** zdroj, klikněte na něj a podívejte se na **Overview**.

- `AZURE_SEARCH_API_KEY` - Poté přejděte na **Settings** a poté **Keys**, abyste zkopírovali primární nebo sekundární administrátorský klíč.

### Externí webová stránka

- `AZURE_OPENAI_API_VERSION` - Navštivte stránku [API version lifecycle](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) pod **Latest GA API release**.

### Nastavení autentizace bez klíče

Místo hardcodování vašich přihlašovacích údajů použijeme připojení bez klíče s Azure OpenAI. K tomu importujeme `DefaultAzureCredential` a později zavoláme funkci `DefaultAzureCredential` pro získání přihlašovacích údajů.

```python
# Python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Zasekli jste se někde?
Pokud máte jakékoli problémy s tímto nastavením, připojte se do našeho <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> nebo <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">vytvořte problém</a>.

## Další lekce

Nyní jste připraveni spustit kód pro tento kurz. Přejeme vám příjemné učení o světě AI agentů!

[Úvod do AI agentů a jejich využití](../01-intro-to-ai-agents/README.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.