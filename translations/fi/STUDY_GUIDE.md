# AI-agentit aloittelijoille - Opas

Käytä tätä opasta käytännön kumppanina kurssin aikana. Se ei
ole tarkoitettu korvaamaan oppitunteja. Se auttaa sinua päättämään mistä aloittaa, mitä
etsiä jokaisesta oppitunnista ja miten yhdistää ideat pieneksi toimivaksi agenttidemoksi.


Jos olet täällä ensimmäistä kertaa, aloita yksinkertaisesti:

1. Lue [Kurssin aloitus](./00-course-setup/README.md).
2. Suorita Oppitunnit 01-06 järjestyksessä.
3. Pidä mielessäsi yksi pieni demointi-idea oppimisen aikana.
4. Jokaisen oppitunnin jälkeen kysy: "Mitä agenttini osaa nyt, mitä se ei
   osannut ennen?"

## Yksinkertainen demo, joka kannattaa pitää mielessä

Hyvä tapa oppia agentteja on seurata yhtä demo-ideaa koko kurssin ajan.

Esimerkkidemo: **kurssiavustaja-agentti**.

Käyttäjä kysyy:

> "Haluan oppia, miten agentit käyttävät työkaluja. Löydä oikeat oppitunnit,
> tiivistä, mitä minun pitäisi ensin lukea, ja anna minulle lyhyt harjoitustehtävä."

Tavallinen chatbot voi vastata siitä, mitä se jo tietää. Agentti pystyy enemmän:

1. **Lue tai hae kurssitiedostoista** löytääksesi oikeat oppitunnit.
2. **Käytä työkaluja** hakeaksesi oppituntien linkkejä, esimerkkejä tai tukimateriaalia.
3. **Suunnittele** lyhyt oppimispolku yhden pitkän vastauksen sijaan.
4. **Käytä kontekstia** nykyisestä keskustelusta pysyäksesi keskittyneenä oppijan
   tavoitteeseen.
5. **Muista hyödylliset mieltymykset**, jos sovellus tukee muistia.
6. **Näytä jäljet, lähteet tai lokit** jotta käyttäjä voi ymmärtää, mitä tapahtui.
7. **Käytä suojaimia** ennen riskialttiita toimia tai arkaluonteisten tietojen käyttöä.

Kun opiskelet kutakin oppituntia, palaa tähän demoon ja kysy: mitä uutta
ominaisuutta tämä oppitunti lisäisi?

## Mitä olet rakentamassa kohti

Kurssin loppuun mennessä sinun pitäisi pystyä selittämään ja rakentamaan agenttijärjestelmiä,
jotka yhdistävät nämä osat:

| Osa | Arkikielinen merkitys | Demossa |
|------|------------------------|-------------|
| Malli | Päättelymoottori, joka tulkitsee käyttäjän pyyntöä | Ymmärtää, että oppija haluaa oppitunteja työkalujen käytöstä |
| Työkalut | Funktiot, API:t, tiedostot, selaimet tai palvelut, joita agentti voi käyttää | Hakee reposta tai noutaa oppituntien sisältöä |
| Tieto | Asiakirjat tai data, joita käytetään vastausten pohjana | Kurssin README-tiedostot ja oppimateriaali |
| Konteksti | Se tieto, joka sisällytetään seuraavaan mallikutsuun | Käyttäjän tavoite ja työkalujen tulokset |
| Muisti | Tallennettu tieto myöhempää käyttöä varten | Oppija suosii käytännön Python-esimerkkejä |
| Suunnittelu | Suuremman tavoitteen jakaminen pienempiin askeliin | Löytää oppitunnit, tiivistää ne, ehdottaa harjoitusta |
| Orkestrointi | Työn ohjaaminen työkalujen, askelten tai agenttien välillä | Suunnittelija kutsuu hakutyökalun, sitten tiivistäjän |
| Luottamus | Turvallisuus, arviointi ja valvottavuus | Kirjaa työkalukutsut ja kysyy ennen suurvaikutteisia toimia |

## Malleja ja tarjoajia

