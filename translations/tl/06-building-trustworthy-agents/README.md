[![Trustworthy AI Agents](../../../translated_images/tl/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(I-click ang larawan sa itaas upang mapanood ang video ng aralin na ito)_

# Pagtatayo ng Mapagkakatiwalaang Mga AI Agents

## Panimula

Sasaklawin ng araling ito ang:

- Paano bumuo at mag-deploy ng ligtas at epektibong mga AI Agents
- Mahahalagang konsiderasyon sa seguridad kapag nagde-develop ng mga AI Agents.
- Paano mapanatili ang privacy ng data at user kapag nagde-develop ng mga AI Agents.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano:

- Tukuyin at bawasan ang mga panganib kapag lumilikha ng AI Agents.
- Magpatupad ng mga hakbang sa seguridad upang masiguro na maayos na pinamamahalaan ang data at access.
- Lumikha ng mga AI Agents na nagpapanatili ng privacy ng data at nagbibigay ng kalidad na karanasan sa user.

## Kaligtasan

Tingnan muna natin ang pagtatayo ng mga ligtas na agentic applications. Ang kaligtasan ay nangangahulugan na ang AI agent ay gumaganap ayon sa disenyo. Bilang mga tagabuo ng agentic applications, mayroon tayong mga pamamaraan at kasangkapan upang mapalawak ang kaligtasan:

### Pagbuo ng System Message Framework

Kung nakabuo ka na ng AI application gamit ang Large Language Models (LLMs), alam mo ang kahalagahan ng pagdidisenyo ng matibay na system prompt o system message. Ang mga prompt na ito ay nagtatakda ng meta rules, mga tagubilin, at mga patnubay kung paano makikipag-ugnayan ang LLM sa user at data.

Para sa mga AI Agents, ang system prompt ay mas mahalaga pa dahil kailangan ng AI Agents ng mas tiyak na mga tagubilin upang matapos ang mga gawain na idinisenyo para sa kanila.

Upang makalikha ng mga scalable na system prompts, maaari tayong gumamit ng system message framework para bumuo ng isa o higit pang mga agents sa ating application:

![Building a System Message Framework](../../../translated_images/tl/system-message-framework.3a97368c92d11d68.webp)

#### Hakbang 1: Gumawa ng Meta System Message

Ang meta prompt ay gagamitin ng LLM upang bumuo ng mga system prompt para sa mga agents na ating nilikha. Dinidesenyo natin ito bilang template upang epektibong makalikha ng maraming agents kung kinakailangan.

Narito ang isang halimbawa ng meta system message na ibibigay natin sa LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Hakbang 2: Gumawa ng basic prompt

Ang susunod na hakbang ay gumawa ng basic prompt upang ilarawan ang AI Agent. Dapat mong isama ang papel ng agent, mga gawain na tatapusin ng agent, at iba pang mga responsibilidad ng agent.

Narito ang isang halimbawa:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Hakbang 3: Ibigay ang Basic System Message sa LLM

Ngayon ay maaari nating i-optimize ang system message na ito sa pamamagitan ng pagbibigay ng meta system message bilang system message pati na ang ating basic system message.

Magbubunga ito ng isang system message na mas maganda ang disenyo para gabayan ang ating mga AI agents:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Hakbang 4: Ulitin at Pagsikapan ang Pagbuti

Ang halaga ng system message framework na ito ay upang mapadali ang pag-scale ng paggawa ng mga system messages mula sa maraming agents pati na rin ang pagpapabuti ng iyong mga system messages sa paglipas ng panahon. Bihira kang magkaroon ng system message na gumagana nang perpekto sa unang subok para sa iyong kumpletong kaso. Ang kakayahang gumawa ng maliliit na tweaks at improvements sa pamamagitan ng pagbabago ng basic system message at pagpapagana nito sa sistema ay magpapahintulot sa iyo na ikumpara at suriin ang mga resulta.

## Pag-unawa sa mga Banta

Upang makabuo ng mapagkakatiwalaang mga AI agents, mahalagang maunawaan at mabawasan ang mga panganib at banta sa iyong AI agent. Tingnan natin ang ilan lamang sa mga iba't ibang bantang maaaring harapin ng AI agents at kung paano ka makakapaghanda at makakapagplano nang mas mabuti para dito.

![Understanding Threats](../../../translated_images/tl/understanding-threats.89edeada8a97fc0f.webp)

### Gawain at Tagubilin

**Paglalarawan:** Sinusubukan ng mga umaatake na baguhin ang mga tagubilin o layunin ng AI agent sa pamamagitan ng prompting o pagmamanipula ng mga input.

**Pagsugpo**: Isagawa ang mga validation check at input filter upang matukoy ang mga posibleng mapanganib na prompt bago ito maiproseso ng AI Agent. Dahil karaniwang nangangailangan ang mga atake na ito ng madalas na pakikipag-ugnayan sa Agent, ang paglilimita sa bilang ng pag-uusap ay isa pang paraan upang maiwasan ang ganitong uri ng atake.

### Access sa Mahahalagang Sistema

**Paglalarawan**: Kung ang AI agent ay may access sa mga sistema at serbisyo na nag-iimbak ng sensitibong data, maaaring ma-kompromiso ng mga umaatake ang komunikasyon sa pagitan ng agent at mga serbisyong ito. Maaari itong maging direktang atake o di-tuwirang pagtatangka na makakuha ng impormasyon tungkol sa mga sistemang ito sa pamamagitan ng agent.

**Pagsugpo**: Dapat magkaroon lamang ng access ang AI agents sa mga sistema kapag kinakailangan upang maiwasan ang ganitong uri ng atake. Ang komunikasyon sa pagitan ng agent at sistema ay dapat din na ligtas. Ang pagpapatupad ng authentication at access control ay isa pang paraan upang maprotektahan ang impormasyong ito.

### Pag-overload ng Resources at Serbisyo

**Paglalarawan:** Maaari gamit ng AI agents ang iba't ibang kasangkapan at serbisyo upang matapos ang mga gawain. Maaaring gamitin ito ng mga umaatake upang atakihin ang mga serbisyong ito sa pamamagitan ng pagpapadala ng mataas na dami ng mga kahilingan sa AI Agent, na maaaring magresulta sa mga pagkasira ng sistema o mataas na gastos.

**Pagsugpo:** Magpatupad ng mga polisiya upang limitahan ang bilang ng mga kahilingang maaaring gawin ng AI agent sa isang serbisyo. Ang paglilimita sa bilang ng pag-uusap at kahilingan sa iyong AI agent ay isa pang paraan upang pigilan ang ganitong uri ng atake.

### Pagkalason ng Knowledge Base

**Paglalarawan:** Ang uri ng atakeng ito ay hindi tuwirang inaatake ang AI agent kundi ang knowledge base at iba pang serbisyo na gagamitin ng AI agent. Maaari itong magsangkot ng pagkasira ng data o impormasyon na gagamitin ng AI agent upang matapos ang gawain, na magreresulta sa bias o hindi inaasahang tugon sa user.

**Pagsugpo:** Magpatupad ng regular na beripikasyon ng data na gagamitin ng AI agent sa workflow nito. Siguraduhing ligtas ang access sa data na ito at binabago lamang ng mga pinagkakatiwalaang tao upang maiwasan ang ganitong uri ng atake.

### Sunud-sunod na Mga Mali

**Paglalarawan:** Gumagamit ang AI agents ng iba't ibang kasangkapan at serbisyo upang matapos ang mga gawain. Ang mga error na dulot ng mga umaatake ay maaaring magdulot ng pagkasira ng iba pang mga sistemang konektado sa AI agent, kaya lumalala ang epekto ng atake at mas mahirap i-troubleshoot.

**Pagsugpo**: Isang paraan upang maiwasan ito ay ang pagpapatakbo ng AI Agent sa isang limitadong kapaligiran, tulad ng paggawa ng mga gawain sa isang Docker container, upang maiwasan ang direktang atake sa sistema. Ang paggawa ng fallback mechanisms at retry logic kapag may mga sistemang nagbigay ng error ay isa pang paraan upang maiwasan ang malawakang pagkasira ng sistema.

## Tao-sa-Loop (Human-in-the-Loop)

Isa pang epektibong paraan upang bumuo ng mapagkakatiwalaang sistema ng AI Agent ay ang paggamit ng Human-in-the-loop. Ito ay lumilikha ng daloy kung saan ang mga user ay maaaring magbigay ng feedback sa mga Agents habang tumatakbo ang proseso. Ang mga user ay epektibong gumaganap bilang mga agent sa isang multi-agent na sistema at sa pamamagitan ng pagbibigay ng pag-apruba o pagtigil sa proseso.

![Human in The Loop](../../../translated_images/tl/human-in-the-loop.5f0068a678f62f4f.webp)

Narito ang isang snippet ng code gamit ang Microsoft Agent Framework upang ipakita kung paano ipinatutupad ang konseptong ito:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Gumawa ng provider na may pag-apruba mula sa tao sa proseso
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Gumawa ng ahente na may hakbang ng pag-apruba mula sa tao
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Maaaring repasuhin at aprubahan ng gumagamit ang tugon
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Konklusyon

Ang pagtatayo ng mapagkakatiwalaang mga AI agents ay nangangailangan ng maingat na disenyo, matibay na mga hakbang sa seguridad, at patuloy na pag-uulit. Sa pamamagitan ng pagpapatupad ng mga istrukturadong sistema ng meta prompting, pag-unawa sa mga posibleng banta, at paggamit ng mga estratehiya sa pagsugpo, maaaring makalikha ang mga developer ng mga AI agents na ligtas at epektibo. Dagdag pa rito, ang pagsasama ng human-in-the-loop na pamamaraan ay nagsisiguro na nananatiling nakaayon ang AI agents sa pangangailangan ng user habang binabawasan ang mga panganib. Habang patuloy na umuunlad ang AI, ang pagpapanatili ng maagap na pananaw sa seguridad, privacy, at mga etikal na konsiderasyon ang susi upang mapalago ang tiwala at pagiging maaasahan ng mga AI-driven na sistema.

## Mga Halimbawa ng Code

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Demonstrasyon ng hakbang-hakbang ng meta-prompt system-message framework.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Mga pre-action approval gates, risk tiering, at audit logging para sa mapagkakatiwalaang mga agent.

### May Iba Ka Pang Mga Tanong Tungkol sa Pagtatayo ng Mapagkakatiwalaang AI Agents?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipagkita sa ibang mga nag-aaral, dumalo sa office hours at masagot ang iyong mga tanong tungkol sa AI Agents.

## Karagdagang Mga Sanggunian

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Pangkalahatang pananagutan sa AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Pagsusuri ng mga generative AI models at AI applications</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mga safety system messages</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Template para sa Pagsusuri ng Panganib</a>

## Nakaraang Aralin

[Agentic RAG](../05-agentic-rag/README.md)

## Susunod na Aralin

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->