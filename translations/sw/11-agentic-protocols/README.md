<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T15:24:24+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "sw"
}
-->
# Kutumia Itifaki za Wakala (MCP, A2A na NLWeb)

[![Itifaki za Wakala](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.sw.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Bofya picha hapo juu kutazama video ya somo hili)_

Kadri matumizi ya mawakala wa AI yanavyoongezeka, ndivyo hitaji la itifaki zinazohakikisha viwango, usalama, na kuunga mkono uvumbuzi wa wazi linavyoongezeka. Katika somo hili, tutajadili itifaki 3 zinazolenga kukidhi hitaji hili - Model Context Protocol (MCP), Agent to Agent (A2A) na Natural Language Web (NLWeb).

## Utangulizi

Katika somo hili, tutajadili:

• Jinsi **MCP** inavyowezesha Mawakala wa AI kufikia zana za nje na data ili kukamilisha majukumu ya mtumiaji.

• Jinsi **A2A** inavyowezesha mawasiliano na ushirikiano kati ya mawakala tofauti wa AI.

• Jinsi **NLWeb** inavyowaletea tovuti kiolesura cha lugha asilia, kuwezesha Mawakala wa AI kugundua na kuingiliana na maudhui.

## Malengo ya Kujifunza

• **Tambua** madhumuni ya msingi na faida za MCP, A2A, na NLWeb katika muktadha wa mawakala wa AI.

• **Eleza** jinsi kila itifaki inavyorahisisha mawasiliano na mwingiliano kati ya LLMs, zana, na mawakala wengine.

• **Tambua** majukumu tofauti ya kila itifaki katika kujenga mifumo changamano ya mawakala.

## Model Context Protocol

**Model Context Protocol (MCP)** ni kiwango cha wazi kinachotoa njia sanifu kwa programu kutoa muktadha na zana kwa LLMs. Hii inaruhusu "kiunganishi cha ulimwengu wote" kwa vyanzo tofauti vya data na zana ambazo Mawakala wa AI wanaweza kuunganishwa nazo kwa njia thabiti.

Hebu tuangalie vipengele vya MCP, faida ikilinganishwa na matumizi ya API moja kwa moja, na mfano wa jinsi Mawakala wa AI wanaweza kutumia seva ya MCP.

### Vipengele vya Msingi vya MCP

MCP inafanya kazi kwa **muundo wa mteja-seva**, na vipengele vyake vya msingi ni:

• **Hosts** ni programu za LLM (kwa mfano, mhariri wa msimbo kama VSCode) zinazozindua miunganisho na Seva ya MCP.

• **Clients** ni vipengele ndani ya programu ya host vinavyodumisha miunganisho ya moja kwa moja na seva.

• **Servers** ni programu nyepesi zinazotoa uwezo maalum.

Itifaki inajumuisha dhana tatu za msingi ambazo ni uwezo wa Seva ya MCP:

• **Tools**: Hizi ni vitendo au kazi maalum ambazo wakala wa AI anaweza kuita ili kutekeleza hatua. Kwa mfano, huduma ya hali ya hewa inaweza kutoa zana ya "pata hali ya hewa," au seva ya biashara mtandaoni inaweza kutoa zana ya "nunua bidhaa." Seva za MCP zinatangaza jina la kila zana, maelezo, na muundo wa pembejeo/mazao katika orodha ya uwezo wao.

• **Resources**: Hizi ni vipengele vya data au nyaraka zinazoweza kusomwa tu ambazo seva ya MCP inaweza kutoa, na wateja wanaweza kuzipata kwa mahitaji. Mifano ni pamoja na maudhui ya faili, rekodi za hifadhidata, au faili za kumbukumbu. Rasilimali zinaweza kuwa maandishi (kama msimbo au JSON) au binary (kama picha au PDF).

• **Prompts**: Hizi ni templeti zilizotayarishwa mapema zinazotoa maoni ya maelekezo, kuruhusu mtiririko wa kazi changamano zaidi.

### Faida za MCP

MCP inatoa faida kubwa kwa Mawakala wa AI:

• **Ugunduzi wa Zana kwa Njia ya Kielektroniki**: Mawakala wanaweza kupokea orodha ya zana zinazopatikana kutoka kwa seva pamoja na maelezo ya kazi zao. Hii ni tofauti na API za jadi, ambazo mara nyingi zinahitaji usimbaji tuli kwa miunganisho, ikimaanisha mabadiliko yoyote ya API yanahitaji masasisho ya msimbo. MCP inatoa mbinu ya "unganisha mara moja," ikileta uwezo wa kubadilika zaidi.

• **Uingiliano Kati ya LLMs**: MCP inafanya kazi kati ya LLMs tofauti, ikitoa kubadilika kwa kubadilisha mifano ya msingi ili kutathmini utendaji bora.

• **Usalama Sanifu**: MCP inajumuisha mbinu sanifu ya uthibitishaji, ikiboresha upanuzi wakati wa kuongeza ufikiaji kwa seva za MCP za ziada. Hii ni rahisi kuliko kusimamia funguo tofauti na aina za uthibitishaji kwa API za jadi.

### Mfano wa MCP

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.sw.png)

