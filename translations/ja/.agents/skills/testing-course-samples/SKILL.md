---
name: testing-course-samples
---
# コースサンプルのテスト

レッスン用ノートブックおよびコードサンプルが実際の
Microsoft Foundry / Azure OpenAI 環境で動作するかを検証します。このリポジトリには
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) という
ランナーが付属しており、全てのPythonノートブックをヘッドレス実行し、


## 使用タイミング
- "すべてのノートブック／サンプルを自分のAzureサブスクリプションで検証したいとき。"
- "パッケージのアップグレードやモデル変更後にコースのスモークテストを行いたいとき。"


AI Smoke Test GitHub Action（<em>デプロイ済み</em>ホストエージェントを検証するもの—[`tests/README.md`](../../../tests/README.md)参照）には<strong>使用しないでください</strong>。このスキルは
ノートブックをローカルで実行します。

## 前提条件（最初にチェック）
1. **Python 3.12+** とコース依存パッケージ：`python -m pip install -r requirements.txt`
   および実行用：`python -m pip install nbconvert ipykernel`。
2. リポジトリルートに **`.env`**（[`.env.example`](../../../../../.env.example) からコピー）を用意し、少なくとも以下を設定：
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundryプロジェクトのエンドポイント
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — 廃止されていないデプロイメント名（例：`gpt-5-mini`）
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) と `AZURE_OPENAI_DEPLOYMENT`
     これはAzure OpenAIを直接呼び出すレッスン用（Lesson 06、02-azure-openai、14 handoff/human-loop）。
3. **`az login`** の完了 — サンプルは `AzureCliCredential` で認証します（Entra ID、キーレス）。
4. モデルデプロイメントが存在するか確認：
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`。

## 検証の実行方法
```powershell
# すべてのPythonノートブック（.NET、.venv、site-packages、translations、スキルアセットはスキップ）
pwsh scripts/validate-notebooks.ps1

# 1つのレッスン、セルごとのタイムアウトが長い
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# 実行されるものをリスト表示するだけ（実行はしない）
pwsh scripts/validate-notebooks.ps1 -List

# 明示的なインタプリタ（`python`がPATHにない場合、例：Windowsストアのエイリアス）
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
スクリプトは実行済みのコピー、ノートブックごとのログ、`results.json`を
`$env:TEMP\aiab-nbval` に書き出し、失敗数を終了コードとして返します。

一時的な失敗（共有サブスクリプションのHTTP 429レート制限、たまに起こる
`AzureCliCredential` トークンの不具合、タイムアウト）は自動的に
リトライされます（`-Retries`（デフォルト2）および `-RetryDelaySeconds` バックオフ（デフォルト20秒））。モデルデプロイメントが頻繁に429を返す場合は、
サブスクリプションのGlobalStandard
TPMクォータ（`az cognitiveservices usage list -l <region>`）を確認してください。単一の
デプロイメントの容量増強は、<em>サブスクリプション</em> クォータが枯渇している場合は効果がありません。

## 結果の解釈
- `PASS` — ノートブックはセルエラーなく最後まで実行されました。
- `FAIL` — 最初の `*Error` / `*Exception` 行が表示されます。完全なトレースバックは、
  出力ディレクトリ内の該当する `log_*.txt` を開いて確認してください。
- 単一ノートブックの失敗は `-Timeout`（セルごと）により制限されます。つまり、
  ハングしたヒューマンインザループセルは `StdinNotImplementedError` として検出され、ハング状態にはなりません。

## 追加リソースが必要なレッスン（無ければ失敗が予想される）
| レッスン | 追加要件 |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search（`AZURE_SEARCH_SERVICE_ENDPOINT`、キー）— インメモリのフォールバックパスあり |
| 11 MCP / GitHub | GitHub MCPサーバー + PAT |
| 13 memory (cognee) | `cognee` がモデルプロバイダーで設定されていること |
| 15 browser-use | Playwrightのブラウザがインストール済み（`playwright install`） + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Localランタイム + ダウンロード済みQwenモデル（デバイス内、クラウド不要） |
| `*-dotnet-*` ノートブック | .NET Interactiveカーネル（既定では除外；`-IncludeDotnet` 使用で含む） |

## 結果の報告
レッスン単位でまとめたPASS／FAILテーブルを作成します。実際のリグレッション
（修正すべきコード・設定のバグ）と環境不足（Search/Foundry Local/PATの未設定）を区別し、
本物の失敗ごとに該当する `log_*.txt` を記載してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->