<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5cc6836626047aa055e8960c8484a7d0",
  "translation_date": "2025-07-24T08:23:59+00:00",
  "source_file": "11-mcp/code_samples/mcp-agents/README.md",
  "language_code": "fi"
}
-->
# Agenttien välisen viestintäjärjestelmän rakentaminen MCP:n avulla

> TL;DR - Voiko MCP:llä rakentaa Agent2Agent-viestintää? Kyllä!

MCP on kehittynyt merkittävästi alkuperäisestä tavoitteestaan "tarjota konteksti LLM:ille". Viimeisimpien parannusten, kuten [jatkettavat streamit](https://modelcontextprotocol.io/docs/concepts/transports#resumability-and-redelivery), [tiedustelu](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation), [näytteenotto](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling) ja ilmoitukset ([edistyminen](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/progress) ja [resurssit](https://modelcontextprotocol.io/specification/2025-06-18/schema#resourceupdatednotification)) ansiosta MCP tarjoaa nyt vankan perustan monimutkaisten agenttien välisen viestintäjärjestelmien rakentamiseen.

## Agentti/Työkalu -väärinkäsitys

Kun yhä useammat kehittäjät tutkivat työkaluja, joilla on agenttimaisia ominaisuuksia (toimivat pitkään, saattavat vaatia lisäsyötettä kesken suorituksen jne.), yleinen väärinkäsitys on, että MCP ei sovellu tähän, koska sen työkalujen primitiiviset esimerkit keskittyivät yksinkertaisiin pyyntö-vastaus-malleihin.

Tämä käsitys on vanhentunut. MCP:n spesifikaatiota on parannettu merkittävästi viime kuukausina ominaisuuksilla, jotka mahdollistavat pitkään toimivan agenttimaisen käyttäytymisen:

- **Streaming & Osittaiset tulokset**: Reaaliaikaiset edistymispäivitykset suorituksen aikana
- **Jatkettavuus**: Asiakkaat voivat muodostaa yhteyden uudelleen ja jatkaa katkoksen jälkeen
- **Kestävyys**: Tulokset säilyvät palvelimen uudelleenkäynnistyksen jälkeen (esim. resurssilinkkien avulla)
- **Monikierroksisuus**: Vuorovaikutteinen syöte kesken suorituksen tiedustelun ja näytteenoton avulla

Näitä ominaisuuksia voidaan yhdistää monimutkaisten agenttien ja monen agentin sovellusten mahdollistamiseksi, kaikki MCP-protokollan avulla.

Viitteeksi kutsumme agenttia "työkaluksi", joka on saatavilla MCP-palvelimella. Tämä tarkoittaa isäntäsovelluksen olemassaoloa, joka toteuttaa MCP-asiakkaan, joka muodostaa istunnon MCP-palvelimen kanssa ja voi kutsua agenttia.

## Mikä tekee MCP-työkalusta "agenttimaisen"?

Ennen kuin siirrymme toteutukseen, määritellään, mitä infrastruktuurikyvykkyyksiä tarvitaan pitkään toimivien agenttien tukemiseksi.

> Määrittelemme agentin autonomiseksi toimijaksi, joka voi toimia pitkään, käsitellä monimutkaisia tehtäviä, jotka saattavat vaatia useita vuorovaikutuksia tai mukautuksia reaaliaikaisen palautteen perusteella.

### 1. Streaming & Osittaiset tulokset

Perinteiset pyyntö-vastaus-mallit eivät toimi pitkään kestävissä tehtävissä. Agenttien on tarjottava:

- Reaaliaikaiset edistymispäivitykset
- Väli-/osatulokset

**MCP-tuki**: Resurssipäivitysilmoitukset mahdollistavat osittaisten tulosten streamauksen, vaikka tämä vaatii huolellista suunnittelua konfliktien välttämiseksi JSON-RPC:n 1:1 pyyntö/vastaus-mallin kanssa.

| Ominaisuus                 | Käyttötapaus                                                                                                                                                                       | MCP-tuki                                                                                   |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Reaaliaikaiset edistymispäivitykset | Käyttäjä pyytää koodikannan migraatiotehtävää. Agentti streamaa edistymistä: "10% - Analysoidaan riippuvuuksia... 25% - Muutetaan TypeScript-tiedostoja... 50% - Päivitetään tuontitiedostoja..." | ✅ Edistymisilmoitukset                                                                     |
| Osittaiset tulokset        | "Kirjan luominen" -tehtävä streamaa osittaisia tuloksia, esim. 1) Juonikaavio, 2) Lukuotsikot, 3) Jokainen luku valmistuessaan. Isäntä voi tarkastella, peruuttaa tai ohjata uudelleen missä tahansa vaiheessa. | ✅ Ilmoituksia voidaan "laajentaa" sisältämään osittaisia tuloksia, katso ehdotukset PR 383, 776 |

### 2. Jatkettavuus

Agenttien on käsiteltävä verkkokatkoksia sujuvasti:

- Yhteyden muodostaminen uudelleen (asiakas) katkoksen jälkeen
- Jatkaminen siitä, mihin jäätiin (viestien uudelleentoimitus)

**MCP-tuki**: MCP StreamableHTTP -kuljetus tukee nykyään istunnon jatkamista ja viestien uudelleentoimitusta istuntotunnuksilla ja viimeisten tapahtumatunnusten avulla. Tärkeä huomio tässä on, että palvelimen on toteutettava EventStore, joka mahdollistaa tapahtumien uudelleentoiston asiakaspuolen yhteyden muodostamisen yhteydessä.

### 3. Kestävyys

Pitkään toimivien agenttien on säilytettävä tila:

- Tulokset säilyvät palvelimen uudelleenkäynnistyksen jälkeen
- Tila voidaan hakea erillään
- Edistymisen seuranta istuntojen välillä

**MCP-tuki**: MCP tukee nyt resurssilinkkien palautustyyppiä työkaluja kutsuttaessa. Nykyään yleinen tapa on suunnitella työkalu, joka luo resurssin ja palauttaa välittömästi resurssilinkin. Työkalu voi jatkaa tehtävän käsittelyä taustalla ja päivittää resurssia. Asiakas voi puolestaan valita resurssin tilan kyselyn saadakseen osittaisia tai täydellisiä tuloksia (perustuen siihen, mitä resurssipäivityksiä palvelin tarjoaa) tai tilata resurssin päivitysilmoituksia.

### 4. Monikierroksiset vuorovaikutukset

Agentit tarvitsevat usein lisäsyötettä kesken suorituksen:

- Ihmisen tarkennus tai hyväksyntä
- AI-apu monimutkaisiin päätöksiin
- Dynaaminen parametrien säätö

**MCP-tuki**: Täysin tuettu näytteenoton (AI-syöte) ja tiedustelun (ihmisen syöte) avulla.

## Pitkään toimivien agenttien toteuttaminen MCP:llä - Koodikatsaus

Osana tätä artikkelia tarjoamme [koodivaraston](https://github.com/victordibia/ai-tutorials/tree/main/MCP%20Agents), joka sisältää täydellisen toteutuksen pitkään toimivista agenteista MCP Python SDK:n avulla StreamableHTTP-kuljetuksella istunnon jatkamista ja viestien uudelleentoimitusta varten.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.