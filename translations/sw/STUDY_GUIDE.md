# Mawakala ya AI kwa Wakianza - Mwongozo wa Kujifunza

Tumia mwongozo huu kama rafiki wa vitendo unapopita katika kozi. Sio
kubadilisha masomo. Husaidia kuamua wapi pa kuanza, kile cha
kutafuta katika kila somo, na jinsi ya kuunganisha mawazo kuwa maonyesho madogo
ya wakala anayefanya kazi.

Ikiwa hii ni mara yako ya kwanza hapa, anza kwa vitu rahisi:

1. Soma [Kuandaa Kozi](./00-course-setup/README.md).
2. Kamilisha Masomo 01-06 kwa mpangilio.
3. Weka wazo moja dogo la maonyesho akilini unavyojifunza.
4. Baada ya kila somo, jiulize: "Wakala wangu sasa anaweza nini ambacho hakuweza
   kufanya kabla?"

## Maonyesho Rahisi ya Kuweka Akilini

Njia nzuri ya kujifunza mawakala ni kufuata wazo moja la maonyesho kupitia kozi.

Mfano wa maonyesho: **wakala msaidizi wa kozi**.

Mtumiaji huuliza:

> "Nataka kujifunza jinsi mawakala wanavyotumia zana. Tafuta masomo sahihi, fupisha
> kile ninachopaswa kusoma kwanza, na nipe zoezi fupi la mazoezi."

Chatbot wa kawaida anaweza kujibu kutokana na kile anachokijua tayari. Wakala anaweza zaidi:

1. **Soma au tafuta faili za kozi** kutafuta masomo sahihi.
2. **Tumia zana** kupata viungo vya masomo, mifano, au nyenzo za msaada.
3. **Panga** njia fupi ya kujifunza badala ya kutoa jibu moja refu.
4. **Tumia muktadha** kutoka kwa mazungumzo ya sasa ili kubaki umakini kwa lengo la mwanafunzi.

5. **Kumbuka mapendeleo muhimu** ikiwa programu inaunga mkono kumbukumbu.
6. **Onyesha nyaraka, marejeo, au rekodi** ili mtumiaji afahamu kilichotokea.
7. **Tumia mipaka ya usalama** kabla ya kuchukua hatua zenye hatari au kutumia data nyeti.

Unajifunza kila somo, rudi kwenye maonyesho haya na jiulize: ni uwezo gani mpya
somo hili lingeongeza?

## Unachojenga

Mwishoni mwa kozi, unapaswa kueleza na kujenga mifumo ya wakala
inayochanganya sehemu hizi:

| Sehemu | Maana kwa lugha rahisi | Katika maonyesho |
|------|------------------------|-------------|
| Mfano | Mashine ya kufikiri inayatafsiri ombi la mtumiaji | Anaelewa kuwa mwanafunzi anataka masomo kuhusu kutumia zana |
| Zana | Kazi, APIs, faili, vivinjari, au huduma wakala anaweza kutumia | Anatafuta katika hazina au kupata maudhui ya somo |
| Maarifa | Nyaraka au data zinazotumika kuimarisha jibu | Faili za README za kozi na nyenzo za somo |
| Muktadha | Taarifa zilizojumuishwa katika simu inayofuata ya mfano | Lengo la mtumiaji na matokeo ya zana |
| Kumbukumbu | Taarifa iliyohifadhiwa kwa matumizi ya baadaye | Mwanafunzi anapendelea mifano ya kiutendaji ya Python |
| Mipango | Kuvunja lengo kubwa kuwa hatua ndogo ndogo | Tafuta masomo, fupisha, pendekeza mazoezi |
| Usanifu | Kusambaza kazi kati ya zana, hatua, au mawakala | Mpenda mipango huwaita zana za utafutaji, kisha mfupishaji |
| Uaminifu | Usalama, usalama, tathmini, na ufuatilizi | Rekodi simu za zana na huuliza kabla ya hatua zenye athari kubwa |

## Mifano na Watoa Huduma

Sampuli za msimbo wa kozi hutumia **Microsoft Agent Framework (MAF)** na lengwa


Unapopita kupitia masomo, una chaguzi kadhaa za watoa huduma:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — njia kuu inayotumika katika masomo yote. Ingia kwa `az login` kwa uthibitishaji wa Entra ID bila funguo.
- **Foundry Local** — endesha mifano kikamilifu kifaa kwa njia ya API inayolingana na OpenAI (hakuna wingu, hakuna funguo za API). Inafaa kwa majaribio ya offline au yasiyo na gharama. Tazama [Course Setup](./00-course-setup/README.md).
- **MiniMax** — mtoa huduma anayolingana na OpenAI akiwa na mifano ya muktadha mkubwa, inayoweza kutumika kama mbadala wa kubadilisha.

