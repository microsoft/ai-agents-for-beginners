# Microsoft Foundry Agent -palvelun kehittäminen

Tässä harjoituksessa käytät Microsoft Foundry Agent -palvelun työkaluja [Microsoft Foundry -portaalissa](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) luodaksesi agentin lentovarauksia varten. Agentti pystyy keskustelemaan käyttäjien kanssa ja tarjoamaan tietoja lennoista.

## Esivaatimukset

Tätä harjoitusta varten tarvitset seuraavat asiat:
1. Azure-tilin, jossa on aktiivinen tilaus. [Luo tili ilmaiseksi](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Sinulla tulee olla oikeudet luoda Microsoft Foundry -keskus tai sellainen on luotava sinulle.
    - Jos roolisi on Avustaja (Contributor) tai Omistaja (Owner), voit seurata tämän opetusohjelman ohjeita.

## Luo Microsoft Foundry -keskus

> **Huom:** Microsoft Foundry tunnettiin aiemmin nimellä Azure AI Studio.

1. Noudata näitä ohjeita Microsoft Foundry -blogikirjoituksesta [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) luodaksesi Microsoft Foundry -keskuksen.
2. Kun projektisi on luotu, sulje mahdolliset ohjevinkit ja tutustu Microsoft Foundry -portaalin projektisivuun, joka näyttää suunnilleen tältä:

    ![Microsoft Foundry Project](../../../translated_images/fi/azure-ai-foundry.88d0c35298348c2f.webp)

## Ota malli käyttöön

1. Valitse projektisi vasemman puolen ruudusta **Omat omaisuudet** -osiossa **Mallit + päätelasemat** -sivu.
2. Valitse **Mallit + päätelasemat** -sivulla **Mallin käyttöönotot** -välilehdeltä valikosta **+ Ota malli käyttöön** ja valitse **Ota perustamalli käyttöön**.
3. Etsi listasta `gpt-5-mini`-malli, valitse se ja vahvista.

    > **Huom**: TPM-arvon pienentäminen auttaa välttämään tilauksessasi olevan kiintiön liiallista käyttöä.

    ![Model Deployed](../../../translated_images/fi/model-deployment.3749c53fb81e18fd.webp)

## Luo agentti

Kun malli on otettu käyttöön, voit luoda agentin. Agentti on keskusteleva tekoälymalli, jota voidaan käyttää vuorovaikutuksessa käyttäjien kanssa.

1. Valitse vasemman puolen ruudusta projektissasi **Rakenna ja mukauta** -osiosta **Agentit**-sivu.
2. Klikkaa **+ Luo agentti** luodaksesi uuden agentin. Agentin asetukset -valintaikkunassa:
    - Anna agentille nimi, esimerkiksi `FlightAgent`.
    - Varmista, että aiemmin luomasi `gpt-5-mini` -mallin käyttöönotto on valittuna.
    - Aseta **Ohjeet** sen kehotteen mukaan, jota haluat agentin noudattavan. Tässä on esimerkki:
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
> Tarkemman kehotteen löydät [tästä arkistosta](https://github.com/ShivamGoyal03/RoamMind).
    
> Lisäksi voit lisätä **Tietopohjan** ja **Toiminnot** antaaksesi agentille lisää kykyjä tarjota tietoa ja suorittaa automaattisia tehtäviä käyttäjän pyyntöihin perustuen. Tässä harjoituksessa nämä vaiheet voi ohittaa.
    
![Agent Setup](../../../translated_images/fi/agent-setup.9bbb8755bf5df672.webp)

3. Luo uusi monitekoälyagentti napsauttamalla **Uusi agentti**. Uusi agentti näkyy sitten agenttisivulla.


## Testaa agenttia

Agentin luomisen jälkeen voit testata sitä nähdäksesi, miten se vastaa käyttäjän kyselyihin Microsoft Foundry -portaalin leikkikentällä.

1. Valitse agentin **Asetukset**-ruudun yläosasta **Kokeile leikkikentässä**.
2. Voit vuorovaikuttaa agentin kanssa **Leikkikenttä**-ruudussa kirjoittamalla kyselyjä chat-ikkunaan. Voit esimerkiksi pyytää agenttia etsimään lentoja Seattlesta New Yorkiin 28. päiväksi.

    > **Huom**: Agentin vastaukset eivät välttämättä ole täysin tarkkoja, koska tässä harjoituksessa ei käytetä reaaliaikaista tietoa. Tavoitteena on testata, miten agentti ymmärtää ja vastaa käyttäjän pyyntöihin annettujen ohjeiden pohjalta.

    ![Agent Playground](../../../translated_images/fi/agent-playground.dc146586de715010.webp)

3. Testauksen jälkeen voit mukauttaa agenttia lisäämällä uusia tarkoituksia, koulutusdataa ja toimintoja, jotta sen kykyjä voidaan parantaa.

## Poista resurssit

Kun olet lopettanut agentin testaamisen, voit poistaa sen lisäkustannusten välttämiseksi.
1. Avaa [Azure-portaali](https://portal.azure.com) ja tarkastele resurssiryhmän sisältöä, johon olet ottanut hubin resurssit käyttöön tässä harjoituksessa.
2. Valitse työkaluriviltä **Poista resurssiryhmä**.
3. Kirjoita resurssiryhmän nimi ja vahvista poisto.

## Resurssit

- [Microsoft Foundryn dokumentaatio](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry -portaali](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Aloittaminen Microsoft Foundryn kanssa](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure AI -agenttien perusteet](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->