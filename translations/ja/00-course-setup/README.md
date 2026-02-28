# コースの設定

## はじめに

このレッスンでは、このコースのコードサンプルの実行方法について説明します。

## 他の学習者に参加してヘルプを得る

リポジトリをクローンする前に、セットアップのヘルプやコースに関する質問、他の学習者とのつながりを得るために [AI Agents For Beginners Discord チャンネル](https://aka.ms/ai-agents/discord) に参加してください。

## このリポジトリをクローンまたはフォークする

始めるには、GitHub リポジトリをクローンまたはフォークしてください。これにより、コードを実行、テスト、調整できる自分用のコース素材のバージョンが作成されます。

これは、<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">リポジトリをフォークする</a> リンクをクリックすることで行えます。

次のリンクに、このコースのフォークした自分用バージョンが表示されているはずです：

![フォークされたリポジトリ](../../../translated_images/ja/forked-repo.33f27ca1901baa6a.webp)

### 浅いクローン（ワークショップ / Codespaces に推奨）

  > 完全な履歴とすべてのファイルをダウンロードすると、リポジトリ全体は大きくなることがあります（約3 GB）。ワークショップに参加している場合や一部のレッスンフォルダだけが必要な場合は、浅いクローン（またはスパースクローン）を使うことで履歴を短縮したり blob をスキップしたりしてほとんどのダウンロードを回避できます。

#### クイック浅いクローン — 最小限の履歴、すべてのファイル

以下のコマンド内の `<your-username>` をフォークの URL（または必要に応じて upstream の URL）に置き換えてください。

最新のコミット履歴のみをクローンする（ダウンロードが小さい）には：

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

特定のブランチをクローンするには：

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分クローン（スパース） — 最小限の blob ＋ 選択したフォルダのみ

これは partial clone と sparse-checkout を使用します（Git 2.25+ が必要で、partial clone をサポートする最新の Git を推奨）：

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

リポジトリフォルダに移動：

```bash|powershell
cd ai-agents-for-beginners
```

次に、必要なフォルダを指定します（以下の例は2つのフォルダを示しています）：

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

クローンしてファイルを確認した後、ファイルだけが必要でディスク領域を解放したい場合は（git の履歴は不要）、リポジトリのメタデータを削除してください（💀不可逆 — すべての Git 機能が失われます：コミット、pull、push、履歴へのアクセスができなくなります）。

```bash
# zshとbash
rm -rf .git
```

```powershell
# パワーシェル
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces の利用（ローカルの大きなダウンロードを避けるために推奨）

- このリポジトリの新しい Codespace を [GitHub の UI](https://github.com/codespaces) から作成します。  

- 新しく作成した Codespace のターミナルで、上記の浅い/スパースクローンのコマンドのいずれかを実行して、必要なレッスンフォルダのみを Codespace ワークスペースに取り込みます。
- 任意：Codespaces 内でクローンした後、追加のディスク領域を回収するために .git を削除します（上記の削除コマンドを参照）。
- 注意：リポジトリを直接 Codespaces で開く（追加のクローンなし）場合、Codespaces は devcontainer 環境を構築し、必要以上にプロビジョニングする可能性があります。新しい Codespace 内で浅いコピーをクローンすると、ディスク使用量をより細かく制御できます。

#### ヒント

- 編集やコミットを行う場合は、必ずクローン URL を自分のフォークに置き換えてください。
- 後でさらに履歴やファイルが必要になった場合は、それらを取得（fetch）するか、sparse-checkout を調整して追加フォルダを含めることができます。

## コードの実行

このコースでは、AI エージェントの構築を実践的に学べる一連の Jupyter ノートブックを提供しています。

コードサンプルは、`AzureAIProjectAgentProvider` を使用する **Microsoft Agent Framework (MAF)** を利用しており、**Microsoft Foundry** 経由で **Azure AI Agent Service V2**（Responses API）に接続します。

すべての Python ノートブックは `*-python-agent-framework.ipynb` とラベル付けされています。

## 要件

- Python 3.12+
  - **NOTE**: Python3.12 がインストールされていない場合は、必ずインストールしてください。requirements.txt から正しいバージョンがインストールされるよう、python3.12 を使って仮想環境を作成してください。
  
    >Example

    Python の venv ディレクトリを作成：

    ```bash|powershell
    python -m venv venv
    ```

    次に venv 環境をアクティブ化：

    ```bash
    # zsh と bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET を使用するサンプルコードのために、[.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 以降をインストールしてください。インストールした .NET SDK のバージョンを確認します：

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — 認証に必要です。[aka.ms/installazurecli](https://aka.ms/installazurecli) からインストールしてください。
- **Azure Subscription** — Microsoft Foundry と Azure AI Agent Service へのアクセスに必要です。
- **Microsoft Foundry Project** — デプロイ済みモデルを含むプロジェクト（例: `gpt-4o`）。以下の [ステップ 1](../../../00-course-setup) を参照してください。

このリポジトリのルートには、コードサンプルを実行するために必要なすべての Python パッケージを含む `requirements.txt` ファイルを同梱しています。

リポジトリのルートで次のコマンドを実行してインストールできます：

```bash|powershell
pip install -r requirements.txt
```

競合や問題を避けるために、Python の仮想環境を作成することを推奨します。

## VSCode のセットアップ

VSCode で正しいバージョンの Python を使用していることを確認してください。

![画像](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry と Azure AI Agent Service の設定

### ステップ 1：Microsoft Foundry プロジェクトの作成

ノートブックを実行するには、デプロイ済みモデルを含む Azure AI Foundry のハブ（hub）とプロジェクトが必要です。

1. [ai.azure.com](https://ai.azure.com) にアクセスし、Azure アカウントでサインインします。
2. ハブ（hub）を作成するか既存のものを使用します。参照: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)。
3. ハブ内でプロジェクトを作成します。
4. **Models + Endpoints** → **Deploy model** からモデル（例: `gpt-4o`）をデプロイします。

### ステップ 2：プロジェクトのエンドポイントとモデルデプロイ名を取得する

Microsoft Foundry ポータル内のプロジェクトから：

- **Project Endpoint** — **Overview** ページに移動して、エンドポイントの URL をコピーします。

![プロジェクト接続文字列](../../../translated_images/ja/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** に移動し、デプロイしたモデルを選択して **Deployment name** を確認します（例: `gpt-4o`）。

### ステップ 3：`az login` で Azure にサインイン

すべてのノートブックは認証に **`AzureCliCredential`** を使用します — 管理する API キーは不要です。これには Azure CLI でサインインしている必要があります。

1. 未インストールの場合は **Azure CLI** をインストールしてください: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. 次を実行してサインインします：

    ```bash|powershell
    az login
    ```

    リモート/Codespace 環境でブラウザが使えない場合：

    ```bash|powershell
    az login --use-device-code
    ```

3. プロンプトが表示されたらサブスクリプションを選択します — Foundry プロジェクトが含まれるサブスクリプションを選んでください。

4. サインインが完了していることを確認します：

    ```bash|powershell
    az account show
    ```

> **なぜ `az login` が必要なのか？** ノートブックは `azure-identity` パッケージの `AzureCliCredential` を使用して認証します。つまり、Azure CLI セッションが認証情報を提供するため、`.env` ファイルに API キーやシークレットを置く必要がありません。これは[セキュリティのベストプラクティス](https://learn.microsoft.com/azure/developer/ai/keyless-connections)です。

### ステップ 4：`.env` ファイルを作成する

サンプルファイルをコピー：

```bash
# zsh と bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

`.env` を開いて次の 2 つの値を入力してください：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| 変数 | 見つける場所 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry ポータル → あなたのプロジェクト → **概要** ページ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry ポータル → **Models + Endpoints** → デプロイ済みモデルの名前 |

ほとんどのレッスンはこれで準備完了です！ノートブックは `az login` セッションを通じて自動的に認証されます。

### ステップ 5：Python の依存関係をインストールする

```bash|powershell
pip install -r requirements.txt
```

これを先ほど作成した仮想環境内で実行することを推奨します。

## レッスン 5（Agentic RAG）の追加設定

レッスン 5 は検索強化生成（retrieval-augmented generation）に **Azure AI Search** を使用します。そのレッスンを実行する場合は、これらの変数を `.env` ファイルに追加してください：

| 変数 | 見つける場所 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure ポータル → あなたの **Azure AI Search** リソース → **概要** → URL |
| `AZURE_SEARCH_API_KEY` | Azure ポータル → あなたの **Azure AI Search** リソース → **設定** → **キー** → プライマリ管理キー |

## レッスン 6 とレッスン 8（GitHub Models）の追加設定

レッスン 6 および 8 の一部のノートブックは Azure AI Foundry の代わりに **GitHub Models** を使用します。これらのサンプルを実行する予定がある場合は、以下の変数を `.env` ファイルに追加してください：

| 変数 | 見つける場所 |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | 使用する URL: `https://models.inference.ai.azure.com`（デフォルト値） |
| `GITHUB_MODEL_ID` | 使用するモデル名（例: `gpt-4o-mini`） |

## レッスン 8（Bing Grounding Workflow）の追加設定

レッスン 8 の条件付きワークフローノートブックは、Azure AI Foundry 経由の **Bing grounding** を使用します。そのサンプルを実行する場合は、次の変数を `.env` ファイルに追加してください：

| 変数 | 見つける場所 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry ポータル → あなたのプロジェクト → **Management** → **Connected resources** → あなたの Bing 接続 → 接続 ID をコピー |

## トラブルシューティング

### macOS での SSL 証明書検証エラー

macOS 上で次のようなエラーが発生した場合：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

これは、macOS 上の Python でシステムの SSL 証明書が自動的に信頼されない既知の問題です。以下の解決策を順に試してください：

**オプション 1：Python の Install Certificates スクリプトを実行する（推奨）**

```bash
# 3.XX をインストール済みの Python バージョン（例: 3.12 または 3.13）に置き換えてください:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**オプション 2：ノートブックで `connection_verify=False` を使用する（GitHub Models ノートブックのみ）**

レッスン 6 のノートブック（`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`）には、コメントアウトされたワークアラウンドが既に含まれています。クライアントを作成する際に `connection_verify=False` のコメントを外してください：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 証明書エラーが発生した場合は SSL 検証を無効にしてください
)
```

> **⚠️ Warning:** SSL 検証を無効化する（`connection_verify=False`）と、証明書検証をスキップすることでセキュリティが低下します。これは開発環境での一時的な回避策としてのみ使用し、本番環境では絶対に使用しないでください。

**オプション 3：`truststore` をインストールして使用する**

```bash
pip install truststore
```

ネットワーク呼び出しを行う前に、ノートブックまたはスクリプトの先頭に次を追加してください：

```python
import truststore
truststore.inject_into_ssl()
```

## 行き詰まっていますか？

このセットアップの実行に問題がある場合は、<a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI コミュニティ Discord</a> に参加するか、<a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">Issue を作成する</a> でご連絡ください。

## 次のレッスン

これでこのコースのコードを実行する準備ができました。AI エージェントの世界についてさらに学んでいきましょう！

[AIエージェントとエージェントのユースケースの紹介](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責事項：
この文書は AI 翻訳サービス「Co‑op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の確保に努めていますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご了承ください。原文（原語の文書）が正式な参照（権威ある情報源）とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈の相違についても、当社は責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->