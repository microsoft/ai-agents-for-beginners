# Ders Kurulumu

## Giriş

Bu ders, bu kursun kod örneklerini nasıl çalıştıracağınızı kapsayacak.

## Diğer Öğrencilerle Katılın ve Yardım Alın

Repo klonlamaya başlamadan önce, kurulumla ilgili yardım almak, kursla ilgili sorular sormak veya diğer öğrenenlerle bağlantı kurmak için [AI Agents For Beginners Discord kanalı](https://aka.ms/ai-agents/discord) sunucusuna katılın.

## Bu Depoyu Klonlayın veya Forklayın

Başlamak için lütfen GitHub deposunu klonlayın veya forklayın. Bu, kurs materyalinin kendi sürümünüzü oluşturacak ve böylece kodu çalıştırıp test edebilir ve değiştirebilirsiniz!

Bu, <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">depoyu fork'lamak</a> için bağlantıya tıklanarak yapılabilir.

Aşağıdaki bağlantıda artık bu kursun forklanmış kendi sürümünüz olmalıdır:

![Forklanmış Depo](../../../translated_images/tr/forked-repo.33f27ca1901baa6a.webp)

### Yüzeysel Klon (atölye / Codespaces için önerilir)

  > Tüm depo, tam geçmiş ve tüm dosyalar indirildiğinde büyük (~3 GB) olabilir. Sadece atölyeye katılıyorsanız veya yalnızca birkaç ders klasörüne ihtiyacınız varsa, geçmişi kısaltan ve/veya blob'ları atlayan yüzeysel bir klon (veya bir sparse clone) bu indirmenin çoğundan kaçınır.

#### Hızlı yüzeysel klon — minimum geçmiş, tüm dosyalar

Aşağıdaki komutlarda `<your-username>` kısmını fork URL'nizle (veya tercih ediyorsanız upstream URL'siyle) değiştirin.

Sadece en son commit geçmişini klonlamak için (küçük indirme):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Belirli bir dalı klonlamak için:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Kısmi (sparse) klon — minimum blob'lar + yalnızca seçilen klasörler

Bu, kısmi klon ve sparse-checkout kullanır (Git 2.25+ gerektirir ve kısmi klon desteği olan modern Git önerilir):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Repo klasörüne geçin:

```bash|powershell
cd ai-agents-for-beginners
```

