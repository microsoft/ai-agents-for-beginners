# Postavljanje tečaja

## Uvod

Ova lekcija će pokriti kako pokrenuti primjere koda iz ovog tečaja.

## Pridruži se drugim učenicima i zatraži pomoć

Prije nego što počneš klonirati svoj repozitorij, pridruži se [AI Agents For Beginners Discord kanalu](https://aka.ms/ai-agents/discord) kako bi dobio pomoć pri postavljanju, postavio pitanja o tečaju ili se povezao s drugim učenicima.

## Kloniraj ili izradi vlastitu granu (fork) ovog repozitorija

Za početak, molimo te da kloniraš ili napraviš fork GitHub repozitorija. To će ti omogućiti da imaš vlastitu verziju materijala tečaja, tako da možeš pokretati, testirati i prilagođavati kod!

To se može učiniti klikom na vezu za <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">napravi fork repozitorija</a>

Sada bi trebao imati vlastitu forkanu verziju ovog tečaja na sljedećoj poveznici:

![Forked Repo](../../../translated_images/hr/forked-repo.33f27ca1901baa6a.webp)

### Shallow klon (preporučeno za radionicu / Codespaces)

  >Cijeli repozitorij može biti velik (~3 GB) kada preuzmeš cijelu povijest i sve datoteke. Ako sudjeluješ samo na radionici ili ti treba samo nekoliko mapa s lekcijama, shallow klon (ili sparse clone) izbjegava veći dio tog preuzimanja skraćivanjem povijesti i/ili preskakanjem blobova.

#### Brzi shallow klon — minimalna povijest, sve datoteke

Zamijeni `<your-username>` u naredbama ispod s URL-om svog forka (ili upstream URL-om ako želiš).

Za kloniranje samo najnovije povijesti commitova (malo preuzimanje):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Za kloniranje određenog branch-a:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Djelomični (sparse) klon — minimalni blobovi + samo odabrane mape

Ovo koristi djelomični klon i sparse-checkout (zahtijeva Git 2.25+ i preporučeni moderni Git s podrškom za djelomični klon):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Uđi u mapu repozitorija:

```bash|powershell
cd ai-agents-for-beginners
```

Zatim specificiraj koje mape želiš (primjer ispod pokazuje dvije mape):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Nakon kloniranja i provjere datoteka, ako ti trebaju samo datoteke i želiš osloboditi prostor (bez git povijesti), molim obriši meta podatke repozitorija (💀nepovratno — izgubit ćeš svu Git funkcionalnost: nema commitova, pullova, pushova ni pristupa povijesti).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Korištenje GitHub Codespaces (preporučeno za izbjegavanje velikih lokalnih preuzimanja)

- Kreiraj novi Codespace za ovaj repozitorij preko [GitHub UI](https://github.com/codespaces).  

- U terminalu novog codespace-a pokreni jedan od shallow/sparse klon naredbi gore kako bi u workspace učitao samo mape lekcija koje trebaš.
- Opcionalno: nakon kloniranja unutar Codespaces, ukloni .git da oslobodiš dodatni prostor (pogledaj naredbe za uklanjanje gore).
- Napomena: Ako želiš otvoriti repozitorij direktno u Codespaces (bez dodatnog kloniranja), imaj na umu da Codespaces napravi devcontainer okruženje i možda će pripremiti više nego što ti treba. Kloniranje shallow kopije unutar svježeg Codespace-a daje ti veću kontrolu nad korištenjem diska.

#### Savjeti

- Uvijek zamijeni URL kloniranja sa svojim fork-om ako želiš uređivati/commit-ati.
- Ako ti kasnije zatreba više povijesti ili datoteka, možeš ih dohvatiti ili prilagoditi sparse-checkout da uključi dodatne mape.

## Pokretanje koda

Ovaj tečaj nudi niz Jupyter bilježnica koje možeš pokretati da stekneš praktično iskustvo u izgradnji AI agenata.

Primjeri koda koriste **Microsoft Agent Framework (MAF)** s `FoundryChatClient`, koji se povezuje na **Microsoft Foundry Agent Service V2** (Responses API) kroz **Microsoft Foundry**.

Sve Python bilježnice su označene s `*-python-agent-framework.ipynb`.

## Zahtjevi

- Python 3.12+
  - **NAPOMENA**: Ako nemaš instaliran Python 3.12, obavezno ga instaliraj. Zatim kreiraj svoj venv koristeći python3.12 da se osigura ispravno verzioniranje paketa iz requirements.txt.
  
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

- .NET 10+: Za uzorke koda koji koriste .NET, osiguraj da imaš instaliran [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ili noviji. Zatim provjeri verziju instaliranog .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Potreban za autentikaciju. Instaliraj s [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Pretplata** — Za pristup Microsoft Foundry i Microsoft Foundry Agent Service.
- **Microsoft Foundry projekt** — Projekt s implementiranim modelom (npr. `gpt-4o`). Pogledaj [Korak 1](#korak-1-kreiraj-microsoft-foundry-projekt) dolje.

Uključili smo `requirements.txt` datoteku u korijenu ovog repozitorija koja sadrži sve potrebne Python pakete za pokretanje primjera koda.

Možeš ih instalirati pokretanjem sljedeće naredbe u terminalu u korijenu repozitorija:

```bash|powershell
pip install -r requirements.txt
```

Preporučujemo kreiranje Python virtualnog okruženja da izbjegneš konflikte i probleme.

## Postavljanje VSCode

Provjeri da koristiš ispravnu verziju Pythona u VSCode-u.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Postavljanje Microsoft Foundry i Microsoft Foundry Agent Service

### Korak 1: Kreiraj Microsoft Foundry projekt

Potreban ti je Microsoft Foundry **hub** i **projekt** s implementiranim modelom za pokretanje bilježnica.

1. Idi na [ai.azure.com](https://ai.azure.com) i prijavi se sa svojim Azure računom.
2. Kreiraj **hub** (ili koristi postojeći). Pogledaj: [Pregled Hub resursa](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Unutar huba kreiraj **projekt**.
4. Implementiraj model (npr. `gpt-4o`) iz **Models + Endpoints** → **Deploy model**.

### Korak 2: Dohvati krajnju točku projekta i ime implementacije modela

Iz svog projekta u Microsoft Foundry portalu:

- **Project Endpoint** — Otvori stranicu **Overview** i kopiraj URL krajnje točke.

![Project Connection String](../../../translated_images/hr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Naziv implementacije modela** — Idi na **Models + Endpoints**, odaberi svoj implementirani model i zabilježi **Deployment name** (npr. `gpt-4o`).

### Korak 3: Prijava u Azure s `az login`

Sve bilježnice koriste **`AzureCliCredential`** za autentikaciju — nema potrebe za upravljanjem API ključevima. Ovo zahtijeva da si prijavljen putem Azure CLI.

1. **Instaliraj Azure CLI** ako već nemaš: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prijavi se** pokretanjem:

    ```bash|powershell
    az login
    ```

    Ili, ako si u udaljenom/Codespace okruženju bez preglednika:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Odaberi pretplatu** ako budeš upitan — izaberi onu koja sadrži tvoj Foundry projekt.

4. **Provjeri** jesi li prijavljen:

    ```bash|powershell
    az account show
    ```

> **Zašto `az login`?** Bilježnice se autentificiraju koristeći `AzureCliCredential` iz paketa `azure-identity`. To znači da tvoja Azure CLI sesija osigurava vjerodajnice — nema API ključeva ili tajni u tvojoj `.env` datoteci. Ovo je [najbolja sigurnosna praksa](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → tvoj projekt → stranica **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → naziv implementiranog modela |

To je to za većinu lekcija! Bilježnice će se automatski autentificirati kroz tvoju `az login` sesiju.

### Korak 5: Instaliraj Python ovisnosti

```bash|powershell
pip install -r requirements.txt
```

Preporučujemo da to pokreneš unutar virtualnog okruženja koje si ranije kreirao.

## Dodatno postavljanje za Lekciju 5 (Agentic RAG)

Lekcija 5 koristi **Azure AI Search** za generiranje s podrškom pretraživanja. Ako planiraš pokrenuti tu lekciju, dodaj ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → tvoj **Azure AI Search** resurs → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → tvoj **Azure AI Search** resurs → **Settings** → **Keys** → primarni administratorski ključ |

## Dodatno postavljanje za lekcije koje direktno koriste Azure OpenAI (lekcije 6 i 8)

Neke bilježnice u lekcijama 6 i 8 koriste **Azure OpenAI** direktno (korištenjem **Responses API**) umjesto Microsoft Foundry projekta. Ti primjeri su prije koristili GitHub Models, što je zastarjelo (ukidanje u srpnju 2026) i ne podržava Responses API. Ako planiraš pokretati te primjere, dodaj ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → tvoj **Azure OpenAI** resurs → **Keys and Endpoint** → Endpoint (npr. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Ime tvog implementiranog modela (npr. `gpt-4o-mini`) koji podržava Responses API |
| `AZURE_OPENAI_API_KEY` | Opcionalno — samo ako koristiš autentikaciju baziranu na ključu umjesto `az login` / Entra ID |

> Responses API koristi stabilnu `/openai/v1/` krajnju točku, pa nije potreban `api-version`. Prijavi se s `az login` za korištenje autentikacije bez ključeva preko Entra ID.

## Alternativni pružatelj: MiniMax (kompatibilan s OpenAI)

[MiniMax](https://platform.minimaxi.com/) pruža modele velikog konteksta (do 204K tokena) kroz OpenAI-kompatibilan API. Budući da Microsoft Agent Frameworkov `OpenAIChatClient` radi s bilo kojom OpenAI-kompatibilnom krajnjom točkom, MiniMax možeš koristiti kao alternativu za Azure OpenAI ili OpenAI.

Dodaj ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platforma](https://platform.minimaxi.com/) → API ključevi |
| `MINIMAX_BASE_URL` | Koristi `https://api.minimax.io/v1` (zadana vrijednost) |
| `MINIMAX_MODEL_ID` | Naziv modela za korištenje (npr. `MiniMax-M3`) |

**Primjeri modela**: `MiniMax-M3` (preporučeni), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (brža odzivnost). Imena modela i dostupnost mogu se mijenjati tijekom vremena, a pristup određenom modelu može ovisiti o tvom računu ili regiji — provjeri [MiniMax Platformu](https://platform.minimaxi.com/) za trenutni popis. Ako `MiniMax-M3` nije dostupan tvom računu, postavi `MINIMAX_MODEL_ID` na model kojem imaš pristup (npr. `MiniMax-M2.7`).

Primjeri koda koji koriste `OpenAIChatClient` (npr. radni tijek rezervacije hotela u lekciji 14) će automatski prepoznati i koristiti tvoju MiniMax konfiguraciju kada je postavljen `MINIMAX_API_KEY`.

## Alternativni pružatelj: Foundry Local (pokreni modele na uređaju)

[Foundry Local](https://foundrylocal.ai) je lagano runtime okruženje koje preuzima, upravlja i poslužuje jezične modele **potpuno na tvom uređaju** kroz OpenAI-kompatibilan API — bez cloud-a, bez Azure pretplate i bez API ključeva. Odlična je opcija za offline razvoj, eksperimentiranje bez troškova u oblaku ili za zadržavanje podataka na uređaju.

Budući da Microsoft Agent Frameworkov `OpenAIChatClient` radi s bilo kojom OpenAI-kompatibilnom krajnjom točkom, Foundry Local je lokalna alternativa Azure OpenAI.

**1. Instaliraj Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Preuzmi i pokreni model** (to također pokreće lokalnu uslugu):

```bash
foundry model list          # vidi dostupne modele
foundry model run phi-4-mini
```

**3. Instaliraj Python SDK** koji se koristi za pronalaženje lokalne krajnje točke:

```bash
pip install foundry-local-sdk
```

**4. Usmjeri Microsoft Agent Framework na svoj lokalni model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Preuzima (ako je potrebno) i poslužuje model lokalno, zatim pronalazi endpoint/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # npr. http://localhost:<port>/v1
    api_key=manager.api_key,        # uvijek "nije potrebna" za Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Napomena:** Foundry Local izlaže OpenAI-kompatibilnu krajnju točku za **Chat Completions**. Koristi ju za lokalni razvoj i offline scenarije. Za puni skup značajki **Responses API** (državni razgovori, duboka orkestracija alata i razvoj u agent-stilu) ciljaj **Azure OpenAI** ili **Microsoft Foundry** projekt kao što je prikazano u lekcijama. Pogledaj [dokumentaciju Foundry Local](https://foundrylocal.ai) za trenutni katalog modela i podršku platforme.

## Dodatno postavljanje za lekciju 8 (Bing Grounding workflow)


Bilježnica s uvjetnim radnim tokom u lekciji 8 koristi **Bing grounding** putem Microsoft Foundry. Ako planirate pokrenuti taj primjer, dodajte ovu varijablu u vašu `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → vaš projekt → **Upravljanje** → **Povezani resursi** → vaša Bing veza → kopirajte ID veze |

## Rješavanje problema

### Pogreške pri provjeri SSL certifikata na macOS-u

Ako ste na macOS-u i naiđete na pogrešku poput:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ovo je poznat problem s Pythonom na macOS-u gdje sustavni SSL certifikati nisu automatski pouzdani. Isprobajte sljedeća rješenja redom:

**Opcija 1: Pokrenite Python skriptu za instalaciju certifikata (preporučeno)**

```bash
# Zamijenite 3.XX s vašom instaliranom verzijom Pythona (npr. 3.12 ili 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opcija 2: Koristite `connection_verify=False` u vašoj bilježnici (samo za GitHub Models bilježnice)**

U bilježnici Lekcije 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), već je uključen zakomentirani zaobilazni način. Otkomentirajte `connection_verify=False` pri stvaranju klijenta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Onemogućite provjeru SSL-a ako naiđete na pogreške certifikata
)
```

> **⚠️ Upozorenje:** Onemogućavanje SSL provjere (`connection_verify=False`) smanjuje sigurnost preskačući provjeru certifikata. Koristite ovo samo kao privremeno rješenje u razvojnom okruženju, nikada u produkciji.

**Opcija 3: Instalirajte i koristite `truststore`**

```bash
pip install truststore
```

Zatim dodajte sljedeće na vrh vaše bilježnice ili skripte prije nego što napravite bilo kakve mrežne pozive:

```python
import truststore
truststore.inject_into_ssl()
```

## Zapeli ste negdje?

Ako imate problema s pokretanjem ovog postava, pridružite se našem <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discordu</a> ili <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">kreirajte issue</a>.

## Sljedeća lekcija

Sada ste spremni za pokretanje koda za ovaj tečaj. Sretno u daljnjem učenju o svijetu AI Agenta! 

[Uvod u AI agente i primjere upotrebe agenata](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->