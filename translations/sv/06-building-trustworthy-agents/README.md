<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T15:25:41+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "sv"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.sv.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klicka på bilden ovan för att se videon för denna lektion)_

# Bygga pålitliga AI-agenter

## Introduktion

Denna lektion kommer att täcka:

- Hur man bygger och distribuerar säkra och effektiva AI-agenter.
- Viktiga säkerhetsaspekter vid utveckling av AI-agenter.
- Hur man upprätthåller dataskydd och användarens integritet vid utveckling av AI-agenter.

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna:

- Identifiera och hantera risker vid skapandet av AI-agenter.
- Implementera säkerhetsåtgärder för att säkerställa att data och åtkomst hanteras korrekt.
- Skapa AI-agenter som upprätthåller dataintegritet och ger en högkvalitativ användarupplevelse.

## Säkerhet

Låt oss först titta på hur man bygger säkra agentiska applikationer. Säkerhet innebär att AI-agenten fungerar som avsett. Som utvecklare av agentiska applikationer har vi metoder och verktyg för att maximera säkerheten:

### Bygga ett ramverk för systemmeddelanden

Om du någonsin har byggt en AI-applikation med hjälp av stora språkmodeller (LLMs) vet du hur viktigt det är att designa en robust systemprompt eller ett systemmeddelande. Dessa meddelanden fastställer de övergripande reglerna, instruktionerna och riktlinjerna för hur LLM ska interagera med användaren och data.

För AI-agenter är systemprompten ännu viktigare eftersom AI-agenter behöver mycket specifika instruktioner för att utföra de uppgifter vi har designat för dem.

För att skapa skalbara systemprompter kan vi använda ett ramverk för systemmeddelanden för att bygga en eller flera agenter i vår applikation:

![Bygga ett ramverk för systemmeddelanden](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.sv.png)

#### Steg 1: Skapa ett metasystemmeddelande

Metaprompten kommer att användas av en LLM för att generera systemprompter för de agenter vi skapar. Vi designar det som en mall så att vi effektivt kan skapa flera agenter vid behov.

Här är ett exempel på ett metasystemmeddelande som vi skulle ge till LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Steg 2: Skapa en grundläggande prompt

Nästa steg är att skapa en grundläggande prompt för att beskriva AI-agenten. Du bör inkludera agentens roll, de uppgifter agenten ska utföra och andra ansvarsområden för agenten.

Här är ett exempel:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Steg 3: Tillhandahåll grundläggande systemmeddelande till LLM

Nu kan vi optimera detta systemmeddelande genom att tillhandahålla metasystemmeddelandet som systemmeddelande och vårt grundläggande systemmeddelande.

Detta kommer att producera ett systemmeddelande som är bättre designat för att vägleda våra AI-agenter:

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

#### Steg 4: Iterera och förbättra

Värdet av detta ramverk för systemmeddelanden är att det gör det enklare att skala skapandet av systemmeddelanden för flera agenter samt förbättra dina systemmeddelanden över tid. Det är sällan du har ett systemmeddelande som fungerar perfekt första gången för hela användningsfallet. Genom att göra små justeringar och förbättringar av det grundläggande systemmeddelandet och köra det genom systemet kan du jämföra och utvärdera resultaten.

## Förstå hot

För att bygga pålitliga AI-agenter är det viktigt att förstå och hantera riskerna och hoten mot din AI-agent. Låt oss titta på några av de olika hoten mot AI-agenter och hur du bättre kan planera och förbereda dig för dem.

![Förstå hot](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.sv.png)

### Uppgifter och instruktioner

**Beskrivning:** Angripare försöker ändra instruktionerna eller målen för AI-agenten genom att manipulera promptar eller indata.

**Åtgärd:** Utför valideringskontroller och filtrering av indata för att upptäcka potentiellt farliga promptar innan de behandlas av AI-agenten. Eftersom dessa attacker vanligtvis kräver frekvent interaktion med agenten kan du begränsa antalet turer i en konversation för att förhindra denna typ av attacker.

### Åtkomst till kritiska system

