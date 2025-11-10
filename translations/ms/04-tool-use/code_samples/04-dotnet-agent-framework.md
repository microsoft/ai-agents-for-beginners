<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:26:51+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "ms"
}
-->
# 🛠️ Penggunaan Alat Lanjutan dengan Model GitHub (.NET)

## 📋 Objektif Pembelajaran

Notebook ini menunjukkan corak integrasi alat peringkat perusahaan menggunakan Microsoft Agent Framework dalam .NET dengan Model GitHub. Anda akan belajar membina agen canggih dengan pelbagai alat khusus, memanfaatkan pengetikan kuat C# dan ciri perusahaan .NET.

**Keupayaan Alat Lanjutan yang Akan Anda Kuasai:**
- 🔧 **Arkitektur Multi-Alat**: Membina agen dengan pelbagai keupayaan khusus
- 🎯 **Pelaksanaan Alat Selamat Jenis**: Memanfaatkan pengesahan masa kompilasi C#
- 📊 **Corak Alat Perusahaan**: Reka bentuk alat yang sedia untuk pengeluaran dan pengendalian ralat
- 🔗 **Komposisi Alat**: Menggabungkan alat untuk aliran kerja perniagaan yang kompleks

## 🎯 Kelebihan Arkitektur Alat .NET

### Ciri Alat Perusahaan
- **Pengesahan Masa Kompilasi**: Pengetikan kuat memastikan ketepatan parameter alat
- **Suntikan Kebergantungan**: Integrasi bekas IoC untuk pengurusan alat
- **Corak Async/Await**: Pelaksanaan alat tanpa blok dengan pengurusan sumber yang betul
- **Log Berstruktur**: Integrasi log terbina dalam untuk pemantauan pelaksanaan alat

### Corak Sedia Pengeluaran
- **Pengendalian Pengecualian**: Pengurusan ralat yang komprehensif dengan pengecualian yang ditaip
- **Pengurusan Sumber**: Corak pelupusan yang betul dan pengurusan memori
- **Pemantauan Prestasi**: Metrik terbina dalam dan kaunter prestasi
- **Pengurusan Konfigurasi**: Konfigurasi selamat jenis dengan pengesahan

## 🔧 Arkitektur Teknikal

### Komponen Alat Teras .NET
- **Microsoft.Extensions.AI**: Lapisan abstraksi alat yang bersatu
- **Microsoft.Agents.AI**: Orkestrasi alat peringkat perusahaan
- **Integrasi Model GitHub**: Klien API berprestasi tinggi dengan pengumpulan sambungan

### Saluran Pelaksanaan Alat
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Kategori & Corak Alat

### 1. **Alat Pemprosesan Data**
- **Pengesahan Input**: Pengetikan kuat dengan anotasi data
- **Operasi Transformasi**: Penukaran dan pemformatan data yang selamat jenis
- **Logik Perniagaan**: Alat pengiraan dan analisis khusus domain
- **Pemformatan Output**: Penjanaan respons berstruktur

### 2. **Alat Integrasi**
- **Penyambung API**: Integrasi perkhidmatan RESTful dengan HttpClient
- **Alat Pangkalan Data**: Integrasi Entity Framework untuk akses data
- **Operasi Fail**: Operasi sistem fail yang selamat dengan pengesahan
- **Perkhidmatan Luaran**: Corak integrasi perkhidmatan pihak ketiga

### 3. **Alat Utiliti**
- **Pemprosesan Teks**: Manipulasi dan pemformatan string
- **Operasi Tarikh/Masa**: Pengiraan tarikh/masa yang peka budaya
- **Alat Matematik**: Pengiraan ketepatan dan operasi statistik
- **Alat Pengesahan**: Pengesahan peraturan perniagaan dan verifikasi data

## ⚙️ Prasyarat & Persediaan

**Persekitaran Pembangunan:**
- SDK .NET 9.0 atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan sambungan C#
- Akses API Model GitHub

**Pakej NuGet Diperlukan:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurasi Persekitaran (fail .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Bersedia untuk membina agen peringkat perusahaan dengan keupayaan alat yang kuat dan selamat jenis dalam .NET? Mari kita arkitekkan beberapa penyelesaian peringkat profesional! 🏢⚡

## 💻 Pelaksanaan Kod

Pelaksanaan lengkap C# tersedia dalam fail pendamping `04-dotnet-agent-framework.cs`. Aplikasi Fail Tunggal .NET ini menunjukkan:

- Memuatkan pembolehubah persekitaran untuk konfigurasi Model GitHub
- Mendefinisikan alat khusus menggunakan kaedah C# dengan atribut
- Mencipta agen AI dengan integrasi alat
- Menguruskan benang perbualan
- Melaksanakan permintaan agen dengan pemanggilan alat

Untuk menjalankan contoh:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Atau menggunakan CLI .NET:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.