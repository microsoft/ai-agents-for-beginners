[![Cum să proiectezi agenți AI buni](../../../translated_images/ro/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Fă clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Modelul de proiectare pentru utilizarea instrumentelor

Instrumentele sunt interesante deoarece permit agenților AI să aibă un spectru mai larg de capabilități. În loc ca agentul să aibă un set limitat de acțiuni pe care le poate efectua, prin adăugarea unui instrument agentul poate acum efectua o gamă largă de acțiuni. În acest capitol, vom analiza Modelul de Proiectare pentru Utilizarea Instrumentelor, care descrie modul în care agenții AI pot utiliza instrumente specifice pentru a-și atinge obiectivele.

## Introducere

În această lecție ne propunem să răspundem la următoarele întrebări:

- Ce este modelul de proiectare pentru utilizarea instrumentelor?
- În ce cazuri de utilizare poate fi aplicat?
- Care sunt elementele/blocurile de construcție necesare pentru a implementa modelul de proiectare?
- Care sunt considerațiile speciale pentru utilizarea Modelului de Proiectare pentru Utilizarea Instrumentelor în construirea unor agenți AI demni de încredere?

## Obiective de învățare

După finalizarea acestei lecții, vei putea:

- Defini Modelul de Proiectare pentru Utilizarea Instrumentelor și scopul său.
- Identifica cazuri de utilizare în care Modelul de Proiectare pentru Utilizarea Instrumentelor este aplicabil.
- Înțelege elementele cheie necesare pentru a implementa modelul de proiectare.
- Recunoaște considerațiile pentru asigurarea încrederii în agenții AI care folosesc acest model de proiectare.

## Ce este Modelul de Proiectare pentru Utilizarea Instrumentelor?

Modelul de Proiectare pentru Utilizarea Instrumentelor se concentrează pe oferirea capacității LLM-urilor de a interacționa cu instrumente externe pentru a atinge obiective specifice. Instrumentele sunt cod care poate fi executat de un agent pentru a efectua acțiuni. Un instrument poate fi o funcție simplă, cum ar fi un calculator, sau un apel API către un serviciu terț, cum ar fi căutarea prețului acțiunilor sau prognoza meteo. În contextul agenților AI, instrumentele sunt concepute pentru a fi executate de agenți ca răspuns la apeluri de funcții generate de model.

## În ce cazuri de utilizare poate fi aplicat?

Agenții AI pot valorifica instrumentele pentru a finaliza sarcini complexe, a recupera informații sau a lua decizii. Modelul de proiectare pentru utilizarea instrumentelor este des folosit în scenarii care necesită interacțiune dinamică cu sisteme externe, cum ar fi baze de date, servicii web sau interpretoare de cod. Această capacitate este utilă pentru o serie de cazuri de utilizare, inclusiv:

- Recuperare dinamică a informațiilor: Agenții pot interoga API-uri externe sau baze de date pentru a obține date actualizate (de exemplu, interogarea unei baze de date SQLite pentru analiză de date, obținerea prețurilor acțiunilor sau a informațiilor meteo).
- Execuție și interpretare de cod: Agenții pot executa cod sau scripturi pentru a rezolva probleme matematice, a genera rapoarte sau a efectua simulări.
- Automatizarea fluxurilor de lucru: Automatizarea sarcinilor repetitive sau a fluxurilor de lucru în mai mulți pași prin integrarea unor instrumente precum programatori de sarcini, servicii de e-mail sau pipeline-uri de date.
- Suport clienți: Agenții pot interacționa cu sisteme CRM, platforme de ticketing sau baze de cunoștințe pentru a rezolva întrebările utilizatorilor.
- Generare și editare de conținut: Agenții pot utiliza instrumente precum verificatoare gramaticale, rezumatori de text sau evaluatori de securitate a conținutului pentru a asista în sarcinile de creare a conținutului.

## Care sunt elementele/blocurile de construcție necesare pentru a implementa modelul de proiectare pentru utilizarea instrumentelor?

Aceste blocuri de construcție permit agentului AI să execute o gamă largă de sarcini. Să analizăm elementele cheie necesare pentru a implementa Modelul de Proiectare pentru Utilizarea Instrumentelor:

- Scheme pentru funcții/instrumente: Definiții detaliate ale instrumentelor disponibile, incluzând numele funcției, scopul, parametrii necesari și rezultatele așteptate. Aceste scheme permit LLM-ului să înțeleagă ce instrumente sunt disponibile și cum să construiască cereri valide.

- Logica de execuție a funcțiilor: Guvernează modul și momentul în care instrumentele sunt invocate pe baza intenției utilizatorului și contextului conversației. Aceasta poate include module de planificare, mecanisme de rutare sau fluxuri condiționale care determină utilizarea instrumentelor în mod dinamic.

- Sistemul de gestionare a mesajelor: Componente care gestionează fluxul conversațional între intrările utilizatorului, răspunsurile LLM, apelurile către instrumente și rezultatele acestora.

- Cadru de integrare a instrumentelor: Infrastructura care conectează agentul la diverse instrumente, fie că sunt funcții simple sau servicii externe complexe.

- Tratarea erorilor și validarea: Mecanisme pentru gestionarea eșecurilor în execuția instrumentelor, validarea parametrilor și administrarea răspunsurilor neașteptate.

- Managementul stării: Urmărește contextul conversației, interacțiunile anterioare cu instrumentele și datele persistente pentru a asigura consistența în interacțiunile pe mai multe runde.

Următorul pas este să analizăm Apelul de Funcții/Instrumente mai în detaliu.
 
### Apelul de Funcții/Instrumente

Apelul de funcții este modalitatea principală prin care permitem Modelelor Lingvistice Mari (LLM) să interacționeze cu instrumentele. Vei vedea adesea „Funcție” și „Instrument” folosite interschimbabil deoarece „funcțiile” (blocuri de cod reutilizabile) sunt „instrumentele” pe care agenții le folosesc pentru a îndeplini sarcini. Pentru ca codul unei funcții să fie invocat, un LLM trebuie să compare cererea utilizatorului cu descrierea funcțiilor. Pentru a face asta, o schemă care conține descrierile tuturor funcțiilor disponibile este trimisă către LLM. LLM selectează apoi funcția cea mai potrivită pentru sarcină și returnează numele și argumentele acesteia. Funcția selectată este invocată, răspunsul ei este trimis înapoi la LLM, care folosește informația pentru a răspunde la cererea utilizatorului.

Pentru ca dezvoltatorii să implementeze apelul de funcții pentru agenți, vei avea nevoie de:

1. Un model LLM care suportă apelul de funcții
2. O schemă care conține descrierile funcțiilor
3. Codul pentru fiecare funcție descrisă

Să folosim exemplul obținerii orei curente într-un oraș pentru a ilustra:

1. Initializează un LLM care suportă apelul de funcții:

    Nu toate modelele suportă apelul de funcții, așa că este important să verifici că LLM-ul pe care îl folosești îl suportă.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> suportă apelul de funcții. Putem începe prin inițializarea clientului Azure OpenAI. 

    ```python
    # Inițializează clientul Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. Creează o schemă de funcție:

    Următorul pas este să definim o schemă JSON care conține numele funcției, descrierea a ceea ce face funcția și numele și descrierile parametrilor funcției.
    Vom lua apoi această schemă și o vom transmite clientului creat anterior, împreună cu cererea utilizatorului de a afla ora în San Francisco. Ceea ce este important de reținut este că un apel la un instrument este ceea ce este returnat, nu răspunsul final la întrebare. După cum s-a menționat mai devreme, LLM returnează numele funcției pe care a selectat-o pentru sarcină și argumentele care îi vor fi transmise.

    ```python
    # Descrierea funcției pentru ca modelul să o citească.
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
  
    # Mesaj inițial al utilizatorului
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Primul apel API: Cere modelului să utilizeze funcția
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Procesează răspunsul modelului
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. Codul funcției necesar pentru a îndeplini sarcina:

    Acum că LLM a ales care funcție trebuie rulată, codul care execută sarcina trebuie implementat și rulat.
    Putem implementa codul pentru a obține ora curentă în Python. De asemenea, va trebui să scriem codul pentru a extrage numele și argumentele din response_message pentru a obține rezultatul final.

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
     # Gestionează apelurile funcțiilor
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
  
      # Al doilea apel la API: Obține răspunsul final de la model
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

Apelul de Funcții se află în centrul majorității, dacă nu al tuturor, designurilor de utilizare a instrumentelor pentru agenți, însă implementarea lui de la zero poate fi uneori provocatoare.
După cum am învățat în [Lesson 2](../../../02-explore-agentic-frameworks) cadrele agentice ne oferă blocuri de construcție predefinite pentru a implementa utilizarea instrumentelor.
 
## Exemple de utilizare a instrumentelor cu cadre agentice

Iată câteva exemple despre cum poți implementa Modelul de Proiectare pentru Utilizarea Instrumentelor folosind diferite cadre agentice:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> este un cadru AI open-source pentru construirea agenților AI. Acesta simplifică procesul de folosire a apelului de funcții permițându-ți să definești instrumente ca funcții Python cu decoratorul `@tool`. Cadrul gestionează comunicarea dus-întors între model și codul tău. De asemenea, oferă acces la instrumente preconstruite precum File Search și Code Interpreter prin `AzureAIProjectAgentProvider`.

Diagrama următoare ilustrează procesul apelului de funcții cu Microsoft Agent Framework:

![apel de funcții](../../../translated_images/ro/functioncalling-diagram.a84006fc287f6014.webp)

În Microsoft Agent Framework, instrumentele sunt definite ca funcții decorate. Putem converti funcția `get_current_time` pe care am văzut-o mai devreme într-un instrument folosind decoratorul `@tool`. Cadrul va serializa automat funcția și parametrii săi, creând schema care va fi trimisă către LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Creează clientul
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Creează un agent și rulează-l cu instrumentul
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> este un cadru agentic mai nou, conceput pentru a permite dezvoltatorilor să construiască, să implementeze și să scaleze în mod securizat agenți AI de înaltă calitate și extensibili, fără a fi nevoie să gestioneze resursele de calcul și stocare subiacente. Este deosebit de util pentru aplicațiile enterprise deoarece este un serviciu complet gestionat cu securitate la nivel enterprise.

Comparativ cu dezvoltarea directă cu API-ul LLM, Azure AI Agent Service oferă câteva avantaje, inclusiv:

- Apel automat al instrumentelor – nu este nevoie să parcurgi procesul de parsare a unui apel către un instrument, invocarea instrumentului și tratarea răspunsului; toate acestea se fac acum server-side
- Date gestionate în siguranță – în loc să îți gestionezi propriul stat al conversației, te poți baza pe threads pentru a stoca toate informațiile de care ai nevoie
- Instrumente disponibile din start – instrumente pe care le poți folosi pentru a interacționa cu sursele tale de date, precum Bing, Azure AI Search și Azure Functions.

Instrumentele disponibile în Azure AI Agent Service pot fi împărțite în două categorii:

1. Instrumente de cunoaștere:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding cu Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Instrumente de acțiune:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Apel de Funcții</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Instrumente definite OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service ne permite să utilizăm aceste instrumente împreună ca un `toolset`. De asemenea, utilizează `threads` care urmăresc istoricul mesajelor dintr-o anumită conversație.

Imaginează-ți că ești agent de vânzări la o companie numită Contoso. Vrei să dezvolți un agent conversațional care să poată răspunde la întrebări despre datele tale de vânzări.

Imaginea următoare ilustrează cum ai putea folosi Azure AI Agent Service pentru a analiza datele tale de vânzări:

![Serviciu Agentic în Acțiune](../../../translated_images/ro/agent-service-in-action.34fb465c9a84659e.webp)

Pentru a folosi oricare dintre aceste instrumente cu serviciul putem crea un client și defini un instrument sau un toolset. Pentru a implementa acest lucru practic putem folosi următorul cod Python. LLM va putea examina toolset-ul și decide dacă să folosească funcția creată de utilizator, `fetch_sales_data_using_sqlite_query`, sau Code Interpreter-ul preconstruit, în funcție de cererea utilizatorului.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funcția fetch_sales_data_using_sqlite_query care poate fi găsită într-un fișier fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inițializează setul de instrumente
toolset = ToolSet()

# Inițializează agentul de apelare a funcțiilor cu funcția fetch_sales_data_using_sqlite_query și adaugă-l la setul de instrumente
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inițializează instrumentul Code Interpreter și adaugă-l la setul de instrumente
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Care sunt considerațiile speciale pentru utilizarea Modelului de Proiectare pentru Utilizarea Instrumentelor în construirea unor agenți AI demni de încredere?

O preocupare comună legată de SQL generat dinamic de LLM-uri este securitatea, în special riscul de SQL injection sau acțiuni malițioase, cum ar fi ștergerea sau modificarea bazei de date. Deși aceste preocupări sunt valide, ele pot fi mitigate eficient prin configurarea corespunzătoare a permisiunilor de acces la baze de date. Pentru majoritatea bazelor de date, aceasta implică configurarea bazei de date ca read-only. Pentru servicii de baze de date precum PostgreSQL sau Azure SQL, aplicația ar trebui să aibă un rol read-only (SELECT).

Rularea aplicației într-un mediu sigur sporește în continuare protecția. În scenarii enterprise, datele sunt, de obicei, extrase și transformate din sistemele operaționale într-o bază de date read-only sau într-un data warehouse cu un schemă prietenoasă. Această abordare asigură că datele sunt securizate, optimizate pentru performanță și accesibilitate și că aplicația are acces restricționat, doar în citire.

## Exemple de cod

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Mai ai întrebări despre Modelele de Proiectare pentru Utilizarea Instrumentelor?

Alătură-te [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la ore de consultanță și a-ți rezolva întrebările despre Agenții AI.

## Resurse suplimentare

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Prezentare generală Microsoft Agent Framework</a>

## Lecția anterioară

[Înțelegerea modelelor de proiectare agentice](../03-agentic-design-patterns/README.md)

## Următoarea lecție
[Agentiv RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să fim cât mai preciși, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă o traducere profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventuale neînțelegeri sau interpretări eronate care rezultă din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->