[![AIエージェントフレームワークを探る](../../../translated_images/ja/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(上の画像をクリックするとこのレッスンのビデオを視聴できます)_

# AIエージェントフレームワークを探る

AIエージェントフレームワークは、AIエージェントの作成、デプロイ、および管理を簡素化するために設計されたソフトウェアプラットフォームです。これらのフレームワークは、開発者に対して事前構築されたコンポーネント、抽象化、およびツールを提供し、複雑なAIシステムの開発を効率化します。

これらのフレームワークは、AIエージェント開発における一般的な課題に対する標準化されたアプローチを提供することで、開発者がアプリケーションのユニークな要素に集中できるようにします。これにより、AIシステムの構築におけるスケーラビリティ、アクセス性、および効率が向上します。

## Introduction 

このレッスンでは以下を扱います:

- AIエージェントフレームワークとは何か、そして開発者が何を達成できるようにするのか？
- チームはこれらをどのように使用して、エージェントの機能を迅速にプロトタイプ、反復、改善できるか？
- Microsoft が作成したフレームワークとツール（<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> と <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>）の違いは何か？
- 既存の Azure エコシステムのツールを直接統合できるのか、それともスタンドアロンのソリューションが必要か？
- Azure AI Agents サービスとは何か、そしてそれはどのように役立っているか？

## Learning goals

このレッスンのゴールは次のことを理解するのに役立ちます:

- AI開発におけるAIエージェントフレームワークの役割。
- AIエージェント構築にAIエージェントフレームワークを活用する方法。
- AIエージェントフレームワークによって可能になる主要な機能。
- Microsoft Agent Framework と Azure AI Agent Service の違い。

## What are AI Agent Frameworks and what do they enable developers to do?

従来のAIフレームワークは、アプリにAIを統合し、次のような方法でこれらのアプリを改善するのに役立ちます:

- **Personalization**: AIはユーザーの行動や好みを分析して、パーソナライズされた推奨、コンテンツ、体験を提供できます。  
  例: Netflixのようなストリーミングサービスは、視聴履歴に基づいて映画や番組を提案し、ユーザーのエンゲージメントと満足度を高めます。
- **Automation and Efficiency**: AIは反復的なタスクを自動化し、ワークフローを合理化し、運用効率を向上させることができます。  
  例: カスタマーサービスアプリは、AI搭載のチャットボットを使用して一般的な問い合わせに対応し、応答時間を短縮し、より複雑な問題に人間のエージェントを割り当てることができます。
- **Enhanced User Experience**: AIは音声認識、自然言語処理、予測テキストなどのインテリジェントな機能を提供することで、全体的なユーザー体験を向上させることができます。  
  例: Siri や Google Assistant のような仮想アシスタントは、音声コマンドを理解して応答するためにAIを使用し、ユーザーがデバイスとやり取りしやすくします。

### That all sounds great right, so why do we need the AI Agent Framework?

AIエージェントフレームワークは、単なるAIフレームワーク以上のものを表します。これらは、ユーザー、他のエージェント、そして環境とやり取りして特定の目標を達成できるインテリジェントなエージェントの作成を可能にするように設計されています。これらのエージェントは自律的な振る舞いを示し、意思決定を行い、変化する状況に適応することができます。AIエージェントフレームワークによって可能になる主な機能を見てみましょう:

- **Agent Collaboration and Coordination**: 複数のAIエージェントを作成し、協力、通信、調整して複雑なタスクを解決できるようにします。
- **Task Automation and Management**: マルチステップワークフローの自動化、タスクの委任、エージェント間の動的なタスク管理の仕組みを提供します。
- **Contextual Understanding and Adaptation**: エージェントにコンテキストを理解し、変化する環境に適応し、リアルタイム情報に基づいて意思決定を行う能力を持たせます。

まとめると、エージェントはより多くのことを可能にし、自動化を次のレベルに引き上げ、環境から適応し学習できるよりインテリジェントなシステムを作成できるようにします。

## How to quickly prototype, iterate, and improve the agent’s capabilities?

これは急速に進化する分野ですが、ほとんどのAIエージェントフレームワークに共通している、迅速にプロトタイプ化および反復するのに役立つ要素があります。具体的にはモジュールコンポーネント、協働ツール、およびリアルタイム学習です。これらについて詳しく見ていきましょう:

- **Use Modular Components**: AI SDKは、AIおよびメモリコネクタ、自然言語やコードプラグインを使った関数呼び出し、プロンプトテンプレートなどの事前構築コンポーネントを提供します。
- **Leverage Collaborative Tools**: 特定の役割とタスクを持つエージェントを設計し、協調ワークフローをテストおよび洗練させることができます。
- **Learn in Real-Time**: エージェントがインタラクションから学習し、動的に挙動を調整するフィードバックループを実装します。

### Use Modular Components

Microsoft Agent Framework のような SDK は、AIコネクタ、ツール定義、およびエージェント管理などの事前構築コンポーネントを提供します。

**How teams can use these**: チームはこれらのコンポーネントを迅速に組み合わせて機能的なプロトタイプを作成でき、ゼロから始める必要がなく、迅速な実験と反復が可能になります。

**How it works in practice**: 事前構築されたパーサーを使用してユーザー入力から情報を抽出し、メモリモジュールでデータを保存および取得し、プロンプトジェネレーターでユーザーと対話する、といったことがすべてゼロから構築することなく可能です。

**Example code**. Microsoft Agent Framework を `AzureAIProjectAgentProvider` と一緒に使用して、モデルがツール呼び出しでユーザー入力に応答する例を見てみましょう:

``` python
# マイクロソフトエージェントフレームワークのPython例

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# 旅行の予約を行うサンプルツール関数を定義します
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # 出力例：2025年1月1日のニューヨーク行きのフライトが正常に予約されました。良い旅を！✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

この例から分かるのは、事前構築されたパーサーを活用して、フライト予約要求の出発地、目的地、日付などの重要な情報をユーザー入力から抽出できることです。このモジュラーアプローチにより、高レベルのロジックに集中できます。

### Leverage Collaborative Tools

Microsoft Agent Framework のようなフレームワークは、協力して動作できる複数のエージェントの作成を容易にします。

**How teams can use these**: チームは特定の役割とタスクを持つエージェントを設計し、協働ワークフローをテストおよび改良して、システム全体の効率を向上させることができます。

**How it works in practice**: データ取得、分析、意思決定などの専門機能を持つ各エージェントがいるエージェントチームを作成できます。これらのエージェントは情報を通信・共有して、ユーザーの質問に答えたりタスクを完了したりするという共通の目標を達成します。

**Example code (Microsoft Agent Framework)**:

```python
# Microsoft Agent Frameworkを使用して協力して動作する複数のエージェントを作成

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# データ取得エージェント
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# データ分析エージェント
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# タスク上でエージェントを順番に実行
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

前のコードで示されているのは、複数のエージェントが連携してデータを分析するタスクをどのように作成できるかという点です。各エージェントは特定の機能を実行し、指定された成果を達成するためにエージェントを調整してタスクが実行されます。専門的な役割を持つ専用のエージェントを作成することで、タスクの効率とパフォーマンスを改善できます。

### Learn in Real-Time

高度なフレームワークは、リアルタイムのコンテキスト理解と適応の機能を提供します。

**How teams can use these**: チームは、エージェントがインタラクションから学習して動的に挙動を調整するフィードバックループを実装でき、機能の継続的な改善と洗練を実現できます。

**How it works in practice**: エージェントはユーザーフィードバック、環境データ、タスク結果を分析して知識ベースを更新し、意思決定アルゴリズムを調整し、時間とともにパフォーマンスを向上させることができます。この反復学習プロセスにより、エージェントは変化する状況やユーザーの好みに適応し、システム全体の有効性を高めます。

## What are the differences between the Microsoft Agent Framework and Azure AI Agent Service?

これらのアプローチを比較する方法は多数ありますが、設計、機能、および対象となるユースケースの点でいくつかの重要な違いを見てみましょう:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework は `AzureAIProjectAgentProvider` を使用して AI エージェントを構築するための簡素化された SDK を提供します。これは、組み込みのツール呼び出し、会話管理、および Azure ID を通じたエンタープライズグレードのセキュリティを備えた Azure OpenAI モデルを活用するエージェントの作成を可能にします。

**Use Cases**: ツール使用、マルチステップワークフロー、およびエンタープライズ統合シナリオを備えた本番環境対応のAIエージェントの構築。

Microsoft Agent Framework のいくつかの重要なコア概念は次のとおりです:

- **Agents**. エージェントは `AzureAIProjectAgentProvider` を介して作成され、名前、指示、およびツールで構成されます。エージェントは次のことができます:
  - **Process user messages** を処理し、Azure OpenAI モデルを使用して応答を生成する。
  - **Call tools** 会話のコンテキストに基づいてツールを自動的に呼び出す。
  - **Maintain conversation state** 複数のやり取りにわたって会話状態を維持する。

  以下はエージェントを作成する方法を示すコードスニペットです:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Tools**. フレームワークは、エージェントが自動的に呼び出すことができる Python 関数としてツールを定義することをサポートします。ツールはエージェント作成時に登録されます:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Multi-Agent Coordination**. 異なる専門分野を持つ複数のエージェントを作成し、それらの作業を調整できます:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure Identity Integration**. フレームワークはセキュアでキー不要の認証のために `AzureCliCredential`（または `DefaultAzureCredential`）を使用し、APIキーを直接管理する必要性を排除します。

## Azure AI Agent Service

Azure AI Agent Service は、Microsoft Ignite 2024で導入された、より最近の追加機能です。Llama 3、Mistral、Cohere のようなオープンソース LLM を直接呼び出すなど、より柔軟なモデルを備えたエージェントの開発とデプロイを可能にします。

Azure AI Agent Service は、より強固なエンタープライズ向けのセキュリティ機構とデータ保存方法を提供し、エンタープライズアプリケーションに適しています。

Microsoft Agent Framework と組み合わせてエージェントの構築とデプロイを行うことができます。

このサービスは現在 Public Preview にあり、エージェント構築に Python と C# をサポートしています。

Azure AI Agent Service Python SDK を使用すると、ユーザー定義のツールを持つエージェントを作成できます:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ツール関数を定義する
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Core concepts

Azure AI Agent Service には次のようなコアコンセプトがあります:

- **Agent**. Azure AI Agent Service は Microsoft Foundry と統合されます。AI Foundry 内では、AI エージェントは質問応答（RAG）、アクションの実行、またはワークフローの完全自動化に使用できる「スマート」マイクロサービスとして機能します。これは、生成AIモデルの力を、実世界のデータソースにアクセスして対話するツールと組み合わせることで実現されます。エージェントの例を示します:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    この例では、モデル `gpt-4o-mini`、名前 `my-agent`、指示 `You are helpful agent` を使ってエージェントが作成されています。エージェントはコード解釈タスクを実行するためのツールとリソースを備えています。

- **Thread and messages**. スレッドは別の重要な概念です。これはエージェントとユーザー間の会話やインタラクションを表します。スレッドは会話の進行状況を追跡し、コンテキスト情報を保存し、インタラクションの状態を管理するために使用できます。スレッドの例を示します:

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

    前のコードではスレッドが作成され、その後スレッドにメッセージが送信されています。`create_and_process_run` を呼び出すことで、エージェントにスレッド上で作業を行うよう依頼します。最後に、メッセージを取得してエージェントの応答をログに記録します。メッセージはユーザーとエージェント間の会話の進行状況を示します。メッセージはテキスト、画像、ファイルなどの異なるタイプになり得ることも理解しておくことが重要です。つまり、エージェントの作業は例えば画像やテキスト応答のような成果をもたらすことがあります。開発者はこの情報を使用して応答をさらに処理したりユーザーに提示したりすることができます。

- **Integrates with the Microsoft Agent Framework**. Azure AI Agent Service は Microsoft Agent Framework とシームレスに連携し、`AzureAIProjectAgentProvider` を使用してエージェントを構築し、Agent Service を通じて本番シナリオにデプロイできます。

**Use Cases**: Azure AI Agent Service は、安全でスケーラブルかつ柔軟な AI エージェントのデプロイを必要とするエンタープライズアプリケーション向けに設計されています。

## What's the difference between these approaches?
 
重複があるように見えるかもしれませんが、設計、機能、および対象ユースケースの観点でいくつか重要な違いがあります:
 
- **Microsoft Agent Framework (MAF)**: エージェントを構築するための本番対応の SDK です。ツール呼び出し、会話管理、および Azure ID 統合を備えたエージェントを作成するための簡素化された API を提供します。
- **Azure AI Agent Service**: Foundry 内のエージェント向けプラットフォームおよびデプロイサービスです。Azure OpenAI、Azure AI Search、Bing Search、コード実行などのサービスへの組み込み接続を提供します。
 
まだどちらを選ぶべきか迷っていますか？

### Use Cases
 
いくつかの一般的なユースケースを見て、選択の助けになるか見てみましょう:
 
> Q: I'm building production AI agent applications and want to get started quickly
>

>A: The Microsoft Agent Framework is a great choice. It provides a simple, Pythonic API via `AzureAIProjectAgentProvider` that lets you define agents with tools and instructions in just a few lines of code.

>Q: I need enterprise-grade deployment with Azure integrations like Search and code execution
>
> A: Azure AI Agent Service is the best fit. It's a platform service that provides built-in capabilities for multiple models, Azure AI Search, Bing Search and Azure Functions. It makes it easy to build your agents in the Foundry Portal and deploy them at scale.
 
> Q: I'm still confused, just give me one option
>
> A: Start with the Microsoft Agent Framework to build your agents, and then use Azure AI Agent Service when you need to deploy and scale them in production. This approach lets you iterate quickly on your agent logic while having a clear path to enterprise deployment.
 
Let's summarize the key differences in a table:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool calling | Agents, Tools, Azure Identity | Building AI agents, tool use, multi-step workflows |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?
答えは「はい」です。既存の Azure エコシステムのツールは、特に Azure AI Agent Service と直接統合できます。これは他の Azure サービスとシームレスに連携するように構築されています。例えば、Bing、Azure AI Search、Azure Functions を統合することができます。Microsoft Foundry との深い統合もあります。

The Microsoft Agent Framework also integrates with Azure services through `AzureAIProjectAgentProvider` and Azure identity, letting you call Azure services directly from your agent tools.

## サンプルコード

- Python: [エージェント フレームワーク](./code_samples/02-python-agent-framework.ipynb)
- .NET: [エージェント フレームワーク](./code_samples/02-dotnet-agent-framework.md)

## AI エージェント フレームワークについてもっと質問がありますか？

他の学習者と出会い、オフィスアワーに参加し、AI エージェントに関する質問に答えてもらうために、[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) に参加してください。

## 参考

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure エージェント サービス</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI の応答</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent サービス</a>

## 前のレッスン

[AI エージェントとエージェントのユースケースの紹介](../01-intro-to-ai-agents/README.md)

## 次のレッスン

[エージェント型デザインパターンの理解](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責事項：
本書は AI 翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を用いて翻訳されました。正確性の確保に努めておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。重要な情報については、原文（原言語の文書）を正式な情報源として参照し、必要に応じて専門の人による翻訳を受けることを推奨します。本翻訳の利用に起因する誤解や解釈の相違については責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->