<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-29T19:57:37+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "sw"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.sw.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Bofya picha hapo juu kutazama video ya somo hili)_

# Agentic RAG

Somo hili linatoa muhtasari wa kina kuhusu Agentic Retrieval-Augmented Generation (Agentic RAG), dhana mpya ya AI ambapo mifano mikubwa ya lugha (LLMs) hupanga hatua zao zinazofuata kwa uhuru huku ikichota taarifa kutoka vyanzo vya nje. Tofauti na mifumo ya kawaida ya "retrieval-then-read", Agentic RAG inahusisha miito ya mara kwa mara kwa LLM, ikichanganywa na matumizi ya zana au kazi na matokeo yaliyojengwa. Mfumo huu hutathmini matokeo, kurekebisha maswali, kutumia zana za ziada inapohitajika, na kuendelea na mzunguko huu hadi suluhisho la kuridhisha lipatikane.

## Utangulizi

Somo hili litashughulikia:

- **Kuelewa Agentic RAG:** Jifunze kuhusu dhana mpya ya AI ambapo mifano mikubwa ya lugha (LLMs) hupanga hatua zao zinazofuata kwa uhuru huku ikichota taarifa kutoka vyanzo vya data vya nje.
- **Kuelewa Mtindo wa Iterative Maker-Checker:** Fahamu mzunguko wa miito ya mara kwa mara kwa LLM, ikichanganywa na matumizi ya zana au kazi na matokeo yaliyojengwa, iliyoundwa kuboresha usahihi na kushughulikia maswali yaliyokosewa.
- **Gundua Matumizi ya Kivitendo:** Tambua hali ambapo Agentic RAG inang'aa, kama mazingira yanayozingatia usahihi, mwingiliano tata wa hifadhidata, na mtiririko wa kazi wa muda mrefu.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utaweza kuelewa/kufanya:

- **Kuelewa Agentic RAG:** Jifunze kuhusu dhana mpya ya AI ambapo mifano mikubwa ya lugha (LLMs) hupanga hatua zao zinazofuata kwa uhuru huku ikichota taarifa kutoka vyanzo vya data vya nje.
- **Mtindo wa Iterative Maker-Checker:** Fahamu dhana ya mzunguko wa miito ya mara kwa mara kwa LLM, ikichanganywa na matumizi ya zana au kazi na matokeo yaliyojengwa, iliyoundwa kuboresha usahihi na kushughulikia maswali yaliyokosewa.
- **Kumiliki Mchakato wa Uamuzi:** Elewa uwezo wa mfumo wa kumiliki mchakato wake wa kufikiri, kufanya maamuzi kuhusu jinsi ya kushughulikia matatizo bila kutegemea njia zilizowekwa awali.
- **Mtiririko wa Kazi:** Elewa jinsi mfano wa agentic unavyoamua kwa uhuru kuchota ripoti za mwenendo wa soko, kutambua data ya washindani, kuhusisha vipimo vya mauzo vya ndani, kuunganisha matokeo, na kutathmini mkakati.
- **Mizunguko ya Iterative, Ujumuishaji wa Zana, na Kumbukumbu:** Jifunze kuhusu utegemezi wa mfumo kwenye muundo wa mwingiliano wa mzunguko, kudumisha hali na kumbukumbu katika hatua ili kuepuka mizunguko ya kurudia na kufanya maamuzi sahihi.
- **Kushughulikia Njia za Kushindwa na Kujirekebisha:** Chunguza mifumo thabiti ya kujirekebisha ya mfumo, ikiwa ni pamoja na kurudia na kuuliza tena, kutumia zana za uchunguzi, na kutegemea usimamizi wa binadamu inapohitajika.
- **Mipaka ya Uwezo wa Kujitegemea:** Elewa mapungufu ya Agentic RAG, ukizingatia uhuru maalum wa kikoa, utegemezi wa miundombinu, na kuheshimu vizuizi.
- **Matumizi ya Kivitendo na Thamani:** Tambua hali ambapo Agentic RAG inang'aa, kama mazingira yanayozingatia usahihi, mwingiliano tata wa hifadhidata, na mtiririko wa kazi wa muda mrefu.
- **Usimamizi, Uwazi, na Uaminifu:** Jifunze kuhusu umuhimu wa usimamizi na uwazi, ikiwa ni pamoja na kufikiri kwa kueleweka, udhibiti wa upendeleo, na usimamizi wa binadamu.

