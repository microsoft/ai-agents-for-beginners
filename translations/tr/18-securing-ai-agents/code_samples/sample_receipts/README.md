# Örnek Makbuz Düzenekleri

Defteri çalıştırmadan inceleme için üç önceden oluşturulmuş makbuz dosyası.

| Dosya | Ne olduğu |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` aracının çağrısı için geçerli imzalı bir makbuz. Doğrulama True döner. |
| `02_tampered_receipt.json` | İmzalandıktan sonra bir alanı değiştirilmiş aynı makbuz. Doğrulama False döner. |
| `03_chain_three_receipts.json` | Üç geçerli makbuzun (arama, tutma, rezervasyon) `previous_receipt_hash` ile her biri öncekine bağlanmış zinciri. |

## Örneklerin doğrulanması

Defter, doğrulamayı dört bölümde anlatır. Bu düzenekleri defter anlatımı olmadan doğrudan doğrulamak için:

```python
import json
from pathlib import Path

# İçe aktarmaları ve yardımcı fonksiyonları tamamladığınızı varsayar
# 18-signed-receipts.ipynb dosyasının 1 ve 2. bölümlerinden.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Doğru

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Yanlış

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Bunların nasıl oluşturulduğu

Düzenekler defterle aynı kod yolunu kullanır, sabit bir imzalama anahtarı
ve bayt yeniden üretilebilirliği için sabit zaman damgaları ile. Yeniden oluşturmak için:

```bash
python3 generate_fixtures.py
```

(Skript bu dizindeki `generate_fixtures.py` dosyasında.)

## Öğrenciler hammadde JSON’u inceleyerek ne öğrenir?

Hammadde makbuz formatını okumak, defter hücrelerinde her zaman sağlanmayan bir sezgi
kazandırır. JSON’u hızla gözden geçiren öğrenciler genellikle fark eder:

1. İmza opak bir base64url dizisidir, ancak diğer tüm alanlar okunabilir
   düz JSON’dur. İmza içeriği şifrelemez; ona doğruluk onayı verir.
2. `public_key` makbuzda gömülüdür. Bir denetçi doğrulama için başka bir şeye ihtiyaç
   duymaz (ancak anahtarın gerçekten iddia edilen vericiye ait olduğuna güvenmek gerekir;
   kimlik altyapısına ilişkin ders README’sine bakınız).
3. Herhangi bir alanın tek bir karakterini değiştirmek ve sonra bu dosyayı
   `02_tampered_receipt.json` ile karşılaştırmak, bayt düzeyindeki mekanizmayı somutlaştırır.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->