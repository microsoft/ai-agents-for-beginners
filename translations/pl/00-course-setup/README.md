# Konfiguracja kursu

## Wprowadzenie

Ta lekcja pokaże, jak uruchomić przykładowe kody z tego kursu.

## Dołącz do innych uczniów i uzyskaj pomoc

Zanim zaczniesz klonować swoje repozytorium, dołącz do [kanału Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord), aby uzyskać pomoc przy konfiguracji, zadawać pytania dotyczące kursu lub nawiązać kontakty z innymi uczniami.

## Sklonuj lub forkuj to repozytorium

Aby rozpocząć, proszę sklonuj lub forkuj repozytorium GitHub. Dzięki temu stworzysz swoją własną wersję materiałów kursu, aby móc uruchamiać, testować i modyfikować kod!

Można to zrobić klikając na link <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forkuj repozytorium</a>

Powinieneś teraz mieć własną forę tego kursu pod następującym linkiem:

![Forked Repo](../../../translated_images/pl/forked-repo.33f27ca1901baa6a.webp)

### Płytkie klonowanie (zalecane dla warsztatów / Codespaces)

  >Pełne repozytorium może być duże (~3 GB), gdy pobierzesz pełną historię i wszystkie pliki. Jeśli uczestniczysz tylko w warsztacie lub potrzebujesz kilku folderów z lekcjami, płytkie klonowanie (lub rzadkie klonowanie) pobiera znacznie mniej.

#### Szybkie płytkie klonowanie — minimalna historia, wszystkie pliki

Zamień `<your-username>` w poniższych poleceniach na URL twojego fork (lub URL oryginalnego repozytorium jeśli wolisz).

Aby sklonować tylko najnowszą historię commitów (mały download):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Aby sklonować konkretną gałąź:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Częściowe (rzadkie) klonowanie — minimalne bloby + tylko wybrane foldery

To wykorzystuje częściowe klonowanie i sparse-checkout (wymaga Git 2.25+ i zalecanego nowoczesnego Gita z obsługą częściowego klonowania):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Przejdź do folderu repozytorium:

```bash
cd ai-agents-for-beginners
```

