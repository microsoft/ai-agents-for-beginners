<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:21:31+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "pl"
}
-->
# Lekcja 11: Integracja z protokołem Model Context Protocol (MCP)

## Wprowadzenie do Model Context Protocol (MCP)

Model Context Protocol (MCP) to nowoczesne rozwiązanie mające na celu standaryzację interakcji między modelami AI a aplikacjami klienckimi. MCP działa jako pomost między modelami AI a aplikacjami, które z nich korzystają, zapewniając spójny interfejs niezależnie od implementacji modelu.

Kluczowe aspekty MCP:

- **Standaryzowana komunikacja**: MCP ustanawia wspólny język dla aplikacji komunikujących się z modelami AI
- **Ulepszone zarządzanie kontekstem**: Umożliwia efektywne przekazywanie informacji kontekstowych do modeli AI
- **Kompatybilność międzyplatformowa**: Działa w różnych językach programowania, takich jak C#, Java, JavaScript, Python i TypeScript
- **Bezproblemowa integracja**: Ułatwia programistom integrację różnych modeli AI z ich aplikacjami

MCP jest szczególnie przydatny w rozwoju agentów AI, ponieważ pozwala im na interakcję z różnymi systemami i źródłami danych za pomocą jednolitego protokołu, czyniąc agentów bardziej elastycznymi i potężnymi.

## Cele nauki
- Zrozumieć, czym jest MCP i jaką rolę odgrywa w rozwoju agentów AI
- Skonfigurować serwer MCP do integracji z GitHubem
- Zbudować system wieloagentowy za pomocą narzędzi MCP
- Zaimplementować RAG (Retrieval Augmented Generation) z Azure Cognitive Search

## Wymagania wstępne
- Python 3.8+
- Node.js 14+
- Subskrypcja Azure
- Konto GitHub
- Podstawowa znajomość Semantic Kernel

## Instrukcje konfiguracji

1. **Konfiguracja środowiska**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfiguracja usług Azure**
   - Utwórz zasób Azure Cognitive Search
   - Skonfiguruj usługę Azure OpenAI
   - Ustaw zmienne środowiskowe w pliku `.env`

3. **Konfiguracja serwera MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Struktura projektu

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## Główne komponenty

### 1. System wieloagentowy
- Agent GitHub: Analiza repozytoriów
- Agent Hackathon: Rekomendacje projektów
- Agent Wydarzeń: Sugestie dotyczące wydarzeń technologicznych

### 2. Integracja z Azure
- Cognitive Search do indeksowania wydarzeń
- Azure OpenAI do inteligencji agentów
- Implementacja wzorca RAG

### 3. Narzędzia MCP
- Analiza repozytoriów GitHub
- Inspekcja kodu
- Ekstrakcja metadanych

## Przegląd kodu

Przykład demonstruje:
1. Integrację serwera MCP
2. Orkiestrację wieloagentową
3. Integrację z Azure Cognitive Search
4. Implementację wzorca RAG

Kluczowe funkcje:
- Analiza repozytoriów GitHub w czasie rzeczywistym
- Inteligentne rekomendacje projektów
- Dopasowywanie wydarzeń za pomocą Azure Search
- Strumieniowe odpowiedzi z Chainlit

## Uruchamianie przykładu

Szczegółowe instrukcje konfiguracji i więcej informacji znajdziesz w [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Uruchom serwer MCP:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Uruchom aplikację:
   ```bash
   chainlit run app.py -w
   ```

3. Przetestuj integrację:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Rozwiązywanie problemów

Typowe problemy i rozwiązania:
1. Problemy z połączeniem MCP
   - Sprawdź, czy serwer działa
   - Zweryfikuj dostępność portu
   - Potwierdź tokeny GitHub

2. Problemy z Azure Search
   - Zweryfikuj ciągi połączeń
   - Sprawdź istnienie indeksu
   - Potwierdź przesyłanie dokumentów

## Kolejne kroki
- Poznaj dodatkowe narzędzia MCP
- Zaimplementuj własnych agentów
- Rozbuduj możliwości RAG
- Dodaj więcej źródeł wydarzeń
- **Zaawansowane**: Sprawdź [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) dla przykładów komunikacji między agentami

## Zasoby
- [MCP dla początkujących](https://aka.ms/mcp-for-beginners)  
- [Dokumentacja MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Dokumentacja Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Przewodniki Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.