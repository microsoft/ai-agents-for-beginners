[![良いAIエージェントの設計方法](../../../translated_images/ja/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(上の画像をクリックすると、このレッスンのビデオが表示されます)_

# ツール使用デザインパターン

ツールは興味深いもので、AIエージェントにより広範な能力を持たせることができます。エージェントが実行できる操作が制限される代わりに、ツールを追加することで、エージェントは幅広い操作を実行できるようになります。この章では、AIエージェントが特定のツールを使って目標を達成する方法を説明する「ツール使用デザインパターン」を見ていきます。

## はじめに

このレッスンでは、以下の質問に答えたいと思います：

- ツール使用デザインパターンとは何か？
- どのようなユースケースに適用できるか？
- デザインパターンを実装するために必要な要素／構成要素は何か？
- 信頼できるAIエージェントを構築するために、ツール使用デザインパターンを使用する際の特別な考慮事項は何か？

## 学習目標

このレッスンを修了すると、次のことができるようになります：

- ツール使用デザインパターンとその目的を定義できる。
- ツール使用デザインパターンが適用できるユースケースを識別できる。
- デザインパターンを実装するために必要な主要な要素を理解できる。
- このデザインパターンを使うAIエージェントにおける信頼性を確保するための考慮点を認識できる。

## ツール使用デザインパターンとは？

**ツール使用デザインパターン**は、LLMに外部ツールと連携する能力を与え、特定の目標を達成することに焦点を当てています。ツールとは、エージェントが実行可能なコードのことです。ツールは計算機のような単純な関数であったり、株価照会や天気予報などのサードパーティサービスへのAPI呼び出しであったりします。AIエージェントの文脈では、ツールは**モデル生成の関数呼び出し**に応答してエージェントが実行するよう設計されています。

## どのようなユースケースに適用できるのか？

AIエージェントはツールを活用して複雑なタスクを完遂したり、情報を取得したり、意思決定を行ったりできます。ツール使用デザインパターンは、データベースやウェブサービス、コードインタプリタのような外部システムと動的に連携する必要がある場面でよく使われます。この能力は以下などの様々なユースケースで有用です：

- **動的情報取得：** エージェントは外部APIやデータベースを問合せて最新データを取得できる（例：SQLiteデータベースの問合せによるデータ分析、株価や天気情報の取得）。
- **コード実行および解釈：** エージェントはコードやスクリプトを実行して数学的問題を解決したり、レポートを生成したり、シミュレーションを実行したりできる。
- **ワークフロー自動化：** タスクスケジューラやメールサービス、データパイプラインなどのツールを統合して、反復処理や複数ステップのワークフローを自動化する。
- **カスタマーサポート：** エージェントはCRMシステムやチケッティングプラットフォーム、ナレッジベースと連携してユーザーの問い合わせを解決する。
- **コンテンツ生成および編集：** エージェントは文法チェッカー、テキスト要約、コンテンツ安全評価ツールなどを活用してコンテンツ作成作業を支援する。

## ツール使用デザインパターンを実装するために必要な要素／構成要素は何か？

これらの構成要素によってAIエージェントは幅広いタスクを実行できます。ツール使用デザインパターンを実装するための主要な要素を見てみましょう：

- **関数／ツールスキーマ**：利用可能なツールの詳細な定義です。関数名、目的、必要なパラメーター、出力結果などを含みます。これらのスキーマにより、LLMはどのツールが利用可能で有効なリクエストをどのように構築すべきかわかります。

- **関数実行ロジック**：ユーザーの意図や会話のコンテキストに基づき、ツールがいつどのように呼び出されるかを管理します。プランナーやルーティング機構、条件分岐により動的にツール利用を決定する場合があります。

- **メッセージ処理システム**：ユーザー入力、LLM応答、ツール呼び出しおよびツール出力間の会話の流れを管理するコンポーネントです。

- **ツール統合フレームワーク**：単純な関数でも複雑な外部サービスでも、エージェントと各種ツールを接続するためのインフラです。

- **エラー処理および検証**：ツール実行の失敗時の対応、パラメーターの検証、予期しない応答の管理を行います。

- **状態管理**：会話のコンテキスト、過去のツールインタラクション、永続データを追跡し、マルチターンのやりとりにおける一貫性を保証します。

次に、関数／ツール呼び出しの詳細を見ていきましょう。
 
### 関数／ツール呼び出し

関数呼び出しは、LLMがツールと連携するための主要な手段です。『関数』と『ツール』はしばしば同じ意味で使われます。なぜなら、『関数』（再利用可能なコードのブロック）が、エージェントがタスクを実行するために使う『ツール』だからです。関数のコードを呼び出すには、LLMがユーザーのリクエストを関数の説明と比較する必要があります。そのため、利用可能な関数すべての説明を含むスキーマがLLMに送られます。LLMはタスクに最も適した関数を選択し、その名前と引数を返します。選択された関数が呼び出され、その応答がLLMに戻され、ユーザーのリクエストに応答するために使われます。

開発者がエージェントの関数呼び出しを実装するには、以下が必要です：

1. 関数呼び出しをサポートするLLMモデル
2. 関数説明を含むスキーマ
3. 各関数の実装コード

都市の現在の時間を取得する例で説明しましょう：

1. **関数呼び出しをサポートするLLMを初期化する：**

    全てのモデルが関数呼び出しをサポートしているわけではないので、使用するLLMが対応しているか確認することが重要です。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a>は関数呼び出しをサポートしています。まずAzure OpenAIクライアントを起動しましょう。

    ```python
    # Azure OpenAI クライアントを初期化する
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **関数スキーマを作成する：**

    次に、関数名、関数の説明、関数パラメーターの名前と説明を含むJSONスキーマを定義します。  
    そしてこのスキーマを先ほど作成したクライアントに渡し、ユーザーの「サンフランシスコの時間を教えて」というリクエストも一緒に渡します。重要なのは、**ツール呼び出し**が返るということで、質問の最終回答ではありません。前述のように、LLMはタスクに選んだ関数名とその引数を返します。

    ```python
    # モデルが読むための関数の説明
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # 初回ユーザーメッセージ
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # 最初のAPI呼び出し：モデルに関数を使用するよう依頼
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # モデルの応答を処理する
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **タスクを実行するために必要な関数コード：**

    LLMが実行すべき関数を選択したので、その関数を実装し実行する必要があります。  
    Pythonで現在の時間を取得するコードを実装しましょう。さらに、レスポンスメッセージから関数名と引数を取り出して最終結果を得るコードも書く必要があります。

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # 関数呼び出しを処理する
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # 2回目のAPI呼び出し: モデルから最終応答を取得する
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

関数呼び出しはほとんど、場合によってはすべてのエージェントツール使用デザインの核となるもので、しかしゼロから実装するのは時に難しい場合があります。  
[レッスン2](../../../02-explore-agentic-frameworks)で学んだように、エージェントフレームワークはツール使用を実装するためのビルディングブロックを提供してくれます。
 
## エージェントフレームワークを用いたツール使用の例

ツール使用デザインパターンを異なるエージェントフレームワークで実装する例をいくつか紹介します：

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a>はAIエージェント構築のためのオープンソースAIフレームワークです。`@tool`デコレーターを使ってPythonの関数としてツールを定義し、関数呼び出しのプロセスを簡素化します。フレームワークはモデルとコード間の往復通信を処理し、`AzureAIProjectAgentProvider`を通じてファイル検索やコードインタプリタなどの事前構築ツールも提供します。

以下の図は、Microsoft Agent Frameworkによる関数呼び出しの流れを示しています：

![function calling](../../../translated_images/ja/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Frameworkではツールはデコレートされた関数として定義されます。先ほど見た`get_current_time`関数を`@tool`デコレーターを使ってツールに変換できます。フレームワークが自動で関数とパラメーターをシリアライズし、LLMに送るスキーマを作成します。

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# クライアントを作成する
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# エージェントを作成し、ツールで実行する
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>は比較的新しいエージェントフレームワークで、開発者が基盤となるコンピューティングやストレージリソースを管理せずに、高品質で拡張可能なAIエージェントを安全に構築、展開、スケールできることを目指しています。特にエンタープライズ用途に適しており、完全管理サービスで企業レベルのセキュリティを提供します。

直接LLM APIで開発する場合と比べ、Azure AI Agent Serviceは次の利点があります：

- ツール呼び出しの自動化 − ツール呼び出しの解析、呼び出し、応答の処理をサーバー側で自動的に行う
- 安全に管理されたデータ − 独自の会話状態管理をせずとも、スレッドに必要な情報をすべて保存可能
- すぐに使えるツール − Bing、Azure AI Search、Azure Functionsなどのデータソースと連携できるツールを利用可能

Azure AI Agent Serviceで利用できるツールは大きく2つのカテゴリに分けられます：

1. ナレッジツール:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing検索によるグラウンディング</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ファイル検索</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. アクションツール:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">関数呼び出し</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">コードインタプリタ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI定義ツール</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

このエージェントサービスは、これらのツールを「ツールセット」としてまとめて使うことを可能にします。また、特定会話のメッセージ履歴を保持する「スレッド」も利用します。

例えば、Contosoという会社で営業担当として働いているとします。営業データに関する質問に応答する会話型エージェントを開発したいと考えています。

以下の画像はAzure AI Agent Serviceを使って営業データ分析を実施する様子を示しています：

![Agentic Service In Action](../../../translated_images/ja/agent-service-in-action.34fb465c9a84659e.webp)

これらのツールをサービスで使うには、クライアントを作成し、ツールまたはツールセットを定義します。これは次のPythonコードで実装可能です。LLMはツールセットを見て、ユーザー作成関数`fetch_sales_data_using_sqlite_query`か事前構築のコードインタプリタを使うかをユーザーリクエストに応じて判断します。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_functions.py ファイルにある fetch_sales_data_using_sqlite_query 関数。
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ツールセットを初期化する
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query 関数を使って関数呼び出しエージェントを初期化し、ツールセットに追加する
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# コードインタプリターツールを初期化し、ツールセットに追加する。
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 信頼できるAIエージェントを構築するためにツール使用デザインパターンを使う際の特別な考慮事項は？

LLMによって動的に生成されるSQLに関してよくある懸念はセキュリティです。特にSQLインジェクションやデータベースの削除・改ざんなどの悪意ある行為のリスクがあります。これらの懸念は正しくデータベースのアクセス権限を設定することで効果的に軽減できます。多くのデータベースでは読み取り専用（Read-Only）に設定することが多いです。PostgreSQLやAzure SQLのようなデータベースサービスの場合、アプリには読み取り専用（SELECT）ロールを割り当てるべきです。

アプリケーションを安全な環境で実行することも保護を強化します。エンタープライズシナリオでは、運用システムからデータを抽出・変換して読み取り専用のデータベースやデータウェアハウスに格納し、ユーザーフレンドリーなスキーマを適用します。この方法により、データは安全に保護され、パフォーマンスやアクセシビリティに最適化され、アプリは制限された読み取り専用アクセス権のみ持つことになります。

## サンプルコード

- Python：[Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET：[Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ツール使用デザインパターンについてもっと知りたい？

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)に参加して、他の学習者と交流したり、オフィスアワーに参加してAIエージェントに関する質問を解決しましょう。

## 追加リソース

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service ワークショップ</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer マルチエージェントワークショップ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework 概要</a>

## 前のレッスン

[Agentic Design Patternsの理解](../03-agentic-design-patterns/README.md)

## 次のレッスン
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があることをご承知おきください。原文はあくまで正式な情報源とみなしてください。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の使用により生じた誤解や誤訳について、一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->