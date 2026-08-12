[![AI ஏஜண்ட் கட்டமைப்புகளை ஆய்வு செய்தல்](../../../translated_images/ta/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(இந்த பாடத்தின் காணொளியை பார்க்க மேலே உள்ள படம் கிளிக் செய்யவும்)_

# AI ஏஜண்ட் கட்டமைப்புகளை ஆய்வு செய்க

AI ஏஜண்ட் கட்டமைப்புகள் AI ஏஜண்ட்களை உருவாக்குதல், நடைமுறைப்படுத்துதல் மற்றும் நிர்வகிப்பதனை எளிமையாக்கும் மென்பொருள் மேடைகள் ஆகும். இக்கட்டமைப்புகள் டெவலப்பர்களுக்கு முன்கூட்டியே தயாரிக்கப்பட்ட கூறுகள்,抽象化கள் மற்றும் கருவிகள் வழங்கி, சிக்கலான AI முறைமை உருவாக்கத்தை எளிதாக்குகின்றன.

இக்கட்டமைப்புகள் டெவலப்பர்களை அவர்களின் பயன்பாடுகளின் தனித்துவ அம்சங்களில் கவனம் செலுத்த உதவுகின்றன, AI ஏஜண்ட் மேம்பாட்டில் பொதுவாக உள்ள சவால்களுக்கு நிலைத்த முறைகளை வழங்கி. இவை AI முறைமைகளை கட்டுவதில் அளவுகோல், அணுகல் மற்றும் செயல்திறனை மேம்படுத்துகின்றன.

## அறிமுகம் 

இந்த பாடத்தில் நாம் பார்க்கவிருக்கும் விஷயங்கள்:

- AI ஏஜண்ட் கட்டமைப்புகள் என்ன மற்றும் டெவலப்பர்கள் எதை பெற முடியும்?
- குழுக்கள் எப்படி விரைவில் முன்னோடிப்படுத்த, மீளிசைத்தல் மற்றும் அவர்களின் ஏஜண்ட் திறன்களை மேம்படுத்தலாம்?
- Microsoft உருவாக்கிய கட்டமைப்புகள் மற்றும் கருவிகள் ( <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> மற்றும் <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) இடையேயுள்ள வேறுபாடுகள் என்ன?
- நான் ஏற்கனவே வைத்துள்ள Azure சூழல் கருவிகளை நேரடியாக இணைக்கலாமா, அல்லது தனித்துவமான தீர்வுகள் தேவைபடுமா?
- Microsoft Foundry Agent Service என்னும் சேவை என்ன மற்றும் இது என்னவாறு எனக்கு உதவுகிறது?

## கற்றல் இலக்குகள்

இந்த பாடத்தின் இலக்குகள்:

- AI உருவாக்கத்தில் AI ஏஜண்ட் கட்டமைப்புகளின் பங்கு.
- அறிவுணர்வு ஏஜண்ட்களை கட்ட AI ஏஜண்ட் கட்டமைப்புகளை எப்படி பயன்படுத்துவது.
- AI ஏஜண்ட் கட்டமைப்புகள் இயக்க அதிகாரப்படுத்தும் முக்கிய திறன்கள்.
- Microsoft Agent Framework மற்றும் Microsoft Foundry Agent Service இடையேயான வேறுபாடுகள்.

## AI ஏஜண்ட் கட்டமைப்புகள் என்ன மற்றும் டெவலப்பர்களுக்கு என்ன செய்ய உதவுகின்றன?

பாரம்பரிய AI கட்டமைப்புகள் உங்கள் செயலிகளில் AIயை ஒருங்கிணைக்க உதவி புரிந்து, இவற்றை கீழ்க்கண்டவாறு சிறப்பாக்க முடியும்:

- **தனிப்பயனாக்கல்**: AI பயன்பாட்டாளரின் பழக்கம் மற்றும் விருப்பங்களைப் பகுப்பாய்வு செய்து, தனிப்பட்ட பரிந்துரைகள், உள்ளடக்கம் மற்றும் அனுபவங்களை வழங்குகிறது.
உதாரணம்: Netflix போன்ற ஸ்ட்ரீமிங் சேவைகள் பார்க்கும் வரலாறின் அடிப்படையில் படங்கள் மற்றும் நிகழ்ச்சிகளை பரிந்துரைக்க AIயைப் பயன்படுத்தி, பயனர் ஈடுபாடு மற்றும் திருப்தியை மேம்படுத்துகின்றன.
- **தானியக்க மற்றும் செயல்திறன்**: AI மீளும் பணிகளை தானாகச் செய்ய, பணிப் பாய்ச்சல் முறைகளை சீரமைக்க மற்றும் செயல்முறை திறன்திறம்படுவதை மேம்படுத்த உதவுகிறது.
உதாரணம்: வாடிக்கையாளர் சேவை செயலிகள் AI-இல் இயங்கும் சாட்பாட்களைப் பயன்படுத்தி சாதாரண விசாரணைகளை கையாளுகின்றன, பதில் நேரத்தை குறைத்து, மனித ஏஜண்ட்களை கடினமான பிரச்சினைகளுக்கு விடுவிக்கின்றன.
- **விருத்தி பெற்ற பயனர் அனுபவம்**: AI குரல் அடையாளம், இயற்கை மொழி செயலாக்கம் மற்றும் முன்னறிவிப்பு உரை போன்ற அறிவுமிக்க அம்சங்களை வழங்கி மொத்த பயனர் அனுபவத்தை மேம்படுத்துகிறது.
உதாரணம்: Siri மற்றும் Google Assistant போன்ற மெய்நிகர் உதவியாளர்கள் AIயை பயன்படுத்தி குரல் கட்டளைகளை புரிந்துகொண்டு பதிலளிக்கின்றன, பயனர்களின் சாதனத்துடன் உரையாடலை எளிதாக்குகின்றன.

### இத்தனை நல்லது தான், அப்படியே AI ஏஜண்ட் கட்டமைப்புகள் எதற்கென நாம் தேவையுள்ளது?

AI ஏஜண்ட் கட்டமைப்புகள் வெறும் AI கட்டமைப்புகளுக்கு மறு படியாக இருக்கின்றன. இவை பயனர், மற்ற ஏஜண்ட்கள் மற்றும் சூழலுடன் தொடர்பு கொண்டு குறிப்பிட்ட இலக்குகளை அடைய அறிவுமிக்க ஏஜண்ட்களை உருவாக்க உதவுகின்றன. இத்தகைய ஏஜண்ட்கள் சுயாதீன நடத்தை வெளிப்படுத்த, முடிவெடுக்க மற்றும் மாற்றமுள்ள சூழலுக்கேற்ற தகுதிகளை மாற்றிக்கொள்ள முடியும். AI ஏஜண்ட் கட்டமைப்புகள் இயக்கும் முக்கிய திறன்கள் சில:

- **ஏஜண்ட் ஒத்துழைப்பு மற்றும் ஒருங்கிணைப்பு**: பல AI ஏஜண்ட்கள் ஒன்றாக வேலை செய்ய, உரையாட மற்றும் ஒருங்கிணைக்க உதவுகிறது.
- **பணி தானியக்க மற்றும் நிர்வாகம்**: பல படிகள் கொண்ட பணிப்பாய்ச்சலை தானியங்கி செய்ய, பணிகளை பகிர்ந்து நிர்வகிக்க வசதிகள்.
- **சூழல் புரிதலும் இயற்றும் திறனும்**: ஏஜண்ட்களுக்கு சூழலை புரிந்து கொண்டே மாற்றமுள்ள சூழலுக்கு ஏற்ப முடிவெடுக்க இயலும் திறனை வழங்குகிறது.

சுருக்கமாகச் சொன்னால், ஏஜண்ட்கள் உங்களுக்கு மேலும் பல காரியங்களை செய்ய, தானியக்கத்தை அடுத்த நிலைக்கு எடுத்துச் சென்று, அடை துடிப்பான, சூழலிலிருந்து கற்றுக்கொள்ளக்கூடிய அறிவுமிக்க முறைமைகளை உருவாக்க உதவுகின்றன.

## ஏஜண்ட் திறன்களை விரைவில் முன்னோடிப்படுத்த, மீளிசைத்து, மேம்படுத்த எப்படி?

இது வேகமாக மாறும் துறையாகும், ஆனால் AI ஏஜண்ட் கட்டமைப்புகளில் பொதுவாக காணப்படும் சில அம்சங்கள் உங்களுக்கு விரைவில் முன்னோடிப்படுத்த மற்றும் மீளிசைக்க உதவுகின்றன, முக்கியமாக கூறுக்கூறுகள், ஒத்துழைப்பு கருவிகள் மற்றும் நேரடி கற்றல். இவை பற்றி பார்ப்போம்:

- **கூறு கூறுகளைக் பயன்படுத்துங்கள்**: AI SDKகள் முன்கூட்டியே AI மற்றும் நினைவகம் இணைப்புகள், இயற்கை மொழி அல்லது குறியீடு பிளகின்கள் மூலம் செயல்பாட்டு அழைப்பு, வடிவமைக்கப்பட்ட கட்டளைகள் போன்றன தருகின்றன.
- **ஒத்துழைப்பு கருவிகளை பயன்படுத்துங்கள்**: குறிப்பிட்ட பங்கு மற்றும் பணிகள் கொண்ட ஏஜண்ட்களை வடிவமைத்து, ஒத்துழைப்பு பணிப்பாய்ச்சல்களை சோதித்து மேம்படுத்துங்கள்.
- **நேரடி கற்றல்**: ஏஜண்ட்கள் எவ்வாறு தொடர்புகொள்கின்றன என்பதை இலகுவாக கற்றுக் கொண்டு தமக்கு தேவையான முறையில் தானாக மாற்றங்களைச் செய்யும் பின்னூட்ட வடிவங்களை செயல்படுத்துங்கள்.

### கூறு கூறுக்களை பயன்படுத்துதல்

Microsoft Agent Framework போன்ற SDKகள் முன்கூட்டியே AI இணைப்புகள், கருவி வரையறைகள் மற்றும் ஏஜண்ட் நிர்வாக கூறுகளை வழங்குகின்றன.

**குழுக்கள் இவற்றை எப்படி பயன்படுத்தலாம்**: குழுக்கள் இக்கூறுகளை விரைவில் சேர்த்து செயல்படும் முன்னோடிப்படுத்தல் செய்யலாம், ஆரம்பமாக மாற்றம் செய்யாமல் விரைவான பரிசோதனை மற்றும் மீளிசைதல் செய்ய உதவும்.

**வெய்தல் எப்படி செயல்படுகிறது**: பயனர் உள்ளீட்டிலிருந்து தகவலை எடுத்துக்கொள்ள முன்கூட்டியே உருவாக்கப்பட்ட பார்சர், தரவை சேமித்து மீட்டெடுக்கும் நினைவகம் மற்றும் பயனர்களுடன் தொடர்பு கொள்ள கட்டளை உற்பத்தி கருவி போன்றவை பயன்படுத்தலாம், இவை அனைத்தும் உங்கள் படைப்பில் நகர்ந்து கொண்டு இருக்கிறன.

**குறியீடு உதாரணம்**. Microsoft Agent Framework பயன்படுத்தி `FoundryChatClient` மூலம் மாற்றியமைப்பு அழைப்புடன் பயனர் உள்ளீட்டுக்கு பதிலளிப்பது எப்படி என்று காண்போம்:

``` python
# மைக்ரோசாப்ட் ஏஜென்ட் கட்டமைப்பு பைத்தான் உதாரணம்

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# பயணத்தை முன்பதிவு செய்ய ஒரு எடுத்துக்காட்டு கருவி செயல்பாட்டை வரையறுக்கவும்
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
    # உதாரண வெளியீடு: உங்கள் 2025 ஜனவரி 1-ஆம் தேதி நியூயார்க் செல்லும் விமானம் வெற்றிகரமாக முன்பதிவு செய்யப்பட்டுள்ளது. பாதுகாப்பாக பயணம் செய்யுங்கள்! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

இந்த உதாரணத்தில் பார்சர் பயன்படுத்தி பயனர் உள்ளீட்டிலிருந்து முக்கிய தகவல்கள் (பிடிபிடிப்பு நடைமுறை, இடம் மற்றும் தேதி போன்றவை) எடுக்கப்படுவது பார்க்கலாம். இது கூறு அடிப்படையிலான அணுகுமுறை உங்களுக்கு உயர்நிலை தலையங்கச் செயல்பாட்டில் கவனம் செலுத்த அனுமதிக்கும்.

### ஒத்துழைப்பு கருவிகளை பயன்படுத்துதல்

Microsoft Agent Framework போன்ற கட்டமைப்புகள் பல ஏஜண்ட்கள் ஒன்றாக வேலை செய்ய உதவுகின்றன.

**குழுக்கள் இவற்றை எப்படி பயன்படுத்தலாம்**: குழுக்கள் குறிப்பிட்ட பங்கு மற்றும் பணிகளுடன் ஏஜண்ட்களை வடிவமைத்து ஒத்துழைப்பு பணிப்பாய்ச்சல்களை சோதித்து முழுக்க அமைப்பை மேம்படுத்தலாம்.

**வெய்தல் எப்படி செயல்படுகிறது**: தரவு மீட்டெடுக்கும், பகுப்பாய்வு செய்யும், முடிவெடுக்கும் போன்ற ஒரு கடமையை வழங்கும் பல ஏஜண்ட்களுடன் குழுவை உருவாக்குங்கள். அவர்கள் செய்திகளை பகிர்ந்து, பயனர் கேள்விக்கு பதில் கூறுவதோ அல்லது பணியை முடிப்பதோ போன்ற ஒரு பொதுவான இலக்கை அடைய சேர்ந்து செயல்படலாம்.

**குறியீடு உதாரணம் (Microsoft Agent Framework)**:

```python
# மைக்ரோசாஃப்ட் ஏஜென்ட் கட்டமைப்பைப் பயன்படுத்தி ஒன்றாக வேலை செய்யும் பல ஏஜென்ட்களை உருவாக்குதல்

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# தரவு பெறும் ஏஜென்ட்
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# தரவு பகுப்பு ஏஜென்ட்
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ஒரு வேலை மீது ஏஜென்ட்களை தொடர் முறையில் இயக்குதல்
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

முன் குறியீட்டில் பல ஏஜண்ட்கள் தரவை பகுப்பாய்வு செய்ய ஒருங்கிணைந்து பணிபுரியும் அமைப்பை உருவாக்குவது பார்க்கலாம். ஒவ்வொரு ஏஜண்டும் தனித்த பணி செய்கிறது, மேலும் ஒத்துழைத்து பணியை செயலான முறையில் நிறைவேற்றுகின்றனர். சிறப்பு பங்குகள் கொண்ட ஏஜண்ட்களை உருவாக்குவதன் மூலம் பணி செயல்திறனும் திறமையும் மேம்படும்.

### நேரடி கற்றல்

மேம்பட்ட கட்டமைப்புகள் நேரடி சூழல் புரிதல் மற்றும் ஏற்பு திறன்களை வழங்குகின்றன.

**குழுக்கள் இவற்றை எப்படி பயன்படுத்தலாம்**: குழுக்கள் கருத்துக் கவர் முறைகளை அமைத்து, தொடர்புகளிலிருந்து ஏஜண்ட்கள் கற்றுக்கொண்டு தங்கள் செயல்பாட்டை தானாக மாற்றி வளர்ச்சி மற்றும் திறன் மேம்படுத்த முடியும்.

**வெய்தல் எப்படி செயல்படுகிறது**: பயனர் பின்னூட்டத்தை, சூழல் தரவை மற்றும் பணியுடை முடிவுகளை பகுப்பாய்வு செய்து ஏஜண்ட்கள் தங்கள் அறிவுக்கணக்கை புதுப்பித்து முடிவு செய்யும் அலகுகளை சரிசெய்து காலப்போக்கில் சிறப்பாக செயல்படுகின்றன. இந்த மீளிசையான கற்றல் மாற்றத்துக்கு ஏற்படும் சூழல் மற்றும் பயனர் விருப்பங்களுக்கு ஏஜண்ட்கள் வேலை செய்ய உதவும், மொத்த முறைமையின் செயல்திறனை உயர்த்தும்.

## Microsoft Agent Framework மற்றும் Microsoft Foundry Agent Service இடையேயான வேறுபாடுகள் என்ன?

இவை ஒப்பிட பல வழிகள் உள்ளன, ஆனால் அவர்களது வடிவமைப்பு, திறன்கள் மற்றும் இலக்கு பயன்பாடுகள் தொடர்பாக சில முக்கிய வேறுபாடுகளை பார்ப்போம்:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `FoundryChatClient` பயன்படுத்தி AI ஏஜண்ட்களை கட்டுவதற்கான வரையறுக்கப்பட்ட SDK வழங்கும். இது Azure OpenAI மாதிரிகளை பயன்படுத்தி ஏஜண்ட்களை உருவாக்க, கருவி அழைப்புகள், உரையாடல் மேலாண்மை மற்றும் Azure அடையாளத்துடன் நிறுவன தர காத்திருப்பு வழங்குகிறது.

**பயன்பாட்டு வழக்குகள்**: கருவி பயன்பாடு, பல படிகள் கொண்ட பணியமைப்புகள் மற்றும் நிறுவன ஒருங்கிணைப்பு சூழல்களில் தயாரிப்புக்கான AI ஏஜண்ட்கள் கட்டல்.

Microsoft Agent Framework-க்கு சில முக்கிய கருத்துச்சொற்கள்:

- **ஏஜண்ட்கள்**. ஒரு ஏஜண்ட் `FoundryChatClient` மூலம் உருவாக்கப்பட்டு பெயர், அறிவுரைகள் மற்றும் கருவிகளுடன் உருவாக்கப்படுகிறது. அந்த ஏஜண்ட்:
  - **பயனர் செய்திகளை நுறைಸಿ** Azure OpenAI மாதிரிகளை பயன்படுத்தி பதில்களை உருவாக்கும்.
  - உரையாடல் சூழலின் அடிப்படையில் **கருவிகளை தானாக அழைக்கும்**.
  - பல தொடர்புகளுக்கிடையில் **உரையாடல் நிலையை பராமரிக்கும்**.

  இதோ அதைப் பயன்படுத்தி ஏஜண்ட் உருவாக்கும் குறியீடு:

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

- **கருவிகள்**. கட்டமைப்பு பைதான் செயல்பாடுகளாக கருவிகளை வரையறுக்க ஆதரவளிக்கிறது, ஏஜண்ட் அவற்றை தானாக அழைக்க முடியும். ஏஜண்ட் உருவாக்கும்போது கருவிகள் பதிவு செய்யப்படுகின்றன:

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

- **பல ஏஜண்ட் ஒருங்கிணைப்பு**. வேறுபட்ட சிறப்புகள் கொண்ட பல ஏஜண்ட்களை உருவாக்கி ஒருங்கிணைக்கலாம்:

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

- **Azure அடையாள ஒருங்கிணைப்பு**. `AzureCliCredential` (அல்லது `DefaultAzureCredential`) பயன்படுத்தி பாதுகாப்பான, API விசைகள் இல்லாத அங்கீகாரத்தை வழங்குகிறது, விசைகளை நேரடியாக நிர்வகிக்க தேவையில்லை.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service சமீபத்திய சேவையாக Microsoft Ignite 2024 இல் அறிமுகப்படுத்தப்பட்டது. இது அதிக தான்மை மாடல்களை உருவாக்க மற்றும் இயக்க அனுமதிக்கிறது, நேரடியாக திறந்த மூல LLMகளை மூலம் இதுபோன்ற Llama 3, Mistral மற்றும் Cohere போன்றவற்றை அழைக்க முடியும்.

Microsoft Foundry Agent Service வலுவான நிறுவன பாதுகாப்பு மற்றும் தரவு சேமிப்பு முறைகள் கொண்டுள்ளது, எனவே வணிக பயன்பாடுகளுக்கு சிறந்தது.

Microsoft Agent Framework உடன் ஒருங்கிணைந்து ஏஜண்ட்களை கட்டி இயக்க முடியும்.

இந்த சேவை தற்போது பொது பார்வைக்குரிய நிலையில் உள்ளது மற்றும் ஏஜண்ட்களை கட்ட Python மற்றும் C# மொழிகளை ஆதரிக்கிறது.

Microsoft Foundry Agent Service Python SDK பயன்படுத்தி பயனர் வரையறுக்கப்பட்ட கருவியுடன் ஏஜண்ட் உருவாக்கலாம்:

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

### முக்கியக் கருத்துகள்

Microsoft Foundry Agent Service இல் பின்வரும் முக்கிய கருத்துகள் உள்ளன:

- **ஏஜண்ட்**. Microsoft Foundry Agent Service Microsoft Foundry உடன் ஒருங்கிணைக்கப்பட்டுள்ளது. இங்கு AI ஏஜண்ட் ஒரு "அறிவுமிக்க" மைக்ரோசெர்விஸ் போல செயல்படுகிறது, இது கேள்விகளுக்கு பதில் (RAG), செயல்பாடுகள் செய்ய, அல்லது முழுமையாக தானியங்கு பணிகள் செய்வதற்காகப் பயன்படுத்தப்படுகிறது. இது உருவாக்கும் AI மாதிரிகளின் சக்தியை, உண்மையான தரவுச் மூலங்களை அணுகி தொடர்பு கொள்ள உதவும் கருவிகளுடன் இணைத்து இயற்றுகிறது. இங்கே ஒரு ஏஜண்ட் உதாரணம்:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    இந்த உதாரணத்தில், `gpt-5-mini` என்ற மாடல், `my-agent` என்ற பெயர் மற்றும் `You are helpful agent` என்ற அறிவுரைகளுடன் ஏஜண்ட் உருவாக்கப்படுகிறது. குறியீடுகளை விளக்கும் பணிகளுக்கான கருவிகள் மற்றும் வளங்கள் ஏஜண்டுக்கு வழங்கப்பட்டுள்ளன.

- **தொடர் மற்றும் செய்திகள்**. தொடர் என்பது இன்னும் முக்கியமான கருத்து. இது ஏஜண்ட் மற்றும் பயனருக்கு இடையேயான உரையாடல் அல்லது தொடர்பை குறிக்கிறது. தொடர்கள் உரையாடல் முன்னேற்றம், சூழல் தகவல் சேமிப்பு மற்றும் தொடர்பின் நிலையை நிர்வகிக்கப் பயன்படுத்தப்படுகின்றன. ஒரு தொடர் உதாரணம்:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # போலீசாரிடம் திரையறையிலே வேலை செய்ய கேளுங்கள்
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # போலீசாரின் பதிலை பார்க்க அனைத்து செய்திகளையும் பெற்று பதிவு செய்யுங்கள்
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    முன் குறியீட்டில் ஒரு தொடர் உருவாக்கப்பட்டு, பின்னர் அதில் ஒரு செய்தி அனுப்பப்பட்டுள்ளது. `create_and_process_run` அழைப்பால், ஏஜண்ட் தொடரில் பணியை செய்ய கேட்கப்படுகின்றது. கடைசியில் செய்திகளை பெற்று ஏஜண்டின் பதிலைக் காணலாம். இந்த செய்திகள் பயனர் மற்றும் ஏஜண்டின் உரையாடல் முன்னேற்றத்தை காட்டுகின்றன. செய்திகள் உரை, படம் அல்லது கோப்பான பல விதங்களாக இருக்க முடியும்; இது ஏஜண்டின் பணியின் விளைவாக இருக்கும். டெவலப்பராக நீங்கள் பின்னர் இந்தத் தகவலை பதிலை மேலதிகமாக செயலாக்கவும் அல்லது பயனருக்கு வழங்கவும் பயன்படுத்தலாம்.

- **Microsoft Agent Framework உடன் ஒருங்கிணைவு**. Microsoft Foundry Agent Service Microsoft Agent Framework உடன் சீராக ஒருங்கிணைகிறது, அதனால் `FoundryChatClient` மூலம் ஏஜண்ட்களை கட்டி, Agent Service வழியாக தயாரிப்புக்கு பயன்படுத்த முடியும்.

**பயன்பாட்டு வழக்குகள்**: Microsoft Foundry Agent Service மிகவும் பாதுகாப்பான, அளவுக்கேற்ற மற்றும் தானியங்கிய AI ஏஜண்ட் இயக்கத்திற்குப் பயன்படும்.

## இத்தரகான அணுகுமுறைகள் இடையே வேறுபாடு என்ன?
 
சிலபருவமாக ஒத்துள்ளன என்றாலும், வடிவமைப்பு, திறன் மற்றும் இலக்கு பயன்பாட்டில் சில முக்கிய வேறுபாடுகள் உள்ளன:
 
- **Microsoft Agent Framework (MAF)**: AI ஏஜண்ட்களை கட்டுவதற்கான தயாரிப்பு-திறன் SDK ஆகும். கருவி அழைப்பு, உரையாடல் மேலாண்மை மற்றும் Azure அடையாள ஒருங்கிணைப்புடன் எளிமையான API வழங்குகிறது.
- **Microsoft Foundry Agent Service**: Microsoft Foundryயில் ஏஜண்ட்களுக்கான மேடையும் இயக்க சேவையும். Azure OpenAI, Azure AI Search, Bing Search மற்றும் குறியீடு இயங்குதளத்துடன் முன்நிறுத்தப்பட்ட இணைப்புகளை வழங்குகிறது.
 
இன்னும் தேர்வதில் குழப்பு உள்ளதா?

### பயன்படுத்தும் வழிகள்
 
பொதுவான பயன்பாட்டை பார்ப்போம்:
 
> கேள்வி: தயாரிப்பு தயாரிக்க விரைவில் AI ஏஜண்ட் செயலிகள் கட்ட வேண்டும்
>

>பதில்: Microsoft Agent Framework சிறந்த தேர்வாகும். `FoundryChatClient` மூலம் கருவிகளும் அறிவுரைகளும் கொண்ட ஏஜண்ட்களை கொள்வது எளிதான Python API வழங்குகிறது.

> கேள்வி: Azure ஒருங்கிணைப்புகளுடன் (Search மற்றும் குறியீடு இயக்கம்) நிறுவன தர நிபந்தனை தேவையானது
>
>பதில்: Microsoft Foundry Agent Service சிறந்த சேவை. இது பல மாதிரிகள், Azure AI Search, Bing Search மற்றும் Azure Functions இணைந்து வழங்குகிறது. Foundry போர்டலில் எளிதில் ஏஜண்ட்களை கட்டி பெரிய அளவில் இயக்க உதவுகிறது.
 
> கேள்வி: இன்னும் குழப்பமாக உள்ளது, ஒரு தேர்வு மட்டும் சொல்லுங்கள்
>
>பதில்: முதலில் Microsoft Agent Framework இதயமாக ஏஜண்ட் கட்டவும், பிறகு தயாரிப்பில் இயக்கம் மற்றும் அளவுபடுத்த Microsoft Foundry Agent Service பயன்படுத்தவும். இது உங்கள் ஏஜண்ட் கர logicல் விரைவில் மேம்படுத்த கிடைக்கும் வழி.
 
முக்கிய வேறுபாடுகளை அட்டவணையில்:

| கட்டமைப்பு | கவனம் | முக்கிய கருத்துக்கள் | பயன்பாடு |
| --- | --- | --- | --- |
| Microsoft Agent Framework | கருவி அழைப்புடன் எளிய ஏஜண்ட் SDK | ஏஜண்ட்கள், கருவிகள், Azure அடையாளம் | AI ஏஜண்ட்கள் கட்டுதல், கருவி பயன்பாடு, பல படி பணிகள் |
| Microsoft Foundry Agent Service | த/free/ழமை மாடல்கள், நிறுவன பாதுகாப்பு, குறியீடு உருவாக்கம், கருவி அழைப்பு | கூறுத்தன்மை, ஒத்துழைப்பு, செயல்முறை ஒருங்கிணைப்பு | பாதுகாப்பான, அளவுக்கேற்ற, த/free/ழமை AI ஏஜண்ட் இயக்கம் |

## ஏற்கனவே உள்ள Azure சூழல் கருவிகளை நேரடியாக இணைக்கலாமா, அல்லது தனித்துவமான தீர்வுகள் தேவைபடுமா?


ஆம் என்பது பதில், நீங்கள் உங்கள் இருந்த Azure சூழல் கருவிகளை நேரடியாக Microsoft Foundry Agent Service உடன் ஒருங்கிணைக்கலாம், குறிப்பாக, இது மற்ற Azure சேவைகளுடன் சீராக செயல்பட கட்டமைக்கப்பட்டுள்ளது. உதாரணமாக, நீங்கள் Bing, Azure AI Search, மற்றும் Azure Functions ஐ ஒருங்கிணைக்கலாம். Microsoft Foundry உடனான ஆழ்ந்த ஒருங்கிணைப்பு கூட உள்ளது.

Microsoft Agent Framework கூட Azure சேவைகளுடன் `FoundryChatClient` மற்றும் Azure அடையாளத்தின் மூலம் ஒருங்கிணைக்கப்பட்டுள்ளது, இது உங்கள் முகவரிகள் கருவிகளிலிருந்து நேரடியாக Azure சேவைகளை அழைக்க அனுமதிக்கிறது.

## மாதிரி குறியீடுகள்

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI முகவர் கட்டமைப்புகள் பற்றிய மேலும் கேள்விகள் உள்ளதா?

மற்ற கற்றுக் கொள்பவர்களை சந்திக்க, அலுவலக நேரங்களுக்கு செல்லவும் மற்றும் உங்கள் AI முகவர்கள் தொடர்பான கேள்விகளுக்கு பதில்களை பெற [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) இல் சேருங்கள்.

## குறிப்பு

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent சேவை</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent சேவை</a>

## முந்தய பாடம்

[AI முகவர்கள் மற்றும் முகவர் பயன்பாட்டு நிலைகள் அறிமுகம்](../01-intro-to-ai-agents/README.md)

## அடுத்த பாடம்

[Agentic வடிவமைப்பு மாதிரிகள் புரிதல்](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->