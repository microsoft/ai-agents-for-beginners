<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T09:47:04+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "tl"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.tl.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(I-click ang imahe sa itaas upang mapanood ang video ng araling ito)_

# Paggawa ng Mapagkakatiwalaang AI Agents

## Panimula

Ang araling ito ay tatalakayin ang:

- Paano gumawa at mag-deploy ng ligtas at epektibong AI Agents
- Mahahalagang konsiderasyon sa seguridad kapag gumagawa ng AI Agents.
- Paano mapanatili ang privacy ng data at user sa paggawa ng AI Agents.

## Mga Layunin sa Pag-aaral

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano:

- Tukuyin at bawasan ang mga panganib sa paggawa ng AI Agents.
- Magpatupad ng mga hakbang sa seguridad upang masiguro na ang data at access ay maayos na pinamamahalaan.
- Gumawa ng AI Agents na pinapanatili ang privacy ng data at nagbibigay ng de-kalidad na karanasan sa user.

## Kaligtasan

Unahin nating talakayin ang paggawa ng ligtas na agentic applications. Ang kaligtasan ay nangangahulugan na ang AI agent ay gumagana ayon sa disenyo. Bilang mga tagalikha ng agentic applications, mayroon tayong mga pamamaraan at tools upang mapataas ang kaligtasan:

### Paggawa ng Framework para sa System Message

Kung nakagawa ka na ng AI application gamit ang Large Language Models (LLMs), alam mo ang kahalagahan ng pagdisenyo ng matibay na system prompt o system message. Ang mga prompt na ito ang nagtatakda ng mga meta rules, instruksyon, at gabay kung paano makikipag-ugnayan ang LLM sa user at data.

Para sa AI Agents, mas mahalaga ang system prompt dahil kailangan ng AI Agents ng napaka-espesipikong instruksyon upang maisagawa ang mga gawain na idinisenyo para sa kanila.

Upang makagawa ng scalable na system prompts, maaari tayong gumamit ng system message framework para sa paggawa ng isa o higit pang agents sa ating application:

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.tl.png)

#### Hakbang 1: Gumawa ng Meta System Message

Ang meta prompt ay gagamitin ng LLM upang makabuo ng system prompts para sa mga agents na ating gagawin. Dinisenyo natin ito bilang template upang mas madali tayong makagawa ng maraming agents kung kinakailangan.

Narito ang halimbawa ng meta system message na ibibigay natin sa LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Hakbang 2: Gumawa ng Basic Prompt

Ang susunod na hakbang ay gumawa ng basic prompt upang ilarawan ang AI Agent. Dapat mong isama ang papel ng agent, ang mga gawain na gagawin ng agent, at iba pang responsibilidad ng agent.

Narito ang halimbawa:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Hakbang 3: Ibigay ang Basic System Message sa LLM

Ngayon, maaari nating i-optimize ang system message sa pamamagitan ng pagbibigay ng meta system message bilang system message at ang ating basic system message.

Ito ay magbubunga ng system message na mas angkop para sa paggabay sa ating AI agents:

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

Ang halaga ng system message framework na ito ay ang kakayahang gawing mas madali ang paggawa ng system messages para sa maraming agents pati na rin ang pagpapabuti ng iyong system messages sa paglipas ng panahon. Bihira kang magkaroon ng system message na gumagana agad para sa buong use case. Ang kakayahang gumawa ng maliliit na pagbabago at pagpapabuti sa pamamagitan ng pagbabago ng basic system message at pagtakbo nito sa system ay magpapahintulot sa iyo na ihambing at suriin ang mga resulta.

## Pag-unawa sa Mga Banta

Upang makagawa ng mapagkakatiwalaang AI agents, mahalagang maunawaan at mabawasan ang mga panganib at banta sa iyong AI agent. Tingnan natin ang ilan sa iba't ibang banta sa AI agents at kung paano mo mas mahusay na mapaplano at maihahanda ang mga ito.

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.tl.png)

### Gawain at Instruksyon

**Paglalarawan:** Sinusubukan ng mga attacker na baguhin ang mga instruksyon o layunin ng AI agent sa pamamagitan ng prompting o pagmamanipula ng mga input.

**Pag-iwas:** Magpatupad ng validation checks at input filters upang matukoy ang mga potensyal na mapanganib na prompt bago ito iproseso ng AI Agent. Dahil ang mga ganitong uri ng pag-atake ay karaniwang nangangailangan ng madalas na pakikipag-ugnayan sa Agent, ang paglilimita sa bilang ng mga turn sa isang pag-uusap ay isa pang paraan upang maiwasan ang mga ganitong uri ng pag-atake.

### Access sa Mahahalagang Sistema

**Paglalarawan:** Kung ang AI agent ay may access sa mga sistema at serbisyo na nagtatago ng sensitibong data, maaaring ma-kompromiso ng mga attacker ang komunikasyon sa pagitan ng agent at ng mga serbisyong ito. Maaaring direktang pag-atake o hindi direktang pagtatangka upang makakuha ng impormasyon tungkol sa mga sistemang ito sa pamamagitan ng agent.

