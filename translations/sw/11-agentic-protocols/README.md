# Kutumia Itifaki za Agentic (MCP, A2A na NLWeb)

[![Agentic Protocols](../../../translated_images/sw/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Bofya picha hapo juu kutazama video ya somo hili)_

Kadiri matumizi ya mawakala wa AI yanavyoongezeka, ndivyo inavyoongezeka pia hitaji la itifaki zinazohakikisha muafaka, usalama, na kuunga mkono ubunifu huru. Katika somo hili, tutashughulikia itifaki 3 zinazotaka kukidhi hitaji hili - Itifaki ya Muktadha wa Mfano (MCP), Mwakala kwa Mwakala (A2A) na Mtandao wa Lugha Asili (NLWeb).

## Utangulizi

Katika somo hili, tutashughulikia:

• Jinsi **MCP** inavyoruhusu Mawakala wa AI kupata zana za nje na data kukamilisha kazi za mtumiaji.

• Jinsi **A2A** inavyowawezesha mawasiliano na ushirikiano kati ya mawakala tofauti wa AI.

• Jinsi **NLWeb** inavyobeba interfaces za lugha asili kwa tovuti yoyote, ikiruhusu Mawakala wa AI kugundua na kuingiliana na maudhui.

## Malengo ya Kujifunza

• **Tambua** kusudi kuu na faida za MCP, A2A, na NLWeb katika muktadha wa mawakala wa AI.

• **Eleza** jinsi kila itifaki inavyorahisisha mawasiliano na mwingiliano kati ya LLMs, zana, na mawakala wengine.

• **Tambua** majukumu tofauti ambayo kila itifaki huchukua katika kujenga mifumo tata ya agentic.

## Itifaki ya Muktadha wa Mfano

**Itifaki ya Muktadha wa Mfano (MCP)** ni kiwango wazi kinachotoa njia ya muafaka kwa programu kutoa muktadha na zana kwa LLMs. Hii inaruhusu "kiunganishi cha ulimwengu" kwa vyanzo tofauti vya data na zana ambazo Mawakala wa AI wanaweza kuunganishwa kwa njia thabiti.

Tuchunguze sehemu za MCP, faida zake ikilinganishwa na matumizi ya moja kwa moja ya API, na mfano wa jinsi mawakala wa AI wanaweza kutumia seva ya MCP.

### Sehemu za Msingi za MCP

MCP inafanya kazi kwa **muundo wa mteja-mtumuaji** na sehemu kuu ni:

• **Mwenyeji (Hosts)** ni programu za LLM (kwa mfano mhariri wa nambari kama VSCode) ambazo huanzisha miunganisho na seva ya MCP.

• **Wateja (Clients)** ni sehemu ndani ya programu mwenyeji zinazohifadhi miunganisho ya mtu kwa mtu na seva.

• **Seva (Servers)** ni programu nyepesi zinazotangaza uwezo maalum.

Katika itifaki kuna vitu vitatu vya msingi ambavyo ni uwezo wa seva ya MCP:

• **Zana (Tools)**: Hizi ni vitendo au kazi maalum ambazo wakala wa AI anaweza kuitumia kutekeleza kitendo. Kwa mfano, huduma ya hali ya hewa inaweza kutangaza zana ya "pata hali ya hewa", au seva ya biashara mtandao inaweza kutangaza zana ya "nunua bidhaa". Seva za MCP hutangaza jina la kila zana, maelezo, na muundo wa ingizo/saida katika orodha ya uwezo wao.

• **Rasilimali (Resources)**: Hizi ni vitu vya data au hati ambazo seva ya MCP inaweza kutoa kwa kusoma tu, na wateja wanaweza kuzipata wakati wanazohitaji. Mifano ni kama maudhui ya faili, rekodi za hifadhidata, au faili za kumbukumbu. Rasilimali zinaweza kuwa maandishi (kama nambari au JSON) au binary (kama picha au PDF).

• **Miondisho (Prompts)**: Hizi ni templeti zilizowekwa awali zinazotoa miondisho inayopendekezwa, kuruhusu mchakato mgumu zaidi wa kazi.

### Faida za MCP

MCP hutoa faida kubwa kwa Mawakala wa AI:

• **Ugunduzi wa Zana kwa Muda Halisi**: Mawakala wanaweza kupokea orodha ya zana zinazopatikana kutoka kwa seva pamoja na maelezo ya kile wanachofanya. Hii ni tofauti na API za jadi, ambazo mara nyingi zinahitaji usimbaji wa msimbo wa kudumu kwa ujumuishaji, ikimaanisha mabadiliko yoyote ya API yanahitaji sasisho la msimbo. MCP hutoa njia ya "jumuisha mara moja", ikileta ufanisi zaidi wa kubadilika.

• **Muingiliano Kati ya LLMs Mbalimbali**: MCP inafanya kazi kwa LLMs mbalimbali, ikitoa uhuru wa kubadili mifano kuu ili kutathmini kwa ufanisi bora.

• **Usalama wa Viwango**: MCP inajumuisha njia ya uthibitishaji ya kawaida, ikiboresha ujumuishaji unapoongeza upatikanaji kwa seva zingine za MCP. Hii ni rahisi kuliko kusimamia funguo tofauti na aina za uthibitishaji kwa API za jadi.

### Mfano wa MCP

![MCP Diagram](../../../translated_images/sw/mcp-diagram.e4ca1cbd551444a1.webp)

Fikiria mtumiaji anayetaka kuhifadhi tiketi ya ndege kwa kutumia msaidizi wa AI aliyezaliwa na MCP.

1. **Muunganisho**: Msaidizi wa AI (mteja wa MCP) anaunganisha na seva ya MCP inayotolewa na shirika la ndege.

2. **Ugunduzi wa Zana**: Mteja anauliza seva ya MCP ya shirika la ndege, "Je, una zana gani zinazopatikana?" Seva hutoa majibu na zana kama "tafuta ndege" na "hifadhi ndege".

3. **Kuitisha Zana**: Kisha unaomba msaidizi wa AI, "Tafadhali tafuta ndege kutoka Portland kwenda Honolulu." Msaidizi wa AI, kwa kutumia LLM yake, hutambua kuwa anahitaji kuita zana ya "tafuta ndege" na hupitisha vigezo vinavyohusika (asili, sehemu ya kwenda) kwa seva ya MCP.

4. **Utekelezaji na Majibu**: Seva ya MCP, ikifanya kama kiambatanisho, hufanya wito halisi kwa API ya uhifadhi ya ndani ya shirika la ndege. Kisha inapokea taarifa ya ndege (mfano data ya JSON) na kuirudisha kwa msaidizi wa AI.

5. **Mwingiliano Zaidi**: Msaidizi wa AI huonyesha chaguzi za ndege. Mara unapochagua ndege, msaidizi anaweza kuitisha zana ya "hifadhi ndege" kwenye seva ile ile ya MCP, kukamilisha uhifadhi.

## Itifaki ya Mwakala kwa Mwakala (A2A)

Wakati MCP inalenga kuunganisha LLMs na zana, **Itifaki ya Mwakala kwa Mwakala (A2A)** huchukua hatua zaidi kwa kuwezesha mawasiliano na ushirikiano kati ya mawakala tofauti wa AI. A2A huunganisha mawakala wa AI katika mashirika, mazingira na mifumo ya kiteknolojia tofauti kukamilisha kazi ya pamoja.

Tutachunguza sehemu na faida za A2A, pamoja na mfano wa jinsi inavyoweza kutumika katika maombi yetu ya usafiri.

### Sehemu za Msingi za A2A

A2A inalenga kuwezesha mawasiliano kati ya mawakala na kufanya kazi pamoja kukamilisha sehemu ndogo ya kazi ya mtumiaji. Kila sehemu ya itifaki inachangia hili:

#### Kadi ya Mwakala

Kama seva ya MCP inavyoshiriki orodha ya zana, Kadi ya Mwakala ina:
- Jina la Mwakala.
- **Maelezo ya kazi kuu** zinazokamilishwa na wakala huyo.
- **Orodha ya ujuzi maalum** na maelezo kusaidia mawakala wengine (au hata watumiaji wa binadamu) kuelewa lini na kwa nini wangetaka kumuita wakala huyo.
- **Anuani ya Endpoint ya sasa** ya wakala
- **Toleo** na **uwezo** wa wakala kama majibu ya mkondo na arifa za kusukuma.

#### Mtendaji wa Wakala

Mtendaji wa Wakala anahusika na **kupitisha muktadha wa mazungumzo ya mtumiaji kwa wakala wa mbali**, wakala wa mbali anahitaji hili kuelewa kazi inayo hitajika kukamilishwa. Katika seva ya A2A, wakala hutumia Mfano Wake wa Lugha Kubwa (LLM) kuchambua maombi yanayo ingia na kutekeleza kazi kwa kutumia zana zake za ndani.

#### Kazi (Artifact)

Baada ya wakala wa mbali kukamilisha kazi iliyotakiwa, matokeo yake huundwa kama kazi. Kazi **inahifadhi matokeo ya kazi ya wakala**, **maelezo ya kile kilichokamilishwa**, na **muktadha wa maandishi** unaotumwa kupitia itifaki. Baada ya kazi kutumwa, muunganisho na wakala wa mbali unafungwa hadi utakapohitajika tena.

#### Foleni ya Matukio

Sehemu hii inatumika kwa **kusimamia masasisho na kupitisha ujumbe**. Ni muhimu hasa katika uzalishaji wa mifumo ya agentic kuzuia muunganisho kati ya mawakala kufungwa kabla ya kazi kukamilika, hasa wakati muda wa kukamilisha kazi unaweza kuwa mrefu.

### Faida za A2A

• **Ushirikiano Ulioboreshwa**: Inawawezesha mawakala kutoka wauzaji na majukwaa tofauti kuingiliana, kushirikiana muktadha, na kufanya kazi pamoja, kukuza kiotomatiki kisichokatika kati ya mifumo iliyokuwa tofauti.

• **Uwezo wa Kuchagua Mfano**: Kila wakala wa A2A anaweza kuamua LLM gani ataitumia kuhudumia maombi yake, kuruhusu mifano iliyoboreshwa au iliyobinafsishwa kwa kila wakala, tofauti na muunganisho mmoja wa LLM katika baadhi ya matukio ya MCP.

• **Uthibitishaji Uliomo Moja kwa Moja**: Uthibitishaji umejumuishwa moja kwa moja kwenye itifaki ya A2A, ukitoa mfumo thabiti wa usalama kwa mwingiliano wa mawakala.

### Mfano wa A2A

![A2A Diagram](../../../translated_images/sw/A2A-Diagram.8666928d648acc26.webp)

Tuchambue zaidi hali yetu ya kuhifadhi tiketi za usafiri, lakini mara hii tukienda kutumia A2A.

1. **Ombi la Mtumiaji kwa Mawakala Wengi**: Mtumiaji anaingia na "Mwakala wa Usafiri" mteja/mwakala wa A2A, labda kwa kusema, "Tafadhali hifadhi safari yote kwenda Honolulu kwa wiki ijayo, ikijumuisha ndege, hoteli, na gari la kukodi".

2. **Utaratibu na Mwakala wa Usafiri**: Mwakala wa Usafiri anapokea ombi hili tata. Anatumia LLM yake kufikiria kuhusu kazi na kubaini anahitaji kuingiliana na mawakala wengine maalum.

3. **Mawasiliano Kati ya Mawakala**: Kisha Mwakala wa Usafiri hutumia itifaki ya A2A kuungana na mawakala wa chini, kama vile "Mwakala wa Shirika la Ndege," "Mwakala wa Hoteli," na "Mwakala wa Ukodi wa Gari" ambao wameundwa na makampuni tofauti.

4. **Utekelezaji wa Kazi uliogawanywa**: Mwakala wa Usafiri hutuma kazi maalum kwa mawakala hawa maalum (mfano, "Tafuta ndege kuelekea Honolulu," "Hifadhi hoteli," "Kodia gari"). Kila wakala maalum, akitumia LLM zake na zana zake (zinazo kuwa seva za MCP wenyewe), hufanya sehemu yake maalum ya uhifadhi.

5. **Majibu Yaliyokusanywa**: Mara mawakala wote wa chini wanapokamilisha kazi zao, Mwakala wa Usafiri hukusanya matokeo (maelezo ya ndege, uthibitisho wa hoteli, uhifadhi wa gari) na kutuma jibu kamili, la mtindo wa mazungumzo kwa mtumiaji.

## Mtandao wa Lugha Asili (NLWeb)

Tovuti imekuwa njia kuu kwa watumiaji kupata taarifa na data mtandaoni kwa muda mrefu.

Tuchunguze sehemu tofauti za NLWeb, faida za NLWeb na mfano wa jinsi NLWeb yetu inavyofanya kazi kwa kuangalia maombi yetu ya usafiri.

### Sehemu za NLWeb

- **Programu ya NLWeb (Msimbo wa Huduma ya Msingi)**: Mfumo unaoshughulikia maswali ya lugha asili. Unaunganisha sehemu tofauti za jukwaa kutengeneza majibu. Unaweza kuifikiria kama **mashine inayoiendesha vipengele vya lugha asili** vya tovuti.

- **Itifaki ya NLWeb**: Hii ni **seti ya msingi ya kanuni za mwingiliano wa lugha asili** na tovuti. Inarudisha majibu kwa muundo wa JSON (mara nyingi ikitumia Schema.org). Kusudi lake ni kuunda msingi rahisi kwa “Mtandao wa AI,” kwa njia ile ile HTML ilivyowezesha kushiriki hati mtandaoni.

- **Seva ya MCP (Kisituo cha Itifaki ya Muktadha wa Mfano)**: Kila usanidi wa NLWeb pia hufanya kazi kama **seva ya MCP**. Hii ina maana inaweza **kushiriki zana (kama njia ya "uliza") na data** na mifumo mingine ya AI. Kwa vitendo, hii hufanya maudhui na uwezo wa tovuti kuwa yanaweza kutumika na mawakala wa AI, ikifanya tovuti kuwa sehemu ya “ekosistema ya mawakala” pana.

- **Mifano ya Uingiza (Embedding Models)**: Mifano hii inatumika kugeuza maudhui ya tovuti kuwa uwakilishi wa nambari unaoitwa vectors (embedding). Vectors hizi huchukua maana kwa njia ambayo kompyuta zinaweza kulinganisha na kutafuta. Zinahifadhiwa katika hifadhidata maalum, na watumiaji wanaweza kuchagua mfano wa embedding wanayotaka kutumia.

- **Hifadhidata ya Vector (Mfumo wa Urejeshaji)**: Hifadhidata hii **inahifadhi embeddings za maudhui ya tovuti**. Mtu anapo uliza swali, NLWeb hutafuta hifadhidata ya vector kwa haraka kupata taarifa yenye umuhimu mkubwa zaidi. Inatoa orodha ya majibu yaliyowekwa kwa mpangilio wa ufanano. NLWeb hufanya kazi na mifumo tofauti ya kuhifadhi vector kama Qdrant, Snowflake, Milvus, Azure AI Search, na Elasticsearch.

### NLWeb kwa Mfano

![NLWeb](../../../translated_images/sw/nlweb-diagram.c1e2390b310e5fe4.webp)

Tufikirie tovuti yetu ya uhifadhi tiketi za usafiri tena, lakini mara hii, inaendesha kwa nguvu ya NLWeb.

1. **Kuingiza Data**: Katalogi za bidhaa za tovuti ya usafiri zilizopo (mfano, orodha za ndege, maelezo ya hoteli, vifurushi vya matembezi) huhaririwa kwa kutumia Schema.org au kupakiwa kupitia feed za RSS. Zana za NLWeb huingiza data hii iliyopangwa, hutoa embeddings, na kuzihifadhi katika hifadhidata ya vector ya ndani au ya mbali.

2. **Swali la Lugha Asili (Binadamu)**: Mtumiaji anatembelea tovuti na, badala ya kuvinjari katika menyu, anaandika kwenye kiolesura cha mazungumzo: "Nipe hoteli rafiki kwa familia huko Honolulu yenye bwawa la kuogelea kwa wiki ijayo".

3. **Usindikaji wa NLWeb**: Programu ya NLWeb inapokea swali hili. Inatuma swali kwa LLM kuelewa na kwa wakati mmoja inatafuta katika hifadhidata yake ya vector zilizohifadhiwa orodha za hoteli zinazofaa.

4. **Matokeo Sahihi**: LLM husaidia kufasiri matokeo ya utafutaji kutoka hifadhidata, kubaini mfanano bora kulingana na vigezo vya "rafiki wa familia," "bwawa," na "Honolulu," kisha kuunda jibu la lugha asili. Muhimu zaidi, jibu linahusu hoteli halisi kutoka katalogi ya tovuti, likiepuka taarifa za kufikirika.

5. **Mwingiliano wa Mwakala wa AI**: Kwa sababu NLWeb hutumika kama seva ya MCP, wakala wa AI wa usafiri wa nje anaweza pia kuungana na mfano wa NLWeb wa tovuti hii. Mwakala wa AI anaweza kutumia njia ya `ask` ya MCP kuuliza tovuti moja kwa moja: `ask("Kuna migahawa yoyote rafiki kwa wanyama wa mboga eneo la Honolulu inayopendekezwa na hoteli?")`. Mfano wa NLWeb ungeisindikiza hii, ukitumia hifadhidata yake ya taarifa za migahawa (ikiwa imepakuliwa), na kurudisha jibu la muundo wa JSON.

### Je, una Maswali Zaidi kuhusu MCP/A2A/NLWeb?

Jiunge na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kukutana na wanafunzi wengine, kuhudhuria saa za ofisi na kupata majibu ya maswali yako kuhusu Mawakala wa AI.

## Rasilimali

- [MCP kwa Waanzilishi](https://aka.ms/mcp-for-beginners)  
- [Nyaraka za MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Hifadhi ya NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Msingi wa Mawakala wa Microsoft](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Somo lililopita

[Mawakala wa AI katika Uzalishaji](../10-ai-agents-production/README.md)

## Somo lijalo

[Uhandisi wa Muktadha kwa Mawakala wa AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->