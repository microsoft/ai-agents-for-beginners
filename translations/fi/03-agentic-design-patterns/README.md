[![Kuinka suunnitella hyviä tekoälyagentteja](../../../translated_images/fi/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_
# Tekoälyagenttien suunnittelun periaatteet

## Johdanto

On monia tapoja lähestyä tekoälyagenttijärjestelmien rakentamista. Koska epäselvyys on ominaisuus eikä virhe generatiivisen tekoälyn suunnittelussa, insinööreille voi joskus olla vaikeaa tietää, mistä edes aloittaa. Olemme luoneet joukon ihmiskeskeisiä UX-suunnitteluperiaatteita, jotka mahdollistavat kehittäjien rakentaa asiakaskeskeisiä agenttipohjaisia järjestelmiä ratkaisemaan liiketoiminnan tarpeita. Nämä suunnitteluperiaatteet eivät ole määrämuotoinen arkkitehtuuri, vaan pikemminkin lähtökohta tiimeille, jotka määrittelevät ja rakentavat agenttikokemuksia.

Yleisesti ottaen agenttien tulisi:

- Laajentaa ja tehostaa ihmisen kykyjä (ideoiden kehittäminen, ongelmanratkaisu, automaatio jne.)
- Täyttää tietämyksen aukkoja (tuoda minulle ajan tasalla olevaa tietoa eri tieteenaloilta, käännökset jne.)
- Edistää ja tukea yhteistyötä tavoilla, joilla yksilöt haluavat työskennellä yhdessä
- Tehdä meistä parempia versioita itsestämme (esim. elämänvalmentaja/tehtävien hallitsija, auttaa oppimaan tunnesäätelyä ja tietoisuustaitoja, rakentaa sinnikkyyttä jne.)

## Mitä tässä oppitunnissa käsitellään

- Mitkä ovat agenttisuunnitteluperiaatteet
- Mitä ohjeita noudattaa näitä periaatteita toteutettaessa
- Esimerkkejä periaatteiden käytöstä

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat:

1. Selittää, mitä agenttisuunnitteluperiaatteet ovat
2. Selittää ohjeet agenttisuunnitteluperiaatteiden käyttöön
3. Ymmärtää, miten agentti rakennetaan käyttäen agenttisuunnitteluperiaatteita

## Agenttisuunnitteluperiaatteet

![Agenttisuunnitteluperiaatteet](../../../translated_images/fi/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agentti (tila)

Tämä on ympäristö, jossa agentti toimii. Nämä periaatteet ohjaavat, miten suunnittelemme agentteja toimimaan fyysisissä ja digitaalisissa maailmoissa.

- **Yhdistää, ei sulauttaa** – auttaa yhdistämään ihmisiä toisiin ihmisiin, tapahtumiin ja toimintakelpoiseen tietoon yhteistyön ja yhteyden mahdollistamiseksi.
- Agentit auttavat yhdistämään tapahtumia, tietoa ja ihmisiä.
- Agentit tuovat ihmisiä lähemmäs toisiaan. Niitä ei ole suunniteltu korvaamaan tai vähättelemään ihmisiä.
- **Helposti saavutettavissa mutta satunnaisesti näkymättömissä** – agentti toimii pääasiassa taustalla ja muistuttaa meitä vain, kun se on merkityksellistä ja sopivaa.
  - Agentin löytäminen ja käyttöoikeutettujen käyttäjien saavutettavuus eri laitteilla tai alustoilla on helppoa.
  - Agentti tukee multimodaalisia syötteitä ja tulosteita (ääni, puhe, teksti jne.).
  - Agentti voi saumattomasti siirtyä etualan ja taustan välillä; proaktiivisen ja reaktiivisen välillä sen mukaan, miten se havaitsee käyttäjän tarpeita.
  - Agentti voi toimia näkymättömässä muodossa, mutta sen taustaprosessipolku ja yhteistyö muiden agenttien kanssa ovat käyttäjälle läpinäkyviä ja hallittavissa.

### Agentti (aika)

Tämä kuvaa, miten agentti toimii ajan kuluessa. Nämä periaatteet ohjaavat, miten suunnittelemme agentteja toimimaan menneisyydessä, nykyhetkessä ja tulevaisuudessa.

- **Menneisyys**: Historian huomioiminen, joka sisältää sekä tilan että kontekstin.
  - Agentti tarjoaa merkityksellisempiä tuloksia analysoimalla laajempaa historiallista dataa pelkkien tapahtumien, ihmisten tai tilojen sijaan.
  - Agentti muodostaa yhteyksiä menneisiin tapahtumiin ja peilaa aktiivisesti muistoja nykytilanteisiin osallistumiseksi.
- **Nyt**: Kannustaa enemmän kuin vain ilmoittaa.
  - Agentti edustaa kokonaisvaltaista lähestymistapaa ihmisten kanssa vuorovaikutukseen. Kun tapahtuma tapahtuu, agentti ylittää staattisen ilmoituksen tai muun muodollisuuden. Agentti voi yksinkertaistaa työnkulkuja tai dynaamisesti luoda vihjeitä ohjaamaan käyttäjän huomiota oikeaan aikaan.
  - Agentti tarjoaa tietoa kontekstuaalisen ympäristön, sosiaalisten ja kulttuuristen muutosten sekä käyttäjän tarkoituksen pohjalta.
  - Agentin vuorovaikutus voi olla asteittaista, kehittyvää/monimutkaistuvaa, voimaannuttaen käyttäjiä pitkällä aikavälillä.
- **Tulevaisuus**: Sopeutuva ja kehittyvä.
  - Agentti sopeutuu erilaisiin laitteisiin, alustoihin ja modaliteetteihin.
  - Agentti sopeutuu käyttäjän käyttäytymiseen, saavutettavuustarpeisiin ja on vapaasti mukautettavissa.
  - Agenttia muokkaa ja kehittyy jatkuvan käyttäjävuorovaikutuksen kautta.

### Agentti (ydin)

Nämä ovat agentin suunnittelun keskeiset elementit.

- **Hyväksy epävarmuus mutta rakenna luottamus**.
  - Tiettyä epävarmuutta agentilta odotetaan. Epävarmuus on olennainen osa agentin suunnittelua.
  - Luottamus ja läpinäkyvyys ovat agentin suunnittelun perustavia kerroksia.
  - Ihmiset hallitsevat, milloin agentti on päällä/pois päältä, ja agentin tila on selvästi näkyvillä koko ajan.

## Ohjeet periaatteiden toteuttamiseen

Kun käytät edellä mainittuja suunnitteluperiaatteita, käytä seuraavia ohjeita:

1. **Läpinäkyvyys**: Kerro käyttäjälle, että tekoäly on mukana, miten se toimii (mukaan lukien aiemmat toimet), ja miten antaa palautetta ja muuttaa järjestelmää.
2. **Hallinta**: Mahdollista käyttäjän mukauttaa, määrittää mieltymyksiä ja personoida sekä hallita järjestelmää ja sen ominaisuuksia (mukaan lukien unohtamisen mahdollisuus).
3. **Johdonmukaisuus**: Pyri johdonmukaisiin, monimuotoisiin kokemuksiin laitteiden ja päätelaselmien välillä. Käytä tutuksi tulleita UI/UX-elementtejä siellä missä mahdollista (esim. mikrofoni-ikoni puhevuorovaikutukseen) ja vähennä asiakkaan kognitiivista kuormitusta mahdollisimman paljon (esim. tiiviit vastaukset, visuaaliset apuvälineet ja ’Lue lisää’ -sisältö).

## Kuinka suunnitella matkatoimistoagentti näiden periaatteiden ja ohjeiden avulla

Kuvittele, että suunnittelet Matkatoimistoagenttia, tässä on kuinka voisit ajatella käyttää suunnitteluperiaatteita ja ohjeita:

1. **Läpinäkyvyys** – Kerro käyttäjälle, että Matkatoimistoagentti on tekoälyllä varustettu agentti. Tarjoa perusohjeita aloitukseen (esim. ”Hei” -viesti, esimerkkikehotteita). Kirjaa tämä selvästi tuotteen sivulle. Näytä lista aiemmin käyttäjän pyytämistä kehotteista. Tee selväksi, miten palaute annetaan (peukku ylös ja alas, lähetä palaute -painike jne.). Selkeästi ilmaise, onko agentilla käyttö- tai aihe-rajoituksia.
2. **Hallinta** – Varmista, että käyttäjä ymmärtää miten agenttia voi muokata luomisen jälkeen esimerkiksi järjestelmäkehotteen avulla. Mahdollista käyttäjän valita, kuinka sanavalmis agentti on, sen kirjoitustyyli ja millaisia varoituksia agentin keskusteltavista asioista on. Anna käyttäjän tarkastella ja poistaa siihen liittyviä tiedostoja, tietoja, kehotteita ja aiempia keskusteluja.
3. **Johdonmukaisuus** – Varmista, että kuvakkeet kehotteen jakamiselle, tiedoston tai valokuvan lisäämiselle ja jonkin merkitsemiselle ovat standardoituja ja tunnistettavia. Käytä paperiliitin-kuvaketta osoittamaan tiedoston lataus/jakaminen agentin kanssa ja kuva-kuvaketta grafiikoiden lataamista varten.

## Esimerkkikoodit

- Python: [Agenttikehys](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agenttikehys](./code_samples/03-dotnet-agent-framework.md)


## Onko sinulla lisää kysymyksiä tekoälyagenttien suunnittelumalleista?

Liity [Microsoft Foundryn Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia tekoälyagenttikysymyksiisi.

## Lisäresurssit

- <a href="https://openai.com" target="_blank">Käytännöt agenttipohjaisten tekoälyjärjestelmien hallintaan | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">HAX Toolkit -projekti - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Vastuullisen tekoälyn työkalupakki</a>

## Edellinen oppitunti

[Agenttikehysten tutkiminen](../02-explore-agentic-frameworks/README.md)

## Seuraava oppitunti

[Työkalujen käyttö -suunnittelumalli](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->