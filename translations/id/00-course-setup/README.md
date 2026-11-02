# Persiapan Kursus

## Pendahuluan

Pelajaran ini akan membahas cara menjalankan contoh kode dari kursus ini.

## Bergabung dengan Pelajar Lain dan Dapatkan Bantuan

Sebelum Anda mulai mengkloning repo Anda, bergabunglah dengan [saluran Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) untuk mendapatkan bantuan dengan pengaturan, pertanyaan tentang kursus, atau untuk berhubungan dengan pelajar lain.

## Kloning atau Fork Repo ini

Untuk memulai, silakan kloning atau fork Repository GitHub. Ini akan membuat versi Anda sendiri dari materi kursus sehingga Anda dapat menjalankan, menguji, dan mengubah kode!

Ini dapat dilakukan dengan mengklik tautan untuk <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repo</a>

Sekarang Anda harus memiliki versi fork Anda sendiri dari kursus ini pada tautan berikut:

![Forked Repo](../../../translated_images/id/forked-repo.33f27ca1901baa6a.webp)

### Kloning Dangkal (disarankan untuk lokakarya / Codespaces)

  >Repositori lengkap bisa sangat besar (~3 GB) saat Anda mengunduh riwayat penuh dan semua file. Jika Anda hanya mengikuti lokakarya atau hanya memerlukan beberapa folder pelajaran, kloning dangkal (atau sparse clone) mengunduh jauh lebih sedikit.

#### Kloning dangkal cepat — riwayat minimal, semua file

Ganti `<your-username>` dalam perintah di bawah dengan URL fork Anda (atau URL upstream jika Anda mau).

Untuk mengkloning hanya riwayat commit terbaru (unduhan kecil):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Untuk mengkloning cabang tertentu:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Kloning Parsial (sparse) — blob minimal + hanya folder yang dipilih

Ini menggunakan kloning parsial dan sparse-checkout (memerlukan Git 2.25+ dan disarankan Git modern dengan dukungan kloning parsial):

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

Setelah mengkloning dan memverifikasi file, jika Anda hanya membutuhkan file dan ingin mengosongkan ruang (tanpa riwayat git), silakan hapus metadata repositori (💀tidak dapat dipulihkan — Anda akan kehilangan semua fungsi Git):

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

- Di terminal codespace yang baru dibuat, jalankan salah satu perintah kloning dangkal/sparse di atas untuk hanya membawa folder pelajaran yang Anda butuhkan ke dalam ruang kerja Codespace.
- Opsional: setelah mengkloning di dalam Codespaces, hapus .git untuk mengembalikan ruang ekstra (lihat perintah penghapusan di atas).
- Catatan: Jika Anda lebih suka membuka repo langsung di Codespaces (tanpa kloning tambahan), perlu diketahui Codespaces akan membangun lingkungan devcontainer dan mungkin masih menyediakan lebih banyak daripada yang Anda butuhkan.

#### Tips

- Selalu ganti URL kloning dengan fork Anda jika Anda ingin mengedit/commit.
- Jika nanti Anda memerlukan lebih banyak riwayat atau file, Anda dapat mengambilnya atau menyesuaikan sparse-checkout untuk menyertakan folder tambahan.

## Menjalankan Kode

Kursus ini menawarkan serangkaian Jupyter Notebooks yang dapat Anda jalankan untuk mendapatkan pengalaman langsung membangun AI Agents.

Contoh kode menggunakan **Microsoft Agent Framework (MAF)** dengan `FoundryChatClient`, yang terhubung ke **Microsoft Foundry Agent Service V2** (API Respons) melalui **Microsoft Foundry**.

Semua notebook Python berlabel `*-python-agent-framework.ipynb`.

## Persyaratan

- Python 3.12+
  - **CATATAN**: Jika Anda belum menginstal Python3.12, pastikan Anda menginstalnya. Kemudian buat venv Anda menggunakan python3.12 untuk memastikan versi yang benar diinstal dari file requirements.txt.
  
    >Contoh

    Buat direktori venv Python:

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

