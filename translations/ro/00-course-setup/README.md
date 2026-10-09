# Configurarea cursului

## Introducere

Această lecție va acoperi modul de rulare a exemplelor de cod din acest curs.

## Alăturați-vă altor cursanți și obțineți ajutor

Înainte de a începe să clonați depozitul, alăturați-vă [canalului Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) pentru a primi ajutor cu configurarea, întrebări despre curs sau pentru a vă conecta cu alți cursanți.

## Clonați sau faceți fork la acest depozit

Pentru a începe, vă rugăm să clonați sau să faceți fork la depozitul GitHub. Acest lucru vă va crea propria versiune a materialului cursului, astfel încât să puteți rula, testa și modifica codul!

Acest lucru se poate face dând click pe linkul <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">pentru a face fork la repo</a>

Acum ar trebui să aveți propria versiune fork-uită a acestui curs la următorul link:

![Forked Repo](../../../translated_images/ro/forked-repo.33f27ca1901baa6a.webp)

### Clonare superficială (recomandată pentru atelier / Codespaces)

  >Depozitul complet poate fi mare (~3 GB) dacă descărcați întreaga istorie și toate fișierele. Dacă participați doar la atelier sau aveți nevoie doar de câteva foldere de lecție, o clonare superficială (sau sparse clone) descarcă mult mai puțin.

#### Clonare superficială rapidă — istorie minimală, toate fișierele

Înlocuiți `<your-username>` în comenzile de mai jos cu URL-ul fork-ului dvs. (sau URL-ul upstream dacă preferați).

Pentru a clona doar istoricul ultimului commit (descărcare mică):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pentru a clona un branch specific:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clonare parțială (sparse) — bloburi minimale + doar folderele selectate

Aceasta folosește clonarea parțială și sparse-checkout (necesită Git 2.25+ și recomandat un Git modern cu suport pentru clonare parțială):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Intrați în folderul repo:

```bash
cd ai-agents-for-beginners
```

Apoi specificați ce foldere doriți (exemplul de mai jos arată două foldere):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

