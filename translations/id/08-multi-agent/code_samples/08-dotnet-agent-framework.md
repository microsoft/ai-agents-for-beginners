# 🤝 Sistem Alur Kerja Multi-Agen Perusahaan (.NET)

## 📋 Tujuan Pembelajaran

Notebook ini menunjukkan cara membangun sistem multi-agen tingkat perusahaan yang canggih menggunakan Microsoft Agent Framework di .NET dengan Azure OpenAI (Responses API). Anda akan belajar mengorkestrasi beberapa agen khusus yang bekerja sama melalui alur kerja terstruktur, memanfaatkan fitur perusahaan .NET untuk solusi siap produksi.

**Kemampuan Multi-Agen Perusahaan yang Akan Anda Bangun:**
- 👥 **Kolaborasi Agen**: Koordinasi agen yang tipe-aman dengan validasi saat kompilasi
- 🔄 **Orkestrasi Alur Kerja**: Definisi alur kerja deklaratif dengan pola async .NET
- 🎭 **Spesialisasi Peran**: Kepribadian dan domain keahlian agen dengan tipe yang kuat
- 🏢 **Integrasi Perusahaan**: Pola siap produksi dengan pemantauan dan penanganan kesalahan

## ⚙️ Prasyarat & Pengaturan

**Lingkungan Pengembangan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan ekstensi C#
- Langganan Azure (untuk agen yang persisten)

**Paket NuGet yang Diperlukan:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Contoh Kode

Kode lengkap yang berfungsi untuk pelajaran ini tersedia di file C# yang menyertainya: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Untuk menjalankan contoh:

```bash
# Jadikan file dapat dieksekusi (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Jalankan contoh
./08-dotnet-agent-framework.cs
```

Atau menggunakan .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Apa yang Didemonstrasikan Contoh Ini

Sistem alur kerja multi-agen ini membuat layanan rekomendasi perjalanan hotel dengan dua agen khusus:

1. **Agen FrontDesk**: Agen perjalanan yang memberikan rekomendasi aktivitas dan lokasi
2. **Agen Concierge**: Meninjau rekomendasi untuk memastikan pengalaman yang autentik dan tidak turistik

Para agen bekerja bersama dalam alur kerja di mana:
- Agen FrontDesk menerima permintaan perjalanan awal
- Agen Concierge meninjau dan menyempurnakan rekomendasi
- Alur kerja mengalirkan respons secara real-time

## Konsep Utama

### Koordinasi Agen
Contoh ini mendemonstrasikan koordinasi agen yang tipe-aman menggunakan Microsoft Agent Framework dengan validasi saat kompilasi.

### Orkestrasi Alur Kerja
Menggunakan definisi alur kerja deklaratif dengan pola async .NET untuk menghubungkan beberapa agen dalam sebuah jalur.

### Streaming Respons
Mengimplementasikan streaming respons agen secara real-time menggunakan enumerables async dan arsitektur berbasis peristiwa.

### Integrasi Perusahaan
Menunjukkan pola siap produksi termasuk:
- Konfigurasi variabel lingkungan
- Manajemen kredensial yang aman
- Penanganan kesalahan
- Pemrosesan peristiwa asinkron

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->