> **Kumbuka:** GitHub Models imesitishwa (itaondolewa Julai 2026) na hailingani na Responses API. Sampuli zimebadilishwa kutumia Azure OpenAI / Microsoft Foundry badala yake.

## Chagua Njia Yako ya Kujifunza

Unaweza kuchukua kozi nzima kwa mpangilio, au ruka kwenye njia kulingana na kile unachotaka
kujenga.

| Ikiwa lengo lako ni... | Anza na | Kisha soma |
|-----------------------|------------|------------|
| Kuelewa ni nini maajenti | 01, 02, 03 | 04, 05, 06 |
| Kujenga maajenti yanayotumia zana | 04 | 05, 07, 14 |
| Kujenga maajenti wa RAG | 05 | 04, 06, 12 |
| Kubuni mchakato wa hatua nyingi | 07 | 08, 09, 14 |
| Kuelewa mifumo ya maajenti wengi | 08 | 07, 09, 11 |
| Kuandaa maajenti kwa uzalishaji | 06, 10 | 12, 13, 16, 18 |
| Kuweka na kupanua maajenti kwenye Foundry | 10, 16 | 06, 13, 18 |
| Kujenga maajenti wa ndani / wa kwanza offline | 17 | 04, 05, 11 |
| Kuchunguza protokoli na kuendesha kivinjari kwa automatisering | 11, 15 | 10, 18 |

Vidokezo: ikiwa wewe ni mpya kwa maajenti, usiruke Masomo 01-06. Yanakupa
msamiati utakao hitajika kwa kozi yote.

## Mwongozo wa Kila Somo  

| Somo | Unajifunza Nini | Jaribu baada ya somo |
|--------|----------------|---------------------------|
| [01 - Utangulizi wa Maajenti wa AI](./01-intro-to-ai-agents/README.md) | Nini kinachofanya maajenti kutofautiana na chatbot ya kawaida. | Elezea wazo lako la maonyesho kama maajenti, sio tu programu ya mazungumzo. |
| [02 - Mifumo ya Agentic](./02-explore-agentic-frameworks/README.md) | Jinsi mifumo inavyosaidia na mifano, zana, hali, na michakato. | Tambua sehemu gani za maonyesho yako ambazo mfumo ungeendesha. |
| [03 - Mifano ya Muundo wa Agentic](./03-agentic-design-patterns/README.md) | Mifano ya kawaida ya kubuni tabia ya maajenti. | Tekeleza safari ya mtumiaji kabla ya kuandika nambari. |
| [04 - Matumizi ya Zana](./04-tool-use/README.md) | Jinsi maajenti wanavyopiga zana kupata data au kuchukua hatua. | Tambua zana moja ambayo maajenti wako wa maonyesho wangahitaji. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Jinsi utafutaji unavyosababisha majibu ya maajenti kuwa na msingi katika nyaraka au data. | Amua chanzo cha maarifa ambacho maonyesho yako yanapaswa kutafuta. |

