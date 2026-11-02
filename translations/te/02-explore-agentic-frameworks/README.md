[![AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లను అన్వేషించడం](../../../translated_images/te/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ఈ పాఠం వీడియోను చూడటానికి పై చిత్రం పై క్లిక్ చేయండి)_

# AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లను అన్వేషించండి

AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు AI ఏజెంట్ల సృష్టి, డిప్లాయ్‌మెంట్ మరియు నిర్వహణను సులభతరం చేయడానికి రూపొందించిన సాఫ్ట్‌వేర్ ప్లాట్‌ఫారం. ఈ ఫ్రేమ్‌వర్క్‌లు డెవలపర్లకు ముందుగా తయారు చేయబడిన భాగాలు, అభియానం, మరియు సాధనాలను అందజేస్తాయి, ఇవి సంక్లిష్ట AI సిస్టమ్‌ల అభివృద్ధిని సులభతరం చేస్తాయి.

ఈ ఫ్రేమ్‌వర్క్‌లు AI ఏజెంట్ అభివృద్ధిలో సాధారణ సవాళ్ళకు ప్రమాణపూర్వక మార్గాలను అందిస్తూ, అభివృద్ధికారులు తమ అప్లికేషన్ల విభిన్నాంశాలపై దృష్టి పెట్టటానికి సహాయపడతాయి. ఇవి AI సిస్టమ్ నిర్మాణంలో వ్యాప్తి, ప్రాప్తి మరియు సామర్థ్యాన్ని పెంచుతాయి.

## పరిచయం 

ఈ పాఠం కిందివి కవర్ చేయబడతాయి:

- AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు ఏమిటి మరియు ఇవి డెవలపర్లకు ఏం సాధించేందుకు అనుమతిస్తాయి?
- టీమ్స్ వీటిని ఎలా ఉపయోగించి త్వరగా ప్రోటోటైప్ చేయవచ్చు, పునరావృతం చేయవచ్చు, మరియు వారి ఏజెంట్ సామర్థ్యాలను మెరుగుపరుచుకోవచ్చు?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> మరియు <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) చేత సృష్టించబడిన ఫ్రేమ్‌వర్క్‌లు మరియు సాధనాల మధ్య భేదాలు ఏమిటి?
- నేను నా ప్రస్తుతం ఉన్న Azure ఎకోసిస్టమ్ సాధనాలను నేరుగా సమ్మిళితం చేయదలుచుకున్నాను, లేదా నేను స్టాండ్అలోన్ పరిష్కారాలు అవసరమా?
- Microsoft Foundry Agent Service ఏమిటి మరియు ఇది నాకు ఎలా సహాయపడుతోంది?

## నేర్చుకున్న లక్ష్యాలు

ఈ పాఠం లక్ష్యాలు మీకు సహాయపడతాయి:

- AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు AI అభివృద్ధి లో ఎలాంటి పాత్ర పోషిస్తాయో.
- తెలివైన ఏజెంట్లను రూపొందించడానికి AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లను ఎలా వినియోగించాలో.
- AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌ల ద్వారా సాదించగల ముఖ్య సామర్థ్యాలు.
- Microsoft Agent Framework మరియు Microsoft Foundry Agent Service మధ్య తేడాలు.

## AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు ఏమిటి మరియు అవి డెవలపర్లకు ఏమి చేస్తాయి?

పారంపర్య AI ఫ్రేమ్‌వర్క్‌లు మీ యాప్స్‌లో AIని ఏకీకృతం చేయడంలో, మరియు ఈ యాప్స్‌ను మెరుగుపరచడంలో సహాయపడతాయి, కిందివిధంగా:

