[![Intro to AI Agents](../../../translated_images/tl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(I-click ang larawan sa itaas para panoorin ang video para sa araling ito)_

# Panimula sa AI Agents at Mga Gamit ng Agent

Maligayang pagdating sa kursong **AI Agents para sa Mga Baguhan**! Ang kursong ito ay nagbibigay sa iyo ng pundamental na kaalaman — at totoong gumaganang code — upang makapagsimula kang bumuo ng AI Agents mula sa simula.

Halina't mag-sabi ng hi sa <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — puno ito ng mga nag-aaral at mga tagabuo ng AI na masayang sumagot sa mga tanong.

Bago tayo tumalon sa pagbuo, siguraduhing naiintindihan natin kung ano talaga ang isang AI Agent *at* kailan makatuwiran gamitin ito.

---

## Panimula

Saklaw ng araling ito:

- Ano ang AI Agents, at ang iba't ibang uri nito
- Anong mga uri ng gawain ang pinakanaaangkop para sa AI Agents
- Ang mga pangunahing sangkap na gagamitin mo sa pagdidisenyo ng isang Agentic na solusyon

## Mga Layunin sa Pagkatuto

Pagkatapos ng araling ito, dapat ay kaya mong:

- Ipaliwanag kung ano ang AI Agent at paano ito naiiba sa isang karaniwang AI solution
- Malaman kung kailan dapat gumamit ng AI Agent (at kung kailan hindi)
- Gumuhit ng isang pangunahing disenyo ng Agentic na solusyon para sa isang tunay na problema

---

## Pagpapakahulugan sa AI Agents at Mga Uri ng AI Agents

### Ano ang AI Agents?

Ganito ang simpleng paraan upang tingnan ito:

> **Ang AI Agents ay mga sistema na nagpapahintulot sa Large Language Models (LLMs) na talagang *gawin ang mga bagay* — sa pamamagitan ng pagbibigay sa kanila ng mga kasangkapan at kaalaman upang kumilos sa mundo, hindi lang basta tumugon sa mga prompt.**

Paliwanag pa ito ng kaunti:

- **Sistema** — Ang AI Agent ay hindi lang isang bagay. Ito ay isang koleksyon ng mga bahagi na nagtutulungan. Sa pinakapuso nito, bawat agent ay may tatlong bahagi:
  - **Kapaligiran** — Ang espasyo kung saan gumagana ang agent. Para sa isang travel booking agent, ito ay ang mismong booking platform.
  - **Sensors** — Paano nababasa ng agent ang kasalukuyang kalagayan ng kapaligiran. Maaaring tignan ng travel agent ang availability ng hotel o presyo ng flight.
  - **Actuators** — Paano kumikilos ang agent. Maaaring mag-book ng kwarto, magpadala ng kumpirmasyon, o mag-cancel ng reservation ang travel agent.

![What Are AI Agents?](../../../translated_images/tl/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Umiiral ang mga agents bago pa man ang LLMs, ngunit ang LLMs ang nagpapalakas sa mga modernong agent. Kaya nilang intindihin ang natural na wika, mag-isip ayon sa konteksto, at gawing konkretong plano ang malabong kahilingan ng gumagamit.

- **Pagsasagawa ng Aksyon** — Kung walang agent system, ang LLM ay gumagawa lamang ng teksto. Sa loob ng agent system, kaya ng LLM na talagang *isagawa* ang mga hakbang — maghanap sa database, tumawag ng API, magpadala ng mensahe.

- **Pag-access sa mga Kasangkapan** — Depende sa (1) kapaligiran kung saan tumatakbo ang agent at (2) sa pinili ng developer na ibigay dito kung ano ang mga kasangkapang magagamit. Maaaring makahanap ng flights ang travel agent ngunit hindi maka-edit ng record ng customer — depende ito sa naka-wire up.

- **Memorya + Kaalaman** — Maaaring magkaroon ang agents ng panandaliang memorya (ang kasalukuyang pag-uusap) at pangmatagalang memorya (database ng customer, nakaraang interaksyon). Maaaring "maalala" ng travel agent na mas gusto mo ang mga window seats.

---

### Mga Iba't Ibang Uri ng AI Agents

Hindi lahat ng agents ay pareho ang pagkakagawa. Narito ang talaan ng mga pangunahing uri, gamit ang travel booking agent bilang halimbawa:

| **Uri ng Agent** | **Ano ang Ginagawa** | **Halimbawa ng Travel Agent** |
|---|---|---|
| **Simple Reflex Agents** | Sumusunod sa mga mahigpit na patakaran — walang memorya, walang plano. | Nakakita ng reklamo sa email → ipinapasa sa customer service. 'Yan lang. |
| **Model-Based Reflex Agents** | Nagpapanatili ng panloob na modelo ng mundo at ina-update ito habang nagbabago ang mga bagay. | Tinututukan ang kasaysayan ng presyo ng flight at pinapansin ang sobrang mahal na ruta. |
| **Goal-Based Agents** | May layunin at unti-unting iniisip kung paano ito mararating. | Nagbu-book ng buong trip (flights, kotse, hotel) mula sa kasalukuyan mong lokasyon para makarating ka sa destinasyon. |
| **Utility-Based Agents** | Hindi lang naghahanap ng *isang* solusyon — hinahanap ang *pinakamainam* sa pamamagitan ng pagtimbang ng mga kalakihan at kahinaan. | Binabalanse ang gastos laban sa kaginhawaan para mahanap ang trip na pinakaangkop sa iyong mga kagustuhan. |
| **Learning Agents** | Yumayabong sa paglipas ng panahon sa pamamagitan ng pagkatuto mula sa feedback. | Inaayos ang mga rekomendasyon sa booking batay sa mga resulta ng survey pagkatapos ng trip. |
| **Hierarchical Agents** | Isang mataas na antas na agent ang naghahati ng gawain sa mga subtask at nagtatalaga sa mas mababang antas ng mga agent. | Ang kahilingan na "i-cancel ang trip" ay hinahati sa: cancel flight, cancel hotel, cancel rental ng kotse — bawat isa ay hawak ng sub-agent. |
| **Multi-Agent Systems (MAS)** | Maramihang independiyenteng agents na nagtutulungan (o nakikipagkompetensya). | Sama-samang nagtatrabaho: mga hiwalay na agent para sa hotels, flights, at entertainment. Kompetisyon: iba't ibang agents ang nakikipagkarera para mapunan ang mga silid ng hotel sa pinakamahusay na presyo. |

---

## Kailan Gagamit ng AI Agents

Hindi dahil kaya mong gumamit ng AI Agent ay palaging dapat mong gawin ito. Narito ang mga sitwasyon kung kailan talagang nagiging kapaki-pakinabang ang mga agents:

![When to use AI Agents?](../../../translated_images/tl/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Mga Problema na Walang Tiyak na Sagot** — Kapag ang mga hakbang para lutasin ang problema ay hindi maaaring i-program nang bago. Kailangan ng LLM na tuklasin ang landas nang dinamiko.
- **Mga Proseso na Maraming Hakbang** — Gawain na nangangailangan ng paggamit ng mga kasangkapan sa maraming ulit, hindi lang isang tingin o paggawa.
- **Pagbuti sa Paglipas ng Panahon** — Kapag gusto mong gumaling ang sistema batay sa feedback ng gumagamit o mga signal mula sa kapaligiran.

Mas pag-aaralan natin nang mabuti ang kung kailan (at kailan *hindi*) gagamit ng AI Agents sa leksyong **Pagtatayo ng Mapagkakatiwalaang AI Agents** sa susunod na bahagi ng kurso.

---

## Mga Pangunahing Kaalaman sa Agentic na mga Solusyon

### Pagbuo ng Agent

Ang unang gagawin kapag bumubuo ng agent ay tukuyin *kung ano ang kaya nitong gawin* — ang mga kasangkapan, aksyon, at asal nito.

Sa kursong ito, ginagamit natin ang **Azure AI Agent Service** bilang pangunahing platform. Sinusuportahan nito ang:

- Mga modelo mula sa mga provider tulad ng OpenAI, Mistral, at Meta (Llama)
- Lisensyadong data mula sa mga provider tulad ng Tripadvisor
- Standardized OpenAPI 3.0 na mga depinisyon ng kasangkapan

### Mga Agentic Patterns

Nakikipag-usap ka sa LLMs sa pamamagitan ng mga prompt. Sa mga agents, hindi laging pwede mano-manong gawin ang bawat prompt — kailangan ng agent na kumilos sa maraming hakbang. Dito pumapasok ang **Agentic Patterns**. Ito ay mga reusable na estratehiya para sa prompting at pag-ayos ng LLMs sa mas scalable at maaasahang paraan.

Nakabatay ang kursong ito sa mga pinaka-karaniwan at kapaki-pakinabang na agentic patterns.

### Mga Agentic Frameworks

Ang Agentic Frameworks ay nagbibigay sa mga developer ng mga template, kasangkapan, at imprastraktura para sa pagpapadali ng paggawa ng mga agent. Pinapadali nila ang:

- Pagsasama ng mga kasangkapan at kakayahan
- Pagsubaybay sa ginagawa ng agent (at pag-debug kapag may mali)
- Pakikipagtulungan sa maraming agent

Sa kursong ito, nakatuon tayo sa **Microsoft Agent Framework (MAF)** para sa paggawa ng mga agent na handa na sa produksyon.

---

## Mga Halimbawang Code

Handa ka na bang makita ito sa aksyon? Narito ang mga halimbawang code para sa araling ito:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## May Mga Tanong?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para makipag-ugnayan sa iba pang mga nag-aaral, dumalo sa office hours, at makakuha ng sagot sa iyong mga tanong tungkol sa AI Agent mula sa komunidad.

---

## Nakaraang Aralin

[Course Setup](../00-course-setup/README.md)

## Susunod na Aralin

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->