<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86b9c2b24da3b3e61711182ffa72601c",
  "translation_date": "2025-09-29T22:13:14+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "mr"
}
-->
[![AI एजंट फ्रेमवर्क्सचा अभ्यास](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.mr.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(वरील प्रतिमेवर क्लिक करून या धड्याचा व्हिडिओ पहा)_

# AI एजंट फ्रेमवर्क्सचा अभ्यास करा

AI एजंट फ्रेमवर्क्स हे सॉफ्टवेअर प्लॅटफॉर्म आहेत जे AI एजंट्स तयार करणे, तैनात करणे आणि व्यवस्थापित करणे सुलभ करतात. हे फ्रेमवर्क्स विकसकांना पूर्व-निर्मित घटक, संकल्पना आणि साधने प्रदान करतात ज्यामुळे जटिल AI प्रणालींच्या विकासाची प्रक्रिया सुलभ होते.

हे फ्रेमवर्क्स AI एजंट विकासातील सामान्य आव्हानांसाठी मानकीकृत दृष्टिकोन प्रदान करून विकसकांना त्यांच्या अनुप्रयोगांच्या अनन्य पैलूंवर लक्ष केंद्रित करण्यास मदत करतात. ते AI प्रणाली तयार करण्यामध्ये स्केलेबिलिटी, प्रवेशयोग्यता आणि कार्यक्षमता वाढवतात.

## परिचय

या धड्यात आपण शिकणार आहोत:

- AI एजंट फ्रेमवर्क्स म्हणजे काय आणि ते विकसकांना काय साध्य करण्यास सक्षम करतात?
- संघ हे फ्रेमवर्क्स कसे वापरून जलद प्रोटोटाइप तयार करू शकतात, पुनरावृत्ती करू शकतात आणि त्यांच्या एजंटच्या क्षमता सुधारू शकतात?
- Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, आणि <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> द्वारे तयार केलेल्या फ्रेमवर्क्स आणि साधनांमध्ये काय फरक आहे?
- मी माझ्या विद्यमान Azure इकोसिस्टम साधनांना थेट समाकलित करू शकतो का, किंवा मला स्वतंत्र उपायांची आवश्यकता आहे?
- Azure AI Agents सेवा म्हणजे काय आणि ती मला कशी मदत करते?

## शिकण्याची उद्दिष्टे

या धड्याचे उद्दिष्टे तुम्हाला समजून घेण्यास मदत करणे आहेत:

- AI विकासामध्ये AI एजंट फ्रेमवर्क्सची भूमिका.
- बुद्धिमान एजंट्स तयार करण्यासाठी AI एजंट फ्रेमवर्क्सचा कसा उपयोग करावा.
- AI एजंट फ्रेमवर्क्सद्वारे सक्षम केलेल्या प्रमुख क्षमता.
- AutoGen, Semantic Kernel, आणि Azure AI Agent Service यामधील फरक.

## AI एजंट फ्रेमवर्क्स म्हणजे काय आणि ते विकसकांना काय साध्य करण्यास सक्षम करतात?

पारंपरिक AI फ्रेमवर्क्स तुमच्या अॅप्समध्ये AI समाकलित करण्यात आणि खालील प्रकारे अॅप्स सुधारण्यात मदत करू शकतात:

- **वैयक्तिकरण**: AI वापरकर्त्याच्या वर्तनाचा आणि प्राधान्यांचा विश्लेषण करून वैयक्तिकृत शिफारसी, सामग्री आणि अनुभव प्रदान करू शकते.
उदाहरण: Netflix सारख्या स्ट्रीमिंग सेवांचा वापरकर्ता इतिहासावर आधारित चित्रपट आणि शो सुचवण्यासाठी AI वापर केला जातो, ज्यामुळे वापरकर्ता सहभाग आणि समाधान वाढते.
- **स्वयंचलन आणि कार्यक्षमता**: AI पुनरावृत्ती होणाऱ्या कार्यांना स्वयंचलित करू शकते, कार्यप्रवाह सुलभ करू शकते आणि कार्यक्षमता सुधारू शकते.
उदाहरण: ग्राहक सेवा अॅप्स सामान्य चौकशी हाताळण्यासाठी AI-सक्षम चॅटबॉट्स वापरतात, प्रतिसाद वेळ कमी करतात आणि अधिक जटिल समस्यांसाठी मानवी एजंट्ससाठी वेळ मोकळा करतात.
- **वाढलेला वापरकर्ता अनुभव**: AI आवाज ओळख, नैसर्गिक भाषा प्रक्रिया आणि प्रेडिक्टिव्ह टेक्स्ट यासारख्या बुद्धिमान वैशिष्ट्ये प्रदान करून एकूण वापरकर्ता अनुभव सुधारू शकतो.
उदाहरण: Siri आणि Google Assistant सारखे व्हर्च्युअल सहाय्यक AI वापरून आवाज आदेश समजून घेतात आणि प्रतिसाद देतात, ज्यामुळे वापरकर्त्यांना त्यांच्या उपकरणांशी संवाद साधणे सोपे होते.

### हे सर्व खूप चांगले वाटते, मग AI एजंट फ्रेमवर्कची गरज का आहे?

AI एजंट फ्रेमवर्क्स हे फक्त AI फ्रेमवर्क्सपेक्षा अधिक काहीतरी दर्शवतात. ते बुद्धिमान एजंट्स तयार करण्यासाठी डिझाइन केले आहेत जे वापरकर्त्यांसोबत, इतर एजंट्ससोबत आणि विशिष्ट उद्दिष्टे साध्य करण्यासाठी वातावरणाशी संवाद साधू शकतात. हे एजंट्स स्वायत्त वर्तन प्रदर्शित करू शकतात, निर्णय घेऊ शकतात आणि बदलत्या परिस्थितीशी जुळवून घेऊ शकतात. चला AI एजंट फ्रेमवर्क्सद्वारे सक्षम केलेल्या काही प्रमुख क्षमतांकडे पाहूया:

- **एजंट्समधील सहकार्य आणि समन्वय**: अनेक AI एजंट्स तयार करण्यास सक्षम करा जे एकत्र काम करू शकतात, संवाद साधू शकतात आणि जटिल कार्ये सोडवण्यासाठी समन्वय साधू शकतात.
- **कार्य स्वयंचलन आणि व्यवस्थापन**: मल्टी-स्टेप कार्यप्रवाह, कार्य प्रतिनिधीकरण आणि एजंट्समधील गतिशील कार्य व्यवस्थापनासाठी यंत्रणा प्रदान करा.
- **संदर्भात्मक समज आणि अनुकूलन**: एजंट्सना संदर्भ समजून घेण्याची, बदलत्या वातावरणाशी जुळवून घेण्याची आणि रिअल-टाइम माहितीच्या आधारे निर्णय घेण्याची क्षमता प्रदान करा.

तर सारांश, एजंट्स तुम्हाला अधिक करण्यास अनुमती देतात, स्वयंचलन पुढील स्तरावर नेण्यासाठी, अधिक बुद्धिमान प्रणाली तयार करण्यासाठी जे त्यांच्या वातावरणातून जुळवून घेऊ शकतात आणि शिकू शकतात.

## एजंटच्या क्षमतांना जलद प्रोटोटाइप, पुनरावृत्ती आणि सुधारणा कशी करावी?

हे एक जलद बदलणारे क्षेत्र आहे, परंतु बहुतेक AI एजंट फ्रेमवर्क्समध्ये काही सामान्य गोष्टी आहेत ज्या तुम्हाला जलद प्रोटोटाइप तयार करण्यात आणि पुनरावृत्ती करण्यात मदत करू शकतात, म्हणजे मॉड्यूलर घटक, सहकारी साधने आणि रिअल-टाइम शिक्षण. चला यावर सविस्तर चर्चा करूया:

- **मॉड्यूलर घटक वापरा**: AI SDKs पूर्व-निर्मित घटक ऑफर करतात जसे की AI आणि मेमरी कनेक्टर्स, नैसर्गिक भाषेचा वापर करून फंक्शन कॉलिंग किंवा कोड प्लगइन्स, प्रॉम्प्ट टेम्पलेट्स आणि बरेच काही.
- **सहकारी साधनांचा लाभ घ्या**: विशिष्ट भूमिका आणि कार्यांसह एजंट्स डिझाइन करा, त्यांना सहकारी कार्यप्रवाह चाचणी आणि सुधारण्यासाठी सक्षम करा.
- **रिअल-टाइममध्ये शिका**: अभिप्राय लूप्स अंमलात आणा जिथे एजंट्स संवादांमधून शिकतात आणि त्यांचे वर्तन गतिशीलपणे समायोजित करतात.

### मॉड्यूलर घटक वापरा

Microsoft Semantic Kernel आणि LangChain सारखे SDKs पूर्व-निर्मित घटक ऑफर करतात जसे की AI कनेक्टर्स, प्रॉम्प्ट टेम्पलेट्स आणि मेमरी व्यवस्थापन.

**संघ हे कसे वापरू शकतात**: संघ हे घटक जलद कार्यशील प्रोटोटाइप तयार करण्यासाठी एकत्र करू शकतात, ज्यामुळे जलद प्रयोग आणि पुनरावृत्ती शक्य होते.

**हे प्रत्यक्षात कसे कार्य करते**: तुम्ही वापरकर्त्याच्या इनपुटमधून माहिती काढण्यासाठी पूर्व-निर्मित पार्सर, डेटा संग्रहित आणि पुनर्प्राप्त करण्यासाठी मेमरी मॉड्यूल आणि वापरकर्त्यांसोबत संवाद साधण्यासाठी प्रॉम्प्ट जनरेटर वापरू शकता, हे घटक स्क्रॅचपासून तयार न करता.

**उदाहरण कोड**. चला Semantic Kernel Python आणि .Net सह पूर्व-निर्मित AI कनेक्टर वापरण्याचे उदाहरण पाहूया जे ऑटो-फंक्शन कॉलिंग वापरते जेणेकरून मॉडेल वापरकर्त्याच्या इनपुटला प्रतिसाद देऊ शकेल:

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

या उदाहरणातून तुम्ही पाहू शकता की वापरकर्त्याच्या इनपुटमधून महत्त्वाची माहिती काढण्यासाठी पूर्व-निर्मित पार्सरचा कसा उपयोग करता येतो, जसे की फ्लाइट बुकिंग विनंतीचा मूळ, गंतव्य आणि तारीख. हा मॉड्यूलर दृष्टिकोन तुम्हाला उच्च-स्तरीय लॉजिकवर लक्ष केंद्रित करण्यास अनुमती देतो.

### सहकारी साधनांचा लाभ घ्या

CrewAI, Microsoft AutoGen, आणि Semantic Kernel सारख्या फ्रेमवर्क्स अनेक एजंट्स तयार करण्यास सुलभ करतात जे एकत्र काम करू शकतात.

**संघ हे कसे वापरू शकतात**: संघ विशिष्ट भूमिका आणि कार्यांसह एजंट्स डिझाइन करू शकतात, त्यांना सहकारी कार्यप्रवाह चाचणी आणि सुधारण्यासाठी सक्षम करू शकतात आणि एकूण प्रणाली कार्यक्षमता सुधारू शकतात.

**हे प्रत्यक्षात कसे कार्य करते**: तुम्ही एजंट्सची एक टीम तयार करू शकता जिथे प्रत्येक एजंटची विशेष कार्ये असतात, जसे की डेटा पुनर्प्राप्ती, विश्लेषण किंवा निर्णय घेणे. हे एजंट्स संवाद साधू शकतात आणि माहिती सामायिक करू शकतात जेणेकरून वापरकर्त्याच्या चौकशीला उत्तर देणे किंवा कार्य पूर्ण करणे यासारखे सामान्य उद्दिष्ट साध्य करता येईल.

**उदाहरण कोड (AutoGen)**:

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

मागील कोडमध्ये तुम्ही पाहू शकता की डेटा विश्लेषणासाठी अनेक एजंट्स एकत्र काम करत आहेत. प्रत्येक एजंट विशिष्ट कार्य करतो आणि एजंट्स समन्वय साधून कार्य पूर्ण करतात. समर्पित एजंट्स तयार करून कार्यक्षमता आणि कार्यप्रदर्शन सुधारता येते.

### रिअल-टाइममध्ये शिका

प्रगत फ्रेमवर्क्स रिअल-टाइम संदर्भ समज आणि अनुकूलनासाठी क्षमता प्रदान करतात.

**संघ हे कसे वापरू शकतात**: संघ अभिप्राय लूप्स अंमलात आणू शकतात जिथे एजंट्स संवादांमधून शिकतात आणि त्यांचे वर्तन गतिशीलपणे समायोजित करतात, ज्यामुळे क्षमतांची सतत सुधारणा आणि परिष्करण होते.

**हे प्रत्यक्षात कसे कार्य करते**: एजंट्स वापरकर्त्याच्या अभिप्राय, पर्यावरणीय डेटा आणि कार्य परिणामांचे विश्लेषण करू शकतात जेणेकरून त्यांचे ज्ञान अद्यतनित करता येईल, निर्णय घेण्याचे अल्गोरिदम समायोजित करता येतील आणि कार्यप्रदर्शन सुधारता येईल. ही पुनरावृत्ती शिकण्याची प्रक्रिया एजंट्सना बदलत्या परिस्थिती आणि वापरकर्त्याच्या प्राधान्यांशी जुळवून घेण्यास सक्षम करते, एकूण प्रणाली प्रभावीपणा वाढवते.

## AutoGen, Semantic Kernel आणि Azure AI Agent Service यामधील फ्रेमवर्क्सचे फरक काय आहेत?

या फ्रेमवर्क्सची तुलना करण्याचे अनेक मार्ग आहेत, परंतु त्यांच्या डिझाइन, क्षमता आणि लक्ष्यित उपयोग प्रकरणांच्या दृष्टीने काही प्रमुख फरक पाहूया:

## AutoGen

AutoGen हे Microsoft Research च्या AI Frontiers Lab द्वारे विकसित केलेले एक ओपन-सोर्स फ्रेमवर्क आहे. हे इव्हेंट-ड्रिव्हन, वितरित *agentic* अनुप्रयोगांवर लक्ष केंद्रित करते, अनेक LLMs आणि SLMs, साधने आणि प्रगत मल्टी-एजंट डिझाइन पॅटर्न सक्षम करते.

AutoGen एजंट्सच्या मुख्य संकल्पनेवर आधारित आहे, जे स्वायत्त घटक आहेत जे त्यांच्या वातावरणाचे आकलन करू शकतात, निर्णय घेऊ शकतात आणि विशिष्ट उद्दिष्टे साध्य करण्यासाठी कृती करू शकतात. एजंट्स असिंक्रोनस संदेशांद्वारे संवाद साधतात, ज्यामुळे ते स्वतंत्रपणे आणि समांतरपणे कार्य करू शकतात, प्रणालीची स्केलेबिलिटी आणि प्रतिसादक्षमता वाढवतात.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">एजंट्स अभिनेता मॉडेलवर आधारित आहेत</a>. Wikipedia नुसार, अभिनेता _सहकार्यात्मक संगणनाचा मूलभूत घटक आहे. प्राप्त झालेल्या संदेशाला प्रतिसाद म्हणून, अभिनेता स्थानिक निर्णय घेऊ शकतो, अधिक अभिनेता तयार करू शकतो, अधिक संदेश पाठवू शकतो आणि प्राप्त झालेल्या पुढील संदेशाला कसे प्रतिसाद द्यायचे ते ठरवू शकतो_.

**उपयोग प्रकरणे**: कोड जनरेशन स्वयंचलित करणे, डेटा विश्लेषण कार्ये आणि नियोजन आणि संशोधन कार्यांसाठी सानुकूल एजंट्स तयार करणे.

AutoGen चे काही महत्त्वाचे मुख्य संकल्पना येथे आहेत:

- **एजंट्स**. एजंट म्हणजे एक सॉफ्टवेअर घटक जो:
  - **संदेशांद्वारे संवाद साधतो**, हे संदेश समकालीन किंवा असिंक्रोनस असू शकतात.
  - **स्वतःची स्थिती राखतो**, जी येणाऱ्या संदेशांद्वारे बदलली जाऊ शकते.
  - **कृती करतो** प्राप्त झालेल्या संदेशांना किंवा त्याच्या स्थितीतील बदलांना प्रतिसाद म्हणून. या कृती एजंटची स्थिती बदलू शकतात आणि बाह्य परिणाम निर्माण करू शकतात, जसे की संदेश लॉग अद्यतनित करणे, नवीन संदेश पाठवणे, कोड अंमलात आणणे किंवा API कॉल करणे.

  येथे तुम्ही चॅट क्षमतांसह तुमचा स्वतःचा एजंट तयार करण्याचा एक छोटा कोड स्निपेट आहे:

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
    
    मागील कोडमध्ये, `MyAgent` तयार केला गेला आहे आणि `RoutedAgent` कडून वारसा घेतला आहे. यात एक संदेश हँडलर आहे जो संदेशाची सामग्री प्रिंट करतो आणि नंतर `AssistantAgent` प्रतिनिधी वापरून प्रतिसाद पाठवतो. विशेषतः लक्षात घ्या की आम्ही `self._delegate` ला `AssistantAgent` ची एक उदाहरणे नियुक्त करतो जी एक पूर्व-निर्मित एजंट आहे जो चॅट पूर्णता हाताळू शकतो.

    AutoGen ला या एजंट प्रकाराबद्दल माहिती देऊया आणि प्रोग्राम सुरू करूया:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    मागील कोडमध्ये एजंट्स रनटाइमसह नोंदणीकृत आहेत आणि नंतर एजंटला एक संदेश पाठवला जातो ज्यामुळे खालील आउटपुट मिळतो:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **मल्टी एजंट्स**. AutoGen अनेक एजंट्स तयार करण्यास समर्थन देते जे जटिल कार्ये साध्य करण्यासाठी एकत्र काम करू शकतात. एजंट्स संवाद साधू शकतात, माहिती सामायिक करू शकतात आणि समस्यांचे अधिक कार्यक्षमतेने निराकरण करण्यासाठी त्यांच्या कृतींचे समन्वय साधू शकतात. मल्टी-एजंट प्रणाली तयार करण्यासाठी, तुम्ही डेटा पुनर्प्राप्ती, विश्लेषण, निर्णय घेणे आणि वापरकर्ता संवाद यासारख्या विशेष कार्ये आणि भूमिका असलेल्या एजंट्सचे वेगवेगळे प्रकार परिभाषित करू शकता. अशा निर्मितीचे स्वरूप कसे आहे ते पाहूया:

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

    मागील कोडमध्ये आमच्याकडे `GroupChatManager` आहे जो रनटाइमसह नोंदणीकृत आहे. हा व्यवस्थापक लेखक, चित्रकार, संपादक आणि वापरकर्ते यासारख्या वेगवेगळ्या प्रकारच्या एजंट्समधील संवादांचे समन्वय साधण्यास जबाबदार आहे.

- **एजंट रनटाइम**. फ्रेमवर्क रनटाइम वातावरण प्रदान करते, एजंट्समधील संवाद सक्षम करते, त्यांची ओळख आणि जीवनचक्र व्यवस्थापित करते आणि सुरक्षा आणि गोपनीयता मर्यादा लागू करते. याचा अर्थ असा की तुम्ही तुमचे एजंट्स सुरक्षित आणि नियंत्रित वातावरणात चालवू शकता, हे सुनिश्चित करून की ते सुरक्षितपणे आणि कार्यक्षमतेने संवाद साधू शकतात. येथे दोन रनटाइम्स आहेत:
  - **स्टँड-अलोन रनटाइम**. हे एकल-प्रक्रिया अनुप्रयोगांसाठी एक चांगला पर्याय आहे जिथे सर्व एजंट्स समान प्रोग्रामिंग भाषेत अंमलात आणले जातात आणि समान प्रक्रियेत चालतात. हे कसे कार्य करते याचे चित्रण येथे आहे:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">स्टँड-अलोन रनटाइम</a>   
अॅप्लिकेशन स्टॅक

    *एजंट्स रनटाइमद्वारे संदेशांद्वारे संवाद साधतात आणि रनटाइम एजंट्सचे जीवनचक्र व्यवस्थापित करते*

  - **वितरित एजंट रनटाइम**, हे मल्टी-प्रक्रिया अनुप्रयोगांसाठी योग्य आहे जिथे एजंट्स वेगवेगळ्या प्रोग्रामिंग भाषांमध्ये अंमलात आणले जाऊ शकतात आणि वेगवेगळ्या मशीनवर चालू शकतात. हे कसे कार्य करते याचे चित्रण येथे आहे:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">वितरित रनटाइम</a>

## Semantic Kernel + Agent Framework

Semantic Kernel हे एंटरप्राइझ-रेडी AI ऑर्केस्ट्रेशन SDK आहे. यात AI आणि मेमरी कनेक्टर्ससह एजंट फ्रेमवर्क आहे.

चला काही मुख्य घटकांवर प्रथम चर्चा करूया:

- **AI कनेक्टर्स**: Python
ही तथ्ये नंतर `SummarizedAzureDocs` या मेमरी संग्रहात संग्रहित केली जातात. हे एक अतिशय सोपे उदाहरण आहे, पण तुम्ही पाहू शकता की LLM साठी माहिती मेमरीमध्ये कशी संग्रहित करता येते.

तर हे Semantic Kernel फ्रेमवर्कचे मूलभूत ज्ञान आहे, पण Agent Framework बद्दल काय?

## Azure AI Agent Service

Azure AI Agent Service ही एक अलीकडील भर आहे, जी Microsoft Ignite 2024 मध्ये सादर केली गेली. हे AI एजंट्स विकसित आणि तैनात करण्यासाठी अधिक लवचिक मॉडेल्ससह, जसे की Llama 3, Mistral, आणि Cohere सारख्या ओपन-सोर्स LLMs थेट कॉल करण्याची परवानगी देते.

Azure AI Agent Service मजबूत एंटरप्राइझ सुरक्षा यंत्रणा आणि डेटा संग्रहण पद्धती प्रदान करते, ज्यामुळे ते एंटरप्राइझ अनुप्रयोगांसाठी योग्य बनते.

हे AutoGen आणि Semantic Kernel सारख्या मल्टी-एजंट ऑर्केस्ट्रेशन फ्रेमवर्कसह सहज कार्य करते.

ही सेवा सध्या Public Preview मध्ये आहे आणि एजंट्स तयार करण्यासाठी Python आणि C# ला समर्थन देते.

Semantic Kernel Python वापरून, आपण वापरकर्त्याने परिभाषित केलेल्या प्लगइनसह Azure AI Agent तयार करू शकतो:

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

### मुख्य संकल्पना

Azure AI Agent Service मध्ये खालील मुख्य संकल्पना आहेत:

- **Agent**. Azure AI Agent Service Azure AI Foundry सह एकत्रित होते. AI Foundry मध्ये, AI Agent एक "स्मार्ट" मायक्रोसर्व्हिस म्हणून कार्य करते जी प्रश्नांची उत्तरे देण्यासाठी (RAG), क्रिया करण्यासाठी किंवा वर्कफ्लो पूर्णपणे स्वयंचलित करण्यासाठी वापरली जाऊ शकते. हे जनरेटिव्ह AI मॉडेल्सची शक्ती आणि वास्तविक-जगातील डेटा स्रोतांशी संवाद साधण्याची परवानगी देणारी साधने एकत्र करून साध्य करते. येथे एजंटचे एक उदाहरण आहे:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    या उदाहरणात, `gpt-4o-mini` मॉडेलसह, `my-agent` नावाने आणि `You are helpful agent` सूचनांसह एक एजंट तयार केला जातो. एजंट कोड इंटरप्रिटेशन कार्ये करण्यासाठी साधने आणि संसाधने सुसज्ज आहे.

- **Thread आणि Messages**. थ्रेड ही आणखी एक महत्त्वाची संकल्पना आहे. हे एजंट आणि वापरकर्त्यादरम्यान संभाषण किंवा संवादाचे प्रतिनिधित्व करते. थ्रेड्स संभाषणाची प्रगती ट्रॅक करण्यासाठी, संदर्भ माहिती संग्रहित करण्यासाठी आणि संवादाची स्थिती व्यवस्थापित करण्यासाठी वापरली जाऊ शकते. येथे थ्रेडचे एक उदाहरण आहे:

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

    मागील कोडमध्ये, एक थ्रेड तयार केला जातो. त्यानंतर, थ्रेडला एक संदेश पाठवला जातो. `create_and_process_run` कॉल करून, एजंटला थ्रेडवर काम करण्यास सांगितले जाते. शेवटी, संदेश प्राप्त केले जातात आणि एजंटच्या प्रतिसादाचे लॉगिंग केले जाते. संदेश वापरकर्ता आणि एजंटमधील संभाषणाची प्रगती दर्शवतात. हे देखील महत्त्वाचे आहे की संदेश वेगवेगळ्या प्रकारचे असू शकतात जसे की मजकूर, प्रतिमा किंवा फाइल, म्हणजे एजंटचे कार्य उदाहरणार्थ प्रतिमा किंवा मजकूर प्रतिसादात परिणत झाले आहे. एक विकसक म्हणून, तुम्ही नंतर या माहितीचा वापर प्रतिसाद पुढे प्रक्रिया करण्यासाठी किंवा वापरकर्त्याला सादर करण्यासाठी करू शकता.

- **इतर AI फ्रेमवर्कसह एकत्रित होते**. Azure AI Agent Service AutoGen आणि Semantic Kernel सारख्या इतर फ्रेमवर्कसह संवाद साधू शकते, म्हणजे तुम्ही तुमच्या अॅपचा काही भाग या फ्रेमवर्कपैकी एकामध्ये तयार करू शकता आणि उदाहरणार्थ Agent Service ऑर्केस्ट्रेटर म्हणून वापरू शकता किंवा तुम्ही सर्वकाही Agent Service मध्ये तयार करू शकता.

**वापर प्रकरणे**: Azure AI Agent Service सुरक्षित, स्केलेबल आणि लवचिक AI एजंट तैनातीसाठी डिझाइन केले आहे.

## या फ्रेमवर्क्समध्ये काय फरक आहे?

हे खूप समान वाटत असले तरी, या फ्रेमवर्क्सच्या डिझाइन, क्षमता आणि लक्ष्यित वापर प्रकरणांमध्ये काही महत्त्वाचे फरक आहेत:

- **AutoGen**: मल्टी-एजंट सिस्टम्सवरील अत्याधुनिक संशोधनावर लक्ष केंद्रित करणारे एक प्रयोगात्मक फ्रेमवर्क आहे. जटिल मल्टी-एजंट सिस्टम्सची प्रोटोटाइप तयार करण्यासाठी आणि प्रयोग करण्यासाठी सर्वोत्तम जागा आहे.
- **Semantic Kernel**: एंटरप्राइझ एजंटिक अनुप्रयोग तयार करण्यासाठी उत्पादन-तयार एजंट लायब्ररी आहे. इव्हेंट-ड्रिव्हन, वितरित एजंटिक अनुप्रयोगांवर लक्ष केंद्रित करते, अनेक LLMs आणि SLMs, साधने आणि सिंगल/मल्टी-एजंट डिझाइन पॅटर्न सक्षम करते.
- **Azure AI Agent Service**: Azure Foundry मधील एजंट्ससाठी एक प्लॅटफॉर्म आणि तैनाती सेवा आहे. Azure OpenAI, Azure AI Search, Bing Search आणि कोड कार्यान्वयनास समर्थन देणाऱ्या सेवांशी कनेक्टिव्हिटी तयार करण्याची ऑफर देते.

तुम्हाला अजूनही कोणते निवडायचे ते समजत नसेल?

### वापर प्रकरणे

चला काही सामान्य वापर प्रकरणांमधून जाऊन तुम्हाला मदत करूया:

> Q: मी प्रयोग करत आहे, शिकत आहे आणि प्रूफ-ऑफ-कॉन्सेप्ट एजंट अनुप्रयोग तयार करत आहे, आणि मला जलदपणे तयार करणे आणि प्रयोग करणे शक्य व्हावे असे वाटते
>

>A: AutoGen या परिस्थितीसाठी चांगला पर्याय असेल, कारण ते इव्हेंट-ड्रिव्हन, वितरित एजंटिक अनुप्रयोगांवर लक्ष केंद्रित करते आणि प्रगत मल्टी-एजंट डिझाइन पॅटर्नला समर्थन देते.

> Q: AutoGen Semantic Kernel आणि Azure AI Agent Service पेक्षा या वापर प्रकरणासाठी चांगला पर्याय का आहे?
>
> A: AutoGen विशेषतः इव्हेंट-ड्रिव्हन, वितरित एजंटिक अनुप्रयोगांसाठी डिझाइन केले आहे, ज्यामुळे कोड जनरेशन आणि डेटा विश्लेषण कार्ये स्वयंचलित करण्यासाठी ते चांगले अनुकूल आहे. जटिल मल्टी-एजंट सिस्टम्स कार्यक्षमतेने तयार करण्यासाठी आवश्यक साधने आणि क्षमता प्रदान करते.

>Q: Azure AI Agent Service येथे देखील कार्य करू शकते, त्यात कोड जनरेशन आणि अधिकसाठी साधने आहेत?

>
> A: होय, Azure AI Agent Service एजंट्ससाठी एक प्लॅटफॉर्म सेवा आहे आणि अनेक मॉडेल्स, Azure AI Search, Bing Search आणि Azure Functions साठी अंगभूत क्षमता जोडते. Foundry Portal मध्ये तुमचे एजंट्स तयार करणे आणि मोठ्या प्रमाणावर तैनात करणे सोपे बनवते.

> Q: मला अजूनही गोंधळ आहे, फक्त एक पर्याय सांगा
>
> A: एक उत्तम पर्याय म्हणजे तुमचा अनुप्रयोग प्रथम Semantic Kernel मध्ये तयार करणे आणि नंतर तुमचा एजंट तैनात करण्यासाठी Azure AI Agent Service वापरणे. या दृष्टिकोनामुळे तुम्हाला तुमचे एजंट्स सहजपणे टिकवता येतील आणि Semantic Kernel मध्ये मल्टी-एजंट सिस्टम्स तयार करण्याची शक्ती मिळेल. याशिवाय, Semantic Kernel मध्ये AutoGen मध्ये कनेक्टर आहे, ज्यामुळे दोन्ही फ्रेमवर्क्स एकत्र वापरणे सोपे होते.

चला मुख्य फरक एका तक्त्यात संक्षेप करूया:

| फ्रेमवर्क | लक्ष केंद्रित | मुख्य संकल्पना | वापर प्रकरणे |
| --- | --- | --- | --- |
| AutoGen | इव्हेंट-ड्रिव्हन, वितरित एजंटिक अनुप्रयोग | एजंट्स, पर्सोनाज, फंक्शन्स, डेटा | कोड जनरेशन, डेटा विश्लेषण कार्ये |
| Semantic Kernel | मानवीसारखे मजकूर सामग्री समजून घेणे आणि तयार करणे | एजंट्स, मॉड्युलर घटक, सहयोग | नैसर्गिक भाषा समजून घेणे, सामग्री निर्मिती |
| Azure AI Agent Service | लवचिक मॉडेल्स, एंटरप्राइझ सुरक्षा, कोड जनरेशन, टूल कॉलिंग | मॉड्युलरिटी, सहयोग, प्रक्रिया ऑर्केस्ट्रेशन | सुरक्षित, स्केलेबल, आणि लवचिक AI एजंट तैनाती |

प्रत्येक फ्रेमवर्कसाठी आदर्श वापर प्रकरण काय आहे?

## मी माझ्या विद्यमान Azure इकोसिस्टम टूल्स थेट एकत्र करू शकतो का, किंवा मला स्वतंत्र सोल्यूशन्सची आवश्यकता आहे?

उत्तर होय आहे, तुम्ही Azure AI Agent Service सह तुमच्या विद्यमान Azure इकोसिस्टम टूल्स थेट एकत्र करू शकता, विशेषतः कारण ते इतर Azure सेवांसह सहजपणे कार्य करण्यासाठी तयार केले गेले आहे. उदाहरणार्थ, तुम्ही Bing, Azure AI Search, आणि Azure Functions एकत्र करू शकता. Azure AI Foundry सह सखोल एकत्रीकरण देखील आहे.

AutoGen आणि Semantic Kernel साठी, तुम्ही Azure सेवांसह देखील एकत्र करू शकता, परंतु तुम्हाला तुमच्या कोडमधून Azure सेवांना कॉल करावे लागेल. एकत्रीकरणाचा आणखी एक मार्ग म्हणजे Azure SDKs वापरून तुमच्या एजंट्समधून Azure सेवांशी संवाद साधणे. याशिवाय, जसे नमूद केले गेले, तुम्ही AutoGen किंवा Semantic Kernel मध्ये तयार केलेल्या एजंट्ससाठी ऑर्केस्ट्रेटर म्हणून Azure AI Agent Service वापरू शकता, ज्यामुळे Azure इकोसिस्टममध्ये सहज प्रवेश मिळतो.

### AI Agent Frameworks बद्दल अधिक प्रश्न आहेत?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा, इतर शिकणाऱ्यांशी भेटा, ऑफिस तासांमध्ये सहभागी व्हा आणि तुमचे AI Agents संबंधित प्रश्न विचारून उत्तर मिळवा.

## संदर्भ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel आणि AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">AutoGen / Semantic Kernel सह Azure AI Agent Service वापरून मल्टी-एजंट सोल्यूशन तयार करणे</a>

## मागील धडा

[AI Agents आणि Agent वापर प्रकरणांची ओळख](../01-intro-to-ai-agents/README.md)

## पुढील धडा

[Agentic Design Patterns समजून घेणे](../03-agentic-design-patterns/README.md)

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपयास लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.