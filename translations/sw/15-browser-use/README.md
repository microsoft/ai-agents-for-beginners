# Ujenzi wa Wakala za Matumizi ya Kompyuta (CUA)

Wakala za matumizi ya kompyuta zinaweza kuingiliana na tovuti kwa njia ile ile mtu anavyofanya: kwa kufungua kivinjari, kukagua ukurasa, na kuchukua hatua inayofuata bora kutoka wanavyoiona. Katika somo hili, utajenga wakala wa kiotomatiki wa kivinjari anayefanya utafutaji kwenye Airbnb, kuchambua data ya orodha zilizopangwa, na kubaini malazi ya bei rahisi zaidi huko Stockholm.

Somo hili linachanganya Browser-Use kwa urambazaji unaoendeshwa na AI, Playwright na Chrome DevTools Protocol (CDP) kwa udhibiti wa kivinjari, Azure OpenAI kwa sababu inayotegemea kuona, na Pydantic kwa uchambuzi uliopangwa.

## Utangulizi

Somo hili litatembelea:

- Kuelewa lini wakala wa matumizi ya kompyuta ni chaguo bora kuliko otomatiki ya API pekee
- Kuchanganya Browser-Use na Playwright na CDP kwa usimamizi wa kuaminika wa mzunguko wa maisha wa kivinjari
- Kutumia Azure OpenAI kuona na uzalishaji uliopangwa wa Pydantic kuchambua data ya orodha kutoka kwa kurasa za wavuti zinazoibuka
- Kuweka uamuzi wa kutumia mtiririko wa kazi wa otomatiki wa kivinjari unaoanza na wakala, mchezaji, au mchanganyiko

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utajua jinsi ya:

- Kusanidi Browser-Use na Azure OpenAI na Playwright
- Kujenga mtiririko wa kazi wa kiotomatiki wa kivinjari unaoelekeza tovuti halisi na kushughulikia vipengele vya UI vinavyoibuka
- Kuchukua matokeo yaliyo-andikwa kutoka kwa maudhui yanayoonekana kwenye ukurasa na kuyageuza kuwa mantiki ya biashara ya baadae
- Kuchagua kati ya mifumo ya wakala na mchezaji kulingana na jinsi kazi ya kivinjari inavyotarajiwa

## Mfano wa Msimbo

Somo hili lina mafunzo moja ya daftari:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Inaendesha kikao cha Chrome kupitia CDP, hufanya utafutaji wa orodha za Stockholm kupitia Airbnb, huchambua bei kwa kutumia Browser-Use vision, na hurudisha chaguo la bei rahisi kama data iliyopangwa.

## Mahitaji ya Awali

- Python 3.12+
- Usanidi wa ugawaji wa Azure OpenAI katika mazingira yako
- Chrome au Chromium imewekwa kwa ndani
- Mipangilio ya kutegemewa ya Playwright imewekwa
- Uzoefu wa msingi na Python asynchronous

## Usanidi

