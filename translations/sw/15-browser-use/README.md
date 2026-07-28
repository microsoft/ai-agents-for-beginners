# Kujenga Wakala wa Matumizi ya Kompyuta (CUA)

Wakala wa matumizi ya kompyuta wanaweza kuingiliana na tovuti kwa njia ile ile mtu angetenda: kwa kufungua kivinjari, kuchunguza ukurasa, na kuchukua hatua bora inayofuata kulingana na kile wanachoona. Katika somo hili, utaunda wakala wa uendeshaji wa kivinjari ambaye anatafuta Airbnb, kunasa data ya orodha iliyopangwa, na kubainisha makazi ya bei nafuu zaidi huko Stockholm.

Somo hili linachanganya Matumizi ya Kivinjari kwa urambazaji unaoendeshwa na AI, Playwright na Chrome DevTools Protocol (CDP) kwa udhibiti wa kivinjari, Azure OpenAI kwa mantiki inayotumia kuona, na Pydantic kwa kunasa data iliyopangwa.

## Utangulizi

Somo hili litatembelea:

- Kuelewa wakati wakala wa matumizi ya kompyuta ni chaguo bora kuliko uendeshaji wa API pekee
- Kuchanganya Matumizi ya Kivinjari na Playwright na CDP kwa usimamizi wa mzunguko wa maisha wa kivinjari unaotegemewa
- Kutumia Azure OpenAI kwa kuona na matokeo ya Pydantic yaliyopangwa ili kunasa data ya orodha kutoka kwa kurasa za wavuti zinazobadilika
- Kuamua wakati wa kutumia mtiririko wa kazi wa uendeshaji wa kivinjari wa wakala kwanza, muigizaji kwanza, au mchanganyiko

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utajua jinsi ya:

- Kusanidi Matumizi ya Kivinjari na Azure OpenAI na Playwright
- Kujenga mtiririko wa kazi wa uendeshaji wa kivinjari unaorambatiza tovuti halisi na kushughulikia vipengele vya UI vinavyobadilika
- Kunasa matokeo yaliyoandikwa kutoka kwa maudhui ya ukurasa yanayoonekana na kuyageuza kuwa mantiki ya biashara ya chini
- Kuchagua kati ya mifumo ya wakala na muigizaji kulingana na jinsi kazi ya kivinjari inavyoweza kutabirika

## Mfano wa Msimbo

Somo hili linajumuisha mafunzo ya daftari moja:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Huitoa kikao cha Chrome kwa CDP, inatafuta orodha za Stockholm kwenye Airbnb, inachukua bei kwa kuona kwa Matumizi ya Kivinjari, na kurudisha chaguo la bei nafuu zaidi kama data iliyopangwa.

## Masharti ya Awali

- Python 3.12+
- Usanidi wa utumaji wa Azure OpenAI umewekwa katika mazingira yako
- Chrome au Chromium imewekwa kwa karibu
- Mategemeo ya Playwright yamewekwa
- Uwezo wa msingi wa Python async

## Usanidi

