<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5cc6836626047aa055e8960c8484a7d0",
  "translation_date": "2025-08-29T18:27:59+00:00",
  "source_file": "11-agentic-protocols/code_samples/mcp-agents/README.md",
  "language_code": "fi"
}
-->
# Agenttien välisen viestintäjärjestelmien rakentaminen MCP:llä

> TL;DR - Voitko rakentaa Agent2Agent-viestintää MCP:llä? Kyllä!

MCP on kehittynyt merkittävästi alkuperäisestä tavoitteestaan "tarjota konteksti LLM:ille". Viimeisimmät parannukset, kuten [jatkettavat streamit](https://modelcontextprotocol.io/docs/concepts/transports#resumability-and-redelivery), [tiedonkeruu](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation), [näytteenotto](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling) ja ilmoitukset ([edistyminen](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/progress) ja [resurssit](https://modelcontextprotocol.io/specification/2025-06-18/schema#resourceupdatednotification)), tarjoavat nyt vankan perustan monimutkaisten agenttien välisen viestintäjärjestelmien rakentamiseen.

## Agentti/Työkalu-harhaluulo

Kun yhä useammat kehittäjät tutkivat työkaluja, joilla on agenttimaisia ominaisuuksia (toimivat pitkään, saattavat vaatia lisäsyötettä kesken suorituksen jne.), yleinen harhaluulo on, että MCP ei sovellu tähän, koska sen varhaiset esimerkit keskittyivät yksinkertaisiin pyyntö-vastaus-malleihin.

Tämä käsitys on vanhentunut. MCP:n spesifikaatiota on parannettu merkittävästi viime kuukausina, ja se sisältää ominaisuuksia, jotka mahdollistavat pitkäkestoisen agenttimaisen toiminnan:

- **Streaming & Osittaiset tulokset**: Reaaliaikaiset edistymispäivitykset suorituksen aikana
- **Jatkettavuus**: Asiakkaat voivat muodostaa yhteyden uudelleen ja jatkaa katkoksen jälkeen
- **Kestävyys**: Tulokset säilyvät palvelimen uudelleenkäynnistyksen jälkeen (esim. resurssilinkkien kautta)
- **Monivaiheisuus**: Vuorovaikutteinen syöte kesken suorituksen tiedonkeruun ja näytteenoton avulla

Näitä ominaisuuksia voidaan yhdistää monimutkaisten agenttien ja monen agentin sovellusten mahdollistamiseksi, kaikki MCP-protokollan avulla.

Viitteenä kutsumme agenttia "työkaluksi", joka on saatavilla MCP-palvelimella. Tämä tarkoittaa isäntäohjelman olemassaoloa, joka toteuttaa MCP-asiakkaan, muodostaa istunnon MCP-palvelimen kanssa ja voi kutsua agenttia.

## Mikä tekee MCP-työkalusta "agenttimaisen"?

Ennen kuin siirrymme toteutukseen, määritellään, mitä infrastruktuurikyvykkyyksiä tarvitaan pitkäkestoisten agenttien tukemiseen.

> Määrittelemme agentin entiteetiksi, joka voi toimia itsenäisesti pitkän ajan, käsitellä monimutkaisia tehtäviä, jotka saattavat vaatia useita vuorovaikutuksia tai säätöjä reaaliaikaisen palautteen perusteella.

### 1. Streaming & Osittaiset tulokset

Perinteiset pyyntö-vastaus-mallit eivät toimi pitkäkestoisissa tehtävissä. Agenttien on tarjottava:

- Reaaliaikaisia edistymispäivityksiä
- Välituloksia

**MCP-tuki**: Resurssipäivitysilmoitukset mahdollistavat osittaisten tulosten streamauksen, vaikka tämä vaatii huolellista suunnittelua konfliktien välttämiseksi JSON-RPC:n 1:1 pyyntö/vastaus-mallin kanssa.

| Ominaisuus                 | Käyttötapaus                                                                                                                                                                       | MCP-tuki                                                                                   |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Reaaliaikaiset edistymispäivitykset | Käyttäjä pyytää koodikannan migraatiotehtävää. Agentti streamaa edistymistä: "10% - Analysoidaan riippuvuuksia... 25% - Muutetaan TypeScript-tiedostoja... 50% - Päivitetään tuontitiedostoja..." | ✅ Edistymisilmoitukset                                                                     |
| Osittaiset tulokset        | "Kirjan luominen" -tehtävä streamaa osittaisia tuloksia, esim. 1) Juonikaavio, 2) Lukuvalikko, 3) Jokainen luku valmistuessaan. Isäntä voi tarkastella, peruuttaa tai ohjata uudelleen missä tahansa vaiheessa. | ✅ Ilmoituksia voidaan "laajentaa" sisällyttämään osittaisia tuloksia, katso ehdotukset PR 383, 776 |

### 2. Jatkettavuus

