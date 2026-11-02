# Fehlerbehebung, Risikotabelle & Stolperfallen

## Fehlerbehebung bei 400er Statuscodes

| Fehler | Lösung |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Werkzeugdefinition verwendet altes verschachteltes Chat Completions Format | Von `{"type": "function", "function": {"name": ...}}` zu `{"type": "function", "name": ..., "parameters": ...}` abflachen — name, beschreibung, parameter kommen auf die oberste Ebene |
| `unknown_parameter: input[N].tool_calls` | Multi-Turn Werkzeugergebnisse verwenden altes Chat Completions Format | Ersetze `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` durch `response.output` Items + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` Werkzeug fehlt `required` Array | Bei `strict: true` müssen alle Eigenschaften in `required` aufgelistet werden und `additionalProperties: false` gesetzt sein |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` Werkzeug fehlt `additionalProperties: false` | Füge `"additionalProperties": false` zur Parameter-Objekt hinzu |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-Shot function_call ID hat falsches Präfix | IDs von Funktionsaufrufen müssen mit `fc_` beginnen (z.B. `fc_example1`), nicht mit `call_` |
| `missing_required_parameter: text.format.name` | Füge dem Format-Dict den Schlüssel `"name"` hinzu (z.B. `"name": "Output"`) |
| `invalid_type: text.format` | Stelle sicher, dass `text.format` ein Dict mit den Schlüsseln `type`, `name`, `strict`, `schema` ist — kein String |
| `invalid input content type` | Verwende `input_text`/`output_text` Inhaltstypen statt Chat `text` |
| `invalid input content type` (Bild) | Bildinhalt verwendet noch `"type": "image_url"` | Ändere zu `"type": "input_image"` |
| `Expected object, got string` bei `image_url` | `image_url` ist noch ein verschachteltes Objekt `{"url": "..."}` | Flache es zu einem einfachen String ab: `"image_url": "https://..."` oder `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` für `max_output_tokens` | Minimum ist **16** bei Azure OpenAI. Nutze 50+ für Tests, 1000+ für Produktion. |
| `429 Too Many Requests` während Streaming | Rate Limit erreicht. Umschließe Streaming mit `try/except`, sende Fehler-JSON an das Frontend, implementiere Backoff/Retry. |
| `KeyError: 'innererror'` bei Content Filter Fehler | Struktur des Fehlerkörpers im Responses API geändert | Chat Completions nutzte `error.body["innererror"]["content_filter_result"]`; Responses API nutzt `error.body["content_filters"][0]["content_filter_results"]` (Plural, in Array). Alle Zugriffe auf `innererror` neu schreiben. |

---

## Migrations-Risikotabelle

