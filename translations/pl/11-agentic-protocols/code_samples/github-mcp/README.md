# Przykład serwera MCP Github

## Opis

To była demonstracja stworzona na Hackathon AI Agents organizowany przez Microsoft Reactor.

Narzędzie służy do rekomendowania projektów hackathonowych na podstawie repozytoriów użytkownika na Github.
Osiąga się to poprzez:

1. **Agent Github** - Korzysta z serwera MCP Github, aby pobrać repozytoria i informacje o tych repozytoriach.
2. **Agent Hackathon** - Analizuje dane od Agenta Github i wymyśla kreatywne pomysły na projekty hackathonowe bazując na repozytoriach, językach używanych przez użytkownika oraz ścieżkach projektów na hackathon AI Agents.
3. **Agent Wydarzeń** - Na podstawie sugestii agenta hackathonowego, agent wydarzeń poleca odpowiednie wydarzenia z serii hackathonów AI Agent.
## Uruchamianie kodu 

### Zmienne środowiskowe

Ta demonstracja wykorzystuje Microsoft Agent Framework, Azure OpenAI Service, serwer MCP Github oraz Azure AI Search.

Upewnij się, że masz ustawione odpowiednie zmienne środowiskowe do korzystania z tych narzędzi:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Uruchamianie serwera Chainlit

Aby połączyć się z serwerem MCP, ta demonstracja używa Chainlit jako interfejsu czatu. 

Aby uruchomić serwer, użyj następującego polecenia w terminalu:

```bash
chainlit run app.py -w
```

To powinno uruchomić twój serwer Chainlit na `localhost:8000` oraz wypełnić twój indeks wyszukiwania Azure AI treścią z `event-descriptions.md`.

## Łączenie się z serwerem MCP

Aby połączyć się z serwerem MCP Github, wybierz ikonę "wtyczki" pod polem czatu "Wpisz wiadomość tutaj..":

![MCP Connect](../../../../../translated_images/pl/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Następnie możesz kliknąć na "Połącz MCP", aby dodać polecenie łączące się z serwerem MCP Github:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Zamień "[YOUR PERSONAL ACCESS TOKEN]" na swój rzeczywisty Token Dostępu Osobistego.

Po połączeniu powinieneś zobaczyć (1) obok ikony wtyczki, co potwierdza połączenie. Jeśli nie, spróbuj ponownie uruchomić serwer chainlit poleceniem `chainlit run app.py -w`.

## Korzystanie z demonstracji 

Aby rozpocząć działanie agenta rekomendującego projekty hackathonowe, możesz wpisać wiadomość taką jak:

"Zaproponuj projekty hackathonowe dla użytkownika Github koreyspace"

Agent Router przeanalizuje twoje zapytanie i zdecyduje, która kombinacja agentów (Github, Hackathon i Wydarzenia) jest najlepiej dopasowana do obsługi twojego zapytania. Agenci współpracują, aby dostarczyć kompleksowe rekomendacje oparte na analizie repozytoriów Github, generowaniu pomysłów na projekty i odpowiednich wydarzeniach technologicznych.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrzeczenie się odpowiedzialności**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym powinien być uważany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->