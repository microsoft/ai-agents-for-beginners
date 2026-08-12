# AGENTS.md

## Proje Genel Bakış

Bu depo "Başlangıç Seviyesi AI Ajanları" içerir - AI Ajanları oluşturmak için gereken her şeyi öğreten kapsamlı bir eğitim kursu. Kurs, temel bilgiler, tasarım desenleri, çerçeveler, üretim dağıtımı, yerel/cihaz üzeri ajanlar ve AI ajanlarının güvenliği konularını kapsayan 18 dersten (00-18 numaralı) oluşmaktadır.

**Temel Teknolojiler:**
- Python 3.12+
- Etkileşimli öğrenim için Jupyter Notebooklar
- AI Çerçeveleri: Microsoft Agent Framework (MAF)
- Azure AI Hizmetleri: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Mimari:**
- Ders bazlı yapı (00-15+ dizinleri)
- Her ders şunları içerir: README dokümantasyonu, kod örnekleri (Jupyter not defterleri) ve görseller
- Otomatik çeviri sistemi ile çoklu dil desteği
- Microsoft Agent Framework kullanan her ders için bir Python not defteri

## Kurulum Komutları

### Gereksinimler
- Python 3.12 veya üzeri
- Azure aboneliği (Microsoft Foundry için)
- Azure CLI kurulumu ve kimlik doğrulaması (`az login`)

### İlk Kurulum

