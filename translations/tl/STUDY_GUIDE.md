# Mga AI Agent para sa Mga Nagsisimula - Gabay sa Pag-aaral at Buod ng Kurso

Ang gabay na ito ay naglalaman ng buod ng kurso na "AI Agents for Beginners" at nagpapaliwanag ng mga pangunahing konsepto, framework, at disenyo ng pattern para sa pagbuo ng mga AI Agent.

## 1. Panimula sa AI Agents

**Ano ang AI Agents?**  
Ang AI Agents ay mga sistema na nagpapalawak ng kakayahan ng Large Language Models (LLMs) sa pamamagitan ng pagbibigay sa kanila ng access sa **mga kasangkapan**, **kaalaman**, at **memorya**. Hindi tulad ng isang karaniwang LLM chatbot na gumagawa lamang ng teksto batay sa data ng pagsasanay, ang AI Agent ay kaya:  
- **Makaramdam** sa kanyang kapaligiran (sa pamamagitan ng mga sensor o input).  
- **Magsagawa ng pangangatwiran** kung paano lutasin ang isang problema.  
- **Kumilos** upang baguhin ang kapaligiran (sa pamamagitan ng mga actuator o pagpapatupad ng kasangkapan).

**Pangunahing Bahagi ng isang Agent:**  
- **Kapaligiran**: Ang espasyong pinaglilingkuran ng agent (hal., isang booking system).  
- **Mga Sensor**: Mekanismo para kumuha ng impormasyon (hal., pagbabasa ng API).  
- **Mga Actuator**: Mekanismo para magsagawa ng mga aksyon (hal., pagpapadala ng email).  
- **Utak (LLM)**: Ang engine ng pangangatwiran na nagpaplano at nagpapasya kung anong mga aksyon ang gagawin.

## 2. Agentic Frameworks

Tinutukoy sa kurso ang tatlong pangunahing framework para sa pagbuo ng mga agent:

| Framework | Pokus | Pinakamainam Para sa |
|-----------|-------|-----------------------|
| **Semantic Kernel** | Produktion-ready SDK para sa .NET/Python | Mga enterprise na aplikasyon, pagsasama ng AI sa kasalukuyang code. |
| **AutoGen** | Multi-agent collaboration | Masalimuot na senaryo na nangangailangan ng maraming espesyalistang agent na nag-uusap. |
| **Azure AI Agent Service** | Managed cloud service | Ligtas, scalable na deployment na may built-in na pamamahala ng estado. |

## 3. Agentic Design Patterns

Ang mga design pattern ay tumutulong sa pag-istruktura kung paano tumatakbo ang mga agent para maayos na malutas ang mga problema.

### **Tool Use Pattern** (Lesson 4)  
Pinapayagan ng pattern na ito ang mga agent na makipag-interact sa labas na mundo.  
- **Konsepto**: Binibigyan ang agent ng "schema" (isang listahan ng mga magagamit na function at kanilang mga parameter). Ang LLM ang nagpapasya *alin* na kasangkapan ang tatawagin at *ano* ang mga argumento base sa kahilingan ng user.  
- **Daloy**: Kahilingan ng User -> LLM -> **Pagpili ng Kasangkapan** -> **Pagpapatupad ng Kasangkapan** -> LLM (kasama ang output ng kasangkapan) -> Pangwakas na Tugon.  
- **Mga Gamit**: Pagkuha ng data sa real-time (panahon, presyo ng stock), pagsasagawa ng kalkulasyon, pagpapatakbo ng code.

### **Planning Pattern** (Lesson 7)  
Pinapayagan ng pattern na ito ang mga agent na malutas ang masalimuot, maraming hakbang na gawain.  
- **Konsepto**: Hinahati ng agent ang mataas na layunin sa isang sunud-sunod na mga mas maliit na subtasks.  
- **Mga Pamamaraan**:  
  - **Task Decomposition**: Hatiin ang "Planuhin ang paglalakbay" sa "Mag-book ng flight", "Mag-book ng hotel", "Mag-renta ng sasakyan".  
  - **Iterative Planning**: Muling sinusuri ang plano base sa output ng mga naunang hakbang (hal., kung puno na ang flight, pumili ng ibang petsa).  
- **Pagpapatupad**: Kadalasang ginagamit ang isang "Planner" agent na bumubuo ng nakaistrukturang plano (hal., JSON) na pagkatapos ay isinasagawa ng ibang mga agent.

## 4. Mga Prinsipyo sa Disenyo

Kapag nagdidisenyo ng mga agent, isaalang-alang ang tatlong dimensyon:  
- **Espasyo**: Dapat magdugtong ang mga agent ng mga tao at kaalaman, maging madaling ma-access ngunit hindi nakakainis.  
- **Oras**: Dapat matuto ang mga agent mula sa *Nakaraan*, magbigay ng makabuluhang pagtutok sa *Ngayon*, at mag-adapt para sa *Hinaharap*.  
- **Puso (Core)**: Yakapin ang kawalang-katiyakan ngunit magtatag ng tiwala sa pamamagitan ng transparency at kontrol ng user.

## 5. Buod ng mga Pangunahing Aral

- **Leksyon 1**: Ang mga agent ay mga sistema, hindi lang mga modelo. Nakakaramdam, nakapagpapangatuwiran, at kumikilos sila.  
- **Leksyon 2**: Ang mga framework tulad ng Semantic Kernel at AutoGen ay nag-a-abstract ng pagiging kumplikado ng pagtawag sa kasangkapan at pamamahala ng estado.  
- **Leksyon 3**: Disenyuhin nang may transparency at kontrol ng user sa isip.  
- **Leksyon 4**: Ang mga kasangkapan ang "mga kamay" ng agent. Mahalagang maayos ang schema upang maunawaan ng LLM kung paano ito gagamitin.  
- **Leksyon 7**: Ang pagpaplano ang "executive function" ng agent, na nagpapahintulot dito na harapin ang masalimuot na mga workflow.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mga mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling tao. Hindi kami mananagot sa anumang mga maling pagkaunawa o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->