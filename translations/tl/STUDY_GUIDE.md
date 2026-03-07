# Mga AI Agent para sa mga Nagsisimula - Gabay sa Pag-aaral at Buod ng Kurso

Ang gabay na ito ay nagbibigay ng buod ng kursong "AI Agents for Beginners" at nagpapaliwanag ng mga mahahalagang konsepto, mga balangkas, at mga disenyo ng pattern para sa paggawa ng mga AI Agent.

## 1. Panimula sa AI Agents

**Ano ang AI Agents?**  
Ang mga AI Agent ay mga sistema na nagpapalawak ng kakayahan ng Large Language Models (LLMs) sa pamamagitan ng pagbibigay sa kanila ng access sa **mga kasangkapan**, **kaalaman**, at **memorya**. Hindi tulad ng karaniwang LLM chatbot na gumagawa lamang ng teksto base sa training data, ang isang AI Agent ay maaaring:  
- **Makita** ang kanyang kapaligiran (sa pamamagitan ng sensors o inputs).  
- **Mag-isip** kung paano lutasin ang isang problema.  
- **Gumawa ng aksyon** upang baguhin ang kapaligiran (sa pamamagitan ng actuators o pagpapatakbo ng kasangkapan).

**Mga Pangunahing Bahagi ng isang Agent:**  
- **Kapaligiran**: Ang lugar kung saan gumagana ang agent (hal., isang sistema ng booking).  
- **Sensors**: Mekanismo para mangalap ng impormasyon (hal., pagbabasa ng API).  
- **Actuators**: Mekanismo para magsagawa ng mga aksyon (hal., pagpapadala ng email).  
- **Utak (LLM)**: Ang engine ng pangangatwiran na nagpaplano at nagdedesisyon kung anong mga aksyon ang gagawin.

## 2. Agentic Frameworks

Ginagamit sa kurso ang **Microsoft Agent Framework (MAF)** kasama ang **Azure AI Foundry Agent Service V2** para sa paggawa ng mga agent:

| Komponent | Pokus | Pinakamainam Para sa |
|-----------|-------|----------------------|
| **Microsoft Agent Framework** | Pinagsamang Python/C# SDK para sa mga agent, kasangkapan, at workflows | Paggawa ng mga agent na may kasangkapan, multi-agent workflows, at mga pattern sa produksyon. |
| **Azure AI Foundry Agent Service** | Managed cloud runtime | Ligtas, scalable na deployment na may built-in na pamamahala ng estado, observability, at pagtitiwala. |

## 3. Agentic Design Patterns

Tinutulungan ng mga disenyo ng pattern ang istraktura kung paano gumana ang mga agent upang maayos na malutas ang mga problema.

### **Tool Use Pattern** (Aralin 4)  
Pinapayagan ng pattern na ito ang mga agent na makipag-ugnayan sa labas ng mundo.  
- **Konsepto**: Binibigyan ang agent ng "schema" (isang listahan ng mga available na function at ang kanilang mga parameter). Ang LLM ang nagdedesisyon *alin* na tool ang tatawagin at *anong* argumento ang gagamitin base sa hiling ng user.  
- **Daloy**: User Request -> LLM -> **Pagpili ng Kasangkapan** -> **Pagsasagawa ng Kasangkapan** -> LLM (na may output ng kasangkapan) -> Pangwakas na Tugon.  
- **Gamit**: Pagkuha ng real-time na data (panahon, presyo ng stock), paggawa ng kalkulasyon, pagpapatakbo ng code.

### **Planning Pattern** (Aralin 7)  
Pinapayagan ng pattern na ito ang mga agent na malutas ang mga kumplikado, multi-step na gawain.  
- **Konsepto**: Hinihiwa-hiwalay ng agent ang isang mataas na antas na layunin sa isang serye ng mas maliliit na subtask.  
- **Pamamaraan**:  
  - **Task Decomposition**: Hatiin ang "Planuhin ang trip" sa "Mag-book ng flight", "Mag-book ng hotel", "Umuupa ng sasakyan".  
  - **Iterative Planning**: Muling suriin ang plano base sa output ng mga naunang hakbang (hal., kung puno ang flight, pumili ng ibang petsa).  
- **Pagsasagawa**: Kadalasan ay may "Planner" agent na lumilikha ng istrakturadong plano (hal., JSON) na ipinatutupad ng ibang mga agent.

## 4. Mga Prinsipyo sa Disenyo

Kapag nagdidisenyo ng mga agent, isaalang-alang ang tatlong dimensyon:  
- **Space**: Dapat ikonekta ng mga agent ang mga tao at kaalaman, maging madaling lapitan ngunit hindi makagambala.  
- **Time**: Dapat matuto ang mga agent mula sa *Nakaraan*, magbigay ng angkop na paalala sa *Ngayon*, at mag-adapt para sa *Hinaharap*.  
- **Core**: Yakapin ang kawalang-katiyakan ngunit magtatag ng pagtitiwala sa pamamagitan ng transparency at kontrol ng user.

## 5. Buod ng mga Mahahalagang Aralin

- **Aralin 1**: Ang mga agent ay mga sistema, hindi lang mga modelo. Nakakakita, nag-iisip, at kumikilos sila.  
- **Aralin 2**: Pinapasimple ng Microsoft Agent Framework ang komplikasyon sa pagtawag ng kasangkapan at pamamahala ng estado.  
- **Aralin 3**: Disenyuhin nang may transparency at kontrol ng user sa isip.  
- **Aralin 4**: Ang mga kasangkapan ang "kamay" ng agent. Mahalaga ang depinisyon ng schema para maintindihan ng LLM kung paano gamitin ang mga ito.  
- **Aralin 7**: Ang pagpaplano ang "executive function" ng agent, na nagbibigay-daan dito upang harapin ang mga kumplikadong workflows.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pahayag ng Pagtanggi**:
Ang dokumentong ito ay isinalin gamit ang AI na serbisyo sa pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, pakatandaan na ang automated na pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring bilang pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot sa anumang pagkalito o maling pagkaunawa na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->