[![Vertrouwbare AI-agenten](../../../translated_images/nl/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klik op de bovenstaande afbeelding om de video van deze les te bekijken)_

# Vertrouwbare AI-agenten bouwen

## Inleiding

Deze les behandelt:

- Hoe veilige en effectieve AI-agenten te bouwen en implementeren
- Belangrijke beveiligingsoverwegingen bij de ontwikkeling van AI-agenten.
- Hoe data- en gebruikersprivacy te waarborgen bij het ontwikkelen van AI-agenten.

## Leerdoelen

Na het voltooien van deze les weet je hoe je:

- Risico's identificeert en beperkt bij het creëren van AI-agenten.
- Beveiligingsmaatregelen implementeert om te zorgen dat data en toegang correct worden beheerd.
- AI-agenten maakt die data privacy respecteren en een kwalitatieve gebruikerservaring bieden.

## Veiligheid

Laten we eerst kijken naar het bouwen van veilige agentische toepassingen. Veiligheid betekent dat de AI-agent functioneert zoals ontworpen. Als bouwers van agentische toepassingen beschikken we over methoden en hulpmiddelen om veiligheid te maximaliseren:

### Een systeembericht-framework bouwen

Als je ooit een AI-toepassing hebt gebouwd met Large Language Models (LLM's), weet je hoe belangrijk het is om een robuuste systeem prompt of systeembericht te ontwerpen. Deze prompts stellen de meta-regels, instructies en richtlijnen vast voor hoe het LLM zal omgaan met de gebruiker en data.

Voor AI-agenten is de systeem prompt nog belangrijker omdat de AI-agenten zeer specifieke instructies nodig hebben om de taken die we voor hen hebben ontworpen uit te voeren.

Om schaalbare systeemprompts te maken, kunnen we een systeembericht-framework gebruiken voor het bouwen van één of meer agenten in onze toepassing:

![Een systeembericht-framework bouwen](../../../translated_images/nl/system-message-framework.3a97368c92d11d68.webp)

#### Stap 1: Maak een Meta Systeembericht

De meta-prompt wordt door een LLM gebruikt om de systeemprompts voor de agenten die wij maken te genereren. We ontwerpen het als een sjabloon zodat we efficiënt meerdere agenten kunnen aanmaken indien nodig.

Hier is een voorbeeld van een meta systeembericht dat we aan de LLM zouden geven:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Stap 2: Maak een basis prompt

De volgende stap is het maken van een basis prompt om de AI-agent te beschrijven. Je moet de rol van de agent, de taken die de agent zal uitvoeren, en andere verantwoordelijkheden van de agent opnemen.

Hier is een voorbeeld:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Stap 3: Voorzie Basis Systeembericht aan LLM

Nu kunnen we dit systeembericht optimaliseren door het meta systeembericht als systeembericht te geven samen met ons basis systeembericht.

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

#### Stap 4: Itereer en Verbeter

De waarde van dit systeembericht-framework is dat het makkelijker wordt om systeemberichten voor meerdere agenten te schalen en je systeemberichten in de loop van de tijd te verbeteren. Het is zeldzaam dat je een systeembericht hebt dat de eerste keer perfect werkt voor je volledig gebruiksscenario. Kleine aanpassingen en verbeteringen maken door het basis systeembericht te wijzigen en het door het systeem te halen stelt je in staat om resultaten te vergelijken en te evalueren.

## Dreigingen Begrijpen

Om vertrouwbare AI-agenten te bouwen, is het belangrijk om de risico's en dreigingen voor je AI-agent te begrijpen en verminderen. Laten we enkele verschillende dreigingen voor AI-agenten bekijken en hoe je beter kunt plannen en voorbereiden.

![Dreigingen begrijpen](../../../translated_images/nl/understanding-threats.89edeada8a97fc0f.webp)

### Taak en Instructie

**Beschrijving:** Aanvallers proberen de instructies of doelen van de AI-agent te wijzigen via prompting of het manipuleren van inputs.

**Beperking:** Voer validatiecontroles en invoerfilters uit om potentieel gevaarlijke prompts te detecteren voordat ze door de AI-agent verwerkt worden. Omdat deze aanvallen doorgaans frequente interactie met de agent vereisen, is het beperken van het aantal beurten in een gesprek een andere manier om dit soort aanvallen te voorkomen.

### Toegang tot Kritieke Systemen

**Beschrijving:** Als een AI-agent toegang heeft tot systemen en diensten die gevoelige data opslaan, kunnen aanvallers de communicatie tussen de agent en deze diensten compromitteren. Dit kunnen directe aanvallen zijn of indirecte pogingen informatie over deze systemen te verkrijgen via de agent.

**Beperking:** AI-agenten zouden toegang tot systemen alleen op basis van noodzaak mogen hebben om dit soort aanvallen te voorkomen. De communicatie tussen agent en systeem moet ook veilig zijn. Het implementeren van authenticatie en toegangscontrole is een andere manier om deze informatie te beschermen.

### Overbelasting van Middelen en Diensten

**Beschrijving:** AI-agenten kunnen verschillende tools en diensten gebruiken om taken te volbrengen. Aanvallers kunnen dit benutten om deze diensten aan te vallen door een hoog volume aan verzoeken via de AI-agent te sturen, wat kan leiden tot systeemstoringen of hoge kosten.

**Beperking:** Implementeer beleidsregels om het aantal verzoeken dat een AI-agent aan een dienst kan doen te beperken. Het beperken van het aantal gespreksturns en verzoeken aan je AI-agent is een andere manier om dit soort aanvallen tegen te gaan.

### Vergiftiging van de Kennisbasis

**Beschrijving:** Dit type aanval richt zich niet direct op de AI-agent, maar op de kennisbasis en andere diensten die de AI-agent gebruikt. Dit kan inhouden dat de data of informatie die de AI-agent gebruikt om een taak uit te voeren wordt gecorrumpeerd, wat leidt tot bevooroordeelde of ongewenste reacties aan de gebruiker.

**Beperking:** Voer regelmatige verificatie uit van de data die de AI-agent gebruikt in zijn workflows. Zorg ervoor dat de toegang tot deze data veilig is en alleen gewijzigd kan worden door vertrouwde personen om dit soort aanvallen te voorkomen.

### Cascaderende Fouten

**Beschrijving:** AI-agenten hebben toegang tot diverse tools en diensten om taken te voltooien. Fouten veroorzaakt door aanvallers kunnen leiden tot storingen in andere systemen waarmee de AI-agent is verbonden, waardoor de aanval zich verspreidt en moeilijker te troubleshooten is.

**Beperking:** Een manier om dit te vermijden is de AI-agent in een beperkte omgeving te laten werken, zoals taken uitvoeren in een Docker-container, om directe systeemaantallen te voorkomen. Het creëren van fallback-mechanismen en retry-logica wanneer bepaalde systemen fouten retourneren is een andere manier om grotere systeemstoringen tegen te gaan.

## Mens-in-de-Lus

Een andere effectieve manier om vertrouwbare AI-agenten te bouwen is door gebruik te maken van een Mens-in-de-lus. Dit creëert een proces waarbij gebruikers feedback kunnen geven aan de agenten tijdens het uitvoeren. Gebruikers fungeren feitelijk als agenten in een multi-agentensysteem en kunnen goedkeuring geven of het proces stoppen.

![Mens in de lus](../../../translated_images/nl/human-in-the-loop.5f0068a678f62f4f.webp)

Hier is een codevoorbeeld dat het concept toont met behulp van het Microsoft Agent Framework:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Maak de provider aan met menselijke tussentijdse goedkeuring
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
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

Het bouwen van vertrouwbare AI-agenten vereist zorgvuldige ontwerpkeuzes, robuuste beveiligingsmaatregelen en voortdurende iteratie. Door gestructureerde meta-promptsystemen te implementeren, potentiële dreigingen te begrijpen en mitigatiestrategieën toe te passen, kunnen ontwikkelaars AI-agenten creëren die zowel veilig als effectief zijn. Het integreren van een mens-in-de-lus aanpak zorgt er bovendien voor dat AI-agenten afgestemd blijven op de behoeften van gebruikers en minimaliseert risico's. Naarmate AI zich blijft ontwikkelen, blijft een proactieve houding ten aanzien van veiligheid, privacy en ethische overwegingen essentieel om vertrouwen en betrouwbaarheid in AI-gedreven systemen te bevorderen.

## Codevoorbeelden

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Stapsgewijze demonstratie van het meta-prompt systeembericht-framework.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Goedkeuringspoorten voor acties, risiconiveaus en auditlogging voor betrouwbare agenten.

### Meer vragen over het bouwen van vertrouwbare AI-agenten?

Word lid van de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere leerlingen te ontmoeten, deel te nemen aan kantoortijd en je vragen over AI-agenten beantwoord te krijgen.

## Aanvullende bronnen

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Overzicht Verantwoord AI-gebruik</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluatie van generatieve AI-modellen en AI-toepassingen</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Veiligheidssysteemberichten</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Risicobeoordelingssjabloon</a>

## Vorige les

[Agentic RAG](../05-agentic-rag/README.md)

## Volgende les

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->