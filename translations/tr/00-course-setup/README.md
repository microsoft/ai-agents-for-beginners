<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T11:46:30+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tr"
}
-->
# Kurs Kurulumu

## Giriş

Bu ders, kursun kod örneklerini nasıl çalıştıracağınızı ele alacaktır.

## Diğer Öğrencilerle Katılın ve Yardım Alın

Depoyu klonlamaya başlamadan önce, kurulumla ilgili yardım almak, kursla ilgili sorular sormak veya diğer öğrencilerle bağlantı kurmak için [AI Agents For Beginners Discord kanalına](https://aka.ms/ai-agents/discord) katılın.

## Bu Depoyu Klonlayın veya Çatallayın

Başlamak için lütfen GitHub Deposunu klonlayın veya çatallayın. Bu, kurs materyalinin kendi versiyonunuzu oluşturmanızı sağlar, böylece kodu çalıştırabilir, test edebilir ve üzerinde değişiklik yapabilirsiniz!

Bunu yapmak için <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">depo çatallama</a> bağlantısına tıklayın.

Artık bu kursun çatallanmış bir versiyonuna aşağıdaki bağlantıdan sahip olmalısınız:

![Çatallanmış Depo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.tr.png)

### Yüzeysel Klonlama (atölye / Codespaces için önerilir)

  >Tam depo, tüm geçmişi ve dosyaları indirdiğinizde büyük (~3 GB) olabilir. Sadece atölyeye katılıyorsanız veya yalnızca birkaç ders klasörüne ihtiyacınız varsa, yüzeysel klonlama (veya seyrek klonlama), geçmişi kısaltarak ve/veya blobları atlayarak bu indirmeyi büyük ölçüde önler.

#### Hızlı yüzeysel klonlama — minimum geçmiş, tüm dosyalar

Aşağıdaki komutlarda `<your-username>` kısmını çatallanmış URL'nizle (veya tercih ederseniz üst akış URL'siyle) değiştirin.

Sadece en son commit geçmişini klonlamak için (küçük indirme):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Belirli bir dalı klonlamak için:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Kısmi (seyrek) klonlama — minimum bloblar + yalnızca seçilen klasörler

Bu, kısmi klonlama ve seyrek-checkout kullanır (Git 2.25+ gerektirir ve kısmi klonlama desteği olan modern Git önerilir):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Depo klasörüne geçiş yapın:

Bash için:

```bash
cd ai-agents-for-beginners
```

Powershell için:

```powershell
Set-Location ai-agents-for-beginners
```

Sonra hangi klasörleri istediğinizi belirtin (aşağıdaki örnek iki klasörü gösterir):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Dosyaları klonladıktan ve doğruladıktan sonra, yalnızca dosyalara ihtiyacınız varsa ve alanı boşaltmak istiyorsanız (git geçmişi olmadan), depo meta verilerini silin (💀geri alınamaz — tüm Git işlevselliğini kaybedersiniz: commit, pull, push veya geçmiş erişimi yok).

Linux/macOS için:

```bash
rm -rf .git
```

Windows için:

