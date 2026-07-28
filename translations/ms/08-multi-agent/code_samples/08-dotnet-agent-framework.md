# 🤝 Sistem Aliran Kerja Multi-Ejen Perusahaan (.NET)

## 📋 Objektif Pembelajaran

Nota ini menunjukkan cara membina sistem multi-ejen bertaraf perusahaan yang canggih menggunakan Microsoft Agent Framework dalam .NET dengan Azure OpenAI (API Respons). Anda akan belajar mengatur beberapa ejen khusus yang bekerja bersama melalui aliran kerja yang berstruktur, memanfaatkan ciri perusahaan .NET untuk penyelesaian sedia produksi.

**Keupayaan Multi-Ejen Perusahaan yang Akan Anda Bina:**
- 👥 **Kerjasama Ejen**: Penyelarasan ejen yang selamat jenis dengan pengesahan masa kompilasi
- 🔄 **Pengaturan Aliran Kerja**: Definisi aliran kerja deklaratif dengan pola async .NET
- 🎭 **Pengkhususan Peranan**: Personaliti ejen dan bidang kepakaran yang bertipe kuat
- 🏢 **Integrasi Perusahaan**: Corak sedia produksi dengan pemantauan dan pengendalian ralat

## ⚙️ Prasyarat & Persediaan

**Persekitaran Pembangunan:**
- SDK .NET 9.0 atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan sambungan C#
- Langganan Azure (untuk ejen berterusan)

**Pakej NuGet Diperlukan:**
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

## Contoh Kod

Kod lengkap yang berfungsi untuk pelajaran ini tersedia dalam fail C# yang disertakan: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Untuk menjalankan contoh:

```bash
# Jadikan fail itu boleh dilaksanakan (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Jalankan sampel
./08-dotnet-agent-framework.cs
```

Atau menggunakan .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Apa yang Ditunjukkan Oleh Contoh Ini

Sistem aliran kerja multi-ejen ini mencipta perkhidmatan cadangan perjalanan hotel dengan dua ejen khusus:

1. **Ejen FrontDesk**: Ejen perjalanan yang menyediakan cadangan aktiviti dan lokasi
2. **Ejen Concierge**: Menyemak cadangan untuk memastikan pengalaman yang asli, bukan pelancongan

Ejen-ejen bekerja bersama dalam aliran kerja di mana:
- Ejen FrontDesk menerima permintaan perjalanan awal
- Ejen Concierge menyemak dan memperhalusi cadangan
- Aliran kerja menyiarkan respons secara masa nyata

## Konsep Utama

### Penyelarasan Ejen
Contoh menunjukkan penyelarasan ejen yang selamat jenis menggunakan Microsoft Agent Framework dengan pengesahan semasa kompilasi.

### Pengaturan Aliran Kerja
Menggunakan definisi aliran kerja deklaratif dengan pola async .NET untuk menyambungkan pelbagai ejen dalam satu saluran.

### Penstriman Respons
Melaksanakan penstriman masa nyata respons ejen menggunakan enumerable async dan seni bina berasaskan acara.

### Integrasi Perusahaan
Menunjukkan corak sedia produksi termasuk:
- Konfigurasi pembolehubah persekitaran
- Pengurusan kelayakan yang selamat
- Pengendalian ralat
- Pemprosesan acara tak segerak

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->