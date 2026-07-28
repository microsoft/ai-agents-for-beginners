# Microsoft Foundry agendi teenuse arendus

Selles harjutuses kasutate Microsoft Foundry agendi teenuse tööriistu Microsoft Foundry portaalis ([Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)) lennupiletite broneerimiseks agendi loomiseks. Agent saab suhelda kasutajatega ja anda teavet lendude kohta.

## Eeltingimused

Selle harjutuse läbimiseks vajate järgmisi asju:
1. Azure konto aktiivse tellimusega. [Loo konto tasuta](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Õigusi Microsoft Foundry keskusete loomiseks või kelleltki, kes selle teie jaoks loob.
    - Kui teie roll on Kaastöötaja või Omanik, võite järgida selles juhendis olevaid samme.

## Loo Microsoft Foundry keskus

> **Märkus:** Microsoft Foundryt nimetati varem Azure AI Studioks.

1. Järgige neid juhiseid [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) blogipostitusest Microsoft Foundry keskuse loomiseks.
2. Kui teie projekt on loodud, sulgege kõik kuvatavad näpunäited ja vaadake üle projekti leht Microsoft Foundry portaalis, mis peaks välja nägema sarnaselt järgmise pildiga:

    ![Microsoft Foundry Project](../../../translated_images/et/azure-ai-foundry.88d0c35298348c2f.webp)

## Mudeli juurutamine

1. Projekti vasakul paneelil jaotises **Minu varad** valige leht **Mudelite + lõpp-punktid**.
2. Lehel **Mudelite + lõpp-punktid**, vahekaardil **Mudeli juurutused**, menüüs **+ Juhtmurdi juurutamine**, valige **Juuruta baasmudel**.
3. Otsige nimekirjast mudel `gpt-5-mini`, valige see ja kinnitage.

    > **Märkus**: TPM-i vähendamine aitab vältida teie kasutatavas tellimuses saadaoleva limiidi liigselt kasutamist.

    ![Model Deployed](../../../translated_images/et/model-deployment.3749c53fb81e18fd.webp)

## Agendi loomine

Nüüd, kui olete mudeli juurutanud, saate luua agendi. Agent on vestluslik AI mudel, mida saab kasutada kasutajatega suhtlemiseks.

1. Projekti vasakul paneelil, jaotises **Ehita ja kohanda**, valige leht **Agendid**.
2. Klõpsake **+ Loo agent** uue agendi loomiseks. Dialoogiboksis **Agendi häälestus**:
    - Sisestage agendi nimi, näiteks `FlightAgent`.
    - Veenduge, et on valitud eelnevalt loodud `gpt-5-mini` mudeli juurutus
    - Määrake **Juhised** vastavalt juhistele, mida soovite agendi järgida. Näiteks:
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
> Täpsema juhise jaoks võite tutvuda [selle hoidla](https://github.com/ShivamGoyal03/RoamMind) lisainfoga.
    
> Lisaks saate lisada **Teadmistebaasi** ja **Tegevusi**, et täiendada agendi võimekust pakkuda rohkem teavet ja täita automatiseeritud ülesandeid kasutajate päringute põhjal. Selle harjutuse jaoks võite need sammud vahele jätta.
    
![Agent Setup](../../../translated_images/et/agent-setup.9bbb8755bf5df672.webp)

3. Uue mitme AI-agendi loomiseks klõpsake lihtsalt **Uus agent**. Värskelt loodud agent kuvatakse seejärel Agendid lehel.


## Agendi testimine

Pärast agendi loomist saate seda testida, et vaadata, kuidas see kasutajate päringutele Microsoft Foundry portaalis mänguväljakul reageerib.

1. Agendi **Häälestus** paneeli ülaosas valige **Proovi mänguväljakul**.
2. Paneelis **Mänguväljak** saate agendiga suhelda, tippides vestlusaknas päringuid. Näiteks võite paluda agendil otsida lende Seattle'ist New Yorki 28. kuupäevaks.

    > **Märkus**: Agent ei pruugi anda täpseid vastuseid, kuna selles harjutuses ei kasutata reaalajas andmeid. Eesmärk on testida agendi võimet mõista ja vastata kasutajate päringutele antud juhiste põhjal.

    ![Agent Playground](../../../translated_images/et/agent-playground.dc146586de715010.webp)

3. Pärast agendi testimist saate seda edasi kohandada, lisades rohkem kavatsusi, koolitusandmeid ja tegevusi selle võimekuse suurendamiseks.

## Ressursside koristamine

Kui olete agendi testimise lõpetanud, saate selle kustutada, et vältida lisakulutusi.
1. Avage [Azure portal](https://portal.azure.com) ja vaadake ressursigrupi sisu, kuhu juurutasite selles harjutuses kasutatud keskuse ressursid.
2. Tööriistaribal valige **Kustuta ressursirühm**.
3. Sisestage ressursigrupi nimi ja kinnitage kustutamine.

## Ressursid

- [Microsoft Foundry dokumentatsioon](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portaal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundryga alustamine](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure AI agentide põhialused](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->