<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86273689a010b5efecaf7fa23104e0fb",
  "translation_date": "2025-11-07T08:43:02+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "id"
}
-->
# Persiapan Kursus

## Pengantar

Pelajaran ini akan membahas cara menjalankan contoh kode dari kursus ini.

## Bergabung dengan Peserta Lain dan Dapatkan Bantuan

Sebelum Anda mulai mengkloning repositori Anda, bergabunglah dengan [saluran Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) untuk mendapatkan bantuan terkait pengaturan, pertanyaan tentang kursus, atau untuk terhubung dengan peserta lainnya.

## Kloning atau Fork Repositori Ini

Untuk memulai, silakan kloning atau fork repositori GitHub. Ini akan membuat versi Anda sendiri dari materi kursus sehingga Anda dapat menjalankan, menguji, dan mengubah kode!

Anda dapat melakukannya dengan mengklik tautan untuk <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repositori</a>.

Sekarang Anda seharusnya memiliki versi fork dari kursus ini di tautan berikut:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.id.png)

### Kloning Shallow (direkomendasikan untuk workshop / Codespaces)

  >Repositori penuh bisa cukup besar (~3 GB) saat Anda mengunduh seluruh riwayat dan semua file. Jika Anda hanya mengikuti workshop atau hanya membutuhkan beberapa folder pelajaran, kloning shallow (atau kloning sparse) menghindari sebagian besar unduhan tersebut dengan memotong riwayat dan/atau melewatkan blob.

#### Kloning shallow cepat — riwayat minimal, semua file

Ganti `<your-username>` dalam perintah di bawah ini dengan URL fork Anda (atau URL upstream jika Anda lebih suka).

Untuk mengkloning hanya riwayat commit terbaru (unduhan kecil):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Untuk mengkloning cabang tertentu:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Kloning parsial (sparse) — blob minimal + hanya folder yang dipilih

Ini menggunakan kloning parsial dan sparse-checkout (memerlukan Git 2.25+ dan Git modern dengan dukungan kloning parsial direkomendasikan):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Masuk ke folder repositori:

```bash|powershell
cd ai-agents-for-beginners
```

Kemudian tentukan folder mana yang Anda inginkan (contoh di bawah menunjukkan dua folder):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Setelah mengkloning dan memverifikasi file, jika Anda hanya membutuhkan file dan ingin mengosongkan ruang (tanpa riwayat git), silakan hapus metadata repositori (💀tidak dapat dibalik — Anda akan kehilangan semua fungsi Git: tidak ada commit, pull, push, atau akses riwayat).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Menggunakan GitHub Codespaces (direkomendasikan untuk menghindari unduhan besar lokal)

