# Beispiel-Beleg Fixtures

Drei vorerstellte Belegdateien zur Inspektion, ohne das Notebook auszuführen.

| Datei | Was es ist |
|---|---|
| `01_valid_receipt.json` | Ein gültiger signierter Beleg für einen `lookup_flights` Tool-Aufruf. Die Verifikation ergibt True. |
| `02_tampered_receipt.json` | Derselbe Beleg mit einem nach der Signierung geänderten Feld. Die Verifikation ergibt False. |
| `03_chain_three_receipts.json` | Eine Kette von drei gültigen Belegen (Suche, Reservierung, Buchung) mit `previous_receipt_hash`, der jeden mit dem vorherigen verknüpft. |

Die Fixtures signieren die kanonischen JCS-Bytes des Payloads direkt mit Ed25519.
SHA-256 wird weiterhin für Inhalts-Digests und Belegketten-Verknüpfungen verwendet, nicht als
zusätzliches Pre-Hash vor der Signierung.

## Verifikation der Beispiele

Das Notebook führt die Verifikation in vier Abschnitten durch. Um diese Fixtures
direkt zu verifizieren, ohne die Notebook-Erzählung durchzugehen:

```python
import json
from pathlib import Path

# Geht davon aus, dass Sie die Importe und Hilfsfunktionen abgeschlossen haben
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

Die Fixtures verwenden denselben Codepfad wie das Notebook, mit einem festen Signierschlüssel
und festen Zeitstempeln für byte-reproduzierbare Ergebnisse. Zum Regenerieren:

```bash
python3 generate_fixtures.py
```

(Das Skript befindet sich in diesem Verzeichnis unter `generate_fixtures.py`.)

## Was Studenten beim Inspektieren des rohen JSON lernen

Das Lesen des rohen Belegformats baut ein Verständnis auf, das die Zellen im Notebook
nicht immer vermitteln. Studenten, die das JSON überfliegen, bemerken oft:

1. Die Signatur ist ein undurchsichtiger base64url-String, aber jedes andere Feld ist einfach
   lesbares JSON. Die Signatur verschlüsselt den Inhalt nicht; sie bestätigt ihn.
2. Der `public_key` ist im Beleg eingebettet. Ein Prüfer benötigt nichts Weiteres,
   um zu verifizieren (vorausgesetzt, er vertraut darauf, dass der Schlüssel tatsächlich dem angegebenen
   Aussteller gehört; siehe die README-Lektion zur Identitätsinfrastruktur).
3. Wenn man ein einzelnes Zeichen eines Feldes ändert und danach diese Datei mit
   `02_tampered_receipt.json` vergleicht, macht das den Mechanismus auf Byte-Ebene greifbar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->