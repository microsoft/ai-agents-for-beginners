[![Trustworthy AI Agents](../../../translated_images/tl/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(I-click ang larawan sa itaas upang mapanood ang video ng araling ito)_

# Pagtatayo ng Mapagkakatiwalaang AI Agents

## Panimula

Saklaw ng araling ito:

- Paano bumuo at mag-deploy ng ligtas at epektibong AI Agents
- Mahahalagang konsiderasyon sa seguridad kapag nagde-develop ng AI Agents.
- Paano mapanatili ang data at privacy ng gumagamit kapag nagde-develop ng AI Agents.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano:

- Tukuyin at bawasan ang mga panganib kapag lumilikha ng AI Agents.
- Magpatupad ng mga hakbang sa seguridad upang matiyak na maayos na pinamamahalaan ang data at access.
- Lumikha ng mga AI Agents na nagpapanatili ng data privacy at nagbibigay ng kalidad na karanasan sa gumagamit.

## Kaligtasan

Una, tingnan muna natin ang paggawa ng ligtas na agentic applications. Ang kaligtasan ay nangangahulugan na ang AI agent ay gumagana ayon sa disenyo. Bilang mga tagabuo ng agentic applications, mayroon tayong mga pamamaraan at kasangkapan upang mapahusay ang kaligtasan:

### Pagtatayo ng isang System Message Framework

Kung nakabuo ka na ng AI application gamit ang Large Language Models (LLMs), alam mo ang kahalagahan ng pagdidisenyo ng matibay na system prompt o system message. Ang mga prompt na ito ay nagtatakda ng mga meta rules, mga tagubilin, at mga patnubay kung paano makikipag-ugnayan ang LLM sa gumagamit at data.

Para sa AI Agents, mas mahalaga ang system prompt dahil kailangang magkaroon ang AI Agents ng napaka-tiyak na mga tagubilin upang matapos ang mga gawaing idinisenyo para sa kanila.

Upang makalikha ng scalable na mga system prompt, maaari nating gamitin ang isang system message framework para bumuo ng isa o higit pang mga agent sa ating aplikasyon:

![Building a System Message Framework](../../../translated_images/tl/system-message-framework.3a97368c92d11d68.webp)

#### Hakbang 1: Lumikha ng Meta System Message 

Ang meta prompt ay gagamitin ng isang LLM upang bumuo ng mga system prompts para sa mga agent na ating nilikha. Dinisenyo natin ito bilang template upang madali tayong makalikha ng maraming agent kung kinakailangan.

Narito ang isang halimbawa ng meta system message na ibibigay natin sa LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Hakbang 2: Lumikha ng pangunahing prompt

Ang susunod na hakbang ay gumawa ng pangunahing prompt upang ilarawan ang AI Agent. Dapat mong isama ang papel ng agent, mga gawain na tatapusin ng agent, at iba pang mga responsibilidad ng agent.

Narito ang halimbawa:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Hakbang 3: Ibigay ang Basic System Message sa LLM

Ngayon ay maaari nating i-optimize ang system message na ito sa pamamagitan ng pagbibigay ng meta system message bilang system message at ang ating basic system message.

Ito ay magreresulta sa system message na mas mahusay na dinisenyo upang gabayan ang ating mga AI agents:

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

#### Hakbang 4: Ulitin at Pagbutihin

Ang halaga ng system message framework na ito ay upang mas madaling mag-scale sa paggawa ng mga system message mula sa maraming agent pati na rin ang pagpapabuti ng iyong mga system message sa paglipas ng panahon. Bihira kang magkaroon ng system message na gumagana nang perpekto sa unang pagkakataon para sa iyong kumpletong kaso ng paggamit. Ang kakayahang gumawa ng maliliit na pag-aayos at pagpapahusay sa pamamagitan ng pagbabago ng basic system message at pagpapatakbo nito sa sistema ay magpapahintulot sa iyo na ihambing at suriin ang mga resulta.

## Pag-unawa sa mga Banta

Upang makabuo ng mapagkakatiwalaang AI agents, mahalagang maunawaan at mabawasan ang mga panganib at banta sa iyong AI agent. Tingnan natin ang ilan lamang sa iba't ibang mga banta sa AI agents at kung paano ka makakapaghanda at makakapagplano para dito.

![Understanding Threats](../../../translated_images/tl/understanding-threats.89edeada8a97fc0f.webp)

### Gawain at Tagubilin

**Paglalarawan:** Sinusubukan ng mga umaatake na baguhin ang mga tagubilin o layunin ng AI agent sa pamamagitan ng prompting o pagmamanipula ng mga input.

**Pagbawas**: Magsagawa ng validation checks at input filters upang matukoy ang mga posibleng mapanganib na prompt bago ito maproseso ng AI Agent. Dahil kadalasan, ang mga atakeng ito ay nangangailangan ng madalas na interaksyon sa Agent, ang paglilimita sa bilang ng mga turn sa isang pag-uusap ay isa pang paraan upang maiwasan ang ganitong uri ng mga atake.

### Access sa Mahahalagang Sistema

**Paglalarawan:** Kung ang AI agent ay may access sa mga sistema at serbisyo na nag-iimbak ng sensitibong data, maaaring sirain ng mga umaatake ang komunikasyon sa pagitan ng agent at ng mga serbisyong ito. Maaari itong maging direktang atake o di-direktang pagtatangkang makakuha ng impormasyon tungkol sa mga sistemang ito sa pamamagitan ng agent.

**Pagbawas:** Dapat limitado lamang ang access ng AI agents sa mga sistema batay sa pangangailangan upang maiwasan ang ganitong uri ng mga atake. Dapat din na secure ang komunikasyon sa pagitan ng agent at sistema. Ang pagpapatupad ng authentication at access control ay isa pang paraan upang protektahan ang impormasyong ito.

### Pag-overload ng Resource at Serbisyo

**Paglalarawan:** Maaaring mag-access ang AI agents ng iba't ibang tools at serbisyo upang matapos ang mga gawain. Maaari itong gamitin ng mga umaatake upang atakihin ang mga serbisyong ito sa pamamagitan ng pagpapadala ng mataas na bilang ng mga request sa AI Agent, na maaaring magdulot ng pagkabigo ng sistema o mataas na gastos.

**Pagbawas:** Magpatupad ng mga polisiya upang limitahan ang bilang ng mga request na maaaring gawin ng isang AI agent sa isang serbisyo. Ang paglilimita rin ng bilang ng pag-uusap at mga request sa iyong AI agent ay isa pang paraan upang maiwasan ang ganitong uri ng mga atake.

### Pagkalason sa Knowledge Base

**Paglalarawan:** Ang uri ng atakeng ito ay hindi direktang tinatarget ang AI agent ngunit ang knowledge base at iba pang mga serbisyo na gagamitin ng AI agent. Maaaring kabilang dito ang paninira sa data o impormasyon na gagamitin ng AI agent upang matapos ang gawain, na nagreresulta sa biased o hindi inaasahang mga tugon sa gumagamit.

**Pagbawas:** Regular na beripikahin ang data na gagamitin ng AI agent sa kanyang mga workflow. Siguraduhin na secure ang access sa data na ito at tanging mga pinagkakatiwalaang indibidwal lamang ang maaaring magbago nito upang maiwasan ang ganitong uri ng atake.

### Sunud-sunod na Mga Error

**Paglalarawan:** Nag-a-access ang AI agents ng iba't ibang tools at serbisyo upang matapos ang mga gawain. Ang mga error na sanhi ng mga umaatake ay maaaring magdulot ng pagkabigo sa iba pang mga sistemang konektado sa AI agent, na nagpapalawak ng epekto ng atake at nagpapahirap sa pag-troubleshoot.

**Pagbawas:** Isang paraan upang maiwasan ito ay ang pagpapatakbo ng AI Agent sa isang limitadong kapaligiran, tulad ng pagsasagawa ng mga gawain sa isang Docker container, upang maiwasan ang direktang atake sa sistema. Ang paggawa ng mga fallback mechanisms at retry logic kapag may mga sistemang nagreresponde ng error ay isa pang paraan upang maiwasan ang mas malalaking pagkabigo sa sistema.

## Human-in-the-Loop

Isa pang epektibong paraan upang makabuo ng mapagkakatiwalaang AI Agent system ay ang paggamit ng Human-in-the-loop. Lumilikha ito ng daloy kung saan ang mga gumagamit ay maaaring magbigay ng feedback sa mga Agent habang tumatakbo ang proseso. Ang mga gumagamit ay kumikilos bilang mga agent sa isang multi-agent system sa pamamagitan ng pagbibigay ng pag-apruba o pag-terminate ng tumatakbong proseso.

![Human in The Loop](../../../translated_images/tl/human-in-the-loop.5f0068a678f62f4f.webp)

Narito ang isang code snippet gamit ang Microsoft Agent Framework upang ipakita kung paano ipinatutupad ang konseptong ito:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Lumikha ng provider na may aprub ng tao sa proseso
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Lumikha ng ahente na may hakbang ng aprub ng tao
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Maaaring suriin at aprubahan ng gumagamit ang tugon
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Konklusyon

Ang pagbubuo ng mapagkakatiwalaang AI agents ay nangangailangan ng maingat na disenyo, matibay na mga hakbang sa seguridad, at tuloy-tuloy na iterasyon. Sa pamamagitan ng pagpapatupad ng mga istrukturadong meta prompting system, pag-unawa sa mga posibleng banta, at paggamit ng mga estratehiya sa pagbawas, makakalikha ang mga developer ng AI agents na ligtas at epektibo. Bukod dito, ang pagsasama ng human-in-the-loop na pamamaraan ay nagsisiguro na ang mga AI agents ay nananatiling nakaayon sa mga pangangailangan ng gumagamit habang pinapaliit ang mga panganib. Habang patuloy na umuunlad ang AI, ang pagpapanatili ng isang maagap na posisyon sa seguridad, privacy, at mga etikal na konsiderasyon ay magiging susi sa pagtataguyod ng tiwala at pagiging maaasahan sa mga AI-driven na sistema.

### May Karagdagang Mga Tanong tungkol sa Pagtatayo ng Mapagkakatiwalaang AI Agents?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa iba pang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

## Karagdagang Mga Mapagkukunan

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Pangkalahatang-ideya ng Responsible AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Pagsusuri ng mga modelong generative AI at AI applications</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mga safety system messages</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Template para sa Risk Assessment</a>

## Nakaraang Aralin

[Agentic RAG](../05-agentic-rag/README.md)

## Susunod na Aralin

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI na serbisyo sa pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa kawastuhan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga error o di-tumpak na bahagi. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pangunahing pinagmulan. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling pagpapakahulugan na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->