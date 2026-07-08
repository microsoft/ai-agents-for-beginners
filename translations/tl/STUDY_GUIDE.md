# Mga AI Agent para sa mga Baguhan - Gabay sa Pag-aaral

Gamitin ang gabay na ito bilang isang praktikal na kasamahan habang dumadaan ka sa kurso. Ito ay
hindi nilalayong palitan ang mga aralin. Tinutulungan ka nitong magpasya kung saan magsisimula, ano ang
dapat hanapin sa bawat aralin, at kung paano iugnay ang mga ideya sa isang maliit na gumaganang demo ng agent
.

Kung ito ang iyong unang beses dito, magsimula sa simple:

1. Basahin ang [Course Setup](./00-course-setup/README.md).
2. Kumpletuhin ang Mga Aralin 01-06 nang sunud-sunod.
3. Magkaroon ng isang maliit na ideya ng demo habang nag-aaral ka.
4. Pagkatapos ng bawat aralin, itanong: "Ano ang kaya na ng aking agent na hindi nito magawa
   noon?"

## Isang Simpleng Demo na Dapat Tandaan

Isang magandang paraan upang matuto tungkol sa mga agent ay sundan ang isang ideya ng demo sa buong kurso.

Halimbawa ng demo: **isang course helper agent**.

Ang user ay nagtatanong:

> "Gusto kong matutunan kung paano gumamit ang mga agent ng mga tool. Hanapin ang tamang mga aralin, ibuod kung ano
> ang dapat kong basahin muna, at bigyan ako ng isang maikling gawain para sa pagsasanay."

Ang isang karaniwang chatbot ay maaaring sumagot base sa alam na nito. Pero ang isang agent ay kaya pang gumawa ng higit pa:

1. **Basahin o hanapin sa mga file ng kurso** upang mahanap ang tamang mga aralin.
2. **Gamitin ang mga tool** upang makuha ang mga link ng aralin, mga halimbawa, o mga karagdagang materyal.
3. **Magplano** ng isang maikling landas ng pag-aaral sa halip na magbigay ng iisang mahabang sagot.
4. **Gamitin ang konteksto** mula sa kasalukuyang usapan upang manatiling nakatuon sa layunin ng nag-aaral.

5. **Tandaan ang mga kapaki-pakinabang na kagustuhan** kung sinusuportahan ng aplikasyon ang memorya.
6. **Ipakita ang mga bakas, sipi, o tala** upang maunawaan ng user kung ano ang nangyari.
7. **Magpatupad ng mga guardrails** bago gumawa ng mga mapanganib na aksyon o gumamit ng sensitibong data.

Habang pinag-aaralan mo ang bawat aralin, bumalik dito sa demo at itanong: anong bagong kakayahan ang
maidaragdag ng araling ito?

## Kung Ano ang Inyong Binubuo

Sa pagtatapos ng kurso, dapat mong maipaliwanag at mabuo ang mga sistema ng agent
na pinagsasama ang mga sumusunod na bahagi:

| Bahagi | Kahulugan sa simpleng salita | Sa demo |
|------|------------------------|-------------|
| Modelo | Ang makina ng pangangatwiran na nagsasalin ng hiling ng user | Naiintindihan na nais ng nag-aaral ang mga aralin tungkol sa paggamit ng tool |
| Mga Tool | Mga function, API, file, browser, o serbisyo na magagamit ng agent | Naghahanap sa repo o kumukuha ng nilalaman ng aralin |
| Kaalaman | Mga dokumento o datos na ginagamit upang patatagin ang sagot | Mga README na file ng Kurso at materyal ng aralin |
| Konteksto | Impormasyon na isinama sa susunod na pagtawag sa modelo | Ang layunin ng user at mga resulta ng tool |
| Memorya | Impormasyon na iniimbak para sa paggamit sa hinaharap | Nais ng nag-aaral na hands-on na mga halimbawa ng Python |
| Pagpaplano | Paghati-hati ng mas malaking layunin sa mga maliliit na hakbang | Hanapin ang mga aralin, ibuod ang mga ito, magmungkahi ng praktis |
| Organisasyon | Pamamahagi ng trabaho sa mga tool, hakbang, o mga agent | Isang planner ang tumatawag ng search tool, tapos summarizer |
| Tiwala | Kaligtasan, seguridad, ebalwasyon, at pagiging nasusubaybayan | Nagtatala ng mga tawag sa tool at nagtatanong bago gumawa ng mataas na epekto na mga aksyon |

