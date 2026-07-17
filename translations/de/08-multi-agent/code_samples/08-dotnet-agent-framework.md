# 🤝 Enterprise-Multi-Agent-Workflow-Systeme (.NET)

## 📋 Lernziele

Dieses Notebook zeigt, wie man anspruchsvolle Multi-Agenten-Systeme auf Unternehmensniveau mit dem Microsoft Agent Framework in .NET und Azure OpenAI (Responses API) erstellt. Sie lernen, mehrere spezialisierte Agenten zu orchestrieren, die durch strukturierte Workflows zusammenarbeiten, und nutzen dabei die Enterprise-Funktionen von .NET für produktionsreife Lösungen.

**Enterprise-Multi-Agent-Fähigkeiten, die Sie entwickeln werden:**
- 👥 **Agentenzusammenarbeit**: Typsichere Agentenkoordination mit Kompilierzeit-Validierung
- 🔄 **Workflow-Orchestrierung**: Deklarative Workflow-Definition mit .NET-Async-Mustern
- 🎭 **Rollenspezialisierung**: Stark typisierte Agentenpersönlichkeiten und Expertendomänen
- 🏢 **Enterprise-Integration**: Produktionsreife Muster mit Überwachung und Fehlerbehandlung

## ⚙️ Voraussetzungen & Einrichtung

**Entwicklungsumgebung:**
- .NET 9.0 SDK oder höher
- Visual Studio 2022 oder VS Code mit C#-Erweiterung
- Azure-Abonnement (für persistenten Agenten)

**Erforderliche NuGet-Pakete:**
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

## Codebeispiel

Der vollständige funktionierende Code für diese Lektion ist in der begleitenden C#-Datei verfügbar: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Um das Beispiel auszuführen:

```bash
# Die Datei ausführbar machen (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Das Beispiel ausführen
./08-dotnet-agent-framework.cs
```

Oder mit dem .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Was dieses Beispiel demonstriert

Dieses Multi-Agenten-Workflow-System erstellt einen Hotel-Reiseempfehlungsdienst mit zwei spezialisierten Agenten:

1. **FrontDesk Agent**: Ein Reiseberater, der Aktivitäten- und Orts-Empfehlungen gibt
2. **Concierge Agent**: Prüft die Empfehlungen, um authentische, nicht-touristische Erlebnisse sicherzustellen

Die Agenten arbeiten in einem Workflow zusammen, bei dem:
- Der FrontDesk-Agent die ursprüngliche Reiseanfrage erhält
- Der Concierge-Agent die Empfehlung prüft und verfeinert
- Der Workflow Antworten in Echtzeit streamt

## Schlüsselkonzepte

### Agentenkoordination
Das Beispiel zeigt typsichere Agentenkoordination mit dem Microsoft Agent Framework und Kompilierzeit-Validierung.

### Workflow-Orchestrierung
Verwendet deklarative Workflow-Definition mit .NET-Async-Mustern, um mehrere Agenten in einer Pipeline zu verbinden.

### Streaming-Antworten
Implementiert Echtzeit-Streaming von Agentenantworten mithilfe async enumerables und ereignisgesteuerter Architektur.

### Enterprise-Integration
Zeigt produktionsreife Muster, einschließlich:
- Konfiguration von Umgebungsvariablen
- Sichere Verwaltung von Anmeldedaten
- Fehlerbehandlung
- Asynchrone Ereignisverarbeitung

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->