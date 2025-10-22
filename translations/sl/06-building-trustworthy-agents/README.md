<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T23:15:38+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "sl"
}
-->
[![Zanesljivi AI agenti](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.sl.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite na zgornjo sliko za ogled videa te lekcije)_

# Gradnja zanesljivih AI agentov

## Uvod

V tej lekciji bomo obravnavali:

- Kako zgraditi in implementirati varne ter učinkovite AI agente.
- Pomembne varnostne vidike pri razvoju AI agentov.
- Kako ohraniti zasebnost podatkov in uporabnikov pri razvoju AI agentov.

## Cilji učenja

Po zaključku te lekcije boste znali:

- Prepoznati in zmanjšati tveganja pri ustvarjanju AI agentov.
- Uvesti varnostne ukrepe za ustrezno upravljanje podatkov in dostopa.
- Ustvariti AI agente, ki ohranjajo zasebnost podatkov in zagotavljajo kakovostno uporabniško izkušnjo.

## Varnost

Najprej si poglejmo, kako zgraditi varne aplikacije z agenti. Varnost pomeni, da AI agent deluje skladno z načrtom. Kot razvijalci aplikacij z agenti imamo metode in orodja za maksimiranje varnosti:

### Gradnja okvirja za sistemska sporočila

Če ste že kdaj gradili AI aplikacijo z uporabo velikih jezikovnih modelov (LLM), veste, kako pomembno je oblikovati robusten sistemski poziv ali sistemsko sporočilo. Ta sporočila določajo meta pravila, navodila in smernice za interakcijo LLM z uporabnikom in podatki.

Za AI agente so sistemska sporočila še pomembnejša, saj potrebujejo zelo specifična navodila za izvedbo nalog, ki smo jih zanje zasnovali.

Za ustvarjanje skalabilnih sistemskih sporočil lahko uporabimo okvir za sistemska sporočila, ki omogoča gradnjo enega ali več agentov v naši aplikaciji:

![Gradnja okvirja za sistemska sporočila](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.sl.png)

#### Korak 1: Ustvarite meta sistemsko sporočilo

Meta poziv bo uporabljen s strani LLM za generiranje sistemskih sporočil za agente, ki jih ustvarimo. Oblikujemo ga kot predlogo, da lahko po potrebi učinkovito ustvarimo več agentov.

Tukaj je primer meta sistemskega sporočila, ki bi ga posredovali LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Korak 2: Ustvarite osnovni poziv

Naslednji korak je ustvariti osnovni poziv za opis AI agenta. Vključiti morate vlogo agenta, naloge, ki jih bo agent opravljal, in vse druge odgovornosti agenta.

Tukaj je primer:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Korak 3: Posredujte osnovno sistemsko sporočilo LLM

Zdaj lahko optimiziramo to sistemsko sporočilo tako, da meta sistemsko sporočilo uporabimo kot sistemsko sporočilo in dodamo naše osnovno sistemsko sporočilo.

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

#### Korak 4: Iteracija in izboljšave

Vrednost tega okvirja za sistemska sporočila je v tem, da omogoča lažje ustvarjanje sistemskih sporočil za več agentov ter izboljšanje sistemskih sporočil skozi čas. Redko boste imeli sistemsko sporočilo, ki bo delovalo že ob prvi uporabi za celoten primer uporabe. Zmožnost izvajanja manjših prilagoditev in izboljšav z spreminjanjem osnovnega sistemskega sporočila ter ponovnim zagonom sistema vam omogoča primerjavo in ocenjevanje rezultatov.

## Razumevanje groženj

Za gradnjo zanesljivih AI agentov je pomembno razumeti in zmanjšati tveganja ter grožnje, ki vplivajo na vašega AI agenta. Poglejmo si nekaj različnih groženj za AI agente in kako se nanje bolje pripraviti.

![Razumevanje groženj](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.sl.png)

### Naloge in navodila

**Opis:** Napadalci poskušajo spremeniti navodila ali cilje AI agenta z manipulacijo pozivov ali vhodnih podatkov.

**Zmanjšanje tveganja:** Izvajajte preverjanja veljavnosti in filtre vhodnih podatkov za zaznavanje potencialno nevarnih pozivov, preden jih obdela AI agent. Ker te vrste napadov običajno zahtevajo pogoste interakcije z agentom, je omejevanje števila korakov v pogovoru še en način za preprečevanje teh napadov.

### Dostop do kritičnih sistemov

**Opis:** Če ima AI agent dostop do sistemov in storitev, ki hranijo občutljive podatke, lahko napadalci kompromitirajo komunikacijo med agentom in temi storitvami. To so lahko neposredni napadi ali poskusi pridobivanja informacij o teh sistemih prek agenta.

**Zmanjšanje tveganja:** AI agenti naj imajo dostop do sistemov le po potrebi, da preprečite tovrstne napade. Komunikacija med agentom in sistemom naj bo varna. Uvedba avtentikacije in nadzora dostopa je še en način za zaščito teh informacij.

### Preobremenitev virov in storitev

**Opis:** AI agenti lahko dostopajo do različnih orodij in storitev za izvedbo nalog. Napadalci lahko to sposobnost izkoristijo za napad na te storitve z velikim številom zahtevkov prek AI agenta, kar lahko povzroči odpoved sistemov ali visoke stroške.

**Zmanjšanje tveganja:** Uvedite politike za omejevanje števila zahtevkov, ki jih AI agent lahko pošlje storitvi. Omejevanje števila korakov v pogovoru in zahtevkov vašemu AI agentu je še en način za preprečevanje teh napadov.

### Zastrupitev baze znanja

**Opis:** Ta vrsta napada ne cilja neposredno na AI agenta, temveč na bazo znanja in druge storitve, ki jih AI agent uporablja. To lahko vključuje korupcijo podatkov ali informacij, ki jih AI agent uporablja za izvedbo naloge, kar vodi do pristranskih ali nenamernih odzivov uporabniku.

**Zmanjšanje tveganja:** Redno preverjajte podatke, ki jih AI agent uporablja v svojih delovnih tokovih. Poskrbite, da je dostop do teh podatkov varen in da jih lahko spreminjajo le zaupanja vredne osebe, da preprečite tovrstne napade.

### Verižne napake

**Opis:** AI agenti dostopajo do različnih orodij in storitev za izvedbo nalog. Napake, ki jih povzročijo napadalci, lahko vodijo do odpovedi drugih sistemov, s katerimi je AI agent povezan, kar povzroči širši napad, ki ga je težje odpraviti.

**Zmanjšanje tveganja:** Ena od metod za preprečevanje tega je, da AI agent deluje v omejenem okolju, kot je izvajanje nalog v Docker kontejnerju, da preprečite neposredne napade na sistem. Ustvarjanje mehanizmov za povratne ukrepe in logike ponovnega poskusa, ko določeni sistemi vrnejo napako, je še en način za preprečevanje večjih odpovedi sistema.

## Človek v zanki

Še en učinkovit način za gradnjo zanesljivih sistemov AI agentov je uporaba pristopa "človek v zanki". To ustvari tok, kjer lahko uporabniki med izvajanjem procesa podajo povratne informacije agentom. Uporabniki v bistvu delujejo kot agenti v večagentnem sistemu, saj odobravajo ali ustavljajo tekoče procese.

![Človek v zanki](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.sl.png)

Tukaj je primer kode z uporabo AutoGen, ki prikazuje, kako je ta koncept implementiran:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Zaključek

Gradnja zanesljivih AI agentov zahteva skrbno načrtovanje, robustne varnostne ukrepe in stalno iteracijo. Z implementacijo strukturiranih sistemov za meta pozive, razumevanjem potencialnih groženj in uporabo strategij za zmanjšanje tveganj lahko razvijalci ustvarijo AI agente, ki so varni in učinkoviti. Poleg tega vključitev pristopa "človek v zanki" zagotavlja, da AI agenti ostanejo usklajeni s potrebami uporabnikov, hkrati pa zmanjšujejo tveganja. Ker se AI še naprej razvija, bo ohranjanje proaktivnega pristopa k varnosti, zasebnosti in etičnim vidikom ključno za spodbujanje zaupanja in zanesljivosti v sistemih, ki jih poganja AI.

### Imate več vprašanj o gradnji zanesljivih AI agentov?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kjer se lahko povežete z drugimi učenci, udeležite uradnih ur in dobite odgovore na svoja vprašanja o AI agentih.

## Dodatni viri

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Pregled odgovorne uporabe AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Vrednotenje generativnih AI modelov in aplikacij</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Varnostna sistemska sporočila</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Predloga za oceno tveganj</a>

## Prejšnja lekcija

[Agentic RAG](../05-agentic-rag/README.md)

## Naslednja lekcija

[Načrtovanje vzorca oblikovanja](../07-planning-design/README.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.