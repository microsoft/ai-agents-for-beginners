# 🎯 การวางแผน & แบบแผนการออกแบบด้วย Azure OpenAI (Responses API) (.NET)

## 📋 วัตถุประสงค์การเรียนรู้

โน้ตบุ๊กนี้แสดงแบบแผนการวางแผนและการออกแบบระดับองค์กรสำหรับการสร้างเอเจนต์อัจฉริยะโดยใช้ Microsoft Agent Framework ใน .NET กับ Azure OpenAI (Responses API) คุณจะได้เรียนรู้วิธีสร้างเอเจนต์ที่สามารถแยกย่อยปัญหาซับซ้อน วางแผนโซลูชันหลายขั้นตอน และดำเนินเวิร์กโฟลว์ที่ซับซ้อนได้ด้วยคุณสมบัติระดับองค์กรของ .NET

## ⚙️ ข้อกำหนดเบื้องต้น & การตั้งค่า

**สภาพแวดล้อมการพัฒนา:**
- .NET 9.0 SDK หรือสูงกว่า
- Visual Studio 2022 หรือ VS Code พร้อมส่วนขยาย C#
- การสมัครใช้งาน Azure พร้อมทรัพยากร Azure OpenAI และการปรับใช้โมเดล
- Azure CLI — ลงชื่อเข้าใช้ด้วยคำสั่ง `az login`

**การติดตั้งไลบรารีที่จำเป็น:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**การกำหนดค่าสภาพแวดล้อม (.env file):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## การรันโค้ด

บทเรียนนี้รวมการใช้งานแอป .NET แบบ Single File การใช้งานโค้ดเรียกใช้ได้ดังนี้:

```bash
# ทำให้ไฟล์นี้เป็นไฟล์ที่สามารถรันได้ (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# รันแอปพลิเคชัน
./07-dotnet-agent-framework.cs
```

หรือใช้คำสั่ง dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## การใช้งานโค้ด

การใช้งานครบถ้วนอยู่ในไฟล์ `07-dotnet-agent-framework.cs` ซึ่งสาธิต:

- การโหลดการกำหนดค่าสภาพแวดล้อมด้วย DotNetEnv
- การตั้งค่าไคลเอนต์ Azure OpenAI และสร้างเอเจนต์ AI ด้วย `GetChatClient().AsAIAgent()`
- การกำหนดโมเดลข้อมูลแบบมีโครงสร้าง (Plan และ TravelPlan) ด้วยการทำ JSON serialization
- การสร้างเอเจนต์ AI ที่มีผลลัพธ์แบบมีโครงสร้างด้วย JSON schema
- การดำเนินการร้องขอการวางแผนด้วยการตอบกลับที่ปลอดภัยตามประเภทข้อมูล

## แนวคิดสำคัญ

### การวางแผนแบบมีโครงสร้างด้วยโมเดลที่ปลอดภัยตามประเภทข้อมูล

เอเจนต์ใช้คลาส C# ในการกำหนดโครงสร้างของผลลัพธ์การวางแผน:

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

### JSON Schema สำหรับผลลัพธ์ที่มีโครงสร้าง

เอเจนต์ถูกตั้งค่าให้ส่งกลับการตอบสนองที่ตรงกับสคีมา TravelPlan:

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

### คำสั่งสำหรับเอเจนต์การวางแผน

เอเจนต์ทำหน้าที่เป็นผู้ประสานงาน โดยมอบหมายงานให้แก่เอเจนต์ย่อยเฉพาะทาง:

- FlightBooking: สำหรับการจองเที่ยวบินและให้ข้อมูลเที่ยวบิน
- HotelBooking: สำหรับการจองโรงแรมและให้ข้อมูลโรงแรม
- CarRental: สำหรับการจองรถยนต์และให้ข้อมูลรถเช่า
- ActivitiesBooking: สำหรับการจองกิจกรรมและให้ข้อมูลกิจกรรม
- DestinationInfo: สำหรับให้ข้อมูลเกี่ยวกับจุดหมายปลายทาง
- DefaultAgent: สำหรับจัดการคำขอทั่วไป

## ผลลัพธ์ที่คาดหวัง

เมื่อคุณรันเอเจนต์ด้วยคำขอวางแผนการเดินทาง เอเจนต์จะวิเคราะห์คำขอและสร้างแผนการที่มีโครงสร้างพร้อมทั้งมอบหมายงานที่เหมาะสมให้กับเอเจนต์เฉพาะทาง โดยจัดรูปแบบเป็น JSON ตามสคีมา TravelPlan

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->