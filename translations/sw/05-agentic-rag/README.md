[![Agentic RAG](../../../translated_images/sw/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Bonyeza picha hapo juu kutazama video ya somo hili)_

# Agentic RAG

Somo hili linatoa muhtasari kamili wa Agentic Retrieval-Augmented Generation (Agentic RAG), mfumo mpya wa AI ambapo mifano mikubwa ya lugha (LLMs) huandaa hatua zao zinazofuata kwa hiari huku wakivuta taarifa kutoka vyanzo vya nje. Tofauti na mifumo ya kawaida ya kuchukua kisha kusoma, Agentic RAG inahusisha simu za mfululizo kwa LLM, ikichanganywa na simu za zana au kazi pamoja na matokeo yaliyopangwa. Mfumo huangalia matokeo, huboresha maswali, hutumia zana za ziada ikiwa zinahitajika, na kuendelea mzunguko huu hadi suluhisho linaloridhisha lipatikane.

## Utangulizi

Somo hili litashughulikia

- **Kuelewa Agentic RAG:** Jifunze kuhusu mfumo unaochipukia katika AI ambapo mifano mikubwa ya lugha (LLMs) huandaa hatua zao zinazofuata kwa hiari huku wakivuta taarifa kutoka vyanzo vya data vya nje.
- **Kuelewa Mtindo wa Iterative Maker-Checker:** Elewa mzunguko wa simu za mfululizo kwa LLM, ikichanganywa na simu za zana au kazi pamoja na matokeo yaliyopangwa, yaliyobuniwa kuboresha usahihi na kushughulikia maswali mabaya.
- **Chunguza Matumizi ya Kivitendo:** Tambua hali ambapo Agentic RAG huangaza, kama mazingira ya usahihi kwanza, mwingiliano mgumu wa database, na michakato iliyosogezwa mbele.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utajua jinsi ya/kuelewa:

- **Kuelewa Agentic RAG:** Jifunze kuhusu mfumo unaochipukia katika AI ambapo mifano mikubwa ya lugha (LLMs) huandaa hatua zao zinazofuata kwa hiari huku wakivuta taarifa kutoka vyanzo vya data vya nje.
- **Mtindo wa Iterative Maker-Checker:** Elewa dhana ya mzunguko wa simu za mfululizo kwa LLM, ikichanganywa na simu za zana au kazi pamoja na matokeo yaliyopangwa, yaliyobuniwa kuboresha usahihi na kushughulikia maswali mabaya.
- **Kumiliki Mchakato wa Kifikra:** Fahamu uwezo wa mfumo kumiliki mchakato wake wa kifikra, kufanya maamuzi juu ya jinsi ya kushughulikia matatizo bila kutegemea njia zilizopangwa awali.
- **Mtiririko wa Kazi:** Elewa jinsi mfano wa agentic unavyoamua pekee kuvuta ripoti za mwenendo wa soko, kutambua data za washindani, kuhusisha vipimo vya mauzo vya ndani, kuunganisha matokeo, na kutathmini mkakati.
- **Mizunguko ya Iterative, Urahisishaji wa Zana, na Kumbukumbu:** Jifunze kuhusu utegemezi wa mfumo kwenye muundo wa mwingiliano wa mzunguko, unaodumisha hali na kumbukumbu hatua kwa hatua ili kuepuka mizunguko ya kurudia na kufanya maamuzi yenye taarifa zaidi.
- **Kushughulikia Njia za Kushindwa na Kujirekebisha:** Chunguza mbinu thabiti za kujirekebisha za mfumo, ikiwa ni pamoja na kurudia na kuuliza maswali tena, kutumia zana za uchunguzi, na kurudi kwa usimamizi wa binadamu.
- **Mipaka ya Uwakilishi:** Fahamu vikwazo vya Agentic RAG, ikizingatia uhuru wa kikoa fulani, utegemezi wa miundombinu, na heshima kwa mipaka ya usalama.
- **Matumizi ya Kivitendo na Thamani:** Tambua hali ambapo Agentic RAG huangaza, kama mazingira ya usahihi kwanza, mwingiliano mgumu wa database, na michakato iliyosogezwa mbele.
- **Utawala, Uwajibikaji, na Uaminifu:** Jifunze kuhusu umuhimu wa utawala na uwazi, ikiwa ni pamoja na ufafanuzi wa mchakato wa kifikra, udhibiti wa upendeleo, na usimamizi wa binadamu.

## Agentic RAG ni nini?

Agentic Retrieval-Augmented Generation (Agentic RAG) ni mfumo mpya wa AI ambapo mifano mikubwa ya lugha (LLMs) huandaa hatua zao zinazofuata kwa hiari huku wakivuta taarifa kutoka vyanzo vya nje. Tofauti na mifumo ya kawaida ya kuchukua kisha kusoma, Agentic RAG inahusisha simu za mfululizo kwa LLM, ikichanganywa na simu za zana au kazi pamoja na matokeo yaliyopangwa. Mfumo huu unathibitisha matokeo, huboresha maswali, hutumia zana za ziada ikiwa zinahitajika, na kuendelea mzunguko huu hadi suluhisho linaloridhisha lipatikane. Mtindo huu wa mchakato wa "maker-checker" husaidia kuboresha usahihi, kushughulikia maswali mabaya, na kuhakikisha matokeo ya hali ya juu.

Mfumo huu unamiliki kikamilifu mchakato wake wa kifikra, kurekebisha maswali yaliyoshindwa, kuchagua mbinu tofauti za utafutaji, na kuunganisha zana nyingi—kama vile utafutaji wa vekta katika Azure AI Search, databases za SQL, au API maalum—kabla ya kumaliza jibu lake. Sifa inayomtofautisha mfumo wa agentic ni uwezo wake wa kumiliki mchakato wake wa kifikra. Matumizi ya kawaida ya RAG hutegemea njia zilizopangwa awali, lakini mfumo wa agentic huamua kwa hiari mfululizo wa hatua kulingana na ubora wa taarifa anazopata.

## Kufafanua Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) ni mfumo mpya wa maendeleo ya AI ambapo LLM huchukua taarifa kutoka vyanzo vya data vya nje na pia huandaa hatua zake zinazofuata kwa hiari. Tofauti na mifumo ya kawaida ya kuchukua kisha kusoma au mfuatano wa maelekezo yaliyopangwa kwa uangalifu, Agentic RAG huhusisha mzunguko wa simu mfululizo kwa LLM, ikichanganywa na simu za zana au kazi pamoja na matokeo yaliyopangwa. Kila mara, mfumo huu huthibitisha matokeo aliyoyapata, huamua kama aendelee kuboresha maswali, hutumia zana za ziada ikiwa zinahitajika, na kuendelea mzunguko huu hadi afikie suluhisho linaloridhisha.

Mtindo huu wa mchakato wa "maker-checker" umeundwa kuboresha usahihi, kushughulikia maswali mabaya kwa databases zilizopangwa (k.m. NL2SQL), na kuhakikisha matokeo yenye usawa na ubora wa hali ya juu. Badala ya kutegemea mfuatano wa maelekezo yaliyobuniwa kwa uangalifu, mfumo huu unamiliki kikamilifu mchakato wake wa kifikra. Unaweza kuandika upya maswali yaliyoshindwa, kuchagua mbinu tofauti za utafutaji, na kuunganisha zana nyingi—kama vile utafutaji wa vekta katika Azure AI Search, databases za SQL, au API maalum—kabla ya kumaliza jibu. Hii inazuia haja ya mifumo tata ya uratibu. Badala yake, mzunguko rahisi wa "simu LLM → matumizi ya zana → simu LLM → …" unaweza kutoa matokeo yaliyo bora na yenye msingi mzuri.

![Agentic RAG Core Loop](../../../translated_images/sw/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Kumiliki Mchakato wa Kifikra

Sifa inayomtofautisha mfumo kuwa "agentic" ni uwezo wake wa kumiliki mchakato wake wa kifikra. Matumizi ya kawaida ya RAG mara nyingi hutegemea binadamu kuweka njia kwa mfano: mfuatano wa mawazo unaoelezea nini cha kuchukua na lini.
Lakini mfumo ukiwa kweli agentic, huamua ndani yake jinsi ya kushughulikia tatizo. Sio tu kutekeleza maandishi; ni kuamua kwa hiari mfuatano wa hatua kulingana na ubora wa taarifa anazopata.
Kwa mfano, ikiwa unaombwa kutengeneza mkakati wa kuanzisha bidhaa, haitegemee kabisa maelekezo yanayoelezea mchakato mzima wa utafiti na maamuzi. Badala yake, mfano wa agentic huamua pekee kufanya:

1. Kuvuta ripoti za mwenendo wa soko wa sasa kwa kutumia Bing Web Grounding
2. Kutambua data za washindani husika kwa kutumia Azure AI Search.
3. Kuunganisha vipimo vya mauzo vya ndani vya kihistoria kwa kutumia Azure SQL Database.
4. Kuunganisha matokeo kuwa mkakati unaoendeshwa kupitia Azure OpenAI Service.
5. Kutathmini mkakati kwa mapungufu au kutokubaliana, kuanzisha mzunguko mwingine wa utafutaji ikiwa inahitajika.
Hatua zote hizi—kuboresha maswali, kuchagua vyanzo, kurudia mpaka "kuridhika" na jibu—huamuliwa na mfano, si maandishi yaliyotengenezwa na mwanadamu.

## Mizunguko ya Iterative, Urahisishaji wa Zana, na Kumbukumbu

![Tool Integration Architecture](../../../translated_images/sw/tool-integration.0f569710b5c17c10.webp)

Mfumo wa agentic hutegemea muundo wa mwingiliano wa mzunguko:

- **Simu ya Awali:** Lengo la mtumiaji (yaani. amri ya mtumiaji) linaonyeshwa kwa LLM.
- **Matumizi ya Zana:** Ikiwa mfano unatambua taarifa zilizokosekana au maelekezo tata, huchagua zana au mbinu ya utafutaji—kama uchunguzi wa database ya vekta (kwa mfano Azure AI Search Hybrid juu ya data binafsi) au simu ya SQL iliyopangwa—kukuza muktadha zaidi.
- **Tathmini & Kuboresha:** Baada ya kupitia data iliyopokelewa, mfano huamua kama taarifa ni ya kutosha. Ikiwa si, huboresha swali, jaribu zana nyingine, au kubadilisha mbinu.
- **Rudia Hadi Kuridhika:** Mzunguko huu unaendelea hadi mfano uamue kuwa una uelewa na ushahidi wa kutosha kutoa jibu la mwisho lisilo na makosa.
- **Kumbukumbu & Hali:** Kwa sababu mfumo huhifadhi hali na kumbukumbu kati ya hatua, unaweza kukumbuka jaribio zilizopita na matokeo yake, kuepuka kurudia kazini na kufanya maamuzi yenye taarifa zaidi wakati unaendelea.

Kadiri muda unavyopita, hii huunda hisia ya uelewa unaokua, kuruhusu mfano kuendesha kazi ngumu za hatua nyingi bila binadamu kuingilia au kubadilisha amri kila mara.

## Kushughulikia Njia za Kushindwa na Kujirekebisha

Uhuru wa Agentic RAG pia unahusisha mbinu thabiti za kujirekebisha. Wakati mfumo unakumbana na vizingiti—kama kupata nyaraka zisizohusiana au maswali mabaya—unaweza:

- **Kurudia na Kuuliza Maswali Mara Tena:** Badala ya kurudisha majibu yasiyo ya thamani, mfano hujaribu mbinu mpya za utafutaji, kuandika upya maswali ya database, au kuangalia seti nyingine za data.
- **Matumizi ya Zana za Uchunguzi:** Mfumo unaweza kuitisha kazi za ziada zilizobuniwa kusaidia kusahihisha hatua zake za kifikra au kuthibitisha usahihi wa data iliyopatikana. Zana kama Azure AI Tracing zitakuwa muhimu kuwezesha ufuatiliaji na uangalizi thabiti.
- **Kurudi kwa Usimamizi wa Binadamu:** Kwa hali zenye hatari kubwa au zinazoshindwa mara kwa mara, mfano unaweza kuashiria kutokuwa na uhakika na kuomba mwongozo wa binadamu. Mara binadamu anapotoa maoni ya kurekebisha, mfano unaweza kujifunza kutoka somo hilo kwa mbele.

Mbinu hii ya mzunguko na mabadiliko huwezesha mfano kuboresha daima, kuhakikisha sio mfumo wa kipindi kimoja tu bali unaojifunza kutokana na makosa wakati wa kikao fulani.

![Self Correction Mechanism](../../../translated_images/sw/self-correction.da87f3783b7f174b.webp)

## Mipaka ya Uwakilishi

Licha ya uhuru wake ndani ya kazi fulani, Agentic RAG si sawa na Akili ya Ujumuishaji wa Jumla ya Bandia (AGI). Uwezo wake wa "agentic" umepunguzwa kwa zana, vyanzo vya data, na sera zinazotolewa na waendelezaji binadamu. Haiwezi kuunda zana zake mwenyewe au kutoka katika mipaka ya eneo lililowekwa. Badala yake, inaongoza kwa kuandaa rasilimali zilizo karibu kwa ufanisi.
Tofauti kuu na aina za AI zilizo juu zaidi ni pamoja na:

1. **Uhuru wa Kikoa Mahususi:** Mifumo ya Agentic RAG inalenga kufanikisha malengo yaliyowekwa na mtumiaji ndani ya kikoa kinachojulikana, ikitumia mikakati kama kuandika upya maswali au kuchagua zana kuboresha matokeo.
2. **Kutegemea Miundombinu:** Uwezo wa mfumo hutegemea zana na data zilizojumuishwa na waendelezaji. Haiwezi kuvuka mipaka hii bila uingizaji wa binadamu.
3. **Heshima kwa Mipaka:** Miongozo ya maadili, sheria za utekelezaji, na sera za kibiashara bado ni muhimu sana. Uhuru wa wakala daima unazuiliwa na hatua za usalama na mbinu za usimamizi (huenda?).

## Matumizi ya Kivitendo na Thamani

Agentic RAG huangaza katika hali zinazohitaji kuboresha hatua kwa hatua na usahihi:

1. **Mazingira ya Usahihi Kwanza:** Katika ukaguzi wa ufuataji, uchambuzi wa kanuni, au utafiti wa kisheria, mfano wa agentic unaweza kuthibitisha mara kwa mara ukweli, kushauriana na vyanzo vingi, na kuandika upya maswali hadi apate jibu lililokaguliwa vizuri.
2. **Mwingiliano Mgumu wa Database:** Wakati wa kushughulikia data zilizopangwa ambapo maswali huenda yakashindikana mara kwa mara au yanahitaji marekebisho, mfumo unaweza kuboresha maswali kwa hiari kwa kutumia Azure SQL au Microsoft Fabric OneLake, kuhakikisha utafutaji wa mwisho unalingana na nia ya mtumiaji.
3. **Mtiririko wa Kazi Mrefu:** Vikao vinavyoendelea kwa muda mrefu vinaweza kubadilika kadri taarifa mpya inavyojitokeza. Agentic RAG inaweza kuingiza data mpya kila mara, kubadilisha mikakati kadri inavyojifunza zaidi kuhusu tatizo.

## Utawala, Uwajibikaji, na Uaminifu

Wakati mifumo hii inavyokuwa na uhuru zaidi katika mchakato wao wa kifikra, utawala na uwazi ni muhimu:

- **Ufafanuzi wa Mchakato wa Kifikra:** Mfano unaweza kutoa rekodi ya maswali aliyoyaweka, vyanzo alivyokagua, na hatua za kifikra alizochukua kufikia hitimisho. Zana kama Azure AI Content Safety na Azure AI Tracing / GenAIOps zinaweza kusaidia kudumisha uwazi na kupunguza hatari.
- **Udhibiti wa Upendeleo na Utafutaji wa Kulingana:** Waendelezaji wanaweza kuandaa mikakati ya utafutaji kuhakikisha vyanzo vya data vyenye uwakilishi na usawa vinazingatiwa, na kukagua mara kwa mara matokeo kugundua upendeleo au mifumo iliyopotoshwa kwa kutumia mifano maalum kwa mashirika ya sayansi ya data yanayotumia Azure Machine Learning.
- **Usimamizi wa Binadamu na Ufuataji:** Kwa kazi nyeti, hakiki za binadamu bado ni muhimu. Agentic RAG haibadilishi hukumu ya binadamu katika maamuzi yenye hatari kubwa—huongeza kwa kutoa chaguzi zilizokaguliwa vyema.

Kuwa na zana zinazotoa rekodi wazi ya hatua ni muhimu. Bila hizo, kutatua kasoro katika mchakato wa hatua nyingi kunaweza kuwa vigumu sana. Angalia mfano ufuatao kutoka Literal AI (kampuni nyuma ya Chainlit) kwa mtiririko wa agent:

![AgentRunExample](../../../translated_images/sw/AgentRunExample.471a94bc40cbdc0c.webp)

## Hitimisho

Agentic RAG inawakilisha mageuzi ya asili katika jinsi mifumo ya AI inavyoshughulikia kazi ngumu zinazohitaji data nyingi. Kwa kutumia muundo wa mwingiliano wa mzunguko, kuchagua zana kwa hiari, na kuboresha maswali hadi kufikia matokeo bora, mfumo unazidi kufuata amri za kawaida na kuwa mtengenezaji wa maamuzi yenye uelewa wa muktadha na uwezo wa kurekebisha. Ingawa bado yanapimwa na miundombinu na miongozo ya maadili inayowekwa na binadamu, uwezo huu wa agentic unakuza mwingiliano wa AI wenye ufanisi zaidi, wenye muktadha mzuri, na hatimaye wenye manufaa kwa mashirika na watumiaji.

### Una Maswali Zaidi kuhusu Agentic RAG?

Jiunge na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kukutana na wanafunzi wengine, kuhudhuria saa za ofisi na kupata majibu kwa maswali yako kuhusu AI Agents.

## Rasilimali Zaidi

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Tekeleza Retrieval Augmented Generation (RAG) kwa Azure OpenAI Service: Jifunze jinsi ya kutumia data yako mwenyewe pamoja na Azure OpenAI Service. Moduli hii ya Microsoft Learn inatoa mwongozo kamili wa utekelezaji wa RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Tathmini ya programu za AI za kizazi pamoja na Microsoft Foundry: Makala hii inashughulikia tathmini na kulinganisha mifano kwenye dataset zilizo ndani ya umma, ikiwa ni pamoja na matumizi ya Agentic AI na usanifu wa RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Agentic RAG ni nini | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Mwongozo Kamili wa Agent-Based Retrieval Augmented Generation – Habari kutoka generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: ongeza kasi RAG yako kwa kutumia mabadiliko ya maswali na kuuliza mwenyewe! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Kuongeza Tabaka za Agentic kwa RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Masaibu ya Wasaidizi wa Maarifa: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Jinsi ya Kujenga Mifumo ya Agentic RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Kutumia Huduma ya Microsoft Foundry Agent kuongeza ukubwa wa maajenti wako wa AI</a>

### Makala za Kitaalamu

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Uboreshaji wa Iterative kwa Kujiripoti</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Mawakala wa Lugha wenye Kujifunza kwa Nguvu ya Maneno</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Mifano Mikubwa ya Lugha Inaweza Kujirekebisha Pamoja na Ukosoaji wa Vyombo</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Utafiti wa Agentic RAG</a>

## Kupima kwa Haraka Huu Mwakala (Hiari)

Baada ya kujifunza kuanzisha maajenti katika [Somo la 16](../16-deploying-scalable-agents/README.md), unaweza kupima kwa haraka `TravelRAGAgent` wa somo hili — ukithibitisha kuwa majibu yake yanatokana na hifadhidata ya maarifa — kwa kutumia [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Angalia [`tests/README.md`](../tests/README.md) kwa jinsi ya kuendesha.

## Somo lililotangulia

[Mfumo wa Muundo wa Matumizi ya Zana](../04-tool-use/README.md)

## Somo linalofuata

[Kujenga Maajenti wa AI wa Kuaminika](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->