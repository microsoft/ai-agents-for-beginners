# AGENTS.md

## Proje Genel Bakış

Bu depo "Başlangıç için Yapay Zeka Ajanları" içerir - Yapay Zeka Ajanları oluşturmak için gereken her şeyi öğreten kapsamlı bir eğitim kursu. Kurs, yapay zeka ajanlarının temelleri, tasarım kalıpları, çerçeveler ve üretim dağıtımı dahil olmak üzere 15+ ders içermektedir.

**Ana Teknolojiler:**
- Python 3.12+
- Etkileşimli öğrenim için Jupyter Notebooks
- Yapay Zeka Çerçeveleri: Microsoft Agent Framework (MAF)
- Azure AI Hizmetleri: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Mimari:**
- Ders tabanlı yapı (00-15+ dizinleri)
- Her ders içerir: README dokümantasyonu, kod örnekleri (Jupyter notebook’ları) ve görseller
- Otomatik çeviri sistemiyle çoklu dil desteği
- Microsoft Agent Framework kullanan her ders için bir Python notebook’u

## Kurulum Komutları

### Önkoşullar
- Python 3.12 veya üstü
- Azure aboneliği (Azure AI Foundry için)
- Azure CLI yüklü ve giriş yapılmış (`az login`)

### İlk Kurulum

1. **Depoyu klonlayın veya çatallayın:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # VEYA
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python sanal ortamı oluşturun ve aktifleştirin:**
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

**Azure AI Foundry** için (Zorunlu):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry proje uç noktası
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model dağıtım adı (ör. gpt-4o)

