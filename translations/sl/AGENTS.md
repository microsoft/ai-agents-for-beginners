# AGENTS.md

## Pregled projekta

Ta repozitorij vsebuje "AI Agents for Beginners" - celovit izobraževalni tečaj, ki uči vse potrebno za izdelavo AI agentov. Tečaj vključuje več kot 15 lekcij, ki pokrivajo osnove, vzorce oblikovanja, ogrodja in uvajanje AI agentov v produkcijo.

**Ključne tehnologije:**
- Python 3.12+
- Jupyter Notebooks za interaktivno učenje
- AI ogrodja: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI storitve: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (na voljo brezplačna različica)

**Arhitektura:**
- Struktura temelji na lekcijah (imeniki 00-15+)
- Vsaka lekcija vsebuje: dokumentacijo README, vzorčne kode (Jupyter notebooks) in slike
- Podpora za več jezikov prek avtomatiziranega sistema za prevajanje
- Več možnosti ogrodij za vsako lekcijo (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Ukazi za nastavitev

### Predpogoji
- Python 3.12 ali novejši
- GitHub račun (za GitHub Models - brezplačna različica)
- Azure naročnina (neobvezno, za Azure AI storitve)

### Začetna nastavitev

1. **Klonirajte ali razvejite repozitorij:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Ustvarite in aktivirajte virtualno okolje za Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Namestite odvisnosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nastavite okoljske spremenljivke:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Zahtevane okoljske spremenljivke

Za **GitHub Models (brezplačno)**:
- `GITHUB_TOKEN` - Osebni dostopni žeton iz GitHuba

Za **Azure AI storitve** (neobvezno):
- `PROJECT_ENDPOINT` - Končna točka projekta Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - API ključ za Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL končne točke Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Ime uvajanja za model klepeta
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Ime uvajanja za vdelave
- Dodatna konfiguracija Azure, kot je prikazano v `.env.example`

## Potek razvoja

### Zagon Jupyter Notebooks

Vsaka lekcija vsebuje več Jupyter notebookov za različna ogrodja:

1. **Zaženite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Pomaknite se do imenika lekcije** (npr. `01-intro-to-ai-agents/code_samples/`)

3. **Odprite in zaženite notebooks:**
   - `*-semantic-kernel.ipynb` - Uporaba ogrodja Semantic Kernel
   - `*-autogen.ipynb` - Uporaba ogrodja AutoGen
   - `*-python-agent-framework.ipynb` - Uporaba Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Uporaba Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Uporaba Azure AI Agent Service

### Delo z različnimi ogrodji

**Semantic Kernel + GitHub Models:**
- Na voljo brezplačna različica z GitHub računom
- Primerno za učenje in eksperimentiranje
- Vzorec datotek: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Na voljo brezplačna različica z GitHub računom
- Zmožnosti orkestracije več agentov
- Vzorec datotek: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Najnovejše ogrodje Microsofta
- Na voljo v Pythonu in .NET
- Vzorec datotek: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Zahteva Azure naročnino
- Funkcije pripravljene za produkcijo
- Vzorec datotek: `*-azureaiagent.ipynb`

## Navodila za testiranje

To je izobraževalni repozitorij z vzorčno kodo, ne produkcijska koda z avtomatiziranimi testi. Za preverjanje vaše nastavitve in sprememb:

### Ročno testiranje

1. **Testirajte Python okolje:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Testirajte izvajanje notebookov:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Preverite okoljske spremenljivke:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Zagon posameznih notebookov

Odprite notebooks v Jupyterju in izvajajte celice zaporedno. Vsak notebook je samostojen in vključuje:
- Uvozne izjave
- Nalaganje konfiguracije
- Primeri implementacij agentov
- Pričakovani izhodi v markdown celicah

## Slog kode

### Python konvencije

- **Python različica**: 3.12+
- **Slog kode**: Upoštevajte standardne Python PEP 8 konvencije
- **Notebooks**: Uporabite jasne markdown celice za razlago konceptov
- **Uvozi**: Razvrstite po standardni knjižnici, tretjih straneh, lokalnih uvozih

### Konvencije za Jupyter Notebook

- Vključite opisne markdown celice pred celicami s kodo
- Dodajte primere izhodov v notebooks za referenco
- Uporabite jasna imena spremenljivk, ki ustrezajo konceptom lekcije
- Ohranite linearni vrstni red izvajanja notebookov (celica 1 → 2 → 3...)

### Organizacija datotek

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

## Gradnja in uvajanje

### Gradnja dokumentacije

Ta repozitorij uporablja Markdown za dokumentacijo:
- README.md datoteke v vsakem imeniku lekcije
- Glavna README.md datoteka v korenu repozitorija
- Avtomatiziran sistem za prevajanje prek GitHub Actions

### CI/CD cevovod

Nahaja se v `.github/workflows/`:

1. **co-op-translator.yml** - Samodejno prevajanje v več kot 50 jezikov
2. **welcome-issue.yml** - Pozdrav za nove ustvarjalce težav
3. **welcome-pr.yml** - Pozdrav za nove prispevke pull requestov

### Uvajanje

To je izobraževalni repozitorij - ni postopka uvajanja. Uporabniki:
1. Razvejijo ali klonirajo repozitorij
2. Zaženejo notebooks lokalno ali v GitHub Codespaces
3. Učijo se z modificiranjem in eksperimentiranjem z vzorci

## Smernice za pull requeste

### Pred oddajo

1. **Testirajte svoje spremembe:**
   - Popolnoma zaženite prizadete notebooks
   - Preverite, da se vse celice izvajajo brez napak
   - Preverite, da so izhodi ustrezni

2. **Posodobitve dokumentacije:**
   - Posodobite README.md, če dodajate nove koncepte
   - Dodajte komentarje v notebooks za kompleksno kodo
   - Poskrbite, da markdown celice pojasnjujejo namen

3. **Spremembe datotek:**
   - Ne vključujte `.env` datotek (uporabite `.env.example`)
   - Ne vključujte imenikov `venv/` ali `__pycache__/`
   - Ohranite izhode notebookov, ko prikazujejo koncepte
   - Odstranite začasne datoteke in varnostne kopije notebookov (`*-backup.ipynb`)

### Format naslova PR

Uporabite opisne naslove:
- `[Lesson-XX] Dodaj nov primer za <koncept>`
- `[Fix] Popravi tipkarsko napako v lesson-XX README`
- `[Update] Izboljšaj vzorčno kodo v lesson-XX`
- `[Docs] Posodobi navodila za nastavitev`

### Zahtevani pregledi

- Notebooks morajo delovati brez napak
- README datoteke morajo biti jasne in natančne
- Upoštevajte obstoječe vzorce kode v repozitoriju
- Ohranite doslednost z drugimi lekcijami

## Dodatne opombe

### Pogoste težave

1. **Neujemanje različice Pythona:**
   - Poskrbite, da uporabljate Python 3.12+
   - Nekateri paketi morda ne delujejo s starejšimi različicami
   - Uporabite `python3 -m venv`, da izrecno določite različico Pythona

2. **Okoljske spremenljivke:**
   - Vedno ustvarite `.env` iz `.env.example`
   - Ne vključujte `.env` datoteke (je v `.gitignore`)
   - GitHub žeton potrebuje ustrezna dovoljenja

3. **Konflikti paketov:**
   - Uporabite sveže virtualno okolje
   - Namestite iz `requirements.txt` namesto posameznih paketov
   - Nekateri notebooks morda zahtevajo dodatne pakete, navedene v njihovih markdown celicah

4. **Azure storitve:**
   - Azure AI storitve zahtevajo aktivno naročnino
   - Nekatere funkcije so specifične za regijo
   - Omejitve brezplačne različice veljajo za GitHub Models

### Učni načrt

Priporočena zaporedja lekcij:
1. **00-course-setup** - Začnite tukaj za nastavitev okolja
2. **01-intro-to-ai-agents** - Razumevanje osnov AI agentov
3. **02-explore-agentic-frameworks** - Spoznajte različna ogrodja
4. **03-agentic-design-patterns** - Osnovni vzorci oblikovanja
5. Nadaljujte z oštevilčenimi lekcijami zaporedno

### Izbira ogrodja

Izberite ogrodje glede na vaše cilje:
- **Učenje/Prototipiranje**: Semantic Kernel + GitHub Models (brezplačno)
- **Sistemi z več agenti**: AutoGen
- **Najnovejše funkcije**: Microsoft Agent Framework (MAF)
- **Uvajanje v produkcijo**: Azure AI Agent Service

### Pomoč

- Pridružite se [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Preglejte README datoteke lekcij za specifične smernice
- Preverite glavno [README.md](./README.md) za pregled tečaja
- Oglejte si [Course Setup](./00-course-setup/README.md) za podrobna navodila za nastavitev

### Prispevanje

To je odprt izobraževalni projekt. Prispevki so dobrodošli:
- Izboljšajte vzorčne kode
- Popravite tipkarske napake ali napake
- Dodajte pojasnjevalne komentarje
- Predlagajte nove teme lekcij
- Prevedite v dodatne jezike

Oglejte si [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za trenutne potrebe.

## Kontekst specifičen za projekt

### Podpora za več jezikov

Ta repozitorij uporablja avtomatiziran sistem za prevajanje:
- Podpora za več kot 50 jezikov
- Prevedene datoteke v imenikih `/translations/<lang-code>/`
- GitHub Actions workflow upravlja posodobitve prevodov
- Izvorne datoteke so v angleščini v korenu repozitorija

### Struktura lekcij

Vsaka lekcija sledi doslednemu vzorcu:
1. Sličica videa s povezavo
2. Pisna vsebina lekcije (README.md)
3. Vzorčne kode v več ogrodjih
4. Cilji učenja in predpogoji
5. Povezave do dodatnih učnih virov

### Poimenovanje vzorčnih kod

Format: `<številka-lekcije>-<ime-ogrodja>.ipynb`
- `04-semantic-kernel.ipynb` - Lekcija 4, Semantic Kernel
- `07-autogen.ipynb` - Lekcija 7, AutoGen
- `14-python-agent-framework.ipynb` - Lekcija 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Lekcija 14, MAF .NET

### Posebni imeniki

- `translated_images/` - Lokalizirane slike za prevode
- `images/` - Izvirne slike za vsebino v angleščini
- `.devcontainer/` - Konfiguracija razvojnega okolja VS Code
- `.github/` - GitHub Actions workflows in predloge

### Odvisnosti

Ključni paketi iz `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen ogrodje
- `semantic-kernel` - Semantic Kernel ogrodje
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI storitve
- `azure-search-documents` - Integracija Azure AI Search
- `chromadb` - Vektorska baza podatkov za primere RAG
- `chainlit` - Okvir za klepet UI
- `browser_use` - Avtomatizacija brskalnika za agente
- `mcp[cli]` - Podpora za Model Context Protocol
- `mem0ai` - Upravljanje pomnilnika za agente

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.