Fikiria mtumiaji anataka kuweka nafasi ya ndege kwa kutumia msaidizi wa AI unaotumia MCP.

1. **Muunganisho**: Msaidizi wa AI (mteja wa MCP) unaunganishwa na seva ya MCP inayotolewa na shirika la ndege.

2. **Ugunduzi wa Zana**: Mteja anauliza seva ya MCP ya shirika la ndege, "Ni zana gani unazo?" Seva inajibu na zana kama "tafuta ndege" na "weka nafasi ya ndege."

3. **Kuitisha Zana**: Kisha unauliza msaidizi wa AI, "Tafadhali tafuta ndege kutoka Portland kwenda Honolulu." Msaidizi wa AI, akitumia LLM yake, anatambua kuwa anahitaji kuita zana ya "tafuta ndege" na kupitisha vigezo husika (asili, marudio) kwa seva ya MCP.

4. **Utekelezaji na Majibu**: Seva ya MCP, ikifanya kama kifuniko, inafanya wito halisi kwa API ya ndani ya shirika la ndege. Kisha inapokea taarifa za ndege (kwa mfano, data ya JSON) na kuirudisha kwa msaidizi wa AI.

5. **Mwingiliano Zaidi**: Msaidizi wa AI anawasilisha chaguo za ndege. Mara unapochagua ndege, msaidizi anaweza kuita zana ya "weka nafasi ya ndege" kwenye seva hiyo hiyo ya MCP, kukamilisha uhifadhi.

## Itifaki ya Wakala kwa Wakala (A2A)

Wakati MCP inazingatia kuunganisha LLMs na zana, **Itifaki ya Wakala kwa Wakala (A2A)** inachukua hatua zaidi kwa kuwezesha mawasiliano na ushirikiano kati ya mawakala tofauti wa AI. A2A inaunganisha mawakala wa AI katika mashirika tofauti, mazingira, na mifumo ya teknolojia ili kukamilisha jukumu la pamoja.

Tutachunguza vipengele na faida za A2A, pamoja na mfano wa jinsi inaweza kutumika katika programu yetu ya kusafiri.

### Vipengele vya Msingi vya A2A

A2A inazingatia kuwezesha mawasiliano kati ya mawakala na kuwafanya wafanye kazi pamoja kukamilisha jukumu la mtumiaji. Kila kipengele cha itifaki huchangia hili:

#### Kadi ya Wakala

Kama vile seva ya MCP inavyoshiriki orodha ya zana, Kadi ya Wakala ina:

- Jina la Wakala.  
- **Maelezo ya majukumu ya jumla** anayokamilisha.  
- **Orodha ya ujuzi maalum** na maelezo kusaidia mawakala wengine (au hata watumiaji binadamu) kuelewa ni lini na kwa nini wangependa kumuita wakala huyo.  
- **URL ya sasa ya Endpoint** ya wakala.  
- **Toleo** na **uwezo** wa wakala kama majibu ya mtiririko na arifa za kusukuma.  

#### Mtekelezaji wa Wakala

Mtekelezaji wa Wakala anawajibika kwa **kupitisha muktadha wa mazungumzo ya mtumiaji kwa wakala wa mbali**, wakala wa mbali unahitaji hili ili kuelewa jukumu linalohitaji kukamilishwa. Katika seva ya A2A, wakala hutumia LLM yake mwenyewe kuchambua maombi yanayoingia na kutekeleza majukumu kwa kutumia zana zake za ndani.

#### Kifaa cha Kazi

Mara wakala wa mbali anapokamilisha jukumu lililoombwa, bidhaa ya kazi yake huundwa kama kifaa cha kazi. Kifaa cha kazi **kinajumuisha matokeo ya kazi ya wakala**, **maelezo ya kilichokamilishwa**, na **muktadha wa maandishi** uliotumwa kupitia itifaki. Baada ya kifaa cha kazi kutumwa, muunganisho na wakala wa mbali hufungwa hadi itakapohitajika tena.

