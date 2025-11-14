<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T15:50:59+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "no"
}
-->
[![Pålitelige AI-agenter](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.no.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klikk på bildet over for å se videoen til denne leksjonen)_

# Bygge pålitelige AI-agenter

## Introduksjon

Denne leksjonen vil dekke:

- Hvordan bygge og distribuere trygge og effektive AI-agenter.
- Viktige sikkerhetshensyn ved utvikling av AI-agenter.
- Hvordan opprettholde databeskyttelse og brukernes personvern under utvikling av AI-agenter.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du vite hvordan du:

- Identifiserer og reduserer risikoer ved opprettelse av AI-agenter.
- Implementerer sikkerhetstiltak for å sikre at data og tilgang håndteres riktig.
- Lager AI-agenter som ivaretar databeskyttelse og gir en god brukeropplevelse.

## Sikkerhet

La oss først se på hvordan man bygger trygge agentapplikasjoner. Sikkerhet betyr at AI-agenten fungerer som tiltenkt. Som utviklere av agentapplikasjoner har vi metoder og verktøy for å maksimere sikkerheten:

### Bygge et rammeverk for systemmeldinger

Hvis du noen gang har bygget en AI-applikasjon ved hjelp av store språkmodeller (LLMs), vet du hvor viktig det er å designe en robust systemprompt eller systemmelding. Disse meldingene etablerer meta-regler, instruksjoner og retningslinjer for hvordan LLM-en skal samhandle med brukeren og dataene.

For AI-agenter er systemprompten enda viktigere, ettersom AI-agentene trenger svært spesifikke instruksjoner for å fullføre oppgavene vi har designet for dem.

For å lage skalerbare systemprompter kan vi bruke et rammeverk for systemmeldinger for å bygge én eller flere agenter i applikasjonen vår:

![Bygge et rammeverk for systemmeldinger](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.no.png)

#### Trinn 1: Lag en meta-systemmelding

Meta-prompten brukes av en LLM for å generere systemprompter for agentene vi lager. Vi designer den som en mal slik at vi effektivt kan lage flere agenter om nødvendig.

Her er et eksempel på en meta-systemmelding vi kan gi til LLM-en:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Trinn 2: Lag en grunnleggende prompt

Neste trinn er å lage en grunnleggende prompt som beskriver AI-agenten. Du bør inkludere agentens rolle, oppgavene agenten skal utføre, og eventuelle andre ansvarsområder.

Her er et eksempel:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Trinn 3: Gi grunnleggende systemmelding til LLM

Nå kan vi optimalisere denne systemmeldingen ved å gi meta-systemmeldingen som systemmelding og vår grunnleggende systemmelding.

Dette vil produsere en systemmelding som er bedre designet for å veilede AI-agentene våre:

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

#### Trinn 4: Iterer og forbedre

Verdien av dette rammeverket for systemmeldinger er at det gjør det enklere å skalere opprettelsen av systemmeldinger for flere agenter, samt forbedre systemmeldingene over tid. Det er sjelden at en systemmelding fungerer perfekt første gang for hele bruksområdet ditt. Ved å gjøre små justeringer og forbedringer i den grunnleggende systemmeldingen og kjøre den gjennom systemet, kan du sammenligne og evaluere resultatene.

## Forstå trusler

For å bygge pålitelige AI-agenter er det viktig å forstå og redusere risikoene og truslene mot AI-agenten din. La oss se på noen av de ulike truslene mot AI-agenter og hvordan du bedre kan planlegge og forberede deg på dem.

![Forstå trusler](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.no.png)

### Oppgaver og instruksjoner

**Beskrivelse:** Angripere forsøker å endre instruksjonene eller målene til AI-agenten gjennom prompter eller manipulering av inndata.

**Tiltak:** Utfør valideringskontroller og inndatafiltre for å oppdage potensielt farlige prompter før de behandles av AI-agenten. Siden disse angrepene vanligvis krever hyppig interaksjon med agenten, kan det også være effektivt å begrense antall samtaleomganger.

### Tilgang til kritiske systemer

**Beskrivelse:** Hvis en AI-agent har tilgang til systemer og tjenester som lagrer sensitiv data, kan angripere kompromittere kommunikasjonen mellom agenten og disse tjenestene. Dette kan være direkte angrep eller indirekte forsøk på å få informasjon om disse systemene via agenten.

**Tiltak:** AI-agenter bør kun ha tilgang til systemer når det er nødvendig for å forhindre slike angrep. Kommunikasjonen mellom agenten og systemet bør også være sikker. Implementering av autentisering og tilgangskontroll er en annen måte å beskytte denne informasjonen på.

### Overbelastning av ressurser og tjenester

**Beskrivelse:** AI-agenter kan bruke ulike verktøy og tjenester for å utføre oppgaver. Angripere kan utnytte denne evnen til å angripe tjenestene ved å sende et høyt volum av forespørsler gjennom AI-agenten, noe som kan føre til systemfeil eller høye kostnader.

**Tiltak:** Implementer retningslinjer for å begrense antall forespørsler en AI-agent kan sende til en tjeneste. Å begrense antall samtaleomganger og forespørsler til AI-agenten er en annen måte å forhindre slike angrep på.

### Forgiftning av kunnskapsbasen

**Beskrivelse:** Denne typen angrep retter seg ikke direkte mot AI-agenten, men mot kunnskapsbasen og andre tjenester som AI-agenten bruker. Dette kan innebære å korrumpere dataene eller informasjonen som AI-agenten bruker for å utføre en oppgave, noe som fører til skjeve eller utilsiktede svar til brukeren.

**Tiltak:** Utfør regelmessig verifisering av dataene som AI-agenten bruker i sine arbeidsflyter. Sørg for at tilgangen til disse dataene er sikker og kun kan endres av betrodde personer for å unngå denne typen angrep.

### Kaskaderende feil

**Beskrivelse:** AI-agenter bruker ulike verktøy og tjenester for å utføre oppgaver. Feil forårsaket av angripere kan føre til feil i andre systemer som AI-agenten er koblet til, noe som gjør angrepet mer omfattende og vanskeligere å feilsøke.

**Tiltak:** En metode for å unngå dette er å la AI-agenten operere i et begrenset miljø, som å utføre oppgaver i en Docker-container, for å forhindre direkte systemangrep. Å lage fallback-mekanismer og retry-logikk når visse systemer svarer med en feil, er en annen måte å forhindre større systemfeil på.

## Menneske i loopen

En annen effektiv måte å bygge pålitelige AI-agentsystemer på er å bruke et menneske i loopen. Dette skaper en flyt der brukere kan gi tilbakemelding til agentene under kjøringen. Brukere fungerer i praksis som agenter i et multi-agent-system ved å gi godkjenning eller avslutte prosessen som kjører.

![Menneske i loopen](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.no.png)

Her er et kodeeksempel som bruker AutoGen for å vise hvordan dette konseptet implementeres:

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

## Konklusjon

Å bygge pålitelige AI-agenter krever nøye design, robuste sikkerhetstiltak og kontinuerlig iterasjon. Ved å implementere strukturerte meta-prompt-systemer, forstå potensielle trusler og anvende tiltak for å redusere risiko, kan utviklere lage AI-agenter som både er trygge og effektive. I tillegg sikrer bruk av et menneske i loopen at AI-agentene forblir tilpasset brukernes behov samtidig som risikoen minimeres. Etter hvert som AI utvikler seg, vil det være avgjørende å opprettholde en proaktiv tilnærming til sikkerhet, personvern og etiske hensyn for å fremme tillit og pålitelighet i AI-drevne systemer.

### Har du flere spørsmål om å bygge pålitelige AI-agenter?

Bli med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på kontortid og få svar på spørsmålene dine om AI-agenter.

## Tilleggsressurser

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Oversikt over ansvarlig bruk av AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluering av generative AI-modeller og AI-applikasjoner</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Sikkerhetssystemmeldinger</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Risikovurderingsmal</a>

## Forrige leksjon

[Agentic RAG](../05-agentic-rag/README.md)

## Neste leksjon

[Planleggingsdesignmønster](../07-planning-design/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.