# AGENTS.md

## Projektübersicht

Dieses Repository enthält "AI Agents for Beginners" – einen umfassenden Bildungskurs, der alles vermittelt, was man zum Erstellen von KI-Agenten benötigt. Der Kurs besteht aus über 15 Lektionen, die Grundlagen, Designmuster, Frameworks und die Bereitstellung von KI-Agenten in der Produktion abdecken.

**Wichtige Technologien:**
- Python 3.12+
- Jupyter Notebooks für interaktives Lernen
- KI-Frameworks: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI-Dienste: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (kostenlose Stufe verfügbar)

**Architektur:**
- Lektionenbasierte Struktur (Verzeichnisse 00-15+)
- Jede Lektion enthält: README-Dokumentation, Codebeispiele (Jupyter Notebooks) und Bilder
- Mehrsprachige Unterstützung durch ein automatisiertes Übersetzungssystem
- Mehrere Framework-Optionen pro Lektion (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Setup-Befehle

### Voraussetzungen
- Python 3.12 oder höher
- GitHub-Konto (für GitHub Models – kostenlose Stufe)
- Azure-Abonnement (optional, für Azure AI-Dienste)

### Ersteinrichtung

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

4. **Umgebungsvariablen einrichten:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### Erforderliche Umgebungsvariablen

Für **GitHub Models (kostenlos)**:
- `GITHUB_TOKEN` – Persönlicher Zugriffstoken von GitHub

Für **Azure AI-Dienste** (optional):
- `PROJECT_ENDPOINT` – Azure AI Foundry-Projekt-Endpunkt
- `AZURE_OPENAI_API_KEY` – Azure OpenAI API-Schlüssel
- `AZURE_OPENAI_ENDPOINT` – Azure OpenAI-Endpunkt-URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` – Bereitstellungsname für Chat-Modell
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` – Bereitstellungsname für Embeddings
- Weitere Azure-Konfigurationen wie in `.env.example` gezeigt

## Entwicklungsworkflow

### Jupyter Notebooks ausführen

Jede Lektion enthält mehrere Jupyter Notebooks für verschiedene Frameworks:

1. **Jupyter starten:**
   ```bash
   jupyter notebook
   ```

2. **Zu einem Lektionen-Verzeichnis navigieren** (z. B. `01-intro-to-ai-agents/code_samples/`)

3. **Notebooks öffnen und ausführen:**
   - `*-semantic-kernel.ipynb` – Verwendung des Semantic Kernel Frameworks
   - `*-autogen.ipynb` – Verwendung des AutoGen Frameworks
   - `*-python-agent-framework.ipynb` – Verwendung des Microsoft Agent Frameworks (Python)
   - `*-dotnet-agent-framework.ipynb` – Verwendung des Microsoft Agent Frameworks (.NET)
   - `*-azureaiagent.ipynb` – Verwendung des Azure AI Agent Service

### Arbeiten mit verschiedenen Frameworks

**Semantic Kernel + GitHub Models:**
- Kostenlose Stufe mit GitHub-Konto verfügbar
- Gut für Lernen und Experimente
- Dateimuster: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Kostenlose Stufe mit GitHub-Konto verfügbar
- Fähigkeiten zur Multi-Agenten-Orchestrierung
- Dateimuster: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Neuestes Framework von Microsoft
- Verfügbar in Python und .NET
- Dateimuster: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Erfordert Azure-Abonnement
- Produktionsreife Funktionen
- Dateimuster: `*-azureaiagent.ipynb`

## Testanweisungen

Dies ist ein Bildungs-Repository mit Beispielcode und keine Produktionssoftware mit automatisierten Tests. Um Ihre Einrichtung und Änderungen zu überprüfen:

### Manuelles Testen

1. **Python-Umgebung testen:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Notebook-Ausführung testen:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Umgebungsvariablen überprüfen:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### Einzelne Notebooks ausführen

Notebooks in Jupyter öffnen und Zellen nacheinander ausführen. Jedes Notebook ist eigenständig und enthält:
- Importanweisungen
- Konfigurationsladevorgänge
- Beispielimplementierungen von Agenten
- Erwartete Ausgaben in Markdown-Zellen

## Code-Stil

### Python-Konventionen

- **Python-Version**: 3.12+
- **Code-Stil**: Standard-Python-PEP-8-Konventionen folgen
- **Notebooks**: Klare Markdown-Zellen zur Erklärung von Konzepten verwenden
- **Imports**: Gruppierung nach Standardbibliothek, Drittanbieter, lokale Imports

### Jupyter Notebook-Konventionen

- Beschreibende Markdown-Zellen vor Code-Zellen einfügen
- Ausgabe-Beispiele in Notebooks als Referenz hinzufügen
- Klare Variablennamen verwenden, die den Lektionen-Konzepten entsprechen
- Reihenfolge der Notebook-Ausführung linear halten (Zelle 1 → 2 → 3...)

### Dateiorganisation

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## Build und Bereitstellung

### Dokumentation erstellen

Dieses Repository verwendet Markdown für die Dokumentation:
- README.md-Dateien in jedem Lektionen-Ordner
- Haupt-README.md im Repository-Stammverzeichnis
- Automatisiertes Übersetzungssystem über GitHub Actions

### CI/CD-Pipeline

Zu finden in `.github/workflows/`:

1. **co-op-translator.yml** – Automatische Übersetzung in über 50 Sprachen
2. **welcome-issue.yml** – Begrüßung neuer Issue-Ersteller
3. **welcome-pr.yml** – Begrüßung neuer Pull-Request-Beitragender

### Bereitstellung

Dies ist ein Bildungs-Repository – kein Bereitstellungsprozess. Benutzer:
1. Forken oder klonen das Repository
2. Führen Notebooks lokal oder in GitHub Codespaces aus
3. Lernen durch Modifikation und Experimentieren mit Beispielen

## Richtlinien für Pull Requests

### Vor dem Einreichen

1. **Änderungen testen:**
   - Betroffene Notebooks vollständig ausführen
   - Sicherstellen, dass alle Zellen fehlerfrei ausgeführt werden
   - Überprüfen, ob die Ausgaben angemessen sind

2. **Dokumentationsaktualisierungen:**
   - README.md aktualisieren, wenn neue Konzepte hinzugefügt werden
   - Kommentare in Notebooks für komplexen Code hinzufügen
   - Sicherstellen, dass Markdown-Zellen den Zweck erklären

3. **Dateiänderungen:**
   - `.env`-Dateien nicht committen (verwenden Sie `.env.example`)
   - `venv/` oder `__pycache__/`-Verzeichnisse nicht committen
   - Notebook-Ausgaben beibehalten, wenn sie Konzepte demonstrieren
   - Temporäre Dateien und Backup-Notebooks (`*-backup.ipynb`) entfernen

### PR-Titel-Format

Verwenden Sie beschreibende Titel:
- `[Lesson-XX] Neues Beispiel für <Konzept> hinzufügen`
- `[Fix] Rechtschreibfehler in lesson-XX README korrigieren`
- `[Update] Codebeispiel in lesson-XX verbessern`
- `[Docs] Setup-Anweisungen aktualisieren`

### Erforderliche Prüfungen

- Notebooks sollten fehlerfrei ausgeführt werden
- README-Dateien sollten klar und korrekt sein
- Bestehende Code-Muster im Repository befolgen
- Konsistenz mit anderen Lektionen wahren

## Zusätzliche Hinweise

### Häufige Stolperfallen

1. **Python-Version nicht kompatibel:**
   - Python 3.12+ verwenden
   - Einige Pakete funktionieren möglicherweise nicht mit älteren Versionen
   - `python3 -m venv` verwenden, um die Python-Version explizit anzugeben

2. **Umgebungsvariablen:**
   - Immer `.env` aus `.env.example` erstellen
   - `.env`-Datei nicht committen (ist in `.gitignore`)
   - GitHub-Token benötigt entsprechende Berechtigungen

3. **Paketkonflikte:**
   - Frische virtuelle Umgebung verwenden
   - Installation aus `requirements.txt` statt einzelner Pakete
   - Einige Notebooks erfordern zusätzliche Pakete, die in ihren Markdown-Zellen erwähnt werden

4. **Azure-Dienste:**
   - Azure AI-Dienste erfordern ein aktives Abonnement
   - Einige Funktionen sind regionsspezifisch
   - Einschränkungen der kostenlosen Stufe gelten für GitHub Models

### Lernpfad

Empfohlene Reihenfolge der Lektionen:
1. **00-course-setup** – Hier beginnen für die Einrichtung der Umgebung
2. **01-intro-to-ai-agents** – Grundlagen von KI-Agenten verstehen
3. **02-explore-agentic-frameworks** – Verschiedene Frameworks kennenlernen
4. **03-agentic-design-patterns** – Wichtige Designmuster
5. Fortsetzung durch nummerierte Lektionen in Reihenfolge

### Framework-Auswahl

Framework basierend auf Ihren Zielen wählen:
- **Lernen/Prototyping**: Semantic Kernel + GitHub Models (kostenlos)
- **Multi-Agenten-Systeme**: AutoGen
- **Neueste Funktionen**: Microsoft Agent Framework (MAF)
- **Produktionsbereitstellung**: Azure AI Agent Service

### Hilfe erhalten

- Treten Sie der [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord) bei
- Überprüfen Sie die README-Dateien der Lektionen für spezifische Anleitungen
- Sehen Sie sich die Haupt-[README.md](./README.md) für die Kursübersicht an
- Konsultieren Sie [Course Setup](./00-course-setup/README.md) für detaillierte Einrichtungshinweise

### Mitwirken

Dies ist ein offenes Bildungsprojekt. Beiträge sind willkommen:
- Codebeispiele verbessern
- Rechtschreibfehler oder Fehler beheben
- Klärende Kommentare hinzufügen
- Neue Lektionsthemen vorschlagen
- Übersetzungen in zusätzliche Sprachen hinzufügen

Siehe [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) für aktuelle Bedürfnisse.

## Projektspezifischer Kontext

### Mehrsprachige Unterstützung

Dieses Repository verwendet ein automatisiertes Übersetzungssystem:
- Unterstützung für über 50 Sprachen
- Übersetzungen in `/translations/<lang-code>/`-Verzeichnissen
- GitHub Actions-Workflow verwaltet Übersetzungsaktualisierungen
- Quelldateien sind auf Englisch im Repository-Stammverzeichnis

### Lektionenstruktur

Jede Lektion folgt einem konsistenten Muster:
1. Video-Thumbnail mit Link
2. Schriftlicher Lektioneninhalt (README.md)
3. Codebeispiele in mehreren Frameworks
4. Lernziele und Voraussetzungen
5. Zusätzliche Lernressourcen verlinkt

### Namensgebung von Codebeispielen

Format: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` – Lektion 4, Semantic Kernel
- `07-autogen.ipynb` – Lektion 7, AutoGen
- `14-python-agent-framework.ipynb` – Lektion 14, MAF Python
- `14-dotnet-agent-framework.ipynb` – Lektion 14, MAF .NET

### Spezielle Verzeichnisse

- `translated_images/` – Lokalisierte Bilder für Übersetzungen
- `images/` – Originalbilder für englische Inhalte
- `.devcontainer/` – VS Code Entwicklungscontainer-Konfiguration
- `.github/` – GitHub Actions Workflows und Vorlagen

### Abhängigkeiten

Wichtige Pakete aus `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` – AutoGen Framework
- `semantic-kernel` – Semantic Kernel Framework
- `agent-framework` – Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` – Azure AI-Dienste
- `azure-search-documents` – Azure AI Search-Integration
- `chromadb` – Vektordatenbank für RAG-Beispiele
- `chainlit` – Chat-UI-Framework
- `browser_use` – Browser-Automatisierung für Agenten
- `mcp[cli]` – Unterstützung für Model Context Protocol
- `mem0ai` – Speicherverwaltung für Agenten

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.