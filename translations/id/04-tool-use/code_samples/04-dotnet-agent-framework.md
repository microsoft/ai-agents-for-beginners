<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:26:42+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "id"
}
-->
# 🛠️ Penggunaan Alat Lanjutan dengan Model GitHub (.NET)

## 📋 Tujuan Pembelajaran

Notebook ini menunjukkan pola integrasi alat tingkat perusahaan menggunakan Microsoft Agent Framework di .NET dengan Model GitHub. Anda akan belajar membangun agen canggih dengan berbagai alat khusus, memanfaatkan pengetikan kuat C# dan fitur-fitur enterprise .NET.

**Kemampuan Alat Lanjutan yang Akan Anda Kuasai:**
- 🔧 **Arsitektur Multi-Alat**: Membangun agen dengan berbagai kemampuan khusus
- 🎯 **Eksekusi Alat yang Aman Tipe**: Memanfaatkan validasi waktu kompilasi C#
- 📊 **Pola Alat Enterprise**: Desain alat siap produksi dan penanganan kesalahan
- 🔗 **Komposisi Alat**: Menggabungkan alat untuk alur kerja bisnis yang kompleks

## 🎯 Manfaat Arsitektur Alat .NET

### Fitur Alat Enterprise
- **Validasi Waktu Kompilasi**: Pengetikan kuat memastikan kebenaran parameter alat
- **Dependency Injection**: Integrasi IoC container untuk pengelolaan alat
- **Pola Async/Await**: Eksekusi alat non-blok dengan pengelolaan sumber daya yang tepat
- **Logging Terstruktur**: Integrasi logging bawaan untuk pemantauan eksekusi alat

### Pola Siap Produksi
- **Penanganan Pengecualian**: Pengelolaan kesalahan yang komprehensif dengan pengecualian yang bertipe
- **Pengelolaan Sumber Daya**: Pola pembuangan yang tepat dan pengelolaan memori
- **Pemantauan Kinerja**: Metrik bawaan dan penghitung kinerja
- **Pengelolaan Konfigurasi**: Konfigurasi yang aman tipe dengan validasi

## 🔧 Arsitektur Teknis

### Komponen Alat Inti .NET
- **Microsoft.Extensions.AI**: Lapisan abstraksi alat yang terintegrasi
- **Microsoft.Agents.AI**: Orkestrasi alat tingkat perusahaan
- **Integrasi Model GitHub**: Klien API berkinerja tinggi dengan pooling koneksi

### Pipeline Eksekusi Alat
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Kategori & Pola Alat

### 1. **Alat Pemrosesan Data**
- **Validasi Input**: Pengetikan kuat dengan anotasi data
- **Operasi Transformasi**: Konversi dan format data yang aman tipe
- **Logika Bisnis**: Alat kalkulasi dan analisis spesifik domain
- **Format Output**: Generasi respons terstruktur

### 2. **Alat Integrasi**
- **Konektor API**: Integrasi layanan RESTful dengan HttpClient
- **Alat Basis Data**: Integrasi Entity Framework untuk akses data
- **Operasi File**: Operasi sistem file yang aman dengan validasi
- **Layanan Eksternal**: Pola integrasi layanan pihak ketiga

### 3. **Alat Utilitas**
- **Pemrosesan Teks**: Manipulasi string dan utilitas format
- **Operasi Tanggal/Waktu**: Kalkulasi tanggal/waktu yang sadar budaya
- **Alat Matematika**: Kalkulasi presisi dan operasi statistik
- **Alat Validasi**: Validasi aturan bisnis dan verifikasi data

## ⚙️ Prasyarat & Pengaturan

**Lingkungan Pengembangan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan ekstensi C#
- Akses API Model GitHub

**Paket NuGet yang Dibutuhkan:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurasi Lingkungan (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Siap membangun agen tingkat perusahaan dengan kemampuan alat yang kuat dan aman tipe di .NET? Mari kita arsitekkan solusi profesional! 🏢⚡

## 💻 Implementasi Kode

Implementasi lengkap C# tersedia dalam file pendamping `04-dotnet-agent-framework.cs`. Aplikasi File Tunggal .NET ini menunjukkan:

- Memuat variabel lingkungan untuk konfigurasi Model GitHub
- Mendefinisikan alat khusus menggunakan metode C# dengan atribut
- Membuat agen AI dengan integrasi alat
- Mengelola thread percakapan
- Menjalankan permintaan agen dengan pemanggilan alat

Untuk menjalankan contoh:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Atau menggunakan .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.