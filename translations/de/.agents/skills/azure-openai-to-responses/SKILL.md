---
name: azure-openai-to-responses
license: MIT
---
# Migration von Python-Apps von Azure OpenAI Chat Completions zur Responses API

> **AUTORITATIVE ANLEITUNG — GENAU BEFOLGEN**
>
> Diese Fähigkeit migriert Python-Codebasen, die Azure OpenAI Chat Completions verwenden,
> zur einheitlichen Responses API. Folgen Sie diesen Anweisungen genau.
> Improvisieren Sie nicht bei Parameterzuordnungen und erfinden Sie keine API-Strukturen.

---

## Auslöser

Aktivieren Sie diese Fähigkeit, wenn der Benutzer:
- Eine Python-App von Azure OpenAI Chat Completions zur Responses API migrieren möchte
- Die Python OpenAI SDK-Nutzung auf die neueste API-Struktur gegen Azure OpenAI aktualisieren will
- Python-Code für GPT-5 oder neuere Modelle vorbereitet, die Responses auf Azure erfordern
- Vom `AzureOpenAI`/`AsyncAzureOpenAI`-Client zum Standard-`OpenAI`/`AsyncOpenAI`-Client mit v1-Endpunkt wechseln möchte
- Veraltete Warnungen im Zusammenhang mit `AzureOpenAI`-Konstruktoren oder `api_version` beheben will

---

## ⚠️ Modellkompatibilität — ZUERST PRÜFEN

> **Vergewissern Sie sich vor der Migration, dass Ihre Azure OpenAI-Bereitstellung die Responses API unterstützt.**

### 1. Schnelltest Ihrer Bereitstellung (schnellster Weg)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **Hinweis**: `max_output_tokens` hat bei Azure OpenAI ein **Minimum von 16**. Werte unter 16 führen zu einem 400-Fehler. Verwenden Sie für Schnelltests 50+.

Wenn dies einen 404 zurückgibt, unterstützt das Modell der Bereitstellung Responses noch nicht — siehe untenstehende Referenz oder setzen Sie die Bereitstellung mit einem unterstützten Modell neu auf.

### 2. Verfügbare Modelle in Ihrer Region prüfen (empfohlen)

Führen Sie das integrierte Modellkompatibilitäts-Tool aus, um zu sehen, welche Modelle in Ihrer Region mit Responses API-Unterstützung verfügbar sind:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Dies fragt Azure ARM live ab und zeigt eine Kompatibilitätsmatrix — welche Modelle Responses, strukturierte Ausgaben, Tools usw. unterstützen. Verwenden Sie `--filter gpt-5.1,gpt-5.2` zur Eingrenzung oder `--json` für Skripting.

### 3. Vollständige Modellunterstützungsreferenz

