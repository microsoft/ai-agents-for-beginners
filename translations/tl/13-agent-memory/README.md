# Memory para sa Mga AI Agent 
[![Memorya ng Ahente](../../../translated_images/tl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kapag pinag-uusapan ang mga natatanging benepisyo ng paggawa ng mga AI Agent, dalawang bagay ang pangunahing pinag-uusapan: ang kakayahang tumawag ng mga tool upang kumpletuhin ang mga gawain at ang kakayahang umunlad sa paglipas ng panahon. Ang memorya ang nasa pundasyon ng paglikha ng self-improving na agent na makagagawa ng mas magagandang karanasan para sa ating mga gumagamit.

Sa leksyong ito, titingnan natin kung ano ang memorya para sa mga AI Agent at kung paano natin ito pamamahalaan at gagamitin para sa kapakinabangan ng ating mga aplikasyon.

## Introduction

Saklaw ng leksyong ito:

• **Understanding AI Agent Memory**: Ano ang memorya at bakit mahalaga ito para sa mga agent.

• **Implementing and Storing Memory**: Mga praktikal na pamamaraan para idagdag ang kakayahan ng memorya sa iyong mga AI agent, na nakatuon sa short-term at long-term memory.

• **Making AI Agents Self-Improving**: Paano pinapagana ng memorya ang mga agent na matuto mula sa mga nakaraang interaksyon at umunlad sa paglipas ng panahon.

## Available Implementations

Kasama sa leksyong ito ang dalawang komprehensibong notebook tutorial:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Nagpapatupad ng memorya gamit ang Mem0 at Azure AI Search kasama ang Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Nagpapatupad ng structured memory gamit ang Cognee, awtomatikong bumubuo ng knowledge graph na suportado ng embeddings, binibigyan ng biswal na presentasyon ang graph, at matalinong retrieval

## Learning Goals

Pagkatapos matapos ang leksyong ito, malalaman mo kung paano:

• **Ihugpong ang pagkakaiba sa pagitan ng iba't ibang uri ng memorya ng AI agent**, kabilang ang working, short-term, at long-term memory, pati na rin ang mga espesyal na anyo tulad ng persona at episodic memory.

• **Magpatupad at pamahalaan ang short-term at long-term memory para sa mga AI agent** gamit ang Microsoft Agent Framework, na ginagamit ang mga tool tulad ng Mem0, Cognee, Whiteboard memory, at pag-integrate sa Azure AI Search.

• **Maunawaan ang mga prinsipyo sa likod ng self-improving na AI agent** at kung paano ang matibay na sistema ng pamamahala ng memorya ay nakakatulong sa tuloy-tuloy na pagkatuto at pag-aangkop.

## Understanding AI Agent Memory

Sa pinakapayak na kahulugan, **ang memorya para sa mga AI agent ay tumutukoy sa mga mekanismong nagpapahintulot sa kanila na magtanggap at magbalik-tanaw ng impormasyon**. Ang impormasyong ito ay maaaring mga tiyak na detalye tungkol sa isang pag-uusap, mga kagustuhan ng gumagamit, mga nagdaang aksyon, o kahit mga natutunang pattern.

Kung walang memorya, ang mga AI application ay kadalasang stateless, ibig sabihin bawat interaksyon ay nagsisimula mula sa simula. Ito ay humahantong sa paulit-ulit at nakakainis na karanasan ng gumagamit kung saan ang agent ay "nakakalimot" ng naunang konteksto o mga kagustuhan.

### Why is Memory Important?

ang intelligence ng isang agent ay malalim na nakaugnay sa kakayahan nitong alalahanin at gamitin ang nakaraang impormasyon. Pinapahintulutan ng memorya ang mga agent na maging:

• **Reflective**: Natututo mula sa mga nagdaang aksyon at kinalabasan.

• **Interactive**: Pinapanatili ang konteksto sa isang nagpapatuloy na pag-uusap.

• **Proactive and Reactive**: Naghuhula ng pangangailangan o tumutugon nang angkop batay sa historikal na data.

• **Autonomous**: Gumagana nang mas malaya sa pamamagitan ng pagkuha mula sa nakaimbak na kaalaman.

Ang layunin ng pagpapatupad ng memorya ay gawing mas **mapagkakatiwalaan at may kakayahan** ang mga agent.

### Types of Memory

#### Working Memory

Isipin ito bilang isang piraso ng scratch paper na ginagamit ng agent sa loob ng isang nagaganap na gawain o proseso ng pag-iisip. Ito ay naglalaman ng agarang impormasyon na kailangan upang kalkulahin ang susunod na hakbang.

Para sa mga AI agent, ang working memory ay madalas na kumukuha ng pinaka-makabuluhang impormasyon mula sa isang pag-uusap, kahit na mahaba o na-truncate ang buong chat history. Nakatuon ito sa pagkuha ng mga pangunahing elemento tulad ng mga kinakailangan, panukala, desisyon, at mga aksyon.

**Working Memory Example**

Sa isang travel booking agent, maaaring kunin ng working memory ang kasalukuyang kahilingan ng gumagamit, tulad ng "Gusto kong mag-book ng biyahe papuntang Paris". Itong tiyak na kinakailangan ay hinahawakan sa agarang konteksto ng agent upang gabayan ang kasalukuyang interaksyon.

#### Short Term Memory

Ang uri ng memoryang ito ay nag-iimbak ng impormasyon para sa haba ng isang solong pag-uusap o session. Ito ang konteksto ng kasalukuyang chat, na nagpapahintulot sa agent na tumukoy pabalik sa mga naunang turn sa diyalogo.

**Short Term Memory Example**

Kung ang isang gumagamit ay magtatanong, "Magkano ang aabutin ng flight papuntang Paris?" at pagkatapos ay susundan ng "Paano naman ang matutuluyan doon?", tinitiyak ng short-term memory na alam ng agent na ang "doon" ay tumutukoy sa "Paris" sa loob ng parehong pag-uusap.

#### Long Term Memory

Ito ang impormasyon na nananatili sa maraming pag-uusap o session. Pinapahintulutan nito ang mga agent na tandaan ang mga kagustuhan ng gumagamit, mga historikal na interaksyon, o pangkalahatang kaalaman sa mahabang panahon. Mahalaga ito para sa personalization.

**Long Term Memory Example**

Maaaring mag-imbak ang long-term memory na "Si Ben ay mahilig sa skiing at mga outdoor na aktibidad, gusto ng kape na may tanawin ng bundok, at nais iwasan ang mga advanced na ski slopes dahil sa isang dating pinsala". Ang impormasyong ito, na natutunan mula sa mga nakaraang interaksyon, ay nakakaimpluwensya sa mga rekomendasyon sa mga susunod na session ng pagpaplano ng paglalakbay, na ginagawang mas naangkop sa personal.

#### Persona Memory

Ang espesyalisadong uri ng memoryang ito ay tumutulong sa isang agent na bumuo ng isang konsistenteng "personality" o "persona". Pinapahintulutan nito ang agent na tandaan ang mga detalye tungkol sa sarili nito o ang itinakdang papel nito, ginagawa ang mga interaksyon na mas maayos at naka-tuon.

**Persona Memory Example**
Kung ang travel agent ay dinisenyo upang maging isang "expert ski planner," maaaring patatagin ng persona memory ang papel na ito, na nakaimpluwensya sa mga tugon nito upang umayon sa tono at kaalaman ng isang eksperto.

#### Workflow/Episodic Memory

Ang memoryang ito ay nag-iimbak ng pagkakasunod-sunod ng mga hakbang na ginawa ng agent sa isang kumplikadong gawain, kasama ang mga tagumpay at pagkabigo. Parang pag-alala sa mga partikular na "episodes" o karanasan upang matuto mula sa mga ito.

**Episodic Memory Example**

Kung sinubukan ng agent na mag-book ng isang partikular na flight ngunit nabigo dahil hindi available, maaaring irekord ng episodic memory ang pagkabigong ito, na nagpapahintulot sa agent na subukan ang mga alternatibong flight o ipaalam sa gumagamit ang isyu nang mas may kaalaman sa susunod na pagtatangka.

#### Entity Memory

Kasama rito ang pagkuha at pag-alala ng mga partikular na entity (tulad ng mga tao, lugar, o bagay) at mga kaganapan mula sa mga pag-uusap. Pinapahintulutan nito ang agent na bumuo ng isang istrukturadong pag-unawa sa mga pangunahing elemento na napag-usapan.

**Entity Memory Example**

Mula sa isang pag-uusap tungkol sa isang nakaraang biyahe, maaaring kunin ng agent ang "Paris," "Eiffel Tower," at "dinner at Le Chat Noir restaurant" bilang mga entity. Sa isang susunod na interaksyon, maaaring maalala ng agent ang "Le Chat Noir" at mag-alok na magpareserba doon muli.

#### Structured RAG (Retrieval Augmented Generation)

Habang ang RAG ay isang mas malawak na teknik, ang "Structured RAG" ay binibigyang-diin bilang isang makapangyarihang teknolohiya ng memorya. Kinukuha nito ang makapal, istrukturadong impormasyon mula sa iba't ibang mga pinagmulan (mga pag-uusap, email, larawan) at ginagamit ito upang mapabuti ang precision, recall, at bilis sa mga tugon. Hindi tulad ng klasikong RAG na umaasa lamang sa semantic similarity, ang Structured RAG ay gumagana kasama ang likas na istruktura ng impormasyon.

**Structured RAG Example**

Sa halip na simpleng tumugma ng mga keyword, maaaring i-parse ng Structured RAG ang mga detalye ng flight (destinasyon, petsa, oras, airline) mula sa isang email at iimbak ang mga ito sa isang istrukturadong paraan. Ito ay nagpapahintulot ng tumpak na mga query tulad ng "Anong flight ang na-book ko papuntang Paris noong Martes?"

## Implementing and Storing Memory

Ang pagpapatupad ng memorya para sa mga AI agent ay nagsasangkot ng isang sistematikong proseso ng **pamamahala ng memorya**, na kinabibilangan ng pagbuo, pag-iimbak, pag-retrieve, pag-integrate, pag-update, at maging ang "pagkakalimot" (o pagtanggal) ng impormasyon. Ang retrieval ay isang partikular na mahalagang aspeto.

### Specialized Memory Tools

#### Mem0

Isang paraan upang mag-imbak at pamahalaan ang memorya ng agent ay ang paggamit ng mga espesyal na tool tulad ng Mem0. Gumagana ang Mem0 bilang isang persistent memory layer, na nagpapahintulot sa mga agent na maalala ang mga may-katuturang interaksyon, iimbak ang mga kagustuhan ng gumagamit at factual context, at matuto mula sa mga tagumpay at pagkabigo sa paglipas ng panahon. Ang ideya dito ay ang mga stateless na agent ay nagiging stateful.

Gumagana ito sa pamamagitan ng isang **two-phase memory pipeline: extraction and update**. Una, ang mga mensaheng idinadagdag sa thread ng agent ay ipinapadala sa Mem0 service, na gumagamit ng isang Large Language Model (LLM) upang ibuod ang conversation history at mag-extract ng mga bagong memorya. Kasunod nito, isang LLM-driven update phase ang tumutukoy kung idaragdag, babaguhin, o tatanggalin ang mga memoryang ito, iniimbak ang mga ito sa isang hybrid data store na maaaring magsama ng vector, graph, at key-value databases. Sinusuportahan din ng sistemang ito ang iba't ibang uri ng memorya at maaaring magsama ng graph memory para sa pamamahala ng mga relasyon sa pagitan ng mga entity.

#### Cognee

Isa pang makapangyarihang pamamaraan ang paggamit ng **Cognee**, isang open-source semantic memory para sa mga AI agent na naglalapat ng istrukturado at hindi istrukturadong data sa mga queryable knowledge graph na suportado ng embeddings. Nagbibigay ang Cognee ng isang **dual-store architecture** na pinaghalo ang vector similarity search sa mga graph relationship, na nagpapahintulot sa mga agent na maunawaan hindi lamang kung ano ang magkapareho ng impormasyon, kundi kung paano magkakaugnay ang mga konsepto sa isa't isa.

Namumukod ito sa **hybrid retrieval** na pinaglalagay ang vector similarity, graph structure, at LLM reasoning - mula sa raw chunk lookup hanggang sa graph-aware question answering. Pinapanatili ng sistema ang **living memory** na umuunlad at lumalago habang nananatiling queryable bilang isang konektadong graph, sumusuporta sa parehong short-term session context at long-term persistent memory.

Ipinapakita ng Cognee notebook tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) kung paano bumuo ng pinag-isang memory layer na ito, kasama ang mga praktikal na halimbawa ng pag-ingest ng iba't ibang pinagmulan ng data, pagbibigay-biswal sa knowledge graph, at pag-query gamit ang iba't ibang search strategies na iniangkop sa partikular na pangangailangan ng agent.

### Storing Memory with RAG

Bukod sa mga espesyal na tool ng memorya tulad ng mem0 , maaari mong gamitin ang matibay na search services tulad ng **Azure AI Search as a backend for storing and retrieving memories**, lalo na para sa structured RAG.

Pinahihintulutan ka nitong i-ground ang mga tugon ng iyong agent gamit ang iyong sariling data, na tinitiyak ang mas may-katuturan at mas tumpak na mga sagot. Maaaring gamitin ang Azure AI Search upang mag-imbak ng mga user-specific travel memories, product catalogs, o anumang iba pang domain-specific na kaalaman.

Sinusuportahan ng Azure AI Search ang mga kakayahan tulad ng **Structured RAG**, na magaling sa pagkuha at pag-retrieve ng makapal, istrukturadong impormasyon mula sa malalaking dataset tulad ng conversation histories, email, o kahit mga larawan. Nagbibigay ito ng "superhuman precision and recall" kumpara sa tradisyonal na text chunking at embedding approaches.

## Making AI Agents Self-Improve

Isang karaniwang pattern para sa self-improving agents ay ang pagpapakilala ng isang **"knowledge agent"**. Ang hiwalay na agent na ito ay nagmamasid sa pangunahing pag-uusap sa pagitan ng gumagamit at ng pangunahing agent. Ang papel nito ay:

1. **Identify valuable information**: Tukuyin kung ang anumang bahagi ng pag-uusap ay karapat-dapat na i-save bilang pangkalahatang kaalaman o isang partikular na kagustuhan ng gumagamit.

2. **Extract and summarize**: Alisin at ibuod ang mahalagang natutunan o kagustuhan mula sa pag-uusap.

3. **Store in a knowledge base**: I-imbak ang na-extract na impormasyong ito, madalas sa isang vector database, upang maaari itong ma-retrieve sa hinaharap.

4. **Augment future queries**: Kapag nagsimula ang gumagamit ng bagong query, binabawi ng knowledge agent ang may-katuturang nakaimbak na impormasyon at idinadagdag ito sa prompt ng gumagamit, na nagbibigay ng mahalagang konteksto sa pangunahing agent (kahalintulad ng RAG).

### Optimizations for Memory

• **Latency Management**: Upang hindi pabagalin ang mga interaksyon ng gumagamit, isang mas mura at mas mabilis na modelo ang maaaring gamitin muna upang mabilis na suriin kung ang impormasyon ay mahalagang i-imbak o i-retrieve, at tatawag lamang sa mas kumplikadong extraction/retrieval process kapag kinakailangan.

• **Knowledge Base Maintenance**: Para sa lumalaking knowledge base, ang hindi gaanong madalas gamitin na impormasyon ay maaaring ilipat sa "cold storage" upang pamahalaan ang mga gastos.

## Got More Questions About Agent Memory?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Paunawa:
Isinalin ang dokumentong ito gamit ang serbisyong pagsasalin na AI na Co-op Translator (https://github.com/Azure/co-op-translator). Bagaman sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa kritikal na impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->