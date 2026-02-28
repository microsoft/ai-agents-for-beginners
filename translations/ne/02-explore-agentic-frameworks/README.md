[![AI एजेन्ट फ्रेमवर्कहरूको अन्वेषण](../../../translated_images/ne/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(उपरोक्त चित्रमा क्लिक गरी यस पाठको भिडियो हेर्नुहोस्)_

# AI एजेन्ट फ्रेमवर्कहरूको अन्वेषण

AI एजेन्ट फ्रेमवर्कहरू ती सफ्टवेयर प्लेटफर्महरू हुन् जसले AI एजेन्टहरूको सिर्जना, तैनाती, र व्यवस्थापनलाई सरल बनाउन डिजाइन गरिएका हुन्छन्। यी फ्रेमवर्कहरूले विकासकर्ताहरूलाई पूर्व-निर्मित कम्पोनेन्टहरू, अमूर्तताहरू, र उपकरणहरू प्रदान गर्दछन् जसले जटिल AI प्रणालीहरूको विकासलाई सहज बनाउँछन्।

यी फ्रेमवर्कहरूले विकासकर्ताहरूलाई AI एजेन्ट विकासका साधारण चुनौतीहरूका लागि मानकीकृत दृष्टिकोणहरू उपलब्ध गराएर उनीहरूको अनुप्रयोगहरूको अनौठा पक्षहरूमा ध्यान केन्द्रित गर्न मद्दत गर्दछन्। यसले स्केलेबिलिटी, पहुँचयोग्यता, र दक्षता सुधार गर्छ।

## परिचय 

यो पाठले समावेश गर्नेछ:

- AI एजेन्ट फ्रेमवर्कहरू के हुन् र तिनीहरूले विकासकर्ताहरूलाई के हासिल गर्न सक्षम बनाउँछन्?
- टोलीहरूले यी प्रयोग गरेर कसरी छिटो प्रोटोटाइप बनाउन, पुनरावृत्ति गर्न, र आफ्ना एजेन्टहरूको क्षमता सुधार गर्न सक्छन्?
- Microsoft द्वारा सिर्जना गरिएका फ्रेमवर्क र उपकरणहरू ( <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> र <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) बीच के फरकहरू छन्?
- के म मेरो अवस्थित Azure इकोसिस्टमका उपकरणहरू सिधै एकीकृत गर्न सक्छु, वा मलाई स्वतन्त्र समाधानहरू आवश्यक छन्?
- Azure AI Agents सेवा के हो र यसले मलाई कसरी मद्दत गरिरहेको छ?

## सिकाइ लक्ष्यहरू

यस पाठका लक्ष्यहरू तपाईंले बुझ्नमा मद्दत गर्न हुन्:

- AI विकासमा AI एजेन्ट फ्रेमवर्कहरूको भूमिका।
- बुद्धिमान एजेन्टहरू निर्माण गर्न AI एजेन्ट फ्रेमवर्कहरू कसरी उपयोग गर्ने।
- AI एजेन्ट फ्रेमवर्कहरूले सक्षम बनाउने प्रमुख क्षमताहरू।
- Microsoft Agent Framework र Azure AI Agent Service बीचको भिन्नताहरू।

## AI एजेन्ट फ्रेमवर्कहरू के हुन् र तिनीहरूले विकासकर्ताहरूलाई के गर्न सक्षम बनाउँछन्?

परम्परागत AI फ्रेमवर्कहरूले तपाईंलाई तपाईंका अनुप्रयोगहरूमा AI एकीकृत गर्न र ती अनुप्रयोगहरूलाई निम्न तरिकाले सुधार गर्न मद्दत गर्न सक्छन्:

- **व्यक्तिकरण**: AI ले प्रयोगकर्ता व्यवहार र प्राथमिकताहरू विश्लेषण गरी व्यक्तिगत सिफारिसहरू, सामग्री, र अनुभवहरू प्रदान गर्न सक्छ।
उदाहरण: Netflix जस्ता स्ट्रिमिङ सेवाहरूले हेर्ने इतिहासको आधारमा चलचित्र र शो सिफारिस गर्न AI प्रयोग गर्छन्, जसले प्रयोगकर्ता संलग्नता र सन्तुष्टि बढाउँछ।
- **स्वचालन र दक्षता**: AI ले दोहोरिने कार्यहरू स्वचालित गर्न, कार्यप्रवाहहरूलाई सरल बनाउन, र सञ्चालनात्मक दक्षता सुधार गर्न सक्छ।
उदाहरण: ग्राहक सेवा अनुप्रयोगहरूले सामान्य प्रश्नहरू सम्हाल्न AI-समर्थित च्याटबटहरू प्रयोग गर्छन्, जसले प्रतिक्रिया समय घटाउँछ र जटिल मुद्दाहरूका लागि मानवीय एजेन्टहरूलाई मुक्त गर्छ।
- **सुधारिएको प्रयोगकर्ता अनुभव**: AI ले भ्वाइस चिन्ने, प्राकृतिक भाषा प्रशोधन, र पूर्वानुमानित पाठ जस्ता बुद्धिमान सुविधाहरू प्रदान गरेर समग्र प्रयोगकर्ता अनुभव सुधार गर्न सक्छ।
उदाहरण: Siri र Google Assistant जस्ता भर्चुअल सहायकहरूले भ्वाइस आदेशहरू बुझ्न र उत्तर दिनका लागि AI प्रयोग गर्छन्, जसले प्रयोगकर्ताहरूलाई आफ्ना उपकरणहरूसँग अन्तर्क्रियामा सजिलो बनाउँछ।

### यी सबै राम्रो लाग्छ हैन? अनि हामीलाई AI एजेन्ट फ्रेमवर्क किन चाहिन्छ?

AI एजेन्ट फ्रेमवर्कहरू केवल AI फ्रेमवर्कहरू भन्दा बढी प्रतिनिधित्व गर्दछन्। तिनीहरू ती बुद्धिमान एजेन्टहरू सिर्जना गर्न सक्षम गराउन डिजाइन गरिएका हुन्छन् जुन प्रयोगकर्ताहरू, अन्य एजेन्टहरू, र वातावरणसँग अन्तर्क्रिया गरी विशिष्ट लक्ष्यहरू हासिल गर्न सक्छन्। यी एजेन्टहरूले स्वतन्त्र व्यवहार प्रदर्शन गर्न, निर्णय लिन, र परिवर्तनशील परिस्थितिहरूमा अनुकूलन गर्न सक्छन्। AI एजेन्ट फ्रेमवर्कहरूले सक्षम गराउने केही प्रमुख क्षमताहरूमा हेर्नुहोस्:

- **एजेन्ट सहयोग र समन्वय**: धेरै AI एजेन्टहरू सिर्जना गर्न सक्षम पार्छ जसले सँगै काम गर्न, सञ्चार गर्न, र जटिल कार्यहरू समाधान गर्न समन्वय गर्न सक्छन्।
- **कार्य स्वचालन र व्यवस्थापन**: बहु-चरण कार्यप्रवाहहरू स्वचालित गर्ने, कार्य प्रतिनिधित्व गर्ने, र एजेन्टहरूबीच गतिशील कार्य व्यवस्थापन गर्ने मेकानिजमहरू प्रदान गर्छ।
- **सन्दर्भगत बुझाइ र अनुकूलन**: एजेन्टहरूलाई सन्दर्भ बुझ्ने, परिवर्तनशील वातावरणमा अनुकूलन गर्ने, र रियल-टाइम जानकारीको आधारमा निर्णय लिन सक्षम बनाउँछ।

सारांशमा, एजेन्टहरूले तपाईंलाई बढी गर्न अनुमति दिन्छन्, स्वचालनलाई अर्को स्तरमा लैजान्छन्, र तिनीहरूले वातावरणबाट सिक्ने र अनुकूलन गर्ने थप बुद्धिमान प्रणालीहरू सिर्जना गर्न मद्दत गर्दछन्।

## कसरी छिटो प्रोटोटाइप गर्न, पुनरावृत्ति गर्न, र एजेन्टको क्षमताहरू सुधार गर्ने?

यो द्रुत रूपमा बदलिने क्षेत्र हो, तर धेरै AI एजेन्ट फ्रेमवर्कहरूमा साझा केहि तत्वहरू छन् जसले छिटो प्रोटोटाइप र पुनरावृत्ति गर्न मद्दत गर्छन्—विशेष गरी मोड्युलर कम्पोनेंटहरू, सहकारी उपकरणहरू, र रियल-टाइम सिकाइ। यीमा हेर्छौं:

- **मोड्युलर कम्पोनेंटहरू प्रयोग गर्नुहोस्**: AI SDK हरूले पूर्व-निर्मित कम्पोनेंटहरू जस्तै AI र मेमोरी कनेक्टरहरू, प्राकृतिक भाषाबाट वा कोड प्लगिनहरू मार्फत फंक्शन कल गर्ने सुविधा, प्रॉम्प्ट टेम्प्लेटहरू, र थप प्रदान गर्दछन्।
- **सहकारी उपकरणहरू प्रयोग गर्नुहोस्**: विशिष्ट भूमिका र कार्यहरूका साथ एजेन्टहरू डिजाइन गर्नुहोस्, जसले उनीहरूलाई सहकारी कार्यप्रवाह परीक्षण र परिष्कृत गर्न सक्षम बनाउँछ।
- **रियल-टाइममा सिक्नुहोस्**: प्रतिक्रिया लूपहरू लागू गर्नुहोस् जहाँ एजेन्टहरूले अन्तर्क्रियाबाट सिक्छन् र आफ्ना व्यवहारहरू गतिशील रूपमा समायोजन गर्दछन्।

### मोड्युलर कम्पोनेंटहरू प्रयोग गर्नुहोस्

Microsoft Agent Framework जस्ता SDK हरूले AI कनेक्टरहरू, उपकरण परिभाषाहरू, र एजेन्ट व्यवस्थापन जस्ता पूर्व-निर्मित कम्पोनेंटहरू प्रदान गर्दछन्।

**टोलीहरूले यी कसरी प्रयोग गर्न सक्छन्**: टोलीहरूले यी कम्पोनेंटहरू छिटो जम्मा गरी कार्यशील प्रोटोटाइप सिर्जना गर्न सक्छन्, जसले शून्यबाट सुरु नगरी द्रुत प्रयोग र पुनरावृत्ति सम्भव बनाउँछ।

**व्यवहारमा यो कसरी काम गर्छ**: तपाईं प्रयोगकर्ता इनपुटबाट जानकारी निकाल्न पूर्व-निर्मित पार्सर, डेटा भण्डारण र पुन:प्राप्तिका लागि मेमोरी मोड्युल, र प्रयोगकर्तासँग अन्तरक्रिया गर्न प्रॉम्प्ट जेनेरेटर प्रयोग गर्न सक्नुहुन्छ, सबै यी कम्पोनेंटहरू शून्यबाट बनाउन आवश्यक बिना।

**उदाहरण कोड**. Microsoft Agent Framework लाई `AzureAIProjectAgentProvider` सँग कसरी प्रयोग गरी मोड्युलर कम्पोनेंटबाट टुल कल सहित मोडलले प्रयोगकर्ता इनपुटमा प्रतिक्रिया दिन सक्छ भनेर तलको उदाहरणमा हेरौं:

``` python
# माइक्रोसफ्ट एजेन्ट फ्रेमवर्क पायथन उदाहरण

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# यात्रा बुक गर्न नमूना उपकरण कार्य परिभाषित गर्नुहोस्
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # उदाहरण आउटपुट: तपाईंको जनवरी १, २०२५ मा न्यूयोर्कका लागि उडान सफलतापूर्वक बुक गरिएको छ। सुरक्षित यात्रा गर्नुहोस्! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

यस उदाहरणबाट तपाईंले देख्न सक्नुहुन्छ कि कसरी प्रयोगकर्ता इनपुटबाट उत्पत्ति, गन्तव्य, र फ्लाइट बुकिङ अनुरोधको मिति जस्ता मुख्य जानकारी निकाल्न पूर्व-निर्मित पार्सरलाई प्रयोग गर्न सकिन्छ। यो मोड्युलर दृष्टिकोणले तपाईंलाई उच्च-स्तरीय लॉजिकमा ध्यान केन्द्रित गर्न अनुमति दिन्छ।

### सहकारी उपकरणहरू प्रयोग गर्नुहोस्

Microsoft Agent Framework जस्ता फ्रेमवर्कहरूले सँगै काम गर्न सक्ने धेरै एजेन्टहरू सिर्जना गर्न सजिलो बनाउँछन्।

**टोलीहरूले यी कसरी प्रयोग गर्न सक्छन्**: टोलीहरूले विशिष्ट भूमिका र कार्यहरू भएकाहरू एजेन्टहरू डिजाइन गर्न सक्छन्, जसले उनीहरूलाई सहकारी कार्यप्रवाहहरू परीक्षण र परिष्कृत गर्न अनुमति दिन्छ र समग्र प्रणाली दक्षता सुधार गर्छ।

**व्यवहारमा यो कसरी काम गर्छ**: तपाईं एक एजेन्ट टोली सिर्जना गर्न सक्नुहुन्छ जहाँ हरेक एजेन्टले विशेष कार्य गर्दछ, जस्तै डेटा पुन:प्राप्ति, विश्लेषण, वा निर्णय-निर्माण। यी एजेन्टहरूले सामान्य लक्ष्य, जस्तै प्रयोगकर्ताको प्रश्नको उत्तर दिन वा कुनै कार्य पूरा गर्न, प्राप्त गर्नका लागि सञ्चार र जानकारी साझा गर्न सक्छन्।

**उदाहरण कोड (Microsoft Agent Framework)**:

```python
# माइक्रोसफ्ट एजेन्ट फ्रेमवर्क प्रयोग गरी सँगै काम गर्ने धेरै एजेन्टहरू सिर्जना गर्दै

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# डाटा प्राप्ति एजेन्ट
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# डाटा विश्लेषण एजेन्ट
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# कार्यमा क्रमशः एजेन्टहरू चलाउँदै
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

अघिल्लो कोडमा तपाईंले देख्नुहुनेछ कि कसरी बहु एजेन्टहरूको समन्वय गरेर डेटा विश्लेषण गर्ने कार्य सिर्जना गर्न सकिन्छ। प्रत्येक एजेन्टले विशेष कार्य पूरा गर्छ, र इच्छित परिणाम हासिल गर्न एजेन्टहरूको समन्वयबाट कार्य निष्पादन गरिन्छ। समर्पित भूमिका भएका एजेन्टहरू सिर्जना गरेर तपाईं कार्य दक्षता र प्रदर्शन सुधार गर्न सक्नुहुन्छ।

### रियल-टाइममा सिक्नुहोस्

उन्नत फ्रेमवर्कहरूले रियल-टाइम सन्दर्भ बुझाइ र अनुकूलन क्षमताहरू प्रदान गर्दछन्।

**टोलीहरूले यी कसरी प्रयोग गर्न सक्छन्**: टोलीहरूले प्रतिक्रिया लूपहरू लागू गर्न सक्छन् जहाँ एजेन्टहरूले अन्तर्क्रियाबाट सिक्छन् र आफ्ना व्यवहारहरू गतिशील रूपमा समायोजन गर्दछन्, जसले निरन्तर सुधार र क्षमताहरूको परिष्करण ल्याउँछ।

**व्यवहारमा यो कसरी काम गर्छ**: एजेन्टहरूले प्रयोगकर्ता प्रतिक्रिया, वातावरणीय डेटा, र कार्य परिणामहरूको विश्लेषण गरी आफ्नो ज्ञान आधार अपडेट गर्न, निर्णय-निर्माण एल्गोरिद्म समायोजन गर्न, र समयसँगै प्रदर्शन सुधार गर्न सक्छन्। यो पुनरावृत्तिमै सिकाइ प्रक्रियाले एजेन्टहरूलाई परिवर्तनशील स्थिति र प्रयोगकर्ता प्राथमिकताहरूमा अनुकूलन गर्न सक्षम बनाउँछ, जसले समग्र प्रणाली प्रभावकारिता बढाउँछ।

## Microsoft Agent Framework र Azure AI Agent Service बीच के फरक छन्?

यी दृष्टिकोणहरू तुलना गर्ने धेरै तरिकाहरू छन्, तर तिनीहरूको डिजाइन, क्षमताहरू, र लक्षित प्रयोग केसहरूको सन्दर्भमा केहि प्रमुख फरकहरू हेर्नुहोस्:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework ले `AzureAIProjectAgentProvider` प्रयोग गरेर AI एजेन्टहरू निर्माण गर्नका लागि प्रवाहशील SDK प्रदान गर्छ। यसले विकासकर्ताहरूलाई Azure OpenAI मोडेलहरू प्रयोग गरी उपकरण कल, संवाद व्यवस्थापन, र Azure पहिचानमार्फत एन्त्रप्राइज-ग्रेड सुरक्षा सहित एजेन्टहरू सिर्जना गर्न सक्षम बनाउँछ।

**प्रयोग केसहरू**: उपकरण प्रयोग, बहु-चरण कार्यप्रवाहहरू, र एन्त्रप्राइज एकीकरण परिदृश्यहरूसँग उत्पादन-तयार AI एजेन्टहरू निर्माण गर्नु।

यहाँ Microsoft Agent Framework का केहि महत्त्वपूर्ण मुख्य अवधारणाहरू छन्:

- **एजेन्टहरू**। एजेन्ट `AzureAIProjectAgentProvider` मार्फत सिर्जना गरिन्छ र नाम, निर्देशनहरू, र उपकरणहरूसँग कन्फिगर गरिन्छ। एजेन्टले:
  - **प्रयोगकर्ता सन्देशहरू प्रशोधन गर्नु** र Azure OpenAI मोडेलहरू प्रयोग गरी प्रतिक्रियाहरू उत्पन्न गर्नु।
  - **स्वतः उपकरण कल गर्नु** कुराकानी सन्दर्भको आधारमा।
  - **धेरै अन्तरक्रियाहरूमा कुराकानी स्थिति कायम राख्नु**।

  यहाँ एजेन्ट कसरी सिर्जना गर्ने देखाउने कोड स्निपेट छ:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **उपकरणहरू (Tools)**। फ्रेमवर्कले एजेन्टले स्वतः आह्वान गर्न सक्ने Python फंक्शनहरूका रूपमा उपकरणहरू परिभाषित गर्न समर्थन गर्दछ। एजेन्ट सिर्जना गर्दा उपकरणहरू दर्ता गरिन्छ:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **बहु-एजेन्ट समन्वय**। तपाईं फरक विशेषीकरण भएका धेरै एजेन्टहरू सिर्जना गर्न र तिनीहरूको काम समन्वय गर्न सक्नुहुन्छ:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure Identity एकीकरण**। फ्रेमवर्कले सुरक्षित, कुंजी-रहित प्रमाणीकरणका लागि `AzureCliCredential` (वा `DefaultAzureCredential`) प्रयोग गर्दछ, जसले सिधा API कुञ्जीहरू व्यवस्थापन गर्ने आवश्यकतालाई हटाउँछ।

## Azure AI Agent Service

Azure AI Agent Service Microsoft Ignite 2024 मा परिचय गराइएको एक नयाँ थप सेवा हो। यसले Llama 3, Mistral, र Cohere जस्ता ओपन-सोर्स LLM हरू सिधै कल गर्नजस्ता बढी लचकदार मोडेलहरू प्रयोग गरेर AI एजेन्टहरूको विकास र तैनाती गर्न अनुमति दिन्छ।

Azure AI Agent Service ले बलियो एन्त्रप्राइज सुरक्षा म्याकानिज्म र डेटा स्टोरेज विधिहरू प्रदान गर्छ, जसले यसलाई एन्त्रप्राइज अनुप्रयोगहरूका लागि उपयुक्त बनाउँछ। 

यसले Microsoft Agent Framework सँग आउट-ऑफ-द-बक्स काम गर्दछ एजेन्टहरू निर्माण र तैनाती गर्नका लागि।

यो सेवा हाल Public Preview मा छ र एजेन्टहरू निर्माणका लागि Python र C# लाई समर्थन गर्छ।

Azure AI Agent Service Python SDK प्रयोग गरेर, हामी प्रयोगकर्ता-परिभाषित उपकरणसँग एउटा एजेन्ट सिर्जना गर्न सक्छौं:

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
        model="gpt-4o-mini",
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

### मुख्य अवधारणाहरू

Azure AI Agent Service का निम्नलिखित मुख्य अवधारणाहरू छन्:

- **एजेन्ट**। Azure AI Agent Service Microsoft Foundry सँग एकीकृत हुन्छ। AI Foundry भित्र, एक AI एजेन्टलाई "स्मार्ट" माइक्रोसर्भिसको रूपमा प्रयोग गर्न सकिन्छ जुन प्रश्नहरूको उत्तर दिन (RAG), क्रियाहरू प्रदर्शन गर्न, वा कार्यप्रवाहहरू पूर्णतया स्वचालित गर्न प्रयोग हुन्छ। यसले जेनेरेटिभ AI मोडेलहरूको शक्ति र उपकरणहरूको संयोजन गरेर वास्तविक-विश्व डेटा स्रोतहरूमा पहुँच र अन्तरक्रिया गर्न सक्षम गर्दछ। यहाँ एउटा एजेन्टको उदाहरण छ:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    यस उदाहरणमा, `gpt-4o-mini` मोडेल, नाम `my-agent`, र निर्देशनहरू `You are helpful agent` सहित एजेन्ट सिर्जना गरिएको छ। एजेन्टलाई कोड व्याख्या कार्यहरू प्रदर्शन गर्न उपकरण र स्रोतहरूसँग सुसज्जित गरिएको छ।

- **थ्रेड र सन्देशहरू**। थ्रेड अर्को महत्त्वपूर्ण अवधारणा हो। यसले एजेन्ट र प्रयोगकर्ता बीचको कुराकानी वा अन्तरक्रिया प्रतिनिधित्व गर्दछ। थ्रेडहरूलाई कुराकानीको प्रगति ट्र्याक गर्न, सन्दर्भ जानकारी भण्डारण गर्न, र अन्तरक्रियाको स्थिति व्यवस्थापन गर्न प्रयोग गर्न सकिन्छ। यहाँ एउटा थ्रेडको उदाहरण छ:

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

    अघिल्लो कोडमा, एउटा थ्रेड सिर्जना गरिएको छ। त्यसपछि, थ्रेडमा एउटा सन्देश पठाइन्छ। `create_and_process_run` कल गरेर, थ्रेडमा एजेन्टलाई काम गर्न सोधिन्छ। अन्त्यमा, एजेन्टको प्रतिक्रिया हेर्न सन्देशहरू ल्याइँन्छ र लग गरिन्छ। सन्देशहरूले प्रयोगकर्ता र एजेन्टबीचको कुराकानीको प्रगति सूचित गर्दछन्। यो पनि बुझ्न महत्त्वपूर्ण छ कि सन्देशहरू विभिन्न प्रकारका हुन सक्छन् जस्तै पाठ, छवि, वा फाइल; अर्थात् एजेन्टको कामले उदाहरणका लागि छवि वा पाठ प्रतिक्रिया उत्पन्न गरेको हुन सक्छ। विकासकर्ताका रूपमा, तपाईंले त्यसपछि यस जानकारीलाई प्रतिक्रिया थप प्रक्रियाका लागि प्रयोग गर्न वा प्रयोगकर्तालाई प्रस्तुत गर्न प्रयोग गर्न सक्नुहुन्छ।

- **Microsoft Agent Framework सँग एकीकृत हुन्छ**। Azure AI Agent Service Microsoft Agent Framework सँग सहज रूपमा काम गर्छ, जसको अर्थ तपाईं `AzureAIProjectAgentProvider` प्रयोग गरेर एजेन्टहरू निर्माण गर्न र उत्पादन परिदृश्यहरूका लागि Agent Service मार्फत तिनीहरूलाई तैनात गर्न सक्नुहुन्छ।

**प्रयोग केसहरू**: Azure AI Agent Service ती एन्त्रप्राइज अनुप्रयोगहरूका लागि डिजाइन गरिएको हो जसलाई सुरक्षित, स्केलेबल, र लचकदार AI एजेन्ट तैनाती आवश्यक हुन्छ।

## यी दृष्टिकोणहरूबीच के फरक छ?
 
यो सुनिन सक्छ कि ओभरलैप छ, तर तिनीहरूको डिजाइन, क्षमताहरू, र लक्षित प्रयोग केसहरूको सन्दर्भमा केही प्रमुख फरकहरू छन्:
 
- **Microsoft Agent Framework (MAF)**: AI एजेन्टहरू निर्माण गर्नका लागि उत्पादन-तयार SDK हो। यसले उपकरण कल, संवाद व्यवस्थापन, र Azure पहिचान एकीकरण सहित एजेन्टहरू सिर्जना गर्ने लागि प्रवाहशील API प्रदान गर्छ।
- **Azure AI Agent Service**: एजेन्टहरूको लागि Azure Foundry मा प्लेटफर्म र तैनाती सेवा हो। यसले Azure OpenAI, Azure AI Search, Bing Search र कोड कार्यान्वयन जस्ता सेवाहरूमा बिल्ट-इन कनेक्टिभिटी प्रदान गर्छ।
 
अझै सुनिश्चित नभए?

### प्रयोग केसहरू
 
केही सामान्य प्रयोग केसहरू मार्फत हेरौं कि कुन कुन अवस्थामा कुन रोज्ने उपयुक्त हुन सक्छ:
 
> प्रश्न: म उत्पादन AI एजेन्ट अनुप्रयोगहरू निर्माण गर्दैछु र छिटो सुरु गर्न चाहन्छु
>

>उत्तर: Microsoft Agent Framework उत्कृष्ट विकल्प हो। यसले `AzureAIProjectAgentProvider` मार्फत सरल, Python-शैली API प्रदान गर्छ जसले तपाईंलाई केही लाइनको कोडमा उपकरण र निर्देशनहरूसहित एजेन्टहरू परिभाषित गर्न दिन्छ।

>प्रश्न: मैले Azure एकीकरणहरू जस्तै Search र कोड कार्यान्वयन सहित एन्त्रप्राइज-ग्रेड तैनाती चाहिन्छ
>
> उत्तर: Azure AI Agent Service सबैभन्दा उपयुक्त छ। यो एउटा प्लेटफर्म सेवा हो जसले बहु मोडेलहरू, Azure AI Search, Bing Search र Azure Functions का लागि बिल्ट-इन क्षमताहरू प्रदान गर्छ। Foundry Portal मा आफ्ना एजेन्टहरू बनाउन र तिनीहरूलाई स्केलमा तैनात गर्न सरल बनाउँछ।
 
> प्रश्न: म अझै पनि अलमलमा छु, मलाई केवल एउटा विकल्प दिनुहोस्
>
> उत्तर: Microsoft Agent Framework बाट सुरु गर्नुहोस् आफ्नो एजेन्टहरू निर्माण गर्न, र उत्पादनमा तैनाती र स्केल चाहिएको बेलामा Azure AI Agent Service प्रयोग गर्नुहोस्। यस दृष्टिकोणले तपाईंलाई एजेन्ट लॉजिकमा छिटो पुनरावृत्ति गर्न अनुमति दिन्छ भने एन्त्रप्राइज तैनातीको लागि स्पष्ट मार्ग पनि राख्छ।
 
मुख्य फरकहरू संक्षेपमा तालिकामा हेर्नुहोस्:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | उपकरण कलसहित प्रवाहशील एजेन्ट SDK | Agents, Tools, Azure Identity | AI एजेन्टहरू निर्माण, उपकरण प्रयोग, बहु-चरण कार्यप्रवाहहरू |
| Azure AI Agent Service | लचकदार मोडेलहरू, एन्त्रप्राइज सुरक्षा, कोड जेनरेशन, उपकरण कल | Modularity, Collaboration, Process Orchestration | सुरक्षित, स्केलेबल, र लचकदार AI एजेन्ट तैनाती |

## के म मेरो अवस्थित Azure इकोसिस्टमका उपकरणहरू सिधै एकीकृत गर्न सक्छु, वा मलाई स्वतन्त्र समाधानहरू आवश्यक छन्?
उत्तर हो — तपाईंले आफ्नो अवस्थित Azure इकोसिस्टम उपकरणहरू Azure AI Agent Service सँग सिधै एकीकृत गर्न सक्नुहुन्छ, किनकि यो अन्य Azure सेवाहरू सँग सहज रूपमा काम गर्ने गरी निर्माण गरिएको हो। उदाहरणका लागि तपाईं Bing, Azure AI Search, र Azure Functions एकीकृत गर्न सक्नुहुन्छ। Microsoft Foundry सँग पनि गहिरो एकीकरण छ।

The Microsoft Agent Framework also integrates with Azure services through `AzureAIProjectAgentProvider` and Azure identity, letting you call Azure services directly from your agent tools.

## नमूना कोडहरू

- Python: [एजेन्ट फ्रेमवर्क](./code_samples/02-python-agent-framework.ipynb)
- .NET: [एजेन्ट फ्रेमवर्क](./code_samples/02-dotnet-agent-framework.md)

## AI Agent Frameworks सम्बन्धी थप प्रश्नहरू छन्?

अन्य सिक्नेहरूसँग भेटघाट गर्न, कार्यालय समयहरूमा भाग लिन र तपाईंका AI Agents सम्बन्धी प्रश्नहरूको जवाफ पाउन [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मा सामेल हुनुहोस्।

## सन्दर्भहरू

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## अघिल्लो पाठ

[AI एजेन्टहरू र एजेन्ट प्रयोग केसहरूको परिचय](../01-intro-to-ai-agents/README.md)

## अर्को पाठ

[एजेण्टिक डिजाइन ढाँचाहरू बुझ्नुहोस्](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौँ, तथापि कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुनसक्छ। मूल दस्तावेजलाई यसको मूल भाषामा अधिकृत स्रोत मानिनु पर्दछ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->