<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e02a1254e28f559a2d7276b5e53ca504",
  "translation_date": "2025-05-21T09:31:29+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# 初心者向けAIエージェント - コース

![Generative AI For Beginners](../../images/repo-thumbnail.png)

## AIエージェント構築の基礎を学べる11のレッスン

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
[![Hindi](https://img.shields.io/badge/Hindi-brightgreen.svg?style=flat-square)](../hi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)


## 🌱 はじめに

このコースはAIエージェント構築の基本を学べる11のレッスンで構成されています。各レッスンは独立したテーマなので、好きなところから始めてください！

このコースは多言語対応しています。対応言語は[こちら](../..)からご覧いただけます。

もしGenerative AIモデルを使った開発が初めてなら、21のレッスンでGenAI構築を学べる[Generative AI For Beginners](https://aka.ms/genai-beginners)コースもチェックしてください。

このリポジトリを[スター(🌟)する](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)ことと、[フォークして](https://github.com/microsoft/ai-agents-for-beginners/fork)コードを実行することを忘れずに。

### 必要なもの

このコースの各レッスンにはコード例が含まれており、code_samplesフォルダーにあります。自分のコピーを作るには[リポジトリをフォーク](https://github.com/microsoft/ai-agents-for-beginners/fork)してください。

これらの演習で使われているコード例は、Azure AI FoundryとGitHub Model Catalogsを利用して言語モデルとやり取りしています：

- [Github Models](https://aka.ms/ai-agents-beginners/github-models) - 無料／制限あり
- [Azure AI Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azureアカウント必須

このコースでは、Microsoftの以下のAIエージェントフレームワークやサービスも使用しています：
- [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service)
- [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel)
- [AutoGen](https://aka.ms/ai-agents/autogen)

このコースのコード実行に関する詳細は、[Course Setup](./00-course-setup/README.md)をご覧ください。

## 🙏 ご協力いただけますか？

提案やスペルミス、コードの誤りを見つけた場合は、[Issueを報告](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst)するか、[プルリクエストを作成](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)してください。

AIエージェントの構築で行き詰まったり質問がある場合は、[Azure AI Foundry Community Discord](https://discord.gg/kzRShWzttr)にご参加ください。

製品に関するフィードバックやエラーについては、[Azure AI Foundry Developer Forum](https://aka.ms/azureaifoundry/forum)をご利用ください。

## 📂 各レッスンに含まれるもの

- READMEにあるテキストレッスンと短い動画
- Azure AI FoundryおよびGithub ModelsをサポートするPythonコードサンプル（無料）
- 学習を続けるための追加リソースへのリンク

## 🗃️ レッスン一覧

| **レッスン**                             | **テキスト＆コード**                                | **動画**                                                    | **追加学習**                                                                            |
|----------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AIエージェント入門とユースケース       | [リンク](./01-intro-to-ai-agents/README.md)          | [動画](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)    | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AIエージェントフレームワークの探求     | [リンク](./02-explore-agentic-frameworks/README.md)  | [動画](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)    | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AIエージェント設計パターンの理解       | [リンク](./03-agentic-design-patterns/README.md)     | [動画](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)    | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ツール利用設計パターン                 | [リンク](./04-tool-use/README.md)                    | [動画](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)    | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Agentic RAG                            | [リンク](./05-agentic-rag/README.md)                 | [動画](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)    | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 信頼できるAIエージェントの構築         | [リンク](./06-building-trustworthy-agents/README.md) | [動画](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK)    | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 計画設計パターン                       | [リンク](./07-planning-design/README.md)             | [動画](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)    | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| マルチエージェントデザインパターン               | [Link](./08-multi-agent/README.md)                 | [Video](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| メタ認知デザインパターン                         | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| プロダクションにおけるAIエージェント             | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| MCPを使ったAIエージェント                         | [Link](./11-mcp/README.md)                         |                                                            | [Link](https://aka.ms/mcp-for-beginners)                                               |

### 🌐 多言語対応

#### GitHub Actionによるサポート（自動化＆常に最新）

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Persian (Farsi)](../fa/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](./README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Polish](../pl/README.md)

## 🎒 その他のコース

私たちのチームは他にもさまざまなコースを制作しています！ぜひご覧ください：

- [**新着** Model Context Protocol (MCP) 入門](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
- [.NETを使った初心者向け生成AI](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [初心者向け生成AI](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向け機械学習](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けデータサイエンス](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けAI](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けサイバーセキュリティ](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [初心者向けWeb開発](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けIoT](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けXR開発](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [AIペアプログラミングのためのGitHub Copilotマスターガイド](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [C#/.NET開発者のためのGitHub Copilotマスターガイド](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [自分だけのCopilotアドベンチャーを選ぼう](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

## 🌟 コミュニティへの感謝

Agentic RAGを示す重要なコードサンプルを提供してくださった[Shivam Goyal](https://www.linkedin.com/in/shivam2003/)に感謝します。

## 貢献について

このプロジェクトは貢献や提案を歓迎します。ほとんどの貢献には、貢献物の使用権を実際に持ち、当社に許諾する権利があることを宣言するContributor License Agreement（CLA）への同意が必要です。詳細は<https://cla.opensource.microsoft.com>をご覧ください。

プルリクエストを提出すると、CLAボットが自動的にCLAの提出が必要かどうかを判断し、PRに適切な装飾（例：ステータスチェック、コメント）を行います。ボットの指示に従うだけで、当社のCLAを使用するすべてのリポジトリで一度だけ行えば済みます。

このプロジェクトは[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)を採用しています。詳細は[Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)をご覧いただくか、ご質問やご意見があれば[opencode@microsoft.com](mailto:opencode@microsoft.com)までお問い合わせください。

## 商標について

このプロジェクトには、プロジェクト、製品、サービスの商標やロゴが含まれている場合があります。Microsoftの商標やロゴの正当な使用は、[Microsoftの商標およびブランドガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)に従う必要があります。本プロジェクトの修正版でMicrosoftの商標やロゴを使用する場合、混乱を招いたりMicrosoftの後援を示唆したりしてはなりません。第三者の商標やロゴの使用は、該当する第三者のポリシーに従います。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。正式な情報源としては、原文の原語版を参照してください。重要な情報については、専門の人間翻訳をご利用いただくことを推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。