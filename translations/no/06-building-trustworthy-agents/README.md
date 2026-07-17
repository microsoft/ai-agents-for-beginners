[![Pålitelige AI-agenter](../../../translated_images/no/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klikk på bildet over for å se videoen av denne leksjonen)_

# Bygging av pålitelige AI-agenter

## Introduksjon

Denne leksjonen vil dekke:

- Hvordan bygge og distribuere sikre og effektive AI-agenter
- Viktige sikkerhetshensyn ved utvikling av AI-agenter.
- Hvordan opprettholde data- og brukerpersonvern ved utvikling av AI-agenter.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du vite hvordan du:

- Identifiserer og reduserer risikoer ved opprettelse av AI-agenter.
- Implementerer sikkerhetstiltak for å sikre at data og tilgang blir riktig administrert.
- Lager AI-agenter som opprettholder dataprivacy og gir en kvalitet brukeropplevelse.

## Sikkerhet

La oss først se på bygging av sikre agentiske applikasjoner. Sikkerhet betyr at AI-agenten fungerer som designet. Som byggere av agentiske applikasjoner har vi metoder og verktøy for å maksimere sikkerheten:

### Bygging av et rammeverk for systemmeldinger

Hvis du noen gang har bygget en AI-applikasjon ved hjelp av store språkmodeller (LLMs), vet du viktigheten av å designe en robust systemprompt eller systemmelding. Disse promptene etablerer metareglene, instruksjonene og retningslinjene for hvordan LLM vil samhandle med brukeren og data.

For AI-agenter er systemprompten enda viktigere ettersom AI-agentene vil trenge svært spesifikke instruksjoner for å utføre oppgavene vi har designet for dem.

For å lage skalerbare systemprompter kan vi bruke et rammeverk for systemmeldinger for å bygge en eller flere agenter i applikasjonen vår:

![Bygging av et rammeverk for systemmeldinger](../../../translated_images/no/system-message-framework.3a97368c92d11d68.webp)

#### Steg 1: Lag en meta systemmelding

Metaprompten vil bli brukt av en LLM for å generere systemprompter for agentene vi oppretter. Vi designer den som en mal slik at vi effektivt kan lage flere agenter om nødvendig.

Her er et eksempel på en meta systemmelding vi ville gitt til LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Steg 2: Lag en grunnleggende prompt

Neste steg er å lage en grunnleggende prompt for å beskrive AI-agenten. Du bør inkludere agentens rolle, oppgavene agenten skal utføre, og eventuelle andre ansvarsområder agenten har.

Her er et eksempel:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Steg 3: Gi grunnleggende systemmelding til LLM

Nå kan vi optimalisere denne systemmeldingen ved å gi meta systemmeldingen som systemmelding sammen med vår grunnleggende systemmelding.

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

#### Steg 4: Iterer og forbedre

Verdien av dette systemmeldingsrammeverket er å kunne skalere opp opprettelsen av systemmeldinger fra flere agenter enklere, i tillegg til å forbedre systemmeldingene over tid. Det er sjelden du får en systemmelding som fungerer perfekt første gang for ditt komplette bruksområde. Å kunne gjøre små justeringer og forbedringer ved å endre den grunnleggende systemmeldingen og kjøre den gjennom systemet vil tillate deg å sammenligne og evaluere resultater.

## Forståelse av trusler

For å bygge pålitelige AI-agenter er det viktig å forstå og redusere risikoer og trusler mot AI-agenten din. La oss se på noen av de ulike truslene mot AI-agenter og hvordan du bedre kan planlegge og forberede deg på dem.

![Forståelse av trusler](../../../translated_images/no/understanding-threats.89edeada8a97fc0f.webp)

### Oppgave og instruksjon

**Beskrivelse:** Angripere prøver å endre instruksjonene eller målene for AI-agenten gjennom prompting eller manipulering av innganger.

**Reduksjon:** Utfør valideringssjekker og input-filtre for å oppdage potensielt farlige prompt før de behandles av AI-agenten. Siden disse angrepene typisk krever hyppig interaksjon med agenten, er det også en måte å forhindre denne typen angrep på å begrense antallet runder i en samtale.

### Tilgang til kritiske systemer

**Beskrivelse:** Hvis en AI-agent har tilgang til systemer og tjenester som lagrer sensitiv data, kan angripere kompromittere kommunikasjonen mellom agenten og disse tjenestene. Dette kan være direkte angrep eller indirekte forsøk på å få informasjon om disse systemene gjennom agenten.

**Reduksjon:** AI-agenter bør ha tilgang til systemer kun etter behov for å forhindre denne typen angrep. Kommunikasjon mellom agenten og systemet bør også være sikker. Implementering av autentisering og tilgangskontroll er en annen måte å beskytte denne informasjonen på.

### Ressurs- og tjeneste-overbelastning

**Beskrivelse:** AI-agenter kan få tilgang til ulike verktøy og tjenester for å fullføre oppgaver. Angripere kan utnytte denne evnen til å angripe disse tjenestene ved å sende et høyt volum av forespørsler gjennom AI-agenten, noe som kan resultere i systemfeil eller høye kostnader.

**Reduksjon:** Implementer retningslinjer for å begrense antallet forespørsler en AI-agent kan sende til en tjeneste. Å begrense antallet samtalerunder og forespørsler til AI-agenten er en annen måte å forhindre denne typen angrep på.

### Forurensning av kunnskapsbase

**Beskrivelse:** Denne typen angrep retter seg ikke direkte mot AI-agenten, men mot kunnskapsbasen og andre tjenester som AI-agenten vil bruke. Dette kan innebære å korrumpert data eller informasjon som AI-agenten bruker til å fullføre en oppgave, noe som fører til skjev eller utilsiktet respons til brukeren.

**Reduksjon:** Gjennomfør regelmessig verifisering av dataene som AI-agenten vil bruke i arbeidsflytene sine. Sørg for at tilgang til disse dataene er sikker og kun kan endres av pålitelige personer for å unngå denne typen angrep.

### Kaskaderende feil

**Beskrivelse:** AI-agenter bruker ulike verktøy og tjenester for å fullføre oppgaver. Feil forårsaket av angripere kan føre til svikt i andre systemer som AI-agenten er koblet til, noe som gjør angrepet mer utbredt og vanskeligere å feilsøke.

**Reduksjon:** En metode for å unngå dette er å la AI-agenten operere i et begrenset miljø, som å utføre oppgaver i en Docker-container, for å forhindre direkte systemangrep. Å lage reserveordninger og forsøk-logikk når visse systemer svarer med feil, er en annen måte å forhindre større systemfeil på.

## Menneske i løkken

En annen effektiv måte å bygge pålitelige AI-agent-systemer på er å bruke en Menneske-i-løkken-tilnærming. Dette skaper en flyt der brukere kan gi tilbakemeldinger til agentene under kjøringen. Brukere fungerer i praksis som agenter i et multi-agent-system ved å gi godkjenning eller avbrudd av den pågående prosessen.

![Menneske i løkken](../../../translated_images/no/human-in-the-loop.5f0068a678f62f4f.webp)

Her er et kodeeksempel som bruker Microsoft Agent Framework for å vise hvordan dette konseptet er implementert:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Opprett leverandøren med menneskelig-godkjenning
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

Å bygge pålitelige AI-agenter krever nøye design, robuste sikkerhetstiltak og kontinuerlig iterasjon. Ved å implementere strukturerte meta-prompt-systemer, forstå potensielle trusler og bruke reduserende strategier, kan utviklere lage AI-agenter som både er sikre og effektive. I tillegg sikrer innlemmelse av en menneske-i-løkken-tilnærming at AI-agentene forblir tilpasset brukerbehov samtidig som risikoene minimeres. Ettersom AI fortsatt utvikler seg, vil det være nøkkelen til å opprettholde en proaktiv tilnærming til sikkerhet, personvern og etiske hensyn for å fremme tillit og pålitelighet i AI-drevne systemer.

## Kodeeksempler

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Trinnvis demonstrasjon av meta-prompt systemmeldingsrammeverket.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Godkjenningsporter før handling, risikoklassifisering og revisjonslogging for pålitelige agenter.

### Har du flere spørsmål om bygging av pålitelige AI-agenter?

Bli med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på kontortimer og få svar på dine spørsmål om AI-agenter.

## Ekstra ressurser

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Oversikt over ansvarlig AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluering av generative AI-modeller og AI-applikasjoner</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Sikkerhetssystemmeldinger</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Mal for risikovurdering</a>

## Forrige leksjon

[Agentisk RAG](../05-agentic-rag/README.md)

## Neste leksjon

[Planleggingsdesignmønster](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->