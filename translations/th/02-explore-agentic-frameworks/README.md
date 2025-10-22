<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86b9c2b24da3b3e61711182ffa72601c",
  "translation_date": "2025-09-29T22:29:56+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "th"
}
-->
[![Exploring AI Agent Frameworks](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.th.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# สำรวจกรอบการทำงานของ AI Agent

กรอบการทำงานของ AI Agent คือแพลตฟอร์มซอฟต์แวร์ที่ออกแบบมาเพื่อช่วยให้การสร้าง การปรับใช้ และการจัดการ AI Agent เป็นเรื่องง่ายขึ้น กรอบการทำงานเหล่านี้มอบส่วนประกอบสำเร็จรูป เครื่องมือ และการจัดการที่ช่วยให้การพัฒนาระบบ AI ที่ซับซ้อนเป็นไปอย่างมีประสิทธิภาพ

กรอบการทำงานเหล่านี้ช่วยให้นักพัฒนาสามารถมุ่งเน้นไปที่แง่มุมเฉพาะของแอปพลิเคชันของตน โดยใช้วิธีการมาตรฐานในการแก้ไขปัญหาทั่วไปในกระบวนการพัฒนา AI Agent ซึ่งช่วยเพิ่มความสามารถในการขยายตัว การเข้าถึง และประสิทธิภาพในการสร้างระบบ AI

## บทนำ

บทเรียนนี้จะครอบคลุม:

- กรอบการทำงานของ AI Agent คืออะไร และช่วยให้นักพัฒนาสามารถทำอะไรได้บ้าง?
- ทีมสามารถใช้กรอบการทำงานเหล่านี้เพื่อสร้างต้นแบบอย่างรวดเร็ว ปรับปรุง และเพิ่มความสามารถของ Agent ได้อย่างไร?
- ความแตกต่างระหว่างกรอบการทำงานและเครื่องมือที่สร้างโดย Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, และ <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> คืออะไร?
- ฉันสามารถผสานรวมเครื่องมือในระบบ Azure ที่มีอยู่ได้โดยตรง หรือจำเป็นต้องใช้โซลูชันแบบแยกส่วน?
- Azure AI Agents Service คืออะไร และช่วยฉันได้อย่างไร?

## เป้าหมายการเรียนรู้

เป้าหมายของบทเรียนนี้คือช่วยให้คุณเข้าใจ:

- บทบาทของกรอบการทำงานของ AI Agent ในการพัฒนา AI
- วิธีใช้กรอบการทำงานของ AI Agent เพื่อสร้าง Agent ที่ชาญฉลาด
- ความสามารถสำคัญที่กรอบการทำงานของ AI Agent มอบให้
- ความแตกต่างระหว่าง AutoGen, Semantic Kernel และ Azure AI Agent Service

## กรอบการทำงานของ AI Agent คืออะไร และช่วยให้นักพัฒนาสามารถทำอะไรได้บ้าง?

กรอบการทำงาน AI แบบดั้งเดิมสามารถช่วยให้คุณผสาน AI เข้ากับแอปพลิเคชันของคุณ และทำให้แอปพลิเคชันเหล่านี้ดีขึ้นในด้านต่าง ๆ ดังนี้:

- **การปรับแต่งเฉพาะบุคคล**: AI สามารถวิเคราะห์พฤติกรรมและความชอบของผู้ใช้เพื่อให้คำแนะนำ เนื้อหา และประสบการณ์ที่ปรับแต่งเฉพาะบุคคล
ตัวอย่าง: บริการสตรีมมิ่งอย่าง Netflix ใช้ AI เพื่อแนะนำภาพยนตร์และรายการทีวีตามประวัติการรับชม ซึ่งช่วยเพิ่มการมีส่วนร่วมและความพึงพอใจของผู้ใช้
- **การทำงานอัตโนมัติและประสิทธิภาพ**: AI สามารถทำงานซ้ำ ๆ โดยอัตโนมัติ ปรับปรุงกระบวนการทำงาน และเพิ่มประสิทธิภาพการดำเนินงาน
ตัวอย่าง: แอปบริการลูกค้าใช้แชทบอทที่ขับเคลื่อนด้วย AI เพื่อจัดการคำถามทั่วไป ลดเวลาตอบกลับ และช่วยให้เจ้าหน้าที่มนุษย์มีเวลาสำหรับปัญหาที่ซับซ้อนมากขึ้น
- **ประสบการณ์ผู้ใช้ที่ดีขึ้น**: AI สามารถปรับปรุงประสบการณ์ผู้ใช้โดยรวมด้วยการมอบคุณสมบัติอัจฉริยะ เช่น การจดจำเสียง การประมวลผลภาษาธรรมชาติ และข้อความคาดการณ์
ตัวอย่าง: ผู้ช่วยเสมือนอย่าง Siri และ Google Assistant ใช้ AI เพื่อเข้าใจและตอบสนองต่อคำสั่งเสียง ทำให้ผู้ใช้โต้ตอบกับอุปกรณ์ได้ง่ายขึ้น

### ฟังดูดีใช่ไหม แล้วทำไมเราถึงต้องการกรอบการทำงานของ AI Agent?

กรอบการทำงานของ AI Agent เป็นมากกว่ากรอบการทำงาน AI ทั่วไป เพราะมันถูกออกแบบมาเพื่อสร้าง Agent ที่ชาญฉลาด ซึ่งสามารถโต้ตอบกับผู้ใช้ Agent อื่น ๆ และสภาพแวดล้อมเพื่อบรรลุเป้าหมายเฉพาะ ตัว Agent เหล่านี้สามารถแสดงพฤติกรรมอิสระ ตัดสินใจ และปรับตัวให้เข้ากับสภาพแวดล้อมที่เปลี่ยนแปลงได้ ลองมาดูความสามารถสำคัญที่กรอบการทำงานของ AI Agent มอบให้:

- **การทำงานร่วมกันและการประสานงานของ Agent**: ช่วยสร้าง AI Agent หลายตัวที่สามารถทำงานร่วมกัน สื่อสาร และประสานงานเพื่อแก้ไขงานที่ซับซ้อน
- **การทำงานอัตโนมัติและการจัดการงาน**: มอบกลไกสำหรับการทำงานหลายขั้นตอนโดยอัตโนมัติ การมอบหมายงาน และการจัดการงานแบบไดนามิกระหว่าง Agent
- **ความเข้าใจและการปรับตัวตามบริบท**: มอบความสามารถให้ Agent เข้าใจบริบท ปรับตัวให้เข้ากับสภาพแวดล้อมที่เปลี่ยนแปลง และตัดสินใจตามข้อมูลแบบเรียลไทม์

สรุปคือ Agent ช่วยให้คุณทำสิ่งต่าง ๆ ได้มากขึ้น ยกระดับการทำงานอัตโนมัติไปอีกขั้น และสร้างระบบที่ชาญฉลาดมากขึ้นที่สามารถปรับตัวและเรียนรู้จากสภาพแวดล้อม

## วิธีสร้างต้นแบบ ปรับปรุง และเพิ่มความสามารถของ Agent อย่างรวดเร็ว?

นี่เป็นพื้นที่ที่มีการเปลี่ยนแปลงอย่างรวดเร็ว แต่มีบางสิ่งที่เป็นเรื่องทั่วไปในกรอบการทำงานของ AI Agent ส่วนใหญ่ที่สามารถช่วยให้คุณสร้างต้นแบบและปรับปรุงได้อย่างรวดเร็ว ได้แก่ ส่วนประกอบแบบโมดูล เครื่องมือการทำงานร่วมกัน และการเรียนรู้แบบเรียลไทม์ ลองมาดูรายละเอียดกัน:

- **ใช้ส่วนประกอบแบบโมดูล**: AI SDK มีส่วนประกอบสำเร็จรูป เช่น ตัวเชื่อมต่อ AI และ Memory การเรียกฟังก์ชันโดยใช้ภาษาธรรมชาติหรือปลั๊กอินโค้ด เทมเพลตคำสั่ง และอื่น ๆ
- **ใช้เครื่องมือการทำงานร่วมกัน**: ออกแบบ Agent ที่มีบทบาทและงานเฉพาะ เพื่อทดสอบและปรับปรุงกระบวนการทำงานร่วมกัน
- **เรียนรู้แบบเรียลไทม์**: ใช้กลไกการตอบกลับที่ Agent เรียนรู้จากการโต้ตอบและปรับพฤติกรรมแบบไดนามิก

### ใช้ส่วนประกอบแบบโมดูล

SDK เช่น Microsoft Semantic Kernel และ LangChain มีส่วนประกอบสำเร็จรูป เช่น ตัวเชื่อมต่อ AI เทมเพลตคำสั่ง และการจัดการ Memory

**วิธีที่ทีมสามารถใช้สิ่งเหล่านี้**: ทีมสามารถประกอบส่วนประกอบเหล่านี้อย่างรวดเร็วเพื่อสร้างต้นแบบที่ใช้งานได้ โดยไม่ต้องเริ่มต้นจากศูนย์ ซึ่งช่วยให้สามารถทดลองและปรับปรุงได้อย่างรวดเร็ว

**วิธีการทำงานในทางปฏิบัติ**: คุณสามารถใช้ตัวแยกวิเคราะห์สำเร็จรูปเพื่อดึงข้อมูลจากการป้อนข้อมูลของผู้ใช้ โมดูล Memory เพื่อจัดเก็บและเรียกข้อมูล และตัวสร้างคำสั่งเพื่อโต้ตอบกับผู้ใช้ โดยไม่ต้องสร้างส่วนประกอบเหล่านี้ตั้งแต่ต้น

**ตัวอย่างโค้ด**. ลองดูตัวอย่างวิธีใช้ตัวเชื่อมต่อ AI สำเร็จรูปกับ Semantic Kernel Python และ .Net ที่ใช้การเรียกฟังก์ชันอัตโนมัติเพื่อให้โมเดลตอบสนองต่อการป้อนข้อมูลของผู้ใช้:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

จากตัวอย่างนี้ คุณจะเห็นวิธีใช้ตัวแยกวิเคราะห์สำเร็จรูปเพื่อดึงข้อมูลสำคัญจากการป้อนข้อมูลของผู้ใช้ เช่น ต้นทาง ปลายทาง และวันที่ของคำขอจองเที่ยวบิน วิธีการแบบโมดูลนี้ช่วยให้คุณมุ่งเน้นไปที่ตรรกะระดับสูง

### ใช้เครื่องมือการทำงานร่วมกัน

กรอบการทำงาน เช่น CrewAI, Microsoft AutoGen และ Semantic Kernel ช่วยให้สามารถสร้าง Agent หลายตัวที่สามารถทำงานร่วมกันได้

**วิธีที่ทีมสามารถใช้สิ่งเหล่านี้**: ทีมสามารถออกแบบ Agent ที่มีบทบาทและงานเฉพาะ เพื่อทดสอบและปรับปรุงกระบวนการทำงานร่วมกัน และเพิ่มประสิทธิภาพของระบบโดยรวม

**วิธีการทำงานในทางปฏิบัติ**: คุณสามารถสร้างทีม Agent ที่แต่ละตัวมีฟังก์ชันเฉพาะ เช่น การดึงข้อมูล การวิเคราะห์ หรือการตัดสินใจ Agent เหล่านี้สามารถสื่อสารและแบ่งปันข้อมูลเพื่อบรรลุเป้าหมายร่วมกัน เช่น การตอบคำถามของผู้ใช้หรือการทำงานให้เสร็จสมบูรณ์

**ตัวอย่างโค้ด (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

ในโค้ดก่อนหน้านี้ คุณจะเห็นวิธีสร้างงานที่เกี่ยวข้องกับ Agent หลายตัวที่ทำงานร่วมกันเพื่อวิเคราะห์ข้อมูล แต่ละ Agent มีฟังก์ชันเฉพาะ และงานจะดำเนินการโดยการประสานงานระหว่าง Agent เพื่อให้ได้ผลลัพธ์ที่ต้องการ การสร้าง Agent เฉพาะที่มีบทบาทเฉพาะช่วยปรับปรุงประสิทธิภาพและประสิทธิผลของงาน

### เรียนรู้แบบเรียลไทม์

กรอบการทำงานขั้นสูงมอบความสามารถในการทำความเข้าใจบริบทและปรับตัวแบบเรียลไทม์

**วิธีที่ทีมสามารถใช้สิ่งเหล่านี้**: ทีมสามารถใช้กลไกการตอบกลับที่ Agent เรียนรู้จากการโต้ตอบและปรับพฤติกรรมแบบไดนามิก ซึ่งนำไปสู่การปรับปรุงและการพัฒนาความสามารถอย่างต่อเนื่อง

**วิธีการทำงานในทางปฏิบัติ**: Agent สามารถวิเคราะห์ความคิดเห็นของผู้ใช้ ข้อมูลสภาพแวดล้อม และผลลัพธ์ของงานเพื่ออัปเดตฐานความรู้ ปรับอัลกอริทึมการตัดสินใจ และปรับปรุงประสิทธิภาพเมื่อเวลาผ่านไป กระบวนการเรียนรู้แบบวนซ้ำนี้ช่วยให้ Agent ปรับตัวให้เข้ากับสภาพแวดล้อมที่เปลี่ยนแปลงและความชอบของผู้ใช้ ซึ่งช่วยเพิ่มประสิทธิภาพของระบบโดยรวม

## ความแตกต่างระหว่างกรอบการทำงาน AutoGen, Semantic Kernel และ Azure AI Agent Service คืออะไร?

มีหลายวิธีในการเปรียบเทียบกรอบการทำงานเหล่านี้ แต่ลองมาดูความแตกต่างสำคัญในแง่ของการออกแบบ ความสามารถ และกรณีการใช้งานเป้าหมาย:

## AutoGen

AutoGen เป็นกรอบการทำงานแบบโอเพ่นซอร์สที่พัฒนาโดย Microsoft Research's AI Frontiers Lab โดยมุ่งเน้นไปที่แอปพลิเคชันแบบกระจายที่ขับเคลื่อนด้วยเหตุการณ์ ซึ่งช่วยให้สามารถใช้งาน LLM และ SLM หลายตัว เครื่องมือ และรูปแบบการออกแบบ Agent หลายตัวขั้นสูง

AutoGen ถูกสร้างขึ้นโดยมีแนวคิดหลักเกี่ยวกับ Agent ซึ่งเป็นเอนทิตีอิสระที่สามารถรับรู้สภาพแวดล้อม ตัดสินใจ และดำเนินการเพื่อบรรลุเป้าหมายเฉพาะ Agent สื่อสารผ่านข้อความแบบอะซิงโครนัส ซึ่งช่วยให้ทำงานได้อย่างอิสระและขนานกัน เพิ่มความสามารถในการขยายตัวและการตอบสนองของระบบ

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agent ถูกสร้างขึ้นบนพื้นฐานของ Actor Model</a> ตามที่ Wikipedia กล่าวไว้ Actor คือ _องค์ประกอบพื้นฐานของการคำนวณแบบขนาน ในการตอบสนองต่อข้อความที่ได้รับ Actor สามารถ: ตัดสินใจในระดับท้องถิ่น สร้าง Actor เพิ่มเติม ส่งข้อความเพิ่มเติม และกำหนดวิธีตอบสนองต่อข้อความถัดไปที่ได้รับ_

**กรณีการใช้งาน**: การสร้างโค้ดอัตโนมัติ งานวิเคราะห์ข้อมูล และการสร้าง Agent แบบกำหนดเองสำหรับฟังก์ชันการวางแผนและการวิจัย

นี่คือแนวคิดหลักที่สำคัญของ AutoGen:

- **Agent**. Agent คือเอนทิตีซอฟต์แวร์ที่:
  - **สื่อสารผ่านข้อความ** ซึ่งข้อความเหล่านี้สามารถเป็นแบบซิงโครนัสหรืออะซิงโครนัส
  - **รักษาสถานะของตัวเอง** ซึ่งสามารถปรับเปลี่ยนได้โดยข้อความที่เข้ามา
  - **ดำเนินการ** เพื่อตอบสนองต่อข้อความที่ได้รับหรือการเปลี่ยนแปลงสถานะของตัวเอง การดำเนินการเหล่านี้อาจปรับเปลี่ยนสถานะของ Agent และสร้างผลกระทบภายนอก เช่น การอัปเดตบันทึกข้อความ การส่งข้อความใหม่ การดำเนินการโค้ด หรือการเรียก API

  นี่คือตัวอย่างโค้ดสั้น ๆ ที่คุณสร้าง Agent ของคุณเองที่มีความสามารถในการแชท:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
ในโค้ดก่อนหน้านี้ `MyAgent` ถูกสร้างขึ้นและสืบทอดจาก `RoutedAgent` โดยมีตัวจัดการข้อความที่พิมพ์เนื้อหาของข้อความและส่งการตอบกลับโดยใช้ตัวแทน `AssistantAgent` โดยเฉพาะอย่างยิ่งสังเกตว่าเราได้กำหนด `self._delegate` เป็นอินสแตนซ์ของ `AssistantAgent` ซึ่งเป็น Agent สำเร็จรูปที่สามารถจัดการการตอบกลับการแชทได้

ลองแจ้ง AutoGen เกี่ยวกับประเภท Agent นี้และเริ่มโปรแกรมต่อไป:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

ในโค้ดก่อนหน้านี้ Agent ถูกลงทะเบียนกับ Runtime และจากนั้นมีการส่งข้อความไปยัง Agent ซึ่งส่งผลให้เกิดผลลัพธ์ดังนี้:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Agent หลายตัว**. AutoGen รองรับการสร้าง Agent หลายตัวที่สามารถทำงานร่วมกันเพื่อบรรลุงานที่ซับซ้อน Agent สามารถสื่อสาร แบ่งปันข้อมูล และประสานการดำเนินการเพื่อแก้ไขปัญหาได้อย่างมีประสิทธิภาพ ในการสร้างระบบ Agent หลายตัว คุณสามารถกำหนดประเภท Agent ต่าง ๆ ที่มีฟังก์ชันและบทบาทเฉพาะ เช่น การดึงข้อมูล การวิเคราะห์ การตัดสินใจ และการโต้ตอบกับผู้ใช้ ลองดูตัวอย่างการสร้างดังกล่าวเพื่อให้เราเข้าใจ:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

ในโค้ดก่อนหน้านี้ เรามี `GroupChatManager` ที่ลงทะเบียนกับ Runtime ผู้จัดการนี้มีหน้าที่ประสานการโต้ตอบระหว่างประเภท Agent ต่าง ๆ เช่น นักเขียน นักวาดภาพ บรรณาธิการ และผู้ใช้

- **Agent Runtime**. กรอบการทำงานมอบสภาพแวดล้อม Runtime ที่ช่วยให้การสื่อสารระหว่าง Agent จัดการตัวตนและวงจรชีวิตของ Agent และบังคับใช้ขอบเขตความปลอดภัยและความเป็นส่วนตัว ซึ่งหมายความว่าคุณสามารถเรียกใช้ Agent ของคุณในสภาพแวดล้อมที่ปลอดภัยและควบคุมได้ เพื่อให้มั่นใจว่า Agent สามารถโต้ตอบได้อย่างปลอดภัยและมีประสิทธิภาพ มี Runtime สองประเภทที่น่าสนใจ:
  - **Runtime แบบ Stand-alone**. นี่เป็นตัวเลือกที่ดีสำหรับแอปพลิเคชันที่ใช้กระบวนการเดียว ซึ่ง Agent ทั้งหมดถูกนำไปใช้ในภาษาโปรแกรมเดียวกันและทำงานในกระบวนการเดียว นี่คือตัวอย่างการทำงาน:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Runtime แบบ Stand-alone</a>   
Application stack

    *Agent สื่อสารผ่านข้อความผ่าน Runtime และ Runtime จัดการวงจรชีวิตของ Agent*

  - **Runtime Agent แบบกระจาย** เหมาะสำหรับแอปพลิเคชันที่ใช้หลายกระบวนการ ซึ่ง Agent อาจถูกนำไปใช้ในภาษาการเขียนโปรแกรมต่าง ๆ และทำงานบนเครื่องต่าง ๆ นี่คือตัวอย่างการทำงาน:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Runtime แบบกระจาย</a>

## Semantic Kernel + Agent Framework

Semantic Kernel เป็น SDK การจัดการ AI ที่พร้อมใช้งานในระดับองค์กร ประกอบด้วยตัวเชื่อมต่อ AI และ Memory พร้อมกับ Agent Framework

ลองมาดูส่วนประกอบหลักกันก่อน:

- **ตัวเชื่อมต่อ AI**: นี่คือตัวเชื่อมต่อกับบริการ AI ภายนอกและแหล่งข้อมูลสำหรับใช้งานใน Python และ C#

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

นี่คือตัวอย่างง่าย ๆ ของวิธีสร้าง Kernel และเพิ่มบริการการตอบกลับการแชท Semantic Kernel สร้างการเชื่อมต่อกับบริการ AI ภายนอก ในกรณีนี้คือ Azure OpenAI Chat Completion

- **ปลั๊กอิน**: ปลั๊กอินเหล่านี้ครอบคลุมฟังก์ช
ข้อเท็จจริงเหล่านี้จะถูกจัดเก็บไว้ในคอลเลกชันหน่วยความจำ `SummarizedAzureDocs` นี่เป็นตัวอย่างที่เรียบง่ายมาก แต่คุณสามารถเห็นได้ว่าคุณสามารถจัดเก็บข้อมูลในหน่วยความจำเพื่อให้ LLM ใช้งานได้อย่างไร

นี่คือพื้นฐานของเฟรมเวิร์ก Semantic Kernel แล้ว Agent Framework ล่ะ?

## Azure AI Agent Service

Azure AI Agent Service เป็นส่วนเสริมใหม่ที่เปิดตัวในงาน Microsoft Ignite 2024 ซึ่งช่วยให้สามารถพัฒนาและปรับใช้ AI agents ด้วยโมเดลที่ยืดหยุ่นมากขึ้น เช่น การเรียกใช้งาน LLMs แบบโอเพ่นซอร์สโดยตรง เช่น Llama 3, Mistral และ Cohere

Azure AI Agent Service มีระบบรักษาความปลอดภัยระดับองค์กรที่แข็งแกร่งและวิธีการจัดเก็บข้อมูลที่เหมาะสำหรับการใช้งานในองค์กร

บริการนี้สามารถใช้งานได้ทันทีร่วมกับเฟรมเวิร์กการจัดการหลายเอเจนต์ เช่น AutoGen และ Semantic Kernel

บริการนี้อยู่ในช่วง Public Preview และรองรับ Python และ C# สำหรับการสร้างเอเจนต์

โดยใช้ Semantic Kernel Python เราสามารถสร้าง Azure AI Agent พร้อมปลั๊กอินที่ผู้ใช้กำหนดเองได้:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### แนวคิดหลัก

Azure AI Agent Service มีแนวคิดหลักดังนี้:

- **Agent**. Azure AI Agent Service ผสานรวมกับ Azure AI Foundry ภายใน AI Foundry เอเจนต์ AI ทำหน้าที่เป็น "ไมโครเซอร์วิสอัจฉริยะ" ที่สามารถใช้ตอบคำถาม (RAG) ดำเนินการ หรือทำงานอัตโนมัติได้อย่างสมบูรณ์ โดยใช้พลังของโมเดล AI เชิงสร้างสรรค์ร่วมกับเครื่องมือที่ช่วยให้สามารถเข้าถึงและโต้ตอบกับแหล่งข้อมูลในโลกจริงได้ ตัวอย่างของเอเจนต์มีดังนี้:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ในตัวอย่างนี้ เอเจนต์ถูกสร้างขึ้นด้วยโมเดล `gpt-4o-mini` ชื่อ `my-agent` และคำแนะนำ `You are helpful agent` เอเจนต์นี้มีเครื่องมือและทรัพยากรที่พร้อมสำหรับการทำงานด้านการตีความโค้ด

- **Thread และข้อความ**. Thread เป็นอีกหนึ่งแนวคิดสำคัญ มันแสดงถึงการสนทนาหรือการโต้ตอบระหว่างเอเจนต์และผู้ใช้ Threads สามารถใช้ติดตามความคืบหน้าของการสนทนา เก็บข้อมูลบริบท และจัดการสถานะของการโต้ตอบ ตัวอย่างของ Thread มีดังนี้:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    ในโค้ดก่อนหน้านี้ Thread ถูกสร้างขึ้น จากนั้นข้อความถูกส่งไปยัง Thread โดยการเรียก `create_and_process_run` เอเจนต์ถูกขอให้ทำงานใน Thread สุดท้ายข้อความถูกดึงและบันทึกเพื่อดูการตอบสนองของเอเจนต์ ข้อความแสดงถึงความคืบหน้าของการสนทนาระหว่างผู้ใช้และเอเจนต์ นอกจากนี้ยังสำคัญที่ต้องเข้าใจว่าข้อความสามารถมีหลายประเภท เช่น ข้อความ รูปภาพ หรือไฟล์ ซึ่งเป็นผลลัพธ์ของงานที่เอเจนต์ทำ เช่น การตอบกลับเป็นข้อความหรือรูปภาพ เป็นต้น ในฐานะนักพัฒนา คุณสามารถใช้ข้อมูลนี้เพื่อประมวลผลเพิ่มเติมหรือแสดงผลให้ผู้ใช้

- **การผสานรวมกับเฟรมเวิร์ก AI อื่นๆ**. Azure AI Agent Service สามารถโต้ตอบกับเฟรมเวิร์กอื่นๆ เช่น AutoGen และ Semantic Kernel ซึ่งหมายความว่าคุณสามารถสร้างส่วนหนึ่งของแอปในเฟรมเวิร์กเหล่านี้ และใช้ Agent Service เป็นตัวจัดการ หรือสร้างทุกอย่างใน Agent Service ได้

**กรณีการใช้งาน**: Azure AI Agent Service ถูกออกแบบมาสำหรับแอปพลิเคชันในองค์กรที่ต้องการการปรับใช้ AI agent ที่ปลอดภัย ขยายขนาดได้ และยืดหยุ่น

## ความแตกต่างระหว่างเฟรมเวิร์กเหล่านี้คืออะไร?

ดูเหมือนว่าเฟรมเวิร์กเหล่านี้จะมีความซ้อนทับกันมาก แต่ก็มีความแตกต่างสำคัญในแง่ของการออกแบบ ความสามารถ และกรณีการใช้งานเป้าหมาย:

- **AutoGen**: เป็นเฟรมเวิร์กสำหรับการทดลองที่มุ่งเน้นการวิจัยล้ำสมัยเกี่ยวกับระบบหลายเอเจนต์ เป็นสถานที่ที่ดีที่สุดสำหรับการทดลองและสร้างต้นแบบระบบหลายเอเจนต์ที่ซับซ้อน
- **Semantic Kernel**: เป็นไลบรารีเอเจนต์ที่พร้อมสำหรับการผลิตสำหรับการสร้างแอปพลิเคชันเอเจนต์ในองค์กร มุ่งเน้นที่แอปพลิเคชันเอเจนต์แบบกระจายที่ขับเคลื่อนด้วยเหตุการณ์ รองรับ LLMs และ SLMs หลายตัว เครื่องมือ และรูปแบบการออกแบบเอเจนต์เดี่ยว/หลายตัว
- **Azure AI Agent Service**: เป็นแพลตฟอร์มและบริการปรับใช้ใน Azure Foundry สำหรับเอเจนต์ มีการเชื่อมต่อกับบริการที่รองรับโดย Azure เช่น Azure OpenAI, Azure AI Search, Bing Search และการดำเนินการโค้ด

ยังไม่แน่ใจว่าจะเลือกอะไร?

### กรณีการใช้งาน

ลองดูว่ากรณีการใช้งานทั่วไปสามารถช่วยคุณได้หรือไม่:

> Q: ฉันกำลังทดลอง เรียนรู้ และสร้างแอปพลิเคชันเอเจนต์ต้นแบบ และต้องการสร้างและทดลองได้อย่างรวดเร็ว
>

>A: AutoGen จะเป็นตัวเลือกที่ดีสำหรับสถานการณ์นี้ เนื่องจากมุ่งเน้นที่แอปพลิเคชันเอเจนต์แบบกระจายที่ขับเคลื่อนด้วยเหตุการณ์ และรองรับรูปแบบการออกแบบเอเจนต์หลายตัวขั้นสูง

> Q: อะไรทำให้ AutoGen เป็นตัวเลือกที่ดีกว่า Semantic Kernel และ Azure AI Agent Service สำหรับกรณีการใช้งานนี้?
>
> A: AutoGen ถูกออกแบบมาโดยเฉพาะสำหรับแอปพลิเคชันเอเจนต์แบบกระจายที่ขับเคลื่อนด้วยเหตุการณ์ ทำให้เหมาะสำหรับการทำงานอัตโนมัติ เช่น การสร้างโค้ดและการวิเคราะห์ข้อมูล มันมีเครื่องมือและความสามารถที่จำเป็นในการสร้างระบบหลายเอเจนต์ที่ซับซ้อนอย่างมีประสิทธิภาพ

>Q: ฟังดูเหมือน Azure AI Agent Service ก็สามารถใช้งานได้ในกรณีนี้เช่นกัน มันมีเครื่องมือสำหรับการสร้างโค้ดและอื่นๆ ใช่ไหม?

>
> A: ใช่ Azure AI Agent Service เป็นบริการแพลตฟอร์มสำหรับเอเจนต์ และมีความสามารถในตัวสำหรับโมเดลหลายตัว Azure AI Search Bing Search และ Azure Functions มันทำให้การสร้างเอเจนต์ใน Foundry Portal และการปรับใช้ในระดับใหญ่เป็นเรื่องง่าย

> Q: ฉันยังสับสนอยู่ แค่บอกตัวเลือกเดียวให้ฉัน
>
> A: ตัวเลือกที่ดีคือการสร้างแอปพลิเคชันของคุณใน Semantic Kernel ก่อน แล้วใช้ Azure AI Agent Service เพื่อปรับใช้เอเจนต์ของคุณ วิธีนี้ช่วยให้คุณสามารถเก็บรักษาเอเจนต์ของคุณได้ง่าย ในขณะที่ใช้พลังของการสร้างระบบหลายเอเจนต์ใน Semantic Kernel นอกจากนี้ Semantic Kernel ยังมีตัวเชื่อมต่อใน AutoGen ทำให้การใช้เฟรมเวิร์กทั้งสองร่วมกันเป็นเรื่องง่าย

สรุปความแตกต่างสำคัญในตาราง:

| เฟรมเวิร์ก | จุดเน้น | แนวคิดหลัก | กรณีการใช้งาน |
| --- | --- | --- | --- |
| AutoGen | แอปพลิเคชันเอเจนต์แบบกระจายที่ขับเคลื่อนด้วยเหตุการณ์ | Agents, Personas, Functions, Data | การสร้างโค้ด การวิเคราะห์ข้อมูล |
| Semantic Kernel | การทำความเข้าใจและสร้างเนื้อหาที่เหมือนมนุษย์ | Agents, Modular Components, Collaboration | การทำความเข้าใจภาษา การสร้างเนื้อหา |
| Azure AI Agent Service | โมเดลที่ยืดหยุ่น ความปลอดภัยระดับองค์กร การสร้างโค้ด การเรียกใช้เครื่องมือ | Modularity, Collaboration, Process Orchestration | การปรับใช้ AI agent ที่ปลอดภัย ขยายขนาดได้ และยืดหยุ่น |

กรณีการใช้งานที่เหมาะสมที่สุดสำหรับแต่ละเฟรมเวิร์กคืออะไร?

## ฉันสามารถผสานรวมเครื่องมือในระบบ Azure ที่มีอยู่ของฉันโดยตรงได้หรือไม่ หรือฉันต้องการโซลูชันแบบสแตนด์อโลน?

คำตอบคือได้ คุณสามารถผสานรวมเครื่องมือในระบบ Azure ที่มีอยู่ของคุณโดยตรงกับ Azure AI Agent Service โดยเฉพาะ เนื่องจากมันถูกสร้างมาให้ทำงานร่วมกับบริการ Azure อื่นๆ ได้อย่างราบรื่น ตัวอย่างเช่น คุณสามารถผสานรวม Bing, Azure AI Search และ Azure Functions นอกจากนี้ยังมีการผสานรวมลึกกับ Azure AI Foundry

สำหรับ AutoGen และ Semantic Kernel คุณก็สามารถผสานรวมกับบริการ Azure ได้เช่นกัน แต่คุณอาจต้องเรียกใช้บริการ Azure จากโค้ดของคุณ อีกวิธีหนึ่งในการผสานรวมคือการใช้ Azure SDKs เพื่อโต้ตอบกับบริการ Azure จากเอเจนต์ของคุณ นอกจากนี้ อย่างที่กล่าวไป คุณสามารถใช้ Azure AI Agent Service เป็นตัวจัดการสำหรับเอเจนต์ที่สร้างใน AutoGen หรือ Semantic Kernel ซึ่งจะช่วยให้เข้าถึงระบบ Azure ได้ง่าย

### มีคำถามเพิ่มเติมเกี่ยวกับ AI Agent Frameworks หรือไม่?

เข้าร่วม [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) เพื่อพบปะกับผู้เรียนคนอื่นๆ เข้าร่วมชั่วโมงทำการ และรับคำตอบสำหรับคำถามเกี่ยวกับ AI Agents ของคุณ

## อ้างอิง

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel และ AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">การใช้ Azure AI Agent Service กับ AutoGen / Semantic Kernel เพื่อสร้างโซลูชันหลายเอเจนต์</a>

## บทเรียนก่อนหน้า

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## บทเรียนถัดไป

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้