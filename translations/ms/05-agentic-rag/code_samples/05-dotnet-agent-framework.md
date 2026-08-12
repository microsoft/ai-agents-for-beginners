# 🔍 RAG Perusahaan dengan Microsoft Foundry (.NET)

## 📋 Objektif Pembelajaran

Buku nota ini menunjukkan cara membina sistem Retrieval-Augmented Generation (RAG) kelas perusahaan menggunakan Microsoft Agent Framework dalam .NET dengan Microsoft Foundry. Anda akan belajar mencipta ejen yang bersedia untuk pengeluaran yang boleh mencari melalui dokumen dan memberikan jawapan yang tepat, sedar konteks dengan keselamatan dan kemampuan skala perusahaan.

**Keupayaan RAG Perusahaan yang Akan Anda Bina:**
- 📚 **Kepintaran Dokumen**: Pemprosesan dokumen lanjutan dengan perkhidmatan AI Azure
- 🔍 **Carian Semantik**: Carian vektor berprestasi tinggi dengan ciri perusahaan
- 🛡️ **Integrasi Keselamatan**: Kawalan akses berasaskan peranan dan corak perlindungan data
- 🏢 **Senibina Boleh Diskala**: Sistem RAG bersedia pengeluaran dengan pemantauan

## 🎯 Senibina RAG Perusahaan

### Komponen Teras Perusahaan
- **Microsoft Foundry**: Platform AI perusahaan yang diurus dengan keselamatan dan pematuhan
- **Ejen Persisten**: Ejen berkeadaan dengan sejarah perbualan dan pengurusan konteks
- **Pengurusan Stor Vektor**: Pengindeksan dan pengambilan dokumen kelas perusahaan
- **Integrasi Identiti**: Pengesahan Azure AD dan kawalan akses berasaskan peranan

### Manfaat .NET Perusahaan
- **Keselamatan Jenis**: Pengesahan masa kompilasi untuk operasi dan struktur data RAG
- **Prestasi Async**: Pemprosesan dokumen dan operasi carian tidak menyekat
- **Pengurusan Memori**: Penggunaan sumber yang cekap untuk koleksi dokumen besar
- **Corak Integrasi**: Integrasi perkhidmatan Azure asli dengan suntikan bergantung

## 🏗️ Senibina Teknikal

### Saluran RAG Perusahaan
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Komponen Teras .NET
- **Azure.AI.Agents.Persistent**: Pengurusan ejen perusahaan dengan pengekalan keadaan
- **Azure.Identity**: Pengesahan terintegrasi untuk akses perkhidmatan Azure yang selamat
- **Microsoft.Agents.AI.AzureAI**: Pelaksanaan rangka kerja ejen yang dioptimumkan untuk Azure
- **System.Linq.Async**: Operasi LINQ tidak serentak berprestasi tinggi

## 🔧 Ciri & Manfaat Perusahaan

### Keselamatan & Pematuhan
- **Integrasi Azure AD**: Pengurusan identiti dan pengesahan perusahaan
- **Akses Berasaskan Peranan**: Kebenaran terperinci untuk akses dokumen dan operasi
- **Perlindungan Data**: Penyulitan semasa rehat dan dalam transit untuk dokumen sensitif
- **Log Audit**: Penjejakan aktiviti menyeluruh untuk keperluan pematuhan

### Prestasi & Kebolehan Skala
- **Pengumpulan Sambungan**: Pengurusan sambungan perkhidmatan Azure yang cekap
- **Pemprosesan Async**: Operasi tidak menyekat untuk senario berkeluaran tinggi
- **Strategi Caching**: Caching pintar untuk dokumen yang kerap diakses
- **Pengimbangan Beban**: Pemprosesan diedarkan untuk penempatan skala besar

### Pengurusan & Pemantauan
- **Pemeriksaan Kesihatan**: Pemantauan terbina dalam untuk komponen sistem RAG
- **Metik Prestasi**: Analitik terperinci mengenai kualiti carian dan masa tindak balas
- **Pengendalian Ralat**: Pengurusan pengecualian menyeluruh dengan polisi cuba semula
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
* Pastikan anda diautentikasi ke langganan Azure yang betul

## 📊 Corak RAG Perusahaan

### Corak Pengurusan Dokumen
- **Muat Naik Pukal**: Pemprosesan cekap koleksi dokumen besar
- **Kemas Kini Inkremental**: Penambahan dan pengubahsuaian dokumen masa nyata
- **Kawalan Versi**: Versi dokumen dan penjejakan perubahan
- **Pengurusan Metadata**: Atribut dokumen yang kaya dan taksonomi

### Corak Carian & Pengambilan
- **Carian Hibrid**: Menggabungkan carian semantik dan kata kunci untuk hasil optimum
- **Carian Berfasa**: Penapisan dan pengkategorian pelbagai dimensi
- **Penalaan Kepentingan**: Algoritma penandaan tersuai untuk keperluan khusus domain
- **Kedudukan Keputusan**: Peringkat lanjutan dengan integrasi logik perniagaan

