<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-05-21T09:38:23+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "pl"
}
-->
# Lekcja 11: Integracja Model Context Protocol (MCP)

## Wprowadzenie do Model Context Protocol (MCP)

Model Context Protocol (MCP) to nowoczesne rozwiązanie stworzone w celu ujednolicenia interakcji między modelami AI a aplikacjami klienckimi. MCP pełni rolę pomostu między modelami AI a aplikacjami, które z nich korzystają, zapewniając spójny interfejs niezależnie od implementacji modelu.

Kluczowe cechy MCP:

- **Ustandaryzowana komunikacja**: MCP ustanawia wspólny język dla aplikacji do komunikacji z modelami AI  
- **Ulepszone zarządzanie kontekstem**: Umożliwia efektywne przekazywanie informacji kontekstowych do modeli AI  
- **Kompatybilność wieloplatformowa**: Działa w różnych językach programowania, w tym C#, Java, JavaScript, Python i TypeScript  
- **Płynna integracja**: Ułatwia deweloperom integrację różnych modeli AI z ich aplikacjami  

MCP jest szczególnie cenny przy tworzeniu agentów AI, ponieważ pozwala agentom na interakcję z różnymi systemami i źródłami danych za pomocą zunifikowanego protokołu, co zwiększa ich elastyczność i możliwości.

## Cele nauki
- Zrozumieć, czym jest MCP i jaka jest jego rola w rozwoju agentów AI  
- Skonfigurować serwer MCP do integracji z GitHub  
- Zbudować system wieloagentowy z użyciem narzędzi MCP  
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
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## Główne komponenty

### 1. System wieloagentowy
- GitHub Agent: analiza repozytoriów  
- Hackathon Agent: rekomendacje projektów  
- Events Agent: propozycje wydarzeń technologicznych  

### 2. Integracja z Azure
- Cognitive Search do indeksowania wydarzeń  
- Azure OpenAI jako inteligencja agentów  
- Implementacja wzorca RAG  

### 3. Narzędzia MCP
- Analiza repozytoriów GitHub  
- Inspekcja kodu  
- Ekstrakcja metadanych  

## Omówienie kodu

Przykład pokazuje:  
1. Integrację serwera MCP  
2. Orkiestrację systemu wieloagentowego  
3. Integrację z Azure Cognitive Search  
4. Implementację wzorca RAG  

Kluczowe funkcje:  
- Analiza repozytoriów GitHub w czasie rzeczywistym  
- Inteligentne rekomendacje projektów  
- Dopasowywanie wydarzeń z użyciem Azure Search  
- Streaming odpowiedzi z Chainlit  

## Uruchamianie przykładu

Szczegółowe instrukcje konfiguracji i więcej informacji znajdziesz w [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Uruchom serwer MCP:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Włącz aplikację:  
   ```bash
   chainlit run app.py -w
   ```

3. Przetestuj integrację:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Rozwiązywanie problemów

Typowe problemy i ich rozwiązania:  
1. Problemy z połączeniem MCP  
   - Sprawdź, czy serwer działa  
   - Zweryfikuj dostępność portu  
   - Potwierdź poprawność tokenów GitHub  

2. Problemy z Azure Search  
   - Sprawdź poprawność connection stringów  
   - Zweryfikuj istnienie indeksu  
   - Sprawdź przesyłanie dokumentów  

## Kolejne kroki
- Poznaj dodatkowe narzędzia MCP  
- Zaimplementuj własnych agentów  
- Rozwiń możliwości RAG  
- Dodaj więcej źródeł wydarzeń  

## Zasoby
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako autorytatywne źródło. W przypadku istotnych informacji zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.