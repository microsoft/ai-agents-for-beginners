<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T18:33:53+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "id"
}
-->
# Github MCP Server Example

## Deskripsi

Ini adalah demo yang dibuat untuk AI Agents Hackathon yang diselenggarakan oleh Microsoft Reactor.

Alat ini digunakan untuk merekomendasikan proyek hackathon berdasarkan repositori Github pengguna. Prosesnya dilakukan dengan cara:

1. **Github Agent** - Menggunakan Github MCP Server untuk mengambil repositori dan informasi tentang repositori tersebut.
2. **Hackathon Agent** - Menggunakan data dari Github Agent untuk menghasilkan ide proyek hackathon yang kreatif berdasarkan proyek, bahasa pemrograman yang digunakan oleh pengguna, dan jalur proyek untuk AI Agents hackathon.
3. **Events Agent** - Berdasarkan saran dari hackathon agent, events agent akan merekomendasikan acara yang relevan dari seri AI Agent Hackathon.

## Menjalankan Kode 

### Variabel Lingkungan

Demo ini menggunakan Azure Open AI Service, Semantic Kernel, Github MCP Server, dan Azure AI Search.

Pastikan Anda telah mengatur variabel lingkungan yang sesuai untuk menggunakan alat-alat ini:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Menjalankan Chainlit Server

Untuk terhubung ke MCP server, demo ini menggunakan Chainlit sebagai antarmuka chat.

Untuk menjalankan server, gunakan perintah berikut di terminal Anda:

```bash
chainlit run app.py -w
```

Ini akan memulai Chainlit server Anda di `localhost:8000` serta mengisi Azure AI Search Index dengan konten dari `event-descriptions.md`.

## Menghubungkan ke MCP Server

Untuk terhubung ke Github MCP Server, pilih ikon "plug" di bawah kotak chat "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.id.png)

Dari sana, Anda dapat mengklik "Connect an MCP" untuk menambahkan perintah guna terhubung ke Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Ganti "[YOUR PERSONAL ACCESS TOKEN]" dengan Personal Access Token Anda yang sebenarnya.

Setelah terhubung, Anda akan melihat angka (1) di sebelah ikon plug untuk mengonfirmasi bahwa koneksi berhasil. Jika tidak, coba mulai ulang Chainlit server dengan `chainlit run app.py -w`.

## Menggunakan Demo 

Untuk memulai alur kerja agen dalam merekomendasikan proyek hackathon, Anda dapat mengetik pesan seperti:

"Rekomendasikan proyek hackathon untuk pengguna Github koreyspace"

Router Agent akan menganalisis permintaan Anda dan menentukan kombinasi agen (GitHub, Hackathon, dan Events) yang paling cocok untuk menangani permintaan Anda. Agen-agen tersebut akan bekerja sama untuk memberikan rekomendasi yang komprehensif berdasarkan analisis repositori Github, ide proyek, dan acara teknologi yang relevan.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.