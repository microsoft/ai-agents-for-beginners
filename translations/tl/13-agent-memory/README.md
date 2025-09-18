<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1923cf93aba522a5f4a493597112a893",
  "translation_date": "2025-09-18T16:18:29+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "tl"
}
-->
# Memory para sa AI Agents

Kapag pinag-uusapan ang mga natatanging benepisyo ng paglikha ng AI Agents, dalawang bagay ang kadalasang binibigyang pansin: ang kakayahang gumamit ng mga tool para tapusin ang mga gawain at ang kakayahang mag-improve sa paglipas ng panahon. Ang memorya ang pundasyon ng paglikha ng self-improving agent na makakagawa ng mas mahusay na karanasan para sa ating mga user.

Sa araling ito, tatalakayin natin kung ano ang memorya para sa AI Agents at kung paano natin ito pamamahalaan at gagamitin para sa kapakinabangan ng ating mga aplikasyon.

## Panimula

Ang araling ito ay sasaklaw sa:

• **Pag-unawa sa Memorya ng AI Agent**: Ano ang memorya at bakit ito mahalaga para sa mga agent.

• **Pagpapatupad at Pag-iimbak ng Memorya**: Praktikal na mga paraan para magdagdag ng memory capabilities sa iyong AI agents, na nakatuon sa short-term at long-term memory.

• **Pagpapahusay ng AI Agents**: Paano nagagamit ang memorya para matuto ang mga agent mula sa nakaraang interaksyon at mag-improve sa paglipas ng panahon.

## Mga Layunin sa Pag-aaral

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano:

• **Pag-iba-ibahin ang iba't ibang uri ng memorya ng AI agent**, kabilang ang working, short-term, at long-term memory, pati na rin ang mga espesyal na anyo tulad ng persona at episodic memory.

• **Ipapatupad at pamahalaan ang short-term at long-term memory para sa AI agents** gamit ang Semantic Kernel framework, gamit ang mga tool tulad ng Mem0 at Whiteboard memory, at pag-integrate sa Azure AI Search.

• **Unawain ang mga prinsipyo sa likod ng self-improving AI agents** at kung paano nakakatulong ang matibay na memory management systems sa tuloy-tuloy na pag-aaral at pag-aangkop.

## Pag-unawa sa Memorya ng AI Agent

Sa pinakapundasyon nito, **ang memorya para sa AI agents ay tumutukoy sa mga mekanismo na nagpapahintulot sa kanila na magpanatili at magbalik ng impormasyon**. Ang impormasyong ito ay maaaring mga detalye tungkol sa isang pag-uusap, mga kagustuhan ng user, nakaraang aksyon, o kahit mga natutunang pattern.

Kung walang memorya, ang mga AI application ay kadalasang stateless, ibig sabihin, bawat interaksyon ay nagsisimula mula sa simula. Nagdudulot ito ng paulit-ulit at nakakainis na karanasan para sa user kung saan "nakakalimutan" ng agent ang nakaraang konteksto o mga kagustuhan.

### Bakit Mahalaga ang Memorya?

Ang katalinuhan ng isang agent ay malapit na konektado sa kakayahan nitong magbalik at gumamit ng nakaraang impormasyon. Ang memorya ay nagpapahintulot sa mga agent na maging:

• **Reflective**: Natututo mula sa nakaraang mga aksyon at resulta.

• **Interactive**: Pinapanatili ang konteksto sa isang tuloy-tuloy na pag-uusap.

• **Proactive at Reactive**: Ina-anticipate ang mga pangangailangan o tumutugon nang naaayon batay sa historical data.

• **Autonomous**: Mas independent na gumagana sa pamamagitan ng paggamit ng nakaimbak na kaalaman.

Ang layunin ng pagpapatupad ng memorya ay gawing mas **maaasahan at may kakayahan** ang mga agent.

### Mga Uri ng Memorya

#### Working Memory

Isipin ito bilang isang piraso ng scratch paper na ginagamit ng agent sa isang solong, tuloy-tuloy na gawain o proseso ng pag-iisip. Nagtatago ito ng agarang impormasyon na kailangan para sa susunod na hakbang.

Para sa AI agents, ang working memory ay kadalasang kumukuha ng pinaka-relevant na impormasyon mula sa isang pag-uusap, kahit na mahaba o truncated ang buong chat history. Nakatuon ito sa pagkuha ng mga pangunahing elemento tulad ng mga kinakailangan, panukala, desisyon, at aksyon.

**Halimbawa ng Working Memory**

Sa isang travel booking agent, maaaring makuha ng working memory ang kasalukuyang kahilingan ng user, tulad ng "Gusto kong mag-book ng biyahe papuntang Paris". Ang partikular na kinakailangang ito ay pinapanatili sa agarang konteksto ng agent para gabayan ang kasalukuyang interaksyon.