După clonare și verificarea fișierelor, dacă aveți nevoie doar de fișiere și doriți să eliberați spațiu (fără istoric git), ștergeți metadata depozitului (💀 ireversibil — veți pierde toată funcționalitatea Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Utilizarea GitHub Codespaces (recomandat pentru a evita descărcări mari locale)

- Creați un Codespace nou pentru acest repo prin [GitHub UI](https://github.com/codespaces).  

- În terminalul din Codespace-ul nou creat, rulați una dintre comenzile shallow/sparse clone de mai sus pentru a aduce doar folderele lecțiilor de care aveți nevoie în spațiul de lucru Codespace.
- Opțional: după clonare în Codespaces, eliminați .git pentru a recupera spațiu suplimentar (vedeți comenzile de ștergere mai sus).
- Notă: Dacă preferați să deschideți repo direct în Codespaces (fără o clonare suplimentară), rețineți că Codespaces va construi mediul devcontainer și poate încă să pregătească mai mult decât aveți nevoie.

#### Sfaturi

- Înlocuiți întotdeauna URL-ul de clonare cu cel al fork-ului dacă doriți să editați/comite.
- Dacă ulterior aveți nevoie de mai mult istoric sau fișiere, le puteți prelua sau ajusta sparse-checkout pentru a include foldere suplimentare.

## Rularea codului

Acest curs oferă o serie de Jupyter Notebooks pe care le puteți rula pentru a obține experiență practică în construirea de agenți AI.

Exemplele de cod utilizează **Microsoft Agent Framework (MAF)** cu `FoundryChatClient`, care se conectează la **Microsoft Foundry Agent Service V2** (API-ul Responses) prin **Microsoft Foundry**.

Toate notebook-urile Python sunt etichetate `*-python-agent-framework.ipynb`.

## Cerințe

- Python 3.12+
  - **NOTĂ**: Dacă nu aveți Python3.12 instalat, asigurați-vă că îl instalați. Apoi creați mediul virtual folosind python3.12 pentru a garanta instalarea versiunilor corecte din fișierul requirements.txt.
  
    >Exemplu

    Creați director pentru mediul virtual Python:

    ```bash
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

- .NET 10+: Pentru exemplele de cod care folosesc .NET, asigurați-vă că instalați [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) sau o versiune ulterioară. Apoi verificați versiunea SDK-ului .NET instalat:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Necesitar pentru autentificare. Instalați de la [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Abonament Azure** — Pentru acces la Microsoft Foundry și Microsoft Foundry Agent Service.
- **Proiect Microsoft Foundry** — Un proiect cu un model implementat (de exemplu, `gpt-5-mini`). Vedeți [Pasul 1](#pasul-1-creați-un-proiect-microsoft-foundry) mai jos.

Am inclus un fișier `requirements.txt` în rădăcina acestui depozit care conține toate pachetele Python necesare pentru rularea exemplelor de cod.

Le puteți instala rulând comanda următoare în terminal la rădăcina depozitului:

```bash
pip install -r requirements.txt
```

Recomandăm să creați un mediu virtual Python pentru a evita conflicte și probleme.

## Configurare VSCode

Asigurați-vă că folosiți versiunea corectă de Python în VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configurare Microsoft Foundry și Microsoft Foundry Agent Service

### Pasul 1: Creați un proiect Microsoft Foundry

Aveți nevoie de un **hub** Microsoft Foundry și un **proiect** cu un model implementat pentru a rula notebook-urile.

1. Accesați [ai.azure.com](https://ai.azure.com) și conectați-vă cu contul dvs. Azure.
2. Creați un **hub** (sau folosiți unul existent). Vezi: [Prezentare generală resurse Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. În interiorul hub-ului, creați un **proiect**.
4. Implementați un model (de exemplu, `gpt-5-mini`) din **Models + Endpoints** → **Deploy model**.

### Pasul 2: Obțineți adresa endpoint și numele de implementare al modelului din proiect

Din proiectul dvs. în portalul Microsoft Foundry:

- **Project Endpoint** — Mergeți la pagina **Overview** și copiați URL-ul endpoint.

![Project Connection String](../../../translated_images/ro/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Accesați **Models + Endpoints**, selectați modelul implementat și notați **Deployment name** (exemplu, `gpt-5-mini`).

### Pasul 3: Conectați-vă la Azure cu `az login`

Cele mai multe notebook-uri se autentifică prin **autentificarea CLI-ului Azure** — folosind `AzureCliCredential` sau `DefaultAzureCredential` (ambele preiau sesiunea `az login`) din pachetul `azure-identity` — astfel că nu necesită chei API. Câteva lecții și integrări opționale folosesc chei API; verificați cerințele fiecărei lecții pentru variabilele suplimentare de mediu. Acest lucru presupune să fiți autentificat prin Azure CLI.

1. **Instalați Azure CLI** dacă nu este deja instalat: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Conectați-vă** rulând:

    ```bash
    az login
    ```

    Sau dacă sunteți într-un mediu remote/Codespace fără browser:

    ```bash
    az login --use-device-code
    ```

3. **Selectați abonamentul** dacă vi se solicită — alegeți cel care conține proiectul Foundry.

4. **Verificați** că sunteți conectat:

    ```bash
    az account show
    ```

> **De ce `az login`?** Notebook-urile se autentifică folosind `AzureCliCredential` (sau `DefaultAzureCredential`, care preia și sesiunea dvs. Azure CLI) din pachetul `azure-identity`. Aceasta înseamnă că sesiunea Azure CLI furnizează credențialele — fără chei API sau secrete în fișierul `.env`. Aceasta este o [practică de securitate recomandată](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variabilă | Unde să o găsiți |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → proiectul dvs. → pagina **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → numele modelului implementat |

Asta este tot pentru majoritatea lecțiilor! Notebook-urile se vor autentifica automat prin sesiunea dvs. `az login`.

### Pasul 5: Instalați dependențele Python

```bash
pip install -r requirements.txt
```

Recomandăm să rulați acest lucru în mediul virtual creat anterior.

## Configurare opțională: Azure AI Search (Lecțiile 5 și 16)

Notebook-urile din Lecția 5 (Agentic RAG) și Lecția 16 rulează direct cu o **bază de cunoștințe în memorie** — fără resurse Azure suplimentare. Dacă doriți să le susțineți cu un index real **Azure AI Search**, rețineți că **notebook-ul din Lecția 16 folosește în prezent autentificare bazată pe chei**: trece de la căutarea în memorie la Azure AI Search doar când **ambele** `AZURE_SEARCH_SERVICE_ENDPOINT` **și** `AZURE_SEARCH_API_KEY` sunt setate, altfel rămâne pe căutarea în memorie — deci pentru a-l rula cu un index real trebuie să setați și cheia admin. Autentificarea fără chei cu Microsoft Entra ID (RBAC) este metoda recomandată pentru codul dvs. de producție, consistentă cu fluxul `az login` folosit peste tot în acest curs.

Pașii RBAC de mai jos se aplică pentru exemplele ghid de configurare și codul dvs. propriu. Ei nu activează autentificarea fără chei în notebook-ul Lecția 16; acesta tot necesită endpoint și cheia admin pentru a folosi Azure AI Search.

1. **Activați accesul bazat pe roluri** pe serviciul dvs. de căutare:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Atribuiți-vă rolurile necesare** (creare/încărcare indexuri și interogare):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Adăugați endpoint-ul** în fișierul dvs. `.env`:

| Variabilă | Unde să o găsiți |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → resursa dvs. **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Necesară (împreună cu endpoint-ul) pentru a activa Azure AI Search în notebook-ul din Lecția 16, care folosește autentificare bazată pe chei. Portal Azure → **Settings** → **Keys** → cheia admin primară |

> **De ce fără chei?** Cheile admin oferă acces complet de scriere la serviciul dvs. de căutare și se pot scurge prin fișiere `.env`. Cu RBAC, identitatea dvs. `az login` este folosită în schimb — același model fără chei Entra ID pe care cursul îl folosește în notebook-uri (prin `AzureCliCredential` / `DefaultAzureCredential`). Vedeți [Conectarea la Azure AI Search folosind roluri](https://learn.microsoft.com/azure/search/search-security-rbac).

Consultați [Ghidul de configurare Azure AI Search](./AzureSearch.md) pentru exemple complete de creare indexuri în Python și .NET.

## Configurare suplimentară pentru lecții care apelează direct Azure OpenAI (Lecțiile 6 și 8)

Unele notebook-uri din lecțiile 6 și 8 apelează **Azure OpenAI** direct (folosind **Responses API**) în loc să treacă printr-un proiect Microsoft Foundry. Aceste exemple foloseau anterior modelele GitHub, care sunt depreciate și nu suportă Responses API. Adăugați aceste variabile în fișierul dvs. `.env`:

| Variabilă | Unde să o găsiți |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → resursa dvs. **Azure OpenAI** → **Keys and Endpoint** → Endpoint (ex. `https://<resursa-dvs>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Numele modelului implementat (ex. `gpt-5-mini`) care suportă Responses API |
| `AZURE_OPENAI_API_KEY` | Opțional — doar dacă folosiți autentificare bazată pe chei în loc de `az login` / Entra ID |

> Responses API folosește endpoint-ul stabil `/openai/v1/`, deci nu este necesară `api-version`. Conectați-vă cu `az login` pentru a folosi autentificare fără chei Entra ID.

## Furnizor alternativ: MiniMax (compatibil OpenAI)

[MiniMax](https://platform.minimaxi.com/) oferă modele cu context mare (până la 204K token-uri) printr-un API compatibil OpenAI. Deoarece `OpenAIChatClient` din Microsoft Agent Framework funcționează cu orice endpoint compatibil OpenAI, puteți folosi MiniMax ca alternativă directă pentru lecțiile care folosesc `OpenAIChatClient`.

Adăugați aceste variabile în fișierul `.env`:

| Variabilă | Unde să o găsiți |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Folosiți `https://api.minimax.io/v1` (valoare implicită) |
| `MINIMAX_MODEL_ID` | Numele modelului de folosit (ex., `MiniMax-M3`) |

**Modele exemplu**: `MiniMax-M3` (recomandat), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (răspunsuri mai rapide). Numele modelelor și disponibilitatea pot varia în timp, iar accesul la un model poate depinde de contul dvs.

Exemplele de cod care folosesc `OpenAIChatClient` (ex., fluxul de rezervare hotel din Lecția 14) vor detecta automat și vor folosi configurația MiniMax când `MINIMAX_API_KEY` este setat.


## Furnizor alternativ: Novita AI (compatibil OpenAI)

[Novita AI](https://novita.ai/llm-api) oferă un API compatibil cu OpenAI pentru LLM-uri open-source și de frontieră (DeepSeek, Llama, Qwen și altele). Deoarece `OpenAIChatClient` din Microsoft Agent Framework funcționează cu orice endpoint compatibil OpenAI, poți folosi Novita AI ca o alternativă plug-and-play la Azure OpenAI sau OpenAI.

Adaugă aceste variabile în fișierul tău `.env`:

| Variabilă | Unde o găsești |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | Folosește `https://api.novita.ai/openai/v1` (valoare implicită) |
| `NOVITA_MODEL_ID` | Numele modelului pe care să-l folosești (ex., `moonshotai/kimi-k3`) |

**Modele exemplu**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI găzduiește de asemenea multe alte familii de modele open-source (Llama, Qwen, GLM și altele) — verifică [biblioteca de modele Novita AI](https://novita.ai/llm-api) pentru lista curentă de modele disponibile și ID-urile acestora.

Exemplele curente nu consumă automat variabilele `NOVITA_*`. Pentru a folosi Novita AI, transmite aceste valori explicit când construiești `OpenAIChatClient` în exemplul pe care îl rulezi.

## Furnizor alternativ: Foundry Local (Rulează modele local)

[Foundry Local](https://foundrylocal.ai) este un runtime ușor care descarcă, administrează și servește modele de limbaj **complet pe propria ta mașină** printr-un API compatibil OpenAI — fără cloud.

Deoarece `OpenAIChatClient` din Microsoft Agent Framework funcționează cu orice endpoint compatibil OpenAI, Foundry Local este o alternativă locală plug-and-play la Azure OpenAI.

**1. Instalează Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Descarcă și rulează un model** (asta pornește și serviciul local):

```bash
foundry model list          # vezi modelele disponibile
foundry model run phi-4-mini
```

**3. Instalează SDK-ul Python** folosit pentru a descoperi endpoint-ul local:

```bash
pip install foundry-local-sdk
```

**4. Configurează Microsoft Agent Framework să folosească modelul tău local:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Descarcă (dacă este necesar) și servește modelul local, apoi descoperă endpoint-ul/portul.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # de ex. http://localhost:<port>/v1
    api_key=manager.api_key,        # întotdeauna "not-required" pentru Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Notă:** Foundry Local oferă un endpoint **Chat Completions** compatibil OpenAI. Folosește-l pentru dezvoltare locală și scenarii offline. Pentru setul complet de funcții al **Responses API** (conversații cu stare, etc.) folosește Azure OpenAI sau un proiect Microsoft Foundry.

## Configurare suplimentară pentru Lecția 8 (Flux de lucru Bing Grounding)

Notebook-ul pentru fluxul condițional din lecția 8 folosește **Bing grounding** prin Microsoft Foundry. Dacă plănuiești să rulezi acel exemplu, adaugă această variabilă în fișierul tău `.env`:

| Variabilă | Unde o găsești |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal Microsoft Foundry → proiectul tău → **Management** → **Connected resources** → conexiunea ta Bing → copiază ID-ul conexiunii |

## Depanare

### Erori de verificare a certificatului SSL pe macOS

Dacă te afli pe macOS și întâmpini o eroare de genul:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Aceasta este o problemă cunoscută cu Python pe macOS, unde certificatele SSL ale sistemului nu sunt considerate automat de încredere. Încearcă următoarele soluții în ordine:

**Opțiunea 1: Rulează scriptul Install Certificates al Python (recomandat)**

```bash
# Înlocuiți 3.XX cu versiunea dvs. Python instalată (de exemplu, 3.12 sau 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opțiunea 2: Folosește `connection_verify=False` în notebook-ul tău (doar pentru notebook-uri GitHub Models)**

În notebook-ul Lecției 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), există deja o soluție comentată. Decomentează `connection_verify=False` când întâlnești erori legate de certificate:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Dezactivează verificarea SSL dacă întâmpini erori de certificat
)
```

> **⚠️ Atenție:** Dezactivarea verificării SSL (`connection_verify=False`) reduce securitatea deoarece sări peste validarea certificatului. Folosește aceasta doar ca soluție temporară în medii de dezvoltare. Nu o folosi niciodată în producție.

**Opțiunea 3: Instalează și folosește `truststore`**

```bash
pip install truststore
```

Apoi adaugă următoarea linie la începutul notebook-ului sau scriptului înainte de a face apeluri de rețea:

```python
import truststore
truststore.inject_into_ssl()
```

## Blocată undeva?

Dacă ai probleme în rularea acestei configurări, intră în <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord-ul Comunității Azure AI</a> sau <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">creează un issue</a>.

## Lecția următoare

Acum ești gata să rulezi codul acestui curs. Spor la învățat mai mult despre lumea AI Agents!

[Introducere în AI Agents și cazuri de utilizare ale agenților](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->