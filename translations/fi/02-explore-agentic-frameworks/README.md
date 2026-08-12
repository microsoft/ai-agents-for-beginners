[![Tutustu tekoälyagenttikehyksiin](../../../translated_images/fi/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

# Tutustu tekoälyagenttikehyksiin

Tekoälyagenttikehykset ovat ohjelmistoalustoja, jotka on suunniteltu helpottamaan tekoälyagenttien luomista, käyttöönottoa ja hallintaa. Nämä kehykset tarjoavat kehittäjille valmiita komponentteja, abstraktioita ja työkaluja, jotka sujuvoittavat monimutkaisten tekoälyjärjestelmien kehitystä.

Nämä kehykset auttavat kehittäjiä keskittymään sovellustensa ainutlaatuisiin puoliin tarjoamalla standardoituja lähestymistapoja tekoälyagenttien kehittämisen yleisiin haasteisiin. Ne parantavat skaalautuvuutta, saavutettavuutta ja tehokkuutta tekoälyjärjestelmien rakentamisessa.

## Johdanto

Tässä oppitunnissa käsitellään:

- Mitä tekoälyagenttikehykset ovat ja mitä ne mahdollistavat kehittäjille?
- Kuinka tiimit voivat käyttää näitä nopeaan prototypointiin, iterointiin ja agenttien kykyjen parantamiseen?
- Mitkä ovat Microsoftin luomien kehysten ja työkalujen (Microsoft Foundry Agent Service ja Microsoft Agent Framework) erot?
- Voinko integroida olemassa olevia Azure-ekosysteemissäni käytettäviä työkaluja suoraan vai tarvitseeko erillisiä ratkaisuja?
- Mitä Microsoft Foundry Agent Service on ja kuinka se auttaa minua?

## Oppimistavoitteet

Tämän oppitunnin tavoitteena on auttaa sinua ymmärtämään:

- Tekoälyagenttikehysten rooli tekoälyn kehityksessä.
- Kuinka hyödyntää tekoälyagenttikehyksiä älykkäiden agenttien rakentamiseen.
- Keskeiset ominaisuudet, joita tekoälyagenttikehykset mahdollistavat.
- Erot Microsoft Agent Frameworkin ja Microsoft Foundry Agent Servicen välillä.

## Mitä tekoälyagenttikehykset ovat ja mitä ne mahdollistavat kehittäjille?

Perinteiset tekoälykehykset voivat auttaa sinua integroimaan tekoälyä sovelluksiin ja parantamaan näitä sovelluksia seuraavilla tavoilla:

- **Personointi**: Tekoäly voi analysoida käyttäjän käyttäytymistä ja mieltymyksiä tarjotakseen personoituja suosituksia, sisältöä ja kokemuksia.
Esimerkki: Suoratoistopalvelut, kuten Netflix, käyttävät tekoälyä ehdottamaan elokuvia ja sarjoja katseluhistorian perusteella lisäten käyttäjien sitoutumista ja tyytyväisyyttä.
- **Automaatio ja tehokkuus**: Tekoäly voi automatisoida toistuvia tehtäviä, virtaviivaistaa työnkulkuja ja parantaa operatiivista tehokkuutta.
Esimerkki: Asiakaspalvelusovelluksissa tekoälypohjaiset chatbotit hoitavat yleisiä tiedusteluja, lyhentäen vastausaikoja ja vapauttaen ihmiskonsultit monimutkaisempiin kysymyksiin.
- **Parannettu käyttäjäkokemus**: Tekoäly voi parantaa kokonaiskäyttäjäkokemusta tarjoamalla älykkäitä ominaisuuksia, kuten puheentunnistusta, luonnollisen kielen käsittelyä ja ennakoivaa tekstinsyöttöä.
Esimerkki: Virtuaaliassistentit kuten Siri ja Google Assistant käyttävät tekoälyä ymmärtääkseen ja vastatakseen puhekäskyihin, helpottaen käyttäjien vuorovaikutusta laitteidensa kanssa.

### Kuulostaa hienolta, mutta miksi tarvitsemme tekoälyagenttikehystä?

Tekoälyagenttikehykset ovat jotain enemmän kuin pelkkiä tekoälykehyksiä. Ne on suunniteltu mahdollistamaan älykkäiden agenttien luominen, jotka voivat olla vuorovaikutuksessa käyttäjien, muiden agenttien ja ympäristön kanssa saavuttaakseen tiettyjä tavoitteita. Nämä agentit voivat osoittaa autonomista käyttäytymistä, tehdä päätöksiä ja sopeutua muuttuviin olosuhteisiin. Katsotaan joitakin tekoälyagenttikehysten mahdollistamia keskeisiä ominaisuuksia:

- **Agenttien yhteistyö ja koordinointi**: Mahdollistavat useiden tekoälyagenttien luomisen, jotka voivat työskennellä yhdessä, kommunikoida ja koordinoida monimutkaisten tehtävien ratkaisemiseksi.
- **Tehtävien automaatio ja hallinta**: Tarjoavat mekanismeja monivaiheisten työnkulkujen automatisointiin, tehtävien delegointiin ja dynaamiseen tehtävien hallintaan agenttien kesken.
- **Kontekstuaalinen ymmärrys ja sopeutuminen**: Varustavat agentit kyvyllä ymmärtää konteksti, sopeutua muuttuviin ympäristöihin ja tehdä päätöksiä reaaliaikaisen tiedon perusteella.

Yhteenvetona, agentit antavat sinun tehdä enemmän, viedä automaation uudelle tasolle, luoda älykkäämpiä järjestelmiä jotka voivat sopeutua ja oppia ympäristöstään.

## Kuinka prototyypittää, iteratiivisesti kehittää ja parantaa agentin kykyjä nopeasti?

Tämä ala kehittyy nopeasti, mutta useimmissa tekoälyagenttikehyksissä on joitakin yhteisiä piirteitä, jotka auttavat sinua nopeaan prototypointiin ja iterointiin, nimittäin modulaariset komponentit, yhteistyötyökalut ja reaaliaikainen oppiminen. Käydään nämä läpi:

- **Käytä modulaarisia komponentteja**: AI:n SDK:t tarjoavat valmiita komponentteja, kuten AI- ja muistiliittimiä, luonnolliseen kieleen tai koodilaajennuksiin perustuvaa funktiokutsua, kehotepohjia ja muuta.
- **Hyödynnä yhteistyötyökaluja**: Suunnittele agenteille erityisiä rooleja ja tehtäviä, jolloin ne voivat testata ja parantaa yhteistyön työnkulkuja.
- **Opiskele reaaliajassa**: Toteuta palautesilmukoita, joissa agentit oppivat vuorovaikutuksista ja säätävät käyttäytymistään dynaamisesti.

### Käytä modulaarisia komponentteja

Microsoft Agent Frameworkin kaltaiset SDK:t tarjoavat valmiita komponentteja, kuten AI-liittimiä, työkalumäärittelyjä ja agenttien hallintaa.

**Kuinka tiimit voivat hyödyntää näitä**: Tiimit voivat nopeasti kokoaa nämä komponentit toimiakseen prototyypin luomisessa ilman aloitusta nollasta, mahdollistaen nopean kokeilun ja iteroinnin.

**Kuinka se toimii käytännössä**: Voit käyttää valmiiksi rakennettua jäsentäjänä tietojen erottamiseen käyttäjän syötteestä, muistimoduulia tietojen tallennukseen ja hakemiseen sekä kehotegeneraattoria käyttäjien kanssa vuorovaikutukseen – kaikki ilman komponenttien rakentamista alusta alkaen.

**Esimerkkikoodi**. Katsotaan esimerkkiä Microsoft Agent Frameworkin käytöstä `FoundryChatClient`-luokan kanssa, jossa malli vastaa käyttäjän syötteeseen työkalukutsun avulla:

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
    # Esimerkkituloste: Lentosi New Yorkiin 1. tammikuuta 2025 on varattu onnistuneesti. Hyvää matkaa! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Tästä esimerkistä näet, kuinka voit hyödyntää valmiiksi rakennettua jäsentäjää avaintietojen poimimiseen käyttäjän syötteestä, kuten lennon varausta koskevat lähtöpaikka, kohde ja päivämäärä. Tämä modulaarinen lähestymistapa antaa sinun keskittyä korkeatasoiseen logiikkaan.

### Hyödynnä yhteistyötyökaluja

Microsoft Agent Frameworkin kaltaiset kehykset helpottavat useiden agenttien luomista, jotka voivat työskennellä yhdessä.

**Kuinka tiimit voivat hyödyntää näitä**: Tiimit voivat suunnitella agenteille erityisiä rooleja ja tehtäviä, mahdollistaen yhteistyön työnkulkujen testaamisen ja parantamisen sekä koko järjestelmän tehokkuuden kasvattamisen.

**Kuinka se toimii käytännössä**: Voit luoda agenttitiimin, jossa kullakin agentilla on erityinen tehtävä, esimerkiksi tietojen hakeminen, analyysi tai päätöksenteko. Agentit voivat kommunikoida ja jakaa tietoja saavuttaakseen yhteisen tavoitteen, kuten käyttäjän kysymyksen vastaamisen tai tehtävän suorittamisen.

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

# Tietojen hakemisen agentti
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Tietojen analysoinnin agentti
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Agenttien suorittaminen peräkkäin tehtävässä
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Edellisessä koodissa näet, kuinka voit luoda tehtävän, joka sisältää useiden agenttien yhteistyön datan analysoimiseksi. Jokainen agentti suorittaa tietyn tehtävän ja työ koordinoidaan halutun lopputuloksen saavuttamiseksi. Omistetuilla erikoisrooleilla varustetut agentit parantavat tehtävän tehokkuutta ja suorituskykyä.

### Opiskele reaaliajassa

Kehittyneet kehykset tarjoavat kyvyn reaaliaikaiseen kontekstin ymmärtämiseen ja sopeutumiseen.

**Kuinka tiimit voivat hyödyntää näitä**: Tiimit voivat toteuttaa palautesilmukoita, joissa agentit oppivat vuorovaikutuksista ja säätävät dynamiikkaa käyttäytymisessään, johtuen jatkuvan parantamisen ja kykyjen hienosäädön.

**Kuinka se toimii käytännössä**: Agentit voivat analysoida käyttäjäpalautetta, ympäristötietoja ja tehtävän tuloksia päivittääkseen tietopohjaansa, säätääkseen päätöksentekoalgoritmeja ja parantaakseen suorituskykyään ajan myötä. Tämä iteratiivinen oppimisprosessi mahdollistaa agenttien sopeutumisen muuttuviin olosuhteisiin ja käyttäjäpreferensseihin, parantaen järjestelmän yleistä tehokkuutta.

## Mitkä ovat Microsoft Agent Frameworkin ja Microsoft Foundry Agent Servicen erot?

Näitä lähestymistapoja voi vertailla monella tavalla, mutta katsotaan keskeisiä eroja niiden suunnittelun, kyvykkyyksien ja kohdesovellusten kannalta:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework tarjoaa virtaviivaistetun SDK:n tekoälyagenttien rakentamiseen `FoundryChatClient`-luokkaa käyttäen. Se mahdollistaa kehittäjille agenttien luomisen, jotka hyödyntävät Azure OpenAI -malleja sisäänrakennetulla työkalukutsulla, keskustelun hallinnalla ja yritystason suojauksella Azure-identiteetin avulla.

**Käyttötapaukset**: Tuotantovalmiiden tekoälyagenttien rakentaminen työkalujen käytöllä, monivaiheisilla työnkuluilla ja yritysintegraatioskenaarioilla.

Tässä muutamia tärkeitä keskeisiä käsitteitä Microsoft Agent Frameworkista:

- **Agentit**. Agentti luodaan `FoundryChatClient`-luokan kautta ja määritellään nimellä, ohjeilla ja työkaluilla. Agentti voi:
  - **Käsitellä käyttäjän viestejä** ja luoda vastauksia Azure OpenAI -malleilla.
  - **Kutsua työkaluja** automaattisesti keskustelukontekstin perusteella.
  - **Ylläpitää keskustelutilaa** useiden vuorovaikutusten ajan.

  Tässä on koodipätkä agentin luomisesta:

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

- **Työkalut**. Kehys tukee työkalujen määrittelyä Python-funktioina, joita agentti voi kutsua automaattisesti. Työkalut rekisteröidään agenttia luotaessa:

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

- **Moni-agenttien koordinointi**. Voit luoda useita agentteja eri erikoistumisilla ja koordinoida niiden työtä:

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

- **Azure-identiteetin integraatio**. Kehys käyttää `AzureCliCredential`- tai `DefaultAzureCredential`-toteutuksia varmassa, avainta vailla olevassa todennuksessa, mikä poistaa API-avainten suoran hallinnan tarpeen.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service on uudempaa teknologiaa, julkaistu Microsoft Ignite 2024 -tapahtumassa. Se mahdollistaa tekoälyagenttien kehittämisen ja käyttöönoton joustavammilla malleilla, kuten suoraan avoimen lähdekoodin LLM-mallien (esim. Llama 3, Mistral, Cohere) kutsumisella.

Microsoft Foundry Agent Service tarjoaa vahvempia yritystason suojausmekanismeja ja tietovarastointimenetelmiä, mikä tekee siitä sopivan yrityskäyttöön.

Se toimii saumattomasti Microsoft Agent Frameworkin kanssa agenttien rakentamisessa ja käyttöönotossa.

Tämä palvelu on tällä hetkellä julkisessa esikatseluvaiheessa ja tukee agenttien rakentamista Pythonilla ja C#:lla.

Microsoft Foundry Agent Service Python SDK:n avulla voimme luoda agentin käyttäjän määrittelemällä työkalulla:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Määritä työkalutoiminnot
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
        model="gpt-5-mini",
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

Microsoft Foundry Agent Servicellä on seuraavat keskeiset käsitteet:

- **Agentti**. Microsoft Foundry Agent Service integroituu Microsoft Foundryyn. Microsoft Foundryn sisällä tekoälyagentti toimii "älykkäänä" mikropalveluna, jota voidaan käyttää kysymyksiin vastaamiseen (RAG), toimintojen suorittamiseen tai työnkulkujen täydelliseen automatisointiin. Tämä onnistuu yhdistämällä generatiivisten AI-mallien voima työkaluihin, jotka mahdollistavat pääsyn todellisiin tietolähteisiin ja niiden kanssa vuorovaikutuksen. Tässä on esimerkki agentista:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Tässä esimerkissä agentti luodaan mallilla `gpt-5-mini`, nimellä `my-agent` ja ohjeilla `You are helpful agent`. Agentti on varustettu työkaluilla ja resursseilla koodin tulkkaustehtävien suorittamiseen.

- **Keskusteluketju ja viestit**. Keskusteluketju on myös tärkeä konsepti. Se edustaa vuorovaikutusta agentin ja käyttäjän välillä. Ketjuja voi käyttää keskustelun etenemisen seuraamiseen, kontekstin tallentamiseen ja vuorovaikutuksen tilan hallintaan. Tässä on esimerkki ketjusta:

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

    Edellisessä koodissa ketju luodaan. Sen jälkeen ketjuun lähetetään viesti. Kutsumalla `create_and_process_run` agentilta pyydetään työskentelemään ketjussa. Lopuksi viestit haetaan ja kirjataan vastauksen näkemiseksi. Viestit ilmaisevat vuorovaikutuksen etenemisen käyttäjän ja agentin välillä. On myös tärkeää ymmärtää, että viestit voivat olla erilaisia tyyppiltään, kuten tekstiä, kuvaa tai tiedostoa, mikä tarkoittaa että agentin työ tuottaa esimerkiksi kuvan tai tekstivastauksen. Kehittäjänä voit käyttää tätä tietoa edelleen vastauksen käsittelyyn tai esittämiseen käyttäjälle.

- **Integroituu Microsoft Agent Frameworkiin**. Microsoft Foundry Agent Service toimii saumattomasti Microsoft Agent Frameworkin kanssa, mikä tarkoittaa että voit rakentaa agenteja `FoundryChatClient` -luokalla ja ottaa ne käyttöön Agent Service:n kautta tuotantotilanteissa.

**Käyttötapaukset**: Microsoft Foundry Agent Service on suunniteltu yrityssovelluksiin, jotka vaativat turvallista, skaalautuvaa ja joustavaa tekoälyagenttien käyttöönottoa.

## Mikä on ero näiden lähestymistapojen välillä?
 
Vaikka vaikutteleekin siltä, että on päällekkäisyyttä, on muutamia keskeisiä eroja niiden suunnittelussa, kyvykkyyksissä ja kohdesovelluksissa:
 
- **Microsoft Agent Framework (MAF)**: Tuotantovalmis SDK tekoälyagenttien rakentamiseen. Tarjoaa virtaviivaistetun API:n agenttien luomiseen, työkalukutsuihin, keskustelun hallintaan ja Azure-identiteetin integraatioon.
- **Microsoft Foundry Agent Service**: On alusta ja käyttöönotopalvelu Microsoft Foundryssa agenteille. Tarjoaa sisäänrakennetun yhteyden palveluihin, kuten Azure OpenAI, Azure AI Search, Bing Search ja koodin suorituksen.
 
Etkö ole vielä varma, kumpaan valita?

### Käyttötapaukset
 
Käydään läpi yleisiä käyttötapauksia, joilla voimme auttaa sinua:
 
> K: Rakennan tuotantovalmiita tekoälyagenttisovelluksia ja haluan päästä nopeasti alkuun
>

> V: Microsoft Agent Framework on erinomainen valinta. Se tarjoaa yksinkertaisen, Python-tyyppisen API:n `FoundryChatClient` kautta, jolla voit määrittää agentteja työkaluineen ja ohjeineen muutamassa koodirivissä.

> K: Tarvitsen yritystason käyttöönoton Azure-integraatioilla kuten Search ja koodin suoritus
>
> V: Microsoft Foundry Agent Service on paras valinta. Se on alusta-palvelu, joka tarjoaa sisäänrakennetut ominaisuudet useille malleille, Azure AI Searchille, Bing Searchille ja Azure Functionsille. Sen avulla voit helposti rakentaa agentteja Foundry-portaalissa ja ottaa niitä käyttöön laajasti.
 
> K: Olen edelleen epävarma, anna minulle yksi vaihtoehto
>
> V: Aloita Microsoft Agent Frameworkilla agenttien rakentamiseen ja käytä Microsoft Foundry Agent Serviceä, kun haluat ottaa agentit käyttöön tuotannossa ja skaalata niitä. Tämä lähestymistapa mahdollistaa nopean iteroinnin agenttilogiikassa ja selkeän polun yrityskäyttöönottoon.
 
Yhteenvetona avain-erot taulukossa:

| Kehys | Fokus | Keskeiset käsitteet | Käyttötapaukset |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Virtaviivaistettu agenttien SDK työkalukutsulla | Agentit, Työkalut, Azure-identiteetti | Tekoälyagenttien rakentaminen, työkalujen käyttö, monivaiheiset työnkulut |
| Microsoft Foundry Agent Service | Joustavat mallit, yritystason suojaus, koodin generointi, työkalukutsu | Modulariteetti, Yhteistyö, Prosessien orkestrointi | Turvallinen, skaalautuva ja joustava tekoälyagenttien käyttöönotto |

## Voinko integroida olemassa olevat Azure-ekosysteemini työkalut suoraan vai tarvitseeko erillisiä ratkaisuja?


Vastaus on kyllä, voit integroida olemassa olevat Azure-ekosysteemisi työkalut suoraan Microsoft Foundry Agent Serviceen, erityisesti koska se on rakennettu toimimaan saumattomasti muiden Azure-palveluiden kanssa. Voisit esimerkiksi integroida Bingin, Azure AI Searchin ja Azure Functionit. Microsoft Foundryn kanssa on myös syvä integraatio.

Microsoft Agent Framework integroituu myös Azure-palveluihin `FoundryChatClient`-rajapinnan ja Azure-identiteetin kautta, jolloin voit kutsua Azure-palveluja suoraan agenttityökaluistasi.

## Esimerkkikoodit

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Onko sinulla lisää kysymyksiä AI Agent Frameworkeista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia AI-agentteihin liittyviin kysymyksiisi.

## Viitteet

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Edellinen Oppitunti

[Johdanto AI-agentteihin ja agentin käyttötapauksiin](../01-intro-to-ai-agents/README.md)

## Seuraava Oppitunti

[Agenttiperäisten suunnittelumallien ymmärtäminen](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->