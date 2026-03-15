# AGENTS.md

## Pregled projekta

Ta repozitorij vsebuje "AI Agente za začetnike" - celovit izobraževalni tečaj, ki poučuje vse, kar je potrebno za izdelavo AI agentov. Tečaj vsebuje več kot 15 lekcij, ki zajemajo osnove, vzorce načrtovanja, ogrodja in produkcijsko nameščanje AI agentov.

**Ključne tehnologije:**
- Python 3.12+
- Jupyter zapiski za interaktivno učenje
- AI ogrodja: Microsoft Agent Framework (MAF)
- Azure AI storitve: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arhitektura:**
- Struktura na osnovi lekcij (imeniki 00-15+)
- Vsaka lekcija vsebuje: README dokumentacijo, vzorce kode (Jupyter zvezke) in slike
- Večjezikovna podpora prek avtomatiziranega sistema prevajanja
- Ena Python zvezka na lekcijo, ki uporablja Microsoft Agent Framework

## Ukazi za namestitev

### Zahteve
- Python 3.12 ali novejši
- Azure naročnina (za Azure AI Foundry)
- Azure CLI nameščen in prijavljen (`az login`)

### Začetna namestitev

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

Za **Azure AI Foundry** (obvezno):
- `AZURE_AI_PROJECT_ENDPOINT` - končna točka projekta Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ime uvajanja modela (npr. gpt-4o)