## Agentic RAG ni Nini?

Agentic Retrieval-Augmented Generation (Agentic RAG) ni dhana mpya ya AI ambapo mifano mikubwa ya lugha (LLMs) hupanga hatua zao zinazofuata kwa uhuru huku ikichota taarifa kutoka vyanzo vya nje. Tofauti na mifumo ya kawaida ya "retrieval-then-read", Agentic RAG inahusisha miito ya mara kwa mara kwa LLM, ikichanganywa na matumizi ya zana au kazi na matokeo yaliyojengwa. Mfumo huu hutathmini matokeo, kurekebisha maswali, kutumia zana za ziada inapohitajika, na kuendelea na mzunguko huu hadi suluhisho la kuridhisha lipatikane. Mtindo huu wa "maker-checker" wa kurudia unalenga kuboresha usahihi, kushughulikia maswali yaliyokosewa, na kuhakikisha matokeo ya hali ya juu.

Mfumo huu unamiliki mchakato wake wa kufikiri kwa uhuru, kuandika upya maswali yaliyoshindwa, kuchagua mbinu tofauti za kuchota taarifa, na kuunganisha zana mbalimbali—kama utafutaji wa vector katika Azure AI Search, hifadhidata za SQL, au API maalum—kabla ya kukamilisha jibu lake. Sifa ya kipekee ya mfumo wa agentic ni uwezo wake wa kumiliki mchakato wake wa kufikiri. Utekelezaji wa kawaida wa RAG hutegemea njia zilizowekwa awali, lakini mfumo wa agentic huamua kwa uhuru mlolongo wa hatua kulingana na ubora wa taarifa inayopatikana.

## Kufafanua Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) ni dhana mpya katika maendeleo ya AI ambapo LLMs si tu zinachota taarifa kutoka vyanzo vya data vya nje bali pia hupanga hatua zao zinazofuata kwa uhuru. Tofauti na mifumo ya kawaida ya "retrieval-then-read" au mlolongo wa maelekezo yaliyopangwa kwa uangalifu, Agentic RAG inahusisha mzunguko wa miito ya mara kwa mara kwa LLM, ikichanganywa na matumizi ya zana au kazi na matokeo yaliyojengwa. Kila hatua, mfumo hutathmini matokeo yaliyopatikana, kuamua kama kurekebisha maswali, kutumia zana za ziada inapohitajika, na kuendelea na mzunguko huu hadi suluhisho la kuridhisha lipatikane.

Mtindo huu wa "maker-checker" wa kurudia unalenga kuboresha usahihi, kushughulikia maswali yaliyokosewa kwa hifadhidata zilizojengwa (mfano NL2SQL), na kuhakikisha matokeo ya hali ya juu na yenye usawa. Badala ya kutegemea tu mlolongo wa maelekezo yaliyoundwa kwa uangalifu, mfumo unamiliki mchakato wake wa kufikiri kwa uhuru. Unaweza kuandika upya maswali yaliyoshindwa, kuchagua mbinu tofauti za kuchota taarifa, na kuunganisha zana mbalimbali—kama utafutaji wa vector katika Azure AI Search, hifadhidata za SQL, au API maalum—kabla ya kukamilisha jibu lake. Hii huondoa hitaji la mifumo tata ya uratibu. Badala yake, mzunguko rahisi wa "miito ya LLM → matumizi ya zana → miito ya LLM → …" unaweza kutoa matokeo ya hali ya juu na yaliyojengwa vizuri.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.sw.png)

## Kumiliki Mchakato wa Uamuzi

