# Paggamit ng Agentic Protocols (MCP, A2A at NLWeb)

[![Mga Agentic Protocol](../../../translated_images/tl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(I-click ang larawan sa itaas upang panoorin ang video ng leksyong ito)_

Habang lumalago ang paggamit ng mga AI agent, lumalago rin ang pangangailangan para sa mga protokol na nagsisiguro ng standardisasyon, seguridad, at sumusuporta sa bukas na inobasyon. Sa leksyong ito, tatalakayin natin ang 3 protokol na naghahangad tugunan ang pangangailangang ito - Model Context Protocol (MCP), Agent to Agent (A2A) at Natural Language Web (NLWeb).

## Panimula

Sa leksiyon na ito, tatalakayin natin:

• Paano pinapayagan ng **MCP** ang mga AI agent na ma-access ang mga panlabas na kasangkapan at datos upang makumpleto ang mga gawain ng gumagamit.

•  Paano pinahihintulutan ng **A2A** ang komunikasyon at pakikipagtulungan sa pagitan ng iba't ibang AI agent.

• Paano dinadala ng **NLWeb** ang mga natural language na interface sa anumang website na nagpapahintulot sa mga AI agent na matuklasan at makipag-ugnayan sa nilalaman.

## Mga Layunin sa Pagkatuto

• **Tukuyin** ang pangunahing layunin at mga benepisyo ng MCP, A2A, at NLWeb sa konteksto ng mga AI agent.

• **Ipaliwanag** kung paano bawat protokol nagpapadali ng komunikasyon at interaksyon sa pagitan ng LLMs, mga kasangkapan, at iba pang mga ahente.

• **Kilalanin** ang natatanging mga papel na ginagampanan ng bawat protokol sa pagbuo ng mga kumplikadong sistemang agentic.

## Model Context Protocol

Ang **Model Context Protocol (MCP)** ay isang bukas na pamantayan na nagbibigay ng isang istandardisadong paraan para ang mga aplikasyon ay magbigay ng konteksto at mga kasangkapan sa mga LLM. Ito ay nagbibigay-daan sa isang "unibersal na adaptor" sa iba't ibang pinagkukunan ng datos at mga kasangkapan na maaaring ikonekta ng mga AI agent sa isang pare-parehong paraan.

Tingnan natin ang mga bahagi ng MCP, ang mga benepisyo kumpara sa direktang paggamit ng API, at isang halimbawa kung paano maaaring gumamit ang mga AI agent ng isang MCP server.

### Mga Pangunahing Bahagi ng MCP

Ang MCP ay gumagana sa isang **client-server architecture** at ang mga pangunahing bahagi ay:

• **Hosts** ay mga aplikasyon ng LLM (halimbawa isang code editor tulad ng VSCode) na nagsisimula ng mga koneksyon sa isang MCP Server.

• **Clients** ay mga komponent sa loob ng host application na nagpapanatili ng one-to-one na koneksyon sa mga server.

• **Servers** ay magagaan na programa na nag-eekspos ng mga tiyak na kakayahan.

Kasama sa protokol ang tatlong pangunahing primitiva na siyang mga kakayahan ng isang MCP Server:

• **Tools**: Ito ay mga hiwalay na aksyon o function na maaaring tawagin ng isang AI agent upang magsagawa ng isang gawain. Halimbawa, maaaring i-expose ng isang weather service ang isang "get weather" na tool, o maaaring i-expose ng isang e-commerce server ang isang "purchase product" na tool. I-a-advertise ng mga MCP server ang pangalan ng bawat tool, paglalarawan, at input/output schema sa kanilang listing ng mga kakayahan.

• **Resources**: Ito ay mga read-only na item ng datos o dokumento na maaaring ibigay ng isang MCP server, at maaaring kunin ng mga client ayon sa pangangailangan. Kabilang dito ang nilalaman ng file, mga rekord ng database, o mga log file. Ang mga resources ay maaaring teksto (tulad ng code o JSON) o binary (tulad ng mga imahe o PDF).

• **Prompts**: Ito ay mga paunang-depinidong template na nagbibigay ng mga mungkahing prompt, na nagpapahintulot ng mas kumplikadong mga workflow.

### Mga Benepisyo ng MCP

Nag-aalok ang MCP ng makabuluhang mga pakinabang para sa mga AI Agent:

• **Dinamiko na Pag-diskubre ng Tool**: Maaaring makatanggap nang dinamik ng listahan ng magagamit na mga tool ang mga agent mula sa isang server kasama ang mga paglalarawan ng ginagawa ng mga ito. Ito ay taliwas sa tradisyonal na mga API, na madalas nangangailangan ng static na pag-code para sa mga integrasyon, na nangangahulugang anumang pagbabago sa API ay nangangailangan ng pag-update ng code. Nag-aalok ang MCP ng isang "integrate once" na paraan, na nagdudulot ng mas malaking kakayahang mag-adapt.

• **Pagkakainteroperable sa Iba't Ibang LLM**: Gumagana ang MCP sa iba't ibang LLM, nagbibigay ng kakayahang magpalit ng pangunahing mga modelo upang suriin para sa mas magandang performance.

• **Istandardisadong Seguridad**: May kasama ang MCP na istandardisadong paraan ng authentication, nagpapabuti ng kakayahang mag-scale kapag nagdaragdag ng access sa karagdagang MCP server. Mas simple ito kaysa sa pamamahala ng iba't ibang susi at uri ng authentication para sa iba't ibang tradisyonal na API.

### Halimbawa ng MCP

![Diagram ng MCP](../../../translated_images/tl/mcp-diagram.e4ca1cbd551444a1.webp)

Isipin na nais ng isang gumagamit na mag-book ng flight gamit ang isang AI assistant na pinalakas ng MCP.

1. **Koneksyon**: Ang AI assistant (ang MCP client) ay kumokonekta sa isang MCP server na ibinigay ng isang airline.

2. **Tool Discovery**: Tinanong ng client ang MCP server ng airline, "Anong mga tool ang mayroon kayo?" Sumagot ang server na may mga tool tulad ng "search flights" at "book flights".

3. **Tool Invocation**: Pagkatapos tinanong mo ang AI assistant, "Paki-search ng flight mula Portland papuntang Honolulu." Kinilala ng AI assistant, gamit ang LLM nito, na kailangan nitong tawagin ang "search flights" na tool at ipinasa ang mga kaugnay na parameter (origin, destination) sa MCP server.

4. **Execution and Response**: Gumagawa ang MCP server, bilang isang wrapper, ng aktwal na tawag sa internal booking API ng airline. Tinatanggap nito ang impormasyon ng flight (hal., JSON data) at ipinapadala pabalik ito sa AI assistant.

5. **Further Interaction**: Ipinapakita ng AI assistant ang mga pagpipilian sa flight. Kapag pinili mo ang isang flight, maaaring tawagin ng assistant ang "book flight" tool sa parehong MCP server, tinatapos ang booking.

## Protocol ng Agent-sa-Agent (A2A)

Habang nakatuon ang MCP sa pagkonekta ng mga LLM sa mga kasangkapan, umuuna ang **Agent-to-Agent (A2A) protocol** sa pamamagitan ng pagpapahintulot ng komunikasyon at pakikipagtulungan sa pagitan ng iba't ibang AI agent. Kinokonekta ng A2A ang mga AI agent mula sa iba't ibang organisasyon, kapaligiran at tech stack upang tapusin ang isang pinagsasaluhang gawain.

Susuriin natin ang mga bahagi at benepisyo ng A2A, kasama ang isang halimbawa kung paano ito maaaring ilapat sa ating travel application.

### Mga Pangunahing Bahagi ng A2A

Nakatuon ang A2A sa pagpapahintulot ng komunikasyon sa pagitan ng mga agent at sa pagpapagawa sa kanila ng pagtutulungan upang tapusin ang isang subtasks ng gumagamit. Ang bawat bahagi ng protokol ay nag-aambag dito:

#### Agent Card

Katulad ng paraan na nagbabahagi ang isang MCP server ng listahan ng mga tool, ang isang Agent Card ay may:
- Ang Pangalan ng Ahente.
- Isang **paglalarawan ng pangkalahatang mga gawain** na kanyang ginagawa.
- Isang **listahan ng mga tiyak na kasanayan** na may mga paglalarawan upang tulungan ang ibang mga ahente (o kahit na mga taong gumagamit) na maunawaan kung kailan at bakit nila tatawagin ang ahenteng iyon.
- Ang **kasalukuyang Endpoint URL** ng ahente
- Ang **bersyon** at **mga kakayahan** ng ahente tulad ng streaming responses at push notifications.

#### Agent Executor

Ang Agent Executor ang responsable sa **pagpapasa ng konteksto ng usapan ng gumagamit sa remote na ahente**, kailangan ito ng remote na ahente upang maunawaan ang gawain na kailangang matapos. Sa isang A2A server, gumagamit ang isang ahente ng sarili nitong Large Language Model (LLM) upang i-parse ang papasok na mga kahilingan at isagawa ang mga gawain gamit ang sariling internal nitong mga kasangkapan.

#### Artifact

Kapag natapos na ng remote na ahente ang hinihinging gawain, ang kanyang produktong gawa ay nililikha bilang isang artifact. Ang isang artifact ay **naglalaman ng resulta ng gawain ng ahente**, isang **paglalarawan ng kung ano ang natapos**, at ang **text context** na ipinadala sa pamamagitan ng protokol. Pagkatapos maipadala ang artifact, isinasara ang koneksyon sa remote na ahente hanggang kailanganin muli.

#### Event Queue

Ang komponenteng ito ay ginagamit para sa **pag-handle ng mga update at pagpapasa ng mga mensahe**. Partikular itong mahalaga sa produksyon para sa mga agentic na sistema upang maiwasan ang pagsasara ng koneksyon sa pagitan ng mga ahente bago matapos ang isang gawain, lalo na kapag maaaring tumagal nang mas matagal ang oras ng pagkumpleto ng gawain.

### Mga Benepisyo ng A2A

• **Pinalawak na Pakikipagtulungan**: Pinapahintulutan nito ang mga ahente mula sa iba't ibang vendor at platform na makipag-ugnayan, magbahagi ng konteksto, at magtulungan, na nagpapadali ng tuloy-tuloy na awtomasyon sa tradisyonal na mga hiwalay na sistema.

• **Kakayahang Pumili ng Modelo**: Maaaring magpasya ang bawat A2A agent kung aling LLM ang gagamitin upang paglingkuran ang mga kahilingan nito, na nagpapahintulot ng mga na-optimize o fine-tuned na modelo bawat ahente, taliwas sa isang solong koneksyon ng LLM sa ilang MCP senaryo.

• **Naka-integrate na Authentication**: Ang authentication ay direktang naka-integrate sa A2A protocol, nagbibigay ng matibay na framework ng seguridad para sa interaksyon ng mga ahente.

### Halimbawa ng A2A

![Diagram ng A2A](../../../translated_images/tl/A2A-Diagram.8666928d648acc26.webp)

Palawakin natin ang ating senaryo ng pag-book ng biyahe, ngunit sa pagkakataong ito gamit ang A2A.

1. **Kahilingan ng Gumagamit sa Multi-Agent**: Nakikipag-ugnayan ang isang gumagamit sa isang "Travel Agent" A2A client/agent, marahil sa pagsabing, "Paki-book ang buong biyahe papuntang Honolulu para sa susunod na linggo, kasama ang mga flight, hotel, at renta ng kotse".

2. **Orkestrasyon ng Travel Agent**: Tinatanggap ng Travel Agent ang komplikadong kahilingang ito. Ginagamit nito ang LLM nito upang mag-reaksyon tungkol sa gawain at tukuyin na kailangan nitong makipag-ugnayan sa ibang mga espesyalisadong ahente.

3. **Inter-Agent Communication**: Pagkatapos ay ginagamit ng Travel Agent ang A2A protocol upang kumonekta sa mga downstream na ahente, tulad ng isang "Airline Agent," isang "Hotel Agent," at isang "Car Rental Agent" na nilikha ng iba't ibang kumpanya.

4. **Delegadong Pagpapatupad ng Gawain**: Ipinapadala ng Travel Agent ang mga tiyak na gawain sa mga espesyalisadong ahenteng ito (hal., "Hanapin ang mga flight papuntang Honolulu," "Mag-book ng hotel," "Mag-renta ng kotse"). Bawat isa sa mga espesyalisadong ahenteng ito, na nagpapatakbo ng kanilang sariling LLMs at gumagamit ng kanilang sariling mga kasangkapan (na maaaring mga MCP server din), ay isinasagawa ang kanilang bahagi ng booking.

5. **Pinagsamang Tugon**: Kapag natapos na ng lahat ng downstream na ahente ang kanilang mga gawain, pinagsama ng Travel Agent ang mga resulta (mga detalye ng flight, kumpirmasyon ng hotel, booking ng renta ng kotse) at nagpadala ng isang komprehensibo, chat-style na tugon pabalik sa gumagamit.

## Natural Language Web (NLWeb)

Matagal nang pangunahing paraan ang mga website para sa mga gumagamit upang ma-access ang impormasyon at datos sa internet.

Tingnan natin ang iba't ibang bahagi ng NLWeb, ang mga benepisyo ng NLWeb at isang halimbawa kung paano gumagana ang ating NLWeb sa pamamagitan ng pagtingin sa ating travel application.

### Mga Bahagi ng NLWeb

- **NLWeb Application (Core Service Code)**: Ang sistema na nagpo-proseso ng mga tanong sa natural na wika. Kinokonekta nito ang iba't ibang bahagi ng platform upang lumikha ng mga sagot. Maaari mo itong isipin bilang ang **engine na nagpapatakbo ng mga tampok na natural language** ng isang website.

- **NLWeb Protocol**: Ito ay isang **pundamental na hanay ng mga patakaran para sa interaksiyong natural language** sa isang website. Nagbabalik ito ng mga tugon sa format na JSON (madalas gamit ang Schema.org). Ang layunin nito ay lumikha ng isang simpleng pundasyon para sa "AI Web," sa parehong paraan na ginawang posible ng HTML ang pagbabahagi ng mga dokumento online.

- **MCP Server (Model Context Protocol Endpoint)**: Bawat NLWeb setup ay gumagana rin bilang isang **MCP server**. Ibig sabihin nito, maaari itong **magbahagi ng mga tool (tulad ng isang “ask” method) at data** sa ibang mga AI system. Sa praktika, ginagawa nitong magagamit ng mga AI agent ang nilalaman at kakayahan ng website, na nagpapahintulot sa site na maging bahagi ng mas malawak na "agent ecosystem."

- **Embedding Models**: Ang mga modelong ito ay ginagamit upang **i-convert ang nilalaman ng website sa mga numerikal na representasyon na tinatawag na vectors** (embeddings). Hinahawakan ng mga vector na ito ang kahulugan sa paraang maaaring i-compare at i-search ng mga kompyuter. Iniimbak ang mga ito sa isang espesyal na database, at maaaring pumili ang mga gumagamit kung aling embedding model ang nais nilang gamitin.

- **Vector Database (Retrieval Mechanism)**: Ang database na ito **nag-iimbak ng mga embedding ng nilalaman ng website**. Kapag may nagtanong, sinusuri ng NLWeb ang vector database upang mabilis na mahanap ang pinaka-may-kaugnayang impormasyon. Nagbibigay ito ng mabilis na listahan ng mga posibleng sagot, niranggo ayon sa pagkakahalintulad. Gumagana ang NLWeb sa iba't ibang vector storage system tulad ng Qdrant, Snowflake, Milvus, Azure AI Search, at Elasticsearch.

### Halimbawa ng NLWeb

![NLWeb](../../../translated_images/tl/nlweb-diagram.c1e2390b310e5fe4.webp)

Isaalang-alang muli ang ating travel booking website, ngunit sa pagkakataong ito, ito ay pinapagana ng NLWeb.

1. **Data Ingestion**: Ang umiiral na mga katalogo ng produkto ng travel website (hal., listahan ng flight, paglalarawan ng hotel, mga tour package) ay ini-format gamit ang Schema.org o niloload sa pamamagitan ng RSS feed. Ina-ingest ng mga tool ng NLWeb ang naka-istrukturang data na ito, lumilikha ng mga embeddings, at iniimbak ang mga ito sa lokal o remote na vector database.

2. **Natural Language Query (Human)**: Bumibisita ang isang gumagamit sa website at, imbes na mag-navigate sa mga menu, nagta-type sa isang chat interface: "Hanapan mo ako ng family-friendly na hotel sa Honolulu na may pool para sa susunod na linggo".

3. **Pagproseso ng NLWeb**: Tinatanggap ng NLWeb application ang query na ito. Ipinapadala nito ang query sa isang LLM para sa pag-unawa at sabay na hinahanap ang vector database para sa mga may-kaugnayang listahan ng hotel.

4. **Tamang Mga Resulta**: Tumutulong ang LLM upang ipakahulugan ang mga resulta ng paghahanap mula sa database, tukuyin ang pinakamahusay na tugma batay sa mga kriteriang "family-friendly," "pool," at "Honolulu", at pagkatapos ay i-format ang isang tugon sa natural na wika. Mahalaga, ang tugon ay tumutukoy sa aktwal na mga hotel mula sa katalogo ng website, na iniiwasan ang mga ipinapasang gawa-gawang impormasyon.

5. **Pakikipag-ugnayan ng AI Agent**: Dahil nagsisilbi ang NLWeb bilang isang MCP server, maaaring kumonekta ang isang external na AI travel agent sa NLWeb instance ng website na ito. Maaari nang gamitin ng AI agent ang `ask` MCP method upang direktang i-query ang website: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. Ipoproseso ito ng NLWeb instance, gamit ang database nito ng impormasyon tungkol sa mga restaurant (kung na-load), at magbabalik ng isang istrukturadong JSON na tugon.

### May Karagdagang Mga Tanong tungkol sa MCP/A2A/NLWeb?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa iba pang mga mag-aaral, dumalo sa oras ng opisina at masagot ang iyong mga tanong tungkol sa AI Agents.

## Mga Mapagkukunan

- [MCP para sa mga Nagsisimula](https://aka.ms/mcp-for-beginners)  
- [Dokumentasyon ng MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repo ng NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Paunawa:
Ang dokumentong ito ay isinalin gamit ang serbisyong AI para sa pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakitandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na bahagi. Dapat ituring na awtoritatibong sanggunian ang orihinal na dokumento sa orihinal nitong wika. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin na isinagawa ng isang taong tagapagsalin. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na bunga ng paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->