**Beskrivning:** Om en AI-agent har åtkomst till system och tjänster som lagrar känslig data kan angripare kompromettera kommunikationen mellan agenten och dessa tjänster. Detta kan vara direkta attacker eller indirekta försök att få information om dessa system via agenten.

**Åtgärd:** AI-agenter bör endast ha åtkomst till system vid behov för att förhindra denna typ av attacker. Kommunikation mellan agenten och systemet bör också vara säker. Implementera autentisering och åtkomstkontroll som ytterligare skydd.

### Överbelastning av resurser och tjänster

**Beskrivning:** AI-agenter kan använda olika verktyg och tjänster för att utföra uppgifter. Angripare kan utnyttja denna förmåga för att attackera dessa tjänster genom att skicka en hög volym av förfrågningar via AI-agenten, vilket kan leda till systemfel eller höga kostnader.

**Åtgärd:** Implementera policyer för att begränsa antalet förfrågningar en AI-agent kan göra till en tjänst. Att begränsa antalet konversationsturer och förfrågningar till din AI-agent är ett annat sätt att förhindra denna typ av attacker.

### Förgiftning av kunskapsbas

**Beskrivning:** Denna typ av attack riktar sig inte direkt mot AI-agenten utan mot kunskapsbasen och andra tjänster som AI-agenten använder. Detta kan innebära att data eller information som AI-agenten använder för att utföra en uppgift korrumperas, vilket leder till partiska eller oavsiktliga svar till användaren.

**Åtgärd:** Utför regelbunden verifiering av den data som AI-agenten använder i sina arbetsflöden. Säkerställ att åtkomst till denna data är säker och endast ändras av betrodda individer för att undvika denna typ av attack.

### Kaskadfel

**Beskrivning:** AI-agenter använder olika verktyg och tjänster för att utföra uppgifter. Fel orsakade av angripare kan leda till att andra system som AI-agenten är ansluten till misslyckas, vilket gör attacken mer omfattande och svårare att felsöka.

**Åtgärd:** Ett sätt att undvika detta är att låta AI-agenten arbeta i en begränsad miljö, som att utföra uppgifter i en Docker-container, för att förhindra direkta systemattacker. Att skapa fallback-mekanismer och återförsökslogik när vissa system svarar med ett fel är ett annat sätt att förhindra större systemfel.

## Människa i loopen

Ett annat effektivt sätt att bygga pålitliga AI-agentsystem är att använda en människa i loopen. Detta skapar ett flöde där användare kan ge feedback till agenterna under körningen. Användare fungerar i princip som agenter i ett multi-agent-system genom att godkänna eller avbryta den pågående processen.

![Människa i loopen](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.sv.png)

Här är ett kodexempel som använder AutoGen för att visa hur detta koncept implementeras:

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

## Slutsats

Att bygga pålitliga AI-agenter kräver noggrann design, robusta säkerhetsåtgärder och kontinuerlig iteration. Genom att implementera strukturerade metasystem för promptar, förstå potentiella hot och tillämpa åtgärdsstrategier kan utvecklare skapa AI-agenter som är både säkra och effektiva. Dessutom säkerställer användningen av en människa i loopen att AI-agenter förblir anpassade till användarens behov samtidigt som riskerna minimeras. När AI fortsätter att utvecklas kommer det att vara avgörande att upprätthålla ett proaktivt förhållningssätt till säkerhet, integritet och etiska överväganden för att främja förtroende och tillförlitlighet i AI-drivna system.

### Har du fler frågor om att bygga pålitliga AI-agenter?

Gå med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra elever, delta i öppet hus och få svar på dina frågor om AI-agenter.

## Ytterligare resurser

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Ansvarsfull AI-översikt</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Utvärdering av generativa AI-modeller och AI-applikationer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Säkerhetssystemmeddelanden</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Mall för riskbedömning</a>

## Föregående lektion

[Agentic RAG](../05-agentic-rag/README.md)

## Nästa lektion

[Planeringsdesignmönster](../07-planning-design/README.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.