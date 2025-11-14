<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T13:12:44+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "tr"
}
-->
[![Güvenilir AI Ajanları](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.tr.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

# Güvenilir AI Ajanları Oluşturma

## Giriş

Bu derste şunlar ele alınacaktır:

- Güvenli ve etkili AI Ajanları nasıl oluşturulur ve dağıtılır.
- AI Ajanları geliştirirken dikkate alınması gereken önemli güvenlik hususları.
- AI Ajanları geliştirirken veri ve kullanıcı gizliliğinin nasıl korunacağı.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları öğrenmiş olacaksınız:

- AI Ajanları oluştururken riskleri tanımlama ve azaltma.
- Verilerin ve erişimin doğru şekilde yönetilmesini sağlamak için güvenlik önlemleri uygulama.
- Veri gizliliğini koruyan ve kaliteli bir kullanıcı deneyimi sunan AI Ajanları oluşturma.

## Güvenlik

Öncelikle güvenli ajan uygulamaları oluşturmayı ele alalım. Güvenlik, AI ajanının tasarlandığı şekilde çalışması anlamına gelir. Ajan uygulamaları geliştiricileri olarak, güvenliği en üst düzeye çıkarmak için yöntemler ve araçlar kullanabiliriz:

### Sistem Mesajı Çerçevesi Oluşturma

Eğer daha önce Büyük Dil Modelleri (LLM'ler) kullanarak bir AI uygulaması geliştirdiyseniz, sağlam bir sistem istemi veya sistem mesajı tasarlamanın önemini bilirsiniz. Bu istemler, LLM'nin kullanıcı ve veri ile nasıl etkileşimde bulunacağını belirleyen meta kuralları, talimatları ve yönergeleri oluşturur.

AI Ajanları için sistem istemi daha da önemlidir çünkü AI Ajanlarının tasarladığımız görevleri tamamlamak için oldukça spesifik talimatlara ihtiyacı olacaktır.

Ölçeklenebilir sistem istemleri oluşturmak için uygulamamızda bir veya daha fazla ajan oluşturmak üzere bir sistem mesajı çerçevesi kullanabiliriz:

![Sistem Mesajı Çerçevesi Oluşturma](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.tr.png)

#### Adım 1: Meta Sistem Mesajı Oluşturma

Meta istem, oluşturduğumuz ajanlar için sistem istemlerini üretmek üzere bir LLM tarafından kullanılacaktır. Bunu bir şablon olarak tasarlarız, böylece gerektiğinde birden fazla ajanı verimli bir şekilde oluşturabiliriz.

İşte LLM'ye vereceğimiz bir meta sistem mesajı örneği:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Adım 2: Temel Bir İstem Oluşturma

Bir sonraki adım, AI Ajanını tanımlamak için temel bir istem oluşturmaktır. Bu istemde ajanın rolü, tamamlayacağı görevler ve diğer sorumluluklar yer almalıdır.

İşte bir örnek:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Adım 3: Temel Sistem Mesajını LLM'ye Sağlama

Şimdi meta sistem mesajını sistem mesajı olarak ve temel sistem mesajımızı sağlayarak bu sistem mesajını optimize edebiliriz.

Bu, AI ajanlarımızı yönlendirmek için daha iyi tasarlanmış bir sistem mesajı üretecektir:

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

#### Adım 4: Yineleme ve İyileştirme

Bu sistem mesajı çerçevesinin değeri, birden fazla ajan için sistem mesajları oluşturmayı kolaylaştırmak ve sistem mesajlarınızı zamanla iyileştirmektir. Tam kullanım senaryonuz için ilk seferde çalışan bir sistem mesajına sahip olmanız nadirdir. Temel sistem mesajını değiştirerek ve sistemi çalıştırarak küçük ayarlamalar ve iyileştirmeler yapabilmek, sonuçları karşılaştırmanıza ve değerlendirmenize olanak tanır.

## Tehditleri Anlama

Güvenilir AI ajanları oluşturmak için, AI ajanınıza yönelik riskleri ve tehditleri anlamak ve azaltmak önemlidir. AI ajanlarına yönelik farklı tehditlerden bazılarına ve bunlara karşı nasıl daha iyi plan yapabileceğinize bakalım.

![Tehditleri Anlama](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.tr.png)

### Görev ve Talimat

**Açıklama:** Saldırganlar, istemler veya girdileri manipüle ederek AI ajanının talimatlarını veya hedeflerini değiştirmeye çalışır.

**Azaltma:** AI Ajanı tarafından işlenmeden önce potansiyel olarak tehlikeli istemleri tespit etmek için doğrulama kontrolleri ve giriş filtreleri uygulayın. Bu tür saldırılar genellikle ajanla sık etkileşim gerektirdiğinden, bir konuşmadaki dönüş sayısını sınırlamak bu tür saldırıları önlemenin başka bir yoludur.

### Kritik Sistemlere Erişim

**Açıklama:** Bir AI ajanı hassas verileri depolayan sistemlere ve hizmetlere erişime sahipse, saldırganlar ajan ile bu hizmetler arasındaki iletişimi tehlikeye atabilir. Bunlar doğrudan saldırılar veya ajan aracılığıyla bu sistemler hakkında bilgi edinmeye yönelik dolaylı girişimler olabilir.

**Azaltma:** AI ajanlarının bu tür saldırıları önlemek için yalnızca gerektiğinde sistemlere erişimi olmalıdır. Ajan ile sistem arasındaki iletişim de güvenli olmalıdır. Kimlik doğrulama ve erişim kontrolü uygulamak, bu bilgiyi korumanın başka bir yoludur.

### Kaynak ve Hizmet Aşırı Yüklenmesi

**Açıklama:** AI ajanları görevleri tamamlamak için farklı araçlara ve hizmetlere erişebilir. Saldırganlar, AI ajanı aracılığıyla bu hizmetlere yüksek hacimli istekler göndererek bu hizmetlere saldırabilir, bu da sistem hatalarına veya yüksek maliyetlere yol açabilir.

**Azaltma:** Bir AI ajanının bir hizmete yapabileceği istek sayısını sınırlamak için politikalar uygulayın. AI ajanınıza yapılan konuşma dönüşlerini ve istekleri sınırlamak, bu tür saldırıları önlemenin başka bir yoludur.

### Bilgi Tabanı Zehirlenmesi

**Açıklama:** Bu tür saldırılar doğrudan AI ajanını hedef almaz, ancak AI ajanının kullanacağı bilgi tabanını ve diğer hizmetleri hedef alır. Bu, AI ajanının bir görevi tamamlamak için kullanacağı verileri veya bilgileri bozmayı içerebilir, bu da kullanıcıya önyargılı veya istenmeyen yanıtlar verilmesine neden olabilir.

**Azaltma:** AI ajanının iş akışlarında kullanacağı verilerin düzenli doğrulamasını yapın. Bu verilere erişimin güvenli olmasını ve yalnızca güvenilir kişiler tarafından değiştirilmesini sağlayarak bu tür saldırılardan kaçının.

### Zincirleme Hatalar

**Açıklama:** AI ajanları görevleri tamamlamak için çeşitli araçlara ve hizmetlere erişir. Saldırganlar tarafından neden olunan hatalar, AI ajanının bağlı olduğu diğer sistemlerin başarısız olmasına yol açabilir, bu da saldırının daha yaygın hale gelmesini ve sorun giderilmesini zorlaştırabilir.

**Azaltma:** Bunu önlemenin bir yöntemi, AI Ajanının Docker konteyneri gibi sınırlı bir ortamda çalışmasını sağlayarak doğrudan sistem saldırılarını önlemektir. Belirli sistemler bir hata yanıtı verdiğinde geri dönüş mekanizmaları ve yeniden deneme mantığı oluşturmak, daha büyük sistem hatalarını önlemenin başka bir yoludur.

## İnsan Döngüsü İçinde

Güvenilir AI Ajanı sistemleri oluşturmanın bir başka etkili yolu, İnsan Döngüsü İçinde (Human-in-the-loop) yaklaşımını kullanmaktır. Bu, kullanıcıların çalıştırma sırasında ajanlara geri bildirim sağlayabileceği bir akış oluşturur. Kullanıcılar, çoklu ajan sisteminde ajanlar gibi hareket eder ve çalıştırma sürecini onaylayarak veya sonlandırarak katkıda bulunur.

![İnsan Döngüsü İçinde](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.tr.png)

İşte bu konseptin AutoGen kullanılarak nasıl uygulandığını gösteren bir kod parçası:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Sonuç

Güvenilir AI ajanları oluşturmak, dikkatli tasarım, sağlam güvenlik önlemleri ve sürekli yineleme gerektirir. Yapılandırılmış meta istem sistemlerini uygulayarak, potansiyel tehditleri anlayarak ve azaltma stratejileri uygulayarak, geliştiriciler hem güvenli hem de etkili AI ajanları oluşturabilir. Ayrıca, insan döngüsü içinde bir yaklaşım benimsemek, AI ajanlarının kullanıcı ihtiyaçlarına uygun kalmasını sağlarken riskleri en aza indirir. AI gelişmeye devam ettikçe, güvenlik, gizlilik ve etik hususlara yönelik proaktif bir duruş sergilemek, AI odaklı sistemlerde güven ve güvenilirliği artırmanın anahtarı olacaktır.

### Güvenilir AI Ajanları Oluşturma Hakkında Daha Fazla Sorunuz mu Var?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) topluluğuna katılarak diğer öğrenicilerle tanışabilir, ofis saatlerine katılabilir ve AI Ajanları ile ilgili sorularınıza yanıt alabilirsiniz.

## Ek Kaynaklar

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Sorumlu AI genel bakış</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Üretken AI modelleri ve AI uygulamalarının değerlendirilmesi</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Güvenlik sistem mesajları</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Risk Değerlendirme Şablonu</a>

## Önceki Ders

[Agentic RAG](../05-agentic-rag/README.md)

## Sonraki Ders

[Planlama Tasarım Deseni](../07-planning-design/README.md)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.