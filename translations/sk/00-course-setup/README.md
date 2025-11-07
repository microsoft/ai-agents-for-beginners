<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86273689a010b5efecaf7fa23104e0fb",
  "translation_date": "2025-11-07T08:47:00+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sk"
}
-->
# Nastavenie kurzu

## Úvod

Táto lekcia sa zaoberá tým, ako spustiť ukážky kódu tohto kurzu.

## Pripojte sa k ostatným študentom a získajte pomoc

Skôr než začnete klonovať svoje úložisko, pripojte sa k [Discord kanálu AI Agents For Beginners](https://aka.ms/ai-agents/discord), kde môžete získať pomoc s nastavením, odpovede na otázky o kurze alebo sa spojiť s ostatnými študentmi.

## Klonujte alebo forknite toto úložisko

Na začiatok prosím klonujte alebo forknite GitHub úložisko. Týmto si vytvoríte vlastnú verziu materiálov kurzu, aby ste mohli spúšťať, testovať a upravovať kód!

Toto môžete urobiť kliknutím na odkaz <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork úložiska</a>.

Teraz by ste mali mať svoju vlastnú forknutú verziu tohto kurzu na nasledujúcom odkaze:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.sk.png)

### Plytký klon (odporúča sa pre workshop / Codespaces)

  >Celé úložisko môže byť veľké (~3 GB), keď stiahnete celú históriu a všetky súbory. Ak sa zúčastňujete len workshopu alebo potrebujete len niekoľko priečinkov lekcií, plytký klon (alebo riedky klon) zabráni väčšine tohto sťahovania tým, že skráti históriu a/alebo preskočí bloby.

#### Rýchly plytký klon — minimálna história, všetky súbory

Nahraďte `<your-username>` v nasledujúcich príkazoch URL adresou vášho forku (alebo upstream URL, ak preferujete).

Na klonovanie len najnovšej histórie commitov (malé stiahnutie):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Na klonovanie konkrétnej vetvy:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Čiastočný (riedky) klon — minimálne bloby + len vybrané priečinky

Toto využíva čiastočný klon a sparse-checkout (vyžaduje Git 2.25+ a odporúča sa moderný Git s podporou čiastočného klonu):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Prejdite do priečinka úložiska:

```bash|powershell
cd ai-agents-for-beginners
```

Potom špecifikujte, ktoré priečinky chcete (príklad nižšie ukazuje dva priečinky):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonovaní a overení súborov, ak potrebujete len súbory a chcete uvoľniť miesto (bez histórie git), prosím odstráňte metadáta úložiska (💀nevratné — stratíte všetku funkčnosť Gitu: žiadne commity, pull, push alebo prístup k histórii).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Použitie GitHub Codespaces (odporúča sa na vyhnutie sa veľkým lokálnym stiahnutiam)

