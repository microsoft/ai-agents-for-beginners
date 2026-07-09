# AGENTS.md

## Prehľad projektu

Tento repozitár obsahuje "AI agentov pre začiatočníkov" - komplexný výučbový kurz, ktorý učí všetko potrebné na vytvorenie AI agentov. Kurz pozostáva z 18 lekcií pokrývajúcich základy, návrhové vzory, rámce a nasadenie AI agentov do produkcie.

**Kľúčové technológie:**
- Python 3.12+
- Jupyter Notebooky pre interaktívne učenie
- AI rámce: Microsoft Agent Framework (MAF)
- Azure AI služby: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektúra:**
- Štruktúra založená na lekciách (adresáre 00-15+)
- Každá lekcia obsahuje: dokumentáciu README, ukážky kódu (Jupyter notebooky) a obrázky
- Podpora viacerých jazykov cez automatizovaný prekladový systém
- Jeden Python notebook pre každú lekciu používajúci Microsoft Agent Framework

## Príkazy na nastavenie

### Predpoklady
- Python 3.12 alebo novší
- Azure predplatné (pre Microsoft Foundry)
- Nainštalovaný a autentifikovaný Azure CLI (`az login`)

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
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - názov nasadenia modelu (napr. gpt-4o)

Pre **Azure AI Search** (Lekcia 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - koncový bod Azure AI Search
- `AZURE_SEARCH_API_KEY` - API kľúč Azure AI Search

Autentifikácia: Spustite `az login` pred spustením notebookov (používa `AzureCliCredential`).

## Vývojový pracovný postup

### Spustenie Jupyter notebookov

Každá lekcia obsahuje viacero Jupyter notebookov pre rôzne rámce:

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
- Používa `FoundryChatClient` pre Agent Service V2 (agentov vidno v Foundry portáli)
- Produkčne pripravené s vstavanou pozorovateľnosťou
- Vzor názvov súborov: `*-python-agent-framework.ipynb`

## Inštrukcie na testovanie

Toto je vzdelávací repozitár s ukážkovým kódom, nie produkčný kód s automatizovanými testami. Pre overenie nastavenia a zmien:

### Manuálne testovanie

1. **Otestujte Python prostredie:**
   ```bash
   python --version  # Malo by byť 3.12 a vyššie
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Otestujte spustenie notebooku:**
   ```bash
   # Preveďte poznámkový blok na skript a spustite (testuje importy)
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
- Príklady implementácie agentov
- Očakávané výstupy v markdown bunkách

## Štýl kódu

### Python konvencie

- **Verzia Python**: 3.12+
- **Štýl kódu**: Dodržiavajte štandardné Python PEP 8 konvencie
- **Notebooky**: Používajte jasné markdown bunky na vysvetlenie konceptov
- **Importy**: Zoskupujte podľa štandardnej knižnice, knižníc tretích strán, lokálnych importov

### Konvencie pre Jupyter Notebooky

- Zahrňte popisné markdown bunky pred kódovými bunkami
- Pridajte príklady výstupov v notebookoch pre referenciu
- Používajte jasné názvy premenných zodpovedajúce konceptom lekcie
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

## Sestavenie a nasadenie

### Tvorba dokumentácie

Tento repozitár používa Markdown na dokumentáciu:
- Súbory README.md v každom adresári lekcie
- Hlavný súbor README.md v koreňovom adresári repozitára
- Automatizovaný prekladový systém cez GitHub Actions

### CI/CD pipeline

Sa nachádza v `.github/workflows/`:

1. **co-op-translator.yml** - Automatický preklad do 50+ jazykov
2. **welcome-issue.yml** - Privítanie tvorcov nových issue
3. **welcome-pr.yml** - Privítanie prispievateľov do pull requestov

### Nasadenie

Toto je vzdelávací repozitár - žiadny proces nasadenia. Používatelia:
1. Forknite alebo naklonujte repozitár
2. Spustite notebooky lokálne alebo v GitHub Codespaces
3. Učte sa úpravou a experimentovaním s príkladmi

## Pokyny k pull requestom

### Pred odoslaním

1. **Otestujte svoje zmeny:**
   - Spustite kompletne ovplyvnené notebooky
   - Overte, že všetky bunky sa vykonajú bez chýb
   - Skontrolujte, či sú výstupy vhodné

2. **Aktualizácie dokumentácie:**
   - Aktualizujte README.md pri pridávaní nových konceptov
   - Pridajte komentáre v notebookoch pre zložitejší kód
   - Zaistite, že markdown bunky vysvetľujú účel

3. **Zmeny súborov:**
   - Neposielajte `.env` súbory (používajte `.env.example`)
   - Neodosielajte adresáre `venv/` alebo `__pycache__/`
   - Zachovajte výstupy notebookov, keď demonštrujú koncepty
   - Odstráňte dočasné súbory a zálohovacie notebooky (`*-backup.ipynb`)

### Formát názvu PR

Používajte popisné názvy:
- `[Lesson-XX] Pridanie nového príkladu pre <koncept>`
- `[Fix] Oprava preklepu v README lekcie XX`
- `[Update] Vylepšenie ukážky kódu v lekcii XX`
- `[Docs] Aktualizácia inštrukcií na nastavenie`

### Povinné kontroly

- Notebooky sa musia vykonať bez chýb
- README súbory musia byť jasné a presné
- Dodržiavať existujúce vzory kódu v repozitári
- Zachovať konzistenciu s ostatnými lekciami

## Dodatočné poznámky

### Bežné úskalia

1. **Nezhoda verzie Python:**
   - Uistite sa, že používate Python 3.12+
   - Niektoré balíčky nemusia fungovať so staršími verziami
   - Použite `python3 -m venv` pre explicitné zvolenie verzie Python

2. **Premenné prostredia:**
   - Vždy vytvorte `.env` z `.env.example`
   - Neposielajte `.env` súbor (je v `.gitignore`)
   - Prihláste sa pomocou `az login` pre autentifikáciu bez kľúčov Entra ID

3. **Konflikty balíčkov:**
   - Použite čerstvé virtuálne prostredie
   - Inštalujte z `requirements.txt` namiesto jednotlivých balíčkov
   - Niektoré notebooky môžu vyžadovať ďalšie balíčky uvedené v markdown bunkách

4. **Azure služby:**
   - Azure AI služby vyžadujú aktívne predplatné
   - Niektoré funkcie sú závislé od regiónu
   - Uistite sa, že vaše nasadenie Azure OpenAI modelu podporuje API odpovedí

### Učebná cesta

Odporúčaný postup cez lekcie:
1. **00-course-setup** - Začnite tu s nastavením prostredia
2. **01-intro-to-ai-agents** - Pochopenie základov AI agentov
3. **02-explore-agentic-frameworks** - Naučte sa o rôznych rámcoch
4. **03-agentic-design-patterns** - Základné návrhové vzory
5. Pokračujte postupne cez číslované lekcie

### Výber rámca

Vyberte rámec podľa vašich cieľov:
- **Všetky lekcie**: Microsoft Agent Framework (MAF) s `FoundryChatClient`
- **Agenti sa registrujú na serverovej strane** v Microsoft Foundry Agent Service V2 a sú viditeľní v Foundry portáli

### Podpora

- Pridajte sa do [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Prečítajte si README súbory lekcií pre konkrétne pokyny
- Skontrolujte hlavný [README.md](./README.md) pre prehľad kurzu
- Odkaz na [Course Setup](./00-course-setup/README.md) pre detailné inštrukcie nastavenia

### Prispievanie

Toto je otvorený vzdelávací projekt. Vítané príspevky:
- Vylepšenie ukážok kódu
- Opravy preklepov alebo chýb
- Pridanie vysvetľujúcich komentárov
- Návrhy na nové témy lekcií
- Preklady do ďalších jazykov

Pozrite si [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pre aktuálne potreby.

## Kontext špecifický pre projekt

### Podpora viacerých jazykov

Tento repozitár používa automatizovaný prekladový systém:
- Podpora 50+ jazykov
- Preklady v adresároch `/translations/<lang-code>/`
- GitHub Actions workflow spravuje aktualizácie prekladov
- Zdrojové súbory sú v angličtine v koreňovom adresári repozitára

### Štruktúra lekcie

Každá lekcia má konzistentný vzor:
1. Náhľad videa s odkazom
2. Písaný obsah lekcie (README.md)
3. Ukážky kódu v rôznych rámcoch
4. Učebné ciele a predpoklady
5. Odkazy na ďalšie učebné zdroje

### Názvoslovie ukážok kódu

Formát: `<cislo-lekcie>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcia 1, MAF Python
- `14-sequential.ipynb` - Lekcia 14, pokročilé vzory MAF

### Špeciálne adresáre

- `translated_images/` - Lokalizované obrázky pre preklady
- `images/` - Pôvodné obrázky pre anglický obsah
- `.devcontainer/` - Konfigurácia vývojového kontajnera VS Code
- `.github/` - GitHub Actions workflow-y a šablóny

### Závislosti

Kľúčové balíčky z `requirements.txt`:
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