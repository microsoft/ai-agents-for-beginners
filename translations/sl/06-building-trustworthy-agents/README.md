[![Zaupljivi AI agenti](../../../translated_images/sl/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite na zgornjo sliko za ogled videa tega lekcije)_

# Gradnja zaupljivih AI agentov

## Uvod

Ta lekcija bo zajemala:

- Kako zgraditi in implementirati varne in učinkovite AI agente
- Pomembne varnostne premisleke pri razvoju AI agentov
- Kako ohraniti zasebnost podatkov in uporabnikov pri razvoju AI agentov

## Cilji učenja

Po končani tej lekciji boste znali:

- Prepoznati in omejiti tveganja pri ustvarjanju AI agentov
- Izvesti varnostne ukrepe za pravilno upravljanje podatkov in dostopa
- Ustvariti AI agente, ki ohranjajo zasebnost podatkov in nudijo kakovostno uporabniško izkušnjo

## Varnost

Najprej poglejmo gradnjo varnih agenčnih aplikacij. Varnost pomeni, da AI agent deluje kot je zasnovano. Kot graditelji agenčnih aplikacij imamo metode in orodja za maksimiranje varnosti:

### Gradnja okvira sistemskih sporočil

Če ste že kdaj zgradili AI aplikacijo z uporabo velikih jezikovnih modelov (LLM), veste, kako pomembno je oblikovati robustni sistemski poziv ali sistemsko sporočilo. Ti pozivi določajo meta pravila, navodila in smernice za to, kako bo LLM sodeloval z uporabnikom in podatki.

Za AI agente je sistemski poziv še pomembnejši, saj bodo AI agenti potrebovali zelo natančna navodila za dokončanje nalog, ki smo jih zanje zasnovali.

Za ustvarjanje razširljivih sistemskih pozivov lahko uporabimo okvir sistemskih sporočil za gradnjo enega ali več agentov v naši aplikaciji:

![Gradnja okvira sistemskih sporočil](../../../translated_images/sl/system-message-framework.3a97368c92d11d68.webp)

#### Korak 1: Ustvari Meta sistemsko sporočilo

Meta poziv bo uporabil LLM za generiranje sistemskih pozivov za agente, ki jih ustvarjamo. Oblikujemo ga kot predlogo, da lahko učinkovito ustvarimo več agentov, če je potrebno.

Tukaj je primer meta sistemskega sporočila, ki bi ga dali LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Korak 2: Ustvari osnovni poziv

Naslednji korak je ustvariti osnovni poziv za opis AI agenta. Vključiti morate vlogo agenta, naloge, ki jih bo agent opravil, in druge odgovornosti agenta.

Tukaj je primer:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Korak 3: Posreduj osnovno sistemsko sporočilo LLM

Zdaj lahko optimiziramo to sistemsko sporočilo tako, da posredujemo meta sistemsko sporočilo kot sistemsko sporočilo in naše osnovno sistemsko sporočilo.

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

#### Korak 4: Iteriraj in izboljšaj

Vrednost tega okvira sistemskih sporočil je, da lahko lažje skaliramo ustvarjanje sistemskih sporočil iz več agentov, pa tudi izboljšujemo sistemska sporočila skozi čas. Redko boste imeli sistemsko sporočilo, ki deluje prvič za vaš celoten primer uporabe. Sposobnost majhnih popravkov in izboljšav z menjavo osnovnega sistemskega sporočila in ponovnim zagonom skozi sistem vam omogoča primerjanje in ocenjevanje rezultatov.

## Razumevanje groženj

Za gradnjo zaupljivih AI agentov je pomembno razumeti in omejiti tveganja ter grožnje vašemu AI agentu. Poglejmo le nekaj različnih groženj AI agentom in kako se nanje bolje pripraviti.

![Razumevanje groženj](../../../translated_images/sl/understanding-threats.89edeada8a97fc0f.webp)

### Naloga in navodila

**Opis:** Napadalci poskušajo spremeniti navodila ali cilje AI agenta s spodbujanjem ali manipulacijo vhodnih podatkov.

**Omejitev**: Izvedite preverjanja in filtre vhodnih podatkov, da zaznate potencialno nevarne pozive, preden jih obdeluje AI agent. Ker ti napadi običajno zahtevajo pogoste interakcije z agentom, je omejevanje števila potez v pogovoru drug način preprečevanja tovrstnih napadov.

### Dostop do kritičnih sistemov

**Opis:** Če ima AI agent dostop do sistemov in storitev, ki hranijo občutljive podatke, lahko napadalci ogrozijo komunikacijo med agentom in temi storitvami. To so lahko neposredni napadi ali poskusi pridobitve informacij o teh sistemih preko agenta.

**Omejitev:** AI agenti naj imajo dostop do sistemov le, če je to nujno potrebno, da se preprečijo tovrstni napadi. Komunikacija med agentom in sistemom naj bo tudi varna. Uvedba overjanja in nadzora dostopa je še en način zaščite teh podatkov.

### Preobremenitev virov in storitev

**Opis:** AI agenti lahko dostopajo do različnih orodij in storitev za izpolnitev nalog. Napadalci lahko izkoristijo to zmožnost za napad na te storitve z velikim številom zahtev preko AI agenta, kar lahko povzroči okvare sistema ali visoke stroške.

**Omejitev:** Uvedite politike za omejitev števila zahtev, ki jih lahko AI agent pošlje storitvi. Omejevanje števila potez v pogovoru in zahtev vašemu AI agentu je še en način preprečevanja tovrstnih napadov.

### Zastrupitev baze znanja

**Opis:** Ta vrsta napada ne cilja neposredno na AI agenta, temveč na bazo znanja in druge storitve, ki jih AI agent uporablja. To lahko vključuje poškodovanje podatkov ali informacij, ki jih AI agent uporablja za opravljanje naloge, kar vodi v pristranske ali neželene odzive uporabniku.

**Omejitev:** Redno preverjajte podatke, ki jih AI agent uporablja v svojih delovnih tokovih. Zagotovite, da je dostop do teh podatkov varen in da jih spreminjajo le zaupanja vredni posamezniki, da se izognete tej vrsti napada.

### Kaskadne napake

**Opis:** AI agenti dostopajo do različnih orodij in storitev za opravljanje nalog. Napake, ki jih povzročijo napadalci, lahko vodijo do okvar drugih sistemov, ki so povezani z AI agentom, zaradi česar postane napad širši in težje odpravljiv.

**Omejitev:** Ena metoda za izogibanje temu je, da AI agent deluje v omejenem okolju, na primer izvaja naloge v Docker kontejnerju, da prepreči neposredne sisteme napade. Ustvarjanje rezervnih mehanizmov in logike ponovnih poskusov, ko določeni sistemi vrnejo napako, je še en način preprečevanja večjih okvar sistema.

## Človek v zanki

Drug učinkovit način za gradnjo zaupljivih sistemov AI agentov je uporaba človeka v zanki. Ta pristop ustvari tok, kjer uporabniki lahko med izvajanjem podajo povratne informacije agentom. Uporabniki v bistvu delujejo kot agenti v sistemu z več agenti in dajejo odobritve ali prekinejo izvajanje procesa.

![Človek v zanki](../../../translated_images/sl/human-in-the-loop.5f0068a678f62f4f.webp)

Tukaj je primer kode, ki uporablja Microsoft Agent Framework in pokaže, kako je ta koncept implementiran:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Ustvarite ponudnika z odobritvijo človeka v zanki
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Ustvarite agenta s korakom človeške odobritve
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

Gradnja zaupljivih AI agentov zahteva skrbno zasnovo, robustne varnostne ukrepe in neprekinjeno iteracijo. Z izvedbo strukturiranih meta pozivnih sistemov, razumevanjem potencialnih groženj in uporabo strategij omejevanja, lahko razvijalci ustvarijo AI agente, ki so varni in učinkoviti. Poleg tega vključevanje pristopa človeka v zanki zagotavlja, da AI agenti ostajajo usklajeni z uporabniškimi potrebami, hkrati pa zmanjšujejo tveganja. Ker AI nadaljuje svoj razvoj, bo vzdrževanje proaktivnega pristopa do varnosti, zasebnosti in etičnih premislekov ključnega pomena za spodbujanje zaupanja in zanesljivosti v sistemih, ki jih poganja AI.

### Imate več vprašanj o gradnji zaupljivih AI agentov?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), da se srečate z drugimi učenci, udeležite ur svetovalcev in dobite odgovore na vaša vprašanja o AI agentih.

## Dodatni viri

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Pregled odgovorne uporabe AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Ocena generativnih AI modelov in AI aplikacij</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Varnostna sistemska sporočila</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Predloga ocene tveganja</a>

## Prejšnja lekcija

[Agentic RAG](../05-agentic-rag/README.md)

## Naslednja lekcija

[Oblikovni vzorec načrtovanja](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->