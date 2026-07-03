# AGENTS.md

## Pregled projekta

Ta repozitorij vsebuje "AI Agentov za začetnike" - celovit izobraževalni tečaj, ki uči vse, kar je potrebno za izdelavo AI agentov. Tečaj obsega 18 lekcij, ki pokrivajo osnove, dizajnerske vzorce, ogrodja in produkcijsko uvajanje AI agentov.

**Ključne tehnologije:**
- Python 3.12+
- Jupyter zvezki za interaktivno učenje
- AI ogrodja: Microsoft Agent Framework (MAF)
- Azure AI storitve: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arhitektura:**
- Struktura na osnovi lekcij (imeniki 00-15+)
- Vsaka lekcija vsebuje: dokumentacijo README, primere kode (Jupyter zvezke) in slike
- Podpora za več jezikov preko avtomatskega sistema prevajanja
- Ena Python zvezek na lekcijo, ki uporablja Microsoft Agent Framework

## Ukazi za nastavitev

### Zahteve
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

2. **Ustvarite in aktivirajte virtualno okolje za Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Na Windows: venv\Scripts\activate
   ```

3. **Namestite odvisnosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nastavite spremenljivke okolja:**
   ```bash
   cp .env.example .env
   # Uredite .env z vašimi API ključi in končnimi točkami
   ```

### Zahtevane spremenljivke okolja

Za **Azure AI Foundry** (zahtevano):
- `AZURE_AI_PROJECT_ENDPOINT` - končna točka projekta Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ime uvajanja modela (npr. gpt-4o)

Za **Azure AI Search** (Lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - končna točka Azure AI Search
- `AZURE_SEARCH_API_KEY` - ključ API za Azure AI Search

Avtentikacija: Pred zagonom zvezkov izvedite `az login` (uporablja `AzureCliCredential`).

## Razvojni potek dela

### Zagon Jupyter zvezkov

Vsaka lekcija vsebuje več Jupyter zvezkov za različna ogrodja:

1. **Zaženite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Pomaknite se do imenika lekcije** (npr. `01-intro-to-ai-agents/code_samples/`)

3. **Odprite in zaženite zvezke:**
   - `*-python-agent-framework.ipynb` - uporaba Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - uporaba Microsoft Agent Framework (.NET)

### Delo z Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Zahteva Azure naročnino
- Uporablja `AzureAIProjectAgentProvider` za Agent Service V2 (agenti vidni na portalu Foundry)
- Pripravljen za produkcijo z vgrajeno opaznostjo
- Vzorec datotek: `*-python-agent-framework.ipynb`

## Navodila za testiranje

To je izobraževalni repozitorij z vzorčno kodo in ne produkcijska koda z avtomatiziranimi testi. Za preverjanje nastavitve in sprememb:

### Ročno testiranje

1. **Testiranje Python okolja:**
   ```bash
   python --version  # Mora biti 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test izvajanja zvezka:**
   ```bash
   # Pretvori zvezek v skripto in zaženi (preizkusi uvoze)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Preverite spremenljivke okolja:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Zagon posameznih zvezkov

Odprite zvezke v Jupyterju in izvajajte celice zaporedno. Vsak zvezek je samostojen in vsebuje:
- Izjave o uvozu
- Nalaganje konfiguracije
- Primeri implementacije agentov
- Pričakovane izhode v markdown celicah

## Stil kode

### Python konvencije

- **Različica Pythona**: 3.12+
- **Stil kode**: Sledite standardnim Python PEP 8 konvencijam
- **Zvezki**: Uporabljajte jasne markdown celice za razlago konceptov
- **Uvozi**: Združujte po standardni knjižnici, tretjih straneh, lokalnih uvozih

### Konvencije za Jupyter zvezke

- Vključite opisne markdown celice pred kode
- Dodajte primere izhodov v zvezkih za referenco
- Uporabljajte jasna imena spremenljivk, ki ustrezajo lekcijam
- Ohranjajte linearni vrstni red izvajanja zvezka (celica 1 → 2 → 3...)

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
- Datoteke README.md v vsakem imeniku lekcije
- Glavni README.md v korenu repozitorija
- Avtomatski sistem prevajanja preko GitHub Actions

### CI/CD cevovod

Nahaja se v `.github/workflows/`:

1. **co-op-translator.yml** - samodejni prevod v 50+ jezikov
2. **welcome-issue.yml** - pozdravlja ustvarjalce novih težav
3. **welcome-pr.yml** - pozdravlja nove prispevke pull requestov

### Uvajanje

To je izobraževalni repozitorij - brez procesa uvajanja. Uporabniki:
1. Fork ali klonirajo repozitorij
2. Zagnajo zvezke lokalno ali v GitHub Codespaces
3. Se učijo z modificiranjem in preizkušanjem primerov

## Smernice za pull requeste

### Pred oddajo

1. **Preizkusite spremembe:**
   - Popolnoma zaženite zvezke, ki jih spremembe vplivajo
   - Preverite, da vse celice tečejo brez napak
   - Preverite, ali so izhodi primerni

2. **Posodobitve dokumentacije:**
   - Posodobite README.md, če dodajate nove koncepte
   - Dodajte komentarje v zvezkih za kompleksno kodo
   - Zagotovite, da markdown celice razlagajo namen

3. **Spremembe datotek:**
   - Izogibajte se commitanju `.env` datotek (uporabite `.env.example`)
   - Ne commajte imenikov `venv/` ali `__pycache__/`
   - Ohranjajte izhode zvezkov, če prikazujejo koncepte
   - Odstranite začasne datoteke in varnostne kopije zvezkov (`*-backup.ipynb`)

### Oblika naslova PR

Uporabljajte opisne naslove:
- `[Lesson-XX] Dodaj nov primer za <koncept>`
- `[Fix] Popravi tipkarsko napako v README lekcije-XX`
- `[Update] Izboljšaj primer kode v lekciji-XX`
- `[Docs] Posodobi navodila za nastavitev`

### Zahtevane kontrole

- Zvezki morajo teči brez napak
- README datoteke morajo biti jasne in natančne
- Sledite obstoječim vzorcem kode v repozitoriju
- Ohranjajte skladnost z drugimi lekcijami

## Dodatne opombe

### Pogoste težave

1. **Neujemanje različice Pythona:**
   - Poskrbite, da uporabljate Python 3.12+
   - Nekateri paketi morda ne delujejo z starejšimi različicami
   - Uporabite `python3 -m venv` za eksplicitno določitev različice

2. **Spremenljivke okolja:**
   - Vedno ustvarite `.env` iz `.env.example`
   - Ne commajte `.env` datoteke (vključeno v `.gitignore`)
   - GitHub žeton potrebuje primerna dovoljenja

3. **Konflikti paketov:**
   - Uporabite sveže virtualno okolje
   - Namestite iz `requirements.txt`, ne posamičnih paketov
   - Nekateri zvezki lahko zahtevajo dodatne pakete, navedene v markdown celicah

4. **Azure storitve:**
   - Azure AI storitve zahtevajo aktivno naročnino
   - Nekatere funkcije so regionalno omejene
   - Omejitve brezplačnega nivoja veljajo za GitHub modele

### Pot učenja

Priporočeni napredek skozi lekcije:
1. **00-course-setup** - Začetek za nastavitev okolja
2. **01-intro-to-ai-agents** - Razumevanje osnov AI agentov
3. **02-explore-agentic-frameworks** - Spoznajte različna ogrodja
4. **03-agentic-design-patterns** - Ključni dizajnerski vzorci
5. Nadaljujte skozi oštevilčene lekcije zaporedno

### Izbira ogrodja

Izberite ogrodje glede na cilje:
- **Vse lekcije**: Microsoft Agent Framework (MAF) z `AzureAIProjectAgentProvider`
- **Agenti se registrirajo strežniško** v Azure AI Foundry Agent Service V2 in so vidni na portalu Foundry

### Kako dobiti pomoč

- Pridružite se [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Preberite README datoteke lekcij za specifična navodila
- Preverite glavni [README.md](./README.md) za pregled tečaja
- Oglejte si [Course Setup](./00-course-setup/README.md) za podrobna navodila

### Prispevanje

To je odprt izobraževalni projekt. Prispevki so dobrodošli:
- Izboljšanje primerov kode
- Popravljanje tipkarskih napak ali drugih napak
- Dodajanje pojasnjevalnih komentarjev
- Predlaganje novih tem za lekcije
- Prevajanje v dodatne jezike

Trenutne potrebe so navedene na [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues).

## Posebni kontekst projekta

### Podpora za več jezikov

Ta repozitorij uporablja avtomatski prevajalski sistem:
- Podpira več kot 50 jezikov
- Prevodi so v imenikih `/translations/<lang-code>/`
- GitHub Actions skripta skrbi za posodobitve prevodov
- Izvorne datoteke so v angleščini v korenu repozitorija

### Struktura lekcij

Vsaka lekcija sledi doslednemu vzorcu:
1. Sličica videa s povezavo
2. Pisna vsebina lekcije (README.md)
3. Primeri kode v več ogrodjih
4. Cilji učenja in zahtevana predznanja
5. Dodatni viri za učenje z povezavami

### Imenovanje primerov kode

Format: `<številka-lekcije>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - lekcija 1, MAF Python
- `14-sequential.ipynb` - lekcija 14, napredni vzorci MAF

### Posebni imeniki

- `translated_images/` - lokalizirane slike za prevode
- `images/` - originalne slike za angleško vsebino
- `.devcontainer/` - konfiguracija razvojnega kontejnerja za VS Code
- `.github/` - GitHub Actions workflowi in predloge

### Odvisnosti

Glavni paketi iz `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - podpora za protokol Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Azure AI storitve
- `azure-identity` - Azure avtentikacija (AzureCliCredential)
- `azure-search-documents` - integracija Azure AI Search
- `mcp[cli]` - podpora za Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->