# コース設定

## はじめに

このレッスンでは、本コースのコードサンプルの実行方法を説明します。

## 他の学習者に参加してヘルプを得る

リポジトリをクローンする前に、セットアップのサポートやコースに関する質問、他の学習者との交流のために[AI Agents For Beginners Discord チャンネル](https://aka.ms/ai-agents/discord)に参加してください。

## このリポジトリをクローンまたはフォークする

開始するには、GitHub リポジトリをクローンまたはフォークしてください。これにより、コードを実行、テスト、調整できる自分専用のコース教材のバージョンが作成されます！

これは、<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">リポジトリをフォークする</a>ためのリンクをクリックすることで実行できます。

以下のリンクから、このコースのフォーク版を入手できます。

![フォークしたリポジトリ](../../../translated_images/ja/forked-repo.33f27ca1901baa6a.webp)

### 浅いクローン（ワークショップ / Codespaces に推奨）

  > リポジトリ全体は、履歴やすべてのファイルを完全にダウンロードすると大きくなることがあります（約3 GB）。ワークショップに参加するだけ、またはいくつかのレッスンフォルダだけが必要な場合、浅いクローン（またはスパースクローン）は履歴を切り詰めたり、blob をスキップすることでその大部分のダウンロードを回避します。

#### クイック浅いクローン — 最小の履歴、すべてのファイル

以下のコマンドの`<your-username>`を、フォークのURL（または必要に応じてアップストリームのURL）に置き換えてください。

最新のコミット履歴のみをクローンするには（ダウンロードサイズは小さいです）：

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

特定のブランチをクローンするには：

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分（スパース）クローン — 最小の blob + 選択したフォルダのみ

これは部分クローンとスパースチェックアウトを使用します（Git 2.25以降が必要で、部分クローンをサポートする最新のGitを推奨します）。

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

リポジトリフォルダに移動します。

```bash|powershell
cd ai-agents-for-beginners
```

次に、必要なフォルダを指定します（以下の例では2つのフォルダを示しています）。

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

ファイルのクローンと検証後、ファイルのみが必要で空き容量を確保したい場合（Git の履歴は不要）、リポジトリのメタデータを削除してください（💀元に戻せません。コミット、プル、プッシュ、履歴へのアクセスなど、すべての Git 機能が失われます）。

```bash
# zsh または bash
rm -rf .git
```

```powershell
# パワーシェル
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces の使用（ローカルでの大きなダウンロードを回避するために推奨）

- [GitHub の UI](https://github.com/codespaces)を使って、このリポジトリ用の新しいCodespaceを作成してください。 
- 新しく作成したコードスペースのターミナルで、上記のシャロークローン/スパースクローンコマンドのいずれかを実行し、必要なレッスンフォルダのみをコードスペースワークスペースにコピーします。
- オプション：コードスペース内でクローンした後、.git を削除して余分なディスク容量を解放します（上記の削除コマンドを参照）。
- 注意：リポジトリをコードスペース内で直接開く場合（追加のクローンを行わない場合）、コードスペースは開発コンテナ環境を構築し、必要以上のリソースをプロビジョニングする可能性があることに注意してください。新しいコードスペース内にシャローコピーをクローンすることで、ディスク使用量をより細かく制御できます。

#### ヒント

- 編集やコミットを行う場合は、必ずクローンURLをフォークしたURLに置き換えてください。
- 後でさらに履歴やファイルが必要になった場合は、それらを取得するか、sparse-checkoutの設定を調整して追加のフォルダを含めることができます。

## コードの実行

このコースでは、AIエージェントの構築を実践的に体験できる一連のJupyter Notebookを提供します。

コードサンプルでは、​​**Microsoft Agent Framework (MAF)**と`AzureAIProjectAgentProvider`を使用し、**Microsoft Foundry**を介して**Azure AI Agent Service V2**（Responses API）に接続します。

すべてのPythonノートブックは`*-python-agent-framework.ipynb`という名前です。

## 要件

- Python 3.12+
  - **注意**: Python 3.12 をインストールしていない場合は、インストールしてください。次に、requirements.txt に記載された正しいバージョンがインストールされるように python3.12 を使って仮想環境を作成してください。
  
    > 例

    Pythonのvenvディレクトリを作成します。

    ```bash|powershell
    python -m venv venv
    ```

    次に、venv環境をアクティブ化します。

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- NET 10 以降: .NET を使用するサンプル コードについては、[.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 以降がインストールされていることを確認してください。次に、インストールされている .NET SDK のバージョンを確認してください。

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — 認証に必要です。インストールは [aka.ms/installazurecli](https://aka.ms/installazurecli) から行ってください。
- **Azure Subscription** — Microsoft Foundry と Azure AI Agent Service へのアクセスに必要です。
- **Microsoft Foundry Project** — デプロイされたモデル（例: `gpt-4o`）を持つプロジェクト。以下の [Step 1](../../../00-course-setup) を参照してください。

このリポジトリのルートディレクトリに、コードサンプルを実行するために必要なすべてのPythonパッケージを記述した`requirements.txt`ファイルを用意しました。

リポジトリのルートディレクトリでターミナルを開き、以下のコマンドを実行することで、これらのパッケージをインストールできます。

```bash|powershell
pip install -r requirements.txt
```

競合や問題を回避するため、Pythonの仮想環境を作成することをお勧めします。

## VSCode のセットアップ

VS Codeで正しいバージョンのPythonを使用していることを確認してください。

![画像](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry と Azure AI Agent Service の設定

### ステップ 1: Microsoft Foundry プロジェクトを作成する

ノートブックを実行するには、デプロイされたモデルを持つ Azure AI Foundry のハブとプロジェクトが必要です。

1. [ai.azure.com](https://ai.azure.com) に移動し、Azure アカウントでサインインします。
2. ハブを作成する（または既存のものを使用）。参照: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)。
3. ハブ内でプロジェクトを作成します。
4. **Models + Endpoints** → **Deploy model** からモデル（例: `gpt-4o`）をデプロイします。

### ステップ 2: プロジェクトのエンドポイントとモデルデプロイ名を取得する

Microsoft Foundry ポータルのプロジェクトから:

- **Project Endpoint** — **Overview** ページに移動してエンドポイントの URL をコピーします。

![プロジェクト接続文字列](../../../translated_images/ja/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** に移動し、デプロイしたモデルを選択して **Deployment name**（例: `gpt-4o`）を確認します。

### ステップ 3: `az login` で Azure にサインインする

すべてのノートブックは認証に**`AzureCliCredential`**を使用するため、APIキーを管理する必要はありません。これにはAzure CLI経由でサインインする必要があります。

1. **Azure CLI をインストール** していない場合はインストールしてください: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **サインイン** は以下を実行します:

    ```bash|powershell
    az login
    ```

    Or if you're in a remote/Codespace environment without a browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **サブスクリプションを選択**（プロンプトが表示された場合）— Foundry プロジェクトを含むサブスクリプションを選択してください。

4. **サインインされていることを確認**:

    ```bash|powershell
    az account show
    ```

> **なぜ `az login` なのか？** ノートブックは `azure-identity` パッケージの `AzureCliCredential` を使用して認証します。つまり、Azure CLI セッションが認証情報を提供するため、`.env` ファイルに API キーやシークレットを置く必要がありません。これは [セキュリティ上のベストプラクティス](https://learn.microsoft.com/azure/developer/ai/keyless-connections) です。

### ステップ 4: `.env` ファイルを作成する

Copy the example file:

```bash
# zsh と bash
cp .env.example .env
```

```powershell
# PowerShell（パワーシェル）
Copy-Item .env.example .env
```

`.env`ファイルを開き、以下の2つの値を入力してください。

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| 変数 | 参照先 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry ポータル → あなたのプロジェクト → **Overview** ページ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry ポータル → **Models + Endpoints** → デプロイしたモデルの名前 |

ほとんどのレッスンはこれで完了です！ノートブックは `az login` セッションを通じて自動的に認証されます。

### ステップ 5: Python 依存関係のインストール

```bash|powershell
pip install -r requirements.txt
```

仮想環境内でこれを実行することをお勧めします。

## レッスン5（エージェント型RAG）の追加セットアップ

Lesson 5 uses **Azure AI Search** for retrieval-augmented generation. If you plan to run that lesson, add these variables to your `.env` file:

| 変数 | 参照先 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure ポータル → あなたの **Azure AI Search** リソース → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure ポータル → あなたの **Azure AI Search** リソース → **Settings** → **Keys** → プライマリ管理キー |

## レッスン6 と レッスン8（GitHub Models）の追加セットアップ

一部のノートブック（レッスン6と8）は Azure AI Foundry の代わりに **GitHub Models** を使用します。これらのサンプルを実行する場合は、以下の変数を `.env` ファイルに追加してください:

| 変数 | 参照先 |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | 使用する: `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | 使用するモデル名（例: `gpt-4o-mini`） |

## レッスン8（Bing Grounding ワークフロー）の追加セットアップ

レッスン8 の条件付きワークフローノートブックは、Azure AI Foundry 経由で **Bing grounding** を使用します。このサンプルを実行する場合は、次の変数を `.env` ファイルに追加してください:

| 変数 | 参照先 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry ポータル → あなたのプロジェクト → **Management** → **Connected resources** → あなたの Bing 接続 → 接続 ID をコピー |

## トラブルシューティング

### macOS での SSL 証明書検証エラー

macOS を使用していて次のようなエラーが発生した場合:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

これは、macOS 上の Python でシステムの SSL 証明書が自動的に信頼されない既知の問題です。以下の解決策を順に試してください:

**オプション 1: Python の Install Certificates スクリプトを実行する（推奨）**

```bash
# インストールされている Python バージョン（例: 3.12 または 3.13）に合わせて 3.XX を置き換えてください:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**オプション 2: ノートブックで `connection_verify=False` を使用する（GitHub Models ノートブックのみ）**

Lesson 6 のノートブック（`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`）には、コメントアウトされた回避策が既に含まれています。クライアントを作成するときに `connection_verify=False` のコメントを外してください:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 証明書エラーが発生した場合は、SSL検証を無効にしてください
)
```

> **⚠️ 警告:** SSL 検証を無効にする（`connection_verify=False`）と、証明書検証をスキップするためセキュリティが低下します。これは開発環境での一時的な回避策としてのみ使用し、本番では絶対に使用しないでください。

**オプション 3: `truststore` をインストールして使用する**

```bash
pip install truststore
```

次に、ネットワーク呼び出しを行う前にノートブックやスクリプトの先頭に以下を追加します:

```python
import truststore
truststore.inject_into_ssl()
```

## 困ったときは？

このセットアップの実行中に問題が発生した場合は、<a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI コミュニティ Discord</a> に参加するか、<a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">問題を作成</a>してください。

## 次のレッスン

これで、このコースのコードを実行する準備が整いました。AIエージェントの世界について、楽しく学びましょう！

[AI エージェントの紹介とユースケース](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責事項:
この文書は AI 翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。原文（原言語で作成された文書）が正式な情報源とみなされます。重要な内容については、専門の翻訳者による人間翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈の相違についても責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
