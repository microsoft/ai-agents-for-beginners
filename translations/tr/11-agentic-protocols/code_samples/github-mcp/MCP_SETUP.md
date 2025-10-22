<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T13:37:00+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "tr"
}
-->
# MCP Sunucu Entegrasyon Kılavuzu

## Ön Koşullar
- Node.js yüklü (sürüm 14 veya üzeri)
- npm paket yöneticisi
- Gerekli bağımlılıklarla birlikte Python ortamı

## Kurulum Adımları

1. **MCP Sunucu Paketini Yükleyin**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **MCP Sunucusunu Başlatın**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Sunucu başlamalı ve bir bağlantı URL'si görüntülenmelidir.

3. **Bağlantıyı Doğrulayın**
   - Chainlit arayüzünüzdeki fiş simgesini (🔌) kontrol edin
   - Fiş simgesinin yanında (1) numarası görünmelidir, bu başarılı bağlantıyı gösterir
   - Konsolda şu mesaj görünmelidir: "GitHub eklenti kurulumu başarıyla tamamlandı" (ek durum satırlarıyla birlikte)

## Sorun Giderme

### Yaygın Sorunlar

1. **Port Çakışması**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Çözüm: Portu şu şekilde değiştirin:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Kimlik Doğrulama Sorunları**
   - GitHub kimlik bilgilerinin doğru şekilde yapılandırıldığından emin olun
   - .env dosyasının gerekli tokenları içerdiğini kontrol edin
   - GitHub API erişimini doğrulayın

3. **Bağlantı Başarısız**
   - Sunucunun beklenen portta çalıştığını doğrulayın
   - Güvenlik duvarı ayarlarını kontrol edin
   - Python ortamının gerekli paketlere sahip olduğunu doğrulayın

## Bağlantı Doğrulama

MCP sunucunuz şu durumlarda düzgün bir şekilde bağlanmıştır:
1. Konsolda "GitHub eklenti kurulumu başarıyla tamamlandı" mesajı görünür
2. Bağlantı günlüklerinde "✓ MCP Bağlantı Durumu: Aktif" mesajı görünür
3. GitHub komutları sohbet arayüzünde çalışır

## Ortam Değişkenleri

.env dosyanızda gerekli olanlar:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Bağlantıyı Test Etme

Sohbette şu test mesajını gönderin:
```
Show me the repositories for username: [GitHub Username]
```
Başarılı bir yanıt, depo bilgilerini gösterecektir.

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.