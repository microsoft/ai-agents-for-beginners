# AGENTS.md

## Přehled projektu

Tento repozitář obsahuje "AI Agents for Beginners" - komplexní vzdělávací kurz, který učí vše potřebné k vytvoření AI agentů. Kurz se skládá z více než 15 lekcí, které pokrývají základy, návrhové vzory, frameworky a nasazení AI agentů do produkce.

**Klíčové technologie:**
- Python 3.12+
- Jupyter Notebooks pro interaktivní učení
- AI frameworky: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI služby: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (dostupná bezplatná verze)

**Architektura:**
- Struktura založená na lekcích (adresáře 00-15+)
- Každá lekce obsahuje: dokumentaci README, ukázky kódu (Jupyter notebooks) a obrázky
- Podpora více jazyků prostřednictvím automatizovaného překladového systému
- Více možností frameworků pro každou lekci (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Příkazy pro nastavení

### Předpoklady
- Python 3.12 nebo vyšší
- GitHub účet (pro GitHub Models - bezplatná verze)
- Azure předplatné (volitelné, pro Azure AI služby)

### Počáteční nastavení

1. **Naklonujte nebo vytvořte fork repozitáře:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Vytvořte a aktivujte virtuální prostředí Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Nainstalujte závislosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nastavte proměnné prostředí:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Požadované proměnné prostředí

Pro **GitHub Models (bezplatná verze)**:
- `GITHUB_TOKEN` - Osobní přístupový token z GitHubu

Pro **Azure AI služby** (volitelné):
- `PROJECT_ENDPOINT` - Endpoint projektu Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - API klíč pro Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL endpointu Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Název nasazení pro chat model
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Název nasazení pro embeddings
- Další konfigurace Azure, jak je uvedeno v `.env.example`

## Pracovní postup vývoje

### Spouštění Jupyter Notebooks

Každá lekce obsahuje několik Jupyter notebooks pro různé frameworky:

1. **Spusťte Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Přejděte do adresáře lekce** (např. `01-intro-to-ai-agents/code_samples/`)

3. **Otevřete a spusťte notebooks:**
   - `*-semantic-kernel.ipynb` - Použití frameworku Semantic Kernel
   - `*-autogen.ipynb` - Použití frameworku AutoGen
   - `*-python-agent-framework.ipynb` - Použití Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Použití Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Použití Azure AI Agent Service

### Práce s různými frameworky

**Semantic Kernel + GitHub Models:**
- Dostupná bezplatná verze s GitHub účtem
- Vhodné pro učení a experimentování
- Vzor souboru: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Dostupná bezplatná verze s GitHub účtem
- Schopnosti orchestrace více agentů
- Vzor souboru: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Nejnovější framework od Microsoftu
- Dostupný v Pythonu a .NET
- Vzor souboru: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Vyžaduje předplatné Azure
- Funkce připravené pro produkci
- Vzor souboru: `*-azureaiagent.ipynb`

## Pokyny k testování

Toto je vzdělávací repozitář s ukázkovým kódem, nikoli produkční kód s automatizovanými testy. Pro ověření nastavení a změn:

### Manuální testování

1. **Otestujte prostředí Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Otestujte spuštění notebooků:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Ověřte proměnné prostředí:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Spouštění jednotlivých notebooků

Otevřete notebooky v Jupyteru a postupně spouštějte buňky. Každý notebook je samostatný a obsahuje:
- Importy
- Načítání konfigurace
- Ukázkové implementace agentů
- Očekávané výstupy v markdown buňkách

## Styl kódu

### Konvence pro Python

- **Verze Pythonu**: 3.12+
- **Styl kódu**: Dodržujte standardní konvence PEP 8
- **Notebooks**: Používejte jasné markdown buňky k vysvětlení konceptů
- **Importy**: Skupiny podle standardní knihovny, třetích stran, lokálních importů

### Konvence pro Jupyter Notebook

- Zahrňte popisné markdown buňky před buňkami s kódem
- Přidejte příklady výstupů v notebooku pro referenci
- Používejte jasné názvy proměnných odpovídající konceptům lekce
- Udržujte lineární pořadí spouštění notebooku (buňka 1 → 2 → 3...)

### Organizace souborů

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```

## Sestavení a nasazení

### Sestavení dokumentace

Tento repozitář používá Markdown pro dokumentaci:
- README.md soubory v každé složce lekce
- Hlavní README.md v kořenovém adresáři repozitáře
- Automatizovaný překladový systém prostřednictvím GitHub Actions

### CI/CD Pipeline

Umístěno v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický překlad do více než 50 jazyků
2. **welcome-issue.yml** - Vítá nové tvůrce issue
3. **welcome-pr.yml** - Vítá nové přispěvatele pull requestů

### Nasazení

Toto je vzdělávací repozitář - žádný proces nasazení. Uživatelé:
1. Vytvoří fork nebo naklonují repozitář
2. Spustí notebooky lokálně nebo v GitHub Codespaces
3. Učí se úpravou a experimentováním s příklady

## Pokyny pro pull requesty

### Před odesláním

1. **Otestujte své změny:**
   - Kompletně spusťte ovlivněné notebooky
   - Ověřte, že všechny buňky se spustí bez chyb
   - Zkontrolujte, zda jsou výstupy vhodné

2. **Aktualizace dokumentace:**
   - Aktualizujte README.md při přidávání nových konceptů
   - Přidejte komentáře v notebooku pro složitý kód
   - Ujistěte se, že markdown buňky vysvětlují účel

3. **Změny souborů:**
   - Nezahrnujte `.env` soubory (použijte `.env.example`)
   - Nezahrnujte adresáře `venv/` nebo `__pycache__/`
   - Zachovejte výstupy notebooků, pokud demonstrují koncepty
   - Odstraňte dočasné soubory a záložní notebooky (`*-backup.ipynb`)

### Formát názvu PR

Používejte popisné názvy:
- `[Lesson-XX] Přidání nového příkladu pro <koncept>`
- `[Fix] Oprava překlepu v README lekce-XX`
- `[Update] Vylepšení ukázky kódu v lekci-XX`
- `[Docs] Aktualizace pokynů k nastavení`

### Požadované kontroly

- Notebooky by měly být spuštěny bez chyb
- README soubory by měly být jasné a přesné
- Dodržujte existující vzory kódu v repozitáři
- Udržujte konzistenci s ostatními lekcemi

## Další poznámky

### Časté problémy

1. **Nesoulad verze Pythonu:**
   - Ujistěte se, že používáte Python 3.12+
   - Některé balíčky nemusí fungovat se staršími verzemi
   - Použijte `python3 -m venv` pro explicitní určení verze Pythonu

2. **Proměnné prostředí:**
   - Vždy vytvořte `.env` z `.env.example`
   - Nezahrnujte `.env` soubor (je v `.gitignore`)
   - GitHub token potřebuje odpovídající oprávnění

3. **Konflikty balíčků:**
   - Použijte nové virtuální prostředí
   - Instalujte z `requirements.txt` místo jednotlivých balíčků
   - Některé notebooky mohou vyžadovat další balíčky uvedené v jejich markdown buňkách

4. **Azure služby:**
   - Azure AI služby vyžadují aktivní předplatné
   - Některé funkce jsou specifické pro region
   - Omezení bezplatné verze platí pro GitHub Models

### Učební cesta

Doporučený postup lekcemi:
1. **00-course-setup** - Začněte zde s nastavením prostředí
2. **01-intro-to-ai-agents** - Pochopte základy AI agentů
3. **02-explore-agentic-frameworks** - Naučte se o různých frameworcích
4. **03-agentic-design-patterns** - Klíčové návrhové vzory
5. Pokračujte postupně očíslovanými lekcemi

### Výběr frameworku

Vyberte framework podle svých cílů:
- **Učení/Prototypování**: Semantic Kernel + GitHub Models (bezplatná verze)
- **Systémy s více agenty**: AutoGen
- **Nejnovější funkce**: Microsoft Agent Framework (MAF)
- **Nasazení do produkce**: Azure AI Agent Service

### Získání pomoci

- Připojte se k [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Projděte README soubory lekcí pro konkrétní pokyny
- Zkontrolujte hlavní [README.md](./README.md) pro přehled kurzu
- Odkazujte na [Course Setup](./00-course-setup/README.md) pro podrobné pokyny k nastavení

### Přispívání

Toto je otevřený vzdělávací projekt. Přispění vítáno:
- Vylepšení ukázek kódu
- Oprava překlepů nebo chyb
- Přidání objasňujících komentářů
- Návrh nových témat lekcí
- Překlad do dalších jazyků

Viz [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pro aktuální potřeby.

## Kontext specifický pro projekt

### Podpora více jazyků

Tento repozitář používá automatizovaný překladový systém:
- Podpora více než 50 jazyků
- Překlady ve složkách `/translations/<lang-code>/`
- GitHub Actions workflow zajišťuje aktualizace překladů
- Zdrojové soubory jsou v angličtině v kořenovém adresáři repozitáře

### Struktura lekcí

Každá lekce má konzistentní strukturu:
1. Miniatura videa s odkazem
2. Písemný obsah lekce (README.md)
3. Ukázky kódu v různých frameworcích
4. Cíle učení a předpoklady
5. Odkazy na další vzdělávací zdroje

### Názvy ukázek kódu

Formát: `<číslo-lekce>-<název-frameworku>.ipynb`
- `04-semantic-kernel.ipynb` - Lekce 4, Semantic Kernel
- `07-autogen.ipynb` - Lekce 7, AutoGen
- `14-python-agent-framework.ipynb` - Lekce 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Lekce 14, MAF .NET

### Speciální adresáře

- `translated_images/` - Lokalizované obrázky pro překlady
- `images/` - Originální obrázky pro obsah v angličtině
- `.devcontainer/` - Konfigurace vývojového kontejneru pro VS Code
- `.github/` - GitHub Actions workflow a šablony

### Závislosti

Klíčové balíčky z `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen framework
- `semantic-kernel` - Semantic Kernel framework
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI služby
- `azure-search-documents` - Integrace Azure AI Search
- `chromadb` - Vektorová databáze pro příklady RAG
- `chainlit` - Framework pro chatovací UI
- `browser_use` - Automatizace prohlížeče pro agenty
- `mcp[cli]` - Podpora Model Context Protocol
- `mem0ai` - Správa paměti pro agenty

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.