Kurssin koodiesimerkit käyttävät **Microsoft Agent Frameworkia (MAF)** ja kohdistuvat **Azure OpenAI Responses APIin** — suositeltuun APIin jatkossa, joka yhdistää keskustelun täydentämisen, työkalukutsut, multimodaalisen syötteen ja tilalliset keskustelut yhdeksi API-rajapinnaksi. Yhdistät joko **Microsoft Foundry** -projektiin (käyttäen `FoundryChatClient`) tai suoraan Azure OpenAI:hin (käyttäen `OpenAIChatClient`).

Opintojen aikana sinulla on muutama tarjoajavaihtoehto:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — pääasiallinen polku, jota käytetään kursseilla. Kirjaudu sisään `az login`-menetelmällä avaimettomaan Entra ID -tunnistukseen.
- **Foundry Local** — suorita mallit kokonaan laitteellasi avoimen OpenAI-yhteensopivan API:n kautta (ei pilveä, ei API-avaimia). Ihanteellinen offline- tai ilmaiseksi kokeiluun. Katso [Kurssin asennus](./00-course-setup/README.md).
- **MiniMax** — OpenAI-yhteensopiva tarjoaja laajakontekstisilla malleilla, käytettävissä korvaavana vaihtoehtona.

> **Huom:** GitHub Models on vanhentunut (lopetetaan heinäkuussa 2026) eikä tue Responses APIa. Esimerkit on päivitetty käyttämään Azure OpenAIta / Microsoft Foundrya sen sijaan.

## Valitse oppimispolkusi

Voit käydä koko kurssin läpi järjestyksessä tai hypätä suoraan polulle sen mukaan, mitä haluat
rakentaa.

| Jos tavoitteesi on... | Aloita kohteesta | Sitten opiskele |
|-----------------------|------------|------------|
| Ymmärtää, mitä agentit ovat | 01, 02, 03 | 04, 05, 06 |
| Rakentaa agentti, joka käyttää työkaluja | 04 | 05, 07, 14 |
| Rakentaa RAG-pohjaisen agentin | 05 | 04, 06, 12 |
| Suunnitella monivaiheisia työnkulkuja | 07 | 08, 09, 14 |
| Ymmärtää moniesagenttijärjestelmät | 08 | 07, 09, 11 |
| Valmistella agentteja tuotantoon | 06, 10 | 12, 13, 16, 18 |
| Ota agentit käyttöön ja skaalaa Foundryssä | 10, 16 | 06, 13, 18 |
| Rakenna paikallisia / offline-ensimmäisiä agentteja | 17 | 04, 05, 11 |
| Tutki protokollia ja selaimen automaatiota | 11, 15 | 10, 18 |

Vinkki: jos olet uusi agenteissa, älä ohita oppitunteja 01-06. Ne antavat sinulle
sanaston, jota tarvitset kurssin loppuosassa.

## Oppitunti oppitunnilta -opas

