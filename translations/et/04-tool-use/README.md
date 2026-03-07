[![Kuidas kujundada häid tehisintellekti agente](../../../translated_images/et/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klõpsake ülaloleval pildil, et vaadata selle õppetunni videot)_

# Tööriistade kasutamise disainimuster

Tööriistad on huvitavad, sest need võimaldavad AI-agentidel omada laiemat võimekust. Selle asemel, et agentil oleks piiratud hulk toiminguid, mida ta saab teha, võimaldab tööriista lisamine agendil nüüd sooritada palju erinevaid toiminguid. Selles peatükis vaatleme Tool Use Design Patterni ehk tööriistade kasutamise disainimustrit, mis kirjeldab, kuidas AI-agentid saavad kasutada konkreetseid tööriistu oma eesmärkide saavutamiseks.

## Sissejuhatus

Selles õppetunnis püüame vastata järgmistele küsimustele:

- Mis on tööriistade kasutamise disainimuster?
- Millistel kasutusjuhtudel seda saab rakendada?
- Millised on elemendid/ehitusplokid, mis on vajalikud disainimustri rakendamiseks?
- Millised on erikohad, mida arvestada tööriistade kasutamise disainimustri abil usaldusväärsete AI-agentide ehitamisel?

## Õpieesmärgid

Pärast selle õppetunni läbimist suudate:

- Määratleda tööriistade kasutamise disainimustri ja selle eesmärgi.
- Tuvastada kasutusjuhtumeid, kus tööriistade kasutamise disainimuster on asjakohane.
- Mõista peamisi elemente, mis on vajalikud disainimustri rakendamiseks.
- Teadvustada kaalutlusi usaldusväärsuse tagamiseks AI-agentide puhul, kes kasutavad seda disainimustrit.

## Mis on tööriistade kasutamise disainimuster?

The **Tool Use Design Pattern** keskendub LLM-idele võime andmisele suhelda väliste tööriistadega konkreetsete eesmärkide saavutamiseks. Tööriistad on kood, mida agent saab täitmiseks kasutada toimingute sooritamiseks. Tööriist võib olla lihtne funktsioon nagu kalkulaator või kolmanda osapoole teenuse API-kõne, näiteks aktsiahindade päring või ilmaprognoos. AI-agentite kontekstis on tööriistad loodud olema täidetavad agentide poolt vastuseks **model-generated function calls**.

## Millistel kasutusjuhtudel seda saab rakendada?

AI-agentid saavad tööriistu kasutada keerukate ülesannete täitmiseks, teabe hankimiseks või otsuste tegemiseks. Tööriistade kasutamise disainimustrit kasutatakse sageli olukordades, kus on vaja dünaamilist suhtlust väliste süsteemidega, nagu andmebaasid, veebiteenused või kooditõlgid. See võime on kasulik mitmesuguste kasutusjuhtude jaoks, sealhulgas:

- **Dünaamiline teabe pärimine:** Agendid saavad pärida väliseid API-sid või andmebaase, et hankida ajakohastatud andmeid (nt SQLite andmebaasi pärimine andmeanalüüsiks, aktsiahindade või ilmainformatsiooni hankimine).
- **Koodi täitmine ja tõlgendamine:** Agendid saavad täita koodi või skripte matemaatiliste ülesannete lahendamiseks, raportite genereerimiseks või simulatsioonide läbiviimiseks.
- **Töövoo automatiseerimine:** Korduvate või mitmeastmeliste töövoogude automatiseerimine, integreerides tööriistu nagu ülesannete ajastajad, e-posti teenused või andmetorud.
- **Klienditugi:** Agendid saavad suhelda CRM-süsteemide, piletisüsteemide või teadmistebaasidega kasutajapäringute lahendamiseks.
- **Sisu genereerimine ja redigeerimine:** Agendid saavad kasutada tööriistu nagu grammatika kontrollijad, teksti kokkuvõttejad või sisu ohutuse hindajad sisu loomise toetamiseks.

## Millised on elemendid/ehitusplokid, mis on vajalikud tööriistade kasutamise disainimustri rakendamiseks?

Need ehitusplokid võimaldavad AI-agendil sooritada laia valikut ülesandeid. Vaatame peamisi elemente, mis on vajalikud Tool Use Design Patterni rakendamiseks:

- **Funktsioonide/tööriistade skeemid:** Üksikasjalikud definitsioonid saadaolevatest tööriistadest, sealhulgas funktsiooni nimi, eesmärk, vajalikud parameetrid ja eeldatavad väljundid. Need skeemid võimaldavad LLM-il mõista, millised tööriistad on saadaval ja kuidas koostada kehtivaid päringuid.

- **Funktsiooni täitmise loogika:** Reguleerib, kuidas ja millal tööriistu kutsutakse vastavalt kasutaja kavatsusele ja vestluse kontekstile. See võib hõlmata planeerija mooduleid, marsruutimismehhanisme või tingimuslikke vooge, mis määravad tööriistade kasutuse dünaamiliselt.

- **Sõnumite käsitlemise süsteem:** Komponendid, mis haldavad konversatsiooni voogu kasutaja sisendite, LLM-vastuste, tööriistakõnede ja tööriistade väljundite vahel.

- **Tööriistade integreerimise raamistik:** Taristu, mis ühendab agendi erinevate tööriistadega, olgu need siis lihtsad funktsioonid või keerukad välisteenused.

- **Veahaldus ja valideerimine:** Mehhanismid tööriista täitmise ebaõnnestumiste käsitlemiseks, parameetrite valideerimiseks ja ootamatute vastuste haldamiseks.

- **Oleku haldus:** Jälgib vestluse konteksti, varasemaid tööriistainteresse ja püsivaid andmeid, et tagada järjepidevus mitmevoorulistes interaktsioonides.

Järgmisena vaatame funktsiooni/tööriista kutsumist üksikasjalikumalt.
 
### Funktsiooni/tööriista kutsumine

Funktsioonide kutsumine on peamine viis, kuidas võimaldame Large Language Modelitel (LLM-idel) suhelda tööriistadega. Tihti kasutatakse sõnu 'Function' ja 'Tool' vaheldumisi, sest 'funktsioonid' (taaskasutatava koodi plokid) on 'tööriistad', mida agendid kasutavad ülesannete täitmiseks. Selleks, et funktsiooni kood saaks kutsutud, peab LLM võrdlema kasutaja päringut funktsioonide kirjeldusega. Selleks saadetakse LLM-ile skeem, mis sisaldab kõigi saadaolevate funktsioonide kirjeldusi. LLM valib seejärel ülesande jaoks kõige sobivama funktsiooni ja tagastab selle nime ning argumendid. Valitud funktsioon kutsutakse ära, selle vastus saadetakse tagasi LLM-ile, kes kasutab seda teavet kasutaja päringule vastamiseks.

Arendajatel, kes soovivad agentidele funktsioonikõnede rakendamist, on vaja:

1. LLM mudelit, mis toetab funktsioonikõnesid
2. Skeemi, mis sisaldab funktsioonikirjeldusi
3. Koodi iga kirjeldatud funktsiooni jaoks

Vaatame näidet, kuidas saada praegust aega linnas, et illustreerida:

1. **Algata LLM, mis toetab funktsioonikõnesid:**

    Mitte kõik mudelid ei toeta funktsioonikõnesid, seega on oluline kontrollida, kas kasutatav LLM seda teeb.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> toetab funktsioonikõnesid. Saame alustada, initsieerides Azure OpenAI kliendi. 

    ```python
    # Initsialiseeri Azure OpenAI klient
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Loo funktsiooni skeem**:

    Järgmisena määratleme JSON-skeemi, mis sisaldab funktsiooni nime, kirjeldust, mida funktsioon teeb, ning funktsiooni parameetrite nimesid ja kirjeldusi.
    Seejärel edastame selle skeemi varem loodud kliendile koos kasutaja päringuga, kus ta tahab teada kellaaja San Franciscos. Oluline on märkida, et tagastatakse **tööriistakutse**, **mitte** lõplik vastus küsimusele. Nagu eelpool mainitud, tagastab LLM valitud funktsiooni nime ja argumendid, mis talle edastatakse.

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
  
    # Esimene API-kõne: Palu mudelil kasutada funktsiooni
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
  
1. **Funktsiooni kood, mis on vajalik ülesande täitmiseks:**

    Nüüd, kui LLM on valinud, millist funktsiooni on vaja käivitada, tuleb realiseerida ja käivitada kood, mis ülesande täidab.
    Saame Pythonis rakendada koodi, mis hangib praeguse kellaaja. Samuti peame kirjutama koodi, mis ekstraheerib response_message'st nime ja argumendid, et saada lõplik tulemus.

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
     # Käsitle funktsioonikõnesid
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
  
      # Teine API-kõne: Hangi mudelilt lõplik vastus
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

Funktsioonikõne on enamikus, kui mitte kõikides agentide tööriistakasutuse disainides keskmes, kuid selle nullist rakendamine võib mõnikord olla keeruline.
Nagu õppisime [Lesson 2](../../../02-explore-agentic-frameworks) osas, pakuvad agentse raamistikud meile eelnevalt ehitatud ehitusplokke tööriistakasutuse rakendamiseks.
 
## Tööriistade kasutamise näited agentse raamistikuga

Siin on mõned näited sellest, kuidas saate tööriistade kasutamise disainimustrit rakendada erinevate agentsete raamistikuga:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> on avatud lähtekoodiga AI-raamistik AI-agentide ehitamiseks. See lihtsustab funktsioonikõnede kasutamist, võimaldades teil määratleda tööriistad Python-funktsioonidena, kasutades dekoratsiooni `@tool`. Raamistik haldab mudeli ja teie koodi vahelist kahepoolset suhtlust. Samuti annab see juurdepääsu eelnevalt ehitatud tööriistadele nagu File Search ja Code Interpreter kaudu `AzureAIProjectAgentProvider`.

Järgmine diagramm illustreerib funktsioonikõnede protsessi Microsoft Agent Frameworkiga:

![function calling](../../../translated_images/et/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Frameworkis määratletakse tööriistad dekoreeritud funktsioonidena. Saame teisendada varem näidatud `get_current_time` funktsiooni tööriistaks, kasutades dekoratsiooni `@tool`. Raamistik serialiseerib automaatselt funktsiooni ja selle parameetrid, luues skeemi, mida saata LLM-ile.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Loo klient
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Loo agent ja käivita see tööriistaga
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> on uuem agentse raamistik, mis on loodud arendajate võimestamiseks turvaliselt ehitada, juurutada ja skaleerida kvaliteetseid ning laiendatavaid AI-agente, ilma et peaks hallama aluseks olevaid arvutus- ja salvestusressursse. See on eriti kasulik ettevõtete rakendustes, kuna tegemist on täielikult hallatud teenusega ettevõttekvaliteediga turvalisusega.

Võrreldes arendamisega otse LLM API-ga annab Azure AI Agent Service mõningaid eeliseid, sealhulgas:

- Automaatne tööriistakutsumine – pole vaja tööriistakutset ise parsida, tööriista kutsuda ja vastust töödelda; kõik see tehakse nüüd serveripoolselt
- Andmete turvaline haldus – selle asemel, et hallata oma vestluse olekut, võite tugineda „threads“-ile, mis salvestavad kogu vajaliku teabe
- Valmis tööriistad – tööriistad, mida saate kasutada oma andmeallikatega suhtlemiseks, näiteks Bing, Azure AI Search ja Azure Functions.

Azure AI Agent Service'is saadaval olevad tööriistad jagunevad kaheks kategooriaks:

1. Teadmiste tööriistad:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Tegevustööriistad:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service võimaldab meil kasutada neid tööriistu koos kui `toolset`i. Lisaks kasutab see `threads`i, mis jälgivad konkreetse vestluse sõnumite ajalugu.

Kujutage ette, et olete müügiesindaja ettevõttes nimega Contoso. Soovite arendada vestlusagenti, mis suudab vastata teie müügiandmete kohta esitatud küsimustele.

Järgmine pilt illustreerib, kuidas võiksite kasutada Azure AI Agent Service'i oma müügiandmete analüüsimiseks:

![Agentic Service In Action](../../../translated_images/et/agent-service-in-action.34fb465c9a84659e.webp)

Nende tööriistade kasutamiseks teenusega saame luua kliendi ja määratleda tööriista või toolseti. Praktiliseks rakendamiseks võime kasutada järgmist Python-koodi. LLM suudab vaadata toolset'i ja otsustada, kas kasutada kasutaja loodud funktsiooni `fetch_sales_data_using_sqlite_query` või eelnevalt ehitatud Code Interpreterit, sõltuvalt kasutaja päringust.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query funktsioon, mida leidub failis fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initsialiseeri tööriistakomplekt
toolset = ToolSet()

# Initsialiseeri funktsiooni kutsuv agent fetch_sales_data_using_sqlite_query funktsiooniga ja lisa see tööriistakomplekti
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initsialiseeri Code Interpreter tööriist ja lisa see tööriistakomplekti
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Millised on erikohad, mida arvestada tööriistade kasutamise disainimustri abil usaldusväärsete AI-agentide ehitamisel?

Üks levinud mure dünaamiliselt LLM-ide genereeritud SQL-i puhul on turvalisus, eriti SQL-süstimise või pahatahtlike tegevuste risk, nagu andmebaasi kustutamine või manipuleerimine. Kuigi need mured on õigustatud, saab neid tõhusalt leevendada andmebaasi juurdepääsulubade nõuetekohase seadistamisega. Enamikus andmebaasides tähendab see andmebaasi seadistamist ainult lugemisõigusega. Selliste andmebaasiteenuste nagu PostgreSQL või Azure SQL puhul tuleks rakendusele määrata ainult lugemisõigus (SELECT).

Rakenduse käitamine turvalises keskkonnas suurendab kaitset veelgi. Ettevõtte stsenaariumites ekstraheeritakse ja muudetakse andmed tavaliselt operatsioonisüsteemidest eraldatud ainult-lugemis andmebaasi või andmehoidlasse kasutajasõbraliku skeemiga. See lähenemine tagab, et andmed on turvalised, optimeeritud jõudluse ja ligipääsetavuse jaoks ning et rakendusel on piiratud, ainult-lugemise juurdepääs.

## Näidiskoodid

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Kas teil on veel küsimusi tööriistade kasutamise disainimustrite kohta?

Liituge [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) kanaliga, et kohtuda teiste õppuritega, osaleda tundi aegadel (office hours) ja saada vastuseid oma AI Agents küsimustele.

## Lisamaterjalid

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## Eelmine õppetund

[Agentse disaini mustrite mõistmine](../03-agentic-design-patterns/README.md)

## Järgmine õppetund
[Agentne RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastutusest loobumine:
See dokument on tõlgitud tehisintellekti tõlketeenuse Co-op Translator (https://github.com/Azure/co-op-translator) abil. Kuigi me püüame olla täpsed, pidage meeles, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokumenti selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste ega valesti tõlgendamise eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->