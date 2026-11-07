# Örnek Makbuz Sabitleri

Not defterini çalıştırmadan inceleme için dört önceden oluşturulmuş makbuz dosyası.

| Dosya | Nedir |
|---|---|
| `01_valid_receipt.json` | Bir `lookup_flights` araç çağrısı için geçerli, imzalanmış bir makbuz. Doğrulama True döner. |
| `02_tampered_receipt.json` | İmzalandıktan sonra bir alanı değiştirilmiş aynı makbuz. Doğrulama False döner. |
| `03_chain_three_receipts.json` | Üç geçerli makbuzdan oluşan bir zincir (arama, tutma, kitap), her biri öncekine bağlayan `previous_receipt_hash` ile. |
| `04_resigned_receipt.json` | Aynı makbuz, bir saldırgan tarafından tahrif edilmiş ve sonra saldırganın kendi genel anahtarı gömülü şekilde yeniden imzalanmış. İçindeki anahtara karşı doğrulanır. Düzenleyenin anahtarına karşı başarısız olur. |

Örnekler, yükün kanonik JCS baytlarını doğrudan Ed25519 ile imzalar.
SHA-256, içerik özetleri ve makbuz zinciri bağlantıları için kullanılmaya devam eder, imzalamadan önce ekstra bir ön özet olarak değil.


## Örneklerin doğrulanması

`18-signed-receipts.ipynb` içinde önce Kurulum ve Bölümler 1'den 3'e kadar çalıştırın.
Bölüm 3 `verify_chain` tanımlar; sadece Bölümler 1 ve 2 yeterli değildir.
Ardından, dizüstü bilgisayarın çalışma diziniyle yeni bir hücrede aşağıdaki bloğu çalıştırın
`18-securing-ai-agents/code_samples` olarak ayarlandı. Aşağıdaki test dosyası yolları görecelidir
o dizine.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# The issuer's key, pinned here rather than read from any receipt. In a real
# deployment it comes from the issuer's JWK Set or a pinned config value.
# This is the public half of the fixed signing key in generate_fixtures.py.
ISSUER_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text(encoding="utf-8"))
print(f"Valid receipt: {verify_receipt(valid, ISSUER_KEY)}")        # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text(encoding="utf-8"))
print(f"Tampered receipt: {verify_receipt(tampered, ISSUER_KEY)}")  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text(encoding="utf-8"))
for r in verify_chain(chain, ISSUER_KEY):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")

# The forgery. Verified against the key it carries, it passes. Against the
# issuer's key, it fails. Only the second question is worth asking.
forged = json.loads((fixture_dir / "04_resigned_receipt.json").read_text(encoding="utf-8"))
print(f"Forged, checked against its own key: "
      f"{verify_receipt(forged, forged['signature']['public_key'])}")  # True
print(f"Forged, checked against issuer key:  "
      f"{verify_receipt(forged, ISSUER_KEY)}")                        # False
```

### Jupyter olmadan örneği kontrol etme

Depo kökünden, ders bağımlılıklarını kurun ve çalıştırın:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Bu testler, defterin Python örneklerini ve yukarıdaki tam README bloğunu çalıştırır.
Ayrıca, doğrulayıcılar tarafından değiştirilmiş ve sabitlenmemiş anahtarların reddedildiğini kontrol eder.
Testler, bağımlılıklar ayrı olarak kurulduğu için defterin `%pip` kurulum hücresini atlar.
Defteri veya sabitleyicileri değiştirmezler.

## Bunlar nasıl oluşturuldu

Test verileri, aynı imzalama anahtarı
ve byte tekrar üretilebilirliği için sabit zaman damgaları ile defterle aynı kod yolunu kullanır. Yeniden oluşturmak için:

```bash
python3 generate_fixtures.py
```

(Betik bu dizindeki `generate_fixtures.py` içinde.)

`../test_signed_receipts.py` bunu otomatik olarak kontrol eder: çalıştırır
defterin kodu, bu dört düzeneği defterin
`verify_receipt` ve `verify_chain` ile doğrular ve düzeneği yeniden oluşturmanın
aynı baytları verdiğini onaylar. `code_samples`'ten:

```bash
python -m unittest test_signed_receipts
```

## Öğrencilerin ham JSON'u inceleyerek öğrendikleri

Ham makbuz formatını okumak, defterdeki hücrelerin her zaman sağlamadığı sezgiyi geliştirir.
JSON'a göz atan öğrenciler genellikle şunları fark eder:

1. İmza opak bir base64url dizesidir, ancak diğer tüm alanlar düz okunabilir JSON'dur.
   İmza içeriği şifrelemez; ona bağlı olduğunu onaylar.
2. `public_key` fişin içine gömülüdür, bu da dosyanın
   kendi içinde tamamlayıcı olmasını sağlar ancak bir denetçinin doğruladığı şey bu değildir. Karşılaştırınız
   `02_tampered_receipt.json` ile `04_resigned_receipt.json`: her ikisi de
   imzalandıktan sonra değiştirilmiştir, ancak ikincisi saldırganın
   kendi anahtarıyla tekrar imzalandığı için, yanındaki anahtara göre doğrulanır. Gömülü anahtar
   dosyanın dahili olarak tutarlı olduğunu gösterir. Kimin verdiğini ise
   sadece başka bir yerden elde edilen anahtar söyleyebilir.
3. `signature` dışındaki herhangi bir alanın tek bir karakterini değiştirmek, sonra
   bu dosyayı `02_tampered_receipt.json` ile karşılaştırmak,
   bayt seviyesindeki mekanizmayı somutlaştırır.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->