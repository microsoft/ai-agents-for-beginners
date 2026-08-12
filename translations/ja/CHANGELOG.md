# 変更履歴

**AI Agents for Beginners** コースのすべての重要な変更点はこのファイルに記録されています。

## [リリース済み] — 2026-07-14

このリリースでは、コースを2つの新規非推奨モデルから移行し、残りのレッスンノートブックを安定版の Microsoft Agent Framework API に移行し、Pythonノートブックをライブの Microsoft Foundry デプロイメントに対して検証しています。

### 変更点

- **非推奨モデルからの移行（`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`）。** `gpt-4.1` と `gpt-4.1-mini` は現在非推奨です（廃止予定日 **2026年10月14日**）。コース内のすべての参照（ドキュメント、`.env.example`、Python/.NETノートブックとサンプル）を非推奨でない `gpt-5-mini` に置き換えました。レッスン16のモデルルーティング例は `gpt-5-nano`（小）と `gpt-5-mini`（大）で小・大の対比を維持しています。サードパーティのベンダーファイル（[15-browser-use/llms.txt](../../15-browser-use/llms.txt)）、歴史的なGitHub Modelsテキスト、および `azure-openai-to-responses` スキルの能力に関する注記は意図的に変更していません。
- **レッスン14ハンドオフノートブックを安定APIに移行。** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb)は現在、`agent_framework.orchestrations.HandoffBuilder` の `.with_start_agent(...)`、`HandoffAgentUserRequest.create_response(...)`、`event.type` によるストリーミング、`FoundryChatClient` を使用しており（削除された pre-1.0 の `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` シンボルに置き換えています)。
- **レッスン14のヒューマン・イン・ザ・ループノートブックを安定APIに移行。** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb)は現在、`ctx.request_info(...)` + `@response_handler` により一時停止し（削除された `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` に置き換え）、`WorkflowBuilder(start_executor=..., output_executors=[...])` で構築し、`default_options={"response_format": ...}` を通じて構造化された出力を管理し、スクリプト化された回答を使っているためノートブックはブロッキングする `input()` なしで無人実行可能です。
- <strong>環境設定</strong> ([.env.example](../../.env.example))：モデルデプロイメント名を `gpt-5-mini` に変更。`AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL`（レッスン16ルーティング用）および以前欠落していた `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`（レッスン15のブラウザー利用用）を追加。
- <strong>依存関係</strong> ([requirements.txt](../../requirements.txt))：自己整合の取れた検証済みセットとして `agent-framework`、`agent-framework-foundry`、`agent-framework-openai` を `~=1.10.0` に固定（1.11.0にはこれらのレッスンが使用するサーフェスに対する実験的破壊的変更が含まれる）。

### メモと既知の制限事項

- **ライブの Microsoft Foundry で検証済み。** Pythonノートブックは `nbconvert` を使ってヘッドレス実行され、Microsoft Foundry プロジェクトで `gpt-5-mini`（レッスン16のルーティングは `gpt-5-nano`）を使って動作確認済み。ご自身のプロジェクトで等価な非推奨モデルでないデプロイメントを展開してください。ノートブックは `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` からデプロイメント名を読み込みます。
- **一部レッスンは追加リソースが必要。** レッスン05は Azure AI Search を必要とし、レッスン08のBing連携ワークフロー（`04.python-agent-framework-workflow-aifoundry-condition.ipynb`）はBing接続と Microsoft Foundry Agent Service ホストツール、レッスン13（Cognee）とレッスン17（Foundry Local）はそれぞれのランタイムを必要とします。

## [リリース済み] — 2026-07-13

このリリースは、Microsoft Foundry へのエージェントのスケールアップと単一ワークステーションへのスケールダウンというデプロイメントの全体像を完成させる2つの新レッスン、スモークテストパイプライン、更新されたコースナビゲーション、新しい学習者スキル、及び更新されたブランディングを追加します。

### 追加したもの

