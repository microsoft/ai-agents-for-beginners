# エージェンティックRAG

このレッスンでは、エージェンティック・リトリーバル・オーグメンテッド・ジェネレーション（Agentic RAG）について包括的に解説します。Agentic RAGは、新たなAIパラダイムで、大規模言語モデル（LLM）が外部ソースから情報を取得しながら、自律的に次のステップを計画する仕組みです。従来の静的な「検索してから読む」パターンとは異なり、Agentic RAGでは、ツールや関数の呼び出し、構造化された出力を交えた反復的なLLM呼び出しが行われます。システムは結果を評価し、クエリを洗練し、必要に応じて追加のツールを呼び出し、満足のいく解決策が得られるまでこのサイクルを続けます。

## はじめに

このレッスンでは以下を学びます：

- **エージェンティックRAGを理解する:** 大規模言語モデル（LLM）が外部データソースから情報を取得しながら、自律的に次のステップを計画する新しいAIパラダイムについて学ぶ
- **反復的な「メーカー・チェッカー」スタイルを把握する:** ツールや関数呼び出し、構造化された出力を交えた反復的なLLM呼び出しのループを理解し、正確性の向上や不完全なクエリの処理方法を学ぶ
- **実用的な応用例を探る:** 正確性が最優先される環境、複雑なデータベースの操作、長時間のワークフローなど、Agentic RAGが活躍するシナリオを特定する

## 学習目標

このレッスンを修了すると、以下を理解し、実践できるようになります：

- **エージェンティックRAGの理解:** 大規模言語モデル（LLM）が外部データソースから情報を取得しながら、自律的に次のステップを計画する新しいAIパラダイムについて学ぶ
- **反復的な「メーカー・チェッカー」スタイル:** ツールや関数呼び出し、構造化された出力を交えた反復的なLLM呼び出しのループを把握し、不完全なクエリの処理や正確性の向上を目指す
- **推論プロセスの所有:** 問題へのアプローチを事前定義されたパスに頼らず、自律的に決定するシステムの能力を理解する
- **ワークフロー:** エージェンティックモデルが市場動向レポートを取得し、競合他社のデータを特定し、内部販売指標を相関させ、結果を統合し、戦略を評価する流れを理解する
- **反復ループ、ツール統合、メモリ:** システムが反復的なインタラクションパターンに依存し、ステップ間で状態とメモリを維持し、繰り返しを避けながら情報に基づいた意思決定を行う方法を学ぶ
- **失敗モードの処理と自己修正:** クエリの再試行や診断ツールの使用、人間の監視に頼るなど、システムの強力な自己修正メカニズムを探る
- **エージェンシーの限界:** ドメイン固有の自律性、インフラストラクチャへの依存、ガードレールの尊重に焦点を当て、Agentic RAGの限界を理解する
- **実用的な使用例と価値:** 正確性が重要な環境、複雑なデータベース操作、長時間のワークフローなど、Agentic RAGが活躍するシナリオを特定する
- **ガバナンス、透明性、信頼:** 説明可能な推論、バイアス制御、人間による監視の重要性を学ぶ

## Agentic RAGとは？

エージェンティック・リトリーバル・オーグメンテッド・ジェネレーション（Agentic RAG）は、大規模言語モデル（LLM）が外部ソースから情報を取得しながら、自律的に次のステップを計画する新たなAIパラダイムです。従来の静的な「検索してから読む」パターンとは異なり、Agentic RAGでは、ツールや関数呼び出し、構造化された出力を交えた反復的なLLM呼び出しが行われます。システムは結果を評価し、クエリを洗練し、必要に応じて追加のツールを呼び出し、満足のいく解決策が得られるまでこのサイクルを続けます。この反復的な「メーカー・チェッカー」スタイルは、正確性を向上させ、不完全なクエリを処理し、高品質な結果を保証します。

システムは推論プロセスを積極的に管理し、失敗したクエリを書き直し、異なる検索方法を選択し、複数のツール（Azure AI Searchのベクター検索、SQLデータベース、カスタムAPIなど）を統合して最終的な回答を完成させます。エージェンティックシステムの際立った特徴は、推論プロセスを自ら管理できる点です。従来のRAG実装では事前定義されたパスに依存しますが、エージェンティックシステムは、見つかった情報の質に基づいて次のステップの順序を自律的に決定します。

