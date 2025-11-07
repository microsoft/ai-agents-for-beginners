<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:06:18+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "id"
}
-->
# 🔍 Enterprise RAG dengan Azure AI Foundry (.NET)

## 📋 Tujuan Pembelajaran

Notebook ini menunjukkan cara membangun sistem Retrieval-Augmented Generation (RAG) tingkat perusahaan menggunakan Microsoft Agent Framework di .NET dengan Azure AI Foundry. Anda akan belajar membuat agen siap produksi yang dapat mencari dokumen dan memberikan respons yang akurat serta kontekstual dengan keamanan dan skalabilitas tingkat perusahaan.

**Kemampuan Enterprise RAG yang Akan Anda Bangun:**
- 📚 **Kecerdasan Dokumen**: Pemrosesan dokumen canggih dengan layanan Azure AI
- 🔍 **Pencarian Semantik**: Pencarian vektor berkinerja tinggi dengan fitur perusahaan
- 🛡️ **Integrasi Keamanan**: Akses berbasis peran dan pola perlindungan data
- 🏢 **Arsitektur Skalabel**: Sistem RAG siap produksi dengan pemantauan

## 🎯 Arsitektur Enterprise RAG

### Komponen Inti Perusahaan
- **Azure AI Foundry**: Platform AI perusahaan yang dikelola dengan keamanan dan kepatuhan
- **Agen Persisten**: Agen dengan riwayat percakapan dan manajemen konteks
- **Manajemen Vector Store**: Pengindeksan dan pengambilan dokumen tingkat perusahaan
- **Integrasi Identitas**: Autentikasi Azure AD dan kontrol akses berbasis peran

### Manfaat .NET untuk Perusahaan
- **Keamanan Tipe**: Validasi waktu kompilasi untuk operasi RAG dan struktur data
- **Kinerja Asinkron**: Pemrosesan dokumen dan operasi pencarian yang tidak memblokir
- **Manajemen Memori**: Pemanfaatan sumber daya yang efisien untuk koleksi dokumen besar
- **Pola Integrasi**: Integrasi layanan Azure secara native dengan dependency injection

## 🏗️ Arsitektur Teknis

### Pipeline Enterprise RAG
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Komponen Inti .NET
- **Azure.AI.Agents.Persistent**: Manajemen agen perusahaan dengan persistensi status
- **Azure.Identity**: Autentikasi terintegrasi untuk akses layanan Azure yang aman
- **Microsoft.Agents.AI.AzureAI**: Implementasi kerangka kerja agen yang dioptimalkan untuk Azure
- **System.Linq.Async**: Operasi LINQ asinkron berkinerja tinggi

## 🔧 Fitur & Manfaat Enterprise

### Keamanan & Kepatuhan
- **Integrasi Azure AD**: Manajemen identitas perusahaan dan autentikasi
- **Akses Berbasis Peran**: Izin yang terperinci untuk akses dokumen dan operasi
- **Perlindungan Data**: Enkripsi saat istirahat dan dalam transit untuk dokumen sensitif
- **Audit Logging**: Pelacakan aktivitas yang komprehensif untuk persyaratan kepatuhan

### Kinerja & Skalabilitas
- **Connection Pooling**: Manajemen koneksi layanan Azure yang efisien
- **Pemrosesan Asinkron**: Operasi yang tidak memblokir untuk skenario throughput tinggi
- **Strategi Caching**: Caching cerdas untuk dokumen yang sering diakses
- **Load Balancing**: Pemrosesan terdistribusi untuk penerapan skala besar

### Manajemen & Pemantauan
- **Health Checks**: Pemantauan bawaan untuk komponen sistem RAG
- **Metode Kinerja**: Analitik terperinci tentang kualitas pencarian dan waktu respons
- **Penanganan Kesalahan**: Manajemen pengecualian yang komprehensif dengan kebijakan retry
- **Manajemen Konfigurasi**: Pengaturan spesifik lingkungan dengan validasi

## ⚙️ Prasyarat & Pengaturan

**Lingkungan Pengembangan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan ekstensi C#
- Langganan Azure dengan akses AI Foundry

**Paket NuGet yang Dibutuhkan:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Pengaturan Autentikasi Azure:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Konfigurasi Lingkungan:**
* Konfigurasi Azure AI Foundry (ditangani secara otomatis melalui Azure CLI)
* Pastikan Anda telah terautentikasi ke langganan Azure yang benar

## 📊 Pola Enterprise RAG

### Pola Manajemen Dokumen
- **Unggahan Massal**: Pemrosesan koleksi dokumen besar secara efisien
- **Pembaruan Bertahap**: Penambahan dan modifikasi dokumen secara real-time
- **Kontrol Versi**: Versi dokumen dan pelacakan perubahan
- **Manajemen Metadata**: Atribut dokumen yang kaya dan taksonomi

### Pola Pencarian & Pengambilan
- **Pencarian Hibrid**: Menggabungkan pencarian semantik dan kata kunci untuk hasil optimal
- **Pencarian Berfasilitas**: Penyaringan dan kategorisasi multi-dimensi
- **Penyetelan Relevansi**: Algoritma penilaian khusus untuk kebutuhan spesifik domain
- **Peringkat Hasil**: Peringkat lanjutan dengan integrasi logika bisnis

