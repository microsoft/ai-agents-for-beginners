# Örnek Makbuz Sabitleri

Not defterini çalıştırmadan inceleme için önceden oluşturulmuş üç makbuz dosyası.

| Dosya | Nedir |
|---|---|
| `01_valid_receipt.json` | Bir `lookup_flights` araç çağrısı için geçerli imzalı bir makbuz. Doğrulama True döner. |
| `02_tampered_receipt.json` | İmzalandıktan sonra bir alanı değiştirilmiş aynı makbuz. Doğrulama False döner. |
| `03_chain_three_receipts.json` | Birbirine ardışık üç geçerli makbuzdan (search, hold, book) oluşan bir zincir, her birini öncekine bağlayan `previous_receipt_hash` ile. |

Donanımlar, yükün kanonik JCS baytlarını doğrudan Ed25519 ile imzalar.
SHA-256, içerik özetleri ve makbuz zinciri bağlantıları için kullanılmaya devam eder, imzalamadan önce
ekstra bir ön-özet olarak değil.

## Örneklerin doğrulanması

`18-signed-receipts.ipynb` içinde önce Setup ve Bölüm 1'den 3'e kadar çalıştırın.
Bölüm 3 `verify_chain`'yı tanımlar; yalnızca Bölüm 1 ve 2 yeterli değildir.
Ardından aşağıdaki bloğu yeni bir hücrede, not defterinin çalışma dizini
`18-securing-ai-agents/code_samples` olarak ayarlanmış şekilde çalıştırın. Aşağıdaki fixture yolları
o dizine göre görecelidir.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# This fixture key is pinned by the verifier, outside the receipt under test.
FIXTURE_ISSUER_PUBLIC_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"
fixture_trusted_public_keys = {FIXTURE_ISSUER_PUBLIC_KEY}

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text())
print(
    f"Valid receipt: {verify_receipt(valid, fixture_trusted_public_keys)}"
)  # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text())
print(
    f"Tampered receipt: {verify_receipt(tampered, fixture_trusted_public_keys)}"
)  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text())
for r in verify_chain(chain, fixture_trusted_public_keys):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

### Jupyter olmadan örneğin kontrol edilmesi

Depo kökünden, ders bağımlılıklarını kurun ve çalıştırın:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Bu testler, not defterinin Python örneklerini ve yukarıdaki tam README bloğunu çalıştırır.
Ayrıca değiştirme ve sabitlenmemiş anahtarların doğrulayıcılar tarafından reddedildiğini kontrol ederler.
Testler, bağımlılıklar ayrı olarak yüklendiği için not defterinin `%pip` kurulum hücresini geçer.
Not defterini veya kısıtlamaları değiştirmezler.

## Bunlar nasıl üretildi

Sabitler not defteriyle aynı kod yolunu kullanır, ancak sabit bir imzalama anahtarı
ve bayt-uyumluluğu için sabit zaman damgalarıyla. Yeniden oluşturmak için:

```bash
python3 generate_fixtures.py
```

(Betik bu dizindeki `generate_fixtures.py` konumundadır.)

## Öğrencilerin ham JSON'ı inceleyerek öğrendikleri

Ham makbuz formatını okumak, not defterindeki hücrelerin her zaman sağlamadığı bir sezgi oluşturur.
JSON'a hızlıca bakan öğrenciler genellikle şunları fark eder:

1. İmza opak bir base64url dizisidir, ancak diğer tüm alanlar okunabilir sade JSON'dur.
   İmza içeriği şifrelemez; ona onay verir.
2. `public_key` makbuzda gömülüdür, bu kendi tutarlılığını kontrol etmek için yeterlidir, ancak
   düzenleyici güveni için yeterli değildir. Bir denetçi, makbuz dışında sabitlenmiş veya güvenilen bir kayıt
   aracılığıyla çözülmüş bir anahtarla karşılaştırmak zorundadır.
3. Herhangi bir alanın tek bir karakterini değiştirmek, sonra bu dosyayı
   `02_tampered_receipt.json` ile tekrar karşılaştırmak, bayt düzeyindeki mekanizmayı somutlaştırır.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->