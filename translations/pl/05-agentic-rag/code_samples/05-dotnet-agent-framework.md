<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:02:23+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "pl"
}
-->
# 🔍 Enterprise RAG z Azure AI Foundry (.NET)

## 📋 Cele nauki

Ten notebook pokazuje, jak budować systemy Retrieval-Augmented Generation (RAG) klasy korporacyjnej, korzystając z Microsoft Agent Framework w .NET z Azure AI Foundry. Nauczysz się tworzyć gotowe do produkcji agenty, które potrafią przeszukiwać dokumenty i dostarczać precyzyjne, kontekstowe odpowiedzi z zachowaniem bezpieczeństwa i skalowalności na poziomie korporacyjnym.

**Funkcje Enterprise RAG, które zbudujesz:**
- 📚 **Inteligencja dokumentów**: Zaawansowane przetwarzanie dokumentów z usługami Azure AI
- 🔍 **Wyszukiwanie semantyczne**: Wysokowydajne wyszukiwanie wektorowe z funkcjami korporacyjnymi
- 🛡️ **Integracja bezpieczeństwa**: Dostęp oparty na rolach i wzorce ochrony danych
- 🏢 **Skalowalna architektura**: Systemy RAG gotowe do produkcji z monitoringiem

## 🎯 Architektura Enterprise RAG

### Kluczowe komponenty korporacyjne
- **Azure AI Foundry**: Zarządzana platforma AI dla przedsiębiorstw z bezpieczeństwem i zgodnością
- **Persistent Agents**: Agenty z zachowaniem stanu, historią rozmów i zarządzaniem kontekstem
- **Zarządzanie magazynem wektorowym**: Indeksowanie i wyszukiwanie dokumentów na poziomie korporacyjnym
- **Integracja tożsamości**: Uwierzytelnianie Azure AD i kontrola dostępu oparta na rolach

### Korzyści z .NET dla przedsiębiorstw
- **Bezpieczeństwo typów**: Walidacja operacji RAG i struktur danych na etapie kompilacji
- **Wydajność asynchroniczna**: Nieblokujące przetwarzanie dokumentów i operacje wyszukiwania
- **Zarządzanie pamięcią**: Efektywne wykorzystanie zasobów dla dużych kolekcji dokumentów
- **Wzorce integracji**: Natywna integracja usług Azure z wstrzykiwaniem zależności

## 🏗️ Architektura techniczna

### Pipeline Enterprise RAG
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Kluczowe komponenty .NET
- **Azure.AI.Agents.Persistent**: Zarządzanie agentami korporacyjnymi z zachowaniem stanu
- **Azure.Identity**: Zintegrowane uwierzytelnianie dla bezpiecznego dostępu do usług Azure
- **Microsoft.Agents.AI.AzureAI**: Implementacja frameworku agentów zoptymalizowana dla Azure
- **System.Linq.Async**: Wysokowydajne asynchroniczne operacje LINQ

## 🔧 Funkcje i korzyści dla przedsiębiorstw

### Bezpieczeństwo i zgodność
- **Integracja Azure AD**: Zarządzanie tożsamością i uwierzytelnianie na poziomie korporacyjnym
- **Dostęp oparty na rolach**: Precyzyjne uprawnienia do dostępu do dokumentów i operacji
- **Ochrona danych**: Szyfrowanie danych w spoczynku i w tranzycie dla dokumentów wrażliwych
- **Rejestrowanie audytów**: Kompleksowe śledzenie aktywności dla wymogów zgodności

### Wydajność i skalowalność
- **Pooling połączeń**: Efektywne zarządzanie połączeniami z usługami Azure
- **Przetwarzanie asynchroniczne**: Operacje nieblokujące dla scenariuszy o wysokiej przepustowości
- **Strategie buforowania**: Inteligentne buforowanie często używanych dokumentów
- **Równoważenie obciążenia**: Rozproszone przetwarzanie dla wdrożeń na dużą skalę

### Zarządzanie i monitoring
- **Kontrole zdrowia**: Wbudowany monitoring komponentów systemu RAG
- **Metryki wydajności**: Szczegółowa analiza jakości wyszukiwania i czasów odpowiedzi
- **Obsługa błędów**: Kompleksowe zarządzanie wyjątkami z politykami ponawiania
- **Zarządzanie konfiguracją**: Ustawienia specyficzne dla środowiska z walidacją

## ⚙️ Wymagania wstępne i konfiguracja

**Środowisko deweloperskie:**
- .NET 9.0 SDK lub wyższy
- Visual Studio 2022 lub VS Code z rozszerzeniem C#
- Subskrypcja Azure z dostępem do AI Foundry

**Wymagane pakiety NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracja uwierzytelniania Azure:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Konfiguracja środowiska:**
* Konfiguracja Azure AI Foundry (automatycznie obsługiwana przez Azure CLI)
* Upewnij się, że jesteś uwierzytelniony w odpowiedniej subskrypcji Azure

## 📊 Wzorce Enterprise RAG

### Wzorce zarządzania dokumentami
- **Masowe przesyłanie**: Efektywne przetwarzanie dużych kolekcji dokumentów
- **Aktualizacje przyrostowe**: Dodawanie i modyfikacja dokumentów w czasie rzeczywistym
- **Kontrola wersji**: Wersjonowanie dokumentów i śledzenie zmian
- **Zarządzanie metadanymi**: Bogate atrybuty dokumentów i taksonomia

