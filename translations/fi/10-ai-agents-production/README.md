# AI-agentit tuotannossa: havaittavuus ja arviointi

[![AI-agentit tuotannossa](../../../translated_images/fi/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kun AI-agentit siirtyvät kokeellisista prototyypeistä todellisiin käyttötapauksiin, kyky ymmärtää niiden käyttäytymistä, seurata niiden suorituskykyä ja systemaattisesti arvioida niiden tuottamia vastauksia muuttuu tärkeäksi.

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat/ymmärrät:
- Agenttien havaittavuuden ja arvioinnin ydinkäsitteet
- Tekniikat agenttien suorituskyvyn, kustannusten ja vaikuttavuuden parantamiseen
- Mitä ja miten arvioida AI-agenttejasi systemaattisesti
- Kuinka hallita kustannuksia, kun otat AI-agentit tuotantoon
- Kuinka instrumentoida agentteja, jotka on rakennettu Microsoft Agent Frameworkilla

Tavoitteena on antaa sinulle tieto muuttaa "mustat laatikot" olevat agentit läpinäkyviksi, hallittaviksi ja luotettaviksi järjestelmiksi.

_**Huom:** On tärkeää ottaa käyttöön turvallisia ja luotettavia AI-agentteja. Tutustu myös oppituntiin [Luotettavien AI-agenttien rakentaminen](./06-building-trustworthy-agents/README.md)._

## Jäljet ja spanit

Havaittavuustyökalut kuten [Langfuse](https://langfuse.com/) tai [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) esittävät yleensä agentin suoritukset jälkinä (traces) ja spaneina (spans).

- **Trace** edustaa täydellistä agentin tehtävää alusta loppuun (kuten käyttäjäkyselyn käsittelyä).
- **Spans** ovat yksittäisiä vaiheita jäljen sisällä (kuten kielimallin kutsu tai datan nouto).

![Trace-puu Langfusessa](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Ilman havaittavuutta AI-agentti voi tuntua "mustalta laatikolta" — sen sisäinen tila ja päättely ovat läpinäkymättömiä, mikä tekee vikojen diagnosoinnista ja suorituskyvyn optimoinnista vaikeaa. Havaittavuuden avulla agentit muuttuvat "lasilaatikoiksi", tarjoten läpinäkyvyyttä, joka on välttämätöntä luottamuksen rakentamiseksi ja varmistaakseen, että ne toimivat tarkoitetulla tavalla.

## Miksi havaittavuus on tärkeää tuotantoympäristöissä

AI-agenttien siirtäminen tuotantoympäristöihin tuo mukanaan uusia haasteita ja vaatimuksia. Havaittavuus ei ole enää pelkkä "hauska lisä", vaan kriittinen kyvykkyys:

*   **Debuggaus ja juurisyyn analyysi**: Kun agentti epäonnistuu tai tuottaa odottamattoman vastauksen, havaittavuustyökalut tarjoavat jäljet, joita tarvitset virheen lähteen paikantamiseen. Tämä on erityisen tärkeää monimutkaisissa agenteissa, jotka saattavat sisältää useita LLM-kutsuja, työkalujen käyttöä ja ehdollista logiikkaa.
*   **Latenssin ja kustannusten hallinta**: AI-agentit perustuvat usein LLM:iin ja muihin ulkoisiin rajapintoihin, joita laskutetaan tokenin tai kutsun perusteella. Havaittavuus mahdollistaa näiden kutsujen tarkan seurannan ja auttaa tunnistamaan operaatioita, jotka ovat liikaa hitaita tai kalliita. Tämä antaa tiimeille mahdollisuuden optimoida kehotteita, valita tehokkaampia malleja tai suunnitella työnkulkuja uudelleen operatiivisten kustannusten hallitsemiseksi ja hyvän käyttäjäkokemuksen varmistamiseksi.
*   **Luottamus, turvallisuus ja vaatimustenmukaisuus**: Monissa sovelluksissa on tärkeää varmistaa, että agentit käyttäytyvät turvallisesti ja eettisesti. Havaittavuus tarjoaa auditointijäljen agentin toimista ja päätöksistä. Tätä voidaan käyttää havaitsemaan ja lieventämään ongelmia, kuten prompt-injektio, haitallisen sisällön generoiminen tai henkilötietojen (PII) väärinkäsittely. Esimerkiksi voit tarkastella jälkiä ymmärtääksesi, miksi agentti antoi tietyn vastauksen tai käytti tiettyä työkalua.
*   **Jatkuvan parantamisen silmukat**: Havaittavuusdata muodostaa iteratiivisen kehitysprosessin perustan. Seuraamalla, miten agentit toimivat todellisessa maailmassa, tiimit voivat tunnistaa parannuskohteita, kerätä dataa mallien hienosäätöön ja validoida muutosten vaikutuksia. Tämä luo palautesilmukan, jossa tuotannon verkossa tehtävät havainnot ohjaavat offline-kokeiluja ja hienosäätöä, mikä johtaa asteittain parempaan agentin suorituskykyyn.

## Seurattavat keskeiset mittarit

Agentin käyttäytymisen seuraamiseksi ja ymmärtämiseksi on seurattava monenlaisia mittareita ja signaaleja. Vaikka tarkat mittarit voivat vaihdella agentin käyttötarkoituksen mukaan, jotkut ovat yleisesti tärkeitä.

Tässä on joitain yleisimmin havainnoitavia mittareita:

**Latenssi:** Kuinka nopeasti agentti vastaa? Pitkät odotusajat heikentävät käyttäjäkokemusta. Sinun tulisi mitata latenssia tehtävien ja yksittäisten vaiheiden osalta jäljittämällä agentin ajot. Esimerkiksi agentti, joka käyttää kaikkien mallikutsujen suorittamiseen 20 sekuntia, voidaan nopeuttaa käyttämällä nopeampaa mallia tai suorittamalla mallikutsut rinnakkain.

**Kustannukset:** Mikä on kustannus per agentin ajo? AI-agentit käyttävät LLM-kutsuja, joita laskutetaan tokenien tai kutsujen mukaan, tai ulkoisia rajapintoja. Usein toistuva työkalujen käyttö tai monet kehotukset voivat nostaa kustannuksia nopeasti. Esimerkiksi jos agentti kutsuu LLM:ää viisi kertaa pienen laadullisen parannuksen vuoksi, sinun on arvioitava, onko kustannus perusteltu vai voitko vähentää kutsujen määrää tai käyttää halvempi malli. Reaaliaikainen seuranta voi myös auttaa tunnistamaan odottamattomia piikkejä (esim. bugeja, jotka aiheuttavat liiallisia API-silmukoita).

**Pyyntövikoja:** Kuinka monta pyyntöä agentti epäonnistui? Tämä voi sisältää API-virheitä tai epäonnistuneita työkalukutsuja. Tehdäksesi agentistasi vakaamman tuotannossa, voit määrittää varajärjestelmiä tai uudelleenyrittämisiä. Esim. jos LLM-palveluntarjoaja A on poissa, voit vaihtaa varapalveluna LLM-palveluntarjoajaan B.

**Käyttäjäpalaute:** Suorat käyttäjäarvioinnit tarjoavat arvokkaita näkemyksiä. Tämä voi sisältää eksplisiittisiä arvioita (👍peukku ylös/👎peukku alas, ⭐1-5 tähteä) tai tekstimuotoisia kommentteja. Toistuva negatiivinen palaute tulisi laukaista hälytys, koska se on merkki siitä, että agentti ei toimi odotetusti.

**Implisiittinen käyttäjäpalaute:** Käyttäjäkäyttäytyminen tarjoaa epäsuoraa palautetta myös ilman eksplisiittisiä arvioita. Tämä voi sisältää välittömän kysymyksen uudelleenmuotoilun, toistuvat kyselyt tai uudelleenyritys-painikkeen klikkaukset. Esim. jos huomaat, että käyttäjät kysyvät toistuvasti samaa kysymystä, se on merkki siitä, että agentti ei toimi odotetusti.

**Tarkkuus:** Kuinka usein agentti tuottaa oikeita tai toivottavia vastauksia? Tarkkuuden määritelmät vaihtelevat (esim. ongelmanratkaisun oikeellisuus, tiedonhakun tarkkuus, käyttäjätyytyväisyys). Ensimmäinen askel on määritellä, miltä onnistuminen näyttää agentillesi. Voit seurata tarkkuutta automatisoitujen tarkistusten, arviointipisteytyksen tai tehtävän suorittamisen tunnisteiden avulla. Esimerkiksi merkitsemällä jäljet arvolla "succeeded" tai "failed".

**Automaattiset arviointimittarit:** Voit myös ottaa käyttöön automaattisia arviointeja. Esimerkiksi voit käyttää LLM:ää pisteyttämään agentin lähtöä sen perusteella, onko se hyödyllinen, tarkka tai ei. On myös useita avoimen lähdekoodin kirjastoja, jotka auttavat pisteyttämään eri osa-alueita agentissa. Esim. [RAGAS](https://docs.ragas.io/) RAG-agentteihin tai [LLM Guard](https://llm-guard.com/) haitallisen kielen tai prompt-injektion havaitsemiseen.

Käytännössä näiden mittareiden yhdistelmä antaa parhaan kattavuuden AI-agentin terveydestä. Tässä luvussa olevan [esimerkkimuistikirjan](./code_samples/10-expense_claim-demo.ipynb) avulla näytämme, miltä nämä mittarit näyttävät todellisissa esimerkeissä, mutta ensin opimme, miltä tyypillinen arviointityönkulku näyttää.

## Instrumentoi agenttisi

Seuranta- ja jälkitietojen keräämiseksi sinun täytyy instrumentoida koodi. Tavoitteena on instrumentoida agenttikoodi siten, että se lähettää jälkiä ja mittareita, jotka voidaan kaapata, käsitellä ja visualisoida havaittavuusalustalla.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) on noussut teollisuuden standardiksi LLM-havaittavuudelle. Se tarjoaa joukon API-rajapintoja, SDK:ita ja työkaluja telemetriadatan generoimiseksi, keräämiseksi ja vientiä varten.

On olemassa monia instrumentointikirjastoja, jotka kääriytyvät olemassa olevien agenttikehysten ympärille ja tekevät OpenTelemetry-spanien viemisestä havaittavuustyökalulle helppoa. Microsoft Agent Framework integroituu OpenTelemetryyn natively. Alla on esimerkki MAF-agentin instrumentoinnista:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentin suoritusta jäljitetään automaattisesti
    pass
```

Tämän luvun [esimerkkimuistikirja](./code_samples/10-expense_claim-demo.ipynb) näyttää, kuinka instrumentoida MAF-agenttisi.

**Manuaalinen spanien luominen:** Vaikka instrumentointikirjastot tarjoavat hyvän peruslähtökohdan, usein tarvitaan yksityiskohtaisempaa tai räätälöityä tietoa. Voit luoda spaneja manuaalisesti lisätäksesi räätälöityä sovelluslogiikkaa. Vielä tärkeämpää on, että ne voivat rikastaa automaattisesti tai manuaalisesti luotuja spaneja mukautetuilla attribuuteilla (tunnetaan myös tageina tai metadatana). Nämä attribuutit voivat sisältää liiketoimintakohtaisia tietoja, välivaiheen laskelmia tai kontekstia, joka voi olla hyödyllistä debuggaamisessa tai analyysissä, kuten `user_id`, `session_id` tai `model_version`.

Esimerkki jälkien ja spanien luomisesta manuaalisesti [Langfuse Python SDK:lla](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentin arviointi

Havaittavuus antaa meille mittareita, mutta arviointi on prosessi, jossa analysoidaan kyseisiä tietoja (ja suoritetaan testejä) selvittääkseen, kuinka hyvin AI-agentti suoriutuu ja miten sitä voidaan parantaa. Toisin sanoen, kun sinulla on nuo jäljet ja mittarit, miten niitä käytetään agentin arviointiin ja päätöksentekoon?

Säännöllinen arviointi on tärkeää, koska AI-agentit ovat usein epädeterministisiä ja voivat kehittyä (päivitysten tai mallin käyttäytymisen siirron myötä) – ilman arviointia et tietäisi, tekeekö "älykäs agenttisi" todella työnsä hyvin vai onko se heikentynyt.

Agenttien arvioinneissa on kaksi kategoriaa: **online-arviointi** ja **offline-arviointi**. Molemmat ovat arvokkaita ja täydentävät toisiaan. Yleensä aloitamme offline-arvioinnilla, koska se on vähimmäisvaatimus ennen minkään agentin käyttöönottoa.

### Offline-arviointi

![Datan kohteet Langfusessa](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Tähän kuuluu agentin arviointi kontrolloidussa ympäristössä, tyypillisesti käyttämällä testidatasettejä, ei live-käyttäjäkyselyjä. Käytät kuratoituja datasettejä, joissa tiedät odotetun tuloksen tai oikean käyttäytymisen, ja ajat agenttisi niiden läpi.

Esimerkiksi, jos olet rakentanut matemaattisten sanatehtävien agentin, sinulla voi olla [testidatasetti](https://huggingface.co/datasets/gsm8k) 100 ongelmasta tunnetuilla vastauksilla. Offline-arviointi tehdään usein kehityksen aikana (ja voi olla osa CI/CD-putkia) tarkistamaan parannukset tai suojautumaan regressioilta. Hyöty on se, että se on **toistettavissa ja saat selkeät tarkkuusmittarit, koska sinulla on ground truth**. Voit myös simuloida käyttäjäkyselyitä ja mitata agentin vastauksia ihanteellisia vastauksia vastaan tai käyttää automatisoituja mittareita kuten edellä kuvattiin.

Offline-arvioinnin keskeinen haaste on varmistaa, että testidatasetti on kattava ja pysyy relevanttina – agentti saattaa pärjätä hyvin kiinteällä testisajalla, mutta kohdata hyvin erilaisia kyselyjä tuotannossa. Siksi testijoukkoja tulisi pitää ajan tasalla uusilla reunatapauksilla ja esimerkeillä, jotka heijastavat todellisia skenaarioita​. Pieniä "savutestitapauksia" ja laajempia arviointijoukkoja yhdistävä sekoitus on hyödyllinen: pienet joukot nopeisiin tarkistuksiin ja suuremmat laajempaan suorituskyvyn mittaamiseen​.

### Online-arviointi

![Havaittavuusmittarien yleiskuva](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Tällä tarkoitetaan agentin arviointia live-ympäristössä, eli todellisen käytön aikana tuotannossa. Online-arviointi sisältää agentin suorituskyvyn seurantaa oikeissa käyttäjävuorovaikutuksissa ja jatkuvaa tulosten analysointia.

Esimerkiksi voit seurata onnistumisprosentteja, käyttäjätyytyväisyysarvioita tai muita mittareita live-liikenteessä. Online-arvioinnin etu on, että se **tallentaa asioita, joita et välttämättä ennusta laboratorio-olosuhteissa** – voit havaita mallin siirtymää ajan myötä (jos agentin tehokkuus heikkenee syöttökuvioiden muuttuessa) ja saada kiinni odottamattomista kyselyistä tai tilanteista, joita ei ollut testidatassa​. Se antaa todellisen kuvan siitä, miten agentti käyttäytyy luonnossa.

Online-arviointi sisältää usein implisiittisen ja eksplisiittisen käyttäjäpalautteen keräämisen, kuten aiemmin käsiteltiin, ja mahdollisesti rinnakkaistestauksen tai A/B-testauksen (missä uusi agenttiversio ajetaan rinnakkain vanhan kanssa vertailua varten). Haasteena on, että luotettavien tunnisteiden tai pisteiden saaminen live-vuorovaikutuksista voi olla hankalaa – saatat joutua luottamaan käyttäjäpalautteeseen tai jälkiseurannan mittareihin (kuten klikkasiko käyttäjä tulosta).

### Yhdistäminen

Online- ja offline-arvioinnit eivät sulje toisiaan pois; ne täydentävät toisiaan hyvin. Verkossa saadut havainnot (esim. uudet käyttäjäkyselytyypit, joissa agentti suoriutuu huonosti) voidaan käyttää offline-testidatasetin laajentamiseen ja parantamiseen. Toisaalta agentit, jotka pärjäävät hyvin offline-testeissä, voidaan turvallisemmin ottaa tuotantoon ja seurata online-ympäristössä.

Monet tiimit noudattavat käytännössä silmukkaa:

_arvioi offline -> ota käyttöön -> seuraa online -> kerää uusia virhetilanteita -> lisää offline-datasettiin -> hio agenttia -> toista_.

## Yleisiä ongelmia

Kun otat AI-agentteja tuotantoon, saatat kohdata erilaisia haasteita. Tässä on joitain yleisiä ongelmia ja niiden mahdollisia ratkaisuja:

| **Issue**    | **Potential Solution**   |
| ------------- | ------------------ |
| AI Agent not performing tasks consistently | - Tiivistä agentille annettua kehotetta; ole selkeä tavoitteiden suhteen.<br>- Tunnista, missä tehtävän jakaminen osatehtäviin ja niiden käsittely useammalla agentilla voi auttaa. |
| AI Agent running into continuous loops  | - Varmista, että sinulla on selkeät lopetusehdot, jotta agentti tietää, milloin lopettaa prosessin.<br>- Komplekseihin tehtäviin, jotka vaativat päättelyä ja suunnittelua, käytä suurempaa mallia, joka on erikoistunut päättelytehtäviin. |
| AI Agent tool calls are not performing well   | - Testaa ja validoi työkalun tuotosta agenttijärjestelmän ulkopuolella.<br>- Hio määriteltyjä parametreja, kehotteita ja työkalujen nimeämistä.  |
| Multi-Agent system not performing consistently | - Hio kunkin agentin saamia kehotteita varmistaaksesi, että ne ovat spesifisiä ja erottuvat toisistaan.<br>- Rakenna hierarkkinen järjestelmä käyttämällä "reititys" tai ohjausagenttia päättämään, mikä agentti on oikea. |

Monet näistä ongelmista voidaan tunnistaa tehokkaammin, kun havaittavuus on käytössä. Aiemmin käsittelemämme jäljet ja mittarit auttavat paikallistamaan täsmälleen, missä kohtaa agentin työnkulkua ongelmat esiintyvät, mikä tekee debuggaamisesta ja optimoinnista paljon tehokkaampaa.

## Kustannusten hallinta
Tässä on joitakin strategioita AI-agenttien tuotantoon käyttöönoton kustannusten hallintaan:

**Pienten mallien käyttäminen:** Pienet kielimallit (SLMs) voivat suoriutua hyvin tietyissä agenttisissa käyttötapauksissa ja vähentävät kustannuksia merkittävästi. Kuten aiemmin mainittiin, arviointijärjestelmän rakentaminen suorituskyvyn määrittämiseksi ja vertaamiseksi suurempiin malleihin on paras tapa ymmärtää, kuinka hyvin SLM toimii omassa käyttötapauksessasi. Harkitse SLMien käyttöä yksinkertaisempiin tehtäviin, kuten intentin luokitteluun tai parametrien poimintaan, ja pidä suuremmat mallit varattuina monimutkaiseen päättelyyn.

**Reititysmallin käyttäminen:** Samankaltainen strategia on käyttää erilaisia malleja ja eri kokoja. Voit käyttää LLM/SLM:ää tai serverittömän toiminnon avulla reitittääksesi pyynnöt monimutkaisuuden mukaan parhaiten sopiville malleille. Tämä auttaa myös vähentämään kustannuksia ja varmistamaan suorituskyvyn oikeissa tehtävissä. Esimerkiksi reititä yksinkertaiset kyselyt pienemmille, nopeammille malleille, ja käytä kalliita suuria malleja vain monimutkaisiin päättelytehtäviin.

**Vastausten välimuistiin tallentaminen:** Yleisten pyyntöjen ja tehtävien tunnistaminen ja vastausten tarjoaminen ennen niiden ohjautumista agenttijärjestelmäsi läpi on hyvä tapa vähentää samanlaisten pyyntöjen määrää. Voit jopa toteuttaa työnkulun, joka tunnistaa, kuinka samanlainen pyyntö on välimuistissa oleviin pyyntöihisi käyttämällä yksinkertaisempia tekoälymalleja. Tämä strategia voi merkittävästi pienentää kustannuksia usein esitettyjen kysymysten tai yleisten työnkulkujen kohdalla.

## Katsotaan, miten tämä toimii käytännössä

Tämän osion [esimerkkimuistikirjassa](./code_samples/10-expense_claim-demo.ipynb) näemme esimerkkejä siitä, miten voimme käyttää observoitavuustyökaluja agenttimme seuraamiseen ja arviointiin.

### Onko sinulla lisää kysymyksiä tekoälyagenttien tuotantokäytöstä?

Liity [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) tapaaksesi muita oppijoita, osallistuaksesi työaikoihin ja saadaksesi vastauksia tekoälyagenttikysymyksiisi.

## Edellinen oppitunti

[Metakognition suunnittelumalli](../09-metacognition/README.md)

## Seuraava oppitunti

[Agenttiset protokollat](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista käännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virheellisistä tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->