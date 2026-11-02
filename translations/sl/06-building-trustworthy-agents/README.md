[![Zanesljivi AI agenti](../../../translated_images/sl/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite na zgornjo sliko za ogled videa te lekcije)_

# Gradnja zanesljivih AI agentov

## Uvod

Ta lekcija bo obravnavala:

- Kako zgraditi in uvajati varne in učinkovite AI agente
- Pomembne varnostne vidike pri razvoju AI agentov.
- Kako ohraniti zasebnost podatkov in uporabnikov pri razvoju AI agentov.

## Cilji učenja

Po končani lekciji boste znali:

- Prepoznati in ublažiti tveganja pri ustvarjanju AI agentov.
- Uvesti varnostne ukrepe za zagotovitev pravilnega upravljanja podatkov in dostopa.
- Ustvariti AI agente, ki ohranjajo zasebnost podatkov in zagotavljajo kakovostno uporabniško izkušnjo.

## Varnost

Najprej si poglejmo, kako zgraditi varne agentne aplikacije. Varnost pomeni, da AI agent deluje tako, kot je bilo zasnovano. Kot graditelji agentnih aplikacij imamo metode in orodja za maksimiranje varnosti:

### Gradnja okvirja sistemskih sporočil

Če ste že kdaj gradili AI aplikacijo z velikimi jezikovnimi modeli (LLM), veste, kako pomembno je oblikovati robusten sistemski poziv ali sistemsko sporočilo. Ti pozivi določajo meta pravila, navodila in smernice, kako bo LLM komuniciral z uporabnikom in podatki.

Za AI agente je sistemski poziv še pomembnejši, saj bodo AI agenti potrebovali zelo specifična navodila za izpolnitev nalog, ki smo jih zanje oblikovali.

Za ustvarjanje razširljivih sistemskih pozivov lahko uporabimo okvir sistemskih sporočil za gradnjo enega ali več agentov v naši aplikaciji:

![Gradnja okvirja sistemskih sporočil](../../../translated_images/sl/system-message-framework.3a97368c92d11d68.webp)

#### Korak 1: Ustvarite meta sistemsko sporočilo

Meta poziv bo uporabil LLM za generiranje sistemskih pozivov za agente, ki jih ustvarimo. Oblikujemo ga kot predlogo, da lahko učinkovito ustvarjamo več agentov, če je potrebno.

Tukaj je primer meta sistemskega sporočila, ki bi ga dali LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Korak 2: Ustvarite osnovni poziv

Naslednji korak je ustvariti osnovni poziv za opis AI agenta. Vključiti morate vlogo agenta, naloge, ki jih bo agent opravil, in druge odgovornosti agenta.

Tukaj je primer:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Korak 3: Predajte osnovno sistemsko sporočilo LLM

Zdaj lahko ta sistemsko sporočilo optimiziramo tako, da kot sistemsko sporočilo zagotovimo meta sistemsko sporočilo in naše osnovno sistemsko sporočilo.

To bo proizvedlo sistemsko sporočilo, ki je bolje zasnovano za usmerjanje naših AI agentov:

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

#### Korak 4: Izboljševanje in iteracija

Vrednost tega okvirja sistemskih sporočil je lažje razširljivo ustvarjanje sistemskih sporočil za več agentov ter izboljševanje vaših sistemskih sporočil skozi čas. Redko se zgodi, da imate sistemsko sporočilo, ki deluje prvič za celoten primer uporabe. Možnost manjših popravkov in izboljšav z menjavo osnovnega sistemskega sporočila in njegovo obdelavo skozi sistem vam bo omogočila primerjavo in ocenjevanje rezultatov.

## Razumevanje groženj

Za gradnjo zanesljivih AI agentov je pomembno razumeti in omiliti tveganja in grožnje za vaš AI agent. Oglejmo si nekaj različnih groženj AI agentom in kako se nanje lahko bolje pripravite.

![Razumevanje groženj](../../../translated_images/sl/understanding-threats.89edeada8a97fc0f.webp)

### Naloga in navodilo

**Opis:** Napadalci poskušajo spremeniti navodila ali cilje AI agenta s pomočjo pozivov ali manipulacije vhodov.

**Omilitev:** Izvedite preverjanje in filtre vhodov za zaznavanje potencialno nevarnih pozivov, preden jih obdela AI agent. Ker ti napadi običajno zahtevajo pogosto interakcijo z agentom, je omejevanje števila krogov v pogovoru še en način za preprečevanje teh vrst napadov.

### Dostop do kritičnih sistemov

**Opis:** Če ima AI agent dostop do sistemov in storitev, ki shranjujejo občutljive podatke, lahko napadalci ogrozijo komunikacijo med agentom in temi storitvami. To so lahko neposredni napadi ali posredni poskusi pridobivanja informacij o teh sistemih preko agenta.

**Omilitev:** AI agenti naj imajo dostop do sistemov le po potrebi, da se preprečijo te vrste napadov. Komunikacija med agentom in sistemom mora biti prav tako varna. Uvedba avtentikacije in nadzora dostopa je še ena pot za zaščito teh informacij.

### Preobremenitev virov in storitev

**Opis:** AI agenti lahko uporabljajo različna orodja in storitve za opravljanje nalog. Napadalci lahko to možnost izkoristijo za napad na te storitve z velikim številom zahtev preko AI agenta, kar lahko povzroči okvare sistema ali visoke stroške.

**Omilitev:** Uvedite politike za omejitev števila zahtev, ki jih lahko AI agent pošlje storitvi. Omejevanje števila krogov v pogovoru in zahtev do vašega AI agenta je še en način za preprečitev teh vrst napadov.

### Zastrupljanje baze znanja

**Opis:** Ta vrsta napada ne cilja neposredno na AI agenta, ampak na bazo znanja in druge storitve, ki jih bo AI agent uporabljal. To lahko vključuje poškodovanje podatkov ali informacij, ki jih bo AI agent uporabil za opravljanje naloge in pri tem vodi do pristranskih ali nenamernih odzivov uporabniku.

**Omilitev:** Redno preverjajte podatke, ki jih bo AI agent uporabljal v svojih delovnih tokovih. Zagotovite, da je dostop do teh podatkov varen in jih lahko spreminjajo le zaupanja vredne osebe, da preprečite tovrstni napad.

### Verižne napake

**Opis:** AI agenti dostopajo do različnih orodij in storitev za opravljanje nalog. Napake, povzročene s strani napadalcev, lahko vodijo do okvar drugih sistemov, na katere je AI agent povezan, zaradi česar napad postane širši in težje odpravljiv.

**Omilitev:** Ena metoda za preprečevanje tega je, da AI agent deluje v omejenem okolju, na primer z izvajanjem nalog v Docker kontejnerju, da preprečimo neposredne napade na sistem. Ustvarjanje rezervnih mehanizmov in logike ponovnega poizkusa, ko določeni sistemi odgovorijo z napako, je še en način za preprečevanje večjih okvar sistema.

## Človeški nadzor

Še en učinkovit način za gradnjo zanesljivih AI agentnih sistemov je uporaba človeškega nadzora (Human-in-the-loop). To ustvari tok, kjer lahko uporabniki med izvajanjem procesujo povratne informacije agentom. Uporabniki v bistvu delujejo kot agenti v sistemu z več agenti s tem, da odobravajo ali prekinejo tekoči proces.

![Človek v zanki](../../../translated_images/sl/human-in-the-loop.5f0068a678f62f4f.webp)

Tukaj je primer kode, ki uporablja Microsoft Agent Framework, da pokaže, kako je ta koncept implementiran:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Ustvarite ponudnika z odobritvijo človeka v zanki
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Ustvarite agenta s korakom odobritve človeka
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Uporabnik lahko pregleda in odobri odgovor
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Zaključek

Gradnja zanesljivih AI agentov zahteva skrbno načrtovanje, robustne varnostne ukrepe in neprestano iteracijo. Z uvedbo strukturiranih sistemov meta pozivov, razumevanjem potencialnih groženj in uporabo strategij ublažitve lahko razvijalci ustvarijo AI agente, ki so varni in učinkoviti. Poleg tega vključitev človeškega nadzora zagotavlja, da AI agenti ostajajo usklajeni s potrebami uporabnikov, hkrati pa minimizirajo tveganja. Ker se AI še naprej razvija, bo ohranjanje proaktivnega pristopa k varnosti, zasebnosti in etičnim vidikom ključno za spodbujanje zaupanja in zanesljivosti v sistemih, ki temeljijo na AI.

## Primeri kode

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Demonstracija korak za korakom sistema meta-piskov sistemskih sporočil.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Pre-odobritvene gate, razvrščanje tveganj in beleženje revizij za zanesljive agente.

### Imate več vprašanj o gradnji zanesljivih AI agentov?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se srečate z drugimi učenci, udeležite ur pisarne in dobite odgovore na vaša vprašanja o AI agentih.

## Dodatni viri

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Pregled odgovorne uporabe AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Ocena generativnih AI modelov in AI aplikacij</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Varnostna sistemska sporočila</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Predloga za oceno tveganj</a>

## Prejšnja lekcija

[Agentni RAG](../05-agentic-rag/README.md)

## Naslednja lekcija

[Načrtovalni vzorec](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->