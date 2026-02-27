# AGENTS.md

## Prehľad projektu

Tento repozitár obsahuje "AI Agentov pre začiatočníkov" - komplexný vzdelávací kurz, ktorý učí všetko potrebné na vytvorenie AI agentov. Kurz sa skladá z viac ako 15 lekcií pokrývajúcich základy, návrhové vzory, frameworky a produkčné nasadenie AI agentov.

**Kľúčové technológie:**
- Python 3.12+
- Jupyter Notebooky pre interaktívne učenie
- AI frameworky: Microsoft Agent Framework (MAF)
- Azure AI služby: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architektúra:**
- Štruktúra založená na lekciách (adresáre 00-15+)
- Každá lekcia obsahuje: dokumentáciu README, ukážky kódu (Jupyter notebooky) a obrázky
- Podpora viacerých jazykov cez automatizovaný prekladový systém
- Jeden Python notebook na lekciu používajúci Microsoft Agent Framework

## Príkazy na nastavenie

### Požiadavky
- Python 3.12 alebo vyšší
- Azure predplatné (pre Azure AI Foundry)
- Azure CLI nainštalované a autentifikované (`az login`)

### Počiatočné nastavenie

1. **Klonujte alebo vytvorte fork repozitára:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ALEBO
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Vytvorte a aktivujte Python virtuálne prostredie:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Vo Windowse: venv\Scripts\activate
   ```

3. **Nainštalujte závislosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nastavte premenné prostredia:**
   ```bash
   cp .env.example .env
   # Upravte .env so svojimi API kľúčmi a koncovými bodmi
   ```

### Povinné premenné prostredia

Pre **Azure AI Foundry** (vyžaduje sa):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint projektu Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - meno nasadenia modelu (napr. gpt-4o)

Pre **Azure AI Search** (Lekcia 05 – RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - API kľúč Azure AI Search

Autentifikácia: Spustite `az login` pred spustením notebookov (používa `AzureCliCredential`).

## Vývojový pracovný postup

### Spustenie Jupyter notebookov

Každá lekcia obsahuje niekoľko Jupyter notebookov pre rôzne frameworky:

1. **Spustite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Prejdite do adresára lekcie** (napr. `01-intro-to-ai-agents/code_samples/`)

3. **Otvorte a spustite notebooky:**
   - `*-python-agent-framework.ipynb` - Použitie Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Použitie Microsoft Agent Framework (.NET)

### Práca s Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Vyžaduje Azure predplatné
- Používa `AzureAIProjectAgentProvider` pre Agent Service V2 (agenti viditeľní v portáli Foundry)
- Produkčne pripravené s integrovanou pozorovateľnosťou
- Vzor súborov: `*-python-agent-framework.ipynb`

## Inštrukcie na testovanie

Toto je vzdelávací repozitár s príkladovým kódom, nie produkčný kód s automatizovanými testami. Na overenie nastavenia a zmien:

### Manuálne testovanie

1. **Otestujte Python prostredie:**
   ```bash
   python --version  # Malo by byť 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Otestujte vykonanie notebooku:**
   ```bash
   # Preveďte poznámkový blok na skript a spustite ho (testuje importy)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Overte premenné prostredia:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Spustenie jednotlivých notebookov

Otvorte notebooky v Jupyter a vykonávajte bunky sekvenčne. Každý notebook je samostatný a obsahuje:
- Importy
- Načítanie konfigurácie
- Príklady implementácie agentov
- Očakávané výstupy v markdown bunkách

## Štýl kódu

### Python konvencie

- **Verzia Pythonu:** 3.12+
- **Štýl kódu:** Dodržiavajte štandardné Python PEP 8 konvencie
- **Notebooky:** Používajte jasné markdown bunky na vysvetlenie konceptov
- **Importy:** Zoraďte podľa štandardnej knižnice, tretích strán a lokálnych importov

### Jupyter Notebook konvencie

- Zahrňte popisné markdown bunky pred kódovými bunkami
- Pridajte príklady výstupov v notebookoch na referenciu
- Používajte jasné názvy premenných zodpovedajúce konceptom lekcie
- Udržiavajte lineárne poradie vykonávania notebooku (bunka 1 → 2 → 3...)

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

## Kompilácia a nasadenie

### Tvorba dokumentácie

Tento repozitár používa Markdown pre dokumentáciu:
- Súbory README.md v každom adresári lekcie
- Hlavný README.md v koreňovom adresári
- Automatizovaný prekladový systém cez GitHub Actions

### CI/CD Pipeline

Nachádza sa v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický preklad do viac ako 50 jazykov
2. **welcome-issue.yml** - Privítanie nových tvorcov issue
3. **welcome-pr.yml** - Privítanie nových prispievateľov pull requestov

### Nasadenie

Toto je vzdelávací repozitár - žiadny proces nasadenia. Používatelia:
1. Vytvoria fork alebo naklonujú repozitár
2. Spúšťajú notebooky lokálne alebo v GitHub Codespaces
3. Učia sa modifikáciou a experimentovaním s príkladmi

## Pokyny pre pull requesty

### Pred odoslaním

1. **Otestujte svoje zmeny:**
   - Spustite úplne dotknuté notebooky
   - Overte, že všetky bunky sa vykonávajú bez chýb
   - Skontrolujte, či sú výstupy vhodné

2. **Aktualizácie dokumentácie:**
   - Aktualizujte README.md ak pridávate nové koncepty
   - Pridajte komentáre do notebookov pri zložitejšom kóde
   - Zaistite, že markdown bunky vysvetľujú účel

3. **Zmeny v súboroch:**
   - Necommitujte `.env` súbory (používajte `.env.example`)
   - Necommitujte adresáre `venv/` alebo `__pycache__/`
   - Zachovajte výstupy notebookov, keď demonštrujú koncepty
   - Odstráňte dočasné a záložné notebooky (`*-backup.ipynb`)

### Formát názvov PR

Používajte popisné názvy:
- `[Lesson-XX] Pridanie nového príkladu pre <koncept>`
- `[Fix] Oprava preklepu v README lekcie-XX`
- `[Update] Vylepšenie ukážky kódu v lekcii-XX`
- `[Docs] Aktualizácia inštrukcií na nastavenie`

### Povinné kontroly

- Notebooky sa musia spustiť bez chýb
- README súbory by mali byť jasné a presné
- Dodržujte existujúce kódové vzory v repozitári
- Zachovajte konzistentnosť s ostatnými lekciami

## Ďalšie poznámky

### Bežné problémy

1. **Nesúlad verzie Pythonu:**
   - Používajte Python 3.12+
   - Niektoré balíčky nemusia fungovať s staršími verziami
   - Použite `python3 -m venv` pre explicitné určenie verzie Pythonu

2. **Premenné prostredia:**
   - Vždy vytvorte `.env` zo súboru `.env.example`
   - `.env` necommitujte (je v `.gitignore`)
   - GitHub token vyžaduje príslušné oprávnenia

3. **Konflikty balíčkov:**
   - Použite čisté virtuálne prostredie
   - Inštalujte zo súboru `requirements.txt`, nie jednotlivé balíčky
   - Niektoré notebooky môžu potrebovať ďalšie balíčky uvedené v markdown bunkách

4. **Azure služby:**
   - Azure AI služby vyžadujú aktívne predplatné
   - Niektoré funkcie sú závislé od regiónu
   - Zdarma tier má obmedzenia pre GitHub Models

### Cesta učenia

Odporúčané poradie lekcií:
1. **00-course-setup** - Začnite tu s nastavením prostredia
2. **01-intro-to-ai-agents** - Pochopenie základov AI agentov
3. **02-explore-agentic-frameworks** - Naučte sa o rôznych frameworkoch
4. **03-agentic-design-patterns** - Základné návrhové vzory
5. Pokračujte v číslovaných lekciách postupne

### Výber frameworku

Vyberte si framework podľa cieľov:
- **Všetky lekcie**: Microsoft Agent Framework (MAF) s `AzureAIProjectAgentProvider`
- **Agenti sa registrujú na serveri** v Azure AI Foundry Agent Service V2 a sú viditeľní v portáli Foundry

### Ako získať pomoc

- Pridajte sa do [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Prezrite si README súbory lekcií pre konkrétne návody
- Skontrolujte hlavný [README.md](./README.md) s prehľadom kurzu
- Odkaz na [Course Setup](./00-course-setup/README.md) s podrobnými inštrukciami na nastavenie

### Prínos

Toto je otvorený vzdelávací projekt. Príspevky sú vítané:
- Zlepšenie príkladov kódu
- Oprava preklepov alebo chýb
- Pridávanie vysvetľujúcich komentárov
- Navrhovanie nových tém lekcií
- Preklady do ďalších jazykov

Pozrite si [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pre aktuálne potreby.

## Kontext projektu

### Podpora viacerých jazykov

Tento repozitár používa automatizovaný prekladový systém:
- Podpora viac ako 50 jazykov
- Preklady v adresároch `/translations/<lang-code>/`
- Prekladové aktualizácie spravuje GitHub Actions workflow
- Zdrojové súbory sú v angličtine v koreňovom adresári

### Štruktúra lekcií

Každá lekcia nasleduje konzistentný vzor:
1. Náhľad videa s odkazom
2. Písaný obsah lekcie (README.md)
3. Ukážky kódu v rôznych frameworkoch
4. Ciele učenia a požiadavky
5. Dodatočné učebné zdroje s odkazmi

### Názvoslovie ukážok kódu

Formát: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcia 1, MAF Python
- `14-sequential.ipynb` - Lekcia 14, MAF pokročilé vzory

### Špeciálne adresáre

- `translated_images/` - lokalizované obrázky pre preklady
- `images/` - originálne obrázky pre anglický obsah
- `.devcontainer/` - konfigurácia VS Code vývojového kontajnera
- `.github/` - workflowy a šablóny GitHub Actions

### Závislosti

Kľúčové balíčky zo súboru `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - podpora protokolu agent-to-agent
- `azure-ai-inference`, `azure-ai-projects` - Azure AI služby
- `azure-identity` - Azure autentifikácia (AzureCliCredential)
- `azure-search-documents` - integrácia Azure AI Search
- `mcp[cli]` - podpora Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vylúčenie zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by sa mal považovať za autoritatívny zdroj. Pri dôležitých informáciách sa odporúča využiť profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->