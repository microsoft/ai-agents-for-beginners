# 🔍 Enterprise RAG dengan Microsoft Foundry (.NET)

## 📋 Tujuan Pembelajaran

Notebook ini menunjukkan cara membangun sistem Retrieval-Augmented Generation (RAG) kelas enterprise menggunakan Microsoft Agent Framework di .NET dengan Microsoft Foundry. Anda akan belajar membuat agen siap produksi yang dapat mencari melalui dokumen dan memberikan respons yang akurat dan sadar konteks dengan keamanan dan skalabilitas enterprise.

**Kemampuan Enterprise RAG yang Akan Anda Bangun:**
- 📚 **Intelijen Dokumen**: Proses dokumen tingkat lanjut dengan layanan Azure AI
- 🔍 **Pencarian Semantik**: Pencarian vektor berkinerja tinggi dengan fitur enterprise
- 🛡️ **Integrasi Keamanan**: Akses berbasis peran dan pola perlindungan data
- 🏢 **Arsitektur Skalabel**: Sistem RAG siap produksi dengan pemantauan

## 🎯 Arsitektur Enterprise RAG

### Komponen Utama Enterprise
- **Microsoft Foundry**: Platform AI enterprise yang dikelola dengan keamanan dan kepatuhan
- **Agen Persisten**: Agen stateful dengan riwayat percakapan dan manajemen konteks
- **Manajemen Penyimpanan Vektor**: Pengindeksan dan pengambilan dokumen kelas enterprise
- **Integrasi Identitas**: Autentikasi Azure AD dan kontrol akses berbasis peran

### Manfaat .NET Enterprise
- **Keamanan Tipe**: Validasi waktu kompilasi untuk operasi dan struktur data RAG
- **Kinerja Async**: Pemrosesan dokumen dan operasi pencarian non-blokir
- **Manajemen Memori**: Pemanfaatan sumber daya yang efisien untuk koleksi dokumen besar
- **Pola Integrasi**: Integrasi layanan Azure asli dengan dependency injection

## 🏗️ Arsitektur Teknis

### Pipeline Enterprise RAG
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Komponen .NET Inti
- **Azure.AI.Agents.Persistent**: Pengelolaan agen enterprise dengan persistence state
- **Azure.Identity**: Autentikasi terintegrasi untuk akses layanan Azure yang aman
- **Microsoft.Agents.AI.AzureAI**: Implementasi kerangka agen yang dioptimalkan untuk Azure
- **System.Linq.Async**: Operasi LINQ asinkron berkinerja tinggi

## 🔧 Fitur & Manfaat Enterprise

### Keamanan & Kepatuhan
- **Integrasi Azure AD**: Manajemen identitas dan autentikasi enterprise
- **Akses Berbasis Peran**: Izin granular untuk akses serta operasi dokumen
- **Perlindungan Data**: Enkripsi saat istirahat dan saat transit untuk dokumen sensitif
- **Audit Logging**: Pelacakan aktivitas komprehensif untuk kebutuhan kepatuhan

### Kinerja & Skalabilitas
- **Connection Pooling**: Manajemen koneksi layanan Azure yang efisien
- **Pemrosesan Async**: Operasi non-blokir untuk skenario throughput tinggi
- **Strategi Caching**: Caching cerdas untuk dokumen yang sering diakses
- **Load Balancing**: Pemrosesan terdistribusi untuk deployment skala besar

### Manajemen & Pemantauan
- **Health Checks**: Pemantauan bawaan untuk komponen sistem RAG
- **Metrik Kinerja**: Analitik rinci mengenai kualitas pencarian dan waktu respons
- **Penanganan Error**: Manajemen exception komprehensif dengan kebijakan pengulangan
- **Manajemen Konfigurasi**: Pengaturan lingkungan khusus dengan validasi

## ⚙️ Prasyarat & Pengaturan

**Lingkungan Pengembangan:**
- SDK .NET 9.0 atau lebih tinggi
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

**Pengaturan Autentikasi Azure:**
```bash
# Instal Azure CLI dan autentikasi
az login
az account set --subscription "your-subscription-id"
```

**Konfigurasi Lingkungan:**
* Konfigurasi Microsoft Foundry (ditangani otomatis melalui Azure CLI)
* Pastikan Anda sudah autentikasi ke langganan Azure yang benar

## 📊 Pola Enterprise RAG

### Pola Manajemen Dokumen
- **Unggah Massal**: Pemrosesan efisien koleksi dokumen besar
- **Pembaruan Bertahap**: Penambahan dan modifikasi dokumen secara real-time
- **Kontrol Versi**: Versi dokumen dan pelacakan perubahan
- **Manajemen Metadata**: Atribut dokumen yang kaya dan taksonomi

