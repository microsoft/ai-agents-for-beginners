<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e056335d729ba6e49571db7a6533825d",
  "translation_date": "2025-10-11T11:15:31+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "et"
}
-->
[![Kuidas kujundada häid AI agente](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.et.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klõpsake ülaloleval pildil, et vaadata selle õppetunni videot)_

# Tööriistade kasutamise disainimuster

Tööriistad on huvitavad, kuna need võimaldavad AI agentidel omada laiemat võimekuste valikut. Kui agent saab kasutada tööriista, ei ole tema tegevused enam piiratud, vaid ta suudab täita mitmesuguseid ülesandeid. Selles peatükis vaatleme tööriistade kasutamise disainimustrit, mis kirjeldab, kuidas AI agendid saavad kasutada konkreetseid tööriistu oma eesmärkide saavutamiseks.

## Sissejuhatus

Selles õppetunnis püüame vastata järgmistele küsimustele:

- Mis on tööriistade kasutamise disainimuster?
- Millistes kasutusjuhtudes seda saab rakendada?
- Millised elemendid/ehitusplokid on vajalikud disainimustri rakendamiseks?
- Millised on erikaalutlused usaldusväärsete AI agentide loomisel, kasutades tööriistade kasutamise disainimustrit?

## Õppeesmärgid

Pärast selle õppetunni läbimist suudate:

- Defineerida tööriistade kasutamise disainimustri ja selle eesmärgi.
- Tuvastada kasutusjuhtumeid, kus tööriistade kasutamise disainimuster on rakendatav.
- Mõista peamisi elemente, mis on vajalikud disainimustri rakendamiseks.
- Tunnustada kaalutlusi, mis tagavad AI agentide usaldusväärsuse, kasutades seda disainimustrit.

## Mis on tööriistade kasutamise disainimuster?

**Tööriistade kasutamise disainimuster** keskendub sellele, et LLM-id (suured keelemudelid) saaksid suhelda väliste tööriistadega, et saavutada konkreetseid eesmärke. Tööriistad on kood, mida agent saab täita, et sooritada tegevusi. Tööriist võib olla lihtne funktsioon, näiteks kalkulaator, või API-kõne kolmanda osapoole teenusele, nagu aktsiahindade otsing või ilmaprognoos. AI agentide kontekstis on tööriistad loodud selleks, et agendid saaksid neid täita vastuseks **mudeli genereeritud funktsioonikõnedele**.

## Millistes kasutusjuhtudes seda saab rakendada?

AI agendid saavad kasutada tööriistu keerukate ülesannete täitmiseks, teabe hankimiseks või otsuste tegemiseks. Tööriistade kasutamise disainimustrit kasutatakse sageli olukordades, mis nõuavad dünaamilist suhtlust väliste süsteemidega, nagu andmebaasid, veebiteenused või kooditõlgid. See võimekus on kasulik mitmesugustes kasutusjuhtudes, sealhulgas:

- **Dünaamiline teabe hankimine:** Agendid saavad pärida väliseid API-sid või andmebaase, et hankida ajakohast teavet (nt päring SQLite andmebaasist andmeanalüüsiks, aktsiahindade või ilmainfo hankimine).
- **Koodi täitmine ja tõlgendamine:** Agendid saavad täita koodi või skripte, et lahendada matemaatilisi probleeme, koostada aruandeid või teha simulatsioone.
- **Töövoo automatiseerimine:** Korduvate või mitmeetapiliste töövoogude automatiseerimine, integreerides tööriistu nagu ülesannete planeerijad, e-posti teenused või andmetorud.
- **Klienditugi:** Agendid saavad suhelda CRM-süsteemide, piletiplatvormide või teadmistebaasidega, et lahendada kasutajate päringuid.
- **Sisu loomine ja redigeerimine:** Agendid saavad kasutada tööriistu, nagu grammatikakontrollijad, teksti kokkuvõtjad või sisuturvalisuse hindajad, et aidata sisuloome ülesannetes.

## Millised elemendid/ehitusplokid on vajalikud tööriistade kasutamise disainimustri rakendamiseks?

Need ehitusplokid võimaldavad AI agendil täita mitmesuguseid ülesandeid. Vaatame peamisi elemente, mis on vajalikud tööriistade kasutamise disainimustri rakendamiseks:

- **Funktsiooni/tööriista skeemid:** Saadaval olevate tööriistade üksikasjalikud kirjeldused, sealhulgas funktsiooni nimi, eesmärk, vajalikud parameetrid ja oodatavad väljundid. Need skeemid võimaldavad LLM-il mõista, millised tööriistad on saadaval ja kuidas koostada kehtivaid päringuid.

- **Funktsiooni täitmise loogika:** Määrab, kuidas ja millal tööriistu kasutatakse vastavalt kasutaja kavatsusele ja vestluse kontekstile. See võib hõlmata planeerimismooduleid, suunamismehhanisme või tingimuslikke vooge, mis määravad tööriistade kasutamise dünaamiliselt.

- **Sõnumite haldamise süsteem:** Komponendid, mis haldavad vestluse voogu kasutaja sisendite, LLM-i vastuste, tööriistakõnede ja tööriistade väljundite vahel.

- **Tööriistade integreerimise raamistik:** Infrastruktuur, mis ühendab agendi erinevate tööriistadega, olgu need lihtsad funktsioonid või keerulised välised teenused.

- **Vigade käsitlemine ja valideerimine:** Mehhanismid tööriistade täitmise ebaõnnestumiste käsitlemiseks, parameetrite valideerimiseks ja ootamatute vastuste haldamiseks.

- **Oleku haldamine:** Jälgib vestluse konteksti, varasemaid tööriistade interaktsioone ja püsivaid andmeid, et tagada järjepidevus mitme pöördega interaktsioonides.

Järgmisena vaatame funktsiooni/tööriista kõnesid lähemalt.

### Funktsiooni/tööriista kõned

Funktsioonikõned on peamine viis, kuidas võimaldame suurte keelemudelite (LLM) suhtlemist tööriistadega. Sageli kasutatakse "funktsiooni" ja "tööriista" vaheldumisi, kuna "funktsioonid" (taaskasutatava koodi plokid) on "tööriistad", mida agendid kasutavad ülesannete täitmiseks. Selleks, et funktsiooni kood täidetaks, peab LLM võrdlema kasutaja päringut funktsiooni kirjeldusega. Selleks saadetakse LLM-ile skeem, mis sisaldab kõigi saadaolevate funktsioonide kirjeldusi. LLM valib ülesande jaoks kõige sobivama funktsiooni ja tagastab selle nime ja argumendid. Valitud funktsioon täidetakse, selle vastus saadetakse tagasi LLM-ile, mis kasutab teavet kasutaja päringule vastamiseks.

Funktsioonikõnede rakendamiseks agentidele vajavad arendajad:

1. LLM-i mudelit, mis toetab funktsioonikõnesid
2. Skeemi, mis sisaldab funktsioonide kirjeldusi
3. Koodi iga kirjeldatud funktsiooni jaoks

Vaatame näidet, kuidas saada praegust aega linnas:

1. **LLM-i, mis toetab funktsioonikõnesid, initsialiseerimine:**

    Kõik mudelid ei toeta funktsioonikõnesid, seega on oluline kontrollida, kas kasutatav LLM seda teeb. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> toetab funktsioonikõnesid. Alustame Azure OpenAI kliendi initsialiseerimisest.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Funktsiooni skeemi loomine:**

    Järgmisena määratleme JSON-skeemi, mis sisaldab funktsiooni nime, funktsiooni eesmärgi kirjeldust ning funktsiooni parameetrite nimesid ja kirjeldusi. Seejärel edastame selle skeemi varem loodud kliendile koos kasutaja päringuga, et leida San Francisco aeg. Oluline on märkida, et tagastatakse **tööriistakõne**, mitte lõplik vastus küsimusele. Nagu varem mainitud, tagastab LLM ülesande jaoks valitud funktsiooni nime ja argumendid, mis sellele edastatakse.

    ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Funktsiooni kood, mis on vajalik ülesande täitmiseks:**

    Nüüd, kui LLM on valinud, millist funktsiooni tuleb käivitada, tuleb rakendada ja täita kood, mis ülesande täidab. Saame rakendada koodi praeguse aja saamiseks Pythonis. Samuti peame kirjutama koodi, et ekstraheerida vastuse sõnumist funktsiooni nimi ja argumendid, et saada lõplik tulemus.

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
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Funktsioonikõned on enamiku, kui mitte kõigi agentide tööriistade kasutamise disainide keskmes, kuid nende nullist rakendamine võib olla keeruline. Nagu õppisime [õppetunnis 2](../../../02-explore-agentic-frameworks), pakuvad agentide raamistikud meile eelnevalt ehitatud ehitusplokke tööriistade kasutamise rakendamiseks.

## Tööriistade kasutamise näited agentide raamistikuga

Siin on mõned näited, kuidas saate rakendada tööriistade kasutamise disainimustrit, kasutades erinevaid agentide raamistikke:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> on avatud lähtekoodiga AI raamistik .NET-i, Pythoni ja Java arendajatele, kes töötavad suurte keelemudelitega (LLM). See lihtsustab funktsioonikõnede kasutamist, kirjeldades automaatselt teie funktsioone ja nende parameetreid mudelile protsessi kaudu, mida nimetatakse <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialiseerimiseks</a>. Samuti haldab see mudeli ja teie koodi vahelist suhtlust. Teine eelis agentide raamistikuna nagu Semantic Kernel on see, et see võimaldab teil kasutada eelnevalt ehitatud tööriistu, nagu <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Failiotsing</a> ja <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Kooditõlgendaja</a>.

Järgmine diagramm illustreerib funktsioonikõnede protsessi Semantic Kerneliga:

![funktsioonikõned](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.et.png)

Semantic Kernelis nimetatakse funktsioone/tööriistu <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Pluginiteks</a>. Saame muuta varem nähtud `get_current_time` funktsiooni pluginaks, muutes selle klassiks, mille sees on funktsioon. Samuti saame importida `kernel_function` dekoratori, mis võtab funktsiooni kirjelduse. Kui loote kerneli GetCurrentTimePluginiga, serialiseerib kernel automaatselt funktsiooni ja selle parameetrid, luues skeemi, mida LLM-ile saata.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> on uuem agentide raamistik, mis on loodud selleks, et võimaldada arendajatel turvaliselt luua, juurutada ja skaleerida kvaliteetseid ning laiendatavaid AI agente, ilma et oleks vaja hallata aluseks olevaid arvutus- ja salvestusressursse. See on eriti kasulik ettevõtte rakendustes, kuna tegemist on täielikult hallatud teenusega, millel on ettevõtte tasemel turvalisus.

Võrreldes arendamisega otse LLM API-ga pakub Azure AI Agent Service mõningaid eeliseid, sealhulgas:

- Automaatne tööriistakõnede haldamine – pole vaja tööriistakõnet parsida, tööriista käivitada ja vastust käsitleda; kõik see tehakse nüüd serveripoolselt.
- Turvaliselt hallatud andmed – vestluse oleku haldamise asemel saate kasutada lõime, et salvestada kogu vajalik teave.
- Valmis tööriistad – tööriistad, mida saate kasutada oma andmeallikatega suhtlemiseks, nagu Bing, Azure AI Search ja Azure Functions.

Azure AI Agent Service'is saadaval olevad tööriistad jagunevad kahte kategooriasse:

1. Teadmiste tööriistad:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Searchi abil maandamine</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Failiotsing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Tegevustööriistad:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktsioonikõned</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kooditõlgendaja</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI määratletud tööriistad</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service võimaldab meil kasutada neid tööriistu koos `tööriistakomplektina`. Samuti kasutab see `lõime`, mis jälgib konkreetse vestluse sõnumite ajalugu.

Kujutage ette, et olete müügiesindaja ettevõttes nimega Contoso. Soovite arendada vestlusagenti, mis suudab vastata küsimustele teie müügiandmete kohta.

Järgmine pilt illustreerib, kuidas saaksite kasutada Azure AI Agent Service'i oma müügiandmete analüüsimiseks:

![Agentiteenuse kasutamine](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.et.jpg)

Nende tööriistade kasutamiseks teenusega saame luua kliendi ja määratleda tööriista või tööriistakomplekti. Selle praktiliseks rakendamiseks saame kasutada järgmist Pythoni koodi. LLM suudab vaadata tööriistakomplekti ja otsustada, kas kasutada kasutaja loodud funktsiooni `fetch_sales_data_using_sqlite_query` või eelnevalt ehitatud kooditõlgendajat, sõltuvalt kasutaja päringust.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Millised on erikaalutlused tööriistade kasutamise disainimustri rakendamisel usaldusväärsete AI agentide loomiseks?

LLM-ide poolt dünaamiliselt genereeritud SQL-i puhul on tavaliseks mureks turvalisus, eriti SQL-i süstimise või pahatahtlike toimingute, nagu andmebaasi kustutamine või rikkumine, risk. Kuigi need mured on õigustatud, saab neid tõhusalt leevendada, konfigureerides andmebaasi juurdepääsuõigused õigesti. Enamiku andmebaaside puhul hõlmab see andmebaasi seadistamist ainult lugemiseks. PostgreSQL-i või Azure SQL-i sarnaste andmebaasiteenuste puhul tuleks rakendusele määrata ainult lugemisõigusega (SELECT) roll.
Rakenduse käitamine turvalises keskkonnas suurendab veelgi kaitset. Ettevõtete stsenaariumides ekstraheeritakse ja töödeldakse andmeid tavaliselt operatsioonisüsteemidest kirjutuskaitstud andmebaasi või andmelaosse, millel on kasutajasõbralik skeem. See lähenemine tagab, et andmed on turvalised, optimeeritud jõudluse ja juurdepääsetavuse jaoks ning et rakendusel on piiratud, ainult lugemisõigusega juurdepääs.

### Kas sul on tööriista kasutamise disainimustrite kohta rohkem küsimusi?

Liitu [Azure AI Foundry Discordiga](https://aka.ms/ai-agents/discord), et kohtuda teiste õppijatega, osaleda vastuvõtutundides ja saada vastuseid oma AI Agentide küsimustele.

## Täiendavad ressursid

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agentide Teenuse Töötuba</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Töötuba</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Funktsioonikutsumise Õpetus</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Kooditõlgendaja</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tööriistad</a>

## Eelmine õppetund

[Agentlike disainimustrite mõistmine](../03-agentic-design-patterns/README.md)

## Järgmine õppetund

[Agentlik RAG](../05-agentic-rag/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.