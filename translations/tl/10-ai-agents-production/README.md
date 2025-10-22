<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cdfd0acc8592c1af14f8637833450375",
  "translation_date": "2025-08-29T09:44:48+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "tl"
}
-->
# AI Agents sa Produksyon: Pagmamasid at Pagsusuri

[![AI Agents sa Produksyon](../../../translated_images/lesson-10-thumbnail.2b79a30773db093e0b4fb47aaa618069e0afb4745fad4836526cf51df87f9ac9.tl.png)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Habang ang mga AI agent ay lumilipat mula sa mga eksperimento patungo sa mga tunay na aplikasyon, nagiging mahalaga ang kakayahang maunawaan ang kanilang pag-uugali, subaybayan ang kanilang pagganap, at sistematikong suriin ang kanilang mga output.

## Mga Layunin sa Pag-aaral

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano/maiintindihan:
- Mga pangunahing konsepto ng pagmamasid at pagsusuri ng agent
- Mga teknik para mapabuti ang pagganap, gastos, at bisa ng mga agent
- Ano at paano sistematikong suriin ang iyong mga AI agent
- Paano kontrolin ang gastos kapag inilalagay ang mga AI agent sa produksyon
- Paano maglagay ng mga instrumento sa mga agent na ginawa gamit ang AutoGen

Ang layunin ay bigyan ka ng kaalaman upang gawing transparent, maayos, at maaasahang sistema ang iyong mga "black box" agent.

_**Tandaan:** Mahalagang mag-deploy ng mga AI Agent na ligtas at mapagkakatiwalaan. Tingnan ang araling [Pagbuo ng Mapagkakatiwalaang AI Agents](./06-building-trustworthy-agents/README.md)._

## Mga Traces at Spans

Ang mga tool sa pagmamasid tulad ng [Langfuse](https://langfuse.com/) o [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) ay karaniwang kumakatawan sa mga takbo ng agent bilang traces at spans.

- **Trace** ay kumakatawan sa kumpletong gawain ng agent mula simula hanggang matapos (halimbawa, paghawak ng tanong ng user).
- **Spans** ay mga indibidwal na hakbang sa loob ng trace (halimbawa, pagtawag sa isang language model o pagkuha ng data).

![Trace tree sa Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Kung walang pagmamasid, ang isang AI agent ay maaaring magmukhang "black box" - ang panloob na estado at pangangatwiran nito ay hindi malinaw, na nagpapahirap sa pag-diagnose ng mga isyu o pag-optimize ng pagganap. Sa pagmamasid, ang mga agent ay nagiging "glass boxes," na nagbibigay ng transparency na mahalaga para sa pagbuo ng tiwala at pagtiyak na gumagana sila ayon sa inaasahan.

## Bakit Mahalaga ang Pagmamasid sa Mga Kapaligiran ng Produksyon

Ang paglipat ng mga AI agent sa mga kapaligiran ng produksyon ay nagdadala ng bagong hanay ng mga hamon at pangangailangan. Ang pagmamasid ay hindi na "maganda kung meron" kundi isang kritikal na kakayahan:

*   **Pag-debug at Pagsusuri ng Ugat ng Problema**: Kapag ang isang agent ay nabigo o nagbigay ng hindi inaasahang output, ang mga tool sa pagmamasid ay nagbibigay ng mga trace na kailangan upang matukoy ang pinagmulan ng error. Ito ay lalong mahalaga sa mga kumplikadong agent na maaaring may kasamang maraming LLM calls, tool interactions, at conditional logic.
*   **Pamamahala ng Latency at Gastos**: Ang mga AI agent ay madalas na umaasa sa LLMs at iba pang external APIs na binabayaran kada token o tawag. Ang pagmamasid ay nagbibigay-daan sa tumpak na pagsubaybay sa mga tawag na ito, na tumutulong upang matukoy ang mga operasyon na sobrang bagal o mahal. Pinapayagan nito ang mga team na i-optimize ang mga prompt, pumili ng mas mahusay na mga modelo, o muling idisenyo ang mga workflow upang pamahalaan ang mga operational cost at tiyakin ang magandang karanasan ng user.
*   **Tiwala, Kaligtasan, at Pagsunod**: Sa maraming aplikasyon, mahalagang tiyakin na ang mga agent ay kumikilos nang ligtas at etikal. Ang pagmamasid ay nagbibigay ng audit trail ng mga aksyon at desisyon ng agent. Maaari itong gamitin upang matukoy at mabawasan ang mga isyu tulad ng prompt injection, pagbuo ng mapanganib na nilalaman, o maling paghawak ng personal na impormasyon (PII). Halimbawa, maaari mong suriin ang mga trace upang maunawaan kung bakit nagbigay ang isang agent ng partikular na sagot o gumamit ng isang tiyak na tool.
*   **Mga Loop ng Patuloy na Pagpapabuti**: Ang data ng pagmamasid ay ang pundasyon ng isang iterative na proseso ng pag-develop. Sa pamamagitan ng pagsubaybay kung paano gumagana ang mga agent sa totoong mundo, maaaring matukoy ng mga team ang mga lugar para sa pagpapabuti, mangolekta ng data para sa fine-tuning ng mga modelo, at i-validate ang epekto ng mga pagbabago. Lumilikha ito ng feedback loop kung saan ang mga insight sa produksyon mula sa online evaluation ay nagbibigay-alam sa offline experimentation at refinement, na humahantong sa progresibong mas mahusay na pagganap ng agent.

## Mga Pangunahing Sukatan na Dapat Subaybayan

Upang masubaybayan at maunawaan ang pag-uugali ng agent, dapat subaybayan ang iba't ibang sukatan at signal. Bagama't maaaring mag-iba ang mga partikular na sukatan batay sa layunin ng agent, may ilang mahalaga sa lahat.

Narito ang ilan sa mga pinaka-karaniwang sukatan na sinusubaybayan ng mga tool sa pagmamasid:

**Latency:** Gaano kabilis tumugon ang agent? Ang mahabang oras ng paghihintay ay negatibong nakakaapekto sa karanasan ng user. Dapat mong sukatin ang latency para sa mga gawain at indibidwal na hakbang sa pamamagitan ng pag-trace ng mga takbo ng agent. Halimbawa, ang isang agent na tumatagal ng 20 segundo para sa lahat ng model calls ay maaaring mapabilis sa pamamagitan ng paggamit ng mas mabilis na modelo o sa pamamagitan ng sabay-sabay na pagpapatakbo ng mga model calls.

**Gastos:** Ano ang gastos kada takbo ng agent? Ang mga AI agent ay umaasa sa mga LLM calls na binabayaran kada token o external APIs. Ang madalas na paggamit ng tool o maraming prompt ay maaaring mabilis na magpataas ng gastos. Halimbawa, kung ang isang agent ay tumatawag sa LLM ng limang beses para sa marginal na pagpapabuti ng kalidad, dapat mong suriin kung ang gastos ay sulit o kung maaari mong bawasan ang bilang ng mga tawag o gumamit ng mas murang modelo. Ang real-time monitoring ay maaari ring makatulong na matukoy ang hindi inaasahang pagtaas (halimbawa, mga bug na nagdudulot ng labis na API loops).

**Mga Error sa Request:** Ilang request ang nabigo ng agent? Kasama dito ang mga error sa API o nabigong tawag sa tool. Upang gawing mas matatag ang iyong agent laban sa mga ito sa produksyon, maaari kang mag-set up ng mga fallback o retries. Halimbawa, kung ang LLM provider A ay hindi gumagana, maaari kang lumipat sa LLM provider B bilang backup.

**Feedback ng User:** Ang pagpapatupad ng direktang pagsusuri ng user ay nagbibigay ng mahalagang insight. Kasama dito ang mga explicit na rating (👍thumbs-up/👎down, ⭐1-5 stars) o mga komentong tekstwal. Ang patuloy na negatibong feedback ay dapat magbigay ng babala dahil ito ay senyales na ang agent ay hindi gumagana ayon sa inaasahan.

**Implicit na Feedback ng User:** Ang mga pag-uugali ng user ay nagbibigay ng hindi direktang feedback kahit walang explicit na rating. Kasama dito ang agarang pag-rephrase ng tanong, paulit-ulit na query, o pag-click sa retry button. Halimbawa, kung nakikita mong paulit-ulit na tinatanong ng mga user ang parehong tanong, ito ay senyales na ang agent ay hindi gumagana ayon sa inaasahan.

**Katumpakan:** Gaano kadalas nagbibigay ang agent ng tamang o kanais-nais na output? Ang mga kahulugan ng katumpakan ay nag-iiba (halimbawa, tamang pagsagot sa problema, katumpakan ng pagkuha ng impormasyon, kasiyahan ng user). Ang unang hakbang ay tukuyin kung ano ang hitsura ng tagumpay para sa iyong agent. Maaari mong subaybayan ang katumpakan sa pamamagitan ng automated na pagsusuri, mga evaluation score, o mga label ng pagkumpleto ng gawain. Halimbawa, pagmamarka ng mga trace bilang "nagtagumpay" o "nabigo."

**Automated Evaluation Metrics:** Maaari ka ring mag-set up ng automated evals. Halimbawa, maaari mong gamitin ang isang LLM upang i-score ang output ng agent, halimbawa kung ito ay kapaki-pakinabang, tumpak, o hindi. Mayroon ding ilang open source libraries na tumutulong sa pag-score ng iba't ibang aspeto ng agent. Halimbawa, [RAGAS](https://docs.ragas.io/) para sa mga RAG agent o [LLM Guard](https://llm-guard.com/) upang matukoy ang mapanganib na wika o prompt injection.

Sa praktika, ang kombinasyon ng mga sukatan na ito ang nagbibigay ng pinakamahusay na coverage ng kalusugan ng AI agent. Sa [halimbawang notebook](./code_samples/10_autogen_evaluation.ipynb) ng kabanatang ito, ipapakita namin kung paano ang mga sukatan na ito ay mukhang sa mga tunay na halimbawa ngunit una, matututo tayo kung paano ang isang tipikal na workflow ng pagsusuri.

## Instrumento ang Iyong Agent

Upang makalikom ng tracing data, kailangan mong maglagay ng mga instrumento sa iyong code. Ang layunin ay instrumentuhin ang code ng agent upang maglabas ng mga trace at sukatan na maaaring makuha, maproseso, at maipakita ng isang platform ng pagmamasid.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) ay lumitaw bilang pamantayan ng industriya para sa pagmamasid sa LLM. Nagbibigay ito ng hanay ng mga API, SDK, at tool para sa pagbuo, pagkolekta, at pag-export ng telemetry data.

Maraming mga instrumentation libraries na nag-wrap sa mga umiiral na agent frameworks at ginagawang madali ang pag-export ng OpenTelemetry spans sa isang tool sa pagmamasid. Narito ang isang halimbawa ng pag-instrument ng isang AutoGen agent gamit ang [OpenLit instrumentation library](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

Ang [halimbawang notebook](./code_samples/10_autogen_evaluation.ipynb) sa kabanatang ito ay magpapakita kung paano mag-instrument ng iyong AutoGen agent.

**Manwal na Paglikha ng Span:** Bagama't ang mga instrumentation libraries ay nagbibigay ng magandang baseline, may mga kaso kung saan mas detalyado o custom na impormasyon ang kinakailangan. Maaari kang manu-manong lumikha ng mga span upang magdagdag ng custom na application logic. Mas mahalaga, maaari nilang pagyamanin ang awtomatiko o manu-manong nilikhang mga span gamit ang mga custom na attribute (kilala rin bilang mga tag o metadata). Ang mga attribute na ito ay maaaring magsama ng business-specific na data, intermediate computations, o anumang konteksto na maaaring maging kapaki-pakinabang para sa pag-debug o pagsusuri, tulad ng `user_id`, `session_id`, o `model_version`.

Halimbawa ng manu-manong paglikha ng mga trace at span gamit ang [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Pagsusuri ng Agent

Ang pagmamasid ay nagbibigay sa atin ng mga sukatan, ngunit ang pagsusuri ay ang proseso ng pag-aaral ng data na iyon (at pagsasagawa ng mga pagsusuri) upang matukoy kung gaano kahusay ang pagganap ng isang AI agent at kung paano ito mapapabuti. Sa madaling salita, kapag mayroon ka nang mga trace at sukatan, paano mo ito gagamitin upang husgahan ang agent at gumawa ng mga desisyon?

Ang regular na pagsusuri ay mahalaga dahil ang mga AI agent ay madalas na hindi deterministiko at maaaring mag-evolve (sa pamamagitan ng mga update o pagbabago sa pag-uugali ng modelo) – kung walang pagsusuri, hindi mo malalaman kung ang iyong "matalinong agent" ay talagang gumagawa ng trabaho nito nang maayos o kung ito ay bumaba ang kalidad.

Mayroong dalawang kategorya ng pagsusuri para sa mga AI agent: **offline evaluation** at **online evaluation**. Parehong mahalaga, at sila ay nagkakatuwang. Karaniwan tayong nagsisimula sa offline evaluation, dahil ito ang minimum na kinakailangang hakbang bago i-deploy ang anumang agent.

### Offline Evaluation

![Mga item ng dataset sa Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Kasama dito ang pagsusuri sa agent sa isang kontroladong setting, karaniwang gamit ang mga test dataset, hindi mga live na query ng user. Gumagamit ka ng mga curated dataset kung saan alam mo kung ano ang inaasahang output o tamang pag-uugali, at pagkatapos ay patakbuhin ang iyong agent sa mga ito.

Halimbawa, kung gumawa ka ng isang math word-problem agent, maaaring mayroon kang [test dataset](https://huggingface.co/datasets/gsm8k) ng 100 problema na may kilalang mga sagot. Ang offline evaluation ay madalas na ginagawa sa panahon ng pag-develop (at maaaring bahagi ng CI/CD pipelines) upang suriin ang mga pagpapabuti o protektahan laban sa mga regression. Ang benepisyo ay **maaaring ulitin at makakakuha ka ng malinaw na mga sukatan ng katumpakan dahil mayroon kang ground truth**. Maaari mo ring gayahin ang mga query ng user at sukatin ang mga tugon ng agent laban sa mga ideal na sagot o gumamit ng mga automated na sukatan tulad ng inilarawan sa itaas.

Ang pangunahing hamon sa offline eval ay tiyakin na ang iyong test dataset ay komprehensibo at nananatiling may kaugnayan – maaaring mag-perform nang maayos ang agent sa isang fixed test set ngunit makaharap ng napaka-ibang mga query sa produksyon. Samakatuwid, dapat mong panatilihing updated ang mga test set na may mga bagong edge cases at mga halimbawa na sumasalamin sa mga sitwasyon sa totoong mundo​. Ang kombinasyon ng maliliit na "smoke test" cases at mas malalaking evaluation sets ay kapaki-pakinabang: maliliit na set para sa mabilisang pagsusuri at mas malalaking set para sa mas malawak na sukatan ng pagganap​.

### Online Evaluation 

![Pangkalahatang-ideya ng mga sukatan sa pagmamasid](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ito ay tumutukoy sa pagsusuri sa agent sa isang live, totoong mundo na kapaligiran, i.e. sa aktwal na paggamit sa produksyon. Ang online evaluation ay kinabibilangan ng pagsubaybay sa pagganap ng agent sa mga tunay na interaksyon ng user at patuloy na pagsusuri ng mga resulta.

Halimbawa, maaari mong subaybayan ang mga rate ng tagumpay, mga score ng kasiyahan ng user, o iba pang sukatan sa live na traffic. Ang bentahe ng online evaluation ay **nakukuha nito ang mga bagay na maaaring hindi mo inaasahan sa isang lab setting** – maaari mong obserbahan ang model drift sa paglipas ng panahon (kung bumaba ang bisa ng agent habang nagbabago ang mga pattern ng input) at mahuli ang mga hindi inaasahang query o sitwasyon na wala sa iyong test data​. Nagbibigay ito ng tunay na larawan kung paano kumikilos ang agent sa totoong mundo.

Ang online evaluation ay madalas na kinabibilangan ng pagkolekta ng implicit at explicit na feedback ng user, tulad ng tinalakay, at posibleng pagpapatakbo ng shadow tests o A/B tests (kung saan ang bagong bersyon ng agent ay tumatakbo nang parallel upang ihambing sa lumang bersyon). Ang hamon ay maaaring mahirap makakuha ng maaasahang mga label o score para sa mga live na interaksyon – maaari kang umasa sa feedback ng user o mga downstream metrics (tulad ng kung nag-click ang user sa resulta).

### Pagsasama ng Dalawa

Ang online at offline evaluations ay hindi magkasalungat; sila ay lubos na nagkakatuwang. Ang mga insight mula sa online monitoring (halimbawa, mga bagong uri ng query ng user kung saan mahina ang pagganap ng agent) ay maaaring gamitin upang palakasin at pagbutihin ang mga offline test dataset. Sa kabilang banda, ang mga agent na mahusay na gumaganap sa offline tests ay mas kumpiyansang ma-deploy at masubaybayan online.

Sa katunayan, maraming team ang gumagamit ng loop:

_suriin offline -> i-deploy -> subaybayan online -> mangolekta ng mga bagong kaso ng pagkabigo -> idagdag sa offline dataset -> pagbutihin ang agent -> ulitin_.

## Mga Karaniwang Isyu

Habang inilalagay ang mga AI agent sa produksyon, maaari kang makaranas ng iba't ibang hamon. Narito ang ilang karaniwang isyu at kanilang mga posibleng solusyon:

| **Isyu**    | **Posibleng Solusyon**   |
| ------------- | ------------------ |
| Hindi palaging gumaganap ang AI Agent ng mga gawain nang pare-pareho | - Pinuhin ang prompt na ibinibigay sa AI Agent; maging malinaw sa mga layunin.<br>- Tukuyin kung saan maaaring hatiin ang mga gawain sa mas maliliit na subtask at hawakan ng maraming agent. |
| Ang AI Agent ay nauwi sa tuloy-tuloy na mga loop  | - Tiyakin na mayroon kang malinaw na mga termino at kundisyon ng pagtatapos upang malaman ng Agent kung kailan titigil ang proseso.

## Mga Karaniwang Problema at Solusyon

Narito ang ilang mga karaniwang problema na maaaring maranasan kapag nagde-deploy ng AI agents sa production, kasama ang mga posibleng solusyon:

| **Problema** | **Solusyon** |
|--------------|--------------|
| Hindi sapat ang performance ng AI agent sa mga kumplikadong gawain | - Gumamit ng mas malaking modelo na espesyal para sa mga gawain na nangangailangan ng masusing pag-iisip. |
| Hindi maayos ang performance ng AI Agent tool calls | - Subukan at i-validate ang output ng tool sa labas ng agent system.<br>- Ayusin ang mga parameter, prompts, at pangalan ng mga tool. |
| Hindi consistent ang performance ng Multi-Agent system | - Ayusin ang mga prompts na ibinibigay sa bawat agent upang masigurong specific at naiiba ang mga ito sa isa’t isa.<br>- Gumawa ng hierarchical system gamit ang "routing" o controller agent upang matukoy kung aling agent ang tamang gamitin. |

Mas madaling matukoy ang mga isyung ito kung may observability. Ang mga traces at metrics na tinalakay natin kanina ay tumutulong upang malaman kung saan eksaktong nagkakaroon ng problema sa workflow ng agent, na nagpapabilis ng debugging at optimization.

## Pamamahala ng Gastos

Narito ang ilang mga estratehiya upang pamahalaan ang gastos sa pag-deploy ng AI agents sa production:

**Paggamit ng Mas Maliit na Modelo:** Ang Small Language Models (SLMs) ay maaaring mag-perform nang maayos sa ilang mga use-case ng agent at makakatipid nang malaki sa gastos. Tulad ng nabanggit kanina, ang paggawa ng evaluation system upang matukoy at maikumpara ang performance laban sa mas malaking modelo ang pinakamainam na paraan upang maunawaan kung gaano kahusay ang SLM sa iyong use case. Isaalang-alang ang paggamit ng SLMs para sa mas simpleng gawain tulad ng intent classification o parameter extraction, habang ginagamit ang mas malaking modelo para sa mas kumplikadong pag-iisip.

**Paggamit ng Router Model:** Isang katulad na estratehiya ay ang paggamit ng iba’t ibang modelo at laki. Maaari kang gumamit ng LLM/SLM o serverless function upang i-route ang mga request batay sa complexity sa mga modelong pinakaangkop. Makakatulong ito sa pagbabawas ng gastos habang sinisigurado ang performance sa tamang gawain. Halimbawa, i-route ang mga simpleng query sa mas maliit at mas mabilis na modelo, at gamitin lamang ang mahal na malaking modelo para sa mga kumplikadong reasoning tasks.

**Caching Responses:** Ang pagtukoy sa mga karaniwang request at gawain at pagbibigay ng mga sagot bago pa ito dumaan sa iyong agentic system ay isang mahusay na paraan upang mabawasan ang dami ng mga katulad na request. Maaari ka ring mag-implement ng flow upang matukoy kung gaano kahawig ang isang request sa iyong mga naka-cache na request gamit ang mas basic na AI models. Ang estratehiyang ito ay maaaring makapagbawas nang malaki sa gastos para sa mga madalas itanong o karaniwang workflows.

## Tingnan Natin Kung Paano Ito Gumagana sa Praktika

Sa [halimbawang notebook ng seksyong ito](./code_samples/10_autogen_evaluation.ipynb), makikita natin ang mga halimbawa kung paano natin magagamit ang mga observability tools upang i-monitor at i-evaluate ang ating agent.

### May Karagdagang Tanong Tungkol sa AI Agents sa Production?

Sumali sa [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) upang makipag-usap sa ibang mga nag-aaral, dumalo sa office hours, at makakuha ng sagot sa iyong mga tanong tungkol sa AI Agents.

## Nakaraang Aralin

[Metacognition Design Pattern](../09-metacognition/README.md)

## Susunod na Aralin

[Agentic Protocols](../11-agentic-protocols/README.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.