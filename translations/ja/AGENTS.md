# AGENTS.md

## プロジェクト概要

このリポジトリには「初心者向けAIエージェント」— AIエージェント構築に必要なすべてを教える包括的な教育コースが含まれています。コースは15以上のレッスンで構成され、基礎、設計パターン、フレームワーク、AIエージェントの本番環境への展開をカバーしています。

**主要技術：**
- Python 3.12以上
- インタラクティブ学習用Jupyterノートブック
- AIフレームワーク：Microsoft Agent Framework (MAF)
- Azure AIサービス：Microsoft Foundry、Azure AI Foundry Agent Service V2

**アーキテクチャ：**
- レッスンベースの構造（00〜15以上のディレクトリ）
- 各レッスンにはREADMEドキュメント、コードサンプル（Jupyterノートブック）、画像を含む
- 自動翻訳システムによる多言語対応
- Microsoft Agent Frameworkを使用した各レッスン1つのPythonノートブック

## セットアップコマンド

### 前提条件
- Python 3.12以上
- Azureサブスクリプション（Azure AI Foundry用）
- Azure CLI がインストールされログイン済み (`az login`)

### 初期セットアップ

1. **リポジトリをクローンまたはフォーク：**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # または
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python仮想環境の作成と有効化：**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
   ```

3. **依存関係のインストール：**
   ```bash
   pip install -r requirements.txt
   ```

4. **環境変数の設定：**
   ```bash
   cp .env.example .env
   # APIキーとエンドポイントを含む.envを編集してください
   ```

### 必須環境変数

**Azure AI Foundry 用（必須）：**
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry プロジェクトのエンドポイント
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - モデル展開名（例：gpt-4o）

**Azure AI Search 用（レッスン05 - RAG）：**
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search エンドポイント
- `AZURE_SEARCH_API_KEY` - Azure AI Search APIキー

認証：ノートブック実行前に `az login` を実行してください（`AzureCliCredential` を使用）。

## 開発ワークフロー

### Jupyterノートブックの実行

各レッスンには異なるフレームワーク用の複数のノートブックがあります：

1. **Jupyterを起動：**
   ```bash
   jupyter notebook
   ```

2. **レッスンディレクトリに移動（例：`01-intro-to-ai-agents/code_samples/`）**

3. **ノートブックを開いて実行：**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework（Python使用）
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework（.NET使用）

### Microsoft Agent Frameworkの利用

**Microsoft Agent Framework + Azure AI Foundry：**
- Azureサブスクリプションが必要
- Agent Service V2用の `AzureAIProjectAgentProvider` を使用（Foundryポータルにエージェントが表示される）
- 本番環境対応、組み込みの可観測性あり
- ファイルパターン：`*-python-agent-framework.ipynb`

## テスト手順

このリポジトリは教育用であり、例示コードが中心で自動テストはありません。セットアップや変更を検証するには：

### 手動テスト

1. **Python環境のテスト：**
   ```bash
   python --version  # 3.12以上である必要があります
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **ノートブック実行のテスト：**
   ```bash
   # ノートブックをスクリプトに変換して実行（インポートのテスト）
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **環境変数の確認：**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### 個別ノートブックの実行方法

Jupyterでノートブックを開き、セルを順番に実行してください。各ノートブックは自己完結型で、以下を含みます：
- インポート文
- 設定の読み込み
- エージェント実装の例
- マークダウンセルでの期待される出力

## コードスタイル

### Pythonの慣習

- **Pythonバージョン**：3.12以上
- **コードスタイル**：標準的なPython PEP 8に従う
- **ノートブック**：概念説明のため明快なマークダウンセルを使用
- **インポート**：標準ライブラリ、サードパーティ、ローカルの順にグループ化

### Jupyterノートブックの慣習

- コードセル前に説明的なマークダウンセルを含める
- ノートブック内に出力例を追加して参照可能にする
- レッスンの概念に合うわかりやすい変数名を使用
- ノートブックの実行順序を線形に保つ（セル 1 → 2 → 3…）

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

本リポジトリはMarkdownでドキュメントを管理：
- 各レッスンフォルダ内のREADME.mdファイル
- リポジトリルートのメインREADME.md
- GitHub Actionsによる自動翻訳システム

### CI/CDパイプライン

`.github/workflows/` に配置：

1. **co-op-translator.yml** - 50以上の言語への自動翻訳
2. **welcome-issue.yml** - 新規イシュー作成者への歓迎メッセージ
3. **welcome-pr.yml** - 新規プルリクエスト作成者への歓迎メッセージ

### デプロイ

教育用リポジトリのためデプロイプロセスはなし。ユーザーは：
1. リポジトリをフォークまたはクローン
2. ローカルまたはGitHub Codespacesでノートブックを実行
3. 例を変更・実験して学習

## プルリクエストガイドライン

### 提出前に

1. **変更をテスト：**
   - 関連ノートブックを完全に実行
   - 全セルがエラーなく実行されることを確認
   - 出力が適切か検証

2. **ドキュメントの更新：**
   - 新概念追加時にはREADME.mdも更新
   - 複雑なコードにはノートブック内にコメントを追加
   - マークダウンセルで目的を説明

3. **ファイルの変更：**
   - `.env` ファイルはコミットしない（代わりに `.env.example`）
   - `venv/` や `__pycache__/` もコミット不要
   - 概念説明用のノートブック出力は保持
   - 一時ファイルやバックアップノートブック (`*-backup.ipynb`) は削除

### PRタイトル形式

記述的なタイトルを使う：
- `[Lesson-XX] <概念> の新しい例を追加`
- `[Fix] レッスンXX READMEの誤字修正`
- `[Update] レッスンXX のコードサンプルを改善`
- `[Docs] セットアップ手順を更新`

### 必須チェック

- ノートブックはエラーなく実行できること
- READMEは明確で正確であること
- 既存のコードパターンに従うこと
- 他のレッスンとの整合性を保つこと

## 付加情報

### よくある問題点

1. **Pythonバージョン不一致：**
   - Python 3.12以上を使用すること
   - 古いバージョンでは動作しないパッケージがある
   - `python3 -m venv`でバージョン明示し仮想環境を作成

2. **環境変数：**
   - `.env.example` から `.env` を作成すること
   - `.env` は `.gitignore` に含まれておりコミットしない
   - GitHubトークンは適切な権限が必要

3. **パッケージ競合：**
   - 新規の仮想環境を使用
   - 個別インストールせず `requirements.txt` からインストール
   - 一部ノートブックはマークダウンセルで追加パッケージが必要と記載

4. **Azureサービス：**
   - Azure AIサービスは有効なサブスクリプションが必要
   - 一部機能は地域制限あり
   - GitHub Modelsは無料枠制限あり

### 学習経路

推奨されるレッスンの進め方：
1. **00-course-setup** - 環境セットアップの開始
2. **01-intro-to-ai-agents** - AIエージェント基礎理解
3. **02-explore-agentic-frameworks** - 様々なフレームワークを学ぶ
4. **03-agentic-design-patterns** - コアデザインパターン
5. 以降、番号順に進む

### フレームワーク選定

目的に応じて選択：
- **すべてのレッスン**：Microsoft Agent Framework (MAF) と `AzureAIProjectAgentProvider`
- **Azure AI Foundry Agent Service V2** にサーバーサイドでエージェント登録し、Foundryポータルに表示

### 助けを得るには

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) に参加
- 各レッスンREADMEで具体的な案内を確認
- メインの [README.md](./README.md) でコース全体概要を確認
- 詳細セットアップは [Course Setup](./00-course-setup/README.md) を参照

### コントリビューション

本プロジェクトはオープンな教育プロジェクトです。歓迎する貢献：
- コード例の改善
- タイポや不具合修正
- コメント追加による説明強化
- 新レッスンテーマの提案
- 追加言語への翻訳

現在のニーズは [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) で確認可能。

## プロジェクト固有のコンテキスト

### 多言語対応

本リポジトリは自動翻訳システムを採用：
- 50言語以上対応
- `/translations/<lang-code>/` ディレクトリに翻訳ファイル
- GitHub Actionsのワークフローで翻訳更新管理
- 英語のソースファイルはリポジトリルートに配置

### レッスン構成

各レッスンは次の一貫したパターン：
1. 動画サムネイルとリンク
2. レッスン本文（README.md）
3. 複数フレームワークのコードサンプル
4. 学習目標と前提条件
5. 追加学習リソースのリンク

### コードサンプルの命名規則

形式：`<レッスン番号>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - レッスン1、MAF Python版
- `14-sequential.ipynb` - レッスン14、MAF高度パターン

### 特殊ディレクトリ

- `translated_images/` - 翻訳用ローカライズ画像
- `images/` - 英語版画像
- `.devcontainer/` - VS Code開発コンテナ設定
- `.github/` - GitHub Actionsワークフローやテンプレート

### 依存関係

`requirements.txt`の主なパッケージ：
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - エージェント間プロトコルサポート
- `azure-ai-inference`, `azure-ai-projects` - Azure AIサービス
- `azure-identity` - Azure認証（AzureCliCredential）
- `azure-search-documents` - Azure AI Search統合
- `mcp[cli]` - モデルコンテキストプロトコルサポート

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されました。正確性の確保に努めておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。正式な情報源としては、原文の言語版を参照してください。重要な内容については、専門の人間翻訳を推奨いたします。本翻訳の利用により生じた誤解や解釈の相違に関して、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->