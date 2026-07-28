[![Kuinka suunnitella hyviä tekoälyagentteja](../../../translated_images/fi/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

# Työkalun käyttö -suunnittelumalli

Työkalut ovat kiinnostavia, koska niiden avulla tekoälyagentit voivat saada laajemman valikoiman kykyjä. Sen sijaan, että agentilla olisi rajattu joukko toimintoja, joita se voi suorittaa, työkalun lisäämisen avulla agentti voi nyt suorittaa monenlaisia toimintoja. Tässä luvussa tarkastelemme työkalun käyttö -suunnittelumallia, joka kuvaa, miten tekoälyagentit voivat käyttää tiettyjä työkaluja saavuttaakseen tavoitteensa.

## Johdanto

Tässä oppitunnissa pyrimme vastaamaan seuraaviin kysymyksiin:

- Mikä on työkalun käyttö -suunnittelumalli?
- Mihin käyttötapauksiin sitä voidaan soveltaa?
- Mitkä ovat tarvittavat elementit/rakennuspalikat suunnittelumallin toteuttamiseen?
- Mitkä ovat erityiset seikat, joita on otettava huomioon käytettäessä työkalun käyttö -suunnittelumallia luotettavien tekoälyagenttien rakentamisessa?

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

- Määritellä työkalun käyttö -suunnittelumalli ja sen tarkoitus.
- Tunnistaa käyttötapaukset, joissa työkalun käyttö -suunnittelumalli on sovellettavissa.
- Ymmärtää suunnittelumallin toteuttamiseen tarvittavat keskeiset elementit.
- Tunnistaa tekijät, jotka varmistavat tekoälyagenttien luotettavuuden käytettäessä tätä suunnittelumallia.

## Mikä on työkalun käyttö -suunnittelumalli?

**Työkalun käyttö -suunnittelumalli** keskittyy antamaan suurille kielimalleille (LLM) kyvyn olla vuorovaikutuksessa ulkoisten työkalujen kanssa tiettyjen tavoitteiden saavuttamiseksi. Työkalut ovat koodia, jota agentti voi suorittaa suorittaakseen toimintoja. Työkalu voi olla yksinkertainen funktio, kuten laskin, tai kolmannen osapuolen palveluun tehtävä API-kutsu, kuten osakekurssin haku tai sääennuste. Tekoälyagenttien kontekstissa työkalut on suunniteltu suoritettaviksi agenttien toimesta mallin generoimien toimintokutsujen perusteella.

## Mihin käyttötapauksiin sitä voidaan soveltaa?

Tekoälyagentit voivat hyödyntää työkaluja monimutkaisten tehtävien suorittamiseen, tiedon hakemiseen tai päätösten tekemiseen. Työkalun käyttö -suunnittelumallia käytetään usein tilanteissa, joissa tarvitaan dynaamista vuorovaikutusta ulkoisten järjestelmien, kuten tietokantojen, verkkopalveluiden tai koodin tulkintaohjelmien, kanssa. Tämä kyky hyödyttää monenlaisissa käyttötapauksissa, kuten:

- **Dynaaminen tiedonhaku:** Agentit voivat kysellä ulkoisia API-rajapintoja tai tietokantoja päivitetyn tiedon hakemiseksi (esim. SQLite-tietokannan kysely tietojen analysointiin, osakekurssien tai säätilan haku).
- **Koodin suoritus ja tulkinta:** Agentit voivat suorittaa koodia tai skriptejä ratkaistakseen matemaattisia ongelmia, laatia raportteja tai tehdä simulaatioita.
- **Työnkulun automatisointi:** Toistuvien tai monivaiheisten työnkulkujen automatisointi integroimalla työkaluja, kuten tehtäväajastimia, sähköpostipalveluita tai dataputkia.
- **Asiakastuki:** Agentit voivat olla vuorovaikutuksessa CRM-järjestelmien, tikettialustojen tai tietopohjien kanssa käyttäjäkyselyjen ratkaisemiseksi.
- **Sisällön luonti ja muokkaus:** Agentit voivat hyödyntää työkaluja, kuten kielioppitarkistimia, tekstin tiivistäjiä tai sisällön turvallisuuden arvioijia, avustaakseen sisällöntuotantotehtävissä.

## Mitkä ovat tarvittavat elementit/rakennuspalikat työkalun käyttö -suunnittelumallin toteuttamiseen?

Nämä rakennuspalikat mahdollistavat tekoälyagentin suorittaa monenlaisia tehtäviä. Tarkastellaan keskeisiä elementtejä työkalun käyttö -suunnittelumallin toteuttamiseksi:

- **Funktio-/työkalu-kaaviot:** Yksityiskohtaiset määritelmät saatavilla olevista työkaluista, mukaan lukien funktion nimi, tarkoitus, vaaditut parametrit ja odotetut tulokset. Nämä kaaviot auttavat LLM:ää ymmärtämään, mitä työkaluja on saatavilla ja miten muodostaa kelvollisia pyyntöjä.

- **Funktion suorituslogiikka:** Määrittää, miten ja milloin työkaluja kutsutaan käyttäjän aikomuksen ja keskustelukontekstin perusteella. Tämä voi sisältää suunnittelumoduuleita, reititysmekanismeja tai ehdollisia virtauksia, jotka määrittävät työkalujen käytön dynaamisesti.

- **Viestinkäsittelyjärjestelmä:** Komponentit, jotka hallinnoivat keskustelun kulkua käyttäjän syötteiden, LLM:n vastausten, työkalukutsujen ja työkalujen vastausten välillä.

- **Työkalujen integraatiokehys:** Infrastruktuuri, joka yhdistää agentin erilaisiin työkaluihin, olivatpa ne sitten yksinkertaisia funktioita tai monimutkaisia ulkoisia palveluita.

- **Virheenkäsittely ja validointi:** Mekanismit virheiden käsittelemiseksi työkalujen suorituksessa, parametrien validoimiseksi ja odottamattomien vastausten hallitsemiseksi.

- **Tilan hallinta:** Seuraa keskustelukontekstia, aiempia työkalujen vuorovaikutuksia ja pysyvää dataa varmistamaan johdonmukaisuuden usean vuoron aikana.

Seuraavaksi tarkastellaan funktioiden/työkalujen kutsumista tarkemmin.
 
### Funktion/työkalun kutsuminen

Funktion kutsuminen on ensisijainen tapa, jolla suurten kielimallien (LLM) annetaan olla vuorovaikutuksessa työkalujen kanssa. Usein termit 'funktio' ja 'työkalu' käytetään synonyymeinä, koska 'funktiot' (uudelleenkäytettävän koodin lohkot) ovat ne 'työkalut', joita agentit käyttävät tehtävien suorittamiseen. Jotta funktion koodi voidaan kutsua, LLM:n täytyy vertailla käyttäjän pyyntöä funktion kuvaukseen. Tätä varten LLM:lle lähetetään kaavio, joka sisältää kaikkien käytettävissä olevien funktioiden kuvaukset. LLM valitsee sitten tehtävään parhaiten sopivan funktion ja palauttaa sen nimen ja argumentit. Valittu funktio suoritetaan, sen vastaus lähetetään takaisin LLM:lle, joka käyttää tietoja vastatakseen käyttäjän pyyntöön.

Kehittäjien, jotka haluavat toteuttaa funktiokutsun agenteille, tulee hankkia:

1. LLM-malli, joka tukee funktiokutsua
2. Kaavio sisältäen funktioiden kuvaukset
3. Koodi kustakin kuvatusta funktiosta

Käytetään esimerkkinä ajan hakemista tietystä kaupungista:

1. **Alusta LLM, joka tukee funktiokutsua:**

    Kaikki mallit eivät tue funktiokutsua, joten on tärkeää varmistaa, että käyttämäsi LLM tukee sitä.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> tukee funktiokutsua. Voimme aloittaa käynnistämällä OpenAI-asiakkaan Azure OpenAI **Responses API**a vastaan (vakaa `/openai/v1/` päätepiste — `api_version` ei tarvita).

    ```python
    # Alusta OpenAI-asiakas Azure OpenAI:ta varten (Responses API, v1-päätepiste)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Luo funktiokaavio:**

    Määrittelemme seuraavaksi JSON-kaavion, joka sisältää funktion nimen, kuvauksen siitä, mitä funktio tekee, sekä funktioparametrien nimet ja kuvaukset.
    Lähetämme tämän kaavion aiemmin luodulle asiakkaalle yhdessä käyttäjän pyynnön kanssa San Franciscon ajankohdan löytämiseksi. On tärkeää huomata, että **työkalukutsu** on se, mitä palautetaan, **ei** lopullinen vastaus kysymykseen. Kuten aiemmin mainittiin, LLM palauttaa valitun funktion nimen ja sille välitettävät argumentit.

    ```python
    # Mallin luettavaksi tarkoitettu funktiokuvailu (Responses API:n litteä työkalumuoto)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # Alkuperäinen käyttäjän viesti
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Ensimmäinen API-kutsu: Pyydä mallia käyttämään toimintoa
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API palauttaa työkalukutsut function_call-kohteina response.outputissa.
    # Lisää ne keskusteluun, jotta mallilla on täydellinen konteksti seuraavassa vuorossa.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Tehtävän suorittamiseen tarvittava funktion koodi:**

    Nyt kun LLM on valinnut suoritettavan funktion, tehtävän suorittava koodi tulee toteuttaa ja suorittaa.
    Voimme toteuttaa ajan hakemiseen tarvittavan koodin Pythonilla. Meidän tulee myös kirjoittaa koodi, joka purkaa nimen ja argumentit response_message-viestistä saadaksemme lopputuloksen.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # Käsittele funktiokutsut
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Palauta työkalun tulos function_call_output-kohteena
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Toinen API-kutsu: Hae lopullinen vastaus mallilta
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Funktiokutsut ovat monien, elleivät kaikkien, agenttien työkalukäytön suunnittelun ytimessä, mutta niiden toteutus alusta alkaen voi joskus olla haastavaa.
Kuten opimme [Oppitunti 2:ssa](../../../02-explore-agentic-frameworks), agenttikehykset tarjoavat meille valmiita rakennuspalikoita työkalun käyttöön.
 
## Työkalun käyttö -esimerkkejä agenttikehyksillä

Tässä muutamia esimerkkejä siitä, kuinka voit toteuttaa työkalun käyttö -suunnittelumallin käyttämällä erilaisia agenttikehyksiä:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> on avoimen lähdekoodin tekoälykehys tekoälyagenttien rakentamiseen. Se yksinkertaistaa funktiokutsujen käyttöä antamalla sinun määritellä työkalut Python-funktioina `@tool`-koristelijan avulla. Kehys hoitaa mallin ja koodisi välisen vuorovaikutuksen. Se tarjoaa myös pääsyn valmiiksi rakennettuihin työkaluihin, kuten Tiedoston haku ja Koodin tulkitseminen, `FoundryChatClient`in kautta.

Seuraava kaavio havainnollistaa funktiokutsujen prosessia Microsoft Agent Frameworkissa:

![function calling](../../../translated_images/fi/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Frameworkissa työkalut määritellään korotettuina funktioina. Voimme muuntaa aiemmin näkemämme `get_current_time`-funktion työkaluksi käyttämällä `@tool`-koristelijaa. Kehys serialisoi automaattisesti funktion ja sen parametrit luodakseen kaavion, joka lähetetään LLM:lle.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Luo asiakas
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Luo agentti ja suorita työkalulla
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> on uudempi agenttikehys, joka on suunniteltu auttamaan kehittäjiä rakentamaan, käyttöönottoa ja skaalaamaan korkealaatuisia ja laajennettavia tekoälyagentteja turvallisesti ilman, että heidän tarvitsee hallita taustalla olevaa laskenta- ja tallennusresursseja. Se on erityisen hyödyllinen yrityssovelluksissa, koska se on täysin hallinnoitu palvelu, jossa on yritystason tietoturva.

Verrattuna suoraan LLM-rajapinnan käyttöön Microsoft Foundry Agent Service tarjoaa joitakin etuja, mukaan lukien:

- Automaattinen työkalukutsu – sinun ei tarvitse jäsentää työkalukutsua, suorittaa työkalua ja käsitellä vastausta; kaikki tämä tapahtuu nyt palvelinpuolella
- Turvallisesti hallinnoidut tiedot – keskustelutilan hallinnan sijaan voit luottaa threadien (keskusteluketjujen) tallentavan kaiken tarvitsemasi tiedon
- Valmiit työkalut – Työkaluja, joilla voit olla vuorovaikutuksessa tietolähteidesi kanssa, kuten Bing, Azure AI Search ja Azure Functions.

Microsoft Foundry Agent Servicen työkalut voidaan jakaa kahteen kategoriaan:

1. Tietotyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Perustaminen Bing-haun avulla</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Tiedoston haku</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Toimintotyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktiokutsut</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Koodin tulkitsin</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-määritellyt työkalut</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service mahdollistaa näiden työkalujen käytön yhdessä työkalusetin (`toolset`) muodossa. Se käyttää myös `threads`-ketjuja, jotka seuraavat tietyn keskustelun viestihistoriaa.

Kuvittele, että olet myyntiedustaja yrityksessä nimeltä Contoso. Haluat kehittää keskustelurobotin, joka pystyy vastaamaan myyntitietoihisi liittyviin kysymyksiin.

Seuraava kuva havainnollistaa, miten voisit käyttää Microsoft Foundry Agent Serviceä myyntitietojen analysointiin:

![Agenttinen palvelu käytössä](../../../translated_images/fi/agent-service-in-action.34fb465c9a84659e.webp)

Käyttääksesi mitä tahansa näistä työkaluista palvelun kanssa, voimme luoda asiakkaan ja määritellä työkalun tai työkalusetin. Toteuttaaksemme tämän käytännössä voimme käyttää seuraavaa Python-koodia. LLM pystyy tarkastelemaan työkalusettiä ja päättämään, käytetäänkö käyttäjän luomaa funktiota `fetch_sales_data_using_sqlite_query` vai valmista Koodin tulkitseminä, käyttäjän pyynnön mukaan.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query -funktio, joka löytyy fetch_sales_data_functions.py-tiedostosta.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Työkalupaketin alustus
toolset = ToolSet()

# Funktiokutsujen agentin alustus fetch_sales_data_using_sqlite_query-funktiolla ja sen lisääminen työkalupakettiin
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Kooditulkki-työkalun alustus ja lisääminen työkalupakettiin.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Mitkä ovat erityiset seikat, joita on otettava huomioon käytettäessä työkalun käyttö -suunnittelumallia luotettavien tekoälyagenttien rakentamisessa?

Yleinen huoli LLM:ien dynaamisesti generoiman SQL:n kanssa on tietoturva, erityisesti SQL-injektio tai haitalliset toimet, kuten tietokannan poistaminen tai manipulointi. Vaikka nämä huolet ovat perusteltuja, ne voidaan tehokkaasti estää konfiguroimalla tietokantakäyttöoikeudet oikein. Useimmissa tietokannoissa tämä tarkoittaa tietokannan asettamista vain luku -tilaan. PostgreSQL:n tai Azure SQL:n kaltaisissa tietokantapalveluissa sovellukselle tulisi antaa vain lukuoikeus (SELECT-rooli).

Sovelluksen suorittaminen turvallisessa ympäristössä lisää suojautumista entisestään. Yritysskenaarioissa data yleensä haetaan ja muunnetaan operatiivisista järjestelmistä vain luku -tietokantaan tai tietovarastoon, jossa on käyttäjäystävällinen kaavio. Tämä varmistaa, että data on turvallista, optimoitu suorituskyvyn ja saatavuuden kannalta, ja sovelluksella on rajoitettu, vain luku -pääsy.

## Esimerkkikoodit

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Onko sinulla lisää kysymyksiä työkalun käyttö -suunnittelumalleista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia tekoälyagentteihin liittyviin kysymyksiisi.

## Lisäresurssit

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service - Työpaja</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent -työpaja</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework - Yleiskatsaus</a>


## Tämän agentin pikakoe (valinnainen)

Kun olet oppinut ottamaan agenteja käyttöön [Luvussa 16](../16-deploying-scalable-agents/README.md), voit pikakokeilla tämän luvun `TravelToolAgent`-agenttia (kutsutaanko se edelleen työkalunsa ja vastaatko?) tiedostolla [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Katso ohjeet suoritukseen tiedostosta [`tests/README.md`](../tests/README.md).

## Edellinen luku

[Agenttimaisten suunnittelumallien ymmärtäminen](../03-agentic-design-patterns/README.md)

## Seuraava luku

[Agenttinen RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->