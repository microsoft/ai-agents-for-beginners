[![Intro to AI Agents](../../../translated_images/tl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(I-click ang larawan sa itaas upang panoorin ang video para sa araling ito)_

# Panimula sa AI Agents at Mga Gamit ng Agent

Maligayang pagdating sa kurso na **AI Agents para sa mga Baguhan**! Ang kursong ito ay nagbibigay sa iyo ng pundamental na kaalaman — at totoong gumaganang code — upang makapagsimula kang bumuo ng AI Agents mula sa simula.

Halika at makipagkumustahan sa <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — puno ito ng mga nag-aaral at tagabuo ng AI na masayang sasagot sa iyong mga katanungan.

Bago tayo magsimula sa pagbuo, tiyakin muna nating nauunawaan natin kung ano nga ba talaga ang isang AI Agent at kailan ito kapaki-pakinabang gamitin.

---

## Panimula

Tinutugunan ng araling ito ang mga sumusunod:

- Ano ang AI Agents, at ang iba't ibang uri nito
- Para saan angkop gamitin ang AI Agents
- Ang mga pangunahing bahagi na gagamitin mong bumuo ng solusyong Agentic

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, dapat ay kaya mong:

- Ipaliwanag kung ano ang AI Agent at paano ito naiiba sa karaniwang AI solution
- Malaman kung kailan dapat magamit ang AI Agent (at kung kailan hindi)
- Gumuhit ng pangunahing disenyo ng solusyong Agentic para sa isang totoong suliranin

---

## Pagpapakahulugan ng AI Agents at Mga Uri ng AI Agents

### Ano ang AI Agents?

Narito ang isang simpleng paraan upang ito’y maunawaan:

> **Ang AI Agents ay mga sistema na nagbibigay-daan sa Large Language Models (LLMs) na *gawin ang mga bagay* — sa pamamagitan ng pagbibigay sa kanila ng mga kagamitan at kaalaman upang kumilos sa mundo, hindi lamang tumugon sa mga prompt.**

Ipaliwanag pa natin:

- **Sistema** — Hindi lamang isang bagay ang AI Agent. Ito ay isang koleksyon ng mga bahagi na nagtutulungan. Sa pinaka-ugat nito, bawat agent ay may tatlong bahagi:
  - **Kapaligiran** — Ang espasyo kung saan gumagana ang agent. Para sa isang travel booking agent, ito ang mismong booking platform.
  - **Sensor** — Paano binabasa ng agent ang kasalukuyang kalagayan ng kanyang kapaligiran. Halimbawa, tinitingnan ng travel agent ang availability ng hotel o presyo ng flight.
  - **Actuator** — Paano kumikilos ang agent. Maaring mag-book ng kwarto, magpadala ng kumpirmasyon, o magcancel ng reservation ang travel agent.

![What Are AI Agents?](../../../translated_images/tl/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Umiiral na ang mga agents bago pa man ang LLMs, ngunit ang LLMs ang nagpapalakas sa makabagong mga agent. Naiintindihan nila ang natural na wika, nakakapag-isip tungkol sa konteksto, at natutugunan ang malabong kahilingan ng user sa isang konkretong plano ng gawain.

- **Pagsasagawa ng Aksyon** — Kung walang agent system, ang isang LLM ay nagge-generate lang ng teksto. Sa loob ng agent system, kaya ng LLM na *isagawa* ang mga hakbang — maghanap sa database, tumawag ng API, magpadala ng mensahe.

- **Pag-access sa mga Kasangkapan** — Ang mga kasangkapang maaaring gamitin ng agent ay nakadepende sa (1) kapaligirang pinapatakbo nito at (2) kung ano ang pinili ng developer na ibigay dito. Maaring maka-search ng flights ang travel agent pero hindi makapag-edit ng talaan ng customer — nakabase ito sa iyong pagkakabit.

- **Memorya + Kaalaman** — Maaaring magkaroon ang mga agent ng panandaliang memorya (kasalukuyang usapan) at pangmatagalang memorya (talaan ng customer, mga nakaraang interaksyon). Maaring "maalala" ng travel agent na gusto mo ng mga upuang nasa tabi ng bintana.

---

### Mga Iba't Ibang Uri ng AI Agents

Hindi lahat ng agent ay pareho ang pagkakagawa. Narito ang paghahati-hati ng mga pangunahing uri, gamit ang travel booking agent bilang halimbawa:

| **Uri ng Agent** | **Ano ang Ginagawa Nito** | **Halimbawa ng Travel Agent** |
|---|---|---|
| **Simple Reflex Agents** | Sumusunod sa mga naka-hardcode na patakaran — walang memorya, walang plano. | Nakita ang reklamo sa email → ipinapasa sa customer service. 'Yan lang. |
| **Model-Based Reflex Agents** | May nakapaloob na modelo ng mundo at ina-update ito kapag may pagbabago. | Sinusubaybayan ang kasaysayan ng presyo ng flight at nagbibigay babala sa mga biglang mahal na ruta. |
| **Goal-Based Agents** | May layunin at iniisip kung paano ito mararating hakbang-hakbang. | Nagbu-book ng buong biyahe (flights, kotse, hotel) mula sa kasalukuyan mong lokasyon patungo sa destinasyon. |
| **Utility-Based Agents** | Hindi lang basta naghahanap ng *isang* solusyon — hinahanap ang *pinakamainam* sa pamamagitan ng pagtimbang ng mga kompromiso. | Iniiwasan ang gastos laban sa kaginhawaan para matukoy ang pinakaangkop na biyahe ayon sa kagustuhan mo. |
| **Learning Agents** | Humuhusay habang tumatagal sa pagkatuto mula sa feedback. | Inaayos ang mga rekomendasyon sa mga susunod na booking batay sa post-trip na survey. |
| **Hierarchical Agents** | Isang mataas na antas na agent ang naghahati ng trabaho sa mga subtask at ipinapasa sa mas mababang antas na agents. | Ang hiling na "i-cancel ang biyahe" ay hinahati sa: cancel flight, cancel hotel, cancel car rental — bawat isa ay hawak ng sub-agent. |
| **Multi-Agent Systems (MAS)** | Maraming magkakaibang agents na nagtutulungan (o nagkokompitensya). | Cooperative: magkahiwalay na agents ang humahawak sa hotel, flights, at libangan. Competitive: maraming agents ang nagkokompitensya para punuan ang mga kwarto sa hotel sa pinakamurang presyo. |

---

## Kailan Gumamit ng AI Agents

Hindi dahil kaya mong gumamit ng AI Agent ay palaging dapat mong gamitin. Narito ang mga sitwasyong talagang kapaki-pakinabang ang mga agent:

![When to use AI Agents?](../../../translated_images/tl/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Mga Problema na Walang Tiyak na Sagot** — Kapag ang mga hakbang upang malutas ang problema ay hindi maaaring i-preprogram. Kailangan ng LLM na tuklasin ang daan nang dinamiko.
- **Mga Prosesong May Maraming Hakbang** — Mga gawain na nangangailangan ng paggamit ng mga kasangkapan sa maraming sali, hindi lang isang lookup o paggawa ng teksto.
- **Pagpapabuti Habang Lumilipas ang Panahon** — Kapag nais mong ang sistema ay maging mas matalino batay sa feedback ng user o senyales mula sa kapaligiran.

Tatalakayin natin ng mas malalim kung kailan (at kung kailan *hindi*) dapat gamitin ang AI Agents sa araling **Pagbuo ng Mapagkakatiwalaang AI Agents** sa kalaunan ng kurso.

---

## Mga Pangunahing Bahagi ng Solusyong Agentic

### Pag-develop ng Agent

Ang unang dapat gawin sa pagbuo ng agent ay tukuyin *ano ang kaya nitong gawin* — ang mga kasangkapan, aksyon, at pag-uugali nito.

Sa kursong ito, ginagamit namin ang **Azure AI Agent Service** bilang pangunahing plataporma. Sinusuportahan nito ang:

- Mga open model tulad ng OpenAI, Mistral, at Llama
- Lisensiyadong datos mula sa mga provider tulad ng Tripadvisor
- Standardized OpenAPI 3.0 na mga kahulugan ng kasangkapan

### Mga Agentic Pattern

Nakikipagkomunika ka sa LLMs sa pamamagitan ng prompts. Sa mga agent, hindi mo palaging magagawa na manu-manong likhain ang bawat prompt — kailangan ng agent na kumilos sa maraming hakbang. Dito pumapasok ang **Agentic Patterns**. Ito ay mga reusable na estratehiya para sa prompting at pag-oorganisa ng LLMs sa mas scalable at mapagkakatiwalaang paraan.

Ang kursong ito ay nakaayos ayon sa mga pinaka-karaniwan at kapaki-pakinabang na agentic patterns.

### Agentic Frameworks

Nagbibigay ang Agentic Frameworks ng mga developer ng handang templates, kasangkapan, at imprastruktura para sa pagbuo ng mga agents. Pinapadali nito ang:

- Pagkakabit ng mga kasangkapan at kakayahan
- Pagsubaybay sa ginagawa ng agent (at pag-debug kapag may mali)
- Pakikipagtulungan sa pagitan ng maraming agents

Sa kursong ito, nakatuon kami sa **Microsoft Agent Framework (MAF)** para sa paggawa ng mga agent na handa na para sa produksyon.

---

## Mga Halimbawa ng Code

Handa ka na bang makita ito sa aksyon? Narito ang mga code sample para sa araling ito:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## May Tanong Ka Ba?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) upang makipag-ugnayan sa ibang mga nag-aaral, dumalo sa mga office hours, at sagutin ang iyong mga tanong tungkol sa AI Agents kasama ang komunidad.

---

## Nakaraang Aralin

[Course Setup](../00-course-setup/README.md)

## Susunod na Aralin

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang serbisyong AI na pagsasalin [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakaugnay. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na opisyal na pinagmulan. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->