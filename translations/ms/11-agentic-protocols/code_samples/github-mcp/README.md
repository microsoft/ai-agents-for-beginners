# Contoh Pelayan Github MCP

## Penerangan

Ini adalah demo yang dibuat untuk AI Agents Hackathon yang dianjurkan melalui Microsoft Reactor.

Alat ini digunakan untuk mencadangkan projek hackathon berdasarkan repositori Github pengguna.
Ini dilakukan dengan:

1. **Agen Github** - Menggunakan Pelayan Github MCP untuk mendapatkan repositori dan maklumat mengenai repositori tersebut.
2. **Agen Hackathon** - Mengambil data dari Agen Github dan menghasilkan idea projek hackathon kreatif berdasarkan projek, bahasa yang digunakan oleh pengguna dan trek projek untuk hackathon AI Agents.
3. **Agen Acara** - Berdasarkan cadangan agen hackathon, agen acara akan mencadangkan acara yang berkaitan dari siri AI Agent Hackathon.
## Menjalankan kod

### Pembolehubah Persekitaran

Demo ini menggunakan Microsoft Agent Framework, Azure OpenAI Service, Pelayan Github MCP dan Azure AI Search.

Pastikan anda telah menetapkan pembolehubah persekitaran yang betul untuk menggunakan alat ini:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Menjalankan Pelayan Chainlit

Untuk berhubung dengan pelayan MCP, demo ini menggunakan Chainlit sebagai antara muka sembang.

Untuk menjalankan pelayan, gunakan arahan berikut dalam terminal anda:

```bash
chainlit run app.py -w
```

Ini akan memulakan pelayan Chainlit anda pada `localhost:8000` serta mengisi Indeks Cari AI Azure anda dengan kandungan `event-descriptions.md`.

## Berhubung dengan Pelayan MCP

Untuk berhubung dengan Pelayan Github MCP, pilih ikon "plug" di bawah kotak sembang "Taip mesej anda di sini..":

![MCP Connect](../../../../../translated_images/ms/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Dari situ anda boleh klik pada "Connect an MCP" untuk menambah arahan untuk berhubung dengan Pelayan Github MCP:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Gantikan "[YOUR PERSONAL ACCESS TOKEN]" dengan Token Akses Peribadi anda yang sebenar.

Selepas berhubung, anda harus melihat (1) di sebelah ikon plug untuk mengesahkan ia telah berhubung. Jika tidak, cuba mulakan semula pelayan chainlit dengan `chainlit run app.py -w`.

## Menggunakan Demo

Untuk memulakan aliran kerja agen bagi mencadangkan projek hackathon, anda boleh menaip mesej seperti:

"Cadangkan projek hackathon untuk pengguna Github koreyspace"

Agen Router akan menganalisis permintaan anda dan menentukan kombinasi agen (GitHub, Hackathon, dan Acara) yang paling sesuai untuk mengendalikan pertanyaan anda. Agen-agen ini bekerjasama untuk memberikan cadangan menyeluruh berdasarkan analisis repositori GitHub, idea projek, dan acara teknologi yang berkaitan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau tafsiran yang salah yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->