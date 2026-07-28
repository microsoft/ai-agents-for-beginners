# Mawakala wa AI Katika Uzalishaji: Uwezekano wa Kuangalia & Tathmini

[![AI Agents in Production](../../../translated_images/sw/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Wakati mawakala wa AI wanapoenda kutoka majaribio ya maumbile hadi matumizi halisi duniani, uwezo wa kuelewa tabia zao, kufuatilia utendaji wao, na kutathmini matokeo yao kwa mfumo unakuwa muhimu.

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utajua jinsi ya/kuelewa:
- Misingi ya uwezekano wa kuangalia mawakala na tathmini
- Mbinu za kuboresha utendaji, gharama, na ufanisi wa mawakala
- Nini na jinsi ya kutathmini mawakala wako wa AI kwa mfumo
- Jinsi ya kudhibiti gharama unapotuma mawakala wa AI uzalishaji
- Jinsi ya kuingiza vyombo vya mawakala waliotengenezwa kwa Microsoft Agent Framework

Lengo ni kukupa maarifa ya kubadilisha mawakala wako wa "kiboksi-kisichoonekana" kuwa mifumo wazi, inayoweza kudhibitiwa, na yenye kuaminika.

_**Kumbuka:** Ni muhimu kusambaza mawakala wa AI ambayo ni salama na yanaaminika. Angalia somo la [Kujenga Mawakala wa AI wa Kuaminika](../06-building-trustworthy-agents/README.md) pia._

## Mfuatano na Mipaka

Vifaa vya uwezekano wa kuangalia kama [Langfuse](https://langfuse.com/) au [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) kwa kawaida huwakilisha kuendesha mawakala kama mfuatano na mipaka.

- **Mfuatano** unaonyesha kazi kamili ya wakala kutoka mwanzo mpaka mwisho (kama kushughulikia swali la mtumiaji).
- **Mipaka** ni hatua za mtu binafsi ndani ya mfuatano (kama kupiga simu kwa mfano wa lugha au kupata data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bila uwezekano wa kuangalia, wakala wa AI anaweza kuhisi kama "kiboksi-kisichoonekana" - hali yake ya ndani na hoja ni wazi kidogo, na kufanya iwe vigumu kutambua matatizo au kuboresha utendaji. Kwa uwezekano wa kuangalia, mawakala huwa "viboksi vya kioo," vinavyotoa uwazi muhimu kwa ujenzi wa imani na kuhakikisha wanafanya kazi kama ilivyokusudiwa.

## Kwa Nini Uwezekano wa Kuangalia Ni Muhimu Katika Mazingira ya Uzalishaji

Kuhamisha mawakala wa AI kwenda mazingira ya uzalishaji huleta changamoto na mahitaji mapya. Uwezekano wa kuangalia si tena "ya kupendeza kuwa nayo" bali ni uwezo muhimu:

*   **Urekebishaji na Uchambuzi wa Chanzo Msingi**: Wakati wakala akishindwa au kutoa matokeo yasiyotarajiwa, vifaa vya uwezekano wa kuangalia hutia mfuatano unaohitajika kupata chanzo cha kosa. Hii ni muhimu hasa katika mawakala tata wanaoweza kujumuisha simu nyingi za LLM, mwingiliano wa zana, na mantiki ya masharti.
*   **Usimamizi wa Muda wa Kicheleweshaji na Gharama**: Mawakala wa AI mara nyingi hutegemea LLM na API zingine za nje zinazolipishwa kwa tokeni au kwa simu. Uwezekano wa kuangalia unaruhusu ufuatiliaji sahihi wa simu hizi, kusaidia kubaini shughuli ambazo ni polepole au ghali sana. Hii inawawezesha timu kuboresha maelekezo, kuchagua mifano yenye ufanisi zaidi, au kubuni upya mchakato wa kazi kudhibiti gharama za uendeshaji na kuhakikisha uzoefu mzuri wa mtumiaji.
*   **Imani, Usalama, na Uzingatiaji Sheria**: Katika matumizi mengi, ni muhimu kuhakikisha kuwa mawakala hufanya kazi kwa usalama na kwa maadili. Uwezekano wa kuangalia hutoa njia ya ukaguzi wa hatua na maamuzi ya wakala. Hii inaweza kutumika kugundua na kupunguza matatizo kama vile sindano za maelekezo, uzalishaji wa maudhui hatarishi, au kushughulikia vibaya taarifa binafsi zinazomtambua mtu (PII). Kwa mfano, unaweza kupitia mfuatano kuelewa kwa nini wakala alitoa majibu fulani au alitumia zana maalum.
*   **Mizunguko ya Uboreshaji Endelevu**: Data ya uwezekano wa kuangalia ni msingi wa mchakato wa maendeleo wa iterative. Kwa kufuatilia jinsi mawakala wanavyofanya kazi duniani halisi, timu zinaweza kubaini maeneo ya kuboresha, kukusanya data kwa ajili ya kufinyanga mifano, na kuthibitisha athari za mabadiliko. Hii huunda mzunguko wa maoni ambapo maarifa kutoka kwa tathmini ya mtandaoni yanajumuishwa katika majaribio na ubunifu wa nje ya mtandao, na kusababisha utendaji bora wa wakala kwa hatua.

## Vipimo Muhimu vya Kufuatilia

Ili kufuatilia na kuelewa tabia ya wakala, aina mbalimbali za vipimo na ishara zinapaswa kufuatiliwa. Ingawa vipimo maalum vinaweza kutofautiana kulingana na lengo la wakala, baadhi ni muhimu sana kwa ujumla.

Hapa kuna baadhi ya vipimo maarufu vinavyofuatiliwa na vifaa vya uwezekano wa kuangalia:

**Kicheleweshaji:** Je, wakala hutoa majibu kwa haraka kiasi gani? Muda mrefu wa kusubiri huathiri uzoefu wa mtumiaji vibaya. Unapaswa kupima kicheleweshaji kwa kazi na hatua binafsi kwa kufuatilia kuendesha kwa wakala. Kwa mfano, wakala anayechukua sekunde 20 kwa simu zote za mfano anaweza kuharakishwa kwa kutumia mfano wa haraka zaidi au kwa kuendesha simu za mfano kwa wakati mmoja.

**Gharama:** Ni kiasi gani cha gharama kwa kuendesha wakala mmoja? Mawakala wa AI hutegemea simu za LLM zinazolipishwa kwa tokeni au API za nje. Matumizi ya mara kwa mara ya zana au maelekezo mengi yanaweza kuongeza gharama kwa haraka. Kwa mfano, ikiwa wakala anaita LLM mara tano kwa kuboresha ubora kidogo, lazima tathmini kama gharama inakubalika au kama unaweza kupunguza idadi ya simu au kutumia mfano wa bei nafuu. Ufuatiliaji wa wakati halisi pia unaweza kusaidia kugundua mizunguko isiyotegemewa (kwa mfano, mende zinazosababisha mizunguko mingi ya API).

**Makosa ya Maombi:** Ni maombi mangapi ambayo wakala ameshindwa? Hii inaweza kujumuisha makosa ya API au simu za zana zilizoshindwa. Ili kufanya wakala wako kuwa imara zaidi dhidi ya haya katika uzalishaji, unaweza basi kuweka mbadala au jaribio la upya. Mfano: ikiwa mtoa huduma wa LLM A hayupo mtandaoni, unabadilisha kwenda kwa mtoa huduma wa LLM B kama msaada.

**Maoni ya Mtumiaji:** Kutekeleza tathmini za moja kwa moja za watumiaji hutoa maarifa muhimu. Hii inaweza kujumuisha alama za wazi (👍kidole juu/👎chini, ⭐nyota 1-5) au maoni ya maandishi. Maoni hasi yanayorudiwa mara kwa mara yanapaswa kukuamsha kwa maana wakala haifanyi kazi kama ilivyotarajiwa.

**Maoni Yasiyo ya Mwongozo ya Mtumiaji:** Tabia za watumiaji hutoa maoni ya moja kwa moja hata bila alama za wazi. Hii inaweza kujumuisha kurekebisha swali mara moja, kuuliza maswali yanayojirudia au kubofya kitufe cha jaribio la upya. Mfano: ikiwa unaona watumiaji wakiuliza swali moja mara nyingi, hii ni ishara kwamba wakala haifanyi kazi kama inavyotarajiwa.

**Usahihi:** Mara ngapi wakala hutengeneza matokeo sahihi au yanayotarajiwa? Maana ya usahihi hutofautiana (mfano, utatuzi wa tatizo sahihi, usahihi wa kupata taarifa, kuridhika kwa mtumiaji). Hatua ya kwanza ni kufafanua mafanikio yanaonekana vipi kwa wakala wako. Unaweza kufuatilia usahihi kwa ukaguzi wa otomatiki, alama za tathmini, au lebo za ukamilifu wa kazi. Kwa mfano, kuweka mfuatano kama "ulifanikiwa" au "ulifeli".

**Vipimo vya Tathmini za Otomatiki:** Pia unaweza kuweka tathmini za otomatiki. Mfano, unaweza kutumia LLM kupima matokeo ya wakala kama ni ya msaada, sahihi, au la. Kuna pia maktaba kadhaa za chanzo wazi zinazokusaidia kupima vipengele tofauti vya wakala. Mfano: [RAGAS](https://docs.ragas.io/) kwa mawakala wa RAG au [LLM Guard](https://llm-guard.com/) kugundua lugha hatarishi au sindano za maelekezo.


Katika vitendo, mchanganyiko wa vipimo hivi hutoa mfukuzo bora wa afya ya wakala wa AI. Katika [noti ya mfano](./code_samples/10-expense_claim-demo.ipynb) katika sura hii, tutaonyesha jinsi vipimo hivi vinavyoonekana katika mifano halisi lakini kwanza, tutajifunza jinsi mtiririko wa tathmini kawaida unavyoonekana.

## Changanua Wakala Wako

Ili kukusanya data za ufuatiliaji, utahitaji kuchanganua msimbo wako. Lengo ni kuchanganua msimbo wa wakala ili kutoa nyaraka na vipimo vinavyoweza kushikiliwa, kuchakatwa, na kuonyeshwa na jukwaa la uangalizi.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) imeibuka kuwa kiwango cha tasnia kwa uangalizi wa LLM. Hutoa seti ya API, SDK, na zana za kuzalisha, kukusanya, na kusafirisha data za telemetry.

Kuna maktaba nyingi za uchanganaji ambazo zinazunguka mifumo ya wakala iliyopo na kurahisisha kusafirisha vipindi vya OpenTelemetry kwa zana ya uangalizi. Microsoft Agent Framework inaunganisha moja kwa moja na OpenTelemetry. Hapa chini ni mfano wa kuchanganua wakala wa MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Utekelezaji wa wakala unafuatiliwa moja kwa moja
    pass
```

[Noti ya mfano](./code_samples/10-expense_claim-demo.ipynb) katika sura hii itaonyesha jinsi ya kuchanganua wakala wako wa MAF.

**Uundaji wa Vipindi kwa Mikono:** Wakati maktaba za uchanganaji hutoa msingi mzuri, mara nyingi kuna kesi ambapo taarifa za kina zaidi au maalum zinahitajika. Unaweza kuunda vipindi kwa mikono kuongeza mantiki maalum ya programu. Muhimu zaidi, vinaweza kuimarishwa kwa njia ya moja kwa moja au kwa mikono na sifa maalum (zinazoitwa pia lebo au metadata). Sifa hizi zinaweza kujumuisha data maalum ya biashara, hesabu za kati, au muktadha wowote ambao unaweza kuwa muhimu kwa uchunguzi au uchambuzi, kama `user_id`, `session_id`, au `model_version`.

Mfano wa kuunda nyaraka na vipindi kwa mikono kwa kutumia [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Tathmini ya Wakala

Uangalizi hutupatia vipimo, lakini tathmini ni mchakato wa kuchambua data hiyo (na kufanya majaribio) ili kubaini jinsi wakala wa AI anavyofanya kazi vizuri na jinsi gani anaweza kuboreshwa. Kwa maneno mengine, mara unapo kuwa na nyaraka na vipimo hivyo, unawezaje kuvitumia kutathmini wakala na kufanya maamuzi?

Tathmini ya kawaida ni muhimu kwa sababu mawakala wa AI mara nyingi hawazingatii sheria kwa ukamilifu na wanaweza kubadilika (kupitia masasisho au mabadiliko ya tabia ya mfano) – bila tathmini, usingejua kama “wakala werevu” anafanya kazi yake vizuri au ameanguka nyuma.

Kuna makundi mawili ya tathmini kwa mawakala wa AI: **tathmini ya mtandaoni** na **tathmini ya nje ya mtandao**. Zote ni muhimu, na zinaongeza thamani kwa kila mmoja. Kwa kawaida huanza na tathmini ya nje ya mtandao, kwani hili ndilo hatua ya chini inayohitajika kabla ya kupeleka wakala wowote.

### Tathmini ya Nje ya Mtandao

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Hii inahusisha kutathmini wakala katika mazingira yaliyodhibitiwa, kawaida kwa kutumia seti za majaribio, si maombi ya watumiaji wa moja kwa moja. Unatumia seti za data zilizochaguliwa ambapo unajua matokeo yanayotarajiwa au tabia sahihi, kisha unamfanya wakala wako kufanya kazi hizo.

Kwa mfano, kama umejenga wakala wa matatizo ya neno la hisabati, unaweza kuwa na [seti ya data ya majaribio](https://huggingface.co/datasets/gsm8k) ya matatizo 100 yenye majibu yanayojulikana. Tathmini ya nje ya mtandao mara nyingi hufanywa wakati wa maendeleo (na inaweza kuwa sehemu ya mizunguko ya CI/CD) ili kuchunguza maboresho au kuzuia kuporomoka. Faida ni kwamba ni **inayoweza kurudiwa na unaweza kupata vipimo wazi vya usahihi kwa kuwa unayo ukweli wa msingi**. Pia unaweza kuiga maombi ya watumiaji na kupima majibu ya wakala dhidi ya majibu bora au kutumia vipimo vya moja kwa moja kama vilivyoelezwa hapo juu.

Changamoto kuu na tathmini ya nje ya mtandao ni kuhakikisha seti yako ya majaribio ni kamilifu na inaendelea kuwa ya kisasa – wakala anaweza kufanya kazi vizuri kwenye seti ya majaribio iliyowekwa lakini kukutana na maombi tofauti sana katika utengenezaji wa bidhaa. Kwa hiyo, unapaswa kusasisha seti za majaribio na kesi mpya za kipekee na mifano inayoonyesha hali halisi za dunia​. Mchanganyiko wa kesi ndogo za "mtihani wa moshi" na seti kubwa za tathmini ni muhimu: seti ndogo kwa ukaguzi wa haraka na kubwa kwa vipimo vya utendaji vya pana​.

### Tathmini ya Mtandaoni

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Hii inamaanisha kutathmini wakala katika mazingira ya moja kwa moja, ya kweli duniani, yani wakati wa matumizi halisi katika utengenezaji wa bidhaa. Tathmini ya mtandaoni inahusisha ufuatiliaji wa utendaji wa wakala katika mwingiliano wa watumiaji halisi na uchambuzi wa matokeo kwa wakati wote.

Kwa mfano, unaweza kufuatilia viwango vya mafanikio, alama za kuridhika kwa mtumiaji, au vipimo vingine kwenye trafiki ya moja kwa moja. Faida ya tathmini ya mtandaoni ni kwamba inakamata mambo ambayo huenda usiyatarajia katika mazingira ya maabara – unaweza kuona mabadiliko ya mfano kwa muda (ikiwa ufanisi wa wakala unaporomoka kadri mifumo ya pembejeo inavyobadilika) na kugundua maombi au hali zisizotarajiwa ambazo hazikuwepo katika data yako ya majaribio​. Inatoa picha halisi ya jinsi wakala anavyojitendea mwilini.

Tathmini ya mtandaoni mara nyingi inahusisha ukusanyaji wa maoni ya watumiaji kwa njia ya moja kwa moja na wazi, kama ilivyojadiliwa, na huenda ukafanya majaribio ya kivuli au majaribio ya A/B (ambapo toleo jipya la wakala linaendeshwa sambamba kulinganisha na la zamani). Changamoto ni kwamba inaweza kuwa vigumu kupata lebo au alama za kuaminika kwa mwingiliano wa moja kwa moja – unaweza kutegemea maoni ya watumiaji au vipimo vya chini ya mto (kama mtumiaji kubofya matokeo).

### Kuchanganya Mbili Hizo

Tathmini za mtandaoni na nje ya mtandao si zilezi; zinatumika kama nyongeza kwa kila mmoja. Maarifa kutoka kwa ufuatiliaji wa mtandaoni (mfano, aina mpya za maombi ya watumiaji ambapo wakala anafanya vibaya) yanaweza kutumika kuongeza na kuboresha seti za majaribio ya nje ya mtandao. Kinyume chake, mawakala wanaofanya vizuri katika majaribio ya nje ya mtandao wanaweza kisha kupelekwa na kufuatiliwa kwa kujiamini zaidi mtandaoni.

Kwa kweli, timu nyingi hutumia mzunguko:

_tathmini nje ya mtandao -> peleka -> fuatilia mtandaoni -> kusanya kesi mpya za kushindwa -> ongeza kwenye seti ya majaribio ya nje ya mtandao -> boresha wakala -> rudia_.

## Masuala ya Kawaida

Unapowapeleka mawakala wa AI utengenezaji wa bidhaa, unaweza kukutana na changamoto mbalimbali. Hapa kuna masuala ya kawaida na suluhisho la huenda likafaa:

| **Tatizo**    | **Suluhisho Lisilowezekana**   |
| ------------- | ------------------ |
| Wakala wa AI haufanyi kazi kwa urahisi | - Boresha onyo linalotolewa kwa Wakala wa AI; kuwa wazi kuhusu malengo.<br>- Tambua sehemu za kugawanya kazi kuwa kazi ndogo ndogo na kuzisimamia na mawakala wengi inaweza kusaidia. |
| Wakala wa AI anakumbana na mizunguko isiyoisha | - Hakikisha una masharti wazi ya kumaliza ili Wakala ajue lini kusitisha mchakato.<br>- Kwa kazi ngumu zinazohitaji hoja na mipango, tumia mfano mkubwa zaidi maalum kwa kazi za kuhoji. |
| Mito ya zana za Wakala wa AI haufanyi kazi vizuri | - Jaribu na thibitisha matokeo ya zana nje ya mfumo wa wakala.<br>- Boresha vigezo vilivyowekwa, onyo, na majina ya zana. |
| Mfumo wa Mawakala Wengi haufanyi kazi kwa urahisi | - Boresha onyo linalotolewa kwa kila wakala ili kuhakikisha ni maalum na tofauti kutoka kwa wengine.<br>- Jenga mfumo wa mfuatiliaji unaotumia wakala wa "uratibu" au mdhibiti kuamua ni wakala gani sahihi. |


Masuala mengi ya aina hii yanaweza kubainishwa kwa ufanisi zaidi ukiwa na uwezo wa uangalizi uliowekwa. Mfuatano na vipimo tulivyoyajadili mapema husaidia kubaini mahali hasa katika mtiririko wa kazi wa wakala ambapo matatizo hutokea, na kufanya utambuzi wa hitilafu na uboreshaji kuwa rahisi zaidi.

## Kusimamia Gharama


Hapa kuna mikakati kadhaa ya kudhibiti gharama za kupeleka mawakala wa AI katika uzalishaji:

**Kutumia Modeli Ndogo:** Modeli Ndogo za Lugha (SLMs) zinaweza kufanya vizuri kwa baadhi ya matumizi ya mawakala na zitapunguza gharama kwa kiasi kikubwa. Kama ilivyotajwa hapo awali, kujenga mfumo wa tathmini ili kubaini na kulinganisha utendaji dhidi ya modeli kubwa ni njia bora ya kuelewa jinsi SLM itakavyofanya kazi kwa matumizi yako. Fikiria kutumia SLM kwa kazi rahisi kama upangaji wa nia au uchukuaji wa vigezo, huku ukihifadhi modeli kubwa kwa ajili ya hoja ngumu.

**Kutumia Modeli ya Router:** Mkakati sawa ni kutumia tofauti za modeli na ukubwa. Unaweza kutumia LLM/SLM au huduma isiyo na server kuongoza ombi kulingana na ugumu kwa modeli zinazofaa zaidi. Hii pia itasaidia kupunguza gharama huku ikihakikisha utendaji kwa kazi sahihi. Kwa mfano, tuma maswali rahisi kwa modeli ndogo na za haraka, na tumia modeli kubwa za gharama kubwa kwa kazi za hoja ngumu tu.

**Kuweka Majibu Kwenye Cache:** Kubaini maombi na kazi zinazojirudia na kutoa majibu kabla ya kupitia kwenye mfumo wako wa mawakala ni njia nzuri ya kupunguza kiasi cha maombi yanayofanana. Unaweza hata kutekeleza mchakato wa kubaini jinsi ombi linavyofanana na maombi yaliyo kwenye cache kwa kutumia modeli za AI za msingi zaidi. Mkakati huu unaweza kupunguza gharama kwa kiasi kikubwa kwa maswali yanayoulizwa mara kwa mara au michakato ya kawaida.

## Tuweze kuona jinsi hili linavyofanya kazi kwa vitendo

Katika [noti ya mfano ya sehemu hii](./code_samples/10-expense_claim-demo.ipynb), tutaona mifano ya jinsi tunavyoweza kutumia zana za ufuatiliaji kuangalia na kutathmini wakala wetu.


### Una Maswali Zaidi kuhusu Wakala wa AI katika Uzalishaji?

Jiunge na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kukutana na wanafunzi wengine, kuhudhuria saa za ofisi na kupata majibu ya maswali yako kuhusu Wakala wa AI.

## Somo lililopita

[Kiolezo cha Ubunifu wa Metakognishaji](../09-metacognition/README.md)

## Somo lijalo

[Itifaki za Mawakala](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->