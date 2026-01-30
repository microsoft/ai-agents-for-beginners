# AGENTS.md

## プロジェクト概要

このリポジトリは「初心者向けAIエージェント」を含んでおり、AIエージェントを構築するために必要なすべてを学べる包括的な教育コースです。このコースは、基礎、デザインパターン、フレームワーク、AIエージェントの本番環境へのデプロイをカバーする15以上のレッスンで構成されています。

**主要技術:**
- Python 3.12以上
- インタラクティブ学習用のJupyter Notebooks
- AIフレームワーク: Semantic Kernel、AutoGen、Microsoft Agent Framework (MAF)
- Azure AIサービス: Azure AI Foundry、Azure AI Agent Service
- GitHub Models Marketplace (無料プランあり)

**アーキテクチャ:**
- レッスンベースの構造 (00-15以上のディレクトリ)
- 各レッスンにはREADMEドキュメント、コードサンプル (Jupyter Notebooks)、画像が含まれる
- 自動翻訳システムによる多言語対応
- 各レッスンで複数のフレームワークオプション (Semantic Kernel、AutoGen、Azure AI Agent Service)

## セットアップコマンド

### 必要条件
- Python 3.12以上
- GitHubアカウント (GitHub Modelsの無料プラン用)
- Azureサブスクリプション (オプション、Azure AIサービス用)

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

**GitHub Models (無料)** 用:
- `GITHUB_TOKEN` - GitHubの個人アクセストークン

**Azure AIサービス** (オプション) 用:
- `PROJECT_ENDPOINT` - Azure AI Foundryプロジェクトのエンドポイント
- `AZURE_OPENAI_API_KEY` - Azure OpenAI APIキー
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAIエンドポイントURL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - チャットモデルのデプロイメント名
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - 埋め込みモデルのデプロイメント名
- `.env.example`に記載されている追加のAzure設定

## 開発ワークフロー

### Jupyter Notebooksの実行

各レッスンには異なるフレームワーク用の複数のJupyter Notebookが含まれています:

1. **Jupyterを起動する:**
   ```bash
   jupyter notebook
   ```

2. **レッスンディレクトリに移動する** (例: `01-intro-to-ai-agents/code_samples/`)

3. **ノートブックを開いて実行する:**
   - `*-semantic-kernel.ipynb` - Semantic Kernelフレームワークを使用
   - `*-autogen.ipynb` - AutoGenフレームワークを使用
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) を使用
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) を使用
   - `*-azureaiagent.ipynb` - Azure AI Agent Serviceを使用

### 異なるフレームワークの利用

**Semantic Kernel + GitHub Models:**
- GitHubアカウントで無料プラン利用可能
- 学習と実験に最適
- ファイルパターン: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- GitHubアカウントで無料プラン利用可能
- マルチエージェントのオーケストレーション機能
- ファイルパターン: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Microsoftの最新フレームワーク
- Pythonと.NETで利用可能
- ファイルパターン: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Azureサブスクリプションが必要
- 本番環境向けの機能
- ファイルパターン: `*-azureaiagent.ipynb`

## テスト手順

このリポジトリは教育目的の例コードを含んでおり、自動テストを備えた本番コードではありません。セットアップや変更を確認するには以下を行います:

### 手動テスト

1. **Python環境をテストする:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **ノートブックの実行をテストする:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **環境変数を確認する:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### 個別ノートブックの実行

Jupyterでノートブックを開き、セルを順番に実行します。各ノートブックは自己完結型で以下を含みます:
- インポート文
- 設定の読み込み
- エージェントの例実装
- マークダウンセルに期待される出力

## コードスタイル

### Pythonの規約

- **Pythonバージョン**: 3.12以上
- **コードスタイル**: 標準Python PEP 8規約に従う
- **ノートブック**: 概念を説明する明確なマークダウンセルを使用
- **インポート**: 標準ライブラリ、サードパーティ、ローカルインポートの順にグループ化

### Jupyter Notebookの規約

- コードセルの前に説明的なマークダウンセルを含める
- 参考用にノートブックに出力例を追加
- レッスンの概念に一致する明確な変数名を使用
- ノートブックの実行順序を線形に保つ (セル1 → 2 → 3...)

### ファイル構成

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## ビルドとデプロイ

### ドキュメントのビルド

このリポジトリはMarkdownを使用してドキュメントを作成しています:
- 各レッスンフォルダ内のREADME.mdファイル
- リポジトリルートのメインREADME.md
- GitHub Actionsによる自動翻訳システム

### CI/CDパイプライン

`.github/workflows/`に配置されています:

1. **co-op-translator.yml** - 50以上の言語への自動翻訳
2. **welcome-issue.yml** - 新しいIssue作成者への歓迎メッセージ
3. **welcome-pr.yml** - 新しいプルリクエスト投稿者への歓迎メッセージ

### デプロイ

このリポジトリは教育目的のため、デプロイプロセスはありません。ユーザーは以下を行います:
1. リポジトリをフォークまたはクローン
2. ノートブックをローカルまたはGitHub Codespacesで実行
3. 例を変更して実験しながら学習

## プルリクエストガイドライン

