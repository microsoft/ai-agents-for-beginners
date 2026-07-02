[![Usaldusväärsed tehisintellekti agendid](../../../translated_images/et/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klõpsa ülaloleval pildil, et vaadata selle õppetunni videot)_

# Usaldusväärsete tehisintellekti agentide loomine

## Sissejuhatus

See õppetund käsitleb:

- Kuidas luua ja juurutada ohutuid ja tõhusaid tehisintellekti agente
- Olulisi turvalisuse kaalutlusi tehisintellekti agentide arendamisel.
- Kuidas säilitada andmete ja kasutajate privaatsus tehisintellekti agentide arendamisel.

## Õpieesmärgid

Pärast selle õppetunni läbimist oskad:

- Tuvastada ja leevendada riske tehisintellekti agentide loomisel.
- Rakendada turvameetmeid, et tagada andmete ja juurdepääsu nõuetekohane haldamine.
- Luua tehisintellekti agente, kes säilitavad andmete privaatsuse ja pakuvad kvaliteetset kasutajakogemust.

## Ohutus

Vaatame esmalt, kuidas ehitada ohutuid agentrakendusi. Ohutus tähendab, et tehisintellekti agent töötab kavandatult. Agentrakenduste loojatena on meil meetodid ja tööriistad ohutuse maksimeerimiseks:

### Süsteemiteate raamistiku loomine

Kui oled kunagi loonud tehisintellekti rakendust kasutades suuri keelemudeleid (LLM-e), tead kui oluline on kavandada tugev süsteemiprompt või süsteemiteade. Need promptid kehtestavad meta reeglid, juhised ja suunised, kuidas LLM suhtleb kasutaja ning andmetega.

Tehisintellekti agentide puhul on süsteemiprompt veelgi olulisem, kuna agentidel on vaja väga spetsiifilisi juhiseid, et täita neile määratud ülesandeid.

Skaalautuvate süsteemipromptide loomiseks võime kasutada süsteemiteate raamistiku ühe või mitme agendi ehitamiseks meie rakenduses:

![Süsteemiteate raamistiku loomine](../../../translated_images/et/system-message-framework.3a97368c92d11d68.webp)

#### Samm 1: Loo meta süsteemiteade

Meta prompti kasutab LLM agentide süsteemipromptide genereerimiseks. Selle kujundame mallina, et saaksime vajadusel efektiivselt luua mitut agenti.

Siin on näide meta süsteemiteatest, mida me annaksime LLM-ile:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Samm 2: Loo põhiprompt

Järgmine samm on luua põhiprompt, mis kirjeldab tehisintellekti agenti. Peaksid kaasama agendi rolli, agendi täidetavad ülesanded ja muud agendi vastutusalad.

Näide:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Samm 3: Esita põhisüsteemiteade LLM-ile

Nüüd saame seda süsteemiteadet optimeerida, esitades meta süsteemiteate süsteemiteate ja meie põhisüsteemiteate.

See annab süsteemiteate, mis on paremini disainitud meie tehisintellekti agentide juhendamiseks:

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

#### Samm 4: Korda ja paranda

Selle süsteemiteate raamistiku väärtus seisneb võimaluses hõlpsamini skaleerida mitme agendi süsteemiteadete loomist ning oma süsteemiteateid aja jooksul parandada. Harva juhtub, et süsteemiteade töötab esimesel korral täielikult sinu kasutusjuhtumil. Võimalus teha väikseid muudatusi ja parandusi, muutes põhisüsteemiteadet ning lastes seda süsteemist läbi, võimaldab tulemusi võrrelda ja hinnata.

## Ohtude mõistmine

Usaldusväärsete tehisintellekti agentide loomisel on oluline mõista ja leevendada riske ning ohtusid sinu tehisintellekti agendile. Vaatame vaid mõnda tehisintellekti agentidele esinevat ohtu ja kuidas saad nende jaoks paremini planeerida ja valmistuda.

![Ohtude mõistmine](../../../translated_images/et/understanding-threats.89edeada8a97fc0f.webp)

### Ülesanne ja juhised

**Kirjeldus:** Ründajad püüavad muuta tehisintellekti agendi juhiseid või eesmärke läbi promptimise või sisendite manipuleerimise.

**Leevendamine:** Käsuvalduste valideerimise kontrollimine ja sisendite filtreerimine potentsiaalselt ohtlike promptide tuvastamiseks enne nende töötlemist tehisintellekti agendi poolt. Kuna need rünnakud nõuavad tavaliselt sagedast suhtlust agendiga, on vestluses toimuvate käikude piiramisega võimalik samuti selliseid rünnakuid takistada.

### Juurdepääs kriitilistele süsteemidele

**Kirjeldus:** Kui tehisintellekti agendil on juurdepääs süsteemidele ja teenustele, mis hoiavad tundlikke andmeid, võivad ründajad kahjustada suhtlust agendi ja nende teenuste vahel. Need võivad olla otsesed rünnakud või kaudsed katsed hankida teavet nende süsteemide kohta agenti kaudu.

**Leevendamine:** Tehisintellekti agentidel peaks olema süsteemidele juurdepääs ainult vajadusel, et vältida selliseid rünnakuid. Agendi ja süsteemi vaheline suhtlus peaks olema samuti turvaline. Autentimise ja juurdepääsukontrolli rakendamine aitab samuti seda infot kaitsta.

### Ressursside ja teenuste ülekoormus

**Kirjeldus:** Tehisintellekti agentidel on ligipääs erinevatele tööriistadele ja teenustele ülesannete täitmiseks. Ründajad võivad seda kasutada nende teenuste ründamiseks, saates tehisintellekti agendi kaudu suures koguses päringuid, mis võib viia süsteemi rikete või kõrgete kuludeni.

**Leevendamine:** Rakendada poliitikaid, mis piiravad tehisintellekti agendi tehtavate päringute arvu teenusele. Vestluse käikude ja päringute arvu piiramine oma tehisintellekti agendi puhul aitab samuti selliseid rünnakuid takistada.

### Teadmistebaasi mürgitamine

**Kirjeldus:** See rünnak ei sihita tehisintellekti agenti otse, vaid teadmistebaasi ja muid teenuseid, mida tehisintellekti agent kasutab. See võib hõlmata agenti kasutatava andme või info rikkumist, mis toob kaasa kallutatud või soovimatuid vastuseid kasutajale.

**Leevendamine:** Kontrolli regulaarselt andmeid, mida tehisintellekti agent kasutab oma töövoogudes. Tagada, et juurdepääs neile andmetele oleks turvaline ja neid muudaksid ainult usaldusväärsed isikud, et vältida sellist rünnakut.

### Järjestikused vead

**Kirjeldus:** Tehisintellekti agentidel on juurdepääs erinevatele tööriistadele ja teenustele ülesannete täitmiseks. Ründajate põhjustatud vead võivad põhjustada ebaõnnestumisi teistes süsteemides, millele tehisintellekti agent on ühendatud, muutes rünnaku ulatuslikumaks ja raskemini tõrjutavaks.

**Leevendamine:** Üks viis selle vältimiseks on lasta tehisintellekti agendil töötada piiratud keskkonnas, näiteks täites ülesandeid Docker konteineris, et takistada otseseid süsteemirünnakuid. Tagavaramehhanismide ja taaskäsitlemisloogika loomine, kui teatud süsteemid annavad veateateid, aitab samuti ennetada ulatuslikumaid süsteemirikkeid.

## Inimene tsüklis

Teine tõhus viis usaldusväärsete tehisintellekti agentide süsteemide loomisel on inimene tsüklis. See loob voolu, kus kasutajad saavad anda agentidele tagasisidet töö ajal. Kasutajad toimivad kaudselt agentidena mitme agendi süsteemis, andes heakskiidu või lõpetades jooksva protsessi.

![Inimene tsüklis](../../../translated_images/et/human-in-the-loop.5f0068a678f62f4f.webp)

Siin on koodinäide, kasutades Microsofti agentide raamistiku, mis näitab, kuidas seda kontseptsiooni rakendatakse:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Loo teenusepakkuja inimest kaasava kinnitusega
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Loo agent inimese kinnitusetapiga
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

Usaldusväärsete tehisintellekti agentide loomine nõuab hoolikat kavandamist, tugevaid turvameetmeid ja pidevat iteratsiooni. Struktureeritud meta-promptimise süsteemide rakendamise, potentsiaalsete ohtude mõistmise ja leevendusstrateegiate kasutuselevõtu kaudu saavad arendajad luua tehisintellekti agente, kes on samaaegselt ohutud ja tõhusad. Lisaks tagab inimese tsüklis lähenemise kaasamine, et tehisintellekti agentide tegevus jääks kooskõlla kasutajate vajadustega, minimeerides riske. Kuna tehisintellekt areneb pidevalt, on turvalisuse, privaatsuse ja eetiliste kaalutluste ennetav käsitlemine võtmetähtsusega usalduse ja usaldusväärsuse loomisel tehisintellektil põhinevates süsteemides.

## Koodinäited

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Samm-sammult näide meta-prompti süsteemiteate raamistiku kohta.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Enne tegevust tehtavad heakskiidulüngad, riskitasemed ja auditijälgimine usaldusväärsete agentide jaoks.

### Kas sul on veel küsimusi usaldusväärsete tehisintellekti agentide loomise kohta?

Liitu [Microsoft Foundry Discordi](https://aka.ms/ai-agents/discord) kanaliga, et kohtuda teiste õppijatega, osaleda kontoritundides ja saada oma tehisintellekti agentide küsimustele vastuseid.

## Täiendavad ressursid

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Vastutustundliku tehisintellekti ülevaade</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatiivsete tehisintellekti mudelite ja rakenduste hindamine</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Turvalisuse süsteemiteated</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Riskide hindamise mall</a>

## Eelmine õppetund

[Agentne RAG](../05-agentic-rag/README.md)

## Järgmine õppetund

[Planeerimise disainimuster](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->