Sakinisha vifurushi vinavyotumika katika daftari:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Sanidi vigezo vya mazingira vya Azure OpenAI vinavyotumika na daftari:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Hiari: chagua toleo la API la hivi karibuni ikiwa halitatajwi
AZURE_OPENAI_API_VERSION=...
```

## Muhtasari wa Mimarisho

Daftari linaonyesha mtiririko wa kazi wa kiotomatiki wa kivinjari mchanganyiko:

1. Chrome inaanza na CDP imewezeshwa ili Playwright na Browser-Use waweze kushiriki kikao kimoja cha kivinjari.
2. Wakala wa Browser-Use hushughulikia kazi za urambazaji zisizo na kikomo kama kufungua Airbnb, kufunga dirisha la matangazo, na kutafuta Stockholm.
3. Ukurasa unaotumika huchambuliwa kwa kutumia kiolezo cha Pydantic kilichopangwa ili kuchukua majina ya orodha, bei za kila usiku, viwango, na URL.
4. Mantiki ya Python inalinganisha orodha zilizopatikana na kuonyesha matokeo ya bei rahisi.

Njia hii inahifadhi akili ya kuona inayojumuishwa ambayo Browser-Use ni mzuri nayo huku ikikupa udhibiti wa uhakika wa kivinjari unahitaji.

## Muhimu wa Kufahamu na Mbinu Bora

### Lini Utumie Wakala vs Mchezaji

| Hali | Tumia Wakala | Tumia Mchezaji |
|----------|-----------|-----------|
| Muundo unaobadilika | Ndiyo, AI inaweza kuendana na mabadiliko ya ukurasa | Hapana, vitambuzi dhaifu vinaweza kuvunjika |
| Muundo unaojulikana | Hapana, wakala ni polepole kuliko udhibiti wa moja kwa moja | Ndiyo, haraka na sahihi |
| Kupata vipengele | Ndiyo, lugha ya asili inafanya kazi vizuri | Hapana, vitambuzi sahihi vinahitajika |
| Udhibiti wa muda | Hapana, hauwezi kutabirika | Ndiyo, udhibiti kamili wa kusubiri na kurudia |
| Mtiririko tata | Ndiyo, hushughulikia hali za UI zisizotarajiwa | Hapana, inahitaji matawi wazi |

### Mbinu Bora za Browser-Use

1. Anza na wakala kwa ajili ya uchunguzi na urambazaji unaobadilika.
2. Badilisha kwa udhibiti wa ukurasa moja kwa moja wakati mwingiliano unapotabirika.
3. Tumia mifano ya uzalishaji uliopangwa ili data iliyochukuliwa ihakikishwe na iwe na aina salama.
4. Ongeza ucheleweshaji kwa mkakati baada ya hatua zinazosababisha mabadiliko yanayoonekana ya UI.
5. Piga skrini tunapoendelea ili kuwezesha utatuzi wa makosa.
6. Tarajia tovuti kubadilika na panga mikakati ya akiba kwa madirisha ya matangazo na mabadiliko ya muundo.
7. Changanya mifumo ya wakala na mchezaji kupata mchanganyiko wa urahisi na usahihi.

### Mipaka ya Usalama kwa Wakala wa Kivinjari

Wakala wa kivinjari hufanya kazi kwenye tovuti hai, hivyo wanahitaji mipaka makini zaidi kuliko script inayoitumia API inayojulikana pekee. Kabla ya kuhamia kutoka kwenye maonyesho ya daftari kwa mtiririko halisi wa kazi, fafanua udhibiti wa kile wakala anaweza kuona, kubofya, na kuwasilisha.

1. **Tambua mazingira ya kivinjari.** Endesha wakala katika profaili ya kivinjari iliyojitolea au sandbox, na umwachilie kwa maeneo yanayohitajika kwa kazi.
2. **Tofautisha uchunguzi na hatua.** Mwachilie wakala kutafuta, kusoma, na kuchambua data kwanza; hitaji hatua wazi ya idhini kabla ya kuwasilisha fomu, kutuma ujumbe, kuweka tiketi, kufanya manunuzi, kufuta rekodi, au kubadilisha mipangilio ya akaunti.
3. **Hifadhi siri nje ya amri na rekodi.** Usimweke nywila, maelezo ya malipo, vidakuzi vya kikao, au data ya kibinafsi ghafi katika muktadha wa mfano. Mruhusu mtumiaji kuchukua udhibiti kwa uthibitisho na kufuta sehemu nyeti kutoka kwa kumbukumbu.
4. **Tumia maudhui ya ukurasa kama ingizo lisilo la kuaminika.** Tovuti inaweza kuwa na maelekezo yanayomlenga wakala, si mtumiaji. Wakala anapaswa kupuuza maandishi yanayomuambia kubadilisha lengo, kufichua data, kuzima kinga, au kutembelea tovuti zisizohusiana.
5. **Tumia ukaguzi wa uhakika katika hatua hatari.** Thibitisha URL ya sasa, kichwa cha ukurasa, kipengele kilichochaguliwa, bei, mpokeaji, na muhtasari wa hatua kwa msimbo kabla ya kumuomba mtumiaji kuidhinisha hatua ya mwisho.
6. **Weka bajeti na vigezo vya kusimama.** Zuia idadi ya hatua, kurudia, vichupo, na dakika wakala anaweza kutumia. Simama wakati hali ya ukurasa haijulikani badala ya kuendelea kubofya.
7. **Rekodi ushahidi muhimu, si kila kitu.** Hifadhi muhtasari wa hatua, muda wa rekodi, URL, maelezo ya kipengele kilichochaguliwa, na kumbukumbu za picha ili kushindwa kuweza kutathminiwa bila kuhifadhi maudhui ya ukurasa usiohitajika.

Katika mfano wa Airbnb, chaguo salama ni kutafuta orodha na kuchukua bei. Kuingia, kuwasiliana na mwenyeji, au kukamilisha uhifadhi inapaswa kuwa hatua tofauti inayoruhusiwa na mtumiaji.

### Matumizi Halisi ya Dunia

- Uhifadhi wa usafiri na ufuatiliaji wa bei
- Kulinganisha bei katika masoko mtandaoni na ukaguzi wa upatikanaji
- Uchambuzi uliopangwa kutoka kwa tovuti zinazoibuka
- Upimaji na uthibitishaji wa UI unaojali kuona
- Ufuatiliaji wa tovuti na tahadhari
- Kujaza fomu kwa akili katika mfululizo wa hatua nyingi

## Mfano Halisi wa Dunia: Mradi wa Microsoft Opal

Wakala unayejenga katika somo hili ni toleo dogo na la ndani la **wakala wa matumizi ya kompyuta (CUA)** — programu inayokuwa kivinjari kama mtu anavyofanya. Microsoft inaleta wazo hili kwa tasnia kwa kupitia **[Mradi Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, uwezo katika Microsoft 365 Copilot.

Kupitia Mradi Opal, unaeleza kazi na wakala anafanya kazi kwa niaba yako kwa kutumia **matumizi ya kompyuta kwenye Windows 365 Cloud PC salama**, akifanya kazi kwenye programu za kivinjari, tovuti, na data za shirika lako. Inafanya kazi **kwa asynchronous baada ya mandharinyuma**, na unaweza kuelekeza kazi au kuchukua udhibiti wakati wowote. Kazi mfano ni:

- Kusimamia maombi ya wanachama wa vikundi vya usalama
- Kukusanya na kuthibitisha ushahidi wa ukaguzi kwa mapitio ya utii
- Kusimamia matukio ya IT (kusasisha hali ya tiketi, kuteua wamiliki, kufunga rudufu)
- Kukusanya data ya Excel katika mwanzo wa kifedha

Opal ni rejeleo muhimu kwa wakala wa matumizi ya kompyuta wa **kinachoaminika na cha kizazi cha uzalishaji** — na inasisitiza dhana kutoka masomo ya awali:

| Dhana katika kozi hii | Jinsi Mradi Opal unavyotekeleza |
|------------------------|-----------------------------|
| **Mtu kati ya mzunguko** (Somo la 06) | Opal husimama kwa ajili ya taarifa za kuingia, data nyeti, au maelekezo yenye utata, na hauingizi nywila au kuwasilisha fomu bila uthibitisho wazi. Unaweza *Kuchukua Udhibiti* na *Kurudisha Udhibiti* wakati wa kazi. |
| **Wakala wa kuaminika na salama** (Masomo 06 & 18) | Inaendesha kwenye Windows 365 Cloud PC iliyotengwa, ni kivinjari pekee kwa chaguo-msingi (ufikiaji wa kompyuta nyingine umezuiwa, huanzishwa kupitia Intune), hutumia kitambulisho chako hivyo inapata tu kile unachoruhusiwa, na hurekodi kila hatua kwa uhakika. |
| **Mipango na metacognition** (Masomo 07 & 09) | Opal huunda mpango wa kazi kwanza, kisha inasimamia akili yake katika kila hatua na kusimama kama inagundua shughuli za kushuku. |
| **Uwezo wa kutumia tena / zana** (Somo la 04) | **Ujuzi** hukuwezesha kuandika maelekezo kwa kazi zinazorudiwa (zilizoungwa kutoka faili `.md` au kuandikwa na Opal) na kuzitumia tena kwenye mazungumzo. |

> **Upatikanaji:** Mradi Opal uko tayari kwa watumiaji katika [mpango wa upatikanaji mapema Frontier](https://adoption.microsoft.com/copilot/frontier-program/) kwa usajili wa Microsoft 365 Copilot, na msimamizi wako lazima akamilishe usanidi. Kwa kuwa ni kipengele cha majaribio cha Frontier, uwezo unaweza kubadilika kwa wakati.

## Jaribio la Maarifa

Jaribu ufahamu wako kabla ya kuendelea kwenye somo lijalo.

**1. Ni lini wakala wa matumizi ya kompyuta aliyejikita kwenye kivinjari ni chaguo bora kuliko mtiririko wa kazi unaotumia API pekee?**

<details>
<summary>Jibu</summary>

Tumia wakala wa kivinjari wakati kazi inategemea kile kinachoonekana kwenye UI ya wavuti, tovuti haifichui API inayohitajika, au ukurasa hubadilika mara kwa mara kiasi kwamba mantiki ya API imara au vitambuzi vinaweza kukatika. Ikiwa API thabiti ipo kwa kazi ile ile, pendelea API kwa kuwa mara nyingi ni haraka, rahisi kujaribu, na rahisi kulinda.
</details>

**2. Katika mtiririko mchanganyiko, ni sehemu gani wakala anapaswa kushughulikia na ni sehemu gani msimbo wa Playwright wa moja kwa moja unapaswa kushughulikia?**

<details>
<summary>Jibu</summary>

Mwachilie wakala kushughulikia urambazaji usio na kikomo na hali za UI zinazobadilika, kama kupata ukurasa sahihi au kufunga madirisha ya matangazo yasiyotegemewa. Badilisha kwa udhibiti wa moja kwa moja wa Playwright wakati muundo wa ukurasa unajulikana na hatua inahitaji usahihi, kurudia, kusubiri, au uhakiki wa uhakika.
</details>

**3. Mfano wa Airbnb hupata orodha ambayo mtumiaji anaweza kutaka kuhifadhi. Nini kinapaswa kutokea kabla mtiririko wa kazi uingie, kuwasiliana na mwenyeji, au kukamilisha uhifadhi?**

<details>
<summary>Jibu</summary>

Mtiririko wa kazi unapaswa kusimama na kuomba idhini ya wazi kutoka kwa mtumiaji. Kabla ya kuuliza, unapaswa kuonyesha muhtasari wazi wa orodha iliyochaguliwa, URL ya sasa, bei, tarehe, na hatua inayokusudiwa. Kutafuta na kuchukua bei kunaweza kuwa huru; ufikiaji wa akaunti, ujumbe, manunuzi, na uhifadhi vinapaswa kuidhinishwa na mtumiaji.
</details>

**4. Ukurasa wa wavuti unaambia wakala kupuuza maelekezo yake ya awali, kutembelea tovuti nyingine, na kufichua nywila zilizohifadhiwa. Wakala anapaswa kutenda vipi na maandishi hayo?**

<details>
<summary>Jibu</summary>

Tachukue kama maudhui ya ukurasa yasiyoaminika, si maelekezo ya mtengenezaji au mtumiaji. Wakala anapaswa kubakia ndani ya kikoa na wigo wa kazi ulioruhusiwa, kukataa kufichua siri, na kuepuka kufuata maandishi yanayobadilisha lengo, kuzima kinga, au kumpeleka kwenye tovuti zisizohusiana.
</details>

**5. Ni ushahidi gani unaofaa kuhifadhi wakati wakala wa kivinjari anafanya kazi, na ni nini kinapaswa kuepukwa?**

<details>
<summary>Jibu</summary>

Hifadhi muhtasari wa hatua, nyakati, URL, maelezo ya kipengele kilichochaguliwa, matokeo ya uthibitisho, na kumbukumbu za picha ili mtiririko uweze kupitiwa. Epuka kuhifadhi nywila, maelezo ya malipo, vidakuzi vya kikao, data ya binafsi ghafi, au maudhui kamili ya ukurasa isipokuwa kuna sababu maalum ya uhifadhi na faragha.
</details>

## Rasilimali Zaidi

- [Anza na Mradi Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Kiolezo cha muunganisho wa Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Vigezo vya wakala wa Browser-Use na uchambuzi wa maudhui](https://docs.browser-use.com/customize/actor/all-parameters)
- [Usanidi wa Kozi](../00-course-setup/README.md)

## Somo lililopita

[Kuchunguza Mfumo wa Wakala wa Microsoft](../14-microsoft-agent-framework/README.md)

## Somo lijalo

[Kuweka Wakala Waliojipanua](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->