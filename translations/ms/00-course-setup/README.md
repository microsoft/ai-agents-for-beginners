# Persediaan Kursus

## Pengenalan

Pelajaran ini akan merangkumi cara menjalankan contoh kod kursus ini.

## Sertai Pelajar Lain dan Dapatkan Bantuan

Sebelum anda mula mengklon repositori anda, sertailah [saluran Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) untuk mendapatkan bantuan mengenai persediaan, sebarang soalan mengenai kursus, atau untuk berhubung dengan pelajar lain.

## Klon atau Fork Repo ini

Untuk memulakan, sila klon atau fork Repositori GitHub. Ini akan membuat versi anda sendiri bahan kursus supaya anda boleh menjalankan, menguji, dan mengubah suai kod!

Ini boleh dilakukan dengan mengklik pautan ke <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repo</a>

Anda kini sepatutnya mempunyai versi fork anda sendiri kursus ini di pautan berikut:

![Forked Repo](../../../translated_images/ms/forked-repo.33f27ca1901baa6a.webp)

### Klon Cetek (disyorkan untuk bengkel / Codespaces)

  >Repositori penuh boleh menjadi besar (~3 GB) apabila anda memuat turun sejarah penuh dan semua fail. Jika anda hanya menghadiri bengkel atau hanya memerlukan beberapa folder pelajaran, klon cetek (atau klon terpilih) memuat turun jauh lebih sedikit.

#### Klon cetek cepat — sejarah minimum, semua fail

Gantikan `<your-username>` dalam arahan di bawah dengan URL fork anda (atau URL utara jika anda lebih suka).

Untuk mengklon hanya sejarah komit terakhir (muat turun kecil):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Untuk mengklon cawangan tertentu:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Klon separa (sparse) — blob minimum + hanya folder terpilih

Ini menggunakan klon separa dan sparse-checkout (memerlukan Git 2.25+ dan disyorkan Git moden dengan sokongan klon separa):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Masuk ke dalam folder repo:

```bash
cd ai-agents-for-beginners
```

