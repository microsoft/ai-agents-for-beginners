# AGENTS.md

## Přehled projektu

Tento repozitář obsahuje "AI Agenty pro začátečníky" - komplexní vzdělávací kurz, který učí vše potřebné k tvorbě AI agentů. Kurz sestává z více než 15 lekcí pokrývajících základy, návrhové vzory, frameworky a produkční nasazení AI agentů.

**Klíčové technologie:**
- Python 3.12 a novější
- Jupyter Notebooky pro interaktivní učení
- AI frameworky: Microsoft Agent Framework (MAF)
- Azure AI služby: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architektura:**
- Struktura založená na lekcích (adresáře 00-15+)
- Každá lekce obsahuje: dokumentaci README, ukázky kódu (Jupyter notebooky) a obrázky
- Podpora více jazyků přes automatizovaný překladový systém
- Jeden Python notebook na lekci používající Microsoft Agent Framework

## Příkazy pro nastavení

### Požadavky
- Python 3.12 nebo vyšší
- Azure předplatné (pro Azure AI Foundry)
- Azure CLI nainstalované a autentizované (`az login`)

### Počáteční nastavení

1. **Naklonujte nebo forkněte repozitář:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # NEBO
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Vytvořte a aktivujte Python virtuální prostředí:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Na Windows: venv\Scripts\activate
   ```

3. **Nainstalujte závislosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nastavte proměnné prostředí:**
   ```bash
   cp .env.example .env
   # Upravte soubor .env s vašimi API klíči a koncovými body
   ```

### Požadované proměnné prostředí

Pro **Azure AI Foundry** (povinné):
- `AZURE_AI_PROJECT_ENDPOINT` - koncový bod projektu Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - jméno nasazení modelu (např. gpt-4o)

Pro **Azure AI Search** (lekce 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - koncový bod Azure AI Search
- `AZURE_SEARCH_API_KEY` - API klíč Azure AI Search

Autentizace: Před spuštěním notebooků spusťte `az login` (používá `AzureCliCredential`).

## Vývojový postup

### Spuštění Jupyter notebooků

Každá lekce obsahuje několik Jupyter notebooků pro různé frameworky:

1. **Spusťte Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Přejděte do adresáře lekce** (např. `01-intro-to-ai-agents/code_samples/`)

3. **Otevřete a spusťte notebooky:**
   - `*-python-agent-framework.ipynb` - Použití Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Použití Microsoft Agent Framework (.NET)

### Práce s Microsoft Agent Frameworkem

**Microsoft Agent Framework + Azure AI Foundry:**
- Vyžaduje Azure předplatné
- Používá `AzureAIProjectAgentProvider` pro Agent Service V2 (agenti viditelní v portálu Foundry)
- Produkčně připravené s vestavěnou sledovatelností
- Vzory souborů: `*-python-agent-framework.ipynb`

## Instrukce pro testování

Toto je vzdělávací repozitář s ukázkovým kódem, nikoli produkční kód s automatizovanými testy. Pro ověření nastavení a změn:

### Manuální testování

1. **Otestujte Python prostředí:**
   ```bash
   python --version  # Mělo by být 3.12 a více
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Otestujte spuštění notebooků:**
   ```bash
   # Převést notebook na skript a spustit (testuje importy)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Ověřte proměnné prostředí:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Spuštění jednotlivých notebooků

Otevřete notebooky v Jupyteru a vykonávejte buňky postupně. Každý notebook je samostatný a obsahuje:
- Importy
- Načtení konfigurace
- Ukázkové implementace agentů
- Očekávané výstupy v markdown buňkách

## Styl kódu

### Python konvence

- **Verze Pythonu**: 3.12 a novější
- **Styl kódu**: Dodržujte standardní konvence Pythonu PEP 8
- **Notebooky**: Používejte jasné markdown buňky k vysvětlení konceptů
- **Importy**: Skupinujte podle standardních knihoven, třetích stran a lokálních importů

### Konvence Jupyter notebooků

- Zahrňte popisné markdown buňky před kódovými buňkami
- Přidávejte příklady výstupu v noteboocích pro referenci
- Používejte jasné názvy proměnných odpovídající konceptům lekcí
- Zachovejte lineární pořadí spuštění notebooku (buňka 1 → 2 → 3...)

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

### Tvorba dokumentace

Tento repozitář používá Markdown pro dokumentaci:
- README.md soubory v každé složce lekce
- Hlavní README.md v kořeni repozitáře
- Automatizovaný překladový systém přes GitHub Actions

### CI/CD pipeline

Umístěno v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický překlad do více než 50 jazyků
2. **welcome-issue.yml** - Vítání nových autorů issues
3. **welcome-pr.yml** - Vítání nových přispěvatelů pull requestů

### Nasazení

Jedná se o vzdělávací repozitář - žádný proces nasazení. Uživatelé:
1. Forknou nebo naklonují repozitář
2. Spouští notebooky lokálně nebo v GitHub Codespaces
3. Učí se úpravami a experimentováním s příklady

## Pravidla pro pull requesty

### Před odesláním

1. **Otestujte své změny:**
   - Kompletně spusťte ovlivněné notebooky
   - Ověřte, že všechny buňky běží bez chyb
   - Zkontrolujte, že výstupy jsou vhodné

2. **Aktualizace dokumentace:**
   - Aktualizujte README.md při přidání nových konceptů
   - Přidejte komentáře kódů v noteboocích pro složité části
   - Zajistěte, že markdown buňky vysvětlují účel

3. **Změny souborů:**
   - Vyhněte se commitování `.env` souborů (použijte `.env.example`)
   - Necommitujte adresáře `venv/` nebo `__pycache__/`
   - Zachovejte výstupy notebooků, pokud demonstrují koncepty
   - Odstraňte dočasné soubory a záložní notebooky (`*-backup.ipynb`)

### Formát názvu PR

Používejte popisné názvy:
- `[Lesson-XX] Přidat nový příklad pro <koncept>`
- `[Fix] Opravit překlep v lesson-XX README`
- `[Update] Vylepšit ukázkový kód v lesson-XX`
- `[Docs] Aktualizovat pokyny pro nastavení`

### Povinné kontroly

- Notebooky musí běžet bez chyb
- README soubory musí být jasné a přesné
- Dodržujte stávající vzory kódu v repozitáři
- Udržujte konzistenci s ostatními lekcemi

## Další poznámky

### Časté problémy

1. **Neodpovídající verze Pythonu:**
   - Zajistěte, že používáte Python 3.12 a novější
   - Některé balíky nemusí fungovat na starších verzích
   - Použijte `python3 -m venv` k explicitnímu určení verze Pythonu

2. **Proměnné prostředí:**
   - Vždy vytvořte `.env` ze souboru `.env.example`
   - Necommitujte `.env` (je v `.gitignore`)
   - GitHub token potřebuje odpovídající oprávnění

3. **Konflikty balíků:**
   - Používejte čerstvé virtuální prostředí
   - Instalujte z `requirements.txt` místo jednotlivých balíků
   - Některé notebooky vyžadují další balíky uvedené v markdown buňkách

4. **Azure služby:**
   - Azure AI služby vyžadují aktivní předplatné
   - Některé funkce jsou specifické pro region
   - Bezplatná úroveň má omezení v GitHub Models

### Výuková cesta

Doporučené postupné procházení lekcí:
1. **00-course-setup** - Začněte zde, nastavení prostředí
2. **01-intro-to-ai-agents** - Pochopení základů AI agentů
3. **02-explore-agentic-frameworks** - Seznámení s různými frameworky
4. **03-agentic-design-patterns** - Základní návrhové vzory
5. Pokračujte v číslovaných lekcích postupně

### Výběr frameworku

Vyberte framework podle svých cílů:
- **Všechny lekce**: Microsoft Agent Framework (MAF) s `AzureAIProjectAgentProvider`
- **Agenti se registrují na serverové straně** v Azure AI Foundry Agent Service V2 a jsou viditelní v portálu Foundry

### Kde hledat pomoc

- Připojte se k [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Prostudujte README soubory lekcí pro specifické návody
- Podívejte se na hlavní [README.md](./README.md) s přehledem kurzu
- Podrobné instrukce v [Course Setup](./00-course-setup/README.md)

### Přispívání

Toto je otevřený vzdělávací projekt. Přispěvatelé vítáni:
- Vylepšovat příklady kódu
- Opravovat překlepy nebo chyby
- Přidávat vysvětlující komentáře
- Navrhovat nová témata lekcí
- Překládat do dalších jazyků

Podívejte se na [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pro aktuální potřeby.

## Kontext specifický pro projekt

### Podpora více jazyků

Tento repozitář používá automatizovaný překladový systém:
- Podpora více než 50 jazyků
- Překlady jsou v adresářích `/translations/<lang-code>/`
- GitHub Actions workflow zajišťuje aktualizace překladů
- Zdroje jsou v angličtině v kořeni repozitáře

### Struktura lekcí

Každá lekce sleduje konzistentní vzor:
1. Náhled videa s odkazem
2. Psaný obsah lekce (README.md)
3. Ukázky kódu v různých frameworcích
4. Výukové cíle a předpoklady
5. Odkazy na doplňkové zdroje

### Pojmenování ukázek kódu

Formát: `<číslo-lekce>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekce 1, MAF Python
- `14-sequential.ipynb` - Lekce 14, pokročilé vzory MAF

### Speciální adresáře

- `translated_images/` - Lokalizované obrázky pro překlady
- `images/` - Originální obrázky pro anglický obsah
- `.devcontainer/` - Konfigurace VS Code vývojového kontejneru
- `.github/` - GitHub Actions workflowy a šablony

### Závislosti

Klíčové balíky z `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Podpora protokolu Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Azure AI služby
- `azure-identity` - Azure autentizace (AzureCliCredential)
- `azure-search-documents` - Integrace Azure AI Search
- `mcp[cli]` - Podpora Model Context Protocolu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědni za jakákoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->