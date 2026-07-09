# AGENTS.md

## Pregled projekta

Ta repozitorij vsebuje "AI agente za začetnike" - celovit izobraževalni tečaj, ki poučuje vse, kar je potrebno za gradnjo AI agentov. Tečaj zajema 18 lekcij, ki pokrivajo osnove, oblikovalske vzorce, okvire in produkcijsko uvajanje AI agentov.

**Ključne tehnologije:**
- Python 3.12+
- Jupyter beležnice za interaktivno učenje
- AI okviri: Microsoft Agent Framework (MAF)
- Azure AI storitve: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitektura:**
- Struktura po lekcijah (mape 00-15+)
- Vsaka lekcija vsebuje: dokumentacijo README, primerke kode (Jupyter beležnice) in slike
- Večjezična podpora preko avtomatiziranega prevajalskega sistema
- Ena Python beležnica na lekcijo, ki uporablja Microsoft Agent Framework

## Ukazi za nastavitev

### Zahteve
- Python 3.12 ali višji
- Azure naročnina (za Microsoft Foundry)
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

### Zahtevane okoljske spremenljivke

Za **Microsoft Foundry** (zahtevano):
- `AZURE_AI_PROJECT_ENDPOINT` - konec projekta Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ime uvajanja modela (npr. gpt-4o)

