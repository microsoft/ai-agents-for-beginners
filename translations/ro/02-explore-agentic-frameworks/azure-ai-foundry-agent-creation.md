# Dezvoltarea Serviciului Agent Microsoft Foundry

În acest exercițiu, veți utiliza uneltele Serviciului Agent Microsoft Foundry din [portalul Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) pentru a crea un agent pentru Rezervarea Zborurilor. Agentul va putea să interacționeze cu utilizatorii și să ofere informații despre zboruri.

## Cerințe preliminare

Pentru a finaliza acest exercițiu, aveți nevoie de următoarele:
1. Un cont Azure cu un abonament activ. [Creați un cont gratuit](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Aveți nevoie de permisiuni pentru a crea un hub Microsoft Foundry sau să aveți unul creat pentru dvs.
    - Dacă rolul dvs. este Contribuitor sau Proprietar, puteți urma pașii din acest tutorial.

## Creați un hub Microsoft Foundry

> **Notă:** Microsoft Foundry a fost cunoscut anterior ca Azure AI Studio.

1. Urmați aceste ghiduri din postarea de blog [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) pentru crearea unui hub Microsoft Foundry.
2. Când proiectul dvs. este creat, închideți orice sfaturi afișate și examinați pagina proiectului în portalul Microsoft Foundry, care ar trebui să arate asemănător cu imaginea următoare:

    ![Microsoft Foundry Project](../../../translated_images/ro/azure-ai-foundry.88d0c35298348c2f.webp)

## Implementați un model

1. În panoul din stânga pentru proiectul dvs., în secțiunea **My assets**, selectați pagina **Models + endpoints**.
2. În pagina **Models + endpoints**, în fila **Model deployments**, în meniul **+ Deploy model**, selectați **Deploy base model**.
3. Căutați modelul `gpt-5-mini` în listă, apoi selectați-l și confirmați.

    > **Notă**: Reducerea TPM ajută la evitarea utilizării excesive a cotei disponibile în abonamentul pe care îl folosiți.

    ![Model Deployed](../../../translated_images/ro/model-deployment.3749c53fb81e18fd.webp)

## Creați un agent

Acum că ați implementat un model, puteți crea un agent. Un agent este un model AI conversațional care poate fi folosit pentru a interacționa cu utilizatorii.

1. În panoul din stânga pentru proiectul dvs., în secțiunea **Build & Customize**, selectați pagina **Agents**.
2. Faceți clic pe **+ Create agent** pentru a crea un agent nou. În caseta de dialog **Agent Setup**:
    - Introduceți un nume pentru agent, de exemplu `FlightAgent`.
    - Asigurați-vă că este selectată implementarea modelului `gpt-5-mini` pe care ați creat-o anterior
    - Stabiliți **Instrucțiunile** conform promptului pe care doriți ca agentul să îl urmeze. Iată un exemplu:
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
> Pentru un prompt detaliat, puteți consulta [acest depozit](https://github.com/ShivamGoyal03/RoamMind) pentru mai multe informații.
    
> Mai mult, puteți adăuga o **Bază de Cunoștințe** și **Acțiuni** pentru a îmbunătăți capabilitățile agentului de a oferi mai multe informații și de a efectua sarcini automate bazate pe cererile utilizatorilor. Pentru acest exercițiu, puteți sări peste acești pași.
    
![Agent Setup](../../../translated_images/ro/agent-setup.9bbb8755bf5df672.webp)

3. Pentru a crea un agent multi-AI nou, faceți pur și simplu clic pe **New Agent**. Agentul nou creat va fi afișat apoi în pagina Agents.


## Testați agentul

După ce creați agentul, îl puteți testa pentru a vedea cum răspunde la întrebări ale utilizatorilor în zona de testare a portalului Microsoft Foundry.

1. În partea de sus a panoului **Setup** pentru agentul dvs., selectați **Try in playground**.
2. În panoul **Playground**, puteți interacționa cu agentul tastând întrebările în fereastra de chat. De exemplu, puteți cere agentului să caute zboruri de la Seattle la New York pe data de 28.

    > **Notă**: Agentul s-ar putea să nu ofere răspunsuri precise, deoarece nu se folosesc date în timp real în acest exercițiu. Scopul este de a testa capacitatea agentului de a înțelege și de a răspunde la întrebările utilizatorilor bazându-se pe instrucțiunile oferite.

    ![Agent Playground](../../../translated_images/ro/agent-playground.dc146586de715010.webp)

3. După testarea agentului, îl puteți personaliza în continuare adăugând mai multe intenții, date de antrenament și acțiuni pentru a-i îmbunătăți capacitățile.

## Curățați resursele

Când ați terminat testarea agentului, îl puteți șterge pentru a evita costuri suplimentare.
1. Deschideți [portalul Azure](https://portal.azure.com) și vedeți conținutul grupului de resurse unde ați implementat resursele hub folosite în acest exercițiu.
2. În bara de instrumente, selectați **Delete resource group**.
3. Introduceți numele grupului de resurse și confirmați că doriți să-l ștergeți.

## Resurse

- [Documentația Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Portalul Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Început cu Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Fundamentele agenților AI pe Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->