### Corak Keselamatan
- **Keselamatan Tahap Dokumen**: Kawalan akses terperinci per dokumen
- **Pengelasan Data**: Pelabelan sensitiviti automatik dan perlindungan
- **Jejak Audit**: Log menyeluruh semua operasi RAG
- **Perlindungan Privasi**: Kebolehan pengesanan dan penghapusan PII

## 🔒 Ciri Keselamatan Perusahaan

### Pengesahan & Pengekalan Kebenaran
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
- **Penyulitan**: Penyulitan menyeluruh untuk dokumen dan indeks carian
- **Kawalan Akses**: Integrasi dengan Azure AD untuk kebenaran pengguna dan kumpulan
- **Lokasi Data**: Kawalan lokasi data geografi untuk pematuhan
- **Sandaran & Pemulihan**: Kebolehan sandaran automatik dan pemulihan bencana

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
- **Pemprosesan Penstriman**: Mengendalikan dokumen besar tanpa isu memori
- **Pengumpulan Sumber**: Penggunaan semula sumber yang mahal dengan cekap
- **Pengumpulan Sampah**: Corak pengagihan memori yang dioptimumkan
- **Pengurusan Sambungan**: Kitar hayat sambungan perkhidmatan Azure yang betul

### Strategi Caching
- **Caching Pertanyaan**: Cache carian yang kerap dilaksanakan
- **Caching Dokumen**: Caching dalam memori untuk dokumen popular
- **Caching Indeks**: Caching indeks vektor yang dioptimumkan
- **Caching Keputusan**: Caching pintar bagi jawapan yang dijana

## 📊 Kes Penggunaan Perusahaan

### Pengurusan Pengetahuan
- **Wiki Korporat**: Carian pintar merentas pangkalan pengetahuan syarikat
- **Polisi & Prosedur**: Pematuhan automatik dan panduan prosedur
- **Bahan Latihan**: Bantuan pembelajaran dan pembangunan yang pintar
- **Pangkalan Data Penyelidikan**: Sistem analisis kertas akademik dan penyelidikan

### Sokongan Pelanggan
- **Pangkalan Pengetahuan Sokongan**: Jawapan perkhidmatan pelanggan automatik
- **Dokumentasi Produk**: Pengambilan maklumat produk yang pintar
- **Panduan Penyelesaian Masalah**: Bantuan penyelesaian masalah kontekstual
- **Sistem FAQ**: Penjanaan FAQ dinamik daripada koleksi dokumen

### Pematuhan Peraturan
- **Analisis Dokumen Undang-Undang**: Kepintaran kontrak dan dokumen undang-undang
- **Pemantauan Pematuhan**: Pemeriksaan pematuhan peraturan automatik
- **Penilaian Risiko**: Analisis dan pelaporan risiko berasaskan dokumen
- **Sokongan Audit**: Penemuan dokumen pintar untuk audit

## 🚀 Pengeluaran Penempatan

### Pemantauan & Kebolehlihatan
- **Application Insights**: Telemetri terperinci dan pemantauan prestasi
- **Metik Tersuai**: Penjejakan KPI dan penggera khusus perniagaan
- **Penjejakan Beredar**: Penjejakan permintaan menyeluruh merentas perkhidmatan
- **Papan Pemuka Kesihatan**: Visualisasi kesihatan dan prestasi sistem masa nyata

### Kebolehan Skala & Kebolehpercayaan
- **Auto-Skala**: Penskalaan automatik berdasarkan beban dan metrik prestasi
- **Ketersediaan Tinggi**: Penempatan berbilang rantau dengan kebolehan failover
- **Ujian Beban**: Pengesahan prestasi di bawah keadaan beban perusahaan
- **Pemulihan Bencana**: Prosedur sandaran dan pemulihan automatik

Bersedia untuk membina sistem RAG kelas perusahaan yang boleh mengendalikan dokumen sensitif pada skala? Mari kita senibina sistem pengetahuan pintar untuk perusahaan! 🏢📖✨

## Pelaksanaan Kod

Contoh kod lengkap untuk pelajaran ini tersedia dalam `05-dotnet-agent-framework.cs`. 

Untuk menjalankan contoh:

```bash
# Jadikan skrip boleh dilaksanakan (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Jalankan Aplikasi Fail Tunggal .NET
./05-dotnet-agent-framework.cs
```

Atau gunakan `dotnet run` secara langsung:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kod ini menunjukkan:

1. **Pemasangan Pakej**: Memasang pakej NuGet yang diperlukan untuk Azure AI Agents
2. **Konfigurasi Persekitaran**: Memuatkan titik akhir dan tetapan model Microsoft Foundry
3. **Muat Naik Dokumen**: Memuat naik dokumen untuk pemprosesan RAG
4. **Penciptaan Stor Vektor**: Mencipta stor vektor untuk carian semantik
5. **Konfigurasi Ejen**: Menyediakan ejen AI dengan keupayaan carian fail
6. **Pelaksanaan Pertanyaan**: Menjalankan pertanyaan ke atas dokumen yang dimuat naik

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->