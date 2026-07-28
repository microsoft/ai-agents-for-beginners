# Razvoj Microsoft Foundry Agent Service

U ovom zadatku koristite Microsoft Foundry Agent Service alate u [Microsoft Foundry portalu](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) za kreiranje agenta za Rezervaciju Letova. Agent će moći komunicirati s korisnicima i pružati informacije o letovima.

## Preduvjeti

Za dovršetak ovog zadatka trebate sljedeće:
1. Azure račun s aktivnom pretplatom. [Napravite račun besplatno](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Potrebna su vam dopuštenja za stvaranje Microsoft Foundry huba ili da vam se jedan stvori.
    - Ako vam je uloga Contributor ili Owner, možete slijediti korake ovog vodiča.

## Kreiranje Microsoft Foundry huba

> **Napomena:** Microsoft Foundry je prethodno bio poznat kao Azure AI Studio.

1. Slijedite ove smjernice iz [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) blog posta za kreiranje Microsoft Foundry huba.
2. Kada je vaš projekt kreiran, zatvorite sve prikazane savjete i pregledajte stranicu projekta u Microsoft Foundry portalu, koja bi trebala izgledati slično sljedećoj slici:

    ![Microsoft Foundry Project](../../../translated_images/hr/azure-ai-foundry.88d0c35298348c2f.webp)

## Postavljanje modela

1. U lijevom izborniku za vaš projekt, u odjeljku **My assets**, odaberite stranicu **Models + endpoints**.
2. Na stranici **Models + endpoints**, u kartici **Model deployments**, u izborniku **+ Deploy model**, odaberite **Deploy base model**.
3. U pretraživanju potražite model `gpt-5-mini`, zatim ga odaberite i potvrdite.

    > **Napomena**: Smanjenje TPM-a pomaže izbjeći pretjerano korištenje kvote dostupne u vašoj pretplati.

    ![Model Deployed](../../../translated_images/hr/model-deployment.3749c53fb81e18fd.webp)

## Kreiranje agenta

Sada kada ste postavili model, možete kreirati agenta. Agent je konverzacijski AI model koji se može koristiti za interakciju s korisnicima.

1. U lijevom izborniku za vaš projekt, u odjeljku **Build & Customize**, odaberite stranicu **Agents**.
2. Kliknite **+ Create agent** za kreiranje novog agenta. U dijaloškom okviru **Agent Setup**:
    - Unesite ime agenta, na primjer `FlightAgent`.
    - Provjerite je li odabrano postavljanje modela `gpt-5-mini` koje ste prethodno kreirali
    - Postavite **Upute** prema promptu koji želite da agent prati. Evo primjera:
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
> Za detaljniji prompt, možete pogledati [ovaj repozitorij](https://github.com/ShivamGoyal03/RoamMind) za više informacija.
    
> Nadalje, možete dodati **Bazu znanja** i **Radnje** za poboljšanje sposobnosti agenta da pruži više informacija i izvršava automatizirane zadatke prema zahtjevima korisnika. Za ovaj zadatak možete preskočiti te korake.
    
![Agent Setup](../../../translated_images/hr/agent-setup.9bbb8755bf5df672.webp)

3. Za kreiranje novog multi-AI agenta jednostavno kliknite **New Agent**. Novokreirani agent će se zatim prikazati na stranici Agents.


## Testiranje agenta

Nakon što ste kreirali agenta, možete ga testirati kako biste vidjeli kako odgovara na upite korisnika u Microsoft Foundry portalu igralištu.

1. Na vrhu okna **Setup** za vašeg agenta, odaberite **Try in playground**.
2. U oknu **Playground** možete komunicirati s agentom upisivanjem upita u prozor chata. Na primjer, možete tražiti od agenta da potraži letove iz Seattlea za New York 28.

    > **Napomena**: Agent možda neće pružiti točne odgovore, budući da se u ovom zadatku ne koriste podaci u stvarnom vremenu. Cilj je testirati sposobnost agenta da razumije i odgovori na korisničke upite na temelju danih uputa.

    ![Agent Playground](../../../translated_images/hr/agent-playground.dc146586de715010.webp)

3. Nakon testiranja agenta, možete ga dodatno prilagoditi dodavanjem više namjera, trening podataka i radnji za poboljšanje njegovih sposobnosti.

## Čišćenje resursa

Kada završite s testiranjem agenta, možete ga izbrisati kako biste izbjegli dodatne troškove.
1. Otvorite [Azure portal](https://portal.azure.com) i pregledajte sadržaj grupe resursa gdje ste postavili hub resurse korištene u ovom zadatku.
2. Na alatnoj traci odaberite **Delete resource group**.
3. Unesite naziv grupe resursa i potvrdite da želite izbrisati grupu.

## Resursi

- [Dokumentacija za Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Uvod u Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Osnove AI agenata na Azureu](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->