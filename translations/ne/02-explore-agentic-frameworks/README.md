[![AI एजेन्ट फ्रेमवर्कहरूको अन्वेषण गर्दै](../../../translated_images/ne/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(यो पाठको भिडियो हेर्न माथिको चित्रमा क्लिक गर्नुहोस्)_

# AI एजेन्ट फ्रेमवर्कहरूको अन्वेषण गर्नुहोस्

AI एजेन्ट फ्रेमवर्कहरू सफ्टवेयर प्लेटफर्महरू हुन् जसले AI एजेन्टहरू निर्माण, परिनियोजन, र व्यवस्थापनलाई सजिलो बनाउन डिजाइन गरिएको हो। यी फ्रेमवर्कहरूले विकासकर्ताहरूलाई पूर्व-निर्मित कम्पोनेन्ट, अमूर्तनहरू, र उपकरणहरू प्रदान गर्छन् जसले जटिल AI प्रणालीहरूको विकासलाई सरल बनाउँछन्।

यी फ्रेमवर्कहरू विकासकर्ताहरूलाई तिनीहरूको अनुप्रयोगका विशिष्ट पक्षहरूमा ध्यान दिन सहयोग गर्छन्, किनभने AI एजेन्ट विकासका सामान्य चुनौतीहरूमा मानकीकृत दृष्टिकोणहरू प्रदान गर्छन्। तिनीहरूले AI प्रणालीहरूको निर्माणमा स्केलेबिलिटी, पहुँचयोग्यता, र दक्षता बढाउँछन्।

## परिचय 

यो पाठमा समावेश हुनेछ:

- AI एजेन्ट फ्रेमवर्कहरू के हुन् र तिनीहरूले विकासकर्ताहरूलाई के गर्न सक्षम पार्छन्?
- टोलीहरूले कसरी ती एजेन्टको क्षमता छिटो प्रोटोटाइप गर्न, पुनरावृत्ति गर्न, र सुधार गर्न प्रयोग गर्न सक्छन्?
- माइक्रोसफ्टले बनाएका फ्रेमवर्क र उपकरणहरू (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> र <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) बीच के फरक छ?
- के म मेरो विद्यमान Azure इकोसिस्टम उपकरणहरू प्रत्यक्ष रूपमा एकीकृत गर्न सक्छु, या मलाई स्वतन्त्र समाधानहरू चाहिन्छ?
- Microsoft Foundry Agent Service के हो र यो कसरी मेरो मद्दत गर्दैछ?

## सिक्ने उद्देश्यहरू

यो पाठको उद्देश्य तपाईँलाई बुझाउन सहयोग पुर्याउनु हो:

- AI एजेन्ट फ्रेमवर्कहरूको AI विकासमा भूमिकाको बारेमा।
- बौद्धिक एजेन्टहरू निर्माण गर्नका लागि AI एजेन्ट फ्रेमवर्कहरूको कसरी उपयोग गर्ने।
- AI एजेन्ट फ्रेमवर्कहरूले सक्षम बनाउने मुख्य क्षमता।
- Microsoft Agent Framework र Microsoft Foundry Agent Service बीचका भिन्नताहरू।

## AI एजेन्ट फ्रेमवर्कहरू के हुन् र तिनीहरूले विकासकर्ताहरूलाई के गर्न सक्षम पार्छन्?

परम्परागत AI फ्रेमवर्कहरूले तपाईंलाई AI लाई तपाईंको अनुप्रयोगहरूमा एकीकृत गर्न र ती अनुप्रयोगहरूलाई तलका तरिकाहरूले सुधार गर्न सहयोग गर्न सक्छन्:

- **व्यक्तिकरण**: AI ले प्रयोगकर्ता व्यवहार र प्राथमिकताहरू विश्लेषण गरेर व्यक्तिगत सिफारिस, सामग्री, र अनुभवहरू प्रदान गर्न सक्छ।
उदाहरण: Netflix जस्ता स्ट्रिमिङ सेवाहरूले AI प्रयोगकर्ता दर्शक इतिहासअनुसार चलचित्र र शोहरू सुझाव दिन प्रयोग गर्छन्, जसले प्रयोगकर्ता संलग्नता र सन्तुष्टिमा वृद्धि गर्छ।
- **स्वचालन र दक्षता**: AI ले दोहोरिने कार्यहरू स्वचालित गर्न, कार्यप्रवाह सरलीकृत गर्न, र सञ्चालन कार्यक्षमतामा सुधार गर्न सक्छ।
उदाहरण: ग्राहक सेवा अनुप्रयोगहरूमा AI–संचालित च्याटबटहरू सामान्य सोधपुछहरू सम्हाल्न प्रयोग गरिन्छन्, जसले प्रतिक्रिया समय घटाउँछ र जटिल समस्याहरूका लागि मानव एजेन्टहरूलाई खाली बनाउँछ।
- **सुधारिएको प्रयोगकर्ता अनुभव**: AI ले आवाज पहिचान, प्राकृतिक भाषा प्रशोधन, र भविष्यवाणी पाठजस्ता बौद्धिक सुविधाहरू प्रदान गरेर कुल प्रयोगकर्ता अनुभव सुधार गर्न सक्छ।
उदाहरण: Siri र Google सहायक जस्ता भर्चुअल सहायकहरूले आवाज आदेश बुझ्न र प्रतिक्रिया दिन AI प्रयोग गर्छन्, जसले प्रयोगकर्ताहरूलाई उनीहरूको उपकरणहरूसँग कुराकानी गर्न सजिलो बनाउँछ।

### त्यो सबै राम्रो लाग्छ, तर किन हामीलाई AI एजेन्ट फ्रेमवर्क चाहिन्छ?

AI एजेन्ट फ्रेमवर्कहरू केवल AI फ्रेमवर्क भन्दा बढी केहि प्रतिनिधित्व गर्छन्। तिनीहरू बुद्धिमान एजेन्टहरू निर्माण गर्न डिजाइन गरिएका छन् जसले प्रयोगकर्ताहरू, अन्य एजेन्टहरू, र वातावरणसँग अन्तरक्रिया गर्न सक्छन् र विशिष्ट लक्ष्यहरू प्राप्त गर्न सक्छन्। यी एजेन्टहरूले स्वतन्त्र व्यवहार देखाउन, निर्णय लिन, र बदलिँदो परिस्थितिमा अनुकूलन गर्न सक्छन्। AI एजेन्ट फ्रेमवर्कहरूले सक्षम बनाउने केही मुख्य क्षमताहरू हेरौं:

- **एजेन्ट सहकार्य र समन्वय**: धेरै AI एजेन्टहरू सिर्जना गर्न सक्षम पार्ने, जुन सँगै काम गर्न, सञ्चार गर्न, र जटिल कार्यहरू समाधान गर्न समन्वय गर्न सक्छन्।
- **कार्य स्वचालन र व्यवस्थापन**: बहु-चरण कार्यप्रवाहहरू स्वचालित गर्ने, कार्य बाँडफाँड गर्ने, र एजेन्टहरूबीच गतिशील कार्य व्यवस्थापनका लागि संयन्त्रहरू प्रदान गर्ने।
- **सन्दर्भ बुझाइ र अनुकूलन**: एजेन्टहरूलाई सन्दर्भ बुझ्न, बदलिँदो वातावरणमा अनुकूलन गर्न, र वास्तविक-समय जानकारीमा आधारित निर्णय लिन सक्षम बनाउने।

सारांशमा, एजेन्टहरूले तपाईंलाई बढी गर्न सक्षम बनाउँछन्, स्वचालनलाई अर्को स्तरमा लैजान्छन्, र वातावरणबाट सिक्न र अनुकूलन गर्न सक्ने बौद्धिक प्रणालीहरू निर्माण गर्न सहयोग गर्छन्।

## कसरी एजेन्टको क्षमता छिटो प्रोटोटाइप गर्न, पुनरावृत्ति गर्न, र सुधार गर्न सकिन्छ?

यो एक छिटो विकसित हुने क्षेत्र हो, तर धेरै AI एजेन्ट फ्रेमवर्कहरूमा साझा हुने केही कुराहरू छन् जसले तपाईंलाई छिटो प्रोटोटाइप र पुनरावृत्ति गर्न मद्दत गर्छन्: मोड्युल कम्पोनेन्टहरू, सहयोगी उपकरणहरू, र वास्तविक-समय सिकाइ। यीमा विस्तार गरौं:

- **मोड्युलर कम्पोनेन्ट्स प्रयोग गर्नुहोस्**: AI SDKहरूले पूर्वनिर्मित कम्पोनेन्टहरू प्रस्ताव गर्छन् जस्तै AI र मेमोरी कन्ट्याक्टरहरू, प्राकृतिक भाषामा वा कोड प्लगइनहरू मार्फत फंक्शन कलिङ, प्राम्प्ट टेम्प्लेटहरू, र अन्य।
- **सहयोगी उपकरणहरूको उपयोग गर्नुहोस्**: विशिष्ट भूमिका र कार्यहरू सहित एजेन्टहरू डिजाइन गर्नुहोस् जसले तिनीहरूलाई सहयोगी कार्यप्रवाह परीक्षण र परिमार्जन गर्न सक्षम बनाउँछ।
- **वास्तविक-समय सिकाइ गर्नुहोस्**: प्रतिक्रिया लूपहरू कार्यान्वयन गर्नुहोस् जहाँ एजेन्टहरू अन्तरक्रियाबाट सिक्छन् र तिनीहरूको व्यवहार गतिशील रूपमा समायोजन गर्छन्।

### मोड्युलर कम्पोनेन्ट्स प्रयोग गर्नुहोस्

Microsoft Agent Framework जस्ता SDKहरूले AI कन्ट्याक्टर, उपकरण परिभाषा, र एजेन्ट व्यवस्थापन जस्ता पूर्वनिर्मित कम्पोनेन्टहरू प्रदान गर्छन्।

**टोलीहरूले यसलाई कसरी प्रयोग गर्न सक्छन्**: टोलीहरूले यी कम्पोनेन्टहरू छिटो जोडेर कार्यशील प्रोटोटाइप बनाउन सक्छन्, जसले छिटो परीक्षण र पुनरावृत्तिको अनुमति दिन्छ।

**व्यावहारिक रूपमा कसरी काम गर्छ**: तपाइँले पूर्वनिर्मित पार्सर प्रयोग गरेर प्रयोगकर्ता इनपुटबाट जानकारी निकाल्न, मेमोरी मोड्युलमा डाटा भण्डारण र पुनःप्राप्त गर्न, र प्राम्प्ट जेनेरेटर मार्फत प्रयोगकर्तासँग अन्तरक्रिया गर्न सक्नुहुन्छ, सबैकुरा नयाँबाट निर्माण नगरी।

**उदाहरण कोड**: Microsoft Agent Framework प्रयोग गरी `FoundryChatClient` सँग कसरी मोडेललाई प्रयोगकर्ताको इनपुटमा उपकरण कल गर्ने प्रतिक्रिया दिन प्रयोग गर्न सकिन्छ, त्यो हेरौं:

``` python
# माइक्रोसफ्ट एजेन्ट फ्रेमवर्क पायथन उदाहरण

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# यात्रा बुक गर्न नमूना उपकरण कार्य परिभाषित गर्नुहोस्
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # उदाहरण आउटपुट: तपाईंको १ जनवरी २०२५ मा न्यूयोर्कको लागि उडान सफलतापूर्वक बुक गरिएको छ। सुरक्षित यात्रा गर्नुहोस्! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

यस उदाहरणबाट देखिन्छ कि कसरी तपाइँ पूर्वनिर्मित पार्सरलाई प्रयोगकर्ता इनपुटबाट कुंजी जानकारी निकाल्न प्रयोग गर्न सक्छौं, जस्तै उडान बुकिङ अनुरोधको उद्गम, गन्तव्य, र मिति। यो मोड्युलर दृष्टिकोणले तपाईंलाई उच्च-स्तरीय तर्कमा ध्यान केन्द्रित गर्न अनुमति दिन्छ।

### सहयोगी उपकरणहरूको उपयोग गर्नुहोस्

Microsoft Agent Framework जस्ता फ्रेमवर्कहरूले धेरै एजेन्टहरू सँगै काम गर्न सक्ने बनाउन सजिलो बनाउँछन्।

**टोलीहरूले यसलाई कसरी प्रयोग गर्न सक्छन्**: टोलीहरूले विशिष्ट भूमिका र कार्यहरू सहित एजेन्टहरू डिजाइन गर्न सक्छन्, जसले उनीहरूलाई सहयोगी कार्यप्रवाह परीक्षण र सुधार गर्न र समग्र प्रणाली दक्षता बढाउन सक्षम बनाउँछ।

**व्यावहारिक रूपमा कसरी काम गर्छ**: तपाइँ यस्तो टोली बनाउन सक्नुहुन्छ जहाँ प्रत्येक एजेन्टले विशेष कार्य गर्दछ, जस्तै डाटाको पुनःप्राप्ति, विश्लेषण, वा निर्णय-निर्माण। यी एजेन्टहरूले सञ्चार गरेर र जानकारी साटासाट गरेर साझा लक्ष्य जस्तै प्रयोगकर्ता प्रश्नको उत्तर दिन वा कार्य पूरा गर्न सक्छन्।

**उदाहरण कोड (Microsoft Agent Framework)**:

```python
# माइक्रोसफ्ट एजेन्ट फ्रेमवर्क प्रयोग गरेर सँगै काम गर्ने धेरै एजेन्टहरू सिर्जना गर्दै

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# डाटा पुनःप्राप्ति एजेन्ट
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# डाटा विश्लेषण एजेन्ट
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# काममा एजेन्टहरूलाई अनुक्रममा चलाउनुहोस्
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

माथिको कोडमा, तपाइँ देख्नुहुन्छ कसरी धेरै एजेन्टहरूलाई डेटा विश्लेषणका लागि सँगै काम गर्न उत्प्रेरित गर्ने कार्य सिर्जना गर्ने। हरेक एजेन्टले विशेष कार्य गर्दछ, र कार्य एजेन्टहरू समन्वय गरेर इच्छित परिणाम प्राप्त गर्न सञ्चालन गरिन्छ। विशेष भूमिका भएका समर्पित एजेन्टहरू सिर्जना गरेर तपाईं दक्षता र प्रदर्शन सुधार गर्न सक्नुहुन्छ।

### वास्तविक-समयमा सिक्नुहोस्

उन्नत फ्रेमवर्कहरू वास्तविक-समय सन्दर्भ बुझाइ र अनुकूलनका लागि क्षमता प्रदान गर्छन्।

**टोलीहरूले यसलाई कसरी प्रयोग गर्न सक्छन्**: टोलीहरूले यस्तो प्रतिक्रिया लूपहरू लागू गर्न सक्छन् जहाँ एजेन्टहरूले अन्तरक्रिया बाट सिक्छन् र आफ्नो व्यवहार गतिशील रूपमा समायोजन गर्छन् जसले क्षमताहरूको निरन्तर सुधार र परिष्करण गर्छ।

**व्यावहारिक रूपमा कसरी काम गर्छ**: एजेन्टहरूले प्रयोगकर्ता प्रतिक्रिया, वातावरणीय डेटा, र कार्य परिणामहरू विश्लेषण गरेर आफ्नो ज्ञान आधार अपडेट गर्छन्, निर्णय-निर्माण एल्गोरिदमहरू समायोजन गर्छन्, र समयसँगै प्रदर्शन सुधार गर्छन्। यस पुनरावृत्त सिकाइ प्रक्रियाले एजेन्टहरूलाई बदलिँदो अवस्थाहरू र प्रयोगकर्ता प्राथमिकताहरूमा अनुकूलन गर्न सक्षम बनाउँछ, जसले कुल प्रणाली प्रभावकारिता बढाउँछ।

## Microsoft Agent Framework र Microsoft Foundry Agent Service बीच के फरक छ?

यी दृष्टिकोणहरू तुलना गर्ने धेरै तरिकाहरू छन्, तर तिनीहरूको डिजाइन, क्षमता, र लक्षित प्रयोग केसका सन्दर्भमा केही मुख्य भिन्नताहरू हेरौं:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework ले `FoundryChatClient` प्रयोग गरी AI एजेन्टहरू निर्माण गर्न एक सरल SDK प्रदान गर्दछ। यसले विकासकर्ताहरूलाई Azure OpenAI मोडेलहरू प्रयोग गरी उपकरण कलिङ, संवाद व्यवस्थापन, र Azure परिचय मार्फत उद्यम-स्तरीय सुरक्षा सहित एजेन्टहरू सिर्जना गर्न सक्षम पार्दछ।

**प्रयोग केसहरू**: उपकरण प्रयोग, बहु-चरण कार्यप्रवाह, र उद्यम एकीकरण परिदृश्यहरूसहित उत्पादन-तयार AI एजेन्टहरू निर्माण गर्ने।

Microsoft Agent Framework का केही महत्वपूर्ण मूल अवधारणाहरू यस्ता छन्:

- **एजेन्टहरू**। `FoundryChatClient` मार्फत एजेन्ट सिर्जना हुन्छ र नाम, निर्देशनहरू, र उपकरणहरू द्वारा कन्फिगर गरिन्छ। एजेन्टले:
  - **प्रयोगकर्ता सन्देशहरू प्रक्रिया गर्ने** र Azure OpenAI मोडेलहरू प्रयोग गरी प्रतिक्रिया उत्पन्न गर्ने।
  - **संवाद सन्दर्भ अनुसार उपकरणहरू स्वचालित रूपमा कल गर्ने**।
  - **धेरै अन्तरक्रियाहरूमा संवाद स्थिति कायम गर्ने**।

  यहाँ एजेन्ट कसरी सिर्जना गर्ने कोड स्निपेट छ:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **उपकरणहरू**। फ्रेमवर्कले पाइथन फंक्शनहरूलाई उपकरणको रूपमा परिभाषित गर्नु समर्थन गर्छ जुन एजेन्टले स्वचालित रूपमा कल गर्न सक्छ। उपकरणहरू एजेन्ट सिर्जना गर्दा दर्ता हुन्छन्:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **बहु-एजेन्ट समन्वय**। तपाइँ विभिन्न विशेषज्ञता भएका धेरै एजेन्टहरू बनाउन र तिनीहरूको कार्य समन्वय गर्न सक्नुहुन्छ:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure परिचय एकीकरण**। फ्रेमवर्कले सुरक्षित, कीबिना प्रमाणिकरणका लागि `AzureCliCredential` (वा `DefaultAzureCredential`) प्रयोग गर्छ, जसले API कुञ्जीहरू व्यवस्थापन गर्न आवश्यक हटाउँछ।

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service हालै Microsoft Ignite 2024 मा परिचय गरिएको नयाँ सेवा हो। यसले Llama 3, Mistral, र Cohere जस्ता खुला स्रोत LLMs लाई प्रत्यक्ष कल गर्ने जस्ता अधिक लचिलो मोडेलहरूको साथ AI एजेन्ट विकास र परिनियोजन अनुमति दिन्छ।

Microsoft Foundry Agent Service ले उद्यम सुरक्षा संयन्त्रहरू र डाटा भण्डारण विधिहरूलाई बढी बलियो बनाउँछ, जसले यसलाई उद्यम अनुप्रयोगहरूका लागि उपयुक्त बनाउँछ।

यो Microsoft Agent Framework सँग सहज रूपमा काम गर्छ एजेन्टहरू निर्माण र परिनियोजनका लागि।

यो सेवा हाल सार्वजनिक पूर्वावलोकन अवस्थामा छ र एजेन्टहरू निर्माणका लागि Python र C# समर्थन गर्छ।

Microsoft Foundry Agent Service Python SDK प्रयोग गरी हामी प्रयोगकर्ताले परिभाषित गरेको उपकरणसहित एजेन्ट सिर्जना गर्न सक्छौं:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# उपकरण कार्यहरू परिभाषित गर्नुहोस्
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### मूल अवधारणाहरू

Microsoft Foundry Agent Service मा निम्न मूल अवधारणाहरू छन्:

- **एजेन्ट**। Microsoft Foundry Agent Service Microsoft Foundry सँग एकीकृत गर्छ। Microsoft Foundry भित्र, AI एजेन्टले "स्मार्ट" माइक्रोसर्भिसको रूपमा काम गर्दछ जुन प्रश्नहरूको जवाफ दिन (RAG), कार्यहरू प्रदर्शन गर्न, वा सम्पूर्ण कार्यप्रवाहहरू स्वचालित गर्न प्रयोग गर्न सकिन्छ। यो जेनेरेटिभ AI मोडेलहरूको शक्ति र उपकरणहरूको संयोजनद्वारा हासिल गर्छ जसले यसलाई वास्तविक-विश्व डाटा स्रोतहरूसँग पहुँच र अन्तरक्रिया गर्न अनुमति दिन्छ। यहाँ एजेन्टको उदाहरण छ:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    यस उदाहरणमा, `gpt-5-mini` मोडेल, नाम `my-agent`, र निर्देशनहरू `You are helpful agent` सहित एजेन्ट सिर्जना गरिएको छ। एजेन्टलाई कोड व्याख्या कार्यहरू प्रदर्शन गर्न उपकरणहरू र स्रोतहरूले सुसज्जित गरिएको छ।

- **थ्रेड र सन्देशहरू**। थ्रेड अर्को महत्वपूर्ण अवधारणा हो। यसले एजेन्ट र प्रयोगकर्ताबीचको संवाद वा अन्तरक्रिया प्रतिनिधित्व गर्छ। थ्रेडहरू प्रयोगकर्तासँग संवादको प्रगति ट्र्याक गर्न, सन्दर्भ जानकारी भण्डारण गर्न, र अन्तरक्रियाको अवस्था व्यवस्थापन गर्न प्रयोग गर्न सकिन्छ। यहाँ थ्रेडको उदाहरण छ:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # एजेन्टलाई थ्रेडमा काम गर्न भनौं
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # एजेन्टको प्रतिक्रिया हेर्न सबै सन्देशहरू ल्याएर लग गर्नुहोस्
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    माथिको कोडमा, एउटा थ्रेड सिर्जना गरिएको छ। त्यसपछि थ्रेडमा सन्देश पठाइन्छ। `create_and_process_run` कल गरेर, एजेन्टलाई थ्रेडमा कार्य गर्न भनिन्छ। अन्त्यमा, सन्देशहरू फेच गरिन्छ र लग गरिन्छ एजेन्टको प्रतिक्रिया हेर्न। यी सन्देशहरूले प्रयोगकर्ता र एजेन्टबीचको संवादको प्रगति देखाउँछन्। यो पनि बुझ्न महत्वपूर्ण छ कि सन्देशहरू विभिन्न प्रकारका हुन सक्छन् जस्तै टेक्स्ट, छवि, वा फाइल, जुन एजेन्टको कामको नतिजा जस्तै छवि वा टेक्स्ट प्रतिक्रिया हुन सक्छ। विकासकर्ताका रूपमा, तपाईं यस जानकारीलाई थप प्रक्रिया गर्न वा प्रयोगकर्तालाई प्रस्तुत गर्न प्रयोग गर्न सक्नुहुन्छ।

- **Microsoft Agent Framework सँग एकीकरण**। Microsoft Foundry Agent Service Microsoft Agent Framework सँग सहज रूपमा काम गर्छ, जसको अर्थ तपाईंले `FoundryChatClient` प्रयोग गरी एजेन्टहरू निर्माण गर्न सक्नुहुन्छ र तिनीहरूलाई उत्पादनका लागि Agent Service मार्फत परिनियोजन गर्न सक्नुहुन्छ।

**प्रयोग केसहरू**: Microsoft Foundry Agent Service उद्यम अनुप्रयोगहरूको लागि डिजाइन गरिएको हो जसलाई सुरक्षित, स्केलेबल, र लचिलो AI एजेन्ट परिनियोजन आवश्यक छ।

## यी दृष्टिकोणहरू बीच के फरक छ?
 
त्यहाँ केही ओभरलैप छ जस्तो लाग्छ, तर डिजाइन, क्षमता, र लक्षित प्रयोग केसहरूको सन्दर्भमा केही मुख्य फरकहरू छन्:
 
- **Microsoft Agent Framework (MAF)**: AI एजेन्टहरू निर्माण गर्नका लागि उत्पादन-तयार SDK हो। यो उपकरण कलिङ, संवाद व्यवस्थापन, र Azure परिचय एकीकरणका साथ एक सरल API प्रदान गर्दछ।
- **Microsoft Foundry Agent Service**: Microsoft Foundry मा एजेन्टहरूको लागि प्लेटफर्म र परिनियोजन सेवा हो। यसले Azure OpenAI, Azure AI Search, Bing Search र कोड निष्पादन जस्ता सेवाहरूमा इन-बिल्ट कनेक्टिभिटी प्रदान गर्दछ।
 
अझै निश्चित हुनुहुन्न कुन रोज्ने?

### प्रयोग केसहरू
 
के हामी तपाईंलाई केही सामान्य प्रयोग केसहरू मार्फत सहयोग गर्न सक्छौं:
 
> प्रश्न: म उत्पादन AI एजेन्ट अनुप्रयोगहरू निर्माण गर्दैछु र छिटो सुरु गर्न चाहन्छु
>

>उत्तर: Microsoft Agent Framework उत्कृष्ट विकल्प हो। यसले `FoundryChatClient` मार्फत सरल, पाइथनिक API प्रदान गर्दछ जसले तपाईंलाई केही लाइनमा उपकरणहरू र निर्देशनहरू सहित एजेन्टहरू परिभाषित गर्न दिन्छ।

>प्रश्न: मलाई Azure एकीकरणहरू जस्तै खोज र कोड निष्पादनका साथ उद्यम-स्तरीय परिनियोजन चाहिन्छ
>
>उत्तर: Microsoft Foundry Agent Service सबैभन्दा उपयुक्त छ। यो प्लेटफर्म सेवा हो जसले धेरै मोडेलहरू, Azure AI Search, Bing Search र Azure Functions को लागि इन-बिल्ट क्षमताहरू प्रदान गर्दछ। तपाईं Foundry पोर्टलमा सजिलै आफ्नो एजेन्टहरू निर्माण र स्केलमा परिनियोजन गर्न सक्नुहुन्छ।
 
> प्रश्न: म अझै समेत कन्फ्युज छु, मलाई एउटा विकल्प दिनुहोस्
>
> उत्तर: Microsoft Agent Framework बाट सुरु गर्नुहोस् तपाइँका एजेन्टहरू निर्माण गर्न, र उत्पादनमा परिनियोजन र स्केल गर्न आवश्यक पर्दा Microsoft Foundry Agent Service प्रयोग गर्नुहोस्। यसले तपाईंलाई एजेन्ट तर्कमा छिटो पुनरावृत्ति गर्न र उद्यम परिनियोजनको स्पष्ट बाटो पाउन मद्दत गर्छ।
 
मुख्य भिन्नताहरू सारांश गर्न तालिका हेरौं:

| फ्रेमवर्क | फोकस | मूल अवधारणाहरू | प्रयोग केसहरू |
| --- | --- | --- | --- |
| Microsoft Agent Framework | उपकरण कलिङ सहित सरल एजेन्ट SDK | एजेन्टहरू, उपकरणहरू, Azure परिचय | AI एजेन्ट निर्माण, उपकरण प्रयोग, बहु-चरण कार्यप्रवाहहरू |
| Microsoft Foundry Agent Service | लचिलो मोडेलहरू, उद्यम सुरक्षा, कोड उत्पादन, उपकरण कलिङ | मोड्युलरिटी, सहयोग, प्रक्रिया व्यवस्थापन | सुरक्षित, स्केलेबल, र लचिलो AI एजेन्ट परिनियोजन |

## के म मेरो विद्यमान Azure इकोसिस्टम उपकरणहरू प्रत्यक्ष रूपमा एकीकृत गर्न सक्छु, या मलाई स्वतन्त्र समाधानहरू चाहिन्छ?


उत्तर हो, तपाईंले आफ्नो अवस्थित Azure पारिस्थितिकी प्रणाली उपकरणहरू Microsoft Foundry Agent Service सँग सिधै एकीकृत गर्न सक्नुहुन्छ, विशेष गरी यो अन्य Azure सेवाहरूसँग सहज रूपमा काम गर्ने गरी निर्माण गरिएको छ। उदाहरणका लागि, तपाईं Bing, Azure AI Search, र Azure Functions लाई एकीकृत गर्न सक्नुहुन्छ। Microsoft Foundry सँग पनि गहिरो एकीकरण छ।

Microsoft Agent Framework ले पनि `FoundryChatClient` र Azure पहिचान मार्फत Azure सेवाहरूसँग एकीकृत गर्दछ, जसले तपाईंलाई तपाईंको एजेन्ट उपकरणहरूबाट सिधै Azure सेवाहरू कल गर्न अनुमति दिन्छ।

## नमूना कोडहरू

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI Agent Frameworks सम्बन्धमा थप प्रश्नहरू छन्?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) मा सहभागी हुनुहोस् जहाँ तपाईं अन्य सिक्नेहरूलाई भेट्न, अफिस आवरमा जान र तपाईंका AI एजेन्ट सम्बन्धी प्रश्नहरूको उत्तर पाउन सक्नुहुन्छ।

## सन्दर्भहरू

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## अघिल्लो पाठ

[AI एजेन्ट र एजेन्ट उपयोगका केसहरूको परिचय](../01-intro-to-ai-agents/README.md)

## अर्को पाठ

[Agentic Design Patterns को समझदारी](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->