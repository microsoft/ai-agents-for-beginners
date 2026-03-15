[![Trustworthy AI Agents](../../../translated_images/da/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_

# Bygning af Pålidelige AI-Agenter

## Introduktion

Denne lektion vil dække:

- Hvordan man bygger og implementerer sikre og effektive AI-agenter
- Vigtige sikkerhedsovervejelser ved udvikling af AI-agenter.
- Hvordan man opretholder data- og brugerprivatliv ved udvikling af AI-agenter.

## Læringsmål

Efter at have gennemført denne lektion vil du vide, hvordan du:

- Identificerer og mindsker risici ved oprettelse af AI-agenter.
- Implementerer sikkerhedsforanstaltninger for at sikre korrekt håndtering af data og adgang.
- Skaber AI-agenter, der opretholder dataprivatliv og giver en god brugeroplevelse.

## Sikkerhed

Lad os først se på at bygge sikre agent-baserede applikationer. Sikkerhed betyder, at AI-agenten fungerer som designet. Som bygherrer af agent-baserede applikationer har vi metoder og værktøjer til at maksimere sikkerheden:

### Bygning af et Systembeskedsframework

Hvis du nogensinde har bygget en AI-applikation ved hjælp af store sprogmodeller (LLMs), kender du vigtigheden af at designe en robust systemprompt eller systembesked. Disse prompts fastlægger de overordnede regler, instruktioner og retningslinjer for, hvordan LLM’en vil interagere med brugeren og data.

For AI-agenter er systemprompten endnu vigtigere, da AI-agenterne vil have brug for meget specifikke instruktioner for at udføre de opgaver, vi har designet til dem.

For at skabe skalerbare systemprompter kan vi bruge et systembeskedsframework til at bygge en eller flere agenter i vores applikation:

![Building a System Message Framework](../../../translated_images/da/system-message-framework.3a97368c92d11d68.webp)

#### Trin 1: Opret en Meta Systembesked

Meta-prompten bruges af en LLM til at generere systemprompter for de agenter, vi opretter. Vi designer den som en skabelon, så vi effektivt kan oprette flere agenter, hvis det er nødvendigt.

Her er et eksempel på en meta systembesked, vi ville give til LLM’en:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Trin 2: Opret en grundlæggende prompt

Næste trin er at oprette en grundlæggende prompt til at beskrive AI-agenten. Du bør inkludere agentens rolle, de opgaver agenten skal udføre, og eventuelle andre ansvarsområder agenten har.

Her er et eksempel:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Trin 3: Giv grundlæggende systembesked til LLM

Nu kan vi optimere denne systembesked ved at give meta systembeskeden som systembesked sammen med vores grundlæggende systembesked.

Dette vil producere en systembesked, der er bedre designet til at lede vores AI-agenter:

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

#### Trin 4: Iterer og forbedr

Værdien af dette systembeskedsframework er, at det gør det nemmere at skalere oprettelsen af systembeskeder fra flere agenter samt forbedre dine systembeskeder over tid. Det er sjældent, at du får en systembesked, der fungerer perfekt første gang for dit komplette brugsscenarie. At kunne lave små justeringer og forbedringer ved at ændre den grundlæggende systembesked og køre den igennem systemet giver dig mulighed for at sammenligne og evaluere resultater.

## Forstå Trusler

For at opbygge pålidelige AI-agenter er det vigtigt at forstå og mindske risici og trusler mod din AI-agent. Lad os se på nogle af de forskellige trusler mod AI-agenter og hvordan du bedre kan planlægge og forberede dig på dem.

![Understanding Threats](../../../translated_images/da/understanding-threats.89edeada8a97fc0f.webp)

### Opgave og Instruktion

**Beskrivelse:** Angribere forsøger at ændre instruktionerne eller målene for AI-agenten gennem prompting eller manipulation af input.

**Forebyggelse**: Udfør valideringstjek og inputfiltre for at opdage potentielt farlige prompts, før de behandles af AI-agenten. Da disse angreb typisk kræver hyppig interaktion med agenten, er det også en måde at forhindre disse angreb ved at begrænse antallet af udvekslinger i en samtale.

### Adgang til Kritiske Systemer

**Beskrivelse:** Hvis en AI-agent har adgang til systemer og tjenester, der gemmer følsomme data, kan angribere kompromittere kommunikationen mellem agenten og disse tjenester. Det kan være direkte angreb eller indirekte forsøg på at få oplysninger om disse systemer gennem agenten.

**Forebyggelse:** AI-agenter bør kun have adgang til systemer efter behov for at forhindre denne type angreb. Kommunikation mellem agenten og systemet skal også være sikker. Implementering af autentificering og adgangskontrol er en anden måde at beskytte disse oplysninger på.

### Ressource- og Serviceoverbelastning

**Beskrivelse:** AI-agenter kan få adgang til forskellige værktøjer og tjenester for at udføre opgaver. Angribere kan udnytte denne evne til at angribe tjenesterne ved at sende et højt volumen af forespørgsler gennem AI-agenten, hvilket kan resultere i systemfejl eller høje omkostninger.

**Forebyggelse:** Implementer politikker, der begrænser antallet af forespørgsler, en AI-agent kan sende til en service. At begrænse antallet af samtaleudvekslinger og forespørgsler til din AI-agent er en anden måde at forhindre denne type angreb på.

### Forgiftning af Vidensbase

**Beskrivelse:** Denne type angreb retter sig ikke direkte mod AI-agenten, men mod vidensbasen og andre tjenester, som AI-agenten vil bruge. Det kan involvere at korrumpere data eller information, som AI-agenten bruger til at udføre en opgave, hvilket fører til partiske eller utilsigtede svar til brugeren.

**Forebyggelse:** Udfør regelmæssig verifikation af de data, AI-agenten vil bruge i sine arbejdsprocesser. Sikr, at adgangen til disse data er sikker og kun kan ændres af betroede personer for at undgå denne type angreb.

### Kaskaderende Fejl

**Beskrivelse:** AI-agenter benytter forskellige værktøjer og tjenester for at udføre opgaver. Fejl forårsaget af angribere kan føre til fejl på andre systemer, som AI-agenten er forbundet med, hvilket gør angrebet mere udbredt og sværere at fejlfinde.

**Forebyggelse:** En metode til at undgå dette er at lade AI-agenten operere i et begrænset miljø, for eksempel ved at udføre opgaver i en Docker-container, for at forhindre direkte systemangreb. At oprette fallback-mekanismer og genforsøg- logik, når visse systemer svarer med fejl, er en anden måde at forhindre større systemfejl.

## Human-in-the-Loop

En anden effektiv måde at bygge pålidelige AI-agent systemer på er ved at anvende en Human-in-the-loop-tilgang. Dette skaber et flow, hvor brugere kan give feedback til agenterne under kørslen. Brugere fungerer i praksis som agenter i et multi-agent system ved at give godkendelse eller stoppe den kørende proces.

![Human in The Loop](../../../translated_images/da/human-in-the-loop.5f0068a678f62f4f.webp)

Her er et kodeeksempel ved hjælp af Microsoft Agent Framework, der viser, hvordan dette koncept implementeres:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Opret udbyderen med menneskelig-godkendelse
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Opret agenten med et menneskeligt godkendelsestrin
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Brugeren kan gennemgå og godkende svaret
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Konklusion

At bygge pålidelige AI-agenter kræver omhyggeligt design, robuste sikkerhedsforanstaltninger og løbende iteration. Ved at implementere strukturerede meta-promptsystemer, forstå potentielle trusler og anvende forebyggelsesstrategier kan udviklere skabe AI-agenter, der både er sikre og effektive. Derudover sikrer inddragelsen af en human-in-the-loop tilgang, at AI-agenter forbliver tilpasset brugerbehov, samtidig med at risici minimeres. Efterhånden som AI udvikler sig, vil en proaktiv tilgang til sikkerhed, privatliv og etiske overvejelser være nøglen til at skabe tillid og pålidelighed i AI-drevne systemer.

### Har du flere spørgsmål om at bygge pålidelige AI-agenter?

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre elever, deltage i office-timer og få svar på dine spørgsmål om AI-agenter.

## Yderligere Ressourcer

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Oversigt over Ansvarlig AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluering af generative AI-modeller og AI-applikationer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Sikkerhedssystembeskeder</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Risikovurderingsskabelon</a>

## Forrige Lektion

[Agentic RAG](../05-agentic-rag/README.md)

## Næste Lektion

[Planlægningsdesignmønster](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør anses for at være den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->