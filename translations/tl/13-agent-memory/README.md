# Memory para sa AI Agents  
[![Agent Memory](../../../translated_images/tl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kapag pinag-uusapan ang natatanging benepisyo ng paggawa ng AI Agents, dalawang bagay ang pangunahing tinatalakay: ang kakayahang tumawag ng mga tool upang matapos ang mga gawain at ang kakayahang umunlad sa paglipas ng panahon. Ang memorya ay nasa pundasyon ng paggawa ng self-improving agent na makalikha ng mas magagandang karanasan para sa ating mga gumagamit.

Sa araling ito, titingnan natin kung ano ang memorya para sa AI Agents at kung paano natin ito mapamamahalaan at magagamit para sa kapakinabangan ng ating mga aplikasyon.

## Panimula

Ang araling ito ay sasaklaw sa:

• **Pag-unawa sa Memorya ng AI Agent**: Ano ang memorya at bakit ito mahalaga para sa mga agent.

• **Pagpapatupad at Pag-iimbak ng Memorya**: Praktikal na pamamaraan para maidagdag ang mga kakayahan sa memorya sa iyong mga AI agent, na nakatuon sa short-term at long-term memory.

• **Paggawing Self-Improving ang AI Agents**: Paano nagiging posible sa memorya na matuto ang mga agent mula sa mga nakaraang interaksyon at umunlad sa paglipas ng panahon.

## Mga Magagamit na Implementasyon

Ang araling ito ay may dalawang komprehensibong notebook tutorial:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Nagpapatupad ng memorya gamit ang Mem0 at Azure AI Search kasama ang Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Nagpapatupad ng structured memory gamit ang Cognee, awtomatikong bumubuo ng knowledge graph na suportado ng embeddings, nagpapakita ng graph, at matalinong retrieval

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano:

• **Pag-iba-ibahin ang iba't ibang uri ng memorya ng AI agent**, kabilang ang working, short-term, at long-term memory, pati na rin ang mga espesyal na anyo tulad ng persona at episodic memory.

• **Ipatupad at pamahalaan ang short-term at long-term memory para sa AI agents** gamit ang Microsoft Agent Framework, gamit ang mga tool tulad ng Mem0, Cognee, Whiteboard memory, at integrasyon sa Azure AI Search.

• **Unawain ang mga prinsipyo sa likod ng self-improving AI agents** at kung paano nakakatulong ang matatag na sistema ng pamamahala ng memorya sa patuloy na pagkatuto at pag-aangkop.

## Pag-unawa sa Memorya ng AI Agent

Sa pinakapuso, **ang memorya para sa AI agents ay tumutukoy sa mga mekanismong nagpapahintulot sa kanila na magtago at maalala ang impormasyon**. Ang impormasyong ito ay maaaring mga partikular na detalye tungkol sa isang pag-uusap, mga kagustuhan ng gumagamit, mga nakaraang aksyon, o kahit mga natutunang pattern.

Kung walang memorya, ang mga AI applications ay kadalasang walang estado (stateless), ibig sabihin, bawat interaksyon ay nagsisimula mula sa simula. Nagdudulot ito ng paulit-ulit at nakakainis na karanasan sa gumagamit kung saan ang agent ay "nakakalimot" ng naunang konteksto o mga kagustuhan.

### Bakit Mahalaga ang Memorya?

Malalim ang kaugnayan ng katalinuhan ng isang ahente sa kakayahan nitong maalala at magamit ang nakaraang impormasyon. Pinapahintulutan ng memorya ang mga agent na maging:

• **Reflective**: Natututo mula sa mga nakaraang aksyon at kinalabasan.

• **Interactive**: Napapanatili ang konteksto sa isang kasalukuyang pag-uusap.

• **Proactive at Reactive**: Natatantiya ang mga pangangailangan o nakatutugon nang naaayon batay sa makasaysayang datos.

• **Autonomous**: Mas independiyenteng gumagana gamit ang nakaimbak na kaalaman.

Ang layunin ng pagpapatupad ng memorya ay gawing mas **mapagkakatiwalaan at may kakayahan** ang mga agent.

### Mga Uri ng Memorya

#### Working Memory

Isipin ito bilang isang piraso ng papel na pansamantala na ginagamit ng agent habang may isinasagawang isang takdang gawain o proseso ng pag-iisip. Dito iniimbak ang agarang kailangang impormasyon upang kalkulahin ang susunod na hakbang.

Para sa AI agents, madalas na kinukuha sa working memory ang pinakamahalagang impormasyon mula sa pag-uusap, kahit na mahaba o naputol ang buong kasaysayan ng chat. Nakatuon ito sa pagkuha ng mga susi tulad ng mga pangangailangan, panukala, desisyon, at mga aksyon.

**Halimbawa ng Working Memory**

Sa isang travel booking agent, ang working memory ay maaaring maglaman ng kasalukuyang kahilingan ng gumagamit, tulad ng "Gusto kong mag-book ng biyahe papuntang Paris". Ang partikular na pangangailangang ito ay nasa agarang konteksto ng agent upang gabayan ang kasalukuyang interaksyon.

#### Short Term Memory

Ang uri ng memoryang ito ay nagtatahak ng impormasyon sa tagal lamang ng isang pag-uusap o sesyon. Ito ang konteksto ng kasalukuyang chat, na nagpapahintulot sa agent na bumalik sa mga naunang turong usapan.

Sa mga halimbawa ng [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK, tumutugma ito sa `AgentSession`, na nilikha gamit ang `agent.create_session()`. Ang session ay ang built-in na short-term memory ng framework: pinananatili nito ang konteksto ng pag-uusap habang ginagamit pa rin ang parehong session, ngunit hindi ito pinapanatili kapag natapos ang session o ni-restart ang aplikasyon. Ginagamit ang long-term memory para sa mga katotohanan at kagustuhan na kailangang manatili sa iba't ibang session, karaniwang sa pamamagitan ng database, vector index, o iba pang permanenteng imbakan.

**Halimbawa ng Short Term Memory**

Kung magtatanong ang gumagamit, "Magkano ang presyo ng flight papuntang Paris?" at pagkatapos ay susundan ng "Paano naman ang akomodasyon doon?", sinisigurado ng short-term memory na alam ng agent na ang "doon" ay tumutukoy sa "Paris" sa loob ng parehong pag-uusap.

#### Long Term Memory

Ito ang impormasyon na nananatili sa maraming pag-uusap o sesyon. Pinapayagan nito ang mga agent na maalala ang mga kagustuhan ng gumagamit, pangkasaysayang interaksyon, o pangkalahatang kaalaman sa matagal na panahon. Mahalaga ito para sa personalisasyon.

**Halimbawa ng Long Term Memory**

Maaaring itala ng long-term memory na "Mahilig si Ben sa skiing at mga gawain sa labas, gusto niya ng kape na may tanawin ng bundok, at nais niyang iwasan ang mga advanced na ski slope dahil sa isang nakaraang pinsala". Ang impormasyong ito, na natutunan mula sa mga nagdaang interaksyon, ay nakakaapekto sa mga rekomendasyon sa mga susunod na sesyon ng pagpaplano ng biyahe, kaya't nagiging napaka-personalized ang mga ito.

#### Persona Memory

Ang espesyal na uri ng memoryang ito ay tumutulong sa agent na magkaroon ng konsistenteng "katauhan" o "persona". Pinapayagan nito ang agent na maalala ang mga detalye tungkol sa sarili nito o sa kanyang tinatangkang papel, na ginagawang mas maayos at nakatuon ang mga interaksyon.

**Halimbawa ng Persona Memory**  
Kung ang travel agent ay dinisenyo upang maging isang "ekspertong tagaplano ng ski," maaaring palakasin ng persona memory ang papel na ito, na nakakaimpluwensya sa mga tugon upang umayon sa tono at kaalaman ng isang eksperto.

#### Workflow/Episodic Memory

Ito ay isang memorya na nag-iimbak ng mga sunod-sunod na hakbang na ginawa ng agent sa isang komplikadong gawain, kabilang ang mga tagumpay at pagkabigo. Para itong pag-alala sa mga partikular na "episodyo" o nakaraang karanasan upang matuto mula rito.

**Halimbawa ng Episodic Memory**

Kung sinubukan ng agent na mag-book ng isang partikular na flight ngunit nabigo dahil sa hindi pagka-available, maaaring itala ng episodic memory ang pagkabigong ito, na nagbibigay-daan sa agent na subukan ang mga alternatibong flight o ipaalam sa gumagamit ang isyu sa mas maalam na paraan sa susunod na pagtatangka.

#### Entity Memory

Ito ay tungkol sa pagkuha at pag-alala ng mga partikular na entity (tulad ng tao, lugar, o bagay) at mga pangyayari mula sa mga pag-uusap. Pinapayagan nito ang agent na bumuo ng istrakturadong pag-unawa sa mga mahahalagang elementong tinalakay.

**Halimbawa ng Entity Memory**

Mula sa isang pag-uusap tungkol sa isang nakaraang biyahe, maaaring kunin ng agent ang "Paris," "Eiffel Tower," at "dinner sa Le Chat Noir restaurant" bilang mga entity. Sa isang susunod na interaksyon, maaaring alalahanin ng agent ang "Le Chat Noir" at ialok na gumawa ng bagong reserbasyon doon.

#### Structured RAG (Retrieval Augmented Generation)

Habang ang RAG ay mas malawak na teknik, ang "Structured RAG" ay itinatampok bilang isang makapangyarihang teknolohiya sa memorya. Kinukuha nito ang makapal at istrakturadong impormasyon mula sa iba't ibang pinagmulan (pag-uusap, email, larawan) at ginagamit ito upang mapabuti ang katumpakan, pag-alala, at bilis sa mga sagot. Hindi tulad ng klasikong RAG na umaasa lamang sa semantikong pagkakapareho, ang Structured RAG ay gumagana gamit ang likas na istraktura ng impormasyon.

**Halimbawa ng Structured RAG**

Sa halip na mag-match lamang ng mga keyword, maaaring i-parse ng Structured RAG ang mga detalye ng flight (destinasyon, petsa, oras, airline) mula sa isang email at iimbak ang mga ito sa nakaistrakturang paraan. Nagbibigay ito ng tumpak na mga query tulad ng "Anong flight ang na-book ko papuntang Paris noong Martes?"

## Pagpapatupad at Pag-iimbak ng Memorya

Ang pagpapatupad ng memorya para sa AI agents ay kinapapalooban ng sistematikong proseso ng **pamamahala ng memorya**, na kinabibilangan ng paggawa, pag-iimbak, pagkuha, pagsasama, pag-update, at maging ang "pagkalimot" (o pagtanggal) ng impormasyon. Mahalaga lalo ang retrieval.

### Espesyal na Mga Tool sa Memorya

#### Mem0

Isang paraan upang iimbak at pamahalaan ang memorya ng agent ay gamit ang mga espesyal na tool tulad ng Mem0. Gumagana ang Mem0 bilang isang persistent memory layer, na nagpapahintulot sa mga agent na maalala ang mga kaugnay na interaksyon, iimbak ang mga kagustuhan ng gumagamit at kontekstong makatotohanan, at matuto mula sa mga tagumpay at kabiguan sa paglipas ng panahon. Ang ideya rito ay nagiging stateful ang mga dating stateless na agent.

Gumagana ito sa pamamagitan ng **two-phase memory pipeline: extraction at update**. Una, ang mga mensaheng idinadagdag sa thread ng agent ay ipinapadala sa serbisyo ng Mem0, na gumagamit ng Large Language Model (LLM) upang ibuod ang kasaysayan ng pag-uusap at kunin ang mga bagong memorya. Sumunod, ang update phase na pinapatakbo ng LLM ang nagdedesisyon kung idaragdag, babaguhin, o tatanggalin ang mga memorya, at iniimbak ito sa isang hybrid data store na maaaring maglaman ng vector, graph, at key-value databases. Sinusuportahan ng sistemang ito ang iba't ibang uri ng memorya at maaaring magsama ng graph memory para sa pamamahala ng mga relasyon sa pagitan ng mga entity.

#### Cognee

Isa pang makapangyarihang paraan ay ang paggamit ng **Cognee**, isang open-source semantic memory para sa AI agents na nagbabago ng istrakturadong at hindi istrakturadong datos sa mga queryable knowledge graph na suportado ng embeddings. Nagbibigay ang Cognee ng **dual-store architecture** na pinagsasama ang vector similarity search at graph relationships, na nagpapahintulot sa mga agent na maunawaan hindi lamang kung ano ang magkahawig na impormasyon, kundi kung paano magkakaugnay ang mga konsepto.

Nangunguna ito sa **hybrid retrieval** na pinaghalo ang vector similarity, graph structure, at LLM reasoning - mula sa raw chunk lookup hanggang sa graph-aware na pagsagot ng tanong. Pinananatili ng sistema ang **living memory** na umuunlad at lumalago habang nananatiling queryable bilang isang magkakaugnay na graph, sinusuportahan ang parehong short-term session context at long-term persistent memory.

Ipinapakita sa Cognee notebook tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) kung paano bumuo ng pinag-isang memory layer na ito, na may praktikal na mga halimbawa ng pagkuha ng iba't ibang pinagmulan ng datos, pagpapakita ng knowledge graph, at pag-query gamit ang iba't ibang search strategies na iniangkop sa partikular na pangangailangan ng agent.

### Pag-iimbak ng Memorya gamit ang RAG

Bukod sa mga espesyal na tool sa memorya tulad ng mem0, maaari kang gumamit ng matibay na search services tulad ng **Azure AI Search bilang backend para sa pag-iimbak at pagkuha ng mga memorya**, lalo na para sa structured RAG.

Pinapayagan ka nitong gawing matibay ang sagot ng iyong agent gamit ang iyong sariling datos, na nagsisiguro ng mas kaugnayan at tumpak na mga sagot. Maaaring gamitin ang Azure AI Search upang mag-imbak ng mga memorya ng paglalakbay ng gumagamit, mga katalogo ng produkto, o anumang iba pang espesipikong kaalaman sa larangan.

Sinusuportahan ng Azure AI Search ang mga kakayahan tulad ng **Structured RAG**, na mahusay sa pagkuha at pagkuha ng makapal, istrakturadong impormasyon mula sa malalaking dataset tulad ng kasaysayan ng pag-uusap, mga email, o kahit mga larawan. Nagbibigay ito ng "superhuman precision and recall" kumpara sa tradisyunal na text chunking at embedding na mga pamamaraan.

## Paggawing Self-Improve ang AI Agents

Isang karaniwang pattern para sa self-improving agents ay ang pagpapakilala ng isang **"knowledge agent"**. Ang hiwalay na agent na ito ay nag-oobserba sa pangunahing pag-uusap sa pagitan ng gumagamit at ng pangunahing agent. Ang papel nito ay:

1. **Tukuyin ang mahalagang impormasyon**: Alamin kung aling bahagi ng pag-uusap ang karapat-dapat i-save bilang pangkalahatang kaalaman o partikular na kagustuhan ng gumagamit.

2. **Kunin at ibuod**: Salain ang mahalagang aral o kagustuhan mula sa pag-uusap.

3. **I-imbak sa knowledge base**: Permanente itong itatago, madalas sa vector database, upang maibalik sa ibang pagkakataon.

4. **Palakasin ang mga susunod na query**: Kapag nagsimula ang gumagamit ng bagong query, kinukuha ng knowledge agent ang kaugnay na naimbak na impormasyon at idinadagdag ito sa prompt ng gumagamit, na nagbibigay ng mahalagang konteksto sa pangunahing agent (katulad ng RAG).

### Mga Pag-optimize para sa Memorya

• **Pag-manage ng Latency**: Upang maiwasang bumagal ang interaksyon ng gumagamit, maaaring gumamit muna ng mas murang, mas mabilis na modelo upang mabilis na suriin kung mahalaga ang impormasyon na iimbak o kukunin, at tatawagin lamang ang mas kumplikadong proseso ng extraction/retrieval kung kinakailangan.

• **Pagpapanatili ng Knowledge Base**: Para sa lumalaking knowledge base, ang hindi gaanong madalas gamitin na impormasyon ay maaaring ilipat sa "cold storage" upang mapamahalaan ang gastos.

## May Karagdagang Tanong Tungkol sa Agent Memory?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa iba pang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->