# AGENTS.md

## Projektübersicht

Dieses Repository enthält "KI-Agenten für Anfänger" - einen umfassenden Lernkurs, der alles Wichtige vermittelt, um KI-Agenten zu erstellen. Der Kurs besteht aus 18 Lektionen (nummeriert von 00 bis 18), die Grundlagen, Designmuster, Frameworks, Produktionseinsatz, lokale/auf dem Gerät laufende Agenten und Sicherheit von KI-Agenten abdecken.

**Wichtigste Technologien:**
- Python 3.12+
- Jupyter Notebooks für interaktives Lernen
- KI-Frameworks: Microsoft Agent Framework (MAF)
- Azure KI-Dienste: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektur:**
- Lektionen-basierte Struktur (Verzeichnisse 00-18)
- Jede Lektion enthält: README-Dokumentation, Code-Beispiele (Jupyter-Notebooks) und Bilder
- Mehrsprachige Unterstützung durch automatisiertes Übersetzungssystem
- Je ein Python-Notebook pro Lektion mit dem Microsoft Agent Framework

## Einrichtungskommandos

### Voraussetzungen
- Python 3.12 oder höher
- Azure-Abonnement (für Microsoft Foundry)
- Azure CLI installiert und authentifiziert (`az login`)

### Erste Einrichtung

1. **Repository klonen oder forken:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python-virtuelle Umgebung erstellen und aktivieren:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Umgebungsvariablen setzen:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Erforderliche Umgebungsvariablen

Für **Microsoft Foundry** (erforderlich):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry Projekt-Endpunkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modell-Deployment-Name (z.B. gpt-5-mini)