1. **Depoyu klonlayın veya çatallayın:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # VEYA
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python sanal ortamı oluşturun ve etkinleştirin:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows'ta: venv\Scripts\activate
   ```

3. **Bağımlılıkları yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ortam değişkenlerini ayarlayın:**
   ```bash
   cp .env.example .env
   # API anahtarlarınız ve uç noktalarınızla .env dosyasını düzenleyin
   ```

### Gerekli Ortam Değişkenleri

**Microsoft Foundry** için (Zorunlu):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry proje uç noktası
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model dağıtım adı (örneğin, gpt-5-mini)

**Azure AI Search** için (Ders 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search uç noktası
- `AZURE_SEARCH_API_KEY` - Azure AI Search API anahtarı

Kimlik doğrulama: Notebookları çalıştırmadan önce `az login` komutunu çalıştırın (`AzureCliCredential` kullanır).

## Geliştirme İş Akışı

### Jupyter Not Defterlerini Çalıştırma

Her ders farklı çerçeveler için birden fazla Jupyter not defteri içerir:

1. **Jupyter'i başlatın:**
   ```bash
   jupyter notebook
   ```

2. **Bir ders dizinine gidin** (örneğin, `01-intro-to-ai-agents/code_samples/`)

3. **Not defterlerini açın ve çalıştırın:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework kullanımı (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework kullanımı (.NET)

### Microsoft Agent Framework ile Çalışma

**Microsoft Agent Framework + Microsoft Foundry:**
- Azure aboneliği gerektirir
- Agent Service V2 için `FoundryChatClient` kullanır (ajanlar Foundry portalında görünür)
- Yerleşik gözlemlenebilirlik ile üretime hazır
- Dosya deseni: `*-python-agent-framework.ipynb`

## Test Talimatları

Bu eğitim deposu örnek kod içerir, otomatik testlere sahip üretim kodu değil. Kurulumu ve değişiklikleri doğrulamak için:

### Manuel Test

1. **Python ortamını test edin:**
   ```bash
   python --version  # 3.12 veya daha yeni olmalı
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Not defteri çalıştırmayı test edin:**
   ```bash
   # Not defterini betiğe dönüştür ve çalıştır (testler ithalatları kontrol eder)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Ortam değişkenlerini doğrulayın:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Bireysel Not Defterlerinin Çalıştırılması

Jupyter’da not defterlerini açıp hücreleri sırasıyla çalıştırın. Her not defteri kendi içinde tamdır ve şunları içerir:
- İçe aktarma ifadeleri
- Konfigürasyon yükleme
- Örnek ajan uygulamaları
- Markdown hücrelerinde beklenen çıktılar

### Dağıtılan Ajanların Duman Testi

Microsoft Foundry barındırılan ajan olarak dağıtılan dersler için (01, 04, 05, 16), depo `tests/` altında duman test katalogları içerir ve `.github/workflows/smoke-test.yml` iş akışı tarafından [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) eylemi ile çalıştırılır. Bunlar, bir geç dağıtım kapısı olarak hafif testlerdir (ajan erişilebilir mi ve temel istem beklentilerine uyuyor mu?), Ders 10 ve 16’daki değerlendirme hattını tamamlar. Katalogdan derse, dersden ajana eşleştirme için [tests/README.md](./tests/README.md) dosyasına bakın. Ders 17 Foundry Local ile yerel olarak çalışır ve barındırılan bir uç noktası yoktur; bu nedenle doğrudan not defteri çalıştırılarak doğrulanır.

## Kod Stili

### Python Konvansiyonları

- **Python Sürümü**: 3.12+
- **Kod Stili**: Standart Python PEP 8 konvansiyonlarına uyun
- **Not defterleri**: Kavramları açıklamak için açık markdown hücreleri kullanın
- **İçe Aktarmalar**: Standart kütüphane, üçüncü taraf, yerel içe aktarmalar olarak gruplandırın

### Jupyter Not Defteri Konvansiyonları

- Kod hücrelerinden önce açıklayıcı markdown hücreleri ekleyin
- Referans için not defterlerinde çıktı örnekleri ekleyin
- Ders kavramları ile uyumlu açık değişken isimleri kullanın
- Not defteri çalıştırma sırasını lineer tutun (hücre 1 → 2 → 3...)

### Dosya Organizasyonu

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Derleme ve Dağıtım

### Dokümantasyon Oluşturma

Bu depo dokümantasyon için Markdown kullanır:
- Her ders klasöründe README.md dosyaları
- Depo kökünde ana README.md
- GitHub Actions ile otomatik çeviri sistemi

### CI/CD Hattı

`.github/workflows/` dizininde yer alır:

1. **co-op-translator.yml** - 50+ dile otomatik çeviri
2. **welcome-issue.yml** - Yeni sorun oluşturanları karşılama
3. **welcome-pr.yml** - Yeni çekme isteği katkıcılarını karşılama

### Dağıtım

Bu, eğitim amaçlı bir depo olup dağıtım süreci yoktur. Kullanıcılar:
1. Depoyu çatallayabilir veya klonlayabilir
2. Not defterlerini yerel veya GitHub Codespaces’te çalıştırabilir
3. Örnekleri değiştirip deneyerek öğrenebilir

## Çekme İsteği Kılavuzu

### Göndermeden Önce

1. **Değişikliklerinizi test edin:**
   - Etkilenen not defterlerini tamamen çalıştırın
   - Tüm hücrelerin hatasız çalıştığını doğrulayın
   - Çıktıların uygun olduğunu kontrol edin

2. **Dokümantasyon güncellemeleri:**
   - Yeni kavram ekliyorsanız README.md dosyasını güncelleyin
   - Karmaşık kod için not defterlerine açıklama ekleyin
   - Markdown hücrelerinin amacını açıklamasını sağlayın

3. **Dosya değişiklikleri:**
   - `.env` dosyalarını commit etmeyin (`.env.example` kullanın)
   - `venv/` veya `__pycache__/` dizinlerini commit etmeyin
   - Kavramları gösteriyorsa not defteri çıktılarını koruyun
   - Geçici dosyaları ve yedek not defterlerini (`*-backup.ipynb`) kaldırın

### PR Başlık Formatı

Açıklayıcı başlıklar kullanın:
- `[Ders-XX] <kavram> için yeni örnek ekle`
- `[Düzeltme] ders-XX README’sindeki yazım hatasını düzelt`
- `[Güncelleme] ders-XX kod örneğini geliştir`
- `[Doküman] kurulum talimatlarını güncelle`

### Gerekli Kontroller

- Not defterleri hatasız çalışmalı
- README dosyaları açık ve doğru olmalı
- Depodaki mevcut kod kalıplarına uyulmalı
- Diğer derslerle uyumluluk sağlanmalı

## Ek Notlar

### Yaygın Sorunlar

1. **Python sürümü uyumsuzluğu:**
   - Python 3.12+ kullanıldığından emin olun
   - Bazı paketler eski sürümlerde çalışmayabilir
   - Python sürümünü net belirtilmek için `python3 -m venv` kullanın

2. **Ortam değişkenleri:**
   - Her zaman `.env.example` dosyasından `.env` oluşturun
   - `.env` dosyasını commit etmeyin (bu dosya `.gitignore`dadır)
   - Anahtarsız Entra ID kimlik doğrulaması için `az login` ile giriş yapın

3. **Paket çakışmaları:**
   - Temiz bir sanal ortam kullanın
   - Tek tek paket yüklemek yerine `requirements.txt` dosyasından yükleyin
   - Bazı not defterleri, markdown hücrelerinde belirtilen ek paketleri gerektirebilir

4. **Azure hizmetleri:**
   - Azure AI hizmetleri aktif abonelik gerektirir
   - Bazı özellikler bölgeye özgüdür
   - Azure OpenAI model dağıtımınızın Responses API’yi desteklediğinden emin olun

### Öğrenme Yolu

Dersler için önerilen ilerleme sırası:
1. **00-course-setup** - Ortam kurulumuyla buradan başlayın
2. **01-intro-to-ai-agents** - AI ajanlarının temellerini anlayın
3. **02-explore-agentic-frameworks** - Farklı çerçeveleri öğrenin
4. **03-agentic-design-patterns** - Temel tasarım desenleri
5. Numaralandırılmış derslerde sıralı ilerleyin

### Çerçeve Seçimi

Hedeflerinize göre çerçeve seçin:
- **Tüm dersler**: Microsoft Agent Framework (MAF) ve `FoundryChatClient`
- **Ajanlar sunucu tarafında kaydolur** Microsoft Foundry Agent Service V2’de ve Foundry portalında görünür

### Yardım Alma

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) topluluğuna katılın
- Spesifik rehberlik için ders README dosyalarını inceleyin
- Kurs genel bakışı için ana [README.md](./README.md) dosyasına bakın
- Detaylı kurulum talimatları için [Course Setup](./00-course-setup/README.md) dosyasına başvurun

### Katkıda Bulunma

Bu açık eğitim projesidir. Katkılarınızı bekliyoruz:
- Kod örneklerini geliştirin
- Yazım hatalarını veya hataları düzeltin
- Açıklayıcı yorumlar ekleyin
- Yeni ders konuları önerin
- Ek dillere çeviri yapın

Mevcut ihtiyaçlar için [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) sayfasına bakın.

## Projeye Özgü Bağlam

### Çoklu Dil Desteği

Bu depo otomatik bir çeviri sistemi kullanır:
- 50’den fazla dil desteklenir
- Çeviriler `/translations/<lang-code>/` dizinlerinde bulunur
- GitHub Actions iş akışı çeviri güncellemelerini yönetir
- Kaynak dosyalar depo kökünde İngilizce olarak bulunur

### Ders Yapısı

Her ders aşağıdaki tutarlı paterni izler:
1. Bağlantılı video küçük resmi
2. Yazılı ders içeriği (README.md)
3. Çeşitli çerçevelerde kod örnekleri
4. Öğrenme hedefleri ve önkoşullar
5. Ek öğrenme kaynaklarına bağlantılar

### Kod Örneği İsimlendirmesi

Biçim: `<ders-numarası>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 1. Ders, MAF Python
- `14-sequential.ipynb` - 14. Ders, MAF gelişmiş desenler
- `16-python-agent-framework.ipynb` - 16. Ders, üretim müşteri destek ajanı
- `17-local-agent-foundry-local.ipynb` - 17. Ders, Foundry Local + Qwen ile yerel ajan

### Özel Diziler

- `translated_images/` - Çeviriler için yerelleştirilmiş görseller
- `images/` - İngilizce içerik için orijinal görseller
- `.devcontainer/` - VS Code geliştirme konteyner yapılandırması
- `.github/` - GitHub Actions iş akışları ve şablonlar

### Bağımlılıklar

`requirements.txt` dosyasından temel paketler:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Ajanlar arası protokol desteği
- `azure-ai-inference`, `azure-ai-projects` - Azure AI hizmetleri
- `azure-identity` - Azure kimlik doğrulama (AzureCliCredential)
- `azure-search-documents` - Azure AI Search entegrasyonu
- `mcp[cli]` - Model Context Protocol desteği

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->