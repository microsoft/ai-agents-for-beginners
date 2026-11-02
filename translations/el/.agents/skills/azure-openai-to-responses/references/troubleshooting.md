# Επίλυση Προβλημάτων, Πίνακας Κινδύνου & Παγίδες

## Επίλυση Προβλημάτων 400s

| Σφάλμα | Διόρθωση |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Η ορισμός εργαλείου χρησιμοποιεί παλιά εμφωλευμένη μορφή Chat Completions | Απεμπλέξτε από `{"type": "function", "function": {"name": ...}}` σε `{"type": "function", "name": ..., "parameters": ...}` — το όνομα, η περιγραφή, και οι παράμετροι βρίσκονται σε ανώτερο επίπεδο |
| `unknown_parameter: input[N].tool_calls` | Αποτελέσματα εργαλείων πολλαπλών γύρων χρησιμοποιούν παλιά μορφή Chat Completions | Αντικαταστήστε `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` με αντικείμενα `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` εργαλείο χωρίς πίνακα `required` | Όταν `strict: true`, όλες οι ιδιότητες πρέπει να αναφέρονται στο `required` και το `additionalProperties: false` πρέπει να έχει οριστεί |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` εργαλείο χωρίς `additionalProperties: false` | Προσθέστε `"additionalProperties": false` στο αντικείμενο παραμέτρων |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Το πλήθος λίγων καλών κλήσεων έχει λάθος πρόθεμα | Τα IDs κλήσεων λειτουργιών πρέπει να ξεκινούν με `fc_` (π.χ., `fc_example1`), όχι με `call_` |
| `missing_required_parameter: text.format.name` | Προσθέστε το κλειδί `"name"` στον πίνακα μορφής (π.χ., `"name": "Output"`) |
| `invalid_type: text.format` | Βεβαιωθείτε ότι το `text.format` είναι αντικείμενο με κλειδιά `type`, `name`, `strict`, `schema` — και όχι μια συμβολοσειρά |
| `invalid input content type` | Χρησιμοποιήστε `input_text`/`output_text` τύπους περιεχομένου αντί για Chat `text` |
| `invalid input content type` (εικόνα) | Το περιεχόμενο εικόνας εξακολουθεί να χρησιμοποιεί `"type": "image_url"` | Αλλάξτε σε `"type": "input_image"` |
| `Expected object, got string` στο `image_url` | Το `image_url` εξακολουθεί να είναι εμφωλευμένο αντικείμενο `{"url": "..."}` | Απεμπλέξτε σε απλή συμβολοσειρά: `"image_url": "https://..."` ή `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` για `max_output_tokens` | Το ελάχιστο είναι **16** στο Azure OpenAI. Χρησιμοποιήστε 50+ για δοκιμές, 1000+ για παραγωγή. |
| `429 Too Many Requests` κατά τη ροή | Περιορισμός ρυθμού. Καλύψτε τη ροή με `try/except`, αποδώστε σφάλμα JSON στο frontend, εφαρμόστε backoff/επαναδοκιμή. |
| `KeyError: 'innererror'` σε σφάλμα φίλτρου περιεχομένου | Η δομή του σώματος σφάλματος φίλτρου περιεχομένου άλλαξε στην API Απαντήσεων | Τα Chat Completions χρησιμοποιούσαν `error.body["innererror"]["content_filter_result"]`; η API Απαντήσεων χρησιμοποιεί `error.body["content_filters"][0]["content_filter_results"]` (πληθυντικός, μέσα σε πίνακα). Επαναγράψτε κάθε πρόσβαση σε `innererror`. |

---

## Πίνακας Κινδύνου Μεταφοράς

| Σύμπτωμα | Πιθανό Λάθος | Διόρθωση |
|---------|---------------|-----|
| Κενό `output_text` / περικομμένη απάντηση | `max_output_tokens` πολύ χαμηλό για μοντέλα συλλογισμού | Ορίστε `max_output_tokens=1000` ή υψηλότερο — οι σύμβολα συλλογισμού μετρούν για το όριο |
| `400 invalid_type: text.format` | Πέρασε συμβολοσειρά `response_format` αντί για πίνακα `text.format` | Χρησιμοποιήστε `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` σε `/openai/v1/responses` | Λάθος `base_url` — λείπει το επίθημα `/openai/v1/` | Βεβαιωθείτε ότι `base_url=f"{endpoint}/openai/v1/"` (με τελικό slash) |
| `401 Unauthorized` μετά τη μετάβαση σε `OpenAI()` | Δεν έχει οριστεί `api_key` ή ο πάροχος token δεν περάστηκε σωστά | Για EntraID: `api_key=token_provider` (η callable). Για κλειδί API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Το μοντέλο επιστρέφει `deployment not found` | Η παράμετρος `model` δεν ταιριάζει με το όνομα ανάπτυξης Azure | Χρησιμοποιήστε `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — αυτό είναι το όνομα ανάπτυξης, όχι του μοντέλου |
| Το `json.loads(resp.output_text)` ρίχνει `JSONDecodeError` | Το σχήμα δεν επιβάλλεται ή το μοντέλο δεν υποστηρίζει αυστηρό JSON | Βεβαιωθείτε ότι υπάρχει `"strict": True` στο σχήμα και επιβεβαιώστε ότι το μοντέλο υποστηρίζει δομημένη έξοδο |
| Η ροή δεν παράγει κανένα γεγονός `delta` | Ελέγχετε λάθος τύπο γεγονότος | Φιλτράρετε με `event.type == "response.output_text.delta"`, όχι με `chat.completion.chunk` του Chat |
| Σφάλμα `400` σε είσοδο εικόνας μετά τη μεταφορά | Ο τύπος περιεχομένου εικόνας δεν έχει ενημερωθεί | Αλλάξτε `"type": "image_url"` σε `"type": "input_image"` και απεμπλέξτε `"image_url": {"url": "..."}` σε `"image_url": "..."` (απλή συμβολοσειρά) |
| Κλήσεις εργαλείων σε άπειρο βρόχο | Λείπει αποτέλεσμα εργαλείου στην επόμενη `input` | Μετά την εκτέλεση εργαλείου, προσθέστε ένα αντικείμενο `{"type": "function_call_output", "call_id": ..., "output": ...}` στην `input` του επόμενου αιτήματος |
| Σφάλμα `temperature` με GPT-5 ή o-series | Ρητή τιμή `temperature` διαφορετική του 1 | Αφαιρέστε το `temperature` ή ορίστε σε `1` για τα μοντέλα GPT-5 και o-series (o1, o3-mini, o3, o4-mini) |
| Σφάλμα `top_p` με o-series | Το `top_p` δεν υποστηρίζεται | Αφαιρέστε το `top_p` όταν στοχεύετε μοντέλα o-series |
| Το `max_completion_tokens` δεν αναγνωρίζεται | Χρήση παραμέτρου ειδικής για Azure | Αντικαταστήστε `max_completion_tokens` με `max_output_tokens`. Ορίστε 4096+ για o-series (οι σύμβολα συλλογισμού μετρούν για το όριο). |
| Κενή ή περικομμένη έξοδος από o-series | `max_output_tokens` πολύ χαμηλό | Η σειρά o-series χρησιμοποιεί εσωτερικά σύμβολα συλλογισμού. Ορίστε `max_output_tokens=4096` ή υψηλότερο — όχι 500–1000. |
| `400 integer_below_min_value` για `max_output_tokens` | Τιμή μικρότερη από 16 | Το Azure OpenAI επιβάλλει `max_output_tokens >= 16`. Χρησιμοποιήστε 50+ για δοκιμές καπνού, 1000+ για παραγωγή. |
| `429 Too Many Requests` κατά τη ροή | Περιορισμός ρυθμού από Azure OpenAI | Η ροή διακόπτεται αθόρυβα χωρίς χειρισμό σφάλματος. Πάντα καλύψτε το `async for event in await coroutine:` με `try/except` και δώστε `{"error": str(e)}` στο frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Λάθος tenant ή μη σύνδεση | Περάστε ρητά `tenant_id=os.getenv("AZURE_TENANT_ID")`. Εκτελέστε τοπικά `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` με χρήση GitHub Models (`models.github.ai`) | Τα GitHub Models δεν υποστηρίζουν την API Απαντήσεων | Αφαιρέστε τελείως τη διαδρομή κώδικα για GitHub Models. Χρησιμοποιήστε Azure OpenAI, OpenAI, ή συμβατό τοπικό endpoint (π.χ., Ollama με υποστήριξη Απαντήσεων). |
| MAF `OpenAIChatCompletionClient` ακόμα χρησιμοποιεί Chat Completions | Χρήση παλαιού πελάτη MAF στην έκδοση 1.0.0+ | Στο MAF 1.0.0+, ο `OpenAIChatClient` χρησιμοποιεί από προεπιλογή την API Απαντήσεων. Αντικαταστήστε `OpenAIChatCompletionClient` με `OpenAIChatClient`. Για πριν την 1.0.0, αναβαθμίστε σε `agent-framework-openai>=1.0.0`. |
| Ο πράκτορας LangChain επιστρέφει κενό ή αποτυγχάνει με κλήσεις εργαλείων | Το `ChatOpenAI` δεν χρησιμοποιεί την API Απαντήσεων | Προσθέστε `use_responses_api=True` στο `ChatOpenAI(...)`. Επίσης αλλάξτε το `.content` σε `.text` στα μηνύματα της απόκρισης. |
| `KeyError: 'innererror'` στον χειριστή σφαλμάτων φίλτρου περιεχομένου | Η δομή σώματος σφάλματος άλλαξε στην API Απαντήσεων | Επαναγράψτε `error.body["innererror"]["content_filter_result"]["jailbreak"]` σε `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Ο περιτύλιγμα `innererror` δεν υπάρχει πια· οι λεπτομέρειες φίλτρου περιεχομένου είναι τώρα σε πίνακα κορυφαίου επιπέδου `content_filters` με `content_filter_results` (πληθυντικό) μέσα σε κάθε εγγραφή. |
| Ακατέργαστο HTTP αίτημα σε `/openai/deployments/.../chat/completions` επιστρέφει 404 | Παλαιό REST endpoint Chat Completions | Επαναγράψτε το URL σε `/openai/v1/responses`. Αλλάξτε σώμα αιτήματος: `messages` → `input`, προσθέστε `max_output_tokens` + `store: false`, αφαιρέστε το query param `api-version`. Αλλάξτε ανάλυση απόκρισης: `choices[0].message.content` → `output[0].content[0].text` (σημείωση: το `output_text` είναι μια ιδιότητα ευκολίας SDK, όχι στο ακατέργαστο JSON REST). |

---

## Παγίδες

1. Αν προηγουμένως χρησιμοποιούσατε Chat Completions για κατάσταση συνομιλίας, διαχειριστείτε ρητά τη δική σας κατάσταση με Responses.
2. Προτιμήστε `max_output_tokens` αντί του παλαιού `max_tokens`.
3. Κατά τη μετανάστευση στο `gpt-5`, βεβαιωθείτε ότι το `temperature` δεν καθορίζεται ή έχει οριστεί σε `1`.
4. Αντικαταστήστε τον Chat τύπο `content[].type: "text"` με τον Responses τύπο `content[].type: "input_text"` για εισόδους χρήστη/συστήματος.
5. Για το `text.format`, παρέχετε σωστό πίνακα (π.χ., `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), όχι απλή συμβολοσειρά.
6. Η παράμετρος `seed` δεν υποστηρίζεται στις Responses· αφαιρέστε την από τα αιτήματα.
7. **Συλλογισμός**: Συμπεριλάβετε το `reasoning` μόνο αν ο αρχικός κώδικας το χρησιμοποιούσε ήδη. Μη προσθέτετε `reasoning` σε κλήσεις API όπου δεν υπήρχε — πολλά μη συλλογιστικά μοντέλα δεν το υποστηρίζουν.
8. **Μέγεθος `max_output_tokens`**: Για μοντέλα συλλογισμού (GPT-5-mini, GPT-5, o-series), χρησιμοποιήστε `max_output_tokens=4096` ή υψηλότερο — όχι 50–1000. Το μοντέλο χρησιμοποιεί εσωτερικά σύμβολα συλλογισμού πριν την ορατή έξοδο· τα πολύ χαμηλά όρια προκαλούν περικομμένες ή κενές απαντήσεις.
9. **`max_completion_tokens` στην o-series**: Αν ο αρχικός κώδικας χρησιμοποίησε `max_completion_tokens` (ειδικό για Azure o-series), αντικαταστήστε με `max_output_tokens`. Η API Απαντήσεων δεν δέχεται `max_completion_tokens`.
10. **`reasoning_effort` στην o-series**: Αν ο αρχικός κώδικας χρησιμοποιεί `reasoning_effort` (χαμηλό/μεσαίο/υψηλό), μετατρέψτε το σε `reasoning={"effort": "<τιμή>"}` στην κλήση API Απαντήσεων.
11. **Καθυστέρηση ροής στην o-series**: Τα μοντέλα o-series πραγματοποιούν εσωτερικό συλλογισμό πριν παραγάγουν έξοδο. Κατά τη ροή, να αναμένετε μεγαλύτερη καθυστέρηση πριν το πρώτο γεγονός `response.output_text.delta`. Αυτό είναι φυσιολογικό — το μοντέλο συλλογίζεται, δεν έχει παγώσει.
9. **Το `_azure_ad_token_provider` έχει φύγει**: Τα `AsyncOpenAI` / `OpenAI` δεν έχουν το χαρακτηριστικό `_azure_ad_token_provider`. Δοκιμές ή κώδικας που το προσπελαύνουν θα αποτύχουν με `AttributeError`. Ο πάροχος token περνάει ως `api_key` και δεν είναι επιθεωρήσιμος από το αντικείμενο πελάτη.
10. **Αρχεία στιγμιοτύπου / golden files**: Αν το σύνολο δοκιμών χρησιμοποιεί snapshot testing, **όλα** τα αρχεία στιγμιοτύπου που περιέχουν σχήματα streaming Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, κλπ.) πρέπει να ενημερωθούν στο νέο σχήμα Responses. Αυτό είναι εύκολο να διαφύγει και προκαλεί αποτυχίες assertions στιγμιοτύπου.
11. **Διαδρομή mock monkeypatch**: Ο στόχος monkeypatch αλλάζει από `openai.resources.chat.AsyncCompletions.create` σε `openai.resources.responses.AsyncResponses.create` (ή `Responses.create` για συγχρονισμό). Η χρήση της παλιάς διαδρομής είναι αθόρυβη και δεν παρεμβάλλεται — το mock δεν αναχαιτίζει και οι δοκιμές χτυπούν την πραγματική API ή αποτυγχάνουν.
12. **`input` όχι `messages`**: Οι mock συναρτήσεις πρέπει να διαβάζουν `kwargs.get("input")` όχι `kwargs.get("messages")`. Η API Απαντήσεων χρησιμοποιεί `input` για το ιστορικό συνομιλίας.
13. **Ονομασία μεταβλητής περιβάλλοντος**: Το Azure Identity SDK χρησιμοποιεί `AZURE_CLIENT_ID` (όχι `AZURE_OPENAI_CLIENT_ID`) για το `ManagedIdentityCredential(client_id=...)`. Μετονομάστε σε δοκιμές, αρχεία `.env`, ρυθμίσεις εφαρμογής, και Bicep/υποδομή.
14. **Το ελάχιστο `max_output_tokens` είναι 16**: Το Azure OpenAI απορρίπτει τιμές κάτω από 16 με `400 integer_below_min_value`. Χρησιμοποιήστε `50` για δοκιμές καπνού, `1000`+ για παραγωγή. Το παλιό `max_tokens` δεν είχε τέτοιο ελάχιστο.
15. **`tenant_id` για `AzureDeveloperCliCredential`**: Όταν ο πόρος Azure OpenAI είναι σε διαφορετικό tenant, **πρέπει** να περάσετε ρητά το `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Χωρίς αυτό, το διαπιστευτήριο χρησιμοποιεί αθόρυβα λάθος tenant και επιστρέφει `401`.
16. **Τα όρια ρυθμού εμφανίζονται διαφορετικά στη ροή**: Με τα Chat Completions, το 429 συνήθως απέτρεπε την έναρξη της ροής. Με τη ροή API Απαντήσεων, ένα 429 μπορεί να συμβεί **κατά τη διάρκεια της ροής** — ο ασύγχρονος επαναλήπτης ρίχνει εξαίρεση. Πάντα καλύπττε το βρόχο ροής με `try/except` και αποδώστε μια γραμμή JSON σφάλματος ώστε το frontend να το χειριστεί ομαλά.

17. **Η διαχείριση σφαλμάτων streaming είναι υποχρεωτική για εφαρμογές ιστού**: Το πρότυπο `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` είναι κρίσιμο. Χωρίς αυτό, το ρεύμα SSE/JSONL σταματά αθόρυβα σε οποιοδήποτε σφάλμα στην πλευρά του διακομιστή και το frontend παγώνει.
18. **Οι ορισμοί εργαλείων πρέπει να χρησιμοποιούν επίπεδη μορφή**: Το Responses API αναμένει `{"type": "function", "name": ..., "parameters": ...}` — όχι τη φωλιασμένη μορφή του Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Αυτό είναι το πιο συνηθισμένο σφάλμα μετανάστευσης για κώδικα που καλεί συναρτήσεις.
19. **Το `pydantic_function_tool()` δεν είναι συμβατό**: Η βοηθητική συνάρτηση `openai.pydantic_function_tool()` εξακολουθεί να παράγει την παλιά φωλιασμένη μορφή. Μην τη χρησιμοποιείτε με `responses.create()`. Ορίστε τα σχήματα εργαλείων χειροκίνητα ή ισιώστε την έξοδο.
20. **Τα αποτελέσματα εργαλείων χρησιμοποιούν `function_call_output`, όχι `role: tool`**: Μετά την εκτέλεση ενός εργαλείου, προσθέστε `{"type": "function_call_output", "call_id": ..., "output": ...}` — όχι `{"role": "tool", "tool_call_id": ..., "content": ...}`. Για το αίτημα εργαλείου του βοηθού, χρησιμοποιήστε `messages.extend(response.output)` — όχι χειροκίνητο λεξικό `{"role": "assistant", "tool_calls": [...]}`.
21. **Το `strict: true` απαιτεί `required` + `additionalProperties: false`**: Όταν χρησιμοποιείτε `strict: true` σε εργαλείο, κάθε ιδιότητα πρέπει να περιλαμβάνεται στον πίνακα `required` και το `additionalProperties` πρέπει να είναι `false`. Η έλλειψη οποιουδήποτε προκαλεί σφάλμα 400.
22. **Τα IDs κλήσεων συναρτήσεων έχουν συγκεκριμένα προθέματα**: Όταν παρέχετε λίγα αντικείμενα `function_call` στο `input`, το πεδίο `id` πρέπει να ξεκινά με `fc_` και το πεδίο `call_id` πρέπει να ξεκινά με `call_` (π.χ. `"id": "fc_example1", "call_id": "call_example1"`). Η χρήση του παλιού Chat Completions προθέματος `call_` για το `id` απορρίπτεται.
23. **Το GitHub Models δεν υποστηρίζει το Responses API**: Εάν η εφαρμογή έχει κώδικα GitHub Models (`base_url` που δείχνει σε `models.github.ai` ή `models.inference.ai.azure.com`), αφαιρέστε τον εντελώς. Δεν υπάρχει μονοπάτι μετανάστευσης — μεταβείτε σε Azure OpenAI, OpenAI ή συμβατό τοπικό endpoint.
24. **Η δομή σώματος σφάλματος φίλτρου περιεχομένου άλλαξε**: Τα σφάλματα Chat Completions χρησιμοποιούσαν `error.body["innererror"]["content_filter_result"]` (ενικός). Τα σφάλματα Responses API χρησιμοποιούν `error.body["content_filters"][0]["content_filter_results"]` (πληθυντικός, μέσα σε πίνακα). Το κλειδί `innererror` δεν υπάρχει πια. Κώδικας που προσπελαύνει απευθείας το `innererror` θα προκαλέσει `KeyError` κατά την εκτέλεση — αυτό είναι εύκολο να παραλειφθεί στη μετανάστευση επειδή εμφανίζεται μόνο όταν ενεργοποιείται το φίλτρο περιεχομένου. Πάντα ψάχνετε για `innererror` κατά τη μετανάστευση.
25. **Οι ακατέργαστες κλήσεις HTTP χρειάζονται αναθεώρηση URL + σώματος**: Εφαρμογές που καλούν απευθείας το Azure OpenAI REST (μέσω `requests`, `httpx`, `aiohttp`) χρησιμοποιώντας `/openai/deployments/{name}/chat/completions?api-version=...` πρέπει να μεταβούν σε `/openai/v1/responses`. Το σώμα του αιτήματος χρησιμοποιεί `input` αντί για `messages`, απαιτεί `max_output_tokens` και `store`, και η παράμετρος ερωτήματος `api-version` αφαιρείται. Το κείμενο της απόκρισης είναι στο `output[0].content[0].text` — **όχι** στο `output_text`, το οποίο είναι ιδιότητα ευκολίας SDK που δεν υπάρχει στο ακατέργαστο REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->