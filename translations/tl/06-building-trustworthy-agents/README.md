[![Trustworthy AI Agents](../../../translated_images/tl/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(I-click ang larawan sa itaas upang panoorin ang video ng leksyon na ito)_

# Pagbuo ng Mapagkakatiwalaang AI Agents

## Panimula

Tatalakayin sa leksyong ito:

- Paano bumuo at mag-deploy ng ligtas at epektibong AI Agents
- Mahahalagang konsiderasyon sa seguridad kapag nagde-develop ng AI Agents.
- Paano panatilihin ang privacy ng data at ng user sa pagbuo ng AI Agents.

## Mga Layunin sa Pagkatuto

Pagkatapos matapos ang leksyong ito, malalaman mo kung paano:

- Kilalanin at mabawasan ang mga panganib kapag lumilikha ng AI Agents.
- Magpatupad ng mga hakbang sa seguridad upang matiyak na ang data at access ay wastong pinamamahalaan.
- Lumikha ng AI Agents na nagpapanatili ng privacy ng data at nagbibigay ng de-kalidad na karanasan sa user.

## Kaligtasan

Unahin nating tingnan ang pagbuo ng ligtas na agentic applications. Ang kaligtasan ay nangangahulugang ang AI agent ay gumagana ayon sa disenyo nito. Bilang mga tagabuo ng agentic applications, may mga pamamaraan at kagamitan tayo upang mapalaki ang kaligtasan:

### Pagbuo ng Isang System Message Framework

Kung nakabuo ka na ng AI application gamit ang Large Language Models (LLMs), alam mo ang kahalagahan ng pagdisenyo ng matibay na system prompt o system message. Ang mga prompt na ito ang nagtatakda ng meta rules, mga instruksiyon, at mga gabay kung paano makikipag-ugnayan ang LLM sa user at data.

Para sa AI Agents, mas mahalaga ang system prompt dahil kailangan ng AI Agents ng napaka-tiyak na mga instruksiyon upang makumpleto ang mga gawain na idinisenyo natin para sa kanila.

Para makalikha ng scalable na mga system prompt, maaari tayong gumamit ng system message framework para magbuo ng isa o higit pang mga agent sa ating aplikasyon:

![Building a System Message Framework](../../../translated_images/tl/system-message-framework.3a97368c92d11d68.webp)

#### Hakbang 1: Gumawa ng Meta System Message

Ang meta prompt ay gagamitin ng isang LLM upang bumuo ng mga system prompt para sa mga agent na lilikhain natin. Dinisenyo natin ito bilang isang template upang epektibong makalikha ng maraming agent kung kinakailangan.

Narito ang isang halimbawa ng meta system message na ibibigay natin sa LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Hakbang 2: Gumawa ng basic prompt

Ang susunod na hakbang ay gumawa ng basic prompt upang ilarawan ang AI Agent. Dapat mong isama ang papel ng agent, ang mga gawain na tatapusin ng agent, at iba pang mga responsibilidad ng agent.

Narito ang isang halimbawa:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Hakbang 3: Ibigay ang Basic System Message sa LLM

Ngayon ay maaari nating i-optimize ang system message na ito sa pamamagitan ng pagbibigay ng meta system message bilang system message pati na rin ang basic system message natin.

Ito ay maglilikha ng isang system message na mas mahusay na idinisenyo para gabayan ang ating mga AI agents:

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

Ang kahalagahan ng system message framework na ito ay upang mapadali ang pag-scale ng paggawa ng mga system message mula sa maraming agent pati na rin ang pagpapabuti ng iyong mga system message sa paglipas ng panahon. Bihira kang magkaroon ng system message na gumagana agad sa unang beses para sa iyong buong use case. Ang kakayahang gumawa ng maliliit na tweaks at pagpapabuti sa pamamagitan ng pagbabago ng basic system message at pagpapatakbo nito sa system ay magbibigay-daan sa iyo upang ihambing at suriin ang mga resulta.

## Pag-unawa sa Mga Banta

Para makabuo ng mapagkakatiwalaang AI agents, mahalagang maunawaan at mabawasan ang mga panganib at banta sa iyong AI agent. Tignan natin ang ilan lamang sa mga iba't ibang banta sa AI agents at kung paano ka makakapaghanda at makakapagplano para sa mga ito.

![Understanding Threats](../../../translated_images/tl/understanding-threats.89edeada8a97fc0f.webp)

### Gawain at Instruksiyon

**Paglalarawan:** Sinusubukan ng mga umaatake na baguhin ang mga instruksiyon o layunin ng AI agent sa pamamagitan ng prompting o pagmamanipula ng mga input.

**Pagsugpo**: Isagawa ang mga validation checks at input filters upang matuklasan ang mga posibleng mapanganib na prompt bago ito iproseso ng AI Agent. Dahil ang mga atakeng ito ay karaniwang nangangailangan ng madalas na interaksyon sa Agent, ang pag-limit ng bilang ng mga turno ng usapan ay isa pang paraan upang pigilan ang mga ganitong uri ng atake.

### Access sa Mahalagang Sistema

**Paglalarawan**: Kung ang AI agent ay may access sa mga sistema at serbisyo na naglalaman ng sensitibong data, maaaring ma-kompromiso ng mga umaatake ang komunikasyon sa pagitan ng agent at ng mga serbisyong ito. Maaaring ito ay mga direktang atake o di-tuwirang pagtatangka upang makakuha ng impormasyon tungkol sa mga sistemang ito sa pamamagitan ng agent.

**Pagsugpo**: Dapat ang mga AI agent ay may access sa mga sistema ayon lamang sa pangangailangan upang maiwasan ang ganitong uri ng mga atake. Ang komunikasyon sa pagitan ng agent at sistema ay dapat ding ligtas. Ang pagpapatupad ng authentication at access control ay isa pang paraan upang protektahan ang impormasyong ito.

### Pag-overload ng Resource at Serbisyo

**Paglalarawan:** Maaaring ma-access ng mga AI agents ang iba't ibang kasangkapan at serbisyo upang tapusin ang mga gawain. Maaaring gamitin ng mga umaatake ang kakayahang ito upang atakihin ang mga serbisyong ito sa pamamagitan ng pagpapadala ng mataas na bilang ng mga kahilingan sa pamamagitan ng AI Agent, na maaaring magresulta sa pagkabigo ng sistema o mataas na gastos.

**Pagsugpo:** Magpatupad ng mga polisiya upang limitahan ang bilang ng mga kahilingang magagawa ng AI agent sa isang serbisyo. Ang pag-limit ng bilang ng mga turno sa usapan at kahilingan sa iyong AI agent ay isa pang paraan upang maiwasan ang ganitong klase ng mga atake.

### Pagkalason ng Knowledge Base

**Paglalarawan:** Ang ganitong uri ng atake ay hindi direktang target ang AI agent kundi ang knowledge base at iba pang serbisyo na gagamitin ng AI agent. Maaaring ito ay pagsira o pagkasira ng data o impormasyon na gagamitin ng AI agent upang tapusin ang isang gawain, na nagreresulta sa may pagkiling o hindi inaasahang tugon sa user.

**Pagsugpo:** Gumawa ng regular na beripikasyon ng data na gagamitin ng AI agent sa mga workflows nito. Tiyakin na ang access sa data na ito ay ligtas at tanging mga pinagkakatiwalaang tao lamang ang makakapagbago nito upang maiwasan ang ganitong uri ng atake.

### Pagkakasunod-sunod ng mga Error

**Paglalarawan:** Ang mga AI agents ay kumokonekta sa iba't ibang kasangkapan at serbisyo upang tapusin ang mga gawain. Ang mga pagkakamaling sanhi ng mga umaatake ay maaaring magdulot ng pagkabigo sa iba pang sistema na konektado sa AI agent, na nagpapalawak ng saklaw ng atake at nagpapahirap sa paglutas ng problema.

**Pagsugpo**: Isang paraan upang maiwasan ito ay ang pagpapatakbo ng AI Agent sa isang limitadong kapaligiran, tulad ng pagsasagawa ng mga gawain sa loob ng Docker container, upang mapigilan ang direktang pag-atake sa sistema. Ang paggawa ng fallback mechanisms at retry logic kapag ang ilang sistema ay nagbigay ng error ay isa pang paraan upang maiwasan ang mas malaking pagkabigo ng sistema.

## Human-in-the-Loop

Isa pang epektibong paraan upang bumuo ng mapagkakatiwalaang mga AI Agent system ay ang paggamit ng Human-in-the-loop. Lumilikha ito ng daloy kung saan ang mga user ay maaaring magbigay ng feedback sa mga Agent habang tumatakbo ang proseso. Ang mga user ay kumikilos bilang mga agent sa isang multi-agent system sa pamamagitan ng pagbibigay ng aprubal o pagtigil sa tumatakbong proseso.

![Human in The Loop](../../../translated_images/tl/human-in-the-loop.5f0068a678f62f4f.webp)

Narito ang isang code snippet gamit ang Microsoft Agent Framework upang ipakita kung paano naipapatupad ang konseptong ito:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Gumawa ng provider na may aprub ng tao sa proseso
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Gumawa ng agent na may hakbang ng aprub ng tao
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

Ang pagbuo ng mapagkakatiwalaang AI agents ay nangangailangan ng maingat na disenyo, matibay na hakbang sa seguridad, at tuloy-tuloy na pag-uulit. Sa pamamagitan ng pagpapatupad ng mga sistematikong meta prompting, pag-unawa sa mga potensyal na banta, at paggamit ng mga estratehiya sa pagsugpo, maaaring makalikha ang mga developer ng AI agents na parehong ligtas at epektibo. Bukod pa rito, ang pagsasama ng human-in-the-loop na pamamaraan ay nagsisiguro na ang mga AI agent ay nananatiling naaayon sa pangangailangan ng user habang pinapaliit ang mga panganib. Habang patuloy na umuunlad ang AI, ang pagpapanatili ng maagap na pananaw sa seguridad, privacy, at etikal na mga konsiderasyon ay magiging susi sa pagtataguyod ng tiwala at pagiging maaasahan sa mga sistemang pinapagana ng AI.

## Mga Halimbawang Code

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Isang hakbang-hakbang na demonstrasyon ng meta-prompt system-message framework.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Mga pre-action approval gates, risk tiering, at audit logging para sa mga mapagkakatiwalaang agent.

### May Karagdagang Mga Tanong Tungkol sa Pagbuo ng Mapagkakatiwalaang AI Agents?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa iba pang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

## Karagdagang Mga Mapagkukunan

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Pangkalahatang-ideya ng Responsible AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Pagsusuri ng mga generative AI model at AI application</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mga safety system message</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Template para sa Risk Assessment</a>

## Nakaraang Leksiyon

[Agentic RAG](../05-agentic-rag/README.md)

## Susunod na Leksiyon

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->