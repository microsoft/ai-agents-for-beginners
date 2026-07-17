# Configurarea cursului

## Introducere

Această lecție va acoperi cum să rulați exemplele de cod din acest curs.

## Alăturați-vă altor cursanți și primiți ajutor

Înainte de a începe să clonați repo-ul, alăturați-vă canalului [AI Agents For Beginners Discord](https://aka.ms/ai-agents/discord) pentru a primi ajutor cu configurarea, orice întrebări legate de curs sau pentru a vă conecta cu alți cursanți.

## Clonați sau faceți fork la acest repo

Pentru început, vă rugăm să clonați sau să faceți fork la Repositorul GitHub. Aceasta vă va crea propria versiune a materialului cursului astfel încât să puteți rula, testa și ajusta codul!

Acest lucru se poate face făcând clic pe linkul <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork la repo</a>

Acum ar trebui să aveți propria versiune fork-uită a acestui curs la linkul următor:

![Forked Repo](../../../translated_images/ro/forked-repo.33f27ca1901baa6a.webp)

### Clonare superficială (recomandat pentru atelier / Codespaces)

  >Repositorio-ul complet poate fi mare (~3 GB) când descărcați istoricul complet și toate fișierele. Dacă participați doar la atelier sau aveți nevoie doar de câteva foldere de lecție, o clonare superficială (sau o clonare sparse) evită majoritatea acelei descărcări prin trunchierea istoricului și/sau sărind peste blob-uri.

#### Clonare superficială rapidă — istoric minimal, toate fișierele

Înlocuiți `<your-username>` în comenzile de mai jos cu URL-ul fork-ului dvs. (sau URL-ul upstream dacă preferați).

Pentru a clona doar istoricul ultimului commit (descărcare mică):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pentru a clona un branch specific:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clonare parțială (sparse) — blob-uri minimale + doar folderele selectate

Aceasta folosește clonare parțială și sparse-checkout (necesită Git 2.25+ și se recomandă un Git modern cu suport pentru clonare parțială):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Intrați în folderul repo:

```bash|powershell
cd ai-agents-for-beginners
```

Apoi specificați ce foldere doriți (exemplul de mai jos arată două foldere):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

După clonare și verificarea fișierelor, dacă aveți nevoie doar de fișiere și doriți să eliberați spațiu (fără istoric git), vă rugăm să ștergeți meta-datele repository-ului (💀 ireversibil — veți pierde toate funcționalitățile Git: fără commit-uri, pull-uri, push-uri sau acces la istoric).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Folosind GitHub Codespaces (recomandat pentru a evita descărcări mari locale)

- Creați un nou Codespace pentru acest repo prin [GitHub UI](https://github.com/codespaces).  

- În terminalul codespace-ului nou creat, rulați una din comenzile de clonare superficială/sparse de mai sus pentru a aduce doar folderele lecțiilor de care aveți nevoie în spațiul de lucru Codespace.
- Opțional: după clonare în Codespaces, eliminați .git pentru a elibera spațiu suplimentar (vezi comenzile de eliminare de mai sus).
- Notă: Dacă preferați să deschideți repo-ul direct în Codespaces (fără clonare suplimentară), rețineți că Codespaces va construi mediul devcontainer și este posibil să aprovisioneze mai mult decât aveți nevoie. Clonarea unei copii superficiale într-un Codespace proaspăt vă oferă mai mult control asupra utilizării discului.

#### Sfaturi

- Întotdeauna înlocuiți URL-ul de clonare cu fork-ul dvs. dacă doriți să modificați/faceți commit.
- Dacă aveți nevoie ulterior de mai mult istoric sau fișiere, le puteți aduce prin fetch sau puteți ajusta sparse-checkout pentru a include foldere suplimentare.

## Rularea codului

Acest curs oferă o serie de Jupyter Notebooks pe care le puteți rula pentru a obține experiență practică în construirea de Agenți AI.

Exemplele de cod folosesc **Microsoft Agent Framework (MAF)** cu `FoundryChatClient`, care se conectează la **Microsoft Foundry Agent Service V2** (API-ul Responses) prin **Microsoft Foundry**.

Toate notebook-urile Python sunt etichetate `*-python-agent-framework.ipynb`.

## Cerințe

- Python 3.12+
  - **NOTĂ**: Dacă nu aveți Python3.12 instalat, asigurați-vă că îl instalați. Apoi creați-vă mediul virtual folosind python3.12 pentru a vă asigura că sunt instalate versiunile corecte din fișierul requirements.txt.
  
    >Exemplu

    Creați directorul pentru mediul virtual Python:

    ```bash|powershell
    python -m venv venv
    ```

    Apoi activați mediul virtual pentru:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Pentru codurile de exemplu care folosesc .NET, asigurați-vă că instalați [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) sau o versiune ulterioară. Apoi verificați versiunea SDK instalată:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Este necesar pentru autentificare. Instalați de la [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Abonament Azure** — Pentru acces la Microsoft Foundry și Microsoft Foundry Agent Service.
- **Proiect Microsoft Foundry** — Un proiect cu un model implementat (ex., `gpt-4.1-mini`). Vezi [Pasul 1](#pasul-1-creați-un-proiect-microsoft-foundry) mai jos.

Am inclus un fișier `requirements.txt` în rădăcina acestui repo care conține toate pachetele Python necesare pentru a rula exemplele de cod.

Le puteți instala rulând comanda următoare în terminal, în directorul rădăcină al repository-ului:

```bash|powershell
pip install -r requirements.txt
```

Recomandăm crearea unui mediu virtual Python pentru a evita conflictele și problemele.

## Configurarea VSCode

Asigurați-vă că utilizați versiunea corectă de Python în VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configurarea Microsoft Foundry și Microsoft Foundry Agent Service

### Pasul 1: Creați un Proiect Microsoft Foundry

Aveți nevoie de un **hub** și **proiect** Microsoft Foundry cu un model implementat pentru a rula notebook-urile.

1. Accesați [ai.azure.com](https://ai.azure.com) și conectați-vă cu contul Azure.
2. Creați un **hub** (sau folosiți unul existent). Vezi: [Prezentare generală resurse Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. În cadrul hub-ului, creați un **proiect**.
4. Implementați un model (ex., `gpt-4.1-mini`) din **Models + Endpoints** → **Deploy model**.

### Pasul 2: Obțineți Endpoint-ul proiectului și numele implementării modelului

Din proiectul dvs. în portalul Microsoft Foundry:

- **Project Endpoint** — Accesați pagina **Overview** și copiați URL-ul endpoint-ului.

![Project Connection String](../../../translated_images/ro/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Accesați **Models + Endpoints**, selectați modelul implementat și rețineți **Deployment name** (ex., `gpt-4.1-mini`).

### Pasul 3: Autentificați-vă în Azure cu `az login`

Toate notebook-urile folosesc **`AzureCliCredential`** pentru autentificare — fără chei API de gestionat. Aceasta necesită să fiți autentificat prin Azure CLI.

1. **Instalați Azure CLI** dacă nu l-ați instalat deja: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Conectați-vă** rulând:

    ```bash|powershell
    az login
    ```

    Sau dacă sunteți într-un mediu remote/Codespace fără browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Selectați abonamentul** dacă vi se solicită — alegeți-l pe cel care conține proiectul Foundry.

4. **Verificați** că sunteți autentificat:

    ```bash|powershell
    az account show
    ```

> **De ce `az login`?** Notebook-urile se autentifică folosind `AzureCliCredential` din pachetul `azure-identity`. Aceasta înseamnă că sesiunea dvs. Azure CLI furnizează credențialele — fără chei API sau secrete în fișierul `.env`. Aceasta este o [practică de securitate recomandată](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Pasul 4: Creați fișierul `.env`

Copiați fișierul exemplu:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Deschideți `.env` și completați aceste două valori:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Variabilă | Unde să o găsiți |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → proiectul dvs. → pagina **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → numele modelului implementat |

Acesta este tot pentru cele mai multe lecții! Notebook-urile se vor autentifica automat prin sesiunea dvs. `az login`.

### Pasul 5: Instalați dependențele Python

```bash|powershell
pip install -r requirements.txt
```

Recomandăm să rulați acest lucru în mediul virtual creat anterior.

## Configurare suplimentară pentru Lecția 5 (Agentic RAG)

Lecția 5 folosește **Azure AI Search** pentru generare augmentată cu recuperare. Dacă intenționați să rulați acea lecție, adăugați aceste variabile în fișierul `.env`:

| Variabilă | Unde să o găsiți |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → resursa dvs. **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Portal Azure → resursa dvs. **Azure AI Search** → **Settings** → **Keys** → cheia principală admin |

## Configurare suplimentară pentru lecțiile care apelează Azure OpenAI direct (Lecțiile 6 și 8)

Unele notebook-uri din lecțiile 6 și 8 apelează **Azure OpenAI** direct (folosind **Responses API**) în loc să treacă printr-un proiect Microsoft Foundry. Aceste exemple foloseau anterior GitHub Models, care este învechit (se retrage în iulie 2026) și nu suportă Responses API. Dacă intenționați să rulați acele exemple, adăugați aceste variabile în fișierul `.env`:

| Variabilă | Unde să o găsiți |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → resursa dvs. **Azure OpenAI** → **Keys and Endpoint** → Endpoint (ex. `https://<resursa-dvs>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Numele modelului implementat (ex. `gpt-4.1-mini`) care suportă Responses API |
| `AZURE_OPENAI_API_KEY` | Opțional — doar dacă folosiți autentificare bazată pe cheie în loc de `az login` / Entra ID |

> Responses API folosește endpoint-ul stabil `/openai/v1/`, deci nu este necesar `api-version`. Autentificați-vă cu `az login` pentru a folosi autentificarea fără cheie Entra ID.

## Furnizor alternativ: MiniMax (compatibil OpenAI)

[MiniMax](https://platform.minimaxi.com/) oferă modele cu context mare (până la 204K tokeni) printr-un API compatibil OpenAI. Deoarece `OpenAIChatClient` din Microsoft Agent Framework funcționează cu orice endpoint compatibil OpenAI, puteți folosi MiniMax ca alternativă directă la Azure OpenAI sau OpenAI.

Adăugați aceste variabile în fișierul `.env`:

| Variabilă | Unde să o găsiți |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Platforma MiniMax](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Folosiți `https://api.minimax.io/v1` (valoare implicită) |
| `MINIMAX_MODEL_ID` | Numele modelului de folosit (ex., `MiniMax-M3`) |

**Modele exemplu**: `MiniMax-M3` (recomandat), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (răspunsuri mai rapide). Numele modelelor și disponibilitatea pot varia în timp, iar accesul la un model depinde de contul sau regiunea dvs. — verificați [Platforma MiniMax](https://platform.minimaxi.com/) pentru lista curentă. Dacă `MiniMax-M3` nu este disponibil pentru contul dvs., setați `MINIMAX_MODEL_ID` la un model la care aveți acces (ex. `MiniMax-M2.7`).

Exemplele de cod care folosesc `OpenAIChatClient` (ex., fluxul de lucru pentru rezervarea hotelului din Lecția 14) vor detecta automat și utiliza configurația MiniMax dacă este setată `MINIMAX_API_KEY`.

## Furnizor alternativ: Foundry Local (Rulează modele local)

[Foundry Local](https://foundrylocal.ai) este un runtime ușor care descarcă, gestionează și servește modele de limbaj **în întregime pe propriul dvs. calculator** printr-un API compatibil OpenAI — fără cloud, fără abonament Azure și fără chei API. Este o opțiune excelentă pentru dezvoltare offline, experimentare fără costuri cloud sau păstrarea datelor local.

Deoarece `OpenAIChatClient` din Microsoft Agent Framework funcționează cu orice endpoint compatibil OpenAI, Foundry Local este o alternativă locală directă la Azure OpenAI.

**1. Instalați Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Descărcați și rulați un model** (aceasta pornește și serviciul local):

```bash
foundry model list          # vezi modelele disponibile
foundry model run phi-4-mini
```

**3. Instalați SDK-ul Python** folosit pentru a descoperi endpoint-ul local:

```bash
pip install foundry-local-sdk
```

**4. Indicați Microsoft Agent Framework către modelul dvs. local:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Descarcă (dacă este necesar) și servește modelul local, apoi descoperă endpoint-ul/portul.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # de ex. http://localhost:<port>/v1
    api_key=manager.api_key,        # întotdeauna "nu este necesar" pentru Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Notă:** Foundry Local expune un endpoint compatibil OpenAI pentru **Chat Completions**. Folosiți-l pentru dezvoltare locală și scenarii offline. Pentru setul complet de funcționalități **Responses API** (conversații stateful, orchestrare complexă de unelte și dezvoltare de tip agent), țintiți către **Azure OpenAI** sau un proiect **Microsoft Foundry** așa cum este arătat în lecții. Consultați [documentația Foundry Local](https://foundrylocal.ai) pentru catalogul curent de modele și suport platformă.


## Configurare suplimentară pentru Lecția 8 (Flux de lucru Bing Grounding)

Notebook-ul de flux condiționat din lecția 8 folosește **Bing grounding** prin Microsoft Foundry. Dacă intenționați să rulați acel exemplu, adăugați această variabilă în fișierul vostru `.env`:

| Variabilă | Unde o găsiți |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal Microsoft Foundry → proiectul vostru → **Management** → **Resurse conectate** → conexiunea Bing → copiați ID-ul conexiunii |

## Depanare

### Erori la verificarea certificatului SSL pe macOS

Dacă folosiți macOS și întâmpinați o eroare ca acesta:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Aceasta este o problemă cunoscută cu Python pe macOS unde certificatele SSL ale sistemului nu sunt acceptate automat. Încercați următoarele soluții în ordine:

**Opțiunea 1: Rulați scriptul Install Certificates al Python (recomandat)**

```bash
# Înlocuiți 3.XX cu versiunea dvs. Python instalată (de ex., 3.12 sau 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opțiunea 2: Folosiți `connection_verify=False` în notebook-ul vostru (doar pentru notebook-urile GitHub Models)**

În notebook-ul Lecția 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), un workaround comentat este deja inclus. Decomentați `connection_verify=False` când creați clientul:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Dezactivați verificarea SSL dacă întâmpinați erori de certificat
)
```

> **⚠️ Atenție:** Dezactivarea verificării SSL (`connection_verify=False`) reduce securitatea prin sărirea validării certificatului. Folosiți asta doar ca soluție temporară în medii de dezvoltare, niciodată în producție.

**Opțiunea 3: Instalați și folosiți `truststore`**

```bash
pip install truststore
```

Apoi adăugați următorul cod la începutul notebook-ului sau scriptului vostru înainte de a face orice apel de rețea:

```python
import truststore
truststore.inject_into_ssl()
```

## Blocată undeva?

Dacă aveți probleme cu această configurare, intrați în <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> sau <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">creați o problemă</a>.

## Lecția următoare

Acum sunteți gata să rulați codul pentru acest curs. Spor la învățat mai multe despre lumea Agenților AI! 

[Introducere în Agenții AI și Cazuri de utilizare a Agenților](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->