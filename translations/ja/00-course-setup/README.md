# コース設定

## はじめに

このレッスンでは、このコースのコードサンプルの実行方法について説明します。

## 他の学習者と参加し、サポートを受ける

リポジトリのクローンを始める前に、[AI Agents For Beginners Discord チャンネル](https://aka.ms/ai-agents/discord) に参加して、セットアップの支援やコースに関する質問、または他の学習者との交流を得てください。

## このリポジトリをクローンまたはフォークする

まず、GitHubリポジトリをクローンまたはフォークしてください。これによりコース教材の自分専用のバージョンができ、コードの実行、テスト、調整が可能になります！

<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">リポジトリをフォークする</a>リンクをクリックすることで行えます。

以下のリンクに、あなた自身のフォークされたコースバージョンが表示されているはずです：

![Forked Repo](../../../translated_images/ja/forked-repo.33f27ca1901baa6a.webp)

### 浅いクローン（ワークショップ / Codespaces推奨）

  >フルのリポジトリは履歴全てとファイルの全てをダウンロードすると大きく（約3GB）なります。ワークショップ参加のみ、または特定のレッスンフォルダだけ必要な場合、浅いクローン（またはスパースクローン）により履歴を縮小したりblobをスキップして大部分のダウンロードを回避できます。

#### 速い浅いクローン — 最小履歴、すべてのファイル

以下のコマンド内の `<your-username>` は、あなたのフォークURL（またはアップストリームURL）に置き換えてください。

最新のコミット履歴のみをクローンする方法（ダウンロードが小さい）：

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

特定のブランチをクローンする方法：

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分的（スパース）クローン — 最小blob＋選択フォルダのみ

これは部分クローンとスパースチェックアウトを使用します（Git 2.25+ が必要、部分クローン対応のモダンなGit推奨）：

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

リポジトリフォルダに移動：

```bash|powershell
cd ai-agents-for-beginners
```

その後、必要なフォルダを指定します（以下は2つのフォルダの例）：

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

クローンしファイルを確認したら、ファイルだけが必要でスペースを解放したい場合（Git履歴不要の場合）、リポジトリのメタデータを削除してください（💀不可逆 — Git機能はすべて使えなくなります：コミット、プル、プッシュ、履歴閲覧不可）。

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces の使用（ローカルでの大容量ダウンロード回避推奨）

- このリポジトリで新しいCodespaceを [GitHub UI](https://github.com/codespaces) から作成します。  

- 新たに作成されたCodespaceのターミナルで、上記の浅い/スパースクローンコマンドのいずれかを実行し、必要なレッスンフォルダだけをCodespaceのワークスペースに取り込みます。
- オプション：Codespaces内でクローン後、.git を削除して追加のスペースを回収可能（前述の削除コマンド参照）。
- 注意：Codespacesでリポジトリを直接開く方法（クローン不要）もありますが、Codespacesはdevcontainer環境を構築するため、必要以上のリソースが割り当てられることがあります。新規Codespace内で浅いコピーをクローンすることでディスク使用量の制御が可能です。

#### ヒント

- 編集/コミットしたい場合は、常にクローンURLを自分のフォークに置き換えてください。
- 後で履歴やファイルがもっと必要になった場合は、それらをフェッチしたり、スパースチェックアウトでフォルダ追加が可能です。

## コードの実行

このコースでは、AIエージェント構築の実践経験を積むために実行可能な一連のJupyter Notebookを提供しています。

コードサンプルは **Microsoft Agent Framework (MAF)** と `FoundryChatClient` を使用し、**Microsoft Foundry Agent Service V2**（Responses API）に<strong>Microsoft Foundry</strong>経由で接続します。

すべてのPythonノートブックは `*-python-agent-framework.ipynb` と名付けられています。

## 必要条件

- Python 3.12以上
  - <strong>注意</strong>: Python3.12がインストールされていない場合は必ずインストールしてください。その後、python3.12を使いvenvを作成し、requirements.txtから正しいバージョンをインストールするようにしてください。
  
    >例

    Python venvディレクトリを作成：

    ```bash|powershell
    python -m venv venv
    ```

    次にvenv環境を以下でアクティベート：

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10以上：.NETを使用するサンプルコードには [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 以上をインストールしてください。その後インストール済みの.NET SDKバージョンを確認します：

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — 認証に必要です。[aka.ms/installazurecli](https://aka.ms/installazurecli)からインストールしてください。
- **Azureサブスクリプション** — Microsoft FoundryとMicrosoft Foundry Agent Serviceへのアクセスに必要です。
- **Microsoft Foundryプロジェクト** — モデルをデプロイしたプロジェクト（例: `gpt-5-mini`）が必要です。以下の[ステップ1](#ステップ-1-microsoft-foundry-プロジェクトを作成する)を参照してください。

このリポジトリのルートに、必要なPythonパッケージをすべて含む `requirements.txt` ファイルが含まれています。

リポジトリのルートで次のコマンドを実行してインストールできます：

```bash|powershell
pip install -r requirements.txt
```

競合や問題を避けるために、Pythonの仮想環境を作成することを推奨します。

## VSCode のセットアップ

VSCodeで正しいPythonバージョンを使用しているか確認してください。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry と Microsoft Foundry Agent Service のセットアップ

### ステップ 1: Microsoft Foundry プロジェクトを作成する

ノートブックを実行するには、Microsoft Foundry の **hub** とデプロイ済みモデルを含む **project** が必要です。

1. [ai.azure.com](https://ai.azure.com) にアクセスして、Azureアカウントでサインインします。
2. **hub** を作成（または既存のものを使用）。詳細は：[Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources) を参照。
3. hub内で **project** を作成します。
4. **Models + Endpoints** → **Deploy model** からモデル（例：`gpt-5-mini`）をデプロイします。

### ステップ 2: プロジェクトのエンドポイントとモデルデプロイ名を取得する

Microsoft Foundry ポータルのプロジェクトから：

- **Project Endpoint** — <strong>Overview</strong>ページに行き、エンドポイントURLをコピーします。

![Project Connection String](../../../translated_images/ja/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** に進み、デプロイ済みモデルを選択し、**Deployment name**（例：`gpt-5-mini`）をメモします。

### ステップ 3: `az login` で Azure にサインインする

すべてのノートブックは認証に **`AzureCliCredential`** を使用します — APIキーは不要です。このためAzure CLIでサインインしている必要があります。

1. **Azure CLIをインストール**（まだであれば）：[aka.ms/installazurecli](https://aka.ms/installazurecli)

2. <strong>サインイン</strong>を実行：

    ```bash|powershell
    az login
    ```

    ブラウザがないリモート/Codespace環境の場合：

    ```bash|powershell
    az login --use-device-code
    ```

3. プロンプトがあれば<strong>サブスクリプションを選択</strong> — Foundryプロジェクトがあるものを選びます。

4. <strong>サインイン確認</strong>：

    ```bash|powershell
    az account show
    ```

> **なぜ `az login` を使うのか？** ノートブックは `azure-identity` パッケージの `AzureCliCredential` で認証します。これはAzure CLIセッションが認証情報を提供し、`.env` にAPIキーやシークレットを含める必要がないためで、[セキュリティベストプラクティス](https://learn.microsoft.com/azure/developer/ai/keyless-connections)でもあります。

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

`.env` を開いて以下の2つの値を入力します：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| 変数名 | 取得場所 |
|--------|----------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundryポータル → あなたのプロジェクト → <strong>Overview</strong>ページ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundryポータル → **Models + Endpoints** → デプロイ済みモデル名 |

これでほとんどのレッスンは準備完了です！ノートブックは `az login` セッションから自動的に認証されます。

### ステップ 5: Python依存関係をインストールする

```bash|powershell
pip install -r requirements.txt
```

先に作成した仮想環境内で実行することを推奨します。

## レッスン5（Agentic RAG）の追加セットアップ

レッスン5は **Azure AI Search** を用いたリトリーバル強化生成を使います。このレッスンを実行する場合は以下の変数を `.env` に追加してください：

| 変数名 | 取得場所 |
|--------|----------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azureポータル → あなたの **Azure AI Search** リソース → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azureポータル → あなたの **Azure AI Search** リソース → <strong>設定</strong> → <strong>キー</strong> → プライマリアドミンキー |

## Azure OpenAI に直接呼び出すレッスン（6と8）の追加セットアップ

レッスン6と8の一部ノートブックはMicrosoft Foundryを経由せず、**Azure OpenAI**（**Responses API**）を直接呼び出します。これらは以前GitHub Modelsを使っていましたが、それは非推奨（2026年7月に廃止予定）でResponses APIをサポートしていません。このサンプルを動かす場合は以下の変数を `.env` に追加してください：

| 変数名 | 取得場所 |
|--------|----------|
| `AZURE_OPENAI_ENDPOINT` | Azureポータル → あなたの **Azure OpenAI** リソース → **Keys and Endpoint** → エンドポイント (例: `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Responses API対応モデルの名前（例：`gpt-5-mini`） |
| `AZURE_OPENAI_API_KEY` | オプション — `az login` / Entra ID以外のキー認証を使う場合のみ |

> Responses APIは安定版の `/openai/v1/` エンドポイントを使用し、`api-version`は不要です。`az login` でサインインし、キー不要のEntra ID認証を利用してください。

## 代替プロバイダー: MiniMax (OpenAI互換)

[MiniMax](https://platform.minimaxi.com/) は大規模コンテキストモデル（最大204Kトークン）をOpenAI互換APIで提供します。Microsoft Agent Frameworkの `OpenAIChatClient` は任意のOpenAI互換エンドポイントで動作するため、MiniMaxはAzure OpenAIやOpenAIの代替として使えます。

以下の変数を `.env` に追加してください：

| 変数名 | 取得場所 |
|--------|----------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → APIキー |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` を使用（デフォルト値） |
| `MINIMAX_MODEL_ID` | 使用するモデル名（例：`MiniMax-M3`） |

<strong>モデル例</strong>：`MiniMax-M3`（推奨）、`MiniMax-M2.7`、`MiniMax-M2.7-highspeed`（高速応答）。モデル名や利用可能性は変動し、アカウントや地域によってアクセス制限がある場合があります。最新情報は [MiniMax Platform](https://platform.minimaxi.com/) をご確認ください。`MiniMax-M3` にアクセスできない場合は、アクセスできるモデル（例：`MiniMax-M2.7`）を設定してください。

`OpenAIChatClient` を使用するコードサンプル（例：レッスン14ホテル予約ワークフロー）は、`MINIMAX_API_KEY` が設定されていると自動的にMiniMax設定を検出し使用します。

## 代替プロバイダー: Foundry Local (モデルをオンデバイスで実行)

[Foundry Local](https://foundrylocal.ai) は言語モデルを完全に自身のマシン上でダウンロード、管理、提供する軽量ランタイムで、OpenAI互換APIを通じて動作します。クラウド不要、Azureサブスクリプション不要、APIキーも不要です。オフライン開発、クラウドコストを抑えた実験や、データのオンデバイス保持に最適です。

Microsoft Agent Frameworkの `OpenAIChatClient` は任意のOpenAI互換エンドポイントで動作するため、Foundry Local はAzure OpenAIのローカル代替としてそのまま使えます。

**1. Foundry Localをインストール**

```bash
# ウィンドウズ
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. モデルをダウンロードして実行**（ローカルサービスも起動されます）：

```bash
foundry model list          # 利用可能なモデルを参照してください
foundry model run phi-4-mini
```

**3. ローカルエンドポイントを検出するPython SDKをインストール**：

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework にローカルモデルを指定する：**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# 必要に応じてモデルをダウンロードしローカルで提供し、その後エンドポイント/ポートを検出します。
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # 例: http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Localでは常に「not-required」です。
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **注意:** Foundry Local はOpenAI互換の **Chat Completions** エンドポイントを提供します。ローカル開発やオフライン利用に適しています。ステートフル会話や深いツールオーケストレーション、エージェント型開発に必要な完全な **Responses API** 機能セットは、Azure OpenAI または Microsoft Foundry プロジェクトを使用してください。最新モデルカタログやプラットフォーム対応は [Foundry Localドキュメント](https://foundrylocal.ai) を参照。

## レッスン8（Bing Grounding Workflow）の追加セットアップ


レッスン8の条件付きワークフローノートブックは、Microsoft Foundry経由の<strong>Bingグラウンディング</strong>を使用しています。このサンプルを実行する予定がある場合は、この変数を`.env`ファイルに追加してください：

| 変数 | 場所 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundryポータル → あなたのプロジェクト → <strong>管理</strong> → <strong>接続済みリソース</strong> → あなたのBing接続 → 接続IDをコピー |

## トラブルシューティング

### macOSでのSSL証明書検証エラー

macOSで以下のようなエラーが発生する場合：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

これはmacOSのPythonの既知の問題で、システムのSSL証明書が自動的に信頼されないためです。以下の解決策を順に試してください：

**オプション1: Pythonの証明書インストールスクリプトを実行する（推奨）**

```bash
# インストールされているPythonのバージョン（例：3.12または3.13）に3.XXを置き換えてください:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**オプション2: ノートブックで `connection_verify=False` を使用する（GitHub Modelsノートブック専用）**

レッスン6ノートブック（`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`）にはコメントアウトされた回避策が既に含まれています。クライアント作成時に`connection_verify=False`のコメントアウトを外してください：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 証明書エラーが発生した場合はSSL検証を無効にしてください
)
```

> **⚠️ 警告:** SSL検証を無効にすること（`connection_verify=False`）は証明書検証をスキップするためセキュリティが低下します。これは開発環境での一時的な回避策としてのみ使用し、本番環境では決して使用しないでください。

**オプション3: `truststore`をインストールして使用する**

```bash
pip install truststore
```

その後、ネットワークコールを行う前にノートブックやスクリプトの先頭に以下を追加してください：

```python
import truststore
truststore.inject_into_ssl()
```

## 行き詰まったら？

このセットアップの実行に問題がある場合は、<a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>に参加するか、<a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">Issueを作成</a>してください。

## 次のレッスン

このコースのコードを実行する準備が整いました。AIエージェントの世界についてさらに学んでいきましょう！

[AIエージェントとエージェントのユースケースの紹介](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
