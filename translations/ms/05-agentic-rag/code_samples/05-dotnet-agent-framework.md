<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:06:40+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "ms"
}
-->
# 🔍 Enterprise RAG dengan Azure AI Foundry (.NET)

## 📋 Objektif Pembelajaran

Notebook ini menunjukkan cara membina sistem Retrieval-Augmented Generation (RAG) bertaraf perusahaan menggunakan Microsoft Agent Framework dalam .NET dengan Azure AI Foundry. Anda akan belajar untuk mencipta agen yang sedia untuk pengeluaran yang boleh mencari dokumen dan memberikan respons yang tepat serta berasaskan konteks dengan keselamatan dan skalabiliti perusahaan.

**Keupayaan Enterprise RAG yang Akan Anda Bina:**
- 📚 **Kecerdasan Dokumen**: Pemprosesan dokumen lanjutan dengan perkhidmatan Azure AI
- 🔍 **Carian Semantik**: Carian vektor berprestasi tinggi dengan ciri perusahaan
- 🛡️ **Integrasi Keselamatan**: Kawalan akses berasaskan peranan dan corak perlindungan data
- 🏢 **Arkitektur Skalabiliti**: Sistem RAG sedia pengeluaran dengan pemantauan

## 🎯 Arkitektur Enterprise RAG

### Komponen Teras Perusahaan
- **Azure AI Foundry**: Platform AI perusahaan yang diurus dengan keselamatan dan pematuhan
- **Agen Berterusan**: Agen berkeadaan dengan sejarah perbualan dan pengurusan konteks
- **Pengurusan Stor Vektor**: Pengindeksan dan pengambilan dokumen bertaraf perusahaan
- **Integrasi Identiti**: Pengesahan Azure AD dan kawalan akses berasaskan peranan

### Kelebihan .NET untuk Perusahaan
- **Keselamatan Jenis**: Pengesahan masa kompilasi untuk operasi RAG dan struktur data
- **Prestasi Asinkron**: Pemprosesan dokumen dan operasi carian tanpa sekatan
- **Pengurusan Memori**: Penggunaan sumber yang cekap untuk koleksi dokumen besar
- **Corak Integrasi**: Integrasi perkhidmatan Azure asli dengan suntikan kebergantungan

## 🏗️ Arkitektur Teknikal

### Saluran Enterprise RAG
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Komponen Teras .NET
- **Azure.AI.Agents.Persistent**: Pengurusan agen perusahaan dengan ketekalan keadaan
- **Azure.Identity**: Pengesahan bersepadu untuk akses perkhidmatan Azure yang selamat
- **Microsoft.Agents.AI.AzureAI**: Pelaksanaan rangka kerja agen yang dioptimumkan untuk Azure
- **System.Linq.Async**: Operasi LINQ asinkron berprestasi tinggi

## 🔧 Ciri & Kelebihan Perusahaan

### Keselamatan & Pematuhan
- **Integrasi Azure AD**: Pengurusan identiti dan pengesahan perusahaan
- **Akses Berasaskan Peranan**: Kebenaran terperinci untuk akses dokumen dan operasi
- **Perlindungan Data**: Penyulitan semasa rehat dan semasa transit untuk dokumen sensitif
- **Log Audit**: Penjejakan aktiviti yang komprehensif untuk keperluan pematuhan

### Prestasi & Skalabiliti
- **Pengumpulan Sambungan**: Pengurusan sambungan perkhidmatan Azure yang cekap
- **Pemprosesan Asinkron**: Operasi tanpa sekatan untuk senario throughput tinggi
- **Strategi Caching**: Caching pintar untuk dokumen yang sering diakses
- **Pengimbangan Beban**: Pemprosesan teragih untuk penyebaran berskala besar

### Pengurusan & Pemantauan
- **Pemeriksaan Kesihatan**: Pemantauan terbina dalam untuk komponen sistem RAG
- **Metrik Prestasi**: Analitik terperinci tentang kualiti carian dan masa respons
- **Pengendalian Ralat**: Pengurusan pengecualian yang komprehensif dengan polisi ulang
- **Pengurusan Konfigurasi**: Tetapan khusus persekitaran dengan pengesahan

## ⚙️ Prasyarat & Persediaan

**Persekitaran Pembangunan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan sambungan C#
- Langganan Azure dengan akses AI Foundry

**Pakej NuGet Diperlukan:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Persediaan Pengesahan Azure:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Konfigurasi Persekitaran:**
* Konfigurasi Azure AI Foundry (ditangani secara automatik melalui Azure CLI)
* Pastikan anda telah disahkan ke langganan Azure yang betul

## 📊 Corak Enterprise RAG

### Corak Pengurusan Dokumen
- **Muat Naik Pukal**: Pemprosesan cekap koleksi dokumen besar
- **Kemas Kini Beransur**: Penambahan dan pengubahsuaian dokumen secara masa nyata
- **Kawalan Versi**: Penjejakan versi dokumen dan perubahan
- **Pengurusan Metadata**: Atribut dokumen yang kaya dan taksonomi

