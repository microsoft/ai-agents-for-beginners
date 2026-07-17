# AGENTS.md

## Pregled projekta

Ta repozitorij vsebuje "AI agente za začetnike" - celovit izobraževalni tečaj, ki uči vse, kar je potrebno za izdelavo AI agentov. Tečaj obsega 18 lekcij (številčene od 00 do 18), ki zajemajo osnove, vzorce načrtovanja, ogrodja, uvajanje v produkcijo, lokalne/na napravi agente in varnost AI agentov.

**Ključne tehnologije:**
- Python 3.12+
- Jupyter Zvezki za interaktivno učenje
- AI ogrodja: Microsoft Agent Framework (MAF)
- Azure AI storitve: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitektura:**
- Struktura, osnovana na lekcijah (mape 00-15+)
- Vsaka lekcija vsebuje: dokumentacijo v README, primere kode (Jupyter zvezke) in slike
- Podpora več jezikov preko avtomatiziranega prevajalskega sistema
- Ena Python zvezek na lekcijo z uporabo Microsoft Agent Framework

## Ukazi za nastavitev

### Predpogoji
- Python 3.12 ali novejši
- Azure naročnina (za Microsoft Foundry)
- Nameščen in preverjen Azure CLI (`az login`)

### Prva nastavitev

1. **Klonirajte ali forknite repozitorij:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ALI
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Ustvarite in aktivirajte Python navidezno okolje:**
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

Za **Microsoft Foundry** (obvezno):
- `AZURE_AI_PROJECT_ENDPOINT` - končna točka projekta Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ime uvajanja modela (npr. gpt-4.1-mini)

