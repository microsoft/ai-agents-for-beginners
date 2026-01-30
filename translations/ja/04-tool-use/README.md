[![良いAIエージェントの設計方法](../../../translated_images/ja/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(上の画像をクリックすると、このレッスンのビデオが表示されます)_

# ツール使用デザインパターン

ツールは、AIエージェントにより広範な能力を持たせることができるため興味深いものです。エージェントが実行できるアクションが限定されている代わりに、ツールを追加することで、エージェントはいろいろな種類のアクションを実行できるようになります。この章では、AIエージェントが目標を達成するために特定のツールを使用する方法を説明する、ツール使用デザインパターンについて見ていきます。

## はじめに

このレッスンでは、次の質問に答えることを目指します：

- ツール使用デザインパターンとは何か？
- どのようなユースケースに適用可能か？
- デザインパターンを実装するために必要な要素／構成要素は何か？
- 信頼できるAIエージェントを構築するためにツール使用デザインパターンを使う際に考慮すべき特別な点は何か？

## 学習目標

このレッスンを終えた後、次のことができるようになります：

- ツール使用デザインパターンとその目的を定義できる。
- ツール使用デザインパターンを適用するユースケースを特定できる。
- デザインパターンの実装に必要な主要な要素を理解できる。
- このデザインパターンを使ったAIエージェントの信頼性を確保するための考慮事項を認識できる。

## ツール使用デザインパターンとは何か？

**ツール使用デザインパターン**は、LLMに外部ツールとやり取りする機能を持たせ、特定の目標を達成させることに焦点を当てています。ツールとは、エージェントがアクションを実行するために呼び出せるコードのことです。ツールは電卓のような単純な関数であったり、株価や天気予報を取得するサードパーティーサービスへのAPI呼び出しであったりします。AIエージェントの文脈では、ツールは**モデルが生成した関数呼び出し**に応じてエージェントによって実行されるよう設計されています。

## どのようなユースケースに適用できるか？

AIエージェントはツールを活用して複雑なタスクを完遂したり、情報を取得したり、意思決定を行ったりできます。ツール使用デザインパターンは、データベース、ウェブサービス、コードインタプリタなど外部システムとの動的なやり取りを必要とするシナリオでよく使われます。この能力は、以下のような多様なユースケースに役立ちます：

- **動的情報取得:** エージェントは外部APIやデータベースに問い合わせて最新データを取得できる（例：SQLiteデータベースの問い合せによるデータ分析、株価・天気情報の取得）。
- **コードの実行と解釈:** エージェントはコードやスクリプトを実行して数学的問題を解いたり、レポートを生成したり、シミュレーションを行ったりする。
- **ワークフローの自動化:** タスクスケジューラ、メールサービス、データパイプラインなどのツールを統合して繰り返しや多段階のワークフローを自動化する。
- **カスタマーサポート:** エージェントはCRMシステムやチケッティングプラットフォーム、ナレッジベースと連携してユーザーの問い合わせを解決する。
- **コンテンツ生成と編集:** 文法チェッカー、テキストサマライザー、コンテンツ安全性評価ツールなどを活用してコンテンツ作成を支援する。

## ツール使用デザインパターンを実装するための要素／構成要素は何か？

これらの構成要素はAIエージェントが多彩なタスクを実行することを可能にします。ツール使用デザインパターンを実装するために必要な主要な要素は以下の通りです：

- **関数／ツールスキーマ**：利用可能なツールの詳細定義（関数名、目的、必要パラメータ、期待される出力など）。これらのスキーマはLLMがどのツールが使えるかを理解し、有効なリクエストを構築するために必要です。

- **関数実行ロジック**：ユーザーの意図や会話コンテキストに基づき、ツールがいつどのように呼び出されるかを制御します。プランナーモジュール、ルーティングメカニズム、条件フローなどが含まれる場合があります。

- **メッセージハンドリングシステム**：ユーザー入力、LLM応答、ツール呼び出し、ツール出力の会話フローを管理するコンポーネント。

- **ツール統合フレームワーク**：単純な関数から複雑な外部サービスまで、エージェントとさまざまなツールとの接続基盤。

- **エラーハンドリング＆検証**：ツール実行の失敗処理、パラメータ検証、不意の応答管理のためのメカニズム。

- **状態管理**：会話コンテキスト、過去のツールとのやり取り、永続データを追跡し、多段会話にわたる一貫性を確保。

次に、関数／ツールの呼び出しについて詳しく見ていきましょう。

### 関数／ツールの呼び出し

関数呼び出しは、大規模言語モデル（LLM）がツールとやり取りするための主な方法です。『関数』と『ツール』はしばしば同義に使われますが、『関数』（再利用可能なコードのブロック）がエージェントがタスクを実行するために使う『ツール』だからです。関数のコードを呼び出すためには、LLMがユーザーのリクエストと関数の説明を比較する必要があります。そのため、利用可能なすべての関数の説明を含むスキーマをLLMに送信します。LLMはタスクに最適な関数を選択し、その名前と引数を返します。選択された関数が呼び出され、その応答がLLMに返され、LLMはこの情報を使ってユーザーのリクエストに応答します。

関数呼び出しをエージェント用に実装するには以下が必要です：

1. 関数呼び出しをサポートするLLMモデル
2. 関数説明を含むスキーマ
3. 各関数の実装コード

都市の現在時刻を取得する例で説明しましょう：

1. **関数呼び出し対応のLLMを初期化する：**

    すべてのモデルが関数呼び出しをサポートしているわけではないので、使用しているLLMが対応しているか確認することが重要です。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a>は関数呼び出しに対応しています。まずAzure OpenAIクライアントを起動します。

    ```python
    # Azure OpenAI クライアントを初期化する
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **関数スキーマの作成：**

    次に、関数名、関数の説明、関数パラメータの名前と説明を含むJSONスキーマを定義します。
    このスキーマを先ほど作成したクライアントに渡し、ユーザーのサンフランシスコの時刻を取得したいというリクエストとともに送ります。重要なのは、**ツール呼び出し**が返されることであって、質問の最終回答ではないという点です。前述したように、LLMはタスクのために選択した関数の名前と、その関数に渡される引数を返します。

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
  
    # 初期ユーザーメッセージ
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # 最初のAPI呼び出し: モデルに関数を使用するよう依頼する
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
  
1. **タスクを実行する関数コード：**

    LLMが実行すべき関数を選択したので、そのタスクを実行するコードを実装・実行します。
    Pythonで現在時刻を取得するコードを実装できます。また、最終結果を得るためにresponse_messageから関数名と引数を抽出するコードも必要です。

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
  
      # 2番目のAPI呼び出し：モデルから最終応答を取得する
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

関数呼び出しはほとんどすべてのエージェントのツール使用デザインの中心ですが、ゼロから実装するのは時に難しいこともあります。
[レッスン2](../../../02-explore-agentic-frameworks)で学んだように、agenticフレームワークを使うことでツール使用を実装するための構成要素があらかじめ用意されています。

## agenticフレームワークを使ったツール使用の例

以下は、さまざまなagenticフレームワークを活用してツール使用デザインパターンを実装する例です：

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a>は、.NET、Python、Javaの開発者向けのオープンソースAIフレームワークで、大規模言語モデル（LLM）利用を簡単にします。関数をモデルに自動で説明し、<a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">シリアライズ</a>することで関数呼び出しのプロセスを簡素化します。また、モデルとコード間の通信も管理します。Semantic Kernelのようなagenticフレームワークを使う利点のひとつは、<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">ファイル検索</a>や<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">コードインタプリタ</a>などの事前構築済みツールにアクセス可能な点です。

以下の図は、Semantic Kernelにおける関数呼び出しプロセスを示しています：

![function calling](../../../translated_images/ja/functioncalling-diagram.a84006fc287f6014.webp)

Semantic Kernelでは関数やツールは<a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">プラグイン</a>と呼ばれます。前述の`get_current_time`関数をクラス化してプラグインに変換できます。また、関数の説明を受け取る`kernel_function`デコレータを使用できます。GetCurrentTimePluginでカーネルを作成すると、カーネルが自動的に関数とパラメータをシリアライズし、LLMに送るためのスキーマを作成します。

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# カーネルを作成する
kernel = Kernel()

# プラグインを作成する
get_current_time_plugin = GetCurrentTimePlugin(location)

# プラグインをカーネルに追加する
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>は、基盤となる計算リソースやストレージ管理不要で高品質かつ拡張可能なAIエージェントを安全に構築・展開・スケールできる新しいagenticフレームワークです。特に企業向けアプリケーションに適しており、エンタープライズグレードのセキュリティを備えたフルマネージドサービスです。

LLM APIを直接使って開発するのと比べ、Azure AI Agent Serviceは以下の利点があります：

- 自動的なツール呼び出し — ツール呼び出しの解析、ツールの実行、応答処理はすべてサーバー側で行われる。
- セキュアに管理されたデータ — 会話状態を自分で管理する代わりにスレッドに必要な情報をすべて保存できる。
- すぐに使えるツール — Bing、Azure AI Search、Azure Functionsなど、データソースと連携するツールが利用可能。

Azure AI Agent Serviceで利用できるツールは、次の2つのカテゴリーに分けられます：

1. 知識ツール：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing検索によるグラウンディング</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ファイル検索</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. アクションツール：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">関数呼び出し</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">コードインタプリタ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI定義のツール</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Serviceは、これらのツールを`toolset`として一緒に使うことを可能にします。また、特定の会話のメッセージ履歴を追跡する`threads`も活用しています。

例えば、Contosoという会社の営業担当者だとします。営業データに関する質問に応答できる対話型エージェントを開発したいとします。

以下の画像は、Azure AI Agent Serviceを使って営業データを分析する様子を表しています：

![Agentic Service In Action](../../../translated_images/ja/agent-service-in-action.34fb465c9a84659e.webp)

これらのツールをサービスで使うには、クライアントを作成し、ツールまたはツールセットを定義します。実際に実装するには次のPythonコードのようにします。LLMはツールセットを見て、ユーザーのリクエストに応じてユーザー作成関数`fetch_sales_data_using_sqlite_query`を使うか、事前構築されたコードインタプリタを使うか判断します。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_functions.py ファイル内にある fetch_sales_data_using_sqlite_query 関数。
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ツールセットの初期化
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query 関数を使用して関数呼び出しエージェントを初期化し、ツールセットに追加する
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter ツールを初期化し、ツールセットに追加する。
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 信頼できるAIエージェント構築のためにツール使用デザインパターンを使う際の特別な考慮点は何か？

LLMにより動的に生成されるSQLでの一般的な懸念はセキュリティです。特にSQLインジェクションやデータベースの削除・改ざんなどの悪意ある行動のリスクがあります。これらの懸念は妥当ですが、適切にデータベースアクセス権限を設定することで効果的に軽減できます。ほとんどのデータベースでは、データベースを読み取り専用に構成します。PostgreSQLやAzure SQLのようなデータベースサービスの場合は、アプリに読み取り専用（SELECT）ロールを割り当てるべきです。
アプリをセキュアな環境で実行することは、保護をさらに強化します。エンタープライズのシナリオでは、データは通常、運用システムから抽出および変換され、ユーザーフレンドリーなスキーマを持つ読み取り専用のデータベースまたはデータウェアハウスに格納されます。このアプローチにより、データは安全で、パフォーマンスやアクセス性が最適化され、アプリは制限された読み取り専用のアクセス権を持つことが保証されます。

## サンプルコード

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ツールの利用デザインパターンについてさらに質問がありますか？

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) に参加して、他の学習者と交流したり、オフィスアワーに参加したり、AIエージェントに関する質問に答えてもらいましょう。

## 追加リソース

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service ワークショップ</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer マルチエージェント ワークショップ</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel 関数呼び出しチュートリアル</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel コードインタプリタ</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen ツール</a>

## 前のレッスン

[エージェンティックデザインパターンの理解](../03-agentic-design-patterns/README.md)

## 次のレッスン

[エージェンティックRAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の利用により生じるいかなる誤解や誤訳についても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->