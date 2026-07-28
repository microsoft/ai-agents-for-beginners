# Kurs Kurulumu

## Giriş

Bu derste, bu kursun kod örneklerinin nasıl çalıştırılacağı ele alınacaktır.

## Diğer Öğrenenlere Katılın ve Yardım Alın

Depo çoğaltmaya başlamadan önce, kurulumla ilgili herhangi bir yardım almak, kurs hakkında sorular sormak veya diğer öğrenenlerle bağlantı kurmak için [AI Agents For Beginners Discord kanalına](https://aka.ms/ai-agents/discord) katılın.

## Bu Depoyu Çoğaltın veya Çatal Yapın

Başlamak için, lütfen GitHub deposunu çoğaltın veya çatal yapın. Bu, kodu çalıştırıp test edebilmeniz ve ayar yapabilmeniz için kurs materyalinin kendi versiyonunuzu oluşturmanızı sağlar!

Bu, <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">depo için çatal yap</a> bağlantısına tıklayarak yapılabilir.

Şimdi bu kursun kendi çatal yapmış versiyonuna aşağıdaki linkten ulaşmalısınız:

![Çatal Yapılmış Depo](../../../translated_images/tr/forked-repo.33f27ca1901baa6a.webp)

### Yüzeysel Çoğaltma (atölye / Codespaces için önerilir)

  >Tüm depo tam geçmişi ve dosyaları indirildiğinde büyük olabilir (~3 GB). Sadece atölyeye katılacaksanız veya yalnızca birkaç ders klasörüne ihtiyacınız varsa, yüzeysel çoğaltma (veya seyrek çoğaltma), geçmişi kısaltarak ve/veya blob'ları atlayarak çoğu indirimi önler.

#### Hızlı yüzeysel çoğaltma — minimal geçmiş, tüm dosyalar

Aşağıdaki komutlarda `<your-username>` yerini kendi çatal URL'nizle (veya tercihinize göre üst depo URL'siyle) değiştirin.

Sadece en son commit geçmişini çoğaltmak için (küçük indirme):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Belirli bir dalı çoğaltmak için:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Kısmi (seyrek) çoğaltma — minimal blob + sadece seçilen klasörler

Bu, kısmi çoğaltma ve seyrek-çekme kullanır (Git 2.25+ gerektirir ve kısmi çoğaltma destekli modern Git önerilir):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Depo klasörüne geçin:

```bash|powershell
cd ai-agents-for-beginners
```

Daha sonra hangi klasörlere ihtiyacınız olduğunu belirtin (aşağıdaki örnekte iki klasör gösterilmiştir):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Çoğaltma ve dosyaları doğruladıktan sonra, sadece dosyalara ihtiyacınız varsa ve yer açmak istiyorsanız (git geçmişi olmadan), repo meta verilerini silin (💀geri alınamaz — tüm Git işlevlerini kaybedersiniz: commit, pull, push veya geçmiş erişimi yok).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces Kullanımı (yerel büyük indirmelerden kaçınmak için önerilir)

