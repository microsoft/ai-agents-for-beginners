[![AI agentų karkasų tyrinėjimas](../../../translated_images/lt/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Spustelėkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# AI agentų karkasų tyrinėjimas

AI agentų karkasai yra programinės įrangos platformos, sukurtos supaprastinti AI agentų kūrimą, diegimą ir valdymą. Šie karkasai suteikia kūrėjams iš anksto paruoštus komponentus, abstrakcijas ir įrankius, kurie palengvina sudėtingų AI sistemų kūrimą.

Šie karkasai padeda kūrėjams sutelkti dėmesį į jų programų unikalumą, teikdami standartizuotus požiūrius į įprastus AI agentų kūrimo iššūkius. Jie didina mastelį, prieinamumą ir efektyvumą kuriant AI sistemas.

## Įvadas

Šioje pamokoje aptarsime:

- Kas yra AI agentų karkasai ir ką jie leidžia kūrėjams pasiekti?
- Kaip komandos gali greitai kurti prototipus, iteruoti ir gerinti savo agentų galimybes?
- Kokie yra skirtumai tarp Microsoft sukurtų karkasų ir įrankių (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> ir <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Ar galiu tiesiogiai integruoti savo esamus Azure ekosistemos įrankius, arba man reikalingi savarankiški sprendimai?
- Kas yra Microsoft Foundry Agent Service ir kaip tai padeda man?

## Mokymosi tikslai

Šios pamokos tikslas – padėti jums suprasti:

- AI agentų karkasų vaidmenį AI kūrime.
- Kaip panaudoti AI agentų karkasus kuriant intelektualius agentus.
- Pagrindines galimybes, kurias suteikia AI agentų karkasai.
- Skirtumus tarp Microsoft Agent Framework ir Microsoft Foundry Agent Service.

## Kas yra AI agentų karkasai ir ką jie leidžia kūrėjams daryti?

Tradiciniai AI karkasai gali padėti integruoti AI į savo programėles ir pagerinti jas šiais būdais:

- **Personalizacija**: AI gali analizuoti vartotojo elgseną ir pageidavimus, kad pateiktų suasmenintus pasiūlymus, turinį ir patirtį.
Pavyzdys: Transliavimo paslaugos, tokios kaip Netflix, naudoja AI siūlydamos filmus ir laidas pagal peržiūrų istoriją, didindamos vartotojų įsitraukimą ir pasitenkinimą.
- **Automatizavimas ir efektyvumas**: AI gali automatizuoti pasikartojančias užduotis, optimizuoti darbo procesus ir gerinti veiklos efektyvumą.
Pavyzdys: Klientų aptarnavimo programėlės naudoja AI pagrįstus pokalbių robotus dažniems užklausimams aptarnauti, trumpindamos atsakymo laiką ir atlaisvindamos žmonių agentus sudėtingesniems klausimams.
- **Pagerinta naudotojo patirtis**: AI gali pagerinti bendrą naudotojo patirtį teikdama išmanias funkcijas, tokias kaip balso atpažinimas, natūralios kalbos apdorojimas ir prognozuojamas tekstas.
Pavyzdys: Virtualūs asistentai, tokie kaip Siri ir Google Assistant, naudoja AI suprasti ir atsakyti į balso komandas, palengvindami naudotojų sąveiką su įrenginiais.

### Viskas skamba puikiai, todėl kodėl mums reikia AI agentų karkaso?

AI agentų karkasai yra daugiau nei tik AI karkasai. Jie skirti leisti kurti intelektualius agentus, kurie gali bendrauti su vartotojais, kitais agentais ir aplinka, siekiant konkrečių tikslų. Šie agentai gali demonstruoti autonominį elgesį, priimti sprendimus ir prisitaikyti prie besikeičiančių sąlygų. Pažiūrėkime į pagrindines AI agentų karkasų suteikiamas galimybes:

- **Agentų bendradarbiavimas ir koordinacija**: Leidžia kurti kelis AI agentus, kurie gali dirbti kartu, bendrauti ir koordinuotis sprendžiant sudėtingas užduotis.
- **Užduočių automatizavimas ir valdymas**: Teikia mechanizmus daugiažingsniams darbo eigos automatizavimui, užduočių delegavimui ir dinamiškam užduočių valdymui agentų tarpe.
- **Kontekstinis supratimas ir prisitaikymas**: Aprūpina agentus gebėjimu suprasti kontekstą, prisitaikyti prie besikeičiančios aplinkos ir priimti sprendimus remiantis realaus laiko informacija.

Taigi apibendrinant, agentai leidžia jums daugiau, pakelia automatizavimą į aukštesnį lygį, kuria protingesnes sistemas, kurios gali prisitaikyti ir mokytis iš savo aplinkos.

## Kaip greitai kurti prototipus, iteruoti ir gerinti agentų galimybes?

Tai sparčiai kintanti sritis, bet daugelyje AI agentų karkasų yra bendrų elementų, kurie padeda greitai kurti prototipus ir iteruoti, tai yra moduliniai komponentai, bendradarbiavimo įrankiai ir realaus laiko mokymasis. Pažiūrėkime į juos:

- **Naudokite moduliarius komponentus**: AI SDK siūlo iš anksto paruoštus komponentus, tokius kaip AI ir atminties jungtys, funkcijų iškvietimas naudojant natūralią kalbą arba kodo papildinius, užklausų šablonus ir daugiau.
- **Išnaudokite bendradarbiavimo įrankius**: Kurkite agentus su konkrečiomis rolėmis ir užduotimis, leidžiančiais testuoti ir tobulinti bendradarbiavimo darbo eigas.
- **Mokykitės realiu laiku**: Įgyvendinkite atsiliepimų ciklus, kur agentai mokosi iš sąveikų ir dinamiškai keičia elgesį.

### Naudokite moduliarius komponentus

Tokie SDK kaip Microsoft Agent Framework siūlo iš anksto paruoštus komponentus, pvz., AI jungtis, įrankių apibrėžimus ir agentų valdymą.

**Kaip komandos gali tai panaudoti**: Komandos gali greitai surinkti šiuos komponentus, kad sukurtų funkcionalų prototipą nepradėdamos nuo nulio, leidžiant greitai eksperimentuoti ir iteruoti.

**Kaip tai veikia praktikoje**: Galite naudoti iš anksto paruoštą analizatorių informacijai iš vartotojo įvesties išgauti, atminties modulį duomenims saugoti ir atkurti, bei užklausų generatorių, kad bendrautumėte su vartotojais, visa tai neteikdami šių komponentų patys.

**Kodo pavyzdys**. Pažiūrėkime, kaip naudoti Microsoft Agent Framework su `FoundryChatClient`, kad modelis atsakytų į vartotojo įvestį įrankių iškvietimu:

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
    # Pavyzdinis išvestis: Jūsų skrydis į Niujorką 2025 m. sausio 1 d. sėkmingai užsakytas. Linkime saugios kelionės! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Iš šio pavyzdžio matyti, kaip galite panaudoti iš anksto paruoštą analizatorių, kad iš vartotojo įvesties išgautumėte pagrindinę informaciją, pvz., kilmę, paskirties vietą ir skrydžio užsakymo datą. Šis modulinis požiūris leidžia sutelkti dėmesį į aukšto lygio logiką.

### Išnaudokite bendradarbiavimo įrankius

Tokie karkasai kaip Microsoft Agent Framework palengvina kelių agentų, kurie gali dirbti kartu, kūrimą.

**Kaip komandos gali tai panaudoti**: Komandos gali kurti agentus su konkrečiomis rolėmis ir užduotimis, leidžiančiais testuoti ir tobulinti bendradarbiavimo darbo procesus bei gerinti bendrą sistemos efektyvumą.

**Kaip tai veikia praktikoje**: Galite sukurti agentų komandą, kur kiekvienas agentas turi specializuotą funkciją, pvz., duomenų gavimą, analizę ar sprendimų priėmimą. Šie agentai gali bendrauti ir dalytis informacija, siekdami bendro tikslo, pvz., atsakyti į vartotojo užklausą ar atlikti užduotį.

**Kodo pavyzdys (Microsoft Agent Framework)**:

```python
# Sukuriant kelis agentus, kurie dirba kartu, naudojant Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Duomenų gavimo agentas
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

# Paleisti agentus iš eilės atliekant užduotį
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Ankstesniame kode matote, kaip sukurti užduotį, kurioje keli agentai dirba kartu analizuodami duomenis. Kiekvienas agentas atlieka konkrečią funkciją, o užduotis vykdoma koordinuojant agentų darbą siekiant norimo rezultato. Kurdamas agentus su specializuotomis rolėmis galite pagerinti užduočių efektyvumą ir našumą.

### Mokykitės realiu laiku

Pažangūs karkasai suteikia galimybes realiu laiku suprasti kontekstą ir prisitaikyti.

**Kaip komandos gali tai panaudoti**: Komandos gali įgyvendinti atsiliepimų ciklus, kuriuose agentai mokosi iš sąveikų ir dinamiškai koreguoja savo elgesį, taip nuolat gerindami ir tobulindami savo galimybes.

**Kaip tai veikia praktikoje**: Agentai gali analizuoti vartotojų atsiliepimus, aplinkos duomenis ir užduočių rezultatus, atnaujinti savo žinių bazę, koreguoti sprendimų algoritmus ir gerinti veikimą laikui bėgant. Šis iteratyvus mokymosi procesas leidžia agentams prisitaikyti prie kintančių sąlygų ir vartotojų pageidavimų, didinant bendrą sistemos efektyvumą.

## Kokie skirtumai tarp Microsoft Agent Framework ir Microsoft Foundry Agent Service?

Yra daug būdų palyginti šiuos požiūrius, bet pažvelkime į pagrindinius skirtumus jų dizaino, galimybių ir tikslinių panaudojimo atvejų atžvilgiu:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework suteikia supaprastintą SDK AI agentų kūrimui naudojant `FoundryChatClient`. Jis leidžia kūrėjams kurti agentus, kurie naudoja Azure OpenAI modelius su įmontuotu įrankių iškvietimu, pokalbių valdymu ir įmonės lygio saugumu per Azure identifikaciją.

**Panaudojimo atvejai**: Gamybai paruoštų AI agentų kūrimas su įrankių naudojimu, daugiažingsniais darbo srautais ir įmonės integracijos scenarijais.

Štai keletas svarbių Microsoft Agent Framework pagrindinių konceptų:

- **Agentai**. Agentas sukuriamas per `FoundryChatClient` ir konfigūruojamas su pavadinimu, instrukcijomis ir įrankiais. Agentas gali:
  - **Apdoroti vartotojo žinutes** ir generuoti atsakymus naudodamas Azure OpenAI modelius.
  - **Automatiškai iškviesti įrankius** pagal pokalbio kontekstą.
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

- **Įrankiai**. Framework palaiko įrankių apibrėžimą kaip Python funkcijas, kurias agentas gali automatiškai kvieti. Įrankiai registruojami agento kūrimo metu:

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

- **Azure identifikacijos integracija**. Framework naudoja `AzureCliCredential` (arba `DefaultAzureCredential`) saugiam autentifikavimui be raktų valdymo, pašalindamas poreikį tiesiogiai tvarkyti API raktus.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service yra naujesnis sprendimas, pristatytas Microsoft Ignite 2024 renginyje. Jis leidžia kurti ir diegti AI agentus su lankstesniais modeliais, pavyzdžiui, tiesiogiai kviečiant atvirojo kodo LLM, tokius kaip Llama 3, Mistral ir Cohere.

Microsoft Foundry Agent Service suteikia griežtesnes įmonių saugumo priemones ir duomenų saugojimo metodus, todėl tinka įmonių programėlėms.

Jis veikia be papildomų konfigūracijų kartu su Microsoft Agent Framework agentų kūrimui ir diegimui.

Ši paslauga šiuo metu yra viešojo peržiūros (Public Preview) stadijoje ir palaiko Python bei C# agentų kūrimui.

Naudodami Microsoft Foundry Agent Service Python SDK galime sukurti agentą su vartotojo apibrėžtu įrankiu:

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

### Pagrindinės sąvokos

Microsoft Foundry Agent Service apima šias pagrindines sąvokas:

- **Agentas**. Microsoft Foundry Agent Service integruojasi su Microsoft Foundry. Žmogaus agentas Microsoft Foundry veikia kaip "išmanioji" mikroserviso funkcija, kuri gali atsakyti į klausimus (RAG), atlikti veiksmus arba visiškai automatizuoti darbo eigas. Tai įgyvendinama derinant generatyviųjų AI modelių galybę su įrankiais, leidžiančiais prieiti ir bendrauti su realaus pasaulio duomenų šaltiniais. Štai agento pavyzdys:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Šiame pavyzdyje agentas sukurtas su modeliu `gpt-5-mini`, pavadinimu `my-agent`, ir instrukcijomis `You are helpful agent`. Agentui suteikti įrankiai ir ištekliai, kad atliktų kodo interpretavimo užduotis.

- **Pokalbio gija ir žinutės**. Gija yra dar vienas svarbus konceptas. Ji atspindi pokalbį arba sąveiką tarp agento ir vartotojo. Gijos gali būti naudojamos sekti pokalbio eigą, saugoti kontekstinę informaciją ir valdyti sąveikos būseną. Štai gijos pavyzdys:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Paprašykite agento atlikti darbą su gija
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Gaukite ir užfiksuokite visus pranešimus, kad pamatytumėte agento atsakymą
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Ankstesniame kode sukurta gija, tada į ją išsiųsta žinutė. Iškvietus `create_and_process_run` agentas paprašomas atlikti darbą gijoje. Galiausiai gaunamos žinutės, kurios užregistruojamos norint pamatyti agento atsakymą. Žinutės rodo pokalbio eigą tarp vartotojo ir agento. Taip pat svarbu suprasti, kad žinutės gali būti įvairių tipų, pavyzdžiui, tekstinės, vaizdinės ar failų tipo – tai reiškia, kad agentų darbas galėjo rezultatuoti pavyzdžiui į vaizdą arba tekstinį atsakymą. Kaip kūrėjas, galite toliau apdoroti šią informaciją arba pateikti ją vartotojui.

- **Integracija su Microsoft Agent Framework**. Microsoft Foundry Agent Service sklandžiai veikia su Microsoft Agent Framework, tai reiškia, kad galite kurti agentus naudodami `FoundryChatClient` ir diegti juos per Agent Service gamybos scenarijose.

**Panaudojimo atvejai**: Microsoft Foundry Agent Service skirta įmonių programėlėms, reikalaujančioms saugaus, mastelio ir lankstaus AI agentų diegimo.

## Kuo skiriasi šie požiūriai?
 
Nors atrodo, kad yra persidengimų, tačiau yra svarbių skirtumų dizaino, galimybių ir panaudojimo atvejų požiūriu:
 
- **Microsoft Agent Framework (MAF)**: Produkcijai paruoštas SDK AI agentų kūrimui. Suteikia supaprastintą API agentų kūrimui su įrankių iškvietimu, pokalbių valdymu ir Azure tapatybės integracija.
- **Microsoft Foundry Agent Service**: Platforma ir diegimo paslauga Microsoft Foundry agentams. Siūlo įmontuotą jungtį su paslaugomis kaip Azure OpenAI, Azure AI Search, Bing Search ir kodo vykdymą.
 
Vis dar nežinote, ką pasirinkti?

### Panaudojimo atvejai
 
Peržvelkime keletą dažnų panaudojimo atvejų ir pažiūrėkime, ar galime jums padėti:
 
> K: Kuriu gamybinius AI agentų sprendimus ir noriu greitai pradėti
>

>A: Microsoft Agent Framework yra puikus pasirinkimas. Jis suteikia paprastą, Python stiliaus API per `FoundryChatClient`, leidžiančią apibrėžti agentus su įrankiais ir instrukcijomis vos keliais kodo eilutėmis.

>K: Man reikia įmonių lygio diegimo su Azure integracijomis, tokiomis kaip Search ir kodo vykdymas
>
> A: Microsoft Foundry Agent Service yra geriausias pasirinkimas. Tai platformos paslauga, suteikianti įmontuotas galimybes keliems modeliams, Azure AI Search, Bing Search ir Azure Functions. Su ja galima lengvai kurti agentus Foundry portale ir diegti juos mastu.
 
> K: Dar nesu tikras, tiesiog duokite vieną pasirinkimą
>
> A: Pradėkite nuo Microsoft Agent Framework agentų kūrimui, o kai reikės gamybos diegimo ir mastelio, naudokite Microsoft Foundry Agent Service. Šis požiūris leidžia greitai iteruoti agentų logiką ir turėti aiškų kelią į įmonių diegimą.
 
Apibendrinkime pagrindinius skirtumus lentelėje:

| Framework | Dėmesys | Pagrindinės sąvokos | Panaudojimo atvejai |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Supaprastintas agentų SDK su įrankių iškvietimu | Agentai, Įrankiai, Azure tapatybė | AI agentų kūrimas, įrankių naudojimas, daugiažingsnės darbo eigos |
| Microsoft Foundry Agent Service | Lankstūs modeliai, įmonių saugumas, kodo generavimas, įrankių iškvietimas | Moduliarumas, Bendradarbiavimas, Procesų orkestravimas | Saugus, mastomas ir lankstus AI agentų diegimas |

## Ar galiu tiesiogiai integruoti savo esamus Azure ekosistemos įrankius, ar man reikia savarankiškų sprendimų?


Atsakymas yra taip, savo esamus Azure ekosistemos įrankius galite tiesiogiai integruoti su Microsoft Foundry Agent Service, ypač kadangi jis buvo sukurtas sklandžiai veikti su kitomis Azure paslaugomis. Pavyzdžiui, galite integruoti Bing, Azure AI Search ir Azure Functions. Taip pat yra gilus integravimas su Microsoft Foundry.

Microsoft Agent Framework taip pat integruojasi su Azure paslaugomis per `FoundryChatClient` ir Azure tapatybę, leidžiant jums tiesiogiai kviesti Azure paslaugas iš savo agentų įrankių.

## Pavyzdiniai kodai

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Turite daugiau klausimų apie AI agentų karkasus?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kad susitiktumėte su kitais mokytojais, dalyvautumėte konsultacijose ir gautumėte atsakymus į savo AI agentų klausimus.

## Nuorodos

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Ankstesnė pamoka

[Įvadas į AI agentus ir agentų naudojimo atvejus](../01-intro-to-ai-agents/README.md)

## Kitoji pamoka

[Agentinės dizaino šablonų supratimas](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->