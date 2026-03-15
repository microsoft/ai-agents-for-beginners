[![Multi-Agent Design](../../../translated_images/tl/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

# Mga pattern ng disenyo para sa multi-agent

Sa sandaling magsimula kang magtrabaho sa isang proyekto na may kinalaman sa maraming ahente, kakailanganin mong isaalang-alang ang pattern ng disenyo para sa multi-agent. Gayunpaman, maaaring hindi agad malinaw kung kailan lilipat sa multi-agents at kung ano ang mga pakinabang nito.

## Panimula

Sa araling ito, layunin nating sagutin ang mga sumusunod na tanong:

- Ano ang mga senaryo kung saan naaangkop ang paggamit ng multi-agents?
- Ano ang mga pakinabang ng paggamit ng multi-agents kumpara sa isang nag-iisang ahente na gumagawa ng maraming gawain?
- Ano ang mga pundasyong bahagi ng pagpapatupad ng pattern ng disenyo para sa multi-agent?
- Paano natin makikita kung paano nag-iinteract ang mga maraming ahente sa isa't isa?

## Mga Layunin sa Pagkatuto

Pagkatapos ng araling ito, dapat mong magawa ang mga sumusunod:

- Tukuyin ang mga senaryong angkop para sa multi-agents
- Kilalanin ang mga pakinabang ng paggamit ng multi-agents kumpara sa isang nag-iisang ahente.
- Unawain ang mga pundasyong bahagi ng pagpapatupad ng pattern ng disenyo para sa multi-agent.

Ano ang mas malawak na larawan?

*Ang multi agents ay isang pattern ng disenyo na nagpapahintulot sa maraming ahente na magtulungan upang makamit ang isang karaniwang layunin*.

Malawak ang paggamit ng pattern na ito sa iba't ibang larangan, kabilang ang robotics, autonomous systems, at distributed computing.

## Mga Senaryo Kung Saan Naaangkop ang Multi-Agents

Ano nga ba ang mga senaryo na magandang gamitin ang multi-agents? Ang sagot ay marami ang mga senaryo kung saan kapaki-pakinabang ang paggamit ng maraming ahente lalo na sa mga sumusunod na kaso:

- **Malalaking gawain**: Maaaring hatiin ang malalaking gawain sa mas maliliit na bahagi at i-assign sa iba't ibang ahente, na nagpapahintulot ng sabayang pagproseso at mas mabilis na pagtatapos. Halimbawa nito ay sa kaso ng malawak na pagproseso ng datos.
- **Komplikadong gawain**: Tulad ng malalaking gawain, maaaring hatiin ang komplikadong gawain sa maliliit na sub-gawain at i-assign sa iba't ibang ahente, na ang bawat isa ay espesiyalista sa partikular na aspeto ng gawain. Halimbawa nito ay sa kaso ng mga autonomous vehicle kung saan ang iba't ibang ahente ang nagsasaayos ng navigation, obstacle detection, at komunikasyon sa ibang mga sasakyan.
- **Iba’t ibang espesyalisasyon**: Maaaring magkaroon ang iba't ibang ahente ng iba’t ibang kaalaman, na nagpapahintulot sa kanila na mas epektibong hawakan ang iba't ibang aspeto ng gawain kumpara sa isang ahente lamang. Halimbawa nito ay sa larangan ng pangangalagang pangkalusugan kung saan ang mga ahente ay maaaring mamahala ng diagnostics, mga plano sa paggamot, at monitoring ng pasyente.

## Mga Pakinabang ng Paggamit ng Multi-Agents Kumpara sa Isang Nag-iisang Ahente

Maaaring gumana nang maayos ang sistemang may isang ahente para sa mga simpleng gawain, ngunit para sa mas komplikadong mga gawain, ang paggamit ng maraming ahente ay nagbibigay ng ilang mga pakinabang:

- **Espesyalisasyon**: Ang bawat ahente ay maaaring maging espesiyalista para sa isang partikular na gawain. Ang kakulangan ng espesyalisasyon sa isang ahente ay nangangahulugan na maaari siyang magawa ang lahat ng bagay ngunit maaaring malito kung ano ang dapat gawin sa harap ng komplikadong gawain. Halimbawa, maaaring magtapos ito sa paggawa ng gawain na hindi niya pinakamahusay na kinaya.
- **Scalability**: Mas madali ang pag-scale ng mga sistema sa pamamagitan ng pagdagdag ng mas maraming ahente kaysa sa pagpapasan ng labis sa isang ahente.
- **Fault Tolerance**: Kung may isang ahente na pumalya, ang ibang ahente ay maaaring magpatuloy sa pag-andar, na tinitiyak ang pagiging maaasahan ng sistema.

Halimbawa, subukan nating mag-book ng biyahe para sa isang user. Ang sistemang may isang ahente ay kailangang pangasiwaan ang lahat ng aspeto ng proseso ng pag-book ng biyahe, mula sa paghahanap ng mga flight hanggang sa pag-book ng hotel at mga rental na sasakyan. Para makamit ito ng isang ahente, kailangan niyang magkaroon ng mga kasangkapan para hawakan ang lahat ng mga gawain na ito. Maaari itong humantong sa isang kumplikado at monolitikong sistema na mahirap panatilihin at i-scale. Sa kabilang banda, ang sistema ng multi-agent ay maaaring magkaroon ng iba't ibang ahente na espesiyalista sa paghahanap ng mga flight, pag-book ng mga hotel, at mga rental na sasakyan. Ginagawa nitong mas modular, mas madaling panatilihin, at mas scalable ang sistema.

Ihambing ito sa isang travel bureau na pinatatakbo bilang isang mom-and-pop store kumpara sa isang travel bureau na pinatatakbo bilang isang prangkisa. Ang mom-and-pop store ay magkakaroon ng isang ahente na humahawak sa lahat ng aspeto ng proseso ng pag-book ng biyahe, samantalang ang prangkisa ay magkakaroon ng iba't ibang ahente na humahawak sa iba't ibang aspeto ng proseso ng pag-book ng biyahe.

## Mga Pundasyon ng Pagpapatupad ng Pattern ng Disenyo para sa Multi-Agent

Bago mo maipatupad ang pattern ng disenyo para sa multi-agent, kailangan mong maunawaan ang mga pundasyong bahagi na bumubuo sa pattern.

Gawing mas tiyak ito sa pamamagitan ng muling pagtingin sa halimbawa ng pag-book ng biyahe para sa isang user. Sa kasong ito, ang mga pundasyong bahagi ay kinabibilangan ng:

- **Komunikasyon ng Ahente**: Ang mga ahente para sa paghahanap ng mga flight, pag-book ng mga hotel, at mga rental na sasakyan ay kailangang makipag-ugnayan at magbahagi ng impormasyon tungkol sa mga kagustuhan at limitasyon ng user. Kailangan mong magpasya sa mga protocol at pamamaraan para sa komunikasyong ito. Ibig sabihin nito nang konkretong ang ahente para sa paghahanap ng mga flight ay kailangang makipag-ugnayan sa ahente para sa pag-book ng mga hotel upang matiyak na ang hotel ay naka-book para sa parehong mga petsa tulad ng flight. Nangangahulugan ito na kailangang magbahagi ang mga ahente ng impormasyon tungkol sa mga petsa ng paglalakbay ng user, kung kaya kailangan mong magpasya *kung alin ang mga ahente na nagbabahagi ng impormasyon at kung paano nila ito ibinabahagi*.
- **Mga Mekanismo ng Koordinasyon**: Kailangang mag-coordinate ang mga ahente sa kanilang mga aksyon upang matiyak na natutugunan ang mga kagustuhan at limitasyon ng user. Ang kagustuhan ng user ay maaaring nais nila ng hotel na malapit sa airport samantalang ang limitasyon naman ay na ang mga rental na sasakyan ay makukuha lamang sa airport. Nangangahulugan ito na kailangang mag-coordinate ang ahente para sa pag-book ng mga hotel sa ahente para sa pag-book ng mga rental na sasakyan upang matiyak na natutugunan ang mga kagustuhan at limitasyon ng user. Nangangahulugan ito na kailangan mong magpasya *kung paano nagko-coordinate ang mga ahente ng kanilang mga aksyon*.
- **Arkitektura ng Ahente**: Kailangang magkaroon ang mga ahente ng panloob na estruktura upang makagawa ng mga desisyon at matuto mula sa kanilang interaksyon sa user. Nangangahulugan ito na kailangang magkaroon ang ahente para sa paghahanap ng mga flight ng panloob na estruktura upang gumawa ng mga desisyon kung aling mga flight ang ire-rekomenda sa user. Nangangahulugan ito na kailangan mong magpasya *kung paano gumagawa ng desisyon ang mga ahente at kung paano sila natututo mula sa kanilang interaksyon sa user*. Halimbawa kung paano natututo at nagpapabuti ang isang ahente ay maaaring ang ahente para sa paghahanap ng mga flight ay gumamit ng machine learning model upang magrekomenda ng mga flight batay sa mga dating kagustuhan ng user.
- **Kakayahang Makita ang Mga Interaksyon ng Multi-Agent**: Kailangan mong magkaroon ng kakayahan na makita kung paano nag-iinteract ang maraming ahente sa isa't isa. Nangangahulugan ito na kailangan mong magkaroon ng mga kagamitan at pamamaraan para subaybayan ang mga gawain at interaksyon ng ahente. Maaaring ito ay sa anyo ng mga logging at monitoring tools, visualization tools, at mga performance metrics.
- **Mga Pattern ng Multi-Agent**: Mayroong iba't ibang mga pattern sa pagpapatupad ng mga sistema ng multi-agent, tulad ng centralized, decentralized, at hybrid na mga arkitektura. Kailangan mong pumili ng pattern na pinakaangkop sa iyong kaso.
- **Tao sa Loop**: Sa karamihan ng mga kaso, mayroong tao sa loop at kailangan mong gabayan ang mga ahente kung kailan humingi ng interbensyon mula sa tao. Maaaring ito ay sa anyo ng user na humihingi ng partikular na hotel o flight na hindi ni-rekomenda ng mga ahente o humihingi ng kumpirmasyon bago mag-book ng flight o hotel.

## Kakayahang Makita ang Mga Interaksyon ng Multi-Agent

Mahalaga na mayroon kang kakayahang makita kung paano nag-iinteract ang maraming ahente sa isa't isa. Ang kakayahang ito ay mahalaga para sa debugging, pag-optimize, at pagtitiyak ng kahusayan ng buong sistema. Upang magawa ito, kailangan mong magkaroon ng mga kagamitan at teknik para subaybayan ang mga gawain at interaksyon ng mga ahente. Maaaring ito ay sa anyo ng mga logging at monitoring tools, visualization tools, at mga performance metrics.

Halimbawa, sa kaso ng pag-book ng biyahe para sa isang user, maaari kang magkaroon ng dashboard na nagpapakita ng status ng bawat ahente, ang mga kagustuhan at limitasyon ng user, at ang mga interaksyon sa pagitan ng mga ahente. Ang dashboard na ito ay maaaring magpakita ng mga petsa ng paglalakbay ng user, ang mga flight na nirerekomenda ng flight agent, mga hotel na nirerekomenda ng hotel agent, at mga rental car na nirerekomenda ng rental car agent. Magbibigay ito ng malinaw na pananaw kung paano nag-iinteract ang mga ahente sa isa't isa at kung natutugunan ba ng mga ito ang mga kagustuhan at limitasyon ng user.

Tingnan natin nang mas detalyado ang bawat aspeto.

- **Mga Kagamitan sa Logging at Monitoring**: Nais mong magkaroon ng logging para sa bawat aksyon na ginawa ng isang ahente. Ang log entry ay maaaring mag-imbak ng impormasyon tungkol sa ahente na gumawa ng aksyon, ang ginawa nitong aksyon, oras ng aksyon, at resulta ng aksyon. Ang impormasyong ito ay maaaring gamitin para sa pag-debug, pag-optimize, at iba pa.
- **Mga Kagamitan sa Visualisasyon**: Makakatulong ang visualization tools upang makita mo ang mga interaksyon sa pagitan ng mga ahente sa mas madaling paraan. Halimbawa, maaari kang magkaroon ng graph na nagpapakita ng daloy ng impormasyon sa pagitan ng mga ahente. Makakatulong ito upang makita ang mga pagsisikip, hindi epektibong bahagi, at iba pang mga isyu sa sistema.
- **Mga Sukatan ng Performance**: Matutulungan ka ng performance metrics na subaybayan ang kahusayan ng multi-agent system. Halimbawa, maaari mong subaybayan ang oras na kinakailangan upang matapos ang isang gawain, ang bilang ng mga gawain na natapos bawat yunit ng oras, at ang katumpakan ng mga rekomendasyong ibinigay ng mga ahente. Magbibigay ang impormasyong ito ng ideya kung saan kailangan ng pagpapabuti at paano mai-optimize ang sistema.

## Mga Pattern ng Multi-Agent

Tingnan natin ang ilang mga kongkretong pattern na maaari nating gamitin upang gumawa ng multi-agent apps. Narito ang ilang mga interesting na pattern na dapat isaalang-alang:

### Group chat

Kapaki-pakinabang ang pattern na ito kapag gusto mong gumawa ng aplikasyon ng group chat kung saan maraming ahente ang maaaring makipagkomunikasyon sa isa't isa. Karaniwang gamit nito ay para sa team collaboration, customer support, at social networking.

Sa pattern na ito, bawat ahente ay kumakatawan sa isang user sa group chat, at nagpapalitan ng mga mensahe sa pagitan ng mga ahente gamit ang messaging protocol. Maaaring magpadala ng mga mensahe ang mga ahente sa group chat, tumanggap ng mga mensahe mula sa group chat, at tumugon sa mga mensahe mula sa ibang mga ahente.

Maaaring ipatupad ang pattern na ito gamit ang centralized architecture kung saan lahat ng mga mensahe ay dumadaan sa isang central server, o decentralized architecture kung saan ang mga mensahe ay nagpapalitan nang diretso.

![Group chat](../../../translated_images/tl/multi-agent-group-chat.ec10f4cde556babd.webp)

### Hand-off

Kapaki-pakinabang ang pattern na ito kapag gusto mong gumawa ng aplikasyon kung saan maraming ahente ay maaaring magpasa-pasahan ng mga gawain sa isa't isa.

Karaniwang gamit nito ay sa customer support, task management, at workflow automation.

Sa pattern na ito, bawat ahente ay kumakatawan sa isang gawain o hakbang sa workflow, at maaari silang magpasa ng mga gawain sa ibang mga ahente base sa mga paunang itinakdang patakaran.

![Hand off](../../../translated_images/tl/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Collaborative filtering

Kapaki-pakinabang ang pattern na ito kapag gusto mong gumawa ng aplikasyon kung saan maraming ahente ang maaaring magtulungan upang gumawa ng mga rekomendasyon para sa mga user.

Bakit mo gustong magtulungan ang maraming ahente ay dahil maaaring may iba’t ibang espesyalisasyon ang bawat ahente at maaaring mag-ambag sa proseso ng rekomendasyon sa iba't ibang paraan.

Halimbawa, isang user ay nais ng rekomendasyon tungkol sa pinakamagandang stock na bibilhin sa stock market.

- **Eksperto sa industriya**: Isang ahente ay maaaring maging eksperto sa isang partikular na industriya.
- **Teknikal na pagsusuri**: Ang isa pang ahente ay maaaring eksperto sa teknikal na pagsusuri.
- **Fundamental na pagsusuri**: At ang isa pang ahente ay maaaring eksperto sa fundamental na pagsusuri. Sa pamamagitan ng pagtutulungan, maaaring magbigay ang mga ahenteng ito ng mas kumpleto at komprehensibong rekomendasyon sa user.

![Recommendation](../../../translated_images/tl/multi-agent-filtering.d959cb129dc9f608.webp)

## Senaryo: Proseso ng Refund

Isipin ang isang senaryo kung saan ang isang customer ay nagpapasuhan ng refund para sa isang produkto, maaaring marami ang mga ahente na kasali sa prosesong ito ngunit hatiin natin sa pagitan ng mga ahente na espesipiko para sa prosesong ito at mga pangkalahatang ahente na maaaring gamitin sa iba pang mga proseso.

**Mga ahenteng espesipiko para sa proseso ng refund**:

Narito ang ilang mga ahente na maaaring kasangkot sa proseso ng refund:

- **Ahente ng Customer**: Ang ahenteng ito ay kumakatawan sa customer at responsable sa pagsisimula ng proseso ng refund.
- **Ahente ng Nagbebenta**: Ang ahenteng ito ay kumakatawan sa nagbebenta at responsable sa pagproseso ng refund.
- **Ahente ng Bayad**: Ang ahenteng ito ay kumakatawan sa proseso ng pagbabayad at responsable sa pag-refund ng bayad ng customer.
- **Ahente ng Resolusyon**: Ang ahenteng ito ay kumakatawan sa proseso ng resolusyon at responsable sa paglutas ng anumang mga isyu na lumitaw sa panahon ng proseso ng refund.
- **Ahente ng Pagsunod**: Ang ahenteng ito ay kumakatawan sa proseso ng pagsunod at responsable sa pagtitiyak na ang proseso ng refund ay sumusunod sa mga regulasyon at patakaran.

**Pangkalahatang mga ahente**:

Ang mga ahenteng ito ay maaaring gamitin ng iba pang bahagi ng iyong negosyo.

- **Ahente ng Pagpapadala**: Ang ahenteng ito ay kumakatawan sa proseso ng pagpapadala at responsable sa pagpapadala ng produkto pabalik sa nagbebenta. Maaaring gamitin ang ahenteng ito para sa parehong proseso ng refund at para sa pangkalahatang pagpapadala ng isang produkto sa pamamagitan ng pagbili, halimbawa.
- **Ahente ng Feedback**: Ang ahenteng ito ay kumakatawan sa proseso ng pagkolekta ng feedback mula sa customer. Maaaring mangyari ang feedback sa anumang oras at hindi lamang sa panahon ng proseso ng refund.
- **Ahente ng Eskalasyon**: Ang ahenteng ito ay kumakatawan sa proseso ng eskalasyon at responsable sa pag-angat ng mga isyu sa mas mataas na antas ng suporta. Maaaring gamitin ang ganitong uri ng ahente para sa anumang proseso kung saan kailangan mong mag-eskala ng isyu.
- **Ahente ng Notification**: Ang ahenteng ito ay kumakatawan sa proseso ng pagpapadala ng mga notification at responsable sa pagpapadala ng mga abiso sa customer sa iba't ibang yugto ng proseso ng refund.
- **Ahente ng Analytics**: Ang ahenteng ito ay kumakatawan sa proseso ng pagsusuri at responsable sa pagsusuri ng data na may kaugnayan sa proseso ng refund.
- **Ahente ng Audit**: Ang ahenteng ito ay kumakatawan sa proseso ng pag-audit at responsable sa pag-audit ng proseso ng refund upang matiyak na ito ay isinasagawa nang tama.
- **Ahente ng Reporting**: Ang ahenteng ito ay kumakatawan sa proseso ng pag-uulat at responsable sa paggawa ng mga ulat tungkol sa proseso ng refund.
- **Ahente ng Kaalaman**: Ang ahenteng ito ay kumakatawan sa proseso ng kaalaman at responsable sa pagpapanatili ng isang knowledge base ng impormasyon na may kaugnayan sa proseso ng refund. Ang ahenteng ito ay maaaring may kaalaman sa parehong mga refund at iba pang bahagi ng iyong negosyo.
- **Ahente ng Seguridad**: Ang ahenteng ito ay kumakatawan sa proseso ng seguridad at responsable sa pagtitiyak ng seguridad ng proseso ng refund.
- **Ahente ng Kalidad**: Ang ahenteng ito ay kumakatawan sa proseso ng kalidad at responsable sa pagtitiyak ng kalidad ng proseso ng refund.

Maraming mga ahente ang nakalista sa itaas, kapwa para sa espesipikong proseso ng refund at para sa pangkalahatang mga ahente na maaaring gamitin sa ibang bahagi ng iyong negosyo. Sana ay mabigyan ka nito ng ideya kung paano ka makakapagpasya kung aling mga ahente ang gagamitin sa iyong multi-agent system.

## Takdang Aralin

Magdisenyo ng multi-agent system para sa proseso ng customer support. Tukuyin ang mga ahenteng kasali sa proseso, ang kanilang mga papel at responsibilidad, at kung paano sila nag-iinteract sa isa't isa. Isaalang-alang ang parehong mga ahenteng espesipiko sa proseso ng customer support at mga pangkalahatang ahente na maaaring gamitin sa ibang bahagi ng iyong negosyo.
> Mag-isip muna bago basahin ang sumusunod na solusyon, maaaring kailanganin mo ang mas maraming ahente kaysa sa inaakala mo.

> TIP: Isipin ang iba't ibang yugto ng proseso ng customer support at isaalang-alang din ang mga ahenteng kailangan para sa anumang sistema.

## Solution

[Solution](./solution/solution.md)

## Knowledge checks

Question: Kailan mo dapat isaalang-alang ang paggamit ng multi-agents?

- [ ] A1: Kapag maliit ang iyong workload at simple ang gawain.
- [ ] A2: Kapag malaki ang iyong workload
- [ ] A3: Kapag simple ang iyong gawain.

[Solution quiz](./solution/solution-quiz.md)

## Summary

Sa araling ito, tiningnan natin ang multi-agent design pattern, kabilang ang mga sitwasyong maaaring gamitin ang multi-agents, ang mga benepisyo ng paggamit ng multi-agents kaysa sa isang ahente lamang, ang mga batayang bahagi ng pag-implementa ng multi-agent design pattern, at kung paano makita kung paano nag-iinteract ang maraming ahente sa isa't isa.

### Mayroon Ka Pang Mga Tanong tungkol sa Multi-Agent Design Pattern?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) upang makihalubilo sa ibang mga nag-aaral, dumalo sa office hours, at makakuha ng mga sagot sa iyong mga tanong tungkol sa AI Agents.

## Additional resources

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework documentation</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentic design patterns</a>


## Previous Lesson

[Planning Design](../07-planning-design/README.md)

## Next Lesson

[Metacognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI na serbisyo sa pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-katiyakan. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->