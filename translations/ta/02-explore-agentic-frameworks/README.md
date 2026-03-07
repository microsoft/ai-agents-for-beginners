[![AI ஏஜென்ட் கட்டமைப்புகளை ஆராய்தல்](../../../translated_images/ta/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(மேலே உள்ள படத்தை கிளிக் செய்து இந்த பாடத்தின் வீடியோவை காணவும்)_

# AI எஏஜென்ட் கட்டமைப்புகளை ஆராயுங்கள்

AI ஏஜென்ட் கட்டமைப்புகள் AI ஏஜென்ட்களை உருவாக்குவது, நடைமுறைப்படுத்துவது மற்றும் நிர்வகிப்பதை எளிதாக்க வடிவமைக்கப்பட்ட மென்பொருள் தளங்கள் ஆகும். இந்த கட்டமைப்புகள் உருவாக்குநர்களுக்கு முன்-உருவாக்கப்பட்ட கூறுகள்,抽象化ங்கள் மற்றும் கருவிகள் ஆகியவைகளை வழங்கி, சிக்கலான AI அமைப்புகளை உருவாக்குவதற்கான செயல்முறைகளை சீரமைக்கின்றன.

இந்த கட்டமைப்புகள் AI ஏஜென்ட் வளர்ச்சியில் பொதுவான சவால்களில் நிலையான அணுகுமுறைகளை வழங்குவதன் மூலம் உருவாக்குநர்கள் தங்களின் பயன்பாடுகளின் தனித்துவமான அம்சங்கள் மீது கவனம் செலுத்த உதவுகின்றன. அவை AI அமைப்புகளை கட்டமைப்பதில் அளவீடுபார்வை, அணுகல் மற்றும் செயல்திறனை மேம்படுத்துகின்றன.

## அறிமுகம் 

இந்த பாடத்தில் கையாளப்படுவது:

- AI ஏஜென்ட் கட்டமைப்புகள் என்ன மற்றும் அவை உருவாக்குநர்களுக்கு என்ன சாதிக்க அனுமதிக்கின்றன?
- குழுக்கள் இவற்றை எப்படி விரைவாக சோதனை மாதிரி உருவாக்க, iteration செய்ய மற்றும் அவர்களின் ஏஜென்டின் திறன்களை மேம்படுத்த பயன்படுத்தலாம்?
- Microsoft உருவாக்கிய கட்டமைப்புகள் மற்றும் கருவிகள் ( <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> மற்றும் <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a> )க்கிடையில் என்ன வேறுபாடுகள் உள்ளன?
- என்னுடைய தற்போதைய Azure சூழல் கருவிகளை நேரடியாக ஒருங்கிணைக்கலாமா, அல்லது தனித்தனி தீர்வுகள் தேவையா?
- Azure AI Agents சேவை என்பது என்ன மற்றும் இது எப்படி உதவுகிறது?

## கற்றல் இலக்குகள்

இந்த பாடத்தின் இலக்குகள் உங்களுக்கு உதவுவதற்காக:

- AI வளர்ச்சியில் AI ஏஜென்ட் கட்டமைப்புகளின் பங்கைக் समझ करना.
- புத்திசாலி ஏஜென்ட்களை கட்டமைக்க AI ஏஜென்ட் கட்டமைப்புகளை எவ்வாறு பயன்படுத்துவது நிகழ்த்துவது.
- AI ஏஜென்ட் கட்டமைப்புகள் மூலம் இயல்பான முக்கிய திறன்கள்.
- Microsoft Agent Framework மற்றும் Azure AI Agent Service ஆகியவற்றிற்கிடையிலான வேறுபாடுகள்.

## AI ஏஜென்ட் கட்டமைப்புகள் என்ன மற்றும் அவை உருவாக்குநர்களை என்ன செய்ய அனுமதிக்கின்றன?

பாரம்பரிய AI கட்டமைப்புகள் உங்கள் செயலிகளில் AI ஐ ஒருங்கிணைக்க மற்றும் அவற்றை மேம்படுத்த பின்வரும் முறையில் உதவலாம்:

- **தனிப்பயன்பாடு**: AI பயனர் நடத்தைகள் மற்றும் விருப்பங்களை பகுப்பாய்வு செய்து தனிப்பயனான பரிந்துரைகள், உள்ளடக்கம் மற்றும் அனுபவங்களை வழங்க முடியும்.
Example: Netflix போன்ற ஸ்ட்ரீமிங் சேவைகள் பார்க்கும் முன்னகர்வின் அடிப்படையில் திரைப்படங்கள் மற்றும் நிகழ்ச்சிகளை பரிந்துரைக்கும், இது பயனர் ஈடுபாடு மற்றும் திருப்தியை உயர்த்துகிறது.
- **தானமயமிடல் மற்றும் திறன்**: AI மீளுருமாற்றான பணிகளை தானாகச் செய்ய, வேலைநடவடிக்கைகளை எளிதாக்க மற்றும் செயல்பாட்டு திறனைக் மேம்படுத்த முடியும்.
Example: வாடிக்கையாளர் சேவை செயலிகள் சாதாரண கேள்விகளைக் கையாள AI-சேதிகை அடிப்படையிலான聊天பாட்கள் பயன்படுத்தி பதிலளிக்கும் நேரத்தை குறைத்து, மனித ஏஜென்ட்களைக் கடினமான பிரச்னைகளுக்கு விடுவிக்கின்றன.
- **மேம்பட்ட பயனர் அனுபவம்**: AI குரல் அறிதல், இயற்கை மொழி இயங்கியல், மற்றும் முன்னறிவிப்பு படைப்பழக்கங்கள் போன்ற புத்திசாலி அம்சங்களை வழங்குவதன் மூலம் மொத்த பயனர் அனுபவத்தை மேம்படுத்த முடியும்.
Example: Siri மற்றும் Google Assistant போன்ற மெய்நிகர் உதவியாளர்கள் குரல் கட்டளைகளை புரிந்து பதிலளிக்க AI ஐ பயன்படுத்தி, பயனர்களுக்கு சாதனங்களை எளிதாக பயன்படுத்த உதவுகின்றன.

### இது எல்லாம் நன்றாகத் தெரிகிறது, அப்படியானால் நாம் AI Agent Framework அத்தை ஏன் தேவை?

AI ஏஜென்ட் கட்டமைப்புகள் வெறும் AI கட்டமைப்புகளைவிட வேறுபட்டவை. அவை பயனர்களுடன், மற்ற ஏஜென்ட்களுடன் மற்றும் சுற்றுப்புறத்துடன் தொடர்பு கொண்டு குறிப்பிட்ட நோக்கங்களை அடையக் கூடிய புத்திசாலி ஏஜென்ட்களை உருவாக்க அனுமதிக்க வடிவமைக்கப்பட்டுள்ளன. இந்த ஏஜென்ட்கள் சுயாதீன நடத்தை காட்டு, முடிவெடுக்க மற்றும் மாறும் சூழ்நிலைகளுக்கு தக்கமாறு சம்பந்தப்படக் கூடியவையாக இருக்கலாம். AI ஏஜென்ட் கட்டமைப்புகள் மூலம் கிடைக்கும் சில முக்கிய திறன்களை நோக்கலாம்:

- **ஏஜென்ட் ஒத்துழைப்பு மற்றும் ஒருங்கிணைப்பு**: பல AI ஏஜென்ட்களை உருவாக்கி அவை ஒன்றாகவே பணியாற்றி, தொடர்பு கொண்டு, சிக்கலான பணிகளை தீர்க்க ஒருங்கிணைக்க முடியும்.
- **பணி தானியங்கி மற்றும் நிர்வகிப்பு**: பலபடி வேலைநடவடிக்கைகள் தானியக்கமாக செயல்படுத்துவது, பணிகளை வேகம் பகிர்தல் மற்றும் ஏஜென்ட்களிடையே திடீர் பணியாளர்ப் பிரிவு உள்ளிட்ட機能களை வழங்குகிறது.
- **சூழன சார்ந்த புரிதலும் தமிழீடாமையும்**: ஏஜென்ட்களுக்கு சூழலை புரிந்துகொள்ளும் திறன், மாறும் சூழல்களுக்கு ஏற்ப தகுதிசெய்யும் திறன் மற்றும் நேரடி தகவலின் அடிப்படையில் முடிவெடுத்தல் ஆகியவற்றை வழங்குகிறது.

மொத்தத்தில், ஏஜென்ட்கள் உங்களுக்குக் கிட்டத்தட்டு செயல்களை செய்யக்கூடியவையாக இருக்கும்; தானியக்கத்தை மேலும் உயர்த்த, சுற்றுப்புறத்திலிருந்து கற்பித்துக்கொள்ளக்கூடிய மற்றும் ஏற்பரியமான அமைப்புகளை உருவாக்க முடியும்.

## ஏஜென்டின் திறன்களை விரைவாக prototype செய்ய, iteration செய்ய மற்றும் மேம்படுத்தஎப்படி?

இது விரைவாக மாறும் துறையாக இருந்தாலும், பெரும்பாலான AI ஏஜென்ட் கட்டமைப்புகளில் சில பொதுவான அந்தஸ்துகள் உள்ளன, அவை module கூறுகள், ஒத்துழைப்பு கருவிகள் மற்றும் நேரடி கற்றல் ஆகியவையாகும். இவற்றைப் பற்றி பார்ப்போம்:

- **தொகுதி கூறுகளைப் பயன்படுத்தவும்**: AI SDKகள் முன்னதாக உருவாக்கப்பட்ட கூறுகளை வழங்குகின்றன—உதாரணமாக AI மற்றும் Memory இணைப்பிகள், இயற்கை மொழி அல்லது கோட் பிளக்-இன்களைப் பயன்படுத்தி function calling, prompt templates மற்றும் மேலும் பல.
- **ஒத்துழைப்பு கருவிகளைப் பயன்படுத்தவும்**: குறிப்பிட்ட பங்கு மற்றும் பணிகள் கொண்ட ஏஜென்ட்களை வடிவமைக்க, அவை ஒத்துழைப்பு பணிவழிகாட்டியைக் சோதித்து மேம்படுத்த அனுமதிக்கவும்.
- **நேரத்தில் கற்றுக்கொள்ளவும்**: ஏஜென்ட்கள் இடையிலான தொடர்புகளில் இருந்து கற்று, அவர்களின் நடத்தை தானாகவே சேர்ந்துகொள்ளும் feedback loop-களை செயல்படுத்தவும்.

### தொகுதி கூறுகளைப் பயன்படுத்தவும்

Microsoft Agent Framework போன்ற SDKகள் AI இணைப்பிகள், கருவி வரையறைகள் மற்றும் ஏஜென்ட் நிர்வகிப்பு போன்ற முன்-உருவாக்கப்பட்ட கூறுகளை வழங்குகின்றன.

**குழுக்கள் இதனை எப்படி பயன்படுத்தலாம்**: குழுக்கள் அவை பயன்படுத்தி புதிதாக இருந்து தொடங்காமல் இவ்வாறு கூறுகளை வேகமாக சேர்த்து ஒரு செயல்பாட்டு prototype உருவாக்க முடியும், இது விரைவான பரிசோதனை மற்றும் iteration ஐ அனுமதிக்கிறது.

**பயிற்றில் இது எப்படி வேலை செய்கிறது**: பயனர் உள்ளீட்டிலிருந்து தகவலை எடுக்க ஒரு முன்-உருவாக்கப்பட்ட parser, தரவை சேமித்து மீட்டெடுக்கும் memory module, மற்றும் பயனர்களுடன் தொடர்பு கொள்ள prompt generator போன்றவற்றைப் பயன்படுத்தலாம், இவை அனைத்தும் ஆரம்பத்திலிருந்து உருவாக்க வேண்டிய அவசியம் இல்லாமல்.

**உதாரண குறியீடு**. Microsoft Agent Framework ஐ `AzureAIProjectAgentProvider` உடன் பயன்படுத்தி மாடல் பயனர் உள்ளீட்டுக்கு tool calling மூலம் பதிலளிக்க எவ்வாறு செய்யலாம் என்பதைப் பார்க்கலாம்:

``` python
# Microsoft முகவர் கட்டமைப்பு பைதான் எடுத்துக்காட்டு

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# பயணத்தை முன்பதிவு செய்ய மாதிரி கருவி செயல்பாட்டை வரையறு
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
    # எடுத்துக்காட்டு வெளியீடு: உங்கள் 2025 ஜனவரி 1-ந் தேதி நியூயார்க்கிற்கு விமானம் வெற்றிகரமாக முன்பதிவு செய்யப்பட்டுள்ளது. பாதுகாப்பான பயணம்! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

இந்த உதாரணத்திலிருந்து நீங்கள் பார்க்கக்கூடியது, பயனர் உள்ளீட்டிலிருந்து முக்கிய தகவல்களை எடுக்க முன்-உருவாக்கப்பட்ட parser ஐ எப்படி பயன்படுத்தலாம் என்பதுதான் — உதாரணமாக ஒரு விமானம் முன்பதிவு கோரிக்கையின் ஆரம்பப்புள்ளி, ஏற்கும் இடம் மற்றும் திகதி போன்றவை. இந்த தொகுதி அணுகுமுறை உங்களுக்கு உயர் நிலை லாஜிக்கில் கவனம் செலுத்த அனுமதிக்கிறது.

### ஒத்துழைப்பு கருவிகளைப் பயன்படுத்தவும்

Microsoft Agent Framework போன்ற கட்டமைப்புகள் ஒன்றாக செயல்படக்கூடிய பல ஏஜென்ட்களை உருவாக்க உதவுகின்றன.

**குழுக்கள் இதனை எப்படி பயன்படுத்தலாம்**: குழுக்கள் குறிப்பிட்ட பணி மற்றும் வேறுபடுத்தப்பட்ட பங்களிப்பு கொண்ட ஏஜென்ட்களை வடிவமைக்கலாம், இது ஒத்துழைப்பு பணிவழிகளை சோதித்து செதுக்குவதற்கு மற்றும் மொத்த அமைப்பின் செயல்திறனை மேம்படுத்த உதவும்.

**பயிற்றில் இது எப்படி வேலை செய்கிறது**: தரவு மீட்டெடுப்பு, பகுப்பாய்வு அல்லது முடிவெடுத்தல் போன்ற குறிப்பிட்ட செயல்பாடுகளைச் செய்வதில் ஒவ்வொரு ஏஜென்டுக்கும் சிறப்பு பொறுப்பு அமைக்க—a team of agents உருவாக்கலாம். இவை தகவலைப் பகிர்ந்து மற்றும் தொடர்பு கொண்டு ஒரு பொதிக் குறிக்கோளை எட்டலாம், உதாரணமாக பயனர் கேள்விக்கிக்குப் பதிலளித்தல் அல்லது ஒரு பணியை முடிக்குதல்.

**உதாரணக் குறியீடு (Microsoft Agent Framework)**:

```python
# மைக்ரோசாஃப்ட் ஏஜென்ட் கட்டமைப்பைப் பயன்படுத்தி ஒரே நேரத்தில் ஒன்றுசேர்ந்து செயல்படும் பல ஏஜெண்ட்களை உருவாக்குதல்

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# தரவு மீட்டெடுக்கும் ஏஜெண்ட்
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# தரவு பகுப்பாய்வு ஏஜெண்ட்
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ஒரு பணியில் பின்பற்றிச் செயல்படுத்தப்படும் ஏஜெண்ட்கள்
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

முந்தைய குறியீட்டில் நீங்கள் பார்க்கும் 것은 பல ஏஜென்ட்கள் ஒன்றாக இணைந்து தரவை பகுப்பாய்வு செய்யும் பணியை எவ்வாறு உருவாக்குவது என்பது. ஒவ்வொரு ஏஜென்டும் ஒரு குறிப்பிட்ட செயல்பாடு செய்யும், மற்றும் அனுகூலமான முடிவை அடைய ஏஜென்ட்களை ஒருங்கிணைத்து அந்தப் பணி செயல்படுத்தப்படுகிறது. சிறப்பு பங்கு கொண்ட கொடுப்பனவுக்கான ஏஜென்ட்களை உருவாக்குவதன் மூலம் பணித்திறன் மற்றும் செயல்திறன் உயர்க்கும்.

### நேரத்தில் கற்றுக்கொள்ளுதல்

மேம்பட்ட கட்டமைப்புகள் நேரடி சூழல் புரிதலும் அதற்கேற்ற தகுதிசெய்தல்களையும் வழங்குவதற்கான திறன்களை வழங்குகின்றன.

**குழுக்கள் இதனை எப்படி பயன்படுத்தலாம்**: குழுக்கள் өмнைய பேச்சுவார்த்தையிலிருந்து பயிற்சி பெறுவதற்கும், பிறருடனான தொடர்புகளில் இருந்து திருத்தி நடத்தை மாற்றுவதற்கும் feedback loop-களை செயல்படுத்தலாம், இதனால் திறன்கள் தொடர்ந்து மேம்பட்டு செழித்தடையும்.

**பயிற்றில் இது எப்படி வேலை செய்கிறது**: ஏஜென்ட்கள் பயனர் பின்னூட்டம், சுற்றுப்புற தரவு மற்றும் பணியின் முடிவுகளை பகுப்பாய்வு செய்து தங்களின் அறிவுத்தொகுப்பை புதுப்பித்து, முடிவெடுத்தல் ஆல்கொரிதங்களைக் সংশுத்தி காலதாமதத்தில்மேலும் செயல்திறனை மேம்படுத்த முடியும். இந்த நிகழ்ச்சி கற்றல் செயல்முறை ஏஜென்ட்களை மாறும் நிலைகளுக்கு மற்றும் பயனர் விருப்பங்களுக்கு ஏற்ப ஒழுங்குபடுத்துவதால் மொத்த அமைப்பின் பயன்திறனை உயர்த்தும்.

## Microsoft Agent Framework மற்றும் Azure AI Agent Service ஆகியவற்றிற்கிடையிலான வேறுபாடுகள் என்ன?

இந்த அணுகுமுறைகளை ஒப்பீடு செய்ய பல வழிகள் உள்ளன, ஆனால் அவற்றின் வடிவமைப்பு, திறன்கள் மற்றும் குறிக்கப்பட்ட பயன்பாட்டு வழக்குகள் என சில முக்கிய வேறுபாடுகளைப் பார்ப்போம்:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `AzureAIProjectAgentProvider` என்பதைப் பயன்படுத்தி AI ஏஜென்ட்களை உருவாக்குவதற்கான ஒரு சீரமைக்கப்பட்ட SDK ஐ வழங்குகிறது. இது உருவாக்குநர்களுக்கு Azure OpenAI மாடல்களை கொண்டு கருவி அழைப்பு, உரையாடல் நிர்வாகம் மற்றும் Azure identity மூலம் நிறுவனத் தரத்தின் பாதுகாப்பு ஆகியவற்றை பயன்படுத்துகின்ற ஏஜென்ட்களை உருவாக்க அனுமதிக்கிறது.

**பயன்பாட்டு வழக்குகள்**: கருவி பயன்பாடு, பல்அடுக்கு பணிநடவடிக்கைகள் மற்றும் நிறுவன ஒருங்கிணைப்பு السينாரியோக்களுக்கு தயாரான உற்பத்தி-நிலையை உருவாக்குதல்.

Microsoft Agent Framework இன் சில முக்கிய மூலக் கருத்துகள் இவை:

- **Agents**. ஒரு ஏஜென்ட் `AzureAIProjectAgentProvider` மூலம் உருவாக்கப்பட்டு பெயர், அறிவுறுத்தல்கள் மற்றும் கருவிகள் கொண்டு கட்டமைக்கப்படுகிறது. அவை:
  - **பயனர் செய்திகளைக் கடைசியாக செயலாக்கி** Azure OpenAI மாடல்களை பயன்படுத்தி பதில்கள் உருவாக்க முடியும்.
  - **கருவிகளை அழைக்க** உரையாடல் சூழலின் அடிப்படையில் தானாகவே செயல்படலாம்.
  - **பல இடையிலான தொடர்புகளில் உரையாடல் நிலையை பராமரிக்க** முடியும்.

  ஏஜென்ட் உருவாக்க எவ்வாறு ஒரு குறியீட்டு துண்டு காண்பிக்கப்படுகிறது:

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

- **Tools**. கட்டமைப்பு ஏஜென்டு தானாக கூலக்கூடிய Python functions ஆக கருவிகளை வரையறுக்க ஆதரவு வழங்குகிறது. ஏஜென்டு உருவாக்கும்போது கருவிகள் பதிவு செய்யப்படுகின்றன:

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

- **பல-ஏஜென்ட் ஒருங்கிணைப்பு**. வெவ்வேறு சிறப்பிற்குரிய பணிகளைக் கொண்ட பல ஏஜென்ட்களை உருவாக்கி அவற்றின் பணிகளை ஒருங்கிணைக்க முடியும்:

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

- **Azure Identity ஒருங்கிணைப்பு**. இந்த கட்டமைப்பு பாதுகாப்பான, API சாவிகளைக் கையாள தேவையில்லாமல் `AzureCliCredential` (அல்லது `DefaultAzureCredential`) பயன்படுத்தி keyless அங்கீகாரம் வழங்குகிறது.

## Azure AI Agent Service

Azure AI Agent Service என்பது Microsoft Ignite 2024 இல் அறிமுகப்படுத்தப்பட்ட சமீபத்திய சேவையாகும். இது Llama 3, Mistral, Cohere போன்ற திறந்த மூல LLMகளை நேரடியாக அழைக்கிக்கொள்வதுபோல திறமையான மாடல்களை வழங்கி, உள்ளமைக்கலான மற்றும் விரிவான ஏஜென்ட்களை உருவாக்கவும் நடைமுறைப்படுத்தவும் இடைமுகம் தருகிறது.

Azure AI Agent Service நிறுவனத் தர பாதுகாப்பு முறைகள் மற்றும் தரவுத் 저장ுக்களை வலுப்படுத்துகிறது, அதனால் இது நிறுவன பயன்பாடுகளுக்கு உடன்படக்கூடியதாக இருக்கும்.

இது Microsoft Agent Framework உடன் சிறப்பாக இணைந்து ஏஜென்ட்களை கட்டமைக்கவும் வெளியிடவும் உதவுகிறது.

இந்த சேவை தற்போது பப்ளிக் முன்னோக்கு நிலை (Public Preview) இல் உள்ளது மற்றும் ஏஜென்ட்களை உருவாக்க Python மற்றும் C# ஐ ஆதரிக்கிறது.

Azure AI Agent Service Python SDK ஐப் பயன்படுத்தி, பயனர்-வரையறுக்கப்பட்ட கருவியுடன் ஒரு ஏஜென்டை நாம் உருவாக்க முடியும்:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# கருவி செயல்பாடுகளை வரையறு
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

### முக்கியக் கருத்துக்கள்

Azure AI Agent Service இன் கீழ்க்காணும் முக்கியக் கருத்துக்களைக் கொண்டுள்ளது:

- **Agent**. Azure AI Agent Service Microsoft Foundry உடன் இணைகிறது. AI Foundry இல், ஒரு AI ஏஜென்ட் "அறிவெழுச்சி"முள்ள மைக்ரோசேவையாக செயல்பட்டு கேள்விகளுக்கு பதிலளிக்க (RAG), செயல்களை நடாத்த அல்லது முழுமையாக வேலைநடவடிக்கைகளை தானாகச் செய்வதற்கும் பயன்படுகிறது. இது உருவாக்குபவர்களுக்கு ஜெனரேட்டிவு AI மாடல்களின் சக்தியையும், உண்மையான தரவுத் தொழில்நுட்பத்துடன் இணைந்து அணுக மற்றும் தொடர்பு கொள்ளும் கருவிகளையும் ஒன்றிணைப்பதன் மூலம் சாதிக்கப்படுகிறது. உதாரணமாக ஒரு ஏஜென்ட்:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    இந்த உதாரணத்தில், `gpt-4o-mini` மாடலைப் பயன்படுத்தி `my-agent` என்ற பெயரில் மற்றும் `You are helpful agent` என்ற அறிவுறுத்தலுடன் ஒரு ஏஜென்ட் உருவாக்கப்படுகின்றது. அந்த ஏஜென்ட் குறியீட்டு விளக்கம் பணிகளை செயற்படுத்த தேவையான கருவிகள் மற்றும் வளங்களுடன் உபகரணப்படுத்தப்படுகிறது.

- **Thread and messages**. thread என்பது ஒரு முக்கியக் கருத்து. அது ஒரு ஏஜென்ட் மற்றும் பயனரின் இடையேயான உரையாடல் அல்லது தொடர்பை பிரதிபலிக்கிறது. Threads உரையாடலின் முன்னேற்றத்தை பின்தொடர, சூழல் தகவல்களை சேமிக்க, மற்றும் தொடர்பின் நிலையை நிர்வகிக்க பயன்படுத்தப்படலாம். thread இன் உதாரணம்:

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

    முந்தைய குறியீட்டில், ஒரு thread உருவாக்கப்படுகிறது. அதன் பிறகு, threadக்கு ஒரு செய்தி அனுப்பப்படுகிறது. `create_and_process_run` ஐ அழிப்பதன் மூலம், thread இல் ஏஜென்டிடம் பணியைச் செய்ய கேட்கப்படுகிறது. இறுதியில், messages அறியப்படுகின்றன மற்றும் ஏஜென்டின் பதிலைப் பார்க்க பதிவு செய்யப்படுகின்றன. messages அவை உரையின் வகையில், படம் அல்லது கோப்பு போன்ற வெவ்வேறு வகைகளில் இருக்கக்கூடியவை என்பது முக்கியம் — உதாரணமாக ஏஜென்ட் ஒரு படத்தை அல்லது உரையை வெளியிட்டிருக்கலாம். ஒரு உருவாக்குநராக, நீங்கள் இதன் மூலம் கிடைக்கும் தகவல்களை மேலும் செயலாக்க அல்லது பயனருக்கு வழங்க முடியும்.

- **Microsoft Agent Framework உடன் ஒருங்கிணைப்பு**. Azure AI Agent Service Microsoft Agent Framework உடன் வெற்றிகரமாக இணைகிறது, அதாவது `AzureAIProjectAgentProvider` பயன்படுத்தி ஏஜென்ட்களை கட்டமைத்து அவற்றை Agent Service மூலம் உற்பத்தி சூழலுக்குத் தரவிறக்க முடியும்.

**பயன்பாட்டு வழக்குகள்**: பாதுகாப்பான, அளவளாவிய மற்றும் நெகிழ்வான AI ஏஜென்ட் வெளியீடுகளை தேவைப்படும் நிறுவன பயன்பாடுகளுக்காக Azure AI Agent Service வடிவமைக்கப்பட்டுள்ளது.

## இந்த அணுகுமுறைகளுக்கிடையிலான வேறுபாடு என்ன?
 
ஒத்திசையும் பகுதிகளும் இருப்பது போலத் தெரியலாம், ஆனால் அவற்றின் வடிவமைப்பு, திறன்கள் மற்றும் குறிக்கப்பட்ட பயன்பாட்டு வழக்குகளின்படி சில முக்கிய வேறுபாடுகள் உள்ளன:
 
- **Microsoft Agent Framework (MAF)**: கருவி அழைப்பு கொண்ட ஏஜென்டுகளை உருவாக்க ஒரு தயாரான SDK. இது ஏஜென்ட்களை உருவாக்குவதற்கான சீரமைக்கப்பட்ட APIஐ வழங்குகிறது, உரையாடல் நிர்வாகம் மற்றும் Azure identity ஒருங்கிணைப்பையும் கொண்டுள்ளது.
- **Azure AI Agent Service**: Agents-காக Azure Foundry இல் ஒரு தளம் மற்றும் வெளியீட்டு சேவை. இது Azure OpenAI, Azure AI Search, Bing Search மற்றும் கோட் செயலாக்கம் போன்ற சேவைகளுடன் உள்ளமைக்கப்பட்ட இணைப்பு வசதிகளை வழங்குகிறது.
 
Still not sure which one to choose?

### Use Cases
 
சில பொதுவான பயன்பாட்டு வழக்குகளைப் பார்த்து உங்களுக்கு உதவுகிறோமா என்று பார்ப்போம்:
 
> Q: I'm building production AI agent applications and want to get started quickly
>

> A: The Microsoft Agent Framework is a great choice. It provides a simple, Pythonic API via `AzureAIProjectAgentProvider` that lets you define agents with tools and instructions in just a few lines of code.

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

## Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?
The answer is yes, you can integrate your existing Azure ecosystem tools directly with Azure AI Agent Service especially, as it has been built to work seamlessly with other Azure services. You could for example integrate Bing, Azure AI Search, and Azure Functions. There's also deep integration with Microsoft Foundry.

The Microsoft Agent Framework also integrates with Azure services through `AzureAIProjectAgentProvider` and Azure identity, letting you call Azure services directly from your agent tools.

## மாதிரி குறியீடுகள்

- Python: [ஏஜெண்ட் ஃப்ரேம்வொர்க்](./code_samples/02-python-agent-framework.ipynb)
- .NET: [ஏஜெண்ட் ஃப்ரேம்வொர்க்](./code_samples/02-dotnet-agent-framework.md)

## AI ஏஜென்ட் ஃப்ரேம்வொர்க்கள் பற்றிப் பற்றி இன்னும் கேள்விகள் உள்ளதா?

மற்ற பயில்பவர்களுடன் சந்திய, அலுவலக நேரங்களில் கலந்துகொண்டு உங்கள் AI ஏஜெண்ட் கேள்விகளுக்கு பதில்கள் பெற [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) இல் சேருங்கள்.

## ஆதாரங்கள்

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure ஏஜென்ட் சேவை</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI பதில்கள்</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI ஏஜென்ட் சேவை</a>

## முந்தைய பாடம்

[AI ஏஜென்ட்கள் மற்றும் ஏஜெண்ட் பயன்பாட்டு வழக்குகளுக்கான அறிமுகம்](../01-intro-to-ai-agents/README.md)

## அடுத்த பாடம்

[ஏஜென்டிக் வடிவமைப்பு மாதிரிகளைப் புரிந்துகொள்ளுதல்](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
மறுப்பு:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவையாகிய [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சித்தாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனிக்கவும். மூல ஆவணம் அதன் சொந்த மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதனால் ஏற்படும் எந்தவொரு தவறான புரிதலுக்கும் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பேற்கமாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->