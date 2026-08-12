# Mga AI Agent para sa mga Baguhan - Gabay sa Pag-aaral

Gamitin ang gabay na ito bilang isang praktikal na kasama habang umuusad ka sa kurso. Ito ay
hindi nilalayong pumalit sa mga aralin. Tinutulungan ka nitong magdesisyon kung saan magsisimula, ano ang
hahanapin sa bawat aralin, at kung paano pagdugtungin ang mga ideya sa isang maliit na gumaganang agent
na demo.

Kung ito ang unang beses mong narito, magsimula sa simple:

1. Basahin ang [Pagsasaayos ng Kurso](./00-course-setup/README.md).
2. Kumpletuhin ang Mga Aralin 01-06 nang sunod-sunod.
3. Panatilihin sa isip ang isang maliit na ideya ng demo habang nag-aaral ka.
4. Pagkatapos ng bawat aralin, itanong: "Ano ang kaya na ng aking agent na hindi nito magawa
   noon?"

## Isang Simpleng Demo na Panatilihin sa Isip

Isang magandang paraan para matuto tungkol sa mga agent ay sundan ang isang ideya ng demo sa buong kurso.

Halimbawa ng demo: **isang agent na tumutulong sa kurso**.

Nagtatanong ang user:

> "Gusto kong matutunan kung paano gumagamit ang mga agent ng mga tool. Hanapin ang mga tamang aralin, ibuod kung ano
> ang dapat kong basahin muna, at bigyan ako ng isang maikling gawain para magpraktis."

Ang isang ordinaryong chatbot ay maaaring sumagot mula sa alam na nito. Mas kaya pa ng isang agent:

1. **Basahin o hanapin ang mga file ng kurso** para mahanap ang tamang mga aralin.
2. **Gamitin ang mga tool** para kunin ang mga link ng aralin, mga halimbawa, o sumusuportang materyal.
3. **Magplano** ng maikling landas ng pagkatuto sa halip na magbigay ng isang mahabang sagot.
4. **Gamitin ang konteksto** mula sa kasalukuyang usapan upang manatiling naka-focus sa layunin ng nag-aaral.

5. **Tandaan ang mga kapaki-pakinabang na kagustuhan** kung sinusuportahan ng aplikasyon ang memorya.
6. **Ipakita ang mga bakas, panipi, o tala** upang maintindihan ng user ang nangyari.
7. **Magpatupad ng mga guardrail** bago gumawa ng mapanganib na aksyon o gumamit ng sensitibong data.

Habang pinag-aaralan mo ang bawat aralin, bumalik sa demo na ito at itanong: ano ang bagong kakayahan
na maidudulot ng araling ito?

## Kung Ano ang Iyong Binubuo

Sa katapusan ng kurso, dapat mong magawang ipaliwanag at bumuo ng mga sistema ng agent
na pinagsasama ang mga bahagi na ito:

| Bahagi | Kahulugan sa karaniwang wika | Sa demo |
|------|------------------------|-------------|
| Modelo | Ang engine ng pangangatwiran na nag-iinterpret ng kahilingan ng user | Naiintindihan na gusto ng nag-aaral ang mga aralin tungkol sa paggamit ng tool |
| Mga Tool | Mga function, API, file, browser, o serbisyo na magagamit ng agent | Naghahanap sa repo o kumukuha ng nilalaman ng aralin |
| Kaalaman | Mga dokumento o datos na ginagamit bilang batayan ng sagot | Mga README file ng kurso at materyal ng aralin |
| Konteksto | Impormasyon na isinasama sa susunod na tawag ng modelo | Ang layunin ng user at mga resulta ng tool |
| Memorya | Impormasyon na iniimbak para sa paggamit sa hinaharap | Ang kagustuhan ng nag-aaral sa mga hands-on na halimbawa ng Python |
| Pagpaplano | Paghahati ng mas malaking layunin sa mas maliliit na hakbang | Maghanap ng mga aralin, ibuod ang mga ito, magmungkahi ng praktis |
| Orkestrasyon | Pag-route ng trabaho sa mga tool, hakbang, o agent | Isang planner ang tumatawag ng search tool, tapos ng summarizer |
| Tiwala | Kaligtasan, seguridad, pagsusuri, at obserbabilidad | Nagtatala ng mga tawag sa tool at nagtatanong bago ang mga apektadong aksyon |

## Mga Modelo at Tagapagbigay

Ang mga halimbawa ng code sa kurso ay gumagamit ng **Microsoft Agent Framework (MAF)** at tinatarget ang **Azure OpenAI Responses API** — ang inirerekomendang API sa hinaharap, na pinagsasama ang chat completions, pagtawag ng tool, multimodal input, at stateful conversations sa iisang API surface. Ikokonekta mo ito sa pamamagitan ng isang **Microsoft Foundry** na proyekto (gamit ang `FoundryChatClient`) o direkta sa Azure OpenAI (gamit ang `OpenAIChatClient`).

