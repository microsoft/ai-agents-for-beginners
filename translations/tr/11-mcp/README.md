<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:22:48+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "tr"
}
-->
# Ders 11: Model Bağlam Protokolü (MCP) Entegrasyonu

## Model Bağlam Protokolü'ne (MCP) Giriş

Model Bağlam Protokolü (MCP), yapay zeka modelleri ile istemci uygulamaları arasındaki etkileşimleri standartlaştırmak için tasarlanmış ileri düzey bir çerçevedir. MCP, yapay zeka modelleri ile bu modelleri kullanan uygulamalar arasında bir köprü görevi görerek, temel model uygulamasından bağımsız olarak tutarlı bir arayüz sağlar.

MCP'nin temel özellikleri:

- **Standartlaştırılmış İletişim**: MCP, uygulamaların yapay zeka modelleriyle iletişim kurması için ortak bir dil oluşturur.
- **Gelişmiş Bağlam Yönetimi**: Yapay zeka modellerine bağlamsal bilgilerin verimli bir şekilde aktarılmasını sağlar.
- **Çapraz Platform Uyumluluğu**: C#, Java, JavaScript, Python ve TypeScript gibi çeşitli programlama dillerinde çalışır.
- **Sorunsuz Entegrasyon**: Geliştiricilerin farklı yapay zeka modellerini uygulamalarına kolayca entegre etmesine olanak tanır.

MCP, özellikle yapay zeka ajanlarının geliştirilmesinde oldukça değerlidir çünkü ajanların çeşitli sistemler ve veri kaynaklarıyla birleşik bir protokol aracılığıyla etkileşim kurmasını sağlar, bu da onları daha esnek ve güçlü hale getirir.

## Öğrenme Hedefleri
- MCP'nin ne olduğunu ve yapay zeka ajanlarının geliştirilmesindeki rolünü anlamak
- GitHub entegrasyonu için bir MCP sunucusunu kurmak ve yapılandırmak
- MCP araçlarını kullanarak çoklu ajan sistemi oluşturmak
- Azure Cognitive Search ile RAG (Retrieval Augmented Generation) uygulamak

## Ön Koşullar
- Python 3.8+
- Node.js 14+
- Azure aboneliği
- GitHub hesabı
- Semantic Kernel hakkında temel bilgi

## Kurulum Talimatları

1. **Ortam Kurulumu**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure Hizmetlerini Yapılandırma**  
   - Azure Cognitive Search kaynağı oluşturun  
   - Azure OpenAI hizmetini ayarlayın  
   - `.env` dosyasında ortam değişkenlerini yapılandırın  

3. **MCP Sunucusunu Kurma**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Proje Yapısı

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## Temel Bileşenler

### 1. Çoklu Ajan Sistemi
- GitHub Ajanı: Depo analizi
- Hackathon Ajanı: Proje önerileri
- Etkinlik Ajanı: Teknoloji etkinliği önerileri

### 2. Azure Entegrasyonu
- Etkinlik indeksleme için Cognitive Search
- Ajan zekası için Azure OpenAI
- RAG deseninin uygulanması

### 3. MCP Araçları
- GitHub deposu analizi
- Kod incelemesi
- Meta veri çıkarımı

## Kod İncelemesi

Örnek, aşağıdakileri göstermektedir:  
1. MCP sunucusu entegrasyonu  
2. Çoklu ajan düzenlemesi  
3. Azure Cognitive Search entegrasyonu  
4. RAG deseninin uygulanması  

Öne çıkan özellikler:  
- Gerçek zamanlı GitHub deposu analizi  
- Akıllı proje önerileri  
- Azure Search kullanarak etkinlik eşleştirme  
- Chainlit ile akışkan yanıtlar  

## Örneği Çalıştırma

Ayrıntılı kurulum talimatları ve daha fazla bilgi için [Github MCP Sunucu Örneği README](./code_samples/github-mcp/README.md) dosyasına bakın.

1. MCP sunucusunu başlatın:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Uygulamayı başlatın:  
   ```bash
   chainlit run app.py -w
   ```

3. Entegrasyonu test edin:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Sorun Giderme

Yaygın sorunlar ve çözümler:  
1. MCP Bağlantı Sorunları  
   - Sunucunun çalıştığını doğrulayın  
   - Portun kullanılabilirliğini kontrol edin  
   - GitHub tokenlerini doğrulayın  

2. Azure Search Sorunları  
   - Bağlantı dizelerini doğrulayın  
   - İndeksin varlığını kontrol edin  
   - Belge yüklemesini doğrulayın  

## Sonraki Adımlar
- Ek MCP araçlarını keşfedin  
- Özel ajanlar uygulayın  
- RAG yeteneklerini geliştirin  
- Daha fazla etkinlik kaynağı ekleyin  
- **İleri Düzey**: Ajanlar arası iletişim örnekleri için [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) dizinine göz atın  

## Kaynaklar
- [MCP'ye Yeni Başlayanlar için](https://aka.ms/mcp-for-beginners)  
- [MCP Belgeleri](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Belgeleri](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel Kılavuzları](https://learn.microsoft.com/semantic-kernel/)  

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.