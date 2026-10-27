# AI-agentit tuotannossa: havaittavuus ja arviointi

[![AI Agents in Production](../../../translated_images/fi/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kun AI-agentit siirtyvät kokeiluversioista todellisiin sovelluksiin, niiden käyttäytymisen ymmärtäminen, suorituskyvyn seuranta ja systemaattinen tuotosten arviointi muuttuvat tärkeiksi.

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat/ymmärrät:
- Agenttien havaittavuuden ja arvioinnin keskeiset käsitteet
- Tekniikat agenttien suorituskyvyn, kustannusten ja tehokkuuden parantamiseen
- Mitä ja miten AI-agentteja arvioidaan systemaattisesti
- Kuinka hallita kustannuksia AI-agenttien tuotantoon käyttöönotossa
- Kuinka instrumentoida Microsoft Agent Frameworkilla rakennettuja agentteja

Tavoite on varustaa sinut tiedolla, jolla voit muuttaa "mustat laatikko" -agenttisi läpinäkyviksi, hallittaviksi ja luotettaviksi järjestelmiksi.

_**Huom:** On tärkeää ottaa käyttöön AI-agentteja, jotka ovat turvallisia ja luotettavia. Tutustu myös oppituntiin [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Jäljet ja jaksot

Havaittavuustyökalut kuten [Langfuse](https://langfuse.com/) tai [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) kuvaavat yleensä agentin ajokerrat jälkinä (traces) ja jaksoina (spans).

- **Jälki (Trace)** kuvaa täydellistä agentin tehtävää alusta loppuun (esim. käyttäjän kyselyn käsittely).
- **Jaksot (Spans)** ovat yksittäisiä vaiheita jäljen sisällä (esim. kielimallin kutsu tai datan nouto).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Ilman havaittavuutta AI-agentti voi tuntua "mustalta laatikolta" – sen sisäinen tila ja päättely ovat läpinäkymättömiä, mikä vaikeuttaa ongelmien diagnosointia tai suorituskyvyn optimointia. Havaittavuuden avulla agentit muuttuvat "lasi-laatikoiksi", jotka tarjoavat läpinäkyvyyttä, mikä on välttämätöntä luottamuksen rakentamiseksi ja toimintavarmuuden varmistamiseksi. 

## Miksi havaittavuus on tärkeää tuotantoympäristöissä

Siirtyminen AI-agenteilla tuotantoympäristöihin tuo mukanaan uusia haasteita ja vaatimuksia. Havaittavuus ei ole enää "kiva lisä", vaan kriittinen ominaisuus:

*   **Virheenkorjaus ja syynmäärittely:** Kun agentti epäonnistuu tai tuottaa odottamattoman tuloksen, havaittavuustyökalut tarjoavat jäljet virheen lähteen paikantamiseen. Tämä on erityisen tärkeää monimutkaisissa agenteissa, joissa voi olla useita LLM-kutsuja, työkalujen vuorovaikutuksia ja ehtologista logiikkaa.
*   **Viive ja kustannusten hallinta:** AI-agentit käyttävät usein LLM-malleja ja muita ulkoisia API-kutsuja, jotka veloitetaan tokenista tai kutsusta. Havaittavuus mahdollistaa näiden kutsujen tarkan seurannan, auttaen tunnistamaan liiallisen hitaita tai kalliita operaatioita. Tämä mahdollistaa kehotteiden optimoinnin, tehokkaampien mallien valinnan tai työnkulkujen uudelleensuunnittelun operatiivisten kustannusten hallitsemiseksi ja käyttäjäkokemuksen varmistamiseksi.
*   **Luottamus, turvallisuus ja vaatimustenmukaisuus:** Monissa sovelluksissa on tärkeää varmistaa, että agentit toimivat turvallisesti ja eettisesti. Havaittavuus tarjoaa agenttien toimien ja päätösten tarkistajäljen. Tätä voidaan käyttää havaitsemaan ja lieventämään ongelmia kuten kehotteiden manipulointia, haitallisen sisällön tuottamista tai henkilötietojen väärinkäsittelyä. Esimerkiksi voit tarkastella jälkiä ymmärtääksesi, miksi agentti antoi tietyn vastauksen tai käytti tiettyä työkalua.
*   **Jatkuvan parantamisen silmukat:** Havaittavuustiedot ovat toistuvan kehitysprosessin perusta. Seuraamalla agenttien suorituskykyä todellisessa käytössä tiimit voivat tunnistaa parannuskohteita, kerätä tietoa mallien hienosäätöön ja validoida muutosten vaikutuksia. Tämä luo palautesilmukan, jossa tuotantoympäristön oheisarviointi ohjaa offline-kokeiluja ja hiomista, mikä johtaa asteittain parempaan agenttien suorituskykyyn.

## Keskeiset seurattavat mittarit

Agenttien käyttäytymisen seuraamiseksi ja ymmärtämiseksi tulisi seurata useita mittareita ja signaaleja. Vaikka tarkat mittarit voivat vaihdella agentin tarkoituksen mukaan, jotkut ovat yleisesti tärkeitä.

Tässä muutamia yleisimmistä mittareista, joita havaittavuustyökalut seuraavat:

**Viive:** Kuinka nopeasti agentti vastaa? Pitkät odotusajat heikentävät käyttäjäkokemusta. Viivettä tulisi mitata tehtävien ja yksittäisten vaiheiden osalta jälkiä seuraamalla. Esimerkiksi agentti, joka käyttää 20 sekuntia kaikkiin mallikutsuihin, voisi olla nopeampi käyttämällä nopeampaa mallia tai suorittamalla kutsut rinnakkain.

**Kustannukset:** Mikä on kustannus per agentin ajo? AI-agentit käyttävät LLM-kutsuja, jotka veloitetaan tokenista tai ulkoisista API-kutsuista. Tiheä työkalujen käyttö tai useat kehotteet voivat nopeasti nostaa kustannuksia. Esimerkiksi jos agentti kutsuu LLM:ää viisi kertaa laadun marginal parantamiseksi, on harkittava, onko kustannus oikeutettu vai voisiko kutsujen määrää vähentää tai käyttää halvempaa mallia. Reaaliaikainen seuranta voi myös auttaa havaitsemaan odottamattomia piikkejä (esimerkiksi bugit, jotka aiheuttavat liiallisia API-silmukoita).

**Pyyntövirheet:** Kuinka monta pyyntöä agentti epäonnistui käsittelemään? Tämä voi sisältää API-virheitä tai epäonnistuneita työkalukutsuja. Tehdäksesi agentista vikasietoisemman tuotannossa, voit määrittää varajärjestelmiä tai uudelleenkokeiluja. Esimerkiksi jos LLM-palveluntarjoaja A on poissa käytöstä, voit vaihtaa palveluntarjoajaan B varajärjestelmänä.

**Käyttäjäpalautteet:** Suorat käyttäjäarvioinnit tarjoavat arvokasta tietoa. Tämä voi sisältää selkeitä arvioita (👍peukku ylös / 👎 alas, ⭐1-5 tähteä) tai tekstimuotoisia kommentteja. Jatkuvasti negatiivinen palaute tulee huomioida varoituksena siitä, että agentti ei toimi odotetusti.

**Epäsuora käyttäjäpalautteet:** Käyttäjäkäyttäytyminen tarjoaa epäsuoraa palautetta ilman suoria arvosteluja. Tämä voi olla välitöntä kysymyksen uudelleenmuotoilua, toistuvia kyselyjä tai uudelleenkokeilupainikkeen klikkaamista. Esimerkiksi jos havaitaan, että käyttäjät kysyvät usein samaa kysymystä uudelleen, se on merkki siitä, että agentti ei toimi odotetusti.

**Tarkkuus:** Kuinka usein agentti tuottaa oikein tai toivottuja vastauksia? Tarkkuuden määritelmät vaihtelevat (esim. ongelmanratkaisun oikeellisuus, tiedonhaku, käyttäjätyytyväisyys). Ensimmäinen askel on määritellä, mitä menestys tarkoittaa agentillesi. Voit seurata tarkkuutta automaattisten tarkistusten, arviointipisteiden tai tehtävän valmistumismerkkien kautta. Esimerkiksi merkitsemällä jäljet "onnistuneiksi" tai "epäonnistuneiksi".

**Automaattiset arviointimittarit:** Voit myös tehdä automaattisia arviointeja. Esimerkiksi voit käyttää LLM:ää arvioimaan agentin tuottaman tuloksen hyödyllisyyden, tarkkuuden tai muutoin. Lisäksi useat avoimen lähdekoodin kirjastot auttavat arvioimaan eri näkökulmia, esim. [RAGAS](https://docs.ragas.io/) RAG-agentteihin tai [LLM Guard](https://github.com/protectai/llm-guard) haitallisen kielen tai kehotteen manipuloinnin tunnistamiseen.

Käytännössä näiden mittarien yhdistelmä antaa parhaan kuvan AI-agentin terveydestä. Tässä luvussa [esimerkkimuistikirja](./code_samples/10-expense_claim-demo.ipynb) näyttää, miltä nämä mittarit näyttävät käytännössä, mutta ensin opimme, miltä tyypillinen arviointityönkulku näyttää.

## Instrumentoi agenttisi

Jälkitietojen keräämiseksi sinun täytyy instrumentoida koodisi. Tavoitteena on tehdä agentin koodista sellainen, että se tuottaa jälkiä ja mittareita, jotka havaittavuusalusta voi kerätä, käsitellä ja visualisoida.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) on noussut alan standardiksi LLM-havaittavuudelle. Se tarjoaa joukko API-rajapintoja, SDK:ita ja työkaluja telemetriadatan generointiin, keräykseen ja vientiin.

On olemassa monia instrumentointikirjastoja, jotka kääriytyvät olemassa olevien agenttikehysten ympärille ja helpottavat OpenTelemetry-jaksojen vientiä havaittavuustyökaluun. Microsoft Agent Framework tukee OpenTelemetria natiivisti. Alla on esimerkki MAF-agentin instrumentoinnista:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass
```

Tässä luvun [esimerkkimuistikirjassa](./code_samples/10-expense_claim-demo.ipynb) näytetään, kuinka instrumentoida MAF-agenttisi.

**Manuaalinen jaksojen luonti:** Vaikka instrumentointikirjastot tarjoavat hyvän perustan, joskus tarvitaan yksityiskohtaisempaa tai räätälöityä tietoa. Voit luoda jaksoja manuaalisesti lisätäksesi mukautettua sovelluslogiikkaa. Tärkeämpää on, että voit rikastaa automaattisesti tai manuaalisesti luotuja jaksoja omilla ominaisuuksilla (tunnetaan myös tageina tai metadatana). Nämä ominaisuudet voivat sisältää liiketoimintaan liittyvää dataa, välivaiheen laskelmia tai mitä tahansa kontekstia, joka voi olla hyödyllistä virheiden etsinnässä tai analyysissä, kuten `user_id`, `session_id` tai `model_version`.

Esimerkki jälkien ja jaksojen manuaalisesta luomisesta [Langfuse Python SDK]:lla (https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentin arviointi

Havaittavuus antaa meille mittareita, mutta arviointi on prosessi, jossa analysoidaan nämä tiedot (ja suoritetaan testejä) määritelläksemme, kuinka hyvin AI-agentti toimii ja kuinka sitä voidaan parantaa. Toisin sanoen, kun sinulla on nuo jäljet ja mittarit, miten käytät niitä agentin arviointiin ja päätösten tekemiseen?

Säännöllinen arviointi on tärkeää, koska AI-agentit ovat usein ei-deterministisiä ja voivat kehittyä (päivitysten tai mallin käyttäytymisen muuttumisen kautta) – ilman arviointia et tietäisi, tekeekö "älykäs agenttisi" todella tavoitteensa mukaisesti vai onko se heikentynyt.

AI-agenttien arviointiin on kaksi kategoriaa: **verkkopohjainen arviointi (online evaluation)** ja **offline-arviointi**. Molemmat ovat arvokkaita ja täydentävät toisiaan. Aloitamme yleensä offline-arvioinnista, sillä se on vähimmäisvaatimus ennen agentin käyttöönottoa.

### Offline-arviointi

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Tämä tarkoittaa agentin arviointia kontrolloidussa ympäristössä, yleensä testaamalla aiemman aineiston avulla, ei live-käyttäjäkyselyillä. Käytät huolellisesti valittuja aineistoja, joissa tiedetään odotettu tulos tai oikea toimintatapa, ja ajat agenttisi niiden päällä.

Esimerkiksi, jos olet rakentanut matemaattisten sanatehtävien agentin, sinulla saattaa olla [testiaineisto](https://huggingface.co/datasets/openai/gsm8k) 100 tunnetulla vastauksella. Offline-arviointi tehdään usein kehityksen aikana (ja voi olla osa CI/CD-putkia) parannusten tarkistamiseen tai taantumien estämiseen. Hyöty on siinä, että se on **toistettavissa ja voit saada selkeät tarkkuusmittarit, koska sinulla on totuusvertailu**. Voit myös simuloida käyttäjäkyselyjä ja mitata agentin vastauksia ihanteellisiin vastauksiin tai käyttää automaattisia mittareita kuten yllä kuvattiin.

Offline-arvioinnin suurin haaste on varmistaa, että testiaineisto on kattava ja pysyy ajantasaisena – agentti voi onnistua hyvin kiinteällä testiaineistolla, mutta kohdata hyvin erilaisia kyselyitä tuotannossa. Siksi testiaineistot tulisi pitää päivitettyinä uusilla rajatapauksilla ja aidoista tilanteista. Pieni "savutesti" ja laajemmat arviointiaineistot ovat hyödyllisiä: pienet aineistot nopeisiin tarkistuksiin ja suuremmat laajempiin suorituskykymittauksiin.

### Online-arviointi

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Tämä tarkoittaa agentin arviointia reaaliajassa tosielämän ympäristössä, eli tuotannossa sen oikean käytön aikana. Online-arviointi sisältää agentin suorituskyvyn seurantaa aidossa käyttäjävuorovaikutuksessa ja tulosten jatkuvaa analysointia.

Esimerkiksi saatat seurata onnistumisprosentteja, käyttäjätyytyväisyyspisteitä tai muita mittareita live-liikenteessä. Online-arvioinnin etuna on, että se **paljastaa asioita, joita et ehkä odottanut laboratorioympäristössä** – voit havaita mallin ajallisen heikkenemisen (jos agentin tehokkuus heikkenee syötteiden muuttuessa) ja poikkeavia kyselyitä tai tilanteita, joita testiaineistossa ei ollut. Se antaa todenmukaisen kuvan agentin käyttäytymisestä luonnossa.

Online-arviointi sisältää usein niin piilotettua kuin suoraakin käyttäjäpalautetta, kuten aikaisemmin keskusteltiin, ja mahdollisesti varjotestauksia tai A/B-testausta (missä agentin uusi versio ajetaan rinnakkain vanhan kanssa vertailua varten). Haasteena on, että luotettavan luokittelun tai pisteytyksen saaminen livenäkökohdasta voi olla hankalaa – voit joutua luottamaan käyttäjäpalautteeseen tai jälkiseurannan mittareihin (esim. klikkasiko käyttäjä tulosta).

### Näiden yhdistäminen

Online- ja offline-arvioinnit eivät ole toisensa poissulkevia; ne tukevat hyvin toisiaan. Online-seurannan havainnot (esim. uudet käyttäjäkyselyt, joissa agentti toimii huonosti) voidaan käyttää offline-testausaineistojen täydentämiseen ja parantamiseen. Vastaavasti hyvin offline-testeissä menestyvät agentit voidaan luottavaisemmin ottaa käyttöön ja seurata online-ympäristössä.

Monet tiimit käyttävät kiertoa:

_arvioi offlinessa -> ota käyttöön -> seuraa onlinessa -> kerää uudet epäonnistumistapaukset -> lisää offline-aineistoon -> hienosäädä agenttia -> toista_.

## Yleisiä ongelmia

Kun otat AI-agentteja tuotantoon, kohtaat monia haasteita. Tässä on joitain yleisiä ongelmia ja niiden mahdollisia ratkaisuja:

| **Ongelma**    | **Mahdollinen ratkaisu**   |
| ------------- | ------------------ |
| AI-agentti ei tee tehtäviä johdonmukaisesti | - Paranna agentille annettua kehotetta; ole selkeä tavoitteiden suhteen.<br>- Tunnista, missä tehtävät voidaan jakaa alatehtäviin ja hoitaa useamman agentin yhteistyöllä. |
| AI-agentti joutuu jatkuviin silmukoihin  | - Varmista selkeät lopettamiskriteerit, jotta agentti tietää, milloin prosessi loppuu.<br>- Monimutkaisissa tehtävissä, joissa tarvitaan päättelyä ja suunnittelua, käytä isompaa mallia, joka on erikoistunut päättelyyn. |
| AI-agentin työkalukutsut eivät toimi hyvin   | - Testaa ja validoi työkalun tulos agenttijärjestelmän ulkopuolella.<br>- Paranna työkalujen parametreja, kehotteita ja nimeämiskäytäntöjä.  |
| Moniagenttijärjestelmä ei toimi johdonmukaisesti | - Paranna jokaiselle agentille annettuja kehotteita varmistaaksesi, että ne ovat spesifisiä ja erillisiä toisistaan.<br>- Rakenna hierarkkinen järjestelmä, jossa "reititys"- tai ohjuriagentti päättää, mikä agentti on oikea. |

Monet näistä ongelmista voidaan tunnistaa tehokkaammin, kun havaittavuus on käytössä. Aiemmin käsitellyt jäljet ja mittarit auttavat paikantamaan ongelmien tarkan sijainnin agentin työnkulussa, mikä tekee virheenkorjauksesta ja optimoinnista paljon tehokkaampaa.

## Kustannusten hallinta

Tässä joitain strategioita AI-agenttien tuotantoon käyttöönoton kustannusten hallintaan:

**Pienten mallien käyttäminen:** Pienet kielimallit (SLM) voivat suoriutua hyvin tietyissä agenttiperustaisissa käyttötapauksissa ja vähentävät kustannuksia merkittävästi. Kuten aiemmin mainittiin, arviointijärjestelmän rakentaminen suorituskyvyn määrittämiseksi ja vertailuksi suurempiin malleihin on paras tapa ymmärtää, kuinka hyvin SLM suoriutuu omassa käyttötapauksessasi. Harkitse SLM:ien käyttöä yksinkertaisempiin tehtäviin, kuten intention luokitteluun tai parametrien poimintaan, ja varaa suuremmat mallit monimutkaiseen päättelyyn.

**Reititinmallin käyttäminen:** Samankaltainen strategia on käyttää erilaisia malleja ja kokoja. Voit käyttää LLM:ää/SLM:ää tai palvelintonta funktiota reitittämään pyynnöt monimutkaisuuden perusteella parhaiten sopiviin malleihin. Tämä auttaa myös vähentämään kustannuksia samalla kun varmistetaan suorituskyky oikeissa tehtävissä. Esimerkiksi ohjaa yksinkertaiset kyselyt pienemmille, nopeammille malleille ja käytä kalliita suuria malleja vain monimutkaisiin päättelytehtäviin.

**Vastausten välimuistitus:** Tavallisten pyyntöjen ja tehtävien tunnistaminen ja vastausten tarjoaminen ennen niiden kulkua agenttijärjestelmän läpi on hyvä tapa vähentää samanlaisten pyyntöjen määrää. Voit jopa toteuttaa prosessin, jossa tunnistetaan, kuinka samanlainen pyyntö on välimuistitetuille pyynnöillesi käyttämällä perustason tekoälymalleja. Tämä strategia voi merkittävästi vähentää kustannuksia usein kysyttyjen kysymysten tai yleisten työnkulkujen kohdalla.

## Katsotaan, miten tämä toimii käytännössä

[Tämän osion esimerkkimuistiossa](./code_samples/10-expense_claim-demo.ipynb) näemme esimerkkejä siitä, miten voimme käyttää havaittavuustyökaluja agenttimme seurantaan ja arviointiin.


### Lisää kysymyksiä tekoälyagenttien tuotannosta?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tapaamaan muita oppijoita, osallistumaan aukioloaikoihin ja saamaan vastauksia tekoälyagenttieksiin.

## Edellinen oppitunti

[Metakognition suunnittelumalli](../09-metacognition/README.md)

## Seuraava oppitunti

[Agenttiprotokollat](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->