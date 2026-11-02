# AGENTS.md

## Přehled projektu

Tento repozitář obsahuje "AI Agenty pro začátečníky" - komplexní vzdělávací kurz, který učí vše potřebné pro tvorbu AI Agentů. Kurz se skládá z 18 lekcí (číslováno 00-18), pokrývajících základy, návrhové vzory, frameworky, nasazení do produkce, lokální/agenty na zařízení a bezpečnost AI agentů.

**Klíčové technologie:**
- Python 3.12+
- Jupyter Notebooks pro interaktivní učení
- AI Frameworky: Microsoft Agent Framework (MAF)
- Azure AI služby: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektura:**
- Struktura založená na lekcích (adresáře 00-18)
- Každá lekce obsahuje: dokumentaci README, ukázky kódu (Jupyter notebooks) a obrázky
- Podpora více jazyků pomocí automatizovaného překladového systému
- Jeden Python notebook na lekci používající Microsoft Agent Framework

## Příkazy pro nastavení

### Požadavky
- Python 3.12 nebo vyšší
- Azure předplatné (pro Microsoft Foundry)
- Nainstalovaný a autentikovaný Azure CLI (`az login`)

### Počáteční nastavení

1. **Klonujte nebo forkněte repozitář:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Vytvořte a aktivujte Python virtuální prostředí:**
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

### Povinné proměnné prostředí

Pro **Microsoft Foundry** (Povinné):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projektový endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Název nasazení modelu (např. gpt-5-mini)

