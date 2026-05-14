[![Cum să proiectezi agenți AI buni](../../../translated_images/ro/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Fă clic pe imaginea de mai sus pentru a vizualiza videoclipul acestei lecții)_

# Tiparul de Proiectare pentru Utilizarea Uneltelor

Uneltele sunt interesante deoarece permit agenților AI să aibă o gamă mai largă de capabilități. În loc ca agentul să aibă un set limitat de acțiuni pe care le poate realiza, prin adăugarea unei unelte, agentul poate acum să realizeze o gamă largă de acțiuni. În acest capitol, vom analiza Tiparul de Proiectare pentru Utilizarea Uneltelor, care descrie modul în care agenții AI pot folosi unelte specifice pentru a-și atinge scopurile.

## Introducere

În această lecție, căutăm să răspundem următoarelor întrebări:

- Ce este tiparul de proiectare pentru utilizarea uneltelor?
- Care sunt cazurile de utilizare la care poate fi aplicat?
- Care sunt elementele/blocurile de construcție necesare pentru implementarea tiparului de proiectare?
- Care sunt considerațiile speciale pentru utilizarea Tiparului de Proiectare pentru Utilizarea Uneltelor pentru a construi agenți AI de încredere?

## Obiective de Învățare

După finalizarea acestei lecții, vei putea:

- Defini Tiparul de Proiectare pentru Utilizarea Uneltelor și scopul său.
- Identifica cazuri de utilizare unde Tiparul de Proiectare pentru Utilizarea Uneltelor este aplicabil.
- Înțelege elementele cheie necesare pentru implementarea tiparului de proiectare.
- Recunoaște considerațiile pentru asigurarea încrederii în agenții AI care folosesc acest tipar de proiectare.

## Ce este Tiparul de Proiectare pentru Utilizarea Uneltelor?

**Tiparul de Proiectare pentru Utilizarea Uneltelor** se concentrează pe oferirea modelelor de limbaj mari (LLM) abilitatea de a interacționa cu unelte externe pentru a atinge obiective specifice. Uneltele sunt cod care poate fi executat de un agent pentru a efectua acțiuni. O unealtă poate fi o funcție simplă, precum un calculator, sau un apel API către un serviciu terț, cum ar fi căutarea prețului acțiunilor sau prognoza meteo. În contextul agenților AI, uneltele sunt proiectate să fie executate de agenți ca răspuns la **apeluri de funcții generate de model**.

## La ce cazuri de utilizare poate fi aplicat?

Agenții AI pot exploata uneltele pentru a finaliza sarcini complexe, a recupera informații sau a lua decizii. Tiparul de proiectare pentru utilizarea uneltelor este adesea folosit în scenarii care necesită interacțiune dinamică cu sisteme externe, cum ar fi baze de date, servicii web sau interpretoare de cod. Această abilitate este utilă pentru o serie de cazuri diferite, inclusiv:

- **Recuperare Dinamică a Informațiilor:** Agenții pot interoga API-uri externe sau baze de date pentru a obține date actualizate (de exemplu, interogarea unei baze de date SQLite pentru analiză de date, obținerea prețurilor acțiunilor sau informații despre vreme).
- **Execuția și Interpretarea Codului:** Agenții pot executa cod sau scripturi pentru a rezolva probleme matematice, genera rapoarte sau realiza simulări.
- **Automatizarea Fluxurilor de Lucru:** Automatizarea sarcinilor repetitive sau a fluxurilor de lucru multi-pas prin integrarea uneltelor precum programatori de sarcini, servicii de email sau conducte de date.
- **Suport pentru Clienți:** Agenții pot interacționa cu sisteme CRM, platforme de ticketing sau baze de cunoștințe pentru a rezolva întrebările utilizatorilor.
- **Generare și Editare de Conținut:** Agenții pot folosi unelte precum verificatoare gramaticale, rezumatori de text sau evaluatori de siguranță a conținutului pentru a asista în sarcini de creare a conținutului.

## Care sunt elementele/blocurile necesare pentru implementarea tiparului de utilizare a uneltelor?

Aceste blocuri de construcție permit agentului AI să efectueze o gamă largă de sarcini. Să vedem elementele cheie necesare pentru implementarea Tiparului de Proiectare pentru Utilizarea Uneltelor:

- **Schemele Funcțiilor/Uneltelor**: Definiții detaliate ale uneltelor disponibile, inclusiv numele funcției, scopul, parametrii necesari și rezultatele așteptate. Aceste scheme permit LLM-ului să înțeleagă ce unelte sunt disponibile și cum să construiască cereri valide.

- **Logica Execuției Funcțiilor**: Guvernează modul și momentul în care uneltele sunt invocate bazat pe intenția utilizatorului și contextul conversației. Aceasta poate include module de planificare, mecanisme de rutare sau fluxuri condiționale care determină utilizarea uneltei dinamic.

- **Sistemul de Gestionare a Mesajelor**: Componente care gestionează fluxul conversațional între intrările utilizatorului, răspunsurile LLM-ului, apelurile către unelte și rezultatele uneltelor.

- **Infrastructura de Integrare a Uneltelor**: Infrastructura care conectează agentul la diverse unelte, fie că sunt funcții simple sau servicii externe complexe.

- **Gestionarea Erorilor și Validarea**: Mecanisme pentru gestionarea eșecurilor în execuția uneltelor, validarea parametrilor și gestionarea răspunsurilor neașteptate.

- **Gestionarea Stării**: Urmărește contextul conversației, interacțiunile anterioare cu uneltele și date persistente pentru a asigura consistența în interacțiunile pe mai multe runde.

Următorul pas este să analizăm apelarea Funcțiilor/Uneltelor în detaliu.

### Apelarea Funcțiilor/Uneltelor

Apelarea funcțiilor este modalitatea principală prin care permitem modelelor de limbaj mari (LLM) să interacționeze cu uneltele. Vei observa adesea că termenii 'Funcție' și 'Unealtă' sunt folosiți interschimbabil deoarece 'funcțiile' (blocuri de cod reutilizabil) sunt 'uneltele' pe care agenții le folosesc pentru a realiza sarcini. Pentru ca codul unei funcții să fie invocat, un LLM trebuie să compare cererea utilizatorului cu descrierea funcțiilor. Pentru a face acest lucru, o schemă care conține descrierile tuturor funcțiilor disponibile este trimisă către LLM. Apoi, LLM selectează funcția cea mai potrivită pentru sarcină și returnează numele și argumentele acesteia. Funcția selectată este invocată, răspunsul ei este trimis înapoi către LLM, care folosește aceste informații pentru a răspunde cererii utilizatorului.

Pentru ca dezvoltatorii să implementeze apelarea funcțiilor pentru agenți, vor avea nevoie de:

1. Un model LLM care suportă apelarea funcțiilor  
2. O schemă care conține descrieri funcțiilor  
3. Codul pentru fiecare funcție descrisă

Să folosim exemplul obținerii orei curente într-un oraș pentru a ilustra:

1. **Inițializarea unui LLM care suportă apelarea funcțiilor:**

    Nu toate modelele suportă apelarea funcțiilor, deci este important să verifici dacă LLM-ul pe care îl folosești o face. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> suportă apelarea funcțiilor. Putem începe prin inițierea clientului Azure OpenAI.

    ```python
    # Inițializează clientul Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **Crearea unei Scheme pentru Funcție:**

    Următorul pas este să definim o schemă JSON care conține numele funcției, descrierea a ceea ce face funcția și numele și descrierile parametrilor funcției. 
    Apoi vom lua această schemă și o vom trimite clientului creat anterior, împreună cu cererea utilizatorului de a afla ora în San Francisco. Ce este important de remarcat este că un **apel de unealtă** este ceea ce se returnează, **nu** răspunsul final la întrebare. După cum s-a menționat mai devreme, LLM-ul returnează numele funcției pe care a ales-o pentru sarcină și argumentele care vor fi transmise acesteia.

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
  
    # Prima apelare API: Solicitați modelului să utilizeze funcția
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Procesați răspunsul modelului
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
3. **Codul funcției necesar pentru realizarea sarcinii:**

    Acum că LLM a ales ce funcție trebuie rulată, codul care realizează sarcina trebuie implementat și executat.  
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
     # Gestionați apelurile funcției
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

Apelarea Funcțiilor este inima majorității, dacă nu a tuturor tiparelor de utilizare a uneltelor pentru agenți, însă implementarea ei de la zero poate fi uneori provocatoare.  
Așa cum am învățat în [Lecția 2](../../../02-explore-agentic-frameworks), cadrele agentice ne furnizează blocuri de construcție predefinite pentru a implementa utilizarea uneltelor.

## Exemple de Utilizare a Uneltelor cu Cadre Agentice

Iată câteva exemple de cum poți implementa Tiparul de Proiectare pentru Utilizarea Uneltelor folosind diferite cadre agentice:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> este un cadru open-source pentru construirea agenților AI. Simplifică procesul de utilizare a apelării funcțiilor permițându-ți să definești uneltele ca funcții Python cu decorarea `@tool`. Cadrul gestionează comunicarea dus-întors între model și codul tău. De asemenea, oferă acces la unelte predefinite cum sunt Căutarea de Fișiere și Interpretorul de Cod prin providerul `AzureAIProjectAgentProvider`.

Diagrama următoare ilustrează procesul apelării funcției cu Microsoft Agent Framework:

![apelarea funcției](../../../translated_images/ro/functioncalling-diagram.a84006fc287f6014.webp)

În Microsoft Agent Framework, uneltele sunt definite ca funcții decorate. Putem converti funcția `get_current_time` pe care am văzut-o mai devreme într-o unealtă folosind decorarea `@tool`. Cadrul va serializa automat funcția și parametrii săi, creând schema pentru a fi trimisă LLM-ului.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> este un cadru agentic mai nou, proiectat să permită dezvoltatorilor să construiască, să implementeze și să scaleze agenți AI de înaltă calitate și extensibili în mod securizat, fără a trebui să gestioneze resursele de calcul și stocare subiacente. Este deosebit de util pentru aplicații enterprise, fiind un serviciu complet gestionat cu securitate de nivel enterprise.

Comparativ cu dezvoltarea directă cu API-ul LLM, Azure AI Agent Service oferă unele avantaje, printre care:

- Apelare automată a uneltelor – nu mai este nevoie să parsezi un apel de unealtă, să invoci unealta și să gestionezi răspunsul; toate acestea se fac acum pe server  
- Date gestionate securizat – în loc să gestionezi propria stare a conversației, poți conta pe threads pentru a stoca toate informațiile necesare  
- Unelte out-of-the-box – unelte pe care le poți folosi pentru a interacționa cu sursele tale de date, cum ar fi Bing, Azure AI Search și Azure Functions.

Uneltele disponibile în Azure AI Agent Service pot fi împărțite în două categorii:

1. Unelte de Cunoaștere:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Împământare cu Bing Search</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Căutare de Fișiere</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Unelte de Acțiune:  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Apelarea Funcțiilor</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpretor de Cod</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Unelte definite OpenAPI</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service ne permite să folosim aceste unelte împreună ca un `toolset`. De asemenea, utilizează `threads` care țin evidența istoricului mesajelor dintr-o conversație anume.

Imaginează-ți că ești un agent de vânzări la o companie numită Contoso. Vrei să dezvolți un agent conversațional care să poată răspunde la întrebări despre datele tale de vânzări.

Imaginea următoare ilustrează cum ai putea folosi Azure AI Agent Service pentru a analiza datele tale de vânzări:

![Serviciul Agentic în Acțiune](../../../translated_images/ro/agent-service-in-action.34fb465c9a84659e.webp)

Pentru a folosi oricare dintre aceste unelte cu serviciul, putem crea un client și defini o unealtă sau un set de unelte. Pentru a implementa practic acest lucru, putem folosi următorul cod Python. LLM va putea să privească setul de unelte și să decidă dacă folosește funcția creată de utilizator, `fetch_sales_data_using_sqlite_query`, sau Interpretorul de Cod predefinit, în funcție de cererea utilizatorului.

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

# Inițializează setul de unelte
toolset = ToolSet()

# Inițializează agentul de apelare a funcțiilor cu funcția fetch_sales_data_using_sqlite_query și o adaugă la setul de unelte
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inițializează unealta Code Interpreter și o adaugă la setul de unelte.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Care sunt considerațiile speciale pentru utilizarea Tiparului de Proiectare pentru Utilizarea Uneltelor în construirea agenților AI de încredere?

O preocupare comună cu SQL generat dinamic de LLM-uri este securitatea, în special riscul de injecție SQL sau acțiuni malițioase, cum ar fi ștergerea sau manipularea bazei de date. Deși aceste preocupări sunt valide, ele pot fi gestionate eficient prin configurarea corectă a permisiunilor de acces la baza de date. Pentru majoritatea bazelor de date, acest lucru presupune configurarea bazei de date ca read-only. Pentru servicii de baze de date precum PostgreSQL sau Azure SQL, aplicația ar trebui să aibă un rol read-only (SELECT).

Executarea aplicației într-un mediu securizat sporește și mai mult protecția. În scenarii enterprise, datele sunt de obicei extrase și transformate din sistemele operaționale într-o bază de date read-only sau depozit de date cu un schelet prietenos pentru utilizator. Această abordare asigură că datele sunt securizate, optimizate pentru performanță și accesibilitate, iar aplicația are acces restricționat, read-only.

## Exemple de Cod

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Ai Mai Multe Întrebări despre Tiparele de Proiectare pentru Utilizarea Uneltelor?

Alătură-te [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la ore de consultații și a-ți primi răspunsurile la întrebările despre Agenți AI.

## Resurse Suplimentare

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Atelier Azure AI Agents Service</a>  
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Atelier Multi-Agent Contoso Creative Writer</a>  
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Prezentare Microsoft Agent Framework</a>

## Lecția Anterioară

[Înțelegerea Tiparelor de Proiectare Agentice](../03-agentic-design-patterns/README.md)

## Lecția Următoare
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->