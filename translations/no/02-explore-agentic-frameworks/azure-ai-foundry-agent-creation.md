# Microsoft Foundry Agent Service-utvikling

I denne øvelsen bruker du Microsoft Foundry Agent Service-verktøyene i [Microsoft Foundry-portalen](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) for å lage en agent for flybestilling. Agenten vil kunne samhandle med brukere og gi informasjon om flyreiser.

## Forutsetninger

For å fullføre denne øvelsen trenger du følgende:
1. En Azure-konto med et aktivt abonnement. [Opprett en konto gratis](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Du må ha tillatelser til å opprette en Microsoft Foundry-hub eller ha en opprettet for deg.
    - Hvis rollen din er Bidragsyter eller Eier, kan du følge trinnene i denne veiledningen.

## Opprett en Microsoft Foundry-hub

> **Merk:** Microsoft Foundry var tidligere kjent som Azure AI Studio.

1. Følg retningslinjene fra [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) blogginnlegget for å opprette en Microsoft Foundry-hub.
2. Når prosjektet ditt er opprettet, lukk eventuelle tips som vises og gjennomgå prosjekt-siden i Microsoft Foundry-portalen, som skal se omtrent slik ut som bildet nedenfor:

    ![Microsoft Foundry Project](../../../translated_images/no/azure-ai-foundry.88d0c35298348c2f.webp)

## Distribuer en modell

1. I ruten til venstre for prosjektet ditt, i seksjonen **Mine ressurser**, velg siden **Modeller + endepunkter**.
2. På siden **Modeller + endepunkter**, i fanen **Modelldistribusjoner**, i menyen **+ Distribuer modell**, velg **Distribuer grunnmodell**.
3. Søk etter `gpt-4o-mini`-modellen i listen, og velg og bekreft den.

    > **Merk**: Å redusere TPM hjelper med å unngå overforbruk av kvoten som er tilgjengelig i abonnementet du bruker.

    ![Model Deployed](../../../translated_images/no/model-deployment.3749c53fb81e18fd.webp)

## Opprett en agent

Nå som du har distribuert en modell, kan du opprette en agent. En agent er en samtale-AI-modell som kan brukes til å samhandle med brukere.

1. I ruten til venstre for prosjektet ditt, i seksjonen **Bygg & Tilpass**, velg siden **Agenter**.
2. Klikk på **+ Opprett agent** for å opprette en ny agent. Under dialogboksen **Agentoppsett**:
    - Skriv inn et navn for agenten, for eksempel `FlightAgent`.
    - Sørg for at distribusjonen av `gpt-4o-mini`-modellen som du opprettet tidligere er valgt
    - Sett **Instruksjonene** i henhold til prompten du vil at agenten skal følge. Her er et eksempel:
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
> For en detaljert prompt kan du sjekke [dette depotet](https://github.com/ShivamGoyal03/RoamMind) for mer informasjon.
    
> I tillegg kan du legge til **Kunnskapsbase** og **Handlinger** for å forbedre agentens evner til å gi mer informasjon og utføre automatiserte oppgaver basert på brukerforespørsler. For denne øvelsen kan du hoppe over disse trinnene.
    
![Agent Setup](../../../translated_images/no/agent-setup.9bbb8755bf5df672.webp)

3. For å opprette en ny multi-AI-agent, klikk ganske enkelt på **Ny agent**. Den nyopprettede agenten vil da vises på Agents-siden.


## Test agenten

Etter å ha opprettet agenten, kan du teste den for å se hvordan den svarer på brukerhenvendelser i Microsoft Foundry-portalen sin lekeplass.

1. Øverst i **Oppsett**-ruten for agenten din velger du **Prøv i lekeplass**.
2. I **Lekeplass**-ruten kan du samhandle med agenten ved å skrive spørsmål i chattevinduet. For eksempel kan du be agenten om å søke etter flyreiser fra Seattle til New York den 28.

    > **Merk**: Agenten kan hende ikke gir nøyaktige svar, ettersom ingen sanntidsdata brukes i denne øvelsen. Formålet er å teste agentens evne til å forstå og svare på brukerhenvendelser basert på instruksjonene som er gitt.

    ![Agent Playground](../../../translated_images/no/agent-playground.dc146586de715010.webp)

3. Etter å ha testet agenten, kan du tilpasse den ytterligere ved å legge til flere intensjoner, treningsdata og handlinger for å forbedre dens evner.

## Rydd opp ressurser

Når du er ferdig med å teste agenten, kan du slette den for å unngå ekstra kostnader.
1. Åpne [Azure-portalen](https://portal.azure.com) og se innholdet i ressursgruppen der du distribuerte hub-ressursene brukt i denne øvelsen.
2. På verktøylinjen velger du **Slett ressursgruppe**.
3. Skriv inn navnet på ressursgruppen og bekreft at du vil slette den.

## Ressurser

- [Microsoft Foundry dokumentasjon](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Kom i gang med Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Grunnleggende om AI-agenter på Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->