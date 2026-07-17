# Microsoft Foundry Agent Service Development

U ovom vježbanju koristite alate Microsoft Foundry Agent Service u [Microsoft Foundry portalu](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) za stvaranje agenta za Rezervaciju letova. Agent će moći komunicirati s korisnicima i pružati informacije o letovima.

## Preduvjeti

Za dovršetak ovog vježbanja potrebni su vam sljedeći uvjeti:
1. Azure račun s aktivnom pretplatom. [Izradite račun besplatno](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Potrebne su vam dozvole za stvaranje Microsoft Foundry središta ili da vam netko drugi stvori jedno.
    - Ako ste u ulozi Suradnika ili Vlasnika, možete pratiti korake u ovom vodiču.

## Stvaranje Microsoft Foundry središta

> **Napomena:** Microsoft Foundry je ranije poznat kao Azure AI Studio.

1. Slijedite ove smjernice iz [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) blog posta za stvaranje Microsoft Foundry središta.
2. Kada je vaš projekt stvoren, zatvorite sve savjete koji se prikazuju i pregledajte stranicu projekta u Microsoft Foundry portalu, koja bi trebala izgledati slično kao na sljedećoj slici:

    ![Microsoft Foundry Project](../../../translated_images/hr/azure-ai-foundry.88d0c35298348c2f.webp)

## Postavljanje modela

1. U lijevom oknu za vaš projekt, u odjeljku **My assets**, odaberite stranicu **Models + endpoints**.
2. Na stranici **Models + endpoints**, u kartici **Model deployments**, u izborniku **+ Deploy model**, odaberite **Deploy base model**.
3. Pretražite model `gpt-4.1-mini` na popisu, zatim ga odaberite i potvrdite.

    > **Napomena**: Smanjenje TPM pomaže izbjeći prekoračenje kvote dostupne u pretplati koju koristite.

    ![Model Deployed](../../../translated_images/hr/model-deployment.3749c53fb81e18fd.webp)

## Stvaranje agenta

Sada kada ste postavili model, možete stvoriti agenta. Agent je konverzacijski AI model koji se može koristiti za komunikaciju s korisnicima.

1. U lijevom oknu za vaš projekt, u odjeljku **Build & Customize**, odaberite stranicu **Agents**.
2. Kliknite **+ Create agent** za stvaranje novog agenta. U dijaloškom okviru **Agent Setup**:
    - Unesite ime za agenta, poput `FlightAgent`.
    - Provjerite je li odabrano postavljanje modela `gpt-4.1-mini` koje ste ranije stvorili
    - Postavite **Instructions** prema uputama koje želite da agent slijedi. Evo primjera:
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
> Za detaljan prompt, pogledajte [ovaj repozitorij](https://github.com/ShivamGoyal03/RoamMind) za više informacija.
    
> Nadalje, možete dodati **Knowledge Base** i **Actions** kako biste unaprijedili mogućnosti agenta za pružanje više informacija i izvođenje automatiziranih zadataka na temelju zahtjeva korisnika. Za ovo vježbanje, ove korake možete preskočiti.
    
![Agent Setup](../../../translated_images/hr/agent-setup.9bbb8755bf5df672.webp)

3. Za stvaranje novog multi-AI agenta, jednostavno kliknite **New Agent**. Novo stvoreni agent će tada biti prikazan na stranici Agents.


## Testiranje agenta

Nakon što ste stvorili agenta, možete ga testirati da vidite kako odgovara na korisničke upite u Microsoft Foundry portalu, u okruženju za testiranje.

1. Na vrhu okna **Setup** za vašeg agenta, odaberite **Try in playground**.
2. U oknu **Playground** možete komunicirati s agentom tako da upisujete upite u prozor za chat. Na primjer, možete zamoliti agenta da pronađe letove od Seattlea do New Yorka 28-og.

    > **Napomena**: Agent možda neće dati točne odgovore jer se u ovom vježbanju ne koriste podaci u stvarnom vremenu. Svrha je testirati sposobnost agenta da razumije i odgovara na upite korisnika na temelju danih uputa.

    ![Agent Playground](../../../translated_images/hr/agent-playground.dc146586de715010.webp)

3. Nakon testiranja agenta, možete ga dodatno prilagoditi dodavanjem više namjera (intents), podataka za treniranje i akcija kako biste unaprijedili njegove mogućnosti.

## Čišćenje resursa

Kada završite s testiranjem agenta, možete ga izbrisati kako biste izbjegli dodatne troškove.
1. Otvorite [Azure portal](https://portal.azure.com) i pregledajte sadržaj grupe resursa gdje ste postavili resurse središta korištene u ovom vježbanju.
2. Na alatnoj traci odaberite **Delete resource group**.
3. Unesite ime grupe resursa i potvrdite da želite obrisati grupu.

## Resursi

- [Microsoft Foundry dokumentacija](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Početak rada s Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Osnove AI agenata na Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->