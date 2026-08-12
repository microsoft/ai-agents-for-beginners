# Paggamit ng Agentic Protocols (MCP, A2A at NLWeb)

[![Agentic Protocols](../../../translated_images/tl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(I-click ang larawan sa itaas upang mapanood ang video ng leksiyon na ito)_

Habang lumalawak ang paggamit ng AI agents, gayundin ang pangangailangan para sa mga protocol na nagsisiguro ng standardisasyon, seguridad, at pagsuporta sa bukas na inobasyon. Sa leksyong ito, tatalakayin natin ang 3 protocol na layuning tugunan ang pangangailangang ito - Model Context Protocol (MCP), Agent to Agent (A2A) at Natural Language Web (NLWeb).

## Panimula

Sa leksyong ito, tatalakayin natin:

• Paano pinapayagan ng **MCP** ang AI Agents na ma-access ang mga panlabas na tools at datos upang matapos ang mga gawain ng user.

• Paano pinapayagan ng **A2A** ang komunikasyon at kolaborasyon sa pagitan ng iba't ibang AI agents.

• Paano nagbibigay ang **NLWeb** ng natural language interfaces sa anumang website upang payagan ang AI Agents na matuklasan at makipag-ugnayan sa nilalaman.

## Mga Layunin ng Pagkatuto

• **Tukuyin** ang pangunahing layunin at benepisyo ng MCP, A2A, at NLWeb sa konteksto ng AI agents.

• **Ipaliwanag** kung paano pinadadali ng bawat protocol ang komunikasyon at interaksyon sa pagitan ng LLMs, tools, at iba pang agents.

• **Kilalanin** ang natatanging papel na ginagampanan ng bawat protocol sa pagbuo ng komplikadong mga agentic system.

## Model Context Protocol

Ang **Model Context Protocol (MCP)** ay isang open standard na nagbibigay ng isang na-standardize na paraan para sa mga aplikasyon upang magbigay ng konteksto at mga tools sa LLMs. Ito ay nagbibigay-daan para sa isang "universal adaptor" sa iba't ibang pinagkukunan ng datos at mga tools na maaaring ikonekta ng AI Agents sa isang pare-parehong paraan.

Tingnan natin ang mga bahagi ng MCP, ang mga benepisyo kumpara sa direktang paggamit ng API, at isang halimbawa kung paano maaaring gamitin ng mga AI agents ang isang MCP server.

### Mga Pangunahing Bahagi ng MCP

Ang MCP ay gumagana sa isang **client-server architecture** at ang pangunahing mga bahagi ay:

• **Hosts** ay mga aplikasyon ng LLM (halimbawa isang code editor tulad ng VSCode) na nagsisimula ng mga koneksyon sa isang MCP Server.

• **Clients** ay mga bahagi sa loob ng host application na nagpapanatili ng one-to-one connections sa mga server.

• **Servers** ay mga magagaan na programa na naglalantad ng mga tiyak na kakayahan.

Kasama sa protocol ang tatlong pangunahing primitives na mga kakayahan ng isang MCP Server:

• **Tools**: Ito ay mga hiwalay na aksyon o function na maaaring tawagan ng isang AI agent upang magsagawa ng aksyon. Halimbawa, ang isang weather service ay maaaring magbigay ng "get weather" tool, o ang isang e-commerce server ay maaaring magbigay ng "purchase product" tool. Ipinapahayag ng mga MCP server ang pangalan ng bawat tool, paglalarawan, at input/output schema sa kanilang listahan ng kakayahan.

• **Resources**: Ito ay mga data item o dokumento na read-only na maaaring ibigay ng MCP server, at maaaring kunin ng mga client kapag kinakailangan. Halimbawa ay laman ng file, talaan ng database, o mga log file. Ang mga resources ay maaaring teksto (tulad ng code o JSON) o binary (tulad ng mga larawan o PDF).

• **Prompts**: Ito ay mga paunang naitakdang template na nagbibigay ng mga mungkahing prompt, na nagpapahintulot para sa mas komplikadong mga workflow.

### Mga Benepisyo ng MCP

Nagbibigay ang MCP ng malalaking kalamangan para sa mga AI Agents:

• **Dynamic Tool Discovery**: Maaari dynamically matanggap ng mga agent ang listahan ng mga magagamit na tool mula sa isang server kasama ang mga paglalarawan ng kanilang ginagawa. Ito ay kabaligtaran sa tradisyunal na mga API na madalas nangangailangan ng static na coding para sa mga integration, ibig sabihin ang anumang pagbabago sa API ay nangangailangan din ng pag-update ng code. Nagbibigay ang MCP ng "integrate once" na pamamaraan, na nagbubunga ng mas mataas na kakayahan sa pag-adjust.

• **Interoperability Across LLMs**: Gumagana ang MCP sa iba't ibang LLMs, nagbibigay ng kalayaan para palitan ang core models upang masuri para sa mas mahusay na performance.

• **Standardized Security**: Kasama sa MCP ang isang standard na paraan ng authentication, na nagpapabuti ng scalability kapag nagdadagdag ng access sa karagdagang MCP servers. Mas madali ito kaysa sa pamamahala ng iba't ibang mga key at uri ng authentication para sa iba't ibang tradisyunal na mga API.

### Halimbawa ng MCP

![MCP Diagram](../../../translated_images/tl/mcp-diagram.e4ca1cbd551444a1.webp)

Isipin ang isang user na nais mag-book ng flight gamit ang AI assistant na pinapagana ng MCP.

1. **Koneksyon**: Ang AI assistant (ang MCP client) ay kumokonekta sa isang MCP server na ibinigay ng isang airline.

2. **Pagkilala sa Tool**: Tinanong ng client ang MCP server ng airline, "Anong mga tool ang mayroon kayo?" Sumagot ang server ng mga tool tulad ng "search flights" at "book flights".

3. **Pagtawag sa Tool**: Pagkatapos ay tinanong mo ang AI assistant, "Paki-search ng flight mula Portland papuntang Honolulu." Gamit ang LLM nito, natukoy ng AI assistant na kailangang tawagan ang "search flights" tool at ipinapasa ang kaukulang mga parameter (origin, destination) sa MCP server.

4. **Pagsasagawa at Tugon**: Bilang isang wrapper, tinatawagan ng MCP server ang internal booking API ng airline. Tinatanggap nito ang impormasyon ng flight (hal., JSON data) at ipinapasa ito pabalik sa AI assistant.

5. **Karagdagang Interaksyon**: Ipinapakita ng AI assistant ang mga opsyon ng flight. Kapag pumili ka na ng flight, maaaring tawagin ng assistant ang "book flight" tool sa parehong MCP server upang makumpleto ang booking.

## Agent-to-Agent Protocol (A2A)

Habang ang MCP ay nakatuon sa pagkonekta ng LLMs sa mga tool, ang **Agent-to-Agent (A2A) protocol** ay nagsusulong ng komunikasyon at kolaborasyon sa pagitan ng iba't ibang AI agents. Pinag-uugnay ng A2A ang mga AI agents mula sa iba't ibang organisasyon, kapaligiran, at tech stacks upang matapos ang isang pinag-isang gawain.

Susuriin natin ang mga bahagi at benepisyo ng A2A, pati na rin ang isang halimbawa kung paano ito maaaring ilapat sa ating travel application.

### Pangunahing Bahagi ng A2A

Nakatuon ang A2A sa pagpapahintulot ng komunikasyon sa pagitan ng mga agent upang magtrabaho nang magkakasama sa pagtapos ng isang subtask ng user. Ang bawat bahagi ng protocol ay may kontribusyon dito:

#### Agent Card

Katulad ng pakikibahagi ng MCP server ng listahan ng mga tool, ang Agent Card ay may:
- Ang Pangalan ng Agent.
- Isang **paglalarawan ng mga pangkalahatang gawain** na ginagawa nito.
- Isang **listahan ng mga espesipikong kasanayan** na may mga paglalarawan upang makatulong sa ibang mga agent (o kahit mga human user) upang maunawaan kung kailan at bakit nila tatawagan ang agent na iyon.
- Ang **kasalukuyang Endpoint URL** ng agent
- Ang **bersyon** at **kakayahan** ng agent tulad ng streaming responses at push notifications.

#### Agent Executor

Ang Agent Executor ay responsable sa **pagpapasa ng konteksto ng user chat sa remote agent**, kailangan ito ng remote agent upang maunawaan ang gawain na kailangang tapusin. Sa isang A2A server, gumagamit ang isang agent ng sarili nitong Large Language Model (LLM) upang suriin ang mga papasok na kahilingan at isagawa ang mga gawain gamit ang sarili nitong internal tools.

#### Artifact

Kapag natapos na ng remote agent ang hinihinging gawain, ang produkto ng trabaho nito ay nililikha bilang artifact. Ang isang artifact ay naglalaman ng resulta ng trabaho ng agent, isang paglalarawan ng nagawa, at ang tekstong konteksto na ipinasa sa protocol. Matapos maipadala ang artifact, pinipigil ang koneksyon sa remote agent hanggang sa kailanganin muli.

#### Event Queue

Ginagamit ang bahaging ito para sa **paghawak ng mga update at pagpapasa ng mga mensahe**. Mahalaga ito sa produksyon ng agentic systems upang maiwasan ang pagsasara ng koneksyon sa pagitan ng mga agents bago matapos ang gawain, lalo na kapag ang mga gawain ay nangangailangan ng mas mahabang panahon.

### Mga Benepisyo ng A2A

• **Pinahusay na Kolaborasyon**: Pinapayagan nito ang mga agent mula sa iba't ibang vendor at platform na makipag-ugnayan, magbahagi ng konteksto, at magtrabaho nang magkakasama, na nagpapadali ng tuluy-tuloy na automation sa tradisyunal na magkakahiwalay na sistema.

• **Kalayaan sa Pagpili ng Model**: Ang bawat A2A agent ay maaaring magdesisyon kung aling LLM ang gagamitin nito upang tugunan ang mga kahilingan, na nagpapahintulot ng optimized o fine-tuned na modelo para sa bawat agent, hindi tulad ng isang solong LLM connection sa ilang MCP scenario.

• **Integrated Authentication**: Ang authentication ay direktang bahagi ng A2A protocol, nagbibigay ng matibay na security framework para sa interaksyon ng mga agent.

### Halimbawa ng A2A

![A2A Diagram](../../../translated_images/tl/A2A-Diagram.8666928d648acc26.webp)

Palalawakin natin ang ating halimbawa ng travel booking, ngunit ngayon gamit ang A2A.

1. **Hiling ng User sa Multi-Agent**: Nakikipag-ugnayan ang user sa isang "Travel Agent" A2A client/agent, marahil sa pagsabi, "Paki-book ng buong trip papuntang Honolulu sa susunod na linggo, kasama na ang mga flight, hotel, at rental car."

2. **Orkestrasyon ng Travel Agent**: Natatanggap ng Travel Agent ang komplikadong kahilingan. Ginagamit nito ang LLM upang pag-isipan ang gawain at tukuyin na kailangan nitong makipag-ugnayan sa ibang espesyalista na mga agent.

3. **Komunikasyon sa pagitan ng mga Agent**: Ginagamit ng Travel Agent ang A2A protocol upang kumonekta sa mga downstream agent, tulad ng "Airline Agent," "Hotel Agent," at "Car Rental Agent" na nilikha ng iba't ibang kumpanya.

4. **Ibinigay na Pagsasagawa ng Gawain**: Nagpapadala ang Travel Agent ng tiyak na mga gawain sa mga espesyalistang agent (hal., "Maghanap ng flight papuntang Honolulu," "Mag-book ng hotel," "Mag-rent ng kotse"). Bawat isa sa mga ito, gamit ang kanilang sariling LLM at sariling tools (na maaaring mga MCP servers din), ay isinasagawa ang bahagi ng booking.

5. **Pinagsama-samang Tugon**: Kapag natapos na ng mga downstream agent ang kanilang mga gawain, pinagsasama-sama ng Travel Agent ang mga resulta (mga detalye ng flight, kumpirmasyon ng hotel, booking ng rent-a-car) at nagpapadala ng komprehensibong tugon, na parang chat, pabalik sa user.

## Natural Language Web (NLWeb)

Matagal nang pangunahing paraan ang mga website para sa mga user upang ma-access ang impormasyon at datos sa internet.

Tingnan natin ang iba't ibang bahagi ng NLWeb, ang mga benepisyo ng NLWeb at isang halimbawa kung paano gumagana ang ating NLWeb sa pamamagitan ng pagtitingin sa ating travel application.

### Mga Bahagi ng NLWeb

- **NLWeb Application (Core Service Code)**: Ang system na nagpoproseso ng mga tanong sa natural na wika. Ito ang nag-uugnay sa iba't ibang bahagi ng platform upang makalikha ng mga tugon. Maaaring isipin ito bilang **engine na nagpapatakbo sa natural language features** ng isang website.

- **NLWeb Protocol**: Ito ay isang **batayang hanay ng mga patakaran para sa natural language interaction** sa isang website. Nagpapadala ito ng mga tugon sa JSON format (madalas gamit ang Schema.org). Layunin nitong lumikha ng simpleng pundasyon para sa "AI Web," tulad ng ginawa ng HTML para sa pagbabahagi ng mga dokumento online.

- **MCP Server (Model Context Protocol Endpoint)**: Bawat setup ng NLWeb ay gumagana rin bilang isang **MCP server**. Nangangahulugan ito na maaari itong **magbahagi ng mga tools (tulad ng “ask” method) at datos** sa iba pang AI system. Sa praktis, nagiging magagamit ng mga AI agents ang nilalaman at kakayahan ng website, pinapahintulutan ang site na maging bahagi ng mas malawak na “agent ecosystem.”

- **Embedding Models**: Ginagamit ang mga modelong ito upang **i-convert ang nilalaman ng website sa mga numerikal na representasyon na tinatawag na vectors** (embeddings). Kinakatawan ng mga vectors na ito ang kahulugan sa paraan na kaya nitong ihambing at hanapin ng mga computer. Sila ay iniimbak sa isang espesyal na database, at maaaring pumili ang mga user kung aling embedding model ang gagamitin nila.

- **Vector Database (Retrieval Mechanism)**: Ang database na ito ay **nag-iimbak ng embeddings ng nilalaman ng website**. Kapag may nagtatanong, sinusuri ng NLWeb ang vector database upang mabilis na mahanap ang pinaka-may kinalamang impormasyon. Nagbibigay ito ng mabilis na listahan ng posibleng sagot, na inayos ayon sa pagkakapareho. Nakikipagtulungan ang NLWeb sa iba't ibang vector storage systems tulad ng Qdrant, Snowflake, Milvus, Azure AI Search, at Elasticsearch.

### NLWeb sa Halimbawa

![NLWeb](../../../translated_images/tl/nlweb-diagram.c1e2390b310e5fe4.webp)

Isipin muli ang ating travel booking website, ngunit ngayon, pinapagana ito ng NLWeb.

1. **Pagsalo ng Datos**: Ang mga umiiral na katalogo ng produkto ng travel website (hal., mga listahan ng flight, paglalarawan ng hotel, mga tour package) ay inaayos gamit ang Schema.org o niloload gamit ang RSS feeds. Tinatanggap ng mga tool ng NLWeb ang tsinakat na datos na ito, lumilikha ng mga embeddings, at iniimbak ito sa isang lokal o remote na vector database.

2. **Natural Language Query (Tao)**: Bumibisita ang user sa website at sa halip na mag-navigate sa mga menu, nagta-type siya sa chat interface: "Hanapan mo ako ng family-friendly na hotel sa Honolulu na may pool para sa susunod na linggo."

3. **Pagpoproseso ng NLWeb**: Natatanggap ng NLWeb application ang query na ito. Ipinapadala nito ang query sa isang LLM para sa pag-unawa at kasabay nito ay naghahanap ito sa vector database para sa relevant na listahan ng hotel.

4. **Tiyak na mga Resulta**: Tumutulong ang LLM upang bigyang-kahulugan ang resulta ng paghahanap mula sa database, tukuyin ang pinakamahusay na tugma base sa mga kriteriang "family-friendly," "pool," at "Honolulu," at pagkatapos ay inihahanda ang tugon sa natural na wika. Mahalaga, ang tugon ay tumutukoy sa totoong mga hotel mula sa katalogo ng website, iniiwasan ang gawang impormasyon.

5. **Interaksyon ng AI Agent**: Dahil nagsisilbing MCP server ang NLWeb, maaaring kumonekta ang isang panlabas na AI travel agent sa instance ng NLWeb ng website na ito. Maaari nitong gamitin ang `ask` MCP method upang direktang magtanong sa website: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. Ipoproseso ito ng NLWeb instance, gamit ang database ng impormasyon ng mga restaurant (kung na-load), at magbibigay ng istrukturadong tugon sa JSON.

### May Karagdagang Mga Tanong Tungkol sa MCP/A2A/NLWeb?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipagkita sa ibang mga nag-aaral, dumalo sa office hours at makakuha ng mga sagot sa iyong mga tanong tungkol sa AI Agents.

## Mga Resources

- [MCP para sa mga Baguhan](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentasyon](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Nakaraang Leksiyon

[AI Agents in Production](../10-ai-agents-production/README.md)

## Susunod na Leksiyon

[Context Engineering para sa AI Agents](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->