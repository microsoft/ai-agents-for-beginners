[![Kuinka suunnitella hyviä tekoälyagentteja](../../../translated_images/fi/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

# Työkalun käyttö -suunnittelumalli

Työkalut ovat kiinnostavia, koska ne antavat tekoälyagenteille laajemman valikoiman kykyjä. Sen sijaan, että agentilla olisi vain rajoitettu joukko toimintoja, joita se voi suorittaa, työkalun lisäämisen myötä agentti voi nyt tehdä monenlaisia toimia. Tässä luvussa tarkastelemme työkalun käyttö -suunnittelumallia, joka kuvaa, miten tekoälyagentit voivat käyttää erityisiä työkaluja tavoitteidensa saavuttamiseksi.

## Johdanto

Tässä oppitunnissa pyrimme vastaamaan seuraaviin kysymyksiin:

- Mikä on työkalun käyttö -suunnittelumalli?
- Mihin käyttötapauksiin sitä voidaan soveltaa?
- Mitkä ovat suunnittelumallin toteuttamiseen tarvittavat elementit/rakennuspalikat?
- Mitä erityisiä huomioita liittyy työkalun käyttö -suunnittelumallin käyttämiseen luotettavien tekoälyagenttien rakentamisessa?

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

- Määritellä työkalun käyttö -suunnittelumalli ja sen tarkoitus.
- Tunnistaa käyttötapaukset, joissa työkalun käyttö -suunnittelumalli soveltuu.
- Ymmärtää suunnittelumallin toteuttamisen tarvitseman keskeiset elementit.
- Tunnistaa näkökohdat, jotka varmistavat luotettavuuden tekoälyagénttien työkalukäytössä.

## Mikä on työkalun käyttö -suunnittelumalli?

**Työkalun käyttö -suunnittelumalli** keskittyy antamaan suurille kielimalleille (LLM) mahdollisuuden olla vuorovaikutuksessa ulkoisten työkalujen kanssa tiettyjen tavoitteiden saavuttamiseksi. Työkalut ovat koodia, jota agentti voi suorittaa tehdäkseen toimintoja. Työkalu voi olla yksinkertainen funktio, kuten laskin, tai kolmannen osapuolen rajapintakutsu, kuten osakekurssihakemisto tai säätiedotus. Tekoälyagenttien yhteydessä työkalut on suunniteltu agenttien suoritettaviksi mallin generoimien funktiokutsujen perusteella.

## Mihin käyttötapauksiin sitä voidaan soveltaa?

Tekoälyagentit voivat hyödyntää työkaluja suorittaakseen monimutkaisia tehtäviä, hakeakseen tietoa tai tehdäkseen päätöksiä. Työkalun käyttö -suunnittelumallia käytetään usein tilanteissa, joissa tarvitaan dynaamista vuorovaikutusta ulkoisten järjestelmien, kuten tietokantojen, verkkopalvelujen tai koodintulkkien kanssa. Tätä kykyä voidaan hyödyntää useissa eri käyttötapauksissa, kuten:

- **Dynaaminen tiedon haku:** Agentit voivat kysyä ulkoisilta rajapinnoilta tai tietokannoista ajantasaista tietoa (esim. kysely SQLite-tietokantaan tietoanalyysejä varten, osakekurssien tai säätietojen hakeminen).
- **Koodin suoritus ja tulkinta:** Agentit voivat ajaa koodia tai skriptejä ratkaistakseen matemaattisia ongelmia, generoida raportteja tai suorittaa simulointeja.
- **Työnkulun automaatio:** Toistuvien tai monivaiheisten työnkulkujen automatisointi integroimalla työkaluja, kuten tehtäväajastimia, sähköpostipalveluja tai datan putkia.
- **Asiakastuki:** Agentit voivat olla vuorovaikutuksessa CRM-järjestelmien, tikettipalveluiden tai tietopohjien kanssa vastatakseen käyttäjien kysymyksiin.
- **Sisällön luonti ja muokkaus:** Agentit voivat hyödyntää työkaluja, kuten kieliopin tarkistajia, tekstin tiivistäjiä tai sisällön turvallisuusarvioijia sisällöntuotannon tukena.

## Mitkä ovat työkalun käyttö -suunnittelumallin toteuttamiseen tarvittavat elementit/rakennuspalikat?

Nämä rakennuspalikat mahdollistavat tekoälyagentin suorittaa laajan joukon tehtäviä. Tarkastellaan keskeisiä elementtejä työkalun käyttö -suunnittelumallin toteuttamiseksi:

- **Funktio-/työkalumääritykset:** Tarkat määritelmät käytettävissä olevista työkaluista, mukaan lukien funktion nimi, tarkoitus, vaaditut parametrit ja odotetut tulosteet. Nämä määritykset mahdollistavat LLM:n ymmärtämään, mitä työkaluja on saatavilla ja miten rakentaa kelvollisia pyyntöjä.

- **Funktion suorituslogiikka:** Ohjaa, miten ja milloin työkaluja kutsutaan käyttäjän tarkoituksen ja keskustelukontekstin perusteella. Tämä voi sisältää suunnittelumoduuleja, reititysmenetelmiä tai ehdollisia kulkuja, jotka määrittävät työkalun käytön dynaamisesti.

- **Viestinkäsittelyjärjestelmä:** Komponentit, jotka hallinnoivat keskustelun kulkua käyttäjän syötteiden, LLM-vastausten, työkalukutsujen ja työkalun vastauksien välillä.

- **Työkalujen integrointikehys:** Infrastruktuuri, joka yhdistää agentin erilaisiin työkaluihin, olivatpa ne yksinkertaisia funktioita tai monimutkaisia ulkoisia palveluja.

- **Virheenkäsittely ja validointi:** Mekanismit työkalun suorituksen virheiden käsittelyyn, parametrien tarkastukseen ja odottamattomien vastausten hallintaan.

- **Tilanhallinta:** Seuraa keskustelukontekstia, aiempia työkalukäyttöjä ja pysyvää dataa varmistaen johdonmukaisuuden monivuorovaikutteisissa tilanteissa.

Seuraavaksi tarkastellaan funktio-/työkalukutsua tarkemmin.
 
### Funktio-/Työkalukutsu

Funktiokutsu on pääasiallinen tapa, jolla annamme suurille kielimalleille (LLM) mahdollisuuden olla vuorovaikutuksessa työkalujen kanssa. Näet usein 'funktion' ja 'työkalun' käytettävän vaihtokelpoisesti, koska 'funktiot' (uudelleenkäytettävän koodin lohkot) ovat työkaluja, joita agentit käyttävät tehtävien suorittamiseen. Jotta funktio voidaan kutsua, LLM:n on verrattava käyttäjän pyyntöä funktiokuvaukseen. Tätä varten LLM:lle lähetetään skeema, joka sisältää kaikkien saatavilla olevien funktioiden kuvaukset. LLM valitsee tehtävään sopivimman funktion ja palauttaa sen nimen ja argumentit. Valittu funktio suoritetaan, sen vastaus lähetetään takaisin LLM:lle, joka käyttää tietoa vastatakseen käyttäjän pyyntöön.

Kehittäjien täytyy toteuttaa funktiokutsut agenteille, ja tarvitset:

1. LLM-mallin, joka tukee funktiokutsuja
2. Skeeman, joka sisältää funktiokuvaukset
3. Koodin kutakin kuvattua funktiota varten

Käytetään esimerkkinä ajankohdan selvittämistä kaupungissa havainnollistamaan:

1. **Alusta funktioita tukevat LLM-mallit:**

    Kaikki mallit eivät tue funktiokutsuja, joten on tärkeää varmistaa, että käyttämäsi LLM tukee sitä.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> tukee funktiokutsuja. Aloitamme luomalla OpenAI-asiakkaan Azure OpenAI **Responses API**:ta vastaan (vakaa `/openai/v1/`-päätepiste – ei `api_version`-tarvetta). 

    ```python
    # Alusta OpenAI-asiakas Azure OpenAI:lle (Responses API, v1-päätepiste)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Luo funktioskeema:**

    Määrittelemme seuraavaksi JSON-skeeman, joka sisältää funktion nimen, kuvauksen siitä, mitä funktio tekee, ja funktion parametrien nimet ja kuvaukset.
    Käytämme sitten tätä skeemaa yhdessä käyttäjän pyynnön kanssa ajan hakemiseksi San Franciscosta. Tärkeää huomata, että palautettu arvo on **työkalukutsu**, **ei** lopullinen vastaus kysymykseen. Kuten aiemmin todettiin, LLM palauttaa valitsemiensa funktioiden nimet ja argumentit.

    ```python
    # Funktion kuvaukselle mallin luettavaksi (Vastaus-rajapinnan litteä työkalumuoto)
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

    # Ensimmäinen API-kutsu: Pyydä mallia käyttämään funktiota
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API palauttaa työkalukutsut function_call-kohteina response.outputissa.
    # Lisää ne keskusteluun, jotta mallilla on täydellinen konteksti seuraavalla kierroksella.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Funktiokoodi tehtävän suorittamiseksi:**

    Nyt kun LLM on valinnut suoritettavan funktion, toteutettava ja suoritettava koodi on kirjoitettava.
    Voimme toteuttaa koodin nykyisen ajan hakemiseksi Pythonilla. Meidän täytyy myös kirjoittaa koodi nimen ja argumenttien purkamiseen response_message-kohdasta lopullisen tuloksen saamiseksi.

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
    # Käsittele funktion kutsut
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Palauta työkalun tulos funktion_kutsu_tuloksena
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Toinen API-kutsu: Hanki malli lopullinen vastaus
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

Funktiokutsu on ydinasia useimmassa, ellei kaikessa agenttien työkalukäytössä, mutta sen toteuttaminen alusta alkaen voi olla toisinaan haastavaa.
Kuten opimme [Oppitunnissa 2](../../../02-explore-agentic-frameworks), agenttirungot tarjoavat meille valmiita rakennuspalikoita työkalujen käyttöön.
 
## Työkalun käyttö -esimerkkejä agenttirungoilla

Tässä on joitakin esimerkkejä työkalun käyttö -suunnittelumallin toteuttamisesta eri agenttirunkojen avulla:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> on avoimen lähdekoodin tekoälykehys tekoälyagenttien rakentamiseen. Se helpottaa funktiokutsujen käyttöä sallimalla työkalujen määrittelyn Python-funktioina `@tool`-koristelijalla. Kehys hoitaa mallin ja koodin välisen viestiliikenteen. Se tarjoaa myös pääsyn valmiisiin työkaluihin, kuten tiedostohakuun ja koodintulkkaukseen `FoundryChatClient`-rajapinnan kautta.

Seuraava kaavio havainnollistaa funktiokutsuprosessia Microsoft Agent Frameworkilla:

![funktion kutsu](../../../translated_images/fi/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Frameworkissa työkalut määritellään koristeltuina funktioina. Voimme muuttaa aiemmin näkemämme `get_current_time` -funktion työkaluksi käyttämällä `@tool`-koristelijaa. Kehys osaa automaattisesti seralisoida funktion ja sen parametrit, luoden skeeman, joka lähetetään LLM:lle.

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

# Luo agentti ja käytä työkalua
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> on uudempi agenttirunko, joka on suunniteltu auttamaan kehittäjiä rakentamaan turvallisesti skaalautuvia ja laajennettavia tekoälyagentteja hallitsematta alustan laskenta- ja tallennusresursseja. Se on erityisen hyödyllinen yrityssovelluksissa, sillä se on täysin hallittu palvelu, jossa on yritystason tietoturva.

Verrattuna suoraan LLM-API:n käyttöön Microsoft Foundry Agent Service tarjoaa etuja, kuten:

- Automaattinen työkalukutsujen hallinta – ei tarvitse käsitellä työkalukutsujen jäsentämistä, kutsua työkalua ja vastaanottaa vastauksia; kaikki tehdään palvelinpuolella
- Turvallisesti hallittu data – omasta keskustelutilasta ei tarvitse huolehtia, vaan tieto tallennetaan säikeisiin
- Valmiit välineet – työkaluja, joita voi käyttää vuorovaikutukseen datalähteiden kanssa, kuten Bing, Azure AI Search ja Azure Functions

Microsoft Foundry Agent Servicen työkalut voidaan jakaa kahteen kategoriaan:

1. Tietotyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing-hakuun perustuva tiedonhaku</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Tiedostohaku</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Toimintotyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktiokutsut</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Koodintulkki</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-määritellyt työkalut</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service mahdollistaa näiden työkalujen käytön yhdessä `toolset`-kokonaisuutena. Se käyttää myös `säikeitä` pitämään kirjaa tietyn keskustelun viestihistoriasta.

Kuvitellaan, että olet myyntiedustaja yrityksessä nimeltä Contoso. Haluat kehittää keskustelevaa agenttia, joka voi vastata kysymyksiin myyntidatastasi.

Seuraava kuva havainnollistaa, miten voisit käyttää Microsoft Foundry Agent Serviceä analysoimaan myyntidataa:

![Agent Service toiminnassa](../../../translated_images/fi/agent-service-in-action.34fb465c9a84659e.webp)

Käyttääksesi mitään näistä työkaluista palvelussa, voit luoda asiakkaan ja määritellä työkalun tai työkalusarjan. Käytännössä voimme toteuttaa tämän seuraavalla Python-koodilla. LLM pystyy tarkastelemaan työkalusarjaa ja päättämään, käytetäänkö käyttäjän luomaa funktiota `fetch_sales_data_using_sqlite_query` vai valmiina olevaa koodintulkkia käyttäjän pyynnön mukaan.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query-funktio, joka löytyy fetch_sales_data_functions.py-tiedostosta.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Työkalupaketin alustaminen
toolset = ToolSet()

# Funktion kutsumisen agentin alustaminen fetch_sales_data_using_sqlite_query-funktiolla ja lisääminen työkalupakettiin
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Koodintulkin työkalun alustaminen ja lisääminen työkalupakettiin.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Mitä erityisiä huomioita liittyy työkalun käyttö -suunnittelumallin käyttämiseen luotettavien tekoälyagenttien rakentamisessa?

Yksi yleinen huolenaihe SQL:n dynaamisesti generoinnissa LLM:ien avulla on tietoturva, erityisesti SQL-injektion riski tai haitalliset toimenpiteet, kuten tietokannan poistaminen tai käsittely. Vaikka nämä huolenaiheet ovat aiheellisia, ne voidaan tehokkaasti estää määrittelemällä tietokannan käyttöoikeudet oikein. Useimmissa tietokannoissa tämä tarkoittaa lukutilan (read-only) määrittelyä. Palveluissa kuten PostgreSQL tai Azure SQL sovellukselle tulee antaa lukuoikeudet (SELECT).

Sovelluksen ajaminen suojatussa ympäristössä lisää suojaa entisestään. Yritysskenaarioissa data yleensä siirretään ja muokataan operatiivisista järjestelmistä lukuoikeudella varustettuun tietokantaan tai tietovarastoon, jossa on käyttäjäystävällinen skeema. Tämä takaa datan turvallisuuden, suorituskyvyn ja saavutettavuuden, ja että sovellus pääsee vain rajoitettuun lukuoikeuteen.

## Näytekoodit

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Onko sinulla lisää kysymyksiä työkalun käyttö -suunnittelumallista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tutustuaksesi muihin oppijoihin, osallistuaksesi kyselytunteihin ja saadaksesi tekoälyagenttikysymyksiisi vastauksia.

## Lisäresurssit

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service -työpaja</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer -moniagenttityöpaja</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Frameworkin yleiskatsaus</a>


## Edellinen oppitunti

[Agenttimaisten suunnittelumallien ymmärtäminen](../03-agentic-design-patterns/README.md)

## Seuraava oppitunti

[Agenttinen RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->