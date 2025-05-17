# Kurs Kurulumu

## Giriş

Bu ders, bu kursun kod örneklerini nasıl çalıştıracağınızı kapsayacaktır.

## Gereksinimler

- Bir GitHub Hesabı  
- Python 3.12+  
- Azure Aboneliği  
- Azure AI Foundry Hesabı  

## Bu Repoyu Klonlama veya Forklama

Başlamak için lütfen GitHub Reposunu klonlayın veya fork’layın. Bu, kurs materyallerinin kendi sürümünüzü oluşturmanızı sağlar; böylece kodu çalıştırabilir, test edebilir ve değiştirebilirsiniz!

Bunu <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repoyu fork’lama</a> bağlantısına tıklayarak yapabilirsiniz.

Artık bu dersin kendi fork’lanmış sürümüne aşağıdaki bağlantıdan erişebilirsiniz:

![Forked Repo](./images/forked-repo.png)

## GitHub Kişisel Erişim Token’ınızı (PAT) Almak

Şu anda bu kurs, AI Ajanları oluşturmak için kullanılacak Üretken Dil Modellerine (LLM’lere) ücretsiz erişim sunmak üzere GitHub Models Marketplace’i kullanıyor.

Bu hizmete erişmek için bir GitHub Kişisel Erişim Token’ı oluşturmanız gerekecek.

Bunu GitHub hesabınızdaki <a href="https://github.com/settings/personal-access-tokens" target="_blank">Kişisel Erişim Token’ları ayarları</a> sayfasına giderek yapabilirsiniz.

Ekranın sol tarafında `Ince ayarlı token’lar (Fine-grained tokens)` seçeneğini işaretleyin.

Ardından `Yeni token oluştur (Generate new token)` seçeneğine tıklayın.

![Generate Token](./images/generate-token.png)

Yeni oluşturduğunuz token’ı kopyalayın. Bunu, bu kursla beraber gelen `.env` dosyanıza ekleyeceksiniz.

## Azure AI Foundry için `.env` Dosyanızı Ayarlama

`.env` dosyanızı oluşturmak için terminalde aşağıdaki komutu çalıştırın:

