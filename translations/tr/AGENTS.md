# AGENTS.md

## Proje Genel Bakış

Bu depo, "Yeni Başlayanlar için AI Ajanları" adlı kapsamlı bir eğitim kursunu içerir. Kurs, AI ajanları oluşturmak için gereken her şeyi öğretir. 15'ten fazla ders, temel bilgiler, tasarım kalıpları, çerçeveler ve AI ajanlarının üretim ortamına dağıtımını kapsar.

**Anahtar Teknolojiler:**
- Python 3.12+
- Etkileşimli öğrenme için Jupyter Notebooks
- AI Çerçeveleri: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI Hizmetleri: Azure AI Foundry, Azure AI Agent Service
- GitHub Modeller Pazarı (ücretsiz katman mevcut)

**Mimari:**
- Ders tabanlı yapı (00-15+ dizinler)
- Her ders şunları içerir: README dokümantasyonu, kod örnekleri (Jupyter not defterleri) ve görseller
- Otomatik çeviri sistemi ile çoklu dil desteği
- Her ders için birden fazla çerçeve seçeneği (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Kurulum Komutları

### Ön Koşullar
- Python 3.12 veya üstü
- GitHub hesabı (GitHub Modelleri için - ücretsiz katman)
- Azure aboneliği (isteğe bağlı, Azure AI hizmetleri için)

### İlk Kurulum

1. **Depoyu klonlayın veya çatallayın:**
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

3. **Bağımlılıkları yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ortam değişkenlerini ayarlayın:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Gerekli Ortam Değişkenleri

**GitHub Modelleri (Ücretsiz)** için:
- `GITHUB_TOKEN` - GitHub'dan alınan kişisel erişim tokeni

**Azure AI Hizmetleri** (isteğe bağlı) için:
- `PROJECT_ENDPOINT` - Azure AI Foundry proje uç noktası
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API anahtarı
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI uç nokta URL'si
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Sohbet modeli için dağıtım adı
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Gömülü modeller için dağıtım adı
- `.env.example` dosyasında gösterilen ek Azure yapılandırması

## Geliştirme İş Akışı

### Jupyter Not Defterlerini Çalıştırma

Her ders, farklı çerçeveler için birden fazla Jupyter not defteri içerir:

1. **Jupyter'i başlatın:**
   ```bash
   jupyter notebook
   ```

2. **Bir ders dizinine gidin** (örneğin, `01-intro-to-ai-agents/code_samples/`)

3. **Not defterlerini açın ve çalıştırın:**
   - `*-semantic-kernel.ipynb` - Semantic Kernel çerçevesini kullanarak
   - `*-autogen.ipynb` - AutoGen çerçevesini kullanarak
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) kullanarak
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) kullanarak
   - `*-azureaiagent.ipynb` - Azure AI Agent Service kullanarak

### Farklı Çerçevelerle Çalışma

**Semantic Kernel + GitHub Modelleri:**
- GitHub hesabı ile ücretsiz katman mevcut
- Öğrenme ve deney için uygun
- Dosya deseni: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Modelleri:**
- GitHub hesabı ile ücretsiz katman mevcut
- Çoklu ajan düzenleme yetenekleri
- Dosya deseni: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Microsoft'un en yeni çerçevesi
- Python ve .NET'te mevcut
- Dosya deseni: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Azure aboneliği gerektirir
- Üretime hazır özellikler
- Dosya deseni: `*-azureaiagent.ipynb`

## Test Talimatları

Bu, otomatik testlere sahip üretim kodu yerine örnek kod içeren bir eğitim deposudur. Kurulumunuzu ve değişikliklerinizi doğrulamak için:

### Manuel Test

1. **Python ortamını test edin:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Not defteri çalıştırmayı test edin:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Ortam değişkenlerini doğrulayın:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Bireysel Not Defterlerini Çalıştırma

Not defterlerini Jupyter'de açın ve hücreleri sırayla çalıştırın. Her not defteri bağımsızdır ve şunları içerir:
- İçe aktarma ifadeleri
- Yapılandırma yükleme
- Örnek ajan uygulamaları
- Beklenen çıktılar markdown hücrelerinde

