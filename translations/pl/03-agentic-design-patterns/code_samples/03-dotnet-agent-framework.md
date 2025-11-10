<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:46:58+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "pl"
}
-->
# 🎨 Wzorce projektowe agentów z modelami GitHub (.NET)

## 📋 Cele nauki

Ten notebook przedstawia wzorce projektowe na poziomie przedsiębiorstwa do budowy inteligentnych agentów przy użyciu Microsoft Agent Framework w .NET z integracją modeli GitHub. Nauczysz się profesjonalnych wzorców i podejść architektonicznych, które sprawiają, że agenci są gotowi do produkcji, łatwi w utrzymaniu i skalowalni.

**Wzorce projektowe na poziomie przedsiębiorstwa:**
- 🏭 **Wzorzec fabryki**: Standaryzowane tworzenie agentów z wykorzystaniem wstrzykiwania zależności
- 🔧 **Wzorzec budowniczego**: Płynna konfiguracja i ustawienia agenta
- 🧵 **Wzorce bezpieczne dla wątków**: Zarządzanie równoczesnymi rozmowami
- 📋 **Wzorzec repozytorium**: Zorganizowane zarządzanie narzędziami i możliwościami

## 🎯 Korzyści architektoniczne specyficzne dla .NET

### Funkcje na poziomie przedsiębiorstwa
- **Silne typowanie**: Walidacja w czasie kompilacji i wsparcie IntelliSense
- **Wstrzykiwanie zależności**: Wbudowana integracja kontenera DI
- **Zarządzanie konfiguracją**: Wzorce IConfiguration i Options
- **Async/Await**: Pierwszorzędne wsparcie dla programowania asynchronicznego

### Wzorce gotowe do produkcji
- **Integracja logowania**: ILogger i wsparcie dla strukturalnego logowania
- **Kontrole zdrowia**: Wbudowane monitorowanie i diagnostyka
- **Walidacja konfiguracji**: Silne typowanie z adnotacjami danych
- **Obsługa błędów**: Strukturalne zarządzanie wyjątkami

## 🔧 Architektura techniczna

### Główne komponenty .NET
- **Microsoft.Extensions.AI**: Ujednolicone abstrakcje usług AI
- **Microsoft.Agents.AI**: Ramy orkiestracji agentów na poziomie przedsiębiorstwa
- **Integracja modeli GitHub**: Wzorce klienta API o wysokiej wydajności
- **System konfiguracji**: Integracja appsettings.json i środowiska

### Implementacja wzorców projektowych
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Przedstawione wzorce na poziomie przedsiębiorstwa

### 1. **Wzorce kreacyjne**
- **Fabryka agentów**: Centralne tworzenie agentów z jednolitą konfiguracją
- **Wzorzec budowniczego**: Płynne API do złożonej konfiguracji agentów
- **Wzorzec singletona**: Zarządzanie wspólnymi zasobami i konfiguracją
- **Wstrzykiwanie zależności**: Luźne powiązania i możliwość testowania

### 2. **Wzorce behawioralne**
- **Wzorzec strategii**: Wymienne strategie wykonywania narzędzi
- **Wzorzec polecenia**: Enkapsulowane operacje agenta z funkcją cofania/powtarzania
- **Wzorzec obserwatora**: Zarządzanie cyklem życia agenta oparte na zdarzeniach
- **Metoda szablonowa**: Standaryzowane przepływy wykonywania agenta

### 3. **Wzorce strukturalne**
- **Wzorzec adaptera**: Warstwa integracji API modeli GitHub
- **Wzorzec dekoratora**: Rozszerzenie możliwości agenta
- **Wzorzec fasady**: Uproszczone interfejsy interakcji z agentem
- **Wzorzec proxy**: Lazy loading i caching dla wydajności

## ⚙️ Wymagania wstępne i konfiguracja

**Środowisko deweloperskie:**
- .NET 9.0 SDK lub wyższy
- Visual Studio 2022 lub VS Code z rozszerzeniem C#
- Dostęp do API modeli GitHub

**Zależności NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracja (plik .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 Zasady projektowania w .NET

### Zasady SOLID
- **Jedna odpowiedzialność**: Każdy komponent ma jedno jasno określone zadanie
- **Otwarte/Zamknięte**: Możliwość rozszerzania bez modyfikacji
- **Podstawienie Liskova**: Implementacje narzędzi oparte na interfejsach
- **Segregacja interfejsów**: Skupione, spójne interfejsy
- **Odwrócenie zależności**: Zależność od abstrakcji, a nie konkretów

### Czysta architektura
- **Warstwa domeny**: Podstawowe abstrakcje agenta i narzędzi
- **Warstwa aplikacji**: Orkiestracja agentów i przepływy pracy
- **Warstwa infrastruktury**: Integracja modeli GitHub i usługi zewnętrzne
- **Warstwa prezentacji**: Interakcja z użytkownikiem i formatowanie odpowiedzi

## 🔒 Rozważania na poziomie przedsiębiorstwa

### Bezpieczeństwo
- **Zarządzanie poświadczeniami**: Bezpieczne obsługiwanie kluczy API z IConfiguration
- **Walidacja wejścia**: Silne typowanie i walidacja z adnotacjami danych
- **Sanityzacja wyjścia**: Bezpieczne przetwarzanie i filtrowanie odpowiedzi
- **Logowanie audytowe**: Kompleksowe śledzenie operacji

### Wydajność
- **Wzorce asynchroniczne**: Operacje I/O bez blokowania
- **Pula połączeń**: Efektywne zarządzanie klientem HTTP
- **Caching**: Buforowanie odpowiedzi dla poprawy wydajności
- **Zarządzanie zasobami**: Odpowiednie zwalnianie i czyszczenie zasobów

### Skalowalność
- **Bezpieczeństwo wątków**: Obsługa równoczesnego wykonywania agentów
- **Pula zasobów**: Efektywne wykorzystanie zasobów
- **Zarządzanie obciążeniem**: Ograniczanie szybkości i obsługa przeciążeń
- **Monitorowanie**: Metryki wydajności i kontrole zdrowia

## 🚀 Wdrożenie produkcyjne

- **Zarządzanie konfiguracją**: Ustawienia specyficzne dla środowiska
- **Strategia logowania**: Strukturalne logowanie z identyfikatorami korelacji
- **Obsługa błędów**: Globalna obsługa wyjątków z odpowiednim odzyskiwaniem
- **Monitorowanie**: Application Insights i liczniki wydajności
- **Testowanie**: Testy jednostkowe, testy integracyjne i wzorce testowania obciążenia

Gotowy, aby budować inteligentnych agentów na poziomie przedsiębiorstwa z .NET? Zbudujmy coś solidnego! 🏢✨

## Przykład kodu

Pełny działający przykład znajdziesz w [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.