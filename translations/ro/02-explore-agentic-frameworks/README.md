[![Exploring AI Agent Frameworks](../../../translated_images/ro/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Explorează Framework-urile pentru Agenți AI

Framework-urile pentru agenți AI sunt platforme software concepute pentru a simplifica crearea, implementarea și gestionarea agenților AI. Aceste framework-uri oferă dezvoltatorilor componente pre-construite, abstracții și instrumente care eficientizează dezvoltarea sistemelor AI complexe.

Aceste framework-uri ajută dezvoltatorii să se concentreze pe aspectele unice ale aplicațiilor lor prin furnizarea de abordări standardizate pentru provocările comune în dezvoltarea agenților AI. Ele îmbunătățesc scalabilitatea, accesibilitatea și eficiența în construirea sistemelor AI.

## Introducere 

Această lecție va acoperi:

- Ce sunt Framework-urile pentru Agenți AI și ce pot realiza dezvoltatorii cu ele?
- Cum pot echipele să folosească aceste framework-uri pentru a prototipa rapid, itera și îmbunătăți capacitățile agentului lor?
- Care sunt diferențele dintre framework-urile și instrumentele create de Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> și <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Pot integra direct instrumentele existente din ecosistemul Azure sau am nevoie de soluții independente?
- Ce este Microsoft Foundry Agent Service și cum mă ajută?

## Obiectivele lecției

Obiectivele acestei lecții sunt să vă ajute să înțelegeți:

- Rolul Framework-urilor pentru Agenți AI în dezvoltarea AI.
- Cum să valorificați Framework-urile pentru Agenți AI pentru a construi agenți inteligenți.
- Capacitățile cheie oferite de Framework-urile pentru Agenți AI.
- Diferențele dintre Microsoft Agent Framework și Microsoft Foundry Agent Service.

## Ce sunt Framework-urile pentru Agenți AI și ce permit dezvoltatorilor să facă?

Framework-urile AI tradiționale vă pot ajuta să integrați AI în aplicațiile dvs. și să le îmbunătățiți în următoarele moduri:

- **Personalizare**: AI poate analiza comportamentul utilizatorului și preferințele pentru a oferi recomandări, conținut și experiențe personalizate.
Exemplu: Serviciile de streaming precum Netflix folosesc AI pentru a sugera filme și seriale pe baza istoricului de vizionare, sporind implicarea și satisfacția utilizatorului.
- **Automatizare și Eficiență**: AI poate automatiza sarcinile repetitive, eficientiza fluxurile de lucru și îmbunătăți eficiența operațională.
Exemplu: Aplicațiile pentru servicii clienți folosesc chatboți powered by AI pentru a gestiona solicitările comune, reducând timpii de răspuns și eliberând agenții umani pentru probleme mai complexe.
- **Îmbunătățirea Experienței Utilizatorului**: AI poate îmbunătăți experiența generală oferind funcții inteligente precum recunoașterea vocală, procesarea limbajului natural și text predictiv.
Exemplu: Asistenții virtuali precum Siri și Google Assistant folosesc AI pentru a înțelege și răspunde la comenzi vocale, facilitând interacțiunea utilizatorilor cu dispozitivele lor.

### Sună bine, nu-i așa? Atunci de ce avem nevoie de Framework-ul pentru Agenți AI?

Framework-urile pentru Agenți AI reprezintă ceva mai mult decât simple framework-uri AI. Ele sunt concepute pentru a permite crearea de agenți inteligenți care pot interacționa cu utilizatorii, alți agenți și mediul înconjurător pentru a atinge scopuri specifice. Acești agenți pot manifesta comportament autonom, pot lua decizii și se pot adapta la condiții în schimbare. Să vedem câteva capacități cheie oferite de Framework-urile pentru Agenți AI:

- **Colaborarea și coordonarea agenților**: Permit crearea mai multor agenți AI care pot lucra împreună, comunica și coordona pentru a rezolva sarcini complexe.
- **Automatizarea și gestionarea sarcinilor**: Oferă mecanisme pentru automatizarea fluxurilor de lucru în mai mulți pași, delegarea sarcinilor și gestionarea dinamică a acestora între agenți.
- **Înțelegerea contextului și adaptarea**: Echiparea agenților cu abilitatea de a înțelege contextul, de a se adapta la medii în schimbare și de a lua decizii bazate pe informații în timp real.

Pe scurt, agenții vă permit să faceți mai mult, să duceți automatizarea la un nivel superior, să creați sisteme inteligente care se pot adapta și învăța din mediu.

## Cum să prototipăm rapid, să iterăm și să îmbunătățim capacitățile agentului?

Acesta este un domeniu în continuă evoluție, dar există câteva elemente comune în majoritatea Framework-urilor pentru Agenți AI care vă pot ajuta să prototipați rapid și să iterați, anume componente modulare, unelte colaborative și învățare în timp real. Să le analizăm:

- **Folosiți componente modulare**: SDK-urile AI oferă componente pre-construite, cum ar fi conectori AI și de memorie, apelarea funcțiilor folosind limbaj natural sau pluginuri de cod, șabloane de prompturi și altele.
- **Valorificați uneltele colaborative**: Proiectați agenți cu roluri și sarcini specifice, permițând testarea și rafinarea fluxurilor colaborative.
- **Învățați în timp real**: Implementați bucle de feedback prin care agenții învață din interacțiuni și își ajustează comportamentul dinamic.

### Folosiți Componente Modulare

SDK-uri precum Microsoft Agent Framework oferă componente pre-construite precum conectori AI, definiții de instrumente și gestionarea agenților.

**Cum pot echipele să le folosească**: Echipele pot asambla rapid aceste componente pentru a crea un prototip funcțional fără să înceapă de la zero, permițând experimentare și iterație rapidă.

**Cum funcționează în practică**: Puteți folosi un parser pre-construit pentru a extrage informații din input-ul utilizatorului, un modul de memorie pentru stocare și recuperare date și un generator de prompturi pentru interacțiunea cu utilizatorii, toate fără a construi aceste componente de la zero.

**Exemplu de cod**. Să vedem un exemplu despre cum puteți folosi Microsoft Agent Framework cu `FoundryChatClient` pentru ca modelul să răspundă input-ului utilizatorului apelând un instrument:

``` python
# Exemplu Microsoft Agent Framework în Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definirea unei funcții exemplu pentru rezervarea călătoriilor
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
    # Exemplu de ieșire: Zborul dumneavoastră către New York, în data de 1 ianuarie 2025, a fost rezervat cu succes. Călătorie plăcută! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Ce puteți observa din acest exemplu este cum puteți valorifica un parser pre-construit pentru a extrage informații cheie din input-ul utilizatorului, cum ar fi originea, destinația și data unei solicitări de rezervare zbor. Această abordare modulară vă permite să vă concentrați pe logica de nivel înalt.

### Valorificați Uneltele Colaborative

Framework-uri precum Microsoft Agent Framework facilitează crearea mai multor agenți care pot lucra împreună.

**Cum pot echipele să le folosească**: Echipele pot proiecta agenți cu roluri și sarcini specifice, permițând testarea și rafinarea fluxurilor de lucru colaborative și îmbunătățirea eficienței sistemului.

**Cum funcționează în practică**: Puteți crea o echipă de agenți în care fiecare agent are o funcție specializată, cum ar fi recuperarea datelor, analiza sau luarea deciziilor. Acești agenți pot comunica și împărți informații pentru a atinge un scop comun, cum ar fi răspunsul la o întrebare a utilizatorului sau realizarea unei sarcini.

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

# Executarea agenților în succesiune pe o sarcină
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Ce vedeți în codul anterior este cum puteți crea o sarcină ce implică mai mulți agenți care lucrează împreună pentru a analiza date. Fiecare agent realizează o funcție specifică, iar sarcina este executată prin coordonarea agenților pentru a atinge rezultatul dorit. Prin crearea de agenți dedicați cu roluri specializate, puteți îmbunătăți eficiența și performanța sarcinilor.

### Învățați în Timp Real

Framework-urile avansate oferă capacități pentru înțelegerea contextului și adaptarea în timp real.

**Cum pot echipele să le folosească**: Echipele pot implementa bucle de feedback în care agenții învață din interacțiuni și își ajustează dinamica comportamentul, ducând la îmbunătățiri continue și rafinarea capacităților.

**Cum funcționează în practică**: Agenții pot analiza feedback-ul utilizatorului, datele mediului și rezultatele sarcinilor pentru a-și actualiza baza de cunoștințe, a ajusta algoritmii de luare a deciziilor și a îmbunătăți performanța în timp. Acest proces iterativ de învățare permite agenților să se adapteze la condiții în schimbare și preferințe ale utilizatorilor, sporind eficacitatea generală a sistemului.

## Care sunt diferențele dintre Microsoft Agent Framework și Microsoft Foundry Agent Service?

Există multe moduri de a compara aceste abordări, dar să vedem câteva diferențe cheie în termeni de design, capacități și cazuri țintă de utilizare:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework oferă un SDK simplificat pentru construirea agenților AI folosind `FoundryChatClient`. Permite dezvoltatorilor să creeze agenți care valorifică modelele Azure OpenAI cu apelare de instrumente integrată, gestionarea conversațiilor și securitate de nivel enterprise prin identitatea Azure.

**Cazuri de utilizare**: Construirea de agenți AI gata de producție cu folosire de instrumente, fluxuri multi-pas și scenarii de integrare enterprise.

Iată câteva concepte de bază importante ale Microsoft Agent Framework:

- **Agenți**. Un agent este creat prin `FoundryChatClient` și configurat cu nume, instrucțiuni și instrumente. Agentul poate:
  - **Procesează mesajele utilizatorului** și generează răspunsuri folosind modelele Azure OpenAI.
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

- **Instrumente**. Framework-ul permite definirea instrumentelor ca funcții Python pe care agentul le poate invoca automat. Instrumentele sunt înregistrate la crearea agentului:

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

- **Coordonarea Multi-Agent**. Puteți crea mai mulți agenți cu specializări diferite și coordona activitatea lor:

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

- **Integrarea identității Azure**. Framework-ul folosește `AzureCliCredential` (sau `DefaultAzureCredential`) pentru autentificare securizată, fără chei, eliminând necesitatea gestionării directe a cheilor API.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service este o adiție mai recentă, introdusă la Microsoft Ignite 2024. Permite dezvoltarea și implementarea agenților AI cu modele mai flexibile, cum ar fi apelarea directă a LLM open-source precum Llama 3, Mistral și Cohere.

Microsoft Foundry Agent Service oferă mecanisme mai puternice de securitate enterprise și metode de stocare a datelor, fiind potrivit pentru aplicații enterprise.

Funcționează imediat cu Microsoft Agent Framework pentru construirea și implementarea agenților.

Acest serviciu este în prezent în Public Preview și suportă Python și C# pentru construirea de agenți.

Utilizând SDK-ul Python Microsoft Foundry Agent Service, putem crea un agent cu un instrument definit de utilizator:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Define funcții pentru instrumente
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
        model="gpt-4.1-mini",
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

Microsoft Foundry Agent Service are următoarele concepte cheie:

- **Agent**. Microsoft Foundry Agent Service se integrează cu Microsoft Foundry. În Microsoft Foundry, un Agent AI acționează ca un microserviciu „inteligent” care poate fi folosit pentru a răspunde la întrebări (RAG), a efectua acțiuni sau a automatiza complet fluxuri de lucru. Realizează acest lucru combinând puterea modelelor AI generative cu instrumente care îi permit accesul și interacțiunea cu surse de date reale. Iată un exemplu de agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    În acest exemplu, un agent este creat cu modelul `gpt-4.1-mini`, numele `my-agent` și instrucțiunile `You are helpful agent`. Agentul este echipat cu instrumente și resurse pentru a efectua sarcini de interpretare a codului.

- **Fir de discuție și mesaje**. Firul de discuție este un alt concept important. Reprezintă o conversație sau interacțiune între un agent și un utilizator. Firele de discuție pot fi folosite pentru a urmări progresul unei conversații, a stoca informații contextuale și a gestiona starea interacțiunii. Iată un exemplu de fir de discuție:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Cere agentului să efectueze lucrul pe fir
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Preia și înregistrează toate mesajele pentru a vedea răspunsul agentului
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    În codul precedent, un fir de discuție este creat. Apoi, un mesaj este trimis la fir. Apelând `create_and_process_run`, agentului i se cere să efectueze o lucrare pe fir. În final, mesajele sunt preluate și înregistrate pentru a vedea răspunsul agentului. Mesajele indică progresul conversației dintre utilizator și agent. De asemenea, este important de înțeles că mesajele pot fi de tipuri diferite, cum ar fi text, imagine sau fișier, ceea ce înseamnă că munca agenților a generat, de exemplu, o imagine sau un răspuns text. Ca dezvoltator, puteți folosi apoi aceste informații pentru a procesa mai departe răspunsul sau pentru a-l prezenta utilizatorului.

- **Se integrează cu Microsoft Agent Framework**. Microsoft Foundry Agent Service funcționează perfect cu Microsoft Agent Framework, ceea ce înseamnă că puteți construi agenți folosind `FoundryChatClient` și îi puteți implementa prin Agent Service pentru scenarii de producție.

**Cazuri de utilizare**: Microsoft Foundry Agent Service este conceput pentru aplicații enterprise care necesită implementare securizată, scalabilă și flexibilă a agenților AI.

## Care este diferența între aceste abordări?
 
Pare că există suprapuneri, dar există diferențe cheie în design, capacități și cazuri de utilizare:
 
- **Microsoft Agent Framework (MAF)**: Este un SDK gata pentru producție pentru construirea agenților AI. Oferă o API simplificată pentru crearea agenților cu apelare de instrumente, gestionarea conversațiilor și integrare identitate Azure.
- **Microsoft Foundry Agent Service**: Este o platformă și serviciu de implementare în Microsoft Foundry pentru agenți. Oferă conectivitate integrată pentru servicii precum Azure OpenAI, Azure AI Search, Bing Search și execuția codului.
 
Încă nu sunteți sigur ce să alegeți?

### Cazuri de utilizare
 
Să vedem dacă putem ajuta trecând prin câteva cazuri comune de utilizare:
 
> Î: Construiesc aplicații agenți AI pentru producție și vreau să încep rapid
>

> R: Microsoft Agent Framework este o alegere excelentă. Oferă o API simplă, pythonică prin `FoundryChatClient` care vă permite să definiți agenți cu instrumente și instrucțiuni în doar câteva linii de cod.

> Î: Am nevoie de implementare enterprise cu integrări Azure precum Search și execuția codului
>
> R: Microsoft Foundry Agent Service este cea mai potrivită. Este un serviciu de platformă care oferă capabilități integrate pentru modele multiple, Azure AI Search, Bing Search și Azure Functions. Face ușoară construirea agenților în portalul Foundry și implementarea lor la scară.
 
> Î: Sunt încă confuz, dă-mi o singură opțiune
>
> R: Începe cu Microsoft Agent Framework pentru a-ți construi agenții, apoi folosește Microsoft Foundry Agent Service când ai nevoie să îi implementezi și să îi scalezi în producție. Această abordare îți permite să iterezi rapid logica agentului având totodată un drum clar către implementare enterprise.
 
Hai să rezumăm diferențele cheie într-un tabel:

| Framework | Focus | Concepte de bază | Cazuri de utilizare |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK simplificat pentru agenți cu apelare instrumente | Agenți, Instrumente, Identitate Azure | Construirea agenților AI, utilizarea instrumentelor, fluxuri multi-pas |
| Microsoft Foundry Agent Service | Modele flexibile, securitate enterprise, generare cod, apelare instrumente | Modularitate, Colaborare, Orchestrare procese | Implementare securizată, scalabilă și flexibilă a agenților AI |

## Pot integra direct instrumentele existente din ecosistemul Azure sau am nevoie de soluții independente?


Răspunsul este da, poți integra instrumentele tale existente din ecosistemul Azure direct cu Microsoft Foundry Agent Service în special, deoarece a fost construit pentru a funcționa perfect cu alte servicii Azure. De exemplu, ai putea integra Bing, Azure AI Search și Azure Functions. Există, de asemenea, o integrare profundă cu Microsoft Foundry.

Framework-ul Microsoft Agent se integrează, de asemenea, cu serviciile Azure prin `FoundryChatClient` și identitate Azure, permițându-ți să apelezi serviciile Azure direct din instrumentele agentului tău.

## Exemple de cod

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Ai mai multe întrebări despre AI Agent Frameworks?

Alătură-te [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la sesiuni de tip office hours și a primi răspunsuri la întrebările tale legate de AI Agents.

## Referințe

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Lecția Anterioară

[Introducere în Agenții AI și cazurile de utilizare ale agenților](../01-intro-to-ai-agents/README.md)

## Lecția Următoare

[Înțelegerea modelelor de design agentic](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->