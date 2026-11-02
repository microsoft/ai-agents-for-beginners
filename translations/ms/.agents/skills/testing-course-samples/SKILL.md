---
name: testing-course-samples
description: Gunakan apabila diminta untuk mengesahkan, menguji, ujian asap, atau
  menjalankan notebook kursus dan contoh kod terhadap konfigurasi Microsoft Foundry
  / Azure OpenAI yang langsung. Meliputi penyediaan persekitaran (.env, az login,
  pakej), pelari skrip/validate-notebooks.ps1, mentafsir keputusan LULUS/GAGAL, dan
  pelajaran mana yang memerlukan sumber tambahan (Azure AI Search, GitHub MCP, Foundry
  Local, Playwright).
---
# Menguji Contoh Kursus

Sahkan bahawa buku nota pelajaran dan contoh kod dijalankan terhadap konfigurasi
Microsoft Foundry / Azure OpenAI yang hidup. Repositori ini menyediakan pelari di
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) yang
melaksanakan setiap buku nota Python tanpa kepala dan mencetak matriks LULUS/GAGAL.

## Bila untuk digunakan
- "Sahkan semua buku nota / contoh terhadap langganan Azure saya."
- "Uji asap kursus selepas menaik taraf pakej atau menukar model."
- "Pelajaran mana yang masih lulus / gagal secara langsung?"

Jangan gunakan ini untuk Tindakan GitHub Ujian Asap AI (yang mengesahkan ejen
yang dihoskan *diterapkan* — lihat [`tests/README.md`](../../../tests/README.md)). Kemahiran ini
menjalankan buku nota secara tempatan.

## Prasyarat (semak dahulu)
1. **Python 3.12+** dengan kebergantungan kursus: `python -m pip install -r requirements.txt`
   serta pelaksana: `python -m pip install nbconvert ipykernel`.
2. **`.env` di akar repositori** (salin dari [`.env.example`](../../../../../.env.example)) dengan sekurang-kurangnya:
   - `AZURE_AI_PROJECT_ENDPOINT` — titik akhir projek Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — penempatan yang tidak usang (contoh `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) dan `AZURE_OPENAI_DEPLOYMENT`
     untuk pelajaran yang memanggil Azure OpenAI secara langsung (Pelajaran 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** selesai — contoh disahkan dengan `AzureCliCredential` (Entra ID, tanpa kekunci).
4. Sahkan penempatan model wujud:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Menjalankan pengesahan
```powershell
# Semua buku nota Python (mengabaikan .NET, .venv, site-packages, terjemahan, aset kemahiran)
pwsh scripts/validate-notebooks.ps1

# Satu pelajaran sahaja, dengan masa tamat per-sel yang lebih lama
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Senaraikan sahaja apa yang akan dijalankan (tanpa pelaksanaan)
pwsh scripts/validate-notebooks.ps1 -List

# Penafsir secara jelas (jika `python` tidak ada dalam PATH, contohnya alias Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skrip menulis salinan yang dilaksanakan, log per-buku nota, dan `results.json` ke
`$env:TEMP\aiab-nbval` dan keluar dengan bilangan kegagalan.

Kegagalan sementara (had kadar HTTP 429 langganan dikongsi, sedikit masalah token
`AzureCliCredential`, atau masa tamat) dicuba semula secara automatik
(`-Retries`, lalai 2, dengan `-RetryDelaySeconds` penangguhan, lalai 20). Jika
penempatan model sentiasa 429, periksa kuota TPM GlobalStandard langganan
(`az cognitiveservices usage list -l <region>`) — menaikkan kapasiti penempatan tunggal tidak membantu apabila kuota *langganan* habis.


## Menafsirkan keputusan
- `PASS` — buku nota dijalankan sepenuhnya tanpa ralat sel.
- `FAIL` — baris pertama `*Error` / `*Exception` dipaparkan; buka
  `log_*.txt` yang sepadan dalam direktori output untuk jejak balik penuh.
- Kegagalan satu buku nota terhad oleh `-Timeout` (setiap sel), jadi sel yang tergantung
  manusia-dalam-gelung ditunjukkan sebagai `StdinNotImplementedError` dan bukannya tergantung.

## Pelajaran yang memerlukan sumber tambahan (dijangka gagal tanpa mereka)
| Pelajaran | Keperluan tambahan |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, kekunci) — ada laluan sandaran dalam ingatan |
| 11 MCP / GitHub | Pelayan GitHub MCP + PAT |
| 13 memory (cognee) | `cognee` dikonfigurasi dengan penyedia model |
| 15 penggunaan penyemak imbas | Penyemak imbas Playwright dipasang (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 agen tempatan | Persekitaran tempatan Foundry + model Qwen dimuat turun (pada peranti, tanpa awan) |
| buku nota `*-dotnet-*` | Kernel .NET Interactive (dikecualikan secara lalai; gunakan `-IncludeDotnet`) |

## Melaporkan kembali
Rumuskan sebagai jadual LULUS/GAGAL berkelompok mengikut pelajaran. Pisahkan regresi sebenar
(pepijat kod/konfigurasi untuk dibaiki) dari kekurangan persekitaran (Cari/Foundry Tempatan/PAT hilang),
dan rujuk `log_*.txt` yang gagal bagi setiap kegagalan sebenar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->