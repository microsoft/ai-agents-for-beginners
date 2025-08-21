<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "76945069b52a49cd0432ae3e0b0ba22e",
  "translation_date": "2025-07-12T07:56:30+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sk"
}
-->
Teraz by ste mali mať svoju vlastnú verziu tohto kurzu, ktorú ste si vytvorili pomocou forku, na nasledujúcom odkaze:

![Forknutý repozitár](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.sk.png)

## Spúšťanie kódu

Tento kurz ponúka sériu Jupyter Notebookov, ktoré môžete spustiť, aby ste získali praktické skúsenosti s budovaním AI agentov.

Ukážky kódu používajú buď:

**Vyžaduje GitHub účet - zadarmo**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Označené ako (semantic-kernel.ipynb)  
2) AutoGen Framework + GitHub Models Marketplace. Označené ako (autogen.ipynb)  

**Vyžaduje Azure predplatné**:  
3) Azure AI Foundry + Azure AI Agent Service. Označené ako (azureaiagent.ipynb)  

Odporúčame vám vyskúšať všetky tri typy príkladov, aby ste zistili, ktorý vám najviac vyhovuje.

Podľa toho, ktorú možnosť si vyberiete, budete musieť postupovať podľa príslušných krokov nastavenia uvedených nižšie:

## Požiadavky

- Python 3.12+  
  - **POZNÁMKA**: Ak nemáte nainštalovaný Python 3.12, uistite sa, že ho nainštalujete. Potom vytvorte svoje virtuálne prostredie pomocou python3.12, aby sa nainštalovali správne verzie z requirements.txt súboru.  
- GitHub účet - pre prístup k GitHub Models Marketplace  
- Azure predplatné - pre prístup k Azure AI Foundry  
- Azure AI Foundry účet - pre prístup k Azure AI Agent Service  

V koreňovom adresári tohto repozitára sme zahrnuli súbor `requirements.txt`, ktorý obsahuje všetky potrebné Python balíčky na spustenie ukážok kódu.

Nainštalujete ich spustením nasledujúceho príkazu v termináli v koreňovom adresári repozitára:

```bash
pip install -r requirements.txt
```  
Odporúčame vytvoriť Python virtuálne prostredie, aby ste sa vyhli konfliktom a problémom.

## Nastavenie VSCode
Uistite sa, že používate správnu verziu Pythonu vo VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavenie pre ukážky používajúce GitHub Models

### Krok 1: Získajte svoj GitHub Personal Access Token (PAT)

V súčasnosti tento kurz používa GitHub Models Marketplace na bezplatný prístup k veľkým jazykovým modelom (LLM), ktoré sa používajú na tvorbu AI agentov.

Toto môžete urobiť vo svojom GitHub účte.

To urobíte tak, že sa prihlásite do svojho GitHub účtu.

1. Na ľavej strane obrazovky vyberte možnosť `Fine-grained tokens`.

    Potom vyberte `Generate new token`.

![Generate Token](../../../translated_images/generate-token.9748d7585dd004cb4119b5aac724baff49c3a85791701b5e8ba3274b037c5b66.sk.png)

Budete vyzvaní zadať názov tokenu, vybrať dátum vypršania platnosti (odporúčané: 30 dní) a vybrať rozsahy oprávnení pre token (verejné repozitáre).

Je tiež potrebné upraviť povolenia tohto tokenu: Permissions -> Models -> Umožniť prístup k GitHub Models

Skopírujte si nový token, ktorý ste práve vytvorili. Teraz ho pridáte do súboru `.env`, ktorý je súčasťou tohto kurzu.

### Krok 2: Vytvorte svoj `.env` súbor

Na vytvorenie súboru `.env` spustite v termináli nasledujúci príkaz:

```bash
cp .env.example .env
```

Tým sa skopíruje príkladový súbor a vytvorí sa `.env` vo vašom adresári, kde vyplníte hodnoty pre premenné prostredia.

So skopírovaným tokenom otvorte `.env` súbor vo svojom obľúbenom textovom editore a vložte svoj token do poľa `GITHUB_TOKEN`.

Teraz by ste mali byť schopní spustiť ukážky kódu z tohto kurzu.

## Nastavenie pre ukážky používajúce Azure AI Foundry a Azure AI Agent Service

### Krok 1: Získajte svoj Azure Project Endpoint

