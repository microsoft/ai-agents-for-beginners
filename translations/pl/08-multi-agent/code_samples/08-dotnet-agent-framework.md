# 🤝 Zaawansowane systemy wieloagentowe dla przedsiębiorstw (.NET)

## 📋 Cele nauki

Ten notatnik demonstruje, jak zbudować zaawansowane systemy wieloagentowe klasy korporacyjnej, wykorzystując Microsoft Agent Framework w .NET z Azure OpenAI (Responses API). Nauczysz się, jak orkiestrując wielu wyspecjalizowanych agentów współpracujących poprzez ustrukturyzowane przepływy pracy, wykorzystać możliwości .NET do rozwiązań gotowych do produkcji.

**Możliwości wieloagentowe dla przedsiębiorstw, które zbudujesz:**
- 👥 **Współpraca agentów**: Koordynacja agentów z typowaniem i walidacją podczas kompilacji
- 🔄 **Orkiestracja przepływów pracy**: Deklaratywne definiowanie przepływów pracy za pomocą async w .NET
- 🎭 **Specjalizacja ról**: Silnie typowane osobowości agentów i dziedziny specjalizacji
- 🏢 **Integracja korporacyjna**: Wzorce produkcyjne z monitorowaniem i obsługą błędów

## ⚙️ Wymagania wstępne i konfiguracja

**Środowisko programistyczne:**
- SDK .NET 9.0 lub nowszy
- Visual Studio 2022 lub VS Code z rozszerzeniem C#
- Subskrypcja Azure (dla agentów trwałych)

**Wymagane pakiety NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Przykład kodu

Kompletny działający kod do tej lekcji dostępny jest w dołączonym pliku C#: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Aby uruchomić przykład:

```bash
# Uczyń plik wykonywalnym (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Uruchom próbkę
./08-dotnet-agent-framework.cs
```

Lub korzystając z .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Co demonstruje ten przykład

Ten system wieloagentowy tworzy usługę rekomendacji podróży hotelowych z dwoma wyspecjalizowanymi agentami:

1. **Agent FrontDesk**: Agent podróży, który dostarcza rekomendacje aktywności i lokalizacji
2. **Agent Concierge**: Przegląda rekomendacje, aby zapewnić autentyczne, nieturystyczne doświadczenia

Agenci współpracują w przepływie pracy, w którym:
- Agent FrontDesk odbiera początkowe żądanie podróży
- Agent Concierge przegląda i udoskonala rekomendacje
- Przepływ pracy realizuje przesyłanie odpowiedzi na żywo

## Kluczowe pojęcia

### Koordynacja agentów
Przykład demonstruje bezpieczną typowo koordynację agentów przy użyciu Microsoft Agent Framework z walidacją podczas kompilacji.

### Orkiestracja przepływów pracy
Wykorzystuje deklaratywne definiowanie przepływów pracy za pomocą async w .NET do łączenia wielu agentów w potok.

### Przesyłanie odpowiedzi na żywo
Implementuje przesyłanie w czasie rzeczywistym odpowiedzi agentów korzystając z async enumerables i architektury opartej na zdarzeniach.

### Integracja korporacyjna
Pokazuje wzorce gotowe do produkcji, w tym:
- Konfigurację zmiennych środowiskowych
- Bezpieczne zarządzanie poświadczeniami
- Obsługę błędów
- Asynchroniczne przetwarzanie zdarzeń

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->