- **వ్యక్తిగతీకరణ**: AI వినియోగదారు ప్రవర్తన మరియు ఇష్టాలను విశ్లేషించి వ్యక్తిగతమైన సిఫార్సులు, విషయం మరియు అనుభవాలను అందించగలదు.
ఉదాహరణ: Netflix వంటి స్ట్రీమింగ్ సర్వీసులు వీక్షణ చరిత్ర ఆధారంగా సినిమాలు మరియు షోలు సిఫార్సు చేస్తూ వినియోగదారు భాగస్వామ్యాన్ని మరియు సంతృప్తిని పెంచుతాయి.
- **ఆటోమేషన్ మరియు సామర్థ్యం**: AI పునరావృత పనులు ఆటోమేటు చేసి, పనిముట్టును వేగవంతం చేసి, కార్యకలాప సామర్థ్యాన్ని మెరుగుపరుస్తుంది.
ఉదాహరణ: కస్టమర్ సేవా యాప్స్ AI-చాలిత చాట్‌బాట్లను ఉపయోగించి సాధారణ విచారణలను నిర్వహిస్తాయి, స్పందన సమయాన్ని తగ్గిస్తూ మరియు మానవ ఏజెంట్లను క్లిష్టమైన సమస్యల కోసం ఉచితంగా ఉంచుతాయి.
- **మెరుగైన వినియోగదారు అనుభవం**: AI వాయిస్ గుర్తింపు, సహజ భాష ప్రక్రియ, మరియు అంచనా టెక్స్ట్ వంటి తెలివైన ఫీచర్లను అందించి సర్వముఖ అనుభవాన్ని మెరుగుపరుస్తుంది.
ఉదాహరణ: Siri మరియు Google Assistant వంటి వర్చువల్ సహాయకులు గొప్పగా వాయిస్ ఆదేశాలను అర్థం చేసుకొని స్పందిస్తూ వినియోగదారులకు తమ డివైస్‌లతో సౌకర్యవంతమైన పరస్పరం అందిస్తారు.

### ఇవన్నీ అద్భుతంగా వినిపిస్తాయి కాబట్టి AI ఏజెంట్ ఫ్రేమ్‌వర్క్ ఎందుకు అవసరం?

AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లు సాధారణ AI ఫ్రేమ్‌వర్క్‌ల కన్నా ఎక్కువది. అవి వినియోగదారులతో, ఇతర ఏజెంట్లతో మరియు పరిసరాలతో పరస్పరం చేయగల తెలివైన ఏజెంట్ల సృష్టిని సాధ్య పరుస్తాయి, ప్రత్యేక లక్ష్యాలను చేరుకోవడానికి. ఈ ఏజెంట్లు స్వయం-నిర్వాహక ప్రవర్తనను ప్రదర్శించగలవు, నిర్ణయాలు తీసుకోవచ్చు మరియు మారుతున్న పరిస్థితులకు అనుగుణంగా కలిగించగలవు. AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌ల ద్వారా సాధ్యమయ్యే కొన్ని ముఖ్య సామర్థ్యాలు ఇక్కడ ఉన్నాయి:

- **ఏజెంట్ సహకారం మరియు సమన్వయం**: అనేక AI ఏజెంట్ల సృష్టిని సాధ్యపరుస్తు ఒకే లక్ష్యం కోసం ప్రస్తావన, సంభాషణ మరియు సమన్వయంతో కష్టసాధ్యమైన పనులను చేద్దాము.
- **పని ఆటోమేషన్ మరియు నిర్వహణ**: బహుళ దశల కార్యప్రవాహాలను ఆటోమేటు చేయడం, పనులను ప్రత్యామ్నాయం చేయడం మరియు ఏజెంట్ల మధ్య డైనమిక్ పనిముట్టును నిర్వహించడం కోసం నిర్వహణ పద్ధతులు అందించే.
- **సందర్భాన్ని అర్థం చేసుకోవడం మరియు అనుగుణంగా మారడం**: ఏజెంట్లు సందర్భాన్ని అర్థం చేసుకొని, మారుతున్న పరిసరాలకు అనుగుణంగా మారిపోడానికి, మరియు నిజ సమయ సమాచారం ఆధారంగా నిర్ణయాలు తీసుకోవడానికి సామర్థ్యాన్ని కలిగించటం.

