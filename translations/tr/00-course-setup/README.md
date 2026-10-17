# Kurs Kurulumu

## Giriş

Bu derste, bu kursun kod örneklerinin nasıl çalıştırılacağı ele alınacaktır.

## Diğer Öğrenenlere Katılın ve Yardım Alın

Depoyu klonlamaya başlamadan önce, kurulumda yardım almak, kursla ilgili sorularınızı sormak veya diğer öğrenenlerle bağlantı kurmak için [AI Agents For Beginners Discord kanalı](https://aka.ms/ai-agents/discord) katılın.

## Bu Depoyu Klonlayın veya Forklayın

Başlamak için lütfen GitHub Deposunu klonlayın veya forklayın. Bu, kodu çalıştırıp test edebilmeniz ve değiştirebilmeniz için kurs materyalinin kendi versiyonunuzu oluşturur!

Bu, <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">deposu forklamak</a> için bağlantıya tıklayarak yapılabilir.

Artık bu kursun aşağıdaki linkte kendi forklanmış versiyonuna sahip olmalısınız:

![Forklanmış Repo](../../../translated_images/tr/forked-repo.33f27ca1901baa6a.webp)

### Yüzeysel Klonlama (atölye çalışması / Codespaces için önerilir)

  > Tam depo geçmişi ve tüm dosyaları indirirken tam depo büyük olabilir (~3 GB). Sadece atölyeye katılıyorsanız veya sadece birkaç ders klasörüne ihtiyacınız varsa, yüzeysel klonlama (veya seyrek klonlama) çok daha az indirir.

#### Hızlı yüzeysel klonlama — minimal geçmiş, tüm dosyalar

Aşağıdaki komutlarda `<your-username>` yerini kendi fork URL'nizle (veya tercihiniz upstream URL ile) değiştirin.

Sadece en son commit geçmişini klonlamak için (küçük indirme):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Belirli bir şubeyi klonlamak için:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Kısmi (seyrek) klonlama — minimal blob + sadece seçilmiş klasörler

Bu, kısmi klonlama ve seyrek-checkout kullanır (Git 2.25+ gerektirir ve kısmi klonlama desteği olan modern Git önerilir):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Depo klasörüne gidin:

```bash
cd ai-agents-for-beginners
```

Sonra istediğiniz klasörleri belirtin (aşağıdaki örnek iki klasör gösterir):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Klonladıktan ve dosyaları doğruladıktan sonra, sadece dosyalara ihtiyacınız var ve alan açmak istiyorsanız (git geçmişi olmadan), depo meta verilerini silin (💀geri döndürülemez — tüm Git işlevselliğini kaybedersiniz):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces Kullanımı (yerel büyük indirmeleri önlemek için önerilir)

- Bu depo için [GitHub UI](https://github.com/codespaces) üzerinden yeni bir Codespace oluşturun.  

- Yeni oluşturulan Codespace terminalinde yukarıdaki yüzeysel/seyrek klonlama komutlarından birini çalıştırarak ihtiyaç duyduğunuz ders klasörlerini Codespace çalışma alanına getirin.
- İsteğe bağlı: Codespaces içinde klonladıktan sonra, ekstra alan açmak için .git klasörünü kaldırabilirsiniz (yukarıdaki kaldırma komutlarına bakın).
- Not: Depoyu doğrudan Codespaces'de açmayı tercih ederseniz (ekstra klonlama olmadan), Codespaces geliştirme konteyner ortamını kurar ve yine de ihtiyacınızdan fazla kaynak sağlayabilir.

#### İpuçları

- Düzenlama/commit yapmak istiyorsanız, klon URL'sini her zaman forkunuzla değiştirin.
- Daha sonra daha fazla geçmiş veya dosya ihtiyacınız olursa, onları alabilir veya sparse-checkout ayarlarını ek klasörleri dahil edecek şekilde değiştirebilirsiniz.

## Kodu Çalıştırma

Bu kurs, AI Ajanları oluşturmak için pratik yapabileceğiniz bir dizi Jupyter Defteri sunar.

Kod örnekleri, **Microsoft Agent Framework (MAF)** ile `FoundryChatClient` kullanır; bu, **Microsoft Foundry** aracılığıyla **Microsoft Foundry Agent Service V2** (Responses API) ile bağlantı kurar.

Tüm Python defterleri `*-python-agent-framework.ipynb` olarak etiketlenmiştir.

## Gereksinimler

- Python 3.12+
  - **NOT**: Python3.12 yüklü değilse, yüklediğinizden emin olun. Ardından requirements.txt dosyasından doğru sürümlerin yüklenmesi için python3.12 ile sanal ortam (venv) oluşturun.
  
    >Örnek

    Python venv dizini oluşturun:

    ```bash
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

- .NET 10+: .NET kullanan örnekler için, [.NET 10 SDK'sını](https://dotnet.microsoft.com/download/dotnet/10.0) veya daha yenisini yüklediğinizden emin olun. Ardından kurulu .NET SDK sürümünüzü kontrol edin:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Kimlik doğrulama için gereklidir. [aka.ms/installazurecli](https://aka.ms/installazurecli) adresinden yükleyin.
- **Azure Aboneliği** — Microsoft Foundry ve Microsoft Foundry Agent Service erişimi için.
- **Microsoft Foundry Projesi** — Dağıtılmış bir modele sahip proje (örneğin, `gpt-5-mini`). Aşağıdaki [Adım 1](#adım-1-bir-microsoft-foundry-projesi-oluşturun) bölümüne bakın.

Bu depo kökünde kod örneklerini çalıştırmak için gereken tüm Python paketlerini içeren bir `requirements.txt` dosyası bulunmaktadır.

Bunları depo kökünde terminalinizde aşağıdaki komutu çalıştırarak kurabilirsiniz:

```bash
pip install -r requirements.txt
```

Herhangi bir çakışma veya sorun yaşamamak için bir Python sanal ortamı oluşturmanızı öneririz.

## VSCode Kurulumu

VSCode içinde doğru Python sürümünü kullandığınızdan emin olun.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ve Microsoft Foundry Agent Service Kurulumu

### Adım 1: Bir Microsoft Foundry Projesi Oluşturun

Defterleri çalıştırmak için dağıtılmış bir modele sahip Microsoft Foundry **hub** ve **projesine** ihtiyacınız var.

1. [ai.azure.com](https://ai.azure.com) sitesine gidin ve Azure hesabınızla oturum açın.
2. Bir **hub** oluşturun (ya da mevcut birini kullanın). Bakınız: [Hub kaynakları genel bakış](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Hub içinde bir **proje** oluşturun.
4. **Models + Endpoints** → **Model dağıt** bölümünden bir model (örneğin, `gpt-5-mini`) dağıtın.

### Adım 2: Proje Uç Noktanızı ve Model Dağıtım Adını Alın

Microsoft Foundry portalındaki projenizden:

- **Proje Uç Noktası** — **Genel Bakış** sayfasına gidin ve uç nokta URL'sini kopyalayın.

![Proje Bağlantı Dizisi](../../../translated_images/tr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Dağıtım Adı** — **Models + Endpoints** bölümüne gidin, dağıttığınız modeli seçin ve **Dağıtım adı**nı not edin (örneğin, `gpt-5-mini`).

### Adım 3: `az login` ile Azure'a Giriş Yapın

Çoğu defter, `azure-identity` paketinden `AzureCliCredential` veya `DefaultAzureCredential` kullanarak **Azure CLI oturumu** ile kimlik doğrular — bu yüzden API anahtarı gerektirmezler. Bazı dersler ve isteğe bağlı entegrasyonlar API anahtarı kullanır; ilave ortam değişkenlerini kontrol etmek için her dersin önkoşullarını inceleyin. Bu, Azure CLI ile oturum açmanızı gerektirir.

1. Eğer yüklü değilse, **Azure CLI'yı yükleyin**: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Oturum açmak için** şu komutu çalıştırın:

    ```bash
    az login
    ```

    Veya tarayıcı olmadan uzak/Codespace ortamındaysanız:

    ```bash
    az login --use-device-code
    ```

3. İstenirse **aboneliğinizi seçin** — Foundry projenizi içeren aboneliği tercih edin.

4. **Oturumunuzun açık olduğunu doğrulayın:**

    ```bash
    az account show
    ```

> **Neden `az login`?** Defterler, `azure-identity` paketinden `AzureCliCredential` (veya `DefaultAzureCredential`, aynı zamanda Azure CLI oturumunuzu alır) kullanarak doğrulama yapar. Bu, Azure CLI oturumu kimlik bilgilerini sağlar — `.env` dosyanızda API anahtarı veya gizli bilgi bulunmaz. Bu bir [güvenlik en iyi uygulamasıdır](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Adım 4: `.env` Dosyanızı Oluşturun

Örnek dosyayı kopyalayın:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

`.env` dosyasını açın ve şu iki değeri doldurun:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Değişken | Nerede bulunur |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → projeniz → **Genel Bakış** sayfası |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → dağıtılan modelinizin adı |

Çoğu ders için bu kadar! Defterler `az login` oturumunuz üzerinden otomatik olarak kimlik doğrulaması yapar.

### Adım 5: Python Bağımlılıklarını Yükleyin

```bash
pip install -r requirements.txt
```

Bunu önceden oluşturduğunuz sanal ortam içinde çalıştırmanızı öneririz.

## İsteğe Bağlı Kurulum: Azure AI Search (5 ve 16. Dersler)

5. (Agentic RAG) ve 16. ders defterleri, ek bir Azure kaynağı gerektirmeyen bir **bellek içi bilgi tabanı** ile kutudan çıkar. Gerçek bir **Azure AI Search** indeksi ile desteklemek isterseniz, **16. ders defteri şu anda anahtarlı kimlik doğrulama kullanır**: Bellek içi aramadan Azure AI Search'e ancak **hem** `AZURE_SEARCH_SERVICE_ENDPOINT` **hem de** `AZURE_SEARCH_API_KEY` ayarlandığında geçer, aksi takdirde bellekte kalır — gerçek bir indekste çalıştırmak için yönetici anahtarını da ayarlamanız gerekir. Keyless kimlik doğrulama Microsoft Entra ID (RBAC) ile önerilen yoldur, bu kursun diğer yerlerinde kullanılan `az login` akışına uygundur.

Aşağıdaki RBAC adımları, kurulum kılavuzu örnekleri ve kendi kodunuz için geçerlidir. 16. ders defterinde anahtarsız kimlik doğrulamayı etkinleştirmez; 16. ders hala Azure AI Search kullanmak için hem uç noktayı hem de yönetici anahtarını gerektirir.

1. Arama hizmetinizde **rol tabanlı erişimi etkinleştirin**:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. Kendinize gerekli rolleri atayın (indeks oluşturmak ve sorgulamak için):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. Uç noktayı `.env` dosyanıza ekleyin:

| Değişken | Nerede bulunur |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → **Azure AI Search** kaynağınız → **Genel Bakış** → URL |
| `AZURE_SEARCH_API_KEY` | Ders 16 defterinde anahtarlı kimlik doğrulamayı etkinleştirmek (ve uç nokta ile birlikte gerekli). Azure portal → **Ayarlar** → **Anahtarlar** → birincil yönetici anahtarı |

> **Neden anahtarsız?** Yönetici anahtarları arama hizmetinize tam yazma erişimi verir ve `.env` dosyalarında sızabilir. RBAC ile bunun yerine `az login` kimliği kullanılır — kurs defterlerinde kullanılan aynı anahtarsız Entra ID modeli (`AzureCliCredential` / `DefaultAzureCredential`). Bakınız [Rollerle Azure AI Search'e bağlanma](https://learn.microsoft.com/azure/search/search-security-rbac).

Python ve .NET'te tam indeks oluşturma örnekleri için [Azure AI Search kurulum kılavuzuna](./AzureSearch.md) bakın.

## Doğrudan Azure OpenAI Çağıran Dersler için Ek Kurulum (6 ve 8. Dersler)

6 ve 8. derslerdeki bazı defterler, Microsoft Foundry projesi yerine **Azure OpenAI**'yi doğrudan (Responses API kullanarak) çağırır. Bu örnekler önceki GitHub Models kullanıyordu, bu yöntem eski ve Responses API'yi desteklemiyor. `.env` dosyanıza şu değişkenleri ekleyin:

| Değişken | Nerede bulunur |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → **Azure OpenAI** kaynağınız → **Anahtarlar ve Uç Nokta** → Uç Nokta (örn. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Responses API'yi destekleyen dağıtılmış model adı (örn. `gpt-5-mini`) |
| `AZURE_OPENAI_API_KEY` | İsteğe bağlı — anahtarlı kimlik doğrulama kullanıyorsanız `az login` / Entra ID yerine |

> Responses API stabil `/openai/v1/` uç noktasını kullanır, bu yüzden `api-version` gerekmez. Anahtarsız Entra ID kimlik doğrulaması için `az login` ile giriş yapın.

## Alternatif Sağlayıcı: MiniMax (OpenAI Uyumluluğu)

[MiniMax](https://platform.minimaxi.com/) büyük-kapsamlı modeller (204K token'a kadar) OpenAI uyumlu API ile sağlar. Microsoft Agent Framework'ün `OpenAIChatClient`'ı her OpenAI uyumlu uç nokta ile çalıştığından, MiniMax'i `OpenAIChatClient` kullanan dersler için drop-in alternatif olarak kullanabilirsiniz.

`.env` dosyanıza şu değişkenleri ekleyin:

| Değişken | Nerede bulunur |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platformu](https://platform.minimaxi.com/) → API Anahtarları |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` kullanın (varsayılan değer) |
| `MINIMAX_MODEL_ID` | Kullanılacak model adı (örn., `MiniMax-M3`) |

**Örnek modeller**: `MiniMax-M3` (önerilir), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (daha hızlı yanıt). Model isimleri ve erişimi zamanla değişebilir, kişisel hesabınıza bağlıdır.

`OpenAIChatClient` kullanan kod örnekleri (örn. Ders 14 otel rezervasyon akışı) `MINIMAX_API_KEY` ayarlandığında MiniMax yapılandırmanızı otomatik algılar ve kullanır.


## Alternatif Sağlayıcı: Novita AI (OpenAI-Uyumlu)

[Novita AI](https://novita.ai/llm-api), açık kaynaklı ve öncü LLM'ler (DeepSeek, Llama, Qwen ve daha fazlası) için OpenAI uyumlu bir API sağlar. Microsoft Agent Framework'ün `OpenAIChatClient`'ı herhangi bir OpenAI uyumlu uç noktasıyla çalıştığı için, Novita AI'yı Azure OpenAI veya OpenAI'a alternatif olarak kullanabilirsiniz.

Bu değişkenleri `.env` dosyanıza ekleyin:

| Değişken | Nerede bulunur |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Kontrol Paneli](https://novita.ai/settings/key-management) → API Anahtarları |
| `NOVITA_BASE_URL` | `https://api.novita.ai/openai/v1` kullanın (varsayılan değer) |
| `NOVITA_MODEL_ID` | Kullanılacak model adı (ör. `moonshotai/kimi-k3`) |

**Örnek modeller**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI ayrıca birçok başka açık kaynak model ailesine (Llama, Qwen, GLM ve daha fazlası) ev sahipliği yapar — mevcut modellerin ve model kimliklerinin güncel listesi için [Novita AI model kütüphanesi](https://novita.ai/llm-api) sayfasını kontrol edin.

Mevcut örnekler otomatik olarak `NOVITA_*` değişkenlerini kullanmaz. Novita AI'yı kullanmak için, çalıştırdığınız örnekte `OpenAIChatClient` yapılandırılırken bu değerleri açıkça geçin.

## Alternatif Sağlayıcı: Foundry Local (Modelleri Cihazda Çalıştırma)

[Foundry Local](https://foundrylocal.ai), dil modellerini **tamamen kendi bilgisayarınızda** indiren, yöneten ve OpenAI uyumlu bir API aracılığıyla sunan hafif bir çalışma zamanıdır — bulut gerektirmez.

Microsoft Agent Framework'ün `OpenAIChatClient`'ı herhangi bir OpenAI uyumlu uç noktasıyla çalıştığı için, Foundry Local yerel ve tak-çalıştır alternatif olarak Azure OpenAI'ın yerine geçer.

**1. Foundry Local'ı kurun**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Bir modeli indirip çalıştırın** (bu aynı zamanda yerel servisi başlatır):

```bash
foundry model list          # mevcut modelleri gör
foundry model run phi-4-mini
```

**3. Yerel uç noktayı keşfetmek için Python SDK'sını kurun:**

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
    api_key=manager.api_key,        # Foundry Local için her zaman "gerekli değil"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Not:** Foundry Local OpenAI uyumlu bir **Chat Completions** uç noktası sunar. Yerel geliştirme ve çevrimdışı senaryolar için kullanın. Tam **Responses API** özellik seti (durumlu konuşmalar vb.) için Azure OpenAI veya bir Microsoft Foundry projesini kullanın.

## Ders 8 İçin Ek Kurulum (Bing Grounding İş Akışı)

Ders 8'deki koşullu iş akışı defteri, Microsoft Foundry aracılığıyla **Bing grounding** kullanır. Bu örneği çalıştırmayı planlıyorsanız, `.env` dosyanıza şu değişkeni ekleyin:

| Değişken | Nerede bulunur |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portalı → projeniz → **Yönetim** → **Bağlantılı kaynaklar** → Bing bağlantınız → bağlantı kimliğini kopyalayın |

## Sorun Giderme

### macOS Üzerinde SSL Sertifika Doğrulama Hataları

Eğer macOS kullanıyorsanız ve şöyle bir hata alıyorsanız:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Bu, sistem SSL sertifikalarının otomatik olarak güvenilmediği macOS üzerindeki Python ile bilinen bir sorun. Aşağıdaki çözümleri sırasıyla deneyin:

**Seçenek 1: Python'un Sertifika Kurulum betiğini çalıştırın (önerilen)**

```bash
# Yüklü Python sürümünüzle 3.XX'i değiştirin (örneğin, 3.12 veya 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Seçenek 2: Not defterinizde `connection_verify=False` kullanın (yalnızca GitHub Modelleri not defterleri için)**

Ders 6 not defterinde (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) zaten yorum satırı halinde bir çözüm bulunmaktadır. Sertifika hatası aldığınızda `connection_verify=False` ifadesinin yorumunu kaldırın:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Sertifika hatalarıyla karşılaşırsanız SSL doğrulamasını devre dışı bırakın
)
```

> **⚠️ Uyarı:** SSL doğrulamasını devre dışı bırakmak (`connection_verify=False`), sertifika doğrulamasını atlayarak güvenliği azaltır. Bunu yalnızca geliştirme ortamlarında geçici çözüm olarak kullanın. Üretimde asla kullanmayın.

**Seçenek 3: `truststore` kurun ve kullanın**

```bash
pip install truststore
```

Ardından, ağ çağrısı yapmadan önce defterinizin ya da betiğinizin en üstüne aşağıdakini ekleyin:

```python
import truststore
truststore.inject_into_ssl()
```

## Bir Yerde Takıldınız Mı?

Bu kurulumu çalıştırmakta sorun yaşarsanız, <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Topluluk Discord</a> kanalımıza katılabilir veya <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">bir sorun oluşturabilirsiniz</a>.

## Sonraki Ders

Bu kursun kodunu çalıştırmaya hazırsınız. AI Ajanlar dünyası hakkında daha fazla öğrenirken bol şanslar!

[AI Ajanlarına ve Ajan Kullanım Senaryolarına Giriş](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->