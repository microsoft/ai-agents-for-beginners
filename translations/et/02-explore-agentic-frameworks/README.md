[![Tehisintellekti agendi raamistikud](../../../translated_images/et/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klõpsake ülaloleval pildil, et vaadata selle õppetunni videot)_

# Avasta tehisintellekti agendi raamistikud

Tehisintellekti agendi raamistikud on tarkvaraplatvormid, mis on loodud tehisintellekti agentide loomise, juurutamise ja haldamise lihtsustamiseks. Need raamistikud pakuvad arendajatele eelvalmis komponente, abstraktsioone ja tööriistu, mis aitavad sujuvamaks muuta keerukate tehisintellektilahenduste arendamise.

Need raamistikud aitavad arendajatel keskenduda oma rakenduste unikaalsetele aspektidele, pakkudes standardiseeritud lähenemisviise tehisintellekti agentide arendamise üldistele väljakutsetele. Nad parandavad skaleeritavust, ligipääsetavust ja tõhusust tehisintellektisüsteemide ehitamisel.

## Sissejuhatus

Selles õppetunnis käsitletakse:

- Mis on tehisintellekti agendi raamistikud ja mida need arendajatele võimaldavad?
- Kuidas saavad meeskonnad neid kiiresti prototüüpida, iteratiivseid versioone teha ja agentide võimeid parandada?
- Millised on Microsofti loodud raamistikute ja tööriistade (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> ja <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) erinevused?
- Kas ma saan oma olemasolevaid Azure'i ökosüsteemi tööriistu otse integreerida või on vaja iseseisvaid lahendusi?
- Mis on Azure AI Agent Service ja kuidas see mind aitab?

## Õpieesmärgid

Selle õppetunni eesmärk on aidata teil mõista:

- Tehisintellekti agendi raamistikute rolli tehisintellekti arenduses.
- Kuidas kasutada tehisintellekti agendi raamistikuid intellektuaalsete agentide loomiseks.
- Olulisi funktsionaalsusi, mida tehisintellekti agendi raamistikud võimaldavad.
- Erinevusi Microsoft Agent Frameworki ja Azure AI Agent Service vahel.

## Mis on tehisintellekti agendi raamistikud ja mida nad arendajatele võimaldavad?

Traditsioonilised tehisintellekti raamistikud võivad aidata teil integreerida tehisintellekti oma rakendustesse ning muuta need rakendused paremaks järgmistes valdkondades:

- **Isikupärastamine**: Tehisintellekt võib analüüsida kasutaja käitumist ja eelistusi, et pakkuda isikupärastatud soovitusi, sisu ja kogemusi.  
Näide: voogedastusplatvormid nagu Netflix kasutavad tehisintellekti filmide ja saadete soovitamiseks vaatajaloo põhjal, parandades kasutajate kaasatust ja rahulolu.
- **Automatiseerimine ja tõhusus**: Tehisintellekt võib automatiseerida rutiinseid ülesandeid, sujuvamaks muuta töövooge ja parandada tegevuste efektiivsust.  
Näide: klienditeenindusrakendused kasutavad tehisintellektil põhinevaid vestlusroboteid korduvate päringute käsitlemiseks, vähendades reageerimisaegu ja vabastades inimagente keerukamate probleemide jaoks.
- **Täiustatud kasutajakogemus**: Tehisintellekt võib parandada üldist kasutajakogemust, pakkudes nutikaid funktsioone nagu hääl- ja kõnetuvastus, loomuliku keele töötlemine ja ennustav tekstisisestus.  
Näide: virtuaalsed assistendid nagu Siri ja Google Assistant kasutavad tehisintellekti häälkäskluste mõistmiseks ja neile vastamiseks, muutes kasutajate seadmetega suhtlemise lihtsamaks.

### See kõik kõlab ju suurepäraselt, miks siis on meil vaja AI Agent Frameworki?

Tehisintellekti agendi raamistikud on rohkem kui lihtsalt tehisintellekti raamistikud. Need on loodud võimaldama nutikate agentide loomist, kes saavad suhelda kasutajate, teiste agentide ja keskkonnaga kindlate eesmärkide saavutamiseks. Need agentid võivad avaldada autonoomset käitumist, teha otsuseid ja kohaneda muutuvate oludega. Vaatame mõningaid AI Agent Frameworkide peamisi funktsionaalsusi:

- **Agentide koostöö ja koordineerimine**: Võimaldab luua mitut tehisintellekti agenti, kes saavad omavahel koostööd teha, suhelda ja keerukaid ülesandeid koordineerida.
- **Ülesannete automatiseerimine ja haldamine**: Pakub mehhanisme mitmeastmeliste tööprotsesside automatiseerimiseks, ülesannete delegeerimiseks ja dünaamiliseks haldamiseks agentide vahel.
- **Kontekstitunnetus ja kohanemine**: Varustab agente võimega mõista konteksti, kohaneda muutuvate keskkondadega ja teha otsuseid reaalajas saadud teabe põhjal.

Seega kokkuvõttes võimaldavad agentide raamistikud teil teha rohkem, viia automatiseerimine uuele tasemele, luua nutikamaid süsteeme, mis suudavad keskkonnast õppida ja kohaneda.

## Kuidas kiiresti prototüüpida, iteratiivseid versioone teha ja agentide võimeid parandada?

See valdkond areneb kiiresti, kuid enamikul tehisintellekti agendi raamistikutel on mõningaid ühiseid omadusi, mis aitavad teil kiiresti prototüüpe luua ja iteratsioone teha, nimelt moodulkomponendid, koostöövahendid ja reaalajas õppimine. Vaatame neid lähemalt:

- **Kasuta moodulkomponente**: AI SDK-d pakuvad eelvalmis komponente nagu tehisintellekti ja mäluga ühendused, funktsioonikutsed loomulikus keeles või koodipistikprogrammidega, püsivormid jms.
- **Kasuta koostöövahendeid**: Kujunda agentidele konkreetsed rollid ja ülesanded, võimaldades neil testida ja täiustada koostöövooge.
- **Õpi reaalajas**: Rakenda tagasisidetsükleid, kus agent õpib suhtlemisest ja kohandab oma käitumist dünaamiliselt.

### Kasuta moodulkomponente

SDK-d nagu Microsoft Agent Framework pakuvad eelvalmis komponente nagu tehisintellekti ühendajad, tööriistade definitsioonid ja agentide haldus.

**Kuidas meeskonnad võivad neid kasutada**: Meeskonnad saavad kiiresti kokkupanekuga luua funktsionaalse prototüübi ilma nullist alustamata, võimaldades kiiret eksperimenteerimist ja iteratsiooni.

**Kuidas see praktikas toimib**: Võite kasutada eelvalmis parserit kasutaja sisendi võtmetähtsusega info väljavõtmiseks, mälumoodulit andmete salvestamiseks ja tagasivõtmiseks ning püsivormi genereerijat kasutajatega suhtlemiseks, ilma et peaksite neid komponente nullist ehitama.

**Näidiskood**. Vaatame näidet, kuidas kasutada Microsoft Agent Frameworki koos `AzureAIProjectAgentProvider`-ga, et mudel reageeriks kasutaja sisendile tööriista kutsumisega:

``` python
# Microsoft Agent Frameworki Pythoni näide

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Määratle näidistööriista funktsioon reisi broneerimiseks
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
    # Näidisväljund: Teie lend New Yorki 1. jaanuaril 2025 on edukalt broneeritud. Head reisi! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Selles näites näete, kuidas saab kasutada eelvalmis parserit võtmetähtsusega teabe (näiteks lennupileti broneerimise päritolu, sihtpunkti ja kuupäeva) väljavõtmiseks kasutaja sisendist. See moodulpõhine lähenemine võimaldab teil keskenduda kõrgetasemelisele loogikale.

### Kasuta koostöövahendeid

Raamistikud nagu Microsoft Agent Framework võimaldavad luua mitut agenti, kes saavad omavahel koostööd teha.

**Kuidas meeskonnad võivad neid kasutada**: Meeskonnad saavad kujundada agentidele spetsiifilised rollid ja ülesanded, võimaldades neil testida ja täiustada koostööprotsesse ning parandada süsteemi üldist tõhusust.

**Kuidas see praktikas toimib**: Võite luua agentide tiimi, kus iga agent täidab spetsialiseerunud funktsiooni, näiteks andmete toomine, analüüs või otsuste tegemine. Need agentid saavad omavahel suhelda ja infot jagada ühise eesmärgi saavutamiseks, näiteks kasutajapäringule vastamiseks või ülesande täitmiseks.

**Näidiskood (Microsoft Agent Framework)**:

```python
# Mitme agendi loomine, kes töötavad koos Microsoft Agent Frameworki abil

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Andmete hankimise agent
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Andmeanalüüsi agent
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Käivita agendid ülesande täitmiseks järjestikku
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Eelnevas koodis näete, kuidas luua ülesanne mitme agenti kaasamisega andmete analüüsimiseks. Iga agent täidab konkreetset funktsiooni ja ülesanne täidetakse agentide koordineerimise kaudu soovitud tulemuse saavutamiseks. Pühendatud agentide loomine spetsialiseerunud rollidega võimaldab parandada ülesannete tõhusust ja tulemuslikkust.

### Õpi reaalajas

Taas keerukamad raamistikud pakuvad võimalusi reaalajas kontekstitundlikuks mõistmiseks ja kohandamiseks.

**Kuidas meeskonnad võivad neid kasutada**: Meeskonnad saavad rakendada tagasisidetsükleid, kus agent õpib suhtlemisest ja kohandab dünaamiliselt oma käitumist, mis võimaldab pidevat arengut ja võimete täiustamist.

**Kuidas see praktikas toimib**: Agentidel on võime analüüsida kasutajate tagasisidet, keskkonnaandmeid ja ülesannete tulemusi, et uuendada oma teadmistebaasi, kohandada otsustusalgoritme ja parandada tulemusi aja jooksul. See iteratiivne õppimisprotsess võimaldab agentidel kohaneda muutuvate tingimuste ja kasutajapreferentsidega, parandades süsteemi üldist efektiivsust.

## Millised on Microsoft Agent Frameworki ja Azure AI Agent Service erinevused?

Neid lähenemisi saab võrrelda mitmeti, kuid vaatame mõned olulised erinevused disaini, funktsionaalsuste ja sihtkasutuse osas:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework pakub lihtsustatud SDK-d AI agentide loomiseks `AzureAIProjectAgentProvider` abil. See võimaldab arendajatel luua agente, kes kasutavad Azure OpenAI mudeleid koos sisseehitatud tööriistakutsumise, vestluse halduse ja ettevõtte turvalisusega Azure identiteedi kaudu.

**Kasutusjuhtumid**: Tootmiskõlblike tehisintellekti agentide ehitamine tööriistakasutusega, mitmeastmeliste töövoogude ja ettevõtte integratsioonistsenaarioidega.

Siin on mõned Microsoft Agent Frameworki olulised põhimõisted:

- **Agendid**. Agent luuakse `AzureAIProjectAgentProvider` kaudu ja konfigureeritakse nime, juhiste ja tööriistadega. Agent saab:
  - **Töödelda kasutaja sõnumeid** ja genereerida vastuseid Azure OpenAI mudelite abil.
  - **Kutsuda tööriistu** automaatselt vestluse konteksti alusel.
  - **Hooldada vestluse olekut** mitme suhtluse jooksul.

  Siin on koodinäide, kuidas agenti luua:

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

- **Tööriistad**. Raamistik toetab tööriistade defineerimist Python funktsioonidena, mida agent saab automaatselt kutsuda. Tööriistad registreeritakse agendi loomisel:

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

- **Mitme agendi koordineerimine**. Võite luua mitu agenti erinevate spetsialiseerumistega ja koordineerida nende tööd:

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

- **Azure identiteedi integratsioon**. Raamistik kasutab turvaliseks ja võtmeta autentimiseks `AzureCliCredential` (või `DefaultAzureCredential`), mis kõrvaldab API võtmete käsitsi haldamise vajaduse.

## Azure AI Agent Service

Azure AI Agent Service on hiljutine täiendus, mis esitleti Microsoft Ignite 2024 üritusel. See võimaldab AI agentide arendust ja juurutamist paindlikumate mudelitega, näiteks otse avatud lähtekoodiga LLM-ide (nagu Llama 3, Mistral ja Cohere) kutsumise kaudu.

Azure AI Agent Service pakub tugevamaid ettevõtte turvamehhanisme ja andmete talletamise meetodeid, sobides hästi ettevõtte rakendusteks.

See töötab vahetult koos Microsoft Agent Frameworkiga agentide ehitamiseks ja juurutamiseks.

Teenust toetatakse praegu Avalikus eelvaates ning see toetab agentide loomist Pythonis ja C#-s.

Azure AI Agent Service Python SDK abil saame luua agendi kasutajamääratud tööriistaga:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Määra tööriista funktsioonid
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

### Põhimõisted

Azure AI Agent Service põhikontseptsioonid on järgmised:

- **Agent**. Azure AI Agent Service integreerub Microsoft Foundry-ga. AI Foundry's tegutseb AI Agent kui "nutikas" mikroteenus, mida saab kasutada küsimustele vastamiseks (RAG), tegevuste sooritamiseks või töövoogude täielikuks automatiseerimiseks. See saavutatakse generatiivsete tehisintellekti mudelite ja tööriistade kombineerimisega, mis võimaldavad juurdepääsu ja suhtlemist reaalse maailma andmeallikatega. Näide agendist:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Selles näites luuakse agent mudeliga `gpt-4o-mini`, nimega `my-agent` ja juhistega `Sa oled abivalmis agent`. Agendile on varustatud tööriistad ja ressursid koodi tõlgendamise ülesannete täitmiseks.

- **Vestlusteema ja sõnumid**. Vestlusteema on teine oluline mõiste. See esindab vestlust või suhtlust agendi ja kasutaja vahel. Vestlusteemasid saab kasutada vestluse edenemise jälgimiseks, konteksti informatsiooni salvestamiseks ja suhtluse oleku haldamiseks. Näide vestlusteemast:

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

    Eelnevas koodis luuakse vestlusteema. Seejärel saadetakse sõnum vestlusteemale. `create_and_process_run` kutsumisega palutakse agendil vestlusteemaga tööd teha. Lõpuks hangitakse ja logitakse sõnumid, et näha agendi vastust. Sõnumid näitavad vestluse edenemist kasutaja ja agendi vahel. Samuti on oluline mõista, et sõnumid võivad olla erinevat tüüpi, näiteks tekst, pilt või fail, mis on agendi töö tulemus, näiteks pilt või tekstivastus. Arendajana saate neid andmeid kasutada vastuse edasiseks töötlemiseks või kasutajale esitamiseks.

- **Integratsioon Microsoft Agent Frameworkiga**. Azure AI Agent Service töötab sujuvalt koos Microsoft Agent Frameworkiga, mis tähendab, et saate ehitada agente `AzureAIProjectAgentProvider` abil ja juurutada neid tootmiskeskkonnas Agent Service kaudu.

**Kasutusjuhtumid**: Azure AI Agent Service on mõeldud ettevõtte rakendustele, mis nõuavad turvalist, skaleeritavat ja paindlikku AI agentide juurutamist.

## Mis erinevused on nende lähenemiste vahel?

Tundub, et kattuvust on, kuid disaini, funktsionaalsuse ja sihtotstarbe osas on olulisi erinevusi:

- **Microsoft Agent Framework (MAF)**: Tootmiskõlbulik SDK tehisintellekti agentide loomiseks. Pakub lihtsustatud API-d agentide loomiseks tööriistakutsumise, vestluse halduse ja Azure identiteedi integratsiooniga.
- **Azure AI Agent Service**: Platvorm ja juurutusteenus Azure Foundry keskkonnas agentidele. Pakub sisseehitatud ühenduvust teenustega nagu Azure OpenAI, Azure AI Search, Bing Search ja koodi täitmine.

Kas ikka ei tea, kumba valida?

### Kasutusjuhtumid

Vaatame, kas saame aidata mõningate tavapäraste kasutusjuhtumite põhjal:

> K: Ehitan tootmiskõlblikke tehisintellekti agentide rakendusi ja soovin kiiresti alustada  
>  
> V: Microsoft Agent Framework on suurepärane valik. See pakub lihtsat, Pythonilikku API-d `AzureAIProjectAgentProvider` kaudu, mis võimaldab vaid mõne koodirea abil defineerida agente tööriistade ja juhistega.

> K: Vajan ettevõtte tasemel juurutust Azure integratsioonidega nagu Search ja koodi täitmine  
>  
> V: Azure AI Agent Service on kõige sobivam. See on platvormiteenus, mis pakub mitme mudeli, Azure AI Searchi, Bing Searchi ja Azure Functionsi sisseehitatud funktsioone. See teeb agentide ehitamise Foundry portaalis lihtsaks ja võimaldab neid suuremas mahus juurutada.

> K: Olen endiselt segaduses, anna üks valik  
>  
> V: Alusta Microsoft Agent Frameworkist agentide loomiseks ja kasuta seejärel Azure AI Agent Service’i, kui vajad agentide tootmiskeskkonnas juurutamist ja skaleerimist. See lähenemine võimaldab teil kiiresti agentide loogikat arendada, säilitades selge tee ettevõtte juurutuseks.

Kokkuvõtame peamised erinevused tabelis:

| Raamistik | Keskendumine | Põhimõisted | Kasutusjuhtumid |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Lihtsustatud agendi SDK tööriistakutsumisega | Agendid, Tööriistad, Azure identiteet | AI agentide loomine, tööriistakasutus, mitmeastmelised töövood |
| Azure AI Agent Service | Paindlikud mudelid, ettevõtte turvalisus, koodigeneratsioon, tööriistakutsumine | Moodulsus, Koostöö, Protsesside orkestreerimine | Turvaline, skaleeritav ja paindlik AI agentide juurutus |

## Kas saan oma olemasolevaid Azure'i ökosüsteemi tööriistu otse integreerida või on vaja iseseisvaid lahendusi?
Vastus on jaatav, saate oma olemasolevaid Azure'i ökosüsteemi tööriistu integreerida otse Azure AI Agent teenusega, eriti kuna see on ehitatud sujuvaks koostööks teiste Azure'i teenustega. Näiteks võite integreerida Bingi, Azure AI Otsingu ja Azure Funktsioonid. Samuti on olemas sügav integratsioon Microsoft Foundryga.

Microsoft Agent raamistiku saab samuti integreerida Azure'i teenustega läbi `AzureAIProjectAgentProvider` ja Azure identiteedi, mis võimaldab teil oma agente tööriistadest Azure'i teenuseid otse kutsuda.

## Näidiskoodid

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Veel küsimusi AI Agent Frameworkside kohta?

Liituge [Microsoft Foundry Discordiga](https://aka.ms/ai-agents/discord), et kohtuda teiste õppuritega, osaleda kantselei aegadel ja saada vastuseid oma AI Agentide küsimustele.

## Viited

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI vastused</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent teenus</a>

## Eelmine õppetund

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Järgmine õppetund

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellekti tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, tuleb arvestada, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument oma algkeeles on autoriteetne allikas. Olulise teabe puhul soovitatakse professionaalset inimtõlget. Me ei vastuta tõlke kasutamisest tulenevate arusaamatuste ega valesti tõlgendamise eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->