# AGENTS.md

## Prehľad Projektu

Táto repozitár obsahuje "AI Agenti pre začiatočníkov" - komplexný vzdelávací kurz, ktorý učí všetko potrebné na vytvorenie AI agentov. Kurz pozostáva z 18 lekcií (číslovaných 00-18), ktoré pokrývajú základy, návrhové vzory, frameworky, produkčné nasadenie, lokálnych/ zariadených agentov a bezpečnosť AI agentov.

**Kľúčové technológie:**
- Python 3.12+
- Jupyter Notebooky pre interaktívne učenie
- AI Frameworky: Microsoft Agent Framework (MAF)
- Azure AI služby: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektúra:**
- Štruktúra založená na lekciách (adresáre 00-15+)
- Každá lekcia obsahuje: README dokumentáciu, ukážky kódu (Jupyter notebooky) a obrázky
- Podpora viacerých jazykov cez automatizovaný prekladový systém
- Jeden Python notebook na lekciu používajúci Microsoft Agent Framework

## Inštrukcie Nastavenia

### Požiadavky
- Python 3.12 alebo vyšší
- Azure predplatné (pre Microsoft Foundry)
- Nainštalovaný a autentifikovaný Azure CLI (`az login`)

### Počiatočné Nastavenie

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
   source venv/bin/activate  # Vo Windows: venv\Scripts\activate
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

### Povinné Premenné Prostredia

Pre **Microsoft Foundry** (Povinné):
- `AZURE_AI_PROJECT_ENDPOINT` - Koncový bod projektu Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Názov nasadenia modelu (napr. gpt-4.1-mini)

