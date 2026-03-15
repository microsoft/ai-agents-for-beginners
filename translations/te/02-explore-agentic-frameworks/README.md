[![AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లను అన్వేషించడం](../../../translated_images/te/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ఈ పాఠమునకు సంబంధించిన వీడియోను చూడటానికి పై చిత్రాన్ని క్లిక్ చేయండి)_

# AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లను అన్వేషించండి

AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు AI ఏజెంట్లను సృష్టించడం, పంపిణీ చేయడం, మరియు నిర్వహించడం సులభతరం చేయడానికి రూపొందించబడిన సాఫ్ట్‌వేర్ ప్లాట్‌ఫారమ్‌లు. ఈ ఫ్రేమ్‌వర్క్‌లు డెవలపర్లకు ముందు-నిర్మించబడిన భాగాలు, సారాంశాలు, మరియు క్లిష్టమైన AI సిస్టమ్‌ల అభివృద్ధిని సులభం చేసే సాధనాలు అందిస్తాయి.

ఈ ఫ్రేమ్‌వర్క్‌లు సాధారణ సమస్యలకు ప్రామాణికమైన విధానాలను అందించడం ద్వారా డెవలపర్లు తమ అనువర్తనాల ప్రత్యేక అంశాలపై దృష్టి పెట్టడానికి సహాయపడతాయి. ఇవి AI సిస్టమ్‌లను నిర్మించడంలో స్కేలబిలిటీ, ప్రాప్తి, మరియు పనితీరును మెరుగుపరుస్తాయి.

## పరిచయం

ఈ పాఠం కవర్ చేయబోతుంది:

- AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు ఏమిటి మరియు ఇవి డెవలపర్లకు ఏం సాధ్యమవిస్తాయి?
- బృందాలు వీటిని ఎలా ఉపయోగించి త్వరగా ప్రోటోటైప్ చేయగలవు, ఇటరేట్ చేయగలవు, మరియు వారి ఏజెంట్ల సామర్థ్యాలను మెరుగుపరుచుకోవచ్చు?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI ఏజెంట్ సర్వీస్</a> మరియు the <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft ఏజెంట్ ఫ్రేమ్‌వర్క్</a>) రూపొందించిన ఫ్రేమ్‌వర్క్‌లు మరియు సాధనాల మధ్య有什么 తేడాలు?
- నేను నా ఉన్నత Azure ఎకోసిస్టమ్ సాధనాలను నేరుగా ఇంటిగ్రేట్ చేయగలనా, లేక వేరే స్టాండ్‌లోన్ పరిష్కారాలు అవసరమా?
- Azure AI Agents సర్వీస్ ఏమిటి మరియు ఇది ఎలా నాకు సహాయం చేయుతోంది?

## అభ్యసన లక్ష్యాలు

ఈ పాఠం లక్ష్యాలు మీకు సహాయపడటానికి:

- AI అభివృద్ధిలో AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌ల పాత్రను అర్థం చేసుకోవడం.
- తెలివైన ఏజెంట్లను తయారు చేయడానికి AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లను ఎలా ఉపయోగించాలో నేర్చుకోవడం.
- AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు ప్రారంభించే ముఖ్య సామర్థ్యాలు తెలుసుకోవడం.
- Microsoft Agent Framework మరియు Azure AI Agent Service మధ్య తేడాలను అర్థం చేసుకోవడం.

## AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు ఏమిటి మరియు ఇవి డెవలపర్లకు ఏమి చేయించగలవు?

సాంప్రదాయ AI ఫ్రేమ్‌వర్క్‌లు మీ అప్లికేషన్లలో AIని ఒకీకరించడంలో మరియు ఈ అప్లికేషన్లను మెరుగుపరచడంలో ఈ క్రింది విధంగా మీకు సహాయపడతాయి:

