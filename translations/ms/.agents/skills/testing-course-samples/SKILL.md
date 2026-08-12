---
name: testing-course-samples
description: Gunakan apabila diminta untuk mengesahkan, menguji, melakukan ujian asap,
  atau menjalankan buku nota dan contoh kod kursus terhadap konfigurasi Microsoft
  Foundry / Azure OpenAI secara langsung. Meliputi penyediaan persekitaran (.env,
  az login, pakej), skrip/validate-notebooks.ps1 sebagai pelancar, mentafsir keputusan
  LULUS/GAGAL, dan pelajaran mana yang memerlukan sumber tambahan (Azure AI Search,
  GitHub MCP, Foundry Local, Playwright).
---
# Menguji Contoh Kursus

Sahkan bahawa buku nota pelajaran dan contoh kod berjalan dengan setup langsung
Microsoft Foundry / Azure OpenAI. Repositori menyediakan runner di
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) yang
menjalankan setiap buku nota Python tanpa kepala dan mencetak matriks LULUS/GAGAL.

## Bila untuk digunakan
- "Sahkan semua buku nota / contoh kepada langganan Azure saya."
- "Ujian asap kursus selepas menaik taraf pakej atau menukar model."
- "Pelajaran mana yang masih lulus / gagal secara langsung?"

Jangan gunakan ini untuk GitHub Action Ujian Asap AI (yang mengesahkan ejen hos yang *dilancar*
— lihat [`tests/README.md`](../../../tests/README.md)). Kemahiran ini
menjalankan buku nota secara tempatan.

## Prasyarat (semak dahulu)
1. **Python 3.12+** dengan kebergantungan kursus: `python -m pip install -r requirements.txt`
   ditambah pelaksana: `python -m pip install nbconvert ipykernel`.
2. **`.env` di akar repositori** (salin dari [`.env.example`](../../../../../.env.example)) dengan sekurang-kurangnya:
   - `AZURE_AI_PROJECT_ENDPOINT` — titik hujung projek Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — penempatan yang tidak dilarang (contoh `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) dan `AZURE_OPENAI_DEPLOYMENT`
     untuk pelajaran yang memanggil Azure OpenAI secara langsung (Pelajaran 06, 02-azure-openai, 14 penyerahan/silangan manusia).
3. **`az login`** telah selesai — contoh mengesahkan dengan `AzureCliCredential` (Entra ID, tanpa kunci).
4. Sahkan penempatan model wujud:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Menjalankan pengesahan
```powershell
# Semua buku nota Python (melangkau .NET, .venv, site-packages, terjemahan, aset kemahiran)
pwsh scripts/validate-notebooks.ps1

# Satu pelajaran sahaja, dengan masa tamat per-sel yang lebih panjang
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Hanya senaraikan apa yang akan dijalankan (tanpa pelaksanaan)
pwsh scripts/validate-notebooks.ps1 -List

# Penafsir secara eksplisit (jika `python` tidak ada dalam PATH, contohnya alias Kedai Windows)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skrip menulis salinan yang dilaksanakan, log per-buku nota, dan `results.json` ke
`$env:TEMP\aiab-nbval` dan keluar dengan bilangan kegagalan.

## Memahami keputusan
- `PASS` — buku nota berjalan dari awal hingga akhir tanpa ralat sel.
- `FAIL` — baris `*Error` / `*Exception` pertama dipaparkan; buka
  `log_*.txt` yang sepadan dalam direktori output untuk traceback penuh.
- Kegagalan satu buku nota dibatasi oleh `-Timeout` (setiap sel), jadi sel human-in-the-loop yang tersekat
  muncul sebagai `StdinNotImplementedError` dan bukannya tersekat.

## Pelajaran yang memerlukan sumber tambahan (dijangka gagal tanpa mereka)
| Pelajaran | Keperluan tambahan |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, kunci) — ada laluan fallback dalam memori |
| 11 MCP / GitHub | Pelayan GitHub MCP + PAT |
| 13 memory (cognee) | `cognee` dikonfigurasi dengan penyedia model |
| 15 penggunaan pelayar | Pelayar Playwright dipasang (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 agen tempatan | Masa jalan Foundry Local + model Qwen yang dimuat turun (di peranti, tiada awan) |
| buku nota `*-dotnet-*` | Kernel .NET Interactive (dikecualikan secara lalai; gunakan `-IncludeDotnet`) |

## Melaporkan kembali
Rumuskan sebagai jadual LULUS/GAGAL yang dikelompokkan mengikut pelajaran. Pisahkan regresi sejati
(pepijat kod/konfigurasi yang perlu diperbaiki) daripada kekurangan persekitaran (Search/Foundry Local/PAT hilang),
dan nyatakan `log_*.txt` yang gagal untuk setiap kegagalan sebenar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->