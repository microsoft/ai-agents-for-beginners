# AGENTS.md

## Proje Genel Bakışı

Bu depo, "Yeni Başlayanlar için Yapay Zeka Ajanları" içeren kapsamlı bir eğitim kursudur ve Yapay Zeka Ajanları oluşturmak için gereken her şeyi öğretir. Kurs, temel bilgiler, tasarım kalıpları, çerçeveler ve yapay zeka ajanlarının üretim ortamına dağıtımı gibi konuları kapsayan 15'ten fazla dersten oluşur.

**Ana Teknolojiler:**
- Python 3.12+
- Etkileşimli öğrenme için Jupyter Notebooks
- Yapay Zeka Çerçeveleri: Microsoft Agent Framework (MAF)
- Azure AI Hizmetleri: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Mimari:**
- Ders bazlı yapı (00-15+ klasörleri)
- Her derste: README dökümantasyonu, kod örnekleri (Jupyter defterleri) ve görseller
- Otomatik çeviri sistemi ile çoklu dil desteği
- Microsoft Agent Framework kullanan her ders için bir Python defteri

## Kurulum Komutları

### Önkoşullar
- Python 3.12 veya üzeri
- Azure aboneliği (Azure AI Foundry için)
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
   # .env dosyasını API anahtarlarınız ve uç noktalarınız ile düzenleyin
   ```

### Gerekli Ortam Değişkenleri

**Azure AI Foundry** için (Gerekli):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry proje uç noktası
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model dağıtım adı (örneğin: gpt-4o)

**Azure AI Search** için (Ders 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search uç noktası
- `AZURE_SEARCH_API_KEY` - Azure AI Search API anahtarı

Kimlik Doğrulama: Defterleri çalıştırmadan önce `az login` komutunu çalıştırın (AzureCliCredential kullanır).

## Geliştirme İş Akışı

### Jupyter Defterlerini Çalıştırma

Her ders, farklı çerçeveler için birden fazla Jupyter defteri içerir:

1. **Jupyter başlatın:**
   ```bash
   jupyter notebook
   ```

2. **Bir ders dizinine gidin** (örneğin, `01-intro-to-ai-agents/code_samples/`)

3. **Defterleri açıp çalıştırın:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework kullanarak (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework kullanarak (.NET)

### Microsoft Agent Framework ile Çalışmak

**Microsoft Agent Framework + Azure AI Foundry:**
- Azure aboneliği gerektirir
- Agent Service V2 için `AzureAIProjectAgentProvider` kullanır (ajanlar Foundry portalında görünür)
- Üretim ortamına hazır, yerleşik gözlemlenebilirlik ile
- Dosya deseni: `*-python-agent-framework.ipynb`

## Test Talimatları

Bu depo, otomatik testler içeren üretim kodu yerine eğitim amaçlı örnek kodları içerir. Kurulumunuzu ve değişikliklerinizi doğrulamak için:

### Manuel Test

1. **Python ortamını test edin:**
   ```bash
   python --version  # 3.12+ olmalı
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Defterlerin çalışmasını test edin:**
   ```bash
   # Defteri betiğe dönüştür ve çalıştır (testler ithalatları yapar)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Ortam değişkenlerini doğrulayın:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Tek Defterleri Çalıştırmak

Jupyter'de defterleri açıp hücreleri sırasıyla çalıştırın. Her defter bağımsızdır ve içerir:
- İçe aktarma beyanları
- Konfigürasyon yükleme
- Örnek ajan uygulamaları
- Markdown hücrelerinde beklenen çıktılar

## Kod Stili

### Python Konvansiyonları

- **Python Sürümü**: 3.12+
- **Kod Stili**: Standart Python PEP 8 konvansiyonlarına uyun
- **Defterler**: Kavramları açıklayan net markdown hücreleri kullanın
- **İçe Aktarmalar**: Standart kütüphane, üçüncü taraf ve yerel içe aktarmaları gruplayın

### Jupyter Defteri Konvansiyonları

- Kod hücrelerinden önce açıklayıcı markdown hücreleri ekleyin
- Referans için notlarda çıktı örnekleri ekleyin
- Ders kavramlarıyla uyumlu net değişken isimleri kullanın
- Defter yürütme sırasını lineer tutun (hücre 1 → 2 → 3...)

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

### Dökümantasyon Oluşturma

Bu depo dokümantasyon için Markdown kullanır:
- Her ders klasöründe README.md dosyaları
- Depo kökünde ana README.md
- GitHub Actions ile otomatik çeviri sistemi

### CI/CD Boru Hattı

`.github/workflows/` dizininde yer alır:

1. **co-op-translator.yml** - 50'den fazla dile otomatik çeviri
2. **welcome-issue.yml** - Yeni sorun açanları karşılar
3. **welcome-pr.yml** - Yeni pull request katkı sağlayanları karşılar

### Dağıtım

Eğitim amaçlı depo - dağıtım süreci yok. Kullanıcılar:
1. Depoyu çatallayabilir veya klonlayabilir
2. Defterleri yerel veya GitHub Codespaces’te çalıştırabilir
3. Örnekleri değiştirerek ve deneyerek öğrenirler

## Pull Request Rehberi

### Gönderim Öncesi

1. **Değişikliklerinizi test edin:**
   - Etkilenen defterleri tamamen çalıştırın
   - Tüm hücrelerin hatasız çalıştığını doğrulayın
   - Çıktıların uygun olduğundan emin olun

2. **Dökümantasyon güncellemeleri:**
   - Yeni kavram ekliyorsanız README.md güncelleyin
   - Karmaşık kodlar için defterlerde yorum ekleyin
   - Markdown hücrelerinin amacı açıkladığından emin olun

3. **Dosya değişiklikleri:**
   - `.env` dosyalarını commit etmeyin (`.env.example` kullanın)
   - `venv/` veya `__pycache__/` dizinlerini commit etmeyin
   - Kavramları gösteren defter çıktılarını korun
   - Geçici dosyaları ve yedek defterleri (`*-backup.ipynb`) kaldırın

### PR Başlık Formatı

Tanımlayıcı başlıklar kullanın:
- `[Lesson-XX] <konsept> için yeni örnek ekle`
- `[Fix] lesson-XX README’de yazım hatası düzeltildi`
- `[Update] lesson-XX kod örneği geliştirildi`
- `[Docs] kurulum talimatları güncellendi`

### Gerekli Kontroller

- Defterler hatasız çalışmalı
- README dosyaları açık ve doğru olmalı
- Depodaki mevcut kod kalıplarına uyulmalı
- Diğer derslerle tutarlılık korunmalı

## Ek Notlar

### Yaygın Problemler

1. **Python sürümü uyumsuzluğu:**
   - Python 3.12+ kullandığınızdan emin olun
   - Bazı paketler eski sürümlerle çalışmayabilir
   - Python sürümünü açıkça belirtmek için `python3 -m venv` kullanın

2. **Ortam değişkenleri:**
   - Her zaman `.env.example` dosyasından `.env` oluşturun
   - `.env` dosyasını commit etmeyin ( `.gitignore`'da)
   - GitHub token uygun izinlere sahip olmalı

3. **Paket çakışmaları:**
   - Yeni bir sanal ortam kullanın
   - Bireysel paketler yerine `requirements.txt` kullanarak kurulum yapın
   - Bazı defterlerin markdown hücrelerinde ek paket gerektiği belirtilmiştir

4. **Azure servisleri:**
   - Azure AI servisleri aktif abonelik ister
   - Bazı özellikler bölgeye özeldir
   - GitHub Modelleri için ücretsiz katman sınırları vardır

### Öğrenme Yolculuğu

Dersleri önerilen sıralama:
1. **00-course-setup** - Ortam kurulumu için başlangıç noktası
2. **01-intro-to-ai-agents** - AI ajan temellerini öğrenin
3. **02-explore-agentic-frameworks** - Farklı çerçeveleri keşfedin
4. **03-agentic-design-patterns** - Temel tasarım kalıpları
5. Numaralandırılmış derslerde sırayla devam edin

### Çerçeve Seçimi

Hedeflerinize göre çerçeve seçin:
- **Tüm dersler**: Microsoft Agent Framework (MAF) ve `AzureAIProjectAgentProvider`
- Ajanlar Azure AI Foundry Agent Service V2’de sunucu tarafında kayıt olur ve Foundry portalında görünür

### Yardım Alma

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) topluluğuna katılın
- Özel rehberlik için ders README dosyalarını inceleyin
- Kurs genel bakışı için ana [README.md](./README.md) dosyasına bakın
- Detaylı kurulum için [Course Setup](./00-course-setup/README.md) dosyasına başvurun

### Katkıda Bulunma

Bu açık eğitim projesidir. Katkılarınızı bekliyoruz:
- Kod örneklerini geliştirin
- Yazım hatalarını veya hataları düzeltin
- Açıklayıcı yorumlar ekleyin
- Yeni ders konuları önerin
- Ek dillere çeviri yapın

Mevcut ihtiyaçlar için [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) sayfasına göz atabilirsiniz.

## Projeye Özel Bağlam

### Çoklu Dil Desteği

Bu depo otomatik çeviri sistemi kullanır:
- 50'den fazla dil desteklenir
- Çeviriler `/translations/<lang-code>/` klasörlerinde
- GitHub Actions iş akışı çeviri güncellemelerini yönetir
- Kaynak dosyalar İngilizce olarak depo kökünde yer alır

### Ders Yapısı

Her ders tutarlı bir desene bağlıdır:
1. Bağlantılı video küçük resmi
2. Yazılı ders içeriği (README.md)
3. Birden çok çerçevede kod örnekleri
4. Öğrenme hedefleri ve ön koşullar
5. Ek öğrenme kaynakları bağlantıları

### Kod Örneği İsimlendirmesi

Format: `<ders-numarası>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Ders 1, MAF Python
- `14-sequential.ipynb` - Ders 14, MAF ileri düzey kalıplar

### Özel Dizinler

- `translated_images/` - Çeviriler için yerelleştirilmiş görseller
- `images/` - İngilizce içerik için orijinal görseller
- `.devcontainer/` - VS Code geliştirme konteyner konfigürasyonu
- `.github/` - GitHub Actions iş akışları ve şablonlar

### Bağımlılıklar

`requirements.txt` dosyasından ana paketler:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokol desteği
- `azure-ai-inference`, `azure-ai-projects` - Azure AI servisleri
- `azure-identity` - Azure kimlik doğrulama (AzureCliCredential)
- `azure-search-documents` - Azure AI Search entegrasyonu
- `mcp[cli]` - Model Context Protocol desteği

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstermekle birlikte, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi tavsiye edilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek herhangi bir yanlış anlama veya yorumlama nedeniyle sorumluluk kabul edilmemektedir.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->