[![Cum să proiectezi agenți AI buni](../../../translated_images/ro/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Dă click pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Tiparul de proiectare Tool Use

Instrumentele sunt interesante deoarece permit agenților AI să aibă o gamă mai largă de capabilități. În loc ca agentul să aibă un set limitat de acțiuni pe care le poate efectua, prin adăugarea unui instrument, agentul poate acum să realizeze o gamă largă de acțiuni. În acest capitol, vom analiza Tiparul de proiectare Tool Use, care descrie cum agenții AI pot folosi instrumente specifice pentru a-și atinge obiectivele.

## Introducere

În această lecție, căutăm să răspundem la următoarele întrebări:

- Ce este tiparul de proiectare Tool Use?
- Pentru ce cazuri de utilizare poate fi aplicat?
- Care sunt elementele/blocurile componente necesare pentru a implementa acest tipar de proiectare?
- Care sunt considerațiile speciale pentru folosirea Tiparului de proiectare Tool Use în construirea agenților AI de încredere?

## Obiective de învățare

După finalizarea acestei lecții, vei putea:

- Defini Tiparul de proiectare Tool Use și scopul său.
- Identifica cazuri de utilizare unde Tiparul de proiectare Tool Use este aplicabil.
- Înțelege elementele cheie necesare pentru implementarea tiparului de proiectare.
- Recunoaște considerațiile pentru asigurarea încrederii în agenții AI care folosesc acest tipar de proiectare.

## Ce este Tiparul de proiectare Tool Use?

**Tiparul de proiectare Tool Use** se concentrează pe oferirea modelelor de limbaj mari (LLM) a capacității de a interacționa cu instrumente externe pentru a atinge obiective specifice. Instrumentele sunt cod care poate fi executat de un agent pentru a efectua acțiuni. Un instrument poate fi o funcție simplă, precum un calculator, sau un apel API către un serviciu terț, precum verificarea prețurilor acțiunilor sau prognoza meteo. În contextul agenților AI, instrumentele sunt concepute să fie executate de agenți ca răspuns la **apeluri de funcții generate de model**.

## Pentru ce cazuri de utilizare poate fi aplicat?

Agenții AI pot valorifica instrumentele pentru a finaliza sarcini complexe, a recupera informații sau a lua decizii. Tiparul de proiectare Tool Use este adesea folosit în scenarii ce necesită interacțiune dinamică cu sisteme externe, cum ar fi baze de date, servicii web sau interpretoare de cod. Această capacitate este utilă pentru o serie de cazuri de utilizare diferite, inclusiv:

- **Recuperare dinamică a informațiilor:** Agenții pot interoga API-uri externe sau baze de date pentru a obține date actualizate (de exemplu, interogarea unei baze de date SQLite pentru analiză de date, obținerea prețurilor acțiunilor sau informațiilor meteorologice).
- **Executarea și interpretarea codului:** Agenții pot executa cod sau scripturi pentru a rezolva probleme matematice, a genera rapoarte sau a realiza simulări.
- **Automatizarea fluxurilor de lucru:** Automatizarea proceselor repetitive sau cu mai mulți pași prin integrarea instrumentelor precum programatori de sarcini, servicii de email sau pipeline-uri de date.
- **Suport pentru clienți:** Agenții pot interacționa cu sisteme CRM, platforme de ticketing sau baze de cunoștințe pentru a soluționa întrebările utilizatorilor.
- **Generare și editare de conținut:** Agenții pot folosi instrumente precum verificatoare gramaticale, rezumatori de text sau evaluatori de siguranță a conținutului pentru a ajuta la sarcini de creare de conținut.

## Care sunt elementele/blocurile componente necesare pentru implementarea tiparului de proiectare Tool Use?

Aceste blocuri componente permit agentului AI să realizeze o gamă largă de sarcini. Să analizăm elementele cheie necesare pentru implementarea Tiparului de proiectare Tool Use:

- **Scheme pentru Funcții/Instrumente**: Definiții detaliate ale instrumentelor disponibile, incluzând numele funcției, scopul, parametrii necesari și rezultatele așteptate. Aceste scheme permit LLM-ului să înțeleagă ce instrumente sunt disponibile și cum să construiască cereri valide.

- **Logica de execuție a funcțiilor**: Guvernează modul și momentul în care instrumentele sunt invocate, pe baza intenției utilizatorului și contextului conversației. Aceasta poate include module de planificare, mecanisme de rutare sau fluxuri condiționale care determină utilizarea dinamică a instrumentelor.

- **Sistemul de gestionare a mesajelor**: Componente care gestionează fluxul conversațional între intrările utilizatorului, răspunsurile LLM, apelurile către instrumente și ieșirile instrumentelor.

- **Cadru de integrare a instrumentelor**: Infrastructura care conectează agentul la diverse instrumente, fie că sunt funcții simple sau servicii externe complexe.

- **Gestionarea erorilor & Validare**: Mecanisme pentru a gestiona eșecurile în execuția instrumentelor, a valida parametrii și a gestiona răspunsuri neașteptate.

- **Gestionarea stării**: Monitorizează contextul conversației, interacțiunile anterioare cu instrumentele și datele persistente pentru a asigura consistența în interacțiunile multi-turn.

Următorul pas este să analizăm apelarea Funcțiilor/Instrumentelor în mai mult detaliu.
 
### Apelarea Funcțiilor/Instrumentelor

Apelarea funcțiilor este principalul mod prin care permitem modelelor mari de limbaj (LLM) să interacționeze cu instrumentele. Vei vedea adesea „Funcția” și „Instrumentul” folosite interschimbabil, deoarece „funcțiile” (blocuri de cod reutilizabil) sunt „instrumentele” pe care agenții le folosesc pentru a îndeplini sarcini. Pentru ca un cod al funcției să fie invocat, un LLM trebuie să compare cererea utilizatorului cu descrierea funcțiilor. Pentru asta se trimite către LLM o schemă ce conține descrierile tuturor funcțiilor disponibile. LLM-ul selectează apoi funcția cea mai potrivită pentru sarcină și returnează numele și argumentele acesteia. Funcția selectată este invocată, iar răspunsul său este trimis înapoi către LLM, care folosește informația pentru a răspunde cererii utilizatorului.

Pentru ca dezvoltatorii să implementeze apelarea funcțiilor pentru agenți, vei avea nevoie de:

1. Un model LLM care suportă apelarea funcțiilor
2. O schemă care conține descrierile funcțiilor
3. Codul pentru fiecare funcție descrisă

Să folosim exemplul obținerii orei curente într-un oraș pentru a ilustra:

1. **Inițializează un LLM care suportă apelarea funcțiilor:**

    Nu toate modelele suportă apelarea funcțiilor, deci este important să verifici dacă LLM-ul folosit o face. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> suportă apelarea funcțiilor. Putem începe prin a iniția clientul OpenAI împotriva API-ului Azure OpenAI **Responses** (endpoint-ul stabil `/openai/v1/` — nu este nevoie de `api_version`). 

    ```python
    # Inițializează clientul OpenAI pentru Azure OpenAI (API răspunsuri, endpoint v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Creează o Scheme pentru Funcție**:

    Mai departe vom defini o schemă JSON care conține numele funcției, descrierea a ceea ce face funcția și numele și descrierile parametrilor funcției.
    Vom transmite această schemă clientului creat anterior, împreună cu cererea utilizatorului de a afla ora în San Francisco. Ce este important de remarcat este că se returnează un **apel de instrument**, **nu** răspunsul final la întrebare. După cum am menționat anterior, LLM-ul returnează numele funcției selectate pentru sarcină și argumentele care vor fi transmise acesteia.

    ```python
    # Descrierea funcției pentru ca modelul să o poată citi (format API Răspunsuri, unealtă plată)
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

    # Prima apelare API: Cere modelului să folosească funcția
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # API-ul de Răspunsuri întoarce apeluri de instrumente ca elemente function_call în response.output.
    # Adaugă-le la conversație astfel încât modelul să aibă context complet la următorul pas.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Codul funcției necesar pentru a efectua sarcina:**

    Acum că LLM-ul a ales care funcție trebuie rulată, codul care îndeplinește sarcina trebuie implementat și executat.
    Putem implementa codul pentru a obține ora curentă în Python. De asemenea, vom avea nevoie să scriem codul pentru a extrage numele și argumentele din response_message pentru a obține rezultatul final.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Returnați rezultatul instrumentului ca un element function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Al doilea apel API: Obțineți răspunsul final de la model
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

Apelarea Funcțiilor este în centrul majorității, dacă nu tuturor implementărilor de utilizare a instrumentelor de către agenți, însă implementarea de la zero poate fi uneori dificilă.
Așa cum am învățat în [Lecția 2](../../../02-explore-agentic-frameworks), cadrele agentice ne oferă blocuri componente predefinite pentru implementarea utilizării instrumentelor.
 
## Exemple de utilizare a instrumentelor cu cadre agentice

Iată câteva exemple despre cum poți implementa Tiparul de proiectare Tool Use folosind cadre agentice diferite:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> este un cadru open-source pentru construirea agenților AI. Simplifică procesul de folosire a apelării funcțiilor permițându-ți să definești instrumente ca funcții Python cu decoratorul `@tool`. Cadrul gestionează comunicarea între model și codul tău. De asemenea, oferă acces la instrumente predefinite precum File Search și Code Interpreter prin `FoundryChatClient`.

Diagrama următoare ilustrează procesul de apelare a funcțiilor cu Microsoft Agent Framework:

![apelarea funcțiilor](../../../translated_images/ro/functioncalling-diagram.a84006fc287f6014.webp)

În Microsoft Agent Framework, instrumentele sunt definite ca funcții decorate. Putem transforma funcția `get_current_time` pe care am văzut-o mai devreme într-un instrument folosind decoratorul `@tool`. Cadrul va serializa automat funcția și parametrii ei, creând schema pentru a fi trimisă către LLM.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> este un cadru agentic mai nou, conceput pentru a permite dezvoltatorilor să creeze, să lanseze și să scaleze în mod sigur agenți AI de înaltă calitate și extensibili, fără a fi nevoie să gestioneze resursele de calcul și stocare subiacente. Este deosebit de util pentru aplicații enterprise, fiind un serviciu complet gestionat cu securitate la nivel enterprise.

Comparativ cu dezvoltarea cu API-ul LLM direct, Microsoft Foundry Agent Service oferă câteva avantaje, inclusiv:

- Apelarea automată a instrumentelor – nu este nevoie să analizezi un apel de instrument, să invoci instrumentul și să gestionezi răspunsul; toate acestea se fac acum pe server
- Date gestionate în mod securizat – în loc să gestionezi propriul context conversațional, poți folosi thread-uri pentru a stoca toate informațiile necesare
- Instrumente gata de utilizare – Instrumente cu care poți interacționa cu sursele tale de date, cum ar fi Bing, Azure AI Search și Azure Functions.

Instrumentele disponibile în Microsoft Foundry Agent Service pot fi împărțite în două categorii:

1. Instrumente de cunoaștere:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Sustentarea cu Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Căutare de fișiere</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Instrumente de acțiune:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Apelarea funcțiilor</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpreter de cod</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Instrumente definite OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Funcții Azure</a>

Serviciul Agent ne permite să folosim aceste instrumente împreună ca un `toolset`. De asemenea, utilizează `threads` care urmăresc istoricul mesajelor dintr-o conversație particulară.

Imaginează-ți că ești un agent de vânzări la o companie numită Contoso. Vrei să dezvolți un agent conversațional care să poată răspunde la întrebări despre datele tale de vânzări.

Imaginea următoare ilustrează cum ai putea folosi Microsoft Foundry Agent Service pentru a analiza datele tale de vânzări:

![Serviciul Agent în Acțiune](../../../translated_images/ro/agent-service-in-action.34fb465c9a84659e.webp)

Pentru a folosi oricare dintre aceste instrumente cu serviciul, putem crea un client și defini un instrument sau un toolset. Pentru a implementa aceasta în mod practic putem folosi următorul cod Python. LLM-ul va putea examina toolset-ul și decide dacă folosește funcția creată de utilizator, `fetch_sales_data_using_sqlite_query`, sau Interpreterul de Cod predefinit în funcție de cererea utilizatorului.

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

# Inițializează agentul de apelare a funcțiilor cu funcția fetch_sales_data_using_sqlite_query și o adaugă în setul de unelte
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inițializează uneltele Code Interpreter și le adaugă în setul de unelte.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Care sunt considerațiile speciale pentru folosirea Tiparului de proiectare Tool Use în construirea agenților AI de încredere?

O preocupare comună legată de SQL-ul generat dinamic de LLM-uri este securitatea, în special riscul de injecție SQL sau acțiuni malițioase, cum ar fi ștergerea sau modificarea bazei de date. Deși aceste preocupări sunt valide, ele pot fi gestionate eficient prin configurarea corectă a permisiunilor de acces la bază de date. Pentru majoritatea bazelor de date, aceasta implică configurarea bazei de date în mod read-only. Pentru servicii de baze de date precum PostgreSQL sau Azure SQL, aplicația trebuie să fie atribuită unui rol read-only (SELECT).

Rularea aplicației într-un mediu securizat crește și mai mult protecția. În scenarii enterprise, datele sunt de obicei extrase și transformate din sistemele operaționale într-o bază de date read-only sau depozit de date cu o schemă ușor accesibilă. Această abordare asigură că datele sunt securizate, optimizate pentru performanță și accesibilitate, iar aplicația are acces restricționat, doar read-only.

## Coduri exemplu

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Ai mai multe întrebări despre Tiparele de proiectare Tool Use?

Alătură-te [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la ore de consultanță și a primi răspunsuri la întrebările despre Agenți AI.

## Resurse suplimentare

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Multi-Agent Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Prezentare generală Microsoft Agent Framework</a>


## Testare rapidă a acestui agent (Opțional)

După ce înveți să implementezi agenți în [Lecția 16](../16-deploying-scalable-agents/README.md), poți testa rapid `TravelToolAgent` din această lecție (apelează încă uneltele sale și răspunde?) cu [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Vezi [`tests/README.md`](../tests/README.md) pentru instrucțiuni despre cum să îl rulezi.

## Lecția anterioară

[Înțelegerea modelelor de design agentic](../03-agentic-design-patterns/README.md)

## Lecția următoare

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->