- **レッスン16 — Microsoft Foundry を使ったスケーラブルなエージェントのデプロイ。** 新しいレッスン [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) と実行可能なノートブック [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) が、プロダクションの顧客サポートエージェント（ツール、RAG、メモリ、モデルルーティング、応答キャッシュ、人間による承認、評価ゲート、および OpenTelemetry トレーシング）を構築。開発・デプロイ・ランタイムの Mermaid 図、知識チェック、課題、チャレンジを含む。
- **レッスン17 — Foundry Local と Qwen を使ったローカルAIエージェントの作成。** 新しいレッスン [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) とノートブック [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) が、完全オンデバイスのエンジニアリングアシスタント（Foundry Local経由のQwen関数呼び出し、サンドボックス化されたファイルツール、ChromaによるローカルRAG、オプションでローカルMCP）を構築。ローカル専用・ローカルRAG・ツール呼び出しの図、知識チェック、課題、チャレンジを含む。
- **スモークテストパイプライン。** 新しい [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) ワークフロー [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) と、レッスン01、04、05、16のデプロイ可能エージェント用カタログ群を [tests/](./tests/README.md) に追加。各カタログをレッスンとホストエージェント名にマッピングするインデックスREADME付き。レッスン16に「スモークテストでのデプロイ済みエージェントの検証」セクションを追加。レッスン01/04/05にはオプションのスモークテストへのポインタを追加。
- **学習者スキル。** `.agents/skills/` に新しいエージェントスキルを追加：[deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md)、[local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md)（レッスン16と17のガイドをパッケージング）、[testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md)（ライブの Microsoft Foundry / Azure OpenAI セットアップに対するノートブックサンプルの検証方法）。
- **ノートブック検証ランナー。** 新しい [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) はすべてのPythonノートブックを `nbconvert` でヘッドレス実行しPASS/FAILマトリックス（および `results.json`）を出力。リポジトリのルートやPythonを自動検出し、非コースノートブック（`.venv`、`site-packages`、`translations`、スキルテンプレート資産）および `.NET` ノートブックをデフォルトで除外し、`-Filter`、`-Timeout`、`-List`、`-IncludeDotnet`、`-Python` をサポート。
- **コースナビゲーション。** レッスン11〜15に前後のレッスンリンクを追加（以前は欠落）、コース全体が00 → 18まで双方向に連結。
- **新しいサムネイル。** レッスン16と17のサムネイル、および2つの新レッスンと `aka.ms/ai-agents-beginners` URLを宣伝する更新されたリポジトリソーシャルイメージ [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png)。
- <strong>依存関係</strong> ([requirements.txt](../../requirements.txt))：レッスン17用に `foundry-local-sdk` と `chromadb` を追加。

### 変更点

- **メイン [README.md](./README.md) レッスン表：** レッスン16と17がコンテンツへリンク（以前は「準備中」）し、リポジトリイメージを `repo-thumbnailv3.png` に更新。
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)：** レッスン16と17をレッスン毎ガイドと学習パスに追加、「スモークテストによるデプロイ済みエージェントの検証」セクションを追加。
- **[AGENTS.md](./AGENTS.md)：** レッスン数/説明（00–18）を更新、スモークテスト検証セクションを追加、レッスン16/17のサンプル命名例を追加。
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)：** 「前のレッスン」がレッスン17を指すように（従来はレッスン15）、チェーンを完結。
- **非推奨でないモデルの標準化された参照。** コース全体のすべての `gpt-4o` / `gpt-4o-mini` 参照（ドキュメント、`.env.example`、Python/.NETノートブックとサンプル）を `gpt-4.1-mini` に置き換えました。`gpt-4o`（すべてのバージョン）は2026年に廃止予定。レッスン16のモデルルーティング例は `gpt-4.1-mini`（小）と `gpt-4.1`（大）で小・大の対比を維持。Pythonノートブックはモデル名を環境変数（`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`）から選択し、ハードコードはしません。

### メモと既知の制限事項

- **ライブの Azure では実行されていません。** 新レッスンのノートブックは教育用サンプルです。ご自身の Microsoft Foundry / Foundry Local セットアップで実行検証してください。スモークテストワークフローはレッスンのエージェントをデプロイし、Foundry プロジェクト範囲での **Azure AI User** ロールを持つ Azure OIDC シークレット（`AZURE_CLIENT_ID`、`AZURE_TENANT_ID`、`AZURE_SUBSCRIPTION_ID`）の構成を必要とします。
- **レッスン17はローカル限定です。** Foundry Responses エンドポイントがないためスモークテストは適用されず、ノートブックをワークステーションで実行して検証してください。