- Bu repoya yeni bir Codespace oluşturun [GitHub UI](https://github.com/codespaces) üzerinden.  

- Yeni oluşturulan Codespace terminalinde, yukarıdaki yüzeysel/seyreklik çoğaltma komutlarından birini çalıştırarak sadece ihtiyacınız olan ders klasörlerini Codespace çalışma alanına getirin.
- Opsiyonel: Codespaces içinde çoğaltıldıktan sonra, ekstra alan kazanmak için .git dosyasını kaldırabilirsiniz (yukarıdaki kaldırma komutlarına bakın).
- Not: Depoyu doğrudan Codespaces içinde açmayı tercih ederseniz (ek çoğaltma olmadan), Codespaces geliştirme konteyner ortamını oluşturacak ve ihtiyacınızdan daha fazlasını sağlayabilir. Yeni bir Codespace içinde yüzeysel kopya çoğaltmak disk kullanımı üzerinde daha fazla kontrol sağlar.

#### İpuçları

- Düzenleme/commit yapmak istiyorsanız, çoğaltma URL'sini her zaman kendi çatalınızla değiştirin.
- Daha sonra daha fazla geçmiş veya dosyaya ihtiyacınız olursa, onları getirerek veya seyrek-çekme ayarını değiştirerek daha fazla klasör dahil edebilirsiniz.

## Kodu Çalıştırma

Bu kurs, AI Agentlar oluşturma konusunda pratik deneyim kazanmanız için çalıştırabileceğiniz bir dizi Jupyter Notebook sunmaktadır.

Kod örnekleri, **Microsoft Agent Framework (MAF)** kullanmakta ve `FoundryChatClient` ile **Microsoft Foundry Agent Service V2** (Yanıtlar API'si) üzerinden **Microsoft Foundry** ile bağlantı kurmaktadır.

Tüm Python notebokları `*-python-agent-framework.ipynb` olarak etiketlenmiştir.

## Gereksinimler

- Python 3.12+
  - **NOT:** Python3.12 yüklü değilse, yüklediğinizden emin olun. Daha sonra, requirements.txt dosyasından doğru sürümlerin yüklendiğine emin olmak için venv'inizi python3.12 kullanarak oluşturun.
  
    >Örnek

    Python venv dizini oluşturun:

    ```bash|powershell
    python -m venv venv
    ```

    Ardından venv ortamını şu şekilde etkinleştirin:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET kullanan örnek kodlar için, [.NET 10 SDK'sı](https://dotnet.microsoft.com/download/dotnet/10.0) veya daha yenisini yüklediğinizden emin olun. Ardından kurulu .NET SDK sürümünüzü kontrol edin:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Kimlik doğrulama için gereklidir. [aka.ms/installazurecli](https://aka.ms/installazurecli) adresinden yükleyin.
- **Azure Aboneliği** — Microsoft Foundry ve Microsoft Foundry Agent Service erişimi için.
- **Microsoft Foundry Projesi** — Dağıtılmış bir modeli (örneğin `gpt-5-mini`) olan bir proje. Aşağıdaki [1. Adım](#1-adım-bir-microsoft-foundry-projesi-oluşturun) bakınız.

Bu depoda, kod örneklerini çalıştırmak için gerekli tüm Python paketlerini içeren bir `requirements.txt` dosyası bulunmaktadır.

Bunları, terminalinizde deponun kök dizininde aşağıdaki komutu çalıştırarak yükleyebilirsiniz:

```bash|powershell
pip install -r requirements.txt
```

Herhangi bir çakışmayı ve sorunu önlemek için bir Python sanal ortamı (virtual environment) oluşturmanızı öneririz.

## VSCode Kurulumu

VSCode'da doğru Python sürümünü kullandığınızdan emin olun.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ve Microsoft Foundry Agent Service Kurulumu

### 1. Adım: Bir Microsoft Foundry Projesi Oluşturun

Notebokları çalıştırmak için dağıtılmış bir modele sahip Microsoft Foundry **hub** ve **projesine** ihtiyacınız var.

1. [ai.azure.com](https://ai.azure.com) adresine gidin ve Azure hesabınızla oturum açın.
2. Bir **hub** oluşturun (veya mevcut biri kullanın). Bkz: [Hub kaynakları genel bakış](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Hub içinde bir **proje** oluşturun.
4. **Modeller + Uç Noktalar** → **Model dağıt** kısmından bir model (örneğin `gpt-5-mini`) dağıtın.

### 2. Adım: Proje Uç Noktası ve Model Dağıtım Adı Alın

Microsoft Foundry portalındaki projenizden:

- **Proje Uç Noktası** — **Genel Bakış** sayfasına gidin ve uç nokta URL'sini kopyalayın.

![Proje Bağlantı Dizesi](../../../translated_images/tr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Dağıtım Adı** — **Modeller + Uç Noktalar** kısmına gidin, dağıtılmış modelinizi seçin ve **Dağıtım adı**nı not alın (örneğin `gpt-5-mini`).

### 3. Adım: `az login` ile Azure'a Giriş Yapın

Tüm noteboklar, kimlik doğrulama için **`AzureCliCredential`** kullanır — API anahtarı yönetimi gerektirmez. Bunun için Azure CLI ile oturum açmanız gerekir.

1. Daha önce yapmadıysanız **Azure CLI Yükleyin**: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. Şu komutla **oturum açın**:

    ```bash|powershell
    az login
    ```

    Ya da tarayıcı olmadan uzak/Codespace ortamındaysanız:

    ```bash|powershell
    az login --use-device-code
    ```

3. İstenirse **aboneliğinizi seçin** — Foundry projenizi içeren aboneliği tercih edin.

4. Oturumunuzun açıldığını **doğrulayın**:

    ```bash|powershell
    az account show
    ```

> **Neden `az login`?** Noteboklar, `azure-identity` paketinden `AzureCliCredential` kullanarak kimlik doğrulama yapar. Bu, Azure CLI oturumunuzun kimlik bilgilerini sağladığı anlamına gelir — `.env` dosyanızda API anahtarı veya gizli anahtar yoktur. Bu bir [güvenlik en iyi uygulamasıdır](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### 4. Adım: `.env` Dosyanızı Oluşturun

Örnek dosyayı kopyalayın:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

`.env` dosyasını açıp bu iki değeri doldurun:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Değişken | Nerede bulunur |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → projeniz → **Genel Bakış** sayfası |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Modeller + Uç Noktalar** → dağıtılmış modelinizin adı |

Çoğu ders için bu kadar! Noteboklar, `az login` oturumunuzla otomatik olarak kimlik doğrulaması yapacaktır.

### 5. Adım: Python Bağımlılıklarını Yükleyin

```bash|powershell
pip install -r requirements.txt
```

Daha önce oluşturduğunuz sanal ortam içinde çalıştırmanızı öneririz.

## Ders 5 için Ek Kurulum (Agentic RAG)

Ders 5, getirme destekli üretim için **Azure AI Search** kullanır. Bu dersi çalıştırmayı planlıyorsanız `.env` dosyanıza bu değişkenleri ekleyin:

| Değişken | Nerede bulunur |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → **Azure AI Search** kaynağınız → **Genel Bakış** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → **Azure AI Search** kaynağınız → **Ayarlar** → **Anahtarlar** → birincil yönetici anahtarı |

## Azure OpenAI'yi Doğrudan Çağıran Dersler için Ek Kurulum (Ders 6 ve 8)

Ders 6 ve 8'deki bazı noteboklar, doğrudan **Azure OpenAI**yı (Yanıtlar API'sini kullanarak) çağırır ve Microsoft Foundry projesinden geçmez. Bu örnekler önceden GitHub Modellerini kullandı, ancak bu kullanım sonlandırılmıştır (Temmuz 2026'da emekli olacak) ve Yanıtlar API'sini desteklemez. Bu örnekleri çalıştırmayı planlıyorsanız `.env` dosyanıza şu değişkenleri ekleyin:

| Değişken | Nerede bulunur |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → **Azure OpenAI** kaynağınız → **Anahtarlar ve Uç Nokta** → Uç Nokta (ör. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Yanıtlar API'sini destekleyen dağıtılmış modelinizin adı (ör. `gpt-5-mini`) |
| `AZURE_OPENAI_API_KEY` | Opsiyonel — `az login` / Entra ID yerine anahtar tabanlı kimlik doğrulaması kullanıyorsanız |

> Yanıtlar API, kararlı `/openai/v1/` uç noktasını kullanır, bu yüzden `api-version` gerekmez. Anahtarsız Entra ID kimlik doğrulaması için `az login` ile oturum açın.

## Alternatif Sağlayıcı: MiniMax (OpenAI Uyumlu)

[MiniMax](https://platform.minimaxi.com/) OpenAI uyumlu API üzerinden büyük bağlam modelleri sağlar (204K token'a kadar). Microsoft Agent Framework'ün `OpenAIChatClient` bileşeni herhangi bir OpenAI uyumlu uç noktada çalıştığı için MiniMax'ı Azure OpenAI veya OpenAI yerine kullanabilirsiniz.

`.env` dosyanıza şu değişkenleri ekleyin:

| Değişken | Nerede bulunur |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Anahtarları |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` olarak kullanın (varsayılan değer) |
| `MINIMAX_MODEL_ID` | Kullanılacak model adı (ör. `MiniMax-M3`) |

**Örnek modeller**: `MiniMax-M3` (önerilen), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (daha hızlı yanıtlar). Model adları ve mevcutluğu zamanla değişebilir ve belirli modellere erişim hesabınız veya bölgenize bağlı olabilir — güncel liste için [MiniMax Platform](https://platform.minimaxi.com/) kontrol edin. Eğer `MiniMax-M3` hesabınıza açık değilse, erişiminiz olan bir modeli `MINIMAX_MODEL_ID` olarak ayarlayın (örneğin `MiniMax-M2.7`).

`OpenAIChatClient` kullanan kod örnekleri (örneğin, Ders 14 otel rezervasyon iş akışı) `MINIMAX_API_KEY` ayarlandığında otomatik olarak MiniMax yapılandırmanızı algılar ve kullanır.

## Alternatif Sağlayıcı: Foundry Local (Modelleri Cihazda Çalıştır)

[Foundry Local](https://foundrylocal.ai), dil modellerini **tamamen kendi makinenizde** indirip yöneten, OpenAI uyumlu bir API ile servis eden hafif bir çalışma zamanı ortamıdır — bulut, Azure aboneliği veya API anahtarı gerekmez. Çevrimdışı geliştirme, bulut maliyetlerine maruz kalmadan deneme yapma ya da verileri cihazda tutmak için mükemmel bir seçenektir.

Microsoft Agent Framework'ün `OpenAIChatClient` bileşeninin herhangi bir OpenAI uyumlu uç noktada çalıştığı için Foundry Local, Azure OpenAI için bir yerel alternatif olarak kullanılabilir.

**1. Foundry Local Kurulumu**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Bir model indirip çalıştırın** (bu aynı zamanda yerel servisi başlatır):

```bash
foundry model list          # mevcut modelleri görüntüle
foundry model run phi-4-mini
```

**3. Yerel uç noktayı keşfetmek için kullanılan Python SDK'sını yükleyin:**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework'ü yerel modelinize yönlendirin:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Modeli yerel olarak indirir (gerekirse) ve sunar, ardından uç noktayı/portu keşfeder.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # örn. http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local için her zaman "not-required"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Not:** Foundry Local, OpenAI uyumlu **Chat Tamamlama** uç noktası sunar. Yerel geliştirme ve çevrimdışı senaryolar için kullanın. Tam **Yanıtlar API** özellik seti (durumsal konular, derin araç orkestrasyonu ve ajan tarzı geliştirme) için aşağıdaki derslerde gösterildiği gibi **Azure OpenAI** veya **Microsoft Foundry** projesini hedefleyin. Güncel model kataloğu ve platform desteği için [Foundry Local dokümantasyonuna](https://foundrylocal.ai) bakın.

## Ders 8 için Ek Kurulum (Bing Grounding İş Akışı)


Ders 8’deki koşullu iş akışı not defteri, Microsoft Foundry üzerinden **Bing temel alma** kullanır. Bu örneği çalıştırmayı planlıyorsanız, bu değişkeni `.env` dosyanıza ekleyin:

| Değişken | Nerede bulunur |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portalı → projeniz → **Yönetim** → **Bağlı kaynaklar** → Bing bağlantınız → bağlantı kimliğini kopyalayın |

## Sorun Giderme

### macOS’ta SSL Sertifika Doğrulama Hataları

macOS kullanıyorsanız ve şu tür bir hata alıyorsanız:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Bu, macOS’te Python ile bilinen bir sorundur; sistem SSL sertifikalarına otomatik olarak güvenilmez. Aşağıdaki çözümleri sırayla deneyin:

**Seçenek 1: Python'un Install Certificates betiğini çalıştırın (önerilir)**

```bash
# Yüklü Python sürümünüzle 3.XX'i değiştirin (örneğin, 3.12 veya 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Seçenek 2: Not defterinizde `connection_verify=False` kullanın (yalnızca GitHub Models not defterleri için)**

Ders 6 not defterinde (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), yorum satırı olarak bir geçici çözüm zaten mevcut. İstemci oluştururken `connection_verify=False` yorumunu kaldırın:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Sertifika hatalarıyla karşılaşırsanız SSL doğrulamasını devre dışı bırakın
)
```

> **⚠️ Uyarı:** SSL doğrulamasını devre dışı bırakmak (`connection_verify=False`) sertifika doğrulamasını atlayarak güvenliği azaltır. Bunu yalnızca geliştirme ortamlarında geçici bir çözüm olarak kullanın, üretimde asla kullanmayın.

**Seçenek 3: `truststore` kurun ve kullanın**

```bash
pip install truststore
```

Ardından, not defterinizin veya betiğinizin en üstüne, herhangi bir ağ çağrısı yapmadan önce şunu ekleyin:

```python
import truststore
truststore.inject_into_ssl()
```

## Bir Yerde Takıldınız mı?

Bu kurulumu çalıştırırken herhangi bir sorun yaşarsanız, <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> adresine katılın veya <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">bir sorun oluşturun</a>.

## Sonraki Ders

Bu kursun kodunu çalıştırmaya artık hazırsınız. AI Ajanlar dünyası hakkında daha fazla öğrenmenin tadını çıkarın!

[AI Ajanlara ve Ajan Kullanım Alanlarına Giriş](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->