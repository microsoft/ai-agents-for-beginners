<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "09e975d95b470ee45ab546c22ee35d33",
  "translation_date": "2025-03-28T11:28:06+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# 初心者向けAIエージェント - コース

![Generative AI For Beginners](../../translated_images/repo-thumbnail.fdd5f487bb7274d4a08459d76907ec4914de268c99637e9af082b1d3eb0730e2.ja.png)

## AIエージェントを構築するために必要な知識を学べる10のレッスン

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 言語サポート
[![English](https://img.shields.io/badge/English-brightgreen.svg?style=flat-square)](README.md)
[![Chinese Simplified](https://img.shields.io/badge/Chinese_Simplified-brightgreen.svg?style=flat-square)](../zh/README.md)
[![Chinese Traditional](https://img.shields.io/badge/Chinese_Traditional-brightgreen.svg?style=flat-square)](../tw/README.md)     
[![Chinese Hong Kong](https://img.shields.io/badge/Chinese_Hong_Kong-brightgreen.svg?style=flat-square)](../hk/README.md) 
[![French](https://img.shields.io/badge/French-brightgreen.svg?style=flat-square)](../fr/README.md)
[![Japanese](https://img.shields.io/badge/Japanese-brightgreen.svg?style=flat-square)](./README.md) 
[![Korean](https://img.shields.io/badge/Korean-brightgreen.svg?style=flat-square)](../ko/README.md)
[![Portuguese Brazilian](https://img.shields.io/badge/Portuguese_Brazilian-brightgreen.svg?style=flat-square)](../pt/README.md)
[![Spanish](https://img.shields.io/badge/Spanish-brightgreen.svg?style=flat-square)](../es/README.md)
[![German](https://img.shields.io/badge/German-brightgreen.svg?style=flat-square)](../de/README.md)  
[![Persian](https://img.shields.io/badge/Persian-brightgreen.svg?style=flat-square)](../fa/README.md) 
[![Polish](https://img.shields.io/badge/Polish-brightgreen.svg?style=flat-square)](../pl/README.md) 

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)


## 🌱 始めるにあたって

このコースは、AIエージェントを構築するための基礎を学べる10のレッスンで構成されています。それぞれのレッスンが個別のトピックを扱っているため、好きな場所から始めてください！

このコースは多言語対応しています。[利用可能な言語はこちら](../..)をご覧ください。

初めて生成AIモデルを使う方は、[初心者向け生成AIコース](https://aka.ms/genai-beginners)をご覧ください。このコースでは、生成AIを活用するための21のレッスンが含まれています。

このリポジトリを[スター（🌟）](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)し、[フォーク](https://github.com/microsoft/ai-agents-for-beginners/fork)してコードを実行するのを忘れないでください。

### 必要なもの

このコースの各レッスンにはコード例が含まれており、code_samplesフォルダに保存されています。このリポジトリを[フォーク](https://github.com/microsoft/ai-agents-for-beginners/fork)して、自分のコピーを作成してください。

これらの演習で使用されるコード例では、Azure AI FoundryやGitHub Model Catalogsを利用して言語モデルと対話します：

- [Github Models](https://aka.ms/ai-agents-beginners/github-models) - 無料 / 制限あり
- [Azure AI Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azureアカウントが必要

このコースでは、Microsoftが提供する以下のAIエージェントフレームワークやサービスも使用します：

- [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service)
- [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel)
- [AutoGen](https://aka.ms/ai-agents/autogen)

このコースのコードを実行する方法については、[Course Setup](./00-course-setup/README.md)をご覧ください。

## 🙏 ご協力いただけますか？

提案やスペルミス、コードのエラーを見つけましたか？[問題を提起する](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst)または[プルリクエストを作成する](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)ことでお知らせください。

AIエージェントの構築に行き詰まったり、質問がある場合は、[Azure AI Community Discord](https://discord.gg/kzRShWzttr)に参加してください。

## 📂 各レッスンに含まれる内容

- READMEに記載されたテキストレッスンと短い動画
- Azure AI FoundryおよびGithub Models（無料）をサポートするPythonコードサンプル
- 学習を継続するための追加リソースへのリンク

## 🗃️ レッスン

| **レッスン**                               | **テキスト＆コード**                               | **動画**                                                   | **追加学習**                                                                          |
|------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AIエージェントの概要と利用ケース            | [リンク](./01-intro-to-ai-agents/README.md)          | [動画](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AIエージェントフレームワークの探索          | [リンク](./02-explore-agentic-frameworks/README.md)  | [動画](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AIエージェント設計パターンの理解            | [リンク](./03-agentic-design-patterns/README.md)     | [動画](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ツール利用設計パターン                     | [リンク](./04-tool-use/README.md)                    | [動画](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| エージェントRAG                            | [リンク](./05-agentic-rag/README.md)                 | [動画](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 信頼できるAIエージェントの構築              | [リンク](./06-building-trustworthy-agents/README.md) | [動画](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 計画設計パターン                           | [リンク](./07-planning-design/README.md)             | [動画](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| マルチエージェント設計パターン              | [リンク](./08-multi-agent/README.md)                 | [動画](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| メタ認知デザインパターン             | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 本番環境でのAIエージェント           | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

## 🌐 多言語対応

| 言語                 | コード | 翻訳されたREADMEへのリンク                            | 最終更新日     |
|----------------------|------|---------------------------------------------------------|--------------|
| 中国語（簡体字）     | zh   | [中国語翻訳](../zh/README.md)               | 2025-03-24   |
| 中国語（繁体字）     | tw   | [中国語翻訳](../tw/README.md)               | 2025-02-13   |
| 中国語（香港）       | hk   | [中国語（香港）翻訳](../hk/README.md)       | 2025-02-13   |
| フランス語           | fr   | [フランス語翻訳](../fr/README.md)           | 2025-02-13   |
| 日本語               | ja   | [日本語翻訳](./README.md)               | 2025-02-13   |
| 韓国語               | ko   | [韓国語翻訳](../ko/README.md)               | 2025-02-13   |
| ポルトガル語         | pt   | [ポルトガル語翻訳](../pt/README.md)         | 2025-02-13   |
| スペイン語           | es   | [スペイン語翻訳](../es/README.md)           | 2025-02-13   |
| ドイツ語             | de   | [ドイツ語翻訳](../de/README.md)             | 2025-02-13   |
| ペルシャ語           | fa   | [ペルシャ語翻訳](../fa/README.md)           | 2025-03-26   |
| ポーランド語         | pl   | [ポーランド語翻訳](../pl/README.md)         | 2025-03-26   |

## 🎒 その他のコース

私たちのチームでは、他にもコースを提供しています！ぜひチェックしてください：

- [**NEW** 初心者向けの.NETを使用した生成AI](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [初心者向け生成AI](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向け機械学習](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けデータサイエンス](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けAI](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けサイバーセキュリティ](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [初心者向けWeb開発](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けIoT](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けXR開発](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [AIペアプログラミングのためのGitHub Copilotマスター](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [C#/.NET開発者向けGitHub Copilotマスター](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [自分で選ぶCopilotアドベンチャー](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

## 🌟 コミュニティへの感謝

Agentic RAGを示す重要なコードサンプルを提供してくれた [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) さんに感謝します。

## コントリビューション

このプロジェクトはコントリビューションと提案を歓迎します。ほとんどのコントリビューションには、Contributor License Agreement (CLA) に同意する必要があります。このCLAは、あなたがコントリビューションの権利を有し、実際にそれを提供する権利を持っていることを宣言するものです。詳細は <https://cla.opensource.microsoft.com> をご覧ください。

プルリクエストを送信すると、CLAボットが自動的にCLAを提供する必要があるかどうかを判断し、PRに適切な装飾（例: ステータスチェック、コメント）を行います。ボットの指示に従ってください。このプロセスは、CLAを使用するすべてのリポジトリで一度だけ行えば済みます。
このプロジェクトは [Microsoft オープンソース行動規範](https://opensource.microsoft.com/codeofconduct/) を採用しています。
詳細については [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) を参照するか、
追加の質問やコメントがある場合は [opencode@microsoft.com](mailto:opencode@microsoft.com) にお問い合わせください。

## 商標

このプロジェクトには、プロジェクト、製品、またはサービスに関する商標やロゴが含まれている場合があります。Microsoftの商標やロゴの使用許可は、
[Microsoft 商標およびブランド ガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) に従う必要があります。
このプロジェクトの改変版で Microsoft の商標やロゴを使用する場合、混乱を引き起こしたり、Microsoft のスポンサーシップを暗示したりしてはなりません。
第三者の商標やロゴの使用は、それぞれの第三者のポリシーに従う必要があります。

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の母国語による文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用に起因する誤解や誤認について、当社は責任を負いません。