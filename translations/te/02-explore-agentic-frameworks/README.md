[![AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లను అన్వేషించడం](../../../translated_images/te/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ఈ పాఠం వీడియోను వీక్షించడానికి పై చిత్రాన్ని క్లిక్ చేయండి)_

# AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లను అన్వేషించండి

AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు AI ఏజెంట్‌ల సృష్టి, డిప్లాయ్‌మెంట్ మరియు నిర్వహణను సరళీకృతం చేసేందుకు రూపొందించిన సాఫ్ట్‌వేర్ ప్లాట్‌ఫారమ్‌లు. ఈ ఫ్రేమ్‌వర్క్‌లు అభివృద్ధికారులకు ముందుగా తయారుచేసిన కంపోనెంట్లు, అబ్స్ట్రాక్షన్లు మరియు సాధనాలను అందిస్తాయి, ఇవి క్లిష్టమైన AI వ్యవస్థల అభివృద్ధిని సరళీకృతం చేస్తాయి.

ఈ ఫ్రేమ్‌వర్క్‌లు అభివృద్ధికారులు వారి అప్లికేషన్ల ప్రత్యేక అంశాలపై దృష్టి పెట్టడానికి సహాయపడతాయి ఎందుకంటే అవి AI ఏజెంట్ అభివృద్ధిలోని సాధారణ సవాళ్ళకు ప్రమాణీకృత పద్ధతులను అందిస్తాయి. అవి స్కేలబిలిటీ, ప్రాప్త్యత మరియు సమర్థతను మెరుగుపరుస్తాయి.

## పరిచయం 

ఈ పాఠం కవర్ చేస్తుంది:

- AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు ఏమిటి మరియు అవి అభివృద్ధికారులు ఏమి సాధించగలరో?
- టీమ్‌లు వీటిని ఉపయోగించి ఎలా వేగంగా ప్రోటోటైప్ చేయగలరో, పునరావృతం చేసుకుని వారి ఏజెంట్ సామర్థ్యాలను మెరుగుపరచగలరో?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI ఏజెంట్ సర్వీస్</a> మరియు the <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft ఏజెంట్ ఫ్రేమ్‌వర్క్</a>) ద్వారా సృష్టించబడిన ఫ్రేమ్‌వర్క్‌లు మరియు సాధనాల మధ్య ఏమిటి తేడాలు?
- నేను నా ప్రస్తుత Azure పరిసర సాధనాలను నేరుగా ఇంటిగ్రేట్ చేయగలనా లేదా నాకు స్వతంత్ర పరిష్కారాలు అవసరమా?
- Azure AI Agents సర్వీస్ అంటే ఏమిటి మరియు ఇది నాకు ఎలా సహాయపడుతుంది?

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం ద్వారా మీరు అర్థం చేసుకోవడముకు సహాయపడాలి:

- AI అభివృద్ధిలో AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌ల పాత్ర.
- తెలివైన ఏజెంట్‌లను నిర్మించడానికి AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లను ఎలా వినియోగించుకోవడం.
- AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌ల ద్వారా అనుమతించబడే ముఖ్య సామర్థ్యాలు.
- Microsoft Agent Framework మరియు Azure AI Agent Service మధ్య తేడాలు.

## AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు ఏమిటి మరియు అవి అభివృద్ధికారులు ఏం చేయగలరో?

పారంపరిక AI ఫ్రేమ్‌వర్క్‌లు మీ యాప్స్‌లో AIని సమకూర్చడంలో మరియు ఈ యాప్స్‌ను క్రింది విధాలుగా మెరుగుపరచడంలో సహాయపడతాయి:

- **Personalization**: AI వినియోగదారుని ప్రవర్తన మరియు ఇష్టాలను విశ్లేషించి వ్యక్తిగతీకరించిన సిఫార్సులు, కంటెంట్ మరియు అనుభవాలను అందించగలదు.
  Example: Netflix వంటి స్ట్రీమింగ్ సేవలు వీక్షణ చరిత్ర ఆధారంగా సినిమాలు మరియు షోలను సిఫార్సు చేయడానికి AIను ఉపయోగిస్తాయి, తద్వారా వినియోగదారు పాల్గొనడం మరియు సంతృప్తి పెరుగుతుంది.
