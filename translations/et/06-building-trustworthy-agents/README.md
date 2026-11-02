[![Usaldusväärsed tehisintellekti agendid](../../../translated_images/et/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klõpsake ülaloleval pildil, et vaadata selle õppetunni videot)_

# Usaldusväärsete tehisintellekti agentide loomine

## Sissejuhatus

See õppetund käsitleb:

- Kuidas luua ja juurutada ohutuid ning tõhusaid tehisintellekti agente
- Olulisi turvakaalutlusi tehisintellekti agentide arendamisel.
- Kuidas säilitada andmete ja kasutajate privaatsust tehisintellekti agentide arendamisel.

## Õpieesmärgid

Pärast selle õppetunni lõpetamist oskad:

- Tuvastada ja leevendada riske tehisintellekti agentide loomisel.
- Rakendada turvameetmeid, et tagada andmete ja juurdepääsu nõuetekohane haldamine.
- Luua tehisintellekti agente, kes säilitavad andmete privaatsuse ja pakuvad kvaliteetset kasutajakogemust.

## Ohutus

Vaatame esmalt, kuidas ehitada turvalisi agentseid rakendusi. Ohutus tähendab, et tehisintellekti agent toimib ettenähtud viisil. Agentsete rakenduste loojatena on meil meetodid ja tööriistad ohutuse maksimeerimiseks:

### Süsteemisõnumi raamistikku loomine

Kui olete kunagi loonud tehisintellekti rakenduse, kasutades suuri keelemudeleid (LLM), siis teate, kui oluline on kujundada robustne süsteemiprompt või süsteemisõnum. Need promptid sätestavad meta reeglid, juhised ja juhendid selle kohta, kuidas LLM suhtleb kasutaja ja andmetega.

Tehisintellekti agentide puhul on süsteemiprompt veelgi olulisem, kuna agentidel on vaja väga spetsiifilisi juhiseid, et täita meile määratud ülesandeid.

Skaalautuvate süsteemipromptide loomiseks saame kasutada süsteemisõnumite raamistikku ühe või mitme agendi ülesehitamiseks meie rakenduses:

![Süsteemisõnumi raamistiku loomine](../../../translated_images/et/system-message-framework.3a97368c92d11d68.webp)

#### Samm 1: Meta süsteemisõnumi loomine

Meta prompti kasutab LLM süsteemipromptide genereerimiseks agentidele, keda me loome. Kujundame selle mallina, et vajadusel saaksime tõhusalt luua mitu agenti.

Siin on näide meta süsteemisõnumist, mida annaksime LLM-ile:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Samm 2: Loo alusprompt

Järgmiseks sammuks on luua baasprompt, mis kirjeldab tehisintellekti agenti. See peaks sisaldama agendi rolli, ülesandeid, mida agent täidab, ja muid vastutusi.

Näiteks:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Samm 3: Esita baassüsteemisõnum LLM-ile

Nüüd saame seda süsteemisõnumit optimeerida, esitades meta süsteemisõnumi süsteemisõnumina koos meie baassüsteemisõnumiga.

See genereerib paremini kavandatud süsteemisõnumi, mis juhatab meie AI agente:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Samm 4: Iteratsioon ja parendamine

Selle süsteemisõnumi raamistikku väärtus seisneb selles, et süsteemisõnumite loomine mitme agendi jaoks muutub lihtsamaks ning saame oma süsteemisõnumeid aja jooksul täiustada. On harva ette tulnud, et süsteemisõnum toimiks esimesel korral ideaalselt kogu kasutusjuhtumi jaoks. Väikeste muudatuste tegemine ja baassüsteemisõnumi muutmine ning süsteemi läbi jooksutamine võimaldab teil võrrelda ja hinnata tulemusi.

## Ohte mõista

Usaldusväärsete tehisintellekti agentide ehitamiseks on oluline mõista ja leevendada AI agentidele avaldatavaid riske ja ohte. Vaatame mõningaid erinevaid ohte ja kuidas neid paremini planeerida ja ennetada.

![Ohte mõistmine](../../../translated_images/et/understanding-threats.89edeada8a97fc0f.webp)

### Ülesanne ja juhised

**Kirjeldus:** Ründajad püüavad muuta AI agendi juhiseid või eesmärke, kasutades promptimist või sisendi manipuleerimist.

**Leevendus:** Tehke valideerimiskontrolle ja sisendifiltreid ohtlike promptide tuvastamiseks enne, kui AI agent neid töötleb. Kuna need rünnakud nõuavad tavaliselt sagedast suhtlust agendiga, aitab vestluse voorude arvu piiramise strateegia selliseid rünnakuid ennetada.

### Juurdepääs kriitilistele süsteemidele

**Kirjeldus:** Kui AI agendil on juurdepääs süsteemidele ja teenustele, kus hoitakse tundlikke andmeid, võivad ründajad kahjustada agenti ja nende teenuste vahelist suhtlust. Need võivad olla nii otsesed rünnakud kui ka kaudsed katsed saada infot nende süsteemide kohta läbi agendi.

**Leevendus:** AI agentidele tuleks anda juurdepääs süsteemidele ainult siis, kui vajalik, et vältida selliseid rünnakuid. Suhtlus agendi ja süsteemi vahel peaks samuti olema turvaline. Autentimise ja juurdepääsu kontrolli rakendamine on veel üks viis info kaitsmiseks.

### Ressursside ja teenuste üleküllus

**Kirjeldus:** AI agentidel on ligipääs erinevatele tööriistadele ja teenustele ülesannete täitmiseks. Ründajad võivad kasutada seda võimekust, et rünnata neid teenuseid, saates AI agendi kaudu suures mahus päringuid, mille tulemusena võib süsteem kokku jooksta või tekkida kõrged kulud.

**Leevendus:** Rakendage poliitikad, mis piiravad, mitu päringut AI agent teenusele teha saab. Vestluse voorude arvu ja päringute piiramise strateegiad AI agendile on veel üks viis selliste rünnakute ennetamiseks.

### Teadmiste baasi mürgitamine

**Kirjeldus:** Selline rünnak ei sihi AI agenti otseselt, vaid sihib teadmiste baasi ja muid teenuseid, mida AI agent kasutab. See võib hõlmata andmete või informatsiooni kahjustamist, mida AI agent kasutab ülesannete täitmisel, põhjustades kallutatud või soovimatuid vastuseid kasutajale.

**Leevendus:** Kontrollige regulaarselt andmeid, mida AI agent oma töövoogudes kasutab. Veenduge, et ligipääs nendele andmetele oleks turvaline ja neid muudaksid ainult usaldusväärsed isikud, et vältida sellist rünnakut.

### Kaskaadervead

**Kirjeldus:** AI agentidel on ligipääs erinevatele tööriistadele ja teenustele ülesannete täitmiseks. Ründajate poolt põhjustatud vead võivad viia teiste süsteemide rikete tekkeni, millega AI agent on ühendatud, põhjustades rünnaku laiemat levikut ja raskendades veaotsingut.

**Leevendus:** Üks meetod selle vältimiseks on lasta AI agendil töötada piiratud keskkonnas, näiteks Docker konteineris, et takistada otseseid süsteemirünnakuid. Tagamehhanismide ja korduslogika loomine tõrgete korral, kui teatud süsteemid annavad veateate, aitab samuti vältida suuremaid süsteemirikkeid.

## Inimene tsüklis

Teine tõhus viis usaldusväärsete AI agentide süsteemide loomiseks on kasutada inimest tsüklis. See loob voolu, kus kasutajad saavad protsessi käigus agentidele tagasisidet anda. Kasutajad toimivad põhimõtteliselt agendina mitmeagentse süsteemi osana, andes heakskiite või lõpetades jooksva protsessi.

![Inimene tsüklis](../../../translated_images/et/human-in-the-loop.5f0068a678f62f4f.webp)

Siin on koodinäide Microsoft Agent Frameworki kasutamisest, mis näitab, kuidas seda kontseptsiooni rakendatakse:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Loo pakkuja, kus on inimeste kinnitamine
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Loo esindaja koos inimeste heakskiidu sammuga
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Kasutaja saab vastust üle vaadata ja kinnitada
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Kokkuvõte

Usaldusväärsete AI agentide loomine nõuab hoolikat kujundust, tugevdatud turvameetmeid ja pidevat iteratsiooni. Struktureeritud meta promptide süsteemide rakendamise, potentsiaalsete ohtude mõistmise ja leevendusstrateegiate kasutuselevõtu kaudu saavad arendajad luua AI agente, kes on nii ohutud kui ka tõhusad. Lisaks kindlustab inimese tsüklis meetod, et AI agent jääb kooskõlla kasutaja vajadustega, minimeerides samal ajal riske. Kuna tehisintellekt areneb edasi, on proaktiivne hoiak turvalisuse, privaatsuse ja eetiliste kaalutluste osas võtmetähtsusega usalduse ja usaldusväärsuse edendamiseks AI-põhistes süsteemides.

## Koodinäited

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Üks samm-sammult demonstratsioon meta prompti süsteemisõnumi raamistikust.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Enne tegevust heakskiidu väravad, riskitasemete määramine ja usaldusväärsete agentide auditeerimise logimine.

### Kas teil on veel küsimusi usaldusväärsete AI agentide loomise kohta?

Liituge [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda vastuvõtutundides ja saada oma AI agentidega seotud küsimustele vastuseid.

## Täiendavad ressursid

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Vastutustundliku tehisintellekti ülevaade</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatiivsete tehisintellekti mudelite ja rakenduste hindamine</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Ohutuse süsteemisõnumid</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Riskihindamise mall</a>

## Eelmine õppetund

[Agentne RAG](../05-agentic-rag/README.md)

## Järgmine õppetund

[Planeerimise disainimuster](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->