Habang tinatapos mo ang mga aralin, mayroon kang ilang mga opsiyon ng tagapagbigay:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — ang pangunahing daan na ginagamit sa mga aralin. Mag-sign in gamit ang `az login` para sa keyless Entra ID authentication.
- **Foundry Local** — patakbuhin ang mga modelo nang ganap sa device sa pamamagitan ng isang OpenAI-compatible API (walang cloud, walang API keys). Ideal para sa offline o libre na eksperimento. Tingnan ang [Pagsasaayos ng Kurso](./00-course-setup/README.md).
- **MiniMax** — isang OpenAI-compatible na tagapagbigay ng serbisyo na may malalaking-context na mga modelo, magagamit bilang isang drop-in na alternatibo.

> **Tandaan:** Ang GitHub Models ay deprecated na (magtatapos sa Hulyo 2026) at hindi sinusuportahan ang Responses API. Ang mga halimbawa ay na-update na upang gamitin ang Azure OpenAI / Microsoft Foundry bilang kapalit.

## Piliin ang Iyong Landas sa Pagkatuto

Maaari mong kunin ang buong kurso nang sunod-sunod, o tumalon sa isang landas batay sa gusto mong
buuin.

| Kung ang iyong layunin ay... | Magsimula sa | Pagkatapos pag-aralan |
|-----------------------|------------|------------|
| Maunawaan kung ano ang mga agent | 01, 02, 03 | 04, 05, 06 |
| Bumuo ng isang agent na gumagamit ng mga tool | 04 | 05, 07, 14 |
| Bumuo ng isang RAG-based na agent | 05 | 04, 06, 12 |
| Magdisenyo ng mga multi-step na workflows | 07 | 08, 09, 14 |
| Maunawaan ang mga multi-agent na sistema | 08 | 07, 09, 11 |
| Ihanda ang mga agent para sa produksyon | 06, 10 | 12, 13, 16, 18 |
| I-deploy at i-scale ang mga agent sa Foundry | 10, 16 | 06, 13, 18 |
| Bumuo ng lokal / offline-first na mga agent | 17 | 04, 05, 11 |
| Tuklasin ang mga protocol at browser automation | 11, 15 | 10, 18 |

Tip: kung bago ka sa mga agent, huwag laktawan ang Mga Aralin 01-06. Ibinibigay nila ang
bokabularyo na kakailanganin mo para sa natitirang bahagi ng kurso.

## Gabay sa Bawat Aralin

| Aralin | Ano ang matututuhan mo | Subukan ito pagkatapos ng aralin |
|--------|----------------|---------------------------|
| [01 - Panimula sa AI Agents](./01-intro-to-ai-agents/README.md) | Ano ang pinagkaiba ng agent sa isang simpleng chatbot. | Ipalinaw ang ideya ng iyong demo bilang isang agent, hindi lamang isang chat app. |
| [02 - Agentic Frameworks](./02-explore-agentic-frameworks/README.md) | Paano tumutulong ang mga framework sa mga modelo, tool, estado, at workflow. | Tukuyin kung aling bahagi ng iyong demo ang pamamahalaan ng framework. |
| [03 - Agentic Design Patterns](./03-agentic-design-patterns/README.md) | Mga karaniwang pattern para sa disenyo ng ugali ng agent. | Gumuhit ng user journey bago magsulat ng code. |
| [04 - Paggamit ng Tool](./04-tool-use/README.md) | Paano tinatawag ng mga agent ang mga tool para kumuha ng data o gumawa ng aksyon. | Tukuyin ang isang tool na kakailanganin ng demo agent mo. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Paano ginagamitan ng retrieval upang i-ground ang mga sagot ng agent sa mga dokumento o data. | Magpasya kung anong source ng kaalaman ang dapat hanapin ng demo mo. |

