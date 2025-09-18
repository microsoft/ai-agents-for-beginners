<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T15:21:51+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "tl"
}
-->
# Paggamit ng Agentic Protocols (MCP, A2A at NLWeb)

[![Agentic Protocols](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.tl.png)](https://youtu.be/X-Dh9R3Opn8)

> _(I-click ang imahe sa itaas para mapanood ang video ng araling ito)_

Habang lumalawak ang paggamit ng AI agents, tumataas din ang pangangailangan para sa mga protocol na nagtitiyak ng standardisasyon, seguridad, at suporta para sa bukas na inobasyon. Sa araling ito, tatalakayin natin ang 3 protocol na naglalayong tugunan ang pangangailangang ito - Model Context Protocol (MCP), Agent to Agent (A2A), at Natural Language Web (NLWeb).

## Panimula

Sa araling ito, tatalakayin natin:

• Paano pinapayagan ng **MCP** ang AI Agents na ma-access ang mga panlabas na tools at data upang maisakatuparan ang mga gawain ng user.

• Paano pinapadali ng **A2A** ang komunikasyon at kolaborasyon sa pagitan ng iba't ibang AI agents.

• Paano dinadala ng **NLWeb** ang mga natural language interface sa anumang website, na nagbibigay-daan sa AI Agents na matuklasan at makipag-ugnayan sa nilalaman.

## Mga Layunin sa Pag-aaral

• **Kilalanin** ang pangunahing layunin at benepisyo ng MCP, A2A, at NLWeb sa konteksto ng AI agents.

• **Ipaliwanag** kung paano pinapadali ng bawat protocol ang komunikasyon at interaksyon sa pagitan ng LLMs, tools, at iba pang agents.

• **Kilalanin** ang natatanging papel ng bawat protocol sa pagbuo ng mas kumplikadong agentic systems.

## Model Context Protocol

Ang **Model Context Protocol (MCP)** ay isang open standard na nagbibigay ng standardized na paraan para sa mga aplikasyon na magbigay ng context at tools sa LLMs. Pinapagana nito ang isang "universal adaptor" para sa iba't ibang data sources at tools na maaaring ikonekta ng AI Agents sa isang pare-parehong paraan.

Tingnan natin ang mga bahagi ng MCP, ang mga benepisyo nito kumpara sa direktang paggamit ng API, at isang halimbawa kung paano maaaring gamitin ng AI agents ang isang MCP server.

### Mga Pangunahing Bahagi ng MCP

Ang MCP ay gumagana sa isang **client-server architecture** at ang mga pangunahing bahagi nito ay:

• **Hosts** ay mga LLM application (halimbawa, isang code editor tulad ng VSCode) na nagsisimula ng koneksyon sa isang MCP Server.

• **Clients** ay mga bahagi sa loob ng host application na nagpapanatili ng one-to-one na koneksyon sa mga server.

• **Servers** ay mga magagaan na programa na naglalantad ng partikular na kakayahan.

Kasama sa protocol ang tatlong pangunahing primitives na siyang mga kakayahan ng isang MCP Server:

• **Tools**: Ito ay mga discrete na aksyon o function na maaaring tawagin ng AI agent upang maisagawa ang isang aksyon. Halimbawa, ang isang weather service ay maaaring magbigay ng "get weather" tool, o ang isang e-commerce server ay maaaring magbigay ng "purchase product" tool. Ang MCP servers ay nag-a-advertise ng pangalan, deskripsyon, at input/output schema ng bawat tool sa kanilang capabilities listing.

• **Resources**: Ito ay mga read-only na data items o dokumento na maaaring ibigay ng isang MCP server, at maaaring kunin ng mga clients kapag kinakailangan. Halimbawa nito ay ang mga file contents, database records, o log files. Ang resources ay maaaring text (tulad ng code o JSON) o binary (tulad ng images o PDFs).

• **Prompts**: Ito ay mga predefined na template na nagbibigay ng mga suggested prompts, na nagpapahintulot sa mas kumplikadong workflows.

### Mga Benepisyo ng MCP

Ang MCP ay nag-aalok ng mga makabuluhang benepisyo para sa AI Agents:

• **Dynamic Tool Discovery**: Ang mga agents ay maaaring tumanggap ng listahan ng mga available na tools mula sa isang server kasama ang mga deskripsyon ng kanilang ginagawa. Ito ay naiiba sa tradisyunal na APIs, na kadalasang nangangailangan ng static coding para sa mga integrasyon, na nangangahulugan na ang anumang pagbabago sa API ay nangangailangan ng pag-update ng code. Ang MCP ay nag-aalok ng "integrate once" na approach, na nagdudulot ng mas malaking adaptability.

• **Interoperability Across LLMs**: Ang MCP ay gumagana sa iba't ibang LLMs, na nagbibigay ng flexibility upang magpalit ng core models para sa mas mahusay na performance.

• **Standardized Security**: Ang MCP ay may kasamang standard na authentication method, na nagpapabuti sa scalability kapag nagdadagdag ng access sa karagdagang MCP servers. Ito ay mas simple kaysa sa pamamahala ng iba't ibang keys at authentication types para sa iba't ibang tradisyunal na APIs.

### Halimbawa ng MCP

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.tl.png)