- **Automation and Efficiency**: AI పునరావృత పనులను автоматిక్‌గా నిర్వహించగలదు, వర్క్‌ఫ్లోలను సరళీకృతం చేయగలదు, మరియు ఆపరేషనల్ సమర్థతను మెరుగుపరచగలదు.
  Example: కస్టమర్ సర్వీస్ యాప్స్ సాధారణ విచారణలను నిర్వహించడానికి AI ఆధారిత చాట్‌బాట్‌లను ఉపయోగిస్తాయి, స్పందనా సమయాలను తగ్గిస్తూ మరియు మానవ ఏజెంట్స్‌ను క్లిష్ట సమస్యల కోసం విడుదల చేస్తాయి.
- **Enhanced User Experience**: AI వాయిస్ గుర్తింపు, నేచురల్ లాంగ్వేజ్ ప్రాసెసింగ్, ప్రెడిక్టివ్ టెక్స్ట్ వంటి తెలివైన ఫీచర్లు అందిస్తూ మొత్తం వినియోగదారు అనుభవాన్ని మెరుగుపరుస్తుంది.
  Example: Siri మరియు Google Assistant వంటి వర్చువల్ అసిస్టెంట్లు వాయిస్ కమాండులను అర్థం చేసుకుని ప్రతిస్పందించడానికి AI ను ఉపయోగిస్తాయి, ఇది వినియోగదారులకు వారి డివైస్‌లతో సులభంగా ఇంటరాక్ట్ చేయటంలో సహాయపడుతుంది.

### ఇది బాగానే అనిపిస్తుంది కదా, అయితే మనకు AI ఏజెంట్ ఫ్రేమ్‌వర్క్ ఎందుకు అవసరం?

AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు సాదారణ AI ఫ్రేమ్‌వర్క్‌లకు మించిన విధంగా ఉంటాయి. అవి వినియోగదారులతో, ఇతర ఏజెంట్‌లతో మరియు పర్యావరణంతో పరస్పరం చేయగలిగే, నిర్దిష్ట లక్ష్యాలను సాధించడానికి సరిపోయే తెలివైన ఏజెంట్‌ల సృష్టిని సాధ్యమచేస్తాయి. ఈ ఏజెంట్‌లు స్వయం అధికారులు ఉండవచ్చు, నిర్ణయాలు తీసుకోవచ్చు మరియు మారుతున్న పరిస్థితులకి అనుకూలంగా మారగలవు. AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు అనుమతించే కొన్ని ముఖ్య సామర్థ్యాలు ఇవే:

- **Agent Collaboration and Coordination**: బహుళ AI ఏజెంట్‌లను సృష్టించడం, అవి కలిసి పనిచేసి, కమ్యూనికేట్ చేసి, సమన్వయం చేయగలిగే విధానం.
- **Task Automation and Management**: బహుళ దశల వర్క్‌ఫ్లోలను ఆటోమేట్ చేయడానికి, పని делెగేషన్ చేయడానికి, మరియు ఏజెంట్‌ల మధ్య డైనమిక్ టాస్క్ మేనేజ్‌మెంట్‌ను అందించే Mexhanisms.
- **Contextual Understanding and Adaptation**: ఏజెంట్‌లకు సందర్భాన్ని అర్థం చేసుకోవడం, మారుతున్న పరిస్థితులకు అనుకూలంగా మార్చుకోవడం, మరియు రియల్-టైమ్ సమాచారం ఆధారంగా నిర్ణయాలు చేయగల శక్తిని ఇవ్వడం.

సారాంశంగా, ఏజెంట్‌లు మీకు ఎక్కువ పని చేయడానికి, ఆటోమేషన్‌ను తదుపరి స్థాయికి తీసుకెళ్ళడానికి, మరియు వారి పర్యావరణం నుండి నేర్చుకుని అనుకూలంగా మార్చుకునే మరింత తెలివైన వ్యవస్థలను సృష్టించడానికి వీలు కల్పిస్తాయి.

## ఏజెంట్ యొక్క సామర్థ్యాలను త్వరగా ప్రోటోటైప్ చేయడం, పునరావృతం చేయడం, మరియు మెరుగుపరచడం ఎలా?