- Vytvorte nový Codespace pre toto úložisko cez [GitHub UI](https://github.com/codespaces).  

- V termináli novovytvoreného Codespace spustite jeden z príkazov na plytký/riedky klon vyššie, aby ste do pracovného priestoru Codespace priniesli len priečinky lekcií, ktoré potrebujete.
- Voliteľné: po klonovaní v Codespaces odstráňte .git na uvoľnenie miesta (pozrite si príkazy na odstránenie vyššie).
- Poznámka: Ak preferujete otvoriť úložisko priamo v Codespaces (bez extra klonu), buďte si vedomí, že Codespaces vytvorí prostredie devcontainer a môže stále poskytnúť viac, než potrebujete. Klonovanie plytkého kópie vo vnútri nového Codespace vám dáva väčšiu kontrolu nad využitím disku.

#### Tipy

- Vždy nahraďte URL adresu klonu vaším forkom, ak chcete upravovať/commitovať.
- Ak neskôr potrebujete viac histórie alebo súborov, môžete ich stiahnuť alebo upraviť sparse-checkout na zahrnutie ďalších priečinkov.

## Spúšťanie kódu

Tento kurz ponúka sériu Jupyter Notebookov, ktoré môžete spustiť, aby ste získali praktické skúsenosti s budovaním AI agentov.

Ukážky kódu používajú buď:

**Vyžaduje GitHub účet - zdarma**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Označené ako (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Označené ako (autogen.ipynb)

**Vyžaduje predplatné Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Označené ako (azureaiagent.ipynb)

Odporúčame vám vyskúšať všetky tri typy príkladov, aby ste zistili, ktorý vám najviac vyhovuje.

Ktorúkoľvek možnosť si vyberiete, určí, ktoré kroky nastavenia musíte dodržať nižšie:

## Požiadavky

- Python 3.12+
  - **NOTE**: Ak nemáte nainštalovaný Python3.12, uistite sa, že ho nainštalujete. Potom vytvorte svoj venv pomocou python3.12, aby ste zabezpečili správne verzie nainštalované zo súboru requirements.txt.
  
    >Príklad

    Vytvorte adresár Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    Potom aktivujte prostredie venv pre:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Pre ukážky kódu používajúce .NET, uistite sa, že ste nainštalovali [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) alebo novší. Potom skontrolujte verziu nainštalovaného .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- GitHub účet - Pre prístup k GitHub Models Marketplace
- Predplatné Azure - Pre prístup k Azure AI Foundry
- Účet Azure AI Foundry - Pre prístup k Azure AI Agent Service

V koreňovom adresári tohto úložiska sme zahrnuli súbor `requirements.txt`, ktorý obsahuje všetky potrebné Python balíčky na spustenie ukážok kódu.

Môžete ich nainštalovať spustením nasledujúceho príkazu vo vašom termináli v koreňovom adresári úložiska:

```bash|powershell
pip install -r requirements.txt
```

Odporúčame vytvoriť Python virtuálne prostredie, aby ste sa vyhli akýmkoľvek konfliktom a problémom.

## Nastavenie VSCode

Uistite sa, že používate správnu verziu Pythonu vo VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavenie pre ukážky používajúce GitHub Models 

### Krok 1: Získajte svoj GitHub Personal Access Token (PAT)

Tento kurz využíva GitHub Models Marketplace, ktorý poskytuje bezplatný prístup k veľkým jazykovým modelom (LLMs), ktoré budete používať na budovanie AI agentov.

Na použitie GitHub Models budete musieť vytvoriť [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Toto môžete urobiť tak, že prejdete na <a href="https://github.com/settings/personal-access-tokens" target="_blank">nastavenia Personal Access Tokens</a> vo vašom GitHub účte.

Prosím, dodržujte [Princíp minimálnych oprávnení](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) pri vytváraní vášho tokenu. To znamená, že by ste mali tokenu poskytnúť len tie oprávnenia, ktoré potrebuje na spustenie ukážok kódu v tomto kurze.

1. Vyberte možnosť `Fine-grained tokens` na ľavej strane obrazovky prechodom na **Developer settings**.

   ![Developer settings](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.sk.png)

   Potom vyberte `Generate new token`.

   ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.sk.png)

2. Zadajte popisný názov pre váš token, ktorý odráža jeho účel, aby ste ho neskôr ľahko identifikovali.

    🔐 Odporúčanie pre trvanie tokenu

    Odporúčané trvanie: 30 dní
    Pre bezpečnejší prístup môžete zvoliť kratšie obdobie — napríklad 7 dní 🛡️
    Je to skvelý spôsob, ako si stanoviť osobný cieľ a dokončiť kurz, kým je vaša motivácia vysoká 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.sk.png)

3. Obmedzte rozsah tokenu na váš fork tohto úložiska.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.sk.png)

4. Obmedzte oprávnenia tokenu: Pod **Permissions**, kliknite na záložku **Account** a kliknite na tlačidlo "+ Add permissions". Zobrazí sa rozbaľovacie menu. Prosím, vyhľadajte **Models** a zaškrtnite políčko.

    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.sk.png)

5. Pred generovaním tokenu overte požadované oprávnenia. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.sk.png)

6. Pred generovaním tokenu sa uistite, že ste pripravení uložiť token na bezpečné miesto, ako je trezor na heslá, pretože po jeho vytvorení ho už nebudete môcť zobraziť. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.sk.png)

Skopírujte svoj nový token, ktorý ste práve vytvorili. Teraz ho pridáte do svojho súboru `.env`, ktorý je súčasťou tohto kurzu.

### Krok 2: Vytvorte svoj `.env` súbor

Na vytvorenie súboru `.env` spustite nasledujúci príkaz vo vašom termináli.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Týmto skopírujete príklad súboru a vytvoríte `.env` vo vašom adresári, kde vyplníte hodnoty pre environmentálne premenné.

S vaším skopírovaným tokenom otvorte súbor `.env` vo vašom obľúbenom textovom editore a vložte váš token do poľa `GITHUB_TOKEN`.

![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.sk.png)

Teraz by ste mali byť schopní spustiť ukážky kódu tohto kurzu.

## Nastavenie pre ukážky používajúce Azure AI Foundry a Azure AI Agent Service

### Krok 1: Získajte svoj Azure Project Endpoint

