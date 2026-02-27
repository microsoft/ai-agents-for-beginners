# Mga AI Agent sa Produksyon: Observability & Evaluation

[![Mga AI Agent sa Produksyon](../../../translated_images/tl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Habang ang mga AI agent ay umuusad mula sa mga eksperimento patungo sa mga aplikasyon sa totoong mundo, nagiging mahalaga ang kakayahang maunawaan ang kanilang pag-uugali, subaybayan ang kanilang pagganap, at sistematikong suriin ang kanilang mga output.

## Mga Layunin sa Pagkatuto

Matapos makumpleto ang araling ito, malalaman/moang maiintindihan mo kung paano:
- Mga pangunahing konsepto ng observability at pagsusuri ng agent
- Mga teknik para mapabuti ang pagganap, gastos, at bisa ng mga agent
- Ano at paano sistematikong susuriin ang iyong mga AI agent
- Paano kontrolin ang gastos kapag nagde-deploy ng mga AI agent sa produksyon
- Paano i-instrument ang mga agent na binuo gamit ang Microsoft Agent Framework

Ang layunin ay bigyan ka ng kaalaman upang gawing transparent, madaling pamahalaan, at maaasahang mga sistema ang iyong mga "black box" na agent.

_**Note:** Mahalaga na mag-deploy ng mga AI Agent na ligtas at mapagkakatiwalaan. Tingnan din ang araling [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md)._

## Traces at Spans

Ang mga tool para sa observability tulad ng [Langfuse](https://langfuse.com/) o [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) ay karaniwang nire-representa ang mga takbo ng agent bilang traces at spans.

- **Trace** kumakatawan sa isang kumpletong gawain ng agent mula simula hanggang matapos (hal., paghawak ng isang query ng user).
- **Spans** ay mga indibidwal na hakbang sa loob ng trace (hal., pagtawag sa isang language model o pagkuha ng datos).

![Punong trace sa Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Kung walang observability, ang isang AI agent ay maaaring magmukhang isang "black box" - ang panloob na estado at pag-iisip nito ay hindi malinaw, na nagpapahirap sa pag-diagnose ng mga isyu o pag-optimize ng pagganap. Sa pamamagitan ng observability, nagiging mga "glass box" ang mga agent, na nagbibigay ng transparency na mahalaga sa pagtatayo ng tiwala at pagtitiyak na gumagana sila ayon sa inaasahan.

## Bakit Mahalaga ang Observability sa Mga Kapaligirang Produksyon

Ang paglipat ng mga AI agent sa mga kapaligirang produksyon ay nagdadala ng bagong hanay ng mga hamon at pangangailangan. Ang observability ay hindi na isang "magandang meron lang" kundi isang kritikal na kakayahan:

*   **Pag-debug at Pagsusuri ng Ugat ng Problema**: Kapag nabigo ang isang agent o nakabuo ng hindi inaasahang output, nagbibigay ang mga tool ng observability ng mga trace na kailangan upang tukuyin ang pinagmulan ng error. Ito ay lalo na mahalaga sa mga kumplikadong agent na maaaring may maraming LLM calls, mga interaksyong tool, at kundisyonal na lohika.
*   **Pamamahala ng Latency at Gastos**: Kadalasang umaasa ang mga AI agent sa mga LLM at iba pang external API na sinisingil per token o bawat tawag. Pinahihintulutan ng observability ang tumpak na pagsubaybay sa mga tawag na ito, na tumutulong tukuyin ang mga operasyon na sobrang mabagal o mahal. Hinahayaan nito ang mga koponan na i-optimize ang mga prompt, pumili ng mas epektibong mga modelo, o muling idisenyo ang mga workflow upang pamahalaan ang operational na gastos at matiyak ang magandang karanasan ng gumagamit.
*   **Tiwala, Kaligtasan, at Pagsunod**: Sa maraming aplikasyon, mahalaga na tiyakin na kumikilos nang ligtas at etikal ang mga agent. Nagbibigay ang observability ng audit trail ng mga aksyon at desisyon ng agent. Maaari itong gamitin upang matukoy at mabawasan ang mga isyu tulad ng prompt injection, pagbuo ng mapanganib na nilalaman, o maling paghawak ng personally identifiable information (PII). Halimbawa, maaari mong repasuhin ang mga trace upang maunawaan kung bakit nagbigay ang agent ng isang tiyak na tugon o ginamit ang isang partikular na tool.
*   **Patuloy na Loop ng Pagpapabuti**: Ang datos mula sa observability ang pundasyon ng iterative na proseso ng pag-develop. Sa pamamagitan ng pagmamasid kung paano gumagana ang mga agent sa totoong mundo, maaaring tukuyin ng mga koponan ang mga lugar na dapat pagbutihin, mangalap ng datos para sa fine-tuning ng mga modelo, at beripikahin ang epekto ng mga pagbabago. Lumilikha ito ng feedback loop kung saan ang mga insight mula sa online evaluation sa produksyon ay nag-iinform ng offline experimentation at refinement, na humahantong sa sunud-sunod na mas mabuting pagganap ng agent.

## Mga Pangunahing Metric na Dapat Subaybayan

Upang subaybayan at maunawaan ang pag-uugali ng agent, dapat subaybayan ang iba't ibang metric at signal. Bagaman maaaring mag-iba ang mga partikular na metric batay sa layunin ng agent, ang ilan ay pangkalahatang mahalaga.

Narito ang ilan sa mga karaniwang metric na sinusubaybayan ng mga tool ng observability:

**Latency:** Gaano kabilis tumugon ang agent? Ang mahabang paghihintay ay nakakaapekto nang negatibo sa karanasan ng gumagamit. Dapat mong sukatin ang latency para sa mga gawain at indibidwal na hakbang sa pamamagitan ng pag-trace ng mga takbo ng agent. Halimbawa, ang isang agent na tumatagal ng 20 segundo para sa lahat ng model calls ay maaaring pabilisin sa pamamagitan ng paggamit ng mas mabilis na modelo o pamamagitan ng pagpapatakbo ng mga model call nang magkakasabay.

**Costs:** Magkano ang gastos kada takbo ng agent? Umaasa ang mga AI agent sa LLM calls na sinisingil per token o sa mga external API. Ang madalas na paggamit ng tool o maraming prompt ay maaaring mabilis na magpataas ng gastos. Halimbawa, kung tinatawagan ng agent ang isang LLM ng limang beses para sa maliit na pagpapabuti ng kalidad, kailangang suriin kung makatarungan ang gastos o kung maaari mong bawasan ang bilang ng tawag o gumamit ng mas murang modelo. Makakatulong din ang real-time monitoring upang tuklasin ang hindi inaasahang pagtaas (hal., bugs na nagdudulot ng labis na API loops).

**Request Errors:** Ilan ang mga request na nabigo ang agent? Maaaring kasama dito ang API errors o nabigong tawag sa tool. Upang gawing mas matibay ang iyong agent laban sa mga ito sa produksyon, maaari kang mag-set up ng mga fallback o retries. Hal., kung down ang LLM provider A, maaari kang lumipat sa LLM provider B bilang backup.

**User Feedback:** Ang pag-implementa ng direktang pagsusuri mula sa user ay nagbibigay ng mahahalagang insight. Maaari itong isama ang tahasang ratings (👍thumbs-up/👎down, ⭐1-5 stars) o tekstuwal na komento. Ang patuloy na negatibong feedback ay dapat mag-alerto sa iyo dahil ito ay senyales na hindi gumagana ang agent ayon sa inaasahan.

**Implicit User Feedback:** Nagbibigay ang mga gawi ng user ng di-tuwirang feedback kahit walang tahasang rating. Maaaring kabilang dito ang agarang pag-rephrase ng tanong, paulit-ulit na mga query, o pag-click ng retry button. Hal., kung nakikita mong paulit-ulit na tinatanong ng mga user ang parehong tanong, ito ay senyales na hindi gumagana ang agent ayon sa inaasahan.

**Accuracy:** Gaano kadalas nagbibigay ang agent ng tama o kanais-nais na mga output? Nag-iiba ang mga depinisyon ng accuracy (hal., tama sa paglutas ng problema, accuracy ng information retrieval, kasiyahan ng user). Ang unang hakbang ay tukuyin kung ano ang itsura ng tagumpay para sa iyong agent. Maaari mong subaybayan ang accuracy sa pamamagitan ng automated checks, evaluation scores, o mga label ng pagkumpleto ng gawain. Halimbawa, pagmamarka ng mga trace bilang "succeeded" o "failed".

**Automated Evaluation Metrics:** Maaari ka ring mag-set up ng automated evals. Halimbawa, maaari mong gamitin ang isang LLM upang i-score ang output ng agent kung ito ay kapaki-pakinabang, tama, o hindi. Mayroon ding ilang open source libraries na tumutulong sa pag-score ng iba't ibang aspeto ng agent. Hal., [RAGAS](https://docs.ragas.io/) para sa RAG agents o [LLM Guard](https://llm-guard.com/) para matukoy ang nakapipinsalang wika o prompt injection.

Sa praktika, ang kombinasyon ng mga metric na ito ang nagbibigay ng pinakamainam na coverage ng kalagayan ng isang AI agent. Sa kabanatang ito [example notebook](./code_samples/10-expense_claim-demo.ipynb), ipapakita namin kung paano lumilitaw ang mga metric na ito sa mga totoong halimbawa, ngunit unang matututuhan muna natin kung ano ang hitsura ng isang tipikal na workflow sa pagsusuri.

## I-instrument ang iyong Agent

Upang makalikom ng tracing data, kailangan mong i-instrument ang iyong code. Ang layunin ay i-instrument ang code ng agent upang mag-emit ng traces at metrics na maaaring makuha, iproseso, at i-visualize ng isang observability platform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) ay umusbong bilang industriyang pamantayan para sa LLM observability. Nagbibigay ito ng set ng mga API, SDK, at tool para sa pagbuo, pagkolekta, at pag-export ng telemetry data.

Maraming instrumentation libraries na nag-wrap sa mga umiiral na agent frameworks at nagpapadali sa pag-export ng OpenTelemetry spans sa isang observability tool. Native na nag-iintegrate ang Microsoft Agent Framework sa OpenTelemetry. Nasa ibaba ang isang halimbawa ng pag-iinstrument ng isang MAF agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Ang pagpapatupad ng ahente ay awtomatikong nasusubaybayan.
    pass
```

The [example notebook](./code_samples/10-expense_claim-demo.ipynb) in this chapter will demonstrate how to instrument your MAF agent.

**Manual Span Creation:** Habang nagbibigay ang mga instrumentation library ng magandang baseline, may mga kaso kung saan kailangan ng mas detalyado o pasadyang impormasyon. Maaari kang manu-manong lumikha ng spans upang magdagdag ng pasadyang lohika ng aplikasyon. Mas mahalaga, maaari nilang pagyamanin ang awtomatiko o manu-manong nilikhang spans ng pasadyang attributes (kilala rin bilang tags o metadata). Kasama sa mga attribute na ito ang business-specific na datos, mga intermediate na kalkulasyon, o anumang konteksto na maaaring maging kapaki-pakinabang para sa pag-debug o pagsusuri, tulad ng `user_id`, `session_id`, o `model_version`.

Halimbawa ng manu-manong paggawa ng traces at spans gamit ang [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Pagsusuri ng Agent

Nagbibigay ang observability ng mga metric, ngunit ang pagsusuri ay ang proseso ng pag-aanalisa ng mga datos na iyon (at pagsasagawa ng mga test) upang tukuyin kung gaano kagaling ang pagganap ng isang AI agent at kung paano pa ito mapapabuti. Sa ibang salita, kapag nakuha mo na ang mga trace at metric na iyon, paano mo gagamitin ang mga ito upang hatulan ang agent at gumawa ng mga desisyon?

Mahalaga ang regular na pagsusuri dahil kadalasan ay hindi deterministic ang mga AI agent at maaari silang magbago (sa pamamagitan ng mga update o drifting na pag-uugali ng modelo) – kung walang pagsusuri, hindi mo malalaman kung ang iyong "matalinong agent" ay talagang gumagawa ng mabuti o kung ito ay nag-regress.

May dalawang kategorya ng pagsusuri para sa mga AI agent: **online evaluation** at **offline evaluation**. Parehong mahalaga ang dalawa, at nagko-komplementa sa isa't isa. Kadalasan nagsisimula tayo sa offline evaluation, dahil ito ang minimum na kinakailangang hakbang bago mag-deploy ng anumang agent.

### Offline Evaluation

![Mga item ng dataset sa Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Kasama rito ang pagsusuri ng agent sa isang kontroladong setting, karaniwang gamit ang test datasets, hindi live na mga query ng user. Gumagamit ka ng curated datasets kung saan alam mo kung ano ang inaasahang output o tamang pag-uugali, at pagkatapos patakbuhin ang iyong agent sa mga iyon.

Halimbawa, kung bumuo ka ng agent para sa math word problems, maaaring mayroon kang [test dataset](https://huggingface.co/datasets/gsm8k) ng 100 problema na may kilalang mga sagot. Madalas isinasagawa ang offline evaluation habang nagde-develop (at maaari itong maging bahagi ng CI/CD pipelines) upang suriin ang mga pagpapabuti o maiwasan ang regressions. Ang benepisyo ay na ito ay **maaaring ulitin at makakakuha ka ng malinaw na mga metric ng accuracy dahil mayroon kang ground truth**. Maaari mo ring i-simulate ang mga query ng user at sukatin ang mga tugon ng agent laban sa ideal na mga sagot o gumamit ng automated metrics gaya ng inilarawan sa itaas.

Ang pangunahing hamon sa offline eval ay ang pagtiyak na komprehensibo at nananatiling relevant ang iyong test dataset – maaaring maganda ang pagganap ng agent sa isang fixed na test set ngunit maka-encounter ng napaka-ibang mga query sa produksyon. Samakatuwid, dapat mong panatilihing na-update ang mga test set gamit ang mga bagong edge case at halimbawa na sumasalamin sa totoong mundo​. Kapaki-pakinabang ang halo ng maliliit na "smoke test" na kaso at mas malalaking evaluation set: maliliit na set para sa mabilisang tseke at mas malalaki para sa mas malawak na metric ng pagganap​.

### Online Evaluation 

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ito ay tumutukoy sa pagsusuri ng agent sa isang live, totoong-kalabasan na kapaligiran, i.e., habang aktwal na ginagamit sa produksyon. Kabilang sa online evaluation ang pagmamasid ng pagganap ng agent sa totoong interaksyon ng user at patuloy na pag-aanalisa ng mga resulta.

Halimbawa, maaari mong subaybayan ang success rates, mga score ng kasiyahan ng user, o iba pang metric sa live traffic. Ang bentahe ng online evaluation ay na ito ay **nakakakuha ng mga bagay na maaaring hindi mo inaasahan sa isang lab setting** – maaari mong obserbahan ang model drift sa paglipas ng panahon (kung bumababa ang bisa ng agent habang nagbabago ang mga pattern ng input) at mahuli ang mga hindi inaasahang query o sitwasyon na wala sa iyong test data​. Nagbibigay ito ng totoong larawan kung paano kumikilos ang agent sa aktwal na paggamit.

Kadalasan kinapapalooban ng online evaluation ang pagkolekta ng implicit at explicit na feedback ng user, gaya ng tinalakay, at posibleng pagpapatakbo ng shadow tests o A/B tests (kung saan ang bagong bersyon ng agent ay tumatakbo nang sabay sa lumang bersyon para ihambing). Ang hamon ay maaaring maging mahirap makakuha ng maaasahang labels o scores para sa live interactions – maaaring umasa ka sa user feedback o downstream metrics (tulad ng kung na-click ba ng user ang resulta).

### Pagsasama ng dalawa

Hindi magkahukuman ang online at offline evaluations; sila ay lubos na nagko-komplementa. Ang mga insight mula sa online monitoring (hal., mga bagong uri ng query ng user kung saan mahina ang agent) ay maaaring gamitin upang dagdagan at pagbutihin ang offline test datasets. Sa kabilang banda, ang mga agent na mahusay sa offline tests ay maaaring mas may kumpiyansang i-deploy at i-monitor online.

Sa katunayan, maraming koponan ang gumagamit ng isang loop:

_evaluate offline -> deploy -> monitor online -> collect new failure cases -> add to offline dataset -> refine agent -> repeat_.

## Mga Karaniwang Isyu

Habang nagde-deploy ka ng mga AI agent sa produksyon, maaari kang makatagpo ng iba't ibang hamon. Narito ang ilang karaniwang isyu at ang mga posibleng solusyon:

| **Isyu**    | **Posibleng Solusyon**   |
| ------------- | ------------------ |
| AI Agent not performing tasks consistently | - Pagandahin ang prompt na ibinibigay sa AI Agent; maging malinaw sa mga layunin.<br>- Tukuyin kung saan makakatulong ang paghahati ng mga gawain sa mga subtask at paghawak nila ng multiple agents. |
| AI Agent running into continuous loops  | - Tiyaking mayroon kang malinaw na termination terms at kondisyon para malaman ng Agent kung kailan titigil ang proseso.<br>- Para sa mga kumplikadong gawain na nangangailangan ng reasoning at planning, gumamit ng mas malaking modelo na espesyalisado sa mga reasoning task. |
| AI Agent tool calls are not performing well   | - Subukan at beripikahin ang output ng tool sa labas ng agent system.<br>- Pinuhin ang mga tinukoy na parameter, prompt, at pagba-rename ng mga tool.  |
| Multi-Agent system not performing consistently | - Pinuhin ang mga prompt na ibinibigay sa bawat agent upang matiyak na sila ay tiyak at magkakaiba.<br>- Bumuo ng hierarchical system gamit ang isang "routing" o controller agent upang tukuyin kung alin ang tamang agent. |

Marami sa mga isyung ito ay maaaring matukoy nang mas epektibo kapag mayroon nang observability. Ang mga trace at metric na tinalakay natin kanina ay tumutulong tukuyin kung saan eksakto sa workflow ng agent nagaganap ang mga problema, na nagpapadali sa pag-debug at pag-optimize.

## Pamamahala ng Gastos
Narito ang ilang mga estratehiya upang pamahalaan ang mga gastos sa pag-deploy ng mga ahente ng AI sa produksyon:

**Using Smaller Models:** Small Language Models (SLMs) can perform well on certain agentic use-cases and will reduce costs significantly. As mentioned earlier, building an evaluation system to determine and compare performance vs larger models is the best way to understand how well an SLM will perform on your use case. Consider using SLMs for simpler tasks like intent classification or parameter extraction, while reserving larger models for complex reasoning.

**Using a Router Model:** Isang katulad na estratehiya ang paggamit ng iba't ibang modelo at sukat. Maaari kang gumamit ng LLM/SLM o serverless na function upang i-route ang mga kahilingan batay sa pagiging kumplikado sa mga modelong pinaka-angkop. Makakatulong din ito na mabawasan ang gastos habang tinitiyak ang pagganap sa mga tamang gawain. Halimbawa, i-route ang mga simpleng query sa mas maliit at mas mabilis na mga modelo, at gamitin lamang ang magastos na malalaking modelo para sa mga kumplikadong gawain ng pangangatwiran.

**Caching Responses:** Ang pagtukoy ng mga karaniwang kahilingan at gawain at pagbibigay ng mga tugon bago pa man dumaan ang mga ito sa iyong agentic system ay isang magandang paraan upang mabawasan ang dami ng magkakatulad na kahilingan. Maaari ka ring magpatupad ng isang daloy upang matukoy kung gaano pagkakahawig ang isang kahilingan sa iyong mga naka-cache na kahilingan gamit ang mas mga basic na AI model. Ang estratehiyang ito ay maaaring makabuluhang magpababa ng gastos para sa madalas itanong na mga tanong o karaniwang mga workflow.

## Tingnan natin kung paano ito gumagana sa praktika

Sa [halimbawang notebook ng seksyong ito](./code_samples/10-expense_claim-demo.ipynb), makikita natin ang mga halimbawa kung paano natin magagamit ang mga tool ng observability upang subaybayan at suriin ang ating ahente.


### May karagdagang tanong tungkol sa mga ahente ng AI na nasa produksyon?

Sumali sa [Discord ng Microsoft Foundry](https://aka.ms/ai-agents/discord) para makipagkita sa ibang mga nag-aaral, dumalo sa office hours at masagot ang iyong mga tanong tungkol sa mga ahente ng AI.

## Nakaraang Aralin

[Disenyo ng Metakognisyon](../09-metacognition/README.md)

## Susunod na Aralin

[Mga Protocol ng Ahente](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Paunawa:
Isinalin ang dokumentong ito gamit ang serbisyong pagsasalin ng AI na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kaming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpak. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin na ginagawa ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->