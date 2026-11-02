# AGENTS.md

## Pregled projekta

Ta repozitorij vsebuje "AI agente za začetnike" - obsežen izobraževalni tečaj, ki uči vse, kar je potrebno za izdelavo AI agentov. Tečaj obsega 18 lekcij (številčenih od 00 do 18), ki zajemajo osnove, oblikovalske vzorce, ogrodja, poganjanje v produkciji, lokalne/na napravah agente ter varnost AI agentov.

**Ključne tehnologije:**
- Python 3.12+
- Jupyter zapiski za interaktivno učenje
- AI ogrodja: Microsoft Agent Framework (MAF)
- Azure AI storitve: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitektura:**
- Struktura na osnovi lekcij (mape 00-18)
- Vsaka lekcija vsebuje: dokumentacijo README, primere kode (Jupyter zapiske) in slike
- Podpora več jezikom preko avtomatiziranega prevajalskega sistema
- En Python zvezek na lekcijo z uporabo Microsoft Agent Framework-a

## Ukazi za nastavitve

### Predpogoji
- Python 3.12 ali novejši
- Azure naročnina (za Microsoft Foundry)
- Azure CLI nameščen in prijavljen (`az login`)

### Začetna nastavitev

1. **Klonirajte ali razvežite repozitorij:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Ustvarite in aktivirajte Python virtualno okolje:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Namestite odvisnosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nastavite spremenljivke okolja:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Zahtevane spremenljivke okolja

Za **Microsoft Foundry** (zahtevano):
- `AZURE_AI_PROJECT_ENDPOINT` - vrata projekta Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ime nameščanja modela (npr. gpt-5-mini)

