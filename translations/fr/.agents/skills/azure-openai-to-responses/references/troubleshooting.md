# Dépannage, Tableau des risques & Pièges

## Dépannage des erreurs 400

| Erreur | Correction |
|-------|-----|
| `missing_required_parameter: tools[0].name` | La définition de l'outil utilise l'ancien format imbriqué Chat Completions | Aplatir de `{"type": "function", "function": {"name": ...}}` à `{"type": "function", "name": ..., "parameters": ...}` — les champs name, description, parameters doivent être au niveau supérieur |
| `unknown_parameter: input[N].tool_calls` | Les résultats d'outils multi-tours utilisent l'ancien format Chat Completions | Remplacer `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` par des éléments `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Outil `strict: true` sans tableau `required` | Quand `strict: true`, toutes les propriétés doivent être listées dans `required` et `additionalProperties: false` doit être défini |
| `invalid_function_parameters: 'additionalProperties' is required` | Outil `strict: true` sans `additionalProperties: false` | Ajouter `"additionalProperties": false` à l'objet des paramètres |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | L'ID function_call few-shot a un mauvais préfixe | Les IDs des appels de fonction doivent commencer par `fc_` (ex. `fc_example1`), pas par `call_` |
| `missing_required_parameter: text.format.name` | Ajouter la clé `"name"` au dictionnaire format (ex. `"name": "Output"`) |
| `invalid_type: text.format` | Vérifier que `text.format` est un dict avec les clés `type`, `name`, `strict`, `schema` — pas une chaîne de caractères |
| `invalid input content type` | Utiliser les types de contenu `input_text`/`output_text` au lieu de Chat `text` |
| `invalid input content type` (image) | Le contenu image utilise encore `"type": "image_url"` | Changer en `"type": "input_image"` |
| `Expected object, got string` sur `image_url` | `image_url` est encore un objet imbriqué `{"url": "..."}` | Aplatir en une simple chaîne : `"image_url": "https://..."` ou `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` pour `max_output_tokens` | Le minimum est **16** sur Azure OpenAI. Utiliser 50+ pour les tests, 1000+ en production. |
| `429 Too Many Requests` pendant le streaming | Limité par le taux. Envelopper le streaming dans un `try/except`, émettre une JSON d'erreur au frontend, implémenter backoff/retry. |
| `KeyError: 'innererror'` sur erreur filtre de contenu | La structure du corps de l'erreur du filtre de contenu a changé dans l'API Responses | Chat Completions utilisait `error.body["innererror"]["content_filter_result"]`; Responses API utilise `error.body["content_filters"][0]["content_filter_results"]` (pluriel, dans un tableau). Réécrire tous les accès `innererror`. |

---

## Tableau des risques de migration

| Symptôme | Erreur probable | Correction |
|---------|---------------|-----|
| `output_text` vide / réponse tronquée | `max_output_tokens` trop bas pour les modèles de raisonnement | Mettre `max_output_tokens=1000` ou plus — les tokens de raisonnement comptent dans la limite |
| `400 invalid_type: text.format` | Passage de la chaîne `response_format` au lieu du dict `text.format` | Utiliser `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` sur `/openai/v1/responses` | Mauvais `base_url` — suffixe `/openai/v1/` manquant | S'assurer que `base_url=f"{endpoint}/openai/v1/"` (avec barre oblique finale) |
| `401 Unauthorized` après passage à `OpenAI()` | `api_key` non défini ou fournisseur de token mal passé | Pour EntraID : `api_key=token_provider` (le callable). Pour clef API : `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Le modèle retourne `deployment not found` | Le paramètre `model` ne correspond pas au nom de déploiement Azure | Utiliser `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — c'est le nom du déploiement, pas celui du modèle |
| `json.loads(resp.output_text)` lève `JSONDecodeError` | Schéma non appliqué ou modèle ne supporte pas JSON strict | S'assurer que `"strict": True` est dans le schéma et vérifier que le modèle supporte la sortie structurée |
| Le streaming ne délivre pas d'événements `delta` | Vérification d'un mauvais type d'événement | Filtrer par `event.type == "response.output_text.delta"`, pas par `chat.completion.chunk` de Chat |
| Erreur `400` sur entrée image après migration | Type de contenu image non mis à jour | Changer `"type": "image_url"` → `"type": "input_image"` et aplatir `"image_url": {"url": "..."}` → `"image_url": "..."` (chaîne simple) |
| Les appels d'outils bouclent indéfiniment | Résultat d'outil manquant dans l'`input` de suivi | Après exécution d'un outil, ajouter un élément `{"type": "function_call_output", "call_id": ..., "output": ...}` à `input` dans la requête suivante |
| Erreur `temperature` avec GPT-5 ou séries o | Valeur explicite de `temperature` autre que 1 | Supprimer `temperature` ou le fixer à `1` pour GPT-5 et les modèles séries o (o1, o3-mini, o3, o4-mini) |
| Erreur `top_p` avec séries o | `top_p` non supporté | Supprimer `top_p` lors de la cible des modèles séries o |
| `max_completion_tokens` pas reconnu | Utilisation d'un paramètre spécifique Azure | Remplacer `max_completion_tokens` par `max_output_tokens`. Mettre à 4096+ pour séries o (les tokens de raisonnement comptent dans la limite). |
| Sortie vide/tronquée des séries o | `max_output_tokens` trop bas | Les séries o utilisent des tokens de raisonnement en interne. Mettre `max_output_tokens=4096` ou plus — pas 500–1000. |
| `400 integer_below_min_value` pour `max_output_tokens` | Valeur inférieure à 16 | Azure OpenAI impose `max_output_tokens >= 16`. Utiliser 50+ pour tests rapides, 1000+ en production. |
| `429 Too Many Requests` en plein streaming | Limitation de taux par Azure OpenAI | Le streaming se coupe silencieusement sans gestion d'erreur. Toujours entourer `async for event in await coroutine:` par un `try/except` et émettre `{"error": str(e)}` au frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Mauvais locataire ou non connecté | Passer explicitement `tenant_id=os.getenv("AZURE_TENANT_ID")`. Exécuter `azd auth login --tenant <tenant-id>` localement. |
| `404 Not Found` avec les modèles GitHub (`models.github.ai`) | Les modèles GitHub ne supportent pas l'API Responses | Supprimer complètement la voie de code des modèles GitHub. Utiliser Azure OpenAI, OpenAI, ou un endpoint local compatible (ex. Ollama avec support Responses). |
| MAF `OpenAIChatCompletionClient` utilise encore Chat Completions | Utilisation du client MAF legacy en 1.0.0+ | Depuis MAF 1.0.0+, `OpenAIChatClient` utilise par défaut l'API Responses. Remplacer `OpenAIChatCompletionClient` par `OpenAIChatClient`. Pour versions <1.0.0, mettre à jour `agent-framework-openai>=1.0.0`. |
| Agent LangChain retourne vide ou échoue avec appels d'outils | `ChatOpenAI` n'utilise pas l'API Responses | Ajouter `use_responses_api=True` à `ChatOpenAI(...)`. Changer aussi `.content` → `.text` sur les messages de réponse. |
| `KeyError: 'innererror'` dans le gestionnaire d'erreur filtre de contenu | La structure du corps d'erreur a changé dans l'API Responses | Réécrire `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Le wrapper `innererror` a disparu ; les détails du filtre sont maintenant dans un tableau de haut niveau `content_filters` avec `content_filter_results` (pluriel) dans chaque entrée. |
| Appel HTTP brut à `/openai/deployments/.../chat/completions` renvoie 404 | Ancien endpoint REST Chat Completions | Réécrire l'URL en `/openai/v1/responses`. Modifier le corps de la requête : `messages` → `input`, ajouter `max_output_tokens` + `store: false`, enlever le paramètre de requête `api-version`. Modifier le parsing de réponse : `choices[0].message.content` → `output[0].content[0].text` (note : `output_text` est une propriété pratique SDK, absente du JSON REST brut). |

