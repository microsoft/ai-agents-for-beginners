<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c55b973b1562abf5aadf6a4028265ac5",
  "translation_date": "2025-08-30T08:41:31+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "pl"
}
-->
# Konfiguracja Kursu

## Wprowadzenie

W tej lekcji dowiesz się, jak uruchamiać przykłady kodu z tego kursu.

## Dołącz do innych uczestników i uzyskaj pomoc

Zanim sklonujesz repozytorium, dołącz do [kanału Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord), aby uzyskać pomoc w konfiguracji, odpowiedzi na pytania dotyczące kursu lub nawiązać kontakt z innymi uczestnikami.

## Sklonuj lub zforkuj to repozytorium

Na początek sklonuj lub zforkuj repozytorium GitHub. Dzięki temu będziesz mieć własną wersję materiałów kursowych, aby móc uruchamiać, testować i modyfikować kod!

Możesz to zrobić, klikając link do

Powinieneś teraz mieć własną zforkowaną wersję tego kursu pod następującym linkiem:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.pl.png)

## Uruchamianie kodu

Ten kurs oferuje serię notatników Jupyter, które możesz uruchomić, aby zdobyć praktyczne doświadczenie w budowaniu agentów AI.

Przykłady kodu wykorzystują:

**Wymaga konta GitHub - Bezpłatne**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Oznaczone jako (semantic-kernel.ipynb)  
2) AutoGen Framework + GitHub Models Marketplace. Oznaczone jako (autogen.ipynb)  

**Wymaga subskrypcji Azure**:  
3) Azure AI Foundry + Azure AI Agent Service. Oznaczone jako (azureaiagent.ipynb)  

Zachęcamy do wypróbowania wszystkich trzech typów przykładów, aby zobaczyć, który z nich najlepiej Ci odpowiada.

Opcja, którą wybierzesz, określi, które kroki konfiguracji musisz wykonać poniżej:

## Wymagania

- Python 3.12+  
  - **NOTE**: Jeśli nie masz zainstalowanego Python3.12, upewnij się, że go zainstalujesz. Następnie utwórz swoje środowisko wirtualne (venv) za pomocą python3.12, aby upewnić się, że odpowiednie wersje zostaną zainstalowane z pliku requirements.txt.  
- Konto GitHub - Dostęp do GitHub Models Marketplace  
- Subskrypcja Azure - Dostęp do Azure AI Foundry  
- Konto Azure AI Foundry - Dostęp do Azure AI Agent Service  

Dołączony został plik `requirements.txt` w głównym katalogu tego repozytorium, który zawiera wszystkie wymagane pakiety Python do uruchamiania przykładów kodu.

Możesz je zainstalować, uruchamiając następujące polecenie w terminalu w głównym katalogu repozytorium:

```bash
pip install -r requirements.txt
```  
Zalecamy utworzenie wirtualnego środowiska Python, aby uniknąć konfliktów i problemów.

## Konfiguracja VSCode

Upewnij się, że używasz odpowiedniej wersji Pythona w VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Konfiguracja dla przykładów z użyciem GitHub Models

### Krok 1: Pobierz swój GitHub Personal Access Token (PAT)

Ten kurs wykorzystuje GitHub Models Marketplace, oferując bezpłatny dostęp do dużych modeli językowych (LLM), które wykorzystasz do budowy agentów AI.

Aby korzystać z GitHub Models, musisz utworzyć [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Możesz to zrobić, przechodząc do swojego konta GitHub.

Proszę postępować zgodnie z [zasadą minimalnych uprawnień](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) podczas tworzenia tokena. Oznacza to, że powinieneś nadać tokenowi tylko te uprawnienia, które są potrzebne do uruchamiania przykładów kodu w tym kursie.

1. Wybierz opcję `Fine-grained tokens` po lewej stronie ekranu, przechodząc do **Developer settings**  
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.pl.png)

   Następnie wybierz `Generate new token`.

   ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.pl.png)

2. Wprowadź opisową nazwę dla swojego tokena, która odzwierciedla jego cel, aby łatwo go było później zidentyfikować.

   🔐 Rekomendacja dotycząca czasu trwania tokena

   Zalecany czas trwania: 30 dni  
   Dla większego bezpieczeństwa możesz wybrać krótszy okres, na przykład 7 dni 🛡️  
   To świetny sposób, aby wyznaczyć sobie cel i ukończyć kurs, utrzymując wysoki poziom motywacji 🚀.

   ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.pl.png)

3. Ogranicz zakres tokena do swojego forka tego repozytorium.

   ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.pl.png)

4. Ogranicz uprawnienia tokena: W sekcji **Permissions** kliknij zakładkę **Account**, a następnie przycisk "+ Add permissions". Pojawi się rozwijane menu. Wyszukaj **Models** i zaznacz pole wyboru.  
   ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.pl.png)

5. Zweryfikuj wymagane uprawnienia przed wygenerowaniem tokena. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.pl.png)

6. Przed wygenerowaniem tokena upewnij się, że jesteś gotowy, aby przechowywać go w bezpiecznym miejscu, takim jak menedżer haseł, ponieważ nie będzie on ponownie wyświetlany po jego utworzeniu. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.pl.png)