- **వ్యక్తిగతీకరణ**: AI వాడుకరి ప్రవర్తన మరియు అభిరుచులను విశ్లేషించి వ్యక్తిగత సిఫార్సులు, కంటెంట్ మరియు అనుభవాలను అందిస్తుంది.
ఉదాహరణ: Netflix వంటి స్ట్రీమింగ్ సేవలు వీక్షన చరిత్ర ఆధారంగా సినిమాలు మరియు షోలు సూచించడానికి AIను ఉపయోగిస్తాయి, వాడుకరి ఆసక్తి మరియు సంతృప్తి పెరగడానికి సహాయపడతాయి.
- **ఆటోమేషన్ మరియు సామర్థ్యం**: AI పునరావృత పనులను ఆటోమేట్ చేయగలదు, వర్క్‌ఫ్లోలను సరళీకృతం చేయగలదు, మరియు ప్రవేశనీయ సామర్థ్యాన్ని మెరుగుపరచగలదు.
ఉదాహరణ: కస్టమర్ సర్వీస్ అప్లికేషన్లు సాధారణ విచారణలను పట్టుకోవడానికి AI-శక్తిగల చాట్‌బాట్లను ఉపయోగిస్తాయి, స్పందన సమయాలను తగ్గించి మరింత క్లిష్ట అంశాల కోసం మానవ ఏజెంట్లను విడిపిస్తాయి.
- **మెరుగైన వాడుకరి అనుభవం**: వాయిస్ గుర్తింపు, సహజ భాషా ప్రాసెసింగ్, మరియు ప్రిడిక్టివ్ టెక్స్ట్ వంటి తెలివైన ఫీచర్లు ద్వారా AI మొత్తం వాడుకరి అనుభవాన్ని మెరుగుపరుస్తుంది.
ఉదాహరణ: Siri మరియు Google Assistant వంటి వర్చువల్ అసిస్టెంట్లు వాయిస్ కమాండ్లను అర్థం చేసుకుని స్పందించడానికి AIని ఉపయోగిస్తాయి, వాడుకరుల కోసం పరికరాలతో పరస్పర చర్య చేయడం సులభతరం చేస్తాయి.

### దీనంతా బాగానే అనిపిస్తుంది, మరి కాని AI Agent Framework అవసరమా?

AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు సాధారణ AI ఫ్రేమ్‌వర్క్‌ల కంటే ఎక్కువ ఫలితాన్ని సూచిస్తాయి. అవి వినియోగదారులతో, ఇతర ఏజెంట్లతో, మరియు పర్యావరణంతో పరస్పర చర్య చేయగల తెలివైన ఏజెంట్లను సృష్టించడానికి రూపొందించబడ్డాయి, ప్రత్యేక లక్ష్యాలను సాధించడానికి. ఈ ఏజెంట్లు స్వయంచాలక ప్రవృత్తిని ప్రదర్శించగలవు, నిర్ణయాలు తీసుకోవచ్చు, మరియు మారుతున్న పరిస్థితులకు అనుకూలత చూపగలవు. ఇవి అందించే ముఖ్య సామర్థ్యాల్ని చూద్దాం:

- **ఏజెంట్ సహకారం మరియు సమన్వయం**: సంక్లిష్ట పనులను పరిష్కరించడానికి కలిసి పని చేయగల, కమ్యూనికేట్ చేయగల, మరియు సమన్వయించగల బహుళ AI ఏజెంట్ల సృష్టిని వీలు చేస్తుంది.
- **పని ఆటోమేషన్ మరియు నిర్వహణ**: బహుళ-దశ వర్క్‌ఫ్లోలను ఆటోమేట్ చేయడం, పని delegation, మరియు ఏజెంట్ల మధ్య డైనమిక్ పనుల నిర్వహణ కోసం మంత్రాలును అందిస్తుంది.
- **సందర్భ అనుభవం మరియు అనుకూలత**: ఏజెంట్లకు సందర్భాన్ని అర్థం చేసుకోవటం, మారుతున్న పరిసరాలకు అనుగుణంగా సరిపోవటం, మరియు రియల్-టైమ్ సమాచారంపై ఆధారపడి నిర్ణయాలు తీసుకోవడం చేయగల సామర్థ్యాన్ని అందిస్తుంది.

సంక్షేపంగా చెప్పాలంటే, ఏజెంట్లు మీకు మరింత చేయించగలవు, ఆటోమేషన్‌ను తదుపరి స్థాయికి తీసుకెళ్తాయి, మరియు పర్యావరణం నుంచి నేర్చుకుని అనుకూలించగల మరింత తెలివైన వ్యవస్థలను సృష్టించడానికి సహాయపడతాయి.

