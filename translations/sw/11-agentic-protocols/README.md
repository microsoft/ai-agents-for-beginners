# Kutumia Itifaki za Kijumla (MCP, A2A na NLWeb)

[![Agentic Protocols](../../../translated_images/sw/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Bonyeza picha hapo juu kutazama video ya somo hili)_

Kadiri matumizi ya mawakala wa AI yanavyoongezeka, ndivyo pia inavyoongezeka haja ya itifaki zinazohakikisha viwango, usalama, na kusaidia uvumbuzi wa wazi. Katika somo hili, tutajadili itifaki 3 zinazolenga kukidhi hitaji hili - Itifaki ya Muktadha wa Mfano (MCP), Mwakala kwa Mwakala (A2A) na Mtandao wa Lugha Asilia (NLWeb).

## Utangulizi

Katika somo hili, tutafunika:

• Jinsi **MCP** inavyomruhusu Mwakala wa AI kupata vifaa na data za nje ili kukamilisha kazi za mtumiaji.

•  Jinsi **A2A** inavyowezesha mawasiliano na ushirikiano kati ya mawakala tofauti wa AI.

• Jinsi **NLWeb** inavyoweka interfaces za lugha asilia kwenye tovuti yoyote, kuwezesha mawakala wa AI kugundua na kuingiliana na maudhui.

## Malengo ya Kujifunza

• **Tambua** lengo kuu na faida za MCP, A2A, na NLWeb katika muktadha wa mawakala wa AI.

• **Elezea** jinsi kila itifaki inavyorahisisha mawasiliano na mwingiliano kati ya LLMs, vifaa, na mawakala wengine.

• **Tambua** majukumu tofauti ambayo kila itifaki inacheza katika kujenga mifumo tata ya kujumuisha mawakala.

## Itifaki ya Muktadha wa Mfano

**Itifaki ya Muktadha wa Mfano (MCP)** ni kiwango wazi kinachotoa njia sanifu kwa programu kutoa muktadha na zana kwa LLMs. Hii inaruhusu "adapter wa ulimwengu" kwa vyanzo mbalimbali vya data na zana ambazo mawakala wa AI wanaweza kuunganishwa nazo kwa njia thabiti.

Tuchaangalie sehemu za MCP, faida zinazopatikana ikilinganishwa na kutumia API moja kwa moja, na mfano wa jinsi mawakala wa AI wanavyoweza kutumia seva ya MCP.

### Sehemu za Msingi za MCP

MCP hufanya kazi kwa **miundo ya mteja-seva** na sehemu zake kuu ni:

• **Hosts** ni programu za LLM (kwa mfano mhariri wa nambari kama VSCode) ambazo huanzisha muunganisho na seva ya MCP.

• **Clients** ni sehemu ndani ya programu ya host zinazodumisha muunganisho wa moja kwa moja na seva.

• **Servers** ni programu nyepesi zinazotoa uwezo maalum.

Katika itifaki kuna misingi mitatu kuu inayojumuishwa ambazo ni uwezo wa seva ya MCP:

• **Tools**: Hizi ni hatua au kazi tofauti ambazo wakala wa AI anaweza kuitisha kufanya tendo fulani. Kwa mfano, huduma ya hali ya hewa inaweza kutoa zana ya "pata hali ya hewa", au seva ya e-commerce inaweza kutoa zana ya "nunua bidhaa". Seva za MCP huorodhesha kila jina la zana, maelezo, na muundo wa pembejeo/matokeo katika orodha ya uwezo.

• **Resources**: Hizi ni data au nyaraka za kusoma tu ambazo seva ya MCP inaweza kutoa, na wateja wanaweza kuzipata inapohitajika. Mifano ni kama maudhui ya faili, rekodi za hifadhidata, au faili za kumbukumbu. Rasilimali zinaweza kuwa maandishi (kama nambari au JSON) au binary (kama picha au PDF).

• **Prompts**: Hizi ni templaiti zilizotayarishwa awali zinazotoa mapendekezo ya vichochezi, zikiruhusu workflows tata zaidi.

### Faida za MCP

MCP hutoa faida kubwa kwa mawakala wa AI:

• **Ugunduzi wa Zana kwa Muda Halisi**: Mawakala wanaweza kupata orodha ya zana zilizopo kutoka kwa seva pamoja na maelezo ya kazi zao. Hii tofauti na API za jadi, ambazo mara nyingi zinahitaji usanidi wa kitaalamu kwa kila muunganisho, hivyo mabadiliko yoyote ya API yanahitaji marekebisho ya msimbo. MCP hutoa njia ya "unganisha mara moja", ikileta ufanisi zaidi.

• **Uwezo wa Kufanya Kazi Kati ya LLMs Mbalimbali**: MCP hufanya kazi kati ya LLMs tofauti, ikitoa uhuru wa kubadilisha modeli kuu kwa ajili ya tathmini ya utendaji bora.

• **Usalama Sanifu**: MCP inajumuisha njia sanifu ya uthibitishaji, ambayo inarahisisha ongezeko la upatikanaji kwa seva zaidi za MCP. Hii ni rahisi zaidi kuliko kusimamia funguo na aina tofauti za uthibitishaji kwa API za jadi.

### Mfano wa MCP

![MCP Diagram](../../../translated_images/sw/mcp-diagram.e4ca1cbd551444a1.webp)

Fikiria mtumiaji anayetaka kuweka tiketi ya ndege kwa kutumia msaidizi wa AI unaotumia MCP.

1. **Muunganisho**: Msaidizi wa AI (mteja wa MCP) anajiunga na seva ya MCP inayotolewa na shirika la ndege.

2. **Uchunguzi wa Zana**: Mteja anauliza seva ya MCP ya shirika la ndege, "Una zana gani zinazopatikana?" Seva hujibu na zana kama "tafuta ndege" na "weka tiketi ya ndege".

3. **Uitishaji wa Zana**: Kisha unauliza msaidizi wa AI, "Tafadhali tafuta ndege kutoka Portland hadi Honolulu." Msaidizi wa AI, akitumia LLM yake, hutambua kwamba anahitaji kuitisha zana ya "tafuta ndege" na hupitisha vigezo muhimu (asalio, mahali pa kupelekwa) kwa seva ya MCP.

4. **Utekelezaji na Majibu**: Seva ya MCP, ikifanya kazi kama kiambatisho, hufanya wito halisi kwa API ya kuhifadhi tiketi ya shirika la ndege. Kisha hupokea taarifa za ndege (kwa mfano data ya JSON) na kuirudisha kwa msaidizi wa AI.

5. **Mwingiliano Zaidi**: Msaidizi wa AI huonyesha chaguzi za ndege. Mara tu unapochagua ndege, msaidizi anaweza kuitisha zana ya "weka tiketi" kwenye seva hiyo ya MCP, kukamilisha uhifadhi.

## Itifaki ya Mwakala kwa Mwakala (A2A)

Wakati MCP inalenga kuunganisha LLMs na zana, **itfaki ya Mwakala kwa Mwakala (A2A)** inachukua hatua zaidi kwa kuwezesha mawasiliano na ushirikiano kati ya mawakala tofauti wa AI. A2A huunganisha mawakala wa AI kati ya mashirika tofauti, mazingira na teknolojia ili kukamilisha kazi ya pamoja.

Tutaangalia sehemu na faida za A2A, pamoja na mfano wa jinsi inaweza kutumika katika programu yetu ya usafiri.

### Sehemu za Msingi za A2A

A2A inalenga kuwezesha mawasiliano kati ya mawakala na kuwafanya wafanye kazi pamoja kukamilisha kazi ndogo ya mtumiaji. Kila sehemu ya itifaki huchangia hili:

#### Kadi ya Mwakala

Kama vile seva ya MCP inavyoshiriki orodha ya zana, Kadi ya Mwakala ina:
- Jina la Mwakala.
- **Maelezo ya kazi kuu** anazokamilisha.
- **Orodha ya ujuzi maalum** pamoja na maelezo kusaidia mawakala wengine (au hata watumiaji wa binadamu) kuelewa lini na kwa nini wangependa kumwita yule wakala.
- **URL ya Endpoint ya sasa** ya wakala
- **Toleo** na **uwezo** wa wakala kama majibu ya mtiririko na taarifa za kusukuma.

#### Mtendaji wa Mwakala

Mtendaji wa Mwakala anahusika na **kupitisha muktadha wa mazungumzo ya mtumiaji kwa wakala wa mbali**, wakala wa mbali anahitaji hili kuelewa kazi inayohitajika kufanyika. Katika seva ya A2A, wakala hutumia LLM yake mwenyewe kuchambua maombi yanayoingia na kutekeleza kazi kwa kutumia zana zake za ndani.

#### Kawaida

Mara wakala wa mbali anapokamilisha kazi iliyotakiwa, bidhaa ya kazi yake hutengenezwa kama kawaida. Kawaida **ina matokeo ya kazi ya wakala**, **maelezo ya kilichokamilishwa**, na **muktadha wa maandishi** unaotumwa kupitia itifaki. Baada ya kawaida kutumwa, muunganisho na wakala wa mbali unafungwa hadi utakapohitajika tena.

#### Foleni ya Matukio

Sehemu hii hutumika kwa **kusimamia masasisho na kupitisha ujumbe**. Ni muhimu hasa katika uzalishaji kwa mifumo ya waakilishi kuzuia muunganisho kati ya mawakala kufungwa kabla ya kazi kukamilika, hasa wakati muda wa kukamilisha kazi unaweza kuchukua muda mrefu.

### Faida za A2A

• **Ushirikiano Bora**: Inawawezesha mawakala kutoka wauzaji na majukwaa tofauti kuingiliana, kushiriki muktadha, na kufanya kazi pamoja, kurahisisha uendeshaji otomatiki baina ya mifumo ambayo hapo awali haikuwa na muunganisho.

• **Uwezo wa Kuchagua Modeli**: Kila wakala wa A2A anaweza kuamua LLM gani itumike huduma zake, kuruhusu matumizi bora au marekebisho maalum kwa wakala mmoja mmoja, tofauti na muunganisho mmoja wa LLM katika baadhi ya matukio ya MCP.

• **Uthibitishaji Uliounganishwa**: Uthibitishaji umejumuishwa moja kwa moja katika itifaki ya A2A, ikitoa mfumo dhabiti wa usalama kwa mwingiliano wa mawakala.

### Mfano wa A2A

![A2A Diagram](../../../translated_images/sw/A2A-Diagram.8666928d648acc26.webp)

Tuendelee na hali yetu ya kuhifadhi usafiri, lakini wakati huu tukitumia A2A.

1. **Ombi la Mtumiaji kwa Mawakala Wengi**: Mtumiaji anawasiliana na mteja/mwakala wa A2A anayeitwa "Mwakala wa Usafiri," labda kwa kusema, "Tafadhali weka safari kamili kwenda Honolulu kwa wiki ijayo, ikijumuisha ndege, hoteli, na gari la kukodisha".

2. **Uendeshaji na Mwakala wa Usafiri**: Mwakala wa Usafiri anapokea ombi hili tata. Anatumia LLM yake kufikiria kuhusu kazi na kubaini kwamba anahitaji kuwasiliana na mawakala maalum wa aina tofauti.

3. **Mawasiliano kati ya Wakala**: Kisha Mwakala wa Usafiri anatumia itifaki ya A2A kuungana na mawakala wa sehemu za chini, kama "Mwakala wa Shirika la Ndege," "Mwakala wa Hoteli," na "Mwakala wa Gari la Kukodisha" waliotengenezwa na kampuni tofauti.

4. **Utekelezaji wa Kazi zilizoko Wapili**: Mwakala wa Usafiri hutuma kazi maalum kwa mawakala hawa maalum (mfano, "Tafuta ndege za kuelekea Honolulu," "Weka hoteli," "Kodi gari"). Kila mmoja wa mawakala hawa maalum, akikimbiza LLM zake binafsi na kutumia zana zao wenyewe (zinaweza kuwa seva za MCP pia), hutekeleza sehemu yake maalum ya uhifadhi.

5. **Jibu la Kufungwa Pamoja**: Mara mawakala wote wa sehemu za chini wanapokamilisha kazi zao, Mwakala wa Usafiri huunganisha matokeo (maelezo ya ndege, uthibitisho wa hoteli, uhifadhi wa gari) na kutuma jibu kamili, la mtindo wa mazungumzo, kwa mtumiaji.

## Mtandao wa Lugha Asilia (NLWeb)

Tovuti zimekuwa njia kuu kwa watumiaji kupata taarifa na data mtandaoni kwa muda mrefu.

Tuchunguze sehemu tofauti za NLWeb, faida za NLWeb na mfano wa jinsi NLWeb inavyofanya kazi kwa kuangalia programu yetu ya usafiri.

### Sehemu za NLWeb

- **Programu ya NLWeb (Msimbo wa Huduma Msingi)**: Mfumo unaosindika maswali ya lugha asilia. Unaunganisha sehemu mbalimbali za jukwaa kuunda majibu. Unaweza kuifikiria kama **motisha inayoiendesha sehemu za lugha asilia** za tovuti.

- **Itifaki ya NLWeb**: Hii ni **seti ya msingi ya sheria za mwingiliano wa lugha asilia** na tovuti. Inarudisha majibu kwa muundo wa JSON (wanaotumia Schema.org). Kusudi lake ni kuunda msingi rahisi wa “Mtandao wa AI,” kwa njia ile ile HTML ilivyofanikisha kushiriki nyaraka mtandaoni.

- **Seva ya MCP (Mwisho wa Itifaki ya Muktadha wa Mfano)**: Kila usanidi wa NLWeb pia hufanya kazi kama **seva ya MCP**. Hii inamaanisha inaweza **kushiriki zana (kama njia ya 'ask') na data** na mifumo mingine ya AI. Kwa vitendo, hii inafanya maudhui na uwezo wa tovuti kutumika na mawakala wa AI, kuwezesha tovuti kuwa sehemu ya “ekosistimu ya mawakala” pana.

- **Modeli za Kuunganisha (Embedding Models)**: Modeli hizi hutumika **kubadilisha maudhui ya tovuti kuwa maelezo ya nambari yanayoitwa vectors (embeddings)**. Vectors hizi zinakamata maana kwa njia kompyuta zinaweza kuzilinganisha na kuitafuta. Zinahifadhiwa katika hifadhidata maalum, na watumiaji wanaweza kuchagua modeli ya embedding wanayotaka kutumia.

- **Hifadhidata ya Vectors (Mbinu ya Urejeshaji)**: Hifadhidata hii **inahifadhi embeddings za maudhui ya tovuti**. Wakati mtu anauliza swali, NLWeb huangalia hifadhidata ya vector ili haraka kupata taarifa muhimu zaidi. Hutoa orodha ya haraka ya majibu yanayowezekana, yakiwa yamepangwa kulingana na ufanano. NLWeb hufanya kazi na mifumo tofauti ya kuhifadhi vectors kama Qdrant, Snowflake, Milvus, Azure AI Search, na Elasticsearch.

### NLWeb kwa Mfano

![NLWeb](../../../translated_images/sw/nlweb-diagram.c1e2390b310e5fe4.webp)

Tazama tena tovuti yetu ya uhifadhi wa usafiri, lakini wakati huu, inaendeshwa na NLWeb.

1. **Kukusanya Data**: Katalogi za bidhaa zilizopo kwenye tovuti ya usafiri (mfano, orodha za ndege, maelezo ya hoteli, vifurushi vya ziara) zimepangwa kwa kutumia Schema.org au kupakiwa kupitia malisho ya RSS. Zana za NLWeb hulisha data hii iliyopangwa, hutengeneza embeddings, na kuzihifadhi katika hifadhidata ya vector ya ndani au ya mbali.

2. **Swali la Lugha Asilia (Binadamu)**: Mtumiaji anatembelea tovuti na, badala ya kuvinjari menyu, anaandika kwenye mazungumzo: "Nipatie hoteli rafiki kwa familia huko Honolulu yenye bwawa la kuogelea kwa wiki ijayo."

3. **Usindikaji wa NLWeb**: Programu ya NLWeb inapokea swali hili. Inalipeleka swali kwa LLM kwa kuelewa na wakati huo huo inatafuta hifadhidata yake ya vector kwa orodha za hoteli zinazohusika.

4. **Matokeo Sahihi**: LLM husaidia kufasiri matokeo ya utafutaji kutoka hifadhidata, kubaini mechi bora kulingana na vigezo vya "rafiki kwa familia," "bwawa," na "Honolulu," kisha kuunda jibu la lugha asilia. Muhimu, jibu linaelekeza kwa hoteli halisi kutoka katalogi ya tovuti, likiepuka taarifa za kubuniwa.

5. **Mwingiliano wa Mwakala wa AI**: Kwa kuwa NLWeb hutumika kama seva ya MCP, wakala wa usafiri wa AI wa nje pia anaweza kuungana kwa mfano wa NLWeb wa tovuti hii. Wakala wa AI basi anaweza kutumia njia ya `ask` ya MCP kuuliza tovuti moja kwa moja: `ask("Je, kuna migahawa rafiki kwa wafuataji wa lishe ya mmea katika eneo la Honolulu inayopendekezwa na hoteli?")`. Mfano wa NLWeb utaendesha hili, ukitumia hifadhidata yake ya taarifa za migahawa (ikiwa imepakuliwa), na kurudisha jibu la JSON lililopangwa.

### Una Maswali Zaidi Kuhusu MCP/A2A/NLWeb?

Jiunge na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kukutana na wanaojifunza wengine, kuhudhuria saa za ofisi na kupata majibu kwa maswali yako kuhusu Mawakala wa AI.

## Rasilimali

- [MCP kwa Wakubwa](https://aka.ms/mcp-for-beginners)  
- [Nyaraka za MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Hifadhi ya NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Mfumo wa Mawakala wa Microsoft](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->