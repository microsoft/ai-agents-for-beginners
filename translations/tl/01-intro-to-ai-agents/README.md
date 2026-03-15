[![Panimula sa mga AI Agent](../../../translated_images/tl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_


# Panimula sa mga AI Agent at Mga Gamit ng Ahente

Maligayang pagdating sa kursong "AI Agents for Beginners"! Nagbibigay ang kursong ito ng pangunahing kaalaman at mga halimbawa ng aplikasyon para sa pagbuo ng mga AI Agent.

Sumali sa <a href="https://discord.gg/kzRShWzttr" target="_blank">Komunidad ng Azure AI sa Discord</a> upang makilala ang iba pang mga nag-aaral at mga Tagabuo ng AI Agent at magtanong ng anumang mga katanungan na mayroon ka tungkol sa kursong ito.

Upang simulan ang kursong ito, sisimulan natin sa pagkuha ng mas mabuting pag-unawa sa kung ano ang mga AI Agent at kung paano natin sila magagamit sa mga aplikasyon at workflow na binubuo natin.

## Panimula

Tinalakay sa araling ito:

- Ano ang mga AI Agent at ano ang iba't ibang uri ng mga ahente?
- Anong mga use case ang pinakaangkop para sa mga AI Agent at paano sila makakatulong sa atin?
- Ano ang ilan sa mga pangunahing sangkap kapag nagdidisenyo ng Mga Solusyong Ahente?

## Mga Layunin sa Pagkatuto
Matapos makumpleto ang araling ito, dapat mong magawa ang mga sumusunod:

- Maunawaan ang mga konsepto ng AI Agent at kung paano sila naiiba mula sa ibang mga solusyon ng AI.
- Magamit ang mga AI Agent nang pinakaepektibo.
- Magdisenyo ng mga solusyon na ahente nang produktibo para sa parehong mga gumagamit at mga customer.

## Paglilinaw sa AI Agent at Mga Uri ng AI Agent

### Ano ang mga AI Agent?

Ang mga AI Agent ay **mga sistema** na nagpapahintulot sa **Malalaking Modelong Pangwika(LLMs)** na **magsagawa ng mga aksyon** sa pamamagitan ng pagpapalawak ng kanilang kakayahan sa pagbibigay sa mga LLM ng **access sa mga kasangkapan** at **kaalaman**.

Hatiin natin ang depinisyon na ito sa mas maliliit na bahagi:

- **Sistema** - Mahalaga na isipin ang mga ahente hindi lamang bilang isang component kundi bilang isang sistema ng maraming bahagi. Sa pinakamababang antas, ang mga bahagi ng isang AI Agent ay:
  - **Kapaligiran** - Ang tinukoy na espasyo kung saan gumagana ang AI Agent. Halimbawa, kung mayroon tayong isang travel booking AI Agent, ang kapaligiran ay maaaring ang travel booking system na ginagamit ng AI Agent upang kumpletuhin ang mga gawain.
  - **Sensor** - Ang mga kapaligiran ay may impormasyon at nagbibigay ng feedback. Ginagamit ng mga AI Agent ang mga sensor upang mangalap at mag-interpret ng impormasyong ito tungkol sa kasalukuyang estado ng kapaligiran. Sa halimbawa ng Travel Booking Agent, ang travel booking system ay maaaring magbigay ng impormasyon tulad ng availability ng hotel o presyo ng mga flight.
  - **Actuator** - Kapag natanggap na ng AI Agent ang kasalukuyang estado ng kapaligiran, para sa kasalukuyang gawain tinutukoy ng agent kung anong aksyon ang gagawin upang baguhin ang kapaligiran. Para sa travel booking agent, maaaring ito ay mag-book ng isang available na kwarto para sa gumagamit.

![Ano ang mga AI Agent?](../../../translated_images/tl/what-are-ai-agents.1ec8c4d548af601a.webp)

**Malalaking Modelong Pangwika** - Umiiral na ang konsepto ng mga ahente bago pa malikha ang mga LLM. Ang bentahe ng pagbuo ng mga AI Agent gamit ang LLMs ay ang kanilang kakayahang mag-interpret ng wikang pantao at datos. Ang kakayahang ito ay nagpapahintulot sa mga LLM na mag-interpret ng impormasyon ng kapaligiran at magtakda ng plano upang baguhin ang kapaligiran.

**Magsagawa ng Mga Aksyon** - Sa labas ng mga sistema ng AI Agent, limitado ang mga LLM sa mga sitwasyon kung saan ang aksyon ay ang pagbuo ng nilalaman o impormasyon batay sa prompt ng gumagamit. Sa loob ng mga sistema ng AI Agent, maaaring makamit ng mga LLM ang mga gawain sa pamamagitan ng pag-interpret ng kahilingan ng gumagamit at paggamit ng mga kasangkapan na magagamit sa kanilang kapaligiran.

**Access sa Mga Kasangkapan** - Ang mga kasangkapang maa-access ng LLM ay tinutukoy ng 1) ang kapaligiran kung saan ito gumagana at 2) ang developer ng AI Agent. Para sa halimbawa ng travel agent namin, ang mga kasangkapan ng agent ay limitado ng mga operasyon na magagamit sa booking system, at/o maaaring limitahan ng developer ang access ng agent sa mga kasangkapan para sa mga flight.

