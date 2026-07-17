# AGENTS.md

## Projektübersicht

Dieses Repository enthält "KI-Agenten für Einsteiger" - einen umfassenden Bildungskurs, der alles vermittelt, was zum Erstellen von KI-Agenten erforderlich ist. Der Kurs besteht aus 18 Lektionen (nummeriert von 00-18), die Grundlagen, Designmuster, Frameworks, Produktionsbereitstellung, lokale/On-Device-Agenten und Sicherheit von KI-Agenten abdecken.

**Schlüsseltechnologien:**
- Python 3.12+
- Jupyter Notebooks für interaktives Lernen
- KI-Frameworks: Microsoft Agent Framework (MAF)
- Azure AI-Dienste: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektur:**
- Lektionenbasierte Struktur (Verzeichnisse 00-15+)
- Jede Lektion enthält: README-Dokumentation, Codebeispiele (Jupyter Notebooks) und Bilder
- Mehrsprachige Unterstützung über automatisches Übersetzungssystem
- Pro Lektion ein Python-Notebook mit dem Microsoft Agent Framework

## Einrichtungskommandos

### Voraussetzungen
- Python 3.12 oder höher
- Azure-Abonnement (für Microsoft Foundry)
- Azure CLI installiert und authentifiziert (`az login`)

### Erste Einrichtung

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
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry Projekt-Endpunkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modellbereitstellungsname (z. B. gpt-4.1-mini)

