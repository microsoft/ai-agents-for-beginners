# Struktura notatnika

Notatniki Jupyter są dokumentami JSON o następującej ogólnej strukturze:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (lista komórek markdown i kodu)

Podczas edytowania plików `.ipynb` programowo:

- Zachowaj `nbformat` i `nbformat_minor` ze szablonu.
- Trzymaj `cells` jako uporządkowaną listę; nie zmieniaj kolejności, chyba że celowo.
- Dla komórek kodu ustaw `execution_count` na `null`, jeśli wartość jest nieznana.
- Dla komórek kodu ustaw `outputs` na pustą listę podczas tworzenia szkieletu.
- Dla komórek markdown zachowaj `cell_type="markdown"` i `metadata={}`.

Korzystaj w pierwszej kolejności ze szkieletów dostarczonych wraz z szablonami lub z `new_notebook.py` (na przykład, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) zamiast ręcznego tworzenia surowego JSON-a notatnika.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Zastrzeżenie:
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy uznać za autorytatywne źródło. W przypadku informacji o charakterze krytycznym zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->