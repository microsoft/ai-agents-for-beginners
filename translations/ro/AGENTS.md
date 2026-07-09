# AGENTS.md

## Prezentare generală a proiectului

Acest depozit conține „AI Agents for Beginners” - un curs educațional cuprinzător care predă tot ce este necesar pentru a construi agenți AI. Cursul constă în 18 lecții care acoperă fundamentele, modelele de design, cadrele de lucru și implementarea în producție a agenților AI.

**Tehnologii cheie:**
- Python 3.12+
- Jupyter Notebooks pentru învățare interactivă
- Cadre AI: Microsoft Agent Framework (MAF)
- Servicii Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitectură:**
- Structură bazată pe lecții (directoare 00-15+)
- Fiecare lecție conține: documentație README, exemple de cod (notebooks Jupyter) și imagini
- Suport multilingv prin sistem automatizat de traducere
- Un notebook Python per lecție folosind Microsoft Agent Framework

## Comenzi de configurare

### Cerințe preliminare
- Python 3.12 sau versiune superioară
- Abonament Azure (pentru Microsoft Foundry)
- Azure CLI instalat și autentificat (`az login`)

### Configurare inițială

1. **Clonați sau faceți fork la depozit:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # SAU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Creați și activați mediul virtual Python:**
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

Pentru **Microsoft Foundry** (Obligatoriu):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint-ul proiectului Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - numele implementării modelului (ex: gpt-4o)

