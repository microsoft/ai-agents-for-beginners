[![How to Design Good AI Agents](../../../translated_images/fi/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Napsauta yllä olevaa kuvaa katsellaksesi tämän oppitunnin videota)_

# Työkalujen Käyttömalli

Työkalut ovat mielenkiintoisia, koska ne antavat tekoälyagenttien laajemmat toimintamahdollisuudet. Sen sijaan, että agentilla olisi rajoitettu joukko toimintoja, joita se voi suorittaa, työkalun lisäämällä agentti voi nyt suorittaa laajan valikoiman toimintoja. Tässä luvussa tarkastelemme työkalujen käyttömallia, joka kuvaa, miten tekoälyagentit voivat käyttää tiettyjä työkaluja tavoitteidensa saavuttamiseksi.

## Johdanto

Tässä oppitunnissa haluamme vastata seuraaviin kysymyksiin:

- Mikä on työkalujen käyttömalli?
- Mihin käyttötapauksiin sitä voidaan soveltaa?
- Mitkä ovat mallin toteuttamiseen tarvittavat elementit/rakennuspalikat?
- Mitkä ovat erityiset huomioitavat asiat työkalujen käyttömallin hyödyntämisessä luotettavien tekoälyagenttien rakentamisessa?

## Oppimistavoitteet

Tämän oppitunnin suorittamisen jälkeen osaat:

- Määritellä työkalujen käyttömallin ja sen tarkoituksen.
- Tunnistaa käyttötapaukset, joissa työkalujen käyttömalli on sovellettavissa.
- Ymmärtää keskeiset elementit, joita tarvitaan mallin toteuttamiseen.
- Tunnistaa huomioitavat asiat tekoälyagenttien luotettavuuden varmistamiseksi tämän mallin käytössä.

## Mikä on työkalujen käyttömalli?

**Työkalujen käyttömalli** keskittyy antamaan suurille kielimalleille (LLM) kyvyn olla vuorovaikutuksessa ulkoisten työkalujen kanssa tiettyjen tavoitteiden saavuttamiseksi. Työkalut ovat koodia, jota agentti voi suorittaa toimintojen tekemiseksi. Työkalu voi olla yksinkertainen funktio kuten laskin, tai API-kutsu kolmannen osapuolen palveluun, kuten osakekurssisovellukseen tai sääennusteeseen. Tekoälyagenttien yhteydessä työkalut on suunniteltu suoritettavaksi agenttien toimesta mallin generoimiin funktiokutsuihin vastauksena.

## Mihin käyttötapauksiin sitä voidaan soveltaa?

Tekoälyagentit voivat hyödyntää työkaluja suorittaakseen monimutkaisia tehtäviä, hakemaan tietoa tai tekemään päätöksiä. Työkalujen käyttömallia käytetään usein tilanteissa, joissa tarvitaan dynaamista vuorovaikutusta ulkoisten järjestelmien, kuten tietokantojen, verkkopalveluiden tai koodin tulkkien kanssa. Tämä kyky on hyödyllinen monissa eri käyttötapauksissa, mukaan lukien:

- **Dynaaminen tiedonhaku:** Agentit voivat kysyä ulkoisia API:ita tai tietokantoja saadakseen ajantasaista dataa (esim. kysely SQLite-tietokannasta analyysiin, osakekurssien tai säätietojen hakeminen).
- **Koodin suoritus ja tulkinta:** Agentit voivat suorittaa koodia tai skriptejä ratkaistakseen matemaattisia ongelmia, tuottaakseen raportteja tai suorittaakseen simulaatioita.
- **Työnkulun automaatio:** Toistuvien tai monivaiheisten työnkulkujen automatisointi yhdistämällä työkaluja kuten tehtäväajoittimia, sähköpostipalveluita tai datan putkia.
- **Asiakaspalvelu:** Agentit voivat olla vuorovaikutuksessa CRM-järjestelmien, tikettipalveluiden tai tietokantojen kanssa ratkaistakseen käyttäjien kyselyn.
- **Sisällöntuotanto ja muokkaus:** Agentit voivat käyttää työkaluja kuten kielioppintarkistajia, tekstin tiivistäjiä tai sisältöturvallisuuden arvioijia auttaakseen sisällöntuotannossa.

## Mitkä ovat mallin toteuttamiseen tarvittavat elementit/rakennuspalikat?

Nämä rakennuspalikat mahdollistavat tekoälyagentille monenlaisten tehtävien suorittamisen. Tarkastellaan keskeisiä elementtejä työkalujen käyttömallin toteuttamiseksi:

- **Funktio-/työkaluskeemat:** Yksityiskohtaiset määritelmät saatavilla olevista työkaluista, mukaan lukien funktion nimi, tarkoitus, vaaditut parametrit ja odotetut tulokset. Nämä skeemat mahdollistavat LLM:n ymmärtää, mitä työkaluja on käytettävissä ja miten muodostaa voimassa olevat pyynnöt.

- **Funktion suorituslogiikka:** Määrittelee miten ja milloin työkaluja kutsutaan käyttäjän tarkoituksen ja keskustelun kontekstin perusteella. Tämä voi sisältää suunnittelijamoduuleja, reititysmekanismeja tai ehdollisia kulkuja, jotka määrittävät työkalujen käytön dynaamisesti.

- **Viestinkäsittelyjärjestelmä:** Osat, jotka hallitsevat keskustelun kulkua käyttäjän syötteiden, LLM-vastausten, työkalukutsujen ja työkalutulosten välillä.

- **Työkalujen integrointikehys:** Infrastruktuuri, joka yhdistää agentin erilaisiin työkaluihin, olivatpa ne yksinkertaisia funktioita tai monimutkaisia ulkoisia palveluita.

- **Virheenkäsittely ja validointi:** Mekanismit, joilla käsitellään työkalujen suorituksen epäonnistumiset, validoidaan parametrit ja hallitaan odottamattomat vastaukset.

- **Tilan hallinta:** Seuraa keskustelun kontekstia, aiempia työkalun käyttäjiä ja pysyvää dataa varmistaakseen johdonmukaisuuden monikertaisissa keskusteluissa.

Seuraavaksi tarkastelemme funktio-/työkalukutsua tarkemmin.

### Funktio-/työkalukutsu

Funktiokutsu on ensisijainen tapa, jolla sallimme suurten kielimallien (LLM) olla vuorovaikutuksessa työkalujen kanssa. Termit 'funktio' ja 'työkalu' käytetään usein vaihdellen, koska 'funktiot' (uudelleenkäytettävän koodin osat) ovat ne 'työkalut', joita agentit käyttävät suorittaakseen tehtäviä. Jotta funktion koodi voidaan kutsua, LLM:n tulee verrata käyttäjän pyyntöä funktion kuvaukseen. Tätä varten LLM:lle lähetetään skeema, joka sisältää kaikkien käytettävissä olevien funktioiden kuvaukset. LLM valitsee tehtävään sopivimman funktion ja palauttaa sen nimen sekä argumentit. Valittu funktio suoritetaan, sen vastaus lähetetään takaisin LLM:lle, joka käyttää tietoa vastatakseen käyttäjän pyyntöön.

Kehittäjien tarvitsee toteuttaakseen funktiokutsun agenteille seuraavat asiat:

1. LLM-malli, joka tukee funktiokutsuja
2. Skeema, joka sisältää funktiokuvaukset
3. Jokaisen kuvattavan funktion koodi

Käytetään esimerkkinä kaupungin nykyisen ajan hakemista:

1. **Alusta LLM, joka tukee funktiokutsua:**

    Kaikki mallit eivät tue funktiokutsua, joten on tärkeää varmistaa käyttämäsi LLM:n tuki. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> tukee funktiokutsua. Voimme aloittaa käynnistämällä Azure OpenAI -asiakkaan.

    ```python
    # Alusta Azure OpenAI -asiakas
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **Luo funktioskeema:**

    Seuraavaksi määrittelemme JSON-skeeman, joka sisältää funktion nimen, kuvauksen siitä mitä funktio tekee ja funktioparametrien nimet ja kuvaukset.
    Lähetämme tämän skeeman aiemmin luodulle asiakkaalle yhdessä käyttäjän pyynnön kanssa hakemaan aikaa San Franciscosta. Tärkeää huomata on, että palautettavana on **työkalukutsu**, **ei** lopullinen vastaus kysymykseen. Kuten aiemmin mainittu, LLM palauttaa tehtävään valitun funktion nimen ja argumentit.

    ```python
    # Funktion kuvaus mallin lukemista varten
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
  
    # Alkuperäinen käyttäjäviesti
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
  
3. **Funktiokoodi tehtävän suorittamiseksi:**

    Nyt kun LLM on valinnut suoritettavan funktion, on toteutettava ja suoritettava tehtävän suorittava koodi.
    Voimme toteuttaa ajan hakemisen Pythonilla. Meidän tulee myös kirjoittaa koodi, joka purkaa nimen ja argumentit response_message-viestistä saadaksemme lopputuloksen.

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

Funktiokutsu on monien, ellei kaikkien, agenttityökalujen käyttömallien ytimessä, mutta sen toteuttaminen alusta voi joskus olla haastavaa.
Kuten opimme [Oppitunnissa 2](../../../02-explore-agentic-frameworks) agentti-kehykset tarjoavat valmiita rakennuspalikoita työkalujen käyttöön.

## Työkalujen Käyttö Esimerkkejä Agentti-kehyksillä

Tässä on muutamia esimerkkejä, miten voit toteuttaa työkalujen käyttömallin eri agentti-kehyksillä:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> on avoimen lähdekoodin tekoälykehys tekoälyagenttien rakentamiseen. Se yksinkertaistaa funktiokutsun käyttöä antamalla sinun määritellä työkalut Python-funktioina, joissa käytetään `@tool`-koristelua. Kehys hoitaa mallin ja koodin välisen vuorovaikutuksen. Se tarjoaa myös pääsyn valmiisiin työkaluihin kuten tiedostohakuun ja koodin tulkkiin `AzureAIProjectAgentProvider`-luokan kautta.

Seuraava kuvio havainnollistaa funktiokutsun prosessia Microsoft Agent Frameworkilla:

![function calling](../../../translated_images/fi/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Frameworkissa työkalut määritellään koristelluiksi funktioiksi. Voimme muuttaa aikaisemmin näkemämme `get_current_time`-funktion työkaluksi käyttämällä `@tool`-koristelua. Kehys sarjoittaa automaattisesti funktion ja sen parametrit, luoden skeeman lähetettäväksi LLM:lle.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> on uudempi agenttikehys, joka on suunniteltu mahdollistamaan kehittäjille turvallinen, skaalautuva ja laajennettava tekoälyagenttien rakentaminen ilman tarvetta hallita taustalla olevaa laskenta- tai tallennusresurssia. Se on erityisen hyödyllinen yrityssovelluksissa, koska se on täysin hallittu palvelu yritystason tietoturvalla.

Suoraan LLM-rajapinnan käyttöön verrattuna Azure AI Agent Service tarjoaa etuja, kuten:

- Automaattinen työkalukutsun hallinta – ei tarvitse purkaa työkalukutsua, suorittaa työkalua ja käsitellä vastausta; kaikki tämä tapahtuu palvelinpuolella
- Turvallisesti hallittu data – keskustelutilaa ei tarvitse hallita itse, vaan säikeet tallentavat kaiken tarvittavan tiedon
- Valmiit työkalut – Työkaluja, joilla voi olla vuorovaikutusta datalähteisiin, kuten Bing, Azure AI Search ja Azure Functions.

Azure AI Agent Servicen työkalut jaetaan kahteen kategoriaan:

1. Tietotyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing-hakukytkentä</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Tiedostohaku</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Toimintatyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktiokutsu</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Koodin tulkki</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-määritellyt työkalut</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agenttipalvelu mahdollistaa näiden työkalujen käytön yhdessä `toolset`-kokonaisuutena. Lisäksi käytössä ovat `threads`-säikeet, jotka pitävät kirjaa tietyn keskustelun viesteistä.

Kuvittele, että olet myyntiedustaja yrityksessä nimeltä Contoso. Haluat kehittää keskustelevaa agenttia, joka voi vastata myyntitietoihin liittyviin kysymyksiin.

Seuraava kuva havainnollistaa, miten voit käyttää Azure AI Agent Serviceä analysoidaksesi myyntidataa:

![Agentic Service In Action](../../../translated_images/fi/agent-service-in-action.34fb465c9a84659e.webp)

Käyttääksesi mitä tahansa näistä työkaluista palvelun kanssa voit luoda asiakkaan ja määritellä työkalun tai työkaluvalikoiman. Käytännön toteutukseen voimme käyttää seuraavaa Python-koodia. LLM pystyy katsomaan työkalusettiä ja päättämään, käytetäänkö käyttäjän määrittelemää funktiota `fetch_sales_data_using_sqlite_query` tai valmiiksi rakennettua Koodin tulkkia käyttäjän pyynnön mukaan.

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

# Työkalupaketin alustaminen
toolset = ToolSet()

# Toiminnon kutsumisen agentin alustaminen fetch_sales_data_using_sqlite_query -toiminnolla ja lisääminen työkalupakettiin
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Koodin tulkitsemistyökalun alustaminen ja lisääminen työkalupakettiin.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Mitkä ovat erityiset huomioitavat asiat työkalujen käyttömallin hyödyntämisessä luotettavien tekoälyagenttien rakentamisessa?

SQL-kyselyiden dynaaminen generointi LLM:llä aiheuttaa usein huolta tietoturvasta, erityisesti SQL-injektion riski tai vahingolliset toimet kuten tietokannan pudottaminen tai muokkaaminen. Vaikka nämä huolenaiheet ovatkin aiheellisia, niitä voidaan tehokkaasti ehkäistä konfiguroimalla tietokannan käyttöoikeudet oikein. Useimmissa tietokannoissa tämä tarkoittaa tietokannan asettamista vain luku -tilaan. Tietokantapalveluissa kuten PostgreSQL tai Azure SQL sovellukselle tulisi antaa vain lukuoikeudet (SELECT-rooli).

Sovelluksen ajaminen turvallisessa ympäristössä parantaa suojaa entisestään. Yrityskäytössä data tyypillisesti haetaan ja muunnetaan operatiivisista järjestelmistä vain luku -tilassa olevaan tietokantaan tai tietovarastoon, jossa on käyttäjäystävällinen skeema. Tämä takaa datan turvallisuuden, suorituskyvyn ja saavutettavuuden optimoinnin sekä rajoitetun lukuoikeuden sovellukselle.

## Esimerkkikoodit

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Lisää kysymyksiä työkalujen käyttömallista?

Liity [Microsoft Foundry Discordiin](https://aka.ms/ai-agents/discord) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia AI Agents -kysymyksiisi.

## Lisäresurssit

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service työpaja</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework yleiskatsaus</a>

## Edellinen oppitunti

[Agenttisuunnittelumallien ymmärtäminen](../03-agentic-design-patterns/README.md)

## Seuraava oppitunti
[Agenttinen RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, on hyvä huomioida, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulisi pitää oikeana ja sitovana lähteenä. Keskeisissä tiedoissa suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa mahdollisista väärinymmärryksistä tai virhetulkintojen seurauksista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->