# Paggamit ng Agentic Protocols (MCP, A2A at NLWeb)

[![Agentic Protocols](../../../translated_images/tl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

Habang lumalago ang paggamit ng AI agents, lumalaki rin ang pangangailangan para sa mga protocol na nagsisiguro ng standardisasyon, seguridad, at sumusuporta sa bukas na inobasyon. Sa araling ito, tatalakayin natin ang 3 protocol na layuning matugunan ang pangangailangan na ito - Model Context Protocol (MCP), Agent to Agent (A2A) at Natural Language Web (NLWeb).

## Panimula

Sa araling ito, tatalakayin natin:

• Paano pinapahintulutan ng **MCP** ang AI Agents na ma-access ang mga panlabas na tool at datos upang matapos ang mga gawain ng gumagamit.

• Paano pinapagana ng **A2A** ang komunikasyon at kolaborasyon sa pagitan ng iba't ibang AI agents.

• Paano dinala ng **NLWeb** ang mga natural language interface sa anumang website na nagpapahintulot sa AI Agents na tuklasin at makipag-ugnayan sa nilalaman.

## Mga Layunin sa Pagkatuto

• **Kilalanin** ang pangunahing layunin at benepisyo ng MCP, A2A, at NLWeb sa konteksto ng AI agents.

• **Ipaliwanag** kung paano pinapadali ng bawat protocol ang komunikasyon at interaksyon sa pagitan ng LLMs, mga tool, at ibang agent.

• **Tukuyin** ang natatanging papel ng bawat protocol sa pagbuo ng mga kumplikadong agentic system.

## Model Context Protocol

Ang **Model Context Protocol (MCP)** ay isang open standard na nagbibigay ng standardisadong paraan para sa mga aplikasyon na magbigay ng konteksto at mga tool sa LLMs. Pinapahintulutan nito ang isang "universal adaptor" sa iba't ibang pinagkukunan ng datos at mga tool na maaaring ikonekta ng AI Agents sa isang konsistenteng paraan.

Tingnan natin ang mga bahagi ng MCP, mga benepisyo kumpara sa direktang paggamit ng API, at isang halimbawa kung paano maaaring gamitin ng AI agents ang isang MCP server.

### Pangunahing Bahagi ng MCP

Ang MCP ay gumagana sa **client-server architecture** at ang mga pangunahing bahagi ay:

• **Hosts** ay mga LLM application (halimbawa isang code editor tulad ng VSCode) na nagsisimula ng koneksyon sa isang MCP Server.

• **Clients** ay mga bahagi sa loob ng host application na nagpapanatili ng one-to-one na koneksyon sa mga server.

• **Servers** ay mga magagaan na programa na nagpapakita ng mga tiyak na kakayahan.

Kasama sa protocol ang tatlong pangunahing primitive na kakayahan ng isang MCP Server:

• **Mga Tool**: Ito ay mga hiwalay na aksyon o function na maaaring tawagan ng isang AI agent para magsagawa ng aksyon. Halimbawa, maaaring magpakita ang isang weather service ng tool na "kunin ang panahon", o ang isang e-commerce server ay maaaring magpakita ng tool na "bumili ng produkto". Ipinapakita ng mga MCP server ang pangalan, paglalarawan, at input/output schema ng bawat tool sa kanilang listahan ng mga kakayahan.

• **Mga Resources**: Ito ay mga read-only na item ng datos o dokumento na maaaring ibigay ng MCP server, at maaaring kunin ng mga client ayon sa pangangailangan. Mga halimbawa nito ay mga nilalaman ng file, talaan sa database, o log files. Ang mga Resources ay maaaring teksto (tulad ng code o JSON) o binary (tulad ng mga larawan o PDF).

• **Mga Prompt**: Ito ay mga nakahandang templates na nagbibigay ng mga mungkahing prompt, na nagpapahintulot ng mas kumplikadong mga workflow.

### Mga Benepisyo ng MCP

Nagbibigay ang MCP ng makabuluhang mga kalamangan para sa AI Agents:

• **Dynamic Tool Discovery**: Maaaring makatanggap ang mga agents ng dynamic na listahan ng mga tool na available mula sa isang server kasama ang mga paglalarawan ng mga ginagawa nito. Ito ay kabaligtaran ng tradisyonal na API, na madalas nangangailangan ng static na coding para sa integrasyon, na nangangahulugang ang anumang pagbabago sa API ay nangangailangan ng pag-update ng code. Nag-aalok ang MCP ng "integrate once" na pamamaraan, na nagdudulot ng mas mataas na kakayahang mag-adapt.

• **Interoperability sa Iba't Ibang LLMs**: Gumagana ang MCP sa iba't ibang LLMs, nagbibigay ng kakayahang magpalit ng mga pangunahing modelo para sa pagsubok ng mas mahusay na performance.

• **Standardized Security**: Kasama sa MCP ang isang standard na paraan ng authentication, na nagpapabuti ng scalability kapag nagdadagdag ng access sa karagdagang MCP servers. Ito ay mas simple kaysa sa pamamahala ng iba't ibang mga key at authentication types para sa iba’t ibang tradisyonal na API.

### Halimbawa ng MCP

![MCP Diagram](../../../translated_images/tl/mcp-diagram.e4ca1cbd551444a1.webp)

Isipin na nais ng isang gumagamit na magpareserba ng flight gamit ang AI assistant na pinapagana ng MCP.

1. **Koneksyon**: Nagkokonekta ang AI assistant (ang MCP client) sa isang MCP server na ibinigay ng airline.

2. **Pagtuklas ng Tool**: Tinanong ng client ang MCP server ng airline, "Anong mga tool ang mayroon kayo?" Sumagot ang server ng mga tool tulad ng "search flights" at "book flights".

3. **Pagtawag sa Tool**: Hiningi mo sa AI assistant, "Pakisiyasat ang flight mula Portland papuntang Honolulu." Gamit ang LLM nito, natukoy ng AI assistant na kailangang tawagin ang tool na "search flights" at ipinasa ang mga kaugnay na parameter (pinagmulan, destinasyon) sa MCP server.

4. **Pagsasagawa at Tugon**: Ang MCP server, bilang wrapper, ang direktang tumawag sa internal booking API ng airline. Natanggap nito ang impormasyon ng flight (halimbawa ay JSON data) at ipinasa ito pabalik sa AI assistant.

5. **Karagdagang Pakikipag-ugnayan**: Ipinakita ng AI assistant ang mga flight options. Kapag pumili ka ng flight, maaaring tawagin ng assistant ang tool na "book flight" sa parehong MCP server upang kumpletuhin ang booking.

## Agent-to-Agent Protocol (A2A)

Habang nakatuon ang MCP sa pagkonekta ng LLMs sa mga tool, ang **Agent-to-Agent (A2A) protocol** ay isang hakbang pa sa pamamagitan ng pagpapahintulot ng komunikasyon at kolaborasyon sa pagitan ng iba't ibang AI agents. Kinokonekta ng A2A ang mga AI agents mula sa iba't ibang mga organisasyon, environment, at tech stack upang matapos ang isang pinagsamang gawain.

Titingnan natin ang mga bahagi at benepisyo ng A2A, pati na rin ang isang halimbawa kung paano ito maaaring gamitin sa ating travel application.

### Pangunahing Bahagi ng A2A

Nakatuon ang A2A sa pagpapahintulot ng komunikasyon sa pagitan ng mga agent at paggawa nila ng sama-samang trabaho upang matapos ang isang subtask para sa gumagamit. Bawat bahagi ng protocol ay nakakatulong dito:

#### Agent Card

Kagaya ng pagbabahagi ng listahan ng mga tool ng MCP server, ang Agent Card ay may:
- Pangalan ng Agent.
- Isang **paglalarawan ng mga pangkalahatang gawain** na natatapos nito.
- Isang **listahan ng mga partikular na kakayahan** kasama ang mga paglalarawan para matulungan ang ibang mga agent (o pati na mga tao) na maunawaan kung kailan at bakit gusto nilang tawagan ang isang agent.
- Ang **kasalukuyang Endpoint URL** ng agent.
- Ang **bersyon** at **kakayahan** ng agent tulad ng streaming responses at push notifications.

#### Agent Executor

Ang Agent Executor ang may pananagutan sa **pagpapasa ng konteksto ng user chat sa remote agent**, kailangan ito ng remote agent upang maunawaan ang gawain na kailangang tapusin. Sa isang A2A server, ginagamit ng isang agent ang sariling Large Language Model (LLM) upang suriin ang mga papasok na kahilingan at isagawa ang mga gawain gamit ang sariling mga internal na tool.

#### Artifact

Kapag natapos na ng remote agent ang hinihinging gawain, ang resulta nito ay nililikha bilang isang artifact. Ang artifact ay **naglalaman ng resulta ng gawa ng agent**, isang **paglalarawan ng natapos**, at ang **text context** na ipinapadala sa protocol. Matapos maipadala ang artifact, ang koneksyon sa remote agent ay isinara hanggang kailanganin muli.

#### Event Queue

Ang bahagi na ito ay ginagamit para sa **pangangasiwa ng mga update at pagpapasa ng mga mensahe**. Importante ito lalo na sa production para sa mga agentic systems upang maiwasan ang pagsasara ng koneksyon sa pagitan ng mga agent bago matapos ang gawain, lalo na kapag mahabang oras ang kinakailangan upang matapos ang gawain.

### Mga Benepisyo ng A2A

• **Pinahusay na Kolaborasyon**: Pinapagana nito ang mga agent mula sa iba't ibang vendor at platform upang makipag-ugnayan, magbahagi ng konteksto, at magtrabaho nang sama-sama, na nagpapadali ng seamless automation sa mga tradisyonal na hindi magkakaugnay na sistema.

• **Kakayahang Piliin ang Modelo**: Maaaring piliin ng bawat A2A agent kung aling LLM ang gagamitin nito sa pagtugon sa mga kahilingan, na nagpapahintulot ng optimized o fine-tuned na mga modelo para sa bawat agent, hindi tulad ng iisang LLM connection sa ilang mga senaryo ng MCP.

• **Built-in Authentication**: Direktang isinama ang authentication sa A2A protocol, na nagbibigay ng matibay na framework sa seguridad para sa interaksyon ng mga agent.

### Halimbawa ng A2A

![A2A Diagram](../../../translated_images/tl/A2A-Diagram.8666928d648acc26.webp)

Palalawakin natin ang senaryo ng booking ng travel, ngunit sa pagkakataong ito gamit ang A2A.

1. **Kahilingan ng User sa Multi-Agent**: Nakikipag-ugnayan ang user sa isang "Travel Agent" A2A client/agent, maaaring sa pagsasabi ng, "Pakireserba ang buong biyahe papuntang Honolulu para sa susunod na linggo, kasama ang mga flight, hotel, at renta ng sasakyan."

2. **Orchestration ng Travel Agent**: Natanggap ng Travel Agent ang kumplikadong kahilingang ito. Ginagamit nito ang LLM nito upang pag-isipan ang gawain at tukuyin na kailangan nitong makipag-ugnayan sa iba pang mga espesyalisadong agent.

3. **Komunikasyon sa Pagitan ng Mga Agent**: Ginagamit ng Travel Agent ang A2A protocol upang kumonekta sa mga downstream agent, tulad ng "Airline Agent," "Hotel Agent," at "Car Rental Agent" na ginawa ng iba't ibang kumpanya.

4. **Pag-delegate ng Pagsasagawa ng Gawain**: Pinapadala ng Travel Agent ang mga partikular na gawain sa mga espesyal na agent na ito (halimbawa, "Humanap ng mga flight papuntang Honolulu," "Magpareserba ng hotel," "Magrenta ng sasakyan"). Ang bawat isa sa mga spezial na agent na ito na nagpapatakbo ng sariling LLM at gumagamit ng sariling mga tool (na pwedeng mga MCP server din) ay nagsasagawa ng kanilang bahagi ng booking.

5. **Pinagsama-samang Tugon**: Kapag natapos na ang lahat ng downstream na mga agent sa kanilang mga gawain, ipinagsasama-sama ng Travel Agent ang mga resulta (mga detalye ng flight, kumpirmasyon ng hotel, booking ng sasakyan) at ipinapadala ang isang komprehensibo, chat-style na tugon pabalik sa user.

## Natural Language Web (NLWeb)

Matagal nang ang mga website ang pangunahing paraan para ma-access ng mga user ang impormasyon at datos sa buong internet.

Tingnan natin ang iba't ibang bahagi ng NLWeb, mga benepisyo nito, at isang halimbawa kung paano gumagana ang NLWeb sa ating travel application.

### Mga Bahagi ng NLWeb

- **NLWeb Application (Core Service Code)**: Ang sistema na nagpoproseso ng mga tanong gamit ang natural language. Kinokonekta nito ang iba't ibang bahagi ng platform upang makalikha ng mga tugon. Maaari mo itong isipin bilang **makina na nagpapatakbo sa natural language na mga katangian** ng isang website.

- **NLWeb Protocol**: Ito ay isang **batayang hanay ng mga patakaran para sa natural language interaction** sa isang website. Nagbabalik ito ng mga tugon sa format na JSON (madalas gumagamit ng Schema.org). Layunin nito ang lumikha ng simpleng pundasyon para sa "AI Web," katulad ng kung paano pinadali ng HTML ang pagbabahagi ng mga dokumento online.

- **MCP Server (Model Context Protocol Endpoint)**: Bawat NLWeb setup ay gumagana rin bilang isang **MCP server**. Nangangahulugan ito na maaari itong **magbahagi ng mga tool (tulad ng isang “ask” method) at datos** sa ibang AI systems. Sa praktis, ginagawa nitong magagamit ng AI agents ang nilalaman at kakayahan ng website, na nagpapahintulot sa site na maging bahagi ng mas malawak na “agent ecosystem.”

- **Embedding Models**: Ginagamit ang mga modelong ito upang **i-convert ang website content sa mga numerical representation na tinatawag na vectors** (embeddings). Kinakatawan ng mga vector na ito ang kahulugan sa paraang maihahambing at mare-retrieve ng mga computer. Iniimbak ang mga ito sa espesyal na database, at maaaring pumili ang mga gumagamit kung aling embedding model ang nais nilang gamitin.

- **Vector Database (Retrieval Mechanism)**: Ang database na ito ay **nagse-store ng mga embedding ng website content**. Kapag may nagtanong, tinitingnan ng NLWeb ang vector database upang mabilis hanapin ang pinaka-nauugnay na impormasyon. Nagbibigay ito ng mabilis na listahan ng mga posibleng sagot, niraranggo batay sa pagkakahawig. Gumagana ang NLWeb sa iba't ibang vector storage system tulad ng Qdrant, Snowflake, Milvus, Azure AI Search, at Elasticsearch.

### NLWeb sa Halimbawa

![NLWeb](../../../translated_images/tl/nlweb-diagram.c1e2390b310e5fe4.webp)

Isipin muli ang ating travel booking website, ngunit ngayong pinapagana ng NLWeb.

1. **Pagpasok ng Datos**: Ang umiiral na mga katalogo ng produkto ng travel website (halimbawa, listahan ng flight, paglalarawan ng hotel, tour packages) ay inaayos gamit ang Schema.org o niloload sa pamamagitan ng RSS feeds. Kinukuha ng mga tool ng NLWeb ang istrukturadong datos na ito, nililikha ang mga embedding, at iniimbak ito sa local o remote na vector database.

2. **Tanong gamit ang Natural Language (Taong Gumagamit)**: Dumadalaw ang isang gumagamit sa website at imbes na mag-navigate sa mga menu, nagtatype sa isang chat interface: "Maghanap ng family-friendly na hotel sa Honolulu na may pool para sa susunod na linggo."

3. **Pagpoproseso ng NLWeb**: Natatanggap ng NLWeb application ang tanong na ito. Ipinapadala nito ang tanong sa isang LLM para interpretasyon at kasabay nito naghahanap sa vector database ng mga kaugnay na listahan ng hotel.

4. **Tumpak na Resulta**: Tinutulungan ng LLM na bigyang-kahulugan ang mga resulta ng paghahanap mula sa database, tukuyin ang pinakamahusay na tugma base sa mga criterion na "family-friendly," "pool," at "Honolulu," at saka ay inaayos ang tugon sa natural language. Mahalaga, tumutukoy ang tugon sa totoong mga hotel mula sa katalogo ng website, iniiwasan ang gawang impormasyon.

5. **Pakikipag-ugnayan sa AI Agent**: Dahil gumagana ang NLWeb bilang isang MCP server, maaaring kumonekta ang isang external AI travel agent sa NLWeb instance ng website. Maaari ng AI agent na gamitin ang `ask` MCP method para direktang magtanong sa website: `ask("Mayroon bang vegan-friendly na mga restawran sa lugar ng Honolulu na inirerekomenda ng hotel?")`. Ipoproseso ito ng NLWeb instance gamit ang database nito ng impormasyon sa mga restawran (kung na-load), at magbabalik ng istrukturadong tugon sa JSON.

### May Iba Pang Katanungan tungkol sa MCP/A2A/NLWeb?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipagtagpo sa iba pang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

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