#### Foleni ya Matukio

Kipengele hiki kinatumika kwa **kushughulikia masasisho na kupitisha ujumbe**. Ni muhimu hasa katika uzalishaji kwa mifumo ya mawakala ili kuzuia muunganisho kati ya mawakala kufungwa kabla ya jukumu kukamilika, hasa wakati nyakati za kukamilisha jukumu zinaweza kuchukua muda mrefu.

### Faida za A2A

• **Ushirikiano Ulioboreshwa**: Inawawezesha mawakala kutoka kwa wauzaji na majukwaa tofauti kuingiliana, kushiriki muktadha, na kufanya kazi pamoja, kuwezesha otomatiki bila mshono katika mifumo ambayo kwa kawaida haijaunganishwa.  

• **Kubadilika kwa Uchaguzi wa Mfano**: Kila wakala wa A2A anaweza kuamua ni LLM gani anayotumia kuhudumia maombi yake, kuruhusu mifano iliyoboreshwa au iliyofanyiwa marekebisho kwa kila wakala, tofauti na muunganisho wa LLM moja katika baadhi ya hali za MCP.  

• **Uthibitishaji Uliojengwa Ndani**: Uthibitishaji umejumuishwa moja kwa moja katika itifaki ya A2A, ikitoa mfumo wa usalama thabiti kwa mwingiliano wa mawakala.  

### Mfano wa A2A

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.sw.png)

Hebu tuendelee na hali yetu ya uhifadhi wa safari, lakini wakati huu tukitumia A2A.

1. **Ombi la Mtumiaji kwa Wakala wa Wakala**: Mtumiaji anawasiliana na "Wakala wa Kusafiri" mteja/wakala wa A2A, labda kwa kusema, "Tafadhali weka safari nzima kwenda Honolulu kwa wiki ijayo, ikijumuisha ndege, hoteli, na gari la kukodisha."

2. **Urari na Wakala wa Kusafiri**: Wakala wa Kusafiri anapokea ombi hili changamano. Anatumia LLM yake kufikiria kuhusu jukumu na kuamua kwamba anahitaji kuingiliana na mawakala wengine maalum.

3. **Mawasiliano Kati ya Mawakala**: Wakala wa Kusafiri kisha anatumia itifaki ya A2A kuunganishwa na mawakala wa chini, kama vile "Wakala wa Ndege," "Wakala wa Hoteli," na "Wakala wa Kukodisha Gari" ambao wameundwa na kampuni tofauti.

4. **Utekelezaji wa Majukumu Yaliyokabidhiwa**: Wakala wa Kusafiri anatuma majukumu maalum kwa mawakala hawa maalum (kwa mfano, "Tafuta ndege kwenda Honolulu," "Weka hoteli," "Kukodisha gari"). Kila mmoja wa mawakala hawa maalum, akiendesha LLM zake na kutumia zana zake (ambazo zinaweza kuwa seva za MCP wenyewe), anatekeleza sehemu yake maalum ya uhifadhi.

5. **Majibu Yaliyojumuishwa**: Mara mawakala wote wa chini wanapokamilisha majukumu yao, Wakala wa Kusafiri anakusanya matokeo (maelezo ya ndege, uthibitisho wa hoteli, uhifadhi wa gari la kukodisha) na kutuma majibu ya kina, kwa mtindo wa mazungumzo, kwa mtumiaji.

## Natural Language Web (NLWeb)

Tovuti zimekuwa njia kuu kwa watumiaji kufikia taarifa na data kwenye mtandao.

Hebu tuangalie vipengele tofauti vya NLWeb, faida za NLWeb, na mfano wa jinsi NLWeb inavyofanya kazi kwa kuangalia programu yetu ya kusafiri.

### Vipengele vya NLWeb

- **Programu ya NLWeb (Msimbo wa Huduma ya Msingi)**: Mfumo unaochakata maswali ya lugha asilia. Unaunganisha sehemu tofauti za jukwaa ili kuunda majibu. Unaweza kufikiria kama **injini inayowezesha vipengele vya lugha asilia** vya tovuti.

- **Itifaki ya NLWeb**: Hii ni **seti ya msingi ya sheria za mwingiliano wa lugha asilia** na tovuti. Inarudisha majibu katika muundo wa JSON (mara nyingi kwa kutumia Schema.org). Madhumuni yake ni kuunda msingi rahisi kwa "Mtandao wa AI," kwa njia sawa na HTML ilivyowezesha kushiriki nyaraka mtandaoni.

