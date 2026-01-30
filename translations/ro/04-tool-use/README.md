[![Cum să proiectăm agenți AI buni](../../../translated_images/ro/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Faceți clic pe imaginea de mai sus pentru a viziona video-ul acestei lecții)_

# Modelul de proiectare Tool Use

Uneltele sunt interesante deoarece permit agenților AI să aibă o gamă mai largă de capacități. În loc ca agentul să aibă un set limitat de acțiuni pe care le poate efectua, prin adăugarea unei unelte, agentul poate acum să execute o gamă largă de acțiuni. În acest capitol, vom analiza modelul de proiectare Tool Use, care descrie cum agenții AI pot utiliza unelte specifice pentru a-și atinge obiectivele.

## Introducere

În această lecție, urmărim să răspundem la următoarele întrebări:

- Ce este modelul de proiectare Tool Use?
- Pentru ce cazuri de utilizare poate fi aplicat?
- Care sunt elementele/blocurile de construcție necesare pentru implementarea modelului de proiectare?
- Care sunt considerațiile speciale pentru utilizarea modelului de proiectare Tool Use în construirea unor agenți AI de încredere?

## Obiectivele de învățare

După finalizarea acestei lecții, veți fi capabil să:

- Definiți modelul de proiectare Tool Use și scopul său.
- Identificați cazurile de utilizare în care modelul de proiectare Tool Use este aplicabil.
- Înțelegeți elementele cheie necesare pentru implementarea modelului de proiectare.
- Recunoașteți considerațiile pentru asigurarea încrederii în agenții AI care utilizează acest model de proiectare.

## Ce este modelul de proiectare Tool Use?

**Modelul de proiectare Tool Use** se concentrează pe oferirea LLM-urilor capacitatea de a interacționa cu unelte externe pentru a atinge obiective specifice. Uneltele sunt cod care poate fi executat de un agent pentru a efectua acțiuni. O unealtă poate fi o funcție simplă, cum ar fi un calculator, sau un apel API către un serviciu terț, cum ar fi consultarea prețurilor acțiunilor sau prognoza meteo. În contextul agenților AI, uneltele sunt proiectate să fie executate de agenți ca răspuns la **apeluri de funcții generate de model**.

## Pentru ce cazuri de utilizare poate fi aplicat?

Agenții AI pot folosi uneltele pentru a finaliza sarcini complexe, a recupera informații sau a lua decizii. Modelul de proiectare Tool Use este adesea folosit în scenarii care necesită interacțiune dinamică cu sisteme externe, cum ar fi baze de date, servicii web sau interpretoare de cod. Această abilitate este utilă pentru mai multe cazuri de utilizare, inclusiv:

- **Recuperare dinamică a informațiilor:** Agenții pot interoga API-uri externe sau baze de date pentru a obține date actualizate (de exemplu, interogarea unei baze de date SQLite pentru analiza datelor, obținerea prețurilor acțiunilor sau a informațiilor meteo).
- **Executarea și interpretarea codului:** Agenții pot executa cod sau scripturi pentru a rezolva probleme matematice, genera rapoarte sau efectua simulări.
- **Automatizarea fluxurilor de lucru:** Automatizarea fluxurilor de lucru repetitive sau cu mai mulți pași prin integrarea uneltelor precum planificatoare de sarcini, servicii de email sau conducte de date.
- **Suport clienți:** Agenții pot interacționa cu sisteme CRM, platforme de ticketing sau baze de cunoștințe pentru a rezolva întrebările utilizatorilor.
- **Generarea și editarea conținutului:** Agenții pot folosi unelte precum verificatoare gramaticale, sumarizatoare de text sau evaluatori ai siguranței conținutului pentru a asista în sarcini de creare a conținutului.

## Care sunt elementele/blocurile de construcție necesare pentru implementarea modelului de proiectare Tool Use?

Aceste blocuri de construcție permit agentului AI să efectueze o gamă largă de sarcini. Să analizăm elementele cheie necesare pentru implementarea modelului de proiectare Tool Use:

- **Scheme de funcții/unelte**: Definiții detaliate ale uneltelor disponibile, incluzând numele funcției, scopul, parametrii necesari și rezultatele așteptate. Aceste scheme permit LLM-ului să înțeleagă ce unelte sunt disponibile și cum să construiască cereri valide.

- **Logică de executare a funcțiilor**: Guvernează cum și când sunt invocate uneltele în funcție de intenția utilizatorului și contextul conversației. Aceasta poate include module de planificare, mecanisme de rutare sau fluxuri condiționale care determină utilizarea dinamică a uneltelor.

- **Sistem de gestionare a mesajelor**: Componente care gestionează fluxul conversațional între intrările utilizatorului, răspunsurile LLM, apelurile către unelte și rezultatele acestora.

- **Cadru de integrare a uneltelor**: Infrastructură care conectează agentul la diferite unelte, fie că sunt funcții simple sau servicii externe complexe.

- **Gestionarea erorilor și validare**: Mecanisme pentru tratarea eșecurilor în execuția uneltelor, validarea parametrilor și gestionarea răspunsurilor neașteptate.

- **Gestionarea stării**: Urmărește contextul conversației, interacțiunile anterioare cu uneltele și date persistente pentru a asigura consistența pe parcursul interacțiunilor pe mai multe runde.

În continuare, să analizăm în detaliu apelarea funcțiilor/uneltelor.
 
### Apelarea funcțiilor/uneltelor

Apelarea funcțiilor este modul principal prin care permitem modelelor de limbaj mari (LLM-uri) să interacționeze cu uneltele. Veți vedea adesea termenii „Funcție” și „Unealtă” folosiți interschimbabil deoarece „funcțiile” (blocuri de cod reutilizabile) sunt „uneltele” pe care agenții le folosesc pentru a realiza sarcini. Pentru ca codul unei funcții să fie invocat, un LLM trebuie să compare cererea utilizatorului cu descrierea funcției. Pentru aceasta, o schemă care conține descrierile tuturor funcțiilor disponibile este trimisă către LLM. LLM selectează apoi funcția cea mai potrivită pentru sarcină și returnează numele și argumentele acesteia. Funcția selectată este apoi invocată, răspunsul său este trimis înapoi către LLM, care folosește informația pentru a răspunde cererii utilizatorului.

Pentru ca dezvoltatorii să implementeze apelarea funcțiilor pentru agenți, vor avea nevoie de:

1. Un model LLM care suportă apelarea funcțiilor
2. O schemă care conține descrierile funcțiilor
3. Codul pentru fiecare funcție descrisă

Să folosim exemplul obținerii orei curente într-un oraș pentru a ilustra:

1. **Inițializați un LLM care suportă apelarea funcțiilor:**

    Nu toate modelele suportă apelarea funcțiilor, așa că este important să verificați dacă modelul LLM pe care îl utilizați face acest lucru. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> suportă apelarea funcțiilor. Putem începe prin inițializarea clientului Azure OpenAI. 

    ```python
    # Inițializează clientul Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Creați o schemă de funcție**:

    Următorul pas este definirea unei scheme JSON care conține numele funcției, descrierea a ceea ce face funcția și numele și descrierile parametrilor funcției.
    Vom lua apoi această schemă și o vom transmite clientului creat anterior, împreună cu cererea utilizatorului pentru a afla ora în San Francisco. Ce este important de menționat este că un **apel al uneltei** este ceea ce se întoarce, **nu** răspunsul final la întrebare. Așa cum am menționat mai devreme, LLM returnează numele funcției selectate pentru sarcină și argumentele care îi vor fi transmise.

    ```python
    # Descrierea funcției pentru ca modelul să o citească
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
  
    # Mesajul inițial al utilizatorului
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Prima apelare API: Cere modelului să utilizeze funcția
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
  
1. **Codul funcției necesar pentru a realiza sarcina:**

    Acum că LLM a ales ce funcție trebuie rulată, codul care efectuează sarcina trebuie implementat și executat.
    Putem implementa codul pentru a obține ora curentă în Python. De asemenea, va trebui să scriem cod pentru a extrage numele și argumentele din response_message pentru a obține rezultatul final.

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
     # Gestionați apelurile funcțiilor
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
  
      # Al doilea apel API: Obțineți răspunsul final de la model
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

Apelarea funcțiilor este în centrul multor, dacă nu a tuturor, modele de utilizare a uneltelor pentru agenți, totuși implementarea de la zero poate fi uneori provocatoare.
Așa cum am învățat în [Lecția 2](../../../02-explore-agentic-frameworks), cadrele agentice ne oferă blocuri de construcție predefinite pentru implementarea utilizării uneltelor.
 
## Exemple de utilizare a uneltelor cu cadre agentice

Iată câteva exemple despre cum puteți implementa modelul de proiectare Tool Use folosind diferite cadre agentice:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> este un cadru AI open-source pentru dezvoltatorii .NET, Python și Java care lucrează cu modele de limbaj mari (LLM-uri). Simplifică procesul de utilizare a apelării funcțiilor prin descrierea automată a funcțiilor și a parametrilor lor către model printr-un proces numit <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializare</a>. De asemenea, gestionează comunicarea în ambele sensuri între model și codul dumneavoastră. Un alt avantaj al utilizării unui cadru agentic precum Semantic Kernel este că vă permite accesul la unelte preconstruite precum <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Căutare în fișiere</a> și <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Interpretator de cod</a>.

Diagrama următoare ilustrează procesul de apelare a funcțiilor cu Semantic Kernel:

![function calling](../../../translated_images/ro/functioncalling-diagram.a84006fc287f6014.webp)

În Semantic Kernel, funcțiile/uneltele sunt numite <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Pluginuri</a>. Putem converti funcția `get_current_time` pe care am văzut-o anterior într-un plugin transformând-o într-o clasă care conține funcția. De asemenea, putem importa decoratorul `kernel_function`, care primește descrierea funcției. Când creați apoi un kernel cu GetCurrentTimePlugin, kernel-ul va serializa automat funcția și parametrii săi, creând schema pe care o trimite către LLM în proces.

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

# Creează kernel-ul
kernel = Kernel()

# Creează pluginul
get_current_time_plugin = GetCurrentTimePlugin(location)

# Adaugă pluginul la kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> este un cadru agentic mai nou care este conceput pentru a permite dezvoltatorilor să construiască, să implementeze și să scaleze în mod securizat agenți AI de înaltă calitate și extensibili, fără a fi nevoie să gestioneze resursele de calcul și stocare subiacente. Este deosebit de util pentru aplicații enterprise, deoarece este un serviciu complet gestionat, cu securitate la nivel enterprise.

Comparativ cu dezvoltarea folosind direct API-ul LLM, Azure AI Agent Service oferă câteva avantaje, inclusiv:

- Apelare automată a uneltelor – nu este necesar să parsați un apel de unealtă, să invocați unealta și să gestionați răspunsul; toate acestea sunt acum făcute pe partea de server
- Date gestionate securizat – în loc să gestionați propriul context de conversație, puteți folosi fire (threads) care stochează toată informația necesară
- Unelte gata de utilizare – unelte pe care le puteți folosi pentru a interacționa cu sursele dumneavoastră de date, precum Bing, Azure AI Search și Azure Functions.

Uneltele disponibile în Azure AI Agent Service pot fi împărțite în două categorii:

1. Unelte de Cunoaștere:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Încorporare cu Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Căutare în fișiere</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Unelte de Acțiune:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Apelare de funcții</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpretator de cod</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Unelte definite OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Serviciul Agent ne permite să folosim aceste unelte împreună ca un `toolset`. De asemenea, utilizează `fir` (threads) care urmăresc istoricul mesajelor dintr-o conversație anume.

Imaginați-vă că sunteți un agent de vânzări la o companie numită Contoso. Doriți să dezvoltați un agent conversațional care să poată răspunde întrebărilor despre datele dumneavoastră de vânzări.

Imaginea următoare ilustrează cum ați putea folosi Azure AI Agent Service pentru a analiza datele dumneavoastră de vânzări:

![Agentic Service In Action](../../../translated_images/ro/agent-service-in-action.34fb465c9a84659e.webp)

Pentru a folosi oricare dintre aceste unelte cu serviciul, putem crea un client și defini o unealtă sau un set de unelte. Pentru a implementa acest lucru practic, putem folosi următorul cod Python. LLM va putea analiza setul de unelte și decide dacă să folosească funcția creată de utilizator, `fetch_sales_data_using_sqlite_query`, sau interpretatorul de cod predefinit, în funcție de cererea utilizatorului.

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

# Inițializați setul de unelte
toolset = ToolSet()

# Inițializați agentul de apelare a funcțiilor cu funcția fetch_sales_data_using_sqlite_query și adăugați-l la setul de unelte
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inițializați instrumentul Code Interpreter și adăugați-l la setul de unelte.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Care sunt considerațiile speciale pentru utilizarea modelului de proiectare Tool Use în construirea unor agenți AI de încredere?

O preocupare comună legată de SQL-ul generat dinamic de LLM-uri este securitatea, în special riscul de injecție SQL sau acțiuni rău intenționate, cum ar fi ștergerea sau manipularea bazei de date. Deși aceste preocupări sunt valide, ele pot fi gestionate eficient prin configurarea corectă a permisiunilor de acces la baza de date. Pentru majoritatea bazelor de date, acest lucru implică configurarea bazei de date în mod read-only. Pentru servicii de baze de date precum PostgreSQL sau Azure SQL, aplicația trebuie să fie atribuită la un rol read-only (SELECT).
Executarea aplicației într-un mediu sigur sporește și mai mult protecția. În scenarii enterprise, datele sunt de obicei extrase și transformate din sistemele operaționale într-o bază de date sau depozit de date doar în citire, cu un schema prietenoasă cu utilizatorul. Această abordare asigură că datele sunt securizate, optimizate pentru performanță și accesibilitate, iar aplicația are acces restricționat, doar în citire.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Ai mai multe întrebări despre utilizarea tiparelor de design pentru unelte?

Alătură-te [Discord Azure AI Foundry](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la orele de consultanță și a primi răspunsuri la întrebările tale despre AI Agents.

## Resurse suplimentare

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Atelierul Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Atelierul Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Tutorial Apelare Funcții Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Interpreter de Cod Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Unelte Autogen</a>

## Lecția Anterioară

[Înțelegerea tiparelor de design agentic](../03-agentic-design-patterns/README.md)

## Lecția Următoare

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventuale neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->