```powershell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces Kullanımı (yerel büyük indirmelerden kaçınmak için önerilir)

- [GitHub UI](https://github.com/codespaces) üzerinden bu depo için yeni bir Codespace oluşturun.  

- Yeni oluşturulan Codespace'in terminalinde, yalnızca ihtiyacınız olan ders klasörlerini Codespace çalışma alanına getirmek için yukarıdaki yüzeysel/seyrek klonlama komutlarından birini çalıştırın.
- İsteğe bağlı: Codespaces içinde klonladıktan sonra, fazladan alan kazanmak için .git'i kaldırın (yukarıdaki kaldırma komutlarına bakın).
- Not: Depoyu doğrudan Codespaces'te açmayı tercih ederseniz (ekstra klonlama olmadan), Codespaces devcontainer ortamını oluşturacak ve yine de ihtiyacınız olandan fazlasını sağlayabilir. Yeni bir Codespace içinde yüzeysel bir kopya klonlamak, disk kullanımını daha iyi kontrol etmenizi sağlar.

#### İpuçları

- Düzenleme/yükleme yapmak istiyorsanız her zaman klon URL'sini çatallanmış versiyonunuzla değiştirin.
- Daha sonra daha fazla geçmiş veya dosyaya ihtiyacınız olursa, bunları alabilir veya seyrek-checkout'u ek klasörleri içerecek şekilde ayarlayabilirsiniz.

## Kodun Çalıştırılması

Bu kurs, AI Agent'ları oluşturma konusunda pratik deneyim kazanmanız için çalıştırabileceğiniz bir dizi Jupyter Notebook sunar.

Kod örnekleri şu seçenekleri kullanır:

**GitHub Hesabı Gerektirir - Ücretsiz**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. (semantic-kernel.ipynb olarak etiketlenmiştir)
2) AutoGen Framework + GitHub Models Marketplace. (autogen.ipynb olarak etiketlenmiştir)

**Azure Aboneliği Gerektirir**:
3) Azure AI Foundry + Azure AI Agent Service. (azureaiagent.ipynb olarak etiketlenmiştir)

Üç tür örneği de denemenizi ve hangisinin sizin için en iyi çalıştığını görmenizi öneririz.

Hangi seçeneği seçerseniz seçin, aşağıdaki kurulum adımlarını belirleyecektir:

## Gereksinimler

- Python 3.12+
  - **NOT**: Python3.12 yüklü değilse, yüklediğinizden emin olun. Daha sonra requirements.txt dosyasından doğru sürümlerin yüklendiğinden emin olmak için python3.12 kullanarak venv oluşturun.
  
    >Örnek

    Python venv dizini oluşturun:

    ``` bash
    python3 -m venv venv
    ```

    Daha sonra venv ortamını şu şekilde etkinleştirin:

    macOS ve Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- GitHub Hesabı - GitHub Models Marketplace'e erişim için
- Azure Aboneliği - Azure AI Foundry'e erişim için
- Azure AI Foundry Hesabı - Azure AI Agent Service'e erişim için

Bu depoda, kod örneklerini çalıştırmak için gerekli olan tüm Python paketlerini içeren bir `requirements.txt` dosyası bulunmaktadır.

Bu dosyayı, depo kökündeki terminalinizde aşağıdaki komutu çalıştırarak yükleyebilirsiniz:

```bash
pip install -r requirements.txt
```

Herhangi bir çakışma ve sorun yaşamamak için bir Python sanal ortamı oluşturmanızı öneririz.

## VSCode Kurulumu
VSCode'da doğru Python sürümünü kullandığınızdan emin olun.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Modellerini Kullanarak Örnekler için Kurulum 

### Adım 1: GitHub Kişisel Erişim Token'ınızı (PAT) Alın

Bu kurs, GitHub Modeller Marketplace'i kullanır ve bu sayede AI Agent'ları oluşturmak için kullanacağınız Büyük Dil Modellerine (LLM'ler) ücretsiz erişim sağlar.

GitHub Modellerini kullanmak için bir [GitHub Kişisel Erişim Token'ı](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) oluşturmanız gerekecek.

Bunu GitHub Hesabınızdaki <a href="https://github.com/settings/personal-access-tokens" target="_blank">Kişisel Erişim Token'ları ayarları</a> sayfasına giderek yapabilirsiniz.

Token oluştururken [En Az Ayrıcalık İlkesi](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) ilkesini takip edin. Bu, token'a yalnızca bu kurstaki kod örneklerini çalıştırmak için gereken izinleri vermeniz gerektiği anlamına gelir.

1. **Geliştirici ayarları** bölümüne giderek ekranın sol tarafında `Hassas tokenlar` seçeneğini seçin.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.tr.png)

    Ardından `Yeni token oluştur` seçeneğini seçin.

    ![Token Oluştur](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.tr.png)

2. Token'ınızın amacını yansıtan açıklayıcı bir ad girin, böylece daha sonra kolayca tanımlayabilirsiniz.

    🔐 Token Süresi Önerisi

    Önerilen süre: 30 gün
    Daha güvenli bir duruş için daha kısa bir süre tercih edebilirsiniz—örneğin, 7 gün 🛡️
    Bu, kişisel bir hedef belirlemek ve öğrenme ivmenizi yüksek tutarak kursu tamamlamak için harika bir yoldur 🚀.

    ![Token Adı ve Süresi](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.tr.png)

3. Token'ın kapsamını bu deponun çatallanmış versiyonuna sınırlayın.

    ![Depo Kapsamını Sınırlama](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.tr.png)

4. Token'ın izinlerini kısıtlayın: **İzinler** altında, **Hesap** sekmesine tıklayın ve "+ İzin ekle" düğmesine tıklayın. Bir açılır menü görünecektir. Lütfen **Modeller** için arama yapın ve kutuyu işaretleyin.
    ![Modeller İzni Ekle](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.tr.png)

5. Token'ı oluşturmadan önce gereken izinleri doğrulayın. ![İzinleri Doğrula](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.tr.png)

6. Token'ı oluşturmadan önce, token'ı bir şifre yöneticisi kasası gibi güvenli bir yerde saklamaya hazır olduğunuzdan emin olun, çünkü oluşturduktan sonra tekrar gösterilmeyecektir. ![Token'ı Güvenli Bir Şekilde Sakla](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.tr.png)

Yeni oluşturduğunuz token'ı kopyalayın. Şimdi bu token'ı bu kursa dahil edilen `.env` dosyasına ekleyeceksiniz.


### Adım 2: `.env` Dosyanızı Oluşturun

`.env` dosyanızı oluşturmak için terminalinizde aşağıdaki komutu çalıştırın.

```bash
cp .env.example .env
```

Bu, örnek dosyayı kopyalayacak ve dizininizde bir `.env` dosyası oluşturacaktır. Bu dosyada çevre değişkenleri için değerleri doldurabilirsiniz.

Token'ınızı kopyaladıktan sonra, favori metin düzenleyicinizi açın ve token'ınızı `GITHUB_TOKEN` alanına yapıştırın.
![GitHub Token Alanı](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.tr.png)


Artık bu kursun kod örneklerini çalıştırabilirsiniz.

## Azure AI Foundry ve Azure AI Agent Service Kullanarak Örnekler için Kurulum

### Adım 1: Azure Proje Uç Noktanızı Alın


Azure AI Foundry'de bir hub ve proje oluşturma adımlarını buradan takip edin: [Hub kaynakları genel bakış](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


Projenizi oluşturduktan sonra, projeniz için bağlantı dizgesini almanız gerekecek.

Bu, Azure AI Foundry portalındaki projenizin **Genel Bakış** sayfasına giderek yapılabilir.

![Proje Bağlantı Dizgesi](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.tr.png)

### Adım 2: `.env` Dosyanızı Oluşturun

`.env` dosyanızı oluşturmak için terminalinizde aşağıdaki komutu çalıştırın.

```bash
cp .env.example .env
```

Bu, örnek dosyayı kopyalayacak ve dizininizde bir `.env` dosyası oluşturacaktır. Bu dosyada çevre değişkenleri için değerleri doldurabilirsiniz.

Token'ınızı kopyaladıktan sonra, favori metin düzenleyicinizi açın ve token'ınızı `PROJECT_ENDPOINT` alanına yapıştırın.

### Adım 3: Azure'a Giriş Yapın

Bir güvenlik en iyi uygulaması olarak, Microsoft Entra ID ile [anahtarsız kimlik doğrulama](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) kullanacağız.

Sonraki adımda, bir terminal açın ve Azure hesabınıza giriş yapmak için `az login --use-device-code` komutunu çalıştırın.

Giriş yaptıktan sonra, terminalde aboneliğinizi seçin.


## Ek Çevre Değişkenleri - Azure Search ve Azure OpenAI 

Agentic RAG Dersi - Ders 5 - Azure Search ve Azure OpenAI kullanan örnekler içerir.

Bu örnekleri çalıştırmak istiyorsanız, `.env` dosyanıza aşağıdaki çevre değişkenlerini eklemeniz gerekecek:

### Genel Bakış Sayfası (Proje)

- `AZURE_SUBSCRIPTION_ID` - Projenizin **Genel Bakış** sayfasındaki **Proje detayları** bölümünü kontrol edin.

- `AZURE_AI_PROJECT_NAME` - Projenizin **Genel Bakış** sayfasının üst kısmına bakın.

- `AZURE_OPENAI_SERVICE` - **Genel Bakış** sayfasındaki **Dahil edilen yetenekler** sekmesinde **Azure OpenAI Service** için bu bilgiyi bulun.

### Yönetim Merkezi

- `AZURE_OPENAI_RESOURCE_GROUP` - **Yönetim Merkezi**nin **Genel Bakış** sayfasındaki **Proje özellikleri**ne gidin.

- `GLOBAL_LLM_SERVICE` - **Bağlı kaynaklar** altında, **Azure AI Services** bağlantı adını bulun. Listelenmemişse, kaynak grubunuzdaki AI Services kaynak adını **Azure portalı**nda kontrol edin.

### Modeller + Uç Noktalar Sayfası

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Gömülü modelinizi seçin (örneğin, `text-embedding-ada-002`) ve model detaylarından **Dağıtım adını** not alın.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Sohbet modelinizi seçin (örneğin, `gpt-4o-mini`) ve model detaylarından **Dağıtım adını** not alın.

### Azure Portalı

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services**'i arayın, üzerine tıklayın, ardından **Kaynak Yönetimi**, **Anahtarlar ve Uç Nokta**ya gidin, "Azure OpenAI uç noktaları" bölümüne kadar aşağı kaydırın ve "Dil API'leri" yazan kısmı kopyalayın.

- `AZURE_OPENAI_API_KEY` - Aynı ekrandan, ANAHTAR 1 veya ANAHTAR 2'yi kopyalayın.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - **Azure AI Search** kaynağınızı bulun, üzerine tıklayın ve **Genel Bakış** bölümüne bakın.

- `AZURE_SEARCH_API_KEY` - Ardından **Ayarlar** ve **Anahtarlar** bölümüne giderek birincil veya ikincil yönetici anahtarını kopyalayın.

### Harici Web Sayfası

- `AZURE_OPENAI_API_VERSION` - [API sürüm yaşam döngüsü](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) sayfasını **En son GA API sürümü** altında ziyaret edin.

### Anahtarsız kimlik doğrulama ayarlama

Kimlik bilgilerinizi kodlamak yerine, Azure OpenAI ile anahtarsız bir bağlantı kullanacağız. Bunu yapmak için `DefaultAzureCredential`'ı içe aktaracağız ve daha sonra kimlik bilgilerini almak için `DefaultAzureCredential` fonksiyonunu çağıracağız.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Bir Yerde Takıldınız mı?
Eğer bu kurulumu çalıştırırken herhangi bir sorun yaşarsanız, <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>'a katılabilir veya <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">bir sorun oluşturabilirsiniz</a>.

## Sonraki Ders

Artık bu kursun kodlarını çalıştırmaya hazırsınız. Yapay Zeka Ajanları dünyası hakkında daha fazla şey öğrenirken iyi eğlenceler!

[Giriş: Yapay Zeka Ajanları ve Ajan Kullanım Alanları](../01-intro-to-ai-agents/README.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.