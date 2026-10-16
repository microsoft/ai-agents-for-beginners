# Beispielquittungs-Fixtures

Drei vorerzeugte Quittungsdateien zur Inspektion, ohne das Notebook auszuführen.

| Datei | Was es ist |
|---|---|
| `01_valid_receipt.json` | Eine gültige signierte Quittung für einen `lookup_flights`-Werkzeugaufruf. Die Verifikation ergibt True. |
| `02_tampered_receipt.json` | Dieselbe Quittung mit einem nach der Signierung veränderten Feld. Die Verifikation ergibt False. |
| `03_chain_three_receipts.json` | Eine Kette von drei gültigen Quittungen (Suche, Halten, Buchen) mit `previous_receipt_hash`, das jede mit der vorherigen verknüpft. |

Die Fixtures signieren direkt die kanonischen JCS-Bytes der Nutzlast mit Ed25519.
SHA-256 wird weiterhin für Inhalts-Hashes und Quittungsketten-Links verwendet, nicht als
zusätzlicher Vorhash vor der Signierung.

## Verifikation der Beispiele

Das Notebook führt die Verifikation in vier Abschnitten durch. Um diese Fixtures
direkt zu verifizieren, ohne die Notebook-Erklärungen durchzugehen:

```python
import json
from pathlib import Path

# Es wird angenommen, dass Sie die Importe und Hilfsfunktionen abgeschlossen haben
# aus den Abschnitten 1 und 2 von 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Wahr

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Falsch

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Wie diese erzeugt wurden

Die Fixtures verwenden denselben Codepfad wie das Notebook, mit einem festen Signaturschlüssel
und festen Zeitstempeln für reproduzierbare Bytes. Zum Neuerzeugen:

```bash
python3 generate_fixtures.py
```

(Das Skript befindet sich in diesem Verzeichnis unter `generate_fixtures.py`.)

## Was Studierende beim Inspizieren rohen JSON lernen

Das Lesen des rohen Quittungsformats baut eine Intuition auf, die die Zellen im Notebook
nicht immer vermitteln. Studierende, die das JSON überfliegen, bemerken oft:

1. Die Signatur ist ein undurchsichtiger base64url-String, aber jedes andere Feld ist reines
   lesbares JSON. Die Signatur verschlüsselt den Inhalt nicht; sie bestätigt ihn.
2. Der `public_key` ist in der Quittung eingebettet. Ein Prüfer benötigt nichts Weiteres
   zur Verifikation (vorausgesetzt, er vertraut darauf, dass der Schlüssel tatsächlich dem angegebenen
   Aussteller gehört; siehe die Lektion-README zur Identitätsinfrastruktur).
3. Das Ändern eines einzelnen Zeichens in einem Feld und anschließendes Vergleichen mit
   `02_tampered_receipt.json` macht den Mechanismus auf Byte-Ebene anschaulich.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->