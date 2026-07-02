[![Zanesljivi AI agenti](../../../translated_images/sl/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite zgornjo sliko za ogled videa te lekcije)_

# Gradnja zanesljivih AI agentov

## Uvod

Ta lekcija bo zajemala:

- Kako zgraditi in uvesti varne in učinkovite AI agente
- Pomembna varnostna vprašanja pri razvoju AI agentov.
- Kako ohraniti zasebnost podatkov in uporabnikov pri razvoju AI agentov.

## Cilji učenja

Po zaključku te lekcije boste znali:

- Prepoznati in ublažiti tveganja pri ustvarjanju AI agentov.
- Uvesti varnostne ukrepe za pravilno upravljanje podatkov in dostopa.
- Ustvariti AI agente, ki ohranjajo zasebnost podatkov in zagotavljajo kakovostno uporabniško izkušnjo.

## Varnost

Najprej si poglejmo, kako zgraditi varne agentne aplikacije. Varnost pomeni, da AI agent deluje tako, kot je zasnovano. Kot graditelji agentnih aplikacij imamo metode in orodja za maksimiranje varnosti:

### Gradnja okvira sistemskega sporočila

Če ste že kdaj gradili AI aplikacijo z uporabo velikih jezikovnih modelov (LLM), veste, kako pomembno je oblikovati robusten sistemski poziv ali sistemsko sporočilo. Ti pozivi vzpostavijo meta pravila, navodila in smernice za interakcijo LLM z uporabnikom in podatki.

Za AI agente je sistemski poziv še pomembnejši, saj bodo AI agenti potrebovali zelo specifična navodila za opravljanje nalog, ki smo jih zanje zasnovali.

Za ustvarjanje razširljivih sistemskih pozivov lahko uporabimo okvir sistemskih sporočil za gradnjo enega ali več agentov v naši aplikaciji:

![Gradnja okvira sistemskega sporočila](../../../translated_images/sl/system-message-framework.3a97368c92d11d68.webp)

#### Korak 1: Ustvarite meta sistemsko sporočilo 

Meta poziv bo uporabil LLM za generiranje sistemskih pozivov za agente, ki jih ustvarjamo. Oblikujemo ga kot predlogo, da bomo lahko učinkovito ustvarili več agentov, če bo potrebno.

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

#### Korak 3: Sistemskemu modelu zagotovite osnovno sistemsko sporočilo

Zdaj lahko to sistemsko sporočilo optimiziramo tako, da damo meta sistemsko sporočilo kot sistemsko sporočilo in našo osnovno sistemsko sporočilo.

To bo ustvarilo sistemsko sporočilo, ki je bolje zasnovano za usmerjanje naših AI agentov:

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

#### Korak 4: Iterirajte in izboljšajte

Vrednost tega okvira sistemskih sporočil je v tem, da omogoča lažje razširjanje ustvarjanja sistemskih sporočil za več agentov, pa tudi izboljševanje vaših sistemskih sporočil skozi čas. Redko se zgodi, da vam bo sistemsko sporočilo delovalo prvič za celoten primer uporabe. Možnost majhnih popravkov in izboljšav z menjavo osnovnega sistemskega sporočila in njegovo obdelavo skozi sistem vam bo omogočila primerjavo in ocenjevanje rezultatov.

## Razumevanje groženj

Za gradnjo zanesljivih AI agentov je pomembno razumeti in ublažiti tveganja in grožnje vašemu AI agentu. Poglejmo le nekatere izmed različnih groženj za AI agente in kako se nanje bolje pripraviti.

![Razumevanje groženj](../../../translated_images/sl/understanding-threats.89edeada8a97fc0f.webp)

### Naloga in navodila

**Opis:** Napadalci poskušajo spremeniti navodila ali cilje AI agenta s pozivanjem ali manipulacijo vhodnih podatkov.

**Ublažitev**: Izvedite preverjanja veljavnosti in filtre vhodnih podatkov, da zaznate potencialno nevarne pozive pred obdelavo AI agentu. Ker ti napadi običajno zahtevajo pogoste interakcije z agentom, je omejevanje števila izmenjav v pogovoru še en način preprečevanja teh vrst napadov.

### Dostop do kritičnih sistemov

**Opis:** Če ima AI agent dostop do sistemov in storitev, ki hranijo občutljive podatke, lahko napadalci ogrozijo komunikacijo med agentom in temi storitvami. To so lahko neposredni napadi ali poskusi posrednih informacij o teh sistemih preko agenta.

**Ublažitev:** Dostop AI agentov do sistemov naj bo omejen na nujne primere, da se preprečijo tovrstni napadi. Komunikacija med agentom in sistemom naj bo tudi varna. Uvedba overjanja in nadzora dostopa je še en način zaščite teh informacij.

### Prekomerna obremenitev virov in storitev

**Opis:** AI agenti lahko dostopajo do različnih orodij in storitev za opravljanje nalog. Napadalci lahko to sposobnost uporabijo za napad na te storitve s pošiljanjem velikega števila zahtevkov preko AI agenta, kar lahko povzroči okvare sistema ali visoke stroške.

**Ublažitev:** Uvedite politike za omejevanje števila zahtevkov, ki jih lahko AI agent pošlje na posamezno storitev. Omejevanje števila izmenjav v pogovoru in zahtev do vašega AI agenta je še en način preprečevanja teh vrst napadov.

### Zastrupitev baze znanja

**Opis:** Ta vrsta napada ni neposredno usmerjena na AI agenta, temveč na bazo znanja in druge storitve, ki jih bo AI agent uporabil. Lahko vključuje korupcijo podatkov ali informacij, ki jih AI agent uporablja za opravljanje nalog, kar vodi v pristranske ali neželene odzive uporabniku.

**Ublažitev:** Redno preverjajte podatke, ki jih bo AI agent uporabljal v svojih procesih. Zagotovite, da je dostop do teh podatkov varen in da jih lahko spreminjajo le zaupanja vredni posamezniki, da se izognete temu tipu napada.

### Verižno napake

**Opis:** AI agenti dostopajo do različnih orodij in storitev za opravljanje nalog. Napake, ki jih povzročijo napadalci, lahko privedejo do okvar drugih sistemov, s katerimi je AI agent povezan, zaradi česar napad postane širši in težje rešljivi.

**Ublažitev**: Ena metoda za preprečevanje tega je, da AI agent deluje v omejenem okolju, na primer z izvajanjem nalog v Docker vsebnku, da se preprečijo neposredni napadi na sistem. Ustvarjanje mehanizmov za povratno rešitev in logike ponovnega poskusa, kadar se nekateri sistemi odzovejo z napako, je še en način za preprečevanje večjih okvar sistema.

## Človek v zanki

Drug učinkovit način gradnje zanesljivih AI agentnih sistemov je uporaba človeka v zanki. To ustvari tok, kjer lahko uporabniki med izvajanjem zagotavljajo povratne informacije agentom. Uporabniki v bistvu delujejo kot agenti v sistemu z več agenti in zagotavljajo potrditev ali prekinitev laufajočega procesa.

![Človek v zanki](../../../translated_images/sl/human-in-the-loop.5f0068a678f62f4f.webp)

Tukaj je primer kode z uporabo Microsoft Agent Framework, ki prikazuje, kako je ta koncept implementiran:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Ustvari ponudnika z odobritvijo s človekom v zanki
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Ustvari agenta z odobritvenim korakom človeka
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

Gradnja zanesljivih AI agentov zahteva skrbno načrtovanje, robustne varnostne ukrepe in stalno iteracijo. Z uvajanjem strukturiranih sistemov meta-pozivanja, razumevanjem potencialnih groženj in uvajanjem strategij ublažitve lahko razvijalci ustvarijo AI agente, ki so hkrati varni in učinkoviti. Poleg tega vključitev človeka v zanko zagotavlja, da AI agenti ostanejo usklajeni s potrebami uporabnikov, hkrati pa zmanjšujejo tveganja. Ker se AI še naprej razvija, bo ključnega pomena, da ohranjamo proaktiven pristop k varnosti, zasebnosti in etičnim vprašanjem za spodbujanje zaupanja in zanesljivosti v sistemih, ki jih poganja AI.

## Primeri kode

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Prikaz okvira sistemskega sporočila meta-poziva korak za korakom.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Vrata za odobritev pred dejanjem, rangiranje tveganja in revizijsko beleženje za zanesljive agente.

### Imate več vprašanj o gradnji zanesljivih AI agentov?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kjer se lahko srečate z drugimi učenci, udeležite ur svetovanja in dobite odgovore na vaša vprašanja o AI agentih.

## Dodatni viri

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Pregled odgovorne uporabe AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Ocena generativnih AI modelov in AI aplikacij</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Varna sistemska sporočila</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Predloga ocene tveganja</a>

## Prejšnja lekcija

[Agentni RAG](../05-agentic-rag/README.md)

## Naslednja lekcija

[Načrtovalni vzorec](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->