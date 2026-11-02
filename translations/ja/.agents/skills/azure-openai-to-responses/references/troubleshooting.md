# トラブルシューティング、リスク表＆注意点

## 400エラーのトラブルシューティング

| エラー | 修正 |
|-------|-----|
| `missing_required_parameter: tools[0].name` | ツール定義が古いChat Completionsのネスト形式を使用している | `{"type": "function", "function": {"name": ...}}` から `{"type": "function", "name": ..., "parameters": ...}` へ平坦化 — name, description, parametersはトップレベルに配置する |
| `unknown_parameter: input[N].tool_calls` | マルチターンツール結果が古いChat Completions形式を使用 | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` を `response.output` アイテム + `{"type": "function_call_output", "call_id": ..., "output": ...}` に置き換える |
| `invalid_function_parameters: 'required' is required` | `strict: true`ツールが`required`配列を欠落 | `strict: true`の場合、すべてのプロパティを`required`に記載し、`additionalProperties: false`を設定する必要がある |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true`ツールが`additionalProperties: false`を欠落 | パラメータオブジェクトに `"additionalProperties": false` を追加する |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call IDのプレフィックスが間違っている | 関数呼び出しIDは `fc_` で始まる必要がある（例：`fc_example1`）、`call_`は不可 |
| `missing_required_parameter: text.format.name` | format辞書に `"name"` キーを追加 (例: `"name": "Output"`) |
| `invalid_type: text.format` | `text.format` は文字列ではなく、`type`, `name`, `strict`, `schema` キーを持つ辞書にする |
| `invalid input content type` | Chatの`text`の代わりに`input_text`/`output_text`コンテンツタイプを使用する |
| `invalid input content type` (image) | 画像コンテンツが `"type": "image_url"` のまま | `"type": "input_image"` に変更する |
| `Expected object, got string` on `image_url` | `image_url` がまだネストオブジェクト `{"url": "..."}` である | 単一の文字列に平坦化する: `"image_url": "https://..."` または `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAIの最小値は<strong>16</strong>。テストは50以上、本番は1000以上を使用 |
| `429 Too Many Requests` during streaming | レート制限。ストリーミングを`try/except`で包み、エラーJSONをフロントエンドに送出し、バックオフ/リトライを実装する |
| `KeyError: 'innererror'` on content filter error | Content filterエラーのボディ構造がResponses APIで変更 | Chat Completionsは `error.body["innererror"]["content_filter_result"]` を使うが、Responses APIは `error.body["content_filters"][0]["content_filter_results"]`（複数形で配列内）を使用。すべての`innererror`アクセスを改訂する |

---

## 移行リスク表

| 症状 | 可能な誤り | 修正 |
|---------|---------------|-----|
| 空の`output_text` / 応答が切れる | 推論モデルに対して `max_output_tokens` が低すぎる | `max_output_tokens=1000`以上に設定 — 推論トークンは制限に含まれる |
| `400 invalid_type: text.format` | `text.format` 辞書ではなく文字列の `response_format` を渡している | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` を使う |
| `/openai/v1/responses`で`404 Not Found` | 間違った `base_url` — `/openai/v1/` のサフィックスが欠落 | `base_url=f"{endpoint}/openai/v1/"` （末尾のスラッシュ込み）を指定 |
| `OpenAI()`に切り替え後に`401 Unauthorized` | `api_key`未設定またはトークンプロバイダーが正しく渡されていない | EntraIDの場合:`api_key=token_provider`（呼び出し可能オブジェクト）。APIキーの場合:`api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| モデルが `deployment not found` を返す | `model` パラメータがAzureデプロイ名と一致していない | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` を使用 — これはデプロイ名でありモデル名ではない |
| `json.loads(resp.output_text)` で `JSONDecodeError` が発生 | スキーマが適用されていないか、モデルが厳密なJSONをサポートしていない | スキーマで `"strict": True` を保証し、モデルが構造化出力をサポートしていることを確認 |
| ストリーミングで`delta`イベントがない | 誤ったイベントタイプでフィルタリングしている | Chatの`chat.completion.chunk`ではなく、`event.type == "response.output_text.delta"`でフィルタする |
| 移行後に画像入力で`400`エラー | 画像コンテンツタイプが更新されていない | `"type": "image_url"`を`"type": "input_image"`に変更し、`"image_url": {"url": "..."}`を`"image_url": "..."`（単純文字列）に平坦化する |
| ツール呼び出しが無限ループ | フォローアップ`input`にツール結果が欠落 | ツール実行後、次のリクエストの`input`に `{"type": "function_call_output", "call_id": ..., "output": ...}` アイテムを追加する |
| GPT-5またはoシリーズで`temperature`エラー | 1以外の明示的な`temperature`値 | GPT-5およびoシリーズモデル（o1, o3-mini, o3, o4-mini）では`temperature`を削除するか1に設定 |
| oシリーズで`top_p`エラー | `top_p`はサポート外 | oシリーズモデル対象時は`top_p`を削除する |
| `max_completion_tokens`が認識されない | Azure固有パラメータの使用 | `max_completion_tokens`を`max_output_tokens`に置き換える。oシリーズは4096以上に設定（推論トークンは制限にカウント） |
| oシリーズの出力が空または切れる | `max_output_tokens`が低すぎる | oシリーズは内部的に推論トークンを使用する。`max_output_tokens=4096`以上に設定する — 500〜1000では不十分 |
| `400 integer_below_min_value` for `max_output_tokens` | 16未満の値 | Azure OpenAIは`max_output_tokens >= 16`を強制。スモークテストは50以上、本番は1000以上を使用 |
| ストリーム途中で`429 Too Many Requests` | Azure OpenAIによるレート制限 | ストリームはエラー処理なしで静かに途切れる。常に`async for event in await coroutine:`を`try/except`で包み、`{"error": str(e)}`をフロントエンドに送りエラー処理を行う |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | テナント違いまたはログインなし | 明示的に `tenant_id=os.getenv("AZURE_TENANT_ID")` を渡す。ローカルで `azd auth login --tenant <tenant-id>` を実行する |
| GitHub Models（`models.github.ai`）で`404 Not Found` | GitHub ModelsはResponses APIをサポートしていない | GitHub Modelsのコードパスを完全に削除。Azure OpenAI、OpenAI、またはResponses対応のローカルエンドポイント（例：Ollama）を使用 |
| MAFの`OpenAIChatCompletionClient`がまだChat Completionsを使用 | 1.0.0+で古いMAFクライアントの使用 | MAF 1.0.0+では`OpenAIChatClient`がデフォルトでResponses APIを使う。`OpenAIChatCompletionClient`を`OpenAIChatClient`に置換。1.0.0未満は`agent-framework-openai>=1.0.0`にアップグレード。 |
| LangChainエージェントが空応答またはツール呼び出しで失敗 | `ChatOpenAI`がResponses APIを使っていない | `ChatOpenAI(...)`に `use_responses_api=True` を追加。応答メッセージの `.content` を `.text` に変更 |
| Content filterエラー処理で`KeyError: 'innererror'` | Responses APIでエラーボディ構造変更 | `error.body["innererror"]["content_filter_result"]["jailbreak"]` を `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` に書き換える。`innererror`ラッパーはなくなり、トップレベルの `content_filters` 配列内に複数形`content_filter_results`が入る形式に変わった。 |
| `/openai/deployments/.../chat/completions`への生HTTP呼び出しが404返す | 古いChat CompletionsのRESTエンドポイント | URLを `/openai/v1/responses` に書き換え。リクエストボディを `messages` → `input` に変更、`max_output_tokens` と `store: false` を追加、`api-version`クエリパラメータを削除。レスポンス解析を `choices[0].message.content` → `output[0].content[0].text` に変更（`output_text`はSDKの便宜的プロパティ、本来REST JSONにはない）。 |

