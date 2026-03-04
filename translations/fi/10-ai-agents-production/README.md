# AI-agentit tuotannossa: havaittavuus ja arviointi

[![AI-agentit tuotannossa](../../../translated_images/fi/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kun AI-agentit siirtyvät kokeiluprojekteista todellisiin käyttötapauksiin, kyky ymmärtää niiden käyttäytymistä, seurata suorituskykyä ja arvioida tuloksia järjestelmällisesti muuttuu tärkeäksi.

## Oppimistavoitteet

Tämän oppitunnin jälkeen tiedät/ymmärrät:
- Agenttien havaittavuuden ja arvioinnin keskeiset käsitteet
- Tekniikoita agenttien suorituskyvyn, kustannusten ja tehokkuuden parantamiseen
- Mitä ja miten arvioida AI-agenttejasi järjestelmällisesti
- Kuinka hallita kustannuksia AI-agenttien tuotantokäytössä
- Kuinka instrumentoida agentteja, jotka on rakennettu AutoGenillä

Tavoitteena on antaa sinulle tieto muuttaa "mustat laatikot" läpinäkyviksi, hallittaviksi ja luotettaviksi järjestelmiksi.

_**Huom:** On tärkeää ottaa tuotantoon turvallisia ja luotettavia AI-agentteja. Tutustu myös oppituntiin [Luotettavien AI-agenttien rakentaminen](../06-building-trustworthy-agents/README.md)._

## Tracet ja spanit

Havaittavuustyökalut, kuten [Langfuse](https://langfuse.com/) tai [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), esittävät yleensä agentin suoritukset trace- ja span-rakenteina.

- **Trace** edustaa kokonaista agentin tehtävää alusta loppuun (esim. käyttäjäkyselyn käsittelyä).
- **Spans** ovat yksittäisiä askeleita tracessa (esim. kielimallin kutsu tai tiedon hakeminen).

![Trace-puu Langfusessa](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Ilman havaittavuutta AI-agentti voi tuntua "musta laatikolta" — sen sisäinen tila ja päättely ovat läpinäkymättömiä, mikä vaikeuttaa vikojen diagnosointia tai suorituskyvyn optimointia. Havaittavuuden avulla agentit muuttuvat "lasisiksi laatikoiksi", tarjoten läpinäkyvyyttä, joka on välttämätöntä luottamuksen rakentamiseksi ja sen varmistamiseksi, että ne toimivat tarkoitetulla tavalla.

## Miksi havaittavuus on tärkeää tuotantoympäristöissä

AI-agenttien siirtäminen tuotantoon tuo mukanaan uuden joukon haasteita ja vaatimuksia. Havaittavuus ei ole enää "kiva lisä", vaan kriittinen ominaisuus:

*   **Debuggaus ja juurisyiden analyysi**: Kun agentti epäonnistuu tai tuottaa odottamattoman tuloksen, havaittavuustyökalut tarjoavat tracet, joiden avulla virheen lähde voidaan paikantaa. Tämä on erityisen tärkeää monimutkaisissa agenteissa, joissa voi olla useita LLM-kutsuja, työkalujen vuorovaikutuksia ja ehdollista logiikkaa.
*   **Viiveen ja kustannusten hallinta**: AI-agentit luottavat usein LLM:iin ja muihin ulkoisiin rajapintoihin, joista laskutetaan token-perusteisesti tai kutsua kohden. Havaittavuus mahdollistaa näiden kutsujen tarkan seurannan, mikä auttaa tunnistamaan liian hitaita tai kalliita operaatioita. Tämä antaa tiimeille mahdollisuuden optimoida kehotteita, valita tehokkaampia malleja tai suunnitella työnkulkuja uudelleen hallitakseen käyttökustannuksia ja varmistaa hyvä käyttäjäkokemus.
*   **Luottamus, turvallisuus ja vaatimustenmukaisuus**: Monissa sovelluksissa on tärkeää varmistaa, että agentit käyttäytyvät turvallisesti ja eettisesti. Havaittavuus tarjoaa agentin toimien ja päätösten tarkastuspolun. Sitä voidaan käyttää esimerkiksi prompt injectionin, haitallisen sisällön generoinnin tai henkilötietojen (PII) väärinkäsittelyn havaitsemiseen ja lieventämiseen. Voit esimerkiksi tarkastella traceja ymmärtääksesi, miksi agentti antoi tietyn vastauksen tai käytti tiettyä työkalua.
*   **Jatkuvan parantamisen silmukat**: Havaittavuustiedot muodostavat iteratiivisen kehitysprosessin perustan. Seuraamalla, miten agentit toimivat todellisessa maailmassa, tiimit voivat tunnistaa parannuskohteita, kerätä tietoa mallien hienosäätöä varten ja validoida muutosten vaikutuksia. Tämä luo palautesilmukan, jossa tuotannon online-arvioinnista saadut havainnot ohjaavat offline-kokeilua ja hienosäätöä, johtuen vähitellen parempaan agentin suorituskykyyn.

## Keskeiset seurattavat mittarit

Agentin käyttäytymisen seuraamiseksi ja ymmärtämiseksi tulisi mitata useita mittareita ja signaaleja. Vaikka tarkat mittarit voivat vaihdella agentin tehtävän mukaan, osa on yleisesti tärkeitä.

Tässä ovat yleisimmät mittarit, joita havaittavuustyökalut seuraavat:

**Viive (Latency):** Kuinka nopeasti agentti vastaa? Pitkät odotusajat heikentävät käyttäjäkokemusta. Mittaa viivettä tehtävien ja yksittäisten vaiheiden osalta tracerunien avulla. Esimerkiksi agentti, joka tarvitsee 20 sekuntia kaikkiin mallikutsuihin, voitaisiin nopeuttaa käyttämällä nopeampaa mallia tai suorittamalla mallikutsut rinnakkain.

**Kustannukset:** Paljonko kustannus per agentin suoritus? AI-agentit käyttävät LLM-kutsuja tai ulkoisia API:ita, joista laskutetaan token- tai kutsuperusteisesti. Työkalujen usein toistuva käyttö tai useat kehotteet voivat nopeasti kasvattaa kustannuksia. Esimerkiksi jos agentti kutsuu LLM:ää viisi kertaa marginaalisen laadun parantamiseksi, on arvioitava, onko kustannus perusteltu vai voisiko kutsujen määrää vähentää tai käyttää halvempaa mallia. Reaaliaikainen seuranta voi myös auttaa tunnistamaan odottamattomat piikit (esim. bugit, jotka aiheuttavat liiallisia API-silmukoita).

**Pyyntövirheet:** Kuinka monessa pyynnössä agentti epäonnistui? Tämä voi sisältää API-virheitä tai epäonnistuneita työkalukutsuja. Tehdäksesi agentistasi kestävämmän tuotannossa, voit ottaa käyttöön varatoimenpiteitä tai uudelleenyrittämisiä. Esim. jos LLM-palveluntarjoaja A on alhaalla, vaihdat varalla olevaan LLM-palveluntarjoajaan B.

**Käyttäjäpalautteet:** Suorat käyttäjäarvioinnit antavat arvokkaita tietoja. Tämä voi sisältää eksplisiittisiä luokituksia (👍peukku ylös/👎peukku alas, ⭐1-5 tähteä) tai tekstimuotoisia kommentteja. Johdonmukainen negatiivinen palaute tulisi ottaa hälytyksenä, koska se kertoo, että agentti ei toimi odotetulla tavalla.

**Implisiittinen käyttäjäpalautteen:** Käyttäjäkäyttäytyminen antaa epäsuoraa palautetta ilman eksplisiittisiä arvioita. Tämä voi sisältää välittömän kysymyksen uudelleenmuotoilun, toistuvia kyselyjä tai uudelleenyrittopainikkeen klikkauksen. Esim. jos näet, että käyttäjät kysyvät samaa kysymystä toistuvasti, se on merkki siitä, että agentti ei toimi odotetusti.

**Tarkkuus (Accuracy):** Kuinka usein agentti tuottaa oikeita tai toivottavia vastauksia? Tarkkuuden määritelmät vaihtelevat (esim. ongelmanratkaisun oikeellisuus, tiedonhakutarkkuus, käyttäjätyytyväisyys). Ensimmäinen askel on määritellä, miltä menestys näyttää agentillesi. Voit seurata tarkkuutta automaattisilla tarkistuksilla, arviointipisteillä tai tehtävän suorittamisen tunnuksilla. Esimerkiksi merkitsemällä traceja "onnistunut" tai "epäonnistunut".

**Automaattiset arviointimittarit:** Voit myös rakentaa automaattisia arviointeja. Esimerkiksi voit käyttää LLM:ää pisteyttämään agentin tuotosta, esim. onko se hyödyllinen, tarkka tai ei. On myös useita avoimen lähdekoodin kirjastoja, jotka auttavat pisteyttämään eri osa-alueita agentista. Esim. [RAGAS](https://docs.ragas.io/) RAG-agenteille tai [LLM Guard](https://llm-guard.com/) haitallisen kielen tai prompt injectionin havaitsemiseen.

Käytännössä näiden mittareiden yhdistelmä antaa parhaan yleiskuvan AI-agentin tilasta. Tässä luvussa oleva [esimerkkimuistio](./code_samples/10_autogen_evaluation.ipynb) näyttää, miltä nämä mittarit näyttävät todellisissa esimerkeissä, mutta ensin opitaan, millainen tyypillinen arviointityönkulku on.

## Instrumentoi agenttisi

Tracedatan keräämiseksi sinun täytyy instrumentoida koodisi. Tavoitteena on instrumentoida agenttikoodi lähettämään traceja ja mittareita, jotka voidaan kaapata, käsitellä ja visualisoida havaittavuusalustalla.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) on noussut LLM-havaittavuuden teollisuuden standardiksi. Se tarjoaa joukon API:ita, SDK:ita ja työkaluja telemetriadatan generointiin, keräämiseen ja vientiin.

On olemassa monia instrumentointikirjastoja, jotka kääreltäviä olemassa olevien agenttikehysten päälle ja helpottavat OpenTelemetry-spanien vientiä havaittavuustyökaluun. Alla on esimerkki AutoGen-agentin instrumentoinnista käyttäen [OpenLit-instrumentointikirjastoa](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

Tämän luvun [esimerkkimuistio](./code_samples/10_autogen_evaluation.ipynb) näyttää, kuinka instrumentoit AutoGen-agenttisi.

**Manuaalinen spanien luominen:** Vaikka instrumentointikirjastot tarjoavat hyvän peruslähestymistavan, usein tarvitaan yksityiskohtaisempaa tai mukautettua tietoa. Voit luoda spanit manuaalisesti lisätäksesi mukautettua sovelluslogiikkaa. Vielä tärkeämpää, voit rikastaa automaattisesti tai manuaalisesti luotuja span:eja mukautetuilla attribuuteilla (tunnetaan myös tageina tai metatietoina). Nämä attribuutit voivat sisältää liiketoimintasovelluksen tietoja, välivaiheen laskelmia tai mitä tahansa kontekstia, joka voi olla hyödyllistä debuggausta tai analyysiä varten, kuten `user_id`, `session_id`, tai `model_version`.

Esimerkki tracejen ja spanien luomisesta manuaalisesti [Langfuse Python SDK:n](https://langfuse.com/docs/sdk/python/sdk-v3) avulla:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentin arviointi

Havaittavuus antaa meille mittareita, mutta arviointi on prosessi, jossa analysoidaan niitä tietoja (ja suoritetaan testejä) määrittääksesi, kuinka hyvin AI-agentti suoriutuu ja miten sitä voi parantaa. Toisin sanoen, kun sinulla on ne tracet ja mittarit, miten käytät niitä agentin arvosteluun ja päätöksentekoon?

Säännöllinen arviointi on tärkeää, koska AI-agentit ovat usein ei-deterministisiä ja voivat kehittyä (päivitysten tai mallin käyttäytymisen siirtymien kautta) – ilman arviointia et tietäisi, tekeekö "älykäs agenttisi" tehtävänsä hyvin vai onko sen suoritus heikentynyt.

Arvioinnit jaetaan kahteen kategoriaan: **online-arviointi** ja **offline-arviointi**. Molemmat ovat arvokkaita ja täydentävät toisiaan. Yleensä aloitetaan offline-arvioinnilla, koska se on vähimmäisvaatimus ennen agentin käyttöönottoa.

### Offline-arviointi

![Aineiston kohteet Langfusessa](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Tämä tarkoittaa agentin arviointia kontrolloidussa ympäristössä, tyypillisesti käyttämällä testiaineistoja, ei live-käyttäjäkyselyjä. Käytät kuratoituja aineistoja, joissa tiedät odotetun tuloksen tai oikean käyttäytymisen, ja ajat agenttisi niiden läpi.

Esimerkiksi, jos olet rakentanut matematiikan sanatehtäväagentin, saatat omata [testiaineiston](https://huggingface.co/datasets/gsm8k) 100 ongelmalla, joiden vastaukset ovat tiedossa. Offline-arviointi tehdään usein kehityksen aikana (ja se voi olla osa CI/CD-putkea) tarkistamaan parannukset tai suojata regressioilta. Hyöty on, että se on **toistettavissa ja saat selkeät tarkkuusmittarit, koska sinulla on ground truth**. Saatat myös simuloida käyttäjäkyselyjä ja mitata agentin vastauksia ihanteellisia vastauksia vastaan tai käyttää automaattisia mittareita kuten yllä on kuvattu.

Offline-arvioinnin keskeinen haaste on varmistaa, että testiaineisto on kattava ja pysyy relevanttina – agentti saattaa suoriutua hyvin kiinteässä testijoukossa mutta kohdata hyvin erilaisia kyselyjä tuotannossa. Siksi testijoukkoja tulisi päivittää uusilla reunatapauksilla ja esimerkeillä, jotka heijastavat todellisia skenaarioita​. Pieniä "pikatestejä" ja suurempia arviointisettejä yhdistävä lähestymistapa on hyödyllinen: pienet setit nopeisiin tarkistuksiin ja suuremmat laajempien suorituskykymittareiden saamiseksi​.

### Online-arviointi

![Havaittavuusmittareiden yleiskatsaus](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Tämä viittaa agentin arviointiin live-ympäristössä, eli todellisen tuotantokäytön aikana. Online-arviointi sisältää agentin suorituskyvyn seuraamisen todellisissa käyttäjävuorovaikutuksissa ja jatkuvan tulosten analysoinnin.

Esimerkiksi saatat seurata onnistumisprosentteja, käyttäjätyytyväisyysarvioita tai muita mittareita live-liikenteessä. Online-arvioinnin etu on, että se **paljastaa asioita, joita et välttämättä osannut odottaa laboratoriotilanteessa** – voit havaita mallin siirtymän ajan myötä (jos agentin tehokkuus heikkenee syötteiden muuttumisen myötä) ja havaita odottamattomia kyselyjä tai tilanteita, joita ei ollut testidatassa​. Se tarjoaa todellisen kuvan siitä, miten agentti käyttäytyy todellisessa ympäristössä.

Online-arviointi sisältää usein implisiittisen ja eksplisiittisen käyttäjäpalautteen keruun, kuten aiemmin kuvattu, ja mahdollisesti shadow-testien tai A/B-testien suorittamisen (missä uusi agenttiversio ajetaan rinnakkain vanhan kanssa vertailua varten). Haasteena on, että live-vuorovaikutuksille voi olla vaikea saada luotettavia merkintöjä tai pisteitä – saatat joutua tukeutumaan käyttäjäpalautteeseen tai välillisiin mittareihin (kuten klikattiinko tulosta).

### Yhdistäminen

Online- ja offline-arvioinnit eivät ole toisiaan poissulkevia; ne täydentävät toisiaan. Online-seurannasta saadut havainnot (esim. uudet käyttäjäkyselytyypit, joissa agentti suoriutuu huonosti) voidaan käyttää offline-testiaineistojen laajentamiseen ja parantamiseen. Vastaavasti agentit, jotka menestyvät hyvin offline-testeissä, voidaan ottaa luottavaisemmin käyttöön ja valvoa online-ympäristössä.

Monet tiimit käyttävät itse asiassa silmukkaa:

_arvioi offline -> ota käyttöön -> valvo online-tilassa -> kerää uudet virhetilanteet -> lisää offline-datasettiin -> hienosäädä agenttia -> toista_.

## Yleisiä ongelmia

Kun siirrät AI-agentteja tuotantoon, voit kohdata erilaisia haasteita. Tässä on joitakin yleisiä ongelmia ja niiden mahdollisia ratkaisuja:

| **Ongelma**    | **Mahdollinen ratkaisu**   |
| ------------- | ------------------ |
| AI-agentti ei suorita tehtäviä johdonmukaisesti | - Hienosäädä agentille annettua promptia; ole selkeä tavoitteiden kanssa.<br>- Tunnista, missä tehtävät kannattaa jakaa alitehtäviin ja antaa useammalle agentille. |
| AI-agentti ajautuu jatkuviin silmukoihin  | - Varmista, että sinulla on selkeät lopetusehdot, jotta agentti tietää, milloin prosessi tulee lopettaa.<br>- Monimutkaisissa tehtävissä, jotka vaativat päättelyä ja suunnittelua, käytä suurempaa mallia, joka on erikoistunut päättelytehtäviin. |
| AI-agentin työkalukutsut eivät toimi hyvin   | - Testaa ja validoi työkalun tuotosta agenttijärjestelmän ulkopuolella.<br>- Hienosäädä määriteltyjä parametreja, kehotteita ja työkalujen nimeämistä.  |
| Moniagenttijärjestelmä ei toimi johdonmukaisesti | - Hienosäädä kullekin agentille annettuja kehotteita varmistaaksesi, että ne ovat spesifisiä ja erottuvat toisistaan.<br>- Rakenna hierarkkinen järjestelmä käyttämällä "reititys-" tai ohjausagenttia määrittämään, mikä agentti on oikea. |

Monet näistä ongelmista voidaan tunnistaa tehokkaammin, kun havaittavuus on paikoillaan. Aiemmin käsitellyt traced ja mittarit auttavat paikantamaan täsmälleen, missä agentin työnkulussa ongelmat ilmenevät, mikä tekee debuggaamisesta ja optimoinnista paljon tehokkaampaa.

## Kustannusten hallinta
Tässä on joitain strategioita tekoälyagenttien käyttöönoton kustannusten hallintaan tuotannossa:

**Pienempien mallien käyttö:** Pienet kielimallit (SLMs) voivat suoriutua hyvin tietyissä agenttipohjaisissa käyttötapauksissa ja vähentävät kustannuksia merkittävästi. Kuten aiemmin mainittiin, arviointijärjestelmän rakentaminen suorituskyvyn määrittämiseksi ja vertailuksi suurempiin malleihin on paras tapa ymmärtää, miten hyvin pieni kielimalli suoriutuu omassa käyttötapauksessasi. Harkitse pienten kielimallien käyttämistä yksinkertaisempiin tehtäviin, kuten aikomuksen luokitteluun tai parametrien poimintaan, ja varaa suuremmat mallit monimutkaiseen päättelyyn.

**Reititysmallin käyttäminen:** Samankaltainen strategia on käyttää erilaisia malleja ja kokoja. Voit käyttää LLM/SLM:ää tai palvelimettomia funktioita reitittääksesi pyyntöjä kompleksisuuden mukaan parhaiten sopiville malleille. Tämä auttaa myös vähentämään kustannuksia ja varmistamaan suorituskyvyn oikeissa tehtävissä. Esimerkiksi reititä yksinkertaiset kyselyt pienemmille, nopeammille malleille, ja käytä kalliita suuria malleja vain monimutkaisiin päättelytehtäviin.

**Vastausten välimuistiin tallentaminen:** Yleisten pyyntöjen ja tehtävien tunnistaminen ja vastausten tarjoaminen ennen kuin ne kulkevat agenttipohjaisen järjestelmäsi läpi on hyvä tapa vähentää samanlaisten pyyntöjen määrää. Voit jopa toteuttaa työnkulun, joka tunnistaa, kuinka samanlainen pyyntö on välimuistiisi tallennettuihin pyyntöihin käyttäen yksinkertaisempia tekoälymalleja. Tämä strategia voi merkittävästi vähentää kustannuksia usein kysyttyjen kysymysten tai yleisten työnkulkujen kohdalla.

## Katsotaan, miten tämä toimii käytännössä

Tämän osion [esimerkkimuistikirjassa](./code_samples/10_autogen_evaluation.ipynb) näemme esimerkkejä siitä, miten voimme käyttää havaittavuustyökaluja agenttimme valvomiseen ja arviointiin.

### Onko sinulla lisää kysymyksiä tekoälyagenteista tuotannossa?

Liity [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) tapaamaan muita oppijoita, osallistumaan toimistoaikoihin ja saamaan vastauksia tekoälyagentteja koskeviin kysymyksiisi.

## Edellinen oppitunti

[Metakognition suunnittelumalli](../09-metacognition/README.md)

## Seuraava oppitunti

[Agenttiprotokollat](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastuuvapauslauseke:
Tämä asiakirja on käännetty tekoälykäännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattisissa käännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä on pidettävä auktoritatiivisena lähteenä. Tärkeää tietoa varten suositellaan ammattimaisen ihmiskääntäjän tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virheellisistä tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->