## エージェンティック・リトリーバル・オーグメンテッド・ジェネレーション（Agentic RAG）の定義

エージェンティック・リトリーバル・オーグメンテッド・ジェネレーション（Agentic RAG）は、LLMが外部データソースから情報を取得するだけでなく、自律的に次のステップを計画するAI開発の新しいパラダイムです。従来の静的な「検索してから読む」パターンや慎重にスクリプト化されたプロンプトシーケンスとは異なり、Agentic RAGは、ツールや関数呼び出し、構造化された出力を交えた反復的なLLM呼び出しのループを含みます。各ステップで、システムは得られた結果を評価し、クエリを洗練するかどうかを決定し、必要に応じて追加のツールを呼び出し、満足のいく解決策が得られるまでこのサイクルを続けます。

この反復的な「メーカー・チェッカー」スタイルの操作は、正確性を向上させ、構造化データベース（例：NL2SQL）に対する不完全なクエリを処理し、バランスの取れた高品質な結果を保証するよう設計されています。慎重に設計されたプロンプトチェーンにのみ依存するのではなく、システムは推論プロセスを積極的に管理します。失敗したクエリを書き直し、異なる検索方法を選択し、複数のツール（Azure AI Searchのベクター検索、SQLデータベース、カスタムAPIなど）を統合して最終的な回答を完成させます。これにより、複雑なオーケストレーションフレームワークの必要性がなくなります。代わりに、「LLM呼び出し → ツール使用 → LLM呼び出し → …」という比較的シンプルなループで洗練された、根拠のある出力を得ることができます。

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.2224925a913fb3439f518bda61a40096ddf6aa432a11c9b5bba8d0d625e47b79.ja.png)

## 推論プロセスの所有

システムが「エージェンティック」と見なされる際立った特徴は、推論プロセスを自ら管理できる能力にあります。従来のRAG実装では、モデルがどの情報をいつ取得するかを事前に定義されたチェーン・オブ・ソートに依存することが一般的です。しかし、本当にエージェンティックなシステムでは、問題へのアプローチを内部で決定します。それは単なるスクリプトの実行ではなく、見つかった情報の質に基づいて次のステップの順序を自律的に決定します。

たとえば、製品発売戦略を作成するよう求められた場合、エージェンティックモデルは以下を自律的に決定します：

1. Bing Web Groundingを使用して現在の市場動向レポートを取得する
2. Azure AI Searchを使用して関連する競合データを特定する
3. Azure SQL Databaseを用いて過去の内部販売指標を相関させる
4. Azure OpenAI Serviceを通じて統合された戦略を作成する
5. 戦略のギャップや矛盾を評価し、必要に応じて再度情報を取得する

これらすべてのステップ（クエリの洗練、情報源の選択、回答に「満足」するまでの反復）は、モデルが自ら決定するものであり、人間が事前にスクリプト化したものではありません。

## 反復ループ、ツール統合、メモリ

![Tool Integration Architecture](../../../translated_images/tool-integration.7b05a923e3278bf1fd2972faa228fb2ac725f166ed084362b031a24bffd26287.ja.png)

エージェンティックシステムは、ループ型のインタラクションパターンに依存しています：

- **初回呼び出し:** ユーザーの目的（ユーザープロンプト）がLLMに提示されます。
- **ツールの呼び出し:** モデルが不足している情報や曖昧な指示を特定した場合、ベクターデータベースクエリ（例：Azure AI Searchによるプライベートデータのハイブリッド検索）や構造化されたSQL呼び出しなど、ツールや検索方法を選択してさらなるコンテキストを収集します。
- **評価と洗練:** 返されたデータをレビューした後、モデルは情報が十分かどうかを判断します。不十分であれば、クエリを洗練し、別のツールを試すか、アプローチを調整します。
- **満足するまで繰り返す:** このサイクルは、モデルが十分な明確さと証拠を得て、最終的な合理的な回答を提供できると判断するまで続きます。
- **メモリと状態:** システムはステップ間で状態とメモリを維持するため、以前の試みとその結果を記憶し、繰り返しを避け、進行する中でより情報に基づいた意思決定を行います。

時間が経つにつれて、これにより進化する理解が生まれ、モデルは複雑なマルチステップタスクを人間が介入したりプロンプトを再形成したりする必要なく、効率的に処理することが可能になります。

