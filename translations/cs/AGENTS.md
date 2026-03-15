# AGENTS.md

## Přehled projektu

Tento repozitář obsahuje "AI Agenty pro začátečníky" - komplexní vzdělávací kurz, který učí vše, co je potřeba k vytvoření AI agentů. Kurz se skládá z více než 15 lekcí pokrývajících základy, návrhové vzory, frameworky a produkční nasazení AI agentů.

**Klíčové technologie:**
- Python 3.12+
- Jupyter Notebooky pro interaktivní učení
- AI Frameworky: Microsoft Agent Framework (MAF)
- Azure AI služby: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architektura:**
- Struktura založená na lekcích (adresáře 00-15+)
- Každá lekce obsahuje: dokumentaci README, ukázkové kódy (Jupyter notebooky) a obrázky
- Podpora vícejazyčnosti pomocí automatizovaného překladového systému
- Jeden Python notebook na lekci používající Microsoft Agent Framework

## Příkazy pro nastavení

### Požadavky
- Python 3.12 nebo vyšší
- Azure předplatné (pro Azure AI Foundry)
- Azure CLI nainstalované a autentizované (`az login`)

### Počáteční nastavení

1. **Klonujte nebo forkněte repozitář:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # NEBO
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Vytvořte a aktivujte Python virtuální prostředí:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Ve Windows: venv\Scripts\activate
   ```

3. **Nainstalujte závislosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nastavte proměnné prostředí:**
   ```bash
   cp .env.example .env
   # Upravte soubor .env a přidejte své API klíče a koncové body
   ```

### Požadované proměnné prostředí

Pro **Azure AI Foundry** (povinné):
- `AZURE_AI_PROJECT_ENDPOINT` - koncový bod Azure AI Foundry projektu
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - název nasazení modelu (např. gpt-4o)

Pro **Azure AI Search** (Lekce 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - koncový bod Azure AI Search
- `AZURE_SEARCH_API_KEY` - API klíč Azure AI Search

Autentizace: Spusťte `az login` před spuštěním notebooků (používá `AzureCliCredential`).

## Vývojový postup

### Spuštění Jupyter notebooků

Každá lekce obsahuje více Jupyter notebooků pro různé frameworky:

1. **Spusťte Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Přejděte do adresáře lekce** (např. `01-intro-to-ai-agents/code_samples/`)

3. **Otevřete a spusťte notebooky:**
   - `*-python-agent-framework.ipynb` - Použití Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Použití Microsoft Agent Framework (.NET)

### Práce s Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Vyžaduje Azure předplatné
- Používá `AzureAIProjectAgentProvider` pro Agent Service V2 (agentové viditelní v Foundry portálu)
- Produkčně připraveno s vestavěnou možností monitorování
- Vzor souborů: `*-python-agent-framework.ipynb`

## Instrukce k testování

Toto je vzdělávací repozitář s ukázkovým kódem, nikoli produkční kód s automatickými testy. Pro ověření nastavení a změn:

### Ruční testování

1. **Otestujte Python prostředí:**
   ```bash
   python --version  # Mělo by být 3.12 a výše
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Otestujte spuštění notebooku:**
   ```bash
   # Převést poznámkový blok na skript a spustit (testuje importy)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Ověřte proměnné prostředí:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Spuštění jednotlivých notebooků

Otevřete notebooky v Jupyter a spouštějte buňky sekvenčně. Každý notebook je samostatný a obsahuje:
- Importy
- Načítání konfigurace
- Ukázkové implementace agentů
- Očekávané výstupy v markdown buňkách

## Styl kódu

### Python konvence

- **Verze Pythonu**: 3.12+
- **Styl kódu**: Dodržujte standardní Python PEP 8 konvence
- **Notebooky**: Používejte srozumitelné markdown buňky pro vysvětlení konceptů
- **Importy**: Skupiny podle standardní knihovny, třetích stran, lokálních importů

### Konvence Jupyter notebooků

- Zařaďte popisné markdown buňky před kódové buňky
- Přidejte příklady výstupů v noteboocích pro referenci
- Používejte jasné názvy proměnných odpovídající konceptům lekce
- Zachovejte lineární pořadí spouštění notebooku (buňka 1 → 2 → 3 ...)

### Organizace souborů

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Sestavení a nasazení

### Vytváření dokumentace

Tento repozitář používá Markdown pro dokumentaci:
- README.md soubory v každé složce lekce
- Hlavní README.md v kořenu repozitáře
- Automatizovaný překladový systém pomocí GitHub Actions

### CI/CD Pipeline

Nachází se v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický překlad do 50+ jazyků
2. **welcome-issue.yml** - Přivítání nových přispěvatelů issues
3. **welcome-pr.yml** - Přivítání nových přispěvatelů pull requestů

### Nasazení

Toto je vzdělávací repozitář - není zde proces nasazení. Uživatelé:
1. Forknou nebo klonují repozitář
2. Spouští notebooky lokálně nebo v GitHub Codespaces
3. Učí se úpravou a experimentováním s příklady

## Směrnice pro Pull Requesty

### Před odesláním

1. **Otestujte své změny:**
   - Kompletně spusťte ovlivněné notebooky
   - Ověřte, že všechny buňky proběhnou bez chyb
   - Zkontrolujte, že výstupy jsou relevantní

2. **Aktualizace dokumentace:**
   - Aktualizujte README.md pokud přidáváte nové koncepty
   - Přidejte komentáře v noteboocích pro složitější kód
   - Ujistěte se, že markdown buňky vysvětlují účel

3. **Změny v souborech:**
   - Vyhněte se commitu `.env` souborů (používejte `.env.example`)
   - Necommitujte složky `venv/` nebo `__pycache__/`
   - Zachovejte výstupy notebooků, pokud demonstrují koncepty
   - Odstraňte dočasné soubory a záložní notebooky (`*-backup.ipynb`)

### Formát názvu PR

Používejte popisné názvy:
- `[Lesson-XX] Přidat nový příklad pro <koncept>`
- `[Fix] Opravit překlep v README lekce XX`
- `[Update] Vylepšit ukázkový kód v lekci XX`
- `[Docs] Aktualizovat instrukce pro nastavení`

### Požadované kontroly

- Notebooky by měly proběhnout bez chyb
- README soubory by měly být jasné a přesné
- Dodržujte existující vzory kódu v repozitáři
- Zachovejte konzistenci s ostatními lekcemi

## Další poznámky

### Časté chyby

1. **Neshoda verze Pythonu:**
   - Ujistěte se, že používáte Python 3.12+
   - Některé balíčky nemusí fungovat na starších verzích
   - Použijte `python3 -m venv` pro explicitní určení verze Pythonu

2. **Proměnné prostředí:**
   - Vždy vytvořte `.env` z `.env.example`
   - Komitujte `.env` soubory (jsou v `.gitignore`)
   - GitHub token potřebuje správná oprávnění

3. **Konflikty balíčků:**
   - Použijte nové virtuální prostředí
   - Instalujte z `requirements.txt` místo jednotlivých balíčků
   - Některé notebooky mohou vyžadovat další balíčky uvedené v markdown buňkách

4. **Azure služby:**
   - Azure AI služby vyžadují aktivní předplatné
   - Některé funkce jsou regionálně omezené
   - Free tier omezení se vztahují na GitHub Models

### Učební cesta

Doporučený postup přes lekce:
1. **00-course-setup** - Začněte zde s nastavením prostředí
2. **01-intro-to-ai-agents** - Porozumění základům AI agentů
3. **02-explore-agentic-frameworks** - Seznámení s různými frameworky
4. **03-agentic-design-patterns** - Základní návrhové vzory
5. Pokračujte postupně podle číslovaných lekcí

### Výběr frameworku

Vyberte framework podle svých cílů:
- **Všechny lekce**: Microsoft Agent Framework (MAF) s `AzureAIProjectAgentProvider`
- **Agenty se registrují server-side** v Azure AI Foundry Agent Service V2 a jsou viditelní v Foundry portálu

### Jak získat pomoc

- Připojte se na [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Prostudujte README soubory k lekcím pro specifické pokyny
- Zkontrolujte hlavní [README.md](./README.md) pro přehled kurzu
- Podívejte se na [Course Setup](./00-course-setup/README.md) pro podrobné nastavení

### Přispívání

Toto je otevřený vzdělávací projekt. Přispívání vítáno:
- Vylepšení příkladů kódu
- Opravy překlepů nebo chyb
- Přidání vysvětlujících komentářů
- Návrhy nových témat lekcí
- Překlady do dalších jazyků

Viz [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pro aktuální potřeby.

## Kontext specifický pro projekt

### Podpora vícejazyčnosti

Tento repozitář používá automatizovaný překladový systém:
- Podpora více než 50 jazyků
- Překlady v adresářích `/translations/<lang-code>/`
- GitHub Actions workflow zajišťuje aktualizace překladů
- Zdrojové soubory jsou v angličtině v kořenu repozitáře

### Struktura lekce

Každá lekce má stejný vzorec:
1. Náhled videa s odkazem
2. Psaný obsah lekce (README.md)
3. Ukázkové kódy v různých frameworcích
4. Cíle učení a požadavky
5. Odkazy na další studijní materiály

### Pojmenování ukázkových kódů

Formát: `<číslo-lekce>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekce 1, MAF Python
- `14-sequential.ipynb` - Lekce 14, pokročilé vzory MAF

### Speciální adresáře

- `translated_images/` - Lokalizované obrázky pro překlady
- `images/` - Originální obrázky pro anglický obsah
- `.devcontainer/` - Konfigurace VS Code vývojového kontejneru
- `.github/` - GitHub Actions workflowy a šablony

### Závislosti

Hlavní balíčky z `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokolová podpora
- `azure-ai-inference`, `azure-ai-projects` - Azure AI služby
- `azure-identity` - Azure autentizace (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integrace
- `mcp[cli]` - Podpora Model Context Protocolu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj je považován originální dokument v jeho původním jazyce. Pro důležité informace se doporučuje využít profesionální lidský překlad. Nejsme odpovědni za jakákoliv nedorozumění nebo chybné výklady vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->