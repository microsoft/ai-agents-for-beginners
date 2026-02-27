# AGENTS.md

## Pregled projekta

This repository contains "AI Agents for Beginners" - a comprehensive educational course teaching everything needed to build AI Agents. The course consists of 15+ lessons covering fundamentals, design patterns, frameworks, and production deployment of AI agents.

**Ključne tehnologije:**
- Python 3.12+
- Jupyter bilježnice za interaktivno učenje
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arhitektura:**
- Struktura temeljena na lekcijama (00-15+ directories)
- Svaka lekcija sadrži: README dokumentaciju, primjere koda (Jupyter bilježnice) i slike
- Višejezična podrška putem automatiziranog prevoditeljskog sustava
- Jedna Python bilježnica po lekciji koja koristi Microsoft Agent Framework

## Naredbe za postavljanje

### Preduvjeti
- Python 3.12 ili noviji
- Azure pretplata (za Azure AI Foundry)
- Azure CLI instaliran i autentificiran (`az login`)

### Početno postavljanje

1. **Klonirajte ili forkajte repozitorij:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ILI
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Kreirajte i aktivirajte Python virtualno okruženje:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Na Windowsu: venv\Scripts\activate
   ```

3. **Instalirajte ovisnosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Postavite varijable okruženja:**
   ```bash
   cp .env.example .env
   # Uredi .env sa svojim API ključevima i krajnjim točkama
   ```

### Potrebne varijable okruženja

Za **Azure AI Foundry** (obavezno):
- `AZURE_AI_PROJECT_ENDPOINT` - krajnja točka Azure AI Foundry projekta
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - naziv razmještaja modela (npr. gpt-4o)

Za **Azure AI Search** (Lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - krajnja točka Azure AI Search
- `AZURE_SEARCH_API_KEY` - API ključ Azure AI Search

Autentikacija: Pokrenite `az login` prije pokretanja bilježnica (koristi `AzureCliCredential`).

## Radni tijek razvoja

### Pokretanje Jupyter bilježnica

Svaka lekcija sadrži više Jupyter bilježnica za različite okvire:

1. **Pokrenite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigirajte u direktorij lekcije** (npr., `01-intro-to-ai-agents/code_samples/`)

3. **Otvorite i pokrenite bilježnice:**
   - `*-python-agent-framework.ipynb` - Korištenje Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Korištenje Microsoft Agent Framework (.NET)

### Rad s Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Zahtijeva Azure pretplatu
- Koristi `AzureAIProjectAgentProvider` za Agent Service V2 (agenti vidljivi u Foundry portalu)
- Prikladno za produkciju s ugrađenom observabilnošću
- Obrasci datoteka: `*-python-agent-framework.ipynb`

## Upute za testiranje

Ovo je edukacijski repozitorij s primjerima koda, a ne proizvodni kod s automatiziranim testovima. Za provjeru vašeg okruženja i promjena:

### Ručno testiranje

1. **Testirajte Python okruženje:**
   ```bash
   python --version  # Treba biti 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testirajte izvršavanje bilježnica:**
   ```bash
   # Pretvori bilježnicu u skriptu i pokreni (testovi uvoze)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Provjerite varijable okruženja:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Pokretanje pojedinačnih bilježnica

Otvorite bilježnice u Jupyteru i izvršavajte ćelije sekvencijalno. Svaka bilježnica je samostalna i uključuje:
- Izjave za uvoz (import statements)
- Učitavanje konfiguracije
- Primjere implementacija agenata
- Očekivane izlaze u markdown ćelijama

## Stil koda

### Python konvencije

- **Verzija Pythona**: 3.12+
- **Stil koda**: Slijedite standardne Python PEP 8 konvencije
- **Bilježnice**: Koristite jasne markdown ćelije za objašnjenja koncepata
- **Importi**: Grupirajte prema standardnoj biblioteci, trećim stranama, lokalnim importima

### Konvencije Jupyter bilježnica

- Uključite opisne markdown ćelije prije kodnih ćelija
- Dodajte primjere izlaza u bilježnicama za referencu
- Koristite jasne nazive varijabli koji odgovaraju konceptima lekcije
- Održavajte linearni redoslijed izvršavanja bilježnica (ćelija 1 → 2 → 3...)

### Organizacija datoteka

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Izgradnja i raspoređivanje

### Izrada dokumentacije

Ovaj repozitorij koristi Markdown za dokumentaciju:
- README.md datoteke u svakoj mapi lekcije
- Glavni README.md u korijenu repozitorija
- Automatizirani sustav za prevođenje putem GitHub Actions

### CI/CD cjevovod

Smešteno u `.github/workflows/`:

1. **co-op-translator.yml** - Automatski prijevod na 50+ jezika
2. **welcome-issue.yml** - Pozdravlja autore novih issueova
3. **welcome-pr.yml** - Pozdravlja nove suradnike koji otvaraju pull requestove

### Raspoređivanje

Ovo je edukacijski repozitorij - nema proces raspoređivanja. Korisnici:
1. Forkajte ili klonirajte repozitorij
2. Pokrenite bilježnice lokalno ili u GitHub Codespaces
3. Učite modificirajući i eksperimentirajući s primjerima

## Smjernice za pull requestove

### Prije slanja

1. **Testirajte svoje promjene:**
   - Pokrenite pogođene bilježnice u potpunosti
   - Provjerite da sve ćelije izvršavaju bez pogrešaka
   - Provjerite jesu li izlazi prikladni

2. **Ažuriranja dokumentacije:**
   - Ažurirajte README.md ako dodajete nove koncepte
   - Dodajte komentare u bilježnice za složeniji kod
   - Osigurajte da markdown ćelije objašnjavaju svrhu

3. **Promjene datoteka:**
   - Izbjegavajte commitanje `.env` datoteka (koristite `.env.example`)
   - Nemojte commitati `venv/` ili `__pycache__/` direktorije
   - Zadržite izlaze bilježnica kada demonstriraju koncepte
   - Uklonite privremene datoteke i backup bilježnice (`*-backup.ipynb`)

### Format naslova PR-a

Koristite opisne naslove:
- `[Lesson-XX] Dodajte novi primjer za <concept>`
- `[Fix] Ispravite tipkarsku pogrešku u lesson-XX README`
- `[Update] Poboljšajte primjer koda u lesson-XX`
- `[Docs] Ažurirajte upute za postavljanje`

### Potrebne provjere

- Bilježnice bi trebale izvršavati bez pogrešaka
- README datoteke trebaju biti jasne i točne
- Slijedite postojeće obrasce koda u repozitoriju
- Održavajte konzistentnost s drugim lekcijama

## Dodatne napomene

### Uobičajeni problemi

1. **Neslaganje verzije Pythona:**
   - Osigurajte da se koristi Python 3.12+
   - Neki paketi možda ne rade s starijim verzijama
   - Koristite `python3 -m venv` da eksplicitno navedete verziju Pythona

2. **Varijable okruženja:**
   - Uvijek kreirajte `.env` iz `.env.example`
   - Nemojte committati `.env` datoteku (nalazi se u `.gitignore`)
   - GitHub token treba odgovarajuće dozvole

3. **Sukobi paketa:**
   - Koristite novo virtualno okruženje
   - Instalirajte iz `requirements.txt` umjesto pojedinačnih paketa
   - Neke bilježnice mogu zahtijevati dodatne pakete navedene u njihovim markdown ćelijama

4. **Azure usluge:**
   - Azure AI usluge zahtijevaju aktivnu pretplatu
   - Neke značajke su specifične za regiju
   - Ograničenja besplatnog sloja primjenjuju se na GitHub Models

### Put učenja

Preporučeni redoslijed kroz lekcije:
1. **00-course-setup** - Započnite ovdje za postavljanje okruženja
2. **01-intro-to-ai-agents** - Razumijevanje osnova AI agenata
3. **02-explore-agentic-frameworks** - Upoznajte različite okvire
4. **03-agentic-design-patterns** - Osnovni dizajnerski obrasci
5. Nastavite kroz numerirane lekcije redom

### Odabir okvira

Odaberite okvir na temelju vaših ciljeva:
- **Sve lekcije**: Microsoft Agent Framework (MAF) s `AzureAIProjectAgentProvider`
- **Agenti se registriraju na poslužiteljskoj strani** u Azure AI Foundry Agent Service V2 i vidljivi su u Foundry portalu

### Dobivanje pomoći

- Pridružite se [Microsoft Foundry zajednici na Discordu](https://aka.ms/ai-agents/discord)
- Pregledajte README datoteke lekcija za specifične upute
- Provjerite glavni [README.md](./README.md) za pregled tečaja
- Pogledajte [Course Setup](./00-course-setup/README.md) za detaljne upute za postavljanje

### Doprinos

Ovo je otvoreni edukacijski projekt. Doprinosi su dobrodošli:
- Poboljšajte primjere koda
- Popravite tipkarske pogreške ili pogreške
- Dodajte pojašnjavajuće komentare
- Predložite nove teme lekcija
- Prevedite na dodatne jezike

Pogledajte [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za trenutne potrebe.

## Kontekst specifičan za projekt

### Višejezična podrška

Ovaj repozitorij koristi automatizirani sustav za prevođenje:
- Podržano 50+ jezika
- Prijevodi u direktorijima `/translations/<lang-code>/`
- GitHub Actions workflow upravlja ažuriranjima prijevoda
- Izvorne datoteke su na engleskom u korijenu repozitorija

### Struktura lekcije

Svaka lekcija slijedi dosljedan obrazac:
1. Video sličica s poveznicom
2. Pisani sadržaj lekcije (README.md)
3. Primjeri koda u više okvira
4. Ciljevi učenja i preduvjeti
5. Povezani dodatni resursi za učenje

### Nazivi primjera koda

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcija 1, MAF Python
- `14-sequential.ipynb` - Lekcija 14, MAF napredni obrasci

### Posebne direktorije

- `translated_images/` - Lokalizirane slike za prijevode
- `images/` - Izvorne slike za sadržaj na engleskom
- `.devcontainer/` - Konfiguracija razvojnog containera za VS Code
- `.github/` - GitHub Actions workflowi i predlošci

### Ovisnosti

Ključni paketi iz `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Podrška za Agent-to-Agent protokol
- `azure-ai-inference`, `azure-ai-projects` - Azure AI usluge
- `azure-identity` - Azure autentikacija (AzureCliCredential)
- `azure-search-documents` - Integracija Azure AI Search
- `mcp[cli]` - Podrška za Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Odricanje od odgovornosti:
Ovaj je dokument preveden pomoću AI usluge prevođenja Co-op Translator (https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati mjerodavnim izvorom. Za važne ili kritične informacije preporučuje se profesionalni (ljudski) prijevod. Ne odgovaramo za bilo kakve nesporazume ili pogrešna tumačenja koja proizađu iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->