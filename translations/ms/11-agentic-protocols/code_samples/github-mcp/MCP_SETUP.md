<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T18:41:00+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "ms"
}
-->
# Panduan Integrasi MCP Server

## Prasyarat
- Node.js dipasang (versi 14 atau lebih tinggi)
- Pengurus pakej npm
- Persekitaran Python dengan kebergantungan yang diperlukan

## Langkah-Langkah Persediaan

1. **Pasang Pakej MCP Server**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Mulakan MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Server akan bermula dan memaparkan URL sambungan.

3. **Sahkan Sambungan**
   - Cari ikon palam (🔌) dalam antara muka Chainlit anda
   - Nombor (1) sepatutnya muncul di sebelah ikon palam menunjukkan sambungan berjaya
   - Konsol akan menunjukkan: "GitHub plugin setup completed successfully" (bersama dengan baris status tambahan)

## Penyelesaian Masalah

### Masalah Biasa

1. **Konflik Port**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Penyelesaian: Tukar port menggunakan:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Masalah Pengesahan**
   - Pastikan kelayakan GitHub dikonfigurasi dengan betul
   - Periksa fail .env mengandungi token yang diperlukan
   - Sahkan akses API GitHub

3. **Sambungan Gagal**
   - Sahkan server berjalan pada port yang dijangka
   - Periksa tetapan firewall
   - Sahkan persekitaran Python mempunyai pakej yang diperlukan

## Pengesahan Sambungan

MCP server anda disambungkan dengan betul apabila:
1. Konsol menunjukkan "GitHub plugin setup completed successfully"
2. Log sambungan menunjukkan "✓ MCP Connection Status: Active"
3. Perintah GitHub berfungsi dalam antara muka chat

## Pembolehubah Persekitaran

Diperlukan dalam fail .env anda:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Ujian Sambungan

Hantar mesej ujian ini dalam chat:
```
Show me the repositories for username: [GitHub Username]
```
Respons yang berjaya akan menunjukkan maklumat repositori.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.