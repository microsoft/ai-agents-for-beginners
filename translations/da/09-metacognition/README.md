[![Multi-Agent Design](../../../translated_images/da/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_
# Metakognition i AI-agenter

## Introduktion

Velkommen til lektionen om metakognition i AI-agenter! Dette kapitel er designet til begyndere, der er nysgerrige efter, hvordan AI-agenter kan tænke over deres egne tankeprocesser. Ved slutningen af denne lektion vil du forstå nøglebegreber og være udstyret med praktiske eksempler til at anvende metakognition i design af AI-agenter.

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

1. Forstå konsekvenserne af ræsonnementssløjfer i agentdefinitioner.
2. Bruge planlægnings- og evalueringsmetoder til at hjælpe selvkorrigerende agenter.
3. Skabe dine egne agenter, der er i stand til at manipulere kode for at udføre opgaver.

## Introduktion til Metakognition

Metakognition henviser til de højere ordens kognitive processer, der involverer at tænke over ens egen tænkning. For AI-agenter betyder det at kunne evaluere og justere deres handlinger baseret på selvbevidsthed og tidligere erfaringer. Metakognition, eller "tænke over tænkning," er et vigtigt begreb i udviklingen af agentiske AI-systemer. Det involverer, at AI-systemer er bevidste om deres egne interne processer og er i stand til at overvåge, regulere og tilpasse deres adfærd i overensstemmelse hermed. Ligesom vi gør, når vi læser rummet eller kigger på et problem. Denne selvbevidsthed kan hjælpe AI-systemer med at træffe bedre beslutninger, identificere fejl og forbedre deres ydeevne over tid – igen forbundet med Turingtesten og debatten om, hvorvidt AI vil overtage.

I konteksten af agentiske AI-systemer kan metakognition hjælpe med at håndtere flere udfordringer, såsom:
- Gennemsigtighed: Sikre, at AI-systemer kan forklare deres ræsonnement og beslutninger.
- Ræsonnement: Forbedre evnen for AI-systemer til at syntetisere information og træffe velbegrundede beslutninger.
- Tilpasning: Tillade AI-systemer at justere sig til nye miljøer og skiftende betingelser.
- Perception: Forbedre nøjagtigheden af AI-systemers genkendelse og fortolkning af data fra deres omgivelser.

### Hvad er Metakognition?

Metakognition, eller "tænke over tænkning," er en højere ordens kognitiv proces, der involverer selvbevidsthed og selvregulering af ens egne kognitive processer. Inden for AI giver metakognition agenter mulighed for at evaluere og tilpasse deres strategier og handlinger, hvilket fører til forbedrede problemløsnings- og beslutningsevner. Ved at forstå metakognition kan du designe AI-agenter, der ikke blot er mere intelligente, men også mere tilpasningsdygtige og effektive. I ægte metakognition ville man se, at AI eksplicit ræsonnerer over sit eget ræsonnement.

Eksempel: "Jeg prioriterede billigere fly fordi… jeg kan måske gå glip af direkte fly, så lad mig tjekke igen."
Holde styr på hvordan eller hvorfor den valgte en bestemt rute.
- Bemærke, at den lavede fejl, fordi den overbetroede brugerpræferencer fra sidste gang, så den ændrer sin beslutningstagningsstrategi, ikke kun den endelige anbefaling.
- Diagnosticere mønstre som, "Når jeg ser brugeren nævne 'for overfyldt', bør jeg ikke kun fjerne visse attraktioner, men også reflektere over, at min metode til at vælge 'topattraktioner' er fejlagtig, hvis jeg altid rangerer efter popularitet."

### Betydningen af Metakognition i AI-agenter

Metakognition spiller en afgørende rolle i designet af AI-agenter af flere årsager:

![Betydningen af Metakognition](../../../translated_images/da/importance-of-metacognition.b381afe9aae352f7.webp)

- Selvrefleksion: Agenter kan vurdere deres egen ydeevne og identificere områder til forbedring.
- Tilpasningsevne: Agenter kan ændre deres strategier baseret på tidligere erfaringer og skiftende miljøer.
- Fejlretning: Agenter kan opdage og rette fejl autonomt, hvilket fører til mere præcise resultater.
- Ressourcestyring: Agenter kan optimere brugen af ressourcer såsom tid og computational kapacitet ved at planlægge og evaluere deres handlinger.

## Komponenter i en AI-agent

Før vi dykker ned i metakognitive processer, er det vigtigt at forstå de grundlæggende komponenter i en AI-agent. En AI-agent består typisk af:

- Persona: Agentens personlighed og karakteristika, som definerer, hvordan den interagerer med brugere.
- Værktøjer: De kapaciteter og funktioner, som agenten kan udføre.
- Færdigheder: Den viden og ekspertise, agenten besidder.

Disse komponenter arbejder sammen for at skabe en "ekspertiseenhed", der kan udføre specifikke opgaver.

**Eksempel**:
Overvej en rejseagent, agenttjenester der ikke kun planlægger din ferie, men også justerer sin kurs baseret på realtidsdata og tidligere kunderejseoplevelser.

### Eksempel: Metakognition i en rejseagenttjeneste

Forestil dig, at du designer en rejseagenttjeneste drevet af AI. Denne agent, "Rejseagenten," hjælper brugere med at planlægge deres ferier. For at inkorporere metakognition skal Rejseagenten evaluere og justere sine handlinger baseret på selvbevidsthed og tidligere erfaringer. Her er, hvordan metakognition kunne spille en rolle:

#### Nuværende opgave

Den aktuelle opgave er at hjælpe en bruger med at planlægge en rejse til Paris.

#### Trin til at fuldføre opgaven

1. **Indsamle brugerpræferencer**: Spørg brugeren om deres rejsedatoer, budget, interesser (f.eks. museer, mad, shopping) og eventuelle specifikke krav.
2. **Hente information**: Søg efter flymuligheder, overnatning, attraktioner og restauranter, der matcher brugerens præferencer.
3. **Generere anbefalinger**: Giv en personlig rejseplan med flyinformation, hotelreservationer og foreslåede aktiviteter.
4. **Justere baseret på feedback**: Spørg brugeren om feedback på anbefalingerne og foretag nødvendige justeringer.

#### Nødvendige ressourcer

- Adgang til fly- og hotelbooking-databaser.
- Information om parisiske attraktioner og restauranter.
- Brugerfeedbackdata fra tidligere interaktioner.

#### Erfaring og selvrefleksion

Rejseagenten bruger metakognition til at evaluere sin ydeevne og lære af tidligere erfaringer. For eksempel:

1. **Analysere brugerfeedback**: Rejseagenten gennemgår brugerfeedback for at afgøre, hvilke anbefalinger der blev godt modtaget, og hvilke der ikke blev. Den justerer sine fremtidige forslag derefter.
2. **Tilpasningsevne**: Hvis en bruger tidligere har nævnt en modvilje mod overfyldte steder, vil Rejseagenten undgå at anbefale populære turiststeder i myldretiden fremover.
3. **Fejlretning**: Hvis Rejseagenten lavede en fejl i en tidligere booking, såsom at foreslå et hotel, der var fuldt booket, lærer den at kontrollere tilgængeligheden mere grundigt, før den laver anbefalinger.

#### Praktisk udviklereksempel

Her er et forenklet eksempel på, hvordan Rejseagentens kode kunne se ud, når metakognition indarbejdes:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Søg efter fly, hoteller og attraktioner baseret på præferencer
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyser feedback og juster fremtidige anbefalinger
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Eksempel på brug
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Hvorfor Metakognition Har Betydning

- **Selvrefleksion**: Agenter kan analysere deres præstation og identificere områder for forbedring.
- **Tilpasningsevne**: Agenter kan ændre strategier baseret på feedback og skiftende forhold.
- **Fejlretning**: Agenter kan opdage og rette fejl autonomt.
- **Ressourcestyring**: Agenter kan optimere ressourceforbruget, såsom tid og beregningskraft.

Ved at inddrage metakognition kan Rejseagenten levere mere personlige og præcise rejseanbefalinger, hvilket forbedrer den samlede brugeroplevelse.

---

## 2. Planlægning i agenter


Planlægning er en kritisk komponent i AI-agentadfærd. Det involverer at skitsere de nødvendige trin for at opnå et mål, med hensyntagen til den nuværende tilstand, ressourcer og mulige forhindringer.

### Elementer af Planlægning

- **Nuværende Opgave**: Definer opgaven klart.
- **Trin for at Fuldføre Opgaven**: Opdel opgaven i håndterbare trin.
- **Nødvendige Ressourcer**: Identificer nødvendige ressourcer.
- **Erfaring**: Brug tidligere erfaringer til at informere planlægningen.

**Eksempel**:
Her er de trin, Rejseagenten skal tage for effektivt at hjælpe en bruger med at planlægge deres rejse:

### Trin for Rejseagent

1. **Indsaml Brugernes Præferencer**
   - Spørg brugeren om detaljer om deres rejsedatoer, budget, interesser og eventuelle specifikke krav.
   - Eksempler: "Hvornår planlægger du at rejse?" "Hvad er dit budget?" "Hvilke aktiviteter nyder du på ferien?"

2. **Hent Information**
   - Søg efter relevante rejsemuligheder baseret på brugerens præferencer.
   - **Fly**: Kig efter tilgængelige fly inden for brugerens budget og foretrukne rejsedatoer.
   - **Indkvartering**: Find hoteller eller lejeboliger, der matcher brugerens præferencer for placering, pris og faciliteter.
   - **Attraktioner og Restauranter**: Identificer populære attraktioner, aktiviteter og spisesteder, der passer til brugerens interesser.

3. **Generer Anbefalinger**
   - Sammensæt den hentede information til en personlig rejseplan.
   - Giv detaljer som flymuligheder, hotelreservationer og foreslåede aktiviteter og skræddersy anbefalingerne til brugerens præferencer.

4. **Præsenter Rejseplanen til Brugeren**
   - Del det foreslåede rejseprogram med brugeren til deres gennemgang.
   - Eksempel: "Her er et foreslået rejseprogram til din tur til Paris. Det inkluderer flydetaljer, hotelreservationer og en liste over anbefalede aktiviteter og restauranter. Lad mig høre, hvad du synes!"

5. **Indsaml Feedback**
   - Spørg brugeren om feedback på den foreslåede rejseplan.
   - Eksempler: "Kan du lide flymulighederne?" "Er hotellet egnet til dine behov?" "Er der nogle aktiviteter, du gerne vil tilføje eller fjerne?"

6. **Tilpas Basere på Feedback**
   - Ændr rejseplanen baseret på brugerens feedback.
   - Foretag nødvendige ændringer i fly-, indkvarterings- og aktivitetsanbefalingerne for bedre at matche brugerens præferencer.

7. **Endelig Bekræftelse**
   - Præsenter den opdaterede rejseplan for brugeren til endelig bekræftelse.
   - Eksempel: "Jeg har lavet ændringerne baseret på din feedback. Her er den opdaterede rejseplan. Ser alt godt ud for dig?"

8. **Book og Bekræft Reservationer**
   - Når brugeren godkender rejseplanen, fortsæt med at booke fly, overnatning og eventuelle forudplanlagte aktiviteter.
   - Send bekræftelsesdetaljer til brugeren.

9. **Giv Løbende Support**
   - Vær tilgængelig for at assistere brugeren med ændringer eller yderligere anmodninger før og under deres rejse.
   - Eksempel: "Hvis du behøver yderligere hjælp under din rejse, er du velkommen til at kontakte mig når som helst!"

### Eksempel på Interaktion

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Eksempel på brug inden for en bookinganmodning
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. Korrigerende RAG System

Først lad os starte med at forstå forskellen mellem RAG-værktøjet og Forudgående Kontekstindlæsning

![RAG vs Context Loading](../../../translated_images/da/rag-vs-context.9eae588520c00921.webp)

### Retrieval-Augmented Generation (RAG)

RAG kombinerer et hentningssystem med en generativ model. Når der stilles en forespørgsel, henter hentningssystemet relevante dokumenter eller data fra en ekstern kilde, og denne hentede information bruges til at forbedre inputtet til den generative model. Dette hjælper modellen til at generere mere præcise og kontekstuelt relevante svar.

I et RAG-system henter agenten relevant information fra en vidensbase og bruger det til at generere passende svar eller handlinger.

### Korrigerende RAG Tilgang

Den korrigerende RAG-tilgang fokuserer på at bruge RAG-teknikker til at rette fejl og forbedre nøjagtigheden af AI-agenter. Dette involverer:

1. **Prompting Teknik**: Brug af specifikke prompts til at guide agenten i at hente relevant information.
2. **Værktøj**: Implementering af algoritmer og mekanismer, der gør det muligt for agenten at vurdere relevansen af den hentede information og generere nøjagtige svar.
3. **Evaluering**: Kontinuerlig vurdering af agentens præstation og foretage justeringer for at forbedre dens nøjagtighed og effektivitet.

#### Eksempel: Korrigerende RAG i en Søgeagent

Overvej en søgeagent, der henter information fra internettet for at besvare brugerforespørgsler. Den korrigerende RAG-tilgang kan involvere:

1. **Prompting Teknik**: Formulere søgeforespørgsler baseret på brugerens input.
2. **Værktøj**: Brug af naturlig sprogbehandling og maskinlæringsalgoritmer til at rangere og filtrere søgeresultater.
3. **Evaluering**: Analysere brugerfeedback for at identificere og rette unøjagtigheder i den hentede information.

### Korrigerende RAG i Rejseagent

Korrigerende RAG (Retrieval-Augmented Generation) forbedrer en AIs evne til at hente og generere information samtidig med at rette eventuelle unøjagtigheder. Lad os se, hvordan Rejseagenten kan bruge den korrigerende RAG-tilgang til at give mere præcise og relevante rejseanbefalinger.

Dette involverer:

- **Prompting Teknik:** Brug af specifikke prompts til at guide agenten i at hente relevant information.
- **Værktøj:** Implementering af algoritmer og mekanismer, der gør det muligt for agenten at evaluere relevansen af den hentede information og generere nøjagtige svar.
- **Evaluering:** Kontinuerlig vurdering af agentens præstation og foretage justeringer for at forbedre dens nøjagtighed og effektivitet.

#### Trin til Implementering af Korrigerende RAG i Rejseagent

1. **Indledende Brugerinteraktion**
   - Rejseagenten indsamler indledende præferencer fra brugeren, såsom destination, rejsedatoer, budget og interesser.
   - Eksempel:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Hentning af Information**
   - Rejseagenten henter information om fly, overnatning, attraktioner og restauranter baseret på brugerens præferencer.
   - Eksempel:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generering af Indledende Anbefalinger**
   - Rejseagenten bruger den hentede information til at generere en personlig rejseplan.
   - Eksempel:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Indsamling af Brugerfeedback**
   - Rejseagenten spørger brugeren om feedback på de indledende anbefalinger.
   - Eksempel:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Korrigerende RAG Proces**
   - **Prompting Teknik**: Rejseagenten formulerer nye søgeforespørgsler baseret på brugerfeedback.
     - Eksempel:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Værktøj**: Rejseagenten bruger algoritmer til at rangere og filtrere nye søgeresultater med fokus på relevansen baseret på brugerfeedback.
     - Eksempel:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Evaluering**: Rejseagenten vurderer løbende relevansen og nøjagtigheden af sine anbefalinger ved at analysere brugerfeedback og foretage nødvendige justeringer.
     - Eksempel:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Praktisk Eksempel

Her er et forenklet Python-kodeeksempel, der inkorporerer den korrigerende RAG-tilgang i Rejseagenten:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# Eksempel på brug
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### Forudgående Kontekstindlæsning


Forudindlæst kontekst involverer indlæsning af relevant kontekst eller baggrundsinformation i modellen, før der behandles en forespørgsel. Det betyder, at modellen har adgang til denne information fra starten, hvilket kan hjælpe den med at generere mere informerede svar uden at skulle hente yderligere data under processen.

Her er et forenklet eksempel på, hvordan en forudindlæst kontekst kunne se ud for en rejseagentapplikation i Python:

```python
class TravelAgent:
    def __init__(self):
        # Forindlæs populære destinationer og deres information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Hent destinationsinformation fra forindlæst kontekst
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Eksempel på brug
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Forklaring

1. **Initialisering (`__init__` metode)**: `TravelAgent` klassen forindlæser en ordbog, der indeholder information om populære destinationer som Paris, Tokyo, New York og Sydney. Denne ordbog indeholder detaljer som land, valuta, sprog og større attraktioner for hver destination.

2. **Hentning af Information (`get_destination_info` metode)**: Når en bruger spørger om en bestemt destination, henter metoden `get_destination_info` den relevante information fra den forudindlæste kontekstordbog.

Ved at forindlæse konteksten kan rejseagentapplikationen hurtigt svare på brugerforespørgsler uden at skulle hente denne information fra en ekstern kilde i realtid. Dette gør applikationen mere effektiv og responsiv.

### Opstart af Plan med et Mål før Iteration

At opstarte en plan med et mål involverer at starte med et klart mål eller ønsket resultat i tankerne. Ved at definere dette mål på forhånd kan modellen bruge det som en ledetråd gennem hele den iterative proces. Dette sikrer, at hver iteration bevæger sig tættere på at opnå det ønskede resultat, hvilket gør processen mere effektiv og fokuseret.

Her er et eksempel på, hvordan du kan opstarte en rejseplan med et mål før iteration for en rejseagent i Python:

### Scenario

En rejseagent ønsker at planlægge en skræddersyet ferie for en klient. Målet er at skabe en rejseplan, der maksimerer klientens tilfredshed baseret på deres præferencer og budget.

### Trin

1. Definer klientens præferencer og budget.
2. Opstart af den indledende plan baseret på disse præferencer.
3. Iterer for at forfine planen og optimere klientens tilfredshed.

#### Python-kode

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Eksempel på brug
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### Kodeforklaring

1. **Initialisering (`__init__` metode)**: `TravelAgent` klassen initialiseres med en liste af potentielle destinationer, som hver har attributter som navn, pris og aktivitetstype.

2. **Opstart af Planen (`bootstrap_plan` metode)**: Denne metode skaber en indledende rejseplan baseret på klientens præferencer og budget. Den gennemgår listen af destinationer og tilføjer dem til planen, hvis de matcher klientens præferencer og passer inden for budgettet.

3. **Matchende Præferencer (`match_preferences` metode)**: Denne metode tjekker, om en destination matcher klientens præferencer.

4. **Iteration af Planen (`iterate_plan` metode)**: Denne metode forfiner den indledende plan ved at forsøge at erstatte hver destination i planen med et bedre match, under hensyntagen til klientens præferencer og budgetbegrænsninger.

5. **Beregning af Pris (`calculate_cost` metode)**: Denne metode beregner den samlede pris for den aktuelle plan, inklusive en potentiel ny destination.

#### Eksempel på anvendelse

- **Indledende Plan**: Rejseagenten skaber en indledende plan baseret på klientens præferencer for sightseeing og et budget på $2000.
- **Forfinet Plan**: Rejseagenten itererer planen for at optimere klientens præferencer og budget.

Ved at opstarte planen med et klart mål (f.eks. at maksimere kundetilfredshed) og iterere for at forfine planen kan rejseagenten skabe en skræddersyet og optimeret rejseplan for klienten. Denne tilgang sikrer, at rejseplanen stemmer overens med klientens præferencer og budget fra starten og forbedres med hver iteration.

### Udnyttelse af LLM til Re-rangering og Scoring

Store sproglige modeller (LLM'er) kan bruges til re-rangering og scoring ved at evaluere relevansen og kvaliteten af indhentede dokumenter eller genererede svar. Sådan fungerer det:

**Hentning:** Det indledende trin henter et sæt kandidatdokumenter eller svar baseret på forespørgslen.

**Re-rangering:** LLM'en evaluerer disse kandidater og re-rangerer dem baseret på deres relevans og kvalitet. Dette sikrer, at den mest relevante og højkvalitetsinformation præsenteres først.

**Scoring:** LLM'en tildeler scores til hver kandidat, der afspejler deres relevans og kvalitet. Dette hjælper med at vælge det bedste svar eller dokument til brugeren.

Ved at udnytte LLM'er til re-rangering og scoring kan systemet give mere præcis og kontekstuel relevant information, hvilket forbedrer den samlede brugeroplevelse.

Her er et eksempel på, hvordan en rejseagent kan bruge en stor sproglig model (LLM) til at re-rangere og score rejsemål baseret på brugerpræferencer i Python:

#### Scenario - Rejse baseret på præferencer

En rejseagent ønsker at anbefale de bedste rejsemål til en kunde baseret på dennes præferencer. LLM'en hjælper med at re-rangere og score destinationerne for at sikre, at de mest relevante muligheder præsenteres.

#### Trin:

1. Indsamle brugerpræferencer.
2. Hent en liste over potentielle rejsemål.
3. Brug LLM'en til at re-rangere og score destinationerne baseret på brugerpræferencer.

Sådan kan du opdatere det tidligere eksempel til at bruge Azure OpenAI Services:

#### Krav

1. Du skal have et Azure-abonnement.
2. Opret en Azure OpenAI-ressource og få din API-nøgle.

#### Eksempel på Python-kode

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generer en prompt til Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Definer overskrifter og payload til forespørgslen
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Kald Azure OpenAI API'en for at få de omplacerede og scorerede destinationer
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Udtræk og returner anbefalingerne
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Eksempel på brug
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### Kodeforklaring - Præferencebooker

1. **Initialisering**: `TravelAgent` klassen initialiseres med en liste af potentielle rejsemål, hver med attributter som navn og beskrivelse.

2. **Hentning af anbefalinger (`get_recommendations` metode)**: Denne metode genererer en prompt til Azure OpenAI-tjenesten baseret på brugerens præferencer og foretager et HTTP POST-kald til Azure OpenAI API'et for at få re-rangerede og scorable destinationer.

3. **Generering af prompt (`generate_prompt` metode)**: Denne metode konstruerer en prompt til Azure OpenAI, inklusiv brugerens præferencer og listen over destinationer. Prompten guider modellen til at re-rangere og score destinationerne baseret på de angivne præferencer.

4. **API-kald**: `requests`-biblioteket bruges til at foretage et HTTP POST-kald til Azure OpenAI API-endpointet. Svaret indeholder de re-rangerede og scorende destinationer.

5. **Eksempel på anvendelse**: Rejseagenten indsamler brugerens præferencer (f.eks. interesse for sightseeing og mangfoldig kultur) og bruger Azure OpenAI-tjenesten til at få re-rangerede og scorerede anbefalinger for rejsemål.

Husk at udskifte `your_azure_openai_api_key` med din faktiske Azure OpenAI API-nøgle og `https://your-endpoint.com/...` med det faktiske endpoint-URL for din Azure OpenAI-udrulning.

Ved at udnytte LLM'en til re-rangering og scoring kan rejseagenten give mere personlige og relevante rejseanbefalinger til kunderne og forbedre deres samlede oplevelse.

### RAG: Promptteknik vs Værktøj

Retrieval-Augmented Generation (RAG) kan både være en promptteknik og et værktøj i udviklingen af AI-agenter. At forstå forskellen mellem de to kan hjælpe dig med at udnytte RAG mere effektivt i dine projekter.

#### RAG som en Promptteknik

**Hvad er det?**

- Som en promptteknik involverer RAG at formulere specifikke forespørgsler eller prompts for at styre hentningen af relevant information fra et stort korpus eller en database. Denne information bruges derefter til at generere svar eller handlinger.

**Hvordan det virker:**

1. **Formulering af Prompts**: Opret velstrukturerede prompts eller forespørgsler baseret på opgaven eller brugerens input.
2. **Hentning af Information**: Brug prompts til at søge efter relevant data fra en eksisterende vidensbase eller datasæt.
3. **Generering af Svar**: Kombiner den hentede information med generative AI-modeller for at producere et omfattende og sammenhængende svar.

**Eksempel i rejseagent:**

- Brugerinput: "Jeg vil besøge museer i Paris."
- Prompt: "Find top museer i Paris."
- Hentet Information: Information om Louvre Museum, Musée d'Orsay, osv.
- Genereret Svar: "Her er nogle top museer i Paris: Louvre Museum, Musée d'Orsay, og Centre Pompidou."

#### RAG som et Værktøj

**Hvad er det?**

- Som et værktøj er RAG et integreret system, der automatiserer hentnings- og genereringsprocessen, hvilket gør det nemmere for udviklere at implementere komplekse AI-funktionaliteter uden manuelt at skulle udforme prompts for hver forespørgsel.

**Hvordan det virker:**

1. **Integration**: Indbyg RAG i AI-agentens arkitektur, så den automatisk kan håndtere hentnings- og genereringsopgaver.
2. **Automatisering**: Værktøjet styrer hele processen, fra modtagelse af brugerinput til generering af det endelige svar, uden at kræve eksplicitte prompts for hvert trin.
3. **Effektivitet**: Forbedrer agentens ydeevne ved at strømline hentnings- og genereringsprocessen, hvilket muliggør hurtigere og mere præcise svar.

**Eksempel i rejseagent:**

- Brugerinput: "Jeg vil besøge museer i Paris."
- RAG-værktøj: Henter automatisk information om museer og genererer et svar.
- Genereret Svar: "Her er nogle top museer i Paris: Louvre Museum, Musée d'Orsay, og Centre Pompidou."

### Sammenligning

| Aspekt                 | Promptteknik                                                | Værktøj                                               |
|------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| **Manuel vs Automatisk**| Manuel formulering af prompts for hver forespørgsel.        | Automatisk proces for hentning og generering.         |
| **Kontrol**            | Tilbyder mere kontrol over hentningsprocessen.              | Strømliner og automatiserer hentning og generering.   |
| **Fleksibilitet**       | Tillader tilpassede prompts baseret på specifikke behov.    | Mere effektiv til implementering i stor skala.         |
| **Kompleksitet**        | Kræver udformning og justering af prompts.                  | Nemmere at integrere i en AI-agents arkitektur.        |

### Praktiske Eksempler

**Eksempel på Promptteknik:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Eksempel på Værktøj:**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### Evaluering af Relevans

Evaluering af relevans er et afgørende aspekt af AI-agenters ydeevne. Det sikrer, at den information, der hentes og genereres af agenten, er passende, korrekt og nyttig for brugeren. Lad os udforske, hvordan man evaluerer relevans i AI-agenter, inklusive praktiske eksempler og teknikker.

#### Centrale Begreber i Evaluering af Relevans

1. **Kontekstbevidsthed**:
   - Agenten skal forstå konteksten af brugerens forespørgsel for at hente og generere relevant information.
   - Eksempel: Hvis en bruger spørger om "bedste restauranter i Paris," bør agenten tage højde for brugerens præferencer, såsom køkkentype og budget.

2. **Nøjagtighed**:
   - Den information, agenten leverer, bør være faktuelt korrekt og opdateret.
   - Eksempel: Anbefaling af restauranter, der er åbne og har gode anmeldelser, fremfor forældede eller lukkede steder.

3. **Brugerintention**:
   - Agenten bør udlede brugerens intention bag forespørgslen for at give den mest relevante information.
   - Eksempel: Hvis en bruger spørger om "budgetvenlige hoteller," bør agenten prioritere prisvenlige muligheder.

4. **Feedback Loop**:
   - Kontinuerlig indsamling og analyse af brugerfeedback hjælper agenten med at forfine sin evaluering af relevans.
   - Eksempel: Indarbejdelse af brugerbedømmelser og feedback på tidligere anbefalinger for at forbedre fremtidige svar.

#### Praktiske Teknikker til Evaluering af Relevans

1. **Relevansscore**:
   - Tildel en relevansscore til hvert hentet element baseret på, hvor godt det matcher brugerens forespørgsel og præferencer.
   - Eksempel:

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. **Filtrering og Rangering**:
   - Filtrer irrelevante elementer fra og ranger de tilbageværende baseret på deres relevansscore.
   - Eksempel:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Returner top 10 relevante elementer
     ```

3. **Natural Language Processing (NLP)**:
   - Brug NLP-teknikker til at forstå brugerens forespørgsel og hente relevant information.
   - Eksempel:

     ```python
     def process_query(query):
         # Brug NLP til at udtrække nøgleinformation fra brugerens forespørgsel
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integration af Brugerfeedback**:
   - Indsaml brugerfeedback på de givne anbefalinger og brug det til at justere fremtidige vurderinger af relevans.
   - Eksempel:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Eksempel: Evaluering af Relevans i Rejseagent

Her er et praktisk eksempel på, hvordan Travel Agent kan evaluere relevansen af rejseanbefalinger:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # Returner de 10 mest relevante elementer

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# Eksempel på anvendelse
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Søgn med Intention

At søge med intention involverer at forstå og fortolke det underliggende formål eller mål bag en brugers forespørgsel for at hente og generere den mest relevante og nyttige information. Denne tilgang går ud over blot at matche nøgleord og fokuserer på at gribe brugerens faktiske behov og kontekst.

#### Centrale Begreber i Søgning med Intention

1. **Forståelse af Brugerintention**:
   - Brugerintention kan kategoriseres i tre hovedtyper: informationssøgende, navigationssøgende og transaktionelle.
     - **Informationssøgende Intention**: Brugeren søger information om et emne (f.eks. "Hvad er de bedste museer i Paris?").
     - **Navigationssøgende Intention**: Brugeren vil navigere til en bestemt hjemmeside eller side (f.eks. "Louvre Museums officielle hjemmeside").
     - **Transaktionel Intention**: Brugeren sigter mod at udføre en transaktion, såsom at booke en flyrejse eller foretage et køb (f.eks. "Book en flyrejse til Paris").

2. **Kontekstbevidsthed**:
   - Analyse af konteksten for brugerens forespørgsel hjælper med præcist at identificere deres intention. Dette inkluderer tidligere interaktioner, brugerpræferencer og de specifikke detaljer i den aktuelle forespørgsel.

3. **Natural Language Processing (NLP)**:
   - NLP-teknikker anvendes til at forstå og fortolke naturlige sprogforespørgsler fra brugere. Dette inkluderer opgaver som entitetsgenkendelse, sentimentanalyse og forespørgselsparsing.

4. **Personalisering**:
   - Personaliserede søgeresultater baseret på brugerens historik, præferencer og feedback forbedrer relevansen af den hentede information.

#### Praktisk Eksempel: Søgn med Intention i Rejseagent

Lad os tage Travel Agent som eksempel og se, hvordan søgning med intention kan implementeres.

1. **Indsamling af Brugerpræferencer**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Forståelse af Brugerintention**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Kontekstbevidsthed**


   ```python
   def analyze_context(query, user_history):
       # Kombiner aktuel forespørgsel med brugerhistorik for at forstå kontekst
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Søg og personaliser resultater**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Eksempel på søgelogik for informationsintention
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Eksempel på søgelogik for navigationsintention
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Eksempel på søgelogik for transaktionsintention
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Eksempel på personaliseringslogik
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Returner top 10 personaliserede resultater
   ```

5. **Eksempel på brug**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. Generering af kode som et værktøj

Kodegenererende agenter bruger AI-modeller til at skrive og eksekvere kode, løse komplekse problemer og automatisere opgaver.

### Kodegenererende agenter

Kodegenererende agenter bruger generative AI-modeller til at skrive og eksekvere kode. Disse agenter kan løse komplekse problemer, automatisere opgaver og levere værdifuld indsigt ved at generere og køre kode i forskellige programmeringssprog.

#### Praktiske anvendelser

1. **Automatiseret kodegenerering**: Generer kodeuddrag til specifikke opgaver, såsom dataanalyse, web-scraping eller maskinlæring.
2. **SQL som en RAG**: Brug SQL-forespørgsler til at hente og manipulere data fra databaser.
3. **Problemløsning**: Opret og eksekver kode for at løse specifikke problemer, såsom optimering af algoritmer eller dataanalyse.

#### Eksempel: Kodegenererende agent til dataanalyse

Forestil dig, at du designer en kodegenererende agent. Her er, hvordan den kunne fungere:

1. **Opgave**: Analysere et datasæt for at identificere trends og mønstre.
2. **Trin**:
   - Indlæs datasættet i et dataanalysetool.
   - Generer SQL-forespørgsler for at filtrere og aggregere dataene.
   - Eksekver forespørgslerne og hent resultaterne.
   - Brug resultaterne til at generere visualiseringer og indsigt.
3. **Nødvendige ressourcer**: Adgang til datasættet, dataanalysetools og SQL-kapaciteter.
4. **Erfaring**: Brug tidligere analysedata til at forbedre nøjagtigheden og relevansen af fremtidige analyser.

### Eksempel: Kodegenererende agent til rejsebureau

I dette eksempel designer vi en kodegenererende agent, Travel Agent, til at hjælpe brugere med at planlægge deres rejse ved at generere og eksekvere kode. Denne agent kan håndtere opgaver som at hente rejsemuligheder, filtrere resultater og sammensætte en rejseplan ved hjælp af generativ AI.

#### Oversigt over den kodegenererende agent

1. **Indsamling af brugerpræferencer**: Indsamler brugerinput som destination, rejsedatoer, budget og interesser.
2. **Generering af kode til dataindsamling**: Genererer kodeuddrag til at hente data om fly, hoteller og attraktioner.
3. **Eksekvering af genereret kode**: Kører den genererede kode for at hente realtidsinformation.
4. **Generering af rejseplan**: Sammensætter de indhentede data til en personlig rejseplan.
5. **Justering baseret på feedback**: Modtager brugerfeedback og genererer eventuelt koden igen for at forbedre resultaterne.

#### Trin-for-trin implementering

1. **Indsamling af brugerpræferencer**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generering af kode til dataindsamling**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Eksempel: Generer kode til at søge efter fly baseret på brugerpræferencer
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Eksempel: Generer kode til at søge efter hoteller
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Eksekvering af genereret kode**

   ```python
   def execute_code(code):
       # Udfør den genererede kode ved hjælp af exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **Generering af rejseplan**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **Justering baseret på feedback**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Juster præferencer baseret på brugerfeedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerer og kør kode med opdaterede præferencer
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Udnyttelse af miljøbevidsthed og ræsonnement

Baseret på skemaet for tabellen kan det faktisk forbedre forespørgselsgenereringsprocessen ved at udnytte miljøbevidsthed og ræsonnement.

Her er et eksempel på, hvordan dette kan gøres:

1. **Forståelse af skemaet**: Systemet forstår tabellens skema og bruger denne information til at forankre genereringen af forespørgsler.
2. **Justering baseret på feedback**: Systemet justerer brugerpræferencer baseret på feedback og ræsonnerer om, hvilke felter i skemaet der skal opdateres.
3. **Generering og eksekvering af forespørgsler**: Systemet genererer og eksekverer forespørgsler for at hente opdaterede fly- og hoteldata baseret på de nye præferencer.

Her er et opdateret Python-kodeeksempel, der inkorporerer disse koncepter:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Juster præferencer baseret på brugerfeedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Begrænsning baseret på skema for at justere andre relaterede præferencer
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Tilpasset logik til at justere præferencer baseret på skema og feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generer kode til at hente flydata baseret på opdaterede præferencer
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generer kode til at hente hoteldata baseret på opdaterede præferencer
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simuler udførelse af kode og returner eksempeldata
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generer rejseplan baseret på fly, hoteller og attraktioner
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Eksempelskema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Eksempelbrug
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Generer og udfør kode igen med opdaterede præferencer
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Forklaring - Booking baseret på feedback

1. **Skemabevidsthed**: Ordbogen `schema` definerer, hvordan præferencer skal justeres baseret på feedback. Den inkluderer felter som `favorites` og `avoid` med tilhørende justeringer.
2. **Justering af præferencer (`adjust_based_on_feedback`-metoden)**: Denne metode justerer præferencer baseret på brugerfeedback og skemaet.
3. **Miljøbaserede justeringer (`adjust_based_on_environment`-metoden)**: Denne metode tilpasser justeringerne baseret på skema og feedback.
4. **Generering og eksekvering af forespørgsler**: Systemet genererer kode til at hente opdateret fly- og hoteldata baseret på de justerede præferencer og simulerer udførelsen af disse forespørgsler.
5. **Generering af rejseplan**: Systemet laver en opdateret rejseplan baseret på de nye fly-, hotel- og attraktionsdata.

Ved at gøre systemet miljøbevidst og ræsonnere baseret på skemaet kan det generere mere præcise og relevante forespørgsler, hvilket fører til bedre rejseanbefalinger og en mere personlig brugeroplevelse.

### Brug af SQL som Retrieval-Augmented Generation (RAG) teknik

SQL (Structured Query Language) er et kraftfuldt værktøj til at interagere med databaser. Når det bruges som en del af en Retrieval-Augmented Generation (RAG) tilgang, kan SQL hente relevante data fra databaser for at informere og generere svar eller handlinger i AI-agenter. Lad os se på, hvordan SQL kan bruges som en RAG-teknik i sammenhæng med Travel Agent.

#### Nøglekoncepter

1. **Databaseinteraktion**:
   - SQL bruges til at forespørge databaser, hente relevant information og manipulere data.
   - Eksempel: Hente flyoplysninger, hotelinformationer og attraktioner fra en rejsedatabase.

2. **Integration med RAG**:
   - SQL-forespørgsler genereres baseret på brugerinput og præferencer.
   - De hentede data bruges derefter til at generere personlige anbefalinger eller handlinger.

3. **Dynamisk forespørgselsgenerering**:
   - AI-agenten genererer dynamiske SQL-forespørgsler baseret på kontekst og brugerbehov.
   - Eksempel: Tilpasning af SQL-forespørgsler for at filtrere resultater baseret på budget, datoer og interesser.

#### Anvendelser

- **Automatiseret kodegenerering**: Generer kodeuddrag til specifikke opgaver.
- **SQL som en RAG**: Brug SQL-forespørgsler til at manipulere data.
- **Problemløsning**: Opret og eksekver kode for at løse problemer.

**Eksempel**:
En dataanalyseagent:

1. **Opgave**: Analysere et datasæt for at finde trends.
2. **Trin**:
   - Indlæs datasættet.
   - Generer SQL-forespørgsler for at filtrere data.
   - Eksekver forespørgsler og hent resultater.
   - Generer visualiseringer og indsigt.
3. **Ressourcer**: Adgang til datasæt, SQL-kapaciteter.
4. **Erfaring**: Brug tidligere resultater til at forbedre fremtidige analyser.

#### Praktisk eksempel: Brug af SQL i Travel Agent

1. **Indsamling af brugerpræferencer**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generering af SQL-forespørgsler**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Eksekvering af SQL-forespørgsler**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **Generering af anbefalinger**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### Eksempel på SQL-forespørgsler

1. **Flyforespørgsel**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Hotel-forespørgsel**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Attraktionsforespørgsel**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Ved at udnytte SQL som en del af Retrieval-Augmented Generation (RAG) teknikken kan AI-agenter som Travel Agent dynamisk hente og bruge relevante data til at levere nøjagtige og personlige anbefalinger.

### Eksempel på metakognition

For at demonstrere en implementering af metakognition, lad os skabe en simpel agent, der *reflekterer over sin beslutningsproces*, mens den løser et problem. I dette eksempel bygger vi et system, hvor en agent prøver at optimere valget af et hotel, men derefter evaluerer sin egen ræsonnering og justerer sin strategi, når den begår fejl eller laver suboptimale valg.

Vi vil simulere dette med et grundlæggende eksempel, hvor agenten vælger hoteller baseret på en kombination af pris og kvalitet, men den vil "reflektere" over sine beslutninger og justere dem derefter.

#### Hvordan dette illustrerer metakognition:

1. **Indledende beslutning**: Agenten vælger det billigste hotel uden at forstå kvalitetsindvirkningen.
2. **Refleksion og evaluering**: Efter det indledende valg vil agenten tjekke, om hotellet var et "dårligt" valg ved hjælp af brugerfeedback. Hvis den finder ud af, at hotellets kvalitet var for lav, reflekterer den over sin ræsonnering.
3. **Justering af strategi**: Agenten justerer sin strategi baseret på sin refleksion og skifter fra "billigst" til "højeste_kvalitet", hvilket forbedrer beslutningsprocessen i fremtidige iterationer.

Her er et eksempel:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Gemmer de hoteller, der tidligere er valgt
        self.corrected_choices = []  # Gemmer de rettede valg
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Tilgængelige strategier

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Lad os antage, at vi har noget brugerfeedback, der fortæller os, om det sidste valg var godt eller ej
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Juster strategi, hvis det tidligere valg var utilfredsstillende
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simuler en liste over hoteller (pris og kvalitet)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Opret en agent
agent = HotelRecommendationAgent()

# Trin 1: Agenten anbefaler et hotel ved hjælp af "billigste" strategi
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Trin 2: Agenten reflekterer over valget og justerer strategien om nødvendigt
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Trin 3: Agenten anbefaler igen, denne gang ved hjælp af den justerede strategi
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Agenters metakognitive evner

Det centrale her er agentens evne til at:
- Evaluere sine tidligere valg og beslutningsproces.
- Justere sin strategi baseret på denne refleksion, dvs. metakognition i praksis.

Dette er en simpel form for metakognition, hvor systemet er i stand til at justere sin ræsonneringsproces baseret på intern feedback.

### Konklusion

Metakognition er et kraftfuldt værktøj, som signifikant kan forbedre AI-agenters evner. Ved at inkorporere metakognitive processer kan du designe agenter, der er mere intelligente, tilpasningsdygtige og effektive. Brug de ekstra ressourcer til at udforske den fascinerende verden af metakognition i AI-agenter yderligere.

### Har du flere spørgsmål om metakognitionsdesignmønsteret?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i office hours og få svar på dine spørgsmål om AI-agenters design.

## Forrige lektion

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Næste lektion

[AI Agents in Production](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->