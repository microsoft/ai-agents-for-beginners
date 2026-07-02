# AI-agentit aloittelijoille - Opas

Käytä tätä opasta käytännön kumppanina kurssin aikana. Se ei ole tarkoitettu korvaamaan
oppitunteja. Se auttaa sinua päättämään, mistä aloittaa, mitä etsiä kussakin oppitunnissa ja
miten yhdistää ideat toimivaan agenttinäytökseen.

Jos olet täällä ensimmäistä kertaa, aloita yksinkertaisesti:

1. Lue [Kurssin aloitus](./00-course-setup/README.md).
2. Suorita oppitunnit 01-06 järjestyksessä.
3. Pidä mielessä yksi pieni demosovellus oppimisen aikana.
4. Jokaisen oppitunnin jälkeen kysy: "Mitä agenttini osaa nyt, mitä se ei pystynyt tekemään
   ennen?"

## Yksinkertainen demo, jonka voit pitää mielessä

Hyvä tapa oppia agenteista on seurata yhtä demoideaa koko kurssin ajan.

Esimerkkidemo: **kurssin apuagentti**.

Käyttäjä kysyy:

> "Haluan oppia, miten agentit käyttävät työkaluja. Etsi oikeat oppitunnit, tee yhteenveto siitä,
> mitä minun pitäisi lukea ensin, ja anna lyhyt harjoitustehtävä."

Tavallinen chatbot voi vastata siitä, mitä se jo tietää. Agentti voi tehdä enemmän:

1. **Lue tai etsi kurssitiedostoja** löytääksesi oikeat oppitunnit.
2. **Käytä työkaluja** hakeaksesi oppituntien linkkejä, esimerkkejä tai tukimateriaaleja.
3. **Suunnittele** lyhyt oppimispolku yhden pitkän vastauksen sijaan.
4. **Käytä kontekstia** nykyisestä keskustelusta pysyäksesi oppijan tavoitteessa.
5. **Muista hyödylliset mieltymykset**, jos sovellus tukee muistia.
6. **Näytä jäljet, lähteet tai lokit** niin käyttäjä ymmärtää, mitä tapahtui.
7. **Käytä suojalaitteita** ennen riskialttiita toimia tai arkaluontoisten tietojen käyttöä.

Kun opiskelet kutakin oppituntia, palaa tähän demoon ja kysy: mitä uutta ominaisuutta tämä oppitunti lisäisi?

## Mitä olet rakentamassa

Kurssin lopussa sinun tulisi osata selittää ja rakentaa agenttijärjestelmiä, jotka yhdistävät nämä osat:

| Osa | Selkokielinen merkitys | Demon kohdalla |
|------|------------------------|-------------|
| Malli | Päättelymoottori, joka tulkitsee käyttäjän pyyntöä | Ymmärtää, että oppija haluaa oppitunteja työkalujen käytöstä |
| Työkalut | Funktiot, API:t, tiedostot, selaimet tai palvelut, joita agentti voi käyttää | Tekee haun repossa tai hakee oppituntien sisältöä |
| Tieto | Dokumentit tai data, joita käytetään vastauksen perustana | Kurssin README-tiedostot ja oppimateriaali |
| Konteksti | Tieto, joka sisällytetään seuraavaan mallin kutsuun | Käyttäjän tavoite ja työkalun tulokset |
| Muisti | Tallennettu tieto myöhempää käyttöä varten | Oppija suosii käytännön Python-esimerkkejä |
| Suunnittelu | Suurempi tavoite pilkotaan pienempiin askeliin | Löytää oppitunnit, tiivistää ne, ehdottaa harjoituksia |
| Orkestrointi | Työ jakaantuu eri työkalujen, askelten tai agenttien kesken | Suunnittelija kutsuu hakutyökalun, sitten tiivistäjän |
| Luottamus | Turvallisuus, arviointi ja havaittavuus | Kirjaa työkalukutsut ja kysyy ennen suurivaikutteisia toimia |

## Valitse oppimispolkusi

Voit suorittaa koko kurssin järjestyksessä tai hypätä polulle sen mukaan, mitä haluat rakentaa.

| Jos tavoitteesi on... | Aloita | Sitten opiskele |
|-----------------------|------------|------------|
| Ymmärtää, mitä agentit ovat | 01, 02, 03 | 04, 05, 06 |
| Rakentaa agentin, joka käyttää työkaluja | 04 | 05, 07, 14 |
| Rakentaa RAG-pohjaisen agentin | 05 | 04, 06, 12 |
| Suunnitella monivaiheisia työnkulkuja | 07 | 08, 09, 14 |
| Ymmärtää moniagenttijärjestelmät | 08 | 07, 09, 11 |
| Valmistella agentteja tuotantoon | 06, 10 | 12, 13, 18 |
| Tutkia protokollia ja selainautomaatioita | 11, 15 | 10, 18 |

Vinkki: jos olet uusi agenteissa, älä ohita oppitunteja 01-06. Ne antavat sanaston, jota tarvitset koko kurssilla.

