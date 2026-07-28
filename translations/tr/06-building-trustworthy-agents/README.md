[![Güvenilir AI Ajanları](../../../translated_images/tr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Bu dersin videosunu görüntülemek için yukarıdaki görsele tıklayın)_

# Güvenilir AI Ajanları İnşa Etmek

## Giriş

Bu ders aşağıdakileri kapsayacaktır:

- Güvenli ve etkili AI Ajanları nasıl inşa edilir ve dağıtılır
- AI Ajanlarını geliştirirken önemli güvenlik hususları.
- AI Ajanlarını geliştirirken veri ve kullanıcı gizliliğinin nasıl korunacağı.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra, şunları bileceksiniz:

- AI Ajanları oluştururken riskleri tanımlamak ve azaltmak.
- Verilerin ve erişimin doğru yönetilmesini sağlamak için güvenlik önlemleri uygulamak.
- Veri gizliliğini koruyan ve kaliteli bir kullanıcı deneyimi sunan AI Ajanları oluşturmak.

## Güvenlik

Öncelikle güvenli ajan uygulamaları inşa etmeye bakalım. Güvenlik, AI ajanının tasarlandığı şekilde çalışması demektir. Ajan uygulamaları geliştiricisi olarak, güvenliği maksimuma çıkarmak için yöntemlerimiz ve araçlarımız vardır:

### Bir Sistem Mesajı Çerçevesi Oluşturma

Eğer daha önce Büyük Dil Modelleri (LLM'ler) kullanarak bir AI uygulaması geliştirdiyseniz, sağlam bir sistem istemi veya sistem mesajı tasarlamanın önemini bilirsiniz. Bu istemler, LLM'nin kullanıcı ve veri ile nasıl etkileşim kuracağına dair meta kurallar, talimatlar ve rehberler oluşturur.

AI Ajanlar için sistem istemi daha da önemlidir çünkü AI Ajanların, tasarladığımız görevleri tamamlamak için çok spesifik talimatlara ihtiyacı vardır.

Ölçeklenebilir sistem istemleri oluşturmak için, uygulamamızdaki bir veya daha fazla ajanı oluşturmak amacıyla bir sistem mesajı çerçevesi kullanabiliriz:

![Bir Sistem Mesajı Çerçevesi Oluşturma](../../../translated_images/tr/system-message-framework.3a97368c92d11d68.webp)

#### Adım 1: Bir Meta Sistem Mesajı Oluşturun

Meta istem, oluşturduğumuz ajanlar için sistem istemleri üretmek amacıyla LLM tarafından kullanılacaktır. Bunu, gerektiğinde birden fazla ajanı verimli bir şekilde oluşturabilmek için şablon olarak tasarlarız.

İşte LLM'ye vereceğimiz bir meta sistem mesajı örneği:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Adım 2: Temel bir istem oluşturun

Sonraki adım, AI Ajanını tanımlayan temel bir istem oluşturmaktır. Ajanın rolünü, tamamlayacağı görevleri ve diğer sorumluluklarını dahil etmelisiniz.

İşte bir örnek:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Adım 3: Temel Sistem Mesajını LLM'ye Sağlayın

Şimdi, meta sistem mesajını sistem mesajı olarak verip temel sistem mesajımızla optimize edebiliriz.

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

Bu sistem mesajı çerçevesinin değeri, birden fazla ajan için sistem mesajları oluşturmayı kolaylaştırmak ve zamanla sistem mesajlarını iyileştirmektir. İlk seferde tüm kullanım durumunu kapsayan bir sistem mesajına sahip olmak nadirdir. Temel sistem mesajını değiştirip sistemi çalıştırarak küçük ayar ve iyileştirmeler yapabilmek, sonuçları karşılaştırmanızı ve değerlendirmenizi sağlar.

## Tehditleri Anlamak

Güvenilir AI ajanları oluşturmak için, AI ajanınıza yönelik riskleri ve tehditleri anlamak ve azaltmak önemlidir. AI ajanlarına yönelik farklı tehditlerin sadece bazılarına bakalım ve nasıl daha iyi planlama ve hazırlık yapabileceğinizi görelim.

![Tehditleri Anlamak](../../../translated_images/tr/understanding-threats.89edeada8a97fc0f.webp)

### Görev ve Talimat

**Açıklama:** Saldırganlar, AI ajanının talimatlarını veya hedeflerini istem yoluyla ya da girdileri manipüle ederek değiştirmeye çalışır.

**Azaltma**: AI ajanı tarafından işlenmeden önce potansiyel tehlikeli istemleri tespit etmek için doğrulama kontrolleri ve giriş filtreleri uygulayın. Bu saldırılar genellikle ajan ile sık etkileşim gerektirdiğinden, bir konuşmadaki tur sayısını sınırlamak bu tür saldırıları önlemenin bir yoludur.

### Kritik Sistemlere Erişim

**Açıklama:** Bir AI ajanı, hassas verileri saklayan sistem ve hizmetlere erişiyorsa, saldırganlar ajan ile bu hizmetler arasındaki iletişimi tehlikeye atabilir. Bunlar doğrudan saldırılar ya da ajan aracılığıyla bu sistemler hakkında bilgi edinmeye yönelik dolaylı girişimler olabilir.

**Azaltma:** AI ajanlarının bu tür saldırıları engellemek için sistemlere yalnızca gerektikçe erişimi olmalıdır. Ajan ile sistem arasındaki iletişim de güvenli olmalıdır. Kimlik doğrulama ve erişim kontrolü uygulamak bu bilgiyi korumanın başka bir yoludur.

### Kaynak ve Hizmet Aşırı Yüklemesi

**Açıklama:** AI ajanları görevleri tamamlamak için çeşitli araç ve hizmetlere erişebilir. Saldırganlar, AI Ajanı aracılığıyla bu hizmetlere yüksek talep göndererek sistem hatalarına veya yüksek maliyetlere yol açabilir.

**Azaltma:** Bir AI ajanının bir hizmete gönderebileceği istek sayısını sınırlayan politikalar uygulayın. Konuşmadaki tur sayısını ve AI ajanına yapılan istekleri sınırlamak bu tür saldırıları önlemenin başka bir yoludur.

### Bilgi Tabanı Zehirlenmesi

**Açıklama:** Bu tür saldırı doğrudan AI ajanını hedef almaz, ama AI ajanının kullanacağı bilgi tabanı ve diğer hizmetleri hedef alır. Bu, AI ajanının bir görevi tamamlamak için kullanacağı veriyi bozmak, yanlı veya istem dışı yanıtlar vermesine neden olabilir.

**Azaltma:** AI ajanının iş akışlarında kullanacağı veriyi düzenli olarak doğrulayın. Bu veriye erişimin güvenli olmasını ve yalnızca güvenilir kişiler tarafından değiştirilmesini sağlayarak bu tür saldırıları önleyin.

### Kademeli Hatalar

**Açıklama:** AI ajanları görevleri tamamlamak için çeşitli araçlara ve hizmetlere erişir. Saldırganlar tarafından neden olunan hatalar, AI ajanının bağlı olduğu diğer sistemlerin de arızalanmasına yol açabilir ve saldırı daha yaygın, teşhis edilmesi zor hale gelir.

**Azaltma**: Bunu önlemenin bir yolu, AI Ajanının sınırlı bir ortamda çalışmasıdır, örneğin görevleri Docker konteynerinde gerçekleştirmek, böylece doğrudan sistem saldırılarını engellemek. Belirli sistemler hata verdiğinde devreye giren yedek mekanizmalar ve yeniden deneme mantığı oluşturmak, daha büyük sistem arızalarını önlemenin başka yöntemleridir.

## İnsan Döngüde

Güvenilir AI Ajan sistemleri oluşturmanın başka etkili bir yolu da İnsan-döngüde yaklaşımını kullanmaktır. Bu, kullanıcıların çalıştırma sırasında ajanlara geri bildirim verebildiği bir akış yaratır. Kullanıcılar çoklu ajan sisteminde adeta ajan görevi görür ve çalışmayı onaylayıp sonlandırabilir.

![İnsan Döngüde](../../../translated_images/tr/human-in-the-loop.5f0068a678f62f4f.webp)

Bu kavramın nasıl uygulandığını göstermek için Microsoft Agent Framework kullanılarak hazırlanmış bir kod snippet'i:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# İnsan onaylı sağlayıcıyı oluştur
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# İnsan onayı adımıyla ajanı oluştur
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Kullanıcı yanıtı inceleyip onaylayabilir
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Sonuç

Güvenilir AI ajanları oluşturmak dikkatli tasarım, sağlam güvenlik önlemleri ve sürekli yineleme gerektirir. Yapılandırılmış meta istem sistemleri uygulayarak, potansiyel tehditleri anlayarak ve azaltma stratejileri uygulayarak geliştiriciler güvenli ve etkili AI ajanları yaratabilir. Ayrıca, insan-döngüde yaklaşımı dahil etmek, AI ajanlarının kullanıcı ihtiyaçları ile uyumlu kalmasını sağlarken riskleri en aza indirir. AI gelişmeye devam ettikçe güvenlik, gizlilik ve etik hususlarda proaktif duruş sürdürmek, AI destekli sistemlerde güven ve güvenilirliği pekiştirmenin anahtarı olacaktır.

## Kod Örnekleri

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Meta-istem sistem-mesaj çerçevesinin adım adım gösterimi.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Güvenilir ajanlar için ön-aksiyon onayı kapıları, risk derecelendirmesi ve denetim kaydı.

### Güvenilir AI Ajanları İnşa Etme hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanları ile ilgili sorularınızı sormak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) topluluğuna katılın.

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

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->