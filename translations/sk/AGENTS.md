# AGENTS.md

## Prehľad projektu

Tento repozitár obsahuje "AI Agentov pre začiatočníkov" - komplexný vzdelávací kurz, ktorý učí všetko potrebné na vytváranie AI agentov. Kurz pozostáva z viac ako 15 lekcií pokrývajúcich základné princípy, návrhové vzory, frameworky a produkčné nasadenie AI agentov.

**Kľúčové technológie:**
- Python 3.12+
- Jupyter Notebooks pre interaktívne učenie
- AI frameworky: Microsoft Agent Framework (MAF)
- Azure AI služby: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architektúra:**
- Štruktúra založená na lekciách (adresáre 00-15+)
- Každá lekcia obsahuje: dokumentáciu README, ukážky kódu (Jupyter notebooky) a obrázky
- Podpora viacerých jazykov cez automatizovaný prekladový systém
- Jeden Python notebook na lekciu používajúci Microsoft Agent Framework

## Príkazy na nastavenie

### Predpoklady
- Python 3.12 alebo vyšší
- Predplatné Azure (pre Azure AI Foundry)
- Nainštalovaný a autentifikovaný Azure CLI (`az login`)

### Počiatočné nastavenie

1. **Klonujte alebo forknete repozitár:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ALEBO
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Vytvorte a aktivujte Python virtuálne prostredie:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Na Windows: venv\Scripts\activate
   ```

3. **Nainštalujte závislosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nastavte premenné prostredia:**
   ```bash
   cp .env.example .env
   # Upraviť .env so svojimi API kľúčmi a koncovými bodmi
   ```

### Požadované premenné prostredia

Pre **Azure AI Foundry** (Povinné):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint projektu Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - názov deploymentu modelu (napr. gpt-4o)

Pre **Azure AI Search** (Lekcia 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - API kľúč Azure AI Search

Autentifikácia: Pred spustením notebookov spustite `az login` (používa sa `AzureCliCredential`).

## Vývojový workflow

### Spustenie Jupyter notebookov

Každá lekcia obsahuje viacero Jupyter notebookov pre rôzne frameworky:

1. **Spustite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Prejdite do adresára s lekciou** (napr. `01-intro-to-ai-agents/code_samples/`)

3. **Otvorte a spustite notebooky:**
   - `*-python-agent-framework.ipynb` - Použitie Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Použitie Microsoft Agent Framework (.NET)

### Práca s Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Vyžaduje predplatné Azure
- Používa `AzureAIProjectAgentProvider` pre Agent Service V2 (agenti viditeľní v portáli Foundry)
- Pripravené na produkciu s integrovanou sledovateľnosťou
- Vzor súboru: `*-python-agent-framework.ipynb`

## Inštrukcie na testovanie

Toto je vzdelávací repozitár s ukážkovým kódom, nie produkčný kód s automatizovanými testami. Na overenie nastavenia a zmien:

### Manuálne testovanie

1. **Otestujte Python prostredie:**
   ```bash
   python --version  # Malo by to byť 3.12 a vyššie
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Otestujte spustenie notebooku:**
   ```bash
   # Konvertujte zošit na skript a spustite (testuje importy)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Overte premenné prostredia:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Spustenie jednotlivých notebookov

Otvorte notebooky v Jupyter a vykonávajte bunky postupne. Každý notebook je samostatný a obsahuje:
- Importy
- Načítanie konfigurácie
- Príklady implementácií agentov
- Očakávané výstupy v markdown bunkách

## Štýl kódu

### Python konvencie

- **Verzia Pythonu**: 3.12+
- **Štýl kódu**: Dodržiavať štandardné Python PEP 8 konvencie
- **Notebooky**: Používať jasné markdown bunky na vysvetlenie konceptov
- **Importy**: Zoskupiť podľa std knižnice, tretích strán a lokálnych importov

### Konvencie Jupyter notebookov

- Zahrnúť popisné markdown bunky pred kódovými bunkami
- Pridávať príklady výstupov v notebookoch ako referenciu
- Používať jasné názvy premenných zodpovedajúce konceptom lekcie
- Udržiavať lineárny poriadok vykonávania buniek (bunka 1 → 2 → 3...)

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

## Stavba a nasadenie

### Tvorba dokumentácie

Tento repozitár používa Markdown pre dokumentáciu:
- README.md súbory v každom priečinku lekcie
- Hlavný README.md v koreňovom adresári repozitára
- Automatizovaný prekladový systém cez GitHub Actions

### CI/CD pipeline

Nachádza sa v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický preklad do viac ako 50 jazykov
2. **welcome-issue.yml** - Privítanie nových autorov issue
3. **welcome-pr.yml** - Privítanie nových prispievateľov pull requestov

### Nasadenie

Ide o vzdelávací repozitár - žiadny proces nasadenia. Používatelia:
1. Forkujú alebo klonujú repozitár
2. Spúšťajú notebooky lokálne alebo v GitHub Codespaces
3. Učia sa úpravou a experimentovaním s príkladmi

## Pokyny pre pull requesty

### Pred odoslaním

1. **Otestujte svoje zmeny:**
   - Spustiť kompletne ovplyvnené notebooky
   - Overiť, že všetky bunky bežia bez chýb
   - Skontrolovať, či výstupy zodpovedajú očakávaniam

2. **Aktualizácie dokumentácie:**
   - Aktualizovať README.md, ak pridávate nové koncepty
   - Pridať komentáre do notebookov pre zložitejšie časti kódu
   - Zaistiť, že markdown bunky vysvetľujú účel

3. **Zmeny v súboroch:**
   - Neposielať `.env` súbory (používať `.env.example`)
   - Neposielať adresáre `venv/` alebo `__pycache__/`
   - Uchovať výstupy notebookov, ak demonštrujú koncepty
   - Odstrániť dočasné súbory a zálohované notebooky (`*-backup.ipynb`)

### Formát názvu PR

Používajte popisné názvy:
- `[Lesson-XX] Pridať nový príklad pre <concept>`
- `[Fix] Opraviť preklep v README lekcie-XX`
- `[Update] Vylepšiť ukážku kódu v lekcii-XX`
- `[Docs] Aktualizovať inštrukcie na nastavenie`

### Povinné kontroly

- Notebooky by mali bežať bez chýb
- README súbory musia byť jasné a presné
- Dodržiavajte existujúce vzory kódu v repozitári
- Udržiavať konzistentnosť s ostatnými lekciami

## Dodatočné poznámky

### Bežné problémy

1. **Nekompatibilita verzie Pythonu:**
   - Použiť Python 3.12+ 
   - Niektoré balíčky nemusia fungovať so staršími verziami
   - Použiť `python3 -m venv` na explicitné nastavenie verzie

2. **Premenné prostredia:**
   - Vždy vytvoriť `.env` zo `.env.example`
   - Neposielať `.env` (je v `.gitignore`)
   - GitHub token vyžaduje príslušné oprávnenia

3. **Konflikty balíčkov:**
   - Použiť čisté virtuálne prostredie
   - Inštalovať z `requirements.txt` a nie jednotlivé balíčky
   - Niektoré notebooky môžu vyžadovať ďalšie balíčky uvedené v markdown bunkách

4. **Azure služby:**
   - Azure AI služby vyžadujú aktívne predplatné
   - Niektoré funkcie sú regiónovo obmedzené
   - Bezplatný režim sa vzťahuje na GitHub Models

### Učebná cesta

Odporúčané poradie lekcií:
1. **00-course-setup** - Začnite tu s nastavením prostredia
2. **01-intro-to-ai-agents** - Základy AI agentov
3. **02-explore-agentic-frameworks** - Prehľad rôznych frameworkov
4. **03-agentic-design-patterns** - Základné návrhové vzory
5. Pokračujte ďalej podľa číslovania lekcií

### Výber frameworku

Vyberte framework podľa cieľov:
- **Všetky lekcie**: Microsoft Agent Framework (MAF) s `AzureAIProjectAgentProvider`
- **Agenti sa registrujú server-side** v Azure AI Foundry Agent Service V2 a sú viditeľní v portáli Foundry

### Kde hľadať pomoc

- Pripojte sa k [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Prezrite si README súbory k lekciám pre špecifické usmernenia
- Prečítať hlavný [README.md](./README.md) s prehľadom kurzu
- Pozrieť [Course Setup](./00-course-setup/README.md) pre podrobné inštrukcie nastavenia

### Prispievanie

Toto je otvorený vzdelávací projekt. Príspevky vítané:
- Vylepšenie ukážok kódu
- Oprava preklepov alebo chýb
- Pridanie vysvetľujúcich komentárov
- Návrhy na nové témy lekcií
- Preklady do ďalších jazykov

Pozrite [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pre aktuálne potreby.

## Kontext projektu

### Podpora viacerých jazykov

Tento repozitár používa automatizovaný prekladový systém:
- Podpora viac ako 50 jazykov
- Preklady v adresároch `/translations/<lang-code>/`
- Aktualizácie prekladov cez GitHub Actions workflow
- Zdrojové súbory sú v angličtine v koreňovom priečinku repozitára

### Štruktúra lekcií

Každá lekcia nasleduje konzistentný vzor:
1. Videonáhľad s odkazom
2. Písaný obsah lekcie (README.md)
3. Ukážky kódu vo viacerých frameworkoch
4. Ciele učenia a predpoklady
5. Doplnkové zdroje na učenie s odkazmi

### Názvy ukážok kódu

Formát: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcia 1, MAF Python
- `14-sequential.ipynb` - Lekcia 14, pokročilé vzory MAF

### Špeciálne adresáre

- `translated_images/` - lokalizované obrázky pre preklady
- `images/` - originálne obrázky pre anglický obsah
- `.devcontainer/` - konfigurácia vývojového kontajnera VS Code
- `.github/` - GitHub Actions workflowy a šablóny

### Závislosti

Kľúčové balíčky z `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - podpora protokolu Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Azure AI služby
- `azure-identity` - Azure autentifikácia (AzureCliCredential)
- `azure-search-documents` - integrácia Azure AI Search
- `mcp[cli]` - podpora Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vylúčenie zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->