- .NET 10+: Untuk kode sampel yang menggunakan .NET, pastikan Anda menginstal [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) atau yang lebih baru. Kemudian, periksa versi SDK .NET yang terinstal:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Diperlukan untuk otentikasi. Instal dari [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Untuk akses ke Microsoft Foundry dan Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Sebuah proyek dengan model yang telah dideploy (misalnya, `gpt-5-mini`). Lihat [Langkah 1](#langkah-1-buat-proyek-microsoft-foundry) di bawah.

Kami telah menyertakan file `requirements.txt` di root repositori ini yang berisi semua paket Python yang diperlukan untuk menjalankan contoh kode.

Anda dapat menginstalnya dengan menjalankan perintah berikut di terminal Anda pada root repositori:

```bash
pip install -r requirements.txt
```

Kami menyarankan membuat lingkungan virtual Python untuk menghindari konflik dan masalah apapun.

## Atur VSCode

Pastikan Anda menggunakan versi Python yang tepat di VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Siapkan Microsoft Foundry dan Microsoft Foundry Agent Service

### Langkah 1: Buat Proyek Microsoft Foundry

Anda memerlukan **hub** dan **proyek** Microsoft Foundry dengan model yang sudah dideploy untuk menjalankan notebook.

1. Buka [ai.azure.com](https://ai.azure.com) dan masuk dengan akun Azure Anda.
2. Buat **hub** (atau gunakan yang sudah ada). Lihat: [Ikhtisar sumber daya Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Di dalam hub, buat sebuah **proyek**.
4. Deploy sebuah model (misalnya, `gpt-5-mini`) dari **Models + Endpoints** → **Deploy model**.

### Langkah 2: Dapatkan Endpoint Proyek dan Nama Deployment Model Anda

Dari proyek Anda di portal Microsoft Foundry:

- **Project Endpoint** — Buka halaman **Overview** dan salin URL endpoint.

![Project Connection String](../../../translated_images/id/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nama Deployment Model** — Buka **Models + Endpoints**, pilih model yang dideploy, dan catat **Deployment name** (misalnya, `gpt-5-mini`).

### Langkah 3: Masuk ke Azure dengan `az login`

Kebanyakan notebook mengotentikasi melalui **Azure CLI sign-in** Anda — menggunakan `AzureCliCredential` atau `DefaultAzureCredential` (keduanya mengambil sesi `az login` Anda) dari paket `azure-identity` — jadi tidak memerlukan kunci API. Beberapa pelajaran dan integrasi opsional menggunakan kunci API; periksa prasyarat setiap pelajaran untuk variabel lingkungan tambahan. Ini mengharuskan Anda masuk melalui Azure CLI.

1. **Instal Azure CLI** jika belum: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Masuk** dengan menjalankan:

    ```bash
    az login
    ```

    Atau jika Anda berada di lingkungan remote/Codespace tanpa browser:

    ```bash
    az login --use-device-code
    ```

3. **Pilih langganan Anda** jika diminta — pilih yang berisi proyek Foundry Anda.

4. **Verifikasi** bahwa Anda sudah masuk:

    ```bash
    az account show
    ```

> **Mengapa `az login`?** Notebook mengautentikasi menggunakan `AzureCliCredential` (atau `DefaultAzureCredential`, yang juga mengambil sign-in Azure CLI Anda) dari paket `azure-identity`. Ini berarti sesi Azure CLI Anda menyediakan kredensial — tidak perlu kunci API atau rahasia di file `.env` Anda. Ini adalah [praktik keamanan terbaik](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

| Variabel | Tempat menemukannya |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → proyek Anda → halaman **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → nama model yang dideploy |

Itu saja untuk sebagian besar pelajaran! Notebook akan otomatis mengotentikasi melalui sesi `az login` Anda.

### Langkah 5: Instal Dependensi Python

```bash
pip install -r requirements.txt
```

Kami sarankan menjalankan ini di dalam lingkungan virtual yang Anda buat sebelumnya.

## Pengaturan Opsional: Azure AI Search (Pelajaran 5 dan 16)

Notebook Pelajaran 5 (Agentic RAG) dan Pelajaran 16 dapat langsung dijalankan dengan **basis pengetahuan dalam memori** — tidak perlu sumber daya Azure tambahan. Jika Anda ingin menggunakan **Azure AI Search** sungguhan, perhatikan bahwa **notebook Pelajaran 16 saat ini menggunakan otentikasi berbasis kunci**: ia beralih dari pencarian dalam memori ke Azure AI Search hanya ketika **kedua** `AZURE_SEARCH_SERVICE_ENDPOINT` **dan** `AZURE_SEARCH_API_KEY` diatur, jika tidak tetap menggunakan pencarian dalam memori — jadi untuk menjalankannya dengan indeks nyata Anda harus menetapkan kunci admin juga. Otentikasi tanpa kunci dengan Microsoft Entra ID (RBAC) adalah pendekatan yang disarankan untuk kode produksi Anda sendiri, sesuai dengan alur `az login` yang digunakan di seluruh kursus ini.

Langkah-langkah RBAC di bawah berlaku untuk contoh panduan pengaturan dan kode Anda sendiri. Mereka tidak mengaktifkan otentikasi tanpa kunci di notebook Pelajaran 16; Pelajaran 16 tetap memerlukan endpoint dan kunci admin untuk menggunakan Azure AI Search.

1. **Aktifkan akses berbasis peran** pada layanan pencarian Anda:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Beri diri Anda peran yang diperlukan** (membuat/memuat indeks dan query):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Tambahkan endpoint** ke file `.env` Anda:

| Variabel | Tempat menemukannya |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → sumber daya **Azure AI Search** Anda → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Diperlukan (bersama endpoint) untuk mengaktifkan Azure AI Search di notebook Pelajaran 16, yang menggunakan otentikasi berbasis kunci. Portal Azure → **Settings** → **Keys** → kunci admin utama |

> **Mengapa tanpa kunci?** Kunci admin memberi akses tulis penuh ke layanan pencarian Anda dan bisa bocor lewat file `.env`. Dengan RBAC, identitas `az login` Anda digunakan sebagai gantinya — pola Entra ID tanpa kunci yang sama yang digunakan notebook kursus (melalui `AzureCliCredential` / `DefaultAzureCredential`). Lihat [Sambungkan ke Azure AI Search menggunakan peran](https://learn.microsoft.com/azure/search/search-security-rbac).

Lihat [panduan pengaturan Azure AI Search](./AzureSearch.md) untuk contoh lengkap pembuatan indeks dalam Python dan .NET.

## Pengaturan Tambahan untuk Pelajaran yang Memanggil Azure OpenAI Langsung (Pelajaran 6 dan 8)

Beberapa notebook di pelajaran 6 dan 8 memanggil **Azure OpenAI** secara langsung (menggunakan **Responses API**) tanpa melalui proyek Microsoft Foundry. Contoh ini sebelumnya menggunakan GitHub Models, yang sudah usang dan tidak mendukung Responses API. Tambahkan variabel ini ke file `.env` Anda:

| Variabel | Tempat menemukannya |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → sumber daya **Azure OpenAI** Anda → **Keys and Endpoint** → Endpoint (misal `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Nama model yang Anda deploy (misal `gpt-5-mini`) yang mendukung Responses API |
| `AZURE_OPENAI_API_KEY` | Opsional — hanya jika Anda menggunakan otentikasi berbasis kunci bukan `az login` / Entra ID |

> Responses API menggunakan endpoint stabil `/openai/v1/`, jadi tidak perlu `api-version`. Masuk dengan `az login` untuk memakai otentikasi Entra ID tanpa kunci.

## Penyedia Alternatif: MiniMax (Kompatibel dengan OpenAI)

[MiniMax](https://platform.minimaxi.com/) menyediakan model konteks besar (hingga 204K token) melalui API kompatibel OpenAI. Karena Microsoft Agent Framework `OpenAIChatClient` bekerja dengan endpoint kompatibel OpenAI apa pun, Anda dapat menggunakan MiniMax sebagai pengganti langsung untuk pelajaran yang menggunakan `OpenAIChatClient`.

Tambahkan variabel ini ke file `.env` Anda:

| Variabel | Tempat menemukannya |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Gunakan `https://api.minimax.io/v1` (nilai default) |
| `MINIMAX_MODEL_ID` | Nama model yang akan digunakan (misal `MiniMax-M3`) |

**Contoh model**: `MiniMax-M3` (disarankan), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (respon lebih cepat). Nama dan ketersediaan model dapat berubah seiring waktu, dan akses ke model tertentu mungkin bergantung pada akun Anda.

Contoh kode yang menggunakan `OpenAIChatClient` (misalnya workflow pemesanan hotel Pelajaran 14) akan otomatis mendeteksi dan menggunakan konfigurasi MiniMax Anda saat `MINIMAX_API_KEY` diatur.


## Penyedia Alternatif: Novita AI (Kompatibel dengan OpenAI)

[Novita AI](https://novita.ai/llm-api) menyediakan API kompatibel OpenAI untuk LLM sumber terbuka dan frontier (DeepSeek, Llama, Qwen, dan lainnya). Karena `OpenAIChatClient` di Microsoft Agent Framework bekerja dengan endpoint apa pun yang kompatibel dengan OpenAI, Anda dapat menggunakan Novita AI sebagai alternatif langsung untuk Azure OpenAI atau OpenAI.

Tambahkan variabel ini ke file `.env` Anda:

| Variabel | Tempat menemukannya |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | Gunakan `https://api.novita.ai/openai/v1` (nilai default) |
| `NOVITA_MODEL_ID` | Nama model yang digunakan (misal, `moonshotai/kimi-k3`) |

**Contoh model**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI juga menyelenggarakan banyak keluarga model sumber terbuka lain (Llama, Qwen, GLM, dan lainnya) — cek [perpustakaan model Novita AI](https://novita.ai/llm-api) untuk daftar model yang tersedia saat ini beserta ID modelnya.

Contoh saat ini tidak secara otomatis menggunakan variabel `NOVITA_*`. Untuk menggunakan Novita AI, berikan nilai ini secara eksplisit ketika membuat `OpenAIChatClient` di contoh yang sedang Anda jalankan.

## Penyedia Alternatif: Foundry Local (Jalankan Model di Perangkat)

[Foundry Local](https://foundrylocal.ai) adalah runtime ringan yang mengunduh, mengelola, dan menyajikan model bahasa **sepenuhnya di mesin Anda sendiri** melalui API kompatibel OpenAI — tanpa perlu cloud.

Karena `OpenAIChatClient` di Microsoft Agent Framework bekerja dengan endpoint kompatibel OpenAI apa pun, Foundry Local adalah alternatif lokal langsung untuk Azure OpenAI.

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

**3. Instal SDK Python** yang digunakan untuk mencari endpoint lokal:

```bash
pip install foundry-local-sdk
```

**4. Arahkan Microsoft Agent Framework ke model lokal Anda:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Mengunduh (jika diperlukan) dan melayani model secara lokal, kemudian menemukan endpoint/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # misalnya http://localhost:<port>/v1
    api_key=manager.api_key,        # selalu "tidak-diperlukan" untuk Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Catatan:** Foundry Local menyediakan endpoint **Chat Completions** yang kompatibel dengan OpenAI. Gunakan untuk pengembangan lokal dan skenario offline. Untuk fitur lengkap dari **Responses API** (percakapan stateful, dll.), gunakan Azure OpenAI atau proyek Microsoft Foundry.

## Pengaturan Tambahan untuk Pelajaran 8 (Alur Kerja Bing Grounding)

Notebook alur kerja kondisional di pelajaran 8 menggunakan **Bing grounding** melalui Microsoft Foundry. Jika Anda berencana menjalankan contoh itu, tambahkan variabel ini ke file `.env` Anda:

| Variabel | Tempat menemukannya |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal Microsoft Foundry → proyek Anda → **Management** → **Connected resources** → koneksi Bing Anda → salin ID koneksi |

## Pemecahan Masalah

### Kesalahan Verifikasi Sertifikat SSL di macOS

Jika Anda menggunakan macOS dan mengalami kesalahan seperti:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ini adalah masalah dikenal dengan Python di macOS di mana sertifikat SSL sistem tidak otomatis dipercaya. Cobalah solusi berikut secara berurutan:

**Opsi 1: Jalankan skrip Install Certificates Python (direkomendasikan)**

```bash
# Ganti 3.XX dengan versi Python yang Anda instal (misalnya, 3.12 atau 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opsi 2: Gunakan `connection_verify=False` di notebook Anda (hanya untuk notebook GitHub Models)**

Dalam notebook Pelajaran 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), sudah ada solusi yang dikomentari. Buka komentar `connection_verify=False` saat Anda mengalami kesalahan sertifikat:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Nonaktifkan verifikasi SSL jika Anda mengalami kesalahan sertifikat
)
```

> **⚠️ Peringatan:** Menonaktifkan verifikasi SSL (`connection_verify=False`) mengurangi keamanan dengan melewati validasi sertifikat. Gunakan ini hanya sebagai solusi sementara dalam lingkungan pengembangan. Jangan pernah gunakan di produksi.

**Opsi 3: Instal dan gunakan `truststore`**

```bash
pip install truststore
```

Kemudian tambahkan kode berikut di atas notebook atau skrip Anda sebelum melakukan panggilan jaringan apapun:

```python
import truststore
truststore.inject_into_ssl()
```

## Bingung di Mana?

Jika Anda mengalami masalah menjalankan pengaturan ini, bergabunglah ke <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> atau <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">buat isu</a>.

## Pelajaran Selanjutnya

Anda sekarang siap menjalankan kode untuk kursus ini. Selamat belajar lebih banyak tentang dunia AI Agents! 

[Pengenalan AI Agents dan Kasus Penggunaan Agen](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->