**Pag-iwas:** Ang AI agents ay dapat magkaroon ng access sa mga sistema batay lamang sa pangangailangan upang maiwasan ang mga ganitong uri ng pag-atake. Ang komunikasyon sa pagitan ng agent at sistema ay dapat ding maging secure. Ang pagpapatupad ng authentication at access control ay isa pang paraan upang maprotektahan ang impormasyong ito.

### Pag-overload ng Resources at Serbisyo

**Paglalarawan:** Ang AI agents ay maaaring mag-access ng iba't ibang tools at serbisyo upang maisagawa ang mga gawain. Maaaring gamitin ng mga attacker ang kakayahang ito upang atakihin ang mga serbisyong ito sa pamamagitan ng pagpapadala ng mataas na dami ng mga request sa pamamagitan ng AI Agent, na maaaring magresulta sa pagkabigo ng sistema o mataas na gastos.

**Pag-iwas:** Magpatupad ng mga polisiya upang limitahan ang bilang ng mga request na maaaring gawin ng AI agent sa isang serbisyo. Ang paglilimita sa bilang ng mga turn ng pag-uusap at mga request sa iyong AI agent ay isa pang paraan upang maiwasan ang mga ganitong uri ng pag-atake.

### Pagkalason ng Knowledge Base

**Paglalarawan:** Ang ganitong uri ng pag-atake ay hindi direktang tina-target ang AI agent ngunit tina-target ang knowledge base at iba pang serbisyo na gagamitin ng AI agent. Maaaring kabilang dito ang pagkasira ng data o impormasyon na gagamitin ng AI agent upang maisagawa ang isang gawain, na nagreresulta sa biased o hindi inaasahang tugon sa user.

**Pag-iwas:** Magsagawa ng regular na beripikasyon ng data na gagamitin ng AI agent sa mga workflow nito. Siguraduhin na ang access sa data na ito ay secure at mababago lamang ng mga pinagkakatiwalaang indibidwal upang maiwasan ang ganitong uri ng pag-atake.

### Pagkakasunod-sunod ng Error

**Paglalarawan:** Ang AI agents ay nag-a-access ng iba't ibang tools at serbisyo upang maisagawa ang mga gawain. Ang mga error na dulot ng mga attacker ay maaaring magresulta sa pagkabigo ng iba pang mga sistema na konektado sa AI agent, na nagiging sanhi ng pagkalat ng pag-atake at mas mahirap i-troubleshoot.

**Pag-iwas:** Isang paraan upang maiwasan ito ay ang pagpapatakbo ng AI Agent sa isang limitadong kapaligiran, tulad ng pagsasagawa ng mga gawain sa isang Docker container, upang maiwasan ang direktang pag-atake sa sistema. Ang paggawa ng fallback mechanisms at retry logic kapag ang ilang mga sistema ay tumugon ng error ay isa pang paraan upang maiwasan ang mas malawak na pagkabigo ng sistema.

## Human-in-the-Loop

Isa pang epektibong paraan upang makagawa ng mapagkakatiwalaang AI Agent systems ay ang paggamit ng Human-in-the-loop. Ito ay lumilikha ng daloy kung saan ang mga user ay maaaring magbigay ng feedback sa Agents habang tumatakbo ang proseso. Ang mga user ay kumikilos bilang mga agent sa isang multi-agent system at nagbibigay ng pag-apruba o pagwawakas ng tumatakbong proseso.

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.tl.png)

Narito ang isang code snippet gamit ang AutoGen upang ipakita kung paano ipinatutupad ang konseptong ito:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Konklusyon

Ang paggawa ng mapagkakatiwalaang AI agents ay nangangailangan ng maingat na disenyo, matibay na hakbang sa seguridad, at patuloy na pag-ulit. Sa pamamagitan ng pagpapatupad ng mga structured meta prompting systems, pag-unawa sa mga potensyal na banta, at paggamit ng mga estratehiya sa pag-iwas, maaaring makagawa ang mga developer ng AI agents na ligtas at epektibo. Bukod dito, ang pagsasama ng human-in-the-loop na approach ay nagsisiguro na ang AI agents ay nananatiling naaayon sa pangangailangan ng user habang binabawasan ang mga panganib. Habang patuloy na umuunlad ang AI, ang pagpapanatili ng proaktibong pananaw sa seguridad, privacy, at etikal na konsiderasyon ay magiging susi sa pagpapalaganap ng tiwala at pagiging maaasahan sa mga AI-driven na sistema.

### May Karagdagang Tanong Tungkol sa Paggawa ng Mapagkakatiwalaang AI Agents?

Sumali sa [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagtagpo sa ibang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

## Karagdagang Resources

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Responsible AI overview</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluation of generative AI models and AI applications</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Safety system messages</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Risk Assessment Template</a>

## Nakaraang Aralin

[Agentic RAG](../05-agentic-rag/README.md)

## Susunod na Aralin

[Planning Design Pattern](../07-planning-design/README.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.