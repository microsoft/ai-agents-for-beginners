# Kumbukumbu kwa Wakala za AI 
[![Kumbukumbu ya Wakala](../../../translated_images/sw/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Wakati tunajadili faida za kipekee za kuundwa kwa Wakala wa AI, mambo mawili hasa hujadiliwa: uwezo wa kuitisha zana ili kukamilisha kazi na uwezo wa kuboresha kwa muda. Kumbukumbu iko kwenye msingi wa kuunda wakala anayejiboresha mwenyewe ambaye anaweza kuunda uzoefu bora kwa watumiaji wetu.

Katika somo hili, tutaangalia ni nini kumbukumbu kwa Wakala za AI na jinsi tunavyoweza kuisimamia na kuitumia kwa manufaa ya programu zetu.

## Utangulizi

Somo hili litashughulikia:

• **Kuelewa Kumbukumbu ya Wakala wa AI**: Kumbukumbu ni nini na kwa nini ni muhimu kwa mawakala.

• **Kutekeleza na Kuhifadhi Kumbukumbu**: Njia za vitendo za kuongeza uwezo wa kumbukumbu kwa mawakala wako wa AI, zikizingatia kumbukumbu ya muda mfupi na ya muda mrefu.

• **Kufanya Wakala wa AI Kujiboresha**: Jinsi kumbukumbu inavyowawezesha mawakala kujifunza kutoka kwa mwingiliano wa zamani na kuboresha kwa muda.

## Utekelezaji Upo

Somo hili linajumuisha sehemu mbili za mafunzo kamili za daftari:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Hutekeleza kumbukumbu kwa kutumia Mem0 na Azure AI Search na Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Hutekeleza kumbukumbu yenye muundo kwa kutumia Cognee, kujenga moja kwa moja grafu ya maarifa inayotegemea embeddings, kuonyesha grafu, na upataji wa akili

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utajua jinsi ya:

• **Kutofautisha aina mbalimbali za kumbukumbu za wakala wa AI**, ikijumuisha kumbukumbu ya kazi, ya muda mfupi, na ya muda mrefu, pamoja na aina maalum kama kumbukumbu ya persona na ya matukio.

• **Kutekeleza na kusimamia kumbukumbu ya muda mfupi na ya muda mrefu kwa mawakala wa AI** kwa kutumia Microsoft Agent Framework, ukiweka mbinu kama Mem0, Cognee, kumbukumbu za Whiteboard, na kuunganishwa na Azure AI Search.

• **Kuelewa misingi nyuma ya mawakala wa AI kujiboresha yenyewe** na jinsi mifumo imara ya usimamizi wa kumbukumbu inavyochangia kujifunza na kubadilika endelevu.

## Kuelewa Kumbukumbu ya Wakala wa AI

Kiini chake, **kumbukumbu kwa mawakala wa AI inahusu michakato inayowawezesha kuhifadhi na kukumbuka taarifa**. Taarifa hizi zinaweza kuwa maelezo maalum kuhusu mazungumzo, mapendeleo ya mtumiaji, matendo ya zamani, au hata mifumo iliyojifunza.

Bila kumbukumbu, programu za AI mara nyingi haziwezi kuhifadhi hali, maana ya kila mwingiliano huanza kutoka awali kabisa. Hii husababisha uzoefu wa mtumiaji unaorudiwa na kuchosha ambapo wakala "anasahau" muktadha wa awali au mapendelea.

### Kumbukumbu ni Muhimu Kwa Nini?

akili ya wakala imefungwa kwa undani na uwezo wake wa kukumbuka na kutumia taarifa za zamani. Kumbukumbu huwafanya mawakala kuwa:

• **Kitekelezi**: Kujifunza kutoka kwa matendo na matokeo ya zamani.

• **Mwingiliano**: Kudumisha muktadha katika mazungumzo yanayoendelea.

• **Kinachochukua Hatua na Kijibu**: Kutegemea mahitaji au kujibu ipasavyo kulingana na data ya zamani.

• **Huru**: Kufanya kazi kwa uhuru zaidi kwa kutumia maarifa yaliyohifadhiwa.

Lengo la kutekeleza kumbukumbu ni kufanya mawakala wawe zaidi **waaminifu na wenye uwezo**.

### Aina za Kumbukumbu

#### Kumbukumbu ya Kazi

Fikiria hii kama kipande cha karatasi cha kuandika mawakala hutumia wakati wa kazi au mchakato wa kufikiria unaoendelea. Hushikilia taarifa za haraka zinazohitajika kwa hatua inayofuata.

Kwa mawakala wa AI, kumbukumbu ya kazi mara nyingi huchukua taarifa muhimu zaidi kutoka kwenye mazungumzo, hata kama historia kamili ya gumzo ni ndefu au imekatika. Inazingatia kutoa vipengele muhimu kama mahitaji, mapendekezo, maamuzi, na vitendo.

**Mfano wa Kumbukumbu ya Kazi**

Katika wakala wa kuhifadhi safari, kumbukumbu ya kazi inaweza kushikilia ombi la mtumiaji la sasa, kama "Nataka kuweka safari kwenda Paris". Mahitaji haya maalum hushikiliwa katika muktadha wa wakala wa sasa kuongoza mwingiliano huu.

#### Kumbukumbu ya Muda Mfupi

Aina hii ya kumbukumbu hushikilia taarifa kwa muda wa mazungumzo au kikao kimoja. Ni muktadha wa gumzo la sasa, kuruhusu wakala kurejelea zamu za awali katika mazungumzo.

Katika mfano wa [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) wa Python SDK, hii inahusiana na `AgentSession`, iliyotengenezwa na `agent.create_session()`. Kikao hiki ndicho kumbukumbu ya muda mfupi ya mfumo huu: hudumisha muktadha wa mazungumzo inapatikana wakati kikao kimoja kinapotumika tena, lakini muktadha huo hauhifadhiwi wakati kikao kinapoisha au programu inapozimwa na kuzimwa tena. Tumia kumbukumbu ya muda mrefu kwa ukweli na mapendeleo yanayohitajika kuishi kwa vikao vingi, kawaida kupitia hifadhidata, kiashirio wa vector, au duka jingine la kudumu.

**Mfano wa Kumbukumbu ya Muda Mfupi**

Ikiwa mtumiaji atauliza, "Ndege ya kwenda Paris itagharimu kiasi gani?" na kisha aongeze na kuuliza "Na kuhusu malazi huko?", kumbukumbu ya muda mfupi huhakikisha wakala anajua "huko" linarejelea "Paris" ndani ya gumzo hilo hilo.

#### Kumbukumbu ya Muda Mrefu

Hii ni taarifa zinazodumu kwa vikao au mazungumzo mengi. Inaruhusu mawakala kukumbuka mapendeleo ya mtumiaji, mwingiliano wa kihistoria, au maarifa ya jumla kwa vipindi virefu. Hii ni muhimu kwa ubinafsishaji.

**Mfano wa Kumbukumbu ya Muda Mrefu**

Kumbukumbu ya muda mrefu inaweza kuhifadhi kuwa "Ben anapenda skiing na shughuli za nje, anapenda kahawa akiwa na mtazamo wa mlima, na anataka kuepuka mwinuko wa ski wa hali ya juu kutokana na jeraha la zamani". Taarifa hii, iliyojifunza kutoka kwa mwingiliano wa awali, huathiri mapendekezo katika vikao vya kupanga safari vya baadaye, na kuifanya iwe binafsi sana.

#### Kumbukumbu ya Persona

Aina hii maalum ya kumbukumbu husaidia wakala kuendeleza "mwenendo wa mtu" au "persona" thabiti. Inamruhusu wakala kukumbuka maelezo kuhusu nafsi yake au jukumu lake linalokusudiwa, na kufanya mwingiliano kuwa wa mtiririko zaidi na wa umakini.

**Mfano wa Kumbukumbu ya Persona**
Ikiwa wakala wa safari ameundwa kuwa "mpangaji mtaalamu wa skiing," kumbukumbu ya persona inaweza kuimarisha jukumu hili, kuathiri majibu yake kufanana na sauti na maarifa ya mtaalamu.

#### Kumbukumbu ya Mtiririko/Mitukio

Kumbukumbu hii huhifadhi mfuatano wa hatua ambazo wakala huchukua wakati wa kazi tata, ikiwa ni pamoja na mafanikio na kushindwa. Ni kama kukumbuka "vipindi" maalum au uzoefu wa zamani kujifunza kutoka kwao.

**Mfano wa Kumbukumbu ya Mitukio**

Ikiwa wakala alijaribu kuweka tiketi ya ndege maalum lakini ikashindwa kwa sababu ya ukosefu wa upatikanaji, kumbukumbu ya mitukio inaweza kurekodi kushindwa hii, kuruhusu wakala kujaribu ndege mbadala au kumjulisha mtumiaji kuhusu tatizo kwa njia iliyo na taarifa zaidi wakati wa jaribio lijalo.

#### Kumbukumbu ya Kitu

Hii inahusisha kutoa na kukumbuka vitu maalum (kama watu, maeneo, au vitu) na matukio kutoka kwa mazungumzo. Inamruhusu wakala kujenga uelewa wa muundo wa vipengele muhimu vilivyojadiliwa.

**Mfano wa Kumbukumbu ya Kitu**

Kutoka kwa mazungumzo kuhusu safari ya zamani, wakala anaweza kutoa "Paris," "Mnara wa Eiffel," na "chakula cha jioni katika mgahawa wa Le Chat Noir" kama vitu. Katika mwingiliano wa baadaye, wakala anaweza kukumbuka "Le Chat Noir" na kutoa kuanzisha uhifadhi mpya huko.

#### RAG Yenye Muundo (Retrieval Augmented Generation)

Ingawa RAG ni mbinu pana zaidi, "RAG Yenye Muundo" inazingatiwa kama teknolojia yenye nguvu ya kumbukumbu. Hutoa taarifa zilizo na muundo na zenye msongamano kutoka vyanzo mbalimbali (mazungumzo, barua pepe, picha) na kuzitumia kuboresha usahihi, upokeaji, na kasi ya majibu. Tofauti na RAG ya kawaida inayotegemea ufananishaji wa maana tu, RAG Yenye Muundo inafanya kazi na muundo wa taarifa ulio ndani yake.

**Mfano wa RAG Yenye Muundo**

Badala ya kulinganisha maneno tu, RAG Yenye Muundo inaweza kuchambua maelezo ya ndege (mahali pa kwenda, tarehe, muda, shirika la ndege) kutoka kwa barua pepe na kuiyahifadhi kwa njia yenye muundo. Hii inaruhusu maswali sahihi kama "Ndege gani niliyoipanga kwenda Paris siku ya Jumanne?"

## Kutekeleza na Kuhifadhi Kumbukumbu

Kutekeleza kumbukumbu kwa mawakala wa AI kunahusisha mchakato wa kimfumo wa **usimamizi wa kumbukumbu**, unaojumuisha kuzalisha, kuhifadhi, kupata, kuunganisha, kusasisha, na hata "kusahau" (au kufuta) taarifa. Upataji ni kipengele muhimu sana.

### Zana Maalum za Kumbukumbu

#### Mem0

Njia moja ya kuhifadhi na kusimamia kumbukumbu ya wakala ni kutumia zana maalum kama Mem0. Mem0 hufanya kazi kama safu ya kumbukumbu ya kudumu, ikiruhusu mawakala kukumbuka mwingiliano muhimu, kuhifadhi mapendeleo ya mtumiaji na muktadha wa ukweli, na kujifunza kutoka kwa mafanikio na kushindwa kwa muda. Wazo hapa ni kwamba mawakala wasio na hali wanageuka kuwa wenye hali.

Hufanya kazi kupitia **mchakato wa hatua mbili wa kumbukumbu: uchimbaji na sasisho**. Kwanza, ujumbe unaoongezwa kwenye mfululizo wa wakala hutumwa kwa huduma ya Mem0, ambayo hutumia Mfano Mkubwa wa Lugha (LLM) kufupisha historia ya mazungumzo na kutoa kumbukumbu mpya. Baadaye, hatua ya sasisho inayoungwa mkono na LLM hutoa uamuzi ikiwa kuongeza, kubadilisha, au kufuta kumbukumbu hizi, zikihifadhiwa katika duka la data la mseto ambalo linaweza kujumuisha hifadhidata za vector, grafu, na key-value. Mfumo huu pia unaunga mkono aina mbalimbali za kumbukumbu na unaweza kuingiza kumbukumbu za grafu kwa usimamizi wa uhusiano kati ya vitu.

#### Cognee

Njia nyingine yenye nguvu ni kutumia **Cognee**, kumbukumbu ya semantiki ya wazi kwa mawakala wa AI inayobadilisha data zenye muundo na zisizo na muundo kuwa grafu za maarifa zinazoweza kuchunguzwa zinazotegemewa na embeddings. Cognee hutoa **miundo ya duka miwili** inayochanganya utafutaji wa ufananishaji wa vector na uhusiano wa grafu, ikiruhusu mawakala kuelewa si tu ni taarifa gani zimefanana, bali jinsi dhana zinavyohusiana.

Inatazama kwa ufanisi **upataji mseto** unaochanganya ufananishaji wa vector, muundo wa grafu, na mantiki ya LLM - kutoka kwenye kutafuta kipande cha taarifa hadi majibu yanayojua grafu. Mfumo huu huweka kumbukumbu "hai" inayobadilika na kukua huku ikibaki inaweza kuchunguzwa kama grafu moja iliyounganishwa, ikisaidia muktadha wa kikao cha muda mfupi na kumbukumbu ya kudumu ya muda mrefu.

Mafunzo ya daftari ya Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) yanaonyesha jinsi ya kujenga safu hii moja ya kumbukumbu, pamoja na mifano ya vitendo ya kuingiza vyanzo mbalimbali vya data, kuona grafu ya maarifa, na kuuliza maswali kwa mikakati tofauti ya utafutaji iliyobinafsishwa kwa mahitaji maalum ya wakala.

### Kuhifadhi Kumbukumbu kwa RAG

Zaidi ya zana maalum za kumbukumbu kama Mem0, unaweza kutumia huduma imara za utafutaji kama **Azure AI Search kama sehemu ya nyuma ya kuhifadhi na kupata kumbukumbu**, hasa kwa RAG Yenye Muundo.

Hii inakuwezesha kuweka majibu ya wakala wako kwenye data yako mwenyewe, kuhakikisha majibu yanayofaa zaidi na sahihi zaidi. Azure AI Search inaweza kutumika kuhifadhi kumbukumbu za safari za mtumiaji, orodha za bidhaa, au maarifa mengine yoyote maalum ya eneo fulani.

Azure AI Search inaunga mkono uwezo kama **RAG Yenye Muundo**, ambayo inajivunia kutoa na kupata taarifa zilizo na muundo na msongamano kutoka kwa data kubwa kama historia za mazungumzo, barua pepe, au hata picha. Hii hutoa "usahihi na upokeaji wa kiwango cha juu zaidi" ikilinganishwa na mbinu za kawaida za kugawanya maandishi na embeddings.

## Kufanya Wakala wa AI Kujiboresha

Mchoro wa kawaida wa mawakala kujiboresha wenyewe unahusisha kuanzisha **"wakala wa maarifa"**. Wakala huyu tofauti hudhibiti mazungumzo kuu kati ya mtumiaji na wakala mkuu. Njia yake ni:

1. **Kutambua taarifa za thamani**: Kuamua kama sehemu yoyote ya mazungumzo ni muhimu kuhifadhiwa kama maarifa ya jumla au upendeleo wa mtumiaji maalum.

2. **Kutoa na kufupisha**: Kuchambua mafunzo muhimu au upendeleo kutoka kwa mazungumzo.

3. **Kuhifadhi katika msingi wa maarifa**: Kuhifadhi taarifa hii iliyotolewa, mara nyingi katika hifadhidata ya vector, ili iweze kupatikana baadaye.

4. **Kuongeza maswali ya baadaye**: Mtumiaji anapoanzisha swali jipya, wakala wa maarifa huchukua taarifa zilizo hifadhiwa na kuziambatanisha kwenye ombi la mtumiaji, kutoa muktadha muhimu kwa wakala mkuu (kama RAG).

### Ubunifu wa Kumbukumbu

• **Usimamizi wa Wakati wa Mwitikio**: Ili kuepuka kuchelewesha mwingiliano wa mtumiaji, mfano rahisi na wa haraka unaweza kutumiwa awali kuangalia haraka kama taarifa ni muhimu kuhifadhiwa au kupatikana, na kisha kutumia mchakato mgumu wa uchimbaji/upataji tu inapobidi.

• **Matengenezo ya Msingi wa Maarifa**: Kwa msingi unaoendelea kukua wa maarifa, taarifa zisizotumika mara kwa mara zinaweza kuhamishiwa "hifadhi baridi" ili kudhibiti gharama.

## Una Maswali Zaidi Kuhusu Kumbukumbu ya Wakala?

Jiunge na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kukutana na waendeshaji wengine wa kujifunza, kuhudhuria saa za ofisi na kupata majibu ya maswali yako kuhusu Wakala wa AI.
## Somo Lililotangulia

[Uhandisi wa Muktadha kwa Wakala wa AI](../12-context-engineering/README.md)

## Somo Linalofuata

[Kuchunguza Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->