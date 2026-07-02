[![Pålitelige AI-agenter](../../../translated_images/no/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klikk på bildet over for å se video av denne leksjonen)_

# Bygge pålitelige AI-agenter

## Introduksjon

Denne leksjonen vil dekke:

- Hvordan bygge og distribuere trygge og effektive AI-agenter
- Viktige sikkerhetshensyn ved utvikling av AI-agenter.
- Hvordan opprettholde data- og brukervennlighet ved utvikling av AI-agenter.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du vite hvordan du:

- Identifiserer og reduserer risikoer ved opprettelse av AI-agenter.
- Implementerer sikkerhetstiltak for å sikre at data og tilgang håndteres korrekt.
- Lager AI-agenter som bevarer dataprivacy og gir en god brukeropplevelse.

## Sikkerhet

La oss først se på å bygge trygge agentiske applikasjoner. Sikkerhet betyr at AI-agenten opptrer som designet. Som utviklere av agentiske applikasjoner har vi metoder og verktøy for å maksimere sikkerheten:

### Bygge et systemmeldingsrammeverk

Hvis du noen gang har bygget en AI-applikasjon ved hjelp av store språkmodeller (LLMs), vet du hvor viktig det er å lage en robust systemprompt eller systemmelding. Disse promptene fastsetter meta-reglene, instruksjonene og retningslinjene for hvordan LLM-en skal samhandle med brukeren og data.

For AI-agenter er systemprompten enda viktigere siden AI-agentene vil trenge svært spesifikke instruksjoner for å fullføre oppgavene vi har designet for dem.

For å lage skalerbare systemprompter kan vi bruke et systemmeldingsrammeverk for å bygge en eller flere agenter i applikasjonen vår:

![Bygge et systemmeldingsrammeverk](../../../translated_images/no/system-message-framework.3a97368c92d11d68.webp)

#### Steg 1: Lag en Meta systemmelding

Meta-prompten vil bli brukt av en LLM for å generere systempromptene til agentene vi lager. Vi designer den som en mal slik at vi effektivt kan lage flere agenter om nødvendig.

Her er et eksempel på en meta systemmelding vi vil gi til LLM-en:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Steg 2: Lag en grunnleggende prompt

Neste steg er å lage en grunnleggende prompt som beskriver AI-agenten. Du bør inkludere agentens rolle, oppgavene agenten skal fullføre, og eventuelle andre ansvarsområder agenten har.

Her er et eksempel:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Steg 3: Gi grunnleggende systemmelding til LLM

Nå kan vi optimalisere denne systemmeldingen ved å gi meta systemmeldingen som systemmelding sammen med vår grunnleggende systemmelding.

Dette vil produsere en systemmelding som er bedre designet for å veilede våre AI-agenter:

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

#### Steg 4: Iterer og forbedre

Verdien av dette systemmeldingsrammeverket er å kunne skalere opprettelse av systemmeldinger for flere agenter enklere, i tillegg til å forbedre systemmeldingene dine over tid. Det er sjeldent du vil ha en systemmelding som fungerer helt fra starten for hele brukstilfellet ditt. Å kunne gjøre små justeringer og forbedringer ved å endre den grunnleggende systemmeldingen og kjøre den gjennom systemet lar deg sammenligne og evaluere resultater.

## Forstå trusler

For å bygge pålitelige AI-agenter er det viktig å forstå og redusere risiko og trusler mot AI-agenten din. La oss se på bare noen av de forskjellige truslene mot AI-agenter og hvordan du kan planlegge bedre og forberede deg på dem.

![Forstå trusler](../../../translated_images/no/understanding-threats.89edeada8a97fc0f.webp)

### Oppgave og instruksjon

**Beskrivelse:** Angripere prøver å endre instruksjonene eller målene til AI-agenten gjennom prompting eller manipulering av input.

**Reduksjon**: Utfør valideringskontroller og input-filtre for å oppdage potensielt farlige prompts før de behandles av AI-agenten. Siden disse angrepene vanligvis krever hyppig interaksjon med agenten, er det en annen måte å forhindre slike angrep på å begrense antall samtalerunder.

### Tilgang til kritiske systemer

**Beskrivelse**: Hvis en AI-agent har tilgang til systemer og tjenester som lagrer sensitiv data, kan angripere kompromittere kommunikasjonen mellom agenten og disse tjenestene. Disse kan være direkte angrep eller indirekte forsøk på å få informasjon om disse systemene gjennom agenten.

**Reduksjon**: AI-agenter bør ha tilgang til systemer kun når det er nødvendig for å forhindre slike angrep. Kommunikasjonen mellom agent og system bør også være sikker. Implementering av autentisering og tilgangskontroll er ytterligere metoder for å beskytte denne informasjonen.

### Overbelastning av ressurser og tjenester

**Beskrivelse:** AI-agenter kan få tilgang til ulike verktøy og tjenester for å fullføre oppgaver. Angripere kan utnytte dette ved å sende mange forespørsler gjennom AI-agenten, noe som kan føre til systemfeil eller høye kostnader.

**Reduksjon:** Implementer policyer som begrenser antallet forespørsler en AI-agent kan sende til en tjeneste. Å begrense antall samtalerunder og forespørsler til AI-agenten er en annen måte å forhindre slike angrep på.

### Forgifting av kunnskapsbasen

**Beskrivelse:** Denne typen angrep retter seg ikke direkte mot AI-agenten, men mot kunnskapsbasen og andre tjenester som AI-agenten bruker. Dette kan innebære korrumpering av data eller informasjon som AI-agenten bruker for å fullføre en oppgave, noe som fører til skjeve eller utilsiktede svar til brukeren.

**Reduksjon:** Utfør regelmessig verifisering av dataen AI-agenten bruker i arbeidsflytene sine. Sørg for at tilgangen til disse dataene er sikker og kun endres av betrodde personer for å unngå denne typen angrep.

### Kaskaderende feil

**Beskrivelse:** AI-agenter får tilgang til mange verktøy og tjenester for å fullføre oppgaver. Feil forårsaket av angripere kan føre til svikt i andre systemer som AI-agenten er koblet til, noe som gjør angrepet mer utbredt og vanskeligere å feilsøke.

**Reduksjon**: En metode for å unngå dette er å la AI-agenten operere i et begrenset miljø, for eksempel ved å utføre oppgaver i en Docker-kontainer, for å forhindre direkte systemangrep. Å lage fallback-mekanismer og retry-logikk når visse systemer svarer med feil, er en annen måte å forhindre større systemsvikt på.

## Menneske-i-løkken

En annen effektiv måte å bygge pålitelige AI-agent-systemer på er å bruke en menneske-i-løkken. Dette skaper et flyt hvor brukere kan gi tilbakemelding til agentene under kjøringen. Brukerne fungerer i praksis som agenter i et multi-agent system ved å godkjenne eller avbryte den pågående prosessen.

![Menneske i løkken](../../../translated_images/no/human-in-the-loop.5f0068a678f62f4f.webp)

Her er et kodeeksempel som bruker Microsoft Agent Framework for å vise hvordan dette konseptet er implementert:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Opprett leverandøren med menneskelig godkjenning
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Opprett agenten med et trinn for menneskelig godkjenning
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Brukeren kan gjennomgå og godkjenne svaret
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Konklusjon

Å bygge pålitelige AI-agenter krever nøye design, robuste sikkerhetstiltak og kontinuerlig iterasjon. Ved å implementere strukturerte meta-promptingssystemer, forstå potensielle trusler og bruke reduksjonsstrategier, kan utviklere lage AI-agenter som både er trygge og effektive. I tillegg sørger man ved å inkludere en menneske-i-løkken-tilnærming for at AI-agentene forblir i tråd med brukernes behov samtidig som risiko reduseres. Etter hvert som AI utvikler seg, vil en proaktiv holdning til sikkerhet, personvern og etiske hensyn være nøkkelen til å fremme tillit og pålitelighet i AI-drevne systemer.

## Kodeeksempler

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Steg-for-steg demonstrasjon av meta-prompt systemmeldingsrammeverk.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Godkjenningsporter før handling, risikoklassifisering og revisjonslogging for pålitelige agenter.

### Har du flere spørsmål om å bygge pålitelige AI-agenter?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre elever, delta i kontortid og få svar på dine spørsmål om AI-agenter.

## Ytterligere ressurser

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Oversikt over ansvarlig AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluering av generative AI-modeller og AI-applikasjoner</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Sikkerhetssystemmeldinger</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Mal for risikovurdering</a>

## Forrige leksjon

[Agentic RAG](../05-agentic-rag/README.md)

## Neste leksjon

[Planleggingsdesignmønster](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->