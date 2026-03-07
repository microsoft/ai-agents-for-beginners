[![एआई एजेन्ट फ्रेमवर्कहरू अन्वेषण](../../../translated_images/ne/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(उपरको छविमा क्लिक गरेर यो पाठको भिडियो हेर्नुहोस्)_

# एआई एजेन्ट फ्रेमवर्कहरू अन्वेषण

एआई एजेन्ट फ्रेमवर्कहरू ती सफ्टवेयर प्लेटफर्महरू हुन् जसले एआई एजेन्टहरूको सिर्जना, तैनाती, र व्यवस्थापनलाई सरल बनाउँछन्। यी फ्रेमवर्कहरूले विकासकर्ताहरूलाई पूर्व-निर्मित कम्पोनेन्टहरू, अमूर्तताहरू, र उपकरणहरू प्रदान गर्दछन् जसले जटिल एआई प्रणालीहरूको विकासलाई सहज बनाउँछ।

यी फ्रेमवर्कहरूले विकासकर्ताहरूलाई साझा चुनौतीहरूका लागि मानकीकृत दृष्टिकोणहरू प्रदान गरेर तिनीहरूका अनुप्रयोगका अनौंठा पक्षहरूमा केन्द्रित हुन मद्दत गर्छन्। तिनीहरूले स्केलेबिलिटी, पहुँचयोग्यता, र दक्षता बढाउँछन् एआई प्रणालीहरू निर्माण गर्दा।

## परिचय 

यस पाठले समेट्नेछ:

- एआई एजेन्ट फ्रेमवर्कहरू के हुन् र यीले विकासकर्ताहरूलाई के उपलब्ध गराउँछन्?
- टोलीहरूले यी प्रयोग गरेर कसरी छिटो प्रोटोटाइप बनाउन, दोहोर्याउन, र आफ्ना एजेन्टको क्षमताहरू सुधार गर्न सक्छन्?
- Microsoft द्वारा बनाइएका फ्रेमवर्क र उपकरणहरू (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent सेवा</a> र <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft एजेन्ट फ्रेमवर्क</a>) बीच के फरक छ?
- के म मेरो विद्यमान Azure इकोसिस्टम उपकरणहरूलाई प्रत्यक्ष रूपमा एकीकृत गर्न सक्छु, वा मलाई स्वतन्त्र समाधानहरू आवश्यक पर्छ?
- Azure AI Agent सेवा के हो र यसले मलाई कसरी सहयोग गर्दछ?

## सिकाइ लक्ष्यहरू

यस पाठका लक्ष्यहरू तपाइँलाई बुझ्न मद्दत गर्नु हुन्:

- एआई विकासमा एआई एजेन्ट फ्रेमवर्कहरूको भूमिका।
- बुद्धिमान एजेन्टहरू निर्माण गर्न एआई एजेन्ट फ्रेमवर्कहरू कसरी प्रयोग गर्ने।
- एआई एजेन्ट फ्रेमवर्कहरूले सक्षम गर्ने प्रमुख क्षमताहरू।
- Microsoft एजेन्ट फ्रेमवर्क र Azure AI Agent सेवाबीचका फरकहरू।

## एआई एजेन्ट फ्रेमवर्कहरू के हुन् र यीले विकासकर्ताहरूलाई के गर्न सक्षम बनाउँछन्?

परम्परागत एआई फ्रेमवर्कहरूले तपाइँलाई तपाइँका अनुप्रयोगहरूमा एआई एकीकृत गर्न र यी अनुप्रयोगहरूलाई तलका तरिकाहरूले सुधार गर्न मद्दत गर्न सक्छन्:

- **व्यक्तिकरण**: एआईले प्रयोगकर्ताको व्यवहार र प्राथमिकताहरू विश्लेषण गरेर व्यक्तिगत सिफारिसहरू, सामग्री, र अनुभवहरू प्रदान गर्न सक्छ।
उदाहरण: Netflix जस्ता स्ट्रिमिङ सेवाहरूले हेर्ने इतिहासका आधारमा चलचित्र र शो सिफारिस गर्न एआई प्रयोग गर्दछन्, जसले प्रयोगकर्ता संलग्नता र सन्तुष्टिलाई बढाउँछ।
- **स्वचालन र दक्षता**: एआईले दोहोरिने कार्यहरू स्वचालित गर्न, कार्यप्रवाहहरू सरलीकृत गर्न, र सञ्चालनमा दक्षता सुधार गर्न सक्छ।
उदाहरण: ग्राहक सेवा अनुप्रयोगहरूले सामान्य सोधपुछहरू ह्यान्डल गर्न एआई-समर्थित च्याटबटहरू प्रयोग गर्दछन्, जसले जवाफ समय घटाउँछ र जटिल समस्याहरूका लागि मानवीय एजेन्टहरूलाई स्वतन्त्र बनाउँछ।
- **उपयुक्त प्रयोगकर्ता अनुभव**: एआईले आवाज पहिचान, प्राकृतिक भाषा प्रशोधन, र पूर्वानुमान टेक्स्ट जस्ता बौद्धिक सुविधाहरू प्रदान गरेर समग्र प्रयोगकर्ता अनुभव सुधार गर्न सक्छ।
उदाहरण: Siri र Google Assistant जस्ता भर्चुअल सहायकहरूले आवाज आदेशहरू बुझ्न र जवाफ दिन एआई प्रयोग गर्दछन्, जसले प्रयोगकर्ताहरूलाई उपकरणहरूसँग सजिलै अन्तरक्रिया गर्न मद्दत गर्छ।

### सबै कुरा राम्रो शुनिन्छ, त्यसो भए हामीलाई एआई एजेन्ट फ्रेमवर्क किन चाहिन्छ?

एआई एजेन्ट फ्रेमवर्कहरू केवल एआई फ्रेमवर्कहरू भन्दा फरक कुरा प्रतिनिधित्व गर्छन्। तिनीहरू ती बुद्धिमान एजेन्टहरू सिर्जना गर्न डिजाइन गरिएका छन् जुन प्रयोगकर्ताहरू, अन्य एजेन्टहरू, र वातावरणसँग अन्तरक्रिया गरी विशेष लक्ष्यहरू हासिल गर्न सक्छन्। यी एजेन्टहरूले स्वतन्त्र व्यवहार प्रदर्शन गर्न, निर्णय लिन र परिवर्तनशील अवस्थाहरूमा अनुकूल हुन सक्छन्। एआई एजेन्ट फ्रेमवर्कहरूले सक्षम गर्ने केही प्रमुख क्षमताहरू हेरौं:

- **एजेन्ट सहकार्य र समन्वय**: बहु एआई एजेन्टहरू सिर्जना गर्न सक्षम पार्दछ जसले सँगै काम गर्न, सञ्चार गर्न, र जटिल कार्यहरू समाधान गर्न समन्वय गर्न सक्छन्।
- **कार्य स्वचालन र व्यवस्थापन**: बहु-चरण कार्यप्रवाहहरू स्वचालन गर्ने, कार्य सुम्पनु र एजेन्टहरू बीच गतिशील कार्य व्यवस्थापनका लागि मेकानिज्महरू प्रदान गर्छ।
- **प्रासंगिक बुझाइ र अनुकूलन**: एजेन्टहरूलाई प्रसंग बुझ्ने, परिवर्तनशील वातावरणमा अनुकूल हुने, र रियल-टाइम जानकारीको आधारमा निर्णय लिन सक्षम बनाउँछ।

सङ्क्षेपमा, एजेन्टहरूले तपाइँलाई बढी गर्न अनुमति दिन्छन् — स्वचालनलाई अर्को स्तरसम्म लाने, वातावरणबाट सिक्ने र अनुकूल हुने थप बुद्धिमान प्रणालीहरू सिर्जना गर्ने।

## कसरी छिटो प्रोटोटाइप बनाउने, दोहोर्याउने, र एजेन्टको क्षमताहरू सुधार्ने?

यो छिटो परिवर्तन हुने क्षेत्र हो, तर धेरै एआई एजेन्ट फ्रेमवर्कहरूमा साझा केही तत्वहरू छन् जसले तपाइँलाई छिटो प्रोटोटाइप र दोहोर्याउन मद्दत गर्छन् — मुख्यतः मोडुलर कम्पोनेन्टहरू, सहकारी उपकरणहरू, र रियल-टाइम सिकाइ। यीमा डुब्नुस्:

- **मोडुलर कम्पोनेन्टहरू प्रयोग गर्नुहोस्**: एआई SDKs ले AI र मेमोरी कनेक्टर्स, फङ्सन कलिंग प्रयोग गरेर प्राकृतिक भाषा वा कोड प्लगइनहरू, प्रॉम्प्ट टेम्प्लेटहरू, र थप जस्ता पूर्व-निर्मित कम्पोनेन्टहरू प्रस्ताव गर्दछन्।
- **सहयोगी उपकरणहरू प्रयोग गर्नुहोस्**: एजेन्टहरूलाई विशिष्ट भूमिका र कार्यहरूसँग डिजाइन गरेर तिनीहरूलाई सहकारी कार्यप्रवाहहरू परीक्षण र परिमार्जन गर्न सक्षम बनाउनुहोस्।
- **वास्तविक समयमा सिक्नुहोस्**: तिनमा प्रतिकृया लूपहरू लागू गर्नुहोस् जहाँ एजेन्टहरूले अन्तरक्रियाबाट सिक्छन् र तिनको व्यवहार गतिशील रूपमा समायोजन गर्छन्।

### मोडुलर कम्पोनेन्टहरू प्रयोग गर्नुहोस्

Microsoft एजेन्ट फ्रेमवर्क जस्ता SDKs ले AI कनेक्टर्स, टुल परिभाषाहरू, र एजेन्ट व्यवस्थापन जस्ता पूर्व-निर्मित कम्पोनेन्टहरू प्रस्ताव गर्दछन्।

**टीमहरू यसलाई कसरी प्रयोग गर्न सक्छन्**: टीमहरूले ती कम्पोनेन्टहरू छिटो जोडेर कुनै कार्यशील प्रोटोटाइप बनाउन सक्छन् बिना सुरुदेखि नै बनाउनु पर्ने, जसले छिटो प्रयोग र दोहोर्याउने सम्भावना दिन्छ।

**व्यावहारिक रूपमा यसले कसरी काम गर्छ**: तपाइँ प्रयोगकर्ताबाट सूचना निकालनको लागि पूर्व-निर्मित पार्सर प्रयोग गर्न सक्नुहुन्छ, डाटा भण्डारण र पुन:प्राप्तिका लागि मेमोरी मोड्युल प्रयोग गर्न सक्नुहुन्छ, र प्रयोगकर्तासँग अन्तरक्रिया गर्न प्रॉम्प्ट जेनेरेटर प्रयोग गर्न सक्नुहुन्छ — ती सबै बिना सुरुदेखि नै यी कम्पोनेन्टहरू निर्माण गर्नुपर्दा।

**उदाहरण कोड**. तपाइँ Microsoft एजेन्ट फ्रेमवर्क कसरी प्रयोग गरेर `AzureAIProjectAgentProvider` सँग मोड्युलर तरिकाले मोडललाई प्रयोगकर्ताको इनपुटमा टुल कलिङ्गका साथ प्रतिक्रिया गराउन सकिन्छ भन्ने उदाहरण हेरौं:

``` python
# माइक्रोसफ्ट एजेन्ट फ्रेमवर्क पायथन उदाहरण

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# यात्रा बुक गर्नको लागि नमूना उपकरण फंक्शन परिभाषित गर्नुहोस्
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
    # उदाहरण आउटपुट: January 1, 2025 मा न्यूयोर्कको लागि तपाईंको उडान सफलतापूर्वक बुक गरिएको छ। सुरक्षित यात्रा गर्नुहोस्! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

यस उदाहरणबाट तपाइँले देख्न सक्नुहुन्छ कि कसरी पूर्व-निर्मित पार्सर प्रयोग गरेर प्रयोगकर्ताको इनपुटबाट महत्वपूर्ण जानकारी निकाल्न सकिन्छ, जस्तै उडान बुकिङ अनुरोधको मूल स्थान, गन्तव्य, र मिति। यो मोडुलर दृष्टिकोणले तपाइँलाई उच्च-स्तरीय तर्कमा केन्द्रित हुन अनुमति दिन्छ।

### सहयोगी उपकरणहरू प्रयोग गर्नुहोस्

Microsoft एजेन्ट फ्रेमवर्क जस्ता फ्रेमवर्कहरूले बहु एजेन्टहरू सिर्जना गर्न र तिनीहरूलाई सँगै काम गराउन सहज बनाउँछन्।

**टीमहरू यसलाई कसरी प्रयोग गर्न सक्छन्**: टीमहरूले विशिष्ट भूमिका र कार्यहरू भएका एजेन्टहरू डिजाइन गर्न सक्छन्, जसले तिनीहरूलाई सहकारी कार्यप्रवाहहरू परीक्षण र परिमार्जन गर्न र समग्र प्रणाली दक्षता सुधार गर्न सक्षम बनाउँछ।

**व्यावहारिक रूपमा यसले कसरी काम गर्छ**: तपाइँ एजेन्टहरूको टोली सिर्जना गर्न सक्नुहुन्छ जहाँ प्रत्येक एजेन्टसँग विशेष कार्य हुनेछ, जस्तै डाटा पुन:प्राप्ति, विश्लेषण, वा निर्णय-निर्माण। यी एजेन्टहरूले सामान्य लक्ष्य, जस्तै प्रयोगकर्ताको प्रश्नको उत्तर दिनु वा कुनै कार्य पूरा गर्नुका लागि सञ्चार र जानकारी साझेदारी गर्न सक्छन्।

**उदाहरण कोड (Microsoft Agent Framework)**:

```python
# माइक्रोसफ्ट एजेन्ट फ्रेमवर्क प्रयोग गरेर सँगै काम गर्ने धेरै एजेन्टहरू सिर्जना गर्दै

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# डाटा पुन:प्राप्ति एजेन्ट
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

# कार्यमा एजेन्टहरूलाई पालोमा चलाउनुहोस्
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

पहिलेको कोडमा तपाइँ देख्नुहुनेछ कसरी बहु एजेन्टहरूले सँगै काम गरेर डाटा विश्लेषण गर्ने कार्य सिर्जना गर्न सकिन्छ। प्रत्येक एजेन्टले विशेष फङ्सन प्रदर्शन गर्दछ, र चाहिएको नतिजा हासिल गर्न एजेन्टहरूको समन्वयले कार्य सञ्चालन गर्दछ। विशेष भूमिकाहरू भएका समर्पित एजेन्टहरू सिर्जना गरेर तपाइँ कार्य दक्षता र प्रदर्शन सुधार गर्न सक्नुहुन्छ।

### वास्तविक समयमा सिक्नुहोस्

उन्नत फ्रेमवर्कहरूले वास्तविक-समय प्रसंग बुझाइ र अनुकूलनका लागि क्षमता दिन्छन्।

**टीमहरू यसलाई कसरी प्रयोग गर्न सक्छन्**: टीमहरूले तिनमा प्रतिकृया लूपहरू लागू गर्न सक्छन् जहाँ एजेन्टहरूले अन्तरक्रियाबाट सिक्छन् र आफ्नो व्यवहार गतिशील रूपमा समायोजन गर्छन्, जसले निरन्तर सुधार र क्षमता परिष्करणतर्फ लैजान्छ।

**व्यावहारिक रूपमा यसले कसरी काम गर्छ**: एजेन्टहरूले प्रयोगकर्ता प्रतिकृया, वातावरणीय डाटा, र कार्य नतिजाहरू विश्लेषण गरेर आफ्नो ज्ञान आधार अपडेट गर्न, निर्णय-निर्माण एल्गोरिदम समायोजन गर्न, र समयसँगै प्रदर्शन सुधार गर्न सक्छन्। यो दोहोरिने सिकाइ प्रक्रिया एजेन्टहरूलाई परिवर्तनशील अवस्थाहरू र प्रयोगकर्ता प्राथमिकताहरूमा अनुकूल हुन सक्षम बनाउँछ, जसले समग्र प्रणाली प्रभावकारिता बढाउँछ।

## Microsoft एजेन्ट फ्रेमवर्क र Azure AI Agent सेवाबीच के फरक छन्?

यी दृष्टिकोणहरू तुलना गर्ने धेरै तरिकाहरू छन्, तर तिनीहरूको डिजाइन, क्षमताहरू, र लक्षित प्रयोग केसहरूको हिसाबले केही मुख्य फरकहरू हेरौं:

## Microsoft एजेन्ट फ्रेमवर्क (MAF)

Microsoft एजेन्ट फ्रेमवर्कले `AzureAIProjectAgentProvider` प्रयोग गरेर एआई एजेन्टहरू निर्माण गर्नका लागि एक सरल SDK प्रदान गर्छ। यसले विकासकर्ताहरूलाई Azure OpenAI मोडेलहरू प्रयोग गरेर उपकरण कलिङ्ग, संवाद व्यवस्थापन, र Azure पहिचानमार्फत एेन्टर्प्राइज-ग्रेड सुरक्षा सहित एजेन्टहरू सिर्जना गर्न सक्षम बनाउँछ।

**प्रयोग केसहरू**: उपकरण प्रयोग, बहु-चरण कार्यप्रवाहहरू, र एंटरप्राइज़ एकीकरण सिनारियोहरूसँग उत्पादन-तयार एआई एजेन्टहरू निर्माण गर्ने।

यहाँ Microsoft एजेन्ट फ्रेमवर्कका केही महत्वपूर्ण कोर अवधारणाहरू छन्:

- **Agents**. एक एजेन्ट `AzureAIProjectAgentProvider` मार्फत सिर्जना गरिन्छ र नाम, निर्देशनहरू, र उपकरणहरूसहित कन्फिगर गरिन्छ। एजेन्टले:
  - **प्रयोगकर्ता सन्देशहरू प्रशोधन** गर्न र Azure OpenAI मोडेलहरू प्रयोग गरेर प्रतिक्रियाहरू उत्पन्न गर्न सक्छ।
  - **स्वचालित रूपमा टुलहरू कल** गर्न सक्छ कुराकानीको प्रसंगको आधारमा।
  - **बहु अन्तरक्रियाहरूमा वार्तालाप अवस्था कायम** राख्न सक्छ।

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

- **Tools**. फ्रेमवर्कले एजेन्टले स्वचालित रूपमा बोलाउन सक्ने Python फङ्सनहरू रूपमा उपकरणहरू परिभाषित गर्न समर्थन गर्दछ। एजेन्ट सिर्जना गर्दा उपकरणहरू दर्ता गरिन्छ:

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

- **बहु-एजेन्ट समन्वय**. तपाइँ फरक विशेषज्ञताहरू भएका बहु एजेन्टहरू सिर्जना गरी तिनीहरूको काम समन्वय गर्न सक्नुहुन्छ:

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

- **Azure पहिचान एकीकरण**. फ्रेमवर्कले सुरक्षित, कुञ्जी रहित प्रमाणीकरणको लागि `AzureCliCredential` (वा `DefaultAzureCredential`) प्रयोग गर्दछ, जसले API कुञ्जीहरू प्रत्यक्ष रूपमा व्यवस्थापन गर्न आवश्यकतालाई हटाउँछ।

## Azure AI Agent सेवा

Azure AI Agent सेवा हालै थपिएको सेवा हो, जुन Microsoft Ignite 2024 मा परिचित गराइयो। यसले अधिक लचिलो मोडेलहरू जस्तै Llama 3, Mistral, र Cohere जस्ता खुला स्रोत LLMs लाई प्रत्यक्ष कल गर्ने क्षमता सहित एआई एजेन्टहरूको विकास र तैनातीको अनुमति दिन्छ।

Azure AI Agent सेवाले बलियो एंटरप्राइज सुरक्षा संयन्त्रहरू र डाटा भण्डारण विधिहरू प्रदान गर्दछ, जसले यसलाई एंटरप्राइज अनुप्रयोगहरूको लागि उपयुक्त बनाउँछ।

यो आउट-ऑफ-द-बक्स Microsoft एजेन्ट फ्रेमवर्कसँग काम गर्दछ एजेन्टहरू निर्माण र तैनातीका लागि।

यो सेवा हाल Public Preview मा छन् र एजेन्टहरू निर्माण गर्न Python र C# लाई समर्थन गर्छ।

Azure AI Agent Service Python SDK प्रयोग गरेर, हामी प्रयोगकर्ता-परिभाषित उपकरणसहित एजेन्ट सिर्जना गर्न सक्छौं:

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

Azure AI Agent सेवाको निम्न मुख्य अवधारणाहरू छन्:

- **Agent**. Azure AI Agent सेवा Microsoft Foundry सँग एकीकरण गर्दछ। AI Foundry भित्र, एक AI एजेन्ट "स्मार्ट" माइक्रोसर्भिसको रूपमा कार्य गर्दछ जसलाई प्रश्नहरूको उत्तर दिन (RAG), कार्यहरू प्रदर्शन गर्न, वा पूर्ण रूपमा कार्यप्रवाहहरू स्वचालित गर्न प्रयोग गर्न सकिन्छ। यसले जेनेरेटिभ AI मोडेलहरूको शक्ति र वास्तविक-विश्व डेटा स्रोतहरू पहुँच गर्न र अन्तरक्रिया गर्न अनुमति दिने उपकरणहरू संयोजन गरेर यो हासिल गर्दछ। यहाँ एजेन्टको उदाहरण छ:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    यस उदाहरणमा, `gpt-4o-mini` मोडेल, नाम `my-agent`, र निर्देशनहरू `You are helpful agent` सहित कुरैएको एजेन्ट सिर्जना गरिएको छ। एजेन्टलाई कोड व्याख्या कार्यहरू प्रदर्शन गर्नका लागि उपकरणहरू र स्रोतहरूसँग सुसज्जित गरिएको छ।

- **थ्रेड र सन्देशहरू**. थ्रेड अर्को महत्वपूर्ण अवधारणा हो। यसले एजेन्ट र प्रयोगकर्ताबीचको वार्तालाप वा अन्तरक्रियालाई प्रतिनिधित्व गर्छ। थ्रेडहरू वार्तालापको प्रगति ट्र्याक गर्न, प्रसंग जानकारी भण्डारण गर्न, र अन्तरक्रियाको अवस्था व्यवस्थापन गर्न प्रयोग गर्न सकिन्छ। यहाँ थ्रेडको उदाहरण छ:

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

    अघिल्लो कोडमा, एउटा थ्रेड सिर्जना गरिएको छ। त्यसपछि, थ्रेडमा सन्देश पठाइन्छ। `create_and_process_run` कल गरेर, एजेन्टलाई थ्रेडमा काम गर्न भनिन्छ। अन्ततः, सन्देशहरू प्राप्त गरेर एजेन्टको प्रतिक्रिया हेर्न लग गरिएको छ। सन्देशहरूले प्रयोगकर्ता र एजेन्ट बीचको वार्तालापको प्रगतिलाई संकेत गर्छ। सन्देशहरू विभिन्न प्रकारका हुन सक्छन् जस्तै टेक्स्ट, इमेज, वा फाइल — अर्थ, एजेन्टको कामले कुनै इमेज वा टेक्स्ट प्रतिक्रिया उत्पादन गर्न सक्छ। विकासकर्ताको रूपमा, तपाइँले यो जानकारी प्रयोग गरी प्रतिक्रिया थप प्रक्रिया गर्न वा प्रयोगकर्तालाई प्रस्तुत गर्न सक्नुहुन्छ।

- **Microsoft एजेन्ट फ्रेमवर्कसँग एकीकरण**. Azure AI Agent सेवा Microsoft एजेन्ट फ्रेमवर्कसँग सहज रूपमा काम गर्छ, जसले मतलब तपाइँ `AzureAIProjectAgentProvider` प्रयोग गरेर एजेन्टहरू निर्माण गरी तिनीहरूलाई उत्पादन सिनारियोका लागि Agent Service मार्फत तैनात गर्न सक्नुहुन्छ।

**प्रयोग केसहरू**: Azure AI Agent सेवा सुरक्षित, स्केलेबल, र लचिलो एआई एजेन्ट तैनाती आवश्यक पर्ने एंटरप्राइज अनुप्रयोगहरूको लागि डिजाइन गरिएको हो।

## यी दृष्टिकोणहरू बीच के फरक छ?
 
तपाइँले ओभरल्याप सुनिन सक्छ, तर डिजाइन, क्षमताहरू, र लक्षित प्रयोग केसहरूका हिसाबले केही प्रमुख फरकहरू छन्:
 
- **Microsoft एजेन्ट फ्रेमवर्क (MAF)**: एआई एजेन्टहरू निर्माण गर्नका लागि उत्पादन-तयार SDK हो। यसले टुल कलिङ्ग, संवाद व्यवस्थापन, र Azure पहिचान एकीकरणसहित एजेन्टहरू सिर्जना गर्ने सुविधाजनक API प्रदान गर्छ।
- **Azure AI Agent सेवा**: एजेन्टहरूको लागि Azure Foundry मा प्ल्याटफर्म र तैनाती सेवा हो। यसले Azure OpenAI, Azure AI Search, Bing Search र कोड निष्पादन जस्ता सेवाहरूमा बिल्ट-इन कनेक्टिविटी प्रदान गर्दछ।
 
अझै कन्फ्युज भएको?

### प्रयोग केसहरू
 
हामीले केही सामान्य प्रयोग केसहरू मार्फत तपाइँलाई मद्दत गर्न सक्छौं कि छैन हेर्नुहोस्:
 
> Q: म उत्पादन-तयार एआई एजेन्ट अनुप्रयोगहरू निर्माण गर्दैछु र छिटो सुरु गर्न चाहन्छु
>
>
>A: Microsoft एजेन्ट फ्रेमवर्क उत्कृष्ट विकल्प हो। यसले `AzureAIProjectAgentProvider` मार्फत सरल, Python-मैत्री API प्रदान गर्छ जसले तपाइँलाई केही लाइनको कोडमा उपकरणहरू र निर्देशनहरूसहित एजेन्ट परिभाषित गर्न दिन्छ।

>Q: मलाई Azure एकीकरण जस्ता Search र कोड निष्पादनसँग एंटरप्राइज़-ग्रेड तैनाती चाहिन्छ
>
> A: Azure AI Agent सेवा उत्तम उपयुक्त छ। यो एउटा प्लेटफर्म सेवा हो जसले बहु मोडेलहरू, Azure AI Search, Bing Search र Azure Functions का लागि बिल्ट-इन क्षमताहरू प्रदान गर्छ। यसले Foundry पोर्टलमा तपाइँका एजेन्टहरू बनाउन र तिनलाई स्केलमा तैनात गर्न सजिलो बनाउँछ।
 
> Q: म अझै पनि भ्रमित छु, केवल एउटा विकल्प दिनुहोस्
>
> A: Microsoft एजेन्ट फ्रेमवर्कबाट सुरु गर्नुहोस् तपाइँका एजेन्टहरू निर्माण गर्न, र त्यसपछि उत्पादनमा तैनाती र स्केलिङ आवश्यक पर्दा Azure AI Agent सेवा प्रयोग गर्नुहोस्। यसले तपाइँलाई एजेन्ट तर्कमा छिटो दोहोर्याउन दिन्छ जबकि एंटरप्राइज तैनातीतर्फ स्पष्ट बाटो पनि प्रदान गर्छ।
 
Let's summarize the key differences in a table:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool calling | Agents, Tools, Azure Identity | Building AI agents, tool use, multi-step workflows |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## के म मेरो विद्यमान Azure इकोसिस्टम उपकरणहरूलाई प्रत्यक्ष रूपमा एकीकृत गर्न सक्छु, वा मलाई स्वतन्त्र समाधानहरू आवश्यक पर्छ?
जवाफ हो, तपाईंले आफ्नो अवस्थित Azure परिसरी उपकरणहरू Azure AI Agent Service सँग सिधै एकीकृत गर्न सक्नुहुन्छ, विशेषगरी यो अन्य Azure सेवाहरूसँग सहज रूपमा काम गर्न बनाइएको छ। उदाहरणका लागि तपाईं Bing, Azure AI Search, र Azure Functions लाई एकीकृत गर्न सक्नुहुन्छ। Microsoft Foundry सँग पनि गहिरो एकीकरण छ।

Microsoft Agent Framework ले पनि `AzureAIProjectAgentProvider` र Azure identity मार्फत Azure सेवाहरूसँग एकीकृत हुन्छ, र यसले तपाईंलाई आफ्नो एजेन्ट उपकरणहरूबाट सिधै Azure सेवाहरू कल गर्न अनुमति दिन्छ।

## नमूना कोडहरू

- Python: [एजेन्ट फ्रेमवर्क](./code_samples/02-python-agent-framework.ipynb)
- .NET: [एजेन्ट फ्रेमवर्क](./code_samples/02-dotnet-agent-framework.md)

## AI एजेन्ट फ्रेमवर्कहरू सम्बन्धी थप प्रश्नहरू?

अन्य सिक्नेहरूसँग भेट गर्न, अफिस आवरहरूमा सहभागी हुन र आफ्नो AI एजेन्टहरू सम्बन्धी प्रश्नहरूको उत्तर पाउनको लागि [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मा सहभागी हुनुहोस्।

## सन्दर्भहरू

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent सेवा</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI प्रतिक्रियाहरू</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent सेवा</a>

## अघिल्लो पाठ

[AI एजेन्टहरू र एजेन्ट प्रयोग केसहरूको परिचय](../01-intro-to-ai-agents/README.md)

## अर्को पाठ

[एजेन्टिक डिजाइन ढाँचाहरू बुझ्ने](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अनिश्चितता हुन सक्छ। मूल दस्तावेजलाई त्यसको मूल भाषामा प्राधिकृत स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि भ्रम वा गलत व्याख्याका लागि हामी उत्तरदायी छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->