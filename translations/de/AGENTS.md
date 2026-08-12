# AGENTS.md

## Projektübersicht

Dieses Repository enthält "KI-Agenten für Anfänger" - einen umfassenden Bildungskurs, der alles vermittelt, was zum Erstellen von KI-Agenten benötigt wird. Der Kurs besteht aus 18 Lektionen (nummeriert 00-18) und behandelt Grundlagen, Designmuster, Frameworks, Produktionseinsatz, lokale/On-Device-Agenten und Sicherheit von KI-Agenten.

**Wichtige Technologien:**
- Python 3.12+
- Jupyter-Notebooks für interaktives Lernen
- KI-Frameworks: Microsoft Agent Framework (MAF)
- Azure KI-Dienste: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektur:**
- Lektionen-basierte Struktur (00-15+ Verzeichnisse)
- Jede Lektion enthält: README-Dokumentation, Codebeispiele (Jupyter-Notebooks) und Bilder
- Mehrsprachige Unterstützung über automatisiertes Übersetzungssystem
- Ein Python-Notebook pro Lektion mit Microsoft Agent Framework

## Setup-Befehle

### Voraussetzungen
- Python 3.12 oder höher
- Azure-Abonnement (für Microsoft Foundry)
- Azure CLI installiert und authentifiziert (`az login`)

### Ersteinrichtung

