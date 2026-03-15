[![Usaldusväärsed tehisintellekti agendid](../../../translated_images/et/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klõpsa ülaloleval pildil, et vaadata selle õppetunni videot)_

# Usaldusväärsete tehisintellekti agentide loomine

## Introduction

This lesson will cover:

- Kuidas ehitada ja juurutada turvalisi ning tõhusaid tehisintellekti agente
- Olulisi turvalisuse aspekte tehisintellekti agentide arendamisel.
- Kuidas tagada andmete ja kasutajate privaatsus tehisintellekti agentide arendamisel.

## Learning Goals

After completing this lesson, you will know how to:

- Tuua välja ja leevendada riske tehisintellekti agentide loomisel.
- Rakendada turvameetmeid, et andmed ja ligipääs oleksid korrektselt hallatud.
- Luua tehisintellekti agente, mis säilitavad andmete privaatsuse ja pakuvad kvaliteetset kasutajakogemust.

## Safety

Vaatleme esmalt turvaliste agentpõhiste rakenduste ehitamist. Turvalisus tähendab, et tehisintellekti agent toimib vastavalt kavandatule. Agentpõhiste rakenduste loojatena on meil meetodid ja tööriistad turvalisuse maksimeerimiseks:

### Süsteemisõnumite raamistikku loomine

Kui oled kunagi ehitanud tehisintellekti rakendust, kasutades suuri keelemudeleid (LLM-e), siis tead, kui oluline on tugeva süsteemprompti või süsteemisõnumi kujundamine. Need promptid kehtestavad metareeglid, juhised ja suunised selle kohta, kuidas LLM suhtleb kasutaja ja andmetega.

AI agentide puhul on süsteemprompt veelgi olulisem, sest agentidel on vaja väga täpseid juhiseid nende jaoks mõeldud ülesannete täitmiseks.

Skaalautuvate süsteempromptide loomiseks võime kasutada süsteemisõnumite raamistikku ühe või mitme agendi ehitamiseks meie rakenduses:

![Süsteemisõnumite raamistikku ehitamine](../../../translated_images/et/system-message-framework.3a97368c92d11d68.webp)

#### Samm 1: Loo meta-süsteemisõnum 

Meta-prompti kasutab LLM süsteempromptide genereerimiseks agentidele, keda me loome. Kavandame selle mallina, et vajaduse korral saaksime tõhusalt luua mitu agenti.

Here is an example of a meta system message we would give to the LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Samm 2: Loo põhiprompt

Järgmine samm on koostada põhiprompt, mis kirjeldab tehisintellekti agenti. Sellel peaks olema kirjas agendi roll, ülesanded, mida agent täidab, ja teised agendi vastutusalad.

Here is an example:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Samm 3: Esita põhisüsteemisõnum LLM-ile

Nüüd saame seda süsteemisõnumit optimeerida, esitades meta-süsteemisõnumi süsteemisõnumina koos meie põhisüsteemisõnumiga.

See toodab süsteemisõnumi, mis on paremini kujundatud meie tehisintellekti agentide juhendamiseks:

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

#### Samm 4: Itereeri ja paranda

Selle süsteemisõnumite raamistiku väärtus on võimaldada hõlpsamini luua süsteemisõnumeid mitmele agendile ning parandada oma süsteemisõnumeid aja jooksul. Harva juhtub, et süsteemisõnum töötab esimesel katsel kogu sinu kasutusjuhtumi jaoks. Võimalus teha väikseid muudatusi ja täiendusi, muutes põhisüsteemisõnumit ja lastes selle läbi meta-süsteemi, võimaldab tulemusi võrrelda ja hinnata.

## Ohtude mõistmine

Usaldusväärsete tehisintellekti agentide loomiseks on oluline mõista ja leevendada agentidele suunatud riske ja ohte. Vaatleme mõned erinevad ohud agentidele ning kuidas nende jaoks paremini planeerida ja ette valmistuda.

![Ohtude mõistmine](../../../translated_images/et/understanding-threats.89edeada8a97fc0f.webp)

### Ülesanne ja juhised

**Kirjeldus:** Ründajad püüavad muuta tehisintellekti agendi juhiseid või eesmärke promptimise või sisendi manipuleerimise teel.

**Leevendus**: Rakenda valideerimiskontrolle ja sisendifiltreid, et tuvastada potentsiaalselt ohtlikke prompte enne, kui need agent töödeldakse. Kuna sellised rünnakud nõuavad tavaliselt sagedast suhtlust agendiga, aitab ka vestluse voorude arvu piiramine neid rünnakuid ennetada.

### Juurdepääs kriitilistele süsteemidele

**Kirjeldus**: Kui tehisintellekti agentil on juurdepääs süsteemidele ja teenustele, mis hoiavad tundlikke andmeid, võivad ründajad kahjustada suhtlust agendi ja nende teenuste vahel. Need võivad olla otsesed rünnakud või kaudsed katsed saada agenti kaudu teavet nende süsteemide kohta.

**Leevendus**: Agentidel peaks olema juurdepääs süsteemidele vaid vajaduspõhiselt, et vältida selliseid rünnakuid. Agendi ja süsteemi vaheline suhtlus peab samuti olema turvaline. Autentimise ja juurdepääsukontrolli rakendamine on veel üks viis selle teabe kaitsmiseks.

### Ressursside ja teenuste ülekoormus

**Kirjeldus:** Agentidel on juurdepääs erinevatele tööriistadele ja teenustele ülesannete täitmiseks. Ründajad võivad seda võimet ära kasutada teenuste ründamiseks, saates läbi agendi suures mahus päringuid, mis võib põhjustada süsteemirikkeid või suuri kulutusi.

**Leevendus:** Rakenda poliitikad, mis piiravad agendi teenusele saatavate päringute arvu. Ka vestluse voorude ja agendile esitatavate päringute arvu piiramine aitab selliseid rünnakuid ära hoida.

### Teadmusbaasi mürgitamine

**Kirjeldus:** See rünnatüüp ei sihi otseselt agenti, vaid sihib teadmistebaasi ja muid teenuseid, mida agent kasutab. See võib hõlmata agendi poolt kasutatava andmebaasi või teabe korrumpeerimist, mis viib kallutatud või ettenägematute vastusteni kasutajale.

**Leevendus:** Käivita regulaarselt andmete kontrollimist, mida agent oma töövoogudes kasutab. Tagage, et juurdepääs nendele andmetele oleks turvaline ja neid muudaksid vaid usaldusväärsed isikud, et vältida selliseid rünnakuid.

### Ahelvead

**Kirjeldus:** Agentid kasutavad erinevaid tööriistu ja teenuseid ülesannete täitmiseks. Ründajate põhjustatud vead võivad viia teiste süsteemide riketeni, millega agent on ühendatud, muutes rünnaku laiemaks ja raskemini tõrjatavaks.

**Leevendus**: Üks viis selle vältimiseks on lasta agendil töötada piiratud keskkonnas, näiteks täites ülesandeid Docker-konteineris, et vältida otseseid süsteemirünnakuid. Varuplaanide ja taaskatsete loogika loomine olukordades, kus teatud süsteemid vastavad veaga, on veel üks viis suuremate süsteemirikete vältimiseks.

## Inimene silmuses

Veel üks tõhus viis usaldusväärsete AI agentide süsteemide loomiseks on inimese kaasamine (human-in-the-loop). See loob töövoo, kus kasutajad saavad jooksvalt agentidele tagasisidet anda. Kasutajad toimivad sisuliselt agentidena multi-agent süsteemis, andes heakskiidu või lõpetades käimasoleva protsessi.

![Inimene silmuses](../../../translated_images/et/human-in-the-loop.5f0068a678f62f4f.webp)

Siin on koodilõik, mis kasutab Microsoft Agent Frameworki, et näidata, kuidas seda kontseptsiooni rakendatakse:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Loo teenusepakkuja, kus kinnitust teeb inimene.
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Loo agent inimese kinnitusetapiga.
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Kasutaja saab vastust üle vaadata ja kinnitada.
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Conclusion

Usaldusväärsete tehisintellekti agentide loomine nõuab hoolikat kavandamist, tugevaid turvameetmeid ja pidevat täiustamist. Struktureeritud meta-promptimise süsteemide rakendamise, võimalike ohtude mõistmise ja leevendusstrateegiate kasutuselevõtu kaudu saavad arendajad luua agente, mis on nii turvalised kui ka tõhusad. Lisaks tagab inimese-silmuses lähenemine, et agentid jäävad kasutajate vajadustega kooskõlaliseks, vähendades samal ajal riske. Kuna tehisintellekt areneb edasi, on turvalisuse, privaatsuse ja eetiliste kaalutluste proaktiivne käsitlemine võtmetähtsusega usalduse ja töökindluse edendamiseks tehisintellekti jõulistes süsteemides.

### Kas sul on veel küsimusi usaldusväärsete tehisintellekti agentide loomise kohta?

Liitu [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), et kohtuda teiste õppuritega, osaleda konsultatsioonitundides ja saada vastused oma tehisintellekti agentide küsimustele.

## Täiendavad ressursid

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Vastutustundliku tehisintellekti ülevaade</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatiivsete tehisintellekti mudelite ja tehisintellekti rakenduste hindamine</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Ohutuse süsteemisõnumid</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Riskihindamise mall</a>

## Previous Lesson

[Agentic RAG](../05-agentic-rag/README.md)

## Next Lesson

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Lahtiütlus:
See dokument on tõlgitud tehisintellekti tõlketeenuse Co-op Translator (https://github.com/Azure/co-op-translator) abil. Kuigi me püüame tagada täpsuse, tuleb arvestada, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Algkeeles olevat originaaldokumenti tuleks pidada autoriteetseks allikaks. Olulise teabe korral soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste ega valede tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->