## ఏజెంట్ సామర్థ్యాలను త్వరగా ప్రోటోటైప్ చేయడం, ఇటరేట్ చేయడం, మరియు మెరుగుపర్చడం ఎలా?

ఇది వేగంగా మారే ప్రాంతం, కానీ అధిక భాగంలో తరచుగా ఉండే కొన్ని అంశాలు మాడ్యూలర్ కంపోనెంట్లు, సహకార సాధనాలు, మరియు రియల్-టైమ్ లెర్నింగ్. వీటిని వివరంగా చూడండి:

- **మాడ్యూలర్ కంపోనెంట్స్‌ను ఉపయోగించండి**: AI SDKలు AI మరియు మెమరీ కనెక్టర్ల వంటి ముందు-నిర్మించబడిన భాగాలు, సహజ భాష లేదా కోడ్ ప్లగిన్ల ద్వారా ఫంక్షన్ కాలింగ్, ప్రాంప్ట్ టెంప్లేట్లు, మరియు మరిన్ని అందిస్తాయి.
- **సహకార సాధనాలను లావించుకోండి**: నిర్దిష్ట పాత్రల మరియు పనులతో ఏజెంట్లను రూపొందించండి, అవి సహకార వర్క్‌ఫ్లోలను పరీక్షించి గూఢతతో మెరుగుపరచడానికి వీలు కల్పిస్తాయి.
- **రియల్-టైమ్‌లో నేర్చుకోండి**: ఏజెంట్లు పరస్పర చర్యల నుండి నేర్చుకుని తమ వినూత్నాన్ని డైనమిక్గా సవరిస్తే ఫీడ్‌బ్యాక్ లూప్‌లు అమలు చేయండి.

### మాడ్యూలర్ కంపోనెంట్లు ఉపయోగించండి

Microsoft Agent Framework వంటి SDKలు AI కనెక్టర్‌లు, టూల్ నిర్వచనాలు, మరియు ఏజెంట్ నిర్వహణ వంటి ముందు-నిర్మించబడిన భాగాలను అందిస్తాయి.

**బృందాలు ఇవి ఎలా ఉపయోగించుకోవచ్చు**: బృందాలు ఈ భాగాలను త్వరగా చేర్చుకుని ఫంక్షనల్ ప్రోటోటైప్‌ను ప్రారంభించగలవు, శూన్యంగా మొదలుపెట్టకుండా త్వరగా ప్రయోగాలు మరియు ఇటరేషన్స్ చేయడానికి అనుమతిస్తుంది.

**విభక్తిలో ఇది ఎలా పని చేస్తుంది**: వినియోగదారు ఇన్‌పుట్ నుండి సమాచారాన్ని ఎక్స్‌ట్రాక్ట్ చేయడానికి ముందు-నిర్మిత పార్సర్, డేటా నిల్వయించడానికి మరియు పునఃప్రాప్తి కోసం మెమరీ మాడ్యూల్, మరియు వినియోగదారులతో పరస్పర చర్య చేయడానికి ప్రాంప్ట్ జనరేటర్ ఉపయోగించవచ్చు, ఇవి అన్ని మూలంగా నిర్మించకుండానే.

**ఉదాహరణ కోడ్**. Microsoft Agent Framework ను `AzureAIProjectAgentProvider` తో ఎలా ఉపయోగించవచ్చో ఉదాహరణ చూద్దాం మరియు మోడల్ వినియోగదారు ఇన్‌పుట్‌ను టూల్ కాలింగ్‌తో స్పందించేలా చేయండి:

