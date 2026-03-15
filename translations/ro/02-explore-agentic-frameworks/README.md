[![Explorarea cadrelor pentru agenți AI](../../../translated_images/ro/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Explorează cadrele pentru agenți AI

Cadrele pentru agenți AI sunt platforme software concepute pentru a simplifica crearea, implementarea și gestionarea agenților AI. Aceste cadre oferă dezvoltatorilor componente pre-construite, abstractizări și instrumente care eficientizează dezvoltarea sistemelor AI complexe.

Aceste cadre ajută dezvoltatorii să se concentreze pe aspectele unice ale aplicațiilor lor prin oferirea unor abordări standardizate pentru provocările comune în dezvoltarea agenților AI. Ele îmbunătățesc scalabilitatea, accesibilitatea și eficiența în construirea sistemelor AI.

## Introducere 

Această lecție va acoperi:

- Ce sunt cadrele pentru agenți AI și ce permit dezvoltatorilor să realizeze?
- Cum pot echipele să folosească aceste cadre pentru a prototipa rapid, itera și îmbunătăți capabilitățile agenților lor?
- Care sunt diferențele dintre cadrele și instrumentele create de Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> și <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Pot integra instrumentele mele existente din ecosistemul Azure direct sau am nevoie de soluții independente?
- Ce este serviciul Azure AI Agents și cum mă ajută acesta?

## Obiective de învățare

Obiectivele acestei lecții sunt să vă ajute să înțelegeți:

- Rolul cadrelor pentru agenți AI în dezvoltarea AI.
- Cum să valorificați cadrele pentru agenți AI pentru a construi agenți inteligenți.
- Capabilitățile cheie oferite de cadrele pentru agenți AI.
- Diferențele dintre Microsoft Agent Framework și Azure AI Agent Service.

## Ce sunt cadrele pentru agenți AI și ce permit dezvoltatorilor să facă?

Cadrele AI tradiționale pot ajuta la integrarea AI în aplicațiile dvs. și îmbunătățirea acestora în următoarele moduri:

- **Personalizare**: AI poate analiza comportamentul și preferințele utilizatorilor pentru a oferi recomandări, conținut și experiențe personalizate.
Exemplu: Serviciile de streaming precum Netflix folosesc AI pentru a sugera filme și emisiuni bazate pe istoricul vizionărilor, sporind implicarea și satisfacția utilizatorilor.
- **Automatizare și Eficiență**: AI poate automatiza sarcini repetitive, eficientiza fluxurile de lucru și îmbunătăți eficiența operațională.
Exemplu: Aplicațiile de asistență clienți folosesc chatbots alimentați de AI pentru a gestiona întrebări comune, reducând timpii de răspuns și eliberând agenții umani pentru probleme mai complexe.
- **Experiență Îmbunătățită a Utilizatorului**: AI poate îmbunătăți experiența generală a utilizatorului prin oferirea de funcții inteligente precum recunoașterea vocală, procesarea limbajului natural și text predictiv.
Exemplu: Asistenții virtuali precum Siri și Google Assistant folosesc AI pentru a înțelege și răspunde comenzilor vocale, facilitând interacțiunea utilizatorilor cu dispozitivele lor.

### Toate acestea sună grozav, deci de ce avem nevoie de cadrul pentru agenți AI?

Cadrele pentru agenți AI reprezintă ceva mai mult decât simple cadre AI. Ele sunt proiectate să permită crearea de agenți inteligenți care pot interacționa cu utilizatorii, alți agenți și mediul pentru a atinge obiective specifice. Acești agenți pot manifesta comportament autonom, pot lua decizii și se pot adapta la condiții în schimbare. Să analizăm câteva capabilități cheie oferite de cadrele pentru agenți AI:

- **Colaborare și coordonare a agenților**: Permite crearea a mai multor agenți AI care pot lucra împreună, comunica și coordona pentru a rezolva sarcini complexe.
- **Automatizarea și gestionarea sarcinilor**: Oferă mecanisme pentru automatizarea fluxurilor de lucru cu mai mulți pași, delegarea sarcinilor și gestionarea dinamică a acestora între agenți.
- **Înțelegerea contextuală și adaptarea**: Echiparea agenților cu abilitatea de a înțelege contextul, a se adapta la medii în schimbare și a lua decizii pe baza informațiilor în timp real.

Pe scurt, agenții vă permit să faceți mai mult, să duceți automatizarea la un nivel superior, să creați sisteme mai inteligente care se pot adapta și învăța din mediul lor.

## Cum să prototipăm rapid, să iterăm și să îmbunătățim capabilitățile agentului?

Aceasta este o zonă în mișcare rapidă, dar există câteva lucruri comune la majoritatea cadrelor pentru agenți AI care vă pot ajuta să prototipați și să iterați rapid, anume componente modulare, instrumente colaborative și învățare în timp real. Să le analizăm:

- **Folosiți componente modulare**: SDK-urile AI oferă componente pre-construite precum conectori AI și de memorie, apelarea funcțiilor folosind limbaj natural sau plugin-uri de cod, șabloane de prompt și altele.
- **Valorificați instrumentele colaborative**: Proiectați agenți cu roluri și sarcini specifice, permițându-le să testeze și să rafineze fluxurile de lucru colaborative.
- **Învățați în timp real**: Implementați bucle de feedback în care agenții învață din interacțiuni și își ajustează comportamentul în mod dinamic.

### Folosiți componente modulare

SDK-uri precum Microsoft Agent Framework oferă componente pre-construite precum conectori AI, definiții de instrumente și management al agenților.

**Cum pot folosi echipele acestea**: Echipele pot asambla rapid aceste componente pentru a crea un prototip funcțional fără a începe de la zero, permițând experimentare și iterare rapidă.

**Cum funcționează în practică**: Puteți folosi un parser pre-construit pentru a extrage informații din input-ul utilizatorului, un modul de memorie pentru a stoca și recupera date și un generator de prompturi pentru a interacționa cu utilizatorii, toate fără a construi aceste componente de la zero.

**Exemplu de cod**. Să vedem un exemplu de folosire a Microsoft Agent Framework cu `AzureAIProjectAgentProvider` pentru a avea modelul să răspundă la input-ul utilizatorului prin apelarea unor instrumente:

``` python
# Exemplu Python pentru Microsoft Agent Framework

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Definește o funcție de exemplu a unui instrument pentru rezervarea călătoriilor
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Exemplu de ieșire: Zborul dvs. către New York din 1 ianuarie 2025 a fost rezervat cu succes. Călătorie plăcută! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Ce puteți observa din acest exemplu este cum puteți valorifica un parser pre-construit pentru a extrage informații cheie din input-ul utilizatorului, cum ar fi originea, destinația și data unei cereri de rezervare zbor. Această abordare modulară vă permite să vă concentrați pe logica de nivel înalt.

### Valorificați instrumentele colaborative

Cadre precum Microsoft Agent Framework facilitează crearea mai multor agenți care pot lucra împreună.

**Cum pot folosi echipele aceasta**: Echipele pot proiecta agenți cu roluri și sarcini specifice, permițându-le să testeze și să rafineze fluxurile de lucru colaborative și să îmbunătățească eficiența globală a sistemului.

**Cum funcționează în practică**: Puteți crea o echipă de agenți în care fiecare agent are o funcție specializată, cum ar fi recuperarea datelor, analiza sau luarea deciziilor. Acești agenți pot comunica și împărtăși informații pentru a atinge un scop comun, precum răspunsul la o întrebare a utilizatorului sau finalizarea unei sarcini.

**Exemplu de cod (Microsoft Agent Framework)**:

```python
# Crearea mai multor agenți care colaborează folosind Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Agent de recuperare a datelor
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent de analiză a datelor
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Rulează agenții în secvență pentru o sarcină
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Ce vedeți în codul anterior este cum puteți crea o sarcină care implică mai mulți agenți care lucrează împreună pentru a analiza date. Fiecare agent efectuează o funcție specifică, iar sarcina este executată prin coordonarea agenților pentru a obține rezultatul dorit. Prin crearea unor agenți dedicați cu roluri specializate, puteți îmbunătăți eficiența și performanța sarcinii.

### Învățați în timp real

Cadrele avansate oferă capabilități pentru înțelegerea contextului și adaptarea în timp real.

**Cum pot folosi echipele aceasta**: Echipele pot implementa bucle de feedback în care agenții învață din interacțiuni și își ajustează comportamentul dinamic, conducând la îmbunătățiri și rafinări continue ale capabilităților.

**Cum funcționează în practică**: Agenții pot analiza feedback-ul utilizatorilor, datele de mediu și rezultatele sarcinilor pentru a-și actualiza baza de cunoștințe, a ajusta algoritmii de luare a deciziilor și a îmbunătăți performanța în timp. Acest proces iterativ de învățare permite agenților să se adapteze la condițiile în schimbare și la preferințele utilizatorilor, sporind eficacitatea generală a sistemului.

## Care sunt diferențele dintre Microsoft Agent Framework și Azure AI Agent Service?

Există multe modalități de a compara aceste abordări, dar să analizăm câteva diferențe cheie în ceea ce privește designul, capabilitățile și cazurile țintă de utilizare:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework oferă un SDK simplificat pentru construirea agenților AI folosind `AzureAIProjectAgentProvider`. Permite dezvoltatorilor să creeze agenți care valorifică modelele Azure OpenAI cu apelare integrată de instrumente, managementul conversațiilor și securitate de nivel enterprise prin identitatea Azure.

**Cazuri de utilizare**: Construirea de agenți AI gata pentru producție cu utilizarea instrumentelor, fluxuri de lucru cu pași multipli și scenarii de integrare enterprise.

Iată câteva concepte de bază importante ale Microsoft Agent Framework:

- **Agenți**. Un agent este creat prin `AzureAIProjectAgentProvider` și configurat cu un nume, instrucțiuni și instrumente. Agentul poate:
  - **Procesează mesajele utilizatorului** și generează răspunsuri folosind modelele Azure OpenAI.
  - **Apelează instrumente** automat, în funcție de contextul conversației.
  - **Menține starea conversației** pe parcursul mai multor interacțiuni.

  Iată un fragment de cod care arată cum să creați un agent:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Instrumente**. Framework-ul suportă definirea instrumentelor ca funcții Python pe care agentul le poate invoca automat. Instrumentele sunt înregistrate la crearea agentului:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Coordonarea multi-agent**. Puteți crea mai mulți agenți cu specializări diferite și să le coordonați lucrul:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Integrarea identității Azure**. Framework-ul folosește `AzureCliCredential` (sau `DefaultAzureCredential`) pentru autentificare securizată fără chei, eliminând necesitatea gestionării directe a cheilor API.

## Azure AI Agent Service

Azure AI Agent Service este o adiție mai recentă, introdusă la Microsoft Ignite 2024. Permite dezvoltarea și implementarea agenților AI cu modele mai flexibile, cum ar fi apelarea directă a LLM-urilor open-source precum Llama 3, Mistral și Cohere.

Azure AI Agent Service oferă mecanisme de securitate enterprise mai puternice și metode de stocare a datelor, făcându-l potrivit pentru aplicații enterprise.

Funcționează imediat cu Microsoft Agent Framework pentru construirea și implementarea agenților.

Acest serviciu este în prezent în previzualizare publică și suportă Python și C# pentru construirea agenților.

Folosind SDK-ul Python Azure AI Agent Service, putem crea un agent cu un instrument definit de utilizator:

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

Azure AI Agent Service are următoarele concepte principale:

- **Agent**. Azure AI Agent Service se integrează cu Microsoft Foundry. În AI Foundry, un agent AI acționează ca un microserviciu „inteligent” care poate fi folosit pentru a răspunde la întrebări (RAG), a efectua acțiuni sau a automatiza complet fluxuri de lucru. Acesta realizează acest lucru combinând puterea modelelor generative AI cu instrumente care îi permit să acceseze și să interacționeze cu surse de date reale. Iată un exemplu de agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    În acest exemplu, un agent este creat cu modelul `gpt-4o-mini`, un nume `my-agent` și instrucțiuni `You are helpful agent`. Agentul este echipat cu instrumente și resurse pentru a efectua sarcini de interpretare a codului.

- **Fir de discuție și mesaje**. Firul de discuție este un alt concept important. Reprezintă o conversație sau o interacțiune între un agent și un utilizator. Firele pot fi folosite pentru a urmări progresul unei conversații, a stoca informații contextuale și a gestiona starea interacțiunii. Iată un exemplu de fir:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    În codul anterior, este creat un fir. Ulterior, un mesaj este trimis în fir. Prin apelarea `create_and_process_run`, agentului i se cere să lucreze pe fir. În final, mesajele sunt preluate și înregistrate pentru a vedea răspunsul agentului. Mesajele indică progresul conversației dintre utilizator și agent. De asemenea, este important să înțelegeți că mesajele pot fi de tipuri diferite, cum ar fi text, imagine sau fișier, ceea ce înseamnă că activitatea agenților a dus, de exemplu, la o imagine sau la un răspuns text. Ca dezvoltator, puteți folosi aceste informații pentru a procesa în continuare răspunsul sau pentru a-l prezenta utilizatorului.

- **Integrează cu Microsoft Agent Framework**. Azure AI Agent Service funcționează perfect cu Microsoft Agent Framework, ceea ce înseamnă că puteți construi agenți folosind `AzureAIProjectAgentProvider` și îi puteți implementa prin Agent Service pentru scenarii de producție.

**Cazuri de utilizare**: Azure AI Agent Service este proiectat pentru aplicații enterprise care necesită implementare sigură, scalabilă și flexibilă a agenților AI.

## Care este diferența dintre aceste abordări?

Se pare că există suprapuneri, dar există diferențe cheie în ceea ce privește designul, capabilitățile și cazurile țintă de utilizare:

- **Microsoft Agent Framework (MAF)**: Este un SDK gata de producție pentru construirea agenților AI. Oferă o API simplificată pentru crearea agenților cu apelare de instrumente, gestionarea conversațiilor și integrarea identității Azure.
- **Azure AI Agent Service**: Este o platformă și un serviciu de implementare în Azure Foundry pentru agenți. Oferă conectivitate încorporată cu servicii precum Azure OpenAI, Azure AI Search, Bing Search și execuție de cod.

Totuși nu sunteți sigur care să alegeți?

### Cazuri de utilizare

Să vedem dacă vă putem ajuta trecând prin câteva cazuri uzuale:

> Întrebare: Construiesc aplicații AI agent în producție și vreau să încep rapid
>

>Răspuns: Microsoft Agent Framework este o alegere excelentă. Oferă o API simplă, pythonică prin `AzureAIProjectAgentProvider` care vă permite să definiți agenți cu instrumente și instrucțiuni în doar câteva linii de cod.

>Întrebare: Am nevoie de o implementare de nivel enterprise cu integrări Azure precum Search și execuția de cod
>
> Răspuns: Azure AI Agent Service este cea mai bună opțiune. Este un serviciu de platformă care oferă capabilități integrate pentru multiple modele, Azure AI Search, Bing Search și Azure Functions. Face ușoară construirea agenților în Portalul Foundry și implementarea lor la scară.

> Întrebare: Sunt încă confuz, dă-mi o singură opțiune
>
> Răspuns: Începeți cu Microsoft Agent Framework pentru a construi agenții, apoi folosiți Azure AI Agent Service când aveți nevoie să îi implementați și să îi scalați în producție. Această abordare vă permite să iterați rapid asupra logicii agentului, având în același timp o cale clară către implementarea enterprise.

Să rezumăm diferențele cheie într-un tabel:

| Cadru | Focalizare | Concepte cheie | Cazuri de utilizare |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK simplificat pentru agenți cu apelare de instrumente | Agenți, Instrumente, Identitate Azure | Construirea agenților AI, utilizarea instrumentelor, fluxuri de lucru multi-pași |
| Azure AI Agent Service | Modele flexibile, securitate enterprise, generare cod, apelare instrumente | Modularitate, Colaborare, Orchestrarea proceselor | Implementare sigură, scalabilă și flexibilă a agenților AI |

## Pot integra instrumentele mele existente din ecosistemul Azure direct sau am nevoie de soluții independente?
Răspunsul este da, poți integra instrumentele tale existente din ecosistemul Azure direct cu Azure AI Agent Service în special, deoarece a fost construit pentru a funcționa perfect cu alte servicii Azure. De exemplu, ai putea integra Bing, Azure AI Search și Azure Functions. Există, de asemenea, o integrare profundă cu Microsoft Foundry.

Microsoft Agent Framework se integrează, de asemenea, cu serviciile Azure prin `AzureAIProjectAgentProvider` și identitatea Azure, permițându-ți să apelezi serviciile Azure direct din instrumentele agentului tău.

## Sample Codes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Got More Questions about AI Agent Frameworks?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Previous Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinarea răspunderii**:
Acest document a fost tradus folosind serviciul de traducere automată [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm răspunderea pentru eventuale neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->