Sifa ya kipekee inayofanya mfumo kuwa "agentic" ni uwezo wake wa kumiliki mchakato wake wa kufikiri. Utekelezaji wa kawaida wa RAG mara nyingi hutegemea binadamu kuweka njia kwa mfano: mlolongo wa mawazo unaoeleza nini cha kuchota na lini. Lakini mfumo unapokuwa kweli agentic, huamua ndani jinsi ya kushughulikia tatizo. Hauendeshi tu script; unajiamulia mlolongo wa hatua kulingana na ubora wa taarifa inayopatikana. Kwa mfano, ikiwa umeulizwa kuunda mkakati wa uzinduzi wa bidhaa, hautegemei tu maelekezo yanayoeleza mtiririko mzima wa utafiti na maamuzi. Badala yake, mfano wa agentic huamua kwa uhuru:

1. Kuchota ripoti za mwenendo wa soko za sasa kwa kutumia Bing Web Grounding.
2. Kutambua data husika ya washindani kwa kutumia Azure AI Search.
3. Kuhusisha vipimo vya mauzo vya kihistoria vya ndani kwa kutumia Azure SQL Database.
4. Kuunganisha matokeo kuwa mkakati wa pamoja unaoratibiwa kupitia Azure OpenAI Service.
5. Kutathmini mkakati kwa mapungufu au kutokuwepo kwa usawa, na kuanzisha mzunguko mwingine wa uchotaji inapohitajika.

Hatua hizi zote—kurekebisha maswali, kuchagua vyanzo, kurudia hadi "kuridhika" na jibu—zinaamuliwa na mfano, si kuandikwa awali na binadamu.

## Mizunguko ya Iterative, Ujumuishaji wa Zana, na Kumbukumbu

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.sw.png)

Mfumo wa agentic hutegemea muundo wa mwingiliano wa mzunguko:

- **Mwito wa Awali:** Lengo la mtumiaji (yaani, maelekezo ya mtumiaji) huwasilishwa kwa LLM.
- **Matumizi ya Zana:** Ikiwa mfano unagundua taarifa inayokosekana au maelekezo yasiyoeleweka, huchagua zana au mbinu ya uchotaji—kama utafutaji wa hifadhidata ya vector (mfano Azure AI Search Hybrid search juu ya data ya kibinafsi) au mwito wa SQL uliopangwa—kukusanya muktadha zaidi.
- **Tathmini na Marekebisho:** Baada ya kupitia data iliyorejeshwa, mfano huamua kama taarifa inatosha. Ikiwa sivyo, hurekebisha swali, kujaribu zana tofauti, au kurekebisha mbinu yake.
- **Rudia Hadi Kuridhika:** Mzunguko huu huendelea hadi mfano uamue kuwa una uwazi wa kutosha na ushahidi wa kutoa jibu la mwisho lililo na mantiki.
- **Kumbukumbu na Hali:** Kwa sababu mfumo unadumisha hali na kumbukumbu katika hatua, unaweza kukumbuka majaribio ya awali na matokeo yake, kuepuka mizunguko ya kurudia na kufanya maamuzi sahihi zaidi kadri unavyoendelea.

Kwa muda, hii huunda hisia ya uelewa unaoendelea, kuwezesha mfano kushughulikia kazi ngumu, za hatua nyingi bila hitaji la binadamu kuingilia mara kwa mara au kuunda upya maelekezo.

## Kushughulikia Njia za Kushindwa na Kujirekebisha

Uhuru wa Agentic RAG pia unahusisha mifumo thabiti ya kujirekebisha. Wakati mfumo unakutana na vikwazo—kama kuchota nyaraka zisizohusiana au kukutana na maswali yaliyokosewa—unaweza:

- **Kurudia na Kuuliza Tena:** Badala ya kutoa majibu ya thamani ya chini, mfano hujaribu mbinu mpya za utafutaji, kuandika upya maswali ya hifadhidata, au kuangalia seti za data mbadala.
- **Kutumia Zana za Uchunguzi:** Mfumo unaweza kutumia kazi za ziada zilizoundwa kusaidia kuangalia hatua zake za kufikiri au kuthibitisha usahihi wa data iliyochotwa. Zana kama Azure AI Tracing zitakuwa muhimu kuwezesha ufuatiliaji thabiti.
- **Kutegemea Usimamizi wa Binadamu:** Kwa hali za hatari kubwa au zinazoshindwa mara kwa mara, mfano unaweza kuashiria kutokuwa na uhakika na kuomba mwongozo wa binadamu. Mara binadamu anapotoa maoni ya kurekebisha, mfano unaweza kujumuisha somo hilo kwa siku zijazo.

