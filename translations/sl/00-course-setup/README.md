# Nastavitev tečaja

## Uvod

Ta lekcija bo zajemala, kako zagnati vzorce kode iz tega tečaja.

## Pridružite se drugim učencem in poiščite pomoč

Preden začnete klonirati vaš repozitorij, se pridružite [kanalu AI Agents For Beginners na Discordu](https://aka.ms/ai-agents/discord), da dobite pomoč pri nastavitvi, odgovore na vprašanja o tečaju ali za povezavo z drugimi učenci.

## Kloniranje ali forkanje tega repozitorija

Za začetek prosimo klonirajte ali forknite GitHub repozitorij. Tako boste imeli svojo verzijo gradiva tečaja, da lahko zaženete, testirate in prilagajate kodo!

To lahko storite tako, da kliknete povezavo <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a>

Sedaj bi morali imeti svojo forknjeno verzijo tega tečaja na naslednji povezavi:

![Forked Repo](../../../translated_images/sl/forked-repo.33f27ca1901baa6a.webp)

### Površinsko kloniranje (priporočeno za delavnico / Codespaces)

  >Celoten repozitorij je lahko velik (~3 GB), če prenesete celotno zgodovino in vse datoteke. Če boste obiskovali le delavnico ali potrebujete le nekaj map z lekcijami, površinsko kloniranje (ali redko kloniranje) prepreči večino prenosa tako, da skrajša zgodovino in/ali preskoči binarne podatke.

#### Hitro površinsko kloniranje — minimalna zgodovina, vse datoteke

V spodnjih ukazih nadomestite `<your-username>` z URL-jem vašega forka (ali z zgornjim URL-jem, če želite).

Za kloniranje samo najnovejše zgodovine commitov (majhen prenos):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Za kloniranje določenega vejice:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delno (redko) kloniranje — minimalni blobi + samo izbrane mape

To uporablja delno kloniranje in sparse-checkout (zahteva Git 2.25+ in priporočen sodoben Git z delnim kloniranjem):

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

Po kloniranju in preverjanju datotek, če potrebujete le datoteke in želite sprostiti prostor (brez git zgodovine), prosim izbrišite metapodatke repozitorija (💀nevratno — izgubili boste vso Git funkcionalnost: brez commitov, pullov, pushov ali dostopa do zgodovine).

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

- V terminalu novoustanovljenega Codespace-a poženite enega izmed ukazov za površinsko/redko kloniranje zgoraj, da pripeljete samo potrebne mape lekcij v Codespace okolje.
- Izbirno: po kloniranju znotraj Codespaces odstranite .git, da sprostite dodatni prostor (glejte ukaze za odstranjevanje zgoraj).
- Opomba: Če želite repozitorij odpreti neposredno v Codespaces (brez dodatnega kloniranja), vedite, da bo Codespaces pripravil razvojno okolje in lahko še vedno pripravi več, kot potrebujete. Kloniranje površinske kopije znotraj svežega Codespace-a vam daje več nadzora nad uporabo diska.

#### Nasveti

- Vedno zamenjajte URL klona z vašim forkom, če želite urejati/commitati.
- Če kasneje potrebujete več zgodovine ali datotek, jih lahko pridobite ali prilagodite sparse-checkout, da vključite dodatne mape.

## Zagon kode

Ta tečaj ponuja serijo Jupyter Notesnikov, ki jih lahko zaženete za praktične izkušnje z gradnjo AI agentov.

Vzorce kode uporabljajo **Microsoft Agent Framework (MAF)** z `FoundryChatClient`, ki se povezuje na **Microsoft Foundry Agent Service V2** (Responses API) prek **Microsoft Foundry**.

Vsi Python notesniki so označeni z `*-python-agent-framework.ipynb`.

## Zahteve

- Python 3.12+
  - **OPOMBA**: Če nimate nameščenega Python3.12, ga namestite. Nato ustvarite vaš venv z uporabo python3.12, da zagotovite pravilne različice iz datoteke requirements.txt.
  
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

- .NET 10+: Za vzorce kode, ki uporabljajo .NET, poskrbite, da imate nameščen [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ali novejši. Nato preverite nameščeno različico .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Potrebno za avtentikacijo. Namestite s [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure naročnina** — Za dostop do Microsoft Foundry in Microsoft Foundry Agent Service.
- **Microsoft Foundry projekt** — Projekt z nameščenim modelom (npr. `gpt-4.1-mini`). Glej [Korak 1](#korak-1-ustvarite-microsoft-foundry-projekt) spodaj.

Vključili smo datoteko `requirements.txt` v korenu tega repozitorija, ki vsebuje vse potrebne Python pakete za zagon vzorcev kode.

Namestite jih lahko z zagonom naslednjega ukaza v terminalu v korenski mapi repozitorija:

```bash|powershell
pip install -r requirements.txt
```

Priporočamo ustvarjanje virtualnega Python okolja, da se izognete konfliktom in težavam.

## Nastavitev VSCode

Prepričajte se, da uporabljate pravo različico Pythona v VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavitev Microsoft Foundry in Microsoft Foundry Agent Service

### Korak 1: Ustvarite Microsoft Foundry projekt

Potrebujete Microsoft Foundry **hub** in **projekt** z nameščenim modelom za zagon notesnikov.

1. Obiščite [ai.azure.com](https://ai.azure.com) in se prijavite z vašim Azure računom.
2. Ustvarite **hub** (ali uporabite obstoječega). Glejte: [Pregled virov hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Znotraj huba ustvarite **projekt**.
4. Namestite model (npr. `gpt-4.1-mini`) iz **Models + Endpoints** → **Deploy model**.

### Korak 2: Pridobite URL projekta in ime nameščenega modela

Iz vašega projekta v Microsoft Foundry portalu:

- **URL projekta** — Pojdite na stran **Overview** in kopirajte URL.

![Project Connection String](../../../translated_images/sl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Ime nameščenega modela** — Pojdite na **Models + Endpoints**, izberite vaš nameščeni model in zabeležite **Ime nameščanja** (npr. `gpt-4.1-mini`).

### Korak 3: Prijavite se v Azure z `az login`

Vsi notesniki uporabljajo **`AzureCliCredential`** za avtentikacijo — ni potrebe po upravljanju API ključev. To zahteva, da ste prijavljeni preko Azure CLI.

1. **Namestite Azure CLI**, če ga še nimate: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prijavite se** z zagonom:

    ```bash|powershell
    az login
    ```

    Ali če ste v oddaljenem/Codespace okolju brez brskalnika:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Izberite vašo naročnino**, če ste pozvani — izberite tisto, ki vsebuje vaš Foundry projekt.

4. **Preverite**, da ste prijavljeni:

    ```bash|powershell
    az account show
    ```

> **Zakaj `az login`?** Notesniki avtenticirajo z uporabo `AzureCliCredential` iz paketa `azure-identity`. To pomeni, da vaša Azure CLI seja zagotavlja poverilnice — brez API ključev ali skrivnosti v vaši `.env` datoteki. To je [najboljša varnostna praksa](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Korak 4: Ustvarite vašo `.env` datoteko

Kopirajte vzorčno datoteko:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Odprite `.env` in vnesite vrednosti za ti dve spremenljivki:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Spremenljivka | Kje jo najdete |
|--------------|---------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → vaš projekt → stran **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → ime vašega nameščenega modela |

To je vse za večino lekcij! Notesniki se bodo avtomatsko avtenticirali preko vaše seje `az login`.

### Korak 5: Namestite Python odvisnosti

```bash|powershell
pip install -r requirements.txt
```

Priporočamo, da to zaženete znotraj virtualnega okolja, ki ste ga prej ustvarili.

## Dodatna nastavitev za Lekcijo 5 (Agentic RAG)

Lekcija 5 uporablja **Azure AI Search** za generiranje z iskanjem. Če nameravate zagnati to lekcijo, dodajte te spremenljivke v vašo `.env` datoteko:

| Spremenljivka | Kje jo najdete |
|--------------|---------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → vaš **Azure AI Search** vir → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → vaš **Azure AI Search** vir → **Settings** → **Keys** → primarni administratorski ključ |

## Dodatna nastavitev za lekcije, ki kličejo Azure OpenAI neposredno (Lekcije 6 in 8)

Nekateri notesniki v lekcijah 6 in 8 kličejo **Azure OpenAI** neposredno (prek **Responses API**), namesto preko Microsoft Foundry projekta. Ti vzorci so prej uporabljali GitHub Models, ki je zastarel (upokojen julija 2026) in ne podpira Responses API-ja. Če želite zagnati te vzorce, dodajte te spremenljivke v vašo `.env` datoteko:

| Spremenljivka | Kje jo najdete |
|--------------|---------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → vaš **Azure OpenAI** vir → **Keys and Endpoint** → Endpoint (npr. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Ime vašega nameščenega modela (npr. `gpt-4.1-mini`), ki podpira Responses API |
| `AZURE_OPENAI_API_KEY` | Izbirno — samo če uporabljate avtentikacijo z uporabo ključa namesto `az login` / Entra ID |

> Responses API uporablja stabilni `/openai/v1/` endpoint, zato ni potrebe po `api-version`. Prijavite se z `az login` za uporabo brezključne avtentikacije Entra ID.

## Alternativni ponudnik: MiniMax (združljiv z OpenAI)

[MiniMax](https://platform.minimaxi.com/) nudi modele z dolgim kontekstom (do 204K tokenov) preko API-ja združljivega z OpenAI. Ker Microsoft Agent Framework `OpenAIChatClient` deluje z vsakim OpenAI združljivim endpointom, lahko MiniMax uporabljate kot vstavno alternativo Azure OpenAI ali OpenAI.

Dodajte te spremenljivke v vašo `.env` datoteko:

| Spremenljivka | Kje jo najdete |
|--------------|---------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API ključi |
| `MINIMAX_BASE_URL` | Uporabite `https://api.minimax.io/v1` (privzeto vrednost) |
| `MINIMAX_MODEL_ID` | Ime modela za uporabo (npr. `MiniMax-M3`) |

**Primer modelov**: `MiniMax-M3` (priporočeno), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (hitrejši odzivi). Imena modelov in razpoložljivost se lahko s časom spreminjajo in dostop do določenega modela je lahko odvisen od vašega računa ali regije — preverite [MiniMax Platform](https://platform.minimaxi.com/) za aktualni seznam. Če vam `MiniMax-M3` ni na voljo, nastavite `MINIMAX_MODEL_ID` na model, do katerega imate dostop (npr. `MiniMax-M2.7`).

Vzorci kode, ki uporabljajo `OpenAIChatClient` (npr. delovni tok rezervacije hotela v Lekciji 14) bodo samodejno zaznali in uporabili vašo MiniMax konfiguracijo, ko je nastavljen `MINIMAX_API_KEY`.

## Alternativni ponudnik: Foundry Local (zaganjajte modele na napravi)

[Foundry Local](https://foundrylocal.ai) je lahko runtim, ki prenese, upravlja in streže jezikovne modele **v celoti na vašem računalniku** preko OpenAI združljivega API-ja — brez oblaka, brez Azure naročnine, brez API ključev. Odlična izbira za offline razvoj, preizkušanje brez stroškov oblaka ali hranjenje podatkov lokalno.

Ker Microsoft Agent Framework `OpenAIChatClient` deluje z vsakim OpenAI združljivim endpointom, je Foundry Local lokalna alternativa Azure OpenAI.

**1. Namestite Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Prenesite in zaženite model** (to tudi zažene lokalno storitev):

```bash
foundry model list          # oglejte si razpoložljive modele
foundry model run phi-4-mini
```

**3. Namestite Python SDK**, ki se uporablja za odkrivanje lokalnega endpointa:

```bash
pip install foundry-local-sdk
```

**4. Povežite Microsoft Agent Framework na vaš lokalni model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Prenese (če je potrebno) in lokalno postreže model, nato odkrije končno točko/vrata.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # npr. http://localhost:<port>/v1
    api_key=manager.api_key,        # vedno "ni potrebno" za Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Opomba:** Foundry Local izpostavlja OpenAI združljiv **Chat Completions** endpoint. Uporabite ga za lokalni razvoj in offline scenarije. Za poln nabor funkcij **Responses API** (statvoer pogovori, globoka orodna orkestracija in razvoj z agentnim slogom) ciljate na **Azure OpenAI** ali **Microsoft Foundry** projekt, kot je prikazano v lekcijah. Glejte [Foundry Local dokumentacijo](https://foundrylocal.ai) za trenutni katalog modelov in podporo platforme.


## Dodatna nastavitev za lekcijo 8 (Bing Grounding Workflow)

Zvezni delovni zvezek v lekciji 8 uporablja **Bing grounding** preko Microsoft Foundry. Če nameravate zagnati ta primer, dodajte to spremenljivko v vašo `.env` datoteko:

| Spremenljivka | Kje jo najti |
|--------------|-------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → vaš projekt → **Upravljanje** → **Povezani viri** → vaša Bing povezava → kopirajte ID povezave |

## Odpravljanje težav

### Napake pri preverjanju SSL certifikata na macOS

Če ste na macOS in naletite na napako, kot je:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

To je znana težava s Pythonom na macOS-ju, kjer sistemski SSL certifikati niso samodejno zaupanja vredni. Poskusite naslednje rešitve v tem zaporedju:

**Možnost 1: Zaženite skripto za namestitev certifikatov v Pythonu (priporočeno)**

```bash
# Zamenjajte 3.XX z vašo nameščeno različico Pythona (npr. 3.12 ali 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnost 2: Uporabite `connection_verify=False` v vašem zvezku (samo za GitHub Models zvezke)**

V zvezku lekcije 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je že vključen komentiran obvoz. Odkomentirajte `connection_verify=False` ob ustvarjanju odjemalca:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Onemogoči preverjanje SSL, če naletiš na napake certifikata
)
```

> **⚠️ Opozorilo:** Onemogočanje SSL preverjanja (`connection_verify=False`) zmanjša varnost, saj preskoči preverjanje certifikata. To uporabite le kot začasno rešitev v razvojnih okoljih, nikoli v produkciji.

**Možnost 3: Namestite in uporabite `truststore`**

```bash
pip install truststore
```

Nato dodajte naslednje na začetek vašega zvezka ali skripte pred izvajanjem kateregakoli omrežnega klica:

```python
import truststore
truststore.inject_into_ssl()
```

## Ste se zataknili?

Če imate težave pri zagonu te nastavitve, se pridružite našemu <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ali <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ustvarite težavo</a>.

## Naslednja lekcija

Sedaj ste pripravljeni, da zaženete kodo za ta tečaj. Veselo učenje o svetu AI agentov! 

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->