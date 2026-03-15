# Configurare Curs

## Introducere

Această lecție va acoperi cum să rulezi exemplele de cod din acest curs.

## Alătură-te Altora care Învăță și Primește Ajutor

Înainte să începi clonarea repo-ului tău, alătură-te canalului [AI Agents For Beginners Discord](https://aka.ms/ai-agents/discord) pentru a primi ajutor cu configurarea, orice întrebări legate de curs sau pentru a te conecta cu alți cursanți.

## Clonează sau Fă Fork la acest Repo

Pentru a începe, te rugăm să clonezi sau să faci fork la Repositorul GitHub. Astfel vei avea propria versiune a materialului cursului pentru a putea rula, testa și modifica codul!

Acest lucru poate fi făcut făcând clic pe link-ul <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a>.

Acum ar trebui să ai propria ta versiune forcată a acestui curs la următorul link:

![Forked Repo](../../../translated_images/ro/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (recomandat pentru workshop / Codespaces)

  > Repositorul complet poate fi mare (~3 GB) când descarci întreaga istorie și toate fișierele. Dacă participi doar la workshop sau ai nevoie doar de câteva directoare din lecții, un shallow clone (sau sparse clone) evită majoritatea descărcării prin trunchierea istoriei și/sau omiterea blob-urilor.

#### Clonare superficială rapidă — istorie minimă, toate fișierele

Înlocuiește `<your-username>` din comenzile de mai jos cu URL-ul fork-ului tău (sau URL-ul upstream dacă preferi).

Pentru a clona doar istoria ultimului commit (descărcare mică):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pentru a clona o ramură specifică:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clonare parțială (sparse) — blob-uri minime + doar directoarele selectate

Aceasta folosește clonare parțială și sparse-checkout (necesită Git 2.25+ și Git modern recomandat cu suport pentru clonare parțială):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Intră în folderul repo-ului:

```bash|powershell
cd ai-agents-for-beginners
```

Apoi specifică ce foldere dorești (exemplul de mai jos arată două foldere):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

După clonare și verificarea fișierelor, dacă ai nevoie doar de fișiere și vrei să eliberezi spațiu (fără istorie git), te rugăm să ștergi meta-datele repository-ului (💀 ireversibil — vei pierde toate funcționalitățile Git: fără commit-uri, pull, push sau acces la istoric).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Folosirea GitHub Codespaces (recomandat pentru a evita descărcările locale mari)

- Creează un nou Codespace pentru acest repo prin intermediul [GitHub UI](https://github.com/codespaces).  

- În terminalul codespace-ului nou creat, rulează una dintre comenzile de clonare superficială/sparse de mai sus pentru a aduce doar directoarele lecțiilor de care ai nevoie în spațiul de lucru Codespace.
- Opțional: după clonare în Codespaces, elimină .git pentru a recâștiga spațiu suplimentar (vezi comenzile de ștergere de mai sus).
- Notă: Dacă preferi să deschizi repo direct în Codespaces (fără clonare suplimentară), fii conștient că Codespaces va construi mediul devcontainer și poate mai provisiona mai mult decât ai nevoie. Clonarea unei copii superficiale într-un Codespace proaspăt îți oferă mai mult control asupra utilizării discului.

#### Sfaturi

- Înlocuiește întotdeauna URL-ul de clonare cu fork-ul tău dacă vrei să editezi/commit-ezi.
- Dacă mai târziu ai nevoie de mai multă istorie sau fișiere, le poți recupera sau ajusta sparse-checkout pentru a include foldere suplimentare.

## Rularea Codului

Acest curs oferă o serie de Jupyter Notebooks pe care le poți rula pentru a avea experiență practică în construirea de Agenți AI.

Exemplele de cod folosesc **Microsoft Agent Framework (MAF)** cu `AzureAIProjectAgentProvider`, care se conectează la **Azure AI Agent Service V2** (API pentru răspunsuri) prin **Microsoft Foundry**.

Toate notebook-urile Python sunt etichetate `*-python-agent-framework.ipynb`.

## Cerințe

- Python 3.12+
  - **NOTĂ**: Dacă nu ai instalat Python3.12, asigură-te că îl instalezi. Apoi creează-ți mediul virtual folosind python3.12 pentru a garanta instalarea versiunilor corecte din fișierul requirements.txt.
  
    > Exemplar

    Creează director pentru venv Python:

    ```bash|powershell
    python -m venv venv
    ```

    Apoi activează mediul venv pentru:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Pentru codurile exemplu care folosesc .NET, asigură-te că ai instalat [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) sau o versiune ulterioară. Apoi verifică versiunea SDK .NET instalată:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Necesită autentificare. Instalează de la [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Abonament Azure** — Pentru acces la Microsoft Foundry și Azure AI Agent Service.
- **Proiect Microsoft Foundry** — Un proiect cu un model implementat (ex. `gpt-4o`). Vezi [Pasul 1](../../../00-course-setup) mai jos.

Am inclus un fișier `requirements.txt` în rădăcina acestui repository care conține toate pachetele Python necesare pentru a rula exemplele de cod.

Le poți instala rulând următoarea comandă în terminalul tău, în rădăcina repository-ului:

```bash|powershell
pip install -r requirements.txt
```

Recomandăm crearea unui mediu virtual Python pentru a evita conflictele și problemele.

## Configurarea VSCode

Asigură-te că folosești versiunea corectă de Python în VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configurarea Microsoft Foundry și Azure AI Agent Service

### Pasul 1: Crearea unui Proiect Microsoft Foundry

Ai nevoie de un **hub** și un **proiect** Azure AI Foundry cu un model implementat pentru a rula notebook-urile.

1. Accesează [ai.azure.com](https://ai.azure.com) și autentifică-te cu contul tău Azure.
2. Creează un **hub** (sau folosește unul existent). Vezi: [Prezentare generală a resurselor hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. În interiorul hub-ului, creează un **proiect**.
4. Implementează un model (ex. `gpt-4o`) din **Models + Endpoints** → **Deploy model**.

### Pasul 2: Obține Endpoint-ul Proiectului și Numele Implementării Modelului

Din proiectul tău în portalul Microsoft Foundry:

- **Project Endpoint** — Mergi la pagina **Overview** și copiază URL-ul endpoint-ului.

![Project Connection String](../../../translated_images/ro/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Mergi la **Models + Endpoints**, selectează modelul implementat și notează **Deployment name** (ex. `gpt-4o`).

### Pasul 3: Autentificare în Azure cu `az login`

Toate notebook-urile folosesc **`AzureCliCredential`** pentru autentificare — nu se gestionează chei API. Aceasta necesită să fii autentificat prin Azure CLI.

1. **Instalează Azure CLI** dacă nu l-ai instalat deja: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Autentifică-te** rulând:

    ```bash|powershell
    az login
    ```

    Sau dacă te afli într-un mediu remote/Codespace fără browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Selectează abonamentul tău** dacă ți se cere — alege cel care conține proiectul Foundry.

4. **Verifică** dacă ești conectat:

    ```bash|powershell
    az account show
    ```

> **De ce `az login`?** Notebook-urile se autentifică folosind `AzureCliCredential` din pachetul `azure-identity`. Aceasta înseamnă că sesiunea ta Azure CLI furnizează credențialele — fără chei API sau secrete în fișierul tău `.env`. Aceasta este o [practică recomandată de securitate](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Pasul 4: Crearea fișierului tău `.env`

Copiază fișierul exemplu:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Deschide `.env` și completează aceste două valori:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variabilă | Unde o găsești |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → proiectul tău → pagina **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → numele modelului implementat |

Asta este tot pentru majoritatea lecțiilor! Notebook-urile se vor autentifica automat prin sesiunea ta `az login`.

### Pasul 5: Instalarea Dependențelor Python

```bash|powershell
pip install -r requirements.txt
```

Recomandăm să rulezi aceasta în mediul virtual creat anterior.

## Configurare suplimentară pentru Lecția 5 (Agentic RAG)

Lecția 5 folosește **Azure AI Search** pentru generare augmentată prin căutare. Dacă plănuiești să rulezi această lecție, adaugă aceste variabile în fișierul tău `.env`:

| Variabilă | Unde o găsești |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → resursa ta **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Portal Azure → resursa ta **Azure AI Search** → **Settings** → **Keys** → cheia principală admin |

## Configurare suplimentară pentru Lecțiile 6 și 8 (Modele GitHub)

Unele notebook-uri din lecțiile 6 și 8 folosesc **GitHub Models** în loc de Azure AI Foundry. Dacă plănuiești să rulezi acele exemple, adaugă aceste variabile în fișierul tău `.env`:

| Variabilă | Unde o găsești |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Folosește `https://models.inference.ai.azure.com` (valoare implicită) |
| `GITHUB_MODEL_ID` | Numele modelului de utilizat (ex. `gpt-4o-mini`) |

## Configurare suplimentară pentru Lecția 8 (Flux de lucru Bing Grounding)

Notebook-ul de flux condiționat din lecția 8 folosește **Bing grounding** prin Azure AI Foundry. Dacă plănuiești să rulezi acel exemplu, adaugă această variabilă în `.env`:

| Variabilă | Unde o găsești |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal Azure AI Foundry → proiectul tău → **Management** → **Connected resources** → conexiunea ta Bing → copiază ID-ul conexiunii |

## Soluționare Probleme

### Erori de Verificare SSL pe macOS

Dacă ești pe macOS și întâmpini o eroare de genul:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Aceasta este o problemă cunoscută cu Python pe macOS unde certificatele SSL ale sistemului nu sunt automat certificate ca fiind de încredere. Încearcă următoarele soluții în ordine:

**Opțiunea 1: Rulează scriptul Install Certificates al Python (recomandat)**

```bash
# Înlocuiește 3.XX cu versiunea ta instalată de Python (de exemplu, 3.12 sau 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opțiunea 2: Folosește `connection_verify=False` în notebook-ul tău (doar pentru notebook-urile GitHub Models)**

În notebook-ul lecției 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), există deja un workaround comentat. Deblochează `connection_verify=False` când creezi clientul:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Dezactivați verificarea SSL dacă întâmpinați erori de certificat
)
```

> **⚠️ Atenție:** Dezactivarea verificării SSL (`connection_verify=False`) reduce securitatea sărind validarea certificatului. Folosește această opțiune doar temporar în mediile de dezvoltare, niciodată în producție.

**Opțiunea 3: Instalează și folosește `truststore`**

```bash
pip install truststore
```

Apoi adaugă următoarea linie în partea de sus a notebook-ului sau scriptului înainte de orice apeluri de rețea:

```python
import truststore
truststore.inject_into_ssl()
```

## Blocat Undeva?

Dacă întâmpini probleme cu această configurare, intră în <a href="https://discord.gg/kzRShWzttr" target="_blank">comunitatea Azure AI pe Discord</a> sau <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">crează un issue</a>.

## Lecția Următoare

Acum ești gata să rulezi codul pentru acest curs. Spor la învățat mai multe despre lumea Agenților AI!

[Introducere în Agenți AI și Cazuri de Utilizare a Agenților](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, este recomandată traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->