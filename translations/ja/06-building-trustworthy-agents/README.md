[![信頼できるAIエージェント](../../../translated_images/ja/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(上の画像をクリックするとこのレッスンの動画が表示されます)_

# 信頼できるAIエージェントの構築

## はじめに

このレッスンでは以下をカバーします：

- 安全で効果的なAIエージェントの構築と展開方法
- AIエージェント開発における重要なセキュリティ上の考慮事項
- AIエージェント開発時のデータおよびユーザープライバシーの維持方法

## 学習目標

このレッスンを修了すると、以下ができるようになります：

- AIエージェントを作成する際のリスクを特定し軽減する
- データとアクセスを適切に管理するためのセキュリティ対策を実装する
- データプライバシーを維持し、質の高いユーザー体験を提供するAIエージェントを作成する

## 安全性

まずは安全なエージェント型アプリケーションの構築について見ていきましょう。安全性とは、AIエージェントが設計通りに動作することを意味します。エージェント型アプリケーションの開発者として、安全性を最大化するための方法やツールがあります：

### システムメッセージフレームワークの構築

LLM（大型言語モデル）を使ってAIアプリケーションを構築したことがあるなら、堅牢なシステムプロンプト（システムメッセージ）設計の重要性をご存知でしょう。これらのプロンプトはLLMがユーザーやデータとどのようにやり取りするかのメタルール、指示、ガイドラインを定めます。

AIエージェントの場合は、エージェントが設計したタスクを完遂するために、さらに具体的な指示が必要なのでシステムプロンプトの役割が一層重要になります。

スケーラブルなシステムプロンプトを作成するには、アプリケーション内で1つ以上のエージェントのためのシステムメッセージフレームワークを使用できます：

![システムメッセージフレームワークの構築](../../../translated_images/ja/system-message-framework.3a97368c92d11d68.webp)

#### ステップ1: メタシステムメッセージを作成する

メタプロンプトは、LLMにエージェントのためのシステムプロンプトを生成させるために使用します。必要に応じて複数のエージェントを効率的に作成できるようテンプレートとして設計します。

以下はLLMに渡すメタシステムメッセージの例です：

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ステップ2: 基本プロンプトを作成する

次に、AIエージェントを説明する基本的なプロンプトを作成します。エージェントの役割、担当するタスク、その他の責務を含めるべきです。

例を示します：

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ステップ3: 基本システムメッセージをLLMに渡す

この時点で、メタシステムメッセージをシステムメッセージとして、さらに基本のシステムメッセージを提供して、このシステムメッセージを最適化します。

これにより、AIエージェントを適切にガイドするためにより良く設計されたシステムメッセージが生成されます：

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

#### ステップ4: 繰り返し改良する

このシステムメッセージフレームワークの価値は、複数のエージェントでシステムメッセージの作成を簡単にスケールアップできること、そして時間経過と共にシステムメッセージを改善できることです。初回で完全に適用できるシステムメッセージは稀なので、基本的なシステムメッセージを変更しシステムに再実行させ、結果を比較評価しながら小さな調整や改善を繰り返すことが重要です。

## 脅威の理解

信頼できるAIエージェントを構築するには、そのAIエージェントに対するリスクや脅威を理解し軽減することが重要です。ここではAIエージェントに対面する代表的な脅威のいくつかと、それに対してどのように計画し準備すべきか見ていきましょう。

![脅威の理解](../../../translated_images/ja/understanding-threats.89edeada8a97fc0f.webp)

### タスクおよび指示の改変

**説明:** 攻撃者はプロンプト操作や入力の改変を通じて、AIエージェントの指示や目標を変更しようと試みます。

**軽減策:** 有害なプロンプトをAIエージェントに処理させる前に検出するため、検証チェックと入力フィルターを実行します。これらの攻撃は頻繁な対話を要する場合が多いため、会話のターン数を制限することも効果的です。

### 重要システムへのアクセス

**説明:** AIエージェントが機密データを保管するシステムやサービスにアクセスできる場合、攻撃者がエージェントとこれらサービス間の通信を乗っ取る可能性があります。これは直接的な攻撃やエージェントを通じて情報収集を行う間接的な攻撃も含みます。

**軽減策:** AIエージェントには必要最低限のシステムアクセスのみに制限することが重要です。エージェントとシステム間の通信はセキュアに保ち、認証やアクセス制御を実装して情報を守りましょう。

### リソースおよびサービスの過負荷

**説明:** AIエージェントは様々なツールやサービスを利用してタスクを完了します。攻撃者はこれを利用し、AIエージェントを通じて大量のリクエストを送りサービスを過負荷にし、システム障害や高額コストの発生を引き起こす可能性があります。

**軽減策:** AIエージェントがサービスへ送るリクエスト数を制限するポリシーを設定してください。会話のターン数やAIエージェントへのリクエスト数の制限もこの種の攻撃防止に有効です。

### 知識ベースの汚染

**説明:** この攻撃はAIエージェント自体を直接狙うわけではなく、AIエージェントが使用する知識ベースや他のサービスを標的とします。データや情報の破損や改ざんが行われ、ユーザーへの回答が偏ったり意図しない内容になる恐れがあります。

**軽減策:** AIエージェントが使用するデータの定期的な検証を行いましょう。このデータへのアクセスは信頼できる人物だけに限定し、安全に保つことが重要です。

### 連鎖的なエラー

**説明:** AIエージェントは複数のツールやサービスを利用します。攻撃者によるエラーは他の連結したシステムの障害を引き起こし、攻撃範囲が拡大しトラブルシューティングが困難になる場合があります。

**軽減策:** AIエージェントをDockerコンテナのような限定された環境で動作させ、直接システム攻撃を防止する方法があります。また、システムからのエラー応答時にフォールバック機構や再試行ロジックを設け、大規模なシステム障害を防ぐ手段となります。

## ヒューマン・イン・ザ・ループ

信頼できるAIエージェントシステムを構築するもう1つの効果的な方法がヒューマン・イン・ザ・ループです。これは実行中にユーザーがエージェントへフィードバックを提供できるフローを作るもので、ユーザーは多エージェントシステムの一員としてプロセスの承認や停止を行います。

![ヒューマン・イン・ザ・ループ](../../../translated_images/ja/human-in-the-loop.5f0068a678f62f4f.webp)

以下はMicrosoft Agent Frameworkを使用し、このコンセプトを実装しているコードスニペットです：

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# 人間の承認を含むプロバイダーを作成する
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

## まとめ

信頼できるAIエージェントを構築するには、慎重な設計、堅牢なセキュリティ対策、継続的な改善が不可欠です。構造化されたメタプロンプトシステムの実装、潜在的な脅威の理解と軽減策の適用により、安全かつ効果的なAIエージェントを開発できます。さらに、ヒューマン・イン・ザ・ループの導入により、ユーザーのニーズに沿いつつリスクの最小化も可能になります。AIの進化に伴い、セキュリティ、プライバシー、倫理的考慮に積極的に取り組むことが、AI駆動型システムの信頼性と信用を高める鍵となるでしょう。

## コードサンプル

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): メタプロンプトシステムメッセージフレームワークのステップバイステップデモ
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): 事前承認ゲート、リスク階層化、信頼できるエージェントのための監査ログ

### 信頼できるAIエージェント構築についてさらに質問がありますか？

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) に参加して他の学習者と交流したり、オフィスアワーに参加してAIエージェントに関する質問に答えてもらいましょう。

## 追加リソース

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">責任あるAIの概要</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">生成AIモデルおよびAIアプリケーションの評価</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">安全性システムメッセージ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">リスク評価テンプレート</a>

## 前のレッスン

[Agentic RAG](../05-agentic-rag/README.md)

## 次のレッスン

[計画デザインパターン](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->