Isipin na ang isang user ay nais mag-book ng flight gamit ang isang AI assistant na pinapagana ng MCP.

1. **Koneksyon**: Ang AI assistant (ang MCP client) ay kumokonekta sa isang MCP server na ibinibigay ng isang airline.

2. **Tool Discovery**: Ang client ay nagtatanong sa MCP server ng airline, "Anong tools ang available sa inyo?" Ang server ay sumasagot ng mga tools tulad ng "search flights" at "book flights".

3. **Tool Invocation**: Pagkatapos ay sasabihin mo sa AI assistant, "Paki-search ng flight mula Portland papuntang Honolulu." Ang AI assistant, gamit ang LLM nito, ay kinikilala na kailangan nitong tawagin ang "search flights" tool at ipasa ang mga kaukulang parameter (origin, destination) sa MCP server.

4. **Execution at Response**: Ang MCP server, na kumikilos bilang wrapper, ay gumagawa ng aktwal na tawag sa internal booking API ng airline. Pagkatapos ay natatanggap nito ang impormasyon ng flight (hal., JSON data) at ibinabalik ito sa AI assistant.

5. **Karagdagang Interaksyon**: Ang AI assistant ay nagpapakita ng mga opsyon sa flight. Kapag pumili ka ng flight, maaaring tawagin ng assistant ang "book flight" tool sa parehong MCP server, na kumukumpleto sa booking.

## Agent-to-Agent Protocol (A2A)

Habang ang MCP ay nakatuon sa pagkonekta ng LLMs sa tools, ang **Agent-to-Agent (A2A) protocol** ay nagdadala nito sa mas mataas na antas sa pamamagitan ng pagpapagana ng komunikasyon at kolaborasyon sa pagitan ng iba't ibang AI agents. Ang A2A ay kumokonekta sa AI agents sa iba't ibang organisasyon, kapaligiran, at teknolohiyang stack upang maisakatuparan ang isang shared na gawain.

Susuriin natin ang mga bahagi at benepisyo ng A2A, kasama ang isang halimbawa kung paano ito maaaring gamitin sa ating travel application.

### Mga Pangunahing Bahagi ng A2A

Ang A2A ay nakatuon sa pagpapagana ng komunikasyon sa pagitan ng mga agents at pagpapagawa sa kanila ng mga gawain para sa user. Ang bawat bahagi ng protocol ay may kontribusyon dito:

#### Agent Card

Katulad ng kung paano nagbabahagi ang isang MCP server ng listahan ng tools, ang Agent Card ay may:
- Pangalan ng Agent.
- **Deskripsyon ng mga pangkalahatang gawain** na natatapos nito.
- **Listahan ng mga partikular na kasanayan** na may mga deskripsyon upang matulungan ang ibang agents (o maging ang mga human users) na maunawaan kung kailan at bakit nila tatawagin ang agent na iyon.
- Ang **kasalukuyang Endpoint URL** ng agent.
- Ang **bersyon** at **kakayahan** ng agent tulad ng streaming responses at push notifications.

#### Agent Executor

Ang Agent Executor ang responsable sa **pagpapasa ng context ng user chat sa remote agent**, na kailangan ng remote agent upang maunawaan ang gawain na kailangang tapusin. Sa isang A2A server, ang isang agent ay gumagamit ng sarili nitong Large Language Model (LLM) upang i-parse ang mga incoming requests at isagawa ang mga gawain gamit ang sarili nitong internal tools.