## Mga Modelo at Provider

Ang mga sample code ng kurso ay gumagamit ng **Microsoft Agent Framework (MAF)** at nakatuon sa **Azure OpenAI Responses API** — ang inirerekomendang API sa hinaharap, na pinagsasama ang chat completions, tool calling, multimodal input, at mga stateful na usapan sa isang API surface. Ikokonekta mo ito alinman sa pamamagitan ng isang **Microsoft Foundry** na proyekto (gamit ang `FoundryChatClient`) o direkta sa Azure OpenAI (gamit ang `OpenAIChatClient`).


Habang nag-aaral ka sa mga aralin, may ilang pagpipilian ka para sa provider:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — ang pangunahing paraan na ginagamit sa mga aralin. Mag-sign in gamit ang `az login` para sa keyless Entra ID authentication.
- **Foundry Local** — patakbuhin ang mga modelo nang buong-on-device sa pamamagitan ng OpenAI-compatible API (walang cloud, walang API keys). Mainam para sa offline o walang gastos na eksperimento. Tingnan ang [Course Setup](./00-course-setup/README.md).
- **MiniMax** — isang OpenAI-compatible na provider na may malalaking-context na modelo, magagamit bilang drop-in na alternatibo.

> **Tandaan:** Ang GitHub Models ay deprecated na (magmamana sa Hulyo 2026) at hindi sumusuporta sa Responses API. Ang mga halimbawa ay na-update na upang gamitin ang Azure OpenAI / Microsoft Foundry.

## Piliin ang Iyong Landas sa Pag-aaral

Maaari mong kunin ang buong kurso nang sunud-sunod, o tumalon sa isang landas batay sa gusto mong
buuin.

| Kung ang layunin mo ay... | Simulan sa | Pag-aralan pagkatapos |
|-----------------------|------------|------------|
| Maunawaan kung ano ang mga ahente | 01, 02, 03 | 04, 05, 06 |
| Bumuo ng isang ahente na gumagamit ng mga tool | 04 | 05, 07, 14 |
| Bumuo ng RAG-based na ahente | 05 | 04, 06, 12 |
| Magdisenyo ng multi-step na mga workflow | 07 | 08, 09, 14 |
| Maunawaan ang multi-agent systems | 08 | 07, 09, 11 |
| Ihanda ang mga ahente para sa produksyon | 06, 10 | 12, 13, 18 |
| Tuklasin ang mga protocol at browser automation | 11, 15 | 10, 18 |

Tip: kung bago ka sa mga ahente, huwag laktawan ang Aralin 01-06. Binibigyan ka nito ng
bokabularyo na kakailanganin mo sa natitirang kurso.

## Gabay sa Bawat Aralin

| Aralin | Ano ang iyong matututunan | Subukan ito pagkatapos ng aralin |
|--------|----------------|---------------------------|
| [01 - Panimula sa AI Agents](./01-intro-to-ai-agents/README.md) | Ano ang pinagkaiba ng isang ahente sa isang simpleng chatbot. | Ipaliwanag ang iyong ideya para sa demo bilang isang ahente, hindi lang isang chat app. |
| [02 - Agentic Frameworks](./02-explore-agentic-frameworks/README.md) | Paano nakakatulong ang mga framework sa mga modelo, tools, estado, at workflows. | Tukuyin kung aling bahagi ng iyong demo ang pamamahalaan ng framework. |
| [03 - Agentic Design Patterns](./03-agentic-design-patterns/README.md) | Karaniwang mga pattern para sa pagdisenyo ng asal ng ahente. | Gumuhit ng user journey bago magsulat ng code. |
| [04 - Tool Use](./04-tool-use/README.md) | Paano tumatawag ang mga ahente ng mga tool para kumuha ng datos o gumawa ng aksyon. | Tukuyin ang isang tool na kakailanganin ng iyong demo agent. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Paano ginagamit ang retrieval upang patotohanan ang mga sagot ng ahente gamit ang mga dokumento o datos. | Pumili ng pinagmumulan ng kaalaman na dapat hanapin ng iyong demo. |
| [06 - Trustworthy Agents](./06-building-trustworthy-agents/README.md) | Paano magdagdag ng mga guardrail, oversight, at mas ligtas na asal. | Magdagdag ng isang patakaran kung kailan dapat munang tanungin ng ahente ang user. |

