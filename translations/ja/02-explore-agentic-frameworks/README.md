<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a9631d0898fc3c6ecbb3a8a0da7aaba3",
  "translation_date": "2025-08-29T23:32:25+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ja"
}
-->
[![AIエージェントフレームワークの探求](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.ja.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(上の画像をクリックすると、このレッスンのビデオをご覧いただけます)_

# AIエージェントフレームワークを探る

AIエージェントフレームワークは、AIエージェントの作成、展開、管理を簡素化するために設計されたソフトウェアプラットフォームです。これらのフレームワークは、開発者に事前構築されたコンポーネント、抽象化、およびツールを提供し、複雑なAIシステムの開発を効率化します。

これらのフレームワークは、AIエージェント開発における一般的な課題に対する標準化されたアプローチを提供することで、開発者がアプリケーションのユニークな側面に集中できるようにします。また、AIシステムのスケーラビリティ、アクセシビリティ、効率性を向上させます。

## はじめに

このレッスンでは以下を学びます：

- AIエージェントフレームワークとは何か、そしてそれが開発者に何を可能にするのか？
- チームがこれらをどのように活用して、エージェントの能力を迅速にプロトタイプ化、反復、改善できるのか？
- Microsoftが作成したフレームワークやツールの違いは何か？
- 既存のAzureエコシステムツールを直接統合できるのか、それともスタンドアロンのソリューションが必要なのか？
- Azure AI Agentsサービスとは何か、そしてそれがどのように役立つのか？

## 学習目標

このレッスンの目標は以下を理解することです：

- AIエージェントフレームワークのAI開発における役割。
- AIエージェントフレームワークを活用してインテリジェントエージェントを構築する方法。
- AIエージェントフレームワークによって可能になる主要な機能。
- AutoGen、Semantic Kernel、Azure AI Agent Serviceの違い。

## AIエージェントフレームワークとは何か、そしてそれが開発者に何を可能にするのか？

従来のAIフレームワークは、アプリにAIを統合し、以下のような方法でアプリを改善するのに役立ちます：

- **パーソナライズ**: AIはユーザーの行動や好みを分析し、パーソナライズされた推奨、コンテンツ、体験を提供します。
例: Netflixのようなストリーミングサービスは、視聴履歴に基づいて映画や番組を提案し、ユーザーのエンゲージメントと満足度を向上させます。
- **自動化と効率化**: AIは反復的なタスクを自動化し、ワークフローを効率化し、運用効率を向上させます。
例: カスタマーサービスアプリは、AI搭載のチャットボットを使用して一般的な問い合わせを処理し、応答時間を短縮し、人間のエージェントをより複雑な問題に集中させます。
- **ユーザー体験の向上**: AIは、音声認識、自然言語処理、予測テキストなどのインテリジェントな機能を提供することで、全体的なユーザー体験を向上させます。
例: SiriやGoogleアシスタントのような仮想アシスタントは、音声コマンドを理解して応答するためにAIを使用し、ユーザーがデバイスと簡単にやり取りできるようにします。

### それは素晴らしいことのように聞こえますが、なぜAIエージェントフレームワークが必要なのでしょうか？

AIエージェントフレームワークは、単なるAIフレームワーク以上のものを表しています。これらは、特定の目標を達成するためにユーザー、他のエージェント、および環境とやり取りできるインテリジェントエージェントの作成を可能にするよう設計されています。これらのエージェントは、自律的な行動を示し、意思決定を行い、変化する条件に適応することができます。AIエージェントフレームワークによって可能になる主な機能を見てみましょう：

- **エージェントの協力と調整**: 複数のAIエージェントを作成し、それらが協力し、コミュニケーションを取り、複雑なタスクを解決するために調整することを可能にします。
- **タスクの自動化と管理**: マルチステップのワークフロー、タスクの委任、およびエージェント間の動的なタスク管理のメカニズムを提供します。
- **コンテキストの理解と適応**: エージェントにコンテキストを理解し、変化する環境に適応し、リアルタイムの情報に基づいて意思決定を行う能力を装備します。

要するに、エージェントはより多くのことを可能にし、自動化を次のレベルに引き上げ、環境から学び適応するよりインテリジェントなシステムを作成することを可能にします。

## エージェントの能力を迅速にプロトタイプ化、反復、改善する方法

この分野は急速に進化していますが、ほとんどのAIエージェントフレームワークに共通するいくつかの要素があります。それは、モジュールコンポーネント、協調ツール、リアルタイム学習です。これらについて詳しく見ていきましょう：

- **モジュールコンポーネントを使用する**: AI SDKは、AIおよびメモリコネクタ、自然言語またはコードプラグインを使用した関数呼び出し、プロンプトテンプレートなどの事前構築されたコンポーネントを提供します。
- **協調ツールを活用する**: 特定の役割とタスクを持つエージェントを設計し、協調ワークフローをテストおよび改善します。
- **リアルタイムで学ぶ**: エージェントがインタラクションから学び、動的に行動を調整するフィードバックループを実装します。

### モジュールコンポーネントを使用する

Microsoft Semantic KernelやLangChainのようなSDKは、AIコネクタ、プロンプトテンプレート、メモリ管理などの事前構築されたコンポーネントを提供します。

**チームがこれをどのように活用できるか**: チームはこれらのコンポーネントを迅速に組み立て、ゼロから始めることなく機能的なプロトタイプを作成し、迅速な実験と反復を可能にします。

**実際の動作**: ユーザー入力から情報を抽出する事前構築されたパーサー、データを保存および取得するメモリモジュール、ユーザーとやり取りするプロンプトジェネレーターを使用することができます。これらのコンポーネントをゼロから構築する必要はありません。

**コード例**。Semantic Kernel Pythonおよび.Netを使用して、ユーザー入力に応答するモデルを自動関数呼び出しで動作させる事前構築されたAIコネクタの使用例を見てみましょう：

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

この例からわかるように、ユーザー入力から出発地、目的地、フライト予約リクエストの日付などの重要な情報を抽出する事前構築されたパーサーをどのように活用できるかが示されています。このモジュールアプローチにより、高レベルのロジックに集中することができます。

### 協調ツールを活用する

CrewAI、Microsoft AutoGen、Semantic Kernelのようなフレームワークは、複数のエージェントを作成することを容易にします。

**チームがこれをどのように活用できるか**: チームは特定の役割とタスクを持つエージェントを設計し、協調ワークフローをテストおよび改善し、システム全体の効率を向上させることができます。

**実際の動作**: データ取得、分析、意思決定などの特定の機能を持つエージェントのチームを作成できます。これらのエージェントは、情報を共有し、共通の目標を達成するために協力します。例えば、ユーザーの問い合わせに答えたり、タスクを完了したりすることができます。

**コード例 (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

前述のコードでは、複数のエージェントがデータを分析するタスクに協力する例が示されています。各エージェントは特定の機能を果たし、エージェントを調整して目的の結果を達成します。特定の役割を持つ専用エージェントを作成することで、タスクの効率とパフォーマンスを向上させることができます。

### リアルタイムで学ぶ

高度なフレームワークは、リアルタイムのコンテキスト理解と適応の機能を提供します。

**チームがこれをどのように活用できるか**: チームは、エージェントがインタラクションから学び、動的に行動を調整するフィードバックループを実装できます。これにより、能力の継続的な改善と洗練が可能になります。

**実際の動作**: エージェントは、ユーザーフィードバック、環境データ、タスクの結果を分析して知識ベースを更新し、意思決定アルゴリズムを調整し、時間とともにパフォーマンスを向上させることができます。この反復的な学習プロセスにより、エージェントは変化する条件やユーザーの好みに適応し、システム全体の有効性を向上させます。

## AutoGen、Semantic Kernel、Azure AI Agent Serviceのフレームワークの違いは何か？

これらのフレームワークを比較する方法は多くありますが、設計、機能、およびターゲットユースケースの観点からいくつかの重要な違いを見てみましょう：

## AutoGen

AutoGenは、Microsoft ResearchのAI Frontiers Labによって開発されたオープンソースフレームワークです。これは、イベント駆動型の分散型*エージェンティック*アプリケーションに焦点を当てており、複数のLLMやSLM、ツール、および高度なマルチエージェント設計パターンを可能にします。

AutoGenは、エージェントというコアコンセプトに基づいて構築されています。エージェントは、自律的に環境を認識し、意思決定を行い、特定の目標を達成するために行動を起こすことができる存在です。エージェントは非同期メッセージを通じて通信し、独立して並行して動作することで、システムのスケーラビリティと応答性を向上させます。

Wikipediaによると、アクターとは_「並行計算の基本的な構成要素であり、受信したメッセージに応じて、ローカルな意思決定を行い、新しいアクターを作成し、メッセージを送信し、次に受信するメッセージへの応答方法を決定する」_ものです。

**ユースケース**: コード生成の自動化、データ分析タスク、計画および研究機能のためのカスタムエージェントの構築。

AutoGenの重要なコアコンセプトをいくつか紹介します：

- **エージェント**: エージェントは以下を行うソフトウェアエンティティです：
  - **メッセージを介して通信する**: メッセージは同期または非同期である可能性があります。
  - **独自の状態を維持する**: この状態は、受信したメッセージによって変更される可能性があります。
  - **アクションを実行する**: 受信したメッセージや状態の変化に応じてアクションを実行します。これらのアクションは、エージェントの状態を変更し、メッセージログの更新、新しいメッセージの送信、コードの実行、API呼び出しなどの外部効果を生み出す可能性があります。

以下は、チャット機能を持つ独自のエージェントを作成する短いコードスニペットです：

  ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
   ```
    
  　上記のコードでは、`MyAgent`が作成され、`RoutedAgent`を継承しています。このエージェントには、メッセージの内容を出力し、その後`AssistantAgent`デリゲートを使用して応答を送信するメッセージハンドラーがあります。特に、`self._delegate`に`AssistantAgent`のインスタンスを割り当てる点に注目してください。このエージェントは、チャット補完を処理できる事前構築されたエージェントです。

  　次に、このエージェントタイプをAutoGenに知らせ、プログラムを開始します：

  ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
  ```

  　上記のコードでは、エージェントがランタイムに登録され、その後エージェントにメッセージが送信され、以下のような出力が得られます：

  ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
  ```

- **マルチエージェント**: AutoGenは、複数のエージェントを作成し、それらが協力して複雑なタスクを達成することをサポートします。エージェントは情報を共有し、行動を調整して問題をより効率的に解決することができます。マルチエージェントシステムを作成するには、データ取得、分析、意思決定、ユーザーインタラクションなどの特定の機能と役割を持つ異なるタイプのエージェントを定義できます。以下はその作成例です：

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    上記のコードでは、`GroupChatManager`がランタイムに登録されています。このマネージャーは、ライター、イラストレーター、編集者、ユーザーなど、さまざまなタイプのエージェント間のやり取りを調整する役割を果たします。

- **エージェントランタイム**: フレームワークはランタイム環境を提供し、エージェント間の通信を可能にし、それらのIDとライフサイクルを管理し、セキュリティとプライバシーの境界を強制します。これにより、エージェントを安全で制御された環境で実行し、安全かつ効率的に相互作用できるようになります。興味深いランタイムは2つあります：
  - **スタンドアロンランタイム**: これは、すべてのエージェントが同じプログラミング言語で実装され、同じプロセスで実行される単一プロセスアプリケーションに適しています。以下はその動作のイラストです：

    アプリケーションスタック

    *エージェントはランタイムを介してメッセージを通信し、ランタイムはエージェントのライフサイクルを管理します*

  - **分散エージェントランタイム**: これは、エージェントが異なるプログラミング言語で実装され、異なるマシンで実行されるマルチプロセスアプリケーションに適しています。以下はその動作のイラストです：

## Semantic Kernel + エージェントフレームワーク

Semantic Kernelは、エンタープライズ対応のAIオーケストレーションSDKです。AIおよびメモリコネクタとエージェントフレームワークで構成されています。

まず、いくつかのコアコンポーネントを紹介します：

- **AIコネクタ**: PythonおよびC#で使用するための外部AIサービスおよびデータソースとのインターフェース。

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    @@CODE_BLOCK_
では、Semantic Kernelフレームワークの基本について説明しましたが、Agent Frameworkについてはどうでしょうか？

## Azure AI Agent Service

Azure AI Agent Serviceは、Microsoft Ignite 2024で導入された比較的新しいサービスです。このサービスでは、Llama 3、Mistral、CohereといったオープンソースのLLMを直接呼び出すなど、より柔軟なモデルを使用してAIエージェントを開発・展開することができます。

Azure AI Agent Serviceは、エンタープライズ向けの強力なセキュリティ機構とデータ保存方法を提供しており、企業アプリケーションに適しています。

このサービスは、AutoGenやSemantic Kernelのようなマルチエージェントオーケストレーションフレームワークとシームレスに連携します。

現在、このサービスはPublic Preview段階にあり、PythonとC#を使用してエージェントを構築することができます。

Semantic Kernel Pythonを使用して、ユーザー定義のプラグインを持つAzure AIエージェントを作成する例を以下に示します：

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### コアコンセプト

Azure AI Agent Serviceには以下のようなコアコンセプトがあります：

- **エージェント (Agent)**  
  Azure AI Agent ServiceはAzure AI Foundryと統合されています。AI Foundry内では、AIエージェントは「スマート」なマイクロサービスとして機能し、質問への回答（RAG）、アクションの実行、またはワークフローの完全な自動化を行うことができます。これは、生成AIモデルの力と、実世界のデータソースにアクセスして対話するツールを組み合わせることで実現されます。以下はエージェントの例です：

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    この例では、`gpt-4o-mini`というモデル、`my-agent`という名前、`You are helpful agent`という指示を持つエージェントが作成されています。このエージェントは、コード解釈タスクを実行するためのツールやリソースを備えています。

- **スレッドとメッセージ (Thread and messages)**  
  スレッドはもう一つの重要な概念です。スレッドは、エージェントとユーザー間の会話ややり取りを表します。スレッドを使用して、会話の進行状況を追跡したり、コンテキスト情報を保存したり、やり取りの状態を管理することができます。以下はスレッドの例です：

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    上記のコードでは、スレッドが作成され、その後スレッドにメッセージが送信されます。`create_and_process_run`を呼び出すことで、エージェントにスレッド上で作業を実行するよう依頼します。最後に、メッセージが取得され、エージェントの応答を確認するためにログに記録されます。これらのメッセージは、ユーザーとエージェント間の会話の進行状況を示しています。また、メッセージはテキスト、画像、ファイルなどさまざまな形式である可能性があり、エージェントの作業結果として画像やテキスト応答が生成される場合もあります。開発者として、この情報を使用して応答をさらに処理したり、ユーザーに提示したりすることができます。

- **他のAIフレームワークとの統合**  
  Azure AI Agent Serviceは、AutoGenやSemantic Kernelなどの他のフレームワークと連携することができます。これにより、アプリケーションの一部をこれらのフレームワークで構築し、例えばAgent Serviceをオーケストレーターとして使用することが可能です。または、すべてをAgent Service内で構築することもできます。

**ユースケース**: Azure AI Agent Serviceは、セキュアでスケーラブル、かつ柔軟なAIエージェントの展開を必要とする企業アプリケーション向けに設計されています。

## これらのフレームワークの違いは何ですか？

これらのフレームワークには多くの重複があるように思えますが、設計、機能、対象となるユースケースにいくつかの重要な違いがあります：

- **AutoGen**: マルチエージェントシステムに関する最先端の研究に焦点を当てた実験フレームワークです。高度なマルチエージェントシステムを実験・プロトタイプ化するのに最適です。
- **Semantic Kernel**: エンタープライズエージェントアプリケーションを構築するためのプロダクション対応のエージェントライブラリです。イベント駆動型、分散型エージェントアプリケーションに焦点を当てており、複数のLLMやSLM、ツール、シングル/マルチエージェント設計パターンを可能にします。
- **Azure AI Agent Service**: Azure Foundry内のエージェント向けプラットフォームおよび展開サービスです。Azure OpenAI、Azure AI Search、Bing Search、コード実行など、Azure Foundryがサポートするサービスとの接続性を提供します。

まだどれを選ぶべきか迷っていますか？

### ユースケース

いくつかの一般的なユースケースを見て、どれが適しているか確認してみましょう：

> Q: 実験や学習、概念実証のエージェントアプリケーションを構築しており、迅速に構築・実験したいです。
>
> A: AutoGenはこのシナリオに適しています。イベント駆動型、分散型エージェントアプリケーションに焦点を当てており、高度なマルチエージェント設計パターンをサポートしています。

> Q: このユースケースにおいて、Semantic KernelやAzure AI Agent ServiceよりもAutoGenが優れている理由は何ですか？
>
> A: AutoGenは特にイベント駆動型、分散型エージェントアプリケーション向けに設計されており、コード生成やデータ分析タスクを自動化するのに適しています。複雑なマルチエージェントシステムを効率的に構築するための必要なツールと機能を提供します。

> Q: Azure AI Agent Serviceもここで使えそうですが、コード生成などのツールもありますよね？
>
> A: はい、Azure AI Agent Serviceはエージェント向けのプラットフォームサービスであり、複数のモデル、Azure AI Search、Bing Search、Azure Functionsなどの組み込み機能を追加しています。Foundry Portalでエージェントを簡単に構築し、大規模に展開することができます。

> Q: まだ混乱しています。一つだけ選ぶとしたら？
>
> A: 最初にSemantic Kernelでアプリケーションを構築し、その後Azure AI Agent Serviceを使用してエージェントを展開するのが良い選択です。このアプローチでは、Semantic Kernelでマルチエージェントシステムを構築する力を活用しながら、エージェントを簡単に永続化できます。さらに、Semantic KernelにはAutoGenとのコネクタがあり、両方のフレームワークを簡単に併用できます。

以下に主要な違いを表にまとめます：

| フレームワーク | フォーカス | コアコンセプト | ユースケース |
| --- | --- | --- | --- |
| AutoGen | イベント駆動型、分散型エージェントアプリケーション | エージェント、ペルソナ、関数、データ | コード生成、データ分析タスク |
| Semantic Kernel | 人間のようなテキストコンテンツの理解と生成 | エージェント、モジュールコンポーネント、コラボレーション | 自然言語理解、コンテンツ生成 |
| Azure AI Agent Service | 柔軟なモデル、エンタープライズセキュリティ、コード生成、ツール呼び出し | モジュール性、コラボレーション、プロセスオーケストレーション | セキュアでスケーラブル、柔軟なAIエージェント展開 |

これらのフレームワークの理想的なユースケースは何ですか？

## 既存のAzureエコシステムツールを直接統合できますか、それともスタンドアロンソリューションが必要ですか？

答えは「はい」です。特にAzure AI Agent Serviceは、他のAzureサービスとシームレスに連携するように設計されているため、既存のAzureエコシステムツールを直接統合できます。例えば、Bing、Azure AI Search、Azure Functionsを統合することが可能です。また、Azure AI Foundryとの深い統合もあります。

AutoGenやSemantic KernelでもAzureサービスと統合できますが、コードからAzureサービスを呼び出す必要がある場合があります。別の方法として、Azure SDKを使用してエージェントからAzureサービスとやり取りすることもできます。さらに、前述のように、AutoGenやSemantic Kernelで構築したエージェントのオーケストレーターとしてAzure AI Agent Serviceを使用することで、Azureエコシステムへのアクセスを簡単にすることができます。

### AIエージェントフレームワークについてさらに質問がありますか？

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)に参加して、他の学習者と交流したり、オフィスアワーに参加したり、AIエージェントに関する質問に答えてもらいましょう。

## 参考資料

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel and AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution</a>

## 前のレッスン

[AIエージェントとそのユースケースの紹介](../01-intro-to-ai-agents/README.md)

## 次のレッスン

[エージェント設計パターンの理解](../03-agentic-design-patterns/README.md)

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。
