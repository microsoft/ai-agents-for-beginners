# Kujenga Wakala wa Matumizi ya Kompyuta (CUA)

Wakala wa matumizi ya kompyuta wanaweza kuingiliana na tovuti kwa njia ile ile mtu anavyofanya: kwa kufungua kivinjari, kuchunguza ukurasa, na kuchukua hatua inayofuata bora kulingana na wanavyoona. Katika somo hili, utajenga wakala wa otomatiki wa kivinjari anayesaka Airbnb, kutoa data ya orodha iliyopangwa, na kubaini malazi ya bei nafuu Stockholm.

Somo hili linaunganisha Matumizi ya Kivinjari kwa urambazaji unaoendeshwa na AI, Playwright na Chrome DevTools Protocol (CDP) kwa ajili ya udhibiti wa kivinjari, Azure OpenAI kwa sababu za kuona na Pydantic kwa uchimbaji wa data wa muundo.

## Utangulizi

Somo hili litashughulikia:

- Kuelewa wakati wakala wa matumizi ya kompyuta ni chaguo bora kuliko otomatiki ya API tu
- Kuunganisha Matumizi ya Kivinjari na Playwright na CDP kwa usimamizi thabiti wa mzunguko wa kivinjari
- Kutumia Azure OpenAI ya kuona na matokeo ya muundo ya Pydantic kutoa data ya orodha kutoka kwa kurasa za wavuti zenye mabadiliko
- Kuamua wakati wa kutumia mtiririko wa kazi wa otomatiki wa kivinjari wa wakala kwanza, mtendaji kwanza, au mseto

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utajua jinsi ya:

- Kusanidi Matumizi ya Kivinjari na Azure OpenAI na Playwright
- Kujenga mtiririko wa kazi wa otomatiki wa kivinjari unaoenda kwenye tovuti halisi na kushughulikia vipengele vya UI vya mabadiliko
- Kutoa matokeo yaliyotambulika kutoka kwa yaliyomo kwenye ukurasa yanayoonekana na kuyageuza kuwa mantiki ya biashara inayofuata
- Kuchagua kati ya mifumo ya wakala na mtendaji kulingana na utabiri wa kazi ya kivinjari

## Mfano wa Msimbo

Somo hili linajumuisha mafunzo ya daftari moja:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Inazindua kikao cha Chrome kupitia CDP, inatafuta orodha za Stockholm kwenye Airbnb, hutoa bei kwa kutumia kuona kwa Browser-Use, na kurejesha chaguo la bei nafuu kama data ya muundo.

## Vigezo Vinavyotakiwa

- Python 3.12+
- Upangishaji wa Azure OpenAI umewekwa kwenye mazingira yako
- Chrome au Chromium imewekwa mahali hapa
- Vitegemezi vya Playwright vimewekwa
- Uelewa wa msingi wa Python asynchronous

## Usanidi

