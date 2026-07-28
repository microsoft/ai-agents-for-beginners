---
name: testing-course-samples
---
# コースサンプルのテスト

レッスンノートブックとコードサンプルがライブの
Microsoft Foundry / Azure OpenAI 環境で動作することを検証します。リポジトリには
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) に
すべてのPythonノートブックをヘッドレスで実行し、PASS/FAILマトリックスを表示するランナーが含まれています。

## いつ使うか
- 「すべてのノートブック／サンプルが自分のAzureサブスクリプションで動作するか検証したい」
- 「パッケージをアップグレードしたりモデルを変更した後のコースのスモークテスト」
- 「まだ動作する／動作しないレッスンはどれか？」

AI Smoke Test GitHub Action には<strong>使用しないでください</strong>（<em>デプロイ済み</em>ホストエージェントを検証する — [`tests/README.md`](../../../tests/README.md) を参照）。このスキルは
ローカルでノートブックを実行します。


1. **Python 3.12+** とコースの依存関係：`python -m pip install -r requirements.txt`
   に加え、実行環境用に：`python -m pip install nbconvert ipykernel`。
2. リポジトリルートに **`.env`** （[`.env.example`](../../../../../.env.example) からコピー）を配置し、
   少なくとも以下を含める：
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundryプロジェクトエンドポイント
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — 廃止されていないデプロイメント（例：`gpt-4.1-mini`）
   - Azure OpenAIを直接呼び出すレッスン用に `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) と `AZURE_OPENAI_DEPLOYMENT`
     （レッスン06、02-azure-openai、14 handoff/human-loop）。
3. **`az login`** が完了していること — サンプルは `AzureCliCredential`（Entra ID、キーレス）で認証します。
4. モデルデプロイメントが存在することを確認：
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`。

## 検証の実行
```powershell
# すべてのPythonノートブック（.NET、.venv、site-packages、翻訳、スキルアセットは除外）
pwsh scripts/validate-notebooks.ps1

# より長いセルごとのタイムアウトがある単一のレッスン
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# 実行せずに実行されるものを一覧表示するだけ
pwsh scripts/validate-notebooks.ps1 -List

# 明示的なインタープリター（`python`がPATHにない場合、例：Windowsストアのエイリアス）
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
スクリプトは実行したコピー、ノートブックごとのログ、`results.json` を
`$env:TEMP\aiab-nbval` に書き込み、失敗数を返します。

## 結果の解釈
- `PASS` — ノートブックがセルエラーなしで最後まで実行されました。
- `FAIL` — 最初に検出された `*Error` / `*Exception` の行が表示されます。対応する
  出力ディレクトリの `log_*.txt` を開き、完全なトレースバックを確認してください。
- 単一ノートブックの失敗は `-Timeout`（セル単位）で制限されるため、
  ハングしている人間ループセルは `StdinNotImplementedError` として検出され、ハングしっぱなしにはなりません。

## 追加リソースが必要なレッスン（それらがなければ失敗します）
| レッスン | 追加要件 |
|--------|------------|
| 05 Agentic RAG | Azure AI Search（`AZURE_SEARCH_SERVICE_ENDPOINT`, キー）— インメモリフォールバックパスあり |
| 11 MCP / GitHub | GitHub MCPサーバー + PAT |
| 13 memory (cognee) | `cognee` がモデルプロバイダーと設定済み |
| 15 browser-use | Playwrightブラウザをインストール済み（`playwright install`） + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + ダウンロード済みQwenモデル（オンデバイス、クラウド不要） |
| `*-dotnet-*` ノートブック | .NET Interactive カーネル（デフォルトで除外、`-IncludeDotnet`を使用） |

## レポート
レッスンごとにグループ化したPASS/FAIL表としてまとめます。真の回帰（修正が必要なコード／設定バグ）と
環境の不足（Search/Foundry Local/PATが足りないなど）を分けて、
実際に失敗した部分には対応する `log_*.txt` を引用してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->