## 失敗モードの処理と自己修正

エージェンティックRAGの自律性には、強力な自己修正メカニズムも含まれています。システムが行き詰まった場合（例：無関係なドキュメントを取得したり、不完全なクエリに遭遇したりした場合）、以下のアプローチを取ります：

- **反復と再クエリ:** 低価値の回答を返す代わりに、モデルは新しい検索戦略を試みたり、データベースクエリを書き直したり、代替データセットを調べたりします。
- **診断ツールの使用:** システムは、推論ステップをデバッグしたり、取得したデータの正確性を確認するための追加機能を呼び出す場合があります。Azure AI Tracingなどのツールは、堅牢な観測性と監視を可能にする重要な要素です。
- **人間の監視に頼る:** 高リスクまたは繰り返し失敗するシナリオでは、モデルは不確実性をフラグとして示し、人間の指導を求める場合があります。人間が修正フィードバックを提供した後、モデルはそのレッスンを今後のセッションに反映させることができます。

この反復的かつ動的なアプローチにより、モデルは継続的に改善し、単なる一度限りのシステムではなく、セッション中に失敗から学ぶことができるシステムとなります。

![Self Correction Mechanism](../../../translated_images/self-correction.3d42c31baf4a476bb89313cec58efb196b0e97959c04d7439cc23d27ef1242ac.ja.png)

## エージェンシーの限界

タスク内での自律性がある一方で、エージェンティックRAGは人工汎用知能（AGI）と同義ではありません。その「エージェンティック」な能力は、人間の開発者が提供したツール、データソース、ポリシーに制限されています。独自のツールを発明したり、設定されたドメインの境界を超えたりすることはできません。その代わり、手元のリソースを動的にオーケストレーションすることに長けています。

より高度なAI形式との主な違いは以下の通りです：

1. **ドメイン固有の自律性:** エージェンティックRAGシステムは、ユーザー定義の目標を達成することに焦点を当てており、クエリの書き換えやツールの選択などの戦略を用いて結果を向上させます。
2. **インフラストラクチャ依存:** システムの能力は、開発者によって統合されたツールとデータに依存しています。これらの境界を人間の介入なしに超えることはできません。
3. **ガードレールの尊重:** 倫理的ガイドライン、コンプライアンスルール、ビジネスポリシーは依然として非常に重要です。エージェントの自由度は常に安全対策と監視メカニズムによって制約されています（おそらく？）。

## 実用的な使用例と価値

エージェンティックRAGは、反復的な洗練と精度が求められるシナリオで活躍します：

1. **正確性が最優先される環境:** コンプライアンスチェック、規制分析、法的調査などでは、エージェンティックモデルが繰り返し事実を確認し、複数のソースを参照し、クエリを書き直して、徹底的に検証された回答を提供します。
2. **複雑なデータベース操作:** クエリが頻繁に失敗したり調整が必要となる構造化データを扱う際、Azure SQLやMicrosoft Fabric OneLakeを使用してクエリを自律的に洗練し、最終的な取得がユーザーの意図に一致するようにします。
3. **長時間のワークフロー:** 新しい情報が出てくるにつれて進化するセッションでは、エージェンティックRAGが継続的に新しいデータを取り込み、問題領域について学びながら戦略を変更します。

## ガバナンス、透明性、信頼

これらのシステムが推論においてより自律的になるにつれ、ガバナンスと透明性が重要になります：

- **説明可能な推論:** モデルは、作成したクエリ、参照したソース、結論に至るまでの推論ステップの監査トレイルを提供できます。Azure AI Content SafetyやAzure AI Tracing / GenAIOpsのようなツールは、透明性を維持し、リスクを軽減するのに役立ちます。
- **バイアス制御とバランスの取れた検索:** 開発者は、バランスの取れた代表的なデータソースが考慮されるように検索戦略を調整し、Azure Machine Learningを使用して出力を定期的に監査し、バイアスや偏ったパターンを検出します。
- **人間の監視とコンプライアンス:** 敏感なタスクでは、人間によるレビューが依然として不可欠です。エージェンティックRAGは、高リスクの意思決定において人間の判断を置き換えるものではなく、より徹底的に検証された選択肢を提供することでそれを補完します。

マルチステップ

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期すよう努めておりますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語で作成された原文が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤った解釈について、当社は一切の責任を負いません。