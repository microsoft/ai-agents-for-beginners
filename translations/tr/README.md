# Başlangıç Seviyesi AI Ajanları - Bir Kurs

![Başlangıç Seviyesi AI Ajanları](../../translated_images/tr/repo-thumbnailv2.06f4a48036fde647.webp)

## AI Ajanları oluşturmaya başlamak için bilmeniz gereken her şeyi öğreten bir kurs

[![GitHub lisansı](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub katkıda bulunanlar](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub sorunları](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub çekme talepleri](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PR'lar Hoş Geldiniz](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 Çok Dilli Destek

#### GitHub Action ile Desteklenmektedir (Otomatik & Her Zaman Güncel)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](./README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Yerel olarak Klonlamayı mı Tercih Ediyorsunuz?**
>
> Bu depo, indirme boyutunu önemli ölçüde artıran 50'den fazla dil çevirisi içerir. Çeviriler olmadan klonlamak için sparse checkout kullanın:
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
> Bu, kursu tamamlamak için ihtiyacınız olan her şeyi çok daha hızlı bir indirme ile size sağlar.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ek dil desteği için talebiniz varsa, desteklenen diller [burada](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) listelenmiştir**

[![GitHub izleyiciler](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Kullanıcı)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub çatalları](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub yıldızları](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Yıldız)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 Başlarken

Bu kurs, AI Ajanları oluşturmanın temellerini kapsayan derslere sahiptir. Her ders kendi konusunu işler, bu yüzden istediğiniz yerden başlayabilirsiniz!

Bu kurs için çoklu dil desteği vardır. Mevcut diller için [buradan](#-multi-language-support) göz atın.

Eğer Generatif AI modelleriyle ilk defa çalışıyorsanız, GenAI ile oluşturmayı içeren 21 ders içeren [Gençler için Generatif AI](https://aka.ms/genai-beginners) kursumuza göz atın.

Kodu çalıştırmak için bu repoya [yıldız (🌟) vermeyi](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ve [forklamayı](https://github.com/microsoft/ai-agents-for-beginners/fork) unutmayın.

### Diğer Öğrenenlerle Tanışın, Sorularınıza Cevap Alın

Takılırsanız veya AI Ajanları oluşturmaya dair sorularınız olursa, [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) içindeki özel Discord Kanalımıza katılın.

### İhtiyacınız Olanlar

Kursun her dersi, kod örnekleri içerir ve bu örnekler code_samples klasöründe bulunabilir. Kendi kopyanızı oluşturmak için [repoyu fork](https://github.com/microsoft/ai-agents-for-beginners/fork) edebilirsiniz.

Bu alıştırmalardaki kod örnekleri, Microsoft Agent Framework ile Azure AI Foundry Agent Service V2 kullanır:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure Hesabı Gereklidir

Bu kurs Microsoft'tan aşağıdaki AI Ajan framework'leri ve servislerini kullanır:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

Bazı kod örnekleri ayrıca, büyük bağlam modelleri (204K token'a kadar) sunan [MiniMax](https://platform.minimaxi.com/) gibi alternatif OpenAI uyumlu sağlayıcıları destekler. Kurulum ayrıntıları için [Kurs Kurulumu](./00-course-setup/README.md) bölümüne bakın.

Bu kursun kodlarını çalıştırmak hakkında daha fazla bilgi için [Kurs Kurulumu](./00-course-setup/README.md) sayfasına gidin.

## 🙏 Yardımcı olmak ister misiniz?

Önerileriniz veya yazım ya da kod hatalarını bulduysanız, [issue açın](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) ya da [pull request oluşturun](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 Her derste şunlar vardır

- README içinde yazılı ders ve kısa bir video
- Microsoft Agent Framework ile Azure AI Foundry kullanarak Python kod örnekleri
- Öğrenmeye devam etmek için ekstra kaynak bağlantıları


## 🗃️ Dersler

| **Ders**                                   | **Metin & Kod**                                    | **Video**                                                  | **Ekstra Öğrenim**                                                                     |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AI Ajanlarına Giriş ve Ajan Kullanım Durumları       | [Bağlantı](./01-intro-to-ai-agents/README.md)          | [Video](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [Bağlantı](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI Ajanik Framework'lerini Keşfetmek              | [Bağlantı](./02-explore-agentic-frameworks/README.md)  | [Video](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [Bağlantı](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI Ajanik Tasarım Kalıplarını Anlamak     | [Bağlantı](./03-agentic-design-patterns/README.md)     | [Video](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [Bağlantı](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Araç Kullanımı Tasarım Kalıbı                      | [Bağlantı](./04-tool-use/README.md)                    | [Video](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [Bağlantı](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Ajanik RAG                                  | [Bağlantı](./05-agentic-rag/README.md)                 | [Video](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [Bağlantı](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Güvenilir AI Ajanları Oluşturmak               | [Bağlantı](./06-building-trustworthy-agents/README.md) | [Video](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [Bağlantı](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Planlama Tasarım Kalıbı                      | [Bağlantı](./07-planning-design/README.md)             | [Video](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [Bağlantı](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Çoklu Ajan Tasarım Kalıbı                   | [Bağlantı](./08-multi-agent/README.md)                 | [Video](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [Bağlantı](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| MetaBiliş Tasarım Deseni                      | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Üretimde Yapay Zeka Ajanları                  | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Ajanik Protokollerin Kullanımı (MCP, A2A ve NLWeb) | [Link](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Yapay Zeka Ajanları için Bağlam Mühendisliği  | [Link](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Ajanik Belleği Yönetmek                        | [Link](./13-agent-memory/README.md)                 | [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)            |                                                                                        |
| Microsoft Agent Framework'ünü Keşfetmek        | [Link](./14-microsoft-agent-framework/README.md)   |                                                            |                                                                                        |
| Bilgisayar Kullanım Ajanları (CUA) Oluşturmak | [Link](./15-browser-use/README.md)                  |                                                            | [Link](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| Ölçeklenebilir Ajanları Dağıtma                | Yakında Geliyor                                    |                                                            |                                                                                        |
| Yerel Yapay Zeka Ajanları Oluşturmak           | Yakında Geliyor                                    |                                                            |                                                                                        |
| Yapay Zeka Ajanlarını Güvence Almak             | Yakında Geliyor                                    |                                                            |                                                                                        |

## 🎒 Diğer Kurslar

Ekibimiz diğer kurslar üretiyor! Göz atın:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![Yeni Başlayanlar için LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![Yeni Başlayanlar için LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![Yeni Başlayanlar için LangChain](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Ajanlar
[![Yeni Başlayanlar için AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için Yapay Zeka Ajanları](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Üretken Yapay Zeka Serisi
[![Yeni Başlayanlar için Üretken Yapay Zeka](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Üretken Yapay Zeka (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Üretken Yapay Zeka (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Üretken Yapay Zeka (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Temel Öğrenme
[![Yeni Başlayanlar için ML](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için Veri Bilimi](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için Yapay Zeka](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için Siber Güvenlik](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Yeni Başlayanlar için Web Geliştirme](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için XR Geliştirme](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Serisi
[![Yapay Zeka Eşli Programlama için Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET için Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Macerası](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 Topluluk Teşekkürü

Agentik RAG'ı gösteren önemli kod örnekleri için [Shivam Goyal](https://www.linkedin.com/in/shivam2003/)'a teşekkürler.

## Katkıda Bulunma

Bu proje katkılara ve önerilere açıktır. Çoğu katkı, katkınızı kullanma hakkını verdiğinizi ve gerçekten haklarınızı bize devrettiğinizi beyan eden bir Katkıda Bulunma Lisans Anlaşması'na (CLA) katılmanızı gerektirir. Ayrıntılar için <https://cla.opensource.microsoft.com> adresini ziyaret edin.

Pull request gönderdiğinizde, bir CLA botu sizin CLA sağlamanız gerekip gerekmediğini otomatik olarak belirleyecek ve PR'ı uygun şekilde süsleyecektir (örneğin, durum kontrolü, yorum). Botun verdiği talimatları takip etmeniz yeterlidir. CLA'yı kullanan tüm repolarda bunu yalnızca bir kez yapmanız gerekir.

Bu proje [Microsoft Açık Kaynak Davranış Kuralları](https://opensource.microsoft.com/codeofconduct/) benimsenmiştir.
Daha fazla bilgi için [Davranış Kuralları SSS](https://opensource.microsoft.com/codeofconduct/faq/) sayfasına bakabilir veya ek sorularınız veya yorumlarınız için [opencode@microsoft.com](mailto:opencode@microsoft.com) adresiyle iletişime geçebilirsiniz.

## Ticari Markalar

Bu proje, projeler, ürünler veya hizmetler için ticari markalar veya logolar içerebilir. Microsoft ticari markalarının veya logolarının yetkili kullanımı, [Microsoft'un Ticari Marka ve Marka Yönergeleri](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) uyarınca olmalı ve bunlara uyulmalıdır.
Microsoft ticari marka veya logolarının bu projenin değiştirilmiş sürümlerinde kullanılması karışıklığa yol açmamalı veya Microsoft sponsorluğunu ima etmemelidir.
Üçüncü taraf ticari markalarının veya logolarının kullanımı, ilgili üçüncü tarafların politikalarına tabidir.

## Yardım Alma

Takıldığınızda veya yapay zeka uygulamaları geliştirmekle ilgili sorularınız olduğunda katılın:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Ürün geri bildirimi veya geliştirme sırasında hatalar için ziyaret edin:

[![Microsoft Foundry Geliştirici Forumu](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->