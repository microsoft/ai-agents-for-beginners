# AGENTS.md

## Přehled projektu

Tento repozitář obsahuje "AI Agenty pro začátečníky" - komplexní vzdělávací kurz, který učí vše potřebné k vytváření AI agentů. Kurz se skládá z 18 lekcí pokrývajících základy, návrhové vzory, rámce a nasazení AI agentů do produkce.

**Klíčové technologie:**
- Python 3.12+
- Jupyter notebooky pro interaktivní učení
- AI rámce: Microsoft Agent Framework (MAF)
- Azure AI služby: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektura:**
- Struktura založená na lekcích (adresáře 00-15+)
- Každá lekce obsahuje: dokumentaci README, ukázky kódu (Jupyter notebooky) a obrázky
- Vícejazyčná podpora pomocí automatizovaného překladatelského systému
- Jeden Python notebook na lekci používající Microsoft Agent Framework

## Příkazy pro nastavení

### Požadavky
- Python 3.12 nebo vyšší
- Azure předplatné (pro Microsoft Foundry)
- Nainstalovaný a autentizovaný Azure CLI (`az login`)

### Počáteční nastavení

1. **Klonujte nebo forknete repozitář:**
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
   # Upravte soubor .env se svými API klíči a koncovými body
   ```

### Požadované proměnné prostředí

Pro **Microsoft Foundry** (požadováno):
- `AZURE_AI_PROJECT_ENDPOINT` - koncový bod projektu Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - název nasazení modelu (např. gpt-4o)

Pro **Azure AI Search** (Lekce 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - koncový bod Azure AI Search
- `AZURE_SEARCH_API_KEY` - API klíč Azure AI Search

Autentizace: Spusťte `az login` před spuštěním notebooků (používá `AzureCliCredential`).

## Vývojový postup

### Spuštění Jupyter notebooků

Každá lekce obsahuje několik Jupyter notebooků pro různé rámce:

1. **Spusťte Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Přejděte do adresáře s lekcí** (např. `01-intro-to-ai-agents/code_samples/`)

3. **Otevřete a spusťte notebooky:**
   - `*-python-agent-framework.ipynb` - Použití Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Použití Microsoft Agent Framework (.NET)

### Práce s Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Vyžaduje předplatné Azure
- Používá `FoundryChatClient` pro Agent Service V2 (agent viditelný v portálu Foundry)
- Produkčně připravený s vestavěnou observabilitou
- Vzor souborů: `*-python-agent-framework.ipynb`

## Instrukce pro testování

Toto je vzdělávací repozitář s ukázkovým kódem, nikoli produkční kód s automatizovanými testy. Pro ověření nastavení a změn:

### Manuální testování

1. **Otestujte Python prostředí:**
   ```bash
   python --version  # Měla by být 3.12+
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

Otevřete notebooky v Jupyteru a vykonávejte buňky postupně. Každý notebook je samostatný a obsahuje:
- Importy
- Načítání konfigurace
- Příklady implementací agentů
- Očekávané výstupy v markdown buňkách

## Styl kódu

### Python konvence

- **Verze Pythonu**: 3.12+
- **Styl kódu**: Dodržujte standardní Python PEP 8 konvence
- **Notebooky**: Používejte jasné markdown buňky pro vysvětlení konceptů
- **Importy**: Skupinujte podle standardní knihovny, cizích, lokálních importů

### Konvence Jupyter notebooků

- Zařaďte popisné markdown buňky před kódové buňky
- Přidejte příklady výstupů v notebooku jako referenci
- Používejte jasné názvy proměnných odpovídající konceptům lekcí
- Zachovejte lineární pořadí spouštění notebooku (buňka 1 → 2 → 3...)

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
- Automatizovaný překladatelský systém přes GitHub Actions

### CI/CD Pipeline

Nachází se v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický překlad do 50+ jazyků
2. **welcome-issue.yml** - Vítání nových autorů issue
3. **welcome-pr.yml** - Vítání nových přispěvatelů pull requestů

### Nasazení

Toto je vzdělávací repozitář - není zde proces nasazení. Uživatelé:
1. Forkují nebo klonují repozitář
2. Spouští notebooky lokálně nebo v GitHub Codespaces
3. Učí se úpravou a experimentováním s příklady

## Pokyny k pull requestům

### Před odesláním

1. **Otestujte své změny:**
   - Kompletně spusťte ovlivněné notebooky
   - Ověřte, že všechny buňky proběhnou bez chyb
   - Zkontrolujte, zda jsou výstupy vhodné

