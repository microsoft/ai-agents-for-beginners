# Postavljanje tečaja

## Uvod

Ova lekcija će obuhvatiti kako pokrenuti primjere koda ovog tečaja.

## Pridruži se drugim polaznicima i zatraži pomoć

Prije nego što počneš klonirati svoj repozitorij, pridruži se [AI Agents For Beginners Discord kanalu](https://aka.ms/ai-agents/discord) da dobiješ pomoć oko postavljanja, postaviš pitanja o tečaju ili se povežeš s drugim polaznicima.

## Kloniraj ili forkuj ovaj repozitorij

Za početak, molimo te da kloniraš ili forkaš GitHub repozitorij. To će ti omogućiti vlastitu verziju materijala tečaja kako bi mogao pokretati, testirati i prilagođavati kod!

To možeš učiniti klikom na poveznicu za <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repozitorija</a>

Sada bi trebao imati svoju forkanu verziju ovog tečaja na sljedećoj poveznici:

![Forked Repo](../../../translated_images/hr/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (preporučeno za radionicu / Codespaces)

  >Cijeli repozitorij može biti velik (~3 GB) kada se preuzima puna povijest i sve datoteke. Ako pohađaš samo radionicu ili trebaš samo nekoliko fascikli sa lekcijama, plitki clone (ili sparse clone) izbjegava većinu tog preuzimanja skraćivanjem povijesti i/ili preskakanjem blob-ova.

#### Brzi plitki clone — minimalna povijest, sve datoteke

Zamijeni `<your-username>` u donjim naredbama s URL-om tvog forka (ili upstream URL-om ako više voliš).

Za kloniranje samo najnovije povijesti commit-a (malo preuzimanje):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Za kloniranje određene grane:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Djelomični (sparse) clone — minimalni blobovi + samo odabrane fascikle

Ovo koristi partial clone i sparse-checkout (zahtijeva Git 2.25+ i preporučuje se moderna verzija Gita s podrškom za partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Uđi u mapu repozitorija:

```bash|powershell
cd ai-agents-for-beginners
```

Zatim specificiraj koje fascikle želiš (primjer ispod pokazuje dvije fascikle):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Nakon kloniranja i provjere datoteka, ako ti trebaju samo datoteke i želiš osloboditi prostor (bez povijesti git-a), izbriši metadata repozitorija (💀nepovratno — izgubit ćeš svu Git funkcionalnost: nema commit-ova, pull-ova, push-ova niti pristupa povijesti).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Korištenje GitHub Codespaces (preporučeno da se izbjegnu lokalna velika preuzimanja)

- Kreiraj novi Codespace za ovaj repozitorij preko [GitHub UI](https://github.com/codespaces).  

- U terminalu novokreiranog codespace-a pokreni jednu od gore navedenih shallow/sparse clone naredbi da u Codespace workspace dovedete samo fascikle lekcija koje trebate.
- Opcionalno: nakon kloniranja unutar Codespaces, ukloni .git za vraćanje dodatnog prostora (pogledaj naredbe za uklanjanje gore).
- Napomena: Ako radije otvoriš repozitorij direktno u Codespaces (bez dodatnog kloniranja), budi svjestan da Codespaces konstruira devcontainer okruženje i može i dalje pripremiti više nego što ti treba. Kloniranje plitke kopije unutar novog Codespace-a daje ti veću kontrolu nad korištenjem diska.

#### Savjeti

- Uvijek zamijeni URL za kloniranje URL-om svog forka ako želiš uređivati/commit-ati.
- Ako kasnije trebaš više povijesti ili datoteka, možeš ih dohvatiti ili prilagoditi sparse-checkout da uključi dodatne fascikle.

## Pokretanje koda

Ovaj tečaj nudi niz Jupyter bilježnica koje možeš pokretati za praktično iskustvo u izradi AI agenata.

Primjeri koda koriste **Microsoft Agent Framework (MAF)** s `FoundryChatClient` koji se povezuje na **Microsoft Foundry Agent Service V2** (Responses API) kroz **Microsoft Foundry**.

Sve Python bilježnice su označene kao `*-python-agent-framework.ipynb`.

## Zahtjevi

- Python 3.12+
  - **NAPOMENA**: Ako nemaš instaliran Python3.12, osiguraj da ga instaliraš. Zatim kreiraj svoj virtualni environment koristeći python3.12 kako bi osigurao/la da su točne verzije instalirane iz requirements.txt datoteke.
  
    >Primjer

    Kreiraj Python venv direktorij:

    ```bash|powershell
    python -m venv venv
    ```

    Zatim aktiviraj venv okruženje za:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Za primjere koda koji koriste .NET, osiguraj da instaliraš [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ili noviji. Zatim provjeri verziju instaliranog .NET SDK-a:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Potreban za autentifikaciju. Instaliraj sa [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure pretplata** — Za pristup Microsoft Foundry i Microsoft Foundry Agent Service.
- **Microsoft Foundry projekt** — Projekt s implementiranim modelom (npr. `gpt-5-mini`). Pogledaj [Korak 1](#korak-1-kreiraj-microsoft-foundry-projekt) dolje.

Uključili smo datoteku `requirements.txt` u korijen ovog repozitorija koja sadrži sve potrebne Python pakete za pokretanje primjera koda.

Možeš ih instalirati pokretanjem sljedeće naredbe u terminalu u korijenu repozitorija:

```bash|powershell
pip install -r requirements.txt
```

Preporučujemo kreiranje Python virtualnog okruženja kako bi izbjegao/la konflikte i probleme.

## Postavljanje VSCode

Provjeri da koristiš ispravnu verziju Pythona u VSCode-u.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Postavljanje Microsoft Foundry i Microsoft Foundry Agent Service

### Korak 1: Kreiraj Microsoft Foundry projekt

Trebaš Microsoft Foundry **hub** i **projekt** s implementiranim modelom da bi pokrenuo/la bilježnice.

1. Idi na [ai.azure.com](https://ai.azure.com) i prijavi se sa svojim Azure računom.
2. Kreiraj **hub** (ili koristi postojeći). Pogledaj: [Pregled resursa hub-a](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Unutar huba kreiraj **projekt**.
4. Implementiraj model (npr. `gpt-5-mini`) iz **Models + Endpoints** → **Deploy model**.

### Korak 2: Dohvati Endpoint projekta i naziv implementacije modela

Iz svog projekta u Microsoft Foundry portalu:

- **Endpoint projekta** — Idi na stranicu **Overview** i kopiraj URL endpointa.

![Project Connection String](../../../translated_images/hr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Naziv implementacije modela** — Idi na **Models + Endpoints**, odaberi svoj implementirani model i zabilježi **Deployment name** (npr. `gpt-5-mini`).

### Korak 3: Prijavi se na Azure s `az login`

Sve bilježnice koriste **`AzureCliCredential`** za autentifikaciju — ne trebaš upravljati API ključevima. Ovo zahtijeva da si prijavljen putem Azure CLI.

1. **Instaliraj Azure CLI** ako već nisi: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prijavi se** pokretanjem:

    ```bash|powershell
    az login
    ```

    Ili ako si u udaljenom/Codespace okruženju bez preglednika:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Odaberi svoju pretplatu** ako te to pita — izaberi onu koja sadrži tvoj Foundry projekt.

4. **Provjeri** da si prijavljen:

    ```bash|powershell
    az account show
    ```

> **Zašto `az login`?** Bilježnice se autentificiraju koristeći `AzureCliCredential` iz paketa `azure-identity`. To znači da tvoja Azure CLI sesija osigurava vjerodajnice — nema API ključeva ili tajni u tvojoj `.env` datoteci. Ovo je [sigurnosna preporuka](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Korak 4: Kreiraj svoju `.env` datoteku

Kopiraj primjer datoteke:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Otvori `.env` i ispuni ove dvije vrijednosti:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → tvoj projekt → stranica **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → naziv tvog implementiranog modela |

To je to za većinu lekcija! Bilježnice će se automatski autentificirati kroz tvoju `az login` sesiju.

### Korak 5: Instaliraj Python ovisnosti

```bash|powershell
pip install -r requirements.txt
```

Preporučujemo da ovo pokreneš unutar virtualnog okruženja koje si ranije kreirao/la.

## Dodatno postavljanje za Lekciju 5 (Agentic RAG)

Lekcija 5 koristi **Azure AI Search** za retrieval-augmented generation. Ako planiraš pokrenuti tu lekciju, dodaj ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → tvoj **Azure AI Search** resurs → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → tvoj **Azure AI Search** resurs → **Settings** → **Keys** → primarni administratorski ključ |

## Dodatno postavljanje za lekcije koje direktno zovu Azure OpenAI (Lekcije 6 i 8)

Neke bilježnice u lekcijama 6 i 8 direktno koriste **Azure OpenAI** (koristeći **Responses API**) umjesto da idu preko Microsoft Foundry projekta. Ovi primjerci su prije koristili GitHub modele koji su zastarjeli (ukidaju se u srpnju 2026) i ne podržavaju Responses API. Ako planiraš pokrenuti te primjere, dodaj ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → tvoj **Azure OpenAI** resurs → **Keys and Endpoint** → Endpoint (npr. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Naziv tvog implementiranog modela (npr. `gpt-5-mini`) koji podržava Responses API |
| `AZURE_OPENAI_API_KEY` | Opcionalno — samo ako koristiš autentifikaciju na bazi ključa umjesto `az login` / Entra ID |

> Responses API koristi stabilni `/openai/v1/` endpoint, tako da nije potreban `api-version`. Prijavi se s `az login` za korištenje autentifikacije bez ključeva putem Entra ID-a.

## Alternativni pružatelj: MiniMax (kompatibilan s OpenAI)

[MiniMax](https://platform.minimaxi.com/) pruža modele s velikim kontekstom (do 204K tokena) putem OpenAI-kompatibilnog API-ja. Budući da Microsoft Agent Framework-ov `OpenAIChatClient` radi s bilo kojim OpenAI-kompatibilnim endpointom, možeš koristiti MiniMax kao zamjenu za Azure OpenAI ili OpenAI.

Dodaj ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platforma](https://platform.minimaxi.com/) → API ključevi |
| `MINIMAX_BASE_URL` | Koristi `https://api.minimax.io/v1` (zadana vrijednost) |
| `MINIMAX_MODEL_ID` | Naziv modela za korištenje (npr. `MiniMax-M3`) |

**Primjeri modela**: `MiniMax-M3` (preporučeno), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (brže reakcije). Nazivi modela i dostupnost mogu se mijenjati tijekom vremena, a pristup određenom modelu može ovisiti o tvom računu ili regiji — provjeri [MiniMax Platformu](https://platform.minimaxi.com/) za ažurni popis. Ako `MiniMax-M3` nije dostupan na tvom računu, postavi `MINIMAX_MODEL_ID` na model kojem imaš pristup (npr. `MiniMax-M2.7`).

Primjeri koda koji koriste `OpenAIChatClient` (npr. Lekcija 14 workflow rezervacije hotela) automatski će prepoznati i koristiti tvoju MiniMax konfiguraciju kada je `MINIMAX_API_KEY` postavljen.

## Alternativni pružatelj: Foundry Local (pokreni modele lokalno)

[Foundry Local](https://foundrylocal.ai) je lagano runtime okruženje koje preuzima, upravlja i poslužuje jezične modele **potpuno na tvom računalu** putem OpenAI-kompatibilnog API-ja — bez oblaka, bez Azure pretplate i bez API ključeva. To je odlična opcija za offline razvoj, eksperimentiranje bez troškova u oblaku ili držanje podataka lokalno na uređaju.

Budući da Microsoft Agent Framework-ov `OpenAIChatClient` radi s bilo kojim OpenAI-kompatibilnim endpointom, Foundry Local je lokalna alternativa Azure OpenAI-u.

**1. Instaliraj Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Preuzmi i pokreni model** (ovo također pokreće lokalnu uslugu):

```bash
foundry model list          # pogledajte dostupne modele
foundry model run phi-4-mini
```

**3. Instaliraj Python SDK** koji se koristi za otkrivanje lokalnog endpointa:

```bash
pip install foundry-local-sdk
```

**4. Usmjeri Microsoft Agent Framework na svoj lokalni model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Preuzima (ako je potrebno) i pokreće model lokalno, zatim pronalazi endpoint/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # npr. http://localhost:<port>/v1
    api_key=manager.api_key,        # uvijek "nije potrebno" za Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Napomena:** Foundry Local izlaže OpenAI-kompatibilni endpoint za **Chat Completions**. Koristi ga za lokalni razvoj i offline scenarije. Za punu funkcionalnost **Responses API** (držanje stanja razgovora, duboka orkestracija alata i razvoj u stilu agenata), ciljaj na **Azure OpenAI** ili **Microsoft Foundry** projekt kao što je prikazano u lekcijama. Pogledaj [Foundry Local dokumentaciju](https://foundrylocal.ai) za trenutačni katalog modela i podršku platforme.

## Dodatno postavljanje za Lekciju 8 (Bing Grounding Workflow)


Bilježnica s uvjetnim tijekovima rada u lekciji 8 koristi **Bing povezivanje** putem Microsoft Foundry. Ako planirate pokrenuti taj primjer, dodajte ovu varijablu u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → vaš projekt → **Upravljanje** → **Povezani resursi** → vaša Bing veza → kopirajte ID veze |

## Rješavanje problema

### Pogreške pri provjeri SSL certifikata na macOS-u

Ako ste na macOS-u i naiđete na pogrešku poput:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ovo je poznati problem s Pythonom na macOS-u gdje sustavni SSL certifikati nisu automatski povjereni. Isprobajte sljedeća rješenja redom:

**Opcija 1: Pokrenite Pythonov Install Certificates skript (preporučeno)**

```bash
# Zamijenite 3.XX s vašom instaliranom verzijom Pythona (npr. 3.12 ili 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opcija 2: Koristite `connection_verify=False` u svojoj bilježnici (samo za GitHub Models bilježnice)**

U bilježnici Lekcije 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) već je uključen zakomentirani zaobilazni način. Odkomentirajte `connection_verify=False` pri kreiranju klijenta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Onemogući SSL provjeru ako naiđeš na pogreške certifikata
)
```

> **⚠️ Upozorenje:** Onemogućavanje SSL provjere (`connection_verify=False`) smanjuje sigurnost preskačući validaciju certifikata. Koristite ovo samo kao privremeni zaobilazni način u razvojnim okruženjima, nikad u produkciji.

**Opcija 3: Instalirajte i koristite `truststore`**

```bash
pip install truststore
```

Zatim dodajte sljedeće na vrh svoje bilježnice ili skripte prije izvođenja mrežnih poziva:

```python
import truststore
truststore.inject_into_ssl()
```

## Zapeli ste negdje?

Ako imate bilo kakvih problema s pokretanjem ovog postava, pridružite se našem <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discordu</a> ili <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">otvorite issue</a>.

## Sljedeća lekcija

Sada ste spremni za pokretanje koda za ovaj tečaj. Sretno u daljnjem učenju o svijetu AI agenata!

[Uvod u AI agente i uporabu agenata](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->