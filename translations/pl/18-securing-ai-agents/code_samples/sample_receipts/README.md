# Przykładowe pliki paragonów

Trzy wstępnie wygenerowane pliki paragonów do inspekcji bez uruchamiania notatnika.

| Plik | Co to jest |
|---|---|
| `01_valid_receipt.json` | Ważny podpisany paragon dla wywołania narzędzia `lookup_flights`. Weryfikacja zwraca True. |
| `02_tampered_receipt.json` | Ten sam paragon z jednym zmodyfikowanym polem po podpisaniu. Weryfikacja zwraca False. |
| `03_chain_three_receipts.json` | Łańcuch trzech ważnych paragonów (search, hold, book) z `previous_receipt_hash` łączącymi każdy z poprzednim. |

Pliki paragonów podpisują bezpośrednio kanoniczne bajty JCS ładunku za pomocą Ed25519.
SHA-256 pozostaje w użyciu dla skrótów zawartości i łączy łańcucha paragonów, a nie jako
dodatkowe wstępne mieszanie przed podpisaniem.

## Weryfikacja przykładów

W `18-signed-receipts.ipynb` najpierw uruchom Setup oraz sekcje 1 do 3.
Sekcja 3 definiuje `verify_chain`; same sekcje 1 i 2 nie są wystarczające.
Następnie uruchom poniższy blok w nowej komórce, ustawiając katalog roboczy notatnika
na `18-securing-ai-agents/code_samples`. Ścieżki do plików poniżej są względem tego katalogu.


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

### Sprawdzanie przykładu bez Jupyter

Z katalogu głównego repozytorium zainstaluj zależności lekcji i uruchom:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Te testy wykonują przykłady Pythona z notatnika oraz dokładny fragment README
powyżej. Sprawdzają również, czy modyfikacje i nieprzypięte klucze są odrzucane przez
weryfikatory. Testy pomijają komórkę ustawień `%pip` notatnika, ponieważ
zależności są instalowane osobno. Nie zmieniają one notatnika ani plików.

## Jak zostały wygenerowane

Pliki paragonów używają tej samej ścieżki kodu co notatnik, z jednym stałym kluczem
podpisującym i stałymi znacznikami czasu dla powtarzalności bajtów. Aby wygenerować ponownie:

```bash
python3 generate_fixtures.py
```

(Skrypt znajduje się w `generate_fixtures.py` w tym katalogu.)

## Czego uczą się studenci, przeglądając surowe JSON

Odczytywanie surowego formatu paragonu buduje intuicję, której komórki w notatniku
nie zawsze dostarczają. Studenci, którzy przejrzą JSON, często zauważają:

1. Podpis jest nieprzezroczystym ciągiem base64url, ale każde inne pole jest czytelnym
   zwykłym JSON-em. Podpis nie szyfruje zawartości; zaświadcza o niej.
2. `public_key` jest osadzony w paragonie, co wystarcza do sprawdzenia
   spójności, ale nie zaufania do wystawcy. Auditor musi porównać go z kluczem
   przypiętym poza paragonem lub rozwiązanym przez zaufany rejestr.
3. Modyfikacja pojedynczego znaku w dowolnym polu, a potem ponowne porównanie tego pliku z
   `02_tampered_receipt.json`, czyni mechanizm na poziomie bajtów namacalnym.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->