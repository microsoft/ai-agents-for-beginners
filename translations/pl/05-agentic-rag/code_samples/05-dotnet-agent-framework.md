# 🔍 Enterprise RAG z Microsoft Foundry (.NET)

## 📋 Cele nauki

Ten notatnik pokazuje, jak budować systemy Retrieval-Augmented Generation (RAG) na poziomie przedsiębiorstwa za pomocą Microsoft Agent Framework w .NET z Microsoft Foundry. Nauczysz się tworzyć gotowe do produkcji agentów, którzy potrafią przeszukiwać dokumenty i dostarczać precyzyjne, uwzględniające kontekst odpowiedzi z bezpieczeństwem i skalowalnością na poziomie przedsiębiorstwa.

**Zdolności Enterprise RAG, które zbudujesz:**
- 📚 **Inteligencja Dokumentów**: Zaawansowane przetwarzanie dokumentów z usługami Azure AI
- 🔍 **Wyszukiwanie Semantyczne**: Wydajne wyszukiwanie wektorowe z funkcjami na poziomie przedsiębiorstwa
- 🛡️ **Integracja Bezpieczeństwa**: Kontrola dostępu oparta na rolach i wzorce ochrony danych
- 🏢 **Skalowalna Architektura**: Gotowe do produkcji systemy RAG z monitorowaniem

## 🎯 Architektura Enterprise RAG

### Podstawowe komponenty przedsiębiorstwa
- **Microsoft Foundry**: Zarządzana platforma AI dla przedsiębiorstw z bezpieczeństwem i zgodnością
- **Agenci trwałościowi**: Agenci z zarządzaniem historią rozmów i kontekstem
- **Zarządzanie magazynem wektorów**: Indeksowanie i wyszukiwanie dokumentów na poziomie przedsiębiorstwa
- **Integracja tożsamości**: Uwierzytelnianie Azure AD i kontrola dostępu oparta na rolach

### Korzyści z .NET w przedsiębiorstwie  
- **Bezpieczeństwo typów**: Walidacja w czasie kompilacji dla operacji RAG i struktur danych
- **Wydajność asynchroniczna**: Nieblokujące przetwarzanie dokumentów i operacje wyszukiwania
- **Zarządzanie pamięcią**: Efektywne wykorzystanie zasobów dla dużych kolekcji dokumentów
- **Wzorce integracji**: Natychmiastowa integracja usług Azure z wstrzykiwaniem zależności

## 🏗️ Architektura techniczna

### Pipeline Enterprise RAG
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Kluczowe komponenty .NET
- **Azure.AI.Agents.Persistent**: Zarządzanie agentami przedsiębiorstwa z utrwaleniem stanu
- **Azure.Identity**: Zintegrowane uwierzytelnianie dla bezpiecznego dostępu do usług Azure
- **Microsoft.Agents.AI.AzureAI**: Implementacja frameworku agentów zoptymalizowana pod Azure
- **System.Linq.Async**: Wydajne operacje LINQ asynchroniczne

## 🔧 Funkcje i korzyści Enterprise

### Bezpieczeństwo i zgodność
- **Integracja Azure AD**: Zarządzanie tożsamością przedsiębiorstwa i uwierzytelnianie
- **Kontrola dostępu oparta na rolach**: Precyzyjne uprawnienia do dostępu do dokumentów i operacji
- **Ochrona danych**: Szyfrowanie spoczynkowe i transferowe dla wrażliwych dokumentów
- **Rejestrowanie audytowe**: Kompleksowe śledzenie działań dla wymogów zgodności

### Wydajność i skalowalność
- **Pule połączeń**: Efektywne zarządzanie połączeniami usług Azure
- **Przetwarzanie asynchroniczne**: Nieblokujące operacje dla scenariuszy o wysokiej przepustowości
- **Strategie cachowania**: Inteligentne cachowanie często używanych dokumentów
- **Równoważenie obciążenia**: Rozproszone przetwarzanie dla dużych wdrożeń

### Zarządzanie i monitorowanie
- **Kontrole stanu zdrowia**: Wbudowane monitorowanie komponentów systemu RAG
- **Metryki wydajności**: Szczegółowa analityka jakości wyszukiwania i czasów odpowiedzi
- **Obsługa błędów**: Kompleksowe zarządzanie wyjątkami z politykami ponawiania
- **Zarządzanie konfiguracją**: Ustawienia specyficzne dla środowiska z walidacją

## ⚙️ Wymagania wstępne i konfiguracja

