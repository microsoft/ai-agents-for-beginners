# Agentin savutestit

Tämä kansio sisältää **savutestiluettelot** agenteille, jotka rakennat kurssin aikana.
Savutesti on nopea ja halpa tarkistus, jolla varmistetaan, että **Microsoft Foundryssa isännöity
agentti** on saavutettavissa, vastaa ja noudattaa perustavanlaatuisimpia kehotuksensa
odotuksia. Se on ensimmäinen portti — ei korvaus koko arviointiputkelle, jonka opit
[Luvussa 10](../10-ai-agents-production/README.md) ja [Luvussa 16](../16-deploying-scalable-agents/README.md).


Luetteloita käyttää [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub-toiminto [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
työnkulun kautta.

## Kuinka ajaa

1. **Ota tunnin agentti käyttöön** Microsoft Foundryssa isännöitynä agenttina (katso
   Luku 16 käyttöönoton työnkulku). Merkitse muistiin **agentin nimi** ja
   **Foundryn projektin päätepiste**.
2. Lisää nämä arkiston salaisuudet (Asetukset → Salaisuudet ja muuttujat → Toiminnot):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Liitetyn
   identiteetin tulee olla **Azure AI User** -roolissa **Foundryn projektin laajuudessa**.
3. Valitse **Toiminnot**-välilehdeltä **Smoke-test hosted agents** ja valitse
   kyseisen tunnin `tests_file`, syötä sitten vastaavat `agent_name` ja
   `project_endpoint`.

## Luettelo → tunti → agentin nimi

| Luettelo | Tunti | Ota agentti käyttöön nimellä |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Johdatus AI-agenteihin](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Työkalun käyttö](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agenttipohjainen RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Skaalautuvien agenttien käyttöönotto](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Missä tunneissa on savutestit?

Savutestit koskevat tunteja, joissa **oto agentti käyttöön**, jonka tekstivastauksia voidaan
verrata tunnettuun sisältöön. Tunnit, jotka ovat konseptuaalisia, toimivat vain paikallisesti
tai tuottavat ei-determinististä luovaa sisältöä, on tarkoituksella jätetty pois:

- **Tunti 17 (Paikallisten AI-agenttien luominen)** ajetaan kokonaan työasemallasi
  Foundry Localin kanssa ja se **ei** tarjoa Foundry Responses -päätepistettä, joten
  tätä toimintoa ei sovelleta. Tarkista se ajamalla muistikirja paikallisesti.
- Suunnittelumallit ja teoriaosuudet (02, 03, 06, 07, 09, 12) eivät sisällä yhtään
  käyttöön otettavaa agenttia savutestiin.

## Luettelon skeema (nopea viite)

Jokainen luettelo on JSON-dokumentti, jonka pääkutena on `tests`-taulukko. Kukin merkintä lähettää
yhden kehotteen ja tarkistaa vastauksen:

| Kenttä | Merkitys |
|-------|---------|
| `id` | Yksilöllinen vaiheiden tunniste, joka tulostetaan lokiin. |
| `description` | Ihmisen luettava tarkoitus. |
| `prompt` | Agentille lähetetty viesti. |
| `assertions.status` | Odotettu HTTP-tila (oletus 200). |
| `assertions.contains_any` | Läpäisee, jos vastaus sisältää jonkin näistä alimerkkijonoista. |
| `assertions.contains_all` | Läpäisee, jos vastaus sisältää jokaisen alimerkkijonon. |
| `assertions.contains_none` | Läpäisee, jos vastaus ei sisällä mitään näistä alimerkkijonoista. |
| `save_response_id_as` | Tallentaa vastauksen id:n myöhempää monikertaisuutta varten. |
| `use_previous_response_id` | Lähettää tämän vuoron ketjutettuna tallennettuun vastaus-id:hen. |

Tarkastukset ovat kirjainkoon unohtavia alimerkkijonotarkistuksia. Katso
[toiminnon dokumentaatio](https://github.com/marketplace/actions/ai-smoke-test) täydellisestä skeemasta,
mukaan lukien Foundryn hallinnoimat keskusteluresurssit.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->