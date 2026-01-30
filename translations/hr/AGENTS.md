# AGENTS.md

## Pregled projekta

Ovaj repozitorij sadrži "AI Agents for Beginners" - sveobuhvatan edukacijski tečaj koji podučava sve potrebno za izradu AI agenata. Tečaj se sastoji od više od 15 lekcija koje pokrivaju osnove, dizajnerske obrasce, okvire i implementaciju AI agenata u produkciji.

**Ključne tehnologije:**
- Python 3.12+
- Jupyter Notebooks za interaktivno učenje
- AI okviri: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI usluge: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (dostupan besplatni plan)

**Arhitektura:**
- Struktura temeljena na lekcijama (00-15+ direktoriji)
- Svaka lekcija sadrži: README dokumentaciju, primjere koda (Jupyter bilježnice) i slike
- Podrška za više jezika putem automatiziranog sustava za prijevod
- Više opcija okvira po lekciji (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Postavljanje okruženja

### Preduvjeti
- Python 3.12 ili noviji
- GitHub račun (za GitHub Models - besplatni plan)
- Azure pretplata (opcionalno, za Azure AI usluge)

### Početno postavljanje

1. **Klonirajte ili forkajte repozitorij:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Kreirajte i aktivirajte Python virtualno okruženje:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Instalirajte ovisnosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Postavite varijable okruženja:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Potrebne varijable okruženja

Za **GitHub Models (besplatno)**:
- `GITHUB_TOKEN` - Osobni pristupni token s GitHuba

Za **Azure AI usluge** (opcionalno):
- `PROJECT_ENDPOINT` - Endpoint projekta Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - API ključ za Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL endpointa za Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Naziv implementacije za chat model
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Naziv implementacije za embeddings
- Dodatna konfiguracija za Azure prikazana u `.env.example`

## Radni tijek razvoja

### Pokretanje Jupyter bilježnica

Svaka lekcija sadrži više Jupyter bilježnica za različite okvire:

1. **Pokrenite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigirajte do direktorija lekcije** (npr. `01-intro-to-ai-agents/code_samples/`)

3. **Otvorite i pokrenite bilježnice:**
   - `*-semantic-kernel.ipynb` - Korištenje Semantic Kernel okvira
   - `*-autogen.ipynb` - Korištenje AutoGen okvira
   - `*-python-agent-framework.ipynb` - Korištenje Microsoft Agent Frameworka (Python)
   - `*-dotnet-agent-framework.ipynb` - Korištenje Microsoft Agent Frameworka (.NET)
   - `*-azureaiagent.ipynb` - Korištenje Azure AI Agent Service

### Rad s različitim okvirima

**Semantic Kernel + GitHub Models:**
- Dostupan besplatni plan s GitHub računom
- Dobro za učenje i eksperimentiranje
- Uzorak datoteke: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Dostupan besplatni plan s GitHub računom
- Sposobnosti orkestracije više agenata
- Uzorak datoteke: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Najnoviji okvir od Microsofta
- Dostupan u Pythonu i .NET-u
- Uzorak datoteke: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Zahtijeva Azure pretplatu
- Značajke spremne za produkciju
- Uzorak datoteke: `*-azureaiagent.ipynb`

## Upute za testiranje

Ovo je edukacijski repozitorij s primjerima koda, a ne produkcijski kod s automatiziranim testovima. Za provjeru postavki i promjena:

### Ručno testiranje

1. **Testirajte Python okruženje:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Testirajte izvršavanje bilježnica:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Provjerite varijable okruženja:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Pokretanje pojedinačnih bilježnica

Otvorite bilježnice u Jupyteru i izvršavajte ćelije redom. Svaka bilježnica je samostalna i uključuje:
- Import naredbe
- Učitavanje konfiguracije
- Primjere implementacije agenata
- Očekivane izlaze u markdown ćelijama

## Stil koda

### Python konvencije

- **Python verzija**: 3.12+
- **Stil koda**: Slijedite standardne Python PEP 8 konvencije
- **Bilježnice**: Koristite jasne markdown ćelije za objašnjenje koncepata
- **Importi**: Grupirajte prema standardnoj biblioteci, trećim stranama, lokalnim importima

### Konvencije za Jupyter bilježnice

- Uključite opisne markdown ćelije prije ćelija s kodom
- Dodajte primjere izlaza u bilježnicama za referencu
- Koristite jasne nazive varijabli koji odgovaraju konceptima lekcije
- Održavajte linearni redoslijed izvršavanja bilježnice (ćelija 1 → 2 → 3...)

### Organizacija datoteka

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

## Izrada i implementacija

### Izrada dokumentacije

Ovaj repozitorij koristi Markdown za dokumentaciju:
- README.md datoteke u svakom direktoriju lekcije
- Glavni README.md u korijenu repozitorija
- Automatizirani sustav za prijevod putem GitHub Actions

### CI/CD cjevovod

Smješten u `.github/workflows/`:

1. **co-op-translator.yml** - Automatski prijevod na više od 50 jezika
2. **welcome-issue.yml** - Pozdravlja autore novih problema
3. **welcome-pr.yml** - Pozdravlja autore novih pull requestova

### Implementacija

Ovo je edukacijski repozitorij - nema procesa implementacije. Korisnici:
1. Forkaju ili kloniraju repozitorij
2. Pokreću bilježnice lokalno ili u GitHub Codespaces
3. Uče modificiranjem i eksperimentiranjem s primjerima

## Smjernice za pull requestove

### Prije slanja

1. **Testirajte svoje promjene:**
   - Potpuno pokrenite zahvaćene bilježnice
   - Provjerite da se sve ćelije izvršavaju bez grešaka
   - Provjerite da su izlazi odgovarajući

2. **Ažuriranja dokumentacije:**
   - Ažurirajte README.md ako dodajete nove koncepte
   - Dodajte komentare u bilježnicama za složeniji kod
   - Osigurajte da markdown ćelije objašnjavaju svrhu

3. **Promjene datoteka:**
   - Izbjegavajte commitanje `.env` datoteka (koristite `.env.example`)
   - Nemojte commitati direktorije `venv/` ili `__pycache__/`
   - Zadržite izlaze bilježnica kada demonstriraju koncepte
   - Uklonite privremene datoteke i backup bilježnice (`*-backup.ipynb`)

### Format naslova PR-a

Koristite opisne naslove:
- `[Lesson-XX] Dodaj novi primjer za <koncept>`
- `[Fix] Ispravi tipfeler u README lekcije-XX`
- `[Update] Poboljšaj primjer koda u lekciji-XX`
- `[Docs] Ažuriraj upute za postavljanje`

### Potrebne provjere

- Bilježnice se trebaju izvršavati bez grešaka
- README datoteke trebaju biti jasne i točne
- Slijedite postojeće obrasce koda u repozitoriju
- Održavajte dosljednost s ostalim lekcijama

## Dodatne napomene

### Česte poteškoće

1. **Neusklađenost verzije Pythona:**
   - Osigurajte da koristite Python 3.12+
   - Neki paketi možda neće raditi s starijim verzijama
   - Koristite `python3 -m venv` za eksplicitno određivanje verzije Pythona

2. **Varijable okruženja:**
   - Uvijek kreirajte `.env` iz `.env.example`
   - Nemojte commitati `.env` datoteku (nalazi se u `.gitignore`)
   - GitHub token treba odgovarajuće dozvole

3. **Sukobi paketa:**
   - Koristite svježe virtualno okruženje
   - Instalirajte iz `requirements.txt` umjesto pojedinačnih paketa
   - Neke bilježnice mogu zahtijevati dodatne pakete navedene u njihovim markdown ćelijama

4. **Azure usluge:**
   - Azure AI usluge zahtijevaju aktivnu pretplatu
   - Neke značajke su specifične za regiju
   - Ograničenja besplatnog plana primjenjuju se na GitHub Models

### Put učenja

Preporučeni redoslijed prolaska kroz lekcije:
1. **00-course-setup** - Započnite ovdje za postavljanje okruženja
2. **01-intro-to-ai-agents** - Razumijevanje osnova AI agenata
3. **02-explore-agentic-frameworks** - Učenje o različitim okvirima
4. **03-agentic-design-patterns** - Ključni dizajnerski obrasci
5. Nastavite kroz numerirane lekcije redom

### Odabir okvira

Odaberite okvir prema svojim ciljevima:
- **Učenje/Prototipiranje**: Semantic Kernel + GitHub Models (besplatno)
- **Sustavi s više agenata**: AutoGen
- **Najnovije značajke**: Microsoft Agent Framework (MAF)
- **Implementacija u produkciji**: Azure AI Agent Service

### Dobivanje pomoći

- Pridružite se [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Pregledajte README datoteke lekcija za specifične smjernice
- Provjerite glavni [README.md](./README.md) za pregled tečaja
- Pogledajte [Course Setup](./00-course-setup/README.md) za detaljne upute za postavljanje

### Doprinos

Ovo je otvoreni edukacijski projekt. Doprinosi su dobrodošli:
- Poboljšajte primjere koda
- Ispravite tipfelere ili greške
- Dodajte pojašnjavajuće komentare
- Predložite nove teme lekcija
- Prevedite na dodatne jezike

Pogledajte [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za trenutne potrebe.

## Kontekst specifičan za projekt

### Podrška za više jezika

Ovaj repozitorij koristi automatizirani sustav za prijevod:
- Podržano više od 50 jezika
- Prijevodi u direktorijima `/translations/<lang-code>/`
- GitHub Actions workflow upravlja ažuriranjima prijevoda
- Izvorne datoteke su na engleskom u korijenu repozitorija

### Struktura lekcija

Svaka lekcija slijedi dosljedan obrazac:
1. Video thumbnail s poveznicom
2. Pisani sadržaj lekcije (README.md)
3. Primjeri koda u više okvira
4. Ciljevi učenja i preduvjeti
5. Dodatni resursi za učenje povezani

### Nazivanje uzoraka koda

Format: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Lekcija 4, Semantic Kernel
- `07-autogen.ipynb` - Lekcija 7, AutoGen
- `14-python-agent-framework.ipynb` - Lekcija 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Lekcija 14, MAF .NET

### Posebni direktoriji

- `translated_images/` - Lokalizirane slike za prijevode
- `images/` - Originalne slike za sadržaj na engleskom
- `.devcontainer/` - Konfiguracija razvojnog okruženja za VS Code
- `.github/` - GitHub Actions workflowi i predlošci

### Ovisnosti

Ključni paketi iz `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen okvir
- `semantic-kernel` - Semantic Kernel okvir
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI usluge
- `azure-search-documents` - Integracija Azure AI Search
- `chromadb` - Vektorska baza podataka za RAG primjere
- `chainlit` - Okvir za chat UI
- `browser_use` - Automatizacija preglednika za agente
- `mcp[cli]` - Podrška za Model Context Protocol
- `mem0ai` - Upravljanje memorijom za agente

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.