Za **Azure AI Search** (Lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - konec storitve Azure AI Search
- `AZURE_SEARCH_API_KEY` - ključ API za Azure AI Search

Avtentikacija: Zaženite `az login` pred zagonom beležnic (uporablja `AzureCliCredential`).

## Delovni proces razvoja

### Zagon Jupyter beležnic

Vsaka lekcija vsebuje več Jupyter beležnic za različne okvire:

1. **Zaženite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Pomaknite se v mapo lekcije** (npr. `01-intro-to-ai-agents/code_samples/`)

3. **Odprite in zaženite beležnice:**
   - `*-python-agent-framework.ipynb` - uporaba Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - uporaba Microsoft Agent Framework (.NET)

### Delo z Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Zahteva Azure naročnino
- Uporablja `FoundryChatClient` za Agent Service V2 (agenti vidni na portalu Foundry)
- Pripravljen za produkcijo z vgrajeno opaznostjo
- Vzorec datoteke: `*-python-agent-framework.ipynb`

## Navodila za testiranje

Gre za izobraževalni repozitorij z vzorčno kodo, ne produkcijsko kodo z avtomatiziranimi testi. Za preverjanje nastavitve in sprememb:

### Ročno testiranje

1. **Testirajte Python okolje:**
   ```bash
   python --version  # Mora biti 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testirajte izvajanje beležnice:**
   ```bash
   # Pretvori zvezek v skripto in zaženi (preizkusi uvoze)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Preverite okoljske spremenljivke:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Zagon posameznih beležnic

Odprite beležnice v Jupyterju in izvajajte celice zaporedoma. Vsaka beležnica je samostojna in vključuje:
- Izjave o uvozu
- Nalaganje konfiguracije
- Primer implementacije agentov
- Pričakovani izhodi v markdown celicah

## Slog kode

### Priporočila za Python

- **Različica Pythona**: 3.12+
- **Slog kode**: Sledite standardnim Python PEP 8 smernicam
- **Beležnice**: Uporabite jasne markdown celice za razlago konceptov
- **Uvozi**: Gruzirajte po standardni knjižnici, tretjih strankah, lokalnih uvozih

### Priporočila za Jupyter beležnice

- Vključite opisne markdown celice pred kodo
- Dodajte primere izhodov v beležnice za referenco
- Uporabite jasna imena spremenljivk, ki ustrezajo konceptom lekcije
- Ohranite linearni vrstni red izvajanja beležnice (celica 1 → 2 → 3...)

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
- Glavna README.md datoteka v korenu repozitorija
- Avtomatiziran prevajalski sistem preko GitHub Actions

### CI/CD cevovod

Nahaja se v `.github/workflows/`:

1. **co-op-translator.yml** - Samodejni prevod v več kot 50 jezikov
2. **welcome-issue.yml** - Pozdravi ustvarjalce novih problemov
3. **welcome-pr.yml** - Pozdravi nove prispevke pull request-ov

### Uvajanje

To je izobraževalni repozitorij - ni postopek uvajanja. Uporabniki:
1. Forrnkajo ali klonirajo repozitorij
2. Zaženejo beležnice lokalno ali v GitHub Codespaces
3. Se učijo z izmenjavami in eksperimenti z vzorci

## Smernice za pull request-e

### Pred oddajo

1. **Preizkusite svoje spremembe:**
   - Popolnoma zaženite prizadete beležnice
   - Preverite, da se vse celice izvedejo brez napak
   - Preverite, da so izhodi ustrezni

2. **Posodobitve dokumentacije:**
   - Posodobite README.md, če dodajate nove koncepte
   - Dodajte komentarje v beležnice za kompleksno kodo
   - Zagotovite, da markdown celice pojasnijo namen

3. **Spremembe datotek:**
   - Izogibajte se commitu `.env` datotek (uporabite `.env.example`)
   - Ne committajte map `venv/` ali `__pycache__/`
   - Ohranite izhode beležnic, kadar prikazujejo koncepte
   - Odstranite začasne datoteke in varnostne kopije beležnic (`*-backup.ipynb`)

### Oblika naslova PR

Uporabite opisne naslove:
- `[Lesson-XX] Dodaj nov primer za <koncept>`
- `[Fix] Popravi tipkarsko napako v lesson-XX README`
- `[Update] Izboljšaj primerek kode v lesson-XX`
- `[Docs] Posodobi navodila za nastavitev`

### Zahtevani pregledi

- Beležnice naj se izvajajo brez napak
- README datoteke naj bodo jasne in točne
- Sledite obstoječim vzorcem v repozitoriju
- Ohranjajte konsistentnost z ostalimi lekcijami

## Dodatne opombe

### Pogoste težave

1. **Neskladje različice Pythona:**
   - Uporabite Python 3.12+
   - Nekateri paketi morda ne delujejo z starejšimi različicami
   - Uporabite `python3 -m venv` za eksplicitno določitev različice

2. **Okoljske spremenljivke:**
   - Vedno ustvarite `.env` iz `.env.example`
   - Ne committajte `.env` datoteke (je v `.gitignore`)
   - Prijavite se z `az login` za avtentikacijo brez ključa Entra ID

3. **Konflikti paketov:**
   - Uporabite sveže virtualno okolje
   - Namestite iz `requirements.txt` namesto posameznih paketov
   - Nekatere beležnice lahko zahtevajo dodatne pakete, navedene v markdown celicah

4. **Azure storitve:**
   - Azure AI storitve zahtevajo aktivno naročnino
   - Nekatere funkcije so specifične za regijo
   - Preverite, da vaše uvajanje Azure OpenAI modela podpira API za odzive

### Pot učenja

Priporočeno zaporedje lekcij:
1. **00-course-setup** - Začnite tukaj za nastavitev okolja
2. **01-intro-to-ai-agents** - Razumite temelje AI agentov
3. **02-explore-agentic-frameworks** - Spoznajte različne okvire
4. **03-agentic-design-patterns** - Ključni oblikovalski vzorci
5. Nadaljujte zaporedno skozi numerirane lekcije

### Izbira okvira

Izberite okvir glede na vaše cilje:
- **Vse lekcije**: Microsoft Agent Framework (MAF) z `FoundryChatClient`
- **Agenti se registrirajo na strežniški strani** v Microsoft Foundry Agent Service V2 in so vidni v portalu Foundry

### Dobivanje pomoči

- Pridružite se [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Preglejte README datoteke lekcij za specifična navodila
- Preverite glavni [README.md](./README.md) za pregled tečaja
- Obrnite se na [Course Setup](./00-course-setup/README.md) za podrobna navodila za nastavitev

### Prispevanje

To je odprt izobraževalni projekt. Prispevki so dobrodošli:
- Izboljšajte primere kode
- Popravite tipkarske napake ali napake
- Dodajte pojasnilne komentarje
- Predlagajte nove teme lekcij
- Prevajajte v dodatne jezike

Oglejte si [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za trenutne potrebe.

## Kontekst specifičen za projekt

### Večjezična podpora

Ta repozitorij uporablja avtomatiziran prevajalski sistem:
- Podprto več kot 50 jezikov
- Prevodi v mapah `/translations/<lang-code>/`
- GitHub Actions obdeluje posodobitve prevodov
- Izvorne datoteke so v angleščini v korenu repozitorija

### Struktura lekcije

Vsaka lekcija sledi doslednemu vzorcu:
1. Sličica videa s povezavo
2. Pisna vsebina lekcije (README.md)
3. Primerki kode v več okvirih
4. Cilji učenja in zahteve
5. Povezana dodatna učna gradiva

### Imenovanje vzorcev kode

Oblika: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcija 1, MAF Python
- `14-sequential.ipynb` - Lekcija 14, napredni vzorci MAF

### Posebne mape

- `translated_images/` - Lokalizirane slike za prevode
- `images/` - Izvirne slike za angleško vsebino
- `.devcontainer/` - konfiguracija razvojnega kontejnerja VS Code
- `.github/` - GitHub Actions delovni tokovi in predloge

### Odvisnosti

Ključni paketi iz `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Podpora protokolu Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Azure AI storitve
- `azure-identity` - Azure avtentikacija (AzureCliCredential)
- `azure-search-documents` - Integracija Azure AI Search
- `mcp[cli]` - Podpora Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->