# Microsoft Foundry Agent Service Udvikling

I denne øvelse bruger du Microsoft Foundry Agent Service-værktøjerne i [Microsoft Foundry-portalen](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) til at oprette en agent til Flybestilling. Agenten vil kunne interagere med brugere og give information om fly.

## Forudsætninger

For at gennemføre denne øvelse skal du bruge følgende:
1. En Azure-konto med et aktivt abonnement. [Opret en konto gratis](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Du skal have tilladelse til at oprette en Microsoft Foundry-hub eller have en oprettet for dig.
    - Hvis din rolle er Bidragyder eller Ejer, kan du følge trinnene i denne vejledning.

## Opret en Microsoft Foundry-hub

> **Bemærk:** Microsoft Foundry var tidligere kendt som Azure AI Studio.

1. Følg disse retningslinjer fra [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) blogindlægget for at oprette en Microsoft Foundry-hub.
2. Når dit projekt er oprettet, luk eventuelle tips, der vises, og gennemgå projektets side i Microsoft Foundry-portalen, som skulle ligne følgende billede:

    ![Microsoft Foundry Project](../../../translated_images/da/azure-ai-foundry.88d0c35298348c2f.webp)

## Implementer en model

1. I venstre rude for dit projekt, i sektionen **Mine aktiver**, vælg siden **Modeller + endepunkter**.
2. På siden **Modeller + endepunkter**, under fanen **Modelimplementeringer**, i menuen **+ Implementer model**, vælg **Implementer basismodel**.
3. Søg efter `gpt-4o-mini` modellen på listen, og vælg derefter og bekræft den.

    > **Bemærk**: At reducere TPM hjælper med at undgå overskridelse af kvoten, der er tilgængelig i det abonnement, du bruger.

    ![Model Deployed](../../../translated_images/da/model-deployment.3749c53fb81e18fd.webp)

## Opret en agent

Nu hvor du har implementeret en model, kan du oprette en agent. En agent er en konversationel AI-model, der kan bruges til at interagere med brugere.

1. I venstre rude for dit projekt, i sektionen **Byg & Tilpas**, vælg siden **Agenter**.
2. Klik på **+ Opret agent** for at oprette en ny agent. Under dialogboksen **Agentopsætning**:
    - Indtast et navn til agenten, f.eks. `FlightAgent`.
    - Sørg for, at den tidligere oprettede modelimplementering `gpt-4o-mini` er valgt
    - Angiv **Instruktioner** i henhold til den prompt, du ønsker, agenten skal følge. Her er et eksempel:
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
> For en detaljeret prompt kan du tjekke [dette repository](https://github.com/ShivamGoyal03/RoamMind) for mere information.
    
> Desuden kan du tilføje **vidensbase** og **handlinger** for at forbedre agentens evner til at give mere information og udføre automatiserede opgaver baseret på brugerens anmodninger. For denne øvelse kan du springe disse trin over.
    
![Agent Setup](../../../translated_images/da/agent-setup.9bbb8755bf5df672.webp)

3. For at oprette en ny multi-AI agent skal du blot klikke på **Ny agent**. Den nyoprettede agent vises derefter på Agents-siden.


## Test agenten

Efter oprettelsen af agenten kan du teste den for at se, hvordan den reagerer på brugerforespørgsler i Microsoft Foundry-portalen playground.

1. Øverst i **Opsætning**-ruden for din agent skal du vælge **Prøv i playground**.
2. I **Playground**-ruden kan du interagere med agenten ved at skrive forespørgsler i chatvinduet. For eksempel kan du bede agenten om at søge efter flyvninger fra Seattle til New York den 28.

    > **Bemærk**: Agenten giver muligvis ikke nøjagtige svar, da ingen realtidsdata bruges i denne øvelse. Formålet er at teste agentens evne til at forstå og besvare brugerforespørgsler baseret på de angivne instruktioner.

    ![Agent Playground](../../../translated_images/da/agent-playground.dc146586de715010.webp)

3. Efter at have testet agenten kan du yderligere tilpasse den ved at tilføje flere intentioner, træningsdata og handlinger for at forbedre dens muligheder.

## Ryd op i ressourcer

Når du er færdig med at teste agenten, kan du slette den for at undgå ekstra omkostninger.
1. Åbn [Azure portalen](https://portal.azure.com) og se indholdet i den ressourcegruppe, hvor du implementerede hub-ressourcerne, der blev brugt i denne øvelse.
2. På værktøjslinjen skal du vælge **Slet ressourcegruppe**.
3. Indtast navnet på ressourcegruppen, og bekræft at du ønsker at slette den.

## Ressourcer

- [Microsoft Foundry dokumentation](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Kom godt i gang med Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Grundlæggende om AI-agenter på Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->