### Pola Pencarian & Pengambilan
- **Pencarian Hibrid**: Menggabungkan pencarian semantik dan kata kunci untuk hasil optimal
- **Pencarian Berfased**: Penyaringan dan kategorisasi multi-dimensi
- **Penyetelan Relevansi**: Algoritma skor kustom untuk kebutuhan domain spesifik
- **Peringkat Hasil**: Peringkat lanjutan dengan integrasi logika bisnis

### Pola Keamanan
- **Keamanan Tingkat Dokumen**: Kontrol akses granular per dokumen
- **Klasifikasi Data**: Pelabelan sensitivitas otomatis dan perlindungan
- **Audit Trails**: Logging komprehensif semua operasi RAG
- **Perlindungan Privasi**: Deteksi dan penghapusan data pribadi (PII)

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
- **Enkripsi**: Enkripsi ujung-ke-ujung untuk dokumen dan indeks pencarian
- **Kontrol Akses**: Integrasi dengan Azure AD untuk izin pengguna dan grup
- **Residensi Data**: Kontrol lokasi data geografis untuk kepatuhan
- **Backup & Recovery**: Kemampuan backup otomatis dan pemulihan bencana

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
- **Pooling Sumber Daya**: Pemakaian ulang sumber daya mahal yang efisien
- **Pengumpulan Sampah**: Pola alokasi memori yang dioptimalkan
- **Manajemen Koneksi**: Siklus hidup koneksi layanan Azure yang tepat

### Strategi Caching
- **Caching Query**: Cache pencarian yang sering dieksekusi
- **Caching Dokumen**: Caching di memori untuk dokumen panas
- **Caching Indeks**: Caching indeks vektor yang dioptimalkan
- **Caching Hasil**: Caching cerdas dari respons yang dihasilkan

## 📊 Kasus Penggunaan Enterprise

### Manajemen Pengetahuan
- **Wiki Perusahaan**: Pencarian cerdas di basis pengetahuan perusahaan
- **Kebijakan & Prosedur**: Kepatuhan otomatis dan panduan prosedur
- **Materi Pelatihan**: Bantuan pembelajaran dan pengembangan cerdas
- **Basis Data Riset**: Sistem analisis makalah akademik dan riset

### Dukungan Pelanggan
- **Basis Pengetahuan Dukungan**: Respons layanan pelanggan otomatis
- **Dokumentasi Produk**: Pengambilan informasi produk cerdas
- **Panduan Pemecahan Masalah**: Bantuan pemecahan masalah kontekstual
- **Sistem FAQ**: Generasi FAQ dinamis dari koleksi dokumen

### Kepatuhan Regulasi
- **Analisis Dokumen Hukum**: Intelijen kontrak dan dokumen hukum
- **Pemantauan Kepatuhan**: Pemeriksaan kepatuhan regulasi otomatis
- **Penilaian Risiko**: Analisis risiko berbasis dokumen dan pelaporan
- **Dukungan Audit**: Penemuan dokumen cerdas untuk audit

## 🚀 Deploy Produksi

### Pemantauan & Observabilitas
- **Application Insights**: Telemetri rinci dan pemantauan kinerja
- **Metrik Kustom**: Pelacakan dan pengingat KPI spesifik bisnis
- **Distributed Tracing**: Pelacakan permintaan ujung ke ujung antar layanan
- **Dashboard Kesehatan**: Visualisasi waktu nyata kesehatan dan kinerja sistem

### Skalabilitas & Keandalan
- **Auto-Scaling**: Skala otomatis berdasarkan beban dan metrik kinerja
- **High Availability**: Deployment multi-wilayah dengan kemampuan failover
- **Load Testing**: Validasi kinerja dalam kondisi beban enterprise
- **Disaster Recovery**: Prosedur backup dan pemulihan otomatis

Siap membangun sistem RAG kelas enterprise yang dapat menangani dokumen sensitif dalam skala besar? Mari arsitek sistem pengetahuan cerdas untuk enterprise! 🏢📖✨

## Implementasi Kode

Contoh kode lengkap untuk pelajaran ini tersedia di `05-dotnet-agent-framework.cs`. 

Untuk menjalankan contohnya:

```bash
# Jadikan skrip dapat dijalankan (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Jalankan Aplikasi File Tunggal .NET
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
4. **Pembuatan Penyimpanan Vektor**: Membuat penyimpanan vektor untuk pencarian semantik
5. **Konfigurasi Agen**: Menyiapkan agen AI dengan kemampuan pencarian file
6. **Eksekusi Query**: Menjalankan query terhadap dokumen yang diunggah

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->