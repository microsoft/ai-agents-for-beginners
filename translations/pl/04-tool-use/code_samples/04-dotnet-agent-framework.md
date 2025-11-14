<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:24:28+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "pl"
}
-->
# 🛠️ Zaawansowane użycie narzędzi z modelami GitHub (.NET)

## 📋 Cele nauki

Ten notebook pokazuje wzorce integracji narzędzi na poziomie korporacyjnym, wykorzystując Microsoft Agent Framework w .NET z modelami GitHub. Nauczysz się budować zaawansowane agenty z wieloma wyspecjalizowanymi narzędziami, korzystając z silnego typowania w C# oraz funkcji korporacyjnych .NET.

**Zaawansowane możliwości narzędzi, które opanujesz:**
- 🔧 **Architektura wielonarzędziowa**: Tworzenie agentów z wieloma wyspecjalizowanymi funkcjami
- 🎯 **Bezpieczne typowanie narzędzi**: Wykorzystanie walidacji w czasie kompilacji w C#
- 📊 **Wzorce narzędzi korporacyjnych**: Projektowanie narzędzi gotowych do produkcji i obsługa błędów
- 🔗 **Kompozycja narzędzi**: Łączenie narzędzi w złożone przepływy biznesowe

## 🎯 Korzyści z architektury narzędzi w .NET

### Funkcje narzędzi korporacyjnych
- **Walidacja w czasie kompilacji**: Silne typowanie zapewnia poprawność parametrów narzędzi
- **Wstrzykiwanie zależności**: Integracja kontenera IoC do zarządzania narzędziami
- **Wzorce Async/Await**: Wykonywanie narzędzi bez blokowania z odpowiednim zarządzaniem zasobami
- **Strukturalne logowanie**: Wbudowana integracja logowania do monitorowania wykonania narzędzi

### Wzorce gotowe do produkcji
- **Obsługa wyjątków**: Kompleksowe zarządzanie błędami z typowanymi wyjątkami
- **Zarządzanie zasobami**: Właściwe wzorce usuwania i zarządzania pamięcią
- **Monitorowanie wydajności**: Wbudowane metryki i liczniki wydajności
- **Zarządzanie konfiguracją**: Konfiguracja z walidacją i bezpiecznym typowaniem

## 🔧 Architektura techniczna

### Główne komponenty narzędzi .NET
- **Microsoft.Extensions.AI**: Ujednolicony warstwa abstrakcji narzędzi
- **Microsoft.Agents.AI**: Orkiestracja narzędzi na poziomie korporacyjnym
- **Integracja z modelami GitHub**: Wydajny klient API z pulą połączeń

### Pipeline wykonania narzędzi
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Kategorie narzędzi i wzorce

### 1. **Narzędzia przetwarzania danych**
- **Walidacja danych wejściowych**: Silne typowanie z adnotacjami danych
- **Operacje transformacji**: Bezpieczna typowo konwersja i formatowanie danych
- **Logika biznesowa**: Narzędzia do obliczeń i analiz specyficznych dla domeny
- **Formatowanie wyników**: Generowanie strukturalnych odpowiedzi

### 2. **Narzędzia integracyjne**
- **Konektory API**: Integracja usług RESTful z HttpClient
- **Narzędzia baz danych**: Integracja Entity Framework do dostępu do danych
- **Operacje na plikach**: Bezpieczne operacje na systemie plików z walidacją
- **Usługi zewnętrzne**: Wzorce integracji usług zewnętrznych

### 3. **Narzędzia użytkowe**
- **Przetwarzanie tekstu**: Manipulacja ciągami znaków i narzędzia formatowania
- **Operacje na datach/czasie**: Obliczenia dat/czasu uwzględniające kulturę
- **Narzędzia matematyczne**: Precyzyjne obliczenia i operacje statystyczne
- **Narzędzia walidacyjne**: Walidacja reguł biznesowych i weryfikacja danych

## ⚙️ Wymagania wstępne i konfiguracja

**Środowisko deweloperskie:**
- .NET 9.0 SDK lub wyższy
- Visual Studio 2022 lub VS Code z rozszerzeniem C#
- Dostęp do API modeli GitHub

**Wymagane pakiety NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracja środowiska (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Gotowy, aby budować agentów na poziomie korporacyjnym z potężnymi, bezpiecznymi typowo narzędziami w .NET? Zbudujmy profesjonalne rozwiązania! 🏢⚡

## 💻 Implementacja kodu

Kompletna implementacja w C# jest dostępna w pliku towarzyszącym `04-dotnet-agent-framework.cs`. Ten pojedynczy plik aplikacji .NET pokazuje:

- Ładowanie zmiennych środowiskowych dla konfiguracji modeli GitHub
- Definiowanie niestandardowych narzędzi za pomocą metod C# z atrybutami
- Tworzenie agenta AI z integracją narzędzi
- Zarządzanie wątkami konwersacji
- Wykonywanie żądań agenta z wywołaniem narzędzi

Aby uruchomić przykład:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Lub używając .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.