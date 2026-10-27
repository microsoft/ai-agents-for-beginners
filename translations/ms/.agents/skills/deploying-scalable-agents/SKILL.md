---
name: deploying-scalable-agents
license: MIT
description: 'Membawa prototaip agen yang berfungsi ke pelaksanaan pengeluaran yang
  boleh diskala dan boleh diperhatikan di Microsoft Foundry. Meliputi corak pelaksanaan
  (agen dihoskan oleh pelanggan, agen dihoskan, aliran kerja agen), kitaran hayat
  agen, pengarahan model, penampan respons, pintu penilaian, kelulusan manusia dalam
  kitaran, kebolehamatan dengan OpenTelemetry, pengoptimuman kos, dan ujian asap agen
  yang dilaksanakan dengan tindakan Ujian Asap AI. Berdasarkan Pelajaran 16 AI Agents
  for Beginners. GUNA UNTUK: melaksanakan agen ke pengeluaran, menskala agen, agen
  yang dihoskan Microsoft Foundry, Perkhidmatan Agen Foundry, pengarahan model, penampan
  respons, pintu penilaian, pintu pelepasan, aliran kerja kelulusan manusia, kebolehamatan
  agen, penjejakan agen, pengoptimuman kos agen, ujian asap agen yang dihoskan, agen
  sokongan pelanggan pengeluaran. JANGAN GUNA UNTUK: membina agen pertama anda (mulakan
  dengan Pelajaran 01), menjalankan agen secara tempatan pada peranti (gunakan local-ai-agents
  / Pelajaran 17), penyediaan infrastruktur Azure yang tidak berkaitan dengan agen,
  sasaran pelaksanaan bukan Foundry.'
---
# Menyebarkan Ejen Skala dengan Microsoft Foundry

> Kemahiran pendamping untuk [Pelajaran 16 – Menyebarkan Ejen Skala](../../../16-deploying-scalable-agents/README.md).
> Gunakannya untuk membantu pelajar memindahkan ejen dari prototaip ke penyebaran pengeluaran yang skala dan dapat diperhatikan.
> Dasarkan setiap cadangan pada kandungan pelajaran dan
> buku nota yang boleh dijalankan; jangan mereka bentuk API Foundry.

## Pencetus

Aktifkan kemahiran ini apabila pelajar ingin:
- Menyebarkan ejen ke Microsoft Foundry sebagai **ejen dihoskan** dan jadikan ia versi/dapat diperhatikan.
- Pilih antara corak penyebaran **client-hosted, hosted-agent, dan agent-workflow**.
- Tambah **penghalaan model**, **pengepaman respons**, atau **konkuren terbatas** untuk mengawal kelewatan dan kos.
- Tambah **pintu penilaian** supaya versi ejen buruk tidak boleh dihantar.
- Tambah langkah **kelulusan manusia dalam gelung** untuk tindakan berisiko tinggi.
- Pasangkan ejen dengan penjejakan **OpenTelemetry** untuk pemerhatian pengeluaran.
- **Uji asap** ejen yang sudah disebarkan sebagai pintu cepat selepas penyebaran.

## Model mental teras

Ejen pengeluaran kebanyakannya adalah rangka operasi *sekeliling* model (~80%),
bukan model itu sendiri. Peta setiap cadangan kepada salah satu kebimbangan ini:

| Kebimbangan | Prototip → Pengeluaran |
|---------|------------------------|
| Penghosan | buku nota → perkhidmatan dihoskan versi |
| Identiti | `az login` anda → identiti terurus + RBAC berjangka |
| Keadaan | dalam memori → stor utas/memori di luar |
| Kegagalan | traceback → percubaan semula, sandaran, amaran |
| Kos | "beberapa sen" → jejak, laluan, cache, bajet |
| Kualiti | pemerhatian mata → pintu penilaian automatik |
| Kepercayaan | anda luluskan → dasar + manusia dalam gelung |