---

## Pièges

1. Si vous utilisiez auparavant Chat Completions pour l'état de la conversation, gérez votre propre état explicitement avec Responses.
2. Préférez `max_output_tokens` au legacy `max_tokens`.
3. Lors de la migration vers `gpt-5`, assurez-vous que `temperature` n'est pas spécifié ou est défini à `1`.
4. Remplacez Chat `content[].type: "text"` par Responses `content[].type: "input_text"` pour les entrées utilisateur/système.
5. Pour `text.format`, fournissez un dict approprié (ex. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), pas une simple chaîne.
6. Le paramètre `seed` n'est pas supporté dans Responses ; supprimez-le des requêtes.
7. **Raisonnement** : Incluez `reasoning` uniquement si le code original l'utilisait déjà. N'ajoutez pas `reasoning` aux appels API qui n'en avaient pas — beaucoup de modèles non-raisonnement ne supportent pas ce paramètre.
8. **Dimensionnement `max_output_tokens`** : Pour les modèles de raisonnement (GPT-5-mini, GPT-5, séries o), utilisez `max_output_tokens=4096` ou plus — pas 50–1000. Le modèle utilise des tokens de raisonnement en interne avant de générer la sortie visible ; des limites trop basses causent des réponses tronquées ou vides.
9. **`max_completion_tokens` séries o** : Si le code original utilisait `max_completion_tokens` (spécifique Azure pour séries o), remplacez par `max_output_tokens`. L'API Responses n'accepte pas `max_completion_tokens`.
10. **`reasoning_effort` séries o** : Si le code original utilise `reasoning_effort` (low/medium/high), migrez-le en `reasoning={"effort": "<valeur>"}` dans l'appel API Responses.
11. **Délai de streaming séries o** : Les modèles séries o effectuent un raisonnement interne avant de générer la sortie. En streaming, attendez un délai plus long avant le premier événement `response.output_text.delta`. Ceci est normal — le modèle raisonne, il n'est pas bloqué.
9. **`_azure_ad_token_provider` a disparu** : `AsyncOpenAI` / `OpenAI` n'ont plus d'attribut `_azure_ad_token_provider`. Les tests ou codes qui y accèdent échoueront avec `AttributeError`. Le fournisseur de token est passé en `api_key` et n'est pas inspectable sur l'objet client.
10. **Snapshots / fichiers golden** : Si la suite de tests utilise le snapshot testing, **tous** les fichiers snapshot contenant des formes Chat Completions streaming (`choices[0]`, `content_filter_results`, `function_call`, etc.) doivent être mis à jour vers la nouvelle forme Responses. C'est facile à manquer et cause des échecs d'assertion snapshot.
11. **Chemin du mock monkeypatch** : La cible monkeypatch change de `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (ou `Responses.create` pour sync). Utiliser l'ancien chemin ne fait rien sans bruit — le mock n'interceptera pas et les tests atteindront la vraie API ou échoueront.
12. **`input` pas `messages`** : Les fonctions mock doivent lire `kwargs.get("input")` pas `kwargs.get("messages")`. L'API Responses utilise `input` pour l'historique de conversation.
13. **Nom des variables d'environnement** : Le SDK Azure Identity utilise `AZURE_CLIENT_ID` (pas `AZURE_OPENAI_CLIENT_ID`) pour `ManagedIdentityCredential(client_id=...)`. Renommer dans les tests, fichiers `.env`, paramètres d'app et Bicep/infrastructure.
14. **`max_output_tokens` minimum est 16** : Azure OpenAI rejette les valeurs inférieures à 16 avec `400 integer_below_min_value`. Utiliser `50` pour les tests rapides, `1000`+ en production. L'ancien `max_tokens` n'avait pas de minimum.
15. **`tenant_id` pour `AzureDeveloperCliCredential`** : Quand la ressource Azure OpenAI est dans un tenant différent, il faut **obligatoirement** passer `tenant_id` explicitement — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Sans cela, le credential utilise silencieusement le mauvais tenant et renvoie `401`.
16. **Les limites de débit apparaissent différemment en streaming** : Avec Chat Completions, un 429 empêchait généralement le démarrage du stream. Avec le streaming de l'API Responses, un 429 peut survenir **en plein stream** — l'itérateur async lève une exception. Toujours entourer la boucle de streaming d'un `try/except` et émettre une ligne JSON d'erreur pour que le frontend puisse la gérer proprement.

17. **La gestion des erreurs en streaming est obligatoire pour les applications web** : Le modèle `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` est essentiel. Sans cela, le flux SSE/JSONL meurt silencieusement en cas d’erreur côté serveur et le frontend reste bloqué.
18. **Les définitions d’outils doivent utiliser un format plat** : L’API Responses attend `{"type": "function", "name": ..., "parameters": ...}` — pas le format imbriqué de Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. C’est l’erreur la plus courante lors de la migration du code d’appel de fonction.
19. **`pydantic_function_tool()` est incompatible** : L’assistant `openai.pydantic_function_tool()` génère encore l’ancien format imbriqué. Ne l’utilisez pas avec `responses.create()`. Définissez manuellement les schémas d’outils ou aplatissez la sortie.
20. **Les résultats d’outils utilisent `function_call_output`, pas `role: tool`** : Après exécution d’un outil, ajoutez `{"type": "function_call_output", "call_id": ..., "output": ...}` — pas `{"role": "tool", "tool_call_id": ..., "content": ...}`. Pour la requête d’un outil par l’assistant, utilisez `messages.extend(response.output)` — pas un dictionnaire manuel `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` exige `required` + `additionalProperties: false`** : Lors de l’utilisation de `strict: true` sur un outil, chaque propriété doit être listée dans le tableau `required` et `additionalProperties` doit être `false`. L’absence de l’un ou l’autre provoque une erreur 400.
22. **Les IDs d’appel de fonction ont des préfixes spécifiques** : Lors de la fourniture d’éléments `function_call` en few-shot dans `input`, le champ `id` doit commencer par `fc_` et le champ `call_id` par `call_` (ex. `"id": "fc_example1", "call_id": "call_example1"`). L’usage de l’ancien préfixe `call_` pour `id` de Chat Completions est refusé.
23. **GitHub Models ne supporte pas l’API Responses** : Si l’application utilise un chemin de code GitHub Models (`base_url` pointant vers `models.github.ai` ou `models.inference.ai.azure.com`), supprimez-le entièrement. Il n’existe aucun chemin de migration — basculez vers Azure OpenAI, OpenAI ou un endpoint local compatible.
24. **La structure du corps des erreurs du filtre de contenu a changé** : Les erreurs Chat Completions utilisaient `error.body["innererror"]["content_filter_result"]` (singulier). L’API Responses utilise `error.body["content_filters"][0]["content_filter_results"]` (pluriel, dans un tableau). La clé `innererror` n’existe plus. Le code accédant directement à `innererror` lèvera une `KeyError` à l’exécution — ce qui est facile à manquer lors de la migration car cela n’apparait que lorsque le filtre de contenu est déclenché. Cherchez toujours `innererror` pendant la migration.
25. **Les appels HTTP bruts nécessitent une réécriture de l’URL + du corps** : Les applications appelant Azure OpenAI REST directement (via `requests`, `httpx`, `aiohttp`) avec `/openai/deployments/{name}/chat/completions?api-version=...` doivent passer à `/openai/v1/responses`. Le corps de la requête utilise `input` au lieu de `messages`, exige `max_output_tokens` et `store`, et le paramètre de requête `api-version` est supprimé. Le texte du corps de la réponse se trouve à `output[0].content[0].text` — **pas** `output_text`, qui est une propriété pratique du SDK absente du JSON REST brut.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->