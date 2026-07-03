[![Cum să proiectezi agenți AI buni](../../../translated_images/ro/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Faceți clic pe imaginea de mai sus pentru a vizualiza videoclipul acestei lecții)_

# Tiparul de proiectare pentru utilizarea uneltelor

Uneltele sunt interesante deoarece permit agenților AI să aibă o gamă mai largă de capabilități. În loc ca agentul să aibă un set limitat de acțiuni pe care le poate efectua, prin adăugarea unei unelte, agentul poate efectua acum o gamă largă de acțiuni. În acest capitol, vom analiza Tiparul de Proiectare pentru Utilizarea Uneltelor, care descrie cum agenții AI pot folosi unelte specifice pentru a-și atinge obiectivele.

## Introducere

În această lecție, ne propunem să răspundem la următoarele întrebări:

- Ce este tiparul de proiectare pentru utilizarea uneltelor?
- În ce cazuri de utilizare poate fi aplicat?
- Care sunt elementele/blocurile de construcție necesare pentru implementarea tiparului de proiectare?
- Care sunt considerentele speciale pentru utilizarea Tiparului de Proiectare pentru Utilizarea Uneltelor în construirea unor agenți AI demni de încredere?

## Obiective de învățare

După finalizarea acestei lecții, vei putea:

- Defini Tiparul de Proiectare pentru Utilizarea Uneltelor și scopul său.
- Identifica cazurile de utilizare în care Tiparul de Proiectare pentru Utilizarea Uneltelor este aplicabil.
- Înțelege elementele cheie necesare pentru implementarea tiparului de proiectare.
- Recunoaște considerentele pentru asigurarea încrederii în agenții AI care utilizează acest tipar de proiectare.

## Ce este Tiparul de Proiectare pentru Utilizarea Uneltelor?

**Tiparul de Proiectare pentru Utilizarea Uneltelor** se concentrează pe oferirea LLM-urilor capacitatea de a interacționa cu unelte externe pentru a atinge obiective specifice. Uneltele sunt cod care poate fi executat de un agent pentru a efectua acțiuni. O unealtă poate fi o funcție simplă, cum ar fi un calculator, sau un apel API către un serviciu terț, cum ar fi consultarea prețului acțiunilor sau prognoza meteo. În contextul agenților AI, uneltele sunt proiectate să fie executate de agenți ca răspuns la **apeluri de funcții generate de model**.

## În ce cazuri de utilizare poate fi aplicat?

Agenții AI pot folosi unelte pentru a finaliza sarcini complexe, a obține informații sau a lua decizii. Tiparul de proiectare pentru utilizarea uneltelor este adesea folosit în scenarii care necesită interacțiune dinamică cu sisteme externe, cum ar fi baze de date, servicii web sau interpretoare de cod. Această abilitate este utilă pentru o serie de cazuri de utilizare, inclusiv:

- **Recuperare dinamică a informațiilor:** Agenții pot interoga API-uri externe sau baze de date pentru a obține date actualizate (de exemplu, interogarea unei baze de date SQLite pentru analiza datelor, obținerea prețurilor acțiunilor sau informații meteo).
- **Executarea și interpretarea codului:** Agenții pot executa cod sau scripturi pentru a rezolva probleme matematice, genera rapoarte sau efectua simulări.
- **Automatizarea fluxurilor de lucru:** Automatizarea fluxurilor de lucru repetitive sau cu mai mulți pași prin integrarea unor unelte precum programatoare de sarcini, servicii de email sau conducte de date.
- **Suport pentru clienți:** Agenții pot interacționa cu sisteme CRM, platforme de ticketing sau baze de cunoștințe pentru a rezolva întrebările utilizatorilor.
- **Generarea și editarea conținutului:** Agenții pot folosi unelte precum verificatoare gramaticale, sumarizatoare de text sau evaluatori ai siguranței conținutului pentru a asista la sarcini de creare a conținutului.

## Care sunt elementele/blocurile de construcție necesare pentru implementarea Tiparului de Proiectare pentru Utilizarea Uneltelor?

Aceste blocuri de construcție permit agentului AI să execute o gamă largă de sarcini. Să analizăm elementele cheie necesare pentru implementarea Tiparului de Proiectare pentru Utilizarea Uneltelor:

- **Schemele funcțiilor/uneltelor:** Definiții detaliate ale uneltelor disponibile, inclusiv numele funcției, scopul, parametrii necesari și rezultatele așteptate. Aceste scheme permit LLM-ului să înțeleagă ce unelte sunt disponibile și cum să construiască cereri valide.

- **Logica de execuție a funcțiilor:** Guvernează cum și când sunt invocate uneltele în funcție de intenția utilizatorului și contextul conversației. Aceasta poate include module planner, mecanisme de rutare sau fluxuri condiționale care determină utilizarea dinamică a uneltelor.

- **Sistem de gestionare a mesajelor:** Componente care gestionează fluxul conversațional între intrările utilizatorului, răspunsurile LLM, apelurile uneltelor și rezultatele uneltelor.

- **Cadru de integrare a uneltelor:** Infrastructura care conectează agentul la diverse unelte, fie că sunt funcții simple, fie servicii externe complexe.

- **Gestionarea erorilor și validarea:** Mecanisme pentru gestionarea eșecurilor în execuția uneltelor, validarea parametrilor și gestionarea răspunsurilor neașteptate.

- **Gestionarea stării:** Urmărește contextul conversațional, interacțiunile anterioare cu uneltele și datele persistente pentru a asigura consistența în interacțiunile pe mai multe ture.

Următorul pas este să analizăm în detaliu Apelarea Funcțiilor/Uneltelor.

### Apelarea Funcțiilor/Uneltelor

Apelarea funcțiilor este modalitatea principală prin care permitem Modelelor Mari de Limbaj (LLM) să interacționeze cu uneltele. Vei vedea adesea termenii 'Funcție' și 'Unealtă' folosiți interschimbabil deoarece 'funcțiile' (blocuri de cod reutilizabile) sunt 'uneltele' pe care agenții le folosesc pentru a îndeplini sarcini. Pentru ca codul unei funcții să fie invocat, un LLM trebuie să compare cererea utilizatorului cu descrierea funcției. Pentru aceasta, se trimite către LLM o schemă ce conține descrierile tuturor funcțiilor disponibile. LLM-ul apoi selectează funcția cea mai potrivită pentru sarcină și returnează numele și argumentele acesteia. Funcția selectată este invocată, răspunsul este trimis înapoi către LLM, care folosește informația pentru a răspunde cererii utilizatorului.

Pentru ca dezvoltatorii să implementeze apelarea funcțiilor pentru agenți, este necesar:

1. Un model LLM care suportă apelarea funcțiilor
2. O schemă care conține descrierile funcțiilor
3. Codul pentru fiecare funcție descrisă

Să folosim exemplul obținerii orei curente într-un oraș pentru ilustrare:

1. **Inițializarea unui LLM care suportă apelarea funcțiilor:**

    Nu toate modelele suportă apelarea funcțiilor, așa că este important să verifici dacă modelul LLM pe care îl folosești face asta. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> suportă apelarea funcțiilor. Putem începe prin inițializarea clientului Azure OpenAI. 

    ```python
    # Inițializați clientul Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Crearea unei Scheme pentru Funcție:**

    Următorul pas este să definim o schemă JSON care conține numele funcției, descrierea a ceea ce face funcția și numele și descrierile parametrilor funcției.
    Apoi vom transmite această schemă clientului creat anterior, împreună cu cererea utilizatorului de a afla ora în San Francisco. Este important de remarcat că un **apel la o unealtă** este ceea ce se returnează, **nu** răspunsul final la întrebare. Așa cum s-a menționat anterior, LLM-ul returnează numele funcției alese pentru sarcină și argumentele care vor fi transmise acesteia.

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
  
    # Mesaj inițial al utilizatorului
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Primul apel API: Cere modelului să folosească funcția
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
  
1. **Codul funcției necesar pentru executarea sarcinii:**

    Acum că LLM-ul a ales ce funcție trebuie rulată, codul care îndeplinește sarcina trebuie implementat și executat.
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

Apelarea funcțiilor este în centrul majorității, dacă nu tuturor, tiparelor de utilizare a uneltelor pentru agenți, însă implementarea acesteia de la zero poate fi uneori o provocare.
Așa cum am învățat în [Lecția 2](../../../02-explore-agentic-frameworks) cadrele agentice ne oferă blocuri de construcție predefinite pentru implementarea utilizării uneltelor.
 
## Exemple de utilizare a uneltelor cu cadre agentice

Iată câteva exemple de cum poți implementa Tiparul de Proiectare pentru Utilizarea Uneltelor folosind diferite cadre agentice:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> este un cadru AI open-source pentru construirea agenților AI. Simplifică procesul de folosire a apelării funcțiilor permițând definirea uneltelor ca funcții Python cu decoratorul `@tool`. Cadrul se ocupă de comunicarea dus-întors între model și codul tău. De asemenea, oferă acces la unelte predefinite precum Căutare de fișiere și Interpreter de cod prin `AzureAIProjectAgentProvider`.

Diagramă următoare ilustrează procesul apelării funcțiilor cu Microsoft Agent Framework:

![apelarea funcțiilor](../../../translated_images/ro/functioncalling-diagram.a84006fc287f6014.webp)

În Microsoft Agent Framework, uneltele sunt definite ca funcții decorate. Putem converti funcția `get_current_time` pe care am văzut-o anterior într-o unealtă folosind decoratorul `@tool`. Cadrul va serializa automat funcția și parametrii săi, creând schema de trimis către LLM.

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

# Creează un agent și rulează cu instrumentul
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> este un cadru agentic mai nou, proiectat să permită dezvoltatorilor să construiască, să implementeze și să scaleze agenți AI de înaltă calitate și extensibili într-un mod securizat, fără a gestiona resursele de calcul și stocare subiacente. Este util în special pentru aplicații enterprise deoarece este un serviciu complet gestionat cu securitate de nivel enterprise.

Comparativ cu dezvoltarea directă folosind API-ul LLM, Azure AI Agent Service oferă unele avantaje, inclusiv:

- Apelarea automată a uneltelor – nu este nevoie să parsezi un apel la unealtă, să invoci unealta și să gestionezi răspunsul; toate acestea se fac acum pe server
- Date gestionate securizat – în loc să gestionezi singur starea conversației, poți folosi threads pentru a stoca toate informațiile necesare
- Unelte gata făcute – unelte pe care le poți folosi pentru a interacționa cu sursele tale de date, cum ar fi Bing, Azure AI Search și Azure Functions.

Uneltele disponibile în Azure AI Agent Service pot fi împărțite în două categorii:

1. Unelte de cunoaștere:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Ancorare cu Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Căutare de fișiere</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Unelte de acțiune:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Apelarea funcțiilor</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpreter de cod</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Unelte definite prin OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service ne permite să folosim aceste unelte împreună ca un `toolset`. De asemenea, utilizează `threads` care țin evidența istoricului mesajelor dintr-o conversație anume.

Imaginează-ți că ești un agent de vânzări la o companie numită Contoso. Vrei să dezvolți un agent conversațional care să poată răspunde la întrebări despre datele tale de vânzări.

Imaginea următoare ilustrează cum ai putea folosi Azure AI Agent Service pentru a analiza datele tale de vânzări:

![Agentic Service în Acțiune](../../../translated_images/ro/agent-service-in-action.34fb465c9a84659e.webp)

Pentru a utiliza oricare dintre aceste unelte cu serviciul, putem crea un client și defini o unealtă sau un set de unelte. Pentru a implementa practic aceasta, putem folosi următorul cod Python. LLM-ul va putea examina toolsetul și decide dacă să folosească funcția creată de utilizator, `fetch_sales_data_using_sqlite_query`, sau Interpreterul de Cod predefinit, în funcție de cererea utilizatorului.

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

# Inițializați setul de instrumente
toolset = ToolSet()

# Inițializați agentul de apelare a funcțiilor cu funcția fetch_sales_data_using_sqlite_query și adăugați-l în setul de instrumente
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inițializați instrumentul Code Interpreter și adăugați-l în setul de instrumente.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Care sunt considerentele speciale pentru utilizarea Tiparului de Proiectare pentru Utilizarea Uneltelor în construirea agenților AI de încredere?

O preocupare comună legată de SQL-ul generat dinamic de LLM-uri este securitatea, în special riscul de injecție SQL sau acțiuni malițioase, cum ar fi ștergerea sau manipularea bazei de date. Deși aceste preocupări sunt valide, ele pot fi gestionate eficient prin configurarea corectă a permisiunilor de acces la baza de date. Pentru majoritatea bazelor de date, acest lucru implică configurarea bazei ca numai în citire. Pentru servicii de baze de date precum PostgreSQL sau Azure SQL, aplicația trebuie să aibă un rol doar în citire (SELECT).

Executarea aplicației într-un mediu securizat oferă o protecție suplimentară. În scenarii enterprise, datele sunt de obicei extrase și transformate din sistemele operaționale într-o bază de date sau depozit de date doar în citire, cu o schemă prietenoasă pentru utilizator. Această abordare asigură că datele sunt securizate, optimizate pentru performanță și accesibilitate, iar aplicația are acces restricționat, doar în citire.

## Mostre de cod

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Mai ai întrebări despre Tiparele de Utilizare a Uneltelor?

Alătură-te [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la ore de birou și a-ți primi răspunsuri la întrebările despre agenții AI.

## Resurse suplimentare

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Atelier Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Atelier Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Prezentare generală Microsoft Agent Framework</a>

## Lecția anterioară

[Înțelegerea Tiparelor de Proiectare Agentice](../03-agentic-design-patterns/README.md)

## Lecția următoare
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->