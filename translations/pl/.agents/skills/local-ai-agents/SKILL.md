---
name: local-ai-agents
license: MIT
---
# Tworzenie lokalnych agentów AI za pomocą Foundry Local i Qwen

> Umiejętność towarzysząca do [Lekcji 17 – Tworzenie lokalnych agentów AI](../../../17-creating-local-ai-agents/README.md).
> Użyj jej, aby pomóc uczniowi zbudować agenta, który samodzielnie rozumuje, wywołuje narzędzia i przeszukuje
> dokumentację w całości na własnym komputerze — bez inferencji w chmurze. Każdą
> rekomendację oprzyj na treści lekcji i działającym notatniku.

## Wyzwalacze

Aktywuj tę umiejętność, gdy uczeń chce:
- Uruchomić agenta **w pełni na urządzeniu** ze względów prywatności, kosztów lub pracy offline.
- Udostępnić model lokalnie za pomocą **Foundry Local** i połączyć się przez zgodny z OpenAI punkt końcowy.
- Użyć modelu **Qwen z wywoływaniem funkcji** do niezawodnego lokalnego wywoływania narzędzi.
- Dodać **lokalne RAG** (Chroma) lub **lokalny serwer MCP**.
- Zaprojektować **hybrydową** strategię trasowania lokalnego/chmurowego.

## Podstawowy model mentalny

SLM wymienia rozległość na prywatność, koszt i działanie offline. Zwycięska
strategia: **pozwól SLM orkiestrze, a narzędziom na ciężką pracę.** Model
nie musi *znać* kodu — musi wiedzieć, kiedy wywołać `read_file` i `search_docs`. To gra do siły SLM (ograniczone decyzje
jak wybór narzędzi) i unika jego słabości (szeroka wiedza, długie wnioskowanie wieloetapowe).



## Dlaczego te konkretne elementy

- **Foundry Local** udostępnia **zgodny z OpenAI punkt końcowy HTTP**, więc kod agenta w chmurze przenosi się przez zmianę tylko `base_url` (i używanie lokalnego zastępczego klucza API). Automatycznie wybiera najlepszą wersję (CPU/GPU/NPU) dla maszyny.
- Modele **Qwen** są trenowane do wywoływania funkcji i konsekwentnie generują dobrze uformowane wywołania narzędzi — to właśnie zmienia lokalny model *chat* w lokalnego *agenta*.
- **Chroma** działa w procesie i przechowuje wektory na dysku, więc cały pipeline RAG (osadź → zapisz → wyszukaj → rozumuj) pozostaje lokalny.
- **MCP** to transport, a nie usługa chmurowa: serwer MCP może działać lokalnie przez `stdio`.

## Podstawy konfiguracji

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # lokalny zastępczy znak
```

~8 GB RAM to realistyczne minimum; GPU/NPU pomaga, ale nie jest wymagane.

## Kluczowe wzorce do odtworzenia

Wskaż uczniowi notatnik
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Narzędzia w piaskownicy**: każde narzędzie plikowe rozwiązuje ścieżki i odrzuca wszystko poza pojedynczym katalogiem projektu — nawet lokalnie narzędzie działa z uprawnieniami użytkownika.
- **Pętla wywoływania narzędzi**: rejestruj narzędzia według schematu narzędzi OpenAI, wykonuj żądane narzędzia lokalnie, podawaj wyniki z powrotem, powtarzaj aż do uzyskania ostatecznej odpowiedzi.
- **Lokalne RAG**: dodawaj dokumenty do kolekcji Chroma; `search_docs` zwraca najlepsze fragmenty.
- **Lokalny MCP**: łącz się z lokalnym serwerem przez `stdio`; ogranicz go do katalogu projektu i waliduj jego wyniki.

## Hybrydowe trasowanie (lokalne jako jeden z modeli)

| Sytuacja | Gdzie działa |
|-----------|---------------|
| Wrażliwe dane / offline | Lokalny SLM |
| Proste, ograniczone zadanie | Lokalny SLM (tani, szybki) |
| Trudne wieloetapowe rozumowanie na danych niewrażliwych | Model w chmurze |
| Przerwa w działaniu chmury | Lokalny SLM (łagodne pogorszenie) |

To odzwierciedla pomysł trasowania modeli z Lekcji 16, gdzie stacja robocza jest jednym
z tras. Preferuj projekty, które przełączają się na lokalne, aby agent obniżał jakość
zamiast całkowicie zawieść.

## Ograniczenia dla asystenta

- Każda operacja na pliku/narzędziu musi być ograniczona do katalogu projektu w piaskownicy.
- Nie wysyłaj kodu ani danych do chmury, gdy celem ucznia jest prywatność/offline — trzymaj cały pipeline lokalnie.
- Ustal realistyczne oczekiwania co do jakości SLM; polegaj na narzędziach i RAG zamiast na zapamiętanej wiedzy modelu.
- Zauważ, że Lekcja 17 nie ma punktu końcowego Foundry Responses, więc test dymny w chmurze nie ma zastosowania — weryfikuj przez uruchomienie notatnika lokalnie.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->