# AGENTS.md

## Pregled projekta

Ovaj repozitorij sadrži "AI agente za početnike" - sveobuhvatan obrazovni tečaj koji podučava sve potrebno za izradu AI agenata. Tečaj se sastoji od 18 lekcija (numeriranih od 00 do 18) koje pokrivaju osnove, dizajnerske obrasce, okvire, proizvodno postavljanje, lokalne/agente na uređajima i sigurnost AI agenata.

**Ključne tehnologije:**
- Python 3.12+
- Jupyter bilježnice za interaktivno učenje
- AI okviri: Microsoft Agent Framework (MAF)
- Azure AI usluge: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitektura:**
- Struktura temeljena na lekcijama (direktoriji 00-18)
- Svaka lekcija sadrži: README dokumentaciju, primjere koda (Jupyter bilježnice) i slike
- Podrška za više jezika putem automatiziranog sustava prijevoda
- Jedna Python bilježnica po lekciji koja koristi Microsoft Agent Framework

## Komande za postavljanje

### Preduvjeti
- Python 3.12 ili noviji
- Azure pretplata (za Microsoft Foundry)
- Azure CLI instaliran i autentificiran (`az login`)

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

Za **Microsoft Foundry** (obavezno):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry krajnja točka projekta
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Naziv modela za postavljanje (npr. gpt-5-mini)

