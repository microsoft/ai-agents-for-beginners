# AGENTS.md

## Prehľad projektu

Tento repozitár obsahuje "AI agentov pre začiatočníkov" - komplexný vzdelávací kurz, ktorý učí všetko potrebné na tvorbu AI agentov. Kurz pozostáva z 18 lekcií pokrývajúcich základy, dizajnové vzory, frameworky a produkčné nasadenie AI agentov.

**Kľúčové technológie:**
- Python 3.12+
- Jupyter Notebooks pre interaktívne učenie
- AI Frameworky: Microsoft Agent Framework (MAF)
- Azure AI služby: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architektúra:**
- Struktúra založená na lekciách (adresáre 00-15+)
- Každá lekcia obsahuje: README dokumentáciu, ukážky kódu (Jupyter notebooks) a obrázky
- Podpora viacerých jazykov prostredníctvom automatizovaného systému prekladu
- Jeden Python notebook na lekciu používajúci Microsoft Agent Framework

## Príkazy na nastavenie

### Požiadavky
- Python 3.12 alebo vyšší
- Azure predplatné (pre Azure AI Foundry)
- Nainštalovaný a autentifikovaný Azure CLI (`az login`)

### Počiatočné nastavenie

1. **Klonujte alebo forknite repozitár:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ALEBO
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Vytvorte a aktivujte Python virtuálne prostredie:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Vo Windows: venv\Scripts\activate
   ```

3. **Nainštalujte závislosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nastavte environmentálne premenné:**
   ```bash
   cp .env.example .env
   # Upravte súbor .env so svojimi API kľúčmi a koncovými bodmi
   ```

### Požadované environmentálne premenné

Pre **Azure AI Foundry** (povinné):
- `AZURE_AI_PROJECT_ENDPOINT` - koncový bod Azure AI Foundry projektu
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - názov nasadenia modelu (napr. gpt-4o)

Pre **Azure AI Search** (lekcia 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - koncový bod Azure AI Search
- `AZURE_SEARCH_API_KEY` - API kľúč pre Azure AI Search

Autentifikácia: Spustite `az login` pred spustením notebookov (používa `AzureCliCredential`).

## Vývojový workflow

### Spustenie Jupyter Notebooks

Každá lekcia obsahuje viacero Jupyter notebookov pre rôzne frameworky:

1. **Spustite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Prejdite do adresára lekcie** (napr. `01-intro-to-ai-agents/code_samples/`)

3. **Otvorenie a spustenie notebookov:**
   - `*-python-agent-framework.ipynb` - Použitie Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Použitie Microsoft Agent Framework (.NET)

### Práca s Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Vyžaduje Azure predplatné
- Používa `AzureAIProjectAgentProvider` pre Agent Service V2 (agentov vidno v portáli Foundry)
- Produkčne pripravené s integrovanou observabilitou
- Pattern súborov: `*-python-agent-framework.ipynb`

## Inštrukcie na testovanie

Toto je vzdelávací repozitár s ukážkovým kódom, nie produkčný kód s automatickými testami. Pre overenie nastavenia a zmien:

### Manuálne testovanie

1. **Otestujte Python prostredie:**
   ```bash
   python --version  # Malo by byť 3.12 a viac
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Otestujte spustenie notebooku:**
   ```bash
   # Konvertovať poznámkový blok na skript a spustiť (testuje importy)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Overte environmentálne premenné:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Spustenie jednotlivých notebookov

Otvorte notebooky v Jupyter a vykonávajte bunky postupne. Každý notebook je samostatný a obsahuje:
- Importy
- Načítanie konfigurácie
- Príklady implementácie agentov
- Očakávané výstupy v markdown bunkách

## Štýl kódu

### Python konvencie

- **Verzia Pythonu**: 3.12+
- **Štýl kódu**: Dodržiavajte štandardné PEP 8 pravidlá Pythonu
- **Notebooky**: Používajte prehľadné markdown bunky na vysvetlenie konceptov
- **Importy**: Zoskupujte podľa štandardnej knižnice, tretích strán a lokálnych importov

### Konvencie Jupyter Notebookov

- Zahrňte popisné markdown bunky pred kódom
- Pridajte príklady výstupov v notebookoch na referenciu
- Používajte zrozumiteľné názvy premenných zodpovedajúce konceptom lekcie
- Zachovajte lineárne poradie vykonávania bunky (bunka 1 → 2 → 3...)

### Organizácia súborov

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Build a nasadenie

### Tvorba dokumentácie

Tento repozitár používa Markdown pre dokumentáciu:
- README.md súbory v každom adresári lekcie
- Hlavný README.md v koreňovom adresári repozitára
- Automatizovaný systém prekladu cez GitHub Actions

### CI/CD pipeline

Nachádza sa v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický preklad do 50+ jazykov
2. **welcome-issue.yml** - Privítanie nových tvorcov issue
3. **welcome-pr.yml** - Privítanie nových prispievateľov pull requestov

### Nasadenie

Toto je vzdelávací repozitár - žiadny proces nasadenia. Používatelia:
1. Forknú alebo sklonujú repozitár
2. Spúšťajú notebooky lokálne alebo v GitHub Codespaces
3. Učia sa úpravou a experimentovaním s príkladmi

## Pokyny pre Pull Requesty

### Pred odoslaním

1. **Otestujte svoje zmeny:**
   - Kompletné spustenie ovplyvnených notebookov
   - Overenie, že všetky bunky bežia bez chýb
   - Skontrolujte, či výstupy sú vhodné

2. **Aktualizácie dokumentácie:**
   - Aktualizujte README.md pri pridávaní nových konceptov
   - Pridajte komentáre v notebookoch pri zložitom kóde
   - Zabezpečte, že markdown bunky vysvetľujú účel

3. **Zmeny v súboroch:**
   - Vyhnite sa commitovaniu `.env` súborov (použite `.env.example`)
   - Nekomitujte adresáre `venv/` alebo `__pycache__/`
   - Zachovajte výstupy notebookov, ak demonštrujú koncepty
   - Odstráňte dočasné súbory a záložné notebooky (`*-backup.ipynb`)

### Formát názvu PR

Používajte popisné názvy:
- `[Lesson-XX] Pridanie nového príkladu pre <koncept>`
- `[Fix] Oprava preklepu v lekcii-XX README`
- `[Update] Vylepšenie ukážky kódu v lekcii-XX`
- `[Docs] Aktualizácia inštrukcií na nastavenie`

### Požadované kontroly

- Notebooky by mali bežať bez chýb
- README súbory by mali byť jasné a presné
- Dodržiavajte existujúce kódové vzory v repozitári
- Zachovávajte konzistenciu s ostatnými lekciami

## Dodatočné poznámky

### Bežné úskalia

1. **Nekompatibilita verzie Pythonu:**
   - Zabezpečte použitie Python 3.12+
   - Niektoré balíky nemusia fungovať so staršími verziami
   - Použite `python3 -m venv` pre explicitné nastavenie verzie Pythonu

2. **Environmentálne premenné:**
   - Vždy vytvorte `.env` zo `.env.example`
   - Nekomitujte `.env` (je v `.gitignore`)
   - GitHub token potrebuje správne povolenia

3. **Konflikty balíkov:**
   - Použite nové virtuálne prostredie
   - Inštalujte zo súboru `requirements.txt` namiesto po jednom balíku
   - Niektoré notebooky môžu potrebovať ďalšie balíky uvedené v markdown bunkách

4. **Azure služby:**
   - Azure AI služby vyžadujú aktívne predplatné
   - Niektoré funkcie sú špecifické pre regióny
   - Bezplatné obmedzenia platia pre GitHub Models

### Cesta učenia

Odporúčaný postup lekcií:
1. **00-course-setup** - Začnite tu pre nastavenie prostredia
2. **01-intro-to-ai-agents** - Zoznámte sa so základmi AI agentov
3. **02-explore-agentic-frameworks** - Spoznajte rôzne frameworky
4. **03-agentic-design-patterns** - Základné dizajnové vzory
5. Pokračujte cez očíslované lekcie postupne

### Výber frameworku

Vyberte framework podľa svojich cieľov:
- **Všetky lekcie**: Microsoft Agent Framework (MAF) s `AzureAIProjectAgentProvider`
- **Agenti sa registrujú na serverovej strane** v Azure AI Foundry Agent Service V2 a sú viditeľní v Foundry portáli

### Hľadanie pomoci

- Pridajte sa do [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Preštudujte README súbory lekcií pre špecifické rady
- Pozrite hlavný [README.md](./README.md) pre prehľad kurzu
- Odporúčané nastavenie nájdete v [Course Setup](./00-course-setup/README.md)

### Prispievanie

Toto je otvorený vzdelávací projekt. Príspevky vítané:
- Vylepšovanie ukážok kódu
- Oprava preklepov alebo chýb
- Pridávanie vysvetľujúcich komentárov
- Návrhy na nové témy lekcií
- Preklady do ďalších jazykov

Pozrite [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pre aktuálne potreby.

## Kontext špecifický pre projekt

### Podpora viacerých jazykov

Tento repozitár používa automatizovaný systém prekladu:
- Podpora 50+ jazykov
- Preklady v adresároch `/translations/<lang-code>/`
- GitHub Actions workflow spravuje aktualizácie prekladov
- Zdrojové súbory sú v angličtine v koreňovom adresári repozitára

### Štruktúra lekcie

Každá lekcia má konzistentný vzor:
1. Náhľad videa s odkazom
2. Písaný obsah lekcie (README.md)
3. Ukážky kódu v rôznych frameworkoch
4. Ciele učenia a predpoklady
5. Odkazy na doplnkové vzdelávacie zdroje

### Názvy ukážok kódu

Formát: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcia 1, MAF Python
- `14-sequential.ipynb` - Lekcia 14, MAF pokročilé vzory

### Špeciálne adresáre

- `translated_images/` - Lokalizované obrázky pre preklady
- `images/` - Pôvodné obrázky pre anglický obsah
- `.devcontainer/` - Konfigurácia vývojového kontajnera pre VS Code
- `.github/` - GitHub Actions workflow a šablóny

### Závislosti

Kľúčové balíky zo súboru `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Podpora protokolu agent-to-agent
- `azure-ai-inference`, `azure-ai-projects` - Azure AI služby
- `azure-identity` - Azure autentifikácia (AzureCliCredential)
- `azure-search-documents` - Integrácia Azure AI Search
- `mcp[cli]` - Podpora Model Context Protokołu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->