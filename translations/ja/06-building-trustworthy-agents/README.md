[![信頼できるAIエージェント](../../../translated_images/ja/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(上の画像をクリックすると、このレッスンのビデオをご覧いただけます)_

# 信頼できるAIエージェントの構築

## はじめに

このレッスンで扱う内容：

- 安全で効果的なAIエージェントの構築とデプロイ方法
- AIエージェント開発における重要なセキュリティ上の考慮事項
- AIエージェント開発におけるデータとユーザープライバシーの維持方法

## 学習目標

このレッスンを完了すると、以下ができるようになります：

- AIエージェント作成時のリスクを特定し、軽減する方法
- データとアクセスが適切に管理されるようにセキュリティ対策を実装する方法
- データプライバシーを保持し、質の高いユーザー体験を提供するAIエージェントの作成

## 安全性

まずは安全なエージェントアプリケーションの構築について見ていきましょう。安全性とは、AIエージェントが設計通りに機能することを意味します。エージェントアプリケーションの構築者として、私たちは安全性を最大化する方法とツールを持っています。

### システムメッセージフレームワークの構築

大規模言語モデル（LLM）を使ってAIアプリケーションを構築したことがあれば、堅牢なシステムプロンプトまたはシステムメッセージの設計がいかに重要かご存知でしょう。これらのプロンプトは、LLMがユーザーやデータとどのようにやり取りするかのメタルール、指示、ガイドラインを設定します。

AIエージェントの場合、設定しているタスクを完了するために非常に具体的な指示が必要になるため、システムプロンプトはさらに重要です。

スケーラブルなシステムプロンプトを作成するために、アプリケーション内で1つ以上のエージェントを構築するためのシステムメッセージフレームワークを使うことができます：

![システムメッセージフレームワークの構築](../../../translated_images/ja/system-message-framework.3a97368c92d11d68.webp)

#### ステップ 1：メタシステムメッセージの作成

メタプロンプトはLLMによって使用され、作成するエージェントのシステムプロンプトを生成します。複数のエージェントを効率よく作成できるようにテンプレートとして設計します。

以下はLLMに与えるメタシステムメッセージの例です：

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ステップ 2：基本プロンプトの作成

次のステップは、AIエージェントを説明する基本プロンプトを作成することです。エージェントの役割、完了するタスク、その他の責任を含めるべきです。

例を示します：

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ステップ 3：基本システムメッセージをLLMに提供

これでシステムメッセージを最適化できます。メタシステムメッセージをシステムメッセージとして提供し、基本システムメッセージを加えます。

これにより、AIエージェントをガイドするためにより適切に設計されたシステムメッセージが生成されます：

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### ステップ 4：繰り返し改善

このシステムメッセージフレームワークの価値は、複数のエージェントからのシステムメッセージ作成をスケールしやすくし、時間をかけてシステムメッセージを改善できることにあります。完全なユースケースに対して一度でうまく機能するシステムメッセージはめったにありません。基本システムメッセージを変えてシステムに通し、小さな調整や改善を行うことで結果を比較・評価できます。

## 脅威の理解

信頼できるAIエージェントを構築するには、AIエージェントに対するリスクや脅威を理解して軽減することが重要です。ここでは、AIエージェントへのさまざまな脅威のいくつかと、それらに対してより良く計画・準備する方法を見ていきます。

![脅威の理解](../../../translated_images/ja/understanding-threats.89edeada8a97fc0f.webp)

### タスクおよび指示の改ざん

**説明:** 攻撃者がプロンプトや入力の操作を通じてAIエージェントの指示や目標を変更しようと試みます。

**軽減策:** 危険な可能性のあるプロンプトを処理前に検出するために検証チェックや入力フィルタを実行します。これらの攻撃は通常頻繁にエージェントとやり取りを必要とするため、会話のターン数を制限することもこうした攻撃の防止につながります。

### 重要システムへのアクセス

**説明:** AIエージェントが機密データを保管するシステムやサービスにアクセスできる場合、攻撃者がエージェントとこれらサービス間の通信を侵害することがあります。これには直接攻撃や、エージェントを通じてこれらのシステムに関する情報を得ようとする間接的な試みも含まれます。

**軽減策:** 必要に応じてのみAIエージェントにシステムアクセスを与えることで、この種の攻撃を防ぎます。エージェントとシステム間の通信も安全であるべきです。認証とアクセス制御の実装も情報保護に有効です。

### リソースおよびサービスの過負荷

**説明:** AIエージェントはタスクを完了するためにさまざまなツールやサービスにアクセスします。攻撃者はこれを利用してエージェント経由で大量のリクエストを送信し、サービスを攻撃し、システム障害や高額なコストを引き起こす可能性があります。

**軽減策:** AIエージェントがサービスに送信できるリクエスト数を制限するポリシーを実装します。会話のターン数やリクエスト数を制限することもこの種の攻撃防止につながります。

### ナレッジベースの改ざん

**説明:** このタイプの攻撃はAIエージェント自体ではなく、エージェントが利用するナレッジベースやその他のサービスを対象とします。これにより、AIエージェントがタスク遂行に使用するデータが破損し、偏ったり意図しない回答をユーザーに返すことがあります。

**軽減策:** AIエージェントがワークフロー内で使用するデータの定期的な検証を行います。このデータへのアクセスは安全に管理され、信頼される人物のみが変更できるようにします。

### 連鎖的エラー

**説明:** AIエージェントは様々なツールやサービスを利用してタスクを行います。攻撃者によるエラーが他の接続されたシステムの障害を引き起こし、攻撃の影響範囲が広がり、トラブルシューティングが困難になることがあります。

**軽減策:** AIエージェントをDockerコンテナ内で実行するなど、限定された環境で動作させることで直接のシステム攻撃を防ぎます。特定のシステムがエラーを返した場合にフォールバックや再試行ロジックを組み込むことも、大規模障害の防止に有効です。

## ヒューマンインザループ

信頼できるAIエージェントシステムを構築するもう一つの効果的な方法は、ヒューマンインザループを使うことです。これによりユーザーは処理中のエージェントにフィードバックを与える流れが生まれます。ユーザーはマルチエージェントシステムの一員のように機能し、処理の承認や終了が可能になります。

![ヒューマンインザループ](../../../translated_images/ja/human-in-the-loop.5f0068a678f62f4f.webp)

次に示すのは、Microsoft Agent Frameworkを使ってこのコンセプトを実装したコードスニペットです：

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# 人間の確認を含むプロバイダーを作成する
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# 人間の承認ステップを含むエージェントを作成する
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ユーザーは応答を確認して承認できます
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## 結論

信頼できるAIエージェントを構築するには、慎重な設計、堅牢なセキュリティ対策、継続的な改善が必要です。構造化されたメタプロンプトシステムの実装、潜在的な脅威の理解および軽減策の適用により、安全かつ効果的なAIエージェントを開発できます。さらに、ヒューマンインザループのアプローチを取り入れることで、AIエージェントがユーザーのニーズに合致しつつリスクを最小限に抑えることが可能です。AIの進化が続くなか、セキュリティ、プライバシー、倫理的配慮において積極的な姿勢を維持することが、AI駆動システムにおける信頼と信頼性を育む鍵となります。

### 信頼できるAIエージェント構築についてもっと知りたいですか？

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)に参加して、他の学習者と交流したり、オフィスアワーに参加し、AIエージェントに関する質問に答えてもらいましょう。

## 追加リソース

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">責任あるAIの概要</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">生成AIモデルおよびAIアプリケーションの評価</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">安全なシステムメッセージ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">リスク評価テンプレート</a>

## 前のレッスン

[Agentic RAG](../05-agentic-rag/README.md)

## 次のレッスン

[計画デザインパターン](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類は、AI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる場合があります。原文の母国語による文書が正式な情報源とみなされるべきです。重要な情報に関しては、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳に関して、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->