Za **Azure AI Search** (Lekcija 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - končna točka Azure AI Search
- `AZURE_SEARCH_API_KEY` - API ključ za Azure AI Search

Avtentikacija: Zaženite `az login` pred zagonom zvezkov (uporablja `AzureCliCredential`).

## Razvojni potek dela

### Zagon Jupyter zvezkov

Vsaka lekcija vsebuje več Jupyter zvezkov za različna ogrodja:

1. **Zaženite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Premaknite se v mapo lekcije** (npr. `01-intro-to-ai-agents/code_samples/`)

3. **Odprite in zaženite zvezke:**
   - `*-python-agent-framework.ipynb` - z uporabo Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - z uporabo Microsoft Agent Framework (.NET)

### Delo z Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Zahteva Azure naročnino
- Uporablja `FoundryChatClient` za Agent Service V2 (agenti vidni v Foundry portalu)
- Pripravljen za produkcijo z vgrajeno opazljivostjo
- Vzorec imen datotek: `*-python-agent-framework.ipynb`

## Navodila za testiranje

To je izobraževalni repozitorij z vzorčno kodo, ne produkcijska koda z avtomatiziranimi testi. Za preverjanje nastavitve in sprememb:

### Ročno testiranje

1. **Preizkusite Python okolje:**
   ```bash
   python --version  # Mora biti 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Preizkusite zagon zvezka:**
   ```bash
   # Pretvori beležnico v skripto in jo zaženi (preizkuša uvoze)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Preverite okoljske spremenljivke:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Zagon posameznih zvezkov

Odprite zvezke v Jupyter in izvajajte celice zaporedno. Vsak zvezek je samostojen in vključuje:
- uvozne izjave
- nalaganje konfiguracije
- primer implementacije agentov
- pričakovane izhode v markdown celicah

### Osnovno testiranje nameščenih agentov

Za lekcije, kjer je agent nameščen kot agent Microsoft Foundry (01, 04, 05, 16), repozitorij vsebuje kataloge za osnovno testiranje v mapi `tests/`, ki jih zažene delovni proces `.github/workflows/smoke-test.yml` preko akcije [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). To je lahek post-deployment preizkus (ali je agent dosegljiv in sledi osnovnim pričakovanjem zahtevka?), ki dopolnjuje ocenjevalno verigo v Lekcijah 10 in 16. Glejte [tests/README.md](./tests/README.md) za povezave med katalogi, lekcijami in agenti. Lekcija 17 teče lokalno s Foundry Local in nima gostujoče končne točke, zato se preverja z neposrednim zagonom njenega zvezka.

## Slog kode

### Python konvencije

- **Različica Pythona**: 3.12+
- **Slog kode**: sledite standardnim Python PEP 8 konvencijam
- **Zvezki**: uporabljajte jasne markdown celice za razlage pojmov
- **Uvozi**: razporedite po standardni knjižnici, tretjih straneh, lokalnih uvozih

### Konvencije Jupyter zvezkov

- Vključite opisne markdown celice pred kodo
- Dodajte primere izhoda v zvezkih za referenco
- Uporabljajte jasne imena spremenljivk, skladna s pojmi lekcije
- Ohranite linearni vrstni red izvajanja zvezka (celica 1 → 2 → 3...)

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

### Izdelava dokumentacije

Ta repozitorij uporablja Markdown za dokumentacijo:
- datoteke README.md v vsaki mapi lekcije
- glavna README.md v korenu repozitorija
- avtomatiziran prevajalski sistem preko GitHub Actions

### CI/CD cevovod

Nahaja se v `.github/workflows/`:

1. **co-op-translator.yml** - samodejni prevod v 50+ jezikov
2. **welcome-issue.yml** - pozdravi nove ustvarjalce težav
3. **welcome-pr.yml** - pozdravi nove prispevke pull requestov

### Uvajanje

To je izobraževalni repozitorij - ni procesa uvajanja. Uporabniki:
1. forknite ali klonirajte repozitorij
2. zaženite zvezke lokalno ali v GitHub Codespaces
3. učite se z modificiranjem in eksperimentiranjem z vzorci

## Smernice za Pull Request

### Pred oddajo

1. **Preizkusite svoje spremembe:**
   - popolnoma zaženite prizadete zvezke
   - preverite, da se vse celice izvajajo brez napak
   - preverite, da so izhodi ustrezni

2. **Posodobitve dokumentacije:**
   - posodobite README.md, če dodajate nove pojme
   - dodajte komentarje v zvezke za kompleksno kodo
   - zagotovite, da markdown celice razložijo namen

3. **Spremembe datotek:**
   - ne vključujte `.env` datotek (uporabite `.env.example`)
   - ne vključujte map `venv/` ali `__pycache__/`
   - obdržite izhode zvezkov, če prikazujejo pojme
   - odstranite začasne datoteke in varnostne kopije zvezkov (`*-backup.ipynb`)

### Oblika naslova PR

Uporabite opisne naslove:
- `[Lesson-XX] Dodaj nov primer za <pojmov>`
- `[Fix] Popravi tipkarsko napako v README lekcije XX`
- `[Update] Izboljšaj primer kode v lekciji XX`
- `[Docs] Posodobi navodila za nastavitev`

### Obvezni pregledi

- Zvezki morajo teči brez napak
- README datoteke naj bodo jasne in točne
- Sledite obstoječim vzorcem kode v repozitoriju
- Ohranite doslednost z drugimi lekcijami

## Dodatne opombe

### Pogoste težave

1. **Neujemanje različice Pythona:**
   - zagotovite uporabo Pythona 3.12+
   - nekateri paketi morda ne delujejo s starejšimi različicami
   - uporabite `python3 -m venv` za natančno določitev različice Pythona

2. **Okoljske spremenljivke:**
   - vedno ustvarite `.env` iz `.env.example`
   - ne vključujte `.env` datoteke v repozitorij (je v `.gitignore`)
   - prijavite se z `az login` za preverjanje pristnosti brez ključa Entra ID

3. **Konflikti paketov:**
   - uporabite sveže navidezno okolje
   - namestite iz `requirements.txt` namesto posameznih paketov
   - nekateri zvezki morda zahtevajo dodatne pakete, omenjene v markdown celicah

4. **Azure storitve:**
   - Azure AI storitve zahtevajo aktivno naročnino
   - nekatere funkcije so specifične za regijo
   - preverite, da vaša Azure OpenAI implementacija podpira Responses API

### Učni načrt

Priporočeni vrstni red lekcij:
1. **00-course-setup** - začnite tukaj za nastavitev okolja
2. **01-intro-to-ai-agents** - spoznajte osnove AI agentov
3. **02-explore-agentic-frameworks** - naučite se o različnih ogrodjih
4. **03-agentic-design-patterns** - osnovni vzorci načrtovanja
5. nadaljujte po številčnih lekcijah zaporedoma

### Izbira ogrodja

Izberite ogrodje glede na vaše cilje:
- **Vse lekcije**: Microsoft Agent Framework (MAF) z `FoundryChatClient`
- **Agenti se registrirajo na strežniški strani** v Microsoft Foundry Agent Service V2 in so vidni v portalu Foundry

### Pomoč

- Pridružite se [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Preglejte README datoteke lekcij za posebna navodila
- Preverite glavni [README.md](./README.md) za pregled tečaja
- Oglejte si [Course Setup](./00-course-setup/README.md) za podrobna navodila za nastavitev

### Prispevanje

To je odprt izobraževalni projekt. Prispevki so dobrodošli:
- izboljšajte primere kode
- popravite tipke ali napake
- dodajte pojasnilne komentarje
- predlagajte nove teme lekcij
- prevedite v dodatne jezike

Oglejte si [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) za trenutne potrebe.

## Projektno specifičen kontekst

### Podpora za več jezikov

Ta repozitorij uporablja avtomatiziran prevajalski sistem:
- 50+ podprtih jezikov
- Prevodi v mapah `/translations/<lang-code>/`
- Delovni tok GitHub Actions upravlja posodobitve prevodov
- Izvorne datoteke so v angleščini v korenu repozitorija

### Struktura lekcije

Vsaka lekcija sledi doslednemu vzorcu:
1. Video sličica z povezavo
2. Pisna vsebina lekcije (README.md)
3. Primeri kode v več ogrodjih
4. Učni cilji in predpogoji
5. Dodatni učni viri z povezavami

### Imenovanje primerov kode

Oblika: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcija 1, MAF Python
- `14-sequential.ipynb` - Lekcija 14, MAF napredni vzorci
- `16-python-agent-framework.ipynb` - Lekcija 16, agent za podporo strankam v produkciji
- `17-local-agent-foundry-local.ipynb` - Lekcija 17, lokalni agent z Foundry Local + Qwen

### Posebne mape

- `translated_images/` - lokalizirane slike za prevode
- `images/` - izvirne slike za angleško vsebino
- `.devcontainer/` - konfiguracija razvojnega kontejnerja VS Code
- `.github/` - GitHub Actions delovni tok in predloge

### Odvisnosti

Ključni paketi iz `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - podpora protokolu Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Azure AI storitve
- `azure-identity` - Azure avtentikacija (AzureCliCredential)
- `azure-search-documents` - integracija Azure AI Search
- `mcp[cli]` - podpora za Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->