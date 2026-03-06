# Postavljanje tečaja

## Uvod

Ova lekcija će obuhvatiti kako pokrenuti primjere koda ovog tečaja.

## Pridružite se drugim polaznicima i zatražite pomoć

Prije nego što počnete klonirati svoj repozitorij, pridružite se [AI Agents For Beginners Discord kanalu](https://aka.ms/ai-agents/discord) kako biste dobili pomoć sa postavljanjem, postavljali pitanja o tečaju ili se povezali s drugim polaznicima.

## Klonirajte ili forkajte ovaj repozitorij

Za početak, molimo klonirajte ili forkajte GitHub repozitorij. To će vam omogućiti vlastitu verziju materijala tečaja kako biste mogli pokretati, testirati i prilagođavati kod!

To možete učiniti klikom na link <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forkajte repozitorij</a>

Sada biste trebali imati vlastitu forkanu verziju ovog tečaja na sljedećem linku:

![Forked Repo](../../../translated_images/hr/forked-repo.33f27ca1901baa6a.webp)

### Plitko kloniranje (preporučeno za radionicu / Codespaces)

  >Cijeli repozitorij može biti velik (~3 GB) kada preuzimate punu povijest i sve datoteke. Ako sudjelujete samo na radionici ili vam trebaju samo određene mape lekcija, plitko kloniranje (ili rijetko kloniranje) izbjegava većinu preuzimanja skraćivanjem povijesti i/ili izostavljanjem blobova.

#### Brzo plitko kloniranje — minimalna povijest, sve datoteke

Zamijenite `<your-username>` u naredbama u nastavku sa URL-om vašeg forka (ili s URL-om originalnog repozitorija ako želite).

Za kloniranje samo najnovije povijesti komita (malo preuzimanja):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Za kloniranje određene grane:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Djelomično (rijetko) kloniranje — minimalni blobovi + samo odabrane mape

Ovo koristi djelomično kloniranje i sparse-checkout (zahtijeva Git 2.25+ i preporučuje se moderni Git s podrškom za djelomično kloniranje):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Uđite u mapu repozitorija:

```bash|powershell
cd ai-agents-for-beginners
```

Onda navedite koje mape želite (u primjeru su prikazane dvije mape):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Nakon kloniranja i provjere datoteka, ako vam trebaju samo datoteke i želite osloboditi prostor (bez git povijesti), molimo obrišite metapodatke repozitorija (💀nepovratno — izgubit ćete svu Git funkcionalnost: nema commitova, pullova, pushova, niti pristupa povijesti).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Korištenje GitHub Codespaces (preporučeno za izbjegavanje velikih lokalnih preuzimanja)

- Kreirajte novi Codespace za ovaj repozitorij putem [GitHub UI](https://github.com/codespaces).  

- U terminalu novokreiranog Codespacea pokrenite jednu od gore navedenih plitkih/rijetkih klon naredbi da unesete u Codespace radni prostor samo mape lekcija koje su vam potrebne.
- Opcionalno: nakon kloniranja unutar Codespaces, uklonite .git kako biste oslobodili dodatni prostor (pogledajte naredbe za uklanjanje gore).
- Napomena: Ako preferirate otvoriti repozitorij direktno u Codespaces (bez dodatnog kloniranja), imajte na umu da će Codespaces stvoriti razvojno okruženje (devcontainer) i može još uvijek imat veći prostor nego što vam treba. Kloniranje plitke kopije unutar svježeg Codespacea pruža vam veću kontrolu nad prostorom na disku.

#### Savjeti

- Uvijek zamijenite URL kloniranja s URL-om vašeg forka ako želite uređivati/commitati.
- Ako kasnije trebate više povijesti ili datoteka, možete ih dohvatiti ili prilagoditi sparse-checkout da uključuje dodatne mape.

## Pokretanje koda

Ovaj tečaj nudi niz Jupyter bilježnica koje možete pokretati kako biste stekli praktično iskustvo u izgradnji AI agenata.

Primjeri koda koriste **Microsoft Agent Framework (MAF)** s `AzureAIProjectAgentProvider` koji se povezuje na **Azure AI Agent Service V2** (Responses API) kroz **Microsoft Foundry**.

Sve Python bilježnice označene su kao `*-python-agent-framework.ipynb`.

## Zahtjevi

- Python 3.12+
  - **NAPOMENA**: Ako nemate instaliran Python3.12, osigurajte da ga instalirate. Zatim kreirajte svoje virtualno okruženje koristeći python3.12 da biste osigurali instalaciju ispravnih verzija iz datoteke requirements.txt.
  
    >Primjer

    Kreirajte Python virtualno okruženje:

    ```bash|powershell
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

- .NET 10+: Za uzorke koda koji koriste .NET, instalirajte [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ili noviji. Zatim provjerite verziju instaliranog .NET SDK-a:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Potrebno za autentikaciju. Instalirajte s [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure pretplata** — Za pristup Microsoft Foundry i Azure AI Agent Service.
- **Microsoft Foundry projekt** — Projekt s implementiranim modelom (npr. `gpt-4o`). Pogledajte [Korak 1](../../../00-course-setup) dolje.

Uključili smo datoteku `requirements.txt` u korijenu ovog repozitorija koja sadrži sve potrebne Python pakete za pokretanje primjera koda.

Možete ih instalirati pokretanjem sljedeće naredbe u vašem terminalu, u korijenu repozitorija:

```bash|powershell
pip install -r requirements.txt
```

Preporučujemo kreiranje Python virtualnog okruženja kako biste izbjegli sukobe i probleme.

## Postavljanje VSCode-a

Provjerite koristite li ispravnu verziju Pythona u VSCode-u.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Postavljanje Microsoft Foundry i Azure AI Agent Service

### Korak 1: Kreirajte Microsoft Foundry projekt

Trebate Azure AI Foundry **hub** i **projekt** s implementiranim modelom za pokretanje bilježnica.

1. Idite na [ai.azure.com](https://ai.azure.com) i prijavite se sa svojim Azure računom.
2. Kreirajte **hub** (ili koristite postojeći). Pogledajte: [Pregled hub resursa](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Unutar huba kreirajte **projekt**.
4. Implementirajte model (npr. `gpt-4o`) iz **Models + Endpoints** → **Deploy model**.

### Korak 2: Dohvatite URL krajnje točke projektnog endpointa i naziv implementacije modela

Iz vašeg projekta u Microsoft Foundry portalu:

- **Project Endpoint** — Idite na stranicu **Overview** i kopirajte URL krajnje točke.

![Project Connection String](../../../translated_images/hr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Idite na **Models + Endpoints**, odaberite svoj implementirani model i zabilježite **Deployment name** (npr. `gpt-4o`).

### Korak 3: Prijavite se u Azure s `az login`

Sve bilježnice koriste **`AzureCliCredential`** za autentikaciju — nema API ključeva za upravljanje. To zahtijeva da ste prijavljeni putem Azure CLI.

1. **Instalirajte Azure CLI** ako već niste: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Prijavite se** pokretanjem:

    ```bash|powershell
    az login
    ```

    Ili ako ste u udaljenom/Codespace okruženju bez preglednika:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Odaberite svoju pretplatu** ako vas zatraži — izaberite onu koja sadrži vaš Foundry projekt.

4. **Provjerite** jeste li prijavljeni:

    ```bash|powershell
    az account show
    ```

> **Zašto `az login`?** Bilježnice se autentificiraju koristeći `AzureCliCredential` iz paketa `azure-identity`. To znači da vaša Azure CLI sesija pruža vjerodajnice — nema API ključeva niti tajni u vašoj `.env` datoteci. Ovo je [sigurnosna najbolja praksa](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → vaš projekt → stranica **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → naziv vašeg implementiranog modela |

To je gotovo za većinu lekcija! Bilježnice će se automatski autentificirati kroz vašu `az login` sesiju.

### Korak 5: Instalirajte Python ovisnosti

```bash|powershell
pip install -r requirements.txt
```

Preporučujemo pokretanje unutar virtualnog okruženja koje ste ranije kreirali.

## Dodatno postavljanje za Lekciju 5 (Agentic RAG)

Lekcija 5 koristi **Azure AI Search** za retrieval-augmented generation. Ako planirate pokrenuti tu lekciju, dodajte ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → vaš **Azure AI Search** resurs → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → vaš **Azure AI Search** resurs → **Settings** → **Keys** → primarni administratorski ključ |

## Dodatno postavljanje za Lekcije 6 i 8 (GitHub modeli)

Neke bilježnice u lekcijama 6 i 8 koriste **GitHub modele** umjesto Azure AI Foundry. Ako planirate pokrenuti te uzorke, dodajte ove varijable u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Koristite `https://models.inference.ai.azure.com` (zadana vrijednost) |
| `GITHUB_MODEL_ID` | Naziv modela za korištenje (npr. `gpt-4o-mini`) |

## Dodatno postavljanje za Lekciju 8 (Bing Grounding Workflow)

Uvjetovana radna bilježnica u lekciji 8 koristi **Bing grounding** putem Azure AI Foundry. Ako planirate pokrenuti taj uzorak, dodajte ovu varijablu u svoju `.env` datoteku:

| Varijabla | Gdje je pronaći |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → vaš projekt → **Management** → **Connected resources** → vaša Bing veza → kopirajte ID veze |

## Rješavanje problema

### Pogreške verifikacije SSL certifikata na macOS-u

Ako ste na macOS i naiđete na pogrešku poput:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ovo je poznati problem s Pythonom na macOS-u gdje se sustavski SSL certifikati ne smatraju automatski pouzdanima. Isprobajte sljedeća rješenja redom:

**Opcija 1: Pokrenite Pythonov skript za instalaciju certifikata (preporučeno)**

```bash
# Zamijenite 3.XX vašom instaliranom verzijom Pythona (npr. 3.12 ili 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opcija 2: Koristite `connection_verify=False` u svojoj bilježnici (samo za GitHub Models bilježnice)**

U bilježnici Lekcije 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) već je uključen zakomentirani zaobilazni put. Odkomentirajte `connection_verify=False` prilikom stvaranja klijenta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Onemogućite SSL provjeru ako naiđete na pogreške sa certifikatom
)
```

> **⚠️ Upozorenje:** Onemogućavanje SSL verifikacije (`connection_verify=False`) smanjuje sigurnost preskačući provjeru certifikata. Koristite ovo samo kao privremeno rješenje u razvojnim okruženjima, nikada u produkciji.

**Opcija 3: Instalirajte i koristite `truststore`**

```bash
pip install truststore
```

Zatim dodajte sljedeće na vrh bilježnice ili skripte prije izvođenja bilo kakvih mrežnih poziva:

```python
import truststore
truststore.inject_into_ssl()
```

## Zapeli ste negdje?

Ako imate bilo kakvih problema s pokretanjem ovog postavljanja, pridružite se našem <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ili <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">kreirajte issue</a>.

## Sljedeća lekcija

Sada ste spremni pokrenuti kod za ovaj tečaj. Sretno u daljnjem učenju svijeta AI agenata!

[Uvod u AI agente i primjere upotrebe agenata](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj je dokument preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, molimo imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->