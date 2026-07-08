# 🎯 Reka Bentuk & Corak Perancangan dengan Azure OpenAI (Responses API) (.NET)

## 📋 Objektif Pembelajaran

Buku nota ini menunjukkan corak perancangan dan reka bentuk bertaraf perusahaan untuk membina ejen pintar menggunakan Microsoft Agent Framework dalam .NET dengan Azure OpenAI (Responses API). Anda akan belajar untuk mencipta ejen yang boleh menguraikan masalah yang kompleks, merancang penyelesaian berbilang langkah, dan melaksanakan aliran kerja sofistikated dengan ciri perusahaan .NET.

## ⚙️ Prasyarat & Persediaan

**Persekitaran Pembangunan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan sambungan C#
- Langganan Azure dengan sumber Azure OpenAI dan penggubalan model
- Azure CLI — log masuk dengan `az login`

**Kebergantungan Diperlukan:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurasi Persekitaran (fail .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Menjalankan Kod

Pelajaran ini termasuk pelaksanaan Aplikasi Fail Tunggal .NET. Untuk menjalankannya:

```bash
# Jadikan fail boleh dilaksanakan (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Jalankan aplikasi
./07-dotnet-agent-framework.cs
```

Atau gunakan arahan dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Pelaksanaan Kod

Pelaksanaan lengkap tersedia dalam `07-dotnet-agent-framework.cs`, yang menunjukkan:

- Memuatkan konfigurasi persekitaran dengan DotNetEnv
- Mengkonfigurasi pelanggan Azure OpenAI untuk Responses API
- Mendefinisikan model data berstruktur (Plan dan TravelPlan) dengan penserialan JSON
- Mencipta agen AI dengan output berstruktur menggunakan skema JSON
- Melaksanakan permintaan perancangan dengan respons jenis-amanah

## Konsep Utama

### Perancangan Berstruktur dengan Model Jenis-Amanah

Ejen menggunakan kelas C# untuk mendefinisikan struktur output perancangan:

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

Ejen dikonfigurasi untuk mengembalikan respons yang sepadan dengan skema TravelPlan:

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

### Arahan Ejen Perancangan

Ejen bertindak sebagai penyelaras, mendelegasikan tugasan kepada sub-ejen khusus:

- FlightBooking: Untuk menempah penerbangan dan menyediakan maklumat penerbangan
- HotelBooking: Untuk menempah hotel dan menyediakan maklumat hotel
- CarRental: Untuk menempah kereta dan menyediakan maklumat sewaan kereta
- ActivitiesBooking: Untuk menempah aktiviti dan menyediakan maklumat aktiviti
- DestinationInfo: Untuk menyediakan maklumat tentang destinasi
- DefaultAgent: Untuk mengendalikan permintaan umum

## Output Dijangka

Apabila anda menjalankan ejen dengan permintaan perancangan perjalanan, ia akan menganalisis permintaan tersebut dan menjana pelan berstruktur dengan tugas yang sesuai diberikan kepada ejen khusus, diformat sebagai JSON yang mematuhi skema TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->