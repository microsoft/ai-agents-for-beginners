# AGENTS.md

## Pregled projekta

Ta repozitorij vsebuje "AI agente za začetnike" – celovit izobraževalni tečaj, ki uči vse, kar je potrebno za izdelavo AI agentov. Tečaj obsega več kot 15 lekcij, ki pokrivajo osnove, oblikovne vzorce, ogrodja in uvajanje AI agentov v produkcijo.

**Ključne tehnologije:**
- Python 3.12+
- Jupyter Notebooki za interaktivno učenje
- AI ogrodja: Microsoft Agent Framework (MAF)
- Azure AI storitve: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arhitektura:**
- Struktura na osnovi lekcij (imeniki 00-15+)
- Vsaka lekcija vsebuje: dokumentacijo README, vzorce kode (Jupyter notebooke) in slike
- Podpora več jezikom preko avtomatiziranega sistema prevajanja
- Ena Python beležnica na lekcijo z uporabo Microsoft Agent Framework

## Ukazi za nastavitev

### Predpogoji
- Python 3.12 ali novejši
- Azure naročnina (za Azure AI Foundry)
- Azure CLI nameščen in prijavljen (`az login`)

### Začetna nastavitev

1. **Klonirajte ali forknite repozitorij:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ALI
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Ustvarite in aktivirajte Python virtualno okolje:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Na Windows: venv\Scripts\activate
   ```

3. **Namestite odvisnosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nastavite okoljske spremenljivke:**
   ```bash
   cp .env.example .env
   # Uredite .env z vašimi API ključi in končnimi točkami
   ```

### Potrebne okoljske spremenljivke

Za **Azure AI Foundry** (zahtevano):
- `AZURE_AI_PROJECT_ENDPOINT` - končna točka projekta Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ime namestitve modela (npr. gpt-4o)

Za **Azure AI Search** (lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - končna točka Azure AI Search
- `AZURE_SEARCH_API_KEY` - API ključ za Azure AI Search

Avtentikacija: Pred zagonom notebookov izvedite `az login` (uporablja `AzureCliCredential`).

## Razvojni potek dela

### Zagon Jupyter notebookov

Vsaka lekcija vsebuje več Jupyter notebookov za različna ogrodja:

1. **Zaženite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Pojdite v imenik lekcije** (npr. `01-intro-to-ai-agents/code_samples/`)

3. **Odprite in zaženite notebooke:**
   - `*-python-agent-framework.ipynb` - uporaba Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - uporaba Microsoft Agent Framework (.NET)

### Delo z Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Zahteva Azure naročnino
- Uporablja `AzureAIProjectAgentProvider` za Agent Service V2 (agenti vidni v portalu Foundry)
- Pripravljen za produkcijo z vgrajeno opaznostjo
- Vzorec datoteke: `*-python-agent-framework.ipynb`

## Navodila za testiranje

To je izobraževalni repozitorij z zgolj primeri kode, ne produkcijska koda z avtomatiziranimi testi. Za preverjanje nastavitve in sprememb:

### Ročno testiranje

1. **Testirajte Python okolje:**
   ```bash
   python --version  # Mora biti 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testirajte zagon notebooka:**
   ```bash
   # Pretvori zvezek v skripto in zaženi (preizkusi uvoze)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Preverite okoljske spremenljivke:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Zagon posameznih notebookov

Odprite notebooke v Jupyterju in izvedite celice zaporedno. Vsak notebook je samostojen in vsebuje:
- uvozne izjave
- nalaganje konfiguracije
- primere implementacij agentov
- pričakovane izhode v markdown celicah

## Stil kode

### Python konvencije

- **Python različica**: 3.12+
- **Stil kode**: Sledite standardnim Python PEP 8 konvencijam
- **Notebooki**: Uporabite jasne markdown celice za razlage pojmov
- **Uvozi**: Združite po standardni knjižnici, tretjih straneh, lokalnih uvozih

### Jupyter Notebook konvencije

- Vključite opisne markdown celice pred celicami s kodo
- Dodajte primere izhodov v notebookih za referenco
- Uporabljajte jasna imena spremenljivk, ki ustrezajo konceptom lekcij
- Izvajanje notebooka naj bo linearno (celica 1 → 2 → 3...)

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

## Gradnja in uvajanje

### Gradnja dokumentacije

Ta repozitorij uporablja Markdown za dokumentacijo:
- README.md datoteke v vsaki mapi lekcije
- Glavna README.md v korenu repozitorija
- Avtomatizirani sistem prevajanja preko GitHub Actions

### CI/CD cevovod

Nahaja se v `.github/workflows/`:

1. **co-op-translator.yml** - Samodejno prevajanje v 50+ jezikov
2. **welcome-issue.yml** - Pozdrav novim ustvarjalcem issuev
3. **welcome-pr.yml** - Pozdrav novim prispevkom (pull requestom)

### Uvajanje

To je izobraževalni repozitorij – ni postopka uvajanja. Uporabniki:
1. Fornkajo ali klonirajo repozitorij
2. Zaženejo notebooke lokalno ali v GitHub Codespaces
3. Se učijo z modificiranjem in eksperimentiranjem z primeri

## Smernice za pull requeste

### Pred oddajo

1. **Preizkusite spremembe:**
   - Zaženite popolnoma vse prizadete notebooke
   - Preverite, da se vse celice izvedejo brez napak
   - Preverite, da so izhodi ustrezni

2. **Posodobitev dokumentacije:**
   - Posodobite README.md, če dodajate nove pojme
   - Dodajte komentarje v notebookih za zapleteno kodo
   - Poskrbite, da markdown celice razlagajo namen

3. **Spremembe datotek:**
   - Izogibajte se commitanju `.env` datotek (uporabite `.env.example`)
   - Ne commitajte `venv/` ali `__pycache__/` imenikov
   - Ohranjajte izhode notebookov, ko demonstrirajo koncepte
   - Odstranite začasne datoteke in varnostne kopije notebookov (`*-backup.ipynb`)

### Oblika naslova PR

Uporabljajte opisne naslove:
- `[Lesson-XX] Dodaj nov primer za <koncept>`
- `[Fix] Popravi tipkarsko napako v lesson-XX README`
- `[Update] Izboljšaj vzorec kode v lesson-XX`
- `[Docs] Posodobitev navodil za nastavitev`

### Potrebni pregledi

- Notebooki se morajo izvesti brez napak
- README datoteke morajo biti jasne in natančne
- Sledite obstoječim vzorcem kode v repozitoriju
- Ohranite skladnost z ostalimi lekcijami

## Dodatne opombe

### Pogoste težave

1. **Neujemanje verzije Pythona:**
   - Poskrbite, da uporabljate Python 3.12+
   - Nekateri paketi ne delujejo z starejšimi različicami
   - Za specifično verzijo uporabite `python3 -m venv`

2. **Okoljske spremenljivke:**
   - Vedno ustvarite `.env` iz `.env.example`
   - Ne commitajte `.env` datoteke (je v `.gitignore`)
   - GitHub token potrebuje ustrezna dovoljenja

3. **Konflikti paketov:**
   - Uporabite sveže virtualno okolje
   - Namestite iz `requirements.txt` namesto posameznih paketov
   - Nekateri notebooki zahtevajo dodatne pakete, navedene v njihovih markdown celicah

4. **Azure storitve:**
   - Azure AI storitve zahtevajo aktivno naročnino
   - Nekatere funkcije so specifične za regijo
   - Brezplačni nivo velja za GitHub modele

### Pot učenja

Priporočeno zaporedje lekcij:
1. **00-course-setup** - Začnite tukaj z nastavitvijo okolja
2. **01-intro-to-ai-agents** - Spoznajte osnove AI agentov
3. **02-explore-agentic-frameworks** - Spoznajte različna ogrodja
4. **03-agentic-design-patterns** - Glavni oblikovni vzorci
5. Nadaljujte zaporedoma skozi lekcije

### Izbira ogrodja

Izberite glede na cilje:
- **Vse lekcije**: Microsoft Agent Framework (MAF) z `AzureAIProjectAgentProvider`
- **Agenti se registrirajo na strežniški strani** v Azure AI Foundry Agent Service V2 in so vidni v Foundry portalu

### Pomoč

- Pridružite se [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Preglejte README datoteke lekcij za specifična navodila
- Oglejte si glavni [README.md](./README.md) za pregled tečaja
- Za podrobna navodila glejte [Course Setup](./00-course-setup/README.md)

### Prispevanje

To je odprt izobraževalni projekt. Prispevki so dobrodošli:
- Izboljšajte primere kode
- Popravite tipke ali napake
- Dodajte pojasnilne komentarje
- Predlagajte nove teme lekcij
- Prevedite v dodatne jezike

Poglejte [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za trenutne potrebe.

## Kontekst specifičen za projekt

### Podpora več jezikom

Ta repozitorij uporablja avtomatiziran sistem prevajanja:
- Podpora za več kot 50 jezikov
- Prevajanja v imenikih `/translations/<lang-code>/`
- GitHub Actions skripta samodejno posodablja prevode
- Izvorne datoteke so v angleščini v korenu repozitorija

### Struktura lekcij

Vsaka lekcija sledi doslednemu vzorcu:
1. Sličica videa s povezavo
2. Pisna vsebina lekcije (README.md)
3. Vzorce kode v več ogrodjih
4. Cilje učenja in predpogoje
5. Dodatne učne vire s povezavami

### Imenovanje vzorcev kode

Oblika: `<številka-lekcije>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - lekcija 1, MAF Python
- `14-sequential.ipynb` - lekcija 14, napredni MAF vzorci

### Posebni imeniki

- `translated_images/` - lokalizirane slike za prevode
- `images/` - izvorne slike za angleško vsebino
- `.devcontainer/` - konfiguracija razvojnega kontejnerja VS Code
- `.github/` - GitHub Actions delovni tokovi in predloge

### Odvisnosti

Ključni paketi iz `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - podpora za protokol agent-to-agent
- `azure-ai-inference`, `azure-ai-projects` - Azure AI storitve
- `azure-identity` - Azure avtentikacija (AzureCliCredential)
- `azure-search-documents` - integracija Azure AI Search
- `mcp[cli]` - podpora Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->