Kemudian tentukan folder yang anda mahu (contoh di bawah menunjukkan dua folder):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Selepas mengklon dan mengesahkan fail, jika anda hanya memerlukan fail dan mahu menjimatkan ruang (tiada sejarah git), sila padam metadata repositori (💀tidak boleh dipulihkan — anda akan kehilangan semua fungsi Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Menggunakan GitHub Codespaces (disyorkan untuk mengelakkan muat turun besar tempatan)

- Cipta Codespace baru untuk repo ini melalui [GitHub UI](https://github.com/codespaces).  

- Dalam terminal Codespace yang baru dibuat, jalankan salah satu arahan klon cetek/sparse di atas untuk membawa hanya folder pelajaran yang anda perlukan ke dalam ruang kerja Codespace.
- Pilihan: selepas mengklon di dalam Codespaces, padam .git untuk mendapatkan ruang tambahan (lihat arahan pemadaman di atas).
- Nota: Jika anda lebih suka membuka repo terus dalam Codespaces (tanpa klon tambahan), maklum Codespaces akan membina persekitaran devcontainer dan mungkin masih menyediakan lebih daripada yang anda perlukan.

#### Petua

- Sentiasa gantikan URL klon dengan fork anda jika anda ingin mengedit/komit.
- Jika anda memerlukan lebih banyak sejarah atau fail kemudian, anda boleh memuat turun atau menyesuaikan sparse-checkout untuk memasukkan folder tambahan.

## Menjalankan Kod

Kursus ini menawarkan siri Jupyter Notebooks yang anda boleh jalankan untuk mendapatkan pengalaman langsung membina Agen AI.

Contoh kod menggunakan **Microsoft Agent Framework (MAF)** dengan `FoundryChatClient`, yang menyambung ke **Microsoft Foundry Agent Service V2** (API Respon) melalui **Microsoft Foundry**.

Semua notebook Python dilabelkan `*-python-agent-framework.ipynb`.

## Keperluan

- Python 3.12+
  - **CATATAN**: Jika anda belum memasang Python3.12, pastikan anda memasangnya. Kemudian cipta venv anda menggunakan python3.12 untuk memastikan versi yang betul dipasang dari fail requirements.txt.
  
    >Contoh

    Cipta direktori venv Python:

    ```bash
    python -m venv venv
    ```

    Kemudian aktifkan persekitaran venv untuk:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Untuk kod contoh menggunakan .NET, pastikan anda memasang [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) atau lebih baru. Kemudian, semak versi SDK .NET yang dipasang:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Diperlukan untuk pengesahan. Pasang dari [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Langganan Azure** — Untuk akses ke Microsoft Foundry dan Microsoft Foundry Agent Service.
- **Projek Microsoft Foundry** — Projek dengan model yang telah dideploy (contoh, `gpt-5-mini`). Lihat [Langkah 1](#langkah-1-cipta-projek-microsoft-foundry) di bawah.

Kami telah sertakan fail `requirements.txt` di akar repositori ini yang mengandungi semua pakej Python yang diperlukan untuk menjalankan contoh kod.

Anda boleh memasangnya dengan menjalankan arahan berikut di terminal anda di akar repositori:

```bash
pip install -r requirements.txt
```

Kami mengesyorkan membuat persekitaran virtual Python untuk mengelakkan sebarang konflik dan isu.

## Persediaan VSCode

Pastikan anda menggunakan versi Python yang betul dalam VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Sediakan Microsoft Foundry dan Microsoft Foundry Agent Service

### Langkah 1: Cipta Projek Microsoft Foundry

Anda memerlukan **hub** dan **projek** Microsoft Foundry dengan model yang telah dideploy untuk menjalankan notebook.

1. Pergi ke [ai.azure.com](https://ai.azure.com) dan log masuk dengan akaun Azure anda.
2. Cipta **hub** (atau gunakan yang sedia ada). Lihat: [Gambaran sumber Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Dalam hub itu, cipta **projek**.
4. Deploy model (contoh, `gpt-5-mini`) dari **Models + Endpoints** → **Deploy model**.

### Langkah 2: Dapatkan Endpoint Projek dan Nama Deployment Model Anda

Dari projek anda dalam portal Microsoft Foundry:

- **Endpoint Projek** — Pergi ke halaman **Overview** dan salin URL endpoint.

![Project Connection String](../../../translated_images/ms/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nama Deployment Model** — Pergi ke **Models + Endpoints**, pilih model yang telah dideploy, dan catat **Deployment name** (contohnya, `gpt-5-mini`).

### Langkah 3: Log masuk ke Azure dengan `az login`

Kebanyakan notebook mengesahkan melalui **log masuk Azure CLI** anda — menggunakan `AzureCliCredential` atau `DefaultAzureCredential` (kedua-duanya mengambil sesi `az login` anda) dari pakej `azure-identity` — jadi ia tidak memerlukan kunci API. Beberapa pelajaran dan integrasi pilihan menggunakan kunci API; semak prasyarat setiap pelajaran untuk sebarang pembolehubah persekitaran tambahan. Ini memerlukan anda log masuk melalui Azure CLI.

1. **Pasang Azure CLI** jika anda belum: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Log masuk** dengan menjalankan:

    ```bash
    az login
    ```

    Atau jika anda dalam persekitaran jauh/Codespace tanpa pelayar:

    ```bash
    az login --use-device-code
    ```

3. **Pilih langganan anda** jika diminta — pilih yang mengandungi projek Foundry anda.

4. **Sahkan** anda log masuk:

    ```bash
    az account show
    ```

> **Kenapa `az login`?** Notebook mengesahkan menggunakan `AzureCliCredential` (atau `DefaultAzureCredential`, yang juga mengambil log masuk Azure CLI anda) dari pakej `azure-identity`. Ini bermakna sesi Azure CLI anda menyediakan kelayakan — tiada kunci API atau rahsia dalam fail `.env` anda. Ini adalah [amalan keselamatan terbaik](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Langkah 4: Cipta Fail `.env` Anda

Salin fail contoh:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Buka `.env` dan isikan kedua-dua nilai ini:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Pembolehubah | Di mana untuk cari |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → projek anda → halaman **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → nama model yang dideploy |

Itu sahaja untuk kebanyakan pelajaran! Notebook akan mengesahkan secara automatik melalui sesi `az login` anda.

### Langkah 5: Pasang Kebergantungan Python

```bash
pip install -r requirements.txt
```

Kami mengesyorkan menjalankan ini dalam persekitaran virtual yang anda cipta tadi.

## Persediaan Pilihan: Azure AI Search (Pelajaran 5 dan 16)

Notebook Pelajaran 5 (Agentic RAG) dan Pelajaran 16 berfungsi terus dengan **pangkalan pengetahuan dalam memori** — tiada sumber Azure tambahan diperlukan. Jika anda ingin menyokongnya dengan indeks **Azure AI Search** sebenar, perhatikan bahawa **notebook Pelajaran 16 kini menggunakan pengesahan berasaskan kunci**: ia bertukar dari carian dalam memori ke Azure AI Search hanya apabila **kedua-dua** `AZURE_SEARCH_SERVICE_ENDPOINT` **dan** `AZURE_SEARCH_API_KEY` ditetapkan, dan sebaliknya kekal dalam carian dalam memori — jadi untuk menjalankannya dengan indeks sebenar anda mesti tetapkan kunci admin juga. Pengesahan tanpa kunci dengan Microsoft Entra ID (RBAC) adalah pendekatan yang disyorkan untuk kod produksi anda sendiri, konsisten dengan aliran `az login` yang digunakan di seluruh kursus ini.

Langkah RBAC di bawah terpakai untuk sampel panduan persediaan dan kod anda sendiri. Ia tidak mengaktifkan pengesahan tanpa kunci dalam notebook Pelajaran 16; Pelajaran 16 masih memerlukan kedua-dua endpoint dan kunci admin untuk menggunakan Azure AI Search.

1. **Hidupkan akses berasaskan peranan** pada perkhidmatan carian anda:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Berikan diri anda peranan yang diperlukan** (cipta/muat indeks dan pertanyaan):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Tambah endpoint** ke fail `.env` anda:

| Pembolehubah | Di mana untuk cari |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → sumber **Azure AI Search** anda → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Diperlukan (dengan endpoint) untuk mengaktifkan Azure AI Search dalam notebook Pelajaran 16, yang menggunakan pengesahan berasaskan kunci. Portal Azure → **Settings** → **Keys** → kunci admin utama |

> **Kenapa tanpa kunci?** Kunci admin memberi akses tulis penuh ke perkhidmatan carian anda dan boleh bocor melalui fail `.env`. Dengan RBAC, identiti `az login` anda digunakan sebaliknya — corak Entra ID tanpa kunci yang sama yang digunakan oleh notebook kursus (melalui `AzureCliCredential` / `DefaultAzureCredential`). Lihat [Sambung ke Azure AI Search menggunakan peranan](https://learn.microsoft.com/azure/search/search-security-rbac).

Lihat [panduan persediaan Azure AI Search](./AzureSearch.md) untuk sampel penciptaan indeks penuh dalam Python dan .NET.

## Persediaan Tambahan untuk Pelajaran yang Memanggil Azure OpenAI Secara Langsung (Pelajaran 6 dan 8)

Sesetengah notebook dalam pelajaran 6 dan 8 memanggil **Azure OpenAI** secara langsung (menggunakan **Responses API**) dan bukan melalui projek Microsoft Foundry. Sampel ini sebelum ini menggunakan Model GitHub, yang telah dihentikan dan tidak menyokong Responses API. Tambahkan pembolehubah ini ke fail `.env` anda:

| Pembolehubah | Di mana untuk cari |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → sumber **Azure OpenAI** anda → **Keys and Endpoint** → Endpoint (contoh `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Nama model yang anda deploy (contoh `gpt-5-mini`) yang menyokong Responses API |
| `AZURE_OPENAI_API_KEY` | Pilihan — hanya jika anda menggunakan pengesahan berasaskan kunci dan bukan `az login` / Entra ID |

> Responses API menggunakan endpoint stabil `/openai/v1/`, jadi tiada `api-version` diperlukan. Log masuk dengan `az login` untuk menggunakan pengesahan Entra ID tanpa kunci.

## Penyedia Alternatif: MiniMax (Boleh Digunakan dengan OpenAI)

[MiniMax](https://platform.minimaxi.com/) menyediakan model konteks besar (hingga 204K token) melalui API yang serasi dengan OpenAI. Oleh kerana `OpenAIChatClient` Microsoft Agent Framework berfungsi dengan mana-mana endpoint yang serasi dengan OpenAI, anda boleh menggunakan MiniMax sebagai alternatif mudah untuk pelajaran yang menggunakan `OpenAIChatClient`.

Tambahkan pembolehubah ini ke fail `.env` anda:

| Pembolehubah | Di mana untuk cari |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Platform MiniMax](https://platform.minimaxi.com/) → Kunci API |
| `MINIMAX_BASE_URL` | Gunakan `https://api.minimax.io/v1` (nilai lalai) |
| `MINIMAX_MODEL_ID` | Nama model untuk digunakan (contoh `MiniMax-M3`) |

**Model contoh**: `MiniMax-M3` (disyorkan), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (respon lebih pantas). Nama model dan ketersediaan mungkin berubah mengikut masa, dan akses ke model tertentu bergantung pada akaun anda.

Contoh kod yang menggunakan `OpenAIChatClient` (contohnya, workflow tempahan hotel Pelajaran 14) akan secara automatik mengesan dan menggunakan konfigurasi MiniMax anda apabila `MINIMAX_API_KEY` ditetapkan.


## Penyedia Alternatif: Novita AI (Kompatibel OpenAI)

[Novita AI](https://novita.ai/llm-api) menyediakan API yang serasi dengan OpenAI untuk LLM sumber terbuka dan terkehadapan (DeepSeek, Llama, Qwen, dan banyak lagi). Oleh kerana `OpenAIChatClient` dalam Microsoft Agent Framework berfungsi dengan mana-mana titik akhir yang serasi OpenAI, anda boleh menggunakan Novita AI sebagai alternatif yang sama guna kepada Azure OpenAI atau OpenAI.

Tambah pembolehubah ini ke dalam fail `.env` anda:

| Pembolehubah | Di mana untuk cari |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → Kunci API |
| `NOVITA_BASE_URL` | Gunakan `https://api.novita.ai/openai/v1` (nilai lalai) |
| `NOVITA_MODEL_ID` | Nama model untuk digunakan (contoh, `moonshotai/kimi-k3`) |

**Contoh model**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI juga menghoskan banyak keluarga model sumber terbuka lain (Llama, Qwen, GLM, dan lain-lain) — semak [perpustakaan model Novita AI](https://novita.ai/llm-api) untuk senarai model tersedia sekarang bersama ID model mereka.

Contoh semasa tidak secara automatik mengambil pembolehubah `NOVITA_*`. Untuk menggunakan Novita AI, sampaikan nilai ini secara eksplisit apabila membina `OpenAIChatClient` dalam contoh yang anda jalankan.

## Penyedia Alternatif: Foundry Local (Jalankan Model Di Peranti)

[Foundry Local](https://foundrylocal.ai) ialah runtime ringan yang memuat turun, mengurus, dan menyampaikan model bahasa **sepenuhnya pada mesin anda sendiri** melalui API yang serasi dengan OpenAI — tanpa keperluan awan.

Oleh kerana `OpenAIChatClient` dalam Microsoft Agent Framework berfungsi dengan mana-mana titik akhir yang serasi OpenAI, Foundry Local adalah alternatif tempatan yang sama guna kepada Azure OpenAI.

**1. Pasang Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Muat turun dan jalankan model** (ini juga memulakan servis tempatan):

```bash
foundry model list          # lihat model yang tersedia
foundry model run phi-4-mini
```

**3. Pasang SDK Python** yang digunakan untuk mengesan titik akhir tempatan:

```bash
pip install foundry-local-sdk
```

**4. Tunjuk Microsoft Agent Framework kepada model tempatan anda:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Memuat turun (jika perlu) dan menyajikan model secara tempatan, kemudian mengesan titik akhir/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # contohnya http://localhost:<port>/v1
    api_key=manager.api_key,        # sentiasa "tidak diperlukan" untuk Foundry Lokal
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Nota:** Foundry Local menyediakan titik akhir **Chat Completions** yang serasi dengan OpenAI. Gunakan untuk pembangunan tempatan dan senario luar talian. Untuk set ciri penuh **Responses API** (perbualan berstatus, dan lain-lain), gunakan Azure OpenAI atau projek Microsoft Foundry.

## Persediaan Tambahan untuk Pelajaran 8 (Aliran Kerja Penetapan Bing)

Buku nota aliran kerja bersyarat dalam pelajaran 8 menggunakan **penetapan Bing** melalui Microsoft Foundry. Jika anda merancang untuk menjalankan contoh itu, tambah pembolehubah ini ke dalam fail `.env` anda:

| Pembolehubah | Di mana untuk cari |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal Microsoft Foundry → projek anda → **Pengurusan** → **Sumber bersambung** → sambungan Bing anda → salin ID sambungan |

## Penyelesaian Masalah

### Ralat Pengesahan Sijil SSL pada macOS

Jika anda menggunakan macOS dan menghadapi ralat seperti:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ini adalah isu yang diketahui dengan Python pada macOS di mana sijil SSL sistem tidak dipercayai secara automatik. Cuba penyelesaian berikut mengikut susunan:

**Pilihan 1: Jalankan skrip Pasang Sijil Python (disyorkan)**

```bash
# Gantikan 3.XX dengan versi Python yang anda pasang (contohnya, 3.12 atau 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Pilihan 2: Gunakan `connection_verify=False` dalam buku nota anda (hanya untuk buku nota Model GitHub)**

Dalam buku nota Pelajaran 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), penyelesaian kerja yang dikomen sudah termasuk. Nyahkomen `connection_verify=False` apabila anda menghadapi ralat sijil:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Nyahaktifkan pengesahan SSL jika anda menghadapi ralat sijil
)
```

> **⚠️ Amaran:** Melumpuhkan pengesahan SSL (`connection_verify=False`) mengurangkan keselamatan dengan melangkau pengesahan sijil. Gunakan ini hanya sebagai penyelesaian sementara di persekitaran pembangunan. Jangan gunakan dalam produksi.

**Pilihan 3: Pasang dan gunakan `truststore`**

```bash
pip install truststore
```

Kemudian tambah yang berikut di bahagian atas buku nota atau skrip anda sebelum membuat apa-apa panggilan rangkaian:

```python
import truststore
truststore.inject_into_ssl()
```

## Tersekat Di Mana-Mana?

Jika anda menghadapi sebarang isu menjalankan persediaan ini, sertai <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord Komuniti Azure AI</a> kami atau <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">cipta isu</a>.

## Pelajaran Seterusnya

Anda kini sedia untuk menjalankan kod bagi kursus ini. Selamat belajar lebih lanjut tentang dunia Ejen AI! 

[Pengenalan kepada Ejen AI dan Kes Penggunaan Ejen](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->