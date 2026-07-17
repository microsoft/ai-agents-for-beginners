[![Tiriame AI agentų kūrimo sistemas](../../../translated_images/lt/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Spustelėkite aukščiau esančią iliustraciją, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# Tyrinėkite AI agentų kūrimo sistemas

AI agentų kūrimo sistemos yra programinės įrangos platformos, skirtos supaprastinti AI agentų kūrimą, paleidimą ir valdymą. Šios sistemos suteikia kūrėjams iš anksto paruoštus komponentus, abstrakcijas ir įrankius, kurie palengvina sudėtingų AI sistemų kūrimą.

Šios sistemos padeda kūrėjams susitelkti į unikalius jų programų aspektus, teikdamos standartizuotus sprendimus dažnai pasitaikančioms AI agentų kūrimo problemoms. Jos gerina mastelį, prieinamumą ir efektyvumą kuriant AI sistemas.

## Įvadas

Šioje pamokoje bus aptarta:

- Kas yra AI agentų kūrimo sistemos ir ką jos leidžia pasiekti kūrėjams?
- Kaip komandos gali naudoti šias sistemas greitai prototipuoti, tobulinti ir gerinti agentų galimybes?
- Kokie yra skirtumai tarp "Microsoft" sukurtų sistemų ir įrankių (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> ir <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Ar galiu tiesiogiai integruoti savo esamus "Azure" ekosistemos įrankius, ar man reikia atskirų sprendimų?
- Kas yra Microsoft Foundry Agent Service ir kaip jis man padeda?

## Mokymosi tikslai

Šios pamokos tikslas yra padėti jums suprasti:

- AI agentų kūrimo sistemų vaidmenį AI kūrime.
- Kaip pasinaudoti AI agentų kūrimo sistemomis protingų agentų kūrimui.
- Pagrindines galimybes, kurias suteikia AI agentų kūrimo sistemos.
- Skirtumus tarp Microsoft Agent Framework ir Microsoft Foundry Agent Service.

## Kas yra AI agentų kūrimo sistemos ir ką jos leidžia kūrėjams daryti?

Tradicinės AI sistemos gali padėti jums integruoti AI į savo programas ir pagerinti jas šiais būdais:

- **Personalizacija**: AI gali analizuoti vartotojų elgseną ir pageidavimus, kad suteiktų suasmenintas rekomendacijas, turinį ir patirtis.
Pavyzdys: srautinio transliavimo paslaugos, tokios kaip Netflix, naudoja AI siūlydamos filmus ir laidas pagal peržiūrų istoriją, didindamos vartotojų įsitraukimą ir pasitenkinimą.
- **Automatizavimas ir efektyvumas**: AI gali automatizuoti pasikartojančias užduotis, supaprastinti darbo eigas ir pagerinti veiklos efektyvumą.
Pavyzdys: klientų aptarnavimo programėlės naudoja AI varomus pokalbių robotus, kad spręstų dažniausiai užduodamus klausimus, trumpindamos atsakymo laiką ir atlaisvindamos žmogaus agentus sudėtingesnėms užduotims.
- **Patobulinta vartotojo patirtis**: AI gali pagerinti bendrą vartotojo patirtį suteikdama protingas funkcijas, tokias kaip balso atpažinimas, natūralios kalbos apdorojimas ir prognozuojamasis tekstas.
Pavyzdys: virtualūs asistentai kaip Siri ir Google Assistant naudoja AI suprasti ir reaguoti į balso komandas, taip palengvindami vartotojų sąveiką su įrenginiais.

### Viskas skamba puikiai, tai kam mums reikalinga AI agentų kūrimo sistema?

AI agentų kūrimo sistemos yra daugiau nei paprastos AI sistemos. Jos skirtos kurti protingus agentus, kurie gali bendrauti su vartotojais, kitais agentais ir aplinka, siekdami konkrečių tikslų. Šie agentai gali turėti autonominį elgesį, priimti sprendimus ir prisitaikyti prie besikeičiančių sąlygų. Pažiūrėkime į keletą pagrindinių galimybių, kurias suteikia AI agentų kūrimo sistemos:

- **Agentų bendradarbiavimas ir koordinacija**: leidžia sukurti kelis AI agentus, kurie gali dirbti kartu, bendrauti ir koordinuoti veiksmus sudėtingoms užduotims spręsti.
- **Užduočių automatizavimas ir valdymas**: suteikia mechanizmus daugiažingsnių darbo eigų automatizavimui, užduočių delegavimui ir dinamiškam užduočių valdymui tarp agentų.
- **Konteksto supratimas ir prisitaikymas**: aprūpina agentus gebėjimu suprasti kontekstą, prisitaikyti prie kintančios aplinkos ir priimti sprendimus, remdamiesi realaus laiko informacija.

Taigi apibendrinant, agentai leidžia jums atlikti daugiau, pakelti automatizaciją į aukštesnį lygį, kurti protingesnes sistemas, kurios gali prisitaikyti ir mokytis iš aplinkos.

## Kaip greitai prototipuoti, tobulinti ir gerinti agentų galimybes?

Tai sparčiai besikeičianti sritis, tačiau daugelyje AI agentų kūrimo sistemų sutinkami tam tikri bendri dalykai, kurie padeda greitai kurti prototipus ir tobulinti — tai moduliniai komponentai, bendradarbiavimo įrankiai ir realaus laiko mokymasis. Panagrinėkime juos:

- **Naudokite modulinės sudėties komponentus**: AI SDK siūlo iš anksto paruoštus komponentus, tokius kaip AI ir atminties jungtys, funkcijų kvietimas naudojant natūralią kalbą ar kodo papildinius, užklausų šablonus ir kt.
- **Naudokite bendradarbiavimo įrankius**: kurkite agentus su specifinėmis rolėmis ir užduotimis, leidžiančiais jiems testuoti ir tobulinti bendradarbiavimo darbo eigas.
- **Mokykitės realiu laiku**: įgyvendinkite atsakymų ciklus, kur agentai mokosi iš sąveikų ir dinamiškai koreguoja savo elgesį.

### Naudokite modulinės sudėties komponentus

Tokie SDK kaip Microsoft Agent Framework siūlo iš anksto paruoštus komponentus, tokius kaip AI jungtys, įrankių apibrėžimai ir agentų valdymas.

**Kaip komandos gali tai naudoti**: komandos gali greitai sukurti funkcinį prototipą, nesikuriant visko nuo nulio, leidžiantį sparčiai eksperimentuoti ir tobulinti.

**Kaip tai veikia praktikoje**: galite naudoti iš anksto paruoštą analizatorių vartotojo įvesties informacijai ištraukti, atminties modulį duomenims laikyti ir gauti bei užklausų generatorių sąveikai su vartotoju – visa tai nesukuriant komponentų nuo nulio.

**Kodo pavyzdys**. Pažiūrėkime pavyzdį, kaip naudoti Microsoft Agent Framework su `FoundryChatClient`, kad modelis atsakytų į vartotojo įvestį naudojant įrankių kvietimą:

``` python
# Microsoft Agent Framework Python Pavyzdys

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Apibrėžkite pavyzdinę įrankio funkciją kelionės užsakymui
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
    # Pavyzdinis išvestis: Jūsų skrydis į Niujorką 2025 m. sausio 1 d. sėkmingai užsakytas. Saugios kelionės! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Iš šio pavyzdžio matote, kaip galite pasinaudoti iš anksto paruoštu analizatoriumi, kad iš vartotojo įvesties ištrauktumėte svarbią informaciją, pvz., skrydžio užsakymo užklausos kilmę, paskirties vietą ir datą. Šis modulinis požiūris leidžia jums susitelkti į aukšto lygio logiką.

### Naudokite bendradarbiavimo įrankius

Tokios sistemos kaip Microsoft Agent Framework palengvina kurti kelis agentus, kurie gali dirbti kartu.

**Kaip komandos gali tai naudoti**: komandos gali kurti agentus su specifinėmis rolėmis ir užduotimis, leidžiančius jiems testuoti ir tobulinti bendradarbiavimo darbo eigas bei pagerinti bendrą sistemos efektyvumą.

**Kaip tai veikia praktikoje**: galite sukurti agentų komandą, kur kiekvienas agentas atlieka specializuotą funkciją, pvz., duomenų rinkimą, analizę ar sprendimų priėmimą. Šie agentai gali bendrauti ir dalintis informacija, kad pasiektų bendrą tikslą, pvz., atsakyti į vartotojo užklausą ar baigti užduotį.

**Kodo pavyzdys (Microsoft Agent Framework)**:

```python
# Kuriami keli agentai, kurie dirba kartu, naudojant Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Duomenų paieškos agentas
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Duomenų analizės agentas
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Vykdyti agentus sekos tvarka užduočiai atlikti
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Ankstesniame kode matote, kaip galite sukurti užduotį, kurioje keli agentai bendradarbiauja duomenų analizei. Kiekvienas agentas atlieka specifinę funkciją, o užduotis vykdoma koordinuojant agentų veiksmus siekiant pageidaujamo rezultato. Kurdamas specializuotus agentus, galite pagerinti užduoties efektyvumą ir našumą.

### Mokymasis realiu laiku

Pažangios sistemos suteikia galimybes realiu laiku suprasti kontekstą ir prisitaikyti.

**Kaip komandos gali tai naudoti**: komandos gali įgyvendinti atsiliepimų ciklus, leidžiančius agentams mokytis iš sąveikų ir dinamiškai koreguoti savo elgesį, užtikrinant nuolatinį galimybių tobulinimą.

**Kaip tai veikia praktikoje**: agentai gali analizuoti vartotojų atsiliepimus, aplinkos duomenis ir užduočių rezultatus, atnaujinti savo žinių bazę, koreguoti sprendimų algoritmus ir laipsniškai gerinti našumą. Šis iteratyvus mokymosi procesas leidžia agentams prisitaikyti prie besikeičiančių sąlygų ir vartotojų pageidavimų, gerinant bendrą sistemos efektyvumą.

## Kokie yra skirtumai tarp Microsoft Agent Framework ir Microsoft Foundry Agent Service?

Yra daug būdų šias sistemas palyginti, bet pažvelkime į keletą pagrindinių skirtumų pagal jų dizainą, galimybes ir taikymo sritis:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework teikia supaprastintą SDK AI agentų kūrimui naudojant `FoundryChatClient`. Jis leidžia kūrėjams kurti agentus, kurie naudoja Azure OpenAI modelius su integruotu įrankių kvietimu, pokalbių valdymu ir įmonės lygio saugumu per Azure tapatybės valdymą.

**Naudojimo atvejai**: gamybos lygio AI agentų kūrimas su įrankių naudojimu, daugiažingsnėmis darbo eigomis ir įmonės integracijos scenarijais.

Štai keletas svarbių Microsoft Agent Framework pagrindinių koncepcijų:

- **Agentai**. Agentas sukuriamas per `FoundryChatClient` ir konfigūruojamas su vardu, instrukcijomis ir įrankiais. Agentas gali:
  - **Apdoroti vartotojo žinutes** ir generuoti atsakymus naudojant Azure OpenAI modelius.
  - **Automatiškai kviesti įrankius** pagal pokalbio kontekstą.
  - **Išlaikyti pokalbio būseną** per kelias sąveikas.

  Štai kodo fragmentas, rodantis, kaip sukurti agentą:

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

- **Įrankiai**. Sistema palaiko įrankių apibrėžimą kaip Python funkcijas, kurias agentas gali iškvieti automatiškai. Įrankiai registruojami agento kūrimo metu:

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

- **Daugiagentų koordinacija**. Galite kurti kelis agentus su skirtingomis specializacijomis ir koordinuoti jų darbą:

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

- **Azure tapatybės integracija**. Sistema naudoja `AzureCliCredential` (arba `DefaultAzureCredential`) saugiam ir be raktų autentifikavimui, eliminuodama būtinybę tiesiogiai tvarkyti API raktus.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service yra naujesnė paslauga, pristatyta Microsoft Ignite 2024 renginyje. Ji leidžia kurti ir paleisti AI agentus su lankstesniais modeliais, pavyzdžiui, tiesiogiai kviečiant atviro kodo LLM modelius kaip Llama 3, Mistral ir Cohere.

Microsoft Foundry Agent Service teikia stipresnes įmonių saugumo priemones ir duomenų saugojimo metodus, todėl tinka įmonių programoms.

Ji veikia paruošta naudoti kartu su Microsoft Agent Framework agentų kūrimui ir diegimui.

Ši paslauga šiuo metu yra viešojo peržiūros etape ir palaiko Python bei C# agentų kūrimui.

Naudojant Microsoft Foundry Agent Service Python SDK, galime sukurti agentą su vartotojo apibrėžtu įrankiu:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Apibrėžkite įrankių funkcijas
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

### Pagrindinės koncepcijos

Microsoft Foundry Agent Service pagrindinės koncepcijos yra šios:

- **Agentas**. Microsoft Foundry Agent Service integruojasi su Microsoft Foundry. Tarp Microsoft Foundry AI Agentas veikia kaip „protingas“ mikroservisas, kuris gali atsakyti į klausimus (RAG), vykdyti veiksmus arba visiškai automatizuoti darbo eigas. Tai pasiekiama derinant generatyvios AI modelius su įrankiais, leidžiančiais prieiti ir sąveikauti su realių duomenų šaltiniais. Štai agento pavyzdys:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Šiame pavyzdyje agentas sukurtas su modeliu `gpt-4.1-mini`, vardu `my-agent` ir instrukcija „Jūs esate naudingas agentas“. Agentas aprūpintas įrankiais ir resursais kodo interpretacijos užduotims atlikti.

- **Gija ir žinutės**. Gija yra dar viena svarbi koncepcija. Ji atspindi pokalbį ar sąveiką tarp agento ir vartotojo. Gijos gali būti naudojamos stebėti pokalbio eigą, saugoti kontekstinę informaciją ir valdyti sąveikos būseną. Štai gijos pavyzdys:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Paprašykite agento atlikti darbą su gija
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Pasiimkite ir užfiksuokite visus pranešimus, kad pamatytumėte agente atsakymą
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Ankstesniame kode sukurta gija. Vėliau į tą giją siunčiama žinutė. Kvietimu `create_and_process_run` agentui liepiama atlikti darbą gijoje. Galiausiai žinutės paimamos ir išvedamos, norint pamatyti agento atsakymą. Žinutės atspindi vartotojo ir agento pokalbio eigą. Taip pat svarbu suprasti, kad žinutės gali būti skirtingų tipų, pavyzdžiui, tekstas, paveikslėlis arba failas, tai reiškia, jog agento darbas gali būti, pavyzdžiui, paveikslėlio ar teksto atsakymas. Kūrėjas gali šią informaciją panaudoti atsakymui toliau apdoroti ar pateikti vartotojui.

- **Integracija su Microsoft Agent Framework**. Microsoft Foundry Agent Service sklandžiai veikia su Microsoft Agent Framework, tai reiškia, kad galite kurti agentus naudodami `FoundryChatClient` ir juos paleisti gamyboje per Agent Service.

**Naudojimo atvejai**: Microsoft Foundry Agent Service sukurta įmonių aplikacijoms, kurioms reikalingas saugus, masteliais pritaikomas ir lankstus AI agentų diegimas.

## Kokie yra skirtumai tarp šių požiūrių?
 
Atrodo, kad yra ir persidengimų, bet yra keletas pagrindinių skirtumų pagal dizainą, galimybes ir taikymo sritis:
 
- **Microsoft Agent Framework (MAF)**: yra gamybos lygio SDK AI agentų kūrimui. Jis teikia supaprastintą API agentams su įrankių kvietimu, pokalbių valdymu ir Azure tapatybės integracija.
- **Microsoft Foundry Agent Service**: yra Microsoft Foundry platforma ir diegimo paslauga agentams. Ji siūlo integruotą ryšį su tokiais servisais kaip Azure OpenAI, Azure AI Search, Bing Search ir kodo vykdymas.
 
Dar neapsisprendėte, ką rinktis?

### Naudojimo atvejai
 
Pažiūrėkime, ar galime jums padėti, apžvelgdami keletą dažnų naudojimo scenarijų:
 
> K: Kuriu gamybinius AI agentų sprendimus ir noriu greitai pradėti
>

>A: Microsoft Agent Framework yra puikus pasirinkimas. Jis suteikia paprastą, Python stilistikos API per `FoundryChatClient`, leidžiančią apibrėžti agentus su įrankiais ir instrukcijomis vos keliomis kodo eilutėmis.

>K: Man reikalingas įmonės lygio diegimas su Azure integracijomis kaip Search ir kodo vykdymas
>
> A: Microsoft Foundry Agent Service yra geriausias pasirinkimas. Tai platformos paslauga, teikianti integruotas galimybes keliems modeliams, Azure AI Search, Bing Search ir Azure Functions. Ji leidžia patogiai kurti agentus Foundry portale ir diegti juos dideliu mastu.
 
> K: Aš vis dar nesu tikras, tiesiog pasiūlyk man vieną galimybę
>
> A: Pradėkite nuo Microsoft Agent Framework agentų kūrimui, o kai reikės diegti ir mastelinti juos gamyboje, naudokite Microsoft Foundry Agent Service. Toks požiūris leidžia greitai kurti agentų logiką ir aiškiai pereiti prie įmonės diegimo.
 
Apibendrinkime pagrindinius skirtumus lentelėje:

| Sistema | Dėmesys | Pagrindinės koncepcijos | Naudojimo atvejai |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Supaprastinta agentų SDK su įrankių kvietimu | Agentai, Įrankiai, Azure tapatybė | AI agentų kūrimas, įrankių naudojimas, daugiažingsnės darbo eigos |
| Microsoft Foundry Agent Service | Lankstūs modeliai, įmonių saugumas, kodo generavimas, įrankių kvietimas | Moduliarumas, bendradarbiavimas, procesų orkestracija | Saugus, masteliais pritaikomas ir lankstus AI agentų diegimas |

## Ar galiu tiesiogiai integruoti savo esamus Azure ekosistemos įrankius, ar man reikia atskirų sprendimų?


Atsakymas yra taip, galite tiesiogiai integruoti savo esamus Azure ekosistemos įrankius su Microsoft Foundry Agent Service, ypač todėl, kad jis sukurtas sklandžiai veikti su kitomis Azure paslaugomis. Pavyzdžiui, galite integruoti Bing, Azure AI Search ir Azure Functions. Taip pat yra gilus integravimas su Microsoft Foundry.

Microsoft Agent Framework taip pat integruojasi su Azure paslaugomis per `FoundryChatClient` ir Azure identitetą, leidžiantį tiesiogiai iš agentų įrankių kviesti Azure paslaugas.

## Pavyzdiniai Kodo Pavyzdžiai

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Turite daugiau klausimų apie AI agentų sistemas?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), susitikite su kitais besimokančiais, dalyvaukite konsultacijose ir gaukite atsakymus į savo AI agentų klausimus.

## Nuorodos

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Ankstesnė pamoka

[Įvadas į AI agentus ir jų naudojimo atvejai](../01-intro-to-ai-agents/README.md)

## Kita pamoka

[Agentinių dizaino šablonų supratimas](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->