| [07 - Planning Design](./07-planning-design/README.md) | Paano hinahati ng mga ahente ang mas malalaking layunin sa mas maliliit na hakbang. | Gumawa ng tatlong-hakbang na plano para sa iyong kahilingan para sa demo. |

| [08 - Multi-Agent Design](./08-multi-agent/README.md) | Kailan hatiin ang trabaho sa iba’t ibang dalubhasang ahente. | Magpasya kung ang iyong demo ay nangangailangan ng isang ahente o ilan pa. |
| [09 - Metacognition](./09-metacognition/README.md) | Paano sinusuri at pinapabuti ng mga ahente ang kanilang sariling output. | Magdagdag ng huling self-check bago sumagot ang ahente. |
| [10 - AI Agents in Production](./10-ai-agents-production/README.md) | Ano ang nagbabago kapag ang isang ahente ay lumipat mula demo patungo sa produksyon. | Ilista kung ano ang iyong imo-monitor: kalidad, gastos, latency, pagkabigo. |
| [11 - Agentic Protocols](./11-agentic-protocols/README.md) | Paano ikinakabit ng mga protocol ang mga ahente sa mga kasangkapan at ibang mga ahente. | Tukuyin kung saan maaaring mapadali ng isang standard protocol ang integrasyon. |
| [12 - Context Engineering](./12-context-engineering/README.md) | Paano pumili, mag-trim, mag-isa, at pamahalaan ang konteksto. | Magpasya kung ano ang dapat isama sa prompt at ano ang dapat iwan sa labas. |
| [13 - Agent Memory](./13-agent-memory/README.md) | Paano makakatipid ang mga ahente ng mahalagang impormasyon sa mga interaksyon. | Pumili ng isang ligtas na preference na maaaring tandaan ng iyong demo. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Mga partikular na block sa framework para sa mga ahente at workflows, pati na rin ang pagho-host ng LangChain/LangGraph na mga ahente sa Microsoft Foundry. | Ipara ang mga hakbang ng demo sa mga konsepto ng framework. |
| [15 - Computer Use Agents](./15-browser-use/README.md) | Paano makikipag-ugnayan ang mga ahente sa browser o UI surfaces, kasama ang mga totoong halimbawa tulad ng Microsoft Project Opal. | Pumili ng isang gawain sa browser na dapat pa ring mangailangan ng kumpirmasyon ng gumagamit. |
| [18 - Securing AI Agents](./18-securing-ai-agents/README.md) | Paano gawing mas ma-audit at tamper-evident ang mga aksyon ng ahente. | Magpasya kung anong mga aksyon sa iyong demo ang dapat i-log o lagyan ng resibo. |

Ang mga Leksyon 16 at 17 ay nakalista sa pangunahing README bilang paparating. Idagdag ito sa iyong
plano sa pag-aaral kapag available na ang laman ng leksyon.

## Mga Pangunahing Ideya sa Madaling Unawain na Paraan

### Mga Kasangkapan

Ang kasangkapan ay isang bagay na maaaring tawagin ng ahente upang gawin ang trabaho sa labas ng modelo. Ang magandang kasangkapan
ay may malinaw na pangalan, tiyak na gawain, typed na input, predictable na output, at ligtas na paraan
para mabigo.

Para sa course helper demo, ang isang kasangkapan ay maaaring:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG at Kaalaman

Tinutulungan ng RAG ang ahente na sumagot mula sa mga pinagkuhanang materyales sa halip na manghula. Sa
kursong ito, ang pinagkuhanang materyales ay maaaring mga lesson README, mga halimbawa ng code, o panlabas na
mga resources na naka-link mula sa mga leksyon.

Gamitin ang RAG kapag ang sagot ay dapat naka-base sa mga dokumento, data, o kasalukuyang
mga file ng proyekto.

### Pagpaplano

Kapaki-pakinabang ang pagpaplano kapag ang kahilingan ay may higit sa isang hakbang. Panatilihing maikli ang mga plano at
sapat na nakikita upang masuri ng developer o ng gumagamit.

Para sa demo, ang isang plano ay maaaring:

1. Hanapin ang mga leksyon na may kaugnayan sa paggamit ng kasangkapan.
2. Buodin ang pinaka-nauugnay na mga leksyon.
3. Irekomenda ang isang gawain sa pagsasanay.

### Konteksto

