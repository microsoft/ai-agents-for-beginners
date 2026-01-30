# AGENTS.md

## Prehľad projektu

Tento repozitár obsahuje kurz "AI Agenti pre začiatočníkov" - komplexný vzdelávací kurz, ktorý učí všetko potrebné na vytvorenie AI agentov. Kurz pozostáva z viac ako 15 lekcií, ktoré pokrývajú základy, návrhové vzory, rámce a nasadenie AI agentov do produkcie.

**Kľúčové technológie:**
- Python 3.12+
- Jupyter Notebooks pre interaktívne učenie
- AI rámce: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI služby: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (dostupná bezplatná verzia)

**Architektúra:**
- Štruktúra založená na lekciách (00-15+ adresáre)
- Každá lekcia obsahuje: README dokumentáciu, ukážky kódu (Jupyter notebooks) a obrázky
- Podpora viacerých jazykov prostredníctvom automatizovaného prekladacieho systému
- Viacero možností rámcov pre každú lekciu (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Príkazy na nastavenie

### Predpoklady
- Python 3.12 alebo vyšší
- GitHub účet (pre GitHub Models - bezplatná verzia)
- Azure predplatné (voliteľné, pre Azure AI služby)

### Počiatočné nastavenie

1. **Naklonujte alebo vytvorte fork repozitára:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Vytvorte a aktivujte Python virtuálne prostredie:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Nainštalujte závislosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nastavte environmentálne premenné:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Požadované environmentálne premenné

Pre **GitHub Models (bezplatné)**:
- `GITHUB_TOKEN` - Osobný prístupový token z GitHubu

Pre **Azure AI služby** (voliteľné):
- `PROJECT_ENDPOINT` - Endpoint projektu Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - API kľúč pre Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL endpointu Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Názov nasadenia pre chat model
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Názov nasadenia pre embeddings
- Ďalšie konfigurácie Azure, ako je uvedené v `.env.example`

## Pracovný postup vývoja

### Spustenie Jupyter Notebooks

Každá lekcia obsahuje viacero Jupyter notebookov pre rôzne rámce:

1. **Spustite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Prejdite do adresára lekcie** (napr. `01-intro-to-ai-agents/code_samples/`)

3. **Otvorte a spustite notebooky:**
   - `*-semantic-kernel.ipynb` - Použitie rámca Semantic Kernel
   - `*-autogen.ipynb` - Použitie rámca AutoGen
   - `*-python-agent-framework.ipynb` - Použitie Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Použitie Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Použitie Azure AI Agent Service

### Práca s rôznymi rámcami

**Semantic Kernel + GitHub Models:**
- Dostupná bezplatná verzia s GitHub účtom
- Vhodné na učenie a experimentovanie
- Vzor súboru: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Dostupná bezplatná verzia s GitHub účtom
- Schopnosti orchestrácie viacerých agentov
- Vzor súboru: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Najnovší rámec od Microsoftu
- Dostupný v Python a .NET
- Vzor súboru: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Vyžaduje Azure predplatné
- Funkcie pripravené na produkciu
- Vzor súboru: `*-azureaiagent.ipynb`

## Pokyny na testovanie

Toto je vzdelávací repozitár s ukážkovým kódom, nie produkčný kód s automatizovanými testami. Na overenie nastavenia a zmien:

### Manuálne testovanie

1. **Otestujte Python prostredie:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Otestujte spustenie notebookov:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Overte environmentálne premenné:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Spustenie jednotlivých notebookov

Otvorte notebooky v Jupyter a postupne vykonávajte bunky. Každý notebook je samostatný a obsahuje:
- Importy
- Načítanie konfigurácie
- Ukážky implementácie agentov
- Očakávané výstupy v markdown bunkách

## Štýl kódu

### Python konvencie

- **Verzia Pythonu**: 3.12+
- **Štýl kódu**: Dodržiavajte štandardné Python PEP 8 konvencie
- **Notebooky**: Používajte jasné markdown bunky na vysvetlenie konceptov
- **Importy**: Skupinujte podľa štandardnej knižnice, tretích strán, lokálnych importov

### Konvencie Jupyter Notebookov

- Zahrňte popisné markdown bunky pred bunkami s kódom
- Pridajte príklady výstupov v notebookoch na referenciu
- Používajte jasné názvy premenných, ktoré zodpovedajú konceptom lekcie
- Udržujte lineárny poriadok vykonávania notebookov (bunka 1 → 2 → 3...)

### Organizácia súborov

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

## Build a nasadenie

### Tvorba dokumentácie

Tento repozitár používa Markdown na dokumentáciu:
- README.md súbory v každom adresári lekcie
- Hlavný README.md v koreňovom adresári repozitára
- Automatizovaný prekladací systém prostredníctvom GitHub Actions

### CI/CD Pipeline

Nachádza sa v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický preklad do viac ako 50 jazykov
2. **welcome-issue.yml** - Privítanie nových tvorcov issue
3. **welcome-pr.yml** - Privítanie nových prispievateľov pull requestov

### Nasadenie

Toto je vzdelávací repozitár - žiadny proces nasadenia. Používatelia:
1. Vytvoria fork alebo naklonujú repozitár
2. Spustia notebooky lokálne alebo v GitHub Codespaces
3. Učia sa úpravou a experimentovaním s príkladmi

## Pokyny pre pull requesty

### Pred odoslaním

1. **Otestujte svoje zmeny:**
   - Úplne spustite ovplyvnené notebooky
   - Overte, že všetky bunky sa vykonajú bez chýb
   - Skontrolujte, či sú výstupy vhodné

2. **Aktualizácie dokumentácie:**
   - Aktualizujte README.md, ak pridávate nové koncepty
   - Pridajte komentáre v notebookoch pre zložitý kód
   - Uistite sa, že markdown bunky vysvetľujú účel

3. **Zmeny súborov:**
   - Vyhnite sa commitovaniu `.env` súborov (použite `.env.example`)
   - Necommitujte adresáre `venv/` alebo `__pycache__/`
   - Zachovajte výstupy notebookov, keď demonštrujú koncepty
   - Odstráňte dočasné súbory a záložné notebooky (`*-backup.ipynb`)

### Formát názvu PR

Používajte popisné názvy:
- `[Lesson-XX] Pridanie novej ukážky pre <koncept>`
- `[Fix] Oprava preklepu v README lekcie-XX`
- `[Update] Zlepšenie ukážky kódu v lekcii-XX`
- `[Docs] Aktualizácia pokynov na nastavenie`

### Požadované kontroly

- Notebooky by sa mali vykonávať bez chýb
- README súbory by mali byť jasné a presné
- Dodržiavajte existujúce vzory kódu v repozitári
- Zachovajte konzistenciu s ostatnými lekciami

## Dodatočné poznámky

### Bežné problémy

1. **Nesúlad verzie Pythonu:**
   - Uistite sa, že používate Python 3.12+
   - Niektoré balíky nemusia fungovať so staršími verziami
   - Použite `python3 -m venv` na explicitné určenie verzie Pythonu

2. **Environmentálne premenné:**
   - Vždy vytvorte `.env` zo `.env.example`
   - Necommitujte `.env` súbor (je v `.gitignore`)
   - GitHub token potrebuje vhodné oprávnenia

3. **Konflikty balíkov:**
   - Použite nové virtuálne prostredie
   - Inštalujte z `requirements.txt` namiesto jednotlivých balíkov
   - Niektoré notebooky môžu vyžadovať ďalšie balíky uvedené v ich markdown bunkách

4. **Azure služby:**
   - Azure AI služby vyžadujú aktívne predplatné
   - Niektoré funkcie sú špecifické pre región
   - Obmedzenia bezplatnej verzie platia pre GitHub Models

### Učebná cesta

Odporúčaný postup cez lekcie:
1. **00-course-setup** - Začnite tu s nastavením prostredia
2. **01-intro-to-ai-agents** - Pochopte základy AI agentov
3. **02-explore-agentic-frameworks** - Naučte sa o rôznych rámcoch
4. **03-agentic-design-patterns** - Základné návrhové vzory
5. Pokračujte cez očíslované lekcie postupne

### Výber rámca

Vyberte rámec podľa svojich cieľov:
- **Učenie/Prototypovanie**: Semantic Kernel + GitHub Models (bezplatné)
- **Systémy viacerých agentov**: AutoGen
- **Najnovšie funkcie**: Microsoft Agent Framework (MAF)
- **Nasadenie do produkcie**: Azure AI Agent Service

### Získanie pomoci

- Pripojte sa k [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Prezrite si README súbory lekcií pre konkrétne pokyny
- Skontrolujte hlavný [README.md](./README.md) pre prehľad kurzu
- Pozrite si [Course Setup](./00-course-setup/README.md) pre podrobné pokyny na nastavenie

### Prispievanie

Toto je otvorený vzdelávací projekt. Príspevky sú vítané:
- Zlepšenie ukážok kódu
- Oprava preklepov alebo chýb
- Pridanie objasňujúcich komentárov
- Návrh nových tém lekcií
- Preklad do ďalších jazykov

Pozrite si [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pre aktuálne potreby.

## Kontext špecifický pre projekt

### Podpora viacerých jazykov

Tento repozitár používa automatizovaný prekladací systém:
- Podpora viac ako 50 jazykov
- Preklady v adresároch `/translations/<lang-code>/`
- GitHub Actions workflow spracováva aktualizácie prekladov
- Zdrojové súbory sú v angličtine v koreňovom adresári repozitára

### Štruktúra lekcií

Každá lekcia nasleduje konzistentný vzor:
1. Náhľad videa s odkazom
2. Písomný obsah lekcie (README.md)
3. Ukážky kódu v rôznych rámcoch
4. Ciele učenia a predpoklady
5. Odkazy na ďalšie vzdelávacie zdroje

### Názvy ukážok kódu

Formát: `<číslo-lekcie>-<názov-rámca>.ipynb`
- `04-semantic-kernel.ipynb` - Lekcia 4, Semantic Kernel
- `07-autogen.ipynb` - Lekcia 7, AutoGen
- `14-python-agent-framework.ipynb` - Lekcia 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Lekcia 14, MAF .NET

### Špeciálne adresáre

- `translated_images/` - Lokalizované obrázky pre preklady
- `images/` - Pôvodné obrázky pre obsah v angličtine
- `.devcontainer/` - Konfigurácia vývojového kontajnera pre VS Code
- `.github/` - GitHub Actions workflowy a šablóny

### Závislosti

Kľúčové balíky z `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen rámec
- `semantic-kernel` - Semantic Kernel rámec
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI služby
- `azure-search-documents` - Integrácia Azure AI Search
- `chromadb` - Vektorová databáza pre RAG príklady
- `chainlit` - Chat UI rámec
- `browser_use` - Automatizácia prehliadača pre agentov
- `mcp[cli]` - Podpora Model Context Protocol
- `mem0ai` - Správa pamäte pre agentov

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.