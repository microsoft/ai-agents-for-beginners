# 🔍 Enterprise RAG dengan Microsoft Foundry (.NET)

## 📋 Tujuan Pembelajaran

Notebook ini menunjukkan cara membangun sistem Retrieval-Augmented Generation (RAG) kelas enterprise menggunakan Microsoft Agent Framework di .NET dengan Microsoft Foundry. Anda akan belajar membuat agen siap produksi yang dapat mencari melalui dokumen dan memberikan respons yang akurat, kontekstual, dengan keamanan dan skalabilitas enterprise.

**Kemampuan Enterprise RAG yang Akan Anda Bangun:**
- 📚 **Kecerdasan Dokumen**: Pemrosesan dokumen tingkat lanjut dengan layanan Azure AI
- 🔍 **Pencarian Semantik**: Pencarian vektor berkinerja tinggi dengan fitur enterprise
- 🛡️ **Integrasi Keamanan**: Akses berbasis peran dan pola perlindungan data
- 🏢 **Arsitektur Skalabel**: Sistem RAG siap produksi dengan pemantauan

## 🎯 Arsitektur Enterprise RAG

### Komponen Inti Enterprise
- **Microsoft Foundry**: Platform AI enterprise terkelola dengan keamanan dan kepatuhan
- **Agen Persisten**: Agen stateful dengan riwayat percakapan dan manajemen konteks
- **Manajemen Penyimpanan Vektor**: Pengindeksan dan pengambilan dokumen kelas enterprise
- **Integrasi Identitas**: Otentikasi Azure AD dan kontrol akses berbasis peran

### Manfaat .NET untuk Enterprise
- **Keamanan Tipe**: Validasi waktu kompilasi untuk operasi RAG dan struktur data
- **Kinerja Async**: Pemrosesan dokumen dan operasi pencarian tanpa blocking
- **Manajemen Memori**: Pemanfaatan sumber daya efisien untuk koleksi dokumen besar
- **Pola Integrasi**: Integrasi layanan Azure asli dengan dependency injection

## 🏗️ Arsitektur Teknis

### Pipeline Enterprise RAG
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Komponen Inti .NET
- **Azure.AI.Agents.Persistent**: Manajemen agen enterprise dengan persistensi state
- **Azure.Identity**: Otentikasi terintegrasi untuk akses layanan Azure yang aman
- **Microsoft.Agents.AI.AzureAI**: Implementasi framework agen teroptimasi Azure
- **System.Linq.Async**: Operasi LINQ asinkron berkinerja tinggi

## 🔧 Fitur & Manfaat Enterprise

### Keamanan & Kepatuhan
- **Integrasi Azure AD**: Manajemen identitas dan otentikasi enterprise
- **Akses Berbasis Peran**: Izin granular untuk akses dan operasi dokumen
- **Perlindungan Data**: Enkripsi saat penyimpanan dan transmisi untuk dokumen sensitif
- **Pencatatan Audit**: Pelacakan aktivitas komprehensif untuk persyaratan kepatuhan

### Kinerja & Skalabilitas
- **Pooling Koneksi**: Manajemen koneksi layanan Azure yang efisien
- **Pemrosesan Async**: Operasi tanpa blocking untuk skenario throughput tinggi
- **Strategi Caching**: Caching cerdas untuk dokumen yang sering diakses
- **Load Balancing**: Pemrosesan terdistribusi untuk deployment berskala besar

### Manajemen & Pemantauan
- **Health Checks**: Pemantauan bawaan untuk komponen sistem RAG
- **Metrik Kinerja**: Analitik rinci tentang kualitas pencarian dan waktu respons
- **Penanganan Error**: Manajemen exception komprehensif dengan kebijakan retry
- **Manajemen Konfigurasi**: Pengaturan khusus lingkungan dengan validasi

## ⚙️ Prasyarat & Penyiapan

**Lingkungan Pengembangan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan ekstensi C#
- Langganan Azure dengan akses Microsoft Foundry

**Paket NuGet yang Diperlukan:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Pengaturan Otentikasi Azure:**
```bash
# Instal Azure CLI dan otentikasi
az login
az account set --subscription "your-subscription-id"
```

**Konfigurasi Lingkungan:**
* Konfigurasi Microsoft Foundry (ditangani otomatis melalui Azure CLI)
* Pastikan Anda terautentikasi ke langganan Azure yang benar

## 📊 Pola Enterprise RAG

### Pola Manajemen Dokumen
- **Unggah Massal**: Pemrosesan efisien koleksi dokumen besar
- **Pembaruan Inkremental**: Penambahan dan modifikasi dokumen secara real-time
- **Kontrol Versi**: Versi dokumen dan pelacakan perubahan
- **Manajemen Metadata**: Atribut dokumen yang kaya dan taksonomi

### Pola Pencarian & Pengambilan
- **Pencarian Hibrid**: Menggabungkan pencarian semantik dan kata kunci untuk hasil optimal
- **Pencarian Berfaset**: Penyaringan dan kategorisasi multidimensi
- **Penyetelan Relevansi**: Algoritma skor kustom untuk kebutuhan domain khusus
- **Peringkat Hasil**: Peringkat canggih dengan integrasi logika bisnis

