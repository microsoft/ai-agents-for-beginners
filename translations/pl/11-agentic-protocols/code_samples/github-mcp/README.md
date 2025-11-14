<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T14:51:22+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "pl"
}
-->
# Przykład serwera MCP na Githubie

## Opis

To demo zostało stworzone na potrzeby Hackathonu AI Agents organizowanego przez Microsoft Reactor.

Narzędzie służy do rekomendowania projektów hackathonowych na podstawie repozytoriów użytkownika na Githubie. Proces ten przebiega w następujący sposób:

1. **Github Agent** - Korzysta z serwera Github MCP, aby pobrać repozytoria i informacje o nich.
2. **Hackathon Agent** - Wykorzystuje dane z Github Agent, aby zaproponować kreatywne pomysły na projekty hackathonowe, bazując na projektach, językach programowania używanych przez użytkownika oraz ścieżkach projektowych dla hackathonu AI Agents.
3. **Events Agent** - Na podstawie sugestii Hackathon Agent, Events Agent rekomenduje odpowiednie wydarzenia z serii AI Agent Hackathon.

## Uruchamianie kodu

### Zmienne środowiskowe

To demo korzysta z Azure Open AI Service, Semantic Kernel, serwera Github MCP oraz Azure AI Search.

Upewnij się, że masz odpowiednio ustawione zmienne środowiskowe, aby korzystać z tych narzędzi:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Uruchamianie serwera Chainlit

Aby połączyć się z serwerem MCP, to demo wykorzystuje Chainlit jako interfejs czatu.

Aby uruchomić serwer, użyj następującego polecenia w terminalu:

```bash
chainlit run app.py -w
```

To powinno uruchomić serwer Chainlit na `localhost:8000` oraz wypełnić indeks wyszukiwania Azure AI treścią z pliku `event-descriptions.md`.

## Łączenie się z serwerem MCP

Aby połączyć się z serwerem Github MCP, kliknij ikonę „wtyczki” znajdującą się pod polem „Type your message here...” w oknie czatu:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.pl.png)

Następnie kliknij „Connect an MCP”, aby dodać polecenie łączenia z serwerem Github MCP:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Zastąp "[YOUR PERSONAL ACCESS TOKEN]" swoim rzeczywistym tokenem dostępu osobistego.

Po połączeniu powinieneś zobaczyć (1) obok ikony wtyczki, co potwierdzi, że połączenie zostało nawiązane. Jeśli nie, spróbuj ponownie uruchomić serwer Chainlit za pomocą `chainlit run app.py -w`.

## Korzystanie z dema

Aby rozpocząć przepływ pracy agenta, który rekomenduje projekty hackathonowe, możesz wpisać wiadomość, na przykład:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent przeanalizuje Twoje zapytanie i określi, która kombinacja agentów (GitHub, Hackathon i Events) najlepiej nadaje się do obsługi Twojego zapytania. Agenci współpracują, aby dostarczyć kompleksowe rekomendacje na podstawie analizy repozytoriów Github, generowania pomysłów na projekty i odpowiednich wydarzeń technologicznych.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.