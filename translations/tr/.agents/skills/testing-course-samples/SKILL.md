---
name: testing-course-samples
---
# Ders Örneklerini Test Etme

Ders defterlerinin ve kod örneklerinin canlı bir
Microsoft Foundry / Azure OpenAI kurulumu üzerinde çalıştığını doğrulayın. Depo,
her Python defterini başsız olarak çalıştıran ve PASS/FAIL matrisi yazdıran
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) adlı bir çalıştırıcı sağlar.

## Ne Zaman Kullanılır
- "Tüm defterleri / örnekleri Azure aboneliğime karşı doğrulamak için."
- "Paketleri yükselttikten veya modelleri değiştirdikten sonra kursu hızlıca test etmek için."
- "Hangi dersler canlı olarak hala geçiyor / başarısız oluyor?"

AI Smoke Test GitHub Action (yayınlanmış
barındırılan ajanları doğrulayan — bkz. [`tests/README.md`](../../../tests/README.md)) için **kullanmayın**. Bu beceri
defterleri yerel olarak çalıştırır.

## Ön Koşullar (önce kontrol edin)
1. **Python 3.12+** ve kurs bağımlılıkları: `python -m pip install -r requirements.txt`
   artı yürütücü: `python -m pip install nbconvert ipykernel`.
2. Depo kökünde **`.env`** dosyası ([`.env.example`](../../../../../.env.example) dosyasından kopyalayın) en az şunları içermeli:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry proje uç noktası
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — kullanım dışı olmayan bir dağıtım (ör. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) ve `AZURE_OPENAI_DEPLOYMENT`
     Azure OpenAI'yi doğrudan çağıran dersler için (Ders 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** tamamlanmış — örnekler `AzureCliCredential` ile kimlik doğrular (Entra ID, anahtarsız).
4. Model dağıtımının var olduğunu doğrulayın:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Doğrulamayı Çalıştırma
```powershell
# Tüm Python defterleri (.NET, .venv, site-packages, çeviriler, beceri varlıkları atlanır)
pwsh scripts/validate-notebooks.ps1

# Her hücre için daha uzun zaman aşımı olan tek bir ders
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Sadece çalıştırılacakları listele (çalıştırma yok)
pwsh scripts/validate-notebooks.ps1 -List

# Açık yorumlayıcı (örneğin `python` PATH'de değilse, Windows Store takma adı gibi)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Betik, çalıştırılan kopyaları, her-defter günlüklerini ve `results.json` dosyasını
`$env:TEMP\aiab-nbval` içine yazar ve başarısızlık sayısıyla çıkar.

Geçici hatalar (paylaşılan abonelik HTTP 429 hız sınırları, zaman zaman bir
`AzureCliCredential` belirteç sorunu veya zaman aşımı) otomatik olarak tekrar denenir
(`-Retries`, varsayılan 2, `-RetryDelaySeconds` geri çekilme ile, varsayılan 20). Eğer bir
model dağıtımı sürekli 429 alıyorsa, aboneliğin GlobalStandard
TPM kotasını kontrol edin (`az cognitiveservices usage list -l <region>`) — tek bir
dağıtım kapasitesini artırmak, *abonelik* kotası dolduğunda yardımcı olmaz.

## Sonuçları Yorumlama
- `PASS` — defter hücre hatası olmadan uçtan uca çalıştı.
- `FAIL` — ilk `*Error` / `*Exception` satırı gösterilir; tam yığın izleme için
  çıktı dizinindeki eşleşen `log_*.txt` dosyasını açın.
- Tek bir defter hatası `-Timeout` ile sınırlıdır (her hücre için), bu yüzden takılan
  insan-döngüsü hücresi takılmak yerine `StdinNotImplementedError` olarak görünür.

## Ek Kaynak Gerektiren Dersler (onlar olmadan başarısız olması beklenir)
| Ders | Ek Gereksinim |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, anahtar) — bir bellek içi geri dönüş yolu bulunur |
| 11 MCP / GitHub | GitHub MCP sunucusu + PAT |
| 13 memory (cognee) | Model sağlayıcı ile yapılandırılmış `cognee` |
| 15 browser-use | Playwright tarayıcıları kurulmuş (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Yerel çalışma zamanı + indirilen bir Qwen modeli (cihazda, bulut yok) |
| `*-dotnet-*` defterleri | .NET Interactive çekirdeği (varsayılan olarak hariç tutulur; `-IncludeDotnet` kullanın) |

## Geri Bildirim
Dersi baz alarak gruplandırılmış bir PASS/FAIL tablosu olarak özetleyin. Gerçek
gerilemeleri (düzeltilecek kod/yapılandırma hataları) ortam eksikliklerinden
(eksik Search/Foundry Local/PAT) ayırın ve her gerçek hata için başarısız olan `log_*.txt` dosyasına atıfta bulunun.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->