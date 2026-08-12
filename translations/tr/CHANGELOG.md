# Değişiklik Günlüğü

**Yeni başlayanlar için AI Ajanları** kursundaki tüm önemli değişiklikler bu dosyada belgelenmiştir.

## [Yayınlandı] — 2026-07-14

Bu sürüm, kursu yeni kullanımdan kaldırılmış iki modelden çıkarır, kalan Ders defterlerini kararlı Microsoft Agent Framework API'sine taşır ve Python defterlerini canlı Microsoft Foundry dağıtımına karşı doğrular.

### Değiştirildi

- **Kullanımdan kaldırılmış modellerden çıktı (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Hem `gpt-4.1` hem de `gpt-4.1-mini` artık kullanımdan kaldırılmıştır (resmi emeklilik tarihi **14 Ekim 2026**). Kursun her referansı (dokümanlar, `.env.example`, Python/.NET defterleri ve örnekleri) kullanımdan kaldırılmamış `gpt-5-mini` ile değiştirildi. Ders 16'nın model yönlendirme örneği, `gpt-5-nano` (küçük) ve `gpt-5-mini` (büyük) kullanarak küçük/büyük kontrastı koruyor. Üçüncü taraf dosyaları ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), tarihi GitHub Modelleri metni ve `azure-openai-to-responses` beceri notları kasıtlı olarak değiştirilmedi.
- **Ders 14 devretme defteri kararlı API'ye taşındı.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) artık `agent_framework.orchestrations.HandoffBuilder` ile `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type` tabanlı akış ve kaldırılmış olan 1.0 öncesi `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` sembolleri yerine `FoundryChatClient` kullanıyor.
- **Ders 14 insan denetimli defter kararlı API'ye taşındı.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) artık `ctx.request_info(...)` + `@response_handler` ile duraklatıyor (kaldırılmış `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` yerine), `WorkflowBuilder(start_executor=..., output_executors=[...])` ile oluşturuluyor, yapılandırılmış çıktıyı `default_options={"response_format": ...}` kullanarak yönlendiriyor ve defterin engellemeyen `input()` olmadan gözetimsiz çalışması için betiklenmiş bir yanıt kullanıyor.
- **Ortam yapılandırması** ([.env.example](../../.env.example)): model dağıtım adları `gpt-5-mini` olarak değiştirildi; `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (Ders 16 yönlendirmesi) ve daha önce eksik olan `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (Ders 15 tarayıcı kullanımı) eklendi.
- **Bağımlılıklar** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry` ve `agent-framework-openai` `~=1.10.0` sürümüne sabitlendi, böylece tutarlı ve doğrulanmış bir set sağlandı (1.11.0, bu derslerin yüzeylerinde deneysel kırıcı değişiklikler içerir).

### Notlar ve bilinen sınırlamalar

- **Canlı Microsoft Foundry üzerinde doğrulandı.** Python defterleri, `gpt-5-mini` (ve Ders 16 yönlendirmesi için `gpt-5-nano`) kullanılan Microsoft Foundry projesine karşı `nbconvert` ile başsız olarak çalıştırıldı. Kendi projenizde kullanımdan kaldırılmamış eşdeğer modelleri dağıtın; defterler dağıtım adını `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`'dan okur.
- **Bazı dersler için hala ek kaynak gerekiyor.** Ders 05 Azure AI Search gerektirir; Ders 08 Bing-bağlantılı iş akışı (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) Bing bağlantısı ve Microsoft Foundry Agent Service barındırılan araçlar gerektirir; Ders 13 (Cognee) ve Ders 17 (Foundry Local) kendi çalışma zamanlarına ihtiyaç duyar.

## [Yayınlandı] — 2026-07-13

Bu sürüm, dağıtım aşamasını tamamlayan iki yeni ders ekler — ajanları Microsoft Foundry'ye ölçeklendirme ve tek bir iş istasyonuna küçültme — ayrıca bir duman testi hattı, yenilenmiş kurs navigasyonu, yeni öğrenen becerileri ve güncellenmiş marka öğeleri içerir.

### Eklendi

- **Ders 16 — Microsoft Foundry ile Ölçeklenebilir Ajanların Yayınlanması.** Yeni ders [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) ve çalışan defter [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) üretim müşteri destek ajanı yapımı (araçlar, RAG, bellek, model yönlendirme, yanıt önbellekleme, insan onayı, bir değerlendirme kapısı ve OpenTelemetry izleme), geliştirme/dağıtım/çalışma zamanı Mermaid diyagramları, bilgi kontrolü, bir ödev ve bir meydan okuma içerir.
- **Ders 17 — Foundry Local ve Qwen ile Yerel AI Ajanları Oluşturma.** Yeni ders [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) ve defter [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) tam anlamıyla cihazda çalışan mühendislik asistanı yapımı (Foundry Local üzerinden Qwen fonksiyon çağrısı, kum havuzu dosya araçları, yerel RAG Chroma ile, isteğe bağlı yerel MCP), sadece yerel / yerel-RAG / araç çağrısı diyagramları, bilgi kontrolü, bir ödev ve bir meydan okuma içerir.
- **Duman testi hattı.** Yeni [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) iş akışı [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) ve Ders 01, 04, 05 ve 16'da dağıtılabilir ajanlar için [tests/](./tests/README.md) altında ders katalogları, her kataloğu ders ve barındırılan ajan adıyla eşleyen bir dizin README. Ders 16 "Duman Testleri ile Dağıtılmış Bir Ajanın Doğrulanması" bölümüne kavuştu; Dersler 01/04/05 opsiyonel duman testi göstergesi aldı.
- **Öğrenen beceriler.** Yeni Ajan Becerileri `.agents/skills/` altında: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (Ders 16 ve 17 rehberini paketler) ve [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (defter örneklerini canlı Microsoft Foundry / Azure OpenAI kurulumu ile nasıl doğrulayacağınız).
- **Defter doğrulama çalıştırıcısı.** Her Python defterini `nbconvert` ile başsız olarak çalıştıran ve GEÇTİ/KALDI matrisi (ve `results.json`) yazdıran yeni [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1). Depo kökü ve Python otomatik algılanır, kurs dışı defterleri (`.venv`, `site-packages`, `translations`, beceri şablonu varlıkları) ve `.NET` defterleri varsayılan olarak hariç tutar, ayrıca `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` ve `-Python` destekler.
- **Kurs navigasyonu.** Ders 11-15'e Önceki/Sonraki ders bağlantıları eklendi (önceden yoktu), böylece tüm kurs 00 → 18 arasında çift yönlü zincir haline geldi.
- **Yeni küçük resimler.** Ders 16 ve 17 için küçük resimler ve yenilenmiş bir depo sosyal görseli [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (şimdi iki yeni ders ve `aka.ms/ai-agents-beginners` URL'si reklamını yapıyor).
- **Bağımlılıklar** ([requirements.txt](../../requirements.txt)): Ders 17 için `foundry-local-sdk` ve `chromadb` eklendi.

### Değiştirildi

- **Ana [README.md](./README.md)** ders tablosu: Ders 16 ve 17 artık içeriklerine bağlanıyor (önceden "Yakında"); depo görseli `repo-thumbnailv3.png` olarak güncellendi.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: Ders 16 ve 17 ders rehberine ve öğrenme yollarına eklendi, ayrıca "Duman Testleri ile Dağıtılmış Ajanları Doğrulama" bölümü eklendi.
- **[AGENTS.md](./AGENTS.md)**: ders sayısı/açıklaması (00–18) güncellendi, duman testi doğrulama bölümü eklendi ve Ders 16/17 örnek adlandırma örnekleri eklendi.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Önceki Ders" artık Ders 17'yi gösterir (önceden Ders 15 idi), zinciri kapatır.
- **Kullanımdan kaldırılmamış modellerde standart model referansları.** Tüm `gpt-4o` / `gpt-4o-mini` referansları kurs genelinde (dokümanlar, `.env.example`, Python/.NET defterleri ve örnekler) `gpt-4.1-mini` ile değiştirildi — `gpt-4o` (tüm sürümler) 2026'da kullanımdan kaldırılıyor. Ders 16'nın model yönlendirme örneği küçük/büyük kontrastı `gpt-4.1-mini` (küçük) ve `gpt-4.1` (büyük) kullanarak koruyor. Python defterleri artık model adını ortam değişkenlerinden (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) seçiyor, sabit yazılmış model adı kullanmıyor.

### Notlar ve bilinen sınırlamalar

- **Canlı Azure üzerinde çalıştırılmadı.** Yeni derslerin defterleri eğitim örnekleridir; bunları kendi Microsoft Foundry / Foundry Local kurulumunuzda çalıştırın ve doğrulayın. Duman testi iş akışı, ders ajanını dağıtmanızı ve Azure OIDC sırlarını (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) Foundry proje kapsamı seviyesinde **Azure AI Kullanıcı** rolü ile yapılandırmanızı gerektirir.
- **Ders 17 sadece yerel.** Foundry Responses uç noktası yoktur, bu yüzden duman testi eylemi uygulanmaz; defteri iş istasyonunuzda çalıştırarak doğrulayın.

## [Yayınlandı] — 2026-07-06

Bu sürüm, kursu **Azure OpenAI Responses API**'ye taşır, ürün adlandırmasını **Microsoft Foundry** ve **Microsoft Agent Framework (MAF)**'a standartlaştırır, GitHub Modelleri kullanımdan kaldırır, SDK sürümlerini günceller ve yerel modeller ve Foundry üzerinde diğer çerçeveleri barındırma hakkında yeni içerik ekler.

### Eklendi

- **Geçiş becerisi** — [.agents/skills/](../../.agents/skills) altında [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (Azure-Samples/azure-openai-to-responses'dan) yüklendi; referansları ve tarayıcı betiği dahil.
- **Foundry Local (modelleri cihazda çalıştırır)** — [00-course-setup/README.md](./00-course-setup/README.md) içinde yeni "Alternatif Sağlayıcı: Foundry Local" bölümü, kurulum (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` ve Microsoft Agent Framework'e `OpenAIChatClient` üzerinden bağlanmayı kapsar.
- **Microsoft Foundry üzerinde LangChain / LangGraph ajanlarını barındırma** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) içinde yeni bir bölüm ve çalıştırılabilir örnek [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), `langchain-azure-ai[hosting]` ve `/responses` protokolü kullanan `ResponsesHostServer` tabanlı; [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) referanslı.
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) içinde yeni "Gerçek Dünya Örneği: Microsoft Project Opal" bölümü; Opal'ı kurumsal bilgisayar kullanım ajanı olarak çerçeveler ve kurs kavramlarına (insan denetimli, güvenlik, planlama, Beceriler) eşler.
- **İkinci Ders 02 Python örneği** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) eklendi (bakınız "Değiştirildi" — eski Semantic Kernel defterinden taşındı) ve ders README'sine bağlandı.
- **Modeller ve Sağlayıcılar** bölümü [STUDY_GUIDE.md](./STUDY_GUIDE.md)'ye eklendi.

