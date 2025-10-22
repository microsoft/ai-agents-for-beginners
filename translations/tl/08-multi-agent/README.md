<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T09:45:50+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "tl"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.tl.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(I-click ang larawan sa itaas upang mapanood ang video ng araling ito)_

# Mga Disenyo ng Multi-Agent

Kapag nagsimula kang magtrabaho sa isang proyekto na may kasamang maraming ahente, kailangan mong isaalang-alang ang disenyo ng multi-agent. Gayunpaman, maaaring hindi agad malinaw kung kailan dapat lumipat sa multi-agents at kung ano ang mga benepisyo nito.

## Panimula

Sa araling ito, susubukan nating sagutin ang mga sumusunod na tanong:

- Anong mga sitwasyon ang angkop para sa multi-agents?
- Ano ang mga benepisyo ng paggamit ng multi-agents kumpara sa isang solong ahente na gumagawa ng maraming gawain?
- Ano ang mga pangunahing bahagi ng pagpapatupad ng disenyo ng multi-agent?
- Paano natin makikita ang interaksyon ng maraming ahente sa isa't isa?

## Mga Layunin sa Pagkatuto

Pagkatapos ng araling ito, dapat mong magawa ang sumusunod:

- Tukuyin ang mga sitwasyon kung saan angkop ang multi-agents.
- Kilalanin ang mga benepisyo ng paggamit ng multi-agents kumpara sa isang solong ahente.
- Maunawaan ang mga pangunahing bahagi ng pagpapatupad ng disenyo ng multi-agent.

Ano ang mas malaking larawan?

*Ang mga multi-agent ay isang disenyo na nagpapahintulot sa maraming ahente na magtulungan upang makamit ang isang karaniwang layunin.*

Ang disenyo na ito ay malawakang ginagamit sa iba't ibang larangan, kabilang ang robotics, autonomous systems, at distributed computing.

## Mga Sitwasyon Kung Saan Angkop ang Multi-Agents

Kaya, anong mga sitwasyon ang magandang gamitin ang multi-agents? Ang sagot ay maraming sitwasyon kung saan kapaki-pakinabang ang paggamit ng maraming ahente, lalo na sa mga sumusunod na kaso:

- **Malalaking gawain**: Ang malalaking gawain ay maaaring hatiin sa mas maliliit na gawain at i-assign sa iba't ibang ahente, na nagpapahintulot ng parallel processing at mas mabilis na pagkumpleto. Halimbawa nito ay sa malalaking data processing tasks.
- **Komplikadong gawain**: Ang mga komplikadong gawain, tulad ng malalaking gawain, ay maaaring hatiin sa mas maliliit na subtask at i-assign sa iba't ibang ahente na dalubhasa sa partikular na aspeto ng gawain. Halimbawa nito ay sa mga autonomous na sasakyan kung saan ang iba't ibang ahente ang namamahala sa navigation, obstacle detection, at komunikasyon sa ibang sasakyan.
- **Iba't ibang kasanayan**: Ang iba't ibang ahente ay maaaring may iba't ibang kasanayan, na nagpapahintulot sa kanila na mas mahusay na hawakan ang iba't ibang aspeto ng isang gawain kaysa sa isang solong ahente. Halimbawa nito ay sa healthcare kung saan ang mga ahente ay maaaring mamahala sa diagnostics, treatment plans, at patient monitoring.

## Mga Benepisyo ng Paggamit ng Multi-Agents Kumpara sa Isang Solong Ahente

Ang isang solong ahente ay maaaring gumana nang maayos para sa mga simpleng gawain, ngunit para sa mas komplikadong gawain, ang paggamit ng maraming ahente ay may ilang benepisyo:

- **Espesyalisasyon**: Ang bawat ahente ay maaaring maging dalubhasa sa isang partikular na gawain. Ang kawalan ng espesyalisasyon sa isang solong ahente ay maaaring magdulot ng kalituhan kapag humarap sa isang komplikadong gawain. Halimbawa, maaaring gawin nito ang isang gawain na hindi ito angkop para sa kanya.
- **Scalability**: Mas madali ang pag-scale ng mga sistema sa pamamagitan ng pagdaragdag ng mas maraming ahente kaysa sa pag-overload ng isang solong ahente.
- **Fault Tolerance**: Kung mabigo ang isang ahente, maaaring magpatuloy ang iba, na tinitiyak ang pagiging maaasahan ng sistema.

