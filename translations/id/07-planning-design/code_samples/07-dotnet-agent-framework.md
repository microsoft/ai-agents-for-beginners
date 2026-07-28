# 🎯 Pola Perencanaan & Desain dengan Azure OpenAI (Responses API) (.NET)

## 📋 Tujuan Pembelajaran

Buku catatan ini mendemonstrasikan pola perencanaan dan desain tingkat perusahaan untuk membangun agen cerdas menggunakan Microsoft Agent Framework dalam .NET dengan Azure OpenAI (Responses API). Anda akan belajar membuat agen yang dapat memecah masalah kompleks, merencanakan solusi multi-langkah, dan menjalankan alur kerja canggih dengan fitur perusahaan .NET.

## ⚙️ Prasyarat & Pengaturan

**Lingkungan Pengembangan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan ekstensi C#
- Langganan Azure dengan sumber daya Azure OpenAI dan penempatan model
- Azure CLI — masuk dengan `az login`

**Dependensi yang Diperlukan:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurasi Lingkungan (file .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Menjalankan Kode

Pelajaran ini mencakup implementasi .NET Single File App. Untuk menjalankannya:

```bash
# Buat file dapat dijalankan (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Jalankan aplikasi
./07-dotnet-agent-framework.cs
```

Atau gunakan perintah dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementasi Kode

Implementasi lengkap tersedia di `07-dotnet-agent-framework.cs`, yang mendemonstrasikan:

- Memuat konfigurasi lingkungan dengan DotNetEnv
- Mengonfigurasi klien Azure OpenAI dan membuat agen AI menggunakan `GetChatClient().AsAIAgent()`
- Mendefinisikan model data terstruktur (Plan dan TravelPlan) dengan serialisasi JSON
- Membuat agen AI dengan keluaran terstruktur menggunakan skema JSON
- Menjalankan permintaan perencanaan dengan respons tipe-aman

## Konsep Kunci

### Perencanaan Terstruktur dengan Model Tipe-Aman

Agen menggunakan kelas C# untuk mendefinisikan struktur keluaran perencanaan:

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

### Skema JSON untuk Keluaran Terstruktur

Agen dikonfigurasi untuk mengembalikan respons yang sesuai dengan skema TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
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

Agen bertindak sebagai koordinator, mendelegasikan tugas ke sub-agen khusus:

- FlightBooking: Untuk memesan penerbangan dan memberikan informasi penerbangan
- HotelBooking: Untuk memesan hotel dan memberikan informasi hotel
- CarRental: Untuk memesan mobil dan memberikan informasi penyewaan mobil
- ActivitiesBooking: Untuk memesan aktivitas dan memberikan informasi aktivitas
- DestinationInfo: Untuk memberikan informasi tentang destinasi
- DefaultAgent: Untuk menangani permintaan umum

## Keluaran yang Diharapkan

Saat Anda menjalankan agen dengan permintaan perencanaan perjalanan, ia akan menganalisis permintaan dan menghasilkan rencana terstruktur dengan penugasan tugas yang sesuai ke agen khusus, diformat sebagai JSON yang sesuai dengan skema TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->