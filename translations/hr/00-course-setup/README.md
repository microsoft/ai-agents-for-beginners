# Postavljanje Tečaja

## Uvod

Ova lekcija će obuhvatiti kako pokrenuti primjere koda ovog tečaja.

## Pridruži se drugim učenicima i zatraži pomoć

Prije nego što počneš klonirati svoj repozitorij, priključi se na [AI Agents For Beginners Discord kanal](https://aka.ms/ai-agents/discord) za pomoć oko postavljanja, pitanja o tečaju ili za povezivanje s drugim učenicima.

## Kloniraj ili Forkaj ovaj Repozitorij

Za početak, molimo te da kloniraš ili fork-aš GitHub repozitorij. To će ti omogućiti vlastitu verziju materijala tečaja kako bi mogao pokretati, testirati i mijenjati kod!

To se može napraviti klikom na poveznicu za <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forkanje repozitorija</a>

Sada bi trebao imati svoju vlastitu forkanu verziju ovog tečaja na sljedećoj poveznici:

![Forked Repo](../../../translated_images/hr/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (preporučeno za radionicu / Codespaces)

  >Cijeli repozitorij može biti velik (~3 GB) ako preuzmeš cijelu povijest i sve datoteke. Ako ideš samo na radionicu ili ti trebaju samo određene mape lekcija, shallow clone (ili sparse clone) izbjegava većinu preuzimanja tako da skraćuje povijest i/ili preskače blobove.

#### Brzi shallow clone — minimalna povijest, sve datoteke

Zamijeni `<your-username>` u naredbama ispod sa svojom fork URL adresom (ili upstream URL ako radije).

Za kloniranje samo najnovije povijesti commita (malo preuzimanje):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Za kloniranje određenog branch-a:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Parcijalni (sparse) clone — minimalni blobovi + odabrane mape

Ovo koristi partial clone i sparse-checkout (zahtijeva Git 2.25+ i preporučeni moderni Git s podrškom za partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Uđi u mapu repozitorija:

```bash|powershell
cd ai-agents-for-beginners
```

Zatim specificiraj koje mape želiš (primjer ispod prikazuje dvije mape):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Nakon kloniranja i provjere datoteka, ako ti trebaju samo datoteke i želiš osloboditi prostor (bez povijesti gita), obavezno ukloni meta-podatke repozitorija (💀nepovratno — izgubit ćeš svu Git funkcionalnost: nema commit-a, pull-a, push-a ili pristupa povijesti).

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

- U terminalu novo kreiranog codespacea pokreni jednu od shallow/sparse clone naredbi gore da dovedeš samo mape lekcija koje ti trebaju u Codespace workspace.
- Opcionalno: nakon kloniranja unutar Codespaces ukloni .git za vraćanje dodatnog prostora (vidi naredbe za uklanjanje gore).
- Napomena: Ako radije otvoriš repozitorij izravno u Codespaces (bez dodatnog kloniranja), imaj na umu da će Codespaces kreirati devcontainer okruženje i možda će i dalje postaviti više nego što ti treba. Kloniranje plitke kopije unutar svježeg Codespacea daje ti veću kontrolu nad korištenjem diska.

#### Savjeti

- Uvijek zamijeni URL kloniranja sa svojom fork verzijom ako želiš uređivati/commit-ati.
- Ako ti kasnije zatreba više povijesti ili datoteka, možeš ih dohvatiti ili prilagoditi sparse-checkout da uključi dodatne mape.

## Pokretanje Koda

Ovaj tečaj nudi niz Jupyter bilježnica koje možeš pokrenuti za praktično iskustvo izrade AI agenata.

Primjeri koda koriste **Microsoft Agent Framework (MAF)** s `AzureAIProjectAgentProvider`, koji se povezuje na **Azure AI Agent Service V2** (Responses API) putem **Microsoft Foundry**.

Sve Python bilježnice imaju oznaku `*-python-agent-framework.ipynb`.

## Zahtjevi

- Python 3.12+
  - **NAPOMENA**: Ako nemaš instaliran Python3.12, pobrini se da ga instaliraš. Potom kreiraj svoje venv koristeći python3.12 kako bi osigurao instalaciju ispravnih verzija iz datoteke requirements.txt.
  
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

- .NET 10+: Za primjer koda koji koristi .NET, osiguraj da instaliraš [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ili noviji. Potom provjeri verziju instaliranog .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Potrebno za autentikaciju. Instaliraj s [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Pretplata** — Za pristup Microsoft Foundry i Azure AI Agent Service.
- **Microsoft Foundry Projekt** — Projekt s raspoređenim modelom (npr. `gpt-4o`). Vidi [Korak 1](../../../00-course-setup) ispod.

Uključen je `requirements.txt` u korijenu ovog repozitorija koji sadrži sve nužne Python pakete za pokretanje primjera koda.

Možeš ih instalirati izvršavanjem naredbe u terminalu u korijenskoj mapi repozitorija:

```bash|powershell
pip install -r requirements.txt
```

Preporučujemo stvaranje Python virtualnog okruženja kako bi izbjegao sukobe i probleme.

## Postavljanje VSCode

Pobrini se da koristiš ispravnu verziju Pythona u VSCode-u.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Postavljanje Microsoft Foundry i Azure AI Agent Service

### Korak 1: Kreiraj Microsoft Foundry Projekt

Trebaš Azure AI Foundry **hub** i **projekt** s raspoređenim modelom za pokretanje bilježnica.

1. Idi na [ai.azure.com](https://ai.azure.com) i prijavi se svojim Azure računom.
2. Kreiraj **hub** (ili koristi postojeći). Vidi: [Pregled resursa Huba](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Unutar huba kreiraj **projekt**.
4. Rasporedi model (npr. `gpt-4o`) iz **Models + Endpoints** → **Deploy model**.

### Korak 2: Preuzmi Endpoint Projekta i Ime Rasporeda Modela

Iz projekta u Microsoft Foundry portalu:

- **Endpoint Projekta** — Idi na stranicu **Overview** i kopiraj URL endpointa.

![Project Connection String](../../../translated_images/hr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Ime Rasporeda Modela** — Idi na **Models + Endpoints**, odaberi svoj raspoređeni model i zabilježi **Deployment name** (npr. `gpt-4o`).

### Korak 3: Prijavi se u Azure preko `az login`

Sve bilježnice koriste **`AzureCliCredential`** za autentikaciju — nema potrebe za upravljanjem API ključevima. Za to je potrebno da si prijavljen preko Azure CLI-ja.

1. **Instaliraj Azure CLI** ako već nemaš: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prijavi se** izvršavanjem:

    ```bash|powershell
    az login
    ```

    Ili ako si u udaljenom/Codespace okruženju bez preglednika:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Odaberi svoju pretplatu** ako se to zatraži — izaberi onu koja sadrži tvoj Foundry projekt.

4. **Provjeri** jesi li prijavljen:

    ```bash|powershell
    az account show
    ```

> **Zašto `az login`?** Bilježnice se autentificiraju koristeći `AzureCliCredential` iz paketa `azure-identity`. To znači da tvoja Azure CLI sesija pruža vjerodajnice — nema API ključeva ili tajni u tvojoj `.env` datoteci. Ovo je [najbolja sigurnosna praksa](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Korak 4: Kreiraj svoju `.env` Datoteku

Kopiraj primjer datoteke:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Otvori `.env` i popuni ove dvije vrijednosti:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → tvoj projekt → stranica **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → ime tvog raspoređenog modela |

To je to za većinu lekcija! Bilježnice će se automatski autentificirati putem tvoje `az login` sesije.

### Korak 5: Instaliraj Python Ovisnosti

```bash|powershell
pip install -r requirements.txt
```

Preporučujemo da ovo pokreneš unutar virtualnog okruženja koje si ranije kreirao.

## Dodatno Postavljanje za Lekciju 5 (Agentic RAG)

Lekcija 5 koristi **Azure AI Search** za retrieval-augmented generation. Ako planiraš pokretati tu lekciju, dodaj ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → tvoj **Azure AI Search** resurs → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → tvoj **Azure AI Search** resurs → **Settings** → **Keys** → primarni administratorski ključ |

## Dodatno Postavljanje za Lekciju 6 i Lekciju 8 (GitHub Models)

Neke bilježnice u lekcijama 6 i 8 koriste **GitHub Models** umjesto Azure AI Foundry. Ako planiraš pokretati te primjere, dodaj ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Koristi `https://models.inference.ai.azure.com` (zadana vrijednost) |
| `GITHUB_MODEL_ID` | Ime modela za korištenje (npr. `gpt-4o-mini`) |

## Dodatno Postavljanje za Lekciju 8 (Bing Grounding Workflow)

Uvjetni workflow bilježnica u lekciji 8 koristi **Bing grounding** putem Azure AI Foundry. Ako planiraš pokretati tu bilježnicu, dodaj ovu varijablu u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → tvoj projekt → **Management** → **Connected resources** → tvoja Bing konekcija → kopiraj Connection ID |

## Rješavanje Problema

### SSL Greške pri Verifikaciji Certifikata na macOS-u

Ako si na macOS-u i dobiješ grešku poput:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ovo je poznati problem s Pythonom na macOS-u gdje sustavski SSL certifikati nisu automatski povjereni. Isprobaj sljedeća rješenja redom:

**Opcija 1: Pokreni Pythonov Install Certificates skript (preporučeno)**

```bash
# Zamijenite 3.XX sa svojom instaliranom verzijom Pythona (npr. 3.12 ili 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opcija 2: Koristi `connection_verify=False` u bilježnici (samo za GitHub Models bilježnice)**

U Lekciji 6 bilježnici (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), već postoji komentirani workaround. Odkomentiraj `connection_verify=False` pri kreiranju klijenta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Onemogući provjeru SSL-a ako naiđeš na greške s certifikatom
)
```

> **⚠️ Upozorenje:** Onemogućavanje SSL verifikacije (`connection_verify=False`) smanjuje sigurnost jer preskače provjeru certifikata. Koristi ovo samo kao privremeno rješenje u razvojnom okruženju, nikad u produkciji.

**Opcija 3: Instaliraj i koristi `truststore`**

```bash
pip install truststore
```

Zatim dodaj sljedeće na početak tvoje bilježnice ili skripte prije bilo kakvih mrežnih poziva:

```python
import truststore
truststore.inject_into_ssl()
```

## Zapelo ti je negdje?

Ako imaš problema s ovim postavljanjem, pridruži se našem <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discordu</a> ili <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">otvori issue</a>.

## Sljedeća Lekcija

Sada si spreman za pokretanje koda ovog tečaja. Sretno u učenju o svijetu AI agenata!

[Uvod u AI Agente i primjere korištenja agenata](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj je dokument preveden koristeći AI prevoditeljsku uslugu [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku smatra se službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->