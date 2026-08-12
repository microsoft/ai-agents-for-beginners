# Maendeleo ya Huduma ya Wakala wa Microsoft Foundry

Katika zoezi hili, unatumia zana za Huduma ya Wakala wa Microsoft Foundry katika [mlango wa Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) kuunda wakala kwa ajili ya Uhifadhi wa Ndege. Wakala huyo ataweza kuwasiliana na watumiaji na kutoa taarifa kuhusu ndege.

## Mambo yanayohitajika

Ili kumaliza zoezi hili, unahitaji yafuatayo:
1. Akaunti ya Azure yenye usajili unaoendelea. [Tengeneza akaunti bure](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Unahitaji ruhusa za kuunda kitovu cha Microsoft Foundry au kuwa na kimoja kilichoundwa kwa niaba yako.
    - Ikiwa nafasi yako ni Mchangiaji au Mwenyeji, unaweza kufuata hatua katika mafunzo haya.

## Unda kitovu cha Microsoft Foundry

> **Kumbuka:** Microsoft Foundry awali ilijulikana kama Azure AI Studio.

1. Fuata miongozo hii kutoka kwa chapisho la blogu la [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) kwa ajili ya kuunda kitovu cha Microsoft Foundry.
2. Wakati mradi wako umetengenezwa, funga vidokezo vyote vinavyoonekana na pitia ukurasa wa mradi katika mlango wa Microsoft Foundry, ambao unatakiwa kuonekana kama picha ifuatayo:

    ![Mradi wa Microsoft Foundry](../../../translated_images/sw/azure-ai-foundry.88d0c35298348c2f.webp)

## Sambaza mfano

1. Katika dirisha la kushoto kwa mradi wako, kwenye sehemu ya **My assets**, chagua ukurasa wa **Models + endpoints**.
2. Katika ukurasa wa **Models + endpoints**, katika kichupo cha **Model deployments**, kwenye menyu ya **+ Deploy model**, chagua **Deploy base model**.
3. Tafuta mfano `gpt-5-mini` katika orodha, halafu uchague na uthibitishe.

    > **Kumbuka**: Kupunguza TPM husaidia kuepuka matumizi ya kiasi cha leseni kinachopatikana katika usajili unaotumia.

    ![Mfano Umesambazwa](../../../translated_images/sw/model-deployment.3749c53fb81e18fd.webp)

## Unda wakala

Sasa umeeneza mfano, unaweza kuunda wakala. Wakala ni mfano wa AI wa mazungumzo ambao unaweza kutumika kuwasiliana na watumiaji.

1. Katika dirisha la kushoto kwa mradi wako, kwenye sehemu ya **Build & Customize**, chagua ukurasa wa **Agents**.
2. Bonyeza **+ Create agent** kuunda wakala mpya. Katika kisanduku cha mazungumzo cha **Agent Setup**:
    - Ingiza jina la wakala, kama `FlightAgent`.
    - Hakikisha kuwa usambazaji wa mfano wa `gpt-5-mini` ulio undwa awali umechaguliwa
    - Weka **Maelekezo** kwa mujibu wa agizo unalotaka wakala afuate. Hapa kuna mfano:
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
> Kwa agizo la kina, unaweza kuangalia [hazina hii](https://github.com/ShivamGoyal03/RoamMind) kwa maelezo zaidi.
    
> Zaidi ya hayo, unaweza kuongeza **Knowledge Base** na **Actions** kuboresha uwezo wa wakala kutoa taarifa zaidi na kufanya kazi za kiotomatiki kulingana na maombi ya watumiaji. Kwa zoezi hili, unaweza kupuuza hatua hizi.
    
![Saa ya Wakala](../../../translated_images/sw/agent-setup.9bbb8755bf5df672.webp)

3. Kuunda wakala mpya wa AI nyingi, bonyeza tu **New Agent**. Wakala mpya atajitokeza kwa ukurasa wa Wakala.


## Jaribu wakala

Baada ya kuunda wakala, unaweza kujaribu kuona jinsi anavyotoa majibu kwa maswali ya watumiaji katika eneo la majaribio la mlango wa Microsoft Foundry.

1. Juu ya dirisha la **Setup** kwa wakala wako, chagua **Try in playground**.
2. Katika dirisha la **Playground**, unaweza kuwasiliana na wakala kwa kuandika maswali katika dirisha la mazungumzo. Kwa mfano, unaweza kumuuliza wakala kutafuta ndege kutoka Seattle kwenda New York tarehe 28.

    > **Kumbuka**: Wakala huenda asitoe majibu sahihi, kwa kuwa hakuna data ya wakati halisi inayotumika katika zoezi hili. Kusudio ni kujaribu uwezo wa wakala kuelewa na kujibu maswali ya watumiaji kulingana na maelekezo yaliyotolewa.

    ![Eneo la Wakala](../../../translated_images/sw/agent-playground.dc146586de715010.webp)

3. Baada ya kujaribu wakala, unaweza kuongeza zaidi kwa kuongeza nia, data za mafunzo, na vitendo kuboresha uwezo wake.

## Safisha rasilimali

Unapomaliza kujaribu wakala, unaweza kuifuta ili kuepuka gharama za ziada.
1. Fungua [mlango wa Azure](https://portal.azure.com) na tazama yaliyomo katika kikundi cha rasilimali ambapo ulisambaza rasilimali za kitovu zinazotumika katika zoezi hili.
2. Kwenye upau wa zana, chagua **Delete resource group**.
3. Ingiza jina la kikundi cha rasilimali na uthibitishe unataka kuifuta.

## Rasilimali

- [Nyaraka za Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Mlango wa Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Anza na Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Misingi ya mawakala wa AI kwenye Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->