## [リリース済み] — 2026-07-06

このリリースではコースを **Azure OpenAI Responses API** に移行し、製品名を **Microsoft Foundry** と **Microsoft Agent Framework (MAF)** に統一し、GitHub Models を廃止し、SDKバージョンを更新し、ローカルモデルと Foundry上での他フレームワークのホスティングに関する新しいコンテンツを追加します。

### 追加したもの

- <strong>移行スキル</strong> — [.agents/skills/azure-openai-to-responses/SKILL.md](./.agents/skills/azure-openai-to-responses/SKILL.md) に [`azure-openai-to-responses`](https://github.com/Azure-Samples/azure-openai-to-responses) エージェントスキルをインストール、その参照とスキャナースクリプトを含む。
- **Foundry Local（デバイス上でモデルを実行）** — [00-course-setup/README.md](./00-course-setup/README.md) に新しい「代替プロバイダー：Foundry Local」セクションを追加。インストール方法（`winget` / `brew`）、`foundry model run`、`foundry-local-sdk`、Microsoft Agent Framework への `FoundryLocalManager` を `OpenAIChatClient` 経由で接続する方法を解説。
- **Microsoft Foundry上での LangChain / LangGraph エージェントのホスティング** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) に新セクション追加と、`langchain-azure-ai[hosting]` と `/responses` プロトコルの `ResponsesHostServer` を使った実行可能なサンプル [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)。[Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) を基にしています。
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) に新しい「実例：Microsoft Project Opal」セクションを追加。Opal を企業のコンピュータ利用エージェントとして位置付け、コースの概念（ヒューマン・イン・ザ・ループ、信頼／セキュリティ、計画、スキル）にマッピング。
- **第2のレッスン02 Pythonサンプル** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) を追加（「変更点」参照 — 旧 Semantic Kernel ノートブックから移行）。レッスンREADMEにリンク。
- <strong>モデルとプロバイダー</strong> セクションを [STUDY_GUIDE.md](./STUDY_GUIDE.md) に追加。

### 変更点

- **Chat Completions → Responses API（Python）。** モデルを直接呼び出していたサンプルは Chat Completions から Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) に移行し、`OpenAI` クライアントを安定版の Azure OpenAI `/openai/v1/` エンドポイント（`api_version`なし）で使用。影響を受けるサンプルは以下：
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — 関数呼び出し完全解説（ツールスキーマを Responses フォーマットにフラット化、ツール結果を `function_call_output`、`max_output_tokens` 等で返す）。

- **GitHub Models → Azure OpenAI.** GitHub Models は非推奨になり（**2026年7月に廃止予定**）、Responses API をサポートしていません。すべての GitHub Models コードパスは Python と .NET のサンプルで Azure OpenAI / Microsoft Foundry に変換されました:
  - Python: レッスン08のワークフローノートブック（`01`–`03`）、レッスン14（`14-handoff`、`14-human-loop`、`hotel_booking_workflow_sample.py`）。
  - .NET: `01`–`04`、`07`、`08` の `*-dotnet-agent-framework.cs` と付随する `.md` ドキュメント、およびレッスン08の dotNET ワークフローノートブック/`.md`（`01`–`03`）は現在、`AzureCliCredential` とともに `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` を使用しています。
- **Semantic Kernel → Microsoft Agent Framework.** 以前の `02-semantic-kernel.ipynb` は Microsoft Agent Framework と Azure OpenAI（Responses API）を使うように書き換えられ、ファイル名が `02-python-agent-framework-azure-openai.ipynb` に変更されました。
- **`FoundryChatClient` + `as_agent` に標準化。** `AzureAIProjectAgentProvider` を参照していた README とノートブックのコードは、レッスン01やフレームワーク自身のサンプルで使われている標準パターンに統一されました：`FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` と `provider.as_agent(...)`。レッスン02–14の README・ノートブック全体（例：レッスン13のメモリ、レッスン14のすべてのノートブック、`11-agentic-protocols/code_samples/github-mcp/app.py`）で更新されています。
- **製品名変更。** 英語の内容全体で名称を変更しました：
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - （変更なし: "Azure OpenAI"、"Azure AI Search"、"Azure AI Inference"、および環境変数名）
- <strong>依存関係</strong>（[requirements.txt](../../requirements.txt)）：
  - `agent-framework>=1.10.0`、`agent-framework-foundry>=1.10.0`、`agent-framework-openai>=1.10.0` に固定。
  - Responses API の最小バージョンとして `openai>=1.108.1` に固定。
  - 移行済み GitHub Models サンプルのみで使用されていた `azure-ai-inference` を除去。
