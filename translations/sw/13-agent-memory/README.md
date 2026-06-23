# Kumbukumbu kwa Wawakilishi wa AI  
[![Agent Memory](../../../translated_images/sw/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Unapojadili faida za kipekee za kutengeneza Wawakilishi wa AI, mambo mawili yanajadiliwa zaidi: uwezo wa kuitisha zana kumaliza kazi na uwezo wa kuboresha kwa muda. Kumbukumbu ipo msingi wa kutengeneza wakala anayejiendeleza mwenyewe ambaye anaweza kuunda uzoefu bora kwa watumiaji wetu.

Katika somo hili, tutaangalia kile kumbukumbu ni kwa ajili ya Wawakilishi wa AI na jinsi tunaweza kuisimamia na kuitumia kwa manufaa ya programu zetu.

## Utangulizi

Somo hili litajumuisha:

• **Kuelewa Kumbukumbu ya Wakala wa AI**: Kumbukumbu ni nini na kwa nini ni muhimu kwa mawakala.

• **Kutekeleza na Kuhifadhi Kumbukumbu**: Mbinu za vitendo za kuongeza uwezo wa kumbukumbu kwa mawakala wako wa AI, ukizingatia kumbukumbu za muda mfupi na muda mrefu.

• **Kufanya Wawakilishi wa AI Kujiendeleza**: Jinsi kumbukumbu inavyowezesha mawakala kujifunza kutoka kwa mwingiliano wa zamani na kuboresha kwa muda.

## Utekelezaji Upo

Somo hili linajumuisha mafunzo mawili ya kina katika daftari la kumbukumbu:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Inatekeleza kumbukumbu kwa kutumia Mem0 na Azure AI Search pamoja na Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Inatekeleza kumbukumbu ya muundo kwa kutumia Cognee, kujenga moja kwa moja grafu ya maarifa inayotegemea embeddings, kuonyesha grafu, na uvutaji wa maarifa kwa akili

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utaweza:

• **Kutofautisha aina mbalimbali za kumbukumbu za wakala wa AI**, ikiwa ni pamoja na kumbukumbu za kazi, za muda mfupi, na za muda mrefu, pamoja na aina maalum kama kumbukumbu za persona na episodic.

• **Kutekeleza na kusimamia kumbukumbu za muda mfupi na muda mrefu kwa mawakala wa AI** kwa kutumia Microsoft Agent Framework, ukitumia zana kama Mem0, Cognee, kumbukumbu ya bodi nyeupe (Whiteboard), na kuingiza na Azure AI Search.

• **Kuelewa kanuni zilizopo nyuma ya mawakala wa AI wanaojiendeleza** na jinsi mifumo thabiti ya usimamizi wa kumbukumbu inavyochangia kujifunza na kuendana mabadiliko kwa kuendelea.

## Kuelewa Kumbukumbu ya Wakala wa AI

Kwa msingi wake, **kumbukumbu kwa mawakala wa AI inahusu mifumo inayowaruhusu kuhifadhi na kukumbuka taarifa**. Taarifa hizi zinaweza kuwa maelezo maalum kuhusu mazungumzo, mapendeleo ya mtumiaji, vitendo vya zamani, au hata mifumo iliyojifunza.

Bila kumbukumbu, programu za AI huwa mara nyingi hazina hali, maana kila mwingiliano huanza kutoka mwanzo. Hii husababisha uzoefu wa mtumiaji kuwa wa kurudia na wa kukasirishwa ambapo wakala "anasahau" muktadha wa awali au mapendeleo.

### Kwa Nini Kumbukumbu ni Muhimu?

Akili ya wakala imo kwa undani kwa uwezo wake wa kukumbuka na kutumia taarifa za zamani. Kumbukumbu huwezesha mawakala kuwa:

• **Wa kutafakari**: Kujifunza kutoka vitendo na matokeo ya zamani.

• **Wa kujihusisha**: Kuhifadhi muktadha wa mazungumzo yanayoendelea.

• **Wa kuanzisha na kujibu**: Kutabiri mahitaji au kujibu ipasavyo kwa kuzingatia data za kihistoria.

• **Wa kujitegemea**: Kufanya kazi kwa uhuru zaidi kwa kutumia maarifa yaliyohifadhiwa.

Lengo la kutekeleza kumbukumbu ni kufanya mawakala wawe zaidi **wa kuaminika na wenye uwezo**.

### Aina za Kumbukumbu

#### Kumbukumbu ya Kazi

Fikiria hii kama kama karatasi ya majaribio ambayo wakala hutumia wakati wa kazi au mchakato wa mawazo unaoendelea. Inahifadhi taarifa za haraka zinazohitajika kuhesabu hatua inayofuata.

Kwa mawakala wa AI, kumbukumbu ya kazi mara nyingi hukamata taarifa muhimu zaidi kutoka mazungumzo, hata kama historia kamili ya mazungumzo ni ndefu au imekatwa. Inazingatia kutoa vipengele muhimu kama mahitaji, mapendekezo, maamuzi, na vitendo.

**Mfano wa Kumbukumbu ya Kazi**

Katika wakala wa kuhifadhi tiketi za usafiri, kumbukumbu ya kazi inaweza kukamata ombi la mtumiaji kwa sasa, kama "Nataka kuhifadhi safari ya kwenda Paris". Mahitaji maalum haya yanahifadhiwa katika muktadha wa haraka wa wakala kuendesha mwingiliano wa sasa.

#### Kumbukumbu ya Muda Mfupi

Aina hii ya kumbukumbu huhifadhi taarifa kwa muda wa mazungumzo au kikao kimoja. Ni muktadha wa mazungumzo ya sasa, ukimaanisha wakala anaweza kurejelea sehemu za awali za mazungumzo.

Katika mifano ya SDK ya Python ya [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), hii inalingana na `AgentSession`, inayoundwa na `agent.create_session()`. Kikao ni kumbukumbu ya muda mfupi yenyewe kwenye mfumo: inahifadhi muktadha wa mazungumzo wakati kikao hicho kinatumiwa tena, lakini muktadha huu hauhifadhiwi baada ya kikao kumalizika au programu kuanzishwa upya. Tumia kumbukumbu ya muda mrefu kwa ajili ya ukweli na mapendeleo yanayotakiwa kuishi zaidi ya vikao, kawaida kupitia hifadhidata, index za vector, au duka jingine la kudumu.

**Mfano wa Kumbukumbu ya Muda Mfupi**

Ikiwa mtumiaji anauliza, "Ningepaje kupunguza gharama ya ndege kwenda Paris?" na kisha anaongeza "Na kuhusu makazi huko?" kumbukumbu ya muda mfupi inahakikisha wakala anajua "huko" inahusu "Paris" ndani ya mazungumzo hayo yale.

#### Kumbukumbu ya Muda Mrefu

Hii ni taarifa inayodumu kati ya mazungumzo au vikao vingi. Inaruhusu mawakala kukumbuka mapendeleo ya mtumiaji, mwingiliano wa kihistoria, au maarifa ya jumla kwa kipindi kirefu. Hii ni muhimu kwa ubinafsishaji.

**Mfano wa Kumbukumbu ya Muda Mrefu**

Kumbukumbu ya muda mrefu inaweza kuhifadhi kuwa "Ben anafurahia ski na shughuli za nje, anapenda kahawa na mtazamo wa mlima, na anataka kuepuka njia za ski za juu kutokana na jeraha la zamani". Taarifa hii, iliyojifunza kutoka kwa mwingiliano wa awali, huathiri mapendekezo katika vikao vya kupanga usafiri vijavyo, na kuifanya kuwa binafsi sana.

#### Kumbukumbu ya Persona

Aina maalum ya kumbukumbu hii husaidia wakala kuendeleza "umoja wa tabia" au "persona". Inamruhusu wakala kukumbuka maelezo kuhusu yeye mwenyewe au jukumu lake lililokusudiwa, na kufanya mwingiliano kuwa laini na wenye lengo.

**Mfano wa Kumbukumbu ya Persona**  
Kama wakala wa usafiri ameundwa kuwa "mtafiti mtaalamu wa mipango ya ski," kumbukumbu ya persona inaweza kuimarisha jukumu hili, na kuathiri majibu yake kulingana na sauti na maarifa ya mtaalamu.

#### Kumbukumbu ya Mtiririko/Matukio (Workflow/Episodic Memory)

Kumbukumbu hii huhifadhi mfululizo wa hatua ambayo wakala huchukua wakati wa kazi ngumu, ikijumuisha mafanikio na makosa. Ni kama kukumbuka "vipindi" maalum au uzoefu wa zamani kujifunza kutoka kwao.

**Mfano wa Kumbukumbu ya Matukio**

Ikiwa wakala alijaribu kuhifadhi tiketi ya ndege maalum lakini ikashindikana kwa sababu ya kutokuwepo, kumbukumbu ya matukio inaweza kurekodi kushindwa hii, na kumruhusu wakala kujaribu ndege mbadala au kumjulisha mtumiaji kuhusu tatizo hilo kwa njia yenye taarifa zaidi wakati wa jaribio lijalo.

#### Kumbukumbu ya Chungu (Entity Memory)

Hii inahusisha kutoa na kukumbuka vitu maalum (kama watu, maeneo, au vitu) na matukio kutoka mazungumzo. Inamruhusu wakala kujenga ufahamu wa muundo wa vipengele muhimu vilivyojadiliwa.

**Mfano wa Kumbukumbu ya Chungu**

Kutoka kwenye mazungumzo kuhusu safari ya zamani, wakala anaweza kutoa "Paris," "Mnara wa Eiffel," na "chakula cha jioni kwenye mgahawa wa Le Chat Noir" kama vitu. Katika mwingiliano wa baadaye, wakala anaweza kukumbuka "Le Chat Noir" na kutoa kutoa kuhifadhi nafasi mpya hapo.

#### RAG ya Muundo (Structured RAG - Retrieval Augmented Generation)

Ingawa RAG ni mbinu pana zaidi, "Structured RAG" inaangaziwa kama teknolojia yenye nguvu ya kumbukumbu. Inatoa taarifa nzito, za muundo kutoka vyanzo mbalimbali (mazungumzo, barua pepe, picha) na kuitumia kuboresha usahihi, kumbukumbu, na kasi katika majibu. Tofauti na RAG ya kawaida inayotegemea tu ulinganifu wa semantiki, Structured RAG hufanya kazi na muundo wa asili wa taarifa.

**Mfano wa Structured RAG**

Badala ya kulinganisha maneno muhimu tu, Structured RAG inaweza kusoma maelezo ya ndege (mwenendo, tarehe, wakati, shirika la ndege) kutoka barua pepe na kuhifadhi kwa njia ya muundo. Hii inaruhusu maswali sahihi kama "Ndege gani nilihifadhi kwenda Paris Jumanne?"

## Kutekeleza na Kuhifadhi Kumbukumbu

Kutekeleza kumbukumbu kwa mawakala wa AI kunahusisha mchakato wa kimfumo wa **usimamizi wa kumbukumbu**, unaojumuisha kuzalisha, kuhifadhi, kupata, kuunganisha, kusasisha, na hata "kusahau" (au kufuta) taarifa. Uvutaji ni sehemu muhimu sana.

### Zana Maalum za Kumbukumbu

#### Mem0

Njia moja ya kuhifadhi na kusimamia kumbukumbu ya wakala ni kutumia zana maalum kama Mem0. Mem0 hufanya kazi kama safu ya kumbukumbu iliyodumu, ikiruhusu mawakala kukumbuka mwingiliano muhimu, kuhifadhi mapendeleo ya mtumiaji na muktadha wa ukweli, na kujifunza kutoka mafanikio na makosa kwa muda. Dhana hapa ni kwamba mawakala wasio na hali hugeuka kuwa wenye hali.

Inafanya kazi kupitia **mchakato wa awamu mbili wa kumbukumbu: kutoa na kusasisha**. Kwanza, ujumbe unaoongezwa kwenye mfululizo wa wakala hutumwa kwa huduma ya Mem0, ambayo hutumia Mfano Mkubwa wa Lugha (LLM) kufanya muhtasari wa historia ya mazungumzo na kutoa kumbukumbu mpya. Baadaye, hatua ya sasisho inayosimamiwa na LLM huamua kama kuziongeza, kubadilisha, au kufuta kumbukumbu hizi, na kuzihifadhi katika duka la data la mseto linaloweza kujumuisha hifadhidata za vector, grafu, na key-value. Mfumo huu pia unaunga mkono aina mbalimbali za kumbukumbu na unaweza kujumuisha kumbukumbu ya grafu kwa kusimamia uhusiano kati ya vitu.

#### Cognee

Njia nyingine yenye nguvu ni kutumia **Cognee**, kumbukumbu ya semantiki ya chanzo wazi kwa mawakala wa AI inayobadilisha data za muundo na zisizo za muundo kuwa grafu za maarifa zinazoweza kuchujwa zinazotegemea embeddings. Cognee hutoa **mipangilio miwili ya kuhifadhi** inayochanganya utafutaji wa ulinganifu wa vector na uhusiano wa grafu, kuziwezesha mawakala kuelewa si tu taarifa sawa na vipi dhana zinavyohusiana.

Inakamilika katika **uvutaji wa mseto** unaochanganya ulinganifu wa vector, muundo wa grafu, na muktadha wa LLM - kutoka kutafuta kipande halisi hadi majibu yanayojumuisha maarifa ya grafu. Mfumo unadumisha **kumbukumbu inayozidi kuishi** inayokua na kuendelea huku ikibaki inaweza kuchujwa kama grafu moja iliyounganishwa, kuunga mkono muktadha wa kikao cha muda mfupi na kumbukumbu ya kudumu ya muda mrefu.

Mafunzo ya daftari la Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) yanaonyesha jinsi ya kujenga safu hii ya kumbukumbu iliyojumuishwa, kwa mifano ya vitendo ya kuingiza vyanzo mbalimbali vya data, kuonyesha grafu ya maarifa, na kuuliza maswali kwa mikakati tofauti ya utafutaji iliyobinafsishwa kwa mahitaji maalum ya wakala.

### Kuhifadhi Kumbukumbu kwa RAG

Zaidi ya zana maalum za kumbukumbu kama mem0 , unaweza kutumia huduma madhubuti za utafutaji kama **Azure AI Search kama msingi wa kuhifadhi na kupata kumbukumbu**, hasa kwa Structured RAG.

Hii inakuwezesha kuimarisha majibu ya wakala wako kwa data yako mwenyewe, kuhakikisha majibu yanayofaa na sahihi zaidi. Azure AI Search inaweza kutumika kuhifadhi kumbukumbu za usafiri za mtumiaji, katalogi za bidhaa, au maarifa mengine maalum ya sekta.

Azure AI Search inaunga mkono uwezo kama **Structured RAG**, ambayo inakamilika kutoa na kupata taarifa nzito, za muundo kutoka kwenye seti kubwa za data kama historia ya mazungumzo, barua pepe, au hata picha. Hii hutoa "usahihi na kumbukumbu ya kiwango cha juu" ukilinganisha na mbinu za kawaida za kugawanya maandishi na embeddings.

## Kufanya Wawakilishi wa AI Waendelee Kujiboresha

Mfumo wa kawaida kwa mawakala wanaojiendeleza ni kuanzisha **"wakala maarifa"**. Wakala huyu tofauti huangalia mazungumzo kuu kati ya mtumiaji na wakala mkuu. Jukumu lake ni:

1. **Kubaini taarifa muhimu**: Kuamua kama sehemu yoyote ya mazungumzo inastahili kuokolewa kama maarifa ya jumla au upendeleo maalum wa mtumiaji.

2. **Kutoa na kufupisha**: Kuchuja somo muhimu au upendeleo kutoka mazungumzo.

3. **Kuhifadhi katika hifadhi ya maarifa**: Kuhifadhi taarifa hii iliyochujwa, mara nyingi katika hifadhidata ya vector, ili iweze kupatikana baadaye.

4. **Kuongeza maswali ya baadaye**: Mtumiaji anapoanzisha swali jipya, wakala maarifa hunyakua taarifa husika zilizohifadhiwa na kuziambatanisha kwenye maoni ya mtumiaji, kutoa muktadha muhimu kwa wakala mkuu (kama RAG).

### Uboreshaji wa Kumbukumbu

• **Usimamizi wa Muda wa Kujibu**: Ili kuepuka kuchelewesha mwingiliano wa mtumiaji, mfano wa gharama nafuu na wa haraka unaweza kutumika awali kukagua kama taarifa ni muhimu kuhifadhi au kupata, na kuanzisha mchakato wa kuchuja/kupata wenye ugumu zaidi tu pale inapohitajika.

• **Matengenezo ya Hifadhidata ya Maarifa**: Kwa hifadhidata inayokua, taarifa ambazo hazitumiki mara kwa mara zinaweza kuhifadhiwa kwenye "hifadhi baridi" ili kudhibiti gharama.

## Una Maswali Zaidi Kuhusu Kumbukumbu ya Wakala?

Jiunge na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) kukutana na wajifunzaji wengine, kuhudhuria saa za ofisi na kupata majibu kwa maswali yako kuhusu Wawakilishi wa AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->