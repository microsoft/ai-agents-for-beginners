# AGENTS.md

## Proje Genel Bakışı

Bu depo, AI Ajanları Oluşturmak İçin Her Şeyi Öğreten kapsamlı bir eğitim kursu olan "Yeni Başlayanlar İçin AI Ajanları"nı içerir. Kurs, temel bilgileri, tasarım kalıplarını, frameworkleri, üretim dağıtımını, yerel/cihaz üstü ajanları ve AI ajanlarının güvenliğini kapsayan 18 dersten (00-18 numaralı) oluşmaktadır.

**Ana Teknolojiler:**
- Python 3.12+
- Etkileşimli öğrenme için Jupyter Notebooks
- AI Frameworkleri: Microsoft Agent Framework (MAF)
- Azure AI Servisleri: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Mimari:**
- Ders tabanlı yapı (00-18 klasörleri)
- Her ders içinde: README dokümantasyonu, kod örnekleri (Jupyter notebookları) ve görseller
- Otomatik çeviri sistemiyle çoklu dil desteği
- Her derste Microsoft Agent Framework kullanan bir Python notebooku

## Kurulum Komutları

### Önkoşullar
- Python 3.12 veya daha üstü
- Azure aboneliği (Microsoft Foundry için)
- Azure CLI kurulu ve kimlik doğrulanmış (`az login`)

### İlk Kurulum

1. **Depoyu klonlayın veya fork yapın:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python sanal ortamı oluşturun ve etkinleştirin:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Gerekli kütüphaneleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ortam değişkenlerini ayarlayın:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
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

### Jupyter Notebooklarını Çalıştırma

Her ders farklı frameworkler için birden fazla Jupyter notebooku içerir:

1. **Jupyter'i başlatın:**
   ```bash
   jupyter notebook
   ```

2. **Bir ders klasörüne gidin** (örneğin, `01-intro-to-ai-agents/code_samples/`)

3. **Notebookları açın ve çalıştırın:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework ile (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework ile (.NET)

### Microsoft Agent Framework ile Çalışma

**Microsoft Agent Framework + Microsoft Foundry:**
- Azure aboneliği gerektirir
- Agent Service V2 için `FoundryChatClient` kullanır (ajanlar Foundry portalında görünür)
- Yerleşik gözlemlenebilirlik ile üretim hazır
- Dosya deseni: `*-python-agent-framework.ipynb`

## Test Talimatları

Bu eğitim deposu, otomatik testlerle üretim kodu değil, örnek kod içerir. Kurulum ve değişikliklerinizi doğrulamak için:

### Manuel Test

1. **Python ortamını test edin:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Notebook çalıştırmayı test edin:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Ortam değişkenlerini doğrulayın:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Tekil Notebookları Çalıştırma

Jupyter’da notebookları açın ve hücreleri sırasıyla çalıştırın. Her notebook bağımsızdır ve şunları içerir:
- İçe aktarma ifadeleri
- Konfigürasyon yükleme
- Örnek ajan uygulamaları
- Markdown hücrelerinde beklenen çıktılar

### Dağıtılan Ajanların Smoke-Testi

Bir ajan Microsoft Foundry tarafından barındırılan ajan olarak dağıtıldığı dersler için (01, 04, 05, 16) bu depo `tests/` altında smoke-test katalogları içerir ve `.github/workflows/smoke-test.yml` iş akışı tarafından [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) aksiyonu ile çalıştırılır. Bunlar, temel prompt beklentilerini yerine getirip getirmediği test edilen hafif bir dağıtım sonrası kapıdır; 10 ve 16. derslerdeki değerlendirme hattını tamamlar. Katalog-ders-ajan eşlemesi için [tests/README.md](./tests/README.md) dosyasına bakınız. 17. ders Foundry Local ile yerelde çalışır ve barındırılan bir uç noktası yoktur, bu nedenle doğrudan notebooku çalıştırılarak doğrulanır.

## Kod Stili

### Python Konvansiyonları

- **Python Sürümü**: 3.12+
- **Kod Stili**: Standart Python PEP 8 konvansiyonlarını takip edin
- **Notebooklar**: Kavramları açıklamak için net markdown hücreleri kullanın
- **İçe Aktarmalar**: Standart kütüphane, üçüncü taraf ve yerel importları gruplayın

### Jupyter Notebook Konvansiyonları

- Kod hücrelerinden önce açıklayıcı markdown hücreleri ekleyin
- Referans için notebooklarda çıktı örnekleri ekleyin
- Ders kavramlarıyla uyumlu açık değişken isimleri kullanın
- Notebook çalıştırma sırasını lineer tutun (hücre 1 → 2 → 3...)

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

### Dokümantasyon Derleme

Bu depo dokümantasyon için Markdown kullanır:
- Her ders klasöründe README.md dosyaları
- Depo kökünde ana README.md
- GitHub Actions ile otomatik çeviri sistemi

### CI/CD Hattı

`.github/workflows/` içinde yer almaktadır:

1. **co-op-translator.yml** - 50+ dile otomatik çeviri
2. **welcome-issue.yml** - Yeni sorun oluşturuculara karşılama
3. **welcome-pr.yml** - Yeni pull request katkıcılarına karşılama

### Dağıtım

Bu eğitim depodur - dağıtım süreci yoktur. Kullanıcılar:
1. Depoyu fork veya klonlar
2. Notebookları yerelde veya GitHub Codespaces'te çalıştırır
3. Örnekleri değiştirip deneyerek öğrenir

## Pull Request Kuralları

### Gönderim Öncesi

1. **Değişikliklerinizi test edin:**
   - Etkilenen notebookları tamamen çalıştırın
   - Tüm hücrelerin hata olmadan çalıştığını doğrulayın
   - Çıktıların uygun olduğunu kontrol edin

2. **Dokümantasyon güncellemeleri:**
   - Yeni kavram ekliyorsanız README.md güncelleyin
   - Karmaşık kod için notebooklarda yorum ekleyin
   - Markdown hücrelerinin amacını açıklamasını sağlayın

3. **Dosya değişiklikleri:**
   - `.env` dosyalarını commit etmeyin (yerine `.env.example` kullanın)
   - `venv/` veya `__pycache__/` klasörlerini commit etmeyin
   - Kavram gösteren notebook çıktıları saklayın
   - Geçici dosya ve yedek notebookları (`*-backup.ipynb`) kaldırın

### PR Başlık Formatı

Açıklayıcı başlıklar kullanın:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Gereken Kontroller

- Notebooklar hatasız çalışmalı
- README dosyaları net ve doğru olmalı
- Mevcut kod kalıpları takip edilmeli
- Diğer derslerle tutarlılık korunmalı

## Ek Notlar

### Yaygın Tuzaklar

1. **Python sürümü uyuşmazlığı:**
   - Python 3.12+ kullandığınızdan emin olun
   - Bazı paketler eski sürümlerle çalışmayabilir
   - Python sürümünü açıkça belirtmek için `python3 -m venv` kullanın

2. **Ortam değişkenleri:**
   - Her zaman `.env` dosyasından `.env.example` oluşturun
   - `.env` dosyasını commit etmeyin (bu dosya `.gitignore` dizinindedir)
   - Anahtarsız Entra ID doğrulaması için `az login` ile giriş yapın

3. **Paket çakışmaları:**
   - Yeni bir sanal ortam kullanın
   - Bireysel paketler yerine `requirements.txt` üzerinden yükleyin
   - Bazı defterler markdown hücrelerinde belirtilen ek paketlere ihtiyaç duyabilir

4. **Azure hizmetleri:**
   - Azure AI hizmetleri için aktif abonelik gerekir
   - Bazı özellikler bölgeye özgüdür
   - Azure OpenAI model dağıtımınızın Responses API’yi desteklediğinden emin olun

### Öğrenme Yolu

Önerilen ders ilerleme sırası:
1. **00-course-setup** - Ortam kurulumu için buradan başlayın
2. **01-intro-to-ai-agents** - AI ajanlarının temellerini anlayın
3. **02-explore-agentic-frameworks** - Farklı çerçeveleri öğrenin
4. **03-agentic-design-patterns** - Temel tasarım kalıpları
5. Numaralandırılmış derslere sırayla devam edin

### Çerçeve Seçimi

Hedeflerinize göre çerçeve seçin:
- **Tüm dersler**: `FoundryChatClient` ile Microsoft Agent Framework (MAF)
- Microsoft Foundry Agent Service V2’de **ajanlar sunucu tarafında kayıtlıdır** ve Foundry portalında görünür

### Yardım Alma

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) katılın
- Belirli rehberlik için derslerin README dosyalarını inceleyin
- Kurs genel bakışı için ana [README.md](./README.md) dosyasını kontrol edin
- Ayrıntılı kurulum talimatları için [Course Setup](./00-course-setup/README.md) bölümüne bakın

