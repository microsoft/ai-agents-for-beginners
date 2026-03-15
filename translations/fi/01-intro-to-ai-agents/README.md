[![Johdatus tekoälyagentteihin](../../../translated_images/fi/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikkaa yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_


# Johdatus tekoälyagentteihin ja agenttien käyttötapauksiin

Tervetuloa "AI Agents for Beginners" -kurssille! Tämä kurssi tarjoaa perustiedot ja käytännön esimerkit tekoälyagenttien rakentamiseen.

Liity <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord -yhteisö</a> tapaamaan muita oppijoita ja tekoälyagenttien rakentajia sekä esittämään kaikki kurssiin liittyvät kysymyksesi.

Aloittaaksemme tämän kurssin käymme ensin läpi, mitä tekoälyagentit ovat ja miten voimme käyttää niitä rakentamissamme sovelluksissa ja työnkuluissa.

## Johdanto

Tässä oppitunnissa käsitellään:

- Mitä tekoälyagentit ovat ja mitkä ovat eri agenttityypit?
- Missä käyttötapauksissa tekoälyagentit sopivat parhaiten ja miten ne voivat auttaa meitä?
- Mitkä ovat agenttipohjaisten ratkaisujen perusrakennuspalikat suunnittelussa?

## Oppimistavoitteet
Tämän oppitunnin jälkeen sinun pitäisi osata:

- Ymmärtää tekoälyagenttien käsitteet ja kuinka ne eroavat muista tekoälyratkaisuista.
- Soveltaa tekoälyagentteja mahdollisimman tehokkaasti.
- Suunnitella agenttipohjaisia ratkaisuja tuottavasti sekä käyttäjille että asiakkaille.

## Tekoälyagenttien määrittely ja agenttityypit

### Mitä ovat tekoälyagentit?

Tekoälyagentit ovat **järjestelmiä** jotka antavat **Large Language Models(LLMs)** suorittaa **toimintoja** laajentamalla niiden kyvykkyyksiä antamalla LLMs **pääsyn työkaluihin** ja **tietämykseen**.

Pilkotaan tätä määritelmää pienempiin osiin:

- **Järjestelmä** - On tärkeää ajatella agentteja ei pelkästään yhtenä komponenttina vaan monen komponentin järjestelmänä. Perustasolla tekoälyagentin komponentit ovat:
  - **Ympäristö** - Määritelty tila, jossa tekoälyagentti toimii. Esimerkiksi, jos meillä olisi matkavarauksen tekoälyagentti, ympäristö voisi olla matkavarauksia käsittelevä järjestelmä, jota agentti käyttää tehtävien suorittamiseen.
  - **Anturit** - Ympäristöllä on tietoa ja se antaa palautetta. Tekoälyagentit käyttävät antureita kerätäkseen ja tulkitakseen tietoa ympäristön nykytilasta. Matkavarauksen agentin esimerkissä varausjärjestelmä voi antaa tietoja, kuten hotellien saatavuudesta tai lentojen hinnoista.
  - **Toimilaitteet** - Kun tekoälyagentti saa tiedon ympäristön nykytilasta, se päät�ttää kulloista tehtävää varten, mitä toimenpidettä suoritetaan ympäristön muuttamiseksi. Matkavarauksen agentin tapauksessa se saattaa varata käyttäjälle saatavilla olevan huoneen.

![Mitä ovat tekoälyagentit?](../../../translated_images/fi/what-are-ai-agents.1ec8c4d548af601a.webp)

**Suurten kielimallien** - Agenttien käsite oli olemassa ennen LLM:ien syntyä. LLM:ien käyttö agenttien rakentamisessa on hyödyllistä niiden kyvyn ansiosta tulkita ihmiskieltä ja dataa. Tämä kyky mahdollistaa LLM:ien ympäristötiedon tulkinnan ja suunnitelman laatimisen ympäristön muuttamiseksi.

**Toimintojen suorittaminen** - Tavanomaisissa järjestelmissä LLM:t rajoittuvat tilanteisiin, joissa toiminto on sisällön tai tiedon tuottaminen käyttäjän kehotteen perusteella. Agenttijärjestelmissä LLM:t voivat suorittaa tehtäviä tulkitsemalla käyttäjän pyynnön ja käyttämällä ympäristössä saatavilla olevia työkaluja.

**Pääsy työkaluihin** - Mitkä työkalut LLM:llä on käytettävissään määräytyy 1) siinä ympäristössä, jossa se toimii ja 2) tekoälyagentin kehittäjän mukaan. Matkavarausesimerkissämme agentin työkalut rajoittuvat varausjärjestelmän tarjoamiin toimintoihin, ja/tai kehittäjä voi rajata agentin työkalukäyttöä esimerkiksi vain lentoihin.

