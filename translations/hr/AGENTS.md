# AGENTS.md

## Pregled Projekta

Ovaj repozitorij sadrži "AI Agente za Početnike" - sveobuhvatan obrazovni tečaj koji podučava sve što je potrebno za izgradnju AI Agenata. Tečaj se sastoji od 18 lekcija (numeriranih od 00 do 18) koje pokrivaju osnove, dizajnerske uzorke, okvire, produkcijsko postavljanje, lokalne/agente na uređaju i sigurnost AI agenata.

**Ključne Tehnologije:**
- Python 3.12+
- Jupyter bilježnice za interaktivno učenje
- AI Okviri: Microsoft Agent Framework (MAF)
- Azure AI Usluge: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitektura:**
- Struktura temeljena na lekcijama (direktoriji 00-15+)
- Svaka lekcija sadrži: README dokumentaciju, primjere koda (Jupyter bilježnice) i slike
- Podrška za više jezika putem automatiziranog sustava prevođenja
- Jedna Python bilježnica po lekciji koristeći Microsoft Agent Framework

## Komande za Podešavanje

### Preduvjeti
- Python 3.12 ili noviji
- Azure pretplata (za Microsoft Foundry)
- Instaliran i autentificiran Azure CLI (`az login`)

### Početno Podešavanje

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

Za **Microsoft Foundry** (Obavezno):
- `AZURE_AI_PROJECT_ENDPOINT` - krajnja točka projekta u Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - naziv implementacije modela (npr. gpt-4.1-mini)

