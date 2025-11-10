<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:58:32+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "id"
}
-->
# 🎯 Perencanaan & Pola Desain dengan Model GitHub (.NET)

## 📋 Tujuan Pembelajaran

Notebook ini menunjukkan pola perencanaan dan desain tingkat perusahaan untuk membangun agen cerdas menggunakan Microsoft Agent Framework di .NET dengan Model GitHub. Anda akan belajar membuat agen yang dapat memecah masalah kompleks, merencanakan solusi multi-langkah, dan menjalankan alur kerja canggih dengan fitur-fitur enterprise dari .NET.

## ⚙️ Prasyarat & Pengaturan

**Lingkungan Pengembangan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan ekstensi C#
- Akses API Model GitHub

**Dependensi yang Dibutuhkan:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurasi Lingkungan (file .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Menjalankan Kode

Pelajaran ini mencakup implementasi Aplikasi File Tunggal .NET. Untuk menjalankannya:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Atau gunakan perintah dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementasi Kode

Implementasi lengkap tersedia di `07-dotnet-agent-framework.cs`, yang menunjukkan:

- Memuat konfigurasi lingkungan dengan DotNetEnv
- Mengonfigurasi klien OpenAI untuk Model GitHub
- Mendefinisikan model data terstruktur (Plan dan TravelPlan) dengan serialisasi JSON
- Membuat agen AI dengan output terstruktur menggunakan skema JSON
- Menjalankan permintaan perencanaan dengan respons yang aman tipe

## Konsep Utama

### Perencanaan Terstruktur dengan Model Aman Tipe

Agen menggunakan kelas C# untuk mendefinisikan struktur output perencanaan:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### Skema JSON untuk Output Terstruktur

Agen dikonfigurasi untuk mengembalikan respons yang sesuai dengan skema TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Instruksi Agen Perencanaan

Agen bertindak sebagai koordinator, mendelegasikan tugas kepada sub-agen khusus:

- FlightBooking: Untuk memesan penerbangan dan memberikan informasi penerbangan
- HotelBooking: Untuk memesan hotel dan memberikan informasi hotel
- CarRental: Untuk memesan mobil dan memberikan informasi penyewaan mobil
- ActivitiesBooking: Untuk memesan aktivitas dan memberikan informasi aktivitas
- DestinationInfo: Untuk memberikan informasi tentang destinasi
- DefaultAgent: Untuk menangani permintaan umum

## Output yang Diharapkan

Ketika Anda menjalankan agen dengan permintaan perencanaan perjalanan, agen akan menganalisis permintaan tersebut dan menghasilkan rencana terstruktur dengan penugasan tugas yang sesuai kepada agen khusus, diformat sebagai JSON yang sesuai dengan skema TravelPlan.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.