Pre **Azure AI Search** (Lekcia 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Koncový bod Azure AI Search
- `AZURE_SEARCH_API_KEY` - API kľúč Azure AI Search

Autentifikácia: Spustite `az login` pred spustením notebookov (používa `AzureCliCredential`).

## Vývojový Priebeh

### Spustenie Jupyter Notebookov

Každá lekcia obsahuje viacero Jupyter notebookov pre rôzne frameworky:

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
- Produkčne pripravené s vnútorným monitorovaním
- Vzor súboru: `*-python-agent-framework.ipynb`

## Inštrukcie na Testovanie

Toto je vzdelávací repozitár s ukážkovým kódom namiesto produkčného kódu s automatizovanými testami. Na overenie vášho nastavenia a zmien:

### Manuálne Testovanie

1. **Otestujte Python prostredie:**
   ```bash
   python --version  # Mala by byť 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Otestujte spustenie notebooku:**
   ```bash
   # Konvertovať poznámkový blok na skript a spustiť (testuje importy)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Overte premenné prostredia:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Spustenie jednotlivých notebookov

Otvorte notebooky v Jupyter a spúšťajte bunky postupne. Každý notebook je samostatný a obsahuje:
- Importy
- Načítanie konfigurácie
- Príklady implementácií agentov
- Očakávané výstupy v markdown bunkách

### Rýchlotestovanie nasadených agentov

Pre lekcie, kde je agent nasadený ako Microsoft Foundry hostovaný agent (01, 04, 05, 16), repozitár obsahuje rýchlotest katalógy v adresári `tests/`, ktoré sú spúšťané workflow `.github/workflows/smoke-test.yml` cez akciu [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Ide o ľahkú kontrolu po nasadení (je agent dostupný a reaguje podľa základných očakávaní?), ktorá dopĺňa evaluačný pipeline v lekciách 10 a 16. Pozrite [tests/README.md](./tests/README.md) pre mapovanie katalógu na lekciu a agenta. Lekcia 17 beží lokálne s Foundry Local a nemá hostený koncový bod, preto sa overuje priamym spustením jej notebooku.

## Štýl Kódu

### Python Konvencie

- **Verzia Pythonu**: 3.12+
- **Štýl kódu**: Dodržiavať štandardné Python PEP 8 konvencie
- **Notebooky**: Použiť jasné markdown bunky na vysvetlenie konceptov
- **Importy**: Triediť podľa štandardnej knižnice, tretích strán, lokálne importy

### Jupyter Notebook Konvencie

- Zahŕňať popisné markdown bunky pred kódovými bunkami
- Pridávať príklady výstupov v notebookoch ako referenciu
- Používať jasné názvy premenných zodpovedajúce lekčným konceptom
- Zachovať lineárne poradie spustenia notebooku (bunka 1 → 2 → 3...)

### Organizácia Súborov

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Skladanie a Nasadenie

### Skladanie Dokumentácie

Tento repozitár používa Markdown pre dokumentáciu:
- README.md súbory v každom adresári lekcie
- Hlavný README.md v koreňovom adresári repozitára
- Automatizovaný prekladový systém cez GitHub Actions

### CI/CD Pipeline

Nachádza sa v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický preklad do 50+ jazykov
2. **welcome-issue.yml** - Privítanie nových tvorcov issue
3. **welcome-pr.yml** - Privítanie nových prispievateľov pull requestov

### Nasadenie

Toto je vzdelávací repozitár - žiadny proces nasadenia. Používatelia:
1. Vytvoria fork alebo sklonujú repozitár
2. Spúšťajú notebooky lokálne alebo v GitHub Codespaces
3. Učia sa modifikáciou a experimentovaním s príkladmi

## Pokyny pre Pull Requesty

### Pred Odoslaním

1. **Otestujte vaše zmeny:**
   - Úplne spustite ovplyvnené notebooky
   - Overte, že všetky bunky sa vykonajú bez chýb
   - Skontrolujte, že výstupy sú vhodné

2. **Aktualizácie dokumentácie:**
   - Aktualizujte README.md, ak pridávate nové koncepty
   - Pridajte komentáre v notebookoch pre zložitejší kód
   - Zabezpečte, aby markdown bunky vysvetľovali účel

3. **Zmeny súborov:**
   - Neposielajte `.env` súbory (použite `.env.example`)
   - Nezahrňujte adresáre `venv/` alebo `__pycache__/`
   - Zachovajte výstupy notebookov, keď demonštrujú koncepty
   - Odstráňte dočasné súbory a zálohovacie notebooky (`*-backup.ipynb`)

### Formát Názvu PR

Používajte popisné názvy:
- `[Lesson-XX] Pridanie nového príkladu pre <koncept>`
- `[Fix] Oprava preklepu v README lekcie-XX`
- `[Update] Vylepšenie ukážky kódu v lekcii-XX`
- `[Docs] Aktualizácia inštrukcií na nastavenie`

### Povinné Kontroly

- Notebooky by sa mali vykonať bez chýb
- README súbory by mali byť jasné a presné
- Dodržiavať existujúce vzory kódu v repozitári
- Zachovať konzistenciu s ostatnými lekciami

## Ďalšie Poznámky

### Časté Problémy

1. **Nesúlad verzie Pythonu:**
   - Používajte Python 3.12+
   - Niektoré balíky nemusia fungovať so staršími verziami
   - Použite `python3 -m venv` na explicitné určenie verzie Pythonu

2. **Premenné prostredia:**
   - Vždy vytvorte `.env` zo súboru `.env.example`
   - Neposielajte `.env` súbor (je v `.gitignore`)
   - Prihláste sa s `az login` pre autentifikáciu Entra ID bez kľúčov

3. **Konflikty balíkov:**
   - Používajte čerstvé virtuálne prostredie
   - Inštalujte zo súboru `requirements.txt` namiesto samostatných balíkov
   - Niektoré notebooky môžu vyžadovať ďalšie balíky uvedené v ich markdown bunkách

4. **Azure služby:**
   - Azure AI služby vyžadujú aktívne predplatné
   - Niektoré funkcie sú špecifické pre región
   - Zabezpečte, že vaše nasadenie Azure OpenAI modelu podporuje Responses API

### Učebná Cesta

Odporúčané poradie lekcií:
1. **00-course-setup** - Začnite tu so nastavením prostredia
2. **01-intro-to-ai-agents** - Pochopenie základov AI agentov
3. **02-explore-agentic-frameworks** - Zoznámte sa s rôznymi frameworkami
4. **03-agentic-design-patterns** - Základné návrhové vzory
5. Pokračujte postupne cez číslované lekcie

### Výber Frameworku

Vyberte framework podľa svojich cieľov:
- **Všetky lekcie**: Microsoft Agent Framework (MAF) s `FoundryChatClient`
- **Agenti sa registrujú na serverovej strane** v Microsoft Foundry Agent Service V2 a sú viditeľní v Foundry portáli

### Ako Získať Pomoc

- Pripojte sa na [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Prezrite si README súbory lekcií pre špecifické usmernenia
- Pozrite hlavný [README.md](./README.md) pre prehľad kurzu
- Pozrite [Course Setup](./00-course-setup/README.md) pre detailné inštrukcie nastavenia

### Prispievanie

Toto je otvorený vzdelávací projekt. Príspevky sú vítané:
- Zlepšiť príklady kódu
- Opraviť preklepy alebo chyby
- Pridať objasňujúce komentáre
- Navrhnúť témy nových lekcií
- Preložiť do ďalších jazykov

Pozrite [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pre aktuálne potreby.

## Kontext špecifický pre projekt

### Podpora Viacerých Jazykov

Tento repozitár používa automatizovaný prekladový systém:
- Podpora 50+ jazykov
- Preklady v adresároch `/translations/<lang-code>/`
- Prekladový workflow riadený GitHub Actions
- Zdrojové súbory sú v angličtine v koreňovom adresári repozitára

### Štruktúra Lekcie

Každá lekcia nasleduje konzistentný vzor:
1. Náhľad videa s odkazom
2. Písaný obsah lekcie (README.md)
3. Ukážky kódu v rôznych frameworkoch
4. Ciele učenia a predpoklady
5. Dodatočné učebné zdroje s odkazmi

### Názvy ukážok kódu

Formát: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcia 1, MAF Python
- `14-sequential.ipynb` - Lekcia 14, pokročilé vzory MAF
- `16-python-agent-framework.ipynb` - Lekcia 16, produkčný agent pre zákaznícku podporu
- `17-local-agent-foundry-local.ipynb` - Lekcia 17, lokálny agent s Foundry Local + Qwen

### Špeciálne Adresáre

- `translated_images/` - Lokalizované obrázky pre preklady
- `images/` - Pôvodné obrázky pre anglický obsah
- `.devcontainer/` - Konfigurácia kontajnera pre VS Code vývoj
- `.github/` - GitHub Actions workflowy a šablóny

### Závislosti

Kľúčové balíky z `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Podpora protokolu Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Azure AI služby
- `azure-identity` - Azure autentifikácia (AzureCliCredential)
- `azure-search-documents` - Integrácia s Azure AI Search
- `mcp[cli]` - Podpora Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->