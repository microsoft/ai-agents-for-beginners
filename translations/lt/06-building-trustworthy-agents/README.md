[![Patikimi AI agentai](../../../translated_images/lt/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Paspauskite paveikslėlį viršuje, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# Patikimų AI agentų kūrimas

## Įvadas

Šioje pamokoje aptarsime:

- Kaip sukurti ir įdiegti saugius ir efektyvius AI agentus
- Svarbias saugumo nuostatas kuriant AI agentus
- Kaip užtikrinti duomenų ir vartotojų privatumo apsaugą kuriant AI agentus

## Mokymosi tikslai

Baigę šią pamoką, žinosite, kaip:

- Nustatyti ir sumažinti rizikas kuriant AI agentus
- Įdiegti saugumo priemones, užtikrinančias tinkamą duomenų ir prieigos valdymą
- Kurti AI agentus, kurie palaiko duomenų privatumą ir suteikia kokybišką vartotojo patirtį

## Saugumas

Pirmiausia pažvelkime, kaip kurti saugias agentines programas. Saugumas reiškia, kad AI agentas veikia pagal numatytą veikimą. Kaip agentinių programų kūrėjai turime metodų ir įrankių, leidžiančių maksimizuoti saugumą:

### Sistemos pranešimų struktūros kūrimas

Jei kada nors kūrėte AI programą naudodami didelius kalbos modelius (LLM), žinote, kaip svarbu sukurti tvirtą sistemos komandą arba sistemos pranešimą. Šios komandos nustato meta taisykles, instrukcijas ir gaires, kaip LLM sąveikaus su vartotoju ir duomenimis.

AI agentams sistemos komanda yra dar svarbesnė, nes AI agentams reikės labai tikslių nurodymų, kad jie galėtų atlikti mums skirtas užduotis.

Norėdami kurti mastelinius sistemos pranešimus, galime naudoti sistemos pranešimų struktūrą, skirtą vieno ar daugiau agentų kūrimui mūsų programoje:

![Sistemos pranešimų struktūros kūrimas](../../../translated_images/lt/system-message-framework.3a97368c92d11d68.webp)

#### 1 žingsnis: sukurkite meta sistemos pranešimą

Meta promptas bus naudojamas LLM generuoti sistemos pranešimus agentams, kuriuos kuriame. Jį projektuojame kaip šabloną, kad efektyviai galėtume sukurti kelis agentus, jei reikia.

Štai pavyzdys, kokį meta sistemos pranešimą pateiktume LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 2 žingsnis: Sukurkite pagrindinį promptą

Kitas žingsnis – sukurti pagrindinį promptą, apibūdinantį AI agentą. Jame turėtumėte nurodyti agento vaidmenį, užduotis, kurias agentas vykdys, ir kitas agento atsakomybes.

Štai pavyzdys:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 3 žingsnis: Pateikite pagrindinį sistemos pranešimą LLM

Dabar galime optimizuoti šį sistemos pranešimą, pateikdami meta sistemos pranešimą kaip sistemos pranešimą kartu su mūsų pagrindiniu sistemos pranešimu.

Tai sugeneruos geriau sukurtą sistemos pranešimą, skirtą vadovauti mūsų AI agentams:

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

#### 4 žingsnis: Kartokite ir tobulinkite

Šios sistemos pranešimų struktūros vertė yra galimybė palengvinti sistemos pranešimų kūrimą iš kelių agentų, taip pat tobulinti savo sistemos pranešimus su laiku. Retai kada turėsite sistemos pranešimą, kuris veiks pirmą kartą visam jūsų naudojimo atvejui. Gebėjimas atlikti mažus pakeitimus ir patobulinimus keisdami pagrindinį sistemos pranešimą ir paleisdami jį per sistemą leis jums palyginti ir įvertinti rezultatus.

## Grėsmių supratimas

Norint sukurti patikimus AI agentus, svarbu suprasti ir mažinti rizikas bei grėsmes jūsų AI agentui. Pažvelkime į keletą skirtingų grėsmių AI agentams ir kaip geriau galite planuoti bei pasiruošti joms.

![Grėsmių supratimas](../../../translated_images/lt/understanding-threats.89edeada8a97fc0f.webp)

### Užduotis ir instrukcija

**Aprašymas:** Užpuolikai bando pakeisti AI agente esančias instrukcijas ar tikslus per promptus arba manipuliuojant įvestimis.

**Prevencija:** Vykdykite įvedimo patikros ir filtravimo procedūras, kad aptiktumėte potencialiai pavojingus promptus prieš juos apdorojant AI agentui. Kadangi šie išpuoliai dažnai reikalauja dažnos sąveikos su agentu, pokalbių pokyčių skaičiaus ribojimas yra dar vienas būdas užkirsti kelią tokiems išpuoliams.

### Prieiga prie kritinių sistemų

**Aprašymas:** Jei AI agentas turi prieigą prie sistemų ir paslaugų, kurios saugo jautrius duomenis, užpuolikai gali pažeisti ryšį tarp agento ir šių paslaugų. Tai gali būti tiesioginiai išpuoliai arba netiesioginiai bandymai gauti informaciją apie šias sistemas per agentą.

**Prevencija:** AI agentams turėtų būti leidžiama prieiga prie sistemų tik pagal poreikį, kad būtų išvengta tokių atakų. Komunikacija tarp agento ir sistemos taip pat turi būti saugi. Autentifikacijos ir prieigos kontrolės įgyvendinimas yra dar vienas būdas apsaugoti šią informaciją.

### Išteklių ir paslaugų perkrova

**Aprašymas:** AI agentai gali naudotis įvairiais įrankiais ir paslaugomis užduotims vykdyti. Užpuolikai gali išnaudoti šią galimybę atakuoti šias paslaugas siųsdami didelį užklausų kiekį per AI agentą, kas gali sukelti sistemų gedimus arba dideles išlaidas.

**Prevencija:** Įdiekite politiką, ribojančią užklausų, kurias AI agentas gali siųsti paslaugai, skaičių. Pokalbio pokyčių ir užklausų limitavimas jūsų AI agentui yra dar vienas būdas užkirsti kelią tokiems išpuoliams.

### Žinių bazės užnuodijimas

**Aprašymas:** Šio tipo ataka nepuola AI agento tiesiogiai, bet taikosi į žinių bazę ir kitas paslaugas, kurias AI agentas naudos. Tai gali būti duomenų arba informacijos sugadinimas, kurią AI agentas naudos vykdydamas užduotį, vedantis prie šališkų ar nenumatytų atsakymų vartotojui.

**Prevencija:** Reguliariai tikrinkite duomenis, kuriuos AI agentas naudos savo darbo eigoje. Užtikrinkite, kad prieiga prie šių duomenų būtų saugi ir juos galėtų keisti tik patikimi asmenys, kad apsisaugotumėte nuo tokios atakos.

### Grandininės klaidos

**Aprašymas:** AI agentai naudojasi įvairiais įrankiais ir paslaugomis užduotims atlikti. Užpuolimų sukeltos klaidos gali sukelti kitų sistemų, prie kurių prijungtas AI agentas, gedimus, todėl ataka gali išplisti ir būti sunkiau taisoma.

**Prevencija:** Vienas būdas išvengti to yra veikti su AI agentu ribotoje aplinkoje, pavyzdžiui, vykdant užduotis Docker konteineryje, kad būtų išvengta tiesioginių sisteminių atakų. Taip pat svarbu kurti atsarginius mechanizmus ir pakartotinio bandymo logiką, kai tam tikros sistemos atsako klaida, kad būtų išvengta didesnių sistemų gedimų.

## Žmogus procesų cikle

Kitas efektyvus būdas kurti patikimas AI agentų sistemas – naudoti žmogų procesų cikle. Tai sukuria srautą, kai vartotojai gali teikti grįžtamąjį ryšį agentams vykdymo metu. Vartotojai iš esmės veikia kaip agentai daugiaagentinėje sistemoje, duodami patvirtinimus arba nutraukdami vykdomą procesą.

![Žmogus procesų cikle](../../../translated_images/lt/human-in-the-loop.5f0068a678f62f4f.webp)

Čia pateiktas kodo fragmentas, naudojant Microsoft Agent Framework, parodyti, kaip ši koncepcija įgyvendinama:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Sukurkite teikėją su žmogaus patvirtinimu cikle
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Sukurkite agentą su žmogaus patvirtinimo žingsniu
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Vartotojas gali peržiūrėti ir patvirtinti atsakymą
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Išvada

Patikimų AI agentų kūrimas reikalauja atsargaus dizaino, tvirtų saugumo priemonių ir nuolatinio tobulinimo. Įgyvendinus struktūrizuotą meta promptų sistemą, supratus galimas grėsmes ir taikant jų mažinimo strategijas, kūrėjai gali sukurti AI agentus, kurie yra saugūs ir efektyvūs. Be to, integruojant žmogaus dalyvavimą cikle užtikrinama, kad AI agentai išliktų suderinti su vartotojų poreikiais ir sumažintų rizikas. Kadangi AI technologijos nuolat vystosi, aktyvus požiūris į saugumą, privatumą ir etikos aspektus bus būtinas norint skatinti pasitikėjimą ir patikimumą AI pagrįstose sistemose.

## Kodo pavyzdžiai

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): žingsnis po žingsnio demonstruojama meta promptų sistemos-struktūros kūrimas.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Veiksmų patvirtinimo vartai, rizikos sluoksniavimas ir audito žurnalavimas patikimiems agentams.

### Turite daugiau klausimų apie patikimų AI agentų kūrimą?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kad susitikti su kitais besimokančiais, dalyvauti aptarimuose ir gauti atsakymus į savo AI agentų klausimus.

## Papildomi ištekliai

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Atsakingo AI naudojimo apžvalga</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatyviųjų AI modelių ir AI programų vertinimas</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Saugumo sistemos pranešimai</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Rizikos įvertinimo šablonas</a>

## Ankstesnė pamoka

[Agentinis RAG](../05-agentic-rag/README.md)

## Kitoji pamoka

[Planavimo dizaino šablonas](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->