2. **Aktualizace dokumentace:**
   - Aktualizujte README.md pokud přidáváte nové koncepty
   - Přidejte komentáře do notebooků pro složitý kód
   - Zajistěte, aby markdown buňky vysvětlovaly účel

3. **Změny souborů:**
   - Vyhněte se commitování `.env` souborů (použijte `.env.example`)
   - Necommitujte adresáře `venv/` nebo `__pycache__/`
   - Zachovejte výstupy notebooků, pokud demonstrují koncepty
   - Odstraňte dočasné soubory a záložní notebooky (`*-backup.ipynb`)

### Formát názvu PR

Používejte popisné názvy:
- `[Lekce-XX] Přidat nový příklad pro <koncept>`
- `[Oprava] Opravit překlep v lesson-XX README`
- `[Aktualizace] Vylepšit ukázkový kód v lesson-XX`
- `[Dokumentace] Aktualizovat pokyny k nastavení`

### Požadované kontroly

- Notebooky by měly proběhnout bez chyb
- README soubory by měly být jasné a přesné
- Dodržujte existující vzory kódu v repozitáři
- Zachovejte konzistenci s ostatními lekcemi

## Dodatečné poznámky

### Časté problémy

1. **Neshoda verze Pythonu:**
   - Ujistěte se, že používáte Python 3.12+
   - Některé balíčky nemusí fungovat se staršími verzemi
   - Používejte `python3 -m venv` pro explicitní určení verze Pythonu

2. **Proměnné prostředí:**
   - Vždy vytvářejte `.env` ze `.env.example`
   - Necommitujte `.env` soubor (je v `.gitignore`)
   - Přihlaste se pomocí `az login` pro bezklíčovou autentizaci Entra ID

3. **Konflikty balíčků:**
   - Použijte čerstvé virtuální prostředí
   - Instalujte ze souboru `requirements.txt` místo jednotlivých balíčků
   - Některé notebooky mohou vyžadovat další balíčky zmíněné v markdown buňkách

4. **Azure služby:**
   - Azure AI služby vyžadují aktivní předplatné
   - Některé funkce jsou regionálně specifické
   - Ujistěte se, že vaše nasazení modelu Azure OpenAI podporuje Responses API

### Výuková cesta

Doporučené pořadí lekcí:
1. **00-course-setup** - Začněte zde s nastavením prostředí
2. **01-intro-to-ai-agents** - Pochopte základy AI agentů
3. **02-explore-agentic-frameworks** - Naučte se o různých rámcích
4. **03-agentic-design-patterns** - Hlavní návrhové vzory
5. Pokračujte postupně podle číslovaných lekcí

### Výběr rámce

Vyberte rámec podle vašich cílů:
- **Ve všech lekcích**: Microsoft Agent Framework (MAF) s `FoundryChatClient`
- **Agenti se registrují server-side** v Microsoft Foundry Agent Service V2 a jsou vidět v portálu Foundry

### Získání pomoci

- Připojte se k [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Prohlédněte si README soubory lekcí pro konkrétní pokyny
- Podívejte se na hlavní [README.md](./README.md) pro přehled kurzu
- Podívejte se na [Course Setup](./00-course-setup/README.md) pro detailní pokyny k nastavení

### Přispívání

Toto je otevřený vzdělávací projekt. Přispívání vítáno:
- Vylepšujte ukázky kódu
- Opravujte překlepy nebo chyby
- Přidávejte objasňující komentáře
- Navrhujte témata nových lekcí
- Překládejte do dalších jazyků

Viz [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pro aktuální potřeby.

## Kontext specifický pro projekt

### Vícejazyčná podpora

Tento repozitář používá automatizovaný překladatelský systém:
- Podpora 50+ jazyků
- Překlady v adresářích `/translations/<lang-code>/`
- GitHub Actions workflow zajišťuje aktualizace překladů
- Zdrojové soubory jsou v angličtině v kořeni repozitáře

### Struktura lekcí

Každá lekce má konzistentní vzor:
1. Miniatura videa s odkazem
2. Psaný obsah lekce (README.md)
3. Ukázky kódu v různých rámcích
4. Cíle učení a předpoklady
5. Propojené další zdroje k učení

### Pojmenování ukázek kódu

Formát: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekce 1, MAF Python
- `14-sequential.ipynb` - Lekce 14, pokročilé vzory MAF

### Speciální adresáře

- `translated_images/` - Lokalizované obrázky pro překlady
- `images/` - Originální obrázky pro anglický obsah
- `.devcontainer/` - Konfigurace vývojového kontejneru VS Code
- `.github/` - GitHub Actions workflow a šablony

### Závislosti

Klíčové balíčky ze souboru `requirements.txt`:
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