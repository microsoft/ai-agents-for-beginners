# Αντιμετώπιση προβλημάτων, Πίνακας Κινδύνων & Προσοχές

## Αντιμετώπιση προβλημάτων 400s

| Σφάλμα | Διόρθωση |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Ο ορισμός εργαλείου χρησιμοποιεί παλιά εμφωλευμένη μορφή Chat Completions | Απλοποιήστε από `{"type": "function", "function": {"name": ...}}` σε `{"type": "function", "name": ..., "parameters": ...}` — το name, description, parameters μπαίνουν στο ανώτερο επίπεδο |
| `unknown_parameter: input[N].tool_calls` | Τα αποτελέσματα εργαλείων πολλαπλών βημάτων χρησιμοποιούν παλιά μορφή Chat Completions | Αντικαταστήστε `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` με αντικείμενα `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Εργαλείο με `strict: true` που λείπει το `required` array | Όταν `strict: true`, όλες οι ιδιότητες πρέπει να αναφέρονται στο `required` και πρέπει να οριστεί `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | Εργαλείο με `strict: true` που λείπει `additionalProperties: false` | Προσθέστε `"additionalProperties": false` στο αντικείμενο παραμέτρων |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Το ID κλήσης function_call λίγων παραδειγμάτων έχει λάθος πρόθεμα | Τα ID κλήσεων πρέπει να αρχίζουν με `fc_` (π.χ. `fc_example1`), όχι με `call_` |
| `missing_required_parameter: text.format.name` | Προσθέστε κλειδί `"name"` στο λεξικό format (π.χ. `"name": "Output"`) |
| `invalid_type: text.format` | Βεβαιωθείτε ότι το `text.format` είναι λεξικό με τα κλειδιά `type`, `name`, `strict`, `schema` — όχι συμβολοσειρά |
| `invalid input content type` | Χρησιμοποιήστε τους τύπους περιεχομένου `input_text`/`output_text` αντί για Chat `text` |
| `invalid input content type` (εικόνα) | Το περιεχόμενο εικόνας συνεχίζει να χρησιμοποιεί `"type": "image_url"` | Αλλάξτε σε `"type": "input_image"` |
| `Expected object, got string` στο `image_url` | Το `image_url` είναι ακόμη εμφωλευμένο αντικείμενο `{"url": "..."}` | Απλοποιήστε σε απλή συμβολοσειρά: `"image_url": "https://..."` ή `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` για `max_output_tokens` | Ελάχιστο είναι **16** στο Azure OpenAI. Χρησιμοποιήστε 50+ για δοκιμές, 1000+ για παραγωγή. |
| `429 Too Many Requests` κατά το streaming | Περιορισμός ρυθμού. Περιτυλίξτε το streaming με `try/except`, επιστρέψτε JSON σφάλματος στο frontend, εφαρμόστε backoff/retry. |
| `KeyError: 'innererror'` σε σφάλμα φίλτρου περιεχομένου | Αλλάχτηκε η δομή σώματος σφάλματος φίλτρου περιεχομένου στο Responses API | Chat Completions χρησιμοποιούσε `error.body["innererror"]["content_filter_result"]`; Responses API χρησιμοποιεί `error.body["content_filters"][0]["content_filter_results"]` (πληθυντικός, μέσα σε πίνακα). Αναγράψτε ξανά όλες τις προσβάσεις `innererror`. |

---

## Πίνακας Κινδύνων Μετάβασης

