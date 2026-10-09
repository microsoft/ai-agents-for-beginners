# コースセットアップ

## はじめに

このレッスンでは、このコースのコードサンプルの実行方法について説明します。

## 他の学習者に参加して助けを得る

リポジトリをクローンする前に、セットアップのサポート、コースに関する質問、または他の学習者との交流のために、[AI Agents For Beginners Discordチャンネル](https://aka.ms/ai-agents/discord)に参加してください。

## このリポジトリをクローンまたはフォークする

まず、GitHubリポジトリをクローンまたはフォークしてください。これにより、コース教材の自分のバージョンが作成され、コードを実行、テスト、調整できます！

これは<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">リポジトリをフォーク</a>するリンクをクリックして行えます。

次のリンクにあなたのフォークしたコースのバージョンができているはずです：

![フォークしたリポジトリ](../../../translated_images/ja/forked-repo.33f27ca1901baa6a.webp)

### 浅いクローン（ワークショップ / Codespacesに推奨）

  >履歴とすべてのファイルを完全にダウンロードすると、リポジトリ全体は大きくなる場合があります（約3 GB）。ワークショップへの参加のみや、一部のレッスンフォルダだけが必要な場合は、浅いクローン（またはスパースクローン）でかなり小さくダウンロードできます。

#### クイック浅いクローン — 最小限の履歴、すべてのファイル

下記のコマンドで`<your-username>`をあなたのフォークURL（またはアップストリームURL）に置き換えてください。

最新のコミット履歴のみをクローンするには：

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

特定のブランチをクローンするには：

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分的な（スパース）クローン — 最小限のblob + 選択したフォルダのみ

これは部分クローンとスパースチェックアウトを使用します（Git 2.25以上が必要で、部分クローンをサポートする最新のGitが推奨されます）：

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

リポジトリフォルダに移動：

```bash
cd ai-agents-for-beginners
```

次に、必要なフォルダを指定します（以下の例は2つのフォルダを表示）：

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

クローンしてファイル確認後、ファイルのみが必要で容量を開放したい場合（git履歴は不要）は、リポジトリのメタデータを削除してください（💀元に戻せません — Git機能はすべて失われます）：

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespacesの利用（ローカルの大きなダウンロードを避けるため推奨）

- [GitHub UI](https://github.com/codespaces)からこのリポジトリの新しいCodespaceを作成します。  

- 新しく作成したCodespaceのターミナルで、上記の浅い/スパースクローンコマンドのいずれかを実行し、必要なレッスンフォルダのみをCodespaceワークスペースに持ってきます。
- オプション：Codespaces内でクローン後に.gitを削除すると追加の容量を確保できます（削除コマンドは上記参照）。
- 注：リポジトリを直接Codespacesで開く場合（追加クローンなし）、Codespacesはdevcontainer環境を構築し、多くの場合必要以上のプロビジョニングが行われます。

#### ヒント

- 編集/コミットしたい場合は、クローンURLを必ず自分のフォークに置き換えてください。
- 後でさらに履歴やファイルが必要になった場合は、それらをフェッチするか、スパースチェックアウトで追加フォルダを含めるように調整可能です。

## コードの実行

このコースでは、AIエージェントの構築を体験できる一連のJupyterノートブックを提供しています。

コードサンプルでは、`FoundryChatClient`を使用した<strong>Microsoft Agent Framework (MAF)</strong>を用い、<strong>Microsoft Foundry</strong>を通じて<strong>Microsoft Foundry Agent Service V2</strong>（Responses API）に接続します。

すべてのPythonノートブックは`*-python-agent-framework.ipynb`というラベルが付いています。

## 要件

- Python 3.12以上
  - <strong>注意</strong>：Python3.12がインストールされていない場合は必ずインストールしてください。requirements.txtの正しいバージョンをインストールするために、python3.12で仮想環境を作成してください。
  
    >例

    Python仮想環境ディレクトリを作成：

    ```bash
    python -m venv venv
    ```

    次に仮想環境を有効化：

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10以上：.NETを使用するサンプルコードの場合、[.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)以上をインストールし、インストール済みの.NET SDKバージョンを確認してください。

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — 認証に必要。 [aka.ms/installazurecli](https://aka.ms/installazurecli)からインストールしてください。
- **Azureサブスクリプション** — Microsoft Foundry と Microsoft Foundry Agent Serviceへのアクセスのために必要です。
- **Microsoft Foundry プロジェクト** — デプロイ済みモデル (例：`gpt-5-mini`) を持つプロジェクト。以下の[ステップ1](#ステップ-1-microsoft-foundryプロジェクトを作成する)を参照してください。

このリポジトリのルートにはコードサンプルを実行するのに必要なPythonパッケージをすべて記載した`requirements.txt`ファイルがあります。

リポジトリのルートで次のコマンドを実行してインストールできます：

```bash
pip install -r requirements.txt
```

コンフリクトや問題を避けるため、Pythonの仮想環境を作成することを推奨します。

## VSCodeのセットアップ

VSCodeで正しいPythonバージョンを使用していることを確認してください。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft FoundryとMicrosoft Foundry Agent Serviceのセットアップ

### ステップ 1: Microsoft Foundryプロジェクトを作成する

ノートブックを実行するには、Microsoft Foundryの<strong>ハブ</strong>と、デプロイされたモデルを持つ<strong>プロジェクト</strong>が必要です。

1. [ai.azure.com](https://ai.azure.com) にアクセスし、Azureアカウントでサインインします。
2. <strong>ハブ</strong>を作成するか（既存のものを使用）、[ハブリソースの概要](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)をご参照ください。
3. ハブ内で<strong>プロジェクト</strong>を作成します。
4. **Models + Endpoints** → <strong>モデルをデプロイ</strong>からモデル（例：`gpt-5-mini`）をデプロイします。

### ステップ 2: プロジェクトのエンドポイントとモデルデプロイ名を取得する

Microsoft Foundryポータルのプロジェクトから：

- <strong>プロジェクトエンドポイント</strong> — **Overview** ページに行き、エンドポイントURLをコピーします。

![プロジェクト接続文字列](../../../translated_images/ja/project-endpoint.8cf04c9975bbfbf1.webp)

- <strong>モデルデプロイ名</strong> — **Models + Endpoints** に移動して、デプロイ済みモデルを選択し、**Deployment name**（例：`gpt-5-mini`）を記録します。

### ステップ 3: `az login` でAzureにサインインする

ほとんどのノートブックは `azure-identity` パッケージの `AzureCliCredential` または `DefaultAzureCredential` で Azure CLI のサインイン状態（`az login`）を使用して認証します。これによりAPIキーは不要です。一部のレッスンやオプション統合はAPIキーを使用しますので、各レッスンの前提条件で追加の環境変数を確認してください。Azure CLIへのサインインが必要です。

1. **Azure CLIが未インストールの場合はインストール**：[aka.ms/installazurecli](https://aka.ms/installazurecli)

2. 次を実行し<strong>サインイン</strong>：

    ```bash
    az login
    ```

    ブラウザがないリモート/Codespace環境の場合：

    ```bash
    az login --use-device-code
    ```

3. プロンプトが表示されたら<strong>サブスクリプションを選択</strong> — Foundryプロジェクトが含まれるものを選んでください。

4. サインイン済みを<strong>確認</strong>：

    ```bash
    az account show
    ```

> **なぜ`az login`？** ノートブックは `azure-identity` の `AzureCliCredential`（または`DefaultAzureCredential`）を使って認証します。これにより`.env` ファイルにAPIキーやシークレットが不要になり、Azure CLIセッションが資格情報を提供します。これは[セキュリティのベストプラクティス](https://learn.microsoft.com/azure/developer/ai/keyless-connections)です。

### ステップ 4: `.env` ファイルを作成する

サンプルファイルをコピー：

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

`.env` を開き、次の2つの値を記入してください：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| 変数 | 場所 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundryポータル → プロジェクト → **Overview** ページ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundryポータル → **Models + Endpoints** → デプロイ済みモデル名 |

これでほとんどのレッスンは準備完了です！ノートブックは自動的に `az login` セッションで認証します。

### ステップ 5: Python依存関係のインストール

```bash
pip install -r requirements.txt
```

先ほど作成した仮想環境内で実行することを推奨します。

## オプションセットアップ：Azure AI Search（レッスン5と16）

レッスン5（Agentic RAG）とレッスン16のノートブックは、<strong>インメモリのナレッジベース</strong>でそのまま実行可能で、追加のAzureリソースは不要です。実際の<strong>Azure AI Search</strong>インデックスでバックアップしたい場合、<strong>レッスン16ノートブックは現在キー認証を使用</strong>しており、`AZURE_SEARCH_SERVICE_ENDPOINT`と`AZURE_SEARCH_API_KEY`の両方が設定された時だけインメモリ検索からAzure AI Searchに切り替わります。そのため実際のインデックスで実行するには管理キーも設定する必要があります。本コースの他の部分で使用されている`az login`フローに準拠した推奨のキーなし認証のMicrosoft Entra ID (RBAC)は、本番コードでは推奨されます。

以下のRBAC手順はセットアップガイドサンプルと自身のコードに適用されますが、レッスン16ノートブックでキーなし認証を有効にするものではありません。レッスン16は引き続きエンドポイントと管理キーの両方を必要とします。

1. 検索サービスで<strong>ロールベースアクセスを有効</strong>にします：

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. 必要なロールを自分に<strong>割り当てる</strong>（インデックスの作成/ロードおよびクエリ）：

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. `.env` ファイルにエンドポイントを追加します：

| 変数 | 場所 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azureポータル → **Azure AI Search** リソース → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | レッスン16ノートブックでAzure AI Searchをキー認証で使用するために必要。Azureポータル → <strong>設定</strong> → <strong>キー</strong> → プライマリ管理キー |

> **なぜキーなし？** 管理キーは検索サービスに対する完全な書き込みアクセスを許可し、`.env`ファイルを通じて漏洩する恐れがあります。RBACでは代わりに `az login` のIDが使われます。これが本コースノートブックのキーなしEntra IDパターン（`AzureCliCredential` / `DefaultAzureCredential`を介す）と一致します。[ロールを使ったAzure AI Searchへの接続](https://learn.microsoft.com/azure/search/search-security-rbac)を参照してください。

[Azure AI Searchセットアップガイド](./AzureSearch.md)にPythonや.NETでの完全なインデックス作成サンプルが掲載されています。

## Azure OpenAIを直接呼び出すレッスン向け追加セットアップ（レッスン6と8）

レッスン6と8の一部ノートブックは、Microsoft Foundryプロジェクトを経由せず<strong>Azure OpenAI</strong>を直接（<strong>Responses API</strong>を使って）呼び出します。これらのサンプルは旧GitHub Modelsを使用していましたが廃止され、Responses APIをサポートしていません。`.env`に次の変数を追加してください：

| 変数 | 場所 |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azureポータル → **Azure OpenAI** リソース → <strong>キーとエンドポイント</strong> → エンドポイント (例：`https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Responses APIをサポートするデプロイ済みモデル名（例：`gpt-5-mini`） |
| `AZURE_OPENAI_API_KEY` | 任意 — `az login` / Entra ID以外のキー認証を使う場合のみ必要 |

> Responses APIは安定版の`/openai/v1/`エンドポイントを使用するため、`api-version`は不要です。キーなしのEntra ID認証には`az login`でサインインしてください。

## 代替プロバイダー：MiniMax（OpenAI互換）

[MiniMax](https://platform.minimaxi.com/)は、最大204Kトークンの長大コンテキスト対応モデルをOpenAI互換APIで提供します。Microsoft Agent Frameworkの`OpenAIChatClient`は任意のOpenAI互換エンドポイントで動作するため、`OpenAIChatClient`を使うレッスンはMiniMaxを代替としてそのまま利用可能です。

`.env` に以下の変数を追加してください：

| 変数 | 場所 |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMaxプラットフォーム](https://platform.minimaxi.com/) → APIキー |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1`（デフォルト値）を使用 |
| `MINIMAX_MODEL_ID` | 使用するモデル名（例：`MiniMax-M3`） |

<strong>モデル例</strong>：`MiniMax-M3`（推奨）、`MiniMax-M2.7`、`MiniMax-M2.7-highspeed`（高速応答）。モデル名と提供状況は時々変わることがあります。また、モデルへのアクセスはアカウントに依存します。

`OpenAIChatClient`を使用するコードサンプル（例：レッスン14のホテル予約ワークフロー）は、`MINIMAX_API_KEY`が設定されていると自動的にMiniMax設定を検出して利用します。


## 代替プロバイダー: Novita AI（OpenAI互換）

[Novita AI](https://novita.ai/llm-api) は、オープンソースおよび最先端のLLM（DeepSeek、Llama、Qwenなど）向けのOpenAI互換APIを提供しています。Microsoft Agent Frameworkの `OpenAIChatClient` はあらゆるOpenAI互換のエンドポイントで動作するため、Novita AIをAzure OpenAIやOpenAIの代替としてそのまま利用できます。

これらの変数を `.env` ファイルに追加してください：

| 変数 | 入手場所 |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI ダッシュボード](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | `https://api.novita.ai/openai/v1` を使う（デフォルト値） |
| `NOVITA_MODEL_ID` | 使用するモデル名（例：`moonshotai/kimi-k3`） |

<strong>例モデル</strong>: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`。Novita AIは他にも多くのオープンソースモデルファミリー（Llama、Qwen、GLMなど）をホストしています — 利用可能なモデルとモデルIDの一覧は[Novita AIモデルライブラリ](https://novita.ai/llm-api)で確認できます。

現状のサンプルは `NOVITA_*` 変数を自動で使用しません。Novita AIを使うには、実行中のサンプルの `OpenAIChatClient` 構築時にこれらの値を明示的に渡してください。

## 代替プロバイダー: Foundry Local（モデルをローカル実行）

[Foundry Local](https://foundrylocal.ai) は軽量なランタイムで、言語モデルを<strong>完全に自分のマシン上で</strong>ダウンロード、管理、提供し、OpenAI互換API経由で利用できます — クラウド不要です。

Microsoft Agent Frameworkの `OpenAIChatClient` はどのOpenAI互換エンドポイントとも動くため、Foundry LocalはAzure OpenAIのローカル代替としてそのまま使えます。

**1. Foundry Local をインストール**

```bash
# ウィンドウズ
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. モデルをダウンロード・実行**（これでローカルサービスも起動します）：

```bash
foundry model list          # 利用可能なモデルを見る
foundry model run phi-4-mini
```

**3. ローカルエンドポイントを発見するためのPython SDKをインストール：**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Frameworkをローカルのモデルに向ける：**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# 必要に応じてモデルをダウンロードし、ローカルで提供してから、エンドポイント/ポートを検出します。
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # 例： http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Localでは常に「not-required」です。
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **補足:** Foundry LocalはOpenAI互換の<strong>Chat Completions</strong>エンドポイントを公開しています。ローカル開発やオフライン用途に使えます。完全な<strong>Responses API</strong>機能セット（状態管理会話など）はAzure OpenAIやMicrosoft Foundryプロジェクトをご利用ください。

## レッスン8の追加セットアップ（Bing Groundingワークフロー）

レッスン8の条件付きワークフローノートブックはMicrosoft Foundry経由の<strong>Bing grounding</strong>を使っています。そのサンプルを実行する場合は、以下の変数を `.env` ファイルに追加してください：

| 変数 | 入手場所 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundryポータル → あなたのプロジェクト → <strong>管理</strong> → <strong>接続リソース</strong> → あなたのBing接続 → 接続IDをコピー |

## トラブルシューティング

### macOSでのSSL証明書検証エラー

macOS上で次のようなエラーが出る場合：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

これはmacOSのPythonでシステムSSL証明書が自動的に信頼されない既知の問題です。以下の順で解決策を試してください：

**オプション1: PythonのInstall Certificatesスクリプトを実行（推奨）**

```bash
# インストールされているPythonのバージョン（例: 3.12 または 3.13）に3.XXを置き換えてください。
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**オプション2: ノートブックで `connection_verify=False` を使う（GitHub Modelsノートブック限定）**

レッスン6のノートブック（`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`）には既にコメントアウトされた回避策が含まれています。証明書エラーがでたら `connection_verify=False` のコメントアウトを外してください：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 証明書エラーが発生した場合はSSL検証を無効にしてください
)
```

> **⚠️ 警告:** SSL検証を無効化する（`connection_verify=False`）と証明書検証をスキップするためセキュリティが低下します。これは開発環境での一時的回避策としてのみ使い、本番環境では絶対に使用しないでください。

**オプション3: `truststore` をインストールして使用**

```bash
pip install truststore
```

その後、ネットワーク呼び出しの前にノートブックやスクリプトの冒頭に以下を追加してください：

```python
import truststore
truststore.inject_into_ssl()
```

## 行き詰まった？

もしセットアップで問題があれば、<a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>に参加するか、<a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">Issueを作成</a>してください。

## 次のレッスン

これでコースのコードを実行する準備が整いました。AIエージェントの世界をさらに学んでください！ 

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->