``` python
# Microsoft ఏజెంట్ ఫ్రేమ్‌వర్క్ పైథాన్ ఉదాహరణ

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# ప్రయాణం బుక్ చేసేందుకు ఒక నమూనా టూల్ ఫంక్షన్ నిర్వచించండి
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
    # ఉదాహరణ ఫలితం: 2025 జనవరి 1న మీ న్యూ యార్క్ విమానం విజయవంతంగా బుక్ అయింది. సురక్షిత ప్రయాణాలు! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ఈ ఉదాహరణలో మీరు చూడగలిగేది ఏమిటంటే, వినియోగదారు ఇన్‌పుట్ నుండి మూల సమాచారాన్ని (ఉదాహరణకు విమాన బుకింగ్ అభ్యర్థనకు’origine, destination, మరియు date’) తీసివెయ్యడానికి ముందు-నిర్మిత పార్సర్‌ను మీరు ఎలా ఉపయోగించవచ్చో. ఈ మాడ్యూలర్ దృష్టికోణం మీకు హై-లెవల్ లాజిక్‌పై దృష్టి సారించే అవకాశం కల్పిస్తుంది.

### సహకార సాధనాలను లావించుకోండి

Microsoft Agent Framework వంటి ఫ్రేమ్‌వర్క్‌లు కలిసి పని చేయగల బహుళ ఏజెంట్ల సృష్టిని సులభతరం చేస్తాయి.

**బృందాలు ఇవి ఎలా ఉపయోగించుకోవచ్చు**: బృందాలు నిర్దిష్ట పాత్రలు మరియు పనులు కలిగిన ఏజెంట్లను డిజైన్ చేయవచ్చు, అవి సహకార వర్క్‌ఫ్లోలను పరీక్షించి మెరుగు పరచడానికి మరియు మొత్తం వ్యవస్థ సామర్థ్యాన్ని పెంచడానికి వీలుగా ఉంటాయి.

**విభక్తిలో ఇది ఎలా పని చేస్తుంది**: ప్రతి ఏజెంట్‌కు డేటా రిట్రీవల్, విశ్లేషణ, లేదా నిర్ణయాలు తీసుకునేలా ప్రత్యేక ఫంక్షన్ ఉండేలా ఒక ఏజెంట్ల జట్టును మీరు సృష్టించవచ్చు. ఈ ఏజెంట్లు సాధారణ లక్ష్యాన్ని సాధించడానికి సమాచారాన్ని కమ్యూనికేట్ చేసి పంచుకోవచ్చు, ఉదాహరణకు వినియోగదారుడి ప్రశ్నను సమాధానించడం లేదా ఒక పని పూర్తిచేయడం.

**ఉదాహరణ కోడ్ (Microsoft Agent Framework)**:

```python
# Microsoft Agent Framework ఉపయోగించి కలిసి పని చేసే అనేక ఏజెంట్లను సృష్టించడం

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# డేటా రీకవరీ ఏజెంట్
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

# ఒక పనిపై ఏజెంట్లను అనుక్రమంలో నడపడం
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

పూర్వాన్ని ఉన్న కోడ్‌లో మీరు చూడగలిగేది ఏంటంటే, బహుళ ఏజెంట్లు కలిసి డేటాను విశ్లేషించడానికి పనిచేసే ఒక పని ఎలా సృష్టించవచ్చో చూపిస్తుంది. ప్రతి ఏజెంట్ ప్రత్యేకమైన ఫంక్షన్‌ని నిర్వహిస్తుంది, మరియు లక్ష్యాన్ని సాధించడానికి ఏజెంట్ల సమన్వయంతో పని నిర్వర్తింపబడుతుంది. ప్రత్యేక పాత్రలతో మార్గనిర్దేశించబడిన ఏజెంట్లను సృష్టించడం ద్వారా, మీరు పని సామర్థ్యాన్ని మరియు పనితీరును మెరుగుపరచవచ్చు.

### రియల్-టైమ్‌లో నేర్చుకోండి

అధునాతన ఫ్రేమ్‌వర్క్‌లు రియల్-టైమ్ సందర్భ ఆలోచనా మరియు అనుకూలత కోసం సామర్థ్యాలను అందిస్తాయి.

**బృందాలు ఇవి ఎలా ఉపయోగించుకోవచ్చు**: ఏజెంట్లు పరస్పర చర్యల నుండి నేర్చుకుని తమ ప్రవర్తనను డైనమిక్గా సవరించుకునే ఫీడ్‌బ్యాక్ లూప్‌లను బృందాలు అమలు చేయగలవు, దీని వల్ల సామర్థ్యాలు నిరంతర మెరుగుదల మరియు సవరణకు గురవుతాయి.

