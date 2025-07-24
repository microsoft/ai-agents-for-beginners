<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-24T08:50:31+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "tl"
}
-->
# AI Agents sa Produksyon: Observability at Pagsusuri

Habang ang mga AI agent ay lumilipat mula sa mga eksperimento patungo sa mga tunay na aplikasyon, nagiging mahalaga ang kakayahang maunawaan ang kanilang pag-uugali, subaybayan ang kanilang performance, at sistematikong suriin ang kanilang mga output.

## Mga Layunin sa Pagkatuto

Pagkatapos ng araling ito, malalaman mo kung paano/maiintindihan mo:
- Mga pangunahing konsepto ng observability at pagsusuri ng agent
- Mga teknik para mapabuti ang performance, gastos, at pagiging epektibo ng mga agent
- Ano at paano sistematikong suriin ang iyong mga AI agent
- Paano kontrolin ang gastos kapag nagde-deploy ng AI agent sa produksyon
- Paano mag-instrument ng mga agent gamit ang AutoGen

Ang layunin ay bigyan ka ng kaalaman upang gawing transparent, madaling pamahalaan, at maaasahang sistema ang iyong mga "black box" na agent.

_**Tandaan:** Mahalagang mag-deploy ng mga AI Agent na ligtas at mapagkakatiwalaan. Tingnan ang aralin na [Pagbuo ng Mapagkakatiwalaang AI Agent](./06-building-trustworthy-agents/README.md) para sa karagdagang impormasyon._

## Mga Traces at Spans

