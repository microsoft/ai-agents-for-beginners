# Dziennik zmian

Wszystkie znaczące zmiany w kursie **AI Agents for Beginners** są dokumentowane w tym pliku.

## [Wydanie] — 2026-07-14

To wydanie przenosi kurs z dwóch nowo przestarzałych modeli, migruje pozostałe notatniki Lekcji do stabilnego API Microsoft Agent Framework i waliduje notatniki Pythona względem działającego środowiska Microsoft Foundry.

### Zmiany

- **Przeniesiono z przestarzałych modeli (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Oba modele `gpt-4.1` i `gpt-4.1-mini` są teraz przestarzałe (data wycofania **14 października 2026**). Każde odniesienie do nich w kursie (dokumentacja, `.env.example`, notatniki i przykłady Python/.NET) zamieniono na nieprzestarzały `gpt-5-mini`. Przykład trasowania modeli w Lekcji 16 zachowuje kontrast mały/duży używając `gpt-5-nano` (mały) i `gpt-5-mini` (duży). Załączone pliki zewnętrzne ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), historyczny tekst GitHub Models oraz notatki o możliwościach skilla `azure-openai-to-responses` celowo pozostały niezmienione.
- **Notatnik przekazania z Lekcji 14 zmigrowany do stabilnego API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) korzysta teraz z `agent_framework.orchestrations.HandoffBuilder` z `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, strumieniowania opartego o `event.type` oraz `FoundryChatClient` (zastępując usunięte symbole pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Notatnik człowieka w pętli z Lekcji 14 zmigrowany do stabilnego API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) teraz pauzuje za pomocą `ctx.request_info(...)` + `@response_handler` (zastępując usunięte `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), buduje za pomocą `WorkflowBuilder(start_executor=..., output_executors=[...])`, steruje strukturalnym outputem przez `default_options={"response_format": ...}`, oraz używa skryptowanej odpowiedzi, aby notatnik działał bez nadzoru (bez blokującego `input()`).
- **Konfiguracja środowiska** ([.env.example](../../.env.example)): zmieniono nazwy wdrożeń modeli na `gpt-5-mini`; dodano `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (trasowanie w Lekcji 16) oraz wcześniej brakujące `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (użycie przeglądarkowe w Lekcji 15).
- **Zależności** ([requirements.txt](../../requirements.txt)): ustalono wersje `agent-framework`, `agent-framework-foundry` oraz `agent-framework-openai` na `~=1.10.0` dla spójnego i zwalidowanego zestawu (wersja 1.11.0 dostarcza eksperymentalne zmiany łamiące interfejsy wykorzystywane przez te lekcje).

### Notatki i znane ograniczenia

