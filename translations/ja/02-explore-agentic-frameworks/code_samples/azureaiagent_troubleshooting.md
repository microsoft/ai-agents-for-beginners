# Azure AI Foundry Agent Service - トラブルシューティングガイド

このドキュメントでは、Azure AI Foundry Agent Service を使用する際によく発生するエラーとその解決方法について説明します。最新のAzure AI Projects SDK (v1.0.0b12+) の重要な変更点も含まれています。

## 📋 目次

1. [SDKバージョンに関する問題](#sdkバージョンに関する問題)
2. [認証関連のトラブルシューティング](#認証関連のトラブルシューティング)
3. [API変更に関する問題](#api変更に関する問題)
4. [環境設定の問題](#環境設定の問題)
5. [リソースアクセスの問題](#リソースアクセスの問題)

## 🔄 SDKバージョンに関する問題

### ⚠️ 重要：Azure AI Projects SDK v1.0.0b12 での重要な変更

最新のSDKでは以下の重要な変更があります：

#### 1. API構造の変更
```python
# ❌ 古いAPI (v1.0.0b10以前)
thread = project_client.agents.create_thread()
message = project_client.agents.create_message(...)
run = project_client.agents.create_and_process_run(...)
messages = project_client.agents.list_messages(...)

# ✅ 新しいAPI (v1.0.0b12+)
thread = project_client.agents.threads.create()
message = project_client.agents.messages.create(...)
run = project_client.agents.runs.create_and_process(...)
messages = project_client.agents.messages.list(...)
```

#### 2. ItemPagedオブジェクトの変更
```python
# ❌ 古い方法（動作しない）
messages = project_client.agents.messages.list(thread_id=thread.id)
for msg in messages.data:  # .data属性は存在しない
    print(msg.content)

# ✅ 新しい方法（推奨）
messages_paged = project_client.agents.messages.list(thread_id=thread.id)
for msg in messages_paged:  # 直接イテレーション
    print(msg.content)

# ✅ 代替方法
messages_list = list(messages_paged)  # リスト変換
```

#### 3. 環境変数の標準化
リポジトリ全体で統一された環境変数名を使用：
```bash
PROJECT_ENDPOINT=https://your-resource.services.ai.azure.com/api/projects/your-project
AZURE_AI_PROJECT_NAME=your-project-name
AZURE_SUBSCRIPTION_ID=your-subscription-id
AZURE_OPENAI_RESOURCE_GROUP=your-resource-group-name
MODEL_DEPLOYMENT_NAME=gpt-4o-mini
```

### 📦 SDKバージョンの確認と更新

**現在のバージョン確認:**
```python
import azure.ai.projects
print("Azure AI Projects SDK version:", azure.ai.projects.__version__)
```

**最新版への更新:**
```bash
pip install --upgrade azure-ai-projects azure-identity python-dotenv openai
```

## 🆔 認証関連のトラブルシューティング

### ⚠️ AIProjectClient 初期化エラー

**重要**: Azure AI Projects SDK v1.0.0b12+ では、`endpoint` と `credential` のみが必須パラメータです。

以下のエラーが発生した場合は、**SDKのバージョンが古い**可能性があります：

```
TypeError: AIProjectClient.__init__() missing 3 required positional arguments: 'subscription_id', 'resource_group_name', and 'project_name'
```

#### � 解決方法

**Step 1: SDKバージョンを確認**
```python
import azure.ai.projects
print("Azure AI Projects SDK version:", azure.ai.projects.__version__)
```

**Step 2: 最新版にアップグレード**
```bash
pip install --upgrade azure-ai-projects azure-identity python-dotenv openai
```

**Step 3: 正しい初期化コード（v1.0.0b12+対応）**
```python
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()

# ✅ 推奨: シンプル版（v1.0.0b12+で動作）
project_client = AIProjectClient(
    endpoint="https://your-resource.services.ai.azure.com/api/projects/your-project",
    credential=credential
)
```

**参考**: 詳細なSDK初期化方法は [Microsoft Learn - Azure AI Projects SDK](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme?view=azure-python-preview#key-concepts) を参照してください。

### Entra ID認証の設定

Azure AI Projects SDK v1.0.0b12では**Entra ID認証のみ**がサポートされています。

#### 必要な準備

1. **Azure CLI のインストール**
   ```bash
   # Windows (PowerShell)
   winget install Microsoft.AzureCLI
   
   # macOS
   brew install azure-cli
   
   # Linux
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
   ```

2. **Azure CLI でログイン**
   ```bash
   az login
   ```

3. **正しいサブスクリプションを設定**
   ```bash
   az account set --subscription <your-subscription-id>
   ```

### 権限設定

Azure Portal で以下を確認してください：

#### 必要なロール（RBAC）

Azure AI Projects SDK を使用するために、以下のいずれかのロールが必要です：

**🔹 開発者向けロール**
- **Cognitive Services User**: AIモデルの呼び出し（推奨）
- **Cognitive Services OpenAI User**: Azure OpenAI専用ロール
- **AI Developer**: Azure AI Foundry プロジェクト向けの包括的ロール

**🔹 管理者向けロール**
- **Cognitive Services Contributor**: モデル管理とデプロイメント
- **Cognitive Services OpenAI Contributor**: Azure OpenAI の管理機能
- **AI Administrator**: Azure AI Foundry プロジェクトの完全管理

#### Azure Portal での設定手順

**ステップ1: Azure AI Foundry プロジェクトへのアクセス**

1. **Azure Portal** ([https://portal.azure.com](https://portal.azure.com)) にアクセス
2. **「Azure AI services」** または **「Cognitive Services」** を検索
3. 対象のAzure AI Foundry プロジェクトリソースを選択
4. 左メニューから **「アクセス制御 (IAM)」** を選択

**ステップ2: ロール割り当ての追加**

1. **「追加」** → **「ロールの割り当ての追加」** をクリック
2. **「ロール」** タブで以下のいずれかを選択：
   - **Cognitive Services User** （推奨・開発用）
   - **AI Developer** （Azure AI Foundry 専用）
   - **Cognitive Services OpenAI User** （OpenAI専用）
3. **「メンバー」** タブで以下を設定：
   - **「アクセスの割り当て先」**: ユーザー、グループ、またはサービス プリンシパル
   - **「メンバー」**: 自分のアカウントまたは対象ユーザーを選択
4. **「確認と割り当て」** をクリック

**ステップ3: 権限の確認**

1. 設定後、**5分程度**で権限が反映されます
2. **「ロールの割り当て」** タブで正しく設定されているか確認

#### Azure AI Foundry ポータルでの確認

**ステップ1: プロジェクト設定の確認**

1. **Azure AI Foundry ポータル** ([https://ai.azure.com](https://ai.azure.com)) にアクセス
2. 対象のプロジェクトを選択
3. 左メニューから **「設定」** を選択
4. **「接続とキー」** タブでエンドポイントを確認・コピー

**ステップ2: モデルデプロイメントの確認**

1. **「モデル + エンドポイント」** を選択
2. **gpt-4o-mini** モデルがデプロイされているか確認
3. デプロイされていない場合は、**「デプロイの作成」** からデプロイ

**ステップ3: プロジェクトアクセス権限の確認**

1. プロジェクト設定で **「アクセス制御」** を確認
2. 自分のアカウントに適切なロールが割り当てられているか確認

#### Azure CLI を使用した権限設定（オプション）

Azure CLI を使用して権限を設定することも可能です：

```bash
# Azure にログイン
az login

# サブスクリプション設定
az account set --subscription "<your-subscription-id>"

# 自分のオブジェクトIDを取得
OBJECT_ID=$(az ad signed-in-user show --query id --output tsv)

# リソースIDを取得
RESOURCE_ID=$(az resource show -g "<resource-group>" -n "<ai-service-name>" --resource-type "Microsoft.CognitiveServices/accounts" --query id --output tsv)

# Cognitive Services User ロールを割り当て
az role assignment create --assignee-object-id $OBJECT_ID --role "Cognitive Services User" --scope $RESOURCE_ID
```

## ✅ 設定完了チェックリスト

以下の項目がすべて完了していることを確認してください：

- ☑️ Azure CLI がインストールされている
- ☑️ `az login` でログインが成功している
- ☑️ 正しいサブスクリプションが選択されている
- ☑️ Azure Portal で適切なロールが割り当てられている
- ☑️ Azure AI Foundry プロジェクトにアクセスできる
- ☑️ gpt-4o-mini モデルがデプロイされている
- ☑️ 環境変数が正しく設定されている
- ☑️ エンドポイントURLが正確である

## 🔧 診断コマンド

問題を診断するために以下のコマンドを実行してください：

### Azure CLI の状態確認
```bash
# Azure CLI バージョン確認
az --version

# ログイン状態確認
az account show

# サブスクリプション一覧
az account list --output table

# リソースグループ一覧
az group list --output table
```

### Azure AI サービスの確認
```bash
# Azure AI サービス一覧
az cognitiveservices account list --resource-group <resource-group-name> --output table

# 特定のAI サービス詳細
az cognitiveservices account show --name <service-name> --resource-group <resource-group-name>
```

### ロール割り当ての確認
```bash
# 自分に割り当てられたロール確認
az role assignment list --assignee $(az ad signed-in-user show --query id --output tsv) --output table

# リソースに対するロール割り当て確認
az role assignment list --scope <resource-id> --output table
```

## � 参考リンク

**公式ドキュメント:**
- [Azure AI Projects SDK - Microsoft Learn](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme?view=azure-python-preview)
- [Azure AI Foundry ドキュメント](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure AI Foundry Agent Service](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Azure CLI ドキュメント](https://learn.microsoft.com/cli/azure/)
- [Azure RBAC ドキュメント](https://learn.microsoft.com/azure/role-based-access-control/)

**GitHub リポジトリ:**
- [Azure SDK for Python - AI Projects](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-projects)
- [Azure AI Projects サンプル](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-projects/samples)