Postupujte podľa krokov na vytvorenie hubu a projektu v Azure AI Foundry, ktoré nájdete tu: [Prehľad hub zdrojov](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Keď vytvoríte svoj projekt, budete musieť získať reťazec pripojenia pre váš projekt.

Toto môžete urobiť na stránke **Overview** vášho projektu v Azure AI Foundry portáli.

![Reťazec pripojenia projektu](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.sk.png)

### Krok 2: Vytvorte svoj `.env` súbor

Na vytvorenie súboru `.env` spustite v termináli nasledujúci príkaz:

```bash
cp .env.example .env
```

Tým sa skopíruje príkladový súbor a vytvorí sa `.env` vo vašom adresári, kde vyplníte hodnoty pre premenné prostredia.

So skopírovaným tokenom otvorte `.env` súbor vo svojom obľúbenom textovom editore a vložte svoj token do poľa `PROJECT_ENDPOINT`.

### Krok 3: Prihláste sa do Azure

Ako bezpečnostnú prax použijeme [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) na autentifikáciu do Azure OpenAI pomocou Microsoft Entra ID. Predtým, než to budete môcť urobiť, musíte si najprv nainštalovať **Azure CLI** podľa [inštrukcií na inštaláciu](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=academic-105485-koreyst) pre váš operačný systém.

Ďalej otvorte terminál a spustite `az login --use-device-code`, aby ste sa prihlásili do svojho Azure účtu.

Po prihlásení vyberte svoje predplatné v termináli.

## Ďalšie premenné prostredia - Azure Search a Azure OpenAI

Pre lekciu Agentic RAG - Lekcia 5 - sú k dispozícii ukážky, ktoré využívajú Azure Search a Azure OpenAI.

Ak chcete spustiť tieto ukážky, budete musieť pridať nasledujúce premenné prostredia do svojho `.env` súboru:

### Stránka prehľadu (projekt)

- `AZURE_SUBSCRIPTION_ID` - Skontrolujte **Project details** na stránke **Overview** vášho projektu.

- `AZURE_AI_PROJECT_NAME` - Pozrite sa na vrch stránky **Overview** vášho projektu.

- `AZURE_OPENAI_SERVICE` - Nájdete v záložke **Included capabilities** pre **Azure OpenAI Service** na stránke **Overview**.

### Centrum správy

- `AZURE_OPENAI_RESOURCE_GROUP` - Prejdite na **Project properties** na stránke **Overview** v **Management Center**.

- `GLOBAL_LLM_SERVICE` - V sekcii **Connected resources** nájdite názov pripojenia **Azure AI Services**. Ak tam nie je, skontrolujte v **Azure portáli** vo vašej skupine zdrojov názov služby AI Services.

### Stránka modelov + koncových bodov

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Vyberte svoj embedding model (napr. `text-embedding-ada-002`) a poznačte si **Deployment name** z detailov modelu.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Vyberte svoj chat model (napr. `gpt-4o-mini`) a poznačte si **Deployment name** z detailov modelu.

### Azure portál

- `AZURE_OPENAI_ENDPOINT` - Nájdite **Azure AI services**, kliknite naň, potom prejdite do **Resource Management**, **Keys and Endpoint**, posuňte sa dole na "Azure OpenAI endpoints" a skopírujte ten, ktorý je označený ako "Language APIs".

- `AZURE_OPENAI_API_KEY` - Z tej istej obrazovky skopírujte KEY 1 alebo KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Nájdite svoj **Azure AI Search** zdroj, kliknite naň a pozrite si **Overview**.

- `AZURE_SEARCH_API_KEY` - Potom prejdite na **Settings** a potom **Keys**, aby ste skopírovali primárny alebo sekundárny admin kľúč.

### Externá webová stránka

- `AZURE_OPENAI_API_VERSION` - Navštívte stránku [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) pod **Latest GA API release**.

### Nastavenie keyless autentifikácie

Namiesto pevného zakódovania prihlasovacích údajov použijeme keyless pripojenie s Azure OpenAI. Na to importujeme `DefaultAzureCredential` a neskôr zavoláme funkciu `DefaultAzureCredential` na získanie poverení.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Máte problém?

Ak máte akékoľvek problémy s týmto nastavením, pripojte sa do nášho

## Ďalšia lekcia

Teraz ste pripravení spustiť kód pre tento kurz. Prajeme vám veľa zábavy pri objavovaní sveta AI agentov!

[Úvod do AI agentov a ich využitia](../01-intro-to-ai-agents/README.md)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.