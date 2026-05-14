[![良いAIエージェントの設計方法](../../../translated_images/ja/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(上の画像をクリックすると、このレッスンのビデオが表示されます)_

# ツール使用デザインパターン

ツールは、AIエージェントにより広範な能力を持たせることができるため興味深いです。エージェントが実行できるアクションが限られている代わりに、ツールを追加することで、幅広いアクションを実行できるようになります。この章では、AIエージェントが特定のツールを使用して目標を達成する方法を説明するツール使用デザインパターンについて見ていきます。

## はじめに

このレッスンでは、以下の質問に答えることを目指します：

- ツール使用デザインパターンとは何か？
- どのようなユースケースに適用できるか？
- デザインパターンを実装するために必要な要素/構成要素は何か？
- 信頼できるAIエージェントを構築するためにツール使用デザインパターンを使う際の特別な考慮事項は何か？

## 学習目標

このレッスンを終えると、以下ができるようになります：

- ツール使用デザインパターンとその目的を定義できる。
- ツール使用デザインパターンを適用できるユースケースを特定できる。
- デザインパターンを実装するために必要な主要な要素を理解できる。
- このデザインパターンを使用するAIエージェントの信頼性を確保するための考慮事項を認識できる。

## ツール使用デザインパターンとは何か？

<strong>ツール使用デザインパターン</strong>は、大規模言語モデル（LLM）が特定の目標を達成するために外部ツールと連携する能力を与えることに焦点を当てています。ツールとは、エージェントが実行可能なコードであり、アクションを行います。ツールは計算機のような単純な関数であったり、株価照会や天気予報のようなサードパーティサービスへのAPI呼び出しであったりします。AIエージェントの文脈では、ツールは<strong>モデル生成の関数呼び出し</strong>に応答してエージェントが実行するように設計されています。

## どのようなユースケースに適用できるか？

AIエージェントはツールを活用して複雑なタスクを完了したり、情報を取得したり、意思決定を行ったりできます。ツール使用デザインパターンは、データベース、ウェブサービス、コードインタープリタなどの外部システムと動的に対話するシナリオでよく利用されます。この能力は以下のさまざまなユースケースに役立ちます：

- **動的情報取得:** エージェントが外部APIやデータベースに問い合わせて最新情報を取得する（例：SQLiteデータベースのデータ分析、株価や天気情報の取得）。
- **コード実行と解釈:** エージェントがコードやスクリプトを実行して数学的問題を解いたり、レポートを生成したり、シミュレーションを行ったりする。
- **ワークフロー自動化:** タスクスケジューラ、メールサービス、データパイプラインなどのツールを統合して繰り返しや複数ステップのワークフローを自動化する。
- **カスタマーサポート:** CRMシステム、チケッティングプラットフォーム、ナレッジベースとやり取りしてユーザーの問い合わせを解決する。
- **コンテンツ生成と編集:** 文法チェッカー、テキスト要約、コンテンツ安全評価ツールなどを利用してコンテンツ作成を支援する。

## ツール使用デザインパターンの実装に必要な要素/構成要素は何か？

これらの構成要素により、AIエージェントは幅広いタスクを実行可能になります。ツール使用デザインパターンを実装するために必要な主要な要素を見てみましょう：

- **関数/ツールスキーマ**: 利用可能なツールの詳細定義（関数名、目的、必要なパラメータ、期待される出力など）。これらのスキーマによりLLMは使えるツールと有効なリクエストの構築方法を理解できる。

- <strong>関数実行ロジック</strong>: ユーザーの意図や会話文脈に基づいてツールを呼び出すタイミングと方法を管理する。プランナー、ルーティング機構、条件分岐フローなどが含まれ、ツール利用を動的に決定する。

- <strong>メッセージ処理システム</strong>: ユーザー入力、LLM応答、ツール呼び出し、ツール出力間の対話フローを管理するコンポーネント。

- <strong>ツール統合フレームワーク</strong>: 単純な関数でも複雑な外部サービスでも、エージェントが様々なツールに接続するためのインフラ。

- **エラー処理 & 検証**: ツール実行の失敗対応、パラメータ検証、予期しない応答管理の仕組み。

- <strong>状態管理</strong>: 会話文脈、過去のツールインタラクション、永続データを追跡し多ターンインタラクションでの一貫性を保つ。

次に、関数/ツール呼び出しについて詳しく見てみましょう。

### 関数/ツール呼び出し

関数呼び出しは、LLMがツールと連携できるようにする主な方法です。よく「関数」と「ツール」が同義的に使われるのは、「関数」（再利用可能なコードの単位）がエージェントがタスクを行うための「ツール」だからです。関数のコードを実行するには、LLMがユーザーのリクエストと関数説明を比較する必要があります。そのため、利用可能な関数の説明を含むスキーマがLLMに送られます。LLMはタスクに最適な関数を選択し、その名前と引数を返します。選択された関数が呼び出され、その応答がLLMに戻され、LLMはそれを使ってユーザーのリクエストに応答します。

開発者がエージェントの関数呼び出しを実装するには、以下が必要です：

1. 関数呼び出しをサポートするLLMモデル
2. 関数の説明を含むスキーマ
3. 説明された各関数のコード

例として都市の現在時刻を取得する場合を見てみましょう：

1. **関数呼び出しをサポートするLLMの初期化：**

    すべてのモデルが関数呼び出しに対応しているわけではないため、使用するLLMが対応していることを確認する必要があります。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a>は関数呼び出しをサポートしています。Azure OpenAIクライアントを初期化しましょう。

    ```python
    # Azure OpenAI クライアントを初期化する
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **関数スキーマの作成：**

    次に、関数名、関数が行う内容の説明、および関数パラメータの名前と説明を含むJSONスキーマを定義します。
    これを先に作ったクライアントに渡し、ユーザーがサンフランシスコの時刻を知りたいというリクエストを送信します。重要なのは、<strong>ツール呼び出し</strong>が返され、質問の最終回答ではないことです。先述したように、LLMはタスクのために選んだ関数名と引数を返します。

    ```python
    # モデルが読み取るための関数説明
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
  
    # 初期ユーザーメッセージ
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # 最初のAPI呼び出し：モデルに関数を使用するよう依頼する
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
  
1. **タスクを実行するための関数コード：**

    LLMが実行すべき関数を選択したので、その関数のコードを実装し実行する必要があります。
    Pythonで現在時刻を取得するコードを実装しましょう。また、response_messageから関数名と引数を抽出して最終結果を得るコードも書く必要があります。

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
  
      # 2回目のAPI呼び出し：モデルからの最終応答を取得する
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

関数呼び出しはほとんどすべてのエージェント用ツール使用設計の中心ですが、ゼロから実装するのは時に難しい場合があります。
[レッスン2](../../../02-explore-agentic-frameworks)で学んだように、エージェントフレームワークはツール使用を実装するためのビルディングブロックを既に提供しています。

## エージェントフレームワークを使ったツール使用の例

異なるエージェントフレームワークを使ってツール使用デザインパターンを実装する例をいくつか紹介します：

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a>はAIエージェント構築のためのオープンソースAIフレームワークです。`@tool`デコレーターを使ってPython関数としてツールを定義することで、関数呼び出しの処理を簡素化します。モデルとコード間の通信をフレームワークが管理します。File SearchやCode Interpreterなどの既製ツールも`AzureAIProjectAgentProvider`経由で利用可能です。

以下の図はMicrosoft Agent Frameworkでの関数呼び出しのプロセスを示しています：

![function calling](../../../translated_images/ja/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Frameworkでは、ツールはデコレートされた関数として定義されます。先ほど見た`get_current_time`関数を`@tool`デコレーターでツールに変換できます。フレームワークが関数とパラメータを自動的にシリアライズし、LLMに送信するスキーマを作成します。

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>は、開発者が基盤となる計算やストレージを管理せずに、高品質で拡張性のあるAIエージェントを安全に構築、展開、スケールできるよう設計された新しいエージェントフレームワークです。特にエンタープライズアプリケーションに有用で、エンタープライズグレードのセキュリティを備えた完全マネージドサービスです。

LLM APIを直接使用して開発する場合と比較して、Azure AI Agent Serviceには以下の利点があります：

- ツール呼び出しの自動化 — ツール呼び出しの解析や実行、レスポンス処理がサーバー側で完結
- セキュアに管理されたデータ — 独自の会話状態管理不要で、スレッドを利用してすべての情報を保存できる
- すぐ使えるツール — Bing、Azure AI Search、Azure Functionsなどのデータソースとやり取りするツール

Azure AI Agent Serviceのツールは大きく2つに分類されます：

1. 知識ツール:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing検索による情報基盤</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ファイル検索</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI検索</a>

2. アクションツール:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">関数呼び出し</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">コードインタープリタ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI定義ツール</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Serviceはこれらのツールを`toolset`として一緒に使えるようにし、特定の会話のメッセージ履歴を管理する`threads`を利用します。

例えば、Contosoという会社の営業担当者で、営業データに関する質問に答えられる会話型エージェントを開発したい場合を考えます。

以下の画像はAzure AI Agent Serviceで営業データを分析する方法を示しています：

![Agentic Service In Action](../../../translated_images/ja/agent-service-in-action.34fb465c9a84659e.webp)

これらのツールをサービスで利用するには、クライアントを作成しツールまたはツールセットを定義します。実用的に実装するために以下のPythonコードが使えます。LLMはツールセットを見て、ユーザー作成の`fetch_sales_data_using_sqlite_query`関数を使うか、事前構築済みのコードインタープリタを使うかをユーザーのリクエストに応じて決定できます。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_functions.pyファイルにあるfetch_sales_data_using_sqlite_query関数。
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ツールセットの初期化
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query関数を用いて関数呼び出しエージェントを初期化し、ツールセットに追加
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreterツールを初期化し、ツールセットに追加
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 信頼できるAIエージェントを構築するためにツール使用デザインパターンを使う際の特別な考慮事項は？

LLMが動的に生成するSQLに関して一般的な懸念はセキュリティであり、特にSQLインジェクションやデータベースの破壊や改ざんなどの悪意ある行為のリスクです。これらの懸念は妥当ですが、データベースアクセス権限を適切に設定することで効果的に軽減できます。多くのデータベースでは読み取り専用に設定することが関係します。PostgreSQLやAzure SQLのようなデータベースサービスでは、アプリに読み取り専用（SELECT）ロールを割り当てるべきです。

アプリを安全な環境で実行することも保護を強化します。企業シナリオでは、データは通常操作システムから抽出され変換され、ユーザーフレンドリーなスキーマを備えた読み取り専用のデータベースやデータウェアハウスに格納されます。この方法により、データは安全かつパフォーマンスやアクセス性の最適化がされ、アプリは制限された読み取り専用アクセスを持ちます。

## サンプルコード

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ツール使用デザインパターンについてさらに質問がありますか？

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) に参加して、他の学習者と交流し、オフィスアワーに参加してAIエージェントの質問に答えてもらいましょう。

## 追加リソース

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service ワークショップ</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer マルチエージェントワークショップ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework 概要</a>

## 前のレッスン

[エージェントデザインパターンの理解](../03-agentic-design-patterns/README.md)

## 次のレッスン
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->