**Azure AI Search** için (Ders 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search uç noktası
- `AZURE_SEARCH_API_KEY` - Azure AI Search API anahtarı

Kimlik Doğrulama: Notebook’ları çalıştırmadan önce `az login` komutunu çalıştırın (`AzureCliCredential` kullanır).

## Geliştirme İş Akışı

### Jupyter Notebook’ları Çalıştırma

Her ders farklı çerçeveler için birden fazla Jupyter notebook içerir:

1. **Jupyter’i başlatın:**
   ```bash
   jupyter notebook
   ```

2. **Bir ders dizinine gidin** (ör. `01-intro-to-ai-agents/code_samples/`)

3. **Notebook’ları açın ve çalıştırın:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework kullanarak (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework kullanarak (.NET)

### Microsoft Agent Framework ile Çalışma

**Microsoft Agent Framework + Azure AI Foundry:**
- Azure aboneliği gerektirir
- Agent Service V2 için `AzureAIProjectAgentProvider` kullanır (ajanlar Foundry portalında görünür)
- Yerleşik gözlemlenebilirlik ile üretime hazır
- Dosya paterni: `*-python-agent-framework.ipynb`

## Test Talimatları

Bu depo üretim kodu yerine eğitim amaçlı örnek kodlar içerir ve otomatik testler yoktur. Kurulumunuzu ve değişikliklerinizi doğrulamak için:

### Manuel Test

1. **Python ortamını test edin:**
   ```bash
   python --version  # 3.12+ olmalıdır
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Notebook çalıştırmayı test edin:**
   ```bash
   # Defteri betiğe dönüştür ve çalıştır (testlerin içe aktarımlarını kontrol eder)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Ortam değişkenlerini doğrulayın:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Tekil Notebook’ları Çalıştırma

Notebook’ları Jupyter'de açın ve hücreleri sırasıyla çalıştırın. Her notebook bağımsızdır ve şunları içerir:
- İçe aktarma ifadeleri
- Konfigürasyon yüklemesi
- Örnek ajan uygulamaları
- Markdown hücrelerinde beklenen çıktılar

## Kod Stili

### Python Konvansiyonları

- **Python Versiyonu**: 3.12+
- **Kod Stili**: Standart Python PEP 8 kurallarına uyun
- **Notebook’lar**: Konseptleri açıklayan net markdown hücreleri kullanın
- **İçe Aktarımlar**: Standart kütüphane, üçüncü taraf, yerel importlar olarak gruplayın

### Jupyter Notebook Konvansiyonları

- Kod hücrelerinden önce açıklayıcı markdown hücreleri ekleyin
- Referans için çıktı örnekleri notebook’larda bulundurun
- Ders kavramlarına uygun net değişken isimleri kullanın
- Notebook yürütme sırasını lineer tutun (hücre 1 → 2 → 3...)

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

`.github/workflows/` dizininde:

1. **co-op-translator.yml** - 50+ dile otomatik çeviri
2. **welcome-issue.yml** - Yeni issue oluşturanları karşılama
3. **welcome-pr.yml** - Yeni pull request katkıda bulunanları karşılama

### Dağıtım

Bu eğitim amaçlı bir depodur - dağıtım süreci yoktur. Kullanıcılar:
1. Depoyu çatallayabilir veya klonlayabilir
2. Notebook’ları yerel veya GitHub Codespaces’de çalıştırabilir
3. Örnekleri değiştirerek ve deneyerek öğrenir

## Pull Request Kılavuzu

### Gönderim Öncesi

1. **Değişikliklerinizi test edin:**
   - İlgili notebook’ları tamamen çalıştırın
   - Tüm hücrelerin hata vermeden tamamlandığını doğrulayın
   - Çıktıların uygun olduğundan emin olun

2. **Dokümantasyon güncellemeleri:**
   - Yeni kavram ekliyorsanız README.md’yi güncelleyin
   - Notebook’larda karmaşık kodlar için yorumlar ekleyin
   - Markdown hücrelerinin amacı açıklamasını sağlayın

3. **Dosya değişiklikleri:**
   - `.env` dosyası göndermekten kaçının (`.env.example` kullanın)
   - `venv/` veya `__pycache__/` dizinlerini göndermeyin
   - Kavramları gösteren notebook çıktılarını koruyun
   - Geçici dosyalar ve yedek notebook’ları (`*-backup.ipynb`) kaldırın

### PR Başlık Formatı

Açıklayıcı başlıklar kullanın:
- `[Lesson-XX] <konsept> için yeni örnek eklendi`
- `[Fix] lesson-XX README’de yazım hatası düzeltildi`
- `[Update] lesson-XX kod örneği iyileştirildi`
- `[Docs] kurulum talimatları güncellendi`

### Gerekli Kontroller

- Notebook’lar hata vermeden çalışmalı
- README dosyaları açık ve doğru olmalı
- Depodaki mevcut kod kalıplarına uyulmalı
- Diğer derslerle tutarlılık korunmalı

## Ek Notlar

### Yaygın Sorunlar

1. **Python sürüm uyumsuzluğu:**
   - Python 3.12+ kullanıldığından emin olun
   - Bazı paketler eski sürümlerle çalışmayabilir
   - Python sürümünü açıkça belirtmek için `python3 -m venv` kullanın

2. **Ortam değişkenleri:**
   - Her zaman `.env.example` dosyasından `.env` oluşturun
   - `.env` dosyasını göndermeyin (`.gitignore`dadır)
   - GitHub jetonunuzun gerekli izinlere sahip olduğundan emin olun

3. **Paket çakışmaları:**
   - Temiz bir sanal ortam kullanın
   - Paketleri tek tek değil, `requirements.txt` üzerinden kurun
   - Bazı notebook’lar markdown hücrelerinde ek paket gereksinimleri belirtebilir

4. **Azure hizmetleri:**
   - Azure AI servisleri aktif abonelik gerektirir
   - Bazı özellikler bölgesel sınırlamalar içerebilir
   - GitHub Modeller için ücretsiz katman kısıtlamaları geçerlidir

### Öğrenme Yolu

Derslere önerilen sıra:
1. **00-course-setup** - Ortam kurulumuna buradan başlayın
2. **01-intro-to-ai-agents** - AI ajanlarının temellerini öğrenin
3. **02-explore-agentic-frameworks** - Farklı çerçeveleri keşfedin
4. **03-agentic-design-patterns** - Temel tasarım kalıpları
5. Numaralandırılmış sonraki derslere sırayla devam edin

### Çerçeve Seçimi

Hedeflerinize göre çerçeve seçin:
- **Tüm dersler**: Microsoft Agent Framework (MAF) ve `AzureAIProjectAgentProvider`
- Ajanlar Azure AI Foundry Agent Service V2’de sunucu tarafında kayıt olur ve Foundry portalında görünür

### Yardım Alma

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)’a katılın
- Ders README dosyalarında spesifik rehberlik bulabilirsiniz
- Kurs genel bakışı için [ana README.md](./README.md)’yi inceleyin
- Detaylı kurulum talimatları için [Course Setup](./00-course-setup/README.md)’a bakın

### Katkıda Bulunma

Bu açık eğitim projesidir. Katkılar kabul edilir:
- Kod örneklerini geliştirin
- Yazım hatalarını veya hataları düzeltin
- Açıklayıcı yorumlar ekleyin
- Yeni ders konuları önerin
- Ek dillere çeviri yapın

Mevcut ihtiyaçlar için [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues)’a bakın.

## Proje Özel Bağlamı

### Çoklu Dil Desteği

Bu depo otomatik çeviri sistemi kullanır:
- 50+ dil desteklenir
- Çeviriler `/translations/<lang-code>/` dizinlerindedir
- GitHub Actions iş akışı çeviri güncellemelerini yönetir
- Kaynak dosyalar İngilizce olarak depo kökündedir

### Ders Yapısı

Her ders tutarlı bir düzen izler:
1. Linkli video küçük resmi
2. Yazılı ders içeriği (README.md)
3. Çoklu çerçevelerde kod örnekleri
4. Öğrenme hedefleri ve ön koşullar
5. Ek öğrenme kaynakları bağlantılı

### Kod Örneği İsimlendirmesi

Format: `<ders-numarası>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 1. Ders, MAF Python
- `14-sequential.ipynb` - 14. Ders, MAF gelişmiş kalıplar

### Özel Dizinler

- `translated_images/` - Çeviriler için yerelleştirilmiş görseller
- `images/` - İngilizce içerik için orijinal görseller
- `.devcontainer/` - VS Code geliştirme konteyner yapılandırması
- `.github/` - GitHub Actions iş akışları ve şablonlar

### Bağımlılıklar

`requirements.txt`’den önemli paketler:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokol desteği
- `azure-ai-inference`, `azure-ai-projects` - Azure AI hizmetleri
- `azure-identity` - Azure kimlik doğrulama (AzureCliCredential)
- `azure-search-documents` - Azure AI Search entegrasyonu
- `mcp[cli]` - Model Context Protocol desteği

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi özgün dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan dolayı tarafımız sorumlu tutulamaz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->