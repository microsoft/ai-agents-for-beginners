<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-29T17:04:38+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "fi"
}
-->
[![Johdanto tekoälyagentteihin](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.fi.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikkaa yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Johdanto tekoälyagentteihin ja niiden käyttötapauksiin

Tervetuloa "Tekoälyagentit aloittelijoille" -kurssille! Tämä kurssi tarjoaa perustiedot ja käytännön esimerkkejä tekoälyagenttien rakentamisesta.

Liity [Azure AI Foundry Discordiin](https://aka.ms/ai-agents/discord) tavataksesi muita oppijoita ja tekoälyagenttien kehittäjiä sekä kysyäksesi mitä tahansa kysymyksiä liittyen tähän kurssiin.

Kurssin aluksi tutustumme siihen, mitä tekoälyagentit ovat ja miten voimme hyödyntää niitä rakentamissamme sovelluksissa ja työnkuluissa.

## Johdanto

Tämä oppitunti käsittelee:

- Mitä tekoälyagentit ovat ja millaisia erilaisia agenttityyppejä on olemassa?
- Mitkä käyttötapaukset sopivat parhaiten tekoälyagenteille ja miten ne voivat auttaa meitä?
- Mitkä ovat agenttipohjaisten ratkaisujen suunnittelun peruspalikat?

## Oppimistavoitteet
Tämän oppitunnin jälkeen sinun tulisi osata:

- Ymmärtää tekoälyagenttien käsitteet ja miten ne eroavat muista tekoälyratkaisuista.
- Soveltaa tekoälyagentteja tehokkaasti.
- Suunnitella agenttipohjaisia ratkaisuja tuottavasti sekä käyttäjille että asiakkaille.

## Tekoälyagenttien määrittely ja tyypit

### Mitä tekoälyagentit ovat?

Tekoälyagentit ovat **järjestelmiä**, jotka mahdollistavat **laajojen kielimallien (LLM)** **toimintojen suorittamisen** laajentamalla niiden kykyjä antamalla niille **pääsyn työkaluihin** ja **tietoon**.

Puretaan tämä määritelmä osiin:

- **Järjestelmä** - On tärkeää ajatella agentteja ei vain yksittäisinä komponentteina, vaan järjestelmänä, joka koostuu monista osista. Tekoälyagentin perusosat ovat:
  - **Ympäristö** - Määritelty tila, jossa tekoälyagentti toimii. Esimerkiksi matkavarauksia tekevässä tekoälyagentissa ympäristö voisi olla varausjärjestelmä, jota agentti käyttää tehtävien suorittamiseen.
  - **Sensorit** - Ympäristöt sisältävät tietoa ja antavat palautetta. Tekoälyagentit käyttävät sensoreita kerätäkseen ja tulkitakseen tietoa ympäristön nykytilasta. Matkavarausagentin tapauksessa varausjärjestelmä voi tarjota tietoa, kuten hotellien saatavuuden tai lentojen hinnat.
  - **Toimilaitteet** - Kun tekoälyagentti saa tiedon ympäristön nykytilasta, se päättää, mitä toimintaa suorittaa muuttaakseen ympäristöä. Matkavarausagentin tapauksessa tämä voisi tarkoittaa käyttäjälle sopivan huoneen varaamista.

![Mitä tekoälyagentit ovat?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.fi.png)

**Laajat kielimallit** - Agenttien käsite oli olemassa jo ennen LLM:ien luomista. LLM:ien etu tekoälyagenttien rakentamisessa on niiden kyky tulkita ihmiskieltä ja dataa. Tämä kyky mahdollistaa ympäristötiedon tulkinnan ja suunnitelman laatimisen ympäristön muuttamiseksi.

**Toimintojen suorittaminen** - Ilman tekoälyagenttijärjestelmiä LLM:ien toiminta rajoittuu sisällön tai tiedon tuottamiseen käyttäjän antaman kehotteen perusteella. Tekoälyagenttijärjestelmissä LLM:t voivat suorittaa tehtäviä tulkitsemalla käyttäjän pyyntöjä ja käyttämällä ympäristössään saatavilla olevia työkaluja.

**Pääsy työkaluihin** - Mitä työkaluja LLM:llä on käytettävissään, määrittyy 1) sen ympäristön mukaan, jossa se toimii, ja 2) tekoälyagentin kehittäjän toimesta. Matkavarausesimerkissä agentin työkalut rajoittuvat varausjärjestelmän tarjoamiin toimintoihin, ja/tai kehittäjä voi rajoittaa agentin työkalujen käyttöä esimerkiksi vain lentoihin.

**Muisti ja tieto** - Muisti voi olla lyhytaikaista, liittyen keskusteluun käyttäjän ja agentin välillä. Pitkällä aikavälillä, ympäristön tarjoaman tiedon lisäksi, tekoälyagentit voivat hakea tietoa muista järjestelmistä, palveluista, työkaluista ja jopa muilta agenteilta. Matkavarausesimerkissä tämä tieto voisi olla käyttäjän matkustustottumuksia koskevaa tietoa asiakasrekisteristä.

### Erilaiset agenttityypit

Nyt kun meillä on yleinen määritelmä tekoälyagenteista, tarkastellaan joitakin erityisiä agenttityyppejä ja miten niitä voitaisiin soveltaa matkavarausagenttiin.

| **Agenttityyppi**             | **Kuvaus**                                                                                                                            | **Esimerkki**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Yksinkertaiset refleksiagentit** | Suorittavat välittömiä toimintoja ennalta määriteltyjen sääntöjen perusteella.                                                                 | Matka-agentti tulkitsee sähköpostin kontekstin ja ohjaa matkavalitukset asiakaspalveluun.                                                                                                                                       |
| **Mallipohjaiset refleksiagentit** | Suorittavat toimintoja maailman mallin ja sen muutosten perusteella.                                                                 | Matka-agentti priorisoi reittejä, joilla on merkittäviä hinnanmuutoksia, perustuen pääsyyn historiallisiin hintatietoihin.                                                                                                      |
| **Tavoitepohjaiset agentit**   | Laativat suunnitelmia tiettyjen tavoitteiden saavuttamiseksi tulkitsemalla tavoitteen ja määrittämällä toimet sen saavuttamiseksi.                                        | Matka-agentti varaa matkan määrittämällä tarvittavat matkajärjestelyt (auto, julkinen liikenne, lennot) nykyisestä sijainnista määränpäähän.                                                                                     |
| **Hyötyyn perustuvat agentit** | Ottavat huomioon mieltymykset ja punnitsevat kompromisseja numeerisesti päättääkseen, miten saavuttaa tavoitteet.                                                         | Matka-agentti maksimoi hyötyä punnitsemalla mukavuuden ja kustannusten välillä matkavarauksia tehdessään.                                                                                                                       |
| **Oppivat agentit**            | Parantavat toimintaansa ajan myötä reagoimalla palautteeseen ja mukauttamalla toimintojaan sen mukaisesti.                                                                | Matka-agentti parantaa toimintaansa käyttämällä asiakaspalautetta matkan jälkeisistä kyselyistä tehdäkseen muutoksia tuleviin varauksiin.                                                                                       |
| **Hierarkkiset agentit**       | Sisältävät useita agentteja kerroksittaisessa järjestelmässä, jossa ylemmän tason agentit jakavat tehtävät alitason agenteille suoritettaviksi.                            | Matka-agentti peruuttaa matkan jakamalla tehtävän alitehtäviin (esimerkiksi tiettyjen varausten peruuttaminen) ja antamalla alitason agenttien suorittaa ne, raportoiden takaisin ylemmän tason agentille.                                                              |
| **Moniagenttijärjestelmät (MAS)** | Agentit suorittavat tehtäviä itsenäisesti, joko yhteistyössä tai kilpailullisesti.                                                                                      | Yhteistyö: Useat agentit varaavat tiettyjä matkustuspalveluita, kuten hotelleja, lentoja ja viihdettä. Kilpailu: Useat agentit hallinnoivat ja kilpailevat jaetusta hotellivarauskalenterista varatakseen asiakkaita hotelliin. |

## Milloin käyttää tekoälyagentteja

Edellisessä osiossa käytimme matkavarausesimerkkiä selittääksemme, miten erilaisia agenttityyppejä voidaan käyttää eri matkavaraustilanteissa. Jatkamme tämän sovelluksen käyttöä koko kurssin ajan.

Tarkastellaan nyt, millaisiin käyttötapauksiin tekoälyagentit sopivat parhaiten:

![Milloin käyttää tekoälyagentteja?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.fi.png)

- **Avoimet ongelmat** - mahdollistavat LLM:n määrittää tarvittavat askeleet tehtävän suorittamiseksi, koska niitä ei aina voida kovakoodata työnkulkuun.
- **Monivaiheiset prosessit** - tehtävät, jotka vaativat tiettyä monimutkaisuutta, jolloin tekoälyagentin täytyy käyttää työkaluja tai tietoa useiden vuorovaikutusten aikana yhden haun sijaan.
- **Parantuminen ajan myötä** - tehtävät, joissa agentti voi parantaa toimintaansa ajan myötä saamalla palautetta joko ympäristöltään tai käyttäjiltä tarjotakseen parempaa hyötyä.

Käsittelemme lisää tekoälyagenttien käyttöön liittyviä huomioita "Luotettavien tekoälyagenttien rakentaminen" -oppitunnissa.

## Agenttipohjaisten ratkaisujen perusteet

### Agenttien kehittäminen

Ensimmäinen askel tekoälyagenttijärjestelmän suunnittelussa on määritellä työkalut, toiminnot ja käyttäytymiset. Tällä kurssilla keskitymme käyttämään **Azure AI Agent Service** -palvelua agenttien määrittelyyn. Se tarjoaa ominaisuuksia, kuten:

- Avoimien mallien, kuten OpenAI, Mistral ja Llama, valinta
- Lisensoidun datan käyttö palveluntarjoajilta, kuten Tripadvisor
- Standardoitujen OpenAPI 3.0 -työkalujen käyttö

### Agenttipohjaiset mallit

Viestintä LLM:ien kanssa tapahtuu kehotteiden avulla. Tekoälyagenttien puoliksi autonomisen luonteen vuoksi ei aina ole mahdollista tai tarpeellista antaa manuaalisesti uutta kehotetta LLM:lle ympäristön muutoksen jälkeen. Käytämme **agenttipohjaisia malleja**, jotka mahdollistavat LLM:n kehotteiden antamisen useiden vaiheiden aikana skaalautuvammalla tavalla.

Tämä kurssi on jaettu joihinkin nykyisin suosittuihin agenttipohjaisiin malleihin.

### Agenttikehykset

Agenttikehykset mahdollistavat kehittäjille agenttipohjaisten mallien toteuttamisen koodin avulla. Nämä kehykset tarjoavat malleja, lisäosia ja työkaluja parempaan tekoälyagenttien yhteistyöhön. Näiden etujen avulla voidaan parantaa tekoälyagenttijärjestelmien havainnointia ja vianetsintää.

Tällä kurssilla tutkimme tutkimuslähtöistä AutoGen-kehystä ja tuotantovalmiista Agent-kehystä Semantic Kernelistä.

### Onko sinulla lisää kysymyksiä tekoälyagenteista?

Liity [Azure AI Foundry Discordiin](https://aka.ms/ai-agents/discord) tavataksesi muita oppijoita, osallistuaksesi toimistotunteihin ja saadaksesi vastauksia tekoälyagentteihin liittyviin kysymyksiisi.

## Edellinen oppitunti

[Kurssin aloitus](../00-course-setup/README.md)

## Seuraava oppitunti

[Agenttikehysten tutkiminen](../02-explore-agentic-frameworks/README.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.