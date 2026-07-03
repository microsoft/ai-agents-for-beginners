# AGENTS.md

## Pregled projekta

Ovaj spremnik sadrži "AI agente za početnike" - sveobuhvatni edukacijski tečaj koji uči sve što je potrebno za izgradnju AI agenata. Tečaj se sastoji od 18 lekcija koje pokrivaju osnove, dizajnerske obrasce, okvire i produkcijsko postavljanje AI agenata.

**Ključne tehnologije:**
- Python 3.12+
- Jupyter bilježnice za interaktivno učenje
- AI okviri: Microsoft Agent Framework (MAF)
- Azure AI usluge: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arhitektura:**
- Struktura bazirana na lekcijama (direktoriji 00-15+)
- Svaka lekcija sadrži: README dokumentaciju, primjere koda (Jupyter bilježnice) i slike
- Podrška za više jezika putem automatiziranog sustava prevođenja
- Jedna Python bilježnica po lekciji koristeći Microsoft Agent Framework

## Komande za postavljanje

### Preduvjeti
- Python 3.12 ili noviji
- Azure pretplata (za Azure AI Foundry)
- Instaliran i autentificiran Azure CLI (`az login`)

### Početno postavljanje

1. **Klonirajte ili forkajte spremnik:**
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
   # Uredite .env s vašim API ključevima i krajnjim točkama
   ```

### Potrebne varijable okoline

Za **Azure AI Foundry** (obavezno):
- `AZURE_AI_PROJECT_ENDPOINT` - krajnja točka Azure AI Foundry projekta
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ime modela za raspoređivanje (npr. gpt-4o)

Za **Azure AI Search** (Lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - krajnja točka Azure AI Search-a
- `AZURE_SEARCH_API_KEY` - API ključ za Azure AI Search

Autentifikacija: Pokrenite `az login` prije pokretanja bilježnica (koristi `AzureCliCredential`).

## Razvojni tijek rada

### Pokretanje Jupyter bilježnica

Svaka lekcija sadrži više Jupyter bilježnica za različite okvire:

1. **Pokrenite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigirajte do direktorija lekcije** (npr. `01-intro-to-ai-agents/code_samples/`)

3. **Otvorite i pokrenite bilježnice:**
   - `*-python-agent-framework.ipynb` - Koristeći Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Koristeći Microsoft Agent Framework (.NET)

### Rad s Microsoft Agent Frameworkom

**Microsoft Agent Framework + Azure AI Foundry:**
- Zahtijeva Azure pretplatu
- Koristi `AzureAIProjectAgentProvider` za Agent Service V2 (agenti vidljivi u Foundry portalu)
- Spreman za produkciju s ugrađenom promatranjem
- Uzorak datoteke: `*-python-agent-framework.ipynb`

## Upute za testiranje

Ovo je edukativni spremnik s primjerima koda, a ne produkcijski kod s automatiziranim testovima. Za provjeru postavki i promjena:

### Ručno testiranje

1. **Testirajte Python okruženje:**
   ```bash
   python --version  # Trebalo bi biti 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testirajte izvršenje bilježnica:**
   ```bash
   # Pretvori bilježnicu u skriptu i pokreni (testira uvoze)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Provjerite varijable okoline:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Pokretanje pojedinačnih bilježnica

Otvorite bilježnice u Jupyteru i izvršavajte ćelije redom. Svaka bilježnica je samostalna i sadrži:
- Izjave o uvozu
- Učitavanje konfiguracije
- Primjere implementacije agenata
- Očekivane izlaze u markdown ćelijama

## Stil koda

### Python konvencije

- **Python verzija**: 3.12+
- **Stil koda**: Slijedite standardne Python PEP 8 konvencije
- **Bilježnice**: Koristite jasne markdown ćelije za objašnjenje koncepata
- **Uvozi**: Grupirajte prema standardnoj biblioteci, trećim stranama i lokalnim importima

### Jupyter bilježnice konvencije

- Uključite opisne markdown ćelije prije kodnih ćelija
- Dodajte primjere izlaza u bilježnicama za referencu
- Koristite jasne nazive varijabli koji se podudaraju s konceptima lekcije
- Održavajte linearni redoslijed izvršavanja bilježnice (ćelija 1 → 2 → 3…)

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

### Izgradnja dokumentacije

Ovaj spremnik koristi Markdown za dokumentaciju:
- README.md datoteke u svakoj mapi lekcije
- Glavni README.md u korijenu spremnika
- Automatizirani sustav prevođenja putem GitHub Actions

### CI/CD pipeline

Nalazi se u `.github/workflows/`:

1. **co-op-translator.yml** - Automatski prijevod na 50+ jezika
2. **welcome-issue.yml** - Dobrodošlica za nove autore problema
3. **welcome-pr.yml** - Dobrodošlica za nove suradnike pull requestova

### Postavljanje

Ovo je edukativni spremnik - nema procesa postavljanja. Korisnici:
1. Forkaju ili kloniraju spremnik
2. Pokreću bilježnice lokalno ili u GitHub Codespaces
3. Uče modificiranjem i eksperimentiranjem s primjerima

## Smjernice za pull requestove

### Prije slanja

1. **Testirajte svoje promjene:**
   - Potpuno pokrenite pogođene bilježnice
   - Provjerite da se sve ćelije izvršavaju bez grešaka
   - Provjerite jesu li izlazi prikladni

2. **Ažuriranja dokumentacije:**
   - Ažurirajte README.md ako dodajete nove koncepte
   - Dodajte komentare u bilježnice za složeniji kod
   - Osigurajte da markdown ćelije objašnjavaju svrhu

3. **Promjene datoteka:**
   - Izbjegavajte commitanje `.env` datoteka (koristite `.env.example`)
   - Ne commitajte direktorije `venv/` ili `__pycache__/`
   - Ostavite izlaze bilježnica ako prikazuju koncepte
   - Uklonite privremene datoteke i backup bilježnice (`*-backup.ipynb`)

### Format naslova PR-a

Koristite opisne naslove:
- `[Lesson-XX] Dodaj novi primjer za <koncept>`
- `[Fix] Ispravi tipfelere u lesson-XX README`
- `[Update] Poboljšaj primjer koda u lesson-XX`
- `[Docs] Ažuriraj upute za postavljanje`

### Potrebne provjere

- Bilježnice se trebaju izvršavati bez grešaka
- README datoteke trebaju biti jasne i točne
- Slijedite postojeće obrasce koda u spremniku
- Održavajte dosljednost s ostalim lekcijama

## Dodatne napomene

### Uobičajene poteškoće

1. **Neusklađenost verzije Pythona:**
   - Pazite da koristite Python 3.12+
   - Neki paketi možda neće raditi s starijim verzijama
   - Koristite `python3 -m venv` za eksplicitno odabiranje verzije Pythona

2. **Varijable okoline:**
   - Uvijek kreirajte `.env` iz `.env.example`
   - Ne commitajte `.env` datoteku (nalazi se u `.gitignore`)
   - GitHub token treba odgovarajuće dozvole

3. **Sukobi paketa:**
   - Koristite novo virtualno okruženje
   - Instalirajte iz `requirements.txt` umjesto pojedinačnih paketa
   - Neke bilježnice mogu zahtijevati dodatne pakete navedene u njihovim markdown ćelijama

4. **Azure usluge:**
   - Azure AI usluge zahtijevaju aktivnu pretplatu
   - Neke značajke su specifične za regiju
   - Ograničenja besplatnog sloja vrijede za GitHub modele

### Put učenja

Preporučeni redoslijed kroz lekcije:
1. **00-course-setup** - Početak za postavljanje okruženja
2. **01-intro-to-ai-agents** - Razumijevanje osnova AI agenata
3. **02-explore-agentic-frameworks** - Učenje o različitim okvirima
4. **03-agentic-design-patterns** - Ključni dizajnerski obrasci
5. Nastavite kroz numerirane lekcije redom

### Odabir okvira

Odaberite okvir prema svojim ciljevima:
- **Sve lekcije**: Microsoft Agent Framework (MAF) s `AzureAIProjectAgentProvider`
- **Agenti se registriraju server-side** u Azure AI Foundry Agent Service V2 i vidljivi su u Foundry portalu

### Dobivanje pomoći

- Pridružite se [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Pregledajte README datoteke lekcija za specifične upute
- Provjerite glavni [README.md](./README.md) za pregled tečaja
- Pogledajte [Course Setup](./00-course-setup/README.md) za detaljne upute postavljanja

### Doprinos

Ovo je otvoreni edukacijski projekt. Dobrodošli doprinosi:
- Poboljšajte primjere koda
- Ispravite tipfelere ili greške
- Dodajte jasnije komentare
- Predložite nove teme lekcija
- Prevedite na dodatne jezike

Pogledajte [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za aktualne potrebe.

## Kontekst specifičan za projekt

### Podrška za više jezika

Ovaj spremnik koristi automatizirani sustav prevođenja:
- Podržano 50+ jezika
- Prijevodi u direktorijima `/translations/<lang-code>/`
- GitHub Actions workflow upravlja ažuriranjima prijevoda
- Izvorne datoteke su na engleskom u korijenu spremnika

### Struktura lekcija

Svaka lekcija slijedi dosljedni obrazac:
1. Video thumbnail s linkom
2. Pisani sadržaj lekcije (README.md)
3. Primjeri koda u više okvira
4. Ciljevi učenja i preduvjeti
5. Povezani dodatni izvori učenja

### Nazivanje primjera koda

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcija 1, MAF Python
- `14-sequential.ipynb` - Lekcija 14, MAF napredni obrasci

### Posebni direktoriji

- `translated_images/` - Lokalizirane slike za prijevode
- `images/` - Izvorne slike za engleski sadržaj
- `.devcontainer/` - Konfiguracija VS Code razvojnih kontejnera
- `.github/` - GitHub Actions workflow-i i predlošci

### Ovisnosti

Ključni paketi iz `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Podrška za Agent-to-Agent protokol
- `azure-ai-inference`, `azure-ai-projects` - Azure AI usluge
- `azure-identity` - Azure autentifikacija (AzureCliCredential)
- `azure-search-documents` - Integracija Azure AI Search
- `mcp[cli]` - Podrška za Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->