**Memorya+Kaalaman** - Ang memorya ay maaaring panandalian sa konteksto ng usapan sa pagitan ng gumagamit at ng agent. Pangmatagalan, sa labas ng impormasyong ibinigay ng kapaligiran, maaari ding kumuha ang mga AI Agent ng kaalaman mula sa ibang mga sistema, serbisyo, kasangkapan, at maging mula sa ibang mga ahente. Sa halimbawa ng travel agent, ang kaalamang ito ay maaaring ang impormasyon tungkol sa mga kagustuhan sa paglalakbay ng gumagamit na nasa isang customer database.

### Iba't ibang uri ng mga ahente

Ngayon na mayroon tayong pangkalahatang depinisyon ng AI Agent, tingnan natin ang ilang mga partikular na uri ng ahente at kung paano sila iaaplay sa isang travel booking AI agent.

| **Agent Type**                | **Description**                                                                                                                       | **Example**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Simple Reflex Agents**      | Perform immediate actions based on predefined rules.                                                                                  | Travel agent interprets the context of the email and forwards travel complaints to customer service.                                                                                                                          |
| **Model-Based Reflex Agents** | Perform actions based on a model of the world and changes to that model.                                                              | Travel agent prioritizes routes with significant price changes based on access to historical pricing data.                                                                                                             |
| **Goal-Based Agents**         | Create plans to achieve specific goals by interpreting the goal and determining actions to reach it.                                  | Travel agent books a journey by determining necessary travel arrangements (car, public transit, flights) from the current location to the destination.                                                                                |
| **Utility-Based Agents**      | Consider preferences and weigh tradeoffs numerically to determine how to achieve goals.                                               | Travel agent maximizes utility by weighing convenience vs. cost when booking travel.                                                                                                                                          |
| **Learning Agents**           | Improve over time by responding to feedback and adjusting actions accordingly.                                                        | Travel agent improves by using customer feedback from post-trip surveys to make adjustments to future bookings.                                                                                                               |
| **Hierarchical Agents**       | Feature multiple agents in a tiered system, with higher-level agents breaking tasks into subtasks for lower-level agents to complete. | Travel agent cancels a trip by dividing the task into subtasks (for example, canceling specific bookings) and having lower-level agents complete them, reporting back to the higher-level agent.                                     |
| **Multi-Agent Systems (MAS)** | Agents complete tasks independently, either cooperatively or competitively.                                                           | Cooperative: Multiple agents book specific travel services such as hotels, flights, and entertainment. Competitive: Multiple agents manage and compete over a shared hotel booking calendar to book customers into the hotel. |

## Kailan Gagamitin ang mga AI Agent

Sa naunang seksyon, ginamit namin ang use-case ng Travel Agent upang ipaliwanag kung paano magagamit ang iba't ibang uri ng mga ahente sa iba't ibang senaryo ng travel booking. Patuloy nating gagamitin ang aplikasyon na ito sa buong kurso.

