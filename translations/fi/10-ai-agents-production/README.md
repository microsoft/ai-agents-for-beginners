# AI-agentit tuotannossa: havaittavuus ja arviointi

[![AI Agents in Production](../../../translated_images/fi/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kun tekoälyagentit siirtyvät kokeellisista prototyypeistä todellisiin sovelluksiin, kyky ymmärtää niiden käyttäytymistä, valvoa niiden suorituskykyä ja systemaattisesti arvioida niiden tuloksia tulee tärkeäksi.

## Oppimistavoitteet

Tämän oppitunnin suorittamisen jälkeen osaat/ymmärrät:
- Agenttien havaittavuuden ja arvioinnin ydinkäsitteet
- Menetelmät agenttien suorituskyvyn, kustannusten ja tehokkuuden parantamiseksi
- Mitä ja miten arvioda tekoälyagenttejasi systemaattisesti
- Kuinka hallita kustannuksia tekoälyagentteja tuotantoon otettaessa
- Kuinka instrumentoida Microsoft Agent Framework -alustalla rakennettuja agentteja

Tavoitteena on antaa sinulle tietoa, jolla voit muuttaa "mustat laatikot" -agenttisi läpinäkyviksi, hallittaviksi ja luotettaviksi järjestelmiksi.

_**Huom:** On tärkeää ottaa käyttöön turvallisia ja luotettavia tekoälyagentteja. Kurkista myös oppitunti [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Jäljet ja jaksot

Havaittavuustyökalut, kuten [Langfuse](https://langfuse.com/) tai [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), kuvaavat yleensä agentin suorittamiset jälkinä ja jaksoina.

- **Jälki** kuvaa koko agentin tehtävää alusta loppuun (esim. käyttäjän kyselyn käsittely).
- **Jaksot** ovat yksittäisiä askelia jäljen sisällä (esim. kielimallin kutsu tai tietojen hakeminen).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Ilman havaittavuutta tekoälyagentti voi tuntua "mustalta laatikolta" – sen sisäinen tila ja päättely ovat läpinäkymättömiä, mikä vaikeuttaa ongelmien diagnosointia tai suorituskyvyn optimointia. Havaittavuuden avulla agentit muuttuvat "lasilaatikoiksi", tarjoten läpinäkyvyyttä, joka on tärkeää luottamuksen rakentamiseksi ja niiden toiminnan varmistamiseksi suunnitellulla tavalla.

## Miksi havaittavuus on tärkeää tuotantoympäristöissä

Tekoälyagenttien siirtyminen tuotantoympäristöihin tuo mukanaan uusia haasteita ja vaatimuksia. Havaittavuus ei ole enää vain "hyvän pitää"-ominaisuus vaan kriittinen kyvykkyys:

*   **Vianmääritys ja juurisyiden analyysi**: Kun agentti epäonnistuu tai tuottaa odottamattoman tuloksen, havaittavuustyökalut tarjoavat jäljet virheen lähteen paikantamiseen. Tämä on erityisen tärkeää monimutkaisissa agenteissa, jotka saattavat sisältää useita LLM-kutsuja, työkalujen vuorovaikutuksia ja ehtologiikkaa.
*   **Viiveen ja kustannusten hallinta**: Tekoälyagentit käyttävät usein LLM:ää ja muita ulkoisia rajapintoja, joista veloitetaan token- tai kutsukohtaisesti. Havaittavuus mahdollistaa näiden kutsujen tarkan seurannan, auttaen tunnistamaan toimintoja, jotka ovat liian hitaita tai kalliita. Tämä mahdollistaa tiimien optimoida kehotteita, valita tehokkaampia malleja tai uudistaa työnkulkuja operatiivisten kustannusten hallitsemiseksi ja hyvän käyttökokemuksen varmistamiseksi.
*   **Luottamus, turvallisuus ja säädösten noudattaminen**: Monissa sovelluksissa on tärkeää varmistaa, että agentit käyttäytyvät turvallisesti ja eettisesti. Havaittavuus tarjoaa auditointijäljen agentin toimista ja päätöksistä. Sitä voidaan käyttää havaitsemaan ja lieventämään ongelmia, kuten kehotteen injektointia, haitallisen sisällön tuottamista tai henkilötietojen väärinkäsittelyä. Esimerkiksi voit tarkastella jälkiä ymmärtääksesi, miksi agentti antoi tietyn vastauksen tai käytti tiettyä työkalua.
*   **Jatkuvan parantamisen sykli**: Havaittavuustiedot ovat iteratiivisen kehitysprosessin perusta. Seuraamalla, miten agentit toimivat todellisessa ympäristössä, tiimit voivat tunnistaa parannuskohteita, kerätä tietoja mallien hienosäätöön ja validoida muutosten vaikutukset. Tämä luo palautesykliä, jossa tuotantoympäristön havainnot online-arvioinnista ohjaavat offline-kokeiluja ja hienosäätöä, mikä johtaa jatkuvasti parempaan agentin suorituskykyyn.

## Keskeisiä seurattavia mittareita

Agentin käyttäytymisen valvomiseksi ja ymmärtämiseksi tulisi seurata useita mittareita ja signaaleja. Vaikka mittarit voivat vaihdella agentin tarkoituksen mukaan, jotkut ovat yleisesti tärkeitä.

Tässä ovat yleisimmät mittarit, joita havaittavuustyökalut seuraavat:

**Viive:** Kuinka nopeasti agentti vastaa? Pitkät odotusajat heikentävät käyttökokemusta. Viivettä tulisi mitata tehtävien ja yksittäisten vaiheiden osalta jälkiä seuraamalla. Esimerkiksi agentti, joka käyttää 20 sekuntia kaikkiin mallikutsuihin, voisi nopeutua käyttämällä nopeampaa mallia tai ajamalla mallikutsut rinnakkain.

**Kustannukset:** Kuinka paljon agentin suoritus maksaa? Tekoälyagentit käyttävät LLM-kutsuja, joista veloitetaan token- tai ulkoisten rajapintojen kutsukohtaisesti. Työkalujen runsas käyttö tai useat kehotteet voivat nopeasti kasvattaa kustannuksia. Esimerkiksi jos agentti kutsuu LLM:ää viisi kertaa marginaalisen laadun parantamiseksi, on arvioitava, onko kustannus perusteltu vai voisiko kutsujen määrää vähentää tai käyttää halvempi malli. Reaaliaikainen seuranta voi myös havaita odottamattomat piikit (esim. virheet, jotka aiheuttavat liiallisia rajapintasilmukoita).

**Pyyntöviraat:** Kuinka monta pyyntöä agentti epäonnistui suorittamaan? Tämä voi sisältää API-virheitä tai epäonnistuneita työkalukutsuja. Tuotannossa agentin tekemiseksi kestävämmäksi näitä vastaan voit asettaa varareittejä tai uudelleenyrittämiä. Esim. jos LLM-palveluntarjoaja A on alas, voit vaihtaa LLM-palveluntarjoaja B:hen varajärjestelmänä.

**Käyttäjäpalautteet:** Suorat käyttäjäarvioinnit tarjoavat arvokkaita näkemyksiä. Tämä voi sisältää eksplisiittisiä arvioita (👍peukut ylös/👎alas, ⭐1-5 tähteä) tai tekstimuotoisia kommentteja. Johdonmukainen negatiivinen palaute tulisi herättää huomioita, sillä se on merkki siitä, ettei agentti toimi odotetusti.

**Implisiittinen käyttäjäpalaute:** Käyttäjien käyttäytyminen antaa epäsuoraa palautetta ilman eksplisiittisiä arvioita. Tämä voi sisältää välittömän uudelleenmuotoilun, toistuvat kyselyt tai yritykset uudelleenvetoon. Esim. jos huomaat käyttäjien toistuvasti esittävän saman kysymyksen, se on merkki siitä, ettei agentti toimi odotetusti.

**Tarkkuus:** Kuinka usein agentti tuottaa oikeita tai toivottuja tuloksia? Tarkkuuden määritelmät vaihtelevat (esim. ongelmanratkaisun oikeellisuus, tiedonhakutarkkuus, käyttäjätyytyväisyys). Ensimmäinen askel on määritellä agenttisi onnistumisen kriteerit. Voit seurata tarkkuutta automaattisten tarkistusten, arviointipisteiden tai tehtävän suorittamisen merkintöjen avulla. Esimerkiksi merkitsemällä jäljet "onnistuneiksi" tai "epäonnistuneiksi".

**Automaattiset arviointimittarit:** Voit myös asettaa automaattisia arviointeja. Esimerkiksi voit käyttää LLM:ää pisteyttämään agentin tuottaman tuloksen, esim. osoittaako se apua, tarkkuutta tai puutteita. Saatavilla on myös useita avoimen lähdekoodin kirjastoja, jotka auttavat pisteyttämään agentin eri näkökulmia. Esim. [RAGAS](https://docs.ragas.io/) RAG-agentteihin tai [LLM Guard](https://llm-guard.com/) haitallisen kielen tai kehotteen injektoinnin havaitsemiseen.

Käytännössä näiden mittareiden yhdistelmä antaa parhaan kattavuuden tekoälyagentin terveystilasta. Tässä luvussa olevassa [esimerkkimateriaali](./code_samples/10-expense_claim-demo.ipynb) näytämme, miltä nämä mittarit näyttävät todellisissa esimerkeissä, mutta ensin opimme, miltä tyypillinen arviointityönkulku näyttää.

## Instrumentoi agenttisi

Jäljitystietojen keräämiseksi sinun täytyy instrumentoida koodisi. Tavoitteena on instrumentoida agentin koodi siten, että se lähettää jälkiä ja mittareita, jotka voidaan tallentaa, käsitellä ja visualisoida havaittavuusalustalla.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) on noussut alan standardiksi LLM-havaittavuudessa. Se tarjoaa API:t, SDK:t ja työkalut telemetriatiedon luomiseen, keräämiseen ja vientiin.

On olemassa monia instrumentointikirjastoja, jotka kietovat olemassa olevat agenttikehykset ja helpottavat OpenTelemetry-jaksojen vientiä havaittavuustyökaluun. Microsoft Agent Framework integroituu OpenTelemetryyn natiivisti. Alla esimerkki MAF-agentin instrumentoinnista:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Edustajan suoritus jäljitetään automaattisesti
    pass
```

Tässä luvussa oleva [esimerkkimateriaali](./code_samples/10-expense_claim-demo.ipynb) osoittaa, miten instrumentoida MAF-agenttisi.

**Manuaalinen jaksojen luonti:** Vaikka instrumentointikirjastot tarjoavat hyvän perustan, on usein tilanteita, joissa tarvitaan yksityiskohtaisempaa tai käyttäjäkohtaista tietoa. Voit luoda manuaalisesti jaksoja lisätäksesi mukautettua sovelluslogiikkaa. Vielä tärkeämpää on, että ne voivat rikastaa automaattisesti tai manuaalisesti luotuja jaksoja mukautetuilla ominaisuuksilla (tunnetaan myös tageina tai metatietoina). Nämä ominaisuudet voivat sisältää liiketoimintakohtaisia tietoja, välivaiheen laskelmia tai mitä tahansa kontekstia, joka voi olla hyödyllistä virheenkorjauksessa tai analyysissä, kuten `user_id`, `session_id` tai `model_version`.

Esimerkki jälkien ja jaksojen manuaalisesta luomisesta [Langfuse Python SDK:n](https://langfuse.com/docs/sdk/python/sdk-v3) kanssa:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentin arviointi

Havaittavuus tarjoaa meille mittarit, mutta arviointi on prosessi, jossa analysoidaan nämä tiedot (ja suoritetaan testejä) selvittääksemme, miten hyvin tekoälyagentti suoriutuu ja miten sitä voidaan parantaa. Toisin sanoen, kun sinulla on nuo jäljet ja mittarit, miten niitä käytetään agentin arviointiin ja päätöksentekoon?

Säännöllinen arviointi on tärkeää, koska tekoälyagentit ovat usein ei-deterministisiä ja voivat kehittyä (päivitysten tai mallin käyttäytymisen muuttumisen kautta) – ilman arviointia et tietäisi, tekeekö "älykäs agenttisi" työtään hyvin vai onko sen suoritus heikentynyt.

AI-agenttien arviointeja on kahta tyyppiä: **online-arviointi** ja **offline-arviointi**. Molemmat ovat arvokkaita ja täydentävät toisiaan. Aloitamme yleensä offline-arvioinnilla, koska se on vähimmäisvaatimus ennen agentin käyttöönottoa.

### Offline-arviointi

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Tämä tarkoittaa agentin arviointia kontrolloidussa ympäristössä, yleensä käyttämällä testiaineistoja, ei live-käyttäjäkyselyjä. Käytät kuratoituja aineistoja, joissa tunnet odotetun tuloksen tai oikean käyttäytymisen, ja suoritat agentin niillä.

Esimerkiksi, jos olet rakentanut matemaattisten tekstitehtävien agentin, sinulla saattaa olla [testiaineisto](https://huggingface.co/datasets/gsm8k), jossa on 100 ongelmaa ja tunnetut vastaukset. Offline-arviointi tehdään usein kehityksen aikana (ja voi olla osa CI/CD-putkia) tarkistamaan parannuksia tai estämään taantumia. Hyöty on, että se on **toistettavissa ja saat selkeät tarkkuusmittarit, koska sinulla on totuustiedot**. Voit simuloida käyttäjäkyselyjä ja mitata agentin vastauksia ihanteellisia vastauksia vastaan tai käyttää automaattisia mittareita, kuten yllä kuvattiin.

Offline-arvioinnin tärkein haaste on varmistaa, että testiaineisto on kattava ja pysyy relevanttina – agentti voi suoriutua hyvin kiinteällä testiaineistolla, mutta kohdata hyvin erilaisia kyselyitä tuotannossa. Siksi testiaineistot tulee pitää ajan tasalla uusilla reunaehdoilla ja esimerkeillä, jotka heijastavat todellisia tilanteita. Pieniä "savukokeita" ja laajempia arviointisettejä on hyödyllistä yhdistää: pienet nopeat tarkistukset ja suuremmat kattavammat suorituskykymittarit.

### Online-arviointi

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Tämä tarkoittaa agentin arviointia live-ympäristössä, eli tuotannon todellisessa käytössä. Online-arviointiin sisältyy agentin suorituskyvyn seuraaminen todellisissa käyttäjävuorovaikutuksissa ja tulosten jatkuva analysointi.

Esimerkiksi voit seurata onnistumisprosentteja, käyttäjätyytyväisyysarvioita tai muita mitattavia arvoja live-liikenteessä. Online-arvioinnin etu on, että se **havaintoja asioita, joita et ehkä odota laboratoriossa** – voit nähdä mallin käyttäytymisen muuttumisen ajan myötä (jos agentin tehokkuus heikkenee syötteiden muuttumisen takia) ja havaita odottamattomia kyselyjä tai tilanteita, joita ei ollut testidatassa. Se tarjoaa todellisen kuvan agentin käyttäytymisestä käytännössä.

Online-arviointi sisältää usein implisiittisen ja eksplisiittisen käyttäjäpalautteen keräämisen, kuten aiemmin käsiteltiin, sekä mahdollisesti varjotestien tai A/B-testien ajamisen (missä uusi agenttiversio toimii rinnakkain vanhan kanssa vertailua varten). Haasteena on saada luotettavia merkintöjä tai pisteitä live-vuorovaikutuksista – voit joutua luottamaan käyttäjäpalautteeseen tai jälkiseuranta-arvoihin (esim. klikkasiko käyttäjä tulosta).

### Kummankin yhdistäminen

Online- ja offline-arviointi eivät ole toisiaan poissulkevia, vaan hyvin täydentäviä. Online-valvonnasta saadut tiedot (esim. uudet käyttäjäkyselytyypit, joissa agentti suoriutuu huonosti) voidaan käyttää offline-testiaineistojen täydentämiseen ja kehittämiseen. Toisaalta agentit, jotka suoriutuvat hyvin offline-testeissä, voidaan luottavaisemmin ottaa käyttöön ja valvoa online-tilassa.

Monet tiimit ottavat käytännössä käyttöön sykliä:

_arvioi offline -> ota käyttöön -> valvo online -> kerää uusia virhetapauksia -> lisää offline-aineistoon -> hienosäädä agenttia -> toista_.

## Yleisiä ongelmia

Kun otat tekoälyagentteja tuotantoon, saatat kohdata useita haasteita. Tässä on joitain yleisiä ongelmia ja niiden mahdollisia ratkaisuja:

| **Ongelma**    | **Mahdollinen ratkaisu**   |
| ------------- | ------------------ |
| Tekoälyagentti ei suorita tehtäviä johdonmukaisesti | - Hio agentille annettua kehotetta; ole selkeä tavoitteista.<br>- Tunnista, missä tehtävät voidaan jakaa osatehtäviin ja hoitaa useilla agenteilla. |
| Tekoälyagentti ajautuu jatkuviin silmukoihin | - Varmista, että sinulla on selkeät päättymisehdot, jotta agentti tietää milloin lopettaa prosessi.<br>- Monimutkaisiin tehtäviin, jotka vaativat päättelyä ja suunnittelua, käytä suurempaa mallia, joka on erikoistunut päättelytehtäviin. |
| Tekoälyagentin työkalukutsut eivät toimi hyvin | - Testaa ja validoi työkalun tuloksia agenttijärjestelmän ulkopuolella.<br>- Hio parametrien, kehotteiden ja työkalujen nimeämistä. |
| Moniagenttijärjestelmä ei toimi johdonmukaisesti | - Hio kullekin agentille annettuja kehotteita varmistaaksesi, että ne ovat spesifisiä ja erillisiä toisistaan.<br>- Rakenna hierarkkinen järjestelmä, jossa on "reititys" tai ohjausagentti päättämässä, mikä agentti on oikea. |

Monet näistä ongelmista voidaan havaita tehokkaammin, kun havaittavuus on käytössä. Aiemmin käsitellyt jäljet ja mittarit auttavat paikallistamaan tarkan kohdan agentin työnkulussa, jossa ongelmat ilmenevät, mikä tekee virheenkorjauksesta ja optimoinnista paljon tehokkaampaa.

## Kustannusten hallinta


Tässä on joitakin strategioita hallita AI-agenttien käyttöönoton kustannuksia tuotannossa:

**Pienempien mallien käyttäminen:** Pienet kielimallit (SLM) voivat suoriutua hyvin tietyissä agenttikäyttötapauksissa ja vähentävät kustannuksia merkittävästi. Kuten aiemmin mainittiin, suorituskyvyn arvioimiseksi ja vertailemiseksi suurempiin malleihin rakentaminen on paras tapa ymmärtää, kuinka hyvin SLM toimii omassa käyttötapauksessasi. Harkitse SLM:ien käyttöä yksinkertaisempiin tehtäviin kuten intentin luokitteluun tai parametrien poimintaan, ja varaa suuremmat mallit monimutkaiseen päättelyyn.

**Reititinmallin käyttäminen:** Samankaltainen strategia on käyttää erilaisia malleja ja kokoja. Voit käyttää LLM:ää/SLM:ää tai serverless-toimintoa ohjaamaan pyynnöt monimutkaisuuden perusteella parhaiten sopiviin malleihin. Tämä auttaa myös vähentämään kustannuksia samalla kun varmistetaan suorituskyky oikeissa tehtävissä. Esimerkiksi reititä yksinkertaiset kyselyt pienemmille, nopeammille malleille ja käytä kalliita suuria malleja vain monimutkaisiin päättelytehtäviin.

**Vastausten välimuisti:** Yleisten pyyntöjen ja tehtävien tunnistaminen ja vastausten tarjoaminen ennen agenttijärjestelmän läpikäyntiä on hyvä tapa vähentää samanlaisten pyyntöjen määrää. Voit jopa toteuttaa virran, joka arvioi kuinka samanlainen pyyntö on välimuistissa oleviin pyyntöihisi käyttämällä perustason AI-malleja. Tämä strategia voi merkittävästi vähentää kustannuksia usein kysyttyjen kysymysten tai yleisten työnkulkujen kohdalla.

## Katsotaan miten tämä toimii käytännössä

Tässä [osion esimerkkimuistikirjassa](./code_samples/10-expense_claim-demo.ipynb) näemme esimerkkejä siitä, kuinka voimme käyttää havainnointityökaluja agenttimme seuraamiseen ja arviointiin.


### Onko sinulla lisää kysymyksiä AI-agenteista tuotannossa?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tapaaaksesi muita oppijoita, osallistuaksesi vastaanottoaikoihin ja saadaksesi vastauksia AI-agenttikysymyksiisi.

## Edellinen oppitunti

[Metakognitiodesignmalli](../09-metacognition/README.md)

## Seuraava oppitunti

[Agenttiset protokollat](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->