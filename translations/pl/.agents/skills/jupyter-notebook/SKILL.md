---
name: jupyter-notebook
description: Użyj, gdy użytkownik prosi o utworzenie, przygotowanie szkieletu lub
  edycję notatników Jupyter (`.ipynb`) do eksperymentów, eksploracji lub samouczków;
  preferuj dołączone szablony i uruchom skrypt pomocniczy `new_notebook.py`, aby wygenerować
  czysty notebook początkowy.
---
# Umiejętność Jupyter Notebook

Twórz czyste, odtwarzalne notatniki Jupyter dla dwóch głównych trybów:

- Eksperymenty i analiza eksploracyjna
- Samouczki i przewodniki skoncentrowane na nauczaniu

Preferuj dołączone szablony i skrypt pomocniczy dla spójnej struktury i mniejszej liczby błędów JSON.

## Kiedy używać
- Utwórz nowy notatnik `.ipynb` od podstaw.
- Przekształć surowe notatki lub skrypty w uporządkowany notatnik.
- Refaktoryzuj istniejący notatnik, aby był bardziej odtwarzalny i łatwiejszy do przeglądania.
- Twórz eksperymenty lub samouczki, które będą czytane lub ponownie uruchamiane przez innych.

## Drzewo decyzyjne
- Jeśli prośba ma charakter eksploracyjny, analityczny lub oparty na hipotezie, wybierz `experiment`.
- Jeśli prośba ma charakter instruktażowy, krok po kroku lub jest skierowana do konkretnej grupy odbiorców, wybierz `tutorial`.
- Jeśli edytujesz istniejący notatnik, traktuj to jako refaktoryzację: zachowaj zamiar i udoskonal strukturę.

## Ścieżka umiejętności (ustaw raz)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

Umiejętności na poziomie użytkownika instalują się w `$CODEX_HOME/skills` (domyślnie: `~/.codex/skills`).

## Przepływ pracy
1. Ustal zamiar.
Określ rodzaj notatnika: `experiment` lub `tutorial`.
Określ cel, odbiorców i to, jak wygląda „zrobione”.

2. Rozpocznij od szablonu.
Użyj skryptu pomocniczego, aby uniknąć ręcznego tworzenia surowego JSON notatnika.

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb
```

3. Wypełnij notatnik małymi, uruchamialnymi krokami.
Utrzymuj każdą komórkę kodu skoncentrowaną na jednym kroku.
Dodaj krótkie komórki Markdown, które wyjaśniają cel i oczekiwany rezultat.
Unikaj dużych, hałaśliwych wyników, gdy wystarczy krótkie podsumowanie.

4. Zastosuj odpowiedni wzorzec.
Dla eksperymentów przestrzegaj `references/experiment-patterns.md`.
Dla samouczków przestrzegaj `references/tutorial-patterns.md`.

5. Edytuj bezpiecznie podczas pracy z istniejącymi notatnikami.
Zachowaj strukturę notatnika; unikaj zmiany kolejności komórek, chyba że poprawia to opowieść od góry do dołu.
Preferuj ukierunkowane poprawki zamiast pełnych przeróbek.
Jeśli musisz edytować surowy JSON, najpierw przejrzyj `references/notebook-structure.md`.

6. Zweryfikuj wynik.
Uruchom notatnik od początku do końca, gdy środowisko na to pozwala.
Jeśli wykonanie nie jest możliwe, powiedz to wprost i opisz, jak zweryfikować lokalnie.
Użyj listy kontrolnej końcowego przeglądu w `references/quality-checklist.md`.

## Szablony i skrypt pomocniczy
- Szablony znajdują się w `assets/experiment-template.ipynb` i `assets/tutorial-template.ipynb`.
- Skrypt pomocniczy ładuje szablon, aktualizuje komórkę z tytułem i zapisuje notatnik.

Ścieżka skryptu:
- `$JUPYTER_NOTEBOOK_CLI` (domyślnie zainstalowany: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Konwencje dla plików tymczasowych i wyników
- Używaj `tmp/jupyter-notebook/` dla plików pośrednich; usuń po zakończeniu.
- Zapisuj końcowe artefakty w `output/jupyter-notebook/` gdy pracujesz w tym repozytorium.
- Używaj stabilnych, opisowych nazw plików (na przykład, `ablation-temperature.ipynb`).

## Zależności (instaluj tylko gdy potrzeba)
Preferuj `uv` do zarządzania zależnościami.

Opcjonalne pakiety Pythona do lokalnego uruchamiania notatników:

```bash
uv pip install jupyterlab ipykernel
```

Dołączony skrypt szablonowy używa tylko standardowej biblioteki Pythona i nie wymaga dodatkowych zależności.

## Środowisko
Brak wymaganych zmiennych środowiskowych.

## Mapa odniesień
- `references/experiment-patterns.md`: struktura eksperymentu i heurystyki.
- `references/tutorial-patterns.md`: struktura samouczku i przebieg nauczania.
- `references/notebook-structure.md`: kształt JSON notatnika i zasady bezpiecznej edycji.
- `references/quality-checklist.md`: lista kontrolna końcowej walidacji.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Zastrzeżenie:
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczeniowej AI Co-op Translator (https://github.com/Azure/co-op-translator). Chociaż dokładamy starań o poprawność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być traktowany jako dokument wiążący. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za ewentualne nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->