<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:56:57+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "pl"
}
-->
# 🎯 Planowanie i wzorce projektowe z modelami GitHub (.NET)

## 📋 Cele nauki

Ten notebook przedstawia wzorce planowania i projektowania na poziomie korporacyjnym, które umożliwiają tworzenie inteligentnych agentów przy użyciu Microsoft Agent Framework w .NET z modelami GitHub. Nauczysz się tworzyć agentów, którzy potrafią rozkładać złożone problemy, planować rozwiązania wieloetapowe i realizować zaawansowane przepływy pracy z wykorzystaniem funkcji korporacyjnych .NET.

## ⚙️ Wymagania wstępne i konfiguracja

**Środowisko programistyczne:**
- .NET 9.0 SDK lub nowszy
- Visual Studio 2022 lub VS Code z rozszerzeniem C#
- Dostęp do API modeli GitHub

**Wymagane zależności:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracja środowiska (plik .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Uruchamianie kodu

Ta lekcja zawiera implementację aplikacji .NET w jednym pliku. Aby ją uruchomić:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Lub użyj polecenia dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementacja kodu

Kompletna implementacja znajduje się w pliku `07-dotnet-agent-framework.cs`, który demonstruje:

- Ładowanie konfiguracji środowiska za pomocą DotNetEnv
- Konfigurowanie klienta OpenAI dla modeli GitHub
- Definiowanie ustrukturyzowanych modeli danych (Plan i TravelPlan) z serializacją JSON
- Tworzenie agenta AI z ustrukturyzowanym wyjściem przy użyciu schematu JSON
- Wykonywanie zapytań planistycznych z odpowiedziami typu bezpiecznego

## Kluczowe pojęcia

### Ustrukturyzowane planowanie z modelami typu bezpiecznego

Agent używa klas C# do definiowania struktury wyników planowania:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### Schemat JSON dla ustrukturyzowanych wyników

Agent jest skonfigurowany do zwracania odpowiedzi zgodnych ze schematem TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Instrukcje dla agenta planującego

Agent działa jako koordynator, delegując zadania wyspecjalizowanym sub-agentom:

- FlightBooking: Rezerwacja lotów i dostarczanie informacji o lotach
- HotelBooking: Rezerwacja hoteli i dostarczanie informacji o hotelach
- CarRental: Rezerwacja samochodów i dostarczanie informacji o wynajmie samochodów
- ActivitiesBooking: Rezerwacja aktywności i dostarczanie informacji o aktywnościach
- DestinationInfo: Dostarczanie informacji o destynacjach
- DefaultAgent: Obsługa ogólnych zapytań

## Oczekiwany wynik

Po uruchomieniu agenta z zapytaniem dotyczącym planowania podróży, przeanalizuje on zapytanie i wygeneruje ustrukturyzowany plan z odpowiednimi przypisaniami zadań do wyspecjalizowanych agentów, sformatowany jako JSON zgodny ze schematem TravelPlan.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.