<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T08:46:42+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "id"
}
-->
# Pelajaran 11: Integrasi Model Context Protocol (MCP)

## Pengantar Model Context Protocol (MCP)

Model Context Protocol (MCP) adalah kerangka kerja mutakhir yang dirancang untuk menstandarisasi interaksi antara model AI dan aplikasi klien. MCP berfungsi sebagai jembatan antara model AI dan aplikasi yang menggunakannya, menyediakan antarmuka yang konsisten terlepas dari implementasi model yang mendasarinya.

Aspek utama MCP:

- **Komunikasi yang Terstandarisasi**: MCP menetapkan bahasa umum untuk aplikasi berkomunikasi dengan model AI
- **Manajemen Konteks yang Ditingkatkan**: Memungkinkan pengiriman informasi kontekstual secara efisien ke model AI
- **Kompatibilitas Lintas Platform**: Bekerja di berbagai bahasa pemrograman termasuk C#, Java, JavaScript, Python, dan TypeScript
- **Integrasi yang Mulus**: Mempermudah pengembang untuk mengintegrasikan berbagai model AI ke dalam aplikasi mereka

MCP sangat berharga dalam pengembangan agen AI karena memungkinkan agen untuk berinteraksi dengan berbagai sistem dan sumber data melalui protokol yang terintegrasi, membuat agen lebih fleksibel dan kuat.

## Tujuan Pembelajaran
- Memahami apa itu MCP dan perannya dalam pengembangan agen AI
- Menyiapkan dan mengonfigurasi server MCP untuk integrasi GitHub
- Membangun sistem multi-agen menggunakan alat MCP
- Mengimplementasikan RAG (Retrieval Augmented Generation) dengan Azure Cognitive Search

## Prasyarat
- Python 3.8+
- Node.js 14+
- Langganan Azure
- Akun GitHub
- Pemahaman dasar tentang Semantic Kernel

## Instruksi Penyiapan

1. **Penyiapan Lingkungan**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfigurasi Layanan Azure**
   - Buat sumber daya Azure Cognitive Search
   - Siapkan layanan Azure OpenAI
   - Konfigurasi variabel lingkungan di `.env`

3. **Penyiapan Server MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Struktur Proyek

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

## Komponen Inti

### 1. Sistem Multi-Agen
- Agen GitHub: Analisis repositori
- Agen Hackathon: Rekomendasi proyek
- Agen Acara: Saran acara teknologi

### 2. Integrasi Azure
- Cognitive Search untuk pengindeksan acara
- Azure OpenAI untuk kecerdasan agen
- Implementasi pola RAG

### 3. Alat MCP
- Analisis repositori GitHub
- Inspeksi kode
- Ekstraksi metadata

## Penjelasan Kode

Contoh ini menunjukkan:
1. Integrasi server MCP
2. Orkestrasi multi-agen
3. Integrasi Azure Cognitive Search
4. Implementasi pola RAG

Fitur utama:
- Analisis repositori GitHub secara real-time
- Rekomendasi proyek yang cerdas
- Pencocokan acara menggunakan Azure Search
- Respons streaming dengan Chainlit

## Menjalankan Contoh

Untuk instruksi penyiapan yang lebih rinci dan informasi lebih lanjut, lihat [README Contoh Server MCP GitHub](./code_samples/github-mcp/README.md).

1. Mulai server MCP:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Luncurkan aplikasi:
   ```bash
   chainlit run app.py -w
   ```

3. Uji integrasi:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Pemecahan Masalah

Masalah umum dan solusinya:
1. Masalah Koneksi MCP
   - Pastikan server berjalan
   - Periksa ketersediaan port
   - Konfirmasi token GitHub

2. Masalah Azure Search
   - Validasi string koneksi
   - Periksa keberadaan indeks
   - Verifikasi pengunggahan dokumen

## Langkah Selanjutnya
- Jelajahi alat MCP tambahan
- Implementasikan agen khusus
- Tingkatkan kemampuan RAG
- Tambahkan lebih banyak sumber acara
- **Lanjutan**: Lihat [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) untuk contoh komunikasi antar-agen

## Sumber Daya
- [MCP untuk Pemula](https://aka.ms/mcp-for-beginners)  
- [Dokumentasi MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Dokumen Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Panduan Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.