[![Planning Design Pattern](../../../translated_images/ja/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(上の画像をクリックするとこのレッスンのビデオが表示されます)_

# プランニングデザイン

## はじめに

このレッスンでは以下を扱います

* 明確な全体目標の定義と複雑なタスクを管理可能なタスクに分割する方法。
* 構造化された出力を活用して、より信頼性が高く機械が読み取りやすい応答を得る方法。
* イベント駆動型アプローチを適用して動的なタスクや予期しない入力を処理する方法。

## 学習目標

このレッスンを終了すると、次のことが理解できるようになります：

* AIエージェントのために全体目標を特定し設定し、達成すべきことを明確にする方法。
* 複雑なタスクを管理可能なサブタスクに分解し、それらを論理的な順序に整理する方法。
* エージェントに適切なツール（例：検索ツールやデータ分析ツール）を装備させ、それらをいつどのように使用するかを判断し、発生した予期しない状況に対処する方法。
* サブタスクの結果を評価し、パフォーマンスを測定し、最終出力を向上させるためにアクションを繰り返す方法。

## 全体目標の定義とタスクの分解

![Defining Goals and Tasks](../../../translated_images/ja/defining-goals-tasks.d70439e19e37c47a.webp)

多くの現実的なタスクは一度のステップで対処するには複雑すぎます。AIエージェントは、その計画と行動を導くために簡潔な目的を必要とします。例えば、次の目標を考えてみてください：

    「3日間の旅行の日程を作成する。」

これは簡単に述べられますが、まだ改善の余地があります。目標が明確であればあるほど、エージェント（および人間の協力者）が適切な成果、たとえばフライトの選択肢、ホテルの推奨、アクティビティの提案を含む包括的な日程作成に集中できます。

### タスクの分解

大規模または複雑なタスクは、小さく目標指向のサブタスクに分割すると管理しやすくなります。旅行日程の例では、目標を以下のように分解できます：

* フライト予約
* ホテル予約
* レンタカー
* パーソナライズ

各サブタスクは専用のエージェントやプロセスで対応できます。例えば、1つのエージェントは最良のフライトディールの検索に特化し、別のエージェントはホテル予約に集中する、といった具合です。調整役や「下流」のエージェントがこれらの結果をまとめて利用者に一体化した日程を提供します。

このモジュール式アプローチは段階的な拡張も可能にします。例えば、食事の推薦や現地のアクティビティ提案に特化したエージェントを追加し、時間をかけて日程を洗練させることもできます。

### 構造化された出力

大規模言語モデル（LLM）は構造化された出力（例えばJSON）を生成でき、これが計画後の下流のエージェントやサービスによる解析と処理を容易にします。これは複数エージェントの環境で特に有用で、計画の出力後にこれらのタスクを実行できます。

以下のPythonコードスニペットは、単純な計画エージェントが目標をサブタスクに分解し構造化された計画を生成する例を示しています：

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# 旅行のサブタスクモデル
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # エージェントにタスクを割り当てたい

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ユーザーメッセージを定義する
system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))
```

### マルチエージェントオーケストレーションを用いたプランニングエージェント

この例では、Semantic Router Agentがユーザーのリクエスト（例："旅行のためのホテルプランが欲しい"）を受け取ります。

プランナーは次のことを行います：

* ホテルプランを受け取る：プランナーはユーザーからのメッセージを取り、利用可能なエージェント情報を含むシステムプロンプトに基づき構造化された旅行プランを生成します。
* エージェントとそのツールの一覧を作成する：エージェントレジストリには、フライト、ホテル、レンタカー、アクティビティ用などのエージェントとそれらの機能やツールのリストが含まれています。
* 計画を該当エージェントにルーティングする：サブタスクの数に応じて、プランナーはメッセージを単一タスクの場合は専用エージェントに直接送り、複数エージェントの協力が必要な場合はグループチャットマネージャ経由で調整します。
* 結果を要約する：最後にプランナーは生成されたプランの要約を行い明確にします。
以下のPythonコードサンプルはこれらのステップを示しています：

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# 旅行サブタスクモデル

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # タスクをエージェントに割り当てたい

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# クライアントを作成する

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# ユーザーメッセージを定義する

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text

# JSONとして読み込んだ後にレスポンスの内容を表示する

pprint(json.loads(response_content))
```

以下は前述のコードの出力例で、この構造化された出力を用いて`assigned_agent`へルーティングし、旅行プランを利用者に要約して提供できます。

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

前述のコードサンプルを含むノートブックは[こちら](07-python-agent-framework.ipynb)から入手できます。

### 反復的プランニング

一部のタスクは往復のやりとりや再計画を必要とし、あるサブタスクの結果が次のタスクに影響を与えます。例えば、エージェントがフライト予約中に予期せぬデータ形式を発見した場合、ホテル予約に進む前に戦略を変更する必要があるかもしれません。

さらに、ユーザーのフィードバック（例：人間がより早いフライトを希望すると判断した場合）が部分的な再計画を引き起こす可能性があります。こうした動的かつ反復的なアプローチにより、最終的なソリューションが現実の制約や変動するユーザーの好みに沿うことが確保されます。

例：サンプルコード

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. 前のコードと同様に、ユーザーの履歴と現在のプランを渡す

system_prompt = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(
    input=user_message,
    instructions=system_prompt,
    context=f"Previous travel plan - {TravelPlan}",
)
# .. 再プランニングして、各担当エージェントにタスクを送信する
```

より包括的なプランニングについては、複雑なタスク解決のためのMagnetic Oneの<a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">ブログポスト</a>をご覧ください。

## まとめ

この記事では、利用可能なエージェントを動的に選択できるプランナーの作成例を見ました。プランナーの出力はタスクを分解しエージェントに割り当てるため、実行が可能になります。エージェントはタスクを実施するために必要な関数やツールにアクセスできることが前提です。加えて、リフレクション、サマライザー、ラウンドロビンチャットなどの他のパターンも含めてさらにカスタマイズ可能です。

## 追加リソース

Magentic One - 複雑なタスクを解決するための汎用マルチエージェントシステムで、複数のチャレンジングなエージェントベンチマークで優れた成果を達成しています。参考：<a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>。この実装ではオーケストレーターがタスク固有の計画を作成し、それらのタスクを利用可能なエージェントに委任します。計画に加え、オーケストレーターは進捗を監視し必要に応じて再計画するトラッキングメカニズムも利用しています。

### プランニングデザインパターンについてさらに質問がありますか？

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)に参加して他の学習者と交流したり、オフィスアワーに参加してAIエージェントに関する質問に答えてもらいましょう。

## 前のレッスン

[信頼できるAIエージェントの構築](../06-building-trustworthy-agents/README.md)

## 次のレッスン

[マルチエージェントデザインパターン](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。正式な情報源としては、原文の母国語による文書を参照してください。重要な情報については、専門の人間翻訳をお勧めします。本翻訳の利用により生じた誤解や解釈の相違について、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->