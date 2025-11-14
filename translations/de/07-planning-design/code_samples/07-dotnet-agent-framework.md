<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:54:22+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "de"
}
-->
# 🎯 Planung & Designmuster mit GitHub-Modellen (.NET)

## 📋 Lernziele

Dieses Notebook zeigt unternehmensgerechte Planungs- und Designmuster für den Aufbau intelligenter Agenten mit dem Microsoft Agent Framework in .NET und GitHub-Modellen. Sie lernen, Agenten zu erstellen, die komplexe Probleme zerlegen, mehrstufige Lösungen planen und anspruchsvolle Workflows mit den Unternehmensfunktionen von .NET ausführen können.

## ⚙️ Voraussetzungen & Einrichtung

**Entwicklungsumgebung:**
- .NET 9.0 SDK oder höher
- Visual Studio 2022 oder VS Code mit C#-Erweiterung
- Zugriff auf die GitHub Models API

**Erforderliche Abhängigkeiten:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Umgebungskonfiguration (.env-Datei):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Code ausführen

Diese Lektion enthält eine Implementierung als .NET Single File App. Um sie auszuführen:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Oder verwenden Sie den Befehl dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Code-Implementierung

Die vollständige Implementierung ist in `07-dotnet-agent-framework.cs` verfügbar und zeigt:

- Laden der Umgebungskonfiguration mit DotNetEnv
- Konfiguration des OpenAI-Clients für GitHub-Modelle
- Definition strukturierter Datenmodelle (Plan und TravelPlan) mit JSON-Serialisierung
- Erstellung eines KI-Agenten mit strukturiertem Output unter Verwendung eines JSON-Schemas
- Ausführung von Planungsanfragen mit typensicheren Antworten

## Schlüsselkonzepte

### Strukturierte Planung mit typensicheren Modellen

Der Agent verwendet C#-Klassen, um die Struktur der Planungsoutputs zu definieren:

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

### JSON-Schema für strukturierte Outputs

Der Agent ist so konfiguriert, dass er Antworten liefert, die dem TravelPlan-Schema entsprechen:

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

### Anweisungen für den Planungsagenten

Der Agent fungiert als Koordinator und delegiert Aufgaben an spezialisierte Sub-Agenten:

- FlightBooking: Für die Buchung von Flügen und Bereitstellung von Fluginformationen
- HotelBooking: Für die Buchung von Hotels und Bereitstellung von Hotelinformationen
- CarRental: Für die Buchung von Autos und Bereitstellung von Mietwageninformationen
- ActivitiesBooking: Für die Buchung von Aktivitäten und Bereitstellung von Aktivitätsinformationen
- DestinationInfo: Für die Bereitstellung von Informationen über Reiseziele
- DefaultAgent: Für die Bearbeitung allgemeiner Anfragen

## Erwartetes Ergebnis

Wenn Sie den Agenten mit einer Reiseplanungsanfrage ausführen, analysiert er die Anfrage und erstellt einen strukturierten Plan mit entsprechenden Aufgaben, die an spezialisierte Agenten delegiert werden. Der Output wird als JSON formatiert, das dem TravelPlan-Schema entspricht.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.