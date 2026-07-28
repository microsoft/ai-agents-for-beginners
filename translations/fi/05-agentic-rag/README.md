[![Agentic RAG](../../../translated_images/fi/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Napsauta yllä olevaa kuvaa katsellaksesi tämän oppitunnin videota)_

# Agentic RAG

Tämä oppitunti tarjoaa kattavan yleiskatsauksen Agentic Retrieval-Augmented Generationista (Agentic RAG), nousevasta tekoälyn paradigmosta, jossa suuret kielimallit (LLM:t) suunnittelevat itsenäisesti seuraavia askeliaan samalla hakeakseen tietoa ulkoisista lähteistä. Toisin kuin staattiset haku-ja-luku -kuviot, Agentic RAG sisältää iteratiivisia kutsuja LLM:lle, joiden välillä tehdään työkalu- tai funktiokutsuja ja tuotetaan jäsenneltyjä tuloksia. Järjestelmä arvioi tulokset, tarkentaa kyselyjä, kutsuu tarvittaessa lisätyökaluja ja jatkaa tätä sykliä, kunnes saavutetaan tyydyttävä ratkaisu.

## Johdanto

Tämä oppitunti käsittelee

- **Agentic RAG:n ymmärtäminen:** Opi tuntemaan tekoälyn uusi paradigman muoto, jossa suuret kielimallit suunnittelevat itsenäisesti seuraavat askeleensa samalla kun ne hakevat tietoa ulkoisista tietolähteistä.
- **Iteratiivisen Maker-Checker-tyylin omaksuminen:** Ymmärrä LLM:lle tehtävien iteratiivisten kutsujen silmukka, jonka lomassa tehdään työkalu- tai funktiokutsuja ja tuotetaan jäsenneltyjä vastauksia, jotka on suunniteltu parantamaan oikeellisuutta ja käsittelemään virheellisiä kyselyjä.
- **Käytännön sovellusten tutkiminen:** Tunnista tilanteet, joissa Agentic RAG on erityisen hyödyllinen, kuten oikeellisuuteen painottuvissa ympäristöissä, monimutkaisissa tietokantaintegraatioissa ja laajennetussa työnkulussa.

## Oppimistavoitteet

Oppitunnin jälkeen osaat/ymmärrät:

- **Agentic RAG:n ymmärtäminen:** Opi tekoälyn uudesta paradigman muodosta, jossa suuret kielimallit suunnittelevat itsenäisesti seuraavat askeleensa samalla kun ne hakevat tietoa ulkoisista tietolähteistä.
- **Iteratiivinen Maker-Checker-tyyli:** Ymmärrä konsepti, jossa LLM:lle tehdään iteratiivisia kutsuja työkalu- tai funktiokutsuilla ja jäsennellyillä tuloksilla parantaen oikeellisuutta ja käsitellen virheellisiä kyselyjä.
- **Päästä käsiksi päättelyprosessiin:** Ymmärrä järjestelmän kyky hallita päättelynsä prosessia itse, tehdä päätöksiä ongelmanratkaisun lähestymistavasta ilman ennalta määriteltyjä polkuja.
- **Työnkulku:** Ymmärrä, kuinka agenttipohjainen malli itsenäisesti päättää hakea markkinatrendifilmitteitä, tunnistaa kilpailijatietoja, korreloi sisäisiä myyntimittareita, yhdistää tulokset ja arvioi strategian.
- **Iteratiiviset silmukat, työkalujen integrointi ja muisti:** Opi järjestelmän riippuvuudesta silmukkamaisesta vuorovaikutuksesta, jossa ylläpidetään tilaa ja muistia vaiheiden välillä, välttäen toistuvia silmukoita ja tehden tietoisia päätöksiä.
- **Virhetilojen käsittely ja itsekorjaus:** Tutki järjestelmän vankkoja itsekorjausmekanismeja, mukaan lukien iterointi ja uudelleenkysely, diagnostisten työkalujen käyttö ja ihmisen valvontaan turvautuminen.
- **Agenttin rajat:** Ymmärrä Agentic RAG:n rajoitukset, jotka liittyvät toimialakohtaiseen autonomiaan, infrastruktuuririippuvuuteen ja turvarajojen kunnioittamiseen.
- **Käytännön käyttötapaukset ja arvo:** Tunnista tilanteet, joissa Agentic RAG on erityisen hyödyllinen, kuten oikeellisuuteen painottuvissa ympäristöissä, monimutkaisissa tietokantaintegraatioissa ja laajennetussa työnkulussa.
- **Hallinnointi, läpinäkyvyys ja luottamus:** Opi hallinnoinnin ja läpinäkyvyyden tärkeydestä, mukaan lukien selitettävissä oleva päättely, vinouman kontrolli ja ihmisen valvonta.

## Mikä on Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) on nouseva tekoälyn paradigma, jossa suuret kielimallit (LLM:t) suunnittelevat itsenäisesti seuraavia askeleitaan samalla kun hakevat tietoa ulkoisista lähteistä. Toisin kuin staattiset haku-ja-luku -mallit, Agentic RAG sisältää iteratiivisia kutsuja LLM:lle, joiden väleissä tehdään työkalu- tai funktiokutsuja ja jäsenneltyjä tuloksia tuotetaan. Järjestelmä arvioi tuloksia, tarkentaa kyselyjä, käyttää tarvittaessa lisätyökaluja ja jatkaa tätä sykliä, kunnes saavutetaan tyydyttävä ratkaisu. Tämä iteratiivinen “maker-checker” -tyyli parantaa oikeellisuutta, käsittelee virheellisiä kyselyjä ja varmistaa laadukkaat tulokset.

Järjestelmä hallitsee aktiivisesti päättelyprosessinsa, muokkaa epäonnistuneita kyselyjä, valitsee erilaisia hakumenetelmiä ja integroi useita työkaluja — kuten vektorihakua Azure AI Searchissa, SQL-tietokantoja tai räätälöityjä rajapintoja — ennen vastauksensa lopullista tuottamista. Agenttisen järjestelmän erottuva ominaisuus on sen kyky hallita oma päättelyprosessinsa. Perinteiset RAG-toteutukset luottavat ennalta määriteltyihin polkuihin, mutta agenttinen järjestelmä määrittää itsenäisesti vaiheiden järjestyksen sen löytämän tiedon laadun perusteella.

## Agentic Retrieval-Augmented Generationin (Agentic RAG) määritelmä

Agentic Retrieval-Augmented Generation (Agentic RAG) on nouseva paradigmamuoto tekoälyn kehityksessä, jossa LLM:t eivät ainoastaan hae tietoa ulkoisista lähteistä, vaan myös suunnittelevat itsenäisesti seuraavia askeleitaan. Toisin kuin staattiset haku-ja-luku -mallit tai huolellisesti kirjoitetut kehotteiden sarjat, Agentic RAG sisältää iteratiivisten kutsujen silmukan LLM:lle, joiden väleissä tehdään työkalu- tai funktiokutsuja ja tuotetaan jäsenneltyjä vastauksia. Järjestelmä arvioi jokaisella kerralla saamansa tulokset, päättää, täytyykö kyselyjä tarkentaa, kutsuu tarvittaessa lisää työkaluja ja jatkaa tätä sykliä, kunnes se saavuttaa tyydyttävän ratkaisun.

Tämä iteratiivinen “maker-checker” -tyyli on suunniteltu parantamaan oikeellisuutta, käsittelemään virheellisiä kyselyjä jäsenneltyihin tietokantoihin (esim. NL2SQL) ja varmistamaan tasapainoiset, laadukkaat tulokset. Sen sijaan, että luotettaisiin pelkästään huolellisesti suunniteltuihin kehotteisiin, järjestelmä hallitsee aktiivisesti omaa päättelyprosessiaan. Se voi kirjoittaa uudelleen epäonnistuneita kyselyjä, valita erilaisia hakumenetelmiä ja yhdistää useita työkaluja — kuten vektorihakua Azure AI Searchissa, SQL-tietokantoja tai räätälöityjä rajapintoja — ennen lopullisen vastauksen tuottamista. Tämä poistaa tarpeen monimutkaisille orkestrointikehyksille. Stattinen “LLM-kutsu → työkalun käyttö → LLM-kutsu → …” -silmukka voi tuottaa kehittyneitä ja hyvin perusteltuja vastauksia.

![Agentic RAG Core Loop](../../../translated_images/fi/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Päättelyprosessin hallinta

Ominaisuus, joka tekee järjestelmästä “agenttisen”, on sen kyky hallita oma päättelyprosessinsa. Perinteiset RAG-toteutukset riippuvat usein ihmisestä, joka ennalta määrittelee mallille polun: ajatusketjun, joka määrittää mitä haetaan ja milloin.
Mutta kun järjestelmä on todella agenttinen, se päättää sisäisesti kuinka lähestyä ongelmaa. Se ei vain suorita skriptiä; se määrittää itsenäisesti vaiheiden järjestyksen löydetyn tiedon laadun perusteella.
Esimerkiksi, jos sitä pyydetään laatimaan tuotteen lanseerausstrategia, se ei perustu pelkästään kehotteeseen, joka kuvaa koko tutkimus- ja päätöksentekoprosessin. Sen sijaan agenttipohjainen malli päättää itsenäisesti:

1. Hakea ajantasaiset markkinatrendiraportit Bing Web Groundingin avulla
2. Tunnistaa asiaankuuluvat kilpailijatiedot Azure AI Searchin avulla
3. Korreloida historiallisia sisäisiä myyntimittareita Azure SQL Databasea käyttäen
4. Yhdistää löydökset yhtenäiseksi strategiaksi, jota orkestroi Azure OpenAI Service
5. Arvioida strategia puutteiden tai ristiriitojen varalta ja tarvittaessa tehdä toinen haku
Kaikki nämä vaiheet – kyselyjen tarkentaminen, lähteiden valinta, toisto kunnes vastaus on “tyydyttävä” – päätetään mallin toimesta, ei ihmisen kirjoittamana skriptinä.

## Iteratiiviset silmukat, työkalujen integrointi ja muisti

![Tool Integration Architecture](../../../translated_images/fi/tool-integration.0f569710b5c17c10.webp)

Agenttinen järjestelmä perustuu silmukkamaisiin vuorovaikutusmalleihin:

- **Alkukutsu:** Käyttäjän tavoite (eli käyttäjän kehotus) esitetään LLM:lle.
- **Työkalujen kutsuminen:** Jos malli havaitsee puuttuvaa tietoa tai epäselviä ohjeita, se valitsee työkalun tai hakutavan – kuten vektoritietokantakyselyn (esim. Azure AI Search Hybrid hakeminen yksityisistä tiedoista) tai jäsennellyn SQL-kutsun – saadakseen lisäkontekstia.
- **Arviointi ja tarkennus:** Palautetun datan jälkeen malli päättää, riittääkö tieto. Jos ei, se tarkentaa kyselyä, kokeilee eri työkalua tai säätää lähestymistapaa.
- **Toista kunnes tyydyttävä:** Tämä sykli jatkuu, kunnes malli katsoo saaneensa tarpeeksi selkeyttä ja näyttöä antaa lopullisen, hyvin perustellun vastauksen.
- **Muisti ja tila:** Koska järjestelmä ylläpitää tilaa ja muistia vaiheiden välillä, se voi muistaa aiemmat yritykset ja niiden tulokset, välttäen toistuvia silmukoita ja tehden paremmin tietoisia päätöksiä prosessin kuluessa.

Ajan myötä tämä luo kehittyvän ymmärryksen tunteen, joka mahdollistaa mallin navigoinnin monivaiheisissa, monimutkaisissa tehtävissä ilman, että ihmisen tarvitsee jatkuvasti puuttua tilanteeseen tai muokata kehotetta.

## Virhetilojen käsittely ja itsekorjaus

Agentic RAG:n autonomia sisältää myös vahvat itsekorjausmekanismit. Kun järjestelmä kohtaa umpikujaa – kuten palauttaa epäolennaisia dokumentteja tai kohtaa virheellisiä kyselyjä – se voi:

- **Iteroida ja kysyä uudelleen:** Sen sijaan, että palauttaisi arvottomia vastauksia, malli kokeilee uusia hakustrategioita, kirjoittaa tietokantakyselyt uudelleen tai tarkastelee vaihtoehtoisia aineistoja.
- **Käyttää diagnostiikkatyökaluja:** Järjestelmä voi kutsua lisätoimintoja, jotka auttavat päättelyvaiheiden virheiden korjaamisessa tai haetun datan oikeellisuuden varmistamisessa. Työkalut kuten Azure AI Tracing ovat tärkeitä robustille havaittavuudelle ja valvonnalle.
- **Turvautua ihmisen valvontaan:** Korkean riskin tai toistuvasti epäonnistuvissa tilanteissa malli voi merkata epävarmuuden ja pyytää ihmisen ohjausta. Kun ihminen antaa korjaavaa palautetta, malli voi ottaa sen oppina tulevaisuudessa.

Tämä iteratiivinen ja dynaaminen lähestymistapa mahdollistaa mallin jatkuvan parantamisen, varmistaen, ettei kyse ole vain kertakäyttöjärjestelmästä, vaan järjestelmästä, joka oppii virheistään kuluvan istunnon aikana.

![Self Correction Mechanism](../../../translated_images/fi/self-correction.da87f3783b7f174b.webp)

## Agentin rajat

Huolimatta tehtävän sisäisestä autonomiasta, Agentic RAG ei ole samanlainen kuin yleinen tekoäly (Artificial General Intelligence). Sen “agenttiset” kyvyt rajoittuvat työkaluisiin, tietolähteisiin ja kehittäjien asettamiin politiikkoihin. Se ei voi keksiä omia työkalujaan tai ylittää sille asetettuja toimialarajoja. Sen sijaan se loistaa dynaamisessa käytettävissä olevien resurssien orkestroinnissa.
Keskeiset erot edistyneempiin tekoälymuotoihin ovat:

1. **Toimialakohtainen autonomia:** Agentic RAG -järjestelmät keskittyvät käyttäjän määrittämien tavoitteiden saavuttamiseen tunnetussa toimialassa, käyttämällä strategioita kuten kyselyjen uudelleenkirjoitus tai työkalun valinta tulosten parantamiseksi.
2. **Infrastruktuuririippuvuus:** Järjestelmän kyvyt riippuvat kehittäjien integroimista työkaluista ja tiedoista. Se ei voi ylittää näitä rajoja ilman ihmisen puuttumista.
3. **Turvarajojen kunnioittaminen:** Eettiset ohjeistukset, sääntelyvaatimukset ja liiketoimintapolitiikat ovat erittäin tärkeitä. Agentin vapaus on aina rajattu turvallisuus- ja valvontamekanismeilla (toivottavasti?).

## Käytännön käyttötapaukset ja arvo

Agentic RAG loistaa tilanteissa, jotka vaativat iteratiivista täsmennystä ja tarkkuutta:

1. **Oikeellisuuteen perustuvat ympäristöt:** Säännösten tarkastuksissa, sääntelyanalyyseissa tai oikeustutkimuksessa agenttipohjainen malli voi toistuvasti varmistaa faktoja, konsultoida useita lähteitä ja kirjoittaa kyselyjä uudelleen, kunnes se tuottaa perusteellisesti tarkistetun vastauksen.
2. **Monimutkaiset tietokantaintegraatiot:** Kun käsitellään jäsenneltyä dataa, jossa kyselyt usein epäonnistuvat tai vaativat säätöä, järjestelmä voi itsenäisesti tarkentaa kyselyjään käyttämällä Azure SQL:ää tai Microsoft Fabric OneLakea varmistaen, että lopullinen haku vastaa käyttäjän tarkoitusta.
3. **Laajennetut työnkulut:** Pidemmät istunnot voivat kehittyä uuden tiedon ilmaantuessa. Agentic RAG voi jatkuvasti sisällyttää uutta dataa ja muuttaa strategioitaan oppiessaan lisää ongelmatilasta.

## Hallinnointi, läpinäkyvyys ja luottamus

Kun nämä järjestelmät tulevat entistä autonomisemmiksi päättelyssään, hallinnointi ja läpinäkyvyys ovat ratkaisevan tärkeitä:

- **Selitettävä päättely:** Malli voi tarjota auditointijäljen tekemistään kyselyistä, käyttämistään lähteistä ja päättelyvaiheista, jotka johtivat sen johtopäätökseen. Työkalut kuten Azure AI Content Safety ja Azure AI Tracing / GenAIOps voivat auttaa ylläpitämään läpinäkyvyyttä ja vähentämään riskejä.
- **Vinouman hallinta ja tasapainoinen haku:** Kehittäjät voivat säätää hakustrategioita varmistaakseen, että tasapainoisia ja edustavia tietolähteitä otetaan huomioon, ja auditointia voidaan tehdä säännöllisesti vinoumien tai vääristymien havaitsemiseksi käyttäen edistyksellisiä malleja Azure Machine Learning -ympäristössä.
- **Ihmisen valvonta ja noudattaminen:** Herkissä tehtävissä ihmisen tarkastus on edelleen välttämätöntä. Agentic RAG ei korvaa ihmisen harkintaa korkean riskin päätöksissä — se täydentää sitä tarjoamalla huolellisesti tarkistettuja vaihtoehtoja.

On tärkeää, että käytettävissä on työkaluja, jotka tarjoavat selkeän toimintojen jäljen. Ilman niitä monivaiheisen prosessin virheiden selvittäminen voi olla hyvin vaikeaa. Seuraava esimerkki Literal AI:lta (yritys Chainlitin takana) näyttää agentin suorituksen:

![AgentRunExample](../../../translated_images/fi/AgentRunExample.471a94bc40cbdc0c.webp)

## Yhteenveto

Agentic RAG edustaa luonnollista kehitystä siinä, miten tekoälyjärjestelmät käsittelevät monimutkaisia, dataintensiivisiä tehtäviä. Ottamalla käyttöön silmukkamaisen vuorovaikutusmallin, valitsemalla työkalut itsenäisesti ja tarkentamalla kyselyjä laadukkaan lopputuloksen saavuttamiseksi, järjestelmä siirtyy staattisesta kehotteiden seuraamisesta adaptiivisemmaksi ja kontekstia ymmärtäväksi päätöksentekijäksi. Vaikka se on yhä rajattu ihmisen määrittämiin infrastruktuureihin ja eettisiin ohjeisiin, nämä agenttiset kyvyt mahdollistavat rikkaammat, dynaamisemmat ja lopulta hyödyllisempiä tekoälyvuorovaikutuksia sekä yrityksille että loppukäyttäjille.

### Onko sinulla lisää kysymyksiä Agentic RAG:sta?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tapaamaan muita oppijoita, osallistumaan aukioloaikoihin ja saamassa vastauksia tekoälyagenttikysymyksiisi.

## Lisäresurssit

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Ota käyttöön Retrieval Augmented Generation (RAG) Azure OpenAI Service -palvelulla: Opi käyttämään omia tietojasi Azure OpenAI Service -palvelun kanssa. Tämä Microsoft Learn -moduuli tarjoaa kattavan oppaan RAG:n toteuttamiseen</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatiivisten tekoälysovellusten arviointi Microsoft Foundryn avulla: Tämä artikkeli käsittelee mallien arviointia ja vertailua julkisilla tietoaineistoilla, mukaan lukien Agentic AI -sovellukset ja RAG-arkkitehtuurit</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Mikä on Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Kattava opas agenttipohjaiseen Retrieval Augmented Generationiin – News from generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agenttinen RAG: tehosta RAGiasi kyselyjen uudelleenmuotoilulla ja itse-kyselyllä! Hugging Face avoimen lähdekoodin AI-keittokirja</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Agenttikerrosten lisääminen RAG:iin</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Tietoavustajien tulevaisuus: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Kuinka rakentaa agenttisia RAG-järjestelmiä</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Microsoft Foundry Agent Service -palvelun käyttö tekoälyagenttien skaalaamiseen</a>

### Akateemiset julkaisut

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iteratiivinen parantelu itsepalautteen avulla</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Kielelliset agentit verbaalisella vahvistusoppimisella</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Suuret kielimallit voivat itsekorjata työkaluinteraktiivisen kritiikin avulla</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agenttinen Retrieval-Augmented Generation: Katsaus agenttiseen RAGiin</a>

## Agentin suorituskyvyn tarkistus (valinnainen)

Kun olet oppinut ottamaan agentit käyttöön [Luku 16:ssa](../16-deploying-scalable-agents/README.md), voit tarkistaa tämän oppitunnin `TravelRAGAgent`-agentin toimintakyvyn – varmistaen, että sen vastaukset perustuvat tietokantaan – käyttämällä tiedostoa [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Katso tiedostosta [`tests/README.md`](../tests/README.md) ohjeet sen suorittamiseen.

## Edellinen oppitunti

[Työkalun käyttö suunnittelumalli](../04-tool-use/README.md)

## Seuraava oppitunti

[Luotettavien tekoälyagenttien rakentaminen](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->