**Środowisko programistyczne:**
- .NET 9.0 SDK lub wyższy
- Visual Studio 2022 lub VS Code z rozszerzeniem C#
- Subskrypcja Azure z dostępem do Microsoft Foundry

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
# Zainstaluj Azure CLI i uwierzytelnij się
az login
az account set --subscription "your-subscription-id"
```

**Konfiguracja środowiska:**
* Konfiguracja Microsoft Foundry (automatycznie obsługiwana przez Azure CLI)
* Upewnij się, że jesteś uwierzytelniony na właściwą subskrypcję Azure

## 📊 Wzorce Enterprise RAG

### Wzorce zarządzania dokumentami
- **Masowy upload**: Efektywne przetwarzanie dużych kolekcji dokumentów
- **Aktualizacje inkrementalne**: Dodawanie i modyfikacja dokumentów w czasie rzeczywistym
- **Kontrola wersji**: Wersjonowanie dokumentów i śledzenie zmian
- **Zarządzanie metadanymi**: Rozbudowane atrybuty dokumentów i klasyfikacja

### Wzorce wyszukiwania i odzyskiwania
- **Wyszukiwanie hybrydowe**: Łączenie wyszukiwania semantycznego i słów kluczowych dla optymalnych rezultatów
- **Wyszukiwanie faceted**: Wielowymiarowe filtrowanie i kategoryzacja
- **Dopasowanie trafności**: Niestandardowe algorytmy punktacji dla potrzeb domenowych
- **Ranking wyników**: Zaawansowany ranking z integracją logiki biznesowej

### Wzorce bezpieczeństwa
- **Bezpieczeństwo na poziomie dokumentu**: Precyzyjna kontrola dostępu do pojedynczych dokumentów
- **Klasyfikacja danych**: Automatyczne etykietowanie czułości i ochrona
- **Ścieżki audytu**: Kompleksowe rejestrowanie wszystkich operacji RAG
- **Ochrona prywatności**: Wykrywanie i zaciemnianie danych osobowych (PII)

## 🔒 Funkcje bezpieczeństwa przedsiębiorstwa

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
- **Kontrola dostępu**: Integracja z Azure AD dla uprawnień użytkowników i grup
- **Lokalizacja danych**: Kontrola geograficznego położenia danych dla zgodności
- **Kopie zapasowe i odzyskiwanie**: Automatyczne tworzenie kopii i procedury odzyskiwania po awarii

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
- **Pule zasobów**: Efektywne ponowne wykorzystanie drogich zasobów
- **Zbieranie śmieci**: Optymalizowane wzorce alokacji pamięci
- **Zarządzanie połączeniami**: Właściwy cykl życia połączeń do usług Azure

### Strategie cachowania
- **Cachowanie zapytań**: Buforowanie często wykonywanych wyszukiwań
- **Cachowanie dokumentów**: Cachowanie w pamięci dla "gorących" dokumentów
- **Cachowanie indeksów**: Optymalizacja cachowania indeksów wektorowych
- **Cachowanie wyników**: Inteligentne cachowanie generowanych odpowiedzi

## 📊 Przypadki użycia w przedsiębiorstwie

### Zarządzanie wiedzą
- **Korporacyjna wiki**: Inteligentne wyszukiwanie w bazach wiedzy firmy
- **Polityki i procedury**: Automatyczne wsparcie zgodności i wytyczne proceduralne
- **Materiały szkoleniowe**: Inteligentna pomoc w nauce i rozwoju
- **Bazy badań**: Systemy analizy publikacji naukowych i badawczych

### Obsługa klienta
- **Baza wiedzy wsparcia**: Automatyczne odpowiedzi w obsłudze klienta
- **Dokumentacja produktów**: Inteligentne wyszukiwanie informacji o produktach
- **Poradniki rozwiązywania problemów**: Kontekstowa pomoc w rozwiązywaniu problemów
- **Systemy FAQ**: Dynamiczne generowanie FAQ z kolekcji dokumentów

### Zgodność regulacyjna
- **Analiza dokumentów prawnych**: Inteligencja umów i dokumentów prawnych
- **Monitorowanie zgodności**: Automatyczne sprawdzanie zgodności regulacyjnej
- **Ocena ryzyka**: Analiza ryzyka i raportowanie oparte na dokumentach
- **Wsparcie audytu**: Inteligentne wyszukiwanie dokumentów do audytów

## 🚀 Wdrożenie produkcyjne

### Monitorowanie i obserwowalność
- **Application Insights**: Szczegółowa telemetria i monitorowanie wydajności
- **Metryki niestandardowe**: Śledzenie KPI biznesowych i alerty
- **Śledzenie rozproszone**: End-to-end śledzenie zapytań w usługach
- **Dashboardy zdrowia systemu**: Wizualizacja stanu zdrowia i wydajności w czasie rzeczywistym

### Skalowalność i niezawodność
- **Auto-skalowanie**: Automatyczne skalowanie na podstawie obciążenia i metryk wydajności
- **Wysoka dostępność**: Wdrożenie wieloregionalne z funkcjami awaryjnego przełączania
- **Testy obciążeniowe**: Walidacja wydajności przy obciążeniu na poziomie przedsiębiorstwa
- **Odzyskiwanie po awarii**: Zautomatyzowane procedury kopii zapasowej i odzyskiwania

Gotowy, by budować systemy RAG na poziomie przedsiębiorstwa, które poradzą sobie z wrażliwymi dokumentami na dużą skalę? Zaprojektujmy inteligentne systemy wiedzy dla przedsiębiorstw! 🏢📖✨

## Implementacja kodu

Kompletny działający przykład kodu do tej lekcji jest dostępny w `05-dotnet-agent-framework.cs`. 

Aby uruchomić przykład:

```bash
# Uczyń skrypt wykonywalnym (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Uruchom aplikację .NET Single File
./05-dotnet-agent-framework.cs
```

Lub użyj bezpośrednio `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kod demonstruje:

1. **Instalację pakietów**: Instalowanie wymaganych pakietów NuGet dla Azure AI Agents
2. **Konfigurację środowiska**: Ładowanie punktu końcowego Microsoft Foundry i ustawień modelu
3. **Wgrywanie dokumentu**: Wgrywanie dokumentu do przetwarzania RAG
4. **Tworzenie magazynu wektorów**: Tworzenie magazynu wektorowego do wyszukiwania semantycznego
5. **Konfigurację agenta**: Ustawianie agenta AI z możliwością wyszukiwania plików
6. **Wykonanie zapytania**: Uruchamianie zapytań na przesłanym dokumencie

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->