| [06 - Wakala Wanaoweza Kuaminika](./06-building-trustworthy-agents/README.md) | Jinsi ya kuongeza vizuizi, uangalizi, na tabia salama zaidi. | Ongeza sheria moja ya wakati wakala anapaswa kumuuliza mtumiaji kwanza. |
| [07 - Ubunifu wa Mipango](./07-planning-design/README.md) | Jinsi mawakala wanavyogawanya malengo makubwa kuwa hatua ndogo ndogo. | Andika mpango wa hatua tatu kwa ombi lako la maonyesho. |
| [08 - Ubunifu wa Mawakala Wengi](./08-multi-agent/README.md) | Wakati wa kugawanya kazi kati ya mawakala waliobobea. | Amua ikiwa maonyesho yako yanahitaji wakala mmoja au kadhaa. |
| [09 - Metakognition](./09-metacognition/README.md) | Jinsi mawakala wanavyoweza kupitia na kuboresha matokeo yao wenyewe. | Ongeza ukaguzi wa mwisho wa kujitathmini kabla ya wakala kujibu. |
| [10 - Mawakala wa AI Katika Uzalishaji](./10-ai-agents-production/README.md) | Mabadiliko yanapotokea wakati wakala anahamia kutoka kwenye maonyesho hadi uzalishaji. | Orodhesha unachotaka kusimamia: ubora, gharama, ucheleweshaji, matatizo. |
| [11 - Itifaki za Wakili](./11-agentic-protocols/README.md) | Jinsi itifaki zinavyounganisha mawakala na zana na mawakala wengine. | Tambua mahali itifaki ya kawaida inaweza kurahisisha ushirikiano. |
| [12 - Uhandisi wa Muktadha](./12-context-engineering/README.md) | Jinsi ya kuchagua, kukata, kutenganisha, na kusimamia muktadha. | Amua ni nini kinapaswa kuwa kwenye ombi na ni nini kinapaswa kubaki nje. |
| [13 - Kumbukumbu ya Wakili](./13-agent-memory/README.md) | Jinsi mawakala wanavyoweza kuhifadhi habari muhimu wakati wa mwingiliano. | Chagua upendeleo mmoja salama ambao maonyesho yako yanaweza kukumbuka. |
| [14 - Mfumo wa Wakili wa Microsoft](./14-microsoft-agent-framework/README.md) | Vijenzi vya kujenga vya mfumo kwa mawakala na michakato, pamoja na kuhudumia mawakala wa LangChain/LangGraph kwenye Microsoft Foundry. | Linganisha hatua za maonyesho yako na dhana za mfumo. |
| [15 - Mawakala wa Matumizi ya Kompyuta](./15-browser-use/README.md) | Jinsi mawakala wanavyoweza kuingiliana na kivinjari au sura za UI, ikijumuisha mifano halisi kama Microsoft Project Opal. | Chagua kazi moja ya kivinjari ambayo bado inapaswa kuhitaji uthibitisho wa mtumiaji. |
| [16 - Kuweka Mawakala Wanaoweza Kupanuka](./16-deploying-scalable-agents/README.md) | Jinsi ya kupeleka wakala kutoka kwenye mfano hadi kwenye uzalishaji unaoweza kupanuka na unaoonekana kwenye Microsoft Foundry (mawakala waliodhaminiwa, upitishaji mfano, kuweka ghala la data, milango ya tathmini, majaribio ya moshi). | Orodhesha masuala ya uzalishaji ambayo maonyesho yako bado yanahitaji: udhamini, upitishaji, gharama, tathmini. |
| [17 - Kuunda Mawakala wa AI wa Ndani](./17-creating-local-ai-agents/README.md) | Jinsi ya kujenga mawakala wa kwanza wa ndani wanaotekeleza kabisa kwenye mashine yako kwa Foundry Local na Qwen (zvombo vya ndani, RAG ya ndani, MCP ya ndani). | Amua ni sehemu gani za maonyesho yako zinapaswa kubaki binafsi na zitekelezwe ndani. |
| [18 - Kuweka Usalama wa Mawakala wa AI](./18-securing-ai-agents/README.md) | Jinsi ya kufanya vitendo vya wakala viwe na uwezo wa kuthibitishwa na kuonyesha wazi uharibifu. | Amua ni vitendo gani katika maonyesho yako vinapaswa kurekodiwa au kupewa risiti. |

## Kukagua Mawakala Walioanzishwa kwa Majaribio ya Moshi

Unapoweka wakala (Somo 16), **jaribio la moshi** ndilo jopo la chini kabisa la kwanza la kuangalia kwamba usambazaji una jibu halisi. Hifadhidata hii huleta orodha tayari-kwa-kutumia
chini ya [tests/](./tests/README.md) kwa mawakala walioweza kusambazwa katika Masomo
01, 04, 05, na 16, zikiwa zimeunganishwa na


[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) Kitendo cha GitHub
. Endesha kutoka kwenye kichupo cha **Actions** baada ya kuweka wakala wa somo.
Vipimo vya moshi ni mlango wa kwanza — tathmini ya mbali na mtandaoni (Masomo 10 na 16)
inakuambia jinsi wakala alivyo *mzuri*.

## Mawazo Muhimu Katika Maneno Rahisi kwa Mwanzo

### Zana

Zana ni kitu ambacho wakala anaweza kuitia ili kufanya kazi nje ya mfano. Zana nzuri
ina jina wazi, kazi ndogo, ingizo lililoainishwa, matokeo yanayotarajiwa, na njia salama
ya kushindwa.

Kwa maonyesho ya msaidizi wa kozi, zana inaweza kuwa:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG na Maarifa

RAG husaidia wakala kutoa majibu kutoka kwa vifaa vya chanzo badala ya kubahatisha. Katika
kozi hii, vifaa hivyo vya chanzo vinaweza kuwa README za masomo, mifano ya msimbo, au rasilimali za
nje zilizo kwenye viungo vya masomo.

Tumia RAG wakati jibu linapaswa kuzingatia hati, data, au faili za mradi wa sasa.


### Mipango

Mipango ni muhimu wakati ombi lina hatua zaidi ya moja. Hifadhi mipango fupi na
iwe wazi ya kutosha kwa mtengenezaji programu au mtumiaji waangalie.