### 提出前

1. **変更をテストする:**
   - 影響を受けたノートブックを完全に実行
   - すべてのセルがエラーなく実行されることを確認
   - 出力が適切であることを確認

2. **ドキュメントの更新:**
   - 新しい概念を追加する場合はREADME.mdを更新
   - 複雑なコードにはノートブックにコメントを追加
   - マークダウンセルが目的を説明していることを確認

3. **ファイルの変更:**
   - `.env`ファイルをコミットしない (`.env.example`を使用)
   - `venv/`や`__pycache__/`ディレクトリをコミットしない
   - 概念を示す場合はノートブックの出力を保持
   - 一時ファイルやバックアップノートブック (`*-backup.ipynb`) を削除

### PRタイトル形式

説明的なタイトルを使用:
- `[Lesson-XX] <概念>の新しい例を追加`
- `[Fix] lesson-XX READMEの誤字を修正`
- `[Update] lesson-XXのコードサンプルを改善`
- `[Docs] セットアップ手順を更新`

### 必須チェック

- ノートブックがエラーなく実行されること
- READMEファイルが明確で正確であること
- リポジトリ内の既存のコードパターンに従うこと
- 他のレッスンとの一貫性を維持すること

## 追加の注意事項

### よくある問題

1. **Pythonバージョンの不一致:**
   - Python 3.12以上を使用すること
   - 一部のパッケージは古いバージョンでは動作しない可能性あり
   - `python3 -m venv`を使用してPythonバージョンを明示的に指定

2. **環境変数:**
   - 常に`.env.example`から`.env`を作成
   - `.env`ファイルをコミットしない (`.gitignore`に含まれている)
   - GitHubトークンには適切な権限が必要

3. **パッケージの競合:**
   - 新しい仮想環境を使用
   - 個別のパッケージではなく`requirements.txt`からインストール
   - 一部のノートブックにはマークダウンセルに記載された追加パッケージが必要

4. **Azureサービス:**
   - Azure AIサービスには有効なサブスクリプションが必要
   - 一部の機能は地域限定
   - GitHub Modelsの無料プランには制限あり

### 学習パス

レッスンの推奨進行順:
1. **00-course-setup** - 環境セットアップから開始
2. **01-intro-to-ai-agents** - AIエージェントの基礎を理解
3. **02-explore-agentic-frameworks** - 異なるフレームワークについて学ぶ
4. **03-agentic-design-patterns** - コアデザインパターン
5. 番号付きレッスンを順番に進める

### フレームワークの選択

目標に応じてフレームワークを選択:
- **学習/プロトタイピング**: Semantic Kernel + GitHub Models (無料)
- **マルチエージェントシステム**: AutoGen
- **最新機能**: Microsoft Agent Framework (MAF)
- **本番環境デプロイ**: Azure AI Agent Service

### ヘルプを得る

- [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)に参加
- 特定のガイダンスについてはレッスンREADMEファイルを確認
- コース概要についてはメイン[README.md](./README.md)を確認
- 詳細なセットアップ手順については[Course Setup](./00-course-setup/README.md)を参照

### コントリビューション

このプロジェクトはオープンな教育プロジェクトです。コントリビューションを歓迎します:
- コード例の改善
- 誤字やエラーの修正
- 明確なコメントの追加
- 新しいレッスンテーマの提案
- 追加の言語への翻訳

現在のニーズについては[GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues)を確認してください。

## プロジェクト固有のコンテキスト

### 多言語対応

このリポジトリは自動翻訳システムを使用しています:
- 50以上の言語をサポート
- `/translations/<lang-code>/`ディレクトリに翻訳が保存
- GitHub Actionsワークフローが翻訳の更新を処理
- ソースファイルはリポジトリルートに英語で保存

### レッスン構造

各レッスンは一貫したパターンに従います:
1. 動画サムネイルとリンク
2. 書かれたレッスン内容 (README.md)
3. 複数フレームワークのコードサンプル
4. 学習目標と前提条件
5. リンクされた追加学習リソース

### コードサンプルの命名

形式: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - レッスン4、Semantic Kernel
- `07-autogen.ipynb` - レッスン7、AutoGen
- `14-python-agent-framework.ipynb` - レッスン14、MAF Python
- `14-dotnet-agent-framework.ipynb` - レッスン14、MAF .NET

### 特別なディレクトリ

- `translated_images/` - 翻訳用のローカライズ画像
- `images/` - 英語コンテンツ用の元画像
- `.devcontainer/` - VS Code開発コンテナ設定
- `.github/` - GitHub Actionsワークフローとテンプレート

### 依存関係

`requirements.txt`からの主要パッケージ:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGenフレームワーク
- `semantic-kernel` - Semantic Kernelフレームワーク
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AIサービス
- `azure-search-documents` - Azure AI Search統合
- `chromadb` - RAG例用のベクターデータベース
- `chainlit` - チャットUIフレームワーク
- `browser_use` - エージェント用ブラウザ自動化
- `mcp[cli]` - モデルコンテキストプロトコルサポート
- `mem0ai` - エージェント用メモリ管理

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文（元の言語で記載された文書）が信頼できる情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。