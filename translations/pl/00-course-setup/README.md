# Konfiguracja kursu

## Wprowadzenie

Ta lekcja będzie dotyczyć sposobu uruchamiania przykładów kodu z tego kursu.

## Dołącz do innych uczniów i uzyskaj pomoc

Zanim zaczniesz klonować swoje repozytorium, dołącz do [kanału Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord), aby uzyskać pomoc przy konfiguracji, zadać pytania dotyczące kursu lub połączyć się z innymi uczestnikami.

## Sklonuj lub utwórz fork tego repozytorium

Aby rozpocząć, proszę sklonuj lub utwórz fork repozytorium GitHub. Spowoduje to utworzenie własnej wersji materiałów kursowych, dzięki czemu będziesz mógł uruchamiać, testować i modyfikować kod!

Można to zrobić, klikając link <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">utwórz fork repozytorium</a>

Powinieneś teraz mieć swoją własną wersję kursu dostępną pod następującym linkiem:

![Forked Repo](../../../translated_images/pl/forked-repo.33f27ca1901baa6a.webp)

### Płytkie klonowanie (zalecane dla warsztatów / Codespaces)

  > Pełne repozytorium może być duże (~3 GB) po pobraniu całej historii i wszystkich plików. Jeśli uczestniczysz tylko w warsztacie lub potrzebujesz tylko kilku folderów z lekcjami, płytkie klonowanie (lub klonowanie częściowe) unika pobrania całej historii i/lub pomija niektóre pliki.

#### Szybkie płytkie klonowanie — minimalna historia, wszystkie pliki

Zastąp `<your-username>` w poniższych poleceniach adresem URL twojego forka (lub adresu upstream, jeśli wolisz).

Aby sklonować tylko najnowszą historię commitów (małe pobranie):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Aby sklonować konkretną gałąź:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Częściowe (rzadkie) klonowanie — minimalne pliki + tylko wybrane foldery

To używa częściowego klonowania i sparse-checkout (wymaga Git 2.25+ oraz zaleca się nowoczesne Git z obsługą częściowego klonowania):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Przejdź do folderu repozytorium:

```bash|powershell
cd ai-agents-for-beginners
```

Następnie określ, które foldery chcesz (przykład poniżej pokazuje dwa foldery):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po sklonowaniu i weryfikacji plików, jeśli potrzebujesz tylko plików i chcesz zwolnić miejsce (bez historii git), usuń metadane repozytorium (💀nieodwracalne — stracisz całą funkcjonalność Git: brak commitów, pullów, pushów, ani dostępu do historii).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Używanie GitHub Codespaces (zalecane, aby uniknąć dużych lokalnych pobrań)