## Oppitunti kerrallaan -opas

| Oppitunti | Mitä opit | Kokeile tämän jälkeen |
|--------|----------------|---------------------------|
| [01 - Johdanto AI-agentteihin](./01-intro-to-ai-agents/README.md) | Mikä erottaa agentin peruschatbotista. | Selitä demosovelluksesi agenttina, ei vain chat-sovelluksena. |
| [02 - Agenttikehykset](./02-explore-agentic-frameworks/README.md) | Miten kehykset auttavat mallien, työkalujen, tilan ja työnkulkujen hallinnassa. | Tunnista, mitkä osat demossasi hoitaisi kehys. |
| [03 - Agenttisuunnittelumallit](./03-agentic-design-patterns/README.md) | Yleisiä malleja agentin käyttäytymisen suunnitteluun. | Laadi käyttäjäpolku ennen koodin kirjoittamista. |
| [04 - Työkalujen käyttö](./04-tool-use/README.md) | Miten agentit kutsuvat työkaluja saadakseen dataa tai tehdäkseen toimia. | Määrittele yksi työkalu, jota demosovelluksesi agentti tarvitsee. |
| [05 - Agenttinen RAG](./05-agentic-rag/README.md) | Miten haku pohjaa agentin vastaukset dokumentteihin tai dataan. | Päätä, mitä tietolähdettä demon tulisi käyttää haussa. |
| [06 - Luotettavat agentit](./06-building-trustworthy-agents/README.md) | Miten lisätään suojauksia, valvontaa ja turvallisempaa käyttäytymistä. | Lisää yksi sääntö, jolloin agentin tulisi ensin kysyä käyttäjältä. |
| [07 - Suunnittelun suunnittelu](./07-planning-design/README.md) | Miten agentit pilkkovat suuremmat tavoitteet pienemmiksi askeleiksi. | Kirjoita kolmivaiheinen suunnitelma demopyynnöllesi. |
| [08 - Moniagenttisuunnittelu](./08-multi-agent/README.md) | Milloin työ tulisi jakaa erikoistuneille agenteille. | Päätä tarvitsetko demoon yhden vai useamman agentin. |
| [09 - Metakognitio](./09-metacognition/README.md) | Miten agentit voivat tarkistaa ja parantaa omaa tuotostaan. | Lisää loppukäteinen itsearviointi ennen agentin vastausta. |
| [10 - AI-agentit tuotannossa](./10-ai-agents-production/README.md) | Mitä muuttuu, kun agentti siirtyy demonsta tuotantoon. | Listaa, mitä seuraisit: laatua, kustannuksia, viivettä, virheitä. |
| [11 - Agenttiset protokollat](./11-agentic-protocols/README.md) | Miten protokollat yhdistävät agentit työkaluihin ja muihin agenteihin. | Tunnista, missä standardiprotokolla voisi yksinkertaistaa integraatiota. |
| [12 - Kontekstisuunnittelu](./12-context-engineering/README.md) | Miten valitaan, rajataan, erotetaan ja hallitaan kontekstia. | Päätä, mikä kuuluu kehotteeseen ja mikä jätetään pois. |
| [13 - Agentin muisti](./13-agent-memory/README.md) | Miten agentit voivat tallentaa hyödyllistä tietoa vuorovaikutusten yli. | Valitse yksi turvallinen mieltymys, jonka demon voisi muistaa. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Kehykseen liittyvät rakennuspalikat agenteille ja työnkuluille. | Yhdistä demosovelluksesi vaiheet kehyskonsepteihin. |
| [15 - Tietokoneen käyttöagentit](./15-browser-use/README.md) | Miten agentit voivat olla vuorovaikutuksessa selaimen tai käyttöliittymän kanssa. | Valitse selaintehtävä, joka vaatii silti käyttäjän vahvistuksen. |
| [18 - AI-agenttien turvallistaminen](./18-securing-ai-agents/README.md) | Miten agenttitoimia voidaan tehdä tarkemmin auditoitaviksi ja väärinkäytöksiä estäviksi. | Päätä, mitkä demon toimet tulisi kirjata tai kuittaa. |

Oppitunnit 16 ja 17 mainitaan pää-README:ssa tulossa pian. Lisää ne opiskelusuunnitelmaasi, kun oppimateriaali on saatavilla.

## Keskeiset ideat aloittelijaystävällisesti

### Työkalut

Työkalu on jotain, jota agentti voi kutsua tehdäkseen työtä mallin ulkopuolella. Hyvä työkalu
on nimeltään selkeä, tekee kapean tehtävän, ottaa tyypitetyt syötteet, tuottaa ennakoitavan tuloksen
ja epäonnistuu turvallisesti.

Kurssin apuagentin työkalut voivat olla esimerkiksi:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG ja tieto

