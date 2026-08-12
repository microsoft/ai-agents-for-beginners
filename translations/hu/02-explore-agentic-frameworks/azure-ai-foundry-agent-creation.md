# Microsoft Foundry Ügynök Szolgáltatás Fejlesztése

Ebben a gyakorlatban a Microsoft Foundry Ügynök Szolgáltatás eszközeit használja a [Microsoft Foundry portálon](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) egy repülőjegyfoglalási ügynök létrehozásához. Az ügynök képes lesz interakcióba lépni a felhasználókkal és információkat nyújtani a járatokról.

## Előfeltételek

A gyakorlat elvégzéséhez a következőkre van szükség:
1. Egy Azure fiók aktív előfizetéssel. [Hozzon létre egy fiókot ingyen](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Jogosultság a Microsoft Foundry hub létrehozásához, vagy egy már létrehozott hub.
    - Ha az Ön szerepe Közreműködő vagy Tulajdonos, akkor kövesse a bemutató lépéseit.

## Microsoft Foundry hub létrehozása

> **Megjegyzés:** A Microsoft Foundry korábban Azure AI Studio néven volt ismert.

1. Kövesse ezeket az irányelveket a [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) blogbejegyzéséből egy Microsoft Foundry hub létrehozásához.
2. Miután a projektje létrejött, zárja be a megjelenő tippeket, és tekintse át a Microsoft Foundry portál projektoldalát, amely hasonló lesz a következő képhez:

    ![Microsoft Foundry Project](../../../translated_images/hu/azure-ai-foundry.88d0c35298348c2f.webp)

## Modell telepítése

1. A bal oldali panelen a projektjénél a **My assets** szakaszban válassza ki a **Models + endpoints** oldalt.
2. A **Models + endpoints** oldalon, a **Model deployments** fülön, a **+ Deploy model** menüben válassza a **Deploy base model** lehetőséget.
3. Keresse meg a `gpt-5-mini` modellt a listában, majd válassza ki és erősítse meg.

    > **Megjegyzés**: A TPM csökkentése segít elkerülni az előfizetésben rendelkezésre álló kvóta túlzott használatát.

    ![Model Deployed](../../../translated_images/hu/model-deployment.3749c53fb81e18fd.webp)

## Ügynök létrehozása

Miután telepítette a modellt, létrehozhat egy ügynököt. Az ügynök egy beszélgető AI modell, amely felhasználókkal való interakcióra használható.

1. A bal oldali panelen a projektjénél a **Build & Customize** szakaszban válassza az **Agents** oldalt.
2. Kattintson a **+ Create agent** gombra egy új ügynök létrehozásához. Az **Agent Setup** párbeszédpanelen:
    - Adjon meg egy nevet az ügynöknek, például `FlightAgent`.
    - Győződjön meg róla, hogy a korábban létrehozott `gpt-5-mini` modell telepítése kiválasztott.
    - Állítsa be az **Instructions** részt a követendő utasítások alapján. Itt egy példa:
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
> A részletes promptért tekintse meg [ezt a tárolót](https://github.com/ShivamGoyal03/RoamMind) további információkért.
    
> Továbbá hozzáadhat **Ismeretbázist** és **Műveleteket**, hogy bővítse az ügynök képességeit több információ szolgáltatására és automatizált feladatok végrehajtására a felhasználói kérések alapján. Ebben a gyakorlatban ezeket a lépéseket kihagyhatja.
    
![Agent Setup](../../../translated_images/hu/agent-setup.9bbb8755bf5df672.webp)

3. Egy új multi-AI ügynök létrehozásához egyszerűen kattintson a **New Agent** gombra. Az újonnan létrehozott ügynök meg fog jelenni az Agents oldalon.


## Ügynök tesztelése

Az ügynök létrehozása után tesztelheti, hogy hogyan válaszol a felhasználói kérdésekre a Microsoft Foundry portál játékterében.

1. Az ügynök **Setup** paneljének tetején válassza a **Try in playground** lehetőséget.
2. A **Playground** panelen érintkezhet az ügynökkel, kérdéseket írva a chat ablakba. Például kérheti az ügynököt, hogy keressen járatokat Seattle és New York között a 28-ai napra.

    > **Megjegyzés**: Az ügynök nem feltétlenül fog pontos válaszokat adni, mivel ebben a gyakorlatban nem használunk valós idejű adatokat. A cél az, hogy teszteljük az ügynök képességét a felhasználói kérdések megértésére és válaszadására a megadott utasítások alapján.

    ![Agent Playground](../../../translated_images/hu/agent-playground.dc146586de715010.webp)

3. A tesztelés után tovább testreszabhatja az ügynököt további szándékok, tréningadatok és műveletek hozzáadásával, hogy fejlessze a képességeit.

## Erőforrások tisztítása

Miután befejezte az ügynök tesztelését, törölheti azt a további költségek elkerülése érdekében.
1. Nyissa meg az [Azure portált](https://portal.azure.com), és tekintse meg annak az erőforráscsoportnak a tartalmát, ahol a hub erőforrásait telepítette a gyakorlat során.
2. Az eszköztáron válassza a **Delete resource group** lehetőséget.
3. Írja be az erőforráscsoport nevét, és erősítse meg a törlést.

## Erőforrások

- [Microsoft Foundry dokumentáció](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portál](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Kezdő lépések a Microsoft Foundry-val](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Az AI ügynökök alapjai az Azure-on](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->