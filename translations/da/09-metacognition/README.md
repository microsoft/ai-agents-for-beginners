[![Multi-Agent Design](../../../translated_images/da/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_
# Metakognition i AI-agenter

## Introduktion

Velkommen til lektionen om metakognition i AI-agenter! Dette kapitel er designet til begyndere, der er nysgerrige efter, hvordan AI-agenter kan reflektere over deres egne tankeprocesser. Ved slutningen af denne lektion vil du have forstået nøglebegreber og være udstyret med praktiske eksempler til at anvende metakognition i design af AI-agenter.

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

1. Forstå konsekvenserne af ræsonneringssløjfer i agentdefinitioner.
2. Anvende planlægnings- og evalueringsmetoder til at hjælpe selvkorrigerende agenter.
3. Skabe dine egne agenter, der er i stand til at manipulere kode for at løse opgaver.

## Introduktion til Metakognition

Metakognition henviser til de højere ordens kognitive processer, der involverer at tænke over eget tænkning. For AI-agenter betyder det at kunne evaluere og justere deres handlinger baseret på selvbevidsthed og tidligere erfaringer. Metakognition, eller "at tænke over tænkning," er et vigtigt koncept i udviklingen af agentiske AI-systemer. Det indebærer, at AI-systemer er bevidste om deres egne interne processer og kan overvåge, regulere og tilpasse deres adfærd derefter. Ligesom vi gør, når vi læser stemningen i et rum eller ser på et problem. Denne selvbevidsthed kan hjælpe AI-systemer med at træffe bedre beslutninger, identificere fejl og forbedre deres ydeevne over tid - og igen knytte det til Turing-testen og debatten om, hvorvidt AI vil overtage.

I forbindelse med agentiske AI-systemer kan metakognition hjælpe med at adressere flere udfordringer, såsom:
- Gennemsigtighed: Sikre, at AI-systemer kan forklare deres ræsonnementer og beslutninger.
- Ræsonnering: Forbedre AI-systemers evne til at syntetisere information og træffe velbegrundede beslutninger.
- Tilpasning: Give AI-systemer mulighed for at justere sig til nye miljøer og skiftende betingelser.
- Opfattelse: Forbedre nøjagtigheden af AI-systemer i at genkende og fortolke data fra deres omgivelser.

### Hvad er Metakognition?

Metakognition, eller "at tænke over tænkning," er en højere ordens kognitiv proces, der involverer selvbevidsthed og selvregulering af egne kognitive processer. Inden for AI giver metakognition agenter mulighed for at evaluere og tilpasse deres strategier og handlinger, hvilket fører til forbedret problemløsning og beslutningstagning. Ved at forstå metakognition kan du designe AI-agenter, der ikke blot er mere intelligente, men også mere tilpasningsdygtige og effektive. I ægte metakognition vil du se, at AI eksplicit ræsonnerer om sit eget ræsonnement.

Eksempel: "Jeg prioriterede billigere flyvninger fordi... jeg måske går glip af direkte fly, så lad mig tjekke igen."
Holde styr på, hvordan eller hvorfor den valgte en bestemt rute.
- Bemærke, at den begik fejl, fordi den overbetroede brugerpræferencer fra sidste gang, så den ændrer sin beslutningstagningsstrategi og ikke bare den endelige anbefaling.
- Diagnosticere mønstre som: "Hver gang jeg ser brugeren nævne 'for mange mennesker', bør jeg ikke kun fjerne visse seværdigheder, men også reflektere over, at min metode til at udvælge 'top seværdigheder' er fejlbehæftet, hvis jeg altid rangerer efter popularitet."

### Betydningen af Metakognition i AI-agenter

Metakognition spiller en afgørende rolle i designet af AI-agenter af flere årsager:

![Betydningen af Metakognition](../../../translated_images/da/importance-of-metacognition.b381afe9aae352f7.webp)

- Selvrefleksion: Agenter kan vurdere deres egen præstation og identificere forbedringsområder.
- Tilpasningsevne: Agenter kan ændre deres strategier baseret på tidligere erfaringer og skiftende miljøer.
- Fejlretning: Agenter kan opdage og rette fejl autonomt, hvilket fører til mere præcise resultater.
- Ressourcestyring: Agenter kan optimere brugen af ressourcer, såsom tid og beregningskraft, ved at planlægge og evaluere deres handlinger.

## Komponenter i en AI-agent

Før vi dykker ned i metakognitive processer, er det vigtigt at forstå de grundlæggende komponenter i en AI-agent. En AI-agent består typisk af:

- Persona: Agentens personlighed og karakteristika, som definerer, hvordan den interagerer med brugerne.
- Værktøjer: Agentens evner og funktioner.
- Færdigheder: Den viden og ekspertise, som agenten besidder.

Disse komponenter arbejder sammen for at skabe en "ekspertiseenhed," der kan udføre specifikke opgaver.

**Eksempel**:
Forestil dig en rejseagent, der ikke kun planlægger din ferie, men også tilpasser sin plan baseret på realtidsdata og tidligere kunderejseoplevelser.

### Eksempel: Metakognition i en Rejseagentservice

Forestil dig, at du designer en rejseagentservice drevet af AI. Denne agent, "Rejseagent," hjælper brugere med at planlægge deres ferier. For at inkorporere metakognition skal Rejseagenten evaluere og tilpasse sine handlinger baseret på selvbevidsthed og tidligere erfaringer. Her er hvordan metakognition kunne spille en rolle:

#### Nuværende Opgave

Den nuværende opgave er at hjælpe en bruger med at planlægge en tur til Paris.

#### Trin for at Fuldføre Opgaven

1. **Indsamle Brugerpræferencer**: Spørg brugeren om deres rejsedatoer, budget, interesser (f.eks. museer, mad, shopping) og eventuelle specifikke krav.
2. **Hente Information**: Søg efter flymuligheder, indkvartering, seværdigheder og restauranter, der matcher brugerens præferencer.
3. **Generere Anbefalinger**: Giv en personlig rejseplan med flydetaljer, hotelreservationer og foreslåede aktiviteter.
4. **Justere Baseret på Feedback**: Spørg brugeren om feedback på anbefalingerne og foretag nødvendige justeringer.

#### Nødvendige Ressourcer

- Adgang til fly- og hotelbookingsdatabaser.
- Information om parisiske seværdigheder og restauranter.
- Brugerfeedbackdata fra tidligere interaktioner.

#### Erfaring og Selvrefleksion

Rejseagenten bruger metakognition til at evaluere sin præstation og lære af tidligere erfaringer. For eksempel:

1. **Analysere Brugerfeedback**: Rejseagenten gennemgår brugerfeedback for at afgøre, hvilke anbefalinger der blev godt modtaget, og hvilke der ikke gjorde. Den justerer sine fremtidige forslag i overensstemmelse hermed.
2. **Tilpasningsevne**: Hvis en bruger tidligere har nævnt, at de ikke kan lide overfyldte steder, vil Rejseagenten fremover undgå at anbefale populære turistattraktioner i myldretiden.
3. **Fejlretning**: Hvis Rejseagenten tidligere lavede en fejl i en booking, såsom at foreslå et hotel, der var fuldt booket, lærer den at tjekke tilgængelighed mere grundigt, før den giver anbefalinger.

#### Praktisk Udvikler Eksempel

Her er et forenklet eksempel på, hvordan Travel Agents kode kunne se ud, når metakognition integreres:

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

#### Hvorfor Metakognition Er Vigtigt

- **Selvrefleksion**: Agenter kan analysere deres ydeevne og identificere forbedringsområder.
- **Tilpasningsevne**: Agenter kan ændre strategier baseret på feedback og skiftende forhold.
- **Fejlretning**: Agenter kan opdage og rette fejl autonomt.
- **Ressourcestyring**: Agenter kan optimere ressourceanvendelse, såsom tid og beregningskraft.

Ved at inkorporere metakognition kan Rejseagenten levere mere personlige og præcise rejseanbefalinger, hvilket forbedrer den samlede brugeroplevelse.

---

## 2. Planlægning i Agenter

Planlægning er en kritisk komponent i AI-agenters adfærd. Det indebærer at skitsere de nødvendige trin for at opnå et mål, idet man tager hensyn til den nuværende tilstand, ressourcer og mulige forhindringer.

### Elementer i Planlægning

- **Nuværende Opgave**: Definer opgaven klart.
- **Trin for at Fuldføre Opgaven**: Opdel opgaven i håndterbare trin.
- **Nødvendige Ressourcer**: Identificer nødvendige ressourcer.
- **Erfaring**: Brug tidligere erfaringer til at informere planlægningen.

**Eksempel**:
Her er de trin, som Rejseagenten skal følge for effektivt at hjælpe en bruger med at planlægge deres rejse:

### Trin for Rejseagent

1. **Indsamle Brugerpræferencer**
   - Spørg brugeren om detaljer om deres rejsedatoer, budget, interesser og eventuelle specifikke krav.
   - Eksempler: "Hvornår planlægger du at rejse?" "Hvad er dit budget?" "Hvilke aktiviteter nyder du på ferie?"

2. **Hente Information**
   - Søg efter relevante rejsemuligheder baseret på brugerpræferencer.
   - **Flyvninger**: Find tilgængelige fly inden for brugerens budget og foretrukne rejsedatoer.
   - **Indkvartering**: Find hoteller eller lejeboliger, der matcher brugerens præferencer for placering, pris og faciliteter.
   - **Seværdigheder og Restauranter**: Identificer populære seværdigheder, aktiviteter og spisesteder, der matcher brugerens interesser.

3. **Generere Anbefalinger**
   - Sammensæt de hentede oplysninger i en personlig rejseplan.
   - Giv detaljer som flymuligheder, hotelreservationer og foreslåede aktiviteter, og tilpas anbefalingerne til brugerens præferencer.

4. **Præsenter Rejseplan til Bruger**
   - Del den foreslåede rejseplan med brugeren til gennemgang.
   - Eksempel: "Her er en foreslået rejseplan til din tur til Paris. Den inkluderer flyoplysninger, hotelbookinger og en liste over anbefalede aktiviteter og restauranter. Fortæl mig, hvad du synes!"

5. **Indsamle Feedback**
   - Spørg brugeren om feedback på den foreslåede rejseplan.
   - Eksempler: "Kan du lide flymulighederne?" "Er hotellet passende for dine behov?" "Er der aktiviteter, du vil tilføje eller fjerne?"

6. **Justere Baseret på Feedback**
   - Tilpas rejseplanen baseret på brugerens feedback.
   - Foretag nødvendige ændringer i fly-, indkvarterings- og aktivitetsanbefalinger for bedre at matche brugerens præferencer.

7. **Endelig Bekræftelse**
   - Præsenter den opdaterede rejseplan for brugeren til endelig bekræftelse.
   - Eksempel: "Jeg har foretaget ændringerne baseret på din feedback. Her er den opdaterede rejseplan. Ser det godt ud for dig?"

8. **Book og Bekræft Reservationer**
   - Når brugeren godkender rejseplanen, fortsæt med at booke fly, indkvartering og eventuelle forudplanlagte aktiviteter.
   - Send bekræftelsesoplysninger til brugeren.

9. **Yde Løbende Support**
   - Vær tilgængelig for at hjælpe brugeren med ændringer eller yderligere forespørgsler før og under rejsen.
   - Eksempel: "Hvis du har brug for yderligere hjælp under din rejse, er du velkommen til at kontakte mig når som helst!"

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

# Eksempel på brug i en bookinganmodning
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

## 3. Korrigerende RAG-system

Lad os først starte med at forstå forskellen mellem RAG-værktøj og Præemptiv kontekstindlæsning

![RAG vs Context Loading](../../../translated_images/da/rag-vs-context.9eae588520c00921.webp)

### Retrieval-Augmented Generation (RAG)

RAG kombinerer et hentningssystem med en generativ model. Når en forespørgsel foretages, henter hentningssystemet relevante dokumenter eller data fra en ekstern kilde, og denne hentede information bruges til at forstærke inputtet til den generative model. Dette hjælper modellen med at generere mere præcise og kontekstuelt relevante svar.

I et RAG-system henter agenten relevant information fra en vidensbase og bruger den til at generere passende svar eller handlinger.

### Korrigerende RAG-tilgang

Den korrigerende RAG-tilgang fokuserer på at bruge RAG-teknikker til at rette fejl og forbedre præcisionen af AI-agenter. Dette involverer:

1. **Prompting-teknik**: Brug af specifikke prompts til at vejlede agenten i at hente relevant information.
2. **Værktøj**: Implementering af algoritmer og mekanismer, der gør agenten i stand til at evaluere relevansen af den hentede information og generere præcise svar.
3. **Evaluering**: Kontinuerlig vurdering af agentens præstation og foretage justeringer for at forbedre nøjagtigheden og effektiviteten.

#### Eksempel: Korrigerende RAG i en Søgeagent

Overvej en søgeagent, der henter information fra internettet for at besvare brugerforespørgsler. Den korrigerende RAG-tilgang kan involvere:

1. **Prompting-teknik**: Formulere søgeforespørgsler baseret på brugerens input.
2. **Værktøj**: Brug af naturlig sprogbehandling og maskinlæringsalgoritmer til at rangere og filtrere søgeresultater.
3. **Evaluering**: Analysere brugerfeedback for at identificere og rette unøjagtigheder i den hentede information.

### Korrigerende RAG i Rejseagent

Korrigerende RAG (Retrieval-Augmented Generation) forbedrer en AI's evne til at hente og generere information samtidig med at rette eventuelle unøjagtigheder. Lad os se, hvordan Rejseagenten kan bruge den korrigerende RAG-tilgang til at give mere præcise og relevante rejseanbefalinger.

Dette indebærer:

- **Prompting-teknik:** Brug af specifikke prompts til at vejlede agenten i at hente relevant information.
- **Værktøj:** Implementering af algoritmer og mekanismer, der gør agenten i stand til at evaluere relevansen af den hentede information og generere præcise svar.
- **Evaluering:** Kontinuerlig vurdering af agentens præstation og foretage justeringer for at forbedre nøjagtigheden og effektiviteten.

#### Trin for Implementering af Korrigerende RAG i Rejseagent

1. **Første Brugerinteraktion**
   - Rejseagenten indsamler de første præferencer fra brugeren, såsom destination, rejsedatoer, budget og interesser.
   - Eksempel:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Indhentning af Information**
   - Rejseagenten henter information om fly, indkvartering, seværdigheder og restauranter baseret på brugerpræferencer.
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

5. **Korrigerende RAG-proces**
   - **Prompting-teknik**: Rejseagenten formulerer nye søgeforespørgsler baseret på brugerens feedback.
     - Eksempel:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Værktøj**: Rejseagenten bruger algoritmer til at rangere og filtrere nye søgeresultater med vægt på relevans baseret på brugerfeedback.
     - Eksempel:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Evaluering**: Rejseagenten vurderer kontinuerligt relevansen og nøjagtigheden af sine anbefalinger ved at analysere brugerfeedback og foretage nødvendige justeringer.
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

### Præemptiv kontekstindlæsning


Forudindlæst Kontekstbelastning involverer at indlæse relevant kontekst eller baggrundsinformation i modellen, før en forespørgsel behandles. Det betyder, at modellen har adgang til denne information fra starten, hvilket kan hjælpe den med at generere mere informerede svar uden at skulle hente yderligere data under processen.

Her er et forenklet eksempel på, hvordan en forudindlæst kontekstbelastning kan se ud for en rejseagent-applikation i Python:

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

1. **Initialisering (`__init__` metode)**: `TravelAgent`-klassen forudindlæser en ordbog, der indeholder information om populære destinationer som Paris, Tokyo, New York og Sydney. Denne ordbog inkluderer detaljer som land, valuta, sprog og større seværdigheder for hver destination.

2. **Hentning af Information (`get_destination_info` metode)**: Når en bruger spørger om en specifik destination, henter `get_destination_info`-metoden den relevante information fra den forudindlæste kontekstordbog.

Ved at forudindlæse konteksten kan rejseagent-applikationen hurtigt besvare brugerforespørgsler uden at skulle hente denne information fra en ekstern kilde i realtid. Det gør applikationen mere effektiv og responsiv.

### Bootstrapping af planen med et mål før iteration

Bootstrapping af en plan med et mål indebærer at starte med et klart objektiv eller ønsket resultat i tankerne. Ved at definere dette mål på forhånd kan modellen bruge det som en vejledende princip gennem hele den iterative proces. Dette hjælper med at sikre, at hver iteration bevæger sig tættere på at opnå det ønskede resultat, hvilket gør processen mere effektiv og fokuseret.

Her er et eksempel på, hvordan du kan bootstrappe en rejseplan med et mål, før du itererer for en rejseagent i Python:

### Scenarie

En rejseagent ønsker at planlægge en tilpasset ferie for en kunde. Målet er at skabe en rejseplan, der maksimerer kundens tilfredshed baseret på deres præferencer og budget.

### Trin

1. Definer kundens præferencer og budget.
2. Bootstrap den indledende plan baseret på disse præferencer.
3. Iterer for at forfine planen og optimere kundens tilfredshed.

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

1. **Initialisering (`__init__` metode)**: `TravelAgent`-klassen initialiseres med en liste af potentielle destinationer, hver med attributter som navn, omkostning og aktivitetstype.

2. **Bootstrapping af Planen (`bootstrap_plan` metode)**: Denne metode opretter en indledende rejseplan baseret på kundens præferencer og budget. Den gennemgår listen af destinationer og tilføjer dem til planen, hvis de matcher kundens præferencer og passer inden for budgettet.

3. **Matchning af Præferencer (`match_preferences` metode)**: Denne metode tjekker, om en destination matcher kundens præferencer.

4. **Iterering af Planen (`iterate_plan` metode)**: Denne metode forfiner den indledende plan ved at forsøge at erstatte hver destination i planen med et bedre match, under hensyntagen til kundens præferencer og budgetbegrænsninger.

5. **Beregning af Omkostninger (`calculate_cost` metode)**: Denne metode beregner den samlede omkostning af den aktuelle plan, inklusive en potentiel ny destination.

#### Eksempel på brug

- **Indledende Plan**: Rejseagenten opretter en indledende plan baseret på kundens præferencer for sightseeing og et budget på $2000.
- **Forfinet Plan**: Rejseagenten itererer planen og optimerer for kundens præferencer og budget.

Ved at bootstrappe planen med et klart mål (f.eks. at maksimere kundetilfredsheden) og iterere for at forfine planen kan rejseagenten skabe en tilpasset og optimeret rejseplan for kunden. Denne tilgang sikrer, at rejseplanen fra starten stemmer overens med kundens præferencer og budget og forbedres ved hver iteration.

### Udnyttelse af LLM til omrangering og scoring

Store Sprogmodeller (LLMs) kan bruges til omrangering og scoring ved at evaluere relevans og kvalitet af hentede dokumenter eller genererede svar. Sådan fungerer det:

**Hentning:** Det indledende hentetrin henter et sæt kandidatdokumenter eller svar baseret på forespørgslen.

**Omrangering:** LLM'en evaluerer disse kandidater og omrangerer dem baseret på deres relevans og kvalitet. Dette trin sikrer, at den mest relevante og kvalitetsrige information præsenteres først.

**Scoring:** LLM'en tildeler score til hver kandidat, som afspejler deres relevans og kvalitet. Dette hjælper med at vælge det bedste svar eller dokument til brugeren.

Ved at udnytte LLM'er til omrangering og scoring kan systemet tilbyde mere præcis og kontekstuelt relevant information, hvilket forbedrer brugeroplevelsen generelt.

Her er et eksempel på, hvordan en rejseagent kan bruge en Stor Sprogmodel (LLM) til omrangering og scoring af rejsedestinationer baseret på brugerpræferencer i Python:

#### Scenarie - Rejse baseret på præferencer

En rejseagent ønsker at anbefale de bedste rejsedestinationer til en kunde baseret på deres præferencer. LLM'en hjælper med at omrangere og score destinationerne for at sikre, at de mest relevante muligheder præsenteres.

#### Trin:

1. Indsaml brugerpræferencer.
2. Hent en liste over potentielle rejsedestinationer.
3. Brug LLM'en til at omrangere og score destinationerne baseret på brugerpræferencer.

Sådan kan du opdatere det tidligere eksempel til at bruge Azure OpenAI Services:

#### Krav

1. Du skal have et Azure-abonnement.
2. Opret en Azure OpenAI-ressource og hent din API-nøgle.

#### Eksempel på Python-kode

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generer et prompt til Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Definer overskrifter og data til forespørgslen
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Kald Azure OpenAI API'et for at få de omplacerede og scorende destinationer
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

#### Kodeforklaring - Præferenceboger

1. **Initialisering**: `TravelAgent`-klassen initialiseres med en liste af potentielle rejsedestinationer, hver med attributter som navn og beskrivelse.

2. **Få anbefalinger (`get_recommendations` metode)**: Denne metode genererer en prompt til Azure OpenAI-service baseret på brugerens præferencer og laver en HTTP POST-anmodning til Azure OpenAI API for at få omrangerede og scorrede destinationer.

3. **Generering af Prompt (`generate_prompt` metode)**: Denne metode konstruerer en prompt til Azure OpenAI, inklusive brugerens præferencer og listen af destinationer. Prompten guider modellen til at omrangere og score destinationerne baseret på de angivne præferencer.

4. **API-opkald**: `requests`-biblioteket bruges til at lave en HTTP POST-anmodning til Azure OpenAI API-endpointet. Svaret indeholder de omrangerede og scorrede destinationer.

5. **Eksempel på brug**: Rejseagenten indsamler brugerpræferencer (f.eks. interesse for sightseeing og mangfoldig kultur) og bruger Azure OpenAI-servicen til at få omrangerede og scorrede anbefalinger af rejsedestinationer.

Sørg for at erstatte `your_azure_openai_api_key` med din faktiske Azure OpenAI API-nøgle og `https://your-endpoint.com/...` med den faktiske endpoint-URL for din Azure OpenAI-udrulning.

Ved at udnytte LLM til omrangering og scoring kan rejseagenten give mere personlige og relevante rejseanbefalinger til kunderne og forbedre deres samlede oplevelse.

### RAG: Prompting-teknik vs værktøj

Retrieval-Augmented Generation (RAG) kan både være en prompting-teknik og et værktøj i udviklingen af AI-agenter. At forstå forskellen mellem de to kan hjælpe dig med at udnytte RAG mere effektivt i dine projekter.

#### RAG som prompting-teknik

**Hvad er det?**

- Som en prompting-teknik involverer RAG formulering af specifikke forespørgsler eller prompts for at styre hentningen af relevant information fra et stort korpus eller en database. Denne information bruges derefter til at generere svar eller handlinger.

**Hvordan det fungerer:**

1. **Formulere Prompts**: Opret velstrukturerede prompts eller forespørgsler baseret på den aktuelle opgave eller brugerens input.
2. **Hente Information**: Brug prompts til at søge efter relevant data fra en forudeksisterende vidensbase eller datasæt.
3. **Generere Svar**: Kombiner den hentede information med generative AI-modeller for at producere et omfattende og sammenhængende svar.

**Eksempel i rejseagent:**

- Brugerinput: "Jeg vil besøge museer i Paris."
- Prompt: "Find de bedste museer i Paris."
- Hentet Information: Detaljer om Louvre-museet, Musée d'Orsay osv.
- Genereret svar: "Her er nogle topmuseer i Paris: Louvre-museet, Musée d'Orsay og Centre Pompidou."

#### RAG som værktøj

**Hvad er det?**

- Som et værktøj er RAG et integreret system, der automatiserer hente- og genereringsprocessen, hvilket gør det lettere for udviklere at implementere komplekse AI-funktionaliteter uden manuelt at skulle skabe prompts for hver forespørgsel.

**Hvordan det fungerer:**

1. **Integration**: Integrer RAG i AI-agentens arkitektur, så den automatisk håndterer hente- og genereringsopgaverne.
2. **Automatisering**: Værktøjet styrer hele processen fra modtagelse af brugerinput til generering af det endelige svar uden at kræve eksplicitte prompts for hvert trin.
3. **Effektivitet**: Forbedrer agentens ydeevne ved at strømline hente- og genereringsprocessen, hvilket muliggør hurtigere og mere præcise svar.

**Eksempel i rejseagent:**

- Brugerinput: "Jeg vil besøge museer i Paris."
- RAG-værktøj: Henter automatisk information om museer og genererer et svar.
- Genereret svar: "Her er nogle topmuseer i Paris: Louvre-museet, Musée d'Orsay og Centre Pompidou."

### Sammenligning

| Aspekt                 | Prompting-teknik                                          | Værktøj                                              |
|------------------------|-----------------------------------------------------------|-----------------------------------------------------|
| **Manuel vs Automatisk**| Manuel formulering af prompts for hver forespørgsel.       | Automatiseret proces for hente- og generering.      |
| **Kontrol**            | Tilbyder mere kontrol over henteprocessen.                 | Strømliner og automatiserer hente- og generering.   |
| **Fleksibilitet**      | Tillader tilpassede prompts baseret på specifikke behov.   | Mere effektiv til storskala-implementeringer.       |
| **Kompleksitet**       | Kræver udformning og justering af prompts.                 | Letter integration i AI-agentens arkitektur.        |

### Praktiske eksempler

**Eksempel på prompting-teknik:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Eksempel på værktøj:**

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

### Evaluering af relevans

Evaluering af relevans er et vigtigt aspekt af AI-agenters ydeevne. Det sikrer, at den information, som agenten henter og genererer, er passende, korrekt og nyttig for brugeren. Lad os udforske, hvordan man evaluerer relevans i AI-agenter, inklusive praktiske eksempler og teknikker.

#### Centrale begreber i evaluering af relevans

1. **Kontekstbevidsthed**:
   - Agenten skal forstå konteksten af brugerens forespørgsel for at hente og generere relevant information.
   - Eksempel: Hvis en bruger spørger efter "bedste restauranter i Paris", bør agenten tage højde for brugerens præferencer, såsom køkken type og budget.

2. **Nøjagtighed**:
   - Den information, agenten leverer, bør være faktuelt korrekt og opdateret.
   - Eksempel: Anbefale restauranter, der er åbne nu med gode anmeldelser i stedet for forældede eller lukkede steder.

3. **Brugerintention**:
   - Agenten skal udlede brugerens intention bag forespørgslen for at levere den mest relevante information.
   - Eksempel: Hvis en bruger spørger om "budgetvenlige hoteller", bør agenten prioritere overkommelige muligheder.

4. **Feedback-loop**:
   - Kontinuerlig indsamling og analyse af brugerfeedback hjælper agenten med at forfine sin evaluering af relevans.
   - Eksempel: Inkorpore brugerbedømmelser og feedback på tidligere anbefalinger for at forbedre fremtidige svar.

#### Praktiske teknikker til evaluering af relevans

1. **Relevance Scoring**:
   - Tildel en relevansscore til hver hentet genstand baseret på, hvor godt den matcher brugerens forespørgsel og præferencer.
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
   - Filtrer irrelevante genstande fra og ranger de resterende baseret på deres relevansscore.
   - Eksempel:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Returner top 10 relevante elementer
     ```

3. **Naturlig Sprogbehandling (NLP)**:
   - Brug NLP-teknikker til at forstå brugerens forespørgsel og hente relevant information.
   - Eksempel:

     ```python
     def process_query(query):
         # Brug NLP til at udtrække nøgleinformation fra brugerens forespørgsel
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integration af Brugerfeedback**:
   - Indsaml brugerfeedback på de givne anbefalinger og brug det til at justere fremtidige evalueringer af relevans.
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

#### Eksempel: Evaluering af relevans i rejseagent

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
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Søgning med intention

Søgning med intention indebærer at forstå og fortolke det underliggende formål eller mål bag en brugers forespørgsel for at hente og generere den mest relevante og nyttige information. Denne tilgang går ud over blot at matche nøgleord og fokuserer på at greje brugerens egentlige behov og kontekst.

#### Centrale begreber i søgning med intention

1. **Forståelse af brugerens intention**:
   - Brugerintention kan kategoriseres i tre hovedtyper: informativ, navigations- og transaktionel.
     - **Informativ intention**: Brugeren søger information om et emne (f.eks. "Hvad er de bedste museer i Paris?").
     - **Navigationsintention**: Brugeren vil navigere til et bestemt websted eller en side (f.eks. "Louvre-museets officielle hjemmeside").
     - **Transaktionel intention**: Brugeren ønsker at udføre en transaktion, som f.eks. at booke en flyvning eller foretage et køb (f.eks. "Book en flyvning til Paris").

2. **Kontekstbevidsthed**:
   - Analyse af brugerens forespørgsels kontekst hjælper med nøjagtigt at identificere deres intention. Dette inkluderer at tage højde for tidligere interaktioner, brugerpræferencer og specifikke detaljer i den aktuelle forespørgsel.

3. **Naturlig Sprogbehandling (NLP)**:
   - NLP-teknikker anvendes til at forstå og fortolke de naturlige sprogforespørgsler, som brugerne afgiver. Dette inkluderer opgaver som entitetsgenkendelse, sentimentanalyse og forespørgselsparsing.

4. **Personalisering**:
   - Personalisering af søgeresultater baseret på brugerens historik, præferencer og feedback forbedrer relevansen af den hentede information.

#### Praktisk eksempel: Søgning med intention i rejseagent

Lad os tage Travel Agent som eksempel for at se, hvordan søgning med intention kan implementeres.

1. **Indsamling af brugerpræferencer**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Forståelse af brugerintention**

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
       # Kombiner den aktuelle forespørgsel med brugerens historik for at forstå konteksten
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Søg og Tilpas Resultater**

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
       # Eksempel på søgelogik for informativ hensigt
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Eksempel på søgelogik for navigationshensigt
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Eksempel på søgelogik for transaktionshensigt
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Eksempel på personaliseringslogik
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Returner de 10 bedste personaliserede resultater
   ```

5. **Eksempel på Brug**

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

Kodegenererende agenter bruger AI-modeller til at skrive og udføre kode, løse komplekse problemer og automatisere opgaver.

### Kodegenererende agenter

Kodegenererende agenter bruger generative AI-modeller til at skrive og udføre kode. Disse agenter kan løse komplekse problemer, automatisere opgaver og give værdifulde indsigt ved at generere og køre kode i forskellige programmeringssprog.

#### Praktiske anvendelser

1. **Automatisk kodegenerering**: Generer kodestumper til specifikke opgaver, såsom dataanalyse, web scraping eller maskinlæring.
2. **SQL som en RAG**: Brug SQL-forespørgsler til at hente og manipulere data fra databaser.
3. **Problemløsning**: Opret og udfør kode for at løse specifikke problemer, såsom optimering af algoritmer eller dataanalyse.

#### Eksempel: Kodegenererende agent til dataanalyse

Forestil dig, at du designer en kodegenererende agent. Sådan kunne den fungere:

1. **Opgave**: Analyser et datasæt for at identificere tendenser og mønstre.
2. **Trin**:
   - Indlæs datasættet i et dataanalysetool.
   - Generer SQL-forespørgsler til at filtrere og aggregere dataene.
   - Udfør forespørgslerne og hent resultaterne.
   - Brug resultaterne til at generere visualiseringer og indsigt.
3. **Nødvendige ressourcer**: Adgang til datasættet, dataanalysetools og SQL-muligheder.
4. **Erfaring**: Brug tidligere analyse-resultater til at forbedre præcisionen og relevansen af fremtidige analyser.

### Eksempel: Kodegenererende agent til rejsebureau

I dette eksempel designer vi en kodegenererende agent, Rejsebureau, til at hjælpe brugere med at planlægge deres rejse ved at generere og udføre kode. Denne agent kan håndtere opgaver som at hente rejsemuligheder, filtrere resultater og sammensætte en rejseplan ved hjælp af generativ AI.

#### Oversigt over den kodegenererende agent

1. **Indsamling af brugerpræferencer**: Indsamler brugerinput som destination, rejsedatoer, budget og interesser.
2. **Generering af kode til datahentning**: Genererer kodestumper for at hente data om fly, hoteller og attraktioner.
3. **Udførelse af genereret kode**: Kører den genererede kode for at hente realtidsinformation.
4. **Generering af rejseplan**: Sammensætter de hentede data til en personlig rejseplan.
5. **Justering baseret på feedback**: Modtager brugerfeedback og genererer kode igen, hvis det er nødvendigt, for at forfine resultaterne.

#### Trin-for-trin implementering

1. **Indsamling af brugerpræferencer**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generering af kode til datahentning**

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

3. **Udførelse af genereret kode**

   ```python
   def execute_code(code):
       # Kør den genererede kode ved hjælp af exec
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
   
   # Gengenerer og kører kode med opdaterede præferencer
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Udnyttelse af miljøbevidsthed og ræsonnering

Baseret på skemaet for tabellen kan man virkelig forbedre forespørgselsgenereringsprocessen ved at udnytte miljøbevidsthed og ræsonnering.

Her er et eksempel på, hvordan det kan gøres:

1. **Forståelse af skemaet**: Systemet forstår skemaet for tabellen og bruger denne information til at forankre forespørgselsgenereringen.
2. **Justering baseret på feedback**: Systemet justerer brugerpræferencer baseret på feedback og ræsonnerer om, hvilke felter i skemaet der skal opdateres.
3. **Generering og udførelse af forespørgsler**: Systemet genererer og udfører forespørgsler for at hente opdaterede fly- og hoteldata baseret på de nye præferencer.

Her er et opdateret Python-kodeeksempel, der inkorporerer disse koncepter:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Juster præferencer baseret på brugerfeedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Argumentation baseret på skema for at justere andre relaterede præferencer
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
    # Simuler udførelse af kode og returner mock-data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generer rejseplan baseret på fly, hoteller og attraktioner
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Eksempelskema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Eksempel på brug
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

1. **Schema Awareness**: Ordbogen `schema` definerer, hvordan præferencer skal justeres baseret på feedback. Den inkluderer felter som `favorites` og `avoid`, med tilsvarende justeringer.
2. **Justering af præferencer (`adjust_based_on_feedback` metode)**: Denne metode justerer præferencer baseret på brugerfeedback og skemaet.
3. **Miljøbaserede justeringer (`adjust_based_on_environment` metode)**: Denne metode tilpasser justeringerne baseret på skemaet og feedback.
4. **Generering og udførelse af forespørgsler**: Systemet genererer kode for at hente opdaterede fly- og hoteldata baseret på de justerede præferencer og simulerer udførelse af disse forespørgsler.
5. **Generering af rejseplan**: Systemet opretter en opdateret rejseplan baseret på de nye fly-, hotel- og attraktionsdata.

Ved at gøre systemet miljøbevidst og ræsonnere baseret på skemaet kan det generere mere præcise og relevante forespørgsler, hvilket fører til bedre rejseanbefalinger og en mere personlig brugeroplevelse.

### Brug af SQL som en Retrieval-Augmented Generation (RAG) teknik

SQL (Structured Query Language) er et kraftfuldt værktøj til at interagere med databaser. Når det bruges som en del af en Retrieval-Augmented Generation (RAG) tilgang, kan SQL hente relevante data fra databaser til at informere og generere svar eller handlinger i AI-agenter. Lad os udforske, hvordan SQL kan bruges som en RAG-teknik i konteksten af Rejsebureau.

#### Nøglekoncepter

1. **Interaktion med databaser**:
   - SQL bruges til at forespørge databaser, hente relevant information og manipulere data.
   - Eksempel: Hente flyoplysninger, hotelinformation og attraktioner fra en rejse-database.

2. **Integration med RAG**:
   - SQL-forespørgsler genereres baseret på brugerinput og præferencer.
   - De hentede data bruges derefter til at generere personlige anbefalinger eller handlinger.

3. **Dynamisk forespørgselsgenerering**:
   - AI-agenten genererer dynamiske SQL-forespørgsler baseret på kontekst og brugerbehov.
   - Eksempel: Tilpasse SQL-forespørgsler for at filtrere resultater baseret på budget, datoer og interesser.

#### Anvendelser

- **Automatisk kodegenerering**: Generer kodestumper til specifikke opgaver.
- **SQL som en RAG**: Brug SQL-forespørgsler til at manipulere data.
- **Problemløsning**: Opret og udfør kode for at løse problemer.

**Eksempel**:
En dataanalyseagent:

1. **Opgave**: Analyser et datasæt for at finde tendenser.
2. **Trin**:
   - Indlæs datasættet.
   - Generer SQL-forespørgsler for at filtrere data.
   - Udfør forespørgsler og hent resultater.
   - Generer visualiseringer og indsigt.
3. **Ressourcer**: Adgang til datasæt, SQL-muligheder.
4. **Erfaring**: Brug tidligere resultater til at forbedre fremtidige analyser.

#### Praktisk eksempel: Brug af SQL i Rejsebureau

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

3. **Udførelse af SQL-forespørgsler**

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

2. **Hotelforespørgsel**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Attraktionsforespørgsel**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Ved at udnytte SQL som en del af Retrieval-Augmented Generation (RAG) teknikken kan AI-agenter som Rejsebureau dynamisk hente og bruge relevante data til at levere præcise og personlige anbefalinger.

### Eksempel på metakognition

For at demonstrere en implementering af metakognition, lad os skabe en simpel agent, der *reflekterer over sin beslutningsproces*, mens den løser et problem. Til dette eksempel bygger vi et system, hvor en agent prøver at optimere valget af et hotel, men derefter evaluerer sin egen ræsonnering og justerer sin strategi, når den laver fejl eller suboptimale valg.

Vi simulerer dette med et grundlæggende eksempel, hvor agenten vælger hoteller baseret på en kombination af pris og kvalitet, men den vil "reflektere" over sine beslutninger og justere sig derefter.

#### Hvordan dette illustrerer metakognition:

1. **Indledende beslutning**: Agenten vælger det billigste hotel uden at forstå kvalitetsindvirkningen.
2. **Refleksion og evaluering**: Efter det indledende valg tjekker agenten, om hotellet er et "dårligt" valg ved hjælp af brugerfeedback. Hvis den finder, at hotellets kvalitet var for lav, reflekterer den over sin ræsonnering.
3. **Justering af strategi**: Agenten justerer sin strategi baseret på refleksionen og skifter fra "billigst" til "højeste kvalitet", hvilket forbedrer dens beslutningsproces i fremtidige iterationer.

Her er et eksempel:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Gemmer de tidligere valgte hoteller
        self.corrected_choices = []  # Gemmer de korrigerede valg
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
        # Lad os antage, at vi har nogle brugertilbagemeldinger, der fortæller os, om det sidste valg var godt eller ej
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

# Trin 3: Agenten anbefaler igen, denne gang ved brug af den justerede strategi
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Agenters metakognitive evner

Det centrale her er agentens evne til at:
- Evaluere sine tidligere valg og beslutningsproces.
- Justere sin strategi baseret på denne refleksion, dvs. metakognition i praksis.

Dette er en simpel form for metakognition, hvor systemet kan justere sin ræsonneringsproces baseret på intern feedback.

### Konklusion

Metakognition er et kraftfuldt værktøj, der kan forbedre AI-agenters evner betydeligt. Ved at integrere metakognitive processer kan du designe agenter, der er mere intelligente, tilpasningsdygtige og effektive. Brug de ekstra ressourcer til at udforske den fascinerende verden af metakognition i AI-agenter.

### Har du flere spørgsmål om metakognitionsdesignmønsteret?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Forrige lektion

[Multi-Agent designmønster](../08-multi-agent/README.md)

## Næste lektion

[AI-agenter i produktion](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->