# AGENTS.md

## プロジェクト概要

このリポジトリには「初心者向けAIエージェント」- AIエージェントを構築するために必要なすべてを教える包括的な教育コースが含まれています。コースは基礎、デザインパターン、フレームワーク、およびAIエージェントの本番展開をカバーする15以上のレッスンで構成されています。

**主要技術:**
- Python 3.12+
- インタラクティブ学習のためのJupyterノートブック
- AIフレームワーク: Microsoft Agent Framework (MAF)
- Azure AIサービス: Microsoft Foundry, Azure AI Foundry Agent Service V2

**アーキテクチャ:**
- レッスンベース構成 (00-15+ ディレクトリ)
- 各レッスンにはREADMEドキュメント、コードサンプル（Jupyterノートブック）、画像が含まれる
- 自動翻訳システムによる多言語サポート
- 各レッスンにMicrosoft Agent Frameworkを使ったPythonノートブックが1つずつ

## セットアップコマンド

### 前提条件
- Python 3.12以上
- Azureサブスクリプション（Azure AI Foundry用）
- Azure CLIがインストールされログイン済み (`az login`)

### 初期セットアップ

1. **リポジトリをクローンまたはフォーク:**
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
   # APIキーとエンドポイントで.envを編集してください
   ```

### 必須環境変数

**Azure AI Foundry**（必須）:
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundryプロジェクトのエンドポイント
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - モデルのデプロイメント名（例：gpt-4o）

**Azure AI Search**（レッスン05 - RAG 用）:
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Searchエンドポイント
- `AZURE_SEARCH_API_KEY` - Azure AI SearchのAPIキー

認証: ノートブックを実行する前に `az login` を実行してください（`AzureCliCredential` を使用）。

## 開発ワークフロー

### Jupyterノートブックの実行

各レッスンには複数のフレームワーク用のJupyterノートブックが含まれています:

1. **Jupyterを起動:**
   ```bash
   jupyter notebook
   ```

2. **レッスンディレクトリに移動**（例: `01-intro-to-ai-agents/code_samples/`）

3. **ノートブックを開いて実行:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework（Python版）
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework（.NET版）

### Microsoft Agent Framework の使用

**Microsoft Agent Framework + Azure AI Foundry:**
- Azureサブスクリプションが必要
- Agent Service V2向けの `AzureAIProjectAgentProvider` を使用（エージェントはFoundryポータルから閲覧可能）
- 本番対応可能で組み込みの可視化機能付き
- ファイルパターン: `*-python-agent-framework.ipynb`

## テスト手順

このリポジトリは例示的なコードを含む教育用であり、自動化されたテストを備えた本番コードではありません。セットアップと変更の検証には以下を行ってください。

### 手動テスト

1. **Python環境のテスト:**
   ```bash
   python --version  # 3.12以上である必要があります
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **ノートブックの実行テスト:**
   ```bash
   # ノートブックをスクリプトに変換して実行する（インポートのテスト）
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **環境変数の確認:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### 個別ノートブックの実行

Jupyterでノートブックを開きセルを順に実行してください。各ノートブックは独立しており以下を含みます：
- インポート文
- 設定の読み込み
- エージェントの実装例
- マークダウンセルでの期待される出力説明

## コードスタイル

### Pythonの規約

- **Pythonバージョン**: 3.12以上
- **コードスタイル**: 標準Python PEP 8規約に従う
- **ノートブック**: 概念を説明する明確なマークダウンセルを使用
- **インポート**: 標準ライブラリ、サードパーティ、ローカルの順にグループ化

### Jupyterノートブック規約

- コードの前に説明的なマークダウンセルを含める
- ノートブックに出力例を含める
- レッスンの概念に対応した分かりやすい変数名を使用
- ノートブックは順序通り実行可能（セル1 → 2 → 3...）

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

### ドキュメントのビルド

このリポジトリはMarkdownで文書化しています:
- 各レッスンフォルダのREADME.md
- リポジトリルートのメインREADME.md
- GitHub Actionsによる自動翻訳システム

### CI/CDパイプライン

`.github/workflows/` 配下にあります:

1. **co-op-translator.yml** - 50以上の言語への自動翻訳
2. **welcome-issue.yml** - 新しいIssue作成者歓迎
3. **welcome-pr.yml** - 新しいPull Request作成者歓迎

### デプロイ

教育用リポジトリのためデプロイプロセスはありません。ユーザーは:
1. リポジトリをフォークまたはクローン
2. ローカルもしくはGitHub Codespacesでノートブックを実行
3. 例を改変・実験しながら学習

## プルリクエストガイドライン

### 提出前に

1. **変更のテスト:**
   - 対象ノートブックを全て実行
   - 全セルがエラーなく実行されることを確認
   - 出力が適切であることを確認

2. **ドキュメントの更新:**
   - 新しい概念を追加した場合はREADME.mdも更新
   - 複雑なコードにはノートブック内にコメントを追加
   - マークダウンセルで目的を説明

3. **ファイル変更:**
   - `.env` ファイルはコミットしない（ `.env.example` を使用）
   - `venv/` または `__pycache__/` ディレクトリはコミットしない
   - 概念を示す出力はノートブックに残す
   - 一時ファイルやバックアップノートブック (`*-backup.ipynb`) は削除

### PRタイトルフォーマット

説明的なタイトルを使用:
- `[Lesson-XX] <概念> の新しい例を追加`
- `[Fix] レッスンXXのREADMEの誤字訂正`
- `[Update] レッスンXXのコードサンプル改善`
- `[Docs] セットアップ手順の更新`

### 必須チェック

- ノートブックはエラーなく実行可能であること
- READMEファイルは明確かつ正確であること
- リポジトリ内の既存パターンに従うこと
- 他レッスンとの整合性を保つこと

## 追加注意事項

### よくある落とし穴

1. **Pythonバージョン不一致:**
   - Python 3.12以上を使用していることを確認
   - 古いバージョンは一部パッケージが動作しない場合あり
   - `python3 -m venv` で明示的にバージョン指定可能

2. **環境変数:**
   - 必ず `.env.example` から `.env` を作成
   - `.env` ファイルは `.gitignore` に記載のためコミットしない
   - GitHubトークンには適切な権限が必要

3. **パッケージ競合:**
   - 新規仮想環境を使用
   - 個別にではなく `requirements.txt` からインストール
   - 一部ノートブックはマークダウンセルで追加パッケージを案内

4. **Azureサービス:**
   - Azure AIサービスは有効なサブスクリプションが必須
   - 一部機能は地域限定の場合あり
   - GitHub Modelsの無料プラン制限あり

### 学習の進め方

推奨されるレッスン順序:
1. **00-course-setup** - 環境構築の開始地点
2. **01-intro-to-ai-agents** - AIエージェントの基礎理解
3. **02-explore-agentic-frameworks** - 複数フレームワークの学習
4. **03-agentic-design-patterns** - 主なデザインパターン
5. 数字順に順次進める

### フレームワーク選択

目的に応じて選択:
- **すべてのレッスン**: Microsoft Agent Framework (MAF) を `AzureAIProjectAgentProvider` と共に使用
- **エージェントはサーバー側に登録され**、Azure AI Foundry Agent Service V2およびFoundryポータルで閲覧可能

### ヘルプを得る方法

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) に参加
- 各レッスンのREADMEを参照
- メインの [README.md](./README.md) でコース概要を確認
- 詳細なセットアップは [Course Setup](./00-course-setup/README.md) を参照

### コントリビューション

これはオープンな教育プロジェクトです。貢献大歓迎:
- コード例の改善
- 誤字脱字の修正
- コメントの追加
- 新しいレッスンテーマの提案
- 追加言語への翻訳

現在の要望は [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) をご覧ください。

## プロジェクト固有のコンテキスト

### 多言語サポート

このリポジトリは自動翻訳システムを使用しています:
- 50以上の言語に対応
- 翻訳は `/translations/<言語コード>/` ディレクトリに配置
- GitHub Actionsのワークフローが翻訳更新を管理
- ソースファイルは英語でリポジトリルートにあります

### レッスン構成

各レッスンでは以下のパターンに従います:
1. ビデオのサムネイルとリンク
2. 書面によるレッスン内容 (README.md)
3. 複数フレームワークのコードサンプル
4. 学習目標と前提条件
5. 追加学習リソースへのリンク

### コードサンプルの命名

フォーマット: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - レッスン1、MAF Python版
- `14-sequential.ipynb` - レッスン14、MAFの応用パターン

### 特殊ディレクトリ

- `translated_images/` - 翻訳用ローカライズされた画像
- `images/` - 英語版オリジナル画像
- `.devcontainer/` - VS Code開発コンテナ設定
- `.github/` - GitHub Actionsワークフローやテンプレート

### 依存関係

`requirements.txt` の主要パッケージ:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agentプロトコル対応
- `azure-ai-inference`, `azure-ai-projects` - Azure AIサービス用
- `azure-identity` - Azure認証 (AzureCliCredential)
- `azure-search-documents` - Azure AI Search統合
- `mcp[cli]` - Model Context Protocolサポート

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご了承ください。原文は母国語で記述されたものが正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の使用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->