# AI-agentit tuotannossa: havaittavuus ja arviointi

[![AI Agents in Production](../../../translated_images/fi/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kun AI-agentit siirtyvät kokeellisista prototyypeistä todellisiin sovelluksiin, kyky ymmärtää niiden käyttäytymistä, seurata suorituskykyä ja systemaattisesti arvioida niiden tuottamia tuloksia tulee tärkeäksi.

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat/ymmärrät:
- Agenttien havaittavuuden ja arvioinnin ydinkäsitteet
- Tekniikat agenttien suorituskyvyn, kustannusten ja tehokkuuden parantamiseksi
- Mitä ja miten arvioida AI-agenttejasi systemaattisesti
- Miten hallita kustannuksia AI-agenttien tuotantoon käyttöönotossa
- Miten instrumentoida Microsoft Agent Frameworkilla rakennetut agentit

Tavoitteena on antaa sinulle tieto muuttaa "mustaksi laatikoksi" jäävät agenttisi läpinäkyviksi, hallittaviksi ja luotettaviksi järjestelmiksi.

_**Huom:** On tärkeää ottaa käyttöön turvallisia ja luotettavia AI-agentteja. Tutustu myös [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md) -oppituntiin._

## Jäljet ja osat

Havaittavuustyökalut kuten [Langfuse](https://langfuse.com/) tai [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) kuvaavat yleensä agentin suoritusprosessit jälkinä ja osina.

- **Jälki** tarkoittaa koko agentin tehtävää alusta loppuun (kuten käyttäjän kyselyn käsittely).
- **Osat** ovat jäljen yksittäisiä vaiheita (kuten kielimallin kutsu tai tiedon haku).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Kuva URL säilytetty kuvaustarkoituksessa -->

Ilman havaittavuutta AI-agentti voi tuntua "mustalta laatikolta" – sen sisäinen tila ja päättely ovat epämääräisiä, mikä vaikeuttaa ongelmien diagnosointia tai suorituskyvyn optimointia. Havaittavuuden avulla agentit muuttuvat "lasilaatikoiksi", jotka tarjoavat läpinäkyvyyttä, välttämätöntä luottamuksen rakentamiseksi ja varmistamiseksi, että ne toimivat tarkoitetulla tavalla.

## Miksi havaittavuus on tärkeää tuotantoympäristöissä

AI-agenttien siirtäminen tuotantoympäristöihin tuo mukanaan uusia haasteita ja vaatimuksia. Havaittavuus ei ole enää "kiva lisä", vaan kriittinen kyvykkyys:

*   **Virheiden selvitys ja juurisyyn analyysi**: Kun agentti epäonnistuu tai tuottaa odottamattoman tuloksen, havaittavuustyökalut tarjoavat jäljet, joiden avulla virheen lähde voidaan paikantaa. Tämä on erityisen tärkeää monimutkaisissa agenteissa, joissa voi olla useita LLM-kutsuja, työkalujen vuorovaikutuksia ja ehtopäätöksiä.
*   **Viiveen ja kustannusten hallinta**: AI-agentit käyttävät usein LLM:ää ja muita ulkoisia API:ita, jotka veloittavat per token tai kutsu. Havaittavuus mahdollistaa näiden kutsujen tarkan seurannan, auttaen tunnistamaan hitaat tai kalliit toiminnot. Tämä mahdollistaa tiimien optimoida kehotteet, valita tehokkaampia malleja tai muokata työnkulkuja operatiivisten kustannusten hallitsemiseksi ja käyttökokemuksen varmistamiseksi.
*   **Luottamus, turvallisuus ja vaatimustenmukaisuus**: Monissa sovelluksissa on tärkeää varmistaa, että agentit toimivat turvallisesti ja eettisesti. Havaittavuus tarjoaa auditointijäljen agentin toiminnasta ja päätöksistä. Tätä voidaan käyttää havaitsemaan ja ehkäisemään ongelmia kuten kehotteen manipulointi, haitallisen sisällön luonti tai henkilötietojen virheellinen käsittely. Voit esimerkiksi tarkastella jälkiä ymmärtääksesi, miksi agentti antoi tietyn vastauksen tai käytti tiettyä työkalua.
*   **Jatkuvat parannussilmukat**: Havaittavuustiedot ovat iteratiivisen kehitysprosessin perusta. Seuraamalla agenttien suorituskykyä todellisessa maailmassa tiimit voivat tunnistaa parannuskohteita, kerätä tietoa mallien hienosäätöä varten ja testata muutosten vaikutusta. Tämä luo palautesilmukan, jossa tuotantoympäristöstä saatavat tiedot online-arvioinnista ohjaavat offline-kokeiluja ja parannuksia, mikä johtaa asteittain parempaan suorituskykyyn.

## Tärkeitä seurattavia mittareita

Agentin käyttäytymisen seuraamiseksi ja ymmärtämiseksi on seurattava useita mittareita ja signaaleja. Mittarit voivat vaihdella agentin tarkoituksen mukaan, mutta jotkut ovat yleisesti tärkeitä.

Tässä joitakin yleisimmin havaittavuustyökalujen mittaamia mittareita:

**Viive:** Kuinka nopeasti agentti vastaa? Pitkät odotusajat heikentävät käyttäjäkokemusta. Sinun tulee mitata viivettä tehtävissä ja yksittäisissä vaiheissa seuraamalla agentin suorituksia. Esimerkiksi agentti, joka käyttää 20 sekuntia kaikkiin mallikutsuihin, voi nopeutua käyttämällä nopeampaa mallia tai suorittamalla mallikutsut rinnakkain.

**Kustannukset:** Paljonko agentin suoritus maksaa? AI-agenttien LLM-kutsut ja ulkoiset API:t veloittavat usein per token tai kutsu. Usein toistuvat työkalujen käyttökerrat tai useat kehotteet voivat nopeasti kasvattaa kustannuksia. Esimerkiksi, jos agentti kutsuu LLM:ää viisi kertaa marginaalisen laadun parantamiseksi, on arvioitava, onko kustannus perusteltu vai voisiko kutsumäärää vähentää tai käyttää halvempaa mallia. Reaaliaikainen seuranta auttaa myös havaitsemaan odottamattomat piikit (esim. virheet aiheuttavat ylisuuret API-silmukat).

**Pyyntövirheet:** Kuinka monta pyyntöä agentti epäonnistui suorittamaan? Tämä voi sisältää API-virheitä tai epäonnistuneita työkalukutsuja. Voit tehdä agentistasi tuotannossa kestävämmän näitä vastaan ottamalla käyttöön varajärjestelmiä tai uudelleenkokeiluja. Esim. jos LLM-palvelin A on pois käytöstä, vaihdat varapalvelimeksi LLM-palvelin B:n.

**Käyttäjäpalaute:** Suorat käyttäjäarviot tarjoavat arvokkaita näkemyksiä. Tämä voi sisältää eksplisiittisiä arvioita (👍peukku ylös/👎alas, ⭐1–5 tähteä) tai tekstuaalisia kommentteja. Toistuva negatiivinen palaute tulisi herättää varoituksen, koska se on merkki, että agentti ei toimi odotetulla tavalla.

**Implisiittinen käyttäjäpalaute:** Käyttäjien käyttäytyminen antaa epäsuoraa palautetta myös ilman eksplisiittisiä arvioita. Tämä voi sisältää välittömiä kysymyksen uudelleenilmaisuja, toistuvia kyselyjä tai uudelleenyrittämispainikkeen käyttöä. Esim. jos näet, että käyttäjät kysyvät samaa asiaa uudestaan ja uudestaan, tämä on osoitus siitä, että agentti ei toimi odotetusti.

**Tarkkuus:** Kuinka usein agentti tuottaa oikeita tai toivottuja tuloksia? Tarkkuuden määritelmät vaihtelevat (esim. ongelmanratkaisun oikeellisuus, tiedonhaun tarkkuus, käyttäjätyytyväisyys). Ensimmäinen askel on määrittää, mitä menestys tarkoittaa agentillesi. Voit seurata tarkkuutta automatisoitujen tarkastusten, arviointipisteiden tai tehtävän suorittamisen merkintöjen avulla. Esimerkiksi merkitsemällä jäljet "onnistui" tai "epäonnistui".

**Automaattiset arviointimittarit:** Voit myös asettaa automaattisia arviointeja. Esimerkiksi voit käyttää LLM:ää pisteyttämään agentin tuottamaa sisältöä, esim. onko se hyödyllinen, tarkka tai ei. Saatavilla on myös useita avoimen lähdekoodin kirjastoja, jotka auttavat pisteyttämään agentin eri osa-alueita. Esim. [RAGAS](https://docs.ragas.io/) RAG-agentteja varten tai [LLM Guard](https://llm-guard.com/) haitallisen kielen tai kehotteiden manipuloinnin havaitsemiseen.

Käytännössä näiden mittareiden yhdistelmä antaa parhaan kokonaiskuvan AI-agentin terveydestä. Tässä luvussa olevan [esimerkkikansion](./code_samples/10-expense_claim-demo.ipynb) avulla näytämme, miltä nämä mittarit näyttävät todellisissa esimerkeissä, mutta ensin opettelemme tyypillisen arviointityönkulun.

## Instrumentoi agenttisi

Jäljitystietojen keräämiseksi sinun tulee instrumentoida koodisi. Tavoitteena on instrumentoida agentin koodi tuottamaan jälkiä ja mittareita, jotka havaittavuusalusta voi tallentaa, käsitellä ja visualisoida.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) on noussut alan standardiksi LLM-havaittavuudessa. Se tarjoaa sarjan API:ita, SDK:ita ja työkaluja telemetriatietojen luomiseen, keräämiseen ja vientiin.

On olemassa monia instrumentointikirjastoja, jotka kietovat olemassa olevat agenttikehykset ja helpottavat OpenTelemetry-spanssien vientiä havaittavuustyökaluun. Microsoft Agent Framework integroituu OpenTelemetryyn natiivisti. Alla on esimerkki MAF-agentin instrumentoinnista:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentin suoritus jäljitetään automaattisesti
    pass
```


Tämän luvun [esimerkkikansio](./code_samples/10-expense_claim-demo.ipynb) näyttää, miten instrumentoit MAF-agentin.

**Spanien luominen manuaalisesti:** Vaikka instrumentointikirjastot tarjoavat hyvän pohjan, usein tarvitaan tarkempaa tai räätälöityä tietoa. Voit luoda spanseja käsin lisätäksesi sovelluslogiikkaa. Vielä tärkeämpää on, että voit rikastaa automaattisesti tai manuaalisesti luotuja spanseja omilla attribuuteilla (tunnetaan myös tageina tai metatietoina). Nämä attribuutit voivat sisältää liiketoimintakohtaisia tietoja, välivaihelaskelmia tai muuta kontekstia, joka on hyödyllistä virheenkorjauksessa tai analyysissa, kuten `user_id`, `session_id` tai `model_version`.

Esimerkki jälkien ja spanien manuaalisesta luomisesta [Langfuse Python SDK:lla](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```


## Agentin arviointi

Havaittavuus antaa meille mittareita, mutta arviointi on prosessi, jossa analysoidaan näitä tietoja (ja tehdään testejä) sen selvittämiseksi, kuinka hyvin AI-agentti toimii ja miten sitä voidaan parantaa. Toisin sanoen, kun sinulla on nämä jäljet ja mittarit, miten käytät niitä arvioidaksesi agenttia ja tehdäkseen päätöksiä?

Säännöllinen arviointi on tärkeää, koska AI-agentit ovat usein epädeterministisiä ja ne voivat kehittyä (päivitysten tai mallikäyttäytymisen muuttumisen seurauksena) – ilman arviointia et tietäisi, tekeekö "älykäs agenttisi" työtehtävänsä hyvin vai taantuuko se.

AI-agenttien arviointia on kahta päätyyppiä: **online-arviointi** ja **offline-arviointi**. Molemmat ovat arvokkaita ja täydentävät toisiaan. Usein aloitetaan offline-arvioinnista, koska se on vähimmäisvaatimus agentin käyttöönoton edellytyksenä.

### Offline-arviointi

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Tämä tarkoittaa agentin arviointia hallitussa ympäristössä, tyypillisesti käyttämällä testidatasettejä eikä live-käyttäjäkyselyjä. Käytät huolellisesti valittuja datasettejä, joissa tiedät odotetun tuloksen tai oikean toiminnan, ja ajat agentin niiden päällä.

Esimerkiksi, jos olet rakentanut matematiikan sanatehtävä-agentin, sinulla voi olla [testidataset](https://huggingface.co/datasets/gsm8k), jossa on 100 ongelmaa ja tunnetut vastaukset. Offline-arviointi tehdään usein kehitysvaiheessa (ja voi olla osa CI/CD-putkea) parannusten tarkistamiseksi tai taantumien estämiseksi. Etuna on, että se on **toistettavissa ja saat selkeät tarkkuusmittarit, koska sinulla on totuustiedot**. Saatat myös simuloida käyttäjäkyselyitä ja mitata agentin vastauksia ihanteellisia vastauksia vastaan tai käyttää automaattisia mittareita edellä kuvatulla tavalla.

Haasteena offline-arvioinnissa on varmistaa, että testidataset on kattava ja pysyy ajan tasalla – agentti voi toimia hyvin kiinteällä testiaineistolla, mutta kohdata täysin erilaisia kyselyjä tuotantoympäristössä. Siksi testiaineistot tulee pitää ajan tasalla uusilla reunatapauksilla ja esimerkeillä, jotka heijastavat reaalimaailman tilanteita. Pieniä "savutestitapauksia" ja laajempia arviointisarjoja kannattaa käyttää rinnakkain: pieniä nopeisiin tarkastuksiin ja suuria kattavampien suoritustietojen saamiseksi.

### Online-arviointi

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Tämä tarkoittaa agentin arviointia reaaliaikaisessa, todellisessa ympäristössä eli tuotannon käytön aikana. Online-arviointi sisältää agentin suorituskyvyn seuraamista oikeiden käyttäjävuorovaikutusten perusteella ja tulosten jatkuvaa analysointia.

Esimerkiksi voit seurata onnistumisprosentteja, käyttäjätyytyväisyyspisteitä tai muita mittareita live-liikenteessä. Online-arvioinnin etu on, että se **havaitsee asioita, joita et osaisi odottaa laboratorioympäristössä** – voit nähdä mallin käyttäytymisen heikkenemisen ajan myötä (jos efektiviteetti laskee syötteen muuttumisen takia) ja havaita odottamattomia kyselyjä tai tilanteita, joita ei ollut testiaineistossa. Se tarjoaa todellisen kuvan agentin toiminnasta luonnossa.

Online-arviointi sisältää usein eksplisiittisen ja implisiittisen käyttäjäpalautteen keräämistä sekä mahdollisesti varjotestejä tai A/B-testejä (missä uusi agentin versio ajetaan rinnakkain vanhan kanssa vertailua varten). Haasteena on, että live-interaktioille voi olla vaikea saada luotettavia luokituksia tai pisteytyksiä – saatat joutua luottamaan käyttäjäpalautteeseen tai jälkiseurannan mittareihin (kuten klikkasiko käyttäjä tulosta).

### Kahden yhdistäminen

Online- ja offline-arvioinnit eivät ole toisiaan poissulkevia; ne täydentävät toisiaan hyvin. Online-seurannan havainnot (esim. uudet käyttäjäkyselyt, joissa agentti toimii heikosti) voidaan käyttää täydentämään ja parantamaan offline-testidatassa. Toisaalta agentit, jotka menestyvät hyvin offline-testeissä, voidaan ottaa luottavaisemmin käyttöön ja seurata online-ympäristössä.

Useat tiimit noudattavat silmukkaa:

_offline-arviointi -> käyttöönotto -> online-seuranta -> uusien epäonnistumistapauksien keruu -> lisäys offline-dataan -> agentin hienosäätö -> toisto_.

## Tavalliset ongelmat

Kun otat AI-agentteja käyttöön tuotannossa, saatat kohdata erilaisia haasteita. Tässä joitakin yleisiä ongelmia ja niiden potentiaalisia ratkaisuja:

| **Ongelma**    | **Mahdollinen ratkaisu**   |
| ------------- | ------------------ |
| AI-agentti ei suorita tehtäviä johdonmukaisesti | - Hienosäädä agentille annettua kehotetta; ole selkeä tavoitteiden kanssa.<br>- Tunnista, milloin tehtävät kannattaa pilkkoa osatehtäviin ja käsitellä niitä useamman agentin kautta. |
| AI-agentti jää jatkuviin silmukoihin  | - Varmista, että sinulla on selkeät päättymisehdot, jotta agentti tietää, milloin prosessi lopetetaan.<br>- Monimutkaisiin tehtäviin, jotka vaativat päättelyä ja suunnittelua, käytä isompaa mallia, joka on erikoistunut päättelytehtäviin. |
| AI-agentin työkalukutsut eivät toimi hyvin   | - Testaa ja validoi työkalun tuotos erillään agenttijärjestelmästä.<br>- Hienosäädä määriteltyjä parametreja, kehotteita ja työkalujen nimeämistä.  |
| Moniagenttijärjestelmä ei toimi johdonmukaisesti | - Hienosäädä kullekin agentille annettuja kehotteita, jotta ne ovat spesifisiä ja toisistaan erillisiä.<br>- Rakenna hierarkkinen järjestelmä käyttämällä "reititys"- tai ohjausagenttia, joka päättää, mikä agentti on oikea. |

Monet näistä ongelmista voidaan tunnistaa tehokkaammin, kun havaittavuus on käytössä. Aiemmin käsitellyt jäljet ja mittarit auttavat paikantamaan tarkalleen, missä agentin työnkulussa ongelmat esiintyvät, mikä tekee virheiden korjauksesta ja optimoinnista paljon tehokkaampaa.

## Kustannusten hallinta
Tässä on joitakin strategioita AI-agenttien käyttöönoton kustannusten hallintaan tuotannossa:

**Pienempien mallien käyttäminen:** Pienet kielimallit (SLM) voivat suoriutua hyvin tietyissä agenttipohjaisissa käyttötapauksissa ja vähentää kustannuksia merkittävästi. Kuten aiemmin mainittiin, suorituskyvyn arvioimiseksi ja vertailuksi suurempiin malleihin paras tapa on rakentaa arviointijärjestelmä. Harkitse SLM-mallien käyttöä yksinkertaisemmissa tehtävissä, kuten intentin luokittelussa tai parametrien poiminnassa, kun taas suuremmat mallit varataan monimutkaiseen päättelyyn.

**Reititinmallin käyttäminen:** Samankaltainen strategia on käyttää monipuolisia malleja ja kokoja. Voit käyttää LLM- tai SLM-mallia tai palvelimettomia funktioita reitittämään pyynnöt niiden monimutkaisuuden perusteella sopivimmille malleille. Tämä auttaa myös kustannusten vähentämisessä sekä varmistaa suorituskyvyn oikeissa tehtävissä. Esimerkiksi reititä yksinkertaiset kyselyt pienemmille, nopeammille malleille ja käytä kalliita suuria malleja vain monimutkaisiin päättelytehtäviin.

**Vastausten välimuistin käyttäminen:** Yleisten pyyntöjen ja tehtävien tunnistaminen ja vastausten antaminen ennen niiden kulkua agenttipohjaisen järjestelmän läpi on hyvä tapa vähentää samanlaisten pyyntöjen määrää. Voit jopa toteuttaa prosessin, jolla tunnistetaan kuinka samanlaisia pyynnöt ovat välimuistitettuihin pyyntöihin käyttäen yksinkertaisempia AI-malleja. Tämä strategia voi merkittävästi pienentää kustannuksia usein toistuvissa kysymyksissä tai yleisissä työnkuluissa.

## Katsotaan miten tämä toimii käytännössä

[Tämän osion esimerkkinotebookissa](./code_samples/10-expense_claim-demo.ipynb) näemme esimerkkejä siitä, miten voimme käyttää havainnointityökaluja seurataksemme ja arvioidaksemme agenttiamme.


### Onko lisää kysymyksiä AI-agenteista tuotannossa?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia AI-agentteihin liittyviin kysymyksiisi.

## Edellinen oppitunti

[Metakognition suunnittelumalli](../09-metacognition/README.md)

## Seuraava oppitunti

[Agenttiperusteiset protokollat](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->