అందువలన సారాంశంగా, ఏజెంట్లు మిమ్మల్ని మరిన్ని పనులు చేయనివ్వును, ఆటోమేషన్‌ని తదుపరి స్థాయికి తీసుకెళ్లును, పరిసరాల నుంచి అర్థం చేసుకుని నేర్చుకునే మేధస్సుగల సిస్టమ్‌లను సృష్ఠించవచ్చు.

## ఏజెంట్ సామర్థ్యాలను త్వరగా ప్రోటోటైప్ చేయడానికి, పునరావృతం చేయడానికి మరియు మెరుగుపరచడానికి ఎలా?

ఇది వేగంగా అభివృద్ధి చెందుతున్న రంగం కాగా, చాలా AI ఏజెంట్ ఫ్రేమ్‌వర్క్‌లలో సాధారణంగా ఉన్న కొన్ని అంశాలు ఉన్నాయి: మాడ్యులర్ భాగాలు, సహకార సాధనాలు మరియు నిజ-సమయ నేర్చుకునే విధానాలు. వీటిని చూద్దాం:

- **మాడ్యులర్ భాగాలను ఉపయోగించండి**: AI SDK‌లు ముందే రూపొందించిన భాగాలను అందిస్తాయి, ఉదా. AI మరియు మెమరీ కనెక్టర్లు, సహజ భాష లేదా కోడ్ ప్లగిన్ల ద్వారా ఫంక్షన్ కాలింగ్, ప్రాంప్ట్ టెంప్లేట్లు మొదలగు.
- **సహకార సాధనాలను వినియోగించండి**: నిర్దిష్ట పాత్రలు మరియు పనులను కలిగిన ఏజెంట్లు రూపొందించి, సహకార కార్యప్రవాహాలను పరీక్షించి మెరుగుపరచగలరు.
- **నిజ-సమయ నేర్చుకోండి**: ఏజెంట్లు పరస్పర సంబంధాల నుంచి నేర్చుకుని ప్రవర్తనను డైనమిక్గా సర్దుబాటు చేసుకునే ఫీడ్‌బ్యాక్ లూప్‌లను అమలు చేయండి.

### మాడ్యులర్ భాగాలను ఉపయోగించండి

Microsoft Agent Framework వంటి SDKలు AI కనెక్టర్‌లు, సాధన నిర్వచనాలు మరియు ఏజెంట్ నిర్వహణ వంటి ముందుగా తయారు చేయబడిన భాగాలను అందిస్తాయి.

**గుంపులు దీనిని ఎలా ఉపయోగించగలవు**: గుంపులు ఈ భాగాలను వెంటనే యిక్కడ వేయించుకొని ఫంక్షనల్ ప్రోటోటైప్‌ను సృష్టించవచ్చు, దీని వల్ల వీరు త్వరగా ప్రయోగాలు మరియు పునరావృతాలు చేయవచ్చు.

**ప్రాక్టీస్‌లో ఇది ఎలా పనిచేస్తుంది**: మీరు వినియోగదారు ఇన్‌పుట్ నుండి సమాచారాన్ని తీసుకునే ముందుగా తయారుచేసిన పార్సర్, డేటాను నిల్వ చేసే మెమరీ మాడ్యూల్, మరియు వినియోగదారులతో ఇంటరాక్ట్ చేసే ప్రాంప్ట్ జనరేటర్‌ని ఉపయోగించవచ్చు, ఇవన్నీ ప్రారంభం నుంచి నిర్మించాల్సిన అవసరం లేని.

**ఉదాహరణ కోడ్**. మోడల్ వినియోగదారు ఇన్‌పుట్‌కు టూల్ కాలింగ్‌తో స్పందించడానికి Microsoft Agent Frameworkని `FoundryChatClient`తో ఎలా ఉపయోగించవచ్చో చూద్దాం:

