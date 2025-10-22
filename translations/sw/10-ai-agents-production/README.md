<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cdfd0acc8592c1af14f8637833450375",
  "translation_date": "2025-08-29T19:53:00+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "sw"
}
-->
# Mawakala wa AI Katika Uzalishaji: Ufuatiliaji na Tathmini

[![Mawakala wa AI Katika Uzalishaji](../../../translated_images/lesson-10-thumbnail.2b79a30773db093e0b4fb47aaa618069e0afb4745fad4836526cf51df87f9ac9.sw.png)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Wakati mawakala wa AI wanapohama kutoka kwa mifano ya majaribio hadi matumizi halisi, uwezo wa kuelewa tabia zao, kufuatilia utendaji wao, na kutathmini matokeo yao kwa utaratibu unakuwa muhimu.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utaweza kujua jinsi ya/kuelewa:
- Dhana kuu za ufuatiliaji na tathmini ya mawakala
- Mbinu za kuboresha utendaji, gharama, na ufanisi wa mawakala
- Nini na jinsi ya kutathmini mawakala wako wa AI kwa utaratibu
- Jinsi ya kudhibiti gharama wakati wa kupeleka mawakala wa AI katika uzalishaji
- Jinsi ya kuweka vifaa kwenye mawakala waliotengenezwa kwa AutoGen

Lengo ni kukupa maarifa ya kubadilisha mawakala wako wa "sanduku jeusi" kuwa mifumo ya uwazi, inayoweza kudhibitiwa, na ya kutegemewa.

_**Kumbuka:** Ni muhimu kupeleka Mawakala wa AI ambao ni salama na wa kuaminika. Angalia somo la [Kujenga Mawakala wa AI wa Kuaminika](./06-building-trustworthy-agents/README.md) pia._

## Mfuatano na Vipande

Zana za ufuatiliaji kama [Langfuse](https://langfuse.com/) au [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) mara nyingi huwakilisha uendeshaji wa mawakala kama mfuatano na vipande.

- **Mfuatano** unawakilisha kazi kamili ya wakala kutoka mwanzo hadi mwisho (kama kushughulikia swali la mtumiaji).
- **Vipande** ni hatua za mtu mmoja mmoja ndani ya mfuatano (kama kuita mfano wa lugha au kupata data).

![Mti wa Mfuatano katika Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Bila ufuatiliaji, wakala wa AI anaweza kuhisi kama "sanduku jeusi" - hali yake ya ndani na hoja zake ni ngumu kueleweka, na kufanya iwe vigumu kugundua matatizo au kuboresha utendaji. Kwa ufuatiliaji, mawakala wanakuwa "masanduku ya kioo," wakitoa uwazi ambao ni muhimu kwa kujenga imani na kuhakikisha wanafanya kazi kama ilivyokusudiwa.

## Kwa Nini Ufuatiliaji Ni Muhimu Katika Mazingira ya Uzalishaji

Kuhamisha mawakala wa AI kwenye mazingira ya uzalishaji huleta changamoto na mahitaji mapya. Ufuatiliaji hauwi tena "kitu kizuri kuwa nacho" bali ni uwezo muhimu:

*   **Utatuzi wa Hitilafu na Uchambuzi wa Sababu ya Msingi**: Wakati wakala anaposhindwa au kutoa matokeo yasiyotarajiwa, zana za ufuatiliaji hutoa mfuatano unaohitajika kubaini chanzo cha hitilafu. Hii ni muhimu hasa kwa mawakala changamano ambao wanaweza kuhusisha miito mingi ya LLM, mwingiliano wa zana, na mantiki ya masharti.
*   **Usimamizi wa Muda wa Kusubiri na Gharama**: Mawakala wa AI mara nyingi hutegemea LLM na API za nje ambazo hutozwa kwa kila tokeni au kila mwito. Ufuatiliaji huruhusu ufuatiliaji wa kina wa miito hii, kusaidia kubaini shughuli ambazo ni polepole au ghali kupita kiasi. Hii inawawezesha timu kuboresha maelezo, kuchagua mifano yenye ufanisi zaidi, au kubuni upya mtiririko wa kazi ili kudhibiti gharama za uendeshaji na kuhakikisha uzoefu mzuri wa mtumiaji.
*   **Imani, Usalama, na Uzingatiaji**: Katika matumizi mengi, ni muhimu kuhakikisha kwamba mawakala wanatenda kwa usalama na kimaadili. Ufuatiliaji hutoa rekodi ya ukaguzi wa vitendo na maamuzi ya wakala. Hii inaweza kutumika kugundua na kupunguza masuala kama sindano ya maelezo, uzalishaji wa maudhui hatari, au utunzaji mbaya wa taarifa za kibinafsi (PII). Kwa mfano, unaweza kupitia mfuatano ili kuelewa kwa nini wakala alitoa jibu fulani au alitumia zana maalum.
*   **Mizunguko ya Uboreshaji Endelevu**: Data ya ufuatiliaji ni msingi wa mchakato wa maendeleo ya kurudia. Kwa kufuatilia jinsi mawakala wanavyofanya kazi katika ulimwengu halisi, timu zinaweza kubaini maeneo ya kuboresha, kukusanya data kwa ajili ya kurekebisha mifano, na kuthibitisha athari za mabadiliko. Hii huunda mzunguko wa maoni ambapo maarifa ya uzalishaji kutoka tathmini ya mtandaoni huarifu majaribio ya nje ya mtandao na uboreshaji, na kusababisha utendaji bora wa wakala kwa hatua.

## Vipimo Muhimu vya Kufuatilia

Ili kufuatilia na kuelewa tabia ya wakala, anuwai ya vipimo na ishara inapaswa kufuatiliwa. Ingawa vipimo maalum vinaweza kutofautiana kulingana na madhumuni ya wakala, baadhi ni muhimu kwa ujumla.

Hapa kuna baadhi ya vipimo vya kawaida ambavyo zana za ufuatiliaji hufuatilia:

**Muda wa Kusubiri:** Je, wakala anajibu haraka kiasi gani? Muda mrefu wa kusubiri huathiri uzoefu wa mtumiaji vibaya. Unapaswa kupima muda wa kusubiri kwa kazi na hatua za mtu mmoja mmoja kwa kufuatilia uendeshaji wa wakala. Kwa mfano, wakala anayechukua sekunde 20 kwa miito yote ya mfano anaweza kuharakishwa kwa kutumia mfano wa haraka zaidi au kwa kuendesha miito ya mfano sambamba.

**Gharama:** Je, ni gharama gani kwa kila uendeshaji wa wakala? Mawakala wa AI hutegemea miito ya LLM inayotozwa kwa kila tokeni au API za nje. Matumizi ya mara kwa mara ya zana au maelezo mengi yanaweza kuongeza gharama haraka. Kwa mfano, ikiwa wakala anaita LLM mara tano kwa uboreshaji mdogo wa ubora, unapaswa kutathmini ikiwa gharama inastahili au ikiwa unaweza kupunguza idadi ya miito au kutumia mfano wa bei nafuu. Ufuatiliaji wa wakati halisi pia unaweza kusaidia kubaini ongezeko lisilotarajiwa (mfano, hitilafu zinazosababisha mizunguko ya API isiyoisha).

**Hitilafu za Ombi:** Ni ombi ngapi ambayo wakala alishindwa? Hii inaweza kujumuisha hitilafu za API au miito ya zana iliyoshindwa. Ili kufanya wakala wako kuwa thabiti zaidi dhidi ya hizi katika uzalishaji, unaweza kuweka mipangilio ya kurudia au njia mbadala. Mfano, ikiwa mtoa huduma wa LLM A yuko chini, unabadilisha kwa mtoa huduma wa LLM B kama chelezo.

**Maoni ya Mtumiaji:** Kutekeleza tathmini za moja kwa moja za watumiaji hutoa maarifa muhimu. Hii inaweza kujumuisha ukadiriaji wa moja kwa moja (👍thumbs-up/👎down, ⭐nyota 1-5) au maoni ya maandishi. Maoni hasi ya mara kwa mara yanapaswa kukutahadharisha kwani ni ishara kwamba wakala hafanyi kazi kama inavyotarajiwa.

**Maoni ya Kijanja ya Mtumiaji:** Tabia za watumiaji hutoa maoni yasiyo ya moja kwa moja hata bila ukadiriaji wa moja kwa moja. Hii inaweza kujumuisha uundaji upya wa maswali mara moja, maswali yanayorudiwa au kubofya kitufe cha kujaribu tena. Mfano, ikiwa unaona kwamba watumiaji wanauliza swali lile lile mara kwa mara, hii ni ishara kwamba wakala hafanyi kazi kama inavyotarajiwa.

**Usahihi:** Je, wakala hutoa matokeo sahihi au yanayotarajiwa mara ngapi? Ufafanuzi wa usahihi hutofautiana (mfano, usahihi wa kutatua matatizo, usahihi wa kupata taarifa, kuridhika kwa mtumiaji). Hatua ya kwanza ni kufafanua mafanikio yanamaanisha nini kwa wakala wako. Unaweza kufuatilia usahihi kupitia ukaguzi wa kiotomatiki, alama za tathmini, au lebo za kukamilisha kazi. Kwa mfano, kuweka alama mfuatano kama "ulifanikiwa" au "ulishindwa."

**Vipimo vya Tathmini ya Kiotomatiki:** Unaweza pia kuweka tathmini za kiotomatiki. Kwa mfano, unaweza kutumia LLM kupima matokeo ya wakala, mfano ikiwa ni ya msaada, sahihi, au la. Kuna pia maktaba kadhaa za chanzo huria zinazokusaidia kupima vipengele tofauti vya wakala. Mfano, [RAGAS](https://docs.ragas.io/) kwa mawakala wa RAG au [LLM Guard](https://llm-guard.com/) kugundua lugha hatari au sindano ya maelezo.

Kwa vitendo, mchanganyiko wa vipimo hivi hutoa uelewa bora wa afya ya wakala wa AI. Katika [notibuku ya mfano](./code_samples/10_autogen_evaluation.ipynb) ya sura hii, tutaonyesha jinsi vipimo hivi vinavyoonekana katika mifano halisi lakini kwanza, tutajifunza jinsi mtiririko wa kawaida wa tathmini unavyoonekana.

## Weka Vifaa Kwenye Wakala Wako

Ili kukusanya data ya mfuatano, utahitaji kuweka vifaa kwenye msimbo wako. Lengo ni kuweka vifaa kwenye msimbo wa wakala ili kutoa mfuatano na vipimo vinavyoweza kukamatwa, kuchakatwa, na kuonyeshwa na jukwaa la ufuatiliaji.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) imeibuka kama kiwango cha tasnia kwa ufuatiliaji wa LLM. Inatoa seti ya API, SDK, na zana za kuzalisha, kukusanya, na kusafirisha data ya telemetry.

Kuna maktaba nyingi za kuweka vifaa zinazofunika mifumo ya wakala iliyopo na kurahisisha kusafirisha vipande vya OpenTelemetry kwa zana ya ufuatiliaji. Hapo chini kuna mfano wa kuweka vifaa kwenye wakala wa AutoGen kwa kutumia [maktaba ya OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[Notibuku ya mfano](./code_samples/10_autogen_evaluation.ipynb) katika sura hii itaonyesha jinsi ya kuweka vifaa kwenye wakala wako wa AutoGen.

**Uundaji wa Vipande kwa Mkono:** Wakati maktaba za kuweka vifaa zinatoa msingi mzuri, mara nyingi kuna matukio ambapo habari ya kina zaidi au maalum inahitajika. Unaweza kuunda vipande kwa mkono ili kuongeza mantiki maalum ya programu. Muhimu zaidi, vinaweza kuimarisha vipande vilivyoundwa kiotomatiki au kwa mkono na sifa maalum (pia zinajulikana kama lebo au metadata). Sifa hizi zinaweza kujumuisha data maalum ya biashara, mahesabu ya kati, au muktadha wowote ambao unaweza kuwa muhimu kwa utatuzi wa hitilafu au uchambuzi, kama `user_id`, `session_id`, au `model_version`.

Mfano wa kuunda mfuatano na vipande kwa mkono kwa kutumia [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Tathmini ya Wakala

Ufuatiliaji hutupa vipimo, lakini tathmini ni mchakato wa kuchambua data hiyo (na kufanya majaribio) ili kubaini jinsi wakala wa AI anavyofanya kazi na jinsi unavyoweza kuboresha. Kwa maneno mengine, mara unapokuwa na mfuatano na vipimo hivyo, unavitumiaje kuhukumu wakala na kufanya maamuzi?

Tathmini ya mara kwa mara ni muhimu kwa sababu mawakala wa AI mara nyingi si wa uhakika na wanaweza kubadilika (kupitia masasisho au mabadiliko ya tabia ya mfano) – bila tathmini, usingejua ikiwa "wakala wako mwerevu" anafanya kazi yake vizuri au ikiwa umepungua.

Kuna aina mbili za tathmini kwa mawakala wa AI: **tathmini ya mtandaoni** na **tathmini ya nje ya mtandao**. Zote ni muhimu, na zinakamilishana. Kwa kawaida tunaanza na tathmini ya nje ya mtandao, kwani hii ni hatua ya chini kabisa inayohitajika kabla ya kupeleka wakala yeyote.

### Tathmini ya Nje ya Mtandao

![Vitu vya Dataset katika Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Hii inahusisha kutathmini wakala katika mazingira yaliyodhibitiwa, kwa kawaida kwa kutumia seti za majaribio, si maswali ya moja kwa moja ya watumiaji. Unatumia seti za data zilizokusanywa ambapo unajua matokeo yanayotarajiwa au tabia sahihi, kisha unaendesha wakala wako kwenye hizo.

Kwa mfano, ikiwa umeunda wakala wa matatizo ya hesabu, unaweza kuwa na [seti ya majaribio](https://huggingface.co/datasets/gsm8k) ya matatizo 100 yenye majibu yanayojulikana. Tathmini ya nje ya mtandao mara nyingi hufanywa wakati wa maendeleo (na inaweza kuwa sehemu ya mabomba ya CI/CD) ili kuangalia maboresho au kuzuia kupungua. Faida ni kwamba ni **ya kurudiwa na unaweza kupata vipimo vya usahihi wazi kwa kuwa una ukweli wa msingi**. Unaweza pia kuiga maswali ya watumiaji na kupima majibu ya wakala dhidi ya majibu bora au kutumia vipimo vya kiotomatiki kama ilivyoelezwa hapo juu.

Changamoto kuu na tathmini ya nje ya mtandao ni kuhakikisha seti yako ya majaribio ni ya kina na inabaki kuwa muhimu – wakala anaweza kufanya vizuri kwenye seti ya majaribio iliyowekwa lakini kukutana na maswali tofauti sana katika uzalishaji. Kwa hivyo, unapaswa kuweka seti za majaribio zikiwa zimesasishwa na kesi mpya za ukingo na mifano inayowakilisha hali halisi​. Mchanganyiko wa kesi ndogo za "majaribio ya moshi" na seti kubwa za tathmini ni muhimu: seti ndogo kwa ukaguzi wa haraka na seti kubwa kwa vipimo vya utendaji mpana​.

### Tathmini ya Mtandaoni 

![Muhtasari wa Vipimo vya Ufuatiliaji](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Hii inahusu kutathmini wakala katika mazingira halisi, ya ulimwengu wa moja kwa moja, yaani, wakati wa matumizi halisi katika uzalishaji. Tathmini ya mtandaoni inahusisha kufuatilia utendaji wa wakala kwenye mwingiliano halisi wa watumiaji na kuchambua matokeo kwa kuendelea.

Kwa mfano, unaweza kufuatilia viwango vya mafanikio, alama za kuridhika kwa watumiaji, au vipimo vingine kwenye trafiki ya moja kwa moja. Faida ya tathmini ya mtandaoni ni kwamba **inakusanya mambo ambayo huenda usingetarajia katika mazingira ya maabara** – unaweza kuona mabadiliko ya mfano kwa muda (ikiwa ufanisi wa wakala unapungua kadri mifumo ya pembejeo inavyobadilika) na kugundua maswali au hali zisizotarajiwa ambazo hazikuwa kwenye data yako ya majaribio​. Inatoa picha halisi ya jinsi wakala anavyofanya kazi katika mazingira halisi.

Tathmini ya mtandaoni mara nyingi inahusisha kukusanya maoni ya moja kwa moja na yasiyo ya moja kwa moja ya watumiaji, kama ilivyojadiliwa, na labda kuendesha majaribio ya kivuli au majaribio ya A/B (ambapo toleo jipya la wakala linaendeshwa sambamba kulinganisha na la zamani). Changamoto ni kwamba inaweza kuwa ngumu kupata lebo au alama za kuaminika kwa mwingiliano wa moja kwa moja – unaweza kutegemea maoni ya watumiaji au vipimo vya chini (kama mtumiaji alibofya matokeo).

### Kuchanganya Zote Mbili

Tathmini ya mtandaoni na nje ya mtandao si za kipekee; zinakamilishana sana. Maarifa kutoka kwa ufuatiliaji wa mtandaoni (mfano, aina mpya za maswali ya watumiaji ambapo wakala hufanya vibaya) yanaweza kutumika kuongeza na kuboresha seti za majaribio ya nje ya mtandao. Kinyume chake, mawakala wanaofanya vizuri katika majaribio ya nje ya mtandao wanaweza kupelekwa kwa ujasiri zaidi na kufuatiliwa mtandaoni.

Kwa kweli, timu nyingi huchukua mzunguko:

_tathmini nje ya mtandao -> peleka -> fuatilia mtandaoni -> kukusanya kesi mpya za kushindwa -> ongeza kwenye seti ya nje ya mtandao -> boresha wakala -> rudia_.

## Masuala ya Kawaida

Unapopeleka mawakala wa AI katika uzalishaji, unaweza kukutana na changamoto mbalimbali. Hapa kuna baadhi ya masuala ya kawaida na suluhisho zao zinazowezekana:

| **Suala**    | **Suluhisho Linalowezekana**

## Kusimamia Changamoto za Mawakala wa AI

Hapa kuna changamoto za kawaida zinazotokea wakati wa kupeleka mawakala wa AI kwenye uzalishaji, pamoja na mikakati ya kuzitatua:

### Changamoto za Utendaji

| **Tatizo**                                   | **Suluhisho**                                                                 |
|---------------------------------------------|-------------------------------------------------------------------------------|
| Mawakala wa AI hawafanyi kazi vizuri         | - Jaribu na thibitisha matokeo ya zana nje ya mfumo wa wakala.<br>- Rekebisha vigezo vilivyowekwa, maelezo ya kazi, na majina ya zana. |
| Mfumo wa Mawakala Wengi hauendi vizuri       | - Rekebisha maelezo ya kazi yaliyotolewa kwa kila wakala ili kuhakikisha kuwa ni maalum na tofauti kati yao.<br>- Unda mfumo wa kihierarkia kwa kutumia wakala wa "routing" au mdhibiti ili kuamua ni wakala gani anayefaa. |

Masuala mengi haya yanaweza kutambuliwa kwa ufanisi zaidi ikiwa kuna ufuatiliaji wa kutosha. Ufuatiliaji na vipimo tulivyojadili awali husaidia kubaini hasa ni wapi katika mtiririko wa kazi wa wakala matatizo yanatokea, na kufanya utatuzi na uboreshaji kuwa rahisi zaidi.

## Kusimamia Gharama

Hapa kuna mikakati ya kusimamia gharama za kupeleka mawakala wa AI kwenye uzalishaji:

**Kutumia Miundo Midogo:** Miundo Midogo ya Lugha (SLMs) inaweza kufanya kazi vizuri kwenye baadhi ya matumizi ya wakala na kupunguza gharama kwa kiasi kikubwa. Kama ilivyotajwa awali, kujenga mfumo wa tathmini ili kuamua na kulinganisha utendaji dhidi ya miundo mikubwa ni njia bora ya kuelewa jinsi SLM itakavyofanya kazi kwenye matumizi yako. Fikiria kutumia SLMs kwa kazi rahisi kama uainishaji wa nia au uchimbaji wa vigezo, huku ukihifadhi miundo mikubwa kwa kazi ngumu za kufikiria.

**Kutumia Modeli ya Router:** Mkakati sawa ni kutumia aina mbalimbali za miundo na ukubwa. Unaweza kutumia LLM/SLM au kazi isiyo na seva (serverless function) kuelekeza maombi kulingana na ugumu wake kwa miundo inayofaa zaidi. Hii pia itasaidia kupunguza gharama huku ikihakikisha utendaji kwenye kazi sahihi. Kwa mfano, elekeza maswali rahisi kwa miundo midogo na ya haraka, na tumia miundo mikubwa na ghali tu kwa kazi ngumu za kufikiria.

**Kuhifadhi Majibu:** Kutambua maombi na kazi za kawaida na kutoa majibu kabla ya kupitia mfumo wako wa wakala ni njia nzuri ya kupunguza idadi ya maombi yanayofanana. Unaweza hata kutekeleza mtiririko wa kutambua jinsi ombi lilivyo sawa na maombi yaliyohifadhiwa kwa kutumia miundo ya AI ya msingi zaidi. Mkakati huu unaweza kupunguza gharama kwa kiasi kikubwa kwa maswali yanayoulizwa mara kwa mara au mtiririko wa kazi wa kawaida.

## Hebu Tuone Jinsi Hii Inavyofanya Kazi Kwenye Mazoezi

Katika [notebook ya mfano wa sehemu hii](./code_samples/10_autogen_evaluation.ipynb), tutaona mifano ya jinsi tunavyoweza kutumia zana za ufuatiliaji kufuatilia na kutathmini wakala wetu.

### Una Maswali Zaidi Kuhusu Mawakala wa AI Kwenye Uzalishaji?

Jiunge na [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ili kukutana na wanafunzi wengine, kuhudhuria masaa ya ofisi, na kupata majibu ya maswali yako kuhusu Mawakala wa AI.

## Somo la Awali

[Muundo wa Metacognition](../09-metacognition/README.md)

## Somo Linalofuata

[Itifaki za Mawakala](../11-agentic-protocols/README.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutokuelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.