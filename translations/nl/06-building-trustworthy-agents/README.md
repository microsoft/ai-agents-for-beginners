[![Betrouwbare AI-agenten](../../../translated_images/nl/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Betrouwbare AI-agenten bouwen

## Introductie

Deze les behandelt:

- Hoe veilige en effectieve AI-agenten te bouwen en te implementeren
- Belangrijke beveiligingsoverwegingen bij het ontwikkelen van AI-agenten.
- Hoe data- en gebruikersprivacy te waarborgen bij het ontwikkelen van AI-agenten.

## Leerdoelen

Na het voltooien van deze les weet je hoe je:

- Risico’s herkent en beperkt bij het creëren van AI-agenten.
- Beveiligingsmaatregelen implementeert om te zorgen dat data en toegang goed worden beheerd.
- AI-agenten maakt die data privacy respecteren en een kwalitatieve gebruikerservaring bieden.

## Veiligheid

Laten we eerst kijken naar het bouwen van veilige agentachtige applicaties. Veiligheid betekent dat de AI-agent werkt zoals ontworpen. Als bouwers van agentachtige applicaties hebben we methoden en tools om veiligheid te maximaliseren:

### Een systeem-bericht framework bouwen

Als je ooit een AI-applicatie hebt gebouwd met Large Language Models (LLM’s), weet je hoe belangrijk het is om een robuuste systeem prompt of systeembericht te ontwerpen. Deze prompts bepalen de metaregels, instructies en richtlijnen voor hoe de LLM met de gebruiker en data omgaat.

Voor AI-agenten is de systeem prompt nog belangrijker omdat de AI-agenten zeer specifieke instructies nodig hebben om de taken te voltooien die wij voor hen hebben ontworpen.

Om schaalbare systeem prompts te maken, kunnen we een systeem-bericht framework gebruiken om een of meerdere agenten in onze applicatie te bouwen:

![Een systeem-bericht framework bouwen](../../../translated_images/nl/system-message-framework.3a97368c92d11d68.webp)

#### Stap 1: Maak een Meta Systeembericht

De metaprompt wordt gebruikt door een LLM om de systeem prompts voor de agenten die we creëren te genereren. We ontwerpen het als een sjabloon zodat we efficiënt meerdere agenten kunnen maken indien nodig.

Hier is een voorbeeld van een meta systeembericht dat we aan de LLM zouden geven:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Stap 2: Maak een basis prompt

De volgende stap is het maken van een basis prompt om de AI-agent te beschrijven. Je zou de rol van de agent, de taken die de agent uitvoert, en andere verantwoordelijkheden van de agent moeten opnemen.

Hier is een voorbeeld:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Stap 3: Voorzie de basis systeembericht aan LLM

Nu kunnen we dit systeembericht optimaliseren door het meta systeembericht als systeembericht te geven en ons basis systeembericht.

Dit zal een systeembericht opleveren dat beter ontworpen is om onze AI-agenten te begeleiden:

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

#### Stap 4: Itereer en verbeter

De waarde van dit systeem-bericht framework is dat het maken van systeemberichten van meerdere agenten makkelijker te schalen is én dat je je systeemberichten in de loop van de tijd kunt verbeteren. Het is zeldzaam dat je meteen een systeembericht hebt dat werkt voor jouw volledige use case. Kleine aanpassingen kunnen gedaan worden door het basis systeembericht te wijzigen en het door het systeem te laten lopen, zodat je de resultaten kunt vergelijken en evalueren.

## Dreigingen begrijpen

Om betrouwbare AI-agenten te bouwen, is het belangrijk om de risico’s en dreigingen voor je AI-agent te begrijpen en te beperken. Laten we kijken naar enkele verschillende dreigingen voor AI-agenten en hoe je hier beter op kunt plannen en voorbereiden.

![Dreigingen begrijpen](../../../translated_images/nl/understanding-threats.89edeada8a97fc0f.webp)

### Taak en Instructie

**Beschrijving:** Aanvallers proberen de instructies of doelen van de AI-agent te veranderen via prompten of manipulatie van inputs.

**Beperking**: Voer validatiechecks en inputfilters uit om potentieel gevaarlijke prompts te detecteren voordat ze door de AI-agent worden verwerkt. Omdat deze aanvallen meestal frequente interactie met de agent vereisen, is het beperken van het aantal beurten in een gesprek ook een manier om dit soort aanvallen te voorkomen.

### Toegang tot kritieke systemen

**Beschrijving:** Als een AI-agent toegang heeft tot systemen en diensten die gevoelige data opslaan, kunnen aanvallers de communicatie tussen de agent en deze diensten compromitteren. Dit kunnen directe aanvallen zijn of indirecte pogingen om via de agent informatie over deze systemen te verkrijgen.

**Beperking:** AI-agenten moeten alleen toegang hebben tot systemen op basis van noodzaak om dit soort aanvallen te voorkomen. Communicatie tussen agent en systeem moet daarnaast ook veilig zijn. Authenticatie en toegangscontrole implementeren is een andere manier om deze informatie te beschermen.

### Overbelasting van middelen en diensten

**Beschrijving:** AI-agenten gebruiken verschillende tools en diensten om taken te voltooien. Aanvallers kunnen dit misbruiken door een grote hoeveelheid verzoeken via de AI-agent te sturen, wat kan leiden tot systeemuitval of hoge kosten.

**Beperking:** Implementeer beleidsregels om het aantal verzoeken dat een AI-agent naar een dienst kan sturen te beperken. Het beperken van het aantal gesprekbeurten en verzoeken aan je AI-agent is een andere manier om dit soort aanvallen te voorkomen.

### Vergiftiging van kennisbasis

**Beschrijving:** Dit type aanval richt zich niet rechtstreeks op de AI-agent, maar op de kennisbasis en andere diensten die de AI-agent gebruikt. Dit kan corruptie van data of informatie inhouden, wat leidt tot bevooroordeelde of onbedoelde antwoorden aan de gebruiker.

**Beperking:** Voer regelmatig controles uit op de data die de AI-agent gebruikt in zijn workflows. Zorg dat toegang tot deze data veilig is en alleen gewijzigd wordt door vertrouwde personen om dit soort aanvallen te vermijden.

### Kettingreactie van fouten

**Beschrijving:** AI-agenten gebruiken diverse tools en diensten om taken te voltooien. Fouten veroorzaakt door aanvallers kunnen leiden tot uitval van andere systemen waarop de AI-agent is aangesloten, waardoor de aanval zich uitbreidt en moeilijker te verhelpen is.

**Beperking**: Een manier om dit te voorkomen is de AI-agent te laten opereren in een beperkte omgeving, zoals taken uitvoeren in een Docker container, om directe systeemaanvallen te voorkomen. Het creëren van fallback-mechanismen en retry-logica wanneer systemen een foutmelding geven, is een andere manier om grotere systeemuitval te voorkomen.

## Mens in de lus

Een andere effectieve manier om betrouwbare AI-agent systemen te bouwen is met een Mens-in-de-lus. Dit creëert een proces waarbij gebruikers feedback kunnen geven aan de agenten tijdens het uitvoeren. Gebruikers functioneren in feite als agenten in een multi-agent systeem door goedkeuring te geven of het lopende proces te beëindigen.

![Mens in de lus](../../../translated_images/nl/human-in-the-loop.5f0068a678f62f4f.webp)

Hier is een codevoorbeeld met het Microsoft Agent Framework om te laten zien hoe dit concept wordt geïmplementeerd:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Maak de provider aan met menselijke goedkeuring in de lus
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Maak de agent aan met een menselijke goedkeuringsstap
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# De gebruiker kan de reactie beoordelen en goedkeuren
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Conclusie

Het bouwen van betrouwbare AI-agenten vereist zorgvuldige ontwerpkeuzes, robuuste beveiligingsmaatregelen en voortdurende iteratie. Door gestructureerde meta prompting systemen te implementeren, potentiële dreigingen te begrijpen en mitigerende strategieën toe te passen, kunnen ontwikkelaars AI-agenten creëren die zowel veilig als effectief zijn. Daarnaast zorgt de toepassing van een mens-in-de-lus benadering ervoor dat AI-agenten afgestemd blijven op de behoeften van gebruikers terwijl risico’s worden geminimaliseerd. Naarmate AI zich verder ontwikkelt, blijft een proactieve houding ten aanzien van beveiliging, privacy en ethische overwegingen de sleutel tot het bevorderen van vertrouwen en betrouwbaarheid in AI-gestuurde systemen.

## Codevoorbeelden

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Stap-voor-stap demonstratie van het meta-prompt systeembericht-framework.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Goedkeuringspoorten voorafgaand aan acties, risicoclassificatie en auditlogs voor betrouwbare agenten.

### Meer vragen over het bouwen van betrouwbare AI-agenten?

Word lid van de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere lerenden te ontmoeten, kantooruren bij te wonen en je vragen over AI-agenten beantwoord te krijgen.

## Extra bronnen

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Overzicht Verantwoordelijke AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluatie van generatieve AI-modellen en AI-toepassingen</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Veiligheid systeemberichten</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Template Risicobeoordeling</a>

## Vorige les

[Agentic RAG](../05-agentic-rag/README.md)

## Volgende les

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->