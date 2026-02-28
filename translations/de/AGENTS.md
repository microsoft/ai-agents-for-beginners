# AGENTS.md

## Projektübersicht

Dieses Repository enthält "KI-Agenten für Anfänger" – einen umfassenden Bildungskurs, der alles Notwendige lehrt, um KI-Agenten zu erstellen. Der Kurs besteht aus 15+ Lektionen, die Grundlagen, Designmuster, Frameworks und den produktiven Einsatz von KI-Agenten abdecken.

**Schlüsseltechnologien:**
- Python 3.12+
- Jupyter Notebooks für interaktives Lernen
- KI-Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architektur:**
- Lektionenbasierte Struktur (Verzeichnisse 00-15+)
- Jede Lektion enthält: README-Dokumentation, Codebeispiele (Jupyter-Notebooks) und Bilder
- Mehrsprachige Unterstützung durch automatisiertes Übersetzungssystem
- Ein Python-Notebook pro Lektion mit Microsoft Agent Framework

## Setup-Befehle

### Voraussetzungen
- Python 3.12 oder höher
- Azure-Abonnement (für Azure AI Foundry)
- Azure CLI installiert und authentifiziert (`az login`)

### Ersteinrichtung

1. **Repository klonen oder forken:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ODER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Virtuelle Python-Umgebung erstellen und aktivieren:**
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
   # Bearbeiten Sie die .env-Datei mit Ihren API-Schlüsseln und Endpunkten
   ```

### Erforderliche Umgebungsvariablen

Für **Azure AI Foundry** (erforderlich):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry Projekt-Endpunkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Name der Modellbereitstellung (z.B. gpt-4o)

Für **Azure AI Search** (Lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search-Endpunkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-Schlüssel

Authentifizierung: Führen Sie `az login` vor dem Ausführen der Notebooks aus (nutzt `AzureCliCredential`).

## Entwicklungsworkflow

### Jupyter-Notebooks ausführen

Jede Lektion enthält mehrere Jupyter-Notebooks für verschiedene Frameworks:

1. **Jupyter starten:**
   ```bash
   jupyter notebook
   ```

2. **Zum Lektion-Verzeichnis navigieren** (z.B. `01-intro-to-ai-agents/code_samples/`)

3. **Notebooks öffnen und ausführen:**
   - `*-python-agent-framework.ipynb` - Nutzung des Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Nutzung des Microsoft Agent Framework (.NET)

### Arbeiten mit Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Erfordert Azure-Abonnement
- Verwendet `AzureAIProjectAgentProvider` für Agent Service V2 (Agenten sichtbar im Foundry-Portal)
- Produktionsreif mit integrierter Überwachbarkeit
- Dateimuster: `*-python-agent-framework.ipynb`

## Testanweisungen

Dies ist ein Bildungskurs mit Beispielcode, kein Produktionscode mit automatisierten Tests. Um Ihre Einrichtung und Änderungen zu prüfen:

### Manueller Test

1. **Python-Umgebung testen:**
   ```bash
   python --version  # Sollte 3.12+ sein
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Ausführung von Notebooks testen:**
   ```bash
   # Notebook in Skript konvertieren und ausführen (Tests für Importe)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Umgebungsvariablen überprüfen:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Einzelne Notebooks ausführen

Öffnen Sie die Notebooks in Jupyter und führen Sie die Zellen nacheinander aus. Jedes Notebook ist eigenständig und enthält:
- Import-Anweisungen
- Konfigurationsladen
- Beispielimplementierungen von Agenten
- Erwartete Ausgaben in Markdown-Zellen

## Code-Stil

### Python-Konventionen

- **Python-Version**: 3.12+
- **Code-Stil**: Befolgen der Standard-Python-PEP-8-Konventionen
- **Notebooks**: Klare Markdown-Zellen zur Erklärung von Konzepten verwenden
- **Imports**: Nach Standardbibliothek, Drittanbieter und lokal gruppieren

### Jupyter-Notebook-Konventionen

- Beschreibende Markdown-Zellen vor Codezellen einfügen
- Ausgabebeispiele in den Notebooks zur Referenz hinzufügen
- Klare Variablennamen verwenden, die zu den Lektionsthemen passen
- Reihenfolge der Notebook-Ausführung linear halten (Zelle 1 → 2 → 3...)

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

## Build und Deployment

### Dokumentation erstellen

Dieses Repository nutzt Markdown für Dokumentation:
- README.md-Dateien in jedem Lektion-Ordner
- Haupt-README.md im Repository-Stamm
- Automatisches Übersetzungssystem über GitHub Actions

### CI/CD-Pipeline

Im Verzeichnis `.github/workflows/`:

1. **co-op-translator.yml** - Automatische Übersetzung in 50+ Sprachen
2. **welcome-issue.yml** - Begrüßung neuer Issue-Ersteller
3. **welcome-pr.yml** - Begrüßung neuer Pull-Request-Beiträger

### Deployment

Dies ist ein Bildungsrepository – kein Deployment-Prozess. Nutzer:
1. Forken oder klonen das Repository
2. Führen Notebooks lokal oder in GitHub Codespaces aus
3. Lernen durch Modifikation und Experimentieren mit Beispielen

## Pull-Request-Richtlinien

### Vor dem Einreichen

1. **Änderungen testen:**
   - Betroffene Notebooks komplett ausführen
   - Sicherstellen, dass alle Zellen fehlerfrei laufen
   - Überprüfen, ob Ausgaben angemessen sind

2. **Dokumentation aktualisieren:**
   - README.md aktualisieren, wenn neue Konzepte hinzugefügt werden
   - Kommentare in Notebooks für komplexen Code hinzufügen
   - Sicherstellen, dass Markdown-Zellen den Zweck erklären

3. **Dateiänderungen:**
   - Keine `.env`-Dateien committen (verwenden Sie `.env.example`)
   - Keine `venv/` oder `__pycache__/`-Verzeichnisse committen
   - Notebook-Ausgaben beibehalten, wenn sie Konzepte demonstrieren
   - Temporäre Dateien und Backup-Notebooks (`*-backup.ipynb`) entfernen

### Format des PR-Titels

Verwenden Sie beschreibende Titel:
- `[Lesson-XX] Neues Beispiel für <Konzept>`
- `[Fix] Tippfehler in lesson-XX README korrigieren`
- `[Update] Codebeispiel in lesson-XX verbessern`
- `[Docs] Setup-Anweisungen aktualisieren`

### Erforderliche Checks

- Notebooks müssen fehlerfrei ausführbar sein
- README-Dateien sollten klar und korrekt sein
- Bestehende Code-Muster im Repository befolgen
- Konsistenz mit anderen Lektionen wahren

## Zusätzliche Hinweise

### Häufige Stolperfallen

1. **Python-Version nicht passend:**
   - Verwenden Sie Python 3.12+
   - Manche Pakete funktionieren nicht mit älteren Versionen
   - Nutzen Sie `python3 -m venv` für explizite Python-Version

2. **Umgebungsvariablen:**
   - `.env` immer aus `.env.example` erstellen
   - `.env` nicht committen (ist in `.gitignore`)
   - GitHub-Token benötigt passende Berechtigungen

3. **Paketkonflikte:**
   - Frische virtuelle Umgebung verwenden
   - Installation über `requirements.txt` statt einzelner Pakete
   - Manche Notebooks benötigen zusätzliche Pakete, die in Markdown-Zellen erwähnt sind

4. **Azure-Dienste:**
   - Azure AI Dienste erfordern aktives Abonnement
   - Manche Features sind regionsspezifisch
   - Kostenlose Kontingente gelten für GitHub-Modelle

### Lernpfad

Empfohlene Reihenfolge der Lektionen:
1. **00-course-setup** - Hier mit der Umgebungseinrichtung starten
2. **01-intro-to-ai-agents** - Grundlagen der KI-Agenten verstehen
3. **02-explore-agentic-frameworks** - Verschiedene Frameworks kennenlernen
4. **03-agentic-design-patterns** - Kern-Designmuster
5. Folgen Sie den nummerierten Lektionen der Reihenfolge nach

### Framework-Auswahl

Wählen Sie das Framework basierend auf Ihren Zielen:
- **Alle Lektionen**: Microsoft Agent Framework (MAF) mit `AzureAIProjectAgentProvider`
- **Agenten sind serverseitig registriert** im Azure AI Foundry Agent Service V2 und im Foundry-Portal sichtbar

### Hilfe erhalten

- Treten Sie dem [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) bei
- Lesen Sie die README-Dateien der Lektionen für spezifische Anleitungen
- Prüfen Sie die Haupt- [README.md](./README.md) für Kursübersicht
- Siehe [Course Setup](./00-course-setup/README.md) für detaillierte Einrichtungshinweise

### Mitwirken

Dies ist ein offenes Bildungsprojekt. Beiträge willkommen:
- Codebeispiele verbessern
- Tippfehler oder Fehler korrigieren
- Klarstellende Kommentare hinzufügen
- Neue Lektionsthemen vorschlagen
- In weitere Sprachen übersetzen

Siehe [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) für aktuelle Bedürfnisse.

## Projektspezifischer Kontext

### Mehrsprachige Unterstützung

Dieses Repository nutzt ein automatisches Übersetzungssystem:
- 50+ unterstützte Sprachen
- Übersetzungen in `/translations/<lang-code>/` Verzeichnissen
- GitHub Actions steuert die Übersetzungsupdates
- Quelldateien sind auf Englisch im Repository-Stamm

### Lektionenstruktur

Jede Lektion folgt einem konsistenten Muster:
1. Video-Thumbnail mit Link
2. Schriftlicher Lektionstext (README.md)
3. Codebeispiele in mehreren Frameworks
4. Lernziele und Voraussetzungen
5. Verlinkte zusätzliche Lernressourcen

### Benennung der Codebeispiele

Format: `<Lektionsnummer>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, MAF fortgeschrittene Muster

### Spezielle Verzeichnisse

- `translated_images/` - Lokalisierte Bilder für Übersetzungen
- `images/` - Originalbilder für englische Inhalte
- `.devcontainer/` - VS Code Entwicklungscontainer-Konfiguration
- `.github/` - GitHub Actions Workflows und Templates

### Abhängigkeiten

Wichtige Pakete aus `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent-Protokoll-Unterstützung
- `azure-ai-inference`, `azure-ai-projects` - Azure AI Dienste
- `azure-identity` - Azure Authentifizierung (AzureCliCredential)
- `azure-search-documents` - Azure AI Search Integration
- `mcp[cli]` - Model Context Protocol Unterstützung

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->