Kwa maonyesho, mpango unaweza kuwa:

1. Tafuta masomo yanayohusiana na matumizi ya zana.
2. Fupisha masomo yanayofaa zaidi.
3. Pendekeza kazi moja ya mazoezi.

### Muktadha

Muktadha ni kile mfano unaona kwa sasa. Muktadha mdogo sana unaweza kufanya wakala
akose maelezo muhimu. Muktadha mwingi sana unaweza kufanya wakala kuwa polepole, gharama kubwa,
au kuwa rahisi kuchanganyikiwa.

Uhandisi mzuri wa muktadha unamaanisha kuchagua taarifa sahihi kwa ajili ya wito lijalo la mfano.


### Kumbukumbu

Kumbukumbu ni taarifa iliyowekwa hifadhi kwa ajili ya baadaye. Usihifadhi kila kitu. Hifadhi taarifa
tu wakati ni muhimu, salama, na rahisi kusasisha au kufuta.

Kwa mfano, kukumbuka "mwanafunzi anapendelea mifano ya Python" kunaweza kuwa muhimu.
Kukumbuka data nyeti za kibinafsi kawaida si muhimu.

### Tathmini na Uangalizi

Tathmini inahoji: je, wakala alifanya jambo sahihi?

Uangalizi unauliza: tunaweza kuona ilivyotokea?

Kwa mawakala wa uzalishaji, fuatilia miito ya mfano, miito ya zana, muktadha uliopatikana,
ucheleweshaji, gharama, matukio ya kushindwa, na mrejesho kutoka kwa mtumiaji.

### Uaminifu na Usalama

Wakala wa kuaminika wanahitaji zaidi ya tu agizo lenye msaada. Tumia zana za chini ya idhini,
idhini ya binadamu kwa vitendo vya athari kubwa, kufuta data inapohitajika, na kumbukumbu au
risiti kwa vitendo vinavyopaswa kuwa na ukaguzi.

## Utaratibu wa Mapitio ya Dakika 15

Tumia utaratibu huu baada ya kila somo:

1. **Fupisha somo kwa sentensi moja.**
2. **Taja uwezo mpya wa wakala.** Kwa mfano: matumizi ya zana, upokeaji,
   upangaji, kumbukumbu, uangalizi, au usalama.
3. **Ongeza kwenye maonyesho ya msaidizi wa kozi.** Ni mabadiliko gani sasa maonyeshoni?
4. **Tafuta hatari.** Nini kinaweza kwenda vibaya ikiwa uwezo huu utatumika vibaya?
5. **Andika swali moja la majaribio.** Je, ungeangaliaje kama wakala anafanya vizuri?

## Ukaguzi wa Haraka wa Kujitathmini

Kabla ya kuendelea, jaribu kujibu maswali haya:

1. Wakala anaweza kufanya nini ambacho chatbot wa kawaida hawezi kufanya peke yake?
2. Ni zana gani wakala wako atahitaji kwanza, na kwa nini?
3. Chanzo gani cha maarifa kinapaswa kuimarisha jibu la wakala?
4. Muktadha gani unapaswa kujumuishwa katika wito lijalo la mfano?

5. Wakala anapaswa kukumbuka nini, na anapaswa kuepuka kuhifadhi nini?
6. Wakala anapaswa kuuliza ruhusa ya binadamu lini?
7. Kumbukumbu, nyendo, au risiti gani zingekusaidia kufanya utambuzi wa hitilafu au ukaguzi wa wakala baadaye?


## Zozi lililopendekezwa la Capstone

Mwishoni mwa kozi, tengeneza wakala mdogo anayesaidia mwanafunzi kuvinjari
hifadhi hii.

Toleo la chini kabisa:

- Kubali mada kutoka kwa mtumiaji.
- Pata masomo yanayohusiana zaidi.
- Fupisha ni nini cha kusoma kwanza.
- Pendekeza kazi moja ya vitendo ya mazoezi.
- Onyesha faili za somo au viungo vilivyotumika.

Toleo la kupanua:

- Kumbuka lugha ya programu iliyopendekezwa na mwanafunzi.
- Tumia mpango rahisi kabla ya kujibu.
- Ongeza hatua ya kujiangalia kabla ya jibu la mwisho.
- Rekodi simu za zana na vyanzo vilivyopatikana.
- Uliza uthibitisho kabla ya kufungua kivinjari au kazi za usanifishaji wa UI.

Hii inakupa njia ndogo lakini halisi ya kutumia zana, RAG, upangaji,
muktadha, kumbukumbu, uangalifu, na kuaminika katika mradi mmoja.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->