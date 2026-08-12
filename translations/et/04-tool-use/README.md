[![Kuidas kujundada häid AI agente](../../../translated_images/et/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klõpsa ülaloleval pildil, et vaadata selle õppetunni videot)_

# Tööriista kasutamise disainimuster

Tööriistad on huvitavad, sest need võimaldavad AI agentidel omada laiemat võimekust. Selle asemel, et agendil oleks piiratud hulk teostatavaid tegevusi, saab tööriista lisamisega agent nüüd teha palju erinevaid toiminguid. Selles peatükis vaatleme tööriista kasutamise disainimustrit, mis kirjeldab, kuidas AI agendid saavad kasutada konkreetseid tööriistu oma eesmärkide saavutamiseks.

## Sissejuhatus

Selles õppetunnis püüame vastata järgmistele küsimustele:

- Mis on tööriista kasutamise disainimuster?
- Millistel juhtudel seda saab rakendada?
- Millised on elemendid/ehituskivid, mida on vaja disainimustri rakendamiseks?
- Millised on erikohad tööriista kasutamise disainimustri kasutamisel usaldusväärsete AI agentide ehitamiseks?

## Õpieesmärgid

Pärast selle õppetunni läbimist oskad:

- Määratleda tööriista kasutamise disainimuster ja selle eesmärk.
- Tuvastada juhtumid, kus tööriista kasutamise disainimuster on rakendatav.
- Mõista disainimustri rakendamiseks vajalikke põhikomponente.
- Tuvastada kaalutlusi, mis tagavad selle disainimustri kasutamisel AI agentide usaldusväärsuse.

## Mis on tööriista kasutamise disainimuster?

**Tööriista kasutamise disainimuster** keskendub LLM-ide võimelisele väliste tööriistadega suhelda kindlate eesmärkide saavutamiseks. Tööriistad on kood, mida agent saab täita toimingute sooritamiseks. Tööriistaks võib olla lihtne funktsioon nagu kalkulaator või kolmanda osapoole teenuse API-kõne, näiteks aktsiahindade päring või ilmaprognoos. AI agentide kontekstis on tööriistad kavandatud agentide poolt täitmiseks mudelipõhiste funktsioonikõnede vastusena.

## Millistes kasutusjuhtumites seda saab rakendada?

AI agendid saavad tööriistu kasutada keerukate ülesannete täitmiseks, info hankimiseks või otsuste tegemiseks. Tööriista kasutamise disainimustrit kasutatakse sageli olukordades, kus on vaja dünaamilist suhtlust väliste süsteemidega, näiteks andmebaasid, veebiteenused või koodi tõlgendajad. See võimekus on kasulik mitme erineva kasutusjuhtumi puhul, sealhulgas:

- **Dünaamiline info päring:** Agendid saavad väliseid API-sid või andmebaase küsida, et hankida ajakohast infot (nt SQLite andmebaasi küsimine andmeanalüüsiks, aktsiahindade või ilmaandmete päring).
- **Koodi täitmine ja tõlgendamine:** Agendid saavad täita koodi või skripte, et lahendada matemaatilisi probleeme, genereerida aruandeid või teha simulatsioone.
- **Töövoo automatiseerimine:** Korduvate või mitmeastmeliste töövoogude automatiseerimine, integreerides tööriistu nagu ülesannete ajastajad, e-posti teenused või andmepipes.
- **Klienditugi:** Agendid saavad suhelda CRM-süsteemide, piletihaldusplatvormide või teadmistebaasidega, et lahendada kasutajate päringuid.
- **Sisu genereerimine ja redigeerimine:** Agendid saavad kasutada tööriistu nagu grammatikakontroll, tekstikokkuvõttejad või sisuturvalisuse hindajad, et aidata sisuloome ülesannetes.

## Millised on elemendid/ehituskivid, mida tööriista kasutamise disainimustri rakendamiseks on vaja?

Need ehituskivid võimaldavad AI agendil täita laia valikut ülesandeid. Vaatleme tööriista kasutamise disainimustri rakendamiseks vajalikke põhielemente:

- **Funktsiooni/Tööriista skeemid**: Detailne info saadavalolevate tööriistade kohta, sisaldades funktsiooni nime, eesmärki, vajalikke parameetreid ja oodatavat väljundit. Need skeemid võimaldavad LLM-il mõista, millised tööriistad on saadaval ja kuidas päringuid õigesti vormistada.

- **Funktsiooni täitmise loogika**: Käsitleb seda, kuidas ja millal tööriistu kutsutakse kasutaja kavatsuse ja vestluse konteksti põhjal. See võib hõlmata plaanimooduleid, marsruutimismehhanisme või tingimusvooge, mis dünaamiliselt määravad tööriistade kasutamise.

- **Sõnumite haldussüsteem**: Komponendid, mis juhivad vestluse voogu kasutaja sisendite, LLM vastuste, tööriistakõnede ja tööriistaväljundite vahel.

- **Tööriistade integreerimise raamistik**: Infrastruktuur, mis ühendab agendi erinevate tööriistadega, olgu need lihtsad funktsioonid või keerukad välised teenused.

- **Vea käsitlemine ja valideerimine**: Mehhanismid tööriista täitmisvigade käsitlemiseks, parameetrite valideerimiseks ja ootamatute vastuste haldamiseks.

- **Oleku haldamine**: Jälgib vestluse konteksti, varasemaid tööriista kasutusi ja püsivaid andmeid, et tagada järjepidevus mitme sammuga suhtlemisel.

Järgmisena vaatleme funktsiooni tööriistakõnet üksikasjalikumalt.
 
### Funktsiooni/Tööriista kõne

Funktsiooni kõne on peamine viis, kuidas võimaldame Large Language Modelitel (LLM-idel) suhelda tööriistadega. Sageli kasutatakse „funktsiooni“ ja „tööriista“ sünonüümselt, sest „funktsioonid“ (taaskasutatavad koodiplokid) on tööriistad, mida agendid kasutavad ülesannete täitmiseks. Selleks, et funktsiooni koodi käivitada, peab LLM võrdlema kasutaja päringut funktsiooni kirjeldusega. Selleks saadetakse LLM-ile skeem, mis sisaldab kõigi saadaolevate funktsioonide kirjeldusi. Seejärel valib LLM ülesande jaoks sobivaima funktsiooni ning tagastab selle nime ja argumendid. Valitud funktsioon kutsutakse käiku, selle vastus saadetakse LLM-ile, mis kasutab infot, et vastata kasutaja päringule.

Arendajatele funktsiooni kõne kasutuselevõtuks agentide jaoks on vaja:

1. LLM mudel, mis toetab funktsiooni kõnet
2. Skeem, mis sisaldab funktsioonide kirjeldusi
3. Kood iga kirjeldusega funktsiooni jaoks

Vaatame näidet, kus küsitakse praegust aega linnas:

1. **Algatame LLM-i, mis toetab funktsiooni kõnet:**

    Kõik mudelid ei toeta funktsiooni kõnet, seetõttu on oluline kontrollida, kas sinu kasutatav LLM seda teeb. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> toetab funktsiooni kõnet. Võime alustada, luues OpenAI kliendi Azure OpenAI **vastuste API** vastu (stabiilne `/openai/v1/` lõpp-punkt — `api_version` ei ole vajalik).

    ```python
    # Algatage OpenAI klient Azure OpenAI jaoks (Responses API, v1 lõpp-punkt)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Loo funktsiooni skeem:**

    Järgnevalt määratleme JSON skeemi, mis sisaldab funktsiooni nime, kirjeldust, mida funktsioon teeb, ning funktsiooni parameetrite nimesid ja kirjelduseid.
    Seejärel edastame skeemi eelmises sammus loodud kliendile koos kasutaja päringuga, mis otsib San Francisco aega. Oluline on märkida, et tagastatakse **tööriistakõne**, mitte lõplik vastus küsimusele. Nagu eelnevalt mainitud, tagastab LLM funktsiooni nime, mille ta ülesandeks valis, ning sellele antavad argumendid.

    ```python
    # Funktsiooni kirjeldus mudeli lugemiseks (vastuste API lame tööriista formaat)
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
  
    # Algne kasutajateade
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Esimene API kõne: Palu mudelil kasutada funktsiooni
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Vastuste API tagastab tööriista kutsed kui function_call üksused response.output-s.
    # Lisa need vestlusele, et mudelil oleks järgmises voorus täielik kontekst.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Funktsiooni kood ülesande täitmiseks:**

    Kui LLM on valinud funktsiooni, mida käivitada, tuleb realiseerida ja täita ülesande täitmise kood.
    Saame rakendada koodi, mis hangib praeguse aja Pythoniga. Peame ka kirjutama koodi, mis väljavõtab vastus_sõnumist nime ja argumendid lõpliku tulemuse saamiseks.

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

                # Tagasta tööriista tulemus kui function_call_output element
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Teine API kutsumine: saa mudeli lõplik vastus
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

Funktsiooni kõne on enamiku, kui mitte kõikide agentide tööriistakasutuse disaini põhialus, kuid selle nullist rakendamine võib mõnikord olla keeruline.
Nagu õppisime [Õppetunnis 2](../../../02-explore-agentic-frameworks), pakuvad agentka raamistikud eelvalmis ehituskilde tööriista kasutamise elluviimiseks.
 
## Tööriista kasutamise näited agentka raamistikudega

Siin on mõned näited, kuidas saab tööriista kasutamise disainimustrit rakendada erinevate agentka raamistikudega:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> on avatud lähtekoodiga AI raamistik AI agentide ehitamiseks. See lihtsustab funktsioonikõnede kasutamist, võimaldades defineerida tööriistu Python funktsioonidena, kasutades `@tool` dekoratsiooni. Raamistik haldab mudeli ja sinu koodi vahelist suhtlust. Samuti pakub see ligipääsu eelnevalt koostatud tööriistadele, nagu File Search ja Code Interpreter, kasutades `FoundryChatClient`.

Järgmine skeem illustreerib funktsioonikõne protsessi Microsoft Agent Frameworkiga:

![function calling](../../../translated_images/et/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Frameworkis defineeritakse tööriistad kaunistatud funktsioonidena. Saame eelnevalt näidatud `get_current_time` funktsiooni teisendada tööriistaks, kasutades `@tool` dekoratsiooni. Raamistik serialiseerib funktsiooni ja selle parameetrid automaatselt ning loob skeemi, mida LLM-ile edastada.

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

# Loo agent ja käivita tööriistaga
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> on uuem agentka raamistik, mis võimaldab arendajatel turvaliselt ehitada, juurutada ja skaleerida kvaliteetseid ja laiendatavaid AI agente, ilma et peaks haldama aluskõvaketta ja salvestusressursse. See on eriti kasulik ärirakendustes, kuna tegemist on täielikult hallatava teenusega koos ettevõtte tasemel turvalisusega.

Võrreldes LLM API-ga otse arendamisega pakub Microsoft Foundry Agent Service mitmeid eeliseid, sealhulgas:

- Automaatne tööriistade kõne – valida tööriistakõne, kutsuda tööriist esile ja hallata vastust pole enam kasutaja vastutuses; kõik toimub serveri poolel
- Turvaliselt hallatud andmed – oma vestluse oleku haldamise asemel saab toetuda lõimedele kogu vajaliku info talletamiseks
- Tööriistad karbist välja – tööriistad, millega saab suhelda andmeallikatega, nagu Bing, Azure AI Search ja Azure Functions.

Microsoft Foundry Agent Services on tööriistad jagatud kaheks kategooriaks:

1. Teadmiste tööriistad:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Otsingu kasutamine andmete baasina</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Failiotsing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Otsing</a>

2. Tegevustööriistad:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktsiooni kõne</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Koodi tõlgendaja</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI määratletud tööriistad</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agentteenus võimaldab neid tööriistu kasutada koos kui `tööriistakomplekti`. Samuti kasutab see `lõime`, mis jälgivad konkreetse vestluse sõnumite ajalugu.

Kujutleme, et oled ettevõttes Contoso müügiesindaja. Soovid arendada vestlusagentti, mis suudab vastata müügiandmete küsimustele.

Järgmine pilt illustreerib, kuidas saaksid Microsoft Foundry Agent Service'it kasutada müügiandmete analüüsimiseks:

![Agentic Service In Action](../../../translated_images/et/agent-service-in-action.34fb465c9a84659e.webp)

Ühtegi neist tööriistadest teenusega kasutamiseks saame luua kliendi ja määratleda tööriista või tööriistakomplekti. Põhiseks rakenduseks saame kasutada järgmist Python koodi. LLM saab tööriistakomplekti vaadata ja otsustada, kas kasutada kasutaja loodud funktsiooni `fetch_sales_data_using_sqlite_query` või eelnevalt koostatud Code Interpreterit, sõltuvalt kasutaja päringust.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funktsioon fetch_sales_data_using_sqlite_query, mida võib leida failist fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Tööriistakomplekti initsialiseerimine
toolset = ToolSet()

# Funktsiooni kutsumise agendi initsialiseerimine koos fetch_sales_data_using_sqlite_query funktsiooniga ja selle lisamine tööriistakomplekti
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Koodi interpreteerija tööriista initsialiseerimine ja selle lisamine tööriistakomplekti.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Millised on erilised kaalutlused tööriista kasutamise disainimustrit usaldusväärsete AI agentide ehitamiseks kasutades?

Üks levinud mure LLM-ide dünaamiliselt genereeritud SQL-i puhul on turvalisus, eriti SQL süstimise või pahatahtlike toimingute risk, nagu andmebaasi kustutamine või rikkumine. Kuigi need ohud on õigustatud, saab neid efektiivselt leevendada andmebaasi ligipääsuõiguste korrapärase seadistamisega. Enamiku andmebaaside puhul tähendab see andmebaasi seadistamist ainult lugemisõigustega. PostgreSQL või Azure SQL puhul tuleks rakendusele määrata ainult lugemisõigus (SELECT roll).

Rakenduse käitamine turvalises keskkonnas suurendab kaitset veelgi. Ettevõtte stsenaariumites ekstrakteeritakse ja töödeldakse andmed operatsioonisüsteemidest lugemisõigustega andmebaasi või andmetehasesse, mille skeem on kasutajasõbralik. See võimaldab andmete turvalisust, optimeeritud jõudlust ja ligipääsetavust ning rakenduse piiratud lugemisõigust.

## Näidiskoodid

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Kas on veel küsimusi tööriista kasutamise disainimustri kohta?

Liitu [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppuritega, osaleda nõuandmissessioonidel ja saada vastuseid AI agentide küsimustele.

## Lisamaterjalid

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service töötoa materjalid</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer mitmeagendi töötoa materjalid</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework ülevaade</a>


## Selle Agendi suitsutestimine (valikuline)

Pärast seda, kui oled õppinud agente kasutuselevõtma [Õppetunnis 16](../16-deploying-scalable-agents/README.md), saad suitsutestida selle õppetunni `TravelToolAgent`'i (kas ta kutsub endiselt tööriistu ja vastab?) failiga [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Vaata, kuidas seda käivitada, failist [`tests/README.md`](../tests/README.md).

## Eelmine õppetund

[Agentsete disainimustrite mõistmine](../03-agentic-design-patterns/README.md)

## Järgmine õppetund

[Agentne RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->