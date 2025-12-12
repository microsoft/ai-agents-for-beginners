<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1d90991499ad697c4ad24decaf36968",
  "translation_date": "2025-12-09T12:37:18+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "tl"
}
-->
# Memory para sa AI Agents 
[![Memory ng Agent](../../../translated_images/lesson-13-thumbnail.959e3bc52d210c64a614a3bece6b170a2c472138dc0a14c7fbde07306ef95ae7.tl.png)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kapag pinag-uusapan ang mga natatanging benepisyo ng paglikha ng AI Agents, dalawang bagay ang karaniwang binibigyang-diin: ang kakayahang gumamit ng mga tool para tapusin ang mga gawain at ang kakayahang mag-improve sa paglipas ng panahon. Ang memorya ang pundasyon ng paglikha ng self-improving agent na makakapagbigay ng mas mahusay na karanasan para sa ating mga user.

Sa araling ito, tatalakayin natin kung ano ang memorya para sa AI Agents at kung paano natin ito mapapamahalaan at magagamit para sa kapakinabangan ng ating mga aplikasyon.

## Panimula

Saklaw ng araling ito ang:

• **Pag-unawa sa Memorya ng AI Agent**: Ano ang memorya at bakit ito mahalaga para sa mga agent.

• **Pagpapatupad at Pag-iimbak ng Memorya**: Praktikal na mga paraan para magdagdag ng kakayahan sa memorya sa iyong AI agents, na nakatuon sa short-term at long-term memory.

• **Pagpapahusay ng AI Agents**: Paano nagagamit ang memorya upang matuto ang mga agent mula sa nakaraang interaksyon at mag-improve sa paglipas ng panahon.

## Mga Magagamit na Implementasyon

Kasama sa araling ito ang dalawang komprehensibong notebook tutorial:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Nagpapatupad ng memorya gamit ang Mem0 at Azure AI Search sa Semantic Kernel framework.

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Nagpapatupad ng structured memory gamit ang Cognee, awtomatikong gumagawa ng knowledge graph na suportado ng embeddings, nag-visualize ng graph, at may intelligent retrieval.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano:

• **Pag-iba-ibahin ang iba't ibang uri ng memorya ng AI agent**, kabilang ang working, short-term, at long-term memory, pati na rin ang mga espesyal na anyo tulad ng persona at episodic memory.

• **Ipapatupad at pamahalaan ang short-term at long-term memory para sa AI agents** gamit ang Semantic Kernel framework, gamit ang mga tool tulad ng Mem0, Cognee, Whiteboard memory, at pagsasama sa Azure AI Search.

• **Maunawaan ang mga prinsipyo sa likod ng self-improving AI agents** at kung paano nakakatulong ang matatag na memory management systems sa tuloy-tuloy na pagkatuto at pag-aangkop.

## Pag-unawa sa Memorya ng AI Agent

Sa pinakapayak na anyo, **ang memorya para sa AI agents ay tumutukoy sa mga mekanismo na nagpapahintulot sa kanila na magpanatili at magbalik ng impormasyon**. Ang impormasyong ito ay maaaring mga detalye ng isang pag-uusap, mga kagustuhan ng user, mga nakaraang aksyon, o mga natutunang pattern.

Kung walang memorya, ang mga AI application ay madalas na stateless, ibig sabihin, bawat interaksyon ay nagsisimula mula sa simula. Nagdudulot ito ng paulit-ulit at nakakainis na karanasan para sa user kung saan "nakakalimutan" ng agent ang nakaraang konteksto o mga kagustuhan.

### Bakit Mahalaga ang Memorya?

Ang katalinuhan ng isang agent ay malapit na konektado sa kakayahan nitong maalala at magamit ang nakaraang impormasyon. Ang memorya ay nagpapahintulot sa mga agent na maging:

• **Reflective**: Natututo mula sa mga nakaraang aksyon at resulta.

• **Interactive**: Pinapanatili ang konteksto sa isang patuloy na pag-uusap.

• **Proactive at Reactive**: Nahuhulaan ang mga pangangailangan o tumutugon nang naaangkop batay sa nakaraang data.

• **Autonomous**: Mas nagiging independent sa pamamagitan ng paggamit ng nakaimbak na kaalaman.

Ang layunin ng pagpapatupad ng memorya ay gawing mas **maaasahan at may kakayahan** ang mga agent.

### Mga Uri ng Memorya

#### Working Memory

Isipin ito bilang isang piraso ng scratch paper na ginagamit ng agent sa isang solong gawain o proseso ng pag-iisip. Pinapanatili nito ang agarang impormasyon na kailangan para sa susunod na hakbang.

Para sa AI agents, ang working memory ay madalas na kumukuha ng pinaka-makabuluhang impormasyon mula sa isang pag-uusap, kahit na mahaba o putol-putol ang buong chat history. Nakatuon ito sa pagkuha ng mga pangunahing elemento tulad ng mga kinakailangan, panukala, desisyon, at aksyon.

**Halimbawa ng Working Memory**

Sa isang travel booking agent, maaaring makuha ng working memory ang kasalukuyang kahilingan ng user, tulad ng "Gusto kong mag-book ng biyahe papuntang Paris". Ang partikular na kahilingang ito ay nananatili sa agarang konteksto ng agent upang gabayan ang kasalukuyang interaksyon.

#### Short Term Memory

Ang ganitong uri ng memorya ay nagtatago ng impormasyon sa tagal ng isang pag-uusap o sesyon. Ito ang konteksto ng kasalukuyang chat, na nagpapahintulot sa agent na bumalik sa mga nakaraang bahagi ng diyalogo.

**Halimbawa ng Short Term Memory**

Kung ang isang user ay magtanong, "Magkano ang flight papuntang Paris?" at pagkatapos ay mag-follow up ng "Paano naman ang tirahan doon?", tinitiyak ng short-term memory na alam ng agent na ang "doon" ay tumutukoy sa "Paris" sa parehong pag-uusap.

#### Long Term Memory

Ito ay impormasyon na nananatili sa kabila ng maraming pag-uusap o sesyon. Pinapayagan nito ang mga agent na maalala ang mga kagustuhan ng user, mga nakaraang interaksyon, o pangkalahatang kaalaman sa mahabang panahon. Mahalaga ito para sa personalisasyon.

**Halimbawa ng Long Term Memory**

Ang long-term memory ay maaaring mag-imbak ng impormasyon tulad ng "Mahilig si Ben sa skiing at outdoor activities, gusto niya ng kape na may tanawin ng bundok, at nais niyang iwasan ang advanced ski slopes dahil sa isang nakaraang pinsala". Ang impormasyong ito, na natutunan mula sa mga nakaraang interaksyon, ay nakakaimpluwensya sa mga rekomendasyon sa mga susunod na sesyon ng pagpaplano ng biyahe, na ginagawang mas personal ang mga ito.

#### Persona Memory

Ang ganitong uri ng memorya ay tumutulong sa isang agent na bumuo ng isang pare-parehong "personalidad" o "persona". Pinapayagan nito ang agent na maalala ang mga detalye tungkol sa sarili nito o sa nilalayong papel nito, na ginagawang mas maayos at nakatuon ang mga interaksyon.

**Halimbawa ng Persona Memory**

Kung ang travel agent ay idinisenyo bilang isang "eksperto sa ski planning," maaaring palakasin ng persona memory ang papel na ito, na nakakaimpluwensya sa mga tugon nito upang umayon sa tono at kaalaman ng isang eksperto.

#### Workflow/Episodic Memory

Ang memoryang ito ay nagtatago ng pagkakasunod-sunod ng mga hakbang na ginagawa ng isang agent sa isang kumplikadong gawain, kabilang ang mga tagumpay at kabiguan. Para itong pag-alala sa mga partikular na "episode" o nakaraang karanasan upang matuto mula rito.

**Halimbawa ng Episodic Memory**

Kung sinubukan ng agent na mag-book ng isang partikular na flight ngunit nabigo dahil sa kawalan ng availability, maaaring i-record ng episodic memory ang kabiguang ito, na nagpapahintulot sa agent na subukan ang mga alternatibong flight o ipaalam sa user ang isyu sa mas may kaalamang paraan sa susunod na pagtatangka.

#### Entity Memory

Kasama rito ang pagkuha at pag-alala ng mga partikular na entity (tulad ng mga tao, lugar, o bagay) at mga kaganapan mula sa mga pag-uusap. Pinapayagan nito ang agent na bumuo ng isang structured na pag-unawa sa mga pangunahing elementong tinalakay.

**Halimbawa ng Entity Memory**

Mula sa isang pag-uusap tungkol sa isang nakaraang biyahe, maaaring makuha ng agent ang "Paris," "Eiffel Tower," at "hapunan sa Le Chat Noir restaurant" bilang mga entity. Sa isang hinaharap na interaksyon, maaaring maalala ng agent ang "Le Chat Noir" at mag-alok na mag-book muli ng reservation doon.

#### Structured RAG (Retrieval Augmented Generation)

Habang ang RAG ay isang mas malawak na teknolohiya, ang "Structured RAG" ay binibigyang-diin bilang isang makapangyarihang memory technology. Kinukuha nito ang masinsinang, structured na impormasyon mula sa iba't ibang mapagkukunan (mga pag-uusap, email, larawan) at ginagamit ito upang mapahusay ang precision, recall, at bilis ng mga tugon. Hindi tulad ng klasikong RAG na umaasa lamang sa semantic similarity, ang Structured RAG ay gumagana sa inherent na istruktura ng impormasyon.

**Halimbawa ng Structured RAG**

Sa halip na tumugma lamang sa mga keyword, maaaring i-parse ng Structured RAG ang mga detalye ng flight (destinasyon, petsa, oras, airline) mula sa isang email at iimbak ang mga ito sa isang structured na paraan. Pinapayagan nito ang mga eksaktong query tulad ng "Anong flight ang na-book ko papuntang Paris sa Martes?"

## Pagpapatupad at Pag-iimbak ng Memorya

Ang pagpapatupad ng memorya para sa AI agents ay nangangailangan ng sistematikong proseso ng **memory management**, na kinabibilangan ng pagbuo, pag-iimbak, pagkuha, pagsasama, pag-update, at kahit "pagkalimot" (o pagtanggal) ng impormasyon. Ang retrieval ay isang partikular na mahalagang aspeto.

### Mga Espesyal na Tool sa Memorya

#### Mem0

Isa sa mga paraan upang mag-imbak at pamahalaan ang memorya ng agent ay ang paggamit ng mga espesyal na tool tulad ng Mem0. Ang Mem0 ay gumagana bilang isang persistent memory layer, na nagpapahintulot sa mga agent na maalala ang mga kaugnay na interaksyon, mag-imbak ng mga kagustuhan ng user at factual context, at matuto mula sa mga tagumpay at kabiguan sa paglipas ng panahon. Ang ideya dito ay ang mga stateless agents ay nagiging stateful.

Gumagana ito sa pamamagitan ng isang **two-phase memory pipeline: extraction at update**. Una, ang mga mensaheng idinagdag sa thread ng agent ay ipinapadala sa Mem0 service, na gumagamit ng Large Language Model (LLM) upang ibuod ang kasaysayan ng pag-uusap at kunin ang mga bagong memorya. Pagkatapos, ang isang LLM-driven update phase ay tumutukoy kung idaragdag, babaguhin, o tatanggalin ang mga memoryang ito, na iniimbak ang mga ito sa isang hybrid data store na maaaring magsama ng vector, graph, at key-value databases. Sinusuportahan din ng sistemang ito ang iba't ibang uri ng memorya at maaaring isama ang graph memory para sa pamamahala ng mga relasyon sa pagitan ng mga entity.

#### Cognee

Isa pang makapangyarihang paraan ay ang paggamit ng **Cognee**, isang open-source semantic memory para sa AI agents na nagbabago ng structured at unstructured data sa queryable knowledge graphs na suportado ng embeddings. Nagbibigay ang Cognee ng **dual-store architecture** na pinagsasama ang vector similarity search sa graph relationships, na nagpapahintulot sa mga agent na maunawaan hindi lamang kung anong impormasyon ang magkatulad, kundi kung paano nauugnay ang mga konsepto sa isa't isa.

Mahusay ito sa **hybrid retrieval** na pinagsasama ang vector similarity, graph structure, at LLM reasoning - mula sa raw chunk lookup hanggang sa graph-aware question answering. Pinapanatili ng sistema ang **living memory** na patuloy na umuunlad at lumalago habang nananatiling queryable bilang isang konektadong graph, na sumusuporta sa parehong short-term session context at long-term persistent memory.

Ang Cognee notebook tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) ay nagpapakita ng paggawa ng unified memory layer na ito, na may mga praktikal na halimbawa ng pag-ingest ng iba't ibang mapagkukunan ng data, pag-visualize ng knowledge graph, at pag-query gamit ang iba't ibang search strategies na iniayon sa mga partikular na pangangailangan ng agent.

