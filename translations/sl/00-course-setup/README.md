# Nastavitev tečaja

## Uvod

Ta lekcija bo prikazala, kako zagnati vzorčne primere kode tega tečaja.

## Pridružite se drugim učečim in pridobite pomoč

Preden začnete klonirati svoj repozitorij, se pridružite [kanalu AI Agents For Beginners Discord](https://aka.ms/ai-agents/discord), da dobite pomoč pri nastavitvi, postavite vprašanja o tečaju ali se povežete z drugimi učečimi.

## Klonirajte ali razvejite ta repozitorij

Za začetek prosimo, klonirajte ali naredite fork GitHub repozitorija. Tako boste imeli svojo različico gradiva tečaja, ki jo lahko zaženete, testirate in prilagajate kodo!

To lahko storite tako, da kliknete povezavo do <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repozitorija</a>

Zdaj bi morali imeti svojo različico tega tečaja na naslednji povezavi:

![Forkan repozitorij](../../../translated_images/sl/forked-repo.33f27ca1901baa6a.webp)

### Površen klon (priporočeno za delavnico / Codespaces)

  >Celoten repozitorij je lahko velik (~3 GB), če prenesete celotno zgodovino in vse datoteke. Če se udeležujete samo delavnice ali potrebujete le nekaj lekcijskih map, površen klon (ali razredčeni klon) prepreči večino prenosa tako, da omeji zgodovino in/ali preskoči blobe.

#### Hitri površen klon — minimalna zgodovina, vse datoteke

Nadomestite `<your-username>` v spodnjih ukazih z URL-jem vašega forka (ali z zgornjim URL-jem, če ga raje uporabite).

Za kloniranje samo zadnje zgodovine commita (majhen prenos):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Za kloniranje določene veje:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delni (razredčeni) klon — minimalni blobi + le izbrane mape

To uporablja delni klon in sparse-checkout (zahteva Git 2.25+ in priporočeno sodoben Git s podporo delnemu klonu):

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

Po kloniranju in preverjanju datotek, če potrebujete samo datoteke in želite sprostiti prostor (brez git zgodovine), prosimo izbrišite metapodatke repozitorija (💀nepopravljivo — izgubili boste vse funkcije Git: brez commitov, pullov, pushov ali dostopa do zgodovine).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Uporaba GitHub Codespaces (priporočeno za izogibanje lokalnim velikim prenosom)

- Ustvarite nov Codespace za ta repozitorij preko [GitHub UI](https://github.com/codespaces).  

- V terminalu novo ustvarjenega Codespace zaženite enega od zgornjih ukazov za površen/razredčeni klon, da prinesete le lekcijske mape, ki jih potrebujete, v workspace Codespace.
- Neobvezno: po kloniranju znotraj Codespaces odstranite .git, da pridobite dodatni prostor (oglejte ukaze za odstranitev zgoraj).
- Opomba: Če raje odprete repozitorij neposredno v Codespaces (brez dodatnega klona), vedite, da Codespaces kliče devcontainer okolje in morda vseeno pripravi več kot potrebujete. Kloniranje plitve kopije znotraj svežega Codespace vam daje več nadzora nad uporabo diska.

#### Nasveti

- Vedno nadomestite URL klona z vašim forkom, če želite urejati/commitati.
- Če boste kasneje potrebovali več zgodovine ali datotek, jih lahko pridobite ali prilagodite sparse-checkout, da vključite dodatne mape.

## Zagon kode

Ta tečaj ponuja serijo Jupyter Beležnic, ki jih lahko zaženete, da pridobite praktične izkušnje z gradnjo AI agentov.

Vzorčni primeri kode uporabljajo **Microsoft Agent Framework (MAF)** z `FoundryChatClient`, ki se poveže z **Microsoft Foundry Agent Service V2** (Responses API) preko **Microsoft Foundry**.

Vse Python beležnice so označene z `*-python-agent-framework.ipynb`.

## Zahteve

- Python 3.12+
  - **OPOMBA**: Če nimate nameščenega Python3.12, ga poskrbite namestiti. Nato ustvarite svoj venv z uporabo python3.12, da zagotovite pravilne različice iz datoteke requirements.txt.
  
    >Primer

    Ustvarite imenik za Python venv:

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

- .NET 10+: Za vzorčne kode, ki uporabljajo .NET, poskrbite, da imate nameščen [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ali novejšo različico. Nato preverite nameščeno različico .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Zahtevano za avtentikacijo. Namestite z [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure naročnina** — Za dostop do Microsoft Foundry in Microsoft Foundry Agent Service.
- **Microsoft Foundry projekt** — Projekt z nameščenim modelom (npr. `gpt-5-mini`). Glejte [Korak 1](#korak-1-ustvarite-microsoft-foundry-projekt) spodaj.

Vključen imamo `requirements.txt` datoteko v korenu tega repozitorija, ki vsebuje vse zahtevane Python pakete za zagon vzorčnih primerov kode.

Lahko jih namestite z zagonom naslednjega ukaza v terminalu v korenu repozitorija:

```bash|powershell
pip install -r requirements.txt
```

Priporočamo, da ustvarite Python virtualno okolje, da se izognete morebitnim konfliktom in težavam.

## Nastavitev VSCode

Poskrbite, da uporabljate pravo različico Pythona v VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavite Microsoft Foundry in Microsoft Foundry Agent Service

### Korak 1: Ustvarite Microsoft Foundry projekt

Potrebujete Microsoft Foundry **hub** in **projekt** z nameščenim modelom za zagon beležnic.

1. Pojdite na [ai.azure.com](https://ai.azure.com) in se prijavite s svojim Azure računom.
2. Ustvarite **hub** (ali uporabite obstoječega). Glejte: [Pregled virov Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Znotraj huba ustvarite **projekt**.
4. Namestite model (npr. `gpt-5-mini`) iz **Models + Endpoints** → **Deploy model**.

### Korak 2: Pridobite URL projekta in ime nameščanja modela

Iz vašega projekta v Microsoft Foundry portalu:

- **Project Endpoint** — Obiščite stran **Overview** in kopirajte URL endpointa.

![Povezava projekta](../../../translated_images/sl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Pojdite na **Models + Endpoints**, izberite nameščeni model in zapišite **Deployment name** (npr. `gpt-5-mini`).

### Korak 3: Prijavite se v Azure z `az login`

Vse beležnice uporabljajo **`AzureCliCredential`** za avtentikacijo — ni potrebnih API ključev. Potrebno se je prijaviti preko Azure CLI.

1. **Namestite Azure CLI**, če ga še nimate: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prijavite se** z zagonom:

    ```bash|powershell
    az login
    ```

    Ali če ste v oddaljenem/Codespace okolju brez brskalnika:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Izberite naročnino**, če vas sistem vpraša — izberite tisto, ki vsebuje vaš Foundry projekt.

4. **Preverite**, da ste prijavljeni:

    ```bash|powershell
    az account show
    ```

> **Zakaj `az login`?** Beležnice se avtenticirajo z uporabo `AzureCliCredential` iz paketa `azure-identity`. To pomeni, da vaša Azure CLI seja zagotavlja poverilnice — ni potrebnih API ključev ali skrivnosti v datoteki `.env`. To je [najboljša varnostna praksa](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Korak 4: Ustvarite svojo `.env` datoteko

Kopirajte vzorčno datoteko:

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → vaš projekt → stran **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → ime vašega nameščenega modela |

To je vse za večino lekcij! Beležnice se bodo samodejno avtenticirale preko vaše `az login` seje.

### Korak 5: Namestite Python odvisnosti

```bash|powershell
pip install -r requirements.txt
```

Priporočamo, da to zaženete znotraj virtualnega okolja, ki ste ga ustvarili prej.

## Dodatna nastaviti za Lekcijo 5 (Agentic RAG)

Lekcija 5 uporablja **Azure AI Search** za generacijo z izboljšanim iskanjem. Če načrtujete zagon te lekcije, dodajte te spremenljivke v svojo `.env` datoteko:

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → vaš **Azure AI Search** vir → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → vaš **Azure AI Search** vir → **Settings** → **Keys** → primarni adminski ključ |

## Dodatna nastaviti za lekcije, ki neposredno kličejo Azure OpenAI (Lekcija 6 in 8)

Nekatere beležnice v lekcijah 6 in 8 neposredno kličejo **Azure OpenAI** (uporabljajoč **Responses API**) namesto Microsoft Foundry projekta. Ti vzorci so prej uporabljali GitHub Models, ki je zastarel (se upokojuje julija 2026) in ne podpira Responses API. Če želite zagnati te vzorce, dodajte te spremenljivke v svojo `.env` datoteko:

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → vaš **Azure OpenAI** vir → **Keys and Endpoint** → Endpoint (npr. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Ime nameščenega modela (npr. `gpt-5-mini`) ki podpira Responses API |
| `AZURE_OPENAI_API_KEY` | Neobvezno — samo, če uporabljate avtentikacijo z ključem namesto `az login` / Entra ID |

> Responses API uporablja stabilen `/openai/v1/` endpoint, zato ni potrebno `api-version`. Prijavite se z `az login`, da uporabljate avtentikacijo brez ključa z Entra ID.

## Alternativni ponudnik: MiniMax (Združljiv z OpenAI)

[MiniMax](https://platform.minimaxi.com/) ponuja modele s velikim kontekstom (do 204K tokenov) preko API združljivega z OpenAI. Ker Microsoft Agent Framework `OpenAIChatClient` deluje z vsakim endpointom združljivim z OpenAI, lahko uporabite MiniMax kot direktno alternativo Azure OpenAI ali OpenAI.

Dodajte te spremenljivke v svojo `.env` datoteko:

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API ključi |
| `MINIMAX_BASE_URL` | Uporabite `https://api.minimax.io/v1` (privzeta vrednost) |
| `MINIMAX_MODEL_ID` | Ime modela za uporabo (npr. `MiniMax-M3`) |

**Primeri modelov**: `MiniMax-M3` (priporočeno), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (hitrejši odgovori). Imena modelov in razpoložljivost se lahko skozi čas spreminjata, dostop do posameznega modela pa je lahko odvisen od vašega računa ali regije — preverite [MiniMax Platformo](https://platform.minimaxi.com/) za aktualni seznam. Če `MiniMax-M3` ni na voljo za vaš račun, nastavite `MINIMAX_MODEL_ID` na model, do katerega imate dostop (npr. `MiniMax-M2.7`).

Vzorčni primeri kode, ki uporabljajo `OpenAIChatClient` (npr. Lekcija 14 delovni tok za rezervacijo hotela), bodo samodejno zaznali in uporabili vašo MiniMax konfiguracijo, ko je nastavljen `MINIMAX_API_KEY`.

## Alternativni ponudnik: Foundry Local (Zagon modelov na napravi)

[Foundry Local](https://foundrylocal.ai) je lahek runtime, ki prenaša, upravlja in streže jezikovne modele **popolnoma na vaši napravi** preko API-ja združljivega z OpenAI — brez oblaka, brez Azure naročnine in brez API ključev. Odlična možnost za razvoj brez povezave, eksperimentiranje brez oblačnih stroškov ali hranjenje podatkov na sami napravi.

Ker Microsoft Agent Framework `OpenAIChatClient` deluje z vsakim endpointom združljivim z OpenAI, je Foundry Local lokalna alternativa Azure OpenAI.

**1. Namestite Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Prenesite in zaženite model** (to tudi zažene lokalno storitev):

```bash
foundry model list          # glej razpoložljive modele
foundry model run phi-4-mini
```

**3. Namestite Python SDK** za odkrivanje lokalnega endpointa:

```bash
pip install foundry-local-sdk
```

**4. Usmerite Microsoft Agent Framework na vaš lokalni model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Prenese (če je potrebno) in streže model lokalno, nato odkrije končno točko/vrata.
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

> **Opomba:** Foundry Local izpostavlja OpenAI združljiv **Chat Completions** endpoint. Uporabite ga za lokalni razvoj in offline scenarije. Za celoten nabor funkcij **Responses API** (državne pogovore, globoko orkestracijo orodij in razvoj v slogu agenta) uporabite **Azure OpenAI** ali **Microsoft Foundry** projekt, kot je prikazano v lekcijah. Glejte [Foundry Local dokumentacijo](https://foundrylocal.ai) za aktualni katalog modelov in podporo platforme.

## Dodatna nastaviti za Lekcijo 8 (Bing Grounding Workflow)


Zvezni delovni zvezek iz 8. lekcije uporablja **Bing grounding** preko Microsoft Foundry. Če nameravate zagnati ta primer, dodajte to spremenljivko v svojo datoteko `.env`:

| Spremenljivka | Kje jo najti |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → vaš projekt → **Upravljanje** → **Povezani viri** → vaša Bing povezava → kopirajte ID povezave |

## Reševanje težav

### Napake preverjanja SSL potrdila na macOS

Če ste na macOS in naletite na napako, kot je:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

To je znana težava s Pythonom na macOS, kjer sistemska SSL potrdila niso samodejno zaupanja vredna. Preizkusite naslednje rešitve po vrsti:

**Možnost 1: Zaženite skripto Install Certificates za Python (priporočeno)**

```bash
# Zamenjajte 3.XX z vašo nameščeno različico Pythona (npr., 3.12 ali 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Možnost 2: V svojem zvezku uporabite `connection_verify=False` (samo za GitHub Models zvezke)**

V zvezku Lekcije 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je že vključen zakomentiran zaobidni ukrep. Odkomentirajte `connection_verify=False` pri ustvarjanju odjemalca:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Onemogoči preverjanje SSL, če naletiš na napake s potrdilom
)
```

> **⚠️ Opozorilo:** Onemogočanje SSL preverjanja (`connection_verify=False`) zmanjša varnost s tem, da preskoči preverjanje potrdila. To uporabite samo kot začasno rešitev v razvojnih okoljih, nikoli v produkciji.

**Možnost 3: Namestite in uporabite `truststore`**

```bash
pip install truststore
```

Nato dodajte naslednje na začetek svojega zvezka ali skripte pred kakršnim koli omrežnim klicem:

```python
import truststore
truststore.inject_into_ssl()
```

## Ste kje obstali?

Če imate kakršnekoli težave z zagonom te nastavitve, se pridružite naši <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord skupnosti Azure AI</a> ali <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ustvarite težavo</a>.

## Naslednja lekcija

Zdaj ste pripravljeni zagnati kodo za ta tečaj. Veselo učenje o svetu AI agentov!

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->