## Kod Stili

### Python Konvansiyonları

- **Python Versiyonu**: 3.12+
- **Kod Stili**: Standart Python PEP 8 konvansiyonlarını takip edin
- **Not Defterleri**: Kavramları açıklamak için net markdown hücreleri kullanın
- **İçe Aktarmalar**: Standart kütüphane, üçüncü taraf, yerel içe aktarmalar olarak gruplandırın

### Jupyter Not Defteri Konvansiyonları

- Kod hücrelerinden önce açıklayıcı markdown hücreleri ekleyin
- Referans için not defterlerinde çıktı örnekleri ekleyin
- Ders kavramlarına uygun net değişken adları kullanın
- Not defteri yürütme sırasını doğrusal tutun (hücre 1 → 2 → 3...)

### Dosya Organizasyonu

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```

## Derleme ve Dağıtım

### Dokümantasyon Derleme

Bu depo, dokümantasyon için Markdown kullanır:
- Her ders klasöründe README.md dosyaları
- Depo kökünde ana README.md
- GitHub Actions aracılığıyla otomatik çeviri sistemi

### CI/CD Pipeline

`.github/workflows/` içinde yer alır:

1. **co-op-translator.yml** - 50+ dile otomatik çeviri
2. **welcome-issue.yml** - Yeni sorun oluşturucuları karşılar
3. **welcome-pr.yml** - Yeni çekme isteği katkıcılarını karşılar

### Dağıtım

Bu bir eğitim deposudur - dağıtım süreci yoktur. Kullanıcılar:
1. Depoyu çatallayın veya klonlayın
2. Not defterlerini yerel olarak veya GitHub Codespaces'te çalıştırın
3. Örnekleri değiştirerek ve deneyerek öğrenin

## Çekme İsteği Yönergeleri

### Göndermeden Önce

1. **Değişikliklerinizi test edin:**
   - Etkilenen not defterlerini tamamen çalıştırın
   - Tüm hücrelerin hatasız çalıştığını doğrulayın
   - Çıktıların uygun olduğunu kontrol edin

2. **Dokümantasyon güncellemeleri:**
   - Yeni kavramlar ekliyorsanız README.md'yi güncelleyin
   - Karmaşık kod için not defterlerine yorum ekleyin
   - Markdown hücrelerinin amacı açıklamasını sağlayın

3. **Dosya değişiklikleri:**
   - `.env` dosyalarını taahhüt etmeyin (`.env.example` kullanın)
   - `venv/` veya `__pycache__/` dizinlerini taahhüt etmeyin
   - Kavramları gösterdiğinde not defteri çıktısını koruyun
   - Geçici dosyaları ve yedek not defterlerini (`*-backup.ipynb`) kaldırın

### PR Başlık Formatı

Açıklayıcı başlıklar kullanın:
- `[Lesson-XX] <kavram> için yeni örnek ekle`
- `[Fix] lesson-XX README'de yazım hatasını düzelt`
- `[Update] lesson-XX'deki kod örneğini iyileştir`
- `[Docs] Kurulum talimatlarını güncelle`

### Gerekli Kontroller

- Not defterleri hatasız çalışmalı
- README dosyaları net ve doğru olmalı
- Depodaki mevcut kod kalıplarını takip edin
- Diğer derslerle tutarlılığı koruyun

## Ek Notlar

### Yaygın Sorunlar

1. **Python sürüm uyumsuzluğu:**
   - Python 3.12+ kullandığınızdan emin olun
   - Bazı paketler eski sürümlerle çalışmayabilir
   - Python sürümünü açıkça belirtmek için `python3 -m venv` kullanın

2. **Ortam değişkenleri:**
   - Her zaman `.env.example` dosyasından `.env` oluşturun
   - `.env` dosyasını taahhüt etmeyin (`.gitignore` içinde)
   - GitHub tokeni uygun izinlere ihtiyaç duyar

