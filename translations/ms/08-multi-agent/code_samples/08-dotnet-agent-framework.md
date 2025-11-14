<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:17:49+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "ms"
}
-->
# 🤝 Sistem Aliran Kerja Multi-Ejen Enterprise (.NET)

## 📋 Objektif Pembelajaran

Notebook ini menunjukkan cara membina sistem multi-ejen yang canggih untuk peringkat enterprise menggunakan Microsoft Agent Framework dalam .NET dengan Model GitHub. Anda akan belajar mengatur pelbagai ejen khusus yang bekerjasama melalui aliran kerja yang terstruktur, memanfaatkan ciri-ciri enterprise .NET untuk penyelesaian yang sedia untuk pengeluaran.

**Keupayaan Multi-Ejen Enterprise yang Akan Anda Bangunkan:**
- 👥 **Kerjasama Ejen**: Penyelarasan ejen yang selamat jenis dengan pengesahan semasa kompilasi
- 🔄 **Orkestrasi Aliran Kerja**: Definisi aliran kerja secara deklaratif dengan corak async .NET
- 🎭 **Pengkhususan Peranan**: Personaliti ejen yang kuat jenis dan domain kepakaran
- 🏢 **Integrasi Enterprise**: Corak sedia pengeluaran dengan pemantauan dan pengendalian ralat

## ⚙️ Prasyarat & Persediaan

**Persekitaran Pembangunan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan sambungan C#
- Langganan Azure (untuk ejen yang berterusan)

**Pakej NuGet Diperlukan:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Contoh Kod

Kod lengkap yang berfungsi untuk pelajaran ini tersedia dalam fail C# yang disertakan: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Untuk menjalankan contoh:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Atau menggunakan CLI .NET:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Apa yang Ditunjukkan oleh Contoh Ini

Sistem aliran kerja multi-ejen ini mencipta perkhidmatan cadangan perjalanan hotel dengan dua ejen khusus:

1. **Ejen FrontDesk**: Ejen perjalanan yang menyediakan cadangan aktiviti dan lokasi
2. **Ejen Concierge**: Menyemak cadangan untuk memastikan pengalaman yang autentik dan bukan bersifat pelancongan

Ejen-ejen ini bekerjasama dalam aliran kerja di mana:
- Ejen FrontDesk menerima permintaan perjalanan awal
- Ejen Concierge menyemak dan memperhalusi cadangan
- Aliran kerja menstrim respons secara masa nyata

## Konsep Utama

### Penyelarasan Ejen
Contoh ini menunjukkan penyelarasan ejen yang selamat jenis menggunakan Microsoft Agent Framework dengan pengesahan semasa kompilasi.

### Orkestrasi Aliran Kerja
Menggunakan definisi aliran kerja secara deklaratif dengan corak async .NET untuk menghubungkan pelbagai ejen dalam satu saluran.

### Penstriman Respons
Melaksanakan penstriman respons ejen secara masa nyata menggunakan enumerasi async dan seni bina berasaskan acara.

### Integrasi Enterprise
Menunjukkan corak sedia pengeluaran termasuk:
- Konfigurasi pemboleh ubah persekitaran
- Pengurusan kelayakan yang selamat
- Pengendalian ralat
- Pemprosesan acara secara asinkron

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.