### Değiştirildi

- **Chat Completions → Responses API (Python).** Modele doğrudan güncelleme yapan örnekler Chat Completions'tan Responses API'ye taşındı (`client.responses.create(input=..., store=False)`, `resp.output_text`), kararlı Azure OpenAI `/openai/v1/` (api_version olmadan) uç noktasında `OpenAI` istemcisi kullanılarak. Etkilenen örnekler:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — tam fonksiyon çağırma anlatımı (araç şeması Responses formatına düzleştirildi, araç sonuçları `function_call_output`, `max_output_tokens` vb. olarak döndü).

- **GitHub Modelleri → Azure OpenAI.** GitHub Modelleri kullanımdan kaldırılmıştır (Temmuz 2026'da emekliye ayrılacak) ve Yanıtlar API'sini desteklememektedir. Tüm GitHub Modelleri kod yolları Python ve .NET örneklerinde Azure OpenAI / Microsoft Foundry ile dönüştürülmüştür:
  - Python: Ders 08 iş akışı defterleri (`01`–`03`), Ders 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + eşlik eden `.md` belgeleri ve Ders 08 dotNET iş akışı defterleri/`.md` (`01`–`03`) artık `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` ile `AzureCliCredential` kullanmaktadır.
- **Semantic Kernel → Microsoft Agent Framework.** Önceki `02-semantic-kernel.ipynb` Microsoft Agent Framework ve Azure OpenAI (Yanıtlar API) kullanacak şekilde yeniden yazıldı ve `02-python-agent-framework-azure-openai.ipynb` olarak yeniden adlandırıldı.
- **`FoundryChatClient` + `as_agent` ile standartlaştırıldı.** `AzureAIProjectAgentProvider` referansları içeren README ve defter kodları, Ders 01 ve framework'un kendi örneklerinde kullanılan kanonik desene göre standart hale getirildi: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` ile `provider.as_agent(...)`. Ders 02–14 README'leri ve defterlerinde güncellendi (örn. Ders 13 hafıza, tüm Ders 14 defterleri, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Ürün isimlendirmesi.** İngilizce içerik boyunca yeniden adlandırıldı:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Değişmeden: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" ve ortam değişkeni isimleri.)
- **Bağımlılıklar** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` sabitlendi.
  - `openai>=1.108.1` (Yanıtlar API için minimum) sabitlendi.
  - `azure-ai-inference` kaldırıldı (sadece taşınan GitHub Modelleri örneklerinde kullanılıyordu).
- **Ortam yapılandırması** ([.env.example](../../.env.example)): GitHub Modelleri değişkenleri (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) kaldırıldı; `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` ve isteğe bağlı `AZURE_OPENAI_API_KEY` eklendi; Microsoft Foundry isimlendirmesine güncellendi.
- **Belgeler** — Yukarıdakiler için [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) ve [STUDY_GUIDE.md](./STUDY_GUIDE.md) güncellendi (ortam değişkenleri ayarı, doğrulama kod parçası, sağlayıcı rehberi, isimlendirme).

### Kaldırıldı

- Kurulum belgelerinden GitHub Modelleri onboarding adımları ve ortam değişkenleri (Azure OpenAI / Microsoft Foundry ile değiştirildi).

### Güvenlik / Gizlilik (genel paylaşım temizliği)

- Gerçek bir **Azure abonelik kimliği**, kaynak-grup / kaynak adları ve Bing bağlantı kimliği ile birlikte geliştirici **yerel dosya yolları ve kullanıcı adlarını** sızdıran Jupyter defteri çalıştırma çıktıları temizlendi:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- İzlenen İngilizce içerikte API anahtarı, token, abonelik kimliği veya kişisel yol kalmadığı doğrulandı (`GITHUB_TOKEN` referansları GitHub Actions token'ı ve Ders 11 kurulumundaki GitHub MCP sunucu PAT'i olup, her ikisi de yasal ve GitHub Modelleri ile ilgisizdir).

### Notlar ve bilinen sınırlamalar

- **Çalıştırılmadı/derlenmedi.** Bunlar API/isimlendirme doğruluğu için güncellenmiş eğitim örnekleridir; canlı Azure kaynaklarına karşı çalıştırılmamış ve .NET örnekleri bu ortamda derlenmemiştir. Kendi Microsoft Foundry / Azure OpenAI kurulumunuzla doğrulayın.
- **Model dağıtımı Yanıtlar API'sini desteklemelidir.** `gpt-4.1-mini`, `gpt-4.1` veya bir `gpt-5.x` modeli gibi bir dağıtım kullanın. Daha eski modeller temel Yanıtlar işlevselliğini destekler ancak her özelliği değil.
- **Agent-framework sürümü.** Örnekler en son MAF (`>=1.10.0`) hedeflemektedir. Kanonik ajan oluşturma çağrısı `client.as_agent(...)`'dır; API'ler framework'ün yayımlanmış belgelerine ve yüklü derlemeye karşı doğrulanmıştır. Farklı bir sürüm sabitlerseniz, yöntemin kullanılabilirliğini doğrulayın (`as_agent` ile `create_agent` arasında).
- **Ders 08 iş akışı defteri 04** kasıtlı olarak `AzureAIAgentClient`'i (`agent-framework-azure-ai`'den) tutar çünkü Microsoft Foundry Agent Service barındırılan araçları (Bing temel alınması, kod yorumlayıcı) kullanır; halihazırda Yanıtlar tabanlıdır.
- **.NET varsayılan dağıtımı.** İki Ders 08 dotNET iş akışı örneği önceden belirli bir modeli sabitlemişti; artık varsayılan olarak `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) kullanıyor. Bir örnek multimodal/görüntü girişine bağımlıysa, `AZURE_OPENAI_DEPLOYMENT`'ı uygun bir modele ayarlayın.
- **Foundry Local** OpenAI uyumlu bir **Chat Completions** uç noktası sunar ve yerel geliştirme içindir; tam Yanıtlar API özellikleri için Azure OpenAI / Microsoft Foundry kullanın.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->