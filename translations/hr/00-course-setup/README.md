# Postavljanje tečaja

## Uvod

Ova lekcija će objasniti kako pokrenuti primjere koda ovog tečaja.

## Pridruži se drugim polaznicima i zatraži pomoć

Prije nego počneš s kloniranjem svog repozitorija, pridruži se [AI Agents For Beginners Discord kanalu](https://aka.ms/ai-agents/discord) za pomoć pri postavljanju, pitanja o tečaju ili povezivanje s drugim polaznicima.

## Kloniraj ili Forkaj ovaj repozitorij

Za početak, molimo te da kloniraš ili forkaš GitHub repozitorij. Tako ćeš imati vlastitu verziju materijala tečaja za pokretanje, testiranje i prilagodbu koda!

To možeš napraviti klikom na link <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forkaj repozitorij</a>

Sada bi trebao imati vlastitu forkanu verziju ovog tečaja na sljedećem linku:

![Forkani Repo](../../../translated_images/hr/forked-repo.33f27ca1901baa6a.webp)

### Plitko kloniranje (preporučeno za radionice / Codespaces)

> Cijeli repozitorij može biti velik (~3 GB) ako preuzmeš kompletnu povijest i sve datoteke. Ako sudjeluješ samo na radionici ili su ti potrebni samo određeni folderi lekcija, plitko kloniranje (ili skupo kloniranje) izbjegava većinu tog preuzimanja time što skraćuje povijest i/ili preskače blobove.

#### Brzo plitko kloniranje — minimalna povijest, sve datoteke

Zamijeni `<your-username>` u naredbama ispod s URL-om svog forka (ili upstream URL ako želiš).

Da kloniraš samo najnoviju povijest commitova (malo preuzimanje):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Da kloniraš određenu granu:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Djelomično (sparse) kloniranje — minimalni blobovi + samo odabrani folderi

Ovo koristi djelomično kloniranje i sparse-checkout (zahtijeva Git 2.25+ i preporučuje se moderni Git s podrškom za djelomično kloniranje):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Uđi u folder repozitorija:

```bash|powershell
cd ai-agents-for-beginners
```

Zatim odredi koje foldere želiš (primjer ispod prikazuje dva foldera):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Nakon kloniranja i provjere datoteka, ako trebaš samo datoteke i želiš osloboditi prostor (bez git povijesti), molimo obriši metapodatke repozitorija (💀nepovratno — izgubit ćeš svu Git funkcionalnost: nijedan commit, pull, push ili pristup povijesti).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Korištenje GitHub Codespaces (preporučeno za izbjegavanje lokalnih velikih preuzimanja)

- Kreiraj novi Codespace za ovaj repozitorij preko [GitHub UI](https://github.com/codespaces).  

- U terminalu novokreiranog codespace-a pokreni jednu od gore navedenih shallow/sparse naredbi da u Codespace workspace učitaš samo potrebne foldere lekcija.
- Opcionalno: nakon kloniranja u Codespaces, ukloni .git kako bi oslobodio dodatni prostor (vidi naredbe za uklanjanje gore).
- Napomena: Ako preferiraš otvoriti repozitorij izravno u Codespaces (bez dodatnog kloniranja), budi svjestan da Codespaces konstruira devcontainer okruženje i možda će i dalje preuzeti više nego što trebaš. Kloniranje plitke kopije unutar svježeg Codespace-a daje ti veću kontrolu nad korištenjem diska.

#### Savjeti

- Uvijek zamijeni URL kloniranja s URL-om svog forka ako želiš uređivati/potpisivati promjene.
- Ako ti kasnije zatreba više povijesti ili datoteka, možeš ih dohvatiti ili promijeniti sparse-checkout da uključi dodatne foldere.

## Pokretanje koda

Ovaj tečaj nudi seriju Jupyter bilježnica koje možeš pokrenuti kako bi stekao praktično iskustvo u izgradnji AI agenata.

Primjeri koda koriste **Microsoft Agent Framework (MAF)** sa `FoundryChatClient`, koji se povezuje na **Microsoft Foundry Agent Service V2** (Responses API) preko **Microsoft Foundry**.

Sve Python bilježnice su označene kao `*-python-agent-framework.ipynb`.

## Zahtjevi

- Python 3.12+
  - **NAPOMENA**: Ako nemaš instaliran Python3.12, osiguraj da ga instaliraš. Zatim kreiraj svoj venv koristeći python3.12 da osiguraš ispravne verzije instalirane iz requirements.txt datoteke.
  
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

- .NET 10+: Za primjere koda koji koriste .NET, osiguraj instalaciju [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ili novijeg. Zatim provjeri instaliranu .NET SDK verziju:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Potrebno za autentifikaciju. Instaliraj s [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Pretplata** — Za pristup Microsoft Foundry i Microsoft Foundry Agent Service.
- **Microsoft Foundry Projekt** — Projekt s implementiranim modelom (npr. `gpt-4.1-mini`). Vidi [Korak 1](#korak-1-kreiraj-microsoft-foundry-projekt) dolje.

Uključili smo `requirements.txt` datoteku u korijenu ovog repozitorija koja sadrži sve potrebne Python pakete za pokretanje primjera koda.

Možeš ih instalirati pokretanjem naredbe u terminalu u korijenu repozitorija:

```bash|powershell
pip install -r requirements.txt
```

Preporučujemo kreiranje Python virtualnog okoliša kako bi izbjegao sukobe i probleme.

## Postavljanje VSCode

Provjeri da koristiš ispravnu verziju Pythona u VSCode-u.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Postavi Microsoft Foundry i Microsoft Foundry Agent Service

### Korak 1: Kreiraj Microsoft Foundry Projekt

Trebaš Microsoft Foundry **hub** i **projekt** s implementiranim modelom da bi mogao pokretati bilježnice.

1. Idi na [ai.azure.com](https://ai.azure.com) i prijavi se sa svojim Azure računom.
2. Kreiraj **hub** (ili koristi postojeći). Vidi: [Pregled Hub resursa](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Unutar huba, kreiraj **projekt**.
4. Implementiraj model (npr. `gpt-4.1-mini`) iz **Models + Endpoints** → **Deploy model**.

### Korak 2: Dohvati Project Endpoint i Naziv implementacije modela

Iz svog projekta u Microsoft Foundry portalu:

- **Project Endpoint** — Idi na stranicu **Overview** i kopiraj URL endpointa.

![Project Connection String](../../../translated_images/hr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Naziv implementacije modela** — Idi na **Models + Endpoints**, odaberi svoj implementirani model, i zabilježi **Deployment name** (npr. `gpt-4.1-mini`).

### Korak 3: Prijavi se u Azure s `az login`

Sve bilježnice koriste **`AzureCliCredential`** za autentifikaciju — nema API ključeva za upravljanje. To zahtijeva da si prijavljen putem Azure CLI.

1. **Instaliraj Azure CLI** ako već nisi: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prijavi se** pokretanjem:

    ```bash|powershell
    az login
    ```

    Ili ako si u udaljenom / Codespace okruženju bez preglednika:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Odaberi svoju pretplatu** ako treba — izaberi onu koja sadrži tvoj Foundry projekt.

4. **Provjeri** da si prijavljen:

    ```bash|powershell
    az account show
    ```

> **Zašto `az login`?** Bilježnice se autentificiraju koristeći `AzureCliCredential` iz `azure-identity` paketa. To znači da tvoja Azure CLI sesija pruža vjerodajnice — nema API ključeva ili tajni u tvojoj `.env` datoteci. Ovo je [sigurnosna najbolja praksa](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → tvoj projekt → stranica **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → naziv tvog implementiranog modela |

To je sve za većinu lekcija! Bilježnice će se automatski autentificirati preko tvoje `az login` sesije.

### Korak 5: Instaliraj Python ovisnosti

```bash|powershell
pip install -r requirements.txt
```

Preporučujemo da ovo pokreneš unutar virtualnog okruženja koje si prethodno napravio.

## Dodatno postavljanje za lekciju 5 (Agentic RAG)

Lekcija 5 koristi **Azure AI Search** za retrieval 강화한 generaciju. Ako planiraš pokretati tu lekciju, dodaj ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → tvoj **Azure AI Search** resurs → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → tvoj **Azure AI Search** resurs → **Settings** → **Keys** → primarni administratorski ključ |

## Dodatno postavljanje za lekcije koje izravno pozivaju Azure OpenAI (lekcije 6 i 8)

Neke bilježnice u lekcijama 6 i 8 izravno koriste **Azure OpenAI** (kroz **Responses API**) umjesto kroz Microsoft Foundry projekt. Ovi primjeri su ranije koristili GitHub modele, koji su zastarjeli (ukidaju se u srpnju 2026) i ne podržavaju Responses API. Ako planiraš koristiti te primjere, dodaj ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → tvoj **Azure OpenAI** resurs → **Keys and Endpoint** → Endpoint (npr. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Naziv tvog implementiranog modela (npr. `gpt-4.1-mini`) koji podržava Responses API |
| `AZURE_OPENAI_API_KEY` | Opcionalno — samo ako koristiš autentifikaciju putem ključa umjesto `az login` / Entra ID |

> Responses API koristi stabilni `/openai/v1/` endpoint, tako da `api-version` nije potreban. Prijavi se s `az login` za korištenje keyless Entra ID autentifikacije.

## Alternativni pružatelj: MiniMax (kompatibilan s OpenAI)

[MiniMax](https://platform.minimaxi.com/) pruža modele s velikim kontekstom (do 204K tokena) preko OpenAI-kompatibilnog API-ja. Budući da Microsoft Agent Framework `OpenAIChatClient` radi s bilo kojim OpenAI-kompatibilnim endpointom, možeš koristiti MiniMax kao izravan zamjenski pružatelj za Azure OpenAI ili OpenAI.

Dodaj ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platforma](https://platform.minimaxi.com/) → API ključevi |
| `MINIMAX_BASE_URL` | Koristi `https://api.minimax.io/v1` (zadana vrijednost) |
| `MINIMAX_MODEL_ID` | Naziv modela za korištenje (npr. `MiniMax-M3`) |

**Primjeri modela**: `MiniMax-M3` (preporučeno), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (brže odgovore). Nazivi modela i dostupnost se mogu mijenjati s vremenom, a pristup određenom modelu može ovisiti o tvom računu ili regiji — provjeri [MiniMax Platformu](https://platform.minimaxi.com/) za trenutačni popis. Ako ti `MiniMax-M3` nije dostupan, postavi `MINIMAX_MODEL_ID` na model kojem imaš pristup (npr. `MiniMax-M2.7`).

Primjeri koda koji koriste `OpenAIChatClient` (npr. radni tok rezervacije hotela u Lekciji 14) automatski će prepoznati i koristiti tvoju MiniMax konfiguraciju kada je postavljen `MINIMAX_API_KEY`.

## Alternativni pružatelj: Foundry Local (pokretanje modela lokalno)

[Foundry Local](https://foundrylocal.ai) je lagano runtime okruženje koje preuzima, upravlja i poslužuje jezične modele **potpuno na tvom računalu** putem OpenAI-kompatibilnog API-ja — bez oblaka, bez Azure pretplate i bez API ključeva. Odlična je opcija za offline razvoj, eksperimentiranje bez troškova u oblaku ili čuvanje podataka lokalno.

Budući da Microsoft Agent Framework `OpenAIChatClient` radi s bilo kojim OpenAI-kompatibilnim endpointom, Foundry Local je izravan lokalni zamjenski pružatelj za Azure OpenAI.

**1. Instaliraj Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Preuzmi i pokreni model** (time se također pokreće lokalna usluga):

```bash
foundry model list          # vidi dostupne modele
foundry model run phi-4-mini
```

**3. Instaliraj Python SDK** koji se koristi za pronalaženje lokalnog endpointa:

```bash
pip install foundry-local-sdk
```

**4. Usmjeri Microsoft Agent Framework na svoj lokalni model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Preuzima (ako je potrebno) i pokreće model lokalno, zatim pronalazi krajnju točku/port.
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

> **Napomena:** Foundry Local izlaže OpenAI-kompatibilan **Chat Completions** endpoint. Koristi ga za lokalni razvoj i offline scenarije. Za puni skup značajki **Responses API** (stanja razgovora, duboka orkestracija alata, i razvoj stilom agenata), ciljanjem **Azure OpenAI** ili **Microsoft Foundry** projekta, kao što je prikazano u lekcijama. Pogledaj [Foundry Local dokumentaciju](https://foundrylocal.ai) za trenutačni katalog modela i podršku platformi.


## Dodatna postava za Lekciju 8 (Bing Grounding Workflow)

Uvjetni tijek rada u lekciji 8 koristi **Bing grounding** putem Microsoft Foundry. Ako planirate pokrenuti taj primjer, dodajte ovu varijablu u vašu `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → vaš projekt → **Management** → **Connected resources** → vaša Bing konekcija → kopirajte ID konekcije |

## Rješavanje problema

### Pogreške prilikom provjere SSL certifikata na macOS-u

Ako ste na macOS-u i naiđete na pogrešku poput:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ovo je poznati problem s Pythonom na macOS-u gdje sustavni SSL certifikati nisu automatski pouzdani. Isprobajte sljedeća rješenja redom:

**Opcija 1: Pokrenite Pythonov Install Certificates skript (preporučeno)**

```bash
# Zamijenite 3.XX s vašom instaliranom verzijom Pythona (npr. 3.12 ili 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opcija 2: Koristite `connection_verify=False` u vašem noteboku (samo za GitHub Models notebooke)**

U notebooku Lekcije 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) već je uključen zakomentirani zaobilazni način. Odkomentirajte `connection_verify=False` pri kreiranju klijenta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Onemogući SSL provjeru ako naiđeš na greške s certifikatom
)
```

> **⚠️ Upozorenje:** Onemogućavanje SSL provjere (`connection_verify=False`) smanjuje sigurnost preskačući validaciju certifikata. Koristite ovo samo kao privremenu zaobilaznicu u razvojnom okruženju, nikada u produkciji.

**Opcija 3: Instalirajte i koristite `truststore`**

```bash
pip install truststore
```

Zatim dodajte sljedeće na vrh vašeg notebuka ili skripte prije bilo kakvih mrežnih poziva:

```python
import truststore
truststore.inject_into_ssl()
```

## Zapeli ste negdje?

Ako imate problema s pokretanjem ove postave, pridružite se našem <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discordu</a> ili <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">kreirajte problem</a>.

## Sljedeća lekcija

Sad ste spremni pokrenuti kod za ovaj tečaj. Sretno u daljnjem učenju o svijetu AI Agenata!

[Uvod u AI Agente i primjere korištenja agenata](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->