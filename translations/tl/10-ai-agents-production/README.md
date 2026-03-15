# Mga AI Agent sa Produksyon: Obserbabilidad & Pagsusuri

[![Mga AI Agent sa Produksyon](../../../translated_images/tl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Habang ang mga AI agent ay gumagalaw mula sa mga eksperimento patungo sa mga aplikasyon sa totoong mundo, nagiging mahalaga ang kakayahang maunawaan ang kanilang pag-uugali, subaybayan ang kanilang pagganap, at sistematikong suriin ang kanilang mga resulta.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang leksyon na ito, malalaman/mo mauunawaan mo:
- Mga pangunahing konsepto ng obserbabilidad at pagsusuri ng agent
- Mga teknik para mapabuti ang pagganap, gastos, at bisa ng mga agent
- Ano at paano sistematikong susuriin ang iyong mga AI agent
- Paano kontrolin ang gastos kapag nagde-deploy ng mga AI agent sa produksyon
- Paano mag-instrument ng mga agent na ginawa gamit ang Microsoft Agent Framework

Ang layunin ay bigyan ka ng kaalaman upang gawing transparent, madaling pamahalaan, at maaasahan ang iyong mga "black box" na agent.

_**Tandaan:** Mahalaga na mag-deploy ng mga AI Agent na ligtas at mapagkakatiwalaan. Tignan din ang leksyon na [Pagbuo ng Mapagkakatiwalaang AI Agents](./06-building-trustworthy-agents/README.md)._

## Mga trace at span

Ang mga observability tool tulad ng [Langfuse](https://langfuse.com/) o [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) ay kadalasang nire-representa ang mga pagtakbo ng agent bilang mga trace at span.

- **Trace** kumakatawan sa isang kumpletong gawain ng agent mula simula hanggang matapos (hal. paghawak ng isang query ng gumagamit).
- **Spans** ay mga indibidwal na hakbang sa loob ng trace (hal. pagtawag sa isang language model o pagkuha ng data).

![Istraktura ng trace sa Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Kung walang obserbabilidad, ang isang AI agent ay maaaring magmukhang isang "black box" - ang panloob na estado at pangangatwiran nito ay hindi malinaw, na nagpapahirap mag-diagnose ng mga isyu o mag-optimize ng pagganap. Sa obserbabilidad, ang mga agent ay nagiging "glass boxes," na nag-aalok ng transparency na mahalaga para sa pagtitiwala at pagtiyak na gumagana sila tulad ng inaasahan. 

## Bakit Mahalaga ang Obserbabilidad sa Mga Kapaligiran ng Produksyon

Ang paglipat ng mga AI agent sa mga kapaligiran ng produksyon ay naglalagay ng bagong hanay ng mga hamon at mga kinakailangan. Hindi na "magandang mayroon" ang obserbabilidad kundi isang kritikal na kakayahan:

*   **Pag-debug at Pagsusuri ng Ugat ng Problema**: Kapag nabigo ang isang agent o nag-produce ng hindi inaasahang output, nagbibigay ang mga tool ng obserbabilidad ng mga trace na kinakailangan upang tukuyin ang pinagmulan ng error. Ito ay lalong mahalaga sa mga komplikadong agent na maaaring may kasamang maraming LLM call, interaksyon sa mga tool, at kondisyunal na lohika.
*   **Pamamahala ng Latensya at Gastos**: Madalas umasa ang mga AI agent sa mga LLM at iba pang external API na sinisingil ayon sa token o bawat tawag. Pinapahintulutan ng obserbabilidad ang tumpak na pagsubaybay sa mga tawag na ito, na tumutulong tukuyin ang mga operasyon na labis na mabagal o magastos. Pinapahintulutan nitong i-optimize ng mga team ang mga prompt, pumili ng mas epektibong modelo, o mag-redisenyo ng workflow upang pamahalaan ang mga operational na gastos at tiyakin ang magandang karanasan ng gumagamit.
*   **Tiwala, Kaligtasan, at Pagsunod**: Sa maraming aplikasyon, mahalaga na tiyakin na kumikilos nang ligtas at etikal ang mga agent. Nagbibigay ang obserbabilidad ng audit trail ng mga aksyon at desisyon ng agent. Maaaring gamitin ito para madetekta at mai-mitigate ang mga isyu tulad ng prompt injection, pag-generate ng mapanganib na nilalaman, o maling paghawak ng personally identifiable information (PII). Halimbawa, maaari mong suriin ang mga trace upang maunawaan kung bakit nagbigay ang agent ng isang partikular na sagot o gumamit ng isang tiyak na tool.
*   **Mga Loop ng Patuloy na Pagpapabuti**: Ang datos ng obserbabilidad ang pundasyon ng iteratibong proseso ng pag-develop. Sa pamamagitan ng pagmamanman kung paano gumaganap ang mga agent sa totoong mundo, maaaring tukuyin ng mga team ang mga lugar para sa pagpapabuti, mangalap ng datos para sa fine-tuning ng mga modelo, at beripikahin ang epekto ng mga pagbabago. Lumilikha ito ng feedback loop kung saan ang mga insight mula sa online evaluation sa produksyon ay nag-iinpluwensya sa offline experimentation at refinement, na nagreresulta sa unti-unting pagbuti ng pagganap ng agent.

## Mga Pangunahing Metrika na Dapat Subaybayan

Upang subaybayan at maunawaan ang pag-uugali ng agent, dapat subaybayan ang iba't ibang metrika at signal. Bagama't maaaring mag-iba ang mga partikular na metrika ayon sa layunin ng agent, ang ilan ay pangkalahatang mahalaga.

Narito ang ilan sa mga pinaka-karaniwang metrika na mino-monitor ng mga observability tool:

**Latensya:** Gaano kabilis tumugon ang agent? Ang mahabang paghihintay ay negatibong nakakaapekto sa karanasan ng gumagamit. Dapat mong sukatin ang latensya para sa mga gawain at indibidwal na hakbang sa pamamagitan ng pag-trace ng mga pagtakbo ng agent. Halimbawa, ang isang agent na tumatagal ng 20 segundo para sa lahat ng tawag sa model ay maaaring pabilisin sa pamamagitan ng paggamit ng mas mabilis na modelo o pagtakbo ng mga tawag sa modelo nang sabay-sabay.

**Mga Gastos:** Magkano ang nagagastos kada pagtakbo ng agent? Umaasa ang mga AI agent sa mga LLM call na sinisingil ayon sa token o sa mga external API. Ang madalas na paggamit ng tool o maraming prompt ay mabilis na nagpapataas ng gastos. Halimbawa, kung tumatawag ang isang agent sa LLM nang limang beses para sa bahagyang pagbuti ng kalidad, kailangang suriin kung makatwiran ang gastos o kung maaari mong bawasan ang bilang ng mga tawag o gumamit ng mas murang modelo. Makakatulong din ang real-time na pagmamanman upang tuklasin ang hindi inaasahang pagtaas (hal., bugs na nagdudulot ng labis na API loops).

**Mga Error sa Kahilingan:** Ilang kahilingan ang nabigo ang agent? Maaari itong kabilang ang mga error sa API o nabigong tawag sa tool. Upang gawing mas matibay ang iyong agent laban sa mga ito sa produksyon, maaari kang mag-set up ng mga fallback o retries. Hal., kung bumagsak ang LLM provider A, lumipat ka sa LLM provider B bilang backup.

**Feedback ng Gumagamit:** Ang pagpapatupad ng direktang ebalwasyon mula sa mga gumagamit ay nagbibigay ng mahahalagang pananaw. Maaaring kabilang dito ang tahasang rating (👍pagsang-ayon/👎hindi pagsang-ayon, ⭐1–5 na bituin) o tekstuwal na mga komento. Ang pare-parehong negatibong feedback ay dapat mag-alerto sa iyo dahil ito ay palatandaan na hindi gumagana ayon sa inaasahan ang agent. 

**Di-tahasang Feedback ng Gumagamit:** Nagbibigay din ang mga kilos ng gumagamit ng di-tahasang feedback kahit walang tahasang rating. Maaaring kabilang dito ang agarang pagre-rephrase ng tanong, paulit-ulit na mga query, o pag-click ng retry button. Hal., kung nakikita mong paulit-ulit na tinatanong ng mga gumagamit ang parehong tanong, ito ay palatandaan na hindi gumagana ayon sa inaasahan ang agent.

**Katumpakan:** Gaano kadalas nagpo-produce ang agent ng tamang o kanais-nais na output? Nag-iiba ang mga kahulugan ng katumpakan (hal., pagkakatama sa paglutas ng problema, katumpakan sa pagkuha ng impormasyon, kasiyahan ng gumagamit). Ang unang hakbang ay tukuyin kung ano ang itsura ng tagumpay para sa iyong agent. Maaari mong subaybayan ang katumpakan sa pamamagitan ng mga automated checks, evaluation scores, o mga label ng pagkakumpleto ng gawain. Halimbawa, pagmamarka ng mga trace bilang "succeeded" o "failed". 

**Automatikong Metrika ng Ebalwasyon:** Maaari ka ring mag-set up ng mga automated eval. Halimbawa, maaari mong gamitin ang isang LLM upang i-score ang output ng agent hal. kung ito ay nakakatulong, tama, o hindi. Mayroon ding ilang open source na library na makakatulong sa iyo na i-score ang iba't ibang aspeto ng agent. Hal., [RAGAS](https://docs.ragas.io/) para sa RAG agents o [LLM Guard](https://llm-guard.com/) upang madetekta ang mapanganib na wika o prompt injection. 

Sa praktika, ang kombinasyon ng mga metrikang ito ang nagbibigay ng pinakamahusay na coverage ng kalusugan ng AI agent. Sa kabanatang ito sa [halimbawang notebook](./code_samples/10-expense_claim-demo.ipynb), ipapakita namin kung paano mukhang ang mga metrikang ito sa totoong mga halimbawa ngunit una, pag-aaralan muna natin kung ano ang hitsura ng isang tipikal na workflow ng ebalwasyon.

## I-instrument ang iyong Agent

Upang makalikom ng tracing data, kailangan mong i-instrument ang iyong code. Ang layunin ay i-instrument ang code ng agent upang mag-emit ng mga trace at metrika na maaaring makuha, maproseso, at ma-visualize ng isang observability platform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) ay naging isang industry standard para sa LLM observability. Nagbibigay ito ng set ng mga API, SDK, at tool para sa pag-generate, pagkolekta, at pag-export ng telemetry data. 

Maraming instrumentation library na bumabalot sa umiiral na agent frameworks at nagpapadali na i-export ang OpenTelemetry spans sa isang observability tool. Natively na nag-iintegrate ang Microsoft Agent Framework sa OpenTelemetry. Nasa ibaba ang isang halimbawa sa pag-iinstrument ng isang MAF agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Ang pagpapatupad ng ahente ay sinusubaybayan nang awtomatiko.
    pass
```

Ang [halimbawang notebook](./code_samples/10-expense_claim-demo.ipynb) sa kabanatang ito ay magpapakita kung paano i-instrument ang iyong MAF agent.

**Manwal na Paglikha ng Span:** Habang nagbibigay ang mga instrumentation library ng magandang baseline, madalas may mga kaso kung saan kailangan ng mas detalyado o custom na impormasyon. Maaari kang manu-manong lumikha ng mga span upang magdagdag ng custom na lohika ng aplikasyon. Mas mahalaga, maaari nilang pagyamanin ang mga awtomatiko o manwal na nilikhang span na may custom na attributes (kilala rin bilang tags o metadata). Kasama sa mga attribute na ito ang business-specific na datos, mga intermediate na kalkulasyon, o anumang konteksto na maaaring maging kapaki-pakinabang para sa pag-debug o pagsusuri, tulad ng `user_id`, `session_id`, o `model_version`.

Halimbawa sa mano-manong paglikha ng mga trace at span gamit ang [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ebalwasyon ng Ahente

Nagbibigay ang obserbabilidad sa atin ng mga metrika, ngunit ang ebalwasyon ay ang proseso ng pagsusuri ng mga datos na iyon (at pagsasagawa ng mga test) upang matukoy kung gaano kahusay gumagana ang isang AI agent at paano ito mapapabuti. Sa ibang salita, kapag mayroon ka nang mga trace at metrika, paano mo ginagamit ang mga ito upang hukuman ang agent at gumawa ng mga desisyon? 

Mahalaga ang regular na ebalwasyon dahil ang mga AI agent ay madalas na non-deterministic at maaaring magbago (sa pamamagitan ng mga update o drifting na pag-uugali ng modelo) – kung walang ebalwasyon, hindi mo malalaman kung ang iyong "smart agent" ay talaga bang gumagana ng maayos o kung ito ay nag-regress.

May dalawang kategorya ng ebalwasyon para sa mga AI agent: **online evaluation** at **offline evaluation**. Parehong mahalaga, at nagko-komplemento sila sa isa't isa. Karaniwan naming sinisimulan sa offline evaluation, dahil ito ang minimum na kinakailangang hakbang bago i-deploy ang anumang agent.

### Offline Ebalwasyon

![Mga item ng dataset sa Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ito ay tungkol sa pagsusuri ng agent sa isang kontroladong setting, karaniwang gamit ang mga test dataset, hindi mga live na query ng gumagamit. Gumagamit ka ng curated na mga dataset kung saan alam mo ang inaasahang output o tamang pag-uugali, at pagkatapos patakbuhin ang iyong agent doon. 

Halimbawa, kung gumawa ka ng agent para sa mga math word-problem, maaari kang magkaroon ng isang [test dataset](https://huggingface.co/datasets/gsm8k) ng 100 problema na may kilalang mga sagot. Madalas ginagawa ang offline evaluation habang nasa development (at maaaring maging bahagi ng CI/CD pipelines) upang tingnan ang mga pagpapabuti o pigilan ang mga regression. Ang benepisyo nito ay na ito ay **maaaring ulitin at makakakuha ka ng malinaw na mga metrika ng katumpakan dahil may ground truth ka**. Maaari mo ring i-simulate ang mga query ng gumagamit at sukatin ang mga tugon ng agent laban sa mga ideal na sagot o gumamit ng mga automated na metrika na inilarawan sa itaas. 

Ang pangunahing hamon sa offline eval ay tiyaking komprehensibo at nananatiling may kaugnayan ang iyong test dataset – maaaring magaling ang agent sa isang fixed test set ngunit makaharap ng napaka-ibang mga query sa produksyon. Samakatuwid, dapat mong panatilihing na-update ang mga test set ng mga bagong edge case at mga halimbawa na sumasalamin sa mga sitwasyon sa totoong mundo​. Magandang pagsamahin ang maliliit na "smoke test" na kaso at mas malalaking evaluation set: maliliit na set para sa mabilis na tseke at mas malalaki para sa mas malawak na metrika ng pagganap​.

### Online Ebalwasyon 

![Pangkalahatang-ideya ng mga metrika ng obserbabilidad](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ito ay tumutukoy sa pagsusuri ng agent sa isang live, totoong-kalakarang kapaligiran, i.e. habang aktwal na ginagamit sa produksyon. Kabilang sa online evaluation ang pagmamanman ng pagganap ng agent sa tunay na interaksyon ng gumagamit at patuloy na pagsusuri ng mga resulta. 

Halimbawa, maaari mong subaybayan ang mga success rate, mga score ng kasiyahan ng gumagamit, o iba pang metrika sa live traffic. Ang bentahe ng online evaluation ay na **na-capture nito ang mga bagay na maaaring hindi mo inaasahan sa lab setting** – maaari mong obserbahan ang model drift sa paglipas ng panahon (kung bumababa ang bisa ng agent habang nagbabago ang mga pattern ng input) at mahuli ang mga hindi inaasahang query o sitwasyon na wala sa iyong test data​. Nagbibigay ito ng tunay na larawan kung paano kumikilos ang agent sa aktwal na paggamit. 

Kadalasan kasama sa online evaluation ang pagkolekta ng implicit at explicit na feedback ng gumagamit, gaya ng napag-usapan, at posibleng pagpapatakbo ng shadow tests o A/B tests (kung saan ang bagong bersyon ng agent ay tumatakbo nang paralel upang ikumpara sa luma). Ang hamon ay maaaring mahirap makakuha ng maasahang labels o score para sa mga live interaction – maaaring umasa ka sa feedback ng gumagamit o downstream na metrika (tulad ng kung klinik ba ng gumagamit ang resulta). 

### Pagsasama ng dalawa

Hindi magkakahiwalay ang online at offline evaluation; lubos silang nagko-komplemento. Ang mga insight mula sa online monitoring (hal., bagong uri ng mga query ng gumagamit kung saan mahina ang agent) ay maaaring gamitin upang mapalawak at pagandahin ang mga offline test dataset. Sa kabilang banda, ang mga agent na maganda ang performance sa offline tests ay maaaring i-deploy nang mas may kumpiyansa at i-monitor online. 

Sa katunayan, maraming team ang nagpapatupad ng isang loop: 

_evaluate offline -> deploy -> monitor online -> collect new failure cases -> add to offline dataset -> refine agent -> repeat_.

## Mga Karaniwang Isyu

Habang ini-deploy mo ang mga AI agent sa produksyon, maaaring makatagpo ka ng iba't ibang hamon. Narito ang ilang karaniwang isyu at ang kanilang mga posibleng solusyon:

| **Isyu**    | **Posibleng Solusyon**   |
| ------------- | ------------------ |
| Hindi palaging matagumpay na isinasagawa ng AI Agent ang mga gawain | - Puhin ang prompt na ibinibigay sa AI Agent; maging malinaw sa mga layunin.<br>- Tukuyin kung saan makakatulong ang paghahati ng mga gawain sa mas maliliit na bahagi at pagtalaga ng iba't ibang agent para hawakan ang mga ito. |
| Nakakapasok ang AI Agent sa tuloy-tuloy na loop  | - Tiyaking mayroon kang malinaw na mga termino at kundisyon sa pagtatapos upang malaman ng Agent kung kailan ititigil ang proseso.<br>- Para sa komplikadong gawain na nangangailangan ng pangangatwiran at pagpaplano, gumamit ng mas malaking modelo na espesyalista sa mga gawain ng pangangatwiran. |
| Hindi mahusay ang pagganap ng mga tawag sa tool ng AI Agent   | - Subukan at beripikahin ang output ng tool sa labas ng sistema ng agent.<br>- Puhin ang mga tinukoy na parameter, mga prompt, at pagngalan ng mga tool.  |
| Hindi konsistent ang pagganap ng multi-agent na sistema | - Puhin ang mga prompt na ibinibigay sa bawat agent upang matiyak na partikular at magkakaiba ang mga ito.<br>- Bumuo ng hierarchical na sistema gamit ang isang "routing" o controller agent upang tukuyin kung alin ang tamang agent. |

Marami sa mga isyung ito ay maaaring tukuyin nang mas epektibo kapag may obserbabilidad. Ang mga trace at metrika na tinalakay natin kanina ay tumutulong tukuyin nang eksakto kung saan sa workflow ng agent nagaganap ang mga problema, na ginagawang mas madali ang pag-debug at pag-optimize.

## Pamamahala ng Gastos
Narito ang ilang mga estratehiya upang pamahalaan ang mga gastos ng pag-deploy ng AI agents sa produksyon:

**Using Smaller Models:** Ang Maliit na mga Modelo ng Wika (SLMs) ay maaaring mag-perform nang maayos sa ilang agentic na mga kaso ng paggamit at makabuluhang makakapagpababa ng gastos. Gaya ng nabanggit kanina, ang pagbuo ng isang sistemang pagsusuri upang matukoy at ihambing ang pagganap kumpara sa mas malalaking modelo ay ang pinakamahusay na paraan upang maunawaan kung gaano kahusay gaganapin ng isang SLM ang iyong kaso ng paggamit. Isaalang-alang ang paggamit ng SLMs para sa mas simpleng gawain tulad ng pag-uuri ng intensyon o pagkuha ng mga parameter, habang inilalaan ang mas malalaking modelo para sa komplikadong pangangatwiran.

**Using a Router Model:** Isang katulad na estratehiya ang paggamit ng iba't ibang mga modelo at sukat. Maaari kang gumamit ng LLM/SLM o serverless function upang i-route ang mga kahilingan batay sa antas ng kahirapan patungo sa pinakaangkop na mga modelo. Makakatulong din ito na mabawasan ang gastos habang tinitiyak ang pagganap sa mga tamang gawain. Halimbawa, i-route ang mga simpleng query sa mas maliit, mas mabilis na mga modelo, at gamitin lamang ang magastos na malalaking modelo para sa mga komplikadong gawain ng pangangatwiran.

**Caching Responses:** Ang pagtukoy sa mga karaniwang kahilingan at gawain at pagbibigay ng mga tugon bago pa man dumaan ang mga ito sa iyong agentic system ay isang magandang paraan upang mabawasan ang dami ng magkakahawig na kahilingan. Maaari mo ring ipatupad ang isang daloy upang tukuyin kung gaano kahawig ang isang kahilingan sa iyong naka-cache na mga kahilingan gamit ang mga mas batayang modelo ng AI. Ang estratehiyang ito ay maaaring makabuluhang magpababa ng gastos para sa madalas na itinatanong na mga tanong o karaniwang mga workflow.

## Tingnan natin kung paano ito gumagana sa praktika

Sa [halimbawang notebook ng seksyong ito](./code_samples/10-expense_claim-demo.ipynb), makikita natin ang mga halimbawa kung paano natin magagamit ang mga kasangkapan sa obserbabilidad upang subaybayan at suriin ang ating ahente.


### May mga karagdagang tanong tungkol sa mga AI Agents sa produksyon?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa iba pang mga nag-aaral, dumalo sa office hours at masagot ang iyong mga tanong tungkol sa AI Agents.

## Nakaraang Aralin

[Metacognition Design Pattern](../09-metacognition/README.md)

## Susunod na Aralin

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Paunawa:
Isinalin ang dokumentong ito gamit ang serbisyo ng AI para sa pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kaming maging tumpak, pakitandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o kawalan ng katumpakan. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na awtoritatibong sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling ginawa ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na magmumula sa paggamit ng salin na ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->