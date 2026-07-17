[![AI Agent Raamistike uurimine](../../../translated_images/et/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klõpsake ülaloleval pildil, et vaadata selle õppetunni videot)_

# Uurige AI Agent Raamistikke

AI agentide raamistikke on loodud tarkvaraplatvormidena, mis lihtsustavad AI agentide loomist, juurutamist ja haldamist. Need raamistike pakuvad arendajatele eelkokkupandud komponente, abstraktsioone ja tööriistu, mis sujuvamaks muudavad keerukate AI süsteemide arendamise.

Need raamistikke aitavad arendajatel keskenduda oma rakenduste unikaalsetele aspektidele, pakkudes standardiseeritud lähenemisviise AI agentide arendamise tavapärastele väljakutsetele. Need parandavad AI süsteemide skaleeritavust, kättesaadavust ja tõhusust.

## Sissejuhatus

Selles õppetunnis käsitleme:

- Mis on AI Agent Raamistikud ja mida need arendajatele võimaldavad saavutada?
- Kuidas saavad meeskonnad neid kasutada, et kiiresti prototüüpida, iteratiivselt täiustada ja parandada oma agendi võimeid?
- Millised on erinevused Microsofti loodud raamistike ja tööriistade vahel (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> ja <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Kas saan oma olemasolevaid Azure ökosüsteemi tööriistu otse integreerida või on vaja iseseisvaid lahendusi?
- Mis on Microsoft Foundry Agent Service ja kuidas see mind aitab?

## Õpieesmärgid

Selle õppetunni eesmärk on aidata teil mõista:

- AI Agent Raamistike rolli AI arenduses.
- Kuidas kasutada AI Agent Raamistikke intelligentsete agentide loomiseks.
- AI Agent Raamistike võimaldavaid peamisi võimeid.
- Microsoft Agent Frameworki ja Microsoft Foundry Agent Service'i erinevusi.

## Mis on AI Agent Raamistikud ja mida need arendajatele võimaldavad teha?

Traditsioonilised AI raamistikke aitavad teil AI-d oma rakendustesse integreerida ja parendada järgmiste viiside kaudu:

- **Personaliseerimine**: AI suudab analüüsida kasutajakäitumist ja eelistusi, et pakkuda isikupärastatud soovitusi, sisu ja kogemusi.
Näide: Filmipleieriteenused nagu Netflix kasutavad AI-d filmide ja saadete soovitamiseks vaatamishoo põhjal, suurendades kasutajate kaasatust ja rahulolu.
- **Automatiseerimine ja tõhusus**: AI saab automatiseerida korduvaid ülesandeid, sujuvamalt korraldada töövooge ja parandada tegevuste efektiivsust.
Näide: Klienditeenindusäpikaid kasutavad AI-põhised vestlusrobotid, mis käsitlevad tavalisi päringuid, vähendades vastamisaegu ja vabastades inimagente keerukamate probleemide lahendamiseks.
- **Täiustatud kasutajakogemus**: AI parandab üldist kasutajakogemust, pakkudes nutikaid funktsioone nagu hääletuvastus, loomuliku keele töötlemine ja ennustav tekst.
Näide: Virtuaalsed assistendid nagu Siri ja Google Assistant kasutavad AI-d, et mõista ja reageerida häälkäsklustele, muutes kasutajate seadmetega suhtlemise lihtsamaks.

### See kõik kõlab suurepäraselt, miks siis on vaja AI Agent Raamistikku?

AI Agent raamistikud tähistavad midagi enamat kui lihtsalt AI raamistikke. Need on loodud võimaldama intelligentsete agentide loomist, kes saavad suhelda kasutajate, teiste agentide ja keskkonnaga kindlate eesmärkide saavutamiseks. Need agentid suudavad näidata autonoomset käitumist, teha otsuseid ja kohaneda muutuvate tingimustega. Vaatame mõningaid peamisi AI Agent Raamistike võimalusi:

- **Agentide koostöö ja koordineerimine**: Võimaldab luua mitmeid AI agente, kes saavad koos töötada, suhelda ja koordineerida keerukate ülesannete lahendamist.
- **Ülesannete automatiseerimine ja juhtimine**: Pakub mehhanisme mitmeastmeliste töövoogude automatiseerimiseks, ülesannete delegeerimiseks ja dünaamiliseks ülesannete haldamiseks agentide vahel.
- **Kontekstiline mõistmine ja kohandumine**: Varustab agente võimega mõista konteksti, kohaneda muutuvate keskkondadega ja teha otsuseid reaalajas info põhjal.

Kokkuvõttes lubavad agentid teil teha rohkem, viia automatiseerimine järgmisele tasemele ja luua targemaid süsteeme, mis suudavad kohaneda ja õppida oma keskkonnast.

## Kuidas kiiresti prototüüpida, iteratiivselt täiustada ja parandada agendi võimeid?

See on kiirelt arenev valdkond, kuid enamik AI Agent Raamistikke jagavad mõningaid ühiseid elemente, mis aitavad teil kiiresti prototüüpida ja iteratiivselt täiustada — nimelt moodulkomponendid, koostööriistad ja reaalajas õppimine. Vaatame neid lähemalt:

- **Kasutage moodulkomponente**: AI SDK-d pakuvad eelnevalt loodud komponente nagu AI ja mälu ühendused, funktsioonikõned loomulikus keeles või koodipistikute abil, promptide mallid ja muud.
- **Kasutage koostööriistu**: Kavandage agente kindlate rollide ja ülesannetega, võimaldades neil testida ja täiustada koostöö töövooge.
- **Õppige reaalajas**: Rakendage tagasisidel silmuseid, kus agentide käitumist kohandatakse dünaamiliselt vastavalt suhtlusele.

### Kasutage moodulkomponente

Sellised SDK-d nagu Microsoft Agent Framework pakuvad eelvalmis komponente nagu AI ühendajad, tööriistade definitsioonid ja agentide haldus.

**Kuidas meeskonnad saavad neid kasutada**: Meeskonnad saavad kiiresti kokku panna need komponendid funktsionaalseks prototüübiks ilma nullist alustamata, võimaldades kiiret katsetamist ja iteratsiooni.

**Praktiline toimimine**: Võite kasutada eelkokkupandud parserit info väljavõtmiseks kasutajasisendist, mälumoodulit andmete salvestamiseks ja tagasisaamiseks ning promptigeneraatorit kasutajatega suhtlemiseks, ilma et peaksite neid komponente algusest peale looma.

**Näidiskood**: Vaatame näidet, kuidas kasutada Microsoft Agent Frameworki koos `FoundryChatClient`-iga, et mudel vastaks kasutajasisendile tööriista kutsumiseks:

``` python
# Microsoft Agendi Raamistiku Pythoni Näide

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Määra näidistööriista funktsioon reisi broneerimiseks
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
    # Näiteväljund: Teie lend New Yorki 1. jaanuaril 2025 on edukalt broneeritud. Head reisi! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Sellest näitest näete, kuidas saate kasutada eelkokkupandud parserit, et väljavõtta võtmeinfo kasutajasisendist, nagu lennubronni päritolu, sihtkoht ja kuupäev. See moodulipõhine lähenemine võimaldab teil keskenduda kõrgetasemelisele loogikale.

### Kasutage koostööriistu

Microsoft Agent Framework võimaldab luua mitut agenti, kes saavad koos töötada.

**Kuidas meeskonnad saavad neid kasutada**: Meeskonnad võivad kujundada agente spetsiifiliste rollide ja ülesannetega, võimaldades testida ja täiustada koostöö töövooge ning parandada süsteemi üldist efektiivsust.

**Praktiline toimimine**: Võite luua agentide meeskonna, kus igal agendil on spetsialiseerunud funktsioon, näiteks andmete hankimine, analüüs või otsustusprotsess. Need agentid suudavad omavahel suhelda ja infot jagada ühise eesmärgi, näiteks kasutajaküsimusele vastamise või ülesande täitmise nimel.

**Näidiskood (Microsoft Agent Framework)**:

```python
# Mitme agenti loomine, kes töötavad koos, kasutades Microsoft Agent Frameworki

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Andmete pärimise agent
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Andmete analüüsi agent
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Agentide järjestikune käivitamine ülesandel
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Eelnevast koodist näete, kuidas luua ülesanne, mis hõlmab mitut agenti, kes koos analüüsivad andmeid. Iga agent täidab kindlat funktsiooni ning ülesanne viiakse ellu agentide koordineerimisega soovitud tulemuse saavutamiseks. Pühendunud rollidega agentide loomisega saate parandada ülesannete tõhusust ja tulemuslikkust.

### Õppige reaalajas

Täiustatud raamistikel on võimekus reaalajas konteksti mõistmiseks ja kohanemiseks.

**Kuidas meeskonnad saavad neid kasutada**: Meeskonnad saavad rakendada tagasiside silmuseid, kus agentide käitumist kohandatakse dünaamiliselt suhtluse põhjal, mis viib pideva täiustamiseni ja võimete arendamisse.

**Praktiline toimimine**: Agentide poolt analüüsitakse kasutajate tagasisidet, keskkonnast kogutud andmeid ja ülesannete tulemusi, et uuendada oma teadmistebaasi, kohandada otsustusalgoritme ja parandada aja jooksul tulemuslikkust. See iteratiivne õppimisprotsess võimaldab agentidel kohaneda muutuvate tingimuste ja kasutajate eelistustega, parandades süsteemi üldist efektiivsust.

## Millised on erinevused Microsoft Agent Frameworki ja Microsoft Foundry Agent Service'i vahel?

Neid lähenemisi saab võrrelda mitmel moel, kuid vaatame mõningaid peamisi erinevusi nende disaini, võimekuste ja sihtkasutuse seisukohast:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework pakub sujuvat SDK-d AI agentide loomiseks kasutades `FoundryChatClient`-i. See lubab arendajatel luua agente, kes kasutavad Azure OpenAI mudeleid sisseehitatud tööriistade kutsumisega, vestluse juhtimise ja ettevõtte taseme turvalisusega Azure identiteedi kaudu.

**Kasutusjuhtumid**: Tootmiskõlbulike AI agentide loomine tööriistade kasutamise, mitmeastmeliste töövoogude ja ettevõtte integratsiooni stsenaariumite jaoks.

Siin on mõned Microsoft Agent Frameworki olulised põhimõisted:

- **Agendid**. Agent luuakse `FoundryChatClient` abil ning see konfigureeritakse nime, juhiste ja tööriistadega. Agent saab:
  - **Töödelda kasutajate sõnumeid** ja genereerida vastuseid Azure OpenAI mudelite abil.
  - **Kutsuda tööriistu** automaatselt vastavalt vestluse kontekstile.
  - **Hoidke vestluse olekut** mitme suhtluse jooksul.

  Siin on koodinäide, mis näitab, kuidas agenti luua:

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

- **Tööriistad**. Raamistik toetab tööriistade defineerimist Python funktsioonidena, mida agent saab automaatselt kutsuda. Tööriistad registreeritakse agendi loomisel:

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

- **Mitme agendi koordineerimine**. Võite luua mitmeid agente, kellel on erinevad spetsialiseerumised ja koordineerida nende tööd:

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

- **Azure identiteedi integratsioon**. Raamistik kasutab `AzureCliCredential` (või `DefaultAzureCredential`) turvalise ja võtmevaba autentimise jaoks, mis kõrvaldab vajaduse API võtmete otse haldamiseks.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service on hiljutine täiendus, mis tutvustati Microsoft Ignite 2024 sündmusel. See võimaldab arendada ja juurutada AI agente paindlikumate mudelitega, näiteks otse kutsudes avatud lähtekoodiga LLM-e nagu Llama 3, Mistral ja Cohere.

Microsoft Foundry Agent Service pakub tugevamaid ettevõtte turvamehhanisme ja andmete säilitamise meetodeid, muutes selle sobivaks ettevõtterakendustele.

See töötab Microsoft Agent Frameworkiga koostöös agendide ehitamiseks ja juurutamiseks.

Teenus on praegu avalikus eelvaates ja toetab Pythonit ja C#-i agentide loomisel.

Microsoft Foundry Agent Service Python SDK abil saame luua agendi kasutaja määratud tööriistaga:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Määratle tööriistade funktsioonid
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
        model="gpt-4.1-mini",
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

### Põhimõisted

Microsoft Foundry Agent Service'l on järgmised põhimõisted:

- **Agent**. Microsoft Foundry Agent Service integreerub Microsoft Foundry keskkonnaga. Microsoft Foundry sees tegutseb AI agent kui "nutikas" mikroteenus, mida saab kasutada küsimustele vastamiseks (RAG), tegevuste sooritamiseks või töövoogude täielikuks automatiseerimiseks. Seda saavutatakse kombineerides generatiivsete AI mudelite võime tööriistadega, mis võimaldavad ligipääsu ja interaktsiooni reaalsete andmeallikatega. Siin on näide agendist:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Selles näites luuakse agent mudeliga `gpt-4.1-mini`, nimega `my-agent` ja juhistega `You are helpful agent`. Agent on varustatud tööriistade ja ressurssidega, et täita koodi interpreteerimise ülesandeid.

- **Jutuajamine ja sõnumid**. Jutuajamine on teine oluline mõiste. See esindab vestlust või suhtlust agenti ja kasutaja vahel. Jutuajamisi kasutatakse vestluse edenemise jälgimiseks, kontekstiinfo salvestamiseks ja suhtluse oleku haldamiseks. Siin on näide jutuajamisest:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Palu agendil lõimel tööd teha
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Hangi ja logi kõik sõnumid, et näha agendi vastust
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Eelnevas koodis luuakse jutuajamine. Seejärel saadetakse sõnum jutuajamisse. Kõne `create_and_process_run` abil palutakse agendil jutuajamise kallal töötada. Lõpuks tõmmatakse sõnumid ja logitakse agendi vastuse nägemiseks. Sõnumid näitavad vestluse edenemist kasutaja ja agendi vahel. On oluline mõista, et sõnumid võivad olla erinevat tüüpi nagu tekst, pilt või fail, mis tähendab, et agentide töö on toonud tulemuseks näiteks pildi või tekstilise vastuse. Arendajana saate seda infot kasutada vastuse edasiseks töötlemiseks või kasutajale esitamiseks.

- **Integreerub Microsoft Agent Frameworkiga**. Microsoft Foundry Agent Service töötab sujuvalt koos Microsoft Agent Frameworkiga, mis tähendab, et saate luua agente `FoundryChatClient` abil ja juurutada neid Agent Service'i kaudu tootmises.

**Kasutusjuhtumid**: Microsoft Foundry Agent Service on loodud ettevõtte rakendustele, mis vajavad turvalist, skaleeritavat ja paindlikku AI agentide juurutamist.

## Milline on nende kahe lähenemise vahe?
 
See võib tunduda kattuvana, kuid disaini, võimekuste ja sihtotstarbe seisukohast on mõned võtmer erinevused:
 
- **Microsoft Agent Framework (MAF)**: On tootmiskõlbulik SDK AI agentide loomiseks. Pakub sujuvat API-t agentide loomiseks tööriistade kasutamise, vestluse juhtimise ja Azure identiteedi integreerimisega.
- **Microsoft Foundry Agent Service**: On platvorm ja juurutusteenus Microsoft Foundrys agentidele. Pakub sisseehitatud ühenduvust teenustega nagu Azure OpenAI, Azure AI Search, Bing Search ja koodi täitmine.
 
Kas pole siiski kindel, kumba valida?

### Kasutusjuhtumid
 
Vaatame, kas suudame aidata mõningate tavakasutusjuhtumite kaudu:
 
> K: Ma loon tootmiskõlblikke AI agentide rakendusi ja soovin kiiresti alustada
>

>V: Microsoft Agent Framework on suurepärane valik. See pakub lihtsat ja pythonilikku API-d `FoundryChatClient` kaudu, mis võimaldab teil määratleda agente tööriistade ja juhistega vaid mõne koodireaga.

>K: Vajan ettevõtte tasemel juurutust Azure integratsioonidega nagu Search ja koodi täitmine
>
> V: Microsoft Foundry Agent Service on parim valik. See on platvormiteenus, mis pakub sisseehitatud võimekusid mitmete mudelite toetamiseks, Azure AI Search, Bing Search ja Azure Functions. See teeb agendide loomise Foundry portaalis ja nende skaalaühendamise lihtsaks.
 
> K: Olen endiselt segaduses, anna mulle lihtsalt üks variant
>
> V: Alusta Microsoft Agent Frameworkiga agentide loomiseks ja kasuta Microsoft Foundry Agent Service'i, kui vajad tootmises juurutamist ja skaleerimist. See lähenemine laseb teil agentide loogikat kiiresti iteratiivselt arendada, hoides samal ajal selge tee ettevõtte juurutamiseks.
 
Lõpetuseks võtame võtmetähtsusega erinevused kokku tabelis:

| Raamistik | Fookus | Põhimõttelised mõisted | Kasutusjuhtumid |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Sujuv agentide SDK tööriistade kutsumisega | Agendid, Tööriistad, Azure identiteet | AI agentide loomine, tööriistad, mitmeastmelised töövood |
| Microsoft Foundry Agent Service | Paindlikud mudelid, ettevõtte turvalisus, koodi genereerimine, tööriistade kutsumine | Moodulisus, Koostöö, Protsessi orkestreerimine | Turvaline, skaleeritav ja paindlik AI agentide juurutus |

## Kas saan oma olemasolevaid Azure ökosüsteemi tööriistu otse integreerida või on vaja iseseisvaid lahendusi?


Vastus on jah, saate oma olemasolevad Azure'i ökosüsteemi tööriistad integreerida otse Microsoft Foundry Agent Service'iga, eriti kuna see on loodud sujuvaks koostööks teiste Azure'i teenustega. Näiteks võiksite integreerida Bing, Azure AI Search ja Azure Functions. Samuti on sügav integratsioon Microsoft Foundry'ga.

Microsoft Agent Framework integreerub ka Azure'i teenustega läbi `FoundryChatClient` ja Azure identiteedi, võimaldades teil kutsuda Azure'i teenuseid otse oma agendi tööriistadest.

## Näidiskoodid

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Kas sul on rohkem küsimusi AI agendi raamistikute kohta?

Liitu [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppuritega, osaleda kontoritundides ja saada vastuseid oma AI agentide küsimustele.

## Viited

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Eelmine õppetund

[Sissejuhatus AI agentidesse ja agentide kasutusjuhtumitesse](../01-intro-to-ai-agents/README.md)

## Järgmine õppetund

[Agentsete disainimustrite mõistmine](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->