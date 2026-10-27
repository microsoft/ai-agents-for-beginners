# AGENTS.md

## Prehľad projektu

Tento repozitár obsahuje "AI Agentov pre Začiatočníkov" - komplexný vzdelávací kurz, ktorý učí všetko potrebné na vytvorenie AI Agentov. Kurz pozostáva z 18 lekcií (číslovaných 00-18), ktoré pokrývajú základy, návrhové vzory, frameworky, nasadenie do produkcie, lokálnych/na zariadení agentov a bezpečnosť AI agentov.

**Kľúčové technológie:**
- Python 3.12+
- Jupyter Notebooky pre interaktívne učenie
- AI Frameworky: Microsoft Agent Framework (MAF)
- Azure AI služby: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektúra:**
- Štruktúra založená na lekciách (adresáre 00-18)
- Každá lekcia obsahuje: dokumentáciu README, ukážky kódu (Jupyter notebooky) a obrázky
- Podpora viacerých jazykov pomocou automatizovaného prekladového systému
- Jeden Python notebook na lekciu používajúci Microsoft Agent Framework

## Príkazy na nastavenie

### Požiadavky
- Python 3.12 alebo vyšší
- Predplatné Azure (pre Microsoft Foundry)
- Nainštalovaný a autentifikovaný Azure CLI (`az login`)

### Počiatočné nastavenie

1. **Klonujte alebo forknite repozitár:**
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

4. **Nastavte premenné prostredia:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Povinné premenné prostredia

Pre **Microsoft Foundry** (povinné):
- `AZURE_AI_PROJECT_ENDPOINT` - Endpoint projektu Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Názov nasadenia modelu (napr. gpt-5-mini)

