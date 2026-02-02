[![Miten suunnitella hyviä AI-agentteja](../../../translated_images/fi/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Napsauta yllä olevaa kuvaa nähdäksesi opetuksen videon)_

# Työkalujen käyttöön perustuva suunnittelumalli

Työkalut ovat kiinnostavia, koska ne antavat AI-agenteille laajemman valikoiman toimintoja. Sen sijaan, että agentilla olisi rajallinen joukko suoritettavia toimintoja, työkalun lisäämällä agentti voi nyt suorittaa monenlaisia toimintoja. Tässä luvussa tarkastelemme työkalujen käyttöön perustuvaa suunnittelumallia, joka kuvaa, miten AI-agentit voivat käyttää tiettyjä työkaluja tavoitteidensa saavuttamiseksi.

## Johdanto

Tässä oppitunnissa pyrimme vastaamaan seuraaviin kysymyksiin:

- Mikä on työkalujen käyttöön perustuva suunnittelumalli?
- Missä käyttötapauksissa sitä voidaan soveltaa?
- Mitkä ovat sen toteuttamiseen tarvittavat osatekijät/rakennuspalikat?
- Mitä erityisiä huomioita tulee ottaa huomioon rakentaessa luotettavia AI-agentteja tämän suunnittelumallin avulla?

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

- Määritellä työkalujen käyttöön perustuvan suunnittelumallin ja sen tarkoituksen.
- Tunnistaa käyttötapaukset, joissa työkalujen käyttöön perustuva suunnittelumalli soveltuu.
- Ymmärtää suunnittelumallin keskeiset toteuttamiseen tarvittavat elementit.
- Tunnistaa luotettavuuteen liittyvät näkökohdat tämän suunnittelumallin käyttämisessä AI-agenteissa.

## Mikä on työkalujen käyttöön perustuva suunnittelumalli?

**Työkalujen käyttöön perustuva suunnittelumalli** keskittyy antamaan suurille kielimalleille (LLM) kyvyn olla vuorovaikutuksessa ulkoisten työkalujen kanssa tiettyjen tavoitteiden saavuttamiseksi. Työkalut ovat koodia, jota agentti voi suorittaa toimintojen toteuttamiseksi. Työkalu voi olla yksinkertainen funktio, kuten laskin, tai API-kutsu kolmannen osapuolen palveluun, kuten osakekurssin tarkistus tai sääennuste. AI-agenttien kontekstissa työkalut on suunniteltu suoritettavaksi agenttien toimesta mallin generoimien funktiokutsujen vastauksena.

## Missä käyttötapauksissa sitä voidaan soveltaa?

AI-agentit voivat hyödyntää työkaluja monimutkaisten tehtävien suorittamiseen, tiedon hakemiseen tai päätöksentekoon. Työkalujen käyttöön perustuva suunnittelumalli soveltuu tilanteisiin, joissa vaaditaan dynaamista vuorovaikutusta ulkoisten järjestelmien kanssa, kuten tietokantojen, verkkopalveluiden tai koodin tulkkien kanssa. Tämä kyky on hyödyllinen monissa eri käyttötapauksissa, mukaan lukien:

- **Dynaaminen tiedonhaku:** Agentit voivat kysyä ulkoisia API-rajapintoja tai tietokantoja saadakseen ajantasaista dataa (esim. SQLite-tietokannan kysely data-analyysia varten, osakekurssien tai säätietojen hakeminen).
- **Koodin suoritus ja tulkkaus:** Agentit voivat suorittaa koodia tai skriptejä ratkaistakseen matemaattisia ongelmia, luodakseen raportteja tai suorittaakseen simulaatioita.
- **Työnkulun automatisointi:** Toistuvien tai monivaiheisten työnkulkujen automatisointi integroimalla työkaluja kuten tehtävien ajastimet, sähköpostipalvelut tai dataputket.
- **Asiakastuki:** Agentit voivat olla vuorovaikutuksessa CRM-järjestelmien, lippujärjestelmien tai tietopohjien kanssa ratkaistakseen käyttäjän kyselyt.
- **Sisällön luonti ja muokkaus:** Agentit voivat hyödyntää työkaluja kuten kielioppitarkistimia, tekstin tiivistäjiä tai sisällön turvallisuusarvioijia sisällöntuotantotehtävissä.

## Mitkä ovat työkalujen käyttöön perustuvan suunnittelumallin toteuttamisen osatekijät/rakennuspalikat?

Nämä rakennuspalikat mahdollistavat AI-agentille monipuolisten tehtävien suorittamisen. Tarkastellaan työkalujen käyttöön perustuvan suunnittelumallin toteuttamiseen tarvittavia keskeisiä elementtejä:

- **Funktio-/työkaluskeemat**: Tarkat määritelmät saatavilla olevista työkaluista, mukaan lukien funktion nimi, tarkoitus, vaaditut parametrit ja odotetut tulokset. Nämä skeemat auttavat LLM:ää ymmärtämään, mitä työkaluja on tarjolla ja miten muodostaa validit pyynnöt.

- **Funktion suorituslogiikka**: Säätelee, miten ja milloin työkaluja kutsutaan käyttäjän aikomuksen ja keskustelukontekstin perusteella. Tämä voi sisältää suunnittelumoduuleja, reititysmekanismeja tai ehtolauseita, jotka määrittävät työkalujen käytön dynaamisesti.

- **Viestinkäsittelyjärjestelmä**: Komponentit, jotka hallinnoivat keskustelun kulkua käyttäjän syötteiden, LLM:n vastausten, työkalukutsujen ja työkaluvastausten välillä.

- **Työkalujen integrointikehys**: Infrastruktuuri, joka yhdistää agentin erilaisiin työkaluihin, oli kyseessä sitten yksinkertaiset funktiot tai monimutkaiset ulkoiset palvelut.

- **Virheenkäsittely ja validointi**: Mekanismit, jotka käsittelevät virheitä työkalujen suorittamisessa, validoivat parametreja ja hallinnoivat odottamattomia vastauksia.

- **Tilanhallinta**: Seuraa keskustelukontekstia, aiempia työkalukuvauksia ja pysyviä tietoja varmistaakseen johdonmukaisuuden monivaiheisissa keskusteluissa.

Seuraavaksi tarkastelemme funktio-/työkalukutsua tarkemmin.

### Funktio-/työkalukutsu

Funktiokutsu on tärkein tapa, jolla suuret kielimallit (LLM) voivat olla vuorovaikutuksessa työkalujen kanssa. Usein 'Funktio' ja 'Työkalu' termejä käytetään vaihdellen, koska 'funktiot' (uudelleen käytettävän koodin osat) ovat työkaluja, joita agentit käyttävät tehtävien suorittamiseen. Jotta funktion koodi voidaan kutsua, LLM:n täytyy verrata käyttäjän pyyntöä funktion kuvaukseen. Tätä varten skeema, joka sisältää kaikkien saatavilla olevien funktioiden kuvaukset, lähetetään LLM:lle. LLM valitsee sitten sopivimman funktion tehtävään ja palauttaa sen nimen ja argumentit. Valittu funktio kutsutaan, sen vastaus lähetetään takaisin LLM:lle, joka käyttää tietoa vastatakseen käyttäjän pyyntöön.

Kehittäjien on toteuttaakseen funktiokutsun agenteille tarpeen:

1. LLM-malli, joka tukee funktiokutsuja
2. Skeema, joka sisältää funktioiden kuvaukset
3. Koodi kutakin kuvattua funktiota varten

Käytetään esimerkkinä nykyisen ajan hakemista kaupungista:

1. **Alusta LLM, joka tukee funktiokutsuja:**

    Kaikki mallit eivät tue funktiokutsuja, joten on tärkeää varmistaa, että käyttämäsi LLM tukee niitä. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> tukee funktiokutsuja. Voimme aloittaa Azure OpenAI -asiakkaan luomisella.

    ```python
    # Alusta Azure OpenAI -asiakas
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **Luo funktioskeema:**

    Määrittelemme JSON-skeeman, joka sisältää funktion nimen, kuvauksen siitä, mitä funktio tekee, sekä funktion parametrien nimet ja kuvaukset.
    Lähetämme tämän skeeman aiemmin luodulle asiakkaalle yhdessä käyttäjän pyynnön kanssa, jossa pyydetään aikaa San Franciscosta. On tärkeää huomata, että palautetaan **työkalukutsu**, **ei** lopullinen vastaus kysymykseen. Kuten aiemmin mainittiin, LLM palauttaa valitsemansa funktion nimen sekä sille annettavat argumentit.

    ```python
    # Funktiokuvauksen lukemista varten mallille
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
  
    # Alkuperäinen käyttäjän viesti
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Ensimmäinen API-kutsu: Pyydä mallia käyttämään funktiota
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Käsittele mallin vastaus
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
3. **Tehtävän suorittava funktiokoodi:**

    Kun LLM on valinnut suorittavan funktion, tarvitsemme koodin, joka toteuttaa tehtävän.
    Voimme toteuttaa nykyisen ajan hakemisen Pythonilla. Lisäksi kirjoitamme koodin, joka poimii nimen ja argumentit response_message-vastauksesta saadakseen lopullisen tuloksen.

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
     # Käsittele funktiokutsuja
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
  
      # Toinen API-kutsu: Hanki malli lopullinen vastaus
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

Funktiokutsu on useimpien, ellei kaikkien, agenttien työkalujen käytön suunnittelun ytimessä, mutta sen toteuttaminen alusta asti voi olla haastavaa.
Kuten opimme [Oppitunnissa 2](../../../02-explore-agentic-frameworks), agenttirajapinnat tarjoavat valmiita rakennuspalikoita työkalujen käyttöön.

## Työkalujen käyttöön liittyviä esimerkkejä agenttirajapintojen kanssa

Tässä on joitakin esimerkkejä siitä, miten voit toteuttaa työkalujen käyttöön perustuvan suunnittelumallin eri agenttirajapintojen avulla:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> on avoimen lähdekoodin AI-kehys .NET-, Python- ja Java-kehittäjille, jotka työskentelevät suurten kielimallien kanssa. Se yksinkertaistaa funktiokutsujen käyttöä kuvaamalla automaattisesti funktiot ja niiden parametrit mallille serialisointiprosessin avulla (<a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialisointi</a>). Lisäksi se hoitaa vuoropuhelun mallin ja koodisi välillä. Toinen etu semanttisen kernelin kaltaisen agenttirajapinnan käytössä on mahdollisuus hyödyntää valmiita työkaluja, kuten <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Tiedostohaku</a> ja <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Koodin tulkki</a>.

Seuraava kaavio havainnollistaa funktiokutsun prosessin Semantic Kernelissä:

![funktiokutsu](../../../translated_images/fi/functioncalling-diagram.a84006fc287f6014.webp)

Semantic Kernelissä funktioita/työkaluja kutsutaan <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Lisäosiksi</a>. Voimme muuntaa aiemmin näkemiämme `get_current_time` -funktion lisäosaksi muuttamalla sen luokaksi, jossa funktio sijaitsee. Voimme myös tuoda `kernel_function`-koristelijan, joka saa funktion kuvauksen. Kun sitten luomme kernelin GetCurrentTimePluginilla, kernel serialisoi automaattisesti funktion ja sen parametrit, luoden skeeman, joka lähetetään LLM:lle.

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

# Luo ydin
kernel = Kernel()

# Luo lisäosa
get_current_time_plugin = GetCurrentTimePlugin(location)

# Lisää lisäosa ytimeen
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> on uudempi agenttirajapinta, joka on suunniteltu antamaan kehittäjille mahdollisuus turvallisesti rakentaa, ottaa käyttöön ja skaalata korkealaatuisia ja laajennettavia AI-agentteja ilman, että heidän tarvitsee hallita taustalla olevaa laskenta- tai tallennusresursseja. Se on erityisen hyödyllinen yrityssovelluksissa, koska se on täysin hallittu palvelu yritystason turvallisuudella.

Verrattuna suoraan LLM-rajapinnan käyttöön, Azure AI Agent Service tarjoaa joitakin etuja, kuten:

- Automaattinen työkalukutsu – ei tarvitse itse jäsentää työkalukutsua, kutsua työkalua ja käsitellä vastausta; kaikki tapahtuu nyt palvelinpuolella
- Turvallisesti hallittu data – oman keskustelutilan hallinnan sijaan voit luottaa ketjuihin (threads), jotka tallentavat kaiken tarvitsemasi tiedon
- Valmiit työkalut – Työkaluja, joilla voit olla vuorovaikutuksessa datalähteidesi kanssa, kuten Bing, Azure AI Search ja Azure Functions.

Azure AI Agent Servicen työkalut voidaan jakaa kahteen kategoriaan:

1. Tietotyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Perustaminen Bing-haun avulla</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Tiedostohaku</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Toimintatyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktiokutsu</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Koodin tulkki</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-määritellyt työkalut</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service antaa meille mahdollisuuden käyttää näitä työkaluja yhdessä `toolset`:inä. Se käyttää myös `threads`-ketjuja, jotka seuraavat tietyn keskustelun viestihistoriaa.

Kuvitellaan, että olet myyntiedustaja yrityksessä nimeltä Contoso. Haluat kehittää keskustelevaa agenttia, joka voi vastata myyntitietoihisi liittyviin kysymyksiin.

Seuraava kuva havainnollistaa, miten voisit käyttää Azure AI Agent Serviceä analysoidaksesi myyntitietojasi:

![Agent Service toiminnassa](../../../translated_images/fi/agent-service-in-action.34fb465c9a84659e.webp)

Käyttääksesi mitä tahansa näistä työkaluista palvelun kanssa voimme luoda asiakkaan ja määritellä työkalun tai työkalusarjan. Käytännössä voimme toteuttaa tämän Python-koodilla. LLM pystyy tarkastelemaan työkalusarjaa ja päättämään, käytetäänkö käyttäjän luomaa funktiota `fetch_sales_data_using_sqlite_query` vai valmista Koodin tulkkia käyttäjän pyynnön mukaan.

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

# Työkalusarjan alustaminen
toolset = ToolSet()

# Funktiokutsujan alustaminen fetch_sales_data_using_sqlite_query-funktion avulla ja lisääminen työkalusarjaan
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Koodin tulkki -työkalun alustaminen ja lisääminen työkalusarjaan.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Mitä erityisiä huomioita tulee ottaa työkalujen käyttöön perustuvan suunnittelumallin käyttämisessä luotettavien AI-agenttien rakentamiseen?

Yleinen huoli LLM:ien dynaamisesti generoiman SQL:n kanssa on turvallisuus, erityisesti SQL-injektiohyökkäysten tai haitallisten toimien vaara, kuten tietokannan poistaminen tai muokkaaminen. Vaikka nämä huolet ovat perusteltuja, ne voidaan tehokkaasti lieventää oikeilla tietokantaoikeuksien asetuksilla. Useimmissa tietokannoissa tähän kuuluu tietokannan määrittäminen vain luku -tilaan. Tietokantapalveluissa kuten PostgreSQL tai Azure SQL sovellukselle tulisi antaa vain lukuoikeudet (SELECT-rooli).
Sovelluksen suorittaminen turvallisessa ympäristössä parantaa suojaa entisestään. Yritysympäristöissä tiedot otetaan tyypillisesti operatiivisista järjestelmistä ja muunnetaan lukutilassa olevaan tietokantaan tai tietovarastoon käyttäjäystävällisen skeeman kanssa. Tämä lähestymistapa varmistaa, että tiedot ovat turvassa, optimoitu suorituskyvyn ja saavutettavuuden kannalta, ja että sovelluksella on rajoitettu, vain luku -pääsy.

## Esimerkkikoodit

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Onko sinulla lisää kysymyksiä työkalun käytön suunnittelumalleista?

Liity [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) -kanavalle tapaamaan muita oppijoita, osallistumaan toimistoaikoihin ja saamaan vastauksia AI Agentteihin liittyviin kysymyksiisi.

## Lisäresurssit

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Edellinen oppitunti

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Seuraava oppitunti

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja omalla kielellään on hallitseva lähde. Tärkeiden tietojen osalta suositellaan ammattilaisen tekemää käännöstä. Emme vastaa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->