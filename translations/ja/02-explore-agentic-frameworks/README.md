<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d3ceafa2939ede602b96d6bd412c5cbf",
  "translation_date": "2025-03-28T11:46:19+00:00",
  "source_file": "02-explore-agentic-frameworks\\README.md",
  "language_code": "ja"
}
-->
[![AIエージェントフレームワークを探る](../../../translated_images/lesson-2-thumbnail.807a3a4fc57057096d10678bf84638d17d50c50239014e75a7708731a33bb802.ja.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(上の画像をクリックして、このレッスンのビデオを視聴)_

# AIエージェントフレームワークを探る

AIエージェントフレームワークは、AIエージェントの作成、展開、管理を簡素化するために設計されたソフトウェアプラットフォームです。これらのフレームワークは、開発者にプリビルドコンポーネント、抽象化、ツールを提供し、複雑なAIシステムの開発を効率化します。

これらのフレームワークは、AIエージェント開発における共通の課題に対する標準化されたアプローチを提供することで、開発者がアプリケーションの独自性に集中できるようにします。これにより、AIシステムのスケーラビリティ、アクセシビリティ、効率性が向上します。

## はじめに

このレッスンでは以下を学びます：

- AIエージェントフレームワークとは何か、それが開発者に何を可能にするのか？
- チームがこれらを活用して、エージェントの能力を迅速にプロトタイプ化、反復、改善する方法
- Microsoftによって作成されたフレームワークとツールの違いは何か？
- 既存のAzureエコシステムツールを直接統合できるのか、それともスタンドアロンソリューションが必要なのか？
- Azure AI Agentsサービスとは何か、それがどのように役立つのか？

## 学習目標

このレッスンの目標は以下の理解を深めることです：

- AIエージェントフレームワークの役割
- AIエージェントフレームワークを活用して知能エージェントを構築する方法
- AIエージェントフレームワークによって可能になる主要な機能
- AutoGen、Semantic Kernel、Azure AI Agent Serviceの違い

## AIエージェントフレームワークとは何か、それが開発者に何を可能にするのか？

従来のAIフレームワークは、アプリにAIを統合し、以下のような方法でアプリを改善するのに役立ちます：

- **パーソナライゼーション**: AIはユーザーの行動や嗜好を分析し、個別化された推奨、コンテンツ、体験を提供します。
例：Netflixのようなストリーミングサービスは、視聴履歴に基づいて映画や番組を提案し、ユーザーの満足度を向上させます。
- **自動化と効率化**: AIは繰り返し作業を自動化し、ワークフローを効率化し、運用効率を向上させます。
例：顧客サービスアプリは、AI搭載のチャットボットを使用して一般的な問い合わせを処理し、応答時間を短縮し、複雑な問題に人間のエージェントを集中させます。
- **ユーザー体験の向上**: AIは音声認識、自然言語処理、予測テキストなどのインテリジェント機能を提供することで、全体的なユーザー体験を向上させます。
例：SiriやGoogleアシスタントのような仮想アシスタントは、AIを使用して音声コマンドを理解し応答し、ユーザーがデバイスと簡単に対話できるようにします。

### 良さそうですよね。でも、なぜAIエージェントフレームワークが必要なのでしょうか？

AIエージェントフレームワークは単なるAIフレームワーク以上のものです。これらは、特定の目標を達成するためにユーザー、他のエージェント、環境と対話できるインテリジェントエージェントの作成を可能にするよう設計されています。これらのエージェントは、自律的な行動を示し、意思決定を行い、変化する条件に適応することができます。以下は、AIエージェントフレームワークによって可能になる主要な機能の例です：

- **エージェントの協力と調整**: 複数のAIエージェントを作成し、共同作業、通信、調整を行い、複雑なタスクを解決する能力を提供します。
- **タスクの自動化と管理**: 多段階のワークフロー、タスクの委任、およびエージェント間の動的タスク管理のためのメカニズムを提供します。
- **コンテキスト理解と適応**: エージェントがコンテキストを理解し、変化する環境に適応し、リアルタイム情報に基づいて意思決定を行う能力を装備します。

つまり、エージェントを使用することで、より高度な自動化、適応性のある知能システムの構築が可能になります。

## エージェントの能力を迅速にプロトタイプ化、反復、改善する方法

この分野は急速に進化していますが、ほとんどのAIエージェントフレームワークに共通する要素があります。それはモジュールコンポーネント、協調ツール、リアルタイム学習です。以下に詳しく説明します：

- **モジュールコンポーネントを活用**: AI SDKは、AIおよびメモリコネクタ、自然言語やコードプラグインを使用した機能呼び出し、プロンプトテンプレートなどのプリビルドコンポーネントを提供します。
- **協調ツールを活用**: 特定の役割やタスクを持つエージェントを設計し、協調的なワークフローをテストして洗練します。
- **リアルタイムで学ぶ**: フィードバックループを実装し、エージェントが対話から学び、動的に行動を調整します。

### モジュールコンポーネントを活用

Microsoft Semantic KernelやLangChainのようなSDKは、AIコネクタ、プロンプトテンプレート、メモリ管理などのプリビルドコンポーネントを提供します。

**チームがこれを活用する方法**: チームはこれらのコンポーネントを迅速に組み立てることで、ゼロから始めることなく機能的なプロトタイプを作成し、迅速な実験と反復を可能にします。

**実際の動作方法**: ユーザー入力から情報を抽出するプリビルドパーサー、データを保存して取得するメモリモジュール、ユーザーと対話するプロンプトジェネレーターを使用することで、これらのコンポーネントをゼロから構築することなく利用できます。

**コード例**. Semantic Kernel Pythonと.Netを使用して、モデルがユーザー入力に応答する自動機能呼び出しを行うプリビルドAIコネクタを使用する例を見てみましょう：

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

この例から分かるように、ユーザー入力からフライト予約要求の出発地、目的地、日付などの重要な情報を抽出するプリビルドパーサーを利用できます。このモジュール型アプローチにより、高レベルのロジックに集中できます。

### 協調ツールを活用

CrewAI、Microsoft AutoGen、Semantic Kernelのようなフレームワークは、複数のエージェントを作成し、それらが協力できるようにします。

**チームがこれを活用する方法**: チームは特定の役割やタスクを持つエージェントを設計し、協調的なワークフローをテストして洗練し、システム全体の効率を向上させます。

**実際の動作方法**: データ取得、分析、意思決定などの特化した機能を持つエージェントのチームを作成できます。これらのエージェントは情報を共有し、ユーザーの質問に答えたりタスクを完了したりするなど、共通の目標を達成するために協力します。

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

このコードでは、複数のエージェントが協力してデータを分析するタスクを作成する方法を示しています。各エージェントは特定の機能を実行し、エージェントを調整して望ましい結果を得るタスクを実行します。特化した役割を持つエージェントを作成することで、タスクの効率とパフォーマンスを向上させることができます。

### リアルタイムで学ぶ

高度なフレームワークは、リアルタイムのコンテキスト理解と適応能力を提供します。

**チームがこれを活用する方法**: チームはフィードバックループを実装し、エージェントが対話から学び、動的に行動を調整することで、能力を継続的に改善・洗練します。

**実際の動作方法**: エージェントはユーザーフィードバック、環境データ、タスク結果を分析し、知識ベースを更新し、意思決定アルゴリズムを調整し、時間とともにパフォーマンスを向上させます。この反復学習プロセスにより、エージェントは変化する条件やユーザーの嗜好に適応し、システム全体の有効性を向上させます。

## AutoGen、Semantic Kernel、Azure AI Agent Serviceのフレームワークの違いは何ですか？

これらのフレームワークを比較する方法はたくさんありますが、設計、機能、対象用途の観点からいくつかの重要な違いを見てみましょう：

## AutoGen

AutoGenはMicrosoft ResearchのAI Frontiers Labによって開発されたオープンソースフレームワークです。イベント駆動型、分散型の*エージェントアプリケーション*に焦点を当てており、複数のLLMやSLM、ツール、高度なマルチエージェント設計パターンを可能にします。

AutoGenは、環境を認識し、意思決定を行い、特定の目標を達成するために行動を起こす自律的なエンティティであるエージェントのコア概念を中心に構築されています。エージェントは非同期メッセージを介して通信し、独立して並行して動作することで、システムのスケーラビリティと応答性を向上させます。

Wikipediaによると、アクターは「並行計算の基本的な構成要素です。受信したメッセージに応答して、アクターはローカルで意思決定を行い、さらに多くのアクターを作成し、さらに多くのメッセージを送信し、次に受信するメッセージにどのように応答するかを決定することができます。」
モジュール性、コラボレーション、プロセスのオーケストレーション | 安全でスケーラブルかつ柔軟なAIエージェントの展開 | これらのフレームワークの理想的なユースケースは何でしょうか？

## 既存のAzureエコシステムツールを直接統合できますか、それとも独立したソリューションが必要ですか？

答えは「はい」、既存のAzureエコシステムツールをAzure AI Agent Serviceと直接統合することができます。特に、このサービスは他のAzureサービスとシームレスに連携するように構築されています。たとえば、Bing、Azure AI Search、Azure Functionsを統合することが可能です。また、Azure AI Foundryとも深く統合されています。

AutoGenやSemantic Kernelの場合でも、Azureサービスと統合することができますが、コードからAzureサービスを呼び出す必要があるかもしれません。もう1つの統合方法としては、Azure SDKを使用してエージェントからAzureサービスとやり取りする方法があります。

さらに、先に述べたように、Azure AI Agent ServiceをAutoGenやSemantic Kernelで構築したエージェントのオーケストレーターとして使用することで、Azureエコシステムへのアクセスが容易になります。

## 参考資料

---

## 前のレッスン

[AIエージェントとそのユースケースの紹介](../01-intro-to-ai-agents/README.md)

## 次のレッスン

[エージェンティックデザインパターンの理解](../03-agentic-design-patterns/README.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な表現が含まれる可能性があることをご了承ください。原文（元の言語で記載された文書）が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用により生じた誤解や誤訳について、当方は一切責任を負いません。