[![How to Design Good AI Agents](../../../translated_images/fi/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Napsauta yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_
# AI-agenttisuunnittelun periaatteet

## Johdanto

AI-agenttijärjestelmien rakentamiseen on monia tapoja suhtautua. Koska epäselvyys on generatiivisen tekoälyn suunnittelussa ominaisuus, ei virhe, insinööreille voi joskus olla vaikeaa tietää, mistä edes aloittaa. Olemme luoneet joukon ihmiskeskeisiä UX-suunnittelun periaatteita, jotka mahdollistavat kehittäjille asiakaskeskeisten agenttijärjestelmien rakentamisen liiketoimintatarpeiden ratkaisemiseksi. Nämä suunnitteluperiaatteet eivät ole määrätty arkkitehtuuri, vaan lähtökohta tiimeille, jotka määrittelevät ja rakentavat agenttikokemuksia.

Yleisesti ottaen agenttien tulisi:

- Laajentaa ja skaalata ihmisten kykyjä (ideoiden kehittäminen, ongelmanratkaisu, automaatio jne.)
- Täyttää tietovajeita (päivittää minut tieteenaloihin, käännökset jne.)
- Helpottaa ja tukea yhteistyötä tavoilla, joita me yksilöinä mieluummin teemme muiden kanssa
- Tehdä meistä parempia versioita itsestämme (esim. elämänvalmentajana/tehtävien hallitsijana auttaen hallitsemaan tunteita ja tietoisuustaitoja, rakentamaan resilienssiä jne.)

## Tämä oppitunti käsittelee

- Mitkä ovat agenttisuunnittelun periaatteet
- Mitä ohjeita noudattaa näitä periaatteita toteuttaessa
- Esimerkkejä siitä, miten periaatteita käytetään

## Oppimistavoitteet

Tämän oppitunnin suorittamisen jälkeen osaat:

1. Selittää, mitä agenttisuunnittelun periaatteet ovat
2. Selittää periaatteiden käytön ohjeet
3. Ymmärtää, miten agentti rakennetaan näitä periaatteita käyttäen

## Agenttisuunnittelun periaatteet

![Agenttisuunnittelun periaatteet](../../../translated_images/fi/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agentti (tila)

Tämä on ympäristö, jossa agentti toimii. Nämä periaatteet ohjaavat, miten suunnittelemme agentteja toimimaan fyysisissä ja digitaalisissa maailmoissa.

- **Yhdistämistä, ei hajoittamista** – auttavat yhdistämään ihmisiä toisiin ihmisiin, tapahtumiin ja käyttökelpoiseen tietoon yhteistyön ja yhteyksien mahdollistamiseksi.
- Agentit auttavat yhdistämään tapahtumia, tietoa ja ihmisiä.
- Agentit tuovat ihmisiä lähemmäksi toisiaan. Niitä ei ole suunniteltu korvaamaan tai vähättelemään ihmisiä.
- **Helposti saavutettavissa, mutta ajoittain näkymättömiä** – agentti toimii suuressa määrin taustalla ja antaa vain kevyitä herätteitä, kun se on relevanttia ja sopivaa.
  - Agentti on helposti löydettävissä ja käyttöönotettavissa valtuutetuille käyttäjille millä tahansa laitteella tai alustalla.
  - Agentti tukee monimuotoisia syötteitä ja tulosteita (ääni, puhe, teksti jne.).
  - Agentti voi saumattomasti siirtyä etualaan ja taustalle; olla ennakoiva tai reaktiivinen käyttäjän tarpeiden mukaan.
  - Agentti voi toimia näkymättömässä muodossa, mutta sen taustaprosessit ja yhteistyö muiden agenttien kanssa ovat käyttäjälle läpinäkyviä ja hallittavissa.

### Agentti (aika)

Tämä kuvaa, miten agentti toimii ajan kuluessa. Nämä periaatteet ohjaavat agenttien suunnittelua menneen, nykyisen ja tulevan kanssa vuorovaikutuksessa.

- **Menneisyys**: historian reflektointi, sisältäen tilan ja kontekstin.
  - Agentti tarjoaa merkityksellisempiä tuloksia analysoimalla runsasta historiallista dataa pelkän tapahtuman, ihmisten tai tilojen lisäksi.
  - Agentti luo yhteyksiä menneistä tapahtumista ja pohdiskelee aktiivisesti muistiaan osallistuakseen nykytilanteisiin.
- **Nyt**: Pieniä kehotuksia suuremmin kuin pelkkää ilmoitusta.
  - Agentissa on kokonaisvaltainen lähestymistapa ihmisten kanssa toimimisessa. Kun tapahtuma tapahtuu, agentti ei tyydy staattiseen ilmoitukseen tai muuhun jäykkään muotoon. Agentti voi yksinkertaistaa prosesseja tai luoda dynaamisia vihjeitä suuntaamaan käyttäjän huomion oikeaan aikaan.
  - Agentti tarjoaa tietoa ympäristöstä, sosiaalisista ja kulttuurisista muutoksista ja käyttäjän tarkoitusperään räätälöitynä.
  - Agentin vuorovaikutus voi olla asteittaista, kehittyvää ja monimutkaistuvaa käyttäjien vahvistamiseksi pitkällä aikavälillä.
- **Tulevaisuus**: Mukautuminen ja kehittyminen.
  - Agentti mukautuu erilaisiin laitteisiin, alustoihin ja modaliteetteihin.
  - Agentti mukautuu käyttäjän käyttäytymiseen, saavutettavuustarpeisiin ja on vapaasti räätälöitävissä.
  - Agentti muovautuu ja kehittyy jatkuvan käyttäjävuorovaikutuksen kautta.

### Agentti (ydin)

Nämä ovat keskeiset osat agentin suunnittelun ytimestä.

- **Hyväksy epävarmuus, mutta rakenna luottamus**.
  - Tietty taso epävarmuutta agentissa on odotettua. Epävarmuus on agenttisuunnittelun avainelementti.
  - Luottamus ja avoimuus ovat agenttisuunnittelun perustavia kerroksia.
  - Ihmiset hallitsevat, milloin agentti on päällä/pois päältä, ja agentin tila on aina selkeästi näkyvissä.

## Ohjeet näiden periaatteiden toteuttamiseen

Kun käytät edellä mainittuja periaatteita, seuraa näitä ohjeita:

1. **Läpinäkyvyys**: Kerro käyttäjälle, että tekoälyä käytetään, miten se toimii (mukaan lukien aiemmat toimet), ja miten antaa palautetta ja muokata järjestelmää.
2. **Hallinta**: Mahdollista käyttäjän räätälöidä, määrittää mieltymyksiä ja personoida, sekä hallita järjestelmää ja sen ominaisuuksia (mukaan lukien unohdustoiminto).
3. **Johdonmukaisuus**: Pyri johdonmukaisiin, monimuotoisiin käyttökokemuksiin eri laitteilla ja päätelaitteissa. Käytä tuttuja UI/UX-elementtejä mahdollisuuksien mukaan (esim. mikrofonikuvake puhevuorovaikutuksessa) ja vähennä asiakkaan kognitiivista kuormitusta niin paljon kuin mahdollista (esim. ytimekkäät vastaukset, visuaaliset apuvälineet ja 'Lue lisää' -sisältö).

## Kuinka suunnitella matkatoimistoagentti näitä periaatteita ja ohjeita käyttäen

Kuvittele, että suunnittelet Matkatoimistoagenttia, näin voisit pohtia suunnitteluperiaatteiden ja ohjeiden käyttöä:

1. **Läpinäkyvyys** – Kerro käyttäjälle, että Matkatoimistoagentti on tekoälypohjainen agentti. Anna perustiedot aloittamiseen (esim. "Hei" -viesti, esimerkkikehotteet). Dokumentoi tämä selkeästi tuotteen sivulla. Näytä lista käyttäjän aiemmista kehotteista. Kerro selkeästi, miten antaa palautetta (peukut ylös/alas, lähetä palaute -painike jne.). Kerro selkeästi, onko agentilla käyttö- tai aihealueiden rajoituksia.
2. **Hallinta** – Varmista, että käyttäjä ymmärtää, miten agenttia voi muokata sen luonnin jälkeen järjestelmäkehotteilla. Mahdollista käyttäjälle valita agentin sanamäärä, kirjoitustyyli ja mahdolliset aiheet, joista agentin ei tulisi puhua. Anna käyttäjälle mahdollisuus tarkastella ja poistaa liitettyjä tiedostoja tai dataa, kehotteita ja aiempia keskusteluja.
3. **Johdonmukaisuus** – Varmista, että kuvakkeet, kuten Jaa-kehote, tiedoston tai kuvan lisääminen sekä jonkun tai jonkin merkintä, ovat standardeja ja tunnistettavia. Käytä paperiliitinkuvaketta tiedostojen latauksen/jakamisen merkkinä agentille ja kuvan kuvaketta grafiikkalatauksen merkkinä.

## Esimerkkikoodit

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Lisäkysymyksiä AI-agenttisuunnittelumalleista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua avoimeen toimistotuntiin ja saada vastauksia AI-agenttikysymyksiisi.

## Lisäresurssit

- <a href="https://openai.com" target="_blank">Agenttiohjattujen tekoälyjärjestelmien hallintakäytännöt | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">HAX Toolkit Project - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Responsible AI Toolbox</a>

## Edellinen oppitunti

[Agenttirunkojen tutkiminen](../02-explore-agentic-frameworks/README.md)

## Seuraava oppitunti

[Työkalun käytön suunnittelumalli](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->