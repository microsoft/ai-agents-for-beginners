# AGENTS.md

## プロジェクト概要

このリポジトリには「初心者向けAIエージェント」— AIエージェントを構築するために必要なすべてを教える包括的な教育コースが含まれています。コースは18のレッスン（番号は00-18）で構成されており、基本、デザインパターン、フレームワーク、製品デプロイメント、ローカル/オンデバイスエージェント、およびAIエージェントのセキュリティをカバーしています。

**主要技術:**
- Python 3.12以上
- 対話型学習のためのJupyterノートブック
- AIフレームワーク: Microsoft Agent Framework (MAF)
- Azure AIサービス: Microsoft Foundry, Microsoft Foundry Agent Service V2

**アーキテクチャ:**
- レッスンごとの構造（00-18 ディレクトリ）
- 各レッスンにはREADMEドキュメント、コードサンプル（Jupyterノートブック）、画像を含む
- 自動翻訳システムによる多言語対応
- Microsoft Agent Frameworkを使用した各レッスンごとのPythonノートブック

## セットアップコマンド

### 前提条件
- Python 3.12以上
- Azureサブスクリプション（Microsoft Foundry用）
- Azure CLIのインストールと認証 (`az login`)

### 初期セットアップ

1. **リポジトリをクローンまたはフォークする:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python仮想環境を作成して有効化する:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **依存関係をインストールする:**
   ```bash
   pip install -r requirements.txt
   ```

4. **環境変数を設定する:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### 必須環境変数

**Microsoft Foundry用**（必須）:
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundryプロジェクトのエンドポイント
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - モデル展開名 (例: gpt-5-mini)

**Azure AI Search用**（レッスン05 - RAG）:
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Searchのエンドポイント
- `AZURE_SEARCH_API_KEY` - Azure AI SearchのAPIキー

認証: ノートブックを実行する前に`az login`を実行してください（`AzureCliCredential`を使用）。

## 開発ワークフロー

### Jupyterノートブックの実行

各レッスンには異なるフレームワーク用の複数のJupyterノートブックがあります:

1. **Jupyterを起動する:**
   ```bash
   jupyter notebook
   ```

2. <strong>レッスンのディレクトリに移動する</strong>（例: `01-intro-to-ai-agents/code_samples/`）

3. **ノートブックを開いて実行する:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework（Python）を使用
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework（.NET）を使用

### Microsoft Agent Frameworkの使用

**Microsoft Agent Framework + Microsoft Foundry:**
- Azureサブスクリプションが必要
- `FoundryChatClient`をAgent Service V2用に使用（Foundryポータルでエージェントが見える）
- 組み込みの監視機能で本番対応
- ファイルパターン: `*-python-agent-framework.ipynb`

## テスト手順

これは例示的なコードを提供する教育用リポジトリであり、自動テスト付きの製品コードではありません。セットアップや変更の確認は以下で行います:

### 手動テスト

1. **Python環境のテスト:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **ノートブック実行のテスト:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **環境変数の検証:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### 個別ノートブックの実行

Jupyterでノートブックを開き、セルを順番に実行します。各ノートブックは独立しており、以下が含まれます:
- インポート文
- 設定の読み込み
- エージェント実装の例
- マークダウンセルに予想される出力

### 配置済みエージェントのスモークテスト

Microsoft Foundryホストエージェントとして配置されているレッスン（01, 04, 05, 16）向けに、`tests/`下にスモークテストカタログが用意されており、`.github/workflows/smoke-test.yml`ワークフローの[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)アクションにより実行されます。これらは軽量のポストデプロイゲート（エージェントは到達可能で基本的なプロンプト期待に従っているか？）として機能し、レッスン10および16の評価パイプラインを補完します。カタログからレッスン、エージェントへのマッピングは[tests/README.md](./tests/README.md)を参照してください。レッスン17はFoundry Localを使ってローカルに実行され、ホストエンドポイントはないため、そのノートブックを直接実行して検証されます。

## コードスタイル

### Python規約

- **Pythonバージョン**: 3.12以上
- <strong>コードスタイル</strong>: 標準Python PEP 8規約に従う
- <strong>ノートブック</strong>: コンセプトを説明する明確なマークダウンセルを使用
- <strong>インポート</strong>: 標準ライブラリ、サードパーティ、ローカルの順にグループ化

### Jupyterノートブック規約

- コードセルの前に説明的なマークダウンセルを含める
- 参考のためにノートブック内に出力例を追加
- レッスンの概念に一致する明確な変数名を使用
- ノートブックの実行順序は線形に保つ（セル1 → 2 → 3...）

### ファイルの整理

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## ビルドとデプロイ

### ドキュメントビルド

このリポジトリはMarkdownでドキュメントを管理しています:
- 各レッスンフォルダ内のREADME.mdファイル
- リポジトリルートのメインREADME.md
- GitHub Actionsによる自動翻訳システム

### CI/CDパイプライン

`.github/workflows/`内にあります:

1. **co-op-translator.yml** - 50以上の言語への自動翻訳
2. **welcome-issue.yml** - 新規イシュー作成者の歓迎
3. **welcome-pr.yml** - 新規プルリクエスト貢献者の歓迎

