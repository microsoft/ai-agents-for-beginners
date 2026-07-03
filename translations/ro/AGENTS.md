# AGENTS.md

## Prezentare generală a proiectului

Acest depozit conține "Agenți AI pentru Începători" - un curs educațional cuprinzător care învață tot ce este necesar pentru a construi Agenți AI. Cursul este alcătuit din 18 lecții care acoperă fundamentele, tiparele de design, cadrele și implementarea în producție a agenților AI.

**Tehnologii cheie:**
- Python 3.12+
- Jupyter Notebooks pentru învățare interactivă
- Cadre AI: Microsoft Agent Framework (MAF)
- Servicii AI Azure: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arhitectură:**
- Structură bazată pe lecții (directoare 00-15+)
- Fiecare lecție conține: documentație README, exemple de cod (notebook-uri Jupyter) și imagini
- Suport multilingv prin sistem automatizat de traducere
- Un notebook Python per lecție folosind Microsoft Agent Framework

## Comenzi de configurare

### Cerințe prealabile
- Python 3.12 sau mai mare
- Abonament Azure (pentru Azure AI Foundry)
- Azure CLI instalat și autentificat (`az login`)

### Configurare inițială

1. **Clonați sau faceți fork la depozit:**
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
   # Editează .env cu cheile tale API și endpoint-urile
   ```

### Variabile de mediu necesare

Pentru **Azure AI Foundry** (Necesare):
- `AZURE_AI_PROJECT_ENDPOINT` - punctul final al proiectului Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - numele implementării modelului (de exemplu, gpt-4o)

Pentru **Azure AI Search** (Lecția 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - punctul final Azure AI Search
- `AZURE_SEARCH_API_KEY` - cheia API Azure AI Search

Autentificare: Rulați `az login` înainte de a rula notebook-urile (folosește `AzureCliCredential`).

## Flux de lucru pentru dezvoltare

### Rularea Jupyter Notebooks

Fiecare lecție conține mai multe notebook-uri Jupyter pentru cadre diferite:

1. **Porniți Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigați la un director de lecție** (de ex., `01-intro-to-ai-agents/code_samples/`)

3. **Deschideți și rulați notebook-urile:**
   - `*-python-agent-framework.ipynb` - Folosind Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Folosind Microsoft Agent Framework (.NET)

### Lucrul cu Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Necesită abonament Azure
- Folosește `AzureAIProjectAgentProvider` pentru Agent Service V2 (agenții sunt vizibili în portalul Foundry)
- Pregătit pentru producție cu observabilitate încorporată
- Model fișier: `*-python-agent-framework.ipynb`

## Instrucțiuni de testare

Acesta este un depozit educațional cu cod exemple, nu cod de producție cu teste automate. Pentru a verifica configurarea și modificările:

### Testare manuală

1. **Testați mediul Python:**
   ```bash
   python --version  # Ar trebui să fie 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testați execuția notebook-ului:**
   ```bash
   # Convertiți caietul în script și rulați-l (testează importurile)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verificați variabilele de mediu:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Rularea individuală a notebook-urilor

Deschideți notebook-urile în Jupyter și executați celulele în ordine. Fiecare notebook este auto-conținut și include:
- Instructiuni de import
- Încărcarea configurației
- Exemple de implementări ale agenților
- Rezultate așteptate în celule markdown

## Stilul de cod

### Convenții Python

- **Versiune Python**: 3.12+
- **Stil cod**: Urmați convențiile standard Python PEP 8
- **Notebook-uri**: Folosiți celule markdown clare pentru explicarea conceptelor
- **Importuri**: Grupează pe biblioteci standard, terțe și importuri locale

### Convenții Jupyter Notebook

- Includeți celule markdown descriptive înaintea celor de cod
- Adăugați exemple de output în notebook-uri pentru referință
- Folosiți nume clare de variabile care să corespundă conceptelor lecției
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
- Fișiere README.md în fiecare dosar de lecție
- README.md principal la rădăcina depozitului
- Sistem automatizat de traducere prin GitHub Actions

### Pipeline CI/CD

Localizat în `.github/workflows/`:

1. **co-op-translator.yml** - Traducere automată în peste 50 de limbi
2. **welcome-issue.yml** - Salută noii creatori de issue-uri
3. **welcome-pr.yml** - Salută noii contributori la pull request-uri

### Implementare

Acesta este un depozit educațional - fără proces de implementare. Utilizatorii:
1. Fac fork sau clonează depozitul
2. Rulează notebook-urile local sau în GitHub Codespaces
3. Învăță prin modificarea și experimentarea cu exemplele

## Ghid pentru Pull Request-uri

### Înainte de trimitere

1. **Testează modificările:**
   - Rulează complet notebook-urile afectate
   - Verifică ca toate celulele să se execute fără erori
   - Confirmă că rezultatele sunt corecte

2. **Actualizări documentație:**
   - Actualizează README.md dacă sunt adăugate concepte noi
   - Adaugă comentarii în notebook-uri pentru cod complex
   - Asigură-te că celulele markdown explică scopul

3. **Modificări fișiere:**
   - Evită să comiți fișiere `.env` (folosește `.env.example`)
   - Nu comite directoarele `venv/` sau `__pycache__/`
   - Păstrează output-urile notebook-urilor când demonstrează concepte
   - Elimină fișiere temporare și backup-uri de notebook-uri (`*-backup.ipynb`)

### Format titlu PR

Folosește titluri descriptive:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Verificări necesare

- Notebook-urile trebuie să se execute fără erori
- Fișierele README să fie clare și corecte
- Urmează modelele de cod existente în depozit
- Menține consistența cu celelalte lecții

## Note adiționale

### Probleme comune

1. **Incompatibilitate versiune Python:**
   - Asigură-te că folosești Python 3.12+
   - Unele pachete pot să nu funcționeze cu versiuni mai vechi
   - Folosește `python3 -m venv` pentru a specifica versiunea Python explicit

2. **Variabile de mediu:**
   - Creează întotdeauna `.env` din `.env.example`
   - Nu comite fișierul `.env` (este în `.gitignore`)
   - Token-ul GitHub necesită permisiuni adecvate

3. **Conflicte de pachete:**
   - Folosește un mediu virtual nou
   - Instalează din `requirements.txt` în loc de pachete individuale
   - Unele notebook-uri pot necesita pachete suplimentare menționate în celulele lor markdown

4. **Servicii Azure:**
   - Serviciile Azure AI necesită abonament activ
   - Unele funcții pot fi specifice regiunii
   - Limitările nivelului gratuit se aplică pentru modelele GitHub

### Cale de învățare

Progres recomandat prin lecții:
1. **00-course-setup** - Pornește de aici pentru configurarea mediului
2. **01-intro-to-ai-agents** - Înțelege fundamentele agenților AI
3. **02-explore-agentic-frameworks** - Află despre cadre diferite
4. **03-agentic-design-patterns** - Tipare esențiale de design
5. Continuă cu lecțiile numerotate în ordine

### Alegerea cadrului

Alege cadrul în funcție de obiective:
- **Toate lecțiile**: Microsoft Agent Framework (MAF) cu `AzureAIProjectAgentProvider`
- **Agenții se înregistrează pe server** în Azure AI Foundry Agent Service V2 și sunt vizibili în portalul Foundry

### Obținerea ajutorului

- Alătură-te la [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Consultă fișierele README ale lecțiilor pentru ghidare specifică
- Verifică [README.md](./README.md) principal pentru prezentare generală curs
- Consultă [Course Setup](./00-course-setup/README.md) pentru instrucțiuni detaliate

### Contribuții

Acesta este un proiect educațional deschis. Contribuțiile sunt binevenite:
- Îmbunătățește exemplele de cod
- Corectează greșeli sau erori
- Adaugă comentarii explicative
- Sugerează subiecte noi de lecții
- Tradu în limbi suplimentare

Vezi [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pentru nevoi curente.

## Context specific proiectului

### Suport multilingv

Acest depozit folosește un sistem automatizat de traducere:
- Suportă peste 50 de limbi
- Traducerile se află în directoarele `/translations/<lang-code>/`
- Fluxul de lucru GitHub Actions gestionează actualizările traducerilor
- Fișierele sursă sunt în engleză la rădăcina depozitului

### Structura lecțiilor

Fiecare lecție urmează un tipar consistent:
1. Miniatură video cu link
2. Conținut scris al lecției (README.md)
3. Exemple de cod în cadre multiple
4. Obiective de învățare și prerechizite
5. Resurse suplimentare legate

### Nomenclatura exemplelor de cod

Format: `<număr-lecție>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lecția 1, MAF Python
- `14-sequential.ipynb` - Lecția 14, tipare avansate MAF

### Directoare speciale

- `translated_images/` - Imagini localizate pentru traduceri
- `images/` - Imaginile originale pentru conținutul în engleză
- `.devcontainer/` - Configurare container dezvoltare VS Code
- `.github/` - Fluxuri GitHub Actions și șabloane

### Dependențe

Pachete cheie din `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - suport protocol Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - servicii AI Azure
- `azure-identity` - autentificare Azure (AzureCliCredential)
- `azure-search-documents` - integrare Azure AI Search
- `mcp[cli]` - suport Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->