<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T18:34:02+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "ms"
}
-->
# Contoh Pelayan MCP Github

## Penerangan

Ini adalah demo yang dicipta untuk Hackathon Ejen AI yang dianjurkan melalui Microsoft Reactor.

Alat ini digunakan untuk mencadangkan projek hackathon berdasarkan repositori Github pengguna. Ini dilakukan melalui:

1. **Ejen Github** - Menggunakan Pelayan MCP Github untuk mendapatkan repositori dan maklumat tentang repositori tersebut.
2. **Ejen Hackathon** - Mengambil data daripada Ejen Github dan menghasilkan idea projek hackathon yang kreatif berdasarkan projek, bahasa yang digunakan oleh pengguna, dan trek projek untuk hackathon Ejen AI.
3. **Ejen Acara** - Berdasarkan cadangan ejen hackathon, ejen acara akan mencadangkan acara yang relevan daripada siri Hackathon Ejen AI.

## Menjalankan Kod

### Pembolehubah Persekitaran

Demo ini menggunakan Azure Open AI Service, Semantic Kernel, Pelayan MCP Github, dan Azure AI Search.

Pastikan anda telah menetapkan pembolehubah persekitaran yang betul untuk menggunakan alat ini:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Menjalankan Pelayan Chainlit

Untuk menyambung ke pelayan MCP, demo ini menggunakan Chainlit sebagai antara muka sembang.

Untuk menjalankan pelayan, gunakan arahan berikut dalam terminal anda:

```bash
chainlit run app.py -w
```

Ini akan memulakan pelayan Chainlit anda pada `localhost:8000` serta mengisi Indeks Carian Azure AI anda dengan kandungan `event-descriptions.md`.

## Menyambung ke Pelayan MCP

Untuk menyambung ke Pelayan MCP Github, pilih ikon "plug" di bawah kotak sembang "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.ms.png)

Dari situ, anda boleh klik pada "Connect an MCP" untuk menambah arahan bagi menyambung ke Pelayan MCP Github:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Gantikan "[YOUR PERSONAL ACCESS TOKEN]" dengan Token Akses Peribadi anda yang sebenar.

Selepas menyambung, anda sepatutnya melihat (1) di sebelah ikon plug untuk mengesahkan bahawa ia telah disambungkan. Jika tidak, cuba mulakan semula pelayan chainlit dengan `chainlit run app.py -w`.

## Menggunakan Demo

Untuk memulakan aliran kerja ejen bagi mencadangkan projek hackathon, anda boleh menaip mesej seperti:

"Cadangkan projek hackathon untuk pengguna Github koreyspace"

Ejen Router akan menganalisis permintaan anda dan menentukan kombinasi ejen (GitHub, Hackathon, dan Acara) yang paling sesuai untuk menangani pertanyaan anda. Ejen-ejen ini akan bekerjasama untuk memberikan cadangan yang komprehensif berdasarkan analisis repositori GitHub, idea projek, dan acara teknologi yang relevan.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.