**Muisti ja tietämys** - Muisti voi olla lyhytaikaista käyttäjän ja agentin välisen keskustelun kontekstissa. Pitkäaikaisesti, ympäristön antaman tiedon lisäksi, tekoälyagentit voivat hakea tietoa muista järjestelmistä, palveluista, työkaluista ja jopa muilta agenteilta. Matkavarausesimerkissä tämä tietämys voi olla käyttäjän matkustusehtoja koskevaa tietoa asiakasrekisterissä.

### Eri agenttityypit

Nyt kun meillä on yleinen määritelmä tekoälyagenteista, tarkastellaan joitain erityisiä agenttityyppejä ja miten niitä sovellettaisiin matkavarausagentin tapauksessa.

| **Agenttityyppi**            | **Kuvaus**                                                                                                                            | **Esimerkki**                                                                                                                                                                                                                 |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Yksinkertaiset refleksiagentit**      | Suorittavat välittömiä toimintoja ennalta määriteltyjen sääntöjen perusteella.                                                                                  | Matkavarauksen agentti tulkitsee sähköpostin kontekstin ja välittää matkaan liittyvät valitukset asiakaspalveluun.                                                                                                                          |
| **Mallipohjaiset refleksiagentit** | Suorittavat toimintoja maailman mallin ja mallin muutosten perusteella.                                                              | Matkavarauksen agentti priorisoi reittejä, joissa on merkittäviä hintamuutoksia, hyödyntäen historiallisia hintatietoja.                                                                                                             |
| **Tavoitepohjaiset agentit**         | Laativat suunnitelmia tiettyjen tavoitteiden saavuttamiseksi tulkitsemalla tavoitteen ja määrittämällä toimenpiteet sen saavuttamiseksi.                                  | Matkavarauksen agentti varaa matkan määrittämällä tarvittavat matkajärjestelyt (auto, joukkoliikenne, lennot) nykyisestä sijainnista määränpäähän.                                                                                |
| **Hyötypohjaiset agentit**      | Ottavat huomioon mieltymykset ja punnitsevat kompromisseja numeerisesti päättääkseen, miten tavoitteet saavutetaan.                                               | Matkavarauksen agentti maksimoi hyödyn punnitsemalla mukavuuden ja kustannusten välistä suhdetta matkaa varatessaan.                                                                                                                                          |
| **Oppivat agentit**           | Parantavat toimintaansa ajan myötä reagoimalla palautteeseen ja säätämällä toimintojaan sen mukaan.                                                        | Matkavarauksen agentti kehittyy käyttämällä asiakaspalautetta matkan jälkeisistä kyselyistä tehdäkseen muutoksia tuleviin varauksiin.                                                                                                               |
| **Hierarkkiset agentit**       | Sisältävät useita agentteja porrastetussa järjestelmässä, jossa korkeamman tason agentit jakavat tehtäviä alempien tasojen agenteille. | Matkavarauksen agentti peruu matkan jakamalla tehtävän osatehtäviin (esimerkiksi peruen yksittäisiä varauksia), jonka alemmat agentit suorittavat ja raportoivat takaisin korkeamman tason agentille.                                     |
| **Moniagenttijärjestelmät (MAS)** | Agentit suorittavat tehtäviä itsenäisesti, joko yhteistyössä tai kilpailullisesti.                                                           | Yhteistyössä: Useat agentit varaavat erilaisia matkpalveluja, kuten hotelleja, lentoja ja viihdettä. Kilpailutilanteessa: Useat agentit hallinnoivat ja kilpailevat jaetusta hotellivarauksen kalenterista varatakseen asiakkaita hotelliin. |

