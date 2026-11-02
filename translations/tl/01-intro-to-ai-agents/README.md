[![Intro to AI Agents](../../../translated_images/tl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(I-click ang larawan sa itaas upang mapanood ang video para sa aralin na ito)_

# Panimula sa Mga AI Agent at Mga Gamit ng Agent

Maligayang pagdating sa kursong **AI Agents for Beginners**! Ang kursong ito ay nagbibigay sa iyo ng pundamental na kaalaman — at tunay na gumaganang code — upang simulan ang paggawa ng mga AI Agent mula sa simula.

Halika at bumati sa <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — puno ito ng mga nag-aaral at mga tagagawa ng AI na masayang sumagot sa mga tanong.

Bago tayo tumalon sa paggawa, siguraduhin muna nating talagang naiintindihan natin kung ano ang *AI Agent* at kailan ito nararapat gamitin.

---

## Panimula

Sinasaklaw ng araling ito ang:

- Ano ang mga AI Agent, at ang iba't ibang uri na umiiral
- Anong mga uri ng gawain ang pinakanararapat para sa mga AI Agent
- Ang mga pangunahing bahagi na gagamitin mo sa pagdidisenyo ng isang Agentic na solusyon

## Mga Layunin sa Pagkatuto

Sa katapusan ng araling ito, dapat kaya mong:

- Ipaliwanag kung ano ang AI Agent at kung paano ito naiiba sa karaniwang AI na solusyon
- Malaman kung kailan dapat gumamit ng AI Agent (at kung kailan hindi)
- Gumuhit ng pangunahing disenyo ng Agentic na solusyon para sa isang tunay na mundo na problema

---

## Pagpapakahulugan sa Mga AI Agent at Mga Uri ng AI Agent

### Ano ang mga AI Agent?

Narito ang isang simpleng paraan upang isipin ito:

> **Ang mga AI Agent ay mga sistema na nagbibigay-daan sa Large Language Models (LLMs) upang aktwal na *gumawa ng mga bagay* — sa pamamagitan ng pagbibigay sa kanila ng mga kagamitan at kaalaman para kumilos sa mundo, hindi lang tumugon sa mga prompt.**

Linawin natin iyan nang kaunti:

- **Sistema** — Ang AI Agent ay hindi lang isang bagay. Ito ay isang koleksyon ng mga bahagi na nagtutulungan. Sa pinakapuso, bawat agent ay may tatlong bahagi:
  - **Kapaligid** — Ang espasyo kung saan gumagana ang agent. Para sa isang travel booking agent, ito ay ang booking platform mismo.
  - **Mga Sensor** — Paano binabasa ng agent ang kasalukuyang kalagayan ng kapaligiran. Ang aming travel agent ay maaaring magsuri ng availability ng hotel o presyo ng flight.
  - **Mga Aktwador** — Paano kumikilos ang agent. Maaaring mag-book ang travel agent ng silid, magpadala ng kumpirmasyon, o kanselahin ang isang reserbasyon.

![What Are AI Agents?](../../../translated_images/tl/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Umiiral na ang mga agent bago pa man ang LLMs, ngunit ang LLMs ang nagpapalakas sa makabagong mga agent. Kaya nilang unawain ang natural na wika, mag-isip tungkol sa konteksto, at gawing tiyak na plano ng aksyon ang isang malabong kahilingan ng gumagamit.

- **Pagsasagawa ng Mga Aksyon** — Kung walang agent system, ang isang LLM ay gumagawa lang ng teksto. Sa loob ng system ng agent, maaaring aktwal na *isaayos* ng LLM ang mga hakbang — maghanap sa database, tumawag ng API, magpadala ng mensahe.

- **Pag-access sa Mga Kagamitan** — Ang mga kagamitan na maaaring gamitin ng agent ay depende sa (1) kapaligiran kung saan ito tumatakbo at (2) kung ano ang pinili ng developer na ibigay dito. Ang isang travel agent ay maaaring makapaghahanap ng mga flight ngunit hindi makakapagbago ng mga tala ng customer — ito ay nakasalalay sa kung paano mo ito nilalagyan.

- **Memorya + Kaalaman** — Maaaring magkaroon ang mga agent ng pansamantalang memorya (ang kasalukuyang pag-uusap) at pangmatagalang memorya (isang database ng customer, mga nakaraang interaksyon). Ang travel agent ay maaaring "matandaan" na mas gusto mo ang mga upuan sa tabi ng bintana.

---

### Iba't Ibang Uri ng AI Agent

Hindi lahat ng agent ay pare-pareho ang pagkakagawa. Narito ang paghahati-hati ng mga pangunahing uri, gamit ang isang travel booking agent bilang halimbawa:

| **Uri ng Agent** | **Ano ang Ginagawa Nito** | **Halimbawa ng Travel Agent** |
|---|---|---|
| **Simple Reflex Agents** | Sumusunod sa mga hard-coded na patakaran — walang memorya, walang pagpaplano. | Nakakakita ng email ng reklamo → ipinapasa sa customer service. Iyon lang. |
| **Model-Based Reflex Agents** | May internal na modelo ng mundo at ina-update ito kapag may pagbabago. | Sinusubaybayan ang mga kasaysayan ng presyo ng flight at tinutukoy ang mga ruta na biglaang mahal. |
| **Goal-Based Agents** | May layunin sa isip at tinutukoy kung paano ito mararating hakbang-hakbang. | Nagbo-book ng buong biyahe (mga flight, kotse, hotel) mula sa inyong kasalukuyang lokasyon papunta sa iyong destinasyon. |
| **Utility-Based Agents** | Hindi lang naghahanap ng *isang* solusyon — hinahanap ang *pinakamahusay* sa pamamagitan ng pagbabasang timbang ng mga tradeoff. | Binabalanse ang gastos laban sa kaginhawaan upang mahanap ang biyahe na pinakamataas ang puntos para sa iyong mga kagustuhan. |
| **Learning Agents** | Humuhusay sa paglipas ng panahon sa pamamagitan ng pagkatuto mula sa feedback. | Inaayos ang mga rekomendasyon sa booking sa hinaharap base sa mga resulta ng post-trip survey. |
| **Hierarchical Agents** | Isang high-level agent ang naghahati-hati ng gawain sa mga subtask at ipinapasa sa mga mababang-level na agent. | Ang kahilingan na "kanselahin ang biyahe" ay hinahati sa: kanselahin ang flight, kanselahin ang hotel, kanselahin ang pag-upa ng kotse — bawat isa ay hinahawakan ng isang sub-agent. |
| **Multi-Agent Systems (MAS)** | Maraming independiyenteng agent na nagtutulungan (o nagtutunggali). | Kooperatibo: magkakahiwalay na agent para sa hotel, flight, at libangan. Kompetisyon: maraming agent ang nakikipagtunggali upang punuin ang mga kwarto ng hotel sa pinakamagandang presyo. |

---

## Kailan Gagamit ng AI Agent

Hindi dahil kaya mong gumamit ng AI Agent ay palaging dapat mo itong gamitin. Narito ang mga sitwasyon kung kailan talagang namumukod-tangi ang mga agent:

![When to use AI Agents?](../../../translated_images/tl/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Mga Problema na Walang Hangganan** — Kapag ang mga hakbang upang malutas ang problema ay hindi maaaring i-preprograma. Kailangang alamin ng LLM ang landas nang dinamiko.
- **Mga Multi-Step na Proseso** — Mga gawain na nangangailangan ng paggamit ng mga kagamitan sa maraming mga hakbang, hindi lang isang lookup o paggawa.
- **Pagpapabuti sa Paglipas ng Panahon** — Kapag nais mong matuto ang sistema mula sa feedback ng gumagamit o mga signal sa kapaligiran.

Tatalakayin natin nang mas malalim kung kailan (at kailan *hindi*) dapat gumamit ng AI Agent sa araling **Building Trustworthy AI Agents** mamaya sa kurso.

---

## Mga Pangunahing Kaalaman sa Mga Agentic na Solusyon

### Pagbuo ng Agent

Ang unang ginagawa kapag bumubuo ng isang agent ay ang pagtukoy ng *kung ano ang kaya nitong gawin* — ang mga kagamitan, aksyon, at mga pag-uugali nito.

Sa kursong ito, ginagamit natin ang **Microsoft Foundry Agent Service** bilang pangunahing plataporma. Sinusuportahan nito:

- Mga modelo mula sa mga tagapagbigay tulad ng OpenAI, Mistral, at Meta (Llama)
- Lisensyadong datos mula sa mga tagapagbigay tulad ng Tripadvisor
- Standardized OpenAPI 3.0 na mga depinisyon ng kagamitan

### Mga Agentic Pattern

Nakikipag-ugnayan ka sa mga LLM sa pamamagitan ng mga prompt. Sa mga agent, hindi mo laging magagawa ang pagbuo ng bawat prompt nang manu-mano — kailangang kumilos ang agent sa maraming hakbang. Dito papasok ang **Agentic Patterns**. Ito ay mga reusable na estratehiya para sa prompting at pagsasaayos ng mga LLM sa mas scalable at maasahang paraan.

Ang kursong ito ay nakaayos sa paligid ng mga pinaka-karaniwan at kapaki-pakinabang na agentic pattern.

### Mga Agentic Framework

Ang mga Agentic Framework ay nagbibigay sa mga developer ng mga handang template, kagamitan, at imprastraktura para sa paggawa ng mga agent. Pinapadali nito ang:

- Pagkonekta ng mga kagamitan at kakayahan
- Pagsubaybay sa ginagawa ng agent (at pag-debug kapag may mali)
- Pakikipagtulungan sa maraming agent

Sa kursong ito, nakatuon tayo sa **Microsoft Agent Framework (MAF)** para sa paggawa ng mga agent na handa na sa produksyon.

---

## Mga Halimbawa ng Code

Handa ka na bang makita ito sa aksyon? Narito ang mga halimbawa ng code para sa araling ito:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## May Mga Katanungan?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipag-ugnayan sa ibang nag-aaral, dumalo sa office hours, at makuha ang sagot sa iyong mga tanong tungkol sa AI Agent mula sa komunidad.


---

## Pagsusuri sa Simpleng Takbo ng Agent na Ito (Opsyonal)

Kapag natutunan mo nang mag-deploy ng mga agent sa [Lesson 16](../16-deploying-scalable-agents/README.md), maaari kang maglagay ng mabilis na post-deploy health check para sa `TravelAgent` ng araling ito gamit ang handang katalogo na [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Tingnan ang [`tests/README.md`](../tests/README.md) para sa kung paano ito patakbuhin.

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