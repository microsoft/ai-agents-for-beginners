[![Kuidas kujundada häid tehisintellekti agente](../../../translated_images/et/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klõpsake ülaloleval pildil, et vaadata selle tunni videot)_

# Tööriistade kasutamise disainimuster

Tööriistad on huvitavad, kuna need võimaldavad tehisintellekti agentidel omada laiemat suutlikkust. Selle asemel, et agentil oleks piiratud hulk tegevusi, mida ta teha saab, võimaldab tööriista lisamine agendil nüüd teha mitmesuguseid toiminguid. Selles peatükis vaatleme Tööriistade kasutamise disainimustrit, mis kirjeldab, kuidas tehisintellekti agentid saavad kasutada konkreetseid tööriistu oma eesmärkide saavutamiseks.

## Sissejuhatus

Selles tunnis püüame vastata järgmistele küsimustele:

- Mis on tööriistade kasutamise disainimuster?
- Millistes kasutusjuhtumites saab seda rakendada?
- Millised on elemendid/komponendid, mida disainimustri rakendamiseks vaja on?
- Millised on eritingimused Tööriistade kasutamise disainimustri kasutamisel usaldusväärsete AI agentide ehitamiseks?

## Õpieesmärgid

Selle tunni lõpetamisel suudate:

- Määratleda Tööriistade kasutamise disainimustri ja selle eesmärgi.
- Tuvastada kasutusjuhtumid, kus Tööriistade kasutamise disainimuster on rakendatav.
- Mõista peamisi elemente, mis on disainimustri rakendamiseks vajalikud.
- Tuvastada kaalutlused usaldusväärsuse tagamiseks AI agentides, kes kasutavad seda disainimustrit.

## Mis on Tööriistade kasutamise disainimuster?

**Tööriistade kasutamise disainimuster** keskendub LLM-idele võime andmisele suhelda väliste tööriistadega, et saavutada konkreetseid eesmärke. Tööriistad on kood, mida agent saab käivitada tegevuste sooritamiseks. Tööriist võib olla lihtne funktsioon nagu kalkulaator või kolmanda osapoole teenuse API-kõne, näiteks aktsiahindade päring või ilmaprognoos. Tehisintellekti agentide kontekstis on tööriistad mõeldud käivitatavaks agentide poolt **mudeli genereeritud funktsiooni kutsete** vastuseks.

## Millistes kasutusjuhtumites seda saab rakendada?

AI agentidel on võimalik tööriistu kasutada keerukate ülesannete täitmiseks, informatsiooni hankimiseks või otsuste tegemiseks. Tööriistade kasutamise disainimustrit kasutatakse sageli olukordades, mis nõuavad dünaamilist suhtlust väliste süsteemidega, nagu andmebaasid, veebiteenused või koodi tõlgendajad. Selle võime on kasulik mitmesugustes kasutusjuhtumites, sh:

- **Dünaamiline info hankimine:** Agendid saavad teha päringuid väliste API-de või andmebaaside poole, et hankida ajakohast andmestikku (nt SQLite andmebaasi päring andmeanalüüsi jaoks, aktsiahindade või ilmainfo hankimine).
- **Koodi täitmine ja tõlgendamine:** Agendid saavad käivitada koodi või skripte matemaatiliste probleemide lahendamiseks, aruannete genereerimiseks või simulatsioonide tegemiseks.
- **Töövoo automatiseerimine:** Korduvate või mitme sammuga töövoogude automatiseerimine, integreerides tööriistu nagu ülesannete planeerijad, e-posti teenused või andmetorud.
- **Klienditugi:** Agendid saavad suhelda kliendisuhete haldussüsteemide, piletisüsteemide või teadmiste baasidega, et lahendada kasutajate päringuid.
- **Sisu genereerimine ja redigeerimine:** Agendid saavad kasutada tööriistu nagu grammatikakontroll, teksti kokkuvõtte tegija või sisuturvalisuse hindaja, et aidata sisuloome ülesannetes.

## Millised on elemendid/komponendid tööriistade kasutamise disainimustri rakendamiseks?

Need komponendid võimaldavad AI agendil täita mitmesuguseid ülesandeid. Vaatleme peamisi elemente, mis on Tööriistade kasutamise disainimustri rakendamiseks vajalikud:

- **Funktsiooni/tööriista skeemid:** Üksikasjalikud määratlemised saadavalolevate tööriistade kohta, kaasa arvatud funktsiooni nimi, eesmärk, vajalikud parameetrid ja oodatavad väljundid. Need skeemid võimaldavad LLM-il mõista, millised tööriistad on olemas ja kuidas ehitada kehtivaid päringuid.

- **Funktsiooni täitmise loogika:** Reguleerib, kuidas ja millal tööriistu kutsutakse kasutaja kavatsuse ja vestluse konteksti alusel. See võib hõlmata planeerijamooduleid, marsruutimise mehhanisme või tingimuslikke vooge, mis määravad tööriistade kasutamise dünaamiliselt.

- **Sõnumi käsitlemise süsteem:** Komponendid, mis haldavad vestlusvoogu kasutaja sisendite, LLM vastuste, tööriistakutsete ja tööriistaväljundite vahel.

- **Tööriistade integreerimise raamistik:** Taristu, mis ühendab agendi erinevate tööriistadega, olgu need lihtsad funktsioonid või keerukad välisteenused.

- **Vigade käsitlemine ja valideerimine:** Mehhanismid tööriistatäitluse tõrgete käsitlemiseks, parameetrite valideerimiseks ja ootamatute vastuste haldamiseks.

- **Oleku haldus:** Jälgib vestluse konteksti, varasemaid tööriistaga suhtlemisi ja püsivat andmestikku, et tagada järjepidevus mitme sammuga vestlustes.

Järgmises osas vaatleme funktsiooni/tööriista kutsumist üksikasjalikumalt.

### Funktsiooni/tööriista kutsumine

Funktsiooni kutsumine on peamine viis, kuidas võimaldame suurte keelemudelite (LLM) tööriistadega suhelda. Sageli kasutatakse termineid 'funktsioon' ja 'tööriist' vaheldumisi, sest 'funktsioonid' (taaskasutatavad koodiplokid) on tööriistad, mida agendid kasutavad ülesannete täitmiseks. Selleks, et funktsiooni kood käivitada, peab LLM võrdlema kasutaja päringut funktsiooni kirjeldusega. Selleks saadetakse LLM-ile skeem, mis sisaldab kõigi saadavalolevate funktsioonide kirjeldusi. LLM valib seejärel ülesande jaoks kõige sobivama funktsiooni ja tagastab selle nime ja argumendid. Valitud funktsioon käivitatakse, selle vastus saadetakse tagasi LLM-ile, kes kasutab seda infot kasutaja päringule vastamiseks.

Arendajatel, kes soovivad funktsiooni kutsumist agentidele rakendada, on vaja:

1. LLM mudelit, mis toetab funktsiooni kutsumist
2. Skeemi, mis sisaldab funktsioonide kirjeldusi
3. Koodi iga kirjeldatud funktsiooni jaoks

Näiteks kujutame ette, et soovime saada linna praegust aega:

1. **Initsialiseerige LLM, mis toetab funktsiooni kutsumist:**

   Mitte kõik mudelid ei toeta funktsiooni kutsumist, seega on oluline kontrollida, kas kasutatav LLM seda teeb. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> toetab funktsiooni kutsumist. Saame alustada Azure OpenAI kliendi käivitamisest.

    ```python
    # Algatage Azure OpenAI klient
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Looge funktsiooni skeem:**

   Seejärel määratleme JSON skeemi, mis sisaldab funktsiooni nime, funktsiooni tegevuse kirjelduse ning funktsiooni parameetrite nimesid ja kirjeldusi.
   See skeem antakse eelnevalt loodud kliendile koos kasutaja päringuga, et leida aeg San Franciscos. Oluline on märkida, et tagastatav on **tööriista kutse**, **mitte** lõplik vastus küsimusele. Nagu varem mainitud, tagastab LLM ülesande jaoks valitud funktsiooni nime ja argumendid, mis talle edastatakse.

    ```python
    # Funktsiooni kirjeldus mudeli lugemiseks
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
  
    # Algne kasutaja sõnum
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Esimene API kõne: Palu mudelil funktsiooni kasutada
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Töötle mudeli vastust
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Funktsiooni kood, mis sooritab ülesande:**

   Kui LLM on valinud funktsiooni, tuleb ülesande täitmiseks kirjutada ja käivitada vastav kood.
   Näiteks saame praeguse aja saamiseks kirjutada Pythonis koodi. Me peame ka väljavõtma funktsiooni nime ja argumendid response_message’st, et saada lõplik tulemus.

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
     # Töötle funktsiooni kõnesid
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
  
      # Teine API kõne: Hangi mudeli lõplik vastus
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

Funktsiooni kutsumine on enamikus, kui mitte kõigis agentide tööriistade kasutamise disainides keskne, kuid selle nullist rakendamine võib mõnikord olla keeruline.
Nagu õppisime [Õppetunnis 2](../../../02-explore-agentic-frameworks) pakuvad agentiraamistikud meile eelvalmis komponente tööriistade kasutuse rakendamiseks.
 
## Tööriistade kasutamise näited agentiraamistikega

Siin on mõned näited, kuidas saab Tööriistade kasutamise disainimustrit rakendada erinevate agentiraamistike abil:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> on avatud lähtekoodiga AI raamistik .NET, Python ja Java arendajatele, kes töötavad suurte keelemudelitega (LLM). See lihtsustab funktsiooni kutsumise protsessi, kirjeldades automaatselt mudelile teie funktsioonid ja nende parameetrid, kasutades protsessi nimega <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialiseerimine</a>. See haldab ka suhtlust mudeli ja teie koodi vahel. Teine eelis agentiraamistiku Semantic Kernel kasutamisel on see, et see võimaldab kasutada eelnevalt loodud tööriistu nagu <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Failiotsing</a> ja <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Koodi tõlgendaja</a>.

Järgnev diagramm illustreerib funktsiooni kutsumise protsessi Semantic Kerneliga:

![function calling](../../../translated_images/et/functioncalling-diagram.a84006fc287f6014.webp)

Semantic Kernelis kutsutakse funktsioone/tööriistu <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">pluginateks</a>. Saame funktsiooni `get_current_time`, mida eelnevalt nägime, muuta pluginaks, muutes selle klassiks koos funktsiooniga. Saame importida ka `kernel_function` dekoratiivse meetodi, mis võtab vastu funktsiooni kirjelduse. Kui siis loote kernel’i koos GetCurrentTimePlugin’iga, serialiseerib kernel automaatselt funktsiooni ja selle parameetrid, luues skeemi, mis saadetakse LLM-ile.

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

# Loo tuum
kernel = Kernel()

# Loo plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Lisa plugin tuuma juurde
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> on uuem agentiraamistik, mis on loodud arendajate võimestamiseks turvaliselt ehitada, juurutada ja suurendada kvaliteetseid ning laiendatavaid AI agente ilma aluseks olevate arvutus- ja salvestusressursside haldamiseta. See on eriti kasulik ettevõtete rakenduste jaoks, kuna tegemist on täielikult hallatava teenusega, millel on ettevõtte taseme turvalisus.

Võrreldes arendamisega otse LLM API-ga, pakub Azure AI Agent Service mõningaid eeliseid, sealhulgas:

- Automaatne tööriistakutsumine – ei pea tööriistakutset parsimagi, tööriista kutsuma ega vastust käsitlema; kõik see toimub nüüd serveripoolselt
- Turvaliselt hallatav andmestik – asemel, et ise vestluse olekut hallata, saab kasutada lõimeid kogu vajaliku info talletamiseks
- Valmis tööriistad – tööriistad, millega saab suhelda oma andmeallikatega, näiteks Bing, Azure AI Search ja Azure Functions.

Azure AI Agent Service'is olevad tööriistad jagunevad kaheks kategooriaks:

1. Teadmiste tööriistad:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search’iga sidumine</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Failiotsing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Tegevustööriistad:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktsiooni kutsumine</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Koodi tõlgendaja</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI määratletud tööriistad</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agentiteenus võimaldab meil kasutada neid tööriistu koos kui `tööriistakomplekti`. Samuti kasutab see `lõime` (threads), mis hoiavad kindlalt meeles konkreetse vestluse sõnumite ajalugu.

Kujutame ette, et olete müügiesindaja ettevõttes Contoso. Soovite arendada vestlusagenti, kes suudab vastata küsimustele teie müügiandmete kohta.

Järgmine pilt illustreerib, kuidas võiksite Azure AI Agent Service abil oma müügiandmeid analüüsida:

![Agentic Service In Action](../../../translated_images/et/agent-service-in-action.34fb465c9a84659e.webp)

Neid tööriistu teenusega kasutamiseks saab luua kliendi ja määratleda tööriista või töövahendite komplekti. Praktikas saame kasutada järgmist Python koodi. LLM saab tööriistakomplekti põhjal otsustada, kas kasutada kasutaja loodud funktsiooni `fetch_sales_data_using_sqlite_query` või eelnevalt loodud Koodi tõlgendajat, sõltuvalt kasutaja päringust.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funktsioon fetch_sales_data_using_sqlite_query, mis asub failis fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Algatage tööriistakomplekt
toolset = ToolSet()

# Algatage funktsiooni kutseagent koos fetch_sales_data_using_sqlite_query funktsiooniga ja lisage see tööriistakomplekti
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Algatage koodi interpretori tööriist ja lisage see tööriistakomplekti.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Millised on eritingimused Tööriistade kasutamise disainimustri kasutamisel usaldusväärsete AI agentide ehitamiseks?

SQL-i, mida LLM-id dünaamiliselt genereerivad, puhul on tavaline mure turvalisus, eriti SQL-süsti või pahatahtlike toimingute risk, nagu andmebaasi kustutamine või kahjustamine. Kuigi need mured on põhjendatud, saab neid tõhusalt leevendada, konfigureerides andmebaasi ligipääsuõigused korrektselt. Enamiku andmebaaside puhul tähendab see andmebaasi konfigureerimist ainult lugemisõigusega. Andmebaasiteenuste nagu PostgreSQL või Azure SQL puhul tuleks rakendusele määrata ainult lugemisõigusega (SELECT) roll.
Rakenduse käitamine turvalises keskkonnas suurendab kaitset veelgi. Ettevõtte stsenaariumites ekstraheeritakse ja muudetakse andmeid tavaliselt operatsioonisüsteemidest ainult lugemiseks mõeldud andmebaasi või andmelao jaoks kasutajasõbraliku skeemiga. See lähenemine tagab andmete turvalisuse, optimeerib jõudlust ja ligipääsetavust ning piirab rakenduse juurdepääsu ainult lugemisõigustega.

## Näidiskoodid

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Kas sul on tööriista kasutamise disainimustrite kohta rohkem küsimusi?

Liitu [Azure AI Foundry Discordi](https://aka.ms/ai-agents/discord) kanaliga, et kohtuda teiste õppuritega, osaleda konsultatsioonitundides ja saada vastused oma AI Agentide küsimustele.

## Lisamaterjalid

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer mitmeagendi töötuba</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel funktsioonikõnede juhend</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel koodi tõlgendaja</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen tööriistad</a>

## Eelmine õppetükk

[Agentse disainimustrite mõistmine](../03-agentic-design-patterns/README.md)

## Järgmine õppetükk

[Agentse RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud AI-tõlke teenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi me püüame täpsust, palun arvestage, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Algkeeles dokumenti tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tekkivate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->