**విభక్తిలో ఇది ఎలా పని చేస్తుంది**: ఏజెంట్లు వినియోగదారు ఫీడ్‌బ్యాక్, పరిసర డేటా, మరియు పనినిర్వహణ ఫలితాలను విశ్లేషించి తమ జ్ఞానాకరణాన్ని నవీకరించుకోవచ్చు, నిర్ణయల తీసుకునే అల్గోరిథమ్‌లను సర్దుబాటు చేయొచ్చు, మరియు కాలక్రమేణా పనితీరును మెరుగుపరచొచ్చు. ఈ పునరావృత నేర్చుకునే ప్రక్రియ ఏజెంట్లను మారుతున్న పరిస్థితులకు మరియు వినియోగదారుల ప్రాధాన్యాలకు అనుగుణంగా మారడానికి వీలు కల్పిస్తుంది, అంతిమంగా మొత్తం వ్యవస్థ ప్రభావాన్ని పెంపొందిస్తుంది.

## Microsoft Agent Framework మరియు Azure AI Agent Service మధ్య తేడాలు ఏమిటి?

ఈ దారులను సరసమైన రూపంలో పోల్చడానికి అనేక మార్గాలు ఉన్నాయి, కానీ వారి డిజైన్, సామర్థ్యాలు, మరియు లక్ష్య వాడుక సంస్థలు సంబంధించి కొన్ని ప్రధాన తేడాలను చూద్దాం:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `AzureAIProjectAgentProvider` ఉపయోగించి AI ఏజెంట్లను నిర్మించడానికి సరళీకృత SDKని అందిస్తుంది. ఇది డెవలపర్లకు Azure OpenAI మోడల్స్‌ను ఉపయోగించి టూల్ కాలింగ్, సంభాషణ నిర్వహణ, మరియు Azure ఐడెంటిటి ద్వారా ఎంటర్‌ప్రైజ్-గ్రేడ్ భద్రత కలిగి ఏజెంట్లను సృష్టించడానికి అనుమతిస్తుంది.

**వినియోగ సందర్భాలు**: టూల్ వినియోగం, బహుళ-దశ వర్క్‌ఫ్లోలు, మరియు ఎంటర్‌ప్రైజ్ ఇంటిగ్రేషన్ السينారియోలతో ప్రొడక్షన్-రెడీ AI ఏజెంట్లను నిర్మించడం.

ఇక్కడ Microsoft Agent Framework యొక్క కొన్ని ముఖ్యమైన కోర్ కాన్సెప్ట్‌లు ఉన్నాయి:

- **ఏజెంట్లు**. ఒక ఏజెంట్ `AzureAIProjectAgentProvider` ద్వారా సృష్టించబడుతుంది మరియు ఒక పేరు, సూచనలు, మరియు టూల్స్‌తో కాన్ఫిగర్ చేయబడుతుంది. ఏజెంట్ చేయగలదు:
  - **వినియోగదారు సందేశాలను ప్రాసెస్ చేయడం** మరియు Azure OpenAI మోడల్స్‌ను ఉపయోగించి స్పందనలు ఉత్పత్తి చేయడం.
  - **ఆటోమాటిక్గా టూల్స్‌ను కాల్ చేయడం** సంభాషణ సందర్భాన్ని ఆధారంగా.
  - **బహుళ పరస్పర చర్యలపై సంభాషణ స్థితిని నిర్వహించడం**.

  ఇక్కడ ఏజెంట్‌ను సృష్టించడం ఎలా అనేది చూపించే ఒక కోడ్ స్నిపెట్ ఉంది:

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

- **టూల్స్**. ఫ్రేమ్‌వర్క్ ఏజెంట్ స్వయంచాలకంగా ఆహ్వానించగల Python ఫంక్షన్‌లుగా టూల్స్‌ను నిర్వచించడాన్ని మద్దతు ఇస్తుంది. ఏజెంటును సృష్టించేటప్పుడు టూల్స్ నమోదు చేయబడతాయి:

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

- **బహుళ-ఏజెంట్ సమన్వయం**. మీరు విభిన్న ప్రత్యేకతలతో బహుళ ఏజెంట్లను సృష్టించి వారి పనిని సమన్వయించవచ్చు:

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

- **Azure Identity ఇంటిగ్రేషన్**. ఫ్రేమ్‌వర్క్ సురక్షిత, కీ-లెస్ ప్రమాణీకరణ కోసం `AzureCliCredential` (లేదా `DefaultAzureCredential`) ను ఉపయోగిస్తుంది, ఇది API కీలు నేరుగా నిర్వహించాల్సిన అవసరాన్ని తొలగిస్తుంది.