RAG auttaa agenttia vastaamaan lähdemateriaaleihin perustuen epävarmuuden sijaan. Tässä
kurssissa lähdemateriaali voi olla oppituntien README-tiedostot, koodiesimerkit tai ulkoiset
resurssit, joihin oppitunnit linkittävät.

Käytä RAGia, kun vastaus tulee perustua dokumentteihin, dataan tai tämänhetkisiin projektitiedostoihin.

### Suunnittelu

Suunnitelma on hyödyllinen, kun pyyntö sisältää useamman vaiheen. Pidä suunnitelmat lyhyinä
ja näkyvinä niin, että kehittäjä tai käyttäjä voi tarkastella niitä.

Demossa suunnitelma voisi olla:

1. Etsi oppitunnit, jotka liittyvät työkalujen käyttöön.
2. Tiivistä asiaankuuluvat oppitunnit.
3. Suosittele yksi harjoitustehtävä.

### Konteksti

Konteksti on se, mitä malli näkee juuri nyt. Liian vähän kontekstia voi aiheuttaa, että agentti
jättää huomiotta tärkeät yksityiskohdat. Liian paljon kontekstia voi tehdä agentista hitaamman,
kalliimman tai helpommin sekoitettavan.

Hyvä kontekstisuunnittelu tarkoittaa oikean tiedon valintaa seuraavaan mallin kutsuun.

### Muisti

Muisti on myöhempää käyttöä varten tallennettua tietoa. Älä tallenna kaikkea. Tallenna tietoa
vain, kun se on hyödyllistä, turvallista ja helppoa päivittää tai poistaa.

Esimerkiksi, muistaa että "oppija suosii Python-esimerkkejä" voi olla hyödyllistä. Henkilökohtaisten
arkaluontoisten tietojen muistaminen ei yleensä ole.

### Arviointi ja havaittavuus

Arviointi kysyy: tekikö agentti oikean asian?

Havaittavuus kysyy: näemmekö, miten se tapahtui?

Tuotantoagenttien tapauksessa seuraa mallikutsuja, työkalukutsuja, haettua kontekstia,
viivettä, kustannuksia, virheitä ja käyttäjäpalautetta.

### Luottamus ja turvallisuus

Luotettavat agentit tarvitsevat enemmän kuin avuliaan kehotteen. Käytä vähimmän oikeuden työkaluja,
ihmishyväksyntää suurissa vaikutuksissa, tietojen suodatusta tarpeen mukaan, sekä lokeja tai kuitteja
toimille, jotka tulee tarkastaa.

## 15 minuutin kertausrutiini

Käytä tätä rutiinia jokaisen oppitunnin jälkeen:

1. **Yhteenvedä oppitunti yhdellä lauseella.**
2. **Nimeä uusi agentin kyky.** Esimerkiksi: työkalun käyttö, haku, suunnittelu, muisti,
   havaittavuus tai turvallisuus.
3. **Lisää se kurssin apuagentti-demoosi.** Mitä nyt muuttuu demossa?
4. **Löydä riski.** Mitä voi mennä pieleen, jos tätä kykyä käytetään väärin?
5. **Kirjoita yksi testikysymys.** Kuinka tarkistat, että agentti käyttäytyy oikein?

## Pikainen itsearviointi

Ennen jatkamista, vastaa näihin kysymyksiin:

1. Mitä agentti voi tehdä, mitä tavallinen chatbot ei pysty tekemään yksin?
2. Mikä työkalu agenttisi tarvitsee ensin ja miksi?
3. Mikä tietolähde pitäisi toimia agentin vastauksen perustana?
4. Mikä konteksti tulisi sisällyttää seuraavaan mallin kutsuun?
5. Mitä agentin pitäisi muistaa ja mitä välttää tallentamasta?
6. Milloin agentin tulisi pyytää ihmisen hyväksyntää?
7. Mitkä lokit, jäljet tai kuitit auttaisivat sinua myöhemmin virheiden korjauksessa tai auditoinnissa?

## Ehdotettu loppuharjoitus

Kurssin lopussa rakenna pieni agentti, joka auttaa oppijaa navigoimaan tässä repossa.

Minimiversio:

- Hyväksyy käyttäjältä aiheen.
- Löytää relevantit oppitunnit.
- Tiivistää, mitä lukea ensin.
- Ehdottaa yhden käytännön harjoitustehtävän.
- Näyttää, mitä oppituntien tiedostoja tai linkkejä käytettiin.

Laajennettu versio:

- Muistaa oppijan suosiman ohjelmointikielen.
- Käyttää yksinkertaista suunnitelmaa ennen vastaamista.
- Lisää itsearviointivaiheen ennen lopullista vastausta.
- Kirjaa työkalukutsut ja haetut lähteet.
- Kysyy vahvistuksen ennen selaimen tai käyttöliittymäautomaation käynnistämistä.

Tämä antaa sinulle pienen mutta realistisen tavan harjoitella työkaluja, RAGia, suunnittelua,
kontekstia, muistia, havaittavuutta ja luottamusta samassa projektissa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->