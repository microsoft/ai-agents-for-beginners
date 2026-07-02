[![Agentic RAG](../../../translated_images/fi/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Napsauta yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Agentic RAG

Tämä oppitunti tarjoaa kattavan yleiskatsauksen Agentic Retrieval-Augmented Generation -mallista (Agentic RAG), nousevasta tekoälyparadigmasta, jossa suuret kielimallit (LLM) suunnittelevat itsenäisesti seuraavia askeleitaan samalla kun ne hakevat tietoa ulkoisista lähteistä. Toisin kuin staattiset haku-lue -mallit, Agentic RAG sisältää toistuvia LLM-kutsuja, joita rytmittävät työkalujen tai funktioiden kutsut sekä rakenteelliset vastaukset. Järjestelmä arvioi tuloksia, tarkentaa kyselyjä, kutsuu tarvittaessa lisätyökaluja ja jatkaa tätä sykliä, kunnes saavutetaan tyydyttävä ratkaisu.

## Johdanto

Tässä oppitunnissa käydään läpi

- **Agentic RAG:n ymmärtäminen:** Opi nouseva tekoälyparadigma, jossa suuret kielimallit (LLM) suunnittelevat itsenäisesti seuraavat toimenpiteensä samalla kun hakevat tietoa ulkoisista tietolähteistä.
- **Iteratiivisen Maker-Checker-tyylin hallitseminen:** Ymmärrys LLM:n toistuvista kutsuista, joita rytmittävät työkalujen tai funktioiden kutsut sekä rakenteelliset vastaukset, parantamaan oikeellisuutta ja käsittelemään virheellisiä kyselyitä.
- **Käytännön sovellusten tutkiminen:** Tunnista tilanteet, joissa Agentic RAG loistaa, kuten oikeellisuuteen keskittyvissä ympäristöissä, monimutkaisessa tietokantaintegraatiossa ja laajennetuissa työnkuluissa.

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat/ymmärrät:

- **Agentic RAG:n ymmärtäminen:** Opi nousevaan tekoälyparadigmaan, jossa suuret kielimallit (LLM) suunnittelevat itsenäisesti seuraavat askeleensa samalla kun hakevat tietoa ulkoisista tietolähteistä.
- **Iteratiivinen Maker-Checker-tyyli:** Ymmärrä toistuvien LLM-kutsujen, työkalujen tai funktioiden kutsujen ja rakenteellisten vastausten kierron käsite, joka parantaa oikeellisuutta ja käsittelee virheellisiä kyselyitä.
- **Päätöksenteon omistaminen:** Opi järjestelmän kyvystä omistaa päätöksentekoprosessinsa, päättää lähestymistavasta ongelmiin ilman ennalta määriteltyjä polkuja.
- **Työnkulku:** Ymmärrä, miten agenttipohjainen malli itsenäisesti päättää hakea markkinatrendiraportit, tunnistaa kilpailijatiedot, yhdistää sisäiset myyntimittarit, syntetisoi löydökset ja arvioi strategian.
- **Iteratiiviset silmukat, työkalujen integrointi ja muisti:** Opi järjestelmän nojaavan toistuviin vuorovaikutusmalleihin, ylläpitäen tilaa ja muistia askelten välillä välttääkseen toistuvia silmukoita ja tehdäkseen perusteltuja päätöksiä.
- **Virhetilanteiden käsittely ja itsensä korjaaminen:** Tutki järjestelmän vahvoja itsekorjausmekanismeja, mukaan lukien iterointi ja uudelleenkyselyt, diagnostiikkatyökalujen käyttö ja ihmisen valvontaan tukeutuminen.
- **Agenttisuuden rajat:** Ymmärrä Agentic RAG:n rajat, keskittyen toimialakohtaiseen autonomiaan, infrastruktuuririippuvuuteen ja valvontarajojen kunnioittamiseen.
- **Käytännön käyttötapaukset ja arvo:** Tunnista tilanteet, joissa Agentic RAG loistaa, kuten oikeellisuuteen painottuvissa ympäristöissä, monimutkaisissa tietokantaintegraatioissa ja laajennetuissa työnkuluissa.
- **Hallinto, läpinäkyvyys ja luottamus:** Opi hallinnon ja läpinäkyvyyden merkityksestä, mukaan lukien selitettävä päätöksenteko, harhavalvonta ja ihmisen valvonta.

## Mitä Agentic RAG on?

Agentic Retrieval-Augmented Generation (Agentic RAG) on nouseva tekoälyparadigma, jossa suuret kielimallit (LLM) suunnittelevat itsenäisesti seuraavia askeleitaan samalla kun hakevat tietoa ulkoisista lähteistä. Toisin kuin staattiset haku-lue -mallit, Agentic RAG sisältää toistuvia LLM-kutsuja, joita rytmittävät työkalujen tai funktioiden kutsut sekä rakenteelliset vastaukset. Järjestelmä arvioi tuloksia, tarkentaa kyselyjä, kutsuu tarvittaessa lisätyökaluja ja jatkaa tätä sykliä, kunnes saavutetaan tyydyttävä ratkaisu. Tämä iteratiivinen "maker-checker" -tyyli parantaa oikeellisuutta, käsittelee virheellisiä kyselyitä ja takaa korkealaatuiset tulokset.

Järjestelmä omistaa aktiivisesti päätöksentekoprosessinsa, kirjoittaa epäonnistuneet kyselyt uudelleen, valitsee erilaiset hakumenetelmät ja integroi useita työkaluja — kuten vektorihakua Azure AI Searchissa, SQL-tietokantoja tai räätälöityjä rajapintoja — ennen kuin lopettaa vastauksensa. Agenttijärjestelmän erotteleva piirre on kyky omistaa ajatteluprosessinsa. Perinteiset RAG-toteutukset nojaavat ennalta määriteltyihin polkuihin, mutta agenttipohjainen järjestelmä päättää itsenäisesti askeleiden sarjan löydetyn tiedon laadun perusteella.

## Agentic Retrieval-Augmented Generationin määrittely (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) on nouseva tekoälykehityksen paradigma, jossa LLM-mallit eivät ainoastaan hae tietoa ulkoisista lähteistä vaan myös suunnittelevat itsenäisesti seuraavat askeleensa. Toisin kuin staattiset haku-lue -mallit tai huolellisesti ohjelmoidut kehotussekvenssit, Agentic RAG sisältää toistuvan silmukan, jossa LLM:lle tehdään toistuvia kutsuja, joita rytmittävät työkalujen tai funktioiden kutsut ja rakenteelliset vastaukset. Joka käänteessä järjestelmä arvioi saatuja tuloksia, päättää tarkentaa kyselyjä, kutsuu lisätyökaluja tarvittaessa ja jatkaa tätä sykliä, kunnes saavutetaan tyydyttävä ratkaisu.

Tämä iteratiivinen “maker-checker” -toimintatyyli on suunniteltu parantamaan oikeellisuutta, käsittelemään virheellisiä kyselyitä rakenteellisissa tietokannoissa (esim. NL2SQL) ja varmistamaan tasapainoisen ja korkealaatuisen lopputuloksen. Sen sijaan, että luotettaisiin pelkästään huolellisesti suunniteltuihin kehotusketjuihin, järjestelmä omistaa päätöksentekoprosessin aktiivisesti. Se voi kirjoittaa epäonnistuneet kyselyt uudelleen, valita erilaisia haku- tai tietolähdekeinoja ja integroida useita työkaluja — kuten vektorihakua Azure AI Searchissa, SQL-tietokantoja tai räätälöityjä rajapintoja — ennen vastauksen lopullista muodostamista. Tämä poistaa tarpeen monimutkaisille orkestrointikehyksille. Sen sijaan suhteellisen yksinkertainen sykli “LLM-kutsu → työkalun käyttö → LLM-kutsu → …” voi tuottaa monimutkaisia ja hyvin perusteltuja vastauksia.

![Agentic RAG Core Loop](../../../translated_images/fi/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Päätöksenteon omistaminen

Erottava piirre, joka tekee järjestelmästä “agenttisen”, on sen kyky omistaa päätöksentekoprosessi. Perinteiset RAG-toteutukset usein riippuvat ihmisistä, jotka määrittelevät mallille polun: ajatusketjun, joka kertoo, mitä haetaan ja milloin. Mutta kun järjestelmä on todella agenttinen, se päättää sisäisesti, miten lähestyy ongelmaa. Se ei vain suorita skriptiä, vaan päättää autonomisesti askelien sarjan löydetyn tiedon laadun perusteella.

Esimerkiksi jos järjestelmää pyydetään luomaan tuotteen lanseerausstrategia, se ei perustu pelkästään kehotukseen, joka selittää koko tutkimus- ja päätöksentekoprosessin. Sen sijaan agenttinen malli itsenäisesti päättää:

1. Hakea ajantasaiset markkinatrendiraportit käyttäen Bing Web Groundingia
2. Tunnistaa relevantit kilpailijatiedot Azure AI Searchin avulla
3. Yhdistää historialliset sisäiset myyntimittarit Azure SQL -tietokannasta
4. Syntetisoida löydökset yhdeksi yhtenäiseksi strategiaksi orkestroituna Azure OpenAI -palvelun kautta
5. Arvioida strategia mahdollisten aukkojen tai epäjohdonmukaisuuksien varalta, ja tarvittaessa käynnistää uusi hakukierros

Kaikki nämä vaiheet — kyselyjen tarkentaminen, lähteiden valinta, iterointi vastaukseen tyytyväiseksi — päätetään mallin toimesta, eivät ennalta ihmisen skriptaamina.

## Iteratiiviset silmukat, työkalujen integrointi ja muisti

![Tool Integration Architecture](../../../translated_images/fi/tool-integration.0f569710b5c17c10.webp)

Agenttijärjestelmä perustuu toistuvaan vuorovaikutuskuvioon:

- **Alkukutsu:** Käyttäjän tavoite (eli käyttäjän kehotus) esitetään LLM:lle.
- **Työkalun kutsu:** Jos malli havaitsee puutteellista tietoa tai epäselviä ohjeita, se valitsee työkalun tai hakumenetelmän — kuten vektoritietokantahaku (esim. Azure AI Search Hybrid hakee yksityisistä tiedoista) tai rakenteellisen SQL-kyselyn — saadakseen lisää kontekstia.
- **Arviointi ja tarkentaminen:** Tarkastettuaan palautetut tiedot, malli päättää, riittääkö tieto. Jos ei, se tarkentaa kyselyä, kokeilee eri työkalua tai muuttaa lähestymistapaansa.
- **Toisto, kunnes tyytyväinen:** Tämä sykli jatkuu, kunnes malli katsoo saavuttaneensa riittävän selvyyden ja todisteet voidakseen antaa lopullisen hyvin perustellun vastauksen.
- **Muisti ja tila:** Järjestelmä säilyttää tilan ja muistin askelten välillä, jolloin se voi muistaa aiemmat yritykset ja niiden tulokset, välttyä toistuvilta silmukoilta ja tehdä perustellumpia päätöksiä edetessään.

Ajan myötä tämä luo kehittyvän ymmärryksen tunteen, mahdollistaen mallin navigoinnin monimutkaisissa, monivaiheisissa tehtävissä ilman ihmisen jatkuvaa puuttumista tai kehotteen uudelleensuunnittelua.

## Virhetilanteiden käsittely ja itsekorjaus

Agentic RAG:n autonomia sisältää myös vahvat itsekorjausmekanismit. Kun järjestelmä törmää umpikujiin — kuten epäolennaisten dokumenttien palauttamiseen tai virheellisiin kyselyihin — se voi:

- **Iteroida ja uudelleenkysellä:** Sen sijaan, että palauttaisi vähäarvoisia vastauksia, malli kokeilee uusia hakustrategioita, kirjoittaa tietokantakyselyt uudelleen tai tutkii vaihtoehtoisia tietoaineistoja.
- **Käyttää diagnostiikkatyökaluja:** Järjestelmä voi kutsua lisätoimintoja, joiden avulla se voi debugata päätöksentekovaiheita tai varmistaa haetun tiedon oikeellisuuden. Työkalut kuten Azure AI Tracing ovat tärkeitä mahdollistamaan tehokkaan havaittavuuden ja valvonnan.
- **Palata ihmisen valvontaan:** Korkean panoksen tai toistuvasti epäonnistuvissa tilanteissa malli voi raportoida epävarmuuden ja pyytää ihmisen ohjausta. Kun ihminen antaa korjaavaa palautetta, malli voi käyttää tätä oppinaan tulevaisuudessa.

Tämä iteratiivinen ja dynaaminen lähestymistapa mahdollistaa mallin jatkuvan kehittymisen, varmistaen, ettei kyse ole vain yksittäisestä ajosta vaan oppivasta järjestelmästä, joka oppii virheistään kyseisen istunnon aikana.

![Self Correction Mechanism](../../../translated_images/fi/self-correction.da87f3783b7f174b.webp)

## Agenttisuuden rajat

Vaikka se on autonominen tehtävän sisällä, Agentic RAG ei ole sama asia kuin yleinen tekoäly (Artificial General Intelligence, AGI). Sen "agenttisen" kyvyt rajoittuvat niihin työkaluihin, tietolähteisiin ja politiikkoihin, joita ihmiskehittäjät ovat määrittäneet. Se ei voi keksiä omia työkalujaan tai astua asetettujen toimialarajojen ulkopuolelle. Sen sijaan se loistaa nykyisten resurssien dynaamisessa orkestroinnissa.

Keskeisiä eroja kehittyneempiin tekoälymuotoihin verrattuna ovat:

1. **Toimialakohtainen autonomia:** Agentic RAG -järjestelmät keskittyvät saavuttamaan käyttäjän määrittelemiä tavoitteita tunnetulla toimialalla, hyödyntäen strategioina esimerkiksi kyselyjen uudelleenkirjoitusta tai työkalujen valintaa parantaakseen tuloksia.
2. **Infrastruktuuririippuvuus:** Järjestelmän kyvyt riippuvat kehittäjien integroimista työkaluista ja tiedoista. Se ei kykene ylittämään näitä rajoja ilman ihmisen puuttumista.
3. **Valvontarajojen kunnioitus:** Eettiset ohjeistukset, vaatimustenmukaisuus ja liiketoimintakäytännöt ovat erittäin tärkeitä. Agentin vapaus on aina rajoitettu turvallisuus- ja valvontamekanismeilla (toivottavasti?).

## Käytännön käyttötapaukset ja arvo

Agentic RAG loistaa tilanteissa, jotka vaativat iteratiivista tarkentamista ja tarkkuutta:

1. **Oikeellisuuteen painottuvat ympäristöt:** Noudattavuustarkastuksissa, sääntelyanalyysissä tai oikeudellisessa tutkimuksessa agenttimalli voi toistuvasti varmistaa faktat, konsultoida useita lähteitä ja kirjoittaa kyselyt uudelleen, kunnes se tuottaa huolellisesti tarkistetun vastauksen.
2. **Monimutkaiset tietokantaintegraatiot:** Rakenteellisen datan kanssa työskenneltäessä, missä kyselyt epäonnistuvat usein tai tarvitsevat tarkennusta, järjestelmä voi itsenäisesti hienosäätää kyselyitään käyttäen Azure SQL -tietokantaa tai Microsoft Fabric OneLakea varmistaen haun kohdistumisen käyttäjän tarkoitukseen.
3. **Laajennetut työnkulut:** Pitkäkestoiset sessiot saattavat kehittyä uusien tietojen ilmaantuessa. Agentic RAG voi jatkuvasti ottaa mukaan uutta dataa ja muuttaa strategioitaan oppiessaan lisää ongelma-alueesta.

## Hallinto, läpinäkyvyys ja luottamus

Näiden järjestelmien itsenäistyessä päätöksenteossa hallinto ja läpinäkyvyys ovat ratkaisevan tärkeitä:

- **Selitettävä päätöksenteko:** Malli voi tarjota jäljitettävän polun tekemistään kyselyistä, heille konsultoiduista lähteistä ja käytetyistä päätöksentekovaiheista. Työkalut kuten Azure AI Content Safety ja Azure AI Tracing / GenAIOps auttavat ylläpitämään läpinäkyvyyttä ja vähentämään riskejä.
- **Harhavalvonta ja tasapainoinen haku:** Kehittäjät voivat säätää hakustrategioita varmistaakseen, että harkitut, edustavat tietolähteet otetaan huomioon, ja säännöllisesti tarkastaa tuotoksia harhojen tai vääristymien varalta käyttämällä räätälöityjä malleja kehittyneille data-analytiikkaorganisaatioille Azure Machine Learningin avulla.
- **Ihmisen valvonta ja vaatimustenmukaisuus:** Sensitiivissä tehtävissä ihmisen arviointi on edelleen välttämätöntä. Agentic RAG ei korvaa ihmisen harkintaa tärkeissä päätöksissä — se täydentää sitä toimittamalla huolellisemmin tarkistettuja vaihtoehtoja.

On välttämätöntä, että järjestelmällä on työkalut, jotka tarjoavat selkeän toimintalokin. Ilman niitä monivaiheisen prosessin virheiden etsiminen voi olla erittäin vaikeaa. Katso seuraava Literal AI:n (Chainlitin taustayritys) esimerkki Agentin ajosta:

![AgentRunExample](../../../translated_images/fi/AgentRunExample.471a94bc40cbdc0c.webp)

## Yhteenveto

Agentic RAG edustaa luonnollista kehitysvaihetta siinä, miten tekoälyjärjestelmät käsittelevät monimutkaisia ja dataintensiivisiä tehtäviä. Omaksumalla toistuvan vuorovaikutusmallin, valitsemalla työkalut itsenäisesti ja tarkentamalla kyselyjä, kunnes laadukas lopputulos saavutetaan, järjestelmä siirtyy pois staattisesta kehoteohjatusta toiminnasta kohti adaptiivisempaa, kontekstia ymmärtävää päätöksentekijää. Vaikka se on edelleen ihmisen määrittelemien infrastruktuurien ja eettisten ohjeistusten rajoittama, nämä agenttipohjaiset kyvyt mahdollistavat rikkaampia, dynaamisempia ja lopulta hyödyllisempiä tekoälyn vuorovaikutuksia sekä yrityksille että loppukäyttäjille.

### Onko sinulla lisää kysymyksiä Agentic RAG:sta?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavattuaksesi muita oppijoita, osallistuaksesi toimistoaikoihin ja saadaksesi vastauksia tekoälyagenttikysymyksiisi.

## Lisäresurssit

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Ota käyttöön Retrieval Augmented Generation (RAG) Azure OpenAI -palvelulla: Opi käyttämään omia tietojasi Azure OpenAI -palvelun kanssa. Tämä Microsoft Learn -moduuli tarjoaa kattavan oppaan RAG:n toteutukseen</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatiivisten tekoälysovellusten arviointi Microsoft Foundryn avulla: Tämä artikkeli kattaa mallien arvioinnin ja vertailun julkisesti saatavilla olevilla aineistoilla, mukaan lukien Agentic AI -sovellukset ja RAG-arkkitehtuurit</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Mitä on Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Täydellinen opas agenttipohjaiseen Retrieval Augmented Generationiin – Uutisia generation RAG:sta</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: tehosta RAG:iasi kyselyn uudelleenmuodostuksella ja itse-kyselyllä! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Agenttikerrosten lisääminen RAG:iin</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Tiedonavustajien tulevaisuus: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Kuinka rakentaa agenttisia RAG-järjestelmiä</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Microsoft Foundry Agent -palvelun käyttö tekoälyagenttien skaalaamiseen</a>

### Akateemiset artikkelit

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iteratiivinen parantaminen itsepalautteella</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Kielipohjaiset agentit verbaalisella vahvistusoppimisella</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Suuret kielimallit voivat korjata itseään työkalupohjaisella arvioinnilla</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Katsaus agenttiseen RAG:iin</a>

## Edellinen oppitunti

[Työkalun käyttö -suunnittelumalli](../04-tool-use/README.md)

## Seuraava oppitunti

[Luotettavien tekoälyagenttien rakentaminen](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->