| [06 - Mapagkakatiwalaang mga Ahente](./06-building-trustworthy-agents/README.md) | Paano magdagdag ng mga guardrail, pangangasiwa, at mas ligtas na kilos. | Magdagdag ng isang panuntunan kung kailan dapat muna tanungin ng ahente ang gumagamit. |
| [07 - Disenyo ng Pagpaplano](./07-planning-design/README.md) | Paano hinahati ng mga ahente ang mas malalaking layunin sa mas maliliit na hakbang. | Sumulat ng tatlong-hakbang na plano para sa iyong demo na kahilingan. |
| [08 - Disenyo ng Multi-Ahente](./08-multi-agent/README.md) | Kailan hahatiin ang trabaho sa mga dalubhasang ahente. | Magpasya kung ang iyong demo ay nangangailangan ng isang ahente o ilan. |
| [09 - Metakognisyon](./09-metacognition/README.md) | Paano nire-review at pinapabuti ng mga ahente ang kanilang sariling output. | Magdagdag ng panghuling self-check bago tumugon ang ahente. |
| [10 - Mga AI na Ahente sa Produksiyon](./10-ai-agents-production/README.md) | Ano ang nagbabago kapag ang ahente ay lumipat mula demo patungong produksyon. | Ilahad kung ano ang iyong imo-monitor: kalidad, gastos, latency, mga pagkabigo. |
| [11 - Mga Agentic Protocol](./11-agentic-protocols/README.md) | Paano nag-uugnay ang mga protocol ng ahente sa mga tool at iba pang mga ahente. | Tukuyin kung saan maaaring mapadali ng isang standard protocol ang integrasyon. |
| [12 - Pag-engineer ng Konteksto](./12-context-engineering/README.md) | Paano pumili, mag-trim, mag-isolate, at mag-manage ng konteksto. | Magpasya kung ano ang dapat ilagay sa prompt at ano ang dapat iwan sa labas. |
| [13 - Memorya ng Ahente](./13-agent-memory/README.md) | Paano maaaring mag-save ng kapaki-pakinabang na impormasyon ang mga ahente sa mga interaksyon. | Pumili ng isang ligtas na preference na maaaring tandaan ng iyong demo. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Mga tukoy na building block ng framework para sa mga ahente at workflows, pati na rin ang pagho-host ng LangChain/LangGraph na mga ahente sa Microsoft Foundry. | I-map ang mga hakbang ng iyong demo sa mga konsepto ng framework. |
| [15 - Mga Ahenteng Ginagamit sa Computer](./15-browser-use/README.md) | Paano makikipag-interact ang mga ahente sa browser o UI surfaces, kasama na ang mga totoong halimbawa tulad ng Microsoft Project Opal. | Piliin ang isang gawain sa browser na dapat ay kailangan pa rin ng kumpirmasyon ng gumagamit. |
| [16 - Pag-deploy ng Scalable na mga Ahente](./16-deploying-scalable-agents/README.md) | Paano dalhin ang ahente mula prototype patungong scalable, observable production deployment sa Microsoft Foundry (hosted agents, model routing, caching, evaluation gates, smoke tests). | Ilahad ang mga alalahanin sa produksyon na kailangan pa ng iyong demo: hosting, routing, gastos, pagsusuri. |
| [17 - Paglikha ng Lokal na AI na mga Ahente](./17-creating-local-ai-agents/README.md) | Paano gumawa ng local-first na mga ahente na tumatakbo nang buong-buo sa iyong makina gamit ang Foundry Local at Qwen (local tools, local RAG, local MCP). | Magpasya kung aling bahagi ng iyong demo ang dapat manatiling pribado at tumakbo nang lokal. |
| [18 - Pag-secure sa mga AI na Ahente](./18-securing-ai-agents/README.md) | Paano gawing mas auditable at tamper-evident ang mga aksyon ng ahente. | Magpasya kung anong mga aksyon sa iyong demo ang dapat i-log o lagyan ng resibo. |

## Pagpapatunay ng Mga Na-deploy na Ahente gamit ang Smoke Tests

Kapag nag-deploy ka ng ahente (Lesson 16), isang **smoke test** ang pinakamurang unang
tseke na ang deployment ay talagang sumasagot. Ang repo na ito ay may kasamang
mga handang patakbuhin na katalogo sa [tests/](./tests/README.md) para sa mga
deployable na ahente sa Mga Lessons 01, 04, 05, at 16, nakakonekta sa
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Action. Patakbuhin ito mula sa **Actions** tab pagkatapos i-deploy ang ahente ng lesson.
Ang smoke tests ay unang tarangkahan — offline at online na pagsusuri (Lessons 10 at 16)
ang nagsasabi sa'yo kung gaano *kahusay* ang ahente.

## Mga Pangunahing Ideya sa Termino na Pwede sa Baguhan

### Mga Tool

Ang tool ay isang bagay na maaaring tawagin ng ahente upang gawin ang trabaho sa labas ng modelo. Ang isang
magandang tool ay may malinaw na pangalan, makitid na gawain, typed na mga input, predictable na output,
at ligtas na paraan upang mabigo.

Para sa course helper demo, isang tool ay maaaring:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG at Kaalaman

Tinutulungan ng RAG ang ahente na sumagot mula sa source material sa halip na manghula. Sa
kursong ito, ang source material ay maaaring mga lesson README, code samples, o mga panlabas na
resources na naka-link mula sa mga lesson.

Gamitin ang RAG kapag ang sagot ay dapat naka-ugat sa mga dokumento, datos, o kasalukuyang
mga file ng proyekto.

### Pagpaplano

