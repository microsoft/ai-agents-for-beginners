<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T11:12:18+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ur"
}
-->
[![AI ایجنٹ فریم ورک کا جائزہ](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.ur.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(اوپر دی گئی تصویر پر کلک کریں تاکہ اس سبق کی ویڈیو دیکھ سکیں)_

# AI ایجنٹ فریم ورک کا جائزہ

AI ایجنٹ فریم ورک ایسے سافٹ ویئر پلیٹ فارمز ہیں جو AI ایجنٹس کی تخلیق، تعیناتی، اور انتظام کو آسان بناتے ہیں۔ یہ فریم ورک ڈویلپرز کو پہلے سے تیار شدہ اجزاء، خلاصے، اور ٹولز فراہم کرتے ہیں جو پیچیدہ AI سسٹمز کی ترقی کو آسان بناتے ہیں۔

یہ فریم ورک ڈویلپرز کو ان کے ایپلیکیشنز کے منفرد پہلوؤں پر توجہ مرکوز کرنے میں مدد دیتے ہیں، AI ایجنٹ کی ترقی میں عام چیلنجز کے لیے معیاری طریقے فراہم کرتے ہیں۔ یہ AI سسٹمز کی توسیع پذیری، رسائی، اور کارکردگی کو بہتر بناتے ہیں۔

## تعارف

اس سبق میں شامل ہوگا:

- AI ایجنٹ فریم ورک کیا ہیں اور یہ ڈویلپرز کو کیا حاصل کرنے کے قابل بناتے ہیں؟
- ٹیمیں ان کا استعمال کیسے کر سکتی ہیں تاکہ ایجنٹ کی صلاحیتوں کو جلدی پروٹوٹائپ، تکرار، اور بہتر بنایا جا سکے؟
- Microsoft کے <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, اور <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> کے ذریعے بنائے گئے فریم ورک اور ٹولز میں کیا فرق ہے؟
- کیا میں اپنے موجودہ Azure ایکو سسٹم ٹولز کو براہ راست ضم کر سکتا ہوں، یا مجھے الگ حل کی ضرورت ہے؟
- Azure AI Agents سروس کیا ہے اور یہ میری کیسے مدد کر رہی ہے؟

## سیکھنے کے اہداف

اس سبق کے اہداف ہیں کہ آپ کو سمجھنے میں مدد دی جائے:

- AI ایجنٹ فریم ورک کا AI ترقی میں کردار۔
- AI ایجنٹ فریم ورک کا استعمال کرتے ہوئے ذہین ایجنٹس بنانے کا طریقہ۔
- AI ایجنٹ فریم ورک کے ذریعے فعال کردہ کلیدی صلاحیتیں۔
- AutoGen, Semantic Kernel, اور Azure AI Agent Service کے درمیان فرق۔

## AI ایجنٹ فریم ورک کیا ہیں اور یہ ڈویلپرز کو کیا کرنے کے قابل بناتے ہیں؟

روایتی AI فریم ورک آپ کو AI کو اپنی ایپس میں ضم کرنے اور ان ایپس کو درج ذیل طریقوں سے بہتر بنانے میں مدد کر سکتے ہیں:

- **ذاتی نوعیت**: AI صارف کے رویے اور ترجیحات کا تجزیہ کر سکتا ہے تاکہ ذاتی نوعیت کی تجاویز، مواد، اور تجربات فراہم کیے جا سکیں۔
مثال: Netflix جیسی اسٹریمنگ سروسز AI کا استعمال کرتی ہیں تاکہ دیکھنے کی تاریخ کی بنیاد پر فلمیں اور شوز تجویز کیے جا سکیں، صارف کی مشغولیت اور اطمینان کو بڑھایا جا سکے۔
- **خودکاریت اور کارکردگی**: AI بار بار ہونے والے کاموں کو خودکار بنا سکتا ہے، ورک فلو کو آسان بنا سکتا ہے، اور آپریشنل کارکردگی کو بہتر بنا سکتا ہے۔
مثال: کسٹمر سروس ایپس AI سے چلنے والے چیٹ بوٹس کا استعمال کرتی ہیں تاکہ عام سوالات کو سنبھالا جا سکے، جواب دینے کے وقت کو کم کیا جا سکے اور انسانی ایجنٹس کو زیادہ پیچیدہ مسائل کے لیے آزاد کیا جا سکے۔
- **بہتر صارف تجربہ**: AI مجموعی صارف تجربے کو بہتر بنا سکتا ہے، جیسے کہ آواز کی پہچان، قدرتی زبان کی پروسیسنگ، اور پیش گوئی کرنے والے متن جیسی ذہین خصوصیات فراہم کر کے۔
مثال: Siri اور Google Assistant جیسے ورچوئل اسسٹنٹس AI کا استعمال کرتے ہیں تاکہ آواز کے احکامات کو سمجھا جا سکے اور ان کا جواب دیا جا سکے، صارفین کے لیے اپنے آلات کے ساتھ بات چیت کرنا آسان بنایا جا سکے۔

### یہ سب بہت اچھا لگتا ہے، تو پھر ہمیں AI ایجنٹ فریم ورک کی ضرورت کیوں ہے؟

AI ایجنٹ فریم ورک صرف AI فریم ورک سے زیادہ کی نمائندگی کرتے ہیں۔ یہ ذہین ایجنٹس کی تخلیق کو فعال کرنے کے لیے ڈیزائن کیے گئے ہیں جو صارفین، دیگر ایجنٹس، اور ماحول کے ساتھ بات چیت کر سکتے ہیں تاکہ مخصوص اہداف حاصل کیے جا سکیں۔ یہ ایجنٹس خود مختار رویہ ظاہر کر سکتے ہیں، فیصلے کر سکتے ہیں، اور بدلتے ہوئے حالات کے مطابق ڈھل سکتے ہیں۔ آئیے AI ایجنٹ فریم ورک کے ذریعے فعال کردہ کچھ کلیدی صلاحیتوں پر نظر ڈالیں:

- **ایجنٹ تعاون اور ہم آہنگی**: متعدد AI ایجنٹس کی تخلیق کو فعال کریں جو ایک ساتھ کام کر سکتے ہیں، بات چیت کر سکتے ہیں، اور پیچیدہ کاموں کو حل کرنے کے لیے ہم آہنگی کر سکتے ہیں۔
- **کام کی خودکاریت اور انتظام**: ملٹی اسٹیپ ورک فلو، کام کی تفویض، اور ایجنٹس کے درمیان متحرک کام کے انتظام کے لیے میکانزم فراہم کریں۔
- **سیاق و سباق کی تفہیم اور موافقت**: ایجنٹس کو سیاق و سباق کو سمجھنے، بدلتے ہوئے ماحول کے مطابق ڈھالنے، اور حقیقی وقت کی معلومات کی بنیاد پر فیصلے کرنے کی صلاحیت سے آراستہ کریں۔

تو خلاصہ یہ ہے کہ ایجنٹس آپ کو زیادہ کرنے کی اجازت دیتے ہیں، خودکاریت کو اگلے درجے تک لے جانے، زیادہ ذہین سسٹمز بنانے کی جو اپنے ماحول سے سیکھ سکتے ہیں اور اس کے مطابق ڈھل سکتے ہیں۔

## ایجنٹ کی صلاحیتوں کو جلدی پروٹوٹائپ، تکرار، اور بہتر بنانے کا طریقہ؟

یہ ایک تیزی سے بدلتا ہوا منظر ہے، لیکن زیادہ تر AI ایجنٹ فریم ورک میں کچھ چیزیں عام ہیں جو آپ کو جلدی پروٹوٹائپ اور تکرار کرنے میں مدد دے سکتی ہیں، یعنی ماڈیول اجزاء، تعاون کے ٹولز، اور حقیقی وقت میں سیکھنا۔ آئیے ان میں گہرائی سے جائیں:

- **ماڈیول اجزاء کا استعمال کریں**: AI SDKs پہلے سے تیار شدہ اجزاء پیش کرتے ہیں جیسے AI اور میموری کنیکٹرز، قدرتی زبان یا کوڈ پلگ انز کا استعمال کرتے ہوئے فنکشن کالنگ، پرومپٹ ٹیمپلیٹس، اور مزید۔
- **تعاون کے ٹولز کا فائدہ اٹھائیں**: مخصوص کرداروں اور کاموں کے ساتھ ایجنٹس کو ڈیزائن کریں، انہیں تعاون کے ورک فلو کو جانچنے اور بہتر بنانے کے قابل بنائیں۔
- **حقیقی وقت میں سیکھیں**: فیڈ بیک لوپس نافذ کریں جہاں ایجنٹس تعاملات سے سیکھیں اور اپنے رویے کو متحرک طور پر ایڈجسٹ کریں۔

### ماڈیول اجزاء کا استعمال کریں

Microsoft Semantic Kernel اور LangChain جیسے SDKs پہلے سے تیار شدہ اجزاء پیش کرتے ہیں جیسے AI کنیکٹرز، پرومپٹ ٹیمپلیٹس، اور میموری مینجمنٹ۔

**ٹیمیں ان کا استعمال کیسے کر سکتی ہیں**: ٹیمیں ان اجزاء کو جلدی سے جمع کر سکتی ہیں تاکہ ایک فعال پروٹوٹائپ بنایا جا سکے بغیر شروع سے شروع کیے، جس سے تیزی سے تجربہ اور تکرار ممکن ہو۔

**یہ عملی طور پر کیسے کام کرتا ہے**: آپ ایک پہلے سے تیار شدہ پارسر کا استعمال کر سکتے ہیں تاکہ صارف کے ان پٹ سے معلومات نکالی جا سکیں، ایک میموری ماڈیول ڈیٹا کو ذخیرہ کرنے اور بازیافت کرنے کے لیے، اور ایک پرومپٹ جنریٹر صارفین کے ساتھ بات چیت کرنے کے لیے، یہ سب بغیر ان اجزاء کو شروع سے بنانے کے۔

**مثال کوڈ**۔ آئیے دیکھتے ہیں کہ آپ Semantic Kernel Python اور .Net کے ساتھ ایک پہلے سے تیار شدہ AI کنیکٹر کا استعمال کیسے کر سکتے ہیں جو صارف کے ان پٹ کا جواب دینے کے لیے آٹو فنکشن کالنگ کا استعمال کرتا ہے:

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

اس مثال سے آپ دیکھ سکتے ہیں کہ آپ صارف کے ان پٹ سے کلیدی معلومات نکالنے کے لیے ایک پہلے سے تیار شدہ پارسر کا فائدہ کیسے اٹھا سکتے ہیں، جیسے کہ فلائٹ بکنگ درخواست کے اصل، منزل، اور تاریخ۔ یہ ماڈیولر طریقہ آپ کو اعلیٰ سطحی منطق پر توجہ مرکوز کرنے کی اجازت دیتا ہے۔

### تعاون کے ٹولز کا فائدہ اٹھائیں

CrewAI, Microsoft AutoGen, اور Semantic Kernel جیسے فریم ورک متعدد ایجنٹس کی تخلیق کو آسان بناتے ہیں جو ایک ساتھ کام کر سکتے ہیں۔

**ٹیمیں ان کا استعمال کیسے کر سکتی ہیں**: ٹیمیں مخصوص کرداروں اور کاموں کے ساتھ ایجنٹس کو ڈیزائن کر سکتی ہیں، انہیں تعاون کے ورک فلو کو جانچنے اور بہتر بنانے اور مجموعی نظام کی کارکردگی کو بہتر بنانے کے قابل بناتی ہیں۔

**یہ عملی طور پر کیسے کام کرتا ہے**: آپ ایجنٹس کی ایک ٹیم بنا سکتے ہیں جہاں ہر ایجنٹ کے پاس ایک مخصوص فنکشن ہو، جیسے ڈیٹا بازیافت، تجزیہ، یا فیصلہ سازی۔ یہ ایجنٹس معلومات کا اشتراک کر سکتے ہیں اور صارف کے سوال کا جواب دینے یا کام مکمل کرنے جیسے مشترکہ مقصد کو حاصل کرنے کے لیے بات چیت کر سکتے ہیں۔

**مثال کوڈ (AutoGen)**:

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

پچھلے کوڈ میں آپ دیکھتے ہیں کہ آپ ایک کام کیسے بنا سکتے ہیں جس میں متعدد ایجنٹس ڈیٹا کا تجزیہ کرنے کے لیے ایک ساتھ کام کرتے ہیں۔ ہر ایجنٹ ایک مخصوص فنکشن انجام دیتا ہے، اور کام مطلوبہ نتیجہ حاصل کرنے کے لیے ایجنٹس کو ہم آہنگ کر کے انجام دیا جاتا ہے۔ مخصوص کرداروں کے ساتھ وقف شدہ ایجنٹس بنا کر، آپ کام کی کارکردگی اور کارکردگی کو بہتر بنا سکتے ہیں۔

### حقیقی وقت میں سیکھیں

جدید فریم ورک حقیقی وقت کے سیاق و سباق کی تفہیم اور موافقت کے لیے صلاحیتیں فراہم کرتے ہیں۔

**ٹیمیں ان کا استعمال کیسے کر سکتی ہیں**: ٹیمیں فیڈ بیک لوپس نافذ کر سکتی ہیں جہاں ایجنٹس تعاملات سے سیکھیں اور اپنے رویے کو متحرک طور پر ایڈجسٹ کریں، جس سے صلاحیتوں کی مسلسل بہتری اور اصلاح ممکن ہو۔

**یہ عملی طور پر کیسے کام کرتا ہے**: ایجنٹس صارف کے فیڈ بیک، ماحولیاتی ڈیٹا، اور کام کے نتائج کا تجزیہ کر سکتے ہیں تاکہ اپنے علم کے ذخیرے کو اپ ڈیٹ کریں، فیصلہ سازی کے الگورتھم کو ایڈجسٹ کریں، اور وقت کے ساتھ کارکردگی کو بہتر بنائیں۔ یہ تکراری سیکھنے کا عمل ایجنٹس کو بدلتے ہوئے حالات اور صارف کی ترجیحات کے مطابق ڈھالنے کے قابل بناتا ہے، مجموعی نظام کی تاثیر کو بڑھاتا ہے۔

## AutoGen, Semantic Kernel اور Azure AI Agent Service کے فریم ورک کے درمیان کیا فرق ہے؟

ان فریم ورک کا موازنہ کرنے کے کئی طریقے ہیں، لیکن آئیے ان کے ڈیزائن، صلاحیتوں، اور ہدف استعمال کے معاملات کے لحاظ سے کچھ اہم فرق دیکھتے ہیں:

## AutoGen

AutoGen Microsoft Research کے AI Frontiers Lab کے ذریعے تیار کردہ ایک اوپن سورس فریم ورک ہے۔ یہ ایونٹ سے چلنے والے، تقسیم شدہ *ایجنٹک* ایپلیکیشنز پر مرکوز ہے، جو متعدد LLMs اور SLMs، ٹولز، اور جدید ملٹی ایجنٹ ڈیزائن پیٹرنز کو فعال کرتا ہے۔

AutoGen ایجنٹس کے بنیادی تصور کے ارد گرد بنایا گیا ہے، جو خود مختار ادارے ہیں جو اپنے ماحول کو محسوس کر سکتے ہیں، فیصلے کر سکتے ہیں، اور مخصوص اہداف حاصل کرنے کے لیے اقدامات کر سکتے ہیں۔ ایجنٹس غیر متزامن پیغامات کے ذریعے بات چیت کرتے ہیں، انہیں آزادانہ طور پر اور متوازی طور پر کام کرنے کی اجازت دیتے ہیں، نظام کی توسیع پذیری اور ردعمل کو بڑھاتے ہیں۔

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">ایجنٹس اداکار ماڈل پر مبنی ہیں</a>۔ ویکیپیڈیا کے مطابق، ایک اداکار _ہم وقت ساز حساب کتاب کا بنیادی تعمیراتی بلاک ہے۔ اسے موصول ہونے والے پیغام کے جواب میں، ایک اداکار مقامی فیصلے کر سکتا ہے، مزید اداکار بنا سکتا ہے، مزید پیغامات بھیج سکتا ہے، اور موصول ہونے والے اگلے پیغام کا جواب دینے کا طریقہ طے کر سکتا ہے_۔

**استعمال کے معاملات**: کوڈ جنریشن، ڈیٹا تجزیہ کے کاموں کو خودکار بنانا، اور منصوبہ بندی اور تحقیقی افعال کے لیے کسٹم ایجنٹس بنانا۔

یہاں AutoGen کے کچھ اہم بنیادی تصورات ہیں:

- **ایجنٹس**۔ ایک ایجنٹ ایک سافٹ ویئر ادارہ ہے جو:
  - **پیغامات کے ذریعے بات چیت کرتا ہے**، یہ پیغامات ہم وقت ساز یا غیر متزامن ہو سکتے ہیں۔
  - **اپنی حالت برقرار رکھتا ہے**، جسے آنے والے پیغامات کے ذریعے تبدیل کیا جا سکتا ہے۔
  - **اقدامات انجام دیتا ہے** موصول ہونے والے پیغامات یا اس کی حالت میں تبدیلیوں کے جواب میں۔ یہ اقدامات ایجنٹ کی حالت کو تبدیل کر سکتے ہیں اور بیرونی اثرات پیدا کر سکتے ہیں، جیسے پیغام لاگز کو اپ ڈیٹ کرنا، نئے پیغامات بھیجنا، کوڈ کو انجام دینا، یا API کالز کرنا۔

  یہاں آپ کے پاس ایک مختصر کوڈ کا ٹکڑا ہے جس میں آپ چیٹ کی صلاحیتوں کے ساتھ اپنا ایجنٹ بناتے ہیں:

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
    
پچھلے کوڈ میں، `MyAgent` بنایا گیا ہے اور `RoutedAgent` سے وراثت حاصل کرتا ہے۔ اس میں ایک پیغام ہینڈلر ہے جو پیغام کے مواد کو پرنٹ کرتا ہے اور پھر `AssistantAgent` ڈیلیگیٹ کا استعمال کرتے ہوئے جواب بھیجتا ہے۔ خاص طور پر نوٹ کریں کہ ہم `self._delegate` کو `AssistantAgent` کی ایک مثال تفویض کرتے ہیں جو ایک پہلے سے تیار شدہ ایجنٹ ہے جو چیٹ مکمل کرنے کو سنبھال سکتا ہے۔

AutoGen کو اس ایجنٹ کی قسم کے بارے میں بتائیں اور پروگرام کو شروع کریں:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

پچھلے کوڈ میں ایجنٹس کو رن ٹائم کے ساتھ رجسٹر کیا گیا ہے اور پھر ایجنٹ کو ایک پیغام بھیجا گیا ہے جس کے نتیجے میں درج ذیل آؤٹ پٹ حاصل ہوتا ہے:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **ملٹی ایجنٹس**۔ AutoGen متعدد ایجنٹس کی تخلیق کی حمایت کرتا ہے جو پیچیدہ کاموں کو حاصل کرنے کے لیے ایک ساتھ کام کر سکتے ہیں۔ ایجنٹس معلومات کا اشتراک کر سکتے ہیں، اور مسائل کو زیادہ مؤثر طریقے سے حل کرنے کے لیے اپنے اعمال کو ہم آہنگ کر سکتے ہیں۔ ایک ملٹی ایجنٹ سسٹم بنانے کے لیے، آپ مختلف قسم کے ایجنٹس کو مخصوص افعال اور کرداروں کے ساتھ بیان کر سکتے ہیں، جیسے ڈیٹا بازیافت، تجزیہ، فیصلہ سازی، اور صارف کے ساتھ بات چیت۔ آئیے دیکھتے ہیں کہ ایسی تخلیق کیسی دکھتی ہے تاکہ ہمیں اس کا اندازہ ہو:

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

پچھلے کوڈ میں ہمارے پاس ایک `GroupChatManager` ہے جو رن ٹائم کے ساتھ رجسٹرڈ ہے۔ یہ مینیجر مختلف قسم کے ایجنٹس، جیسے مصنفین، مصور، ایڈیٹرز، اور صارفین کے درمیان تعاملات کو ہم آہنگ کرنے کا ذمہ دار ہے۔

- **ایجنٹ رن ٹائم**۔ فریم ورک ایک رن ٹائم ماحول فراہم کرتا ہے، ایجنٹس کے درمیان بات چیت کو فعال کرتا ہے، ان کی شناخت اور زندگی کے چکر کو منظم کرتا ہے، اور سیکیورٹی اور پرائیویسی کی حدود کو نافذ کرتا ہے۔ اس کا مطلب یہ ہے کہ آپ اپنے ایجنٹس کو ایک محفوظ اور کنٹرول شدہ ماحول میں چلا سکتے ہیں، اس بات کو یقینی بناتے ہوئے کہ وہ محفوظ طریقے سے اور مؤثر طریقے سے بات چیت کر سکیں۔ دلچسپی کے دو رن ٹائم ہیں:
  - **اسٹینڈ الون رن ٹائم**۔ یہ سنگل پروسیس ایپلیکیشنز کے لیے ایک اچھا انتخاب ہے جہاں تمام ایجنٹس ایک ہی پروگرامنگ زبان میں نافذ کیے گئے ہیں اور ایک ہی پروسیس میں چلتے ہیں۔ اس کے کام کرنے کا ایک خاکہ یہ ہے:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">اسٹینڈ الون رن ٹائم</a>   
ایپلیکیشن اسٹیک

    *ایجنٹس رن ٹائم کے ذریعے پیغامات کے ذریعے بات چیت کرتے ہیں، اور رن ٹائم ایجنٹس کے زندگی کے چکر کو منظم کرتا ہے*

  - **تقسیم شدہ ایجنٹ رن ٹائم**، ملٹی پروسیس ایپلیکیشنز کے لیے موزوں ہے جہاں ایجنٹس مختلف پروگرامنگ زبانوں میں نافذ کیے جا سکتے ہیں اور مختلف مشینوں پر چل رہے ہیں۔ اس کے کام کرنے کا ایک خاکہ یہ ہے:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">تقسیم شدہ رن ٹائم</a>

## Semantic Kernel + ایجنٹ فریم ورک

Semantic Kernel ایک انٹرپرائز کے لیے تیار AI Orchestration SDK ہے۔ اس میں AI اور میموری کنیکٹرز کے ساتھ ایک ایجنٹ فریم ورک شامل ہے۔

آئیے پہلے کچھ بنیادی اجزاء کا احاطہ کریں:

- **AI کنیکٹرز**: یہ بیرونی AI سروسز اور ڈیٹا ذرائع کے ساتھ انٹرفیس ہے جو Python اور C# دونوں میں استعمال کے لیے ہے۔

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


یہ حقائق پھر میموری کلیکشن `SummarizedAzureDocs` میں محفوظ کیے جاتے ہیں۔ یہ ایک بہت ہی سادہ مثال ہے، لیکن آپ دیکھ سکتے ہیں کہ کس طرح معلومات کو LLM کے استعمال کے لیے میموری میں محفوظ کیا جا سکتا ہے۔

تو یہ تھا Semantic Kernel فریم ورک کا بنیادی تعارف، لیکن Agent Framework کے بارے میں کیا خیال ہے؟

## Azure AI Agent Service

Azure AI Agent Service ایک حالیہ اضافہ ہے، جو Microsoft Ignite 2024 میں متعارف کرایا گیا۔ یہ زیادہ لچکدار ماڈلز کے ساتھ AI ایجنٹس کی ترقی اور تعیناتی کی اجازت دیتا ہے، جیسے کہ اوپن سورس LLMs جیسے Llama 3، Mistral، اور Cohere کو براہ راست کال کرنا۔

Azure AI Agent Service مضبوط انٹرپرائز سیکیورٹی میکانزم اور ڈیٹا اسٹوریج کے طریقے فراہم کرتا ہے، جو اسے انٹرپرائز ایپلیکیشنز کے لیے موزوں بناتا ہے۔

یہ سروس AutoGen اور Semantic Kernel جیسے ملٹی ایجنٹ آرکیسٹریشن فریم ورکس کے ساتھ فوری طور پر کام کرتی ہے۔

یہ سروس اس وقت پبلک پریویو میں ہے اور ایجنٹس بنانے کے لیے Python اور C# کو سپورٹ کرتی ہے۔

Semantic Kernel Python کا استعمال کرتے ہوئے، ہم ایک یوزر ڈیفائنڈ پلگ ان کے ساتھ Azure AI Agent بنا سکتے ہیں:

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

### بنیادی تصورات

Azure AI Agent Service کے درج ذیل بنیادی تصورات ہیں:

- **ایجنٹ**۔ Azure AI Agent Service، Azure AI Foundry کے ساتھ انٹیگریٹ کرتا ہے۔ AI Foundry کے اندر، ایک AI ایجنٹ ایک "سمارٹ" مائیکرو سروس کے طور پر کام کرتا ہے جو سوالات کے جوابات دینے (RAG)، اعمال انجام دینے، یا مکمل طور پر ورک فلو کو خودکار کرنے کے لیے استعمال کیا جا سکتا ہے۔ یہ جنریٹو AI ماڈلز کی طاقت کو ان ٹولز کے ساتھ جوڑ کر حاصل کرتا ہے جو اسے حقیقی دنیا کے ڈیٹا سورسز تک رسائی اور تعامل کی اجازت دیتے ہیں۔ یہاں ایک ایجنٹ کی مثال ہے:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    اس مثال میں، ایک ایجنٹ `gpt-4o-mini` ماڈل، `my-agent` نام، اور ہدایات `You are helpful agent` کے ساتھ بنایا گیا ہے۔ ایجنٹ کو کوڈ انٹرپریٹیشن کے کام انجام دینے کے لیے ٹولز اور وسائل سے لیس کیا گیا ہے۔

- **تھریڈ اور پیغامات**۔ تھریڈ ایک اور اہم تصور ہے۔ یہ ایجنٹ اور یوزر کے درمیان گفتگو یا تعامل کی نمائندگی کرتا ہے۔ تھریڈز کو گفتگو کی پیش رفت کو ٹریک کرنے، سیاق و سباق کی معلومات کو محفوظ کرنے، اور تعامل کی حالت کو منظم کرنے کے لیے استعمال کیا جا سکتا ہے۔ یہاں ایک تھریڈ کی مثال ہے:

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

    پچھلے کوڈ میں، ایک تھریڈ بنایا گیا ہے۔ اس کے بعد، تھریڈ کو ایک پیغام بھیجا جاتا ہے۔ `create_and_process_run` کو کال کرکے، ایجنٹ سے کہا جاتا ہے کہ وہ تھریڈ پر کام کرے۔ آخر میں، پیغامات کو ایجنٹ کے جواب کو دیکھنے کے لیے لاگ کیا جاتا ہے۔ پیغامات یوزر اور ایجنٹ کے درمیان گفتگو کی پیش رفت کی نشاندہی کرتے ہیں۔ یہ بھی سمجھنا ضروری ہے کہ پیغامات مختلف اقسام کے ہو سکتے ہیں جیسے کہ متن، تصویر، یا فائل، جو ایجنٹ کے کام کا نتیجہ ہو سکتا ہے، مثلاً ایک تصویر یا متن کا جواب۔ ایک ڈویلپر کے طور پر، آپ اس معلومات کو مزید جواب پر عمل کرنے یا یوزر کو پیش کرنے کے لیے استعمال کر سکتے ہیں۔

- **دیگر AI فریم ورکس کے ساتھ انٹیگریٹ کرتا ہے**۔ Azure AI Agent Service دیگر فریم ورکس جیسے AutoGen اور Semantic Kernel کے ساتھ تعامل کر سکتا ہے، جس کا مطلب ہے کہ آپ اپنی ایپ کا کچھ حصہ ان فریم ورکس میں سے کسی ایک میں بنا سکتے ہیں اور مثال کے طور پر ایجنٹ سروس کو آرکیسٹریٹر کے طور پر استعمال کر سکتے ہیں یا آپ سب کچھ ایجنٹ سروس میں بنا سکتے ہیں۔

**استعمال کے کیسز**: Azure AI Agent Service انٹرپرائز ایپلیکیشنز کے لیے ڈیزائن کیا گیا ہے جنہیں محفوظ، اسکیل ایبل، اور لچکدار AI ایجنٹ کی تعیناتی کی ضرورت ہوتی ہے۔

## ان فریم ورکس میں کیا فرق ہے؟

یہ لگتا ہے کہ ان فریم ورکس میں کافی حد تک اوورلیپ ہے، لیکن ان کے ڈیزائن، صلاحیتوں، اور ہدف کے استعمال کے کیسز کے لحاظ سے کچھ اہم فرق ہیں:

- **AutoGen**: یہ ایک تجرباتی فریم ورک ہے جو ملٹی ایجنٹ سسٹمز پر جدید تحقیق پر مرکوز ہے۔ یہ پیچیدہ ملٹی ایجنٹ سسٹمز کو پروٹوٹائپ اور تجربہ کرنے کے لیے بہترین جگہ ہے۔
- **Semantic Kernel**: یہ انٹرپرائز ایجنٹک ایپلیکیشنز بنانے کے لیے ایک پروڈکشن ریڈی ایجنٹ لائبریری ہے۔ یہ ایونٹ ڈرائیون، ڈسٹریبیوٹڈ ایجنٹک ایپلیکیشنز پر مرکوز ہے، جو متعدد LLMs اور SLMs، ٹولز، اور سنگل/ملٹی ایجنٹ ڈیزائن پیٹرنز کو فعال بناتا ہے۔
- **Azure AI Agent Service**: یہ Azure Foundry میں ایجنٹس کے لیے ایک پلیٹ فارم اور تعیناتی سروس ہے۔ یہ Azure OpenAI، Azure AI Search، Bing Search، اور کوڈ ایکزیکیوشن جیسے Azure Found کے ذریعے سپورٹ شدہ سروسز سے کنیکٹیویٹی بنانے کی پیشکش کرتا ہے۔

اب بھی یقین نہیں کہ کون سا منتخب کریں؟

### استعمال کے کیسز

آئیے کچھ عام استعمال کے کیسز کے ذریعے آپ کی مدد کرنے کی کوشش کرتے ہیں:

> سوال: میں تجربہ کر رہا ہوں، سیکھ رہا ہوں اور پروف آف کانسیپٹ ایجنٹ ایپلیکیشنز بنا رہا ہوں، اور میں جلدی سے تعمیر اور تجربہ کرنا چاہتا ہوں۔
>

> جواب: AutoGen اس منظرنامے کے لیے ایک اچھا انتخاب ہوگا، کیونکہ یہ ایونٹ ڈرائیون، ڈسٹریبیوٹڈ ایجنٹک ایپلیکیشنز پر مرکوز ہے اور جدید ملٹی ایجنٹ ڈیزائن پیٹرنز کو سپورٹ کرتا ہے۔

> سوال: اس استعمال کے کیس کے لیے AutoGen کو Semantic Kernel اور Azure AI Agent Service سے بہتر انتخاب کیا بناتا ہے؟
>
> جواب: AutoGen خاص طور پر ایونٹ ڈرائیون، ڈسٹریبیوٹڈ ایجنٹک ایپلیکیشنز کے لیے ڈیزائن کیا گیا ہے، جو اسے کوڈ جنریشن اور ڈیٹا اینالیسس کے کاموں کو خودکار بنانے کے لیے موزوں بناتا ہے۔ یہ پیچیدہ ملٹی ایجنٹ سسٹمز کو مؤثر طریقے سے بنانے کے لیے ضروری ٹولز اور صلاحیتیں فراہم کرتا ہے۔

> سوال: لگتا ہے کہ Azure AI Agent Service بھی یہاں کام کر سکتا ہے، اس میں کوڈ جنریشن اور مزید کے لیے ٹولز ہیں؟
>
> جواب: جی ہاں، Azure AI Agent Service ایجنٹس کے لیے ایک پلیٹ فارم سروس ہے اور متعدد ماڈلز، Azure AI Search، Bing Search، اور Azure Functions کے لیے بلٹ ان صلاحیتیں شامل کرتا ہے۔ یہ آپ کے ایجنٹس کو Foundry پورٹل میں بنانے اور بڑے پیمانے پر تعینات کرنے کو آسان بناتا ہے۔

> سوال: میں اب بھی الجھن میں ہوں، بس مجھے ایک آپشن دے دیں۔
>
> جواب: ایک بہترین انتخاب یہ ہے کہ آپ اپنی ایپلیکیشن Semantic Kernel میں بنائیں اور پھر اپنے ایجنٹ کو تعینات کرنے کے لیے Azure AI Agent Service کا استعمال کریں۔ یہ طریقہ آپ کو اپنے ایجنٹس کو آسانی سے برقرار رکھنے کی اجازت دیتا ہے جبکہ Semantic Kernel میں ملٹی ایجنٹ سسٹمز بنانے کی طاقت کا فائدہ اٹھاتا ہے۔ اس کے علاوہ، Semantic Kernel میں AutoGen کے لیے ایک کنیکٹر ہے، جو دونوں فریم ورکس کو ایک ساتھ استعمال کرنا آسان بناتا ہے۔

آئیے ایک جدول میں اہم فرق کا خلاصہ کریں:

| فریم ورک | فوکس | بنیادی تصورات | استعمال کے کیسز |
| --- | --- | --- | --- |
| AutoGen | ایونٹ ڈرائیون، ڈسٹریبیوٹڈ ایجنٹک ایپلیکیشنز | ایجنٹس، پرسنز، فنکشنز، ڈیٹا | کوڈ جنریشن، ڈیٹا اینالیسس کے کام |
| Semantic Kernel | انسانی جیسا متن سمجھنا اور تخلیق کرنا | ایجنٹس، ماڈیولر کمپوننٹس، تعاون | نیچرل لینگویج انڈرسٹینڈنگ، مواد کی تخلیق |
| Azure AI Agent Service | لچکدار ماڈلز، انٹرپرائز سیکیورٹی، کوڈ جنریشن، ٹول کالنگ | ماڈیولریٹی، تعاون، پروسیس آرکیسٹریشن | محفوظ، اسکیل ایبل، اور لچکدار AI ایجنٹ کی تعیناتی |

ہر ایک فریم ورک کے لیے مثالی استعمال کا کیس کیا ہے؟

## کیا میں اپنے موجودہ Azure ایکوسسٹم ٹولز کو براہ راست انٹیگریٹ کر سکتا ہوں، یا مجھے اسٹینڈ الون سلوشنز کی ضرورت ہے؟

جواب ہاں میں ہے، آپ اپنے موجودہ Azure ایکوسسٹم ٹولز کو خاص طور پر Azure AI Agent Service کے ساتھ براہ راست انٹیگریٹ کر سکتے ہیں، کیونکہ یہ دیگر Azure سروسز کے ساتھ بغیر کسی رکاوٹ کے کام کرنے کے لیے بنایا گیا ہے۔ آپ مثال کے طور پر Bing، Azure AI Search، اور Azure Functions کو انٹیگریٹ کر سکتے ہیں۔ Azure AI Foundry کے ساتھ بھی گہری انٹیگریشن موجود ہے۔

AutoGen اور Semantic Kernel کے لیے، آپ Azure سروسز کے ساتھ انٹیگریٹ کر سکتے ہیں، لیکن اس کے لیے آپ کو اپنے کوڈ سے Azure سروسز کو کال کرنے کی ضرورت ہو سکتی ہے۔ انٹیگریٹ کرنے کا ایک اور طریقہ یہ ہے کہ Azure SDKs کا استعمال کرتے ہوئے اپنے ایجنٹس سے Azure سروسز کے ساتھ تعامل کریں۔ اس کے علاوہ، جیسا کہ ذکر کیا گیا، آپ Azure AI Agent Service کو AutoGen یا Semantic Kernel میں بنائے گئے ایجنٹس کے لیے آرکیسٹریٹر کے طور پر استعمال کر سکتے ہیں، جو Azure ایکوسسٹم تک آسان رسائی فراہم کرے گا۔

## نمونہ کوڈز

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI Agent Frameworks کے بارے میں مزید سوالات ہیں؟

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) میں شامل ہوں تاکہ دیگر سیکھنے والوں سے ملاقات کریں، آفس آورز میں شرکت کریں اور اپنے AI ایجنٹس کے سوالات کے جوابات حاصل کریں۔

## حوالہ جات

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel اور AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">AutoGen / Semantic Kernel کے ساتھ Azure AI Agent Service کا استعمال کرتے ہوئے ملٹی ایجنٹ کا حل بنانا</a>

## پچھلا سبق

[AI ایجنٹس اور ان کے استعمال کے کیسز کا تعارف](../01-intro-to-ai-agents/README.md)

## اگلا سبق

[ایجنٹک ڈیزائن پیٹرنز کو سمجھنا](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->