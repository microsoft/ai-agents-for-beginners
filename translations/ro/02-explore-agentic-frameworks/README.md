[![Explorarea cadrelor de agent AI](../../../translated_images/ro/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Faceți clic pe imaginea de mai sus pentru a vizualiza videoclipul acestei lecții)_

# Explorați cadrele de agenți AI

Cadrele de agenți AI sunt platforme software proiectate pentru a simplifica crearea, implementarea și gestionarea agenților AI. Aceste cadre oferă dezvoltatorilor componente preconstruite, abstracții și instrumente care eficientizează dezvoltarea sistemelor AI complexe.

Aceste cadre ajută dezvoltatorii să se concentreze pe aspectele unice ale aplicațiilor lor oferind abordări standardizate pentru provocările comune în dezvoltarea agenților AI. Ele îmbunătățesc scalabilitatea, accesibilitatea și eficiența în construcția sistemelor AI.

## Introducere

Această lecție va acoperi:

- Ce sunt cadrele de agenți AI și ce le permit dezvoltatorilor să realizeze?
- Cum pot echipele să utilizeze aceste cadre pentru a prototipa rapid, itera și îmbunătăți capabilitățile agentului lor?
- Care sunt diferențele dintre cadrele și instrumentele create de Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> și <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Pot integra direct instrumentele mele existente din ecosistemul Azure sau am nevoie de soluții independente?
- Ce este Microsoft Foundry Agent Service și cum mă ajută acesta?

## Obiective de învățare

Obiectivele acestei lecții sunt să vă ajute să înțelegeți:

- Rolul cadrelor de agenți AI în dezvoltarea AI.
- Cum să valorificați cadrele de agenți AI pentru a construi agenți inteligenți.
- Capabilitățile cheie activate de cadrele de agenți AI.
- Diferențele dintre Microsoft Agent Framework și Microsoft Foundry Agent Service.

## Ce sunt cadrele de agenți AI și ce le permit dezvoltatorilor să facă?

Cadrele AI tradiționale vă pot ajuta să integrați AI în aplicațiile dvs. și să faceți aceste aplicații mai bune în următoarele moduri:

- **Personalizare**: AI poate analiza comportamentul și preferințele utilizatorului pentru a oferi recomandări, conținut și experiențe personalizate.
Exemplu: Serviciile de streaming precum Netflix folosesc AI pentru a sugera filme și emisiuni pe baza istoricului de vizionare, sporind angajamentul și satisfacția utilizatorilor.
- **Automatizare și Eficiență**: AI poate automatiza sarcinile repetitive, optimiza fluxurile de lucru și îmbunătăți eficiența operațională.
Exemplu: Aplicațiile de servicii pentru clienți folosesc chatboți alimentați de AI pentru a gestiona întrebările comune, reducând timpii de răspuns și eliberând agenții umani pentru probleme mai complexe.
- **Experiență îmbunătățită a utilizatorului**: AI poate îmbunătăți experiența generală a utilizatorului prin oferirea de funcționalități inteligente precum recunoașterea vocală, procesarea limbajului natural și text predictiv.
Exemplu: Asistenții virtuali precum Siri și Google Assistant folosesc AI pentru a înțelege și răspunde la comenzi vocale, facilitând interacțiunea utilizatorilor cu dispozitivele lor.

### Sună bine, nu-i așa? Atunci de ce avem nevoie de cadru de agenți AI?

Cadrele de agenți AI reprezintă ceva mai mult decât simple cadre AI. Ele sunt proiectate să permită crearea de agenți inteligenți care pot interacționa cu utilizatorii, alți agenți și cu mediul pentru a atinge obiective specifice. Acești agenți pot manifesta comportament autonom, pot lua decizii și se pot adapta la condiții în schimbare. Să vedem câteva capabilități cheie activate de cadrele de agenți AI:

- **Colaborarea și coordonarea agenților**: Permite crearea mai multor agenți AI care pot lucra împreună, comunica și coordona pentru a rezolva sarcini complexe.
- **Automatizarea și gestionarea sarcinilor**: Oferă mecanisme pentru automatizarea fluxurilor de lucru multi-pas, delegarea sarcinilor și gestionarea dinamică a sarcinilor între agenți.
- **Înțelegerea și adaptarea contextuală**: Echiparea agenților cu abilitatea de a înțelege contextul, de a se adapta la medii schimbătoare și de a lua decizii pe baza informațiilor în timp real.

Pe scurt, agenții vă permit să faceți mai mult, să duceți automatizarea la nivelul următor, să creați sisteme mai inteligente care pot învăța și adapta din mediul înconjurător.

## Cum să prototipați rapid, să iterați și să îmbunătățiți capabilitățile agentului?

Aceasta este o piață în mișcare rapidă, dar există câteva aspecte comune în majoritatea cadrelor de agenți AI care vă pot ajuta să prototipați rapid și să iterați, și anume componente modulare, instrumente colaborative și învățare în timp real. Să explorăm acestea:

- **Folosiți componente modulare**: SDK-urile AI oferă componente preconstruite precum conectori AI și de memorie, apelarea funcțiilor folosind limbaj natural sau plugin-uri de cod, șabloane de prompturi și altele.
- **Valorificați instrumentele colaborative**: Proiectați agenți cu roluri și sarcini specifice, permițându-le să testeze și să rafineze fluxuri de lucru colaborative.
- **Învățați în timp real**: Implementați bucle de feedback în care agenții învață din interacțiuni și își ajustează comportamentul dinamic.

### Folosiți componente modulare

SDK-uri precum Microsoft Agent Framework oferă componente preconstruite precum conectori AI, definiții de instrumente și gestionarea agenților.

**Cum pot echipele să le folosească**: Echipele pot asambla rapid aceste componente pentru a crea un prototip funcțional fără a începe de la zero, permițând experimentare rapidă și iterație.

**Cum funcționează în practică**: Puteți folosi un parser preconstruit pentru a extrage informații din input-ul utilizatorului, un modul de memorie pentru a stoca și recupera date și un generator de prompturi pentru interacțiunea cu utilizatorii, toate fără a construi aceste componente de la zero.

**Cod exemplu**. Să vedem un exemplu de cum puteți folosi Microsoft Agent Framework cu `FoundryChatClient` pentru a face modelul să răspundă la input-ul utilizatorului cu apelare de instrumente:

``` python
# Exemplu Microsoft Agent Framework în Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definește o funcție exemplu pentru rezervarea călătoriilor
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
    # Exemplu de rezultat: Zborul tău către New York pe 1 ianuarie 2025 a fost rezervat cu succes. Călătorie plăcută! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Din acest exemplu puteți observa cum puteți valorifica un parser preconstruit pentru a extrage informații cheie din input-ul utilizatorului, precum originea, destinația și data unei cereri de rezervare zbor. Această abordare modulară vă permite să vă concentrați pe logica de nivel înalt.

### Valorificați instrumentele colaborative

Cadre precum Microsoft Agent Framework facilitează crearea mai multor agenți care pot lucra împreună.

**Cum pot echipele să le folosească**: Echipele pot proiecta agenți cu roluri și sarcini specifice, permitând testarea și rafinarea fluxurilor de lucru colaborative și îmbunătățirea eficienței sistemului în ansamblu.

**Cum funcționează în practică**: Puteți crea o echipă de agenți unde fiecare agent are o funcție specializată, cum ar fi recuperarea datelor, analiza sau luarea deciziilor. Acești agenți pot comunica și partaja informații pentru a atinge un scop comun, cum ar fi răspunsul la o întrebare a utilizatorului sau îndeplinirea unei sarcini.

**Cod exemplu (Microsoft Agent Framework)**:

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

# Agent pentru preluarea datelor
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent pentru analiza datelor
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Rularea agenților în secvență pentru o sarcină
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Ce vedeți în codul precedent este cum puteți crea o sarcină care implică mai mulți agenți care lucrează împreună pentru a analiza date. Fiecare agent îndeplinește o funcție specifică, iar sarcina este executată prin coordonarea agenților pentru a atinge rezultatul dorit. Prin crearea de agenți dedicați cu roluri specializate, puteți îmbunătăți eficiența și performanța sarcinii.

### Învățați în timp real

Cadrele avansate oferă capacități pentru înțelegerea contextului și adaptarea în timp real.

**Cum pot echipele să le folosească**: Echipele pot implementa bucle de feedback în care agenții învață din interacțiuni și își ajustează comportamentul dinamic, ducând la îmbunătățire continuă și rafinare a capabilităților.

**Cum funcționează în practică**: Agenții pot analiza feedback-ul utilizatorilor, date de mediu și rezultatele sarcinilor pentru a-și actualiza baza de cunoștințe, a ajusta algoritmii de luare a deciziilor și a îmbunătăți performanța în timp. Acest proces iterativ de învățare permite agenților să se adapteze la condiții și preferințe în schimbare ale utilizatorilor, sporind eficacitatea generală a sistemului.

## Care sunt diferențele dintre Microsoft Agent Framework și Microsoft Foundry Agent Service?

Există multe moduri de a compara aceste abordări, dar să vedem câteva diferențe cheie în termeni de design, capabilități și cazuri de utilizare targetate:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework oferă un SDK simplificat pentru construirea agenților AI folosind `FoundryChatClient`. Permite dezvoltatorilor să creeze agenți care valorifică modelele Azure OpenAI cu apelare încorporată de instrumente, gestionarea conversațiilor și securitate la nivel enterprise prin identitate Azure.

**Cazuri de utilizare**: Construirea de agenți AI gata pentru producție cu utilizarea de instrumente, fluxuri de lucru multi-pas și scenarii de integrare enterprise.

Iată câteva concepte de bază importante ale Microsoft Agent Framework:

- **Agenți**. Un agent este creat prin `FoundryChatClient` și configurat cu un nume, instrucțiuni și instrumente. Agentul poate:
  - **Procesa mesajele utilizatorului** și genera răspunsuri folosind modelele Azure OpenAI.
  - **Apela instrumente** automat în funcție de contextul conversației.
  - **Menține starea conversației** pe durata mai multor interacțiuni.

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

- **Instrumente**. cadrul suportă definirea instrumentelor ca funcții Python pe care agentul le poate invoca automat. Instrumentele sunt înregistrate la crearea agentului:

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

- **Coordonarea multi-agent**. Puteți crea mai mulți agenți cu specializări diferite și coordona munca lor:

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

- **Integrarea Azure Identity**. cadrul folosește `AzureCliCredential` (sau `DefaultAzureCredential`) pentru autentificare securizată fără gestionarea cheilor, eliminând necesitatea de a administra direct chei API.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service este o adiție mai recentă, introdusă la Microsoft Ignite 2024. Permite dezvoltarea și implementarea agenților AI cu modele mai flexibile, cum ar fi apelarea directă a LLM-urilor open-source precum Llama 3, Mistral și Cohere.

Microsoft Foundry Agent Service oferă mecanisme mai puternice de securitate enterprise și metode de stocare a datelor, făcându-l potrivit pentru aplicații enterprise.

Funcționează out-of-the-box cu Microsoft Agent Framework pentru construcția și implementarea agenților.

Acest serviciu este momentan în Public Preview și suportă Python și C# pentru construirea agenților.

Folosind SDK-ul Python Microsoft Foundry Agent Service, putem crea un agent cu un instrument definit de utilizator:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Define funcțiile instrumentului
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
        model="gpt-5-mini",
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

- **Agent**. Microsoft Foundry Agent Service se integrează cu Microsoft Foundry. În Microsoft Foundry, un agent AI acționează ca un microserviciu „inteligent” care poate fi folosit pentru a răspunde la întrebări (RAG), a executa acțiuni sau a automatiza complet fluxuri de lucru. Realizează asta combinând puterea modelelor AI generative cu instrumente care îi permit să acceseze și să interacționeze cu surse reale de date. Iată un exemplu de agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    În acest exemplu, un agent este creat cu modelul `gpt-5-mini`, numele `my-agent` și instrucțiunile `You are helpful agent`. Agentul este echipat cu instrumente și resurse pentru a efectua sarcini de interpretare de cod.

- **Fir și mesaje**. Firul este un alt concept important. Reprezintă o conversație sau interacțiune între un agent și un utilizator. Firele pot fi folosite pentru a urmări progresul unei conversații, stoca informații contextuale și gestiona starea interacțiunii. Iată un exemplu de fir:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Cere agentului să efectueze lucru pe fir
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Preia și înregistrează toate mesajele pentru a vedea răspunsul agentului
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    În codul anterior, un fir este creat. Apoi, un mesaj este trimis către fir. Prin apelarea `create_and_process_run`, agentului i se solicită să efectueze o lucrare pe fir. În final, mesajele sunt preluate și înregistrate pentru a vedea răspunsul agentului. Mesajele indică progresul conversației între utilizator și agent. Este important de înțeles că mesajele pot fi de tipuri diferite, cum ar fi text, imagine sau fișier, adică munca agenților a generat, de exemplu, o imagine sau un răspuns text. Ca dezvoltator, puteți folosi aceste informații pentru a procesa mai departe răspunsul sau a-l prezenta utilizatorului.

- **Integrare cu Microsoft Agent Framework**. Microsoft Foundry Agent Service funcționează perfect cu Microsoft Agent Framework, ceea ce înseamnă că puteți construi agenți folosind `FoundryChatClient` și să îi implementați prin Agent Service pentru scenarii de producție.

**Cazuri de utilizare**: Microsoft Foundry Agent Service este proiectat pentru aplicații enterprise care necesită implementare sigură, scalabilă și flexibilă a agenților AI.

## Care este diferența între aceste abordări?
 
Pare că există suprapuneri, dar sunt diferențe cheie între ele în termeni de design, capabilități și cazuri țintă:
 
- **Microsoft Agent Framework (MAF)**: Este un SDK gata de producție pentru construirea agenților AI. Oferă o API simplificată pentru crearea agenților cu apelare de instrumente, gestionarea conversațiilor și integrare cu identitatea Azure.
- **Microsoft Foundry Agent Service**: Este o platformă și un serviciu de implementare în Microsoft Foundry pentru agenți. Oferă conectivitate încorporată cu servicii precum Azure OpenAI, Azure AI Search, Bing Search și executarea de cod.
 
Încă nu sunteți sigur pe care să o alegeți?

### Cazuri de utilizare
 
Să vedem dacă vă putem ajuta parcurgând câteva cazuri comune:
 
> Î: Construiesc aplicații de agenți AI pentru producție și vreau să încep rapid
>

>R: Microsoft Agent Framework este o alegere excelentă. Oferă o API simplă, Pythonică prin `FoundryChatClient` care vă permite să definiți agenți cu instrumente și instrucțiuni în doar câteva linii de cod.

>Î: Am nevoie de implementare enterprise cu integrări Azure precum Search și executare cod
>
> R: Microsoft Foundry Agent Service este cea mai potrivită. Este un serviciu de platformă care oferă capabilități încorporate pentru mai multe modele, Azure AI Search, Bing Search și Azure Functions. Facilitează construirea agenților dvs. în Foundry Portal și implementarea lor la scară.
 
> Î: Încă sunt confuz, dați-mi o singură opțiune
>
> R: Începeți cu Microsoft Agent Framework pentru a vă construi agenții, apoi folosiți Microsoft Foundry Agent Service când trebuie să îi implementați și scalați în producție. Această abordare vă permite să iterați rapid asupra logicii agentului în timp ce aveți o cale clară către implementarea enterprise.
 
Să sumarizăm diferențele cheie într-un tabel:

| Cadru | Focus | Concepte de bază | Cazuri de utilizare |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK simplificat pentru agenți cu apelare de instrumente | Agenți, Instrumente, Identitate Azure | Construirea de agenți AI, utilizarea instrumentelor, fluxuri de lucru multi-pas |
| Microsoft Foundry Agent Service | Modele flexibile, securitate enterprise, generare cod, apelare instrumente | Modularitate, Colaborare, Orchestrarea proceselor | Implementare sigură, scalabilă și flexibilă a agenților AI |

## Pot integra direct instrumentele mele existente din ecosistemul Azure sau am nevoie de soluții independente?


Răspunsul este da, puteți integra instrumentele existente din ecosistemul Azure direct cu Serviciul Microsoft Foundry Agent, în special deoarece acesta a fost construit pentru a funcționa perfect cu alte servicii Azure. De exemplu, ați putea integra Bing, Azure AI Search și Azure Functions. Există, de asemenea, o integrare profundă cu Microsoft Foundry.

Framework-ul Microsoft Agent se integrează de asemenea cu serviciile Azure prin `FoundryChatClient` și identitatea Azure, permițându-vă să apelați serviciile Azure direct din instrumentele agentului dvs.

## Exemple de cod

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Ai mai multe întrebări despre AI Agent Frameworks?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la ore de birou și a primi răspunsuri la întrebările despre AI Agents.

## Referințe

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Lecția Anterioară

[Introducere în AI Agents și cazuri de utilizare a agentului](../01-intro-to-ai-agents/README.md)

## Lecția Următoare

[Înțelegerea pattern-urilor de design agentic](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->