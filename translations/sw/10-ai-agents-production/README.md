# Wakala za AI Katika Uzalishaji: Ufuatiliaji & Tathmini

[![Wakala za AI Katika Uzalishaji](../../../translated_images/sw/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Wakati wakala za AI zinavyohamia kutoka mifano ya majaribio kuelekea matumizi halisi ya ulimwengu, uwezo wa kuelewa tabia zao, kufuatilia utendakazi wao, na kutathmini kwa mfumo matokeo yao unakuwa muhimu.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utajua/utaelewa:
- Misingi ya ufuatiliaji (observability) na tathmini ya wakala
- Mbinu za kuboresha utendakazi, gharama, na ufanisi wa wakala
- Nini na jinsi ya kutathmini wakala wako wa AI kwa mfumo
- Jinsi ya kudhibiti gharama wakati wa kupeleka wakala wa AI uzalishaji
- Jinsi ya kuweka vyombo vya ufuatiliaji kwa wakala uliotengenezwa kwa Microsoft Agent Framework

Lengo ni kukupa maarifa ya kubadilisha wakala wako "sanduku jeusi" kuwa mifumo iliyo wazi, inayoweza kusimamiwa, na kuaminika.

_**Kumbuka:** Ni muhimu kupeleka Wakala wa AI ambao ni salama na wa kuaminika. Angalia pia somo la [Kujenga Wakala wa AI wa Kuaminika](./06-building-trustworthy-agents/README.md)._

## Traces and Spans

Vifaa vya ufuatiliaji kama [Langfuse](https://langfuse.com/) au [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) kawaida huwakilisha utekelezaji wa wakala kama traces na spans.

- **Trace** inawakilisha kazi kamili ya wakala kutoka mwanzo hadi mwisho (kama kushughulikia swali la mtumiaji).
- **Spans** ni hatua binafsi ndani ya trace (kama kuita modeli ya lugha au kupata data).

![Mti wa trace kwenye Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bila ufuatiliaji, wakala wa AI anaweza kuhisi kama "sanduku jeusi" - hali yake ya ndani na uamuzi wake ni hafifu, ikifanya iwe vigumu kutambua matatizo au kuboresha utendakazi. Kwa ufuatiliaji, wakala zinakuwa "sanduku za kioo," zikitangaza uwazi ambao ni muhimu kwa kujenga uaminifu na kuhakikisha zinafanya kazi kama ilivyokusudiwa. 

## Kwa Nini Ufuatiliaji ni Muhimu katika Mazingira ya Uzalishaji

Kuhamisha wakala za AI kwenye mazingira ya uzalishaji kunaleta changamoto na mahitaji mapya. Ufuatiliaji sio tena "ni vizuri kuwa nao" bali ni uwezo wa lazima:

*   **Urekebishaji na Uchambuzi wa Sababu za Msingi**: Wakati wakala anashindwa au kutoa matokeo yasiyotarajiwa, vifaa vya ufuatiliaji hutoa traces zinazohitajika kutambua chanzo cha kosa. Hii ni muhimu hasa kwa wakala tata ambao wanaweza kuhusisha miito kadhaa ya LLM, mwingiliano wa zana, na mantiki za masharti.
*   **Usimamizi wa Ucheleweshaji na Gharama**: Wakala za AI mara nyingi hutegemea LLM na API zingine za nje zinazolipishwa kwa tokeni au kwa kila mwito. Ufuatiliaji unawezesha kufuatilia kwa usahihi miito hii, kusaidia kutambua operesheni zinazo chelewesha kupita kiasi au ghali. Hii inawaruhusu timu kuboresha prompts, kuchagua modeli zenye ufanisi zaidi, au kubuni tena mtiririko wa kazi ili kudhibiti gharama za uendeshaji na kuhakikisha uzoefu mzuri kwa mtumiaji.
*   **Uaminifu, Usalama, na Uzingatiaji**: Katika programu nyingi, ni muhimu kuhakikisha wakala wanafanya kazi kwa usalama na kimaadili. Ufuatiliaji hutoa njia ya ukaguzi ya vitendo na maamuzi ya wakala. Hii inaweza kutumika kugundua na kupunguza matatizo kama utekezaji wa prompt, uzalishaji wa maudhui hatari, au kushughulikia vibaya taarifa za mtu binafsi (PII). Kwa mfano, unaweza kupitia traces kuelewa kwa nini wakala alitoa jibu fulani au kutumia zana maalum.
*   **Mizunguko ya Kuboresha Endelevu**: Data ya ufuatiliaji ni msingi wa mchakato wa maendeleo unaoendelea. Kwa kufuatilia jinsi wakala wanavyoitikia katika ulimwengu halisi, timu zinaweza kutambua maeneo ya kuboresha, kukusanya data kwa ajili ya kuimarisha modeli, na kuthibitisha athari za mabadiliko. Hii inaunda mzunguko wa mrejesho ambapo maarifa ya uzalishaji kutoka tathmini mtandaoni yanaarifu majaribio na uboreshaji wa nje ya mtandao, ikileta utendaji bora wa wakala kadri muda unavyoendelea.

## Vigezo Muhimu vya Kufuatilia

Ili kufuatilia na kuelewa tabia ya wakala, aina mbalimbali za vigezo na ishara zinapaswa kufuatiliwa. Ingawa vigezo maalum vinaweza kutofautiana kulingana na kusudi la wakala, baadhi ni muhimu kwa ulimwengu mzima.

Hapa kuna baadhi ya vigezo vinavyofuatiliwa mara kwa mara na zana za ufuatiliaji:

**Ucheleweshaji:** Je, wakala anajibu haraka kiasi gani? Muda mrefu wa kusubiri unaathiri vibaya uzoefu wa mtumiaji. Unapaswa kupima ucheleweshaji kwa kazi na hatua binafsi kwa kufuatilia utekelezaji wa wakala. Kwa mfano, wakala anayechukua sekunde 20 kwa miito yote ya modeli anaweza kuharakishwa kwa kutumia modeli ya kasi zaidi au kwa kufanya miito ya modeli kwa wakati mmoja.

**Gharama:** Ni gharama kiasi gani kwa kila utekelezaji wa wakala? Wakala wa AI hutegemea miito ya LLM inayolipishwa kwa tokeni au API za nje. Matumizi ya zana mara kwa mara au prompts nyingi yanaweza kuongeza gharama kwa haraka. Kwa mfano, kama wakala anaita LLM mara tano kwa kuboresha ubora wa kidogo, ni lazima kutathmini kama gharama inafaa au kama unaweza kupunguza idadi ya miito au kutumia modeli ya gharama nafuu. Ufuatiliaji wa wakati halisi pia unaweza kusaidia kugundua mabadiliko yasiyotarajiwa (mfano, hitilafu zinazosababisha mizunguko ya API kupita kiasi).

**Makosa ya Maombi:** Ni maombi mangapi ambayo wakala alishindwa? Hii inaweza kujumuisha makosa ya API au miito ya zana iliyoshindwa. Ili kufanya wakala wako kuwa imara zaidi dhidi ya haya katika uzalishaji, unaweza kuweka mbinu za kukabiliana au kurudia maombi. Mfano: ikiwa mtoaji wa LLM A yuko nje ya huduma, badilisha hadi mtoaji wa LLM B kama cheo cha akiba.

**Maoni ya Mtumiaji:** Kutekeleza tathmini za moja kwa moja kutoka kwa watumiaji kunatoa ufahamu wa thamani. Hii inaweza kujumuisha alama za wazi (👍thumbs-up/👎down, ⭐1-5 nyota) au maoni ya maandishi. Maoni hasi ya mara kwa mara yanapaswa kukutaarifu kwani ni dalili kwamba wakala haifanyi kazi kama ilivyotarajiwa. 

**Maoni yasiyo ya moja kwa moja ya Mtumiaji:** Tabia za mtumiaji hutoa mrejesho wa namna isiyo ya moja kwa moja hata bila alama wazi. Hii inaweza kujumuisha kubadilisha haraka swali, kuuliza tena mara nyingi au kubofya kitufe cha rudisha. Mfano: ikiwa unaona kuwa watumiaji wanauliza swali hilo mara kwa mara, hii ni dalili kwamba wakala haifanyi kazi kama ilivyotarajiwa.

**Usahihi:** Kwa mara ngapi wakala hutoa matokeo sahihi au yanayotakikana? Maana ya usahihi zinatofautiana (mfano, usahihi wa kutatua matatizo, usahihi wa kupata taarifa, kuridhika kwa mtumiaji). Hatua ya kwanza ni kufafanua jinsi mafanikio yanavyotarajiwa kwa wakala wako. Unaweza kufuatilia usahihi kupitia ukaguzi wa kiotomatiki, alama za tathmini, au lebo za kukamilika kwa kazi. Kwa mfano, kuweka traces kama "imefanikiwa" au "imeshindwa". 

**Vigezo vya Tathmini za Kiotomatiki:** Pia unaweza kuweka tathmini za kiotomatiki. Kwa mfano, unaweza kutumia LLM kutoa alama kwa matokeo ya wakala kama vile ikiwa ni ya msaada, sahihi, au la. Pia kuna maktaba kadhaa za chanzo huria zinazokusaidia kutoa alama kwa nyanja tofauti za wakala. Mfano: [RAGAS](https://docs.ragas.io/) kwa wakala wa RAG au [LLM Guard](https://llm-guard.com/) kugundua lugha hatari au utekezaji wa prompt. 

Katika vitendo, mchanganyiko wa vigezo hivi hutoa ufunuo bora wa afya ya wakala wa AI. Katika [daftari la mfano](./code_samples/10-expense_claim-demo.ipynb) cha sura hii, tutaonyesha jinsi vigezo hivi vinavyoonekana katika mifano halisi lakini kwanza, tutajifunza jinsi mtiririko wa tathmini kawaida unavyoonekana.

## Sanidi Ufuatiliaji kwa Wakala wako

Ili kukusanya data za tracing, utahitaji kuweka vyombo vya ufuatiliaji kwenye msimbo wako. Lengo ni kuingiza ufuatiliaji kwenye msimbo wa wakala ili kutoa traces na vigezo vinavyoweza kukamatwa, kuchakatwa, na kuonyeshwa na jukwaa la ufuatiliaji.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) imeibuka kama kiwango cha tasnia kwa ufuatiliaji wa LLM. Inatoa seti ya API, SDK, na zana za kuzalisha, kukusanya, na kusafirisha telemetry.

Kuna maktaba nyingi za uingizaji ambazo zinafunika mifumo ya wakala iliyopo na kurahisisha kusafirisha OpenTelemetry spans kwenda zana ya ufuatiliaji. Microsoft Agent Framework inaunganisha kwa asili na OpenTelemetry. Hapa chini kuna mfano wa kuweka ufuatiliaji kwa wakala wa MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Utekelezaji wa wakala unafuatiliwa kiotomatiki
    pass
```

Daftari la mfano (./code_samples/10-expense_claim-demo.ipynb) katika sura hii litaonyesha jinsi ya kuweka ufuatiliaji kwa wakala wako wa MAF.

**Uundaji wa Spans kwa Mikono:** Wakati maktaba za uingizaji hutoa msingi mzuri, mara kwa mara kuna kesi ambapo taarifa za kina zaidi au maalum zinahitajika. Unaweza kuunda spans kwa mikono ili kuongeza mantiki maalum ya programu. Muhimu zaidi, wanaweza kuimarisha spans zilizoundwa kiotomatiki au kwa mikono kwa vigezo maalum (vinavyojulikana pia kama tags au metadata). Vigezo hivi vinaweza kujumuisha data maalum ya biashara, mahesabu ya kati, au muktadha wowote ambao unaweza kuwa wa msaada kwa urekebishaji au uchambuzi, kama `user_id`, `session_id`, au `model_version`.

Mfano wa kuunda traces na spans kwa mikono kwa kutumia [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Tathmini ya Wakala

Ufuatiliaji hutupa vigezo, lakini tathmini ni mchakato wa kuchambua data hiyo (na kufanya majaribio) ili kubaini jinsi wakala wa AI anavyoenda vizuri na jinsi ya kuuboresha. Kwa maneno mengine, mara tu unapokuwa na traces na vigezo hivyo, jinsi unavyovitumia kuhukumu wakala na kufanya maamuzi?

Tathmini ya mara kwa mara ni muhimu kwa sababu wakala za AI mara nyingi si za lazima kutoa matokeo ya kila mara na zinaweza kubadilika (kupitia masasisho au mabadiliko ya tabia ya modeli) – bila tathmini, usingejua kama "wakala mwerevu" wako anaifanya kazi vizuri au ameanguka.

Kuna aina mbili za tathmini kwa wakaala za AI: **tathmini za mtandaoni (online)** na **tathmini za nje ya mtandao (offline)**. Zote zina thamani, na zina maletana. Kawaida tunaanza na tathmini ya nje ya mtandao, kwani hii ndiyo hatua ya lazima kabla ya kupeleka wakala wowote.

### Tathmini Nje ya Mtandao (Offline)

![Vitu vya seti ya data kwenye Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Hii inahusisha kutathmini wakala kwenye mazingira yaliyodhibitiwa, kawaida kutumia seti za majaribio, si maswali ya watumiaji hai. Unatumia seti zilizochaguliwa ambapo unajua matokeo yanayotarajiwa au tabia sahihi, kisha unaendesha wakala wako juu yao.

Kwa mfano, ikiwa umeunda wakala wa kutatua matatizo ya maneno ya hesabu, unaweza kuwa na [seti ya majaribio](https://huggingface.co/datasets/gsm8k) ya matatizo 100 yenye majibu yanayojulikana. Tathmini ya nje ya mtandao mara nyingi hufanywa wakati wa maendeleo (na inaweza kuwa sehemu ya mizunguko ya CI/CD) ili kukagua maboresho au kuzuia kuanguka kwa ubora. Faida yake ni kwamba ni **inarudiwa na unaweza kupata vigezo wazi vya usahihi tangu una ukweli wa ardhi (ground truth)**. Pia unaweza kuiga maswali ya watumiaji na kupima majibu ya wakala dhidi ya majibu bora au kutumia vigezo vya kiotomatiki kama ilivyoelezwa hapo juu.

Changamoto kuu na tathmini ya nje ya mtandao ni kuhakikisha seti yako ya majaribio ni jumuishi na inabaki muhimu – wakala anaweza kufanya vizuri kwenye seti ya majaribio iliyowekwa lakini kukutana na maswali tofauti kabisa katika uzalishaji. Kwa hivyo, unapaswa kuweka seti za majaribio zikisasishwa na kesi mpya za pembezoni na mifano inayoakisi hali za ulimwengu halisi​. Mchanganyiko wa kesi ndogo za "smoke test" na seti kubwa za tathmini ni wa maana: seti ndogo kwa ukaguzi wa haraka na kubwa kwa vigezo vya utendaji kwa ujumla​.

### Tathmini Mtandaoni (Online)

![Muhtasari wa vigezo vya ufuatiliaji](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Hii inahusu kutathmini wakala katika mazingira ya moja kwa moja, ya ulimwengu halisi, yaani wakati wa matumizi halisi katika uzalishaji. Tathmini ya mtandaoni inajumuisha kufuatilia utendakazi wa wakala kwenye mwingiliano wa watumiaji wa kweli na kuchambua matokeo kwa kuendelea.

Kwa mfano, unaweza kufuatilia viwango vya mafanikio, alama za kuridhika kwa watumiaji, au vigezo vingine kwenye trafiki ya moja kwa moja. Faida ya tathmini mtandaoni ni kwamba **inakamata vitu ambavyo huenda hukutegemea kwenye maabara** – unaweza kuona mabadiliko ya modeli kwa muda (ikiwa ufanisi wa wakala unapungua wakati muundo wa pembejeo unabadilika) na kugundua maswali yasiyotarajiwa au hali ambazo hazikuwa kwenye data yako ya mtihani​. Inatoa picha halisi ya jinsi wakala anavyofanya kazi katika mazingira ya kweli.

Tathmini mtandaoni mara nyingi inahusisha kukusanya maoni ya wazi na yasiyo ya moja kwa moja kutoka kwa watumiaji, kama ilivyojadiliwa, na huenda kuendesha majaribio ya kivuli au majaribio ya A/B (ambapo toleo jipya la wakala linaendeshwa sambamba ili kulinganisha na toleo la zamani). Changamoto ni kwamba inaweza kuwa ngumu kupata lebo au alama za kuaminika kwa mwingiliano wa moja kwa moja – unaweza kutegemea maoni ya watumiaji au vigezo vinavyofuata (kama mtumiaji alibonyeza matokeo).

### Kuunganisha zote mbili

Tathmini mtandaoni na nje ya mtandao sio za kutenganishwa; zinaendana vizuri. Maarifa kutoka kwa ufuatiliaji mtandaoni (mfano, aina mpya za maswali ya watumiaji ambapo wakala anafanya vibaya) yanaweza kutumika kuongeza na kuboresha seti za majaribio za nje ya mtandao. Kinyume chake, wakala wanaofanya vizuri katika majaribio ya nje ya mtandao wanaweza kupelekwa kwa uhakika zaidi na kufuatiliwa mtandaoni.

Kwa kweli, timu nyingi zinachukua mzunguko:

_tathmini nje ya mtandao -> tuma uzalishaji -> fuatilia mtandaoni -> kusanya kesi mpya za kushindwa -> ongeza kwenye seti ya nje ya mtandao -> boresha wakala -> rudia_.

## Masuala ya Kawaida

Unapopeleka wakala za AI uzalishaji, unaweza kukutana na changamoto mbalimbali. Hapa kuna baadhi ya masuala ya kawaida na suluhisho zao zinazowezekana:

| **Tatizo**    | **Suluhisho Linawezekana**   |
| ------------- | ------------------ |
| Wakala wa AI hauendeshi kazi kwa uthabiti | - Fanyia marekebisho maelekezo yaliyotolewa kwa Wakala wa AI; kuwa wazi kuhusu malengo.<br>- Tambua sehemu ambapo kugawa kazi kuwa madogo na kuzishughulikia na wakala wengi kunaweza kusaidia. |
| Wakala wa AI unaingia katika mizunguko ya kuendelea  | - Hakikisha una vigezo vya kusitisha vya wazi ili Wakala ajue lini kusitisha mchakato.<br>- Kwa kazi ngumu zinazohitaji fikra na upangaji, tumia modeli kubwa ambayo imeabadilishwa kwa kazi za msingi wa fikra. |
| Miito ya zana za Wakala haifanyi vizuri   | - Jaribu na thibitisha matokeo ya zana nje ya mfumo wa wakala.<br>- Fanyia marekebisho vigezo vilivyofafanuliwa, prompts, na majina ya zana.  |
| Mfumo wa Wakala Wengi hauendeshi kwa uthabiti | - Fanyia marekebisho prompts zinazotolewa kwa kila wakala kuhakikisha zinaeleweka na kutofautiana kati yao.<br>- Jenga mfumo wa ngazi kwa kutumia wakala wa "routing" au mtawala kuamua ni wakala gani anayefaa. |

Mengi ya masuala haya yanaweza kutambulika kwa ufanisi zaidi ikiwa ufuatiliaji uko mahali. Traces na vigezo tulivyoyajadili hapo juu husaidia kubainisha hasa wapi katika mtiririko wa kazi za wakala matatizo yanatokea, na kufanya urekebishaji na uboreshaji kuwa wa ufanisi zaidi.

## Kusimamia Gharama
Hapa kuna baadhi ya mikakati ya kupunguza gharama za kupeleka mawakala wa AI ndani ya uzalishaji:

**Using Smaller Models:** Modeli Ndogo za Lugha (SLMs) zinaweza kufanya vizuri kwa baadhi ya matukio ya matumizi ya wakala na zitapunguza gharama kwa kiasi kikubwa. Kama ilivyoelezwa awali, kujenga mfumo wa tathmini ili kubaini na kulinganisha utendaji dhidi ya modeli kubwa ni njia bora ya kuelewa jinsi SLM itakavyofanya kazi katika kesi yako ya matumizi. Fikiria kutumia SLMs kwa kazi rahisi kama vile upangaji wa nia au uchimbaji wa vigezo, wakati ukihifadhi modeli kubwa kwa mantiki ngumu.

**Using a Router Model:** Mkakati sawa ni kutumia utofauti wa modeli na ukubwa. Unaweza kutumia LLM/SLM au serverless function kupitisha maombi kulingana na ugumu kwa modeli zinazofaa zaidi. Hii pia itasaidia kupunguza gharama sambamba na kuhakikisha utendaji kwa kazi zinazofaa. Kwa mfano, panga maswali rahisi kwa modeli ndogo, za haraka, na tumia modeli kubwa, za gharama kubwa, tu kwa kazi za kufikiri kwa kiwango cha juu.

**Caching Responses:** Kutambua maombi na kazi zinazojirudia na kutoa majibu kabla hayajakupitia mfumo wako wa wakala ni njia nzuri ya kupunguza wingi wa maombi yanayofanana. Unaweza hata kutekeleza mchakato wa kutambua jinsi ombi linavyofanana na maombi yako yaliyohifadhiwa katika cache kwa kutumia modeli za AI za msingi. Mkakati huu unaweza kupunguza gharama kwa kiasi kikubwa kwa maswali yanayoulizwa mara kwa mara au mtiririko wa kazi wa kawaida.

## Hebu tuone jinsi hii inavyofanya kazi kwa vitendo

Katika [daftari la mfano la sehemu hii](./code_samples/10-expense_claim-demo.ipynb), tutaona mifano ya jinsi tunavyoweza kutumia zana za ufuatiliaji (observability tools) kufuatilia na kutathmini wakala wetu.


### Una Maswali Zaidi kuhusu Mawakala wa AI katika Uzalishaji?

Jiunge na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ili kukutana na wanafunzi wengine, kuhudhuria saa za ofisi na kupata majibu kwa maswali yako kuhusu Mawakala wa AI.

## Somo Lililopita

[Mfano wa Ubunifu wa Metacognition](../09-metacognition/README.md)

## Somo Linalofuata

[Itifaki za Wakala](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Taarifa ya kutolea dhamana:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kufikia usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au ukosefu wa usahihi. Nyaraka ya asili katika lugha yake inapaswa kuchukuliwa kama chanzo cha kuaminika. Kwa taarifa muhimu, inapendekezwa kutumia tafsiri iliyofanywa na mtaalamu wa lugha. Hatuwajibiki kwa kutokuelewana au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->