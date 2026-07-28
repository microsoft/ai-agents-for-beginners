# Configurarea cursului

## Introducere

Această lecție va acoperi cum să rulați exemplele de cod din acest curs.

## Alăturați-vă altor cursanți și obțineți ajutor

Înainte de a începe să clonați repo-ul, alăturați-vă canalului [AI Agents For Beginners Discord](https://aka.ms/ai-agents/discord) pentru a primi ajutor cu configurarea, orice întrebare privind cursul sau pentru a vă conecta cu alți cursanți.

## Clonați sau faceți fork la acest Repo

Pentru început, vă rugăm să clonați sau să faceți fork la Repository-ul GitHub. Aceasta vă va crea propria versiune a materialului de curs, astfel încât să puteți rula, testa și modifica codul!

Acest lucru poate fi făcut făcând clic pe linkul pentru <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">a face fork la repo</a>

Ar trebui să aveți acum propria versiune fork-uită a acestui curs la următorul link:

![Repo Fork-uit](../../../translated_images/ro/forked-repo.33f27ca1901baa6a.webp)

### Clonare superficială (recomandată pentru workshop / Codespaces)

  >Repository-ul complet poate fi mare (~3 GB) dacă descărcați toată istoricul și toate fișierele. Dacă participați doar la workshop sau aveți nevoie doar de câteva foldere de lecții, o clonare superficială (sau clonare parcimonioasă) evită majoritatea descărcărilor prin trunchierea istoricului și/sau omisiunea bloburilor.

#### Clonare superficială rapidă — istoric minim, toate fișierele

Înlocuiți `<your-username>` în comenzile de mai jos cu URL-ul fork-ului dvs. (sau URL-ul upstream dacă preferați).

Pentru a clona numai istoricul ultimului commit (descărcare mică):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pentru a clona o anumită ramură:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clonare parțială (sparsa) — bloburi minime + doar folderele selectate

Aceasta folosește clonare parțială și sparse-checkout (necesită Git 2.25+ și Git modern recomandat cu suport pentru clonare parțială):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Intrați în folderul repo-ului:

```bash|powershell
cd ai-agents-for-beginners
```

Apoi specificați ce foldere doriți (exemplul de mai jos arată două foldere):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

După clonare și verificarea fișierelor, dacă aveți nevoie doar de fișiere și doriți să eliberați spațiu (fără istoric git), vă rugăm să ștergeți metadatele repository-ului (💀 ireversibil — veți pierde toată funcționalitatea Git: fără commit-uri, pull-uri, push-uri sau acces la istoric).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Utilizarea GitHub Codespaces (recomandat pentru a evita descărcările mari locale)

- Creați un nou Codespace pentru acest repo prin [interfața GitHub](https://github.com/codespaces).  

- În terminalul noului codespace creat, rulați una dintre comenzile de clonare superficială/sparse de mai sus pentru a aduce în workspace doar folderele lecțiilor de care aveți nevoie.
- Opțional: după clonare în Codespaces, eliminați .git pentru a recupera spațiu suplimentar (vedeți comenzile de eliminare de mai sus).
- Notă: Dacă preferați să deschideți repo-ul direct în Codespaces (fără clonare suplimentară), țineți cont că Codespaces va construi mediul devcontainer și poate provisiona mai mult decât aveți nevoie. Clonarea unei copii superficiale într-un Codespace nou vă oferă mai mult control asupra utilizării discului.

#### Sfaturi

- Întotdeauna înlocuiți URL-ul de clonare cu cel al fork-ului dacă doriți să editați/faceți commit.
- Dacă ulterior aveți nevoie de mai mult istoric sau fișiere, le puteți aduce prin fetch sau ajusta sparse-checkout pentru a include foldere adiționale.

## Rularea Codului

Acest curs oferă o serie de Jupyter Notebooks pe care le puteți rula pentru a obține experiență practică creând agenți AI.

Exemplele de cod folosesc **Microsoft Agent Framework (MAF)** cu `FoundryChatClient`, care se conectează la **Microsoft Foundry Agent Service V2** (API-ul Responses) prin **Microsoft Foundry**.

Toate notele Python sunt etichetate `*-python-agent-framework.ipynb`.

## Cerințe

- Python 3.12+
  - **NOTĂ**: Dacă nu aveți Python3.12 instalat, asigurați-vă că îl instalați. Apoi creați mediul virtual folosind python3.12 pentru a asigura instalarea versiunilor corecte din fișierul requirements.txt.
  
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

- .NET 10+: Pentru codurile de exemplu care folosesc .NET, asigurați-vă că instalați [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) sau o versiune ulterioară. Apoi verificați versiunea instalată a SDK-ului .NET:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Necesită pentru autentificare. Instalați de la [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Abonament Azure** — Pentru acces la Microsoft Foundry și Microsoft Foundry Agent Service.
- **Proiect Microsoft Foundry** — Un proiect cu un model implementat (ex: `gpt-5-mini`). Vezi [Pasul 1](#pasul-1-creați-un-proiect-microsoft-foundry) mai jos.

Am inclus un fișier `requirements.txt` în radacina acestui repository care conține toate pachetele Python necesare pentru a rula exemplele de cod.

Le puteți instala rulând următoarea comandă în terminal, în rădăcina repository-ului:

```bash|powershell
pip install -r requirements.txt
```

Recomandăm crearea unui mediu virtual Python pentru a evita conflicte și probleme.

## Configurare VSCode

Asigurați-vă că folosiți versiunea corectă de Python în VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configurați Microsoft Foundry și Microsoft Foundry Agent Service

### Pasul 1: Creați un proiect Microsoft Foundry

Aveți nevoie de un **hub** și un **proiect** Microsoft Foundry cu un model implementat pentru a rula notebook-urile.

1. Accesați [ai.azure.com](https://ai.azure.com) și conectați-vă cu contul dvs. Azure.
2. Creați un **hub** (sau folosiți unul existent). Vezi: [Prezentare resurse Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. În interiorul hub-ului, creați un **proiect**.
4. Implementați un model (ex: `gpt-5-mini`) din **Models + Endpoints** → **Deploy model**.

### Pasul 2: Obțineți Endpoint-ul Proiectului și Numele Implementării Modelului

Din proiectul dvs. din portalul Microsoft Foundry:

- **Endpoint Proiect** — Mergeți la pagina **Overview** și copiați URL-ul endpoint-ului.

![Șirul de conexiune al proiectului](../../../translated_images/ro/project-endpoint.8cf04c9975bbfbf1.webp)

- **Numele implementării modelului** — Mergeți la **Models + Endpoints**, selectați modelul implementat și rețineți **Deployment name** (ex: `gpt-5-mini`).

### Pasul 3: Autentificați-vă la Azure cu `az login`

Toate notele folosesc **`AzureCliCredential`** pentru autentificare — nu trebuie să gestionați chei API. Acest lucru necesită să fiți autentificat prin Azure CLI.

1. **Instalați Azure CLI** dacă nu l-ați instalat deja: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Autentificați-vă** rulând:

    ```bash|powershell
    az login
    ```

    Sau dacă sunteți într-un mediu remote/Codespace fără browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Selectați abonamentul** dacă vi se cere — alegeți-l pe cel care conține proiectul Foundry.

4. **Verificați** că sunteți autentificat:

    ```bash|powershell
    az account show
    ```

> **De ce `az login`?** Notebook-urile se autentifică folosind `AzureCliCredential` din pachetul `azure-identity`. Aceasta înseamnă că sesiunea dvs. Azure CLI furnizează credențialele — fără chei API sau secrete în fișierul `.env`. Acesta este un [cel mai bun practică de securitate](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Pasul 4: Creați fișierul dvs. `.env`

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variabilă | Unde să o găsiți |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → proiectul dvs. → pagina **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → numele modelului implementat |

Asta e tot pentru majoritatea lecțiilor! Notebook-urile se vor autentifica automat prin sesiunea dvs. `az login`.

### Pasul 5: Instalați dependențele Python

```bash|powershell
pip install -r requirements.txt
```

Recomandăm să rulați aceasta în mediul virtual creat anterior.

## Configurare suplimentară pentru Lecția 5 (Agentic RAG)

Lecția 5 folosește **Azure AI Search** pentru generare augmentată cu recuperare. Dacă intenționați să rulați acea lecție, adăugați aceste variabile în fișierul `.env`:

| Variabilă | Unde să o găsiți |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → resursa dvs. **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Portal Azure → resursa dvs. **Azure AI Search** → **Settings** → **Keys** → cheia principală de admin |

## Configurare suplimentară pentru lecțiile care apelează direct Azure OpenAI (Lecțiile 6 și 8)

Unele notele din lecțiile 6 și 8 apelează direct **Azure OpenAI** (folosind API-ul Responses) în loc să treacă printr-un proiect Microsoft Foundry. Aceste exemple foloseau anterior modelele GitHub, care sunt deprecate (se vor retrage în iulie 2026) și nu suportă API-ul Responses. Dacă intenționați să rulați acele exemple, adăugați aceste variabile în fișierul dvs. `.env`:

| Variabilă | Unde să o găsiți |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → resursa dvs. **Azure OpenAI** → **Keys and Endpoint** → Endpoint (ex: `https://<resursa-dvs>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Numele modelului implementat (ex: `gpt-5-mini`) care suportă API-ul Responses |
| `AZURE_OPENAI_API_KEY` | Opțional — doar dacă folosiți autentificare pe bază de cheie în loc de `az login` / Entra ID |

> API-ul Responses folosește endpoint-ul stabil `/openai/v1/`, așadar nu este nevoie de `api-version`. Autentificați-vă cu `az login` pentru a folosi autentificarea fără cheie Entra ID.

## Furnizor alternativ: MiniMax (compatibil OpenAI)

[MiniMax](https://platform.minimaxi.com/) oferă modele cu context mare (până la 204K tokeni) printr-un API compatibil OpenAI. Deoarece `OpenAIChatClient` din Microsoft Agent Framework funcționează cu orice endpoint compatibil OpenAI, puteți folosi MiniMax ca alternativă de tip drop-in la Azure OpenAI sau OpenAI.

Adăugați aceste variabile în fișierul `.env`:

| Variabilă | Unde să o găsiți |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Platforma MiniMax](https://platform.minimaxi.com/) → Chei API |
| `MINIMAX_BASE_URL` | Folosiți `https://api.minimax.io/v1` (valoarea implicită) |
| `MINIMAX_MODEL_ID` | Numele modelului de folosit (ex: `MiniMax-M3`) |

**Modele exemplu**: `MiniMax-M3` (recomandat), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (răspunsuri mai rapide). Numele și disponibilitatea modelelor pot varia în timp, iar accesul la un model depinde de contul dvs. sau regiune — verificați [Platforma MiniMax](https://platform.minimaxi.com/) pentru lista actuală. Dacă `MiniMax-M3` nu este disponibil pentru contul dvs., setați `MINIMAX_MODEL_ID` la un model la care aveți acces (ex: `MiniMax-M2.7`).

Exemplele de cod care folosesc `OpenAIChatClient` (ex: fluxul de rezervare hotel din Lecția 14) vor detecta și utiliza automat configurația MiniMax când `MINIMAX_API_KEY` este setat.

## Furnizor alternativ: Foundry Local (rulează modele local)

[Foundry Local](https://foundrylocal.ai) este un runtime ușor care descarcă, gestionează și servește modele lingvistice **în întregime pe mașina dvs.** printr-un API compatibil OpenAI — fără cloud, fără abonament Azure și fără chei API. Este o opțiune excelentă pentru dezvoltare offline, experimentare fără costuri cloud sau păstrarea datelor local.

Deoarece `OpenAIChatClient` din Microsoft Agent Framework funcționează cu orice endpoint compatibil OpenAI, Foundry Local este o alternativă locală tip drop-in pentru Azure OpenAI.

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

**4. Direcționați Microsoft Agent Framework către modelul local:**

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

> **Notă:** Foundry Local oferă un endpoint compatibil OpenAI pentru **Chat Completions**. Folosiți-l pentru dezvoltare locală și scenarii offline. Pentru funcționalitatea completă a **API-ului Responses** (conversații cu stare, orchestrare profundă a uneltelor și dezvoltare de tip agent), folosiți **Azure OpenAI** sau un proiect **Microsoft Foundry** așa cum este arătat în lecții. Consultați [documentația Foundry Local](https://foundrylocal.ai) pentru catalogul actual al modelelor și suportul platformei.

## Configurare suplimentară pentru Lecția 8 (Flux de lucru Bing Grounding)


Jurnalul de lucru condițional din lecția 8 utilizează **Bing grounding** prin Microsoft Foundry. Dacă intenționați să rulați acel exemplu, adăugați această variabilă în fișierul `.env`:

| Variabilă | Unde să o găsiți |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portalul Microsoft Foundry → proiectul dvs. → **Management** → **Resurse conectate** → conexiunea dvs. Bing → copiați ID-ul conexiunii |

## Depanare

### Erori la verificarea certificatului SSL pe macOS

Dacă utilizați macOS și întâmpinați o eroare de genul:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Aceasta este o problemă cunoscută cu Python pe macOS, unde certificatele SSL ale sistemului nu sunt considerate automat de încredere. Încercați următoarele soluții în ordine:

**Opțiunea 1: Rulați scriptul Install Certificates al Python (recomandat)**

```bash
# Înlocuiește 3.XX cu versiunea ta instalată de Python (de exemplu, 3.12 sau 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opțiunea 2: Folosiți `connection_verify=False` în jurnalul dvs. (doar pentru jurnalele GitHub Models)**

În jurnalul din Lecția 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), un ocol comentat este deja inclus. Deblocați `connection_verify=False` când creați clientul:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Dezactivați verificarea SSL dacă întâmpinați erori de certificat
)
```

> **⚠️ Atenție:** Dezactivarea verificării SSL (`connection_verify=False`) reduce securitatea prin sărirea validării certificatului. Folosiți aceasta doar ca o soluție temporară în mediile de dezvoltare, niciodată în producție.

**Opțiunea 3: Instalați și folosiți `truststore`**

```bash
pip install truststore
```

Apoi adăugați următorul cod în partea de sus a jurnalului sau scriptului înainte de a face orice apel de rețea:

```python
import truststore
truststore.inject_into_ssl()
```

## Blocată undeva?

Dacă aveți probleme în rularea acestei configurații, intrați în <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord-ul Comunității Azure AI</a> sau <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">creați un tichet (issue)</a>.

## Lecția următoare

Acum sunteți gata să rulați codul pentru acest curs. Spor la învățat mai multe despre lumea Agenților AI!

[Introducere în Agenții AI și Cazuri de Utilizare ale Agenților](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->