## Azure AI Agent Service

Azure AI Agent Service Microsoft Ignite 2024లో పరిచయం చేయబడిన తాజాగా వచ్చిన పరిచయం. ఇది Llama 3, Mistral, మరియు Cohere వంటి ఓపెన్-సోర్స్ LLMలను నేరుగా కాల్ చేయగల వంటి మరింత ఫ్లెక్సిబుల్ మోడల్స్‌తో AI ఏజెంట్ల అభివృద్ధి మరియు డిప్లాయ్మెంట్‌ను అనుమతిస్తుంది.

Azure AI Agent Service బలమైన ఎంటర్‌ప్రైజ్ భద్రతా మెకానిజమ్స్ మరియు డేటా స్టోరేజ్ పద్ధతులను అందిస్తుంది, దీని వల్ల ఇది ఎంటర్‌ప్రైజ్ అప్లికేషన్లకు అనువుగా ఉంటుంది.

ఇది Microsoft Agent Frameworkతో బాక్సులో పని చేయి, ఏజెంట్లను నిర్మించడానికి మరియు డిప్లాయ్ చేయడానికి అవుట్-ఆఫ్-ది-బాక్స్ అనుభవాన్ని అందిస్తుంది.

ఈ సేవ ప్రస్తుతం Public Previewలో ఉంది మరియు ఏజెంట్లు నిర్మించడానికి Python మరియు C# మద్దతు చేస్తుంది.

Azure AI Agent Service Python SDK ఉపయోగించి, వినియోగదారు నిర్వచించిన టూల్‌తో ఒక ఏజెంట్‌ని ఇలా సృష్టించవచ్చు:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# సాధన కార్యాచరణలను నిర్వచించండి
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

Azure AI Agent Service కింద ఈ క్రింది ప్రధాన కాన్సెప్ట్‌లు ఉన్నాయి:

- **ఏజెంట్**. Azure AI Agent Service Microsoft Foundryతో సమీకరించబడింది. AI Foundryలో, ఒక AI ఏజెంట్ ఒక "స్మార్ట్" మైక్రోసర్వీస్‌లా పనిచేస్తుంది, ఇది ప్రశ్నలకు సంబంధించిన సమాధానాలు (RAG), చర్యలు చేపట్టడం, లేదా పూర్తిగా వర్క్‌ఫ్లోలను ఆటోమేట్ చేయడానికి ఉపయోగించవచ్చు. ఇది జనరేటివ్ AI మోడల్స్ శక్తిని రియల్-వరల్డ్ డేటా సోర్సుల్ని యాక్సెస్ చేసి పరస్పర చర్య చేయగల టూల్స్‌తో కలపడం ద్వారా సాధిస్తుంది. ఇక్కడ ఒక ఏజెంట్ యొక్క ఉదాహరణ ఉంది:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ఈ ఉదాహరణలో, ఒక ఏజెంట్ `gpt-4o-mini` మోడల్‌తో, పేరు `my-agent`, మరియు సూచనలు `You are helpful agent` తో సృష్టించబడింది. ఏజెంట్ కోడ్ ఇంటర్ప్రిటేషన్ పనులను చేయడానికి అవసరమైన టూల్స్ మరియు వనరులతో సజ్జమైనది.