Postupujte podľa krokov na vytvorenie hubu a projektu v Azure AI Foundry, ktoré nájdete tu: [Prehľad hubových zdrojov](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)

Keď vytvoríte svoj projekt, budete musieť získať reťazec pripojenia pre váš projekt.

Toto môžete urobiť tak, že prejdete na stránku **Prehľad** vášho projektu v portáli Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.sk.png)

### Krok 2: Vytvorte svoj `.env` súbor

Na vytvorenie súboru `.env` spustite nasledujúci príkaz vo vašom termináli.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Týmto skopírujete príklad súboru a vytvoríte `.env` vo vašom adresári, kde vyplníte hodnoty pre environmentálne premenné.

S vaším skopírovaným tokenom otvorte súbor `.env` vo vašom obľúbenom textovom editore a vložte váš token do poľa `PROJECT_ENDPOINT`.

### Krok 3: Prihláste sa do Azure

Ako bezpečnostnú najlepšiu prax použijeme [autentifikáciu bez kľúča](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) na autentifikáciu do Azure OpenAI pomocou Microsoft Entra ID. 

Ďalej otvorte terminál a spustite `az login --use-device-code`, aby ste sa prihlásili do svojho Azure účtu.

Po prihlásení vyberte svoje predplatné v termináli.

## Dodatočné environmentálne premenné - Azure Search a Azure OpenAI 

Pre lekciu Agentic RAG - Lekcia 5 - existujú ukážky, ktoré používajú Azure Search a Azure OpenAI.

Ak chcete spustiť tieto ukážky, budete musieť pridať nasledujúce environmentálne premenné do svojho súboru `.env`:

### Stránka Prehľad (Projekt)

- `AZURE_SUBSCRIPTION_ID` - Skontrolujte **Detaily projektu** na stránke **Prehľad** vášho projektu.

- `AZURE_AI_PROJECT_NAME` - Pozrite sa na vrch stránky **Prehľad** vášho projektu.

- `AZURE_OPENAI_SERVICE` - Nájdite to na karte **Zahrnuté schopnosti** pre **Azure OpenAI Service** na stránke **Prehľad**.

### Centrum správy

- `AZURE_OPENAI_RESOURCE_GROUP` - Prejdite na **Vlastnosti projektu** na stránke **Prehľad** v **Centrum správy**.

- `GLOBAL_LLM_SERVICE` - Pod **Pripojené zdroje**, nájdite názov pripojenia **Azure AI Services**. Ak nie je uvedený, skontrolujte **Azure portál** pod vašou skupinou zdrojov pre názov zdroja AI Services.

### Stránka Modely + koncové body

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Vyberte svoj embedding model (napr. `text-embedding-ada-002`) a poznačte si **Názov nasadenia** z detailov modelu.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Vyberte svoj chat model (napr. `gpt-4o-mini`) a poznačte si **Názov nasadenia** z detailov modelu.

### Azure portál

- `AZURE_OPENAI_ENDPOINT` - Nájdite **Azure AI services**, kliknite na to, potom prejdite na **Správa zdrojov**, **Kľúče a koncové body**, posuňte sa dole na "Azure OpenAI endpoints" a skopírujte ten, ktorý hovorí "Language APIs".

- `AZURE_OPENAI_API_KEY` - Z tej istej obrazovky skopírujte KĽÚČ 1 alebo KĽÚČ 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Nájdite svoj **Azure AI Search** zdroj, kliknite naň a pozrite si **Prehľad**.

- `AZURE_SEARCH_API_KEY` - Potom prejdite na **Nastavenia** a potom **Kľúče**, aby ste skopírovali primárny alebo sekundárny administrátorský kľúč.

### Externá webová stránka

- `AZURE_OPENAI_API_VERSION` - Navštívte stránku [Životný cyklus verzie API](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) pod **Najnovšie GA API vydanie**.

### Nastavenie autentifikácie bez kľúča

Namiesto pevného kódovania vašich poverení použijeme pripojenie bez kľúča s Azure OpenAI. Na to importujeme `DefaultAzureCredential` a neskôr zavoláme funkciu `DefaultAzureCredential`, aby sme získali poverenie.

```python
# Python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Zasekli ste sa niekde?
Ak máte akékoľvek problémy s týmto nastavením, pripojte sa do nášho <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> alebo <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">vytvorte problém</a>.

## Ďalšia lekcia

Teraz ste pripravení spustiť kód pre tento kurz. Prajeme vám veľa zábavy pri objavovaní sveta AI agentov!

[Úvod do AI agentov a ich využitia](../01-intro-to-ai-agents/README.md)

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.