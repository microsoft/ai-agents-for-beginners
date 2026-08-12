---
name: local-ai-agents
license: MIT
---
# Erstellen von lokalen KI-Agenten mit Foundry Local und Qwen

> Begleitfertigkeit für [Lektion 17 – Erstellen lokaler KI-Agenten](../../../17-creating-local-ai-agents/README.md).
> Verwenden Sie sie, um einem Lernenden zu helfen, einen Agenten zu erstellen, der eigenständig
> schlussfolgert, Werkzeuge aufruft und Dokumentationen durchsucht – vollständig auf dem eigenen Gerät, ohne Cloud-Inferenzen.
> Begründen Sie jede Empfehlung durch die Lektioneninhalte und das ausführbare Notebook.

## Auslöser

Aktivieren Sie diese Fertigkeit, wenn ein Lernender:
- Einen Agenten **vollständig lokal** aus Datenschutz-, Kosten- oder Offline-Gründen ausführen möchte.
- Ein Modell lokal mit **Foundry Local** bereitstellen und über den OpenAI-kompatiblen Endpunkt verbinden möchte.
- Ein **Qwen-Funktionsaufruf-Modell** verwenden möchte, um zuverlässige lokale Werkzeugaufrufe zu steuern.
- **Lokales RAG** (Chroma) oder einen **lokalen MCP-Server** hinzufügen möchte.
- Eine **hybride** lokale/Cloud-Routing-Strategie entwerfen möchte.

## Kern-Mentalmodell

Ein SLM tauscht Breite gegen Datenschutz, Kosten und Offline-Betrieb ein. Die erfolgreiche
Strategie: **Lassen Sie das SLM orchestrieren und die Werkzeuge die schwere Arbeit erledigen.**
Das Modell muss die Codebasis nicht *kennen* – es muss wissen, wann `read_file` und `search_docs` aufgerufen werden.
Das spielt mit den Stärken eines SLM (begrenzt Entscheidungen wie Werkzeugauswahl)
und weg von seinen Schwächen (breites Wissen, langes Multi-Hop-Schlussfolgern).


## Warum gerade diese Komponenten

- **Foundry Local** stellt einen **OpenAI-kompatiblen HTTP-Endpunkt** bereit, sodass Cloud-Agenten-Code durch bloßes Ändern der `base_url` übertragbar ist (mit lokalem Platzhalter-API-Schlüssel). Es wählt außerdem automatisch den besten Build (CPU/GPU/NPU) für die Maschine aus.
- **Qwen**-Modelle sind für Funktionsaufrufe trainiert und erzeugen konsistent wohlgeformte Werkzeugaufrufe – das verwandelt ein lokales *Chat*-Modell in einen lokalen *Agenten*.
- **Chroma** läuft im Prozess und speichert Vektoren auf der Festplatte, sodass die gesamte RAG-Pipeline (Einbetten → Speichern → Abrufen → Schließen) lokal bleibt.
- **MCP** ist ein Transport, kein Cloud-Dienst: ein MCP-Server kann lokal über `stdio` laufen.

## Einrichtung - Wesentliches

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # lokaler Platzhalter
```

~8 GB RAM sind ein realistisches Minimum; eine GPU/NPU hilft, ist aber nicht zwingend erforderlich.

## Zu reproduzierende Schlüsselmuster

Weisen Sie den Lernenden auf das Notebook
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) hin:

- **Sandboxed Werkzeuge**: jedes Dateiwertzeug löst Pfade auf und lehnt alles außerhalb eines einzelnen Projektstamms ab – selbst lokal läuft ein Werkzeug mit den Berechtigungen des Nutzers.
- **Werkzeugaufruf-Schleife**: Werkzeuge gemäß dem OpenAI-Werkzeugschema registrieren, lokal ausführen, Ergebnisse zurückspeisen, wiederholen bis zur finalen Antwort.
- **Lokales RAG**: Dokumente in eine Chroma-Sammlung einfügen; `search_docs` gibt die Top-k Abschnitte zurück.
- **Lokales MCP**: Verbindung zu einem lokalen Server über `stdio` herstellen; begrenzen auf ein Projektverzeichnis und Ausgaben validieren.

## Hybrides Routing (lokal als eines der Modelle)

| Situation | Wo es läuft |
|-----------|---------------|
| Sensible Daten / offline | Lokales SLM |
| Einfache, begrenzte Aufgabe | Lokales SLM (kostengünstig, schnell) |
| Kompliziertes Multi-Hop-Schlussfolgern bei nicht-sensiblen Daten | Cloud-Modell |
| Cloud-Ausfall | Lokales SLM (sanfter Abbau) |

Das spiegelt die Idee des Modell-Routings aus Lektion 16 wider, wobei die Arbeitsstation eine der Routen ist.
Bevorzugen Sie Designs, die auf lokal zurückfallen, sodass der Agent in der
Qualität nachlässt, anstatt komplett auszufallen.

## Schutzmaßnahmen für den Assistenten

- Halten Sie jede Datei-/Werkzeugoperation auf ein sandboxed Projektverzeichnis beschränkt.
- Senden Sie keinen Code oder Daten in die Cloud, wenn das erklärte Ziel des Lernenden Datenschutz/Offline ist – halten Sie die gesamte Pipeline lokal.
- Setzen Sie realistische Erwartungen an die Qualität des SLM; verlassen Sie sich eher auf Werkzeuge und RAG als auf das im Modell gespeicherte Wissen.
- Beachten Sie, dass Lektion 17 **keinen** Foundry Responses Endpunkt hat, sodass der Cloud-Rauchtest nicht gilt – validieren Sie durch lokale Ausführung des Notebooks.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->