- Buat Codespace baru untuk repositori ini melalui [UI GitHub](https://github.com/codespaces).  

- Di terminal Codespace yang baru dibuat, jalankan salah satu perintah kloning shallow/sparse di atas untuk membawa hanya folder pelajaran yang Anda butuhkan ke dalam ruang kerja Codespace.
- Opsional: setelah mengkloning di dalam Codespaces, hapus .git untuk mengosongkan ruang ekstra (lihat perintah penghapusan di atas).
- Catatan: Jika Anda lebih suka membuka repositori langsung di Codespaces (tanpa kloning tambahan), harap diperhatikan bahwa Codespaces akan membangun lingkungan devcontainer dan mungkin masih menyediakan lebih dari yang Anda butuhkan. Mengkloning salinan shallow di dalam Codespace baru memberi Anda lebih banyak kontrol atas penggunaan disk.

#### Tips

- Selalu ganti URL kloning dengan fork Anda jika Anda ingin mengedit/commit.
- Jika Anda nanti membutuhkan lebih banyak riwayat atau file, Anda dapat mengambilnya atau menyesuaikan sparse-checkout untuk menyertakan folder tambahan.

## Menjalankan Kode

Kursus ini menawarkan serangkaian Jupyter Notebooks yang dapat Anda jalankan untuk mendapatkan pengalaman langsung membangun AI Agents.

Contoh kode menggunakan:

**Memerlukan Akun GitHub - Gratis**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Ditandai sebagai (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Ditandai sebagai (autogen.ipynb)

**Memerlukan Langganan Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Ditandai sebagai (azureaiagent.ipynb)

Kami mendorong Anda untuk mencoba ketiga jenis contoh ini untuk melihat mana yang paling cocok untuk Anda.

Pilihan mana pun yang Anda pilih, itu akan menentukan langkah pengaturan mana yang perlu Anda ikuti di bawah ini:

## Persyaratan

- Python 3.12+
  - **NOTE**: Jika Anda belum menginstal Python3.12, pastikan Anda menginstalnya. Kemudian buat venv Anda menggunakan python3.12 untuk memastikan versi yang benar diinstal dari file requirements.txt.
  
    >Contoh

    Buat direktori Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    Kemudian aktifkan lingkungan venv untuk:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Untuk contoh kode yang menggunakan .NET, pastikan Anda menginstal [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) atau yang lebih baru. Kemudian, periksa versi SDK .NET yang diinstal:

    ```bash|powershell
    dotnet --list-sdks
    ```

- Akun GitHub - Untuk Akses ke GitHub Models Marketplace
- Langganan Azure - Untuk Akses ke Azure AI Foundry
- Akun Azure AI Foundry - Untuk Akses ke Azure AI Agent Service

Kami telah menyertakan file `requirements.txt` di root repositori ini yang berisi semua paket Python yang diperlukan untuk menjalankan contoh kode.

Anda dapat menginstalnya dengan menjalankan perintah berikut di terminal Anda di root repositori:

```bash|powershell
pip install -r requirements.txt
```

Kami merekomendasikan membuat lingkungan virtual Python untuk menghindari konflik dan masalah.

## Pengaturan VSCode

Pastikan Anda menggunakan versi Python yang benar di VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Pengaturan untuk Contoh yang Menggunakan GitHub Models 

### Langkah 1: Ambil Token Akses Pribadi (PAT) GitHub Anda

Kursus ini memanfaatkan GitHub Models Marketplace, yang menyediakan akses gratis ke Large Language Models (LLMs) yang akan Anda gunakan untuk membangun AI Agents.

Untuk menggunakan GitHub Models, Anda perlu membuat [Token Akses Pribadi GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Ini dapat dilakukan dengan pergi ke <a href="https://github.com/settings/personal-access-tokens" target="_blank">Pengaturan Token Akses Pribadi</a> di Akun GitHub Anda.

Harap ikuti [Prinsip Privilege Minimum](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) saat membuat token Anda. Ini berarti Anda hanya harus memberikan token izin yang diperlukan untuk menjalankan contoh kode dalam kursus ini.

1. Pilih opsi `Fine-grained tokens` di sisi kiri layar Anda dengan menuju ke **Pengaturan Pengembang**.

   ![Developer settings](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.id.png)

   Kemudian pilih `Generate new token`.

   ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.id.png)

2. Masukkan nama deskriptif untuk token Anda yang mencerminkan tujuannya, sehingga mudah diidentifikasi nanti.

    🔐 Rekomendasi Durasi Token

    Durasi yang direkomendasikan: 30 hari
    Untuk keamanan yang lebih baik, Anda dapat memilih periode yang lebih pendek—seperti 7 hari 🛡️
    Ini adalah cara yang bagus untuk menetapkan target pribadi dan menyelesaikan kursus sambil momentum belajar Anda tinggi 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.id.png)

3. Batasi cakupan token ke fork repositori ini.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.id.png)

4. Batasi izin token: Di bawah **Permissions**, klik tab **Account**, dan klik tombol "+ Add permissions". Dropdown akan muncul. Silakan cari **Models** dan centang kotaknya.

    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.id.png)

5. Verifikasi izin yang diperlukan sebelum membuat token. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.id.png)

6. Sebelum membuat token, pastikan Anda siap menyimpan token di tempat yang aman seperti brankas pengelola kata sandi, karena token tidak akan ditampilkan lagi setelah Anda membuatnya. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.id.png)

Salin token baru Anda yang baru saja dibuat. Anda sekarang akan menambahkannya ke file `.env` yang disertakan dalam kursus ini.

### Langkah 2: Buat File `.env` Anda

Untuk membuat file `.env` Anda, jalankan perintah berikut di terminal Anda.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Ini akan menyalin file contoh dan membuat `.env` di direktori Anda di mana Anda mengisi nilai untuk variabel lingkungan.

Dengan token Anda disalin, buka file `.env` di editor teks favorit Anda dan tempelkan token Anda ke bidang `GITHUB_TOKEN`.

![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.id.png)

Sekarang Anda seharusnya dapat menjalankan contoh kode dari kursus ini.

## Pengaturan untuk Contoh yang Menggunakan Azure AI Foundry dan Azure AI Agent Service

### Langkah 1: Ambil Endpoint Proyek Azure Anda

