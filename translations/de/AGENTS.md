# AGENTS.md

## Projektübersicht

Dieses Repository enthält "KI-Agenten für Anfänger" – einen umfassenden Bildungskurs, der alles Notwendige vermittelt, um KI-Agenten zu entwickeln. Der Kurs besteht aus mehr als 15 Lektionen, die Grundlagen, Designmuster, Frameworks und Produktionseinsatz von KI-Agenten abdecken.

**Schlüsseltechnologien:**
- Python 3.12+
- Jupyter Notebooks für interaktives Lernen
- KI-Frameworks: Microsoft Agent Framework (MAF)
- Azure AI-Dienste: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architektur:**
- Lektionenbasierte Struktur (Verzeichnisse 00-15+)
- Jede Lektion enthält: README-Dokumentation, Codebeispiele (Jupyter-Notebooks) und Bilder
- Mehrsprachige Unterstützung über automatisiertes Übersetzungssystem
- Ein Python-Notebook pro Lektion, das das Microsoft Agent Framework verwendet

## Setup-Befehle

### Voraussetzungen
- Python 3.12 oder höher
- Azure-Abonnement (für Azure AI Foundry)
- Azure CLI installiert und authentifiziert (`az login`)

### Erste Einrichtung

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
   # Bearbeiten Sie die .env mit Ihren API-Schlüsseln und Endpunkten
   ```

### Erforderliche Umgebungsvariablen

Für **Azure AI Foundry** (Erforderlich):
- `AZURE_AI_PROJECT_ENDPOINT` – Azure AI Foundry Projekt-Endpunkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` – Name der Modellbereitstellung (z.B. gpt-4o)

