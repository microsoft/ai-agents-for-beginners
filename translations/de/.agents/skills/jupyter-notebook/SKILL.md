---
name: jupyter-notebook
description: Verwenden Sie, wenn der Benutzer darum bittet, Jupyter-Notebooks (`.ipynb`)
  für Experimente, Erkundungen oder Tutorials zu erstellen, aufzusetzen oder zu bearbeiten;
  bevorzugen Sie die mitgelieferten Vorlagen und führen Sie das Hilfsskript `new_notebook.py`
  aus, um ein sauberes Start-Notebook zu erzeugen.
---
# Jupyter Notebook-Fähigkeit

Erstelle saubere, reproduzierbare Jupyter-Notebooks für zwei Hauptmodi:

- Experimente und explorative Analyse
- Tutorials und lehrorientierte Schritt-für-Schritt-Anleitungen

Bevorzuge die mitgelieferten Vorlagen und das Hilfsskript für eine konsistente Struktur und weniger JSON-Fehler.

## Wann verwenden
- Erstelle ein neues `.ipynb`-Notebook von Grund auf.
- Konvertiere grobe Notizen oder Skripte in ein strukturiertes Notebook.
- Überarbeite ein vorhandenes Notebook, um es reproduzierbarer und übersichtlicher zu machen.
- Baue Experimente oder Tutorials, die von anderen gelesen oder erneut ausgeführt werden.

## Entscheidungsbaum
- Wenn die Anfrage explorativ, analytisch oder hypothesengetrieben ist, wähle `experiment`.
- Wenn die Anfrage instruktiv, schrittweise oder zielgruppenspezifisch ist, wähle `tutorial`.
- Wenn du ein bestehendes Notebook bearbeitest, behandle es als Refaktorierung: erhalte die Absicht und verbessere die Struktur.

## Fähigkeitenpfad (einmal festlegen)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Arbeitsablauf
1. Absicht festlegen.
Identifiziere die Notebook-Art: `experiment` oder `tutorial`.
Erfasse das Ziel, die Zielgruppe und wie "fertig" aussieht.

2. Gerüst aus der Vorlage erstellen.
Verwende das Hilfsskript, um zu vermeiden, das rohe Notebook-JSON manuell zu erstellen.

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb
```

3. Fülle das Notebook mit kleinen, ausführbaren Schritten.
Halte jede Code-Zelle auf einen Schritt fokussiert.
Füge kurze Markdown-Zellen hinzu, die Zweck und erwartetes Ergebnis erklären.
Vermeide umfangreiche, unübersichtliche Ausgaben, wenn eine kurze Zusammenfassung ausreicht.

4. Wende das richtige Muster an.
Für Experimente folge `references/experiment-patterns.md`.
Für Tutorials folge `references/tutorial-patterns.md`.

5. Beim Bearbeiten bestehender Notebooks sicher vorgehen.
Erhalte die Notebook-Struktur; vermeide das Umordnen von Zellen, es sei denn, es verbessert die von oben nach unten erzählte Reihenfolge.
Bevorzuge gezielte Änderungen gegenüber kompletten Neuüberarbeitungen.
Wenn du das rohe JSON bearbeiten musst, lies zuerst `references/notebook-structure.md`.

6. Ergebnis validieren.
Führe das Notebook von oben nach unten aus, wenn die Umgebung es zulässt.
Wenn die Ausführung nicht möglich ist, gib dies ausdrücklich an und beschreibe, wie lokal validiert werden kann.
Verwende die Abschluss-Checkliste in `references/quality-checklist.md`.

## Vorlagen und Hilfsskript
- Vorlagen befinden sich in `assets/experiment-template.ipynb` und `assets/tutorial-template.ipynb`.
- Das Hilfsskript lädt eine Vorlage, aktualisiert die Titelzelle und schreibt ein Notebook.

Skriptpfad:
- `$JUPYTER_NOTEBOOK_CLI` (standardmäßig installiert: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Temp- und Ausgabe-Konventionen
- Verwende `tmp/jupyter-notebook/` für Zwischenfiles; lösche sie nach Abschluss.
- Schreibe finale Artefakte unter `output/jupyter-notebook/`, wenn du in diesem Repo arbeitest.
- Verwende stabile, beschreibende Dateinamen (zum Beispiel `ablation-temperature.ipynb`).

## Abhängigkeiten (nur bei Bedarf installieren)
Bevorzuge `uv` für das Abhängigkeitsmanagement.

Optionale Python-Pakete für lokale Notebook-Ausführung:

```bash
uv pip install jupyterlab ipykernel
```

Das mitgelieferte Scaffold-Skript verwendet nur die Python-Standardbibliothek und benötigt keine zusätzlichen Abhängigkeiten.

## Umgebung
Keine erforderlichen Umgebungsvariablen.

## Referenzübersicht
- `references/experiment-patterns.md`: Aufbau von Experimenten und Heuristiken.
- `references/tutorial-patterns.md`: Struktur von Tutorials und Lehrablauf.
- `references/notebook-structure.md`: Form des Notebook-JSON und Regeln für sicheres Bearbeiten.
- `references/quality-checklist.md`: Abschließende Validierungs-Checkliste.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Haftungsausschluss:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir um Genauigkeit bemüht sind, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Originalsprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->