Ikuti langkah-langkah untuk membuat hub dan proyek di Azure AI Foundry yang dapat ditemukan di sini: [Ikhtisar sumber daya Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)

Setelah Anda membuat proyek Anda, Anda perlu mengambil string koneksi untuk proyek Anda.

Ini dapat dilakukan dengan pergi ke halaman **Overview** proyek Anda di portal Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.id.png)

### Langkah 2: Buat File `.env` Anda

Untuk membuat file `.env` Anda, jalankan perintah berikut di terminal Anda.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Ini akan menyalin file contoh dan membuat `.env` di direktori Anda di mana Anda mengisi nilai untuk variabel lingkungan.

Dengan token Anda disalin, buka file `.env` di editor teks favorit Anda dan tempelkan token Anda ke bidang `PROJECT_ENDPOINT`.

### Langkah 3: Masuk ke Azure

Sebagai praktik keamanan terbaik, kita akan menggunakan [otentikasi tanpa kunci](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) untuk otentikasi ke Azure OpenAI dengan Microsoft Entra ID. 

Selanjutnya, buka terminal dan jalankan `az login --use-device-code` untuk masuk ke akun Azure Anda.

Setelah Anda masuk, pilih langganan Anda di terminal.

## Variabel Lingkungan Tambahan - Azure Search dan Azure OpenAI 

Untuk Pelajaran Agentic RAG - Pelajaran 5 - ada contoh yang menggunakan Azure Search dan Azure OpenAI.

Jika Anda ingin menjalankan contoh ini, Anda perlu menambahkan variabel lingkungan berikut ke file `.env` Anda:

### Halaman Ikhtisar (Proyek)

- `AZURE_SUBSCRIPTION_ID` - Periksa **Detail Proyek** di halaman **Overview** proyek Anda.

- `AZURE_AI_PROJECT_NAME` - Lihat bagian atas halaman **Overview** untuk proyek Anda.

- `AZURE_OPENAI_SERVICE` - Temukan ini di tab **Included capabilities** untuk **Azure OpenAI Service** di halaman **Overview**.

### Pusat Manajemen

- `AZURE_OPENAI_RESOURCE_GROUP` - Pergi ke **Properti Proyek** di halaman **Overview** dari **Pusat Manajemen**.

- `GLOBAL_LLM_SERVICE` - Di bawah **Connected resources**, temukan nama koneksi **Azure AI Services**. Jika tidak terdaftar, periksa **portal Azure** di bawah grup sumber daya Anda untuk nama sumber daya AI Services.

### Halaman Model + Endpoint

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Pilih model embedding Anda (misalnya, `text-embedding-ada-002`) dan catat **Deployment name** dari detail model.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Pilih model chat Anda (misalnya, `gpt-4o-mini`) dan catat **Deployment name** dari detail model.

### Portal Azure

- `AZURE_OPENAI_ENDPOINT` - Cari **Azure AI services**, klik di atasnya, lalu pergi ke **Resource Management**, **Keys and Endpoint**, gulir ke bawah ke "Azure OpenAI endpoints", dan salin yang mengatakan "Language APIs".

- `AZURE_OPENAI_API_KEY` - Dari layar yang sama, salin KEY 1 atau KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Temukan sumber daya **Azure AI Search** Anda, klik di atasnya, dan lihat **Overview**.

- `AZURE_SEARCH_API_KEY` - Kemudian pergi ke **Settings** dan kemudian **Keys** untuk menyalin kunci admin utama atau sekunder.

### Halaman Eksternal

- `AZURE_OPENAI_API_VERSION` - Kunjungi halaman [siklus hidup versi API](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) di bawah **Rilis API GA terbaru**.

### Pengaturan otentikasi tanpa kunci

Daripada menghardcode kredensial Anda, kita akan menggunakan koneksi tanpa kunci dengan Azure OpenAI. Untuk melakukannya, kita akan mengimpor `DefaultAzureCredential` dan kemudian memanggil fungsi `DefaultAzureCredential` untuk mendapatkan kredensial.

```python
# Python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Terjebak di Suatu Tempat?
Jika Anda mengalami masalah saat menjalankan pengaturan ini, bergabunglah dengan <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> kami atau <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">buat sebuah isu</a>.

## Pelajaran Selanjutnya

Anda sekarang siap untuk menjalankan kode dalam kursus ini. Selamat belajar lebih banyak tentang dunia AI Agents!

[Pengenalan AI Agents dan Kasus Penggunaan Agen](../01-intro-to-ai-agents/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.