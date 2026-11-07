# Przykładowe pliki paragonów

Cztery wstępnie wygenerowane pliki paragonów do sprawdzenia bez uruchamiania notesu.

| Plik | Co to jest |
|---|---|
| `01_valid_receipt.json` | Prawidłowy podpisany paragon dla wywołania narzędzia `lookup_flights`. Weryfikacja zwraca True. |
| `02_tampered_receipt.json` | Ten sam paragon z jednym polem zmienionym po podpisaniu. Weryfikacja zwraca False. |
| `03_chain_three_receipts.json` | Łańcuch trzech prawidłowych paragonów (search, hold, book) z `previous_receipt_hash` łączącym każdy z poprzednim. |
| `04_resigned_receipt.json` | Ten sam paragon zmanipulowany, a następnie ponownie podpisany przez atakującego, z osadzonym własnym kluczem publicznym atakującego. Weryfikuje się względem klucza w nim zawartego. Nie przechodzi weryfikacji względem klucza wystawcy. |

Pliki fixture podpisują bezpośrednio kanoniczne bajty JCS ładunku za pomocą Ed25519.
SHA-256 pozostaje w użyciu do skrótów treści i łączenia łańcucha paragonów, nie jako
dodatkowy pre-skrót przed podpisaniem.

## Weryfikacja próbek

W `18-signed-receipts.ipynb` najpierw uruchom Setup oraz sekcje od 1 do 3.
Sekcja 3 definiuje `verify_chain`; same sekcje 1 i 2 nie są wystarczające.
Następnie uruchom poniższy blok w nowej komórce, ustawiając katalog roboczy notesu
na `18-securing-ai-agents/code_samples`. Ścieżki do fixture poniżej są względne
względem tego katalogu.

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

### Sprawdzenie przykładu bez Jupyter

Z katalogu głównego repozytorium zainstaluj zależności lekcji i uruchom:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Testy te wykonują przykłady Pythona z notesu oraz dokładny blok README
powyżej. Sprawdzają też, że manipulacje i nieprzypięte klucze są odrzucane przez
weryfikatory. Testy pomijają komórkę setup `%pip` z notesu, ponieważ zależności
są instalowane osobno. Nie zmieniają notesu ani plików fixture.

## Jak to zostało wygenerowane

Pliki fixture używają tej samej ścieżki kodu co notes, z jednym stałym kluczem podpisującym
i stałymi znacznikami czasu dla reprodukowalności bajtowej. Aby wygenerować ponownie:

```bash
python3 generate_fixtures.py
```

(Skrypt znajduje się w `generate_fixtures.py` w tym katalogu.)

`../test_signed_receipts.py` sprawdza to wszystko automatycznie: uruchamia
kod notatnika, weryfikuje te cztery fikstury z notatnikiem
`verify_receipt` i `verify_chain` oraz potwierdza, że ponowne wygenerowanie
fikstur daje identyczne bajty. Z `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Czego uczą się studenci, analizując surowy JSON

Czytanie surowego formatu paragonu buduje intuicję, której komórki w notatniku
nie zawsze dostarczają. Studenci, którzy przeglądają JSON, często zauważają:

1. Podpis jest nieprzezroczystym ciągiem base64url, ale każde inne pole to zwykły,
   czytelny JSON. Podpis nie szyfruje zawartości; poświadcza ją.
2. `public_key` jest osadzone w paragonie, co czyni plik samowystarczalnym,
   ale nie jest tym, co audytor weryfikuje. Porównaj
   `02_tampered_receipt.json` z `04_resigned_receipt.json`: oba zostały
   zmienione po podpisaniu, ale drugi został ponownie podpisany kluczem
   atakującego, więc weryfikuje się względem klucza, który ze sobą niesie.
   Osadzony klucz mówi ci, że plik jest wewnętrznie spójny. Tylko klucz
   pozyskany z innego źródła mówi ci, kto go wydał.
3. Zmiana pojedynczego znaku w dowolnym polu poza `signature`, a następnie
   ponowne porównanie tego pliku z `02_tampered_receipt.json`, uświadamia
   mechanizm na poziomie bajtów.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->