## Milloin käyttää tekoälyagentteja

Edellisessä osiossa käytimme matkavarausesimerkkiä selittämään, miten eri agenttityyppejä voidaan käyttää erilaisissa matkavarauksen tilanteissa. Jatkamme tämän sovelluksen käyttöä koko kurssin ajan.

Katsotaan, millaisiin käyttötapauksiin tekoälyagentit soveltuvat parhaiten:

![Milloin käyttää tekoälyagentteja?](../../../translated_images/fi/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Avoimet ongelmat** - antaa LLM:lle mahdollisuuden määrittää tarvittavat vaiheet tehtävän suorittamiseksi, koska niitä ei aina voi kovakoodata työnkulkuun.
- **Monivaiheiset prosessit** - tehtävät, jotka vaativat sellaisen monimutkaisuuden, että agentin täytyy käyttää työkaluja tai tietoa useiden vuorojen aikana yksittäisen haun sijaan.  
- **Parantuminen ajan myötä** - tehtävät, joissa agentti voi kehittyä ajan myötä saamalla palautetta joko ympäristöstä tai käyttäjiltä tarjotakseen paremman hyödyn.

Käsittelemme lisää tekoälyagenttien käytön huomioon otettavia seikkoja Oppitunnissa "Building Trustworthy AI Agents".

## Agenttipohjaisten ratkaisujen perusteet

### Agentin kehittäminen

Ensimmäinen vaihe tekoälyagenttijärjestelmän suunnittelussa on määrittää työkalut, toiminnot ja käyttäytymiset. Tässä kurssissa keskitymme käyttämään **Azure AI Agent Service** -palvelua agenttien määrittelyyn. Se tarjoaa ominaisuuksia, kuten:

- Avoimien mallien valinta, kuten OpenAI, Mistral ja Llama
- Lisensoidun datan käyttö palveluntarjoajien kautta, esimerkiksi Tripadvisor
- Standardoitujen OpenAPI 3.0 -työkalujen käyttö

### Agenttipatternit

Viestintä LLM:ien kanssa tapahtuu kehotteiden avulla. Agenttien puoliksi itsenäisen luonteen vuoksi ei aina ole mahdollista tai tarpeellista kehottaa LLM:ää uudelleen käsin ympäristön muutoksen jälkeen. Käytämme **agenttipatterneja**, jotka sallivat LLM:ien kehotteistamisen useassa vaiheessa skaalautuvammalla tavalla.

Tämä kurssi on jaoteltu joidenkin nykyisten suosittujen agenttipatternien mukaan.

### Agenttikehykset

Agenttikehykset antavat kehittäjille mahdollisuuden toteuttaa agenttipatternit koodin avulla. Nämä kehykset tarjoavat malleja, liitännäisiä ja työkaluja paremman tekoälyagenttien yhteistyön mahdollistamiseksi. Nämä edut tarjoavat paremmat mahdollisuudet observoitavuuteen ja vianetsintään tekoälyagenttijärjestelmissä.

Tässä kurssissa tutkimme Microsoft Agent Frameworkia (MAF) tuotantovalmiiden tekoälyagenttien rakentamista varten.

## Esimerkkikoodit

- Python: [Agenttikehys](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agenttikehys](./code_samples/01-dotnet-agent-framework.md)

## Onko sinulla lisää kysymyksiä tekoälyagenteista?

Liity [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) tapaamaan muita oppijoita, osallistumaan toimistoaikoihin ja saadaksesi vastauksia tekoälyagentteja koskeviin kysymyksiisi.

## Edellinen oppitunti

[Kurssin asetukset](../00-course-setup/README.md)

## Seuraava oppitunti

[Agenttikehysten tutkiminen](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastuuvapauslauseke:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää määräysvaltaisena lähteenä. Tärkeissä asioissa suositellaan ammattimaisen ihmiskääntäjän tekemää käännöstä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->