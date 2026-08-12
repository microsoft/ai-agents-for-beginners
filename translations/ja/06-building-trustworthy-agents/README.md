[![Trustworthy AI Agents](../../../translated_images/ja/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(上の画像をクリックするとこのレッスンのビデオが見られます)_

# 信頼できるAIエージェントの構築

## はじめに

本レッスンでは以下について説明します：

- 安全で効果的なAIエージェントの構築とデプロイ方法
- AIエージェント開発時の重要なセキュリティ上の考慮事項
- AIエージェント開発時のデータおよびユーザープライバシーの維持方法

## 学習目標

このレッスンを修了すると、以下ができるようになります：

- AIエージェント作成時のリスクの特定と軽減
- データとアクセスが適切に管理されるようにするためのセキュリティ対策の実装
- データプライバシーを守り、質の高いユーザー体験を提供するAIエージェントの作成

## 安全性

まずは安全なエージェントアプリケーションの構築について見ていきましょう。安全性とは、AIエージェントが設計どおりに動作することを意味します。エージェントアプリケーションの開発者として、安全性を最大化する方法やツールがあります：

### システムメッセージフレームワークの構築

大規模言語モデル（LLM）を使ってAIアプリケーションを構築したことがあるなら、堅牢なシステムプロンプトやシステムメッセージの設計がいかに重要かご存じでしょう。これらのプロンプトは、LLMがユーザーやデータとどのようにやり取りするかのメタルール、指示、ガイドラインを設定します。

AIエージェントの場合はさらに重要で、AIエージェントに課したタスクを完遂するために極めて具体的な指示が必要です。

スケーラブルなシステムプロンプトを作成するには、アプリケーション内の一つまたは複数のエージェントを構築するためのシステムメッセージフレームワークを使用できます：

![Building a System Message Framework](../../../translated_images/ja/system-message-framework.3a97368c92d11d68.webp)

#### ステップ 1：メタシステムメッセージの作成

メタプロンプトは、作成するエージェントのシステムプロンプトを生成するためにLLMで使用されます。これはテンプレートとして設計し、必要に応じて複数のエージェントを効率的に作成できるようにします。

こちらはLLMに与えるメタシステムメッセージの例です：

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ステップ 2：基本的なプロンプトの作成

次のステップは、AIエージェントを説明する基本的なプロンプトを作成することです。エージェントの役割、エージェントが実行するタスク、その他エージェントの責任を含めるべきです。

例はこちらです：

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ステップ 3：基本システムメッセージをLLMに提供

今度はメタシステムメッセージをシステムメッセージとして及び基本システムメッセージと共に提供して、システムメッセージを最適化します。

これにより、AIエージェントを効果的に導くためにより良く設計されたシステムメッセージが生成されます：

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

#### ステップ 4：繰り返しと改善

このシステムメッセージフレームワークの価値は、複数エージェントからのシステムメッセージ作成を簡単にスケーリングできること、及びシステムメッセージを時間と共に改善できることにあります。最初から完全なユースケースにぴったり合うシステムメッセージは稀です。基本的なシステムメッセージを微調整し、システムを通じて結果を比較評価することで小さな改善を繰り返せます。

## 脅威の理解

信頼できるAIエージェントを構築するには、リスクや脅威を理解して軽減することが重要です。AIエージェントに対するさまざまな脅威の一部と、それらに備え計画する方法を見ていきましょう。

![Understanding Threats](../../../translated_images/ja/understanding-threats.89edeada8a97fc0f.webp)

### タスクと指示

**説明:** 攻撃者はプロンプトや入力の操作を通じてAIエージェントの指示や目標を変更しようとします。

**軽減策:** AIエージェントに処理される前に潜在的に危険なプロンプトを検出するために、検証チェックと入力フィルターを実行します。これらの攻撃は通常頻繁なやり取りを必要とするため、会話のターン数を制限することもこれらの攻撃防止に有効です。

### 重要システムへのアクセス

**説明:** AIエージェントが機密データを格納するシステムやサービスにアクセス権を持つ場合、攻撃者はエージェントとそのサービス間の通信を侵害できます。これには直接攻撃のほか、エージェントを通じてこれらのシステムの情報を得ようとする間接的な試みも含まれます。

**軽減策:** AIエージェントは必要に応じた最低限のシステムアクセスに制限し、エージェントとシステム間の通信は安全であるべきです。認証やアクセス制御を実装することも情報保護に役立ちます。

### リソースとサービスの過負荷

**説明:** AIエージェントはタスク完遂のため様々なツールやサービスにアクセスできます。攻撃者はこの能力を利用してAIエージェントを通じ大量のリクエストを送ることで、システム障害や高コストを引き起こす攻撃を仕掛けることができます。

**軽減策:** AIエージェントがサービスに送信できるリクエスト数を制限するポリシーを実装します。会話のターン数やAIエージェントへのリクエスト数を制限することもこれら攻撃防止に有効です。

### ナレッジベース汚染

**説明:** この攻撃はAIエージェント自体を直接狙うのではなく、エージェントが利用するナレッジベースやその他サービスを標的とします。これによりAIエージェントが使用するデータや情報が汚染され、偏ったり予期しない応答をユーザーに返す可能性があります。

**軽減策:** AIエージェントのワークフローで使用するデータの定期的な検証を行い、このデータへのアクセスは信頼できる人だけが変更できるように安全に保つことが必要です。

### 連鎖的なエラー

**説明:** AIエージェントは様々なツールやサービスにアクセスしてタスクを完遂します。攻撃者によるエラーがこれら他の接続システムの障害を招き、攻撃がより広範囲となり、トラブルシューティングが困難になることがあります。

**軽減策:** これを防ぐ方法の一つが、AIエージェントを制限された環境（たとえばDockerコンテナ内）で動作させ、直接のシステム攻撃を防止することです。特定システムがエラーを返した場合のフォールバック機構やリトライロジックの作成も大きなシステム障害防止に役立ちます。

## ヒューマン・イン・ザ・ループ

信頼できるAIエージェントシステムを構築するもう一つの効果的な方法がヒューマン・イン・ザ・ループの導入です。これは実行中にユーザーがエージェントにフィードバックを提供できる仕組みを作ります。ユーザーは基本的にマルチエージェントシステムの一員として機能し、実行プロセスの承認や終了を提供します。

![Human in The Loop](../../../translated_images/ja/human-in-the-loop.5f0068a678f62f4f.webp)

以下はMicrosoft Agent Frameworkを使ってこの概念を実装したコードスニペットです：

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# 人間の承認を含むプロバイダーを作成する
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# 人間の承認ステップを含むエージェントを作成する
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ユーザーはレスポンスを確認し、承認できます
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## 結論

信頼できるAIエージェントの構築には、慎重な設計、堅牢なセキュリティ対策、継続的な改善が必要です。構造化されたメタ・プロンプトシステムの実装、潜在的な脅威の理解、軽減策の適用により、安全かつ効果的なAIエージェントを開発できます。加えて、ヒューマン・イン・ザ・ループ方式を取り入れることで、AIエージェントはユーザーのニーズに沿いながらリスクを最小化して動作し続けられます。AIが進化し続ける中で、セキュリティ、プライバシー、倫理面での積極的な対策を維持することが、AI駆動システムの信頼性と信頼を育む鍵となります。

## コードサンプル

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): メタプロンプトのシステムメッセージフレームワークを段階的に実演。
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): 信頼できるエージェントのための事前承認ゲート、リスク階層化、監査ログ。

### 信頼できるAIエージェントの構築についてもっと質問がありますか？

その他の学習者と交流したり、オフィスアワーに参加してAIエージェントの質問に答えてもらうには、[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)に参加してください。

## 追加リソース

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">責任あるAIの概要</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">生成AIモデルおよびAIアプリケーションの評価</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">安全なシステムメッセージ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">リスク評価テンプレート</a>

## 前のレッスン

[Agentic RAG](../05-agentic-rag/README.md)

## 次のレッスン

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->