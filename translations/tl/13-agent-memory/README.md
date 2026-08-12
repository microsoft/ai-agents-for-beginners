# Memorya para sa mga AI Agents 
[![Agent Memory](../../../translated_images/tl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kapag pinag-uusapan ang mga natatanging benepisyo ng paglikha ng mga AI Agents, dalawang bagay ang pangunahing tinalakay: ang kakayahang tumawag ng mga tool upang tapusin ang mga gawain at ang kakayahang umunlad sa paglipas ng panahon. Ang memorya ang pundasyon ng paglikha ng self-improving agent na maaaring gumawa ng mas magagandang karanasan para sa ating mga gumagamit.

Sa araling ito, titingnan natin kung ano ang memorya para sa mga AI Agents at kung paano natin ito mapamamahalaan at magagamit para sa kapakinabangan ng ating mga aplikasyon.

## Panimula

Tatalakayin sa araling ito ang:

• **Pag-unawa sa Memorya ng AI Agent**: Ano ang memorya at bakit ito mahalaga para sa mga agent.

• **Pagpapatupad at Pag-iimbak ng Memorya**: Praktikal na mga pamamaraan para maidagdag ang mga kakayahan sa memorya sa iyong mga AI agent, na nakatuon sa pansamantala at pangmatagalang memorya.

• **Paggawa sa AI Agents na Self-Improving**: Paano pinapagana ng memorya ang mga agent upang matuto mula sa mga nakaraang interaksyon at umunlad sa paglipas ng panahon.

## Mga Available na Implementasyon

Ang araling ito ay may kasamang dalawang komprehensibong notebook tutorial:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Nagpapatupad ng memorya gamit ang Mem0 at Azure AI Search kasama ng Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Nagpapatupad ng istrukturadong memorya gamit ang Cognee, na awtomatikong bumubuo ng knowledge graph na sinusuportahan ng mga embeddings, nagvi-visualize ng graph, at matalinong retrieval

## Mga Layunin sa Pagkatuto

Matapos makumpleto ang araling ito, malalaman mo kung paano:

• **Pagkakaiba-ibahin ang iba't ibang uri ng memorya ng AI agent**, kabilang ang working, short-term, at long-term memory, pati na rin ang mga espesyalisadong anyo tulad ng persona at episodic memory.

• **Magpatupad at pamahalaan ang short-term at long-term memory para sa mga AI agent** gamit ang Microsoft Agent Framework, na gumagamit ng mga tool tulad ng Mem0, Cognee, Whiteboard memory, at pagsasama sa Azure AI Search.

• **Maunawaan ang mga prinsipyo sa likod ng self-improving AI agents** at kung paano nakakatulong ang matibay na sistema ng pamamahala ng memorya sa tuluy-tuloy na pagkatuto at pag-aangkop.

## Pag-unawa sa Memorya ng AI Agent

Sa pinakapuso nito, **ang memorya para sa mga AI agents ay tumutukoy sa mga mekanismo na nagpapahintulot sa kanila na magtago at magbalik-tanaw ng impormasyon**. Ang impormasyong ito ay maaaring mga partikular na detalye tungkol sa isang pag-uusap, mga kagustuhan ng gumagamit, mga nakaraang aksyon, o kahit mga natutunang pattern.

Kung walang memorya, kadalasan ay stateless ang mga AI application, ibig sabihin, nagsisimula sa simula ang bawat interaksyon. Nagdudulot ito ng paulit-ulit at nakakainis na karanasan para sa gumagamit kung saan "nakakalimutan" ng agent ang mga naunang konteksto o kagustuhan.

### Bakit Mahalaga ang Memorya?

Ang katalinuhan ng isang agent ay mahigpit na nakatali sa kanyang kakayahang balikan at gamitin ang mga nakaraang impormasyon. Pinapayagan ng memorya ang mga agent na maging:

• **Reflective**: Natututo mula sa mga nakaraang aksyon at resulta.

• **Interactive**: Pinananatili ang konteksto sa isang kasalukuyang pag-uusap.

• **Proactive at Reactive**: Nag-aasahan ng mga pangangailangan o tumutugon nang naaayon base sa makasaysayang datos.

• **Autonomous**: Mas malayang nakakagawa ng operasyon sa pagbabatay sa nakasagang kaalaman.

Ang layunin ng pagpapatupad ng memorya ay gawing mas **mapagkakatiwalaan at may kakayahan** ang mga agent.

### Mga Uri ng Memorya

#### Working Memory

Isipin ito bilang isang piraso ng scratch paper na ginagamit ng agent sa isang solong, kasalukuyang gawain o proseso ng pag-iisip. Naglalaman ito ng agarang impormasyon na kailangan para kalkulahin ang susunod na hakbang.

Para sa mga AI agents, madalas na kinukuha ng working memory ang pinakamahalagang impormasyon mula sa isang pag-uusap, kahit na mahaba o putol ang buong history ng chat. Nakatuon ito sa pagkuha ng mga pangunahing elemento tulad ng mga kinakailangan, suhestiyon, desisyon, at mga aksyon.

**Halimbawa ng Working Memory**

Sa isang travel booking agent, maaaring kunin ng working memory ang kasalukuyang kahilingan ng gumagamit, tulad ng "Gusto kong mag-book ng biyahe papuntang Paris". Ang partikular na kahilingang ito ay hawak sa agarang konteksto ng agent upang gabayan ang kasalukuyang interaksyon.

#### Short Term Memory

Ang uri ng memoryang ito ay nagtatago ng impormasyon para sa tagal ng isang solong pag-uusap o sesyon. Ito ang konteksto ng kasalukuyang chat, na nagpapahintulot sa agent na balikan ang mga nakaraang turno sa diyologo.

Sa mga sample ng [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK, ito ay tumutugma sa `AgentSession`, na nilikha gamit ang `agent.create_session()`. Ang sesyon ang built-in na short-term memory ng framework: pinananatili nito ang konteksto ng pag-uusap habang ginagamit muli ang parehas na sesyon, ngunit hindi iniimbak ang kontekstong iyon kapag nagtapos ang sesyon o nag-restart ang aplikasyon. Gamitin ang long-term memory para sa mga katotohanan at kagustuhan na kailangang manatili sa maraming sesyon, karaniwan sa pamamagitan ng database, vector index, o ibang persistent store.

**Halimbawa ng Short Term Memory**

Kung magtatanong ang isang gumagamit, "Magkano ang flight papuntang Paris?" at susundan ito ng "Paano naman ang akomodasyon doon?", tiniyak ng short-term memory na alam ng agent na ang "doon" ay tumutukoy sa "Paris" sa parehong pag-uusap.

#### Long Term Memory

Ito ay impormasyon na nananatili sa maraming pag-uusap o sesyon. Pinapayagan nito ang mga agent na maalala ang mga kagustuhan ng gumagamit, mga makasaysayang interaksyon, o pangkalahatang kaalaman sa mahabang panahon. Mahalaga ito para sa personalisasyon.

**Halimbawa ng Long Term Memory**

Maaaring itala ng long-term memory na "Gusto ni Ben ang skiing at mga panlabas na aktibidad, mahilig sa kape na may tanawin ng bundok, at nais iwasan ang advanced na ski slopes dahil sa nakaraang pinsala". Ang impormasyong ito, na natutunan mula sa mga nakaraang interaksyon, ay nakakaapekto sa mga rekomendasyon sa mga susunod na sesyon ng pagpaplano ng biyahe, na ginagawa itong napaka-personalize.

#### Persona Memory

Ang espesyalisadong uri ng memoryang ito ay tumutulong sa isang agent na magkaroon ng pare-parehong "pagkatao" o "persona". Pinapayagan nito ang agent na maalala ang mga detalye tungkol sa sarili nito o sa nilalayong papel, na ginagawang mas daloy at nakatuon ang mga interaksyon.

**Halimbawa ng Persona Memory**
Kung ang travel agent ay dinisenyo bilang isang "expert ski planner," maaaring patatagin ng persona memory ang papel na ito, na nakakaapekto sa mga tugon nito upang tumugma sa tono at kaalaman ng isang eksperto.

#### Workflow/Episodic Memory

Itinatago ng memoryang ito ang sunod-sunod na mga hakbang na ginagawa ng agent sa isang komplikadong gawain, kasama ang mga tagumpay at kabiguan. Parang pag-alala sa mga tiyak na "episodes" o nakaraang karanasan para matuto mula rito.

**Halimbawa ng Episodic Memory**

Kung sinubukan ng agent na mag-book ng isang partikular na flight ngunit nabigo dahil sa hindi pagkakaroon, maaaring itala ng episodic memory ang kabiguang ito, na nagpapahintulot sa agent na subukan ang mga alternatibong flight o ipaalam sa gumagamit ang isyu nang mas may alam sa susunod na pagtatangka.

#### Entity Memory

Ito ay tumutukoy sa pagkuha at pag-alala ng mga tiyak na entity (tulad ng mga tao, lugar, o bagay) at mga pangyayari mula sa mga pag-uusap. Pinapayagan nito ang agent na bumuo ng istrakturadong pag-unawa sa mga mahahalagang elemento na napag-usapan.

**Halimbawa ng Entity Memory**

Mula sa isang pag-uusap tungkol sa isang nakaraang biyahe, maaaring kunin ng agent ang "Paris," "Eiffel Tower," at "hapunan sa Le Chat Noir restaurant" bilang mga entity. Sa susunod na interaksyon, maaaring maalala ng agent ang "Le Chat Noir" at mag-alok na gumawa ng bagong reserbasyon doon.

#### Structured RAG (Retrieval Augmented Generation)

Bagama't ang RAG ay isang mas malawak na teknika, ang "Structured RAG" ay binibigyang-diin bilang isang makapangyarihang teknolohiya sa memorya. Kinukuha nito ang masikip, istrakturadong impormasyon mula sa iba't ibang pinagmulan (mga pag-uusap, emails, larawan) at ginagamit ito upang mapahusay ang katumpakan, pagbabalik-tanaw, at bilis sa mga tugon. Hindi tulad ng klasikong RAG na nakabatay lamang sa semantic similarity, ang Structured RAG ay gumagana sa likas na istruktura ng impormasyon.

**Halimbawa ng Structured RAG**

Sa halip na mag-match lang ng mga keyword, maaaring i-parse ng Structured RAG ang mga detalye ng flight (destinasyon, petsa, oras, airline) mula sa isang email at i-imbak ito sa isang istrakturadong paraan. Pinapayagan nito ang tumpak na mga query tulad ng "Anong flight ang na-book ko papuntang Paris noong Martes?"

## Pagpapatupad at Pag-iimbak ng Memorya

Ang pagpapatupad ng memorya para sa mga AI agent ay kinapapalooban ng isang sistematikong proseso ng **pamamahala ng memorya**, na kinabibilangan ng paggawa, pag-iimbak, retrieval, integrasyon, pag-update, at kahit na "pagkakalimot" (o pagtanggal) ng impormasyon. Ang retrieval ay isang napakahalagang aspeto.

### Mga Espesyalisadong Tool sa Memorya

#### Mem0

Isang paraan upang mag-imbak at pamahalaan ang memorya ng agent ay paggamit ng mga espesyalisadong tool tulad ng Mem0. Gumagana ang Mem0 bilang isang persistent memory layer, na nagpapahintulot sa mga agent na maalala ang mga mahalagang interaksyon, itago ang mga kagustuhan ng gumagamit at katotohanan sa konteksto, at matuto mula sa mga tagumpay at kabiguan sa paglipas ng panahon. Ang ideya dito ay nagiging stateful ang mga stateless na agent.

Gumagana ito sa pamamagitan ng **two-phase memory pipeline: extraction at update**. Una, ipinapadala ang mga mensahe na idinadagdag sa thread ng agent sa Mem0 service, na gumagamit ng Large Language Model (LLM) upang ibuod ang kasaysayan ng pag-uusap at kumuha ng mga bagong memorya. Sumunod, ang LLM-driven update phase ay nagtatakda kung idadagdag, babaguhin, o tatanggalin ang mga memoryang ito, na iniimbak sa isang hybrid data store na maaaring maglaman ng vector, graph, at key-value databases. Sinusuportahan din ng sistemang ito ang iba't ibang uri ng memorya at maaaring isama ang graph memory para pamahalaan ang mga relasyon sa pagitan ng mga entity.

#### Cognee

Isa pang makapangyarihang pamamaraan ay ang paggamit ng **Cognee**, isang open-source semantic memory para sa mga AI agent na nagbabago ng istrukturado at hindi istrukturadong datos sa mga queryable knowledge graph na sinusuportahan ng embeddings. Nagbibigay ang Cognee ng **dual-store architecture** na pinagsasama ang vector similarity search sa graph relationships, na nagpapahintulot sa mga agent na maunawaan hindi lang kung ano ang impormasyon na magkatulad, kundi kung paano magkakaugnay ang mga konsepto sa isa't isa.

Ito ay mahusay sa **hybrid retrieval** na pinaghalo ang vector similarity, graph structure, at LLM reasoning - mula sa raw chunk lookup hanggang sa graph-aware question answering. Pinananatili ng system ang **living memory** na umuunlad at lumalago habang nananatiling mabisang ma-query bilang isang nakakonektang graph, sinusuportahan ang parehong short-term session context at long-term persistent memory.

Ipinapakita sa Cognee notebook tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) kung paano bumuo ng iisang layer ng memorya, na may praktikal na mga halimbawa ng pag-ingest ng iba't ibang pinagkukunan ng datos, pag-visualize ng knowledge graph, at pag-query gamit ang iba't ibang search strategies na iniangkop sa partikular na pangangailangan ng agent.

### Pag-iimbak ng Memorya gamit ang RAG

Bukod sa mga espesyalisadong tool sa memorya tulad ng Mem0, maaari kang gumamit ng matatag na mga serbisyo sa paghahanap tulad ng **Azure AI Search bilang backend para sa pag-iimbak at retrieval ng mga memorya**, lalo na para sa structured RAG.

Pinapayagan nitong gawing grounded ang mga tugon ng iyong agent gamit ang iyong sariling datos, tinitiyak ang mas kaugnay at tumpak na mga sagot. Maaaring gamitin ang Azure AI Search para mag-imbak ng memorya sa paglalakbay na pang-gamit, mga katalogo ng produkto, o anumang iba pang espesipikong kaalaman sa domain.

Sinusuportahan ng Azure AI Search ang mga kakayahan tulad ng **Structured RAG**, na mahusay sa pagkuha at pag-retrieve ng masikip, istrakturadong impormasyon mula sa malalaking datasets tulad ng kasaysayan ng pag-uusap, mga email, o kahit mga larawan. Nagbibigay ito ng "superhuman precision and recall" kumpara sa tradisyunal na text chunking at embedding approaches.

## Paggawa sa AI Agents na Self-Improve

Isang karaniwang pattern para sa mga self-improving agent ay ang pagpapakilala ng isang **"knowledge agent"**. Ang hiwalay na agent na ito ay nagmamasid sa pangunahing pag-uusap sa pagitan ng gumagamit at ang pangunahing agent. Ang tungkulin nito ay:

1. **Kilalanin ang mahalagang impormasyon**: Tukuyin kung may bahagi ng pag-uusap na karapat-dapat itago bilang pangkalahatang kaalaman o partikular na kagustuhan ng gumagamit.

2. **Kunin at ibuod**: Ilahad ang mahalagang natutunan o kagustuhan mula sa pag-uusap.

3. **I-imbak sa knowledge base**: Itago ang nakuha na impormasyong ito, madalas sa vector database, upang maaaring balikan sa hinaharap.

4. **Palawakin ang mga susunod na query**: Kapag nagsimula ang gumagamit ng bagong query, kinukuha ng knowledge agent ang kaugnay na naimbak na impormasyon at idinadagdag ito sa prompt ng gumagamit, nagbibigay ng mahalagang konteksto sa pangunahing agent (katulad ng RAG).

### Mga Optimization para sa Memorya

• **Pamamahala ng Latency**: Upang maiwasan ang pagpapabagal ng mga interaksyon ng gumagamit, maaaring gamitin muna ang mas mura at mas mabilis na modelo upang mabilis na suriin kung mahalaga ang impormasyon na itago o kunin, na ginagamit lamang ang mas kumplikadong extraction/retrieval process kapag kinakailangan.

• **Pagpapanatili ng Knowledge Base**: Para sa lumalaking knowledge base, ang hindi gaanong madalas gamitin na impormasyon ay maaaring ilipat sa "cold storage" upang pamahalaan ang mga gastusin.

## May Karagdagang Tanong Tungkol sa Agent Memory?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipagkita sa ibang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.
## Nakaraang Aralin

[Context Engineering for AI Agents](../12-context-engineering/README.md)

## Susunod na Aralin

[Exploring Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->