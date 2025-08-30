<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c55b973b1562abf5aadf6a4028265ac5",
  "translation_date": "2025-08-30T07:49:41+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ja"
}
-->
# コースセットアップ

## はじめに

このレッスンでは、このコースのコードサンプルを実行する方法について説明します。

## 他の学習者と交流し、助けを得る

リポジトリをクローンする前に、[AI Agents For Beginners Discordチャンネル](https://aka.ms/ai-agents/discord)に参加してください。セットアップに関するヘルプやコースに関する質問、他の学習者との交流ができます。

## リポジトリをクローンまたはフォークする

まず、GitHubリポジトリをクローンまたはフォークしてください。これにより、コース教材の自分専用のバージョンが作成され、コードを実行、テスト、調整することができます。

リンクをクリックすることでこれを行うことができます。

![フォークされたリポジトリ](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.ja.png)

## コードの実行

このコースでは、AIエージェントを構築する実践的な経験を得るための一連のJupyter Notebookを提供しています。

コードサンプルは以下のいずれかを使用します：

**GitHubアカウントが必要 - 無料**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace (autogen.ipynb)

**Azureサブスクリプションが必要**:
3) Azure AI Foundry + Azure AI Agent Service (azureaiagent.ipynb)

3つの例をすべて試してみて、自分に最適なものを見つけることをお勧めします。

選択したオプションに応じて、以下のセットアップ手順が異なります。

## 必要条件

- Python 3.12以上
  - **NOTE**: Python3.12がインストールされていない場合は、インストールしてください。その後、python3.12を使用してvenvを作成し、requirements.txtファイルから正しいバージョンをインストールしてください。
- GitHubアカウント - GitHub Models Marketplaceへのアクセス用
- Azureサブスクリプション - Azure AI Foundryへのアクセス用
- Azure AI Foundryアカウント - Azure AI Agent Serviceへのアクセス用

このリポジトリのルートには、コードサンプルを実行するために必要なPythonパッケージを含む`requirements.txt`ファイルが含まれています。

以下のコマンドをリポジトリのルートでターミナルで実行することでインストールできます：

```bash
pip install -r requirements.txt
```
Python仮想環境を作成することをお勧めします。これにより、競合や問題を回避できます。

## VSCodeのセットアップ
VSCodeで正しいバージョンのPythonを使用していることを確認してください。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Modelsを使用したサンプルのセットアップ

### ステップ1: GitHub Personal Access Token (PAT)を取得する

このコースではGitHub Models Marketplaceを利用し、AIエージェントを構築するために使用する大規模言語モデル（LLM）への無料アクセスを提供します。

GitHub Modelsを使用するには、[GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)を作成する必要があります。

これはGitHubアカウントで以下の手順を実行することで行えます。

最小権限の原則（[Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely)）に従ってトークンを作成してください。つまり、このコースのコードサンプルを実行するために必要な権限のみをトークンに付与するべきです。

1. **Developer settings**に移動し、画面左側の`Fine-grained tokens`オプションを選択します。
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.ja.png)

    次に`Generate new token`を選択します。

    ![トークン生成](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.ja.png)

2. トークンの目的を反映した説明的な名前を入力し、後で簡単に識別できるようにします。

    🔐 トークンの有効期間の推奨

    推奨期間: 30日間  
    より安全な設定を希望する場合は、7日間などの短期間を選択することもできます 🛡️  
    これは個人的な目標を設定し、学習の勢いが高い間にコースを完了する素晴らしい方法です 🚀。

    ![トークン名と有効期限](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.ja.png)

3. トークンのスコープをこのリポジトリのフォークに限定します。

    ![スコープをフォークリポジトリに限定](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.ja.png)

4. トークンの権限を制限します: **Permissions**の下で**Account**タブをクリックし、`+ Add permissions`ボタンをクリックします。ドロップダウンが表示されます。**Models**を検索し、チェックボックスをオンにしてください。
    ![Models権限を追加](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.ja.png)

5. トークンを生成する前に、必要な権限を確認してください。 ![権限確認](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.ja.png)

6. トークンを生成する前に、パスワードマネージャーの保管庫など安全な場所にトークンを保存する準備ができていることを確認してください。生成後は再表示されません。 ![トークンを安全に保存](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.ja.png)

作成した新しいトークンをコピーしてください。このトークンをこのコースに含まれる`.env`ファイルに追加します。

### ステップ2: `.env`ファイルを作成する

ターミナルで以下のコマンドを実行して`.env`ファイルを作成します。