### Corak Carian & Pengambilan
- **Carian Hibrid**: Menggabungkan carian semantik dan kata kunci untuk hasil optimum
- **Carian Berasaskan Fasa**: Penapisan dan pengkategorian pelbagai dimensi
- **Penalaan Relevansi**: Algoritma pemarkahan tersuai untuk keperluan khusus domain
- **Peringkat Hasil**: Pemeringkatan lanjutan dengan integrasi logik perniagaan

### Corak Keselamatan
- **Keselamatan Tahap Dokumen**: Kawalan akses terperinci bagi setiap dokumen
- **Pengelasan Data**: Pelabelan sensitiviti automatik dan perlindungan
- **Jejak Audit**: Log komprehensif semua operasi RAG
- **Perlindungan Privasi**: Pengesanan dan penyuntingan PII

## 🔒 Ciri Keselamatan Perusahaan

### Pengesahan & Kebenaran
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
- **Penyulitan**: Penyulitan hujung ke hujung untuk dokumen dan indeks carian
- **Kawalan Akses**: Integrasi dengan Azure AD untuk kebenaran pengguna dan kumpulan
- **Kediaman Data**: Kawalan lokasi data geografi untuk pematuhan
- **Sandaran & Pemulihan**: Keupayaan sandaran dan pemulihan bencana automatik

## 📈 Pengoptimuman Prestasi

### Corak Pemprosesan Asinkron
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Pengurusan Memori
- **Pemprosesan Penstriman**: Mengendalikan dokumen besar tanpa masalah memori
- **Pengumpulan Sumber**: Penggunaan semula sumber yang mahal dengan cekap
- **Pengumpulan Sampah**: Corak peruntukan memori yang dioptimumkan
- **Pengurusan Sambungan**: Kitaran hayat sambungan perkhidmatan Azure yang betul

### Strategi Caching
- **Caching Pertanyaan**: Cache carian yang sering dijalankan
- **Caching Dokumen**: Caching dalam memori untuk dokumen panas
- **Caching Indeks**: Caching indeks vektor yang dioptimumkan
- **Caching Hasil**: Caching pintar respons yang dijana

## 📊 Kes Penggunaan Perusahaan

### Pengurusan Pengetahuan
- **Wiki Korporat**: Carian pintar merentasi pangkalan pengetahuan syarikat
- **Dasar & Prosedur**: Panduan pematuhan dan prosedur automatik
- **Bahan Latihan**: Bantuan pembelajaran dan pembangunan pintar
- **Pangkalan Data Penyelidikan**: Sistem analisis kertas akademik dan penyelidikan

### Sokongan Pelanggan
- **Pangkalan Pengetahuan Sokongan**: Respons perkhidmatan pelanggan automatik
- **Dokumentasi Produk**: Pengambilan maklumat produk pintar
- **Panduan Penyelesaian Masalah**: Bantuan penyelesaian masalah berasaskan konteks
- **Sistem FAQ**: Penjanaan FAQ dinamik daripada koleksi dokumen

### Pematuhan Peraturan
- **Analisis Dokumen Undang-Undang**: Kecerdasan kontrak dan dokumen undang-undang
- **Pemantauan Pematuhan**: Pemeriksaan pematuhan peraturan automatik
- **Penilaian Risiko**: Analisis dan pelaporan risiko berasaskan dokumen
- **Sokongan Audit**: Penemuan dokumen pintar untuk audit

## 🚀 Penyebaran Pengeluaran

### Pemantauan & Kebolehlihatan
- **Application Insights**: Telemetri terperinci dan pemantauan prestasi
- **Metrik Tersuai**: Penjejakan KPI khusus perniagaan dan amaran
- **Penjejakan Teragih**: Penjejakan permintaan hujung ke hujung merentasi perkhidmatan
- **Papan Pemuka Kesihatan**: Visualisasi kesihatan dan prestasi sistem masa nyata

### Skalabiliti & Kebolehpercayaan
- **Auto-Skala**: Penskalaan automatik berdasarkan beban dan metrik prestasi
- **Ketersediaan Tinggi**: Penyebaran pelbagai wilayah dengan keupayaan failover
- **Ujian Beban**: Pengesahan prestasi di bawah keadaan beban perusahaan
- **Pemulihan Bencana**: Prosedur sandaran dan pemulihan automatik

Sedia untuk membina sistem RAG bertaraf perusahaan yang boleh mengendalikan dokumen sensitif pada skala besar? Mari kita arkitekkan sistem pengetahuan pintar untuk perusahaan! 🏢📖✨

## Pelaksanaan Kod

Contoh kod lengkap untuk pelajaran ini tersedia dalam `05-dotnet-agent-framework.cs`. 

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

Kod ini menunjukkan:

1. **Pemasangan Pakej**: Memasang pakej NuGet yang diperlukan untuk Azure AI Agents
2. **Konfigurasi Persekitaran**: Memuatkan tetapan titik akhir dan model Azure AI Foundry
3. **Muat Naik Dokumen**: Memuat naik dokumen untuk pemprosesan RAG
4. **Penciptaan Stor Vektor**: Mencipta stor vektor untuk carian semantik
5. **Konfigurasi Agen**: Menyediakan agen AI dengan keupayaan carian fail
6. **Pelaksanaan Pertanyaan**: Menjalankan pertanyaan terhadap dokumen yang dimuat naik

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.