| Σύμπτωμα | Πιθανό Λάθος | Διόρθωση |
|---------|---------------|-----|
| Άδειο `output_text` / κομμένη απάντηση | `max_output_tokens` πολύ χαμηλό για μοντέλα λογικής | Ορίστε `max_output_tokens=1000` ή μεγαλύτερο — τα tokens λογικής μετράνε στο όριο |
| `400 invalid_type: text.format` | Πέρασε `response_format` συμβολοσειρά αντί για `text.format` λεξικό | Χρησιμοποιήστε `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` στο `/openai/v1/responses` | Λάθος `base_url` — λείπει το `/openai/v1/` στο τέλος | Βεβαιωθείτε `base_url=f"{endpoint}/openai/v1/"` (με τελικό slash) |
| `401 Unauthorized` μετά τη μετάβαση σε `OpenAI()` | Δεν έχει οριστεί το `api_key` ή ο πάροχος token δεν περάστηκε σωστά | Για EntraID: `api_key=token_provider` (η callable). Για API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Το μοντέλο επιστρέφει `deployment not found` | Η παράμετρος `model` δεν ταιριάζει με το όνομα του Azure deployment σας | Χρησιμοποιήστε `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — αυτό είναι το όνομα του deployment, όχι του μοντέλου |
| `json.loads(resp.output_text)` δημιουργεί `JSONDecodeError` | Δεν εφαρμόζεται το σχήμα ή το μοντέλο δεν υποστηρίζει αυστηρό JSON | Βεβαιωθείτε ότι υπάρχει `"strict": True` στο σχήμα, και επιβεβαιώστε ότι το μοντέλο υποστηρίζει δομημένη έξοδο |
| Streaming δεν επιστρέφει `delta` events | Ελέγχετε λάθος τύπο event | Φιλτράρετε με `event.type == "response.output_text.delta"` και όχι με Chat `chat.completion.chunk` |
| `400` σφάλμα στην είσοδο εικόνας μετά τη μετάβαση | Δεν ανανεώθηκε ο τύπος περιεχομένου εικόνας | Αλλάξτε `"type": "image_url"` → `"type": "input_image"` και απλοποιήστε `"image_url": {"url": "..."}` → `"image_url": "..."` (απλή συμβολοσειρά) |
| Κλήσεις εργαλείων σε ατέρμονα βρόχο | Λείπει το αποτέλεσμα εργαλείου στην επόμενη `input` | Μετά την εκτέλεση εργαλείου, προσθέστε ένα αντικείμενο `{"type": "function_call_output", "call_id": ..., "output": ...}` στην επόμενη `input` |
| Σφάλμα `temperature` με GPT-5 ή o-series | Ρητή τιμή `temperature` διαφορετική του 1 | Αφαιρέστε το `temperature` ή ορίστε το σε `1` για μοντέλα GPT-5 και o-series (o1, o3-mini, o3, o4-mini) |
| Σφάλμα `top_p` με o-series | Το `top_p` δεν υποστηρίζεται | Αφαιρέστε το `top_p` όταν στοχεύετε μοντέλα o-series |
| `max_completion_tokens` δεν αναγνωρίζεται | Χρήση παραμέτρου ειδικής για Azure | Αντικαταστήστε `max_completion_tokens` με `max_output_tokens`. Ορίστε 4096+ για o-series (τα tokens λογικής μετράνε στο όριο). |
| Άδεια/κομμένη έξοδος από o-series | Το `max_output_tokens` είναι πολύ χαμηλό | Τα o-series χρησιμοποιούν tokens λογικής εσωτερικά. Ορίστε `max_output_tokens=4096` ή πάνω — όχι 500–1000. |
| `400 integer_below_min_value` για `max_output_tokens` | Τιμή κάτω από 16 | Το Azure OpenAI απαιτεί `max_output_tokens >= 16`. Χρησιμοποιήστε 50+ για δοκιμές καπνού, 1000+ για παραγωγή. |
| `429 Too Many Requests` στη μέση του streaming | Περιορισμός ρυθμού από Azure OpenAI | Το stream σπάει αθόρυβα χωρίς χειρισμό σφάλματος. Περιτυλίξτε πάντα το `async for event in await coroutine:` με `try/except` και επιστρέψτε `{"error": str(e)}` στο frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Λάθος tenant ή μη σύνδεση | Δώστε ρητά `tenant_id=os.getenv("AZURE_TENANT_ID")`. Τρέξτε `azd auth login --tenant <tenant-id>` τοπικά. |
| `404 Not Found` με GitHub Models (`models.github.ai`) | Τα GitHub Models δεν υποστηρίζουν το Responses API | Αφαιρέστε εντελώς τον κώδικα GitHub Models. Χρησιμοποιήστε Azure OpenAI, OpenAI ή συμβατό τοπικό endpoint (π.χ. Ollama με υποστήριξη Responses). |
| MAF `OpenAIChatCompletionClient` χρησιμοποιεί ακόμα Chat Completions | Χρήση παλαιού MAF client μετά την έκδοση 1.0.0+ | Στο MAF 1.0.0+, ο `OpenAIChatClient` χρησιμοποιεί το Responses API από προεπιλογή. Αντικαταστήστε `OpenAIChatCompletionClient` με `OpenAIChatClient`. Για προ 1.0.0, αναβαθμίστε σε `agent-framework-openai>=1.0.0`. |
| Ο πράκτορας LangChain επιστρέφει άδειο ή αποτυγχάνει με κλήσεις εργαλείων | To `ChatOpenAI` δεν χρησιμοποιεί το Responses API | Προσθέστε `use_responses_api=True` στο `ChatOpenAI(...)`. Αλλάξτε επίσης `.content` → `.text` στα μηνύματα απόκρισης. |
| `KeyError: 'innererror'` στον χειριστή σφάλματος φίλτρου περιεχομένου | Αλλάχτηκε η δομή σώματος σφάλματος στο Responses API | Αναγράψτε `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Ο περιτύλιγμα `innererror` έχει φύγει. Οι λεπτομέρειες φίλτρου είναι πλέον σε πίνακα `content_filters` με `content_filter_results` (πληθυντικός) σε κάθε καταχώρηση. |
| Ακατέργαστο HTTP κλήση σε `/openai/deployments/.../chat/completions` επιστρέφει 404 | Παλιό REST endpoint Chat Completions | Αναγράψτε ξανά το URL σε `/openai/v1/responses`. Αλλάξτε το σώμα αιτήματος: `messages` → `input`, προσθέστε `max_output_tokens` + `store: false`, αφαιρέστε το query param `api-version`. Αλλάξτε ανάλυση απόκρισης: `choices[0].message.content` → `output[0].content[0].text` (σημείωση: το `output_text` είναι βοηθητική ιδιότητα SDK, όχι στο ακατέργαστο JSON REST). |

