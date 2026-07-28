# AGENTS.md

## Prehľad projektu

Tento repozitár obsahuje "AI Agenti pre Začiatočníkov" - komplexný vzdelávací kurz, ktorý učí všetko potrebné na tvorbu AI agentov. Kurz pozostáva z 18 lekcií (číslovaných 00-18), ktoré pokrývajú základy, návrhové vzory, frameworky, produkčné nasadenie, lokálnych/na zariadení agentov a bezpečnosť AI agentov.

**Kľúčové technológie:**
- Python 3.12+
- Jupyter Notebooky pre interaktívne učenie
- AI Frameworky: Microsoft Agent Framework (MAF)
- Azure AI služby: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektúra:**
- Štruktúra podľa lekcií (adresáre 00-15+)
- Každá lekcia obsahuje: dokumentáciu README, príklady kódu (Jupyter notebooky) a obrázky
- Podpora viacerých jazykov cez automatizovaný prekladový systém
- Jeden Python notebook na lekciu používajúci Microsoft Agent Framework

## Príkazy na nastavenie

### Požiadavky
- Python 3.12 alebo novší
- Azure predplatné (pre Microsoft Foundry)
- Azure CLI nainštalované a autentifikované (`az login`)

### Počiatočné nastavenie

1. **Naklonujte alebo forknite repozitár:**
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
   # Upravte .env so svojimi API kľúčmi a koncovými bodmi
   ```

### Povinné premenné prostredia

Pre **Microsoft Foundry** (povinné):
- `AZURE_AI_PROJECT_ENDPOINT` - koncový bod projektu Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - názov nasadenia modelu (napr. gpt-5-mini)

Pre **Azure AI Search** (Lekcia 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - koncový bod Azure AI Search
- `AZURE_SEARCH_API_KEY` - API kľúč Azure AI Search

Autentifikácia: Spustite `az login` pred spustením notebookov (používa `AzureCliCredential`).

## Vývojový pracovný tok

### Spustenie Jupyter Notebookov

Každá lekcia obsahuje viaceré Jupyter notebooky pre rôzne frameworky:

1. **Spustite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Prejdite do adresára lekcie** (napr. `01-intro-to-ai-agents/code_samples/`)

3. **Otvorte a spustite notebooky:**
   - `*-python-agent-framework.ipynb` - Použitie Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Použitie Microsoft Agent Framework (.NET)

### Práca s Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Vyžaduje Azure predplatné
- Používa `FoundryChatClient` pre Agent Service V2 (agenti viditeľní v portáli Foundry)
- Produkčná pripravenosť so zabudovanou pozorovateľnosťou
- Vzor súborov: `*-python-agent-framework.ipynb`

## Inštrukcie na testovanie

Toto je vzdelávací repozitár s ukážkovým kódom, nie produkčný kód s automatizovanými testami. Na overenie nastavenia a zmien:

### Manuálne testovanie

1. **Otestujte Python prostredie:**
   ```bash
   python --version  # Mala by byť 3.12 a vyššia
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Otestujte spustenie notebooku:**
   ```bash
   # Preveďte notebook na skript a spustite (testuje importy)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Overte premenné prostredia:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Spustenie jednotlivých notebookov

Otvorte notebooky v Jupyter a postupne vykonajte bunky. Každý notebook je samostatný a obsahuje:
- Importy
- Načítanie konfigurácie
- Príklady implementácií agentov
- Očakávané výstupy v markdown bunkách

### Rýchle testovanie nasadených agentov

Pre lekcie, kde je agent nasadený ako Microsoft Foundry hosťovaný agent (01, 04, 05, 16), repozitár obsahuje smoke-test katalógy v `tests/`, ktoré spúšťa workflow `.github/workflows/smoke-test.yml` cez akciu [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Ide o ľahké post-deploy brány (je agent dostupný a plní základné očakávania promptov?), ktoré dopĺňajú evaluačný pipeline v lekciách 10 a 16. Pozri [tests/README.md](./tests/README.md) pre mapovanie katalóg-lezkcia-agent. Lekcia 17 beží lokálne s Foundry Local a nemá hosťovaný endpoint, preto je validovaná priamym spustením jej notebooku.

## Štýl kódu

### Python konvencie

- **Verzia Pythonu**: 3.12+
- **Štýl kódu**: Dodržiavať štandardné Python PEP 8 konvencie
- **Notebooky**: Používať jasné markdown bunky na vysvetlenie konceptov
- **Importy**: Triediť podľa štandardnej knižnice, tretích strán, lokálne importy

### Jupyter Notebook konvencie

- Zahrnúť popisné markdown bunky pred kódovými bunkami
- Pridávať príklady výstupov v notebookoch na referenciu
- Používať jasné názvy premenných zodpovedajúce konceptom lekcie
- Zachovať lineárne poradie spustenia notebooku (bunka 1 → 2 → 3...)

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

## Skladanie a nasadzovanie

### Skladanie dokumentácie

Tento repozitár používa Markdown na dokumentáciu:
- Súbory README.md v každom adresári lekcie
- Hlavný README.md v koreňovom adresári repozitára
- Automatizovaný prekladový systém cez GitHub Actions

### CI/CD Pipelines

Nachádzajú sa v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický preklad do viac ako 50 jazykov
2. **welcome-issue.yml** - Privítanie tvorcov nových issues
3. **welcome-pr.yml** - Privítanie autorov nových pull requestov

### Nasadzovanie

Toto je vzdelávací repozitár - žiadny proces nasadzovania. Používatelia:
1. Forknú alebo naklonujú repozitár
2. Spúšťajú notebooky lokálne alebo v GitHub Codespaces
3. Učia sa úpravou a experimentovaním s príkladmi

## Pokyny pre pull requesty

### Pred odoslaním

1. **Otestujte svoje zmeny:**
   - Spustite úplne ovplyvnené notebooky
   - Overte, že všetky bunky sa vykonajú bez chýb
   - Skontrolujte, či sú výstupy vhodné

2. **Aktualizácie dokumentácie:**
   - Aktualizujte README.md, ak pridávate nové koncepty
   - Pridajte komentáre v notebookoch pre komplexný kód
   - Zabezpečte, že markdown bunky vysvetľujú účel

3. **Zmeny súborov:**
   - Vyhýbajte sa commitovaniu `.env` súborov (použite `.env.example`)
   - Necommitujte adresáre `venv/` alebo `__pycache__/`
   - Zachovajte výstupy notebookov, ak demonštrujú koncepty
   - Odstráňte dočasné súbory a zálohovacie notebooky (`*-backup.ipynb`)

### Formát názvov PR

Používajte popisné názvy:
- `[Lesson-XX] Pridaj nový príklad pre <koncept>`
- `[Fix] Oprav preklep v README lekcie-XX`
- `[Update] Vylepši ukážku kódu v lekcii-XX`
- `[Docs] Aktualizuj inštrukcie na nastavenie`

### Povinné kontroly

- Notebooky by sa mali spúšťať bez chýb
- README súbory by mali byť jasné a presné
- Dodržiavať existujúce vzory kódu v repozitári
- Zachovať konzistentnosť s ostatnými lekciami

## Dodatočné poznámky

### Bežné úskalia

1. **Nekompatibilita verzie Pythonu:**
   - Uistite sa, že používate Python 3.12+
   - Niektoré balíčky nemusia fungovať so staršími verziami
   - Použite `python3 -m venv`, aby ste explicitne špecifikovali verziu Pythonu

2. **Premenné prostredia:**
   - Vždy vytvorte `.env` zo súboru `.env.example`
   - Neukladajte `.env` súbor do repozitára (je v `.gitignore`)
   - Prihláste sa pomocou `az login` pre kľúčovú autentifikáciu Entra ID

3. **Konflikty balíčkov:**
   - Používajte čisté virtuálne prostredie
   - Inštalujte z `requirements.txt` namiesto po jednom balíčku
   - Niektoré notebooky môžu požadovať ďalšie balíčky uvedené v markdown bunkách

4. **Azure služby:**
   - Azure AI služby vyžadujú aktívne predplatné
   - Niektoré funkcie sú špecifické pre región
   - Zabezpečte, aby vaše Azure OpenAI nasadenie modelu podporovalo Responses API

### Učebná cesta

Odporúčané postupné prechádzanie lekciami:
1. **00-course-setup** - Začnite tu pre nastavenie prostredia
2. **01-intro-to-ai-agents** - Pochopte základy AI agentov
3. **02-explore-agentic-frameworks** - Naučte sa o rôznych frameworkoch
4. **03-agentic-design-patterns** - Základné návrhové vzory
5. Pokračujte postupne cez číslované lekcie

### Výber frameworku

Vyberte framework podľa vašich cieľov:
- **Všetky lekcie**: Microsoft Agent Framework (MAF) s `FoundryChatClient`
- **Agenti sa registrujú serverovo** v Microsoft Foundry Agent Service V2 a sú viditeľní v portáli Foundry

### Získanie pomoci

- Pripojte sa k [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Prezrite si README súbory lekcií pre špecifické usmernenia
- Skontrolujte hlavný [README.md](./README.md) pre prehľad kurzu
- Odkaz na [Course Setup](./00-course-setup/README.md) pre detailné inštrukcie nastavenia

### Príspevky

Toto je otvorený vzdelávací projekt. Príspevky sú vítané:
- Vylepšenie príkladov kódu
- Oprava preklepov alebo chýb
- Pridanie objasňujúcich komentárov
- Navrhovanie nových tém lekcií
- Preklady do ďalších jazykov

Pozrite si [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pre aktuálne potreby.

## Kontext špecifický pre projekt

### Podpora viacerých jazykov

Tento repozitár používa automatizovaný prekladový systém:
- Podpora viac ako 50 jazykov
- Preklady v adresároch `/translations/<lang-code>/`
- GitHub Actions workflow spravuje aktualizácie prekladu
- Zdrojové súbory sú v angličtine v koreňovom adresári repozitára

### Štruktúra lekcií

Každá lekcia dodržiava konzistentný vzor:
1. Náhľad videa s odkazom
2. Písaný obsah lekcie (README.md)
3. Príklady kódu v rôznych frameworkoch
4. Ciele učenia a požiadavky
5. Odkazy na extra zdroje učenia

### Názvy príkladov kódu

Formát: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcia 1, MAF Python
- `14-sequential.ipynb` - Lekcia 14, pokročilé vzory MAF
- `16-python-agent-framework.ipynb` - Lekcia 16, produkčný agent zákazníckej podpory
- `17-local-agent-foundry-local.ipynb` - Lekcia 17, lokálny agent s Foundry Local + Qwen

### Špeciálne adresáre

- `translated_images/` - Lokalizované obrázky pre preklady
- `images/` - Pôvodné obrázky pre anglický obsah
- `.devcontainer/` - Konfigurácia vývojového kontajnera VS Code
- `.github/` - GitHub Actions workflowy a šablóny

### Závislosti

Kľúčové balíčky zo súboru `requirements.txt`:
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