| Oppitunti | Mitä opit | Kokeile tämän jälkeen |
|--------|----------------|---------------------------|
| [01 - Johdatus AI-agentteihin](./01-intro-to-ai-agents/README.md) | Mikä erottaa agentin tavallisesta chatbottista. | Selitä demon ideasi agenttina, ei pelkkänä keskustelusovelluksena. |
| [02 - Agenttikehykset](./02-explore-agentic-frameworks/README.md) | Miten kehykset auttavat malleissa, työkaluissa, tilassa ja työnkuluissa. | Tunnista, mitkä osat demon hallinnasta olisi kehys hallitsemassa. |
| [03 - Agenttisuunnittelumallit](./03-agentic-design-patterns/README.md) | Yleisiä malleja agentin käyttäytymisen suunnitteluun. | Laadi käyttäjämatka ennen koodin kirjoittamista. |
| [04 - Työkalujen käyttö](./04-tool-use/README.md) | Miten agentit kutsuvat työkaluja saadakseen tietoa tai toimiakseen. | Määrittele yksi työkalu, jota demon agentti tarvitsee. |
| [05 - Agenttinen RAG](./05-agentic-rag/README.md) | Miten haku perustaa agentin vastaukset dokumentteihin tai dataan. | Päätä, mitä tietolähdettä demon tulisi käyttää haussa. |
| [06 - Luotettavat agentit](./06-building-trustworthy-agents/README.md) | Miten lisätään suojakaiteita, valvontaa ja turvallisempaa käyttäytymistä. | Lisää sääntö siitä, milloin agentin tulee kysyä ensin käyttäjältä. |
| [07 - Suunnittelun rakenne](./07-planning-design/README.md) | Miten agentit pilkkovat suuremmat tavoitteet pienemmiksi askeliksi. | Laadi kolmen vaiheen suunnitelma demon pyynnölle. |
| [08 - Moni-agenttisuunnittelu](./08-multi-agent/README.md) | Milloin työ jaetaan erikoistuneille agenteille. | Päätä, tarvitseeko demon agentti yhden vai useamman agentin. |
| [09 - Metakognitio](./09-metacognition/README.md) | Miten agentit voivat arvioida ja parantaa omaa tuotostaan. | Lisää viimeinen itsearviointi ennen kuin agentti vastaa. |
| [10 - AI-agentit tuotannossa](./10-ai-agents-production/README.md) | Mitä muuttuu, kun agentti siirtyy demonsta tuotantoon. | Listaa, mitä seuraat: laatu, kustannukset, viive, virheet. |
| [11 - Agenttiprotocollet](./11-agentic-protocols/README.md) | Miten protokollat yhdistävät agentit työkaluihin ja muihin agentteihin. | Tunnista kohta, jossa vakio-protokolla helpottaisi integraatiota. |
| [12 - Kontekstisuunnittelu](./12-context-engineering/README.md) | Miten valitaan, rajataan, eristetään ja hallitaan kontekstia. | Päätä, mikä kuuluu kehotteeseen ja mikä ei. |
| [13 - Agentin muisti](./13-agent-memory/README.md) | Miten agentit voivat tallentaa hyödyllistä tietoa eri vuorovaikutuksissa. | Valitse yksi turvallinen mieltymys, jonka demo voisi muistaa. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Kehyskohtaisten rakennuspalikoiden käyttö agenteissa ja työnkuluissa sekä LangChain/LangGraph-agenttien hostaus Microsoft Foundryssä. | Sijoita demoaskelmat kehyskonsepteihin. |
| [15 - Tietokonekäyttöagentit](./15-browser-use/README.md) | Miten agentit voivat olla vuorovaikutuksessa selaimen tai käyttöliittymän kanssa, mukaan lukien oikean maailman esimerkkejä kuten Microsoft Project Opal. | Valitse yksi selaintehtävä, joka vaatii edelleen käyttäjän vahvistuksen. |
| [16 - Skaalautuvien agenttien käyttöönotto](./16-deploying-scalable-agents/README.md) | Miten agentti siirretään prototyypistä skaalautuvaan, havaittavaan tuotantokäyttöön Microsoft Foundryssä (isännöidyt agentit, mallin reititys, välimuisti, arviointipisteet, savutestit). | Listaa tuotantoon liittyvät asiat, joita demossasi vielä tarvitaan: hosting, reititys, kustannukset, arviointi. |
| [17 - Paikallisten AI-agenttien luominen](./17-creating-local-ai-agents/README.md) | Miten rakentaa paikallisesti toimivia agentteja, jotka suoritetaan kokonaan koneellasi Foundry Localin ja Qwenin avulla (paikalliset työkalut, paikallinen RAG, paikallinen MCP). | Päätä, mitkä demon osat säilyvät yksityisinä ja toimivat paikallisesti. |
| [18 - AI-agenttien suojaaminen](./18-securing-ai-agents/README.md) | Miten agenttitoimia tehdään helpommin auditoitaviksi ja manipulointia kestäviksi. | Päätä, mitkä demosi toimet tulisi lokittaa tai vastaanottaa. |

## Käyttöönotettujen agenttien validointi savutesteillä

Kun otat agentin käyttöön (oppitunti 16), **savutesti** on halvin ensimmäinen
tarkistus siitä, että käyttöönotto todella vastaa. Tämä repositorio sisältää valmiiksi ajettavat
luettelot kansiossa [tests/](./tests/README.md) käyttöönotettaville agenteille oppitunneilla
01, 04, 05 ja 16, jotka on liitetty
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Toimintoon. Suorita ne **Actions**-välilehdeltä oppitunnin agentin käyttöönoton jälkeen.
Savutestit ovat ensimmäinen portti — offline- ja online-arviointi (oppitunnit 10 ja 16)
kertovat, kuinka *hyvä* agentti on.

## Tärkeitä ideoita aloittelijaystävällisesti

### Työkalut

