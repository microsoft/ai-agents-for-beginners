# AI-agentit tuotannossa: havaittavuus ja arviointi

[![AI-agentit tuotannossa](../../../translated_images/fi/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kun AI-agentit siirtyvät kokeellisista prototyypeistä todellisiin sovelluksiin, on tärkeää pystyä ymmärtämään niiden käyttäytymistä, seuraamaan niiden suorituskykyä ja arvioimaan järjestelmällisesti niiden tuloksia.

## Oppimistavoitteet

Tämän oppitunnin suorittamisen jälkeen tiedät/ymmärrät:
- Agentin havaittavuuden ja arvioinnin ydinkäsitteet
- Tekniikat agenttien suorituskyvyn, kustannusten ja tehokkuuden parantamiseksi
- Mitä ja miten arvioida AI-agenttejasi järjestelmällisesti
- Kuinka hallita kustannuksia, kun otat AI-agentit tuotantoon
- Kuinka instrumentoida Microsoft Agent Frameworkilla rakennettuja agenteja

Tavoitteena on antaa sinulle tiedot muuttaa "musta laatikko" -agentit läpinäkyviksi, hallittaviksi ja luotettaviksi järjestelmiksi.

_**Huom:** On tärkeää ottaa tuotantoon turvallisia ja luotettavia AI-agentteja. Tutustu myös [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md) -oppituntiin._

## Jäljet (traces) ja spanit (spans)

Havaittavuustyökalut, kuten [Langfuse](https://langfuse.com/) tai [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), kuvaavat yleensä agentin suoritukset jälkinä (traces) ja span:eina.

- **Trace** edustaa täydellistä agentin tehtävää alusta loppuun (kuten käyttäjäkyselyn käsittely).
- **Spans** ovat yksittäisiä vaiheita jäljen sisällä (kuten kielimallin kutsu tai tiedon noutaminen).

![Trace-puu Langfuse:ssa](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Ilman havaittavuutta AI-agentti voi tuntua "musta laatikolta" — sen sisäinen tila ja päättely ovat läpinäkymättömiä, mikä tekee ongelmien diagnosoinnista tai suorituskyvyn optimoinnista vaikeaa. Havaittavuuden avulla agentit muuttuvat "lasisiksi laatikoiksi", jotka tarjoavat läpinäkyvyyttä, mikä on oleellista luottamuksen rakentamiseksi ja sen varmistamiseksi, että ne toimivat tarkoitetulla tavalla.

## Miksi havaittavuus on tärkeää tuotantoympäristöissä

AI-agenttien siirtäminen tuotantoon tuo mukanaan uusia haasteita ja vaatimuksia. Havaittavuus ei ole enää "kiva lisä", vaan kriittinen ominaisuus:

*   **Vianetsintä ja juurisyyn analyysi**: Kun agentti epäonnistuu tai tuottaa odottamattoman tuloksen, havaittavuustyökalut tarjoavat jäljet, joiden avulla virheen lähde voidaan paikantaa. Tämä on erityisen tärkeää monimutkaisissa agenteissa, jotka voivat sisältää useita LLM-kutsuja, työkalujen vuorovaikutuksia ja ehdollista logiikkaa.
*   **Viiveen ja kustannusten hallinta**: AI-agentit käyttävät usein LLM:iä ja muita ulkoisia rajapintoja, joista veloitetaan per token tai per kutsu. Havaittavuus mahdollistaa näiden kutsujen tarkan seurannan, auttaen tunnistamaan hitaat tai kalliit toiminnot. Tämä antaa tiimeille mahdollisuuden optimoida kehotteita, valita tehokkaampia malleja tai suunnitella työnkulkuja uudelleen operatiivisten kustannusten hallitsemiseksi ja hyvän käyttäjäkokemuksen varmistamiseksi.
*   **Luottamus, turvallisuus ja vaatimustenmukaisuus**: Monissa sovelluksissa on tärkeää varmistaa, että agentit toimivat turvallisesti ja eettisesti. Havaittavuus antaa auditoitavan jäljen agentin toiminnoista ja päätöksistä. Tätä voidaan käyttää havaitsemaan ja lieventämään ongelmia, kuten prompt-injektiota, haitallisen sisällön tuottamista tai henkilötietojen (PII) väärinkäsittelyä. Esimerkiksi voit tarkastella jälkiä ymmärtääksesi, miksi agentti antoi tietyn vastauksen tai käytti tiettyä työkalua.
*   **Jatkuvan parantamisen silmukat**: Havaittavuustiedot muodostavat iteratiivisen kehitysprosessin perustan. Seuraamalla, miten agentit toimivat todellisessa maailmassa, tiimit voivat tunnistaa kehityskohteita, kerätä tietoa mallien hienosäätöä varten ja validoida muutosten vaikutuksia. Tämä luo palautesilmukan, jossa tuotannosta saadut havainnot online-arvioinnista vaikuttavat offline-kokeiluihin ja parannuksiin, mikä johtaa asteittain parempaan agentin suorituskykyyn.

## Tärkeimmät seurattavat mittarit

Agentin käyttäytymisen seuraamiseksi ja ymmärtämiseksi tulisi seurata erilaisia mittareita ja signaaleja. Tarkat mittarit voivat vaihdella agentin käyttötarkoituksen mukaan, mutta jotkut ovat yleisesti tärkeitä.

Tässä on joitakin yleisimpiä mittareita, joita havaittavuustyökalut seuraavat:

**Viive:** Kuinka nopeasti agentti vastaa? Pitkät odotusajat heikentävät käyttäjäkokemusta. Sinun tulisi mitata viivettä tehtävittäin ja yksittäisissä vaiheissa jäljittämällä agentin suorituksia. Esimerkiksi agentti, joka käyttää koko mallikutsuihin 20 sekuntia, voidaan nopeuttaa käyttämällä nopeampaa mallia tai suorittamalla mallikutsut rinnakkain.

**Kustannukset:** Mikä on kustannus per agentin suoritus? AI-agentit perustuvat LLM-kutsuihin tai ulkoisiin API-kutsuihin. Työkalujen tiheä käyttö tai useat kehotteet voivat nopeasti kasvattaa kuluja. Esimerkiksi jos agentti kutsuu LLM:ää viisi kertaa pienen laadunparannuksen vuoksi, on arvioitava, onko kustannus perusteltu vai voisiko kutsujen määrää vähentää tai käyttää halvempaa mallia. Reaaliaikainen seuranta voi myös auttaa tunnistamaan odottamattomia piikkejä (esim. bugit, jotka aiheuttavat liiallisia API-silmukoita).

**Kutsujen virheet:** Kuinka monta pyyntöä agentti epäonnistui käsittelemään? Tämä voi sisältää API-virheitä tai epäonnistuneita työkalukutsuja. Tehdäksesi agentistasi kestävämmän näitä virheitä vastaan tuotannossa, voit asettaa varajärjestelmiä tai uudelleenyrittämisiä. Esim. jos LLM-palveluntarjoaja A on poissa käytöstä, voit siirtyä LLM-palveluntarjoaja B:hen varapalveluna.

**Käyttäjäpalaute:** Suorat käyttäjäarviot antavat arvokkaita näkemyksiä. Tämä voi sisältää eksplisiittisiä arvioita (👍peukku ylös/👎alas, ⭐1–5 tähteä) tai tekstimuotoisia kommentteja. Toistuva negatiivinen palaute pitäisi herättää hälytys, sillä se on merkki siitä, että agentti ei toimi odotetulla tavalla.

**Epäsuora käyttäjäpalaute:** Käyttäjäkäyttäytyminen antaa epäsuoraa palautetta myös ilman eksplisiittisiä arvioita. Tämä voi sisältää välittömiä uudelleenmuotoiluita, toistuvia kyselyjä tai uudelleenyritys-painikkeen klikkauksia. Esim. jos huomaat, että käyttäjät kysyvät samaa kysymystä toistuvasti, se on merkki siitä, että agentti ei toimi odotetulla tavalla.

**Tarkkuus:** Kuinka usein agentti tuottaa oikeita tai toivottavia tuloksia? Tarkkuuden määrittelyt vaihtelevat (esim. ongelmanratkaisun oikeellisuus, tiedonhaustarkkuus, käyttäjätyytyväisyys). Ensimmäinen askel on määritellä, miltä onnistuminen näyttää agentillesi. Voit seurata tarkkuutta automaattisilla tarkistuksilla, arviointipisteillä tai tehtävän suorittamisen tageilla. Esimerkiksi merkitsemällä jäljet "onnistui" tai "epäonnistui".

**Automaattiset arviointimittarit:** Voit myös ottaa käyttöön automatisoituja arviointeja. Esimerkiksi voit käyttää LLM:ää pisteyttämään agentin tuottaman vastauksen — onko se hyödyllinen, tarkka tai ei. On olemassa myös useita avoimen lähdekoodin kirjastoja, jotka auttavat pisteyttämään eri osa-alueita. Esim. [RAGAS](https://docs.ragas.io/) RAG-agentteihin tai [LLM Guard](https://llm-guard.com/) haitallisen kielen tai prompt-injektion havaitsemiseen.

Käytännössä näiden mittareiden yhdistelmä antaa parhaan kuvan AI-agentin tilasta. Tässä luvussa [esimerkkimuistio](./code_samples/10-expense_claim-demo.ipynb) näytämme, miltä nämä mittarit näyttävät todellisissa esimerkeissä, mutta ensin opimme, miltä tyypillinen arviointityönkulku näyttää.

## Instrumentoi agenttisi

Kerätäkseen jäljitustietoja sinun täytyy instrumentoida koodisi. Tavoitteena on instrumentoida agenttikoodi siten, että se lähettää jälkiä ja mittareita, jotka voidaan siepata, käsitellä ja visualisoida havaittavuusalustan avulla.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) on noussut teollisuuden standardiksi LLM-havaittavuudessa. Se tarjoaa joukon API-rajapintoja, SDK:ita ja työkaluja telemetriatietojen luomiseen, keräämiseen ja vientiin.

On olemassa monia instrumentointikirjastoja, jotka kääriävät olemassa olevia agenttikehyksiä ja tekevät OpenTelemetry-spanien viemisestä havaittavuustyökaluun helppoa. Microsoft Agent Framework integroituu OpenTelemetryyn natiivisti. Alla on esimerkki MAF-agentin instrumentoinnista:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentin suoritusta seurataan automaattisesti
    pass
```

Tämän luvun [esimerkkimuistio](./code_samples/10-expense_claim-demo.ipynb) havainnollistaa, kuinka instrumentoida MAF-agenttisi.

**Manuaalinen spanien luominen:** Vaikka instrumentointikirjastot antavat hyvän perustan, on usein tilanteita, joissa tarvitaan yksityiskohtaisempaa tai räätälöityä tietoa. Voit luoda span:eja manuaalisesti lisätäksesi mukautettua sovelluslogiikkaa. Vielä tärkeämpää on, että voit rikastaa automaattisesti tai manuaalisesti luotuja span:eja mukautetuilla attribuuteilla (tunnetaan myös tageina tai metadatana). Nämä attribuutit voivat sisältää liiketoimintakohtaista dataa, välivaiheen laskelmia tai mitä tahansa kontekstia, joka voi olla hyödyllistä vianetsinnässä tai analyysissä, kuten `user_id`, `session_id` tai `model_version`.

Esimerkki jälkien ja spanien manuaalisesta luomisesta [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) -kirjastolla:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentin arviointi

Havaittavuus antaa meille mittareita, mutta arviointi on prosessi, jossa analysoidaan näitä tietoja (ja suoritetaan testejä) määrittääksesi, kuinka hyvin AI-agentti suoriutuu ja miten sitä voidaan parantaa. Toisin sanoen, kun sinulla on ne jäljet ja mittarit, miten käytät niitä arvioidaksesi agentin ja tehdessäsi päätöksiä?

Säännöllinen arviointi on tärkeää, koska AI-agentit ovat usein epädeterministisiä ja voivat kehittyä (päivitysten tai mallien driftauksen kautta) — ilman arviointia et tietäisi, tekeekö "älykäs agenttisi" todella työnsä hyvin vai onko sen suoritus heikentynyt.

Agenttien arvioinnit voidaan jakaa kahteen kategoriaan: **online-arviointi** ja **offline-arviointi**. Molemmat ovat arvokkaita ja täydentävät toisiaan. Usein aloitetaan offline-arvioinnilla, koska se on vähimmäisvaatimus ennen agentin käyttöönottoa.

### Offline-arviointi

![Datasetin kohteet Langfuse:ssa](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Tämä tarkoittaa agentin arviointia hallitussa ympäristössä, yleensä käyttämällä testidatatiedostoja, ei live-käyttäjäkyselyjä. Käytät kuratoituja datasettejä, joissa tiedät odotetun tuloksen tai oikean käytöksen, ja ajat agenttisi niiden läpi.

Esimerkiksi, jos olet rakentanut matemaattisten tekstitehtävien agentin, sinulla voi olla [testidatasetti](https://huggingface.co/datasets/gsm8k) 100 ongelmasta, joilla on tunnetut vastaukset. Offline-arviointi tehdään usein kehityksen aikana (ja se voi olla osa CI/CD-putkea) tarkistamaan parannuksia tai estämään regressioita. Hyöty on se, että se on **toistettavissa ja saat selkeät tarkkuusmittarit, koska sinulla on totuusdata**. Voit myös simuloida käyttäjäkyselyjä ja verrata agentin vastauksia ideaalivastauksiin tai käyttää automatisoituja mittareita, kuten yllä kuvattiin.

Offline-arvioinnin keskeinen haaste on varmistaa, että testidatasetti on kattava ja pysyy relevanttina — agentti saattaa toimia hyvin kiinteällä testijoukolla mutta kohdata hyvin erilaisia kyselyjä tuotannossa. Siksi testijoukkoja tulisi päivittää uusilla reunatapauksilla ja esimerkeillä, jotka heijastavat todellisia tilanteita. Pieniä "smoke test" -tapauksia ja suurempia arviointisettejä yhdistävä lähestymistapa on hyödyllinen: pienet sarjat nopeisiin tarkistuksiin ja suuremmat laajempien suorituskykymittareiden saamiseksi.

### Online-arviointi

![Havaittavuusmittareiden yleiskatsaus](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Tällä tarkoitetaan agentin arviointia live-ympäristössä, eli todellisessa käytössä tuotannossa. Online-arviointi sisältää agentin suorituskyvyn seuraamisen todellisissa käyttäjävuorovaikutuksissa ja tulosten jatkuvan analysoinnin.

Esimerkiksi voit seurata onnistumisprosentteja, käyttäjätyytyväisyyspisteitä tai muita mittareita live-liikenteessä. Online-arvioinnin etu on se, että se **kaappaa asioita, joita et välttämättä osaa ennakoida lab-ympäristössä** — voit havaita mallin driftauksen ajan kuluessa (jos agentin tehokkuus heikkenee syöttömalleissa tapahtuvien muutosten vuoksi) ja löytää odottamattomia kyselyitä tai tilanteita, jotka eivät olleet testidatassa. Se antaa todellisen kuvan siitä, miten agentti käyttäytyy kentällä.

Online-arviointi sisältää usein epäsuoran ja suoranaisen käyttäjäpalautteen keräämisen, kuten aiemmin käsiteltiin, ja mahdollisesti varjotestejä tai A/B-testejä (missä uusi agenttiversio ajetaan rinnakkain vanhan kanssa vertailua varten). Haasteena on, että luotettavien tunnisteiden tai pisteiden saaminen live-vuorovaikutuksille voi olla vaikeaa — saatat luottaa käyttäjäpalautteeseen tai vähäisempään jälkitulokseen (esim. klikkasiko käyttäjä tulosta).

### Näiden yhdistäminen

Online- ja offline-arvioinnit eivät ole toisensa poissulkevia; ne täydentävät toisiaan hyvin. Online-seurannasta saadut havainnot (esim. uudentyyppiset käyttäjäkyselyt, joissa agentti suoriutuu huonosti) voidaan käyttää offline-testidatasetin laajentamiseen ja parantamiseen. Toisaalta agentit, jotka toimivat hyvin offline-testeissä, voidaan ottaa luottavaisemmin käyttöön ja seurata online-ympäristössä.

Monet tiimit käyttävät itse asiassa silmukkaa:

_arvioi offline -> ota käyttöön -> seuraa online -> kerää uusia virhetilanteita -> lisää offline-datasettiin -> hienosäädä agenttia -> toista_.

## Yleisiä ongelmia

Kun otat AI-agentteja tuotantoon, saatat kohdata erilaisia haasteita. Tässä on joitakin yleisiä ongelmia ja niiden mahdollisia ratkaisuja:

| **Ongelma**    | **Mahdollinen ratkaisu**   |
| ------------- | ------------------ |
| AI Agent ei suorita tehtäviä johdonmukaisesti | - Hienosäädä agentille annettua kehotetta; ole selkeä tavoitteissa.<br>- Tunnista, missä tehtävien jakaminen alitehtäviin ja niiden käsittely useiden agenttien välillä voi auttaa. |
| AI Agent ajautuu jatkuviin silmukoihin  | - Varmista, että sinulla on selkeät lopetusehdot ja säännöt, jotta agentti tietää, milloin prosessi pitää lopettaa.<br>- Monimutkaisiin päättelyä ja suunnittelua vaativiin tehtäviin käytä suurempaa mallia, joka on erikoistunut päättelytehtäviin. |
| AI Agentin työkalukutsut eivät toimi hyvin   | - Testaa ja validoi työkalun output erikseen agenttijärjestelmän ulkopuolella.<br>- Hienosäädä määriteltyjä parametreja, kehotteita ja työkalujen nimeämistä.  |
| Moni-agenttijärjestelmä ei toimi johdonmukaisesti | - Hienosäädä kullekin agentille annettuja kehotteita varmistaaksesi, että ne ovat spesifisiä ja erottuvat toisistaan.<br>- Rakenna hierarkkinen järjestelmä käyttämällä "reititys"- tai ohjausagenttia, joka määrittää, mikä agentti on oikea. |

Monet näistä ongelmista voidaan tunnistaa tehokkaammin, kun havaittavuus on käytössä. Aiemmin käsitellyt jäljet ja mittarit auttavat paikantamaan tarkan kohdan agentin työnkulussa, jossa ongelmat ilmenevät, mikä tekee vianetsinnästä ja optimoinnista paljon tehokkaampaa.

## Kustannusten hallinta
Tässä on joitakin strategioita tekoälyagenttien tuotantoon käyttöönoton kustannusten hallintaan:

**Using Smaller Models:** Pienemmät kielimallit (SLMs) voivat toimia hyvin tietyissä agenttikäyttötapauksissa ja vähentää kustannuksia merkittävästi. Kuten aiemmin mainittiin, arviointijärjestelmän rakentaminen suorituskyvyn määrittämiseksi ja vertaamiseksi suurempiin malleihin on paras tapa ymmärtää, miten hyvin SLMs toimii sinun käyttötapauksessasi. Harkitse niiden käyttämistä yksinkertaisempiin tehtäviin kuten aikomuksen luokittelu tai parametrien poiminta, ja varaa suuremmat mallit monimutkaiseen päättelyyn.

**Using a Router Model:** Samankaltainen strategia on käyttää monipuolista valikoimaa malleja ja kokoja. Voit käyttää LLM/SLM-mallia tai serverless-funktiota reitittämään pyyntöjä niiden monimutkaisuuden perusteella parhaiten sopiville malleille. Tämä auttaa myös vähentämään kustannuksia samalla kun varmistat suorituskyvyn oikeissa tehtävissä. Esimerkiksi reititä yksinkertaiset kyselyt pienemmille, nopeammille malleille, ja käytä kalliita suuria malleja vain monimutkaisiin päättelytehtäviin.

**Caching Responses:** Yleisten pyyntöjen ja tehtävien tunnistaminen ja vastausten tarjoaminen ennen niiden kulkemista agenttijärjestelmäsi läpi on hyvä tapa vähentää samanlaisten pyyntöjen määrää. Voit jopa toteuttaa työnkulun tunnistaaksesi, kuinka samankaltainen pyyntö on välimuistiisi tallennettuihin pyyntöihin käyttäen yksinkertaisempia tekoälymalleja. Tämä strategia voi merkittävästi vähentää kustannuksia usein kysyttyjen kysymysten tai yleisten työnkulkujen kohdalla.

## Katsotaan miten tämä toimii käytännössä

In the [tämän osion esimerkkimuistikirjassa](./code_samples/10-expense_claim-demo.ipynb), we’ll see examples of how we can use observability tools to monitor and evaluate our agent.


### Onko sinulla lisää kysymyksiä tekoälyagenttien tuotantoon liittyen?

Liity [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) tapaamaan muita oppijoita, osallistumaan office hours -tilaisuuksiin ja saadaksesi vastauksia tekoälyagentteja koskeviin kysymyksiisi.

## Edellinen oppitunti

[Metakognition suunnittelumalli](../09-metacognition/README.md)

## Seuraava oppitunti

[Agenttiset protokollat](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme täsmällisyyteen, huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää määräävänä lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->