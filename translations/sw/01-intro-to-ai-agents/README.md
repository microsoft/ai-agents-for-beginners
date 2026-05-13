[![Intro to AI Agents](../../../translated_images/sw/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Bonyeza picha hapo juu kutazama video ya somo hili)_

# Utangulizi wa Wakala wa AI na Matumizi ya Wakala

Karibu kwenye kozi ya **Wakala wa AI kwa Komo Msumari**! Kozi hii inakupa maarifa ya msingi — na msimbo wa kazi halisi — kuanza kujenga Wakala wa AI kutoka mwanzo.

Njooni kusema hii katika <a href="https://discord.gg/kzRShWzttr" target="_blank">Jumuiya ya Azure AI Discord</a> — imejaa wanafunzi na wajenzi wa AI ambao wana furaha kujibu maswali.

Kabla hatujaanza kujenga, hebu tuhakikishe kwamba tunafahamu kabisa ni nini Wakala wa AI *ni* na lini inafaa kutumia mmoja.

---

## Utangulizi

Somo hili linahusu:

- Wakala wa AI ni nini, na aina tofauti zinazopo
- Aina gani za kazi Wakala wa AI wanafaa zaidi kwao
- Misingi ya msingi utakayotumia wakati wa kubuni suluhisho la Agentic

## Malengo ya Kujifunza

Mwisho wa somo hili, unapaswa kuwa na uwezo wa:

- Eleza ni nini Wakala wa AI ni na jinsi inavyotofautiana na suluhisho la kawaida la AI
- Jua lini kufikia Wakala wa AI (na lini usifanye hivyo)
- Chora muundo wa msingi wa suluhisho la Agentic kwa tatizo halisi la dunia

---

## Kufafanua Wakala wa AI na Aina za Wakala wa AI

### Wakala wa AI ni Nini?

Hii ni njia rahisi ya kufikiri kuhusu hilo:

> **Wakala wa AI ni mifumo inayowezesha Miundo Mikubwa ya Lugha (LLMs) *kufanya mambo* — kwa kuwapa zana na maarifa ya kuchukua hatua duniani, siyo tu kujibu maelekezo.**

Hebu tuchambue kidogo:

- **Mfumo** — Wakala wa AI si kitu kimoja tu. Ni mkusanyiko wa sehemu zinazofanya kazi pamoja. Kimsingi, kila wakala ana vipande vitatu:
  - **Mazingira** — Eneo ambalo wakala anafanya kazi ndani yake. Kwa wakala wa kuhudumia usafiri, hili lingekuwa jukwaa la uhifadhi tiketi.
  - **Sensor** — Jinsi wakala anavyosoma hali ya mazingira sasa. Wakala wetu wa usafiri anaweza kuchunguza upatikanaji wa hoteli au bei za ndege.
  - **Kifaa cha Kuchukua Hatua** — Jinsi wakala anavyotenda. Wakala wa usafiri anaweza kuhifadhi chumba, kutuma uthibitisho, au kufuta uhifadhi.

![What Are AI Agents?](../../../translated_images/sw/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Miundo Mikubwa ya Lugha** — Wakala walikuwepo kabla ya LLMs, lakini LLMs ndizo zinazofanya wakala wa kisasa kuwa wenye nguvu sana. Wanaweza kuelewa lugha ya asili, kutafakari muktadha, na kugeuza ombi batili la mtumiaji kuwa mpango wa kina wa hatua.

- **Kuchukua Hatua** — Bila mfumo wa wakala, LLM hutoa maandishi tu. Ndani ya mfumo wa wakala, LLM inaweza *kufanikisha* hatua — kutafuta kwenye hifadhi ya data, kuwaita API, kutuma ujumbe.

- **Upatikanaji wa Zana** — Zana ambazo wakala anaweza kutumia zinategemea (1) mazingira ambayo anaendesha ndani yake na (2) kile mtengenezaji alichoamua kumpa. Wakala wa usafiri anaweza kuweza kutafuta ndege lakini asiweze kuhariri rekodi za wateja — yote ni kuhusu unavyounganisha.

- **Kumbukumbu + Maarifa** — Wakala wanaweza kuwa na kumbukumbu ya muda mfupi (mazungumzo ya sasa) na kumbukumbu ya muda mrefu (hifadhi ya wateja, mabadilishano ya zamani). Wakala wa usafiri anaweza "kukumbuka" kuwa unapendelea viti karibu na dirisha.

---

### Aina Tofauti za Wakala wa AI

Sio wakala wote wamejengwa sawa. Hapa kuna muhtasari wa aina kuu, ukitumia mfano wa wakala wa kuhudumia usafiri kama mfano unaoendelea:

| **Aina ya Wakala** | **Kinachofanya** | **Mfano wa Wakala wa Usafiri** |
|---|---|---|
| **Wakala wa Mwito wa Moja kwa Moja Rahisi** | Hufuata sheria zilizowekwa ngumu — haina kumbukumbu, haina mipango. | Anaona barua ya malalamiko → anaituma kwa huduma kwa wateja. Hiyo tu. |
| **Wakala wa Mwito wa Moja kwa Moja unaotegemea Mfano** | Hushikilia mfano wa ndani wa dunia na kuuboresha inavyo badilika mambo. | Anafuatilia bei za ndege za zamani na kuangazia njia zinazogharimu ghafi ghafi. |
| **Wakala wa Kulingana na Malengo** | Ana lengo akilini na hupanga hatua moja baada ya nyingine kufikia lengo hilo. | Anaandaa safari kamili (ndege, gari, hoteli) kuanzia mahali ulipo sasa hadi unakotaka kwenda. |
| **Wakala wa Kulingana na Taarifa za Faida** | Asiangalii suluhisho *moja* tu — anatafuta suluhisho *bora* kwa kuzingatia mambo yanayobadilishana. | Analinganisha gharama dhidi ya urahisi kupata safari inayokufaa zaidi. |
| **Wakala wa Kujifunza** | Huboresha utendaji kwa muda kwa kujifunza kutokana na mrejesho. | Hubadilisha mapendekezo ya uhifadhi wa baadaye kulingana na matokeo kutoka kwa tafiti baada ya safari. |
| **Wakala wa Kihiari** | Wakala wa ngazi ya juu hugawanya kazi kuwa vitakamilifu vidogo na kuzipa wakala wa ngazi ya chini. | Ombi la "kufuta safari" hugawanywa: futa ndege, futa hoteli, futa ukodishaji gari — kila moja linaendeshwa na wakala mdogo. |
| **Mifumo ya Wakala Wengi (MAS)** | Wakala wengi hufanya kazi kwa ushirikiano (au ushindani). | Ushirikiano: wakala tofauti hushughulikia hoteli, ndege, na burudani. Ushindani: wakala wengi hushindana kujaza vyumba vya hoteli kwa bei bora zaidi. |

---

## Lini Kutumia Wakala wa AI

Kwa kuwa unaweza kutumia Wakala wa AI husababisha si kwamba kila wakati unapaswa kufanya hivyo. Hapa ni hali ambapo wakala huonyesha upekee wao:

![When to use AI Agents?](../../../translated_images/sw/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Matatizo Yasiyo na Mwisho Kamili** — Wakati hatua za kutatua tatizo haziwezi kupangwa kabla. Unahitaji LLM kugundua njia kwa nguvu ya hali halisi.
- **Mchakato wa Hatua Nyingi** — Kazi zinazohitaji matumizi ya zana kupitia mizunguko mingi, siyo kutafuta au kuzalisha mara moja tu.
- **Kuboresha kwa Muda** — Wakati unataka mfumo kuwa akili zaidi kulingana na mrejesho wa mtumiaji au ishara za mazingira.

Tutazama kwa kina zaidi lini (na lini *si*) kutumia Wakala wa AI katika somo la **Kujenga Wakala wa AI Wanaoaminika** baadaye kwenye kozi.

---

## Misingi ya Suluhisho la Agentic

### Maendeleo ya Wakala

Jambo la kwanza unalofanya wakati wa kujenga wakala ni kufafanua *anachoweza kufanya* — zana zake, vitendo, na tabia zake.

Katika kozi hii, tunatumia **Huduma ya Wakala wa AI ya Azure** kama jukwaa letu kuu. Inasaidia:

- Miundo kutoka kwa wasambazaji kama OpenAI, Mistral, na Meta (Llama)
- Data iliyo na leseni kutoka kwa wasambazaji kama Tripadvisor
- Ufafanuzi wa zana uliopangwa wa OpenAPI 3.0

### Mifumo ya Agentic

Unawasiliana na LLM kupitia maelekezo. Kwa wakala, huwezi kila wakati kuunda maelekezo kwa mkono — wakala anahitaji kuchukua hatua katika hatua nyingi. Hapa ndipo **Mifumo ya Agentic** inapotumika. Ni mbinu zinazoweza kutumika tena kwa kuongoza na kupangilia LLM kwa njia inayoweza kupanuka na kuaminika zaidi.

Kozi hii imejengwa kwa kuzingatia mifumo maarufu na muhimu zaidi ya agentic.

### Mipangilio ya Agentic

Mipangilio ya Agentic huwapa waandaaji templeti, zana, na miundombinu tayari kwa kujenga wakala. Hufanya iwe rahisi:

- Kuunganisha zana na uwezo
- Kutazama kile wakala anachofanya (na kutatua tatizo linapotokea)
- Kushirikiana kati ya wakala wengi

Katika kozi hii, tunazingatia **Microsoft Agent Framework (MAF)** kwa ajili ya kujenga wakala wanaoweza kutumika kwenye uzalishaji.

---

## Mifano ya Msimbo

Tayari kuona inavyofanya kazi? Hapa ni mifano ya msimbo kwa somo hili:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Una Maswali?

Jiunge na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) kuungana na wanafunzi wengine, kuhudhuria masaa ya ofisi, na kupata majibu ya maswali yako kuhusu Wakala wa AI kutoka jumuiya.

---

## Somo lililopita

[Course Setup](../00-course-setup/README.md)

## Somo lijalo

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->