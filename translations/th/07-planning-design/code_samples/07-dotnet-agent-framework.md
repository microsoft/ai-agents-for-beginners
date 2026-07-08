# 🎯 การวางแผนและรูปแบบการออกแบบด้วย Azure OpenAI (Responses API) (.NET)

## 📋 วัตถุประสงค์การเรียนรู้

สมุดบันทึกนี้แสดงให้เห็นถึงรูปแบบการวางแผนและออกแบบระดับองค์กรสำหรับการสร้างเอเจนต์อัจฉริยะโดยใช้ Microsoft Agent Framework ใน .NET กับ Azure OpenAI (Responses API) คุณจะได้เรียนรู้การสร้างเอเจนต์ที่สามารถแยกปัญหาซับซ้อน ออกแบบวิธีแก้ไขแบบหลายขั้นตอน และดำเนินการเวิร์กโฟลว์ขั้นสูงด้วยคุณสมบัติระดับองค์กรของ .NET

## ⚙️ ข้อกำหนดเบื้องต้นและการตั้งค่า

**สภาพแวดล้อมการพัฒนา:**
- .NET 9.0 SDK หรือสูงกว่า
- Visual Studio 2022 หรือ VS Code พร้อมส่วนขยาย C#
- บัญชี Azure ที่มีทรัพยากร Azure OpenAI และการปรับใช้โมเดล
- Azure CLI — ลงชื่อเข้าใช้ด้วย `az login`

**การติดตั้งที่จำเป็น:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**การกำหนดค่าสภาพแวดล้อม (.env file):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## การรันโค้ด

บทเรียนนี้มีตัวอย่างแอปแบบไฟล์เดียวของ .NET ในการรัน:

```bash
# ทำให้ไฟล์เรียกใช้งานได้ (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# รันแอปพลิเคชัน
./07-dotnet-agent-framework.cs
```

หรือใช้คำสั่ง dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## การใช้งานโค้ด

การใช้งานครบถ้วนมีอยู่ในไฟล์ `07-dotnet-agent-framework.cs` ซึ่งแสดงถึง:

- การโหลดการกำหนดค่าสิ่งแวดล้อมด้วย DotNetEnv
- การกำหนดค่าไคลเอ็นต์ Azure OpenAI สำหรับ Responses API
- การกำหนดโมเดลข้อมูลเชิงโครงสร้าง (Plan และ TravelPlan) พร้อมการแปลงข้อมูลเป็น JSON
- การสร้างเอเจนต์ AI พร้อมผลลัพธ์เชิงโครงสร้างโดยใช้สกีมา JSON
- การเรียกใช้คำขอวางแผนที่มีการตอบสนองแบบปลอดภัยด้วยชนิดข้อมูล

## แนวคิดสำคัญ

### การวางแผนเชิงโครงสร้างด้วยโมเดลที่ปลอดภัยชนิดข้อมูล

เอเจนต์ใช้คลาส C# เพื่อกำหนดโครงสร้างของผลลัพธ์การวางแผน:

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

### สกีมา JSON สำหรับผลลัพธ์เชิงโครงสร้าง

เอเจนต์ถูกตั้งค่าให้คืนคำตอบที่ตรงตามสกีมา TravelPlan:

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

### คำแนะนำสำหรับเอเจนต์วางแผน

เอเจนต์ทำหน้าที่เป็นผู้ประสานงาน มอบหมายงานให้เอเจนต์เฉพาะด้าน:

- FlightBooking: สำหรับจองเที่ยวบินและให้ข้อมูลเที่ยวบิน
- HotelBooking: สำหรับจองโรงแรมและให้ข้อมูลโรงแรม
- CarRental: สำหรับจองรถยนต์และให้ข้อมูลการเช่ารถ
- ActivitiesBooking: สำหรับจองกิจกรรมและให้ข้อมูลกิจกรรม
- DestinationInfo: สำหรับให้ข้อมูลเกี่ยวกับจุดหมายปลายทาง
- DefaultAgent: สำหรับจัดการคำขอทั่วไป

## ผลลัพธ์ที่คาดหวัง

เมื่อคุณรันเอเจนต์ด้วยคำขอวางแผนการเดินทาง มันจะวิเคราะห์คำขอและสร้างแผนเชิงโครงสร้างพร้อมการมอบหมายงานที่เหมาะสมให้กับเอเจนต์เฉพาะด้าน พร้อมทั้งจัดรูปแบบเป็น JSON ที่เป็นไปตามสกีมา TravelPlan

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->