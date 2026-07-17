# 🎯 Planung & Entwurfsmuster mit Azure OpenAI (Responses API) (.NET)

## 📋 Lernziele

Dieses Notebook zeigt unternehmensgerechte Planungs- und Entwurfsmuster für den Aufbau intelligenter Agenten mit dem Microsoft Agent Framework in .NET und Azure OpenAI (Responses API). Sie lernen, Agenten zu erstellen, die komplexe Probleme zerlegen, mehrstufige Lösungen planen und ausgeklügelte Workflows mit den Enterprise-Funktionen von .NET ausführen können.

## ⚙️ Voraussetzungen & Einrichtung

**Entwicklungsumgebung:**
- .NET 9.0 SDK oder höher
- Visual Studio 2022 oder VS Code mit C#-Erweiterung
- Ein Azure-Abonnement mit einer Azure OpenAI-Ressource und einem Modell-Deployment
- Die Azure CLI — Anmeldung mit `az login`

**Benötigte Abhängigkeiten:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Umgebungskonfiguration (.env-Datei):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## Den Code ausführen

Diese Lektion beinhaltet eine Implementierung als .NET Single File App. Zum Ausführen:

```bash
# Machen Sie die Datei ausführbar (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Führen Sie die Anwendung aus
./07-dotnet-agent-framework.cs
```

Oder nutzen Sie den Befehl dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Code-Implementierung

Die vollständige Implementierung finden Sie in `07-dotnet-agent-framework.cs`, welche Folgendes demonstriert:

- Laden der Umgebungskonfiguration mit DotNetEnv
- Konfigurieren des Azure OpenAI-Clients und Erstellen eines KI-Agenten mit `GetChatClient().AsAIAgent()`
- Definieren strukturierter Datenmodelle (Plan und TravelPlan) mit JSON-Serialisierung
- Erstellen eines KI-Agenten mit strukturiertem Output mittels JSON-Schema
- Ausführen von Planungsanfragen mit typsicheren Antworten

## Schlüsselkonzepte

### Strukturiertes Planen mit typsicheren Modellen

Der Agent verwendet C#-Klassen, um die Struktur der Planungsausgaben zu definieren:

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

### JSON-Schema für strukturierte Ausgaben

Der Agent ist so konfiguriert, dass er Antworten zurückgibt, die dem TravelPlan-Schema entsprechen:

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

### Anweisungen für den Planungsagenten

Der Agent fungiert als Koordinator und delegiert Aufgaben an spezialisierte Teilagenten:

- FlightBooking: Für Flugbuchungen und Fluginformationen
- HotelBooking: Für Hotelbuchungen und Hotelinformationen
- CarRental: Für Mietwagenbuchungen und Mietwageninformationen
- ActivitiesBooking: Für Buchung von Aktivitäten und Bereitstellung von Aktivitätsinformationen
- DestinationInfo: Für die Bereitstellung von Informationen über Reiseziele
- DefaultAgent: Für die Bearbeitung allgemeiner Anfragen

## Erwartete Ausgabe

Wenn Sie den Agenten mit einer Reiseplanungsanfrage ausführen, analysiert er die Anfrage und generiert einen strukturierten Plan mit passenden Aufgabenverteilungen an spezialisierte Agenten, formatiert als JSON entsprechend dem TravelPlan-Schema.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->