- **Walidacja względem działającego Microsoft Foundry.** Notatniki Pythona zostały uruchomione bezgłowo przy użyciu `nbconvert` względem projektu Microsoft Foundry z użyciem `gpt-5-mini` (oraz `gpt-5-nano` dla trasowania w Lekcji 16). Wdrażaj odpowiedniki nieprzestarzałych modeli w swoim projekcie; notatniki odczytują nazwę wdrożenia z `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Niektóre lekcje nadal wymagają dodatkowych zasobów.** Lekcja 05 potrzebuje Azure AI Search; workflow Bing w Lekcji 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) wymaga połączenia z Bing i narzędzi hostowanych przez Microsoft Foundry Agent Service; Lekcje 13 (Cognee) i 17 (Foundry Local) potrzebują własnych środowisk uruchomieniowych.

## [Wydanie] — 2026-07-13

To wydanie dodaje dwie nowe lekcje zamykające łuk wdrażania — skalowanie agentów do Microsoft Foundry i ograniczenie do pojedynczej stacji roboczej — oraz pipeline testowy, odświeżoną nawigację kursu, nowe umiejętności uczniów i zaktualizowaną identyfikację wizualną.

### Dodano

- **Lekcja 16 — Wdrażanie skalowalnych agentów z Microsoft Foundry.** Nowa lekcja [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) oraz uruchamialny notatnik [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) tworzący produkcyjnego agenta wsparcia klienta (narzędzia, RAG, pamięć, trasowanie modeli, cache'owanie odpowiedzi, zatwierdzenie przez człowieka, brama ewaluacyjna i śledzenie OpenTelemetry), z diagramami Mermaid procesu rozwoju/wdrażania/uruchomienia, testem wiedzy, zadaniem i wyzwaniem.
- **Lekcja 17 — Tworzenie lokalnych agentów AI z Foundry Local i Qwen.** Nowa lekcja [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) oraz notatnik [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) budujący w pełni lokalnego asystenta inżynierskiego (wywoływanie funkcji Qwen przez Foundry Local, piaskownicowe narzędzia plikowe, lokalny RAG z Chroma, opcjonalny lokalny MCP), wraz z diagramami lokalnego/częściowo lokalnego RAG/wywoływania narzędzi, testem wiedzy, zadaniem i wyzwaniem.
- **Pipeline testu dymnego.** Nowy workflow [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) oraz katalogi na lekcję pod [tests/](./tests/README.md) dla wdrażalnych agentów w Lekcjach 01, 04, 05 i 16, wraz z plikiem indeksu README mapującym katalog na lekcję i nazwę hostowanego agenta. Lekcja 16 zyskuje sekcję "Walidacja wdrożonego agenta testami dymnymi"; Lekcje 01/04/05 opcjonalny wskaźnik testu dymnego.
- **Umiejętności uczniów.** Nowe umiejętności Agent Skills w `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (pakiet wskazówek z Lekcji 16 i 17) oraz [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (jak walidować przykłady notatników względem działającego Microsoft Foundry / Azure OpenAI).
- **Runner walidacji notatników.** Nowy [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) uruchamiający bezgłowo każdy notatnik Pythona przez `nbconvert` i drukujący macierz PASS/FAIL (oraz `results.json`). Automatycznie wykrywa root repozytorium i Pythona, wyklucza domyślnie niekursowe notatniki (`.venv`, `site-packages`, `translations`, zasoby szablonów skillów) i notatniki `.NET`, wspiera parametry `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, i `-Python`.
- **Nawigacja kursu.** Dodano linki Poprzednia/Następna lekcja do Lekcji 11–15 (wcześniej brakujące), tak że cały kurs jest połączony 00 → 18 w obu kierunkach.
- **Nowe miniaturki.** Miniaturki do Lekcji 16 i 17 oraz odświeżony obraz społecznościowy repozytorium [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (teraz reklamujący dwie nowe lekcje i adres `aka.ms/ai-agents-beginners`).
- **Zależności** ([requirements.txt](../../requirements.txt)): dodano `foundry-local-sdk` oraz `chromadb` dla Lekcji 17.

### Zmiany

- **Główna tabela lekcji w [README.md](./README.md)**: Lekcje 16 i 17 teraz linkują do swojej zawartości (wcześniej "Wkrótce"); obraz repozytorium podbity do `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: dodano Lekcje 16 i 17 do przewodnika lekcja po lekcji i ścieżek nauki oraz sekcję "Walidacja wdrożonych agentów testami dymnymi".
- **[AGENTS.md](./AGENTS.md)**: zaktualizowano liczbę/opis lekcji (00–18), dodano sekcję walidacji testami dymnymi oraz przykłady nazw próbnych dla Lekcji 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Poprzednia lekcja" teraz wskazuje Lekcję 17 (wcześniej Lekcja 15), zamykając łańcuch.
- **Ujednolicono odniesienia do modeli na nieprzestarzałe.** Zamieniono wszystkie odniesienia do `gpt-4o` / `gpt-4o-mini` w kursie (dokumentacja, `.env.example`, notatniki Python/.NET i przykłady) na `gpt-4.1-mini` — `gpt-4o` (wszystkie wersje) będzie wycofywany w 2026. Przykład trasowania modeli w Lekcji 16 zachowuje kontrast mały/duży używając `gpt-4.1-mini` (mały) i `gpt-4.1` (duży). Notatniki Python wybierają model teraz z zmiennych środowiskowych (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) zamiast zakodowanej nazwy modelu.

### Notatki i znane ograniczenia

- **Nie uruchamiane względem live Azure.** Notatniki nowych lekcji są przykładami edukacyjnymi; uruchamiaj i waliduj je we własnym środowisku Microsoft Foundry / Foundry Local. Workflow testu dymnego wymaga wdrożenia agenta lekcji i skonfigurowania sekretów Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) z rolą **Azure AI User** na poziomie projektu Foundry.
- **Lekcja 17 jest wyłącznie lokalna.** Nie ma punktu końcowego Foundry Responses, więc akcja testu dymnego nie dotyczy; waliduj ją, uruchamiając notatnik na swojej stacji roboczej.

