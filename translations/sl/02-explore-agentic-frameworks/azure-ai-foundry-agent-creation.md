# Microsoft Foundry Agent Service Development

V tej vaji uporabite orodja Microsoft Foundry Agent Service v [Microsoft Foundry portalu](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) za ustvarjanje agenta za rezervacijo letov. Agent bo lahko komuniciral z uporabniki in zagotavljal informacije o letih.

## Predpogoji

Za dokončanje te vaje potrebujete naslednje:
1. Račun Azure z aktivno naročnino. [Ustvari račun brezplačno](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Potrebujete dovoljenja za ustvarjanje Microsoft Foundry hub-a ali pa naj ga za vas ustvari nekdo drug.
    - Če je vaša vloga Contributor ali Owner, lahko sledite korakom v tem vodiču.

## Ustvarjanje Microsoft Foundry hub-a

> **Opomba:** Microsoft Foundry je bil prej znan kot Azure AI Studio.

1. Sledite tem smernicam iz [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) bloga za ustvarjanje Microsoft Foundry hub-a.
2. Ko je vaš projekt ustvarjen, zaprite vse prikazane nasvete in preglejte stran projekta v Microsoft Foundry portalu, ki naj bi izgledala podobno kot naslednja slika:

    ![Microsoft Foundry Project](../../../translated_images/sl/azure-ai-foundry.88d0c35298348c2f.webp)

## Naložite model

1. V levem podoknu za vaš projekt, v razdelku **My assets**, izberite stran **Models + endpoints**.
2. Na strani **Models + endpoints**, na zavihku **Model deployments**, v meniju **+ Deploy model** izberite **Deploy base model**.
3. V seznamu poiščite model `gpt-5-mini`, nato ga izberite in potrdite.

    > **Opomba**: Znižanje TPM pomaga preprečiti prekomerno uporabo kvote, ki je na voljo v naročnini, ki jo uporabljate.

    ![Model Deployed](../../../translated_images/sl/model-deployment.3749c53fb81e18fd.webp)

## Ustvarite agenta

Ko ste naložili model, lahko ustvarite agenta. Agent je pogovorni AI model, ki lahko komunicira z uporabniki.

1. V levem podoknu za vaš projekt, v razdelku **Build & Customize**, izberite stran **Agents**.
2. Kliknite **+ Create agent**, da ustvarite novega agenta. V pogovornem oknu **Agent Setup**:
    - Vnesite ime za agenta, na primer `FlightAgent`.
    - Prepričajte se, da je izbran model `gpt-5-mini`, ki ste ga prej naložili
    - Nastavite **Instructions** po sporočilu, ki ga želite, da agent sledi. Tukaj je primer:
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
> Za podrobnejše sporočilo si lahko ogledate [ta repozitorij](https://github.com/ShivamGoyal03/RoamMind) za več informacij.
    
> Poleg tega lahko dodate **Knowledge Base** in **Actions** za izboljšanje zmogljivosti agenta, da zagotovi več informacij in izvaja avtomatizirane naloge na podlagi uporabniških zahtev. Za to vajo lahko te korake preskočite.
    
![Agent Setup](../../../translated_images/sl/agent-setup.9bbb8755bf5df672.webp)

3. Če želite ustvariti novega multi-AI agenta, preprosto kliknite **New Agent**. Novi agent bo nato prikazan na strani Agents.


## Preizkusite agenta

Po ustvarjanju agenta ga lahko preizkusite, kako odgovarja na uporabniške poizvedbe v Microsoft Foundry portalu na poligonu.

1. Na vrhu podokna **Setup** za vašega agenta izberite **Try in playground**.
2. V podoknu **Playground** lahko komunicirate z agentom tako, da v pogovornem oknu vnašate poizvedbe. Na primer, lahko agenta vprašate, naj poišče lete iz Seattla v New York 28. dne.

    > **Opomba**: Agent morda ne bo podal natančnih odgovorov, saj pri tej vaji ne uporabljamo podatkov v realnem času. Namen je preizkusiti zmožnost agenta, da razume in odgovori na uporabniške poizvedbe na podlagi danih navodil.

    ![Agent Playground](../../../translated_images/sl/agent-playground.dc146586de715010.webp)

3. Po preizkusu agenta ga lahko dodatno prilagodite z dodajanjem več namenov, učnih podatkov in dejanj za izboljšanje njegovih sposobnosti.

## Počistite vire

Ko zaključite s preizkusom agenta, ga lahko izbrišete, da se izognete dodatnim stroškom.
1. Odprite [Azure portal](https://portal.azure.com) in si oglejte vsebino skupine virov, kjer ste namestili vire hub-a, uporabljene v tej vaji.
2. Na orodni vrstici izberite **Delete resource group**.
3. Vnesite ime skupine virov in potrdite, da jo želite izbrisati.

## Viri

- [Microsoft Foundry dokumentacija](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Začetek z Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Osnove AI agentov na Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->