- **థ్రెడ్ మరియు సందేశాలు**. థ్రెడ్ మరో ముఖ్యమైన కాన్సెప్ట్. ఇది ఏజెంట్ మరియు వినియోగదారుడి మధ్య సంభాషణ లేదా పరస్పర చర్యను సూచిస్తుంది. థ్రెడ్లు సంభాషణ పురోగమనాన్ని ట్రాక్ చేయడానికి, సందర్భ సమాచారాన్ని నిల్వ చేయడానికి, మరియు పరస్పర చర్య యొక్క స్థితిని నిర్వహించడానికి ఉపయోగించబడతాయి. ఇక్కడ ఒక థ్రెడ్ యొక్క ఉదాహరణ ఉంది:

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

    పూర్వలోని కోడ్‌లో, ఒక థ్రెడ్ సృష్టించబడింది. అంత తర్వాత, ఒక సందేశం థ్రెడ్‌కు పంపబడింది. `create_and_process_run` ను కాల్ చేయడం ద్వారా, ఏజెంట్‌ను థ్రెడ్‌పై పని చేయమని అడుగుతుంది. చివరగా, ఏజెంట్ యొక్క స్పందన చూడటానికి సందేశాలను పొందించి లాగ్ చేయబడతాయి. సందేశాలు వినియోగదారు మరియు ఏజెంట్ మధ్య సంభాషణ పురోగమనాన్ని సూచిస్తాయి. సందేశాలు వచనం, చిత్రం, లేదా ఫైల్ వంటి వివిధ రకాలుగా ఉండగలవు అని కూడా అర్థం చేసుకోవాలి; ఉదాహరణకు ఏజెంట్ పని ఫలితంగా ఒక చిత్రం లేదా వచన స్పందనను ఫలితంగా ఇవ్వవచ్చు. ఒక డెవలపర్‌గా, మీరు ఆ సమాచారాన్ని మరింత ప్రాసెస్ చేయడానికి లేదా వినియోగదారుడికి ప్రదర్శించడానికి తర్వాత ఉపయోగించవచ్చు.

- **Microsoft Agent Frameworkతో సమీకరణం**. Azure AI Agent Service Microsoft Agent Frameworkతో సజావుగా పనిచేస్తుంది, అంటే మీరు `AzureAIProjectAgentProvider` ఉపయోగించి ఏజెంట్లను నిర్మించి వాటిని ప్రొడక్షన్ సన్నివేశాల కోసం Agent Service ద్వారా డిప్లాయ్ చేయగలరు.

**వినియోగ సందర్భాలు**: Azure AI Agent Service సెక్యూర్, స్కేలబుల్, మరియు ఫ్లెక్సిబుల్ AI ఏజెంట్ డిప్లాయ్మెంట్ అవసరమయ్యే ఎంటర్‌ప్రైజ్ అప్లికేషన్ల కోసం రూపొందించబడింది.

## ఈ దారుల మధ్య తేడా ఏమిటి?

ఒకదాన్ని మరొకటి తో పోల్చితే ఓవర్లాప్ ఉన్నట్లు అనిపించవచ్చు, కానీ వారి డిజైన్, సామర్థ్యాలు, మరియు లక్ష్య వాడుక సంఘాల పరంగా కొన్ని ముఖ్య తేడాలు కలవు:

- **Microsoft Agent Framework (MAF)**: టూల్ కాలింగ్‌తో కూడిన ఏజెంట్లను నిర్మించడానికి ప్రొడక్షన్-రెడీ SDK. ఇది ఏజెంట్లను టూల్ కాలింగ్, సంభాషణ నిర్వహణ, మరియు Azure ఐడెంటిటి ఇంటిగ్రేషన్‌తో సృష్టించడానికి సరళీకృత APIని అందిస్తుంది.
- **Azure AI Agent Service**: ఏజెంట్ల కోసం Azure Foundryలోని ఒక ప్లాట్‌ఫారమ్ మరియు డిప్లాయ్‌మెంట్ సేవ. ఇది Azure OpenAI, Azure AI Search, Bing Search మరియు కోడ్ ఎగ్జిక్యూషన్ వంటి సేవలకు బిల్ట్-ఇన్ కనెక్టివిటీని అందిస్తుంది.

ఇంకా ఎంచుకోవాలో తెలియకపోతే?

### వినియోగ సందర్భాలు

కొన్ని సాధారణ వినియోగ సందర్భాల ద్వారా మీకు సహాయపడుదామా చూసేద్దాం:

> Q: I'm building production AI agent applications and want to get started quickly
>

>A: The Microsoft Agent Framework is a great choice. It provides a simple, Pythonic API via `AzureAIProjectAgentProvider` that lets you define agents with tools and instructions in just a few lines of code.

>Q: I need enterprise-grade deployment with Azure integrations like Search and code execution
>
> A: Azure AI Agent Service is the best fit. It's a platform service that provides built-in capabilities for multiple models, Azure AI Search, Bing Search and Azure Functions. It makes it easy to build your agents in the Foundry Portal and deploy them at scale.
 
