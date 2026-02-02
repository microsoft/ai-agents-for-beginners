# AGENTS.md

## Prezentare generală a proiectului

Acest depozit conține "AI Agents for Beginners" - un curs educațional cuprinzător care predă tot ce este necesar pentru a construi agenți AI. Cursul constă în peste 15 lecții care acoperă fundamentele, modelele de design, cadrele și implementarea în producție a agenților AI.

**Tehnologii cheie:**
- Python 3.12+
- Jupyter Notebooks pentru învățare interactivă
- Cadre AI: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Servicii Azure AI: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (disponibilă versiunea gratuită)

**Arhitectură:**
- Structură bazată pe lecții (directoare 00-15+)
- Fiecare lecție conține: documentație README, exemple de cod (notebook-uri Jupyter) și imagini
- Suport multilingv prin sistem de traducere automatizat
- Opțiuni multiple de cadre pentru fiecare lecție (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Comenzi de configurare

### Cerințe preliminare
- Python 3.12 sau mai recent
- Cont GitHub (pentru GitHub Models - versiunea gratuită)
- Abonament Azure (opțional, pentru serviciile Azure AI)

### Configurare inițială

1. **Clonează sau fork-uiește depozitul:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Creează și activează un mediu virtual Python:**
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

### Variabile de mediu necesare

Pentru **GitHub Models (Gratuit)**:
- `GITHUB_TOKEN` - Token de acces personal de la GitHub

Pentru **Servicii Azure AI** (opțional):
- `PROJECT_ENDPOINT` - Endpoint-ul proiectului Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - Cheia API Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL-ul endpoint-ului Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Numele implementării pentru modelul de chat
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Numele implementării pentru embeddings
- Configurații suplimentare Azure, așa cum sunt prezentate în `.env.example`

## Flux de lucru pentru dezvoltare

### Rularea notebook-urilor Jupyter

Fiecare lecție conține mai multe notebook-uri Jupyter pentru diferite cadre:

1. **Pornește Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navighează la un director de lecție** (de exemplu, `01-intro-to-ai-agents/code_samples/`)

3. **Deschide și rulează notebook-urile:**
   - `*-semantic-kernel.ipynb` - Utilizând cadrul Semantic Kernel
   - `*-autogen.ipynb` - Utilizând cadrul AutoGen
   - `*-python-agent-framework.ipynb` - Utilizând Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Utilizând Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Utilizând Azure AI Agent Service

### Lucrul cu diferite cadre

**Semantic Kernel + GitHub Models:**
- Disponibil gratuit cu cont GitHub
- Ideal pentru învățare și experimentare
- Model de fișier: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Disponibil gratuit cu cont GitHub
- Capacități de orchestrare multi-agent
- Model de fișier: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Cel mai nou cadru de la Microsoft
- Disponibil în Python și .NET
- Model de fișier: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Necesită abonament Azure
- Funcționalități pregătite pentru producție
- Model de fișier: `*-azureaiagent.ipynb`

## Instrucțiuni de testare

Acesta este un depozit educațional cu cod de exemplu, nu cod de producție cu teste automate. Pentru a verifica configurarea și modificările:

### Testare manuală

1. **Testează mediul Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Testează execuția notebook-urilor:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifică variabilele de mediu:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Rularea notebook-urilor individuale

Deschide notebook-urile în Jupyter și execută celulele în ordine. Fiecare notebook este independent și include:
- Declarații de import
- Încărcarea configurației
- Implementări de agenți exemplu
- Rezultate așteptate în celulele markdown

## Stilul codului

### Convenții Python

- **Versiune Python**: 3.12+
- **Stilul codului**: Urmează convențiile standard PEP 8
- **Notebook-uri**: Folosește celule markdown clare pentru a explica conceptele
- **Importuri**: Grupate după bibliotecă standard, terță parte, importuri locale

### Convenții pentru notebook-uri Jupyter

- Include celule markdown descriptive înainte de celulele de cod
- Adaugă exemple de rezultate în notebook-uri pentru referință
- Folosește nume de variabile clare care se potrivesc cu conceptele lecției
- Menține ordinea de execuție a notebook-urilor liniară (celula 1 → 2 → 3...)

### Organizarea fișierelor

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```

## Construire și implementare

### Construirea documentației

Acest depozit folosește Markdown pentru documentație:
- Fișiere README.md în fiecare folder de lecție
- README.md principal la rădăcina depozitului
- Sistem de traducere automatizat prin GitHub Actions

### Pipeline CI/CD

Localizat în `.github/workflows/`:

1. **co-op-translator.yml** - Traducere automată în peste 50 de limbi
2. **welcome-issue.yml** - Mesaj de bun venit pentru creatorii de probleme noi
3. **welcome-pr.yml** - Mesaj de bun venit pentru contribuitorii de pull request-uri noi

### Implementare

Acesta este un depozit educațional - nu există proces de implementare. Utilizatorii:
1. Fork-uiesc sau clonează depozitul
2. Rulează notebook-urile local sau în GitHub Codespaces
3. Învață modificând și experimentând cu exemplele

## Ghid pentru pull request-uri

### Înainte de a trimite

1. **Testează modificările tale:**
   - Rulează complet notebook-urile afectate
   - Verifică ca toate celulele să se execute fără erori
   - Asigură-te că rezultatele sunt adecvate

2. **Actualizări ale documentației:**
   - Actualizează README.md dacă adaugi concepte noi
   - Adaugă comentarii în notebook-uri pentru cod complex
   - Asigură-te că celulele markdown explică scopul

3. **Modificări ale fișierelor:**
   - Evită să comiți fișiere `.env` (folosește `.env.example`)
   - Nu comite directoarele `venv/` sau `__pycache__/`
   - Păstrează rezultatele notebook-urilor când demonstrează concepte
   - Elimină fișierele temporare și backup-urile notebook-urilor (`*-backup.ipynb`)

### Formatul titlului PR

Folosește titluri descriptive:
- `[Lesson-XX] Adaugă exemplu nou pentru <concept>`
- `[Fix] Corectează o greșeală în README-ul lecției XX`
- `[Update] Îmbunătățește exemplul de cod în lecția XX`
- `[Docs] Actualizează instrucțiunile de configurare`

### Verificări necesare

- Notebook-urile trebuie să se execute fără erori
- Fișierele README trebuie să fie clare și corecte
- Urmează modelele de cod existente în depozit
- Menține consistența cu celelalte lecții

## Note suplimentare

### Probleme frecvente

1. **Nepotrivire versiune Python:**
   - Asigură-te că folosești Python 3.12+
   - Unele pachete pot să nu funcționeze cu versiuni mai vechi
   - Folosește `python3 -m venv` pentru a specifica explicit versiunea Python

2. **Variabile de mediu:**
   - Creează întotdeauna `.env` din `.env.example`
   - Nu comite fișierul `.env` (este în `.gitignore`)
   - Token-ul GitHub necesită permisiuni adecvate

3. **Conflicte de pachete:**
   - Folosește un mediu virtual nou
   - Instalează din `requirements.txt` în loc de pachete individuale
   - Unele notebook-uri pot necesita pachete suplimentare menționate în celulele markdown

4. **Servicii Azure:**
   - Serviciile Azure AI necesită abonament activ
   - Unele funcționalități sunt specifice regiunii
   - Limitările versiunii gratuite se aplică pentru GitHub Models

### Parcurs de învățare

Progres recomandat prin lecții:
1. **00-course-setup** - Începe aici pentru configurarea mediului
2. **01-intro-to-ai-agents** - Înțelege fundamentele agenților AI
3. **02-explore-agentic-frameworks** - Învață despre diferite cadre
4. **03-agentic-design-patterns** - Modele de design de bază
5. Continuă prin lecțiile numerotate în ordine

### Selectarea cadrului

Alege cadrul în funcție de obiectivele tale:
- **Învățare/Prototipare**: Semantic Kernel + GitHub Models (gratuit)
- **Sisteme multi-agent**: AutoGen
- **Funcționalități noi**: Microsoft Agent Framework (MAF)
- **Implementare în producție**: Azure AI Agent Service

### Obținerea ajutorului

- Alătură-te [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Consultă fișierele README ale lecțiilor pentru ghid specific
- Verifică [README.md principal](./README.md) pentru prezentarea cursului
- Consultă [Course Setup](./00-course-setup/README.md) pentru instrucțiuni detaliate de configurare

### Contribuții

Acesta este un proiect educațional deschis. Contribuțiile sunt binevenite:
- Îmbunătățirea exemplelor de cod
- Corectarea greșelilor sau erorilor
- Adăugarea de comentarii explicative
- Sugestii pentru noi subiecte de lecții
- Traducerea în limbi suplimentare

Vezi [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pentru nevoile actuale.

## Context specific proiectului

### Suport multilingv

Acest depozit folosește un sistem de traducere automatizat:
- Suport pentru peste 50 de limbi
- Traduceri în directoarele `/translations/<lang-code>/`
- Workflow-ul GitHub Actions gestionează actualizările traducerilor
- Fișierele sursă sunt în engleză la rădăcina depozitului

### Structura lecțiilor

Fiecare lecție urmează un model consistent:
1. Miniatură video cu link
2. Conținut scris al lecției (README.md)
3. Exemple de cod în mai multe cadre
4. Obiective de învățare și cerințe preliminare
5. Resurse suplimentare de învățare legate

### Denumirea exemplelor de cod

Format: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Lecția 4, Semantic Kernel
- `07-autogen.ipynb` - Lecția 7, AutoGen
- `14-python-agent-framework.ipynb` - Lecția 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Lecția 14, MAF .NET

### Directoare speciale

- `translated_images/` - Imagini localizate pentru traduceri
- `images/` - Imagini originale pentru conținutul în engleză
- `.devcontainer/` - Configurație container de dezvoltare VS Code
- `.github/` - Workflow-uri și șabloane GitHub Actions

### Dependențe

Pachete cheie din `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - Cadru AutoGen
- `semantic-kernel` - Cadru Semantic Kernel
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Servicii Azure AI
- `azure-search-documents` - Integrare Azure AI Search
- `chromadb` - Bază de date vectorială pentru exemple RAG
- `chainlit` - Cadru UI pentru chat
- `browser_use` - Automatizare browser pentru agenți
- `mcp[cli]` - Suport pentru Model Context Protocol
- `mem0ai` - Gestionarea memoriei pentru agenți

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.