Ardından hangi klasörleri istediğinizi belirtin (aşağıdaki örnek iki klasör gösterir):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Klonladıktan ve dosyaları doğruladıktan sonra, yalnızca dosyalara ihtiyacınız varsa ve alan açmak istiyorsanız (git geçmişi yok), depo meta verilerini silin (💀geri alınamaz — tüm Git işlevselliğini kaybedersiniz: commit'ler, pull'lar, push'lar veya geçmiş erişimi olmayacak).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces Kullanımı (yerel büyük indirmelerden kaçınmak için önerilir)

- Bu depo için yeni bir Codespace oluşturun via the [GitHub UI](https://github.com/codespaces).  

- Yeni oluşturulan codespace'in terminalinde, sadece ihtiyaç duyduğunuz ders klasörlerini Codespace çalışma alanına getirmek için yukarıdaki yüzeysel/sparse klon komutlarından birini çalıştırın.
- İsteğe bağlı: Codespaces içinde klonladıktan sonra ekstra alan kazanmak için .git'i kaldırın (yukarıdaki kaldırma komutlarına bakın).
- Not: Depoyu doğrudan Codespaces'te açmayı tercih ederseniz (ek bir klon yapmadan), Codespaces geliştirme konteyneri ortamını oluşturacak ve yine de ihtiyacınız olandan fazlasını sağlayabilir. Yeni bir Codespace içinde yüzeysel bir kopya klonlamak disk kullanımı üzerinde daha fazla kontrol sağlar.

#### İpuçları

- Düzenleme/commit yapmak istiyorsanız klon URL'sini her zaman fork'unuzla değiştirin.
- Daha sonra daha fazla geçmişe veya dosyaya ihtiyacınız olursa, bunları alabilir veya sparse-checkout'u ek klasörleri içerecek şekilde ayarlayabilirsiniz.

## Kodu Çalıştırma

Bu kurs, Yapay Zeka Ajanları oluşturma konusunda uygulamalı deneyim kazanmanız için çalıştırabileceğiniz bir dizi Jupyter Notebook sunar.

Kod örnekleri, `AzureAIProjectAgentProvider` ile **Microsoft Agent Framework (MAF)** kullanır; bu, **Microsoft Foundry** aracılığıyla **Azure AI Agent Service V2** (Responses API) ile bağlanır.

Tüm Python not defterleri `*-python-agent-framework.ipynb` olarak adlandırılmıştır.

## Gereksinimler

- Python 3.12+
  - **NOT**: Python3.12 yüklü değilse, lütfen yükleyin. Ardından requirements.txt dosyasından doğru sürümlerin kurulduğundan emin olmak için venv'inizi python3.12 ile oluşturun.
  
    >Örnek

    Python venv dizini oluşturun:

    ```bash|powershell
    python -m venv venv
    ```

    Ardından venv ortamını etkinleştirin:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET kullanan örnek kodlar için, lütfen [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) veya daha yenisini yükleyin. Ardından yüklü .NET SDK sürümünüzü kontrol edin:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Kimlik doğrulama için gereklidir. [aka.ms/installazurecli](https://aka.ms/installazurecli) adresinden yükleyin.
- **Azure Aboneliği** — Microsoft Foundry ve Azure AI Agent Service erişimi için.
- **Microsoft Foundry Projesi** — Dağıtılmış bir modele (ör. `gpt-4o`) sahip bir proje. Aşağıdaki [Adım 1](../../../00-course-setup) bölümüne bakın.

Bu depo kökünde çalıştırma için gerekli tüm Python paketlerini içeren bir `requirements.txt` dosyası ekledik.

Bunları depo kökünde terminalinizde aşağıdaki komutu çalıştırarak kurabilirsiniz:

```bash|powershell
pip install -r requirements.txt
```

Herhangi bir çakışma ve sorunları önlemek için bir Python sanal ortamı oluşturmanızı öneririz.

## VSCode Kurulumu

VSCode'da doğru Python sürümünü kullandığınızdan emin olun.

![resim](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ve Azure AI Agent Service Kurulumu

### Adım 1: Bir Microsoft Foundry Projesi Oluşturun

Not defterlerini çalıştırmak için dağıtılmış bir modele sahip bir Azure AI Foundry **hub** ve **project** gerekir.

1. [ai.azure.com](https://ai.azure.com) adresine gidin ve Azure hesabınızla oturum açın.
2. Bir **hub** oluşturun (veya mevcut bir hub'ı kullanın). bkz: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Hub içinde bir **project** oluşturun.
4. **Models + Endpoints** → **Deploy model** üzerinden bir model (ör. `gpt-4o`) dağıtın.

### Adım 2: Proje Uç Noktanızı ve Model Dağıtım Adını Alın

Microsoft Foundry portalındaki projenizden:

- **Project Endpoint** — **Overview** sayfasına gidin ve uç nokta URL'sini kopyalayın.

![Project Connection String](../../../translated_images/tr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** bölümüne gidin, dağıttığınız modeli seçin ve **Deployment name**'i not edin (ör. `gpt-4o`).

### Adım 3: `az login` ile Azure'a giriş yapın

Tüm not defterleri kimlik doğrulama için **`AzureCliCredential`** kullanır — yönetilecek API anahtarları yoktur. Bu, Azure CLI üzerinden oturum açmanızı gerektirir.

1. Henüz yüklü değilse **Azure CLI'yi yükleyin**: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Giriş yapın**:

    ```bash|powershell
    az login
    ```

    Veya tarayıcı olmayan uzak/Codespace ortamındaysanız:

    ```bash|powershell
    az login --use-device-code
    ```

3. Gerekirse aboneliğinizi seçin — Foundry projenizi içeren aboneliği seçin.

4. Oturum açtığınızı doğrulayın:

    ```bash|powershell
    az account show
    ```

> **Neden `az login`?** Not defterleri `azure-identity` paketinden `AzureCliCredential` kullanarak kimlik doğrulaması yapar. Bu, Azure CLI oturumunuzun kimlik bilgilerini sağladığı anlamına gelir — `.env` dosyanızda API anahtarları veya gizli bilgiler yoktur. Bu bir [güvenlik en iyi uygulamasıdır](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

`.env` dosyasını açın ve bu iki değeri doldurun:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Değişken | Nerede bulunur |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portalı → projeniz → **Overview** sayfası |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portalı → **Models + Endpoints** → dağıttığınız modelin adı |

Çoğu ders için bu kadar! Not defterleri `az login` oturumunuz aracılığıyla otomatik olarak kimlik doğrulaması yapacaktır.

### Adım 5: Python Bağımlılıklarını Kurun

```bash|powershell
pip install -r requirements.txt
```

Bunu daha önce oluşturduğunuz sanal ortam içinde çalıştırmanızı öneririz.

## Ders 5 için Ek Kurulum (Agentic RAG)

Ders 5, retrieval-augmented generation için **Azure AI Search** kullanır. Bu dersi çalıştırmayı planlıyorsanız, `.env` dosyanıza şu değişkenleri ekleyin:

| Değişken | Nerede bulunur |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portalı → **Azure AI Search** kaynağınız → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portalı → **Azure AI Search** kaynağınız → **Settings** → **Keys** → birincil yönetici anahtarı |

## Ders 6 ve Ders 8 için Ek Kurulum (GitHub Modelleri)

Ders 6 ve 8'deki bazı not defterleri Azure AI Foundry yerine **GitHub Models** kullanır. Bu örnekleri çalıştırmayı planlıyorsanız, `.env` dosyanıza şu değişkenleri ekleyin:

| Değişken | Nerede bulunur |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (varsayılan değer) |
| `GITHUB_MODEL_ID` | Kullanılacak model adı (ör. `gpt-4o-mini`) |

## Ders 8 için Ek Kurulum (Bing Grounding Workflow)

Ders 8'deki koşullu workflow not defteri, Azure AI Foundry üzerinden **Bing grounding** kullanır. Bu örneği çalıştırmayı planlıyorsanız, `.env` dosyanıza bu değişkeni ekleyin:

| Değişken | Nerede bulunur |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portalı → projeniz → **Management** → **Connected resources** → Bing bağlantınız → bağlantı kimliğini kopyalayın |

## Sorun Giderme

### macOS'te SSL Sertifika Doğrulama Hataları

macOS kullanıyorsanız ve aşağıdaki gibi bir hata alırsanız:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Bu, sistem SSL sertifikalarının otomatik olarak güvenilir olmadığı macOS üzerindeki Python ile bilinen bir sorundur. Aşağıdaki çözümleri sırasıyla deneyin:

**Seçenek 1: Python'ın Install Certificates betiğini çalıştırın (önerilir)**

```bash
# 3.XX'i yüklü Python sürümünüzle değiştirin (örn. 3.12 veya 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Seçenek 2: Not defterinizde `connection_verify=False` kullanın (yalnızca GitHub Models not defterleri için)**

Lesson 6 not defterinde (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) zaten yorumlanmış bir geçici çözüm bulunuyor. İstemci oluştururken `connection_verify=False` satırının yorumunu kaldırın:

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

Ardından ağ çağrısı yapmadan önce not defterinizin veya betiğinizin en üstüne aşağıdakini ekleyin:

```python
import truststore
truststore.inject_into_ssl()
```

## Bir Yerde Takıldınız mı?

Bu kurulumu çalıştırırken herhangi bir sorun yaşarsanız, <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Topluluğu Discord</a> sunucumuza katılın veya <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">bir sorun oluşturun</a>.

## Sonraki Ders

Bu kursun kodlarını çalıştırmaya hazırsınız. AI Ajanları dünyası hakkında daha fazlasını öğrenirken iyi öğrenmeler! 

[AI Ajanlarına Giriş ve Ajan Kullanım Durumları](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Feragatname:
Bu belge, yapay zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Kaynak dildeki orijinal belge yetkili/nihai kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanılması sonucu ortaya çıkabilecek herhangi bir yanlış anlaşılma veya yanlış yorumlama nedeniyle sorumluluk kabul etmiyoruz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->