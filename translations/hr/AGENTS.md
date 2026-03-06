# AGENTS.md

## Pregled projekta

Ovo spremište sadrži "AI Agents for Beginners" - sveobuhvatan edukacijski tečaj koji podučava sve što je potrebno za izgradnju AI agenata. Tečaj se sastoji od 15+ lekcija koje pokrivaju osnove, obrasce dizajna, okvire i produkcijsko postavljanje AI agenata.

**Ključne tehnologije:**
- Python 3.12+
- Jupyter Notebooks za interaktivno učenje
- AI okviri: Microsoft Agent Framework (MAF)
- Azure AI usluge: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arhitektura:**
- Struktura temeljena na lekcijama (direktoriji 00-15+)
- Svaka lekcija sadrži: README dokumentaciju, primjere koda (Jupyter bilježnice) i slike
- Podrška za više jezika putem automatiziranog sustava prijevoda
- Jedna Python bilježnica po lekciji koristeći Microsoft Agent Framework

## Komande za postavljanje

### Preduvjeti
- Python 3.12 ili noviji
- Azure pretplata (za Azure AI Foundry)
- Azure CLI instaliran i autentificiran (`az login`)

### Početno postavljanje

1. **Klonirajte ili forkajte spremište:**
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

4. **Postavite varijable okoline:**
   ```bash
   cp .env.example .env
   # Uredi .env s vašim API ključevima i endpointima
   ```

### Potrebne varijable okoline

Za **Azure AI Foundry** (Obavezno):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry projekt endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Naziv implementacije modela (npr., gpt-4o)

