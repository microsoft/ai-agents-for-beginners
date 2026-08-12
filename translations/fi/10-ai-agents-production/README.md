# AI-agentit tuotannossa: havaittavuus ja arviointi

[![AI Agents in Production](../../../translated_images/fi/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kun tekoälyagentit siirtyvät kokeellisista prototyypeistä todellisiin sovelluksiin, kyky ymmärtää niiden käyttäytymistä, seurata niiden suorituskykyä ja arvioida systemaattisesti niiden tuottamia tuloksia tulee tärkeäksi.

## Oppimistavoitteet

Tämän oppitunnin suorittamisen jälkeen osaat/ymmärrät:
- Agenttien havaittavuuden ja arvioinnin keskeiset käsitteet
- Menetelmiä agenttien suorituskyvyn, kustannusten ja tehokkuuden parantamiseen
- Mitä ja miten arvioida tekoälyagenttejasi systemaattisesti
- Miten hallita kustannuksia, kun otat AI-agentteja tuotantoon
- Miten instrumentoida Microsoft Agent Frameworkilla rakennettuja agentteja

Tavoitteena on varustaa sinut tiedolla, jolla voit muuttaa "mustat laatikot" -agenttisi läpinäkyviksi, hallittaviksi ja luotettaviksi järjestelmiksi.

_**Huom:** On tärkeää ottaa käyttöön turvallisia ja luotettavia tekoälyagentteja. Tutustu myös oppituntiin [Luotettavien tekoälyagenttien rakentaminen](../06-building-trustworthy-agents/README.md)._

## Jäljet ja laajuudet

Havaittavuustyökalut, kuten [Langfuse](https://langfuse.com/) tai [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), kuvaavat yleensä agentin suoritukset jälkinä ja laajuuksina.

- **Jälki** edustaa kokonaista agentin tehtävää alusta loppuun (kuten käyttäjäkyselyn käsittely).
- **Laajuudet** ovat yksittäisiä vaiheita jäljen sisällä (kuten kielimallin kutsuminen tai tiedon hakeminen).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Ilman havaittavuutta tekoälyagentti voi tuntua "mustalta laatikolta" – sen sisäinen tila ja päättely ovat läpinäkymättömiä, mikä vaikeuttaa ongelmien diagnosointia tai suorituskyvyn optimointia. Havaittavuuden avulla agentit muuttuvat "lasilaatikoiksi", tarjoten läpinäkyvyyttä, joka on olennaista luottamuksen rakentamiseksi ja sen varmistamiseksi, että ne toimivat tarkoitetulla tavalla.

## Miksi havaittavuus on tärkeää tuotantoympäristöissä

Siirtyminen tekoälyagenttien tuotantoympäristöihin tuo mukanaan uusia haasteita ja vaatimuksia. Havaittavuus ei ole enää "kiva lisä", vaan kriittinen ominaisuus:

*   **Virheenkorjaus ja ongelman perussyiden analyysi**: Kun agentti epäonnistuu tai tuottaa odottamattoman tuloksen, havaittavuustyökalut tarjoavat jäljet, jotka auttavat virheen lähteen paikantamisessa. Tämä on erityisen tärkeää monimutkaisissa agenteissa, jotka voivat sisältää useita LLM-kutsuja, työkalujen vuorovaikutuksia ja ehdollista logiikkaa.
*   **Viiveen ja kustannusten hallinta**: Tekoälyagentit käyttävät usein LLM:ää ja muita ulkoisia rajapintoja, joita veloitetaan tokenia tai kutsua kohden. Havaittavuus mahdollistaa näiden kutsujen tarkan seurannan, mikä auttaa tunnistamaan liian hitaita tai kalliita toimintoja. Tämä antaa tiimeille mahdollisuuden optimoida kehotteita, valita tehokkaampia malleja tai suunnitella työnkulkuja uudelleen hallitakseen operatiivisia kustannuksia ja varmistaakseen hyvän käyttökokemuksen.
*   **Luottamus, turvallisuus ja vaatimustenmukaisuus**: Monissa sovelluksissa on tärkeää varmistaa, että agentit käyttäytyvät turvallisesti ja eettisesti. Havaittavuus tarjoaa auditointilokin agenttien toimista ja päätöksistä. Tätä voidaan käyttää havaitsemaan ja lieventämään ongelmia, kuten kehotteiden manipulointia, haitallisen sisällön generointia tai henkilötietojen (PII) väärinkäsittelyä. Voit esimerkiksi tarkastella jälkiä ymmärtääksesi, miksi agentti antoi tietyn vastauksen tai käytti tiettyä työkalua.
*   **Jatkuvan parantamisen silmukat**: Havaittavuustiedot muodostavat iteratiivisen kehitysprosessin perustan. Seuraamalla, miten agentit suoriutuvat todellisessa ympäristössä, tiimit voivat tunnistaa kehitystarpeita, kerätä aineistoa mallien hienosäätöön ja validoida muutosten vaikutuksia. Tämä luo palautesilmukan, jossa tuotantoympäristön havainnot verkkotestaamisesta ohjaavat offline-kokeiluja ja parannuksia, mikä johtaa asteittain parempaan agentin suorituskykyyn.

## Keskeiset seurattavat mittarit

Agentin käyttäytymisen seuraamiseksi ja ymmärtämiseksi tulisi seurata erilaisia mittareita ja signaaleja. Vaikka tarkat mittarit voivat vaihdella agentin tarkoituksen mukaan, jotkut ovat universaalisti tärkeitä.

Tässä on joitakin yleisimpiä mittareita, joita havaittavuustyökalut seuraavat:

**Viive:** Kuinka nopeasti agentti vastaa? Pitkät odotusajat vaikuttavat negatiivisesti käyttäjäkokemukseen. Tulisi mitata viive tehtäville ja yksittäisille vaiheille jäljittämällä agentin suorituksia. Esimerkiksi agentti, joka käyttää 20 sekuntia kaikkiin mallikutsuihin, voidaan nopeuttaa käyttämällä nopeampaa mallia tai suorittamalla mallikutsut rinnakkain.

**Kustannukset:** Paljonko maksaa yksi agentin suoritus? AI-agentit käyttävät LLM-kutsuja, joista veloitetaan tokenia tai ulkoisia rajapintoja kohden. Työkalujen runsas käyttö tai useat kehotteet voivat nopeasti kasvattaa kustannuksia. Esimerkiksi, jos agentti kutsuu LLM:ää viisi kertaa marginaalisen laadun parantamiseksi, on arvioitava, onko kustannus perusteltu vai voisiko kutsujen määrää vähentää tai käyttää halvempaa mallia. Reaaliaikainen seuranta auttaa myös tunnistamaan odottamattomia kustannushuippuja (esim. bugit, jotka aiheuttavat liiallisia rajapintasilmukoita).

**Pyynnön virheet:** Kuinka monta pyyntöä agentti epäonnistui? Tämä voi sisältää API-virheitä tai epäonnistuneita työkalukutsuja. Tehdäkseen agentistasi kestävämmän tuotannossa, voit asettaa varajärjestelyjä tai uudelleenkutsuja. Esim. jos LLM-palveluntarjoaja A on pois käytöstä, vaihdat varalle LLM-palveluntarjoaja B:hen.

**Käyttäjäpalaute:** Suora käyttäjäarviointi antaa arvokasta tietoa. Tämä voi sisältää nimenomaisia arvioita (👍yllään/👎alaspäin, ⭐1-5 tähteä) tai tekstimuotoisia kommentteja. Johdonmukaisesti negatiivinen palaute tulisi herättää hälytysmerkkinä, sillä se kertoo, ettei agentti toimi odotetusti.

**Vihjeellinen käyttäjäpalaute:** Käyttäjän käyttäytyminen antaa epäsuoraa palautetta myös ilman suoria arvioita. Tämä voi sisältää välittömän kysymyksen uudelleenmuotoilun, toistuvat kyselyt tai uudelleenyrittämispainikkeen napsautuksen. Esim. jos näet, että käyttäjät kysyvät toistuvasti samaa kysymystä, se on merkki siitä, että agentti ei toimi odotetusti.

**Tarkkuus:** Kuinka usein agentti tuottaa oikeita tai toivottuja vastauksia? Tarkkuuden määritelmät vaihtelevat (esim. ongelmanratkaisun oikeellisuus, tiedonhaun tarkkuus, käyttäjätyytyväisyys). Ensimmäinen askel on määritellä, millainen onnistuminen agentillesi tarkoittaa. Voit seurata tarkkuutta automaattisilla tarkistuksilla, arviointipisteillä tai tehtävän suoritusmerkinnöillä. Esimerkiksi merkitsemällä jäljet "onnistuneiksi" tai "epäonnistuneiksi".

**Automaattiset arviointimittarit:** Voit myös asettaa automaattisia arviointeja. Esimerkiksi voit käyttää LLM:ää arvioimaan agentin tulosta, esimerkiksi onko se hyödyllinen, tarkka tai ei. Saatavilla on myös useita avoimen lähdekoodin kirjastoja, jotka auttavat arvioimaan agentin eri osa-alueita. Esim. [RAGAS](https://docs.ragas.io/) RAG-agentteihin tai [LLM Guard](https://llm-guard.com/) haitallisen kielen tai kehotteiden manipuloinnin havaitsemiseen.

Käytännössä näiden mittareiden yhdistelmä tarjoaa parhaan kattavuuden tekoälyagentin terveydestä. Tässä luvussa olevan [esimerkkimuistikirjan](./code_samples/10-expense_claim-demo.ipynb) avulla näytämme, miltä nämä mittarit näyttävät käytännön esimerkeissä, mutta ensin opettelemme, miltä tyypillinen arviointityönkulku näyttää.

## Instrumentoi agenttisi

Jäljitettävien tietojen keräämiseksi sinun täytyy instrumentoida koodisi. Tavoitteena on instrumentoida agentin koodi tuottamaan jälkiä ja mittareita, jotka voidaan tallentaa, käsitellä ja visualisoida havaittavuusalustan avulla.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) on noussut alan standardiksi LLM-havaittavuudessa. Se tarjoaa joukko API-rajapintoja, SDK:ita ja työkaluja telemetriadatan generointiin, keräämiseen ja vientiin.

On olemassa monia instrumentointikirjastoja, jotka kietovat olemassa olevat agenttikehykset ja helpottavat OpenTelemetry-laajuuksien vientiä havaittavuustyökaluun. Microsoft Agent Framework integroituu natiivisti OpenTelemetryyn. Alla esimerkki MAF-agentin instrumentoinnista:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentin suoritus jäljitetään automaattisesti
    pass
```

Tässä luvussa oleva [esimerkkimuistikirja](./code_samples/10-expense_claim-demo.ipynb) opastaa, kuinka instrumentoida MAF-agenttisi.

**Manuaalinen laajuuksien luonti:** Instrumentointikirjastot tarjoavat hyvän perusratkaisun, mutta usein tarvitaan yksityiskohtaisempaa tai räätälöityä tietoa. Voit luoda laajuuksia manuaalisesti lisätäksesi räätälöityä sovelluslogiikkaa. Vielä tärkeämpää on, että voit rikastuttaa automaattisesti tai manuaalisesti luotuja laajuuksia käyttäen räätälöityjä attribuutteja (tunnetaan myös tunnisteina tai metadatana). Nämä attribuutit voivat sisältää liiketoiminnallisia tietoja, välivaiheen laskelmia tai mitä tahansa kontekstia, joka voi olla hyödyllistä virheiden korjauksessa tai analyysissa, kuten `user_id`, `session_id` tai `model_version`.

Esimerkki jälkien ja laajuuksien manuaalisesta luomisesta [Langfuse Python SDK:n](https://langfuse.com/docs/sdk/python/sdk-v3) avulla:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentin arviointi

Havaittavuus antaa meille mittarit, mutta arviointi on prosessi, jossa analysoidaan nämä tiedot (ja tehdään testejä) määrittämään, kuinka hyvin tekoälyagentti suoriutuu ja miten sitä voidaan parantaa. Toisin sanoen, kun sinulla on nämä jäljet ja mittarit, miten käytät niitä agentin arvosteluun ja päätösten tekemiseen?

Säännöllinen arviointi on tärkeää, koska AI-agentit ovat usein epädeterministisiä ja voivat kehittyä (päivitysten tai mallin käyttäytymisen siirtymisen kautta) – ilman arviointia et tietäisi, tekeekö "älykäs agenttisi" työnsä hyvin vai onko sen suoritus heikentynyt.

AI-agenttien arvioinnissa on kaksi kategoriaa: **online-arviointi** ja **offline-arviointi**. Molemmat ovat arvokkaita ja täydentävät toisiaan. Aloitamme tavallisesti offline-arvioinnista, koska se on vähimmäistoimenpide ennen agentin käyttöönottoa.

### Offline-arviointi

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Tämä tarkoittaa agentin arviointia hallitussa ympäristössä, tyypillisesti käyttämällä testidatasettejä, ei live-käyttäjäkyselyjä. Käytät valikoituja aineistoja, joissa tiedät odotetun tuloksen tai oikean käyttäytymisen, ja ajat agenttisi niiden päällä.

Esimerkiksi, jos olet rakentanut matematiikan sanatehtäväagentin, sinulla saattaa olla [testiaineisto](https://huggingface.co/datasets/gsm8k), jossa on 100 tehtävää tunnetuilla vastauksilla. Offline-arviointi tehdään usein kehitysvaiheessa (ja se voi olla osa CI/CD-putkia) parannusten tarkistamiseksi tai regressioiden estämiseksi. Hyöty on, että se on **toistettavissa ja saat selkeitä tarkkuusmittareita, koska sinulla on totuustieto**. Voit myös simuloida käyttäjäkyselyjä ja mitata agentin vastauksia ihanteellisiin vastauksiin tai käyttää edellä kuvattuja automaattisia mittareita.

Haaste offline-arvioinnissa on varmistaa, että testiaineistojoukko on kattava ja pysyy relevanttina – agentti saattaa suoriutua hyvin kiinteällä testiajatuksella, mutta kohdata hyvin erilaisia kyselyitä tuotannossa. Siksi sinun tulee pitää testisarjat ajan tasalla uusilla reunatapauksilla ja esimerkeillä, jotka heijastavat todellisia tilanteita. Pieni "savukoe" -sarja ja suurempia arviointijoukkoja on hyödyllistä: pienet sarjat nopeiden tarkistusten tekemiseen ja suuremmat laajemman suorituskyvyn mittaamiseksi.

### Online-arviointi

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Tämä tarkoittaa agentin arviointia elävässä, todellisessa ympäristössä, eli tuotannon aikana käytön yhteydessä. Online-arviointi sisältää agentin suorituskyvyn jatkuvan seurannan todellisissa käyttäjävuorovaikutuksissa ja tulosten analysoinnin.

Esimerkiksi voit seurata onnistumisprosentteja, käyttäjätyytyväisyysarvioita tai muita mittareita liikenteessä. Online-arvioinnin etuna on, että se **tallentaa asioita, joita et välttämättä osaisi ennakoida laboratoriossa** – voit havaita mallin siirtymiä ajan kuluessa (jos agentin tehokkuus heikkenee, kun syötteen mallit muuttuvat) ja havaita odottamattomia kyselyitä tai tilanteita, joita testidatassa ei ollut. Se tarjoaa todenperäisen kuvan siitä, miten agentti käyttäytyy käytännössä.

Online-arviointi sisältää usein käyttäjän implisiittisen ja eksplisiittisen palautteen keräämisen, kuten aiemmin on kuvattu, ja mahdollisesti varjokokeiden tai A/B-testien tekemisen (missä uusi agenttiversio toimii rinnakkain vanhan kanssa vertailua varten). Haasteena on, että luotettavien tunnisteiden tai pisteiden saaminen live-käyttötilanteisiin voi olla hankalaa – saatat joutua tukeutumaan käyttäjäpalautteeseen tai seuraaviin mittareihin (esim. klikkasiko käyttäjä tulosta).

### Yhdistämällä ne

Online- ja offline-arvioinnit eivät ole toisiaan poissulkevia; ne täydentävät toisiaan hyvin. Online-seurannan havainnot (esim. uudet käyttäjäkyselytyypit, joissa agentti suoriutuu huonosti) voidaan käyttää laajentamaan ja parantamaan offline-testiaineistoja. Vastaavasti agentit, jotka pärjäävät hyvin offline-testeissä, voidaan ottaa käyttöön ja seurata luottavaisemmin online-ympäristössä.

Monet tiimit noudattavat silmukkaa:

_arvioi offline -> ota käyttöön -> seuraa online -> kerää uusia epäonnistumis tapauksia -> lisää offline-aineistoon -> paranna agenttia -> toista_.

## Yleisiä ongelmia

Kun otat tekoälyagentteja tuotantoon, saatat kohdata erilaisia haasteita. Tässä on joitakin yleisiä ongelmia ja niiden mahdolliset ratkaisut:

| **Ongelma**    | **Mahdollinen ratkaisu**   |
| ------------- | ------------------ |
| AI-agentti ei suorita tehtäviä johdonmukaisesti | - Tarkenna AI-agentille annettua kehotetta; ole selkeä tavoitteiden suhteen.<br>- Tunnista, missä tehtävät kannattaa jakaa alat tehtäviksi ja käsitellä niitä useammalla agentilla. |
| AI-agentti jää keskeytymättömiin silmukoihin | - Varmista, että sinulla on selkeät lopetus ehdot, jotta agentti tietää, milloin prosessi lopetetaan.<br>- Monimutkaisia tehtäviä, jotka vaativat päättelyä ja suunnittelua varten, käytä isompaa mallia, joka on erikoistunut päättelyyn. |
| AI-agentin työkalukutsut eivät toimi hyvin | - Testaa ja validoi työkalun tulos agenttijärjestelmän ulkopuolella.<br>- Tarkenna määriteltyjä parametreja, kehotteita ja työkalujen nimityksiä.  |
| Moni-agenttijärjestelmä ei toimi johdonmukaisesti | - Tarkenna jokaiselle agentille annettuja kehotteita varmistaaksesi, että ne ovat spesifejä ja eroavat toisistaan.<br>- Rakenna hierarkkinen järjestelmä käyttämällä "reititys" tai ohjausagenttia määrittelemään oikea agentti. |

Monet näistä ongelmista voidaan havaita tehokkaammin, kun havaittavuus on käytössä. Aiemmin mainitut jäljet ja mittarit auttavat paikallistamaan tarkasti, missä agentin työnkulussa ongelmat esiintyvät, jolloin virheenkorjaus ja optimointi sujuvat paljon tehokkaammin.

## Kustannusten hallinta


Tässä on joitakin strategioita tekoälyagenttien käyttökustannusten hallintaan tuotannossa:

**Pienempien mallien käyttäminen:** Pienet kielimallit (SLM) voivat toimia hyvin tietyissä agenttisissa käyttötapauksissa ja vähentävät kustannuksia merkittävästi. Kuten aiemmin mainittiin, arviointijärjestelmän rakentaminen suorituskyvyn määrittämiseksi ja vertailemiseksi isompien mallien kanssa on paras tapa ymmärtää, miten hyvin SLM toimii käyttötapauksessasi. Harkitse SLM:ien käyttöä yksinkertaisemmissa tehtävissä, kuten aikomuksen luokittelussa tai parametrien poiminnassa, samalla kun varaat suuremmat mallit monimutkaiseen päättelyyn.

**Reititinmallin käyttäminen:** Samankaltainen strategia on käyttää erikokoisia ja -tyyppisiä malleja. Voit käyttää LLM:ää/SLM:ää tai serverless-funktiota reitittämään pyynnöt monimutkaisuuden perusteella parhaiten sopiviin malleihin. Tämä auttaa myös alentamaan kustannuksia ja varmistaa suorituskyvyn oikeissa tehtävissä. Esimerkiksi reititä yksinkertaiset kyselyt pienemmille, nopeammille malleille ja käytä kalliita suuria malleja vain monimutkaisiin päättelytehtäviin.

**Vastausten välimuisti:** Yleisten pyyntöjen ja tehtävien tunnistaminen ja vastausten antaminen ennen niiden etenemistä agenttijärjestelmäsi läpi on hyvä tapa vähentää samanlaisten pyyntöjen määrää. Voit jopa toteuttaa prosessin, jolla tunnistetaan, kuinka samanlainen pyyntö on välimuistissa oleviin pyyntöihin käyttäen yksinkertaisempia tekoälymalleja. Tämä strategia voi merkittävästi vähentää kustannuksia usein kysytyissä kysymyksissä tai yleisissä työnkuluissa.

## Katsotaanpa, miten tämä toimii käytännössä

Tässä [osion esimerkkimuistikirjassa](./code_samples/10-expense_claim-demo.ipynb) näemme esimerkkejä siitä, miten voimme käyttää havaittavuustyökaluja agenttimme valvontaan ja arviointiin.


### Onko sinulla lisää kysymyksiä tekoälyagenteista tuotannossa?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tapaamaan muita oppijoita, osallistumaan aukioloihin ja saamaan vastauksia tekoälyagenttikysymyksiisi.

## Edellinen oppitunti

[Metakognition suunnittelumalli](../09-metacognition/README.md)

## Seuraava oppitunti

[Agenttikohtaiset protokollat](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->