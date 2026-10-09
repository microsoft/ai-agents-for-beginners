# Postavljanje tečaja

## Uvod

Ova lekcija će obuhvatiti kako pokrenuti primjere koda iz ovog tečaja.

## Pridružite se drugim polaznicima i zatražite pomoć

Prije nego što počnete klonirati svoj repozitorij, pridružite se [AI Agents For Beginners Discord kanalu](https://aka.ms/ai-agents/discord) kako biste dobili pomoć oko postavljanja, pitanja o tečaju ili povezivanja s drugim polaznicima.

## Klonirajte ili forkajte ovaj repozitorij

Za početak, molimo da klonirate ili forkate GitHub repozitorij. To će vam omogućiti vlastitu verziju materijala tečaja koju možete pokretati, testirati i prilagođavati kod!

To možete učiniti klikom na <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repozitorij</a>

Sada biste trebali imati vlastitu forkanu verziju ovog tečaja na sljedećem linku:

![Forked Repo](../../../translated_images/hr/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (preporučeno za radionice / Codespaces)

  > Cijeli repozitorij može biti velik (~3 GB) kada preuzimate cijelu povijest i sve datoteke. Ako sudjelujete samo na radionici ili vam trebaju samo određene lekcije, shallow clone (ili sparse clone) preuzima puno manje.

#### Brzi shallow clone — minimalna povijest, sve datoteke

Zamijenite `<your-username>` u naredbama ispod s URL-om vašeg forka (ili upstream URL-om ako preferirate).

Za kloniranje samo najnovije povijesti commitova (malo preuzimanje):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Za kloniranje određenog branch-a:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Djelomični (sparse) clone — minimalni blobovi + samo odabrani direktoriji

Ovo koristi partial clone i sparse-checkout (zahtijeva Git 2.25+ i preporučeni moderni Git s podrškom za partial clone):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Uđite u direktorij repozitorija:

```bash
cd ai-agents-for-beginners
```

Zatim navedite koje direktorije želite (primjer ispod prikazuje dva direktorija):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Nakon kloniranja i provjere datoteka, ako vam trebaju samo datoteke i želite osloboditi prostor (bez git povijesti), obrišite repozitorijske metapodatke (💀nepovratno — izgubiti ćete kompletnu Git funkcionalnost):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Korištenje GitHub Codespaces (preporučeno za izbjegavanje lokalnog velikog preuzimanja)

- Kreirajte novi Codespace za ovaj repozitorij preko [GitHub UI](https://github.com/codespaces).  

- U terminalu novog Codespace-a, pokrenite jednu od gore navedenih shallow/sparse clone naredbi da u workspace Codespace-a dovedete samo potrebne lekcije.
- Opcionalno: nakon kloniranja unutar Codespaces, uklonite .git da oslobodite dodatni prostor (vidi gore navedene naredbe za uklanjanje).
- Napomena: Ako želite otvoriti repozitorij direktno u Codespaces (bez dodatnog kloniranja), imajte na umu da Codespaces konstruira razvojno okruženje te može i dalje postaviti više nego što vam treba.

#### Savjeti

- Uvijek zamijenite URL kloniranja s URL-om svog forka ako želite uređivati / praviti commitove.
- Ako vam kasnije zatreba više povijesti ili datoteka, možete ih dohvatiti ili prilagoditi sparse-checkout da uključi dodatne direktorije.

## Pokretanje koda

Ovaj tečaj nudi niz Jupyter bilježnica (notebook) koje možete pokretati za praktično iskustvo u izradi AI agenata.

Primjeri koda koriste **Microsoft Agent Framework (MAF)** s `FoundryChatClient`, koji se povezuje na **Microsoft Foundry Agent Service V2** (Responses API) preko **Microsoft Foundry**.

Sve Python bilježnice su označene kao `*-python-agent-framework.ipynb`.

## Zahtjevi

- Python 3.12+
  - **NAPOMENA**: Ako nemate instaliran Python 3.12, pobrinite se da ga instalirate. Zatim stvorite virtualno okruženje koristeći python3.12 da biste osigurali instalaciju pravih verzija iz datoteke requirements.txt.
  
    >Primjer

    Stvorite direktorij Python virtualnog okruženja:

    ```bash
    python -m venv venv
    ```

    Zatim aktivirajte virtualno okruženje za:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Za primjere koda koji koriste .NET, pobrinite se da instalirate [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ili noviju verziju. Zatim provjerite verziju instaliranog .NET SDK:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Potrebno za autentifikaciju. Instalirajte s [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure pretplata** — Za pristup Microsoft Foundry i Microsoft Foundry Agent Service.
- **Microsoft Foundry projekt** — Projekt s postavljenim modelom (npr. `gpt-5-mini`). Pogledajte [Korak 1](#korak-1-kreirajte-microsoft-foundry-projekt) u nastavku.

U korijenu ovog repozitorija uključen je `requirements.txt` koji sadrži sve potrebne Python pakete za pokretanje primjera koda.

Možete ih instalirati pokretanjem sljedeće naredbe u terminalu u korijenu repozitorija:

```bash
pip install -r requirements.txt
```

Preporučujemo stvaranje Python virtualnog okruženja kako bi izbjegli sukobe i probleme.

## Postavljanje VSCode

Pobrinite se da koristite pravu verziju Pythona u VSCode-u.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Postavljanje Microsoft Foundry i Microsoft Foundry Agent Service

### Korak 1: Kreirajte Microsoft Foundry projekt

Potreban vam je Microsoft Foundry **hub** i **projekt** s postavljenim modelom da biste pokrenuli bilježnice.

1. Idite na [ai.azure.com](https://ai.azure.com) i prijavite se svojim Azure računom.
2. Kreirajte **hub** (ili koristite postojeći). Pogledajte: [Pregled Hub resursa](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. U okviru huba kreirajte **projekt**.
4. Postavite model (npr. `gpt-5-mini`) iz **Models + Endpoints** → **Deploy model**.

### Korak 2: Nabavite URL projekta i naziv postavljenog modela

Iz svog projekta u Microsoft Foundry portalu:

- **Project Endpoint** — Idite na stranicu **Overview** i kopirajte URL endpointa.

![Project Connection String](../../../translated_images/hr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Idite na **Models + Endpoints**, odaberite svoj postavljeni model i zabilježite **Ime postavljanja** (npr. `gpt-5-mini`).

### Korak 3: Prijavite se u Azure s `az login`

Većina bilježnica autentificira putem vaše **Azure CLI prijave** — koristeći `AzureCliCredential` ili `DefaultAzureCredential` (obu hvataju vašu `az login` sesiju) iz `azure-identity` paketa — pa ne zahtijevaju API ključeve. Nekoliko lekcija i opcionalnih integracija koristi API ključeve; provjerite uvjete svake lekcije za dodatne varijable okruženja. Ovo zahtijeva da budete prijavljeni preko Azure CLI.

1. **Instalirajte Azure CLI** ako već nemate: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prijavite se** pokretanjem:

    ```bash
    az login
    ```

    Ili ako ste u udaljenom/Codespace okruženju bez preglednika:

    ```bash
    az login --use-device-code
    ```

3. **Odaberite pretplatu** ako vam se traži — odaberite onu koja sadrži vaš Foundry projekt.

4. **Provjerite** jeste li prijavljeni:

    ```bash
    az account show
    ```

> **Zašto `az login`?** Bilježnice se autentificiraju pomoću `AzureCliCredential` (ili `DefaultAzureCredential` koji također hvata vašu Azure CLI prijavu) iz `azure-identity` paketa. To znači da vaša Azure CLI sesija daje vjerodajnice — nema API ključeva ili tajni u vašoj `.env` datoteci. Ovo je [sigurnosna najbolja praksa](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Korak 4: Kreirajte vašu `.env` datoteku

Kopirajte primjer datoteke:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Otvorite `.env` i ispunite ove dvije vrijednosti:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Varijabla | Gdje ju pronaći |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → vaš projekt → stranica **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → ime vašeg postavljenog modela |

To je sve za većinu lekcija! Bilježnice će se automatski autentificirati preko vaše `az login` sesije.

### Korak 5: Instalirajte Python ovisnosti

```bash
pip install -r requirements.txt
```

Preporučujemo pokretanje unutar virtualnog okruženja koje ste ranije kreirali.

## Opcionalno postavljanje: Azure AI Search (Lekcije 5 i 16)

Lekcije 5 (Agentic RAG) i 16 bilježnice rade odmah s **memorijskom bazom znanja** — nije potrebno dodatno Azure resurse. Ako ih želite povezati s pravim **Azure AI Search** indeksom, imajte na umu da **bilježnica Lekcije 16 trenutno koristi autentifikaciju s ključem**: prebacuje s memorijske pretrage na Azure AI Search samo kada su **obje** varijable `AZURE_SEARCH_SERVICE_ENDPOINT` **i** `AZURE_SEARCH_API_KEY` postavljene, inače ostaje na memorijskoj pretrazi — dakle za korištenje stvarnog indeksa morate također postaviti admin ključ. Autentifikacija bez ključa pomoću Microsoft Entra ID-a (RBAC) je preporučeni pristup za vlastiti produkcijski kod, u skladu s `az login` tokom koji se koristi u ostatku ovog tečaja.

Koraci RBAC ispod primjenjuju se na uzorke vodiča za postavljanje i vaš vlastiti kod. Ne omogućavaju autentifikaciju bez ključa u bilježnici Lekcije 16; Lekcija 16 i dalje zahtijeva endpoint i admin ključ za korištenje Azure AI Search.

1. **Omogućite ulogama pristup** na svom servisu za pretraživanje:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Dodijelite sebi potrebne uloge** (kreiranje/učitavanje indeksa i upite):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Dodajte endpoint** u vašu `.env` datoteku:

| Varijabla | Gdje ju pronaći |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → vaš **Azure AI Search** resurs → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Potrebno (uz endpoint) za omogućavanje Azure AI Search u bilježnici Lekcije 16 koja koristi autentifikaciju s ključem. Azure portal → **Settings** → **Keys** → primarni admin ključ |

> **Zašto bez ključa?** Admin ključevi daju potpuni pristup pisanju na vaš servis za pretraživanje i mogu se slučajno izložiti kroz `.env` datoteke. S RBAC-om se koristi vaš `az login` identitet — isti obrazac bez ključa Entra ID koji koriste bilježnice tečaja (putem `AzureCliCredential` / `DefaultAzureCredential`). Pogledajte [Povezivanje s Azure AI Search korištenjem uloga](https://learn.microsoft.com/azure/search/search-security-rbac).

Pogledajte [Vodič za postavljanje Azure AI Search](./AzureSearch.md) za primjere kompletne kreacije indeksa u Pythonu i .NET.

## Dodatno postavljanje za lekcije koje direktno pozivaju Azure OpenAI (Lekcije 6 i 8)

Neke bilježnice u lekcijama 6 i 8 pozivaju **Azure OpenAI** direktno (koristeći **Responses API**) umjesto da idu preko Microsoft Foundry projekta. Ovi primjeri su prethodno koristili GitHub modele, koji su zastarjeli i ne podržavaju Responses API. Dodajte ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje ju pronaći |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → vaš **Azure OpenAI** resurs → **Keys and Endpoint** → Endpoint (npr. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Ime vašeg postavljenog modela (npr. `gpt-5-mini`) koji podržava Responses API |
| `AZURE_OPENAI_API_KEY` | Opcionalno — samo ako koristite autentifikaciju s ključem umjesto `az login` / Entra ID |

> Responses API koristi stabilni `/openai/v1/` endpoint, nije potreban `api-version`. Prijavite se s `az login` za korištenje autentifikacije bez ključa Entra ID-a.

## Alternativni pružatelj: MiniMax (kompatibilan s OpenAI)

[MiniMax](https://platform.minimaxi.com/) pruža modele s velikim kontekstom (do 204K tokena) putem API-ja kompatibilnog s OpenAI. Kako Microsoft Agent Framework-ov `OpenAIChatClient` radi s bilo kojim OpenAI-kompatibilnim endpointom, možete koristiti MiniMax kao zamjenu za lekcije koje koriste `OpenAIChatClient`.

Dodajte ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje ju pronaći |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API ključevi |
| `MINIMAX_BASE_URL` | Koristite `https://api.minimax.io/v1` (zadana vrijednost) |
| `MINIMAX_MODEL_ID` | Ime modela za korištenje (npr. `MiniMax-M3`) |

**Primjeri modela**: `MiniMax-M3` (preporučeni), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (brži odgovori). Imena i dostupnost modela mogu se mijenjati tijekom vremena, a pristup određenom modelu može ovisiti o vašem računu.

Primjeri koda koji koriste `OpenAIChatClient` (npr. Lekcija 14 za hotel booking workflow) će automatski prepoznati i koristiti vašu MiniMax konfiguraciju kada je `MINIMAX_API_KEY` postavljen.


## Alternativni pružatelj usluga: Novita AI (kompatibilan s OpenAI)

[Novita AI](https://novita.ai/llm-api) nudi OpenAI-kompatibilan API za open-source i najnovije LLM-ove (DeepSeek, Llama, Qwen i druge). Budući da Microsoft Agent Frameworkov `OpenAIChatClient` radi s bilo kojim OpenAI-kompatibilnim endpointom, možete koristiti Novita AI kao direktnu alternativu Azure OpenAI ili OpenAI.

Dodajte ove varijable u svoj `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI nadzorna ploča](https://novita.ai/settings/key-management) → API ključevi |
| `NOVITA_BASE_URL` | Koristite `https://api.novita.ai/openai/v1` (zadana vrijednost) |
| `NOVITA_MODEL_ID` | Naziv modela za korištenje (npr. `moonshotai/kimi-k3`) |

**Primjeri modela**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI također hosta mnoge druge open-source obitelji modela (Llama, Qwen, GLM i druge) — pogledajte [Novita AI biblioteku modela](https://novita.ai/llm-api) za trenutni popis dostupnih modela i njihove ID-ove.

Trenutni primjeri ne koriste automatski `NOVITA_*` varijable. Za korištenje Novita AI-a, proslijedite te vrijednosti eksplicitno prilikom konstruiranja `OpenAIChatClient` u primjeru koji pokrećete.

## Alternativni pružatelj usluga: Foundry Local (pokrenite modele na uređaju)

[Foundry Local](https://foundrylocal.ai) je lagano runtime okruženje koje preuzima, upravlja i pokreće jezične modele **posve lokalno na vašem računalu** preko OpenAI-kompatibilnog API-ja — nema potrebe za cloudom.

Budući da Microsoft Agent Frameworkov `OpenAIChatClient` radi s bilo kojim OpenAI-kompatibilnim endpointom, Foundry Local je lokalna zamjenska opcija za Azure OpenAI.

**1. Instalirajte Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Preuzmite i pokrenite model** (time se također pokreće lokalni servis):

```bash
foundry model list          # vidi dostupne modele
foundry model run phi-4-mini
```

**3. Instalirajte Python SDK** koji se koristi za pronalaženje lokalnog endpointa:

```bash
pip install foundry-local-sdk
```

**4. Usmjerite Microsoft Agent Framework na vaš lokalni model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Preuzima (ako je potrebno) i lokalno poslužuje model, zatim pronalazi endpoint/port.
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

> **Napomena:** Foundry Local izlaže OpenAI-kompatibilan endpoint za **Chat završetke**. Koristite ga za lokalni razvoj i offline scenarije. Za puni skup značajki **Responses API-ja** (držanje stanja razgovora itd.), koristite Azure OpenAI ili Microsoft Foundry projekt.

## Dodatna konfiguracija za Lekciju 8 (Bing Grounding workflow)

Uvjetni workflow notebook u lekciji 8 koristi **Bing grounding** preko Microsoft Foundry. Ako planirate pokrenuti taj primjer, dodajte ovu varijablu u svoj `.env` fajl:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → vaš projekt → **Upravljanje** → **Povezani resursi** → vaša Bing veza → kopirajte ID veze |

## Rješavanje problema

### Pogreške provjere SSL certifikata na macOS-u

Ako ste na macOS-u i naiđete na pogrešku poput:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ovo je poznati problem s Pythonom na macOS-u gdje se sistemski SSL certifikati ne vjeruju automatski. Isprobajte sljedeća rješenja redom:

**Opcija 1: Pokrenite Pythonov Install Certificates skript (preporučeno)**

```bash
# Zamijenite 3.XX s vašom instaliranom verzijom Pythona (npr. 3.12 ili 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opcija 2: Koristite `connection_verify=False` u vašem notebooku (samo za GitHub Models bilježnice)**

U Lesson 6 notebooku (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) već postoji zakomentirano zaobilazno rješenje. Odkomentirajte `connection_verify=False` kad dođe do pogrešaka certifikata:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Onemogućite provjeru SSL-a ako naiđete na pogreške certifikata
)
```

> **⚠️ Upozorenje:** Onemogućavanje SSL provjere (`connection_verify=False`) smanjuje sigurnost jer preskače validaciju certifikata. Koristite ovo samo kao privremenu mjera u razvojnom okruženju. Nikada ne koristite u produkciji.

**Opcija 3: Instalirajte i koristite `truststore`**

```bash
pip install truststore
```

Zatim dodajte sljedeće na početak vašeg notebooka ili skripte prije bilo kakvih mrežnih poziva:

```python
import truststore
truststore.inject_into_ssl()
```

## Zapeli ste negdje?

Ako imate problema s pokretanjem ove postavke, pridružite se našem <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discordu</a> ili <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">otvorite issue</a>.

## Sljedeća lekcija

Sada ste spremni pokrenuti kod ovog tečaja. Sretno u učenju o svijetu AI agenata!

[Uvod u AI agente i primjene agenata](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->