1. **Repository klonen oder forken:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ODER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python-virtuelle Umgebung erstellen und aktivieren:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Unter Windows: venv\Scripts\activate
   ```

3. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Umgebungsvariablen einrichten:**
   ```bash
   cp .env.example .env
   # Bearbeiten Sie .env mit Ihren API-Schlüsseln und Endpunkten
   ```

### Erforderliche Umgebungsvariablen

Für **Microsoft Foundry** (erforderlich):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry Projektendpunkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modellbereitstellungsname (z.B. gpt-5-mini)

Für **Azure AI Search** (Lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search Endpunkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-Schlüssel

Authentifizierung: Vor Ausführung der Notebooks `az login` ausführen (verwendet `AzureCliCredential`).

## Entwicklungsablauf

### Jupyter-Notebooks ausführen

Jede Lektion enthält mehrere Jupyter-Notebooks für unterschiedliche Frameworks:

1. **Jupyter starten:**
   ```bash
   jupyter notebook
   ```

2. **In ein Lektionenverzeichnis navigieren** (z.B. `01-intro-to-ai-agents/code_samples/`)

3. **Notebooks öffnen und ausführen:**
   - `*-python-agent-framework.ipynb` - Mit Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Mit Microsoft Agent Framework (.NET)

### Arbeiten mit Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Erfordert Azure-Abonnement
- Verwendet `FoundryChatClient` für Agent Service V2 (Agenten sichtbar im Foundry-Portal)
- Produktionsbereit mit integrierter Beobachtbarkeit
- Dateimuster: `*-python-agent-framework.ipynb`

## Testanweisungen

Dies ist ein Bildungsrepository mit Beispielcode und nicht produktionsreifem Code mit automatisierten Tests. Um Ihre Einrichtung und Änderungen zu überprüfen:

### Manueller Test

1. **Python-Umgebung testen:**
   ```bash
   python --version  # Sollte 3.12+ sein
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Notebook-Ausführung testen:**
   ```bash
   # Notebook in Skript umwandeln und ausführen (prüft Importe)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Umgebungsvariablen überprüfen:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Einzelne Notebooks ausführen

Öffnen Sie die Notebooks in Jupyter und führen Sie die Zellen sequentiell aus. Jedes Notebook ist eigenständig und beinhaltet:
- Import-Anweisungen
- Konfigurationsladen
- Beispielimplementierungen von Agenten
- Erwartete Ausgaben in Markdown-Zellen

### Smoke-Test von bereitgestellten Agenten

Für Lektionen, in denen ein Agent als Microsoft Foundry gehosteter Agent bereitgestellt wird (01, 04, 05, 16), enthält das Repo Smoke-Test-Kataloge unter `tests/`, die vom Workflow `.github/workflows/smoke-test.yml` über die Aktion [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) ausgeführt werden. Diese sind ein leichter Nachbereitungs-Gate (ist der Agent erreichbar und folgt den grundlegenden Prompt-Erwartungen?), ergänzen die Evaluierungspipeline in den Lektionen 10 und 16. Siehe [tests/README.md](./tests/README.md) für die Zuordnung Katalog→Lektion→Agent. Lektion 17 läuft lokal mit Foundry Local und hat keinen gehosteten Endpunkt, daher wird sie durch direkte Ausführung des Notebooks validiert.

## Code-Stil

### Python-Konventionen

- **Python-Version**: 3.12+
- **Code-Stil**: Folge den Standard-Python-PEP-8-Konventionen
- **Notebooks**: Verwende klare Markdown-Zellen zur Erklärung von Konzepten
- **Imports**: Gruppiere nach Standardbibliothek, Drittanbieter, lokale Imports

### Jupyter-Notebook-Konventionen

- Einschließen beschreibender Markdown-Zellen vor Code-Zellen
- Füge Ausgabebeispiele in Notebooks zur Referenz hinzu
- Klare Variablennamen verwenden, die zu den Lektionsthemen passen
- Lineare Ausführungsreihenfolge der Notebooks beibehalten (Zelle 1 → 2 → 3...)

### Dateiorganisation

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Erstellen und Bereitstellen

### Dokumentation erstellen

Dieses Repository verwendet Markdown für die Dokumentation:
- README.md-Dateien in jedem Lektionenordner
- Haupt-README.md im Repository-Stamm
- Automatisiertes Übersetzungssystem über GitHub Actions

### CI/CD-Pipeline

Befindet sich in `.github/workflows/`:

1. **co-op-translator.yml** - Automatische Übersetzung in über 50 Sprachen
2. **welcome-issue.yml** - Begrüßt neue Issue-Ersteller
3. **welcome-pr.yml** - Begrüßt neue Pull-Request-Beiträge

### Bereitstellung

Dies ist ein Bildungsrepository - kein Bereitstellungsprozess. Anwender:
1. Forken oder klonen das Repository
2. Führen Notebooks lokal oder in GitHub Codespaces aus
3. Lernen durch Modifikation und Experimente mit Beispielen

## Richtlinien für Pull Requests

### Vor dem Einreichen

1. **Teste deine Änderungen:**
   - Führe betroffene Notebooks vollständig aus
   - Überprüfe, dass alle Zellen fehlerfrei ausgeführt werden
   - Prüfe, ob die Ausgaben angemessen sind

2. **Aktualisierung der Dokumentation:**
   - README.md aktualisieren, wenn neue Konzepte hinzugefügt werden
   - Kommentare in Notebooks für komplexen Code hinzufügen
   - Sicherstellen, dass Markdown-Zellen den Zweck erklären

3. **Dateiänderungen:**
   - Vermeide das Committen von `.env`-Dateien (verwende `.env.example`)
   - Committe keine `venv/`- oder `__pycache__/`-Verzeichnisse
   - Behalte Notebook-Ausgaben, wenn sie Konzepte veranschaulichen
   - Entferne temporäre Dateien und Backup-Notebooks (`*-backup.ipynb`)

### Format des PR-Titels

Verwende beschreibende Titel:
- `[Lesson-XX] Neues Beispiel für <Konzept> hinzufügen`
- `[Fix] Tipfehler im lesson-XX README korrigieren`
- `[Update] Codebeispiel in lesson-XX verbessern`
- `[Docs] Setup-Anleitungen aktualisieren`

### Erforderliche Prüfungen

- Notebooks sollten fehlerfrei ausgeführt werden
- README-Dateien sollten klar und genau sein
- Bestehenden Code-Patterns im Repository folgen
- Konsistenz mit anderen Lektionen beibehalten

## Zusätzliche Hinweise

### Häufige Stolpersteine

1. **Python-Versionskonflikt:**
   - Achte auf Python 3.12+
   - Einige Pakete funktionieren nicht mit älteren Versionen
   - Nutze `python3 -m venv`, um Python-Version explizit festzulegen

2. **Umgebungsvariablen:**
   - Erstelle immer `.env` aus `.env.example`
   - Committe die `.env`-Datei nicht (ist in `.gitignore`)
   - Melde dich mit `az login` für schlüssel-losen Entra ID-Zugang an

3. **Paketkonflikte:**
   - Verwende eine frische virtuelle Umgebung
   - Installiere aus `requirements.txt` und nicht einzelne Pakete
   - Einige Notebooks benötigen zusätzliche Pakete, die in ihren Markdown-Zellen erwähnt sind

4. **Azure-Dienste:**
   - Azure AI-Dienste erfordern ein aktives Abonnement
   - Einige Funktionen sind regionsspezifisch
   - Stelle sicher, dass deine Azure OpenAI Modellbereitstellung die Responses API unterstützt

### Lernpfad

Empfohlene Reihenfolge der Lektionen:
1. **00-course-setup** - Beginne hier für die Umgebungseinrichtung
2. **01-intro-to-ai-agents** - Verstehe die Grundlagen von KI-Agenten
3. **02-explore-agentic-frameworks** - Lerne verschiedene Frameworks kennen
4. **03-agentic-design-patterns** - Kerndesignmuster
5. Folge den nummerierten Lektionen der Reihe nach

### Framework-Auswahl

Wähle das Framework entsprechend deiner Ziele:
- **Alle Lektionen**: Microsoft Agent Framework (MAF) mit `FoundryChatClient`
- **Agenten registrieren sich serverseitig** im Microsoft Foundry Agent Service V2 und sind im Foundry-Portal sichtbar

### Hilfe erhalten

- Tritt dem [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) bei
- Sieh dir die README-Dateien der Lektionen für spezifische Anleitungen an
- Schaue im Haupt-[README.md](./README.md) für Kursübersicht nach
- Siehe [Course Setup](./00-course-setup/README.md) für detaillierte Einrichtungshinweise

### Beitrag leisten

Dies ist ein offenes Bildungsprojekt. Beiträge sind willkommen:
- Verbesserung der Code-Beispiele
- Korrigieren von Tippfehlern oder Fehlern
- Hinzufügen erklärender Kommentare
- Vorschlagen neuer Lernthemen
- Übersetzung in weitere Sprachen

Siehe [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) für aktuelle Bedürfnisse.

## Projektspezifischer Kontext

### Mehrsprachige Unterstützung

Dieses Repository verwendet ein automatisiertes Übersetzungssystem:
- Über 50 unterstützte Sprachen
- Übersetzungen in Verzeichnissen `/translations/<lang-code>/`
- GitHub Actions Workflow verwaltet Übersetzungsupdates
- Quelldateien sind auf Englisch im Repository-Stamm

### Lektionenstruktur

Jede Lektion folgt einem konsistenten Muster:
1. Videovorschaubild mit Link
2. Geschriebener Lektionstext (README.md)
3. Codebeispiele in mehreren Frameworks
4. Lernziele und Voraussetzungen
5. Verlinkte zusätzliche Lernressourcen

### Benennung von Code-Beispielen

Format: `<lektion-nummer>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, MAF fortgeschrittene Muster
- `16-python-agent-framework.ipynb` - Lektion 16, produktionsreifer Kundensupport-Agent
- `17-local-agent-foundry-local.ipynb` - Lektion 17, lokaler Agent mit Foundry Local + Qwen

### Spezielle Verzeichnisse

- `translated_images/` - Lokalisierte Bilder für Übersetzungen
- `images/` - Originalbilder für englische Inhalte
- `.devcontainer/` - VS Code Entwicklungscontainer-Konfiguration
- `.github/` - GitHub Actions Workflows und Vorlagen

### Abhängigkeiten

Schlüssel-Pakete aus `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent-Protokoll-Unterstützung
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-Dienste
- `azure-identity` - Azure-Authentifizierung (AzureCliCredential)
- `azure-search-documents` - Azure AI Search Integration
- `mcp[cli]` - Model Context Protocol Unterstützung

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->