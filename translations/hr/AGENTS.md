# AGENTS.md

## Pregled Projekta

Ovaj repozitorij sadrži "AI agente za početnike" - sveobuhvatan edukacijski tečaj koji podučava sve što je potrebno za izgradnju AI agenata. Tečaj se sastoji od 18 lekcija (numeriranih 00-18) koje pokrivaju osnove, dizajnerske obrasce, okvire, produkcijsko pokretanje, lokalne/uređajske agente i sigurnost AI agenata.

**Ključne Tehnologije:**
- Python 3.12+
- Jupyter bilježnice za interaktivno učenje
- AI Okviri: Microsoft Agent Framework (MAF)
- Azure AI Usluge: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitektura:**
- Struktura temeljem lekcija (direktoriji 00-15+)
- Svaka lekcija sadrži: README dokumentaciju, primjere koda (Jupyter bilježnice) i slike
- Višejezična podrška putem automatiziranog prevoditeljskog sustava
- Jedna Python bilježnica po lekciji koristeći Microsoft Agent Framework

## Komande za Postavljanje

### Preduvjeti
- Python 3.12 ili noviji
- Azure pretplata (za Microsoft Foundry)
- Azure CLI instaliran i autentificiran (`az login`)

### Početno postavljanje

1. **Klendirajte ili forkirajte repozitorij:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ILI
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Kreirajte i aktivirajte Python virtualno okruženje:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Na Windowsima: venv\Scripts\activate
   ```

3. **Instalirajte ovisnosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Postavite varijable okruženja:**
   ```bash
   cp .env.example .env
   # Uredite .env s vašim API ključevima i krajnjim točkama
   ```

### Potrebne Varijable Okruženja

Za **Microsoft Foundry** (obavezno):
- `AZURE_AI_PROJECT_ENDPOINT` - krajnja točka Microsoft Foundry projekta
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - naziv implementacije modela (npr. gpt-5-mini)

Za **Azure AI Search** (Lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - krajnja točka Azure AI Search
- `AZURE_SEARCH_API_KEY` - API ključ za Azure AI Search

Autentifikacija: Pokrenite `az login` prije pokretanja bilježnica (koristi `AzureCliCredential`).

## Radni Tijek Razvoja

### Pokretanje Jupyter Bilježnica

Svaka lekcija sadrži više Jupyter bilježnica za različite okvire:

1. **Pokrenite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigirajte do direktorija lekcije** (npr. `01-intro-to-ai-agents/code_samples/`)

3. **Otvorite i pokrenite bilježnice:**
   - `*-python-agent-framework.ipynb` - Koristeći Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Koristeći Microsoft Agent Framework (.NET)

### Rad s Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Zahtijeva Azure pretplatu
- Koristi `FoundryChatClient` za Agent Service V2 (agenti vidljivi u Foundry portalu)
- Spreman za produkciju s ugrađenom promatranjem
- Uzorak datoteke: `*-python-agent-framework.ipynb`

## Upute za Testiranje

Ovo je edukacijski repozitorij s primjerima koda, a ne produkcijski kod s automatiziranim testovima. Za provjeru postavki i promjena:

### Ručno Testiranje

1. **Testirajte Python okruženje:**
   ```bash
   python --version  # Trebalo bi biti 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testirajte izvršavanje bilježnice:**
   ```bash
   # Pretvori bilježnicu u skriptu i pokreni (testira uvoze)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Provjerite varijable okruženja:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Pokretanje Pojedinačnih Bilježnica

Otvorite bilježnice u Jupyteru i izvršavajte ćelije sekvencijalno. Svaka bilježnica je samostalna i sadrži:
- Izjave o uvozu
- Učitavanje konfiguracije
- Primjere implementacija agenata
- Očekivane izlaze u markdown ćelijama

### Smoke-testiranje Implementiranih Agenata

Za lekcije gdje je agent implementiran kao Microsoft Foundry hostirani agent (01, 04, 05, 16), repozitorij ima kataloške smoke-testove pod `tests/` koje pokreće `.github/workflows/smoke-test.yml` kroz [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) akciju. Ovo je lagani post-implementacijski test (je li agent dostupan i prati osnovne očekivanja prompta?), koji nadopunjuje evaluacijski pipeline u lekcijama 10 i 16. Pogledajte [tests/README.md](./tests/README.md) za mapiranje kataloga na lekciju i agenta. Lekcija 17 se pokreće lokalno s Foundry Local i nema hostanu krajnju točku, stoga se validira pokretanjem svoje bilježnice izravno.

## Stil Koda

### Python Konvencije

- **Python Verzija**: 3.12+
- **Stil Koda**: Pratite standardne Python PEP 8 konvencije
- **Bilježnice**: Koristite jasne markdown ćelije za objašnjenje koncepata
- **Uvozi**: Grupirajte prema standardnoj biblioteci, paketima trećih strana, lokalnim uvozima

### Jupyter Bilježničke Konvencije

- Uključite opisne markdown ćelije prije kôd ćelija
- Dodajte primjere izlaza u bilježnicama kao referencu
- Koristite jasne nazive varijabli koji odgovaraju konceptima lekcije
- Održavajte linearni redoslijed izvršavanja bilježnice (ćelija 1 → 2 → 3...)

### Organizacija Datoteka

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Izgradnja i Implementacija

### Izrada Dokumentacije

Ovaj repozitorij koristi Markdown za dokumentaciju:
- README.md datoteke u svakom direktoriju lekcije
- Glavni README.md u korijenu repozitorija
- Automatizirani sustav prevođenja putem GitHub Actions

### CI/CD Pipeline

Smešten u `.github/workflows/`:

1. **co-op-translator.yml** - Automatski prijevod na 50+ jezika
2. **welcome-issue.yml** - Dobrodošlica novim kreatorima issuea
3. **welcome-pr.yml** - Dobrodošlica novim contributorima pull requestova

### Implementacija

Ovo je edukacijski repozitorij - nema procesa implementacije. Korisnici:
1. Forikiraju ili kloniraju repozitorij
2. Pokreću bilježnice lokalno ili u GitHub Codespaces
3. Uče modifikacijom i eksperimentiranjem s primjerima

## Smjernice za Pull Request

### Prije Slanja

1. **Testirajte promjene:**
   - Potpuno pokrenite pogođene bilježnice
   - Provjerite da se sve ćelije izvršavaju bez grešaka
   - Provjerite jesu li izlazi prikladni

2. **Ažuriranja dokumentacije:**
   - Ažurirajte README.md ako dodajete nove koncepte
   - Dodajte komentare u bilježnicama za složeniji kod
   - Pazite da markdown ćelije objašnjavaju svrhu

3. **Promjene datoteka:**
   - Izbjegavajte commitanje `.env` datoteka (koristite `.env.example`)
   - Ne committajte direktorije `venv/` ili `__pycache__/`
   - Ostavite izlaze bilježnica kada ilustriraju koncepte
   - Uklonite privremene datoteke i backup bilježnice (`*-backup.ipynb`)

### Format Naslova PR-a

Koristite opisne naslove:
- `[Lesson-XX] Dodaj novi primjer za <koncept>`
- `[Fix] Ispravi tipografsku grešku u lesson-XX README`
- `[Update] Poboljša primjer koda u lesson-XX`
- `[Docs] Ažuriraj upute za postavljanje`

### Obavezne Provjere

- Bilježnice trebaju raditi bez grešaka
- README datoteke trebaju biti jasne i točne
- Slijedite postojeće obrasce koda u repozitoriju
- Održavajte dosljednost s ostalim lekcijama

## Dodatne Napomene

### Česti Problemi

1. **Nepodudaranje verzije Pythona:**
   - Osigurajte korištenje Pythona 3.12+
   - Neki paketi možda neće raditi s starijim verzijama
   - Koristite `python3 -m venv` za eksplicitno navođenje verzije Pythona

2. **Varijable okruženja:**
   - Uvijek kreirajte `.env` iz `.env.example`
   - Nemojte commitati `.env` datoteku (nalazi se u `.gitignore`)
   - Prijavite se s `az login` za autentifikaciju bez ključa Entra ID-a

3. **Sukobi paketa:**
   - Koristite čisto virtualno okruženje
   - Instalirajte iz `requirements.txt` umjesto pojedinačnih paketa
   - Neke bilježnice mogu zahtijevati dodatne pakete navedene u njihovim markdown ćelijama

4. **Azure usluge:**
   - Azure AI usluge zahtijevaju aktivnu pretplatu
   - Neke značajke su specifične za regiju
   - Osigurajte da vaša Azure OpenAI implementacija modela podržava Responses API

### Put Učenja

Preporučeni redoslijed lekcija:
1. **00-course-setup** - Počnite ovdje za postavljanje okruženja
2. **01-intro-to-ai-agents** - Razumijevanje osnova AI agenata
3. **02-explore-agentic-frameworks** - Učenje o različitim okvirima
4. **03-agentic-design-patterns** - Glavni dizajnerski obrasci
5. Nastavite redom kroz numerirane lekcije

### Izbor Okvira

Izaberite okvir prema vašim ciljevima:
- **Sve lekcije**: Microsoft Agent Framework (MAF) s `FoundryChatClient`
- **Agenti se registriraju na serverskoj strani** u Microsoft Foundry Agent Service V2 i vidljivi su u Foundry portalu

### Dobivanje Pomoći

- Pridružite se [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Pregledajte README datoteke u lekcijama za specifične smjernice
- Pogledajte glavni [README.md](./README.md) za pregled tečaja
- Pogledajte [Course Setup](./00-course-setup/README.md) za detaljne upute za postavljanje

### Doprinos

Ovo je otvoreni edukacijski projekt. Dobrodošli doprinosi:
- Poboljšajte primjere koda
- Ispravite tipografske greške ili pogreške
- Dodajte objašnjavajuće komentare
- Predložite nove teme lekcija
- Prevedite na dodatne jezike

Pogledajte [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za trenutne potrebe.

## Kontekst Specifičan za Projekt

### Višejezična Podrška

Ovaj repozitorij koristi automatizirani sustav prevođenja:
- Podržano 50+ jezika
- Prijevodi u direktorijima `/translations/<lang-code>/`
- GitHub Actions workflow upravlja ažuriranjima prijevoda
- Izvorne datoteke na engleskom u korijenu repozitorija

### Struktura Lekcije

Svaka lekcija slijedi dosljedan obrazac:
1. Sličica videa s linkom
2. Pisani sadržaj lekcije (README.md)
3. Primjeri koda u više okvira
4. Ciljevi učenja i preduvjeti
5. Poveznice na dodatne izvore učenja

### Imenovanje Primjera Koda

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcija 1, MAF Python
- `14-sequential.ipynb` - Lekcija 14, MAF napredni obrasci
- `16-python-agent-framework.ipynb` - Lekcija 16, produkcijski agent korisničke podrške
- `17-local-agent-foundry-local.ipynb` - Lekcija 17, lokalni agent s Foundry Local + Qwen

### Posebni Direktoriji

- `translated_images/` - Lokalizirane slike za prijevode
- `images/` - Izvorne slike za sadržaj na engleskom
- `.devcontainer/` - Konfiguracija razvojnih kontejnera za VS Code
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
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->