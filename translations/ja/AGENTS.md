# AGENTS.md

## プロジェクト概要

このリポジトリには「初心者向けAIエージェント」- AIエージェント構築に必要なすべてを網羅した教育コースが含まれています。コースは18のレッスン（00-18番号付け）で構成され、基礎、デザインパターン、フレームワーク、実運用展開、ローカル/デバイス上のエージェント、AIエージェントのセキュリティを扱います。

**主要技術:**
- Python 3.12以上
- インタラクティブ学習用Jupyterノートブック
- AIフレームワーク: Microsoft Agent Framework (MAF)
- Azure AIサービス: Microsoft Foundry, Microsoft Foundry Agent Service V2

**アーキテクチャ:**
- レッスンベースの構成（00-15以上のディレクトリ）
- 各レッスンはREADMEドキュメント、コードサンプル（Jupyterノートブック）、画像を含む
- 自動翻訳システムによる多言語対応
- Microsoft Agent Frameworkを使用したレッスンごとのPythonノートブック

## セットアップコマンド

### 前提条件
- Python 3.12またはそれ以上
- Azureサブスクリプション（Microsoft Foundry用）
- Azure CLIのインストールと認証済み (`az login`)

### 初期セットアップ

1. **リポジトリのクローンまたはフォーク:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # または
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python仮想環境の作成と有効化:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
   ```

3. **依存関係のインストール:**
   ```bash
   pip install -r requirements.txt
   ```

4. **環境変数の設定:**
   ```bash
   cp .env.example .env
   # APIキーとエンドポイントを含む.envファイルを編集してください
   ```

### 必須環境変数

**Microsoft Foundry用** (必須):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundryプロジェクトエンドポイント
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - モデル展開名（例：gpt-5-mini）

**Azure AI Search用** (レッスン05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Searchエンドポイント
- `AZURE_SEARCH_API_KEY` - Azure AI Search APIキー

認証: ノートブックを実行する前に `az login` を実行してください（`AzureCliCredential` を使用）。

## 開発ワークフロー

### Jupyterノートブックの実行

各レッスンには異なるフレームワーク用の複数のJupyterノートブックが含まれます:

1. **Jupyter起動:**
   ```bash
   jupyter notebook
   ```

2. <strong>レッスンディレクトリに移動</strong>（例：`01-intro-to-ai-agents/code_samples/`）

3. **ノートブックを開いて実行:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) 使用
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) 使用

### Microsoft Agent Frameworkの操作

**Microsoft Agent Framework + Microsoft Foundry:**
- Azureサブスクリプション必須
- Agent Service V2用`FoundryChatClient`を使用（Foundryポータルでエージェント確認可能）
- 実運用対応の組み込みオブザーバビリティあり
- ファイルパターン: `*-python-agent-framework.ipynb`

## テスト手順

これは教育用リポジトリで、例示コードを提供し、自動テストを備えた運用コードではありません。セットアップや変更の確認手順は以下です:

### 手動テスト

1. **Python環境のテスト:**
   ```bash
   python --version  # 3.12以上である必要があります
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **ノートブック実行のテスト:**
   ```bash
   # ノートブックをスクリプトに変換して実行（テストのインポート）
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **環境変数の検証:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### 個別ノートブックの実行

Jupyterでノートブックを開きセルを順に実行してください。各ノートブックは自己完結型で以下を含みます:
- インポート文
- 設定の読み込み
- 例示的なエージェント実装
- 期待される出力を示すマークダウンセル

### 配備済みエージェントのスモークテスト

エージェントがMicrosoft Foundryホストエージェントとして配備されているレッスン（01, 04, 05, 16）では、 `tests/` 以下にスモークテストカタログがあり、`.github/workflows/smoke-test.yml` ワークフローで [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) アクションを使って実行されます。これらは軽量のデプロイ後ゲート（エージェントが到達可能で基本プロンプトに応答しているか）で、レッスン10と16の評価パイプラインの補完です。カタログからレッスン、エージェントへの対応は [tests/README.md](./tests/README.md) を参照してください。レッスン17はFoundry Localでローカル実行し、ホストエンドポイントはないため、ノートブック直接実行で検証されます。

## コードスタイル

### Python規約

- **Pythonバージョン**: 3.12以上
- <strong>コードスタイル</strong>: 標準Python PEP 8に準拠
- <strong>ノートブック</strong>: 概念説明の明確なマークダウンセル使用
- <strong>インポート</strong>: 標準ライブラリ、サードパーティ、ローカル別にグループ化

### Jupyterノートブック規約

- コードセル前に説明的なマークダウンセルを含める
- 参照用の出力例をノートブック内に記載
- レッスンの概念に合ったわかりやすい変数名を使用
- ノートブックの実行順は線形（セル1 → 2 → 3...）

### ファイル構成

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

### ドキュメント構築

リポジトリはMarkdownドキュメントを使用:
- 各レッスンフォルダのREADME.mdファイル
- リポジトリルートのメインREADME.md
- GitHub Actionsによる自動翻訳システム

### CI/CDパイプライン

`.github/workflows/` に配置:

1. **co-op-translator.yml** - 50以上の言語への自動翻訳
2. **welcome-issue.yml** - 新規Issue作成者への歓迎
3. **welcome-pr.yml** - 新規プルリクエスト提出者への歓迎

### 展開

これは教育用リポジトリで、展開プロセスはありません。ユーザーは:
1. リポジトリをフォークまたはクローン
2. ローカルまたはGitHub Codespacesでノートブックを実行
3. 例を編集・試行して学習

## プルリクエストガイドライン

### 提出前に

1. **変更のテスト:**
   - 影響を受けるノートブックを完全に実行
   - 全セルがエラーなしに実行されることを確認
   - 出力が適切であることをチェック

2. **ドキュメント更新:**
   - 新規概念追加時はREADME.mdを更新
   - 複雑なコードにはノートブック内でコメント追加
   - マークダウンセルで目的を説明

3. **ファイル変更:**
   - `.env` ファイルはコミット避ける（`.env.example`を使用）
   - `venv/` や `__pycache__/` ディレクトリはコミット不可
   - 概念説明のためノートブック出力は保持
   - 一時ファイルやバックアップノートブック（ `*-backup.ipynb` ）は削除

### PRタイトルフォーマット

説明的なタイトルを使用:
- `[Lesson-XX] <概念>の新しい例を追加`
- `[Fix] lesson-XX READMEのタイプミス修正`
- `[Update] lesson-XXのコードサンプル改善`
- `[Docs] セットアップ手順更新`

### 必須チェック

- ノートブックはエラーなく実行されること
- READMEは明確かつ正確であること
- リポジトリ内既存コードパターンに従うこと
- 他のレッスンとの一貫性を保つこと

## 追加の注意点

### よくある落とし穴

1. **Pythonバージョンの不一致:**
   - Python 3.12以上の使用を確認
   - 古いバージョンでは動作しないパッケージあり
   - `python3 -m venv` でPythonバージョンを明示指定可能

2. **環境変数:**
   - `.env.example` から必ず `.env` を作成
   - `.env` ファイルはコミットしない（`.gitignore`入り）
   - キーレスEntra ID認証のために `az login` でログイン

3. **パッケージ競合:**
   - 新規仮想環境を使用
   - 個別パッケージより `requirements.txt` からインストール
   - 一部ノートブックはマークダウンセルに追加パッケージ要件アリ

4. **Azureサービス:**
   - Azure AIサービスは有効なサブスクリプションが必要
   - 一部機能はリージョン限定
   - Azure OpenAIモデル展開がResponses APIをサポートしていることを確認

### 学習パス

推奨進行順序:
1. **00-course-setup** - 環境セットアップをここから始める
2. **01-intro-to-ai-agents** - AIエージェントの基礎理解
3. **02-explore-agentic-frameworks** - さまざまなフレームワークの学習
4. **03-agentic-design-patterns** - コアデザインパターン
5. 番号順にレッスンを順次進める

### フレームワークの選択

目的に応じて以下を選択:
- <strong>全レッスン共通</strong>: Microsoft Agent Framework (MAF) と `FoundryChatClient`
- <strong>サーバー側にエージェント登録</strong> はMicrosoft Foundry Agent Service V2で、Foundryポータルから確認可能

### ヘルプの取得

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) に参加
- 各レッスンのREADMEファイルで具体的なガイダンスを確認
- コース概要はメインの [README.md](./README.md) を参照
- 詳細セットアップは [Course Setup](./00-course-setup/README.md) を参照

### コントリビューション

これはオープンな教育プロジェクトです。貢献歓迎:
- コード例の改善
- タイプミスや誤りの修正
- 説明コメントの追加
- 新しいレッスンテーマの提案
- 他言語への翻訳

現在のニーズは [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) を参照してください。

## プロジェクト固有の文脈

### 多言語対応

このリポジトリは自動翻訳システムを使用:
- 50以上の言語をサポート
- `/translations/<lang-code>/` 内に翻訳ファイル
- GitHub Actionsワークフローで翻訳更新を管理
- ソースファイルはリポジトリルートに英文

### レッスン構成

各レッスンの一貫したパターン:
1. リンク付き動画サムネイル
2. 書面によるレッスン内容（README.md）
3. 複数フレームワークでのコードサンプル
4. 学習目標と前提条件
5. 追加学習リソースのリンク

### コードサンプルの命名

フォーマット: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - レッスン1、MAF Python
- `14-sequential.ipynb` - レッスン14、MAF高度パターン
- `16-python-agent-framework.ipynb` - レッスン16、実運用の顧客サポートエージェント
- `17-local-agent-foundry-local.ipynb` - レッスン17、Foundry Local + Qwenによるローカルエージェント

### 特殊ディレクトリ

- `translated_images/` - 翻訳用ローカライズ画像
- `images/` - 英語コンテンツのオリジナル画像
- `.devcontainer/` - VS Code開発コンテナ設定
- `.github/` - GitHub Actionsワークフローとテンプレート

### 依存関係

`requirements.txt` の主要パッケージ:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - エージェント間プロトコルサポート
- `azure-ai-inference`, `azure-ai-projects` - Azure AIサービス
- `azure-identity` - Azure認証（AzureCliCredential）
- `azure-search-documents` - Azure AI Search統合
- `mcp[cli]` - モデルコンテキストプロトコルサポート

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->