Skopiuj nowo utworzony token. Teraz dodasz go do pliku `.env` dołączonego do tego kursu.

### Krok 2: Utwórz plik `.env`

Aby utworzyć plik `.env`, uruchom następujące polecenie w terminalu:

```bash
cp .env.example .env
```

To polecenie skopiuje plik przykładowy i utworzy `.env` w Twoim katalogu, gdzie wypełnisz wartościami zmienne środowiskowe.

Po skopiowaniu tokena otwórz plik `.env` w swoim ulubionym edytorze tekstu i wklej token w polu `GITHUB_TOKEN`.  
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.pl.png)

Powinieneś teraz być w stanie uruchamiać przykłady kodu z tego kursu.

## Konfiguracja dla przykładów z użyciem Azure AI Foundry i Azure AI Agent Service

### Krok 1: Pobierz punkt końcowy projektu Azure

Postępuj zgodnie z krokami tworzenia huba i projektu w Azure AI Foundry opisanymi tutaj: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Po utworzeniu projektu musisz pobrać ciąg połączenia dla swojego projektu.

Można to zrobić, przechodząc do strony **Overview** swojego projektu w portalu Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.pl.png)

### Krok 2: Utwórz plik `.env`

Aby utworzyć plik `.env`, uruchom następujące polecenie w terminalu:

```bash
cp .env.example .env
```

To polecenie skopiuje plik przykładowy i utworzy `.env` w Twoim katalogu, gdzie wypełnisz wartościami zmienne środowiskowe.

Po skopiowaniu tokena otwórz plik `.env` w swoim ulubionym edytorze tekstu i wklej token w polu `PROJECT_ENDPOINT`.

### Krok 3: Zaloguj się do Azure

Jako najlepszą praktykę bezpieczeństwa użyjemy [uwierzytelniania bez klucza](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst), aby uwierzytelnić się w Azure OpenAI za pomocą Microsoft Entra ID.

Następnie otwórz terminal i uruchom `az login --use-device-code`, aby zalogować się na swoje konto Azure.

Po zalogowaniu wybierz swoją subskrypcję w terminalu.

## Dodatkowe zmienne środowiskowe - Azure Search i Azure OpenAI

Dla lekcji Agentic RAG - Lekcja 5 - dostępne są przykłady wykorzystujące Azure Search i Azure OpenAI.

Jeśli chcesz uruchomić te przykłady, musisz dodać następujące zmienne środowiskowe do swojego pliku `.env`:

### Strona przeglądu (Projekt)

- `AZURE_SUBSCRIPTION_ID` - Sprawdź **Project details** na stronie **Overview** swojego projektu.

- `AZURE_AI_PROJECT_NAME` - Spójrz na górę strony **Overview** swojego projektu.

- `AZURE_OPENAI_SERVICE` - Znajdź to w zakładce **Included capabilities** dla **Azure OpenAI Service** na stronie **Overview**.

### Centrum zarządzania

- `AZURE_OPENAI_RESOURCE_GROUP` - Przejdź do **Project properties** na stronie **Overview** w **Management Center**.

- `GLOBAL_LLM_SERVICE` - W sekcji **Connected resources** znajdź nazwę połączenia **Azure AI Services**. Jeśli nie jest wymieniona, sprawdź **Azure portal** w swojej grupie zasobów, aby znaleźć nazwę zasobu AI Services.

### Strona modeli i punktów końcowych

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Wybierz swój model osadzania (np. `text-embedding-ada-002`) i zanotuj **Deployment name** z szczegółów modelu.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Wybierz swój model czatu (np. `gpt-4o-mini`) i zanotuj **Deployment name** z szczegółów modelu.

### Portal Azure

- `AZURE_OPENAI_ENDPOINT` - Znajdź **Azure AI services**, kliknij na to, a następnie przejdź do **Resource Management**, **Keys and Endpoint**, przewiń w dół do "Azure OpenAI endpoints" i skopiuj ten, który mówi "Language APIs".

- `AZURE_OPENAI_API_KEY` - Z tego samego ekranu skopiuj KLUCZ 1 lub KLUCZ 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Znajdź swój zasób **Azure AI Search**, kliknij na niego i zobacz **Overview**.

- `AZURE_SEARCH_API_KEY` - Następnie przejdź do **Settings**, a potem **Keys**, aby skopiować klucz administratora głównego lub pomocniczego.

### Zewnętrzna strona internetowa

- `AZURE_OPENAI_API_VERSION` - Odwiedź stronę [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) w sekcji **Latest GA API release**.

### Konfiguracja uwierzytelniania bez klucza

Zamiast twardo kodować swoje dane uwierzytelniające, użyjemy połączenia bez klucza z Azure OpenAI. Aby to zrobić, zaimportujemy `DefaultAzureCredential`, a następnie wywołamy funkcję `DefaultAzureCredential`, aby uzyskać dane uwierzytelniające.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Utknąłeś?

Jeśli masz jakiekolwiek problemy z uruchomieniem tej konfiguracji, dołącz do naszego

lub

## Następna lekcja

Jesteś teraz gotowy, aby uruchomić kod z tego kursu. Powodzenia w nauce o świecie agentów AI!

[Wprowadzenie do agentów AI i przypadków użycia agentów](../01-intro-to-ai-agents/README.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.