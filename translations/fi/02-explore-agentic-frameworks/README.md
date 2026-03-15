[![Tutustu tekoälyagenttikehyksiin](../../../translated_images/fi/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Napsauta yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Tutustu tekoälyagenttikehyksiin

Tekoälyagenttikehykset ovat ohjelmistoalustoja, jotka on suunniteltu yksinkertaistamaan tekoälyagenttien luomista, käyttöönottoa ja hallintaa. Nämä kehykset tarjoavat kehittäjille valmiita komponentteja, abstraktioita ja työkaluja, jotka sujuvoittavat monimutkaisten tekoälyjärjestelmien kehitystä.

Nämä kehykset auttavat kehittäjiä keskittymään sovellustensa ainutlaatuisiin puoliin tarjoamalla standardoituja lähestymistapoja yleisiin haasteisiin tekoälyagenttien kehityksessä. Ne parantavat skaalautuvuutta, saavutettavuutta ja tehokkuutta tekoälyjärjestelmien rakentamisessa.

## Johdanto 

Tässä oppitunnissa käsitellään:

- Mitä tekoälyagenttikehykset ovat ja mitä ne mahdollistavat kehittäjille?
- Miten tiimit voivat käyttää näitä nopeasti prototypointiin, iterointiin ja agentin kyvykkyyksien parantamiseen?
- Mitkä ovat erot Microsoftin luomien kehysten ja työkalujen välillä (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> ja <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Voinko integroida olemassa olevat Azure-ekosysteemin työkaluni suoraan, vai tarvitaanko erillisiä ratkaisuja?
- Mikä on Azure AI Agents -palvelu ja miten se auttaa minua?

## Oppimistavoitteet

Tämän oppitunnin tavoitteena on auttaa sinua ymmärtämään:

- Tekoälyagenttikehysten rooli tekoälyn kehityksessä.
- Kuinka hyödyntää tekoälyagenttikehyksiä älykkäiden agenttien rakentamisessa.
- Tekoälyagenttikehysten mahdollistamat keskeiset kyvykkyydet.
- Erot Microsoft Agent Frameworkin ja Azure AI Agent Servicen välillä.

## Mitä tekoälyagenttikehykset ovat ja mitä ne mahdollistavat kehittäjille?

Perinteiset tekoälykehykset voivat auttaa sinua integroimaan tekoälyä sovelluksiisi ja parantamaan näitä sovelluksia seuraavilla tavoilla:

- **Personalisointi**: Tekoäly voi analysoida käyttäjän käyttäytymistä ja mieltymyksiä tarjotakseen personoituja suosituksia, sisältöä ja käyttökokemuksia.
Esimerkki: Suoratoistopalvelut kuten Netflix käyttävät tekoälyä ehdottamaan elokuvia ja sarjoja katseluhistorian perusteella, mikä lisää käyttäjien sitoutumista ja tyytyväisyyttä.
- **Automaatio ja tehokkuus**: Tekoäly voi automatisoida toistuvia tehtäviä, virtaviivaistaa työnkulkuja ja parantaa operatiivista tehokkuutta.
Esimerkki: Asiakaspalvelusovellukset käyttävät tekoälypohjaisia chatboteja käsittelemään yleisiä kyselyjä, mikä lyhentää vasteaikoja ja vapauttaa ihmistyöntekijöitä monimutkaisempiin tehtäviin.
- **Parannettu käyttäjäkokemus**: Tekoäly voi parantaa kokonaiskäyttäjäkokemusta tarjoamalla älykkäitä ominaisuuksia, kuten puheentunnistusta, luonnollisen kielen käsittelyä ja ennustavaa tekstiä.
Esimerkki: Virtuaaliassistentit kuten Siri ja Google Assistant käyttävät tekoälyä ymmärtääkseen ja vastatakseen puhekäskyihin, jolloin laitteiden käyttäminen on helpompaa.

### Kuulostaa hyvältä, mutta miksi tarvitsemme tekoälyagenttikehystä?

Tekoälyagenttikehykset edustavat enemmän kuin pelkkiä tekoälykehyksiä. Ne on suunniteltu mahdollistamaan älykkäiden agenttien luominen, jotka voivat olla vuorovaikutuksessa käyttäjien, muiden agenttien ja ympäristön kanssa saavuttaakseen tiettyjä tavoitteita. Nämä agentit voivat osoittaa autonomista käyttäytymistä, tehdä päätöksiä ja sopeutua muuttuviin olosuhteisiin. Tarkastellaan joitakin keskeisiä kyvykkyyksiä, joita tekoälyagenttikehykset mahdollistavat:

- **Agenttien yhteistyö ja koordinointi**: Mahdollistaa useiden tekoälyagenttien luomisen, jotka voivat työskennellä yhdessä, kommunikoida ja koordinoitua ratkaistakseen monimutkaisia tehtäviä.
- **Tehtävien automaatio ja hallinta**: Tarjoaa mekanismeja monivaiheisten työnkulkujen automatisointiin, tehtävien delegointiin ja dynaamiseen tehtävien hallintaan agenttien kesken.
- **Kontekstuaalinen ymmärrys ja sopeutuminen**: Varustaa agentit kyvyllä ymmärtää kontekstia, sopeutua muuttuviin ympäristöihin ja tehdä päätöksiä reaaliaikaisen tiedon perusteella.

Yhteenvetona agentit antavat sinun tehdä enemmän: viedä automaation seuraavalle tasolle ja luoda älykkäämpiä järjestelmiä, jotka voivat sopeutua ja oppia ympäristöstään.

## Kuinka nopeasti prototypoida, iteroi ja parantaa agentin kyvykkyyksiä?

Tämä alue kehittyy nopeasti, mutta useimmissa tekoälyagenttikehyksissä on yhteisiä elementtejä, jotka auttavat sinua prototypoimaan ja iteratiivisesti kehittämään agentteja nopeasti: modulaariset komponentit, yhteistyövälineet ja reaaliaikainen oppiminen. Syvennytään näihin:

- **Käytä modulaarisia komponentteja**: AI-SDK:t tarjoavat valmiita komponentteja, kuten AI- ja Muistiyhteyksiä, funktiokutsuja luonnollisella kielellä tai koodilaajennuksilla, kehotepohjia ja paljon muuta.
- **Hyödynnä yhteistyövälineitä**: Suunnittele agentteja tietyillä rooleilla ja tehtävillä, jolloin ne voivat testata ja hioa yhteistyötyönkulkuja.
- **Opiskele reaaliajassa**: Toteuta palautesilmukoita, joissa agentit oppivat vuorovaikutuksista ja säätävät käyttäytymistään dynaamisesti.

### Käytä modulaarisia komponentteja

SDK:t, kuten Microsoft Agent Framework, tarjoavat valmiita komponentteja, kuten AI-yhdyskäytävät, työkalumäärittelyt ja agenttien hallinnan.

**Miten tiimit voivat käyttää näitä**: Tiimit voivat nopeasti koota nämä komponentit toimivaksi prototyypiksi ilman, että kaikkea tarvitsee rakentaa alusta alkaen, mikä mahdollistaa nopean kokeilun ja iteroinnin.

**Miten se toimii käytännössä**: Voit käyttää valmista jäsentä (parser) tietojen poimimiseen käyttäjän syötteestä, muistimoduulia tietojen tallentamiseen ja noutamiseen sekä kehotegeneraattoria vuorovaikutukseen käyttäjän kanssa — kaikki ilman, että sinun tarvitsee rakentaa näitä komponentteja tyhjästä.

**Esimerkkikoodi**. Tarkastellaan esimerkkiä siitä, miten voit käyttää Microsoft Agent Frameworkia `AzureAIProjectAgentProvider`-komponentin kanssa, jotta malli vastaa käyttäjän syötteeseen työkalukutsujen avulla:

``` python
# Microsoft Agent Framework Python -esimerkki

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Määrittele esimerkkityökalufunktio matkavarauksen tekemiseen
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Esimerkkituloste: Lentosi New Yorkiin 1. tammikuuta 2025 on varattu onnistuneesti. Hyvää matkaa! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Tästä esimerkistä näet, miten voit hyödyntää valmista jäsentä poimiaksesi keskeisiä tietoja käyttäjän syötteestä, kuten lähtöpaikan, määränpään ja päivämäärän lentovarauksen pyynnöstä. Tämä modulaarinen lähestymistapa antaa sinun keskittyä korkean tason logiikkaan.

### Hyödynnä yhteistyövälineitä

Kehykset kuten Microsoft Agent Framework helpottavat useiden agenttien luomista, jotka voivat työskennellä yhdessä.

**Miten tiimit voivat käyttää näitä**: Tiimit voivat suunnitella agentteja tiettyihin rooleihin ja tehtäviin, jolloin ne voivat testata ja hioa yhteistyötyönkulkuja ja parantaa järjestelmän kokonaistoimivuutta.

**Miten se toimii käytännössä**: Voit luoda agenttitiimin, jossa jokaisella agentilla on erikoistunut tehtävä, kuten tietojen haku, analyysi tai päätöksenteko. Nämä agentit voivat kommunikoida ja jakaa tietoa saavuttaakseen yhteisen tavoitteen, kuten vastaamalla käyttäjän kyselyyn tai suorittamalla tehtävän.

**Esimerkkikoodi (Microsoft Agent Framework)**:

```python
# Useiden agenttien luominen, jotka työskentelevät yhdessä Microsoft Agent Frameworkin avulla

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Datanhakija-agentti
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Datanalyysi-agentti
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Suorita agentit tehtävässä peräkkäin
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Edellisessä koodissa näet, miten voit luoda tehtävän, joka vaatii useiden agenttien yhteistyötä datan analysoimiseksi. Kukin agentti suorittaa yhden erikoistuneen toiminnon, ja tehtävä toteutetaan koordinoimalla agenttien työtä halutun lopputuloksen saavuttamiseksi. Luomalla omistautuneita agentteja erikoisrooleilla voi parantaa tehtävien tehokkuutta ja suorituskykyä.

### Opiskele reaaliajassa

Edistyneet kehykset tarjoavat kyvykkyyksiä reaaliaikaiseen kontekstin ymmärrykseen ja sopeutumiseen.

**Miten tiimit voivat käyttää näitä**: Tiimit voivat toteuttaa palautesilmukoita, joissa agentit oppivat vuorovaikutuksista ja säätävät käyttäytymistään dynaamisesti, mikä johtaa jatkuvaan parantamiseen ja kyvykkyyksien hienosäätöön.

**Miten se toimii käytännössä**: Agentit voivat analysoida käyttäjäpalautetta, ympäristötietoja ja tehtävien tuloksia päivittääkseen tietopohjaansa, säätääkseen päätöksentekoalgoritmejaan ja parantaakseen suoritustaan ajan myötä. Tämä iteratiivinen oppimisprosessi mahdollistaa agenttien sopeutumisen muuttuviin olosuhteisiin ja käyttäjäpreferensseihin, parantaen järjestelmän kokonaistehokkuutta.

## Mitkä ovat erot Microsoft Agent Frameworkin ja Azure AI Agent Servicen välillä?

Näitä lähestymistapoja voi verrata monin tavoin, mutta tarkastellaan joitakin keskeisiä eroja suunnittelun, kyvykkyyksien ja kohdekäyttötapausten näkökulmasta:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework tarjoaa virtaviivaisen SDK:n tekoälyagenttien rakentamiseen käyttäen `AzureAIProjectAgentProvider`-komponenttia. Se mahdollistaa agenttien luomisen, jotka hyödyntävät Azure OpenAI -malleja sisäänrakennetulla työkalukutsutoiminnallisuudella, keskustelunhallinnalla ja yritystason tietoturvalla Azure-identiteetin kautta.

**Käyttötapaukset**: Tuotantovalmiiden tekoälyagenttien rakentaminen, jotka käyttävät työkaluja, monivaiheisia työnkulkuja ja yritysintegraatioskenaarioita.

Tässä joitakin Microsoft Agent Frameworkin keskeisiä käsitteitä:

- **Agents**. Agentti luodaan `AzureAIProjectAgentProvider`-komponentin kautta ja konfiguroidaan nimellä, ohjeilla ja työkaluilla. Agentti voi:
  - **Käsitellä käyttäjäviestejä** ja tuottaa vastauksia Azure OpenAI -malleja käyttäen.
  - **Kutsua työkaluja** automaattisesti keskustelukontekstiin perustuen.
  - **Ylläpitää keskustelutilaa** useiden vuorovaikutusten ajan.

  Tässä on koodikatkelma, joka näyttää miten agentti luodaan:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Tools**. Kehys tukee työkalujen määrittelyä Python-funktioina, joita agentti voi kutsua automaattisesti. Työkalut rekisteröidään agenttia luodessa:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Moni-agenttien koordinointi**. Voit luoda useita agentteja eri erikoistumisilla ja koordinoida niiden toimintaa:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure Identity -integraatio**. Kehys käyttää `AzureCliCredential`- (tai `DefaultAzureCredential`) -todennusta turvalliseen, avaimettomaan autentikointiin, mikä poistaa tarpeen hallita API-avaimia suoraan.

## Azure AI Agent Service

Azure AI Agent Service on uudempi lisäys, esitelty Microsoft Ignite 2024 -tapahtumassa. Se mahdollistaa tekoälyagenttien kehittämisen ja käyttöönoton joustavampien mallien kanssa, kuten suoran kutsun avaimeen lähdekoodiin perustuviin LLM-malleihin kuten Llama 3, Mistral ja Cohere.

Azure AI Agent Service tarjoaa vahvempia yritystason tietoturvamekanismeja ja tiedonvarastointimenetelmiä, mikä tekee siitä sopivan yrityssovelluksiin.

Se toimii heti yhteensopivasti Microsoft Agent Frameworkin kanssa agenttien rakentamiseen ja käyttöönottoon.

Tämä palvelu on tällä hetkellä Public Preview -vaiheessa ja tukee agenttien rakentamista Pythonilla ja C#:lla.

Using the Azure AI Agent Service Python SDK, we can create an agent with a user-defined tool:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Määrittele työkalufunktiot
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Keskeiset käsitteet

Azure AI Agent Service sisältää seuraavat keskeiset käsitteet:

- **Agent**. Azure AI Agent Service integroituu Microsoft Foundryyn. AI Foundryn sisällä AI Agent toimii "älykkäänä" mikropalveluna, jota voidaan käyttää kysymyksiin vastaamiseen (RAG), toimien suorittamiseen tai työnkulkujen täydelliseen automatisointiin. Se saavuttaa tämän yhdistämällä generatiivisten mallien voiman työkaluihin, jotka antavat agentille pääsyn ja mahdollisuuden olla vuorovaikutuksessa reaalimaailman tietolähteiden kanssa. Tässä on esimerkki agentista:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Tässä esimerkissä agentti luodaan mallilla `gpt-4o-mini`, nimellä `my-agent` ja ohjeella `You are helpful agent`. Agentilla on käytössään työkaluja ja resursseja suoritettavaksi koodin tulkinta -tehtäviä.

- **Keskustelu ja viestit**. Lankaketju (thread) on toinen tärkeä käsite. Se edustaa keskustelua tai vuorovaikutusta agentin ja käyttäjän välillä. Lankoja voidaan käyttää keskustelun etenemisen seuraamiseen, kontekstin tallentamiseen ja vuorovaikutuksen tilan hallintaan. Tässä on esimerkki lankaketjusta:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Edellisessä koodissa luodaan lankaketju. Tämän jälkeen lankaan lähetetään viesti. Kutsumalla `create_and_process_run` pyydetään agenttia suorittamaan työtä lankaketjulle. Lopuksi viestit haetaan ja kirjataan nähdäksesi agentin vastauksen. Viestit osoittavat keskustelun etenemisen käyttäjän ja agentin välillä. On myös tärkeää ymmärtää, että viestit voivat olla eri tyyppejä, kuten tekstiä, kuva tai tiedosto — eli agentin työ on voinut esimerkiksi tuottaa kuvan tai tekstivastauksen. Kehittäjänä voit sitten käyttää tätä tietoa vastauksen jatkokäsittelyyn tai sen esittämiseen käyttäjälle.

- **Integroituu Microsoft Agent Frameworkin kanssa**. Azure AI Agent Service toimii saumattomasti Microsoft Agent Frameworkin kanssa, mikä tarkoittaa, että voit rakentaa agentteja käyttäen `AzureAIProjectAgentProvider`-komponenttia ja ottaa ne käyttöön Agent Service -palvelun kautta tuotantoympäristöihin.

**Käyttötapaukset**: Azure AI Agent Service on suunniteltu yrityssovelluksiin, jotka vaativat turvallista, skaalautuvaa ja joustavaa tekoälyagenttien käyttöönottoa.

## Mikä on ero näiden lähestymistapojen välillä?
 
Näyttäisi siltä, että päällekkäisyyttä on, mutta suunnittelun, kyvykkyyksien ja kohdekäyttötapausten osalta on joitakin keskeisiä eroja:
 
- **Microsoft Agent Framework (MAF)**: On tuotantovalmiiksi tarkoitettu SDK tekoälyagenttien rakentamiseen. Se tarjoaa virtaviivaisen API:n agenttien luomiseen työkaluilla, keskustelunhallinnalla ja Azure-identiteetin integraatiolla.
- **Azure AI Agent Service**: On alusta ja käyttöönotopalvelu Azure Foundryssa agentteja varten. Se tarjoaa sisäänrakennetun yhteyden palveluihin, kuten Azure OpenAI, Azure AI Search, Bing Search ja koodin suoritus.
 
Et ole vielä varma, kumpi valita?

### Käyttötapaukset
 
Käydään läpi joitakin yleisiä käyttötapauksia, jotka voivat auttaa päätöksenteossa:
 
> Q: Rakennan tuotantoon meneviä tekoälyagenttisovelluksia ja haluan päästä nopeasti alkuun
>
> A: Microsoft Agent Framework on erinomainen valinta. Se tarjoaa yksinkertaisen, Python-tyyppisen API:n `AzureAIProjectAgentProvider`-komponentin kautta, jonka avulla voit määritellä agentteja työkaluilla ja ohjeilla vain muutamalla koodirivillä.
 
> Q: Tarvitsen yritystason käyttöönoton Azure-integraatioilla, kuten Search ja koodin suoritus
>
> A: Azure AI Agent Service on paras valinta. Se on alusta, joka tarjoaa sisäänrakennetut kyvykkyydet monille malleille, Azure AI Searchille, Bing Searchille ja Azure Functionsille. Sen avulla agenttien rakentaminen Foundry-portaalissa ja niiden käyttöönotto laajassa mittakaavassa on helppoa.
 
> Q: Olen vielä epävarma, anna yksi vaihtoehto
>
> A: Aloita Microsoft Agent Frameworkilla agenttien rakentamiseen, ja käytä Azure AI Agent Servicea, kun tarvitset käyttöönottoa ja skaalausta tuotannossa. Tämä lähestymistapa antaa sinulle mahdollisuuden iteroda nopeasti agenttilogiikkaa samalla kun sinulla on selkeä polku yritystason käyttöönottoon.
 
Yhteenvetona keskeiset erot taulukossa:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool calling | Agents, Tools, Azure Identity | Building AI agents, tool use, multi-step workflows |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## Voinko integroida olemassa olevat Azure-ekosysteemin työkaluni suoraan, vai tarvitaanko erillisiä ratkaisuja?
Vastaus on kyllä: voit integroida olemassa olevat Azure-ekosysteemisi työkalut suoraan erityisesti Azure AI Agent Serviceen, koska se on rakennettu toimimaan saumattomasti muiden Azure-palveluiden kanssa. Voit esimerkiksi integroida Bingin, Azure AI Searchin ja Azure Functionsin. Microsoft Foundryn kanssa on myös syvä integraatio.

Microsoft Agent Framework integroituu myös Azure-palveluihin `AzureAIProjectAgentProvider`-komponentin ja Azure-identiteetin kautta, jolloin voit kutsua Azure-palveluita suoraan agenttityökaluistasi.

## Sample Codes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Got More Questions about AI Agent Frameworks?

Liity [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) tapaamaan muita oppijoita, osallistumaan vastaanottoaikoihin ja saadaksesi vastauksia AI-agentteja koskeviin kysymyksiisi.

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Previous Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastuuvapauslauseke:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua Co-op Translator (https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomaathan, että automatisoiduissa käännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää määräysvallassa olevana lähteenä. Kriittisten tietojen osalta suositellaan ammattimaisen ihmiskääntäjän käyttöä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->