Następnie określ, które foldery chcesz (przykład poniżej pokazuje dwa foldery):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po sklonowaniu i weryfikacji plików, jeśli potrzebujesz tylko plików i chcesz zwolnić miejsce (bez historii git), usuń metadane repozytorium (💀nieodwracalne — stracisz całą funkcjonalność Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Korzystanie z GitHub Codespaces (zalecane, aby uniknąć dużych lokalnych pobrań)

- Utwórz nowy Codespace dla tego repozytorium przez [GitHub UI](https://github.com/codespaces).  

- W terminalu nowo utworzonego Codespace uruchom jedno z poleceń płytkiego/rzadkiego klonowania powyżej, aby pobrać tylko potrzebne foldery z lekcjami do przestrzeni roboczej Codespace.
- Opcjonalnie: po sklonowaniu wewnątrz Codespaces usuń .git, aby odzyskać dodatkową przestrzeń (zobacz polecenia usuwania powyżej).
- Uwaga: jeśli wolisz otworzyć repo bezpośrednio w Codespaces (bez dodatkowego klonowania), pamiętaj, że Codespaces utworzy środowisko devcontainer i nadal może przygotować więcej niż potrzebujesz.

#### Wskazówki

- Zawsze zamień URL klonowania na swój fork, jeśli chcesz edytować/commitować.
- Jeśli później potrzebujesz więcej historii lub plików, możesz je pobrać lub dostosować sparse-checkout, aby uwzględnić dodatkowe foldery.

## Uruchamianie kodu

Ten kurs oferuje serię notatników Jupyter, które możesz uruchamiać, aby zdobyć praktyczne doświadczenie w budowaniu Agentów AI.

Przykładowe kody używają **Microsoft Agent Framework (MAF)** wraz z `FoundryChatClient`, który łączy się z **Microsoft Foundry Agent Service V2** (API Odpowiedzi) poprzez **Microsoft Foundry**.

Wszystkie notatniki Pythona są oznaczone jako `*-python-agent-framework.ipynb`.

## Wymagania

- Python 3.12+
  - **UWAGA**: Jeżeli nie masz zainstalowanego Pythona 3.12, upewnij się, że go zainstalujesz. Następnie utwórz środowisko wirtualne (venv) używając python3.12, aby zapewnić instalację odpowiednich wersji z pliku requirements.txt.
  
    >Przykład

    Utwórz katalog venv Pythona:

    ```bash
    python -m venv venv
    ```

    Następnie aktywuj środowisko venv dla:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Dla przykładowych kodów korzystających z .NET, upewnij się, że zainstalowałeś [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) lub nowszą wersję. Następnie sprawdź zainstalowaną wersję SDK .NET:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — wymagany do uwierzytelniania. Zainstaluj z [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Subskrypcja Azure** — do dostępu do Microsoft Foundry i Microsoft Foundry Agent Service.
- **Projekt Microsoft Foundry** — projekty z wdrożonym modelem (np. `gpt-5-mini`). Zobacz [Krok 1](#krok-1-utwórz-projekt-microsoft-foundry) poniżej.

Dołączyliśmy plik `requirements.txt` w katalogu głównym tego repozytorium, który zawiera wszystkie potrzebne pakiety Pythona do uruchomienia przykładów.

Możesz je zainstalować uruchamiając poniższe polecenie w terminalu w katalogu głównym repozytorium:

```bash
pip install -r requirements.txt
```

Zalecamy utworzenie wirtualnego środowiska Pythona, aby uniknąć konfliktów i problemów.

## Konfiguracja VSCode

Upewnij się, że w VSCode używasz odpowiedniej wersji Pythona.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Konfiguracja Microsoft Foundry i Microsoft Foundry Agent Service

### Krok 1: Utwórz projekt Microsoft Foundry

Potrzebujesz **hub** i **projektu** w Microsoft Foundry z wdrożonym modelem, aby uruchomić notatniki.

1. Wejdź na [ai.azure.com](https://ai.azure.com) i zaloguj się na konto Azure.
2. Utwórz **hub** (lub użyj istniejącego). Zobacz: [Przegląd zasobów hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. W hub utwórz **projekt**.
4. Wdróż model (np. `gpt-5-mini`) z **Models + Endpoints** → **Deploy model**.

### Krok 2: Pobierz adres endpointu projektu i nazwę wdrożenia modelu

Z twojego projektu w portalu Microsoft Foundry:

- **Endpoint projektu** — przejdź na stronę **Overview** i skopiuj URL endpointu.

![Project Connection String](../../../translated_images/pl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nazwa wdrożenia modelu** — przejdź do **Models + Endpoints**, wybierz wdrożony model i zanotuj **Deployment name** (np. `gpt-5-mini`).

### Krok 3: Zaloguj się do Azure przez `az login`

Większość notatników uwierzytelnia się przez **logowanie Azure CLI** — używając `AzureCliCredential` lub `DefaultAzureCredential` (oba pobierają sesję `az login`) z pakietu `azure-identity` — więc nie wymagają kluczy API. Kilka lekcji i opcjonalnych integracji korzysta z kluczy API; sprawdź wymagania każdej lekcji pod kątem dodatkowych zmiennych środowiskowych. Wymaga to zalogowania się przez Azure CLI.

1. **Zainstaluj Azure CLI** jeśli jeszcze tego nie zrobiłeś: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Zaloguj się** uruchamiając:

    ```bash
    az login
    ```

    Lub jeśli jesteś w zdalnym środowisku/Codespace bez przeglądarki:

    ```bash
    az login --use-device-code
    ```

3. **Wybierz subskrypcję** jeśli zostanie pokazane — wybierz tę, która zawiera projekt Foundry.

4. **Sprawdź** czy jesteś zalogowany:

    ```bash
    az account show
    ```

> **Dlaczego `az login`?** Notatniki uwierzytelniają się z `AzureCliCredential` (lub `DefaultAzureCredential`, który też pobiera logowanie Azure CLI) z pakietu `azure-identity`. Oznacza to, że sesja Azure CLI dostarcza poświadczenia — bez kluczy API lub sekretów w pliku `.env`. To jest [bezpieczna najlepsza praktyka](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Krok 4: Utwórz swój plik `.env`

Skopiuj przykładowy plik:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Otwórz `.env` i wypełnij te dwie wartości:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → twój projekt → strona **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → nazwa twojego wdrożonego modelu |

To wszystko dla większości lekcji! Notatniki uwierzytelnią się automatycznie przez twoją sesję `az login`.

### Krok 5: Zainstaluj zależności Pythona

```bash
pip install -r requirements.txt
```

Zalecamy uruchomienie tego wewnątrz wcześniej utworzonego środowiska wirtualnego.

## Opcjonalna konfiguracja: Azure AI Search (lekcje 5 i 16)

Notatniki z lekcji 5 (Agentic RAG) i 16 działają od razu z **pamięciową bazą wiedzy** — bez potrzeby dodatkowych zasobów Azure. Jeśli chcesz je wesprzeć prawdziwym indeksem **Azure AI Search**, pamiętaj, że **notatnik z lekcji 16 aktualnie wymaga uwierzytelniania opartego na kluczach**: przełącza się z wyszukiwania w pamięci na Azure AI Search tylko gdy **zarówno** `AZURE_SEARCH_SERVICE_ENDPOINT` **jak i** `AZURE_SEARCH_API_KEY` są ustawione, w przeciwnym razie pozostaje w wyszukiwaniu pamięciowym — więc aby uruchomić go z prawdziwym indeksem, musisz też ustawić klucz administratora. Bezkluczowe uwierzytelnianie za pomocą Microsoft Entra ID (RBAC) jest zalecanym podejściem dla własnego kodu produkcyjnego, zgodnym z przepływem `az login` używanym w całym kursie.

Poniższe kroki RBAC odnoszą się do przykładów przewodnika konfiguracji i twojego własnego kodu. Nie włączają bezkluczowego uwierzytelniania w notatniku lekcji 16; lekcja 16 nadal wymaga obu, endpoint i klucza administratora, do korzystania z Azure AI Search.

1. **Włącz dostęp oparty na rolach** w usłudze wyszukiwania:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Przypisz sobie wymagane role** (tworzenie/ładowanie indeksów i zapytania):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Dodaj endpoint** do pliku `.env`:

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → twój zasób **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Wymagany (razem z endpointem) do uruchomienia Azure AI Search w notatniku z lekcji 16, który używa uwierzytelniania opartego na kluczu. Portal Azure → **Settings** → **Keys** → główny klucz administratora |

> **Dlaczego bezkluczowe?** Klucze administratorów dają pełny dostęp do zapisu do usługi wyszukiwania i mogą wyciec przez pliki `.env`. Z RBAC twoja tożsamość z `az login` jest używana zamiast tego — ten sam schemat bezkluczowego Entra ID, który notatniki kursu używają (poprzez `AzureCliCredential` / `DefaultAzureCredential`). Zobacz [Połącz się z Azure AI Search za pomocą ról](https://learn.microsoft.com/azure/search/search-security-rbac).

Zobacz [przewodnik konfiguracji Azure AI Search](./AzureSearch.md) dla pełnych przykładów tworzenia indeksów w Python i .NET.

## Dodatkowa konfiguracja dla lekcji wywołujących bezpośrednio Azure OpenAI (lekcje 6 i 8)

Niektóre notatniki z lekcji 6 i 8 wywołują bezpośrednio **Azure OpenAI** (używając **Responses API**) zamiast korzystać z projektu Microsoft Foundry. Przykłady te wcześniej wykorzystywały GitHub Models, które są przestarzałe i nie obsługują Responses API. Dodaj te zmienne do swojego pliku `.env`:

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → twój zasób **Azure OpenAI** → **Keys and Endpoint** → Endpoint (np. `https://<twoj-zasob>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Nazwa wdrożonego modelu (np. `gpt-5-mini`), który obsługuje Responses API |
| `AZURE_OPENAI_API_KEY` | Opcjonalne — tylko jeśli korzystasz z uwierzytelniania opartego na kluczu zamiast `az login` / Entra ID |

> Responses API używa stabilnego endpointu `/openai/v1/`, więc nie wymaga `api-version`. Zaloguj się przez `az login`, aby użyć bezkluczowego uwierzytelniania Entra ID.

## Alternatywny dostawca: MiniMax (zgodny z OpenAI)

[MiniMax](https://platform.minimaxi.com/) dostarcza modele z dużym kontekstem (do 204 tys. tokenów) przez OpenAI-kompatybilne API. Ponieważ `OpenAIChatClient` w Microsoft Agent Framework działa z dowolnym endpointem kompatybilnym z OpenAI, możesz użyć MiniMax jako zamiennik w lekcjach korzystających z `OpenAIChatClient`.

Dodaj te zmienne do pliku `.env`:

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Platforma MiniMax](https://platform.minimaxi.com/) → Klucze API |
| `MINIMAX_BASE_URL` | Użyj `https://api.minimax.io/v1` (wartość domyślna) |
| `MINIMAX_MODEL_ID` | Nazwa modelu do użycia (np. `MiniMax-M3`) |

**Przykładowe modele**: `MiniMax-M3` (zalecany), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (szybsze odpowiedzi). Nazwy i dostępność modeli mogą się zmieniać, a dostęp do konkretnego modelu może zależeć od twojego konta.

Przykłady kodu używające `OpenAIChatClient` (np. przepływ rezerwacji hotelu z lekcji 14) automatycznie wykryją i użyją konfiguracji MiniMax, gdy `MINIMAX_API_KEY` jest ustawiony.


## Alternatywny Dostawca: Novita AI (kompatybilny z OpenAI)

[Novita AI](https://novita.ai/llm-api) udostępnia API kompatybilne z OpenAI dla otwartych i najnowocześniejszych modeli językowych (DeepSeek, Llama, Qwen i inne). Ponieważ `OpenAIChatClient` Microsoft Agent Framework działa z każdym końcowym punktem zgodnym z OpenAI, możesz używać Novita AI jako bezpośredniej alternatywy dla Azure OpenAI lub OpenAI.

Dodaj te zmienne do swojego pliku `.env`:

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `NOVITA_API_KEY` | [Panel Novita AI](https://novita.ai/settings/key-management) → Klucze API |
| `NOVITA_BASE_URL` | Użyj `https://api.novita.ai/openai/v1` (wartość domyślna) |
| `NOVITA_MODEL_ID` | Nazwa modelu do użycia (np. `moonshotai/kimi-k3`) |

**Przykładowe modele**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI hostuje także wiele innych rodzin modeli open source (Llama, Qwen, GLM i inne) — sprawdź [bibliotekę modeli Novita AI](https://novita.ai/llm-api) dla aktualnej listy dostępnych modeli i ich identyfikatorów.

Aktualne przykłady nie korzystają automatycznie ze zmiennych `NOVITA_*`. Aby użyć Novita AI, przekaż te wartości jawnie podczas tworzenia `OpenAIChatClient` w uruchamianym przykładzie.

## Alternatywny Dostawca: Foundry Local (uruchamiaj modele lokalnie)

[Foundry Local](https://foundrylocal.ai) to lekki runtime, który pobiera, zarządza i udostępnia modele językowe **całkowicie na Twoim własnym urządzeniu** przez API kompatybilne z OpenAI — bez konieczności chmury.

Ponieważ `OpenAIChatClient` Microsoft Agent Framework działa z każdym końcowym punktem zgodnym z OpenAI, Foundry Local jest lokalną bezpośrednią alternatywą dla Azure OpenAI.

**1. Zainstaluj Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Pobierz i uruchom model** (to również uruchomi lokalną usługę):

```bash
foundry model list          # zobacz dostępne modele
foundry model run phi-4-mini
```

**3. Zainstaluj SDK w Pythonie** używane do odkrywania lokalnego punktu końcowego:

```bash
pip install foundry-local-sdk
```

**4. Skieruj Microsoft Agent Framework na lokalny model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Pobiera (jeśli potrzebne) i udostępnia model lokalnie, następnie odnajduje punkt końcowy/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # np. http://localhost:<port>/v1
    api_key=manager.api_key,        # zawsze "nie-wymagane" dla Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Uwaga:** Foundry Local udostępnia OpenAI-kompatybilny punkt końcowy **Chat Completions**. Używaj go do rozwoju lokalnego i scenariuszy offline. Aby uzyskać pełen zestaw funkcji **Responses API** (stanowe konwersacje itp.), używaj Azure OpenAI lub projektu Microsoft Foundry.

## Dodatkowa konfiguracja do Lekcji 8 (workflow Bing Grounding)

Notebook z workflow warunkowym w lekcji 8 używa **Bing grounding** przez Microsoft Foundry. Jeśli planujesz uruchomić ten przykład, dodaj tę zmienną do swojego pliku `.env`:

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal Microsoft Foundry → twój projekt → **Zarządzanie** → **Połączone zasoby** → twoje połączenie Bing → skopiuj identyfikator połączenia |

## Rozwiązywanie problemów

### Błędy weryfikacji certyfikatu SSL na macOS

Jeśli używasz macOS i napotkasz błąd taki jak:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Jest to znany problem z Pythonem na macOS, gdzie systemowe certyfikaty SSL nie są automatycznie uznawane za zaufane. Spróbuj następujących rozwiązań w kolejności:

**Opcja 1: Uruchom skrypt instalujący certyfikaty Pythona (zalecane)**

```bash
# Zamień 3.XX na zainstalowaną wersję Pythona (np. 3.12 lub 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opcja 2: Użyj `connection_verify=False` w notebooku (tylko dla notebooków GitHub Models)**

W notebooku Lekcji 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) znajduje się już zakomentowany obejście. Odkomentuj `connection_verify=False` gdy pojawią się błędy certyfikatu:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Wyłącz weryfikację SSL, jeśli pojawią się błędy certyfikatu
)
```

> **⚠️ Ostrzeżenie:** Wyłączenie weryfikacji SSL (`connection_verify=False`) zmniejsza bezpieczeństwo, pomijając walidację certyfikatu. Używaj tego tylko jako tymczasowego obejścia w środowiskach deweloperskich. Nigdy nie stosuj tego w produkcji.

**Opcja 3: Zainstaluj i użyj `truststore`**

```bash
pip install truststore
```

Następnie dodaj poniższe na początku notebooka lub skryptu przed wykonywaniem jakichkolwiek wywołań sieciowych:

```python
import truststore
truststore.inject_into_ssl()
```

## Utknąłeś gdzieś?

Jeśli masz problemy z uruchomieniem tej konfiguracji, dołącz do naszego <a href="https://discord.gg/kzRShWzttr" target="_blank">Discorda Społeczności Azure AI</a> lub <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">załóż zgłoszenie</a>.

## Następna Lekcja

Jesteś teraz gotowy, aby uruchomić kod tego kursu. Życzymy owocnej nauki o świecie Agentów AI!

[Wprowadzenie do Agentów AI i Zastosowań Agentów](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->