#### Short Term Memory

Ang ganitong uri ng memorya ay nagtatago ng impormasyon sa tagal ng isang pag-uusap o session. Ito ang konteksto ng kasalukuyang chat, na nagpapahintulot sa agent na bumalik sa mga nakaraang bahagi ng dialogue.

**Halimbawa ng Short Term Memory**

Kung ang user ay magtanong, "Magkano ang flight papuntang Paris?" at pagkatapos ay mag-follow up ng "Paano naman ang accommodation doon?", tinitiyak ng short-term memory na alam ng agent na ang "doon" ay tumutukoy sa "Paris" sa parehong pag-uusap.

#### Long Term Memory

Ito ang impormasyon na nananatili sa maraming pag-uusap o session. Pinapayagan nito ang mga agent na tandaan ang mga kagustuhan ng user, mga nakaraang interaksyon, o pangkalahatang kaalaman sa mahabang panahon. Mahalaga ito para sa personalization.

**Halimbawa ng Long Term Memory**

Ang long-term memory ay maaaring mag-imbak ng "Si Ben ay mahilig sa skiing at outdoor activities, gusto ng kape na may tanawin ng bundok, at nais iwasan ang advanced ski slopes dahil sa nakaraang injury". Ang impormasyong ito, na natutunan mula sa mga nakaraang interaksyon, ay nakakaimpluwensya sa mga rekomendasyon sa mga susunod na travel planning session, na ginagawang highly personalized ang mga ito.

#### Persona Memory

Ang ganitong uri ng memorya ay tumutulong sa agent na magkaroon ng consistent na "personality" o "persona". Pinapayagan nito ang agent na tandaan ang mga detalye tungkol sa sarili nito o sa intended role nito, na ginagawang mas natural at nakatuon ang mga interaksyon.

**Halimbawa ng Persona Memory**

Kung ang travel agent ay idinisenyo bilang isang "expert ski planner," maaaring palakasin ng persona memory ang role na ito, na nakakaimpluwensya sa mga sagot nito upang umayon sa tono at kaalaman ng isang eksperto.

#### Workflow/Episodic Memory

Ang memoryang ito ay nagtatago ng sequence ng mga hakbang na ginawa ng agent sa isang kumplikadong gawain, kabilang ang mga tagumpay at pagkabigo. Para itong pag-alala sa mga partikular na "episodes" o nakaraang karanasan upang matuto mula sa mga ito.

**Halimbawa ng Episodic Memory**

Kung sinubukan ng agent na mag-book ng isang partikular na flight ngunit nabigo dahil sa unavailability, maaaring i-record ng episodic memory ang pagkabigo na ito, na nagpapahintulot sa agent na subukan ang mga alternatibong flight o ipaalam sa user ang isyu sa mas maalam na paraan sa susunod na pagtatangka.

#### Entity Memory

Ito ay tumutukoy sa pagkuha at pag-alala ng mga partikular na entity (tulad ng tao, lugar, o bagay) at mga kaganapan mula sa mga pag-uusap. Pinapayagan nito ang agent na bumuo ng structured na pag-unawa sa mga pangunahing elementong tinalakay.

**Halimbawa ng Entity Memory**

Mula sa isang pag-uusap tungkol sa nakaraang biyahe, maaaring makuha ng agent ang "Paris," "Eiffel Tower," at "hapunan sa Le Chat Noir restaurant" bilang mga entity. Sa isang susunod na interaksyon, maaaring maalala ng agent ang "Le Chat Noir" at mag-alok na mag-reserve muli doon.

#### Structured RAG (Retrieval Augmented Generation)

Habang ang RAG ay isang mas malawak na teknolohiya, ang "Structured RAG" ay binibigyang-diin bilang isang makapangyarihang memory technology. Kumukuha ito ng dense, structured na impormasyon mula sa iba't ibang sources (mga pag-uusap, email, larawan) at ginagamit ito para mapahusay ang precision, recall, at bilis ng mga sagot. Hindi tulad ng classic RAG na umaasa lamang sa semantic similarity, ang Structured RAG ay gumagana sa inherent structure ng impormasyon.

**Halimbawa ng Structured RAG**

Sa halip na mag-match lang ng keywords, maaaring i-parse ng Structured RAG ang mga detalye ng flight (destinasyon, petsa, oras, airline) mula sa isang email at i-store ang mga ito sa structured na paraan. Pinapayagan nito ang mga precise na query tulad ng "Anong flight ang na-book ko papuntang Paris sa Martes?"

## Pagpapatupad at Pag-iimbak ng Memorya