Halimbawa, mag-book tayo ng biyahe para sa isang user. Ang isang solong ahente ay kailangang hawakan ang lahat ng aspeto ng proseso ng pag-book ng biyahe, mula sa paghahanap ng mga flight hanggang sa pag-book ng mga hotel at rental cars. Upang magawa ito, kailangang magkaroon ng mga tool ang ahente para sa lahat ng mga gawaing ito. Maaari itong magresulta sa isang komplikado at monolitikong sistema na mahirap i-maintain at i-scale. Sa kabilang banda, ang isang multi-agent system ay maaaring magkaroon ng iba't ibang ahente na dalubhasa sa paghahanap ng mga flight, pag-book ng mga hotel, at rental cars. Gagawin nitong mas modular, mas madaling i-maintain, at scalable ang sistema.

Ihambing ito sa isang travel bureau na pinapatakbo bilang isang maliit na tindahan kumpara sa isang travel bureau na pinapatakbo bilang isang prangkisa. Ang maliit na tindahan ay may isang ahente na humahawak sa lahat ng aspeto ng proseso ng pag-book ng biyahe, habang ang prangkisa ay may iba't ibang ahente na humahawak sa iba't ibang aspeto ng proseso.

## Mga Pangunahing Bahagi ng Pagpapatupad ng Disenyo ng Multi-Agent

Bago mo maipatupad ang disenyo ng multi-agent, kailangan mong maunawaan ang mga pangunahing bahagi na bumubuo sa disenyo.

Gawin nating mas kongkreto ito sa pamamagitan ng pagtingin muli sa halimbawa ng pag-book ng biyahe para sa isang user. Sa kasong ito, ang mga pangunahing bahagi ay kinabibilangan ng:

- **Komunikasyon ng Ahente**: Ang mga ahente para sa paghahanap ng mga flight, pag-book ng mga hotel, at rental cars ay kailangang mag-usap at magbahagi ng impormasyon tungkol sa mga kagustuhan at limitasyon ng user. Kailangan mong magdesisyon sa mga protocol at pamamaraan para sa komunikasyong ito. Halimbawa, kailangang mag-usap ang ahente para sa paghahanap ng mga flight sa ahente para sa pag-book ng mga hotel upang matiyak na ang hotel ay naka-book para sa parehong mga petsa ng flight.
- **Mga Mekanismo ng Koordinasyon**: Kailangang i-coordinate ng mga ahente ang kanilang mga aksyon upang matiyak na natutugunan ang mga kagustuhan at limitasyon ng user. Halimbawa, maaaring gusto ng user ng hotel na malapit sa airport, ngunit ang limitasyon ay ang mga rental cars ay available lamang sa airport.
- **Arkitektura ng Ahente**: Kailangang magkaroon ng internal na istruktura ang mga ahente upang makagawa ng mga desisyon at matuto mula sa kanilang interaksyon sa user. Halimbawa, maaaring gumamit ang ahente para sa paghahanap ng mga flight ng machine learning model upang magrekomenda ng mga flight batay sa mga nakaraang kagustuhan ng user.
- **Visibility sa Interaksyon ng Multi-Agent**: Kailangan mong magkaroon ng visibility sa kung paano nag-iinteract ang maraming ahente sa isa't isa. Halimbawa, maaaring magkaroon ng dashboard na nagpapakita ng status ng bawat ahente, mga kagustuhan at limitasyon ng user, at ang mga interaksyon sa pagitan ng mga ahente.
- **Mga Pattern ng Multi-Agent**: May iba't ibang pattern para sa pagpapatupad ng mga multi-agent system, tulad ng centralized, decentralized, at hybrid architectures. Kailangan mong magdesisyon kung aling pattern ang pinakaangkop sa iyong use case.
- **Human in the Loop**: Sa karamihan ng mga kaso, magkakaroon ng tao sa proseso, at kailangan mong turuan ang mga ahente kung kailan hihingi ng interbensyon ng tao. Halimbawa, maaaring humiling ang user ng partikular na hotel o flight na hindi inirekomenda ng mga ahente.

