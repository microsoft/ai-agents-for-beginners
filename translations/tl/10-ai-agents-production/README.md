# Mga AI Agent sa Produksyon: Obserbabilidad at Pagsusuri

[![AI Agents in Production](../../../translated_images/tl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Habang ang mga AI agent ay lumilipat mula sa mga eksperimentong prototype patungo sa mga aplikasyon sa totoong mundo, nagiging mahalaga ang kakayahang maunawaan ang kanilang kilos, subaybayan ang kanilang pagganap, at sistematikong suriin ang kanilang mga nagagawa.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, malalaman/moangunawaan mo kung paano:
- Mga pangunahing konsepto ng obserbabilidad at pagsusuri ng mga agent
- Mga teknik para mapabuti ang pagganap, gastos, at bisa ng mga agent
- Ano at paano sistematikong suriin ang iyong mga AI agent
- Paano kontrolin ang gastos kapag naglunsad ng mga AI agent sa produksyon
- Paano mag-instrument ng mga agent na binuo gamit ang Microsoft Agent Framework

Ang layunin ay bigyan ka ng kaalaman upang gawing transparent, mapamamahalaan, at maaasahan ang iyong mga "black box" na agent.

_**Tandaan:** Mahalaga ang paglulunsad ng mga AI Agent na ligtas at mapagkakatiwalaan. Tingnan din ang aralin na [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Mga Traces at Spans

Ang mga tool sa obserbabilidad gaya ng [Langfuse](https://langfuse.com/) o [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) ay karaniwang kumakatawan sa mga pagtakbo ng agent bilang mga traces at spans.

- **Trace** ay kumakatawan sa isang kumpletong gawain ng agent mula simula hanggang matapos (tulad ng pagproseso ng query ng gumagamit).
- **Spans** ay mga indibidwal na hakbang sa loob ng trace (tulad ng pagtawag ng language model o pagkuha ng datos).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Kung walang obserbabilidad, maaaring maging parang "black box" ang isang AI agent – ang panloob nitong estado at pag-iisip ay hindi malinaw, kaya mahirap mag-diagnose ng mga isyu o pagbutihin ang pagganap. Sa obserbabilidad, nagiging "glass boxes" ang mga agent, na nag-aalok ng transparency na mahalaga para sa pagtitiwala at pagtitiyak na gumagana sila ayon sa nilalayon.

## Bakit Mahalaga ang Obserbabilidad sa Mga Kapaligiran ng Produksyon

Ang paglilipat ng mga AI agent sa mga kapaligiran ng produksyon ay nagdadala ng bagong hanay ng mga hamon at pangangailangan. Ang obserbabilidad ay hindi na "magandang magkaroon" kundi isang kritikal na kakayahan:

*   **Pag-debug at Pagsusuri ng Ugat na Sanhi**: Kapag nabigo ang isang agent o naglabas ng hindi inaasahang output, nagbibigay ang mga tool sa obserbabilidad ng mga trace upang matukoy ang pinagmulan ng error. Mahalaga ito lalo na sa mga komplikadong agent na maaaring tumawag ng maraming LLM, makipag-ugnayan sa mga tool, at gumamit ng kondisyunal na lohika.
*   **Pamamahala ng Latency at Gastos**: Madalas umasa ang mga AI agent sa LLM at iba pang panlabas na API na sinisingil batay sa token o pagtawag. Pinahihintulutan ng obserbabilidad ang tumpak na pagsubaybay ng mga tawag na ito, na tumutulong matukoy ang mga operasyong napakabagal o magastos. Nagbibigay ito daan sa mga koponan para i-optimize ang mga prompt, pumili ng mas epektibong modelo, o muling disenyo ng mga workflow upang pamahalaan ang gastos at matiyak ang magandang karanasan ng gumagamit.
*   **Tiwala, Kaligtasan, at Pagsunod**: Sa maraming aplikasyon, mahalagang tiyakin na kumikilos nang ligtas at etikal ang mga agent. Nagbibigay ang obserbabilidad ng audit trail ng mga aksyon at desisyon ng agent. Maaari itong gamitin upang matukoy at malimitahan ang mga isyu tulad ng prompt injection, paggawa ng mapanganib na nilalaman, o maling paghawak ng personally identifiable information (PII). Halimbawa, maaari mong suriin ang mga trace para maunawaan kung bakit nagbigay ang agent ng isang partikular na tugon o ginamit ang isang partikular na tool.
*   **Patuloy na Loop ng Pagpapabuti**: Ang data ng obserbabilidad ang pundasyon ng iterative na proseso ng pag-unlad. Sa pamamagitan ng pagsubaybay kung paano gumaganap ang mga agent sa totoong mundo, maaaring matukoy ng mga koponan ang mga lugar na kailangang pagbutihin, mangalap ng data para sa fine-tuning ng mga modelo, at beripikahin ang epekto ng mga pagbabago. Lumilikha ito ng feedback loop kung saan ang mga insight mula sa online na pagsusuri sa produksyon ay nag-iimpluwensya sa offline na eksperimento at pagpino, na humahantong sa mas mahusay na pagganap ng agent.

## Mga Pangunahing Sukatan na Dapat Subaybayan

Upang masubaybayan at maunawaan ang kilos ng agent, dapat subaybayan ang iba't ibang sukatan at signal. Bagaman maaaring mag-iba ang partikular na mga sukatan depende sa layunin ng agent, may ilang mahalagang sukatan na unibersal.

Narito ang ilan sa mga karaniwang sukatan na sinusubaybayan ng mga tool sa obserbabilidad:

**Latency:** Gaano kabilis ang tugon ng agent? Ang mahabang oras ng paghintay ay negatibong nakakaapekto sa karanasan ng gumagamit. Dapat mong sukatin ang latency para sa mga gawain at mga indibidwal na hakbang sa pamamagitan ng pagsubaybay ng mga pagtakbo ng agent. Halimbawa, ang isang agent na tumatagal ng 20 segundo para sa lahat ng tawag sa modelo ay maaaring pabilisin sa pamamagitan ng paggamit ng mas mabilis na modelo o pagpapatakbo ng mga model calls nang sabay-sabay.

**Gastos:** Magkano ang gastos bawat pagtakbo ng agent? Umaasa ang mga AI agent sa mga tawag sa LLM na sinisingil bawat token o sa mga panlabas na API. Ang madalas na paggamit ng tool o maraming mga prompt ay maaaring mabilis magpataas ng gastos. Halimbawa, kung tatlong beses tumatawag ang isang agent sa LLM para sa kaunting pagbuti sa kalidad, dapat mong suriin kung makatwiran ang gastos o kung maaari mong bawasan ang bilang ng mga tawag o gumamit ng mas murang modelo. Makakatulong din ang real-time na pagsubaybay upang matukoy ang hindi inaasahang pagtaas (hal., bug na sanhi ng labis na loop ng API).

**Mga Error sa Request:** Ilan ang mga request na nabigo ang agent? Maaari itong kabilang ang error sa API o nabigong mga tawag sa tool. Upang maging mas matibay ang iyong agent laban sa mga ito sa produksyon, maaari kang mag-set up ng mga fallback o retries. Halimbawa, kung bumagsak ang LLM provider A, maaaring lumipat sa LLM provider B bilang backup.

**Feedback mula sa User:** Ang pagpapatupad ng direktang pagsusuri mula sa mga gumagamit ay nagbibigay ng mahalagang insight. Maaari itong kabilang ang mga hayagang rating (👍thumbs-up/👎down, ⭐1-5 stars) o mga tekstuwal na komento. Ang patuloy na negatibong feedback ay dapat magbigay ng babala dahil ito ay tanda na hindi gumagana nang ayon sa inaasahan ang agent.

**Implicit na Feedback mula sa User:** Nagbibigay ang mga gawi ng gumagamit ng di-tuwirang feedback kahit walang hayagang rating. Maaari itong kabilang ang agad na pagrephrase ng tanong, paulit-ulit na mga query, o pag-click sa retry button. Halimbawa, kung nakikita mong paulit-ulit na tinatanong ng mga user ang parehong tanong, ito ay tanda na hindi gumagana nang ayon sa inaasahan ang agent.

**Katumpakan:** Gaano kadalas gumagawa ng tamang o kanais-nais na output ang agent? Nagkakaiba ang mga kahulugan ng katumpakan (hal., tama sa pagsosolve ng problema, katumpakan sa pagkuha ng impormasyon, kasiyahan ng gumagamit). Ang unang hakbang ay tukuyin kung ano ang itsura ng tagumpay para sa iyong agent. Maaari mong subaybayan ang katumpakan sa pamamagitan ng automated na tseke, mga evaluation score, o mga label ng pagkakatapos ng gawain. Halimbawa, pagmamarka ng mga trace bilang "naging matagumpay" o "nabigo".

**Mga Automated Evaluation Metrics:** Maaari ka ring mag-set up ng automated evals. Halimbawa, maaari kang gumamit ng LLM upang i-score ang output ng agent kung ito ay kapaki-pakinabang, tumpak, o hindi. Mayroon ding ilang open source na library na tumutulong sa pag-score ng iba't ibang aspeto ng agent. Halimbawa, [RAGAS](https://docs.ragas.io/) para sa mga RAG agent o [LLM Guard](https://llm-guard.com/) upang matukoy ang mapanganib na wika o prompt injection.

Sa praktika, ang kumbinasyon ng mga sukatan na ito ang nagbibigay ng pinakamahusay na sakop ng kalusugan ng AI agent. Sa [example notebook](./code_samples/10-expense_claim-demo.ipynb) ng kabanatang ito, ipapakita namin kung paano ganito ang mga sukatan sa mga totoong halimbawa ngunit una, pag-aaralan natin kung ano ang karaniwang workflow ng pagsusuri.

## I-instrument ang iyong Agent

Upang makalap ng tracing data, kailangan mong i-instrument ang iyong code. Layunin nitong i-instrument ang code ng agent upang maglabas ng mga trace at sukatan na maaaring makuha, iproseso, at ipakita ng isang platform ng obserbabilidad.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) ay naging isang industriya-standard para sa obserbabilidad ng LLM. Nagbibigay ito ng set ng mga API, SDK, at mga tool para sa pagbuo, pagkolekta, at pag-export ng telemetry data.

Maraming mga instrumentation library na sumasaklaw sa mga umiiral na framework ng agent na nagpapadali sa pag-export ng OpenTelemetry spans sa isang tool ng obserbabilidad. Native na nakikipag-integrate ang Microsoft Agent Framework sa OpenTelemetry. Narito ang isang halimbawa ng pag-instrument sa isang MAF agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Ang pagsubaybay sa pagpapatupad ng ahente ay awtomatiko
    pass
```

Ang [example notebook](./code_samples/10-expense_claim-demo.ipynb) sa kabanatang ito ay magpapakita kung paano i-instrument ang iyong MAF agent.

**Manual na Paglikha ng Span:** Habang nagbibigay ang mga instrumentation library ng magandang baseline, madalas may mga pagkakataon na kailangan ng mas detalyado o custom na impormasyon. Maaari kang manu-manong gumawa ng spans para magdagdag ng custom na logic sa aplikasyon. Mas mahalaga, maaari nilang pagyamanin ang mga awtomatiko o manwal na span na nilikha ng mga custom attribute (tinatawag ding tag o metadata). Ang mga attribute na ito ay maaaring maglaman ng espesipikong data ng negosyo, mga intermediate na kalkulasyon, o anumang konteksto na maaaring maging kapaki-pakinabang sa pag-debug o pagsusuri, tulad ng `user_id`, `session_id`, o `model_version`.

Halimbawa ng manu-manong paglikha ng mga trace at span gamit ang [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Pagsusuri ng Agent

Nagbibigay ang obserbabilidad sa atin ng mga sukatan, ngunit ang pagsusuri ay ang proseso ng pag-analyze ng data na iyon (at pagsasagawa ng mga pagsusulit) upang matukoy kung gaano kagaling ang pagganap ng AI agent at paano ito mapapabuti. Sa madaling salita, kapag mayroon ka nang mga trace at sukatan, paano mo ito gagamitin upang husgahan ang agent at gumawa ng mga desisyon?

Mahalaga ang regular na pagsusuri dahil madalas na hindi deterministic ang mga AI agent at maaaring magbago (sa mga update o pag-shift ng pag-uugali ng modelo) – kung walang pagsusuri, hindi mo malalaman kung talagang nagagawa nang maayos ng iyong "matalinong agent" ang gawain nito o bumaba na ang kalidad.

May dalawang uri ng pagsusuri para sa AI agent: **online evaluation** at **offline evaluation**. Parehong mahalaga, at nagko-komplemento ang mga ito. Kadalasang nagsisimula tayo sa offline evaluation, dahil ito ang minimum na hakbang bago maglunsad ng anumang agent.

### Offline Evaluation

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Kasama rito ang pagsusuri ng agent sa isang kontroladong kapaligiran, karaniwang gamit ang mga test dataset, hindi aktwal na query ng gumagamit. Ginagamit mo ang mga napiling dataset kung saan alam mo ang inaasahang output o tamang kilos, at tinatakbo mo ang agent sa mga iyon.

Halimbawa, kung gumawa ka ng math word-problem agent, maaaring mayroon kang [test dataset](https://huggingface.co/datasets/gsm8k) na may 100 problema na may kilalang sagot. Karaniwang ginagawa ang offline evaluation habang nasa development pa (at maaaring bahagi ng CI/CD pipeline) upang suriin ang mga pagbuti o maiwasan ang regresyon. Ang benepisyo ay **maalis-ulit ito at makakakuha ka ng malinaw na accuracy metrics dahil mayroon kang ground truth**. Maaari ka ring magsimula ng mga simulation ng user query at sukatin ang mga sagot ng agent laban sa mga ideal na sagot o gumamit ng automated metrics tulad ng nabanggit na.

Ang pangunahing hamon sa offline eval ay tiyakin na komprehensibo at napapanahon ang iyong test dataset – maaaring maganda ang pagganap ng agent sa isang fixed test set ngunit makatagpo ng ibang-ibang query sa produksyon. Kaya dapat mong panatilihing updated ang mga test set gamit ang mga bagong edge cases at halimbawa na tumutugon sa mga totoong senaryo. Kapaki-pakinabang ang halo ng maliit na “smoke test” cases at mas malalaking evaluation sets: maliit para sa mabilisang tseke at malaki para sa malawakang sukatan ng pagganap.

### Online Evaluation

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Tumutukoy ito sa pagsusuri ng agent sa isang live, totoong kapaligiran, ibig sabihin habang aktwal na ginagamit sa produksyon. Kasama sa online evaluation ang pagsubaybay sa pagganap ng agent sa aktwal na interaksyon ng mga gumagamit at tuloy-tuloy na pag-aanalisa ng mga resulta.

Halimbawa, maaaring subaybayan mo ang success rates, mga score ng kasiyahan ng gumagamit, o iba pang sukatan sa live na traffic. Ang kalamangan ng online evaluation ay **nakukuha nito ang mga bagay na maaaring hindi mo inaasahan sa isang lab setting** – maaari mong obserbahan ang pag-shift ng modelo sa paglipas ng panahon (kung bumababa ang bisa ng agent habang nagbabago ang mga pattern ng input) at mahuli ang mga hindi inaasahang query o sitwasyon na wala sa iyong test data. Nagbibigay ito ng tunay na larawan kung paano kumikilos ang agent sa totoong mundo.

Madalas kasama sa online evaluation ang pangongolekta ng implicit at explicit na feedback ng user, gaya ng napagusapan, at maaaring magsagawa ng shadow tests o A/B tests (kung saan ang bagong bersyon ng agent ay tumatakbo kasabay ng lumang bersyon upang maikumpara). Ang hamon ay maaaring mahirap makakuha ng maaasahang label o score para sa live na interaksyon – maaaring umasa ka sa feedback ng gumagamit o downstream metrics (tulad ng kung nag-click ba ang user sa resulta).

### Pagsasama ng dalawa

Hindi magkahiwalay ang online at offline evaluations; lubos silang nagko-komplemento. Ang mga insight mula sa online monitoring (hal., mga bagong uri ng user queries kung saan mahina ang agent) ay maaaring gamitin upang dagdagan at pagbutihin ang offline test datasets. Sa kabilang banda, ang mga agent na mahusay sa offline tests ay maaaring mas kumpiyansang ilunsad at subaybayan online.

Sa katunayan, maraming koponan ang gumagamit ng loop:

_offline evaluation -> deploy -> online monitoring -> kolekta ng bagong failure cases -> idagdag sa offline dataset -> pinuhin ang agent -> ulitin_.

## Mga Karaniwang Isyu

Habang inilulunsad mo ang mga AI agent sa produksyon, maaari kang makatagpo ng iba't ibang hamon. Narito ang ilang karaniwang isyu at posibleng solusyon:

| **Isyu**    | **Posibleng Solusyon**   |
| ------------- | ------------------ |
| Hindi palagian ang pagganap ng AI Agent sa mga gawain | - Pinuhin ang prompt na ibinibigay sa AI Agent; maging malinaw sa mga layunin.<br>- Tukuyin kung saan makakatulong ang paghahati ng mga gawain sa mga subtasks at paghawak ng maraming agent. |
| Paulit-ulit na loop ang AI Agent | - Siguraduhin na may malinaw kang mga termino at kondisyon para sa pagtigil upang malaman ng Agent kung kailan hihinto.<br>- Para sa mga komplikadong gawain na nangangailangan ng reasoning at planning, gumamit ng mas malaking modelo na espesyal na ginawa para sa mga ganitong gawain. |
| Hindi maganda ang pagganap ng mga tawag ng AI Agent sa mga tool | - Subukin at beripikahin ang output ng tool sa labas ng sistema ng agent.<br>- Pinuhin ang mga parameter, prompt, at pangalan ng mga tool. |
| Hindi konsistent ang pagganap ng Multi-Agent system | - Pinuhin ang mga prompt na ibinibigay sa bawat agent upang siguraduhing ito ay espesipiko at naiiba sa isa't isa.<br>- Gumawa ng hierarchical na sistema gamit ang isang "routing" o controller agent upang tukuyin kung alin ang tamang agent. |

Marami sa mga isyung ito ay mas madaling matukoy kung may obserbabilidad. Ang mga trace at sukatan na napag-usapan natin ay tumutulong tukuyin nang tukoy kung saan sa workflow ng agent nagkakaroon ng problema, kaya't mas epektibo ang pag-debug at pag-optimize.

## Pamamahala ng Gastos


Narito ang ilang mga estratehiya upang pamahalaan ang mga gastos sa pag-deploy ng mga AI agents sa produksyon:

**Paggamit ng Mas Maliit na Modelo:** Ang Maliit na Language Models (SLMs) ay maaaring gumana nang maayos sa ilang mga use-case ng agentic at makakabawas nang malaki sa mga gastos. Tulad ng nabanggit kanina, ang paggawa ng isang evaluation system upang tukuyin at ikumpara ang performance laban sa mas malalaking modelo ang pinakamainam na paraan upang maintindihan kung gaano kabilis at kahusay ang isang SLM sa iyong use case. Isaalang-alang ang paggamit ng SLM para sa mga mas simpleng gawain tulad ng intent classification o parameter extraction, habang inilalaan naman ang mas malalaking modelo para sa mga kumplikadong reasoning.

**Paggamit ng Router Model:** Isang katulad na estratehiya ang paggamit ng iba’t ibang mga modelo at sukat. Maaari kang gumamit ng LLM/SLM o serverless function upang i-route ang mga request batay sa komplikasyon patungo sa mga pinakaangkop na modelo. Makakatulong din ito upang mapababa ang mga gastos habang tinitiyak ang performance sa tamang mga gawain. Halimbawa, i-route ang mga simpleng query sa mas maliit, mas mabilis na mga modelo, at gamitin lamang ang mahal na malalaking modelo para sa mga kumplikadong gawain ng reasoning.

**Pag-cache ng Mga Tugon:** Ang pagtukoy sa mga karaniwang request at gawain at pagbibigay ng mga tugon bago pa ito dumaan sa iyong agentic system ay isang magandang paraan upang mabawasan ang dami ng magkakatulad na mga request. Maaari mo pang ipatupad ang isang flow upang tukuyin kung gaano kasimilar ang isang request sa iyong mga naka-cache na request gamit ang mga mas batayang AI models. Ang estratehiyang ito ay maaaring makabawas nang malaki sa mga gastos para sa mga madalas itanong na mga tanong o karaniwang workflows.

## Tingnan natin kung paano ito gumagana sa praktika

Sa [example notebook ng seksyong ito](./code_samples/10-expense_claim-demo.ipynb), makikita natin ang mga halimbawa kung paano natin magagamit ang mga observability tools upang subaybayan at suriin ang ating agent.


### May Karagdagang Mga Tanong tungkol sa AI Agents sa Produksyon?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipagkita sa iba pang mga nag-aaral, dumalo sa office hours at sagutin ang iyong mga tanong tungkol sa AI Agents.

## Nakaraang Aralin

[Metacognition Design Pattern](../09-metacognition/README.md)

## Susunod na Aralin

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->