Za **Azure AI Search** (Lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - končna točka Azure AI Search
- `AZURE_SEARCH_API_KEY` - ključ API za Azure AI Search

Avtentikacija: Zaženite `az login` pred zagonom zvezkov (uporablja `AzureCliCredential`).

## Razvojni potek dela

### Zagon Jupyter zvezkov

Vsaka lekcija vsebuje več Jupyter zvezkov za različna ogrodja:

1. **Zaženite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Pojdite v imenik lekcije** (npr. `01-intro-to-ai-agents/code_samples/`)

3. **Odprite in zaženite zvezke:**
   - `*-python-agent-framework.ipynb` - uporaba Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - uporaba Microsoft Agent Framework (.NET)

### Delo z Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Zahteva Azure naročnino
- Uporablja `AzureAIProjectAgentProvider` za Agent Service V2 (agenti vidni v Foundry portalu)
- Pripravljen za produkcijo z vgrajeno opaznostjo
- Vzorec imen datotek: `*-python-agent-framework.ipynb`

## Navodila za testiranje

To je izobraževalni repozitorij z vzorčno kodo, ne produkcijska koda z avtomatiziranimi testi. Za preverjanje nastavitve in sprememb:

### Ročno testiranje

1. **Testirajte Python okolje:**
   ```bash
   python --version  # Mora biti 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testirajte zagon zvezkov:**
   ```bash
   # Pretvori zvezek v skripto in zaženi (preizkusi uvoze)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Preverite okoljske spremenljivke:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Zagon posameznih zvezkov

Odprite zvezke v Jupyterju in izvršite celice zaporedoma. Vsak zvezek je samostojen ter vsebuje:
- Ukaze za uvoz
- Naložitev konfiguracije
- Primeri implementacije agentov
- Pričakovani izhod v markdown celicah

## Slog kode

### Python konvencije

- **Python različica**: 3.12+
- **Slog kode**: Sledite standardnim Python PEP 8 konvencijam
- **Zvezki**: Uporabljajte jasne markdown celice za razlago pojmov
- **Uvozi**: Združite standardno knjižnico, tretje osebe in lokalne uvoze

### Konvencije za Jupyter zvezke

- Vključite opisne markdown celice pred kodnimi celicami
- Dodajte primere izhoda v zvezkih za referenco
- Uporabljajte jasna imena spremenljivk, ki ustrezajo konceptom lekcije
- Ohranite linearni vrstni red izvrševanja zvezka (celica 1 → 2 → 3...)

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

## Gradnja in nameščanje

### Gradnja dokumentacije

Ta repozitorij uporablja Markdown za dokumentacijo:
- README.md datoteke v vsakem imeniku lekcije
- Glavni README.md v korenu repozitorija
- Avtomatiziran sistem prevajanja preko GitHub Actions

### CI/CD cevovod

Nahaja se v `.github/workflows/`:

1. **co-op-translator.yml** - Samodejno prevajanje v več kot 50 jezikov
2. **welcome-issue.yml** - Pozdravlja nove ustvarjalce težav
3. **welcome-pr.yml** - Pozdravlja nove sodelujoče pri pull zahtevah

### Nameščanje

To je izobraževalni repozitorij - brez postopka nameščanja. Uporabniki:
1. Forlkajo ali klonirajo repozitorij
2. Zaženejo zvezke lokalno ali v GitHub Codespaces
3. Se učijo z modificiranjem in eksperimentiranjem z vzorci

## Smernice za pull zahteve

### Pred oddajo

1. **Testirajte svoje spremembe:**
   - Celovito zaženite prizadete zvezke
   - Preverite, da se vse celice izvršijo brez napak
   - Preverite, ali so izhodi ustrezni

2. **Posodobitve dokumentacije:**
   - Posodobite README.md, če dodajate nove koncepte
   - Dodajte komentarje v zvezke za kompleksno kodo
   - Prepričajte se, da markdown celice pojasnjujejo namen

3. **Spremembe datotek:**
   - Ne dodajajte `.env` datotek (uporabite `.env.example`)
   - Ne vlagajte imenikov `venv/` ali `__pycache__/`
   - Ohranite izhode zvezkov, če prikazujejo koncepte
   - Odstranite začasne datoteke in varnostne kopije zvezkov (`*-backup.ipynb`)

### Format naslova PR

Uporabljajte opisne naslove:
- `[Lesson-XX] Dodaj nov primer za <koncept>`
- `[Fix] Popravi napako v lesson-XX README`
- `[Update] Izboljšaj vzorec kode v lesson-XX`
- `[Docs] Posodobi namestitvena navodila`

### Potrebne kontrole

- Zvezki se morajo izvršiti brez napak
- README datoteke morajo biti jasne in natančne
- Sledite obstoječim vzorcem kode v repozitoriju
- Ohranjajte skladnost z ostalimi lekcijami

## Dodatne opombe

### Pogoste težave

1. **Neujemanje verzije Python:**
   - Prepričajte se, da uporabljate Python 3.12+
   - Nekateri paketi ne delujejo z starejšimi verzijami
   - Za eksplicitno določitev verzije uporabite `python3 -m venv`

2. **Okoljske spremenljivke:**
   - Vedno ustvarite `.env` iz `.env.example`
   - Ne vlagajte `.env` datoteke (je v `.gitignore`)
   - GitHub token zahteva ustrezna dovoljenja

3. **Konflikti paketov:**
   - Uporabite novo virtualno okolje
   - Namestite pakete iz `requirements.txt`, ne posameznih
   - Nekateri zvezki potrebujejo dodatne pakete, omenjene v markdown celicah

4. **Azure storitve:**
   - Za Azure AI storitve je potrebna aktivna naročnina
   - Nekatere funkcije so omejene na določene regije
   - Brezplačni nivo ima omejitve za GitHub modele

### Pot učenja

Priporočeno vrstno učenje preko lekcij:
1. **00-course-setup** - Začnite tukaj s pripravo okolja
2. **01-intro-to-ai-agents** - Spoznajte osnove AI agentov
3. **02-explore-agentic-frameworks** - Spoznajte različna ogrodja
4. **03-agentic-design-patterns** - Osnovni vzorci načrtovanja
5. Nadaljujte zaporedno s številčenimi lekcijami

### Izbira ogrodja

Izberite ogrodje glede na cilje:
- **Vse lekcije**: Microsoft Agent Framework (MAF) z `AzureAIProjectAgentProvider`
- **Agenti se registrirajo na strežniški strani** v Azure AI Foundry Agent Service V2 in so vidni v Foundry portalu

### Kako dobiti pomoč

- Pridružite se [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Preverite README datoteke lekcij za posebna navodila
- Oglejte si glavni [README.md](./README.md) za pregled tečaja
- Raziščite [Course Setup](./00-course-setup/README.md) za podrobna namestitvena navodila

### Prispevanje

To je odprt izobraževalni projekt. Prispevki so dobrodošli:
- Izboljšajte primere kode
- Popravite pravopisne napake ali napake
- Dodajte pojasnjujoče komentarje
- Predlagajte nove teme lekcij
- Prevedite v dodatne jezike

Oglejte si [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za trenutne potrebe.

## Kontekst specifičen za projekt

### Večjezikovna podpora

Ta repozitorij uporablja avtomatiziran sistem prevajanja:
- Podpora za več kot 50 jezikov
- Prevedene datoteke v imenikih `/translations/<lang-code>/`
- GitHub Actions workflow upravlja posodobitve prevodov
- Izvorne datoteke so v angleščini v korenu repozitorija

### Struktura lekcij

Vsaka lekcija sledi doslednemu vzorcu:
1. Sličica videa s povezavo
2. Pisna vsebina lekcije (README.md)
3. Vzorci kode v več ogrodjih
4. Cilji učenja in predpogoji
5. Dodatni učni viri s povezavami

### Imena vzorcev kode

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcija 1, MAF Python
- `14-sequential.ipynb` - Lekcija 14, MAF napredni vzorci

### Posebni imeniki

- `translated_images/` - Lokalizirane slike za prevode
- `images/` - Izvirne slike za angleško vsebino
- `.devcontainer/` - Konfiguracija razvojnega kontejnerja za VS Code
- `.github/` - GitHub Actions workflow-i in predloge

### Odvisnosti

Ključni paketi iz `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Podpora za Agent-to-Agent protokol
- `azure-ai-inference`, `azure-ai-projects` - Azure AI storitve
- `azure-identity` - Azure avtentikacija (AzureCliCredential)
- `azure-search-documents` - Integracija Azure AI Search
- `mcp[cli]` - Podpora za Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Opozorilo**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvorni jezik je treba upoštevati kot avtoritativni vir. Za kritične informacije priporočamo strokovni prevod s strani človeškega prevajalca. Nismo odgovorni za morebitne napačne interpretacije ali nesporazume, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->