### Pag-iimbak ng Memorya gamit ang RAG

Bukod sa mga espesyal na tool sa memorya tulad ng Mem0, maaari mong gamitin ang mga matatag na search services tulad ng **Azure AI Search bilang backend para sa pag-iimbak at pagkuha ng mga memorya**, lalo na para sa structured RAG.

Pinapayagan ka nitong i-ground ang mga tugon ng iyong agent gamit ang sarili mong data, na tinitiyak ang mas may kaugnayan at tumpak na mga sagot. Ang Azure AI Search ay maaaring gamitin upang mag-imbak ng mga user-specific travel memories, product catalogs, o anumang iba pang domain-specific knowledge.

Sinusuportahan ng Azure AI Search ang mga kakayahan tulad ng **Structured RAG**, na mahusay sa pagkuha at pag-retrieve ng masinsinang, structured na impormasyon mula sa malalaking dataset tulad ng mga kasaysayan ng pag-uusap, email, o kahit mga larawan. Nagbibigay ito ng "superhuman precision and recall" kumpara sa tradisyunal na text chunking at embedding approaches.

## Pagpapahusay ng AI Agents

Isang karaniwang pattern para sa self-improving agents ay ang pagpapakilala ng isang **"knowledge agent"**. Ang hiwalay na agent na ito ay nagmamasid sa pangunahing pag-uusap sa pagitan ng user at ng pangunahing agent. Ang papel nito ay:

