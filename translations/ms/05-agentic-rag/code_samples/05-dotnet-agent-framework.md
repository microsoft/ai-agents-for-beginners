# 🔍 RAG Perusahaan dengan Microsoft Foundry (.NET)

## 📋 Objektif Pembelajaran

Nota ini menunjukkan cara membina sistem Retrieval-Augmented Generation (RAG) gred perusahaan menggunakan Microsoft Agent Framework dalam .NET dengan Microsoft Foundry. Anda akan belajar mencipta ejen siap produksi yang boleh mencari melalui dokumen dan menyediakan respons yang tepat, peka konteks dengan keselamatan dan skala perusahaan.

**Keupayaan RAG Perusahaan yang Akan Anda Bina:**
- 📚 **Kepintaran Dokumen**: Pemprosesan dokumen lanjutan dengan perkhidmatan Azure AI
- 🔍 **Carian Semantik**: Carian vektor berprestasi tinggi dengan ciri perusahaan
- 🛡️ **Integrasi Keselamatan**: Akses berasaskan peranan dan corak perlindungan data
- 🏢 **Seni Bina Boleh Skala**: Sistem RAG siap produksi dengan pemantauan

## 🎯 Seni Bina RAG Perusahaan

### Komponen Teras Perusahaan
- **Microsoft Foundry**: Platform AI perusahaan yang diurus dengan keselamatan dan pematuhan
- **Ejen Persisten**: Ejen berkeadaan dengan sejarah perbualan dan pengurusan konteks
- **Pengurusan Stor Vektor**: Pengindeksan dan pengambilan dokumen gred perusahaan
- **Integrasi Identiti**: Pengesahan Azure AD dan kawalan akses berasaskan peranan

### Manfaat .NET Perusahaan
- **Keselamatan Jenis**: Pengesahan waktu kompilasi untuk operasi RAG dan struktur data
- **Prestasi Async**: Pemprosesan dan operasi carian dokumen tanpa sekatan
- **Pengurusan Memori**: Penggunaan sumber cekap untuk koleksi dokumen besar
- **Corak Integrasi**: Integrasi perkhidmatan Azure asli dengan suntikan kebergantungan

## 🏗️ Seni Bina Teknikal

### Saluran RAG Perusahaan
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Komponen Teras .NET
- **Azure.AI.Agents.Persistent**: Pengurusan ejen perusahaan dengan ketekalan keadaan
- **Azure.Identity**: Pengesahan terintegrasi untuk akses perkhidmatan Azure yang selamat
- **Microsoft.Agents.AI.AzureAI**: Pelaksanaan rangka kerja ejen dioptimumkan untuk Azure
- **System.Linq.Async**: Operasi LINQ tak segerak berprestasi tinggi

## 🔧 Ciri & Manfaat Perusahaan

### Keselamatan & Pematuhan
- **Integrasi Azure AD**: Pengurusan identiti dan pengesahan perusahaan
- **Akses Berasaskan Peranan**: Kebenaran terperinci untuk akses dan operasi dokumen
- **Perlindungan Data**: Penyulitan semasa rehat dan dalam transit untuk dokumen sensitif
- **Audit Logging**: Penjejak aktiviti menyeluruh untuk keperluan pematuhan

### Prestasi & Skala
- **Pengumpulan Sambungan**: Pengurusan sambungan perkhidmatan Azure yang cekap
- **Pemprosesan Async**: Operasi tanpa sekatan untuk senario pelalu tinggi
- **Strategi Caching**: Caching pintar untuk dokumen yang sering diakses
- **Pengimbangan Beban**: Pemprosesan teragih untuk pengerahan berskala besar

### Pengurusan & Pemantauan
- **Pemeriksaan Kesihatan**: Pemantauan terbina dalam untuk komponen sistem RAG
- **Metrix Prestasi**: Analitik terperinci mengenai kualiti carian dan masa respons
- **Pengendalian Ralat**: Pengurusan pengecualian menyeluruh dengan polisi ulang cuba
- **Pengurusan Konfigurasi**: Tetapan khusus persekitaran dengan pengesahan

## ⚙️ Prasyarat & Persediaan

