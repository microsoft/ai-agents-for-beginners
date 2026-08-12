# Inhenyeriya ng Konteksto para sa mga Ahente ng AI

[![Inhenyeriya ng Konteksto](../../../translated_images/tl/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(I-click ang larawan sa itaas upang mapanood ang video ng araling ito)_

Mahalaga ang pag-unawa sa pagiging kumplikado ng aplikasyon na iyong binubuo para sa isang AI agent upang makalikha ng maaasahan nito. Kailangan nating bumuo ng mga AI Agent na epektibong namamahala ng impormasyon upang matugunan ang mga kumplikadong pangangailangan lampas sa prompt engineering.

Sa araling ito, titingnan natin kung ano ang inhenyeriya ng konteksto at ang papel nito sa pagbuo ng mga AI agent.

## Panimula

Saklaw ng araling ito ang:

• **Ano ang Inhenyeriya ng Konteksto** at bakit ito naiiba sa prompt engineering.

• **Mga Estratehiya para sa epektibong Inhenyeriya ng Konteksto**, kabilang ang kung paano magsulat, pumili, mag-compress, at mag-isolate ng impormasyon.

• **Karaniwang Pagkabigo sa Konteksto** na maaaring makasagasa sa iyong AI agent at kung paano ito ayusin.

## Mga Layunin sa Pagkatuto

Matapos makumpleto ang araling ito, mauunawaan mo kung paano:

• **Ilarawan ang inhenyeriya ng konteksto** at pag-iba nito sa prompt engineering.

• **Kilalanin ang mga pangunahing bahagi ng konteksto** sa mga aplikasyon ng Large Language Model (LLM).

• **Ipatupad ang mga estratehiya para sa pagsusulat, pagpili, pag-compress, at pag-isolate ng konteksto** upang mapabuti ang pagganap ng agent.

• **Kilalanin ang mga karaniwang pagkabigo sa konteksto** tulad ng poisoning, distraction, confusion, at clash, at ipatupad ang mga teknik para sa paglutas nito.

## Ano ang Inhenyeriya ng Konteksto?

Para sa mga AI Agent, ang konteksto ang nagpapatakbo ng pagpaplano ng AI Agent upang isagawa ang mga tiyak na aksyon. Ang inhenyeriya ng konteksto ay ang pagsasanay upang matiyak na ang AI Agent ay may tamang impormasyon upang makumpleto ang susunod na hakbang ng gawain. May limitasyon sa laki ng konteksto na maaaring matanggap, kaya bilang mga tagagawa ng agent kailangan nating bumuo ng mga sistema at proseso para pangasiwaan ang pagdagdag, pagtanggal, at pagsasama-sama ng impormasyon sa konteksto.

### Prompt Engineering laban sa Context Engineering

Ang prompt engineering ay nakatuon sa isang set ng static na instruksyon upang epektibong gabayan ang mga AI Agent gamit ang mga patakaran. Ang inhenyeriya ng konteksto naman ay kung paano pamahalaan ang dynamic na set ng impormasyon, kabilang ang paunang prompt, upang matiyak na ang AI Agent ay may kinakailangan nito sa pagdaan ng panahon. Ang pangunahing ideya sa inhenyeriya ng konteksto ay gawing paulit-ulit at maaasahan ang prosesong ito.

### Mga Uri ng Konteksto

[![Mga Uri ng Konteksto](../../../translated_images/tl/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Mahalaga tandaan na ang konteksto ay hindi lamang iisang bagay. Ang impormasyong kailangan ng AI Agent ay maaaring manggaling sa iba't ibang pinagkukunan at nasa atin ang responsibilidad na tiyakin na may access ang agent sa mga ito:

Ang mga uri ng konteksto na maaaring kailanganin ng isang AI agent na pamahalaan ay kinabibilangan ng:

• **Instruksyon:** Ito ang mga "patakaran" ng agent – mga prompt, system message, few-shot examples (na naglalahad kung paano gagawin ng AI ang isang bagay), at mga paglalarawan ng mga kasangkapang maaaring gamitin. Dito nagsasama ang pokus ng prompt engineering at inhenyeriya ng konteksto.

• **Kaalaman:** Saklaw nito ang mga katotohanan, impormasyon mula sa mga database, o mga pangmatagalang alaala na naipon ng agent. Kasama dito ang pagsasama ng Retrieval Augmented Generation (RAG) system kung kailangan ng agent ng access sa iba't ibang tindahan ng kaalaman at database.

• **Mga Kasangkapan:** Ito ang mga depinisyon ng mga panlabas na function, APIs, at MCP Servers na maaaring tawagan ng agent, kasama ang mga feedback (mga resulta) mula sa paggamit nito.

• **Kasaysayan ng Usapan:** Ang patuloy na dayalogo sa isang user. Habang tumatagal, ang mga pag-uusap na ito ay lumalalim at nagiging mas kumplikado na nangangahulugang kumukuha ito ng puwang sa window ng konteksto.

• **Mga Kagustuhan ng User:** Impormasyon na natutunan tungkol sa mga gusto o ayaw ng user sa pagdaan ng panahon. Maaaring itago ito at tawagin sa paggawa ng mga mahahalagang desisyon upang makatulong sa user.

## Mga Estratehiya para sa Epektibong Inhenyeriya ng Konteksto

### Mga Estratehiya sa Pagpaplano

[![Pinakamahusay na Praktis sa Inhenyeriya ng Konteksto](../../../translated_images/tl/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Nagsisimula ang mahusay na inhenyeriya ng konteksto sa mahusay na pagpaplano. Narito ang isang paraan na makakatulong sa iyo upang magsimulang pag-isipan kung paano iapply ang konsepto ng inhenyeriya ng konteksto:

1. **Tukuyin ang Malinaw na Resulta** - Dapat malinaw na tukuyin ang mga resulta ng mga gawain na iaatas sa AI Agent. Sagutin ang tanong - "Ano ang magiging itsura ng mundo kapag natapos na ang AI Agent sa kanyang gawain?" Sa ibang salita, anong pagbabago, impormasyon, o tugon ang dapat matanggap ng user matapos makipag-ugnay sa AI Agent.
2. **I-map ang Konteksto** - Kapag natukoy mo na ang mga resulta ng AI Agent, kailangan mong sagutin ang tanong na "Anong impormasyon ang kailangan ng AI Agent upang makumpleto ang gawain na ito?". Sa ganitong paraan makakapagsimula kang i-map ang konteksto kung saan matatagpuan ang impormasyong iyon.
3. **Gumawa ng Mga Pipeline ng Konteksto** - Ngayon na alam mo kung saan ang impormasyon, kailangan mong sagutin ang tanong na "Paano makukuha ng Agent ang impormasyong ito?". Maaaring gawin ito sa iba't ibang paraan kabilang ang RAG, paggamit ng MCP servers at iba pang mga kasangkapan.

### Mga Praktikal na Estratehiya

Mahalaga ang pagpaplano pero kapag nagsimulang dumaloy ang impormasyon sa window ng konteksto ng ating agent, kailangan natin ng mga praktikal na estratehiya upang pamahalaan ito:

#### Pamamahala ng Konteksto

Habang ang ilang impormasyon ay awtomatikong idaragdag sa window ng konteksto, ang inhenyeriya ng konteksto ay tungkol sa pagiging mas aktibo sa pamamahala ng impormasyong ito na maaaring gawin gamit ang ilang mga estratehiya:

 1. **Agent Scratchpad**
 Pinapayagan ang AI Agent na magtala ng mga mahalagang detalye tungkol sa kasalukuyang mga gawain at pakikipag-ugnayan sa user sa loob ng isang session. Dapat ito ay nasa labas ng window ng konteksto sa isang file o runtime na bagay na maaaring kunin muli ng agent habang tumatakbo ang session kung kinakailangan.

 2. **Mga Alaala**
 Ang scratchpad ay maganda para sa pamamahala ng impormasyon sa labas ng window ng konteksto sa isang session. Pinapayagan ng mga alaala ang mga agent na itabi at bawiin ang mahalagang impormasyon sa maraming sesyon. Maaaring kabilang dito ang mga buod, mga kagustuhan ng user at feedback para sa mga pagpapabuti sa hinaharap.

 3. **Pag-compress ng Konteksto**
  Kapag lumalaki na ang window ng konteksto at papalapit na sa kanyang limitasyon, maaaring gamitin ang mga pamamaraan tulad ng pagbuod at pag-trim. Kasama dito ang pagpapanatili lamang ng pinakamahalagang impormasyon o pagtanggal ng mga lumang mensahe.
  
 4. **Mga Multi-Agent Systems**
  Ang pagbuo ng multi-agent system ay isang paraan ng inhenyeriya ng konteksto dahil bawat agent ay may sariling window ng konteksto. Kung paano ibinahagi at ipinasa ang konteksto sa iba't ibang agent ay isa pang bagay na dapat planuhin sa paggawa ng mga sistemang ito.
  
 5. **Sandbox Environments**
  Kung kailangang magpatakbo ng code ang agent o iproseso ang malaking dami ng impormasyon sa isang dokumento, maaari itong tumagal ng maraming tokens upang iproseso ang mga resulta. Sa halip na ito ay lahat ay nakaimbak sa window ng konteksto, maaaring gamitin ng agent ang isang sandbox environment na kayang patakbuhin ang code na ito at basahin lamang ang mga resulta at iba pang mahalagang impormasyon.
  
 6. **Runtime State Objects**
   Ginagawa ito sa pamamagitan ng paglikha ng mga lalagyan ng impormasyon upang pamahalaan ang mga sitwasyon kung kailangang ma-access ng Agent ang tiyak na impormasyon. Sa isang kumplikadong gawain, pinapayagan nito ang Agent na itago ang mga resulta ng bawat subtask hakbang-hakbang, na nagbibigay-daan sa konteksto na manatiling konektado lamang sa tiyak na subtask na iyon.

#### Pag-inspeksyon ng Konteksto

Matapos ilapat ang isa sa mga estratehiyang ito, mahalagang suriin kung ano talaga ang natanggap ng susunod na tawag sa modelo. Isang kapaki-pakinabang na tanong para sa pag-debug ay:

> Nag-load ba ang agent ng sobrang konteksto, maling konteksto, o may nawawalang konteksto na kailangan niya?

Hindi mo kailangang i-log ang mga raw prompt, output ng mga kasangkapan, o nilalaman ng memorya upang masagot ang tanong na iyon. Sa produksyon, mas mainam ang maliliit na rekord ng inspeksyon ng konteksto na kumukuha ng bilang, mga id, mga hash, at mga label ng patakaran:

- **Pagpili:** Subaybayan kung ilang kandidato chunk, tools, o alaala ang isinasaalang-alang, ilan ang napili, at aling patakaran o score ang nagresulta ng pagsasala sa iba.
- **Pag-compress:** Itala ang pinagmulan ng saklaw o trace id, ang summary id, tinatayang bilang ng token bago at pagkatapos ng compression, at kung ang raw na nilalaman ay isinama o hindi sa susunod na tawag.
- **Pag-isolate:** Tandaan kung aling subtask ang tumakbo sa hiwalay na agent, session, o sandbox, kung anong bounded summary ang ibinalik, at kung naka-stay sa labas ng konteksto ng parent agent ang malalaking output ng tool.
- **Memorya at RAG:** Itago ang mga retrieval document id, memory id, mga score, napiling id, at estado ng redaction sa halip na buong retrieved na teksto.
- **Kaligtasan at privacy:** Mas gusto ang mga hash, id, token buckets, at label ng patakaran kaysa sa sensitibong teksto ng prompt, argument ng tool, resulta ng tool, o katawan ng memorya ng user.

Ang layunin ay hindi upang mag-imbak ng mas maraming konteksto. Ito ay upang mag-iwan ng sapat na ebidensya upang malaman ng developer kung aling estratehiya ng konteksto ang ginamit at kung ito ay nagbago ng susunod na tawag sa modelo sa tamang paraan.

### Halimbawa ng Inhenyeriya ng Konteksto

Sabihin nating gusto nating magkaroon ng AI agent na **"Mag-book ng biyahe papuntang Paris para sa akin."**

• Isang simpleng agent na gumagamit lamang ng prompt engineering ay maaaring sumagot ng: **"Sige, kailan mo gustong pumunta sa Paris?"** Pinroseso lamang nito ang direktang tanong mo sa oras ng pagtatanong.

• Ang isang agent na gumagamit ng mga estratehiya ng inhenyeriya ng konteksto na tinatalakay ay gagawa ng mas marami pa. Bago sumagot, maaaring gawin ng kanyang sistema ang mga sumusunod:

  ◦ **Suriin ang iyong kalendaryo** para sa mga magagamit na petsa (nangongolekta ng real-time data).

 ◦ **Alalahanin ang mga huling kagustuhan sa paglalakbay** (mula sa pangmatagalang memorya) tulad ng iyong paboritong airline, badyet, o kung mas gusto mo ang direct flights.

 ◦ **Kilalanin ang mga magagamit na kasangkapan** para sa pag-book ng flight at hotel.

- Pagkatapos, isang halimbawa ng tugon ay:  "Hi [Pangalan Mo]! Nakikita kong malaya ka sa unang linggo ng Oktubre. Hahanapin ko ba ang mga direct flights papuntang Paris gamit ang [Paboritong Airline] sa karaniwang badyet mo na [Badyet]?" Ipinapakita ng mas makahulugang tugon na ito na may kamalayan sa konteksto ang inhenyeriya ng konteksto.

## Karaniwang Pagkabigo sa Konteksto

### Pagkalason ng Konteksto

**Ano ito:** Kapag pumasok sa konteksto ang isang hallucination (maling impormasyon na ginawa ng LLM) o error at paulit-ulit na binabanggit, na nagdudulot na ang agent ay maghangad ng imposibleng mga layunin o bumuo ng mga walang katuturang stratehiya.

**Ano ang gagawin:** Magpatupad ng **pagpapatunay ng konteksto** at **quarantine**. Patunayan ang impormasyon bago ito idagdag sa pangmatagalang memorya. Kung may napansing posibleng pagkalason, magsimula ng mga bagong konteksto upang pigilan ang pagkalat ng maling impormasyon.

**Halimbawa sa Pag-book ng Biyahe:** Ang iyong agent ay nagmulat ng isang **direct flight mula sa maliit na lokal na paliparan papunta sa malayong internasyonal na lungsod** na wala namang tunay na internasyonal na flight. Ang impormasyong flight na hindi totoo ay naiimbak sa konteksto. Pagkatapos, kapag humiling kang mag-book, patuloy itong naghahanap ng tiket para sa imposibleng ruta na ito, na nagdudulot ng paulit-ulit na mga error.

**Solusyon:** Magpatupad ng hakbang na **pinapatunayan ang pag-iral ng flight at mga ruta gamit ang real-time na API** _bago_ idagdag ang detalye ng flight sa working context ng agent. Kung nabigo ang pagpapatunay, ang maling impormasyon ay "kini-quarantine" at hindi na gagamitin pa.

### Pagdistract ng Konteksto

**Ano ito:** Kapag lumaki ang konteksto nang husto na masyado nang nakatuon ang modelo sa naipon na kasaysayan kaysa sa paggamit ng kanyang natutunan sa pagsasanay, na nagreresulta sa paulit-ulit o hindi kapaki-pakinabang na mga aksyon. Maaaring magsimulang magkamali ang mga modelo kahit bago pa mapuno ang konteksto.

**Ano ang gagawin:** Gamitin ang **pagbubuod ng konteksto**. Paminsan-minsang i-compress ang naipong impormasyon sa mas maiikling buod, pinananatili ang mahahalagang detalye habang tinatanggal ang sobrang kasaysayan. Nakakatulong ito upang "i-reset" ang pokus.

**Halimbawa sa Pag-book ng Biyahe:** Matagal na ninyong pinag-uusapan ang iba't ibang dream travel destinations, kabilang ang detalyadong kwento ng backpacking trip mo dalawang taon na ang nakalilipas. Nang hilingin mo sa wakas na **"maghanap ng murang flight para sa susunod na buwan,"** nabibigo ang agent dahil sa mga lumang hindi mahalagang detalye at patuloy na tinatanong tungkol sa iyong backpacking gear o mga lumang itinerary, na nagpapabaya sa iyong kasalukuyang kahilingan.

**Solusyon:** Pagkatapos ng ilang mga turn o kapag lumaki nang husto ang konteksto, dapat **ibuod ng agent ang pinaka-kamakailan at mahalagang bahagi ng pag-uusap** – nakatuon sa iyong kasalukuyang mga petsa ng paglalakbay at destinasyon – at gamitin ang pinaikling buod na ito para sa susunod na tawag sa LLM, tinatanggal ang mga hindi gaanong mahalagang usapan ng nakaraan.

### Pagkalito sa Konteksto

**Ano ito:** Kapag ang hindi kailangang konteksto, madalas sa anyo ng sobrang dami ng magagamit na kasangkapan, ay nagdudulot sa modelo na makagawa ng maling sagot o tumawag ng mga tool na hindi angkop. Mas madaling mangyari ito sa maliliit na modelo.

**Ano ang gagawin:** Magpatupad ng **pamamahala ng tool loadout** gamit ang mga teknik sa RAG. Itago ang mga paglalarawan ng tool sa isang vector database at piliin _lamang_ ang pinaka-nauugnay na mga tool para sa bawat tiyak na gawain. Ipinapakita ng pananaliksik na mas mabuting limitahan ang pagpili ng tool sa mas mababa sa 30.

**Halimbawa sa Pag-book ng Biyahe:** May access ang iyong agent sa dosenang mga kasangkapan: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations`, at iba pa. Tinanong mo, **"Ano ang pinakamagandang paraan upang maglibot sa Paris?"** Dahil sa dami ng mga tool, nalilito ang agent at sinusubukang tawagan ang `book_flight` _sa loob_ ng Paris, o `rent_car` kahit na mas gusto mo ang pampublikong transportasyon, dahil maaaring magkapatong-patong ang mga paglalarawan ng tool o hindi nito makilala ang pinakamainam na tool.

**Solusyon:** Gamitin ang **RAG sa mga paglalarawan ng tool**. Kapag tinanong mo tungkol sa paglibot sa Paris, ang sistema ay dinamiko na kukunin _lamang_ ang pinaka-nauugnay na mga tool tulad ng `rent_car` o `public_transport_info` batay sa iyong query, na nagpapakita ng nakatutok na "loadout" ng mga tool sa LLM.

### Pagkakasalungat ng Konteksto

**Ano ito:** Kapag may salungatan sa impormasyon sa konteksto, na nagdudulot ng hindi magkakatugmang pangangatwiran o maling huling sagot. Mangyayari ito kapag dumadaloy ang impormasyon ng paunti-unti, at ang mga maagang maling hinuha ay nananatili sa konteksto.

**Ano ang gagawin:** Gamitin ang **pag-puno ng konteksto** at **offloading**. Ang pruning ay ang pagtanggal ng lipas o salungat na impormasyon habang dumarating ang mga bagong detalye. Ang offloading ay nagbibigay sa modelo ng hiwalay na "scratchpad" na espasyo upang iproseso ang impormasyon nang hindi ginugulo ang pangunahing konteksto.


**Halimbawa ng Pag-book ng Biyahe:** Sa simula, sinabi mo sa iyong ahente, **"Gusto kong lumipad sa economy class."** Sa kalaunan ng pag-uusap, nagbago ang iyong isip at sinabi, **"Sa katunayan, para sa biyahe na ito, pumunta tayo sa business class."** Kung nananatili sa konteksto ang parehong mga tagubilin, maaaring makatanggap ang ahente ng magkasalungat na mga resulta ng paghahanap o malito kung alin sa mga kagustuhan ang uuna.

**Solusyon:** Ipatupad ang **context pruning**. Kapag ang bagong tagubilin ay salungat sa lumang tagubilin, ang mas dating tagubilin ay inaalis o tahasang nilalampasan sa konteksto. Bilang alternatibo, maaaring gumamit ang ahente ng **scratchpad** upang pag-isahin ang mga magkasalungat na kagustuhan bago magpasya, na tinitiyak na ang huling, pare-parehong tagubilin lamang ang gumabay sa kanyang mga aksyon.

## May Iba Ka Pang Mga Tanong Tungkol sa Context Engineering?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipagkita sa iba pang mga nag-aaral, dumalo sa mga oras ng opisina at masagot ang iyong mga tanong tungkol sa AI Agents.
## Nakaraang Aralin

[Agentic Protocols](../11-agentic-protocols/README.md)

## Susunod na Aralin

[Memory for AI Agents](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->