<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f112154d137460ec15a92bf3eec99df",
  "translation_date": "2026-01-01T10:12:33+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# 初心者向け AI エージェント - コース

![生成AI入門](../../translated_images/ja/repo-thumbnailv2.06f4a48036fde647.webp)

## AIエージェントを構築し始めるために必要なすべてを教えるコース

[![GitHub ライセンス](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub コントリビューター](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub の Issue](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub プルリクエスト](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRを歓迎](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 マルチ言語サポート

#### GitHub Actions でサポート（自動化・常に最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[アラビア語](../ar/README.md) | [ベンガル語](../bn/README.md) | [ブルガリア語](../bg/README.md) | [ビルマ語（ミャンマー）](../my/README.md) | [中国語（簡体字）](../zh/README.md) | [中国語（繁体字、香港）](../hk/README.md) | [中国語（繁体字、マカオ）](../mo/README.md) | [中国語（繁体字、台湾）](../tw/README.md) | [クロアチア語](../hr/README.md) | [チェコ語](../cs/README.md) | [デンマーク語](../da/README.md) | [オランダ語](../nl/README.md) | [エストニア語](../et/README.md) | [フィンランド語](../fi/README.md) | [フランス語](../fr/README.md) | [ドイツ語](../de/README.md) | [ギリシャ語](../el/README.md) | [ヘブライ語](../he/README.md) | [ヒンディー語](../hi/README.md) | [ハンガリー語](../hu/README.md) | [インドネシア語](../id/README.md) | [イタリア語](../it/README.md) | [日本語](./README.md) | [カンナダ語](../kn/README.md) | [韓国語](../ko/README.md) | [リトアニア語](../lt/README.md) | [マレー語](../ms/README.md) | [マラヤーラム語](../ml/README.md) | [マラーティー語](../mr/README.md) | [ネパール語](../ne/README.md) | [ナイジェリア・ピジン語](../pcm/README.md) | [ノルウェー語](../no/README.md) | [ペルシア語（ファールシー）](../fa/README.md) | [ポーランド語](../pl/README.md) | [ポルトガル語（ブラジル）](../br/README.md) | [ポルトガル語（ポルトガル）](../pt/README.md) | [パンジャブ語（グルムキー）](../pa/README.md) | [ルーマニア語](../ro/README.md) | [ロシア語](../ru/README.md) | [セルビア語（キリル文字）](../sr/README.md) | [スロバキア語](../sk/README.md) | [スロベニア語](../sl/README.md) | [スペイン語](../es/README.md) | [スワヒリ語](../sw/README.md) | [スウェーデン語](../sv/README.md) | [タガログ語（フィリピン）](../tl/README.md) | [タミル語](../ta/README.md) | [テルグ語](../te/README.md) | [タイ語](../th/README.md) | [トルコ語](../tr/README.md) | [ウクライナ語](../uk/README.md) | [ウルドゥー語](../ur/README.md) | [ベトナム語](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**追加の翻訳を希望する場合、サポートされている言語は[こちら](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)に記載されています**

[![GitHub ウォッチャー](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub フォーク](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub スター](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry の Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 はじめに

このコースは、AIエージェント構築の基本を扱うレッスンで構成されています。各レッスンはそれぞれのトピックを扱うため、お好きなところから始めてください！

このコースはマルチ言語対応です。利用可能な言語は[こちら](../..)をご覧ください。 

生成AIモデルでの開発が初めての場合は、[生成AI入門](https://aka.ms/genai-beginners)コースをご覧ください。本コースにはGenAIを使った構築に関する21のレッスンが含まれています。

コードを実行するために、このリポジトリに[スター（🌟）を付ける](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)と[フォークする](https://github.com/microsoft/ai-agents-for-beginners/fork)ことをお忘れなく。

### 他の学習者と交流し、質問に答えを得る

AIエージェントの構築で行き詰まったり質問がある場合は、専用のDiscordチャンネル（[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)）に参加してください。

### 必要なもの

このコースの各レッスンにはコード例が含まれており、code_samplesフォルダーにあります。自身のコピーを作成するには[このリポジトリをフォーク](https://github.com/microsoft/ai-agents-for-beginners/fork)してください。  

これらの演習のコード例は、言語モデルとやり取りするために Azure AI Foundry と GitHub Model Catalogs を利用します:

- [GitHubモデル](https://aka.ms/ai-agents-beginners/github-models) - 無料 / 制限あり
- [Azure AI Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure アカウントが必要

このコースでは、Microsoft の以下のAIエージェントフレームワークとサービスも使用します:

- [Microsoft Agent Framework (MAF) - 新登場!](https://aka.ms/ai-agents-beginners/agent-framewrok)
- [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service)
- [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel)
- [AutoGen](https://aka.ms/ai-agents/autogen)


For more information on running the code for this course, go to the [コースセットアップ](./00-course-setup/README.md).

## 🙏 手伝いたいですか？

提案やスペル、コードの誤りを見つけましたか？[Issue を作成する](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst)か、[プルリクエストを作成する](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 各レッスンには以下が含まれます

- README にある文章によるレッスンと短いビデオ
- Azure AI Foundry と GitHub Models（無料）をサポートする Python コードサンプル
- 学習を続けるための追加リソースへのリンク


## 🗃️ レッスン

| **レッスン**                                   | **テキスト & コード**                                    | **ビデオ**                                                  | **追加学習**                                                                     |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AIエージェントとユースケース入門       | [リンク](./01-intro-to-ai-agents/README.md)          | [ビデオ](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AIエージェントフレームワークの探求              | [リンク](./02-explore-agentic-frameworks/README.md)  | [ビデオ](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AIエージェント設計パターンの理解     | [リンク](./03-agentic-design-patterns/README.md)     | [ビデオ](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ツール利用の設計パターン                      | [リンク](./04-tool-use/README.md)                    | [ビデオ](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| エージェンティックRAG                                  | [リンク](./05-agentic-rag/README.md)                 | [ビデオ](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 信頼できるAIエージェントの構築               | [リンク](./06-building-trustworthy-agents/README.md) | [ビデオ](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 計画の設計パターン                      | [リンク](./07-planning-design/README.md)             | [ビデオ](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| マルチエージェント設計パターン                   | [リンク](./08-multi-agent/README.md)                 | [ビデオ](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| メタ認知設計パターン                 | [リンク](./09-metacognition/README.md)               | [ビデオ](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 本番運用のAIエージェント                      | [リンク](./10-ai-agents-production/README.md)        | [ビデオ](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| エージェンティックプロトコルの使用 (MCP、A2A、NLWeb) | [リンク](./11-agentic-protocols/README.md)           | [ビデオ](https://youtu.be/X-Dh9R3Opn8)                                 | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AIエージェントのためのコンテキストエンジニアリング            | [リンク](./12-context-engineering/README.md)         | [ビデオ](https://youtu.be/F5zqRV7gEag)                                 | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| エージェンティックメモリの管理                      | [リンク](./13-agent-memory/README.md)     |      [ビデオ](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| Microsoft Agent Framework の探索                         | [リンク](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| コンピュータ利用エージェント (CUA) の構築           | 近日公開                            |                                                            |                                                                                        |
| スケーラブルなエージェントのデプロイ                    | 近日公開                            |                                                            |                                                                                        |
| ローカルAIエージェントの作成                     | 近日公開                               |                                                            |                                                                                        |
| AIエージェントのセキュリティ                           | 近日公開                               |                                                            |                                                                                        |

## 🎒 その他のコース

私たちのチームは他にもコースを制作しています！ぜひご覧ください：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j（初心者向け）](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js（初心者向け）](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / エージェント
[![AZD（初心者向け）](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI（初心者向け）](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP（初心者向け）](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AIエージェント（初心者向け）](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 生成AIシリーズ
[![生成AI（初心者向け）](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![生成AI（.NET）](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![生成AI（Java）](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![生成AI（JavaScript）](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### コア学習
[![機械学習（初心者向け）](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![データサイエンス（初心者向け）](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI（初心者向け）](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![サイバーセキュリティ（初心者向け）](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web開発（初心者向け）](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT（初心者向け）](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR開発（初心者向け）](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilotシリーズ
[![AIペアプログラミング向け Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET向け Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilotアドベンチャー](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 コミュニティへの感謝

Agentic RAG を示す重要なコードサンプルを提供してくれた [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) に感謝します。 

## 貢献

このプロジェクトは貢献や提案を歓迎します。 ほとんどの貢献には、あなたが貢献物を使用する権利を有し、実際に当社にその権利を付与することを宣言する Contributor License Agreement (CLA) に同意することが必要です。詳細は <https://cla.opensource.microsoft.com> をご覧ください。

プルリクエストを送信すると、CLAボットが自動的にCLAの提供が必要かどうかを判断し、PRに適切な注記（例：ステータスチェック、コメント）を行います。ボットの指示に従ってください。この手続きは、当社のCLAを使用するすべてのリポジトリに対して一度だけ行えば十分です。

このプロジェクトは [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) を採用しています。詳細は [行動規範 FAQ](https://opensource.microsoft.com/codeofconduct/faq/) を参照するか、追加の質問やコメントがある場合は [opencode@microsoft.com](mailto:opencode@microsoft.com) にご連絡ください。

## 商標

このプロジェクトには、プロジェクト、製品、またはサービスの商標やロゴが含まれている場合があります。Microsoft の商標またはロゴの許可された使用は、[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) に従う必要があります。本プロジェクトの改変版で Microsoft の商標やロゴを使用する場合は、混乱を招いたり Microsoft の後援を示唆したりしてはなりません。第三者の商標やロゴの使用は、当該第三者の方針に従うものとします。

## ヘルプを得る


AIアプリの構築で行き詰まったり質問がある場合は、参加してください：

[![Microsoft Foundry の Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

製品に関するフィードバックやビルド中のエラーがある場合は、次を訪問してください：

[![Microsoft Foundry 開発者フォーラム](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責事項：
この文書は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されました。正確性には努めていますが、自動翻訳には誤りや不正確さが含まれる可能性があることにご留意ください。原文（原語の文書）を正式な出典としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用に起因して生じる誤解や誤った解釈について、当方は責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->