Mbinu hii ya kurudia na yenye nguvu inaruhusu mfano kuboresha kila mara, kuhakikisha kuwa si mfumo wa "jaribio moja" bali ni mfumo unaojifunza kutokana na makosa yake wakati wa kikao fulani.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.sw.png)

## Mipaka ya Uwezo wa Kujitegemea

Licha ya uhuru wake ndani ya kazi, Agentic RAG si sawa na Akili ya Kijumla ya Kifaa. Uwezo wake wa "agentic" unafungika kwa zana, vyanzo vya data, na sera zinazotolewa na watengenezaji wa binadamu. Haiwezi kuunda zana zake au kuvuka mipaka ya kikoa iliyowekwa. Badala yake, inang'aa katika kuratibu kwa nguvu rasilimali zilizopo.

Tofauti kuu na aina za AI zilizoendelea zaidi ni:

1. **Uhuru Maalum wa Kikoa:** Mifumo ya Agentic RAG inalenga kufanikisha malengo yaliyofafanuliwa na mtumiaji ndani ya kikoa kinachojulikana, ikitumia mikakati kama kuandika upya maswali au kuchagua zana kuboresha matokeo.
2. **Utegemezi wa Miundombinu:** Uwezo wa mfumo hutegemea zana na data zilizojumuishwa na watengenezaji. Haiwezi kuvuka mipaka hii bila kuingilia binadamu.
3. **Kuheshimu Vizuizi:** Miongozo ya kimaadili, sheria za kufuata, na sera za biashara zinabaki kuwa muhimu sana. Uhuru wa mfumo daima unafungika na hatua za usalama na mifumo ya usimamizi (labda?).

## Matumizi ya Kivitendo na Thamani

Agentic RAG inang'aa katika hali zinazohitaji marekebisho ya mara kwa mara na usahihi:

1. **Mazingira Yanayozingatia Usahihi:** Katika ukaguzi wa kufuata, uchambuzi wa kanuni, au utafiti wa kisheria, mfano wa agentic unaweza kuthibitisha ukweli mara kwa mara, kushauriana na vyanzo vingi, na kuandika upya maswali hadi kutoa jibu lililokaguliwa kikamilifu.
2. **Mwingiliano Tata wa Hifadhidata:** Wakati wa kushughulikia data iliyojengwa ambapo maswali yanaweza mara nyingi kushindwa au kuhitaji marekebisho, mfumo unaweza kurekebisha maswali yake kwa uhuru kwa kutumia Azure SQL au Microsoft Fabric OneLake, kuhakikisha uchotaji wa mwisho unalingana na nia ya mtumiaji.
3. **Mtiririko wa Kazi wa Muda Mrefu:** Vikao vya muda mrefu vinaweza kubadilika kadri taarifa mpya zinavyopatikana. Agentic RAG inaweza kuendelea kujumuisha data mpya, kubadilisha mikakati kadri inavyojifunza zaidi kuhusu eneo la tatizo.

## Usimamizi, Uwazi, na Uaminifu

Kadri mifumo hii inavyokuwa huru zaidi katika kufikiri kwake, usimamizi na uwazi ni muhimu:

- **Kufikiri kwa Kueleweka:** Mfano unaweza kutoa rekodi ya maswali uliyouliza, vyanzo ulivyoshauriana, na hatua za kufikiri ulizochukua kufikia hitimisho lake. Zana kama Azure AI Content Safety na Azure AI Tracing / GenAIOps zinaweza kusaidia kudumisha uwazi na kupunguza hatari.
- **Udhibiti wa Upendeleo na Uchotaji wa Usawa:** Watengenezaji wanaweza kurekebisha mikakati ya uchotaji ili kuhakikisha vyanzo vya data vilivyowakilishwa kwa usawa vinazingatiwa, na kukagua matokeo mara kwa mara ili kugundua upendeleo au mifumo iliyopotoshwa kwa kutumia mifano maalum kwa mashirika ya hali ya juu ya sayansi ya data yanayotumia Azure Machine Learning.
- **Usimamizi wa Binadamu na Ufuataji:** Kwa kazi nyeti, ukaguzi wa binadamu unabaki kuwa muhimu. Agentic RAG haibadilishi uamuzi wa binadamu katika maamuzi ya hatari kubwa—inaongeza kwa kutoa chaguo zilizokaguliwa zaidi.

