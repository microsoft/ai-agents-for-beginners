# AGENTS.md

## Pregled projekta

To repozitorij vsebuje "AI agente za začetnike" - obsežen izobraževalni tečaj, ki uči vse, kar je potrebno za izdelavo AI agentov. Tečaj obsega 18 lekcij (številčne od 00 do 18), ki zajemajo osnove, oblikovalske vzorce, ogrodja, uvajanje v produkcijo, lokalne/naprave-agente in varnost AI agentov.

**Ključne tehnologije:**
- Python 3.12+
- Jupyter zvezki za interaktivno učenje
- AI ogrodja: Microsoft Agent Framework (MAF)
- Azure AI storitve: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitektura:**
- Struktura na osnovi lekcij (mape 00-15+)
- Vsaka lekcija vsebuje: dokumentacijo README, vzorce kode (Jupyter zvezki) in slike
- Podpora več jezikom prek avtomatiziranega prevajalskega sistema
- En Python zvezek na lekcijo z uporabo Microsoft Agent Framework

## Ukazi za namestitev

### Predpogoji
- Python 3.12 ali novejši
- Azure naročnina (za Microsoft Foundry)
- Azure CLI nameščen in prijavljen (`az login`)

### Začetna namestitev

1. **Kloniraj ali forkej repozitorij:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ALI
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Ustvari in aktiviraj Python virtualno okolje:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Na Windows: venv\Scripts\activate
   ```

3. **Namesti odvisnosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nastavi okoljske spremenljivke:**
   ```bash
   cp .env.example .env
   # Uredite .env z vašimi API ključi in končnimi točkami
   ```

### Potrebne okoljske spremenljivke

Za **Microsoft Foundry** (obvezno):
- `AZURE_AI_PROJECT_ENDPOINT` - konec točke projekta Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ime uvajanja modela (npr. gpt-5-mini)

Za **Azure AI Search** (lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - konec točke Azure AI Search
- `AZURE_SEARCH_API_KEY` - API ključ Azure AI Search

Avtentikacija: Zaženi `az login` pred zagonom zvezkov (uporablja `AzureCliCredential`).

## Razvojni potek

### Zagon Jupyter zvezkov

Vsaka lekcija vsebuje več Jupyter zvezkov za različna ogrodja:

1. **Zaženi Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Pojdi v mapo z lekcijo** (npr. `01-intro-to-ai-agents/code_samples/`)

3. **Odpri in zaženi zvezke:**
   - `*-python-agent-framework.ipynb` - z uporabo Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - z uporabo Microsoft Agent Framework (.NET)

### Delo z Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Zahteva Azure naročnino
- Uporablja `FoundryChatClient` za Agent Service V2 (agenti so vidni v portalu Foundry)
- Pripravljen za produkcijo z vgrajeno opazljivostjo
- Vzorec datotek: `*-python-agent-framework.ipynb`

## Navodila za testiranje

To je izobraževalni repozitorij z vzorčno kodo in ne produkcijska koda z avtomatiziranimi testi. Za preverjanje vaše namestitve in sprememb:

### Ročno testiranje

1. **Preizkusi Python okolje:**
   ```bash
   python --version  # Mora biti 3.12 ali več
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Preizkusi izvedbo zvezkov:**
   ```bash
   # Pretvori zvezek v skripto in zaženi (preizkusi uvoze)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Preveri okoljske spremenljivke:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Zagon posameznih zvezkov

Odpri zvezke v Jupyterju in zaporedno izvedi celice. Vsak zvezek je samostojen in vključuje:
- Uvozne izjave
- Nalaganje konfiguracije
- Primeri implementacij agentov
- Pričakovani izhodi v markdown celicah

### Smoke-testiranje uvajanih agentov

Za lekcije, kjer je agent uvajan kot gostujoči agent Microsoft Foundry (01, 04, 05, 16), repozitorij vsebuje smoke-test kataloge v `tests/`, ki jih izvaja workflow `.github/workflows/smoke-test.yml` preko akcije [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). To je lahka kontrola po uvajanju (ali je agent dosegljiv in sledi osnovnim pričakovanjem poziva?), ki dopolnjuje ocenjevalno verigo v lekcijah 10 in 16. Glej [tests/README.md](./tests/README.md) za povezavo med katalogom, lekcijo in agentom. Lekcija 17 teče lokalno z Foundry Local in nima gostujoče končne točke, zato se preveri z neposrednim zagonom zvezka.

## Slog kode

### Python konvencije

- **Python verzija**: 3.12+
- **Slog kode**: Sledi standardnim Python PEP 8 konvencijam
- **Zvezki**: Uporabi jasne markdown celice za razlago konceptov
- **Uvozi**: Združi po standardnih knjižnicah, tretjih straneh, lokalnih uvozih

### Konvencije Jupyter zvezkov

- Vključi opisne markdown celice pred celicami s kodo
- Dodaj primere izhodov v zvezkih za primere
- Uporabi jasna imena spremenljivk, ki ustrezajo konceptom lekcije
- Ohrani linearno zaporedje izvajanja zvezka (celica 1 → 2 → 3...)

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
- Avtomatiziran prevajalski sistem preko GitHub Actions

### CI/CD cevovod

Nahaja se v `.github/workflows/`:

1. **co-op-translator.yml** - Samodejni prevod v 50+ jezikov
2. **welcome-issue.yml** - Pozdravlja ustvarjalce novih težav
3. **welcome-pr.yml** - Pozdravlja prispevke pull requestov

### Uvajanje

To je izobraževalni repozitorij - brez procesa uvajanja. Uporabniki:
1. Forkej ali kloniraj repozitorij
2. Zaženi zvezke lokalno ali v GitHub Codespaces
3. Uči se z urejanjem in eksperimentiranjem z vzorci

## Navodila za Pull Request

### Pred oddajo

1. **Testiraj svoje spremembe:**
   - Popolnoma zaženi prizadete zvezke
   - Preveri, da vse celice tečejo brez napak
   - Preveri, da so izhodi ustrezni

2. **Posodobitve dokumentacije:**
   - Posodobi README.md, če dodajaš nove koncepte
   - Dodaj komentarje v zvezkih za zahtevno kodo
   - Poskrbi, da markdown celice pojasnjujejo namen

3. **Spremembe datotek:**
   - Izogibaj se dodajanju `.env` datotek (uporabi `.env.example`)
   - Ne potiskaj map `venv/` ali `__pycache__/`
   - Ohrani izhode zvezkov, če prikazujejo koncepte
   - Odstrani začasne datoteke in varnostne kopije zvezkov (`*-backup.ipynb`)

### Format naslova PR

Uporabi opisne naslove:
- `[Lesson-XX] Dodaj nov primer za <koncept>`
- `[Fix] Popravi tipkarsko napako v lesson-XX README`
- `[Update] Izboljšaj vzorec kode v lesson-XX`
- `[Docs] Posodobi navodila za namestitev`

### Zahtevane kontrole

- Zvezki morajo teči brez napak
- README datoteke morajo biti jasne in točne
- Sledi obstoječim vzorcem kode v repozitoriju
- Ohrani konsistentnost z ostalimi lekcijami

## Dodatne opombe

### Pogoste pasti

1. **Neujemanje verzije Pythona:**
   - Poskrbi, da uporabljaš Python 3.12+
   - Nekateri paketi morda ne delujejo na starejših verzijah
   - Za natančno določitev verzije uporabi `python3 -m venv`

2. **Okoljske spremenljivke:**
   - Vedno ustvari `.env` iz `.env.example`
   - Ne potiskaj `.env` datoteke (je v `.gitignore`)
   - Prijavi se z `az login` za prijavo brez ključev z Entra ID

3. **Spori med paketi:**
   - Uporabi sveže virtualno okolje
   - Namesti iz `requirements.txt` namesto posameznih paketov
   - Nekateri zvezki potrebujejo dodatne pakete navedene v markdown celicah

4. **Azure storitve:**
   - Azure AI storitve zahtevajo aktivno naročnino
   - Nekatere funkcije so specifične za regijo
   - Poskrbi, da tvoje uvajanje modela Azure OpenAI podpira Responses API

### Pot učenja

Priporočeno zaporedje lekcij:
1. **00-course-setup** - Začni tukaj za nastavitev okolja
2. **01-intro-to-ai-agents** - Razumi osnove AI agentov
3. **02-explore-agentic-frameworks** - Spoznaj različna ogrodja
4. **03-agentic-design-patterns** - Osnovni oblikovalski vzorci
5. Nadaljuj s številčnimi lekcijami zaporedoma

### Izbira ogrodja

Izberi ogrodje glede na cilje:
- **Vse lekcije**: Microsoft Agent Framework (MAF) z `FoundryChatClient`
- **Agenti se registrirajo na strežniški strani** v Microsoft Foundry Agent Service V2 in so vidni v portalu Foundry

### Pomoč

- Pridruži se [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Preglej README datoteke posameznih lekcij za specifična navodila
- Preveri glavni [README.md](./README.md) za pregled tečaja
- Oglej si [Course Setup](./00-course-setup/README.md) za podrobna navodila za nastavitev

### Prispevanje

To je odprt izobraževalni projekt. Prispevki so dobrodošli:
- Izboljšaj vzorce kode
- Popravi tipkarske napake ali napake
- Dodaj pojasnilne komentarje
- Predlagaj nove teme lekcij
- Prevedi v dodatne jezike

Glej [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za trenutne potrebe.

## Kontekst specifičen za projekt

### Podpora več jezikom

Ta repozitorij uporablja avtomatizirani prevajalski sistem:
- Podprto 50+ jezikov
- Prevodi v mapah `/translations/<lang-code>/`
- GitHub Actions workflow upravlja osvežitev prevodov
- Izvorne datoteke so v angleščini v korenu repozitorija

### Struktura lekcije

Vsaka lekcija sledi skladnemu vzorcu:
1. Predogled videa s povezavo
2. Pisna vsebina lekcije (README.md)
3. Vzorce kode v več ogrodjih
4. Cilji učenja in predpogoji
5. Dodatni učni viri s povezavami

### Poimenovanje vzorcev kode

Format: `<število-lekcije>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcija 1, MAF Python
- `14-sequential.ipynb` - Lekcija 14, MAF napredni vzorci
- `16-python-agent-framework.ipynb` - Lekcija 16, produkcijski agent za podporo strankam
- `17-local-agent-foundry-local.ipynb` - Lekcija 17, lokalni agent z Foundry Local + Qwen

### Posebne mape

- `translated_images/` - Lokalizirane slike za prevode
- `images/` - Izvirne slike za angleško vsebino
- `.devcontainer/` - Konfiguracija razvojnega kontejnerja za VS Code
- `.github/` - GitHub Actions workflowi in predloge

### Odvisnosti

Ključni paketi iz `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Podpora protokolu agent-agenta
- `azure-ai-inference`, `azure-ai-projects` - Azure AI storitve
- `azure-identity` - Azure avtentikacija (AzureCliCredential)
- `azure-search-documents` - Integracija Azure AI Search
- `mcp[cli]` - Podpora Model Context Protokolu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->