Pre **Azure AI Search** (Lekcia 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - API kľúč Azure AI Search

Autentifikácia: Spustite `az login` pred spustením notebookov (používa `AzureCliCredential`).

## Vývojový pracovný tok

### Spustenie Jupyter notebookov

Každá lekcia obsahuje viacero Jupyter notebookov pre rôzne frameworky:

1. **Spustite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Prejdite do adresára lekcie** (napr. `01-intro-to-ai-agents/code_samples/`)

3. **Otvorte a spustite notebooky:**
   - `*-python-agent-framework.ipynb` - Pomocou Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Pomocou Microsoft Agent Framework (.NET)

### Práca s Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Vyžaduje predplatné Azure
- Používa `FoundryChatClient` pre Agent Service V2 (agenti viditeľní v portáli Foundry)
- Produkčný pripravený so zabudovanou pozorovateľnosťou
- Vzor súboru: `*-python-agent-framework.ipynb`

## Inštrukcie na testovanie

Toto je vzdelávací repozitár s ukážkovým kódom, nie produkčný kód s automatizovanými testami. Na overenie nastavenia a zmien:

### Manuálne testovanie

1. **Otestujte Python prostredie:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Otestujte vykonávanie notebooku:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Overte premenné prostredia:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Spustenie jednotlivých notebookov

Otvorte notebooky v Jupyter a vykonávajte bunky postupne. Každý notebook je samostatný a obsahuje:
- Importy
- Načítanie konfigurácie
- Príklady implementácií agentov
- Očakávané výstupy v markdown bunkách

### Smoke-testovanie nasadených agentov

Pre lekcie, kde je agent nasadený ako Microsoft Foundry hostovaný agent (01, 04, 05, 16), repozitár obsahuje smoke-test katalógy pod `tests/`, ktoré sú spúšťané workflow `.github/workflows/smoke-test.yml` cez akciu [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Sú to ľahké povinné testy po nasadení (je agent dosiahnuteľný a vyhovuje základným očakávaniam promptov?), dopĺňajúce evaluačný pipeline v lekciách 10 a 16. Pozrite [tests/README.md](./tests/README.md) pre mapovanie katalóg-lekcia-agent. Lekcia 17 beží lokálne s Foundry Local a nemá hostovaný endpoint, preto je overená priamym spustením svojho notebooku.

## Štýl kódu

### Python konvencie

- **Verzia Pythonu**: 3.12+
- **Štýl kódu**: Dodržiavajte štandardné Python PEP 8 konvencie
- **Notebooky**: Používajte jasné markdown bunky na vysvetlenie konceptov
- **Importy**: Zoskupujte podľa štandardnej knižnice, tretích strán, lokálnych importov

### Konvencie Jupyter Notebookov

- Zahrňujte popisné markdown bunky pred kódom
- Pridávajte príklady výstupov v notebookoch pre referenciu
- Používajte jasné názvy premenných zodpovedajúce konceptom lekcií
- Zachovajte lineárny poriadok spúšťania notebooku (bunka 1 → 2 → 3...)

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
- Hlavný README.md v koreňovom adresári repozitára
- Automatizovaný prekladový systém cez GitHub Actions

### CI/CD pipeline

Nachádza sa v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický preklad do 50+ jazykov
2. **welcome-issue.yml** - Privítanie tvorcov nových issue
3. **welcome-pr.yml** - Privítanie nových prispievateľov pull requestov

### Nasadenie

Toto je vzdelávací repozitár - žiadny proces nasadenia. Používatelia:
1. Forknú alebo sklonujú repozitár
2. Spúšťajú notebooky lokálne alebo v GitHub Codespaces
3. Učia sa úpravou a experimentovaním s ukážkami

## Pokyny pre Pull Requesty

### Pred odoslaním

1. **Otestujte svoje zmeny:**
   - Kompletné spustenie dotknutých notebookov
   - Overenie, že všetky bunky vykonajú bez chýb
   - Skontrolujte, či výstupy sú vhodné

2. **Aktualizácie dokumentácie:**
   - Aktualizujte README.md pri pridávaní nových konceptov
   - Pridajte komentáre do notebookov pre komplikovaný kód
   - Zabezpečte, aby markdown bunky vysvetľovali účel

3. **Zmeny súborov:**
   - Vyhnite sa commitovaniu `.env` súborov (používajte `.env.example`)
   - Necommitujte adresáre `venv/` alebo `__pycache__/`
   - Zachovajte výstupy v notebookoch pri demonštrácii konceptov
   - Odstráňte dočasné súbory a záložné notebooky (`*-backup.ipynb`)

### Formát názvu PR

Používajte popisné názvy:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Povinné kontroly

- Notebooky by mali bežať bez chýb
- README súbory by mali byť jasné a presné
- Dodržiavať existujúce vzory kódu v repozitári
- Zachovať konzistentnosť s ostatnými lekciami

## Dodatočné poznámky

### Bežné problémy

1. **Nesúlad verzií Pythonu:**
   - Používajte Python 3.12+
   - Niektoré balíky nemusia fungovať so staršími verziami
   - Použite `python3 -m venv` na explicitné určenie verzie Pythonu

2. **Premenné prostredia:**
   - Vždy vytvárajte `.env` z `.env.example`
   - Necommitujte súbor `.env` (je v `.gitignore`)
   - Pri autentifikácii bez kľúča použite prihlásenie cez `az login` pre Entra ID

3. **Konflikty balíkov:**
   - Používajte čerstvé virtuálne prostredie
   - Inštalujte z `requirements.txt` namiesto jednotlivých balíkov
   - Niektoré notebooky môžu vyžadovať ďalšie balíky uvedené v ich markdown bunkách

4. **Azure služby:**
   - Azure AI služby vyžadujú aktívne predplatné
   - Niektoré funkcie sú špecifické pre regióny
   - Overte, či váš Azure OpenAI model nasadenia podporuje Responses API

### Cesta učenia

Odporúčaný postup lekcií:
1. **00-course-setup** - Začnite tu, aby ste nastavili prostredie
2. **01-intro-to-ai-agents** - Pochopte základy AI agentov
3. **02-explore-agentic-frameworks** - Naučte sa o rôznych frameworkoch
4. **03-agentic-design-patterns** - Základné návrhové vzory
5. Pokračujte postupne cez číslované lekcie

### Výber frameworku

Vyberte framework podľa svojich cieľov:
- **Všetky lekcie**: Microsoft Agent Framework (MAF) s `FoundryChatClient`
- **Agenti registrovaní na serverovej strane** v Microsoft Foundry Agent Service V2 a viditeľní v portáli Foundry

### Získanie pomoci

- Pripojte sa k [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Preštudujte súbory README lekcií pre špecifické pokyny
- Pozrite hlavný [README.md](./README.md) pre prehľad kurzu
- Obráťte sa na [Course Setup](./00-course-setup/README.md) pre detailné inštrukcie nastavenia

### Prispievanie

Toto je otvorený vzdelávací projekt. Vítané príspevky:
- Vylepšiť príklady kódu
- Opravovať preklepy alebo chyby
- Pridávať objasňujúce komentáre
- Navrhovať nové témy lekcií
- Prekladať do ďalších jazykov

Pozrite [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pre aktuálne potreby.

## Kontext špecifický pre projekt

### Podpora viacerých jazykov

Tento repozitár používa automatizovaný prekladový systém:
- Podpora pre 50+ jazykov
- Preklady v adresároch `/translations/<lang-code>/`
- GitHub Actions workflow spravuje aktualizácie prekladov
- Zdrojové súbory sú v angličtine v koreňovom adresári repozitára

### Štruktúra lekcie

Každá lekcia má konzistentný vzor:
1. Náhľad videa s odkazom
2. Písaný obsah lekcie (README.md)
3. Ukážky kódu v rôznych frameworkoch
4. Ciele učenia a požiadavky
5. Pridané ďalšie vzdelávacie zdroje s odkazmi

### Názvoslovie ukážok kódu

Formát: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcia 1, MAF Python
- `14-sequential.ipynb` - Lekcia 14, pokročilé vzory MAF
- `16-python-agent-framework.ipynb` - Lekcia 16, produkčný agent zákazníckej podpory
- `17-local-agent-foundry-local.ipynb` - Lekcia 17, lokálny agent s Foundry Local + Qwen

### Špeciálne adresáre

- `translated_images/` - Lokalizované obrázky pre preklady
- `images/` - Originálne obrázky pre anglický obsah
- `.devcontainer/` - Konfigurácia vývojového kontajnera VS Code
- `.github/` - GitHub Actions workflowy a šablóny

### Závislosti

Kľúčové balíky z `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Podpora protokolu Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Azure AI služby
- `azure-identity` - Azure autentifikácia (AzureCliCredential)
- `azure-search-documents` - Integrácia Azure AI Search
- `mcp[cli]` - Podpora Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->