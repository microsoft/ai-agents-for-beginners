<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:58:38+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "ms"
}
-->
# 🎯 Perancangan & Corak Reka Bentuk dengan Model GitHub (.NET)

## 📋 Objektif Pembelajaran

Notebook ini menunjukkan perancangan dan corak reka bentuk bertaraf perusahaan untuk membina agen pintar menggunakan Microsoft Agent Framework dalam .NET dengan Model GitHub. Anda akan belajar untuk mencipta agen yang boleh menguraikan masalah kompleks, merancang penyelesaian berbilang langkah, dan melaksanakan aliran kerja canggih dengan ciri perusahaan .NET.

## ⚙️ Prasyarat & Persediaan

**Persekitaran Pembangunan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan sambungan C#
- Akses API Model GitHub

**Kebergantungan Diperlukan:**
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

## Menjalankan Kod

Pelajaran ini termasuk pelaksanaan Aplikasi Fail Tunggal .NET. Untuk menjalankannya:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Atau gunakan arahan dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Pelaksanaan Kod

Pelaksanaan lengkap tersedia dalam `07-dotnet-agent-framework.cs`, yang menunjukkan:

- Memuatkan konfigurasi persekitaran dengan DotNetEnv
- Mengkonfigurasi klien OpenAI untuk Model GitHub
- Mendefinisikan model data berstruktur (Plan dan TravelPlan) dengan serialisasi JSON
- Mencipta agen AI dengan output berstruktur menggunakan skema JSON
- Melaksanakan permintaan perancangan dengan respons jenis selamat

## Konsep Utama

### Perancangan Berstruktur dengan Model Jenis Selamat

Agen menggunakan kelas C# untuk mendefinisikan struktur output perancangan:

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

### Skema JSON untuk Output Berstruktur

Agen dikonfigurasi untuk mengembalikan respons yang sepadan dengan skema TravelPlan:

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

### Arahan Agen Perancangan

Agen bertindak sebagai penyelaras, menyerahkan tugas kepada sub-agen khusus:

- FlightBooking: Untuk menempah penerbangan dan menyediakan maklumat penerbangan
- HotelBooking: Untuk menempah hotel dan menyediakan maklumat hotel
- CarRental: Untuk menempah kereta dan menyediakan maklumat sewa kereta
- ActivitiesBooking: Untuk menempah aktiviti dan menyediakan maklumat aktiviti
- DestinationInfo: Untuk menyediakan maklumat tentang destinasi
- DefaultAgent: Untuk mengendalikan permintaan umum

## Output Dijangka

Apabila anda menjalankan agen dengan permintaan perancangan perjalanan, ia akan menganalisis permintaan tersebut dan menghasilkan rancangan berstruktur dengan tugasan tugas yang sesuai kepada agen khusus, diformatkan sebagai JSON yang mematuhi skema TravelPlan.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.