# Kutumia Itifaki za Mawakala (MCP, A2A na NLWeb)

[![Itifaki za Mawakala](../../../translated_images/sw/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Bonyeza picha hapo juu kutazama video ya somo hili)_

Wakati matumizi ya mawakala wa AI yanavyoongezeka, ndivyo ilivyo haja ya itifaki zinazohakikisha upangaji wa kawaida, usalama, na kusaidia ubunifu wazi. Katika somo hili, tutashughulikia itifaki 3 zinazolenga kukidhi hitaji hili - Itifaki ya Muktadha wa Mfano (MCP), Mwakala kwa Mwakala (A2A) na Wavuti ya Lugha Asilia (NLWeb).

## Utangulizi

Katika somo hili, tutafunika:

• Jinsi **MCP** inavyomruhusu Mwakala wa AI kufikia zana za nje na data ili kukamilisha kazi za mtumiaji.

• Jinsi **A2A** inavyowezesha mawasiliano na ushirikiano kati ya mawakala tofauti wa AI.

• Jinsi **NLWeb** inavyoleta miunganisho ya lugha asilia kwa tovuti yoyote, ikiwawezesha Mawakala wa AI kugundua na kuingiliana na yaliyomo.

## Malengo ya Kujifunza

• **Tambua** kusudi msingi na faida za MCP, A2A, na NLWeb katika muktadha wa mawakala wa AI.

• **Eleza** jinsi kila itifaki inavyorahisisha mawasiliano na mwingiliano kati ya LLMs, zana, na mawakala wengine.

• **Tambua** majukumu maalum ambayo kila itifaki inacheza katika kujenga mifumo tata ya mawakala.

## Itifaki ya Muktadha wa Mfano

Itifaki ya Muktadha wa Mfano (**MCP**) ni kiwango wazi kinachotoa njia iliyopangwa kwa programu kutoa muktadha na zana kwa LLMs. Hii inaruhusu "kiunganishi cha ulimwengu wote" kwa vyanzo tofauti vya data na zana ambazo Mawakala wa AI wanaweza kuunganishwa nazo kwa njia thabiti.

Tuchunguze vipengele vya MCP, faida ikilinganishwa na matumizi ya API moja kwa moja, na mfano wa jinsi mawakala wa AI wanavyoweza kutumia seva ya MCP.

### Vipengele Vikuu vya MCP

MCP inafanya kazi kwa usanifu wa **mteja-seva** na vipengele vikuu ni:

• **Hosts** ni programu za LLM (kwa mfano mhariri wa msimbo kama VSCode) ambazo huanza muunganisho na Seva ya MCP.

• **Clients** ni vipengele ndani ya programu mwenyeji vinavyodumisha muunganisho wa mmoja kwa mmoja na seva.

• **Servers** ni programu nyepesi zinazofunua uwezo maalum.

Imeingizwa katika itifaki ni mibobezi mitatu ya msingi ambayo ni uwezo wa Seva ya MCP:

• **Tools**: Hizi ni vitendo au kazi maalum ambazo Mwakala wa AI anaweza kuita ili kufanya kitendo. Kwa mfano, huduma ya hali ya hewa inaweza funua zana ya "pata hali ya hewa", au seva ya biashara ya mtandaoni inaweza funua zana ya "nunua bidhaa". Seva za MCP hutangaza jina la kila zana, maelezo, na skimu ya pembejeo/pembezaji katika orodha yao ya uwezo.

• **Resources**: Hizi ni vitu vya data au nyaraka zinazosomeka tu ambazo seva ya MCP inaweza kutoa, na wateja wanaweza kuzivuta wanapohitaji. Mifano ni pamoja na yaliyomo ya faili, rekodi za hifadhidata, au faili za kumbukumbu. Rasilimali zinaweza kuwa maandishi (kama msimbo au JSON) au bainari (kama picha au PDF).

• **Prompts**: Hizi ni templeti zilizotanguliwa ambazo zinatoa mapendekezo ya maelekezo, kuruhusu mtiririko wa kazi wenye ugumu zaidi.

### Faida za MCP

MCP inatoa faida kubwa kwa Mawakala wa AI:

• **Ugunduzi wa Zana unaobadilika**: Mawakala wanaweza kwa nguvu kupokea orodha ya zana zinazopatikana kutoka seva pamoja na maelezo ya kile wanachofanya. Hii ni tofauti na API za jadi, ambazo mara nyingi zinahitaji ufungaji wa msimbo kwa miunganiko, ikimaanisha kubadilika kwa API yoyote kunahitaji masasisho ya msimbo. MCP inatoa mbinu ya "unganisha mara moja", ikileta urekebishaji mkubwa.

• **Utangamano kati ya LLMs**: MCP inafanya kazi kati ya LLMs tofauti, ikitoa uharibifu wa kubadilisha modeli za msingi ili kutathmini utendaji bora.

• **Usalama Uliopangwa**: MCP inajumuisha njia ya kawaida ya uthibitishaji, ikibonyeza upanuzi wakati wa kuongeza ufikiaji kwa seva za MCP za ziada. Hii ni rahisi kuliko kusimamia funguo na aina tofauti za uthibitishaji kwa API za jadi mbalimbali.

### Mfano wa MCP

![Mchoro wa MCP](../../../translated_images/sw/mcp-diagram.e4ca1cbd551444a1.webp)

Fikiria mtumiaji anayetaka kuweka tiketi ya ndege kwa kutumia msaidizi wa AI unaotumia MCP.

1. **Connection**: Msaidizi wa AI (mteja wa MCP) anajenga muunganisho na seva ya MCP inayotolewa na shirika la ndege.

2. **Tool Discovery**: Mteja huuliza seva ya MCP ya shirika la ndege, "Mna zana gani zinazopatikana?" Seva inajibu kwa zana kama "tafuta ndege" na "weka tiketi".

3. **Tool Invocation**: Kisha unauliza msaidizi wa AI, "Tafadhali tafuta ndege kutoka Portland hadi Honolulu." Msaidizi wa AI, akitumia LLM yake, hutambua kwamba inahitaji kuita zana ya "tafuta ndege" na hupitisha vigezo vinavyofaa (asili, marudio) kwa seva ya MCP.

4. **Execution and Response**: Seva ya MCP, ikitenda kama kiambatisho, inafanya wito halisi kwa API ya ndani ya uhifadhi ya shirika la ndege. Kisha inapokea taarifa za ndege (mfano, data ya JSON) na kuzirudisha kwa msaidizi wa AI.

5. **Further Interaction**: Msaidizi wa AI huwasilisha chaguzi za ndege. Mara ukichagua ndege, msaidizi anaweza kuitisha zana ya "weka tiketi" kwenye seva moja hiyo ya MCP, kukamilisha uhifadhi.

## Itifaki ya Mwakala kwa Mwakala (A2A)

Wakati MCP inazingatia kuunganisha LLMs na zana, itifaki ya **Mwakala kwa Mwakala (A2A)** inaenda hatua zaidi kwa kuwezesha mawasiliano na ushirikiano kati ya mawakala tofauti wa AI. A2A inaunganisha mawakala wa AI kutoka taasisi, mazingira na mifumo tofauti ya kiteknolojia ili kukamilisha kazi iliyo gawanywa.

Tutachunguza vipengele na faida za A2A, pamoja na mfano wa jinsi ingeweza kutumika katika programu yetu ya usafiri.

### Vipengele Vikuu vya A2A

A2A inalenga kuwaruhusu mawakala kuwasiliana na kufanya kazi pamoja kukamilisha sehemu ya kazi ya mtumiaji. Kila kipengele cha itifaki huchangia hili:

#### Agent Card

Sawa na jinsi seva ya MCP inavyoshare orodha ya zana, Kadi ya Mwakala ina:
- Jina la Mwakala .  
- Maelezo ya **kazi za jumla** anayofanya.
- **orodha ya ujuzi maalum** na maelezo ili kusaidia mawakala wengine (au hata watumiaji wa kibinadamu) kuelewa wakati na kwanini wangependa kumuita wakala huyo.
- **URL ya Endpoint ya sasa** ya wakala
- **toleo** na **uwezo** wa wakala kama vile majibu ya kutiririka na arifa za push.

#### Agent Executor

Mtekelezaji wa Mwakala anawajibika kwa **kupitisha muktadha wa mazungumzo ya mtumiaji kwa wakala wa mbali**, wakala wa mbali anahitaji hili ili kuelewa kazi inayopaswa kukamilishwa. Katika seva ya A2A, wakala hutumia Mfano Wake Mkubwa wa Lugha (LLM) kutafsiri ombi zinazokuja na kutekeleza kazi kwa kutumia zana zake za ndani.

#### Artefakti

Mara wakala wa mbali anapokamilisha kazi iliyotakiwa, bidhaa yake ya kazi huundwa kama artefakti. Artefakti **ina matokeo ya kazi ya wakala**, **maelezo ya kile kilichokamilishwa**, na **muktadha wa maandishi** ambao unatumwa kupitia itifaki. Baada artefakti itakapotumwa, muunganisho na wakala wa mbali unafungwa hadi itakapohitajika tena.

#### Foleni ya Matukio

Kipengele hiki kinatumika kwa **kusimamia masasisho na kupitisha ujumbe**. Ni muhimu hasa katika uzalishaji kwa mifumo ya mawakala ili kuzuia muunganisho kati ya mawakala kufunguliwa kabla ya kazi kukamilika, hasa wakati muda wa kukamilisha kazi unaweza kuchukua muda mrefu.

### Faida za A2A

• **Ushirikiano Ulioimarishwa**: Inawawezesha mawakala kutoka kwa wauzaji na majukwaa tofauti kuingiliana, kushirikiana muktadha, na kufanya kazi pamoja, ikirahisisha automatisering bila mshono kati ya mifumo iliyokuwa imegawanywa.

• **Ubunifu wa Uchaguzi wa Mfano**: Kila wakala wa A2A anaweza kuamua ni LLM gani atakayoiweka kwa huduma za ombi lake, ikiruhusu modeli zilizoboreshwa au zilizofanyiwa faini kwa kila wakala, tofauti na muunganisho wa LLM moja katika baadhi ya matukio ya MCP.

• **Uthibitishaji Umejumuishwa**: Uthibitishaji umejengwa moja kwa moja ndani ya itifaki ya A2A, ukitoa mfumo thabiti wa usalama kwa mwingiliano wa mawakala.

### Mfano wa A2A

![Mchoro wa A2A](../../../translated_images/sw/A2A-Diagram.8666928d648acc26.webp)

Tuchambue zaidi katika hadithi yetu ya uhifadhi wa safari, lakini mara hii tukitumia A2A.

1. **User Request to Multi-Agent**: Mtumiaji anaingiliana na "Mwakala wa Safari" mteja/mwakala wa A2A, labda kwa kusema, "Tafadhali andaa safari nzima kwenda Honolulu kwa wiki ijayo, ikijumuisha ndege, hoteli, na gari la kukodisha".

2. **Orchestration by Travel Agent**: Mwakala wa Safari anapokea ombi hili tata. Anatumia LLM yake kutafakari juu ya kazi na kuamua kwamba anahitaji kuwasiliana na mawakala maalum wengine.

3. **Inter-Agent Communication**: Mwakala wa Safari kisha anatumia itifaki ya A2A kuungana na mawakala wa chini, kama "Mwakala wa Shirika la Ndege," "Mwakala wa Hoteli," na "Mwakala wa Kukodisha Gari" ambazo zimeundwa na kampuni tofauti.

4. **Delegated Task Execution**: Mwakala wa Safari anatuma kazi maalum kwa mawakala maalum hayo (mfano, "Tafuta ndege kwenda Honolulu," "Weka hoteli," "Kodia gari"). Kila mmoja wa mawakala maalum, wakiruninga LLM zao wenyewe na kutumia zana zao za ndani (ambazo zinaweza kuwa seva za MCP wenyewe), hufanya sehemu yake ya uhifadhi.

5. **Consolidated Response**: Mara mawakala wote wa chini wanapokamilisha kazi zao, Mwakala wa Safari anakusanya matokeo (maelezo ya ndege, uthibitisho wa hoteli, uhifadhi wa gari la kukodisha) na kutuma jibu kamili, la mtindo wa mazungumzo, kwa mtumiaji.

## Wavuti ya Lugha Asilia (NLWeb)

Tovuti zimekuwa kwa muda mrefu njia kuu kwa watumiaji kupata habari na data kupitia intaneti.

Tuchunguze vipengele tofauti vya NLWeb, faida za NLWeb na mfano jinsi NLWeb inavyofanya kazi kwa kuangalia programu yetu ya usafiri.

### Vipengele vya NLWeb

- **NLWeb Application (Core Service Code)**: Mfumo unaoshughulikia maswali ya lugha asilia. Unaunganisha sehemu tofauti za jukwaa ili kuunda majibu. Unaweza kuifikiria kama **mashine inayoiendesha vipengele vya lugha asilia** vya tovuti.

- **NLWeb Protocol**: Hii ni **seti ya msingi ya sheria za mwingiliano wa lugha asilia** na tovuti. Inarudisha majibu kwa muundo wa JSON (mara nyingi ikitumia Schema.org). Kusudi lake ni kuunda msingi rahisi kwa "Wavuti ya AI," kwa njia ile ile HTML ilivyofanya iwezekane kushiriki nyaraka mtandaoni.

- **MCP Server (Model Context Protocol Endpoint)**: Kila usanidi wa NLWeb pia hufanya kazi kama **seva ya MCP**. Hii inamaanisha inaweza **kushare zana (kama njia ya “ask”) na data** na mifumo mingine ya AI. Kwa vitendo, hili hufanya yaliyomo na uwezo wa tovuti kutumika na mawakala wa AI, kuruhusu tovuti kuwa sehemu ya "ekosistimu ya mawakala" pana.

- **Embedding Models**: Mifano hii hutumiwa **kugeuza yaliyomo ya tovuti kuwa uwakilishi nambari unaoitwa vekta (embeddings)**. Vekta hizi zinakamata maana kwa njia ambayo kompyuta zinaweza kulinganisha na kutafuta. Zinahifadhiwa katika hifadhidata maalum, na watumiaji wanaweza kuchagua ni mfano gani wa embedding wanayotaka kutumia.

- **Vector Database (Retrieval Mechanism)**: Hifadhidata hii **inahifadhi embeddings za yaliyomo ya tovuti**. Wakati mtu anauliza swali, NLWeb hutafuta katika hifadhidata ya vektor ili haraka kupata taarifa muhimu zaidi. Inatoa orodha ya majibu yanayowezekana, yaliyopangwa kwa kulingana na ufananisho. NLWeb inafanya kazi na mifumo tofauti ya uhifadhi wa vektor kama Qdrant, Snowflake, Milvus, Azure AI Search, na Elasticsearch.

### NLWeb kwa Mfano

![NLWeb](../../../translated_images/sw/nlweb-diagram.c1e2390b310e5fe4.webp)

Fikiria tena tovuti yetu ya uhifadhi wa safari, lakini mara hii, inafanywa na NLWeb.

1. **Data Ingestion**: Katalogi za bidhaa za tovuti ya usafiri zilizopo (mfano, orodha za ndege, maelezo ya hoteli, vifurushi vya ziara) zimepangwa kwa kutumia Schema.org au kupakiwa kupitia vyanzo vya RSS. Zana za NLWeb huzalisha data hii iliyopangwa, kuunda embeddings, na kuzihifadhi katika hifadhidata ya vektor ya ndani au ya mbali.

2. **Natural Language Query (Human)**: Mtumiaji anatembelea tovuti na, badala ya kuvinjari menyu, anaandika kwenye kiolesura cha gumzo: "Nitafutie hoteli rafiki kwa familia huko Honolulu yenye bwawa kwa wiki ijayo".

3. **NLWeb Processing**: Programu ya NLWeb inapokea swali hili. Inatuma swali kwa LLM kwa kuelewa na kwa wakati mmoja inatafuta katika hifadhidata yake ya vektor kwa orodha za hoteli zinazofaa.

4. **Accurate Results**: LLM husaidia kutafsiri matokeo ya utafutaji kutoka kwenye hifadhidata, kutambua mechi bora kulingana na vigezo vya "rafiki kwa familia," "bwawa," na "Honolulu", kisha kuunda jibu la lugha asilia. Muhimu, jibu linahusu hoteli halisi kutoka kwa katalogi ya tovuti, likiepuka habari za kubuniwa.

5. **AI Agent Interaction**: Kwa sababu NLWeb inatumikia kama seva ya MCP, wakala wa AI wa usafiri wa nje pia angeweza kuungana na mfano wa NLWeb wa tovuti hii. Wakala wa AI angeweza kisha kutumia njia ya MCP ya `ask` kuhoji tovuti moja kwa moja: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. Mfano wa NLWeb ungechakata hili, akitumia hifadhidata yake ya taarifa za mikahawa (ikiwa imepakiwa), na kurudisha jibu lililopangwa kwa muundo wa JSON.

### Je, Una Maswali Zaidi kuhusu MCP/A2A/NLWeb?

Jiunge na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) kukutana na wanafunzi wengine, kuhudhuria saa za ofisi na kupata majibu kwa maswali yako kuhusu Mawakala wa AI.

## Rasilimali

- [MCP kwa Waanzilishi](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repo ya NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Mfumo wa Mawakala wa Microsoft](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Kauli ya kutokuwa na dhamana:
Dokumenti hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiautomatiki zinaweza kuwa na makosa au upotofu. Nakala ya awali katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, inashauriwa kutumia tafsiri ya mtaalamu wa kibinadamu. Hatutawajibika kwa uelewa mbaya au tafsiri isiyo sahihi inayotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->