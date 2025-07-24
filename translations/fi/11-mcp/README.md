<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T08:36:53+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "fi"
}
-->
# Oppitunti 11: Model Context Protocol (MCP) -integraatio

## Johdatus Model Context Protocoliin (MCP)

Model Context Protocol (MCP) on huippuluokan kehys, joka on suunniteltu standardoimaan vuorovaikutukset tekoälymallien ja asiakassovellusten välillä. MCP toimii sillan tavoin tekoälymallien ja niitä käyttävien sovellusten välillä, tarjoten yhtenäisen rajapinnan riippumatta mallin toteutuksesta.

MCP:n keskeiset ominaisuudet:

- **Standardoitu viestintä**: MCP luo yhteisen kielen sovellusten ja tekoälymallien väliseen viestintään
- **Parannettu kontekstinhallinta**: Mahdollistaa tehokkaan kontekstuaalisen tiedon välittämisen tekoälymalleille
- **Yhteensopivuus eri alustoilla**: Toimii useilla ohjelmointikielillä, kuten C#, Java, JavaScript, Python ja TypeScript
- **Helppo integrointi**: Mahdollistaa erilaisten tekoälymallien vaivattoman integroinnin sovelluksiin

MCP on erityisen hyödyllinen tekoälyagenttien kehityksessä, sillä se mahdollistaa agenttien vuorovaikutuksen eri järjestelmien ja tietolähteiden kanssa yhtenäisen protokollan kautta, tehden agenteista joustavampia ja tehokkaampia.

## Oppimistavoitteet
- Ymmärtää, mitä MCP on ja sen rooli tekoälyagenttien kehityksessä
- Asentaa ja konfiguroida MCP-palvelin GitHub-integraatiota varten
- Rakentaa monen agentin järjestelmä MCP-työkaluilla
- Toteuttaa RAG (Retrieval Augmented Generation) Azure Cognitive Searchin avulla

## Esivaatimukset
- Python 3.8+
- Node.js 14+
- Azure-tilaus
- GitHub-tili
- Perustiedot Semantic Kernelistä

## Asennusohjeet

1. **Ympäristön asennus**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure-palveluiden konfigurointi**
   - Luo Azure Cognitive Search -resurssi
   - Määritä Azure OpenAI -palvelu
   - Konfiguroi ympäristömuuttujat tiedostossa `.env`

3. **MCP-palvelimen asennus**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Projektin rakenne

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## Keskeiset komponentit

### 1. Monen agentin järjestelmä
- GitHub-agentti: Repositorion analyysi
- Hackathon-agentti: Projektisuositukset
- Tapahtuma-agentti: Teknologiatapahtumien ehdotukset

### 2. Azure-integraatio
- Cognitive Search tapahtumien indeksointiin
- Azure OpenAI agenttien älykkyyteen
- RAG-mallin toteutus

### 3. MCP-työkalut
- GitHub-repositorion analyysi
- Koodin tarkastus
- Metadataan poiminta

## Koodin läpikäynti

Esimerkki näyttää:
1. MCP-palvelimen integroinnin
2. Monen agentin orkestroinnin
3. Azure Cognitive Search -integraation
4. RAG-mallin toteutuksen

Keskeiset ominaisuudet:
- Reaaliaikainen GitHub-repositorion analyysi
- Älykkäät projektisuositukset
- Tapahtumien yhdistäminen Azure Searchin avulla
- Vastausten suoratoisto Chainlitin avulla

## Esimerkin suorittaminen

Yksityiskohtaiset asennusohjeet ja lisätiedot löytyvät [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Käynnistä MCP-palvelin:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Käynnistä sovellus:
   ```bash
   chainlit run app.py -w
   ```

3. Testaa integraatio:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Vianmääritys

Yleisiä ongelmia ja ratkaisuja:
1. MCP-yhteysongelmat
   - Varmista, että palvelin on käynnissä
   - Tarkista portin saatavuus
   - Vahvista GitHub-tunnukset

2. Azure Search -ongelmat
   - Tarkista yhteysmerkkijonot
   - Varmista indeksin olemassaolo
   - Vahvista dokumenttien lataus

## Seuraavat askeleet
- Tutustu lisätyökaluihin MCP:ssä
- Toteuta omia agentteja
- Paranna RAG-ominaisuuksia
- Lisää uusia tapahtumalähteitä
- **Edistynyt**: Katso [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) esimerkkejä agenttien välisestä viestinnästä

## Resurssit
- [MCP aloittelijoille](https://aka.ms/mcp-for-beginners)  
- [MCP-dokumentaatio](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search -dokumentaatio](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel -oppaat](https://learn.microsoft.com/semantic-kernel/)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.