Kapaki-pakinabang ang pagpaplano kapag ang kahilingan ay may higit sa isang hakbang. Panatilihing maikli at
sapat na nakikita ang mga plano para masuri ng developer o gumagamit.

Para sa demo, ang plano ay maaaring:

1. Hanapin ang mga lesson na may kaugnayan sa paggamit ng tool.
2. Ibuod ang mga pinaka-nauugnay na lesson.
3. Magrekomenda ng isang practice task.

### Konteksto

Ang konteksto ay kung ano ang nakikita ng modelo ngayon. Ang kakulangan ng konteksto ay maaaring
magpahuli sa ahente sa mahahalagang detalye. Ang sobrang konteksto ay maaaring magpabagal,
magpataas ng gastos, o magpahirap na malito ang ahente.

Ang magandang pag-engineer ng konteksto ay nangangahulugang pagpili ng tamang impormasyon para sa susunod na
tawag ng modelo.

### Memorya

Ang memorya ay impormasyong iniimbak para sa susunod. Huwag i-save ang lahat. I-save lamang ang impormasyon
kung ito ay kapaki-pakinabang, ligtas, at madaling i-update o tanggalin.

Halimbawa, ang pag-alala na "mas gusto ng learner ang mga halimbawa ng Python" ay maaaring kapaki-pakinabang.
Ang pag-alala ng sensitibong personal na data ay karaniwang hindi.

### Pagsusuri at Observability

Ang pagsusuri ay nagtatanong: ginawa ba ng ahente ang tamang bagay?

Ang observability ay nagtatanong: nakikita ba natin kung paano ito nangyari?

Para sa mga production na ahente, subaybayan ang mga tawag sa modelo, tawag sa tool, nakuha na konteksto,
latency, gastos, mga pagkabigo, at feedback ng gumagamit.

### Tiwala at Seguridad

Ang mga mapagkakatiwalaang ahente ay nangangailangan ng higit pa sa isang kapaki-pakinabang na prompt. Gumamit ng mga tool na least-privilege,
human approval para sa mataas na-impact na aksyon, pag-redact ng data kung saan kinakailangan, at mga log o
resibo para sa mga aksyon na kailangang ma-audit.

## Isang 15-Minuto na Review Routine

Gamitin ang routine na ito pagkatapos ng bawat lesson:

1. **Ibuod ang lesson sa isang pangungusap.**
2. **Pangalanan ang bagong kakayahan ng ahente.** Halimbawa: paggamit ng tool, retrieval,
   pagpaplano, memorya, observability, o seguridad.
3. **Idagdag ito sa course helper demo.** Ano ang nagbago sa demo ngayon?
4. **Hanapin ang panganib.** Ano ang maaaring pumalya kung mali ang paggamit sa kakayahang ito?
5. **Sumulat ng isang tanong sa pagsubok.** Paano mo susuriin kung maayos ang pag-uugali ng ahente?

## Mabilis na Self-Check

Bago magpatuloy, subukang sagutin ang mga tanong na ito:

1. Ano ang kaya ng isang ahente na hindi kayang gawin ng isang regular na chatbot mag-isa?
2. Anong tool ang unang kailangan ng iyong ahente, at bakit?
3. Anong pinagkukunan ng kaalaman ang dapat pag-ugatan ng sagot ng ahente?
4. Anong konteksto ang dapat isama sa susunod na tawag ng modelo?

5. Ano ang dapat tandaan ng ahente, at ano ang dapat nitong iwasang itabi?
6. Kailan dapat humingi ng pahintulot mula sa tao ang ahente?
7. Anong mga tala, bakas, o resibo ang makakatulong sa iyo upang i-debug o suriin ang ahente sa kalaunan?


## Inirekomendang Pagsasanay na Capstone

Sa pagtatapos ng kurso, bumuo ng isang maliit na ahente na tutulong sa isang tagapag-aral na mag-navigate sa
repositoryong ito.

Minimum na bersyon:

- Tanggapin ang isang paksa mula sa gumagamit.
- Hanapin ang pinaka-makabuluhang mga leksyon.
- Ibuod kung ano ang dapat basahin muna.
- Magmungkahi ng isang gawaing praktikal.
- Ipakita kung aling mga file ng leksyon o mga link ang ginamit.

Pinalawak na bersyon:

- Tandaan ang paboritong programming language ng tagapag-aral.
- Gumamit ng isang simpleng plano bago sumagot.
- Magdagdag ng sariling pagsusuri bago ang panghuling sagot.
- I-log ang mga tawag sa tool at mga nakuha na pinagmulan.
- Humingi ng kumpirmasyon bago buksan ang browser o mga UI automation na gawain.

Ito ay nagbibigay sa iyo ng isang maliit ngunit makatotohanang paraan upang magpraktis ng mga tool, RAG, pagpaplano,
konteksto, memorya, obserbabilidad, at pagtitiwala sa isang proyekto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->