Za **Azure AI Search** (Lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - krajnja točka Azure AI Search-a
- `AZURE_SEARCH_API_KEY` - API ključ za Azure AI Search

Autentikacija: Pokrenite `az login` prije pokretanja bilježnica (koristi `AzureCliCredential`).

## Radni Tijek Razvoja

### Pokretanje Jupyter Bilježnica

Svaka lekcija sadrži više Jupyter bilježnica za različite okvire:

1. **Pokrenite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigirajte do direktorija lekcije** (npr. `01-intro-to-ai-agents/code_samples/`)

3. **Otvorite i pokrenite bilježnice:**
   - `*-python-agent-framework.ipynb` - koristeći Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - koristeći Microsoft Agent Framework (.NET)

### Rad sa Microsoft Agent Framework-om

**Microsoft Agent Framework + Microsoft Foundry:**
- Zahtijeva Azure pretplatu
- Koristi `FoundryChatClient` za Agent Service V2 (agenti vidljivi u Foundry portalu)
- Spreman za produkciju s ugrađenom vidljivošću
- Obrasci datoteka: `*-python-agent-framework.ipynb`

## Upute za Testiranje

Ovo je obrazovni repozitorij s primjerima koda, a ne produkcijski kod s automatiziranim testovima. Za provjeru vašeg okruženja i promjena:

### Ručno Testiranje

1. **Testirajte Python okruženje:**
   ```bash
   python --version  # Trebalo bi biti 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testirajte izvršavanje bilježnica:**
   ```bash
   # Pretvori bilježnicu u skriptu i pokreni (testira uvoze)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Provjerite varijable okruženja:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Pokretanje Pojedinačnih Bilježnica

Otvorite bilježnice u Jupyteru i izvršavajte ćelije redom. Svaka bilježnica je samostalna i uključuje:
- Izjave za import
- Učitavanje konfiguracije
- Primjere implementacija agenata
- Očekivane izlaze u markdown ćelijama

### Osnovno Testiranje Implementiranih Agenata

Za lekcije gdje je agent implementiran kao Microsoft Foundry hostirani agent (01, 04, 05, 16), repozitorij isporučuje smoke-test katalozi u `tests/` koji se pokreću putem `.github/workflows/smoke-test.yml` tijeka rada koristeći akciju [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Ovo je lagani post-implementacijski gateway (je li agent dostupan i slijedi osnovna očekivanja prompta?), što dopunjuje evaluacijski tijek u lekcijama 10 i 16. Pogledajte [tests/README.md](./tests/README.md) za mapiranje kataloga-lekcija-agenta. Lekcija 17 se pokreće lokalno s Foundry Local i nema hostiranu krajnju točku, pa se provjerava pokretanjem njenog bilježničkog sadržaja direktno.

## Stil Koda

### Python Konvencije

- **Python Verzija**: 3.12+
- **Stil Koda**: Slijediti standardne Python PEP 8 konvencije
- **Bilježnice**: Koristiti jasne markdown ćelije za objašnjenje koncepata
- **Importi**: Grupirati po standardnoj biblioteci, trećim stranama i lokalnim importima

### Jupyter Bilježnica Konvencije

- Uključiti opisne markdown ćelije prije ćelija koda
- Dodati primjere izlaza u bilježnicama za referencu
- Koristiti jasne nazive varijabli koje odgovaraju konceptima lekcije
- Održavati linearni redoslijed izvršavanja bilježnice (ćelija 1 → 2 → 3...)

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

### Izgradnja Dokumentacije

Ovaj repozitorij koristi Markdown za dokumentaciju:
- README.md datoteke u svakom direktoriju lekcije
- Glavni README.md u korijenu repozitorija
- Automatizirani sustav prevođenja putem GitHub akcija

### CI/CD Pipeline

Smješten je u `.github/workflows/`:

1. **co-op-translator.yml** - Automatski prijevod na više od 50 jezika
2. **welcome-issue.yml** - Dobrodošlica novim kreatorima issue-a
3. **welcome-pr.yml** - Dobrodošlica novim suradnicima s pull requestovima

### Implementacija

Ovo je edukativni repozitorij - nema procesa implementacije. Korisnici:
1. Forkaju ili kloniraju repozitorij
2. Pokreću bilježnice lokalno ili u GitHub Codespaces
3. Uče mijenjajući i eksperimentirajući s primjerima

## Smjernice za Pull Requestove

### Prije Slanja

1. **Testirajte svoje promjene:**
   - Potpuno pokrenite pogođene bilježnice
   - Provjerite da se sve ćelije izvršavaju bez grešaka
   - Provjerite jesu li izlazi odgovarajući

2. **Ažuriranja dokumentacije:**
   - Ažurirajte README.md ako dodajete nove koncepte
   - Dodajte komentare u bilježnice za složeniji kod
   - Osigurajte da markdown ćelije objašnjavaju svrhu

3. **Promjene datoteka:**
   - Izbjegavajte dodavanje `.env` datoteka (koristite `.env.example`)
   - Ne dodavajte `venv/` ili `__pycache__/` direktorije
   - Zadržite izlaze bilježnica kad demonstriraju koncepte
   - Uklonite privremene datoteke i backup bilježnice (`*-backup.ipynb`)

### Format Naslova PR-a

Koristite opisne naslove:
- `[Lesson-XX] Dodaj novi primjer za <concept>`
- `[Fix] Ispravi tipfelere u lesson-XX README`
- `[Update] Poboljšaj primjer koda u lesson-XX`
- `[Docs] Ažuriraj upute za postavljanje`

### Potrebne Provjere

- Bilježnice se trebaju izvršavati bez grešaka
- README datoteke trebaju biti jasne i točne
- Slijedite postojeće obrasce koda u repozitoriju
- Održavajte dosljednost s drugim lekcijama

## Dodatne Napomene

### Uobičajene Zamke

1. **Neusklađenost verzije Pythona:**
   - Koristite Python 3.12+ 
   - Neki paketi možda neće raditi sa starijim verzijama
   - Koristite `python3 -m venv` za eksplicitno određivanje verzije Pythona

2. **Varijable okruženja:**
   - Uvijek napravite `.env` iz `.env.example`
   - Ne dodavajte `.env` datoteku u repozitorij (nalazi se u `.gitignore`)
   - Prijavite se s `az login` za autentikaciju bez ključeva putem Entra ID-a

3. **Sukobi paketa:**
   - Koristite svježe virtualno okruženje
   - Instalirajte iz `requirements.txt` umjesto pojedinačnih paketa
   - Neke bilježnice mogu zahtijevati dodatne pakete navedene u njihovim markdown ćelijama

4. **Azure usluge:**
   - Azure AI usluge zahtijevaju aktivnu pretplatu
   - Neke funkcije su specifične za regiju
   - Osigurajte da vaša Azure OpenAI implementacija modela podržava Responses API

### Put Učenja

Preporučeni napredak kroz lekcije:
1. **00-course-setup** - Počnite ovdje za postavljanje okruženja
2. **01-intro-to-ai-agents** - Razumite osnove AI agenata
3. **02-explore-agentic-frameworks** - Naučite o različitim okvirima
4. **03-agentic-design-patterns** - Osnovni dizajnerski uzorci
5. Nastavite kroz numerirane lekcije sekvencijalno

### Izbor Okvira

Izaberite okvir prema svojim ciljevima:
- **Sve lekcije**: Microsoft Agent Framework (MAF) s `FoundryChatClient`
- **Agenti se registriraju na serverskoj strani** u Microsoft Foundry Agent Service V2 i vidljivi su u Foundry portalu

### Dobivanje Pomoći

- Pridružite se [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Pregledajte README datoteke lekcija za specifične upute
- Provjerite glavni [README.md](./README.md) za pregled tečaja
- Pogledajte [Course Setup](./00-course-setup/README.md) za detaljne upute za postavljanje

### Doprinos

Ovo je otvoreni edukativni projekt. Dobrodošli doprinosi:
- Poboljšajte primjere koda
- Ispravite tipfelere ili greške
- Dodajte pojašnjavajuće komentare
- Predložite nove teme lekcija
- Prevedite na dodatne jezike

Pogledajte [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za trenutne potrebe.

## Kontekst Specifičan za Projekt

### Podrška za Više Jezika

Ovaj repozitorij koristi automatizirani sustav prevođenja:
- Podržano više od 50 jezika
- Prijevodi u direktorijima `/translations/<lang-code>/`
- GitHub Actions tijek rada upravlja ažuriranjima prijevoda
- Izvorne datoteke su na engleskom na korijenu repozitorija

### Struktura Lekcija

Svaka lekcija slijedi dosljedan obrazac:
1. Video minijatura s linkom
2. Pisani sadržaj lekcije (README.md)
3. Primjeri koda u više okvira
4. Ciljevi učenja i preduvjeti
5. Dodatni resursi za učenje povezani

### Imenovanje Primjera Koda

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcija 1, MAF Python
- `14-sequential.ipynb` - Lekcija 14, MAF napredni uzorci
- `16-python-agent-framework.ipynb` - Lekcija 16, produkcijski agent za korisničku podršku
- `17-local-agent-foundry-local.ipynb` - Lekcija 17, lokalni agent s Foundry Local + Qwen

### Posebni Direktoriji

- `translated_images/` - Lokalizirane slike za prijevode
- `images/` - Izvorne slike za sadržaj na engleskom
- `.devcontainer/` - Konfiguracija razvojne kontejnere za VS Code
- `.github/` - GitHub Actions tijekovi rada i predlošci

### Ovisnosti

Ključni paketi iz `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Podrška za Agent-to-Agent protokol
- `azure-ai-inference`, `azure-ai-projects` - Azure AI usluge
- `azure-identity` - Azure autentikacija (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integracija
- `mcp[cli]` - Podrška za Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->