Ang konteksto ay ang nakikita ng modelo ngayon. Kapag kulang ang konteksto, maaaring
hindi makuha ng ahente ang mahalagang detalye. Kapag sobra naman, maaaring maging mabagal,
mas mahal, o madaling malito ang ahente.

Ang magandang context engineering ay nangangahulugan ng pagpili ng tamang impormasyon para sa susunod na modelo

tawag.

### Memorya

Ang memorya ay impormasyon na iniimbak para sa kalaunan. Huwag i-save ang lahat. I-save ang impormasyon
lamang kapag ito ay kapaki-pakinabang, ligtas, at madaling i-update o burahin.

Halimbawa, maaaring maging kapaki-pakinabang ang pag-alala na "mas gusto ng nag-aaral ang mga halimbawa sa Python."
Karaniwang hindi kapaki-pakinabang ang pag-alala ng sensitibong personal na datos.

### Pagsusuri at Kakayahang Masubaybayan

Nagtatanong ang pagsusuri: nagawa ba ng ahente ang tamang bagay?

Nagtatanong ang kakayahang masubaybayan: nakikita ba natin kung paano ito nangyari?

Para sa mga production agents, subaybayan ang mga pagtawag sa modelo, paggamit ng tool, nakuha na konteksto,
pagkaantala, gastos, pagkabigo, at feedback ng gumagamit.

### Tiwala at Seguridad

Nangangailangan ang mga pinagkakatiwalaang ahente ng higit pa sa isang kapaki-pakinabang na prompt. Gumamit ng mga tool na may pinakamababang pribilehiyo,
aprubasyon ng tao para sa mga aksyon na may malaking epekto, pag-redact ng datos kung kinakailangan, at mga log o
resibo para sa mga aksyong kailangang suriin.

## Isang 15-Minutong Rutin ng Pagsusuri

Gamitin ang rutin na ito pagkatapos ng bawat aralin:

1. **Ibuod ang aralin sa isang pangungusap.**
2. **Pangalanan ang bagong kakayahan ng ahente.** Halimbawa: paggamit ng tool, retrieval,
   pagplano, memorya, kakayahang masubaybayan, o seguridad.
3. **Idagdag ito sa course helper demo.** Ano ang nagbago sa demo ngayon?
4. **Hanapin ang panganib.** Ano ang maaaring magkamali kung mali ang paggamit ng kakayahan na ito?
5. **Sumulat ng isang tanong para sa pagsusuri.** Paano mo susuriin na tama ang pag-uugali ng ahente?

## Mabilis na Self-Check

Bago magpatuloy, subukang sagutin ang mga tanong na ito:

1. Ano ang magagawa ng isang ahente na hindi kayang gawin ng karaniwang chatbot nang mag-isa?
2. Anong tool ang unang kakailanganin ng iyong ahente, at bakit?
3. Anong pinagkunang kaalaman ang dapat magsilbing batayan ng sagot ng ahente?
4. Anong konteksto ang dapat isama sa susunod na pagtawag sa modelo?
5. Ano ang dapat alalahanin ng ahente, at ano ang dapat iwasang iimbak?
6. Kailan dapat humingi ng aprubasyon mula sa tao ang ahente?
7. Anong mga log, bakas, o resibo ang makakatulong sa iyong mag-debug o magsuri ng ahente sa hinaharap?

## Inirekomendang Ehersisyong Capstone

Sa katapusan ng kurso, gumawa ng maliit na ahente na tumutulong sa nag-aaral na mag-navigate sa
repositoryong ito.

Minimum na bersyon:

- Tumanggap ng paksa mula sa gumagamit.
- Hanapin ang mga pinaka-relebanteng aralin.
- Ibuod kung ano ang unang dapat basahin.
- Magmungkahi ng isang praktikal na gawain.
- Ipakita kung aling mga file ng aralin o link ang ginamit.

Pinalawak na bersyon:

- Alalahanin ang nais na programming language ng nag-aaral.
- Gumamit ng simpleng plano bago sumagot.
- Magdagdag ng step ng self-check bago ang panghuling sagot.
- Itala ang mga pagtawag sa tool at nakuha na mga pinagmulan.
- Humingi ng kumpirmasyon bago magbukas ng browser o mga UI automation na gawain.

Binibigyan ka nito ng maliit ngunit makatotohanang paraan upang magsanay ng mga tool, RAG, pagplano,
konteksto, memorya, kakayahang masubaybayan, at tiwala sa iisang proyekto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->