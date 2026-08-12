# Microsoft Agent Framework Workflow を使ったマルチエージェントアプリケーションの構築

このチュートリアルでは、Microsoft Agent Framework を使用したマルチエージェントアプリケーションの理解と構築を案内します。マルチエージェントシステムの基本概念を探り、フレームワークの Workflow コンポーネントのアーキテクチャを深掘りし、さまざまなワークフローパターンに対する Python と .NET の実用的な例を通じて解説します。

## 1\. マルチエージェントシステムの理解

AI エージェントは標準的な大規模言語モデル（LLM）の能力を超えたシステムです。環境を認識し、意思決定を行い、特定の目標を達成するために行動します。マルチエージェントシステムは、単一のエージェントでは処理が困難または不可能な問題を解決するために複数のエージェントが協力する仕組みです。

### 一般的な適用シナリオ

  * <strong>複雑な問題解決</strong>: 大きなタスク（例：全社イベントの計画）を、専門化したエージェント群（例：予算エージェント、物流エージェント、マーケティングエージェント）に分割して処理。
  * <strong>バーチャルアシスタント</strong>: 主エージェントがスケジューリング、調査、予約などのタスクを他の専門エージェントに委任。
  * <strong>自動コンテンツ作成</strong>: ひとつのエージェントが草稿作成、別のエージェントが正確性とトーンをレビューし、さらに別のエージェントが公開するワークフロー。

### マルチエージェントパターン

マルチエージェントシステムは、相互作用の仕方によって様々なパターンに分類されます：

  * <strong>順次</strong>: エージェントは定められた順序で動作し、一つのエージェントの出力が次の入力となる、組立ラインのような流れ。
  * <strong>並行</strong>: 複数のエージェントがタスクの別々の部分を同時に処理し、その結果を最後に集約。
  * <strong>条件分岐</strong>: エージェントの出力に基づき流れが分岐するワークフロー。if-then-else 文のような構造。

## 2\. Microsoft Agent Framework Workflow のアーキテクチャ

Agent Framework のワークフローシステムは、複数エージェント間の複雑なやり取りを管理する先進的なオーケストレーションエンジンです。これは [Pregel スタイルの実行モデル](https://kowshik.github.io/JPregel/pregel_paper.pdf) に基づくグラフベースのアーキテクチャで、「スーパーステップ」と呼ばれる同期された処理ステップで処理が行われます。

### コアコンポーネント

アーキテクチャは主に三つの部分から成ります：

1.  **Executor（実行単位）**: 基本的な処理単位。例では `Agent` がこの executor の一種です。各 executor は複数のメッセージハンドラーを持ち、受信したメッセージの種類に応じて自動的に呼び出されます。
2.  **Edges（エッジ）**: メッセージが executor 間で通る経路を定義。条件付きも可能で、ワークフローグラフ内で情報の動的ルーティングを可能にします。
3.  **Workflow（ワークフロー）**: 全プロセスを統括し、executor、edges、実行の流れ全体を管理。メッセージが正しい順序で処理されるようにし、監視のためのイベントストリームも提供します。

*ワークフローシステムのコアコンポーネントを示す図。*

この構造により、順次チェーン、並列処理のファンアウト/ファンイン、条件付きフローのスイッチケースロジックなどの基本パターンを用いた堅牢でスケーラブルなアプリケーション構築が可能です。

## 3\. 実用例とコード解析

では、フレームワークを使ってさまざまなワークフローパターンを実装する方法を見ていきましょう。各例で Python と .NET のコードを解説します。

### ケース 1: 基本的な順次ワークフロー

最もシンプルなパターンで、一つのエージェントの出力が直接次のエージェントに渡されます。シナリオは、ホテルの `FrontDesk` エージェントが旅行推薦を行い、その推薦を `Concierge` エージェントがレビューします。

*基本的な FrontDesk -> Concierge ワークフローの図。*

#### シナリオ背景

旅行者がパリでの推薦を求めます。

1.  `FrontDesk` エージェントは簡潔にルーブル美術館の訪問を推奨します。
2.  実体験重視の `Concierge` エージェントがこの推奨を受け取り、レビューし、より地元らしい観光客の少ない代替案を提案します。

#### Python 実装解析

Python の例では、最初にそれぞれ固有の指示を持つ二つのエージェントを定義・作成します。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# エージェントの役割と指示を定義する
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# エージェントのインスタンスを作成する
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

次に `WorkflowBuilder` でグラフを構築。`front_desk_agent` を開始点とし、出力を `reviewer_agent` につなぐエッジを作成します。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

最後に初期ユーザープロンプトでワークフローを実行します。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# runはワークフローを実行します；get_outputs()は出力実行者の結果を返します。
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) 実装解析

.NET 実装も非常に似たロジックを辿ります。最初にエージェント名や指示文の定数を定義します。

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

`AzureOpenAIClient`（Responses API）を使ってエージェントを作成し、`WorkflowBuilder` で `frontDeskAgent` から `reviewerAgent` へ順次フローを設定します。

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

ユーザーメッセージでワークフローを起動し、結果をストリームで受け取ります。

### ケース 2: 複数ステップの順次ワークフロー

基本的な連続パターンを拡張して多くのエージェントが参加。複数段階の精査や変換が必要なプロセスに適しています。

#### シナリオ背景

ユーザーがリビングルームの画像を提供し家具見積もりを求めます。

