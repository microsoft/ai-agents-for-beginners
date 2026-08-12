[![Multi-Agent Design](../../../translated_images/tl/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(I-click ang larawan sa itaas upang mapanood ang video ng leksyon na ito)_

# Mga disenyo ng multi-agent

Sa sandaling mag-umpisa kang magtrabaho sa isang proyekto na may kinalaman sa maraming agent, kakailanganin mong isaalang-alang ang disenyo ng multi-agent. Gayunpaman, maaaring hindi agad malinaw kung kailan lilipat sa multi-agent at kung ano ang mga bentahe nito.

## Panimula

Sa araling ito, nais naming sagutin ang mga sumusunod na tanong:

- Ano ang mga senaryo kung saan ang mga multi-agent ay naaangkop?
- Ano ang mga bentahe ng paggamit ng mga multi-agent kumpara sa isang singular na agent na gumagawa ng maraming gawain?
- Ano ang mga pangunahing bagay sa pagpapatupad ng disenyo ng multi-agent?
- Paano natin makikita kung paano nag-iinteract ang maraming agent sa isa't isa?

## Mga Layunin sa Pagkatuto

Pagkatapos ng araling ito, dapat mong magawa ang mga sumusunod:

- Tukuyin ang mga senaryo kung saan naaangkop ang mga multi-agent
- Kilalanin ang mga bentahe ng paggamit ng mga multi-agent kumpara sa isang singular na agent.
- Mauunawaan ang mga pangunahing bagay sa pagpapatupad ng disenyo ng multi-agent.

Ano ang mas malaking larawan?

*Ang mga multi-agent ay isang disenyo na nagpapahintulot sa maraming agent na magtulungan upang makamit ang isang pangkaraniwang layunin*.

Ang pattern na ito ay malawakang ginagamit sa iba't ibang larangan, kabilang ang robotics, autonomous systems, at distributed computing.

## Mga Senaryo Kung Saan Naaangkop ang Multi-Agent

Kaya ano ang mga senaryo na magandang gamitin para sa mga multi-agent? Ang sagot ay maraming senaryo kung saan kapaki-pakinabang ang pag-employ ng maraming agent lalo na sa mga sumusunod na kaso:

- **Malalaking gawain**: Ang malalaking gawain ay maaaring hatiin sa mas maliliit na gawain at ibigay sa iba't ibang agent, na nagpapahintulot ng parallel processing at mas mabilis na pagkompleto. Halimbawa nito ay sa malalaking gawain sa pagproseso ng data.
- **Kumplikadong gawain**: Tulad ng malalaking gawain, ang mga kumplikadong gawain ay maaaring hatiin sa mas maliliit na subtasks at ibigay sa iba't ibang agent, bawat isa ay dalubhasa sa isang partikular na aspeto ng gawain. Isang magandang halimbawa nito ay sa autonomous na mga sasakyan kung saan ang iba't ibang agent ay namamahala sa navigation, pag-detect ng hadlang, at komunikasyon sa ibang mga sasakyan.
- **Iba't ibang kaalaman**: Ang iba't ibang agent ay maaaring may iba't ibang espesyalisasyon, na nagpapahintulot sa kanila na hawakan ang iba't ibang aspeto ng gawain nang mas epektibo kaysa sa isang agent lang. Isang magandang halimbawa nito ay sa healthcare kung saan ang mga agent ay namamahala sa diagnostics, mga plano sa paggamot, at pagmamanman ng pasyente.

## Mga Bentahe ng Paggamit ng Multi-Agent Kumpara sa Isang Singular na Agent

Maaaring gumana nang maayos ang isang system na may isang agent para sa simpleng mga gawain, ngunit sa mas kumplikadong mga gawain, ang paggamit ng maraming agent ay maaaring magbigay ng ilang mga bentahe:

- **Espesyalisasyon**: Ang bawat agent ay maaaring maging dalubhasa sa isang partikular na gawain. Ang kakulangan sa espesyalisasyon ng isang agent lang ay nangangahulugan na meron kang agent na kayang gawin ang lahat ngunit maaaring malito kung ano ang gagawin kapag naharap sa kumplikadong gawain. Halimbawa, maaaring gawin nito ang isang gawain na hindi ito angkop.
- **Scalability**: Mas madali ang pag-scale ng mga system sa pamamagitan ng pagdagdag ng mas maraming agent kaysa sa pagbibigay ng sobrang trabaho sa isang agent lang.
- **Fault Tolerance**: Kung may isang agent na pumalya, ang iba ay maaaring magpatuloy sa paggana, na tinitiyak ang pagiging maaasahan ng system.

Magbigay tayo ng halimbawa, mag-book tayo ng biyahe para sa isang user. Ang isang system na may isang agent lang ay kailangang hawakan ang lahat ng aspeto ng proseso ng pagbu-book ng biyahe, mula sa paghahanap ng mga flight hanggang sa pagbu-book ng mga hotel at rental car. Para magawa ito ng isang agent lang, kailangan nitong may mga tool para hawakan lahat ng mga gawain na ito. Maaari itong magresulta sa isang komplikado at monolithic na system na mahirap pangalagaan at i-scale. Sa kabilang banda, ang multi-agent system ay maaaring may iba't ibang agent na dalubhasa sa paghahanap ng flight, pagbu-book ng hotel, at pagbu-book ng rental car. Ginagawa nitong mas modular, mas madaling alagaan, at scalable ang system.

Ihambing ito sa isang travel bureau na pinapatakbo ng mom-and-pop store versus isang travel bureau na pinapatakbo bilang franchise. Sa mom-and-pop store, isang agent lang ang humahawak sa lahat ng aspeto ng proseso ng pagbu-book ng biyahe, habang sa franchise ay may iba't ibang agent na humahawak sa iba't ibang aspeto ng proseso.

## Mga Pangunahing Bahagi ng Pagpapatupad ng Disenyo ng Multi-Agent

Bago ka makapagpatupad ng disenyo ng multi-agent, kailangan mong maunawaan ang mga pangunahing bahagi na bumubuo sa disenyo.

Gawing mas konkretong muli ang halimbawa ng pagbu-book ng biyahe para sa isang user. Sa kasong ito, kabilang sa mga pangunahing bahagi ang:

- **Komunikasyon ng Agent**: Ang mga agent para sa paghahanap ng mga flight, pagbu-book ng hotel, at rental car ay kailangang magkomunikasyon at magbahagi ng impormasyon tungkol sa mga kagustuhan at limitasyon ng user. Kailangan mong magdesisyon sa mga protocol at paraan para sa komunikasyong ito. Kongkretong ibig sabihin nito, ang agent para sa paghahanap ng flight ay kailangang makipag-ugnayan sa agent para sa pagbu-book ng hotel upang matiyak na ang hotel ay na-book para sa parehong mga petsa ng flight. Ibig sabihin nito, kailangan magbahagi ang mga agent ng impormasyon tungkol sa mga petsa ng paglalakbay ng user, kaya kailangan mong magdesisyon *alin sa mga agent ang magbabahagi ng impormasyon at paano nila ito ibinabahagi*.
- **Mga Mekanismo ng Koordinasyon**: Kailangan mag-coordinate ang mga agent ng kanilang mga aksyon upang matiyak na ang mga kagustuhan at limitasyon ng user ay natutugunan. Maaaring gusto ng user na malapit ang hotel sa airport samantalang ang limitasyon naman ay na ang mga rental car ay available lang sa airport. Ibig sabihin nito, kailangang makipag-coordinate ang agent para sa pagbu-book ng hotel sa agent para sa pagbu-book ng rental car upang matiyak na natutugunan ang mga kagustuhan at limitasyon ng user. Kaya kailangan mong magdesisyon *kung paano nagko-coordinate ang mga agent sa kanilang mga aksyon*.
- **Arkitektura ng Agent**: Kailangang may internal na istruktura ang mga agent upang makagawa ng desisyon at matuto mula sa kanilang interaksyon sa user. Ibig sabihin, ang agent para sa paghahanap ng flight ay kailangang magkaroon ng internal na istruktura upang makagawa ng desisyon kung aling mga flight ang irekomenda sa user. Kaya kailangan mong magdesisyon *kung paano gumagawa ng desisyon at natututo ang mga agent mula sa kanilang interaksyon sa user*. Halimbawa kung paano natututo at nagpapabuti ang isang agent ay maaaring ang agent para sa paghahanap ng flight ay gumamit ng modelo ng machine learning upang magrekomenda ng mga flight sa user base sa kanilang mga nakaraang kagustuhan.
- **Pagkakita sa mga Interaksyon ng Multi-Agent**: Kailangan mong makita kung paano nag-iinteract ang maraming agent sa isa't isa. Ibig sabihin, kailangan mong magkaroon ng mga tool at teknik para sa pagsubaybay sa mga aktibidad at interaksyon ng agent. Maaari itong anyo ng logging at monitoring tools, visualization tools, at performance metrics.
- **Mga Pattern ng Multi-Agent**: May iba't ibang pattern para sa pagpapatupad ng mga multi-agent system, gaya ng centralized, decentralized, at hybrid na arkitektura. Kailangan mong magdesisyon sa pattern na pinaka-akma sa iyong use case.
- **Human in the loop**: Karamihan sa mga kaso, may tao sa proseso at kailangan mong turuan ang mga agent kung kailan hihingi ng papasok ng tao. Maaaring ito ay nasa anyo ng user na humihingi ng partikular na hotel o flight na hindi ni-rekomenda ng mga agent, o humihingi ng kumpirmasyon bago mag-book ng flight o hotel.

## Pagkakita sa mga Interaksyon ng Multi-Agent

Mahalaga na makita mo kung paano nag-iinteract ang maraming agent sa isa't isa. Ang pagkakakita na ito ay mahalaga para sa pag-debug, pag-optimize, at pagtitiyak ng kabuuang bisa ng system. Para magawa ito, kailangan mong magkaroon ng mga tool at teknik para sa pagsubaybay sa mga aktibidad at interaksyon ng agent. Maaari itong anyo ng logging at monitoring tools, visualization tools, at performance metrics.

Halimbawa, sa kaso ng pagbu-book ng biyahe para sa user, maaari kang magkaroon ng dashboard na nagpapakita ng estado ng bawat agent, ang mga kagustuhan at limitasyon ng user, at ang mga interaksyon sa pagitan ng mga agent. Maaaring ipakita ng dashboard na ito ang mga petsa ng paglalakbay ng user, ang mga flight na nirerekomenda ng flight agent, ang mga hotel na nirerekomenda ng hotel agent, at ang mga rental car na nirerekomenda ng rental car agent. Magbibigay ito ng malinaw na tanawin kung paano nag-iinteract ang mga agent at kung natutugunan ba ang mga kagustuhan at limitasyon ng user.

Tingnan natin nang mas detalyado ang bawat isa sa mga aspetong ito.

- **Mga Tool sa Logging at Monitoring**: Gusto mong magkaroon ng logging para sa bawat aksyon na ginawa ng isang agent. Ang isang entry ng log ay maaaring magtala ng impormasyon tungkol sa agent na gumawa ng aksyon, ang aksyong ginawa, ang oras ng aksyon, at ang resulta ng aksyon. Maaari itong magamit para sa pag-debug, pag-optimize, at iba pa.

- **Mga Tool sa Visualization**: Makakatulong ang mga visualization tool na makita mo ang interaksyon sa pagitan ng mga agent sa isang mas madaling intindihin na paraan. Halimbawa, maaari kang magkaroon ng grap na nagpapakita ng daloy ng impormasyon sa pagitan ng mga agent. Makakatulong ito na matukoy ang mga bottleneck, kahinaan, at ibang problema sa system.

- **Mga Metric sa Performance**: Makakatulong ang performance metrics na subaybayan ang bisa ng multi-agent system. Halimbawa, maaari mong subaybayan ang oras na ginugol upang matapos ang gawain, ang bilang ng mga gawaing natapos sa bawat yunit ng oras, at ang katumpakan ng mga rekomendasyong ginawa ng mga agent. Makakatulong ang impormasyong ito na tukuyin ang mga lugar na dapat pagbutihin at i-optimize ang system.

## Mga Pattern ng Multi-Agent

Tignan natin ang ilang konkretong pattern na maaari nating gamitin para gumawa ng mga multi-agent na apps. Narito ang ilang mga kawili-wiling pattern na dapat isaalang-alang:

### Group chat

Ang pattern na ito ay kapaki-pakinabang kapag gusto mong gumawa ng group chat application kung saan maraming agent ang maaaring magkomunikasyon sa isa't isa. Karaniwang gamit sa pattern na ito ay para sa pakikipagtulungan ng team, suporta sa customer, at social networking.

Sa pattern na ito, bawat agent ay kumakatawan sa isang user sa group chat, at ang mga mensahe ay ipinapadala sa pagitan ng mga agent gamit ang messaging protocol. Maaari magpadala ang mga agent ng mga mensahe sa group chat, tumanggap ng mga mensahe mula sa group chat, at tumugon sa mga mensahe mula sa ibang agent.

Maaaring ipatupad ang pattern na ito gamit ang centralized na arkitektura kung saan lahat ng mensahe ay pinaparating sa isang central server, o isang decentralized na arkitektura kung saan direktang ipinagpapalitan ang mga mensahe.

![Group chat](../../../translated_images/tl/multi-agent-group-chat.ec10f4cde556babd.webp)

### Hand-off

Kapaki-pakinabang ang pattern na ito kapag gusto mong gumawa ng application kung saan maraming agent ang maaaring mag-handoff ng mga gawain sa isa't isa.

Karaniwang gamit sa pattern na ito ay customer support, pamamahala ng gawain, at awtomasyon ng workflow.

Sa pattern na ito, bawat agent ay kumakatawan sa isang gawain o hakbang sa workflow, at maaaring mag-handoff ng mga gawain ang mga agent sa ibang agent base sa mga paunang itinakdang alituntunin.

![Hand off](../../../translated_images/tl/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Collaborative filtering

Kapaki-pakinabang ang pattern na ito kapag gusto mong gumawa ng application kung saan maraming agent ang maaaring magtulungan upang makagawa ng mga rekomendasyon sa mga user.

Bakit gusto mong magtulungan ang maraming agent? Dahil bawat agent ay maaaring may iba't ibang espesyalisasyon at makakatulong sa rekomendasyon sa iba't ibang paraan.

Kunin natin ang halimbawa kung saan ang isang user ay nais ng rekomendasyon tungkol sa pinakamahusay na stock na bibilhin sa stock market.

- **Eksperto sa industriya**: Maaaring ang isang agent ay eksperto sa isang partikular na industriya.
- **Teknikal na pagsusuri**: Ang isa pang agent ay maaaring eksperto sa teknikal na pagsusuri.
- **Pangunahing pagsusuri**: At isa pang agent ay maaaring eksperto sa pangunahing pagsusuri. Sa pamamagitan ng pagtutulungan, maibibigay ng mga agent na ito ang mas komprehensibong rekomendasyon sa user.

![Recommendation](../../../translated_images/tl/multi-agent-filtering.d959cb129dc9f608.webp)

## Senaryo: Proseso ng Refund

Isaalang-alang ang senaryo kung saan ang isang customer ay sinusubukang makakuha ng refund para sa isang produkto, maraming mga agent ang maaaring kasangkot sa prosesong ito ngunit hatiin natin ito sa mga agent na espesipiko sa prosesong ito at mga pangkalahatang agent na magagamit sa ibang mga proseso.

**Mga agent na espesipiko para sa proseso ng refund**:

Narito ang ilang mga agent na maaaring kasangkot sa proseso ng refund:

- **Customer agent**: Ang agent na ito ay kumakatawan sa customer at responsable sa pagsisimula ng proseso ng refund.
- **Seller agent**: Ang agent na ito ay kumakatawan sa seller at responsable sa pagproseso ng refund.
- **Payment agent**: Ang agent na ito ay kumakatawan sa proseso ng pagbabayad at responsable sa pag-refund ng bayad ng customer.
- **Resolution agent**: Ang agent na ito ay kumakatawan sa proseso ng resolusyon at responsable sa paglutas ng anumang isyu na lumitaw sa proseso ng refund.
- **Compliance agent**: Ang agent na ito ay kumakatawan sa proseso ng pagsunod at responsable sa pagtitiyak na ang proseso ng refund ay sumusunod sa mga regulasyon at patakaran.

**Pangkalahatang mga agent**:

Maaaring gamitin ang mga agent na ito sa ibang bahagi ng iyong negosyo.

- **Shipping agent**: Ang agent na ito ay kumakatawan sa proseso ng pagpapadala at responsable sa pagpapadala ng produkto pabalik sa seller. Maaari itong magamit para sa parehong proseso ng refund at sa pangkalahatang pagpapadala ng produkto sa pamamagitan ng pagbili halimbawa.
- **Feedback agent**: Ang agent na ito ay kumakatawan sa proseso ng feedback at responsable sa pagkolekta ng feedback mula sa customer. Maaring magkaroon ng feedback anumang oras, hindi lang panahon ng proseso ng refund.
- **Escalation agent**: Ang agent na ito ay kumakatawan sa proseso ng escalation at responsable sa pag-escalate ng mga isyu sa mas mataas na antas ng suporta. Maaari mong gamitin ang ganitong uri ng agent para sa anumang proseso kung saan kailangan mong i-escalate ang isang isyu.
- **Notification agent**: Ang agent na ito ay kumakatawan sa proseso ng notipikasyon at responsable sa pagpapadala ng mga notification sa customer sa iba't ibang yugto ng proseso ng refund.
- **Analytics agent**: Ang agent na ito ay kumakatawan sa proseso ng analytics at responsable sa pagsusuri ng data na may kaugnayan sa proseso ng refund.
- **Audit agent**: Ang agent na ito ay kumakatawan sa proseso ng audit at responsable sa pag-audit ng proseso ng refund upang matiyak na ito ay isinasagawa nang tama.
- **Reporting agent**: Ang agent na ito ay kumakatawan sa proseso ng pag-uulat at responsable sa paggawa ng mga ulat tungkol sa proseso ng refund.
- **Knowledge agent**: Ang agent na ito ay kumakatawan sa proseso ng kaalaman at responsable sa pagpapanatili ng knowledge base ng impormasyon na may kaugnayan sa proseso ng refund. Maaaring maging dalubhasa ang agent na ito sa mga refund at iba pang bahagi ng iyong negosyo.
- **Security agent**: Ang agent na ito ay kumakatawan sa proseso ng seguridad at responsable sa pagtitiyak ng seguridad ng proseso ng refund.
- **Quality agent**: Ang agent na ito ay kumakatawan sa proseso ng kalidad at responsable sa pagtitiyak ng kalidad ng proseso ng refund.

Maraming mga agent na nakalista sa itaas, kapwa para sa espesipikong proseso ng refund at pati na rin para sa mga pangkalahatang agent na maaaring gamitin sa ibang bahagi ng iyong negosyo. Sana ay nakatulong ito sa iyo upang magkaroon ng ideya kung paano ka makakapagpasya sa mga agent na gagamitin sa iyong multi-agent system.

## Takdang Aralin

Disenyuhin ang isang multi-agent system para sa proseso ng customer support. Tukuyin ang mga agent na kasangkot sa proseso, ang kanilang mga papel at responsibilidad, at kung paano sila nag-iinteract sa isa't isa. Isaalang-alang ang parehong mga agent na espesipiko sa proseso ng customer support at mga pangkalahatang agent na maaaring gamitin sa ibang bahagi ng iyong negosyo.


> Mag-isip muna bago basahin ang sumusunod na solusyon, maaaring kailangan mo ng mas maraming ahente kaysa sa iyong iniisip.

> TIP: Isipin ang iba't ibang yugto ng proseso ng customer support at isaalang-alang din ang mga ahente na kailangan para sa anumang sistema.

## Solusyon

[Solusyon](./solution/solution.md)

## Mga pagsusuri sa kaalaman

### Tanong 1

Aling sitwasyon ang pinakanaaangkop para sa isang multi-agent na sistema?

- [ ] A1: Isang support bot ang sumasagot sa karaniwang mga tanong gamit ang isang knowledge base at maliit na hanay ng mga kasangkapan.
- [ ] A2: Ang refund workflow ay nangangailangan ng hiwalay na mga tungkulin para sa fraud, payment, at compliance, na bawat isa ay may sariling mga kasangkapan, at kailangang maayos ang kanilang mga resulta.
- [ ] A3: Ang iisang simpleng klasipikasyon na kahilingan ay dumarating ng libu-libo beses kada oras.

### Tanong 2

Kailan karaniwang mas mainam ang paggamit ng isang solo agent?

- [ ] A1: Ang gawain ay maaaring hawakan gamit ang isang set ng mga tagubilin at kasangkapan, nang walang pangangailangan ng espesyal na paghahatid.
- [ ] A2: Ang ahente ay may access sa higit sa isang kasangkapan.
- [ ] A3: Ang workflow ay nangangailangan ng hiwalay na mga tungkulin na may iba't ibang mga permiso at independent na audit trails.

[Solusyon quiz](./solution/solution-quiz.md)

## Buod

Sa araling ito, tiningnan natin ang multi-agent design pattern, kabilang ang mga sitwasyon kung saan ang multi-agent ay angkop, ang mga kalamangan ng paggamit ng multi-agent kaysa sa isang solong ahente, ang mga pangunahing bahagi ng pagpapatupad ng multi-agent design pattern, at kung paano magkaroon ng pananaw sa kung paano nagtutulungan ang mga maraming ahente.

### May Karagdagang Tanong tungkol sa Multi-Agent Design Pattern?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipagkita sa iba pang mga nag-aaral, dumalo sa office hours at sagutin ang iyong mga tanong tungkol sa AI Agents.

## Karagdagang mga mapagkukunan

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentasyon ng Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Mga Agentic design patterns</a>


## Nakaraang Aralin

[Planning Design](../07-planning-design/README.md)

## Susunod na Aralin

[Metacognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->