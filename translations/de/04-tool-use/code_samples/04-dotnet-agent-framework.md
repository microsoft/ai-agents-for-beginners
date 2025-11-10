<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:20:50+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "de"
}
-->
# 🛠️ Erweiterte Werkzeugnutzung mit GitHub-Modellen (.NET)

## 📋 Lernziele

Dieses Notebook zeigt Integrationsmuster für Unternehmenswerkzeuge mit dem Microsoft Agent Framework in .NET und GitHub-Modellen. Sie lernen, wie man anspruchsvolle Agenten mit mehreren spezialisierten Werkzeugen erstellt und dabei die starke Typisierung von C# sowie die Unternehmensfunktionen von .NET nutzt.

**Fortgeschrittene Werkzeugfähigkeiten, die Sie meistern werden:**
- 🔧 **Multi-Tool-Architektur**: Agenten mit mehreren spezialisierten Fähigkeiten erstellen
- 🎯 **Typensichere Werkzeugausführung**: Nutzung der Kompilierungszeitvalidierung von C#
- 📊 **Unternehmens-Werkzeugmuster**: Produktionsreife Werkzeuggestaltung und Fehlerbehandlung
- 🔗 **Werkzeugkomposition**: Kombination von Werkzeugen für komplexe Geschäftsabläufe

## 🎯 Vorteile der .NET-Werkzeugarchitektur

### Unternehmens-Werkzeugfunktionen
- **Kompilierungszeitvalidierung**: Starke Typisierung gewährleistet die Korrektheit der Werkzeugparameter
- **Dependency Injection**: IoC-Container-Integration für Werkzeugverwaltung
- **Async/Await-Muster**: Nicht blockierende Werkzeugausführung mit ordnungsgemäßem Ressourcenmanagement
- **Strukturiertes Logging**: Eingebaute Logging-Integration zur Überwachung der Werkzeugausführung

### Produktionsreife Muster
- **Fehlerbehandlung**: Umfassendes Fehlermanagement mit typisierten Ausnahmen
- **Ressourcenmanagement**: Ordnungsgemäße Entsorgungsmuster und Speicherverwaltung
- **Leistungsüberwachung**: Eingebaute Metriken und Leistungszähler
- **Konfigurationsmanagement**: Typensichere Konfiguration mit Validierung

## 🔧 Technische Architektur

### Kernkomponenten der .NET-Werkzeuge
- **Microsoft.Extensions.AI**: Einheitliche Abstraktionsschicht für Werkzeuge
- **Microsoft.Agents.AI**: Unternehmensgerechte Werkzeugorchestrierung
- **GitHub Models Integration**: Hochleistungsfähiger API-Client mit Verbindungspooling

### Werkzeugausführungspipeline
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Werkzeugkategorien & Muster

### 1. **Datenverarbeitungswerkzeuge**
- **Eingabevalidierung**: Starke Typisierung mit Datenanmerkungen
- **Transformationsoperationen**: Typensichere Datenkonvertierung und -formatierung
- **Geschäftslogik**: Domänenspezifische Berechnungs- und Analysetools
- **Ausgabeformatierung**: Strukturierte Antwortgenerierung

### 2. **Integrationswerkzeuge**
- **API-Connectoren**: RESTful-Service-Integration mit HttpClient
- **Datenbankwerkzeuge**: Entity Framework-Integration für Datenzugriff
- **Dateioperationen**: Sichere Dateisystemoperationen mit Validierung
- **Externe Dienste**: Muster für die Integration von Drittanbieterdiensten

### 3. **Hilfswerkzeuge**
- **Textverarbeitung**: Zeichenkettenmanipulation und Formatierungswerkzeuge
- **Datum-/Zeitoperationen**: Kulturabhängige Berechnungen von Datum/Zeit
- **Mathematische Werkzeuge**: Präzisionsberechnungen und statistische Operationen
- **Validierungswerkzeuge**: Validierung von Geschäftsregeln und Datenüberprüfung

## ⚙️ Voraussetzungen & Einrichtung

**Entwicklungsumgebung:**
- .NET 9.0 SDK oder höher
- Visual Studio 2022 oder VS Code mit C#-Erweiterung
- Zugriff auf die GitHub Models API

**Erforderliche NuGet-Pakete:**
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

Bereit, Unternehmensagenten mit leistungsstarken, typensicheren Werkzeugfähigkeiten in .NET zu erstellen? Lassen Sie uns professionelle Lösungen entwickeln! 🏢⚡

## 💻 Code-Implementierung

Die vollständige C#-Implementierung finden Sie in der Begleitdatei `04-dotnet-agent-framework.cs`. Diese .NET-Single-File-App demonstriert:

- Laden von Umgebungsvariablen für die Konfiguration der GitHub-Modelle
- Definition benutzerdefinierter Werkzeuge mit C#-Methoden und Attributen
- Erstellung eines KI-Agenten mit Werkzeugintegration
- Verwaltung von Konversationssträngen
- Ausführung von Agentenanfragen mit Werkzeugaufrufen

Um das Beispiel auszuführen:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Oder mit dem .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.