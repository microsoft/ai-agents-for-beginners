# Pengaturan Kursus

## Pengantar

Pelajaran ini akan membahas cara menjalankan contoh kode dari kursus ini.

## Bergabung dengan Peserta Lain dan Dapatkan Bantuan

Sebelum Anda mulai meng-clone repo Anda, bergabunglah dengan [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) untuk mendapatkan bantuan mengenai setup, pertanyaan tentang kursus, atau untuk terhubung dengan peserta lain.

## Clone atau Fork Repo ini

Untuk memulai, silakan clone atau fork Repositori GitHub. Ini akan membuat versi Anda sendiri dari materi kursus sehingga Anda dapat menjalankan, menguji, dan mengubah kode!

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repositori</a>

You should now have your own forked version of this course in the following link:

![Repositori yang di-fork](../../../translated_images/id/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (disarankan untuk workshop / Codespaces)

  >Repostitori penuh bisa besar (~3 GB) ketika Anda mengunduh seluruh riwayat dan semua file. Jika Anda hanya menghadiri workshop atau hanya membutuhkan beberapa folder pelajaran, shallow clone (atau sparse clone) menghindari sebagian besar unduhan tersebut dengan memotong riwayat dan/atau melewati blob.

#### Quick shallow clone — riwayat minimal, semua file

Replace `<your-username>` in the below commands with your fork URL (or the upstream URL if you prefer).

To clone only the latest commit history (small download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone a specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — blob minimal + hanya folder yang dipilih

This uses partial clone and sparse-checkout (requires Git 2.25+ and recommended modern Git with partial clone support):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Traverse into the repo folder:

```bash|powershell
cd ai-agents-for-beginners
```

Then specify which folders you want (example below shows two folders):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

After cloning and verifying the files, if you only need files and want to free space (no git history), please delete the repository metadata (💀irreversible — you will lose all Git functionality: no commits, pulls, pushes, or history access).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Menggunakan GitHub Codespaces (disarankan untuk menghindari unduhan besar lokal)

- Create a new Codespace for this repo via the [GitHub UI](https://github.com/codespaces).  

- In the terminal of the newly created codespace, run one of the shallow/sparse clone commands above to bring only the lesson folders you need into the Codespace workspace.
- Optional: after cloning inside Codespaces, remove .git to reclaim extra space (see removal commands above).
- Note: If you prefer to open the repo directly in Codespaces (without an extra clone), be aware Codespaces will construct the devcontainer environment and may still provision more than you need. Cloning a shallow copy inside a fresh Codespace gives you more control over disk usage.

#### Tips

- Always replace the clone URL with your fork if you want to edit/commit.
- If you later need more history or files, you can fetch them or adjust sparse-checkout to include additional folders.

## Menjalankan Kode

Kursus ini menyediakan serangkaian Jupyter Notebook yang dapat Anda jalankan untuk mendapatkan pengalaman langsung membangun Agen AI.

Contoh kode menggunakan **Microsoft Agent Framework (MAF)** dengan `AzureAIProjectAgentProvider`, yang terhubung ke **Azure AI Agent Service V2** (the Responses API) melalui **Microsoft Foundry**.

Semua notebook Python diberi label `*-python-agent-framework.ipynb`.

## Persyaratan

- Python 3.12+
  - **CATATAN**: Jika Anda belum menginstal Python3.12, pastikan Anda menginstalnya. Kemudian buat venv Anda menggunakan python3.12 untuk memastikan versi yang benar diinstal dari file requirements.txt.
  
    >Contoh

    Create Python venv directory:

    ```bash|powershell
    python -m venv venv
    ```

    Then activate venv environment for:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Untuk contoh kode yang menggunakan .NET, pastikan Anda menginstal [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) atau versi yang lebih baru. Kemudian, periksa versi .NET SDK yang terpasang:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Diperlukan untuk otentikasi. Instal dari [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Untuk akses ke Microsoft Foundry dan Azure AI Agent Service.
- **Microsoft Foundry Project** — Sebuah proyek dengan model yang dideploy (mis., `gpt-4o`). Lihat [Langkah 1](../../../00-course-setup) di bawah.

We have included a `requirements.txt` file in the root of this repository that contains all the required Python packages to run the code samples.

You can install them by running the following command in your terminal at the root of the repository:

```bash|powershell
pip install -r requirements.txt
```

We recommend creating a Python virtual environment to avoid any conflicts and issues.

## Menyiapkan VSCode

Make sure that you are using the right version of Python in VSCode.

![gambar](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Menyiapkan Microsoft Foundry dan Azure AI Agent Service

### Langkah 1: Buat Proyek Microsoft Foundry

Anda memerlukan Azure AI Foundry **hub** dan **project** dengan model yang dideploy untuk menjalankan notebook.

1. Go to [ai.azure.com](https://ai.azure.com) and sign in with your Azure account.
2. Create a **hub** (or use an existing one). See: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inside the hub, create a **project**.
4. Deploy a model (e.g., `gpt-4o`) from **Models + Endpoints** → **Deploy model**.

### Langkah 2: Ambil Endpoint Proyek dan Nama Deployment Model Anda

Dari proyek Anda di portal Microsoft Foundry:

- **Project Endpoint** — Buka halaman **Ikhtisar** dan salin URL endpoint.

![Project Connection String](../../../translated_images/id/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Buka **Models + Endpoints**, pilih model yang dideploy, dan catat **Deployment name** (mis., `gpt-4o`).

### Langkah 3: Masuk ke Azure dengan `az login`

Semua notebook menggunakan **`AzureCliCredential`** untuk otentikasi — tidak ada kunci API yang perlu dikelola. Ini mengharuskan Anda masuk melalui Azure CLI.

1. **Install the Azure CLI** if you haven't already: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Sign in** by running:

    ```bash|powershell
    az login
    ```

    Or if you're in a remote/Codespace environment without a browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Select your subscription** if prompted — choose the one containing your Foundry project.

4. **Verify** you're signed in:

    ```bash|powershell
    az account show
    ```

> **Mengapa `az login`?** The notebooks authenticate using `AzureCliCredential` from the `azure-identity` package. This means your Azure CLI session provides the credentials — no API keys or secrets in your `.env` file. This is a [security best practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Langkah 4: Buat File `.env` Anda

Copy the example file:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Open `.env` and fill in these two values:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variabel | Di mana menemukannya |
|----------|---------------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → your project → **Ikhtisar** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → your deployed model's name |

That's it for most lessons! The notebooks will authenticate automatically through your `az login` session.

### Langkah 5: Instal Dependensi Python

```bash|powershell
pip install -r requirements.txt
```

We recommend running this inside the virtual environment you created earlier.

## Pengaturan Tambahan untuk Pelajaran 5 (Agentic RAG)

Lesson 5 uses **Azure AI Search** for retrieval-augmented generation. If you plan to run that lesson, add these variables to your `.env` file:

| Variabel | Di mana menemukannya |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → your **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → your **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## Pengaturan Tambahan untuk Pelajaran 6 dan Pelajaran 8 (GitHub Models)

Some notebooks in lessons 6 and 8 use **GitHub Models** instead of Azure AI Foundry. If you plan to run those samples, add these variables to your `.env` file:

| Variabel | Di mana menemukannya |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Gunakan `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## Pengaturan Tambahan untuk Pelajaran 8 (Bing Grounding Workflow)

The conditional workflow notebook in lesson 8 uses **Bing grounding** via Azure AI Foundry. If you plan to run that sample, add this variable to your `.env` file:

| Variabel | Di mana menemukannya |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → your project → **Manajemen** → **Connected resources** → your Bing connection → copy the connection ID |

## Pemecahan Masalah

### Kesalahan Verifikasi Sertifikat SSL di macOS

If you are on macOS and encounter an error like:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

This is a known issue with Python on macOS where the system SSL certificates are not automatically trusted. Try the following solutions in order:

**Opsi 1: Jalankan skrip Install Certificates Python (disarankan)**

```bash
# Ganti 3.XX dengan versi Python yang terpasang (misalnya, 3.12 atau 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opsi 2: Gunakan `connection_verify=False` di notebook Anda (hanya untuk notebook GitHub Models)**

In the Lesson 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), a commented-out workaround is already included. Uncomment `connection_verify=False` when creating the client:

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

Then add the following at the top of your notebook or script before making any network calls:

```python
import truststore
truststore.inject_into_ssl()
```

## Terjebak di Suatu Tempat?

Jika Anda memiliki masalah menjalankan setup ini, masuk ke <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord Komunitas Azure AI</a> atau <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">buat issue</a>.

## Pelajaran Berikutnya

Sekarang Anda siap menjalankan kode untuk kursus ini. Selamat belajar lebih jauh tentang dunia Agen AI! 

[Pengantar Agen AI dan Kasus Penggunaan Agen](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya mencapai akurasi, harap diingat bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat krusial, disarankan menggunakan jasa penerjemah manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->