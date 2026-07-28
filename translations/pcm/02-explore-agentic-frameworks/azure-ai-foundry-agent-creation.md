# Microsoft Foundry Agent Service Development

For dis exercise, you go use Microsoft Foundry Agent Service tools for inside [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) to create agent for Flight Booking. Di agent go fit interact wit users plus give information about flights.

## Prerequisites

To fit complete dis exercise, you need dis tins:
1. Azure account wey dey active for subscription. [Create account for free](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. You gats get permissions to create Microsoft Foundry hub or make person create am for you.
    - If your role na Contributor or Owner, you fit follow steps for dis tutorial.

## Create Microsoft Foundry hub

> **Note:** Microsoft Foundry na im dem before dey call Azure AI Studio.

1. Follow dis guide straight from [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) blog post wey show how to create Microsoft Foundry hub.
2. After your project don ready, close any tip wey show and check the project page for Microsoft Foundry portal, e suppose be like dis picture:

    ![Microsoft Foundry Project](../../../translated_images/pcm/azure-ai-foundry.88d0c35298348c2f.webp)

## Deploy model

1. For the pane wey dey left for your project, for **My assets** section, choose **Models + endpoints** page.
2. For **Models + endpoints** page, go **Model deployments** tab, inside **+ Deploy model** menu, select **Deploy base model**.
3. Search for `gpt-5-mini` model for the list, then select am and confirm.

    > **Note**: Lower the TPM to avoid you dey use pass the subscription quota wey dey for your use.

    ![Model Deployed](../../../translated_images/pcm/model-deployment.3749c53fb81e18fd.webp)

## Create agent

Now as you don deploy model, you fit create agent. Agent na conversational AI model wey fit talk with users.

1. For the pane wey dey your project left side, for **Build & Customize** section, select **Agents** page.
2. Click **+ Create agent** to make new agent. For **Agent Setup** dialog box:
    - Put name for agent, like `FlightAgent`.
    - Make sure say `gpt-5-mini` model deployment wey you create before don dey selected
    - Set **Instructions** like how you want agent to follow prompt. Example dey below:
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
> If you want full detail prompt, you fit check [this repository](https://github.com/ShivamGoyal03/RoamMind) for more info.
    
> Also, you fit add **Knowledge Base** and **Actions** to make agent get more power to give more info and do automatic work based on user requests. For dis exercise, you fit skip dis steps.
    
![Agent Setup](../../../translated_images/pcm/agent-setup.9bbb8755bf5df672.webp)

3. To create new multi-AI agent, just click **New Agent**. The new agent go show for Agents page.


## Test agent

After you create agent, you fit test am to see how e respond to user questions for Microsoft Foundry portal playground.

1. For the top of **Setup** pane for your agent, choose **Try in playground**.
2. For **Playground** pane, you fit type question inside chat window to talk with agent. For example, you fit ask agent to find flight from Seattle to New York for 28th.

    > **Note**: Agent fit no give exact correct answer, because no real-time data dey for dis exercise. Purpose na to test how agent sabi understand and respond to user questions base on instructions.

    ![Agent Playground](../../../translated_images/pcm/agent-playground.dc146586de715010.webp)

3. After testing, you fit add more intents, training data, and actions to make am dey more powerful.

## Clean up resources

After you finish with testing agent, you fit delete am to make you no pay extra money.
1. Open [Azure portal](https://portal.azure.com) check the resource group wey you deploy hub resources wey you use for dis exercise.
2. For toolbar, select **Delete resource group**.
3. Enter resource group name and confirm say you wan delete am.

## Resources

- [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Getting Started with Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Fundamentals of AI agents on Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->