Sakinisha vifurushi vinavyotumika kwenye daftari:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Weka mabadiliko ya mazingira ya Azure OpenAI yanayotumika na daftari:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Hiari: chaguo-msingi ni toleo la hivi karibuni la API linapoachwa
AZURE_OPENAI_API_VERSION=...
```

## Muhtasari wa Muundo

Daftari linaonyesha mtiririko wa kazi wa mchanganyiko wa uendeshaji wa kivinjari:

1. Chrome huanza na CDP imelengwa ili Playwright na Matumizi ya Kivinjari waweze kushiriki kikao kimoja cha kivinjari.
2. Wakala wa Matumizi ya Kivinjari hushughulikia kazi za mwelekeo zisizo na kikomo kama kufungua Airbnb, kufunga dirisha za pop-up, na kutafuta Stockholm.
3. Ukurasa unaotekelezwa unachunguzwa kwa kutumia muundo wa Pydantic ili kunasa vichwa vya orodha, bei za usiku, alama, na URL.
4. Mantiki ya Python inalinganisha orodha zilizochukuliwa na kuonyesha matokeo ya bei nafuu zaidi.

Njia hii inahifadhi mantiki inayotegemea kuona inayobadilika ambayo Matumizi ya Kivinjari ni mzuri nayo huku ikikuwezesha udhibiti wa kivinjari unaotegemewa unapo hitajika.

## Muhimu wa Kuhifadhi na Mbinu Bora

### Wakati wa Kutumia Wakala dhidi ya Muigizaji

| Hali | Tumia Wakala | Tumia Muigizaji |
|----------|-----------|-----------|
| Muundo unaobadilika | Ndiyo, AI inaweza kuendana na mabadiliko ya ukurasa | Hapana, vichujio dhaifu vinaweza kuvunjika |
| Muundo unaojulikana | Hapana, wakala ni polepole zaidi kuliko udhibiti wa moja kwa moja | Ndiyo, haraka na sahihi |
| Kupata vipengele | Ndiyo, lugha ya asili hufanya kazi vizuri | Hapana, vichujio halisi vinahitajika |
| Udhibiti wa muda | Hapana, hauwezi kutabirika | Ndiyo, udhibiti kamili wa kusubiri na kujaribu tena |
| Mtiririko mgumu wa kazi | Ndiyo, hushughulikia hali zisizotarajiwa za UI | Hapana, inahitaji matawi wazi |

### Mbinu Bora za Matumizi ya Kivinjari

1. Anza na wakala kwa ajili ya upelelezi na urambazaji unaobadilika.
2. Badilisha kwa udhibiti wa moja kwa moja wa ukurasa wakati mwingiliano unapokuwa wa kutabirika.
3. Tumia mifano ya matokeo iliyopangwa ili data iliyochukuliwa ithibitiswe na iwe salama aina zake.
4. Ongeza ucheleweshaji kwa kistratejia baada ya hatua zinazosababisha mabadiliko ya UI yanayoonekana.
5. Chukua picha za skrini wakati wa kutekeleza hatua ili makosa yapate utambuzi rahisi.
6. Tarajia tovuti kubadilika na tengeneza mikakati ya dharura kwa dirisha za pop-up na mabadiliko ya mpangilio.
7. Changanya mifumo ya wakala na muigizaji ili kupata raha na usahihi.

### Miongozo ya Usalama kwa Wakala wa Kivinjari

Wakala wa kivinjari hufanya kazi kwenye tovuti zinazoendelea, kwa hivyo wanahitaji mipaka madhubuti zaidi kuliko script inayoitumia API inayojulikana pekee. Kabla ya kutoka kwenye maonyesho ya daftari hadi mtiririko halisi wa kazi, fafanua udhibiti wa kile wakala anaweza kuona, kubofya, na kuwasilisha.

1. **Pima mazingira ya urambazaji.** Endesha wakala katika profaili ya kivinjari iliyotengwa au sandbox, na umweke kikomo kwa maeneo yanayohitajika kwa kazi.
2. **Tenganisha uchunguzi kutoka kwa hatua.** Mruhusu wakala atafute, asome, na achukue data kwanza; hitaji idhini wazi kabla ya kuwasilisha fomu, kutuma ujumbe, kuweka booking, kununua, kufuta rekodi, au kubadilisha mipangilio ya akaunti.
3. **Usiweke siri kwenye maelekezo na rekodi.** Usianze nywila, maelezo ya malipo, vidakuzi vya kikao, au data mbichi ya binafsi kwenye muktadha wa mfano. Mruhusu mtumiaji kuingia kwa uthibitisho na kufuta sehemu nyeti kwenye kumbukumbu.
4. **Chukulia maudhui ya ukurasa kama pembejeo isiyoaminika.** Tovuti inaweza kuwa na maagizo maalum kwa wakala, si kwa mtumiaji. Wakala anapaswa kupuuzia maandishi yanayoitikia kubadilisha lengo lake, kufichua data, kuzima kinga, au kutembelea maeneo yasiyo husika.
5. **Tumia ukaguzi thabiti kwa hatua zenye hatari.** Hakikisha URL ya sasa, kichwa cha ukurasa, kipengee kilichochaguliwa, bei, mpokeaji, na muhtasari wa hatua na msimbo kabla ya kumhitaji mtumiaji kuidhinisha hatua ya mwisho.
6. **Weka bajeti na masharti ya kuacha.** Kuweka kikomo cha idadi ya hatua, majaribio, tabo, na dakika ambazo wakala anaweza kutumia. Acha wakati hali ya ukurasa haieleweki badala ya kuendelea kubofya.
7. **Rekodi ushahidi unaotumika, si kila kitu.** Hifadhi muhtasari wa hatua, alama za wakati, URL, maelezo ya kipengee kilichochaguliwa, na marejeleo ya picha za skrini ili kushindwa kutathminiwa bila kuhifadhi maudhui yasiyohitajika ya ukurasa.

Katika mfano wa Airbnb, chaguo salama ni kutafuta orodha na kunasa bei. Kuingia, kuwasiliana na mwenyeji, au kukamilisha booking inapaswa kuwa hatua tofauti inayothibitishwa na mtumiaji.

### Matumizi Halisi Duniani

- Kuweka booking ya safari na kufuatilia bei
- Kulinganisha bei na kukagua upatikanaji kwenye e-commerce
- Kunasa data iliyopangwa kutoka kwa tovuti zinazobadilika
- Upimaji na uthibitishaji wa UI unaojua kuona
- Kufuatilia na kutangaza tovuti
- Kujaza fomu kwa ujanja katika mtiririko wa hatua nyingi

## Mfano Halisi Duniani: Mradi wa Microsoft Opal

Wakala unaoujenga katika somo hili ni toleo dogo, la ndani la **wakala wa matumizi ya kompyuta (CUA)** — programu inayodhibiti kivinjari kama mtu anavyofanya. Microsoft inaleta wazo hili kwa wateja wa biashara kupitia **[Mradi Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, kipengele katika Microsoft 365 Copilot.

Kwa Mradi Opal, unaelezea kazi na wakala hufanya kazi kwa niaba yako akitumia **matumizi ya kompyuta kwenye Windows 365 Cloud PC salama**, akifanya kazi katika programu, tovuti, na data zinazotegemea kivinjari za shirika lako. Hufanya kazi **kimtandao kwa nyuma**, na unaweza kuelekeza kazi au kuchukua udhibiti wakati wowote. Kazi za mfano ni pamoja na:

- Kusimamia maombi ya uanachama wa vikundi vya usalama
- Kukusanya na kuthibitisha ushahidi wa ukaguzi kwa mapitio ya ufuatiliaji
- Kusuluhisha matukio ya IT (kusasisha hali ya tiketi, kugawa wamiliki, kufunga nakala)
- Kukuza data za Excel kwa jedwali la kufunga kifedha

Opal ni rejeleo muhimu la jinsi **wakala wa matumizi ya kompyuta wa kiwango cha uzalishaji na wa kuaminika** anavyoonekana — na linaimarisha dhana kutoka masomo ya awali:

| Dhana katika kozi hii | Jinsi Mradi Opal unavyoitumia |
|------------------------|-----------------------------|
| **Binadamu aliyeingiliana** (Somo la 06) | Opal husimama kwa ajili ya taarifa za kuingia, data nyeti, au maagizo yasiyoeleweka, na kamwe haingii nywila au kuwasilisha fomu bila uthibitisho wazi. Unaweza *Kuchukua Udhibiti* na *Kurejesha Udhibiti* katikati ya kazi. |
| **Wakala wa kuaminika na salama** (Masomo 06 & 18) | Hufanya kazi kwenye Windows 365 Cloud PC iliyotengwa, ni kivinjari pekee kwa chaguo-msingi (upatikanaji mwingine wa kompyuta umezuiwa, unaendeshwa kupitia Intune), hutumia utambulisho wako tu kwa hivyo inaingia taarifa unazoidhinishwa, na hurekodi kila hatua kwa ajili ya ukaguzi. |
| **Mipango na uwezo wa kujitathmini** (Masomo 07 & 09) | Opal huunda mpango wa kazi kwanza, kisha husimamia mantiki yake kila hatua na hushimama ikiwa inagundua shughuli zenye kutiliwa shaka. |
| **Uwezo unaoweza kutumika tena / zana** (Somo la 04) | **Ujuzi** hukuruhusu kuandika maelekezo ya kazi zinazorudiwa (zinazoletwa kutoka kwenye faili ya `.md` au kuandikwa na Opal) na kuzitumia katika mazungumzo tofauti. |

> **Upatikanaji:** Mradi Opal kwa sasa upo kwa watumiaji wa [mpango wa mapema wa Frontier](https://adoption.microsoft.com/copilot/frontier-program/) pamoja na usajili wa Microsoft 365 Copilot, na msimamizi wako lazima akamilishe usanidi. Kwa kuwa ni kipengele cha majaribio cha Frontier, uwezo unaweza kubadilika kwa muda.

## Rasilimali Zaidi

- [Anza na Mradi Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Kiolezo cha muunganisho wa Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Vigezo vya muigizaji wa Browser-Use na kunasa maudhui](https://docs.browser-use.com/customize/actor/all-parameters)
- [Usanidi wa Kozi](../00-course-setup/README.md)

## Somo lililopita

[Kuchunguza Mfumo wa Wakala wa Microsoft](../14-microsoft-agent-framework/README.md)

## Somo lijalo

[Kuweka wakala wanaoweza kupanuka](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->