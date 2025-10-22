<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T18:40:50+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "id"
}
-->
# Panduan Integrasi Server MCP

## Prasyarat
- Node.js terinstal (versi 14 atau lebih tinggi)
- Pengelola paket npm
- Lingkungan Python dengan dependensi yang diperlukan

## Langkah-Langkah Setup

1. **Instal Paket Server MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Jalankan Server MCP**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Server akan mulai dan menampilkan URL koneksi.

3. **Verifikasi Koneksi**
   - Cari ikon colokan (🔌) di antarmuka Chainlit Anda
   - Angka (1) akan muncul di sebelah ikon colokan yang menunjukkan koneksi berhasil
   - Konsol akan menampilkan: "GitHub plugin setup completed successfully" (bersama dengan baris status tambahan)

## Pemecahan Masalah

### Masalah Umum

1. **Konflik Port**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Solusi: Ubah port menggunakan:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Masalah Autentikasi**
   - Pastikan kredensial GitHub dikonfigurasi dengan benar
   - Periksa file .env berisi token yang diperlukan
   - Verifikasi akses API GitHub

3. **Koneksi Gagal**
   - Pastikan server berjalan di port yang diharapkan
   - Periksa pengaturan firewall
   - Verifikasi lingkungan Python memiliki paket yang diperlukan

## Verifikasi Koneksi

Server MCP Anda terhubung dengan benar jika:
1. Konsol menampilkan "GitHub plugin setup completed successfully"
2. Log koneksi menunjukkan "✓ MCP Connection Status: Active"
3. Perintah GitHub berfungsi di antarmuka obrolan

## Variabel Lingkungan

Diperlukan dalam file .env Anda:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Pengujian Koneksi

Kirim pesan uji ini di obrolan:
```
Show me the repositories for username: [GitHub Username]
```
Respons yang berhasil akan menampilkan informasi repositori.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.