### Wzorce wyszukiwania i pobierania
- **Wyszukiwanie hybrydowe**: Łączenie wyszukiwania semantycznego i słownego dla optymalnych wyników
- **Wyszukiwanie fasetowe**: Wielowymiarowe filtrowanie i kategoryzacja
- **Dopasowanie trafności**: Niestandardowe algorytmy punktacji dla specyficznych potrzeb domeny
- **Ranking wyników**: Zaawansowane rankingi z integracją logiki biznesowej

### Wzorce bezpieczeństwa
- **Bezpieczeństwo na poziomie dokumentu**: Precyzyjna kontrola dostępu dla każdego dokumentu
- **Klasyfikacja danych**: Automatyczne etykietowanie wrażliwości i ochrona
- **Ścieżki audytu**: Kompleksowe rejestrowanie wszystkich operacji RAG
- **Ochrona prywatności**: Wykrywanie i redakcja danych osobowych (PII)

## 🔒 Funkcje bezpieczeństwa dla przedsiębiorstw

### Uwierzytelnianie i autoryzacja
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### Ochrona danych
- **Szyfrowanie**: Szyfrowanie end-to-end dla dokumentów i indeksów wyszukiwania
- **Kontrole dostępu**: Integracja z Azure AD dla uprawnień użytkowników i grup
- **Rezydencja danych**: Kontrola lokalizacji danych geograficznych dla zgodności
- **Kopia zapasowa i odzyskiwanie**: Automatyczne kopie zapasowe i procedury odzyskiwania

## 📈 Optymalizacja wydajności

### Wzorce przetwarzania asynchronicznego
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Zarządzanie pamięcią
- **Przetwarzanie strumieniowe**: Obsługa dużych dokumentów bez problemów z pamięcią
- **Pooling zasobów**: Efektywne ponowne wykorzystanie kosztownych zasobów
- **Zbieranie śmieci**: Optymalizacja wzorców alokacji pamięci
- **Zarządzanie połączeniami**: Prawidłowy cykl życia połączeń z usługami Azure

### Strategie buforowania
- **Buforowanie zapytań**: Buforowanie często wykonywanych wyszukiwań
- **Buforowanie dokumentów**: Buforowanie w pamięci dla popularnych dokumentów
- **Buforowanie indeksów**: Optymalizacja buforowania indeksów wektorowych
- **Buforowanie wyników**: Inteligentne buforowanie wygenerowanych odpowiedzi

## 📊 Przypadki użycia dla przedsiębiorstw

### Zarządzanie wiedzą
- **Wiki korporacyjne**: Inteligentne wyszukiwanie w bazach wiedzy firmy
- **Polityki i procedury**: Automatyczne wskazówki dotyczące zgodności i procedur
- **Materiały szkoleniowe**: Inteligentna pomoc w nauce i rozwoju
- **Bazy danych badawczych**: Systemy analizy prac akademickich i badawczych

### Obsługa klienta
- **Baza wiedzy wsparcia**: Automatyczne odpowiedzi w obsłudze klienta
- **Dokumentacja produktów**: Inteligentne wyszukiwanie informacji o produktach
- **Przewodniki rozwiązywania problemów**: Kontekstowa pomoc w rozwiązywaniu problemów
- **Systemy FAQ**: Dynamiczne generowanie FAQ z kolekcji dokumentów

### Zgodność regulacyjna
- **Analiza dokumentów prawnych**: Inteligencja kontraktów i dokumentów prawnych
- **Monitoring zgodności**: Automatyczne sprawdzanie zgodności regulacyjnej
- **Ocena ryzyka**: Analiza ryzyka oparta na dokumentach i raportowanie
- **Wsparcie audytowe**: Inteligentne wyszukiwanie dokumentów dla audytów

## 🚀 Wdrożenie produkcyjne

### Monitoring i obserwowalność
- **Application Insights**: Szczegółowa telemetria i monitoring wydajności
- **Metryki niestandardowe**: Śledzenie i alerty specyficzne dla KPI biznesowych
- **Śledzenie rozproszone**: Śledzenie żądań end-to-end w usługach
- **Pulpity zdrowia**: Wizualizacja zdrowia systemu i wydajności w czasie rzeczywistym

### Skalowalność i niezawodność
- **Auto-skalowanie**: Automatyczne skalowanie na podstawie obciążenia i metryk wydajności
- **Wysoka dostępność**: Wdrożenie wieloregionowe z funkcjami przełączania awaryjnego
- **Testy obciążeniowe**: Walidacja wydajności pod obciążeniem korporacyjnym
- **Odzyskiwanie po awarii**: Automatyczne kopie zapasowe i procedury odzyskiwania

Gotowy, aby budować systemy RAG klasy korporacyjnej, które mogą obsługiwać wrażliwe dokumenty na dużą skalę? Zaprojektujmy inteligentne systemy wiedzy dla przedsiębiorstw! 🏢📖✨

## Implementacja kodu

Kompletny działający przykład kodu dla tej lekcji znajduje się w `05-dotnet-agent-framework.cs`. 

Aby uruchomić przykład:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Lub użyj `dotnet run` bezpośrednio:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kod demonstruje:

1. **Instalacja pakietów**: Instalacja wymaganych pakietów NuGet dla Azure AI Agents
2. **Konfiguracja środowiska**: Ładowanie punktu końcowego Azure AI Foundry i ustawień modelu
3. **Przesyłanie dokumentów**: Przesyłanie dokumentu do przetwarzania RAG
4. **Tworzenie magazynu wektorowego**: Tworzenie magazynu wektorowego dla wyszukiwania semantycznego
5. **Konfiguracja agenta**: Konfiguracja agenta AI z funkcjami wyszukiwania plików
6. **Wykonywanie zapytań**: Uruchamianie zapytań na przesłanym dokumencie

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, należy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku ojczystym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.