| Symptom | Wahrscheinlicher Fehler | Lösung |
|---------|---------------|-----|
| Leerer `output_text` / abgeschnittene Antwort | `max_output_tokens` zu niedrig für Reasoning-Modelle | Setze `max_output_tokens=1000` oder höher — Reasoning-Token zählen gegen das Limit |
| `400 invalid_type: text.format` | `response_format` String übergeben statt `text.format` Dict | Nutze `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` bei `/openai/v1/responses` | Falsche `base_url` — `/openai/v1/` Suffix fehlt | Setze `base_url=f"{endpoint}/openai/v1/"` (mit abschließendem Slash) |
| `401 Unauthorized` nach Wechsel zu `OpenAI()` | `api_key` nicht gesetzt oder Token Provider nicht korrekt übergeben | Für EntraID: `api_key=token_provider` (callable). Für API Key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Modell gibt `deployment not found` zurück | `model` Parameter stimmt nicht mit deinem Azure-Deployment-Namen überein | Nutze `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — dies ist der Deployment-Name, nicht der Modellname |
| `json.loads(resp.output_text)` wirft `JSONDecodeError` | Schema nicht durchgesetzt oder Modell unterstützt kein strenges JSON | Stelle sicher, dass `"strict": True` im Schema ist und prüfe, ob Modell strukturiertes Output unterstützt |
| Streaming liefert keine `delta` Events | Prüfung des falschen Ereignistyps | Filtere nach `event.type == "response.output_text.delta"`, nicht Chat's `chat.completion.chunk` |
| `400` Fehler bei Bildeingabe nach Migration | Bild Inhaltstyp nicht aktualisiert | Ändere `"type": "image_url"` → `"type": "input_image"` und flache `"image_url": {"url": "..."}` → `"image_url": "..."` (einfache Zeichenkette) ab |
| Werkzeugaufrufe schleifen unendlich | Ergebnis eines Werkzeugs im Folge-`input` fehlt | Nach Ausführung eines Werkzeugs ein `{"type": "function_call_output", "call_id": ..., "output": ...}` Item zum `input` der nächsten Anfrage hinzufügen |
| `temperature` Fehler mit GPT-5 oder o-Serie | Expliziter `temperature` Wert ungleich 1 | Entferne `temperature` oder setze auf `1` für GPT-5 und o-Serie Modelle (o1, o3-mini, o3, o4-mini) |
| `top_p` Fehler mit o-Serie | `top_p` wird nicht unterstützt | Entferne `top_p` bei Ziel auf o-Serie Modelle |
| `max_completion_tokens` nicht erkannt | Verwendung Azure-spezifischen Parameters | Ersetze `max_completion_tokens` durch `max_output_tokens`. Setze auf 4096+ für o-Serie (Reasoning-Token zählen gegen Limit). |
| Leeres oder abgeschnittenes Output von o-Serie | `max_output_tokens` zu niedrig | O-Serie nutzt intern Reasoning-Token. Setze `max_output_tokens=4096` oder höher — nicht 500–1000. |
| `400 integer_below_min_value` für `max_output_tokens` | Wert unter 16 | Azure OpenAI fordert `max_output_tokens >= 16`. Nutze 50+ für Smoke Tests, 1000+ für Produktion. |
| `429 Too Many Requests` mittendrin im Stream | Rate Limit durch Azure OpenAI | Stream bricht ohne Fehlermeldung ab. Umschließe `async for event in await coroutine:` immer mit `try/except` und sende `{"error": str(e)}` an das Frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Falscher Tenant oder nicht eingeloggt | `tenant_id=os.getenv("AZURE_TENANT_ID")` explizit übergeben. Lokal `azd auth login --tenant <tenant-id>` ausführen. |
| `404 Not Found` bei GitHub Modellen (`models.github.ai`) | GitHub Modelle unterstützen Responses API nicht | Entferne den GitHub Model-Codepfad komplett. Nutze Azure OpenAI, OpenAI oder kompatiblen lokalen Endpoint (z.B. Ollama mit Responses Support). |
| MAF `OpenAIChatCompletionClient` verwendet noch Chat Completions | Legacy MAF Client in 1.0.0+ verwendet | In MAF 1.0.0+ verwendet `OpenAIChatClient` standardmäßig Responses API. Ersetze `OpenAIChatCompletionClient` durch `OpenAIChatClient`. Für vor 1.0.0: Upgrade auf `agent-framework-openai>=1.0.0`. |
| LangChain Agent liefert leere Antwort oder scheitert bei Werkzeugaufrufen | `ChatOpenAI` nutzt nicht Responses API | Füge `use_responses_api=True` zu `ChatOpenAI(...)` hinzu. Ändere auch `.content` → `.text` bei Antwortnachrichten. |
| `KeyError: 'innererror'` im Content Filter Fehlerhandler | Fehlerkörperstruktur in Responses API geändert | Schreibe `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` um. `innererror` Wrapper entfällt; Filterdetails sind nun im obersten `content_filters` Array mit `content_filter_results` (Plural) in jedem Eintrag. |
| Direkter HTTP-Aufruf zu `/openai/deployments/.../chat/completions` liefert 404 | Alter Chat Completions REST Endpoint | URL auf `/openai/v1/responses` umschreiben. Request Body: `messages` → `input`, `max_output_tokens` + `store: false` hinzufügen, `api-version` Query Param entfernen. Response Parsen: `choices[0].message.content` → `output[0].content[0].text` (Achtung: `output_text` ist eine SDK Komfort-Eigenschaft, nicht in rohem REST JSON). |

---

## Stolperfallen

1. Wenn du zuvor Chat Completions für Gesprächszustand verwendet hast, verwalte deinen Zustand bei Responses explizit selbst.
2. Bevorzuge `max_output_tokens` statt des veralteten `max_tokens`.
3. Beim Wechsel zu `gpt-5` sicherstellen, dass `temperature` nicht angegeben oder auf `1` gesetzt ist.
4. Ersetze Chat `content[].type: "text"` durch Responses `content[].type: "input_text"` für Nutzer-/System-Eingaben.
5. Für `text.format` ein korrektes Dict bereitstellen (z.B. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), keinen einfachen String.
6. Der Parameter `seed` wird in Responses nicht unterstützt; entferne ihn aus Anfragen.
7. **Reasoning**: Nur `reasoning` hinzufügen, wenn der ursprüngliche Code es bereits benutzt hat. Füge `reasoning` nicht zu API-Aufrufen hinzu, die es nicht hatten — viele Nicht-Reasoning-Modelle unterstützen diesen Parameter nicht.
8. **Größe von `max_output_tokens`**: Für Reasoning-Modelle (GPT-5-mini, GPT-5, o-Serie) `max_output_tokens=4096` oder mehr verwenden — nicht zwischen 50–1000. Das Modell verwendet intern Reasoning-Token vor der sichtbaren Ausgabe; zu niedrige Limits führen zu abgeschnittenen oder leeren Antworten.
9. **O-Serie `max_completion_tokens`**: Wenn der originale Code `max_completion_tokens` (Azure-spezifisch für o-Serie) nutzte, ersetze durch `max_output_tokens`. Die Responses API akzeptiert `max_completion_tokens` nicht.
10. **O-Serie `reasoning_effort`**: Wenn der ursprüngliche Code `reasoning_effort` (low/medium/high) nutzte, migriere dies zu `reasoning={"effort": "<Wert>"}` im Responses API-Aufruf.
11. **O-Serie Streaming-Verzögerung**: O-Serie Modelle führen internes Reasoning durch, bevor sie Ausgabe generieren. Beim Streaming ist eine längere Verzögerung vor dem ersten `response.output_text.delta` Event normal — das Modell berechnet gerade, ist nicht hängen geblieben.
9. **`_azure_ad_token_provider` ist verschwunden**: `AsyncOpenAI` / `OpenAI` haben kein `_azure_ad_token_provider` Attribut mehr. Tests oder Code, die darauf zugreifen, schlagen mit `AttributeError` fehl. Der Token Provider wird als `api_key` übergeben und ist auf dem Client-Objekt nicht einsehbar.
10. **Snapshot- / Golden-Dateien**: Wenn der Test-Suite Snapshot-Tests nutzt, müssen **alle** Snapshot-Dateien mit Chat Completions Streaming-Struktur (`choices[0]`, `content_filter_results`, `function_call`, etc.) auf das neue Responses-Format aktualisiert werden. Das wird leicht übersehen und führt zu Prüfungsfehlern.
11. **Mock Monkeypatch-Pfad**: Der Monkeypatch-Zielpfad ändert sich von `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (oder `Responses.create` für sync). Nutzung des alten Pfads bewirkt stillschweigend nichts — der Mock wird nicht abgefangen, Tests laufen gegen echte API oder schlagen fehl.
12. **`input` statt `messages`**: Mock-Funktionen müssen `kwargs.get("input")` statt `kwargs.get("messages")` lesen. Die Responses API nutzt `input` für den Gesprächsverlauf.
13. **Umbenennung von Umgebungsvariablen**: Azure Identity SDK verwendet `AZURE_CLIENT_ID` (nicht `AZURE_OPENAI_CLIENT_ID`) für `ManagedIdentityCredential(client_id=...)`. In Tests, `.env` Dateien, App-Settings und Bicep/Infra umbenennen.
14. **Mindestwert von `max_output_tokens` ist 16**: Azure OpenAI lehnt Werte unter 16 mit `400 integer_below_min_value` ab. Für Smoke Tests `50`, für Produktion `1000`+ verwenden. Das alte `max_tokens` hatte dieses Minimum nicht.
15. **`tenant_id` für `AzureDeveloperCliCredential`**: Befindet sich die Azure OpenAI-Ressource in einem anderen Mandanten, muss `tenant_id` explizit übergeben werden — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Ohne dies wird stillschweigend der falsche Mandant verwendet und `401` Fehler zurückgegeben.
16. **Rate Limits äußern sich beim Streaming anders**: Bei Chat Completions verhinderte ein 429 meist das Starten des Streams. Bei Responses API Streaming kann ein 429 **mitten im Stream** auftreten — der asynchrone Iterator wirft eine Ausnahme. Umschließe die Streaming-Schleife immer mit `try/except` und sende eine Fehler-JSON-Zeile, damit das Frontend dies sauber behandeln kann.

