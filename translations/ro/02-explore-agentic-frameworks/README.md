[![Explorarea cadrelor pentru agenți AI](../../../translated_images/ro/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Explorați cadrele pentru agenți AI

Cadrele pentru agenți AI sunt platforme software proiectate pentru a simplifica crearea, implementarea și gestionarea agenților AI. Aceste cadre oferă dezvoltatorilor componente preconstruite, abstracții și instrumente care accelerează dezvoltarea sistemelor AI complexe.

Aceste cadre îi ajută pe dezvoltatori să se concentreze pe aspectele unice ale aplicațiilor lor, oferind abordări standardizate pentru provocările comune din dezvoltarea agenților AI. Ele îmbunătățesc scalabilitatea, accesibilitatea și eficiența în construirea sistemelor AI.

## Introducere 

Această lecție va acoperi:

- Ce sunt cadrele pentru agenți AI și ce le permit dezvoltatorilor să realizeze?
- Cum pot echipele să folosească aceste cadre pentru a prototipa rapid, itera și îmbunătăți capabilitățile agenților lor?
- Care sunt diferențele între cadrele și instrumentele create de Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> și <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Pot integra direct instrumentele mele existente din ecosistemul Azure sau am nevoie de soluții independente?
- Ce este Microsoft Foundry Agent Service și cum mă ajută acesta?

## Obiective de învățare

Obiectivele acestei lecții sunt să vă ajute să înțelegeți:

- Rolul cadrelor pentru agenți AI în dezvoltarea AI.
- Cum să valorificați cadrele pentru agenți AI pentru a construi agenți inteligenți.
- Capabilitățile cheie oferite de cadrele pentru agenți AI.
- Diferențele între Microsoft Agent Framework și Microsoft Foundry Agent Service.

## Ce sunt cadrele pentru agenți AI și ce le permit dezvoltatorilor să facă?

Cadrele AI tradiționale vă pot ajuta să integrați AI în aplicațiile dvs. și să le faceți mai bune în următoarele moduri:

- **Personalizare**: AI poate analiza comportamentul și preferințele utilizatorilor pentru a oferi recomandări personalizate, conținut și experiențe.
Exemplu: Serviciile de streaming precum Netflix folosesc AI pentru a sugera filme și emisiuni bazate pe istoricul vizionărilor, sporind implicarea și satisfacția utilizatorilor.
- **Automatizare și eficiență**: AI poate automatiza sarcinile repetitive, simplifica fluxurile de lucru și îmbunătăți eficiența operațională.
Exemplu: Aplicațiile pentru asistență clienți folosesc chatboți alimentați de AI pentru a răspunde întrebărilor comune, reducând timpul de răspuns și eliberând agenții umani pentru probleme mai complexe.
- **Experiență îmbunătățită a utilizatorului**: AI poate îmbunătăți experiența generală a utilizatorului oferind funcții inteligente precum recunoașterea vocală, procesarea limbajului natural și text predictiv.
Exemplu: Asistenții virtuali precum Siri și Google Assistant folosesc AI pentru a înțelege și răspunde comenzilor vocale, facilitând interacțiunea utilizatorilor cu dispozitivele lor.

### Toate acestea sună grozav, nu-i așa? Deci de ce avem nevoie de cadrul pentru agenți AI?

Cadrele pentru agenți AI reprezintă ceva mai mult decât simple cadre AI. Ele sunt proiectate pentru a permite crearea de agenți inteligenți care pot interacționa cu utilizatorii, alți agenți și mediul înconjurător pentru a atinge obiective specifice. Acești agenți pot manifesta un comportament autonom, pot lua decizii și se pot adapta la condițiile în schimbare. Să vedem câteva capabilități cheie oferite de cadrele pentru agenți AI:

- **Colaborarea și coordonarea agenților**: Permit crearea mai multor agenți AI care pot lucra împreună, comunica și colabora pentru a rezolva sarcini complexe.
- **Automatizarea și gestionarea sarcinilor**: Oferă mecanisme pentru automatizarea fluxurilor multi-pas, delegarea sarcinilor și gestionarea dinamică a sarcinilor între agenți.
- **Înțelegerea contextuală și adaptarea**: Echiparea agenților cu abilitatea de a înțelege contextul, a se adapta la medii în schimbare și a lua decizii bazate pe informații în timp real.

Pe scurt, agenții vă permit să faceți mai mult, să duceți automatizarea la nivelul următor, să creați sisteme mai inteligente care pot învăța și se pot adapta mediului lor.

## Cum să prototipăm rapid, să iterăm și să îmbunătățim capabilitățile agentului?

Este un domeniu în mișcare rapidă, dar există câteva elemente comune în majoritatea cadrelor pentru agenți AI care pot ajuta la prototiparea și iterarea rapidă, și anume componente modulare, instrumente colaborative și învățare în timp real. Să le explorăm:

- **Folosiți componente modulare**: SDK-urile AI oferă componente preconstruite precum conectori AI și de memorie, apelarea de funcții prin limbaj natural sau pluginuri de cod, șabloane de prompt și altele.
- **Valorificați instrumentele colaborative**: Proiectați agenți cu roluri și sarcini specifice, permițând testarea și rafinarea fluxurilor de lucru colaborative.
- **Învățați în timp real**: Implementați bucle de feedback unde agenții învață din interacțiuni și își ajustează comportamentul dinamic.

### Folosiți componente modulare

SDK-uri precum Microsoft Agent Framework oferă componente preconstruite, cum ar fi conectori AI, definiții de instrumente și gestionarea agenților.

**Cum pot folosi echipele acestea**: Echipele pot combina rapid aceste componente pentru a crea un prototip funcțional fără a începe de la zero, ceea ce permite experimentarea și iterarea rapidă.

**Cum funcționează în practică**: Puteți folosi un parser preconstruit pentru extragerea informațiilor din intrarea utilizatorului, un modul de memorie pentru stocare și accesarea datelor și un generator de prompt pentru interacțiunea cu utilizatorii, toate fără a construi aceste componente de la zero.

**Exemplu de cod**. Să vedem un exemplu despre cum puteți folosi Microsoft Agent Framework cu `FoundryChatClient` pentru ca modelul să răspundă la input-ul utilizatorului folosind apelarea de instrumente:

``` python
# Exemplu Python pentru Microsoft Agent Framework

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definirea unei funcții de instrument exemplu pentru rezervarea călătoriei
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Exemplu de rezultat: Zborul dvs. către New York din 1 ianuarie 2025 a fost rezervat cu succes. Călătorie plăcută! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Ce puteți observa din acest exemplu este cum puteți valorifica un parser preconstruit pentru extragerea informațiilor cheie din input-ul utilizatorului, cum ar fi originea, destinația și data unei cereri de rezervare zbor. Această abordare modulară vă permite să vă concentrați pe logica de nivel înalt.

### Valorificați instrumentele colaborative

Cadre precum Microsoft Agent Framework facilitează crearea mai multor agenți care pot lucra împreună.

**Cum pot folosi echipele acestea**: Echipele pot proiecta agenți cu roluri și sarcini specifice, permițând testarea și rafinarea fluxurilor colaborative și îmbunătățirea eficienței generale a sistemului.

**Cum funcționează în practică**: Puteți crea o echipă de agenți, fiecare cu o funcție specializată, cum ar fi preluarea datelor, analiza sau luarea deciziilor. Acești agenți pot comunica și pot împărtăși informații pentru a atinge un obiectiv comun, cum ar fi răspunsul la o întrebare a utilizatorului sau finalizarea unei sarcini.

**Exemplu de cod (Microsoft Agent Framework)**:

```python
# Crearea mai multor agenți care lucrează împreună folosind Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Agent de preluare a datelor
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent de analiză a datelor
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Rularea agenților în secvență pe o sarcină
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Ce vedeți în codul anterior este modul în care puteți crea o sarcină ce implică mai mulți agenți care colaborează pentru a analiza date. Fiecare agent îndeplinește o funcție specifică, iar sarcina este executată prin coordonarea agenților pentru a obține rezultatul dorit. Prin crearea unor agenți dedicați cu roluri specializate, puteți îmbunătăți eficiența și performanța sarcinilor.

### Învățați în timp real

Cadrele avansate oferă capabilități pentru înțelegerea contextuală și adaptarea în timp real.

**Cum pot folosi echipele acestea**: Echipele pot implementa bucle de feedback în care agenții învață din interacțiuni și își ajustează comportamentul dinamic, ducând la îmbunătățirea continuă și rafinarea capabilităților.

**Cum funcționează în practică**: Agenții pot analiza feedback-ul utilizatorilor, datele de mediu și rezultatele sarcinilor pentru a-și actualiza baza de cunoștințe, a ajusta algoritmii de luare a deciziilor și a-și îmbunătăți performanța în timp. Acest proces iterativ de învățare le permite agenților să se adapteze la condiții și preferințe ale utilizatorilor în schimbare, sporind eficacitatea generală a sistemului.

## Care sunt diferențele dintre Microsoft Agent Framework și Microsoft Foundry Agent Service?

Există multe modalități de a compara aceste abordări, dar să vedem câteva diferențe cheie în ceea ce privește designul, capabilitățile și cazurile de utilizare vizate:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework oferă un SDK simplificat pentru construirea agenților AI folosind `FoundryChatClient`. Permite dezvoltatorilor să creeze agenți care valorifică modelele Azure OpenAI cu apelare de instrumente încorporată, gestionarea conversațiilor și securitate de nivel enterprise prin identitatea Azure.

**Cazuri de utilizare**: Construirea de agenți AI pregătiți pentru producție cu utilizarea instrumentelor, fluxuri multi-pas și scenarii de integrare enterprise.

Iată câteva concepte esențiale importante în Microsoft Agent Framework:

- **Agenți**. Un agent este creat prin `FoundryChatClient` și configurat cu un nume, instrucțiuni și instrumente. Agentul poate:
  - **Procesa mesajele utilizatorului** și genera răspunsuri folosind modelele Azure OpenAI.
  - **Apela automat instrumente** pe baza contextului conversației.
  - **Menține starea conversației** pe parcursul mai multor interacțiuni.

  Iată un fragment de cod care arată cum să creați un agent:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Instrumente**. cadrul suportă definirea instrumentelor ca funcții Python pe care agentul le poate invoca automat. Instrumentele se înregistrează când se creează agentul:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Coordonare multi-agenți**. Puteți crea mai mulți agenți cu specializări diferite și coordona munca lor:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Integrare identitate Azure**. cadrul folosește `AzureCliCredential` (sau `DefaultAzureCredential`) pentru autentificare securizată, fără chei, eliminând necesitatea gestionării directe a cheilor API.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service este o componentă mai recentă, lansată la Microsoft Ignite 2024. Permite dezvoltarea și implementarea agenților AI cu modele mai flexibile, cum ar fi apelarea directă a LLM-urilor open-source precum Llama 3, Mistral și Cohere.

Microsoft Foundry Agent Service oferă mecanisme mai puternice de securitate enterprise și metode de stocare a datelor, fiind potrivit pentru aplicații enterprise.

Funcționează fără efort împreună cu Microsoft Agent Framework pentru construirea și implementarea agenților.

Acest serviciu este în prezent în Public Preview și suportă Python și C# pentru construirea agenților.

Folosind SDK-ul Python Microsoft Foundry Agent Service, putem crea un agent cu un instrument definit de utilizator:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Define funcții pentru unelte
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Concepte de bază

Microsoft Foundry Agent Service are următoarele concepte de bază:

- **Agent**. Microsoft Foundry Agent Service se integrează cu Microsoft Foundry. În cadrul Microsoft Foundry, un agent AI acționează ca un microserviciu „inteligent” care poate răspunde la întrebări (RAG), efectua acțiuni sau automatiza complet fluxurile de lucru. Acest lucru se realizează prin combinarea puterii modelelor AI generative cu instrumente care îi permit să acceseze și să interacționeze cu surse de date din lumea reală. Iată un exemplu de agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    În acest exemplu, un agent este creat cu modelul `gpt-4o-mini`, numele `my-agent` și instrucțiunile `You are helpful agent`. Agentul este echipat cu instrumente și resurse pentru a realiza sarcini de interpretare a codului.

- **Fire și mesaje**. Firul este un concept important. Reprezintă o conversație sau o interacțiune între agent și utilizator. Firele pot fi folosite pentru a urmări progresul unei conversații, pentru a stoca informații contextuale și a gestiona starea interacțiunii. Iată un exemplu de fir:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Cere agentului să efectueze munca pe fir
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Preia și înregistrează toate mesajele pentru a vedea răspunsul agentului
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    În codul anterior, un fir este creat. Ulterior, se trimite un mesaj către fir. Prin apelarea lui `create_and_process_run`, agentul este solicitat să realizeze o sarcină pe fir. În cele din urmă, mesajele sunt recuperate și înregistrate pentru a vedea răspunsul agentului. Mesajele indică progresul conversației între utilizator și agent. De asemenea, este important să înțelegem că mesajele pot fi de diferite tipuri, cum ar fi text, imagine sau fișier, adică rezultatul muncii agenților a fost, de exemplu, o imagine sau un răspuns text. Ca dezvoltator, puteți folosi apoi aceste informații pentru a procesa mai departe răspunsul sau pentru a-l prezenta utilizatorului.

- **Integrarea cu Microsoft Agent Framework**. Microsoft Foundry Agent Service funcționează perfect cu Microsoft Agent Framework, ceea ce înseamnă că puteți construi agenți folosind `FoundryChatClient` și să îi implementați prin intermediul Agent Service pentru scenarii de producție.

**Cazuri de utilizare**: Microsoft Foundry Agent Service este conceput pentru aplicații enterprise care necesită implementare de agenți AI securizată, scalabilă și flexibilă.

## Care este diferența dintre aceste abordări?
 
Pare că există suprapuneri, dar există câteva diferențe cheie în ceea ce privește designul, capabilitățile și cazurile de utilizare țintă:
 
- **Microsoft Agent Framework (MAF)**: Este un SDK pregătit pentru producție pentru construirea agenților AI. Oferă o API simplificată pentru crearea agenților cu apelare de instrumente, gestionarea conversațiilor și integrarea identității Azure.
- **Microsoft Foundry Agent Service**: Este o platformă și un serviciu de implementare în Microsoft Foundry pentru agenți. Oferă conectivitate încorporată la servicii precum Azure OpenAI, Azure AI Search, Bing Search și execuție de cod.
 
Nu sunteți încă sigur ce să alegeți?

### Cazuri de utilizare
 
Să vedem dacă putem să vă ajutăm parcurgând câteva cazuri comune de utilizare:
 
> Î: Construiesc aplicații AI de producție și vreau să încep rapid
>

>R: Microsoft Agent Framework este o alegere excelentă. Oferă o API simplă, pythonică prin `FoundryChatClient` care vă permite să definiți agenți cu instrumente și instrucțiuni în doar câteva linii de cod.

>Î: Am nevoie de implementare de nivel enterprise cu integrări Azure precum Search și execuția de cod
>
> R: Microsoft Foundry Agent Service este cea mai bună alegere. Este un serviciu de platformă care oferă capabilități încorporate pentru multiple modele, Azure AI Search, Bing Search și Azure Functions. Face ușor să vă construiți agenții în Foundry Portal și să îi implementați la scară.
 
> Î: Sunt încă confuz, dă-mi doar o opțiune
>
> R: Începeți cu Microsoft Agent Framework pentru a vă construi agenții, apoi folosiți Microsoft Foundry Agent Service când aveți nevoie să îi implementați și să îi scalați în producție. Această abordare vă permite să iterați rapid pe logica agentului dvs., având în același timp un drum clar pentru implementarea enterprise.
 
Să rezumăm diferențele cheie într-un tabel:

| Cadru | Focus | Concepte de bază | Cazuri de utilizare |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK agent simplificat cu apelare de instrumente | Agenți, Instrumente, Identitate Azure | Construirea agenților AI, utilizarea instrumentelor, fluxuri multi-pas |
| Microsoft Foundry Agent Service | Modele flexibile, securitate enterprise, generare cod, apelare instrumente | Modularitate, Colaborare, Orchestrarea proceselor | Implementarea securizată, scalabilă și flexibilă a agenților AI |

## Pot integra direct instrumentele mele existente din ecosistemul Azure sau am nevoie de soluții independente?


Răspunsul este da, poți integra instrumentele tale existente din ecosistemul Azure direct cu Microsoft Foundry Agent Service, mai ales că a fost construit pentru a funcționa perfect cu alte servicii Azure. De exemplu, ai putea integra Bing, Azure AI Search și Azure Functions. Există, de asemenea, o integrare profundă cu Microsoft Foundry.

Microsoft Agent Framework se integrează, de asemenea, cu serviciile Azure prin `FoundryChatClient` și identitatea Azure, permițându-ți să apelezi serviciile Azure direct din instrumentele agentului tău.

## Coduri Exemplu

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Mai ai întrebări despre AI Agent Frameworks?

Alătură-te [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la ore de consultații și a primi răspunsuri la întrebările tale despre agenți AI.

## Referințe

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Lecția Anterioară

[Introducere în Agenți AI și Cazuri de Utilizare a Agenților](../01-intro-to-ai-agents/README.md)

## Lecția Următoare

[Înțelegerea Tiparelor de Proiectare Agentică](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->