## Visibility sa Interaksyon ng Multi-Agent

Mahalagang magkaroon ng visibility sa kung paano nag-iinteract ang maraming ahente sa isa't isa. Ang visibility na ito ay mahalaga para sa debugging, pag-optimize, at pagtiyak ng pagiging epektibo ng kabuuang sistema. Upang makamit ito, kailangan mong magkaroon ng mga tool at pamamaraan para sa pagsubaybay sa mga aktibidad at interaksyon ng ahente.

Halimbawa, sa kaso ng pag-book ng biyahe para sa isang user, maaaring magkaroon ng dashboard na nagpapakita ng status ng bawat ahente, mga kagustuhan at limitasyon ng user, at ang mga interaksyon sa pagitan ng mga ahente. Ang dashboard na ito ay maaaring magpakita ng mga petsa ng biyahe ng user, mga flight na inirekomenda ng flight agent, mga hotel na inirekomenda ng hotel agent, at mga rental cars na inirekomenda ng rental car agent. Magbibigay ito ng malinaw na pananaw kung paano nag-iinteract ang mga ahente sa isa't isa at kung natutugunan ang mga kagustuhan at limitasyon ng user.

Tingnan natin ang bawat aspeto nang mas detalyado.

- **Mga Tool sa Pag-log at Pagsubaybay**: Dapat magkaroon ng pag-log para sa bawat aksyon na ginawa ng isang ahente. Ang isang log entry ay maaaring mag-imbak ng impormasyon tungkol sa ahente na gumawa ng aksyon, ang aksyon na ginawa, ang oras ng aksyon, at ang resulta ng aksyon. Ang impormasyong ito ay maaaring gamitin para sa debugging, pag-optimize, at iba pa.
- **Mga Tool sa Visualization**: Ang mga tool sa visualization ay makakatulong sa iyong makita ang mga interaksyon sa pagitan ng mga ahente sa mas madaling maunawaang paraan. Halimbawa, maaaring magkaroon ng graph na nagpapakita ng daloy ng impormasyon sa pagitan ng mga ahente.
- **Mga Sukatan ng Pagganap**: Ang mga sukatan ng pagganap ay makakatulong sa iyong subaybayan ang pagiging epektibo ng multi-agent system. Halimbawa, maaari mong subaybayan ang oras na ginugol sa pagkumpleto ng isang gawain, ang bilang ng mga gawain na nakumpleto bawat yunit ng oras, at ang katumpakan ng mga rekomendasyon ng mga ahente.

## Mga Pattern ng Multi-Agent

Tingnan natin ang ilang mga konkretong pattern na maaari nating gamitin upang lumikha ng mga multi-agent na app. Narito ang ilang mga pattern na maaaring isaalang-alang:

### Group Chat

Ang pattern na ito ay kapaki-pakinabang kapag nais mong lumikha ng isang group chat application kung saan maaaring makipag-usap ang maraming ahente sa isa't isa. Karaniwang mga use case para sa pattern na ito ay ang team collaboration, customer support, at social networking.

Sa pattern na ito, ang bawat ahente ay kumakatawan sa isang user sa group chat, at ang mga mensahe ay ipinapasa sa pagitan ng mga ahente gamit ang isang messaging protocol. Ang mga ahente ay maaaring magpadala ng mga mensahe sa group chat, tumanggap ng mga mensahe mula sa group chat, at tumugon sa mga mensahe mula sa ibang mga ahente.

Ang pattern na ito ay maaaring ipatupad gamit ang isang centralized architecture kung saan ang lahat ng mga mensahe ay dumadaan sa isang central server, o isang decentralized architecture kung saan ang mga mensahe ay direktang ipinapasa.

![Group chat](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.tl.png)