``` python
# Microsoft Agent Framework పైథాన్ ఉదాహరణ

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# ప్రయాణం బుకింగ్‌ కోసం ఒక నమూనా టూల్ ఫంక్షన్‌ను paribhAsa
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
    # ఉదాహరణ అవుట్పుట్: 2025 జనవరి 1న మీ న్యూయార్క్ విమానం విజయవంతంగా బుక్ చేయబడింది. సురక్షిత ప్రయాణం! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ఈ ఉదాహరణ నుండి మీరు చూడొచ్చు వినియోగదారు ఇన్‌పుట్ నుండి ఎగుమతి చేయగలిగే ముఖ్య సమాచారాన్ని, ఉదా. వాయిస్, గమ్యం మరియు విమాన బుకింగ్ ఆర్డర్ తేదీ. ఈ మాడ్యులర్ విధానం మీకు ఉన్నత స్థాయి తర్కంపై దృష్టి పెట్టడానికి వీలు కల్పిస్తుంది.

### సహకార సాధనాలను వినియోగించండి

Microsoft Agent Framework వంటి ఫ్రేమ్‌వర్క్‌లు అనేక ఏజెంట్లు కలిసి పనిచేయగలగడం సులభతరం చేస్తాయి.

**గుంపులు దీనిని ఎలా ఉపయోగించగలవు**: నిర్దిష్ట పాత్రలు మరియు పనులతో ఏజెంట్లను రూపొందించి, సహకార కార్యప్రవాహాలను పరీక్షించి మెరుగుపరిచి చేర్చవచ్చు.

**ప్రాక్టీస్‌లో ఇది ఎలా పనిచేస్తుంది**: మీరు ప్రతి ఏజెంట్ ప్రత్యేక ఫంక్షన్ కలిగి, ఉదా. డేటా తిరిగి తీసుకోవడం, విశ్లేషణ, లేదా నిర్ణయాలు తీయడం వంటి, ఏజెంట్ల టీమ్‌ను ఆరంభించవచ్చు. ఈ ఏజెంట్లు సంభాషించడం మరియు సమాచారం పంచుకోవడం ద్వారా ఒక సాధారణ లక్ష్యాన్ని చేరుకోవచ్చు, ఉదా. వినియోగదారు ప్రశ్నకు సమాధానం లేదా పని పూర్తిచేయడం.

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

# డేటా పొందడం ఏజెంట్
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

# ఒక పనిపై ఏజెంట్లను వరుసగా నడిపించండి
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

మునుపటి కోడ్‌లో మీరు చూడగలరు అనేక ఏజెంట్లు కలిసి డేటాను విశ్లేషించేందుకు పనిచేస్తున్న ఒక పనిని సృష్టించడం. ప్రతి ఏజెంట్ ఒక ప్రత్యేక పని నిర్వర్తిస్తుంది, పనిని అనుసంధానించి ఫలితాన్ని సాధించడం. ప్రత్యేక పాత్రలతో డెడికేటెడ్ ఏజెంట్లను సృష్టించడం ద్వారా పని సామర్థ్యం మరియు ప్రదర్శన మెరుగుపడుతుంది.

### నిజ సమయాన్ని నేర్చుకోండి

ఆధునిక ఫ్రేమ్‌వర్క్‌లు నిరంతర సందర్భం అర్థం చేసుకోవడం మరియు అనుగుణంగా మారే సామర్థ్యాలు అందిస్తాయి.

**గుంపులు దీనిని ఎలా ఉపయోగించగలవు**: గుంపులు ఏజెంట్లు పరస్పర చర్యల నుంచి నేర్చుకుని ప్రవర్తనను డైనమిక్గా సర్దుబాటు చేసే ఫీడ్‌బ్యాక్ లూప్‌లు అమలు చేయవచ్చు, ఇది నిరంతర మెరుగుదల మరియు సామర్థ్య పునరావృతానికి దారితీస్తుంది.

**ప్రాక్టీస్‌లో ఇది ఎలా పనిచేస్తుంది**: ఏజెంట్లు వినియోగదారు ఫీడ్‌బ్యాక్, పరిసర డేటా మరియు పని ఫలితాలను విశ్లేషించి జ్ఞానాదారాన్ని నవీకరించవచ్చు, నిర్ణయం తీసుకునే అల్గోరిథంలను సర్దుచేసుకుని సమయానుకూలంగా ప్రదర్శన మెరుగుపరచగలవు. ఈ పునరావృత అధ్యయన ప్రక్రియ ఏజెంట్లను మారుతున్న పరిస్థితులకు మరియు వినియోగదారు ఇష్టాలకు అనుగుణంగా మారేలా చేస్తుంది, మొత్తంగా సిస్టమ్ ప్రభావాన్ని పెంచుతుంది.

## Microsoft Agent Framework మరియు Microsoft Foundry Agent Service మధ్య తేడాలు ఏమిటి?

వీటిని పోల్చడానికి ఎన్నో విధానాలు ఉన్నా, వారి రూపకల్పన, సామర్థ్యాలు మరియు లక్ష్య వినియోగ దశలను పరంగా కొన్ని ప్రధాన తేడాలను చూద్దాం:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `FoundryChatClient` ఉపయోగించి AI ఏజెంట్లను సృష్టించడానికిగాను సరళమైన SDK ని అందిస్తుంది. ఇది డెవలపర్లకు Azure OpenAI మోడల్స్‌తో టూల్ కాలింగ్, సంభాషణ నిర్వహణ మరియు Azure గుర్తింపు ద్వారా ఎంటర్ప్రైజ్-స్థాయి భద్రత కలిగిన ఏజెంట్లను సృష్టించడానికి అనుమతిస్తుంది.

**వినియోగ సందర్భాలు**: టూల్ వినియోగం, బహుళ దశల వర్క్‌ఫ్లోలు మరియు ఎంటర్ప్రైజ్ సమ్మిళిత పరిస్థితులతో ఉత్పత్తి సిద్ధమైన AI ఏజెంట్‌ల నిర్మాణం.

Microsoft Agent Framework యొక్క కొన్ని ముఖ్యమైన మూలభావాలు ఈ క్రింది విధంగా ఉన్నాయి:

- **ఏజెంట్లు**. ఏజెంట్ `FoundryChatClient` ద్వారా సృష్టించబడుతుంది మరియు పేరు, సూచనలు, టూల్స్‌తో కాన్ఫిగర్ చేయబడుతుంది. ఏజెంట్ చేయగలదు:
  - **వినియోగదారు సందేశాలను ప్రాసెస్ చేయడం** మరియు Azure OpenAI మోడల్స్ సహాయంతో స్పందనలు సృష్టించడం.
  - **చర్చ సందర్భం ఆధారంగా టూల్స్‌ను ఆటోమేటుగా కాల్ చేయడం**.
  - **బహుళ పరస్పర చర్యలలో సంభాషణ రాష్ట్రాన్ని నిర్వహించడం**.

  ఏజენტის సృష్టిని చూపే కోడ్ స్నిపెట్ ఇక్కడ ఉంది:

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

- **టూల్స్**. ఫ్రేమ్‌వర్క్ ఏజెంట్ ఆటోమేటిక్‌గా పిలవగల Python ఫంక్షన్ల రూపంలో టూల్స్‌ను నిర్వచించడాన్ని మద్దతు ఇస్తుంది. టూల్స్ ఏజెంట్ సృష్టినప్పుడు నమోదు చేయబడతాయి:

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

- **బహుళ ఏజెంట్ సమన్వయం**. వివిధ ప్రత్యేకతలతో అనేక ఏజెంట్లను సృష్టించి వాటి పనిని సమన్వయించవచ్చు:

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

- **Azure గుర్తింపు సమ్మిళనం**. ఫ్రేమ్‌వర్క్ `AzureCliCredential` (లేదా `DefaultAzureCredential`) ఉపయోగించి భద్రత కలిగిన, కీ లేని ధృవీకరణను అందిస్తుంది, ఇది API కీలు ప్రత్యక్షంగా నిర్వహించాల్సిన అవసరాన్ని తొలగిస్తుంది.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service Microsoft Ignite 2024 లో పరిచయమైన తాజా సేవ. ఇది Llama 3, Mistral, Cohere వంటి ఓపెన్-సోర్స్ LLM లను నేరుగా పిలవగల సామర్థ్యంతో మరింత గиб్బిగమయిన మోడల్స్ అందిస్తుంది.

Microsoft Foundry Agent Service బలమైన ఎంటర్ప్రైజ్ భద్రతా వ్యవస్థలు మరియు డేటా నిల్వ విధానాలను అందిస్తుంది, ఇది ఎంటర్ప్రైజ్ అప్లికేషన్లకు అనుకూలం.

ఇది Microsoft Agent Frameworkతో బాక్స్ నుండి సిద్దంగా సహకరిస్తుంది, ఏజెంట్లను నిర్మించి డిప్లాయ్ చేయడానికి.

ఈ సేవ ప్రస్తుతానికి పబ్లిక్ ప్రివ్యూ లో ఉంది మరియు ఏజెంట్ల సృష్టికి Python మరియు C# ని మద్దతు ఇస్తుంది.

Microsoft Foundry Agent Service Python SDKని ఉపయోగించి వినియోగదారు నిర్వచించిన టూల్‌తో ఏజెంట్ సృష్టించవచ్చు:

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

### మూల సిద్ధాంతాలు

Microsoft Foundry Agent Serviceకి క్రింది మూల సిద్ధాంతాలు ఉన్నాయి:

- **ఏజెంట్**. Microsoft Foundry Agent Service Microsoft Foundryతో సమ్మిళితం అవుతుంది. Microsoft Foundryలో, ఒక AI ఏజెంట్ "స్మార్ట్" మైక్రోసర్వీస్‌గా పనిచేస్తుంది, ఇది ప్రశ్నలకు (RAG), చర్యలు తీసుకోవడం, లేదా పూర్తిగా వర్క్‌ఫ్లోలను ఆటోమేట్ చేయగలదు. ఇది జనరేటివ్ AI మోడల్స్ శక్తిని నిజ ప్రపంచ డేటా వనరులతో ప్రాప్యత మరియు పరస్పర చర్య చేయగల సాధనాలతో కలిపి సాధిస్తుంది. ఏజెంట్ ఉదాహరణ ఇక్కడ ఉంది:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ఈ ఉదాహరణలో, `gpt-5-mini` మోడల్, `my-agent` పేరు మరియు `You are helpful agent` సూచనలు తో ఏజెంట్ సృష్టించబడింది. ఏజెంట్ కోడ్ వివరణ పనులను చేయడానికి టూల్స్ మరియు వనరులుతో సమకూర్చబడింది.

- **త్రెడ్ మరియు సందేశాలు**. త్రెడ్ మరో ముఖ్యమైన భావన. ఇది ఏజెంట్ మరియు వినియోగదారుతో సంభాషణ లేదా పరస్పర చర్యను సూచిస్తుంది. త్రెడ్‌లను సంభాషణ పురోగతిని ట్రాక్ చేయడానికి, సందర్భ సమాచారాన్ని నిల్వ చేయడానికి మరియు పరస్పర చర్య స్థితిని నిర్వహించడానికి ఉపయోగించవచ్చు. త్రెడ్ ఉదాహరణ ఇక్కడ ఉంది:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # ఏజెంట్‌ను థ్రెడ్‌పై పని చేయమని అడగండి
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # ఏజెంట్ స్పందనను చూడటానికి అన్ని సందేశాలను తీసుకుని లాగ్ చేయండి
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    మునుపటి కోడ్‌లో, త్రెడ్ సృష్టించబడింది. అందుతర్వాత, సందేశం త్రెడ్‌కి పంపబడింది. `create_and_process_run` కాల్ చేయడం ద్వారా ఏజెంట్ త్రెడ్‌లో పని చేయమని అడగబడ్డది. చివరగా, సందేశాలు తెచ్చి ఏజెంట్ స్పందనను నమోదు చేశారు. ఈ సందేశాలు వినియోగదారు మరియు ఏజెంట్ మధ్య సంభాషణ పురోగతిని సూచిస్తాయి. సందేశాలు వేరువేరు రకాల వుండవచ్చు, ఉదా. వచనం, చిత్రం, లేదా ఫైల్, అంటే ఏజెంట్ పని ఫలితంగా చిత్రం లేదా వచన స్పందన కలిగి ఉండవచ్చు. అభివృద్ధికారి గా మీరు ఈ సమాచారాన్ని తర్వాతి ప్రాసెస్ లేదా వినియోగదారుకు చూపించడానికి కావచ్చు.

- **Microsoft Agent Frameworkతో సమ్మేళనం**. Microsoft Foundry Agent Service Microsoft Agent Frameworkతో సున్నితంగా పని చేస్తుంది, అంటే మీరు `FoundryChatClient` ఉపయోగించి ఏజెంట్లను నిర్మించి, వాటిని ఏజెంట్ సర్వీస్ ద్వారా ఉత్పత్తి సన్నాహకాలకు పంపిణీ చేయవచ్చు.

**వినియోగ సందర్భాలు**: Microsoft Foundry Agent Service భద్రత కలిగిన, వ్యాప్తి సాధ్యమైన, మరియు తేలికపాటి AI ఏజెంట్ డిప్లాయ్‌మెంట్ అవసరమయ్యే ఎంటర్ప్రైజ్ అప్లికేషన్ల కోసం రూపొంది ఉంది.

## ఈ దశలను మధ్య తేడాలు ఏమిటి?
 
అవి కొంతవరకు సమం గానే కనబడుతున్నప్పటికీ, రూపకల్పన, సామర్థ్యాలు మరియు లక్ష్య వినియోగ దశల పరంగా కొన్ని ముఖ్య తేడాలు ఉన్నాయి:
 
- **Microsoft Agent Framework (MAF)**: AI ఏజెంట్లను నిర్మించడానికి ఉత్పత్తి సిద్ధమైన SDK. ఇది టూల్ కాలింగ్, సంభాషణ నిర్వహణ, మరియు Azure గుర్తింపు సమ్మిళనం తో ఒక సరళమైన API ని అందిస్తుంది.
- **Microsoft Foundry Agent Service**: Microsoft Foundryలో ఏజెంట్లు కోసం ఒక ప్లాట్‌ఫారం మరియు డిప్లాయ్‌మెంట్ సేవ. ఇది Azure OpenAI, Azure AI Search, Bing Search మరియు కోడ్ ఎగ్జిక్యూషన్ వంటి సేవలకు ఇంటిగ్రేషన్ కల్పిస్తుంది.
 
ఇంకా ఎంచుకోవాలో క్లారిటీ లేదు?

### వినియోగ సందర్భాలు
 
కొన్ని సాధారణ వినియోగ సందర్భాల ద్వారా మీకు సహాయం చేయగలమా చూద్దాం:
 
> ప్రశ్న: నేను ఉత్పత్తి స్థాయి AI ఏజెంట్ అప్లికేషన్లు రూపొందిస్తున్నాను మరియు త్వరగా ప్రారంభించాలనుకుంటున్నాను
>

>జవాబు: Microsoft Agent Framework మంచి ఎంపిక. ఇది `FoundryChatClient` ద్వారా టూల్స్ మరియు సూచనలతో ఏజెంట్లను కొన్ని కోడ్ లైన్లలో నిర్వచించడానికి సహజమైన Python API అందిస్తుంది.

>ప్రశ్న: నాకు Azure Search మరియు కోడ్ ఎగ్జిక్యూషన్ వంటి ఇంటిగ్రేషన్లతో ఎంటర్ప్రైజ్ స్థాయి డిప్లాయ్‌మెంట్ కావాలి
>
> జవాబు: Microsoft Foundry Agent Service ఉత్తమం. ఇది ఫౌండ్రీ పోర్టల్‌లో మీ ఏజెంట్లను సులభంగా నిర్మించి స్థాయిలో పంపిణీ చేయడానికి అనేక మోడల్స్, Azure AI Search, Bing Search మరియు Azure Functionsతో బిల్ట్-ఇన్ సామర్థ్యాలను అందిస్తుంది.
 
> ప్రశ్న: నాకు ఇంకా గందరగోళం ఉంది, ఒకే ఒక ఎంపిక చెప్పండి
>
> జవాబు: Microsoft Agent Frameworkతో మీ ఏజెంట్లను నిర్మించడం ప్రారంభించండి, ఆపై Microsoft Foundry Agent Serviceని ఉత్పత్తిలో పంపిణీకి ఉపయోగించండి. ఈ విధానం మీ ఏజెంట్ తర్కంపై త్వరగా పునరావృతం అనుమతిస్తూ ఎంటర్ప్రైజ్ డిప్లాయ్‌మెంట్‌కు స్పష్టమైన మార్గాన్ని అందిస్తుంది.
 
కీ తేడాలను పట్టికలో సరాంశం చేద్దాం:

| ఫ్రేమ్‌వర్క్ | దృష్టి | మూల సిద్ధాంతాలు | వినియోగ సందర్భాలు |
| --- | --- | --- | --- |
| Microsoft Agent Framework | టూల్ కాలింగ్‌తో సరళ agent SDK | ఏజెంట్లు, టూల్స్, Azure గుర్తింపు | AI ఏజెంట్లు నిర్మాణం, టూల్ వినియోగం, బహుళ దశల వర్క్‌ఫ్లోలు |
| Microsoft Foundry Agent Service | తేలికపాటి మోడల్స్, ఎంటర్ప్రైజ్ భద్రత, కోడ్ ఉత్పత్తి, టూల్ కాలింగ్ | మాడ్యులరిటి, సహకారం, ప్రాసెస్ ఏర్పాటు | భద్రత కలిగిన, విస్తరివచనగల, తేలికపాటి AI ఏజెంట్ డిప్లాయ్‌మెంట్ |

## నేను నా ప్రస్తుతం ఉన్న Azure ఎకోసిస్టమ్ సాధనాలను నేరుగా సమ్మిళితం చేయగలనా, లేక స్టాండ్అలోన్ పరిష్కారాలు అవసరమా?


సమాధానం అవును, మీరు మీ ప్రస్తుతం ఉన్న Azure ఎకోసిస్టం టూల్స్‌ను Microsoft Foundry Agent Serviceతో నేరుగా సమగ్రపరచుకోవచ్చు, ముఖ్యంగా ఇది ఇతర Azure సర్వీసులతో సజావుగా పనిచేయడానికి నిర్మించబడినది. ఉదాహరణకు మీరు Bing, Azure AI Search, మరియు Azure Functions ను సమగ్రపరచుకోవచ్చు. Microsoft Foundryతో కూడా లోతైన సమగ్రత ఉంది.

Microsoft Agent Framework కూడా `FoundryChatClient` మరియు Azure identity ద్వారా Azure సర్వీసులతో సమగ్రపరచబడుతుంది, ఇది మీ ఏజెంట్ టూల్స్ నుండి నేరుగా Azure సర్వీసులను కాల్ చేయడానికి అనుమతిస్తుంది.

## ఉదాహరణ కోడ్లు

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI ఏజెంట్ ఫ్రేమ్‌వర్క్స్ గురించి మరిన్ని ప్రశ్నలు ఉన్నాయా?

మరింత మంది శిక్షణార్థులతో కలుసుకోవడానికి, ఆఫీస్ అవర్స్‌కు హాజరుకావడానికి మరియు మీ AI ఏజెంట్ల ప్రశ్నలకు సమాధానం పొందడానికి [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) లో చేరండి.

## సూచనలు

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## ముందరి పాఠం

[AI ఏజెంట్లకు పరిచయం మరియు ఏజెంట్ ఉపయోగ కేసులు](../01-intro-to-ai-agents/README.md)

## తరువాతి పాఠం

[Agentic Design Patterns అర్థం చేసుకోవడం](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->