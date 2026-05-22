# Beispielbeleg Fixtures

Drei vorab generierte Belegdateien zur Inspektion ohne Ausführung des Notebooks.

| Datei | Was es ist |
|---|---|
| `01_valid_receipt.json` | Ein gültiger signierter Beleg für einen `lookup_flights` Toolaufruf. Die Verifikation ergibt True. |
| `02_tampered_receipt.json` | Derselbe Beleg mit einem Feld, das nach der Signierung geändert wurde. Die Verifikation ergibt False. |
| `03_chain_three_receipts.json` | Eine Kette von drei gültigen Belegen (Suche, Reservierung, Buchung) mit `previous_receipt_hash`, die jeden mit dem vorherigen verbindet. |

## Verifikation der Beispiele

Das Notebook führt die Verifikation in vier Abschnitten durch. Um diese Fixtures
direkt zu verifizieren, ohne das Notebook-Szenario durchzugehen:

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

Die Fixtures verwenden denselben Codepfad wie das Notebook, mit einem festen Signierschlüssel
und festen Zeitstempeln für byte-reproduzierbarkeit. Zur Neuerzeugung:

```bash
python3 generate_fixtures.py
```

(Das Skript befindet sich in `generate_fixtures.py` in diesem Verzeichnis.)

## Was Studierende beim Betrachten des rohen JSON lernen

Das Lesen des rohen Belegformats baut Intuition auf, die die Zellen im Notebook
nicht immer vermitteln. Studierende, die das JSON überfliegen, bemerken oft:

1. Die Signatur ist ein undurchschaubarer base64url-String, aber jedes andere Feld ist einfach
   lesbares JSON. Die Signatur verschlüsselt den Inhalt nicht; sie bestätigt ihn.
2. Der `public_key` ist im Beleg eingebettet. Ein Prüfer benötigt nichts Anderes
   zur Verifikation (vorausgesetzt, er vertraut darauf, dass der Schlüssel tatsächlich zum angegebenen
   Aussteller gehört; siehe die README der Lektion zur Identitätsinfrastruktur).
3. Wird ein einzelnes Zeichen eines Feldes verändert und diese Datei dann mit
   `02_tampered_receipt.json` verglichen, macht das den Mechanismus auf Byte-Ebene anschaulich.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->