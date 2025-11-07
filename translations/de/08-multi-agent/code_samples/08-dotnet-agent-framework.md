<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:13:18+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "de"
}
-->
# 🤝 Enterprise Multi-Agent Workflow-Systeme (.NET)

## 📋 Lernziele

Dieses Notebook zeigt, wie man anspruchsvolle Multi-Agent-Systeme auf Unternehmensniveau mit dem Microsoft Agent Framework in .NET und GitHub-Modellen erstellt. Sie lernen, mehrere spezialisierte Agenten durch strukturierte Workflows zu orchestrieren und dabei die Enterprise-Funktionen von .NET für produktionsreife Lösungen zu nutzen.

**Fähigkeiten für Enterprise-Multi-Agent-Systeme, die Sie entwickeln werden:**
- 👥 **Agenten-Kollaboration**: Typensichere Koordination von Agenten mit Validierung zur Kompilierungszeit
- 🔄 **Workflow-Orchestrierung**: Deklarative Workflow-Definition mit den asynchronen Mustern von .NET
- 🎭 **Rollen-Spezialisierung**: Stark typisierte Agentenpersönlichkeiten und Fachgebiete
- 🏢 **Enterprise-Integration**: Produktionsreife Muster mit Überwachung und Fehlerbehandlung

## ⚙️ Voraussetzungen & Einrichtung

**Entwicklungsumgebung:**
- .NET 9.0 SDK oder höher
- Visual Studio 2022 oder VS Code mit C#-Erweiterung
- Azure-Abonnement (für persistente Agenten)

**Erforderliche NuGet-Pakete:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Codebeispiel

Der vollständige funktionierende Code für diese Lektion ist in der begleitenden C#-Datei verfügbar: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Um das Beispiel auszuführen:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Oder mit der .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Was dieses Beispiel zeigt

Dieses Multi-Agent-Workflow-System erstellt einen Hotel-Reiseempfehlungsdienst mit zwei spezialisierten Agenten:

1. **FrontDesk-Agent**: Ein Reiseagent, der Aktivitäten- und Standortempfehlungen bereitstellt
2. **Concierge-Agent**: Überprüft Empfehlungen, um authentische, nicht touristische Erlebnisse sicherzustellen

Die Agenten arbeiten in einem Workflow zusammen, bei dem:
- Der FrontDesk-Agent die ursprüngliche Reiseanfrage erhält
- Der Concierge-Agent die Empfehlung überprüft und verfeinert
- Der Workflow Antworten in Echtzeit streamt

## Schlüsselkonzepte

### Agenten-Koordination
Das Beispiel zeigt typensichere Agenten-Koordination mit dem Microsoft Agent Framework und Validierung zur Kompilierungszeit.

### Workflow-Orchestrierung
Verwendet deklarative Workflow-Definition mit den asynchronen Mustern von .NET, um mehrere Agenten in einer Pipeline zu verbinden.

### Streaming-Antworten
Implementiert Echtzeit-Streaming von Agenten-Antworten mit asynchronen Enumerables und ereignisgesteuerter Architektur.

### Enterprise-Integration
Zeigt produktionsreife Muster, einschließlich:
- Konfiguration von Umgebungsvariablen
- Sichere Verwaltung von Anmeldeinformationen
- Fehlerbehandlung
- Asynchrone Ereignisverarbeitung

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.