```bash
cp .env.example .env
````

Bu, örnek dosyayı kopyalayarak dizininizde bir `.env` oluşturur; ortam değişkenleri için değerleri buraya girin.

Aşağıda her değeri Azure AI Foundry’da, portalda veya ilgili diğer konumlarda nerede bulacağınızı görebilirsiniz.

### GitHub

* `GITHUB_TOKEN` – GitHub’da kişisel erişim token’ı oluşturun ve `.env` dosyanızdaki `GITHUB_TOKEN=` alanına yapıştırın.

### Genel Bakış Sayfası (Proje)

* `AZURE_SUBSCRIPTION_ID` – Projenizin **Genel Bakış (Overview)** sayfasındaki **Proje ayrıntıları (Project details)** bölümünde bulunur.
* `AZURE_AI_PROJECT_NAME` – Projenizin **Genel Bakış** sayfasının üst kısmında yer alır.
* `AZURE_OPENAI_SERVICE` – **Genel Bakış** sayfasında **Azure OpenAI Service** için **Dahil edilen yetenekler (Included capabilities)** sekmesinde bulunur.
* `PROJECT_CONNECTION_STRING` – **Genel Bakış** sayfasındaki **Proje ayrıntıları** bağlantısına gidip **Proje bağlantı dizesini** kopyalayın. Dizenin **https\://** ile başladığından ve **;** ile ayrılmış dört bölüm içerdiğinden emin olun. Şu an Azure AI Foundry’da başındaki **https\://** eksik olabilir.

### Yönetim Merkezi (Management Center)

* `AZURE_OPENAI_RESOURCE_GROUP` – **Yönetim Merkezi** **Genel Bakış** sayfasındaki **Proje özellikleri (Project properties)** bölümünde bulunur.
* `GLOBAL_LLM_SERVICE` – **Bağlı kaynaklar (Connected resources)** altında **Azure AI Services** bağlantı adını bulun. Listede değilse, Azure portalında ilgili kaynak grubunuz altındaki AI Services kaynak adını kontrol edin.

### Modeller + Uç Noktalar (Endpoints) Sayfası

* `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` – Gömmeli modelinizi (ör. `text-embedding-ada-002`) seçin ve model ayrıntılarından **Deployment name** değerini not edin.
* `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` – Sohbet modelinizi (ör. `gpt-4o-mini`) seçin ve model ayrıntılarından **Deployment name** değerini not edin.

### Azure Portal

* `AZURE_OPENAI_ENDPOINT` – **Azure AI services** kaynağınızı seçin, ardından **Kaynak Yönetimi (Resource Management)**, **Anahtarlar ve Uç Nokta (Keys and Endpoint)** bölümüne gidin, “Azure OpenAI endpoints” kısmından **Language APIs** uç noktasını kopyalayın.
* `AZURE_OPENAI_API_KEY` – Aynı ekrandan KEY 1 veya KEY 2’yi kopyalayın.
* `AZURE_SEARCH_SERVICE_ENDPOINT` – **Azure AI Search** kaynağınızı seçin ve **Genel Bakış** bölümünü kontrol edin.
* `AZURE_SEARCH_API_KEY` – Ardından **Ayarlar (Settings)** > **Anahtarlar (Keys)** bölümünden birincil veya ikincil yönetici anahtarını kopyalayın.

### Dış Web Sayfası

* `AZURE_OPENAI_API_VERSION` – [API sürüm yaşam döngüsü](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) sayfasındaki **Latest GA API release** bölümüne bakın.

## Gerekli Paketleri Yükleme

Gerekli Python paketlerini yüklemek için terminalde aşağıdaki komutu çalıştırın.

Herhangi bir çakışma ve soruna karşı bir Python sanal ortamı oluşturmanızı öneririz.

```bash
pip install -r requirements.txt
```

Bu, gerekli Python paketlerini yükleyecektir.

# Azure’a Giriş Yapma

Güvenlik en iyi uygulaması olarak, Azure OpenAI’ya Microsoft Entra Kimliği ile [anahtarsız kimlik doğrulama (keyless authentication)](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) kullanacağız. Bunu yapabilmek için önce işletim sisteminiz için [Azure CLI’yi yükleme talimatlarını](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=academic-105485-koreyst) izleyerek Azure CLI’yi kurmanız gerekmektedir.

Terminali açın ve Azure hesabınıza giriş yapmak için `az login` komutunu çalıştırın.

## Azure’a Giriş Yapma

Azure kaynaklarınızı oluşturmak için kullandığınız Azure AI hesabınızla giriş yapın.

Yeni bir terminal açın ve aşağıdaki komutu girip ekrandaki talimatları izleyin:

```bash
az login --use-device-code
```

Giriş yaptıktan sonra terminalde aboneliğinizi seçin.

## Ortam Değişkenlerine Erişim

Ortam değişkenlerine erişmek için `os` ve `load_dotenv` modüllerini içe aktaracağız.

```python
import os
from dotenv import load_dotenv

load_dotenv()
```

## Anahtarsız Kimlik Doğrulama Kurulumu

Kimlik bilgilerinizi doğrudan kodda yazmak yerine Azure OpenAI ile anahtarsız bağlantı kullanacağız. Bunun için `DefaultAzureCredential` modülünü içe aktaracak ve daha sonra `DefaultAzureCredential` fonksiyonunu çağıracağız.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

Artık bu kursun kodlarını çalıştırmaya hazırsınız; AI Ajanlar dünyasını keşfederken iyi öğrenmeler!

Herhangi bir sorun yaşarsanız, <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>’a katılabilir veya <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">bir issue oluşturabilirsiniz</a>.

## Sonraki Ders

[AI Ajanlarına Giriş ve Kullanım Örnekleri](../01-intro-to-ai-agents/README.md)


