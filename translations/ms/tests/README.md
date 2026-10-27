# Ujian Asap Ejen

Folder ini memegang **katalog ujian asap** untuk ejen yang anda bina dalam kursus.
Ujian asap adalah pemeriksaan yang murah dan pantas bahawa **ejen yang dihoskan Microsoft Foundry yang
telah dikerahkan** boleh dicapai, memberi respons, dan mengikuti jangkaan
arahan paling asasnya. Ia adalah pintu gerbang pertama — bukan pengganti bagi
saluran penilaian penuh yang anda pelajari dalam [Pelajaran 10](../10-ai-agents-production/README.md) dan
[Pelajaran 16](../16-deploying-scalable-agents/README.md).

Katalog digunakan oleh [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action melalui aliran kerja [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml).


## Cara menjalankan

1. **Kerahkan ejen pelajaran** ke Microsoft Foundry sebagai ejen yang dihoskan (lihat
   Pelajaran 16 untuk aliran kerja penyebaran). Nota **nama ejen** dan
   **titik hujung projek Foundry** anda.
2. Tambah rahsia repositori ini (Tetapan → Rahsia dan pembolehubah → Tindakan):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Pengenalan persekutuan
   memerlukan peranan **Pengguna Azure AI** pada **skop projek Foundry**.
3. Dari tab **Tindakan**, jalankan **Ujian-asap ejen dihoskan** dan pilih
   `tests_file` untuk pelajaran itu, kemudian beri `agent_name` dan
   `project_endpoint` yang sepadan.

## Katalog → pelajaran → nama ejen

| Katalog | Pelajaran | Kerahkan ejen sebagai |
|---------|-----------|----------------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Pengenalan kepada Ejen AI](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Penggunaan Alat](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – RAG Ejenik](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Mengkerahkan Ejen Skala Besar](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Pelajaran mana yang ada ujian asap?

Ujian asap digunakan pada pelajaran di mana anda **kerahkan ejen** yang maklum balas teksnya boleh
disahkan terhadap kandungan yang diketahui. Pelajaran yang bersifat konsep, hanya dijalankan secara tempatan,
atau menghasilkan output kreatif tak tentukan sengaja dikecualikan:

- **Pelajaran 17 (Membina Ejen AI Tempatan)** dijalankan sepenuhnya di stesen kerja anda dengan
  Foundry Local dan **tidak** mendedahkan titik hujung Tindak Balas Foundry, jadi
  tindakan ini tidak terpakai. Sahkan dengan menjalankan buku nota secara tempatan.
- Pelajaran corak-reka dan teori (02, 03, 06, 07, 09, 12) tidak membekalkan apa-apa
  ejen yang boleh dikerahkan untuk ujian asap.

## Skema katalog (rujukan pantas)

Setiap katalog adalah dokumen JSON dengan tatasusunan `tests` di peringkat atas. Setiap entri POST
satu arahan dan menegaskan balasan:

| Medan | Maksud |
|-------|--------|
| `id` | Pengecam langkah unik yang dicetak dalam log. |
| `description` | Tujuan yang boleh dibaca manusia. |
| `prompt` | Mesej yang dihantar ke ejen. |
| `assertions.status` | Status HTTP yang dijangka (lalai 200). |
| `assertions.contains_any` | Lulus jika balasan mengandungi mana-mana substring ini. |
| `assertions.contains_all` | Lulus jika balasan mengandungi setiap substring. |
| `assertions.contains_none` | Lulus jika balasan tidak mengandungi mana-mana substring ini. |
| `save_response_id_as` | Simpan ID balasan untuk langkah multi-pusingan kemudian. |
| `use_previous_response_id` | Hantar pusingan ini berantai kepada ID balasan yang disimpan. |

Penegasan adalah pemeriksaan substring tanpa mengira huruf besar-kecil. Lihat
[dokumentasi tindakan](https://github.com/marketplace/actions/ai-smoke-test) untuk
skema penuh, termasuk sumber perbualan yang diuruskan oleh Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->