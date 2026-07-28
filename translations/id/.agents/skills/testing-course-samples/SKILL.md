---
name: testing-course-samples
---
# Menguji Contoh Kursus

Validasi bahwa buku catatan pelajaran dan contoh kode berjalan terhadap pengaturan Microsoft Foundry / Azure OpenAI yang aktif.
Repo menyediakan sebuah runner di
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) yang
menjalankan setiap notebook Python tanpa antarmuka dan mencetak matriks PASS/FAIL.

## Kapan digunakan
- "Validasi semua notebook / contoh terhadap langganan Azure saya."
- "Uji cepat kursus setelah memperbarui paket atau mengubah model."
- "Pelajaran mana yang masih lulus / gagal secara langsung?"

Jangan gunakan ini untuk AI Smoke Test GitHub Action (yang memvalidasi agen yang *dideploy*
yang dihosting — lihat [`tests/README.md`](../../../tests/README.md)). Skill ini
menjalankan notebook secara lokal.

## Prasyarat (periksa dulu)
1. **Python 3.12+** dengan dependensi kursus: `python -m pip install -r requirements.txt`
   plus executor: `python -m pip install nbconvert ipykernel`.
2. **`.env` di root repo** (salin dari [`.env.example`](../../../../../.env.example)) dengan minimal:
   - `AZURE_AI_PROJECT_ENDPOINT` — endpoint proyek Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — sebuah deployment yang tidak usang (mis. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) dan `AZURE_OPENAI_DEPLOYMENT`
     untuk pelajaran yang memanggil Azure OpenAI langsung (Pelajaran 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** sudah selesai — contoh otentikasi dengan `AzureCliCredential` (Entra ID, tanpa kunci).
4. Verifikasi deployment model ada:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Menjalankan validasi
```powershell
# Semua notebook Python (melewati .NET, .venv, site-packages, terjemahan, aset keterampilan)
pwsh scripts/validate-notebooks.ps1

# Sebuah pelajaran tunggal, dengan batas waktu per-sel yang lebih lama
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Hanya daftarkan apa yang akan dijalankan (tanpa eksekusi)
pwsh scripts/validate-notebooks.ps1 -List

# Interpreter eksplisit (jika `python` tidak ada di PATH, misalnya alias Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skrip menulis salinan yang dijalankan, log per-notebook, dan `results.json` ke
`$env:TEMP\aiab-nbval` dan keluar dengan jumlah kegagalan.

Kegagalan sementara (batas laju HTTP 429 langganan bersama, gangguan sesekali
token `AzureCliCredential`, atau timeout) akan dicoba ulang secara otomatis
(`-Retries`, default 2, dengan penundaan `-RetryDelaySeconds`, default 20). Jika
deployment model sering mendapatkan 429, periksa kuota GlobalStandard
TPM langganan (`az cognitiveservices usage list -l <region>`) — menaikkan kapasitas
satu deployment saja tidak membantu bila kuota *langganan* habis.

## Menafsirkan hasil
- `PASS` — notebook berjalan dari awal sampai akhir tanpa error pada sel.
- `FAIL` — baris `*Error` / `*Exception` pertama ditampilkan; buka
  `log_*.txt` yang sesuai di direktori output untuk traceback lengkap.
- Kegagalan satu notebook dibatasi oleh `-Timeout` (per sel), jadi sel human-in-the-loop yang macet
  muncul sebagai `StdinNotImplementedError` daripada menggantung.

## Pelajaran yang membutuhkan sumber daya tambahan (diperkirakan gagal tanpa itu)
| Pelajaran | Persyaratan tambahan |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, kunci) — memiliki jalur fallback di memori |
| 11 MCP / GitHub | Server GitHub MCP + PAT |
| 13 memory (cognee) | `cognee` dikonfigurasi dengan penyedia model |
| 15 browser-use | Browser Playwright terinstal (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Runtime Foundry Lokal + model Qwen yang diunduh (di perangkat, tanpa cloud) |
| notebook `*-dotnet-*` | kernel .NET Interactive (tidak disertakan secara default; gunakan `-IncludeDotnet`) |

## Melaporkan kembali
Ringkas sebagai tabel PASS/FAIL dikelompokkan berdasarkan pelajaran. Pisahkan regresi nyata
(bug kode/konfigurasi yang harus diperbaiki) dari kekurangan lingkungan (Search/Foundry Local/PAT yang hilang),
dan cantumkan `log_*.txt` yang gagal untuk setiap kegagalan nyata.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->