Za **Azure AI Search** (Lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API ključ

Autentikacija: Pokrenite `az login` prije pokretanja bilježnica (koristi `AzureCliCredential`).

## Razvojni tijek

### Pokretanje Jupyter bilježnica

Svaka lekcija sadrži više Jupyter bilježnica za različite okvire:

1. **Pokrenite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigirajte do direktorija lekcije** (npr., `01-intro-to-ai-agents/code_samples/`)

3. **Otvorite i pokrenite bilježnice:**
   - `*-python-agent-framework.ipynb` - Korištenje Microsoft Agent Frameworka (Python)
   - `*-dotnet-agent-framework.ipynb` - Korištenje Microsoft Agent Frameworka (.NET)

### Rad s Microsoft Agent Frameworkom

**Microsoft Agent Framework + Azure AI Foundry:**
- Potrebna Azure pretplata
- Koristi `AzureAIProjectAgentProvider` za Agent Service V2 (agenti vidljivi u Foundry portalu)
- Spreman za produkciju s ugrađenom uvidljivošću
- Obrasci datoteka: `*-python-agent-framework.ipynb`

## Upute za testiranje

Ovo je edukacijsko spremište s primjerima koda, a ne produkcijski kod s automatiziranim testovima. Za provjeru vašeg okruženja i promjena:

### Ručno testiranje

1. **Testirajte Python okruženje:**
   ```bash
   python --version  # Treba biti 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testirajte izvršavanje bilježnice:**
   ```bash
   # Pretvori bilježnicu u skriptu i pokreni (importi testova)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Provjerite varijable okoline:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Pokretanje pojedinačnih bilježnica

Otvorite bilježnice u Jupyteru i izvršavajte ćelije redom. Svaka bilježnica je samostalna i uključuje:
- Izjave o uvozu
- Učitavanje konfiguracije
- Primjere implementacija agenta
- Očekivane izlaze u markdown ćelijama

## Stil koda

### Python konvencije

- **Python verzija**: 3.12+
- **Stil koda**: Slijedite standardne Python PEP 8 konvencije
- **Bilježnice**: Koristite jasne markdown ćelije za objašnjenje koncepata
- **Uvozi**: Grupirajte po standardnoj biblioteci, third-party i lokalnim uvozima

### Konvencije za Jupyter bilježnice

- Uključite opisne markdown ćelije prije kodnih ćelija
- Dodajte primjere izlaza u bilježnicama za referencu
- Koristite jasna imena varijabli koja odgovaraju konceptima lekcije
- Održavajte linearni redoslijed izvršavanja bilježnice (ćelija 1 → 2 → 3...)

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

## Izgradnja i postavljanje

### Izrada dokumentacije

Ovo spremište koristi Markdown za dokumentaciju:
- README.md datoteke u svakom folderu s lekcijama
- Glavni README.md u korijenu spremišta
- Automatizirani sustav prijevoda putem GitHub Actions

### CI/CD pipeline

Nalazi se u `.github/workflows/`:

1. **co-op-translator.yml** - Automatski prijevod na 50+ jezika
2. **welcome-issue.yml** - Dobrodošlica autorima novih issueova
3. **welcome-pr.yml** - Dobrodošlica autorima novih pull requestova

### Postavljanje

Ovo je edukacijsko spremište - nema proces postavljanja. Korisnici:
1. Forkaju ili kloniraju spremište
2. Pokreću bilježnice lokalno ili u GitHub Codespaces
3. Uče modificirajući i eksperimentirajući s primjerima

## Smjernice za Pull Requestove

### Prije slanja

1. **Testirajte svoje promjene:**
   - Pokrenite pogođene bilježnice u cijelosti
   - Provjerite da se sve ćelije izvršavaju bez grešaka
   - Provjerite da su izlazi prikladni

2. **Ažuriranja dokumentacije:**
   - Ažurirajte README.md ako dodajete nove koncepte
   - Dodajte komentare u bilježnicama za složeniji kod
   - Osigurajte da markdown ćelije objašnjavaju svrhu

3. **Promjene datoteka:**
   - Izbjegavajte commitanje `.env` datoteka (koristite `.env.example`)
   - Nemojte commitati `venv/` ili `__pycache__/` direktorije
   - Zadržite izlaze bilježnica kada demonstriraju koncepte
   - Uklonite privremene datoteke i backup bilježnice (`*-backup.ipynb`)

### Format naslova PR-a

Koristite opisne naslove:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Potrebne provjere

- Bilježnice se trebaju izvršavati bez grešaka
- README datoteke trebaju biti jasne i točne
- Slijedite postojeće obrasce koda u spremištu
- Održavajte dosljednost s ostalim lekcijama

## Dodatne napomene

### Uobičajene zamke

1. **Neusklađenost verzije Pythona:**
   - Osigurajte da se koristi Python 3.12+
   - Neki paketi možda neće raditi s starijim verzijama
   - Koristite `python3 -m venv` da eksplicitno odredite verziju Pythona

2. **Varijable okoline:**
   - Uvijek kreirajte `.env` iz `.env.example`
   - Nemojte commitati `.env` datoteku (nalazi se u `.gitignore`)
   - GitHub token treba odgovarajuće dozvole

3. **Konflikti paketa:**
   - Koristite svježe virtualno okruženje
   - Instalirajte iz `requirements.txt` umjesto pojedinačnih paketa
   - Neke bilježnice mogu zahtijevati dodatne pakete navedene u njihovim markdown ćelijama

4. **Azure usluge:**
   - Azure AI usluge zahtijevaju aktivnu pretplatu
   - Neke značajke su specifične za regiju
   - Ograničenja besplatnog sloja primjenjuju se na GitHub Models

### Put učenja

Preporučeni slijed kroz lekcije:
1. **00-course-setup** - Počnite ovdje za postavljanje okruženja
2. **01-intro-to-ai-agents** - Razumijevanje osnova AI agenata
3. **02-explore-agentic-frameworks** - Učenje o različitim okvirima
4. **03-agentic-design-patterns** - Temeljni obrasci dizajna
5. Nastavite kroz numerirane lekcije redom

### Odabir okvira

Odaberite okvir ovisno o svojim ciljevima:
- **Sve lekcije**: Microsoft Agent Framework (MAF) s `AzureAIProjectAgentProvider`
- **Agenti se registriraju server-side** u Azure AI Foundry Agent Service V2 i vidljivi su u Foundry portalu

### Dobivanje pomoći

- Pridružite se [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Pregledajte README datoteke lekcija za specifične upute
- Provjerite glavni [README.md](./README.md) za pregled tečaja
- Pogledajte [Course Setup](./00-course-setup/README.md) za detaljne upute o postavljanju

### Doprinos

Ovo je otvoreni edukacijski projekt. Dobrodošli su doprinosi:
- Poboljšajte primjere koda
- Ispravite tipografske pogreške ili greške
- Dodajte pojašnjavajuće komentare
- Predložite nove teme lekcija
- Prevedite na dodatne jezike

Pogledajte [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za trenutne potrebe.

## Kontekst specifičan za projekt

### Podrška za više jezika

Ovo spremište koristi automatizirani sustav prijevoda:
- Podrška za 50+ jezika
- Prijevodi u direktorijima `/translations/<lang-code>/`
- GitHub Actions workflow obrađuje ažuriranja prijevoda
- Izvorne datoteke su na engleskom u korijenu spremišta

### Struktura lekcije

Svaka lekcija slijedi dosljedan obrazac:
1. Video thumbnail s linkom
2. Napisani sadržaj lekcije (README.md)
3. Primjeri koda u više okvira
4. Ciljevi učenja i preduvjeti
5. Dodatni resursi za učenje povezani

### Imenovanje primjera koda

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcija 1, MAF Python
- `14-sequential.ipynb` - Lekcija 14, MAF napredni obrasci

### Posebni direktoriji

- `translated_images/` - Lokalizirane slike za prijevode
- `images/` - Izvorne slike za sadržaj na engleskom
- `.devcontainer/` - VS Code konfiguracija development containera
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
**Odricanje odgovornosti**:
Ovaj je dokument preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->