ఇది వేగంగా మారే పరిసరం అయినప్పటికీ, చాలా AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లలో సాధారణంగా ఉండే కొన్ని అంశాలు ఉన్నాయి, ఇవి మీకు త్వరగా ప్రోటోటైపింగ్ మరియు పునరావృతం చేయడంలో సహాయపడతాయి: మాడ్యూలర్ కంపోనెంట్లు, సహకార సాధనాలు, మరియు రియల్-టైమ్ లెర్నింగ్. ఇవి వివరంగా చూద్దాం:

- **Use Modular Components**: AI SDKలు ముందుగా తయారుచేసిన కంపోనెంట్లు అందిస్తాయి—ఊదాహరణకు AI మరియు మెమరీ కనెక్టర్లు, నేచురల్ లాంగ్వేజ్ లేదా కోడ్ ప్లగిన్లు ఉపయోగించి ఫంక్షన్ కాలింగ్, ప్రాంప్ట్ టెంప్లేట్లు, మరియు మరిన్ని.
- **Leverage Collaborative Tools**: నిర్దిష్ట పాత్రలు మరియు పనులతో ఏజెంట్‌లను డిజైన్ చేయండి, ఇవి కలసి పనిచేసే వర్క్‌ఫ్లోలను పరీక్షించడానికి మరియు పరి�శీలించడానికి సహాయపడతాయి.
- **Learn in Real-Time**: ఏజెంట్‌లు నాడి పరస్పర చర్యల నుండి నేర్చుకుని వారి ప్రవర్తనను డైనమిక్గా సర్దుబాటు చేసుకునే ఫీడ్‌బ్యాక్ లూప్స్‌ను అమలు చేయండి.

### మాడ్యూలర్ కంపోనెంట్లను ఉపయోగించండి

Microsoft Agent Framework వంటి SDKలు AI కనెక్టర్లు, సాధన నిర్వచనలు మరియు ఏజెంట్ నిర్వహణ వంటి ప్రీ-బిల్ట్ కంపోనెంట్‌లను అందిస్తాయి.

**టీమ్‌లు ఇవి ఎలా ఉపయోగించగలవు**: టీమ్‌లు ఈ కంపోనెంట్లను త్వరగా కలిపి ఫంక్షనల్ ప్రోటోటైప్‌ను రూపొందించవచ్చు, మూలం నుండే ప్రారంభించాల్సిన అవసరం లేకుండా వేగంగా ప్రయోగించవచ్చు మరియు పునరావృతం చేయవచ్చు.

**ప్రాక్టికల్‌లో ఇది ఎలా పనిచేస్తుంది**: మీరు వినియోగదారు ఇన్పుట్ నుండి సమాచారం తీసివేయడానికి ప్రీ-బిల్ట్ పార్సర్‌ను, డేటా నిల్వ చేయడానికి మరియు పొందడానికి మెమరీ మాడ్యూల్‌ను, వినియోగదారులతో పరస్పర చర్య కోసం ప్రాంప్ట్ జనరేటర్‌ను వాడవచ్చు, ఇవన్నీ సామಾನ್ಯంగా మీరే ప్రారంభించాల్సిన అవసరం లేకుండా.

**Example code**. Let's look at an example of how you can use the Microsoft Agent Framework with `AzureAIProjectAgentProvider` to have the model respond to user input with tool calling:

