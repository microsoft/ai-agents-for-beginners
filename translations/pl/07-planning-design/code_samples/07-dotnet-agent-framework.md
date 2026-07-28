# 🎯 Planowanie i Wzorce Projektowe z Azure OpenAI (Responses API) (.NET)

## 📋 Cele Nauki

Ten notebook demonstruje wzorce planowania i projektowania klasy korporacyjnej do budowania inteligentnych agentów przy użyciu Microsoft Agent Framework w .NET z Azure OpenAI (Responses API). Nauczysz się tworzyć agentów, którzy potrafią dekomponować złożone problemy, planować rozwiązania wieloetapowe i wykonywać zaawansowane przepływy pracy z użyciem funkcji korporacyjnych .NET.

## ⚙️ Wymagania wstępne i konfiguracja

**Środowisko programistyczne:**
- .NET 9.0 SDK lub nowszy
- Visual Studio 2022 lub VS Code z rozszerzeniem C#
- Subskrypcja Azure z zasobem Azure OpenAI i wdrożeniem modelu
- Azure CLI — zaloguj się używając `az login`

**Wymagane zależności:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracja środowiska (plik .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Uruchamianie kodu

Ta lekcja zawiera implementację aplikacji .NET w pojedynczym pliku. Aby ją uruchomić:

```bash
# Uczyń plik wykonalnym (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Uruchom aplikację
./07-dotnet-agent-framework.cs
```

Lub użyj polecenia dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementacja kodu

Pełna implementacja jest dostępna w `07-dotnet-agent-framework.cs`, która demonstruje:

- Ładowanie konfiguracji środowiska za pomocą DotNetEnv
- Konfigurowanie klienta Azure OpenAI oraz tworzenie agenta AI przy użyciu `GetChatClient().AsAIAgent()`
- Definiowanie strukturalnych modeli danych (Plan i TravelPlan) z serializacją JSON
- Tworzenie agenta AI z ustrukturyzowanym wyjściem wykorzystując schemat JSON
- Wykonywanie zapytań planistycznych z typowo bezpiecznymi odpowiedziami

## Kluczowe pojęcia

### Ustrukturyzowane planowanie z modelami typowo bezpiecznymi

Agent wykorzystuje klasy C#, aby zdefiniować strukturę wyjścia planowania:

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

### Schemat JSON dla ustrukturyzowanych wyjść

Agent jest skonfigurowany do zwracania odpowiedzi zgodnych ze schematem TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Instrukcje dla agenta planistycznego

Agent działa jako koordynator, delegując zadania wyspecjalizowanym podagentom:

- FlightBooking: Do rezerwacji lotów i dostarczania informacji o lotach
- HotelBooking: Do rezerwacji hoteli i dostarczania informacji o hotelach
- CarRental: Do rezerwacji samochodów i dostarczania informacji o wynajmie samochodów
- ActivitiesBooking: Do rezerwacji aktywności i dostarczania informacji o nich
- DestinationInfo: Do udzielania informacji o miejscach docelowych
- DefaultAgent: Do obsługi ogólnych zapytań

## Oczekiwany wynik

Po uruchomieniu agenta z zapytaniem planistycznym dotyczącym podróży, agent przeanalizuje zapytanie i wygeneruje ustrukturyzowany plan z odpowiednim przydziałem zadań wyspecjalizowanym agentom, sformatowany jako JSON zgodny ze schematem TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->