[![マルチエージェント設計](../../../translated_images/ja/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(上の画像をクリックすると、このレッスンのビデオを見ることができます)_
# AIエージェントにおけるメタ認知

## はじめに

AIエージェントにおけるメタ認知のレッスンへようこそ！この章は、AIエージェントが自らの思考過程についてどのように考えることができるのかに興味を持つ初心者向けに設計されています。このレッスンの終わりには、主要な概念を理解し、メタ認知をAIエージェント設計に適用するための実践的な例を身につけることができます。

## 学習目標

このレッスンを修了すると、以下ができるようになります：

1. エージェント定義における推論ループの意味を理解する。
2. 自己修正型エージェントを助けるために、計画と評価技術を使用する。
3. タスクを達成するためにコードを操作できる独自のエージェントを作成する。

## メタ認知の紹介

メタ認知とは、自分自身の思考について考える高次の認知プロセスを指します。AIエージェントにとっては、自己認識や過去の経験に基づいて行動を評価し調整できることを意味します。メタ認知、つまり「思考について考えること」は、エージェント型AIシステムの開発において重要な概念です。それはAIシステムが自らの内部プロセスを認識し、それをモニターし、制御し、適応させる能力を含みます。私たちが場の空気を読む時や問題を見る時のように。この自己認識により、AIシステムはより良い意思決定を行い、誤りを特定し、時間と共に性能を向上させることが可能になります―これはチューリングテストやAIが支配するか否かの議論にもつながります。

エージェント型AIシステムの文脈では、メタ認知は以下のような課題に対処する助けとなります：
- 透明性: AIシステムが自身の推論や決定を説明できるようにすること。
- 推論: AIシステムが情報を統合し、合理的な決定を下す能力を高めること。
- 適応性: AIシステムが新しい環境や変化する条件に適応できるようにすること。
- 知覚: AIシステムが環境からのデータを認識し解釈する精度を向上させること。

### メタ認知とは何か？

メタ認知、または「思考について考えること」は、自身の認知プロセスの自己認識と自己制御を伴う高次の認知プロセスです。AIの分野では、メタ認知はエージェントが自らの戦略や行動を評価し適応することを可能にし、問題解決や意思決定能力の向上につながります。メタ認知を理解することで、より知的で柔軟かつ効率的なAIエージェントを設計できます。真のメタ認知では、AIが自らの推論について明示的に推論しているのを見ることができます。

例：「私は安い航空券を優先しましたが…直行便を逃しているかもしれないので再確認しよう」。
あるルートを選んだ理由や方法を追跡すること。
- 前回のユーザーの好みに過度に依存して誤りを犯したことに気づき、最終的な推薦だけでなく意思決定戦略自体を修正する。
- 「ユーザーが‘混雑しすぎ’と言った時は、特定の観光地を外すだけでなく、人気順で‘トップアトラクション’を選択する方法に欠陥があるかもしれない」とパターンを診断すること。

### AIエージェントにおけるメタ認知の重要性

メタ認知は以下の理由でAIエージェント設計において極めて重要な役割を果たします：

![メタ認知の重要性](../../../translated_images/ja/importance-of-metacognition.b381afe9aae352f7.webp)

- 自己反省: エージェントが自身のパフォーマンスを評価し改善点を特定できる。
- 適応性: 過去の経験や変化する環境に基づいて戦略を修正できる。
- エラー修正: エージェントが誤りを自律的に検出し修正できることで、より正確な結果を生む。
- 資源管理: エージェントが時間や計算資源などのリソースの使用を最適化するために行動を計画し評価できる。

## AIエージェントの構成要素

メタ認知プロセスに入る前に、AIエージェントの基本的な構成要素を理解することが重要です。AIエージェントは通常以下で構成されます：

- ペルソナ: エージェントの個性と特性で、ユーザーとのやり取りの仕方を定義します。
- ツール: エージェントが実行できる能力や機能。
- スキル: エージェントが持つ知識と専門性。

これらの要素が一緒になって、特定のタスクを実行する「専門ユニット」を構成します。

<strong>例</strong>：
旅行代理店を考えてみてください。単に休暇を計画するだけでなく、リアルタイムデータや過去の顧客の旅の経験に基づいて経路を調整するエージェントサービスです。

### 例: 旅行代理店サービスにおけるメタ認知

AIが搭載された旅行代理店サービスを設計すると想像してください。このエージェント「トラベルエージェント」は、ユーザーの休暇計画を支援します。メタ認知を組み込むために、トラベルエージェントは自己認識や過去の経験に基づいて自身の行動を評価し調整する必要があります。メタ認知がどのように役立つかは以下の通りです：

#### 現在のタスク

現在のタスクは、ユーザーのパリ旅行の計画を支援することです。

#### タスクを完了するためのステップ

1. <strong>ユーザーの好みを収集</strong>：旅行日程、予算、興味（例：博物館、料理、ショッピング）、特別な要件をユーザーに聞きます。
2. <strong>情報を取得</strong>：ユーザーの好みに合致するフライト、宿泊施設、観光地、レストランを検索します。
3. <strong>推奨案を作成</strong>：フライト詳細、ホテル予約、提案アクティビティを含むパーソナライズされた旅程を提供します。
4. <strong>フィードバックに基づいて調整</strong>：推奨案に関してユーザーのフィードバックを求め、必要な修正を行います。

#### 必要なリソース

- フライトとホテルの予約データベースへのアクセス。
- パリの観光地やレストランの情報。
- 過去のユーザーインタラクションからのフィードバックデータ。

#### 経験と自己反省

トラベルエージェントはメタ認知を活用して自身のパフォーマンスを評価し、過去の経験から学習します。例えば：

1. <strong>ユーザーフィードバックの分析</strong>：どの推奨が好評でどれがそうでなかったかをレビューし、将来の提案を調整します。
2. <strong>適応性</strong>：もしユーザーが過去に混雑した場所を嫌うと言っていたら、ピーク時に人気観光地を推奨するのを避けます。
3. <strong>誤りの修正</strong>：過去に予約ミス（満室のホテルを提案したなど）があった場合、推奨前により厳密に空室状況を確認するよう学びます。

#### 実践的な開発者向け例

次は、メタ認知を組み込んだトラベルエージェントのコード例を簡単に示します：

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # 好みに基づいてフライト、ホテル、観光地を検索します
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # フィードバックを分析し、今後の推薦を調整します
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# 使用例
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### なぜメタ認知が重要なのか

- <strong>自己反省</strong>: エージェントが自身のパフォーマンスを分析し改善点を特定できる。
- <strong>適応性</strong>: フィードバックや変化する状況に応じて戦略を修正できる。
- <strong>誤り修正</strong>: 自律的に誤りを検出し修正できる。
- <strong>資源管理</strong>: 時間や計算資源の使用を最適化できる。

メタ認知を組み込むことで、トラベルエージェントはより個別化され正確な旅行推奨を提供し、ユーザー体験を向上させることができます。

---

## 2. エージェントにおける計画

計画はAIエージェントの行動において重要な要素です。これは目標を達成するために必要なステップを、現在の状態、リソース、そして可能な障害を考慮して概説することを含みます。

### 計画の要素

- <strong>現在のタスク</strong>：タスクを明確に定義する。
- <strong>タスク完了のためのステップ</strong>：タスクを管理可能なステップに分解する。
- <strong>必要なリソース</strong>：必要なリソースを特定する。
- <strong>経験</strong>：過去の経験を活用して計画に情報を与える。

<strong>例</strong>：
トラベルエージェントがユーザーの旅行計画を効果的に支援するために取るべきステップは以下の通りです：

### トラベルエージェントのステップ

1. <strong>ユーザーの好みを収集</strong>
   - 旅行日程、予算、興味、および特別な要件についてユーザーに尋ねる。
   - 例：「いつ旅行を計画していますか？」「予算の範囲は？」「休暇でどんなアクティビティを楽しみますか？」

2. <strong>情報を取得</strong>
   - ユーザーの好みを基に関連する旅行オプションを検索する。
   - <strong>フライト</strong>：ユーザーの予算と希望旅行日に基づく利用可能なフライトを探す。
   - <strong>宿泊施設</strong>：場所、価格、アメニティのユーザーの好みに合うホテルやレンタル物件を見つける。
   - <strong>観光地とレストラン</strong>：ユーザーの興味に合う人気の観光地、アクティビティ、飲食店を特定する。

3. <strong>推奨案を作成</strong>
   - 取得した情報をまとめてパーソナライズされた旅程を作成する。
   - フライト情報、ホテル予約、推奨アクティビティなど、ユーザーの好みに合わせて提案を行う。

4. <strong>ユーザーに旅程を提示</strong>
   - 提案された旅程をユーザーに共有し、レビューしてもらう。
   - 例：「こちらがパリ旅行の提案旅程です。フライト詳細、ホテル予約、推奨アクティビティとレストランのリストが含まれています。ご意見をお聞かせください！」

5. <strong>フィードバックを収集</strong>
   - ユーザーから提案旅程に対するフィードバックを求める。
   - 例：「フライトオプションは気に入りましたか？」「ホテルはご希望に合っていますか？」「追加または削除したいアクティビティはありますか？」

6. <strong>フィードバックに基づいて調整</strong>
   - ユーザーのフィードバックに基づき旅程を修正する。
   - ユーザーの好みに合うようフライト、宿泊施設、アクティビティの提案を必要に応じて変更する。

7. <strong>最終確認</strong>
   - 修正後の旅程をユーザーに提示し最終確認してもらう。
   - 例：「フィードバックに基づき調整しました。更新された旅程です。全て問題ないでしょうか？」

8. <strong>予約の確定と確認</strong>
   - ユーザーが旅程を承認した後、フライト、宿泊施設、事前計画アクティビティの予約を進める。
   - 確認情報をユーザーに送付する。

9. <strong>継続的なサポート提供</strong>
   - 旅行前および旅行中にユーザーの変更や追加リクエストに対応できるよう待機する。
   - 例：「旅行中に何かご助力が必要でしたら、いつでもご連絡ください！」

### 例示的な対話

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# ブッキングリクエストでの使用例
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. 是正的RAGシステム

まずは、RAGツールと先取りコンテキストロードの違いについて理解しましょう。

![RAGとコンテキストロードの比較](../../../translated_images/ja/rag-vs-context.9eae588520c00921.webp)

### 取得強化生成（RAG）

RAGは、検索システムと生成モデルを組み合わせたものです。クエリが発生すると、検索システムが外部ソースから関連する文書やデータを取得し、その情報を生成モデルへの入力に加えることで、より正確で文脈に沿った応答を生成するのを助けます。

RAGシステムでは、エージェントが知識ベースから関連情報を取得し、それを用いて適切な応答や行動を生成します。

### 是正的RAGアプローチ

是正的RAGアプローチは、RAG技術を活用してエラーを修正し、AIエージェントの精度を向上させることに焦点を当てています。これには以下が含まれます：

1. <strong>プロンプト技術</strong>：エージェントが関連情報を取得するように導く特定のプロンプトを使う。
2. <strong>ツール</strong>：取得情報の関連性を評価し、正確な応答を生成できるアルゴリズムや仕組みを実装する。
3. <strong>評価</strong>：エージェントの性能を継続的に評価し、精度と効率を改善するために調整する。

#### 例：検索エージェントにおける是正的RAG

ウェブから情報を取得してユーザーの質問に答える検索エージェントを考えましょう。是正的RAGアプローチでは以下が行われるかもしれません：

1. <strong>プロンプト技術</strong>：ユーザー入力に基づき検索クエリを形成する。
2. <strong>ツール</strong>：自然言語処理と機械学習アルゴリズムを用いて、検索結果をランク付けしフィルタリングする。
3. <strong>評価</strong>：ユーザーフィードバックを分析して取得情報の不正確さを特定し修正する。

### トラベルエージェントにおける是正的RAG

是正的RAG（取得強化生成）は、AIの情報取得と生成能力を向上させるだけでなく、不正確さの修正も同時に行います。トラベルエージェントが是正的RAGアプローチを使って、より正確かつ関連性の高い旅行提案を提供する方法を見てみましょう。

これには以下が含まれます：

- **プロンプト技術:** エージェントが関連情報を取得するための特定のプロンプトを使用する。
- **ツール:** 取得情報の関連性を評価し、正確な応答を生成できるアルゴリズムと仕組みを実装する。
- **評価:** エージェントの性能を継続的に評価し、精度と効率の向上のために調整を行う。

#### トラベルエージェントに是正的RAGを実装するステップ

1. <strong>初期ユーザーインタラクション</strong>
   - トラベルエージェントが目的地、旅行日程、予算、興味などの初期ユーザーの好みを収集する。
   - 例：

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. <strong>情報の取得</strong>
   - トラベルエージェントがユーザーの好みに基づくフライト、宿泊、観光地、レストランの情報を取得する。
   - 例：

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. <strong>初期推奨案の生成</strong>
   - トラベルエージェントが取得情報を用いてパーソナライズされた旅程を生成する。
   - 例：

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. <strong>ユーザーフィードバックの収集</strong>
   - トラベルエージェントが初期推奨案に対するユーザーフィードバックを求める。
   - 例：

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **是正的RAGプロセス**
   - <strong>プロンプト技術</strong>：トラベルエージェントはユーザーフィードバックに基づき新たな検索クエリを作成する。
     - 例：

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - <strong>ツール</strong>：トラベルエージェントは新しい検索結果をユーザーフィードバックに基づきランク付けしフィルタリングするアルゴリズムを利用する。
     - 例：

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - <strong>評価</strong>：トラベルエージェントはユーザーフィードバックを分析し推奨の関連性と正確性を継続的に評価し、必要に応じて調整を行う。
     - 例：

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### 実践的な例

以下はトラベルエージェントに是正的RAGアプローチを組み込んだ簡単なPythonコード例です：

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# 使用例
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### 先取りコンテキストロード


先制的なコンテキストロードとは、クエリを処理する前に関連するコンテキストや背景情報をモデルに読み込ませることを指します。これによりモデルは最初からこの情報にアクセスできるため、処理中に追加データを取得する必要がなく、より情報に基づいた応答を生成するのに役立ちます。

以下は、Pythonでの旅行代理店アプリケーションにおける先制的なコンテキストロードの簡略化された例です：

```python
class TravelAgent:
    def __init__(self):
        # 人気のある目的地とその情報を事前に読み込む
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # 事前に読み込んだコンテキストから目的地情報を取得する
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# 使用例
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### 説明

1. **初期化（`__init__` メソッド）**: `TravelAgent` クラスは、パリ、東京、ニューヨーク、シドニーなどの人気目的地に関する情報を含む辞書をあらかじめ読み込みます。この辞書には各目的地の国、通貨、言語、主要な観光地などの詳細が含まれます。

2. **情報取得（`get_destination_info` メソッド）**: ユーザーが特定の目的地について問い合わせたとき、`get_destination_info` メソッドは先に読み込んだコンテキスト辞書から該当する情報を取得します。

コンテキストをあらかじめ読み込むことで、旅行代理店アプリケーションは外部ソースからリアルタイムに情報を取得することなく、ユーザークエリに素早く応答できます。これによりアプリケーションはより効率的で応答性が向上します。

### 目標を定めてから計画をブートストラップして繰り返し改善する

計画を目標でブートストラップするとは、明確な目的や目標結果を最初に設定して始めることを指します。こうした目標を前もって設定することで、モデルは反復プロセス全体の指針としてそれを活用できます。これにより各反復で目標達成に近づくことが保証され、プロセスの効率化と集中化に繋がります。

以下は、Pythonで旅行代理店向けに目標を設定してから計画をブートストラップし、繰り返し改善する例です：

### シナリオ

旅行代理店がクライアントの好みや予算に基づいて満足度を最大化するカスタマイズされた旅行プランを立てたいと考えています。

### ステップ

1. クライアントの好みと予算を定義する。
2. これらの好みに基づいて初期プランをブートストラップする。
3. クライアントの満足度を最適化するために繰り返し計画を改善する。

#### Pythonコード

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# 使用例
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### コード説明

1. **初期化（`__init__` メソッド）**: `TravelAgent` クラスは、名前、費用、アクティビティタイプなどの属性をもつ複数の候補目的地リストで初期化されます。

2. **計画のブートストラップ（`bootstrap_plan` メソッド）**: このメソッドは、クライアントの好みと予算に基づき初期の旅行計画を作成します。目的地リストを反復し、クライアントの好みに合致し予算内であれば計画に追加します。

3. **好みのマッチング（`match_preferences` メソッド）**: このメソッドは、目的地がクライアントの好みに合うかどうかをチェックします。

4. **計画の繰り返し改善（`iterate_plan` メソッド）**: このメソッドは、計画内の各目的地をより良いマッチに置き換えられるか試み、好みと予算制約を考慮して計画を精緻化します。

5. **費用計算（`calculate_cost` メソッド）**: このメソッドは、潜在的に新しい目的地を含む現在の計画の総費用を計算します。

#### 使用例

- <strong>初期計画</strong>：旅行代理店は、観光を好むクライアントの好みと2000ドルの予算に基づいて初期計画を作成します。
- <strong>精緻化計画</strong>：旅行代理店は、クライアントの好みと予算を最適化するために計画を繰り返し改善します。

目標（例：クライアントの満足度の最大化）で計画をブートストラップし、繰り返し改善することで、旅行代理店はクライアントにカスタマイズされ最適化された旅程を作成できます。この方法は計画が最初からクライアントの好みと予算に合致し、各反復で向上することを保証します。

### LLMを活用した再ランキングとスコアリング

大規模言語モデル（LLM）は、検索した文書や生成した回答の関連性と質を評価することで再ランキングやスコアリングに利用できます。仕組みは以下の通りです：

**検索:** 最初の検索ステップで、クエリに基づき候補となる文書や回答のセットを取得します。

**再ランキング:** LLMはこれらの候補を評価し、関連性と質に基づいて再ランキングします。このステップにより最も関連性が高く質の良い情報が優先的に提示されます。

**スコアリング:** LLMは候補それぞれに関連性と質を反映したスコアを割り当て、ユーザーに最適な回答や文書を選択するのを支援します。

LLMを再ランキングとスコアリングに活用することで、システムはより正確で文脈に合った情報を提供し、全体的なユーザー体験が向上します。

以下は、Pythonでユーザーの好みに基づいて旅行先をLLMを利用して再ランキングおよびスコアリングする旅行代理店の例です：

#### シナリオ - 好みに基づく旅行

旅行代理店がクライアントの好みに基づいて最適な旅行先を推薦したいと考えています。LLMは旅行先を再ランキングおよびスコアリングして、最も関連性の高い選択肢を提供するのに役立ちます。

#### ステップ:

1. ユーザーの好みを収集する。
2. 候補となる旅行先のリストを取得する。
3. LLMを使い、ユーザーの好みに基づいて旅行先を再ランキングおよびスコアリングする。

これまでの例をAzure OpenAI Servicesを使うように更新するには以下のようにします：

#### 必要条件

1. Azureのサブスクリプションが必要です。
2. Azure OpenAIリソースを作成し、APIキーを取得します。

#### Pythonの例コード

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Azure OpenAI のためのプロンプトを生成する
        prompt = self.generate_prompt(preferences)
        
        # リクエストのヘッダーとペイロードを定義する
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # 再ランク付けされスコア付けされた目的地を取得するために Azure OpenAI API を呼び出す
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # 推薦内容を抽出して返す
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# 使用例
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### コード説明 - Preference Booker

1. <strong>初期化</strong>: `TravelAgent` クラスは、名前と説明の属性を持つ複数の潜在的旅行先リストで初期化されます。

2. **推薦の取得（`get_recommendations` メソッド）**: このメソッドはユーザーの好みに基づくプロンプトをAzure OpenAIサービスに生成し、HTTP POSTリクエストをAzure OpenAI APIに送信して再ランキングおよびスコアリングされた旅行先を取得します。

3. **プロンプト生成（`generate_prompt` メソッド）**: このメソッドはユーザーの好みと旅行先リストを含むAzure OpenAI向けのプロンプトを構築します。プロンプトは提供された好みに基づいて旅行先を再ランキングおよびスコアリングするようモデルを誘導します。

4. **API呼び出し**: `requests` ライブラリでAzure OpenAI APIエンドポイントにHTTP POSTリクエストを行います。レスポンスは再ランキングおよびスコアリングされた旅行先を含みます。

5. <strong>使用例</strong>: 旅行代理店がユーザーの好み（例：観光への関心、多様な文化）を収集し、Azure OpenAIサービスを利用して再ランキングとスコア付きの旅行先推薦を取得します。

`your_azure_openai_api_key` は実際のAzure OpenAI APIキーに、`https://your-endpoint.com/...` はご自身のAzure OpenAIデプロイメントのエンドポイントURLに置き換えてください。

LLMを再ランキングとスコアリングに活用することで、旅行代理店はよりパーソナライズされ関連性の高い旅行推薦をクライアントに提供し、体験を向上させられます。

### RAG: プロンプティング手法とツールの比較

検索強化生成（RAG）はAIエージェント開発においてプロンプト手法としても、ツールとしても利用できます。この両者の違いを理解すると、プロジェクトにおけるRAGの活用をより効果的にできます。

#### プロンプティング手法としてのRAG

**それは何か？**

- プロンプティング手法としてのRAGは、タスクやユーザー入力に基づいた特定のクエリやプロンプトを作成し、大規模なコーパスやデータベースから関連情報を検索します。その情報を利用して回答やアクションを生成します。

**仕組み：**

1. <strong>プロンプトの作成</strong>：タスクやユーザー入力に基づき、適切に構造化されたプロンプトやクエリを作成します。
2. <strong>情報の検索</strong>：既存の知識ベースやデータセットからプロンプトを用いて関連データを検索します。
3. <strong>応答の生成</strong>：検索した情報と生成AIモデルを組み合わせて包括的で一貫性のある応答を生成します。

<strong>旅行代理店における例</strong>：

- ユーザー入力："パリの博物館を訪れたい。"
- プロンプト："パリのトップ博物館を見つけてください。"
- 検索情報：ルーヴル美術館、オルセー美術館などの詳細。
- 生成応答："パリのおすすめ博物館はこちら：ルーヴル美術館、オルセー美術館、ポンピドゥー・センター。"

#### ツールとしてのRAG

**それは何か？**

- ツールとしてのRAGは、検索と生成プロセスを自動化する統合システムであり、各クエリのために手動でプロンプトを作成することなく複雑なAI機能を開発者が容易に実装できます。

**仕組み：**

1. <strong>統合</strong>：RAGをAIエージェントのアーキテクチャに組み込み、検索と生成処理を自動で行います。
2. <strong>自動化</strong>：ユーザー入力の受け取りから最終応答の生成まで全プロセスを自動管理し、明示的なプロンプトが不要です。
3. <strong>効率性</strong>：検索と生成プロセスを合理化し、より迅速かつ正確な応答を可能にします。

<strong>旅行代理店における例</strong>：

- ユーザー入力："パリの博物館を訪れたい。"
- RAGツール：博物館情報を自動で検索し応答を生成します。
- 生成応答："パリのおすすめ博物館はこちら：ルーヴル美術館、オルセー美術館、ポンピドゥー・センター。"

### 比較

| 項目                   | プロンプティング手法                                         | ツール                                                |
|------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| **手動 vs 自動**       | 各クエリのために手動でプロンプトを作成                        | 検索と生成を自動化                                    |
| <strong>制御</strong>               | 検索プロセスに対してより細かい制御が可能                      | 検索と生成を効率化・自動化                            |
| <strong>柔軟性</strong>             | 特定のニーズに合わせたカスタムプロンプトが可能                | 大規模実装に適し効率的                               |
| <strong>複雑さ</strong>             | プロンプトの作成と調整が必要                                   | AIエージェントのアーキテクチャに組み込みやすい       |

### 実用例

**プロンプティング手法の例：**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**ツールの例：**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### 関連性の評価

関連性評価はAIエージェントの性能において重要な側面です。これはエージェントが取得および生成する情報がユーザーに適切で正確かつ有用であることを保証します。ここでは関連性評価の方法、実例、技術を探ります。

#### 関連性評価の重要な概念

1. <strong>コンテキスト認識</strong>:
   - エージェントはユーザーのクエリの文脈を理解して関連情報を検索・生成する必要があります。
   - 例: ユーザーが「パリのおすすめレストラン」と尋ねた場合、料理の種類や予算などユーザーの好みを考慮すべきです。

2. <strong>正確性</strong>:
   - エージェントが提供する情報は事実に基づき最新であるべきです。
   - 例: 古い情報や閉店した店舗ではなく、現在営業中で評判の良いレストランを推薦すること。

3. <strong>ユーザーの意図</strong>:
   - クエリ背後のユーザーの意図を推測し、最も関連する情報を提供するべきです。
   - 例: 「予算に合ったホテル」と尋ねられたら、手頃な価格帯を優先する。

4. <strong>フィードバックループ</strong>:
   - ユーザーのフィードバックを継続的に収集・分析し、関連性評価を改善していきます。
   - 例: 以前の推薦に対するユーザー評価を取り入れて今後の応答を向上させる。

#### 関連性評価の実践的技術

1. <strong>関連性スコアリング</strong>:
   - 取得した各項目に対して、ユーザーのクエリや好みにどれほど合致しているかに基づきスコアを割り当てます。
   - 例：

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. <strong>フィルタリングとランキング</strong>:
   - 関連性の低い項目を除外し、残りを関連性スコアで順位付けします。
   - 例：

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # 上位10件の関連アイテムを返す
     ```

3. **自然言語処理（NLP）**:
   - NLP技術を利用してユーザーのクエリを理解し、関連情報を取得します。
   - 例：

     ```python
     def process_query(query):
         # ユーザーのクエリから重要な情報を抽出するためにNLPを使用する
         processed_query = nlp(query)
         return processed_query
     ```

4. <strong>ユーザーフィードバック統合</strong>:
   - 提供した推薦に対するユーザーフィードバックを収集し、今後の関連性評価に反映します。
   - 例：

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### 例：旅行代理店における関連性評価

旅行代理店が旅行推薦の関連性を評価する実践例はこちらです：

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # 上位10件の関連アイテムを返します

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# 使用例
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### 意図をもった検索

意図をもった検索とは、ユーザーのクエリに隠された目的や目標を理解・解釈し、最も関連性が高く有用な情報の検索と生成を行うことです。このアプローチは単なるキーワードの一致を超え、ユーザーの真のニーズと文脈を把握することに焦点を当てています。

#### 意図をもった検索の重要な概念

1. <strong>ユーザー意図の理解</strong>:
   - ユーザー意図は主に情報取得型、ナビゲーション型、取引型の3つに分類されます。
     - <strong>情報取得型</strong>: ユーザーがトピックについて情報を求めている（例：「パリのおすすめ博物館は？」）。
     - <strong>ナビゲーション型</strong>: 特定のウェブサイトやページに移動したい（例：「ルーヴル美術館の公式サイト」）。
     - <strong>取引型</strong>: 取引や予約などを行いたい（例：「パリへの航空券を予約」）。

2. <strong>コンテキスト認識</strong>:
   - クエリの文脈を分析し、過去の対話、ユーザーの好み、現在の要件などを考慮して意図を正確に特定します。

3. **自然言語処理（NLP）**:
   - NLP技術を用いてユーザーの自然言語クエリを理解・解釈します。エンティティ認識、感情分析、構文解析などが含まれます。

4. <strong>パーソナライズ</strong>:
   - ユーザーの履歴、好み、フィードバックに基づいて検索結果を個別化し、関連性を高めます。

#### 実践例：旅行代理店における意図をもった検索

旅行代理店を例に、意図をもった検索の実装例を見てみましょう。

1. <strong>ユーザーの好み収集</strong>

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. <strong>ユーザー意図の理解</strong>

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. <strong>コンテキスト認識</strong>


   ```python
   def analyze_context(query, user_history):
       # 現在のクエリをユーザーの履歴と組み合わせて文脈を理解する
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. <strong>検索と結果のパーソナライズ</strong>

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # 情報目的の検索ロジックの例
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # ナビゲーション目的の検索ロジックの例
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # 取引目的の検索ロジックの例
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # 個人化ロジックの例
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # トップ10のパーソナライズされた結果を返す
   ```

5. <strong>使用例</strong>

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. ツールとしてのコード生成

コード生成エージェントはAIモデルを使ってコードを書き、実行し、複雑な問題を解決しタスクを自動化します。

### コード生成エージェント

コード生成エージェントは生成AIモデルを用いてコードを書き、実行します。これらのエージェントは、複雑な問題を解決し、タスクを自動化し、様々なプログラミング言語でコードを生成・実行することで貴重な洞察を提供します。

#### 実用例

1. <strong>自動コード生成</strong>：データ分析、ウェブスクレイピング、機械学習など特定のタスクのためのコードスニペットを生成する。
2. **RAGとしてのSQL**：データベースからデータを取得し操作するためにSQLクエリを使用する。
3. <strong>問題解決</strong>：アルゴリズムの最適化やデータ分析など、特定の問題を解決するコードを作成・実行する。

#### 例：データ分析用のコード生成エージェント

コード生成エージェントの設計を想像してみましょう。次のように動作するかもしれません：

1. <strong>タスク</strong>：データセットを分析して傾向とパターンを特定する。
2. <strong>ステップ</strong>：
   - データセットをデータ分析ツールに読み込む。
   - データを絞り込み集約するためのSQLクエリを生成する。
   - クエリを実行し結果を取得する。
   - 結果を使って可視化や洞察を生成する。
3. <strong>必要リソース</strong>：データセットへのアクセス、データ分析ツール、SQL機能。
4. <strong>経験</strong>：過去の分析結果を用いて将来の分析の精度と関連性を高める。

### 例：旅行代理店用コード生成エージェント

この例では、旅行計画の支援のためコードを生成・実行する旅行代理店というコード生成エージェントを設計します。このエージェントは、旅行オプションの取得、結果のフィルタリング、日程表の作成などのタスクを生成AIを使って処理できます。

#### コード生成エージェントの概要

1. <strong>ユーザーの好みの収集</strong>：目的地、旅行日程、予算、興味などのユーザー入力を収集する。
2. <strong>データ取得のためのコード生成</strong>：フライト、ホテル、観光名所に関するデータを取得するコードスニペットを生成する。
3. <strong>生成コードの実行</strong>：生成したコードを実行しリアルタイム情報を取得する。
4. <strong>旅程の生成</strong>：取得したデータを基にパーソナライズされた旅行プランを作成する。
5. <strong>フィードバックに基づく調整</strong>：ユーザーのフィードバックを受け取り、必要に応じてコードを再生成して結果を改善する。

#### 実装のステップバイステップ

1. <strong>ユーザーの好みの収集</strong>

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. <strong>データ取得コードの生成</strong>

   ```python
   def generate_code_to_fetch_data(preferences):
       # 例：ユーザーの希望に基づいてフライトを検索するコードを生成する
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # 例：ホテルを検索するコードを生成する
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. <strong>生成コードの実行</strong>

   ```python
   def execute_code(code):
       # execを使用して生成されたコードを実行する
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. <strong>旅程の生成</strong>

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. <strong>フィードバックに基づく調整</strong>

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # ユーザーのフィードバックに基づいて設定を調整する
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # 更新された設定でコードを再生成および実行する
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### 環境認識と推論の活用

テーブルのスキーマに基づくことで、環境認識と推論を活用してクエリ生成プロセスを強化できます。

具体的な例を示します：

1. <strong>スキーマの理解</strong>：システムはテーブルのスキーマを理解し、この情報を基にクエリ生成を行います。
2. <strong>フィードバックに基づく調整</strong>：フィードバックを基にユーザーの好みを調整し、スキーマのどのフィールドを更新すべきか推論します。
3. <strong>クエリの生成と実行</strong>：調整された好みに基づき、フライトとホテルの最新データを取得するクエリを生成、実行します。

これらの概念を取り入れた更新されたPythonコード例は以下の通りです：

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # ユーザーのフィードバックに基づいて設定を調整する
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # スキーマに基づいた推論で他の関連設定を調整する
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # スキーマとフィードバックに基づくカスタムロジックで設定を調整する
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # 更新された設定に基づいてフライトデータを取得するコードを生成する
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # 更新された設定に基づいてホテルデータを取得するコードを生成する
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # コードの実行をシミュレートし、モックデータを返す
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # フライト、ホテル、アトラクションに基づいて旅程を生成する
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# 例のスキーマ
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# 使用例
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# 更新された設定でコードを再生成し実行する
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### 説明 - フィードバックに基づく予約

1. <strong>スキーマ認識</strong>：`schema`辞書は、フィードバックに基づく好みの調整方法を定義し、`favorites`や`avoid`といったフィールドと対応する調整を含みます。
2. **好みの調整（`adjust_based_on_feedback`メソッド）**：このメソッドはユーザーのフィードバックとスキーマを用いて好みを調整します。
3. **環境に基づく調整（`adjust_based_on_environment`メソッド）**：スキーマとフィードバックに基づいて調整内容をカスタマイズします。
4. <strong>クエリの生成と実行</strong>：調整済みの好みに基づき更新されたフライトとホテルデータを取得するコードを生成・実行します。
5. <strong>旅程の生成</strong>：新しいフライト、ホテル、観光名所データを元に更新された旅程を作成します。

システムを環境認識させ、スキーマに基づく推論を行うことで、より正確で関連性の高いクエリを生成し、より良い旅行の提案とパーソナライズされたユーザー体験を実現できます。

### RAG技術としてのSQLの利用

SQL（構造化問い合わせ言語）はデータベースとのやり取りに強力なツールです。Retrieval-Augmented Generation (RAG) の一部として使用すると、SQLはデータベースから関連データを取得し、AIエージェントの応答や行動生成に活用できます。Travel Agentの文脈でRAG技術としてのSQLの利用法を見てみましょう。

#### 重要な概念

1. <strong>データベースとのやり取り</strong>：
   - SQLはデータベースにクエリを送り、関連情報を取得し、データ操作を行うために使われます。
   - 例：旅行データベースからフライト情報、ホテル情報、観光地情報を取得する。

2. **RAGとの統合**：
   - ユーザーの入力と好みに基づいてSQLクエリを生成します。
   - 取得したデータを用いてパーソナライズされた提案や行動を作成します。

3. <strong>動的クエリ生成</strong>：
   - AIエージェントは状況とユーザーのニーズに基づき動的にSQLクエリを生成します。
   - 例：予算、日程、興味に基づいてクエリをカスタマイズし結果を絞り込む。

#### 応用例

- <strong>自動コード生成</strong>：特定のタスク用のコードスニペットを生成。
- **RAGとしてのSQL**：データ操作のためにSQLクエリを利用。
- <strong>問題解決</strong>：問題解決用のコードを作成・実行。

<strong>例</strong>：
データ分析エージェント：

1. <strong>タスク</strong>：データセットを分析し傾向を見つける。
2. <strong>ステップ</strong>：
   - データセットの読み込み。
   - データを絞り込むSQLクエリの生成。
   - クエリの実行と結果取得。
   - 可視化と洞察の生成。
3. <strong>リソース</strong>：データセットアクセス、SQL機能。
4. <strong>経験</strong>：過去の結果を活用し将来の分析を改善。

#### 実践例：Travel AgentでのSQL利用

1. <strong>ユーザーの好み収集</strong>

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **SQLクエリ生成**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **SQLクエリ実行**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. <strong>提案生成</strong>

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### SQLクエリ例

1. <strong>フライトクエリ</strong>

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. <strong>ホテルクエリ</strong>

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. <strong>観光名所クエリ</strong>

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Retrieval-Augmented Generation (RAG) の一環としてSQLを活用することで、Travel AgentのようなAIエージェントは関連データを動的に取得し、正確でパーソナライズされた提案を行うことができます。

### メタ認知の例

メタ認知の実装例として、問題を解決する際に<em>意思決定プロセスを振り返る</em>単純なエージェントを作成しましょう。この例では、エージェントがホテルを選択し、その後自らの推論を評価し、誤りや最適でない選択をした場合に戦略を調整します。

価格と品質の組み合わせに基づいてホテルを選択しつつ、決定を「振り返り」調整する基本的な例でシミュレーションします。

#### これがメタ認知を示す方法：

1. <strong>初期決定</strong>：エージェントは品質の影響を理解せず、最も安いホテルを選びます。
2. <strong>振り返りと評価</strong>：初期選択後、ユーザーのフィードバックを使いそのホテルが「悪い」選択かどうかを確認し、品質が低すぎる場合は推論を振り返ります。
3. <strong>戦略の調整</strong>：振り返りに基づいて戦略を調整し、「最安値」から「最高品質」への切替を行い、今後の意思決定を改善します。

例を示します：

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # 以前に選ばれたホテルを保存します
        self.corrected_choices = []  # 修正された選択を保存します
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # 利用可能な戦略

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # 最後の選択が良かったかどうかを教えてくれるユーザーフィードバックがあると仮定します
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # 前回の選択が満足できなかった場合に戦略を調整します
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# ホテルのリスト（価格と品質）をシミュレートします
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# エージェントを作成します
agent = HotelRecommendationAgent()

# ステップ1：エージェントが「最安値」戦略を使ってホテルを推薦します
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# ステップ2：エージェントが選択を振り返り、必要に応じて戦略を調整します
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# ステップ3：エージェントが調整後の戦略を使って再度推薦します
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### エージェントのメタ認知能力

キーポイントはエージェントが：
- 過去の選択と意思決定プロセスを評価すること。
- その振り返りに基づき戦略を調整すること、つまりメタ認知の実践です。

これはシンプルなメタ認知の形態で、システムが内部フィードバックに基づき推論プロセスを調整できることを示します。

### 結論

メタ認知はAIエージェントの能力を大幅に向上させる強力なツールです。メタ認知プロセスを組み込むことで、より知的で適応性があり効率的なエージェントを設計できます。追加リソースを使用してAIエージェントにおけるメタ認知の魅力的な世界をさらに探求しましょう。

### メタ認知デザインパターンについてさらに質問がありますか？

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) に参加して他の学習者と交流し、オフィスアワーに参加し、AIエージェントに関する質問に答えてもらいましょう。

## 前のレッスン

[マルチエージェントデザインパターン](../08-multi-agent/README.md)

## 次のレッスン

[実運用でのAIエージェント](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->