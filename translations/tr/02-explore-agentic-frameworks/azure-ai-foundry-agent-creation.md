# Microsoft Foundry Ajan Hizmeti Geliştirme

Bu egzersizde, [Microsoft Foundry portalı](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) içindeki Microsoft Foundry Ajan Hizmeti araçlarını kullanarak Uçuş Rezervasyonu için bir ajan oluşturacaksınız. Ajan, kullanıcılarla etkileşim kurabilecek ve uçuşlar hakkında bilgi sağlayabilecektir.

## Ön koşullar

Bu egzersizi tamamlamak için aşağıdaki gereksinimlere ihtiyacınız vardır:
1. Aktif aboneliğe sahip bir Azure hesabı. [Ücretsiz bir hesap oluşturun](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Bir Microsoft Foundry hub’ı oluşturmak için izinlere sahip olmanız ya da sizin için birinin oluşturmuş olması gerekir.
    - Rolünüz Katkıda Bulunan veya Sahip ise, bu öğreticideki adımları takip edebilirsiniz.

## Microsoft Foundry hub oluşturun

> **Not:** Microsoft Foundry önceden Azure AI Studio olarak bilinmekteydi.

1. Microsoft Foundry hub oluşturmak için [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) blog yazısındaki kılavuzları takip edin.
2. Projeniz oluşturulduğunda, görüntülenen ipuçlarını kapatın ve Microsoft Foundry portalındaki proje sayfasını inceleyin; sayfa aşağıdaki görsele benzer olmalıdır:

    ![Microsoft Foundry Project](../../../translated_images/tr/azure-ai-foundry.88d0c35298348c2f.webp)

## Bir model dağıtın

1. Projenizin sol panelinde, **Varlıklarım** bölümünde, **Modeller + uç noktalar** sayfasını seçin.
2. **Modeller + uç noktalar** sayfasında, **Model dağıtımları** sekmesinde, **+ Model dağıt** menüsünden **Temel modeli dağıt** seçeneğini seçin.
3. Listeden `gpt-5-mini` modelini arayın, sonra seçin ve onaylayın.

    > **Not**: TPM'yi düşürmek, kullandığınız abonelikteki kota aşımını önlemeye yardımcı olur.

    ![Model Deployed](../../../translated_images/tr/model-deployment.3749c53fb81e18fd.webp)

## Bir ajan oluşturun

Model dağıttıktan sonra bir ajan oluşturabilirsiniz. Ajan, kullanıcılarla etkileşim kurmak için kullanılan konuşma tabanlı bir yapay zeka modelidir.

1. Projenizin sol panelinde, **Oluştur & Özelleştir** bölümünde, **Ajanlar** sayfasını seçin.
2. Yeni bir ajan oluşturmak için **+ Ajan oluştur** butonuna tıklayın. **Ajan Kurulumu** iletişim kutusunda:
    - Ajana bir ad girin, örneğin `FlightAgent`.
    - Daha önce oluşturduğunuz `gpt-5-mini` model dağıtımının seçili olduğundan emin olun.
    - Ajana uyulacak talimatları **Talimatlar** bölümüne girin. İşte bir örnek:
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> Daha detaylı bir talimat için, [bu depoyu](https://github.com/ShivamGoyal03/RoamMind) inceleyebilirsiniz.
    
> Ayrıca, ajanın kullanıcı isteklerine göre daha fazla bilgi sunmasını ve otomatik görevler yapmasını sağlamak için **Bilgi Tabanı** ve **Eylemler** ekleyebilirsiniz. Bu egzersizde bu adımlar atlanabilir.
    
![Agent Setup](../../../translated_images/tr/agent-setup.9bbb8755bf5df672.webp)

3. Yeni bir çoklu yapay zekâ ajanı oluşturmak için sadece **Yeni Ajan** butonuna tıklayın. Oluşturulan ajan Ajanlar sayfasında görünecektir.


## Ajanı test edin

Ajanı oluşturduktan sonra, Microsoft Foundry portalının oyun alanında kullanıcı sorgularına nasıl yanıt verdiğini test edebilirsiniz.

1. Ajanınız için **Kurulum** panelinin üstünde, **Oyun alanında dene** seçeneğini seçin.
2. **Oyun alanı** panelinde, sohbet penceresine sorgular yazarak ajanla etkileşimde bulunabilirsiniz. Örneğin, ajan’dan 28’inde Seattle’dan New York’a uçuş aramasını isteyebilirsiniz.

    > **Not**: Bu egzersizde gerçek zamanlı veri kullanılmadığından ajan doğru yanıtlar vermeyebilir. Amaç, ajanın verilen talimatlara dayanarak kullanıcı sorgularını anlayıp yanıt verme yeteneğini test etmektir.

    ![Agent Playground](../../../translated_images/tr/agent-playground.dc146586de715010.webp)

3. Ajanı test ettikten sonra, daha fazla niyet, eğitim verisi ve eylem ekleyerek yeteneklerini geliştirebilirsiniz.

## Kaynakları temizleyin

Ajanı test etmeyi bitirdiğinizde, ek maliyetlerden kaçınmak için silebilirsiniz.
1. [Azure portalını](https://portal.azure.com) açın ve bu egzersizde kullandığınız hub kaynaklarını dağıttığınız kaynak grubunun içeriğine bakın.
2. Araç çubuğunda, **Kaynak grubunu sil** seçeneğini seçin.
3. Kaynak grubu adını girin ve silmek istediğinizi onaylayın.

## Kaynaklar

- [Microsoft Foundry dokümantasyonu](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portalı](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry ile Başlarken](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure’daki AI ajanlarının Temelleri](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->