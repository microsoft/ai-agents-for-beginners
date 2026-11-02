# エージェント スモークテスト

このフォルダーには、コースで作成するエージェントのための<strong>スモークテストカタログ</strong>が入っています。
スモークテストとは、<strong>デプロイされた Microsoft Foundry ホスト型エージェント</strong>が到達可能で応答し、
最も基本的なプロンプトの期待値に従っているかを低コストかつ高速にチェックするものです。
これは最初の関門であり、[レッスン10](../10-ai-agents-production/README.md)や
[レッスン16](../16-deploying-scalable-agents/README.md)で学ぶ完全な評価パイプラインの代替ではありません。


これらのカタログは、[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Actionによって、[`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
ワークフロー経由で利用されます。

## 実行方法

1. Microsoft Foundry にホストエージェントとして<strong>レッスンのエージェントをデプロイ</strong>します（デプロイワークフローは
   レッスン16を参照）。<strong>エージェント名</strong>とあなたの
   <strong>Foundryプロジェクトエンドポイント</strong>を控えておきます。
2. これらのリポジトリシークレットを追加します（設定 → Secrets and variables → Actions）：
   `AZURE_CLIENT_ID`、`AZURE_TENANT_ID`、`AZURE_SUBSCRIPTION_ID`。フェデレーテッド
   IDには<strong>Foundryプロジェクトスコープ</strong>での<strong>Azure AIユーザー</strong>ロールが必要です。
3. **Actions** タブから **Smoke-test hosted agents** を実行し、対応するレッスンの
   `tests_file` を選択、続けて対応する `agent_name` と
   `project_endpoint` を入力します。

## カタログ → レッスン → エージェント名

| カタログ | レッスン | デプロイエージェント名 |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – AIエージェント入門](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – ツール利用](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – エージェント的RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – スケーラブルエージェントのデプロイ](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## どのレッスンにスモークテストがあるか？

スモークテストは、テキスト返信が既知の内容と照合可能な<strong>エージェントをデプロイ</strong>するレッスンに適用されます。
概念的なレッスン、ローカルのみで実行するもの、
または非決定的で創造的な出力を生成するものは意図的に除外されています：

- <strong>レッスン17（ローカルAIエージェントの作成）</strong>は完全にワークステーション上の
  Foundry Localで実行され、Foundryレスポンスエンドポイントを公開しないため、
  この操作は適用されません。ノートブックをローカルで実行して検証してください。
- デザインパターンや理論のレッスン（02, 03, 06, 07, 09, 12）は単一の
  デプロイ可能なエージェントを出荷していないため、スモークテストはありません。

## カタログスキーマ（簡易参照）

各カタログはトップレベルに`tests`配列を持つJSONドキュメントです。各エントリは
1つのプロンプトをPOSTし、応答をアサートします：

| フィールド | 意味 |
|-------|---------|
| `id` | ログに表示されるユニークなステップ識別子。 |
| `description` | 人間可読の目的説明。 |
| `prompt` | エージェントに送信されるメッセージ。 |
| `assertions.status` | 期待されるHTTPステータス（デフォルトは200）。 |
| `assertions.contains_any` | 応答がこれらの部分文字列のいずれかを含むと合格。 |
| `assertions.contains_all` | 応答がすべての部分文字列を含むと合格。 |
| `assertions.contains_none` | 応答がこれらの部分文字列を含まないと合格。 |
| `save_response_id_as` | 後のマルチターンステップ用に応答IDを保存。 |
| `use_previous_response_id` | 保存された応答IDに連結してこのターンを送信。 |

アサーションは大文字・小文字を区別しない部分文字列チェックです。詳細は
[アクションドキュメント](https://github.com/marketplace/actions/ai-smoke-test)で、
Foundry管理の会話リソースを含む完全なスキーマを参照してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->