# Microsoft Foundry Agent Service-utveckling

I den här övningen använder du verktygen för Microsoft Foundry Agent Service i [Microsoft Foundry-portalen](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) för att skapa en agent för flygbokning. Agenten kommer att kunna interagera med användare och tillhandahålla information om flyg.

## Förutsättningar

För att slutföra denna övning behöver du följande:
1. Ett Azure-konto med en aktiv prenumeration. [Skapa ett konto gratis](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Du behöver behörigheter för att skapa en Microsoft Foundry-hubb eller ha en skapad åt dig.
    - Om din roll är Bidragsgivare eller Ägare kan du följa stegen i denna handledning.

## Skapa en Microsoft Foundry-hubb

> **Notera:** Microsoft Foundry var tidigare känt som Azure AI Studio.

1. Följ riktlinjerna från [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) bloggpost för att skapa en Microsoft Foundry-hubb.
2. När ditt projekt är skapat, stäng eventuella tips som visas och granska projektsidan i Microsoft Foundry-portalen, som bör se ut ungefär som på bilden nedan:

    ![Microsoft Foundry Project](../../../translated_images/sv/azure-ai-foundry.88d0c35298348c2f.webp)

## Distribuera en modell

1. I rutan till vänster för ditt projekt, under avsnittet **Mina tillgångar**, välj sidan **Modeller + slutpunkter**.
2. På sidan **Modeller + slutpunkter**, under fliken **Modelldistributioner**, i menyn **+ Distribuera modell**, välj **Distribuera basmodell**.
3. Sök efter modellen `gpt-5-mini` i listan, välj den och bekräfta.

    > **Notera**: Att minska TPM hjälper till att undvika att överskrida den kvot som finns i den prenumeration du använder.

    ![Model Deployed](../../../translated_images/sv/model-deployment.3749c53fb81e18fd.webp)

## Skapa en agent

Nu när du har distribuerat en modell kan du skapa en agent. En agent är en konversationsbaserad AI-modell som kan användas för att interagera med användare.

1. I rutan till vänster för ditt projekt, under avsnittet **Bygg & Anpassa**, välj sidan **Agenter**.
2. Klicka på **+ Skapa agent** för att skapa en ny agent. Under dialogrutan **Agentinstallation**:
    - Ange ett namn för agenten, till exempel `FlightAgent`.
    - Kontrollera att den tidigare skapade modell-distributionen `gpt-5-mini` är vald.
    - Ange **Instruktioner** enligt den prompt du vill att agenten ska följa. Här är ett exempel:
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
> För en detaljerad prompt kan du titta på [detta arkiv](https://github.com/ShivamGoyal03/RoamMind) för mer information.
    
> Dessutom kan du lägga till **Kunskapsbas** och **Åtgärder** för att förbättra agentens förmåga att ge mer information och utföra automatiserade uppgifter baserat på användarens önskemål. För denna övning kan du hoppa över dessa steg.
    
![Agent Setup](../../../translated_images/sv/agent-setup.9bbb8755bf5df672.webp)

3. För att skapa en ny multi-AI-agent, klicka helt enkelt på **Ny agent**. Den nyss skapade agenten kommer då att visas på sidan Agenter.


## Testa agenten

Efter att ha skapat agenten kan du testa den för att se hur den svarar på användarfrågor i Microsoft Foundry-portals lekplats.

1. Överst i **Installations**panelen för din agent väljer du **Testa i lekplats**.
2. I **Lekplats**-panelen kan du interagera med agenten genom att skriva frågor i chattfönstret. Till exempel kan du be agenten att söka efter flyg från Seattle till New York den 28:e.

    > **Notera**: Agenten kan ge inexakta svar eftersom ingen realtidsdata används i den här övningen. Syftet är att testa agentens förmåga att förstå och svara på användarfrågor baserat på de angivna instruktionerna.

    ![Agent Playground](../../../translated_images/sv/agent-playground.dc146586de715010.webp)

3. Efter att ha testat agenten kan du anpassa den ytterligare genom att lägga till fler avsikter, träningsdata och åtgärder för att förbättra dess kapacitet.

## Rensa resurser

När du är klar med att testa agenten kan du ta bort den för att undvika ytterligare kostnader.
1. Öppna [Azure-portalen](https://portal.azure.com) och visa innehållet i resursgruppen där du distribuerade hubbresurserna som användes i denna övning.
2. På verktygsfältet väljer du **Ta bort resursgrupp**.
3. Ange resursgruppens namn och bekräfta att du vill ta bort den.

## Resurser

- [Microsoft Foundry-dokumentation](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry-portalen](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Kom igång med Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Grundläggande om AI-agenter på Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->