- **Seva ya MCP (Endpoint ya Model Context Protocol)**: Kila usanidi wa NLWeb pia hufanya kazi kama **seva ya MCP**. Hii inamaanisha inaweza **kushiriki zana (kama njia ya "uliza") na data** na mifumo mingine ya AI. Kwa vitendo, hii inafanya maudhui na uwezo wa tovuti kutumika na mawakala wa AI, kuruhusu tovuti kuwa sehemu ya "mfumo wa mawakala" mpana.

- **Mifano ya Kuweka Embedding**: Mifano hii hutumika **kubadilisha maudhui ya tovuti kuwa uwakilishi wa namba unaoitwa vectors** (embedding). Vectors hizi zinakamata maana kwa njia ambayo kompyuta zinaweza kulinganisha na kutafuta. Zinahifadhiwa katika hifadhidata maalum, na watumiaji wanaweza kuchagua mfano wa embedding wanaotaka kutumia.

- **Hifadhidata ya Vectors (Njia ya Kupata)**: Hifadhidata hii **inahifadhi embedding za maudhui ya tovuti**. Wakati mtu anauliza swali, NLWeb huangalia hifadhidata ya vectors ili kupata haraka taarifa inayofaa zaidi. Inatoa orodha ya haraka ya majibu yanayowezekana, yaliyopangwa kwa kufanana. NLWeb inafanya kazi na mifumo tofauti ya hifadhi ya vectors kama Qdrant, Snowflake, Milvus, Azure AI Search, na Elasticsearch.

### NLWeb kwa Mfano

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.sw.png)

Fikiria tovuti yetu ya uhifadhi wa safari tena, lakini wakati huu, inatumia NLWeb.

1. **Kuingiza Data**: Katalogi za bidhaa zilizopo za tovuti ya kusafiri (kwa mfano, orodha za ndege, maelezo ya hoteli, vifurushi vya ziara) zimeundwa kwa kutumia Schema.org au kupakiwa kupitia milisho ya RSS. Zana za NLWeb zinachukua data hii iliyoundwa, kuunda embedding, na kuziweka katika hifadhidata ya vectors ya ndani au ya mbali.

2. **Swali la Lugha Asilia (Binadamu)**: Mtumiaji anatembelea tovuti na, badala ya kuvinjari menyu, anaandika kwenye kiolesura cha mazungumzo: "Nipatie hoteli inayofaa kwa familia huko Honolulu yenye bwawa la kuogelea kwa wiki ijayo."

3. **Usindikaji wa NLWeb**: Programu ya NLWeb inapokea swali hili. Inatuma swali kwa LLM kwa uelewa na wakati huo huo inatafuta hifadhidata yake ya vectors kwa orodha za hoteli zinazofaa.

4. **Majibu Sahihi**: LLM inasaidia kutafsiri matokeo ya utafutaji kutoka hifadhidata, kutambua mechi bora kulingana na vigezo vya "inayofaa kwa familia," "bwawa la kuogelea," na "Honolulu," kisha kuunda jibu la lugha asilia. Muhimu, jibu linarejelea hoteli halisi kutoka katalogi ya tovuti, kuepuka taarifa zilizotungwa.

5. **Mwingiliano wa Wakala wa AI**: Kwa sababu NLWeb inahudumu kama seva ya MCP, wakala wa AI wa kusafiri wa nje pia anaweza kuunganishwa na NLWeb ya tovuti hii. Wakala wa AI anaweza kutumia njia ya `uliza` ya MCP kuuliza tovuti moja kwa moja: `uliza("Je, kuna mikahawa inayofaa kwa walaji wa mboga katika eneo la Honolulu inayopendekezwa na hoteli?")`. NLWeb ingechakata hili, ikitumia hifadhidata yake ya taarifa za mikahawa (ikiwa imepakiwa), na kurudisha jibu la JSON lililoundwa.

### Una Maswali Zaidi Kuhusu MCP/A2A/NLWeb?

Jiunge na [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ili kukutana na wanafunzi wengine, kuhudhuria masaa ya ofisi, na kupata majibu ya maswali yako kuhusu Mawakala wa AI.

## Rasilimali

- [MCP kwa Anayeanza](https://aka.ms/mcp-for-beginners)  
- [Hati za MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Repo ya NLWeb](https://github.com/nlweb-ai/NLWeb)  
- [Mwongozo wa Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)  

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.