Für **Azure AI Search** (Lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search Endpunkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-Schlüssel

Authentifizierung: Führen Sie `az login` vor dem Ausführen der Notebooks aus (nutzt `AzureCliCredential`).

## Entwicklungsablauf

### Ausführen von Jupyter-Notebooks

Jede Lektion enthält mehrere Jupyter-Notebooks für unterschiedliche Frameworks:

1. **Jupyter starten:**
   ```bash
   jupyter notebook
   ```

2. **Zum Lektionen-Verzeichnis navigieren** (z.B. `01-intro-to-ai-agents/code_samples/`)

3. **Notebooks öffnen und ausführen:**
   - `*-python-agent-framework.ipynb` - Mit Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Mit Microsoft Agent Framework (.NET)

### Arbeiten mit dem Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Erfordert Azure-Abonnement
- Nutzt `FoundryChatClient` für Agent Service V2 (Agenten sichtbar im Foundry-Portal)
- Produktionsbereit mit integrierter Beobachtbarkeit
- Dateimuster: `*-python-agent-framework.ipynb`

## Testanweisungen

Dies ist ein Lern-Repository mit Beispielcode, kein Produktionscode mit automatisierten Tests. Zur Überprüfung Ihrer Einrichtung und Änderungen:

### Manuelles Testen

1. **Python-Umgebung testen:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Notebook-Ausführung testen:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Umgebungsvariablen prüfen:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Einzelne Notebooks ausführen

Öffnen Sie Notebooks in Jupyter und führen Sie die Zellen nacheinander aus. Jedes Notebook ist eigenständig und enthält:
- Import-Anweisungen
- Konfigurationsladung
- Beispielimplementierungen von Agenten
- Erwartete Ausgaben in Markdown-Zellen

### Smoke-Tests für bereitgestellte Agenten

Für Lektionen, in denen ein Agent als Microsoft Foundry-hosted Agent bereitgestellt wird (01, 04, 05, 16), liefert das Repo Smoke-Testkataloge unter `tests/`, die vom `.github/workflows/smoke-test.yml`-Workflow über die [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) Aktion ausgeführt werden. Diese sind ein leichter Nachbereitungs-Gate (ist der Agent erreichbar und erfüllt Grundlagen der Eingabeaufforderungen?), welche die Evaluierungspipeline in den Lektionen 10 und 16 ergänzen. Siehe [tests/README.md](./tests/README.md) für die Zuordnung Katalog → Lektion → Agent. Lektion 17 läuft lokal mit Foundry Local und hat keinen gehosteten Endpunkt, sie wird durch Ausführen des Notebooks direkt validiert.

## Code-Stil

### Python-Konventionen

- **Python-Version**: 3.12+
- **Code-Stil**: Folgen Sie den Standard-Python PEP 8 Konventionen
- **Notebooks**: Verwenden Sie klare Markdown-Zellen zur Erklärung von Konzepten
- **Imports**: Gruppieren Sie nach Standardbibliothek, Drittanbieter, lokale Importe

### Jupyter Notebook-Konventionen

- Beschreibende Markdown-Zellen vor Code-Zellen einfügen
- Beispielausgaben in Notebooks als Referenz hinzufügen
- Klare Variablennamen verwenden, die zu den Lektionsthemen passen
- Reihenfolge der Notebook-Ausführung linear halten (Zelle 1 → 2 → 3 ...)

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

## Aufbau und Bereitstellung

### Dokumentation erstellen

Dieses Repository verwendet Markdown für die Dokumentation:
- README.md Dateien in jedem Lektionenordner
- Haupt-README.md im Wurzelverzeichnis des Repositories
- Automatisches Übersetzungssystem über GitHub Actions

### CI/CD-Pipeline

Befindet sich in `.github/workflows/`:

1. **co-op-translator.yml** - Automatische Übersetzung in 50+ Sprachen
2. **welcome-issue.yml** - Begrüßt Ersteller neuer Issues
3. **welcome-pr.yml** - Begrüßt neue Pull-Request-Beitragende

### Bereitstellung

Dies ist ein Lern-Repository - kein Bereitstellungsprozess. Nutzer:
1. Forken oder klonen das Repository
2. Führen Notebooks lokal oder in GitHub Codespaces aus
3. Lernen durch Modifizieren und Experimentieren mit Beispielen

## Richtlinien für Pull Requests

### Vor dem Einreichen

1. **Änderungen testen:**
   - Betroffene Notebooks vollständig ausführen
   - Sicherstellen, dass alle Zellen fehlerfrei laufen
   - Überprüfen, dass Ausgaben angemessen sind

2. **Dokumentationsupdates:**
   - README.md aktualisieren, wenn neue Konzepte hinzugefügt werden
   - Kommentare in Notebooks für komplexen Code ergänzen
   - Sicherstellen, dass Markdown-Zellen den Zweck erklären

3. **Dateiänderungen:**
   - Vermeiden Sie das Committen von `.env` Dateien (verwenden Sie `.env.example`)
   - Committen Sie keine `venv/` oder `__pycache__/` Verzeichnisse
   - Behalten Sie Notebook-Ausgaben bei, wenn sie Konzepte demonstrieren
   - Entfernen Sie temporäre Dateien und Backup-Notebooks (`*-backup.ipynb`)

### Format der PR-Titel

Verwenden Sie aussagekräftige Titel:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Erforderliche Prüfungen

- Notebooks sollten fehlerfrei ausführbar sein
- README-Dateien sollten klar und akkurat sein
- Bestehenden Code-Stil im Repository beachten
- Konsistenz mit anderen Lektionen wahren

## Zusätzliche Hinweise

### Häufige Stolperfallen

1. **Python-Versionskonflikt:**
   - Stellen Sie sicher, dass Python 3.12+ verwendet wird
   - Einige Pakete funktionieren mit älteren Versionen nicht
   - Nutzen Sie `python3 -m venv` zur expliziten Angabe der Python-Version

2. **Umgebungsvariablen:**
   - Immer `.env` aus `.env.example` erstellen
   - Committen Sie keine `.env` Datei (liegt in `.gitignore`)
   - Melden Sie sich mit `az login` für eine keyless Entra ID-Authentifizierung an

3. **Paketkonflikte:**
   - Verwenden Sie eine frische virtuelle Umgebung
   - Installation aus `requirements.txt` statt einzelner Pakete
   - Einige Notebooks erfordern zusätzliche Pakete, die in ihren Markdown-Zellen genannt sind

4. **Azure-Dienste:**
   - Azure KI-Dienste erfordern ein aktives Abonnement
   - Einige Funktionen sind regionsspezifisch
   - Stellen Sie sicher, dass Ihr Azure OpenAI Modell-Deployment die Responses API unterstützt

### Lernpfad

Empfohlene Reihenfolge der Lektionen:
1. **00-course-setup** - Start für die Umgebungs-Einrichtung
2. **01-intro-to-ai-agents** - Grundlagen der KI-Agenten verstehen
3. **02-explore-agentic-frameworks** - Verschiedene Frameworks kennenlernen
4. **03-agentic-design-patterns** - Kern-Designmuster
5. Sequential die nummerierten Lektionen fortsetzen

### Framework-Auswahl

Framework basierend auf Ihren Zielen wählen:
- **Alle Lektionen**: Microsoft Agent Framework (MAF) mit `FoundryChatClient`
- **Agenten registrieren sich serverseitig** im Microsoft Foundry Agent Service V2 und sind im Foundry-Portal sichtbar

### Unterstützung erhalten

- Treten Sie dem [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) bei
- Lesen Sie die README-Dateien der Lektionen für spezifische Hinweise
- Siehe die Haupt-[README.md](./README.md) für die Kursübersicht
- Für detaillierte Einrichtungshinweise siehe [Course Setup](./00-course-setup/README.md)

### Beiträge

Dies ist ein offenes Lernprojekt. Beiträge sind willkommen:
- Verbesserung von Code-Beispielen
- Fehlerkorrekturen und Tippfehlerbehebungen
- Hinzufügen erklärender Kommentare
- Vorschläge für neue Lektionsthemen
- Übersetzungen in weitere Sprachen

Siehe [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) für aktuellen Bedarf.

## Projektspezifischer Kontext

### Mehrsprachige Unterstützung

Dieses Repository verwendet ein automatisiertes Übersetzungssystem:
- 50+ unterstützte Sprachen
- Übersetzungen in `/translations/<lang-code>/` Verzeichnissen
- GitHub Actions Workflow verwaltet Übersetzungs-Updates
- Quelldateien sind auf Englisch im Wurzelverzeichnis des Repositories

### Lektionen-Struktur

Jede Lektion folgt einem konsistenten Muster:
1. Video-Vorschaubild mit Link
2. Schriftlicher Lektionstext (README.md)
3. Code-Beispiele in mehreren Frameworks
4. Lernziele und Voraussetzungen
5. Verknüpfte zusätzliche Lernressourcen

### Benennung von Code-Beispielen

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, MAF erweiterte Muster
- `16-python-agent-framework.ipynb` - Lektion 16, produktiver Kundenbetreuungs-Agent
- `17-local-agent-foundry-local.ipynb` - Lektion 17, lokaler Agent mit Foundry Local + Qwen

### Spezielle Verzeichnisse

- `translated_images/` - Lokalisierte Bilder für Übersetzungen
- `images/` - Originalbilder für englische Inhalte
- `.devcontainer/` - VS Code Entwicklungscontainer-Konfiguration
- `.github/` - GitHub Actions Workflows und Vorlagen

### Abhängigkeiten

Wichtige Pakete aus `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent Protokollunterstützung
- `azure-ai-inference`, `azure-ai-projects` - Azure KI-Dienste
- `azure-identity` - Azure-Authentifizierung (AzureCliCredential)
- `azure-search-documents` - Azure AI Search Integration
- `mcp[cli]` - Model Context Protocol Unterstützung

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->