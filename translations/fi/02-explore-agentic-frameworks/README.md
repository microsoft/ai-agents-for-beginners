[![Tutustu tekoälyagenttikehyksiin](../../../translated_images/fi/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klikkaa yllä olevaa kuvaa katsellaksesi tämän oppitunnin videon)_

# Tutustu tekoälyagenttikehyksiin

Tekoälyagenttikehykset ovat ohjelmistoalustoja, jotka on suunniteltu helpottamaan tekoälyagenttien luomista, käyttöönottoa ja hallintaa. Nämä kehykset tarjoavat kehittäjille valmiita komponentteja, abstraktioita ja työkaluja, jotka tehostavat monimutkaisten tekoälyjärjestelmien kehittämistä.

Kehykset auttavat kehittäjiä keskittymään sovellustensa ainutlaatuisiin osa-alueisiin tarjoamalla standardoituja lähestymistapoja tekoälyagenttien kehittämisessä yleisiin haasteisiin. Ne parantavat skaalautuvuutta, saavutettavuutta ja tehokkuutta tekoälyjärjestelmien rakentamisessa.

## Johdanto 

Tässä oppitunnissa käsitellään:

- Mitä tekoälyagenttikehykset ovat ja mitä ne mahdollistavat kehittäjille?
- Miten tiimit voivat käyttää näitä nopeasti prototyyppien tekemiseen, iterointiin ja agenttien kykyjen parantamiseen?
- Mitkä ovat Microsoftin kehittämien kehysten ja työkalujen eroavaisuudet (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> ja <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Voinko integroida olemassa olevat Azure-ekosysteemin työkaluni suoraan, vai tarvitaanko erillisiä ratkaisuja?
- Mikä on Microsoft Foundry Agent Service ja miten se auttaa minua?

## Oppimistavoitteet

Tämän oppitunnin tavoitteena on auttaa sinua ymmärtämään:

- Tekoälyagenttikehysten rooli tekoälyn kehityksessä.
- Miten hyödyntää tekoälyagenttikehyksiä älykkäiden agenttien rakentamisessa.
- Tärkeimmät tekoälyagenttikehysten tarjoamat kyvyt.
- Eroja Microsoft Agent Frameworkin ja Microsoft Foundry Agent Servicen välillä.

## Mitä tekoälyagenttikehykset ovat ja mitä ne mahdollistavat kehittäjille?

Perinteiset tekoälykehykset voivat auttaa integroimaan tekoälyä sovelluksiisi ja parantamaan näitä sovelluksia seuraavilla tavoilla:

- **Personalisointi**: Tekoäly voi analysoida käyttäjän käyttäytymistä ja mieltymyksiä tarjotakseen personoituja suosituksia, sisältöä ja käyttökokemuksia.
Esimerkki: Suoratoistopalvelut kuten Netflix käyttävät tekoälyä ehdottaakseen elokuvia ja sarjoja katseluhistorian perusteella, mikä parantaa käyttäjän sitoutumista ja tyytyväisyyttä.
- **Automaatio ja tehokkuus**: Tekoäly voi automatisoida toistuvia tehtäviä, virtaviivaistaa työprosesseja ja parantaa operatiivista tehokkuutta.
Esimerkki: Asiakaspalvelusovellukset käyttävät tekoälyllä toimivia chatboteja käsittelemään yleisiä kyselyitä, jolloin vasteajat lyhenevät ja ihmiskonsultit voivat keskittyä monimutkaisempiin asioihin.
- **Parannettu käyttökokemus**: Tekoäly voi parantaa yleistä käyttökokemusta tarjoamalla älykkäitä ominaisuuksia kuten puheentunnistusta, luonnollisen kielen käsittelyä ja ennakoivaa tekstinkirjoitusta.
Esimerkki: Virtuaaliassistenteet kuten Siri ja Google Assistant käyttävät tekoälyä ymmärtämään ja vastaamaan äänikomentoihin, helpottaen käyttäjien vuorovaikutusta laitteidensa kanssa.

### Kaikki kuulostaa hyvältä, mutta miksi sitten tarvitsemme tekoälyagenttikehyksen?

Tekoälyagenttikehykset ovat enemmän kuin pelkkiä tekoälykehyksiä. Ne on suunniteltu mahdollistamaan älykkäiden agenttien luominen, jotka voivat olla vuorovaikutuksessa käyttäjien, muiden agenttien ja ympäristön kanssa tiettyjen tavoitteiden saavuttamiseksi. Nämä agentit voivat toimia itsenäisesti, tehdä päätöksiä ja sopeutua muuttuviin olosuhteisiin. Tarkastellaan joitakin keskeisiä tekoälyagenttikehysten mahdollistamia kykyjä:

- **Agenttien yhteistyö ja koordinointi**: Mahdollistaa useiden tekoälyagenttien luomisen, jotka voivat työskennellä yhdessä, kommunikoida ja koordinoida monimutkaisten tehtävien ratkaisemiseksi.
- **Tehtävien automaatio ja hallinta**: Tarjoaa mekanismeja monivaiheisten työnkulkujen automatisointiin, tehtävien delegointiin ja dynaamiseen tehtävähallintaan agenttien välillä.
- **Kontekstuaalinen ymmärtäminen ja sopeutuminen**: Varustaa agentit kyvyllä ymmärtää kontekstia, sopeutua muuttuviin ympäristöihin ja tehdä päätöksiä reaaliaikaisen tiedon perusteella.

Yhteenvetona agentit mahdollistavat enemmän tekemistä, automaation nostamisen uudelle tasolle ja älykkäämpien järjestelmien luomisen, jotka voivat oppia ja sopeutua ympäristöönsä.

## Miten nopeasti prototyyppien tekoon, iterointiin ja agentin kykyjen parantamiseen?

Tämä ala kehittyy nopeasti, mutta useimmissa tekoälyagenttikehyksissä on joitakin yleisiä piirteitä, jotka auttavat sinua tekemään prototyyppejä ja iteratiivista kehitystä, nimittäin modulaariset komponentit, yhteistyövälineet ja reaaliaikainen oppiminen. Tutkitaanpa näitä:

- **Käytä modulaarisia komponentteja**: Tekoälyohjelmistokehykset tarjoavat valmiita komponentteja, kuten tekoäly- ja muistikytkimiä, luonnollisen kielen tai koodin laajennusten funktiokutsuja, kehotemalleja ja muuta.
- **Hyödynnä yhteistyövälineitä**: Suunnittele agentteja erityisillä rooleilla ja tehtävillä, jotka mahdollistavat yhteistyöprosessien testaamisen ja hiomisen.
- **Opiskele reaaliajassa**: Toteuta palautesilmukoita, joissa agentit oppivat vuorovaikutuksista ja sopeuttavat käyttäytymistään dynaamisesti.

### Käytä modulaarisia komponentteja

Esimerkiksi Microsoft Agent Framework tarjoaa valmiita komponentteja, kuten tekoälykytkimiä, työkalumääritelmiä ja agenttien hallintaa.

**Miten tiimit voivat käyttää näitä**: Tiimit voivat nopeasti kokoilla nämä komponentit toimivaksi prototyypiksi ilman, että heidän tarvitsee aloittaa alusta, mikä mahdollistaa nopean kokeilun ja iteroinnin.

**Näin se toimii käytännössä**: Voit käyttää valmista parseria käyttäjän syötteestä tiedon poimimiseen, muistimoduulia tiedon tallentamiseen ja hakemiseen sekä kehotegeneraattoria vuorovaikutukseen käyttäjien kanssa, kaikki ilman tarvetta rakentaa näitä komponentteja alusta.

**Esimerkkikoodi**. Tarkastellaan esimerkkiä siitä, miten Microsoft Agent Frameworkia voi käyttää `FoundryChatClient`-luokan kanssa, jotta malli vastaa käyttäjän syötteeseen työkalukutsujen avulla:

``` python
# Microsoft Agent Framework Python -esimerkki

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Määrittele esimerkkityökalu matkavarauksen tekemiseen
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Esimerkkituloste: Lentosi New Yorkiin 1. tammikuuta 2025 on onnistuneesti varattu. Hyvää matkaa! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Tässä esimerkissä näet, kuinka voit hyödyntää valmista parseria käyttäjältä saatujen tärkeiden tietojen, kuten lähtöpaikan, määränpään ja lennon varaustiedon päivämäärän, poimimiseen. Tämä modulaarinen lähestymistapa antaa sinun keskittyä korkean tason logiikkaan.

### Hyödynnä yhteistyövälineitä

Kehykset kuten Microsoft Agent Framework helpottavat useiden agenttien luomista, jotka voivat työskennellä yhdessä.

**Miten tiimit voivat käyttää näitä**: Tiimit voivat suunnitella agentteja erityisillä rooleilla ja tehtävillä, joita voidaan testata ja hienosäätää yhteistyötyönkulkuja parantaen kokonaistehokkuutta.

**Näin se toimii käytännössä**: Voit luoda agenttitiimin, jossa jokaisella agentilla on erikoistunut tehtävä, kuten tiedonhaku, analyysi tai päätöksenteko. Nämä agentit voivat kommunikoida ja jakaa tietoa yhteisen tavoitteen saavuttamiseksi, kuten vastaamaan käyttäjän kyselyyn tai suorittamaan tehtävän.

**Esimerkkikoodi (Microsoft Agent Framework)**:

```python
# Useiden agenttien luominen, jotka työskentelevät yhdessä Microsoft Agent Frameworkin avulla

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Tietojen hakemiseen tarkoitettu agentti
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Tietojen analysointiin tarkoitettu agentti
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Suorita agentit tehtävässä peräkkäin
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Edellisessä koodissa näet, miten voit luoda tehtävän, johon osallistuu useita agentteja yhdessä analysoimaan dataa. Jokainen agentti suorittaa oman erikoistehtävänsä, ja tehtävä hoidetaan koordinoimalla agentteja tavoitteen saavuttamiseksi. Erikoistuneiden agenttien luominen parantaa tehtävän tehokkuutta ja suorituskykyä.

### Opiskele reaaliajassa

Edistyneet kehykset tarjoavat kykyjä reaaliaikaiseen kontekstin ymmärtämiseen ja sopeutumiseen.

**Miten tiimit voivat käyttää näitä**: Tiimit voivat toteuttaa palautesilmukoita, joissa agentit oppivat vuorovaikutuksista ja sopeuttavat käyttäytymistään dynaamisesti, mikä johtaa kykyjen jatkuvaan parantamiseen ja hienosäätöön.

**Näin se toimii käytännössä**: Agentit voivat analysoida käyttäjäpalautetta, ympäristötietoja ja tehtävien tuloksia päivittääkseen tietopohjaansa, säädelläkseen päätöksentekoalgoritmejaan ja parantaakseen suorituskykyä ajan myötä. Tämä iteratiivinen oppimisprosessi mahdollistaa agenttien sopeutumisen muuttuviin olosuhteisiin ja käyttäjäpreferensseihin, parantaen järjestelmän kokonaistehokkuutta.

## Mitkä ovat Microsoft Agent Frameworkin ja Microsoft Foundry Agent Servicen erot?

Näitä lähestymistapoja voi vertailla monella tavalla, mutta tarkastellaan joitakin keskeisiä eroja suunnittelun, kykyjen ja kohdekäyttötarkoitusten osalta:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework tarjoaa virtaviivaistetun SDK:n tekoälyagenttien rakentamiseen käyttäen `FoundryChatClient`-luokkaa. Se mahdollistaa kehittäjien luoda agentteja, jotka hyödyntävät Azure OpenAI -malleja sisäänrakennetulla työkalukutsulla, keskustelun hallinnalla ja yritystason turvallisuudella Azure-identiteetin kautta.

**Käyttötapaukset**: Tuotantovalmiiden tekoälyagenttien rakentaminen, joissa on työkalujen käyttö, monivaiheiset työnkulut ja yritysintegrointitilanteet.

Tässä muutamia tärkeitä Microsoft Agent Frameworkin ydinkäsitteitä:

- **Agentit**. Agentti luodaan `FoundryChatClient`-luokan kautta ja konfiguroidaan nimellä, ohjeilla ja työkaluilla. Agentti voi:
  - **Käsitellä käyttäjän viestejä** ja tuottaa vastauksia Azure OpenAI -malleilla.
  - **Kutsua työkaluja** automaattisesti keskustelukontekstin perusteella.
  - **Ylläpitää keskustelutilaa** useiden vuorovaikutusten ajan.

  Tässä on koodinpätkä, joka näyttää agentin luomisen:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Työkalut**. Kehys tukee työkalujen määrittelyä Python-funktioina, joita agentti voi kutsua automaattisesti. Työkalut rekisteröidään agenttia luodessa:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Usean agentin koordinointi**. Voit luoda useita eri erikoistuneita agentteja ja koordinoida heidän työtään:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure-identiteetin integrointi**. Kehys käyttää `AzureCliCredential`- tai `DefaultAzureCredential`-luokkia turvalliseen, avaimettomaan tunnistautumiseen, mikä poistaa API-avainten hallinnan tarpeen.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service on uudempi lisäys, joka esiteltiin Microsoft Ignite 2024 -tapahtumassa. Se mahdollistaa tekoälyagenttien kehittämisen ja käyttöönoton joustavammilla malleilla, kuten suoraan avoimen lähdekoodin LLM:illä kuten Llama 3, Mistral ja Cohere.

Microsoft Foundry Agent Service tarjoaa vahvemmat yritystason suojausmekanismit ja tietovarastointitavat, tehden siitä soveltuvan yrityssovelluksiin.

Se toimii suoraan yhdessä Microsoft Agent Frameworkin kanssa agenttien rakentamiseen ja käyttöönottoon.

Tämä palvelu on tällä hetkellä julkisessa esikatseluvaiheessa ja tukee Pythonia ja C#:tä agenttien rakentamiseen.

Käyttämällä Microsoft Foundry Agent Service Python -SDK:ta voidaan luoda agentti käyttäjän määrittelemällä työkalulla:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Määrittele työkalutoiminnot
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

### Ydinkäsitteet

Microsoft Foundry Agent Servicellä on seuraavat ydinkäsitteet:

- **Agentti**. Microsoft Foundry Agent Service integroituu Microsoft Foundryn kanssa. Microsoft Foundryn sisällä tekoälyagentti toimii "älykkäänä" mikropalveluna, jota voidaan käyttää kysymysten vastaamiseen (RAG), toimenpiteiden suorittamiseen tai työnkulkujen täydelliseen automaatioon. Tämä onnistuu yhdistämällä generatiivisten tekoälymallien voima työkaluihin, joiden avulla agentti voi käyttää ja olla vuorovaikutuksessa todellisten tietolähteiden kanssa. Tässä esimerkki agentista:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Tässä esimerkissä luodaan agentti mallilla `gpt-4o-mini`, nimellä `my-agent` ja ohjeistuksella `You are helpful agent`. Agentti on varustettu työkaluilla ja resursseilla koodin tulkintatehtäviä varten.

- **Keskusteluketju ja viestit**. Keskusteluketju on toinen tärkeä käsite. Se kuvaa keskustelua tai vuorovaikutusta agentin ja käyttäjän välillä. Keskusteluketjuja voidaan käyttää keskustelun etenemisen seuraamiseen, kontekstin tallennukseen ja vuorovaikutustilan hallintaan. Tässä esimerkki ketjusta:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Pyydä agenttia suorittamaan työtä ketjussa
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Hae ja kirjaa kaikki viestit nähdäksesi agentin vastauksen
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Edellisessä koodissa luodaan ketju, johon sen jälkeen lähetetään viesti. Kutsumalla `create_and_process_run` agenttia pyydetään suorittamaan tehtävä ketjussa. Lopuksi viestit haetaan ja tallennetaan nähtäväksi agentin vastaus. Viestit kertovat keskustelun etenemisestä käyttäjän ja agentin välillä. On myös tärkeää ymmärtää, että viestit voivat olla eri tyyppejä, kuten tekstiä, kuvaa tai tiedostoa, jotka agentin työ on tuottanut esimerkiksi kuvan tai tekstivastauksen muodossa. Kehittäjänä voit käyttää tätä tietoa vastausten jatkokäsittelyyn tai esittämiseen käyttäjälle.

- **Integroituu Microsoft Agent Frameworkiin**. Microsoft Foundry Agent Service toimii saumattomasti Microsoft Agent Frameworkin kanssa, mikä tarkoittaa, että voit rakentaa agentteja `FoundryChatClient`-luokalla ja ottaa ne käyttöön Agent Service -palvelun kautta tuotantokäyttöön.

**Käyttötapaukset**: Microsoft Foundry Agent Service on suunniteltu yrityssovelluksiin, jotka vaativat turvallista, skaalautuvaa ja joustavaa tekoälyagenttien käyttöönottoa.

## Mikä ero näissä lähestymistavoissa on?
 
Vaikka vaikutelma on, että alueet menevät päällekkäin, tässä on joitakin keskeisiä eroja suunnittelun, kykyjen ja kohdekäyttötarkoitusten osalta:
 
- **Microsoft Agent Framework (MAF)**: Tuotantovalmis SDK tekoälyagenttien rakentamiseen. Se tarjoaa virtaviivaistetun API:n agenttien luomiseen työkalukutsulla, keskustelun hallinnalla ja Azure-identiteetin integroinnilla.
- **Microsoft Foundry Agent Service**: On Microsoft Foundryssa toimiva alusta ja käyttöönotto-palvelu agenteille. Se tarjoaa valmiin yhteyden palveluihin kuten Azure OpenAI, Azure AI Search, Bing Search ja koodin suoritus.
 
Etkö ole vieläkään varma, kumpi valita?

### Käyttötapaukset
 
Katsotaanpa, jos voimme auttaa käymällä läpi muutamia yleisiä käyttötapauksia:
 
> K: Rakennan tuotantovalmiita tekoälyagenttisovelluksia ja haluan päästä nopeasti alkuun
>

>V: Microsoft Agent Framework on loistava valinta. Se tarjoaa yksinkertaisen, Python-tyyppisen API:n `FoundryChatClient`-luokan kautta, jonka avulla voit määritellä agentteja työkaluilla ja ohjeilla vain muutamalla koodirivillä.

>K: Tarvitsen yritystason käyttöönoton Azure-integraatioilla kuten Search ja koodin suoritus
>
>V: Microsoft Foundry Agent Service on paras valinta. Se on palvelualusta, joka tarjoaa valmiit kyvyt useille malleille, Azure AI Searchille, Bing Searchille ja Azure Functionsille. Sen avulla voit helposti rakentaa agenttisi Foundry-portaalissa ja ottaa ne käyttöön suuressa mittakaavassa.
 
> K: Olen edelleen hämmentynyt, anna minulle vain yksi vaihtoehto
>
> V: Aloita Microsoft Agent Frameworkista agenttien rakentamiseen ja siirry Microsoft Foundry Agent Serviceen, kun tarvitset tuotantokäyttöön vientiä ja skaalautuvuutta. Tämä malli mahdollistaa nopean iteraation agenttisi logiikassa pitäen kuitenkin selkeän polun yritystason käyttöönottoon.
 
Tehdään yhteenveto keskeisistä eroista taulukossa:

| Kehys | Keskittyminen | Ydinkäsitteet | Käyttötapaukset |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Virtaviivaistettu agenttien SDK työkalukutsulla | Agentit, Työkalut, Azure-identiteetti | Tekoälyagenttien rakentaminen, työkalujen käyttö, monivaiheiset työnkulut |
| Microsoft Foundry Agent Service | Joustavat mallit, yritystason turvallisuus, koodin generointi, työkalukutsu | Modulaarisuus, Yhteistyö, Prosessin orkestrointi | Turvallinen, skaalautuva ja joustava tekoälyagenttien käyttöönotto |

## Voinko integroida olemassa olevat Azure-ekosysteemin työkaluni suoraan, vai tarvitaanko erillisiä ratkaisuja?


Vastaus on kyllä, voit integroida olemassa olevat Azure-ekosysteemin työkalusi suoraan Microsoft Foundry Agent Serviceen erityisesti, koska se on rakennettu toimimaan saumattomasti muiden Azure-palveluiden kanssa. Voisit esimerkiksi integroida Bingiä, Azure AI Searchia ja Azure Functionseja. Microsoft Foundryn kanssa on myös syvä integraatio.

Microsoft Agent Framework integroituu myös Azure-palveluihin `FoundryChatClient`- ja Azure-identityn kautta, jolloin voit kutsua Azure-palveluita suoraan agenttityökaluistasi.

## Esimerkkikoodit

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Lisää kysymyksiä AI-agenttikehyksistä?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia AI-agenttien kysymyksiisi.

## Viitteet

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Edellinen Oppitunti

[Johdatus AI-agentteihin ja agenttien käyttötapauksiin](../01-intro-to-ai-agents/README.md)

## Seuraava Oppitunti

[Agenttista suunnittelumallien ymmärtäminen](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->