- <strong>環境設定</strong>（[.env.example](../../.env.example)）：GitHub Models の変数（`GITHUB_TOKEN`、`GITHUB_ENDPOINT`、`GITHUB_MODEL_ID`）を削除し、`AZURE_OPENAI_ENDPOINT`、`AZURE_OPENAI_DEPLOYMENT`、および任意の `AZURE_OPENAI_API_KEY` を追加。命名を Microsoft Foundry に更新。
- <strong>ドキュメント</strong> — [00-course-setup/README.md](./00-course-setup/README.md)、[AGENTS.md](./AGENTS.md)、[README.md](./README.md)、[STUDY_GUIDE.md](./STUDY_GUIDE.md) を上記に合わせて更新（環境変数設定、確認スニペット、プロバイダーガイダンス、名称など）。

### 削除されたもの

- 設定ドキュメントから GitHub Models のオンボーディング手順と環境変数を削除（Azure OpenAI / Microsoft Foundry に置き換え）。

### セキュリティ / プライバシー（公開共有のクリーンアップ）

- Jupyter ノートブックの実行結果から、実際の **Azure サブスクリプション ID**、リソースグループ・リソース名、Bing 接続 ID と、開発者の <strong>ローカルファイルパスやユーザー名</strong> が漏れていたのを消去しました：
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- トラッキングされている英語のコンテンツ内に API キー、トークン、サブスクリプション ID、個人パスが残っていないことを確認（残っている `GITHUB_TOKEN` は GitHub Actions のワークフロー中のトークンや、レッスン11セットアップの GitHub MCP サーバー PAT であり、正当かつ GitHub Models とは無関係です）。

### 備考と既知の制限

- **実行/コンパイルされていません。** これらは教育用サンプルで、API・名称の正確性のために更新したものであり、実際の Azure リソースで実行されたわけではなく、.NET サンプルはこの環境でのコンパイルもしていません。自身の Microsoft Foundry / Azure OpenAI デプロイメントで検証してください。
- **モデルデプロイメントは Responses API をサポートする必要があります。** `gpt-4.1-mini`、`gpt-4.1`、または `gpt-5.x` モデルのようなデプロイメントを使用してください。古いモデルは Responses の基本機能はサポートしますがすべての機能をサポートしません。
- **Agent-framework のバージョン。** サンプルは最新の MAF（`>=1.10.0`）をターゲットとしています。標準的なエージェント作成呼び出しは `client.as_agent(...)` です。API はフレームワークの公開ドキュメントとインストール済みビルドで検証済みです。別バージョンを固定する場合はメソッドの可用性（`as_agent` と `create_agent`）を確認してください。
- **レッスン08 ワークフローノートブック 04** は意図的に `AzureAIAgentClient`（`agent-framework-azure-ai`由来）を保持しています。Microsoft Foundry Agent Service のホストツール（Bing グラウンディング、コードインタープリター）を使うためであり、すでに Responses ベースです。
- **.NET のデフォルトデプロイメント。** 2つのレッスン08 dotNET ワークフローサンプルは以前は特定モデルをハードコードしていましたが、現在は `AZURE_OPENAI_DEPLOYMENT` （`gpt-4.1-mini`）がデフォルトです。マルチモーダル/ビジョン入力を使うサンプルは、適切なモデルに `AZURE_OPENAI_DEPLOYMENT` を設定してください。
- **Foundry Local** は OpenAI 互換の **Chat Completions** エンドポイントを公開しており、ローカル開発向けです。完全な Responses API 機能セットには Azure OpenAI / Microsoft Foundry を使用してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->