Za **Azure AI Search** (Lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - vrata Azure AI Search
- `AZURE_SEARCH_API_KEY` - API ključ Azure AI Search

Avtentikacija: Zaženite `az login` pred zagonom zvezkov (uporablja `AzureCliCredential`).

## Razvojni potek

### Zagon Jupyter zvezkov

Vsaka lekcija vsebuje več Jupyter zvezkov za različna ogrodja:

1. **Zaženite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Pomaknite se v mapo lekcije** (npr. `01-intro-to-ai-agents/code_samples/`)

3. **Odprite in zaženite zvezke:**
   - `*-python-agent-framework.ipynb` - Uporaba Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Uporaba Microsoft Agent Framework (.NET)

### Delo z Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Potrebna Azure naročnina
- Uporablja `FoundryChatClient` za Agent Service V2 (agenti vidni v Foundry portalu)
- Pripravljen za produkcijo z vgrajenim opazovanjem
- Vzorec imen datotek: `*-python-agent-framework.ipynb`

## Navodila za testiranje

To je izobraževalni repozitorij z vzorčno kodo, ne produkcijska koda z avtomatiziranimi testi. Za preverjanje nastavitve in sprememb:

### Ročno testiranje

1. **Test okolja Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test izvedbe zvezka:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Preverite spremenljivke okolja:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Zagon posameznih zvezkov

Odprite zvezke v Jupyterju in izvršite celice zaporedno. Vsak zvezek je samostojen in vključuje:
- Izjave o uvozu
- Nalaganje konfiguracije
- Primeri implementacij agentov
- Pričakovani izhodi v markdown celicah

### Smoke-testiranje nameščenih agentov

Za lekcije, kjer je agent nameščen kot gostovani agent Microsoft Foundry (01, 04, 05, 16), repozitorij vsebuje smoke-test kataloge pod `tests/`, ki jih izvršuje delovni tok `.github/workflows/smoke-test.yml` preko akcije [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). To je lahka varovalka po namestitvi (ali je agent dosegljiv in sledi osnovnim pričakovanjem ukazov?), ki dopolnjuje evalvacijski potek pri lekcijah 10 in 16. Oglejte si [tests/README.md](./tests/README.md) za preslikavo kataloga v lekcijo in agenta. Lekcija 17 teče lokalno s Foundry Local in nima gostovanih vrat, zato se preverja z neposrednim zagonom zvezka.

## Stil kode

### Python konvencije

- **Python različica**: 3.12+
- **Stil kode**: Sledite standardnim Python PEP 8 konvencijam
- **Zvezki**: Uporabljajte jasne markdown celice za razlago konceptov
- **Uvozi**: Razvrstite po standardni knjižnici, tretjih straneh, lokalnih uvozih

### Konvencije Jupyter zvezkov

- Vključite opisne markdown celice pred kodo
- V zvezkih dodajte primere izhodov za referenco
- Uporabljajte jasna imena spremenljivk, ki ustrezajo konceptom lekcije
- Ohranjajte linearni red izvajanja zvezkov (celica 1 → 2 → 3...)

### Organizacija datotek

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Gradnja in namestitev

### Gradnja dokumentacije

Ta repozitorij uporablja Markdown za dokumentacijo:
- README.md datoteke v vsaki mapi lekcije
- Glavna README.md v korenu repozitorija
- Avtomatiziran prevajalski sistem preko GitHub Actions

### CI/CD potek

Nahaja se v `.github/workflows/`:

1. **co-op-translator.yml** - Samodejni prevod v več kot 50 jezikov
2. **welcome-issue.yml** - Pozdravlja ustvarjalce novih težav
3. **welcome-pr.yml** - Pozdravlja prispevke iz pull requestov

### Namestitev

To je izobraževalni repozitorij - ni procesa namestitve. Uporabniki:
1. Razvejajo ali klonirajo repozitorij
2. Zaženejo zvezke lokalno ali v GitHub Codespaces
3. Se učijo z združevanjem in eksperimentiranjem s primeri

## Smernice za pull request

### Pred oddajo

1. **Testirajte svoje spremembe:**
   - Popolnoma zaženite prizadete zvezke
   - Prepričajte se, da se vse celice izvršijo brez napak
   - Preverite, da so izhodi ustrezni

2. **Posodobitve dokumentacije:**
   - Posodobite README.md, če dodajate nove koncepte
   - Dodajte komentarje v zvezkih za zahtevnejšo kodo
   - Poskrbite, da markdown celice razložijo namen

3. **Spremembe datotek:**
   - Izogibajte se commitanju `.env` datotek (uporabljajte `.env.example`)
   - Ne committajte `venv/` ali `__pycache__/` map
   - Ohranjajte izhode zvezkov, kadar demonstrirajo koncepte
   - Odstranite začasne datoteke in varnostne kopije zvezkov (`*-backup.ipynb`)

### Format naslova PR

Uporabljajte opisne naslove:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Zahtevani pregledi

- Zvezki naj se izvajajo brez napak
- README datoteke naj bodo jasne in natančne
- Sledite obstoječim vzorcem kode v repozitoriju
- Ohranjajte konsistentnost z ostalimi lekcijami

## Dodatne opombe

### Pogoste napake

1. **Neujemanje različice Pythona:**
   - Poskrbite, da uporabljate Python 3.12 ali novejši
   - Nekateri paketi morda ne delujejo z starejšimi različicami
   - Za natančno določitve različice uporabite `python3 -m venv`

2. **Spremenljivke okolja:**
   - Vedno ustvarite `.env` iz `.env.example`
   - Ne committajte datoteke `.env` (je v `.gitignore`)
   - Prijavite se z `az login` za preverjanje pristnosti Entra ID brez ključa

3. **Konflikti paketov:**
   - Uporabite sveže virtualno okolje
   - Namestite iz `requirements.txt` namesto posameznih paketov
   - Nekateri zvezki morda zahtevajo dodatne pakete, navedene v njihovih markdown celicah

4. **Azure storitve:**
   - Azure AI storitve zahtevajo aktivno naročnino
   - Nekatere funkcije so specifične za regijo
   - Prepričajte se, da vaša Azure OpenAI nameščena različica podpira Responses API

### Pot učenja

Priporočeno zaporedje lekcij:
1. **00-course-setup** - Začetek za nastavitev okolja
2. **01-intro-to-ai-agents** - Razumevanje osnov AI agentov
3. **02-explore-agentic-frameworks** - Spoznajte različna ogrodja
4. **03-agentic-design-patterns** - Osnovni oblikovalski vzorci
5. Nadaljujte po zaporedju lekcij

### Izbira ogrodja

Izberite ogrodje glede na vaše cilje:
- **Vse lekcije**: Microsoft Agent Framework (MAF) z `FoundryChatClient`
- **Agenti se registrirajo na strežniški strani** v Microsoft Foundry Agent Service V2 in so vidni v portalu Foundry

### Iskanje pomoči

- Pridružite se [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Preglejte README datoteke lekcij za specifična navodila
- Preverite glavno [README.md](./README.md) za pregled tečaja
- Za podrobna navodila o nastavitvi glejte [Course Setup](./00-course-setup/README.md)

### Prispevanje

To je odprt izobraževalni projekt. Prispevki so dobrodošli:
- Izboljšave primerov kode
- Popravljanje tipkarskih napak ali napak
- Dodajanje pojasnjevalnih komentarjev
- Predlaganje novih tem lekcij
- Prevodi v dodatne jezike

Oglejte si [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za aktualne potrebe.

## Kontekst specifičen za projekt

### Podpora več jezikom

Ta repozitorij uporablja avtomatiziran prevajalski sistem:
- Podpora za več kot 50 jezikov
- Prevodi v `/translations/<lang-code>/` mapah
- GitHub Actions delovni tok skrbi za posodobitve prevodov
- Izvorne datoteke so v angleščini v korenu repozitorija

### Struktura lekcije

Vsaka lekcija sledi doslednemu vzorcu:
1. Videoposnetek s sličico in povezavo
2. Pisna vsebina lekcije (README.md)
3. Primeri kode v različnih ogrodjih
4. Cilji učenja in predpogoji
5. Povezani dodatni viri za učenje

### Imenovanje vzorcev kode

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcija 1, MAF Python
- `14-sequential.ipynb` - Lekcija 14, MAF napredni vzorci
- `16-python-agent-framework.ipynb` - Lekcija 16, produkcijski agent za podporo strankam
- `17-local-agent-foundry-local.ipynb` - Lekcija 17, lokalni agent z Foundry Local + Qwen

### Posebne mape

- `translated_images/` - Lokalizirane slike za prevode
- `images/` - Izvirne slike za angleško vsebino
- `.devcontainer/` - Konfiguracija razvojnega kontejnerja VS Code
- `.github/` - GitHub Actions delovni tokovi in predloge

### Odvisnosti

Ključni paketi iz `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Podpora protokola Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Azure AI storitve
- `azure-identity` - Azure avtentikacija (AzureCliCredential)
- `azure-search-documents` - Integracija Azure AI Search
- `mcp[cli]` - Podpora Model Context protokolu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->