1. **Tukuyin ang mahalagang impormasyon**: Tukuyin kung alinmang bahagi ng pag-uusap ang mahalagang i-save bilang pangkalahatang kaalaman o partikular na kagustuhan ng user.

2. **Kunin at ibuod**: I-distill ang mahahalagang natutunan o kagustuhan mula sa pag-uusap.

3. **I-imbak sa knowledge base**: I-persist ang nakuhang impormasyon, kadalasan sa isang vector database, upang ito ay ma-retrieve sa hinaharap.

4. **Palakasin ang mga susunod na query**: Kapag nagpasimula ang user ng bagong query, kinukuha ng knowledge agent ang kaugnay na nakaimbak na impormasyon at idinadagdag ito sa prompt ng user, na nagbibigay ng mahalagang konteksto sa pangunahing agent (katulad ng RAG).

### Mga Pag-optimize para sa Memorya

• **Pamamahala ng Latency**: Upang maiwasan ang pagbagal ng mga interaksyon ng user, maaaring gumamit ng mas mura at mas mabilis na modelo sa simula upang mabilis na suriin kung mahalagang i-store o i-retrieve ang impormasyon, at gagamitin lamang ang mas kumplikadong proseso ng extraction/retrieval kapag kinakailangan.

• **Pagpapanatili ng Knowledge Base**: Para sa lumalaking knowledge base, ang mas madalang gamitin na impormasyon ay maaaring ilipat sa "cold storage" upang mapamahalaan ang mga gastos.

## May Karagdagang Tanong Tungkol sa Memorya ng Agent?

Sumali sa [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) upang makipag-usap sa iba pang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->