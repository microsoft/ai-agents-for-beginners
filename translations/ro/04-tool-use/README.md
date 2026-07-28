[![Cum să Proiectezi Agenți AI Buni](../../../translated_images/ro/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Tiparul de Proiectare pentru Utilizarea Instrumentelor

Instrumentele sunt interesante pentru că permit agenților AI să aibă un spectru mai larg de capabilități. În loc ca agentul să aibă un set limitat de acțiuni pe care le poate efectua, prin adăugarea unui instrument, agentul poate acum să execute o gamă largă de acțiuni. În acest capitol, vom analiza Tiparul de Proiectare pentru Utilizarea Instrumentelor, care descrie cum agenții AI pot folosi instrumente specifice pentru a-și atinge scopurile.

## Introducere

În această lecție, ne propunem să răspundem la următoarele întrebări:

- Ce este tiparul de proiectare pentru utilizarea instrumentelor?
- Pentru ce cazuri de utilizare poate fi aplicat?
- Care sunt elementele/blocurile de construcție necesare pentru implementarea tiparului de proiectare?
- Care sunt considerațiile speciale pentru utilizarea Tiparului de Proiectare pentru Utilizarea Instrumentelor în construirea agenților AI de încredere?

## Obiective de Învățare

După finalizarea acestei lecții, vei putea:

- Să definești Tiparul de Proiectare pentru Utilizarea Instrumentelor și scopul său.
- Să identifici cazuri de utilizare unde Tiparul de Proiectare pentru Utilizarea Instrumentelor este aplicabil.
- Să înțelegi elementele cheie necesare pentru implementarea tiparului de proiectare.
- Să recunoști considerațiile pentru asigurarea încrederii în agenții AI care folosesc acest tipar de proiectare.

## Ce este Tiparul de Proiectare pentru Utilizarea Instrumentelor?

**Tiparul de Proiectare pentru Utilizarea Instrumentelor** se concentrează pe oferirea modelelor mari de limbaj (LLM) a capacității de a interacționa cu instrumente externe pentru a atinge scopuri specifice. Instrumentele sunt cod care poate fi executat de un agent pentru a realiza acțiuni. Un instrument poate fi o funcție simplă, cum ar fi un calculator, sau un apel API către un serviciu terț, cum ar fi căutarea prețului acțiunilor sau prognoza meteo. În contextul agenților AI, instrumentele sunt proiectate să fie executate de agenți ca răspuns la **apeluri de funcții generate de model**.

## Pentru ce cazuri de utilizare poate fi aplicat?

Agenții AI pot utiliza instrumente pentru a finaliza sarcini complexe, pentru a obține informații sau pentru a lua decizii. Tiparul de utilizare a instrumentelor este folosit frecvent în scenarii care necesită interacțiune dinamică cu sisteme externe, cum ar fi baze de date, servicii web sau interpretoare de cod. Această abilitate este utilă pentru o serie de cazuri de utilizare, inclusiv:

- **Recuperare Dinamică a Informațiilor:** Agenții pot interoga API-uri externe sau baze de date pentru a obține date actualizate (ex: interogarea unei baze de date SQLite pentru analiza datelor, obținerea prețurilor acțiunilor sau informații meteo).
- **Executare și Interpretare de Cod:** Agenții pot executa cod sau scripturi pentru a rezolva probleme matematice, pentru a genera rapoarte sau pentru a efectua simulări.
- **Automatizarea Fluxurilor de Lucru:** Automatizarea fluxurilor repetitive sau cu mai mulți pași prin integrarea unor instrumente precum programatoare de sarcini, servicii de email sau conducte de date.
- **Suport Clienți:** Agenții pot interacționa cu sisteme CRM, platforme de ticketing sau baze de cunoștințe pentru a rezolva întrebările utilizatorilor.
- **Generare și Editare de Conținut:** Agenții pot folosi instrumente precum verificatoare gramaticale, rezumatori de text sau evaluatori de siguranță a conținutului pentru a asista în sarcini de creare a conținutului.

## Care sunt elementele/blocurile necesare pentru implementarea tiparului de utilizare a instrumentelor?

Aceste blocuri de construcție permit agentului AI să execute o gamă largă de sarcini. Să analizăm elementele cheie necesare pentru implementarea Tiparului de Proiectare pentru Utilizarea Instrumentelor:

- **Scheme de Funcții/Instrumente**: Definiții detaliate ale instrumentelor disponibile, incluzând numele funcției, scopul, parametrii necesari și rezultatele așteptate. Aceste scheme permit LLM-ului să înțeleagă ce instrumente sunt disponibile și cum să construiască cereri valide.

- **Logica de Executare a Funcțiilor**: Guvernează modul și momentul în care instrumentele sunt invocate, pe baza intenției utilizatorului și contextului conversației. Poate include module de planificare, mecanisme de rutare sau fluxuri condiționale care determină utilizarea instrumentelor dinamic.

- **Sistem de Gestionare a Mesajelor**: Componente care gestionează fluxul conversației între input-urile utilizatorului, răspunsurile LLM, apelurile instrumentelor și rezultatele acestora.

- **Cadru de Integrare a Instrumentelor**: Infrastructură care conectează agentul la diverse instrumente, fie că sunt funcții simple sau servicii externe complexe.

- **Gestionarea Erorilor și Validare**: Mecanisme pentru a gestiona eșecurile în execuția instrumentelor, validarea parametrilor și gestionarea răspunsurilor neașteptate.

- **Gestionarea Stării**: Urmărește contextul conversației, interacțiunile anterioare cu instrumentele și date persistente pentru a asigura consistența în interacțiuni cu mai mulți pași.

Următorul pas este să analizăm în detaliu Apelarea Funcțiilor/Instrumentelor.
 
### Apelarea Funcțiilor/Instrumentelor

Apelarea funcțiilor este metoda principală prin care permităm modelelor mari de limbaj (LLM) să interacționeze cu instrumentele. Vei vedea adesea termenii „Funcție” și „Instrument” folosiți interschimbabil pentru că „funcțiile” (blocuri reutilizabile de cod) sunt „instrumentele” pe care agenții le folosesc pentru a realiza sarcini. Pentru ca codul unei funcții să fie invocat, un LLM trebuie să compare solicitarea utilizatorului cu descrierea funcțiilor. Pentru aceasta, se trimite către LLM o schemă care conține descrierile tuturor funcțiilor disponibile. LLM selectează funcția cea mai potrivită pentru sarcină și returnează numele său și argumentele. Funcția selectată este invocată, răspunsul său este trimis înapoi la LLM, care folosește informația pentru a răspunde solicitării utilizatorului.

Pentru dezvoltatori care doresc să implementeze apelarea funcțiilor pentru agenți, veți avea nevoie:

1. Un model LLM care suportă apelarea funcțiilor
2. O schemă care conține descrierile funcțiilor
3. Codul pentru fiecare funcție descrisă

Să folosim exemplul obținerii orei curente într-un oraș pentru a ilustra:

1. **Inițializează un LLM care suportă apelarea funcțiilor:**

    Nu toate modelele suportă apelarea funcțiilor, așa că este important să verifici dacă LLM-ul pe care îl folosești are această funcționalitate. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> suportă apelarea funcțiilor. Putem începe prin inițierea clientului OpenAI pentru Azure OpenAI **Responses API** (endpoint-ul stabil `/openai/v1/` — nu este nevoie de `api_version`).

    ```python
    # Initializează clientul OpenAI pentru Azure OpenAI (API Răspunsuri, endpoint v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Creează o Schematizare a Funcției**:

    Apoi vom defini o schemă JSON care conține numele funcției, o descriere a ceea ce face funcția și numele și descrierile parametrilor funcției.
    Vom transmite această schemă clientului creat anterior, împreună cu solicitarea utilizatorului de a afla ora în San Francisco. Este important de notat că se returnează un **apel la instrument**, **nu** răspunsul final la întrebare. După cum am menționat anterior, LLM returnează numele funcției pe care a selectat-o pentru sarcină și argumentele care vor fi transmise acesteia.

    ```python
    # Descrierea funcției pentru ca modelul să o citească (formatul instrumentului Responses API flat)
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
  
    # Mesajul inițial al utilizatorului
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Prima apelare API: Cere modelului să utilizeze funcția
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # API-ul de răspunsuri returnează apeluri către uneltele ca elemente function_call în response.output.
    # Adaugă-le conversației pentru ca modelul să aibă context complet la următoarea interacțiune.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Codul funcției necesar pentru a realiza sarcina:**

    Acum că LLM a ales ce funcție trebuie rulată, codul care execută sarcina trebuie implementat și executat.
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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Returnează rezultatul instrumentului ca un element function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Al doilea apel API: Obține răspunsul final de la model
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

Apelarea funcțiilor este în inima majorității, dacă nu a tuturor, proiectărilor de utilizare a instrumentelor pentru agenți, însă implementarea sa de la zero poate fi uneori provocatoare.
După cum am învățat în [Lecția 2](../../../02-explore-agentic-frameworks), cadrele agentice ne oferă blocuri de construcție predefinite pentru implementarea utilizării instrumentelor.
 
## Exemple de Utilizare a Instrumentelor cu Cadre Agentice

Iată câteva exemple despre cum poți implementa Tiparul de Proiectare pentru Utilizarea Instrumentelor folosind diferite cadre agentice:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> este un cadru AI open-source pentru construirea agenților AI. Simplifică procesul de utilizare a apelării funcțiilor prin permiterea de a defini instrumente ca funcții Python decorate cu `@tool`. Cadrul gestionează comunicarea dus-întors între model și codul tău. De asemenea, oferă acces la instrumente predefinite precum Căutarea de Fișiere și Interpretatorul de Cod prin `FoundryChatClient`.

Diagrama următoare ilustrează procesul de apelare a funcțiilor cu Microsoft Agent Framework:

![apelarea funcțiilor](../../../translated_images/ro/functioncalling-diagram.a84006fc287f6014.webp)

În Microsoft Agent Framework, instrumentele sunt definite ca funcții decorate. Putem converti funcția `get_current_time` pe care am văzut-o mai devreme într-un instrument folosind decoratorul `@tool`. Cadrul va serializa automat funcția și parametrii acesteia, creând schema pentru a fi trimisă către LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Creează clientul
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Creează un agent și rulează cu instrumentul
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> este un cadru agentic mai nou, proiectat să permită dezvoltatorilor să construiască, să implementeze și să scaleze în mod securizat agenți AI de înaltă calitate și extensibili, fără a fi nevoie să gestioneze resursele de calcul și stocare subiacente. Este util în special pentru aplicații enterprise deoarece este un serviciu complet gestionat, cu securitate de nivel enterprise.

Comparativ cu dezvoltarea directă cu API-ul LLM, Microsoft Foundry Agent Service oferă câteva avantaje, inclusiv:

- Apelarea automată a instrumentelor – nu este nevoie să analizezi un apel la instrument, să invoci instrumentul și să gestionezi răspunsul; toate acestea se fac server-side
- Gestionarea securizată a datelor – în loc să gestionezi starea conversației proprii, poți folosi fire pentru a stoca toată informația necesară
- Instrumente gata de utilizare – instrumente cu care poți interacționa cu sursele tale de date, precum Bing, Azure AI Search și Azure Functions.

Instrumentele disponibile în Microsoft Foundry Agent Service pot fi împărțite în două categorii:

1. Instrumente de Cunoaștere:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Fundamentare cu Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Căutare de Fișiere</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Instrumente de Acțiune:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Apelarea Funcțiilor</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpretator de Cod</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Instrumente definite prin OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Serviciul Agent ne permite să folosim aceste instrumente împreună într-un `toolset`. De asemenea, utilizează `threads` care țin evidența istoricului mesajelor dintr-o conversație particulară.

Imaginează-ți că ești agent de vânzări într-o companie numită Contoso. Vrei să dezvolți un agent conversațional care să poată răspunde întrebărilor despre datele tale de vânzări.

Imaginea următoare ilustrează cum ai putea folosi Microsoft Foundry Agent Service pentru a analiza datele de vânzări:

![Serviciul Agentic în Acțiune](../../../translated_images/ro/agent-service-in-action.34fb465c9a84659e.webp)

Pentru a folosi oricare dintre aceste instrumente cu serviciul, putem crea un client și defini un instrument sau un toolset. Pentru a implementa practic putem folosi codul Python de mai jos. LLM va putea analiza toolsetul și decide dacă folosește funcția creată de utilizator, `fetch_sales_data_using_sqlite_query`, sau Interpretatorul de Cod predefinit în funcție de solicitarea utilizatorului.

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

# Inițializare set de unelte
toolset = ToolSet()

# Inițializare agent de apelare funcții cu funcția fetch_sales_data_using_sqlite_query și adăugarea acesteia în setul de unelte
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inițializare unealtă Interpreter Cod și adăugarea acesteia în setul de unelte.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Care sunt considerațiile speciale pentru utilizarea Tiparului de Proiectare pentru Utilizarea Instrumentelor în construirea agenților AI de încredere?

O preocupare comună legată de SQL-ul generat dinamic de LLM-uri este securitatea, în special riscul de injecție SQL sau acțiuni malițioase, precum ștergerea sau manipularea bazei de date. Deși aceste preocupări sunt valide, ele pot fi atenuate eficient prin configurarea corespunzătoare a permisiunilor de acces la bază de date. Pentru majoritatea bazelor de date aceasta presupune configurarea bazei în mod read-only. Pentru servicii de baze de date precum PostgreSQL sau Azure SQL, aplicația trebuie să aibă un rol read-only (SELECT).

Rularea aplicației într-un mediu securizat sporește această protecție. În scenariile enterprise, datele sunt, de obicei, extrase și transformate din sistemele operaționale într-o bază de date read-only sau într-un depozit de date cu schemă prietenoasă utilizatorului. Această abordare asigură că datele sunt securizate, optimizate pentru performanță și accesibilitate, iar aplicația are un acces restricționat, doar pentru citire.

## Coduri Exemplu

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Ai Mai Multe Întrebări despre Tiparele de Proiectare pentru Utilizarea Instrumentelor?

Alătură-te [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a cunoaște alți cursanți, a participa la sesiuni de tip „office hours” și pentru a primi răspunsuri la întrebările tale legate de Agenții AI.

## Resurse Suplimentare

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Prezentare Generală Microsoft Agent Framework</a>


## Testare rapidă a acestui agent (Opțional)

După ce înveți să implementezi agenți în [Lecția 16](../16-deploying-scalable-agents/README.md), poți testa rapid `TravelToolAgent` din această lecție (mai apelează instrumentele și răspunde?) folosind [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Vezi [`tests/README.md`](../tests/README.md) pentru instrucțiuni de rulare.

## Lecția Anterioară

[Înțelegerea modelelor de design agentic](../03-agentic-design-patterns/README.md)

## Lecția Următoare

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->