Kuwa na zana zinazotoa rekodi wazi ya hatua ni muhimu. Bila zana hizo, kurekebisha mchakato wa hatua nyingi inaweza kuwa ngumu sana. Tazama mfano ufuatao kutoka Literal AI (kampuni nyuma ya Chainlit) kwa mwendo wa wakala:

![AgentRunExample](../../../translated_images/AgentRunExample.471a94bc40cbdc0cd04c1f43c8d8c9b751f10d97918c900e29cb3ba0d6aa4c00.sw.png)

## Hitimisho

Agentic RAG inawakilisha mageuzi ya asili katika jinsi mifumo ya AI inavyoshughulikia kazi ngumu, zinazohitaji data nyingi. Kwa kupitisha muundo wa mwingiliano wa mzunguko, kuchagua zana kwa uhuru, na kurekebisha maswali hadi kufikia matokeo ya hali ya juu, mfumo unazidi mifumo ya kawaida ya kufuata maelekezo na kuwa mtoaji wa maamuzi unaojitegemea zaidi na unaojali muktadha. Ingawa bado umefungwa na miundombinu iliyofafanuliwa na binadamu na miongozo ya kimaadili, uwezo huu wa agentic unaruhusu mwingiliano tajiri zaidi, wa nguvu zaidi, na hatimaye wa manufaa zaidi wa AI kwa mashirika na watumiaji wa mwisho.

### Una Maswali Zaidi Kuhusu Agentic RAG?

Jiunge na [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ili kukutana na wanafunzi wengine, kuhudhuria masaa ya ofisi, na kupata majibu ya maswali yako kuhusu AI Agents.

## Rasilimali za Z
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Tekeleza Retrieval Augmented Generation (RAG) na Huduma ya Azure OpenAI: Jifunze jinsi ya kutumia data yako mwenyewe na Huduma ya Azure OpenAI. Moduli hii ya Microsoft Learn inatoa mwongozo wa kina juu ya kutekeleza RAG  
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Tathmini ya matumizi ya AI ya kizazi na Azure AI Foundry: Makala hii inashughulikia tathmini na kulinganisha mifano kwenye seti za data zinazopatikana hadharani, ikijumuisha matumizi ya Agentic AI na miundo ya RAG</a>  
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Agentic RAG ni nini | Weaviate</a>  
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Mwongozo Kamili wa Retrieval Augmented Generation inayotegemea mawakala – Habari kutoka kizazi cha RAG</a>  
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: ongeza kasi ya RAG yako kwa uundaji upya wa maswali na kujijibu! Hugging Face Open-Source AI Cookbook</a>  
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Kuongeza Tabaka za Agentic kwenye RAG</a>  
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Mustakabali wa Wasaidizi wa Maarifa: Jerry Liu</a>  
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Jinsi ya Kujenga Mifumo ya Agentic RAG</a>  
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Kutumia Huduma ya Mawakala ya Azure AI Foundry kuongeza kiwango cha mawakala wako wa AI</a>  

### Karatasi za Kitaaluma  

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Marekebisho ya Mara kwa Mara kwa Kujipatia Maoni</a>  
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Mawakala wa Lugha na Kujifunza kwa Kuimarisha kwa Maneno</a>  
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Mifano Mikubwa ya Lugha Inaweza Kujirekebisha kwa Kukosoa kwa Kuingiliana na Zana</a>  
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Utafiti juu ya Agentic RAG</a>  

## Somo la Awali  

[Muundo wa Matumizi ya Zana](../04-tool-use/README.md)  

## Somo Linalofuata  

[Kujenga Mawakala wa AI Wenye Kuaminika](../06-building-trustworthy-agents/README.md)  

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.