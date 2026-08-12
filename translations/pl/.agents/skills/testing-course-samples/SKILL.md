---
name: testing-course-samples
---
# Testowanie przykładów kursu

Sprawdź, czy notatniki lekcji i przykładowy kod działają na żywo
w konfiguracji Microsoft Foundry / Azure OpenAI. Repozytorium zawiera runner w
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), który
uruchamia każdy notatnik Pythona bez interfejsu i wyświetla macierz PASS/FAIL.

## Kiedy używać
- "Zweryfikować wszystkie notatniki / przykłady na moim subskrypcji Azure."
- "Szybki test kursu po aktualizacji pakietów lub zmianie modeli."
- "Które lekcje nadal przechodzą / nie przechodzą na żywo?"

Nie używaj tego do AI Smoke Test GitHub Action (który weryfikuje *wdrożonych*
hostowanych agentów — patrz [`tests/README.md`](../../../tests/README.md)). To narzędzie
uruchamia notatniki lokalnie.

## Wymagania wstępne (sprawdź najpierw)
1. **Python 3.12+** z zależnościami kursu: `python -m pip install -r requirements.txt`
   plus wykonawcą: `python -m pip install nbconvert ipykernel`.
2. **`.env` w katalogu głównym repozytorium** (skopiuj z [`.env.example`](../../../../../.env.example)) zawierający co najmniej:
   - `AZURE_AI_PROJECT_ENDPOINT` — punkt końcowy projektu Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — nieprzestarzałe wdrożenie (np. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) i `AZURE_OPENAI_DEPLOYMENT`
     dla lekcji które bezpośrednio wywołują Azure OpenAI (Lekcja 06, 02-azure-openai, 14 handoff/human-loop).
3. Ukończone **`az login`** — próbki uwierzytelniają się przez `AzureCliCredential` (Entra ID, bez klucza).
4. Zweryfikuj, że wdrożenie modelu istnieje:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Uruchomienie walidacji
```powershell
# Wszystkie notatniki Pythona (pomija .NET, .venv, site-packages, tłumaczenia, zasoby umiejętności)
pwsh scripts/validate-notebooks.ps1

# Pojedyncza lekcja, z dłuższym limitem czasu na pojedynczą komórkę
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Tylko lista tego, co by się uruchomiło (bez wykonywania)
pwsh scripts/validate-notebooks.ps1 -List

# Jawny interpreter (jeśli `python` nie jest w PATH, np. alias Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skrypt zapisuje wykonane kopie, logi per-notebook i `results.json` do
`$env:TEMP\aiab-nbval` i kończy się liczbą błędów.

Przemijające błędy (limity HTTP 429 współdzielonej subskrypcji, okazjonalne
problemy z tokenem `AzureCliCredential`, lub timeout) są automatycznie powtarzane
(`-Retries`, domyślnie 2, z opóźnieniem `-RetryDelaySeconds`, domyślnie 20). Jeśli
wdrożenie modelu często powoduje 429, sprawdź globalny limit TPM subskrypcji standardowej
(`az cognitiveservices usage list -l <region>`) — zwiększenie pojemności pojedynczego
wdrożenia nic nie da gdy *limit subskrypcji* jest wyczerpany.

## Interpretacja wyników
- `PASS` — notatnik uruchomił się od początku do końca bez błędów w komórkach.
- `FAIL` — pokazana jest pierwsza linia `*Error` / `*Exception`; otwórz pasujący
  `log_*.txt` w katalogu wyjściowym, aby zobaczyć pełny traceback.
- Pojedyncza nieudana próba notatnika objęta jest limitem `-Timeout` (na komórkę), więc zablokowana
  komórka interaktywna powoduje `StdinNotImplementedError` zamiast zawieszenia.

## Lekcje wymagające dodatkowych zasobów (oczekiwane niepowodzenia bez nich)
| Lekcja | Dodatkowy wymóg |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, klucz) — posiada ścieżkę awaryjną w pamięci |
| 11 MCP / GitHub | Serwer GitHub MCP + PAT |
| 13 pamięć (cognee) | `cognee` skonfigurowany z dostawcą modelu |
| 15 użycie przeglądarki | Zainstalowane przeglądarki Playwright (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 lokalny agent | Lokalne środowisko Foundry + pobrany model Qwen (na urządzeniu, bez chmury) |
| notatniki `*-dotnet-*` | Jądro .NET Interactive (domyślnie wykluczone; użyj `-IncludeDotnet`) |

## Raportowanie wyników
Podsumuj w tabeli PASS/FAIL pogrupowanej według lekcji. Oddziel rzeczywiste regresje
(błędy kodu/konfiguracji do naprawienia) od braków środowiskowych (brak Search/Foundry Local/PAT),
i wskaż odpowiedni `log_*.txt` dla każdego rzeczywistego błędu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->