``` python
# మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ పైథాన్ ఉదాహరణ

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# ప్రయాణం బుక్ చేసుకునేందుకు నమూనా టూల్ ఫంక్షన్‌ని నిర్వచించండి
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
    # ఉదాహరణ అవుట్‌పుట్: మీ జనవరి 1, 2025 న్యూయార్క్‌కు విమాన టికెట్ విజయవంతంగా బుక్ చేయబడింది. మంచి ప్రయాణం! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

What you can see from this example is how you can leverage a pre-built parser to extract key information from user input, such as the origin, destination, and date of a flight booking request. This modular approach allows you to focus on the high-level logic.

### సహకార సాధనాలను వినియోగించండి

Microsoft Agent Framework వంటి ఫ్రేమ్‌వర్క్‌లు కలిసి పనిచేసే బహుళ ఏజెంట్‌లను సృష్టించేందుకు సౌకర్యాన్ని కల్పిస్తాయి.

**టీమ్‌లు ఇవి ఎలా ఉపయోగించగలవు**: టీమ్‌లు నిర్దిష్ట పాత్రలు మరియు పనులతో ఏజెంట్‌లను డిజైన్ చేసి, సహకార వర్క్‌ఫ్లోలను పరీక్షించి మెరుగుపరచవచ్చు.

**ప్రాక్టికల్‌లో ఇది ఎలా పనిచేస్తుంది**: మీరు డేటా రిట్రీవల్, విశ్లేషణ లేదా నిర్ణయాల కోసం ప్రత్యేక ఫంక్షన్ ఉండే ఏజెంట్‌ల బృందాన్ని సృష్టించవచ్చు. ఈ ఏజెంట్‌లు పరస్పరం సమాచారాన్ని పంచుకొని ఒక సాధారణ లక్ష్యాన్ని సాధించడానికి సమన్వయం చేస్తాయి, ఉదాహరణకు వినియోగదారుని ప్రశ్నకు సమాధానం ఇవ్వడం లేదా ఒక టాస్క్‌ను పూర్తి చేయడం.

**Example code (Microsoft Agent Framework)**:

```python
# మైక్రోసాఫ్ట్ ఏజంట్ ఫ్రేమ్‌వర్క్‌ను ఉపయోగించి కలిసి పని చేసే అనేక ఏజెంట్లను సృష్టించడం

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# డేటా రిట్రీవల్ ఏజెంట్
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# డేటా విశ్లేషణ ఏజెంట్
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ఒక పనిపై ఏజెంట్లను వరసగా నిలిపి నిర్వహించడం
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

What you see in the previous code is how you can create a task that involves multiple agents working together to analyze data. Each agent performs a specific function, and the task is executed by coordinating the agents to achieve the desired outcome. By creating dedicated agents with specialized roles, you can improve task efficiency and performance.

### రియల్-టైమ్‌లో నేర్చుకోండి

అధునాతన ఫ్రేమ్‌వర్క్‌లు రియల్-టైమ్ సందర్భ అవగాహన మరియు అనుకూలత కోసం సామర్థ్యాలను అందిస్తాయి.

**టీమ్‌లు ఇవి ఎలా ఉపయోగించగలవు**: టీమ్‌లు ఏజెంట్‌లు పరస్పర చర్యల నుండి నేర్చుకునే మరియు వారి ప్రవర్తనను డైనమిక్గా సర్దుకుందే ఫీడ్‌బ్యాక్ లూప్‌లను అమలు చేయవచ్చు, ఇది సామర్థ్యాల నిరంతర మెరుగుదలకు దారితీయబడుతుంది.

**ప్రాక్టికల్‌లో ఇది ఎలా పనిచేస్తుంది**: ఏజెంట్‌లు వినియోగదారు ఫీడ్‌బ్యాక్, పర్యావరణ డేటా మరియు టాస్క్ అవుట్‌కమ్‌లను విశ్లేషించి వారి జ్ఞాన పేర్ష (knowledge base)ను అప్డేట్ చేయవచ్చు, నిర్ణయాల అల్గోరిథంలను సర్దుకోవచ్చు, తద్వారా సమయం పాటు పనితీరును మెరుగుపరుస్తాయి. ఈ పునరావృత నేర్చుకునే ప్రక్రియ ఏజెంట్‌లను మారుతున్న పరిస్థితులకు మరియు వినియోగదారు ప్రాధాన్యాలకి అనుకూలంగా మారేందుకు సహాయపడుతుంది.

## Microsoft Agent Framework మరియు Azure AI Agent Service మధ్య有什么 తేడాలు?

ఇవి పోలికలా అనిపించవచ్చు, కానీ రూపకల్పన, సామర్థ్యాలు మరియు లక్ష్య వినియోగాల పరంగా కొన్ని ముఖ్య తేడాలు ఉన్నాయి:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `AzureAIProjectAgentProvider` ఉపయోగించి AI ఏజెంట్‌లను నిర్మించడానికి సరళీకృత SDKని అందిస్తుంది. ఇది అభివృద్ధికారులకు Azure OpenAI మోడళ్లను వినియోగించి బిల్ట్-ఇన్ టూల్ కాలింగ్, సంభాషణ నిర్వహణ మరియు Azure ఐడెంటిటీ ద్వారా ఎంటర్‌ప్రైజ్-గ్రేడ్ భద్రతను ఉపయోగించి ఏజెంట్‌లను సృష్టించడానికి సామర్థ్యాన్ని ఇస్తుంది.

