[![Pålitelige AI-agenter](../../../translated_images/no/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klikk på bildet over for å se video av denne leksjonen)_

# Bygge pålitelige AI-agenter

## Introduksjon

Denne leksjonen vil dekke:

- Hvordan bygge og distribuere trygge og effektive AI-agenter
- Viktige sikkerhetshensyn når man utvikler AI-agenter.
- Hvordan opprettholde data- og brukerpersonvern når man utvikler AI-agenter.

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite hvordan du:

- Identifiserer og reduserer risikoer ved opprettelse av AI-agenter.
- Implementerer sikkerhetstiltak for å sikre at data og tilgang håndteres korrekt.
- Lager AI-agenter som ivaretar dataprivacy og gir en kvalitetsrik brukeropplevelse.

## Sikkerhet

La oss først se på å bygge trygge agentdrevne applikasjoner. Sikkerhet betyr at AI-agenten oppfører seg som designet. Som byggere av agentdrevne applikasjoner har vi metoder og verktøy for å maksimere sikkerheten:

### Bygge et systemmeldingsrammeverk

Hvis du noen gang har bygget en AI-applikasjon ved hjelp av store språkmodeller (LLMs), vet du hvor viktig det er å designe en robust systemprompt eller systemmelding. Disse promptene fastsetter metareglene, instruksjonene og retningslinjene for hvordan LLM skal samhandle med bruker og data.

For AI-agenter er systemprompten enda viktigere, da AI-agentene vil trenge svært spesifikke instruksjoner for å fullføre oppgavene vi har designet for dem.

For å lage skalerbare systemprompter kan vi bruke et systemmeldingsrammeverk for å bygge en eller flere agenter i applikasjonen vår:

![Bygge et systemmeldingsrammeverk](../../../translated_images/no/system-message-framework.3a97368c92d11d68.webp)

#### Steg 1: Lag en meta systemmelding 

Metaprompten vil bli brukt av en LLM for å generere systempromptene for agentene vi lager. Vi designer den som en mal slik at vi effektivt kan lage flere agenter ved behov.

Her er et eksempel på en meta systemmelding vi vil gi til LLM:

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

Nå kan vi optimalisere denne systemmeldingen ved å gi metasytemmeldingen som systemmelding sammen med vår grunnleggende systemmelding.

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

Verdien av dette systemmeldingsrammeverket er at det gjør det lettere å skalere opprettelsen av systemmeldinger for flere agenter, samt å forbedre systemmeldingene over tid. Det er sjeldent at man har en systemmelding som fungerer perfekt første gang for hele brukstilfellet. Å kunne gjøre små justeringer og forbedringer ved å endre den grunnleggende systemmeldingen og kjøre den gjennom systemet vil tillate deg å sammenligne og evaluere resultater.

## Forstå trusler

For å bygge pålitelige AI-agenter er det viktig å forstå og redusere risikoer og trusler mot AI-agenten din. La oss se på noen av de ulike truslene mot AI-agenter og hvordan du kan planlegge og forberede deg bedre for dem.

![Forstå trusler](../../../translated_images/no/understanding-threats.89edeada8a97fc0f.webp)

### Oppgaver og instruksjon

**Beskrivelse:** Angripere forsøker å endre instruksjonene eller målene til AI-agenten gjennom prompting eller manipulering av innganger.

**Reduksjon:** Utfør valideringskontroller og input-filtre for å oppdage potensielt farlige prompts før de behandles av AI-agenten. Siden disse angrepene vanligvis krever hyppig interaksjon med agenten, er det en annen måte å forhindre denne typen angrep på å begrense antall runder i en samtale.

### Tilgang til kritiske systemer

**Beskrivelse:** Hvis en AI-agent har tilgang til systemer og tjenester som lagrer sensitiv data, kan angripere kompromittere kommunikasjonen mellom agenten og disse tjenestene. Disse kan være direkte angrep eller indirekte forsøk på å hente informasjon om disse systemene gjennom agenten.

**Reduksjon:** AI-agenter bør ha tilgang til systemer kun ved behov for å forhindre denne typen angrep. Kommunikasjonen mellom agenten og systemet bør også være sikker. Implementering av autentisering og tilgangskontroll er en annen måte å beskytte denne informasjonen på.

### Overbelastning av ressurser og tjenester

**Beskrivelse:** AI-agenter kan få tilgang til ulike verktøy og tjenester for å utføre oppgaver. Angripere kan bruke denne evnen til å angripe disse tjenestene ved å sende et høyt volum av forespørsler gjennom AI-agenten, noe som kan føre til systemfeil eller høye kostnader.

**Reduksjon:** Implementer policyer for å begrense antall forespørsler en AI-agent kan sende til en tjeneste. Å begrense antall samtalerunder og forespørsler til AI-agenten er en annen måte å forhindre denne typen angrep på.

### Forgifting av kunnskapsbase

**Beskrivelse:** Denne typen angrep er ikke rettet direkte mot AI-agenten, men mot kunnskapsbasen og andre tjenester som AI-agenten vil bruke. Dette kan innebære korrumpering av data eller informasjon som AI-agenten bruker for å fullføre oppgaver, noe som fører til partiske eller utilsiktede svar til brukeren.

**Reduksjon:** Utfør regelmessig verifikasjon av dataene som AI-agenten bruker i arbeidsflyten sin. Sørg for at tilgangen til disse dataene er sikker og kun kan endres av betrodde personer for å unngå denne typen angrep.

### Kaskaderende feil

**Beskrivelse:** AI-agenter får tilgang til ulike verktøy og tjenester for å utføre oppgaver. Feil forårsaket av angripere kan føre til feil i andre systemer som AI-agenten er koblet til, slik at angrepet blir mer omfattende og vanskeligere å feilsøke.

**Reduksjon:** En metode for å unngå dette er å la AI-agenten operere i et begrenset miljø, som å utføre oppgaver i en Docker-container, for å forhindre direkte systemangrep. Å lage fallback-mekanismer og retry-logikk når enkelte systemer svarer med feil er en annen måte å forhindre større systemfeil på.

## Mennesket i løkken

En annen effektiv måte å bygge pålitelige AI-agent systemer på er å bruke mennesket i løkken. Dette skaper en flyt hvor brukere kan gi tilbakemeldinger til agentene under kjøringen. Brukere fungerer i praksis som agenter i et multi-agent system ved å gi godkjenning eller terminering av den pågående prosessen.

![Mennesket i løkken](../../../translated_images/no/human-in-the-loop.5f0068a678f62f4f.webp)

Her er et kodeeksempel som bruker Microsoft Agent Framework for å vise hvordan dette konseptet er implementert:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Opprett leverandøren med menneskelig godkjenningsprosess
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
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

Å bygge pålitelige AI-agenter krever nøye design, robuste sikkerhetstiltak og kontinuerlig iterasjon. Ved å implementere strukturerte metasystemprompt-systemer, forstå potensielle trusler og anvende reduseringstiltak kan utviklere skape AI-agenter som både er trygge og effektive. I tillegg sikrer inkorporering av mennesket i løkken at AI-agentene forblir i samsvar med brukerbehov samtidig som risikoene minimeres. Ettersom AI fortsetter å utvikle seg, vil det være avgjørende å opprettholde et proaktivt fokus på sikkerhet, personvern og etiske hensyn for å fremme tillit og pålitelighet i AI-drevne systemer.

## Kodeeksempler

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Trinnvis demonstrasjon av metasystemprompt-rammeverket.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Godkjenningsporter før handling, risikoklassifisering og revisjonslogging for pålitelige agenter.

### Har du flere spørsmål om å bygge pålitelige AI-agenter?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på dine AI-agent spørsmål.

## Ekstra ressurser

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Ansvarlig AI oversikt</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluering av generative AI-modeller og AI-applikasjoner</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Sikkerhetssystemmeldinger</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Risikovurderingsmal</a>

## Forrige leksjon

[Agentic RAG](../05-agentic-rag/README.md)

## Neste leksjon

[Planleggingsdesignmønster](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->