Sakinisha vifurushi vinavyotumika katika daftari:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Sanidi mazingira ya Azure OpenAI yanayotumika na daftari:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Hiari: huchukua toleo la API la hivi karibuni kama lisipotajwa
AZURE_OPENAI_API_VERSION=...
```

## Muhtasari wa Mimariko

Daftari linaonyesha mtiririko wa kazi wa otomatiki wa kivinjari mseto:

1. Chrome huanza na CDP imewezeshwa ili Playwright na Browser-Use waweze kushiriki kikao kimoja cha kivinjari.
2. Wakala wa Browser-Use hushughulikia kazi za urambazaji zisizo na kikomo kama kufungua Airbnb, kufunga dirisha za pop-ups, na kutafuta Stockholm.
3. Ukurasa unaoendeshwa huchunguzwa kwa matumizi ya skimu ya Pydantic iliyopangwa kutoa vichwa vya orodha, bei za usiku, viwango, na URL.
4. Mantiki ya Python inalinganisha orodha zilizotolewa na kuangazia matokeo ya bei nafuu.

Njia hii huweka hoja ya kuona inayobadilika vizuri ambayo Browser-Use ni mzuri katika, huku ikikupatia udhibiti thabiti wa kivinjari wakati unahitaji.

## Muhimu wa Kufahamu na Mbinu Bora

### Wakati wa Kutumia Wakala dhidi ya Mtendaji

| Hali | Tumia Wakala | Tumia Mtendaji |
|----------|-----------|-----------|
| Mpangilio wenye mabadiliko | Ndiyo, AI inaweza kuendana na mabadiliko ya ukurasa | Hapana, waanzilishi dhaifu wanaweza kuvunjika |
| Muundo unaojulikana | Hapana, wakala ni polepole kuliko udhibiti wa moja kwa moja | Ndiyo, haraka na sahihi |
| Kupata vipengele | Ndiyo, lugha ya asili hufanya kazi vizuri | Hapana, waanzilishi sahihi yanahitajika |
| Udhibiti wa muda | Hapana, haibashiriki utabiri mzuri | Ndiyo, udhibiti kamili juu ya kuchelewa na jaribio tena |
| Mitiririko ngumu ya kazi | Ndiyo, hushughulikia hali zisizotarajiwa za UI | Hapana, zinahitaji matawi wazi |

### Mbinu Bora za Browser-Use

1. Anza na wakala kwa ajili ya utafutaji na urambazaji unaobadilika.
2. Badilika kwa udhibiti wa moja kwa moja wa ukurasa wakati mwingiliano unakuwa wa utabiri.
3. Tumia mifano ya matokeo ya muundo ili data iliyotolewa ithibitishe na iwe salama kwa aina.
4. Ongeza kuchelewesha kwa makusudi baada ya vitendo vinavyoanzisha mabadiliko ya UI yanayoonekana.
5. Piga maelezo ya skrini unapoendelea ili makosa yawe rahisi kufuatilia.
6. Tarajia tovuti kubadilika na tengeneza mikakati ya kuepuka kwa dirisha za pop-ups na mabadiliko ya mpangilio.
7. Changanya mifumo ya wakala na mtendaji kupata mabadiliko na usahihi.

### Matumizi Halisi Duniani

- Uhifadhi wa usafiri na ufuatiliaji wa bei
- Ulinganisho wa bei wa e-commerce na ukaguzi wa upatikanaji
- Uchimbaji wa muundo kutoka kwa tovuti zinazobadilika
- Mazingira ya mtihani na uhakikisho wa UI unaojali kuona
- Ufuatiliaji wa tovuti na kutoa arifa
- Kujaza fomu kwa akili kupitia taratibu zenye hatua nyingi

## Mfano wa Kiasili: Microsoft Project Opal

Wakala unaojenga katika somo hili ni toleo dogo, la mahali hapa la **wakala wa matumizi ya kompyuta (CUA)** — programu inayosukuma kivinjari kwa njia mtu anavyofanya. Microsoft inaleta wazo hili kwa uongozi wa biashara kupitia **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, uwezo ndani ya Microsoft 365 Copilot.

Kwa Project Opal, unaelezea kazi na wakala hufanya kazi kwa niaba yako kwa kutumia **matumizi ya kompyuta kwenye Windows 365 Cloud PC salama**, ukifanya kazi kwenye programu, tovuti, na data za kivinjari za shirika lako. Hufanya kazi **kwa mtiririko wa asilia kwa nyuma**, na unaweza kuelekeza kazi au kuchukua udhibiti wakati wowote. Kazi za mfano ni pamoja na:

- Kusimamia maombi ya uanachama wa kundi la usalama
- Kusanya na kuthibitisha ushahidi wa ukaguzi kwa ajili ya mapitio ya ufuatiliaji
- Kusimamia matukio ya IT (kusasisha hali ya tiketi, kugawa wamiliki, kufunga nakala)
- Kukusanya data za Excel katika jedwali la kufunga kifedha

Opal ni rejea muhimu kwa jinsi wakala wa matumizi ya kompyuta wa **kiwango cha uzalishaji, wa kuaminika** anavyopaswa kuonekana — na inathibitisha dhana kutoka masomo ya awali:

| Dhana katika kozi hii | Jinsi Project Opal inavyoiweka |
|------------------------|-----------------------------|
| **Mtu ndani ya mzunguko** (Somo 06) | Opal inasimama kwa ajili ya vitambulisho vya kuingia, data nyeti, au maelekezo yasiyo wazi, na haingii nywila au kuwasilisha fomu bila uthibitisho wazi. Unaweza *Kuchukua Udhibiti* na *Kurudisha Udhibiti* katikati ya kazi. |
| **Wakala wa kuaminika na salama** (Masomo 06 & 18) | Hufanya kazi ndani ya Windows 365 Cloud PC iliyotengwa, ni kivinjari pekee kwa default (upatikanaji mwingine wa kompyuta umefungwa, unasimamiwa kupitia Intune), hutumia *kitambulisho chako* kwa hivyo huhitaji tu kile unachoruhusiwa, na hurekodi kila hatua kwa ajili ya ukaguzi. |
| **Mipango & fikra juu ya fikra** (Masomo 07 & 09) | Opal hutengeneza mpango wa kazi kwanza, kisha inasimamia hoja zake katika kila hatua na kusimama endapo itagundua shughuli za shaka. |
| **Uwezo wa kutumika tena / zana** (Somo 04) | **Ujuzi** hukuruhusu kuandika maelekezo kwa kazi zinazojirudia (zinaingizwa kutoka faili `.md` au kuandikwa na Opal) na kuzitumia tena katika mazungumzo. |

> **Upatikanaji:** Project Opal kwa sasa inapatikana kwa watumiaji wa [mpango wa ufikiaji wa mapema wa Frontier](https://adoption.microsoft.com/copilot/frontier-program/) kwa usajili wa Microsoft 365 Copilot, na msimamizi wako anapaswa kukamilisha usanidi. Kwa kuwa ni kipengele cha majaribio cha Frontier, uwezo unaweza kubadilika kadri muda unavyopita.

## Rasilimali Zaidi

- [Anza na Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Kiolezo cha muunganisho wa Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Vigezo vya mtendaji wa Browser-Use na uchimbaji wa maudhui](https://docs.browser-use.com/customize/actor/all-parameters)
- [Usanidi wa Kozi](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->