### Pola Keamanan
- **Keamanan Level Dokumen**: Kontrol akses granulasi per dokumen
- **Klasifikasi Data**: Pelabelan sensitivitas otomatis dan perlindungan
- **Jejak Audit**: Pencatatan komprehensif semua operasi RAG
- **Perlindungan Privasi**: Deteksi dan redaksi PII

## 🔒 Fitur Keamanan Enterprise

### Otentikasi & Otorisasi
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
- **Enkripsi**: Enkripsi ujung-ke-ujung untuk dokumen dan indeks pencarian
- **Kontrol Akses**: Integrasi dengan Azure AD untuk izin pengguna dan grup
- **Residen Data**: Kontrol lokasi geografis data untuk kepatuhan
- **Cadangan & Pemulihan**: Kapabilitas cadangan otomatis dan pemulihan bencana

## 📈 Optimasi Kinerja

### Pola Pemrosesan Async
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Manajemen Memori
- **Pemrosesan Streaming**: Menangani dokumen besar tanpa masalah memori
- **Pooling Sumber Daya**: Pemanfaatan ulang sumber daya mahal secara efisien
- **Pengumpulan Sampah**: Pola pengalokasian memori yang dioptimalkan
- **Manajemen Koneksi**: Siklus hidup koneksi layanan Azure yang tepat

### Strategi Caching
- **Caching Query**: Cache pencarian yang sering dijalankan
- **Caching Dokumen**: Caching dalam memori untuk dokumen panas
- **Caching Indeks**: Caching indeks vektor yang dioptimalkan
- **Caching Hasil**: Caching cerdas dari respons yang dihasilkan

## 📊 Kasus Penggunaan Enterprise

### Manajemen Pengetahuan
- **Wiki Perusahaan**: Pencarian cerdas di seluruh basis pengetahuan perusahaan
- **Kebijakan & Prosedur**: Otomatisasi kepatuhan dan panduan prosedur
- **Materi Pelatihan**: Bantuan pembelajaran dan pengembangan yang cerdas
- **Database Riset**: Sistem analisis makalah akademik dan riset

### Dukungan Pelanggan
- **Basis Pengetahuan Dukungan**: Respons pelayanan pelanggan otomatis
- **Dokumentasi Produk**: Pengambilan informasi produk yang cerdas
- **Panduan Pemecahan Masalah**: Bantuan pemecahan masalah kontekstual
- **Sistem FAQ**: Generasi FAQ dinamis dari koleksi dokumen

### Kepatuhan Regulasi
- **Analisis Dokumen Hukum**: Kecerdasan kontrak dan dokumen hukum
- **Pemantauan Kepatuhan**: Pemeriksaan kepatuhan regulasi otomatis
- **Penilaian Risiko**: Analisis risiko dan pelaporan berbasis dokumen
- **Dukungan Audit**: Penemuan dokumen cerdas untuk audit

## 🚀 Deploy Produksi

### Pemantauan & Observabilitas
- **Application Insights**: Telemetri rinci dan pemantauan kinerja
- **Metrik Kustom**: Pelacakan dan pemberitahuan KPI khusus bisnis
- **Distributed Tracing**: Pelacakan permintaan ujung-ke-ujung antar layanan
- **Health Dashboards**: Visualisasi kesehatan sistem dan kinerja real-time

### Skalabilitas & Keandalan
- **Auto-Scaling**: Skala otomatis berdasarkan beban dan metrik kinerja
- **Ketersediaan Tinggi**: Deploy multi-region dengan kapabilitas failover
- **Uji Beban**: Validasi kinerja di bawah kondisi beban enterprise
- **Pemulihan Bencana**: Prosedur cadangan dan pemulihan otomatis

Siap membangun sistem RAG kelas enterprise yang dapat menangani dokumen sensitif dalam skala besar? Mari arsitek sistem pengetahuan cerdas untuk enterprise! 🏢📖✨

## Implementasi Kode

Contoh kode lengkap untuk pelajaran ini tersedia di `05-dotnet-agent-framework.cs`.

Untuk menjalankan contoh:

```bash
# Jadikan skrip executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Jalankan Aplikasi .NET File Tunggal
./05-dotnet-agent-framework.cs
```

Atau gunakan `dotnet run` langsung:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kode ini mendemonstrasikan:

1. **Instalasi Paket**: Menginstal paket NuGet yang diperlukan untuk Azure AI Agents
2. **Konfigurasi Lingkungan**: Memuat endpoint Microsoft Foundry dan pengaturan model
3. **Unggah Dokumen**: Mengunggah dokumen untuk pemrosesan RAG
4. **Pembuatan Penyimpanan Vektor**: Membuat vector store untuk pencarian semantik
5. **Konfigurasi Agen**: Menyiapkan agen AI dengan kemampuan pencarian file
6. **Eksekusi Query**: Menjalankan kueri terhadap dokumen yang diunggah

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->