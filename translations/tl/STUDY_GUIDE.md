# AI Agents para sa mga Nagsisimula - Gabay sa Pag-aaral at Buod ng Kurso

Ang gabay na ito ay nagbibigay ng buod ng kurso na "AI Agents para sa mga Nagsisimula" at nagpapaliwanag ng mga pangunahing konsepto, mga framework, at mga disenyo ng pattern para sa pagbuo ng AI Agents.

## 1. Panimula sa AI Agents

**Ano ang AI Agents?**
Ang AI Agents ay mga sistema na nagpapalawak sa kakayahan ng Large Language Models (LLMs) sa pamamagitan ng pagbibigay sa kanila ng access sa **mga tools**, **kaalaman**, at **memorya**. Hindi tulad ng karaniwang LLM chatbot na nagge-generate lamang ng teksto batay sa training data, ang AI Agent ay maaaring:
- **Makaunawa** sa kapaligiran nito (sa pamamagitan ng sensors o input).
- **Mag-isip** kung paano lutasin ang isang problema.
- **Gumawa ng aksyon** upang baguhin ang kapaligiran (sa pamamagitan ng actuators o pagpapatupad ng tools).

**Pangunahing Bahagi ng isang Agent:**
- **Kapaligiran**: Ang espasyo kung saan kumikilos ang agent (hal., sistema ng booking).
- **Sensors**: Mga mekanismo para mangalap ng impormasyon (hal., pagbasa ng API).
- **Actuators**: Mga mekanismo para magsagawa ng mga aksyon (hal., pagpapadala ng email).
- **Utak (LLM)**: Ang reasoning engine na nagpaplano at nagpapasya kung anong mga aksyon ang gagawin.

## 2. Agentic Frameworks

Ginagamit ng kurso ang **Microsoft Agent Framework (MAF)** kasama ang **Azure AI Foundry Agent Service V2** para sa pagbuo ng mga agent:

| Bahagi | Pokus | Pinakamainam Para sa |
|--------|-------|----------------------|
| **Microsoft Agent Framework** | Pinagsamang Python/C# SDK para sa mga agent, tools, at workflows | Pagbuo ng mga agent na may mga tools, multi-agent workflows, at production patterns. |
| **Azure AI Foundry Agent Service** | Managed cloud runtime | Secure, scalable deployment na may built-in na state management, observability, at tiwala. |

## 3. Mga Agentic Design Patterns

Ang mga design pattern ay tumutulong ayusin kung paano gumagana ang mga agent upang makatugon ng maaasahan sa mga problema.

### **Tool Use Pattern** (Lesson 4)
Pinapahintulutan ng pattern na ito ang mga agent na makipag-ugnayan sa labas ng mundo.
- **Konsepto**: Ang agent ay binibigyan ng "schema" (isang listahan ng mga magagamit na function at kanilang mga parameter). Pinipili ng LLM *kung aling* tool ang tatawagin at kung *anong* argumento ayon sa kahilingan ng user.
- **Daloy**: Kahilingan ng User -> LLM -> **Pagpili ng Tool** -> **Pagsasagawa ng Tool** -> LLM (kasama ang output ng tool) -> Panghuling Tugon.
- **Mga Gamit**: Pagkuha ng real-time na data (panahon, presyo ng stock), paggawa ng kalkulasyon, pagpapatupad ng code.

### **Planning Pattern** (Lesson 7)
Pinapahintulutan ng pattern na ito ang mga agent na lutasin ang mahihirap at multi-step na gawain.
- **Konsepto**: Hinahati ng agent ang isang mataas na layunin sa sunud-sunod na mas maliliit na subtasks.
- **Mga Paraan**:
  - **Task Decomposition**: Hatiin ang "Magplano ng biyahe" sa "Mag-book ng flight", "Mag-book ng hotel", "Magrenta ng sasakyan".
  - **Iterative Planning**: Muling sinusuri ang plano batay sa output ng mga naunang hakbang (hal., kung puno ang flight, pumili ng ibang petsa).
- **Implementasyon**: Kadalasang may "Planner" agent na gumagawa ng estrukturadong plano (hal., JSON) na pagkatapos ay ipinatutupad ng ibang mga agent.

## 4. Mga Prinsipyo sa Disenyo

Kapag gumagawa ng mga agent, isaalang-alang ang tatlong dimensyon:
- **Espasyo**: Dapat kumonekta ang mga agent sa mga tao at kaalaman, maging accessible ngunit hindi pabigat.
- **Oras**: Dapat matuto ang mga agent mula sa *Nakaraan*, magbigay ng angkop na paalala sa *Kasalukuyan*, at umangkop para sa *Hinaharap*.
- **Puso (Core)**: Tanggapin ang kawalang-katiyakan ngunit magtatag ng tiwala sa pamamagitan ng transparensiya at kontrol ng user.

## 5. Buod ng mga Pangunahing Aralin

- **Aralin 1**: Ang mga agent ay mga sistema, hindi lang mga modelo. Nakakaunawa, nag-iisip, at kumikilos sila.
- **Aralin 2**: Ang Microsoft Agent Framework ay nagpapasimple sa komplikasyon ng pagtawag ng tool at pamamahala ng estado.
- **Aralin 3**: Disenyuhin nang may transparensiya at kontrol ng user sa isip.
- **Aralin 4**: Ang mga tools ay ang "mga kamay" ng agent. Mahalaga ang schema definition para maintindihan ng LLM kung paano gagamitin ang mga ito.
- **Aralin 7**: Ang pagpaplano ay ang "executive function" ng agent, na nagbibigay-daan ito upang harapin ang mga kumplikadong workflow.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat aming pinagsisikapan ang katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling ginagawa ng tao. Hindi kami mananagot sa anumang maling pagkaunawa o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->