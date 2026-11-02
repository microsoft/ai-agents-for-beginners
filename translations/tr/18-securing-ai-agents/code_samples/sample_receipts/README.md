# Örnek Makbuz Araçları

Not defterini çalıştırmadan inceleme için önceden oluşturulmuş üç makbuz dosyası.

| Dosya | Nedir |
|---|---|
| `01_valid_receipt.json` | Bir `lookup_flights` aracı çağrısı için geçerli imzalı makbuz. Doğrulama True döner. |
| `02_tampered_receipt.json` | İmzalandıktan sonra bir alanı değiştirilmiş aynı makbuz. Doğrulama False döner. |
| `03_chain_three_receipts.json` | Önceki makbuza `previous_receipt_hash` ile bağlanan üç geçerli makbuz zinciri (ara, tut, rezervasyon). |

Araçlar, yüklemenin kanonik JCS baytlarını doğrudan Ed25519 ile imzalar.
SHA-256 içerik özetleri ve makbuz zinciri bağlantıları için kullanılır, imzadan önce ekstra bir
ön-özet olarak değil.

## Örneklerin doğrulanması

Not defteri doğrulamayı dört bölümde gösterir. Bu araçları doğrudan not defteri anlatımını
çalıştırmadan doğrulamak için:

```python
import json
from pathlib import Path

# İthalatları ve yardımcı fonksiyonları tamamladığınızı varsayar
# 18-signed-receipts.ipynb dosyasının 1. ve 2. bölümlerinden.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Doğru

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Yanlış

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Nasıl oluşturuldukları

Araçlar, not defteri ile aynı kod yolunu kullanır; sabit bir imzalama anahtarı
ve bayt tekrarlanabilirliği için sabit zaman damgalarıyla. Yeniden oluşturmak için:

```bash
python3 generate_fixtures.py
```

(Betik bu dizindeki `generate_fixtures.py` dosyasında.)

## Öğrencilerin ham JSON incelemesinden öğrendikleri

Ham makbuz formatını okumak, not defterindeki hücrelerin her zaman sağlamadığı sezgiyi geliştirir.
JSON'i hızlıca gözden geçiren öğrenciler genellikle şunları fark eder:

1. İmza opak bir base64url dizisidir, ancak diğer tüm alanlar düz okunabilir JSON'dur.
   İmza içeriği şifrelemez; ona tanıklık eder.
2. `public_key` makbuza gömülüdür. Bir denetçi, doğrulama yapmak için başka bir şeye gerek
   duymaz (anahtarın gerçekten iddia edilen yayıncıya ait olduğuna güvenmek koşuluyla;
   kimlik altyapısına ilişkin derse bakınız).
3. Herhangi bir alanın tek bir karakterini değiştirmek ve ardından bu dosyayla
   `02_tampered_receipt.json` dosyasını karşılaştırmak, bayt düzeyi mekanizmayı somutlaştırır.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->