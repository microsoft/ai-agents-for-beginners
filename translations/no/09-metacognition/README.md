[![Multi-agent design](../../../translated_images/no/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Klikk på bildet over for å se video av denne leksjonen)_
# Metakognisjon i AI-agenter

## Introduksjon

Velkommen til leksjonen om metakognisjon i AI-agenter! Dette kapitlet er laget for nybegynnere som er nysgjerrige på hvordan AI-agenter kan tenke på sine egne tankeprosesser. Når du er ferdig med denne leksjonen, vil du forstå nøkkelkonsepter og være utstyrt med praktiske eksempler for å anvende metakognisjon i utformingen av AI-agenter.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du kunne:

1. Forstå implikasjonene av resoneringssløyfer i agentdefinisjoner.
2. Bruke planleggings- og evalueringsteknikker for å hjelpe selvkorrigerende agenter.
3. Lage egne agenter som kan manipulere kode for å utføre oppgaver.

## Introduksjon til Metakognisjon

Metakognisjon refererer til de kognitive prosessene på et høyere nivå som innebærer å tenke på egen tenking. For AI-agenter betyr dette å kunne evaluere og justere sine handlinger basert på selvbevissthet og tidligere erfaringer. Metakognisjon, eller "å tenke på tenking," er et viktig konsept i utviklingen av agentiske AI-systemer. Det innebærer at AI-systemer er bevisste på sine egne interne prosesser og kan overvåke, regulere og tilpasse sin atferd deretter. Mye som vi gjør når vi "leser rommet" eller ser på et problem. Denne selvbevisstheten kan hjelpe AI-systemer med å ta bedre beslutninger, identifisere feil og forbedre ytelsen over tid – noe som igjen knytter tilbake til Turing-testen og debatten om hvorvidt AI kommer til å ta over.

I konteksten av agentiske AI-systemer kan metakognisjon hjelpe med å håndtere flere utfordringer, som:
- Åpenhet: Sikre at AI-systemer kan forklare sin resonnement og beslutninger.
- Resonnering: Forbedre AI-systemers evne til å syntetisere informasjon og ta gode beslutninger.
- Tilpasning: La AI-systemer justere seg til nye miljøer og skiftende forhold.
- Persepsjon: Forbedre nøyaktigheten til AI-systemer i å gjenkjenne og tolke data fra omgivelsene.

### Hva er Metakognisjon?

Metakognisjon, eller "å tenke på tenking," er en kognitiv prosess på et høyere nivå som innebærer selvbevissthet og selvregulering av egne kognitive prosesser. Innen AI gir metakognisjon agenter mulighet til å evaluere og tilpasse sine strategier og handlinger, noe som fører til forbedret problemløsing og beslutningstaking. Ved å forstå metakognisjon kan du designe AI-agenter som ikke bare er mer intelligente, men også mer tilpasningsdyktige og effektive. Ved ekte metakognisjon ser du AI eksplisitt resonnere om sin egen resonnement.

Eksempel: "Jeg prioriterte billigere flyreiser fordi... Jeg kan gå glipp av direkteflyvninger, så la meg sjekke på nytt."
Holde oversikt over hvordan eller hvorfor den valgte en bestemt rute.
- Legge merke til at den gjorde feil fordi den stolte for mye på brukerens preferanser fra sist gang, så den endrer sin beslutningsstrategi, ikke bare den endelige anbefalingen.
- Diagnostisere mønstre som, "Når jeg ser at brukeren nevner 'for mye mennesker,' bør jeg ikke bare fjerne visse attraksjoner, men også reflektere over at metoden min for å velge 'toppattraksjoner' er feil hvis jeg alltid rangerer etter popularitet."

### Viktigheten av Metakognisjon i AI-agenter

Metakognisjon spiller en avgjørende rolle i designen av AI-agenter av flere grunner:

![Viktigheten av Metakognisjon](../../../translated_images/no/importance-of-metacognition.b381afe9aae352f7.webp)

- Selvrefleksjon: Agenter kan vurdere sin egen ytelse og identifisere forbedringsområder.
- Tilpasningsevne: Agenter kan endre sine strategier basert på tidligere erfaring og skiftende omgivelser.
- Feilretting: Agenter kan oppdage og rette feil autonomt, noe som fører til mer nøyaktige resultater.
- Ressursforvaltning: Agenter kan optimalisere bruk av ressurser, som tid og beregningskraft, ved å planlegge og evaluere sine handlinger.

## Komponenter i en AI-agent

Før vi dykker ned i metakognitive prosesser, er det viktig å forstå de grunnleggende komponentene i en AI-agent. En AI-agent består vanligvis av:

- Persona: Agentens personlighet og egenskaper som definerer hvordan den samhandler med brukere.
- Verktøy: Kapasiteter og funksjoner som agenten kan utføre.
- Ferdigheter: Kunnskapen og ekspertisen agenten besitter.

Disse komponentene fungerer sammen for å skape en "ekspertiseenhet" som kan utføre spesifikke oppgaver.

**Eksempel**:
Tenk på en reiseagent, tjenesteagenten som ikke bare planlegger ferien din, men også justerer sin rute basert på sanntidsdata og tidligere kundeopplevelser.

### Eksempel: Metakognisjon i en reiseagenttjeneste

Forestill deg at du designer en reiseagenttjeneste drevet av AI. Denne agenten, "Reiseagent," hjelper brukere med å planlegge feriene sine. For å inkorporere metakognisjon må Reiseagenten evaluere og justere sine handlinger basert på selvbevissthet og tidligere erfaringer. Slik kan metakognisjon spille en rolle:

#### Nåværende oppgave

Den nåværende oppgaven er å hjelpe en bruker med å planlegge en tur til Paris.

#### Steg for å fullføre oppgaven

1. **Samle brukerpreferanser**: Spør brukeren om reisedatoer, budsjett, interesser (f.eks. museer, mat, shopping) og eventuelle spesifikke krav.
2. **Hente informasjon**: Søk etter flymuligheter, overnatting, attraksjoner og restauranter som matcher brukerens preferanser.
3. **Generere anbefalinger**: Gi en personlig reiserute med flydetaljer, hotellreservasjoner og foreslåtte aktiviteter.
4. **Justere basert på tilbakemeldinger**: Be brukeren om tilbakemelding på anbefalingene og gjør nødvendige justeringer.

#### Nødvendige ressurser

- Tilgang til databaser for fly- og hotellbestillinger.
- Informasjon om severdigheter og restauranter i Paris.
- Brukertilbakemeldinger fra tidligere interaksjoner.

#### Erfaring og selvrefleksjon

Reiseagenten bruker metakognisjon for å evaluere sin ytelse og lære av tidligere erfaringer. For eksempel:

1. **Analysere brukertilbakemeldinger**: Reiseagenten gjennomgår tilbakemeldinger for å avgjøre hvilke anbefalinger som ble godt mottatt og hvilke som ikke gjorde det. Den justerer sine fremtidige forslag deretter.
2. **Tilpasningsevne**: Hvis en bruker tidligere har nevnt at de ikke liker overfylte steder, vil Reiseagenten unngå å anbefale populære turiststeder i rushtiden i fremtiden.
3. **Feilretting**: Hvis Reiseagenten gjorde en feil i en tidligere bestilling, for eksempel foreslo et fulltbooket hotell, lærer den å sjekke tilgjengeligheten grundigere før den gir anbefalinger.

#### Praktisk utviklereksempel

Her er et forenklet eksempel på hvordan koden til Reiseagenten kan se ut ved inkorporering av metakognisjon:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Søk etter fly, hoteller og attraksjoner basert på preferanser
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
        # Analyser tilbakemeldinger og juster fremtidige anbefalinger
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Eksempel på bruk
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

#### Hvorfor metakognisjon betyr noe

- **Selvrefleksjon**: Agenter kan analysere sin ytelse og identifisere forbedringsområder.
- **Tilpasningsevne**: Agenter kan endre strategier basert på tilbakemelding og skiftende forhold.
- **Feilretting**: Agenter kan autonomt oppdage og rette feil.
- **Ressursforvaltning**: Agenter kan optimalisere ressursbruk, som tid og beregningskraft.

Ved å inkorporere metakognisjon kan Reiseagenten gi mer personlige og nøyaktige reiseanbefalinger, noe som forbedrer brukeropplevelsen totalt.

---

## 2. Planlegging i Agenter


Planlegging er en kritisk komponent i AI-agenters atferd. Det innebærer å skissere trinnene som trengs for å oppnå et mål, med hensyn til nåværende tilstand, ressurser og mulige hindringer.

### Elementer av planlegging

- **Nåværende oppgave**: Definer oppgaven klart.
- **Trinn for å fullføre oppgaven**: Del opp oppgaven i håndterbare trinn.
- **Nødvendige ressurser**: Identifiser nødvendige ressurser.
- **Erfaring**: Bruk tidligere erfaringer for å informere planlegging.

**Eksempel**:
Her er trinnene Reiseagent må ta for å hjelpe en bruker med å planlegge reisen effektivt:

### Trinn for Reiseagent

1. **Samle brukerpreferanser**
   - Spør brukeren om detaljer om reisedatoer, budsjett, interesser og eventuelle spesifikke krav.
   - Eksempler: "Når planlegger du å reise?" "Hva er ditt budsjettområde?" "Hvilke aktiviteter liker du på ferie?"

2. **Hente informasjon**
   - Søk etter relevante reisealternativer basert på brukerens preferanser.
   - **Flyvninger**: Se etter tilgjengelige flyvninger innen brukerens budsjett og foretrukne reisedatoer.
   - **Overnatting**: Finn hoteller eller leieeiendommer som matcher brukerens preferanser for beliggenhet, pris og fasiliteter.
   - **Attraksjoner og restauranter**: Identifiser populære attraksjoner, aktiviteter og spisesteder som stemmer overens med brukerens interesser.

3. **Generere anbefalinger**
   - Sett sammen den hentede informasjonen til en personlig reiseplan.
   - Gi detaljer som flyvalg, hotellreservasjoner og foreslåtte aktiviteter, og sørg for å skreddersy anbefalingene til brukerens preferanser.

4. **Presentere reiseplan til bruker**
   - Del det foreslåtte reiseopplegget med brukeren for gjennomgang.
   - Eksempel: "Her er et foreslått reiseopplegg for din tur til Paris. Det inkluderer flydetaljer, hotellbestillinger og en liste over anbefalte aktiviteter og restauranter. Gi meg gjerne tilbakemelding!"

5. **Innhente tilbakemelding**
   - Spør brukeren om tilbakemelding på det foreslåtte reiseopplegget.
   - Eksempler: "Liker du flyvalgene?" "Er hotellet passende for dine behov?" "Er det noen aktiviteter du vil legge til eller fjerne?"

6. **Justere basert på tilbakemelding**
   - Endre reiseplanen basert på brukerens tilbakemelding.
   - Gjør nødvendige endringer i fly-, overnattings- og aktivitetsanbefalingene for bedre å matche brukerens preferanser.

7. **Endelig bekreftelse**
   - Presenter den oppdaterte reiseplanen til brukeren for endelig bekreftelse.
   - Eksempel: "Jeg har gjort justeringene basert på tilbakemeldingen din. Her er den oppdaterte reiseplanen. Ser alt bra ut for deg?"

8. **Bestille og bekrefte reservasjoner**
   - Når brukeren godkjenner reiseplanen, gå videre med å bestille fly, overnatting og eventuelle forhåndsplanlagte aktiviteter.
   - Send bekreftelsesdetaljer til brukeren.

9. **Gi løpende støtte**
   - Vær tilgjengelig for å hjelpe brukeren med endringer eller ytterligere forespørsler før og under reisen.
   - Eksempel: "Hvis du trenger mer assistanse under reisen din, ikke nøl med å kontakte meg når som helst!"

### Eksempel på samhandling

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

# Eksempel på bruk i en bestillingsforespørsel
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

Først starter vi med å forstå forskjellen mellom RAG-verktøy og forhåndslasting av kontekst

![RAG vs Context Loading](../../../translated_images/no/rag-vs-context.9eae588520c00921.webp)

### Hentetilleggsgenerering (RAG)

RAG kombinerer et hentingssystem med en generativ modell. Når en forespørsel gjøres, henter hentingssystemet relevante dokumenter eller data fra en ekstern kilde, og denne hentede informasjonen brukes til å berike inngangen til den generative modellen. Dette hjelper modellen med å generere mer nøyaktige og kontekstrelevante svar.

I et RAG-system henter agenten relevant informasjon fra en kunnskapsbase og bruker den til å generere passende svar eller handlinger.

### Korrigerende RAG-tilnærming

Den korrigerende RAG-tilnærmingen fokuserer på å bruke RAG-teknikker for å rette feil og forbedre nøyaktigheten til AI-agenter. Dette innebærer:

1. **Promptteknikk**: Bruke spesifikke prompt for å veilede agenten i å hente relevant informasjon.
2. **Verktøy**: Implementere algoritmer og mekanismer som gjør det mulig for agenten å evaluere relevansen av hentet informasjon og generere nøyaktige svar.
3. **Evaluering**: Kontinuerlig vurdere agentens ytelse og gjøre justeringer for å forbedre nøyaktighet og effektivitet.

#### Eksempel: Korrigerende RAG i en søkeagent

Tenk på en søkeagent som henter informasjon fra nettet for å svare på brukerforespørsler. Den korrigerende RAG-tilnærmingen kan innebære:

1. **Promptteknikk**: Formulere søkeforespørsler basert på brukerens input.
2. **Verktøy**: Bruke naturlig språkprosessering og maskinlæringsalgoritmer for å rangere og filtrere søkeresultater.
3. **Evaluering**: Analysere brukerfeedback for å identifisere og rette unøyaktigheter i den hentede informasjonen.

### Korrigerende RAG i Reiseagent

Korrigerende RAG (Retrieval-Augmented Generation) forbedrer en AIs evne til å hente og generere informasjon samtidig som den retter opp unøyaktigheter. La oss se hvordan Reiseagent kan bruke den korrigerende RAG-tilnærmingen for å gi mer nøyaktige og relevante reiseanbefalinger.

Dette innebærer:

- **Promptteknikk:** Bruke spesifikke prompt for å veilede agenten i å hente relevant informasjon.
- **Verktøy:** Implementere algoritmer og mekanismer som gjør det mulig for agenten å evaluere relevansen av den hentede informasjonen og generere nøyaktige svar.
- **Evaluering:** Kontinuerlig vurdere agentens ytelse og gjøre justeringer for å forbedre nøyaktighet og effektivitet.

#### Trinn for å implementere korrigerende RAG i Reiseagent

1. **Innledende brukerinteraksjon**
   - Reiseagent samler inn første preferanser fra brukeren, som destinasjon, reisedatoer, budsjett og interesser.
   - Eksempel:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Henting av informasjon**
   - Reiseagent henter informasjon om flyvninger, overnatting, attraksjoner og restauranter basert på brukerens preferanser.
   - Eksempel:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generere innledende anbefalinger**
   - Reiseagent bruker den hentede informasjonen for å generere en personlig reiseplan.
   - Eksempel:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Innhente brukerfeedback**
   - Reiseagent ber brukeren om tilbakemelding på de innledende anbefalingene.
   - Eksempel:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Korrigerende RAG-prosess**
   - **Promptteknikk**: Reiseagent formulerer nye søkeforspørsler basert på brukerfeedback.
     - Eksempel:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Verktøy**: Reiseagent bruker algoritmer for å rangere og filtrere nye søkeresultater, med vekt på relevans basert på brukerfeedback.
     - Eksempel:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Evaluering**: Reiseagent vurderer kontinuerlig relevansen og nøyaktigheten av anbefalingene ved å analysere brukerfeedback og gjøre nødvendige justeringer.
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

#### Praktisk eksempel

Her er et forenklet Python-kodeeksempel som inkorporerer den korrigerende RAG-tilnærmingen i Reiseagent:

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

# Eksempel på bruk
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

### Forhåndslasting av kontekst


Forhåndslasting av kontekst innebærer å laste relevant kontekst eller bakgrunnsinformasjon inn i modellen før en spørring behandles. Dette betyr at modellen har tilgang til denne informasjonen fra starten av, noe som kan hjelpe den med å generere mer informerte svar uten å trenge å hente ekstra data underveis.

Her er et forenklet eksempel på hvordan forhåndslasting av kontekst kan se ut for en reisebyråapplikasjon i Python:

```python
class TravelAgent:
    def __init__(self):
        # Forhåndslast populære destinasjoner og deres informasjon
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Hent destinasjonsinformasjon fra forhåndslastet kontekst
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Eksempel på bruk
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Forklaring

1. **Initialisering (`__init__`-metode)**: `TravelAgent`-klassen forhåndslaster en ordbok som inneholder informasjon om populære destinasjoner som Paris, Tokyo, New York og Sydney. Denne ordboken inkluderer detaljer som land, valuta, språk og hovedattraksjoner for hver destinasjon.

2. **Hente informasjon (`get_destination_info`-metode)**: Når en bruker spør om en bestemt destinasjon, henter `get_destination_info`-metoden relevant informasjon fra den forhåndslastede kontekstordboken.

Ved å forhåndslaste konteksten kan reisebyråapplikasjonen raskt svare på brukerforespørsler uten å måtte hente denne informasjonen fra en ekstern kilde i sanntid. Dette gjør applikasjonen mer effektiv og responsiv.

### Bootstrapping av planen med et mål før iterasjon

Å bootstrappe en plan med et mål innebærer å starte med et klart mål eller ønsket resultat i tankene. Ved å definere dette målet på forhånd kan modellen bruke det som en ledende prinsipp gjennom hele den iterative prosessen. Dette hjelper med å sikre at hver iterasjon bringer oss nærmere å oppnå ønsket resultat, noe som gjør prosessen mer effektiv og fokusert.

Her er et eksempel på hvordan du kan bootstrappe en reiseplan med et mål før iterasjon for et reisebyrå i Python:

### Scenario

Et reisebyrå ønsker å planlegge en tilpasset ferie for en kunde. Målet er å lage en reiserute som maksimerer kundens tilfredshet basert på deres preferanser og budsjett.

### Steg

1. Definer kundens preferanser og budsjett.
2. Bootstrap den innledende planen basert på disse preferansene.
3. Iterer for å raffinere planen, optimalisert for kundens tilfredshet.

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

# Eksempel på bruk
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

#### Forklaring av kode

1. **Initialisering (`__init__`-metode)**: `TravelAgent`-klassen initialiseres med en liste over potensielle destinasjoner, hver med attributter som navn, kostnad og aktivitetstype.

2. **Bootstrapping av plan (`bootstrap_plan`-metode)**: Denne metoden lager en innledende reiseplan basert på kundens preferanser og budsjett. Den går gjennom listen av destinasjoner og legger dem til i planen hvis de matcher kundens preferanser og passer innenfor budsjettet.

3. **Matchende preferanser (`match_preferences`-metode)**: Denne metoden sjekker om en destinasjon samsvarer med kundens preferanser.

4. **Iterere plan (`iterate_plan`-metode)**: Denne metoden raffinerer den innledende planen ved å prøve å bytte ut hver destinasjon i planen med en bedre match, med tanke på kundens preferanser og budsjettbegrensninger.

5. **Beregne kostnad (`calculate_cost`-metode)**: Denne metoden beregner totalkostnaden for den nåværende planen, inkludert en potensiell ny destinasjon.

#### Eksempel på bruk

- **Innledende plan**: Reisebyrået lager en innledende plan basert på kundens preferanser for sightseeing og et budsjett på 2000 dollar.
- **Raffinert plan**: Reisebyrået itererer planen, optimalisert for kundens preferanser og budsjett.

Ved å bootstrappe planen med et klart mål (f.eks. å maksimere kundetilfredshet) og iterere for å raffinere planen, kan reisebyrået lage en tilpasset og optimalisert reiserute for kunden. Denne tilnærmingen sikrer at reiseplanen stemmer overens med kundens preferanser og budsjett fra starten av og forbedres for hver iterasjon.

### Utnyttelse av LLM for re-ranking og scoring

Store språkmodeller (LLM) kan brukes til re-ranking og scoring ved å evaluere relevansen og kvaliteten på hentede dokumenter eller genererte svar. Slik fungerer det:

**Henting:** Det første hentetrinnet henter et sett med kandidatdokumenter eller svar basert på spørringen.

**Re-ranking:** LLM evaluerer disse kandidatene og rangerer dem på nytt basert på relevans og kvalitet. Dette trinnet sikrer at den mest relevante og høy-kvalitets informasjonen presenteres først.

**Scoring:** LLM tildeler poeng til hver kandidat, som reflekterer deres relevans og kvalitet. Dette hjelper med å velge det beste svaret eller dokumentet for brukeren.

Ved å utnytte LLM for re-ranking og scoring kan systemet tilby mer nøyaktig og kontekstrelevant informasjon, noe som forbedrer brukeropplevelsen generelt.

Her er et eksempel på hvordan et reisebyrå kan bruke en stor språkmodell (LLM) for re-ranking og scoring av reisemål basert på brukerpreferanser i Python:

#### Scenario - Reise basert på preferanser

Et reisebyrå ønsker å anbefale de beste reisemålene til en kunde basert på deres preferanser. LLM vil hjelpe til med å re-rangere og score destinasjonene for å sikre at de mest relevante valgene presenteres.

#### Steg:

1. Samle brukerpreferanser.
2. Hent en liste over potensielle reisemål.
3. Bruk LLM til å re-rangere og score destinasjonene basert på brukerpreferanser.

Her er hvordan du kan oppdatere forrige eksempel for å bruke Azure OpenAI-tjenester:

#### Krav

1. Du må ha et Azure-abonnement.
2. Opprett en Azure OpenAI-ressurs og skaff API-nøkkelen din.

#### Eksempel på Python-kode

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generer en prompt for Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Definer overskrifter og innhold for forespørselen
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Kall Azure OpenAI API for å få de rangordnede og vurderte destinasjonene
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Hent ut og returner anbefalingene
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

# Eksempel på bruk
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

#### Forklaring av kode - Preference Booker

1. **Initialisering**: `TravelAgent`-klassen initialiseres med en liste over potensielle reisemål, hver med attributter som navn og beskrivelse.

2. **Få anbefalinger (`get_recommendations`-metode)**: Denne metoden genererer en prompt for Azure OpenAI-tjenesten basert på brukerens preferanser og gjør en HTTP POST-forespørsel til Azure OpenAI API for å få re-rangerte og scorede destinasjoner.

3. **Generere prompt (`generate_prompt`-metode)**: Denne metoden konstruerer en prompt for Azure OpenAI, som inkluderer brukerens preferanser og listen over destinasjoner. Prompten guider modellen til å re-rangere og score destinasjonene basert på de oppgitte preferansene.

4. **API-kall**: `requests`-biblioteket brukes for å gjøre en HTTP POST-forespørsel til Azure OpenAI API-endepunktet. Svaret inneholder de re-rangerte og scorede destinasjonene.

5. **Eksempel på bruk**: Reisebyrået samler brukerpreferanser (f.eks. interesse for sightseeing og mangfoldig kultur) og bruker Azure OpenAI-tjenesten for å få re-rangerte og scorede anbefalinger for reisemål.

Husk å erstatte `your_azure_openai_api_key` med din faktiske Azure OpenAI API-nøkkel og `https://your-endpoint.com/...` med den faktiske endepunkt-URL-en til din Azure OpenAI-distribusjon.

Ved å utnytte LLM for re-ranking og scoring kan reisebyrået gi mer personaliserte og relevante reiseanbefalinger til kunder, og dermed forbedre deres totale opplevelse.

### RAG: Prompting-teknikk kontra verktøy

Retrieval-Augmented Generation (RAG) kan være både en prompting-teknikk og et verktøy i utviklingen av AI-agenter. Å forstå forskjellen mellom de to kan hjelpe deg med å utnytte RAG mer effektivt i prosjektene dine.

#### RAG som prompting-teknikk

**Hva er det?**

- Som en prompting-teknikk innebærer RAG å formulere spesifikke spørringer eller prompts for å styre henting av relevant informasjon fra et stort korpus eller en database. Denne informasjonen brukes deretter til å generere svar eller handlinger.

**Hvordan det fungerer:**

1. **Formulere prompts**: Lag godt strukturerte prompts eller spørringer basert på oppgaven eller brukerens inndata.
2. **Hente informasjon**: Bruk promptene til å søke etter relevant data fra en forhåndseksisterende kunnskapsbase eller datasett.
3. **Generere svar**: Kombiner den hentede informasjonen med generative AI-modeller for å produsere et omfattende og sammenhengende svar.

**Eksempel i reisebyrå:**

- Brukerinput: "Jeg vil besøke museer i Paris."
- Prompt: "Finn toppmuseer i Paris."
- Hentet informasjon: Detaljer om Louvre-museet, Musée d'Orsay osv.
- Generert svar: "Her er noen toppmuseer i Paris: Louvre-museet, Musée d'Orsay og Centre Pompidou."

#### RAG som verktøy

**Hva er det?**

- Som et verktøy er RAG et integrert system som automatiserer hente- og genereringsprosessen, og gjør det enklere for utviklere å implementere komplekse AI-funksjoner uten å manuelt lage prompts for hver spørring.

**Hvordan det fungerer:**

1. **Integrasjon**: Integrer RAG i AI-agentens arkitektur, slik at den automatisk håndterer hente- og genereringsoppgaver.
2. **Automatisering**: Verktøyet administrerer hele prosessen, fra mottak av brukerinput til generering av det endelige svaret, uten at det kreves eksplisitte prompts for hvert trinn.
3. **Effektivitet**: Forbedrer agentens ytelse ved å strømlinjeforme hente- og genereringsprosessen, som muliggjør raskere og mer presise svar.

**Eksempel i reisebyrå:**

- Brukerinput: "Jeg vil besøke museer i Paris."
- RAG-verktøy: Henter automatisk informasjon om museer og genererer et svar.
- Generert svar: "Her er noen toppmuseer i Paris: Louvre-museet, Musée d'Orsay og Centre Pompidou."

### Sammenligning

| Aspekt                 | Prompting-teknikk                                        | Verktøy                                                |
|------------------------|---------------------------------------------------------|-------------------------------------------------------|
| **Manuell vs Automatisk**| Manuell formulering av prompts for hver spørring.       | Automatisert prosess for henting og generering.       |
| **Kontroll**            | Gir mer kontroll over hentingsprosessen.                 | Strømlinjeformer og automatiserer henting og generering.|
| **Fleksibilitet**        | Tillater tilpassede prompts basert på spesifikke behov. | Mer effektiv for store implementasjoner.              |
| **Kompleksitet**         | Krever utforming og justering av prompts.                | Enklere å integrere i AI-agentens arkitektur.         |

### Praktiske eksempler

**Eksempel på prompting-teknikk:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Eksempel på verktøy:**

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

### Evaluering av relevans

Evaluering av relevans er et avgjørende aspekt ved ytelsen til AI-agenter. Det sikrer at informasjonen som hentes og genereres av agenten er hensiktsmessig, nøyaktig og nyttig for brukeren. La oss utforske hvordan man evaluerer relevans i AI-agenter, inkludert praktiske eksempler og teknikker.

#### Nøkkelbegreper i evaluering av relevans

1. **Kontekstbevissthet**:
   - Agenten må forstå konteksten til brukerens forespørsel for å hente og generere relevant informasjon.
   - Eksempel: Hvis en bruker spør om "beste restauranter i Paris," bør agenten vurdere brukerens preferanser som kjøkkentype og budsjett.

2. **Nøyaktighet**:
   - Informasjonen som gis av agenten bør være faktuelt korrekt og oppdatert.
   - Eksempel: Anbefale restauranter som er åpne nå og har gode omtaler, i stedet for utdaterte eller lukkede alternativer.

3. **Brukerens intensjon**:
   - Agenten bør avlede intensjonen bak brukerens spørring for å gi den mest relevante informasjonen.
   - Eksempel: Hvis en bruker spør om "budsjettvennlige hoteller," bør agenten prioritere rimelige alternativer.

4. **Tilbakemeldingssløyfe**:
   - Kontinuerlig innsamling og analyse av brukerfeedback hjelper agenten med å forbedre sin evaluering av relevans.
   - Eksempel: Inkludere brukerbedømmelser og feedback på tidligere anbefalinger for å forbedre fremtidige svar.

#### Praktiske teknikker for evaluering av relevans

1. **Relevansscore**:
   - Tilordne en relevansscore til hvert hentet element basert på hvor godt det matcher brukerens forespørsel og preferanser.
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

2. **Filtrering og rangering**:
   - Filtrer ut irrelevante elementer og ranger de gjenværende basert på relevansscore.
   - Eksempel:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Returner topp 10 relevante elementer
     ```

3. **Naturlig språkprosessering (NLP)**:
   - Bruk NLP-teknikker for å forstå brukerens forespørsel og hente relevant informasjon.
   - Eksempel:

     ```python
     def process_query(query):
         # Bruk NLP for å hente ut nøkkelinformasjon fra brukerens forespørsel
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integrering av brukerfeedback**:
   - Samle brukerfeedback på de anbefalte forslagene og bruke denne til å justere fremtidige evalueringer av relevans.
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

#### Eksempel: Evaluering av relevans i reisebyrå

Her er et praktisk eksempel på hvordan Travel Agent kan evaluere relevansen av reiseanbefalinger:

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
        return ranked_items[:10]  # Returner topp 10 relevante elementer

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

# Eksempel på bruk
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

### Søking med intensjon

Søking med intensjon innebærer å forstå og tolke det underliggende formålet eller målet bak en brukers spørring for å hente og generere den mest relevante og nyttige informasjonen. Denne tilnærmingen går utover bare å matche nøkkelord og fokuserer på å gripe brukerens faktiske behov og kontekst.

#### Nøkkelbegreper i søking med intensjon

1. **Forstå brukerens intensjon**:
   - Brukerens intensjon kan kategoriseres i tre hovedtyper: informasjonsorientert, navigasjonsorientert og transaksjonsorientert.
     - **Informasjonsintensjon**: Brukeren søker informasjon om et tema (f.eks. "Hva er de beste museene i Paris?").
     - **Navigasjonsintensjon**: Brukeren ønsker å navigere til et spesifikt nettsted eller side (f.eks. "Louvre Museums offisielle nettside").
     - **Transaksjonsintensjon**: Brukeren ønsker å utføre en transaksjon, som å bestille en flyreise eller kjøpe noe (f.eks. "Bestill fly til Paris").

2. **Kontekstbevissthet**:
   - Analyse av konteksten i brukerens spørring hjelper med å nøyaktig identifisere intensjonen deres. Dette inkluderer å vurdere tidligere interaksjoner, brukerpreferanser og detaljer i den nåværende spørringen.

3. **Naturlig språkprosessering (NLP)**:
   - NLP-teknikker brukes for å forstå og tolke naturlige språkspørringer fra brukere. Dette inkluderer oppgaver som enhetsgjenkjenning, sentimentanalyse og spørringsparsing.

4. **Personalisering**:
   - Personalisering av søkeresultater basert på brukerens historikk, preferanser og feedback forbedrer relevansen av hentet informasjon.

#### Praktisk eksempel: Søking med intensjon i reisebyrå

La oss bruke Travel Agent som et eksempel for å se hvordan søking med intensjon kan implementeres.

1. **Innsamling av brukerpreferanser**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Forstå brukerens intensjon**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Kontekstbevissthet**


   ```python
   def analyze_context(query, user_history):
       # Kombiner nåværende forespørsel med brukerhistorikk for å forstå kontekst
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Søk og personaliser resultater**

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
       # Eksempel på søkelogikk for informasjonsformål
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Eksempel på søkelogikk for navigasjonsformål
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Eksempel på søkelogikk for transaksjonsformål
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Eksempel på personaliseringslogikk
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Returner topp 10 personaliserte resultater
   ```

5. **Eksempel på bruk**

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

## 4. Generere kode som et verktøy

Kodegenererende agenter bruker AI-modeller til å skrive og kjøre kode, løse komplekse problemer og automatisere oppgaver.

### Kodegenererende agenter

Kodegenererende agenter bruker generative AI-modeller til å skrive og kjøre kode. Disse agentene kan løse komplekse problemer, automatisere oppgaver og gi verdifulle innsikter ved å generere og kjøre kode i ulike programmeringsspråk.

#### Praktiske anvendelser

1. **Automatisk kodegenerering**: Generer kodebiter for spesifikke oppgaver, som dataanalyse, nettskraping eller maskinlæring.
2. **SQL som RAG**: Bruk SQL-spørringer for å hente og manipulere data fra databaser.
3. **Problemløsning**: Lag og kjør kode for å løse spesifikke problemer, som å optimalisere algoritmer eller analysere data.

#### Eksempel: Kodegenererende agent for dataanalyse

Forestill deg at du designer en kodegenererende agent. Slik kan den fungere:

1. **Oppgave**: Analyser et datasett for å identifisere trender og mønstre.
2. **Trinn**:
   - Last inn datasettet i et dataanalyserverktøy.
   - Generer SQL-spørringer for å filtrere og aggregere dataene.
   - Kjør spørringene og hent resultatene.
   - Bruk resultatene til å generere visualiseringer og innsikter.
3. **Nødvendige ressurser**: Tilgang til datasettet, dataanalyserverktøy og SQL-muligheter.
4. **Erfaring**: Bruk tidligere analyseresultater for å forbedre nøyaktighet og relevans i fremtidige analyser.

### Eksempel: Kodegenererende agent for reisebyrå

I dette eksempelet designer vi en kodegenererende agent, Reisebyrå, for å hjelpe brukere med å planlegge reiser ved å generere og kjøre kode. Denne agenten kan håndtere oppgaver som å hente reisealternativer, filtrere resultater og sette sammen en reiserute ved hjelp av generativ AI.

#### Oversikt over kodegenererende agent

1. **Innhente brukerpreferanser**: Samler inn brukerdata som destinasjon, reisedatoer, budsjett og interesser.
2. **Generere kode for datainnhenting**: Genererer kodebiter for å hente data om flyvninger, hoteller og attraksjoner.
3. **Utføre generert kode**: Kjører den genererte koden for å hente oppdatert informasjon.
4. **Generere reiserute**: Kompilerer hentede data til en personlig tilpasset reiseplan.
5. **Justere basert på tilbakemeldinger**: Mottar brukerfeedback og genererer ny kode om nødvendig for å forbedre resultatene.

#### Trinnvis implementering

1. **Innhente brukerpreferanser**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generere kode for datainnhenting**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Eksempel: Generer kode for å søke etter flyreiser basert på brukerpreferanser
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Eksempel: Generer kode for å søke etter hoteller
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Utføre generert kode**

   ```python
   def execute_code(code):
       # Kjør den genererte koden ved hjelp av exec
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

4. **Generere reiserute**

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

5. **Justere basert på tilbakemeldinger**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Juster preferanser basert på brukerens tilbakemelding
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerer og kjør kode med oppdaterte preferanser
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Utnytte miljøbevissthet og resonnement

Basert på skjemaet til tabellen kan man virkelig forbedre spørregenereringsprosessen ved å utnytte miljøbevissthet og resonnement.

Her er et eksempel på hvordan dette kan gjøres:

1. **Forstå skjemaet**: Systemet vil forstå tabellens skjema og bruke denne informasjonen til å forankre spørregenereringen.
2. **Justere basert på tilbakemeldinger**: Systemet vil justere brukerpreferanser basert på tilbakemeldinger og resonnere om hvilke felt i skjemaet som må oppdateres.
3. **Generere og kjøre spørringer**: Systemet vil generere og kjøre spørringer for å hente oppdatert fly- og hotellsdata basert på de nye preferansene.

Her er et oppdatert Python-eksempel som inkluderer disse konseptene:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Juster preferanser basert på brukertilbakemelding
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Resonnement basert på skjema for å justere andre relaterte preferanser
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Egendefinert logikk for å justere preferanser basert på skjema og tilbakemelding
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generer kode for å hente flydata basert på oppdaterte preferanser
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generer kode for å hente hotelldata basert på oppdaterte preferanser
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simuler utførelse av kode og returner mock-data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generer reiserute basert på fly, hoteller og attraksjoner
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Eksempel på skjema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Eksempel på bruk
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Generer på nytt og kjør kode med oppdaterte preferanser
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Forklaring – booking basert på tilbakemeldinger

1. **Skjema-bevissthet**: Ordboken `schema` definerer hvordan preferanser skal justeres basert på tilbakemelding. Den inkluderer felt som `favorites` og `avoid` med tilhørende justeringer.
2. **Juster preferanser (`adjust_based_on_feedback`-metode)**: Denne metoden justerer preferansene basert på brukerfeedback og skjemaet.
3. **Miljøbaserte justeringer (`adjust_based_on_environment`-metode)**: Denne metoden tilpasser justeringene basert på skjema og tilbakemelding.
4. **Generere og kjøre spørringer**: Systemet genererer kode for å hente oppdatert fly- og hotellsdata basert på de justerte preferansene og simulerer kjøringen av disse spørringene.
5. **Generere reiserute**: Systemet lager en oppdatert reiserute basert på nye fly-, hotell- og attraktionsdata.

Ved å gjøre systemet miljøbevisst og legge til resonnement basert på skjemaet, kan det generere mer nøyaktige og relevante spørringer, som fører til bedre reiseanbefalinger og en mer personlig brukeropplevelse.

### Bruke SQL som en Retrieval-Augmented Generation (RAG) teknikk

SQL (Structured Query Language) er et kraftig verktøy for å samhandle med databaser. Når den brukes som del av en Retrieval-Augmented Generation (RAG)-tilnærming, kan SQL hente relevant data fra databaser for å informere og generere svar eller handlinger i AI-agenter. La oss utforske hvordan SQL kan brukes som en RAG-teknikk i konteksten av Reisebyrå.

#### Nøkkelkonsepter

1. **Databaseinteraksjon**:
   - SQL brukes for å spørrre databaser, hente relevant informasjon og manipulere data.
   - Eksempel: Hente flydetaljer, hotellinformasjon og attraksjoner fra en reisedatabase.

2. **Integrasjon med RAG**:
   - SQL-spørringer genereres basert på brukerinput og preferanser.
   - De hentede dataene brukes deretter til å generere personlige anbefalinger eller handlinger.

3. **Dynamisk spørringsgenerering**:
   - AI-agenten genererer dynamiske SQL-spørringer basert på kontekst og brukerbehov.
   - Eksempel: Tilpasse SQL-spørringer for å filtrere resultater basert på budsjett, datoer og interesser.

#### Anvendelser

- **Automatisk kodegenerering**: Generer kodebiter for spesifikke oppgaver.
- **SQL som RAG**: Bruk SQL-spørringer for å manipulere data.
- **Problemløsning**: Lag og kjør kode for å løse problemer.

**Eksempel**:
En dataanalyse-agent:

1. **Oppgave**: Analyser et datasett for å finne trender.
2. **Trinn**:
   - Last inn datasettet.
   - Generer SQL-spørringer for å filtrere data.
   - Kjør spørringer og hent resultater.
   - Generer visualiseringer og innsikter.
3. **Ressurser**: Tilgang til datasett, SQL-muligheter.
4. **Erfaring**: Bruk tidligere resultater for å forbedre fremtidige analyser.

#### Praktisk eksempel: Bruke SQL i Reisebyrå

1. **Innhente brukerpreferanser**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generere SQL-spørringer**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Kjøre SQL-spørringer**

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

4. **Generere anbefalinger**

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

#### Eksempelsql-spørringer

1. **Flyspørring**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Hotellspørring**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Attraksjonsspørring**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Ved å utnytte SQL som en del av Retrieval-Augmented Generation (RAG)-teknikken, kan AI-agenter som Reisebyrå dynamisk hente og bruke relevante data til å gi nøyaktige og personlige anbefalinger.

### Eksempel på metakognisjon

For å demonstrere en implementering av metakognisjon, la oss lage en enkel agent som *reflekterer over sin beslutningsprosess* mens den løser et problem. For dette eksempelet bygger vi et system hvor en agent prøver å optimalisere valget av hotell, men deretter evaluerer sin egen resonnement og justerer strategien når den gjør feil eller suboptimale valg.

Vi vil simulere dette med et grunnleggende eksempel der agenten velger hoteller basert på en kombinasjon av pris og kvalitet, men den vil "reflektere" over sine valg og justere deretter.

#### Slik illustrerer dette metakognisjon:

1. **Første beslutning**: Agenten velger det billigste hotellet, uten å forstå kvalitetens påvirkning.
2. **Refleksjon og evaluering**: Etter første valg sjekker agenten om hotellet var et "dårlig" valg basert på tilbakemeldinger fra brukeren. Hvis den finner at kvaliteten var for lav, reflekterer den over resonnementet sitt.
3. **Strategijustering**: Agenten justerer strategien basert på sin refleksjon og bytter fra "billigst" til "høyest_kvalitet", og forbedrer beslutningsprosessen for fremtidige iterasjoner.

Her er et eksempel:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Lagrer hotellene som ble valgt tidligere
        self.corrected_choices = []  # Lagrer de korrigerte valgene
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Tilgjengelige strategier

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
        # La oss anta at vi har tilbakemelding fra brukeren som forteller oss om det siste valget var bra eller ikke
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Juster strategi hvis det forrige valget var utilfredsstillende
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

# Lag en agent
agent = HotelRecommendationAgent()

# Steg 1: Agenten anbefaler et hotell ved hjelp av strategien "billigst"
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Steg 2: Agenten reflekterer over valget og justerer strategien om nødvendig
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Steg 3: Agenten anbefaler igjen, denne gangen med den justerte strategien
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Agenters metakognitive evner

Nøkkelen her er agentens evne til å:
- Evaluere tidligere valg og beslutningsprosesser.
- Justere strategi basert på denne refleksjonen, altså metakognisjon i praksis.

Dette er en enkel form for metakognisjon hvor systemet kan justere resonnementet sitt basert på intern feedback.

### Konklusjon

Metakognisjon er et kraftfullt verktøy som kan forbedre egenskapene til AI-agenter betydelig. Ved å inkorporere metakognitive prosesser kan du designe agenter som er mer intelligente, tilpasningsdyktige og effektive. Bruk de ekstra ressursene for å utforske den fascinerende verdenen av metakognisjon i AI-agenter videre.

### Har du flere spørsmål om Metakognisjon som designmønster?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på dine spørsmål om AI-agenter.

## Forrige leksjon

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Neste leksjon

[AI Agents in Production](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->