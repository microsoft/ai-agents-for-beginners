# Vývoj služby Microsoft Foundry Agent

V tomto cvičení použijete nástroje služby Microsoft Foundry Agent Service v [Microsoft Foundry portálu](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) k vytvoření agenta pro rezervaci letů. Agent bude schopen komunikovat s uživateli a poskytovat informace o letech.

## Požadavky

K dokončení tohoto cvičení potřebujete:
1. Azure účet s aktivním předplatným. [Vytvořte si účet zdarma](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Máte oprávnění ke vytvoření Microsoft Foundry hubu nebo je pro vás vytvořen.
    - Pokud je vaše role Přispěvatel nebo Vlastník, můžete postupovat podle kroků v tomto návodu.

## Vytvoření Microsoft Foundry hubu

> **Poznámka:** Microsoft Foundry byl dříve známý jako Azure AI Studio.

1. Postupujte podle pokynů z [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) blogu pro vytvoření Microsoft Foundry hubu.
2. Po vytvoření projektu zavřete všechny zobrazené tipy a prohlédněte si stránku projektu v Microsoft Foundry portálu, která by měla vypadat podobně jako na následujícím obrázku:

    ![Microsoft Foundry Project](../../../translated_images/cs/azure-ai-foundry.88d0c35298348c2f.webp)

## Nasazení modelu

1. V levém panelu vašeho projektu v sekci **My assets** vyberte stránku **Models + endpoints**.
2. Na stránce **Models + endpoints**, v záložce **Model deployments**, v nabídce **+ Deploy model** vyberte **Deploy base model**.
3. Vyhledejte model `gpt-5-mini` v seznamu, poté jej vyberte a potvrďte.

    > **Poznámka**: Snížení TPM pomáhá zabránit nadměrnému využití kvóty v rámci používaného předplatného.

    ![Model Deployed](../../../translated_images/cs/model-deployment.3749c53fb81e18fd.webp)

## Vytvoření agenta

Nyní, když jste nasadili model, můžete vytvořit agenta. Agent je konverzační model umělé inteligence, který může komunikovat s uživateli.

1. V levém panelu vašeho projektu v sekci **Build & Customize** vyberte stránku **Agents**.
2. Klikněte na **+ Create agent** pro vytvoření nového agenta. V dialogovém okně **Agent Setup**:
    - Zadejte jméno pro agenta, například `FlightAgent`.
    - Ujistěte se, že je vybráno nasazení modelu `gpt-5-mini`, které jste vytvořili dříve.
    - Nastavte **Instructions** podle pokynů, které chcete, aby agent dodržoval. Zde je příklad:
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
> Pro podrobnější prompt si můžete prohlédnout [tento repozitář](https://github.com/ShivamGoyal03/RoamMind) pro více informací.
    
> Dále můžete přidat **Knowledge Base** a **Actions** pro rozšíření schopností agenta poskytovat více informací a vykonávat automatizované úkoly na základě požadavků uživatelů. Pro toto cvičení můžete tyto kroky přeskočit.
    
![Agent Setup](../../../translated_images/cs/agent-setup.9bbb8755bf5df672.webp)

3. Pro vytvoření nového multi-AI agenta jednoduše klikněte na **New Agent**. Nově vytvořený agent se zobrazí na stránce Agents.


## Testování agenta

Po vytvoření agenta ho můžete otestovat, jak reaguje na dotazy uživatelů v Microsoft Foundry portálovém playgroundu.

1. V horní části panelu **Setup** vašeho agenta vyberte **Try in playground**.
2. V panelu **Playground** můžete komunikovat s agentem zadáváním dotazů do chatovacího okna. Například můžete požádat agenta, aby vyhledal lety ze Seattlu do New Yorku na 28. datum.

    > **Poznámka**: Agent nemusí poskytovat přesné odpovědi, protože v tomto cvičení nejsou použita žádná data v reálném čase. Účelem je otestovat schopnost agenta porozumět a reagovat na dotazy uživatelů na základě zadaných pokynů.

    ![Agent Playground](../../../translated_images/cs/agent-playground.dc146586de715010.webp)

3. Po testování agenta ho můžete dále přizpůsobit přidáním více záměrů, tréninkových dat a akcí pro zvýšení jeho schopností.

## Vyčištění zdrojů

Po dokončení testování agenta jej můžete odstranit, abyste se vyhnuli dalším nákladům.
1. Otevřete [Azure portál](https://portal.azure.com) a zobrazte obsah skupiny prostředků, kde jste nasadili zdroje hubu použité v tomto cvičení.
2. Na panelu nástrojů vyberte **Delete resource group**.
3. Zadejte název skupiny prostředků a potvrďte její smazání.

## Zdroje

- [Dokumentace Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portál](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Začínáme s Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Základy AI agentů na Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->