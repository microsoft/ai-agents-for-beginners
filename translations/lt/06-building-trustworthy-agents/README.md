[![Patikimi DI Agentai](../../../translated_images/lt/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Spustelėkite aukščiau esantį paveikslėlį, kad peržiūrėtumėte vaizdo įrašą apie šią pamoką)_

# Patikimų DI Agentų kūrimas

## Įvadas

Šioje pamokoje bus aptariama:

- Kaip sukurti ir diegti saugius ir efektyvius DI Agentus
- Svarbūs saugumo aspektai kuriant DI Agentus.
- Kaip užtikrinti duomenų ir vartotojų privatumą kuriant DI Agentus.

## Mokymosi tikslai

Baigę šią pamoką, žinosite, kaip:

- Nustatyti ir sumažinti rizikas kuriant DI Agentus.
- Įgyvendinti saugumo priemones, kad duomenys ir prieiga būtų tinkamai valdomi.
- Kurti DI Agentus, kurie palaiko duomenų privatumo apsaugą ir suteikia kokybišką vartotojo patirtį.

## Saugumas

Pirmiausia pažvelkime į saugių agentinių programų kūrimą. Saugumas reiškia, kad DI agentas veikia pagal numatytą paskirtį. Kaip agentinių programų kūrėjai, turime metodus ir įrankius saugumui maksimizuoti:

### Sisteminės žinutės struktūros kūrimas

Jei kada nors kūrėte DI programą, naudodami didelius kalbos modelius (LLM), žinote, kokia svarbi yra patikima sistemos užklausa arba sistemos žinutė. Šios užklausos nustato meta taisykles, nurodymus ir gaires, kaip LLM bendraus su vartotoju ir duomenimis.

DI Agentams sistemos užklausa yra dar svarbesnė, nes agentams reikės labai specifinių nurodymų, kad jie įvykdytų mums skirtas užduotis.

Norėdami sukurti mastelio sistemines užklausas, galime naudoti sistemos žinučių struktūros sistemą, skirtą vienam ar daugiau agentų kurti mūsų programoje:

![Sistemos žinutės struktūros kūrimas](../../../translated_images/lt/system-message-framework.3a97368c92d11d68.webp)

#### 1 žingsnis: Sukurkite meta sistemos žinutę

Meta užklausa bus naudojama LLM generuoti sistemos užklausoms agentams, kuriuos kuriame. Ją suprojektuojame kaip šabloną, kad galėtume efektyviai kurti kelis agentus, jei reikia.

Štai pavyzdys meta sistemos žinutės, kurią suteiktume LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 2 žingsnis: Sukurkite pagrindinę užklausą

Kitas žingsnis yra sukurti pagrindinę užklausą, apibūdinančią DI Agentą. Reikėtų įtraukti agento vaidmenį, užduotis, kurias agentas atliks, ir kitas agento atsakomybes.

Štai pavyzdys:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 3 žingsnis: Pateikite pagrindinę sistemos žinutę LLM

Dabar galime optimizuoti šią sistemos žinutę, pateikdami meta sistemos žinutę kaip sistemos žinutę ir mūsų pagrindinę sistemos žinutę.

Tai sukurs geriau pritaikytą sistemos žinutę, skirtą vadovauti mūsų DI agentams:

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

Šios sistemos žinučių struktūros vertė yra ta, kad galime mastelio keisti sistemines žinutes iš kelių agentų ir laikui bėgant jas tobulinti. Retai pasitaiko, kad sistemos žinutė iš karto veiktų jūsų visiškam naudojimo atvejui. Galimybė atlikti mažus patikslinimus ir tobulinimus keičiant pagrindinę sistemos žinutę ir ją praleidžiant per sistemą leis palyginti ir įvertinti rezultatus.

## Grėsmių supratimas

Norint sukurti patikimus DI agentus, svarbu suprasti ir sumažinti rizikas bei grėsmes jūsų DI agentui. Pažvelkime į kelias grėsmes DI agentams ir kaip galite geriau suplanuoti bei pasiruošti joms.

![Grėsmių supratimas](../../../translated_images/lt/understanding-threats.89edeada8a97fc0f.webp)

### Užduotis ir nurodymai

**Aprašymas:** Užpuolikai bando pakeisti DI agento nurodymus ar tikslus per užklausas arba manipuliuodami įėjimais.

**Sumažinimas:** Atlikite patikrinimus ir įėjimų filtrus, kad aptiktumėte galimai pavojingas užklausas prieš jas apdorojant DI Agentui. Kadangi tokie atakai dažnai reikalauja dažnos sąveikos su Agentu, apribojant pokalbio etapų skaičių, galima užkirsti kelią tokioms atakoms.

### Prieiga prie kritinių sistemų

**Aprašymas:** Jei DI agentas turi prieigą prie sistemų ir paslaugų, kuriose saugomi jautrūs duomenys, užpuolikai gali pažeisti ryšį tarp agento ir šių paslaugų. Tai gali būti tiesioginės atakos arba netiesioginės bandymai gauti informaciją apie šias sistemas per agentą.

**Sumažinimas:** DI agentai turėtų turėti prieigą prie sistemų tik pagal poreikį, kad būtų išvengta tokių atakų. Ryšys tarp agento ir sistemos taip pat turėtų būti saugus. Autentifikacijos ir prieigos valdymo įgyvendinimas yra dar vienas būdas apsaugoti šią informaciją.

### Išteklių ir paslaugų perkrova

**Aprašymas:** DI agentai gali naudotis įvairiais įrankiais ir paslaugomis užduotims atlikti. Užpuolikai gali išnaudoti šią galimybę atakuodami šias paslaugas siųsdami didelį užklausų kiekį per DI Agentą, kas gali sukelti sistemos gedimus arba dideles išlaidas.

**Sumažinimas:** Įgyvendinkite taisykles, ribojančias užklausų, kurias DI agentas gali siųsti paslaugai, skaičių. Pokalbio etapų skaičiaus ir užklausų apribojimas jūsų DI agentui yra dar vienas būdas užkirsti kelią tokioms atakoms.

### Žinių bazės užteršimas

**Aprašymas:** Šio tipo ataka tiesiogiai nepuola DI agento, bet taikosi į žinių bazę ir kitas paslaugas, kurias agentas naudos. Tai gali apimti duomenų ar informacijos sugadinimą, kurią DI agentas naudos užduočiai atlikti, o tai lemia šališkus ar netikėtus atsakymus vartotojui.

**Sumažinimas:** Reguliariai tikrinkite duomenis, kuriuos DI agentas naudos savo veikloje. Užtikrinkite, kad prieiga prie šių duomenų būtų saugi ir juos keistų tik patikimi asmenys, kad išvengtumėte tokių atakų.

### Sekančios klaidos

**Aprašymas:** DI agentai pasiekia įvairius įrankius ir paslaugas vykdydami užduotis. Užpuolikų sukeltos klaidos gali sukelti kitų su agentu susijusių sistemų gedimus, dėl ko ataka išplinta ir tampa sunkiau aptinkama bei taisoma.

**Sumažinimas:** Vienas būdas to išvengti – leisti DI Agentui veikti ribotoje aplinkoje, pavyzdžiui, vykdyti užduotis Docker konteineryje, kad būtų išvengta tiesioginių sistemų atakų. Sukurkite atsarginio veikimo mechanizmus ir pakartotino bandymo logiką, kai tam tikros sistemos atsako klaidomis, tai padės užkirsti kelią didesniems sistemos gedimams.

## Žmogus cikle

Dar vienas veiksmingas būdas kurti patikimus DI Agentų sistemas yra naudoti žmogiškąją sąsają (human-in-the-loop). Tai sukuria srautą, kuriame vartotojai gali pateikti atsiliepimus Agentams vykdymo metu. Vartotojai iš esmės veikia kaip agentai daugiaagentėje sistemoje, patvirtindami arba nutraukdami vykdomą procesą.

![Žmogus cikle](../../../translated_images/lt/human-in-the-loop.5f0068a678f62f4f.webp)

Čia yra kodo fragmentas, naudojantis Microsoft Agent Framework, parodydamas, kaip įgyvendinama ši koncepcija:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Sukurkite paslaugų teikėją su žmogaus patvirtinimo žingsniu
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
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

Patikimų DI agentų kūrimas reikalauja atidžios projektavimo, tvirtų saugumo priemonių ir nuolatinio tobulinimo. Įgyvendindami struktūruotas meta užklausų sistemas, suprasdami galimas grėsmes ir taikydami jų mažinimo strategijas, kūrėjai gali sukurti saugius ir veiksmingus DI agentus. Be to, įtraukdami žmogų cikle užtikrina, kad DI agentai išliktų suderinti su vartotojų poreikiais ir sumažintų rizikas. Kadangi DI toliau vystosi, aktyvus požiūris į saugumą, privatumą ir etinius aspektus bus esminis kuriant pasitikėjimą ir patikimumą DI valdomose sistemose.

## Kodo pavyzdžiai

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Metaužklausų sistemos žinučių struktūros žingsnis po žingsnio demonstracija.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Veiksmų patvirtinimo vartai, rizikos lyginimas ir veiklos audito registravimas patikimiems agentams.

### Turite daugiau klausimų apie patikimų DI agentų kūrimą?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), susitikite su kitais besimokančiais, dalyvaukite biuro valandomis ir gaukite atsakymus į savo DI Agentų klausimus.

## Papildomi ištekliai

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Atsakingo DI apžvalga</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatyvių DI modelių ir DI programų vertinimas</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Saugumo sistemos žinutės</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Rizikos vertinimo šablonas</a>

## Ankstesnė pamoka

[Agentinė RAG](../05-agentic-rag/README.md)

## Kitoji pamoka

[Planavimo dizaino šablonas](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->