Ang pagpapatupad ng memorya para sa AI agents ay nangangailangan ng sistematikong proseso ng **memory management**, na kinabibilangan ng pagbuo, pag-iimbak, pagkuha, pag-integrate, pag-update, at kahit "pagkalimot" (o pag-delete) ng impormasyon. Ang retrieval ay isang partikular na mahalagang aspeto.

### Mga Specialized Memory Tools

Isa sa mga paraan para mag-imbak at pamahalaan ang memorya ng agent ay ang paggamit ng mga specialized tools tulad ng Mem0. Ang Mem0 ay gumagana bilang isang persistent memory layer, na nagpapahintulot sa mga agent na maalala ang mga relevant na interaksyon, mag-imbak ng mga kagustuhan ng user at factual context, at matuto mula sa mga tagumpay at pagkabigo sa paglipas ng panahon. Ang ideya dito ay ang stateless agents ay nagiging stateful.

Gumagana ito sa pamamagitan ng **two-phase memory pipeline: extraction at update**. Una, ang mga mensaheng idinagdag sa thread ng agent ay ipinapadala sa Mem0 service, na gumagamit ng Large Language Model (LLM) para i-summarize ang history ng pag-uusap at kunin ang mga bagong memorya. Pagkatapos, ang LLM-driven update phase ay nagdedesisyon kung magdadagdag, magbabago, o magde-delete ng mga memoryang ito, na ini-store sa hybrid data store na maaaring maglaman ng vector, graph, at key-value databases. Sinusuportahan din ng sistemang ito ang iba't ibang uri ng memorya at maaaring mag-integrate ng graph memory para sa pamamahala ng mga relasyon sa pagitan ng mga entity.

### Pag-iimbak ng Memorya gamit ang RAG

Bukod sa mga specialized memory tools tulad ng Mem0, maaari kang gumamit ng mga robust search services tulad ng **Azure AI Search bilang backend para sa pag-iimbak at pagkuha ng mga memorya**, lalo na para sa structured RAG.

Pinapayagan nito ang grounding ng mga sagot ng agent gamit ang sariling data, na tinitiyak ang mas relevant at accurate na mga sagot. Ang Azure AI Search ay maaaring gamitin para mag-imbak ng mga user-specific travel memories, product catalogs, o anumang domain-specific na kaalaman.

Sinusuportahan ng Azure AI Search ang mga kakayahan tulad ng **Structured RAG**, na mahusay sa pagkuha at pag-retrieve ng dense, structured na impormasyon mula sa malalaking datasets tulad ng history ng pag-uusap, email, o kahit mga larawan. Nagbibigay ito ng "superhuman precision and recall" kumpara sa tradisyunal na text chunking at embedding approaches.

## Pagpapahusay ng AI Agents

Isang karaniwang pattern para sa self-improving agents ay ang pagpapakilala ng **"knowledge agent"**. Ang hiwalay na agent na ito ay nagmamasid sa pangunahing pag-uusap sa pagitan ng user at ng pangunahing agent. Ang role nito ay:

1. **Tukuyin ang mahalagang impormasyon**: Alamin kung may bahagi ng pag-uusap na mahalagang i-save bilang general knowledge o partikular na kagustuhan ng user.

2. **Kunin at i-summarize**: Distill ang mahalagang learning o preference mula sa pag-uusap.

3. **I-store sa knowledge base**: I-persist ang nakuha na impormasyon, kadalasang sa vector database, para ma-retrieve ito sa hinaharap.

4. **Palakasin ang mga susunod na query**: Kapag nag-initiate ang user ng bagong query, kinukuha ng knowledge agent ang relevant na nakaimbak na impormasyon at ina-append ito sa prompt ng user, na nagbibigay ng mahalagang konteksto sa pangunahing agent (katulad ng RAG).

### Mga Optimization para sa Memorya

• **Pamamahala ng Latency**: Para maiwasan ang pagbagal ng interaksyon ng user, maaaring gumamit ng mas mura at mas mabilis na modelo sa simula para mabilis na suriin kung mahalagang i-store o i-retrieve ang impormasyon, at gagamitin lamang ang mas kumplikadong proseso ng extraction/retrieval kapag kinakailangan.

• **Pagpapanatili ng Knowledge Base**: Para sa lumalaking knowledge base, ang mas madalang gamitin na impormasyon ay maaaring ilipat sa "cold storage" para makatipid sa gastos.

## May Karagdagang Tanong Tungkol sa Context Engineering?

Sumali sa [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) para makipag-usap sa ibang mga nag-aaral, dumalo sa office hours, at makuha ang sagot sa iyong mga tanong tungkol sa AI Agents.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.