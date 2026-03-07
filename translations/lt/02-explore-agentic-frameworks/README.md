[![Tyrinėjant AI agentų karkasus](../../../translated_images/lt/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Spustelėkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# Tyrinėkite AI agentų karkasus

Dirbtinio intelekto agentų karkasai yra programinės įrangos platformos, sukurtos supaprastinti AI agentų kūrimą, diegimą ir valdymą. Šie karkasai suteikia kūrėjams iš anksto paruoštas dalis, abstrakcijas ir įrankius, kurie pagreitina sudėtingų AI sistemų kūrimą.

Šie karkasai padeda kūrėjams susitelkti į unikalius jų programų aspektus, teikdami standartinius sprendimus įprastoms AI agentų kūrimo problemoms. Jie didina mastelį, prieinamumą ir efektyvumą kuriant AI sistemas.

## Įvadas 

Šioje pamokoje aptarsime:

- Kas yra AI agentų karkasai ir ką jie leidžia pasiekti kūrėjams?
- Kaip komandos gali naudoti šiuos karkasus greitai prototipavimui, iteracijoms ir agentų gebėjimų tobulinimui?
- Kokie yra skirtumai tarp Microsoft sukurtų karkasų ir įrankių (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> ir <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Ar galiu integruoti esamus savo Azure ekosistemos įrankius tiesiogiai, ar man reikia atskirų sprendimų?
- Kas yra Azure AI Agents paslauga ir kaip ji man padeda?

## Mokymosi tikslai

Šios pamokos tikslai yra padėti jums suprasti:

- AI agentų karkasų vaidmenį AI kūrime.
- Kaip pasinaudoti AI agentų karkasais kuriant intelektualius agentus.
- Pagrindines galimybes, kurias suteikia AI agentų karkasai.
- Skirtumus tarp Microsoft Agent Framework ir Azure AI Agent Service.

## Kas yra AI agentų karkasai ir ką jie leidžia kūrėjams daryti?

Tradiciniai AI karkasai gali padėti integruoti AI į jūsų programas ir pagerinti jas šiais būdais:

- **Personalizavimas**: AI gali analizuoti vartotojo elgesį ir pageidavimus, kad pateiktų suasmenintas rekomendacijas, turinį ir patirtis.
Pavyzdys: transliacijos paslaugos, tokios kaip Netflix, naudoja AI siūlydamos filmus ir serialus pagal peržiūros istoriją, taip didindamos vartotojų įsitraukimą ir pasitenkinimą.
- **Automatizavimas ir efektyvumas**: AI gali automatizuoti pasikartojančias užduotis, supaprastinti darbo srautus ir pagerinti veiklos efektyvumą.
Pavyzdys: klientų aptarnavimo programos naudoja AI pagrįstus pokalbių robotus, kurie tvarko įprastus užklausimus, mažindami atsako laiką ir atlaisvindami žmogiškuosius agentus sudėtingesniems klausimams.
- **Pagerinta vartotojo patirtis**: AI gali pagerinti bendrą vartotojo patirtį teikdama intelektualias funkcijas, tokias kaip balso atpažinimas, natūralios kalbos apdorojimas ir prognozuojamo teksto funkcijos.
Pavyzdys: virtualūs asistentai, tokie kaip Siri ir Google Assistant, naudoja AI suprasti ir reaguoti į balso komandas, palengvindami vartotojų sąveiką su įrenginiais.

### Viską skamba puikiai, bet kodėl mums reikia AI agentų karkaso?

AI agentų karkasai reiškia kažką daugiau nei tik AI karkasai. Jie sukurti leidžiant kurti intelektualius agentus, kurie gali sąveikauti su vartotojais, kitais agentais ir aplinka, siekdami konkrečių tikslų. Šie agentai gali demonstruoti autonominį elgesį, priimti sprendimus ir prisitaikyti prie kintančių sąlygų. Pažvelkime į keletą pagrindinių galimybių, kurias suteikia AI agentų karkasai:

- **Agentų bendradarbiavimas ir koordinavimas**: leidžia kurti kelis AI agentus, kurie gali dirbti kartu, bendrauti ir koordinuotis sprendžiant sudėtingas užduotis.
- **Užduočių automatizavimas ir valdymas**: suteikia mechanizmus daugiasluoksniams darbo srautams automatizuoti, užduočių delegavimui ir dinamiškam užduočių valdymui tarp agentų.
- **Kontekstinis supratimas ir prisitaikymas**: aprūpina agentus gebėjimu suprasti kontekstą, prisitaikyti prie kintančios aplinkos ir priimti sprendimus remiantis realaus laiko informacija.

Apibendrinant, agentai leidžia jums atlikti daugiau, pakelti automatizavimą į kitą lygį ir kurti intelektualesnes sistemas, kurios gali prisitaikyti ir mokytis iš savo aplinkos.

## Kaip greitai prototipuoti, iteruoti ir tobulinti agento gebėjimus?

Tai sparčiai besikeičianti sritis, tačiau yra keletas bendrų savybių daugelyje AI agentų karkasų, kurios gali padėti greitai prototipuoti ir iteruoti — tai modulinių komponentų, bendradarbiavimo įrankių ir realaus laiko mokymosi panaudojimas. Pažiūrėkime tai išsamiau:

- **Naudokite modulius komponentus**: AI SDK siūlo iš anksto paruoštus komponentus, tokius kaip AI ir atminties jungtys, funkcijų kvietimas naudojant natūralią kalbą ar kodo papildinius, pranešimų šablonai ir daugiau.
- **Pasinaudokite bendradarbiavimo įrankiais**: projektuokite agentus su konkrečiomis rolėmis ir užduotimis, leidžiančiomis jiems išbandyti ir tobulinti bendradarbiavimo darbo srautus.
- **Mokykitės realiu laiku**: įdiekite grįžtamojo ryšio kilpas, kuriose agentai mokosi iš sąveikų ir dinamiškai koreguoja savo elgesį.

### Naudokite modulius komponentus

SDK, tokie kaip Microsoft Agent Framework, siūlo iš anksto paruoštus komponentus, tokius kaip AI jungtys, įrankių apibrėžimai ir agentų valdymas.

**Kaip komandos gali tai naudoti**: Komandos gali greitai surinkti šiuos komponentus ir sukurti funkcinį prototipą be pradedančio nuo nulio, leidžiančią greitai eksperimentuoti ir kartoti.

**Kaip tai veikia praktikoje**: galite naudoti iš anksto paruoštą parser'į, kad išgautumėte informaciją iš vartotojo įvesties, atminties modulį duomenų saugojimui ir gavimui, bei pranešimų generatorių sąveikai su vartotojais — visa tai be poreikio kurti šiuos komponentus nuo nulio.

**Pavyzdinis kodas**. Pažiūrėkime pavyzdį, kaip galite naudoti Microsoft Agent Framework su `AzureAIProjectAgentProvider`, kad modelis atsakytų į vartotojo įvestį kviesdamas įrankius:

``` python
# Microsoft Agent Framework Python pavyzdys

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Apibrėžkite pavyzdinę įrankio funkciją kelionės užsakymui
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
    # Pavyzdinis rezultatas: Jūsų skrydis į Niujorką 2025 m. sausio 1 d. sėkmingai užsakytas. Saugių kelionių! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Iš šio pavyzdžio matyti, kaip galite pasinaudoti iš anksto paruoštu parser'iu, kad iš vartotojo įvesties išgautumėte pagrindinę informaciją, pvz., skrydžio užsakymo užklausos kilmę, paskirties vietą ir datą. Šis modulinis požiūris leidžia susitelkti į aukšto lygio logiką.

### Pasinaudokite bendradarbiavimo įrankiais

Karkasai, tokie kaip Microsoft Agent Framework, palengvina kelių agentų, galinčių dirbti kartu, kūrimą.

**Kaip komandos gali tai naudoti**: Komandos gali sukurti agentus su konkrečiomis rolėmis ir užduotimis, leidžiančiomis išbandyti ir tobulinti bendradarbiavimo darbo srautus bei pagerinti bendrą sistemos efektyvumą.

**Kaip tai veikia praktikoje**: galite sukurti agentų komandą, kur kiekvienas agentas atlieka specializuotą funkciją, pvz., duomenų gavimą, analizę ar sprendimų priėmimą. Šie agentai gali bendrauti ir dalintis informacija siekdami bendro tikslo, pvz., atsakyti į vartotojo užklausą arba atlikti užduotį.

**Pavyzdinis kodas (Microsoft Agent Framework)**:

```python
# Kuriami keli agentai, kurie dirba kartu, naudojant Microsoft Agent sistemą

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Duomenų gavimo agentas
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Duomenų analizės agentas
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Vykdyti agentus iš eilės užduoties atlikimui
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Iš ankstesnio kodo matote, kaip galite sukurti užduotį, kurioje dalyvauja keli agentai, dirbantys kartu duomenų analizei. Kiekvienas agentas atlieka specifinę funkciją, o užduotis vykdoma koordinuojant agentus, kad būtų pasiektas pageidaujamas rezultatas. Kuriant skirtus agentus su specializuotomis rolėmis, galite pagerinti užduočių efektyvumą ir našumą.

### Mokykitės realiu laiku

Išplėstiniai karkasai suteikia galimybes realaus laiko konteksto supratimui ir prisitaikymui.

**Kaip komandos gali tai naudoti**: Komandos gali įdiegti grįžtamojo ryšio grandines, kuriose agentai mokosi iš sąveikų ir dinamiškai keičia savo elgesį, kas veda prie nuolatinio gebėjimų tobulėjimo ir rafinavimo.

**Kaip tai veikia praktikoje**: agentai gali analizuoti vartotojų atsiliepimus, aplinkos duomenis ir užduočių rezultatus, atnaujinti savo žinių bazę, koreguoti sprendimų priėmimo algoritmus ir palaipsniui gerinti našumą. Šis iteratyvus mokymosi procesas leidžia agentams prisitaikyti prie kintančių sąlygų ir vartotojų pageidavimų, didinant bendrą sistemos veiksmingumą.

## Kokie yra skirtumai tarp Microsoft Agent Framework ir Azure AI Agent Service?

Yra daug būdų palyginti šiuos požiūrius, bet pažvelkime į keletą pagrindinių skirtumų jų dizaino, galimybių ir tikslinių naudojimo atvejų požiūriu:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework teikia supaprastintą SDK AI agentų kūrimui naudojant `AzureAIProjectAgentProvider`. Jis suteikia kūrėjams galimybę kurti agentus, kurie naudoja Azure OpenAI modelius su integruotu įrankių kvietimu, pokalbių valdymu ir įmoniniu saugumu per Azure tapatybę.

**Naudojimo atvejai**: Kurti gamybai paruoštus AI agentus, naudojančius įrankius, daugiasluoksnius darbo srautus ir įmonines integracijos scenarijas.

Štai keletas svarbių Microsoft Agent Framework pagrindinių sąvokų:

- **Agentai**. Agentas sukuriamas per `AzureAIProjectAgentProvider` ir konfigūruojamas su pavadinimu, instrukcijomis ir įrankiais. Agentas gali:
  - **Apdoroti vartotojo žinutes** ir generuoti atsakymus naudodamas Azure OpenAI modelius.
  - **Kviesti įrankius** automatiškai, remiantis pokalbio kontekstu.
  - **Išlaikyti pokalbio būseną** per kelias sąveikas.

  Čia pateiktas kodo fragmentas, rodantis, kaip sukurti agentą:

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

- **Įrankiai**. Karkasas palaiko įrankių apibrėžimą kaip Python funkcijas, kurias agentas gali kviesti automatiškai. Įrankiai registruojami kuriant agentą:

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

- **Daugiagentų koordinavimas**. Galite sukurti kelis agentus su skirtinga specializacija ir koordinuoti jų darbą:

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

- **Azure tapatybės integracija**. Karkasas naudoja `AzureCliCredential` (ar `DefaultAzureCredential`) saugiam, be raktų autentifikavimui, taip pašalinant poreikį tiesiogiai valdyti API raktus.

## Azure AI Agent Service

Azure AI Agent Service yra naujesnis priedas, pristatytas Microsoft Ignite 2024 metu. Jis leidžia kurti ir diegti AI agentus su lankstesniais modeliais, pavyzdžiui, tiesiogiai kviečiant atviro kodo LLM'us, tokius kaip Llama 3, Mistral ir Cohere.

Azure AI Agent Service teikia stipresnius įmonės saugumo mechanizmus ir duomenų saugojimo metodus, todėl tinka įmoninėms programoms.

Jis veikia „iš dėžutės“ kartu su Microsoft Agent Framework agentų kūrimui ir diegimui.

Ši paslauga šiuo metu yra viešoje peržiūroje (Public Preview) ir palaiko Python ir C# agentų kūrimui.

Naudodami Azure AI Agent Service Python SDK galime sukurti agentą su vartotojo apibrėžtu įrankiu:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Apibrėžti įrankio funkcijas
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

### Pagrindinės sąvokos

Azure AI Agent Service apima šias pagrindines sąvokas:

- **Agentas**. Azure AI Agent Service integruojasi su Microsoft Foundry. AI Foundry viduje AI agentas veikia kaip „išmanus“ mikropaslaugas, kuris gali būti naudojamas atsakyti į klausimus (RAG), atlikti veiksmus arba visiškai automatizuoti darbo srautus. Tai pasiekiama derinant generatyvinių AI modelių galią su įrankiais, leidžiančiais pasiekti ir sąveikauti su realaus pasaulio duomenų šaltiniais. Štai agento pavyzdys:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Šiame pavyzdyje agentas sukurtas su modeliu `gpt-4o-mini`, pavadinimu `my-agent` ir instrukcijomis `You are helpful agent`. Agentas aprūpintas įrankiais ir ištekliais kodo interpretavimo užduotims atlikti.

- **Gija ir žinutės**. Gija yra kita svarbi sąvoka. Ji atspindi pokalbį arba sąveiką tarp agente ir vartotojo. Gijos gali būti naudojamos stebėti pokalbio eigą, saugoti kontekstinę informaciją ir valdyti sąveikos būseną. Štai gijos pavyzdys:

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

    Ankstesniame kode sukurta gija. Vėliau į giją siunčiama žinutė. Kviesdami `create_and_process_run`, prašome agento atlikti darbą gijoje. Galiausiai žinutės yra gaunamos ir registruojamos, kad būtų matomas agento atsakymas. Žinutės nurodo pokalbio eigą tarp vartotojo ir agente. Taip pat svarbu suprasti, kad žinutės gali būti skirtingų tipų, pavyzdžiui, tekstas, vaizdas ar failas — tai reiškia, kad agento darbas galėjo sukelti, pavyzdžiui, vaizdo ar teksto atsakymą. Būdamas kūrėju, tuomet galite panaudoti šią informaciją tolesniam atsakymo apdorojimui arba jo pateikimui vartotojui.

- **Integracija su Microsoft Agent Framework**. Azure AI Agent Service sklandžiai veikia su Microsoft Agent Framework, tai reiškia, kad galite kurti agentus naudodami `AzureAIProjectAgentProvider` ir diegti juos per Agent Service gamybos scenarijoms.

**Naudojimo atvejai**: Azure AI Agent Service sukurta įmoninėms programoms, kurioms reikalingas saugus, išplečiamas ir lanksčiai diegiamas AI agentų palaikymas.

## Kuo šie požiūriai skiriasi?
 
Atrodo, jog yra perdengimų, bet yra keletas pagrindinių skirtumų jų dizaino, galimybių ir tikslinių naudojimo atvejų požiūriu:
 
- **Microsoft Agent Framework (MAF)**: yra gamybai paruoštas SDK AI agentų kūrimui. Jis suteikia supaprastintą API agentų kūrimui su įrankių kvietimu, pokalbių valdymu ir Azure tapatybės integracija.
- **Azure AI Agent Service**: yra platforma ir diegimo paslauga Azure Foundry. Ji siūlo integruotą jungtį su paslaugomis, tokiomis kaip Azure OpenAI, Azure AI Search, Bing Search ir kodo vykdymas.
 
Vis dar nesate tikri, kurį pasirinkti?

### Naudojimo atvejai
 
Pažiūrėkime, ar galime jums padėti peržiūrėdami keletą dažnų naudojimo atvejų:
 
> Q: Kuriu gamybos AI agentų programas ir noriu greitai pradėti
>

>A: Microsoft Agent Framework yra puikus pasirinkimas. Jis suteikia paprastą, Python stilistika paremtą API per `AzureAIProjectAgentProvider`, leidžiančią apibrėžti agentus su įrankiais ir instrukcijomis vos keliose kodo eilutėse.

>Q: Man reikia įmoninio lygio diegimo su Azure integracijomis, tokiomis kaip Search ir kodo vykdymas
>
> A: Azure AI Agent Service yra geriausias variantas. Tai platformos paslauga, kuri teikia integruotas galimybes keliems modeliams, Azure AI Search, Bing Search ir Azure Functions. Ji palengvina agentų kūrimą Foundry portale ir jų diegimą mastu.
 
> Q: Vis dar nesuprantu, pasirinkite vieną variantą už mane
>
> A: Pradėkite nuo Microsoft Agent Framework, kad sukurtumėte savo agentus, o vėliau naudokite Azure AI Agent Service, kai reikės juos diegti ir masteliuoti gamyboje. Šis požiūris leidžia greitai iteruoti agentų logiką, turint aiškų kelią į įmoninį diegimą.
 
Apibendrinkime pagrindinius skirtumus lentelėje:

| Framework | Dėmesys | Pagrindinės sąvokos | Naudojimo atvejai |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Supaprastintas agentų SDK su įrankių kvietimu | Agentai, Įrankiai, Azure tapatybė | AI agentų kūrimas, įrankių naudojimas, daugiasluoksniai darbo srautai |
| Azure AI Agent Service | Lankstūs modeliai, įmonės saugumas, kodo generavimas, įrankių kvietimas | Modularumas, Bendradarbiavimas, Procesų orkestracija | Saugus, išplečiamas ir lankstus AI agentų diegimas |

## Ar galiu integruoti esamus savo Azure ekosistemos įrankius tiesiogiai, ar man reikia atskirų sprendimų?
Atsakymas yra taip — galite tiesiogiai integruoti esamus savo Azure ekosistemos įrankius su Azure AI Agent Service, ypač todėl, kad jis buvo sukurtas sklandžiai veikti su kitomis Azure paslaugomis. Pavyzdžiui, galite integruoti Bing, Azure AI Search ir Azure Functions. Taip pat yra glaudi integracija su Microsoft Foundry.

Microsoft Agent Framework taip pat integruojasi su Azure paslaugomis per `AzureAIProjectAgentProvider` ir Azure identitetą, leidžiant jums kviesti Azure paslaugas tiesiogiai iš savo agentų įrankių.

## Pavyzdžių kodai

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Turite daugiau klausimų apie AI agentų sistemas?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kad susipažintumėte su kitais besimokančiais, dalyvautumėte konsultacijose ir gautumėte atsakymus į savo AI agentų klausimus.

## Nuorodos

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Ankstesnė pamoka

[Įvadas į AI agentus ir agentų naudojimo atvejus](../01-intro-to-ai-agents/README.md)

## Kita pamoka

[Agentinių dizaino šablonų supratimas](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Atsakomybės apribojimas:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą Co-op Translator (https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Esant svarbiai informacijai rekomenduojama naudoti profesionalaus vertėjo atliktą vertimą. Mes neatsakome už jokius nesusipratimus ar klaidingas interpretacijas, kylančias dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->