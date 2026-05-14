[![Kuidas disainida head AI agente](../../../translated_images/et/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klõpsa ülaloleval pildil, et vaadata selle tunni videot)_

# Tööriistade kasutamise disainimuster

Tööriistad on huvitavad, sest need võimaldavad AI agentidel omada laiemat võimekust. Selle asemel, et agendil oleks piiratud hulk teostatavaid tegevusi, saab tööriista lisamisega agent nüüd teha paljusid erinevaid toiminguid. Selles peatükis vaatleme tööriistade kasutamise disainimustrit, mis kirjeldab, kuidas AI agendid saavad kasutada konkreetseid tööriistu oma eesmärkide saavutamiseks.

## Sissejuhatus

Selles õppetükis püüame vastata järgmistele küsimustele:

- Mis on tööriistade kasutamise disainimuster?
- Millistes kasutusjuhtumites seda saab rakendada?
- Millised elemendid/ehitusplokid on vajalikud disainimustri rakendamiseks?
- Millised on tööriistade kasutamise disainimustri kasutamise erikohad usaldusväärsete AI agentide loomiseks?

## Õpieesmärgid

Pärast selle õppetüki läbimist suudad:

- Määratleda tööriistade kasutamise disainimustri ja selle eesmärgi.
- Tuvastada kasutusjuhud, kus tööriistade kasutamise disainimuster on rakendatav.
- Mõista disainimustri rakendamiseks vajalikke põhireaktsioone.
- Tunnustada kaalutlusi usaldusväärsuse tagamiseks AI agentidel, kes kasutavad seda disainimustrit.

## Mis on tööriistade kasutamise disainimuster?

**Tööriistade kasutamise disainimuster** keskendub LLM-ide võimele suhelda väliste tööriistadega spetsiifiliste eesmärkide saavutamiseks. Tööriistad on kood, mida agent saab käivitada tegevuste sooritamiseks. Tööriist võib olla lihtne funktsioon, näiteks kalkulaator, või API-kõne kolmanda osapoole teenusele, nagu aktsiahindade otsing või ilmateade. AI agentide kontekstis on tööriistad loodud täitmiseks agentide poolt vastuseks **mudelipõhistele funktsioonikõnedele**.

## Millistes kasutusjuhtumites seda saab rakendada?

AI agendid saavad tööriistu kasutada keerukate ülesannete täitmiseks, info otsimiseks või otsuste tegemiseks. Tööriistade kasutamise disainimustrit kasutatakse sageli olukordades, kus on vaja dünaamiliselt suhelda väliste süsteemidega, näiteks andmebaaside, veebiteenuste või kooditõlgendajatega. See võime on kasulik mitmetes kasutusjuhtumites, sealhulgas:

- **Dünaamiline info päring:** Agendid saavad väliseid API-sid või andmebaase pärida, et saada ajakohast teavet (nt SQLite andmebaasist andmeanalüüsiks andmete päring, aktsiahindade või ilmaandmete toomine).
- **Koodi täitmine ja tõlgendamine:** Agendid saavad käivitada koodi või skripte matemaatiliste probleemide lahendamiseks, aruannete koostamiseks või simulatsioonide tegemiseks.
- **Töövoo automatiseerimine:** Korduvate või mitmeastmeliste töövoogude automatiseerimine, ühendades tööriistu nagu ülesannete ajastajad, meiliteenused või andmepipelines.
- **Klienditugi:** Agendid saavad suhelda kliendihaldussüsteemide, piletisüsteemide või teadmistebaasidega kasutajaküsimuste lahendamiseks.
- **Sisu loomine ja redigeerimine:** Agendid saavad kasutada tööriistu nagu grammatikakontrollijad, tekstisummariseerijad või sisuturvalisuse hindajad, et abistada sisuloome ülesannetes.

## Millised elemendid/ehitusplokid on vajalikud tööriistade kasutamise disainimustri rakendamiseks?

Need ehitusplokid võimaldavad AI agendil täita palju erinevaid ülesandeid. Vaatame põhilisi elemente, mis on vajalikud tööriistade kasutamise disainimustri rakendamiseks:

- **Funktsiooni/tööriista skeemid**: Detailne definitsioonid saadaval olevatest tööriistadest, sisaldades funktsioonide nimesid, eesmärke, vajalikke parameetreid ja oodatavaid tulemusi. Need skeemid võimaldavad LLM-il mõista, millised tööriistad on saadaval ja kuidas koostada korrektseid päringuid.

- **Funktsiooni täitmise loogika**: Käsitleb, kuidas ja millal tööriistu kutsutakse vastavalt kasutaja kavatsusele ja vestluse kontekstile. See võib hõlmata planeerijaid, marsruutimismehhanisme või tingimusvooge, mis dünaamiliselt määravad tööriistade kasutuse.

- **Sõnumikäitluse süsteem**: Komponendid, mis haldavad vestlusevoogu kasutajasisendite, LLM vastuste, tööriistakutsete ja tööriistade väljundite vahel.

- **Tööriistade integratsiooniraamistik**: Infrastruktuur, mis ühendab agendi erinevate tööriistadega, olgu need lihtsad funktsioonid või keerukad välised teenused.

- **Veakäsitlus ja valideerimine**: Mehhanismid tööriistatäitmise vigade käsitlemiseks, parameetrite valideerimiseks ja ootamatute vastuste haldamiseks.

- **Seisundihaldus**: Jälgib vestluse konteksti, eelnevaid tööriistakõnesid ja püsivaid andmeid, tagamaks järjepidevuse mitme sammu pikkustes interaktsioonides.

Järgmisena vaatleme funktsioonide/tööriistade kutsumist üksikasjalikumalt.

### Funktsioonide/tööriistade kutsumine

Funktsioonikutsumine on peamine viis, kuidas võimaldame suurte keelemudelite (LLM) suhelda tööriistadega. Sageli kasutatakse sõnu "funktsioon" ja "tööriist" vaheldumisi, sest "funktsioonid" (taaskasutatava koodilõigud) on just agentide kasutatavad tööriistad ülesannete täitmiseks. Selleks, et funktsiooni koodi kutsuda, peab LLM võrdlema kasutaja päringut funktsiooni kirjeldusega. Selleks saadetakse LLM-ile skeem, mis sisaldab kõigi saadaolevate funktsioonide kirjelduseid. LLM valib kõige sobivama funktsiooni ülesande jaoks ning tagastab selle nime ja argumendid. Valitud funktsioon käivitatakse, selle vastus saadetakse LLM-ile, mis kasutab seda teavet, et vastata kasutaja päringule.

Arendajatel, kes soovivad agentide funktsioonikutsumist rakendada, on vaja:

1. LLM-i mudelit, mis toetab funktsioonikutsumist
2. Skeemi, mis sisaldab funktsioonide kirjeldusi
3. Koodi iga funktsiooni kohta

Vaatame näidet, kus saame praeguse aja linnas välja küsida:

1. **Alusta LLM-iga, mis toetab funktsioonikutsumist:**

    Mitte kõik mudelid ei toeta funktsioonikutsumist, seega on oluline kontrollida, kas sinu kasutatav LLM seda teeb. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> toetab funktsioonikutsumist. Saame alustada Azure OpenAI kliendi initsialiseerimisega.

    ```python
    # Initsialiseeri Azure OpenAI klient
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```


1. **Loo funktsiooni skeem**:

    Seejärel defineerime JSON skeemi, mis sisaldab funktsiooni nime, kirjelduse, mida funktsioon teeb, ja funktsiooni parameetrite nimesid ning kirjeldusi.
    Seda skeemi edastame eelnevalt loodud kliendile koos kasutaja päringuga, mis küsib aega San Franciscos. Oluline on märkida, et tagastatakse **tööriistakutse**, **mitte** lõplik vastus küsimusele. Nagu juba mainitud, tagastab LLM selle funktsiooni nime, mille ta ülesande jaoks valis, ja argumendid, mida talle antakse.

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
  
    # Esialgne kasutajateade
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Esimene API kõne: Palu mudelil kasutada funktsiooni
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
  

1. **Funktsiooni kood ülesande täitmiseks:**

    Nüüd, kui LLM on valinud, millist funktsiooni käivitada, on vaja see kood realiseerida ja täita.
    Saame implementerida koodi praeguse aja saamiseks Pythonis. Samuti tuleb kirjutada kood, mis võtab response_message-st välja nime ja argumendid, et saada lõplik tulemus.

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
  
      # Teine API kõne: Hangi mudelist lõplik vastus
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


Funktsioonide kutsumine on enamiku, kui mitte kõigi, agente tööriistade kasutamise disainikujunduste keskmes, kuid selle nullist rakendamine võib olla keeruline.
Nagu õpitud [tunnis 2](../../../02-explore-agentic-frameworks), pakuvad agentpõhised raamistikud ette ehitatud plokke tööriistade kasutamiseks.

## Tööriistade kasutamise näited agentpõhiste raamistikudega

Siin on mõned näited, kuidas kasutada tööriistade kasutamise disainimustrit erinevate agentpõhiste raamistikudega:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> on avatud lähtekoodiga AI raamistik AI agentide loomiseks. See lihtsustab funktsioonikutsumise kasutamist, võimaldades määratleda tööriistad Python funktsioonidena, kasutades `@tool` dekoratsiooni. Raamistik haldab mudeli ja koodi vahelist suhtlust. Lisaks on saadaval valmis tööriistad nagu Failide otsing ja Koodi tõlgendaja, mida saab kasutada `AzureAIProjectAgentProvider` kaudu.

Järgmine diagramm illustreerib funktsioonide kutsumise protsessi Microsoft Agent Framework abil:

![function calling](../../../translated_images/et/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Frameworkis on tööriistad määratletud dekoratsiooniga funktsioonidena. Saame senise `get_current_time` funktsiooni muuta tööriistaks, kasutades `@tool` dekoratsiooni. Raamistik serialiseerib funktsiooni ja selle parameetrid automaatselt ning loob skeemi, mida edastada LLM-ile.

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

# Loo agent ja käivita tööriistaga
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  

### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> on uuem agentpõhine raamistik, mis võimaldab arendajatel turvaliselt luua, juurutada ja skaleerida kvaliteetseid ning laiendatavaid AI agente ilma alusressursside haldamiseta. See sobib eriti hästi ettevõtete rakendusteks, kuna on täisautomaatne teenus ettevõttele vajaliku turvalisusega.

Võrreldes LLM API-ga otse arendamisega pakub Azure AI Agent Service mõningaid eeliseid:

- Automaatne tööriistakutsumine – ei pea ise tööriistakutset tõlgendama, tööriista käivitama ega vastuseid haldama; kõik toimub serveripoolselt
- Turvaliselt hallatud andmed – vestluse seisundi hoidmise asemel saab tugineda thread-idele, mis salvestavad kogu vajaliku info
- Valmis tööriistad – tööriistad, mida saab kasutada andmeallikatega suhtlemiseks, nt Bing, Azure AI Search ja Azure Functions.

Azure AI Agent Service-s olevad tööriistad jagunevad kaheks kategooriaks:

1. Teadmiste tööriistad:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Ühendamine Bing Searchiga</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Failide otsing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Tegevuse tööriistad:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktsioonikutsumine</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Koodi tõlgendaja</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI määratletud tööriistad</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service võimaldab neid tööriistu kasutada ühiselt kui `toolset`-i. Samuti kasutatakse `threads`eid, mis hoiavad konkreetse vestluse sõnumite ajalugu.

Kujutagem ette, et oled müügiesindaja ettevõttes Contoso. Soovid arendada vestlusagenti, mis vastab müügiandmete küsimustele.

Järgmine pilt illustreerib, kuidas saaks Azure AI Agent Service abil analüüsida müügiandmeid:

![Agentic Service In Action](../../../translated_images/et/agent-service-in-action.34fb465c9a84659e.webp)

Neid tööriistu teenusega kasutamiseks saame luua kliendi ning määratleda tööriista või tööriistakomplekti. Praktiliseks rakenduseks võime kasutada järgmist Pythoni koodi. LLM saab vaadata toolset-i ning otsustada, kas kasutada kasutaja loodud funktsiooni `fetch_sales_data_using_sqlite_query` või eelnevalt ehitatud Koodi tõlgendajat, olenevalt kasutaja päringust.

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

# Tööriistakomplekti algatamine
toolset = ToolSet()

# Funktsiooni kutsumise agendi algatamine fetch_sales_data_using_sqlite_query funktsiooniga ja selle lisamine tööriistakomplekti
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Koodi interpreteerija tööriista algatamine ja selle lisamine tööriistakomplekti.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```


## Millised on tööriistade kasutamise disainimustri eripärased kaalutlused usaldusväärsete AI agentide loomiseks?

Levinud mure SQL-i dünaamiliselt LLM-ide poolt genereeritud päringute puhul on turvalisus, eelkõige SQL süstimise või pahatahtlike toimingute oht, nagu andmebaasi kustutamine või rikkumine. Kuigi need mured on põhjendatud, saab neid tõhusalt vähendada andmebaasi ligipääsuõiguste nõuetekohase seadistamisega. Enamikes andmebaasides tähendab see andmebaasi seadistamist ainult lugemisõigusega. Andmebaasiteenuste puhul nagu PostgreSQL või Azure SQL tuleks rakendusele määrata ainult lugemisõigused (SELECT roll).

Rakenduse käitamine turvalises keskkonnas tugevdab kaitset veelgi. Ettevõtete kasutusjuhtudel ekstraktitakse ja muundatakse andmed operatiivsetest süsteemidest lugemisõigusega andmebaasi või andmeletti struktureeritud skeemaga. Selline lähenemine tagab andmete turvalisuse, optimeerib jõudlust ja ligipääsetavust ning piirab rakenduse juurdepääsu ainult lugemiseks.

## Näidiskoodid

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Kas Sul on veel küsimusi tööriistade kasutamise disainimustrite kohta?

Liitu [Microsoft Foundry Discordiga](https://aka.ms/ai-agents/discord), et kohtuda teiste õppijatega, osaleda lahtistes tundides ja saada vastuseid AI agentide küsimustele.

## Lisamaterjalid

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agentide teenuse töötuba</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer mitme agendi töötuba</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework ülevaade</a>

## Eelmine tund

[Agentpõhiste disainimustrite mõistmine](../03-agentic-design-patterns/README.md)

## Järgmine tund
[Agentlik RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->