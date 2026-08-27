# Pengaturan Kursus

## Pendahuluan

Pelajaran ini akan membahas cara menjalankan contoh kode dari kursus ini.

## Bergabung dengan Pembelajar Lain dan Dapatkan Bantuan

Sebelum Anda mulai meng-clone repo Anda, bergabunglah dengan [saluran Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) untuk mendapatkan bantuan setup, pertanyaan tentang kursus, atau untuk berhubungan dengan pembelajar lain.

## Clone atau Fork Repo ini

Untuk memulai, silakan clone atau fork Repository GitHub. Ini akan membuat versi Anda sendiri dari materi kursus sehingga Anda dapat menjalankan, menguji, dan mengubah kode!

Ini dapat dilakukan dengan mengklik tautan <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repo</a>

Anda sekarang harus memiliki versi forked dari kursus ini pada tautan berikut:

![Forked Repo](../../../translated_images/id/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (disarankan untuk workshop / Codespaces)

  >Repo penuh bisa sangat besar (~3 GB) saat Anda mengunduh riwayat lengkap dan semua file. Jika Anda hanya mengikuti workshop atau hanya membutuhkan beberapa folder pelajaran, shallow clone (atau sparse clone) mengunduh lebih sedikit.

#### Shallow clone cepat — riwayat minimal, semua file

Ganti `<your-username>` pada perintah di bawah dengan URL fork Anda (atau URL upstream jika Anda mau).

Untuk clone hanya riwayat commit terbaru (unduh kecil):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Untuk clone specific branch:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — blob minimal + hanya folder terpilih

Ini menggunakan partial clone dan sparse-checkout (memerlukan Git 2.25+ dan disarankan Git modern dengan dukungan partial clone):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Masuk ke folder repo:

```bash
cd ai-agents-for-beginners
```

Kemudian tentukan folder mana yang Anda inginkan (contoh di bawah menunjukkan dua folder):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Setelah cloning dan memverifikasi file, jika Anda hanya perlu file dan ingin mengosongkan ruang (tanpa riwayat git), silakan hapus metadata repository (💀tidak dapat dikembalikan — Anda akan kehilangan semua fungsi Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Menggunakan GitHub Codespaces (disarankan untuk menghindari unduhan besar lokal)

- Buat Codespace baru untuk repo ini melalui [GitHub UI](https://github.com/codespaces).  

- Di terminal codespace yang baru dibuat, jalankan salah satu perintah shallow/sparse clone di atas untuk membawa hanya folder pelajaran yang Anda butuhkan ke ruang kerja Codespace.
- Opsional: setelah cloning dalam Codespaces, hapus .git untuk mengembalikan ruang ekstra (lihat perintah penghapusan di atas).
- Catatan: Jika Anda memilih membuka repo langsung di Codespaces (tanpa cloning tambahan), harap diketahui Codespaces akan menyusun lingkungan devcontainer dan mungkin masih menyediakan lebih dari yang Anda butuhkan.

#### Tips

- Selalu ganti URL clone dengan fork Anda jika ingin mengedit/commit.
- Jika Anda nanti membutuhkan lebih banyak riwayat atau file, Anda dapat mengambilnya (fetch) atau sesuaikan sparse-checkout untuk menyertakan folder tambahan.

## Menjalankan Kode

Kursus ini menawarkan serangkaian Jupyter Notebooks yang dapat Anda jalankan untuk mendapatkan pengalaman langsung membangun Agen AI.

Contoh kode menggunakan **Microsoft Agent Framework (MAF)** dengan `FoundryChatClient`, yang terhubung ke **Microsoft Foundry Agent Service V2** (Responses API) melalui **Microsoft Foundry**.

Semua notebook Python dilabeli `*-python-agent-framework.ipynb`.

## Persyaratan

- Python 3.12+
  - **CATATAN**: Jika Anda belum memiliki Python3.12 terpasang, pastikan untuk menginstalnya. Kemudian buat venv menggunakan python3.12 untuk memastikan versi yang benar terpasang dari file requirements.txt.
  
    >Contoh

    Buat direktori Python venv:

    ```bash
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

- .NET 10+: Untuk kode contoh yang menggunakan .NET, pastikan untuk menginstal [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) atau lebih baru. Kemudian, cek versi .NET SDK yang diinstal:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Diperlukan untuk autentikasi. Instal dari [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Untuk akses ke Microsoft Foundry dan Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Proyek dengan model yang telah dideploy (misal, `gpt-5-mini`). Lihat [Langkah 1](#langkah-1-buat-proyek-microsoft-foundry) di bawah.

Kami telah menyertakan file `requirements.txt` di root repository ini yang berisi semua paket Python yang dibutuhkan untuk menjalankan contoh kode.

Anda dapat menginstalnya dengan menjalankan perintah berikut di terminal Anda pada root repository:

```bash
pip install -r requirements.txt
```

Kami merekomendasikan membuat lingkungan virtual Python untuk menghindari konflik dan masalah.

## Setup VSCode

Pastikan Anda menggunakan versi Python yang tepat di VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Atur Microsoft Foundry dan Microsoft Foundry Agent Service

### Langkah 1: Buat Proyek Microsoft Foundry

Anda memerlukan **hub** dan **proyek** Microsoft Foundry dengan model yang sudah dideploy untuk menjalankan notebook.

1. Buka [ai.azure.com](https://ai.azure.com) dan masuk dengan akun Azure Anda.
2. Buat **hub** (atau gunakan yang sudah ada). Lihat: [Ikhtisar sumber daya Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Di dalam hub, buat **proyek**.
4. Deploy model (misal, `gpt-5-mini`) dari **Models + Endpoints** → **Deploy model**.

### Langkah 2: Dapatkan Endpoint Proyek dan Nama Deployment Model Anda

Dari proyek Anda di portal Microsoft Foundry:

- **Project Endpoint** — Buka halaman **Overview** dan salin URL endpoint.

![Project Connection String](../../../translated_images/id/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Buka **Models + Endpoints**, pilih model yang sudah dideploy, dan catat **Deployment name** (misal, `gpt-5-mini`).

### Langkah 3: Masuk ke Azure dengan `az login`

Kebanyakan notebook melakukan autentikasi melalui **Azure CLI sign-in** — memakai `AzureCliCredential` atau `DefaultAzureCredential` (keduanya mengambil sesi `az login` Anda) dari paket `azure-identity` — jadi tidak memerlukan kunci API. Beberapa pelajaran dan integrasi opsional menggunakan kunci API; periksa prasyarat setiap pelajaran untuk variabel lingkungan tambahan. Ini memerlukan Anda sudah masuk via Azure CLI.

1. **Instal Azure CLI** jika belum: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Masuk** dengan menjalankan:

    ```bash
    az login
    ```

    Atau jika Anda berada di lingkungan remote/Codespace tanpa browser:

    ```bash
    az login --use-device-code
    ```

3. **Pilih subscription Anda** jika diminta — pilih yang berisi proyek Foundry Anda.

4. **Verifikasi** bahwa Anda sudah masuk:

    ```bash
    az account show
    ```

> **Kenapa `az login`?** Notebook menggunakan autentikasi `AzureCliCredential` (atau `DefaultAzureCredential` yang juga memakai sign-in Azure CLI) dari paket `azure-identity`. Ini berarti sesi Azure CLI Anda memberikan kredensial — tanpa kunci API atau rahasia dalam file `.env` Anda. Ini adalah [praktik keamanan terbaik](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Langkah 4: Buat File `.env` Anda

Salin file contoh:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Buka `.env` dan isi dua nilai ini:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variabel | Lokasi mendapatkan |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → proyek Anda → halaman **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → nama model yang sudah dideploy |

Itu saja untuk sebagian besar pelajaran! Notebook akan melakukan autentikasi otomatis melalui sesi `az login` Anda.

### Langkah 5: Instal Dependensi Python

```bash
pip install -r requirements.txt
```

Kami merekomendasikan menjalankan ini di dalam lingkungan virtual yang Anda buat sebelumnya.

## Setup Opsional: Azure AI Search (Pelajaran 5 dan 16)

Notebook Pelajaran 5 (Agentic RAG) dan Pelajaran 16 berjalan langsung dengan **basis pengetahuan in-memory** — tanpa perlu sumber daya Azure tambahan. Jika Anda ingin mendukungnya dengan indeks **Azure AI Search** nyata, catat bahwa **Notebook Pelajaran 16 saat ini menggunakan autentikasi berbasis kunci**: ia beralih dari pencarian in-memory ke Azure AI Search hanya saat **kedua** `AZURE_SEARCH_SERVICE_ENDPOINT` **dan** `AZURE_SEARCH_API_KEY` disetel, dan tetap menggunakan pencarian in-memory jika tidak — jadi untuk menjalankannya terhadap indeks nyata Anda harus menetapkan kunci admin juga. Autentikasi tanpa kunci dengan Microsoft Entra ID (RBAC) adalah pendekatan yang direkomendasikan untuk kode produksi Anda sendiri, konsisten dengan alur `az login` yang digunakan di seluruh kursus ini.

Langkah RBAC di bawah ini berlaku untuk contoh panduan setup dan kode Anda sendiri. Ini tidak memungkinkan autentikasi tanpa kunci di Notebook Pelajaran 16; Pelajaran 16 masih membutuhkan endpoint dan kunci admin untuk menggunakan Azure AI Search.

1. **Aktifkan akses berbasis peran** pada layanan pencarian Anda:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Berikan diri Anda peran yang diperlukan** (buat/muat indeks dan query):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Tambahkan endpoint** ke file `.env` Anda:

| Variabel | Lokasi mendapatkan |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → sumber daya **Azure AI Search** Anda → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Diperlukan (bersama endpoint) untuk mengaktifkan Azure AI Search di Notebook Pelajaran 16, yang menggunakan autentikasi berbasis kunci. Portal Azure → **Settings** → **Keys** → kunci admin utama |

> **Kenapa tanpa kunci?** Kunci admin memberikan akses penuh tulis ke layanan pencarian Anda dan bisa bocor melalui file `.env`. Dengan RBAC, identitas `az login` Anda yang digunakan — pola Entra ID tanpa kunci yang sama digunakan oleh notebook kursus (melalui `AzureCliCredential` / `DefaultAzureCredential`). Lihat [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

Lihat [panduan setup Azure AI Search](./AzureSearch.md) untuk contoh lengkap pembuatan indeks dalam Python dan .NET.

## Setup Tambahan untuk Pelajaran yang Memanggil Azure OpenAI Langsung (Pelajaran 6 dan 8)

Beberapa notebook di pelajaran 6 dan 8 memanggil **Azure OpenAI** langsung (menggunakan **Responses API**) alih-alih melalui proyek Microsoft Foundry. Contoh ini sebelumnya menggunakan GitHub Models, yang sudah tidak digunakan dan tidak mendukung Responses API. Tambahkan variabel berikut ke file `.env` Anda:

| Variabel | Lokasi mendapatkan |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → sumber daya **Azure OpenAI** Anda → **Keys and Endpoint** → Endpoint (misal, `https://<resource-anda>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Nama model yang Anda deploy (misal, `gpt-5-mini`) yang mendukung Responses API |
| `AZURE_OPENAI_API_KEY` | Opsional — hanya jika Anda menggunakan autentikasi berbasis kunci bukan `az login` / Entra ID |

> Responses API menggunakan endpoint stabil `/openai/v1/`, jadi tidak perlu `api-version`. Masuk dengan `az login` untuk menggunakan autentikasi Entra ID tanpa kunci.

## Penyedia Alternatif: MiniMax (Kompatibel dengan OpenAI)

[MiniMax](https://platform.minimaxi.com/) menyediakan model ber-konteks besar (hingga 204K token) melalui API yang kompatibel dengan OpenAI. Karena `OpenAIChatClient` dari Microsoft Agent Framework berfungsi dengan endpoint yang kompatibel OpenAI apa saja, Anda dapat menggunakan MiniMax sebagai alternatif langsung untuk pelajaran yang menggunakan `OpenAIChatClient`.

Tambahkan variabel ini ke file `.env` Anda:

| Variabel | Lokasi mendapatkan |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Platform MiniMax](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Gunakan `https://api.minimax.io/v1` (nilai default) |
| `MINIMAX_MODEL_ID` | Nama model yang digunakan (misal, `MiniMax-M3`) |

**Model contoh**: `MiniMax-M3` (disarankan), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (respon lebih cepat). Nama model dan ketersediaan dapat berubah seiring waktu, dan akses ke model tertentu bisa tergantung akun Anda.

Contoh kode yang menggunakan `OpenAIChatClient` (misal, workflow pemesanan hotel Pelajaran 14) akan otomatis mendeteksi dan menggunakan konfigurasi MiniMax Anda saat `MINIMAX_API_KEY` disetel.


## Penyedia Alternatif: Foundry Local (Jalankan Model di Perangkat)

[Foundry Local](https://foundrylocal.ai) adalah runtime ringan yang mengunduh, mengelola, dan melayani model bahasa **sepenuhnya di mesin Anda sendiri** melalui API yang kompatibel dengan OpenAI — tanpa memerlukan cloud.

Karena `OpenAIChatClient` di Microsoft Agent Framework bekerja dengan endpoint yang kompatibel dengan OpenAI apa pun, Foundry Local adalah alternatif lokal yang siap pakai untuk Azure OpenAI.

**1. Pasang Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Unduh dan jalankan model** (ini juga memulai layanan lokal):

```bash
foundry model list          # lihat model yang tersedia
foundry model run phi-4-mini
```

**3. Pasang SDK Python** yang digunakan untuk menemukan endpoint lokal:

```bash
pip install foundry-local-sdk
```

**4. Arahkan Microsoft Agent Framework ke model lokal Anda:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Mengunduh (jika diperlukan) dan melayani model secara lokal, lalu menemukan endpoint/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # misalnya http://localhost:<port>/v1
    api_key=manager.api_key,        # selalu "tidak-diperlukan" untuk Foundry Lokal
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Catatan:** Foundry Local menyediakan endpoint **Chat Completions** yang kompatibel dengan OpenAI. Gunakan untuk pengembangan lokal dan skenario offline. Untuk fitur lengkap **Responses API** (percakapan berstatus, dll.), gunakan Azure OpenAI atau proyek Microsoft Foundry.

## Pengaturan Tambahan untuk Pelajaran 8 (Alur Kerja Bing Grounding)

Notebook alur kerja bersyarat di pelajaran 8 menggunakan **Bing grounding** melalui Microsoft Foundry. Jika Anda berencana menjalankan contoh tersebut, tambahkan variabel ini ke file `.env` Anda:

| Variabel | Tempat menemukannya |
|----------|---------------------|
| `BING_CONNECTION_ID` | Portal Microsoft Foundry → proyek Anda → **Management** → **Connected resources** → koneksi Bing Anda → salin ID koneksi |

## Pemecahan Masalah

### Kesalahan Verifikasi Sertifikat SSL di macOS

Jika Anda menggunakan macOS dan mengalami kesalahan seperti:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ini adalah masalah yang diketahui dengan Python di macOS di mana sertifikat SSL sistem tidak secara otomatis dipercaya. Cobalah solusi berikut secara berurutan:

**Opsi 1: Jalankan skrip Install Certificates Python (direkomendasikan)**

```bash
# Ganti 3.XX dengan versi Python yang Anda pasang (misalnya, 3.12 atau 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opsi 2: Gunakan `connection_verify=False` di notebook Anda (hanya untuk notebook GitHub Models)**

Dalam notebook Pelajaran 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), solusi sementara yang dikomentari sudah disertakan. Hapus komentar pada `connection_verify=False` saat Anda mengalami kesalahan sertifikat:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Nonaktifkan verifikasi SSL jika Anda mengalami kesalahan sertifikat
)
```

> **⚠️ Peringatan:** Menonaktifkan verifikasi SSL (`connection_verify=False`) mengurangi keamanan dengan melewati validasi sertifikat. Gunakan ini hanya sebagai solusi sementara di lingkungan pengembangan. Jangan pernah menggunakannya di produksi.

**Opsi 3: Pasang dan gunakan `truststore`**

```bash
pip install truststore
```

Kemudian tambahkan berikut ini di bagian atas notebook atau skrip Anda sebelum melakukan panggilan jaringan apapun:

```python
import truststore
truststore.inject_into_ssl()
```

## Bingung di Mana?

Jika Anda mengalami masalah menjalankan pengaturan ini, bergabunglah dengan <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> kami atau <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">buat sebuah masalah</a>.

## Pelajaran Berikutnya

Anda sekarang siap menjalankan kode untuk kursus ini. Semoga senang belajar lebih banyak tentang dunia Agen AI!

[Pengenalan Agen AI dan Kasus Penggunaan Agen](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->