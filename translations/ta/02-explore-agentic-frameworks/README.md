[![Exploring AI Agent Frameworks](../../../translated_images/ta/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(இந்த பாடத்தின் வீடியோவை பார்க்க மேலுள்ள படத்தை அழுத்தவும்)_

# AI முகவரிகள் வடிவமைப்புகளை ஆராய்க

AI முகவர் வடிவமைப்புகள் என்பது AI முகவரிகளை உருவாக்க, பரப்பவும், நிர்வகிப்பதற்கான சிரமங்களை எளிதாக்க உருவாக்கப்பட்ட மென்பொருள் பிளாட்ஃபாரங்களாகும். இந்த வடிவமைப்புகள் டெவலப்பர்களுக்கு முன்கூட்டிய கூறுகள், உலகளாவிய கண்ணோட்டம் மற்றும் கருவிகள் வழங்கி, சிக்கலான AI அமைப்புகளின் மேம்பாட்டை எளிதாக்குகின்றன.

இந்த வடிவமைப்புகள் டெவலப்பர்களை அவர்களது பயன்பாடுகளின் தனித்துவமான அம்சங்களில் கவனம் செலுத்த உதவுகின்றன; AI முகவர் மேம்பாட்டில் பொதுவான சவால்களுக்கு சர்வாதிகார ப approach களை வழங்குகின்றன. AI அமைப்புகளை கட்டுவதில் மாற்றுத்திறன், அணுகல் மற்றும் செயல்திறனை மேம்படுத்துகின்றன.

## அறிமுகம் 

இந்த பாடத்தில் நாம் பார்ப்பதுகள்:

- AI முகவர் வடிவமைப்புகள் என்ன மற்றும் அவை டெவலப்பர்களுக்கு என்ன செய்ய உதவுகின்றன?
- குழுக்கள் எப்படி இவற்றை விரைவாக புரோட்டோடைப் செய்ய, நுணுக்கப்படுத்த மற்றும் முகவர்களின் திறன்களை மேம்படுத்த பயன்படுத்தலாம்?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> மற்றும் <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) உருவாக்கிய வடிவமைப்புகள் மற்றும் கருவிகளுக்கிடையேயான வேறுபாடுகள் என்ன?
- நான் என் தற்போதைய Azure சூழல் கருவிகளை நேரடியாக இணைக்கலாமா, அல்லது தனிப்பட்ட தீர்வுகள் தேவையா?
- Microsoft Foundry Agent Service என்ன, இது எனக்கு எப்படி உதவுகிறது?

## கற்றல் இலக்குகள்

இந்த பாடத்தின் இலக்குகள் இவ்வாறு:

- AI Agent Frameworks இன் AI மேம்பாட்டில் தாங்கும் பங்கு.
- கற்றல் முகவர்களை கட்ட AI Agent Frameworks இனை எப்படி பயன்படுத்துவது.
- AI Agent Frameworks மூலம் செயல்படுத்தப்படும் முக்கிய திறன்கள்.
- Microsoft Agent Framework மற்றும் Microsoft Foundry Agent Service இடையேயான வேறுபாடுகள்.

## AI Agent Frameworks என்ன மற்றும் அவை டெவலப்பர்களுக்கு என்ன செய்ய உதவுகின்றன?

பாரம்பரிய AI வடிவமைப்புகள் உங்கள் செயலிகள் AI கொண்டு மேம்படுத்த உதவுகின்றன, கீழ்க்காணும் வழிகளில்:

- **தனிப்பயன்பாடு**: AI பயனர் செயல்பாடுகள் மற்றும் விருப்பங்களை பகுப்பாய்வு செய்து தனிப்பட்ட பரிந்துரைகள், உள்ளடக்கம் மற்றும் அனுபவங்களை வழங்க முடியும்.
உதாரணம்: Netflix போன்ற ஸ்ட்ரீமிங் சேவைகள் AI-யைப் பயன்படுத்தி பார்வை வரலாற்றை அடிப்படையாகக் கொண்டு திரைப்படங்கள் மற்றும் நிகழ்ச்சிகளை பரிந்துரைக்கின்றன, இது பயனர் ஈடுபாடு மற்றும் திருப்தியை அதிகரிக்கின்றது.
- **தானியங்கி மற்றும் திறன்**: AI சீரமைப்பு பணிகளை தானியங்கிக் கொண்டு, செயற்குழு வேலைப்பாட்டை எளிதாக்கி, செயல்பாட்டு திறனை மேம்படுத்த முடியும்.
உதாரணம்: வாடிக்கையாளர் சேவை செயலிகள் AI சார்ந்த சாட்பாட்களைப் பயன்படுத்தி பொதுவான கேள்விகளுக்கு பதிலளித்து, எதிர்கால நேரத்தை குறைத்து, மனித முகவர்களை சிக்கலான பிரச்சனைகளுக்காக விடுவிக்கின்றன.
- **மேம்படுத்தப்பட்ட பயனர் அனுபவம்**: AI குரல் அடையாளம், இயற்கை மொழி செயலாக்கம் மற்றும் முன்னறிவிப்பு உரை போன்ற அறிவார்ந்த அம்சங்களைக் கொண்டு முழுமையான பயனர் அனுபவத்தை மேம்படுத்த முடியும்.
உதாரணம்: Siri, Google Assistant போன்ற மெய்நிகர் உதவியாளர்கள் AI வினாக்களை புரிந்து குரல் கட்டளைகளை மேற்கொண்டு, பயனர்களுக்கு சாதனங்களுடன் எளிதாக தொடர்பது செய்யும்.

### இது எல்லாம் அருமைதான், ஆனா ஏன் AI Agent Framework தேவை?

AI Agent Frameworks என்பது வெறும் AI வடிவமைப்பு இல்லை. இது பயனர்களுடன், மற்ற முகவர்களுடன் மற்றும் சூழலைச் சேர்ந்திழப்புடன் தொடர்பு கொண்டே ஒரு குறிப்பிட்ட இலக்கை அடைவதற்கான அறிவார்ந்த முகவர்களை உருவாக்குவதற்காக வடிவமைக்கப்பட்டுள்ளது. இந்த முகவர்கள் தன்னிச்சையான நடத்தை காட்சிப்படுத்து, முடிவெடுக்கவும் மற்றும் மாற்றமடைந்த சூழலுக்கு தகுந்துவிடவும் יכולים. AI Agent Frameworks மூலம் கிடைக்கும் சில முக்கிய செயல்திறன்கள் இவை:

- **முகவர் ஒத்துழைப்பு மற்றும் ஒருங்கிணைப்பு**: பல AI முகவர்கள் ஒன்றாக வேலை செய்து, தொடர்பு கொண்டு, சிக்கலான பணிகளை தீர்க்கவும் உதவுகின்றனர்.
- **பணி தானியங்கி மற்றும் மேலாண்மை**: பல படி வேலைப்பாட்டை தானியங்கி செய்ய, பணியை ஒதுக்கீடு செய்ய மற்றும் முகவர்களுக்கிடையேயான பணி மேலாண்மையை இயக்கும் வகையில் முறைகளை வழங்குகிறது.
- **சூழல் புரிதல் மற்றும் தகுந்துத்தன்மை**: முகவர்கள் சூழலைப் புரிந்து, மாற்றமடைந்த சூழலுக்கு ஏற்ப தக்கமாற்றங்களை மேற்கொண்டு, நேரடி தகவலின் அடிப்படையில் முடிவெடுக்க திறன் பெறுகின்றனர்.

சுருக்கமாக, முகவர்கள் உங்களுக்கு அதிக வேலை செய்ய முடியும், தானியக்கத்தை அடுத்த நிலைக்கு கொண்டு செல்கின்றன, மேலும் அவர்கள் சூழலைப் புரிந்து கற்று என்ன கற்றுக்கொள்கின்றன என்பதன் மூலம் அறிவார்ந்த அமைப்புகளை உருவாக்க உதவுகின்றன.

## முகவர்களின் திறன்களை விரைவாக புரொட்டோடைபிங், திருத்தம் மற்றும் மேம்படுத்துவது எப்படி?

இது வேகமாக மாறும் உலகம், ஆனாலும் பல AI Agent Frameworks இல் பொதுவான அம்சங்கள் உள்ளன: கூறுகள், ஒத்துழைப்பு கருவிகள் மற்றும் நேரடி கற்றல். இவை என்ன என்பதை பார்ப்போம்:

- **மொடுலர் கூறுகளை பயன்படுத்தவும்**: AI SDKக்கள் AI மற்றும் நினைவக இணைப்பாளிகள், இயற்கை மொழி அல்லது குறியீட்டு பிளக்-இன்கள் மூலம் செயல்பட்ட குறிப்பிடுதற்கான கூறுகள் மற்றும் சார்பு வடிவங்கள் போன்ற முன்கூட்டிய கூறுகளை வழங்குகின்றன.
- **ஒத்துழைப்பு கருவிகளை பயன்படுத்தவும்**: குறிப்பிட்ட பங்கு மற்றும் பணி கொண்ட முகவர்களை வடிவமைக்கவும், ஒத்துழைப்பு வேலைப்பாடுகளை சோதனை செய்து மேம்படுத்தவும் உதவும்.
- **நேரடி கற்றல்**: முகவர்கள் தொடர்புகளிலிருந்து கற்றுக் கொண்டு தம் நடத்தை தானாக சமைகின்ற கருத்து வழங்கும் முடிவு தொகுதிகளை செயல்படுத்தவும்.

### மோடுலர் கூறுகளை பயன்படுத்தவும்

Microsoft Agent Framework போன்ற SDKகள் AI இணைப்பாளிகள், கருவி வரையறைகள் மற்றும் முகவர் மேலாண்மை போன்ற முன்கூட்டிய கூறுகளை வழங்குகின்றன.

**குழுக்கள் இதைப் பயன்படுதல்**: குழுக்கள் இந்த கூறுகளை விரைவாக ஒன்றிணைத்து செயல்பாட்டுக்கான ஒரு புரொட்டோடைப்பை உருவாக்க முடியும், இதனால் வேகமான மேம்பாடு மற்றும் திருத்தம் செய்ய முடியும்.

**வாவகையில் இது எப்படி செயல் படும்**: பயனர் உள்ளீட்டிலிருந்து தகவலை எடுக்க முன்கூட்டிய பகுப்பாய்வாளரை பயன்படுத்தலாம், தரவை சேமித்து மீட்டெடுக்க நினைவக கூறை பயன்படுத்தலாம் மற்றும் பயனர்களுடன் தொடர்பு கொள்ள ப்ராம்ட் உருவாக்கியை பயன்படுத்தலாம் - இவை அனைத்தும் இருப்பினும், கூறுகளை இனிமேல் உருவாக்க தேவையில்லை.

**உதாரணக் குறியீடு**. Microsoft Agent Framework ஐ `FoundryChatClient` உடன் எப்படி பயன்படுத்தி மாடலை கருவிகள் அழைக்கும் பதில்களை உருவாக்கலாம் என்பதைக் காண்போம்:

``` python
# மைக୍ரோசாஃப்ட் ஏஜென்ட் ஃப்ரேம்வொர்க் பைதான் உதாரணம்

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# பயணம் முன்பதிவு செய்ய ஒரு மாதிரியான கருவி செயல்பாட்டை வரையறுக்கவும்
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
    # உதாரணமான வெளியீடு: 2025 ஜனவரி 1 ஆம் தேதி நியூயார்க்குக்கு உங்கள் விமானம் வெற்றிகரமாக முன்பதிவு செய்யப்பட்டுள்ளது. பாதுகாப்பான பயணம்! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

இந்த உதாரணத்தில், பயனர் உள்ளீட்டிலிருந்து முக்கிய தகவல்கள் (எதிர்வரும் இடம், செல்லும் இடம், தேதி) போன்றவை எடுத்து பயன்படுத்தும் முன்கூட்டிய பகுப்பாய்வாளர் எப்படி பயன்படுகிறது என்பதை காணலாம். இந்த மோடுலர் அணுகுமுறை உங்களுக்குத் தலைமை தர்க்கத்தில் கவனம் செலுத்த அனுமதிக்கின்றது.

### ஒத்துழைப்பு கருவிகளை பயன்படுத்தவும்

Microsoft Agent Framework போன்ற வடிவமைப்புகள் ஒருங்கிணைந்து பணியாற்றக்கூடிய பல முகவர்களை உருவாக்க உதவுகின்றன.

**குழுக்கள் இதைப் பயன்படுதல்**: குழுக்கள் பல முகவர்களை வகுப்புடன் மற்றும் பங்களிப்புடன் வடிவமைக்கவும், ஒத்துழைப்பு வேலைப்பாட்டை சோதனை செய்து மேம்படுத்தவும், மொத்த செயல்திறனை கூட்ட முடியும்.

**வாவகையில் இது எப்படி செயல் படும்**: தரவு மீட்டெடுப்பு, பகுப்பாய்வு அல்லது முடிவு எடுப்பின் ஒவ்வொரு பணிக்குமான நிபுணத்துவ முகவர்களை உருவாக்கலாம். இந்த முகவர்கள் ஒருங்கிணைந்து பயனர் கேள்விக்கு பதில் அளிக்க அல்லது பணி நிறைவேற்ற ஒன்றாக பணியாற்றுகிறார்கள்.

**உதாரணக் குறியீடு (Microsoft Agent Framework)**:

```python
# மைக்ரோசாஃப்ட் ஏஜென்ட் கட்டமைப்பைப் பயன்படுத்தி ஒன்றாக வேலை செய்யும் பல ஏஜென்டுகளை உருவாக்குதல்

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# தரவு மீட்டெடுக்கும் ஏஜென்ட்
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# தரவு பகுப்பாய்வு ஏஜென்ட்
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ஒரு பணியில் வரிசைப்படுத்தி ஏஜென்ட்களை இயக்குதல்
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

மேலே உள்ள குறியீட்டில் பல முகவர்கள் கலந்து தரவை பகுப்பாய்வு செய்யும் பணியை உருவாக்குவது எப்படி என்பதைக் காணலாம். ஒவ்வொரு முகவரும் தனித்துவமான பணி செய்கிறது, மேலும் முகவர்கள் ஒருங்கிணைந்து டாஸ்க்கை நிறைவேற்றுகின்றனர். இதனால் பணி திறன் மற்றும் செயல்திறன் மேம்படுகிறது.

### நேரடியாக கற்றல்

முன்னேற்றமடைந்த வடிவமைப்புகள் நேரடி சூழல் புரிதல் மற்றும் தகுந்துத்தன்மைக்கு திறனை வழங்குகின்றன.

**குழுக்கள் இதைப் பயன்படுதல்**: முகவர்கள் தொடர்புகளிலிருந்து கற்றுக்கொண்டு தங்கள் நடத்தை தானாக மாற்றிக் கொள்ளும் கருத்து வழங்கும் முறைகளை உருவாக்கலாம்; இது திறன்களின் தொடர்ச்சியான மேம்பாடு மற்றும் நுணுக்கப்படுத்தலை ஏற்படுத்தும்.

**வாவகையில் இது எப்படி செயல் படும்**: முகவர்கள் பயனர் பின்னூட்டம், சூழல் தரவு மற்றும் பணிப் விளைவுகளை பகுப்பாய்வு செய்து தங்கள் அறிவுத் தளத்தை புதுப்பிக்க, முடிவு எடுக்கும் கருவிகளை சீரமைக்கவும், நேரடி நேர்த்தியான செயல்திறனை மேம்படுத்திக் கொள்கின்றனர். இந்த திரும்பப்பெறும் கற்றல் செயல்முறை அவற்றை மாற்றம் அடைந்த சூழல் மற்றும் பயனர் விருப்பங்களுக்கு தக்கவாறு எளிதாக்குகிறது மற்றும் மொத்த அமைப்பின் பயன்முறைத்தன்மையை மேம்படுத்துகிறது.

## Microsoft Agent Framework மற்றும் Microsoft Foundry Agent Service இடையேயான வேறுபாடுகள் என்ன?

இந்த அணுகுமுறைகளை பலவாறு ஒப்பிடலாம், ஆனால் அவற்றின் வடிவமைப்பு, திறன்கள் மற்றும் நோக்கிய பயன்பாடுக்களின் கட்டமைப்பில் சில முக்கிய வேறுபாடுகளை பார்ப்போம்:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework என்பது `FoundryChatClient` பயன்படுத்தி AI முகவர்களை உருவாக்க எளிய SDK யை வழங்குகிறது. இது Azure OpenAI மாதிரிகளை பயன்படுத்தி கருவிகள் அழைப்பு, உரையாடல் மேலாண்மை மற்றும் Azure அடையாளம் மூலம் நிறுவன தரப்படுத்தப்பட்ட பாதுகாப்பை வழங்குகிறது.

**பயன்பாட்டு நிலைகள்**: கருவி பயன்பாடு, பல படி வேலைவழிகள், மற்றும் நிறுவன ஒருங்கிணைப்பு சூழல்களில் தயாரிப்புக்கான AI முகவர்களை கட்டல்.

Microsoft Agent Framework இன் சில முக்கிய மூலக் கருத்துக்கள்:

- **முகவர்கள்**: `FoundryChatClient` மூலம் ஒரு முகவர் உருவாக்கப்பட்டு பெயர், வழிகாட்டிகள் மற்றும் கருவிகள் உடன் கட்டமைக்கப்படுகிறது. அந்த முகவர்:
  - **பயனர் செய்திகளை செயலாக்கி** Azure OpenAI மாதிரிகளைக் கொண்டு பதில்களை உருவாக்குகிறது.
  - **உரையாடல் சூழலுக்கேற்ப** கருவிகளை தானாக அழைக்க முடியும்.
  - **பல தொடர்புகளில் உரையாடல் நிலையை பராமரிக்க முடியும்**.

  ஒரு முகவர்களை உருவாக்கும் குறியீட்டு பகுதியைப் பார்க்கலாம்:

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

- **கருவிகள்**: வடிவமைப்பு கருவிகளை Python செயல்பாடுகளாக வரையறுக்க அனுமதிக்கிறது; முகவர் தாமாகவே அவற்றை அழைக்கலாம். கருவிகள் முகவரைக் கட்டும் போது பதிவு செய்யப்படுகின்றன:

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

- **பல முகவர் ஒருங்கிணைப்பு**: வித்தியாசமான நுட்பங்கள் கொண்ட பல முகவர்களை உருவாக்கி அவற்றின் வேலையை ஒருங்கிணைக்க முடியும்:

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

- **Azure அடையாள ஒருங்கிணைப்பு**: API விசைகளை நேரடியாக நிர்வகிக்கும் தேவையின்றி `AzureCliCredential` (அல்லது `DefaultAzureCredential`) மூலம் பாதுகாப்பான, விசையில்லா அங்கீகாரத்தை வழங்குகிறது.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service என்பது 2024 Microsoft Ignite இல் அறிமுகப்படுத்தப்பட்ட சமீபத்திய சேவை. இது Llama 3, Mistral மற்றும் Cohere போன்ற திறந்த மூல LLM களை நேரடியாக அழைக்கும் நெட்வொர்க் மாதிரிகள் உடன் AI முகவர்கள் உருவாக்கவும் பரப்பவும் அனுமதிக்கிறது.

Microsoft Foundry Agent Service நிறுவன பாதுகாப்பு செயல்முறைகள் மற்றும் தரவு சேமிப்பு முறைகள் வலுவானவை; எனவே இது நிறுவன பயன்பாடுகளுக்கு ஏற்றதாகும்.

Microsoft Agent Framework உடன் ஒருங்கிணைந்து முகவர்களை உருவாக்கி பரப்புவது சுலபம்.

இந்த சேவை தற்பொழுது பொது முன்னோட்ட நிலையில் உள்ளது மற்றும் Python மற்றும் C# மூலமாக முகவர்களை உருவாக்க ஆதரவளிக்கிறது.

Microsoft Foundry Agent Service Python SDK பயன்படுத்தி, பயனர் பிரத்தியேக கருவியைக் கொண்டு முகவர்களை உருவாகலாம்:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# கருவி செயல்பாடுகளை வரையறுக்கவும்
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

### முக்கிய கருத்துக்கள்

Microsoft Foundry Agent Service இன் கீழ்க்கண்ட முக்கிய கருத்துக்கள் உள்ளன:

- **முகவர்**: Microsoft Foundry ஐ உட்பட்கொண்டு Microsoft Foundry Agent Service ஒரு "அறிவார்ந்த" மைக்ரோசெர்வீசாக செயல்படும் AI முகவர்களை உருவாக்க அனுமதிக்கிறது. இவர்கள் RAG (வினாத்தொடர்பு), செயல்பாடுகள் நிறைவேற்றுதல், அல்லது வேலைநெறிகளை முழுமையாக தானியக்கமாக்க நடவடிக்கைகள் எடுக்கின்றனர். இது உருவாக்கும் AI மாதிரிகள் மற்றும் உண்மை உலக தரவு ஆதாரங்கள் அணுக மற்றும் தொடர்பு கொள்ள உதவும் கருவிகளைப் பயன்படுத்தி அடையப்படுகிறது. முகவர்களின் உதாரணம் இங்கே:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    இந்த உதாரணத்தில், `gpt-4.1-mini` மாதிரி, `my-agent` என்ற பெயர் மற்றும் `You are helpful agent` என்ற வழிகாட்டிகளுடன் ஒரு முகவர் உருவாக்கப்பட்டுள்ளது. இந்த முகவரி குறியீட்டுப் புரிதல் பணிகளை செய்ய கருவிகள் மற்றும் வளங்களுடன் பதிவு செய்யப்பட்டுள்ளது.

- **தொடர் மற்றும் செய்திகள்**: தொடர் என்பது ஒரு முக்கிய கருத்து ஆகும். இது முகவர் மற்றும் பயனர் இடையேயான உரையாடல் அல்லது தொடர்பை குறிக்கிறது. உரையாடலின் முன்னேற்றத்தை கண்காணிக்க, சூழல் தகவல்களை சேமிக்க மற்றும் தொடர்பின் நிலையை நிர்வகிக்க தொடர்கள் பயன்படுத்தப்படுகின்றன. இதோ ஒரு தொடர் உதாரணம்:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # செயலியை திரெட்டில் பணி செய்ய கேளுங்கள்
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # செயலியின் பதிலை பார்க்க அனைத்து செய்திகளையும் எக்கவும் பதிவு செய்யவும்
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    மேலே உள்ள குறியீட்டில் ஒரு தொடர் உருவாக்கப்படுகிறது. பின்னர் அந்த தொடருக்கு ஒரு செய்தி அனுப்பப்படுகிறது. `create_and_process_run` அழைப்பால், முகவரிடம் தொடரில் பணி செய்வதற்கு கோர்கிறது. இறுதியில், செய்திகள் எடுக்கப்பட்டு முகவரின் பதிலை காண்பிக்க பதிவு செய்யப்படுகிறது. இந்த செய்திகள் பயனர் மற்றும் முகவருக்கிடையேயான உரையாடல் முன்னேற்றத்தை காட்டுகின்றன. செய்திகள் எழுத்து, படம், கோப்பு போன்ற வெவ்வேறு வகைகளை கொண்டிருக்கக்கூடும்; அதாவது முகவரி உதவிக் கோப்புகள் அல்லது எழுத்து பதில்களை உருவாக்கியிருக்கலாம். டெவலப்பர் இந்தத் தகவலை மேலும் செயல்படுத்த அல்லது பயனருக்கு காட்ட பயன்படுத்தலாம்.

- **Microsoft Agent Framework உடன் ஒருங்கிணைப்பு**: Microsoft Foundry Agent Service Microsoft Agent Framework உடன் சீரான ஒருங்கிணைப்பை வழங்குகிறது, இதன் மூலம் `FoundryChatClient` ஐ பயன்படுத்தி முகவர்கள் உருவாக்கி, உற்பத்தி சூழலுக்கு பரப்பக்கூடியதாக இருக்கிறது.

**பயன்பாட்டு நிலைகள்**: Microsoft Foundry Agent Service நிறுவனம் தேவைப்படும் பாதுகாப்பான, உயர்தர அளவிடும் மற்றும் திடமான AI முகவர் பரப்புதலுக்காக வடிவமைக்கப்பட்டது.

## இந்த அணுகுமுறைகளில் என்ன வேறுபாடுகள் இருக்கின்றன?
 
இது ஒட்டுமொத்தமாக ஒத்திருக்கலாம், ஆனால் வடிவமைப்பு, திறன்கள் மற்றும் நோக்கிய பயன்பாடுகளின் அடிப்படையில் சில முக்கிய வேறுபாடுகள் உள்ளன:
 
- **Microsoft Agent Framework (MAF)**: தயாரிப்புக்கு தயாராக இருக்கும் SDK ஆகும். கருவி அழைப்பு, உரையாடல் மேலாண்மை மற்றும் Azure அடையாள ஒருங்கிணைப்பு ஆகியவற்றுடன் முகவர்களை உருவாக்க எளிமையான API வழங்குகிறது.
- **Microsoft Foundry Agent Service**: Microsoft Foundry இல் முகவர்களுக்கு ஒரு தளம் மற்றும் பரப்பும் சேவையாகும். Azure OpenAI, Azure AI Search, Bing Search மற்றும் குறியீட்டை செயல் படுத்தும் சேவைகளுடன் ஒருங்கிணைக்கப்பட்டுள்ளது.
 
இன்னமும் எது தேர்ந்தெடுக்க வேண்டும் என்று உறுதியாக இல்லைவா?

### பயன்பாட்டு நிலைகள்
 
பொதுவான சில பயன்பாடுகளுக்கு உதவுவோம்:
 
> கேள்வி: நான் தயாரிப்புக்கான AI முகவர் பயன்பாடுகளை உருவாக்கி விரைவாக தொடங்க விரும்புகிறேன்
>

>பதில்: Microsoft Agent Framework சிறந்த தேர்வு. இது `FoundryChatClient` மூலம் கருவிகள் மற்றும் வழிகாட்டிகளுடன் முகவர்களை வரையறுக்க 몇 வரிகள் குறியீடு yeter, எளிமையான மற்றும் பைதானிக் API வழங்குகிறது.

> கேள்வி: எனக்கு Azure ஒருங்கிணைப்புகள் உட்பட நிறுவனம் தரப்பட்ட பரப்புதலும் தேவை, தேடல் மற்றும் குறியீட்டு இயக்கங்கள் போல
>
> பதில்: Microsoft Foundry Agent Service சிறந்த பொருத்தம். இது பல மாதிரிகள், Azure AI Search, Bing Search மற்றும் Azure Functions உடைய நிழற்படிக் கட்டமைப்புடன் ஒரு தளம் சேவையாகும். Foundry போர்டலில் உங்கள் முகவர்களை உருவாக்கி பரப்பும் பணியை எளிதாக்குகிறது.
 
> கேள்வி: நான் இன்னும் குழப்பத்தில் இருக்கிறேன், ஒரு விருப்பம் மட்டும் சொல்லுங்கள்
>
> பதில்: முதலில் Microsoft Agent Framework-ஐத் தொடங்கிக் கொண்டு உங்கள் முகவர்களை கட்டியமைக்கவும், பின்னர் உற்பத்தி நிலை பரப்புதலுக்கு Microsoft Foundry Agent Service பயன்படுத்தவும். இது முகவர் தர்க்கத்தில் விரைவாக திருத்தங்களைச் செய்யும் வழியையும் நிறுவன அளவுக்கு பரப்பும் வழியையும் தருகிறது.
 
முக்கிய வேறுபாடுகளை ஒரு அட்டவணையில் சுருக்கி பார்க்கலாம்:

| வடிவமைப்பு | கவனம் | முக்கிய கருத்துக்கள் | பயன்பாடு |
| --- | --- | --- | --- |
| Microsoft Agent Framework | கருவி அழைப்புடன் நிலைநாட்டப்பட்ட முகவர் SDK | முகவர்கள், கருவிகள், Azure அடையாளம் | AI முகவர்கள் கட்டல், கருவி பயன்பாடு, பல படி வேலைவழிகள் |
| Microsoft Foundry Agent Service | திடமான மாதிரிகள், நிறுவனம் பாதுகாப்பு, குறியீட்டு உற்பத்தி, கருவி அழைப்பு | கூறுபாடு, ஒத்துழைப்பு, செயல்முறை ஒருங்கிணைப்பு | பாதுகாப்பான, உயர்தர அளவிடக்கூடிய மற்றும் திடமான AI முகவர் பரப்பு |

## நான் என் தற்போதைய Azure சூழல் கருவிகளை நேரடியாக இணைக்கலாமா, அல்லது தனிப்பட்ட தீர்வுகள் தேவைபடுமா?


பதில் ஆம், உங்கள் ஏற்கனவே உள்ள Azure சூழல் கருவிகளை Microsoft Foundry Agent Service உடன் நேரடியாக இணைக்கலாம், குறிப்பாக இது பிற Azure சேவைகளுடன் சீரான முறையில் செயல்பட உருவாக்கப்பட்டுள்ளதால். உதாரணமாக, Bing, Azure AI Search, மற்றும் Azure Functions ஐ இணைக்கலாம். Microsoft Foundry உடன் ஆழமான ஒருங்கிணைப்பு உண்டு.

Microsoft Agent Framework Azure சேவைகளுடன் `FoundryChatClient` மற்றும் Azure அடையாளத்தின் மூலம் ஒருங்கிணைகிறது, இது உங்கள் முகவர் கருவிகளிலிருந்து நேரடியாக Azure சேவைகளை அழைக்க அனுமதிக்கிறது.

## மாதிரி குறியீடு

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI முகவர் கட்டமைப்புகள் குறித்து மேலதிக கேள்விகள் உள்ளதா?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) உடன் சேரவும், மற்ற கற்றலாளர்களைச் சந்திக்கவும், அலுவலக நேரங்களில் பங்கேற்கவும் மற்றும் உங்கள் AI முகவர் கேள்விகளுக்கு விடைகள் பெறவும்.

## குறிப்பு

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## முந்தைய பாடம்

[AI முகவர்களின் அறிமுகம் மற்றும் முகவர் பயன்பாட்டு வழக்குகள்](../01-intro-to-ai-agents/README.md)

## அடுத்த பாடம்

[Agentic வடிவமைப்பு விதிகள் புரிதல்](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->