#### Artifact

Kapag natapos ng remote agent ang hinihinging gawain, ang produkto ng trabaho nito ay nililikha bilang isang artifact. Ang artifact ay **naglalaman ng resulta ng trabaho ng agent**, isang **deskripsyon ng kung ano ang natapos**, at ang **text context** na ipinadala sa protocol. Kapag naipadala na ang artifact, ang koneksyon sa remote agent ay isinasara hanggang sa muli itong kailanganin.

#### Event Queue

Ang bahaging ito ay ginagamit para sa **paghawak ng mga update at pagpapasa ng mga mensahe**. Ito ay partikular na mahalaga sa produksyon para sa agentic systems upang maiwasan ang pagsasara ng koneksyon sa pagitan ng mga agents bago matapos ang isang gawain, lalo na kung ang oras ng pagkumpleto ng gawain ay maaaring tumagal.

### Mga Benepisyo ng A2A

• **Mas Pinahusay na Kolaborasyon**: Pinapagana nito ang mga agents mula sa iba't ibang vendor at platform na makipag-ugnayan, magbahagi ng context, at magtulungan, na nagpapadali sa seamless automation sa mga tradisyunal na disconnected na sistema.

• **Flexibility sa Model Selection**: Ang bawat A2A agent ay maaaring magdesisyon kung aling LLM ang gagamitin nito upang i-service ang mga requests, na nagpapahintulot sa optimized o fine-tuned na models bawat agent, hindi tulad ng isang single LLM connection sa ilang MCP scenarios.

• **Built-in Authentication**: Ang authentication ay direktang isinama sa A2A protocol, na nagbibigay ng matibay na security framework para sa interaksyon ng mga agents.

### Halimbawa ng A2A

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.tl.png)

Palawakin natin ang ating travel booking scenario, ngunit sa pagkakataong ito gamit ang A2A.

1. **Request ng User sa Multi-Agent**: Ang isang user ay nakikipag-ugnayan sa isang "Travel Agent" A2A client/agent, marahil sa pamamagitan ng pagsasabi, "Paki-book ng buong biyahe papuntang Honolulu para sa susunod na linggo, kasama ang flights, hotel, at rental car."

2. **Orkestrasyon ng Travel Agent**: Natatanggap ng Travel Agent ang kumplikadong request na ito. Ginagamit nito ang LLM nito upang mag-isip tungkol sa gawain at matukoy na kailangan nitong makipag-ugnayan sa iba pang specialized agents.

3. **Komunikasyon sa pagitan ng Agents**: Ang Travel Agent ay gumagamit ng A2A protocol upang kumonekta sa mga downstream agents, tulad ng isang "Airline Agent," isang "Hotel Agent," at isang "Car Rental Agent" na ginawa ng iba't ibang kumpanya.

4. **Delegated Task Execution**: Ang Travel Agent ay nagpapadala ng mga partikular na gawain sa mga specialized agents na ito (hal., "Maghanap ng flights papuntang Honolulu," "Mag-book ng hotel," "Mag-rent ng kotse"). Ang bawat isa sa mga specialized agents, na nagpapatakbo ng sarili nilang LLMs at gumagamit ng sarili nilang tools (na maaaring MCP servers mismo), ay gumagawa ng partikular na bahagi ng booking.

5. **Pinagsamang Tugon**: Kapag natapos ng lahat ng downstream agents ang kanilang mga gawain, pinagsasama-sama ng Travel Agent ang mga resulta (detalye ng flight, kumpirmasyon ng hotel, booking ng car rental) at nagpapadala ng komprehensibo, chat-style na tugon pabalik sa user.

## Natural Language Web (NLWeb)

Ang mga website ay matagal nang pangunahing paraan para sa mga user na ma-access ang impormasyon at data sa internet.

Tingnan natin ang iba't ibang bahagi ng NLWeb, ang mga benepisyo nito, at isang halimbawa kung paano gumagana ang NLWeb sa pamamagitan ng pagtingin sa ating travel application.

### Mga Bahagi ng NLWeb

- **NLWeb Application (Core Service Code)**: Ang sistema na nagpoproseso ng mga natural language na tanong. Kinokonekta nito ang iba't ibang bahagi ng platform upang makagawa ng mga tugon. Maaari mo itong isipin bilang ang **engine na nagpapagana sa natural language features** ng isang website.

