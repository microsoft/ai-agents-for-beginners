[![Intro to AI Agents](../../../translated_images/sw/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Bofya picha hapo juu kutazama video ya somo hili)_

# Utangulizi wa Wakala wa AI na Matumizi ya Wakala

Karibu kwenye kozi ya **Wakala wa AI kwa Waanzilishi**! Kozi hii inakupatia maarifa ya msingi — na msimbo halisi unaofanya kazi — kuanza kujenga Wakala wa AI kutoka mwanzo.

Njoo tuseme habari katika <a href="https://discord.gg/kzRShWzttr" target="_blank">Jumuiya ya Azure AI Discord</a> — imejaa wanafunzi na wajenzi wa AI ambao wako tayari kujibu maswali.

Kabla hatujaanza kujenga, hebu tukague tu kama tunaelewa kweli ni nini Wakala wa AI *ni* na ni lini inafaa kutumia moja.

---

## Utangulizi

Somo hili linajumuisha:

- Wakala wa AI ni nini, na aina tofauti zinazopo
- Aina gani za kazi ambayo Wakala wa AI ni bora kwa ajili yake
- Vitu vikuu vya msingi utakavyotumia unapobuni suluhisho la Ajaniki

## Malengo ya Kujifunza

Mwisho wa somo hili, unapaswa kuwa na uwezo wa:

- Eleza ni nini Wakala wa AI na jinsi inavyotofautiana na suluhisho la kawaida la AI
- Kujua lini unapaswa kutumia Wakala wa AI (na lini usitumie)
- Kuchora mchoro wa msingi wa kubuni suluhisho la ajaniki kwa tatizo halisi la dunia

---

## Kufafanua Wakala wa AI na Aina za Wakala wa AI

### Wakala wa AI ni Nini?

Hapa kuna njia rahisi ya kuifikiria:

> **Wakala wa AI ni mifumo inayowezesha Mifano Mikubwa ya Lugha (LLMs) kufanya *mambo* — kwa kuwapa zana na maarifa ya kuchukua hatua katika dunia, sio tu kujibu maagizo.**

Hebu tufafanue kidogo:

- **Mfumo** — Wakala wa AI sio kitu kimoja tu. Ni mkusanyiko wa sehemu zinazofanya kazi pamoja. Msingi wake, kila wakala ana vipande vitatu:
  - **Mazingira** — Eneo ambalo wakala anafanya kazi ndani yake. Kwa wakala wa kuhifadhi tiketi za usafiri, hii itakuwa jukwaa la kuhifadhi tiketi lenyewe.
  - **Vipimo** — Jinsi wakala anavyosoma hali ya sasa ya mazingira yake. Wakala wetu wa usafiri anaweza kuangalia upatikanaji wa hoteli au bei za ndege.
  - **Vitendo** — Jinsi wakala anavyochukua hatua. Wakala wa usafiri anaweza kuhifadhi chumba, kutuma uthibitisho, au kughairi uhifadhi.

![What Are AI Agents?](../../../translated_images/sw/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Mifano Mikubwa ya Lugha** — Wakala walikuwepo kabla ya LLMs, lakini LLMs ndio yanayowafanya wakala wa kisasa kuwa wenye nguvu sana. Wanaweza kuelewa lugha ya kawaida, kufikiri kuhusu muktadha, na kubadilisha ombi la mtumiaji kuwa mpango halisi wa hatua.

- **Kuchukua Hatua** — Bila mfumo wa wakala, LLM inazalisha maandishi tu. Ndani ya mfumo wa wakala, LLM inaweza *kutekeleza* hatua — kutafuta kwenye hifadhidata, kuita API, kutuma ujumbe.

- **Kupata Zana** — Ni zana gani wakala anaweza kutumia hutegemea (1) mazingira anayotumia na (2) kile mtengenezaji ameamua kumpa. Wakala wa usafiri anaweza kutafuta ndege lakini asibadilishe rekodi za wateja — yote ni kuhusu unachounganisha.

- **Kumbukumbu + Maarifa** — Wakala anaweza kuwa na kumbukumbu ya muda mfupi (mazungumzo ya sasa) na kumbukumbu ya muda mrefu (hifadhidata ya wateja, maingiliano ya zamani). Wakala wa usafiri anaweza "kumbuka" kuwa unapendelea viti vya madirisha.

---

### Aina Tofauti za Wakala wa AI

Si wakala wote wamejengwa kwa njia moja. Hapa kuna muhtasari wa aina kuu, tukitumia wakala wa kuhifadhi tiketi za usafiri kama mfano:

| **Aina ya Wakala** | **Kinachofanya** | **Mfano wa Wakala wa Usafiri** |
|---|---|---|
| **Wakala wa Reflɛksi Rahisi** | Hufuata sheria zilizoandikwa — haina kumbukumbu, haina kupanga. | Anaona barua ya malalamiko → anaipeleka huduma kwa wateja. Hilo tu. |
| **Wakala wa Reflɛksi Anayetumia Mfano** | Huweka mfano wa ndani wa dunia na kuuboresha inapobadilika. | Hufuata bei za ndege za zamani na kuangazia njia ambazo ghafla ni ghali. |
| **Wakala wa Kulingana na Lengo** | Ana lengo akilini na huamua hatua kwa hatua jinsi la kufikia. | Huongeza safari kamili (ndege, gari, hoteli) kuanzia mahali ulipo kufikia marudio yako. |
| **Wakala wa Kulingana na Faida** | Hairudzi tu suluhisho *moja* — inatafuta *bora* kwa kuzingatia ushindani. | Huamua kati ya gharama dhidi ya urahisi kupata safari inayokidhi vipaumbele vyako. |
| **Wakala wa Kujifunza** | Huimarika kwa muda kwa kujifunza kutoka kwa maoni. | Hurekebisha mapendekezo ya uhifadhi wa baadaye kulingana na matokeo ya utafiti wa baada ya safari. |
| **Wakala wa Kielea juu (Hierarchical)** | Wakala wa ngazi ya juu hugawanya kazi ndani ya kazi ndogo na kupeana kwa wakala wa ngazi ya chini. | Omdhani "ghairi safari" unagawanywa: ghairi ndege, ghairi hoteli, ghairi kukodisha gari — kila moja inashughulikiwa na sub-wakala. |
| **Mifumo ya Wakala wa Nyingi (MAS)** | Wakala wengi hufanya kazi pamoja (au kushindana). | Ushirikiano: wakala tofauti hushughulikia hoteli, ndege na burudani. Ushindani: wakala wengi wanasaka kujaa vyumba vya hoteli kwa bei nzuri zaidi. |

---

## Lini Kutumia Wakala wa AI

Kuwa na uwezo wa kutumia Wakala wa AI haimaanishi kila mara unapaswa. Hapa ni hali ambapo wakala wanafaa kweli:

![When to use AI Agents?](../../../translated_images/sw/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Matatizo Yasiyo na Mwisho Wazi** — Wakati hauwezi kupanga mwendo wa hatua za kutatua tatizo mapema. Unahitaji LLM kugundua njia kwa nguvu ya hali halisi.
- **Mchakato wa Hatua Nyingi** — Kazi zinazohitaji kutumia zana kwa mizunguko mingi, si kujitolea au kutafuta mara moja tu.
- **Kuboresha Kwa Muda** — Unapotaka mfumo uwe na akili zaidi kwa msingi wa maoni ya mtumiaji au ishara za mazingira.

Tutaelezea zaidi lini (na lini *sio*) kutumia Wakala wa AI katika somo la **Kujenga Wakala wa AI wa Kuaminika** baadaye katika kozi.

---

## Misingi ya Suluhisho la Ajaniki

### Maendeleo ya Wakala

Kitu cha kwanza unachofanya unapoanza kujenga wakala ni kufafanua *anachoweza kufanya* — zana zake, vitendo, na tabia zake.

Katika kozi hii, tunatumia **Huduma ya Wakala wa Azure AI** kama jukwaa letu kuu. Inaunga mkono:

- Mifano wazi kama OpenAI, Mistral, na Llama
- Data yenye leseni kutoka kwa watoa kama Tripadvisor
- Maelezo ya zana ya OpenAPI 3.0 yaliyosanifishwa

### Mifumo ya Ajaniki

Unawasiliana na LLM kupitia maagizo. Kwa wakala, huwezi kila mara kuandaa maagizo yote kwa mkono — wakala anahitaji kuchukua hatua katika hatua nyingi. Hapo ndipo **Mifumo ya Ajaniki** inakuja. Ni mikakati inayoweza kutumika tena ya kutoa maagizo na kupanga LLM kwa njia inayoweza kupanuliwa na ya kuaminika zaidi.

Kozi hii imejengwa kando ya mifumo ya ajaniki ya kawaida na yenye manufaa.

### Mifumo ya Agentic

Mifumo ya Agentic huwapa watengenezaji templati tayari, zana, na miundombinu ya kujenga wakala. Zinawasaidia kufanya urahisi:

- Kuweka pamoja zana na uwezo
- Kuangalia anachofanya wakala (na kufuatilia dosari inapokosea)
- Kushirikiana kati ya wakala wengi

Katika kozi hii, tunazingatia **Mfumo wa Wakala wa Microsoft (MAF)** kwa ajili ya kujenga wakala tayari kwa uzalishaji.

---

## Sampuli za Msimbo

Uko tayari kuona inavyofanya kazi? Hapa kuna sampuli za msimbo za somo hili:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Una Maswali?

Jiunge na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) kuungana na wanafunzi wengine, hudhuria saa za ofisi, na pokea majibu kwa maswali yako ya Wakala wa AI kutoka kwa jumuiya.

---

## Somo Lililopita

[Course Setup](../00-course-setup/README.md)

## Somo Linalofuata

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tangazo la Kuondoa Uwajibikaji**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Wakati tunajitahidi kuwa sahihi, tafadhali fahamu kuwa tafsiri za moja kwa moja zinaweza kuwa na makosa au taarifa zisizo sahihi. Hati asilia katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa habari muhimu, tafsiri ya mtaalamu wa binadamu inashauriwa. Hatubebei dhima kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->