**Use Cases**: టూల్ వినియోగం, బహుళ-దశ వర్క్‌ఫ్లోలు మరియు ఎంటర్‌ప్రైజ్ ఇంటిగ్రేషన్ సందర్భాలతో తయారీ-తయారు ఏజెంట్‌ల నిర్మాణం.

ఇవి Microsoft Agent Framework యొక్క కొన్ని ముఖ్యమైన కోర్ కాన్సెప్ట్‌లు:

- **Agents**. ఏజెంట్ `AzureAIProjectAgentProvider` ద్వారా సృష్టించబడుతుంది మరియు పేరుతో, సూచనలతో మరియు టూల్స్‌తో కాన్ఫిగర్ చేయబడుతుంది. ఏజెంట్ చేయగలదు:
  - **Process user messages** మరియు Azure OpenAI మోడళ్లను ఉపయోగించి స్పందనలు ఉత్పత్తి చేయడం.
  - **Call tools** సంభాషణ సందర్భం ఆధారంగా ఆటో‌మేటిక్‌గా.
  - **Maintain conversation state** బహుళ పరస్పర చర్యలలో గుండా సంభాషణ స్థితిని నిర్వహించడం.

  Here is a code snippet showing how to create an agent:

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

- **Tools**. ఫ్రేమ్‌వర్క్ టూల్స్‌ను Python ఫంక్షన్‌లుగా నిర్వచించడాన్ని సపోర్ట్ చేస్తుంది, ఇవి ఏజెంట్ ఆటోమేటిక్‌గా పిలవగలదు. టూల్స్ ఏజెంట్‌ను సృష్టించినప్పుడు రిజిస్టర్ చేయబడతాయి:

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

- **Multi-Agent Coordination**. మీరు విభిన్న ప్రత్యేకతలతో బహుళ ఏజెంట్‌లను సృష్టించి వాటి పనిని సమన్వయపరచవచ్చు:

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

- **Azure Identity Integration**. ఫ్రేమ్‌వర్క్ `AzureCliCredential` (లేదా `DefaultAzureCredential`)ను సురక్షిత, కీ లేకుండా ఆటోంతికరణ కోసం ఉపయోగిస్తుంది, దీని వలన API కీలు నేరుగా నిర్వహించాల్సిన అవసరం ఉండదు.

## Azure AI Agent Service

Azure AI Agent Service Microsoft Ignite 2024 వద్ద పరిచయం చేయబడింది. ఇది Llama 3, Mistral, Cohere వంటి ఓపెన్-సోర్స్ LLMs‌ను నేరుగా కాల్ చేయగలిగేలా మరింత సాఫ్ట్ మోడల్స్‌కు అనుకూలత కలిగిన ఏజెంట్‌లను అభివృద్ధి చేయడానికి మరియు డిప్లాయ్ చేయడానికి వీలుగా రూపొందించబడింది.

Azure AI Agent Service బలమైన ఎంటర్‌ప్రైజ్ భద్రతా యంత్రాంగాలు మరియు డేటా నిల్వ పద్ధతులను అందిస్తుంది, దీని వల్ల ఇది ఎంటర్‌ప్రైజ్ అప్లికేషన్లకు అనుకూలంగా ఉంటుంది.

ఇది Microsoft Agent Frameworkతో బయటే పనిచేస్తుంది మరియు ఏజెంట్‌లను నిర్మించడానికి మరియు డిప్లాయ్ చేయడానికి ఉపయోగపడుతుంది.

ఈ సర్వీస్ ప్రస్తుతం Public Previewలో ఉంది మరియు ఏజెంట్‌లను నిర్మించడానికి Python మరియు C# ను సపోర్ట్ చేస్తుంది.

Azure AI Agent Service Python SDK ఉపయోగించి, ఒక వినియోగదారు-ప్రత్యేక టూల్తో ఏజెంట్‌ను yarat చేయవచ్చు:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# టూల్ ఫంక్షన్లను నిర్వచించండి
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

### కోర్ కాన్సెప్ట్‌లు

Azure AI Agent Service కు క్రింది కోర్ కాన్సెప్ట్‌లు ఉన్నాయి:

- **Agent**. Azure AI Agent Service Microsoft Foundryతో ఇన్టిగ్రేట్ అవుతుంది. AI Foundryలో, ఒక AI ఏజెంట్ "స్మార్ట్" మైక్రోసర్వీస్‌గా მოქმედించి ప్రశ్నలకు సమాధానాలు ఇవ్వడంలో (RAG), చర్యలు అమలు చేయడంలో లేదా వర్క్‌ఫ్లోలను పూర్తిగా ఆటోమేట్ చేయడంలో ఉపయోగపడుతుంది. ఇది జనరేటివ్ AI మోడళ్ల శక్తిని రియల్-వర్డ్ డేటా సోర్స్‌లను యాక్సెస్ చేయడానికి మరియు వాటితో పరస్పరం చేయడానికి అనుమతించే టూల్స్‌తో కలపడం ద్వారా సాధ్యమవుతుంది. Here's an example of an agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    In this example, an agent is created with the model `gpt-4o-mini`, a name `my-agent`, and instructions `You are helpful agent`. The agent is equipped with tools and resources to perform code interpretation tasks.

- **Thread and messages**. థ్రెడ్ మరో ముఖ్య కాన్సెప్ట్. ఇది ఏజెంట్ మరియు వినియోగదారునికిమధ్య సంభాషణ లేదా పరస్పరం చూపిస్తుంది. థ్రెడ్‌లు సంభాషణ పురోగతిని ట్రాక్ చేయడానికి, సందర్భ సమాచారాన్ని నిల్వ చేయడానికి మరియు పరస్పరం స్థితిని నిర్వహించడానికి ఉపయోగపడతాయి. Here's an example of a thread:

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

    In the previous code, a thread is created. Thereafter, a message is sent to the thread. By calling `create_and_process_run`, the agent is asked to perform work on the thread. Finally, the messages are fetched and logged to see the agent's response. The messages indicate the progress of the conversation between the user and the agent. It's also important to understand that the messages can be of different types such as text, image, or file, that is the agents work has resulted in for example an image or a text response for example. As a developer, you can then use this information to further process the response or present it to the user.

- **Integrates with the Microsoft Agent Framework**. Azure AI Agent Service Microsoft Agent Frameworkతో సుళభంగా పని చేస్తుంది, అంటే మీరు `AzureAIProjectAgentProvider` ఉపయోగించి ఏజెంట్‌లను నిర్మించవచ్చు మరియు వాటిని ప్రొడక్షన్ సందర్భాలలో డిప్లాయ్ చేయడానికి Agent Service ద్వారా పంపవచ్చు.

**Use Cases**: Azure AI Agent Service భద్రత గల, స్కేలబుల్ మరియు అనుకూలమైన AI ఏజెంట్ డిప్లాయ్‌మెంట్ అవసరమయ్యే ఎంటర్‌ప్రైజ్ అప్లికేషన్ల కోసం రూపొందించబడింది.

## ఈ రెండు విధానాల మధ్య తేడా ఏమిటి?
 
ఇవి కొంతవరకు ఓవర్‌ల్యాప్ ఉన్నట్టు అనిపిస్తుంది, కానీ రూపకల్పన, సామర్థ్యాలు మరియు లక్ష్య వినియోగాల పరంగా కొన్ని ముఖ్య తేడాలు ఉన్నాయి:
 
- **Microsoft Agent Framework (MAF)**: AI ఏజెంట్‌లను నిర్మించడానికి ప్రొడక్షన్-రెడీ SDK. ఇది టూల్ కాలింగ్, సంభాషణ నిర్వహణ, మరియు Azure ఐడెంటిటీ ఇంటిగ్రేషన్ కోసం సరళీకృత APIని అందిస్తుంది.
- **Azure AI Agent Service**: Azure Foundryలో ఏజెంట్‌ల కోసం ఒక ప్లాట్‌ఫారం మరియు డిప్లాయ్‌మెంట్ సర్వీస్. ఇది Azure OpenAI, Azure AI Search, Bing Search మరియు కోడ్ ఎగ్జిక్యూషన్ వంటి సేవలకు బిల్ట్-ఇన్ కనెక్టివిటీని అందిస్తుంది.
 