Agenttien on käsiteltävä verkkokatkoksia sujuvasti:

- Yhteyden muodostaminen uudelleen (asiakas) katkoksen jälkeen
- Jatkaminen siitä, mihin jäätiin (viestien uudelleentoimitus)

**MCP-tuki**: MCP StreamableHTTP -kuljetus tukee nykyään istunnon jatkamista ja viestien uudelleentoimitusta istuntotunnusten ja viimeisten tapahtumatunnusten avulla. Tärkeä huomio tässä on, että palvelimen on toteutettava EventStore, joka mahdollistaa tapahtumien uudelleentoiston asiakasohjelman uudelleenyhdistämisen yhteydessä.  
Huomaa, että yhteisön ehdotus (PR #975) tutkii kuljetusagnostisia jatkettavia streameja.

| Ominaisuus      | Käyttötapaus                                                                                                                                                   | MCP-tuki                                                                 |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Jatkettavuus    | Asiakas katkaisee yhteyden pitkäkestoisen tehtävän aikana. Uudelleenyhdistämisen jälkeen istunto jatkuu, ja menetetyt tapahtumat toistetaan saumattomasti siitä, mihin jäätiin. | ✅ StreamableHTTP-kuljetus istuntotunnusten, tapahtumien toiston ja EventStoren avulla |

### 3. Kestävyys

Pitkäkestoiset agentit tarvitsevat pysyvän tilan:

- Tulokset säilyvät palvelimen uudelleenkäynnistyksen jälkeen
- Tila voidaan hakea erillään
- Edistymisen seuranta istuntojen välillä

**MCP-tuki**: MCP tukee nyt resurssilinkkien palautustyyppiä työkalu-kutsuille. Nykyään mahdollinen malli on suunnitella työkalu, joka luo resurssin ja palauttaa välittömästi resurssilinkin. Työkalu voi jatkaa tehtävän käsittelyä taustalla ja päivittää resurssia. Asiakas voi puolestaan valita resurssin tilan kyselyn saadakseen osittaisia tai täydellisiä tuloksia (perustuen siihen, mitä resurssipäivityksiä palvelin tarjoaa) tai tilata resurssin päivitysilmoituksia.

Yksi rajoitus tässä on, että resurssien kysely tai päivitysten tilaaminen voi kuluttaa resursseja, mikä voi vaikuttaa skaalautuvuuteen. Avoin yhteisön ehdotus (mukaan lukien #992) tutkii mahdollisuutta sisällyttää webhookeja tai laukaisimia, joita palvelin voi kutsua ilmoittaakseen asiakkaalle/isäntäohjelmalle päivityksistä.

| Ominaisuus    | Käyttötapaus                                                                                                                                        | MCP-tuki                                                        |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Kestävyys     | Palvelin kaatuu datan migraatiotehtävän aikana. Tulokset ja edistyminen säilyvät uudelleenkäynnistyksen jälkeen, asiakas voi tarkistaa tilan ja jatkaa pysyvästä resurssista. | ✅ Resurssilinkit pysyvällä tallennuksella ja tilailmoituksilla |

### 4. Monivaiheiset vuorovaikutukset

Agentit tarvitsevat usein lisäsyötettä kesken suorituksen:

- Ihmisen tarkennus tai hyväksyntä
- AI-apu monimutkaisiin päätöksiin
- Dynaaminen parametrien säätö

**MCP-tuki**: Täysin tuettu näytteenoton (AI-syöte) ja tiedonkeruun (ihmisen syöte) avulla.

| Ominaisuus                 | Käyttötapaus                                                                                                                                     | MCP-tuki                                           |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Monivaiheiset vuorovaikutukset | Matkavarauksen agentti pyytää käyttäjältä hintavahvistusta, sitten pyytää AI:ta tiivistämään matkadataa ennen varauksen viimeistelyä. | ✅ Tiedonkeruu ihmisen syötteelle, näytteenotto AI-syötteelle |

## Toteutus pitkäkestoisille agenteille MCP:llä - Koodikatsaus

Osana tätä artikkelia tarjoamme [koodivaraston](https://github.com/victordibia/ai-tutorials/tree/main/MCP%20Agents), joka sisältää täydellisen toteutuksen pitkäkestoisille agenteille MCP Python SDK:lla käyttäen StreamableHTTP-kuljetusta istunnon jatkamiseen ja viestien uudelleentoimitukseen. Toteutus osoittaa, kuinka MCP:n ominaisuuksia voidaan yhdistää mahdollistamaan kehittyneitä agenttimaisia toimintoja.

## Johtopäätös

MCP:n parannetut ominaisuudet - resurssipäivitykset, tiedonkeruu/näytteenotto, jatkettavat streamit ja pysyvät resurssit - mahdollistavat monimutkaiset agenttien väliset vuorovaikutukset samalla säilyttäen protokollan yksinkertaisuuden.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.