Pentru **Azure AI Search** (Lecția 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - cheie API Azure AI Search

Autentificare: Rulați `az login` înainte de a executa notebook-urile (folosește `AzureCliCredential`).

## Flux de dezvoltare

### Rularea Jupyter Notebooks

Fiecare lecție conține mai multe notebook-uri Jupyter pentru cadre diferite:

1. **Porniți Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigați la un director de lecție** (ex: `01-intro-to-ai-agents/code_samples/`)

3. **Deschideți și rulați notebook-urile:**
   - `*-python-agent-framework.ipynb` - Folosind Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Folosind Microsoft Agent Framework (.NET)

### Lucrul cu Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Necesită abonament Azure
- Folosește `FoundryChatClient` pentru Agent Service V2 (agenți vizibili în portalul Foundry)
- Pregătit pentru producție cu monitorizare integrată
- Tipar fișier: `*-python-agent-framework.ipynb`

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
   # Convertește caietul în script și rulează (testează importurile)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verificați variabilele de mediu:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Rularea notebook-urilor individuale

Deschideți notebook-urile în Jupyter și executați celulele în ordine. Fiecare notebook este auto-conținut și include:
- Instrucțiuni de import
- Încărcarea configurației
- Implementări exemplu de agenți
- Ieșiri așteptate în celulele markdown

## Stil de cod

### Convenții Python

- **Versiune Python**: 3.12+
- **Stil cod**: Urmați convențiile standard Python PEP 8
- **Notebooks**: Folosiți celule markdown clare pentru a explica conceptele
- **Importuri**: Grupați după standard library, terți, importuri locale

### Convenții Jupyter Notebook

- Include celule markdown descriptive înaintea celulelor de cod
- Adăugați exemple de ieșire în notebook-uri pentru referință
- Folosiți nume clare de variabile care corespund conceptelor lecției
- Păstrați ordinea de execuție liniară a notebook-urilor (celula 1 → 2 → 3...)

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

### Crearea documentației

Acest depozit folosește Markdown pentru documentație:
- Fișiere README.md în fiecare folder de lecție
- README.md principal în rădăcina depozitului
- Sistem automatizat de traducere prin GitHub Actions

### Pipelină CI/CD

Situată în `.github/workflows/`:

1. **co-op-translator.yml** - Traducere automată în peste 50 limbi
2. **welcome-issue.yml** - Mesaj de întâmpinare pentru creatori de issue-uri noi
3. **welcome-pr.yml** - Mesaj de întâmpinare pentru contributori noi de pull request-uri

### Implementare

Acesta este un depozit educațional - fără proces de implementare. Utilizatorii:
1. Fac fork sau clonează depozitul
2. Rulează notebook-uri local sau în GitHub Codespaces
3. Învață modificând și experimentând cu exemplele

## Ghid pentru Pull Requests

### Înainte de a trimite

1. **Testați modificările:**
   - Rulați complet notebook-urile afectate
   - Verificați că toate celulele se execută fără erori
   - Verificați că ieșirile sunt corespunzătoare

2. **Actualizări de documentație:**
   - Actualizați README.md dacă adăugați concepte noi
   - Adăugați comentarii în notebook-uri pentru cod complex
   - Asigurați-vă că celulele markdown explică scopul

3. **Modificări de fișiere:**
   - Evitați comiterea fișierelor `.env` (folosiți `.env.example`)
   - Nu comiteți directoarele `venv/` sau `__pycache__/`
   - Păstrați ieșirile notebook-urilor când demonstrează conceptele
   - Eliminați fișiere temporare și notebook-uri de backup (`*-backup.ipynb`)

### Format titlu PR

Folosiți titluri descriptive:
- `[Lesson-XX] Adaugă exemplu nou pentru <concept>`
- `[Fix] Corectează greșeală tipar în lecția-XX README`
- `[Update] Îmbunătățește exemplul de cod în lecția-XX`
- `[Docs] Actualizează instrucțiunile de configurare`

### Verificări obligatorii

- Notebook-urile trebuie să se execute fără erori
- Fișierele README trebuie să fie clare și corecte
- Urmați modelele de cod existente în depozit
- Mențineți consistența cu celelalte lecții

## Note suplimentare

### Capcane comune

1. **Nedesincronizare versiune Python:**
   - Asigurați-vă că folosiți Python 3.12+
   - Unele pachete pot să nu funcționeze cu versiuni mai vechi
   - Folosiți `python3 -m venv` pentru a specifica versiunea Python explicit

2. **Variabilele de mediu:**
   - Creați întotdeauna `.env` pornind de la `.env.example`
   - Nu comiteți fișierul `.env` (este inclus în `.gitignore`)
   - Autentificați-vă cu `az login` pentru autentificare Entra ID fără cheie

3. **Conflicte de pachete:**
   - Folosiți un mediu virtual curat
   - Instalați din `requirements.txt` în loc de pachete individuale
   - Unele notebook-uri pot necesita pachete suplimentare menționate în celulele markdown

4. **Servicii Azure:**
   - Serviciile Azure AI necesită abonament activ
   - Unele funcții sunt specifice regiunii
   - Asigurați-vă că implementarea modelului Azure OpenAI suportă API-ul Responses

### Parcurs de învățare

Progresia recomandată prin lecții:
1. **00-course-setup** - Începeți aici pentru configurarea mediului
2. **01-intro-to-ai-agents** - Înțelegeți fundamentele agenților AI
3. **02-explore-agentic-frameworks** - Aflați despre cadre diferite
4. **03-agentic-design-patterns** - Modele de design esențiale
5. Continuați în ordine secvențială prin lecțiile numerotate

### Alegerea cadrului

Alegeți cadrul în funcție de obiectivele dvs.:
- **Toate lecțiile**: Microsoft Agent Framework (MAF) cu `FoundryChatClient`
- **Agenții se înregistrează server-side** în Microsoft Foundry Agent Service V2 și sunt vizibili în portalul Foundry

### Obținerea ajutorului

- Alăturați-vă comunității [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Consultați fișierele README ale lecțiilor pentru ghidare specifică
- Verificați principalul [README.md](./README.md) pentru prezentarea cursului
- Consultați [Course Setup](./00-course-setup/README.md) pentru instrucțiuni detaliate de configurare

### Contribuții

Acesta este un proiect educațional deschis. Contribuțiile sunt binevenite:
- Îmbunătățirea exemplelor de cod
- Corectarea greșelilor de tipar sau erorilor
- Adăugarea de comentarii explicative
- Sugestii pentru subiecte noi de lecții
- Traduceri în limbi suplimentare

Consultați [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pentru nevoile curente.

## Context specific proiectului

### Suport multilingv

Acest depozit folosește un sistem automatizat de traducere:
- Suport pentru peste 50 limbi
- Traduceri în directoarele `/translations/<lang-code>/`
- Workflow GitHub Actions gestionează actualizările traducerilor
- Fișierele sursă sunt în engleză în rădăcina depozitului

### Structura lecțiilor

Fiecare lecție urmează un tipar consistent:
1. Miniatură video cu link
2. Conținut scris al lecției (README.md)
3. Exemple de cod în cadre multiple
4. Obiective de învățare și cerințe preliminare
5. Resurse suplimentare legate

### Denumirea exemplelor de cod

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lecția 1, MAF Python
- `14-sequential.ipynb` - Lecția 14, modele MAF avansate

### Directoare speciale

- `translated_images/` - Imagini localizate pentru traduceri
- `images/` - Imagini originale pentru conținut în engleză
- `.devcontainer/` - Configurare container dezvoltare VS Code
- `.github/` - Workflow-uri și template-uri GitHub Actions

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