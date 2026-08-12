# Notebook-Struktur

Jupyter-Notebooks sind JSON-Dokumente mit dieser groben Struktur:

- `nbformat` und `nbformat_minor`
- `metadata`
- `cells` (eine Liste von Markdown- und Codezellen)

Beim programmgesteuerten Bearbeiten von `.ipynb`-Dateien:

- Behalten Sie `nbformat` und `nbformat_minor` aus der Vorlage bei.
- Behalten Sie `cells` als geordnete Liste bei; ändern Sie die Reihenfolge nicht, es sei denn, dies ist beabsichtigt.
- Für Codezellen setzen Sie `execution_count` auf `null`, wenn unbekannt.
- Für Codezellen setzen Sie `outputs` auf eine leere Liste, wenn Sie ein Grundgerüst erstellen.
- Für Markdown-Zellen behalten Sie `cell_type="markdown"` und `metadata={}` bei.

Bevorzugen Sie das Erstellen eines Grundgerüsts aus den mitgelieferten Vorlagen oder `new_notebook.py` (zum Beispiel `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) anstatt rohes Notebook-JSON von Hand zu erstellen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Haftungsausschluss:
Dieses Dokument wurde mit dem KI‑Übersetzungsdienst Co-op Translator (https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->