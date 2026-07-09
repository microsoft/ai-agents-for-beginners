# Dezvoltarea Serviciului Microsoft Foundry Agent

În acest exercițiu, folosești uneltele serviciului Microsoft Foundry Agent din [portalul Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) pentru a crea un agent pentru Rezervarea Zborurilor. Agentul va putea interacționa cu utilizatorii și va oferi informații despre zboruri.

## Cerințe preliminare

Pentru a finaliza acest exercițiu, ai nevoie de următoarele:
1. Un cont Azure cu un abonament activ. [Creează un cont gratuit](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Ai nevoie de permisiuni să creezi un hub Microsoft Foundry sau să ți se creeze unul.
    - Dacă rolul tău este Contributor sau Owner, poți urma pașii din acest tutorial.

## Creează un hub Microsoft Foundry

> **Notă:** Microsoft Foundry a fost anterior cunoscut sub numele de Azure AI Studio.

1. Urmează aceste indicații din postarea de blog [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) pentru a crea un hub Microsoft Foundry.
2. Când proiectul tău este creat, închide orice sugestii afișate și revizuiește pagina proiectului din portalul Microsoft Foundry, care ar trebui să semene cu următoarea imagine:

    ![Microsoft Foundry Project](../../../translated_images/ro/azure-ai-foundry.88d0c35298348c2f.webp)

## Deployarea unui model

1. În panoul din stânga al proiectului tău, în secțiunea **My assets**, selectează pagina **Models + endpoints**.
2. În pagina **Models + endpoints**, în fila **Model deployments**, în meniul **+ Deploy model**, selectează **Deploy base model**.
3. Caută modelul `gpt-4o-mini` în listă, apoi selectează-l și confirmă.

    > **Notă**: Reducerea TPM ajută la evitarea utilizării excesive a cotei disponibile în abonamentul folosit.

    ![Model Deployed](../../../translated_images/ro/model-deployment.3749c53fb81e18fd.webp)

## Creează un agent

Acum că ai deployat un model, poți crea un agent. Un agent este un model AI conversațional ce poate fi folosit pentru a interacționa cu utilizatorii.

1. În panoul din stânga al proiectului tău, în secțiunea **Build & Customize**, selectează pagina **Agents**.
2. Click pe **+ Create agent** pentru a crea un agent nou. În dialogul **Agent Setup**:
    - Introdu un nume pentru agent, de exemplu `FlightAgent`.
    - Asigură-te că este selectată deployarea modelului `gpt-4o-mini` pe care ai creat-o anterior.
    - Setează **Instructions** conform promptului pe care vrei ca agentul să îl urmeze. Iată un exemplu:
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> Pentru un prompt detaliat, poți consulta [acest depozit](https://github.com/ShivamGoyal03/RoamMind) pentru mai multe informații.
    
> Mai mult, poți adăuga o **Bază de Cunoștințe** și **Acțiuni** pentru a îmbunătăți capabilitățile agentului de a oferi mai multe informații și a efectua sarcini automate bazate pe cererile utilizatorilor. Pentru acest exercițiu, poți sări peste acești pași.
    
![Agent Setup](../../../translated_images/ro/agent-setup.9bbb8755bf5df672.webp)

3. Pentru a crea un agent multi-AI nou, apasă simplu pe **New Agent**. Agentul creat va apărea apoi în pagina Agents.


## Testează agentul

După ce ai creat agentul, poți să-l testezi pentru a vedea cum răspunde la interogările utilizatorilor în zona de testare (playground) din portalul Microsoft Foundry.

1. În partea de sus a panoului **Setup** pentru agentul tău, selectează **Try in playground**.
2. În panoul **Playground**, poți interacționa cu agentul tastând întrebări în fereastra de chat. De exemplu, poți cere agentului să caute zboruri de la Seattle la New York pe data de 28.

    > **Notă**: Agentul poate să nu ofere răspunsuri exacte, deoarece nu se folosesc date în timp real în acest exercițiu. Scopul este de a testa abilitatea agentului de a înțelege și răspunde la întrebările utilizatorilor pe baza instrucțiunilor date.

    ![Agent Playground](../../../translated_images/ro/agent-playground.dc146586de715010.webp)

3. După testarea agentului, îl poți personaliza adăugând mai multe intenții, date de antrenament și acțiuni pentru a-i extinde capabilitățile.

## Curățarea resurselor

Când ai terminat testarea agentului, îl poți șterge pentru a evita costuri suplimentare.
1. Deschide [portalul Azure](https://portal.azure.com) și vezi conținutul grupului de resurse unde ai deployat resursele hub folosite în acest exercițiu.
2. În bara de instrumente, selectează **Delete resource group**.
3. Introdu numele grupului de resurse și confirmă că vrei să îl ștergi.

## Resurse

- [Documentația Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Portalul Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Introducere în Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Fundamentele agenților AI pe Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->