### Pola Keamanan
- **Keamanan Tingkat Dokumen**: Kontrol akses terperinci per dokumen
- **Klasifikasi Data**: Pelabelan sensitivitas otomatis dan perlindungan
- **Jejak Audit**: Logging komprehensif dari semua operasi RAG
- **Perlindungan Privasi**: Deteksi dan redaksi PII

## 🔒 Fitur Keamanan Enterprise

### Autentikasi & Otorisasi
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### Perlindungan Data
- **Enkripsi**: Enkripsi ujung ke ujung untuk dokumen dan indeks pencarian
- **Kontrol Akses**: Integrasi dengan Azure AD untuk izin pengguna dan grup
- **Residensi Data**: Kontrol lokasi geografis data untuk kepatuhan
- **Cadangan & Pemulihan**: Kemampuan cadangan dan pemulihan bencana otomatis

## 📈 Optimasi Kinerja

### Pola Pemrosesan Asinkron
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Manajemen Memori
- **Pemrosesan Streaming**: Menangani dokumen besar tanpa masalah memori
- **Pengumpulan Sumber Daya**: Penggunaan ulang sumber daya mahal secara efisien
- **Pengumpulan Sampah**: Pola alokasi memori yang dioptimalkan
- **Manajemen Koneksi**: Siklus hidup koneksi layanan Azure yang tepat

### Strategi Caching
- **Caching Query**: Cache pencarian yang sering dilakukan
- **Caching Dokumen**: Caching dalam memori untuk dokumen yang sering diakses
- **Caching Indeks**: Caching indeks vektor yang dioptimalkan
- **Caching Hasil**: Caching cerdas dari respons yang dihasilkan

## 📊 Kasus Penggunaan Enterprise

### Manajemen Pengetahuan
- **Wiki Perusahaan**: Pencarian cerdas di basis pengetahuan perusahaan
- **Kebijakan & Prosedur**: Panduan kepatuhan dan prosedur otomatis
- **Materi Pelatihan**: Bantuan pembelajaran dan pengembangan yang cerdas
- **Basis Data Penelitian**: Sistem analisis makalah akademik dan penelitian

### Dukungan Pelanggan
- **Basis Pengetahuan Dukungan**: Respons layanan pelanggan otomatis
- **Dokumentasi Produk**: Pengambilan informasi produk yang cerdas
- **Panduan Pemecahan Masalah**: Bantuan pemecahan masalah yang kontekstual
- **Sistem FAQ**: Pembuatan FAQ dinamis dari koleksi dokumen

### Kepatuhan Regulasi
- **Analisis Dokumen Hukum**: Kecerdasan kontrak dan dokumen hukum
- **Pemantauan Kepatuhan**: Pemeriksaan kepatuhan regulasi otomatis
- **Penilaian Risiko**: Analisis dan pelaporan risiko berbasis dokumen
- **Dukungan Audit**: Penemuan dokumen cerdas untuk audit

## 🚀 Penerapan Produksi

### Pemantauan & Observabilitas
- **Application Insights**: Telemetri terperinci dan pemantauan kinerja
- **Metode Kustom**: Pelacakan KPI spesifik bisnis dan pemberitahuan
- **Tracing Terdistribusi**: Pelacakan permintaan ujung ke ujung di seluruh layanan
- **Dasbor Kesehatan**: Visualisasi kesehatan sistem dan kinerja secara real-time

### Skalabilitas & Keandalan
- **Auto-Scaling**: Skalabilitas otomatis berdasarkan beban dan metrik kinerja
- **Ketersediaan Tinggi**: Penerapan multi-region dengan kemampuan failover
- **Pengujian Beban**: Validasi kinerja di bawah kondisi beban perusahaan
- **Pemulihan Bencana**: Prosedur cadangan dan pemulihan otomatis

Siap membangun sistem RAG tingkat perusahaan yang dapat menangani dokumen sensitif dalam skala besar? Mari arsitek sistem pengetahuan cerdas untuk perusahaan! 🏢📖✨

## Implementasi Kode

Contoh kode lengkap untuk pelajaran ini tersedia di `05-dotnet-agent-framework.cs`. 

Untuk menjalankan contoh:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Atau gunakan `dotnet run` secara langsung:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kode ini menunjukkan:

1. **Instalasi Paket**: Menginstal paket NuGet yang diperlukan untuk Azure AI Agents
2. **Konfigurasi Lingkungan**: Memuat endpoint Azure AI Foundry dan pengaturan model
3. **Unggahan Dokumen**: Mengunggah dokumen untuk pemrosesan RAG
4. **Pembuatan Vector Store**: Membuat vector store untuk pencarian semantik
5. **Konfigurasi Agen**: Menyiapkan agen AI dengan kemampuan pencarian file
6. **Eksekusi Query**: Menjalankan query terhadap dokumen yang diunggah

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.