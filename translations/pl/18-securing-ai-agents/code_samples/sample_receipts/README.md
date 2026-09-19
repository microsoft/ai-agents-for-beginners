# Przykładowe pliki paragonów

Trzy wcześniej wygenerowane pliki paragonów do inspekcji bez uruchamiania notatnika.

| Plik | Co to jest |
|---|---|
| `01_valid_receipt.json` | Prawidłowo podpisany paragon dla wywołania narzędzia `lookup_flights`. Weryfikacja zwraca True. |
| `02_tampered_receipt.json` | Ten sam paragon z jednym zmodyfikowanym polem po podpisaniu. Weryfikacja zwraca False. |
| `03_chain_three_receipts.json` | Łańcuch trzech prawidłowych paragonów (wyszukiwanie, blokowanie, rezerwacja) z `previous_receipt_hash` łączącym każdy z poprzednim. |

Pliki podpisują kanoniczne bajty JCS ładunku bezpośrednio przy użyciu Ed25519.
SHA-256 pozostaje używany do skrótów treści i łączy łańcucha paragonów, nie jako
dodatkowy wstępny skrót przed podpisaniem.

## Weryfikacja próbek

Notatnik przeprowadza weryfikację w czterech sekcjach. Aby bezpośrednio zweryfikować te pliki
bez przeglądania narracji notatnika:

```python
import json
from pathlib import Path

# Zakłada, że ukończyłeś importy i funkcje pomocnicze
# z sekcji 1 i 2 pliku 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Prawda

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Fałsz

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Jak to zostało wygenerowane

Pliki używają tej samej ścieżki kodu co notatnik, z jednym stałym kluczem podpisu
i stałymi znacznikami czasu dla powtarzalności bajtów. Aby wygenerować ponownie:

```bash
python3 generate_fixtures.py
```

(Skrypt znajduje się w `generate_fixtures.py` w tym katalogu.)

## Czego uczą się studenci, analizując surowy JSON

Czytanie surowego formatu paragonu buduje intuicję, której komórki w notatniku
nie zawsze dostarczają. Studenci, którzy przejrzą JSON, często zauważają:

1. Podpis jest nieprzejrzystym łańcuchem base64url, ale każde inne pole jest zwykłym,
   czytelnym JSON-em. Podpis nie szyfruje zawartości; zaświadcza o niej.
2. `public_key` jest osadzony w paragonie. Audytor nie potrzebuje niczego więcej,
   aby zweryfikować (pod warunkiem zaufania, że klucz rzeczywiście należy do deklarowanego
   wystawcy; zobacz README lekcji o infrastrukturze tożsamości).
3. Modyfikacja pojedynczego znaku w jakimkolwiek polu, a następnie porównanie tego pliku z
   `02_tampered_receipt.json`, urealnia mechanizm na poziomie bajtów.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->