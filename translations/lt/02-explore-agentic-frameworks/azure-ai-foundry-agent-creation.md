# Microsoft Foundry agento paslaugos kūrimas

Šioje užduotyje naudojate Microsoft Foundry Agent Service įrankius [Microsoft Foundry portale](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst), kad sukurtumėte agentą skrydžių rezervacijai. Agentas galės bendrauti su vartotojais ir teikti informaciją apie skrydžius.

## Prieš pradedant

Norėdami atlikti šią užduotį, jums reikės:
1. Azure paskyros su aktyvia prenumerata. [Sukurkite paskyrą nemokamai](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Leidimų sukurti Microsoft Foundry centrą arba kad jis būtų sukurtas jums.
    - Jei jūsų vaidmuo yra Bendradarbis (Contributor) arba Savininkas (Owner), galite sekti šio vadovo žingsnius.

## Sukurkite Microsoft Foundry centrą

> **Pastaba:** Microsoft Foundry anksčiau buvo žinomas kaip Azure AI Studio.

1. Vadovaukitės šiais nurodymais iš [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) tinklaraščio įrašo, kaip susikurti Microsoft Foundry centrą.
2. Kai jūsų projektas bus sukurtas, uždarykite rodomas patarimų korteles ir peržiūrėkite projekto puslapį Microsoft Foundry portale, kuris turėtų atrodyti panašiai kaip parodyta žemiau:

    ![Microsoft Foundry Projektas](../../../translated_images/lt/azure-ai-foundry.88d0c35298348c2f.webp)

## Įdiekite modelį

1. Kairėje projekto srityje, skyriuje **My assets**, pasirinkite puslapį **Models + endpoints**.
2. Puslapyje **Models + endpoints**, skirtuke **Model deployments**, meniu **+ Deploy model** pasirinkite **Deploy base model**.
3. Suraskite `gpt-5-mini` modelį sąraše, pasirinkite jį ir patvirtinkite.

    > **Pastaba**: Sumažinus TPM, padedama išvengti per didelio prenumeratos kvotos sunaudojimo.

    ![Modelio diegimas](../../../translated_images/lt/model-deployment.3749c53fb81e18fd.webp)

## Sukurkite agentą

Dabar, kai įdiegėte modelį, galite sukurti agentą. Agentas yra pokalbių AI modelis, kurį galima naudoti bendraujant su vartotojais.

1. Kairėje projekto srityje, skyriuje **Build & Customize**, pasirinkite puslapį **Agents**.
2. Spustelėkite **+ Create agent**, kad sukurtumėte naują agentą. Atidariame laukelyje **Agent Setup**:
    - Įveskite agento pavadinimą, pvz., `FlightAgent`.
    - Užtikrinkite, kad būtų pasirinktas anksčiau sukurtas `gpt-5-mini` modelio diegimas.
    - Nustatykite **Instructions** pagal užduotį, kurios norite, kad agentas laikytųsi. Štai pavyzdys:
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
> Išsamesnei užduočiai galite pasitikrinti [šiame repozitoriume](https://github.com/ShivamGoyal03/RoamMind) daugiau informacijos.
    
> Be to, galite pridėti **Knowledge Base** ir **Actions**, kad pagerintumėte agente funkcionalumą teikti daugiau informacijos ir atlikti automatinius veiksmus pagal vartotojo užklausas. Šioje užduotyje tai galima praleisti.
    
![Agent Setup](../../../translated_images/lt/agent-setup.9bbb8755bf5df672.webp)

3. Norėdami sukurti naują daugialypį AI agentą, tiesiog spustelėkite **New Agent**. Naujas agentas bus rodomas Agents puslapyje.


## Testuokite agentą

Sukūrę agentą, galite jį išbandyti, kaip jis atsako į vartotojo užklausas Microsoft Foundry portalo žaidimų aikštelėje.

1. Viršuje jūsų agento **Setup** srityje pasirinkite **Try in playground**.
2. Žaidimų aikštelės srityje galite bendrauti su agentu, rašydami užklausas pokalbių lange. Pavyzdžiui, galite paklausti agento, kad jis surastų skrydžius iš Sietlo į Niujorką 28 dienai.

    > **Pastaba**: Agentas gali nesuteikti tikslių atsakymų, nes šioje užduotyje nenaudojami realaus laiko duomenys. Tikslas yra ištestuoti agento gebėjimą suprasti ir atsakyti į vartotojo užklausas pagal pateiktas instrukcijas.

    ![Agent Play ground](../../../translated_images/lt/agent-playground.dc146586de715010.webp)

3. Išbandžius agentą, galite toliau jį pritaikyti pridėdami daugiau ketinimų (intents), mokomųjų duomenų ir veiksmų, kad pagerintumėte jo galimybes.

## Išvalykite išteklius

Baigę testuoti agentą, galite jį pašalinti, kad išvengtumėte papildomų išlaidų.
1. Atidarykite [Azure portalą](https://portal.azure.com) ir peržiūrėkite išteklių grupę, kurioje diegėte centro išteklius, naudotus šioje užduotyje.
2. Įrankių juostoje pasirinkite **Delete resource group**.
3. Įveskite išteklių grupės pavadinimą ir patvirtinkite, kad norite ją ištrinti.

## Ištekliai

- [Microsoft Foundry dokumentacija](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portalas](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Pradžia su Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [AI agentų pagrindai Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->