### Katkıda Bulunma

Bu açık eğitim projesidir. Katkılarınızı bekliyoruz:
- Kod örneklerini geliştirin
- Yazım hatalarını veya hataları düzeltin
- Açıklayıcı yorumlar ekleyin
- Yeni ders konuları önerin
- Ek dillere çeviri yapın

Mevcut ihtiyaçlar için [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) sayfasına bakın.

## Projeye Özgü Bağlam

### Çok Dilli Destek

Bu depo otomatik çeviri sistemi kullanır:
- 50’den fazla dil desteklenir
- Çeviriler `/translations/<lang-code>/` dizinlerindedir
- Çeviri güncellemeleri GitHub Actions iş akışı tarafından yönetilir
- Kaynak dosyalar depoda İngilizce olarak kök dizindedir

### Ders Yapısı

Her ders tutarlı bir düzen izler:
1. Bağlantılı video küçük resmi
2. Yazılı ders içeriği (README.md)
3. Birden fazla çerçevede kod örnekleri
4. Öğrenme hedefleri ve ön gereksinimler
5. Bağlantılı ek öğrenme kaynakları

### Kod Örneği İsimlendirmesi

Biçim: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Ders 1, MAF Python
- `14-sequential.ipynb` - Ders 14, MAF ileri seviye kalıplar
- `16-python-agent-framework.ipynb` - Ders 16, üretim müşteri destek ajanı
- `17-local-agent-foundry-local.ipynb` - Ders 17, Foundry Local + Qwen ile yerel ajan

### Özel Dizinler

- `translated_images/` - Çeviriler için yerelleştirilmiş resimler
- `images/` - İngilizce içerik için orijinal resimler
- `.devcontainer/` - VS Code geliştirme konteyner yapılandırması
- `.github/` - GitHub Actions iş akışları ve şablonlar

### Bağımlılıklar

`requirements.txt` içindeki önemli paketler:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Ajanlar arası protokol desteği
- `azure-ai-inference`, `azure-ai-projects` - Azure AI hizmetleri
- `azure-identity` - Azure kimlik doğrulaması (AzureCliCredential)
- `azure-search-documents` - Azure AI Arama entegrasyonu
- `mcp[cli]` - Model Bağlam Protokolü desteği

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->