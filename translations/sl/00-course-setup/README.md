# Nastavitev tečaja

## Uvod

Ta lekcija bo zajemala, kako zagnati vzorce kode iz tega tečaja.

## Pridružite se drugim učečim in poiščite pomoč

Preden začnete klonirati svoj repo, se pridružite [kanalu AI Agents For Beginners na Discordu](https://aka.ms/ai-agents/discord), da dobite pomoč pri nastavitvi, vprašanja o tečaju ali se povežete z drugimi učečimi.

## Klonirajte ali 'forkajte' ta repozitorij

Za začetek prosimo klonirajte ali 'forkajte' GitHub repozitorij. Tako boste imeli svojo različico gradiva tečaja, da boste lahko zagnali, preizkusili in prilagodili kodo!

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ustvarite fork repozitorija</a>

You should now have your own forked version of this course in the following link:

![Forkan repozitorij](../../../translated_images/sl/forked-repo.33f27ca1901baa6a.webp)

### Plihen klon (priporočeno za delavnice / Codespaces)

  >Celoten repozitorij je lahko velik (~3 GB) ko prenesete celotno zgodovino in vse datoteke. Če se udeležujete le delavnice ali potrebujete le nekaj map z lekcijami, se s plihem kloniranjem (ali sparse klonom) izognete večjemu prenosu, saj skrajšate zgodovino in/ali preskočite velike blob-e.

#### Hiter plitki klon — minimalna zgodovina, vse datoteke

Replace `<your-username>` in the below commands with your fork URL (or the upstream URL if you prefer).

To clone only the latest commit history (small download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone a specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimalni blobs + le izbrane mape

This uses partial clone and sparse-checkout (requires Git 2.25+ and recommended modern Git with partial clone support):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Traverse into the repo folder:

```bash|powershell
cd ai-agents-for-beginners
```

Then specify which folders you want (example below shows two folders):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

After cloning and verifying the files, if you only need files and want to free space (no git history), please delete the repository metadata (💀irreversible — you will lose all Git functionality: no commits, pulls, pushes, or history access).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Uporaba GitHub Codespaces (priporočeno za izogibanje velikim lokalnim prenosom)

- Ustvarite nov Codespace za ta repozitorij prek [uporabniškega vmesnika GitHub](https://github.com/codespaces).  

- V terminalu novonastalega codespace-a zaženite enega od zgornjih shallow/sparse clone ukazov, da v Codespace delovno okolje pripeljete le mape z lekcijami, ki jih potrebujete.
- Izbirno: po kloniranju znotraj Codespaces odstranite .git za sprostitev dodatnega prostora (glejte ukaze za odstranjevanje zgoraj).
- Opomba: Če raje odprete repozitorij neposredno v Codespaces (brez dodatnega klona), upoštevajte, da bo Codespaces zgradil devcontainer okolje in morda še vedno pripravil več, kot potrebujete. Kloniranje plitke kopije znotraj svežega Codespace-a vam daje več nadzora nad porabo diska.

#### Nasveti

- Vedno zamenjajte URL za klon s URL-jem vašega forka, če želite urejati/commitati.
- Če pozneje potrebujete več zgodovine ali datotek, jih lahko pridobite z fetch ali prilagodite sparse-checkout, da vključite dodatne mape.

## Zagon kode

Ta tečaj ponuja serijo Jupyter zvezkov (Notebooks), ki jih lahko zaženete, da pridobite praktične izkušnje pri gradnji AI agentov.

The code samples use **Microsoft Agent Framework (MAF)** with the `AzureAIProjectAgentProvider`, which connects to **Azure AI Agent Service V2** (the Responses API) through **Microsoft Foundry**.

Vsi Python zvezki so označeni z `*-python-agent-framework.ipynb`.

## Zahteve

- Python 3.12+
  - **OPOMBA**: Če nimate nameščenega Python 3.12, ga namestite. Nato ustvarite virtualno okolje z python3.12, da zagotovite pravilne različice, nameščene iz datoteke requirements.txt.
  
    >Primer

    Create Python venv directory:

    ```bash|powershell
    python -m venv venv
    ```

    Then activate venv environment for:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: For the sample codes using .NET, ensure you install [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) or later. Then, check your installed .NET SDK version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Potrebno za avtentikacijo. Namestite s [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Za dostop do Microsoft Foundry in Azure AI Agent Service.
- **Microsoft Foundry Project** — Projekt z nameščenim modelom (npr. `gpt-4o`). Glejte [Korak 1](../../../00-course-setup) spodaj.

V korenu tega repozitorija smo vključili datoteko `requirements.txt`, ki vsebuje vse potrebne Python pakete za zagon vzorcev kode.

Namestite jih tako, da v terminalu, v korenu repozitorija, zaženete naslednji ukaz:

```bash|powershell
pip install -r requirements.txt
```

Priporočamo ustvarjanje Python virtualnega okolja, da se izognete konfliktom in težavam.

## Nastavitev VSCode

Prepričajte se, da v VSCode uporabljate pravo različico Pythona.

![slika](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavitev Microsoft Foundry in Azure AI Agent Service

### Korak 1: Ustvarite projekt v Microsoft Foundry

You need an Azure AI Foundry **hub** and **project** with a deployed model to run the notebooks.

1. Pojdite na [ai.azure.com](https://ai.azure.com) in se prijavite z vašim Azure računom.
2. Ustvarite **hub** (ali uporabite obstoječega). Glejte: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Znotraj huba ustvarite **projekt**.
4. Namestite (deploy) model (npr. `gpt-4o`) iz **Models + Endpoints** → **Deploy model**.

### Korak 2: Pridobite svoj endpoint projekta in ime nameščene različice modela

From your project in the Microsoft Foundry portal:

- **Project Endpoint** — Pojdite na stran **Overview** in kopirajte URL endpointa.

![Povezava projekta](../../../translated_images/sl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Pojdite na **Models + Endpoints**, izberite nameščeni model in zabeležite **Deployment name** (npr. `gpt-4o`).

### Korak 3: Prijavite se v Azure z `az login`

Vsi zvezki uporabljajo **`AzureCliCredential`** za overjanje — ni treba upravljati API ključev. To zahteva, da ste prijavljeni preko Azure CLI.

1. **Namestite Azure CLI**, če ga še niste: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prijavite se** tako, da zaženete:

    ```bash|powershell
    az login
    ```

    Ali če ste v oddaljenem/Codespace okolju brez brskalnika:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Izberite svojo naročnino** če ste pozvani — izberite tisto, ki vsebuje vaš Foundry projekt.

4. **Preverite**, da ste prijavljeni:

    ```bash|powershell
    az account show
    ```

> **Zakaj `az login`?** Zvezki se overijo z uporabo `AzureCliCredential` iz paketa `azure-identity`. To pomeni, da vaša Azure CLI seja zagotavlja poverilnice — ni API ključev ali skrivnosti v vaši datoteki `.env`. To je [varnostna najboljša praksa](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Korak 4: Ustvarite svojo datoteko `.env`

Copy the example file:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Open `.env` and fill in these two values:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → vaš projekt → stran **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → ime vaše nameščene različice modela |

To je to za večino lekcij! Zvezki se bodo samodejno overili prek vaše `az login` seje.

### Korak 5: Namestite Python odvisnosti

```bash|powershell
pip install -r requirements.txt
```

Priporočamo, da to zaženete v virtualnem okolju, ki ste ga prej ustvarili.

## Dodatna nastavitev za Lekcijo 5 (Agentic RAG)

Lekcija 5 uporablja **Azure AI Search** za retrieval-augmented generation. Če nameravate zagnati to lekcijo, dodajte te spremenljivke v vašo datoteko `.env`:

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → vaš **Azure AI Search** vir → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → vaš **Azure AI Search** vir → **Settings** → **Keys** → primarni administratorski ključ |

## Dodatna nastavitev za Lekcijo 6 in Lekcijo 8 (GitHub Models)

Nekateri zvezki v lekcijah 6 in 8 uporabljajo **GitHub Models** namesto Azure AI Foundry. Če nameravate zagnati te primere, dodajte te spremenljivke v vašo datoteko `.env`:

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Ime modela za uporabo (npr. `gpt-4o-mini`) |

## Dodatna nastavitev za Lekcijo 8 (Bing Grounding Workflow)

The conditional workflow notebook in lesson 8 uses **Bing grounding** via Azure AI Foundry. If you plan to run that sample, add this variable to your `.env` file:

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → vaš projekt → **Management** → **Connected resources** → vaša Bing povezava → kopirajte connection ID |

## Odpravljanje težav

### Napake pri preverjanju SSL certifikatov na macOS-u

If you are on macOS and encounter an error like:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

This is a known issue with Python on macOS where the system SSL certificates are not automatically trusted. Try the following solutions in order:

**Možnost 1: Zaženite skripto Install Certificates za Python (priporočeno)**

```bash
# Zamenjajte 3.XX z vašo nameščeno različico Pythona (npr. 3.12 ali 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnost 2: Uporabite `connection_verify=False` v vašem zvezku (samo za zvezke z GitHub Models)**

V lekciji 6 zvezku (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je že vključen začrtan način rešitve. Odkomentirajte `connection_verify=False` pri ustvarjanju klienta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Onemogočite preverjanje SSL, če naletite na napake s certifikatom
)
```

> **⚠️ Opozorilo:** Onemogočanje preverjanja SSL (`connection_verify=False`) zmanjša varnost, saj preskoči preverjanje certifikatov. Uporabljajte to le kot začasno rešitev v razvojnih okoljih, nikoli v produkciji.

**Možnost 3: Namestite in uporabite `truststore`**

```bash
pip install truststore
```

Then add the following at the top of your notebook or script before making any network calls:

```python
import truststore
truststore.inject_into_ssl()
```

## Se zataknete?

If you have any issues running this setup, hop into our <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> or <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ustvarite issue</a>.

## Naslednja lekcija

Zdaj ste pripravljeni za zagon kode za ta tečaj. Uživajte pri učenju o svetu AI agentov! 

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za točnost, upoštevajte, da lahko samodejni prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvor­nem jeziku naj velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->