[![Patikimi DI agentai](../../../translated_images/lt/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Spustelėkite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# Kaip kurti patikimus DI agentus

## Įvadas

Šioje pamokoje bus aptariama:

- Kaip sukurti ir įdiegti saugius bei veiksmingus DI agentus
- Svarbūs saugumo aspektai, kuriuos reikia apsvarstyti kūriant DI agentus.
- Kaip išlaikyti duomenų ir vartotojų privatumą kuriant DI agentus.

## Mokymosi tikslai

Baigus šią pamoką, jūs žinosite kaip:

- Nustatyti ir sumažinti rizikas, kuriant DI agentus.
- Įgyvendinti saugumo priemones, užtikrinančias tinkamą duomenų ir prieigos valdymą.
- Kurti DI agentus, kurie užtikrina duomenų privatumą ir suteikia kokybišką vartotojo patirtį.

## Saugumas

Pirmiausia pažvelkime, kaip kurti saugias agentines programas. Saugumas reiškia, kad DI agentas veikia pagal numatytą paskirtį. Kūdnant agentines programas, turime metodus ir įrankius saugumo maksimalizavimui:

### Sistemos žinučių karkaso kūrimas

Jei kada nors kūrėte DI programą naudojant Didelio kalbos modelius (LLM), žinote, kaip svarbu sukurti stiprų sistemos raginimą arba sistemos žinutę. Šie raginimai nustato metareglas, instrukcijas ir gaires, kaip LLM bendraus su vartotoju ir duomenimis.

DI agentams sistemos raginimas yra dar svarbesnis, nes agentams reikia itin konkrečių nurodymų, kad jie įvykdytų mums skirtas užduotis.

Norėdami sukurti plečiamus sistemos raginimus, galime naudoti sistemos žinučių karkasą, skirtą vienam ar daugiau agentų mūsų programoje kurti:

![Sistemos žinučių karkaso kūrimas](../../../translated_images/lt/system-message-framework.3a97368c92d11d68.webp)

#### 1 veiksmas: Sukurkite meta sistemos žinutę

Meta raginimas bus naudojamas LLM generuoti sistemos raginimus sukuriamiems agentams. Jį kuriame kaip šabloną, kad galėtume efektyviai sukurti kelis agentus, jei reikia.

Štai pavyzdys meta sistemos žinutės, kurią pateiktume LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 2 veiksmas: Sukurkite pagrindinį raginimą

Toliau reikia sukurti pagrindinį raginimą, apibūdinantį DI agentą. Jame turėtumėte nurodyti agento vaidmenį, užduotis, kurias agentas atliks, bei kitas agente numatytas atsakomybes.

Štai pavyzdys:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 3 veiksmas: Pateikite pagrindinę sistemos žinutę LLM

Dabar galime patobulinti šią sistemos žinutę, suteikdami meta sistemos žinutę kaip sistemos žinutę kartu su pagrindine sistemos žinute.

Tai sukurs sistemos žinutę, geriau parengtą vadovauti mūsų DI agentams:

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

#### 4 veiksmas: Kartokite ir tobulinkite

Šio sistemos žinučių karkaso vertė yra galimybė lengviau plečiamai kurti sistemos žinutes keliems agentams, taip pat laikui bėgant tobulinti savo sistemos žinutes. Retai pasitaiko, kad pirmą kartą sukurta sistemos žinutė tobulai atitiktų jūsų visą naudojimo atvejį. Galimybė daryti nedidelius pakeitimus ir patobulinimus keisdamas pagrindinę sistemos žinutę ir išbandydamas ją sistemoje leis jums palyginti ir įvertinti rezultatus.

## Grėsmių supratimas

Norint sukurti patikimus DI agentus, svarbu suprasti ir sumažinti rizikas bei grėsmes, kylančias jūsų DI agentui. Pažvelkime tik į keletą skirtingų grėsmių DI agentams ir kaip galite geriau suplanuoti ir pasiruošti joms.

![Grėsmių supratimas](../../../translated_images/lt/understanding-threats.89edeada8a97fc0f.webp)

### Užduotis ir instrukcijos

**Aprašymas:** Užpuolikai bando pakeisti DI agente nurodymus arba tikslus per raginimus ar įvesties manipuliavimą.

**Sumažinimas:** Vykdykite patikrinimus ir įvesties filtrus, kad aptiktumėte galimai pavojingus raginimus prieš juos apdorojant DI agentui. Kadangi šie užpuolimai paprastai reikalauja dažnos sąveikos su agentu, pokalbio turų ribojimas yra dar viena priemonė, padedanti apsisaugoti nuo tokių užpuolimų.

### Prieiga prie kritinių sistemų

**Aprašymas:** Jei DI agentas turi prieigą prie sistemų ir paslaugų, kurios saugo jautrius duomenis, užpuolikai gali pažeisti ryšį tarp agento ir šių paslaugų. Tai gali būti tiesioginiai užpuolimai arba netiesioginės pastangos gauti informacijos apie šias sistemas per agentą.

**Sumažinimas:** DI agentams turėtų būti suteikta tik būtina prieiga prie sistemų, kad būtų išvengta tokių užpuolimų. Ryšys tarp agento ir sistemos taip pat turi būti saugus. Įdiegti autentifikaciją ir prieigos kontrolę yra dar vienas būdas apsaugoti šią informaciją.

### Išteklių ir paslaugų perkrova

**Aprašymas:** DI agentai gali naudotis įvairiais įrankiais ir paslaugomis užduotims atlikti. Užpuolikai gali išnaudoti šią galimybę siųsdami didelį užklausų kiekį per DI agentą, kas gali sukelti sistemų gedimus arba dideles išlaidas.

**Sumažinimas:** Įdiekite politiką, ribojančią užklausų skaičių, kurį DI agentas gali siųsti paslaugai. Pokalbio turų ir užklausų DI agentui ribojimas yra dar viena priemonė užkirsti kelią tokiems užpuolimams.

### Žinių bazės užteršimas

**Aprašymas:** Šio tipo užpuolimas nėra nukreiptas į DI agentą tiesiogiai, tačiau į žinių bazę ir kitas paslaugas, kurias DI agentas naudos. Tai gali būti duomenų ar informacijos, kuria agentas naudojasi užduočiai atlikti, sugadinimas, sukeliantis šališkas arba netinkamas reakcijas vartotojui.

**Sumažinimas:** Reguliariai tikrinkite duomenis, kuriuos DI agentas naudos savo veiklos procesuose. Užtikrinkite, kad prieiga prie šių duomenų būtų saugi ir kad juos galėtų keisti tik patikimi asmenys, siekiant išvengti tokio tipo užpuolimų.

### Kaskadinės klaidos

**Aprašymas:** DI agentai naudoja įvairius įrankius ir paslaugas užduotims atlikti. Užpuolikų sukeltos klaidos gali sukelti kitų su agentu susijusių sistemų gedimus, todėl užpuolimas išplinta ir jį sunkiau išspręsti.

**Sumažinimas:** Vienas būdų išvengti šios problemos - leisti DI agentui veikti ribotoje aplinkoje, pavyzdžiui, vykdant užduotis Docker konteineryje, kad būtų apsaugota nuo tiesioginių sistemos atakų. Taip pat naudokite atsarginio plano mechanizmus ir bandymo pakartojimus, kai tam tikros sistemos atsako klaida, tai padeda išvengti didesnių sistemos gedimų.

## Žmogaus dalyvavimas procese

Kitas efektyvus būdas kurti patikimas DI agentų sistemas yra naudoti žmogų procese („Human-in-the-loop“). Tai sudaro srautą, kuriame vartotojai gali teikti atsiliepimus agentams vykdymo metu. Vartotojai iš esmės veikia kaip agentai daugiagentėje sistemoje ir suteikia leidimą ar nutraukia vykdymo procesą.

![Žmogus procese](../../../translated_images/lt/human-in-the-loop.5f0068a678f62f4f.webp)

Štai kodo fragmentas, naudojant Microsoft agentų karkasą, parodantis, kaip įgyvendinama ši koncepcija:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Sukurkite teikėją su žmogaus patvirtinimu
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

Kuriant patikimus DI agentus reikia kruopštaus dizaino, tvirtų saugumo priemonių ir nuolatinio tobulinimo. Įdiegus struktūruotas meta raginių sistemas, supratus galimas grėsmes ir taikant rizikos mažinimo strategijas, kūrėjai gali sukurti tiek saugius, tiek veiksmingus DI agentus. Be to, įtraukus žmogaus dalyvavimą procese užtikrinama, kad DI agentai išliktų suderinti su vartotojų poreikiais ir tuo pačiu minimizuojamos rizikos. DI toliau tobulėjant, aktyvus požiūris į saugumą, privatumą ir etinius aspektus bus svarbus pasitikėjimo ir patikimumo skatinimui DI valdomose sistemose.

### Turite daugiau klausimų apie patikimų DI agentų kūrimą?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kad susipažintumėte su kitais besimokančiais, sudalyvautumėte biuro valandose ir gautumėte atsakymus į savo DI agentų klausimus.

## Papildomi ištekliai

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Atsakingas DI naudojimas – apžvalga</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatyvių DI modelių ir DI programų vertinimas</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Saugumo sistemos žinutės</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Rizikos vertinimo šablonas</a>

## Ankstesnė pamoka

[Agentinis RAG](../05-agentic-rag/README.md)

## Kitoji pamoka

[Planavimo dizaino šablonas](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės atsisakymas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turi būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus vertimas žmogaus. Mes neatsakome už jokias nesusipratimus ar neteisingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->