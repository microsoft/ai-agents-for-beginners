# Microsoft Foundry エージェントサービス開発

この演習では、[Microsoft Foundry ポータル](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) の Microsoft Foundry エージェントサービスツールを使用して、フライト予約用のエージェントを作成します。エージェントはユーザーと対話し、フライトに関する情報を提供できるようになります。

## 前提条件

この演習を完了するには、以下が必要です：
1. 有効なサブスクリプションを持つ Azure アカウント。[無料でアカウントを作成](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
2. Microsoft Foundry ハブを作成する権限を持っているか、作成済みのハブが必要です。
    - 役割が Contributor または Owner の場合は、このチュートリアルの手順に従ってください。

## Microsoft Foundry ハブを作成する

> **注意:** Microsoft Foundry は以前は Azure AI Studio と呼ばれていました。

1. [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) のブログ投稿のガイドラインに従い、Microsoft Foundry ハブを作成します。
2. プロジェクトが作成されたら、表示されるヒントを閉じ、Microsoft Foundry ポータルのプロジェクトページを確認します。画面は以下の画像のようなものになります：

    ![Microsoft Foundry Project](../../../translated_images/ja/azure-ai-foundry.88d0c35298348c2f.webp)

## モデルをデプロイする

1. プロジェクトの左側のペインで、**My assets** セクションの **Models + endpoints** ページを選択します。
2. **Models + endpoints** ページの **Model deployments** タブで、**+ Deploy model** メニューから **Deploy base model** を選択します。
3. 一覧から `gpt-5-mini` モデルを検索し、選択して確認します。

    > <strong>注意</strong>: TPM（トークン毎分）を減らすことで、使用中のサブスクリプションのクォータの過剰使用を防ぐことができます。

    ![Model Deployed](../../../translated_images/ja/model-deployment.3749c53fb81e18fd.webp)

## エージェントを作成する

モデルをデプロイしたので、エージェントを作成できます。エージェントは、ユーザーと対話するために使用できる会話型 AI モデルです。

1. プロジェクトの左側のペインで、**Build & Customize** セクションの **Agents** ページを選択します。
2. **+ Create agent** をクリックして新しいエージェントを作成します。**Agent Setup** ダイアログボックスで：
    - `FlightAgent` のような名前をエージェントに入力します。
    - 先ほど作成した `gpt-5-mini` モデルのデプロイメントが選択されていることを確認します。
    - エージェントに従わせたいプロンプトに応じて **Instructions** を設定します。例は以下の通りです：
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> 詳細なプロンプトについては、[こちらのリポジトリ](https://github.com/ShivamGoyal03/RoamMind)をご参照ください。
    
> また、**Knowledge Base** や **Actions** を追加してエージェントの能力を強化し、ユーザーのリクエストに基づく追加情報の提供や自動化タスクの実行を行えます。この演習ではこれらのステップはスキップできます。
    
![Agent Setup](../../../translated_images/ja/agent-setup.9bbb8755bf5df672.webp)

3. 新しいマルチ AI エージェントを作成するには、**New Agent** をクリックします。作成されたエージェントは Agents ページに表示されます。


## エージェントをテストする

エージェントを作成したら、Microsoft Foundry ポータルのプレイグラウンドでユーザーのクエリにどのように応答するかテストできます。

1. エージェントの **Setup** ペイン上部で、**Try in playground** を選択します。
2. **Playground** ペインでチャットウィンドウにクエリを入力してエージェントと対話します。例として、28日にシアトルからニューヨークへのフライト検索をエージェントに依頼できます。

    > <strong>注意</strong>: この演習ではリアルタイムデータは使用していないため、エージェントの応答が正確でない可能性があります。目的は、指示に基づきユーザーのクエリを理解して応答する能力をテストすることです。

    ![Agent Playground](../../../translated_images/ja/agent-playground.dc146586de715010.webp)

3. エージェントのテスト後、追加のインテント、トレーニングデータ、アクションを加えて能力を強化するなど、さらなるカスタマイズが可能です。

## リソースのクリーンアップ

エージェントのテストが終了したら、追加コストを避けるために削除してください。
1. [Azure ポータル](https://portal.azure.com) を開き、この演習で使用したハブリソースがデプロイされたリソースグループの内容を表示します。
2. ツールバーで **Delete resource group** を選択します。
3. リソースグループ名を入力し、削除を確定します。

## リソース

- [Microsoft Foundry ドキュメント](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry ポータル](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry 入門](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure 上の AI エージェントの基本](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->