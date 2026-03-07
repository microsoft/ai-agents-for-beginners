[![Vertrouwde AI Agents](../../../translated_images/nl/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Vertrouwde AI Agents bouwen

## Introductie

Deze les behandelt:

- Hoe veilige en effectieve AI Agents te bouwen en te implementeren
- Belangrijke beveiligingsoverwegingen bij het ontwikkelen van AI Agents.
- Hoe gegevens- en privacy van gebruikers te waarborgen bij het ontwikkelen van AI Agents.

## Leerdoelen

Na het voltooien van deze les weet je hoe je:

- Risico's kunt identificeren en verminderen bij het creëren van AI Agents.
- Beveiligingsmaatregelen kunt implementeren om te zorgen dat gegevens en toegang goed beheerd worden.
- AI Agents maakt die de privacy van gegevens behouden en een kwalitatieve gebruikerservaring bieden.

## Veiligheid

Laten we eerst kijken naar het bouwen van veilige agent-gebaseerde applicaties. Veiligheid betekent dat de AI-agent presteert zoals ontworpen. Als bouwers van agent-gebaseerde applicaties hebben we methoden en tools om de veiligheid te maximaliseren:

### Het bouwen van een Systeem Boodschappen Framework

Als je ooit een AI-applicatie hebt gebouwd met Large Language Models (LLM's), weet je hoe belangrijk het is om een robuuste systeem prompt of systeem boodschap te ontwerpen. Deze prompts stellen de metaregels, instructies en richtlijnen vast voor hoe het LLM zal communiceren met de gebruiker en data.

Voor AI Agents is de systeem prompt nog belangrijker omdat AI Agents zeer specifieke instructies nodig hebben om de taken te voltooien die we voor hen hebben ontworpen.

Om schaalbare systeem prompts te creëren, kunnen we een systeem boodschap framework gebruiken om één of meerdere agents in onze applicatie te bouwen:

![Het bouwen van een Systeem Boodschappen Framework](../../../translated_images/nl/system-message-framework.3a97368c92d11d68.webp)

#### Stap 1: Maak een Meta Systeem Boodschap

De meta prompt wordt gebruikt door een LLM om de systeem prompts voor de agents die we creëren te genereren. We ontwerpen deze als een sjabloon, zodat we meerdere agents efficiënt kunnen creëren indien nodig.

Hier is een voorbeeld van een meta systeem boodschap die we aan het LLM zouden geven:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Stap 2: Maak een basis prompt

De volgende stap is het maken van een basis prompt om de AI Agent te beschrijven. Je moet de rol van de agent, de taken die de agent zal voltooien, en eventuele andere verantwoordelijkheden van de agent opnemen.

Hier is een voorbeeld:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Stap 3: Verstrek basis Systeem Boodschap aan LLM

Nu kunnen we deze systeem boodschap optimaliseren door de meta systeem boodschap te gebruiken als systeem boodschap en onze basis systeem boodschap toe te voegen.

Dit zal een systeem boodschap opleveren die beter ontworpen is om onze AI agents te begeleiden:

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

#### Stap 4: Itereren en Verbeteren

De waarde van dit systeem boodschap framework is dat het makkelijker wordt om systeem boodschappen van meerdere agents te schalen, evenals om je systeem boodschappen in de loop van de tijd te verbeteren. Het is zeldzaam dat je een systeem boodschap hebt die de eerste keer voor je volledige use case werkt. Kleine aanpassingen en verbeteringen maken door de basis systeem boodschap te wijzigen en te laten uitvoeren via het systeem stelt je in staat om resultaten te vergelijken en te evalueren.

## Dreigingen Begrijpen

Om vertrouwde AI agents te bouwen, is het belangrijk om de risico's en dreigingen voor je AI agent te begrijpen en te verminderen. Laten we kijken naar enkele van de verschillende dreigingen voor AI agents en hoe je hier beter op kunt plannen en voorbereiden.

![Dreigingen Begrijpen](../../../translated_images/nl/understanding-threats.89edeada8a97fc0f.webp)

### Taak en Instructie

**Beschrijving:** Aanvallers proberen de instructies of doelen van de AI agent te wijzigen via prompting of het manipuleren van invoer.

**Mitigatie**: Voer validatiecontroles en invoerfilters uit om mogelijke gevaarlijke prompts te detecteren vóórdat ze door de AI Agent worden verwerkt. Omdat deze aanvallen meestal frequente interactie met de Agent vereisen, is het beperken van het aantal stappen in een gesprek een andere manier om deze soorten aanvallen te voorkomen.

### Toegang tot Kritieke Systemen

**Beschrijving**: Als een AI agent toegang heeft tot systemen en diensten die gevoelige data opslaan, kunnen aanvallers de communicatie tussen de agent en deze diensten compromitteren. Dit kunnen directe aanvallen zijn of indirecte pogingen om informatie over deze systemen via de agent te verkrijgen.

**Mitigatie**: AI agents moeten alleen op basis van noodzaak toegang hebben tot systemen om dit soort aanvallen te voorkomen. De communicatie tussen de agent en het systeem moet ook veilig zijn. Het implementeren van authenticatie en toegangscontrole is een andere manier om deze informatie te beschermen.

### Overbelasting van Resources en Diensten

**Beschrijving:** AI agents kunnen verschillende tools en diensten benaderen om taken te voltooien. Aanvallers kunnen deze mogelijkheid misbruiken om deze diensten aan te vallen door een hoog volume aan verzoeken via de AI Agent te sturen, wat kan leiden tot systeemuitval of hoge kosten.

**Mitigatie:** Implementeer beleid om het aantal verzoeken dat een AI agent kan doen aan een dienst te beperken. Het beperken van het aantal gespreksturns en verzoeken aan je AI agent is een andere manier om dit soort aanvallen te voorkomen.

### Vergiftiging van de Kennisbasis

**Beschrijving:** Dit type aanval richt zich niet direct op de AI agent, maar richt zich op de kennisbasis en andere diensten die de AI agent zal gebruiken. Dit kan het corrupt maken van data of informatie inhouden die de AI agent gebruikt om een taak te voltooien, wat leidt tot bevooroordeelde of ongewenste reacties aan de gebruiker.

**Mitigatie:** Voer regelmatige verificatie uit van de data die de AI agent zal gebruiken in zijn workflows. Zorg dat de toegang tot deze data veilig is en alleen door vertrouwde personen wordt gewijzigd om dit type aanval te vermijden.

### Cascaderende Fouten

**Beschrijving:** AI agents gebruiken verschillende tools en diensten om taken uit te voeren. Fouten veroorzaakt door aanvallers kunnen leiden tot uitval van andere systemen waar de AI agent mee verbonden is, waardoor de aanval zich verspreidt en moeilijker te verhelpen is.

**Mitigatie**: Een manier om dit te voorkomen is ervoor te zorgen dat de AI Agent in een beperkte omgeving opereert, zoals taken uitvoeren in een Docker-container, om directe systeemaanvallen te voorkomen. Het creëren van fallback-mechanismen en retry-logica wanneer bepaalde systemen met een fout reageren, is een andere manier om grotere systeemuitval te voorkomen.

## Mens-in-de-Lus

Een andere effectieve manier om vertrouwde AI Agent systemen te bouwen is het gebruik van een Mens-in-de-lus. Dit creëert een proces waarbij gebruikers feedback kunnen geven aan de Agents tijdens het uitvoeren. Gebruikers fungeren als agents binnen een multi-agent systeem en kunnen goedkeuring of beëindiging van het lopende proces geven.

![Mens in de Lus](../../../translated_images/nl/human-in-the-loop.5f0068a678f62f4f.webp)

Hier is een codefragment met het Microsoft Agent Framework om te laten zien hoe dit concept wordt geïmplementeerd:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Maak de provider met menselijke goedkeuring
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Maak de agent met een menselijke goedkeuringsstap
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# De gebruiker kan de reactie bekijken en goedkeuren
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Conclusie

Het bouwen van vertrouwde AI agents vereist zorgvuldig ontwerp, robuuste beveiligingsmaatregelen en voortdurende iteratie. Door gestructureerde meta-promptsystemen te implementeren, potentiële dreigingen te begrijpen en mitigatiestrategieën toe te passen, kunnen ontwikkelaars AI agents maken die zowel veilig als effectief zijn. Daarnaast zorgt het integreren van een mens-in-de-lus aanpak ervoor dat AI agents afgestemd blijven op de behoeften van gebruikers terwijl risico’s worden geminimaliseerd. Naarmate AI zich blijft ontwikkelen, zal het handhaven van een proactieve houding ten aanzien van beveiliging, privacy en ethische overwegingen essentieel zijn om vertrouwen en betrouwbaarheid in op AI gebaseerde systemen te bevorderen.

### Nog meer vragen over het bouwen van vertrouwde AI Agents?

Sluit je aan bij de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere lerenden te ontmoeten, deel te nemen aan spreekuren en antwoorden op je AI Agents vragen te krijgen.

## Aanvullende bronnen

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Overzicht Verantwoord AI-gebruik</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluatie van generatieve AI-modellen en AI-toepassingen</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Veiligheid systeem boodschappen</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Sjabloon Risicobeoordeling</a>

## Vorige les

[Agentic RAG](../05-agentic-rag/README.md)

## Volgende les

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel wij streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onjuistheden kunnen bevatten. Het originele document in de oorspronkelijke taal dient als de gezaghebbende bron te worden beschouwd. Voor belangrijke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->