## Corak penyebaran (pilih satu, atau gabungkan)

1. **Client-hosted** — gelung penalaran berjalan dalam proses anda. Kawalan maksimum; anda memiliki skala/keadaan.
2. **Hosted agent (Perkhidmatan Ejen Foundry)** — Foundry menghoskan gelung, menyimpan utas, menguatkuasakan RBAC/keselamatan kandungan, menunjukkan ejen dalam portal. Kurang kawalan, jauh kurang permukaan operasi.
3. **Agent workflow** — pelbagai ejen/alatan disusun menjadi graf dengan percabangan, nod kelulusan, dan penanda checkpoint tahan lama.

## Kitaran hayat (gelung yang menghantar ejen)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**Penilaian luar talian adalah pintu, bukan perkara sampingan** — versi tidak dihantar
melainkan ia memenuhi ambang. Pemerhatian dalam talian memberi maklum balas kegagalan sebenar
ke set ujian luar talian.

## Pemegang skala dan kos (mengikut keutamaan)

1. **Saizkan model dengan betul** — gunakan model terkecil yang lulus pintu penilaian.
2. **Laluan mengikut kerumitan** — model kecil/pantas untuk permintaan mudah, model besar untuk penalaran sebenar (pengklasifikasi DIY atau Penghala Model Foundry).
3. **Cache** — layani permintaan hampir-serupa tanpa panggilan model.
4. **Reka bentuk tanpa keadaan + konkuren terbatas** — luarkan keadaan; cuba semula dengan penambahbaikan masa.

## Corak utama untuk ditiru

Tunjukkan pelajar kepada ini dari buku nota
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Pengendali permintaan**: cache → laluan mengikut kerumitan → jejak span → jalankan → cache.
- **Pintu penilaian**: skor set ujian luar talian; pulangkan `pass_rate >= threshold` dan hanya sebarkan jika benar.
- **Kelulusan manusia**: `@tool(approval_mode="always_require")` untuk tindakan seperti bayaran balik besar.
- **Penjejakan**: bungkus setiap permintaan dalam `tracer.start_as_current_span(...)` dan tetapkan atribut seperti `routed.model`, `customer.id`.

## Uji asap ejen yang sudah disebarkan

Selepas penyebaran, sahkan titik akhir benar-benar menjawab (penyebaran hijau masih boleh
senyap). Gunakan tindakan [Ujian Asap AI](https://github.com/marketplace/actions/ai-smoke-test)
melalui [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
dengan katalog dalam [`tests/`](../../../tests/README.md). Pelari POST setiap
arahan kepada `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
dan menegaskan teks balasan. Identiti memerlukan peranan **Pengguna Azure AI** pada
skop projek Foundry; audiens token mesti `https://ai.azure.com/`.

Lapiskan pintu: **ujian asap** (boleh capai/bertindak balas, setiap penyebaran) → **penilaian luar talian** (cukup baik untuk dihantar, sebelum promosi) → **penilaian dalam talian** (bagaimana ia berfungsi di dunia sebenar, berterusan).



## Kawalan perusahaan

- **RBAC**: beri setiap ejen dihoskan identiti terurus dengan keistimewaan paling rendah.
- **MCP dalam pengeluaran**: anggap setiap pelayan MCP sebagai sempadan tidak dipercayai — pin versi, skop identiti, sahkan output, had kadar, jangan dedahkan rahsia.

## Kawalan keselamatan untuk pembantu

- Utamakan corak canonik `FoundryChatClient(...)` + `provider.as_agent(...)` yang digunakan di seluruh kursus.
- Jangan janjikan hasil Azure langsung yang belum anda sahkan; sarankan aliran kerja ujian asap untuk mengesahkan penyebaran.
- Kekalkan nasihat penilaian dan kos bersama: penilaian menetapkan lantai kualiti, penghalaan/pengepaman mengekalkan kos dekat dengan lantai itu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->