---

## Προσοχές

1. Αν χρησιμοποιούσατε παλαιότερα τα Chat Completions για την κατάσταση συνομιλίας, διαχειριστείτε την κατάσταση ρητά με το Responses.
2. Προτιμήστε `max_output_tokens` αντί για το παλιό `max_tokens`.
3. Κατά τη μετάβαση στο `gpt-5`, βεβαιωθείτε ότι το `temperature` δεν ορίζεται ή είναι 1.
4. Αντικαταστήστε Chat `content[].type: "text"` με Responses `content[].type: "input_text"` για εισόδους χρήστη/συστήματος.
5. Για `text.format`, παρέχετε ένα σωστό λεξικό (π.χ. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), όχι απλή συμβολοσειρά.
6. Η παράμετρος `seed` δεν υποστηρίζεται στο Responses· αφαιρέστε την από τα αιτήματα.
7. **Λογική (Reasoning)**: Συμπεριλάβετε το `reasoning` μόνο εάν ο αρχικός κώδικας το χρησιμοποιούσε ήδη. Μην προσθέτετε `reasoning` σε κλήσεις API που δεν το είχαν — πολλά μοντέλα (π.χ. gpt-4o-mini) δεν το υποστηρίζουν.
8. **Μέγεθος `max_output_tokens`**: Για μοντέλα λογικής (GPT-5-mini, GPT-5, o-series), χρησιμοποιήστε `max_output_tokens=4096` ή μεγαλύτερο — όχι 50–1000. Το μοντέλο χρησιμοποιεί tokens λογικής εσωτερικά πριν παράγει ορατή έξοδο. Πολύ χαμηλά όρια προκαλούν κομμένες ή άδειες απαντήσεις.
9. **O-series `max_completion_tokens`**: Αν ο αρχικός κώδικας χρησιμοποιούσε `max_completion_tokens` (ειδικό για Azure o-series), αντικαταστήστε το με `max_output_tokens`. Το Responses API δεν δέχεται `max_completion_tokens`.
10. **O-series `reasoning_effort`**: Αν ο αρχικός κώδικας χρησιμοποιεί `reasoning_effort` (χαμηλό/μεσαίο/υψηλό), μεταφέρετέ το σε `reasoning={"effort": "<τιμή>"}` στην κλήση του Responses API.
11. **Καθυστέρηση streaming σε o-series**: Τα μοντέλα o-series κάνουν εσωτερική λογική πριν παράγουν έξοδο. Όταν γίνεται streaming, αναμένεται μεγαλύτερη καθυστέρηση πριν το πρώτο event `response.output_text.delta`. Αυτό είναι φυσιολογικό — το μοντέλο επεξεργάζεται, δεν έχει κολλήσει.
9. **Το `_azure_ad_token_provider` έχει αφαιρεθεί**: Τα `AsyncOpenAI` / `OpenAI` δεν έχουν το χαρακτηριστικό `_azure_ad_token_provider`. Οι δοκιμές ή κώδικας που το προσπελαύνουν θα αποτύχουν με `AttributeError`. Ο πάροχος token περνάει ως `api_key` και δεν είναι προσβάσιμος από το αντικείμενο client.
10. **Αρχεία snapshot / golden files**: Αν το σύνολο δοκιμών χρησιμοποιεί snapshot testing, **όλα** τα αρχεία snapshot που περιέχουν σχήματα streaming Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, κ.ά.) πρέπει να ενημερωθούν στο νέο σχήμα Responses. Αυτό είναι εύκολο να παραβλεφθεί και προκαλεί αποτυχίες assertions στα snapshots.
11. **Mock monkeypatch path**: Ο στόχος monkeypatch αλλάζει από `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (ή `Responses.create` για συγχρονισμό). Η χρήση του παλιού μονοπατιού δεν κάνει τίποτα αθόρυβα — το mock δεν θα παρεμβαίνει και οι δοκιμές θα χτυπήσουν το πραγματικό API ή θα αποτύχουν.
12. **`input` όχι `messages`**: Οι mock συναρτήσεις πρέπει να διαβάζουν `kwargs.get("input")` όχι `kwargs.get("messages")`. Το Responses API χρησιμοποιεί `input` για το ιστορικό συνομιλίας.
13. **Ονομασία περιβαλλοντικής μεταβλητής**: Το Azure Identity SDK χρησιμοποιεί `AZURE_CLIENT_ID` (όχι `AZURE_OPENAI_CLIENT_ID`) για το `ManagedIdentityCredential(client_id=...)`. Μετονομάστε στις δοκιμές, αρχεία `.env`, ρυθμίσεις εφαρμογής και Bicep/infra.
14. **Ελάχιστο `max_output_tokens` είναι 16**: Το Azure OpenAI απορρίπτει τιμές κάτω από 16 με `400 integer_below_min_value`. Χρησιμοποιήστε `50` για δοκιμές καπνού, `1000`+ για παραγωγή. Το παλιό `max_tokens` δεν είχε τέτοιο ελάχιστο.
15. **`tenant_id` για `AzureDeveloperCliCredential`**: Όταν ο πόρος Azure OpenAI είναι σε διαφορετικό tenant, **πρέπει** να περάσετε ρητά το `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Χωρίς αυτό, το credential αθόρυβα χρησιμοποιεί λάθος tenant και επιστρέφει `401`.
16. **Τα όρια ρυθμού εμφανίζονται διαφορετικά σε streaming**: Με Chat Completions, το 429 συνήθως εμπόδιζε την εκκίνηση του stream. Με το Responses API streaming, ένα 429 μπορεί να εμφανιστεί **μέσα στο stream** — ο ασύγχρονος επαναληπτικός εγείρει εξαίρεση. Περιτυλίξτε πάντα τον βρόχο streaming σε `try/except` και επιστρέψτε μια γραμμή JSON σφάλματος ώστε το frontend να το διαχειρίζεται ομαλά.
17. **Η διαχείριση σφαλμάτων ροής είναι υποχρεωτική για τις web εφαρμογές**: Το μοτίβο `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` είναι κρίσιμο. Χωρίς αυτό, το SSE/JSONL stream πεθαίνει σιωπηλά σε οποιοδήποτε σφάλμα στην πλευρά του διακομιστή και το frontend κολλάει.
18. **Οι ορισμοί εργαλείων πρέπει να χρησιμοποιούν το επίπεδο format**: Το Responses API αναμένει `{"type": "function", "name": ..., "parameters": ...}` — όχι το nested `{"type": "function", "function": {"name": ..., "parameters": ...}}` του Chat Completions. Αυτό είναι το πιο κοινό λάθος μετανάστευσης για τον κώδικα κλήσης συναρτήσεων.
19. **`pydantic_function_tool()` δεν είναι συμβατό**: Ο βοηθός `openai.pydantic_function_tool()` εξακολουθεί να δημιουργεί το παλιό nested format. Μην τον χρησιμοποιείτε με `responses.create()`. Ορίστε χειροκίνητα τα σχήματα εργαλείων ή απλώστε το αποτέλεσμα.
20. **Τα αποτελέσματα εργαλείων χρησιμοποιούν `function_call_output`, όχι `role: tool`**: Μετά την εκτέλεση ενός εργαλείου, προσθέστε `{"type": "function_call_output", "call_id": ..., "output": ...}` — όχι `{"role": "tool", "tool_call_id": ..., "content": ...}`. Για το αίτημα εργαλείου του βοηθού, χρησιμοποιήστε `messages.extend(response.output)` — όχι το χειροκίνητο λεξικό `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` απαιτεί `required` + `additionalProperties: false`**: Όταν χρησιμοποιείτε `strict: true` σε ένα εργαλείο, κάθε ιδιότητα πρέπει να αναφέρεται στον πίνακα `required` και το `additionalProperties` να είναι `false`. Η παράλειψη οποιουδήποτε προκαλεί σφάλμα 400.
22. **Τα IDs των κλήσεων συναρτήσεων έχουν συγκεκριμένα προθέματα**: Όταν παρέχετε λίγα αντικείμενα `function_call` στο `input`, το πεδίο `id` πρέπει να αρχίζει με `fc_` και το πεδίο `call_id` με `call_` (π.χ., `"id": "fc_example1", "call_id": "call_example1"`). Η χρήση του παλιού προθέματος `call_` για το `id` στο Chat Completions απορρίπτεται.
23. **Το GitHub Models δεν υποστηρίζει το Responses API**: Αν η εφαρμογή έχει διαδρομή κώδικα GitHub Models (`base_url` προς `models.github.ai` ή `models.inference.ai.azure.com`), αφαιρέστε την εντελώς. Δεν υπάρχει μονοπάτι μετανάστευσης — μεταβείτε σε Azure OpenAI, OpenAI ή συμβατό τοπικό endpoint.
24. **Αλλάζει η δομή του σώματος του σφάλματος φίλτρου περιεχομένου**: Τα σφάλματα Chat Completions χρησιμοποιούσαν `error.body["innererror"]["content_filter_result"]` (ενικός). Τα σφάλματα Responses API χρησιμοποιούν `error.body["content_filters"][0]["content_filter_results"]` (πολυπληθυντικός, μέσα σε πίνακα). Το κλειδί `innererror` δεν υπάρχει πλέον. Ο κώδικας που προσπελαύνει απευθείας το `innererror` θα προκαλέσει `KeyError` κατά το runtime — αυτό είναι εύκολο να παραβλεφθεί στη μετανάστευση, καθώς εμφανίζεται μόνο όταν ενεργοποιείται το φίλτρο περιεχομένου. Πάντα ψάχνετε για `innererror` κατά τη μετανάστευση.
25. **Οι άμεσες HTTP κλήσεις απαιτούν επανεγγραφή URL + σώματος**: Εφαρμογές που καλούν άμεσα το Azure OpenAI REST (μέσω `requests`, `httpx`, `aiohttp`) χρησιμοποιώντας `/openai/deployments/{name}/chat/completions?api-version=...` πρέπει να αλλάξουν σε `/openai/v1/responses`. Το σώμα του αιτήματος χρησιμοποιεί `input` αντί για `messages`, απαιτεί `max_output_tokens` και `store`, και το query param `api-version` αφαιρείται. Το κείμενο του σώματος της απόκρισης βρίσκεται στο `output[0].content[0].text` — **όχι** στο `output_text`, που είναι ιδιότητα διευκόλυνσης SDK και δεν υπάρχει στο ακατέργαστο REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->