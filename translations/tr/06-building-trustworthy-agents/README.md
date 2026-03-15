[![Güvenilir AI Ajanları](../../../translated_images/tr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

# Güvenilir AI Ajanları Oluşturma

## Giriş

Bu ders şu konuları kapsayacaktır:

- Güvenli ve etkili AI Ajanları nasıl oluşturulur ve dağıtılır
- AI Ajanları geliştirilirken önemli güvenlik hususları
- AI Ajanları geliştirilirken veri ve kullanıcı gizliliğinin nasıl korunacağı

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra, şunları bileceksiniz:

- AI Ajanları oluştururken risklerin nasıl tanımlanacağı ve azaltılacağı
- Veri ve erişimin uygun şekilde yönetilmesini sağlamak için güvenlik önlemlerinin nasıl uygulanacağı
- Veri gizliliğini koruyan ve kaliteli kullanıcı deneyimi sunan AI Ajanları oluşturma

## Güvenlik

Öncelikle güvenli ajan uygulamaları oluşturmayı inceleyelim. Güvenlik, AI ajanının tasarlandığı şekilde çalışması demektir. Ajan uygulamaları geliştirenler olarak, güvenliği en üst düzeye çıkarmak için metotlar ve araçlar kullanırız:

### Bir Sistem Mesaj Çerçevesi Oluşturmak

Eğer bir AI uygulaması oluştururken Büyük Dil Modelleri (LLM) kullandıysanız, sağlam bir sistem istemi veya sistem mesajı tasarlamanın önemini bilirsiniz. Bu istemler, LLM'nin kullanıcı ve veriyle nasıl etkileşime gireceğine dair meta kurallar, talimatlar ve yönergeleri belirler.

AI Ajanları için sistem istemi daha da önemlidir çünkü AI Ajanlarının, onlara tasarladığımız görevleri tamamlamak için çok spesifik talimatlara ihtiyacı olacaktır.

Ölçeklenebilir sistem istemleri oluşturmak için, uygulamamızda bir veya daha fazla ajan oluşturmak üzere bir sistem mesaj çerçevesi kullanabiliriz:

![Bir Sistem Mesaj Çerçevesi Oluşturmak](../../../translated_images/tr/system-message-framework.3a97368c92d11d68.webp)

#### Adım 1: Bir Meta Sistem Mesajı Oluşturun

Meta istem, oluşturduğumuz ajanlar için sistem istemlerini oluşturmak üzere bir LLM tarafından kullanılacaktır. Bunu, ihtiyaç duyulursa birden fazla ajanı verimli şekilde oluşturabileceğimiz bir şablon olarak tasarlarız.

İşte LLM’ye vereceğimiz bir meta sistem mesajına örnek:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Adım 2: Temel bir istem oluşturun

Sonraki adım, AI Ajanını tanımlayan temel bir istem yaratmaktır. Ajanın rolünü, tamamlayacağı görevleri ve ajanla ilgili diğer sorumlulukları dahil etmelisiniz.

İşte bir örnek:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Adım 3: Temel Sistem Mesajını LLM'ye sağlayın

Şimdi bu sistem mesajını, meta sistem mesajını sistem mesajı olarak ve temel sistem mesajımızı sağlayarak optimize edebiliriz.

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

#### Adım 4: Yineleyin ve İyileştirin

Bu sistem mesaj çerçevesinin değeri, birden çok ajan için sistem mesajları oluşturmayı daha kolay ölçekleyebilmek ve zaman içinde sistem mesajlarınızı geliştirebilmektir. Tam kullanım durumunuz için ilk seferde çalışan bir sistem mesajına sahip olmak nadirdir. Temel sistem mesajında küçük değişiklikler yapıp sistemden geçirerek sonuçları karşılaştırmak ve değerlendirmek mümkün olacaktır.

## Tehditleri Anlamak

Güvenilir AI ajanları oluşturmak için, AI ajanınıza yönelik riskleri ve tehditleri anlamanız ve azaltmanız önemlidir. AI ajanlarına yönelik bazı farklı tehditlere ve bunlarla daha iyi nasıl planlama yapıp hazırlık yapılacağına bakalım.

![Tehditleri Anlamak](../../../translated_images/tr/understanding-threats.89edeada8a97fc0f.webp)

### Görev ve Talimat

**Açıklama:** Saldırganlar, istem veya girdi manipülasyonu yoluyla AI ajanının talimatlarını veya hedeflerini değiştirmeye çalışır.

**Azaltma:** Potansiyel tehlikeli istemleri AI Ajan işlenmeden önce tespit etmek için doğrulama kontrolleri ve girdi filtreleri uygulayın. Bu tür saldırılar genellikle ajanın sık etkileşim gerektirdiği için, konuşmadaki tur sayısını sınırlamak bu tür saldırıları önlemenin başka bir yoludur.

### Kritik Sistemlere Erişim

**Açıklama:** Bir AI ajanı, hassas verileri depolayan sistemlere ve hizmetlere erişime sahipse, saldırganlar ajan ile bu hizmetler arasındaki iletişimi tehlikeye atabilir. Bu doğrudan saldırılar veya ajan üzerinden bu sistemler hakkında bilgi edinme girişimleri olabilir.

**Azaltma:** Bu tür saldırıları önlemek için AI ajanlarının sistemlere sadece ihtiyaç bazında erişimi olmalıdır. Ajan ile sistem arasındaki iletişim de güvenli olmalıdır. Kimlik doğrulama ve erişim kontrolü uygulamak bu bilgileri korumanın başka bir yoludur.

### Kaynak ve Hizmet Aşırı Yüklenmesi

**Açıklama:** AI ajanları, görevleri yerine getirmek için farklı araçlara ve hizmetlere erişebilir. Saldırganlar, yüksek sayıda isteği AI Ajan aracılığıyla göndererek bu hizmetlere saldırabilir, bu da sistem arızalarına veya yüksek maliyetlere yol açabilir.

**Azaltma:** Bir AI ajanının bir hizmete yapabileceği istek sayısını sınırlayan politikalar uygulayın. Konuşma turu ve istek sayısını sınırlamak, bu tür saldırıları önlemenin başka bir yoludur.

### Bilgi Tabanının Zehirlenmesi

**Açıklama:** Bu tür saldırı, AI ajanını doğrudan hedef almaz, ancak AI ajanının kullanacağı bilgi tabanı ve diğer hizmetleri hedefler. Bu, AI ajanının görev tamamlamak için kullanacağı veri veya bilgiyi bozmak anlamına gelir, bu da kullanıcılara taraflı veya beklenmedik yanıtlar verilmesine yol açabilir.

**Azaltma:** AI ajanının iş akışlarında kullanılacak verinin düzenli olarak doğrulanmasını sağlayın. Bu verilere erişimin güvenli olduğundan ve sadece güvenilen kişilerce değiştirilebildiğinden emin olun, böylece bu tür saldırılardan kaçınılır.

### Zincirleme Hatalar

**Açıklama:** AI ajanları görevleri yerine getirmek için çeşitli araçlar ve hizmetlere erişir. Saldırganların neden olduğu hatalar, AI ajanının bağlı olduğu diğer sistemlerin arızalarına yol açabilir ve saldırının yaygınlaşmasına ve sorun çözümünün zorlaşmasına neden olur.

**Azaltma:** Bunu önlemek için AI Ajanının Docker konteyneri gibi izole bir ortamda çalıştırılması sağlanabilir ve doğrudan sistem saldırılarından korunabilir. Belirli sistemler hata verdiğinde devreye giren yedek mekanizmalar ve yeniden deneme mantığı oluşturmak, daha büyük sistem arızalarını önlemenin başka bir yoludur.

## İnsan-Döngüde

Güvenilir AI Ajan sistemleri oluşturmanın bir diğer etkili yolu İnsan-döngüde yaklaşımını kullanmaktır. Bu, kullanıcıların çalışma sırasında ajanlara geri bildirim verebildiği bir akış oluşturur. Kullanıcılar çok ajanlı sistemde birer ajan gibi davranarak çalışmayı onaylayabilir veya durdurabilir.

![Döngüde İnsan](../../../translated_images/tr/human-in-the-loop.5f0068a678f62f4f.webp)

Bu kavramın nasıl uygulandığını göstermek için Microsoft Agent Framework kullanılarak bir kod örneği:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# İnsan onaylı bir sağlayıcı oluştur
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# İnsan onay adımı ile ajan oluştur
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Kullanıcı yanıtı gözden geçirip onaylayabilir
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Sonuç

Güvenilir AI ajanları oluşturmak özenli tasarım, sağlam güvenlik önlemleri ve sürekli yineleme gerektirir. Yapılandırılmış meta istem sistemleri uygulayarak, potansiyel tehditleri anlayarak ve azaltma stratejileri uygulayarak geliştiriciler hem güvenli hem de etkili AI ajanları yaratabilir. Ayrıca, insan-döngüde yaklaşımını dahil etmek, AI ajanlarının kullanıcı ihtiyaçlarıyla uyumlu kalmasını ve risklerin minimize edilmesini sağlar. AI gelişmeye devam ederken, güvenlik, gizlilik ve etik hususlara proaktif yaklaşım sürdürmek, AI-merkezli sistemlerde güven oluşturmanın anahtarı olacaktır.

### Güvenilir AI Ajanları Oluşturma hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanlar sorularınızı yanıtlatmak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) topluluğuna katılabilirsiniz.

## Ek Kaynaklar

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Sorumlu AI genel bakışı</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Üretken AI modelleri ve AI uygulamalarının değerlendirilmesi</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Güvenlik sistem mesajları</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Risk Değerlendirme Şablonu</a>

## Önceki Ders

[Agentic RAG](../05-agentic-rag/README.md)

## Sonraki Ders

[Planlama Tasarım Deseni](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu tutulamayız.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->