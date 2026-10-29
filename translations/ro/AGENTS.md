# AGENTS.md

## Prezentarea Proiectului

Acest depozit conține "Agenți AI pentru Începători" - un curs educațional cuprinzător care predă tot ce este necesar pentru a construi Agenți AI. Cursul constă în 18 lecții (numerotate 00-18) care acoperă fundamentele, modele de design, framework-uri, implementare în producție, agenți locali/pe dispozitiv și securitatea agenților AI.

**Tehnologii Cheie:**
- Python 3.12+
- Jupyter Notebooks pentru învățare interactivă
- Framework-uri AI: Microsoft Agent Framework (MAF)
- Servicii Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitectură:**
- Structură bazată pe lecții (directorii 00-18)
- Fiecare lecție conține: documentație README, exemple de cod (jurnale Jupyter) și imagini
- Suport multi-limbă prin sistem automatizat de traducere
- Un notebook Python per lecție folosind Microsoft Agent Framework

## Comenzi de Configurare

### Cerințe Prealabile
- Python 3.12 sau versiune superioară
- Abonament Azure (pentru Microsoft Foundry)
- Azure CLI instalat și autentificat (`az login`)

### Configurare Inițială

1. **Clonează sau fă fork la depozit:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Creează și activează mediul virtual Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Instalează dependențele:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurează variabilele de mediu:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Variabile de Mediu Necesare

Pentru **Microsoft Foundry** (Necesar):
- `AZURE_AI_PROJECT_ENDPOINT` - Endpoint-ul proiectului Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Numele implementării modelului (exemplu: gpt-5-mini)