Ang mga observability tool tulad ng [Langfuse](https://langfuse.com/) o [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) ay karaniwang nagrerepresenta ng mga takbo ng agent bilang traces at spans.

- **Trace** ay kumakatawan sa isang kumpletong gawain ng agent mula simula hanggang matapos (halimbawa, paghawak ng query ng user).
- **Spans** ay mga indibidwal na hakbang sa loob ng trace (halimbawa, pagtawag sa isang language model o pagkuha ng data).

![Trace tree sa Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Kung walang observability, ang isang AI agent ay maaaring magmukhang "black box" - ang panloob na estado at pangangatwiran nito ay hindi malinaw, na nagpapahirap sa pag-diagnose ng mga isyu o pag-optimize ng performance. Sa tulong ng observability, nagiging "glass box" ang mga agent, na nagbibigay ng transparency na mahalaga para sa pagtitiwala at pagtiyak na gumagana ang mga ito ayon sa inaasahan.

## Bakit Mahalaga ang Observability sa Mga Kapaligiran ng Produksyon

Ang paglipat ng mga AI agent sa produksyon ay nagdadala ng mga bagong hamon at pangangailangan. Ang observability ay hindi na isang "nice-to-have" kundi isang kritikal na kakayahan:

*   **Pag-debug at Root-Cause Analysis**: Kapag nabigo ang isang agent o nagbigay ng hindi inaasahang output, nagbibigay ang mga observability tool ng mga trace na kailangan upang matukoy ang pinagmulan ng error. Mahalaga ito lalo na sa mga kumplikadong agent na maaaring may kasamang maraming LLM calls, tool interactions, at conditional logic.
*   **Pamamahala ng Latency at Gastos**: Ang mga AI agent ay madalas na umaasa sa mga LLM at iba pang external APIs na binabayaran kada token o tawag. Ang observability ay nagbibigay-daan sa tumpak na pagsubaybay sa mga tawag na ito, na tumutulong upang matukoy ang mga operasyong masyadong mabagal o magastos. Sa ganitong paraan, maaaring i-optimize ang mga prompt, pumili ng mas epektibong modelo, o muling idisenyo ang mga workflow upang pamahalaan ang gastos at tiyakin ang magandang karanasan ng user.
*   **Tiwala, Kaligtasan, at Pagsunod**: Sa maraming aplikasyon, mahalagang tiyakin na ang mga agent ay kumikilos nang ligtas at etikal. Ang observability ay nagbibigay ng audit trail ng mga aksyon at desisyon ng agent. Maaari itong gamitin upang matukoy at maibsan ang mga isyu tulad ng prompt injection, pagbuo ng mapanganib na nilalaman, o maling paghawak ng personal na impormasyon (PII). Halimbawa, maaari mong suriin ang mga trace upang maunawaan kung bakit nagbigay ang isang agent ng partikular na sagot o gumamit ng isang tiyak na tool.
*   **Mga Loop para sa Patuloy na Pagpapabuti**: Ang data mula sa observability ay pundasyon ng isang iterative na proseso ng pag-develop. Sa pamamagitan ng pagsubaybay kung paano gumagana ang mga agent sa totoong mundo, maaaring matukoy ng mga team ang mga lugar na kailangang pagbutihin, mangolekta ng data para sa fine-tuning ng mga modelo, at i-validate ang epekto ng mga pagbabago. Lumilikha ito ng feedback loop kung saan ang mga insight mula sa online evaluation ay nagbibigay-kaalaman sa offline experimentation at refinement, na humahantong sa unti-unting pagpapabuti ng performance ng agent.

## Mga Pangunahing Sukatan na Dapat Subaybayan

Upang masubaybayan at maunawaan ang pag-uugali ng agent, kailangang subaybayan ang iba't ibang sukatan at signal. Bagama't maaaring mag-iba ang mga partikular na sukatan batay sa layunin ng agent, may ilang mahalaga sa lahat ng pagkakataon.

Narito ang ilan sa mga karaniwang sukatan na sinusubaybayan ng mga observability tool:

**Latency:** Gaano kabilis tumugon ang agent? Ang mahabang oras ng paghihintay ay negatibong nakakaapekto sa karanasan ng user. Dapat sukatin ang latency para sa mga gawain at indibidwal na hakbang sa pamamagitan ng pag-trace ng mga takbo ng agent. Halimbawa, ang isang agent na tumatagal ng 20 segundo para sa lahat ng model calls ay maaaring pabilisin sa pamamagitan ng paggamit ng mas mabilis na modelo o sa pamamagitan ng sabay-sabay na pagpapatakbo ng mga model calls.

**Gastos:** Magkano ang gastos kada takbo ng agent? Ang mga AI agent ay umaasa sa mga LLM calls na binabayaran kada token o external APIs. Ang madalas na paggamit ng tool o maraming prompt ay maaaring mabilis na magpataas ng gastos. Halimbawa, kung ang isang agent ay tumatawag sa LLM ng limang beses para sa bahagyang pagpapabuti ng kalidad, kailangang suriin kung sulit ang gastos o kung maaaring bawasan ang bilang ng mga tawag o gumamit ng mas murang modelo. Ang real-time na pagsubaybay ay maaari ring makatulong na matukoy ang mga hindi inaasahang pagtaas ng gastos (halimbawa, mga bug na nagdudulot ng labis na API loops).

**Mga Error sa Request:** Ilang request ang nabigo ang agent? Maaaring kabilang dito ang mga error sa API o nabigong tawag sa tool. Upang gawing mas matatag ang iyong agent laban sa mga ito sa produksyon, maaari kang mag-set up ng mga fallback o retries. Halimbawa, kung ang LLM provider A ay hindi gumagana, lilipat sa LLM provider B bilang backup.

**Feedback ng User:** Ang pagpapatupad ng direktang pagsusuri mula sa user ay nagbibigay ng mahalagang insight. Maaaring kabilang dito ang mga explicit na rating (👍thumbs-up/👎down, ⭐1-5 stars) o mga komento. Ang patuloy na negatibong feedback ay dapat magbigay ng babala dahil ito ay senyales na hindi gumagana ang agent ayon sa inaasahan.

**Implicit na Feedback ng User:** Ang mga pag-uugali ng user ay nagbibigay ng hindi direktang feedback kahit walang explicit na rating. Maaaring kabilang dito ang agarang pag-rephrase ng tanong, paulit-ulit na query, o pag-click sa retry button. Halimbawa, kung makikita mong paulit-ulit na tinatanong ng mga user ang parehong tanong, ito ay senyales na hindi gumagana ang agent ayon sa inaasahan.

**Katumpakan:** Gaano kadalas nagbibigay ang agent ng tamang o kanais-nais na output? Ang mga depinisyon ng katumpakan ay nag-iiba-iba (halimbawa, tamang pagsagot sa problema, katumpakan ng impormasyon, kasiyahan ng user). Ang unang hakbang ay tukuyin kung ano ang hitsura ng tagumpay para sa iyong agent. Maaari mong subaybayan ang katumpakan sa pamamagitan ng automated na pagsusuri, mga evaluation score, o mga label ng pagkumpleto ng gawain. Halimbawa, pagmamarka ng mga trace bilang "naging matagumpay" o "nabigo."

**Automated Evaluation Metrics:** Maaari ka ring mag-set up ng automated na pagsusuri. Halimbawa, maaari mong gamitin ang isang LLM upang i-score ang output ng agent, halimbawa kung ito ay kapaki-pakinabang, tumpak, o hindi. Mayroon ding ilang open-source na library na tumutulong sa pag-score ng iba't ibang aspeto ng agent. Halimbawa, [RAGAS](https://docs.ragas.io/) para sa mga RAG agent o [LLM Guard](https://llm-guard.com/) upang matukoy ang mapanganib na wika o prompt injection.

Sa praktika, ang kombinasyon ng mga sukatan na ito ang nagbibigay ng pinakamahusay na coverage ng kalusugan ng AI agent. Sa [halimbawang notebook](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) ng kabanatang ito, ipapakita namin kung paano ang mga sukatan na ito ay makikita sa mga tunay na halimbawa, ngunit una, pag-aaralan natin kung paano ang hitsura ng isang tipikal na workflow ng pagsusuri.

## I-instrument ang Iyong Agent

Upang makalikom ng tracing data, kailangan mong i-instrument ang iyong code. Ang layunin ay i-instrument ang code ng agent upang maglabas ng mga trace at sukatan na maaaring makuha, maproseso, at maipakita ng isang observability platform.

**OpenTelemetry (OTel):** Ang [OpenTelemetry](https://opentelemetry.io/) ay naging pamantayan sa industriya para sa observability ng LLM. Nagbibigay ito ng hanay ng mga API, SDK, at tool para sa pagbuo, pagkolekta, at pag-export ng telemetry data.

Maraming instrumentation library na nag-e-encapsulate ng mga umiiral na framework ng agent at ginagawang madali ang pag-export ng OpenTelemetry spans sa isang observability tool. Narito ang isang halimbawa ng pag-instrument ng isang AutoGen agent gamit ang [OpenLit instrumentation library](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

Ang [halimbawang notebook](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) sa kabanatang ito ay magpapakita kung paano i-instrument ang iyong AutoGen agent.

**Manwal na Paglikha ng Span:** Bagama't ang mga instrumentation library ay nagbibigay ng magandang baseline, may mga pagkakataon kung saan kinakailangan ang mas detalyado o custom na impormasyon. Maaari kang manu-manong lumikha ng mga span upang magdagdag ng custom na lohika ng aplikasyon. Higit sa lahat, maaari nilang pagyamanin ang mga awtomatiko o manu-manong nilikhang span gamit ang mga custom na attribute (kilala rin bilang mga tag o metadata). Ang mga attribute na ito ay maaaring magsama ng data na partikular sa negosyo, intermediate na kalkulasyon, o anumang konteksto na maaaring maging kapaki-pakinabang para sa pag-debug o pagsusuri, tulad ng `user_id`, `session_id`, o `model_version`.

Halimbawa ng manu-manong paglikha ng mga trace at span gamit ang [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Pagsusuri ng Agent

Ang observability ay nagbibigay sa atin ng mga sukatan, ngunit ang pagsusuri ay ang proseso ng pagsusuri ng data na iyon (at pagsasagawa ng mga pagsusuri) upang matukoy kung gaano kahusay ang performance ng isang AI agent at kung paano ito mapapabuti. Sa madaling salita, kapag mayroon ka nang mga trace at sukatan, paano mo ito gagamitin upang husgahan ang agent at gumawa ng mga desisyon?

Mahalaga ang regular na pagsusuri dahil ang mga AI agent ay madalas na hindi deterministiko at maaaring magbago (sa pamamagitan ng mga update o pagbabago sa pag-uugali ng modelo) – kung walang pagsusuri, hindi mo malalaman kung ang iyong "matalinong agent" ay talagang gumagawa ng maayos na trabaho o kung ito ay bumaba ang kalidad.

May dalawang kategorya ng pagsusuri para sa mga AI agent: **offline evaluation** at **online evaluation**. Pareho silang mahalaga at nagkakatuwang. Karaniwan, nagsisimula tayo sa offline evaluation, dahil ito ang minimum na kinakailangang hakbang bago mag-deploy ng anumang agent.

### Offline Evaluation

![Mga item ng dataset sa Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Kasama rito ang pagsusuri ng agent sa isang kontroladong kapaligiran, karaniwang gamit ang mga test dataset, hindi mga live na query ng user. Gumagamit ka ng mga curated dataset kung saan alam mo ang inaasahang output o tamang pag-uugali, at pagkatapos ay patakbuhin ang iyong agent sa mga ito.

Halimbawa, kung gumawa ka ng isang agent para sa mga math word-problem, maaari kang magkaroon ng isang [test dataset](https://huggingface.co/datasets/gsm8k) na may 100 problema na may kilalang sagot. Ang offline evaluation ay karaniwang ginagawa sa panahon ng pag-develop (at maaaring maging bahagi ng CI/CD pipelines) upang suriin ang mga pagpapabuti o maiwasan ang mga regression. Ang benepisyo nito ay **maaaring ulitin at makakakuha ka ng malinaw na mga sukatan ng katumpakan dahil mayroon kang ground truth**. Maaari ka ring magsagawa ng simulation ng mga query ng user at sukatin ang mga tugon ng agent laban sa mga ideal na sagot o gumamit ng mga automated na sukatan tulad ng nabanggit sa itaas.

Ang pangunahing hamon sa offline evaluation ay tiyakin na ang iyong test dataset ay komprehensibo at nananatiling may kaugnayan – maaaring mag-perform nang maayos ang agent sa isang nakapirming test set ngunit makaharap ng napakaibang mga query sa produksyon. Samakatuwid, dapat mong panatilihing updated ang mga test set gamit ang mga bagong edge case at halimbawa na sumasalamin sa mga tunay na sitwasyon​. Ang kombinasyon ng maliliit na "smoke test" na kaso at mas malalaking evaluation set ay kapaki-pakinabang: maliliit na set para sa mabilisang pagsusuri at mas malalaking set para sa mas malawak na sukatan ng performance​.

### Online Evaluation 

![Pangkalahatang-ideya ng mga observability metrics](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ito ay tumutukoy sa pagsusuri ng agent sa isang live, tunay na kapaligiran, ibig sabihin, sa aktwal na paggamit sa produksyon. Ang online evaluation ay kinabibilangan ng pagsubaybay sa performance ng agent sa mga tunay na interaksyon ng user at patuloy na pagsusuri ng mga resulta.

Halimbawa, maaari mong subaybayan ang mga success rate, mga score ng kasiyahan ng user, o iba pang sukatan sa live na trapiko. Ang bentahe ng online evaluation ay **nahuhuli nito ang mga bagay na maaaring hindi mo inaasahan sa isang lab setting** – maaari mong obserbahan ang model drift sa paglipas ng panahon (kung bumababa ang bisa ng agent habang nagbabago ang mga pattern ng input) at mahuli ang mga hindi inaasahang query o sitwasyon na wala sa iyong test data​. Nagbibigay ito ng tunay na larawan kung paano kumikilos ang agent sa totoong mundo.

Ang online evaluation ay madalas na kinabibilangan ng pagkolekta ng implicit at explicit na feedback ng user, tulad ng nabanggit, at posibleng pagsasagawa ng shadow tests o A/B tests (kung saan ang isang bagong bersyon ng agent ay tumatakbo nang sabay upang ihambing sa luma). Ang hamon ay maaaring mahirap makakuha ng maaasahang mga label o score para sa mga live na interaksyon – maaaring umasa ka sa feedback ng user o mga downstream metrics (halimbawa, kung nag-click ba ang user sa resulta).

### Pagsasama ng Dalawa

Ang online at offline evaluation ay hindi magkasalungat; sila ay lubos na nagkakatuwang. Ang mga insight mula sa online monitoring (halimbawa, mga bagong uri ng query ng user kung saan mahina ang performance ng agent) ay maaaring gamitin upang mapahusay at mapabuti ang mga offline test dataset. Sa kabilang banda, ang mga agent na mahusay ang performance sa offline tests ay mas may kumpiyansang ma-deploy at masubaybayan online.

Sa katunayan, maraming team ang gumagamit ng loop:

_evaluate offline -> deploy -> monitor online -> collect new failure cases -> add to offline dataset -> refine agent -> repeat_.

## Mga Karaniwang Isyu

Habang nagde-deploy ka ng mga AI agent sa produksyon, maaaring makaharap ka ng iba't ibang hamon. Narito ang ilang karaniwang isyu at ang kanilang posibleng solusyon:

| **Isyu**    | **Posibleng Solusyon**   |
| ------------- | ------------------ |
| Hindi palaging nagagawa ng AI Agent ang mga gawain nang maayos | - Pinuhin ang prompt na ibinibigay sa AI Agent; gawing malinaw ang mga layunin.<br>- Tukuyin kung saan makakatulong ang paghahati ng mga gawain sa mas maliliit na bahagi at paghawak ng mga ito ng maraming agent. |
| Ang AI Agent ay nauuwi sa tuloy-tuloy na mga loop  | - Tiyakin na mayroon kang malinaw na mga tuntunin at kundisyon ng pagtatapos upang malaman ng Agent kung kailan titigil.<br>- Para sa mga kumplikadong gawain na nangangailangan ng pangangatwiran at pagpaplano, gumamit ng mas malaking modelo na dalubhasa sa mga reasoning task. |
| Hindi mahusay ang performance ng mga tool calls ng AI Agent   | - Subukan at i-validate ang output ng tool sa labas ng sistema ng agent. |

- Pinuhin ang mga itinakdang parameter, mga prompt, at pangalan ng mga tool.  |
| Hindi palaging maayos ang pagganap ng Multi-Agent system | - Pinuhin ang mga prompt na ibinibigay sa bawat agent upang masigurong tiyak at naiiba ang mga ito sa isa't isa.<br>- Bumuo ng hierarchical system gamit ang isang "routing" o controller agent upang matukoy kung aling agent ang tamang gamitin. |

Maraming sa mga isyung ito ang mas madaling matukoy kung may observability. Ang mga traces at metrics na tinalakay natin kanina ay tumutulong upang matukoy nang eksakto kung saan sa workflow ng agent nagkakaroon ng problema, na nagpapadali sa debugging at optimization.

## Pamamahala ng Gastos

Narito ang ilang estratehiya upang pamahalaan ang gastos ng pag-deploy ng AI agents sa production:

**Paggamit ng Mas Maliit na Modelo:** Ang Small Language Models (SLMs) ay maaaring magbigay ng mahusay na performance sa ilang agentic use-cases at makakabawas nang malaki sa gastos. Tulad ng nabanggit kanina, ang pagbuo ng evaluation system upang matukoy at maikumpara ang performance laban sa mas malalaking modelo ang pinakamainam na paraan upang maunawaan kung gaano kahusay ang magiging performance ng SLM sa iyong use case. Isaalang-alang ang paggamit ng SLMs para sa mas simpleng gawain tulad ng intent classification o parameter extraction, habang itinatabi ang mas malalaking modelo para sa mas kumplikadong reasoning.

**Paggamit ng Router Model:** Isang katulad na estratehiya ay ang paggamit ng iba't ibang modelo at laki. Maaari kang gumamit ng LLM/SLM o serverless function upang i-route ang mga request batay sa complexity sa mga modelong pinakaangkop. Makakatulong din ito sa pagbawas ng gastos habang sinisiguro ang performance sa tamang gawain. Halimbawa, i-route ang mga simpleng query sa mas maliit at mas mabilis na modelo, at gamitin lamang ang mahal na malalaking modelo para sa mas kumplikadong reasoning tasks.

**Caching Responses:** Ang pagtukoy sa mga karaniwang request at gawain at pagbibigay ng mga sagot bago pa ito dumaan sa iyong agentic system ay isang mahusay na paraan upang mabawasan ang dami ng magkakatulad na request. Maaari ka ring magpatupad ng flow upang matukoy kung gaano kahawig ang isang request sa iyong mga naka-cache na request gamit ang mas basic na AI models. Ang estratehiyang ito ay maaaring makabawas nang malaki sa gastos para sa mga madalas itanong o karaniwang workflows.

## Tingnan Natin Kung Paano Ito Gumagana sa Praktika

Sa [halimbawang notebook ng seksyong ito](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb), makikita natin ang mga halimbawa kung paano natin magagamit ang mga observability tools upang i-monitor at i-evaluate ang ating agent.

## Nakaraang Aralin

[Metacognition Design Pattern](../09-metacognition/README.md)

## Susunod na Aralin

[MCP](../11-mcp/README.md)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi eksaktong salin. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.