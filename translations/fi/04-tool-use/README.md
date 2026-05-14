[![Kuinka suunnitella hyviä tekoälyagentteja](../../../translated_images/fi/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Napsauta yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Työkalujen käyttö -suunnittelumalli

Työkalut ovat mielenkiintoisia, koska ne antavat tekoälyagenteille laajemman valikoiman kykyjä. Sen sijaan, että agentilla olisi rajoitettu joukko toimintoja, joita se voi suorittaa, työkalun lisäämällä agentti voi nyt suorittaa monenlaisia toimintoja. Tässä luvussa tarkastelemme Työkalujen käyttö -suunnittelumallia, joka kuvaa, kuinka tekoälyagentit voivat käyttää tiettyjä työkaluja tavoitteidensa saavuttamiseksi.

## Johdanto

Tässä oppitunnissa pyrimme vastaamaan seuraaviin kysymyksiin:

- Mitä on työkalujen käyttö -suunnittelumalli?
- Mille käyttötapauksille sitä voidaan soveltaa?
- Mitkä ovat suunnittelumallin toteuttamiseen tarvittavat elementit/rakennuspalikat?
- Mitkä ovat erityishuomiot, kun käytetään Työkalujen käyttö -suunnittelumallia luottamuksellisten tekoälyagenttien rakentamiseen?

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat:

- Määritellä Työkalujen käyttö -suunnittelumallin ja sen tarkoituksen.
- Tunnistaa käyttötapaukset, joissa Työkalujen käyttö -suunnittelumalli on sovellettavissa.
- Ymmärtää keskeiset elementit suunnittelumallin toteuttamiseksi.
- Tunnistaa huomiot luottamuksellisuuden varmistamiseksi tämän suunnittelumallin avulla rakennetuissa tekoälyagenteissa.

## Mitä on Työkalujen käyttö -suunnittelumalli?

**Työkalujen käyttö -suunnittelumalli** keskittyy siihen, että LLM:t pystyvät vuorovaikuttamaan ulkoisten työkalujen kanssa tiettyjen tavoitteiden saavuttamiseksi. Työkalut ovat koodia, jota agentti voi suorittaa tehtävien toteuttamiseksi. Työkalu voi olla yksinkertainen toiminto, kuten laskin, tai kolmannen osapuolen palvelua kutsuva rajapinta, kuten osakekurssihaku tai sääennuste. Tekoälyagenttien kontekstissa työkalut on suunniteltu suoritettaviksi agenttien toimesta mallin generoimien toimintakutsujen perusteella.

## Mille käyttötapauksille sitä voidaan soveltaa?

Tekoälyagentit voivat hyödyntää työkaluja monimutkaisten tehtävien suorittamiseen, tiedon hakemiseen tai päätösten tekemiseen. Työkalujen käyttö -suunnittelumallia käytetään usein tilanteissa, joissa tarvitaan dynaamista vuorovaikutusta ulkoisten järjestelmien, kuten tietokantojen, web-palveluiden tai koodin tulkitsijoiden kanssa. Tämä kyky on hyödyllinen monissa käyttötapauksissa, muun muassa:

- **Dynaaminen tiedonhaku:** Agentit voivat kysyä ulkoisista rajapinnoista tai tietokannoista saadakseen ajantasaisia tietoja (esim. SQLite-tietokannan tietojen kysely analyysiä varten, osakekurssien tai säätietojen hakeminen).
- **Koodin suoritus ja tulkinta:** Agentit voivat suorittaa koodia tai skriptejä matemaattisten ongelmien ratkaisemiseksi, raporttien luomiseksi tai simulointien suorittamiseksi.
- **Työnkulkujen automaatio:** Toistuvien tai monivaiheisten työnkulkujen automatisointi integroitujen työkalujen, kuten tehtäväaikatauluttimien, sähköpostipalveluiden tai datavirtojen avulla.
- **Asiakastuki:** Agentit voivat olla vuorovaikutuksessa CRM-järjestelmien, tikettialustojen tai tietopankkien kanssa käyttäjäkyselyiden ratkaisemiseksi.
- **Sisällön luonti ja muokkaus:** Agentit voivat hyödyntää työkaluja, kuten kieliopin tarkistajia, tekstin tiivistäjiä tai sisällön turvallisuusarvioijia, sisällöntuotannon avuksi.

## Mitkä ovat suunnittelumallin toteuttamiseen tarvittavat elementit/rakennuspalikat?

Nämä rakennuspalikat mahdollistavat tekoälyagentin suorittaa monenlaisia tehtäviä. Tarkastellaan keskeisiä elementtejä Työkalujen käyttö -suunnittelumallin toteuttamiseksi:

- **Toiminto-/työkaluskeemat**: Yksityiskohtaiset määritelmät käytettävissä olevista työkaluista, mukaan lukien toiminnon nimi, tarkoitus, vaaditut parametrit ja odotetut tulokset. Nämä skeemat auttavat LLM:ää ymmärtämään, mitä työkaluja on saatavilla ja miten muodostaa päteviä pyyntöjä.

- **Toiminnon suorituslogiikka**: Sääntelee miten ja milloin työkaluja kutsutaan käyttäjän aikomuksen ja keskustelukontekstin perusteella. Tämä voi sisältää suunnittelumoduuleja, reititysmekanismeja tai ehdollisia kulkuja, jotka määrittävät työkalujen käytön dynaamisesti.

- **Viestien käsittelyjärjestelmä**: Komponentit, jotka hallinnoivat keskustelun kulkua käyttäjän syötteiden, LLM:n vastausten, työkalukutsujen ja työkalujen vastausten välillä.

- **Työkalun integrointikehys**: Infrastruktuuri, joka yhdistää agentin erilaisiin työkaluihin, olivatpa ne yksinkertaisia toimintoja tai monimutkaisia ulkoisia palveluita.

- **Virheiden käsittely ja validointi**: Mekanismit työkalujen suorituksen epäonnistumisten käsittelyyn, parametrien validointiin ja odottamattomien vastausten hallintaan.

- **Tilanhallinta**: Seuraa keskustelukontekstia, aiempia työkalujen käyttötapahtumia ja pysyviä tietoja, jotta monivaiheiset keskustelut pysyvät johdonmukaisina.

Seuraavaksi tarkastelemme Toimintojen/työkalujen kutsumista tarkemmin.

### Toimintojen/työkalujen kutsuminen

Toimintojen kutsuminen on ensisijainen tapa, jolla mahdollistamme Large Language Modelsin (LLM) vuorovaikutuksen työkalujen kanssa. Usein 'Toiminto' ja 'Työkalu' termejä käytetään toistensa synonyymeina, koska 'toiminnot' (uudelleenkäytettävän koodin lohkot) ovat 'työkaluja', joita agentit käyttävät tehtävien suorittamiseen. Jotta toiminnon koodi voidaan kutsua, LLM:n täytyy verrata käyttäjän pyyntöä toimintojen kuvaukseen. Tätä varten LLM:lle lähetetään skeema, joka sisältää kaikkien käytettävissä olevien toimintojen kuvaukset. LLM valitsee tehtävään sopivimman toiminnon ja palauttaa sen nimen ja argumentit. Valittu toiminto kutsutaan, sen vastaus lähetetään takaisin LLM:lle, joka käyttää tietoa vastatakseen käyttäjän pyyntöön.

Kehittäjien tulee varmistaa seuraavat asiat toteuttaakseen toimintojen kutsumisen agenteille:

1. LLM-malli, joka tukee toimintojen kutsumista
2. Skeema, joka sisältää toimintojen kuvaukset
3. Koodi kullekin kuvatulle toiminnolle

Käytetään esimerkkinä nykyisen ajan hakemista kaupungista:

1. **Alusta toimintojen kutsumista tukeva LLM:**

    Kaikki mallit eivät tue toimintojen kutsumista, joten on tärkeää tarkistaa, että käyttämäsi LLM tukee sitä. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> tukee toimintojen kutsumista. Voimme aloittaa Azure OpenAI -asiakkaan käynnistyksellä.

    ```python
    # Alusta Azure OpenAI -asiakas
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Luo toimintojen skeema**:

    Määrittelemme seuraavaksi JSON-skeeman, joka sisältää toiminnon nimen, kuvauksen siitä, mitä toiminto tekee, sekä toiminnon parametrien nimet ja kuvaukset.
    Lähetämme tämän skeeman aiemmin luodulle asiakkaalle yhdessä käyttäjän pyynnön kanssa etsiä kelloajan San Franciscosta. Tärkeää on huomata, että **työkalukutsu** on se, mikä palautetaan, **ei** lopullinen vastaus kysymykseen. Kuten aiemmin todettiin, LLM palauttaa valitsemaansa toiminnon nimen ja sille välitettävät argumentit.

    ```python
    # Mallin lukemista varten tarkoitettu funktiokuvaus
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
  
1. **Tehtävän suorittava toiminnon koodi:**

    Nyt kun LLM on valinnut, mikä toiminto suoritetaan, tehtävän suorittava koodi tulee toteuttaa ja suorittaa.
    Voimme toteuttaa nykyisen ajan hakemisen Pythonilla. Meidän täytyy myös kirjoittaa koodi, joka purkaa nimen ja argumentit response_message -viestistä saadaksemme lopullisen tuloksen.

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
  
      # Toinen API-kutsu: Hanki lopullinen vastaus mallilta
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

Toimintojen kutsuminen on keskeinen osa useimpia, ellei kaikkia agenttien työkalujen käyttöön suunniteltuja toimintoja, mutta sen toteuttaminen alusta asti voi joskus olla haastavaa.
Kuten opimme [Oppitunnissa 2](../../../02-explore-agentic-frameworks) agenttipohjaiset kehykset tarjoavat valmiita rakennuspalikoita työkalujen käytön toteuttamiseen.

## Työkalujen käyttö -esimerkkejä agenttipohjaisilla kehyksillä

Tässä on joitakin esimerkkejä siitä, kuinka voit toteuttaa Työkalujen käyttö -suunnittelumallin eri agenttipohjaisten kehysten avulla:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> on avoimen lähdekoodin tekoälykehys tekoälyagenttien rakentamiseen. Se yksinkertaistaa toimintojen kutsumisen prosessia sallimalla työkalujen määrittelemisen Python-funktioina, joissa on `@tool`-koristelija. Kehys hoitaa mallin ja koodisi välisen viestinnän. Se tarjoaa myös pääsyn valmiisiin työkaluihin, kuten Tiedostohakuun ja Kooditulkkaukseen, `AzureAIProjectAgentProviderin` kautta.

Seuraava kaavio havainnollistaa toimintojen kutsumista Microsoft Agent Frameworkissa:

![function calling](../../../translated_images/fi/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Frameworkissa työkalut määritellään koristeltuina funktioina. Voimme muuttaa aiemmin katsomamme `get_current_time` -funktion työkaluksi käyttämällä `@tool` -koristelijaa. Kehys serialisoi automaattisesti funktion ja sen parametrit luoden skeeman, joka lähetetään LLM:lle.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Luo asiakas
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Luo agentti ja suorita työkaluilla
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> on uudempia agenttipohjaisia kehyksiä, joka on suunniteltu antamaan kehittäjille mahdollisuus turvallisesti rakentaa, ottaa käyttöön ja skaalata korkealaatuisia ja laajennettavia tekoälyagentteja ilman, että heidän tarvitsee hallita taustalla olevaa laskenta- ja tallennusresursseja. Se on erityisen hyödyllinen yrityssovelluksissa, koska kyseessä on täysin hallittu palvelu yritystason tietoturvalla.

Suoraan LLM-rajapintaa kehittämiseen verrattuna Azure AI Agent Service tarjoaa etuja, kuten:

- Automaattinen työkalukutsujen hallinta – työkalukutsun jäsentelyä, työkalun kutsumista ja vastauksen käsittelyä ei tarvitse tehdä itse; kaikki tapahtuu palvelinpuolella
- Turvallisesti hallinnoitu data – sen sijaan, että hallinnoisit omaa keskustelutilaa, voit luottaa ketjuihin, jotka säilyttävät kaiken tarvitsemasi tiedon
- Valmiit työkalut – työkaluja, joilla voi olla vuorovaikutusta datalähteisiisi, kuten Bing, Azure AI Search ja Azure Functions.

Azure AI Agent Servicen työkalut voidaan jakaa kahteen kategoriaan:

1. Tietotyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing-haun käyttöön perustaminen</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Tiedostohaku</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Toimintatyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Toimintojen kutsuminen</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Koodin tulkki</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-määritteiset työkalut</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agenttipalvelu mahdollistaa näiden työkalujen käytön yhdessä `toolset` -kokoelmana. Se hyödyntää myös `threads` -ketjuja, jotka seuraavat tietyn keskustelun viestihistoriaa.

Kuvittele, että olet myyntiedustaja yrityksessä nimeltä Contoso. Haluat kehittää keskusteluagentin, joka osaa vastata kysymyksiin myyntidatastasi.

Seuraava kuva havainnollistaa, miten voisit käyttää Azure AI Agent Serviceä myyntidatasi analysoimiseksi:

![Agentic Service In Action](../../../translated_images/fi/agent-service-in-action.34fb465c9a84659e.webp)

Voit käyttää mitä tahansa näistä työkaluista palvelun kanssa luomalla asiakkaan ja määrittelemällä työkalun tai työkalukokoelman. Käytännön toteutukseen voimme käyttää seuraavaa Python-koodia. LLM pystyy tarkastelemaan työkalukokoelmaa ja päättämään, käyttääkö käyttäjän luomaa funktiota `fetch_sales_data_using_sqlite_query` vai valmista Koodin tulkkia käyttäjän pyynnöstä riippuen.

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

# Toimintokutsuvahdin alustaminen fetch_sales_data_using_sqlite_query-funktiolla ja lisääminen työkalupakettiin
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Kooditulkki-työkalun alustaminen ja lisääminen työkalupakettiin.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Mitä erityishuomioita Työkalujen käyttö -suunnittelumallin kanssa on luottamuksellisten tekoälyagenttien rakentamisessa?

Yleinen huolenaihe dynaamisesti LLM:ien generoimissa SQL-kyselyissä liittyy tietoturvaan, erityisesti SQL-injektioihin tai haitallisiin toimiin, kuten tietokannan pudottamiseen tai vahingoittamiseen. Vaikka nämä huolet ovat perusteltuja, ne voidaan tehokkaasti estää konfiguroimalla tietokannan käyttöoikeudet oikein. Useimmissa tietokannoissa tämä tarkoittaa tietokannan määrittämistä vain luku -tilaan. PostgreSQL- tai Azure SQL -tietokantapalveluissa sovellukselle tulisi määrittää vain luku (SELECT) -rooli.

Sovelluksen ajaminen turvallisessa ympäristössä parantaa suojaa entisestään. Yritysskenaarioissa data yleensä haetaan ja muunnetaan operatiivisista järjestelmistä vain luku -tietokanta- tai tietovarastomuotoon, jossa on käyttäjäystävällinen skeema. Tämä lähestymistapa varmistaa datan turvallisuuden, suorituskyvyn ja saavutettavuuden optimoinnin sekä sovelluksen rajoitetun, vain luku -pääsyn.

## Esimerkkikoodit

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Lisää kysymyksiä Työkalujen käyttö -suunnittelumalleista?

Liity [Microsoft Foundry Discord -palveluun](https://aka.ms/ai-agents/discord) tapaamaan muita oppijoita, osallistumaan työaikoihin ja saamaan vastauksia tekoälyagentteihin liittyviin kysymyksiisi.

## Lisäresurssit

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Moni-agenttityöpaja</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework - Yleiskatsaus</a>

## Edellinen oppitunti

[Agenttipohjaisten suunnittelumallien ymmärtäminen](../03-agentic-design-patterns/README.md)

## Seuraava oppitunti
[Agenttinen RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->