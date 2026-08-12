# AGENTS.md

## Prezentare generală a proiectului

Acest depozit conține „Agenți AI pentru începători” - un curs educațional cuprinzător care predă tot ce este necesar pentru a crea agenți AI. Cursul constă din 18 lecții (numerotate 00-18) care acoperă fundamentele, tiparele de design, cadrele de lucru, implementarea în producție, agenții locali/pe dispozitiv și securitatea agenților AI.

**Tehnologii cheie:**
- Python 3.12+
- Jupyter Notebooks pentru învățare interactivă
- Cadre AI: Microsoft Agent Framework (MAF)
- Servicii Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitectură:**
- Structură bazată pe lecții (directoare 00-15+)
- Fiecare lecție conține: documentație README, exemple de cod (Jupyter notebooks) și imagini
- Suport multi-limbaj prin sistem automatizat de traducere
- Un notebook Python per lecție folosind Microsoft Agent Framework

## Comenzi de configurare

### Cerințe preliminare
- Python 3.12 sau versiune mai nouă
- Abonament Azure (pentru Microsoft Foundry)
- Azure CLI instalat și autentificat (`az login`)

### Configurare inițială

1. **Clonează sau fork-ează depozitul:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # SAU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Crează și activează mediul virtual Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Pe Windows: venv\Scripts\activate
   ```

3. **Instalează dependențele:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurează variabilele de mediu:**
   ```bash
   cp .env.example .env
   # Editează .env cu cheile și punctele tale finale API
   ```

### Variabile de mediu necesare

Pentru **Microsoft Foundry** (Necesare):
- `AZURE_AI_PROJECT_ENDPOINT` - punctul final al proiectului Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - numele implementării modelului (ex. gpt-5-mini)

Pentru **Azure AI Search** (Lecția 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - punctul final Azure AI Search
- `AZURE_SEARCH_API_KEY` - cheie API Azure AI Search

Autentificare: Rulați `az login` înainte de a rula notebook-urile (folosește `AzureCliCredential`).

## Flux de lucru pentru dezvoltare

### Rularea Jupyter Notebooks

Fiecare lecție conține mai multe notebook-uri Jupyter pentru cadre diferite:

1. **Pornește Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navighează către directorul unei lecții** (ex: `01-intro-to-ai-agents/code_samples/`)

3. **Deschide și rulează notebook-urile:**
   - `*-python-agent-framework.ipynb` - Folosind Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Folosind Microsoft Agent Framework (.NET)

### Lucrul cu Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Necesită abonament Azure
- Folosește `FoundryChatClient` pentru Agent Service V2 (agenți vizibili în portalul Foundry)
- Pregătit pentru producție cu observabilitate integrată
- Model fișier: `*-python-agent-framework.ipynb`

## Instrucțiuni de testare

Acesta este un depozit educațional cu cod exemplu, nu cod de producție cu teste automatizate. Pentru a verifica configurarea și modificările:

### Testare manuală

1. **Testează mediul Python:**
   ```bash
   python --version  # Ar trebui să fie 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testează execuția notebook-ului:**
   ```bash
   # Convertiți caietul în script și rulați-l (testează importurile)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifică variabilele de mediu:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Rularea notebook-urilor individuale

Deschide notebook-urile în Jupyter și execută celulele sequential. Fiecare notebook este autonom și include:
- Declarații de import
- Încărcarea configurației
- Implementări exemplu de agenți
- Rezultate așteptate în celulele markdown

### Testare de bază a agenților implementați

Pentru lecțiile în care un agent este implementat ca agent găzduit Microsoft Foundry (01, 04, 05, 16), depozitul oferă cataloage de testare de bază sub `tests/` ce sunt rulate de workflow-ul `.github/workflows/smoke-test.yml` prin acțiunea [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Acestea sunt un filtru ușor după implementare (este agentul accesibil și respectă așteptările de prompt de bază?), completând pipeline-ul de evaluare din Lecțiile 10 și 16. Vezi [tests/README.md](./tests/README.md) pentru maparea catalog-urilor către lecții și agenți. Lecția 17 rulează local cu Foundry Local și nu are punct găzduit, așa că este validată prin rularea notebook-ului direct.

## Stil de cod

### Convenții Python

- **Versiunea Python**: 3.12+
- **Stil de cod**: Urmează convențiile standard PEP 8 pentru Python
- **Notebook-uri**: Folosește celule markdown clare pentru explicarea conceptelor
- **Importuri**: Grupează importurile în standard library, terțe părți, locale

### Convenții pentru Jupyter Notebook

- Include celule markdown descriptive înaintea celulelor de cod
- Adaugă exemple de ieșiri în notebook-uri pentru referință
- Folosește nume clare de variabile care reflectă conceptele lecției
- Păstrează execuția liniară a notebook-urilor (celula 1 → 2 → 3...)

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

Situat în `.github/workflows/`:

1. **co-op-translator.yml** - Traducere automată în peste 50 de limbi
2. **welcome-issue.yml** - Primirea creatorilor de issue-uri noi
3. **welcome-pr.yml** - Primirea contributorilor la pull request-uri

### Implementare

Acesta este un depozit educațional - nu există proces de implementare. Utilizatorii:
1. Fac fork sau clonează depozitul
2. Rulează notebook-urile local sau în GitHub Codespaces
3. Învață prin modificarea și experimentarea cu exemplele

## Ghid pentru Pull Request

### Înainte de a trimite

1. **Testează modificările:**
   - Rulează complet notebook-urile afectate
   - Verifică că toate celulele se execută fără erori
   - Verifică dacă ieșirile sunt adecvate

2. **Actualizări în documentație:**
   - Actualizează README.md dacă adaugi concepte noi
   - Adaugă comentarii în notebook-uri pentru cod complex
   - Asigură-te că celulele markdown explică scopul

3. **Modificări în fișiere:**
   - Evită să comiți fișiere `.env` (folosește `.env.example`)
   - Nu comite directoarele `venv/` sau `__pycache__/`
   - Păstrează ieșirile notebook-urilor când demonstrează concepte
   - Elimină fișierele temporare și backup notebook-uri (`*-backup.ipynb`)

### Format titlu PR

Folosește titluri descriptive:
- `[Lesson-XX] Adaugă exemplu nou pentru <concept>`
- `[Fix] Corectează greșeală în README lecția-XX`
- `[Update] Îmbunătățește exemplul de cod în lecția-XX`
- `[Docs] Actualizează instrucțiunile de setup`

### Verificări necesare

- Notebook-urile trebuie să ruleze fără erori
- Fișierele README trebuie să fie clare și corecte
- Urmărește modelele de cod existente în depozit
- Menține consistența cu celelalte lecții

## Note suplimentare

### Capcane comune

1. **Incompatibilitate versiune Python:**
   - Asigură-te că folosești Python 3.12+
   - Unele pachete pot să nu funcționeze pe versiuni mai vechi
   - Folosește `python3 -m venv` pentru a specifica explicit versiunea Python

2. **Variabile de mediu:**
   - Creează întotdeauna `.env` din `.env.example`
   - Nu commit-ui fișierul `.env` (este în `.gitignore`)
   - Autentificare fără cheie cu `az login` pentru Entra ID

3. **Conflicte de pachete:**
   - Folosește un mediu virtual curat
   - Instalează din `requirements.txt` în loc de pachete individuale
   - Unele notebook-uri pot necesita pachete suplimentare menționate în celulele markdown

4. **Servicii Azure:**
   - Serviciile Azure AI necesită abonament activ
   - Unele funcționalități sunt specifice regiunii
   - Asigură-te că implementarea modelului Azure OpenAI suportă Responses API

### Calea de învățare

Progres recomandat prin lecții:
1. **00-course-setup** - Începe de aici pentru configurarea mediului
2. **01-intro-to-ai-agents** - Înțelegerea fundamentelor agenților AI
3. **02-explore-agentic-frameworks** - Află despre cadre diferite
4. **03-agentic-design-patterns** - Tipare de design de bază
5. Continuă prin lecțiile numerotate în ordine

### Alegerea cadrului

Alege cadrul în funcție de obiectivele tale:
- **Toate lecțiile**: Microsoft Agent Framework (MAF) cu `FoundryChatClient`
- **Agenții se înregistrează server-side** în Microsoft Foundry Agent Service V2 și sunt vizibili în portalul Foundry

### Obținerea ajutorului

- Alătură-te comunității [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Consultă fișierele README ale lecțiilor pentru ghiduri specifice
- Verifică [README.md](./README.md) principal pentru prezentarea cursului
- Consultă [Configurare curs](./00-course-setup/README.md) pentru instrucțiuni detaliate

### Contribuții

Acesta este un proiect educațional deschis. Contribuțiile sunt binevenite:
- Îmbunătățirea exemplelor de cod
- Corectarea greșelilor de tastare sau erori
- Adăugarea de comentarii explicative
- Sugestii pentru noi subiecte de lecții
- Traduceri în limbi suplimentare

Vezi [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pentru necesitățile curente.

## Context specific proiectului

### Suport multi-limbaj

Acest depozit folosește un sistem automatizat de traducere:
- Suport pentru peste 50 de limbi
- Traduceri în directoarele `/translations/<cod-limba>/`
- Fluxul de lucru GitHub Actions gestionează actualizările traducerilor
- Fișierele sursă sunt în engleză la rădăcina depozitului

### Structura lecțiilor

Fiecare lecție urmează un tipar consecvent:
1. Miniatura video cu link
2. Conținut scris al lecției (README.md)
3. Exemple de cod în mai multe cadre
4. Obiective de învățare și cerințe preliminare
5. Resurse suplimentare de învățare legate

### Denumirea exemplelor de cod

Format: `<numar-lectie>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lecția 1, MAF Python
- `14-sequential.ipynb` - Lecția 14, tipare avansate MAF
- `16-python-agent-framework.ipynb` - Lecția 16, agent suport clienți în producție
- `17-local-agent-foundry-local.ipynb` - Lecția 17, agent local cu Foundry Local + Qwen

### Directoare speciale

- `translated_images/` - Imagini localizate pentru traduceri
- `images/` - Imagini originale pentru conținut în engleză
- `.devcontainer/` - Configurare container dezvoltare VS Code
- `.github/` - Workflow-uri și șabloane GitHub Actions

### Dependențe

Pachete cheie din `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suport protocol Agent- către-Agent
- `azure-ai-inference`, `azure-ai-projects` - Servicii Azure AI
- `azure-identity` - Autentificare Azure (AzureCliCredential)
- `azure-search-documents` - Integrare Azure AI Search
- `mcp[cli]` - Suport Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->