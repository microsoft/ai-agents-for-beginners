<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:49:39+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "id"
}
-->
# 🎨 Pola Desain Agentik dengan Model GitHub (.NET)

## 📋 Tujuan Pembelajaran

Notebook ini menunjukkan pola desain tingkat perusahaan untuk membangun agen cerdas menggunakan Microsoft Agent Framework di .NET dengan integrasi Model GitHub. Anda akan mempelajari pola profesional dan pendekatan arsitektur yang membuat agen siap produksi, mudah dipelihara, dan skalabel.

**Pola Desain Perusahaan:**
- 🏭 **Factory Pattern**: Pembuatan agen yang terstandarisasi dengan dependency injection
- 🔧 **Builder Pattern**: Konfigurasi dan pengaturan agen secara fluent
- 🧵 **Thread-Safe Patterns**: Pengelolaan percakapan secara bersamaan
- 📋 **Repository Pattern**: Pengelolaan alat dan kemampuan yang terorganisir

## 🎯 Manfaat Arsitektur Khusus .NET

### Fitur Perusahaan
- **Strong Typing**: Validasi saat kompilasi dan dukungan IntelliSense
- **Dependency Injection**: Integrasi container DI bawaan
- **Manajemen Konfigurasi**: Pola IConfiguration dan Options
- **Async/Await**: Dukungan pemrograman asinkron kelas satu

### Pola Siap Produksi
- **Integrasi Logging**: Dukungan ILogger dan logging terstruktur
- **Health Checks**: Pemantauan dan diagnostik bawaan
- **Validasi Konfigurasi**: Strong typing dengan anotasi data
- **Penanganan Kesalahan**: Manajemen pengecualian yang terstruktur

## 🔧 Arsitektur Teknis

### Komponen Inti .NET
- **Microsoft.Extensions.AI**: Abstraksi layanan AI yang terpadu
- **Microsoft.Agents.AI**: Kerangka kerja orkestrasi agen tingkat perusahaan
- **Integrasi Model GitHub**: Pola klien API berkinerja tinggi
- **Sistem Konfigurasi**: Integrasi appsettings.json dan lingkungan

### Implementasi Pola Desain
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Pola Perusahaan yang Ditunjukkan

### 1. **Pola Kreasi**
- **Agent Factory**: Pembuatan agen terpusat dengan konfigurasi yang konsisten
- **Builder Pattern**: API fluent untuk konfigurasi agen yang kompleks
- **Singleton Pattern**: Pengelolaan sumber daya dan konfigurasi bersama
- **Dependency Injection**: Keterhubungan yang longgar dan mudah diuji

### 2. **Pola Perilaku**
- **Strategy Pattern**: Strategi eksekusi alat yang dapat diganti
- **Command Pattern**: Operasi agen yang terenkapsulasi dengan undo/redo
- **Observer Pattern**: Pengelolaan siklus hidup agen berbasis event
- **Template Method**: Alur kerja eksekusi agen yang terstandarisasi

### 3. **Pola Struktural**
- **Adapter Pattern**: Lapisan integrasi API Model GitHub
- **Decorator Pattern**: Peningkatan kemampuan agen
- **Facade Pattern**: Antarmuka interaksi agen yang disederhanakan
- **Proxy Pattern**: Lazy loading dan caching untuk kinerja

## ⚙️ Prasyarat & Pengaturan

**Lingkungan Pengembangan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan ekstensi C#
- Akses API Model GitHub

**Dependensi NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurasi (file .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 Prinsip Desain .NET

### Prinsip SOLID
- **Single Responsibility**: Setiap komponen memiliki satu tujuan yang jelas
- **Open/Closed**: Dapat diperluas tanpa modifikasi
- **Liskov Substitution**: Implementasi alat berbasis antarmuka
- **Interface Segregation**: Antarmuka yang fokus dan kohesif
- **Dependency Inversion**: Bergantung pada abstraksi, bukan konkret

### Arsitektur Bersih
- **Domain Layer**: Abstraksi inti agen dan alat
- **Application Layer**: Orkestrasi agen dan alur kerja
- **Infrastructure Layer**: Integrasi Model GitHub dan layanan eksternal
- **Presentation Layer**: Interaksi pengguna dan pemformatan respons

## 🔒 Pertimbangan Perusahaan

### Keamanan
- **Manajemen Kredensial**: Penanganan kunci API yang aman dengan IConfiguration
- **Validasi Input**: Strong typing dan validasi anotasi data
- **Sanitasi Output**: Pemrosesan respons yang aman dan penyaringan
- **Audit Logging**: Pelacakan operasi yang komprehensif

### Kinerja
- **Pola Asinkron**: Operasi I/O non-blok
- **Connection Pooling**: Pengelolaan klien HTTP yang efisien
- **Caching**: Caching respons untuk meningkatkan kinerja
- **Manajemen Sumber Daya**: Pola pembuangan dan pembersihan yang tepat

### Skalabilitas
- **Keamanan Thread**: Dukungan eksekusi agen secara bersamaan
- **Pengelolaan Sumber Daya**: Pemanfaatan sumber daya yang efisien
- **Manajemen Beban**: Pembatasan laju dan penanganan tekanan balik
- **Pemantauan**: Metrik kinerja dan pemeriksaan kesehatan

## 🚀 Penerapan Produksi

- **Manajemen Konfigurasi**: Pengaturan spesifik lingkungan
- **Strategi Logging**: Logging terstruktur dengan ID korelasi
- **Penanganan Kesalahan**: Penanganan pengecualian global dengan pemulihan yang tepat
- **Pemantauan**: Application insights dan penghitung kinerja
- **Pengujian**: Pola pengujian unit, integrasi, dan beban

Siap membangun agen cerdas tingkat perusahaan dengan .NET? Mari arsitekkan sesuatu yang tangguh! 🏢✨

## Contoh Kode

Untuk contoh kerja lengkap, lihat [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.