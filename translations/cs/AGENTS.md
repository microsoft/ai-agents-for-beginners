# AGENTS.md

## Přehled projektu

Toto úložiště obsahuje „AI Agentů pro začátečníky“ - komplexní vzdělávací kurz, který učí vše potřebné k vytvoření AI agentů. Kurz se skládá z 18 lekcí (číslovaných 00-18), pokrývajících základy, designové vzory, frameworky, nasazení do produkce, lokální/agenty na zařízení a bezpečnost AI agentů.

**Klíčové technologie:**
- Python 3.12+
- Jupyter Notebooks pro interaktivní učení
- AI Frameworky: Microsoft Agent Framework (MAF)
- Azure AI služby: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektura:**
- Struktura založená na lekcích (adresáře 00-15+)
- Každá lekce obsahuje: dokumentaci README, ukázky kódu (Jupyter notebooks) a obrázky
- Vícejazyčná podpora prostřednictvím automatizovaného překladového systému
- Jeden Python notebook na lekci používající Microsoft Agent Framework

## Příkazy pro nastavení

### Předpoklady
- Python 3.12 nebo vyšší
- Azure předplatné (pro Microsoft Foundry)
- Nainstalovaný a autentizovaný Azure CLI (`az login`)

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
   # Upravte soubor .env se svými API klíči a koncovými body
   ```

### Povinné proměnné prostředí

Pro **Microsoft Foundry** (povinné):
- `AZURE_AI_PROJECT_ENDPOINT` - koncový bod projektu Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - název nasazení modelu (např. gpt-5-mini)

Pro **Azure AI Search** (lekce 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - koncový bod Azure AI Search
- `AZURE_SEARCH_API_KEY` - API klíč Azure AI Search

Autentizace: Spusťte `az login` před spuštěním notebooků (používá `AzureCliCredential`).

## Vývojový postup

### Spuštění Jupyter notebooků

Každá lekce obsahuje několik Jupyter notebooků pro různé frameworky:

1. **Spusťte Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Přejděte do adresáře lekce** (např. `01-intro-to-ai-agents/code_samples/`)

3. **Otevřete a spusťte notebooky:**
   - `*-python-agent-framework.ipynb` - Používání Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Používání Microsoft Agent Framework (.NET)

### Práce s Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Vyžaduje Azure předplatné
- Používá `FoundryChatClient` pro Agent Service V2 (agenti jsou viditelní v portálu Foundry)
- Připravené pro produkci s vestavěnou pozorovatelností
- Vzor souboru: `*-python-agent-framework.ipynb`

## Instrukce pro testování

Toto je vzdělávací repozitář s ukázkovým kódem, nikoli produkční kód s automatizovanými testy. Pro ověření vašeho nastavení a změn:

### Manuální testování

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
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Spuštění jednotlivých notebooků

Otevřete notebooky v Jupyteru a spouštějte buňky postupně. Každý notebook je samostatný a zahrnuje:
- Importy
- Načítání konfigurace
- Příkladové implementace agentů
- Očekávané výstupy v markdown buňkách

### Smoke-testování nasazených agentů

Pro lekce, kde je agent nasazen jako Microsoft Foundry hostovaný agent (01, 04, 05, 16), obsahuje repozitář smoke-test katalogy v `tests/`, které jsou spouštěny workflow `.github/workflows/smoke-test.yml` přes akci [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Jedná se o lehkou bránu po nasazení (je agent dostupný a odpovídá základním očekáváním promptu?), doplňující evaluační pipeline v lekcích 10 a 16. Viz [tests/README.md](./tests/README.md) pro mapování katalog-lekce-agent. Lekce 17 běží lokálně s Foundry Local a nemá hostovaný endpoint, proto se validuje přímým spuštěním svého notebooku.

## Styl kódu

### Python konvence

- **Verze Pythonu**: 3.12+
- **Styl kódu**: Dodržujte standardní Python PEP 8 konvence
- **Notebooky**: Používejte jasné markdown buňky k vysvětlení konceptů
- **Importy**: Seskupujte podle standardní knihovny, třetích stran, lokální importy

### Konvence Jupyter notebooků

- Zahrňte popisné markdown buňky před kódové buňky
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

### Tvorba dokumentace

Toto repozitář používá Markdown pro dokumentaci:
- README.md soubory v každé složce lekce
- Hlavní README.md v kořenovém adresáři repozitáře
- Automatizovaný překladový systém přes GitHub Actions

### CI/CD pipeline

Nachází se v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický překlad do více než 50 jazyků
2. **welcome-issue.yml** - Přivítání nových autorů issues
3. **welcome-pr.yml** - Přivítání nových přispěvatelů pull requestů

### Nasazení

Toto je vzdělávací repozitář - žádný proces nasazení. Uživatelé:
1. Forknou nebo naklonují repozitář
2. Spouští notebooky lokálně nebo v GitHub Codespaces
3. Učí se úpravami a experimentováním s příklady

## Pokyny pro pull requesty

### Před odesláním

1. **Otestujte své změny:**
   - Kompletně spusťte upravené notebooky
   - Ověřte, že se všechny buňky spustí bez chyb
   - Zkontrolujte, zda jsou výstupy vhodné

2. **Aktualizace dokumentace:**
   - Aktualizujte README.md, pokud přidáváte nové koncepty
   - Přidejte komentáře v noteboocích pro složitější kód
   - Ujistěte se, že markdown buňky vysvětlují účel

3. **Změny souborů:**
   - Vyvarujte se commitování `.env` souborů (používejte `.env.example`)
   - Necommitujte adresáře `venv/` nebo `__pycache__/`
   - Zachovejte výstupy notebooků, pokud demonstrují koncepty
   - Odstraňte dočasné soubory a záložní notebooky (`*-backup.ipynb`)

### Formát názvu PR

Používejte popisné názvy:
- `[Lesson-XX] Přidat nový příklad pro <koncept>`
- `[Fix] Opravit překlep v README lekce-XX`
- `[Update] Vylepšit ukázku kódu v lekci-XX`
- `[Docs] Aktualizovat instrukce ke setupu`

### Povinné kontroly

- Notebooky by měly běžet bez chyb
- README soubory by měly být jasné a přesné
- Dodržujte stávající vzory kódu v repozitáři
- Udržujte konzistenci s ostatními lekcemi

## Další poznámky

### Časté problémy

1. **Nesoulad verze Pythonu:**
   - Používejte Python 3.12+
   - Některé balíčky nemusí fungovat ve starších verzích
   - Použijte `python3 -m venv` pro explicitní specifikaci verze Pythonu

2. **Proměnné prostředí:**
   - Vždy vytvořte `.env` z `.env.example`
   - Necommitujte `.env` soubor (je v `.gitignore`)
   - Přihlašte se pomocí `az login` pro autentizaci Entra ID bez klíče

3. **Konflikty balíčků:**
   - Použijte čisté virtuální prostředí
   - Instalujte ze `requirements.txt` namísto jednotlivých balíčků
   - Některé notebooky mohou vyžadovat další balíčky uvedené v jejich markdown buňkách

4. **Azure služby:**
   - Azure AI služby vyžadují aktivní předplatné
   - Některé funkce jsou regionálně omezené
   - Ujistěte se, že vaše nasazení modelu Azure OpenAI podporuje Responses API

### Cesta učením

Doporučené pořadí lekcí:
1. **00-course-setup** - Začněte zde s nastavením prostředí
2. **01-intro-to-ai-agents** - Porozumění základům AI agentů
3. **02-explore-agentic-frameworks** - Seznamte se s různými frameworky
4. **03-agentic-design-patterns** - Základní designové vzory
5. Pokračujte postupně podle číslovaných lekcí

### Výběr frameworku

Vyberte framework podle svých cílů:
- **Všechny lekce**: Microsoft Agent Framework (MAF) s `FoundryChatClient`
- **Agenti se registrují na serverové straně** ve službě Microsoft Foundry Agent Service V2 a jsou viditelní v portálu Foundry

### Získání pomoci

- Připojte se k [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Prohlédněte si README soubory k lekcím pro konkrétní rady
- Zkontrolujte hlavní [README.md](./README.md) pro přehled kurzu
- Odkaz na [Course Setup](./00-course-setup/README.md) pro podrobné instrukce nastavení

### Přispívání

Toto je otevřený vzdělávací projekt. Přispívání vítáno:
- Vylepšování příkladů kódu
- Opravy překlepů nebo chyb
- Přidání vysvětlujících komentářů
- Návrhy nových témat lekcí
- Překlady do dalších jazyků

Viz [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pro aktuální potřeby.

## Kontext specifický pro projekt

### Vícejazyčná podpora

Toto úložiště používá automatizovaný překladový systém:
- Podporováno více než 50 jazyků
- Překlady v adresářích `/translations/<lang-code>/`
- GitHub Actions workflow zajišťuje aktualizace překladů
- Zdrojové soubory jsou v angličtině v kořenovém adresáři repozitáře

### Struktura lekcí

Každá lekce následuje konzistentní vzor:
1. Miniatura videa s odkazem
2. Písemný obsah lekce (README.md)
3. Ukázky kódu v různých frameworcích
4. Výukové cíle a předpoklady
5. Odkazy na další zdroje ke studiu

### Pojmenování ukázek kódu

Formát: `<číslo-lekce>-python-agent-framework.ipynb`
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