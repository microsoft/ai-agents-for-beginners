# Postavljanje tečaja

## Uvod

Ova lekcija će obuhvatiti kako pokrenuti primjere koda ovog tečaja.

## Pridružite se drugim polaznicima i zatražite pomoć

Prije nego što započnete s kloniranjem svog repozitorija, pridružite se [AI Agents For Beginners Discord kanalu](https://aka.ms/ai-agents/discord) za pomoć oko postavljanja, pitanja o tečaju ili povezivanje s drugim polaznicima.

## Klonirajte ili forkajte ovaj repozitorij

Za početak, molimo klonirajte ili forkajte GitHub repozitorij. To će vam napraviti vlastitu verziju materijala tečaja kako biste mogli pokretati, testirati i mijenjati kod!

To možete učiniti klikom na link <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forkajte repozitorij</a>

Sada biste trebali imati svoju vlastitu forkanu verziju ovog tečaja na sljedećem linku:

![Forked Repo](../../../translated_images/hr/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (preporučeno za radionice / Codespaces)

  > Cijeli repozitorij može biti velik (~3 GB) kada preuzmete punu povijest i sve datoteke. Ako pohađate samo radionicu ili trebate samo nekoliko mapa s lekcijama, shallow clone (ili sparse clone) izbjegava većinu preuzimanja skraćujući povijest i/ili preskačući blobove.

#### Brzi shallow clone — minimalna povijest, sve datoteke

Zamijenite `<your-username>` u naredbama ispod svojim fork URL-om (ili upstream URL-om ako želite).

Za kloniranje samo najnovije povijesti (mali download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Za kloniranje određenog branch-a:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Djelomični (sparse) clone — minimalni blobovi + samo odabrane mape

Ovo koristi partial clone i sparse-checkout (zahtijeva Git 2.25+ te preporučeni moderni Git s podrškom za partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Uđite u mapu repozitorija:

```bash|powershell
cd ai-agents-for-beginners
```

Zatim navedite koje mape želite (primjer ispod prikazuje dvije mape):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Nakon kloniranja i provjere datoteka, ako trebate samo datoteke i želite osloboditi prostor (bez git povijesti), obrišite metapodatke repozitorija (💀nepovratno — izgubit ćete svu funkcionalnost Gita: nema commitova, pullova, pushava ni pristupa povijesti).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Korištenje GitHub Codespaces (preporučeno za izbjegavanje velikih lokalnih preuzimanja)

- Kreirajte novi Codespace za ovaj repozitorij preko [GitHub sučelja](https://github.com/codespaces).  

- U terminalu novokreiranog codespacea pokrenite jednu od shallow/sparse clone naredbi iznad kako biste u workspace učitali samo potrebne mape lekcija.
- Opcionalno: nakon kloniranja unutar Codespaces, uklonite .git da biste oslobodili dodatni prostor (pogledajte naredbe za uklanjanje gore).
- Napomena: ako želite otvoriti repozitorij direktno u Codespaces (bez dodatnog kloniranja), imajte na umu da će Codespaces izgraditi devcontainer okruženje i može pripremiti više nego što vam treba. Kloniranje shallow kopije unutar svježeg Codespacea daje vam veću kontrolu nad korištenjem diska.

#### Savjeti

- Uvijek zamijenite clone URL sa svojim forkom ako želite uređivati ili raditi commitove.
- Ako vam kasnije treba više povijesti ili datoteka, možete ih dohvatiti ili prilagoditi sparse-checkout da uključi dodatne mape.

## Pokretanje koda

Ovaj tečaj nudi niz Jupyter bilježnica koje možete pokretati za praktično iskustvo izgradnje AI agenata.

Primjeri koda koriste **Microsoft Agent Framework (MAF)** s `AzureAIProjectAgentProvider`, koji se povezuje na **Azure AI Agent Service V2** (Responses API) putem **Microsoft Foundry**.

Sve Python bilježnice su označene `*-python-agent-framework.ipynb`.

## Zahtjevi

- Python 3.12+
  - **NAPOMENA**: Ako nemate instaliran Python 3.12, osigurajte instalaciju. Zatim kreirajte virtualno okruženje koristeći python3.12 kako biste osigurali ispravne verzije instalirane iz requirements.txt datoteke.
  
    >Primjer

    Kreirajte Python venv direktorij:

    ```bash|powershell
    python -m venv venv
    ```

    Zatim aktivirajte venv okruženje za:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Za primjere koda u .NET-u, instalirajte [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ili noviji. Zatim provjerite verziju instaliranog .NET SDK-a:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Potrebno za autentikaciju. Instalirajte sa [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Pretplata** — Za pristup Microsoft Foundry i Azure AI Agent Service.
- **Microsoft Foundry Projekt** — Projekt s implementiranim modelom (npr. `gpt-4o`). Pogledajte [Korak 1](#korak-1-kreirajte-microsoft-foundry-projekt) dolje.

U korijenu ovog repozitorija nalazi se `requirements.txt` datoteka koja sadrži sve potrebne Python pakete za pokretanje primjera koda.

Možete ih instalirati pokretanjem sljedeće naredbe u terminalu u korijenu repozitorija:

```bash|powershell
pip install -r requirements.txt
```

Preporučujemo kreiranje Python virtualnog okruženja kako biste izbjegli konflikte i probleme.

## Postavljanje VSCode-a

Provjerite koristite li ispravnu verziju Pythona u VSCode-u.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Postavljanje Microsoft Foundry i Azure AI Agent Service

### Korak 1: Kreirajte Microsoft Foundry Projekt

Potrebni su vam Azure AI Foundry **hub** i **projekt** s implementiranim modelom kako biste mogli pokretati bilježnice.

1. Idite na [ai.azure.com](https://ai.azure.com) i prijavite se sa svojim Azure računom.
2. Kreirajte **hub** (ili upotrijebite postojeći). Pogledajte: [Pregled Hub resursa](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Unutar huba kreirajte **projekt**.
4. Implementirajte model (npr. `gpt-4o`) iz **Models + Endpoints** → **Deploy model**.

### Korak 2: Dohvatite endpoint projekta i ime instance modela

U portalu Microsoft Foundry, u vašem projektu:

- **Project Endpoint** — Idite na stranicu **Overview** i kopirajte URL endpointa.

![Project Connection String](../../../translated_images/hr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Ime instance modela** — Idite na **Models + Endpoints**, odaberite implementirani model i zapamtite **Deployment name** (npr. `gpt-4o`).

### Korak 3: Prijavite se u Azure pomoću `az login`

Sve bilježnice koriste **`AzureCliCredential`** za autentikaciju — nema API ključeva za upravljanje. Potrebno je biti prijavljen preko Azure CLI-ja.

1. **Instalirajte Azure CLI** ako već nije instaliran: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prijavite se** pokretanjem:

    ```bash|powershell
    az login
    ```

    Ili ako ste u udaljenom ili Codespace okruženju bez preglednika:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Odaberite pretplatu** ako se to zatraži — odaberite onu u kojoj se nalazi vaš Foundry projekt.

4. **Provjerite** jesu li prijavljeni:

    ```bash|powershell
    az account show
    ```

> **Zašto `az login`?** Bilježnice koriste `AzureCliCredential` iz `azure-identity` paketa za autentikaciju. To znači da vaša Azure CLI sesija osigurava vjerodajnice — nema potreba za API ključevima ili tajnama u `.env` datoteci. Ovo je [najbolja sigurnosna praksa](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Korak 4: Kreirajte svoju `.env` datoteku

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Varijabla | Gdje se nalazi |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → vaš projekt → stranica **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → ime vaše implementacije modela |

To je sve za većinu lekcija! Bilježnice će se automatski autentificirati kroz vašu `az login` sesiju.

### Korak 5: Instalirajte Python ovisnosti

```bash|powershell
pip install -r requirements.txt
```

Preporučujemo pokretanje unutar virtualnog okruženja koje ste ranije kreirali.

## Dodatno postavljanje za Lekciju 5 (Agentic RAG)

Lekcija 5 koristi **Azure AI Search** za retrieval-augmented generation. Ako planirate pokrenuti tu lekciju, dodajte ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje se nalazi |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → vaš **Azure AI Search** resurs → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → vaš **Azure AI Search** resurs → **Settings** → **Keys** → primarni administratorski ključ |

## Dodatno postavljanje za Lekciju 6 i Lekciju 8 (GitHub modeli)

Neke bilježnice u lekcijama 6 i 8 koriste **GitHub Models** umjesto Azure AI Foundry. Ako planirate pokretati te primjere, dodajte ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje se nalazi |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Koristite `https://models.inference.ai.azure.com` (zadana vrijednost) |
| `GITHUB_MODEL_ID` | Ime modela za korištenje (npr. `gpt-4o-mini`) |

## Alternativni dobavljač: MiniMax (OpenAI-kompatibilan)

[MiniMax](https://platform.minimaxi.com/) nudi modele velikog opsega konteksta (do 204K tokena) kroz OpenAI-kompatibilan API. Budući da Microsoft Agent Frameworkov `OpenAIChatClient` radi s bilo kojim OpenAI-kompatibilnim endpointom, možete koristiti MiniMax kao zamjenu za GitHub Models ili OpenAI.

Dodajte ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje se nalazi |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax platforma](https://platform.minimaxi.com/) → API ključevi |
| `MINIMAX_BASE_URL` | Koristite `https://api.minimax.io/v1` (zadana vrijednost) |
| `MINIMAX_MODEL_ID` | Ime modela za korištenje (npr. `MiniMax-M3`) |

**Primjeri modela**: `MiniMax-M3` (preporučeno), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (brže odgovore). Imena modela i dostupnost mogu se mijenjati tijekom vremena, a pristup određenom modelu može ovisiti o vašem računu ili regiji — provjerite [MiniMax platformu](https://platform.minimaxi.com/) za trenutni popis. Ako vam `MiniMax-M3` nije dostupan, postavite `MINIMAX_MODEL_ID` na model kojem imate pristup (npr. `MiniMax-M2.7`).

Primjeri koda koji koriste `OpenAIChatClient` (npr. Lekcija 14 workflow rezervacije hotela) automatski će otkriti i koristiti vašu MiniMax konfiguraciju kad je `MINIMAX_API_KEY` postavljen.

## Dodatno postavljanje za Lekciju 8 (Bing Grounding Workflow)

Uslovni workflow u lekciji 8 koristi **Bing grounding** putem Azure AI Foundry. Ako planirate pokrenuti taj primjer, dodajte ovu varijablu u svoju `.env` datoteku:

| Varijabla | Gdje se nalazi |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → vaš projekt → **Management** → **Connected resources** → vaša Bing veza → kopirajte connection ID |

## Rješavanje problema

### Greške u verifikaciji SSL certifikata na macOS-u

Ako ste na macOS-u i naiđete na pogrešku poput:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ovo je poznat problem s Pythonom na macOS-u gdje sistemski SSL certifikati nisu automatski vjerodostojni. Isprobajte sljedeća rješenja redom:

**Opcija 1: Pokrenite Pythonov Install Certificates skript (preporučeno)**

```bash
# Zamijenite 3.XX s verzijom Pythona koju imate instaliranu (npr. 3.12 ili 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opcija 2: Koristite `connection_verify=False` u vašoj bilježnici (samo za GitHub Models bilježnice)**

U lekciji 6 bilježnici (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) je već uključen zakomentirani način rada. Okomentirajte `connection_verify=False` prilikom kreiranja klijenta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Onemogući provjeru SSL-a ako naiđeš na pogreške certifikata
)
```

> **⚠️ Upozorenje:** Onemogućavanje SSL verifikacije (`connection_verify=False`) smanjuje sigurnost jer preskače validaciju certifikata. Koristite ovo samo kao privremeno rješenje u razvojnom okruženju, nikada u produkciji.

**Opcija 3: Instalirajte i koristite `truststore`**

```bash
pip install truststore
```

Zatim dodajte sljedeće na početak bilježnice ili skripte prije bilo kakvih mrežnih poziva:

```python
import truststore
truststore.inject_into_ssl()
```

## Zapeli ste negdje?

Ako imate problema s postavljanjem, pridružite se našem <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discordu</a> ili <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">kreirajte issue</a>.
## Sljedeća lekcija

Sada ste spremni pokrenuti kod za ovaj tečaj. Sretno s učenjem o svijetu AI agenata!

[Uvod u AI agente i primjere upotrebe agenata](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->