Tingnan natin ang mga uri ng use case na pinakaangkop sa paggamit ng mga AI Agent:

![Kailan gagamitin ang mga AI Agent?](../../../translated_images/tl/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Mga Bukas na Problema** - pinapahintulutan ang LLM na tukuyin ang mga kinakailangang hakbang upang kumpletuhin ang isang gawain dahil hindi palaging maaaring i-hardcode ang mga ito sa isang workflow.
- **Mga Proseso na May Maramihang Hakbang** - mga gawain na nangangailangan ng antas ng komplikasyon kung saan kailangang gumamit ang AI Agent ng mga kasangkapan o impormasyon sa maraming pag-ikot sa halip na isang beses na retrieval.  
- **Pagbuti sa Paglipas ng Panahon** - mga gawain kung saan maaaring mag-improve ang agent sa paglipas ng panahon sa pamamagitan ng pagtanggap ng feedback mula sa kapaligiran o mga gumagamit upang magbigay ng mas mahusay na utility.

Tinutukoy namin ang higit pang mga konsiderasyon sa paggamit ng mga AI Agent sa araling Building Trustworthy AI Agents.

## Mga Pangunahing Kaalaman sa Mga Solusyong Ahente

### Pagbuo ng Ahente

Ang unang hakbang sa pagdidisenyo ng isang sistema ng AI Agent ay tukuyin ang mga kasangkapan, aksyon, at mga pag-uugali. Sa kursong ito, nakatuon kami sa paggamit ng **Azure AI Agent Service** upang tukuyin ang aming mga Ahente. Nag-aalok ito ng mga tampok tulad ng:

- Selection of Open Models such as OpenAI, Mistral, and Llama
- Use of Licensed Data through providers such as Tripadvisor
- Use of standardized OpenAPI 3.0 tools

### Mga Pattern ng Ahente

Ang komunikasyon sa mga LLM ay sa pamamagitan ng prompts. Dahil sa semi-autonomous na katangian ng mga AI Agent, hindi palaging posible o kinakailangan na manu-manong i-reprompt ang LLM pagkatapos ng pagbabago sa kapaligiran. Gumagamit tayo ng **Mga Pattern ng Ahente** na nagpapahintulot sa atin na i-prompt ang LLM sa maraming hakbang sa isang mas scalable na paraan.

Hinirati ang kursong ito sa ilang mga kasalukuyang popular na Mga Pattern ng Ahente.

### Mga Balangkas ng Ahente

Pinahihintulutan ng Mga Balangkas ng Ahente ang mga developer na ipatupad ang mga pattern ng ahente sa pamamagitan ng code. Nag-aalok ang mga balangkas na ito ng mga template, plugin, at mga kasangkapan para sa mas mahusay na kolaborasyon ng AI Agent. Ang mga benepisyo na ito ay nagbibigay ng kakayahan para sa mas mahusay na observability at troubleshooting ng mga sistema ng AI Agent.

Sa kursong ito, susuriin natin ang Microsoft Agent Framework (MAF) para sa pagbuo ng mga production-ready na AI agent.

## Mga Halimbawang Kodigo

- Python: [Balangkas ng Ahente](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Balangkas ng Ahente](./code_samples/01-dotnet-agent-framework.md)

## May Karagdagang Tanong tungkol sa mga AI Agent?

Sumali sa [Discord ng Microsoft Foundry](https://aka.ms/ai-agents/discord) upang makipagkita sa ibang mga nag-aaral, dumalo sa office hours at masagot ang iyong mga tanong tungkol sa mga AI Agent.

## Nakaraang Aralin

[Pagsasaayos ng Kurso](../00-course-setup/README.md)

## Susunod na Aralin

[Pagtuklas sa Mga Balangkas ng Ahente](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Paunawa:
Ang dokumentong ito ay isinalin gamit ang serbisyong pagsasalin na pinapagana ng AI na Co-op Translator (https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpak. Dapat ituring na awtoritatibong pinagmulan ang orihinal na dokumento sa orihinal nitong wika. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng isang tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->