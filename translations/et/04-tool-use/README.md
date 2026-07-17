[![Kuidas disainida head AI agente](../../../translated_images/et/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klõpsake ülaloleval pildil, et vaadata selle õppetunni videot)_

# Tööriistade kasutamise disainimuster

Tööriistad on huvitavad, kuna võimaldavad tehisintellekti agentidel omada laiemat võimekuse valikut. Selle asemel, et agendil oleks piiratud tegevuste komplekt, mida ta saab teha, saab tööriista lisamisega agent nüüd teha palju erinevaid tegevusi. Selles peatükis vaatleme tööriistade kasutamise disainimustrit, mis kirjeldab, kuidas tehisintellekti agentid saavad kasutada konkreetseid tööriistu oma eesmärkide saavutamiseks.

## Sissejuhatus

Selles õppetükis püüame vastata järgmistele küsimustele:

- Mis on tööriistade kasutamise disainimuster?
- Millistes kasutusjuhtumites seda saab rakendada?
- Millised elemendid/ehituskivid on disainimustri rakendamiseks vajalikud?
- Millised on erilised kaalutlused tööriistade kasutamise disainimustri kasutamisel usaldusväärsete AI agentide loomiseks?

## Õpieesmärgid

Pärast selle õppetüki läbimist suudate:

- Määratleda tööriistade kasutamise disainimuster ja selle eesmärgi.
- Tuvastada kasutusjuhtumeid, kus tööriistade kasutamise disainimuster tuleb rakendada.
- Mõista peamisi elemente, mis on vajalikud disainimustri rakendamiseks.
- Tunnustada kaalutlusi usaldusväärsuse tagamiseks AI agentide puhul, kes kasutavad seda disainimustrit.

## Mis on tööriistade kasutamise disainimuster?

**Tööriistade kasutamise disainimuster** keskendub sellele, et anda LLM-idele võime suhelda väliste tööriistadega, et saavutada kindlaid eesmärke. Tööriistad on kood, mida agent saab käivitada tegevuste sooritamiseks. Tööriist võib olla lihtne funktsioon nagu kalkulaator või API kõne kolmanda osapoole teenusele, näiteks aktsiahindade otsing või ilmastikuennustus. AI agentide kontekstis on tööriistad disainitud olema täidetavad agentide poolt vastusena **mudeli poolt genereeritud funktsiooni kõnedele**.

## Millistes kasutusjuhtumites seda saab rakendada?

AI agentidel on võimalik tööriistu kasutada keerukate ülesannete täitmiseks, teabe hankimiseks või otsuste tegemiseks. Tööriistade kasutamise disainimustrit kasutatakse sageli olukordades, kus on vaja dünaamilist suhtlust väliste süsteemidega, nagu andmebaasid, veebiteenused või koodi tõlgendajad. See võimekus on kasulik mitmesugusteks kasutusjuhtumiteks, sealhulgas:

- **Dünaamiline info hankimine:** Agendid saavad pärida väliseid API-sid või andmebaase, et saada ajakohastatud andmeid (nt SQLite andmebaasi päring andmeanalüüsiks, aktsiahindade või ilmaandmete toomine).
- **Koodi täitmine ja tõlgendamine:** Agendid saavad käivitada koodi või skripte matemaatiliste probleemide lahendamiseks, aruannete genereerimiseks või simulatsioonide läbiviimiseks.
- **Töövoogude automatiseerimine:** Korduvate või mitmeastmeliste töövoogude automatiseerimine, integreerides tööriistu nagu ülesannete ajastajad, e-posti teenused või andmepuurid.
- **Klienditugi:** Agendid saavad suhelda kliendisuhete juhtimise süsteemide, piletihaldusplatvormide või teadmistebaasidega, et lahendada kasutajaküsimusi.
- **Sisu genereerimine ja redigeerimine:** Agendid saavad kasutada tööriistu nagu grammatikakontrollijad, teksti kokkuvõtjad või sisu ohutuse hindajad, et aidata sisuloomet.

## Millised elemendid/ehituskivid on tööriistade kasutamise disainimustri rakendamiseks vajalikud?

Need ehituskivid võimaldavad AI agendil täita mitmesuguseid ülesandeid. Vaatame peamisi elemente, mis on vajalikud tööriistade kasutamise disainimustri rakendamiseks:

- **Funktsioonide/tööriistade skeemid**: Detailne kirjeldus saadaval olevatest tööriistadest, sealhulgas funktsiooni nimi, eesmärk, vajalikud parameetrid ja oodatud väljundid. Need skeemid võimaldavad LLM-il mõista, millised tööriistad on olemas ja kuidas koostada kehtivaid taotlusi.

- **Funktsiooni täitmise loogika**: Määrab, kuidas ja millal tööriistu kutsutakse vastavalt kasutaja kavatsusele ja vestluse kontekstile. See võib hõlmata planeerija mooduleid, marsruutimismehhanisme või tingimuslikke vooge, mis dynaamiliselt otsustavad tööriista kasutamise.

- **Sõnumite käsitlemise süsteem**: Komponendid, mis haldavad vestlust kasutaja sisendi, LLM vastuste, tööriista kõnede ja tööriistaväljundite vahel.

- **Tööriistade integreerimise raamistik**: Infrastruktuur, mis ühendab agendi erinevate tööriistadega, olgu need siis lihtsad funktsioonid või keerukad välised teenused.

- **Vigade käsitlemine ja valideerimine**: Mehhanismid tööriista täitmise vigade käsitlemiseks, parameetrite valideerimiseks ja ootamatute vastuste haldamiseks.

- **Oleku haldamine**: Jälgib vestluse konteksti, varasemaid tööriistakõnesid ja püsivaid andmeid, et tagada järjepidevus mitmevoorulistes suhetes.

Järgnevalt vaatleme funktsiooni/tööriista kutsumist lähemalt.
 
### Funktsiooni/tööriista kutsumine

Funktsiooni kutsumine on peamine viis, kuidas võimaldada suurte keelemudelite (LLM) kasutamist tööriistadega suhtlemiseks. Sageli kasutatakse sõnu „funktsioon“ ja „tööriist“ vaheldumisi, sest „funktsioonid“ (taaskasutatav koodiplokk) on tööriistad, mida agendid kasutavad ülesannete täitmiseks. Selleks, et funktsiooni koodi kutsuda, peab LLM võrdlema kasutaja taotlust funktsiooni kirjeldusega. Selleks saadetakse LLM-ile skeem, mis sisaldab kirjeldusi kõigist saadaval olevatest funktsioonidest. LLM valib ülesande jaoks sobivama funktsiooni, tagastab selle nime ja argumendid. Valitud funktsioon kutsutakse välja, selle vastus saadetakse tagasi LLM-ile, kes kasutab seda informatsiooni kasutaja taotlusele vastamiseks.

Arendajatel, kes soovivad agentidele funktsiooni kutsumist rakendada, on vaja:

1. LLM mudelit, mis toetab funktsiooni kutsumist
2. Skeemi, mis sisaldab funktsioonide kirjeldusi
3. Koodi iga kirjeldusega funktsiooni jaoks

Näiteks võtame kohaliku aja saamiseks linnas:

1. **Algata LLM, mis toetab funktsiooni kutsumist:**

    Mitte kõik mudelid ei toeta funktsiooni kutsumist, seega on oluline kontrollida, kas kasutatav LLM seda toetab.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> toetab funktsiooni kutsumist. Saame alustada OpenAI kliendi initsialiseerimisest Azure OpenAI **Responses API** vastu (stabiilse `/openai/v1/` lõpp-punkti kasutamine — `api_version` pole vajalik). 

    ```python
    # Algatage OpenAI klient Azure OpenAI jaoks (Responses API, v1 lõpp-punkt)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Loo funktsiooni skeem**:

    Järgmiseks määratleme JSON-skeemi, mis sisaldab funktsiooni nime, selle tegevuse kirjelduse ning parameetrite nimed ja kirjeldused.
    Seejärel edastame selle skeemi koos kasutaja taotlusega, kes soovib teada saada aega San Franciscos. Oluline on märkida, et tagastatakse **tööriista kõne**, **mitte** lõplik vastus küsimusele. Nagu eelnevalt mainitud, tagastab LLM ülesande jaoks valitud funktsiooni nime ja argumendid.

    ```python
    # Funktsiooni kirjeldus mudeli lugemiseks (Responses API flat tööriista formaat)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # Esialgne kasutaja sõnum
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Esimene API kõne: Palu mudelil kasutada funktsiooni
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Vastuste API tagastab tööriista kõned funktsioonikõne üksustena vastuses.output.
    # Lisa need vestlusesse, et mudelil oleks järgmisel sammul täielik kontekst.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Funktsiooni kood ülesande täitmiseks:**

    Nüüd, kui LLM on valinud, millist funktsiooni tuleb käivitada, tuleb ülesande täitmiseks vajalik kood implementeerida ja käivitada.
    Saame Pythonis kirjutada koodi, mis tagastab kohaliku aja. Samuti on vaja kirjutada kood, mis ekstraheerib response_message'st funktsiooni nime ja argumendid, et saada lõplik tulemus.

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
    # Töötle funktsioonikõnesid
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Tagasta tööriista tulemus funktsioonikõne väljundi elemendina
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Teine API kõne: saa mudeli lõplik vastus
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Funktsiooni kutsumine on enamiku, kui mitte kõigi agentide tööriistade kasutamise disainide süda, kuid selle nullist realiseerimine võib olla mõnikord keeruline.
Nagu õppisime [Õppetükk 2](../../../02-explore-agentic-frameworks) raames, pakuvad agenti raamistikes ette ehitatud ehituskive tööriistade kasutamise rakendamiseks.
 
## Tööriistade kasutamise näited agenti raamistikuga

Siin on mõned näited, kuidas saate tööriistade kasutamise disainimustri rakendada erinevate agenti raamistikute abil:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> on avatud lähtekoodiga tehisintellekti raamistik AI agentide loomiseks. See lihtsustab funktsiooni kutsumise protsessi, võimaldades teil määratleda tööriistad Python funktsioonidena kasutades `@tool` dekoratiivfunktsiooni. Raamistik haldab mudeli ja teie koodi vahelist suhtlust. Samuti annab see ligipääsu eelnevalt ehitatud tööriistadele nagu Failiotsing ja Koodi Tõlgendaja, millele pääseb ligi `FoundryChatClient` kaudu.

Järgmine diagramm illustreerib funktsiooni kutsumise protsessi Microsoft Agent Framework'is:

![function calling](../../../translated_images/et/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Frameworkis määratakse tööriistad kaunistatud funktsioonidena. Saame eelmainitud `get_current_time` funktsiooni muuta tööriistaks, kasutades `@tool` dekoratiivfunktsiooni. Raamistik serialiseerib funktsiooni ja selle parameetrid automaatselt, luues skeemi, mis saadetakse LLM-ile.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Loo klient
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Loo agent ja käivita see tööriistaga
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> on uuem agenti raamistik, mis on loodud selleks, et võimaldada arendajatel turvaliselt luua, juurutada ja skaleerida kvaliteetseid ning laiendatavaid AI agente ilma vajaduseta hallata aluseks olevaid arvutus- ja salvestusressursse. See sobib eriti hästi ettevõtte rakendustega, kuna on täielikult hallatav teenus ettevõtte taseme turvalisusega.

Võrreldes otse LLM API kasutamisega pakub Microsoft Foundry Agent Service mitmeid eeliseid, sealhulgas:

- Automaatne tööriistade kutsumine – pole vaja ise tööriista kutsumist parsida, tööriista vallandada ja vastust hallata; kogu see protsess toimub nüüd serveripoolt
- Turvaliselt hallatud andmed – selle asemel, et hallata oma vestluse olekut, võite tugineda lõimedele, mis salvestavad kogu vajaliku info
- Out-of-the-box tööriistad – tööriistad, mida saate kasutada oma andmeallikatega suhtlemiseks, nagu Bing, Azure AI Search ja Azure Functions.

Microsoft Foundry Agent Service'is olevad tööriistad saab jagada kahte kategooriasse:

1. Teadmiste tööriistad:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search põhjaline otsing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Failiotsing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Tegevuse tööriistad:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktsiooni kutsumine</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Koodi tõlgendaja</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI määratletud tööriistad</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service võimaldab meil neid tööriistu kasutada koos kui `toolset` (tööriistakomplekt). See kasutab ka `lõime` (threads), mis jälgivad konkreetse vestluse sõnumite ajalugu.

Kujutage ette, et olete müügiesindaja ettevõttes nimega Contoso. Soovite arendada vestlusagent, kes suudab vastata küsimustele teie müügiandmete kohta.

Järgmine pilt illustreerib, kuidas saaksite Microsoft Foundry Agent Service'i kasutada oma müügiandmete analüüsimiseks:

![Agentic Service In Action](../../../translated_images/et/agent-service-in-action.34fb465c9a84659e.webp)

Nende tööriistade kasutamiseks teenusega saame luua kliendi ja määratleda tööriista või tööriistade komplekti. Seda praktiliselt rakendades võime kasutada järgmist Python koodi. LLM saab vaadata tööriistade komplekti ja otsustada, kas kasutada kasutaja loodud funktsiooni `fetch_sales_data_using_sqlite_query` või eelnevalt ehitatud Koodi Tõlgendajat vastavalt kasutaja taotlusele.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query funktsioon, mida saab leida failist fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initsialiseeri tööriistakomplekt
toolset = ToolSet()

# Initsialiseeri funktsioonide kutsumise agent koos fetch_sales_data_using_sqlite_query funktsiooniga ja lisa see tööriistakomplekti
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initsialiseeri Koodi Tõlgendi tööriist ja lisa see tööriistakomplekti.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Millised on erilised kaalutlused tööriistade kasutamise disainimustri kasutamisel usaldusväärsete AI agentide loomiseks?

Ühine mure SQL-i dünaamilise genereerimise puhul LLM-ide poolt on turvalisus, eriti SQL süstimise või pahatahtlike tegevuste oht, nagu andmebaasi kustutamine või muutmine. Kuigi need ohud on õigustatud, saab neid efektiivselt leevendada, konfigureerides andmebaasi ligipääsu õigusi nõuetekohaselt. Enamiku andmebaaside puhul tähendab see andmebaasi seadistamist ainult lugemisõiguslikuks. Selliste teenuste nagu PostgreSQL või Azure SQL puhul peaks rakendusele määrama lugemisõigusega (SELECT) rolli.

Rakenduse käitamine turvalises keskkonnas tugevdab veelgi kaitset. Ettevõtte stsenaariumites ekstraheeritakse ja muudetakse andmeid tavaliselt operatsioonisüsteemidest lugemisõigusliku andmebaasi või andmelao jaoks kasutajasõbraliku skeemiga. See lähenemine tagab, et andmed on turvalised, optimeeritud jõudluseks ja ligipääsetavuseks ning rakendusel on piiratud, ainult lugemisõigus.

## Näidiskoodid

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Kas teil on rohkem küsimusi tööriistade kasutamise disainimustrite kohta?

Liituge [Microsoft Foundry Discordi](https://discord.com/invite/ATgtXmAS5D) kogukonnaga, et kohtuda teiste õppijatega, osaleda küsimuste-tundides ja saada vastused oma AI agentide küsimustele.

## Täiendavad ressursid

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agentide teenuse töötuba</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer mitmeagentide töötuba</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Frameworki ülevaade</a>


## Selle Agendi Suitsetestimine (Valikuline)

Pärast seda, kui õpite agente juurutama [Õppetükk 16](../16-deploying-scalable-agents/README.md), saate suitsutesti teha selle õppetüki `TravelToolAgent`-i jaoks (kas see ikka kasutab oma tööriistu ja vastab?) faili [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) abil. Vaadake, kuidas seda käivitada, failist [`tests/README.md`](../tests/README.md).

## Eelmine õppetükk

[Agentse disainimustrite mõistmine](../03-agentic-design-patterns/README.md)

## Järgmine õppetükk

[Agentne RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->