1.  **Sales-Agent**: 画像内の家具を特定してリスト化。
2.  **Price-Agent**: リストの各項目に予算、中価格帯、高価格帯を含む詳細な価格内訳を提供。
3.  **Quote-Agent**: 価格リストを受け取り、Markdown 形式で正式な見積もり書を作成。

*Sales -> Price -> Quote ワークフローの図。*

#### Python 実装解析

それぞれ専門の役割を持つ三つのエージェントを定義。`add_edge` を用い連鎖を作成：`sales_agent` -> `price_agent` -> `quote_agent`。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# 3つの専門エージェントを作成する
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# 逐次ワークフローを構築する
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

入力はテキストと画像 URI を含む `ChatMessage`。フレームワークが各エージェントの出力を次に渡し、最終見積もりを生成。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# ユーザーメッセージにはテキストと画像の両方が含まれています
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# ワークフローを実行する
events = await workflow.run(message)
```

#### .NET (C\#) 実装解析

.NET 版は Python と同じ構成。三つのエージェント（`salesagent`, `priceagent`, `quoteagent`）を作成し、`WorkflowBuilder` で順次接続。

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

画像データ（バイト形式）とテキストプロンプトを含むユーザーメッセージを構築。`InProcessExecution.RunStreamingAsync` でワークフローを開始し、ストリームから最終出力を取得。

### ケース 3: 並行ワークフロー

タスクを同時実行して時間短縮する場合に使用。複数エージェントへの「ファンアウト」と結果をまとめる「ファンイン」で構成。

#### シナリオ背景

ユーザーがシアトル旅行の計画を依頼。

1.  **Dispatcher（ファンアウト）**: ユーザーのリクエストを同時に二つのエージェントに送信。
2.  **Researcher-Agent**: 12月のシアトル旅行の観光地、天候、注意点を調査。
3.  **Plan-Agent**: 独自に詳細な日毎の旅行計画を作成。
4.  **Aggregator（ファンイン）**: 調査と計画の両エージェントの出力を集約し、最終結果として提示。

*並行する Researcher と Planner ワークフローの図。*

#### Python 実装解析

`ConcurrentBuilder` によりこのパターンが簡単に作成できる。関係するエージェントを列挙するだけで、ファンアウトとファンインのロジックが自動生成される。

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilderはファンアウト／ファンインのロジックを処理します
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# ワークフローを実行します
events = await workflow.run("Plan a trip to Seattle in December")
```

フレームワークは `research_agent` と `plan_agent` を並行実行し、最終出力をリストにまとめる。

#### .NET (C\#) 実装解析

.NET ではこのパターンを明示的に定義する必要がある。カスタム executor（`ConcurrentStartExecutor` と `ConcurrentAggregationExecutor`）を作成し、ファンアウト/ファンインロジックを実装。

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

次に `WorkflowBuilder` で `AddFanOutEdge` と `AddFanInEdge` を使ってこれらカスタム executor とエージェントを含むグラフを構築。

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### ケース 4: 条件付きワークフロー

条件付きワークフローは分岐ロジックを導入し、中間結果に基づき異なる経路をたどれるようにします。

#### シナリオ背景

技術チュートリアルの作成と公開を自動化するワークフロー。

1.  **Evangelist-Agent**: 与えられた概要と URL に基づきチュートリアルの草稿を作成。
2.  **ContentReviewer-Agent**: 草稿をレビュー。語数が200語を超えているか確認。
3.  <strong>条件分岐</strong>:
      * **承認された場合（`Yes`）**: ワークフローは `Publisher-Agent` へ進行。
      * **否認された場合（`No`）**: ワークフローは停止し、拒否理由を出力。
4.  **Publisher-Agent**: 草稿が承認された場合、内容を Markdown ファイルとして保存。

#### Python 実装解析

条件ロジックを実装するためにカスタム関数 `select_targets` を使用。この関数は `add_multi_selection_edge_group` に渡され、レビュアーの出力の `review_result` フィールドに基づきワークフローを導きます。

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# この関数はレビュー結果に基づいて次のステップを決定します
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # 承認された場合、'save_draft'実行者へ進みます
        return [save_draft_id]
    else:
        # 却下された場合、失敗を報告するために'handle_review'実行者へ進みます
        return [handle_review_id]

# ワークフロービルダーはルーティングに選択関数を使用します
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # マルチセレクションエッジは条件付きロジックを実装します
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` のようなカスタム executor は、エージェントからの JSON 出力を解析し、選択関数で検査可能な強い型のオブジェクトに変換する役割を果たします。

#### .NET (C\#) 実装解析

.NET 版も似たアプローチで条件関数を使用。`ReviewResult` オブジェクトの `Result` プロパティをチェックする `Func<object?, bool>` を定義。

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

`AddEdge` メソッドの `condition` パラメーターは `WorkflowBuilder` に分岐パスを作らせる。条件 `GetCondition(expectedResult: "Yes")` が true の場合のみ `publishExecutor` へのエッジが選択され、それ以外は `sendReviewerExecutor` へ進みます。

## 結論

Microsoft Agent Framework Workflow は複雑なマルチエージェントシステムをオーケストレーションするための強力で柔軟な基盤を提供します。グラフベースのアーキテクチャとコアコンポーネントを活用することで、開発者は Python と .NET の双方で高度なワークフローを設計・実装可能です。単純な順次処理、並列実行、動的な条件分岐いずれの要件にも対応し、パワフルでスケーラブルかつ型安全な AI 駆動ソリューション構築の道具を提供します。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->