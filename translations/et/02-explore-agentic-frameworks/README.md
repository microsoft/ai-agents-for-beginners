[![Tehisintellekti agentide raamistikud](../../../translated_images/et/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klõpsa ülaloleval pildil, et vaadata selle õppetunni videot)_

# Uuri AI agentide raamistikuid

AI agentide raamistikud on tarkvaraplatvormid, mis on loodud lihtsustama AI agentide loomist, juurutamist ja haldamist. Need raamistikud pakuvad arendajatele eelvalmistatud komponente, abstraktsioone ja tööriistu, mis hõlbustavad keerukate AI süsteemide arendamist.

Need raamistikud aitavad arendajatel keskenduda oma rakenduste unikaalsetele aspektidele, pakkudes standardiseeritud lahendusi AI agentide arendamise levinud väljakutsetele. Need parandavad skaleeritavust, kasutajasõbralikkust ja tõhusust AI süsteemide loomisel.

## Sissejuhatus 

Selles õppetunnis käsitletakse:

- Mis on AI agentide raamistikud ja mida need arendajatele võimaldavad?
- Kuidas meeskonnad saavad neid kasutada, et kiiresti prototüüpida, iteratiivselt arendada ja parandada oma agentide võimekust?
- Millised on Microsofti loodud raamistikute ja tööriistade erinevused (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> ja <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) vahel?
- Kas ma saan oma olemasolevaid Azure ökoloogias tööriistu otse integreerida või on vaja eraldiseisvaid lahendusi?
- Mis on Microsoft Foundry Agent Service ja kuidas see mind aitab?

## Õpieesmärgid

Selle õppetunni eesmärk on aidata sul mõista:

- AI agentide raamistike rolli AI arenduses.
- Kuidas kasutada AI agentide raamistikku intelligentsete agentide loomisel.
- AI agentide raamistike võimaldavaid võtmevõimeid.
- Erinevusi Microsoft Agent Frameworki ja Microsoft Foundry Agent Service vahel.

## Mis on AI agentide raamistikud ja mida need arendajatele võimaldavad teha?

Traditsioonilised AI raamistikud aitavad sul integreerida tehisintellekti oma rakendustesse ja teha need rakendused paremaks järgmiselt:

- **Isikupärastamine**: AI suudab analüüsida kasutaja käitumist ja eelistusi, et pakkuda isikupärastatud soovitusi, sisu ja kogemusi.
Näide: Voogedastusteenused nagu Netflix kasutavad AI-d soovituste tegemiseks filmide ja saadete osas vaadatud ajaloo põhjal, suurendades kasutajate kaasatust ja rahulolu.
- **Automatiseerimine ja tõhusus**: AI suudab automatiseerida korduvaid ülesandeid, lihtsustada töövooge ja parandada tegevuste efektiivsust.
Näide: Klienditeeninduse rakendused kasutavad AI-põhiseid vestlusrobotid, et käsitleda sagedasemaid päringuid, vähendades reageerimisaegu ja vabastades inimagente keerukamate probleemide jaoks.
- **Parandatud kasutajakogemus**: AI parandab üldist kasutajakogemust, pakkudes nutikaid funktsioone, nagu häälituvastus, loomulik keele töötlemine ja ennustav tekst.
Näide: Virtuaalsed assistendid nagu Siri ja Google Assistant kasutavad AI-d häälkäskluste mõistmiseks ja neile vastamiseks, muutes kasutajate suhtlemise seadmetega lihtsamaks.

### See kõik kõlab suurepäraselt, miks siis meil on vaja AI agentide raamistikku?

AI agentide raamistikud on rohkem kui lihtsalt AI raamistikud. Need on loodud võimaldamaks intelligentsete agentide loomist, kes saavad suhelda kasutajate, teiste agentide ja keskkonnaga konkreetsete eesmärkide saavutamiseks. Need agentid suudavad näidata autonoomset käitumist, teha otsuseid ja kohanduda muutuvate tingimustega. Vaatame mõningaid AI agentide raamistike võimalikke võtmevõimeid:

- **Agentide koostöö ja koordineerimine**: Võimaldavad luua mitmeid AI agente, kes saavad koos töötada, suhelda ja koordineerida keerukate ülesannete lahendamiseks.
- **Ülesannete automatiseerimine ja haldamine**: Pakuvad mehhanisme mitmeastmeliste töövoogude automatiseerimiseks, ülesannete delegeerimiseks ja dünaamiliseks juhtimiseks agentide vahel.
- **Kontekstipõhine mõistmine ja kohanemine**: Varustavad agente võimega mõista konteksti, kohanduda muutuvate keskkondadega ja teha otsuseid reaalajas saadaval oleva info põhjal.

Kokkuvõtteks võimaldavad agentide raamistikud sul teha rohkem, viia automatiseerimine uuele tasemele ning luua intelligentsemaid süsteeme, mis suudavad keskkonnast õppida ja kohaneda.

## Kuidas kiiresti prototüüpida, iteratiivselt arendada ja parandada agendi võimekust?

See valdkond areneb kiiresti, kuid enamikus AI agentide raamistikutes on mõned ühised osad, mis aitavad sul kiirelt prototüüpida ja iteratiivselt edasi liikuda — nimelt moodulkomponendid, koostöövahendid ja reaalajas õppimine. Vaatame neid lähemalt:

- **Kasuta moodulkomponente**: AI SDK-d pakuvad eelvalmistatud komponente nagu AI ja mälu liidesed, funktsioonide kutsumine loomulikus keeles või koodipistikute kaudu, käsupõhjad ja muud.
- **Kasuta koostöövahendeid**: Disaini agente kindlate rollide ja ülesannetega, võimaldades neil testida ja täiustada koostöö töövooge.
- **Õpi reaalajas**: Rakenda tagasisideahelad, kus agent õpib suhtlusest ja kohandab käitumist dünaamiliselt.

### Kasuta moodulkomponente

SDK-d nagu Microsoft Agent Framework pakuvad eelvalmistatud komponente nagu AI liidesed, tööriistade definitsioonid ja agentide haldus.

**Kuidas meeskonnad saavad neid kasutada**: Meeskonnad saavad kiiresti kokku panna need komponendid tööprototüübi loomiseks ilma nullist alustamata, võimaldades kiiret katsetamist ja iteratsiooni.

**Kuidas see praktikas toimib**: Sa võid kasutada eelvalmistatud parserit, et ekstraktida teavet kasutaja sisendist, mälumoodulit andmete talletamiseks ja hankimiseks ning käsu generaatorit kasutajatega suhtlemiseks, kõike seda ilma komponentide nullist ehitamiseta.

**Näidiskood**. Vaatame näidet, kuidas Microsoft Agent Frameworki kasutada koos `FoundryChatClient`-iga, et mudel saaks vastata kasutaja päringule tööriista kutsumise abil:

``` python
# Microsoft Agent Framework Python Näide

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Määra näidis tööriista funktsioon reisi broneerimiseks
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
    # Näidise väljund: Teie lend New Yorki 1. jaanuaril 2025 on edukalt broneeritud. Head reisi! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Sellest näitest näed, kuidas saad kasutada eelvalmistatud parserit võtmeinfo eraldamiseks kasutaja sisendist, näiteks lennu broneerimise päritolu, sihtkoha ja kuupäeva. See moodulipõhine lähenemine võimaldab sul keskenduda kõrgetasemelisele loogikale.

### Kasuta koostöövahendeid

Raamistikud nagu Microsoft Agent Framework võimaldavad luua mitu agenti, kes saavad koos töötada.

**Kuidas meeskonnad saavad neid kasutada**: Meeskonnad saavad disainida agente kindlate rollide ja ülesannetega, võimaldades neil testida ja täiustada koostöö töövooge ning parandada süsteemi üldist tõhusust.

**Kuidas see praktikas toimib**: Võid luua agentide meeskonna, kus igal agentil on spetsialiseerunud funktsioon, näiteks andmete hankimine, analüüs või otsuste tegemine. Need agentid suhtlevad ja jagavad informatsiooni, et saavutada ühine eesmärk, näiteks kasutajapäringu vastamine või ülesande täitmine.

**Näidiskood (Microsoft Agent Framework)**:

```python
# Mitme agenti loomine, kes töötavad koos Microsoft Agent Frameworki abil

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Andmete hankimise agent
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Andmeanalüüsi agent
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Agentide järjestikune käivitamine ülesande täitmiseks
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Eelnevas koodis näed, kuidas luua ülesanne, mis hõlmab mitme agendi koostööd andmete analüüsimisel. Iga agent täidab konkreetset funktsiooni ja ülesanne teostatakse, koordineerides agente soovitud tulemuse saavutamiseks. Spetsialiseerunud agentide loomisega saad parandada ülesande efektiivsust ja tulemuslikkust.

### Õpi reaalajas

Täiustatud raamistikud pakuvad võimekust konteksti mõistmiseks ja kohanemiseks reaalajas.

**Kuidas meeskonnad saavad neid kasutada**: Meeskonnad saavad rakendada tagasisideahelad, kus agentid õpivad suhtlustest ja kohandavad oma käitumist dünaamiliselt, mis viib võimekuse pidevale parandamisele ja täiendamisele.

**Kuidas see praktikas toimib**: Agendid analüüsivad kasutajate tagasisidet, keskkonnaandmeid ja ülesannete tulemusi, et uuendada oma teadmistebaasi, kohandada otsustusalgoritme ja parandada sooritust aja jooksul. See iteratiivne õppimisprotsess võimaldab agentidel kohaneda muutuvate tingimuste ja kasutajate eelistustega, tugevdades süsteemi üldist efektiivsust.

## Millised on erinevused Microsoft Agent Frameworki ja Microsoft Foundry Agent Service vahel?

Nende lähenemiste võrdlemiseks on palju võimalusi, kuid vaatame mõningaid olulisi erinevusi nende disaini, võimekuste ja sihtkasutuse osas:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework pakub sujuvat SDK-d AI agentide ehitamiseks kasutades `FoundryChatClient`-i. See võimaldab arendajatel luua agente, kes kasutavad Azure OpenAI mudeleid koos sisseehitatud tööriistade kutsumise, vestluse halduse ja äriklassi turvalisusega Azure identiteedi kaudu.

**Kasutusjuhtumid**: Tootmisklassi valmis AI agentide ehitamine tööriistade kasutamise, mitmest kergest töövoost ja ettevõtte integreerimisdomeenidega.

Siin on mõned Microsoft Agent Frameworki olulised põhimõisted:

- **Agendid**. Agent luuakse `FoundryChatClient` abil ja konfigureeritakse nime, juhiste ja tööriistadega. Agent suudab:
  - **Kasutajate sõnumeid töödelda** ja genereerida vastuseid Azure OpenAI mudelite abil.
  - **Tööriistu kutsuda** automaatselt vestluse konteksti põhjal.
  - **Vestluse seisundit hoida** mitme suhtluse vältel.

  Siin on koodinäide, kuidas agenti luua:

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

- **Tööriistad**. Raamistik toetab tööriistade defineerimist Python funktsioonidena, mida agent saab automaatselt kutsuda. Tööriistad registreeritakse agenti loomisel:

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

- **Mitme agendi koordineerimine**. Võid luua mitu agenti erinevate spetsialiseerumistega ja koordineerida nende tööd:

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

- **Azure identiteedi integratsioon**. Raamistik kasutab turvaliseks, võtmevabaks autentimiseks `AzureCliCredential`-i (või `DefaultAzureCredential`-i), kõrvaldades vajaduse API võtmete otseseks haldamiseks.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service on hiljutine täiendus, mis esitleti Microsoft Ignite 2024 üritusel. See võimaldab AI agentide arendamist ja juurutamist paindlikemate mudelitega, näiteks kutsudes otse avatud lähtekoodiga LLM-e nagu Llama 3, Mistral ja Cohere.

Microsoft Foundry Agent Service pakub tugevamaid äriklassi turvamehhanisme ja andmete säilitamise meetodeid, mis teevad selle sobivaks ettevõtterakenduseks.

See toimib välja karbist koos Microsoft Agent Frameworkiga, et ehitada ja juurutada agente.

Teenus on praegu avalikus eelvaates ja toetab agentide loomiseks Pythoni ja C# keeli.

Microsoft Foundry Agent Service Pythoni SDK abil saame luua agendi kasutaja määratletud tööriistaga:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Määra tööriistade funktsioonid
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

### Põhikontseptsioonid

Microsoft Foundry Agent Service sisaldab järgmisi põhikontsepte:

- **Agent**. Microsoft Foundry Agent Service integreerub Microsoft Foundryga. Microsoft Foundry sees toimib AI agent „nutika“ mikroteenusena, mida saab kasutada küsimustele vastamiseks (RAG), tegevuste täitmiseks või töövoogude täielikuks automatiseerimiseks. See saavutatakse generatiivsete AI mudelite võimendamisega ja tööriistadega, mis võimaldavad pääseda ligi ja suhelda reaalse andmeallikatega. Siin on näide agendist:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Selles näites luuakse agent mudeli `gpt-5-mini`, nimega `my-agent` ja juhistega `You are helpful agent`. Agent on varustatud tööriistade ja ressurssidega koodi interpreteerimise ülesannete täitmiseks.

- **Vestluslõim ja sõnumid**. Vestluslõim on teine oluline mõiste. See esindab suhtlust või interaktsiooni agendi ja kasutaja vahel. Lõimeid saab kasutada vestluse edenemise jälgimiseks, konteksti info hoidmiseks ja interaktsiooni seisundi haldamiseks. Siin on näide lõimest:

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

    Eelnenud koodis luuakse lõim. Seejärel saadetakse lõimele sõnum. Kutsudes `create_and_process_run`, palutakse agendil lõimes tööd teha. Lõpuks hangitakse sõnumid ja logitakse agendi vastuse nägemiseks. Sõnumid näitavad kasutaja ja agendi vahelist vestluse edenemist. On oluline mõista, et sõnumid võivad olla erinevat tüüpi, nagu tekst, pilt või fail, mis tähendab, et agente töö võib tulemuseks olla näiteks pildi- või tekstipõhine vastus. Arendajana saad kasutada seda infot vastuse edasiseks töötlemiseks või esitamiseks kasutajale.

- **Integreerub Microsoft Agent Frameworkiga**. Microsoft Foundry Agent Service töötab laitmatult koos Microsoft Agent Frameworkiga, mis tähendab, et saad agente ehitada kasutades `FoundryChatClient`-i ja juurutada neid Agent Service'i kaudu tootmiskeskkonda.

**Kasutusjuhtumid**: Microsoft Foundry Agent Service on mõeldud ärirakendustele, mis vajavad turvalist, skaleeritavat ja paindlikku AI agentide juurutamist.

## Mis vahe on nende lähenemiste vahel?
 
Tundub, et on kattuvusi, kuid seal on mõned olulised erinevused nende disaini, võimekuste ja sihtkasutuse osas:
 
- **Microsoft Agent Framework (MAF)**: On tootmisklassi SDK AI agentide ehitamiseks. See pakub sujuvat API-d agentide loomiseks tööriistade kutsumise, vestluse halduse ja Azure identiteedi integratsiooniga.
- **Microsoft Foundry Agent Service**: On Microsoft Foundry platvorm ja juurutusteenus agentidele. Pakub sisseehitatud ühendusi teenustega nagu Azure OpenAI, Azure AI Search, Bing Search ja koodi täitmine.
 
Kas oled endiselt otsustushetkel?

### Kasutusjuhtumid
 
Vaatame, kas saame sind aidata mõningate tavapäraste kasutusjuhtumite toel:
 
> K: Teen tootmisklassi AI agentide rakendust ja tahan kiiresti alustada
>

>V: Microsoft Agent Framework on suurepärane valik. See pakub lihtsat, Pythonile omast API-d `FoundryChatClient` abil, mis võimaldab defineerida agendid tööriistade ja juhistega vaid mõne koodireaga.

>K: Vajan äriklassi juurutust koos Azure integreeringutega nagu Search ja koodi täitmine
>
> V: Microsoft Foundry Agent Service on parim valik. See on platvormiteenus, mis pakub sisseehitatud võimeid mitmete mudelitega, Azure AI Search, Bing Search ja Azure Functions. See muudab agentide ehitamise Foundry portaalis lihtsaks ja nende ulatusliku juurutamise võimalikuks.
 
> K: Olen ikka veel segaduses, anna mulle üks variant
>
> V: Alusta Microsoft Agent Frameworkiga agentide ehitamiseks ja kasuta seejärel Microsoft Foundry Agent Service'i, kui vajad agentide tootmisjuurutust ja skaleerimist. See lähenemine võimaldab sul kiiresti iteratiivselt arendada agendi loogikat ja samal ajal hoida selget teed äriklassi juurutuseks.
 
Kokkuvõtame peamised erinevused tabelis:

| Raamistik | Fookus | Põhikontseptsioonid | Kasutusjuhtumid |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Sujuv agendi SDK koos tööriista kutsumisega | Agendid, tööriistad, Azure identiteet | AI agentide ehitamine, tööriistade kasutamine, mitmeastmelised töövood |
| Microsoft Foundry Agent Service | Paindlikud mudelid, äriklassi turvalisus, koodi genereerimine, tööriistade kutsumine | Modulaarsus, koostöö, protsesside orkestreerimine | Turvaline, skaleeritav ja paindlik AI agentide juurutus |

## Kas ma saan oma olemasolevaid Azure ökosüsteemi tööriistu otse integreerida või on vaja eraldiseisvaid lahendusi?


Vastus on jah, saate oma olemasolevaid Azure ökosüsteemi tööriistu integreerida Microsoft Foundry Agent Service'iga otse, eriti kuna see on loodud sujuvaks koostööks teiste Azure teenustega. Näiteks võiksite integreerida Bingit, Azure AI Searchi ja Azure Functions'i. Microsoft Foundry'ga on ka sügav integratsioon.

Microsoft Agent Framework integreerub ka Azure teenustega läbi `FoundryChatClient` ja Azure identiteedi, võimaldades teil kutsuda Azure teenuseid otse oma agendi tööriistadest.

## Näidiskoodid

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Kas on veel küsimusi AI Agent Frameworkide kohta?

Liituge [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppuritega, osaleda kontoritundides ja saada vastused oma AI agentide küsimustele.

## Viited

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Eelmine õppetund

[Sissejuhatus AI agentidesse ja agentide kasutusjuhtudesse](../01-intro-to-ai-agents/README.md)

## Järgmine õppetund

[Agentse disaini mustrite mõistmine](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->