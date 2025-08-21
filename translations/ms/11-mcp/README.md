<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:35:05+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ms"
}
-->
# Pelajaran 11: Integrasi Protokol Konteks Model (MCP)

## Pengenalan kepada Protokol Konteks Model (MCP)

Protokol Konteks Model (MCP) adalah kerangka kerja terkini yang direka untuk menyeragamkan interaksi antara model AI dan aplikasi klien. MCP berfungsi sebagai jambatan antara model AI dan aplikasi yang menggunakannya, menyediakan antara muka yang konsisten tanpa mengira pelaksanaan model yang mendasarinya.

Aspek utama MCP:

- **Komunikasi Standard**: MCP menetapkan bahasa umum untuk aplikasi berkomunikasi dengan model AI
- **Pengurusan Konteks yang Dipertingkatkan**: Membolehkan penghantaran maklumat kontekstual kepada model AI dengan cekap
- **Keserasian Merentas Platform**: Berfungsi merentas pelbagai bahasa pengaturcaraan termasuk C#, Java, JavaScript, Python, dan TypeScript
- **Integrasi Lancar**: Memudahkan pembangun untuk mengintegrasikan pelbagai model AI ke dalam aplikasi mereka

MCP sangat berguna dalam pembangunan ejen AI kerana ia membolehkan ejen berinteraksi dengan pelbagai sistem dan sumber data melalui protokol yang bersatu, menjadikan ejen lebih fleksibel dan berkuasa.

## Objektif Pembelajaran
- Memahami apa itu MCP dan peranannya dalam pembangunan ejen AI
- Menyediakan dan mengkonfigurasi pelayan MCP untuk integrasi GitHub
- Membina sistem multi-ejen menggunakan alat MCP
- Melaksanakan RAG (Retrieval Augmented Generation) dengan Azure Cognitive Search

## Prasyarat
- Python 3.8+
- Node.js 14+
- Langganan Azure
- Akaun GitHub
- Pemahaman asas tentang Semantic Kernel

## Arahan Persediaan

1. **Persediaan Persekitaran**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfigurasi Perkhidmatan Azure**
   - Cipta sumber Azure Cognitive Search
   - Sediakan perkhidmatan Azure OpenAI
   - Konfigurasi pembolehubah persekitaran dalam `.env`

3. **Persediaan Pelayan MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Struktur Projek

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## Komponen Utama

### 1. Sistem Multi-Ejen
- Ejen GitHub: Analisis repositori
- Ejen Hackathon: Cadangan projek
- Ejen Acara: Cadangan acara teknologi

### 2. Integrasi Azure
- Cognitive Search untuk pengindeksan acara
- Azure OpenAI untuk kecerdasan ejen
- Pelaksanaan corak RAG

### 3. Alat MCP
- Analisis repositori GitHub
- Pemeriksaan kod
- Pengekstrakan metadata

## Penjelasan Kod

Contoh ini menunjukkan:
1. Integrasi pelayan MCP
2. Orkestrasi multi-ejen
3. Integrasi Azure Cognitive Search
4. Pelaksanaan corak RAG

Ciri utama:
- Analisis repositori GitHub secara masa nyata
- Cadangan projek pintar
- Pencocokan acara menggunakan Azure Search
- Respons penstriman dengan Chainlit

## Menjalankan Contoh

Untuk arahan persediaan terperinci dan maklumat lanjut, rujuk [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Mulakan pelayan MCP:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Lancarkan aplikasi:
   ```bash
   chainlit run app.py -w
   ```

3. Uji integrasi:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Penyelesaian Masalah

Isu biasa dan penyelesaian:
1. Masalah Sambungan MCP
   - Pastikan pelayan sedang berjalan
   - Periksa ketersediaan port
   - Sahkan token GitHub

2. Masalah Azure Search
   - Sahkan rentetan sambungan
   - Periksa kewujudan indeks
   - Sahkan muat naik dokumen

## Langkah Seterusnya
- Terokai alat MCP tambahan
- Laksanakan ejen tersuai
- Tingkatkan keupayaan RAG
- Tambah lebih banyak sumber acara
- **Lanjutan**: Lihat [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) untuk contoh komunikasi ejen-ke-ejen

## Sumber
- [MCP untuk Pemula](https://aka.ms/mcp-for-beginners)  
- [Dokumentasi MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Dokumen Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Panduan Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.