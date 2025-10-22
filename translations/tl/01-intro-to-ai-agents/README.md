<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-29T09:38:37+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "tl"
}
-->
[![Intro to AI Agents](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.tl.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(I-click ang larawan sa itaas upang mapanood ang video ng araling ito)_

# Panimula sa AI Agents at Mga Gamit Nito

Maligayang pagdating sa kursong "AI Agents para sa mga Baguhan"! Ang kursong ito ay nagbibigay ng mga pangunahing kaalaman at mga halimbawa ng aplikasyon para sa paggawa ng AI Agents.

Sumali sa [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa ibang mga mag-aaral at tagabuo ng AI Agents at magtanong tungkol sa kursong ito.

Upang simulan ang kursong ito, magsisimula tayo sa mas malalim na pag-unawa kung ano ang AI Agents at paano natin ito magagamit sa mga aplikasyon at daloy ng trabaho na ating binubuo.

## Panimula

Tatalakayin sa araling ito:

- Ano ang AI Agents at ano-ano ang iba't ibang uri ng agents?
- Anong mga kaso ng paggamit ang pinakaangkop para sa AI Agents at paano ito makakatulong sa atin?
- Ano ang mga pangunahing bahagi sa pagdidisenyo ng Agentic Solutions?

## Mga Layunin sa Pagkatuto
Pagkatapos ng araling ito, dapat mong magawa ang sumusunod:

- Maunawaan ang mga konsepto ng AI Agent at paano ito naiiba sa ibang AI solutions.
- Magamit ang AI Agents nang mas epektibo.
- Makapagdisenyo ng Agentic solutions na produktibo para sa parehong mga gumagamit at kliyente.

## Pagpapakilala sa AI Agents at Mga Uri Nito

### Ano ang AI Agents?

Ang AI Agents ay mga **sistema** na nagbibigay-daan sa **Large Language Models (LLMs)** na **gumawa ng mga aksyon** sa pamamagitan ng pagpapalawak ng kanilang kakayahan sa pagbibigay ng **access sa mga tools** at **kaalaman**.

Himayin natin ang depinisyong ito:

- **Sistema** - Mahalaga na isipin ang agents bilang isang sistema ng maraming bahagi, hindi lamang isang solong bahagi. Sa pinaka-pangunahing antas, ang mga bahagi ng isang AI Agent ay:
  - **Kapaligiran** - Ang tinukoy na espasyo kung saan gumagana ang AI Agent. Halimbawa, kung mayroon tayong travel booking AI Agent, ang kapaligiran ay maaaring ang travel booking system na ginagamit ng AI Agent upang tapusin ang mga gawain.
  - **Sensors** - Ang kapaligiran ay may impormasyon at nagbibigay ng feedback. Ginagamit ng AI Agents ang sensors upang mangalap at mag-interpret ng impormasyon tungkol sa kasalukuyang estado ng kapaligiran. Sa halimbawa ng Travel Booking Agent, ang travel booking system ay maaaring magbigay ng impormasyon tulad ng availability ng hotel o presyo ng flight.
  - **Actuators** - Kapag natanggap na ng AI Agent ang kasalukuyang estado ng kapaligiran, tinutukoy nito ang aksyon na kailangang gawin upang baguhin ang kapaligiran. Para sa travel booking agent, maaaring ito ay mag-book ng available na kwarto para sa user.

![Ano ang AI Agents?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.tl.png)

**Large Language Models** - Ang konsepto ng agents ay umiiral na bago pa man ang paglikha ng LLMs. Ang bentahe ng paggawa ng AI Agents gamit ang LLMs ay ang kanilang kakayahang mag-interpret ng wika ng tao at datos. Ang kakayahang ito ay nagbibigay-daan sa LLMs na maunawaan ang impormasyon mula sa kapaligiran at makabuo ng plano upang baguhin ito.

**Gumawa ng Aksyon** - Sa labas ng mga sistema ng AI Agent, limitado ang LLMs sa mga sitwasyon kung saan ang aksyon ay ang paggawa ng nilalaman o impormasyon batay sa prompt ng user. Sa loob ng mga sistema ng AI Agent, maaaring maisakatuparan ng LLMs ang mga gawain sa pamamagitan ng pag-interpret ng kahilingan ng user at paggamit ng mga tools na nasa kanilang kapaligiran.

**Access sa Tools** - Ang mga tools na maaaring gamitin ng LLM ay tinutukoy ng 1) ang kapaligiran kung saan ito gumagana at 2) ang developer ng AI Agent. Sa halimbawa ng travel agent, ang mga tools ng agent ay limitado ng mga operasyon na available sa booking system, at/o maaaring limitahan ng developer ang access ng agent sa mga flights.

**Memorya+Kaalaman** - Ang memorya ay maaaring panandalian sa konteksto ng pag-uusap sa pagitan ng user at ng agent. Pangmatagalan, bukod sa impormasyong ibinibigay ng kapaligiran, maaaring kumuha ng kaalaman ang AI Agents mula sa ibang sistema, serbisyo, tools, at maging sa ibang agents. Sa halimbawa ng travel agent, ang kaalamang ito ay maaaring impormasyon tungkol sa mga travel preferences ng user na nasa isang customer database.

### Ang iba't ibang uri ng agents

Ngayon na mayroon na tayong pangkalahatang depinisyon ng AI Agents, tingnan natin ang ilang partikular na uri ng agents at paano ito maaaring gamitin sa isang travel booking AI agent.

| **Uri ng Agent**              | **Paglalarawan**                                                                                                                       | **Halimbawa**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Simple Reflex Agents**      | Gumagawa ng agarang aksyon batay sa mga paunang itinakdang patakaran.                                                                 | Ang travel agent ay nag-iinterpret ng konteksto ng email at ipinapasa ang mga reklamo sa customer service.                                                                                                                      |
| **Model-Based Reflex Agents** | Gumagawa ng aksyon batay sa isang modelo ng mundo at mga pagbabago dito.                                                              | Ang travel agent ay inuuna ang mga ruta na may malalaking pagbabago sa presyo batay sa access sa historical pricing data.                                                                                                       |
| **Goal-Based Agents**         | Lumilikha ng mga plano upang makamit ang mga tiyak na layunin sa pamamagitan ng pag-interpret ng layunin at pagtukoy ng mga aksyon upang maabot ito.                                  | Ang travel agent ay nagbu-book ng biyahe sa pamamagitan ng pagtukoy ng mga kinakailangang travel arrangements (kotse, pampublikong transportasyon, flights) mula sa kasalukuyang lokasyon patungo sa destinasyon.                                                      |
| **Utility-Based Agents**      | Isinasaalang-alang ang mga kagustuhan at tinataya ang mga tradeoff nang numerikal upang matukoy kung paano makakamit ang mga layunin.                                               | Ang travel agent ay pinapakinabangan ang utility sa pamamagitan ng pagtimbang ng kaginhawaan laban sa gastos kapag nagbu-book ng biyahe.                                                                                                                              |
| **Learning Agents**           | Nagpapabuti sa paglipas ng panahon sa pamamagitan ng pagtugon sa feedback at pag-aadjust ng mga aksyon nang naaayon.                                                        | Ang travel agent ay nagpapabuti sa pamamagitan ng paggamit ng feedback ng customer mula sa mga post-trip survey upang gumawa ng mga pagsasaayos sa mga susunod na booking.                                                                                             |
| **Hierarchical Agents**       | Mayroong maraming agents sa isang tiered system, kung saan ang mga higher-level agents ay naghahati ng mga gawain sa mga subtasks para sa mga lower-level agents na tapusin. | Ang travel agent ay nagkakansela ng biyahe sa pamamagitan ng paghahati ng gawain sa mga subtasks (halimbawa, pagkansela ng mga partikular na booking) at pinapagawa ito sa mga lower-level agents, na nag-uulat pabalik sa higher-level agent.                             |
| **Multi-Agent Systems (MAS)** | Ang mga agents ay gumagawa ng mga gawain nang independyente, maaaring kooperatibo o kompetitibo.                                                           | Kooperatibo: Maraming agents ang nagbu-book ng mga partikular na serbisyo sa paglalakbay tulad ng mga hotel, flights, at entertainment. Kompetitibo: Maraming agents ang namamahala at nagkakumpetensya sa isang shared hotel booking calendar upang mag-book ng mga customer sa hotel. |

## Kailan Gagamit ng AI Agents

Sa naunang bahagi, ginamit natin ang Travel Agent use-case upang ipaliwanag kung paano maaaring gamitin ang iba't ibang uri ng agents sa iba't ibang sitwasyon ng travel booking. Patuloy nating gagamitin ang aplikasyon na ito sa buong kurso.

Tingnan natin ang mga uri ng kaso ng paggamit kung saan pinakamahusay gamitin ang AI Agents:

![Kailan gagamit ng AI Agents?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.tl.png)

- **Mga Bukas na Problema** - pinapayagan ang LLM na tukuyin ang mga kinakailangang hakbang upang tapusin ang isang gawain dahil hindi ito laging maaaring i-hardcode sa isang workflow.
- **Mga Multi-Step na Proseso** - mga gawain na nangangailangan ng antas ng pagiging kumplikado kung saan kailangang gumamit ng tools o impormasyon ang AI Agent sa maraming pagkakataon sa halip na isang besesang retrieval.  
- **Pagpapabuti sa Paglipas ng Panahon** - mga gawain kung saan maaaring mag-improve ang agent sa paglipas ng panahon sa pamamagitan ng pagtanggap ng feedback mula sa kapaligiran o mga user upang makapagbigay ng mas mahusay na utility.

Tatalakayin natin ang higit pang mga konsiderasyon sa paggamit ng AI Agents sa araling "Building Trustworthy AI Agents."

## Mga Pangunahing Kaalaman sa Agentic Solutions

### Pagbuo ng Agent

Ang unang hakbang sa pagdidisenyo ng isang AI Agent system ay ang pagtukoy sa mga tools, aksyon, at pag-uugali. Sa kursong ito, magpo-focus tayo sa paggamit ng **Azure AI Agent Service** upang tukuyin ang ating mga Agents. Nag-aalok ito ng mga tampok tulad ng:

- Pagpili ng Open Models tulad ng OpenAI, Mistral, at Llama
- Paggamit ng Licensed Data mula sa mga provider tulad ng Tripadvisor
- Paggamit ng mga standardized OpenAPI 3.0 tools

### Mga Agentic Pattern

Ang komunikasyon sa LLMs ay sa pamamagitan ng prompts. Dahil sa semi-autonomous na kalikasan ng AI Agents, hindi laging posible o kinakailangan na manu-manong i-reprompt ang LLM pagkatapos ng pagbabago sa kapaligiran. Gumagamit tayo ng **Agentic Patterns** na nagbibigay-daan sa atin na i-prompt ang LLM sa maraming hakbang sa mas scalable na paraan.

Ang kursong ito ay nahahati sa ilan sa mga kasalukuyang popular na Agentic patterns.

### Mga Agentic Framework

Ang mga Agentic Framework ay nagbibigay-daan sa mga developer na ipatupad ang mga agentic pattern sa pamamagitan ng code. Ang mga framework na ito ay nag-aalok ng mga template, plugin, at tools para sa mas mahusay na kolaborasyon ng AI Agents. Ang mga benepisyong ito ay nagbibigay ng kakayahan para sa mas mahusay na observability at troubleshooting ng mga sistema ng AI Agent.

Sa kursong ito, susuriin natin ang research-driven na AutoGen framework at ang production-ready na Agent framework mula sa Semantic Kernel.

### May Karagdagang Tanong Tungkol sa AI Agents?

Sumali sa [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa ibang mga mag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

## Nakaraang Aralin

[Course Setup](../00-course-setup/README.md)

## Susunod na Aralin

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.