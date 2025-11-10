<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:16:03+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "pl"
}
-->
# 🤝 Systemy Przepływu Pracy Wieloagentowej dla Przedsiębiorstw (.NET)

## 📋 Cele Nauki

Ten notebook pokazuje, jak budować zaawansowane systemy wieloagentowe na poziomie przedsiębiorstwa, korzystając z Microsoft Agent Framework w .NET z modelami GitHub. Nauczysz się koordynować pracę wielu wyspecjalizowanych agentów w ramach zorganizowanych przepływów pracy, wykorzystując funkcje .NET dla rozwiązań gotowych do produkcji.

**Funkcje Wieloagentowe dla Przedsiębiorstw, które Zbudujesz:**
- 👥 **Współpraca Agentów**: Koordynacja agentów z walidacją w czasie kompilacji
- 🔄 **Orkiestracja Przepływu Pracy**: Deklaratywne definiowanie przepływów pracy z wykorzystaniem asynchronicznych wzorców .NET
- 🎭 **Specjalizacja Ról**: Silnie typowane osobowości agentów i ich domeny ekspertyzy
- 🏢 **Integracja Przedsiębiorstw**: Wzorce gotowe do produkcji z monitorowaniem i obsługą błędów

## ⚙️ Wymagania Wstępne i Konfiguracja

**Środowisko Programistyczne:**
- .NET 9.0 SDK lub nowszy
- Visual Studio 2022 lub VS Code z rozszerzeniem C#
- Subskrypcja Azure (dla trwałych agentów)

**Wymagane Pakiety NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Przykład Kodów

Kompletny kod dla tej lekcji znajduje się w załączonym pliku C#: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Aby uruchomić przykład:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Lub korzystając z .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Co Pokazuje Ten Przykład

Ten system przepływu pracy wieloagentowej tworzy usługę rekomendacji podróży hotelowych z dwoma wyspecjalizowanymi agentami:

1. **Agent Recepcji**: Agent podróży, który dostarcza rekomendacje dotyczące aktywności i lokalizacji
2. **Agent Konsjerża**: Przegląda rekomendacje, aby zapewnić autentyczne, nieturystyczne doświadczenia

Agenci współpracują w przepływie pracy, gdzie:
- Agent Recepcji otrzymuje początkowe zapytanie dotyczące podróży
- Agent Konsjerża przegląda i udoskonala rekomendację
- Przepływ pracy przesyła odpowiedzi w czasie rzeczywistym

## Kluczowe Koncepcje

### Koordynacja Agentów
Przykład pokazuje koordynację agentów z walidacją w czasie kompilacji, korzystając z Microsoft Agent Framework.

### Orkiestracja Przepływu Pracy
Wykorzystuje deklaratywne definiowanie przepływów pracy z asynchronicznymi wzorcami .NET, aby połączyć wielu agentów w jednym pipeline.

### Strumieniowanie Odpowiedzi
Implementuje strumieniowanie odpowiedzi agentów w czasie rzeczywistym, korzystając z asynchronicznych enumeratorów i architektury opartej na zdarzeniach.

### Integracja Przedsiębiorstw
Pokazuje wzorce gotowe do produkcji, w tym:
- Konfigurację zmiennych środowiskowych
- Bezpieczne zarządzanie poświadczeniami
- Obsługę błędów
- Asynchroniczne przetwarzanie zdarzeń

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, należy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.