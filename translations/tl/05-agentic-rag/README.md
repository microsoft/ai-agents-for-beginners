[![Agentic RAG](../../../translated_images/tl/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

# Agentic RAG

Ang araling ito ay nagbibigay ng komprehensibong pangkalahatang-ideya ng Agentic Retrieval-Augmented Generation (Agentic RAG), isang umuusbong na paradigma ng AI kung saan ang malalaking modelo ng wika (LLMs) ay awtonomong nagpaplano ng kanilang mga susunod na hakbang habang kumukuha ng impormasyon mula sa mga panlabas na pinagmulan. Hindi tulad ng mga static na retrieval-then-read na pattern, ang Agentic RAG ay kinapapalooban ng paulit-ulit na pagtawag sa LLM, na sinusundan ng mga pagtawag sa tool o function at mga istrukturadong output. Sinusuri ng sistema ang mga resulta, pinipino ang mga query, tinatawagan ang karagdagang mga tool kung kinakailangan, at ipinagpapatuloy ang siklong ito hanggang makamit ang kasiya-siyang solusyon.

## Panimula

Tatalakayin sa araling ito

- **Unawain ang Agentic RAG:** Alamin ang tungkol sa umuusbong na paradigma sa AI kung saan ang malalaking modelo ng wika (LLMs) ay awtonomong nagpaplano ng kanilang mga susunod na hakbang habang kumukuha ng impormasyon mula sa mga panlabas na pinanggagalingan ng data.
- **Maunawaan ang Iterative Maker-Checker Style:** Intindihin ang siklo ng paulit-ulit na pagtawag sa LLM, na sinasabayan ng pagtawag sa mga tool o function at mga istrukturadong output, na dinisenyo upang mapabuti ang katumpakan at malutas ang mga maling pormang query.
- **Suriin ang Praktikal na Mga Aplikasyon:** Tukuyin ang mga senaryo kung saan namumukod-tangi ang Agentic RAG, tulad ng sa mga kapaligirang nakatutok sa katumpakan, kumplikadong pakikipag-ugnayan sa database, at pinalawig na mga workflow.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano/unawain:

- **Pag-unawa sa Agentic RAG:** Alamin ang tungkol sa umuusbong na paradigma sa AI kung saan ang malalaking modelo ng wika (LLMs) ay awtonomong nagpaplano ng kanilang mga susunod na hakbang habang kumukuha ng impormasyon mula sa mga panlabas na pinanggagalingan ng data.
- **Iterative Maker-Checker Style:** Maunawaan ang konsepto ng siklo ng paulit-ulit na pagtawag sa LLM, na sinasabayan ng pagtawag sa mga tool o function at mga istrukturadong output, na dinisenyo upang mapabuti ang katumpakan at malutas ang mga maling pormang query.
- **Pagmamay-ari sa Proseso ng Pangangatwiran:** Intindihin ang kakayahan ng sistema na pagmay-ari ang sariling proseso ng pangangatwiran, gumagawa ng mga desisyon kung paano lalapitan ang mga problema nang hindi umaasa sa mga pre-defined na landas.
- **Workflow:** Unawain kung paano ang isang agentic na modelo ay malayang nagpapasya na kumuha ng mga ulat ng trend sa merkado, tukuyin ang data ng mga kakumpitensya, iugnay ang mga internal na sukatan ng benta, sintetisahin ang mga natuklasan, at suriin ang estratehiya.
- **Iterative Loops, Integrasyon ng Tool, at Memorya:** Matutunan ang tungkol sa pagtitiwala ng sistema sa pattern ng paulit-ulit na interaksyon, pagpapanatili ng estado at memorya sa mga hakbang upang maiwasan ang paulit-ulit na mga loop at makabuo ng mas mahusay na mga desisyon.
- **Pagharap sa Mga Failure Modes at Sariling Pagwawasto:** Siyasatin ang matatag na mekanismo ng sariling pagwawasto ng sistema, kabilang na ang pag-ulit at muling pagtatanong, paggamit ng mga diagnostic tool, at pag-sandalan sa pangangasiwa ng tao.
- **Mga Hangganan ng Ahensya:** Unawain ang mga limitasyon ng Agentic RAG, na nakatuon sa domain-specific na awtonomiya, depende sa imprastruktura, at paggalang sa mga guardrails.
- **Praktikal na Paggamit at Halaga:** Tukuyin ang mga senaryo kung saan namumukod-tangi ang Agentic RAG, tulad ng mga kapaligirang nakatuon sa katumpakan, kumplikadong pakikipag-ugnayan sa database, at pinalawig na mga workflow.
- **Pamamahala, Transparency, at Tiwala:** Alamin ang kahalagahan ng pamamahala at transparency, kabilang ang explainable reasoning, kontrol sa bias, at pangangasiwa ng tao.

## Ano ang Agentic RAG?

Ang Agentic Retrieval-Augmented Generation (Agentic RAG) ay isang umuusbong na paradigma ng AI kung saan ang malalaking modelo ng wika (LLMs) ay awtonomong nagpaplano ng kanilang mga susunod na hakbang habang kumukuha ng impormasyon mula sa mga panlabas na pinanggagalingan. Hindi tulad ng mga static na retrieval-then-read na pattern, ang Agentic RAG ay kinapapalooban ng paulit-ulit na pagtawag sa LLM, na sinasabayan ng mga pagtawag sa tool o function at mga istrukturadong output. Sinusuri ng sistema ang mga resulta, pinipino ang mga query, tinatawagan ang karagdagang mga tool kung kinakailangan, at ipinagpapatuloy ang siklong ito hanggang makamit ang kasiya-siyang solusyon. Ang paulit-ulit na istilong “maker-checker” na ito ay nagpapabuti sa katumpakan, nilulutas ang mga maling pormang query, at tinitiyak ang mataas na kalidad ng mga resulta.

Aktibong pagmamay-ari ng sistema ang proseso ng pangangatwiran nito, nire-rewrite ang mga nabigong query, pumipili ng iba't ibang mga paraan ng retrieval, at nagsasama ng maraming mga tool—tulad ng vector search sa Azure AI Search, mga SQL database, o mga custom na API—bago tuluyang ibigay ang sagot. Ang natatanging katangian ng isang agentic na sistema ay ang kakayahan nitong pagmay-ari ang proseso ng pangangatwiran nito. Ang tradisyunal na mga implementasyon ng RAG ay umaasa sa mga pre-defined na landas, ngunit ang agentic na sistema ay awtonomong tumutukoy ng pagkakasunod-sunod ng mga hakbang batay sa kalidad ng impormasyong natagpuan nito.

## Pagbibigay-Kahulugan sa Agentic Retrieval-Augmented Generation (Agentic RAG)

Ang Agentic Retrieval-Augmented Generation (Agentic RAG) ay isang umuusbong na paradigma sa pag-unlad ng AI kung saan hindi lamang kumukuha ng impormasyon mula sa mga panlabas na pinanggagalingan ng data ang mga LLM kundi awtonomong nagpaplano rin ng kanilang mga susunod na hakbang. Hindi tulad ng mga static retrieval-then-read na pattern o maingat na naka-script na mga prompt sequence, ang Agentic RAG ay kinapapalooban ng isang loop ng paulit-ulit na pagtawag sa LLM, na sinasabayan ng mga pagtawag sa tool o function at mga istrukturadong output. Sa bawat hakbang, sinusuri ng sistema ang mga resulta na nakuha nito, nagpapasya kung pipinohin ang mga query, tinatawagan ang karagdagang mga tool kung kinakailangan, at ipinagpapatuloy ang siklong ito hanggang makamit ang kasiya-siyang solusyon.

Ang paulit-ulit na istilong “maker-checker” ng operasyon ay dinisenyo upang mapabuti ang katumpakan, malutas ang mga maling pormang query sa mga istrukturadong database (hal. NL2SQL), at matiyak ang balanseng, mataas na kalidad na mga resulta. Sa halip na umaasa lamang sa mga maingat na inhenyeriyang mga chain ng prompt, aktibong pagmamay-ari ng sistema ang proseso ng pangangatwiran nito. Kaya nitong i-rewrite ang mga query na pumalpak, pumili ng ibang mga pamamaraan ng retrieval, at pagsamahin ang maramihang mga tool—tulad ng vector search sa Azure AI Search, mga SQL database, o mga custom na API—bago tuluyang magbigay ng sagot. Nilalaktawan nito ang pangangailangan para sa labis na komplikadong mga framework ng orkestrasyon. Sa halip, ang isang medyo simpleng loop ng “pagtawag sa LLM → gamit ang tool → pagtawag sa LLM → …” ay maaaring magbunga ng mga sopistikado at matibay na mga output.

![Agentic RAG Core Loop](../../../translated_images/tl/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Pagmamay-ari ng Proseso ng Pangangatwiran

Ang natatanging katangian na nagpapagawa sa isang sistema na maging “agentic” ay ang kakayahan nitong pagmay-ari ang proseso ng pangangatwiran nito. Ang mga tradisyunal na implementasyon ng RAG ay madalas na umaasa sa mga tao na magtakda nang maaga ng landas para sa modelo: isang chain-of-thought na naglalarawan kung ano ang kukunin at kailan.
Ngunit kapag ang isang sistema ay tunay na agentic, ito ay sariling nagpapasya kung paano lalapitan ang problema. Hindi lang ito basta sumusunod ng script; awtonomong tinutukoy nito ang pagkakasunod-sunod ng mga hakbang batay sa kalidad ng impormasyong natagpuan nito.
Halimbawa, kung hihilingin itong gumawa ng estratehiya sa paglulunsad ng produkto, hindi lang ito umaasa sa isang prompt na detalyadong nagsasaad ng buong workflow ng pananaliksik at paggawa ng desisyon. Sa halip, ang agentic na modelo ay malayang nagpapasya na:

1. Kumuha ng mga ulat ng kasalukuyang trend sa merkado gamit ang Bing Web Grounding
2. Tukuyin ang mga kaugnay na data ng kakumpitensya gamit ang Azure AI Search.
3. Iugnay ang mga historikal na panloob na sukatan ng benta gamit ang Azure SQL Database.
4. Isintetisa ang mga natuklasan sa isang magkakaugnay na estratehiya na pinamamahalaan sa pamamagitan ng Azure OpenAI Service.
5. Suriin ang estratehiya para sa mga puwang o hindi pagkakatugma, na nag-uudyok ng isa pang round ng retrieval kung kinakailangan.
Lahat ng mga hakbang na ito—pagpino ng mga query, pagpili ng mga pinagmulan, pag-uulit hanggang sa “masaya” sa sagot—ay pinapasiya ng modelo, hindi ito pre-scripted ng tao.

## Mga Iterative Loop, Integrasyon ng Tool, at Memorya

![Tool Integration Architecture](../../../translated_images/tl/tool-integration.0f569710b5c17c10.webp)

Ang isang agentic na sistema ay umaasa sa isang paulit-ulit na pattern ng interaksyon:

- **Unang Tawag:** Ipinapasa ang layunin ng user (aka. user prompt) sa LLM.
- **Pagtawag ng Tool:** Kung natukoy ng modelo na kulang ang impormasyon o malabo ang mga instruksyon, pipili ito ng tool o paraan ng retrieval—tulad ng query sa vector database (hal. Azure AI Search Hybrid search sa pribadong data) o isang istrukturadong SQL call—upang makakuha ng dagdag na konteksto.
- **Pagsusuri at Pagpino:** Pagkatapos suriin ang ibinalik na datos, nagpapasya ang modelo kung sapat ang impormasyon. Kung hindi, pinipino nito ang query, sumusubok ng ibang tool, o inaayos ang diskarte.
- **Ulitin Hanggang Masiyahan:** Ipinagpapatuloy ang siklong ito hanggang matukoy ng modelo na sapat na ang kalinawan at ebidensya upang magbigay ng huling, mahusay na pangangatwirang tugon.
- **Memorya at Estado:** Dahil pinapanatili ng sistema ang estado at memorya sa mga hakbang, naaalala nito ang mga naunang pagtatangka at kinalabasan, iniiwasan ang paulit-ulit na mga loop at gumagawa ng mas mahusay na mga desisyon habang nagpapatuloy.

Sa paglipas ng panahon, lumilikha ito ng pakiramdam ng nagbabagong pag-unawa, na nagpapahintulot sa modelo na gumalaw sa mga kumplikadong multi-step na gawain nang hindi nangangailangan ng patuloy na panghihimasok o pagbabago ng prompt mula sa tao.

## Pagharap sa Mga Failure Modes at Sariling Pagwawasto

Kasama rin sa awtonomiya ng Agentic RAG ang matatag na mga mekanismo ng sariling pagwawasto. Kapag naabot ng sistema ang mga dead end—tulad ng pagkuha ng mga hindi kaugnay na dokumento o pagharap sa mga maling pormang query—maaari nitong:

- **Ulitin at Muling Mag-Query:** Sa halip na magbalik ng mababang halaga na tugon, sinusubukan ng modelo ang mga bagong estratehiya sa paghahanap, nire-rewrite ang mga query sa database, o tumitingin sa ibang mga set ng data.
- **Gamitin ang Mga Diagnostic Tool:** Maaaring tawagan ng sistema ang mga karagdagang function na idinisenyo upang tulungan itong i-debug ang mga hakbang ng pangangatwiran o kumpirmahin ang katumpakan ng nakuha na data. Magiging mahalaga ang mga tool tulad ng Azure AI Tracing upang payagan ang matatag na obserbabilidad at pagmamanman.
- **I-sandalan ang Pangangasiwa ng Tao:** Para sa mga sensitibong sitwasyon o paulit-ulit na pumapalpak, maaaring i-flag ng modelo ang kawalang-katiyakan at humiling ng gabay mula sa tao. Kapag nagbibigay ng korektibong feedback ang tao, maaaring isama ng modelo ang aral na iyon sa mga susunod.

Ang paulit-ulit at dinamikong diskarte na ito ay nagpapahintulot sa modelo na patuloy na mag-improve, na tinitiyak na hindi ito isang one-shot na sistema kundi isa na natututo mula sa mga pagkakamali nito sa isang sesyon.

![Self Correction Mechanism](../../../translated_images/tl/self-correction.da87f3783b7f174b.webp)

## Mga Hangganan ng Ahensya

Sa kabila ng awtonomiya nito sa isang gawain, ang Agentic RAG ay hindi katulad ng Artificial General Intelligence. Ang mga kakayahan nitong “agentic” ay limitado sa mga tool, pinanggagalingan ng data, at mga patakarang ibinigay ng mga human developer. Hindi nito magagawa na likhain ang sarili nitong mga tool o lumabas sa mga hangganan ng domain na itinakda. Sa halip, mahusay ito sa dinamiko na pag-orchestrate ng mga mapagkukunan na nasa kamay.
Ang mga pangunahing pagkakaiba mula sa mas advanced na mga anyo ng AI ay kinabibilangan ng:

1. **Domain-Specific na Awtonomiya:** Nakatuon ang mga Agentic RAG system sa pagtamo ng mga layunin na itinakda ng user sa loob ng kilalang domain, gamit ang mga estratehiya tulad ng pagre-rewrite ng query o pagpili ng tool upang mapabuti ang mga resulta.
2. **Nakasalalay sa Imprastruktura:** Nakabatay ang mga kakayahan ng sistema sa mga tool at data na isinama ng mga developer. Hindi nito kayang lampasan ang mga hangganan na ito nang walang panghihimasok ng tao.
3. **Paggalang sa mga Guardrail:** Mahalaga pa rin ang mga alituntunin sa etika, mga patakaran sa pagsunod, at mga patakaran sa negosyo. Ang kalayaan ng ahente ay palaging napapailalim sa mga hakbang sa kaligtasan at mga mekanismo ng pangangasiwa (sana?).

## Praktikal na Paggamit at Halaga

Namumukod-tangi ang Agentic RAG sa mga senaryong nangangailangan ng paulit-ulit na pagpino at katumpakan:

1. **Mga Kapaligirang Nakatutok sa Katumpakan:** Sa mga pagsusuri ng pagsunod, regulatory analysis, o legal na pananaliksik, maaaring paulit-ulit na i-verify ng agentic na modelo ang mga katotohanan, kumunsulta sa maraming pinagmulan, at i-rewrite ang mga query hanggang makabuo ito ng lubos na nasuri na sagot.
2. **Kumplikadong Pakikipag-ugnayan sa Database:** Kapag humaharap sa mga istrukturadong data kung saan madalas pumalpak o kailangang i-adjust ang mga query, maaaring awtonomong pinuhin ng sistema ang mga query gamit ang Azure SQL o Microsoft Fabric OneLake, na tinitiyak na ang huling retrieval ay naaayon sa intensyon ng user.
3. **Pinalawig na Workflow:** Ang mga mas mahabang sesyon ay maaaring umusbong habang may bagong impormasyon na lumilitaw. Patuloy na maisasama ng Agentic RAG ang bagong data, at magbabago ang mga estratehiya habang natututo ito nang higit pa tungkol sa problemang tinatrabaho.

## Pamamahala, Transparency, at Tiwala

Habang nagiging mas awtonomo ang mga sistemang ito sa kanilang pangangatwiran, mahalaga ang pamamahala at transparency:

- **Maipaliwanag na Pangangatwiran:** Maaaring magbigay ang modelo ng audit trail ng mga query na ginawa nito, mga pinanggalingan na konsulta, at mga hakbang ng pangangatwiran na ginawa upang maabot ang konklusyon. Makakatulong ang mga tool tulad ng Azure AI Content Safety at Azure AI Tracing / GenAIOps upang mapanatili ang transparency at mabawasan ang mga panganib.
- **Kontrol ng Bias at Balanseng Retrieval:** Maaaring ayusin ng mga developer ang mga estratehiya sa retrieval upang matiyak na isinasaalang-alang ang balanseng, kinatawan na mga pinagmulan ng data, at regular na i-audit ang mga output upang matukoy ang bias o skewed pattern gamit ang mga custom na modelo para sa mga advanced na organisasyon ng data science gamit ang Azure Machine Learning.
- **Pangangasiwa ng Tao at Pagsunod:** Para sa mga sensitibong gawain, mahalaga pa rin ang pagsusuri ng tao. Hindi pinapalitan ng Agentic RAG ang paghuhusga ng tao sa mga desisyong may mataas na pusta—pinapalakas nito iyon sa pamamagitan ng paghahatid ng mas lubos na nasuring mga opsyon.

Mahalagang magkaroon ng mga tool na nagbibigay ng malinaw na talaan ng mga aksyon. Kung wala ang mga ito, magiging mahirap ang pag-debug ng multi-step na proseso. Tingnan ang sumusunod na halimbawa mula sa Literal AI (kompanyang nasa likod ng Chainlit) para sa isang Agent run:

![AgentRunExample](../../../translated_images/tl/AgentRunExample.471a94bc40cbdc0c.webp)

## Konklusyon

Kinakatawan ng Agentic RAG ang isang natural na ebolusyon kung paano pinangangasiwaan ng mga sistema ng AI ang mga kumplikado at matinding data-intensive na gawain. Sa pamamagitan ng pag-aampon ng pattern ng looped interaction, awtonomong pagpili ng mga tool, at pagpino ng mga query hanggang makamit ang mataas na kalidad na resulta, lumalampas ang sistema sa static prompt-following patungo sa isang mas adaptive, context-aware na tagagawa ng desisyon. Bagaman nananatili itong limitado ng mga imprastrukturang itinakda ng tao at mga alituntunin sa etika, pinapayagan ng mga kakayahang agentic na ito ang mas mayaman, mas dinamiko, at sa huli ay mas kapaki-pakinabang na mga pakikipag-ugnayan sa AI para sa parehong mga negosyo at mga end-user.

### May Iba Ka Pang Mga Tanong tungkol sa Agentic RAG?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipagkita sa iba pang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

## Karagdagang Mga Mapagkukunan

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Ipatupad ang Retrieval Augmented Generation (RAG) gamit ang Azure OpenAI Service: Alamin kung paano gamitin ang sarili mong data gamit ang Azure OpenAI Service. Nagbibigay ang Microsoft Learn module na ito ng komprehensibong gabay sa pagpapatupad ng RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Pagsusuri ng mga aplikasyong generative AI gamit ang Microsoft Foundry: Tinatalakay ng artikulong ito ang pagsusuri at paghahambing ng mga modelo sa mga pampublikong dataset, kabilang ang mga aplikasyon ng Agentic AI at mga arkitektura ng RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Ano ang Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Isang Kumpletong Gabay sa Agent-Based Retrieval Augmented Generation – Balita mula sa generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: pasiglahin ang iyong RAG gamit ang pag-reformulate ng query at self-query! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Pagdaragdag ng Agentic Layers sa RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Ang Kinabukasan ng Knowledge Assistants: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Paano Bumuo ng Agentic RAG Systems</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Paggamit ng Microsoft Foundry Agent Service upang palakihin ang iyong AI agents</a>

### Mga Akademikong Papel

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Paulit-ulit na Pagpapahusay gamit ang Self-Feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Mga Language Agents na may Verbal Reinforcement Learning</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Kayang Mag-Self-Correct ng Malalaking Language Models gamit ang Tool-Interactive Critiquing</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Isang Survey tungkol sa Agentic RAG</a>

## Pagsusuri ng Agent na Ito (Opsyonal)

Pagkatapos matutunan kung paano i-deploy ang mga ahente sa [Lesson 16](../16-deploying-scalable-agents/README.md), maaari mong i-smoke-test ang `TravelRAGAgent` ng leksyon na ito — tinitingnan na ang mga sagot nito ay manatiling nakabatay sa knowledge base — gamit ang [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Tingnan ang [`tests/README.md`](../tests/README.md) para sa mga paraan kung paano ito patakbuhin.

## Nakaraang Aralin

[Tool Use Design Pattern](../04-tool-use/README.md)

## Susunod na Aralin

[Pagbuo ng Maaasahang AI Agents](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->