# AIエージェント初心者向けコース

![AIエージェント初心者向け](../../translated_images/ja/repo-thumbnailv2.06f4a48036fde647.webp)

## AIエージェント構築を始めるために必要なすべてを教えるコース

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 多言語対応

#### GitHubアクションによるサポート（自動かつ常に最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](./README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ローカルにクローンしたいですか？**
>
> このリポジトリには50以上の言語翻訳が含まれているため、ダウンロードサイズが大幅に増加します。翻訳を含めずにクローンする場合はスパースチェックアウトを使用してください。
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> これにより、コースを完了するために必要なすべてをはるかに高速なダウンロードで取得できます。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**もし追加の翻訳言語のサポートを希望する場合は[こちら](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)でご確認ください。**

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 はじめに

本コースはAIエージェント構築の基礎をカバーするレッスンがあります。各レッスンはそれぞれのトピックを扱っているので、お好きなところから始めてください！

本コースは多言語対応です。対応言語の一覧は[こちら](#-multi-language-support)をご覧ください。

もしジェネレーティブAIモデルでの構築が初めての場合は、21のレッスンでGenAI構築を学べる[Generative AI For Beginners](https://aka.ms/genai-beginners)コースもご確認ください。

[このリポジトリにスター（🌟）を付ける](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)ことと、[フォークする](https://github.com/microsoft/ai-agents-for-beginners/fork)ことを忘れずに、コードを動かしてみてください。

### 他の学習者と出会い、質問に答えてもらう

AIエージェント構築で行き詰まったり質問がある場合は、[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)内の専用Discordチャンネルに参加してください。

### 必要なもの

本コースの各レッスンにはコード例があり、code_samplesフォルダにあります。ご自身のコピーを作成するには[このリポジトリをフォーク](https://github.com/microsoft/ai-agents-for-beginners/fork)してください。

これらの演習でのコード例は、Microsoft Agent Framework と Azure AI Foundry Agent Service V2 を使っています：

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azureアカウントが必要です

本コースはMicrosoftの以下のAIエージェントフレームワークとサービスを使用しています：

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

一部コード例は、大規模コンテキストモデル（最大204Kトークン）を提供する[MiniMax](https://platform.minimaxi.com/)など、OpenAI互換の代替プロバイダーもサポートしています。設定の詳細は[コースセットアップ](./00-course-setup/README.md)をご覧ください。

本コースのコード実行に関する詳細は[コースセットアップ](./00-course-setup/README.md)をご参照ください。

## 🙏 ご協力ください

提案やスペル、コードの誤りを見つけた場合は[Issueを投稿](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst)するか、[プルリクエストを作成](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)してください。



## 📂 各レッスンに含まれるもの

- READMEと短い動画によるテキストレッスン
- Microsoft Agent Framework と Azure AI Foundryを用いたPythonコードサンプル
- 学習を続けるための追加リソースへのリンク


## 🗃️ レッスン

| <strong>レッスン</strong>                                  | **テキスト & コード**                               | <strong>動画</strong>                                                   | <strong>追加学習</strong>                                                                           |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AIエージェントとエージェントユースケース入門 | [リンク](./01-intro-to-ai-agents/README.md)          | [動画](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)   | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AIエージェントフレームワークの探求           | [リンク](./02-explore-agentic-frameworks/README.md)  | [動画](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)   | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AIエージェントデザインパターンの理解         | [リンク](./03-agentic-design-patterns/README.md)     | [動画](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)   | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ツール使用デザインパターン                    | [リンク](./04-tool-use/README.md)                    | [動画](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)   | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| エージェントRAG                               | [リンク](./05-agentic-rag/README.md)                 | [動画](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)   | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 信頼できるAIエージェントの構築                 | [リンク](./06-building-trustworthy-agents/README.md) | [動画](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK )  | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 計画デザインパターン                          | [リンク](./07-planning-design/README.md)             | [動画](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)   | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| マルチエージェントデザインパターン             | [リンク](./08-multi-agent/README.md)                 | [動画](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)   | [リンク](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| メタ認知デザインパターン                         | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| プロダクションにおけるAIエージェント             | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| エージェンティックプロトコルの使用 (MCP、A2A、およびNLWeb) | [Link](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AIエージェントのためのコンテキストエンジニアリング     | [Link](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| エージェンティックメモリの管理                    | [Link](./13-agent-memory/README.md)     |      [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| Microsoft Agent Frameworkの探索                      | [Link](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| コンピュータ使用エージェント（CUA）の構築            | [Link](./15-browser-use/README.md)     |                                                            | [Link](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| スケーラブルエージェントの展開                      | 近日公開                            |                                                            |                                                                                        |
| ローカルAIエージェントの作成                       | 近日公開                               |                                                            |                                                                                        |
| AIエージェントのセキュリティ                       | 近日公開                               |                                                            |                                                                                        |

## 🎒 その他のコース

私たちのチームは他のコースも制作しています！ぜひご覧ください：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ジェネレーティブAIシリーズ
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### コアラーニング
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### コパイロットシリーズ
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 コミュニティへの感謝

エージェンティックRAGを示す重要なコードサンプルを提供してくれた [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) に感謝します。

## 貢献について

このプロジェクトは貢献や提案を歓迎します。ほとんどの貢献には、あなたが貢献物の権利を有し、実際に使用許諾を当社に提供することを宣言する貢献者ライセンス契約（CLA）への同意が必要です。詳細については <https://cla.opensource.microsoft.com> をご覧ください。

プルリクエストを提出すると、CLAボットが自動的にCLAの提出の必要性を判定し、PRに適切な装飾（例: ステータスチェック、コメント）を行います。ボットの指示に従ってください。この手続きは、当社のCLAを使用するすべてのリポジトリで1回だけ行えば十分です。

本プロジェクトは[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)を採用しています。
詳細は[行動規範FAQ](https://opensource.microsoft.com/codeofconduct/faq/)をご覧いただくか、ご質問やコメントは[opencode@microsoft.com](mailto:opencode@microsoft.com)までお問い合わせください。

## 商標について

このプロジェクトにはプロジェクト、製品、サービスの商標やロゴが含まれる場合があります。Microsoftの商標やロゴの正当な使用は、[Microsoftの商標・ブランドガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)に従う必要があります。
Microsoftの商標またはロゴを修正したバージョンに使用する場合、混乱を引き起こしたりMicrosoftのスポンサーシップを示唆したりしてはなりません。
サードパーティの商標やロゴの使用は、それらのサードパーティの方針に従います。

## サポートを受けるには

AIアプリの構築に行き詰まったり質問がある場合は、以下に参加してください：

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

製品のフィードバックや構築中のエラーについては、以下をご利用ください：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご承知おきください。原文のネイティブ言語での文書が正式な情報源と見なされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->