# Microsoft Foundry agento paslaugos kūrimas

Šiame pratime naudojate Microsoft Foundry agento paslaugos įrankius [Microsoft Foundry portale](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst), kad sukurtumėte agentą skrydžių rezervavimui. Agentas galės bendrauti su vartotojais ir pateikti informaciją apie skrydžius.

## Reikalavimai

Norėdami užbaigti šį pratimą, jums reikia:
1. Azure paskyros su aktyvia prenumerata. [Sukurti paskyrą nemokamai](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Leidimų sukurti Microsoft Foundry hub arba kad jums būtų sukurtas hub.
    - Jei jūsų vaidmuo yra Bendradarbis (Contributor) arba Savininkas (Owner), galite vadovautis šio vadovo veiksmais.

## Sukurkite Microsoft Foundry hub

> **Pastaba:** Microsoft Foundry anksčiau buvo žinomas kaip Azure AI Studio.

1. Sekite šias gaires iš [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) tinklaraščio įrašo, kaip sukurti Microsoft Foundry hub.
2. Kai jūsų projektas bus sukurtas, uždarykite rodomas patarimų skiltis ir peržiūrėkite projekto puslapį Microsoft Foundry portale, kuris turėtų atrodyti panašiai kaip žemiau pateiktoje nuotraukoje:

    ![Microsoft Foundry Project](../../../translated_images/lt/azure-ai-foundry.88d0c35298348c2f.webp)

## Diegti modelį

1. Kairiajame skydelyje savo projekte, skiltyje **My assets**, pasirinkite puslapį **Models + endpoints**.
2. Puslapyje **Models + endpoints**, skirtuke **Model deployments**, meniu **+ Deploy model** pasirinkite **Deploy base model**.
3. Suraskite sąraše modelį `gpt-4.1-mini`, pasirinkite jį ir patvirtinkite.

    > **Pastaba**: TPM sumažinimas padeda išvengti per daug sunaudojamos jūsų prenumeratai skirtos kvotos.

    ![Model Deployed](../../../translated_images/lt/model-deployment.3749c53fb81e18fd.webp)

## Sukurkite agentą

Dabar, kai modelis įdiegtas, galite sukurti agentą. Agentas yra pokalbių AI modelis, kuris gali bendrauti su vartotojais.

1. Kairiajame skydelyje savo projekte, skiltyje **Build & Customize**, pasirinkite puslapį **Agents**.
2. Spauskite **+ Create agent**, kad sukurtumėte naują agentą. Dialogo lange **Agent Setup**:
    - Įveskite agento pavadinimą, pvz., `FlightAgent`.
    - Įsitikinkite, kad pasirinktas anksčiau sukurtas `gpt-4.1-mini` modelio diegimas.
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
> Daugiau informacijos apie išsamų prašymą galite rasti [šiame repozitoriume](https://github.com/ShivamGoyal03/RoamMind).
    
> Be to, galite pridėti **Knowledge Base** ir **Actions**, kad pagerintumėte agento galimybes teikti daugiau informacijos ir atlikti automatizuotas užduotis pagal vartotojo užklausas. Šiam pratimui šių žingsnių galite praleisti.
    
![Agent Setup](../../../translated_images/lt/agent-setup.9bbb8755bf5df672.webp)

3. Norėdami sukurti naują multi-AI agentą, paprasčiausiai spauskite **New Agent**. Naujai sukurtas agentas bus rodomas Agents puslapyje.


## Išbandykite agentą

Sukūrę agentą, galite jį išbandyti, kaip jis reaguoja į vartotojų užklausas Microsoft Foundry portalo žaidimų aikštelėje.

1. Viršuje skiltyje **Setup** savo agentui pasirinkite **Try in playground**.
2. **Playground** skydelyje galite bendrauti su agentu rašydami užklausas pokalbių lange. Pavyzdžiui, galite paprašyti agento ieškoti skrydžių iš Sietlo į Niujorką 28 dienai.

    > **Pastaba**: Agentas gali nepateikti tikslių atsakymų, nes šiame pratime nenaudojami realaus laiko duomenys. Pagrindinis tikslas – išbandyti agento gebėjimą suprasti ir atsakyti į vartotojo užklausas pagal pateiktas instrukcijas.

    ![Agent Playground](../../../translated_images/lt/agent-playground.dc146586de715010.webp)

3. Išbandę agentą, galite toliau jį pritaikyti pridėdami daugiau ketinimų, mokymo duomenų ir veiksmų, kad pagerintumėte jo galimybes.

## Išvalykite išteklius

Baigę testuoti agentą, galite jį ištrinti, kad išvengtumėte papildomų išlaidų.
1. Atidarykite [Azure portalą](https://portal.azure.com) ir peržiūrėkite išteklių grupės turinį, kur įdiegėte šiame pratime naudotus hub išteklius.
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