**Persekitaran Pembangunan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan sambungan C#
- Langganan Azure dengan akses Microsoft Foundry

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
# Pasang Azure CLI dan sahkan diri
az login
az account set --subscription "your-subscription-id"
```

**Konfigurasi Persekitaran:**
* Konfigurasi Microsoft Foundry (ditangani secara automatik melalui Azure CLI)
* Pastikan anda telah diautentikasi ke langganan Azure yang betul

## 📊 Corak RAG Perusahaan

### Corak Pengurusan Dokumen
- **Muat Naik Pukal**: Pemprosesan cekap koleksi dokumen besar
- **Kemas Kini Inkremental**: Penambahan dan pengubahsuaian dokumen masa nyata
- **Kawalan Versi**: Pemberian versi dokumen dan penjejakan perubahan
- **Pengurusan Metadata**: Atribut dokumen kaya dan taksonomi

### Corak Carian & Pengambilan
- **Carian Hibrid**: Menggabungkan carian semantik dan kata kunci untuk hasil optimum
- **Carian Berfasa**: Penapisan dan pengkategorian berbilang dimensi
- **Penalaan Relevan**: Algoritma skor khusus untuk keperluan domain
- **Peringkat Keputusan**: Peringkat lanjutan dengan integrasi logik perniagaan

### Corak Keselamatan
- **Keselamatan Per-Dokumen**: Kawalan akses terperinci per dokumen
- **Pengelasan Data**: Pelabelan sensitiviti dan perlindungan automatik
- **Jejak Audit**: Log menyeluruh semua operasi RAG
- **Perlindungan Privasi**: Keupayaan pengesanan dan pengaburan PII

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
- **Penyulitan**: Penyulitan ujung ke ujung untuk dokumen dan indeks carian
- **Kawalan Akses**: Integrasi dengan Azure AD untuk kebenaran pengguna dan kumpulan
- **Kediaman Data**: Kawalan lokasi data geografi untuk pematuhan
- **Sandaran & Pemulihan**: Keupayaan sandaran automatik dan pemulihan bencana

## 📈 Pengoptimuman Prestasi

### Corak Pemprosesan Async
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Pengurusan Memori
- **Pemprosesan Penstriman**: Menangani dokumen besar tanpa isu memori
- **Pengumpulan Sumber**: Penggunaan semula sumber mahal yang cekap
- **Pengumpulan Sampah**: Corak pengalokasian memori yang dioptimumkan
- **Pengurusan Sambungan**: Kitar hayat sambungan perkhidmatan Azure yang betul

### Strategi Caching
- **Caching Pertanyaan**: Cache carian yang sering dijalankan
- **Caching Dokumen**: Caching dalam memori untuk dokumen panas
- **Caching Indeks**: Caching indeks vektor yang dioptimumkan
- **Caching Keputusan**: Caching pintar respons yang dijana

## 📊 Kes Penggunaan Perusahaan

### Pengurusan Pengetahuan
- **Wiki Korporat**: Carian pintar merentas pangkalan pengetahuan syarikat
- **Polisi & Prosedur**: Pematuhan automatik dan panduan prosedur
- **Bahan Latihan**: Bantuan pembelajaran dan pembangunan pintar
- **Pangkalan Data Penyelidikan**: Sistem penganalisaan kertas akademik dan penyelidikan

### Sokongan Pelanggan
- **Pangkalan Pengetahuan Sokongan**: Respons automatik perkhidmatan pelanggan
- **Dokumentasi Produk**: Pengambilan maklumat produk pintar
- **Panduan Penyelesaian Masalah**: Bantuan penyelesaian masalah kontekstual
- **Sistem FAQ**: Penjanaan FAQ dinamik dari koleksi dokumen

### Pematuhan Peraturan
- **Analisis Dokumen Perundangan**: Kepintaran kontrak dan dokumen perundangan
- **Pemantauan Pematuhan**: Pemeriksaan pematuhan peraturan automatik
- **Penilaian Risiko**: Analisis risiko berasaskan dokumen dan pelaporan
- **Sokongan Audit**: Penemuan dokumen pintar untuk audit

## 🚀 Penghantaran Produksi

### Pemantauan & Kebolehlihatan
- **Application Insights**: Telemetri dan pemantauan prestasi terperinci
- **Metrix Tersuai**: Penjejakan dan amaran KPI khusus perniagaan
- **Penjejakan Teragih**: Penjejakan permintaan hujung-ke-hujung merentas perkhidmatan
- **Papan Pemuka Kesihatan**: Visualisasi masa nyata kesihatan dan prestasi sistem

### Skalabiliti & Kebolehpercayaan
- **Auto-Skala**: Skala automatik berdasarkan beban dan metrik prestasi
- **Ketersediaan Tinggi**: Penghantaran pelbagai rantau dengan keupayaan failover
- **Ujian Beban**: Pengesahan prestasi di bawah keadaan beban perusahaan
- **Pemulihan Bencana**: Prosedur sandaran dan pemulihan automatik

Bersedia untuk membina sistem RAG gred perusahaan yang boleh mengendalikan dokumen sensitif pada skala? Mari kita bina sistem pengetahuan pintar untuk perusahaan! 🏢📖✨

## Pelaksanaan Kod

Sampel kod lengkap untuk pelajaran ini tersedia dalam `05-dotnet-agent-framework.cs`. 

Untuk menjalankan contoh:

```bash
# Jadikan skrip boleh dilaksanakan (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Jalankan Aplikasi Fail Tunggal .NET
./05-dotnet-agent-framework.cs
```

Atau gunakan `dotnet run` terus:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kod ini menunjukkan:

1. **Pemasangan Pakej**: Memasang pakej NuGet yang diperlukan untuk Azure AI Agents
2. **Konfigurasi Persekitaran**: Memuatkan titik akhir dan tetapan model Microsoft Foundry
3. **Muat Naik Dokumen**: Memuat naik dokumen untuk pemprosesan RAG
4. **Penciptaan Stor Vektor**: Mencipta stor vektor untuk carian semantik
5. **Konfigurasi Ejen**: Menyediakan ejen AI dengan keupayaan carian fail
6. **Pelaksanaan Pertanyaan**: Menjalankan pertanyaan terhadap dokumen yang dimuat naik

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->