- **NLWeb Protocol**: Ito ay isang **basic na set ng rules para sa natural language interaction** sa isang website. Nagpapadala ito ng mga tugon sa JSON format (madalas gamit ang Schema.org). Ang layunin nito ay lumikha ng simpleng pundasyon para sa “AI Web,” katulad ng kung paano ginawa ng HTML na posible ang pagbabahagi ng mga dokumento online.

- **MCP Server (Model Context Protocol Endpoint)**: Ang bawat NLWeb setup ay gumagana rin bilang isang **MCP server**. Nangangahulugan ito na maaari itong **magbahagi ng tools (tulad ng “ask” method) at data** sa iba pang AI systems. Sa praktikal, ginagawa nitong magagamit ng AI agents ang nilalaman at kakayahan ng website, na nagpapahintulot sa site na maging bahagi ng mas malawak na “agent ecosystem.”

- **Embedding Models**: Ang mga modelong ito ay ginagamit upang **i-convert ang nilalaman ng website sa numerical representations na tinatawag na vectors** (embeddings). Ang mga vectors na ito ay kumukuha ng kahulugan sa paraang maaaring ikumpara at hanapin ng mga computer. Ini-store ang mga ito sa isang espesyal na database, at maaaring pumili ang mga user kung aling embedding model ang nais nilang gamitin.

- **Vector Database (Retrieval Mechanism)**: Ang database na ito ay **nag-iimbak ng embeddings ng nilalaman ng website**. Kapag may nagtanong, sinisiyasat ng NLWeb ang vector database upang mabilis na mahanap ang pinaka-nauugnay na impormasyon. Nagbibigay ito ng mabilis na listahan ng mga posibleng sagot, na niraranggo batay sa similarity. Gumagana ang NLWeb sa iba't ibang vector storage systems tulad ng Qdrant, Snowflake, Milvus, Azure AI Search, at Elasticsearch.

### Halimbawa ng NLWeb

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.tl.png)

Isipin ang ating travel booking website, ngunit sa pagkakataong ito, pinapagana ng NLWeb.

1. **Data Ingestion**: Ang umiiral na product catalogs ng travel website (hal., flight listings, hotel descriptions, tour packages) ay naka-format gamit ang Schema.org o na-load sa pamamagitan ng RSS feeds. Ang tools ng NLWeb ay nag-i-ingest ng structured data na ito, gumagawa ng embeddings, at ini-store ang mga ito sa isang lokal o remote na vector database.

2. **Natural Language Query (Human)**: Ang isang user ay bumibisita sa website at, sa halip na mag-navigate sa mga menu, nagta-type sa isang chat interface: "Maghanap ng family-friendly na hotel sa Honolulu na may pool para sa susunod na linggo."

3. **NLWeb Processing**: Natatanggap ng NLWeb application ang query na ito. Ipinapadala nito ang query sa isang LLM para sa pag-unawa at sabay na sinisiyasat ang vector database nito para sa mga nauugnay na hotel listings.

4. **Accurate Results**: Tinutulungan ng LLM na i-interpret ang mga search results mula sa database, kilalanin ang pinakamahusay na mga tugma batay sa "family-friendly," "pool," at "Honolulu" na criteria, at pagkatapos ay i-format ang isang natural language na tugon. Mahalagang tandaan, ang tugon ay tumutukoy sa aktwal na mga hotel mula sa catalog ng website, na iniiwasan ang mga gawa-gawang impormasyon.

5. **AI Agent Interaction**: Dahil ang NLWeb ay nagsisilbing MCP server, maaaring kumonekta ang isang external AI travel agent sa NLWeb instance ng website na ito. Ang AI agent ay maaaring gumamit ng `ask` MCP method upang direktang magtanong sa website: `ask("Mayroon bang mga vegan-friendly na restaurant sa lugar ng Honolulu na inirerekomenda ng hotel?")`. Ipoproseso ng NLWeb instance ito, gamit ang database ng impormasyon ng restaurant (kung na-load), at magbabalik ng structured JSON response.

### May Karagdagang Tanong Tungkol sa MCP/A2A/NLWeb?

Sumali sa [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagtagpo sa ibang mga nag-aaral, dumalo sa office hours, at makuha ang mga sagot sa iyong mga tanong tungkol sa AI Agents.

## Mga Resources

- [MCP para sa Mga Baguhan](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.