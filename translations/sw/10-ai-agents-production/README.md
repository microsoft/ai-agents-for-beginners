# Mawakala ya AI Katika Uzalishaji: Uwazi & Tathmini

[![Mawakala wa AI Katika Uzalishaji](../../../translated_images/sw/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Wakati mawakala wa AI yanavyohamia kutoka mifano ya majaribio hadi matumizi halisi ya dunia, uwezo wa kuelewa tabia zao, kufuatilia utendaji wao, na kutathmini kwa mfumo matokeo yao unakuwa muhimu.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utajua jinsi ya/utaelewa:
- Misingi ya ufuatiliaji (observability) na tathmini ya mawakala
- Mbinu za kuboresha utendaji, gharama, na ufanisi wa mawakala
- Nini na jinsi ya kutathmini mawakala wako wa AI kwa mfumo
- Jinsi ya kudhibiti gharama unapopeleka mawakala wa AI uzalishoni
- Jinsi ya kuingiza ufuatiliaji kwa mawakala yaliyotengenezwa kwa Microsoft Agent Framework

Lengo ni kukupa maarifa ya kugeuza mawakala wako "sanduku nyeusi" kuwa mifumo iliyo wazi, inayoweza kusimamiwa, na inayowaaminika.

_**Kumbuka:** Ni muhimu kupeleka Mawakala wa AI ambao ni salama na wa kuaminika. Angalia pia somo la [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md)._

## Traces and Spans

Vifaa vya ufuatiliaji kama [Langfuse](https://langfuse.com/) au [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) kwa kawaida huwakilisha utekelezaji wa wakala kama traces na spans.

- **Trace** inawakilisha kazi kamili ya wakala kutoka mwanzo hadi mwisho (kama kushughulikia swali la mtumiaji).
- **Spans** ni hatua za mtu mmoja ndani ya trace (kama kupiga simu kwa modeli ya lugha au kupata data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bila ufuatiliaji, wakala wa AI anaweza kuhisi kama "sanduku nyeusi" - hali yake ya ndani na hoja zake ni za wazi, na hii inafanya kuwa vigumu kutambua matatizo au kuboresha utendaji. Kwa ufuatiliaji, mawakala huwa "sanduku za kioo," huku wakiweka uwazi ambao ni muhimu kwa kujenga uaminifu na kuhakikisha wanafanya kazi kama ilivyokusudiwa.

## Kwa Nini Uwazi ni Muhimu katika Mazingira ya Uzalishaji

Kuhamisha mawakala wa AI kwenye mazingira ya uzalishaji huleta changamoto na mahitaji mapya. Ufuatiliaji si tena "aina ya nzuri kuwa nayo" bali ni uwezo muhimu:

*   **Kurekebisha Makosa na Uchambuzi wa Chanzo Halisi**: Wakati wakala anashindwa au anatoa matokeo yasiyotegemewa, zana za ufuatiliaji hutoa traces zinazohitajika ili kubaini chanzo cha kosa. Hii ni muhimu hasa kwa mawakala tata ambao yanaweza kuhusisha simu nyingi za LLM, mwingiliano wa zana, na mantiki ya masharti.
*   **Uendeshaji wa Ugumu na Usimamizi wa Gharama**: Mawakala ya AI mara nyingi hutegemea LLMs na API za nje zinazolipishwa kwa tokeni au kwa simu. Ufuatiliaji unaruhusu ufuatiliaji sahihi wa simu hizi, ukisaidia kubaini shughuli ambazo ni polepole mno au ghali. Hii inawawezesha timu kuboresha prompts, kuchagua modeli zilizo na ufanisi zaidi, au kubadilisha mtiririko wa kazi ili kusimamia gharama za uendeshaji na kuhakikisha uzoefu mzuri wa mtumiaji.
*   **Uaminifu, Usalama, na Uzingatiaji**: Katika programu nyingi, ni muhimu kuhakikisha kwamba mawakala hufanya kazi kwa usalama na kwa maadili. Ufuatiliaji hutoa njia ya ukaguzi ya vitendo na maamuzi ya wakala. Hii inaweza kutumika kugundua na kupunguza matatizo kama sindano ya prompt (prompt injection), utengenezaji wa maudhui hatarishi, au utunzaji mbaya wa taarifa za kibinafsi (PII). Kwa mfano, unaweza kupitia traces kuelewa kwanini wakala alitoa jibu fulani au alitumia zana maalum.
*   **Mizunguko ya Uboreshaji Endelevu**: Data ya ufuatiliaji ni msingi wa mchakato wa maendeleo wa kuendelea. Kwa kufuatilia jinsi mawakala wanavyofanya kazi kwa ulimwengu halisi, timu zinaweza kubaini maeneo ya kuboresha, kukusanya data kwa ajili ya kuimarisha modeli, na kuthibitisha athari za mabadiliko. Hii inaunda mnyororo wa maoni ambapo maarifa ya uzalishaji kutoka tathmini mtandaoni yanawaongoza majaribio ya nje ya mtandao na urekebishaji, na kusababisha utendaji bora wa wakala kwa hatua.

## Vipimo Muhimu vya Kufuatilia

Ili kufuatilia na kuelewa tabia ya wakala, aina mbalimbali za vipimo na ishara zinapaswa kufuatiliwa. Wakati vipimo maalum vinaweza kutofautiana kulingana na kusudio la wakala, baadhi ni muhimu kwa ujumla.

Hapa kuna baadhi ya vipimo vinavyofuatiliwa mara kwa mara na zana za ufuatiliaji:

**Latency:** Je, wakala anarejea kwa haraka kiasi gani? Muda mrefu wa kusubiri unaathiri vibaya uzoefu wa mtumiaji. Unapaswa kupima latency kwa kazi na hatua binafsi kwa kufuatilia utekelezaji wa wakala. Kwa mfano, wakala anayechukua sekunde 20 kwa simu zote za modeli anaweza kuharakishwa kwa kutumia modeli ya kasi zaidi au kwa kufanya simu za modeli kwa sambamba.

**Gharama:** Ni gharama gani kwa kila utekelezaji wa wakala? Mawakala ya AI hutegemea simu za LLM zinazolipishwa kwa tokeni au API za nje. Matumizi ya zana mara kwa mara au prompts nyingi yanaweza kuongeza gharama kwa haraka. Kwa mfano, ikiwa wakala anaita LLM mara tano kwa kuboresha ubora kidogo, lazima uangalia kama gharama inafaa au kama unaweza kupunguza idadi ya simu au kutumia modeli ya bei nafuu. Ufuatiliaji wa wakati halisi pia unaweza kusaidia kubaini madoadoa yasiyotarajiwa (kwa mfano, viongezeo vinavyosababisha mizunguko ya API isiyohitajika).

**Makosa ya Maombi:** Ni maombi mangapi yaliyoshindikana? Hii inaweza kujumuisha makosa ya API au simu za zana zilizoshindwa. Ili kufanya wakala wako kuwa imara zaidi dhidi ya haya katika uzalishaji, unaweza basi kuweka mbadala au kurudia maombi. Mfano: ikiwa mtoaji wa LLM A yamezama, unabadilisha kwa mtoaji wa LLM B kama nakala ya ziada.

**Maoni ya Watumiaji:** Kutekeleza tathmini za moja kwa moja kutoka kwa watumiaji kunatoa maarifa muhimu. Hii inaweza kujumuisha viwango vya wazi (👍kuchwa kwa kidole/👎chini, ⭐1-5 nyota) au maoni ya maandishi. Maoni hasi mara kwa mara yanapaswa kukujulisha kwa kuwa ni ishara kuwa wakala haufanyi kazi kama inavyotarajiwa.

**Maoni Yasiyo ya Moja kwa Moja kutoka kwa Watumiaji:** Tabia za watumiaji hutoa maoni ya kidole hata bila viwango vya wazi. Hii inaweza kujumuisha kurekebisha swali mara moja, kuuliza tena maswali, au kubofya kitufe cha jaribu tena. Mfano: ikiwa unaona watumiaji mara kwa mara wanauliza swali lile lile, hii ni ishara kwamba wakala haufanyi kazi kama inavyotarajiwa.

**Usahihi:** Mara ngapi wakala hutoa matokeo sahihi au yanayotakikana? Maana ya usahihi zinatofautiana (mfano, usahihi wa kutatua tatizo, usahihi wa kupata taarifa, kuridhika kwa mtumiaji). Hatua ya kwanza ni kufafanua jinsi mafanikio yanavyoonekana kwa wakala wako. Unaweza kufuatilia usahihi kupitia ukaguzi wa atomatiki, alama za tathmini, au lebo za kukamilika kwa kazi. Kwa mfano, kuweka traces kama "succeeded" au "failed".

**Vipimo vya Tathmini ya Kiotomatiki:** Pia unaweza kuweka tathmini za kiotomatiki. Kwa mfano, unaweza kutumia LLM kupima matokeo ya wakala, kama ikiwa ni ya msaada, sahihi, au la. Pia kuna maktaba kadhaa za chanzo huria zinazokusaidia kupima nyanja tofauti za wakala. Mfano: [RAGAS](https://docs.ragas.io/) kwa mawakala wa RAG au [LLM Guard](https://llm-guard.com/) kugundua lugha hatarishi au sindano ya prompt.

Katika vitendo, mchanganyiko wa vipimo hivi hutoa mfuko bora wa afya ya wakala wa AI. Katika karatasi hii [mfano wa daftari](./code_samples/10-expense_claim-demo.ipynb), tutaonyesha jinsi vipimo hivi vinavyoonekana katika mifano halisi lakini kwanza, tutajifunza jinsi mtiririko wa tathmini wa kawaida unavyoonekana.

## Chomeka ufuatiliaji kwenye Wakala Wako

Ili kukusanya data za tracing, utahitaji kuingiza ufuatiliaji kwenye msimbo wako. Lengo ni kuingiza msimbo wa wakala ili kutoa traces na vipimo vinavyoweza kukamatwa, kusindika, na kuonyeshwa na jukwaa la ufuatiliaji.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) imeibuka kama kiwango cha tasnia kwa ufuatiliaji wa LLM. Inatoa seti ya API, SDK, na zana za kuzalisha, kukusanya, na kusafirisha telemetry data.

Kuna maktaba nyingi za instrumentation zinazozunguka mifumo ya wakala iliyopo na kufanya iwe rahisi kusafirisha OpenTelemetry spans kwa kifaa cha ufuatiliaji. Microsoft Agent Framework inaunganisha na OpenTelemetry asilia. Hapa chini ni mfano wa kuingiza ufuatiliaji kwa wakala wa MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Utekelezaji wa wakala unafuatiliwa kiotomatiki
    pass
```

Daftari la [mfano](./code_samples/10-expense_claim-demo.ipynb) katika sura hii litaonyesha jinsi ya kuingiza ufuatiliaji kwa wakala wako wa MAF.

**Uundaji wa Span kwa Mkono:** Wakati maktaba za instrumentation zinatoa msingi mzuri, mara nyingi kuna kesi ambapo taarifa za kina zaidi au za kawaida zinahitajika. Unaweza kuunda spans kwa mkono kuongeza mantiki maalum ya programu. Muhimu zaidi, zinaweza kuongeza urefu spans zilizoundwa kiotomatiki au kwa mkono kwa sifa maalum (pia zinajulikana kama tags au metadata). Sifa hizi zinaweza kujumuisha data maalum ya biashara, hesabu za kati, au muktadha wowote ambao ungeweza kuwa muhimu kwa kurekebisha au uchambuzi, kama `user_id`, `session_id`, au `model_version`.

Mfano wa kuunda traces na spans kwa mkono na [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Tathmini ya Wakala

Ufuatiliaji unatupa vipimo, lakini tathmini ni mchakato wa kuchambua data hiyo (na kufanya majaribio) ili kubaini jinsi wakala wa AI anavyofanya kazi na jinsi unavyoweza kuboreshwa. Kwa maneno mengine, mara tu unapokuwa na traces na vipimo hivyo, unavitumia vipi kuhukumu wakala na kufanya uamuzi?

Tathmini ya kawaida ni muhimu kwa sababu mawakala wa AI mara nyingi hawafuati sheria kali na yanaweza kubadilika (kupitia masasisho au mabadiliko ya tabia ya modeli) – bila tathmini, usingejua kama "wakala mwerevu" wako kwa kweli anafanya kazi vizuri au kama ameporomoka.

Kuna aina mbili za tathmini kwa mawakala wa AI: **tathmini mtandaoni** na **tathmini nje ya mtandao**. Zote mbili ni muhimu, na zinakamilishana. Kawaida tunaanza na tathmini nje ya mtandao, kwani hili ndilo hatua ndogo inayohitajika kabla ya kupeleka wakala wowote.

### Tathmini Nje ya Mtandao

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Hii inahusisha kutathmini wakala katika mazingira yaliyodhibitiwa, kawaida kwa kutumia seti za majaribio, si maswali ya watumiaji wanaoishi. Unatumia seti za data zilizoandaliwa ambapo unajua matokeo yanayotarajiwa au tabia sahihi, kisha uendeshe wakala wako juu yao.

Kwa mfano, ikiwa ujenzi wa wakala wa kutatua matatizo ya neno la hisabati, unaweza kuwa na [seti ya majaribio](https://huggingface.co/datasets/gsm8k) yenye matatizo 100 yenye majibu yanayojulikana. Tathmini nje ya mtandao mara nyingi hufanywa wakati wa maendeleo (na inaweza kuwa sehemu ya mitiririko ya CI/CD) ili kuangalia maboresho au kujikinga dhidi ya kuporomoka. Faida ni kwamba ni **inayoweza kurudiwa na unaweza kupata vipimo wazi vya usahihi kwa sababu una ukweli wa msingi**. Pia unaweza kuiga maswali ya watumiaji na kupima majibu ya wakala dhidi ya majibu bora au kutumia vipimo vya kiotomatiki kama ilivyoelezwa hapo juu.

Changamoto kuu na tathmini ya nje ya mtandao ni kuhakikisha seti yako ya majaribio ni kamili na inabaki muhimu – wakala anaweza kufanya vizuri kwenye seti ya mtihani iliyowekwa lakini kukutana na maswali tofauti kabisa uzalishoni. Kwa hivyo, unapaswa kuweka seti za mtihani zikisasishwa kwa kesi mpya na mifano inayowakilisha hali za dunia halisi. Mchanganyiko wa kesi ndogo za "mtihani wa moshi" na seti kubwa za tathmini ni muhimu: seti ndogo kwa ukaguzi wa haraka na seti kubwa kwa vipimo vya utendaji kwa ujumla.

### Tathmini Mtandaoni 

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Hii inahusu kutathmini wakala katika mazingira ya moja kwa moja, duniani halisi, yaani wakati wa matumizi halisi uzalishoni. Tathmini mtandaoni inahusisha kufuatilia utendaji wa wakala kwenye mwingiliano wa watumiaji wa kweli na kuchambua matokeo kwa kuendelea.

Kwa mfano, unaweza kufuatilia kiwango cha mafanikio, alama za kuridhika kwa watumiaji, au vipimo vingine kwenye trafiki ya moja kwa moja. Faida ya tathmini mtandaoni ni kwamba **inashirikisha mambo ambayo huenda hukutarajia katika maabara** – unaweza kuona mabadiliko ya modeli kwa muda (ikiwa ufanisi wa wakala unapungua wakati mifumo ya pembejeo inabadilika) na kugundua maswali yasiyotegemewa au hali ambazo hazikuwepo kwenye data yako ya mtihani. Inatoa picha halisi ya jinsi wakala anavyofanya kazi kwa watu.

Tathmini mtandaoni mara nyingi inajumuisha kukusanya maoni ya wazi na yasiyo ya wazi kutoka kwa watumiaji, kama ilivyojadiliwa, na labda kuendesha majaribio ya kivuli au majaribio ya A/B (ambapo toleo jipya la wakala linaendesha kwa sambamba kulinganisha na lile la zamani). Changamoto ni kuwa inaweza kuwa ngumu kupata lebo au alama za kuaminika kwa mwingiliano wa moja kwa moja – unaweza kutegemea maoni ya watumiaji au vipimo vya chini (kama je, mtumiaji alibofya matokeo).

### Kuunganisha Zote Mbili

Tathmini mtandaoni na nje ya mtandao sio kwa ubaguzi; zinakamilishana sana. Maarifa kutoka kwa ufuatiliaji mtandaoni (mfano, aina mpya za maswali ya watumiaji ambapo wakala anafanya vibaya) yanaweza kutumika kuongeza na kuboresha seti za mtihani za nje ya mtandao. Kinyume chake, mawakala yanayofanya vizuri kwenye majaribio ya nje ya mtandao yanaweza kisha kupelekwa kwa kujiamini zaidi na kufuatiliwa mtandaoni.

Kwa kweli, timu nyingi zinachukua mzunguko:

_tathmini nje ya mtandao -> weka kwenye uzalishaji -> fuatilia mtandaoni -> kusanya kesi mpya za kushindwa -> ongeza kwenye seti ya mtihani ya nje ya mtandao -> boresha wakala -> rudia_.

## Masuala ya Kawaida

Unapopeleka mawakala wa AI uzalishoni, unaweza kukutana na changamoto mbalimbali. Hapa kuna baadhi ya masuala ya kawaida na suluhisho zinazowezekana:

| **Tatizo**    | **Suluhisho Linawezekana**   |
| ------------- | ------------------ |
| Wakala wa AI hafanyi kazi kwa uthabiti | - Boresha prompt iliyotolewa kwa Wakala wa AI; kuwa wazi kuhusu malengo.<br>- Tambua ambapo kugawa kazi katika vitendo vidogo na kushughulikiwa na mawakala kadhaa kunaweza kusaidia. |
| Wakala wa AI kuingia katika mizunguko ya kuendelea  | - Hakikisha una vigezo vya kumaliza wazi ili Wakala ajue lini kuacha mchakato.<br>- Kwa kazi ngumu zinazohitaji hoja na upangaji, tumia modeli kubwa iliyobobea kwa kazi za hoja. |
| Simu za zana za Wakala hazifanyi kazi vizuri   | - Jaribu na kutathmini matokeo ya zana nje ya mfumo wa wakala.<br>- Boresha vigezo vilivyotolewa, prompts, na majina ya zana.  |
| Mfumo wa Mawakala Wengi hauendi vizuri kwa uthabiti | - Boresha prompts zinazotolewa kwa kila wakala kuhakikisha zina uhakika na tofauti kati yao.<br>- Jenga mfumo wa hierarkia ukitumia wakala wa "routing" au mdhibiti kuamua ni wakala gani sahihi. |

Mengi ya matatizo haya yanaweza kubainishwa kwa ufanisi zaidi ikiwa ufuatiliaji umetekelezwa. Traces na vipimo tulivyojadili hapo juu husaidia kubainisha hasa wapi ndani ya mtiririko wa kazi ya wakala matatizo yanatokea, na kufanya urejesho wa makosa na uboreshaji kuwa wa ufanisi zaidi.

## Kusimamia Gharama
Hapa kuna mikakati kadhaa ya kusimamia gharama za kupeleka mawakala wa AI uzalishoni:

**Kutumia Modeli Ndogo:** Small Language Models (SLMs) zinaweza kufanya vyema katika baadhi ya matumizi ya mawakala na zitapunguza gharama kwa kiasi kikubwa. Kama ilivyotajwa hapo awali, kujenga mfumo wa tathmini wa kubainisha na kulinganisha utendaji ikilinganishwa na modeli kubwa ni njia bora ya kuelewa jinsi SLM itakavyofanya kazi katika matumizi yako. Fikiria kutumia SLMs kwa kazi rahisi kama utambuzi wa nia (intent classification) au uondoaji wa vigezo (parameter extraction), huku ukihifadhi modeli kubwa kwa uamuzi mgumu.

**Kutumia Modeli ya Router:** Mkakati sawa ni kutumia utofauti wa modeli na ukubwa. Unaweza kutumia LLM/SLM au serverless function kuongoza maombi kulingana na ugumu kwa modeli zinazofaa zaidi. Hii pia itasaidia kupunguza gharama huku ikihakikisha utendaji kwenye kazi zinazofaa. Kwa mfano, elekeza maswali rahisi kwa modeli ndogo, zenye kasi zaidi, na tumia modeli kubwa za gharama juu tu kwa kazi za fikra ngumu.

**Kuhifadhi Majibu kwa Cache:** Kutambua maombi na kazi zinazorudiwa na kutoa majibu kabla hayajapitia mfumo wako wa mawakala ni njia nzuri ya kupunguza idadi ya maombi yanayofanana. Unaweza hata kutekeleza mtiririko wa kubaini jinsi ombi linavyofanana na maombi yaliyo kwenye cache yako kwa kutumia modeli za AI za msingi. Mkakati huu unaweza kupunguza kwa kiasi kikubwa gharama kwa maswali yanayoulizwa mara kwa mara au mtiririko wa kazi unaojirudia.

## Hebu tuone jinsi hili linavyofanya kazi kwa vitendo

Katika [daftari la mfano la sehemu hii](./code_samples/10-expense_claim-demo.ipynb), tutaona mifano ya jinsi tunavyoweza kutumia zana za ufuatiliaji (observability tools) kufuatilia na kutathmini wakala wetu.

### Je, Una Maswali Zaidi kuhusu Mawakala wa AI Katika Uzalishaji?

Jiunge na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) kukutana na wanafunzi wengine, kuhudhuria saa za ofisi na kupata majibu ya maswali yako kuhusu Mawakala wa AI.

## Previous Lesson

[Metacognition Design Pattern](../09-metacognition/README.md)

## Next Lesson

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Tamko la kutokuwa na dhamana:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI Co-op Translator (https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au ukosefu wa usahihi. Nyaraka ya asili katika lugha yake ya asili inapaswa kutazamwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, inashauriwa kutumia tafsiri ya kitaalamu iliyofanywa na mtafsiri binadamu. Sisi hatuwajibiki kwa mkanganyiko au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->