3. **Paket çatışmaları:**
   - Yeni bir sanal ortam kullanın
   - Bireysel paketler yerine `requirements.txt` dosyasından yükleme yapın
   - Bazı not defterleri markdown hücrelerinde belirtilen ek paketlere ihtiyaç duyabilir

4. **Azure hizmetleri:**
   - Azure AI hizmetleri aktif abonelik gerektirir
   - Bazı özellikler bölgeye özeldir
   - GitHub Modelleri için ücretsiz katman sınırlamaları geçerlidir

### Öğrenme Yolu

Dersler arasında önerilen ilerleme:
1. **00-course-setup** - Ortam kurulumuna buradan başlayın
2. **01-intro-to-ai-agents** - AI ajanlarının temelini anlayın
3. **02-explore-agentic-frameworks** - Farklı çerçeveleri öğrenin
4. **03-agentic-design-patterns** - Temel tasarım kalıpları
5. Numaralandırılmış derslere sırayla devam edin

### Çerçeve Seçimi

Hedeflerinize göre çerçeve seçin:
- **Öğrenme/Prototipleme**: Semantic Kernel + GitHub Modelleri (ücretsiz)
- **Çoklu ajan sistemleri**: AutoGen
- **En yeni özellikler**: Microsoft Agent Framework (MAF)
- **Üretim dağıtımı**: Azure AI Agent Service

### Yardım Alma

- [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord) topluluğuna katılın
- Belirli rehberlik için ders README dosyalarını inceleyin
- Kurs genel bakışı için ana [README.md](./README.md) dosyasını kontrol edin
- Ayrıntılı kurulum talimatları için [Course Setup](./00-course-setup/README.md) dosyasına bakın

### Katkıda Bulunma

Bu açık bir eğitim projesidir. Katkılar memnuniyetle karşılanır:
- Kod örneklerini iyileştirin
- Yazım hatalarını veya hataları düzeltin
- Açıklayıcı yorumlar ekleyin
- Yeni ders konuları önerin
- Ek dillerde çeviri yapın

Mevcut ihtiyaçlar için [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) bölümüne bakın.

## Proje-Specifik Bağlam

### Çoklu Dil Desteği

Bu depo, otomatik bir çeviri sistemi kullanır:
- 50+ dil desteklenir
- Çeviriler `/translations/<lang-code>/` dizinlerinde yer alır
- GitHub Actions iş akışı çeviri güncellemelerini yönetir
- Kaynak dosyalar depo kökünde İngilizce olarak bulunur

### Ders Yapısı

Her ders tutarlı bir deseni takip eder:
1. Video küçük resmi ve bağlantısı
2. Yazılı ders içeriği (README.md)
3. Birden fazla çerçevede kod örnekleri
4. Öğrenme hedefleri ve ön koşullar
5. Ek öğrenme kaynaklarına bağlantılar

### Kod Örnek Adlandırma

Format: `<ders-numarası>-<çerçeve-adı>.ipynb`
- `04-semantic-kernel.ipynb` - Ders 4, Semantic Kernel
- `07-autogen.ipynb` - Ders 7, AutoGen
- `14-python-agent-framework.ipynb` - Ders 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Ders 14, MAF .NET

### Özel Dizinler

- `translated_images/` - Çeviriler için yerelleştirilmiş görseller
- `images/` - İngilizce içerik için orijinal görseller
- `.devcontainer/` - VS Code geliştirme konteyner yapılandırması
- `.github/` - GitHub Actions iş akışları ve şablonlar

### Bağımlılıklar

`requirements.txt` dosyasından önemli paketler:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen çerçevesi
- `semantic-kernel` - Semantic Kernel çerçevesi
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI hizmetleri
- `azure-search-documents` - Azure AI Arama entegrasyonu
- `chromadb` - RAG örnekleri için vektör veritabanı
- `chainlit` - Sohbet UI çerçevesi
- `browser_use` - Ajanlar için tarayıcı otomasyonu
- `mcp[cli]` - Model Context Protocol desteği
- `mem0ai` - Ajanlar için hafıza yönetimi

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.