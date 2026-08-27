# Örnek Makbuz Örnekleri

Defteri çalıştırmadan inceleme için önceden oluşturulmuş üç makbuz dosyası.

| Dosya | Nedir |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` aracı çağrısı için geçerli, imzalı bir makbuz. Doğrulama True döner. |
| `02_tampered_receipt.json` | İmzalandıktan sonra bir alanı değiştirilmiş aynı makbuz. Doğrulama False döner. |
| `03_chain_three_receipts.json` | Üç geçerli makbuzdan oluşan bir zincir (arama, tutma, rezervasyon) ve her biri bir öncekine bağlı `previous_receipt_hash` ile. |

Örnekler, yükün kanonik JCS baytlarını doğrudan Ed25519 ile imzalarlar.
SHA-256, içerik özetleri ve makbuz zinciri bağlantılarında kullanılmaya devam eder, imzadan önce
ekstra bir ön özet olarak değil.

## Örneklerin doğrulanması

Defter doğrulamayı dört bölümde açıklar. Bu örnekleri defter anlatısını çalıştırmadan
doğrudan doğrulamak için:

```python
import json
from pathlib import Path

# İçe aktarımları ve yardımcı fonksiyonları tamamladığınızı varsayar
# 18-signed-receipts.ipynb dosyasının 1. ve 2. bölümlerinden.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Doğru

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Yanlış

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Bunların nasıl oluşturulduğu

Örnekler, defterdeki ile aynı kod yolunu kullanır, sabit bir imzalama anahtarı
ve byte-tekrarlanabilirliği için sabit zaman damgaları vardır. Yeniden oluşturmak için:

```bash
python3 generate_fixtures.py
```

(Betik, bu dizindeki `generate_fixtures.py` dosyasındadır.)

## Öğrencilerin ham JSON'u inceleyerek öğrendikleri

Ham makbuz formatını okumak, defterdeki hücrelerin her zaman sağlamadığı bir sezgi oluşturur.
JSON'a hızlıca göz atan öğrenciler genellikle fark ederler ki:

1. İmza opak bir base64url dizisidir, ancak diğer tüm alanlar düz okunabilir JSON'dur.
   İmza içeriği şifrelemez; ona dair onay verir.
2. `public_key` makbuzun içine gömülüdür. Bir denetçi
   doğrulama için başka bir şeye ihtiyaç duymaz (anahtarın gerçekten iddia edilen
   yayıncıya ait olduğuna güvenmek şartıyla; kimlik altyapısı için ders README'sine bakınız).
3. Herhangi bir alanın tek bir karakterini değiştirip bu dosyayı
   `02_tampered_receipt.json` ile tekrar karşılaştırmak, bayt düzeyindeki mekanizmayı somutlaştırır.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->