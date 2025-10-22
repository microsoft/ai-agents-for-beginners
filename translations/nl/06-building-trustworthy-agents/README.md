<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T17:25:12+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "nl"
}
-->
[![Betrouwbare AI-agenten](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.nl.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Betrouwbare AI-agenten bouwen

## Introductie

In deze les behandelen we:

- Hoe je veilige en effectieve AI-agenten bouwt en implementeert.
- Belangrijke beveiligingsoverwegingen bij het ontwikkelen van AI-agenten.
- Hoe je gegevens en gebruikersprivacy waarborgt bij het ontwikkelen van AI-agenten.

## Leerdoelen

Na het voltooien van deze les kun je:

- Risico's identificeren en beperken bij het creëren van AI-agenten.
- Beveiligingsmaatregelen implementeren om ervoor te zorgen dat gegevens en toegang goed worden beheerd.
- AI-agenten maken die gegevensprivacy waarborgen en een kwalitatieve gebruikerservaring bieden.

## Veiligheid

Laten we eerst kijken naar het bouwen van veilige agenttoepassingen. Veiligheid betekent dat de AI-agent presteert zoals ontworpen. Als ontwikkelaars van agenttoepassingen hebben we methoden en tools om de veiligheid te maximaliseren:

### Een systeemberichtframework bouwen

Als je ooit een AI-toepassing hebt gebouwd met behulp van Large Language Models (LLMs), weet je hoe belangrijk het is om een robuuste systeemprompt of systeembericht te ontwerpen. Deze prompts stellen de meta-regels, instructies en richtlijnen vast voor hoe de LLM met de gebruiker en gegevens omgaat.

Voor AI-agenten is de systeemprompt nog belangrijker, omdat de AI-agenten zeer specifieke instructies nodig hebben om de taken uit te voeren waarvoor we ze hebben ontworpen.

Om schaalbare systeemprompts te maken, kunnen we een systeemberichtframework gebruiken om één of meerdere agenten in onze toepassing te bouwen:

![Een systeemberichtframework bouwen](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.nl.png)

#### Stap 1: Maak een meta-systeembericht

De meta-prompt wordt door een LLM gebruikt om de systeemprompts te genereren voor de agenten die we maken. We ontwerpen het als een sjabloon, zodat we efficiënt meerdere agenten kunnen maken indien nodig.

Hier is een voorbeeld van een meta-systeembericht dat we aan de LLM zouden geven:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Stap 2: Maak een basisprompt

De volgende stap is het maken van een basisprompt om de AI-agent te beschrijven. Je moet de rol van de agent, de taken die de agent zal uitvoeren en andere verantwoordelijkheden van de agent opnemen.

Hier is een voorbeeld:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Stap 3: Basis-systeembericht aan LLM geven

Nu kunnen we dit systeembericht optimaliseren door het meta-systeembericht als systeembericht te gebruiken en ons basis-systeembericht toe te voegen.

Dit zal een systeembericht opleveren dat beter is ontworpen om onze AI-agenten te begeleiden:

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

#### Stap 4: Itereren en verbeteren

De waarde van dit systeemberichtframework is dat het gemakkelijker wordt om systeemberichten voor meerdere agenten te maken en om je systeemberichten in de loop van de tijd te verbeteren. Het is zeldzaam dat een systeembericht in één keer werkt voor je volledige use case. Door kleine aanpassingen en verbeteringen aan te brengen in het basis-systeembericht en dit door het systeem te laten lopen, kun je resultaten vergelijken en evalueren.

## Bedreigingen begrijpen

Om betrouwbare AI-agenten te bouwen, is het belangrijk om de risico's en bedreigingen voor je AI-agent te begrijpen en te beperken. Laten we enkele van de verschillende bedreigingen voor AI-agenten bekijken en hoe je hier beter op kunt plannen en je kunt voorbereiden.

![Bedreigingen begrijpen](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.nl.png)

### Taken en instructies

**Beschrijving:** Aanvallers proberen de instructies of doelen van de AI-agent te wijzigen door middel van prompts of manipulatie van invoer.

**Beperking:** Voer validatiecontroles en invoerfilters uit om potentieel gevaarlijke prompts te detecteren voordat ze door de AI-agent worden verwerkt. Aangezien deze aanvallen meestal frequente interactie met de agent vereisen, is het beperken van het aantal beurten in een gesprek een andere manier om dit soort aanvallen te voorkomen.

### Toegang tot kritieke systemen

**Beschrijving:** Als een AI-agent toegang heeft tot systemen en diensten die gevoelige gegevens opslaan, kunnen aanvallers de communicatie tussen de agent en deze diensten compromitteren. Dit kunnen directe aanvallen zijn of indirecte pogingen om informatie over deze systemen via de agent te verkrijgen.

**Beperking:** AI-agenten zouden alleen toegang moeten hebben tot systemen op basis van noodzaak om dit soort aanvallen te voorkomen. De communicatie tussen de agent en het systeem moet ook veilig zijn. Het implementeren van authenticatie en toegangscontrole is een andere manier om deze informatie te beschermen.

### Overbelasting van bronnen en diensten

**Beschrijving:** AI-agenten kunnen verschillende tools en diensten gebruiken om taken uit te voeren. Aanvallers kunnen deze mogelijkheid gebruiken om deze diensten aan te vallen door een groot aantal verzoeken via de AI-agent te sturen, wat kan leiden tot systeemstoringen of hoge kosten.

**Beperking:** Implementeer beleidsregels om het aantal verzoeken dat een AI-agent naar een dienst kan sturen te beperken. Het beperken van het aantal gesprekstappen en verzoeken aan je AI-agent is een andere manier om dit soort aanvallen te voorkomen.

### Vergiftiging van de kennisbasis

**Beschrijving:** Dit type aanval richt zich niet direct op de AI-agent, maar op de kennisbasis en andere diensten die de AI-agent zal gebruiken. Dit kan inhouden dat de gegevens of informatie die de AI-agent zal gebruiken om een taak uit te voeren, worden gecorrumpeerd, wat leidt tot bevooroordeelde of onbedoelde reacties aan de gebruiker.

**Beperking:** Voer regelmatige verificatie uit van de gegevens die de AI-agent zal gebruiken in zijn workflows. Zorg ervoor dat de toegang tot deze gegevens veilig is en alleen door vertrouwde personen wordt gewijzigd om dit soort aanvallen te voorkomen.

### Cascaderende fouten

**Beschrijving:** AI-agenten gebruiken verschillende tools en diensten om taken uit te voeren. Fouten veroorzaakt door aanvallers kunnen leiden tot storingen in andere systemen waarmee de AI-agent is verbonden, waardoor de aanval zich verder verspreidt en moeilijker te verhelpen is.

**Beperking:** Een methode om dit te voorkomen is om de AI-agent in een beperkte omgeving te laten werken, zoals het uitvoeren van taken in een Docker-container, om directe systeemaanvallen te voorkomen. Het creëren van fallback-mechanismen en retry-logica wanneer bepaalde systemen met een fout reageren, is een andere manier om grotere systeemstoringen te voorkomen.

## Mens-in-de-lus

Een andere effectieve manier om betrouwbare AI-agentensystemen te bouwen, is door gebruik te maken van een mens-in-de-lus. Dit creëert een proces waarbij gebruikers feedback kunnen geven aan de agenten tijdens de uitvoering. Gebruikers fungeren in feite als agenten in een multi-agentsysteem door goedkeuring te geven of het proces te beëindigen.

![Mens-in-de-lus](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.nl.png)

Hier is een codevoorbeeld met AutoGen om te laten zien hoe dit concept wordt geïmplementeerd:

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

## Conclusie

Het bouwen van betrouwbare AI-agenten vereist zorgvuldig ontwerp, robuuste beveiligingsmaatregelen en continue iteratie. Door gestructureerde meta-promptsystemen te implementeren, potentiële bedreigingen te begrijpen en mitigatiestrategieën toe te passen, kunnen ontwikkelaars AI-agenten creëren die zowel veilig als effectief zijn. Bovendien zorgt het opnemen van een mens-in-de-lus-benadering ervoor dat AI-agenten afgestemd blijven op de behoeften van gebruikers, terwijl risico's worden geminimaliseerd. Naarmate AI blijft evolueren, zal een proactieve houding ten aanzien van beveiliging, privacy en ethische overwegingen essentieel zijn om vertrouwen en betrouwbaarheid in AI-gedreven systemen te bevorderen.

### Meer vragen over het bouwen van betrouwbare AI-agenten?

Word lid van de [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) om andere leerlingen te ontmoeten, spreekuren bij te wonen en je vragen over AI-agenten beantwoord te krijgen.

## Aanvullende bronnen

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Overzicht van verantwoord gebruik van AI</a>  
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluatie van generatieve AI-modellen en AI-toepassingen</a>  
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Veiligheidssysteemberichten</a>  
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Risicobeoordelingssjabloon</a>  

## Vorige les

[Agentic RAG](../05-agentic-rag/README.md)

## Volgende les

[Planning Design Pattern](../07-planning-design/README.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.