<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T13:31:01+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "tr"
}
-->
# Github MCP Sunucusu Örneği

## Açıklama

Bu, Microsoft Reactor tarafından düzenlenen AI Agents Hackathon için oluşturulmuş bir demo çalışmasıdır.

Araç, bir kullanıcının Github depolarına dayanarak hackathon projeleri önermekte kullanılır. Bu işlem şu şekilde gerçekleştirilir:

1. **Github Agent** - Github MCP Sunucusunu kullanarak depoları ve bu depolar hakkındaki bilgileri alır.
2. **Hackathon Agent** - Github Agent'tan gelen verileri kullanarak, kullanıcının projeleri, kullandığı diller ve AI Agents hackathonunun proje kategorilerine dayanarak yaratıcı hackathon proje fikirleri üretir.
3. **Events Agent** - Hackathon Agent'ın önerisine dayanarak, AI Agent Hackathon serisinden ilgili etkinlikleri önerir.

## Kodun Çalıştırılması 

### Ortam Değişkenleri

Bu demo, Azure Open AI Service, Semantic Kernel, Github MCP Sunucusu ve Azure AI Search kullanır.

Bu araçları kullanabilmek için doğru ortam değişkenlerini ayarladığınızdan emin olun:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit Sunucusunu Çalıştırma

MCP sunucusuna bağlanmak için bu demo, bir sohbet arayüzü olarak Chainlit kullanır.

Sunucuyu çalıştırmak için terminalinizde aşağıdaki komutu kullanın:

```bash
chainlit run app.py -w
```

Bu, Chainlit sunucunuzu `localhost:8000` üzerinde başlatmalı ve `event-descriptions.md` içeriği ile Azure AI Search Index'inizi doldurmalıdır.

## MCP Sunucusuna Bağlanma

Github MCP Sunucusuna bağlanmak için, "Mesajınızı buraya yazın.." sohbet kutusunun altındaki "fiş" simgesini seçin:

![MCP Bağlan](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.tr.png)

Buradan, Github MCP Sunucusuna bağlanma komutunu eklemek için "Bir MCP Bağlayın" seçeneğine tıklayabilirsiniz:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" kısmını gerçek Kişisel Erişim Jetonunuz ile değiştirin.

Bağlandıktan sonra, fiş simgesinin yanında bir (1) görmelisiniz, bu bağlantının başarılı olduğunu doğrular. Eğer görmüyorsanız, `chainlit run app.py -w` komutuyla Chainlit sunucusunu yeniden başlatmayı deneyin.

## Demoyu Kullanma 

Hackathon projeleri önermek için ajan iş akışını başlatmak adına şu gibi bir mesaj yazabilirsiniz:

"Github kullanıcısı koreyspace için hackathon projeleri öner"

Router Agent, isteğinizi analiz eder ve sorgunuzu en iyi şekilde ele alacak ajan kombinasyonunu (GitHub, Hackathon ve Events) belirler. Ajanlar, Github depo analizi, proje fikirleri üretimi ve ilgili teknoloji etkinlikleri önerileri temelinde kapsamlı öneriler sunmak için birlikte çalışır.

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.