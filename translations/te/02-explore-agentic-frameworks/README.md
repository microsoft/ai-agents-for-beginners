[![AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లను అన్వేషించడం](../../../translated_images/te/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ఈ పాఠం వీడియోను చూడడానికి పై చిత్రాన్ని క్లిక్ చేయండి)_

# AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లను అన్వేషించండి

AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు AI ఏజెంట్ల సృష్టి, పంపిణీ మరియు నిర్వహణను సులభతరం చేయడానికి రూపొందించిన సాఫ్ట్‌వేర్ ప్లాట్‌ఫారమ్‌లు. ఈ ఫ్రేమ్‌వర్క్‌లు డెవలపర్లు ముందుగానే అందుబాటులో ఉన్న భాగాలు, అవబోధ్యాలు మరియు సాధనాలను అందిస్తూ సంక్లిష్టమైన AI వ్యవస్థల అభివృద్ధిని సులభతరం చేస్తాయి.

ఈ ఫ్రేమ్‌వర్క్‌లు డెవలపర్లను వారి అనువర్తనాల ప్రత్యేకతలపై దృష్టి పెట్టేందుకు సహాయపడతాయి, AI ఏజెంట్ అభివృద్ధిలో సాధారణ సవాళ్లకు ప్రమాణీకృత దృష్టాంతాలను అందిస్తూ. ఇవి AI వ్యవస్థలను నిర్మించడంలో స్కేలబిలిటీ, యాక్సెసిబిలిటీ మరియు సమర్థతను మెరుగుపరుస్తాయి.

## పరిచయం

ఈ పాఠంలో ఈ అంశాలు ఉంటాయి:

- AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు ఏమిటి మరియు అవి డెవలపర్లను ఏమి సాధించుకునేందుకు అనుమతిస్తాయి?
- జట్లు ఎలా త్వరగానే ప్రోటోటైప్ చేయడం, మళ్లీ పునఃసమీక్షించడం మరియు ఏజెంట్ సామర్థ్యాలను మెరుగుపరచుకోవచ్చు?
- మైక్రోసాఫ్ట్ ( <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> మరియు <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a> ) సృష్టించిన ఫ్రేమ్‌వర్క్‌లు మరియు సాధనాలలో తేడాలేమిటి?
- నా ప్రస్తుతం ఉన్న Azure పరిసర సాధనాలను నేరుగా ఇంటిగ్రేట్ చేయాలా, లేక స్వతంత్ర పరిష్కారాలు అవసరమా?
- Microsoft Foundry Agent Service అంటే ఏమిటి మరియు ఇది నాకు ఎలా సహాయపడుతోంది?

## అభ్యాస లక్ష్యాలు

ఈ పాఠం ఇక్కడి వరకు తెలుసుకునేందుకు సహాయపడుతుంది:

- AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌ల పాత్ర గురించి.
- తెలివైన ఏజెంట్ల నిర్మాణానికి AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లను ఎలా ఉపయోగించాలో.
- AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు సాధించే ప్రధాన సామర్థ్యాలు.
- Microsoft Agent Framework మరియు Microsoft Foundry Agent Service మధ్య తేడాలు.

## AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు ఏమిటి మరియు డెవలపర్లు ఏం సాధించగలరు?

సంప్రదాయ AI ఫ్రేమ్‌వర్క్‌లు మీ అనువర్తనాల్లో AIని ఏకీకృతం చేసి, ఈ విధాలుగా మెరుగుపరచడంలో సహాయపడతాయి:

- **వ్యక్తిగతీకరణ**: AI వినియోగదారుల ప్రవర్తన మరియు ఇష్టం విశ్లేషించి, వ్యక్తిగత సిఫార్సులు, కంటెంట్ మరియు అనుభవాలు అందించగలదు.
ఉదాహరణ: Netflix వంటి స్ట్రీమింగ్ సేవలు వీక్షణ చరిత్ర ఆధారంగా సినిమాలు, షోయ్‌లను సిఫారసు చేయడానికి AIను ఉపయోగించి వినియోగదారుల ఆసక్తిని మరియు సంతృప్తిని పెంచుతాయి.
- **ఆటోమేషన్ మరియు సమర్థత**: AI పునరావృత పనులను ఆటోమేట్ చేసి, పనిముట్టులను సుసంపన్నంగా చేసి, ఆపరేషన్ల సమర్థతను మెరుగుపరచగలదు.
ఉదాహరణ: కస్టమర్ సర్వీస్ యాప్స్ సాధారణ విచారణలకు AI-చాలిత చాట్‌బాట్‌లను ఉపయోగించి ప్రతిస్పందన సమయాన్ని తగ్గించి, మానవ ఏజెంట్లను క్లిష్ట సమస్యల పరిష్కారానికి విముక్తం చేస్తాయి.
- **మెరుగైన వినియోగదారుల అనుభవం**: AI వాయిస్ రికగ్నిషన్, సహజ భాష ప్రాసెసింగ్, ముందస్తు వచన సూచనలు వంటి తెలివైన ఫీచర్లతో వినియోగదారుల అనుభవాన్ని మెరుగుపరుస్తుంది.
ఉదాహరణ: Siri మరియు Google అసిస్టెంట్ వాయిస్ కమాండ్లను అర్థం చేసుకుని స్పందించడానికి AIను ఉపయోగించి వినియోగదారులు వారి పరికరాలతో సులభంగా అటు ఇటు మసకబారకుండా మెలగగలుగుతారు.

### బాగుంది కదా, కాబట్టి AI ఏజెంట్ ఫ్రేమ్‌వర్క్ ఎందుకు అవసరం?

AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు సాధారణ AI ఫ్రేమ్‌వర్క్‌ల కన్నా ఎక్కువగా ప్రతినిధిత్వం చేస్తాయి. అవి వినియోగదారులు, ఇతర ఏజెంట్లు మరియు పర్యావరణంతో పరస్పర చర్య చేయగల తెలివైన ఏజెంట్ల సృష్టిని సులభతరం చేస్తాయి. ఈ ఏజెంట్లు స్వయంచాలక ప్రవర్తన ప్రదర్శించగలవు, నిర్ణయాలు తీసుకోగలవు, మారుతున్న పరిస్థితులకు తగినట్టు అనుకూలించగలవు. AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు సాధించే ముఖ్యమైన సామర్థ్యాలు ఇవి:

- **ఏజెంట్ సహకారం మరియు సమన్వయం**: కలిసి పనిచేయగల, పరస్పరం కమ్యూనికేట్ చేసి క్లిష్ట పనులను పరిష్కరించుకునేందుకు అనేక AI ఏజెంట్ల సృష్టిని సాధ్యమవుతుంది.
- **పనుల ఆటోమేషన్ మరియు నిర్వహణ**: బహుళ దశల వర్క్‌ఫ్లోలు ఆటోమేట్ చేయడం, పనుల అప్పగింపు మరియు ఏజెంట్ల మధ్య డైనమిక్ పనులు నిర్వహణకు మెకానిజమ్‌లు అందిస్తుంది.
- **సందర్భాన్ని అర్థం చేసుకోవడం మరియు అనుకూలం కావడం**: ఏజెంట్లు ప్రస్తుత సందర్భాన్ని అర్థం చేసుకుని, పరిసరాల మార్పులకి అనుగుణంగా నిర్ణయాలు తీసుకునే సామర్థ్యం కలిగి ఉంటాయి.

సంక్షిప్తంగా చెప్పాలంటే, ఏజెంట్లు మరింత మెరుగైన ఆటోమేషన్, మరింత తెలివైన వ్యవస్థలను సృష్టించడం, వాటి పరిసరాల నుండి నేర్చుకుని అనుకూలంగా మారడం చేస్తాయి.

## ఏజెంట్ సామర్థ్యాలను త్వరగా ప్రోటోటైప్, పునఃసమీక్షించి మెరుగుపరచటం ఎలా?

ఇది వేగంగా మెరుగవుతున్న విభాగం, కానీ ఎక్కువ AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లలో సాధారణంగా ఉన్న కొన్ని విషయాలు మోడ్యూల్ భాగాలు, సహకార సాధనాలు, రియల్-టైమ్ నేర్చుకునే విధానాలు, ఇవి సహాయపడతాయి. నీటికి లోతుగా వెళ్దాం:

- **మోడ్యూలర్ భాగాలను ఉపయోగించండి**: AI SDKలు ముందుగానే తయారు చేసిన భాగాలు అందిస్తాయి, ఉదా: AI మరియు మేమరీ కనెక్టర్లు, సహజ భాష లేదా కోడ్ ప్లగిన్ల ద్వారా ఫంక్షన్ కాలింగ్, ప్రాంప్ట్ టెంప్లేట్లు మొదలైనవి.
- **సహకార సాధనాలను వినియోగించండి**: ప్రత్యేక పాత్రలు, పనుల కోసం ఏజెంట్లను డిజైన్ చేసి, సహకార వర్క్‌ఫ్లోలను పరీక్షించి మెరుగుపర్చండి.
- **రియల్-టైమ్‌లో నేర్చుకోండి**: ఏజెంట్లు పరస్పర చర్యల నుండి నేర్చుకుని ప్రవర్తనలో తగిన మార్పులు చేసుకునే ఫీడ్బ్యాక్ లూపులను అమలు చేయండి.

### మోడ్యూలర్ భాగాలు ఉపయోగించడం

Microsoft Agent Framework లాంటి SDKలు AI కనెక్టర్లు, టూల్ నిర్వచనలు మరియు ఏజెంట్ నిర్వహణ వంటి ముందస్తు భాగాలను అందిస్తాయి.

**జట్లు ఎలా ఉపయోగిస్తాయి**: జట్లు ఈ భాగాలను వెంటనే కలిపి పనితీరు ప్రోటోటైప్ సృష్టించవచ్చు, కొత్తదాన్ని మొదలు పెట్టకుండా త్వరగా ప్రయోగాలు చేసి పునఃసమీక్ష చేయవచ్చు.

**వాస్తవాలలో ఇది ఎలా పనిచేస్తుంది**: ఉపయోగదారుల ఇన్‌పుట్ నుండి సమాచారాన్ని తీసుకొనే ప్రీ-బడ్ట్ పార్సర్, డేటా నిల్వ, పొందుట కోసం మెమరీ మాడ్యూల్, వినియోగదారులతో సంభాషణకు ప్రాంప్ట్ జెనరేటర్ వంటివి నల్ల నిర్మించకూడదు.

**ఉదాహరణ కోడ్**. ఉపయోగదారుల ఇన్‌పుట్‌కు టూల్ కాలింగ్‌తో స్పందించేందుకు Microsoft Agent Framework ను `FoundryChatClient` తో ఎలా ఉపయోగించాలో చూద్దాం:

``` python
# మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ పైథాన్ ఉదాహరణ

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# ప్రయాణాన్ని బుక్ చేయడానికి ఒక నమూనా టూల్ ఫంక్షన్‌ని నిర్వచించండి
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
    # ఉదాహరణ అవుట్‌పుట్: మీను 2025 జనవరి 1న న్యూయార్క్‌కు ఫ్లైటును విజయవంతంగా బుక్ చేయబడింది. సురక్షిత ప్రయాణాలు! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ఈ ఉదాహరణలో మీరు ముందుగానే ఉన్న పార్సర్ ద్వారా ప్రయాణ బుకింగ్ అభ్యర్థన గురించి ముఖ్య సమాచారం (మూలం, గమ్యం, తేదీ) ఎలా తీసుకోవచ్చో చూడొచ్చు. ఈ మోడ్యూలర్ విధానం మీరించే పెద్ద స్థాయి లాజిక్ పై కేంద్రీకరించటానికి అనుమతిస్తుంది.

### సహకార సాధనాలను వినియోగించండి

Microsoft Agent Framework వంటి ఫ్రేమ్‌వర్క్‌లు అనేక ఏజెంట్లు కలిసి పని చేయడానికి సహాయపడతాయి.

**జట్లు ఎలా ఉపయోగిస్తాయి**: జట్లు నిర్దిష్ట పాత్రలు, పనులతో ఏజెంట్లను డిజైన్ చేసి, సహకార వర్క్‌ఫ్లోలను పరీక్షించి మెరుగుపరచి వ్యవస్థ సమర్థతను పెంచవచ్చు.

**వాస్తవాలలో ఇది ఎలా పనిచేస్తుంది**: డేటా పొందడం, విశ్లేషణ లేదా నిర్ణయాలు తీసుకోవడం వంటి ప్రత్యేక పనులు ఉన్న ఏజెంట్ల జట్టును మీరు సృష్టించవచ్చు. ఈ ఏజెంట్లు పరస్పరం సమాచారాన్ని పంచుకుని ఒకే లక్ష్యం సాధిస్తాయి, ఉదా: వినియోగదారుడి ప్రశ్నకు సమాధానం ఇవ్వడం లేదా పని పూర్తిచేయడం.

**ఉదాహరణ కోడ్ (Microsoft Agent Framework)**:

```python
# Microsoft Agent Framework ఉపయోగించి కలిసి పనిచేసే బహుళ ఏజెంట్లను సృష్టించడం

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# డేటా రికవరీ ఏజెంట్
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# డేటా విశ్లేషణ ఏజెంట్
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ఒక పనిపై ఏజెంట్లను వరుసగా నడపండి
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

ముందున్న కోడ్‌లో మీరు పలురకాల ఏజెంట్లు కలిసి డేటాను విశ్లేషించేందుకు పని ఎలా చేస్తుందో చూస్తారు. ప్రతి ఏజెంట్ ప్రత్యేక పని నిర్వహించి, పని ఏజెంట్ల సమన్వయంతో లక్ష్యాన్ని సాధిస్తుంది. ప్రత్యేక పాత్రలతో ఏజెంట్లను సృష్టించడం పనుల సమర్థత, ప్రదర్శన మెరుగుపరుస్తుంది.

### రియల్-టైమ్‌లో నేర్చుకోండి

అధునాతన ఫ్రేమ్‌వర్క్‌లు రియల్-టైమ్ సాందర్భిక అవగాహన మరియు అనుకూలతను కలిగిస్తాయి.

**జట్లు ఎలా ఉపయోగిస్తాయి**: ఏజెంట్లు పరస్పర చర్యల నుండి నేర్చుకుని ప్రవర్తనలో తగిన మార్పులు చేసుకునే ఫీడ్బ్యాక్ లూపులను అమలు చేయడం ద్వారా నిరంతర మెరుగుదల సాధిస్తాయి.

**వాస్తవాలలో ఇది ఎలా పనిచేస్తుంది**: ఏజెంట్లు వినియోగదారు అభిప్రాయం, పర్యావరణ సమాచారం మరియు పనుల ఫలితాలను విశ్లేషించి వారి జ్ఞానసారాన్ని నవీకరిస్తాయి, నిర్ణయాల ఆల్గోరిథంలను సరిచేస్తాయి మరియు సమయంతో పనితీరును మెరుగుపరుస్తాయి. ఈ పునరావృత నేర్పుకునే ప్రక్రియ ఏజెంట్లకు మార్తాంశాల మరియు వినియోగదారుల ఇష్టాలకు అనుగుణంగా మారేందుకు సహాయపడుతోందు.

## Microsoft Agent Framework మరియు Microsoft Foundry Agent Service మధ్య తేడాలేమిటి?

ఈ రెండు దృష్టాంతాలను పోల్చగలవు అనేక మార్గాలు ఉన్నాయి, కానీ వారి రూపకల్పన, సామర్థ్యాలు మరియు లక్ష్య ఉపయోగ సందర్భాల పరంగా కొన్ని ముఖ్య తేడాలు ఉన్నాయి:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `FoundryChatClient` ఉపయోగించి AI ఏజెంట్లు నిర్మించేందుకు సరళమైన SDK ను అందిస్తుంది. ఇది Azure OpenAI మోడళ్లను ఉపయొగించి, బిల్ట్-ఇన్ టూల్ కాలింగ్, సంభాషణ నిర్వహణ, Azure గుర్తింపుతో ఎంటర్ప్రైజ్-గ్రేడ్ భద్రత కలిగిస్తుంది.

**ఉపయోగ సందర్భాలు**: టూల్ వినియోగం, బహుళ దశల వర్క్‌ఫ్లోలు, ఎంటర్ప్రైజ్ ఏకీకరణ సన్నివేశాలతో ఉత్పత్తి-సిద్ధ AI ఏజెంట్లు నిర్మించడం.

Microsoft Agent Framework యొక్క కొన్ని ముఖ్యాంశాలు:

- **ఏజెంట్లు**: ఒక ఏజెంట్ `FoundryChatClient` ద్వారా సృష్టించబడుతుంది, పేరు, సూచనలు, మరియు టూల్స్‌తో కాన్ఫిగర్ చేయబడుతుంది. ఏజెంట్ చేయగలదు:
  - **వినియోగదారు సందేశాలను ప్రాసెస్ చేయడం** మరియు Azure OpenAI మోడళ్లతో సమాధానాలు రూపొందించడం.
  - **సంభాషణ సాందర్భాన్ని ఆధారంగా** ఆటోమేటిక్‌గా టూల్స్‌ని కాల్ చేయడం.
  - **బహుళ పరస్పర చర్యలలో సంభాషణ స్థితిని నిర్వహించడం**.

  ఏజెంట్ సృష్టించే కోడ్ అంతరానాను చూడండి:

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

- **టూల్స్**: ఫ్రేమ్‌వర్క్ టూల్స్‌ను Python ఫంక్షన్‌లుగా నిర్వచించడం మద్దతిస్తుంది, ఇవి ఏజెంట్ ఆటోమేటిక్‌గా పిలవగలదు. ఏజెంట్ సృష్టించే సమయంలో టూల్స్ రిజిస్టర్ చేస్తారు:

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

- **బహుళ ఏజెంట్ సమన్వయం**: వేర్వేరు ప్రత్యేకతలు ఉన్న అనేక ఏజెంట్లను సృష్టించి వారి పనులను సమన్వయ పెట్టవచ్చు:

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

- **Azure గుర్తింపు ఏకీకరణ**: ఫ్రేమ్‌వర్క్ `AzureCliCredential` (లేదా `DefaultAzureCredential`) ఉపయోగించి స్వయంచాలక, కీలు నిర్వహణలో రహిత భద్రతను అందిస్తుంది.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service Microsoft Ignite 2024లో పరిచయమైన తాజా సేవ. ఇది ఎక్కువ స్వేచ్ఛ కలిగిన మోడళ్లతో AI ఏజెంట్ల ను అభివృద్ధి, పంపిణీ చేసేందుకు అనుమతిస్తుంది, ఉదాహరణకి Llama 3, Mistral, Cohere వంటి ఓపెన్ సోర్స్ LLMలను నేరుగా పిలవడం.

Microsoft Foundry Agent Service మెరుగైన ఎంటర్ప్రైజ్ భద్రతా పద్ధతులు మరియు డేటా నిల్వ విధానాలు కలిగి ఉండి, ఎంటర్ప్రైజ్ అప్లికేషన్ల కోసం అనుకూలంగా ఉంటుంది.

ఇది Microsoft Agent Framework తో కలిసి ఏజెంట్లను సృష్టించి పంపిణీ చేయడానికి తయారైన విధంగా పనిచేస్తుంది.

ఈ సేవ ప్రస్తుతం పబ్లిక్ ప్రివ్యూ లో ఉంది మరియు ఏజెంట్లను నిర్మించడానికి Python మరియు C# మద్దతు కలిగి ఉంది.

Microsoft Foundry Agent Service Python SDK ఉపయోగించి, యూజర్-నిర్దిష్ట టూల్ తో ఏజెంట్ సృష్టించవచ్చు:

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
        model="gpt-4.1-mini",
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

### ప్రధాన భావనలు

Microsoft Foundry Agent Service ఈ ముఖ్య భావనలు కలిగిఉన్నది:

- **ఏజెంట్**: Microsoft Foundry Agent Service Microsoft Foundryతో సమైక్యం అవుతది. Microsoft Foundry లో AI Agent "స్మార్ట్" మైక్రోసర్వీస్‌లా పనిచేస్తుంది, ప్రశ్నలకు సమాధానం (RAG), చర్యలు తీసుకోవడం, లేదా పూర్తి ఆటోమేషన్ వర్క్‌ఫ్లోలను చేస్తుంది. ఇది జనరేటివ్ AI మోడళ్ల శక్తిని ప్రతినిధించటానికి, నిజమైన డేటా వనరులకు యాక్సెస్ మరియు పరస్పరం చర్యచేసే టూల్స్‌తో కలిపి ఇది సాధ్యం.

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ఈ ఉదాహరణలో, `gpt-4.1-mini` మోడల్, పేరు `my-agent`, మరియు సూచనలు `You are helpful agent`. ఏజెంట్ కాంప్యూట్ కోడ్ వివరణ పనులు చేయడానికి టూల్స్ మరియు వనరులతో సജ్జంగా ఉంది.

- **థ్రెడ్ మరియు సందేశాలు**: థ్రెడ్ అనేది మరొక ముఖ్య భావన. ఇది ఏజెంట్ మరియు వినియోగదారుని మధ్య సంభాషణ లేదా పరస్పరం చర్యను సూచిస్తుంది. థ్రెడ్‌లను సంభాషణ పురోగతిని ట్రాక్ చేయడానికి, సాందర్భిక సమాచారాన్ని నిల్వ చేయడానికి మరియు పరస్పర చర్య స్థితిని నిర్వహించడానికి ఉపయోగిస్తారు. థ్రెడ్ ఉదాహరణ ఇక్కడ ఉంది:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # ఏజెంట్‌కి థ్రెడ్‌పై పని చేయమని అడగండి
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # ఏజెంట్ ప్రతిస్పందన చూడడానికి అన్ని సందేశాలను తీసుకుని లాగ్ చేయండి
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    ముందుయున్న కోడ్‌లో, ఒక థ్రెడ్ సృష్టించబడింది. తరువాత, థ్రెడ్‌కు సందేశం పంపబడింది. `create_and_process_run` కాల్ చేయడం ద్వారా ఏజెంటు థ్రెడ్‌లో పని చేయడానికి అడుగుతుంది. చివరిలో, సందేశాలు తీసుకుని ఏజెంట్ ప్రతిస్పందనను లాగ్ చేస్తారు. సందేశాలు వినియోగదారు మరియు ఏజెంట్ మధ్య సంభాషణ పురోగతిని సూచిస్తాయి. సందేశాలు టెక్స్ట్, చిత్రం లేదా ఫైల్ వంటివి కావచ్చు, అంటే ఏజెంట్ పని ఫలితంగా చిత్రం లేదా వచన స్పందన ఏర్పడ్డాయేమో. డెవలపర్‌గా ఈ సమాచారాన్ని ఇంకా ప్రాసెస్ చేయడం లేదా వినియోగదారుని సమీక్షకు అందించడం చేయవచ్చు.

- **Microsoft Agent Frameworkతో సమైక్యం**: Microsoft Foundry Agent Service Microsoft Agent Frameworkతో సజావుగా పనిచేస్తుంది, అంటే `FoundryChatClient` ఉపయోగించి ఏజెంట్లను తయారు చేసి Agent Service ద్వారా పంపిణీ చేయవచ్చు.

**ఉపయోగ సందర్భాలు**: Microsoft Foundry Agent Service భద్రమైన, స్కేలబుల్, మరియు సులభమైన ఎంటర్ప్రైజ్ AI ఏజెంట్ డిప్లాయ్‌మెంట్ అవసరాల కోసం రూపొందించబడింది.

## ఈ దృష్టాంతాల మధ్య తేడాలు ఏమిటి?
 
ఇది ఓవర్లాప్ ఉన్నట్టుగా ఉండొచ్చు, కాని రూపకల్పన, సామర్థ్యం మరియు లక్ష్య ఉపయోగ సందర్భాల పరంగా కొన్ని ముఖ్య తేడాలు ఉన్నాయి:
 
- **Microsoft Agent Framework (MAF)**: AI ఏజెంట్ల నిర్మాణానికి ఉత్పత్తి-సిద్ధ SDK. టూల్ కాలింగ్, సంభాషణ నిర్వహణ మరియు Azure గుర్తింపు ఏకీకరణ కోసం సరళమైన APIని అందిస్తుంది.
- **Microsoft Foundry Agent Service**: Microsoft Foundryలో ఏజెంట్లకు ప్లాట్‌ఫారం మరియు పంపిణీ సేవ. Azure OpenAI, Azure AI Search, Bing Search మరియు కోడ్ ఎగ్జిక్యూషన్ వంటి సేవలకు బిల్ట్-ఇన్ కనెక్టివిటీ కలిగిఉంటుంది.
 
ఇంకా ఎంచుకోవడం సంక్లిష్టంగా ఉందా?

### ఉపయోగ సందర్భాలు
 
కొన్ని సర్వసాధారణ ఉపయోగ కేసులు చూసి మీకు సహాయపడదామా చూద్దాం:
 
> Q: నేను ఉత్పత్తి AI ఏజెంట్ అప్లికేషన్లు నిర్మిస్తున్నాను, త్వరగానే ప్రారంభించాలంటే ఏమి చేయాలి?
>

>A: Microsoft Agent Framework చాలా సరైన ఎంపిక. ఇది `FoundryChatClient` ద్వారా సరళమైన, Python షైళీలో ఏజెంట్లను టూల్స్ మరియు సూచనలతో కొన్ని పంక్తుల కోడ్‌తో నిర్వచించవచ్చు.

>Q: నాకు ఎంటర్ప్రైజ్-గ్రేడ్ డిప్లాయ్‌మెంట్ కావాలి, Azure Search మరియు కోడ్ ఎగ్జిక్యూషన్ వంటి ఇంటిగ్రేషన్లు అవసరం.
>
> A: Microsoft Foundry Agent Service అత్యుత్తమ ఎంపిక. ఇది అనేక మోడళ్లకు, Azure AI Search, Bing Search మరియు Azure ఫంక్షన్స్‌కు బిల్ట్-ఇన్ సామర్థ్యాలు కల్పించే ప్లాట్‌ఫారం సేవ. మీరు Foundry పోర్టల్‌లో ఏజెంట్లను సృష్టించి పెద్ద కొలతలో డిప్లాయ్ చేయడం సులభం చేస్తుంది.
 
> Q: ఇంకా క్లారిటీ లేదు, ఒక ఎంపిక ఇవ్వండి.
>
> A: Microsoft Agent Framework తో ఏజెంట్లను సృష్టించడం ప్రారంభించండి, తరువాత ఉత్పత్తిలో వాటిని పంపిణీ చేయడానికి Microsoft Foundry Agent Service ఉపయోగించండి. ఈ విధానం మీకు ఏజెంట్ లాజిక్‌పై త్వరగా తిరగబడే అవకాశం ఇస్తుంది మరియు ఎంటర్ప్రైజ్ డిప్లాయ్‌మెంట్ దిశగా స్పష్టమైన మార్గాన్ని కల్పిస్తుంది.
 
ముఖ్య తేడాలను పట్టికలో సారాంశం చేద్దాం:

| ఫ్రేమ్‌వర్క్ | ఫోకస్ | ప్రధాన భావనలు | ఉపయోగ సందర్భాలు |
| --- | --- | --- | --- |
| Microsoft Agent Framework | టూల్ కాలింగ్‌తో సమర్థ agent SDK | ఏజెంట్లు, టూల్స్, Azure గుర్తింపు | AI ఏజెంట్ల నిర్మాణం, టూల్ వినియోగం, బహుళ దశల వర్క్‌ఫ్లోలు |
| Microsoft Foundry Agent Service | సౌకర్యవంతమైన మోడళ్లు, ఎంటర్ప్రైజ్ భద్రత, కోడ్ జనరేషన్, టూల్ కాలింగ్ | మాడ్యులారిటీ, సహకారం, ప్రాసెస్ నిర్వహణ | భద్రమైన, స్కేలబుల్, సౌకర్యవంతమైన AI ఏజెంట్ డిప్లాయ్‌మెంట్ |

## నా ప్రస్తుతం ఉన్న Azure పరిసర సాధనాలను నేరుగా ఇంటిగ్రేట్ చేయవచ్చు, లేదా స్వతంత్ర పరిష్కారాలు కావాలా?


సమాధానం అవును, మీరు మీ ఉన్న Azure ఎకోసిస్ట్ టూల్స్‌ను Microsoft Foundry Agent Service తో నేరుగా సమ్మిళితం చేయవచ్చు, ముఖ్యంగా ఇది ఇతర Azure సేవలతో సజీవంగా పనిచేయడానికి రూపొందించబడింది. ఉదాహరణకు మీరు Bing, Azure AI Search, మరియు Azure Functions ని సమ్మిళితం చేయవచ్చు. Microsoft Foundryతో కూడా లోతైన సమ్మిళితం ఉంది.

Microsoft Agent Framework కూడా `FoundryChatClient` మరియు Azure identity ద్వారా Azure సేవలతో సమ్మిళితం అవుతుంది, ఇది మీ ఏజెంట్ టూల్స్ నుండి నేరుగా Azure సేవలను కాల్ చేయడానికి అనుమతిస్తుంది.

## నమూనా కోడ్లు

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI ఏజెంట్ ఫ్రేమ్‌వర్క్ల గురించి మరిన్ని ప్రశ్నలున్నాయా?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) లో చేరి ఇతర అధ్యయనార్ధులతో కలుసుకోండి, ఆఫీస్ గంటలకు హాజరవండి మరియు మీ AI ఏజెంట్ ప్రశ్నలకు సమాధానం పొందండి.

## సూచనలు

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## προηγούμενο μάθημα

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## తదుపరి పాఠం

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->