---
name: jupyter-notebook
description: Kullanıcı deneyler, keşifler veya öğreticiler için Jupyter not defterleri
  (`.ipynb`) oluşturmasını, iskeletini hazırlamasını veya düzenlemesini istediğinde
  kullanın; birlikte gelen şablonları tercih edin ve temiz bir başlangıç not defteri
  oluşturmak için yardımcı betik `new_notebook.py`'yi çalıştırın.
---
# Jupyter Notebook Becerisi

İki birincil mod için temiz, yeniden üretilebilir Jupyter defterleri oluşturun:

- Deneyler ve keşifsel analiz
- Öğretici ve öğretim odaklı adım adım anlatımlar

Tutarlı yapı ve daha az JSON hatası için paketlenmiş şablonları ve yardımcı betiği tercih edin.

## Ne zaman kullanılmalı
- Yeni bir `.ipynb` defteri sıfırdan oluşturun.
- Kaba notları veya betikleri yapılandırılmış bir deftere dönüştürün.
- Mevcut bir defteri yeniden düzenleyerek daha yeniden üretilebilir ve okunması kolay hale getirin.
- Başkaları tarafından okunacak veya yeniden çalıştırılacak deneyler veya öğreticiler oluşturun.

## Karar ağacı
- Talep keşifsel, analitik veya hipotez odaklıysa `experiment` seçin.
- Talep öğretici, adım adım veya belirli bir kitleye yönelikse `tutorial` seçin.
- Mevcut bir defteri düzenliyorsanız, bunu bir yeniden düzenleme (refactor) olarak ele alın: niyeti koruyun ve yapıyı iyileştirin.

## Yetenek yolu (bir kez ayarlanır)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

Kullanıcı kapsamlı yetenekler `$CODEX_HOME/skills` altında yüklenir (varsayılan: `~/.codex/skills`).

## İş Akışı
1. Niyeti kesinleştirin.
Belirleyin defter türünü: `experiment` veya `tutorial`.
Hedefi, kitleyi ve "tamamlanmış" durumunun nasıl görüneceğini yakalayın.

2. Şablondan iskelet oluşturun.
Ham notebook JSON'unu elle yazmaktan kaçınmak için yardımcı betiği kullanın.

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb
```

3. Defteri küçük, çalıştırılabilir adımlarla doldurun.
Her kod hücresini tek bir adıma odaklı tutun.
Amacı ve beklenen sonucu açıklayan kısa markdown hücreleri ekleyin.
Kısa bir özet yeterliyse, büyük ve gürültülü çıktılardan kaçının.

4. Doğru deseni uygulayın.
Deneyler için şu belgeyi izleyin: `references/experiment-patterns.md`.
Öğreticiler için şu belgeyi izleyin: `references/tutorial-patterns.md`.

5. Mevcut defterlerle çalışırken güvenli düzenleme yapın.
Notebook yapısını koruyun; hücreleri baştan sona akışı iyileştirmiyorsa yeniden sıralamaktan kaçının.
Tam yeniden yazımlardan ziyade hedeflenmiş düzenlemeleri tercih edin.
Ham JSON'u düzenlemeniz gerekiyorsa önce şu belgeyi inceleyin: `references/notebook-structure.md`.

6. Sonucu doğrulayın.
Ortam izin verdiğinde defteri baştan sona çalıştırın.
Çalıştırma mümkün değilse bunu açıkça belirtin ve yerel olarak nasıl doğrulanacağını açıklayın.
Son kontrol listesini kullanın: `references/quality-checklist.md`.

## Şablonlar ve yardımcı betik
- Şablonlar `assets/experiment-template.ipynb` ve `assets/tutorial-template.ipynb` dizininde bulunur.
- Yardımcı betik bir şablonu yükler, başlık hücresini günceller ve bir defter yazar.

Betik yolu:
- `$JUPYTER_NOTEBOOK_CLI` (varsayılan kurulum: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Geçici ve çıktı kuralları
- Ara dosyalar için `tmp/jupyter-notebook/` kullanın; işiniz bittiğinde silin.
- Bu depo üzerinde çalışırken son ürünleri `output/jupyter-notebook/` altında yazın.
- Kararlı, açıklayıcı dosya adları kullanın (örneğin, `ablation-temperature.ipynb`).

## Bağımlılıklar (gerektiğinde yükleyin)
Bağımlılık yönetimi için `uv`'yi tercih edin.

Yerel defter çalıştırması için isteğe bağlı Python paketleri:

```bash
uv pip install jupyterlab ipykernel
```

Paketlenmiş iskelet betiği yalnızca Python standart kütüphanesini kullanır ve ek bağımlılık gerektirmez.

## Ortam
Gerekli ortam değişkeni yok.

## Referans haritası
- `references/experiment-patterns.md`: deney yapısı ve sezgisel kurallar.
- `references/tutorial-patterns.md`: öğretici yapısı ve öğretim akışı.
- `references/notebook-structure.md`: notebook JSON yapısı ve güvenli düzenleme kuralları.
- `references/quality-checklist.md`: son doğrulama kontrol listesi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Feragatname:
Bu belge, AI çeviri hizmeti Co-op Translator (https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki metin yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu tutulamayız.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->