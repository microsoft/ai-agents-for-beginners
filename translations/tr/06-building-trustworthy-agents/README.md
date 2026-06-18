[![Güvenilir AI Ajanları](../../../translated_images/tr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

# Güvenilir AI Ajanları Oluşturma

## Giriş

Bu ders şunları kapsayacaktır:

- Güvenli ve etkili AI Ajanları nasıl oluşturulur ve dağıtılır.
- AI Ajanları geliştirirken önemli güvenlik hususları.
- AI Ajanları geliştirirken veri ve kullanıcı gizliliği nasıl korunur.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları bileceksiniz:

- AI Ajanları oluştururken riskleri tanımlama ve azaltma.
- Verilerin ve erişimin uygun şekilde yönetilmesini sağlamak için güvenlik önlemleri uygulama.
- Veri gizliliğini koruyan ve kaliteli kullanıcı deneyimi sunan AI Ajanları oluşturma.

## Güvenlik

Öncelikle güvenli ajan uygulamaları oluşturmayı inceleyelim. Güvenlik, AI ajanının tasarlandığı şekilde çalışması demektir. Ajan uygulamaları geliştiricileri olarak güvenliği en üst düzeye çıkarmak için yöntemlerimiz ve araçlarımız vardır:

### Sistem Mesajı Çerçevesi Oluşturma

Eğer daha önce Büyük Dil Modelleri (LLM'ler) kullanarak bir AI uygulaması geliştirdiyseniz, sağlam bir sistem istemi veya sistem mesajı tasarlamanın önemini bilirsiniz. Bu istemler, LLM'nin kullanıcı ve verilerle nasıl etkileşimde bulunacağını belirleyen meta kurallar, talimatlar ve yönergeleri oluşturur.

AI Ajanları için, sistem mesajı daha da önemlidir çünkü AI Ajanlarının, onlar için tasarladığımız görevleri tamamlayabilmek için çok spesifik talimatlara ihtiyacı olacaktır.

Ölçeklenebilir sistem istemleri oluşturmak için, uygulamamızda bir veya daha fazla ajan için sistem mesajı çerçevesi kullanabiliriz:

![Sistem Mesajı Çerçevesi Oluşturma](../../../translated_images/tr/system-message-framework.3a97368c92d11d68.webp)

#### Adım 1: Meta Sistem Mesajı Oluşturun

Meta istem, oluşturduğumuz ajanlar için sistem istemlerini üretmek üzere bir LLM tarafından kullanılacaktır. Eğer gerekirse birden fazla ajanı verimli şekilde oluşturabilmek için bunu bir şablon olarak tasarlarız.

LLM'ye vereceğimiz bir meta sistem mesajı örneği:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Adım 2: Temel bir istem oluşturun

Sonraki adım, AI Ajanını tanımlayan temel bir istem oluşturmaktır. Burada ajanın rolünü, tamamlayacağı görevleri ve diğer sorumluluklarını dahil etmelisiniz.

Bir örnek:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Adım 3: Temel Sistem Mesajını LLM'ye Verin

Şimdi bu sistem mesajını optimize edebiliriz; meta sistem mesajını sistem mesajı olarak ve temel sistem mesajımızı sağlayarak.

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

#### Adım 4: Tekrarlayın ve Geliştirin

Bu sistem mesajı çerçevesinin değeri, birçok ajandan sistem mesajları oluşturmayı ölçeklendirmek ve sistem mesajlarınızı zamanla geliştirmek olanağı sağlamasıdır. Kullanım durumunuz için tam olarak işe yarayan bir sistem mesajına ilk defada sahip olmak nadirdir. Temel sistem mesajı değiştirip sistemi yeniden çalıştırarak küçük ayarlamalar ve iyileştirmeler yapabilmek, son sonuçları karşılaştırıp değerlendirmenizi sağlar.

## Tehditleri Anlamak

Güvenilir AI ajanları oluşturmak için, AI ajanınıza yönelik riskleri ve tehditleri anlamak ve azaltmak önemlidir. AI ajanlarına yönelik bazı farklı tehditlere bakalım ve bunlara nasıl daha iyi planlama ve hazırlık yapabileceğinize değinelim.

![Tehditleri Anlamak](../../../translated_images/tr/understanding-threats.89edeada8a97fc0f.webp)

### Görev ve Talimat

**Açıklama:** Saldırganlar, AI ajanının talimatlarını veya hedeflerini istem veya girdi manipülasyonu yoluyla değiştirmeye çalışır.

**Azaltma:** Tehlikeli olabilecek istemlerin AI Ajanı tarafından işlenmeden önce tespit edilmesi için doğrulama kontrolleri ve girdi filtreleri uygulatın. Bu tür saldırılar genellikle ajana sık sık etkileşim gerektirdiğinden, sohbet turu sayısını sınırlamak da bu saldırıların önlenmesine yardımcı olur.

### Kritik Sistemlere Erişim

**Açıklama:** AI ajanının hassas veriler barındıran sistem ve hizmetlere erişimi varsa, saldırganlar ajan ve bu hizmetler arasındaki iletişimi bozabilir. Bu, doğrudan saldırılar veya agent üzerinden sistemler hakkında bilgi edinmeye yönelik dolaylı girişimler olabilir.

**Azaltma:** AI ajanlarının sisteme yalnızca ihtiyaç duyulduğunda erişimi olmalıdır. Ajan ile sistem arasındaki iletişim güvenli olmalıdır. Kimlik doğrulama ve erişim kontrolü uygulamak da bu bilgileri korumak için başka bir yöntemdir.

### Kaynak ve Hizmet Aşırı Yüklenmesi

**Açıklama:** AI ajanları görevleri tamamlamak için farklı araçlara ve hizmetlere erişebilir. Saldırganlar, AI Ajanı aracılığıyla yüksek hacimli istekler göndererek bu hizmetlere saldırabilir, bu da sistem hatalarına veya yüksek maliyetlere yol açabilir.

**Azaltma:** Bir AI ajanının bir hizmete yapabileceği istek sayısını sınırlamak için politikalar uygulayın. AI ajanınıza yapılan konuşma turu ve istek sayısının sınırlandırılması da bu tür saldırıların önüne geçmek için başka bir yoldur.

### Bilgi Tabanı Zehirlenmesi

**Açıklama:** Bu saldırı türü doğrudan AI ajanını hedef almaz, ancak AI ajanının görevleri tamamlamak için kullanacağı bilgi tabanı ve diğer hizmetleri hedefler. Bu, AI ajanının kullanacağı verilerin bozulması veya değiştirilmesini içerebilir ve sonuçta kullanıcıya önyargılı ya da istenmeyen yanıtlar dönebilir.

**Azaltma:** AI ajanının iş akışlarında kullanacağı verinin düzenli olarak doğruluğunu kontrol edin. Bu verilere erişimin güvenli olduğunu ve yalnızca güvenilir kişiler tarafından değiştirilebildiğini sağlayın.

### Zincirleme Hatalar

**Açıklama:** AI ajanları görevleri tamamlamak için çeşitli araçlara ve hizmetlere erişir. Saldırganların neden olduğu hatalar, AI ajanının bağlı olduğu diğer sistemlerin başarısız olmasına yol açabilir; bu da saldırının daha yaygın ve giderilmesinin zor olmasına neden olabilir.

**Azaltma:** AI Ajanını sınırlı bir ortamda çalıştırmak (örneğin, görevleri bir Docker konteynerinde gerçekleştirmek) doğrudan sistem saldırılarını önleyebilir. Ayrıca, belirli sistemler hata yanıtı verdiğinde yedek mekanizmalar ve yeniden deneme mantığı kurmak daha büyük sistem hatalarının önüne geçer.

## İnsan Döngüsünde (Human-in-the-Loop)

Güvenilir AI Ajan sistemleri oluşturmanın bir diğer etkili yolu insan döngüsünü kullanmaktır. Bu, kullanıcıların çalıştırma sırasında Ajana geri bildirim verebilmesini sağlayan bir akış oluşturur. Kullanıcılar, çoklu ajan sisteminde ajan gibi hareket eder ve çalıştırılan sürecin onayını verir veya sonlandırır.

![İnsan Döngüsü](../../../translated_images/tr/human-in-the-loop.5f0068a678f62f4f.webp)

Microsoft Agent Framework kullanarak bu konseptin nasıl uygulandığını gösteren bir kod parçası:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# İnsan onayının dahil edildiği sağlayıcıyı oluştur
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# İnsan onay adımı ile ajanı oluştur
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

Güvenilir AI ajanları oluşturmak dikkatli tasarım, sağlam güvenlik önlemleri ve sürekli iyileştirme gerektirir. Yapılandırılmış meta istem sistemleri uygulayarak, olası tehditleri anlayarak ve azaltma stratejileri uygulayarak geliştiriciler güvenli ve etkili AI ajanları yaratabilirler. Ayrıca insan döngüsü yaklaşımını dahil etmek, AI ajanlarının kullanıcı ihtiyaçları ile uyumlu kalmasını ve risklerin azaltılmasını sağlar. AI geliştikçe güvenlik, gizlilik ve etik hususlarda proaktif bir tutum sürdürmek, AI destekli sistemlerde güvenilirlik ve güven tesis etmenin anahtarı olacaktır.

## Kod Örnekleri

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Meta-istem sistem-mesaj çerçevesinin adım adım gösterimi.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Güvenilir ajanlar için ön işlem onay kapıları, risk sınıflandırması ve denetim kaydı.

### Güvenilir AI Ajanları Oluşturma ile İlgili Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanlarınızla ilgili sorularınızı sormak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)'a katılın.

## Ek Kaynaklar

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Sorumlu AI genel bakışı</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Yapay üretici AI modelleri ve AI uygulamaları değerlendirmesi</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Güvenlik sistem mesajları</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Risk Değerlendirme Şablonu</a>

## Önceki Ders

[Agentic RAG](../05-agentic-rag/README.md)

## Sonraki Ders

[Planlama Tasarım Deseni](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->