> Q: I'm still confused, just give me one option
>
> A: Start with the Microsoft Agent Framework to build your agents, and then use Azure AI Agent Service when you need to deploy and scale them in production. This approach lets you iterate quickly on your agent logic while having a clear path to enterprise deployment.
 
కొన్ని ముఖ్య తేడాలను పట్టికలో సారాంశం చేద్దాం:

| ఫ్రేమ్‌వర్క్ | ఫోకస్ | ప్రధాన కాన్సెప్ట్‌లు | ఉపయోగాల కేసులు |
| --- | --- | --- | --- |
| Microsoft Agent Framework | టూల్ కాలింగ్‌తో సరళీకృత ఏజెంట్ SDK | ఏజెంట్లు, టూల్స్, Azure Identity | AI ఏజెంట్‌లు నిర్మించడం, టూల్ వినియోగం, బహుళ-దశ వర్క్‌ఫ్లోలు |
| Azure AI Agent Service | ఫ్లెక్సిబుల్ మోడల్స్, ఎంటర్‌ప్రైజ్ భద్రత, కోడ్ జనరేషన్, టూల్ కాలింగ్ | మాడ్యులారిటీ, సహకారం, ప్రాసెస్ ఆర్కెస్ట్రేషన్ | సెక్యూర్, స్కేలబుల్, మరియు ఫ్లెక్సిబుల్ AI ఏజెంట్ డిప్లాయ్మెంట్ |

## నేను నా ఉన్నత Azure ఎకోసిస్టమ్ సాధనాలను నేరుగా ఇంటిగ్రేట్ చేయగలనా, లేక వేరే స్టాండ్‌లోన్ పరిష్కారాలు అవసరమా?
సమాధానం: అవును — మీరు మీ υπάρగ్రహించిన Azure ఎకోసిస్టమ్ టూల్స్‌ను ప్రత్యేకంగా Azure AI Agent Service తో నేరుగా ఏకీకృతం చేయవచ్చు, ఇది ఇతర Azure సేవలతో సజావుగా పనిచేయడానికి రూపొందించబడింది. ఉదాహరణకి మీరు Bing, Azure AI Search, మరియు Azure Functions ని ఏకీకృతం చేయవచ్చు. Microsoft Foundry తో కూడా లోతైన ఇంటిగ్రేషన్ ఉంది.

Microsoft Agent Framework కూడా `AzureAIProjectAgentProvider` మరియు Azure identity ద్వారా Azure సేవలతో ఇంటిగ్రేట్ అవుతుంది, ఇది మీ ఏజెంట్ టూల్స్ నుండి నేరుగా Azure సేవలను పిలవడానికి అనుమతిస్తుంది.

## నమూనా కోడ్‌లు

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌ల గురించి మరిన్ని ప్రశ్నలు ఉన్నా?

ఇతర నేర్చుకొనేవారిని కలవడానికి, ఆఫీస్ గంటలకు హాజరుకావడానికి మరియు మీ AI Agents‌కు సంబంధించిన ప్రశ్నలకు సమాధానాలు పొందడానికి [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)లో చేరండి.

## సూచనలు

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure ఏజెంట్ సర్వీస్</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI స్పందనలు</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI ఏజెంట్ సర్వీస్</a>

## గత పాఠం

[AI ఏజెంట్స్ మరియు ఏజెంట్ వినియోగ కేసుల ప్రవేశం](../01-intro-to-ai-agents/README.md)

## తదుపరి పాఠం

[ఏజెంటిక్ డిజైన్ ప్యాటర్న్‌లను అర్థం చేసుకోవడం](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ దస్త్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించారు. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, స్వయంచాలిత అనువాదాల్లో తప్పులు లేదా తెల్లింపులేమి ఉండొచ్చు. స్థానిక భాషలోని అసలు పత్రం ఆధారముగా పరిగణించాలి. కీలకమైన సమాచారం కోసం నిపుణులైన మానవ అనువాదాన్ని ఉపయోగించడం సూచించబడుతుంది. ఈ అనువాదాన్ని ఉపయోగించడం వలన కలిగే ఏవైనా గందరగోళాలు లేదా తప్పుగా అర్థం చేసుకోవడంపై మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->