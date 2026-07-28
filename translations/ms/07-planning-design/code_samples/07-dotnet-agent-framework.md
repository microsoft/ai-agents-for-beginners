# 🎯 Perancangan & Corak Reka Bentuk dengan Azure OpenAI (API Tindak Balas) (.NET)

## 📋 Objektif Pembelajaran

Buku nota ini menunjukkan corak perancangan dan reka bentuk kelas perusahaan untuk membina agen pintar menggunakan Microsoft Agent Framework dalam .NET dengan Azure OpenAI (API Tindak Balas). Anda akan belajar mencipta agen yang boleh memecahkan masalah kompleks, merancang penyelesaian berbilang langkah, dan melaksanakan aliran kerja yang canggih dengan ciri perusahaan .NET.

## ⚙️ Keperluan & Persediaan

**Persekitaran Pembangunan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan sambungan C#
- Langganan Azure dengan sumber Azure OpenAI dan penyebaran model
- Azure CLI — daftar masuk dengan `az login`

**Pergantungan Diperlukan:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurasi Persekitaran (fail .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Menjalankan Kod

Pelajaran ini termasuk pelaksanaan Aplikasi Fail Tunggal .NET. Untuk menjalankannya:

```bash
# Jadikan fail boleh dilaksanakan (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Jalankan aplikasi
./07-dotnet-agent-framework.cs
```

Atau gunakan perintah dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Pelaksanaan Kod

Pelaksanaan lengkap tersedia dalam `07-dotnet-agent-framework.cs`, yang menunjukkan:

- Memuat konfigurasi persekitaran dengan DotNetEnv
- Mengkonfigurasi klien Azure OpenAI dan mencipta agen AI menggunakan `GetChatClient().AsAIAgent()`
- Mendefinisikan model data berstruktur (Plan dan TravelPlan) dengan penyerialan JSON
- Mencipta agen AI dengan output berstruktur menggunakan skema JSON
- Melaksanakan permintaan perancangan dengan tindak balas yang jenis-selamat

## Konsep Utama

### Perancangan Berstruktur dengan Model Jenis-Selamat

Agen menggunakan kelas C# untuk menentukan struktur output perancangan:

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

Agen dikonfigurasi untuk mengembalikan tindak balas yang sepadan dengan skema TravelPlan:

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

### Arahan Agen Perancangan

Agen bertindak sebagai penyelaras, mendelegasikan tugasan kepada sub-agen khusus:

- FlightBooking: Untuk tempahan penerbangan dan menyediakan maklumat penerbangan
- HotelBooking: Untuk tempahan hotel dan menyediakan maklumat hotel
- CarRental: Untuk tempahan kereta dan menyediakan maklumat sewaan kereta
- ActivitiesBooking: Untuk tempahan aktiviti dan menyediakan maklumat aktiviti
- DestinationInfo: Untuk menyediakan maklumat tentang destinasi
- DefaultAgent: Untuk mengendalikan permintaan am

## Output Yang Dijangka

Apabila anda menjalankan agen dengan permintaan perancangan perjalanan, ia akan menganalisis permintaan dan menghasilkan pelan berstruktur dengan penugasan tugasan yang sesuai kepada agen khusus, diformatkan sebagai JSON yang mematuhi skema TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->