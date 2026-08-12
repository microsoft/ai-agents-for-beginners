# Contoh Server MCP Github

## Deskripsi

Ini adalah demo yang dibuat untuk AI Agents Hackathon yang diselenggarakan melalui Microsoft Reactor.

Alat ini digunakan untuk merekomendasikan proyek hackathon berdasarkan repositori Github pengguna.
Ini dilakukan dengan cara:

1. **Github Agent** - Menggunakan Github MCP Server untuk mengambil repositori dan informasi tentang repositori tersebut.
2. **Hackathon Agent** - Mengambil data dari Github Agent dan menghasilkan ide proyek hackathon kreatif berdasarkan proyek-proyek tersebut, bahasa yang digunakan oleh pengguna, dan jalur proyek untuk AI Agents hackathon.
3. **Events Agent** - Berdasarkan saran dari hackathon agent, events agent akan merekomendasikan acara yang relevan dari seri AI Agent Hackathon.
## Menjalankan kode 

### Variabel Lingkungan

Demo ini menggunakan Microsoft Agent Framework, Azure OpenAI Service, the Github MCP Server and Azure AI Search.

Pastikan bahwa Anda memiliki variabel lingkungan yang tepat diatur untuk menggunakan alat-alat ini:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Menjalankan Server Chainlit

Untuk terhubung ke server MCP, demo ini menggunakan Chainlit sebagai antarmuka obrolan. 

Untuk menjalankan server, gunakan perintah berikut di terminal Anda:

```bash
chainlit run app.py -w
```

Ini akan memulai server Chainlit Anda di `localhost:8000` serta mengisi Indeks Pencarian Azure AI Anda dengan konten `event-descriptions.md`. 

## Menghubungkan ke Server MCP

Untuk terhubung ke Github MCP Server, pilih ikon "plug" di bawah kotak obrolan "Type your message here..":

![Sambungkan MCP](../../../../../translated_images/id/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Dari sana Anda dapat mengklik "Sambungkan MCP" untuk menambahkan perintah guna menghubungkan ke Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Gantilah "[YOUR PERSONAL ACCESS TOKEN]" dengan Personal Access Token Anda yang sebenarnya. 

Setelah terhubung, Anda seharusnya melihat (1) di sebelah ikon plug untuk mengonfirmasi bahwa terhubung. Jika tidak, coba mulai ulang server chainlit dengan `chainlit run app.py -w`.

## Menggunakan Demo 

Untuk memulai alur kerja agen dalam merekomendasikan proyek hackathon, Anda dapat mengetik pesan seperti: 

"Rekomendasikan proyek hackathon untuk pengguna Github koreyspace"

Router Agent akan menganalisis permintaan Anda dan menentukan kombinasi agen mana (GitHub, Hackathon, dan Events) yang paling sesuai untuk menangani kueri Anda. Para agen bekerja sama untuk memberikan rekomendasi komprehensif berdasarkan analisis repositori GitHub, ide proyek, dan acara teknologi yang relevan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan terjemahan profesional oleh penerjemah manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->