Työkalu on jotain, mitä agentti voi kutsua tehdäkseen töitä mallin ulkopuolella. Hyvällä työkalulla
on selvä nimi, kapea tehtävä, tyypitetyt syötteet, ennustettava tulos ja turvallinen tapa
epäonnistua.

Kurssiavustajan demon kohdalla työkalu voisi olla:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG ja tieto

RAG auttaa agenttia vastaamaan lähdemateriaalin perusteella arvaamisen sijaan. Tässä
kurssissa lähdemateriaali voi olla oppituntien README-tiedostoja, koodiesimerkkejä tai ulkoisia
resursseja, joihin viitataan oppitunneilla.

Käytä RAGia, kun vastaus tulisi perustua dokumentteihin, dataan tai ajankohtaisiin
projektitiedostoihin.

### Suunnittelu

Suunnittelu on hyödyllistä, kun pyyntöön liittyy useampia vaiheita. Pidä suunnitelmat lyhyinä ja
riittävän näkyvinä kehittäjän tai käyttäjän tarkasteltavaksi.

Demon kohdalla suunnitelma voisi olla:

1. Etsi oppitunnit, jotka käsittelevät työkalujen käyttöä.
2. Tiivistä asiaankuuluvat oppitunnit.
3. Suosittele yksi harjoitustehtävä.

### Konteksti

Konteksti on se, mitä malli näkee juuri nyt. Liian vähän kontekstia voi saada agentin
missaamaan tärkeitä yksityiskohtia. Liian paljon kontekstia voi tehdä agentista hitaamman, kalliimman
tai helpommin sekaisin menevän.

Hyvä kontekstisuunnittelu tarkoittaa oikean tiedon valitsemista seuraavaa mallikutsua varten.




vain silloin kun se on hyödyllistä, turvallista ja helppoa päivittää tai poistaa.


Henkilökohtaisten arkaluontoisten tietojen muistaminen yleensä ei ole.








viivettä, kustannuksia, virheitä ja käyttäjäpalautetta.




ihmisen hyväksyntää korkean vaikutuksen toimiin, tietojen suodatusta tarvittaessa, sekä lokitusta tai
kuittauksia toimiin, jotka on auditoitava.






2. **Nimeä uusi agenttikyky.** Esimerkiksi: työkalujen käyttö, haku,
   suunnittelu, muisti, havaittavuus tai turvallisuus.
3. **Lisää se kurssiavustajan demoon.** Mitä muutoksia demon toimintaan tulee nyt?
4. **Löydä riski.** Mikä voisi mennä pieleen, jos tätä kykyä käytetään väärin?
5. **Kirjoita yksi testikysymys.** Miten tarkistat, että agentti käyttäytyy hyvin?






2. Mitä työkalua agenttisi tarvitsisi ensin ja miksi?
3. Minkä tietolähteen pitäisi perustaa agentin vastaus?
4. Mikä konteksti tulisi sisällyttää seuraavaan mallikutsuun?
5. Mitä agentin pitäisi muistaa ja mitä sen tulisi välttää tallentamasta?
6. Milloin agentin pitäisi pyytää ihmisen hyväksyntää?
7. Mitkä lokit, jäljet tai kuitit auttaisivat sinua virheenetsinnässä tai auditoinnissa myöhemmin?




Kurssin lopussa rakenna pieni agentti, joka auttaa oppijaa navigoimaan tässä
repositoriossa.

Minimiversio:

- Hyväksyy käyttäjältä aiheen.
- Löytää aiheeseen relevanttimmat oppitunnit.
- Tiivistää, mitä lukea ensin.
- Ehdottaa yhden käytännön harjoitustehtävän.
- Näyttää, mitä oppituntitiedostoja tai linkkejä käytettiin.

Laajennettu versio:

- Muistaa oppijan mieluisan ohjelmointikielen.
- Käyttää yksinkertaista suunnitelmaa ennen vastaamista.
- Lisää itsearviointivaiheen ennen lopullista vastausta.
- Kirjaa työkalukutsut ja haetut lähteet.
- Kysyy vahvistuksen ennen selaimen tai käyttöliittymäautomaation käynnistämistä.

Tämä tarjoaa pienen mutta realistisen tavan harjoitella työkaluja, RAG:ia, suunnittelua,
kontekstia, muistia, havainnointia ja luottamusta yhdessä projektissa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->