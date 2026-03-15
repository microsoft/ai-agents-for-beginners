# Github MCP Server Örneği

## Açıklama

Bu, Microsoft Reactor aracılığıyla düzenlenen AI Agents Hackathon için oluşturulmuş bir demoydu.

Bu araç, bir kullanıcının Github depolarına dayanarak hackathon projeleri önermek için kullanılır. Bu şu şekilde yapılır:

1. **Github Agent** - Github MCP Server'ı kullanarak depoları ve bu depolara ait bilgileri almak.
2. **Hackathon Agent** - Github Agent'ten alınan verileri kullanır ve projelere, kullanıcının kullandığı dillere ve AI Agents hackathonunun proje kategorilerine dayanarak yaratıcı hackathon proje fikirleri üretir.
3. **Events Agent** - Hackathon agentinin önerilerine dayanarak, Events Agent AI Agent Hackathon serisinden ilgili etkinlikleri önerir.

## Kodu Çalıştırma 

### Ortam Değişkenleri

Bu demo Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server ve Azure AI Search kullanır.

Bu araçları kullanmak için uygun ortam değişkenlerinin ayarlandığından emin olun:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit Sunucusunu Çalıştırma

MCP sunucusuna bağlanmak için bu demo, sohbet arayüzü olarak Chainlit kullanır. 

Sunucuyu çalıştırmak için terminalinizde aşağıdaki komutu kullanın:

```bash
chainlit run app.py -w
```

Bu, Chainlit sunucunuzu `localhost:8000` üzerinde başlatmalı ve ayrıca Azure AI Search İndeksinizi `event-descriptions.md` içeriği ile doldurmalıdır. 

## MCP Sunucusuna Bağlanma

Github MCP Server'a bağlanmak için, sohbet kutusunun altındaki "plug" simgesini seçin:

![MCP Bağlantısı](../../../../../translated_images/tr/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Oradan, Github MCP Sunucusuna bağlanma komutunu eklemek için "Connect an MCP"e tıklayabilirsiniz:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" ifadesini gerçek Personal Access Token'ınız ile değiştirin. 

Bağlandıktan sonra, bağlı olduğunu doğrulamak için plug simgesinin yanında (1) görmelisiniz. Eğer görmüyorsanız, chainlit sunucusunu `chainlit run app.py -w` ile yeniden başlatmayı deneyin.

## Demoyu Kullanma 

Hackathon projeleri önermeye yönelik ajan iş akışını başlatmak için şu tür bir mesaj yazabilirsiniz: 

"Github kullanıcısı koreyspace için hackathon projeleri öner"

Router Agent isteğinizi analiz edecek ve sorgunuzu ele almak için hangi ajan kombinasyonunun (GitHub, Hackathon, ve Events) en uygun olduğunu belirleyecektir. Ajanlar, GitHub depo analizi, proje fikirleri ve ilgili teknoloji etkinliklerine dayalı kapsamlı öneriler sağlamak için birlikte çalışır.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Feragatname:
Bu belge, Co-op Translator (https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk konusunda titiz olsak da, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilindeki metni esas alınarak yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->