### デプロイ

これは教育用リポジトリのため、デプロイプロセスはありません。ユーザーは:
1. リポジトリをフォークまたはクローン
2. ローカルまたはGitHub Codespacesでノートブックを実行
3. サンプルを変更・実験して学習

## プルリクエストガイドライン

### 提出前に

1. **変更をテストする:**
   - 影響を受けるノートブックを完全に実行
   - すべてのセルがエラーなしに実行されることを確認
   - 出力が適切であることをチェック

2. **ドキュメントの更新:**
   - 新しい概念を追加した場合はREADME.mdを更新
   - 複雑なコードにはノートブックにコメントを追加
   - マークダウンセルで目的を説明することを確実に

3. **ファイルの変更:**
   - `.env`ファイルのコミットは避ける（代わりに`.env.example`を使用）
   - `venv/`や`__pycache__/`ディレクトリはコミットしない
   - コンセプトを示すノートブックの出力は保持
   - 一時ファイルやバックアップノートブック（`*-backup.ipynb`）は削除

### PRタイトルフォーマット

説明的なタイトルを使用:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### 必須チェック

- ノートブックはエラーなしで実行されること
- READMEファイルは明確かつ正確であること
- 既存のコードパターンに従うこと
- 他のレッスンとの一貫性を維持すること

## 追加の注意事項

### よくある注意点

1. **Pythonバージョンの不一致:**
   - Python 3.12以上を使用していることを確認
   - 古いバージョンでは一部パッケージが動作しない場合がある
   - `python3 -m venv`でPythonバージョンを明示的に指定

2. **環境変数:**
   - 常に`.env`から`.env.example`を作成
   - `.env`ファイルはコミットしない（`.gitignore`に含まれる）
   - キーレスEntra ID認証には`az login`でサインイン

3. **パッケージの競合:**
   - 新しい仮想環境を使用
   - 個別パッケージではなく`requirements.txt`からインストール
   - 一部ノートブックはマークダウンセルで追加パッケージを要求

4. **Azureサービス:**
   - Azure AIサービスは有効なサブスクリプションが必要
   - 一部の機能は地域限定
   - Azure OpenAIモデル展開がResponses APIをサポートしていることを確認

### 学習パス

推奨されるレッスンの進め方:
1. **00-course-setup** - 環境セットアップのスタートポイント
2. **01-intro-to-ai-agents** - AIエージェントの基礎理解
3. **02-explore-agentic-frameworks** - 様々なフレームワークの学習
4. **03-agentic-design-patterns** - 主要なデザインパターン
5. 番号順に続くレッスンを順次進める

### フレームワークの選択

目的に応じてフレームワークを選択:
- <strong>すべてのレッスン</strong>: Microsoft Agent Framework (MAF) と `FoundryChatClient`
- <strong>エージェントはサーバー側で登録</strong> され、Microsoft Foundry Agent Service V2で管理されFoundryポータルで確認可能

### ヘルプを得るには

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)に参加
- 特定のガイダンスはレッスンのREADMEを参照
- コース概要はメインREADME.md[./README.md]を参照
- 詳細なセットアップは[Course Setup](./00-course-setup/README.md)を参照

### 貢献について

これはオープンな教育プロジェクトです。貢献は歓迎します:
- コード例の改善
- 誤字やエラーの修正
- 説明的なコメントの追加
- 新しいレッスントピックの提案
- 追加言語への翻訳

現在のニーズは[GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues)を参照。

## プロジェクト特有の文脈

### 多言語対応

このリポジトリは自動翻訳システムを使用:
- 50以上の言語に対応
- 翻訳は`/translations/<lang-code>/`ディレクトリに格納
- GitHub Actionsのワークフローで翻訳を更新
- ソースファイルはリポジトリルートの英語版

### レッスン構成

各レッスンは一貫したパターンに従う:
1. 動画のサムネイルとリンク
2. 書面によるレッスン内容（README.md）
3. 複数フレームワークのコードサンプル
4. 学習目標と前提条件
5. 追加の学習リソースへのリンク

### コードサンプルの命名

形式: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - レッスン1、MAF Python
- `14-sequential.ipynb` - レッスン14、MAF高度パターン
- `16-python-agent-framework.ipynb` - レッスン16、本番用途顧客サポートエージェント
- `17-local-agent-foundry-local.ipynb` - レッスン17、Foundry Local + Qwenによるローカルエージェント

### 特別なディレクトリ

- `translated_images/` - 翻訳用のローカライズ画像
- `images/` - 英語コンテンツ用のオリジナル画像
- `.devcontainer/` - VS Code開発コンテナ設定
- `.github/` - GitHub Actionsのワークフローとテンプレート

### 依存パッケージ

`requirements.txt`からの主要パッケージ:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agentプロトコルサポート
- `azure-ai-inference`, `azure-ai-projects` - Azure AIサービス
- `azure-identity` - Azure認証（AzureCliCredential）
- `azure-search-documents` - Azure AI Search統合
- `mcp[cli]` - モデルコンテキストプロトコルサポート

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->