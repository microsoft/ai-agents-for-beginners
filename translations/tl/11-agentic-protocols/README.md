# Paggamit ng Agentic Protocols (MCP, A2A at NLWeb)

[![Agentic Protocols](../../../translated_images/tl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(I-click ang larawan sa itaas upang mapanood ang video ng araling ito)_

Habang lumalago ang paggamit ng AI agents, gayundin ang pangangailangan para sa mga protocol na nagsisiguro ng standardisasyon, seguridad, at sumusuporta sa bukas na inobasyon. Sa araling ito, tatalakayin natin ang 3 protocol na naglalayong tugunan ang pangangailangang ito - Model Context Protocol (MCP), Agent to Agent (A2A) at Natural Language Web (NLWeb).

## Panimula

Sa araling ito, tatalakayin natin:

• Paano pinapayagan ng **MCP** ang AI Agents na ma-access ang mga panlabas na kasangkapan at datos upang makumpleto ang mga gawain ng gumagamit.

• Paano pinahihintulutan ng **A2A** ang komunikasyon at kolaborasyon sa pagitan ng iba't ibang AI agents.

• Paano nagdadala ang **NLWeb** ng mga natural na interface ng wika sa anumang website na nagpapahintulot sa AI Agents na matuklasan at makipag-ugnayan sa nilalaman.

## Mga Layunin sa Pag-aaral

• **Matukoy** ang pangunahing layunin at mga benepisyo ng MCP, A2A, at NLWeb sa konteksto ng AI agents.

• **Ipaliwanag** kung paano pinapadali ng bawat protocol ang komunikasyon at interaksyon sa pagitan ng LLMs, mga kasangkapan, at iba pang mga agent.

• **Kilalanin** ang kakaibang papel na ginagampanan ng bawat protocol sa pagbuo ng mga komplikadong agentic system.

## Model Context Protocol

Ang **Model Context Protocol (MCP)** ay isang bukas na pamantayan na nagbibigay ng istandardisadong paraan para sa mga aplikasyon na magbigay ng konteksto at mga kasangkapan sa LLMs. Pinapayagan nito ang isang "unibersal na adaptor" sa iba't ibang pinagkukunan ng datos at mga kasangkapan na maaaring ikonekta ng AI Agents sa isang pare-parehong paraan.

Tingnan natin ang mga bahagi ng MCP, ang mga benepisyo nito kumpara sa direktang paggamit ng API, at isang halimbawa kung paano maaaring gamitin ng mga AI agents ang isang MCP server.

### Pangunahing Bahagi ng MCP

Gumagana ang MCP sa **client-server architecture** at ang mga pangunahing bahagi ay:

• **Hosts** ay mga aplikasyon ng LLM (halimbawa isang code editor tulad ng VSCode) na nagsisimula ng mga koneksyon sa isang MCP Server.

• **Clients** ay mga bahagi sa loob ng host application na nagpapanatili ng one-to-one na koneksyon sa mga server.

• **Servers** ay mga magagaan na programa na naglalantad ng mga partikular na kakayahan.

Kasama sa protocol ang tatlong pangunahing primitives na mga kakayahan ng isang MCP Server:

• **Tools**: Ito ay mga hiwalay na aksyon o function na maaaring tawagin ng AI agent para magsagawa ng isang gawain. Halimbawa, maaaring maglantad ng isang weather service ng tool na "get weather", o isang e-commerce server ng tool na "purchase product". Ipinapahayag ng mga MCP server ang pangalan ng bawat tool, paglalarawan, at input/output schema sa kanilang listahan ng mga kakayahan.

• **Resources**: Ito ay mga data item o dokumentong read-only na maibibigay ng MCP server at maaaring kunin ng mga client kapag kailangan. Halimbawa ay mga nilalaman ng file, rekord sa database, o mga log file. Ang mga resources ay maaaring teksto (tulad ng code o JSON) o binary (tulad ng mga larawan o PDF).

• **Prompts**: Ito ay mga naunang template na nagbibigay ng mga mungkahing prompt, na nagpapahintulot ng mas kumplikadong workflow.

### Mga Benepisyo ng MCP

Nagbibigay ang MCP ng mga makabuluhang kalamangan para sa AI Agents:

• **Dynamic Tool Discovery**: Maaaring awtomatikong makatanggap ang mga agents ng listahan ng mga available na tool mula sa isang server kasama ang mga paglalarawan kung ano ang ginagawa ng mga ito. Kabaligtaran ito ng tradisyunal na mga API na madalas nangangailangan ng static coding para sa mga integrasyon, ibig sabihin ang anumang pagbabago sa API ay nangangailangan ng pag-update ng code. Nag-aalok ang MCP ng "integrate once" na pamamaraan, na humahantong sa mas mataas na kakayahan sa pag-adapt.

• **Interoperability Across LLMs**: Gumagana ang MCP sa iba't ibang LLM, nagbibigay ito ng kakayahang magpalit ng pangunahing mga modelo para sa mas mahusay na pagganap.

• **Standardized Security**: Kasama sa MCP ang pamantayang paraan ng authentication, nagpapabuti ito ng scalability kapag nagdadagdag ng access sa mga dagdag na MCP server. Mas simple ito kumpara sa pamamahala ng iba't ibang susi at uri ng authentication para sa iba't ibang tradisyunal na API.

### Halimbawa ng MCP

![MCP Diagram](../../../translated_images/tl/mcp-diagram.e4ca1cbd551444a1.webp)

Isipin na nais ng isang gumagamit mag-book ng flight gamit ang AI assistant na pinapagana ng MCP.

1. **Koneksyon**: Nakakonekta ang AI assistant (ang MCP client) sa isang MCP server na ibinigay ng airline.

2. **Tool Discovery**: Tinanong ng client ang MCP server ng airline, "Anong mga tool ang mayroon kayo?" Sumasagot ang server ng mga tool tulad ng "search flights" at "book flights".

3. **Pagtawag ng Tool**: Sunod mong sasabihin sa AI assistant, "Paki-search ng flight mula Portland patungong Honolulu." Ginagamit ng AI assistant ang LLM nito, natutukoy nito na kailangang tawagin ang tool na "search flights" at ipinapasa ang mga kinakailangang parameter (pinanggalingan, patutunguhan) sa MCP server.

4. **Pagsasagawa at Tugon**: Gumagana ang MCP server bilang isang wrapper at ginagawa ang aktwal na tawag sa internal booking API ng airline. Tinatanggap nito ang impormasyon ng flight (hal. JSON data) at ibinabalik sa AI assistant.

5. **Karagdagang Interaksyon**: Ipinapakita ng AI assistant ang mga opsyon sa flights. Kapag pumili ka ng flight, maaaring tawagin ng assistant ang tool na "book flight" sa parehong MCP server upang kumpletuhin ang booking.

## Agent-to-Agent Protocol (A2A)

Habang nakatuon ang MCP sa pagkonekta ng LLMs sa mga kasangkapan, ang **Agent-to-Agent (A2A) protocol** ay lumalawak pa sa pamamagitan ng pagpapahintulot ng komunikasyon at kolaborasyon sa pagitan ng iba't ibang AI agent. Kinokonekta ng A2A ang AI agents mula sa iba't ibang organisasyon, kapaligiran, at mga tech stack upang makumpleto ang isang shared na gawain.

Titingnan natin ang mga bahagi at benepisyo ng A2A, pati na ang isang halimbawa kung paano ito maaaring gamitin sa ating travel application.

### Pangunahing Bahagi ng A2A

Nakatuon ang A2A sa pagpapahintulot ng komunikasyon sa pagitan ng mga agent at pagpapagana sa kanila na magtulungan upang makumpleto ang isang subtasks ng gumagamit. Nakakatulong ang bawat bahagi ng protocol dito:

#### Agent Card

Katulad ng pagbahagi ng isang MCP server ng listahan ng mga tool, ang Agent Card ay naglalaman ng:
- Pangalan ng Agent.
- Isang **paglalarawan ng mga pangkalahatang gawain** na naisakatuparan nito.
- Isang **listahan ng mga partikular na kasanayan** na may mga paglalarawan upang matulungan ang ibang mga agent (o pati na mga taong gumagamit) na maunawaan kung kailan at bakit nila nais tawagin ang agent na iyon.
- Ang **kasalukuyang Endpoint URL** ng agent
- Ang **berisyon** at **mga kakayahan** ng agent tulad ng streaming responses at push notifications.

#### Agent Executor

Ang Agent Executor ang responsable sa **pagpapasa ng konteksto ng usapan ng gumagamit sa remote agent**, kailangan ito ng remote agent upang maunawaan ang gawain na kailangang gawin. Sa isang A2A server, gumagamit ang isang agent ng sarili nitong Large Language Model (LLM) upang unawain ang mga papasok na kahilingan at magsagawa ng mga gawain gamit ang sarili nitong mga internal na kasangkapan.

#### Artifact

Kapag nakumpleto na ng remote agent ang hinihiling na gawain, ang produktong gawa nito ay nililikha bilang artifact. Ang artifact ay **naglalaman ng resulta ng gawain ng agent**, isang **paglalarawan kung ano ang natapos**, at ang **tekstuwal na konteksto** na ipinapasa sa protocol. Pagkatapos maipadala ang artifact, ang koneksyon sa remote agent ay isinara hanggang sa kailanganin muli.

#### Event Queue

Ginagamit ang bahaging ito para sa **paghawak ng mga update at pagpapasa ng mga mensahe**. Mahalaga ito lalo na sa produksyon para sa mga agentic system upang maiwasan ang pagsasara ng koneksyon sa pagitan ng mga agent bago matapos ang isang gawain, lalo na kapag ang tagal ng pagkumpleto ng gawain ay maaaring tumagal ng mas matagal.

### Mga Benepisyo ng A2A

• **Pinalawak na Kolaborasyon**: Pinapahintulutan nito ang mga agent mula sa iba't ibang vendor at platform na makipag-ugnayan, magbahagi ng konteksto, at magtulungan, na nagpapadali ng banayad na automasyon sa mga tradisyunal na hiwalay na sistema.

• **Kakayahang Pumili ng Modelo**: Maaaring piliin ng bawat A2A agent kung anong LLM ang gagamitin nila upang tugunan ang kanilang mga kahilingan, nagpapahintulot ng optimisasyon o finely tuned na mga modelo bawat agent, hindi tulad ng isang LLM connection sa ilang MCP na mga senaryo.

• **Built-in na Authentication**: Ang authentication ay direktang kasama sa A2A protocol, nagbibigay ito ng matibay na framework ng seguridad para sa interaksyon ng mga agent.

### Halimbawa ng A2A

![A2A Diagram](../../../translated_images/tl/A2A-Diagram.8666928d648acc26.webp)

Palalawakin natin ang ating senaryo sa pag-book ng paglalakbay, ngunit sa pagkakataong ito gamit ang A2A.

1. **Hiling ng Gumagamit sa Multi-Agent**: Nakikipag-ugnayan ang isang gumagamit sa isang "Travel Agent" na A2A client/agent, marahil ay nagsabi, "Pakibook ang buong lakbay papuntang Honolulu para sa susunod na linggo, kasama na ang flights, hotel, at rental na sasakyan".

2. **Orkestrasyon ng Travel Agent**: Tinatanggap ng Travel Agent ang kumplikadong hiling na ito. Ginagamit nito ang LLM nito upang pag-isipan ang gawain at tukuyin na kailangan nitong makipag-ugnayan sa iba pang espesyal na mga agent.

3. **Inter-Agent Communication**: Ginagamit ng Travel Agent ang A2A protocol upang kumonekta sa downstream agents, tulad ng "Airline Agent," "Hotel Agent," at "Car Rental Agent" na nilikha ng iba't ibang kumpanya.

4. **Delegated Task Execution**: Ipinapadala ng Travel Agent ang mga partikular na gawain sa mga espesyal na agent na ito (halimbawa, "Maghanap ng mga flight papuntang Honolulu," "Mag-book ng hotel," "Magrenta ng sasakyan"). Bawat isa sa mga espesyal na agent na ito, na nagpapatakbo ng sarili nilang LLMs at gumagamit ng kanilang sariling mga kasangkapan (na maaaring mga MCP server mismo), ay isinasagawa ang partikular nitong bahagi ng booking.

5. **Pinagsama-samang Tugon**: Kapag natapos na ng lahat ng downstream agents ang kanilang mga gawain, pinagsasama ng Travel Agent ang mga resulta (mga detalye ng flight, kumpirmasyon ng hotel, booking ng car rental) at nagpapadala ng komprehensibong, chat-style na tugon pabalik sa gumagamit.

## Natural Language Web (NLWeb)

Matagal nang pangunahing paraan ang mga website para ma-access ng mga gumagamit ang impormasyon at datos sa buong internet.

Tingnan natin ang iba't ibang bahagi ng NLWeb, ang mga benepisyo ng NLWeb at isang halimbawa kung paano gumagana ang NLWeb sa ating travel application.

### Mga Bahagi ng NLWeb

- **NLWeb Application (Core Service Code)**: Ang sistemang nagpoproseso ng mga tanong gamit ang natural na wika. Kinokonekta nito ang iba't ibang bahagi ng platform upang makalikha ng mga tugon. Maaari mo itong isipin bilang **makina na nagpapatakbo ng mga tampok ng natural na wika** ng isang website.

- **NLWeb Protocol**: Ito ay isang **pangunahing hanay ng mga patakaran para sa natural na pakikipag-ugnayan gamit ang wika** sa isang website. Nagpapadala ito pabalik ng mga tugon sa format na JSON (madalas gumagamit ng Schema.org). Layunin nito na lumikha ng simpleng pundasyon para sa "AI Web," katulad ng paraan ng HTML para sa pagbabahagi ng mga dokumento online.

- **MCP Server (Model Context Protocol Endpoint)**: Ang bawat setup ng NLWeb ay gumagana rin bilang isang **MCP server**. Ibig sabihin, maaari itong **magbahagi ng mga tools (tulad ng “ask” method) at datos** sa ibang AI system. Sa praktis, ginagawa nitong magagamit ng AI agents ang nilalaman at kakayahan ng website, pinapayagan ang site na maging bahagi ng mas malawak na "agent ecosystem."

- **Embedding Models**: Ginagamit ang mga modelong ito upang **i-convert ang nilalaman ng website sa mga numerikal na representasyon na tinatawag na vectors** (embeddings). Kinukuha ng mga vector na ito ang kahulugan sa paraang magagamit ng mga kompyuter sa paghahambing at paghahanap. Itinatago sila sa isang espesyal na database, at maaaring pumili ang mga gumagamit kung aling embedding model ang nais nilang gamitin.

- **Vector Database (Retrieval Mechanism)**: Ang database na ito ay **nagtatago ng mga embeddings ng nilalaman ng website**. Kapag may nagtatanong, sinusuri ng NLWeb ang vector database upang mabilis na mahanap ang pinakanaaangkop na impormasyon. Nagbibigay ito ng mabilis na listahan ng mga posibleng sagot, niraranggo ayon sa pagkakatulad. Gumagana ang NLWeb sa iba't ibang vector storage systems tulad ng Qdrant, Snowflake, Milvus, Azure AI Search, at Elasticsearch.

### NLWeb sa Halimbawa

![NLWeb](../../../translated_images/tl/nlweb-diagram.c1e2390b310e5fe4.webp)

Isipin muli ang ating travel booking website, ngunit sa pagkakataong ito, pinapagana ito ng NLWeb.

1. **Pagpasok ng Datos**: Ang mga umiiral na katalogo ng produkto ng travel site (halimbawa, mga flight listing, paglalarawan ng hotel, tour packages) ay nakaayos gamit ang Schema.org o iniloload gamit ang RSS feeds. Kinokonsumo ng mga tools ng NLWeb ang istrukturadong datos na ito, lumilikha ng embeddings, at itinatago ang mga ito sa lokal o remote vector database.

2. **Pagtanong gamit ang Natural na Wika (Tao)**: Bumibisita ang isang gumagamit sa website at imbes na mag-navigate sa mga menu, nagta-type sa chat interface, "Maghanap ng hotel na pamilyang-friendly sa Honolulu na may pool para sa susunod na linggo".

3. **Pagproseso ng NLWeb**: Tinatanggap ng NLWeb application ang tanong na ito. Ipinapasa nito ang tanong sa isang LLM para sa pag-unawa at sabay nitong hinahanap sa vector database ang mga kaugnay na listing ng hotel.

4. **Tama at Akmang Resulta**: Tinutulungan ng LLM na bigyang-kahulugan ang mga resulta ng paghahanap mula sa database, tukuyin ang pinakamahusay na tugma base sa mga pamantayan na "family-friendly," "pool," at "Honolulu," at pagkatapos ay inaayos ang tugon sa natural na wika. Mahalagang ang tugon ay tumutukoy sa aktwal na mga hotel mula sa katalogo ng website, iniiwasan ang gawa-gawa na impormasyon.

5. **Pakikipag-ugnayan ng AI Agent**: Dahil nagsisilbi ang NLWeb bilang MCP server, maaaring kumonekta ang panlabas na AI travel agent sa instance ng NLWeb ng website na ito. Maaari gamitin ng AI agent ang `ask` MCP method upang direktang magtanong sa website: `ask("May mga vegan-friendly ba na restawran sa lugar ng Honolulu na inirerekomenda ng hotel?")`. Ipoproseso ng NLWeb instance ito gamit ang database ng impormasyon ng mga restoran (kung na-load), at magbabalik ng istrakturadong JSON na tugon.

### May Mga Karagdagang Tanong tungkol sa MCP/A2A/NLWeb?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para makipagkilala sa ibang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

## Mga Mapagkukunan

- [MCP para sa mga Baguhan](https://aka.ms/mcp-for-beginners)  
- [Dokumentasyon ng MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Nakaraang Aralin

[AI Agents sa Produksyon](../10-ai-agents-production/README.md)

## Susunod na Aralin

[Context Engineering para sa AI Agents](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->