Pro **Azure AI Search** (Lekce 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API klíč

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

**Microsoft Agent Framework + Microsoft Foundry:**
- Vyžaduje Azure předplatné
- Používá `FoundryChatClient` pro Agent Service V2 (agenti viditelní v portálu Foundry)
- Produkčně připravené s vestavěnou pozorovatelností
- Vzor souboru: `*-python-agent-framework.ipynb`

## Pokyny pro testování

Toto je vzdělávací repozitář s ukázkovým kódem, ne produkční kód s automatickými testy. Pro ověření nastavení a změn:

### Ruční testování

1. **Otestujte Python prostředí:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Otestujte spuštění notebooku:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Ověřte proměnné prostředí:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Spuštění jednotlivých notebooků

Otevřete notebooky v Jupyter a spouštějte buňky postupně. Každý notebook je uzavřený a obsahuje:
- Importy
- Načítání konfigurace
- Příklady implementací agentů
- Očekávané výstupy v markdown buňkách

### Smoke-testování nasazených agentů

Pro lekce, kde je agent nasazen jako Microsoft Foundry hostovaný agent (01, 04, 05, 16), repozitář obsahuje smoke-test katalogy pod `tests/`, které spouští workflow `.github/workflows/smoke-test.yml` pomocí akce [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Jsou to lehké post-nasazovací kontroly (je agent dostupný a odpovídá základním očekáváním promptů?), doplňující evaluační pipeline v lekcích 10 a 16. Viz [tests/README.md](./tests/README.md) pro mapování katalogů na lekce a agenty. Lekce 17 běží lokálně s Foundry Local a nemá hostovaný endpoint, proto se ověřuje přímým spuštěním svého notebooku.

## Styl kódu

### Python konvence

- **Verze Pythonu**: 3.12+
- **Styl kódu**: Dodržujte standardní Python PEP 8 konvence
- **Notebooky**: Používejte srozumitelné markdown buňky pro vysvětlení konceptů
- **Importy**: Skupiny podle standardní knihovny, třetích stran, lokální importy

### Jupyter Notebook konvence

- Zahrnujte popisné markdown buňky před kódovými buňkami
- Přidávejte příklady výstupů v noteboocích jako referenci
- Používejte jasné názvy proměnných odpovídající konceptům lekcí
- Zachovejte lineární pořadí spouštění buněk (buňka 1 → 2 → 3...)

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
- Hlavní README.md v kořenovém adresáři repozitáře
- Automatizovaný překladový systém přes GitHub Actions

### CI/CD Pipeline

Nachází se v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický překlad do 50+ jazyků
2. **welcome-issue.yml** - Přivítání tvůrců nových issues
3. **welcome-pr.yml** - Přivítání přispěvatelů nových pull requestů

### Nasazení

Toto je vzdělávací repozitář - bez procesu nasazení. Uživatelé:
1. Forkují nebo klonují repozitář
2. Spouštějí notebooky lokálně nebo v GitHub Codespaces
3. Učí se tím, že mění a experimentují s příklady

## Pokyny pro pull requesty

### Před odesláním

1. **Otestujte své změny:**
   - Kompletně spusťte ovlivněné notebooky
   - Ověřte, že všechny buňky proběhnou bez chyb
   - Zkontrolujte, že výstupy jsou vhodné

2. **Aktualizace dokumentace:**
   - Aktualizujte README.md při přidání nových konceptů
   - Přidejte komentáře do notebooků k složitému kódu
   - Zajistěte, aby markdown buňky vysvětlovaly účel

3. **Změny v souborech:**
   - Vyvarujte se commitu `.env` souborů (použijte `.env.example`)
   - Nekomitujte `venv/` nebo `__pycache__/` adresáře
   - Zachovejte výstupy notebooků, pokud demonstrují koncepty
   - Odstraňte dočasné soubory a zálohy notebooků (`*-backup.ipynb`)

### Formát názvu PR

Používejte popisné názvy:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Povinné kontroly

- Notebooky by měly běžet bez chyb
- README soubory by měly být jasné a přesné
- Dodržujte existující vzory kódu v repozitáři
- Zachovejte konzistenci s ostatními lekcemi

## Další poznámky

### Časté problémy

1. **Neshoda verze Pythonu:**
   - Používejte Python 3.12+
   - Některé balíčky nemusí fungovat s nižšími verzemi
   - Použijte `python3 -m venv` pro explicitní nastavení verze Pythonu

2. **Proměnné prostředí:**
   - Vždy vytvářejte `.env` z `.env.example`
   - Nekomitujte `.env` soubor (je v `.gitignore`)
   - Přihlašujte se přes `az login` pro autentizaci Entra ID bez klíče

3. **Konflikty balíčků:**
   - Používejte nové virtuální prostředí
   - Instalujte z `requirements.txt` místo jednotlivých balíčků
   - Některé notebooky mohou vyžadovat další balíčky uvedené v jejich markdown buňkách

4. **Azure služby:**
   - Azure AI služby vyžadují aktivní předplatné
   - Některé funkce jsou regionálně specifické
   - Ujistěte se, že vaše nasazení Azure OpenAI modelu podporuje Responses API

### Učební cesta

Doporučené pořadí lekcí:
1. **00-course-setup** - Začněte zde s nastavením prostředí
2. **01-intro-to-ai-agents** - Pochopte základy AI agentů
3. **02-explore-agentic-frameworks** - Naučte se o různých frameworkech
4. **03-agentic-design-patterns** - Jádrové návrhové vzory
5. Pokračujte postupně přes číslované lekce

### Výběr frameworku

Vyberte framework podle svých cílů:
- **Všechny lekce**: Microsoft Agent Framework (MAF) s `FoundryChatClient`
- **Agenti se registrují na serveru** v Microsoft Foundry Agent Service V2 a jsou vidět v portálu Foundry

### Získání pomoci

- Připojte se k [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Prohlédněte si README soubory lekcí pro konkrétní rady
- Nahlédněte do hlavního [README.md](./README.md) pro přehled kurzu
- Viz [Course Setup](./00-course-setup/README.md) pro detailní instrukce nastavení

### Přispívání

Toto je otevřený vzdělávací projekt. Vítány jsou příspěvky:
- Vylepšení příkladů kódu
- Opravy překlepů nebo chyb
- Přidání upřesňujících komentářů
- Návrhy nových témat lekcí
- Překlady do dalších jazyků

Viz [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pro aktuální potřeby.

## Kontext specifický pro projekt

### Podpora více jazyků

Tento repozitář používá automatizovaný překladový systém:
- Podpora více než 50 jazyků
- Překlady v `/translations/<lang-code>/` adresářích
- Překladové aktualizace spravuje GitHub Actions workflow
- Zdrojové soubory jsou v angličtině v kořenovém adresáři repozitáře

### Struktura lekcí

Každá lekce má konzistentní vzor:
1. Video náhled s odkazem
2. Psaný obsah lekce (README.md)
3. Ukázky kódu ve více frameworcích
4. Vzdělávací cíle a požadavky
5. Odkazy na další zdroje k učení

### Pojmenování ukázek kódu

Formát: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekce 1, MAF Python
- `14-sequential.ipynb` - Lekce 14, pokročilé vzory MAF
- `16-python-agent-framework.ipynb` - Lekce 16, produkční agent zákaznické podpory
- `17-local-agent-foundry-local.ipynb` - Lekce 17, lokální agent s Foundry Local + Qwen

### Speciální adresáře

- `translated_images/` - Lokalizované obrázky pro překlady
- `images/` - Originální obrázky pro anglický obsah
- `.devcontainer/` - Konfigurace vývojového kontejneru VS Code
- `.github/` - GitHub Actions workflowy a šablony

### Závislosti

Klíčové balíčky z `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Podpora protokolu Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Azure AI služby
- `azure-identity` - Azure autentizace (AzureCliCredential)
- `azure-search-documents` - Integrace Azure AI Search
- `mcp[cli]` - Podpora Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->