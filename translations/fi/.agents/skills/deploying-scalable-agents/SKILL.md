---
name: deploying-scalable-agents
license: MIT
---
# Skaalautuvien agenttien käyttöönotto Microsoft Foundryn avulla

> Seurantaosa [Luku 16 – Skaalautuvien agenttien käyttöönotto](../../../16-deploying-scalable-agents/README.md).
> Käytä tätä auttamaan oppijaa siirtämään agentti prototyypistä skaalautuvaan, havaittavaan
> tuotantokäyttöönottoon. Perusta jokainen suositus lukuun ja
> suoritettavaan muistikirjaan; älä keksi Foundryn API-rajapintoja.

## Laukaisimet

Aktivoi tämä osaaminen, kun oppija haluaa:
- Ota agentti käyttöön Microsoft Foundryssa **isännöitynä agenttina** ja tee siitä versioitu/havaittava.
- Valita **asiakas-isännöityjen, isännöityjen agenttien ja agenttityönkulkujen** käyttöönoton välillä.
- Lisätä **mallin reititys**, **vastausten välimuisti** tai **rajoitettu samanaikaisuus** hallitsemaan latenssia ja kustannuksia.
- Lisätä **arviointipistetarkastus**, jotta huono agenttiversio ei voi mennä tuotantoon.
- Lisätä **ihminen-väliintulossa -hyväksyntä** korkean riskin toimenpiteille.
- Instrumentoi agentti **OpenTelemetry**-jäljityksellä tuotantohavaittavuutta varten.
- **Savutesti** otetun agentin nopeaksi käyttöönoton jälkeiseksi portiksi.

## Ydinmalli

Tuotantoagentti on enimmäkseen operatiivinen runko *mallin ympärillä* (~80%),
ei itse malli. Kohdista jokainen suositus yhteen näistä huolenaiheista:

| Huoli | Prototyyppi → Tuotanto |
|---------|------------------------|
| Isännöinti | muistikirja → versioitu isännöity palvelu |
| Identiteetti | sinun `az login` → hallittu identiteetti + rajattu RBAC |
| Tila | muistiin → ulkoistettu säie/muistivarasto |
| Virhe | jäljitteenä → uudelleenyritykset, varatoimet, hälytykset |
| Kustannus | "muutama sentti" → seurattu, reititetty, välimuistitettu, budjetoitu |
| Laatu | silmämääräinen tarkastus → automatisoitu arviointipistetyö |
| Luottamus | sinun hyväksyntäsi → politiikka + ihminen-väliintulossa |

## Käyttöönoton mallit (valitse yksi tai yhdistä)

1. **Asiakas-isännöity** — ajattelusilmukka pyörii sinun prosessissasi. Maksimi hallinta; omistat skaalaamisen/tilan.
2. **Isännöity agentti (Foundry Agent Service)** — Foundry isännöi silmukkaa, tallentaa säikeet, valvoo RBAC-sisältöturvaa, näyttää agentin portaalissa. Vähemmän hallintaa, paljon vähemmän operatiivista pintaa.
3. **Agenttityönkulku** — useita agentteja/työkaluja koostettuna graafiksi haarautumineen, hyväksyntäsolmujen ja kestävien tarkistuspisteiden kanssa.

## Elinkaari (silmukka, joka toimittaa agentin)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**Offline-arviointi on portti, ei jälkikäteen tehtävä** — versiota ei toimiteta
ennen kuin se ylittää kynnyksen. Online-havaittavuus syöttää todelliset virheet takaisin
offline-testiaineistoon.

## Skaalaus- ja kustannusvipuja (prioriteettijärjestyksessä)

1. **Mallin oikea koko** — käytä pienintä mallia, joka läpäisee arviointipisteen.
2. **Reititä monimutkaisuuden mukaan** — pieni/nopea malli yksinkertaisiin pyyntöihin, iso malli todelliseen päättelyyn (tee-se-itse-luokittelija tai Foundry Model Router).
3. **Välimuisti** — palvele lähes identtiset pyynnöt ilman mallikutsua.
4. **Tilaton suunnittelu + rajattu samanaikaisuus** — ulkoista tila; yritä uudelleen viiveellä.

## Tärkeät mallit toistettavaksi

Ohjaa oppija näihin muistikirjasta
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Pyyntöjen käsittelijä**: välimuisti → reititys monimutkaisuuden mukaan → jäljitetyön vaihe → suorita → välimuisti.
- **Arviointipiste**: pisteytä offline-testiaineisto; palauta `pass_rate >= threshold` ja ota käyttöön vain, jos tosi.
- **Ihmisen hyväksyntä**: `@tool(approval_mode="always_require")` toimenpiteille, kuten isot hyvitykset.
- **Jäljitys**: ympäröi jokainen pyyntö `tracer.start_as_current_span(...)` ja aseta attribuutit kuten `routed.model`, `customer.id`.

## Oton jälkeinen savutestaus

Oton jälkeen varmista, että päätepiste todella vastaa (vihreä käyttöönotto voi olla
hiljainen). Käytä [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
toimintoa [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
kanssa luettelossa [`tests/`](../../../tests/README.md). Ajaja POSTaa jokaisen
kehotteen `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`:lle
ja tarkistaa vastaustekstin. Identiteetillä tulee olla rooli **Azure AI User**
Foundry-projektialueella; tokenin vastaanottajan tulee olla `https://ai.azure.com/`.

Kerro porteille kerroksia: **savutesti** (saavutettavissa/vastaava, jokainen käyttöönotto) → **offline-arviointi** (riittävän hyvä lähetettäväksi, ennen promootiota) → **online-arviointi** (kuinka se suoriutuu luonnossa, jatkuva).



## Yrityksen hallinta

- **RBAC**: anna jokaiselle isännöidylle agentille hallittu identiteetti vähimmillä oikeuksilla.
- **MCP tuotannossa**: kohdtele jokaista MCP-palvelinta luottamattomana rajapintana — kiinnitä versio, rajaa identiteetti, validoi tulokset, rajoita nopeutta, älä koskaan paljasta salaisuuksia.

## Avustajan turvarajaukset

- Suosi kurssilla käytettyä kanonista `FoundryChatClient(...)` + `provider.as_agent(...)` -kaavaa.
- Älä lupaa reaaliaikaisia Azure-tuloksia, joita et ole varmistanut; suosittele savutestityönkulkua käyttöönoton vahvistamiseksi.
- Pidä arviointi ja kustannusneuvot sidottuna yhteen: arviointi asettaa laatutason, reititys/välimuisti pitävät kustannuksen lähellä sitä tasoa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->