ఇంకా ఏదంతి ఎంచుకోవాలో ఆశ్చర్యంగా ఉన్నారా?

### ఉపయోగ సందర్భాలు
 
మనం కొన్ని సాధారణ ఉపయోగ సందర్భాల ద్వారా మీకు సహాయం చేయగలమో చూసేద్దాం:
 
> Q: I'm building production AI agent applications and want to get started quickly
>
>A: The Microsoft Agent Framework is a great choice. It provides a simple, Pythonic API via `AzureAIProjectAgentProvider` that lets you define agents with tools and instructions in just a few lines of code.

>Q: I need enterprise-grade deployment with Azure integrations like Search and code execution
>
> A: Azure AI Agent Service is the best fit. It's a platform service that provides built-in capabilities for multiple models, Azure AI Search, Bing Search and Azure Functions. It makes it easy to build your agents in the Foundry Portal and deploy them at scale.
 
> Q: I'm still confused, just give me one option
>
> A: Start with the Microsoft Agent Framework to build your agents, and then use Azure AI Agent Service when you need to deploy and scale them in production. This approach lets you iterate quickly on your agent logic while having a clear path to enterprise deployment.
 
Let's summarize the key differences in a table:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool calling | Agents, Tools, Azure Identity | Building AI agents, tool use, multi-step workflows |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## నేను నా ప్రస్తుత Azure పరిసర సాధనాలను నేరుగా ఇంటిగ్రేట్ చేయగలనా, లేదా నాకు స్వతంత్ర పరిష్కారాలు అవసరమా?
సమాధానం అవును — మీరు మీ ఇప్పటికే ఉన్న Azure ఎకోసిస్టమ్ టూల్స్‌ను ప్రత్యేకంగా Azure AI Agent Serviceతో నేరుగా సమీకరించవచ్చు, ఎందుకంటే ఇది ఇతర Azure సేవలతో సౌకర్యవంతంగా పని చేయాలనే దృష్టితో నిర్మించబడింది. ఉదాహరణకు మీరు Bing, Azure AI Search, మరియు Azure Functions‌ని సమీకరించవచ్చు. Microsoft Foundryతో కూడా లోతైన సమీకరణ ఉంది.

The Microsoft Agent Framework కూడా `AzureAIProjectAgentProvider` మరియు Azure identity ద్వారా Azure సేవలతో సమీకరించబడుతుంది, ఇది మీ ఏజెంట్ టూల్స్ నుండి Azure సేవలను నేరుగా కాల్ చేయడానికి వీలు కల్పిస్తుంది.

## నమూనా కోడ్లు

- Python: [ఏజెంట్ ఫ్రేమ్‌వర్క్](./code_samples/02-python-agent-framework.ipynb)
- .NET: [ఏజెంట్ ఫ్రేమ్‌వర్క్](./code_samples/02-dotnet-agent-framework.md)

## AI ఏజెంట్ ఫ్రేమ్‌వర్క్స్ గురించి ఇంకా ప్రశ్నలు ఉన్నాయా?

ఇతర అభ్యసకులతో కలవడానికి, ఆఫీస్ గంటల్లో పాల్గొనడానికి మరియు మీ AI ఏజెంట్స్ ప్రశ్నలకు సమాధానాలు పొందడానికి [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)లో చేరండి.

## సూచనలు

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure ఏజెంట్ సర్వీస్</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI ప్రతిస్పందనలు</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent సేవ</a>

## గత పాఠం

[AI ఏజెంట్లు మరియు ఏజెంట్ ఉపయోగ సందర్భాల పరిచయం](../01-intro-to-ai-agents/README.md)

## తదుపరి పాఠం

[ఏజెంటిక్ డిజైన్ నమూనాలను అర్థం చేసుకోవడం](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి యత్నించినప్పటికీ, స్వయంచాలక అనువాదాల్లో లోపాలు లేదా తప్పుదోషాలు ఉండే అవకాశం ఉందని దయచేసి గమనించండి. మాతృభాషలో ఉన్న అసలు పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి నిపుణులైన మానవ అనువాదాన్ని సిఫార్సు చేస్తాము. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల కలిగే ఏవైనా అవగాహనా లోపాలు లేదా తప్పుగా అర్థం చేసుకోవడాలకై మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->