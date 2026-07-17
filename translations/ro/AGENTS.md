# AGENTS.md

## Prezentare generală a proiectului

Acest depozit conține „Agenți AI pentru Începători” - un curs educațional cuprinzător care predă tot ce este necesar pentru a construi Agenți AI. Cursul constă din 18 lecții (numerotate de la 00 la 18) care acoperă elementele fundamentale, modele de design, cadre, implementare în producție, agenți locali/pe dispozitiv și securitatea agenților AI.

**Tehnologii cheie:**
- Python 3.12+
- Jupyter Notebooks pentru învățare interactivă
- Cadre AI: Microsoft Agent Framework (MAF)
- Servicii Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitectură:**
- Structură bazată pe lecții (directoare 00-15+)
- Fiecare lecție conține: documentație README, exemple de cod (Jupyter notebooks) și imagini
- Suport multilingv prin sistem automatizat de traducere
- Un notebook Python per lecție folosind Microsoft Agent Framework

## Comenzi de configurare

### Cerințe preliminare
- Python 3.12 sau o versiune superioară
- Abonament Azure (pentru Microsoft Foundry)
- Azure CLI instalat și autentificat (`az login`)

### Configurare inițială

1. **Clonați sau faceți fork depozitul:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # SAU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Creați și activați un mediu virtual Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Pe Windows: venv\Scripts\activate
   ```

3. **Instalați dependențele:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurați variabilele de mediu:**
   ```bash
   cp .env.example .env
   # Editează .env cu cheile tale API și punctele finale
   ```

### Variabile de mediu necesare

Pentru **Microsoft Foundry** (obligatoriu):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint-ul proiectului Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - numele implementării modelului (ex.: gpt-4.1-mini)

Pentru **Azure AI Search** (Lecția 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint-ul Azure AI Search
- `AZURE_SEARCH_API_KEY` - cheia API Azure AI Search

Autentificare: Executați `az login` înainte de a rula notebook-urile (folosește `AzureCliCredential`).

## Flux de lucru pentru dezvoltare

### Rularea Jupyter Notebooks

Fiecare lecție conține mai multe Jupyter notebooks pentru diferite cadre:

1. **Porniți Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigați către directorul lecției** (ex.: `01-intro-to-ai-agents/code_samples/`)

3. **Deschideți și rulați notebook-urile:**
   - `*-python-agent-framework.ipynb` - Folosind Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Folosind Microsoft Agent Framework (.NET)

### Lucrul cu Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Necesită abonament Azure
- Folosește `FoundryChatClient` pentru Agent Service V2 (agenții vizibili în portalul Foundry)
- Pregătit pentru producție cu observabilitate integrată
- Model fișier: `*-python-agent-framework.ipynb`

## Instrucțiuni de testare

Acesta este un depozit educațional cu cod exemplu, nu cod de producție cu teste automate. Pentru a verifica configurarea și modificările:

### Testare manuală

1. **Testați mediul Python:**
   ```bash
   python --version  # Ar trebui să fie 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testați execuția notebook-ului:**
   ```bash
   # Convertiți notebook-ul în script și rulați-l (testează importurile)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verificați variabilele de mediu:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Rularea notebook-urilor individuale

Deschideți notebook-uri în Jupyter și executați celulele secvențial. Fiecare notebook este autonom și include:
- Declarații de import
- Încărcarea configurației
- Implementări exemplu pentru agenți
- Ieșiri așteptate în celule markdown

### Testare sumară a agenților implementați

Pentru lecțiile unde un agent este implementat ca agent găzduit Microsoft Foundry (01, 04, 05, 16), repo-ul conține cataloage pentru testare sumară sub `tests/` care sunt rulate de workflow-ul `.github/workflows/smoke-test.yml` prin acțiunea [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Acestea sunt o poartă ușoară post-implementare (este agentul accesibil și urmează așteptările de prompt de bază?), completând pipeline-ul de evaluare din Lecțiile 10 și 16. Vezi [tests/README.md](./tests/README.md) pentru maparea catalog-urilor către lecții și agenți. Lecția 17 rulează local cu Foundry Local și nu are endpoint găzduit, deci este validată prin rularea notebook-ului direct.

## Stilul codului

### Convenții Python

- **Versiunea Python**: 3.12+
- **Stilul codului**: Urmați convențiile standard Python PEP 8
- **Notebooks**: Folosiți celule markdown clare pentru a explica conceptele
- **Importuri**: Grupați după bibliotecă standard, terță parte, importuri locale

### Convenții pentru Jupyter Notebook

- Includeți celule markdown descriptive înaintea celulelor de cod
- Adăugați exemple de ieșiri în notebooks ca referință
- Folosiți nume de variabile clare care corespund conceptelor lecției
- Mențineți ordinea liniară a execuției notebook-ului (celula 1 → 2 → 3...)

### Organizarea fișierelor

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Construire și implementare

### Construirea documentației

Acest depozit folosește Markdown pentru documentație:
- Fișiere README.md în fiecare folder de lecție
- README.md principal la rădăcina depozitului
- Sistem automatizat de traducere prin GitHub Actions

### Pipeline CI/CD

Localizat în `.github/workflows/`:

1. **co-op-translator.yml** - traducere automată în peste 50 de limbi
2. **welcome-issue.yml** - întâmpină creatorii de issue-uri noi
3. **welcome-pr.yml** - întâmpină contribuitorii la pull request-uri noi

### Implementare

Acesta este un depozit educațional - fără proces de implementare. Utilizatorii:
1. Fac fork sau clonează depozitul
2. Rulează notebook-urile local sau în GitHub Codespaces
3. Învățare prin modificarea și experimentarea cu exemplele

## Ghid pentru Pull Request-uri

### Înainte de a trimite

1. **Testați modificările:**
   - Rulați complet notebook-urile afectate
   - Verificați că toate celulele se execută fără erori
   - Verificați că ieșirile sunt adecvate

2. **Actualizări documentație:**
   - Actualizați README.md la adăugarea de noi concepte
   - Adăugați comentarii în notebook-uri pentru cod complex
   - Asigurați-vă că celulele markdown explică scopul

3. **Modificări de fișiere:**
   - Evitați comiterea fișierelor `.env` (folosiți `.env.example`)
   - Nu comiteți directoarele `venv/` sau `__pycache__/`
   - Păstrați ieșirile din notebook-uri când demonstrează concepte
   - Îndepărtați fișiere temporare și notebook-uri de backup (`*-backup.ipynb`)

### Format titlu PR

Folosiți titluri descriptive:
- `[Lesson-XX] Adăugați exemplu nou pentru <concept>`
- `[Fix] Corectați greșeală de scriere în README lecția-XX`
- `[Update] Îmbunătățiți exemplul de cod în lecția-XX`
- `[Docs] Actualizați instrucțiunile de configurare`

### Verificări necesare

- Notebook-urile trebuie să ruleze fără erori
- Fișierele README trebuie să fie clare și precise
- Urmați modelele de cod existente în depozit
- Mențineți consistența cu celelalte lecții

## Note suplimentare

### Capcane comune

1. **Neconcordanță versiune Python:**
   - Asigurați utilizarea Python 3.12+
   - Unele pachete pot să nu funcționeze cu versiuni mai vechi
   - Folosiți `python3 -m venv` pentru a specifica explicit versiunea Python

2. **Variabile de mediu:**
   - Creați întotdeauna `.env` din `.env.example`
   - Nu comiteți fișierul `.env` (este în `.gitignore`)
   - Autentificați-vă cu `az login` pentru autentificare fără cheie Entra ID

3. **Conflicte între pachete:**
   - Folosiți un mediu virtual proaspăt
   - Instalați din `requirements.txt` în loc de pachete individuale
   - Unele notebook-uri pot necesita pachete suplimentare menționate în celule markdown

4. **Servicii Azure:**
   - Serviciile Azure AI necesită abonament activ
   - Unele funcționalități sunt specifice regiunii
   - Asigurați-vă că implementarea modelului Azure OpenAI suportă API-ul Responses

### Traseul de învățare

Progres recomandat prin lecții:
1. **00-course-setup** - Începeți de aici pentru configurarea mediului
2. **01-intro-to-ai-agents** - Înțelegeți elementele fundamentale ale agenților AI
3. **02-explore-agentic-frameworks** - Aflați despre diferite cadre
4. **03-agentic-design-patterns** - Modele de design de bază
5. Continuați secvențial prin lecțiile numerotate

### Selecția cadrului

Alegeți cadrul în funcție de obiectivele dvs.:
- **Toate lecțiile**: Microsoft Agent Framework (MAF) cu `FoundryChatClient`
- **Agenții se înregistrează server-side** în Microsoft Foundry Agent Service V2 și sunt vizibili în portalul Foundry

### Obținerea ajutorului

- Alăturați-vă [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Consultați fișierele README ale lecțiilor pentru ghidaj specific
- Verificați README.md principal pentru prezentarea cursului
- Consultați [Course Setup](./00-course-setup/README.md) pentru instrucțiuni detaliate de configurare

### Contribuții

Acesta este un proiect educațional deschis. Sunt binevenite contribuții:
- Îmbunătățirea exemplelor de cod
- Corectarea greșelilor de scriere sau erorilor
- Adăugarea de comentarii care să clarifice
- Sugestii pentru subiecte noi de lecții
- Traduceri în limbi suplimentare

Vezi [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pentru nevoile curente.

## Context specific proiectului

### Suport multilingv

Acest depozit folosește un sistem automatizat de traducere:
- Peste 50 de limbi suportate
- Traduceri în directoarele `/translations/<lang-code>/`
- Workflow GitHub Actions gestionează actualizările traducerilor
- Fișierele sursă sunt în engleză la rădăcina depozitului

### Structura lecției

Fiecare lecție urmează un model consecvent:
1. Miniatură video cu link
2. Conținut scris al lecției (README.md)
3. Exemple de cod în cadre multiple
4. Obiective de învățare și cerințe preliminare
5. Resurse suplimentare de învățare legate

### Nomenclatura exemplelor de cod

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lecția 1, MAF Python
- `14-sequential.ipynb` - Lecția 14, modele avansate MAF
- `16-python-agent-framework.ipynb` - Lecția 16, agent de support clienți în producție
- `17-local-agent-foundry-local.ipynb` - Lecția 17, agent local cu Foundry Local + Qwen

### Directoare speciale

- `translated_images/` - Imagini localizate pentru traduceri
- `images/` - Imagini originale pentru conținut în limba engleză
- `.devcontainer/` - Configurare container dezvoltare VS Code
- `.github/` - Workflow-uri și șabloane GitHub Actions

### Dependențe

Pachete cheie din `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suport protocol Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Servicii Azure AI
- `azure-identity` - Autentificare Azure (AzureCliCredential)
- `azure-search-documents` - Integrare Azure AI Search
- `mcp[cli]` - Suport Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->