# Configurarea Cursului

## Introducere

Această lecție va explica cum să rulezi exemplele de cod din acest curs.

## Alătură-te altor cursanți și primește ajutor

Înainte de a începe să clonezi repo-ul, alătură-te canalului [AI Agents For Beginners Discord](https://aka.ms/ai-agents/discord) pentru a primi ajutor cu configurarea, întrebări despre curs sau pentru a te conecta cu alți cursanți.

## Clonează sau fă Fork la acest Repo

Pentru a începe, te rugăm să clonezi sau să faci fork la Repozitoriul GitHub. Acest lucru îți va crea propria versiune a materialului de curs astfel încât să poți rula, testa și modifica codul!

Acest lucru se poate face dând click pe linkul către <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fă fork la repo</a>

Ar trebui să ai acum propria versiune fork-uită a acestui curs în următorul link:

![Forked Repo](../../../translated_images/ro/forked-repo.33f27ca1901baa6a.webp)

### Clonare superficială (recomandată pentru workshop / Codespaces)

  >Repozitoriul complet poate fi mare (~3 GB) când descarci istoricul complet și toate fișierele. Dacă participi doar la workshop sau ai nevoie doar de câteva foldere de lecție, o clonare superficială (sau o clonare sparse) evită majoritatea descărcărilor prin trunchierea istoricului și/sau sărind peste blob-uri.

#### Clonare superficială rapidă — istoric minim, toate fișierele

Înlocuiește `<your-username>` în comenzile de mai jos cu URL-ul fork-ului tău (sau URL-ul upstream dacă preferi).

Pentru a clona doar istoricul ultimului commit (descărcare mică):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pentru clonarea unui branch specific:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clonare parțială (sparse) — blob-uri minime + doar foldere selectate

Aceasta folosește clonare parțială și sparse-checkout (necesită Git 2.25+ și recomandat Git modern cu suport pentru clonare parțială):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Accesează folderul repo:

```bash|powershell
cd ai-agents-for-beginners
```

Apoi specifică ce foldere vrei (exemplul de mai jos arată două foldere):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

După clonare și verificarea fișierelor, dacă ai nevoie doar de fișiere și dorești să eliberezi spațiu (fără istoric git), șterge metadatele repo-ului (💀 ireversibil — vei pierde toată funcționalitatea Git: fără commit-uri, pull, push sau acces la istoric).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Utilizarea GitHub Codespaces (recomandat pentru a evita descărcări mari locale)

- Creează un nou Codespace pentru acest repo prin [interfața GitHub](https://github.com/codespaces).  

- În terminalul noului codespace creat, rulează una dintre comenzile de clonare superficială/sparse de mai sus ca să aduci doar folderele de lecții de care ai nevoie în spațiul de lucru Codespace.
- Opțional: după clonare în Codespaces, elimină .git pentru a recupera spațiu suplimentar (vezi comenzile de eliminare de mai sus).
- Notă: Dacă preferi să deschizi repo-ul direct în Codespaces (fără clonare suplimentară), ia în calcul că Codespaces va construi mediul devcontainer și poate încă configura mai mult decât ai nevoie. Clonarea unei copii superficiale într-un Codespace proaspăt îți oferă mai mult control asupra utilizării discului.

#### Sfaturi

- Înlocuiește întotdeauna URL-ul de clonare cu fork-ul tău dacă dorești să editezi/commit-ui.
- Dacă ulterior ai nevoie de mai mult istoric sau fișiere, poți să le iei cu fetch sau să ajustezi sparse-checkout pentru a include foldere suplimentare.

## Rularea Codului

Acest curs oferă o serie de Jupyter Notebooks pe care le poți rula pentru a câștiga experiență practică în construirea AI Agents.

Exemplele de cod folosesc **Microsoft Agent Framework (MAF)** cu `FoundryChatClient`, care se conectează la **Microsoft Foundry Agent Service V2** (API-ul de Răspunsuri) prin **Microsoft Foundry**.

Toate noteboocurile Python sunt etichetate `*-python-agent-framework.ipynb`.

## Cerințe

- Python 3.12+
  - **NOTĂ**: Dacă nu ai instalat Python3.12, asigură-te că îl instalezi. Apoi creează-ți mediul virtual folosind python3.12 pentru a garanta că versiunile corecte sunt instalate din fișierul requirements.txt.
  
    >Exemplu

    Creează director pentru mediul Python virtual:

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

- .NET 10+: Pentru codurile de exemplu care folosesc .NET, asigură-te că instalezi [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) sau o versiune ulterioară. Apoi verifică versiunea instalată a SDK-ului .NET:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Necesare pentru autentificare. Instalează de la [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Abonament Azure** — Pentru acces la Microsoft Foundry și Microsoft Foundry Agent Service.
- **Proiect Microsoft Foundry** — Un proiect cu un model implementat (ex., `gpt-4o`). Vezi [Pasul 1](#pasul-1-creează-un-proiect-microsoft-foundry) mai jos.

Am inclus un fișier `requirements.txt` în rădăcina acestui repo care conține toate pachetele Python necesare pentru rularea exemplelor de cod.

Le poți instala rulând următoarea comandă în terminal, în rădăcina repo-ului:

```bash|powershell
pip install -r requirements.txt
```

Recomandăm crearea unui mediu virtual Python pentru a evita conflicte și probleme.

## Configurarea VSCode

Asigură-te că folosești versiunea corectă de Python în VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configurarea Microsoft Foundry și Microsoft Foundry Agent Service

### Pasul 1: Creează un Proiect Microsoft Foundry

Ai nevoie de un **hub** și un **proiect** în Microsoft Foundry cu un model implementat pentru a rula noteboocurile.

1. Accesează [ai.azure.com](https://ai.azure.com) și autentifică-te cu contul tău Azure.
2. Creează un **hub** (sau folosește unul existent). Vezi: [Prezentare generală resurse Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. În interiorul hub-ului, creează un **proiect**.
4. Implementează un model (ex., `gpt-4o`) din **Models + Endpoints** → **Deploy model**.

### Pasul 2: Obține Endpoint-ul Proiectului tău și Numele Implementării Modelului

Din proiectul tău în portalul Microsoft Foundry:

- **Project Endpoint** — Mergi la pagina **Overview** și copiază URL-ul endpoint-ului.

![Project Connection String](../../../translated_images/ro/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Accesează **Models + Endpoints**, selectează modelul implementat și notează **Deployment name** (ex., `gpt-4o`).

### Pasul 3: Autentificare în Azure cu `az login`

Toate noteboocurile folosesc **`AzureCliCredential`** pentru autentificare — fără a gestiona chei API. Acest lucru necesită să fii autentificat prin Azure CLI.

1. **Instalează Azure CLI** dacă nu ai făcut-o deja: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Autentifică-te** rulând:

    ```bash|powershell
    az login
    ```

    Sau dacă ești într-un mediu remote/Codespace fără browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Selectează abonamentul** dacă ți se cere — alege-l pe cel care conține proiectul Foundry.

4. **Verifică** că ești autentificat:

    ```bash|powershell
    az account show
    ```

> **De ce `az login`?** Noteboocurile se autentifică folosind `AzureCliCredential` din pachetul `azure-identity`. Aceasta înseamnă că sesiunea ta Azure CLI furnizează credențialele — fără chei API sau secrete în fișierul `.env`. Aceasta este o [practică de securitate recomandată](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Pasul 4: Creează fișierul tău `.env`

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

Asta este tot pentru majoritatea lecțiilor! Noteboocurile se vor autentifica automat prin sesiunea ta `az login`.

### Pasul 5: Instalează dependențele Python

```bash|powershell
pip install -r requirements.txt
```

Recomandăm să rulezi această comandă în mediul virtual pe care l-ai creat mai devreme.

## Configurare suplimentară pentru Lecția 5 (Agentic RAG)

Lecția 5 folosește **Azure AI Search** pentru generare augmentată pe baza căutării. Dacă intenționezi să rulezi acea lecție, adaugă aceste variabile în fișierul tău `.env`:

| Variabilă | Unde o găsești |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → resursa ta **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Portal Azure → resursa ta **Azure AI Search** → **Settings** → **Keys** → cheia de administrator principală |

## Configurare suplimentară pentru lecțiile care apelează direct Azure OpenAI (Lecțiile 6 și 8)

Unele noteboocuri din lecțiile 6 și 8 apelează direct **Azure OpenAI** (folosind **Responses API**) în loc să treacă printr-un proiect Microsoft Foundry. Aceste exemple foloseau anterior Modele GitHub, care sunt învechite (se retrag în iulie 2026) și nu suportă Responses API. Dacă intenționezi să rulezi acele exemple, adaugă aceste variabile în fișierul tău `.env`:

| Variabilă | Unde o găsești |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → resursa ta **Azure OpenAI** → **Keys and Endpoint** → Endpoint (ex. `https://<resursa-ta>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Numele modelului implementat (ex. `gpt-4o-mini`) care suportă Responses API |
| `AZURE_OPENAI_API_KEY` | Opțional — doar dacă folosești autentificare pe bază de cheie în loc de `az login` / Entra ID |

> Responses API folosește endpointul stabil `/openai/v1/`, deci nu este nevoie de `api-version`. Autentifică-te cu `az login` pentru autentificare fără chei prin Entra ID.

## Furnizor alternativ: MiniMax (compatibil OpenAI)

[MiniMax](https://platform.minimaxi.com/) oferă modele cu context mare (până la 204K tokeni) printr-un API compatibil OpenAI. Deoarece `OpenAIChatClient` din Microsoft Agent Framework funcționează cu orice endpoint compatibil OpenAI, poți folosi MiniMax ca alternativă plug-and-play la Azure OpenAI sau OpenAI.

Adaugă aceste variabile în fișierul tău `.env`:

| Variabilă | Unde o găsești |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → Chei API |
| `MINIMAX_BASE_URL` | Folosește `https://api.minimax.io/v1` (valoare implicită) |
| `MINIMAX_MODEL_ID` | Numele modelului de folosit (ex. `MiniMax-M3`) |

**Modele exemplu**: `MiniMax-M3` (recomandat), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (răspunsuri mai rapide). Numele și disponibilitatea modelelor pot varia în timp, iar accesul poate depinde de contul sau regiunea ta — verifică [MiniMax Platform](https://platform.minimaxi.com/) pentru lista curentă. Dacă `MiniMax-M3` nu este disponibil pentru contul tău, setează `MINIMAX_MODEL_ID` la un model la care ai acces (ex. `MiniMax-M2.7`).

Exemplele de cod care folosesc `OpenAIChatClient` (ex., fluxul de lucru de rezervare hotel din Lecția 14) vor detecta și folosi automat configurația MiniMax când `MINIMAX_API_KEY` este setat.

## Furnizor alternativ: Foundry Local (Rulează Modele pe Dispozitiv)

[Foundry Local](https://foundrylocal.ai) este un runtime ușor care descarcă, gestionează și servește modele de limbaj **complet pe propriul tău calculator** printr-un API compatibil OpenAI — fără cloud, fără abonament Azure și fără chei API. Este o opțiune excelentă pentru dezvoltare offline, experimentare fără costuri cloud sau menținerea datelor pe dispozitiv.

Deoarece `OpenAIChatClient` din Microsoft Agent Framework funcționează cu orice endpoint compatibil OpenAI, Foundry Local este o alternativă locală plug-and-play la Azure OpenAI.

**1. Instalează Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Descarcă și rulează un model** (aceasta pornește și serviciul local):

```bash
foundry model list          # vezi modelele disponibile
foundry model run phi-4-mini
```

**3. Instalează SDK-ul Python** folosit pentru a descoperi endpointul local:

```bash
pip install foundry-local-sdk
```

**4. Configurează Microsoft Agent Framework să folosească modelul local:**

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

> **Notă:** Foundry Local oferă un endpoint compatibil OpenAI pentru **Chat Completions**. Folosește-l pentru dezvoltare locală și scenarii offline. Pentru caracteristicile complete ale **Responses API** (conversații stateful, orchestrare avansată a instrumentelor și dezvoltare în stil agent), țintește către **Azure OpenAI** sau un proiect **Microsoft Foundry** așa cum este arătat în lecții. Vezi [documentația Foundry Local](https://foundrylocal.ai) pentru catalogul curent de modele și suportul platformei.

## Configurare suplimentară pentru Lecția 8 (Flux de lucru cu Bing Grounding)


Caietul de lucru al fluxului condițional din lecția 8 folosește **Bing grounding** prin Microsoft Foundry. Dacă intenționați să rulați acel exemplu, adăugați această variabilă în fișierul vostru `.env`:

| Variabilă | Unde o găsiți |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portalul Microsoft Foundry → proiectul vostru → **Management** → **Resurse conectate** → conexiunea voastră Bing → copiați ID-ul conexiunii |

## Rezolvarea problemelor

### Erori la verificarea certificatului SSL pe macOS

Dacă folosiți macOS și întâmpinați o eroare de genul:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Aceasta este o problemă cunoscută cu Python pe macOS, unde certificatele SSL ale sistemului nu sunt automat de încredere. Încercați următoarele soluții în ordine:

**Opțiunea 1: Rulați scriptul Install Certificates al Python (recomandat)**

```bash
# Înlocuiți 3.XX cu versiunea Python instalată (de exemplu, 3.12 sau 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opțiunea 2: Folosiți `connection_verify=False` în caietul vostru (doar pentru caietele GitHub Models)**

În caietul din Lecția 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), este deja inclusă o soluție comentată. Decomentați `connection_verify=False` când creați clientul:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Dezactivați verificarea SSL dacă întâmpinați erori de certificat
)
```

> **⚠️ Atenție:** Dezactivarea verificării SSL (`connection_verify=False`) reduce securitatea deoarece se sare peste validarea certificatului. Folosiți această opțiune doar ca soluție temporară în medii de dezvoltare, niciodată în producție.

**Opțiunea 3: Instalați și folosiți `truststore`**

```bash
pip install truststore
```

Apoi adăugați următoarele la începutul caietului sau scriptului vostru înainte de a face orice apel de rețea:

```python
import truststore
truststore.inject_into_ssl()
```

## Blocată undeva?

Dacă aveți probleme cu rularea acestui setup, intrați în <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord-ul Comunității Azure AI</a> sau <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">creați un issue</a>.

## Lecția următoare

Sunteți gata acum să rulați codul pentru acest curs. Spor la învățat mai multe despre lumea AI Agents! 

[Introducere în AI Agents și cazuri de utilizare a agenților](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->