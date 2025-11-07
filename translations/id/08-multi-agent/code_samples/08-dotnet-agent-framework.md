<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:17:41+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "id"
}
-->
# 🤝 Sistem Alur Kerja Multi-Agen untuk Perusahaan (.NET)

## 📋 Tujuan Pembelajaran

Notebook ini menunjukkan cara membangun sistem multi-agen tingkat perusahaan yang canggih menggunakan Microsoft Agent Framework di .NET dengan Model GitHub. Anda akan belajar mengatur beberapa agen khusus yang bekerja sama melalui alur kerja terstruktur, memanfaatkan fitur-fitur enterprise .NET untuk solusi siap produksi.

**Kemampuan Multi-Agen Perusahaan yang Akan Anda Bangun:**
- 👥 **Kolaborasi Agen**: Koordinasi agen yang aman dengan validasi waktu kompilasi
- 🔄 **Orkestrasi Alur Kerja**: Definisi alur kerja deklaratif dengan pola async .NET
- 🎭 **Spesialisasi Peran**: Kepribadian agen yang bertipe kuat dan domain keahlian
- 🏢 **Integrasi Perusahaan**: Pola siap produksi dengan pemantauan dan penanganan kesalahan

## ⚙️ Prasyarat & Pengaturan

**Lingkungan Pengembangan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan ekstensi C#
- Langganan Azure (untuk agen yang persisten)

**Paket NuGet yang Diperlukan:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Contoh Kode

Kode lengkap yang berfungsi untuk pelajaran ini tersedia dalam file C# yang menyertainya: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Untuk menjalankan contoh:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Atau menggunakan .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Apa yang Ditunjukkan oleh Contoh Ini

Sistem alur kerja multi-agen ini menciptakan layanan rekomendasi perjalanan hotel dengan dua agen khusus:

1. **Agen FrontDesk**: Agen perjalanan yang memberikan rekomendasi aktivitas dan lokasi
2. **Agen Concierge**: Meninjau rekomendasi untuk memastikan pengalaman yang autentik dan tidak terlalu turis

Agen-agen ini bekerja sama dalam alur kerja di mana:
- Agen FrontDesk menerima permintaan perjalanan awal
- Agen Concierge meninjau dan menyempurnakan rekomendasi
- Alur kerja mengalirkan respons secara real-time

## Konsep Utama

### Koordinasi Agen
Contoh ini menunjukkan koordinasi agen yang aman menggunakan Microsoft Agent Framework dengan validasi waktu kompilasi.

### Orkestrasi Alur Kerja
Menggunakan definisi alur kerja deklaratif dengan pola async .NET untuk menghubungkan beberapa agen dalam pipeline.

### Streaming Respons
Mengimplementasikan streaming respons agen secara real-time menggunakan enumerables async dan arsitektur berbasis event.

### Integrasi Perusahaan
Menunjukkan pola siap produksi termasuk:
- Konfigurasi variabel lingkungan
- Pengelolaan kredensial yang aman
- Penanganan kesalahan
- Pemrosesan event secara asinkron

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.