<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T11:40:34+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ja"
}
-->
# コースセットアップ

## はじめに

このレッスンでは、このコースのコードサンプルを実行する方法について説明します。

## 他の学習者と交流し、助けを得る

リポジトリをクローンする前に、[AI Agents For Beginners Discordチャンネル](https://aka.ms/ai-agents/discord)に参加してください。セットアップに関するヘルプやコースに関する質問、他の学習者との交流ができます。

## このリポジトリをクローンまたはフォークする

まず、GitHubリポジトリをクローンまたはフォークしてください。これにより、コース教材の自分専用のバージョンを作成し、コードを実行、テスト、調整することができます。

以下のリンクをクリックして、<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">リポジトリをフォーク</a>してください。

これで、以下のリンクにこのコースのフォーク版が作成されます。

![フォークされたリポジトリ](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.ja.png)

### 浅いクローン（ワークショップやCodespacesに推奨）

  >リポジトリ全体をダウンロードすると、履歴やすべてのファイルを含むため、サイズが大きくなることがあります（約3GB）。ワークショップに参加する場合や特定のレッスンフォルダのみが必要な場合は、浅いクローン（またはスパースクローン）を使用することで、ダウンロード量を大幅に削減できます。

#### 簡易浅いクローン — 最小限の履歴、すべてのファイル

以下のコマンドで`<your-username>`をフォークURL（または好みに応じてアップストリームURL）に置き換えてください。

最新のコミット履歴のみをクローンするには（ダウンロード量が少ない）：

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

特定のブランチをクローンするには：

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分（スパース）クローン — 最小限のデータ + 選択したフォルダのみ

これは部分クローンとスパースチェックアウトを使用します（Git 2.25+が必要で、部分クローンをサポートする最新のGitを推奨）。

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

リポジトリフォルダに移動します：

bashの場合：

```bash
cd ai-agents-for-beginners
```

Powershellの場合：

```powershell
Set-Location ai-agents-for-beginners
```

次に、必要なフォルダを指定します（以下の例では2つのフォルダを示しています）：

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

クローンしてファイルを確認した後、ファイルのみが必要で、スペースを解放したい場合（Git履歴は不要）、リポジトリのメタデータを削除してください（💀不可逆 — Git機能はすべて失われます：コミット、プル、プッシュ、履歴アクセスができなくなります）。

Linux/macOSの場合：

```bash
rm -rf .git
```

Windowsの場合：

```powershell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespacesを使用する（ローカルでの大規模ダウンロードを避けるために推奨）

- [GitHub UI](https://github.com/codespaces)を通じて、このリポジトリの新しいCodespaceを作成します。

- 新しく作成されたCodespaceのターミナルで、上記の浅い/スパースクローンコマンドのいずれかを実行し、必要なレッスンフォルダのみをCodespaceワークスペースに取り込みます。
- オプション：Codespaces内でクローンした後、.gitを削除して余分なスペースを回収します（削除コマンドは上記を参照）。
- 注意：リポジトリを直接Codespacesで開くことを好む場合、Codespacesはdevcontainer環境を構築し、必要以上のプロビジョニングを行う可能性があります。新しいCodespace内で浅いコピーをクローンすることで、ディスク使用量をよりコントロールできます。

#### ヒント

- 編集やコミットを行いたい場合は、常にクローンURLを自分のフォークに置き換えてください。
- 後で履歴やファイルがさらに必要になった場合は、それらをフェッチしたり、スパースチェックアウトを調整して追加のフォルダを含めることができます。

## コードの実行

このコースでは、AIエージェントを構築する実践的な経験を得るための一連のJupyter Notebookを提供しています。

コードサンプルは以下のいずれかを使用します：

**GitHubアカウントが必要 - 無料**：

1) Semantic Kernel Agent Framework + GitHub Models Marketplace（semantic-kernel.ipynbとしてラベル付け）
2) AutoGen Framework + GitHub Models Marketplace（autogen.ipynbとしてラベル付け）

**Azureサブスクリプションが必要**：
3) Azure AI Foundry + Azure AI Agent Service（azureaiagent.ipynbとしてラベル付け）

これら3つの例をすべて試してみて、どれが最適かを確認することをお勧めします。

選択したオプションに応じて、以下のセットアップ手順が必要になります：

## 必要条件

- Python 3.12+
  - **NOTE**: Python3.12がインストールされていない場合は、インストールしてください。その後、python3.12を使用してvenvを作成し、requirements.txtファイルから正しいバージョンをインストールしてください。
  
    >例

    Python venvディレクトリを作成：

    ``` bash
    python3 -m venv venv
    ```

    次に、venv環境をアクティブ化します：

    macOSとLinuxの場合：

    ```bash
    source venv/bin/activate
    ```
  
    Windowsの場合：

    ```bash
    venv\Scripts\activate
    ```

- GitHubアカウント - GitHub Models Marketplaceへのアクセス用
- Azureサブスクリプション - Azure AI Foundryへのアクセス用
- Azure AI Foundryアカウント - Azure AI Agent Serviceへのアクセス用

このリポジトリのルートには、コードサンプルを実行するために必要なPythonパッケージを含む`requirements.txt`ファイルが含まれています。

以下のコマンドをリポジトリのルートでターミナルに入力してインストールできます：

```bash
pip install -r requirements.txt
```
Python仮想環境を作成することをお勧めします。これにより、競合や問題を回避できます。

## VSCodeのセットアップ
VSCodeで正しいバージョンのPythonを使用していることを確認してください。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Modelsを使用したサンプルのセットアップ

### ステップ1: GitHub個人アクセストークン（PAT）を取得する

このコースではGitHub Models Marketplaceを活用し、AIエージェントを構築するために使用する大規模言語モデル（LLM）への無料アクセスを提供します。

GitHub Modelsを使用するには、[GitHub個人アクセストークン](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)を作成する必要があります。

GitHubアカウントの<a href="https://github.com/settings/personal-access-tokens" target="_blank">個人アクセストークン設定</a>に移動して作成できます。

トークンを作成する際は、[最小権限の原則](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely)に従ってください。つまり、このコースのコードサンプルを実行するために必要な権限のみをトークンに付与するべきです。

1. **開発者設定**に移動し、画面左側の`Fine-grained tokens`オプションを選択します。
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.ja.png)

    次に、`Generate new token`を選択します。

    ![トークン生成](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.ja.png)

2. トークンの目的を反映した説明的な名前を入力し、後で簡単に識別できるようにします。

    🔐 トークンの有効期間の推奨

    推奨期間: 30日間  
    より安全な設定を希望する場合は、7日間などの短期間を選択することもできます 🛡️  
    これは個人的な目標を設定し、学習の勢いが高い間にコースを完了する素晴らしい方法です 🚀。

    ![トークン名と有効期限](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.ja.png)

3. トークンのスコープをこのリポジトリのフォークに制限します。

    ![フォークリポジトリへのスコープ制限](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.ja.png)

4. トークンの権限を制限します：**Permissions**の下で**Account**タブをクリックし、"+ Add permissions"ボタンをクリックします。ドロップダウンが表示されます。**Models**を検索し、チェックボックスをオンにしてください。
    ![Models権限を追加](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.ja.png)

5. トークンを生成する前に、必要な権限を確認してください。 ![権限確認](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.ja.png)

6. トークンを生成する前に、パスワードマネージャーの保管庫など安全な場所にトークンを保存する準備ができていることを確認してください。生成後は再表示されません。 ![トークンを安全に保存](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.ja.png)

作成した新しいトークンをコピーしてください。このトークンをこのコースに含まれる`.env`ファイルに追加します。

### ステップ2: `.env`ファイルを作成する

ターミナルで以下のコマンドを実行して`.env`ファイルを作成します。

```bash
cp .env.example .env
```

これにより、例のファイルがコピーされ、ディレクトリ内に`.env`ファイルが作成されます。環境変数の値を入力してください。

コピーしたトークンを使用して、お気に入りのテキストエディタで`.env`ファイルを開き、トークンを`GITHUB_TOKEN`フィールドに貼り付けます。
![GitHubトークンフィールド](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.ja.png)

これで、このコースのコードサンプルを実行できるようになります。

## Azure AI FoundryとAzure AI Agent Serviceを使用したサンプルのセットアップ

### ステップ1: Azureプロジェクトエンドポイントを取得する

Azure AI Foundryでのハブとプロジェクトの作成手順については、[ハブリソースの概要](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)をご覧ください。

プロジェクトを作成したら、プロジェクトの接続文字列を取得する必要があります。

これは、Azure AI Foundryポータルのプロジェクトの**概要**ページに移動することで行えます。

![プロジェクト接続文字列](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.ja.png)

### ステップ2: `.env`ファイルを作成する

ターミナルで以下のコマンドを実行して`.env`ファイルを作成します。

```bash
cp .env.example .env
```

これにより、例のファイルがコピーされ、ディレクトリ内に`.env`ファイルが作成されます。環境変数の値を入力してください。

コピーしたトークンを使用して、お気に入りのテキストエディタで`.env`ファイルを開き、トークンを`PROJECT_ENDPOINT`フィールドに貼り付けます。

### ステップ3: Azureにサインインする

セキュリティのベストプラクティスとして、Microsoft Entra IDを使用した[キーなし認証](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst)を使用してAzure OpenAIに認証します。

次に、ターミナルを開き、`az login --use-device-code`を実行してAzureアカウントにサインインします。

ログインしたら、ターミナルでサブスクリプションを選択してください。

## 追加の環境変数 - Azure SearchとAzure OpenAI

Agentic RAGレッスン - レッスン5 - では、Azure SearchとAzure OpenAIを使用するサンプルがあります。

これらのサンプルを実行するには、以下の環境変数を`.env`ファイルに追加する必要があります：

### 概要ページ（プロジェクト）

- `AZURE_SUBSCRIPTION_ID` - プロジェクトの**概要**ページの**プロジェクト詳細**を確認してください。

- `AZURE_AI_PROJECT_NAME` - プロジェクトの**概要**ページの上部を確認してください。

- `AZURE_OPENAI_SERVICE` - **概要**ページの**含まれる機能**タブで**Azure OpenAI Service**を確認してください。

### 管理センター

- `AZURE_OPENAI_RESOURCE_GROUP` - **管理センター**の**概要**ページで**プロジェクトプロパティ**を確認してください。

- `GLOBAL_LLM_SERVICE` - **接続されたリソース**の下で**Azure AI Services**接続名を見つけてください。リストにない場合は、リソースグループ内のAzureポータルでAI Servicesリソース名を確認してください。

### モデル + エンドポイントページ

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - 埋め込みモデル（例：`text-embedding-ada-002`）を選択し、モデル詳細から**デプロイメント名**を確認してください。

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - チャットモデル（例：`gpt-4o-mini`）を選択し、モデル詳細から**デプロイメント名**を確認してください。

### Azureポータル

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services**を探し、クリックして**リソース管理**、**キーとエンドポイント**に移動し、「Azure OpenAIエンドポイント」の「言語API」をコピーしてください。

- `AZURE_OPENAI_API_KEY` - 同じ画面からKEY 1またはKEY 2をコピーしてください。

- `AZURE_SEARCH_SERVICE_ENDPOINT` - **Azure AI Search**リソースを見つけてクリックし、**概要**を確認してください。

- `AZURE_SEARCH_API_KEY` - 次に**設定**に移動し、**キー**でプライマリまたはセカンダリ管理キーをコピーしてください。

### 外部ウェブページ

- `AZURE_OPENAI_API_VERSION` - [APIバージョンライフサイクル](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release)ページの**最新のGA APIリリース**を確認してください。

### キーなし認証のセットアップ

資格情報をハードコードする代わりに、Azure OpenAIとのキーなし接続を使用します。そのために、`DefaultAzureCredential`をインポートし、後で`DefaultAzureCredential`関数を呼び出して資格情報を取得します。

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## どこかで詰まっていますか？
セットアップを実行する際に問題が発生した場合は、<a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>に参加するか、<a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">問題を作成</a>してください。

## 次のレッスン

これで、このコースのコードを実行する準備が整いました。AIエージェントの世界についてさらに学ぶことを楽しんでください！

[AIエージェントとその利用ケースの紹介](../01-intro-to-ai-agents/README.md)

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。