### Hand-off

Ang pattern na ito ay kapaki-pakinabang kapag nais mong lumikha ng isang application kung saan maaaring ipasa ng maraming ahente ang mga gawain sa isa't isa.

Karaniwang mga use case para sa pattern na ito ay ang customer support, task management, at workflow automation.

Sa pattern na ito, ang bawat ahente ay kumakatawan sa isang gawain o isang hakbang sa workflow, at maaaring ipasa ng mga ahente ang mga gawain sa ibang mga ahente batay sa mga paunang natukoy na mga patakaran.

![Hand off](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.tl.png)

### Collaborative Filtering

Ang pattern na ito ay kapaki-pakinabang kapag nais mong lumikha ng isang application kung saan maaaring magtulungan ang maraming ahente upang magbigay ng mga rekomendasyon sa mga user.

Ang dahilan kung bakit nais mong magtulungan ang maraming ahente ay dahil ang bawat ahente ay maaaring may iba't ibang kasanayan at maaaring mag-ambag sa proseso ng rekomendasyon sa iba't ibang paraan.

Halimbawa, kung nais ng isang user ng rekomendasyon sa pinakamahusay na stock na bibilhin sa stock market:

- **Eksperto sa Industriya**: Isang ahente ang maaaring dalubhasa sa isang partikular na industriya.
- **Teknikal na Pagsusuri**: Isa pang ahente ang maaaring dalubhasa sa teknikal na pagsusuri.
- **Pangunahing Pagsusuri**: At isa pang ahente ang maaaring dalubhasa sa pangunahing pagsusuri. Sa pamamagitan ng pagtutulungan, maaaring magbigay ang mga ahenteng ito ng mas komprehensibong rekomendasyon sa user.

![Recommendation](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.tl.png)

## Sitwasyon: Proseso ng Refund

Isaalang-alang ang isang sitwasyon kung saan sinusubukan ng isang customer na makakuha ng refund para sa isang produkto. Maaaring may ilang mga ahente na kasangkot sa prosesong ito, ngunit hatiin natin ito sa mga ahenteng partikular para sa prosesong ito at mga pangkalahatang ahente na maaaring gamitin sa iba pang mga proseso.

**Mga Ahenteng Partikular para sa Proseso ng Refund**:

Narito ang ilang mga ahente na maaaring kasangkot sa proseso ng refund:

- **Customer Agent**: Ang ahenteng ito ay kumakatawan sa customer at responsable sa pagsisimula ng proseso ng refund.
- **Seller Agent**: Ang ahenteng ito ay kumakatawan sa nagbebenta at responsable sa pagproseso ng refund.
- **Payment Agent**: Ang ahenteng ito ay kumakatawan sa proseso ng pagbabayad at responsable sa pag-refund ng bayad ng customer.
- **Resolution Agent**: Ang ahenteng ito ay kumakatawan sa proseso ng resolution at responsable sa paglutas ng anumang isyu na lumitaw sa panahon ng proseso ng refund.
- **Compliance Agent**: Ang ahenteng ito ay kumakatawan sa proseso ng pagsunod at responsable sa pagtiyak na ang proseso ng refund ay sumusunod sa mga regulasyon at patakaran.

**Mga Pangkalahatang Ahente**:

Ang mga ahenteng ito ay maaaring gamitin sa iba pang bahagi ng iyong negosyo.

