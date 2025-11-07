<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:49:51+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "ms"
}
-->
# 🎨 Corak Reka Bentuk Agentic dengan Model GitHub (.NET)

## 📋 Objektif Pembelajaran

Notebook ini menunjukkan corak reka bentuk bertaraf perusahaan untuk membina agen pintar menggunakan Microsoft Agent Framework dalam .NET dengan integrasi Model GitHub. Anda akan mempelajari corak profesional dan pendekatan seni bina yang menjadikan agen bersedia untuk pengeluaran, mudah diselenggara, dan boleh diskalakan.

**Corak Reka Bentuk Perusahaan:**
- 🏭 **Corak Kilang**: Penciptaan agen yang standard dengan suntikan kebergantungan
- 🔧 **Corak Pembina**: Konfigurasi dan persediaan agen yang lancar
- 🧵 **Corak Selamat Benang**: Pengurusan perbualan serentak
- 📋 **Corak Repositori**: Pengurusan alat dan keupayaan yang teratur

## 🎯 Kelebihan Seni Bina Khusus .NET

### Ciri Perusahaan
- **Jenis Kuat**: Pengesahan masa kompilasi dan sokongan IntelliSense
- **Suntikan Kebergantungan**: Integrasi bekas DI terbina dalam
- **Pengurusan Konfigurasi**: Corak IConfiguration dan Options
- **Async/Await**: Sokongan pengaturcaraan tak segerak kelas pertama

### Corak Sedia Pengeluaran
- **Integrasi Log**: Sokongan ILogger dan log berstruktur
- **Pemeriksaan Kesihatan**: Pemantauan dan diagnostik terbina dalam
- **Pengesahan Konfigurasi**: Jenis kuat dengan anotasi data
- **Pengendalian Ralat**: Pengurusan pengecualian berstruktur

## 🔧 Seni Bina Teknikal

### Komponen Teras .NET
- **Microsoft.Extensions.AI**: Abstraksi perkhidmatan AI yang bersatu
- **Microsoft.Agents.AI**: Kerangka orkestrasi agen perusahaan
- **Integrasi Model GitHub**: Corak klien API berprestasi tinggi
- **Sistem Konfigurasi**: appsettings.json dan integrasi persekitaran

### Pelaksanaan Corak Reka Bentuk
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Corak Perusahaan yang Ditunjukkan

### 1. **Corak Penciptaan**
- **Kilang Agen**: Penciptaan agen yang berpusat dengan konfigurasi yang konsisten
- **Corak Pembina**: API lancar untuk konfigurasi agen yang kompleks
- **Corak Singleton**: Pengurusan sumber dan konfigurasi yang dikongsi
- **Suntikan Kebergantungan**: Penggandingan longgar dan kebolehujian

### 2. **Corak Tingkah Laku**
- **Corak Strategi**: Strategi pelaksanaan alat yang boleh ditukar ganti
- **Corak Perintah**: Operasi agen yang terkapsul dengan undo/redo
- **Corak Pemerhati**: Pengurusan kitaran hayat agen yang didorong oleh acara
- **Kaedah Templat**: Aliran kerja pelaksanaan agen yang standard

### 3. **Corak Struktur**
- **Corak Penyesuai**: Lapisan integrasi API Model GitHub
- **Corak Penghias**: Peningkatan keupayaan agen
- **Corak Fasad**: Antara muka interaksi agen yang dipermudahkan
- **Corak Proksi**: Pemuatan malas dan caching untuk prestasi

## ⚙️ Prasyarat & Persediaan

**Persekitaran Pembangunan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan sambungan C#
- Akses API Model GitHub

**Kebergantungan NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurasi (fail .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 Prinsip Reka Bentuk .NET

### Prinsip SOLID
- **Tanggungjawab Tunggal**: Setiap komponen mempunyai tujuan yang jelas
- **Terbuka/Tertutup**: Boleh diperluaskan tanpa pengubahsuaian
- **Penggantian Liskov**: Pelaksanaan alat berasaskan antara muka
- **Pemisahan Antara Muka**: Antara muka yang fokus dan padu
- **Penyongsangan Kebergantungan**: Bergantung pada abstraksi, bukan konkrit

### Seni Bina Bersih
- **Lapisan Domain**: Abstraksi alat dan agen teras
- **Lapisan Aplikasi**: Orkestrasi agen dan aliran kerja
- **Lapisan Infrastruktur**: Integrasi Model GitHub dan perkhidmatan luaran
- **Lapisan Persembahan**: Interaksi pengguna dan pemformatan respons

## 🔒 Pertimbangan Perusahaan

### Keselamatan
- **Pengurusan Kredensial**: Pengendalian kunci API yang selamat dengan IConfiguration
- **Pengesahan Input**: Jenis kuat dan pengesahan anotasi data
- **Pembersihan Output**: Pemprosesan respons yang selamat dan penapisan
- **Log Audit**: Penjejakan operasi yang komprehensif

### Prestasi
- **Corak Tak Segerak**: Operasi I/O yang tidak menyekat
- **Pengumpulan Sambungan**: Pengurusan klien HTTP yang cekap
- **Caching**: Caching respons untuk meningkatkan prestasi
- **Pengurusan Sumber**: Corak pelupusan dan pembersihan yang betul

### Skalabiliti
- **Keselamatan Benang**: Sokongan pelaksanaan agen serentak
- **Pengumpulan Sumber**: Penggunaan sumber yang cekap
- **Pengurusan Beban**: Had kadar dan pengendalian tekanan balik
- **Pemantauan**: Metrik prestasi dan pemeriksaan kesihatan

## 🚀 Pengeluaran Pengeluaran

- **Pengurusan Konfigurasi**: Tetapan khusus persekitaran
- **Strategi Log**: Log berstruktur dengan ID korelasi
- **Pengendalian Ralat**: Pengendalian pengecualian global dengan pemulihan yang betul
- **Pemantauan**: Wawasan aplikasi dan kaunter prestasi
- **Pengujian**: Corak ujian unit, ujian integrasi, dan ujian beban

Sedia untuk membina agen pintar bertaraf perusahaan dengan .NET? Mari kita seni bina sesuatu yang kukuh! 🏢✨

## Contoh Kod

Untuk contoh kerja lengkap, lihat [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.