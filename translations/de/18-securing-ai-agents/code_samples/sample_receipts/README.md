# Beispielquittungs-Fixtures

Vier vorab generierte Quittungsdateien zur Inspektion ohne Ausführung des Notebooks.

| Datei | Was es ist |
|---|---|
| `01_valid_receipt.json` | Eine gültige signierte Quittung für einen `lookup_flights` Werkzeugaufruf. Die Verifikation ergibt True. |
| `02_tampered_receipt.json` | Dieselbe Quittung, bei der nach der Signierung ein Feld geändert wurde. Die Verifikation ergibt False. |
| `03_chain_three_receipts.json` | Eine Kette von drei gültigen Quittungen (search, hold, book), wobei `previous_receipt_hash` jede mit der vorherigen verknüpft. |
| `04_resigned_receipt.json` | Dieselbe Quittung manipuliert und dann von einem Angreifer erneut signiert, mit dem öffentlichen Schlüssel des Angreifers eingebettet. Verifiziert gegen den darin enthaltenen Schlüssel. Scheitert an dem Schlüssel des Ausstellers. |

Die Fixtures signieren die kanonischen JCS-Bytes der Nutzlast direkt mit Ed25519.
SHA-256 bleibt für Inhalts-Hashes und Quittungs-Ketten-Links in Gebrauch, nicht als
zusätzlicher Pre-Hash vor der Signierung.

## Verifikation der Beispiele

In `18-signed-receipts.ipynb` zunächst Setup und die Abschnitte 1 bis 3 ausführen.
Abschnitt 3 definiert `verify_chain`; nur die Abschnitte 1 und 2 sind nicht ausreichend.
Dann den folgenden Block in einer neuen Zelle ausführen, wobei das Arbeitsverzeichnis des Notebooks
auf `18-securing-ai-agents/code_samples` gesetzt ist. Die Pfade der Fixtures unten sind relativ zu diesem Verzeichnis.


```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# The issuer's key, pinned here rather than read from any receipt. In a real
# deployment it comes from the issuer's JWK Set or a pinned config value.
# This is the public half of the fixed signing key in generate_fixtures.py.
ISSUER_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text(encoding="utf-8"))
print(f"Valid receipt: {verify_receipt(valid, ISSUER_KEY)}")        # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text(encoding="utf-8"))
print(f"Tampered receipt: {verify_receipt(tampered, ISSUER_KEY)}")  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text(encoding="utf-8"))
for r in verify_chain(chain, ISSUER_KEY):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")

# The forgery. Verified against the key it carries, it passes. Against the
# issuer's key, it fails. Only the second question is worth asking.
forged = json.loads((fixture_dir / "04_resigned_receipt.json").read_text(encoding="utf-8"))
print(f"Forged, checked against its own key: "
      f"{verify_receipt(forged, forged['signature']['public_key'])}")  # True
print(f"Forged, checked against issuer key:  "
      f"{verify_receipt(forged, ISSUER_KEY)}")                        # False
```

### Überprüfung des Beispiels ohne Jupyter

Vom Repository-Stamm aus die Abhängigkeiten der Lektion installieren und ausführen:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Diese Tests führen die Python-Beispiele des Notebooks und den exakten README-Block
oben aus. Sie prüfen auch, dass Manipulationen und ungepinnte Schlüssel von den
Verifizierern abgelehnt werden. Die Tests überspringen die `%pip` Setup-Zelle des Notebooks, da Abhängigkeiten
separat installiert werden. Sie verändern weder das Notebook noch die Fixtures.

## So wurden diese erzeugt

Die Fixtures verwenden denselben Codepfad wie das Notebook, mit einem festen Signaturschlüssel
und festen Zeitstempeln für Bytereproduzierbarkeit. Zur Neuerzeugung:

```bash
python3 generate_fixtures.py
```

(Das Skript befindet sich in `generate_fixtures.py` in diesem Verzeichnis.)

`../test_signed_receipts.py` überprüft das alles automatisch: es führt den
Code des Notebooks aus, verifiziert diese vier Fixtures mit den
`verify_receipt` und `verify_chain` des Notebooks und bestätigt, dass die Neuerzeugung der
Fixtures identische Bytes liefert. Von `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Was Studierende durch das Betrachten von rohem JSON lernen

Das Lesen des rohen Quittungsformats schafft eine Intuition, die die Zellen im Notebook
nicht immer bieten. Studierende, die das JSON überfliegen, bemerken oft:

1. Die Signatur ist ein undurchsichtiger base64url-String, aber jedes andere Feld ist einfach
   lesbares JSON. Die Signatur verschlüsselt den Inhalt nicht; sie bestätigt ihn.
2. Der `public_key` ist in der Quittung eingebettet, was die Datei
   eigenständig macht, aber nicht Gegenstand der Verifikation durch einen Prüfer ist. Vergleiche
   `02_tampered_receipt.json` mit `04_resigned_receipt.json`: beide wurden
   nach der Signierung verändert, aber die zweite wurde mit dem
   eigenen Schlüssel des Angreifers erneut signiert, sodass sie gegen den darin enthaltenen Schlüssel verifiziert wird. Der eingebettete Schlüssel
   zeigt an, dass die Datei intern konsistent ist. Nur ein anderweitig erhaltener Schlüssel
   gibt Auskunft darüber, wer sie ausgestellt hat.
3. Wird ein einzelnes Zeichen eines beliebigen Felds außerhalb von `signature` geändert und dann
   diese Datei mit `02_tampered_receipt.json` erneut verglichen, wird der
   bytegenaue Mechanismus anschaulich.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->