Für **Azure AI Search** (Lektion 05 – RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` – Azure AI Search Endpunkt
- `AZURE_SEARCH_API_KEY` – Azure AI Search API-Schlüssel

Authentifizierung: Führen Sie `az login` vor Ausführung der Notebooks aus (verwendet `AzureCliCredential`).

## Entwicklungsworkflow

### Ausführen von Jupyter-Notebooks

Jede Lektion enthält mehrere Jupyter-Notebooks für verschiedene Frameworks:

1. **Jupyter starten:**
   ```bash
   jupyter notebook
   ```

2. **Zum Lektionenverzeichnis navigieren** (z.B. `01-intro-to-ai-agents/code_samples/`)

3. **Notebooks öffnen und ausführen:**
   - `*-python-agent-framework.ipynb` – Mit Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` – Mit Microsoft Agent Framework (.NET)

### Arbeiten mit Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Benötigt Azure-Abonnement
- Verwendet `AzureAIProjectAgentProvider` für Agent Service V2 (Agenten sind im Foundry-Portal sichtbar)
- Produktionsbereit mit integrierter Beobachtbarkeit
- Dateimuster: `*-python-agent-framework.ipynb`

## Testanweisungen

Dies ist ein Bildungsrepository mit Beispielcode und nicht mit produktionstauglichem Code und automatisierten Tests. Um Ihre Einrichtung und Änderungen zu überprüfen:

### Manuelles Testen

1. **Python-Umgebung testen:**
   ```bash
   python --version  # Sollte 3.12+ sein
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Ausführung des Notebooks testen:**
   ```bash
   # Notebook in Skript umwandeln und ausführen (testet Importe)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Umgebungsvariablen überprüfen:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Einzelne Notebooks ausführen

Öffnen Sie Notebooks in Jupyter und führen Sie die Zellen nacheinander aus. Jedes Notebook ist eigenständig und enthält:
- Importanweisungen
- Konfigurationsladen
- Beispielagentimplementierungen
- Erwartete Ausgaben in Markdown-Zellen

## Code-Stil

### Python-Konventionen

- **Python-Version**: 3.12+
- **Code-Stil**: Folgen Sie den Standard-Python-PEP-8-Konventionen
- **Notebooks**: Verwenden Sie klare Markdown-Zellen zur Erklärung von Konzepten
- **Imports**: Gruppieren nach Standardbibliothek, Drittanbieter, lokale Importe

### Jupyter-Notebook-Konventionen

- Fügen Sie beschreibende Markdown-Zellen vor Codezellen ein
- Fügen Sie Ausgabe-Beispiele in Notebooks als Referenz hinzu
- Verwenden Sie klare Variablennamen, die den Lektionsthemen entsprechen
- Halten Sie die Ausführungsreihenfolge der Notebooks linear (Zelle 1 → 2 → 3...)

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

Dieses Repository verwendet Markdown für die Dokumentation:
- README.md-Dateien in jedem Lektionenordner
- Haupt-README.md im Repository-Stamm
- Automatisches Übersetzungssystem über GitHub Actions

### CI/CD-Pipeline

Lokalisiert in `.github/workflows/`:

1. **co-op-translator.yml** – Automatische Übersetzung in 50+ Sprachen
2. **welcome-issue.yml** – Begrüßt neue Issue-Ersteller
3. **welcome-pr.yml** – Begrüßt neue Pull-Request-Beiträger

### Deployment

Dies ist ein Bildungsrepository – kein Deployment-Prozess. Nutzer:
1. Forken oder klonen das Repository
2. Führen Notebooks lokal oder in GitHub Codespaces aus
3. Lernen durch Modifikation und Experimente mit Beispielen

## Richtlinien für Pull Requests

### Vor dem Einreichen

1. **Testen Sie Ihre Änderungen:**
   - Führen Sie die betroffenen Notebooks vollständig aus
   - Stellen Sie sicher, dass alle Zellen fehlerfrei ausführbar sind
   - Prüfen Sie, ob Ausgaben angemessen sind

2. **Dokumentationsupdates:**
   - README.md aktualisieren, wenn neue Konzepte hinzugefügt werden
   - Kommentare in Notebooks bei komplexem Code hinzufügen
   - Sicherstellen, dass Markdown-Zellen den Zweck erklären

3. **Dateiänderungen:**
   - Keine `.env`-Dateien committen (verwenden Sie `.env.example`)
   - Keine `venv/` oder `__pycache__/` Verzeichnisse committen
   - Notebook-Ausgaben beibehalten, wenn diese Konzepte demonstrieren
   - Temporäre Dateien und Backup-Notebooks (`*-backup.ipynb`) entfernen

### PR-Titel-Format

Verwenden Sie beschreibende Titel:
- `[Lesson-XX] Neues Beispiel für <Konzept> hinzufügen`
- `[Fix] Rechtschreibfehler in lesson-XX README korrigieren`
- `[Update] Codebeispiel in lesson-XX verbessern`
- `[Docs] Setup-Anleitung aktualisieren`

### Erforderliche Prüfungen

- Notebooks sollten fehlerfrei ausführbar sein
- README-Dateien sollten klar und präzise sein
- Bestehende Code-Muster im Repository einhalten
- Konsistenz mit anderen Lektionen bewahren

## Zusätzliche Hinweise

### Häufige Fallen

1. **Python-Version stimmt nicht überein:**
   - Stellen Sie sicher, dass Python 3.12+ verwendet wird
   - Einige Pakete funktionieren nicht mit älteren Versionen
   - Verwenden Sie `python3 -m venv`, um die Python-Version explizit anzugeben

2. **Umgebungsvariablen:**
   - Erstellen Sie immer `.env` aus `.env.example`
   - Committen Sie keine `.env`-Datei (sie ist in `.gitignore`)
   - GitHub-Token benötigt passende Berechtigungen

3. **Paketkonflikte:**
   - Verwenden Sie eine frische virtuelle Umgebung
   - Installieren Sie aus `requirements.txt` und nicht einzelne Pakete
   - Einige Notebooks benötigen möglicherweise zusätzliche Pakete, die in Markdown-Zellen angegeben sind

4. **Azure-Dienste:**
   - Azure AI-Dienste benötigen ein aktives Abonnement
   - Einige Features sind regionsspezifisch
   - Für GitHub-Modelle gelten Beschränkungen der kostenlosen Stufe

### Lernpfad

Empfohlene Fortschreitung durch die Lektionen:
1. **00-course-setup** – Hier starten für Umgebungs-Setup
2. **01-intro-to-ai-agents** – Grundlagen von KI-Agenten verstehen
3. **02-explore-agentic-frameworks** – Verschiedene Frameworks kennenlernen
4. **03-agentic-design-patterns** – Wichtige Designmuster
5. Fortschreiten durch nummerierte Lektionen der Reihe nach

### Framework-Auswahl

Wählen Sie Framework basierend auf Ihren Zielen:
- **Alle Lektionen**: Microsoft Agent Framework (MAF) mit `AzureAIProjectAgentProvider`
- **Agenten melden sich serverseitig an** im Azure AI Foundry Agent Service V2 und sind im Foundry-Portal sichtbar

### Hilfe erhalten

- Tritt dem [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) bei
- Siehe Lektionen-README für spezifische Anweisungen
- Überprüfe das Haupt-[README.md](./README.md) für Kursübersicht
- Siehe [Course Setup](./00-course-setup/README.md) für detaillierte Einrichtungshinweise

### Beiträge

Dies ist ein offenes Bildungsprojekt. Beiträge sind willkommen:
- Codebeispiele verbessern
- Rechtschreib- oder Fehlerkorrekturen
- Klärende Kommentare hinzufügen
- Neue Lektionsthemen vorschlagen
- Übersetzungen in weitere Sprachen erstellen

Siehe [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) für aktuellen Bedarf.

## Projektspezifischer Kontext

### Mehrsprachige Unterstützung

Dieses Repository benutzt ein automatisiertes Übersetzungssystem:
- 50+ unterstützte Sprachen
- Übersetzungen in `/translations/<lang-code>/` Verzeichnissen
- GitHub Actions-Workflow verwaltet Übersetzungsupdates
- Quelldateien sind auf Englisch im Repository-Stamm

### Lektionenstruktur

Jede Lektion folgt einem konsistenten Muster:
1. Video-Thumbnail mit Link
2. Schriftlicher Lektionstext (README.md)
3. Codebeispiele in mehreren Frameworks
4. Lernziele und Voraussetzungen
5. Zusätzliche Lernressourcen verlinkt

### Benennung von Codebeispielen

Format: `<Lektionsnummer>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` – Lektion 1, MAF Python
- `14-sequential.ipynb` – Lektion 14, MAF fortgeschrittene Muster

### Spezielle Verzeichnisse

- `translated_images/` – Lokalisierte Bilder für Übersetzungen
- `images/` – Originalbilder für englische Inhalte
- `.devcontainer/` – VS Code Entwicklungskontainer-Konfiguration
- `.github/` – GitHub Actions Workflows und Templates

### Abhängigkeiten

Schlüsselpakete aus `requirements.txt`:
- `agent-framework` – Microsoft Agent Framework
- `a2a-sdk` – Agent-to-Agent-Protokoll-Unterstützung
- `azure-ai-inference`, `azure-ai-projects` – Azure AI-Dienste
- `azure-identity` – Azure-Authentifizierung (AzureCliCredential)
- `azure-search-documents` – Azure AI Search Integration
- `mcp[cli]` – Model Context Protocol-Unterstützung

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->