- **Shipping Agent**: Ang ahenteng ito ay kumakatawan sa proseso ng pagpapadala at responsable sa pagpapadala ng produkto pabalik sa nagbebenta. Maaari itong gamitin sa parehong proseso ng refund at sa pangkalahatang pagpapadala ng produkto, halimbawa sa pagbili.
- **Feedback Agent**: Ang ahenteng ito ay kumakatawan sa proseso ng feedback at responsable sa pagkolekta ng feedback mula sa customer. Ang feedback ay maaaring makuha anumang oras at hindi lamang sa panahon ng proseso ng refund.
- **Escalation Agent**: Ang ahenteng ito ay kumakatawan sa proseso ng escalation at responsable sa pag-escalate ng mga isyu sa mas mataas na antas ng suporta. Maaari mong gamitin ang ganitong uri ng ahente para sa anumang proseso kung saan kailangan mong i-escalate ang isang isyu.
- **Notification Agent**: Ang ahenteng ito ay kumakatawan sa proseso ng notification at responsable sa pagpapadala ng mga notification sa customer sa iba't ibang yugto ng proseso ng refund.
- **Analytics Agent**: Ang ahenteng ito ay kumakatawan sa proseso ng analytics at responsable sa pagsusuri ng data na may kaugnayan sa proseso ng refund.
- **Audit Agent**: Ang ahenteng ito ay kumakatawan sa proseso ng audit at responsable sa pag-audit ng proseso ng refund upang matiyak na ito ay isinasagawa nang tama.
- **Reporting Agent**: Ang ahenteng ito ay kumakatawan sa proseso ng reporting at responsable sa paggawa ng mga ulat tungkol sa proseso ng refund.
- **Knowledge Agent**: Ang ahenteng ito ay kumakatawan sa proseso ng kaalaman at responsable sa pagpapanatili ng isang knowledge base ng impormasyon na may kaugnayan sa proseso ng refund. Ang ahenteng ito ay maaaring may kaalaman sa parehong refund at iba pang bahagi ng iyong negosyo.
- **Security Agent**: Ang ahenteng ito ay kumakatawan sa proseso ng seguridad at responsable sa pagtiyak ng seguridad ng proseso ng refund.
- **Quality Agent**: Ang ahenteng ito ay kumakatawan sa proseso ng kalidad at responsable sa pagtiyak ng kalidad ng proseso ng refund.

Maraming mga ahente ang nakalista sa itaas, parehong para sa partikular na proseso ng refund at para sa mga pangkalahatang ahente na maaaring gamitin sa iba pang bahagi ng iyong negosyo. Sana ay nagbigay ito sa iyo ng ideya kung paano ka makakapagdesisyon kung aling mga ahente ang gagamitin sa iyong multi-agent system.

## Gawain
Magdisenyo ng isang multi-agent system para sa proseso ng customer support. Tukuyin ang mga agent na kasangkot sa proseso, ang kanilang mga tungkulin at responsibilidad, at kung paano sila nakikipag-ugnayan sa isa't isa. Isaalang-alang ang parehong mga agent na tiyak sa proseso ng customer support at mga pangkalahatang agent na maaaring gamitin sa iba pang bahagi ng iyong negosyo.

> Mag-isip muna bago basahin ang sumusunod na solusyon, maaaring kailanganin mo ng mas maraming agent kaysa sa inaakala mo.

> TIP: Isaalang-alang ang iba't ibang yugto ng proseso ng customer support at isama rin ang mga agent na kailangan para sa anumang sistema.

## Solusyon

[Solusyon](./solution/solution.md)

## Mga Tanong sa Kaalaman

Tanong: Kailan mo dapat isaalang-alang ang paggamit ng multi-agents?

- [ ] A1: Kapag maliit ang workload at simple ang gawain.
- [ ] A2: Kapag malaki ang workload.
- [ ] A3: Kapag simple ang gawain.

[Solusyon sa quiz](./solution/solution-quiz.md)

## Buod

Sa araling ito, tinalakay natin ang multi-agent design pattern, kabilang ang mga sitwasyon kung saan naaangkop ang multi-agents, ang mga benepisyo ng paggamit ng multi-agents kumpara sa isang singular agent, ang mga pangunahing bahagi ng pagpapatupad ng multi-agent design pattern, at kung paano magkaroon ng visibility sa kung paano nakikipag-ugnayan ang mga multiple agents sa isa't isa.

### May Karagdagang Katanungan Tungkol sa Multi-Agent Design Pattern?

Sumali sa [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa ibang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

## Karagdagang mga mapagkukunan

- 

## Nakaraang Aralin

[Disenyo ng Pagpaplano](../07-planning-design/README.md)

## Susunod na Aralin

[Metacognition sa AI Agents](../09-metacognition/README.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.