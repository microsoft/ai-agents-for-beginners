<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-30T15:00:18+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "pl"
}
-->
# Przewodnik integracji serwera MCP

## Wymagania wstępne
- Zainstalowany Node.js (wersja 14 lub nowsza)
- Menedżer pakietów npm
- Środowisko Python z wymaganymi zależnościami

## Kroki konfiguracji

1. **Zainstaluj pakiet serwera MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Uruchom serwer MCP**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Serwer powinien się uruchomić i wyświetlić adres URL połączenia.

3. **Zweryfikuj połączenie**  
   - Poszukaj ikony wtyczki (🔌) w interfejsie Chainlit  
   - Obok ikony wtyczki powinna pojawić się liczba (1), wskazująca na pomyślne połączenie  
   - Konsola powinna wyświetlić: „GitHub plugin setup completed successfully” (wraz z dodatkowymi liniami statusu)

## Rozwiązywanie problemów

### Typowe problemy

1. **Konflikt portów**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Rozwiązanie: Zmień port za pomocą:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problemy z uwierzytelnianiem**  
   - Upewnij się, że dane uwierzytelniające GitHub są poprawnie skonfigurowane  
   - Sprawdź, czy plik .env zawiera wymagane tokeny  
   - Zweryfikuj dostęp do API GitHub  

3. **Nieudane połączenie**  
   - Upewnij się, że serwer działa na oczekiwanym porcie  
   - Sprawdź ustawienia zapory sieciowej  
   - Zweryfikuj, czy środowisko Python ma zainstalowane wymagane pakiety  

## Weryfikacja połączenia

Twój serwer MCP jest poprawnie połączony, gdy:  
1. Konsola wyświetla „GitHub plugin setup completed successfully”  
2. Logi połączenia pokazują „✓ MCP Connection Status: Active”  
3. Polecenia GitHub działają w interfejsie czatu  

## Zmienne środowiskowe

Wymagane w pliku .env:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testowanie połączenia

Wyślij tę wiadomość testową w czacie:  
```
Show me the repositories for username: [GitHub Username]
```  
Pomyślna odpowiedź pokaże informacje o repozytorium.  

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.