```bash
cp .env.example .env
```

これにより、例のファイルがコピーされ、ディレクトリ内に`.env`ファイルが作成されます。このファイルに環境変数の値を入力します。

コピーしたトークンを使用して、お気に入りのテキストエディタで`.env`ファイルを開き、`GITHUB_TOKEN`フィールドにトークンを貼り付けます。
![GitHubトークンフィールド](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.ja.png)

これで、このコースのコードサンプルを実行できるようになります。

## Azure AI FoundryとAzure AI Agent Serviceを使用したサンプルのセットアップ

### ステップ1: Azureプロジェクトエンドポイントを取得する

Azure AI Foundryでハブとプロジェクトを作成する手順については、[Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)を参照してください。

プロジェクトを作成したら、プロジェクトの接続文字列を取得する必要があります。

これはAzure AI Foundryポータルのプロジェクトの**概要**ページに移動することで行えます。

![プロジェクト接続文字列](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.ja.png)

### ステップ2: `.env`ファイルを作成する

ターミナルで以下のコマンドを実行して`.env`ファイルを作成します。

```bash
cp .env.example .env
```

これにより、例のファイルがコピーされ、ディレクトリ内に`.env`ファイルが作成されます。このファイルに環境変数の値を入力します。

コピーしたトークンを使用して、お気に入りのテキストエディタで`.env`ファイルを開き、`PROJECT_ENDPOINT`フィールドにトークンを貼り付けます。

### ステップ3: Azureにサインインする

セキュリティのベストプラクティスとして、Microsoft Entra IDを使用してAzure OpenAIに認証するために[キーなし認証](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst)を使用します。

次に、ターミナルを開き、`az login --use-device-code`を実行してAzureアカウントにサインインします。

ログイン後、ターミナルでサブスクリプションを選択します。

## 追加の環境変数 - Azure SearchとAzure OpenAI

エージェント型RAGレッスン - レッスン5 - では、Azure SearchとAzure OpenAIを使用するサンプルがあります。

これらのサンプルを実行するには、以下の環境変数を`.env`ファイルに追加する必要があります：

### 概要ページ（プロジェクト）

- `AZURE_SUBSCRIPTION_ID` - プロジェクトの**概要**ページの**プロジェクト詳細**を確認してください。

- `AZURE_AI_PROJECT_NAME` - プロジェクトの**概要**ページの上部を確認してください。

- `AZURE_OPENAI_SERVICE` - **Azure OpenAI Service**の**概要**ページの**含まれる機能**タブで確認してください。

### 管理センター

- `AZURE_OPENAI_RESOURCE_GROUP` - **管理センター**の**概要**ページの**プロジェクトプロパティ**を確認してください。

- `GLOBAL_LLM_SERVICE` - **接続されたリソース**の下で**Azure AI Services**の接続名を確認してください。リストされていない場合は、**Azureポータル**でリソースグループ内のAI Servicesリソース名を確認してください。

### モデル + エンドポイントページ

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - 埋め込みモデル（例: `text-embedding-ada-002`）を選択し、モデル詳細から**デプロイメント名**を確認してください。

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - チャットモデル（例: `gpt-4o-mini`）を選択し、モデル詳細から**デプロイメント名**を確認してください。

### Azureポータル

- `AZURE_OPENAI_ENDPOINT` - **Azure AI Services**を探し、クリックして**リソース管理**、**キーとエンドポイント**に移動し、「Azure OpenAIエンドポイント」の「Language APIs」をコピーしてください。

- `AZURE_OPENAI_API_KEY` - 同じ画面からKEY 1またはKEY 2をコピーしてください。

- `AZURE_SEARCH_SERVICE_ENDPOINT` - **Azure AI Search**リソースを探し、クリックして**概要**を確認してください。

- `AZURE_SEARCH_API_KEY` - 次に**設定**、**キー**に移動して、プライマリまたはセカンダリ管理キーをコピーしてください。

### 外部ウェブページ

- `AZURE_OPENAI_API_VERSION` - [APIバージョンライフサイクル](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release)ページの**最新GA APIリリース**を参照してください。

### キーなし認証のセットアップ

資格情報をハードコードする代わりに、Azure OpenAIとのキーなし接続を使用します。そのために`DefaultAzureCredential`をインポートし、後で`DefaultAzureCredential`関数を呼び出して資格情報を取得します。

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## どこかでつまずいた場合

セットアップを実行する際に問題がある場合は、私たちの

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された原文が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用に起因する誤解や誤認について、当方は一切の責任を負いません。