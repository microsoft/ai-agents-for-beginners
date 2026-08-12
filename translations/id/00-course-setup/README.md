# Pengaturan Kursus

## Pengantar

Pelajaran ini akan membahas cara menjalankan contoh kode dari kursus ini.

## Bergabung dengan Pelajar Lain dan Dapatkan Bantuan

Sebelum Anda mulai mengkloning repo Anda, bergabunglah dengan [channel Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) untuk mendapatkan bantuan dengan pengaturan, pertanyaan tentang kursus, atau untuk terhubung dengan pelajar lain.

## Kloning atau Fork Repo ini

Untuk memulai, silakan kloning atau fork Repository GitHub. Ini akan membuat versi Anda sendiri dari materi kursus sehingga Anda dapat menjalankan, menguji, dan mengubah kode!

Ini dapat dilakukan dengan mengklik tautan untuk <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repo</a>

Anda sekarang harus memiliki versi forked Anda sendiri dari kursus ini pada tautan berikut:

![Forked Repo](../../../translated_images/id/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (direkomendasikan untuk workshop / Codespaces)

  >Repositori penuh bisa sangat besar (~3 GB) saat Anda mengunduh sejarah lengkap dan semua file. Jika Anda hanya menghadiri workshop atau hanya membutuhkan beberapa folder pelajaran, shallow clone (atau sparse clone) menghindari sebagian besar unduhan tersebut dengan memotong sejarah dan/atau melewati blob.

#### Quick shallow clone — sejarah minimal, semua file

Ganti `<your-username>` pada perintah di bawah dengan URL fork Anda (atau URL upstream jika Anda lebih suka).

Untuk mengkloning hanya sejarah commit terbaru (unduhan kecil):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Untuk mengkloning cabang tertentu:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — blob minimal + hanya folder terpilih

Ini menggunakan partial clone dan sparse-checkout (diperlukan Git 2.25+ dan direkomendasikan Git modern dengan dukungan partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Masuk ke folder repo:

```bash|powershell
cd ai-agents-for-beginners
```

Kemudian tentukan folder mana yang Anda inginkan (contoh di bawah menunjukkan dua folder):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Setelah mengkloning dan memverifikasi file, jika Anda hanya membutuhkan file dan ingin mengosongkan ruang (tanpa sejarah git), silakan hapus metadata repositori (💀tidak dapat dibalik — Anda akan kehilangan semua fungsi Git: tidak ada commit, pull, push, atau akses sejarah).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Menggunakan GitHub Codespaces (direkomendasikan untuk menghindari unduhan besar lokal)

- Buat Codespace baru untuk repo ini melalui [GitHub UI](https://github.com/codespaces).  

- Di terminal codespace yang baru dibuat, jalankan salah satu perintah shallow/sparse clone di atas untuk membawa hanya folder pelajaran yang Anda butuhkan ke workspace Codespace.
- Opsional: setelah clone di dalam Codespaces, hapus .git untuk menghemat ruang tambahan (lihat perintah penghapusan di atas).
- Catatan: Jika Anda lebih suka membuka repo langsung di Codespaces (tanpa clone tambahan), ketahuilah Codespaces akan membangun lingkungan devcontainer dan mungkin masih menyediakan lebih dari yang Anda butuhkan. Mengclone salinan shallow di dalam Codespace baru memberi Anda kontrol lebih atas penggunaan disk.

#### Tips

- Selalu ganti URL clone dengan fork Anda jika Anda ingin mengedit/commit.
- Jika nanti Anda membutuhkan lebih banyak sejarah atau file, Anda dapat mengambilnya atau menyesuaikan sparse-checkout untuk menyertakan folder tambahan.

## Menjalankan Kode

Kursus ini menawarkan serangkaian Jupyter Notebooks yang dapat Anda jalankan untuk mendapatkan pengalaman langsung membangun AI Agents.

Contoh kode menggunakan **Microsoft Agent Framework (MAF)** dengan `FoundryChatClient`, yang terhubung ke **Microsoft Foundry Agent Service V2** (Responses API) melalui **Microsoft Foundry**.

Semua notebook Python diberi label `*-python-agent-framework.ipynb`.

## Persyaratan

- Python 3.12+
  - **CATATAN**: Jika Anda belum menginstal Python3.12, pastikan Anda menginstalnya. Kemudian buat venv Anda menggunakan python3.12 untuk memastikan versi yang benar terinstal dari file requirements.txt.
  
    >Contoh

    Membuat direktori Python venv:

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

- .NET 10+: Untuk kode contoh yang menggunakan .NET, pastikan Anda menginstal [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) atau yang lebih baru. Kemudian, periksa versi SDK .NET yang terinstal:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Diperlukan untuk autentikasi. Instal dari [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Langganan Azure** — Untuk akses ke Microsoft Foundry dan Microsoft Foundry Agent Service.
- **Proyek Microsoft Foundry** — Proyek dengan model yang dideploy (misalnya, `gpt-5-mini`). Lihat [Langkah 1](#langkah-1-membuat-proyek-microsoft-foundry) di bawah.

Kami telah menyertakan file `requirements.txt` di root repositori ini yang berisi semua paket Python yang diperlukan untuk menjalankan contoh kode.

Anda dapat menginstalnya dengan menjalankan perintah berikut di terminal Anda di root repositori:

```bash|powershell
pip install -r requirements.txt
```

Kami menyarankan membuat lingkungan virtual Python untuk menghindari konflik dan masalah.

## Pengaturan VSCode

Pastikan Anda menggunakan versi Python yang tepat di VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Menyiapkan Microsoft Foundry dan Microsoft Foundry Agent Service

### Langkah 1: Membuat Proyek Microsoft Foundry

Anda memerlukan **hub** dan **proyek** Microsoft Foundry dengan model yang dideploy untuk menjalankan notebook.

1. Pergi ke [ai.azure.com](https://ai.azure.com) dan masuk dengan akun Azure Anda.
2. Buat **hub** (atau gunakan yang sudah ada). Lihat: [Tinjauan sumber daya Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Di dalam hub, buat sebuah **proyek**.
4. Deploy model (misalnya, `gpt-5-mini`) dari **Models + Endpoints** → **Deploy model**.

### Langkah 2: Ambil Endpoint Proyek dan Nama Deployment Model Anda

Dari proyek Anda di portal Microsoft Foundry:

- **Project Endpoint** — Pergi ke halaman **Overview** dan salin URL endpoint.

![Project Connection String](../../../translated_images/id/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Pergi ke **Models + Endpoints**, pilih model Anda yang telah dideploy, dan catat **Deployment name** (misalnya, `gpt-5-mini`).

### Langkah 3: Masuk ke Azure dengan `az login`

Semua notebook menggunakan **`AzureCliCredential`** untuk autentikasi — tidak ada kunci API yang perlu diatur. Ini mengharuskan Anda masuk melalui Azure CLI.

1. **Instal Azure CLI** jika Anda belum: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Masuk** dengan menjalankan:

    ```bash|powershell
    az login
    ```

    Atau jika Anda berada di lingkungan remote/Codespace tanpa browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Pilih langganan Anda** jika diminta — pilih yang berisi proyek Foundry Anda.

4. **Verifikasi** Anda sudah masuk:

    ```bash|powershell
    az account show
    ```

> **Kenapa `az login`?** Notebook mengautentikasi menggunakan `AzureCliCredential` dari paket `azure-identity`. Ini berarti sesi Azure CLI Anda menyediakan kredensial — tidak ada kunci API atau rahasia di file `.env` Anda. Ini adalah [praktik terbaik keamanan](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

| Variabel | Dimana menemukannya |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → proyek Anda → halaman **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → nama model yang telah dideploy |

Itu saja untuk sebagian besar pelajaran! Notebook akan mengautentikasi secara otomatis melalui sesi `az login` Anda.

### Langkah 5: Instal Dependensi Python

```bash|powershell
pip install -r requirements.txt
```

Kami menyarankan menjalankan ini di dalam lingkungan virtual yang Anda buat sebelumnya.

## Pengaturan Tambahan untuk Pelajaran 5 (Agentic RAG)

Pelajaran 5 menggunakan **Azure AI Search** untuk retrieval-augmented generation. Jika Anda berencana menjalankan pelajaran itu, tambahkan variabel ini ke file `.env` Anda:

| Variabel | Dimana menemukannya |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → sumber daya **Azure AI Search** Anda → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Portal Azure → sumber daya **Azure AI Search** Anda → **Settings** → **Keys** → kunci admin utama |

## Pengaturan Tambahan untuk Pelajaran yang Memanggil Azure OpenAI Langsung (Pelajaran 6 dan 8)

Beberapa notebook di pelajaran 6 dan 8 memanggil **Azure OpenAI** langsung (menggunakan **Responses API**) alih-alih melalui proyek Microsoft Foundry. Contoh ini sebelumnya menggunakan GitHub Models, yang sudah tidak digunakan (dihentikan Juli 2026) dan tidak mendukung Responses API. Jika Anda berencana menjalankan contoh tersebut, tambahkan variabel ini ke file `.env` Anda:

| Variabel | Dimana menemukannya |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → sumber daya **Azure OpenAI** Anda → **Keys and Endpoint** → Endpoint (misal `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Nama model yang telah Anda deploy (misal `gpt-5-mini`) yang mendukung Responses API |
| `AZURE_OPENAI_API_KEY` | Opsional — hanya jika Anda menggunakan autentikasi berbasis kunci alih-alih `az login` / Entra ID |

> Responses API menggunakan endpoint stabil `/openai/v1/`, jadi tidak perlu `api-version`. Masuklah dengan `az login` untuk menggunakan autentikasi Entra ID tanpa kunci.

## Penyedia Alternatif: MiniMax (Kompatibel OpenAI)

[MiniMax](https://platform.minimaxi.com/) menyediakan model konteks besar (hingga 204K token) melalui API yang kompatibel dengan OpenAI. Karena Microsoft Agent Framework `OpenAIChatClient` berfungsi dengan endpoint kompatibel OpenAI mana pun, Anda dapat menggunakan MiniMax sebagai pengganti drop-in Azure OpenAI atau OpenAI.

Tambahkan variabel ini ke file `.env` Anda:

| Variabel | Dimana menemukannya |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Gunakan `https://api.minimax.io/v1` (nilai default) |
| `MINIMAX_MODEL_ID` | Nama model yang digunakan (misalnya, `MiniMax-M3`) |

**Model contoh**: `MiniMax-M3` (direkomendasikan), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (respon lebih cepat). Nama model dan ketersediaan dapat berubah dari waktu ke waktu, dan akses ke model tertentu mungkin tergantung pada akun atau wilayah Anda — periksa [MiniMax Platform](https://platform.minimaxi.com/) untuk daftar terkini. Jika `MiniMax-M3` tidak tersedia untuk akun Anda, setel `MINIMAX_MODEL_ID` ke model yang Anda miliki akses (misal `MiniMax-M2.7`).

Contoh kode yang menggunakan `OpenAIChatClient` (misal, alur kerja pemesanan hotel Pelajaran 14) akan otomatis mendeteksi dan menggunakan konfigurasi MiniMax Anda ketika `MINIMAX_API_KEY` disetel.

## Penyedia Alternatif: Foundry Local (Jalankan Model Di Perangkat)

[Foundry Local](https://foundrylocal.ai) adalah runtime ringan yang mengunduh, mengelola, dan melayani model bahasa **sepenuhnya di mesin Anda sendiri** melalui API kompatibel OpenAI — tanpa cloud, tanpa langganan Azure, dan tanpa kunci API. Ini adalah opsi bagus untuk pengembangan offline, bereksperimen tanpa biaya cloud, atau menyimpan data di perangkat.

Karena Microsoft Agent Framework `OpenAIChatClient` bekerja dengan endpoint kompatibel OpenAI mana pun, Foundry Local adalah alternatif lokal yang dapat digunakan sebagai pengganti Azure OpenAI.

**1. Instal Foundry Local**

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

**3. Instal SDK Python** yang digunakan untuk menemukan endpoint lokal:

```bash
pip install foundry-local-sdk
```

**4. Arahkan Microsoft Agent Framework ke model lokal Anda:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Mengunduh (jika diperlukan) dan menyajikan model secara lokal, kemudian menemukan endpoint/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # misal http://localhost:<port>/v1
    api_key=manager.api_key,        # selalu "tidak-dibutuhkan" untuk Foundry Lokal
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Catatan:** Foundry Local menyediakan endpoint kompatibel OpenAI **Chat Completions**. Gunakan untuk pengembangan lokal dan skenario offline. Untuk fitur lengkap **Responses API** (percakapan berstatus, orkestrasi alat mendalam, dan pengembangan gaya agen), tuju **Azure OpenAI** atau proyek **Microsoft Foundry** seperti yang ditunjukkan di pelajaran. Lihat [dokumentasi Foundry Local](https://foundrylocal.ai) untuk katalog model dan dukungan platform terkini.

## Pengaturan Tambahan untuk Pelajaran 8 (Alur Kerja Bing Grounding)


Notebook alur kerja kondisional di pelajaran 8 menggunakan **Bing grounding** melalui Microsoft Foundry. Jika Anda berencana menjalankan contoh tersebut, tambahkan variabel ini ke file `.env` Anda:

| Variabel | Tempat menemukannya |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal Microsoft Foundry → proyek Anda → **Management** → **Connected resources** → koneksi Bing Anda → salin ID koneksi |

## Pemecahan Masalah

### Error Verifikasi Sertifikat SSL di macOS

Jika Anda menggunakan macOS dan menemui error seperti:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ini adalah masalah yang sudah diketahui dengan Python di macOS di mana sertifikat SSL sistem tidak otomatis dipercaya. Coba solusi berikut secara berurutan:

**Opsi 1: Jalankan skrip Install Certificates Python (direkomendasikan)**

```bash
# Ganti 3.XX dengan versi Python yang Anda instal (misalnya, 3.12 atau 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opsi 2: Gunakan `connection_verify=False` di notebook Anda (hanya untuk notebook GitHub Models)**

Dalam notebook Pelajaran 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), sudah terdapat solusi sementara yang dikomentari. Hapus komentar `connection_verify=False` saat membuat klien:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Nonaktifkan verifikasi SSL jika Anda mengalami kesalahan sertifikat
)
```

> **⚠️ Peringatan:** Menonaktifkan verifikasi SSL (`connection_verify=False`) mengurangi keamanan dengan melewati validasi sertifikat. Gunakan ini hanya sebagai solusi sementara di lingkungan pengembangan, jangan pernah di produksi.

**Opsi 3: Instal dan gunakan `truststore`**

```bash
pip install truststore
```

Lalu tambahkan yang berikut di bagian atas notebook atau skrip Anda sebelum melakukan panggilan jaringan apa pun:

```python
import truststore
truststore.inject_into_ssl()
```

## Terjebak di Suatu Tempat?

Jika Anda mengalami masalah saat menjalankan pengaturan ini, bergabunglah di <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> atau <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">buat sebuah issue</a>.

## Pelajaran Selanjutnya

Anda sekarang siap menjalankan kode untuk kursus ini. Selamat belajar lebih banyak tentang dunia AI Agents!

[Pengenalan AI Agents dan Kasus Penggunaan Agen](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->