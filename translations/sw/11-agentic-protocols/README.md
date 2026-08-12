# Kutumia Itifaki za Wakala (MCP, A2A na NLWeb)

[![Itifaki za Wakala](../../../translated_images/sw/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Bofya picha hapo juu kutazama video ya somo hili)_

Kadri matumizi ya mawakala wa AI yanavyoongezeka, ndivyo pia inavyoongezeka haja ya itifaki zinazohakikisha ulinganifu, usalama, na kuunga mkono uvumbuzi wazi. Katika somo hili, tutashughulikia itifaki 3 zinazolenga kutimiza haja hii - Model Context Protocol (MCP), Agent to Agent (A2A) na Natural Language Web (NLWeb).

## Utangulizi

Katika somo hili, tutashughulikia:

• Jinsi **MCP** inavyowezesha Mawakala wa AI kufikia zana za nje na data ili kukamilisha kazi za mtumiaji.

• Jinsi **A2A** inavyowawezesha mawasiliano na ushirikiano kati ya mawakala tofauti wa AI.

• Jinsi **NLWeb** inaleta kiolesura cha lugha asilia kwa tovuti yoyote kuwezesha Mawakala wa AI kugundua na kuingiliana na yaliyomo.

## Malengo ya Kujifunza

• **Tambua** madhumuni makuu na faida za MCP, A2A, na NLWeb katika muktadha wa mawakala wa AI.

• **Eleza** jinsi itifaki kila moja inavyorahisisha mawasiliano na mwingiliano kati ya LLMs, zana, na mawakala wengine.

• **Tambua** majukumu tofauti yanayochezwa na kila itifaki katika ujenzi wa mifumo tata ya mawakala.

## Itifaki ya Muktadha wa Mfano

**Model Context Protocol (MCP)** ni kiwango wazi kinachotoa njia ya kuingiza muktadha na zana kwa LLMs kwa njia iliyopangwa. Hii inaruhusu "kiunganishi kamili" kwa vyanzo tofauti vya data na zana ambazo Mawakala wa AI wanaweza kuunganishwa nazo kwa njia thabiti.

Tuchunguze vipengele vya MCP, faida zake ikilinganishwa na matumizi ya API moja kwa moja, na mfano wa jinsi mawakala wa AI wanavyotumia server ya MCP.

### Vipengele Msingi vya MCP

MCP hufanya kazi kwa **miundo ya mteja-server** na vipengele vikuu ni:

• **Hosts** ni programu za LLM (kwa mfano mhariri wa msimbo kama VSCode) zinazozindua miunganisho na Server ya MCP.

• **Clients** ni vipengele ndani ya programu mwenyeji vinavyodumisha miunganisho ya moja kwa moja na server.

• **Servers** ni programu nyepesi zinazotoa uwezo maalum.

Katika itifaki kuna vitu vitatu vya msingi ambavyo ni uwezo wa Server ya MCP:

• **Zana**: Hizi ni vitendo au kazi zilizotengwa ambavyo wakala wa AI anaweza kuita kufanya kitendo. Kwa mfano, huduma ya hali ya hewa inaweza kutoa zana ya "pata hali ya hewa", au server ya e-commerce inaweza kutoa zana ya "nunua bidhaa". Servers za MCP hutangaza jina la kila zana, maelezo, na muundo wa pembejeo/pato katika orodha ya uwezo wao.

• **Rasilimali**: Hizi ni vitu vya data au hati zinazoweza kusomwa tu ambavyo server ya MCP inaweza kutoa, na wateja wanaweza kuzivuta wanapohitaji. Mfano ni maudhui ya faili, rekodi za database, au faili za kumbukumbu. Rasilimali zinaweza kuwa maandishi (kama msimbo au JSON) au binary (kama picha au PDFs).

• **Maelekezo**: Hizi ni templeti zilizosanifiwa ambazo hutoa maelekezo yaliyopendekezwa, kuruhusu mtiririko wa kazi tata zaidi.

### Faida za MCP

MCP inatoa faida kubwa kwa Mawakala wa AI:

• **Ugunduzi wa Zana Unaobadilika**: Mawakala wanaweza kupokea orodha ya zana zinazopatikana kutoka kwa server pamoja na maelezo ya kazi zao. Hii ni tofauti na API za kawaida zinazohitaji usimbaji wa msimbo wa kudumu wa mchakato wa kuunganishwa, ambayo mabadiliko yoyote ya API yanahitaji maboresho ya msimbo. MCP inatoa njia ya "unganisha mara moja", ikiyafanya mawakala kuwa na uwezo wa kuendana na mabadiliko.

• **Kushirikiana Kati ya LLMs**: MCP hufanya kazi kati ya LLMs tofauti, ikitoa uwezo wa kubadili modeli kuu kwa ajili ya tathmini ya utendaji bora.

• **Usalama wa Kiwango**: MCP ina njia iliyosimamiwa ya uthibitishaji, kuboresha uwezo wa kuongeza upatikanaji kwa servers zaidi za MCP. Hii ni rahisi zaidi kuliko kusimamia funguo na aina tofauti za uthibitishaji kwa API za kawaida.

### Mfano wa MCP

![MCP Diagram](../../../translated_images/sw/mcp-diagram.e4ca1cbd551444a1.webp)

Fikiria mtumiaji anayetaka kuweka tiketi ya ndege kwa msaada wa msaidizi wa AI unaotumia MCP.

1. **Muunganisho**: Msaidizi wa AI (mteja wa MCP) anaunganisha na server ya MCP inayotolewa na shirika la ndege.

2. **Ugunduzi wa Zana**: Mteja anauliza server ya MCP ya shirika la ndege, "Ni zana gani mnalizo?" Server inajibu na zana kama "tafuta ndege" na "weke ndege".

3. **Kuitisha Zana**: Kisha unauliza msaidizi wa AI, "Tafadhali tafuta ndege kutoka Portland kwenda Honolulu." Msaidizi wa AI, akitumia LLM yake, anabaini ana haja ya kuita zana ya "tafuta ndege" na anapitia vigezo husika (asili, marudio) kwa server ya MCP.

4. **Utekelezaji na Majibu**: Server ya MCP, ikifanya kama kiambatisho, inafanya wito halisi kwa API ya ndani ya shirika la ndege. Kisha inapokea taarifa za ndege (mfano, data ya JSON) na kuzirudisha kwa msaidizi wa AI.

5. **Mwingiliano Zaidi**: Msaidizi wa AI huonyesha chaguzi za ndege. Mara unachagua ndege, msaidizi anaweza kuita zana ya "weke ndege" kwenye server ile ile ya MCP, kukamilisha uhifadhi.

## Itifaki ya Wakala kwa Wakala (A2A)

Wakati MCP inazingatia kuunganisha LLMs na zana, **Itifaki ya Wakala kwa Wakala (A2A)** inachukua hatua zaidi kwa kuwezesha mawasiliano na ushirikiano kati ya mawakala tofauti wa AI.  A2A inaunganisha mawakala wa AI kutoka mashirika, mazingira na mifumo tofauti ili kukamilisha kazi ya pamoja.

Tutachambua vipengele na faida za A2A, pamoja na mfano wa jinsi inaweza kutumika katika programu yetu ya usafiri.

### Vipengele Msingi vya A2A

A2A inazingatia kuwezesha mawasiliano kati ya mawakala na kuwafanya wafanye kazi pamoja ili kukamilisha sehemu ndogo ya kazi ya mtumiaji. Kila kipengele cha itifaki kina mchango huu:

#### Kadi ya Wakala

Kama server ya MCP inavyoshiriki orodha ya zana, Kadi ya Wakala ina:
- Jina la Wakala.
- **maelezo ya kazi za jumla** anazokamilisha.
- **orodha ya ujuzi maalum** yenye maelezo kusaidia mawakala wengine (au hata watumiaji wa binadamu) kuelewa lini na kwa nini wangependa kumuita wakala huyo.
- **URL ya Endpoint ya sasa** ya wakala.
- **toleo** na **uwezo** wa wakala kama vile majibu ya mtiririko na taarifa za push.

#### Mtendaji wa Wakala

Mtendaji wa Wakala ana jukumu la **kupeleka muktadha wa mazungumzo ya mtumiaji kwa wakala wa mbali**, wakala wa mbali anahitaji hii kuelewa kazi inayohitaji kutekelezwa. Katika server ya A2A, wakala hutumia Modeli yake ya Lugha Kubwa (LLM) kusoma maombi yanayokuja na kutekeleza kazi kwa kutumia zana zake za ndani.

#### Kielelezo

Mara wakala wa mbali anakamilisha kazi iliyotakiwa, matokeo yake hutengenezwa kama kielelezo. Kielelezo **kinabeba matokeo ya kazi ya wakala**, **maelezo ya yaliyokamilishwa**, na **muktadha wa maandishi** unaotumwa kupitia itifaki. Baada ya kielelezo kutumwa, muunganisho na wakala wa mbali unafungwa hadi itakapohitajika tena.

#### Foleni ya Matukio

Kipengele hiki hutumika kwa **kusimamia masasisho na kupitisha ujumbe**. Ni muhimu hasa katika uzalishaji wa mifumo ya mawakala kuzuia kufungwa kwa muunganisho kati ya mawakala kabla ya kazi kukamilika, hasa wakati muda wa kukamilisha kazi unaweza kuchukua muda mrefu.

### Faida za A2A

• **Ushirikiano Ulioimarishwa**: Huwawezesha mawakala kutoka wauzaji na majukwaa tofauti kuingiliana, kushirikiana muktadha, na kufanya kazi pamoja, kurahisisha otomatiki bila usumbufu kati ya mifumo ambayo kawaida haijawaunganisha.

• **Uwezo wa Uchaguzi wa Modeli**: Kila wakala wa A2A anaweza kuamua LLM gani ataitumia kutekeleza maombi yake, kuruhusu modeli zilizoboreshwa au hiziwekwa upya kwa kila wakala, tofauti na muunganisho mmoja wa LLM katika baadhi ya hali za MCP.

• **Uthibitishaji Umejengwa Ndani**: Uthibitishaji umejumuishwa moja kwa moja ndani ya itifaki ya A2A, ikitoa mfumo thabiti wa usalama kwa mwingiliano wa mawakala.

### Mfano wa A2A

![A2A Diagram](../../../translated_images/sw/A2A-Diagram.8666928d648acc26.webp)

Twendelee na mfano wetu wa kuweka tiketi za usafiri, lakini sasa tukitumia A2A.

1. **Ombi la Mtumiaji kwa Mawakala Wengi**: Mtumiaji anawasiliana na "Mwakala wa Safari" kama mteja/wakala wa A2A, labda kwa kusema, "Tafadhali weka safari nzima kwenda Honolulu wiki ijayo, ikijumuisha ndege, hoteli, na gari la kukodisha".

2. **Usimamizi na Mwakala wa Safari**: Mwakala wa Safari anapokea ombi hili tata. Anatumia LLM yake kufikiria kuhusu kazi na kubaini kwamba anahitaji kuingiliana na mawakala wengine maalum.

3. **Mawasiliano kati ya Mawakala**: Mwakala wa Safari hutumia itifaki ya A2A kuunganishwa na mawakala wa chini, kama vile "Mwakala wa Shirika la Ndege," "Mwakala wa Hoteli," na "Mwakala wa Kukodisha Gari" wanaoundwa na makampuni tofauti.

4. **Utekelezaji Wa Kazi Ulio_GAIN_wa**: Mwakala wa Safari hutuma kazi maalum kwa mawakala hawa maalum (mfano, "Tafuta ndege za kwenda Honolulu," "Weka hoteli," "Kodi gari"). Kila wakala huyu maalum, akitumia LLM zake na zana zake (ambazo zinaweza kuwa servers za MCP wenyewe), hufanya sehemu yake ya uhifadhi.

5. **Majibu Yaliyoshirikishwa**: Mara mawakala wote wa chini wanapokamilisha kazi zao, Mwakala wa Safari hukusanya matokeo (maelezo ya ndege, uthibitisho wa hoteli, uhifadhi wa gari) na kutuma jibu kamili, kwa mtindo wa mazungumzo, kwa mtumiaji.

## Wavuti ya Lugha Asilia (NLWeb)

Tovuti zimekuwa kwa muda mrefu njia kuu kwa watumiaji kupata taarifa na data mtandaoni.

Tuchunguze vipengele tofauti vya NLWeb, faida za NLWeb na mfano wa jinsi NLWeb yetu inavyofanya kazi kwa kuangalia programu yetu ya usafiri.

### Vipengele vya NLWeb

- **Programu ya NLWeb (Kanuni Kuu ya Huduma)**: Mfumo unaoshughulikia maswali ya lugha asilia. Unaunganisha sehemu tofauti za jukwaa kutengeneza majibu. Unaweza kuiangalia kama **mashine inayoiendesha sifa za lugha asilia za tovuti**.

- **Itifaki ya NLWeb**: Huu ni **seti ya kanuni za msingi kwa mwingiliano wa lugha asilia** na tovuti. Hutuma majibu kama muundo wa JSON (mara nyingi ikitumia Schema.org). Madhumuni yake ni kuunda msingi rahisi kwa "Wavuti ya AI," kwa njia ile ile HTML iliyoifanya iwezekane kushiriki hati mtandaoni.

- **Server ya MCP (Mwenendo wa Itifaki ya Muktadha wa Mfano)**: Kila usanidi wa NLWeb pia hufanya kazi kama **server ya MCP**. Hii inamaanisha inaweza **kushiriki zana (kama njia ya "kuwauliza") na data** na mifumo mingine ya AI. Katika matumizi halisi, hii hufanya maudhui na uwezo wa tovuti yatumiwe na mawakala wa AI, kuruhusu tovuti kuwa sehemu ya "mazingira ya mawakala."

- **Mifano ya Uingiliaji**: Mifano hii hutumika **kugeuza maudhui ya tovuti kuwa uwakilishi wa nambari unaoitwa vekta** (embedding). Vekta hizi zinashikilia maana kwa njia kompyuta zinaweza kulinganisha na kutafuta. Zinahifadhiwa katika hifadhidata maalum, na watumiaji wanaweza kuchagua mfano wa uingiliaji wanayotaka kutumia.

- **Hifadhidata ya Vekta (Mekaniki ya Kuwapata)**: Hifadhidata hii **inahifadhi uingiliaji wa maudhui ya tovuti**. Mtumiaji anapouliza swali, NLWeb huchunguza hifadhidata ya vekta kupata haraka taarifa muhimu zaidi. Inatoa orodha ya haraka ya majibu yanayowezekana, ikipangwa kwa kulinganishwa. NLWeb hufanya kazi na mifumo tofauti ya uhifadhi vekta kama Qdrant, Snowflake, Milvus, Azure AI Search, na Elasticsearch.

### NLWeb kwa Mfano

![NLWeb](../../../translated_images/sw/nlweb-diagram.c1e2390b310e5fe4.webp)

Tufikirie tena tovuti yetu ya kuweka tiketi za usafiri, lakini sasa inayotumia NLWeb.

1. **Kukusanya Data**: Katalogi za bidhaa zilizopo za tovuti ya usafiri (mfano, orodha za ndege, maelezo ya hoteli, pakiti za ziara) zimeandaliwa kwa kutumia Schema.org au kupakiwa kupitia vifuatiliaji vya RSS. Zana za NLWeb huchakata data hii iliyopangwa, kuunda uingiliaji, na kuhifadhi katika hifadhidata ya vekta ya ndani au ya mbali.

2. **Swali la Lugha Asilia (Binadamu)**: Mtumiaji anaenda kwenye tovuti na, badala ya kuvinjari menyu, anaandika kwenye kiolesura cha mazungumzo: "Nipe hoteli rafiki kwa familia huko Honolulu yenye bwawa la kuogelea kwa wiki ijayo".

3. **Usindikaji wa NLWeb**: Programu ya NLWeb inapokea swali hili. Inatuma swali kwa LLM kwa kuelewa na kwa wakati mmoja inatafuta hifadhidata yake ya vekta kupata orodha za hoteli zinazohusiana.

4. **Matokeo Sahihi**: LLM husaidia kutafsiri matokeo ya utafutaji kutoka kwa hifadhidata, kubaini mechi bora kulingana na vigezo "rafiki kwa familia," "bwawa," na "Honolulu," kisha kuunda jibu la lugha asilia. Muhimu, jibu linaelekeza kwa hoteli halisi kutoka katalogi ya tovuti, likiepuka taarifa za kubuniwa.

5. **Mwingiliano wa Wakala wa AI**: Kwa sababu NLWeb hutumika kama server ya MCP, wakala wa usafiri wa AI wa nje pia anaweza kuunganishwa na toleo la NLWeb la tovuti hii. Wakala wa AI anaweza kutumia njia ya `ask` ya MCP kuuliza tovuti moja kwa moja: `ask("Kuna migahawa yoyote rafiki kwa wanasheria wa veji katika eneo la Honolulu inayopendekezwa na hoteli?")`. Toleo la NLWeb litasindika hili, likitumia hifadhidata ya taarifa za migahawa (ikiwa imeloadiwa), na kurudisha jibu lililopangwa la JSON.

### Je, Una Maswali Zaidi kuhusu MCP/A2A/NLWeb?

Jiunge na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kukutana na wanafunzi wengine, kuhudhuria saa za ofisi na kupata majibu ya maswali yako kuhusu Mawakala wa AI.

## Rasilimali

- [MCP kwa Wachanga](https://aka.ms/mcp-for-beginners)  
- [Nyaraka za MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Hifadhidata ya NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Mfumo wa Mawakala wa Microsoft](https://aka.ms/ai-agents-beginners/agent-framework)

## Somo Lililopita

[Mawakala wa AI katika Uzalishaji](../10-ai-agents-production/README.md)

## Somo Lijalo

[Uhandisi wa Muktadha kwa Mawakala wa AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->