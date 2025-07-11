<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "76945069b52a49cd0432ae3e0b0ba22e",
  "translation_date": "2025-07-03T00:00:00+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ja"
}
-->

# コースのセットアップ

## GitHubサンプルを実行するためのセットアップ

### ステップ1: GitHubトークンの作成

GitHubアカウントでログインしてください。

画面左側の「Fine-grained tokens」オプションを選択します。

次に「Generate new token」を選択します。

![トークンの生成](../../../00-course-setup/images/generate-token.png)

トークンの名前を入力し、有効期限を選択（推奨：30日間）し、トークンのスコープ（公開リポジトリ）を選択するよう求められます。

このトークンの権限を編集することも必要です：「Permissions」→「Models」→「Allows access to GitHub Models」を選択してください。

作成したばかりの新しいトークンをコピーしてください。これを、このコースに含まれる`.env`ファイルに追加します。

### ステップ2: `.env`ファイルの作成

`.env`ファイルを作成するには、ターミナルで以下のコマンドを実行します：

```bash
cp .env.example .env
```

これにより、サンプルファイルがコピーされて、ディレクトリに`.env`ファイルが作成されます。このファイルに環境変数の値を入力します。

トークンをコピーしたら、お好みのテキストエディタで`.env`ファイルを開き、`GITHUB_TOKEN`フィールドにトークンを貼り付けます。

これで、このコースのコードサンプルを実行できるようになりました。

## Azure AI FoundryとAzure AIエージェントサービスを使用するサンプルのセットアップ

### ステップ1: Azure プロジェクトエンドポイントの取得

Azure AI Foundryでハブとプロジェクトを作成する手順は、こちらを参照してください：[ハブリソースの概要](https://learn.microsoft.com/ja-jp/azure/ai-foundry/concepts/ai-resources)

プロジェクトを作成したら、プロジェクトの接続文字列を取得する必要があります。

これはAzure AI Foundryポータルのプロジェクトの**概要**ページで確認できます。

![プロジェクト接続文字列](../../../00-course-setup/images/project-endpoint.png)

### ステップ2: `.env`ファイルの作成

`.env`ファイルを作成するには、ターミナルで以下のコマンドを実行します：

```bash
cp .env.example .env
```

これにより、サンプルファイルがコピーされて、ディレクトリに`.env`ファイルが作成されます。このファイルに環境変数の値を入力します。

トークンをコピーしたら、お好みのテキストエディタで`.env`ファイルを開き、`PROJECT_ENDPOINT`フィールドにトークンを貼り付けます。

### ステップ3: Azureにサインイン

セキュリティのベストプラクティスとして、Microsoft Entra IDを使用して[キーレス認証](https://learn.microsoft.com/ja-jp/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst)でAzure OpenAIに認証します。まず、お使いのオペレーティングシステムに合わせた[インストール手順](https://learn.microsoft.com/ja-jp/cli/azure/install-azure-cli?WT.mc_id=academic-105485-koreyst)に従って**Azure CLI**をインストールする必要があります。

次に、ターミナルを開き、`az login --use-device-code`を実行してAzureアカウントにサインインします。

ログインしたら、ターミナルでサブスクリプションを選択します。

## 追加の環境変数 - Azure SearchとAzure OpenAI

エージェントRAGレッスン（レッスン5）では、Azure SearchとAzure OpenAIを使用するサンプルがあります。

これらのサンプルを実行したい場合は、`.env`ファイルに以下の環境変数を追加する必要があります：

### 概要ページ（プロジェクト）

- `AZURE_SUBSCRIPTION_ID` - プロジェクトの**概要**ページの**プロジェクトの詳細**を確認してください。

- `AZURE_AI_PROJECT_NAME` - プロジェクトの**概要**ページの上部を確認してください。

- `AZURE_OPENAI_SERVICE` - **概要**ページの**含まれる機能**タブの**Azure OpenAI Service**で確認できます。

### 管理センター

- `AZURE_OPENAI_RESOURCE_GROUP` - **管理センター**の**概要**ページの**プロジェクトのプロパティ**に移動します。

- `GLOBAL_LLM_SERVICE` - **接続されたリソース**の下で、**Azure AIサービス**接続名を見つけます。リストにない場合は、リソースグループのAIサービスリソース名を**Azureポータル**で確認してください。

### モデル + エンドポイントページ

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - 埋め込みモデル（例：`text-embedding-ada-002`）を選択し、モデルの詳細から**デプロイメント名**を確認します。

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - チャットモデル（例：`gpt-4o-mini`）を選択し、モデルの詳細から**デプロイメント名**を確認します。

### Azureポータル

- `AZURE_OPENAI_ENDPOINT` - **Azure AIサービス**を探し、クリックして**リソース管理**、**キーとエンドポイント**に移動し、下にスクロールして「Azure OpenAIエンドポイント」を確認し、「Language APIs」と書かれているものをコピーします。

- `AZURE_OPENAI_API_KEY` - 同じ画面から、キー1またはキー2をコピーします。

- `AZURE_SEARCH_SERVICE_ENDPOINT` - **Azure AI Search**リソースを見つけ、クリックして**概要**を確認します。

- `AZURE_SEARCH_API_KEY` - **設定**に移動し、**キー**からプライマリまたはセカンダリ管理者キーをコピーします。

### 外部ウェブページ

- `AZURE_OPENAI_API_VERSION` - [APIバージョンのライフサイクル](https://learn.microsoft.com/ja-jp/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release)ページの**最新のGA APIリリース**を確認してください。

### キーレス認証のセットアップ

認証情報をハードコードする代わりに、Azure OpenAIとキーレス接続を使用します。そのために、`DefaultAzureCredential`をインポートし、後で`DefaultAzureCredential`関数を呼び出して認証情報を取得します。

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## 問題が発生した場合は？

セットアップで問題が発生した場合は、お気軽にお問い合わせください。

## 次のレッスン

これで、このコースのコードを実行する準備が整いました。AIエージェントの世界をもっと学んで楽しんでください！

[AIエージェントの紹介とエージェントのユースケース](../01-intro-to-ai-agents/README.md)

**免責事項**：  
本文書はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。原文の言語によるオリジナル文書が権威ある情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。
