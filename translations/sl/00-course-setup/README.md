# Nastavitev tečaja

## Uvod

Ta lekcija bo pokrila, kako zagnati primere kode iz tega tečaja.

## Pridružite se drugim učencem in pridobite pomoč

Preden začnete s kloniranjem vašega repozitorija, se pridružite [kanalu AI Agents For Beginners Discord](https://aka.ms/ai-agents/discord), da dobite pomoč pri nastavitvi, vprašanja glede tečaja ali da se povežete z drugimi učenci.

## Klonirajte ali forkajte ta repozitorij

Za začetek prosimo klonirajte ali forkajte GitHub repozitorij. Tako boste imeli svojo različico učnega gradiva, da boste lahko zagnali, preizkusili in prilagajali kodo!

To lahko storite tako, da kliknete povezavo za <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repozitorija</a>.

Sedaj morate imeti svojo forknjeno različico tega tečaja na naslednji povezavi:

![Forked Repo](../../../translated_images/sl/forked-repo.33f27ca1901baa6a.webp)

### Povrhnji klon (priporočeno za delavnice / Codespaces)

> Celoten repozitorij je lahko velik (~3 GB), če prenesete celotno zgodovino in vse datoteke. Če obiskujete samo delavnico ali potrebujete le nekaj map lekcij, povrhnji klon (ali redki klon) prepreči večino tega prenosa s skrajšanjem zgodovine in/ali preskakovanjem blobov.

#### Hitri povrhnji klon — minimalna zgodovina, vse datoteke

Zamenjajte `<your-username>` v spodnjih ukazih z URL-jem vaše forknjene različice (ali URL-jem upstream, če želite).

Za kloniranje zgolj najnovejše zgodovine commita (majhen prenos):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Za kloniranje določene veje:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delni (sparse) klon — minimalni blobi + samo izbrane mape

To uporablja delni klon in sparse-checkout (zahteva Git 2.25+ in priporočen sodoben Git s podporo delnih klonov):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pojdite v mapo repozitorija:

```bash|powershell
cd ai-agents-for-beginners
```

Nato določite, katere mape želite (primer spodaj prikazuje dve mapi):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po kloniranju in preverjanju datotek, če potrebujete le datoteke in želite sprostiti prostor (brez git zgodovine), izbrišite metapodatke repozitorija (💀nepreklicno — izgubili boste vse git funkcionalnosti: brez commitov, pullov, pushov ali dostopa do zgodovine).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Uporaba GitHub Codespaces (priporočeno za izogibanje velikim lokalnim prenosom)

- Ustvarite nov Codespace za ta repozitorij preko [GitHub UI](https://github.com/codespaces).

- V terminalu novonastalega codespace-a zaženite enega izmed zgornjih ukazov za povrhnji/sparse klon, da pripeljete samo potrebne mape lekcij v delovno okolje Codespace-a.
- Izbirno: po kloniranju znotraj Codespaces odstranite .git, da sprostite dodatni prostor (glej ukaze za odstranjevanje zgoraj).
- Opomba: Če želite repozitorij odpreti neposredno v Codespaces (brez dodatnega kloniranja), vedite, da Codespaces ustvari devcontainer okolje in lahko še vedno namesti več, kot potrebujete. Kloniranje povrhnje kopije znotraj svežega Codespace-a vam daje več nadzora nad uporabo diska.

#### Nasveti

- Vedno zamenjajte URL klona z vašim forkom, če želite urejati/commit-ati.
- Če kasneje potrebujete več zgodovine ali datotek, jih lahko pridobite (fetchate) ali prilagodite sparse-checkout, da vključite dodatne mape.

## Zagon kode

Ta tečaj ponuja serijo Jupyter zvezkov, ki jih lahko zaženete, da pridobite praktične izkušnje z izdelavo AI agentov.

Primeri kode uporabljajo **Microsoft Agent Framework (MAF)** z `AzureAIProjectAgentProvider`, ki se povezuje z **Azure AI Agent Service V2** (Responses API) prek **Microsoft Foundry**.

Vsi Python zvezki so označeni z `*-python-agent-framework.ipynb`.

## Zahteve

- Python 3.12+
  - **OPOMBA**: Če nimate nameščenega Python 3.12, poskrbite, da ga namestite. Nato ustvarite virtualno okolje z python3.12, da zagotovite pravilne različice paketov iz datoteke requirements.txt.
  
    >Primer

    Ustvarite Python venv mapo:

    ```bash|powershell
    python -m venv venv
    ```

    Nato aktivirajte venv okolje za:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Za vzorčne kode, ki uporabljajo .NET, zagotovite, da imate nameščen [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ali novejši. Nato preverite nameščeno različico .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Potrebno za avtentikacijo. Namestite ga iz [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure naročnina** — Za dostop do Microsoft Foundry in Azure AI Agent Service.
- **Microsoft Foundry projekt** — Projekt z nameščenim modelom (npr. `gpt-4o`). Glej [1. korak](#korak-1-ustvarite-microsoft-foundry-projekt) spodaj.

V korenski mapi tega repozitorija smo vključili datoteko `requirements.txt`, ki vsebuje vse potrebne Python pakete za zagon primerov kode.

Namestite jih s tem ukazom v terminalu v korenski mapi repozitorija:

```bash|powershell
pip install -r requirements.txt
```

Priporočamo, da ustvarite Python virtualno okolje, da se izognete konfliktom in težavam.

## Nastavite VSCode

Prepričajte se, da uporabljate pravo različico Pythona v VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavitev Microsoft Foundry in Azure AI Agent Service

### Korak 1: Ustvarite Microsoft Foundry projekt

Za zagon zvezkov potrebujete Azure AI Foundry **hub** in **projekt** z nameščenim modelom.

1. Pojdite na [ai.azure.com](https://ai.azure.com) in se prijavite s svojim Azure računom.
2. Ustvarite **hub** (ali uporabite že obstoječega). Glej: [Pregled virov huba](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Znotraj huba ustvarite **projekt**.
4. Namestite model (npr. `gpt-4o`) preko **Models + Endpoints** → **Deploy model**.

### Korak 2: Pridobite naslov končne točke in ime izdaje modela vašega projekta

Iz vašega projekta v Microsoft Foundry portalu:

- **Naslov končne točke projekta** — Pojdite na stran **Pregled** in kopirajte URL končne točke.

![Project Connection String](../../../translated_images/sl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Ime izdaje modela** — Pojdite na **Models + Endpoints**, izberite vaš nameščeni model in zabeležite **Deployment name** (npr. `gpt-4o`).

### Korak 3: Prijavite se v Azure z `az login`

Vsi zvezki uporabljajo **`AzureCliCredential`** za avtentikacijo — ni treba upravljati z API ključi. To zahteva, da ste prijavljeni preko Azure CLI.

1. **Namestite Azure CLI**, če še nimate: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prijavite se** z zagonom:

    ```bash|powershell
    az login
    ```

    Ali če ste v oddaljenem/Codespace okolju brez brskalnika:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Izberite vašo naročnino**, če vas to vpraša — izberite tisto, ki vsebuje vaš Foundry projekt.

4. **Preverite**, da ste prijavljeni:

    ```bash|powershell
    az account show
    ```

> **Zakaj `az login`?** Zvezki avtenticirajo z `AzureCliCredential` iz paketa `azure-identity`. To pomeni, da vaša Azure CLI seja zagotavlja poverilnice — brez API ključev ali skrivnosti v vaši `.env` datoteki. To je [najboljša varnostna praksa](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Korak 4: Ustvarite vašo `.env` datoteko

Kopirajte primer datoteke:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Odprite `.env` in izpolnite ti dve vrednosti:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Spremenljivka | Kje jo najdete |
|--------------|----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → vaš projekt → stran **Pregled** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → ime vaše izdaje modela |

To je vse za večino lekcij! Zvezki se bodo samodejno avtenticirali preko vaše `az login` seje.

### Korak 5: Namestite Python odvisnosti

```bash|powershell
pip install -r requirements.txt
```

Priporočamo, da to zaženete znotraj virtualnega okolja, ki ste ga prej ustvarili.

## Dodatna nastavitev za Lekcijo 5 (Agentic RAG)

Lekcija 5 uporablja **Azure AI Search** za generacijo z izboljšanim iskanjem. Če nameravate zagnati to lekcijo, dodajte te spremenljivke v vašo `.env` datoteko:

| Spremenljivka | Kje jo najdete |
|---------------|----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → vaš **Azure AI Search** vir → **Pregled** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → vaš **Azure AI Search** vir → **Nastavitve** → **Ključi** → primarni administratorski ključ |

## Dodatna nastavitev za Lekciji 6 in 8 (GitHub modeli)

Nekateri zvezki v lekcijah 6 in 8 uporabljajo **GitHub modele** namesto Azure AI Foundry. Če nameravate zagnati te vzorce, dodajte te spremenljivke v vašo `.env` datoteko:

| Spremenljivka | Kje jo najdete |
|---------------|----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Uporabite `https://models.inference.ai.azure.com` (privzeta vrednost) |
| `GITHUB_MODEL_ID` | Ime modela, ki ga želite uporabiti (npr. `gpt-4o-mini`) |

## Alternativni ponudnik: MiniMax (združljiv z OpenAI)

[MiniMax](https://platform.minimaxi.com/) nudi modele za velike kontekste (do 204K tokenov) preko API-ja, združljivega z OpenAI. Ker Microsoft Agent Frameworkov `OpenAIChatClient` deluje z vsakim endpointom, združljivim z OpenAI, lahko MiniMax uporabljate kot alternativo GitHub modelom ali OpenAI.

Dodajte te spremenljivke v vašo `.env` datoteko:

| Spremenljivka | Kje jo najdete |
|---------------|----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API ključi |
| `MINIMAX_BASE_URL` | Uporabite `https://api.minimax.io/v1` (privzeta vrednost) |
| `MINIMAX_MODEL_ID` | Ime modela za uporabo (npr. `MiniMax-M3`) |

**Primer modeli**: `MiniMax-M3` (priporočeno), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (hitrejši odgovori). Imena in razpoložljivost modelov se lahko skozi čas spreminjata, dostop do določenega modela pa je lahko odvisen od vašega računa ali regije — preverite [MiniMax Platform](https://platform.minimaxi.com/) za aktualni seznam. Če `MiniMax-M3` ni na voljo za vaš račun, nastavite `MINIMAX_MODEL_ID` na model, do katerega imate dostop (npr. `MiniMax-M2.7`).

Primeri kode, ki uporabljajo `OpenAIChatClient` (npr. Lekcija 14 hotelski delovni tok) bodo samodejno zaznali in uporabili vašo MiniMax konfiguracijo, ko je nastavljena spremenljivka `MINIMAX_API_KEY`.

## Dodatna nastavitev za Lekcijo 8 (Bing integracijski delovni tok)

Pogojni delovni tok v lekciji 8 uporablja **Bing integracijo** prek Azure AI Foundry. Če nameravate zagnati ta vzorec, dodajte to spremenljivko v vašo `.env` datoteko:

| Spremenljivka | Kje jo najdete |
|---------------|----------------|
| `BING_CONNECTION_ID` | Portal Azure AI Foundry → vaš projekt → **Management** → **Connected resources** → vaša Bing povezava → kopirajte ID povezave |

## Odpravljanje težav

### Napake ob preverjanju SSL certifikatov na macOS

Če uporabljate macOS in naletite na napako, kot je:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

To je poznana težava pri Pythonu na macOS, kjer sistemski SSL certifikati niso samodejno zaupanja vredni. Poskusite naslednje rešitve po vrstnem redu:

**Možnost 1: Zaženite Pythonov skript za namestitev certifikatov (priporočeno)**

```bash
# Zamenjajte 3.XX z vašo nameščeno različico Pythona (npr. 3.12 ali 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnost 2: Uporabite `connection_verify=False` v vašem zvezku (samo za GitHub modele)**

V lekciji 6 zvezku (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je že vključen zakomentiran popravek. Odkomentirajte `connection_verify=False` pri ustvarjanju klienta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Onemogoči preverjanje SSL, če naletiš na napake s certifikati
)
```

> **⚠️ Opozorilo:** Onemogočanje SSL preverjanja (`connection_verify=False`) zmanjša varnost, ker preskoči preverjanje certifikata. Uporabljajte to le kot začasno rešitev v razvojnih okoljih, nikoli v produkciji.

**Možnost 3: Namestite in uporabite `truststore`**

```bash
pip install truststore
```

Nato dodajte naslednje na začetek zvezka ali skripta pred izvajanjem omrežnih klicev:

```python
import truststore
truststore.inject_into_ssl()
```

## Se zataknete?

Če imate kakršne koli težave z zagonom te nastavitve, pridružite se našemu <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ali <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ustvarite issue</a>.
## Naslednja lekcija

Zdaj ste pripravljeni zagnati kodo za ta tečaj. Veselo učenje o svetu AI agentov! 

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->