Pentru **Azure AI Search** (Lecția 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - Cheia API Azure AI Search

Autentificare: Rulează `az login` înainte de a rula jurnalele (folosește `AzureCliCredential`).

## Fluxul de Dezvoltare

### Executarea Jupyter Notebooks

Fiecare lecție conține mai multe jurnale Jupyter pentru diferite framework-uri:

1. **Pornește Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navighează la un director de lecție** (exemplu: `01-intro-to-ai-agents/code_samples/`)

3. **Deschide și rulează jurnalele:**
   - `*-python-agent-framework.ipynb` - Folosind Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Folosind Microsoft Agent Framework (.NET)

### Lucrul cu Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Necesită abonament Azure
- Folosește `FoundryChatClient` pentru Agent Service V2 (agenți vizibili în portalul Foundry)
- Pregătit pentru producție cu observabilitate integrată
- Pattern de fișier: `*-python-agent-framework.ipynb`

## Instrucțiuni de Testare

Acesta este un depozit educațional cu cod exemplu mai degrabă decât cod de producție cu teste automate. Pentru a verifica configurarea și modificările tale:

### Testare Manuală

1. **Testează mediul Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testează execuția jurnalelor:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifică variabilele de mediu:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Rularea Jurnale Individuale

Deschide jurnalele în Jupyter și execută celulele în ordine. Fiecare jurnal este autonom și include:
- Declarații de import
- Încărcarea configurației
- Implementări de agenți exemplu
- Rezultate așteptate în celulele markdown

### Testare Sumativă pentru Agenți Implementați

Pentru lecțiile în care un agent este implementat ca agent găzduit în Microsoft Foundry (01, 04, 05, 16), repo-ul include cataloage pentru testare sumativă sub `tests/` care sunt rulate de fluxul `.github/workflows/smoke-test.yml` prin acțiunea [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Acestea sunt un filtru ușor post-implementare (este agentul accesibil și urmează cerințele de prompt de bază?), completând pipeline-ul de evaluare din Lecțiile 10 și 16. Vezi [tests/README.md](./tests/README.md) pentru alocarea catalog-lecție-agent. Lecția 17 rulează local cu Foundry Local și nu are un punct final găzduit, deci este validată prin rularea directă a jurnalului său.

## Stilul Codului

### Convenții Python

- **Versiune Python**: 3.12+
- **Stil Cod**: Urmează convențiile standard Python PEP 8
- **Jurnale**: Folosește celule markdown clare pentru explicarea conceptelor
- **Importuri**: Grupează după bibliotecă standard, terță parte, importuri locale

### Convenții Jupyter Notebook

- Include celule markdown descriptive înaintea codului
- Adaugă exemple de output în jurnale pentru referință
- Folosește nume clare de variabile care corespund conceptelor lecției
- Menține ordinea liniară a executării jurnalului (celula 1 → 2 → 3...)

### Organizarea Fișierelor

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Construire și Implementare

### Construirea Documentației

Acest depozit folosește Markdown pentru documentație:
- Fișiere README.md în fiecare dosar de lecție
- README.md principal la rădăcina depozitului
- Sistem automatizat de traducere prin GitHub Actions

### Pipeline CI/CD

Situat în `.github/workflows/`:

1. **co-op-translator.yml** - Traducere automată în peste 50 de limbi
2. **welcome-issue.yml** - Salută creatorii de issue-uri noi
3. **welcome-pr.yml** - Salută contributorii pull request-urilor noi

### Implementare

Acesta este un depozit educațional - fără proces de implementare. Utilizatorii:
1. Fă fork sau clonează depozitul
2. Rulează jurnalele local sau în GitHub Codespaces
3. Învață modificând și experimentând cu exemplele

## Ghiduri pentru Pull Request

### Înainte de a Trimite

1. **Testează modificările tale:**
   - Rulează complet jurnalele afectate
   - Verifică ca toate celulele să se execute fără erori
   - Asigură-te că rezultatele sunt potrivite

2. **Actualizări de documentație:**
   - Actualizează README.md dacă adaugi concepte noi
   - Adaugă comentarii în jurnale pentru cod complex
   - Asigură-te că celulele markdown explică scopul

3. **Modificări de fișiere:**
   - Evită să comiți fișierele `.env` (folosește `.env.example`)
   - Nu comiți directoarele `venv/` sau `__pycache__/`
   - Păstrează output-urile jurnalelor când demonstrează concepte
   - Elimină fișiere temporare și backup-uri de jurnale (`*-backup.ipynb`)

### Format Titlu PR

Folosește titluri descriptive:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Verificări Necesare

- Jurnalele trebuie să se execute fără erori
- Fișierele README trebuie să fie clare și corecte
- Urmează modelele de cod existente în depozit
- Menține consistența cu celelalte lecții

## Note Suplimentare

### Probleme Comune

1. **Neconcordanță versiune Python:**
   - Asigură-te că folosești Python 3.12+
   - Unele pachete pot să nu funcționeze cu versiuni mai vechi
   - Folosește `python3 -m venv` pentru a specifica explicit versiunea Python

2. **Variabile de mediu:**
   - Creează întotdeauna `.env` din `.env.example`
   - Nu comite fișierul `.env` (este în `.gitignore`)
   - Autentifică-te cu `az login` pentru autentificare Entra ID fără chei

3. **Conflicte de pachete:**
   - Folosește un mediu virtual nou
   - Instalează din `requirements.txt` în loc de pachete individuale
   - Unele jurnale pot necesita pachete adiționale menționate în celulele markdown

4. **Servicii Azure:**
   - Serviciile Azure AI necesită abonament activ
   - Unele funcționalități sunt specifice regiunii
   - Asigură-te că implementarea modelului tău Azure OpenAI suportă API-ul de Răspunsuri

### Parcurs de Învățare

Progres recomandat prin lecții:
1. **00-course-setup** - Începe aici pentru configurarea mediului
2. **01-intro-to-ai-agents** - Înțelege fundamentele agenților AI
3. **02-explore-agentic-frameworks** - Află despre diferite framework-uri
4. **03-agentic-design-patterns** - Modele principale de design
5. Continuă secvențial prin lecțiile numerotate

### Alegerea Framework-ului

Alege framework-ul în funcție de obiectivele tale:
- **Toate lecțiile**: Microsoft Agent Framework (MAF) cu `FoundryChatClient`
- **Agenții se înregistrează pe server** în Microsoft Foundry Agent Service V2 și sunt vizibili în portalul Foundry

### Obținerea Ajutorului

- Alătură-te [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Consultă fișierele README ale lecțiilor pentru indicații specifice
- Verifică README.md principal pentru prezentarea cursului [README.md](./README.md)
- Consultă [Course Setup](./00-course-setup/README.md) pentru instrucțiuni detaliate de configurare

### Contribuții

Acesta este un proiect educațional deschis. Contribuțiile sunt binevenite:
- Îmbunătățirea exemplelor de cod
- Corectarea greșelilor de scriere sau a erorilor
- Adăugarea de comentarii clarificatoare
- Sugestii pentru subiecte noi de lecții
- Traduceri în limbi suplimentare

Vezi [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pentru nevoile curente.

## Context Specific Proiectului

### Suport Multi-Limbă

Acest depozit folosește un sistem automatizat de traducere:
- Suportă peste 50 de limbi
- Traducerile sunt în directoarele `/translations/<lang-code>/`
- Workflow-ul GitHub Actions se ocupă de actualizările de traducere
- Fișierele sursă sunt în engleză la rădăcina depozitului

### Structura Lecțiilor

Fiecare lecție urmează un model consecvent:
1. Miniatură video cu link
2. Conținut scris al lecției (README.md)
3. Exemple de cod în mai multe framework-uri
4. Obiective de învățare și prerechizite
5. Resurse suplimentare de învățare linkuite

### Denumirea Exemplului de Cod

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lecția 1, MAF Python
- `14-sequential.ipynb` - Lecția 14, modele avansate MAF
- `16-python-agent-framework.ipynb` - Lecția 16, agent suport clienți pentru producție
- `17-local-agent-foundry-local.ipynb` - Lecția 17, agent local cu Foundry Local + Qwen

### Directoare Speciale

- `translated_images/` - Imagini localizate pentru traduceri
- `images/` - Imagini originale pentru conținutul în engleză
- `.devcontainer/` - Configurarea container-ului de dezvoltare VS Code
- `.github/` - Workflow-uri și template-uri GitHub Actions

### Dependențe

Pachete cheie din `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suport protocol Agent-la-Agent
- `azure-ai-inference`, `azure-ai-projects` - Servicii Azure AI
- `azure-identity` - Autentificare Azure (AzureCliCredential)
- `azure-search-documents` - Integrare Azure AI Search
- `mcp[cli]` - Suport Protocol Context Model

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->