Za **Azure AI Search** (Lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search krajnja točka
- `AZURE_SEARCH_API_KEY` - Azure AI Search API ključ

Autentifikacija: Pokrenite `az login` prije pokretanja bilježnica (koristi `AzureCliCredential`).

## Razvojni tijek rada

### Pokretanje Jupyter bilježnica

Svaka lekcija sadrži više Jupyter bilježnica za različite okvire:

1. **Pokrenite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Idite u direktorij lekcije** (npr. `01-intro-to-ai-agents/code_samples/`)

3. **Otvorite i pokrenite bilježnice:**
   - `*-python-agent-framework.ipynb` - Korištenje Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Korištenje Microsoft Agent Framework (.NET)

### Rad s Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Zahtijeva Azure pretplatu
- Koristi `FoundryChatClient` za Agent Service V2 (agenti vidljivi u Foundry portalu)
- Spreman za produkciju s ugrađenom opservabilnošću
- Obrasci datoteka: `*-python-agent-framework.ipynb`

## Upute za testiranje

Ovo je obrazovni repozitorij sa primjerima koda, a ne produkcijski kod s automatiziranim testovima. Za provjeru postavki i promjena:

### Ručno testiranje

1. **Testirajte Python okruženje:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testirajte izvršavanje bilježnice:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Provjerite varijable okruženja:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Pokretanje pojedinačnih bilježnica

Otvorite bilježnice u Jupyter i izvršavajte ćelije redom. Svaka bilježnica je samostalna i uključuje:
- Izjave o uvozu
- Učitavanje konfiguracije
- Primjere implementacije agenta
- Očekivane izlaze u markdown ćelijama

### Smoke-testiranje postavljenih agenata

Za lekcije gdje je agent postavljen kao Microsoft Foundry hostani agent (01, 04, 05, 16), repozitorij sadrži smoke-test kataloge u `tests/` koji se pokreću putem `.github/workflows/smoke-test.yml` tijeka rada preko [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) akcije. To je lagani post-deploy test (je li agent dostupan i slijedi osnovna očekivanja prompta?), koji nadopunjuje evaluacijski pipeline u lekcijama 10 i 16. Pogledajte [tests/README.md](./tests/README.md) za mapiranje kataloga-lekcija-agenta. Lekcija 17 se izvršava lokalno s Foundry Local i nema hostani endpoint, stoga se provjerava pokretanjem njene bilježnice izravno.

## Stil kodiranja

### Python konvencije

- **Python verzija**: 3.12+
- **Stil kodiranja**: Slijediti standardne Python PEP 8 konvencije
- **Bilježnice**: Koristite jasne markdown ćelije za objašnjenje koncepata
- **Uvozi**: Grupirajte standardnu biblioteku, third-party i lokalne uvoze

### Jupyter bilježničke konvencije

- Uključite opisne markdown ćelije prije ćelija koda
- Dodajte primjere izlaza u bilježnicama kao referencu
- Koristite jasne nazive varijabli koje odgovaraju konceptima lekcije
- Održavajte linearni redoslijed izvršavanja ćelija (ćelija 1 → 2 → 3...)

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

Ovaj repozitorij koristi Markdown za dokumentaciju:
- README.md datoteke u svakom direktoriju lekcije
- Glavni README.md u korijenu repozitorija
- Automatizirani sustav prijevoda putem GitHub Actions

### CI/CD pipeline

Smješten u `.github/workflows/`:

1. **co-op-translator.yml** - Automatski prijevod na 50+ jezika
2. **welcome-issue.yml** - Pozdravlja autore novih problema
3. **welcome-pr.yml** - Pozdravlja autore novih pull requestova

### Postavljanje

Ovo je obrazovni repozitorij - nema procesa postavljanja. Korisnici:
1. Forkaju ili kloniraju repozitorij
2. Pokreću bilježnice lokalno ili u GitHub Codespaces
3. Uče modifikacijama i eksperimentiranjem s primjerima

## Smjernice za pull requestove

### Prije slanja

1. **Testirajte svoje promjene:**
   - Potpuno pokrenite pogođene bilježnice
   - Provjerite da sve ćelije izvršavaju bez grešaka
   - Provjerite jesu li izlazi primjereni

2. **Ažuriranja dokumentacije:**
   - Ažurirajte README.md ako dodajete nove koncepte
   - Dodajte komentare u bilježnicama za složeniji kod
   - Osigurajte da markdown ćelije objašnjavaju svrhu

3. **Promjene datoteka:**
   - Izbjegavajte commitati `.env` datoteke (koristite `.env.example`)
   - Ne commitajte `venv/` ili `__pycache__/` direktorije
   - Održavajte izlaze bilježnica kada ilustriraju koncepte
   - Uklonite privremene i backup datoteke (`*-backup.ipynb`)

### Format naslova PR-a

Koristite opisne naslove:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Obavezne provjere

- Bilježnice bi trebale izvršavati bez grešaka
- README datoteke trebaju biti jasne i točne
- Slijedite postojeće obrasce koda u repozitoriju
- Održavajte dosljednost s ostalim lekcijama

## Dodatne bilješke

### Uobičajene zamke

1. **Nepodudaranje verzije Pythona:**
   - Osigurajte da koristite Python 3.12+
   - Neki paketi možda neće raditi s starijim verzijama
   - Koristite `python3 -m venv` za eksplicitno specificiranje verzije Pythona

2. **Varijable okruženja:**
   - Uvijek kreirajte `.env` iz `.env.example`
   - Ne commitajte `.env` datoteku (nalazi se u `.gitignore`)
   - Prijavite se uz `az login` za prijavu bez ključa putem Entra ID

3. **Sukobi paketa:**
   - Koristite svježe virtualno okruženje
   - Instalirajte iz `requirements.txt` umjesto pojedinačnih paketa
   - Neke bilježnice mogu zahtijevati dodatne pakete navedene u njihovim markdown ćelijama

4. **Azure usluge:**
   - Azure AI usluge zahtijevaju aktivnu pretplatu
   - Neke značajke su specifične za regiju
   - Osigurajte da vaša Azure OpenAI distribucija modela podržava Responses API

### Put učenja

Preporučeni redoslijed kroz lekcije:
1. **00-course-setup** - Počnite ovdje za postavljanje okruženja
2. **01-intro-to-ai-agents** - Razumjeti osnove AI agenata
3. **02-explore-agentic-frameworks** - Upoznajte različite okvire
4. **03-agentic-design-patterns** - Glavni dizajnerski obrasci
5. Nastavite kroz numerirane lekcije redom

### Odabir okvira

Odaberite okvir na temelju vaših ciljeva:
- **Sve lekcije**: Microsoft Agent Framework (MAF) s `FoundryChatClient`
- **Agenti se registriraju na strani servera** u Microsoft Foundry Agent Service V2 i vidljivi su u Foundry portalu

### Dobivanje pomoći

- Pridružite se [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Pregledajte README datoteke lekcija za specifične upute
- Provjerite glavni [README.md](./README.md) za pregled tečaja
- Pogledajte [Course Setup](./00-course-setup/README.md) za detaljne upute o postavljanju

### Doprinos

Ovo je otvoreni obrazovni projekt. Dobrodošli doprinosi:
- Unaprijedite primjere koda
- Ispravite tipfelere ili greške
- Dodajte pojašnjavajuće komentare
- Predložite nove teme lekcija
- Prevedite na dodatne jezike

Pogledajte [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za trenutne potrebe.

## Kontekst specifičan za projekt

### Podrška za više jezika

Ovaj repozitorij koristi automatizirani sustav prijevoda:
- Podržano 50+ jezika
- Prijevodi u `/translations/<lang-code>/` direktorijima
- GitHub Actions tijek rada upravlja ažuriranjima prijevoda
- Izvorne datoteke su na engleskom u korijenu repozitorija

### Struktura lekcija

Svaka lekcija slijedi dosljedan obrazac:
1. Video minijatura s linkom
2. Pisani sadržaj lekcije (README.md)
3. Primjeri koda u više okvira
4. Ciljevi učenja i preduvjeti
5. Dodatni resursi za učenje povezani

### Imenovanje primjera koda

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcija 1, MAF Python
- `14-sequential.ipynb` - Lekcija 14, MAF napredni obrasci
- `16-python-agent-framework.ipynb` - Lekcija 16, proizvodni agent za korisničku podršku
- `17-local-agent-foundry-local.ipynb` - Lekcija 17, lokalni agent s Foundry Local + Qwen

### Posebni direktoriji

- `translated_images/` - Lokalizirane slike za prijevode
- `images/` - Izvorne slike za sadržaj na engleskom
- `.devcontainer/` - Konfiguracija VS Code razvojne kontejnerske okoline
- `.github/` - GitHub Actions tokovi rada i šablone

### Ovisnosti

Ključni paketi iz `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Podrška za Agent-to-Agent protokol
- `azure-ai-inference`, `azure-ai-projects` - Azure AI usluge
- `azure-identity` - Azure autentikacija (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integracija
- `mcp[cli]` - Podrška za Model Context protokol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->