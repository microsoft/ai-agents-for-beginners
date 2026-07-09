# AGENTS.md

## Pregled Projekta

Ovaj repozitorij sadrži "AI agente za početnike" - sveobuhvatan obrazovni tečaj koji podučava sve što je potrebno za izradu AI agenata. Tečaj se sastoji od 18 lekcija koje pokrivaju osnove, obrasce dizajna, okvire i produkcijsko implementiranje AI agenata.

**Ključne Tehnologije:**
- Python 3.12+
- Jupyter bilježnice za interaktivno učenje
- AI Okviri: Microsoft Agent Framework (MAF)
- Azure AI Usluge: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitektura:**
- Struktura bazirana na lekcijama (direktoriji 00-15+)
- Svaka lekcija sadrži: README dokumentaciju, primjere koda (Jupyter bilježnice) i slike
- Podrška za više jezika putem automatiziranog sustava prevođenja
- Jedna Python bilježnica po lekciji koristeći Microsoft Agent Framework

## Komande za Postavljanje

### Preduvjeti
- Python 3.12 ili noviji
- Azure pretplata (za Microsoft Foundry)
- Instaliran i autentificiran Azure CLI (`az login`)

### Početno Postavljanje

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
   # Uredite .env sa svojim API ključevima i krajnjim točkama
   ```

### Potrebne Varijable Okruženja

Za **Microsoft Foundry** (obavezno):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry krajnja točka projekta
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Ime implementacije modela (npr. gpt-4o)

Za **Azure AI Search** (Lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Krajnja točka Azure AI Search
- `AZURE_SEARCH_API_KEY` - API ključ za Azure AI Search

Autentifikacija: Pokrenite `az login` prije pokretanja bilježnica (koristi `AzureCliCredential`).

## Razvojni Radni Tok

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
- Koristi `FoundryChatClient` za Agent Service V2 (agenti vidljivi na Foundry portalu)
- Spreman za produkciju s ugrađenom promatranjem
- Uzorak datoteke: `*-python-agent-framework.ipynb`

## Upute za Testiranje

Ovo je obrazovni repozitorij s primjerima koda, a ne produkcijski kod s automatiziranim testovima. Za provjeru vaše postavke i promjena:

### Ručno Testiranje

1. **Testirajte Python okruženje:**
   ```bash
   python --version  # Trebalo bi biti 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testirajte izvođenje bilježnice:**
   ```bash
   # Pretvori bilježnicu u skriptu i pokreni (testira importe)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Provjerite varijable okruženja:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Pokretanje Pojedinačnih Bilježnica

Otvorite bilježnice u Jupyteru i izvršavajte ćelije sekvencijalno. Svaka bilježnica je samostalna i uključuje:
- Izjave o importu
- Učitavanje konfiguracije
- Primjere implementacija agenata
- Očekivane izlaze u markdown ćelijama

## Stil Koda

### Python Konvencije

- **Python Verzija**: 3.12+
- **Stil Koda**: Slijedite standardne Python PEP 8 konvencije
- **Bilježnice**: Koristite jasne markdown ćelije za objašnjenje koncepata
- **Importi**: Grupirajte po standardnoj biblioteci, vanjskim paketima, lokalnim importima

### Jupyter Bilježničke Konvencije

- Uključite opisne markdown ćelije prije kodnih ćelija
- Dodajte primjere izlaza u bilježnice kao referencu
- Koristite jasne nazive varijabli koji odgovaraju konceptima lekcije
- Održavajte linearni redoslijed izvršavanja bilježnica (ćelija 1 → 2 → 3...)

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

### CI/CD Cjevovod

Nalazi se u `.github/workflows/`:

1. **co-op-translator.yml** - Automatski prijevod na 50+ jezika
2. **welcome-issue.yml** - Dobrodošlica novim kreatorima problema
3. **welcome-pr.yml** - Dobrodošlica novim suradnicima pull requestova

### Implementacija

Ovo je obrazovni repozitorij - nema procesa implementacije. Korisnici:
1. Forkaju ili kloniraju repozitorij
2. Pokreću bilježnice lokalno ili u GitHub Codespaces
3. Uče modificirajući i eksperimentirajući s primjerima

## Smjernice za Pull Requestove

### Prije Slanja

1. **Testirajte svoje promjene:**
   - Potpuno pokrenite pogođene bilježnice
   - Provjerite da sve ćelije izvršavaju bez pogrešaka
   - Provjerite jesu li izlazi prikladni

2. **Ažuriranja dokumentacije:**
   - Ažurirajte README.md ako dodajete nove koncepte
   - Dodajte komentare u bilježnice za složeniji kod
   - Osigurajte da markdown ćelije objašnjavaju svrhu

3. **Promjene datoteka:**
   - Izbjegavajte committanje `.env` datoteka (koristite `.env.example`)
   - Nemojte commitati direktorije `venv/` ili `__pycache__/`
   - Zadržite izlaze bilježnica kada demonstriraju koncepte
   - Uklonite privremene datoteke i backup bilježnice (`*-backup.ipynb`)

### Format Naslova PR-a

Koristite opisne naslove:
- `[Lesson-XX] Dodaj novi primjer za <concept>`
- `[Fix] Ispravi tipfeler u README lekcije-XX`
- `[Update] Poboljšaj primjer koda u lekciji-XX`
- `[Docs] Ažuriraj upute za postavljanje`

### Potrebne Provjere

- Bilježnice trebaju izvršavati bez pogrešaka
- README datoteke trebaju biti jasne i točne
- Slijediti postojeće obrasce koda u repozitoriju
- Održavati konzistentnost s ostalim lekcijama

## Dodatne Napomene

### Česte Zamke

1. **Neusklađenost verzije Pythona:**
   - Osigurajte da koristite Python 3.12+
   - Neki paketi možda ne rade s starijim verzijama
   - Koristite `python3 -m venv` za eksplicitno određivanje verzije Pythona

2. **Varijable okruženja:**
   - Uvijek kreirajte `.env` iz `.env.example`
   - Nemojte commitati `.env` datoteku (nalazi se u `.gitignore`)
   - Prijavite se s `az login` za autentifikaciju Entra ID bez ključa

3. **Sukobi paketa:**
   - Koristite novo virtualno okruženje
   - Instalirajte iz `requirements.txt`, a ne pojedinačne pakete
   - Neke bilježnice mogu zahtijevati dodatne pakete navedene u njihovim markdown ćelijama

4. **Azure usluge:**
   - Azure AI usluge zahtijevaju aktivnu pretplatu
   - Neke značajke su specifične za regiju
   - Osigurajte da vaša Azure OpenAI implementacija modela podržava Responses API

### Put Učenja

Preporučen tijek kroz lekcije:
1. **00-course-setup** - Počnite ovdje za postavljanje okruženja
2. **01-intro-to-ai-agents** - Razumijevanje osnova AI agenata
3. **02-explore-agentic-frameworks** - Učenje o različitim okvirima
4. **03-agentic-design-patterns** - Temeljni obrasci dizajna
5. Nastavite kroz numerirane lekcije redom

### Izbor Okvira

Odaberite okvir prema svojim ciljevima:
- **Sve lekcije**: Microsoft Agent Framework (MAF) s `FoundryChatClient`
- **Agenti se registriraju na serverskoj strani** u Microsoft Foundry Agent Service V2 i vidljivi su na Foundry portalu

### Dobivanje Pomoći

- Pridružite se [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Pregledajte README datoteke lekcija za specifične upute
- Pogledajte glavni [README.md](./README.md) za pregled tečaja
- Pogledajte [Course Setup](./00-course-setup/README.md) za detaljne upute za postavljanje

### Doprinos

Ovo je otvoreni obrazovni projekt. Dobrodošli su doprinosi:
- Poboljšajte primjere koda
- Ispravite tipfelere ili greške
- Dodajte pojašnjavajuće komentare
- Predložite nove teme lekcija
- Prevedite na dodatne jezike

Pogledajte [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za aktualne potrebe.

## Kontekst Specifičan za Projekt

### Podrška za Više Jezika

Ovaj repozitorij koristi automatizirani sustav prevođenja:
- Podržano 50+ jezika
- Prijevodi u direktorijima `/translations/<lang-code>/`
- GitHub Actions workflow upravlja ažuriranjem prijevoda
- Izvorne datoteke su na engleskom u korijenu repozitorija

### Struktura Lekcija

Svaka lekcija slijedi dosljedan obrazac:
1. Sličica videa s linkom
2. Tekstualni sadržaj lekcije (README.md)
3. Primjeri koda u više okvira
4. Ciljevi učenja i preduvjeti
5. Povezani dodatni resursi za učenje

### Imenovanje Primjera Koda

Format: `<broj-lekcije>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcija 1, MAF Python
- `14-sequential.ipynb` - Lekcija 14, napredni MAF obrasci

### Posebni Direktoriji

- `translated_images/` - Lokalizirane slike za prijevode
- `images/` - Originalne slike za sadržaj na engleskom
- `.devcontainer/` - Konfiguracija razvojnih kontejnera za VS Code
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