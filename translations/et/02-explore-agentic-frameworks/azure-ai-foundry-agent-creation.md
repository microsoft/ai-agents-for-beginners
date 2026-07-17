# Microsoft Foundry Agent Teenuse Arendamine

Selles harjutuses kasutate Microsoft Foundry Agent Teenuse tööriistu [Microsoft Foundry portaali](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) kaudu, et luua agent lennupiletite broneerimiseks. Agent saab kasutajatega suhelda ja pakkuda teavet lendude kohta.

## Nõuded

Selle harjutuse läbimiseks vajate järgmist:
1. Azure'i konto aktiivse tellimusega. [Loo konto tasuta](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Teil peavad olema õigused Microsoft Foundry keskuse loomiseks või keegi peab selle teie jaoks loonud olema.
    - Kui teie roll on Kaastööline või Omanik, saate järgida selle õppematerjali samme.

## Microsoft Foundry keskuse loomine

> **Märkus:** Microsoft Foundry oli varem tuntud kui Azure AI Studio.

1. Järgige neid juhiseid [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) blogipostitusest Microsoft Foundry keskuse loomiseks.
2. Kui teie projekt on loodud, sulgege kuvatud näpunäited ja vaadake Microsoft Foundry portaali projektilehte, mis peaks välja nägema sarnaselt järgmisele pildile:

    ![Microsoft Foundry Project](../../../translated_images/et/azure-ai-foundry.88d0c35298348c2f.webp)

## Mudeli juurutamine

1. Vasakpoolses paneelis oma projekti juures valige jaotises **Minu varad** leht **Mudelite + lõpp-punktid**.
2. Lehel **Mudelite + lõpp-punktid**, vahekaardil **Mudeli juurutamine**, valige menüüst **+ Uueta mudel** suvand **Uuenda alammudelit**.
3. Otsige nimekirjast mudel `gpt-4.1-mini`, valige see ja kinnitage.

    > **Märkus**: TPM-i vähendamine aitab vältida teie kasutatava tellimuse kvota ülekoormamist.

    ![Model Deployed](../../../translated_images/et/model-deployment.3749c53fb81e18fd.webp)

## Agendi loomine

Nüüd, kui olete mudeli juurutanud, saate luua agendi. Agent on vestluslik AI mudel, mida saab kasutada kasutajatega suhtlemiseks.

1. Vasakpoolses paneelis oma projekti juures valige jaotises **Ehita ja kohanda** leht **Agendid**.
2. Klõpsake **+ Loo agent** uue agendi loomiseks. Dialoogiboksis **Agendi häälestus**:
    - Sisestage agendi nimi, näiteks `FlightAgent`.
    - Veenduge, et valitud on eelnevalt loodud mudeli juurutus `gpt-4.1-mini`.
    - Määrake **Juhendid** vastavalt käsule, mida soovite, et agent järgiks. Näide:
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
> Täpsema käsu jaoks vaadake [seda repositooriumi](https://github.com/ShivamGoyal03/RoamMind) lisateabe saamiseks.
    
> Ühtlasi saate lisada **Teadmistebaasi** ja **Tegevusi**, et laiendada agendi võimekust pakkuda rohkem teavet ja sooritada automaatseid toiminguid kasutajapäringute põhjal. Selle harjutuse jaoks võite need sammud vahele jätta.
    
![Agent Setup](../../../translated_images/et/agent-setup.9bbb8755bf5df672.webp)

3. Uue mitme AI agenti loomiseks klõpsake lihtsalt **Uus agent**. Värskelt loodud agent kuvatakse seejärel Agendi lehel.


## Agendi testimine

Pärast agendi loomist saate seda testida, et näha, kuidas ta kasutajate päringutele Microsoft Foundry portaali mänguväljakul vastab.

1. Agendi **Häälestus** paneeli ülaosas valige **Proovi mänguväljakul**.
2. Mänguväljaku paneelis saate agendiga suhelda, sisestades päringuid vestlusaknasse. Näiteks võite paluda agendil otsida lende Seattle'ist New Yorki 28. kuupäevaks.

    > **Märkus**: Agen til ei pruugi anda täpseid vastuseid, kuna selles harjutuses ei kasutata reaalajas andmeid. Eesmärk on testida agendi võimet mõista ja vastata kasutajate päringutele antud juhiste põhjal.

    ![Agent Playground](../../../translated_images/et/agent-playground.dc146586de715010.webp)

3. Pärast agendi testimist võite seda veelgi kohandada, lisades rohkem kavatsusi, koolitusandmeid ja tegevusi selle võimekuse suurendamiseks.

## Ressursside puhastamine

Kui olete agendi testimise lõpetanud, saate selle kustutada, et vältida täiendavaid kulutusi.
1. Avage [Azure portaali](https://portal.azure.com) ja vaadake haru rühma sisu, kuhu te juurutasite selle harjutuse jaoks kasutatud keskuse ressursid.
2. Tööriistaribal valige **Kustuta ressursirühm**.
3. Sisestage ressursirühma nimi ja kinnitage selle kustutamine.

## Ressursid

- [Microsoft Foundry dokumentatsioon](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portaal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundryga alustamine](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [AI agentide alused Azure'is](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->