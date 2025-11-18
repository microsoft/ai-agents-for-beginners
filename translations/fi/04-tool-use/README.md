<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T17:46:04+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "fi"
}
-->
[![Kuinka suunnitella hyviä tekoälyagentteja](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.fi.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

# Työkalujen käyttö -suunnittelumalli

Työkalut ovat mielenkiintoisia, koska ne mahdollistavat tekoälyagenttien laajemman toimintakyvyn. Sen sijaan, että agentilla olisi vain rajallinen joukko toimintoja, joita se voi suorittaa, työkalun lisääminen antaa agentille mahdollisuuden suorittaa monenlaisia toimintoja. Tässä luvussa tarkastelemme Työkalujen käyttö -suunnittelumallia, joka kuvaa, kuinka tekoälyagentit voivat käyttää tiettyjä työkaluja tavoitteidensa saavuttamiseksi.

## Johdanto

Tässä oppitunnissa pyrimme vastaamaan seuraaviin kysymyksiin:

- Mikä on työkalujen käyttö -suunnittelumalli?
- Mihin käyttötapauksiin sitä voidaan soveltaa?
- Mitkä ovat tarvittavat elementit/muodostavat osat suunnittelumallin toteuttamiseksi?
- Mitä erityisiä huomioita on otettava huomioon, kun käytetään Työkalujen käyttö -suunnittelumallia luotettavien tekoälyagenttien rakentamiseen?

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat:

- Määritellä Työkalujen käyttö -suunnittelumallin ja sen tarkoituksen.
- Tunnistaa käyttötapaukset, joissa Työkalujen käyttö -suunnittelumalli on sovellettavissa.
- Ymmärtää keskeiset elementit, jotka tarvitaan suunnittelumallin toteuttamiseen.
- Tunnistaa huomioita, jotka varmistavat tekoälyagenttien luotettavuuden tätä suunnittelumallia käytettäessä.

## Mikä on Työkalujen käyttö -suunnittelumalli?

**Työkalujen käyttö -suunnittelumalli** keskittyy antamaan LLM:ille kyvyn olla vuorovaikutuksessa ulkoisten työkalujen kanssa saavuttaakseen tiettyjä tavoitteita. Työkalut ovat koodia, jonka agentti voi suorittaa toimintoja varten. Työkalu voi olla yksinkertainen funktio, kuten laskin, tai API-kutsu kolmannen osapuolen palveluun, kuten osakekurssien haku tai säätiedot. Tekoälyagenttien yhteydessä työkalut on suunniteltu suoritettaviksi agenttien toimesta vastauksena **mallin tuottamiin funktiokutsuihin**.

## Mihin käyttötapauksiin sitä voidaan soveltaa?

Tekoälyagentit voivat hyödyntää työkaluja monimutkaisten tehtävien suorittamiseen, tiedon hakemiseen tai päätöksentekoon. Työkalujen käyttö -suunnittelumallia käytetään usein tilanteissa, joissa tarvitaan dynaamista vuorovaikutusta ulkoisten järjestelmien, kuten tietokantojen, verkkopalveluiden tai koodintulkitsijoiden kanssa. Tämä kyky on hyödyllinen monissa eri käyttötapauksissa, kuten:

- **Dynaaminen tiedonhaku:** Agentit voivat kysyä ulkoisia API:ita tai tietokantoja saadakseen ajankohtaista tietoa (esim. kysely SQLite-tietokannasta data-analyysia varten, osakekurssien tai säätietojen haku).
- **Koodin suoritus ja tulkinta:** Agentit voivat suorittaa koodia tai skriptejä ratkaistakseen matemaattisia ongelmia, luodakseen raportteja tai suorittaakseen simulaatioita.
- **Työnkulun automatisointi:** Toistuvien tai monivaiheisten työnkulkujen automatisointi integroimalla työkaluja, kuten tehtäväajastimia, sähköpostipalveluita tai dataputkia.
- **Asiakastuki:** Agentit voivat olla vuorovaikutuksessa CRM-järjestelmien, tikettialustojen tai tietokantojen kanssa ratkaistakseen käyttäjien kyselyitä.
- **Sisällön luominen ja muokkaus:** Agentit voivat hyödyntää työkaluja, kuten kielioppitarkistimia, tekstin tiivistäjiä tai sisällön turvallisuusarvioijia, avustaakseen sisällön luomistehtävissä.

## Mitkä ovat tarvittavat elementit/muodostavat osat työkalujen käyttö -suunnittelumallin toteuttamiseksi?

Nämä elementit mahdollistavat tekoälyagentin suorittaa monenlaisia tehtäviä. Tarkastellaan keskeisiä elementtejä, jotka tarvitaan Työkalujen käyttö -suunnittelumallin toteuttamiseen:

- **Funktio-/työkaluskeemat:** Saatavilla olevien työkalujen yksityiskohtaiset määritelmät, mukaan lukien funktion nimi, tarkoitus, vaaditut parametrit ja odotetut tulokset. Nämä skeemat mahdollistavat LLM:n ymmärtää, mitkä työkalut ovat käytettävissä ja kuinka rakentaa kelvollisia pyyntöjä.

- **Funktioiden suorituslogiikka:** Määrittää, miten ja milloin työkaluja kutsutaan käyttäjän tarkoituksen ja keskustelukontekstin perusteella. Tämä voi sisältää suunnittelumoduuleja, reititysmekanismeja tai ehdollisia virtauksia, jotka määrittävät työkalujen käytön dynaamisesti.

- **Viestien käsittelyjärjestelmä:** Komponentit, jotka hallitsevat keskustelun kulkua käyttäjän syötteiden, LLM:n vastausten, työkalukutsujen ja työkalutulosten välillä.

- **Työkalujen integrointikehys:** Infrastruktuuri, joka yhdistää agentin erilaisiin työkaluihin, olivatpa ne yksinkertaisia funktioita tai monimutkaisia ulkoisia palveluita.

- **Virheenkäsittely ja validointi:** Mekanismit työkalujen suoritusvirheiden käsittelyyn, parametrien validointiin ja odottamattomien vastausten hallintaan.

- **Tilanhallinta:** Seuraa keskustelukontekstia, aiempia työkaluvuorovaikutuksia ja pysyvää dataa varmistaakseen johdonmukaisuuden monivaiheisissa vuorovaikutuksissa.

Seuraavaksi tarkastellaan funktio-/työkalukutsuja tarkemmin.

### Funktio-/työkalukutsut

Funktiokutsut ovat ensisijainen tapa, jolla mahdollistamme Suurten Kielimallien (LLM) vuorovaikutuksen työkalujen kanssa. Usein näet 'Funktio' ja 'Työkalu' käytettävän keskenään, koska 'funktiot' (uudelleenkäytettävän koodin lohkot) ovat 'työkaluja', joita agentit käyttävät tehtävien suorittamiseen. Jotta funktion koodi voidaan kutsua, LLM:n täytyy verrata käyttäjän pyyntöä funktion kuvaukseen. Tätä varten LLM:lle lähetetään skeema, joka sisältää kaikkien saatavilla olevien funktioiden kuvaukset. LLM valitsee tehtävään sopivimman funktion ja palauttaa sen nimen ja argumentit. Valittu funktio kutsutaan, sen vastaus lähetetään takaisin LLM:lle, joka käyttää tietoa vastatakseen käyttäjän pyyntöön.

Jotta kehittäjät voivat toteuttaa funktiokutsuja agenteille, tarvitset:

1. LLM-mallin, joka tukee funktiokutsuja
2. Skeeman, joka sisältää funktioiden kuvaukset
3. Koodin jokaiselle kuvatulle funktiolle

Käytetään esimerkkinä ajan hakemista kaupungissa:

1. **Alusta LLM, joka tukee funktiokutsuja:**

    Kaikki mallit eivät tue funktiokutsuja, joten on tärkeää varmistaa, että käyttämäsi LLM tukee niitä. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> tukee funktiokutsuja. Voimme aloittaa Azure OpenAI -asiakkaan alustamisella.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Luo funktioskeema:**

    Seuraavaksi määrittelemme JSON-skeeman, joka sisältää funktion nimen, kuvauksen siitä, mitä funktio tekee, sekä funktion parametrien nimet ja kuvaukset. Tämän skeeman avulla voimme välittää sen aiemmin luodulle asiakkaalle yhdessä käyttäjän pyynnön kanssa löytää aika San Franciscossa. On tärkeää huomata, että palautettu **työkalukutsu** ei ole lopullinen vastaus kysymykseen. Kuten aiemmin mainittiin, LLM palauttaa funktion nimen, jonka se valitsi tehtävään, ja argumentit, jotka sille välitetään.

    ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Funktiokoodi, joka tarvitaan tehtävän suorittamiseen:**

    Nyt kun LLM on valinnut, mikä funktio täytyy suorittaa, tehtävän suorittamiseen tarvittava koodi täytyy toteuttaa ja suorittaa. Voimme toteuttaa koodin nykyisen ajan hakemiseksi Pythonilla. Meidän täytyy myös kirjoittaa koodi, joka poimii nimen ja argumentit response_message:sta saadaksemme lopullisen tuloksen.

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
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Funktiokutsut ovat keskeinen osa useimpia, ellei kaikkia agenttien työkalujen käyttöön liittyviä suunnitelmia, mutta niiden toteuttaminen alusta alkaen voi joskus olla haastavaa. Kuten opimme [Oppitunnissa 2](../../../02-explore-agentic-frameworks), agenttikehykset tarjoavat meille valmiita rakennuspalikoita työkalujen käytön toteuttamiseen.

## Työkalujen käyttöesimerkkejä agenttikehysten avulla

Tässä on joitakin esimerkkejä siitä, kuinka voit toteuttaa Työkalujen käyttö -suunnittelumallin eri agenttikehysten avulla:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> on avoimen lähdekoodin tekoälykehys .NET-, Python- ja Java-kehittäjille, jotka työskentelevät Suurten Kielimallien (LLM) kanssa. Se yksinkertaistaa funktiokutsujen käyttöä kuvaamalla automaattisesti funktiosi ja niiden parametrit mallille prosessin kautta, jota kutsutaan <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialisoinniksi</a>. Se myös hallitsee edestakaista viestintää mallin ja koodisi välillä. Toinen etu agenttikehyksen, kuten Semantic Kernelin, käytössä on, että se mahdollistaa pääsyn valmiisiin työkaluihin, kuten <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Tiedostohaku</a> ja <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Koodintulkitsija</a>.

Seuraava kaavio havainnollistaa funktiokutsujen prosessia Semantic Kernelin avulla:

![funktiokutsut](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.fi.png)

Semantic Kernelissä funktioita/työkaluja kutsutaan <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugineiksi</a>. Voimme muuntaa aiemmin näkemämme `get_current_time`-funktion pluginiksi muuttamalla sen luokaksi, jossa funktio sijaitsee. Voimme myös tuoda `kernel_function`-koristelijan, joka ottaa funktion kuvauksen. Kun sitten luot kernelin GetCurrentTimePluginin kanssa, kernel serialisoi automaattisesti funktion ja sen parametrit, luoden skeeman lähetettäväksi LLM:lle prosessin aikana.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> on uudempi agenttikehys, joka on suunniteltu auttamaan kehittäjiä rakentamaan, ottamaan käyttöön ja skaalaamaan korkealaatuisia ja laajennettavia tekoälyagentteja turvallisesti ilman, että heidän tarvitsee hallita taustalla olevia laskenta- ja tallennusresursseja. Se on erityisen hyödyllinen yrityssovelluksissa, koska se on täysin hallinnoitu palvelu yritystason turvallisuudella.

Kun verrataan suoraan LLM API:n kanssa kehittämiseen, Azure AI Agent Service tarjoaa joitakin etuja, kuten:

- Automaattinen työkalukutsu – ei tarvitse käsitellä työkalukutsua, kutsua työkalua ja käsitellä vastausta; kaikki tämä tehdään nyt palvelinpuolella
- Turvallisesti hallittu data – sen sijaan, että hallitsisit omaa keskustelutilaa, voit luottaa säikeisiin tallentaaksesi kaiken tarvitsemasi tiedon
- Valmiit työkalut – Työkalut, joita voit käyttää vuorovaikutukseen datalähteidesi kanssa, kuten Bing, Azure AI Search ja Azure Functions.

Azure AI Agent Servicen saatavilla olevat työkalut voidaan jakaa kahteen kategoriaan:

1. Tietotyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing-haun avulla tehtävä pohjustus</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Tiedostohaku</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Toimintatyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktiokutsut</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Koodintulkitsija</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-määritellyt työkalut</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service mahdollistaa näiden työkalujen käytön yhdessä `toolset`-kokonaisuutena. Se hyödyntää myös `threads`-säikeitä, jotka pitävät kirjaa tietyn keskustelun viestihistoriasta.

Kuvittele, että olet myyntiedustaja yrityksessä nimeltä Contoso. Haluat kehittää keskusteluagentin, joka voi vastata kysymyksiin myyntidatastasi.

Seuraava kuva havainnollistaa, kuinka voisit käyttää Azure AI Agent Servicea analysoidaksesi myyntidatasi:

![Agenttikehys toiminnassa](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.fi.jpg)

Jotta voisit käyttää mitä tahansa näistä työkaluista palvelun kanssa, voit luoda asiakkaan ja määritellä työkalun tai työkalukokonaisuuden. Käytännön toteutuksessa voimme käyttää seuraavaa Python-koodia. LLM pystyy tarkastelemaan työkalukokonaisuutta ja päättämään, käyttääkö se käyttäjän luomaa funktiota, `fetch_sales_data_using_sqlite_query`, vai valmiiksi rakennettua Koodintulkitsijaa käyttäjän pyynnön mukaan.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Mitä erityisiä huomioita on otettava huomioon, kun käytetään Työkalujen käyttö -suunnittelumallia luotettavien tekoälyagenttien rakentamiseen?

Yleinen huoli LLM:ien dynaamisesti generoimassa SQL:ssä on turvallisuus, erityisesti SQL-injektion tai haitallisten toimien, kuten tietokannan pudottamisen tai manipuloinnin, riski. Vaikka nämä huolet ovat perusteltuja, ne voidaan tehokkaasti lieventää määrittämällä tietokannan käyttöoikeudet asianmukaisesti. Useimmille tietokannoille tämä tarkoittaa tietokannan määrittämistä vain lukuoikeudella. Tietokantapalveluissa, kuten PostgreSQL tai Azure SQL, sovellukselle tulisi antaa vain lukuoikeus (SELECT-rooli).
Sovelluksen suorittaminen turvallisessa ympäristössä parantaa suojaa entisestään. Yritysympäristöissä data yleensä kerätään ja muokataan operatiivisista järjestelmistä vain luku -tietokantaan tai tietovarastoon, jossa on käyttäjäystävällinen skeema. Tämä lähestymistapa varmistaa, että data on turvallista, optimoitu suorituskyvyn ja käytettävyyden kannalta, ja että sovelluksella on rajoitettu, vain luku -pääsy.

## Esimerkkikoodit

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Onko sinulla lisää kysymyksiä työkalujen käyttöön liittyvistä suunnittelumalleista?

Liity [Azure AI Foundry Discordiin](https://aka.ms/ai-agents/discord) tapaamaan muita oppijoita, osallistumaan toimistotunteihin ja saamaan vastauksia AI Agents -kysymyksiisi.

## Lisäresurssit

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Edellinen oppitunti

[Agentic Design Patterns - Ymmärtäminen](../03-agentic-design-patterns/README.md)

## Seuraava oppitunti

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->