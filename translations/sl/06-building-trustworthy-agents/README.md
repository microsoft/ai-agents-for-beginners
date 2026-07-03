[![Zaupanja vredni AI agenti](../../../translated_images/sl/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite na sliko zgoraj za ogled videa tega poglavja)_

# Gradnja zaupanja vrednih AI agentov

## Uvod

To poglavje bo zajemalo:

- Kako zgraditi in uporabiti varne in učinkovite AI agente
- Pomembne varnostne premisleke pri razvoju AI agentov.
- Kako ohraniti zasebnost podatkov in uporabnikov pri razvoju AI agentov.

## Cilji učenja

Po zaključku tega poglavja boste znali:

- Prepoznati in ublažiti tveganja pri ustvarjanju AI agentov.
- Uvesti varnostne ukrepe za zagotovitev pravilnega upravljanja podatkov in dostopa.
- Ustvariti AI agente, ki ohranjajo zasebnost podatkov in zagotavljajo kakovostno uporabniško izkušnjo.

## Varnost

Najprej si poglejmo gradnjo varnih agentnih aplikacij. Varstvo pomeni, da AI agent deluje kot je zasnovan. Kot graditelji agentnih aplikacij imamo metode in orodja za maksimiranje varnosti:

### Gradnja ogrodja sistemskih sporočil

Če ste že kdaj gradili AI aplikacijo z uporabo velikih jezikovnih modelov (LLM), veste, kako pomembno je oblikovanje robustnega sistemskega navdiha ali sistemskega sporočila. Ti navdihi določajo meta pravila, navodila in smernice, kako bo LLM sodeloval z uporabnikom in podatki.

Za AI agente je sistemski navdih še pomembnejši, saj bodo agenti potrebovali zelo specifična navodila za dokončanje nalog, ki smo jih zanje zasnovali.

Za ustvarjanje razširljivih sistemskih navdihov lahko uporabimo ogrodje sistemskega sporočila za gradnjo enega ali več agentov v naši aplikaciji:

![Gradnja ogrodja sistemskih sporočil](../../../translated_images/sl/system-message-framework.3a97368c92d11d68.webp)

#### Korak 1: Ustvarite meta sistemsko sporočilo

Meta navdih bo uporabil LLM za generiranje sistemskih navdihov za agenta, ki jih ustvarjamo. Oblikujemo ga kot predlogo, da lahko učinkovito ustvarimo več agentov, če je to potrebno.

Tukaj je primer meta sistemskega sporočila, ki bi ga dali LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Korak 2: Ustvarite osnovni navdih

Naslednji korak je ustvariti osnovni navdih, ki opisuje AI agenta. Vključiti morate vlogo agenta, naloge, ki jih bo agent opravil, in vse druge odgovornosti agenta.

Tukaj je primer:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Korak 3: Posredujte osnovno sistemsko sporočilo LLM

Zdaj lahko optimiziramo to sistemsko sporočilo tako, da meta sistemsko sporočilo zagotovimo kot sistemsko sporočilo skupaj z našim osnovnim sistemskim sporočilom.

To bo ustvarilo sistemsko sporočilo, ki je bolje oblikovano za usmerjanje naših AI agentov:

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

#### Korak 4: Iterirajte in izboljšujte

Vrednost tega ogrodja sistemskih sporočil je v tem, da omogoča lažje razširjanje ustvarjanja sistemskih sporočil za več agentov ter izboljševanje vaših sistemskih sporočil skozi čas. Redko se zgodi, da bo sistemsko sporočilo delovalo popolno pri prvem poskusu za vaš celotni primer uporabe. Zmožnost manjših popravkov in izboljšav z menjavo osnovnega sistemskega sporočila in njegovo obdelavo skozi sistem vam bo omogočila primerjavo in oceno rezultatov.

## Razumevanje groženj

Za gradnjo zaupanja vrednih AI agentov je pomembno razumeti in ublažiti tveganja ter grožnje, ki grozijo vašemu AI agentu. Poglejmo le nekatere izmed različnih groženj AI agentom in kako se lahko bolje načrtujete in pripravite nanje.

![Razumevanje groženj](../../../translated_images/sl/understanding-threats.89edeada8a97fc0f.webp)

### Naloga in navodila

**Opis:** Napadalci skušajo spremeniti navodila ali cilje AI agenta preko spodbud ali manipulacije vhodnih podatkov.

**Ublažitev:** Izvedite validacijske preglede in filtre vhodnih podatkov za odkrivanje morebitno nevarnih spodbud pred obdelavo AI agenta. Ker ti napadi običajno zahtevajo pogosto interakcijo z agentom, je omejitev števila korakov v pogovoru še en način preprečevanja takšnih napadov.

### Dostop do kritičnih sistemov

**Opis:** Če ima AI agent dostop do sistemov in storitev, ki shranjujejo občutljive podatke, lahko napadalci ogrozijo komunikacijo med agentom in temi storitvami. To so lahko neposredni napadi ali posredni poskusi pridobitve informacij o teh sistemih preko agenta.

**Ublažitev:** AI agenti naj dostopajo do sistemov le po potrebi, da se preprečijo takšni napadi. Komunikacija med agentom in sistemom naj bo tudi varna. Uvedba avtentikacije in nadzora dostopa je še en način zaščite teh informacij.

### Preobremenitev virov in storitev

**Opis:** AI agenti lahko dostopajo do različnih orodij in storitev za opravljanje nalog. Napadalci lahko to zmožnost izrabijo za napad na te storitve, tako da preko AI agenta pošiljajo veliko število zahtevkov, kar lahko pripelje do okvar sistema ali visokih stroškov.

**Ublažitev:** Uvedite politike omejevanja števila zahtevkov, ki jih lahko AI agent pošlje storitvi. Omejevanje števila korakov pogovora in zahtevkov proti vašemu AI agentu je še en način preprečevanja teh napadov.

### Zastrupitev baze znanja

**Opis:** Ta vrsta napada ne cilja neposredno na AI agenta, ampak na bazo znanja in druge storitve, ki jih bo AI agent uporabljal. Lahko gre za poškodovanje podatkov ali informacij, ki jih bo AI agent uporabljal za dokončanje naloge, kar vodi do pristranskih ali neželenih odgovorov uporabniku.

**Ublažitev:** Redno preverjajte podatke, ki jih bo AI agent uporabljal v svojih delovnih tokovih. Zagotovite, da je dostop do teh podatkov varen in jih spreminjajo le zaupanja vredni posamezniki, da preprečite tovrstne napade.

### Verižne napake

**Opis:** AI agenti dostopajo do različnih orodij in storitev za opravljanje nalog. Napake, ki jih povzročijo napadalci, lahko povzročijo okvare drugih sistemov, s katerimi je AI agent povezan, zaradi česar postane napad bolj razširjen in je težje odpraviti napake.

**Ublažitev:** Eden izmed načinov za preprečevanje tega je, da AI agent deluje v omejenem okolju, na primer opravljanje nalog v Docker kontejnerju, da se preprečijo neposredni sistemi napadi. Ustvarjanje rezervnih mehanizmov in logike ponovnega poizkusa, ko določeni sistemi odgovorijo z napako, je še en način za preprečevanje večjih sistemskih okvar.

## Človek v zanki

Še en učinkovit način za gradnjo zaupanja vrednih sistemov AI agentov je uporaba človeka v zanki. To ustvari tok, kjer lahko uporabniki med izvajanjem zagotavljajo povratne informacije agentom. Uporabniki v bistvu delujejo kot agenti v sistemu z več agenti in s tem odobrijo ali prekinejo tečeči proces.

![Človek v zanki](../../../translated_images/sl/human-in-the-loop.5f0068a678f62f4f.webp)

Tukaj je prikaz kode z uporabo Microsoft Agent Framework za prikaz, kako je ta koncept implementiran:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Ustvarite ponudnika z odobritvijo s strani človeka v procesu
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Ustvarite agenta z korakom odobritve s strani človeka
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Uporabnik lahko pregleda in odobri odziv
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Zaključek

Gradnja zaupanja vrednih AI agentov zahteva skrbno načrtovanje, robustne varnostne ukrepe in nenehno iteracijo. Z izvajanjem strukturiranih meta spodbudnih sistemov, razumevanjem možnih groženj in uporabo strategij za ublažitev lahko razvijalci ustvarijo AI agente, ki so varni in učinkoviti. Poleg tega vključevanje pristopa človek v zanki zagotavlja, da AI agenti ostanejo usklajeni z uporabniškimi potrebami in hkrati zmanjšujejo tveganja. Ker se AI nenehno razvija, bo ohranjanje proaktivnega odnosa do varnosti, zasebnosti in etičnih premislekov ključno za spodbujanje zaupanja in zanesljivosti v sistemih, ki jih poganja AI.

## Vzorci kode

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Demonstracija ogrodja meta-sporočil sistemskih spodbud korak za korakom.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Vrata za odobritev pred akcijo, razvrščanje tveganj in beleženje revizij za zaupanja vredne agente.

### Imate še več vprašanj o gradnji zaupanja vrednih AI agentov?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kjer se lahko srečate z drugimi učenci, udeležite ur za pomoč in dobite odgovore na vprašanja o AI agentih.

## Dodatni viri

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Pregled odgovorne uporabe AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Ocena generativnih AI modelov in AI aplikacij</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Varnostna sistemska sporočila</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Predloga za oceno tveganja</a>

## Prejšnje poglavje

[Agentni RAG](../05-agentic-rag/README.md)

## Naslednje poglavje

[Načrtovalni oblikovni vzorec](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->