Für **Azure AI Search** (Lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search Endpunkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-Schlüssel

Authentifizierung: Führen Sie `az login` vor dem Ausführen der Notebooks aus (verwendet `AzureCliCredential`).

## Entwicklungsablauf

### Ausführen von Jupyter Notebooks

Jede Lektion enthält mehrere Jupyter Notebooks für verschiedene Frameworks:

1. **Jupyter starten:**
   ```bash
   jupyter notebook
   ```

2. **In ein Lektionsverzeichnis wechseln** (z. B. `01-intro-to-ai-agents/code_samples/`)

3. **Notebooks öffnen und ausführen:**
   - `*-python-agent-framework.ipynb` - Nutzung des Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Nutzung des Microsoft Agent Framework (.NET)

### Arbeiten mit dem Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Erfordert Azure-Abonnement
- Verwendet `FoundryChatClient` für Agent Service V2 (Agenten im Foundry-Portal sichtbar)
- Produktionsreif mit integrierter Beobachtbarkeit
- Dateimuster: `*-python-agent-framework.ipynb`

## Testanweisungen

Dies ist ein Bildungrepository mit Beispielcode und keinen produktionsreifen automatisierten Tests. Um Ihre Einrichtung und Änderungen zu überprüfen:

### Manueller Test

1. **Python-Umgebung testen:**
   ```bash
   python --version  # Sollte 3.12+ sein
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Notebook-Ausführung testen:**
   ```bash
   # Notebook in Skript umwandeln und ausführen (Tests Importe)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Umgebungsvariablen überprüfen:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Einzelne Notebooks ausführen

Öffnen Sie Notebooks in Jupyter und führen Sie die Zellen nacheinander aus. Jedes Notebook ist eigenständig und enthält:
- Import-Anweisungen
- Konfigurationsladen
- Beispielimplementierungen von Agenten
- Erwartete Ausgaben in Markdown-Zellen

### Smoke-Tests für bereitgestellte Agenten

Für Lektionen, in denen ein Agent als Microsoft Foundry gehosteter Agent bereitgestellt wird (01, 04, 05, 16), liefert das Repo Smoke-Test-Kataloge unter `tests/`, die vom Workflow `.github/workflows/smoke-test.yml` über die [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)-Action ausgeführt werden. Diese sind ein leichter Post-Deploy-Gate (ist der Agent erreichbar und folgt er grundlegenden Prompt-Erwartungen?), ergänzen die Evaluierungspipeline in Lektionen 10 und 16. Siehe [tests/README.md](./tests/README.md) für die Zuordnung Katalog-Lektion-Agent. Lektion 17 läuft lokal mit Foundry Local und hat keinen gehosteten Endpunkt, daher wird sie durch direkte Ausführung ihres Notebooks validiert.

## Code-Stil

### Python-Konventionen

- **Python-Version**: 3.12+
- **Code-Stil**: Standard-Python PEP 8-Konventionen folgen
- **Notebooks**: Klare Markdown-Zellen zur Konzept-Erklärung verwenden
- **Imports**: Nach Standardbibliothek, Drittanbieter, lokalen Imports gruppieren

### Jupyter Notebook-Konventionen

- Beschreibende Markdown-Zellen vor Codezellen einfügen
- Ausgabe-Beispiele in Notebooks als Referenz hinzufügen
- Klare Variablennamen verwenden, die zu den Lektionsthemen passen
- Die Ausführungsreihenfolge der Notebooks linear halten (Zelle 1 → 2 → 3 ...)

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

Dieses Repository verwendet Markdown für Dokumentation:
- README.md Dateien in jedem Lektionordner
- Haupt-README.md im Repository-Stamm
- Automatisiertes Übersetzungssystem via GitHub Actions

### CI/CD-Pipeline

Befindet sich in `.github/workflows/`:

1. **co-op-translator.yml** - Automatische Übersetzung in 50+ Sprachen
2. **welcome-issue.yml** - Begrüßt neue Issue-Ersteller
3. **welcome-pr.yml** - Begrüßt neue Pull-Request-Beiträge

### Deployment

Dies ist ein Bildungsrepository - kein Bereitstellungsprozess. Nutzer:
1. Forken oder klonen das Repository
2. Führen Notebooks lokal oder in GitHub Codespaces aus
3. Lernen durch Modifikation und Experimentieren mit Beispielen

## Pull-Request-Richtlinien

### Vor dem Einreichen

1. **Testen Sie Ihre Änderungen:**
   - Ausführung der betroffenen Notebooks komplett durchführen
   - Sicherstellen, dass alle Zellen ohne Fehler laufen
   - Prüfen, ob Ausgaben passend sind

2. **Dokumentationsaktualisierungen:**
   - README.md bei neuen Konzepten aktualisieren
   - Kommentare in Notebooks bei komplexem Code hinzufügen
   - Sicherstellen, dass Markdown-Zellen den Zweck erläutern

3. **Dateiänderungen:**
   - `.env`-Dateien nicht committen (stattdessen `.env.example` verwenden)
   - Keine `venv/` oder `__pycache__/` Verzeichnisse committen
   - Notebook-Ausgaben beibehalten, wenn sie Konzepte demonstrieren
   - Temporäre Dateien und Backup-Notebooks (`*-backup.ipynb`) entfernen

### PR-Titelformat

Verwenden Sie beschreibende Titel:
- `[Lesson-XX] Neues Beispiel für <Konzept> hinzufügen`
- `[Fix] Tippfehler in Lesson-XX README korrigieren`
- `[Update] Codebeispiel in Lesson-XX verbessern`
- `[Docs] Setup-Anweisungen aktualisieren`

### Erforderliche Prüfungen

- Notebooks sollten ohne Fehler ausführbar sein
- README-Dateien sollten klar und korrekt sein
- Bestehende Code-Muster im Repository befolgen
- Konsistenz mit anderen Lektionen gewährleisten

## Zusätzliche Hinweise

### Häufige Fallstricke

1. **Python-Versionsinkompatibilität:**
   - Sicherstellen, dass Python 3.12+ verwendet wird
   - Manche Pakete funktionieren nicht mit älteren Versionen
   - Nutzen Sie `python3 -m venv`, um die Python-Version explizit festzulegen

2. **Umgebungsvariablen:**
   - Immer `.env` von `.env.example` erstellen
   - `.env`-Datei nicht committen (steht in `.gitignore`)
   - Anmeldung mit `az login` für schlüssellose Entra ID-Authentifizierung

3. **Paketkonflikte:**
   - Frische virtuelle Umgebung verwenden
   - Installation aus `requirements.txt` bevorzugen statt einzelner Pakete
   - Manche Notebooks benötigen zusätzliche Pakete, die in ihren Markdown-Zellen erwähnt werden

4. **Azure-Dienste:**
   - Azure AI-Dienste erfordern aktives Abonnement
   - Einige Features sind regionsspezifisch
   - Sicherstellen, dass Ihre Azure OpenAI Modellbereitstellung die Responses API unterstützt

### Lernpfad

Empfohlene Reihenfolge der Lektionen:
1. **00-course-setup** - Einstieg für Umgebungseinrichtung
2. **01-intro-to-ai-agents** - Grundlagen der KI-Agenten verstehen
3. **02-explore-agentic-frameworks** - Verschiedene Frameworks kennenlernen
4. **03-agentic-design-patterns** - Kern-Designmuster
5. Danach sequenziell die nummerierten Lektionen fortsetzen

### Framework-Auswahl

Framework basierend auf Ihren Zielen wählen:
- **Alle Lektionen**: Microsoft Agent Framework (MAF) mit `FoundryChatClient`
- **Agenten registrieren sich serverseitig** im Microsoft Foundry Agent Service V2 und sind im Foundry-Portal sichtbar

### Hilfe erhalten

- Treten Sie dem [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) bei
- Lesen Sie die README-Dateien der Lektionen für spezifische Hinweise
- Überprüfen Sie das Haupt-[README.md](./README.md) für Kursübersicht
- Siehe [Course Setup](./00-course-setup/README.md) für detaillierte Einrichtungshinweise

### Beiträge leisten

Dies ist ein offenes Bildungsprojekt. Beiträge sind willkommen:
- Codebeispiele verbessern
- Tippfehler oder Fehler korrigieren
- Klärende Kommentare hinzufügen
- Neue Lektionsthemen vorschlagen
- In weitere Sprachen übersetzen

Siehe [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) für aktuelle Bedürfnisse.

## Projektspezifischer Kontext

### Mehrsprachige Unterstützung

Dieses Repository verwendet ein automatisiertes Übersetzungssystem:
- 50+ unterstützte Sprachen
- Übersetzungen in `/translations/<lang-code>/` Verzeichnissen
- GitHub Actions Workflow verwaltet Übersetzungsupdates
- Quelldateien sind auf Englisch im Repository-Stamm

### Lektionenstruktur

Jede Lektion folgt einem konsistenten Muster:
1. Video-Vorschaubild mit Link
2. Schriftlicher Lektionstext (README.md)
3. Codebeispiele in mehreren Frameworks
4. Lernziele und Voraussetzungen
5. Zusätzliche Lernressourcen verlinkt

### Benennung der Codebeispiele

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, MAF fortgeschrittene Muster
- `16-python-agent-framework.ipynb` - Lektion 16, produktionsreifer Kunden-Support-Agent
- `17-local-agent-foundry-local.ipynb` - Lektion 17, lokaler Agent mit Foundry Local + Qwen

### Spezielle Verzeichnisse

- `translated_images/` - Lokalisierte Bilder für Übersetzungen
- `images/` - Originalbilder für englische Inhalte
- `.devcontainer/` - VS Code Entwicklungscontainer-Konfiguration
- `.github/` - GitHub Actions Workflows und Templates

### Abhängigkeiten

Wichtige Pakete aus `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent Protokollunterstützung
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-Dienste
- `azure-identity` - Azure-Authentifizierung (AzureCliCredential)
- `azure-search-documents` - Azure AI Search Integration
- `mcp[cli]` - Model Context Protocol Unterstützung

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->