## [Wydanie] — 2026-07-06

To wydanie migruje kurs do **Azure OpenAI Responses API**, ujednolica nazewnictwo produktu na **Microsoft Foundry** i **Microsoft Agent Framework (MAF)**, wycofuje GitHub Models, aktualizuje wersje SDK i dodaje nowe treści o modelach lokalnych oraz hostingu innych frameworków na Foundry.

### Dodano

- **Umiejętność migracji** — Zainstalowano Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (z [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) w `.agents/skills/`, wraz z jego odniesieniami i skryptem skanującym.
- **Foundry Local (uruchamianie modeli lokalnie)** — Nowa sekcja "Alternatywny dostawca: Foundry Local" w [00-course-setup/README.md](./00-course-setup/README.md) opisująca instalację (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` oraz powiązanie `FoundryLocalManager` z Microsoft Agent Framework za pomocą `OpenAIChatClient`.
- **Hostowanie agentów LangChain / LangGraph na Microsoft Foundry** — Nowa sekcja w [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) oraz uruchamialny przykład [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) używający `langchain-azure-ai[hosting]` i `ResponsesHostServer` (protokół `/responses`), na podstawie [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nowa sekcja "Przykład z życia: Microsoft Project Opal" w [15-browser-use/README.md](./15-browser-use/README.md) przedstawiająca Opal jako agenta do użytku komputerowego w przedsiębiorstwie oraz mapująca go na koncepcje kursu (człowiek w pętli, zaufanie/bezpieczeństwo, planowanie, Skills).
- **Drugi przykład Python z Lekcji 02** — Dodano [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (patrz "Zmiany" — migracja z dawnego notatnika Semantic Kernel) i podlinkowano go w README lekcji.
- Dodano sekcję Modele i Dostawcy do [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Zmiany

- **Chat Completions → Responses API (Python).** Przykłady wywołujące model bezpośrednio zostały zmigrowane z Chat Completions na Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), używając klienta `OpenAI` wobec stabilnego punktu końcowego Azure OpenAI `/openai/v1/` (bez `api_version`). Dotyczy to przykładów:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — pełny walkthrough wywoływania funkcji (schemat narzędzia spłaszczony do formatu Responses, wyniki narzędzia zwracane jako `function_call_output`, `max_output_tokens` itp.).

- **Modele GitHub → Azure OpenAI.** Modele GitHub są przestarzałe (wycofywane **lipiec 2026**) i nie obsługują Responses API. Wszystkie ścieżki kodu modeli GitHub zostały przekonwertowane na Azure OpenAI / Microsoft Foundry w przykładach Pythona i .NET:
  - Python: notatniki z lekcji 08 workflow (`01`–`03`), lekcja 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + towarzyszące dokumenty `.md` oraz notatniki / `.md` workflow dotNET lekcji 08 (`01`–`03`) teraz używają `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` z `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Poprzedni `02-semantic-kernel.ipynb` został przepisany, aby używać Microsoft Agent Framework z Azure OpenAI (Responses API) i przemianowany na `02-python-agent-framework-azure-openai.ipynb`.
- **Ustandaryzowano na `FoundryChatClient` + `as_agent`.** Kod w README i notatnikach, który odnosił się do `AzureAIProjectAgentProvider`, został ustandaryzowany zgodnie z kanonicznym wzorem stosowanym w Lekcji 01 i własnymi przykładami frameworka: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` z `provider.as_agent(...)`. Zaktualizowano w README i notatnikach Lekcji 02–14 (np. pamięć w Lekcji 13, wszystkie notatniki Lekcji 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Nazewnictwo produktu.** Zmieniono w całej angielskiej zawartości:
  - „Azure AI Foundry” / „Azure AI Studio” → **Microsoft Foundry**
  - „Azure AI Agent Service” → **Microsoft Foundry Agent Service**
  - (Bez zmian: „Azure OpenAI”, „Azure AI Search”, „Azure AI Inference” oraz nazwy zmiennych środowiskowych.)
- **Zależności** ([requirements.txt](../../requirements.txt)):
  - Zamrożono `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Zamrożono `openai>=1.108.1` (minimalna wersja dla Responses API).
  - Usunięto `azure-ai-inference` (było używane tylko w migrowanych przykładach modeli GitHub).
- **Konfiguracja środowiska** ([.env.example](../../.env.example)): usunięto zmienne modeli GitHub (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); dodano `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` oraz opcjonalne `AZURE_OPENAI_API_KEY`; zaktualizowano nazewnictwo na Microsoft Foundry.
- **Dokumentacja** — Zaktualizowano [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) oraz [STUDY_GUIDE.md](./STUDY_GUIDE.md) pod kątem powyższych zmian (zmienne środowiskowe, fragmenty weryfikujące, wskazówki dotyczące dostawców, nazewnictwo).

### Usunięto

- Kroki wdrożeniowe modeli GitHub i zmienne środowiskowe z dokumentacji konfiguracji (zastąpione przez Azure OpenAI / Microsoft Foundry).

### Bezpieczeństwo / Prywatność (sprzątanie przed publicznym udostępnieniem)

- Wyczyściliśmy wyniki wykonania notatników Jupyter, które ujawniały prawdziwe **ID subskrypcji Azure**, nazwy grup zasobów / zasobów oraz identyfikator połączenia Bing, a także developerzkie **lokalne ścieżki plików i nazwy użytkowników**, w:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Zweryfikowano, że w śledzonej angielskiej zawartości nie pozostały żadne klucze API, tokeny, ID subskrypcji ani ścieżki osobiste (pozostałości `GITHUB_TOKEN` to token GitHub Actions w workflow oraz PAT serwera GitHub MCP w konfiguracji Lekcji 11 — oba legalne i niezwiązane z modelami GitHub).

### Uwagi i znane ograniczenia

- **Nie wykonane/nie skompilowane.** Są to przykłady edukacyjne zaktualizowane pod kątem poprawności API i nazewnictwa; nie były uruchamiane na żywych zasobach Azure, a przykłady .NET nie były kompilowane w tym środowisku. Zweryfikuj je z własnym wdrożeniem Microsoft Foundry / Azure OpenAI.
- **Wdrożony model musi obsługiwać Responses API.** Używaj wdrożenia takiego jak `gpt-4.1-mini`, `gpt-4.1` lub modelu z serii `gpt-5.x`. Starsze modele obsługują podstawowe funkcje Responses, ale nie wszystkie.
- **Wersja agent-framework.** Przykłady celują w najnowszy MAF (`>=1.10.0`). Kanonicznym wywołaniem tworzenia agenta jest `client.as_agent(...)`; API zweryfikowano na podstawie opublikowanej dokumentacji frameworka oraz zainstalowanej wersji. Jeśli przypniesz inną wersję, potwierdź dostępność metody (`as_agent` vs `create_agent`).
- **Notatnik workflow lekcji 08, nr 04** świadomie zachowuje `AzureAIAgentClient` (z `agent-framework-azure-ai`), ponieważ używa hostowanych narzędzi Microsoft Foundry Agent Service (grounding Bing, interpreter kodu); jest już oparty na Responses.
- **Domyślne wdrożenie .NET.** Dwa przykłady workflow dotNET z lekcji 08 wcześniej miały na stałe wpisany konkretny model; teraz domyślnie używają `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Jeśli przykłady polegają na wejściu multimodalnym/wizji, ustaw `AZURE_OPENAI_DEPLOYMENT` na odpowiedni model.
- **Foundry Local** udostępnia kompatybilny z OpenAI punkt końcowy **Chat Completions** i jest przeznaczony do lokalnego rozwoju; do pełnego zestawu funkcji Responses API używaj Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->