- Utwórz nowy Codespace dla tego repozytorium przez [GitHub UI](https://github.com/codespaces).  

- W terminalu nowo utworzonego codespace uruchom jedno z powyższych poleceń płytkiego/rzadkiego klonowania, aby pobrać tylko potrzebne foldery z lekcjami do workspace Codespace.
- Opcjonalnie: po klonowaniu w Codespaces usuń folder .git, aby odzyskać miejsce (zobacz polecenia usuwania powyżej).
- Uwaga: Jeśli wolisz otworzyć repozytorium bezpośrednio w Codespaces (bez dodatkowego klonowania), pamiętaj, że Codespaces zbuduje środowisko devcontainer i może nadal uruchomić więcej zasobów, niż potrzebujesz. Klonowanie płytkiej kopii w świeżym Codespace daje większą kontrolę nad wykorzystaniem dysku.

#### Wskazówki

- Zawsze zastępuj adres URL klonowania swoim forkiem, jeśli chcesz edytować/zatwierdzać zmiany.
- Jeśli później potrzebujesz więcej historii lub plików, możesz je pobrać lub dostosować sparse-checkout, aby uwzględnić dodatkowe foldery.

## Uruchamianie kodu

Ten kurs oferuje serię notatników Jupyter, które możesz uruchamiać, aby zdobyć praktyczne doświadczenie w budowaniu agentów AI.

Przykłady kodu korzystają z **Microsoft Agent Framework (MAF)** z `AzureAIProjectAgentProvider`, który łączy się z **Azure AI Agent Service V2** (API odpowiedzi) przez **Microsoft Foundry**.

Wszystkie notatniki Pythona mają oznaczenie `*-python-agent-framework.ipynb`.

## Wymagania

- Python 3.12+
  - **UWAGA**: Jeśli nie masz zainstalowanego Pythona 3.12, upewnij się, że go zainstalujesz. Następnie utwórz swoje środowisko wirtualne za pomocą python3.12, aby zapewnić poprawne wersje pakietów z pliku requirements.txt.
  
    >Przykład

    Utwórz katalog środowiska wirtualnego Pythona:

    ```bash|powershell
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

- .NET 10+: Dla przykładowych kodów używających .NET zainstaluj [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) lub nowszy. Następnie sprawdź zainstalowaną wersję SDK .NET:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — niezbędne do uwierzytelniania. Zainstaluj ze strony [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Subskrypcja Azure** — dla dostępu do Microsoft Foundry i Azure AI Agent Service.
- **Projekt Microsoft Foundry** — projekt z wdrożonym modelem (np. `gpt-4o`). Zobacz [Krok 1](../../../00-course-setup) poniżej.

W katalogu głównym tego repozytorium znajduje się plik `requirements.txt`, zawierający wszystkie niezbędne pakiety Pythona do uruchomienia przykładów.

Możesz je zainstalować, uruchamiając poniższe polecenie w terminalu w katalogu głównym repozytorium:

```bash|powershell
pip install -r requirements.txt
```

Zalecamy utworzenie wirtualnego środowiska Pythona, aby uniknąć konfliktów i problemów.

## Konfiguracja VSCode

Upewnij się, że w VSCode używasz właściwej wersji Pythona.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Konfiguracja Microsoft Foundry i Azure AI Agent Service

### Krok 1: Utwórz projekt Microsoft Foundry

Aby uruchomić notatniki, potrzebujesz **huba** i **projektu** Microsoft Azure AI Foundry z wdrożonym modelem.

1. Przejdź do [ai.azure.com](https://ai.azure.com) i zaloguj się na swoje konto Azure.
2. Utwórz **hub** (lub użyj już istniejącego). Zobacz: [Przegląd zasobów huba](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. W hubie utwórz **projekt**.
4. Wdróż model (np. `gpt-4o`) z sekcji **Models + Endpoints** → **Deploy model**.

### Krok 2: Pobierz punkt końcowy projektu i nazwę wdrożenia modelu

W portalu projektu Microsoft Foundry:

- **Punkt końcowy projektu** — przejdź do strony **Overview** i skopiuj adres URL endpointu.

![Project Connection String](../../../translated_images/pl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nazwa wdrożenia modelu** — przejdź do **Models + Endpoints**, wybierz wdrożony model i zanotuj **Deployment name** (np. `gpt-4o`).

### Krok 3: Zaloguj się do Azure używając `az login`

Wszystkie notatniki używają **`AzureCliCredential`** do uwierzytelniania — nie ma potrzeby zarządzania kluczami API. Wymaga to zalogowania za pomocą Azure CLI.

1. **Zainstaluj Azure CLI**, jeśli jeszcze tego nie zrobiłeś: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Zaloguj się** za pomocą polecenia:

    ```bash|powershell
    az login
    ```

    Lub, jeśli jesteś w środowisku zdalnym/Codespace bez przeglądarki:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Wybierz subskrypcję**, jeśli zostaniesz o to poproszony — wybierz tę, w której znajduje się twój projekt Foundry.

4. **Sprawdź**, czy jesteś zalogowany:

    ```bash|powershell
    az account show
    ```

> **Dlaczego `az login`?** Notatniki uwierzytelniają się za pomocą `AzureCliCredential` z pakietu `azure-identity`. Oznacza to, że sesja Azure CLI dostarcza dane uwierzytelniające — nie musisz mieć kluczy API ani sekretów w pliku `.env`. To jest [dobry standard bezpieczeństwa](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Krok 4: Utwórz plik `.env`

Skopiuj plik przykładowy:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Otwórz `.env` i uzupełnij te dwie wartości:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → twój projekt → strona **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → nazwa twojego wdrożonego modelu |

To wszystko dla większości lekcji! Notatniki uwierzytelniają się automatycznie przez twoją sesję `az login`.

### Krok 5: Zainstaluj zależności Pythona

```bash|powershell
pip install -r requirements.txt
```

Zalecamy uruchomienie tego we wcześniej utworzonym środowisku wirtualnym.

## Dodatkowa konfiguracja do Lekcji 5 (Agentic RAG)

Lekcja 5 używa **Azure AI Search** do generowania wspomaganego wyszukiwaniem. Jeśli planujesz uruchomić tę lekcję, dodaj te zmienne do pliku `.env`:

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → twoje zasoby **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Portal Azure → twoje zasoby **Azure AI Search** → **Settings** → **Keys** → klucz administracyjny podstawowy |

## Dodatkowa konfiguracja do Lekcji 6 i Lekcji 8 (Modele GitHub)

Niektóre notatniki w lekcjach 6 i 8 używają **GitHub Models** zamiast Azure AI Foundry. Jeśli planujesz uruchomić te przykłady, dodaj te zmienne do pliku `.env`:

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Użyj `https://models.inference.ai.azure.com` (wartość domyślna) |
| `GITHUB_MODEL_ID` | Nazwa modelu do użycia (np. `gpt-4o-mini`) |

## Dodatkowa konfiguracja do Lekcji 8 (Bing Grounding Workflow)

Warunkowy notatnik przepływu pracy z lekcji 8 używa **Bing grounding** przez Azure AI Foundry. Jeśli planujesz uruchomić ten przykład, dodaj tę zmienną do pliku `.env`:

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal Azure AI Foundry → twój projekt → **Management** → **Connected resources** → twoje połączenie Bing → skopiuj ID połączenia |

## Rozwiązywanie problemów

### Błędy weryfikacji certyfikatu SSL na macOS

Jeśli korzystasz z macOS i napotkasz błąd podobny do:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

To znany problem z Pythonem na macOS, gdzie systemowe certyfikaty SSL nie są automatycznie zaufane. Spróbuj poniższych rozwiązań w kolejności:

**Opcja 1: Uruchom skrypt instalacji certyfikatów Pythona (zalecane)**

```bash
# Zastąp 3.XX zainstalowaną wersją Pythona (np. 3.12 lub 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opcja 2: Użyj `connection_verify=False` w notatniku (tylko dla notatników GitHub Models)**

W notatniku Lekcji 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) jest już zawarte zakomentowane rozwiązanie. Odkomentuj `connection_verify=False` podczas tworzenia klienta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Wyłącz weryfikację SSL, jeśli napotkasz błędy certyfikatu
)
```

> **⚠️ Ostrzeżenie:** Wyłączenie weryfikacji SSL (`connection_verify=False`) zmniejsza bezpieczeństwo, pomijając sprawdzanie certyfikatów. Używaj tego tylko jako tymczasowe rozwiązanie w środowiskach deweloperskich, nigdy w produkcji.

**Opcja 3: Zainstaluj i użyj `truststore`**

```bash
pip install truststore
```

Następnie dodaj poniższe na początku swojego notatnika lub skryptu, przed jakimikolwiek wywołaniami sieciowymi:

```python
import truststore
truststore.inject_into_ssl()
```

## Utknąłeś gdzieś?

Jeśli masz jakiekolwiek problemy z uruchomieniem tego setupu, dołącz do naszej <a href="https://discord.gg/kzRShWzttr" target="_blank">Społeczności Azure AI na Discord</a> lub <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">zglos problem</a>.

## Następna lekcja

Jesteś teraz gotowy do uruchomienia kodu dla tego kursu. Powodzenia w dalszej nauce o świecie agentów AI!

[Wprowadzenie do Agentów AI i przypadków użycia agentów](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Ten dokument został przetłumaczony przy użyciu usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło ostateczne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->