[![Pålitliga AI-agenter](../../../translated_images/sv/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klicka på bilden ovan för att se video av denna lektion)_

# Bygga pålitliga AI-agenter

## Introduktion

Denna lektion täcker:

- Hur man bygger och distribuerar säkra och effektiva AI-agenter
- Viktiga säkerhetsaspekter vid utveckling av AI-agenter.
- Hur man upprätthåller data- och användarintegritet vid utveckling av AI-agenter.

## Lärandemål

Efter att ha avslutat denna lektion kommer du att veta hur du:

- Identifierar och minskar risker vid skapande av AI-agenter.
- Implementerar säkerhetsåtgärder för att säkerställa att data och åtkomst hanteras korrekt.
- Skapar AI-agenter som bibehåller dataintegritet och erbjuder en kvalitativ användarupplevelse.

## Säkerhet

Låt oss först titta på att bygga säkra agentbaserade applikationer. Säkerhet innebär att AI-agenten presterar som avsett. Som byggare av agentbaserade applikationer har vi metoder och verktyg för att maximera säkerheten:

### Att bygga ett ramverk för systemmeddelanden

Om du någonsin har byggt en AI-applikation med stora språkmodeller (LLMs), vet du hur viktigt det är att utforma en robust system-prompt eller systemmeddelande. Dessa prompts fastställer metaregler, instruktioner och riktlinjer för hur LLM ska interagera med användaren och data.

För AI-agenter är system-prompten ännu viktigare eftersom AI-agenterna behöver mycket specifika instruktioner för att slutföra de uppgifter vi har utformat för dem.

För att skapa skalbara systemprompts kan vi använda ett ramverk för systemmeddelanden för att bygga en eller flera agenter i vår applikation:

![Bygga ett ramverk för systemmeddelanden](../../../translated_images/sv/system-message-framework.3a97368c92d11d68.webp)

#### Steg 1: Skapa ett meta systemmeddelande

Meta-prompten kommer att användas av en LLM för att generera systemprompts för de agenter vi skapar. Vi utformar den som en mall så att vi effektivt kan skapa flera agenter om det behövs.

Här är ett exempel på ett meta systemmeddelande som vi skulle ge till LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Steg 2: Skapa en grundläggande prompt

Nästa steg är att skapa en grundläggande prompt för att beskriva AI-agenten. Du bör inkludera agentens roll, vilka uppgifter agenten ska utföra och andra ansvarsområden för agenten.

Här är ett exempel:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Steg 3: Förse LLM med grundläggande systemmeddelande

Nu kan vi optimera detta systemmeddelande genom att tillhandahålla meta systemmeddelandet som systemmeddelande samt vårt grundläggande systemmeddelande.

Detta kommer att producera ett systemmeddelande som är bättre utformat för att vägleda våra AI-agenter:

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

Värdet av detta ramverk för systemmeddelanden är att kunna skala upp skapandet av systemmeddelanden från flera agenter enklare samt förbättra dina systemmeddelanden över tid. Det är sällan du får ett systemmeddelande som fungerar perfekt vid första försöket för ditt kompletta användningsfall. Att kunna göra små justeringar och förbättringar genom att ändra det grundläggande systemmeddelandet och köra det igen i systemet gör att du kan jämföra och utvärdera resultat.

## Förstå hot

För att bygga pålitliga AI-agenter är det viktigt att förstå och minska risker och hot mot din AI-agent. Låt oss titta på några av de olika hoten mot AI-agenter och hur du kan planera och förbereda dig bättre för dem.

![Förstå hot](../../../translated_images/sv/understanding-threats.89edeada8a97fc0f.webp)

### Uppgift och instruktion

**Beskrivning:** Angripare försöker ändra instruktionerna eller målen för AI-agenten genom att skapa promptar eller manipulera indata.

**Motåtgärd**: Kör valideringskontroller och indatagranskningar för att upptäcka potentiellt farliga promptar innan de bearbetas av AI-agenten. Eftersom dessa attacker vanligtvis kräver frekvent interaktion med agenten är en annan metod att begränsa antal turer i en konversation för att förhindra denna typ av attacker.

### Åtkomst till kritiska system

**Beskrivning**: Om en AI-agent har åtkomst till system och tjänster som lagrar känslig data, kan angripare kompromettera kommunikationen mellan agenten och dessa tjänster. Det kan vara direkta attacker eller indirekta försök att få information om dessa system via agenten.

**Motåtgärd**: AI-agenter bör bara ha åtkomst till system vid behov för att förhindra dessa typer av attacker. Kommunikation mellan agent och system ska också vara säker. Att implementera autentisering och åtkomstkontroll är ytterligare ett sätt att skydda denna information.

### Resurs- och tjänsteöverbelastning

**Beskrivning:** AI-agenter kan använda olika verktyg och tjänster för att utföra uppgifter. Angripare kan utnyttja denna förmåga för att attackera dessa tjänster genom att skicka ett stort antal förfrågningar via AI-agenten, vilket kan leda till systemfel eller höga kostnader.

**Motåtgärd:** Implementera riktlinjer för att begränsa antal förfrågningar en AI-agent kan göra till en tjänst. Att begränsa antal samtalsturer och förfrågningar till din AI-agent är också ett sätt att förhindra denna typ av attacker.

### Förgiftning av kunskapsbasen

**Beskrivning:** Den här typen av attack riktar sig inte direkt mot AI-agenten utan mot kunskapsbasen och andra tjänster som AI-agenten använder. Det kan innebära att data eller information som AI-agenten använder för att slutföra en uppgift korrumperas, vilket leder till partiska eller oavsiktliga svar till användaren.

**Motåtgärd:** Utför regelbunden verifiering av den data som AI-agenten använder i sina arbetsflöden. Säkerställ att åtkomst till denna data är säker och endast förändras av betrodda personer för att undvika denna typ av attacker.

### Kaskaderande fel

**Beskrivning:** AI-agenter använder olika verktyg och tjänster för att slutföra uppgifter. Fel orsakade av angripare kan leda till fel i andra system som AI-agenten är kopplad till, vilket gör attacken mer utbredd och svårare att felsöka.

**Motåtgärd**: En metod för att undvika detta är att låta AI-agenten arbeta i en begränsad miljö, till exempel utföra uppgifter i en Docker-container, för att förhindra direkta systemattacker. Att skapa fallback-mekanismer och retry-logik när vissa system svarar med fel är ett annat sätt att förhindra större systemfel.

## Människa-i-loopen

Ett annat effektivt sätt att bygga pålitliga AI-agent system är att använda människa-i-loopen. Detta skapar ett flöde där användare kan ge feedback till agenterna under körningen. Användare agerar i praktiken som agenter i ett multi-agent system och godkänner eller avbryter den pågående processen.

![Människa i loopen](../../../translated_images/sv/human-in-the-loop.5f0068a678f62f4f.webp)

Här är ett kodexempel som använder Microsoft Agent Framework för att visa hur detta koncept implementeras:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Skapa leverantören med mänsklig i loopen-godkännande
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Skapa agenten med ett steg för mänskligt godkännande
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Användaren kan granska och godkänna svaret
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Slutsats

Att bygga pålitliga AI-agenter kräver noggrann design, robusta säkerhetsåtgärder och kontinuerlig iteration. Genom att implementera strukturerade metaprompt-system, förstå potentiella hot och tillämpa åtgärder för att minska risker kan utvecklare skapa AI-agenter som både är säkra och effektiva. Dessutom säkerställer en människa-i-loopen-approach att AI-agenter förblir anpassade till användarens behov samtidigt som riskerna minimeras. Eftersom AI fortsätter att utvecklas kommer en proaktiv inställning till säkerhet, integritet och etiska överväganden vara avgörande för att främja förtroende och tillförlitlighet i AI-drivna system.

### Fler frågor om att bygga pålitliga AI-agenter?

Gå med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra lärande, delta i kontorstid och få svar på dina AI-agent-frågor.

## Ytterligare resurser

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Översikt över ansvarsfull AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Utvärdering av generativa AI-modeller och AI-applikationer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Säkerhetssystemmeddelanden</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Riskbedömningsmall</a>

## Föregående lektion

[Agentic RAG](../05-agentic-rag/README.md)

## Nästa lektion

[Planeringsdesignmönster](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör anses vara den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår på grund av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->