17. **Fehlerbehandlung beim Streaming ist für Web-Apps obligatorisch**: Das Muster `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` ist entscheidend. Ohne dieses stirbt der SSE/JSONL-Stream bei einem serverseitigen Fehler stillschweigend ab und das Frontend hängt.
18. **Tool-Definitionen müssen das flache Format verwenden**: Die Responses API erwartet `{"type": "function", "name": ..., "parameters": ...}` — nicht das verschachtelte Chat Completions Format `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Dies ist der häufigste Migrationsfehler bei Funktion-aufrufendem Code.
19. **`pydantic_function_tool()` ist inkompatibel**: Der Helfer `openai.pydantic_function_tool()` erzeugt weiterhin das alte verschachtelte Format. Verwenden Sie ihn nicht mit `responses.create()`. Definieren Sie Tool-Schemata manuell oder flachen Sie die Ausgabe ab.
20. **Ergebnisse von Tools verwenden `function_call_output`, nicht `role: tool`**: Nach Ausführung eines Tools hängen Sie `{"type": "function_call_output", "call_id": ..., "output": ...}` an — nicht `{"role": "tool", "tool_call_id": ..., "content": ...}`. Für die Tool-Anfrage des Assistenten verwenden Sie `messages.extend(response.output)` — nicht ein manuelles `{"role": "assistant", "tool_calls": [...]}`-Dict.
21. **`strict: true` erfordert `required` + `additionalProperties: false`**: Wenn Sie `strict: true` bei einem Tool verwenden, muss jede Eigenschaft im Array `required` aufgeführt sein und `additionalProperties` muss `false` sein. Fehlt eines davon, entsteht ein 400 Fehler.
22. **Funktionsaufruf-IDs haben spezifische Präfixe**: Wenn Sie Few-Shot-`function_call`-Elemente in `input` angeben, muss das Feld `id` mit `fc_` beginnen und das Feld `call_id` mit `call_` (z. B. `"id": "fc_example1", "call_id": "call_example1"`). Die Verwendung des alten Chat Completions-Präfixes `call_` für `id` wird abgelehnt.
23. **GitHub Models unterstützen die Responses API nicht**: Wenn die App einen GitHub Models Codepfad hat (`base_url` verweist auf `models.github.ai` oder `models.inference.ai.azure.com`), entfernen Sie ihn komplett. Es gibt keinen Migrationspfad — wechseln Sie zu Azure OpenAI, OpenAI oder einem kompatiblen lokalen Endpunkt.
24. **Die Struktur des Fehlerkörpers beim Inhaltsfilter hat sich geändert**: Chat Completions Fehler nutzten `error.body["innererror"]["content_filter_result"]` (Singular). Responses API Fehler nutzen `error.body["content_filters"][0]["content_filter_results"]` (Plural, in einem Array). Der Schlüssel `innererror` existiert nicht mehr. Code, der direkt auf `innererror` zugreift, wirft zur Laufzeit einen `KeyError` — dies kann bei der Migration leicht übersehen werden, da es nur auftritt, wenn der Inhaltsfilter tatsächlich ausgelöst wird. Suchen Sie beim Migrieren immer nach `innererror`.
25. **Roh-HTTP-Aufrufe benötigen URL- und Body-Anpassung**: Apps, die Azure OpenAI REST direkt aufrufen (z. B. mit `requests`, `httpx`, `aiohttp`) und `/openai/deployments/{name}/chat/completions?api-version=...` verwenden, müssen zu `/openai/v1/responses` wechseln. Der Anfragetext nutzt `input` statt `messages`, benötigt `max_output_tokens` und `store`, und der `api-version` Query-Parameter wird entfernt. Der Antworttext befindet sich in `output[0].content[0].text` — **nicht** in `output_text`, das eine Komfort-Eigenschaft des SDK ist und im rohen REST JSON nicht vorhanden ist.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->