- **Live-Abfrage**: `python migrate.py models` (siehe oben — regionsspezifisch, immer aktuell)
- **Verfügbarkeit durchsuchen**: [Modell-Zusammentfassungstabelle und Regionsverfügbarkeit](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Schnellstart & Anleitung**: **https://aka.ms/openai/start**

### ⚠️ Einschränkungen älterer Modelle

> **WARNUNG**: Ältere Modelle (vor `gpt-4.1`) unterstützen möglicherweise nicht alle Features der Responses API vollständig.
>
> Bekannte Einschränkungen bei älteren Modellen:
> - **`reasoning`-Parameter**: Von vielen Nicht-Reasoning-Modellen nicht unterstützt. Migrations nur, wenn `reasoning` bereits im Originalcode vorhanden war.
> - **`seed`-Parameter**: In der Responses API überhaupt nicht unterstützt — aus allen Anfragen entfernen.
> - **Strukturierte Ausgabe via `text.format`**: Ältere Modelle hören die JSON-Schemas mit `strict: true` unter Umständen nicht zuverlässig durch.
> - **Tool-Orchestrierung**: GPT-5+ orchestriert Werkzeugaufrufe als Teil der internen Reasoning-Logik. Ältere Modelle funktionieren mit Responses weiterhin, aber ohne diese tiefe Integration.
> - **Temperaturbeschränkungen**: Bei Migration zu `gpt-5` muss `temperature` weggelassen oder auf `1` gesetzt werden. Ältere Modelle haben diese Einschränkung nicht.

### O-Series Reasoning-Modelle (o1, o3-mini, o3, o4-mini)

O-Series-Modelle haben besondere Parameterbeschränkungen. Wenn Sie Apps migrieren, die auf O-Series-Modelle abzielen:

- **`temperature`**: Muss `1` sein (oder weggelassen werden). O-Series-Modelle akzeptieren keine anderen Werte.
- **`max_completion_tokens` → `max_output_tokens`**: Apps mit dem Azure-spezifischen `max_completion_tokens` müssen auf `max_output_tokens` umstellen. Setzen Sie hohe Werte (4096+), da Reasoning-Token auf das Limit angerechnet werden.
- **`reasoning_effort`**: Wenn die App `reasoning_effort` (low/medium/high) verwendet, beibehalten — die Responses API unterstützt diesen Parameter für O-Series-Modelle.
- **Streaming-Verhalten**: O-Series-Modelle können Ausgaben puffern, bis Reasoning abgeschlossen ist, bevor sie Text-Delta-Ereignisse senden. Streaming funktioniert weiterhin, aber der erste `response.output_text.delta` kann später eintreffen als bei GPT-Modellen.
- **`top_p`**: Nicht unterstützt auf O-Series — wenn vorhanden, entfernen.
- **Tool-Nutzung**: O-Series-Modelle unterstützen Tools via Responses API wie GPT-Modelle, aber die Qualität der Toolaufruf-Orchestrierung variiert je Modell.

**Anweisung — proaktive Modellberatung**: Während der Scanphase prüfen Sie, welches Modell die App anspricht (Bereitstellungsnamen, Umgebungsvariablen, Konfiguration). Wenn das Modell älter als `gpt-4.1` ist (nicht gpt-4.1+), informieren Sie den Nutzer proaktiv:
- Die Migration funktioniert für Basis-Text, Chat, Streaming und Tools mit ihrem aktuellen Modell.
- Neuere Modelle (`gpt-5.1`, `gpt-5.2`) bieten bessere Tool-Orchestrierung, strukturierte Ausgabe, Reasoning und regionsübergreifende Verfügbarkeit.
- Sie sollten ein Upgrade ihrer Bereitstellung erwägen, wenn es passt — es blockiert die Migration nicht.

Blockieren Sie die Migration nicht basierend auf Modellversion. Die Beratung ist informativ.

### GitHub Models unterstützt NICHT die Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) unterstützen die Responses API nicht.**

Wenn der Codepfad GitHub Models enthält (achten Sie auf `base_url` mit `models.github.ai` oder `models.inference.ai.azure.com`), **entfernen Sie ihn vollständig** während der Migration. Die Responses API benötigt Azure OpenAI, OpenAI oder einen kompatiblen lokalen Endpunkt (z. B. Ollama mit Responses-Unterstützung).

Aktion während Scan:
- Markieren Sie alle GitHub Models-Codepfade zur Entfernung.

---

## Framework-Migration

Viele Apps verwenden höherwertige Frameworks oberhalb von OpenAI. Bei deren Migration ändern sich auch die APIs der Frameworks — nicht nur die zugrundeliegenden OpenAI-Aufrufe.

### Microsoft Agent Framework (MAF)

**Prüfen Sie zuerst Ihre MAF-Version** — die Migration hängt davon ab, ob Sie MAF 1.0.0+ oder eine Beta/RC vor 1.0.0 nutzen.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **nutzt bereits die Responses API** — keine Migration nötig. Wenn der Code die alte `OpenAIChatCompletionClient`-Klasse verwendet (die `chat.completions.create` nutzt), ersetzen Sie sie durch `OpenAIChatClient`.

| Vorher | Nachher |
|--------|---------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Zur Versionsprüfung: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (Beta/RC-Versionen)

In MAF vor 1.0.0 nutzte `OpenAIChatClient` noch Chat Completions. Aktualisieren Sie auf `agent-framework-openai>=1.0.0`, wo `OpenAIChatClient` standardmäßig die Responses API nutzt.

Weitere Änderungen sind nicht nötig — `Agent` und Tool-APIs bleiben gleich.

### LangChain (`langchain-openai`)

Fügen Sie `use_responses_api=True` zu `ChatOpenAI()` hinzu. Aktualisieren Sie außerdem den Zugriif auf Antwortinhalt von `.content` auf `.text`.

| Vorher | Nachher |
|--------|---------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Vollständige Codebeispiele vor/nach finden Sie in [cheat-sheet.md](./references/cheat-sheet.md).

---

## Hinweise zur Frontend-Migration

> **Die Responses API ist eine serverseitige Angelegenheit.** Migrieren Sie Ihr Python-Backend; der HTTP-Vertrag des Frontends sollte unverändert bleiben, außer Ihr Backend ist nur eine dünne Weiterleitung — in diesem Fall erwägen Sie, das Responses-Request-Format zu übernehmen, um eine Übersetzungsschicht zu eliminieren. Wenn das Frontend OpenAI direkt mit einem clientseitigen Schlüssel aufruft, verschieben Sie diese Aufrufe zuerst in ein Backend.

### Deprecation von `@microsoft/ai-chat-protocol`

Das npm-Paket `@microsoft/ai-chat-protocol` ist veraltet und sollte durch [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) ersetzt werden. Falls es im Frontend vorkommt:

1. Ersetzen Sie das CDN-Skript-Tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Entfernen Sie die Instanziierung von `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Ersetzen Sie `client.getStreamedCompletion(messages)` durch einen direkten `fetch()`-Aufruf zum Backend-Streaming-Endpunkt.
4. Ersetzen Sie `for await (const response of result)` durch `for await (const chunk of readNDJSONStream(response.body))`.
5. Aktualisieren Sie die Eigenschaftszugriffe von `response.delta.content` / `response.error` auf `chunk.delta.content` / `chunk.error`.

---

## Ziele

- Alle Python-Aufrufe mit Chat Completions oder Legacy Completions gegen Azure OpenAI auflisten.
- Einen Migrationsplan mit Reihenfolge für die Python-Codebasis vorschlagen.
- Sichere, minimale Änderungen zur Umschaltung auf die Responses API vornehmen.
- Aufrufer auf die Responses-Ausgabeschema aktualisieren; keine Abwärtskompatibilitäts-Hüllen.
- Tests/Lints ausführen; triviale Fehler durch Migration beheben.
- Kleine, überprüfbare Änderungssätze vorbereiten und eine abschließende Zusammenfassung mit Diffs liefern (nicht committen).

---

## Leitplanken

- Nur Dateien im Git-Arbeitsbereich ändern. Niemals außerhalb schreiben.
- Keine Abwärtskompatibilitäts-Shims erhalten; Code auf neue API-Struktur migrieren.
- Keine Friedhofs-/Übergangskommentare oder Backup-Dateien hinterlassen.
- Streaming-Semantik beibehalten, falls zuvor genutzt; sonst ohne Streaming.
- In Genehmigungsmodus vor Befehlen oder Netzwerkaufrufen um Bestätigung bitten.
- Kein `git add`/`git commit`/`git push` ausführen; nur Arbeitsbaum-Änderungen erzeugen.

---

## Schritt 0: Azure OpenAI Client Migration (Voraussetzung)

Falls der Code `AzureOpenAI` oder `AsyncAzureOpenAI` Konstruktoren verwendet, migrieren Sie zuerst auf die Standard-`OpenAI` / `AsyncOpenAI` Konstruktoren. Die Azure-spezifischen Konstruktoren sind in `openai>=1.108.1` veraltet.

### Warum der v1 API-Pfad?

Der neue `/openai/v1`-Endpunkt verwendet den Standard-`OpenAI()`-Client anstelle von `AzureOpenAI()`, benötigt keinen `api_version`-Parameter und funktioniert identisch bei OpenAI und Azure OpenAI. Der gleiche Client-Code ist zukunftssicher — kein Versionsmanagement nötig.

### Wichtige Änderungen

| Vorher | Nachher |
|--------|---------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Komplett entfernen |

### Aufräumcheckliste

- Entfernen Sie das `api_version`-Argument aus dem Client-Konstruktor.
- Entfernen Sie Umgebungsvariablen `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` aus `.env`, App-Einstellungen und Bicep-/Infrastrukturdateien.
- Benennen Sie `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` um in `.env`, App-Einstellungen, Bicep-/Infra und Test-Fixures (Standard in Azure Identity SDK).
- Stellen Sie sicher, dass `openai>=1.108.1` in `requirements.txt` oder `pyproject.toml` steht.

### Umgebungsvariablen-Migration

| Alte Umgebungsvariable | Aktion | Anmerkungen |
|------------------------|---------|------------|
| `AZURE_OPENAI_VERSION` | **Entfernen** | Kein `api_version` mit v1-Endpunkt nötig |
| `AZURE_OPENAI_API_VERSION` | **Entfernen** | Gleich wie oben |
| `AZURE_OPENAI_CLIENT_ID` | **Umbenennen** → `AZURE_CLIENT_ID` | Standard-Azure-Identity-SDK-Konvention für `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Beibehalten** | Wird weiterhin zur `base_url`-Konstruktion benötigt |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Beibehalten** | Wird als `model`-Parameter in `responses.create` verwendet |
| `AZURE_OPENAI_API_KEY` | **Beibehalten** | Für Schlüssel-basierte Authentifizierung als `api_key` genutzt |

Codebeispiele zur Client-Einrichtung (sync, async, EntraID, API-Schlüssel, Multi-Tenant) finden Sie in [cheat-sheet.md](./references/cheat-sheet.md).

---

## Schritt 1: Legacy-Aufrufe erkennen

Führen Sie das Skript [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) aus, um alle Aufrufe zu finden, die migriert werden müssen:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Alternativ führen Sie diese Suchen manuell aus — jeder Treffer ist ein Migrationsziel:

```bash
# Veraltete API-Aufrufe (müssen neu geschrieben werden)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Veraltete Azure-Client-Konstruktoren (müssen ersetzt werden)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Zugriffs-Muster auf Antwortstrukturen (müssen aktualisiert werden)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Werkzeugdefinitionen im alten verschachtelten Format (müssen abgeflacht werden)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Werkzeugergebnisse im alten Format (müssen in function_call_output konvertiert werden)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Veraltete Parameter (müssen entfernt oder umbenannt werden)
rg "response_format"
rg "max_tokens\b"        # Umbenennen in max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Veraltete Umgebungsvariablen (aufräumen)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # sollte AZURE_CLIENT_ID sein

# GitHub-Model-Endpunkte (müssen entfernt werden — Responses API wird nicht unterstützt)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Framework-weite veraltete Muster (müssen aktualisiert werden)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: durch OpenAIChatClient ersetzen
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: benötigt use_responses_api=True

# Testinfrastruktur (muss aktualisiert werden)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Zugriff auf Fehlerinhalt des Inhaltsfilters (muss aktualisiert werden — Struktur geändert)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # altes Singular — jetzt content_filter_results (Plural) innerhalb des content_filters-Arrays

# Rohe HTTP-Aufrufe an Chat Completions-Endpunkt (müssen URL aktualisieren)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristiken (erkennen und umschreiben)

- **Chat Completions Client**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure-Client-Konstruktoren**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Werkzeuge**: konvertiere Funktionsaufruf-Werkzeugdefinitionen vom verschachtelten Format (`{"type": "function", "function": {"name": ...}}`) in das flache Responses-Format (`{"type": "function", "name": ...}`); benutze `tool_choice`; gebe Werkzeugergebnisse als `{"type": "function_call_output", "call_id": ..., "output": ...}`-Elemente zurück (nicht als `{"role": "tool", ...}`).
- **Werkzeug-Rundreisen**: wenn das Modell Funktionsaufrufe zurückgibt, hänge `response.output`-Elemente an die Unterhaltung an (nicht ein manuelles `{"role": "assistant", "tool_calls": [...]}` Dictionary), dann füge `function_call_output`-Elemente für jedes Ergebnis hinzu.
- **Few-shot Werkzeug-Beispiele**: wenn die Unterhaltung fest codierte Werkzeugaufruf-Beispiele enthält, konvertiere sie zu `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`-Elementen. IDs müssen mit `fc_` beginnen.
- **`pydantic_function_tool()`**: dieser Helfer erzeugt noch das alte verschachtelte Format und ist **nicht kompatibel** mit `responses.create()`. Ersetze ihn durch manuelle Werkzeugdefinitionen oder eine Flach-Wrapping-Funktion.
- **Mehrstufig**: pflege den Unterhaltungshistorie im Client; übergebe vorherige Runden über `input`-Elemente.
- **Formatierung**: ersetze Chats oberste Ebene `response_format` durch `text.format` in Responses. Kanonische Form: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Content-Elemente**: ersetze Chat `content[].type: "text"` durch Responses `content[].type: "input_text"` für Benutzer/System-Runden.
- **Bild-Content-Elemente**: ersetze Chat `content[].type: "image_url"` durch Responses `content[].type: "input_image"`. Das Feld `image_url` ändert sich von einem verschachtelten Objekt `{"url": "..."}` zu einem flachen String. Siehe Cheat Sheet für Vorher/Nachher-Beispiele.
- **Argumentationsaufwand**: **migriere `reasoning` nur, wenn es bereits im Originalcode vorhanden ist**.
- **Fehlerbehandlung Content-Filter**: die Struktur des Fehlerkörpers hat sich geändert. Chat Completions nutzte `error.body["innererror"]["content_filter_result"]` (Singular); die Responses API nutzt `error.body["content_filters"][0]["content_filter_results"]` (Plural, in einem Array). Code, der auf `innererror` zugreift, löst `KeyError` aus. Schreibe es um, um den neuen Pfad zu verwenden.
- **Rohe HTTP-Aufrufe**: wenn die App direkt die Azure OpenAI REST API aufruft (via `requests`, `httpx` etc.) unter `/openai/deployments/{name}/chat/completions?api-version=...`, ändere es zu `/openai/v1/responses`. Der Request-Body ändert sich: `messages` → `input`, hinzufügen von `max_output_tokens` und `store: false`, entfernen des Query-Parameters `api-version`. Der Response-Body ändert sich: `choices[0].message.content` → `output[0].content[0].text` (Hinweis: `output_text` ist eine SDK-Komfort-Eigenschaft, nicht im rohen REST JSON enthalten).

---

## Schritt 2: Migration anwenden

### Migrationshinweise (Chat Completions → Responses)

- **Warum migrieren**: Responses ist die einheitliche API für Text, Werkzeuge und Streaming; Chat Completions ist veraltet. Mit GPT-5 ist Responses für beste Leistung erforderlich.
- **HTTP**: Azure-Endpunkt wechselt von `/openai/deployments/{name}/chat/completions` zu `/openai/v1/responses`.
- **Felder**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` bleibt unverändert.
- **Formatierung**: `response_format` → `text.format` mit einem passenden Objekt.
- **Content-Elemente**: Ersetze Chat `content[].type: "text"` durch Responses `content[].type: "input_text"` für System-/Benutzerrunden.
- **Bild-Content-Elemente**: Ersetze Chat `content[].type: "image_url"` durch Responses `content[].type: "input_image"`. Wandle das `image_url`-Feld von `{"image_url": {"url": "..."}}` zu `{"image_url": "..."}` (ein einfacher String — entweder eine HTTPS-URL oder eine `data:image/...;base64,...` Daten-URI) um.

### Parameter Mapping Referenz

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (Array von Items) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (Objekt) |
| `temperature` | `temperature` (unverändert) |
| `stop` | `stop` (unverändert) |
| `frequency_penalty` | `frequency_penalty` (unverändert) |
| `presence_penalty` | `presence_penalty` (unverändert) |
| `tools` / Funktionsaufrufe | `tools` (unverändert) |
| `seed` | **Entfernen** (nicht unterstützt) |
| `store` | `store` (auf `false` gesetzt) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (flacher String) |

Für vollständige Vorher/Nachher-Codebeispiele siehe [cheat-sheet.md](./references/cheat-sheet.md).

Für Migration der Testinfrastruktur (Mocks, Snapshots, Assertions) siehe [test-migration.md](./references/test-migration.md).

Für Fehlerbehebung und häufige Fallen siehe [troubleshooting.md](./references/troubleshooting.md).

---

## Datenaufbewahrung & Zustand

- Setze `store: false` für alle Requests an Responses.
- Verlasse dich nicht auf vorherige Nachrichten-IDs oder serverseitig gespeicherten Kontext; halte den Zustand client-managed und minimiere Metadaten.

---

## Akzeptanzkriterien

### Code-Level Gates (alle müssen bestehen)

- [ ] Keine Treffer für `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` in migrierten Dateien.
- [ ] Keine Treffer für `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — alle Konstruktoren verwenden `OpenAI`/`AsyncOpenAI` mit dem v1-Endpunkt.
- [ ] Keine Treffer für `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub Models Codepfade entfernt.
- [ ] Keine Treffer für `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ Code verwendet `OpenAIChatClient` (der die Responses API nutzt). Vor 1.0.0 auf `agent-framework-openai>=1.0.0` upgraden.
- [ ] Alle `ChatOpenAI(...)` Aufrufe beinhalten `use_responses_api=True`.
- [ ] Keine Treffer für `rg "choices\[0\]"` — alle Antwortzugriffe verwenden `resp.output_text` oder das Responses-Ausgabe-Schema.
- [ ] Kein `response_format` auf oberster Ebene; alle strukturierte Ausgabe verwendet `text={"format": {...}}`.
- [ ] `openai>=1.108.1` und `azure-identity` in `requirements.txt` oder `pyproject.toml`; Abhängigkeiten neu installiert.
- [ ] `store=False` gesetzt bei jedem `responses.create` Aufruf.
- [ ] Kein `api_version` beim Client-Konstruktor; `AZURE_OPENAI_API_VERSION` aus Umgebungsdateien und Infrastruktur entfernt.

### Testinfrastruktur Gates (alle müssen bestehen)

- [ ] Keine Treffer für `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Keine Treffer für `rg "_azure_ad_token_provider" tests/` — Assertions aktualisiert zur Prüfung von `isinstance(client, AsyncOpenAI)` oder `base_url`.
- [ ] Keine Treffer für `rg "prompt_filter_results|content_filter_results" tests/` — Azure-spezifische Filter-Mocks entfernt.
- [ ] Mock-Fixtures verwenden `kwargs.get("input")` statt `kwargs.get("messages")`.
- [ ] Snapshot- / Golden-Dateien aktualisiert auf Response Streaming-Form (kein `choices[0]`, `function_call`, `logprobs`, usw.).
- [ ] `pytest` läuft ohne Fehler nach allen Testanpassungen.

### Verhaltens-Gates (manuell oder mittels Test-Harness überprüfen)

- [ ] **Basis Completion**: Nicht-Streaming `responses.create` gibt nicht-leeren `output_text` zurück.
- [ ] **Streaming-Parität**: Wenn im Originalcode Streaming genutzt wurde, streamt der migrierte Code und liefert `response.output_text.delta` Ereignisse mit nicht-leeren Deltas.
- [ ] **Strukturierte Ausgabe**: Wenn `text.format` mit `json_schema` genutzt wird, gelingen `json.loads(resp.output_text)` und entspricht dem Schema.
- [ ] **Werkzeug-Aufruf-Schleife**: Wenn Werkzeuge genutzt werden, schickt das Modell Werkzeugaufrufe, die App führt sie aus, und die Folgeanfrage liefert ein finales `output_text` (keine Endlosschleife).
- [ ] **Async-Parität**: Wenn `AsyncAzureOpenAI` genutzt wurde, funktioniert das äquivalente `AsyncOpenAI` mit `await`.
- [ ] **Fehlerrate**: Keine neuen 400/401/404 Fehler im Vergleich zur Basis-Version vor der Migration.

### Liefergegenstände

- Zusammenfassung beinhaltet bearbeitete Dateien, Vorher/Nachher Zählung der Legacy-Aufrufe, und nächste Schritte.
- Änderungen nur als Arbeitsbaumbearbeitung (keine Commits).

---

## SDK Versionsanforderungen

| Paket | Minimale Version |
|-------|-----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Neueste (für EntraID Authentifizierung) |

---

## Referenzen

- [Cheat Sheet — alle Code-Snippets](./references/cheat-sheet.md)
- [Test Migration — Mocks, Snapshots, Assertions](./references/test-migration.md)
- [Fehlerbehebung — Fehler, Risikotabelle, Fallen](./references/troubleshooting.md)
- [detect_legacy.py — automatischer Scanner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API Dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API Versionslebenszyklus](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API Referenz](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->