# Beispiel-Quittungen Fixtures

Drei vorgefertigte Quittungsdateien zur Ansicht, ohne das Notebook auszuführen.

| Datei | Was es ist |
|---|---|
| `01_valid_receipt.json` | Eine gültige signierte Quittung für einen `lookup_flights` Toolaufruf. Die Verifikation ergibt True. |
| `02_tampered_receipt.json` | Dieselbe Quittung mit einem nach der Signierung veränderten Feld. Die Verifikation ergibt False. |
| `03_chain_three_receipts.json` | Eine Kette von drei gültigen Quittungen (search, hold, book) mit `previous_receipt_hash`, die jede mit der vorherigen verbinden. |

Die Fixtures signieren die kanonischen JCS-Bytes der Nutzlast direkt mit Ed25519.
SHA-256 wird weiterhin für Inhalts-Hashes und Quittungsketten-Verbindungen verwendet, jedoch nicht als
zusätzlicher Pre-Hash vor der Signierung.

## Verifikation der Beispiele

Führen Sie in `18-signed-receipts.ipynb` zunächst Setup und die Abschnitte 1 bis 3 aus.
Abschnitt 3 definiert `verify_chain`; die Abschnitte 1 und 2 alleine reichen nicht aus.
Führen Sie dann den folgenden Block in einer neuen Zelle aus, wobei das Arbeitsverzeichnis des Notebooks
auf `18-securing-ai-agents/code_samples` gesetzt ist. Die untenstehenden Fixture-Pfade beziehen sich relativ
auf dieses Verzeichnis.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# This fixture key is pinned by the verifier, outside the receipt under test.
FIXTURE_ISSUER_PUBLIC_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"
fixture_trusted_public_keys = {FIXTURE_ISSUER_PUBLIC_KEY}

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text())
print(
    f"Valid receipt: {verify_receipt(valid, fixture_trusted_public_keys)}"
)  # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text())
print(
    f"Tampered receipt: {verify_receipt(tampered, fixture_trusted_public_keys)}"
)  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text())
for r in verify_chain(chain, fixture_trusted_public_keys):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

### Prüfung des Beispiels ohne Jupyter

Vom Repository-Stammverzeichnis aus installieren Sie die Abhängigkeiten der Lektion und führen aus:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Diese Tests führen die Python-Beispiele des Notebooks und den exakten README-Block
oben aus. Sie prüfen auch, dass Manipulationen und nicht festgelegte Schlüssel von den
Verifizierern abgelehnt werden. Die Tests überspringen die Setup-Zelle `%pip` des Notebooks, da Abhängigkeiten
separat installiert werden. Sie verändern weder das Notebook noch die Fixtures.

## Wie diese erzeugt wurden

Die Fixtures verwenden denselben Codepfad wie das Notebook, mit einem festen Signaturschlüssel
und festen Zeitstempeln zur Byte-Reproduzierbarkeit. Zur Neuerstellung:

```bash
python3 generate_fixtures.py
```

(Das Skript befindet sich in diesem Verzeichnis bei `generate_fixtures.py`.)

## Was Studierende aus der Betrachtung des rohen JSON lernen

Das Lesen des rohen Quittungsformats fördert eine Intuition, die die Zellen im Notebook
nicht immer vermitteln. Studierende, die das JSON überfliegen, bemerken oft:

1. Die Signatur ist ein undurchsichtiger base64url-String, aber jedes andere Feld ist einfach
   lesbares JSON. Die Signatur verschlüsselt den Inhalt nicht; sie bestätigt ihn.
2. Das `public_key` ist in der Quittung eingebettet, was ausreicht, um die
   Selbstkonsistenz zu prüfen, jedoch nicht das Vertrauen in den Aussteller. Ein Prüfer muss es mit einem
   Schlüssel vergleichen, der außerhalb der Quittung festgelegt oder über ein vertrauenswürdiges Register aufgelöst wird.
3. Das Ändern eines einzelnen Zeichens in einem Feld und anschließendes erneutes Vergleichen dieser Datei mit
   `02_tampered_receipt.json` macht den Mechanismus auf Byte-Ebene greifbar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->