---

## 注意点

1. 以前Chat Completionsで会話状態を使用していた場合は、Responsesで自分で明示的に状態管理を行うこと。
2. レガシーな`max_tokens`より`max_output_tokens`を優先して使うこと。
3. `gpt-5`に移行する際は、必ず`temperature`が指定されていないか、`1`に設定されていることを確認すること。
4. Chatの `content[].type: "text"` はResponsesの `content[].type: "input_text"` に置き換える。ユーザー/システム入力向け。
5. `text.format`には文字列ではなく、適切な辞書（例：`{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`）を指定すること。
6. `seed` パラメータはResponsesではサポートされていないため、リクエストから削除すること。
7. <strong>推論パラメータ</strong>：元のコードで既に使われている場合のみ`reasoning`を含めること。推論を使わないAPI呼び出しに`reasoning`を追加してはいけない — 多くの非推論モデルはこのパラメータをサポートしない。
8. **`max_output_tokens`のサイズ**：推論モデル（GPT-5-mini, GPT-5, oシリーズ）は`max_output_tokens=4096`以上を使用すること。50〜1000では不十分。モデルは可視出力の前に内部で推論トークンを使用するため、制限が低すぎると応答が切れたり空になる。
9. **oシリーズの`max_completion_tokens`**：元のコードでAzure固有の `max_completion_tokens` を使っている場合は、`max_output_tokens` に置き換える。Responses APIは `max_completion_tokens` を受け付けない。
10. **oシリーズの`reasoning_effort`**：元コードで `reasoning_effort`（low/medium/high）を使っているなら、Responses API呼び出しでは `reasoning={"effort": "<値>"}` に移行する。
11. **oシリーズのストリーミング遅延**：oシリーズモデルは出力生成前に内部的な推論を行う。ストリーミング時、最初の `response.output_text.delta` イベントが来るまで遅延が長いのは正常 — モデルがハングしているわけではなく推論中。
9. **`_azure_ad_token_provider`は廃止**：`AsyncOpenAI`/`OpenAI`に `_azure_ad_token_provider`属性はなくなった。これにアクセスするテストやコードは`AttributeError`で失敗する。トークンプロバイダーは`api_key`として渡し、クライアントオブジェクトで検査できない。
10. **スナップショット/ゴールデンファイル**：テストスイートでスナップショットテストを使う場合、Chat Completionsのストリーミング形式（`choices[0]`, `content_filter_results`, `function_call`など）を含むすべてのスナップショットファイルを新しいResponses形式に更新する必要がある。これを見逃すとスナップショットのアサーションに失敗する。
11. <strong>モックのモンキーパッチパス</strong>：モンキーパッチのターゲットは`openai.resources.chat.AsyncCompletions.create`から`openai.resources.responses.AsyncResponses.create`（同期は`Responses.create`）に変わる。旧パスは何もせず、モックが効かずテストが実APIを叩くか失敗する。
12. **`input`は`messages`でなく**：モック関数は`kwargs.get("input")`を読む必要がある。Responses APIは会話履歴に`input`を使う。
13. <strong>環境変数名の変更</strong>：Azure Identity SDKは`ManagedIdentityCredential(client_id=...)`用に`AZURE_CLIENT_ID`（`AZURE_OPENAI_CLIENT_ID`ではない）を使う。テスト、`.env`ファイル、アプリ設定、Bicep/インフラで名前を変更する。
14. **`max_output_tokens`最小値は16**：Azure OpenAIは16未満の値を`400 integer_below_min_value`で拒否する。スモークテストは50、本番は1000以上を使う。旧`max_tokens`にはこの最小値制限はなかった。
15. **`AzureDeveloperCliCredential`の`tenant_id`**：Azure OpenAIリソースが異なるテナントにある場合、`tenant_id`を明示的に渡す必要がある — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`。指定しないと誤ったテナントが使われて`401`になる。
16. <strong>ストリーミングでのレート制限の表示が異なる</strong>：Chat Completionsでは429は通常ストリーム開始前に発生。一方Responses APIのストリーミングでは<strong>途中で</strong>429が発生し、非同期イテレータが例外をスローする。ストリーミングループを常に`try/except`で包み、エラーのJSON行を送出してフロントエンドで適切に処理できるようにする。

17. <strong>ストリーミングエラー処理はウェブアプリで必須です</strong>: パターン `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` は重要です。これがないと、SSE/JSONLストリームはサーバー側のエラーでひっそりと停止し、フロントエンドがハングアップします。
18. <strong>ツール定義はフラット形式を使用する必要があります</strong>: Responses APIは `{"type": "function", "name": ..., "parameters": ...}` を期待しており、Chat Completionsの入れ子形式 `{"type": "function", "function": {"name": ..., "parameters": ...}}` ではありません。これは関数呼び出しコードの最も一般的な移行エラーです。
19. **`pydantic_function_tool()` は互換性がありません**: `openai.pydantic_function_tool()` ヘルパーは旧入れ子形式をまだ生成します。`responses.create()` と共に使用しないでください。ツールスキーマは手動で定義するか、出力をフラット化してください。
20. **ツールの結果は `function_call_output` を使い、`role: tool` は使いません**: ツールを実行した後は、`{"type": "function_call_output", "call_id": ..., "output": ...}` を追加し、`{"role": "tool", "tool_call_id": ..., "content": ...}` は使いません。アシスタントのツールリクエストには、手動の `{"role": "assistant", "tool_calls": [...]}` 辞書ではなく、`messages.extend(response.output)` を使用してください。
21. **`strict: true` は `required` と `additionalProperties: false` を要求します**: ツールで `strict: true` を使う場合は、すべてのプロパティを `required` 配列に列挙し、`additionalProperties` は `false` にする必要があります。どちらかが欠けていると400エラーになります。
22. **関数呼び出しIDには特定のプレフィックスがあります**: `input` 内で少数の `function_call` 項目を提供する場合、`id` フィールドは `fc_` で始まり、`call_id` フィールドは `call_` で始まる必要があります（例: `"id": "fc_example1", "call_id": "call_example1"`）。従来のChat Completionsの `call_` プレフィックスを `id` に使うと拒否されます。
23. **GitHub ModelsはResponses APIをサポートしていません**: アプリにGitHub Modelsのコードパス（`base_url` が `models.github.ai` または `models.inference.ai.azure.com` を指す）がある場合は、完全に削除してください。移行パスはなく、Azure OpenAI、OpenAI、または互換のローカルエンドポイントに切り替えてください。
24. <strong>コンテンツフィルターのエラー本文構造が変わりました</strong>: Chat Completionsのエラーは `error.body["innererror"]["content_filter_result"]`（単数）を使っていました。Responses APIのエラーは `error.body["content_filters"][0]["content_filter_results"]`（複数、配列内）を使います。`innererror` キーはもう存在しません。コードが直接 `innererror` にアクセスすると、実行時に `KeyError` が発生します。これはコンテンツフィルターが実際にトリガーされたときのみ表面化するため、移行時に見落としがちです。必ず移行中に `innererror` をグレップしてください。
25. **生のHTTP呼び出しはURLと本文の書き換えが必要です**: Azure OpenAI RESTを直接呼び出すアプリ（`requests`、`httpx`、`aiohttp`経由）で `/openai/deployments/{name}/chat/completions?api-version=...` を使っている場合は `/openai/v1/responses` に切り替えてください。リクエスト本文は `messages` ではなく `input` を使い、`max_output_tokens` と `store` が必要で、`api-version` クエリパラメータは廃止されます。レスポンス本文のテキストは `output[0].content[0].text` にあり、SDKの便宜的プロパティである `output_text`（生のREST JSONには存在しません）ではありません。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->