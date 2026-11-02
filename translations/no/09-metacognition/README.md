[![Multi-Agent Design](../../../translated_images/no/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Klikk på bildet over for å se video av denne leksjonen)_
# Metakognisjon i AI-agenter

## Introduksjon

Velkommen til leksjonen om metakognisjon i AI-agenter! Dette kapitlet er laget for nybegynnere som er nysgjerrige på hvordan AI-agenter kan reflektere over sine egne tenkeprosesser. Ved slutten av denne leksjonen vil du forstå nøkkelbegreper og være utstyrt med praktiske eksempler for å anvende metakognisjon i design av AI-agenter.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du kunne:

1. Forstå konsekvensene av resonnementssløyfer i agentdefinisjoner.
2. Bruke planleggings- og evalueringsmetoder for å hjelpe selvkorrigerende agenter.
3. Lage dine egne agenter som kan manipulere kode for å utføre oppgaver.

## Introduksjon til metakognisjon

Metakognisjon refererer til høyere ordens kognitive prosesser som involverer å tenke på egen tenkning. For AI-agenter betyr dette å kunne evaluere og justere sine handlinger basert på selvbevissthet og tidligere erfaringer. Metakognisjon, eller "å tenke på tenkning", er et viktig konsept i utviklingen av agentiske AI-systemer. Det innebærer at AI-systemer er bevisste på sine egne interne prosesser og kan overvåke, regulere og tilpasse sin atferd deretter. Akkurat som vi gjør når vi leser rommet eller gransker et problem. Denne selvbevisstheten kan hjelpe AI-systemer å ta bedre beslutninger, identifisere feil, og forbedre ytelsen over tid – som igjen knytter seg til Turing-testen og debatten om hvorvidt AI vil ta over.

I sammenheng med agentiske AI-systemer kan metakognisjon hjelpe med flere utfordringer, slik som:
- Transparens: Sikre at AI-systemer kan forklare sin resonnement og beslutninger.
- Resonnering: Forbedre evnen til AI-systemer til å syntetisere informasjon og ta gode beslutninger.
- Tilpasning: La AI-systemer justere seg til nye miljøer og endrede forhold.
- Persepsjon: Forbedre nøyaktigheten av AI-systemer i å gjenkjenne og tolke data fra sitt miljø.

### Hva er metakognisjon?

Metakognisjon, eller "å tenke på tenkning", er en kognitiv prosess på høyere nivå som involverer selvbevissthet og selvregulering av egne kognitive prosesser. Innen AI gir metakognisjon agenter mulighet til å evaluere og tilpasse sine strategier og handlinger, noe som fører til bedre problemløsning og beslutningsevner. Ved å forstå metakognisjon kan du designe AI-agenter som ikke bare er mer intelligente, men også mer tilpasningsdyktige og effektive. I ekte metakognisjon vil du se at AI eksplisitt resonnerer rundt sitt eget resonnement.

Eksempel: "Jeg prioriterte billigere fly fordi… jeg kan gå glipp av direkteflyvninger, så jeg sjekker på nytt."
Holde oversikt over hvordan eller hvorfor den valgte en bestemt rute.
- Noterer at den gjorde feil fordi den stolte for mye på brukerpreferanser fra forrige gang, så den endrer sin beslutningsstrategi, ikke bare den endelige anbefalingen.
- Diagnostiserer mønstre som, "Når jeg ser at brukeren nevner 'for folksomt', bør jeg ikke bare fjerne visse attraksjoner, men også reflektere over at min metode for å velge 'top attraksjoner' er feil hvis jeg alltid rangerer etter popularitet."

### Viktigheten av metakognisjon i AI-agenter

Metakognisjon spiller en avgjørende rolle i design av AI-agenter av flere grunner:

![Viktigheten av metakognisjon](../../../translated_images/no/importance-of-metacognition.b381afe9aae352f7.webp)

- Selvrefleksjon: Agenter kan vurdere egen ytelse og identifisere forbedringsområder.
- Tilpasningsevne: Agenter kan endre sine strategier basert på tidligere erfaringer og skiftende miljøer.
- Feilretting: Agenter kan oppdage og rette feil autonomt, noe som gir mer nøyaktige resultater.
- Ressursforvaltning: Agenter kan optimalisere bruken av ressurser, som tid og datakraft, ved å planlegge og evaluere sine handlinger.

## Komponenter i en AI-agent

Før vi dykker ned i metakognitive prosesser, er det viktig å forstå de grunnleggende komponentene i en AI-agent. En AI-agent består typisk av:

- Persona: Agentens personlighet og karakteristikker, som definerer hvordan den samhandler med brukere.
- Verktøy: Kapasiteter og funksjoner agenten kan utføre.
- Ferdigheter: Kunnskapen og ekspertisen agenten besitter.

Disse komponentene jobber sammen for å skape en "ekspertiseenhet" som kan utføre spesifikke oppgaver.

**Eksempel**:
Tenk på en reiseagent, et agentsystem som ikke bare planlegger ferien din, men også justerer ruten basert på sanntidsdata og tidligere kundereiseerfaringer.

### Eksempel: Metakognisjon i en reiseagenttjeneste

Forestill deg at du designer en AI-drevet reiseagenttjeneste. Denne agenten, "Reiseagent", hjelper brukere med å planlegge ferier. For å inkorporere metakognisjon må Reiseagent evaluere og justere sine handlinger basert på selvbevissthet og tidligere erfaringer. Slik kan metakognisjon spille en rolle:

#### Nåværende oppgave

Den nåværende oppgaven er å hjelpe en bruker med å planlegge en tur til Paris.

#### Steg for å fullføre oppgaven

1. **Innhente brukerpreferanser**: Spør brukeren om reisedatoer, budsjett, interesser (f.eks. museer, mat, shopping) og eventuelle spesifikke krav.
2. **Hente informasjon**: Søk etter flyalternativer, overnatting, attraksjoner og restauranter som matcher brukerens preferanser.
3. **Generere anbefalinger**: Gi en personlig reiserute med flydetaljer, hotellreservasjoner og foreslåtte aktiviteter.
4. **Justere basert på tilbakemeldinger**: Be brukeren om tilbakemelding på anbefalingene og gjør nødvendige justeringer.

#### Nødvendige ressurser

- Tilgang til databaser for fly- og hotellbestillinger.
- Informasjon om attraksjoner og restauranter i Paris.
- Brukertilbakemeldingsdata fra tidligere interaksjoner.

#### Erfaring og selvrefleksjon

Reiseagent bruker metakognisjon for å evaluere sin egen ytelse og lære av tidligere erfaringer. For eksempel:

1. **Analysere brukertilbakemeldinger**: Reiseagent gjennomgår tilbakemeldinger for å avgjøre hvilke anbefalinger som ble godt mottatt og hvilke som ikke ble det. Den justerer fremtidige forslag deretter.
2. **Tilpasningsevne**: Hvis en bruker tidligere har nevnt misnøye med trange steder, vil Reiseagent unngå å anbefale populære turiststeder i rushtiden i framtiden.
3. **Feilretting**: Hvis Reiseagent gjorde en feil ved forrige booking, for eksempel foreslo et hotell som var fullt, lærer den å sjekke tilgjengeligheten grundigere før anbefalinger.

#### Praktisk utvikler-eksempel

Her er et forenklet eksempel på hvordan Reiseagents kode kan se ut når metakognisjon er innarbeidet:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Søk etter flyreiser, hoteller og attraksjoner basert på preferanser
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

- **Selvrefleksjon**: Agenter kan analysere egen ytelse og identifisere forbedringsområder.
- **Tilpasningsevne**: Agenter kan endre strategier basert på tilbakemeldinger og endrede forhold.
- **Feilretting**: Agenter kan oppdage og rette feil på egen hånd.
- **Ressursforvaltning**: Agenter kan optimalisere ressursbruk, som tid og datakraft.

Ved å inkorporere metakognisjon kan Reiseagent gi mer personlige og nøyaktige reiseanbefalinger, noe som forbedrer brukeropplevelsen.

---

## 2. Planlegging i agenter

Planlegging er en kritisk komponent i AI-agenters oppførsel. Det innebærer å skissere trinnene som trengs for å oppnå et mål, med tanke på nåværende tilstand, ressurser og mulige hindringer.

### Elementer i planlegging

- **Nåværende oppgave**: Definer oppgaven tydelig.
- **Trinn for å fullføre oppgaven**: Del opp oppgaven i håndterbare trinn.
- **Nødvendige ressurser**: Identifiser nødvendige ressurser.
- **Erfaring**: Bruk tidligere erfaringer for å informere planleggingen.

**Eksempel**:
Her er trinnene Reiseagent må ta for å hjelpe en bruker med å planlegge turen effektivt:

### Trinn for Reiseagent

1. **Innhente brukerpreferanser**
   - Spør brukeren om detaljer om reisedatoer, budsjett, interesser og eventuelle spesifikke krav.
   - Eksempler: "Når planlegger du å reise?" "Hva er ditt budsjett?" "Hvilke aktiviteter liker du på ferie?"

2. **Hente informasjon**
   - Søk etter relevante reisevalg basert på brukerpreferanser.
   - **Flyvninger**: Finn tilgjengelige fly innenfor brukerens budsjett og foretrukne reisedatoer.
   - **Overnatting**: Finn hoteller eller leieboliger som matcher brukerens preferanser for beliggenhet, pris og fasiliteter.
   - **Attraksjoner og restauranter**: Identifiser populære attraksjoner, aktiviteter og spisesteder som stemmer overens med brukerens interesser.

3. **Generere anbefalinger**
   - Sett sammen den innhentede informasjonen til en personlig reiserute.
   - Gi detaljer som flyalternativer, hotellreservasjoner og foreslåtte aktiviteter, og tilpass anbefalingene til brukerens preferanser.

4. **Presentere reiseruten til brukeren**
   - Del den foreslåtte reiseruten med brukeren for gjennomgang.
   - Eksempel: "Her er et forslag til reiserute for turen din til Paris. Den inkluderer flydetaljer, hotellreservasjoner og en liste over anbefalte aktiviteter og restauranter. Gi meg beskjed om hva du synes!"

5. **Samle tilbakemeldinger**
   - Be brukeren om tilbakemeldinger på den foreslåtte reiseruten.
   - Eksempler: "Liker du flyalternativene?" "Er hotellet passende for dine behov?" "Er det noen aktiviteter du vil legge til eller fjerne?"

6. **Justere basert på tilbakemeldinger**
   - Endre reiseruten basert på brukerens tilbakemeldinger.
   - Foreta nødvendige endringer i fly-, overnattings- og aktivitetsanbefalinger for bedre å møte brukerens preferanser.

7. **Endelig bekreftelse**
   - Presenter den oppdaterte reiseruten til brukeren for endelig godkjenning.
   - Eksempel: "Jeg har gjort justeringene basert på dine tilbakemeldinger. Her er den oppdaterte reiseruten. Ser alt greit ut for deg?"

8. **Bestille og bekrefte reservasjoner**
   - Når brukeren godkjenner reiseruten, fortsett med å bestille fly, overnatting og eventuelle forhåndsplanlagte aktiviteter.
   - Send bekreftelsesdetaljer til brukeren.

9. **Gi løpende støtte**
   - Vær tilgjengelig for å hjelpe brukeren med eventuelle endringer eller ekstra forespørsler før og under reisen.
   - Eksempel: "Hvis du trenger mer hjelp under reisen, er det bare å kontakte meg når som helst!"

### Eksempelinteraksjon

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

# Eksempel på bruk i en bookingforespørsel
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

La oss først begynne med å forstå forskjellen mellom RAG-verktøy og Pre-emptive Context Load

![RAG vs Context Loading](../../../translated_images/no/rag-vs-context.9eae588520c00921.webp)

### Retrieval-Augmented Generation (RAG)

RAG kombinerer et hentingssystem med en generativ modell. Når et spørsmål stilles, henter hentingssystemet relevante dokumenter eller data fra en ekstern kilde, og denne informasjonen brukes til å berike inngangen til den generative modellen. Dette hjelper modellen med å generere mer nøyaktige og kontekstrelevante svar.

I et RAG-system henter agenten relevant informasjon fra en kunnskapsbase og bruker denne til å generere passende svar eller handlinger.

### Korrigerende RAG-tilnærming

Den korrigerende RAG-tilnærmingen fokuserer på å bruke RAG-teknikker for å rette opp feil og forbedre nøyaktigheten til AI-agenter. Dette innebærer:

1. **Prompting-teknikk**: Bruke spesifikke prompts for å veilede agenten i å hente relevant informasjon.
2. **Verktøy**: Implementere algoritmer og mekanismer som gjør det mulig for agenten å evaluere relevansen av hentet informasjon og generere nøyaktige svar.
3. **Evaluering**: Kontinuerlig vurdere agentens ytelse og gjøre justeringer for å forbedre nøyaktighet og effektivitet.

#### Eksempel: Korrigerende RAG i en søkeagent

Tenk på en søkeagent som henter informasjon fra nettet for å svare på brukerforespørsler. Den korrigerende RAG-tilnærmingen kan innebære:

1. **Prompting-teknikk**: Formulere søkespørringer basert på brukerens innspill.
2. **Verktøy**: Bruke naturlig språkprosessering og maskinlæringsalgoritmer for å rangere og filtrere søkeresultater.
3. **Evaluering**: Analysere brukertilbakemeldinger for å identifisere og korrigere unøyaktigheter i hentet informasjon.

### Korrigerende RAG i Reiseagent

Korrigerende RAG (Retrieval-Augmented Generation) forbedrer en AIs evne til å hente og generere informasjon samtidig som den retter opp eventuelle unøyaktigheter. La oss se hvordan Reiseagent kan bruke den korrigerende RAG-tilnærmingen for å gi mer presise og relevante reiseanbefalinger.

Dette innebærer:

- **Prompting-teknikk:** Bruke spesifikke prompts for å veilede agenten i å hente relevant informasjon.
- **Verktøy:** Implementere algoritmer og mekanismer som gjør det mulig for agenten å evaluere relevansen av hentet informasjon og generere nøyaktige svar.
- **Evaluering:** Kontinuerlig å vurdere agentens ytelse og tilpasse for å forbedre nøyaktighet og effektivitet.

#### Trinn for implementering av korrigerende RAG i Reiseagent

1. **Innledende brukerinteraksjon**
   - Reiseagent henter innledende preferanser fra brukeren, som reisemål, reisedatoer, budsjett og interesser.
   - Eksempel:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Informasjonshenting**
   - Reiseagent henter informasjon om fly, overnatting, attraksjoner og restauranter basert på brukerpreferanser.
   - Eksempel:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generering av initiale anbefalinger**
   - Reiseagent bruker hentet informasjon for å lage en personlig reiserute.
   - Eksempel:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Innhenting av brukertilbakemeldinger**
   - Reiseagent ber brukeren om tilbakemeldinger på de første anbefalingene.
   - Eksempel:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Korrigerende RAG-prosess**
   - **Prompting-teknikk**: Reiseagent formulerer nye søkespørringer basert på brukertilbakemeldinger.
     - Eksempel:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Verktøy**: Reiseagent bruker algoritmer for å rangere og filtrere nye søkeresultater, med fokus på relevans basert på tilbakemeldingene.
     - Eksempel:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Evaluering**: Reiseagent vurderer kontinuerlig relevans og nøyaktighet i sine anbefalinger ved å analysere brukertilbakemeldinger og gjøre nødvendige justeringer.
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

Her er et forenklet Python-kodeeksempel som inkorporerer korrigerende RAG-tilnærming i Reiseagent:

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

### Pre-emptive Context Load


Forhåndslasting av kontekst innebærer å laste relevant kontekst eller bakgrunnsinformasjon inn i modellen før den behandler en forespørsel. Dette betyr at modellen har tilgang til denne informasjonen fra starten av, noe som kan hjelpe den med å generere mer informerte svar uten å måtte hente ekstra data under prosessen.

Her er et forenklet eksempel på hvordan en forhåndslasting av kontekst kan se ut for en reisebyråapplikasjon i Python:

```python
class TravelAgent:
    def __init__(self):
        # Forbelast populære destinasjoner og deres informasjon
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

1. **Initialisering (`__init__`-metode)**: `TravelAgent`-klassen forhåndslaster en ordbok som inneholder informasjon om populære destinasjoner som Paris, Tokyo, New York og Sydney. Denne ordboken inkluderer detaljer som land, valuta, språk og viktige attraksjoner for hver destinasjon.

2. **Henting av informasjon (`get_destination_info`-metode)**: Når en bruker stiller spørsmål om en spesifikk destinasjon, henter `get_destination_info`-metoden relevant informasjon fra den forhåndslastede kontekstordboken.

Ved å forhåndslaste konteksten kan reisebyråapplikasjonen raskt svare på brukerforespørsler uten å måtte hente denne informasjonen fra en ekstern kilde i sanntid. Dette gjør applikasjonen mer effektiv og responsiv.

### Starte Planlegging med et Mål Før Iterasjon

Å starte en plan med et mål innebærer å begynne med en klar hensikt eller ønsket resultat i tankene. Ved å definere dette målet på forhånd kan modellen bruke det som en ledende prinsipp gjennom hele den iterative prosessen. Dette hjelper med å sikre at hver iterasjon beveger seg nærmere det ønskede resultatet, noe som gjør prosessen mer effektiv og fokusert.

Her er et eksempel på hvordan du kan starte en reiseplan med et mål før du itererer for en reisebyråapplikasjon i Python:

### Scenario

Et reisebyrå ønsker å planlegge en skreddersydd ferie for en kunde. Målet er å lage en reiseplan som maksimerer kundens tilfredshet basert på deres preferanser og budsjett.

### Trinn

1. Definer kundens preferanser og budsjett.
2. Start den innledende planen basert på disse preferansene.
3. Iterer for å forbedre planen, optimaliser for kundens tilfredshet.

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

#### Kodeforklaring

1. **Initialisering (`__init__`-metode)**: `TravelAgent`-klassen initialiseres med en liste over potensielle destinasjoner, hver med attributter som navn, kostnad og aktivitetstype.

2. **Starte Planleggingen (`bootstrap_plan`-metode)**: Denne metoden lager en innledende reiseplan basert på kundens preferanser og budsjett. Den går gjennom listen over destinasjoner og legger dem til planen hvis de matcher kundens preferanser og passer innenfor budsjettet.

3. **Matchende Preferanser (`match_preferences`-metode)**: Denne metoden sjekker om en destinasjon matcher kundens preferanser.

4. **Iterere Planen (`iterate_plan`-metode)**: Denne metoden forbedrer den innledende planen ved å prøve å erstatte hver destinasjon i planen med en bedre match, med hensyn til kundens preferanser og budsjettbegrensninger.

5. **Beregne Kostnad (`calculate_cost`-metode)**: Denne metoden beregner den totale kostnaden for den nåværende planen, inkludert en potensiell ny destinasjon.

#### Eksempel på bruk

- **Innledende Plan**: Reisebyrået lager en innledende plan basert på kundens preferanser for sightseeing og et budsjett på $2000.
- **Forbedret Plan**: Reisebyrået itererer planen for å optimalisere for kundens preferanser og budsjett.

Ved å starte planen med et klart mål (f.eks. å maksimere kundetilfredshet) og iterere for å forbedre planen, kan reisebyrået lage en skreddersydd og optimalisert reiserute for kunden. Denne tilnærmingen sikrer at reiseplanen samsvarer med kundens preferanser og budsjett fra starten av, og forbedres med hver iterasjon.

### Utnytte LLM for Omrangering og Poengsetting

Store språkmodeller (LLMs) kan brukes til omrangering og poengsetting ved å evaluere relevans og kvalitet på hentede dokumenter eller genererte svar. Slik fungerer det:

**Henting:** Det første hentetrinnet henter et sett med kandidatdokumenter eller svar basert på forespørselen.

**Omrangering:** LLM vurderer disse kandidatene og omrangerer dem basert på relevans og kvalitet. Dette trinnet sikrer at det mest relevante og høykvalitetsinformasjonen presenteres først.

**Poengsetting:** LLM tildeler poeng til hver kandidat som reflekterer deres relevans og kvalitet. Dette hjelper til med å velge det beste svaret eller dokumentet for brukeren.

Ved å utnytte LLM for omrangering og poengsetting, kan systemet gi mer nøyaktig og kontekstuelt relevant informasjon, noe som forbedrer brukeropplevelsen.

Her er et eksempel på hvordan et reisebyrå kan bruke en stor språkmodell (LLM) for omrangering og poengsetting av reisemål basert på brukerpreferanser i Python:

#### Scenario — Reise basert på preferanser

Et reisebyrå ønsker å anbefale de beste reisemålene til en kunde basert på deres preferanser. LLM vil hjelpe til med å omrangere og poengsette destinasjonene for å sikre at de mest relevante alternativene presenteres.

#### Trinn:

1. Samle inn brukerens preferanser.
2. Hent en liste med potensielle reisemål.
3. Bruk LLM for å omrangere og poengsette destinasjonene basert på brukerpreferansene.

Slik kan du oppdatere det tidligere eksemplet for å bruke Azure OpenAI-tjenester:

#### Krav

1. Du må ha et Azure-abonnement.
2. Opprett en Azure OpenAI-ressurs og få API-nøkkelen din.

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
        
        # Kall Azure OpenAI API for å få de om-rangerte og scorede destinasjonene
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Ekstraher og returner anbefalingene
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

#### Kodeforklaring – Preference Booker

1. **Initialisering**: `TravelAgent`-klassen initialiseres med en liste over potensielle reisemål, hvor hvert har attributter som navn og beskrivelse.

2. **Få anbefalinger (`get_recommendations`-metode)**: Denne metoden genererer en prompt for Azure OpenAI-tjenesten basert på brukerens preferanser og gjør en HTTP POST-forespørsel til Azure OpenAI API for å få omrangert og poengsatte destinasjoner.

3. **Generere Prompt (`generate_prompt`-metode)**: Denne metoden bygger en prompt til Azure OpenAI, inkludert brukerens preferanser og listen over destinasjoner. Prompten guider modellen til å omrangere og poengsette destinasjonene basert på de oppgitte preferansene.

4. **API-kall**: `requests`-biblioteket brukes til å gjøre en HTTP POST-forespørsel til Azure OpenAI API-endepunktet. Svaret inneholder de omrangede og poengsatte destinasjonene.

5. **Eksempel på bruk**: Reisebyrået samler inn brukerpreferanser (for eksempel interesse for sightseeing og mangfoldig kultur) og bruker Azure OpenAI-tjenesten for å få omrangert og poengsatte anbefalinger for reisemål.

Husk å bytte ut `your_azure_openai_api_key` med din faktiske Azure OpenAI API-nøkkel og `https://your-endpoint.com/...` med den faktiske endepunktadressen for din Azure OpenAI-distribusjon.

Ved å utnytte LLM for omrangering og poengsetting kan reisebyrået tilby mer personaliserte og relevante reiseanbefalinger til klientene, og dermed forbedre deres totale opplevelse.

### RAG: Prompting-teknikk vs Verktøy

Retrieval-Augmented Generation (RAG) kan være både en prompting-teknikk og et verktøy i utviklingen av AI-agenter. Å forstå forskjellen mellom de to kan hjelpe deg med å utnytte RAG mer effektivt i dine prosjekter.

#### RAG som en Prompting-teknikk

**Hva er det?**

- Som en prompting-teknikk innebærer RAG å formulere spesifikke forespørsler eller prompts for å styre innhentingen av relevant informasjon fra en stor korpus eller database. Denne informasjonen brukes deretter til å generere svar eller handlinger.

**Hvordan det fungerer:**

1. **Formulere Prompter**: Lag godt strukturerte prompts eller forespørsler basert på oppgaven eller brukerens input.
2. **Hent Informasjon**: Bruk promptene til å søke etter relevant data fra en forhåndseksisterende kunnskapsbase eller datasett.
3. **Generere Svar**: Kombiner den hentede informasjonen med generative AI-modeller for å produsere et omfattende og sammenhengende svar.

**Eksempel i Reisebyrå**:

- Brukerinput: "Jeg vil besøke museer i Paris."
- Prompt: "Finn toppmuseer i Paris."
- Hentet informasjon: Detaljer om Louvre Museum, Musée d'Orsay, osv.
- Generert svar: "Her er noen av de beste museene i Paris: Louvre Museum, Musée d'Orsay og Centre Pompidou."

#### RAG som Verktøy

**Hva er det?**

- Som et verktøy er RAG et integrert system som automatiserer hente- og genereringsprosessen, noe som gjør det enklere for utviklere å implementere komplekse AI-funksjoner uten å manuelt lage prompts for hver forespørsel.

**Hvordan det fungerer:**

1. **Integrasjon**: Inkluder RAG i AI-agentens arkitektur, slik at den automatisk kan håndtere hente- og genereringsoppgaver.
2. **Automatisering**: Verktøyet håndterer hele prosessen, fra mottak av brukerinput til generering av sluttsvar, uten å kreve eksplisitte prompts for hvert trinn.
3. **Effektivitet**: Forbedrer agentens ytelse ved å strømlinjeforme hente- og genereringsprosessen, noe som muliggjør raskere og mer nøyaktige svar.

**Eksempel i Reisebyrå**:

- Brukerinput: "Jeg vil besøke museer i Paris."
- RAG-verktøy: Henter automatisk informasjon om museer og genererer et svar.
- Generert svar: "Her er noen av de beste museene i Paris: Louvre Museum, Musée d'Orsay og Centre Pompidou."

### Sammenligning

| Aspekt                 | Prompting-teknikk                                          | Verktøy                                              |
|------------------------|------------------------------------------------------------|------------------------------------------------------|
| **Manuell vs Automatisk**| Manuell formulering av prompts for hver forespørsel.       | Automatisert prosess for innhenting og generering.   |
| **Kontroll**            | Gir mer kontroll over henteprosessen.                       | Strømlinjeformer og automatiserer hente- og genereringsprosessen. |
| **Fleksibilitet**       | Muliggjør tilpassede prompts basert på spesifikke behov.   | Mer effektivt for storskala implementeringer.        |
| **Kompleksitet**         | Krever å utforme og justere prompts.                        | Enklere å integrere i en AI-agents arkitektur.       |

### Praktiske Eksempler

**Eksempel på Prompting-teknikk:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Eksempel på Verktøy:**

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

### Evaluering av Relevans

Evaluering av relevans er et avgjørende aspekt ved AI-agenters ytelse. Det sikrer at informasjonen som hentes og genereres av agenten er passende, korrekt og nyttig for brukeren. La oss utforske hvordan man kan evaluere relevans i AI-agenter, inkludert praktiske eksempler og teknikker.

#### Nøkkelkonsepter i Evaluering av Relevans

1. **Kontekstbevissthet**:
   - Agenten må forstå konteksten for brukerens forespørsel for å hente og generere relevant informasjon.
   - Eksempel: Hvis en bruker spør om "beste restauranter i Paris," bør agenten ta hensyn til brukerens preferanser, som kjøkkenstil og budsjett.

2. **Nøyaktighet**:
   - Informasjonen som agenten gir bør være faktuelt korrekt og oppdatert.
   - Eksempel: Anbefale restauranter som er åpne nå med gode anmeldelser i stedet for utdaterte eller stengte alternativer.

3. **Brukerintensjon**:
   - Agenten bør utlede brukerens intensjon bak forespørselen for å gi den mest relevante informasjonen.
   - Eksempel: Hvis en bruker spør om "budsjettvennlige hoteller," bør agenten prioritere rimelige alternativer.

4. **Tilbakemeldingssløyfe**:
   - Kontinuerlig innsamling og analyse av brukerfeedback hjelper agenten med å forbedre relevanseevalueringen.
   - Eksempel: Inkludere brukervurderinger og tilbakemeldinger på tidligere anbefalinger for å forbedre fremtidige svar.

#### Praktiske teknikker for å evaluere relevans

1. **Relevanspoengsetting**:
   - Gi en relevanspoengsum til hvert hentet element basert på hvor godt det matcher brukerens forespørsel og preferanser.
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
   - Filtrer ut irrelevante elementer og ranger de gjenværende basert på relevanspoengsummene.
   - Eksempel:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Returner topp 10 relevante elementer
     ```

3. **Naturlig språkbehandling (NLP)**:
   - Bruk NLP-teknikker for å forstå brukerens forespørsel og hente relevant informasjon.
   - Eksempel:

     ```python
     def process_query(query):
         # Bruk NLP for å hente ut nøkkelinformasjon fra brukerens forespørsel
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integrering av brukerfeedback**:
   - Samle brukerfeedback på de foreslåtte anbefalingene og bruk dette til å justere fremtidige relevansvurderinger.
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

#### Eksempel: Evaluere relevans i Reisebyrå

Her er et praktisk eksempel på hvordan Reisebyrå kan evaluere relevansen av reiseanbefalinger:

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
        return ranked_items[:10]  # Returner de 10 mest relevante elementene

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

### Søking med Intensjon

Søking med intensjon innebærer å forstå og tolke det underliggende formålet eller målet bak en brukers forespørsel for å hente og generere den mest relevante og nyttige informasjonen. Denne tilnærmingen går utover bare å matche nøkkelord og fokuserer på å fatte brukerens faktiske behov og kontekst.

#### Nøkkelkonsepter i Søking med Intensjon

1. **Forstå brukerintensjon**:
   - Brukerintensjon kan kategoriseres i tre hovedtyper: informasjons-, navigasjons- og transaksjonsintensjon.
     - **Informasjonsintensjon**: Brukeren søker informasjon om et tema (f.eks. "Hva er de beste museene i Paris?").
     - **Navigasjonsintensjon**: Brukeren ønsker å navigere til en bestemt nettside eller side (f.eks. "Louvre Museums offisielle nettside").
     - **Transaksjonsintensjon**: Brukeren ønsker å utføre en transaksjon, som å bestille en flyreise eller kjøpe noe (f.eks. "Bestill en flybillett til Paris").

2. **Kontekstbevissthet**:
   - Analyse av konteksten i brukerens forespørsel hjelper til med å identifisere intensjonen nøyaktig. Dette inkluderer tidligere interaksjoner, brukerpreferanser og detaljer i den aktuelle forespørselen.

3. **Naturlig språkbehandling (NLP)**:
   - NLP-teknikker brukes for å forstå og tolke de naturlige språklige forespørslene fra brukerne. Dette inkluderer oppgaver som entitetsgjenkjenning, sentimentanalyse og spørringsparsing.

4. **Personalisering**:
   - Å tilpasse søkeresultatene basert på brukerens historikk, preferanser og tilbakemeldinger forbedrer relevansen av informasjonen som hentes.

#### Praktisk eksempel: Søking med intensjon i Reisebyrå

La oss ta Reisebyrå som et eksempel for å se hvordan søking med intensjon kan implementeres.

1. **Samle inn brukerpreferanser**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Forstå brukerintensjon**

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
       # Kombiner nåværende forespørsel med brukerhistorikk for å forstå konteksten
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Søk og personliggjør resultater**

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
       # Eksempel på søkelogikk for informasjonsintensjon
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Eksempel på søkelogikk for navigasjonsintensjon
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Eksempel på søkelogikk for transaksjonsintensjon
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

1. **Automatisk kodegenerering**: Generer kodestumper for spesifikke oppgaver, som dataanalyse, webskraping eller maskinlæring.
2. **SQL som en RAG**: Bruk SQL-spørringer for å hente og manipulere data fra databaser.
3. **Problemløsning**: Lag og kjør kode for å løse spesifikke problemer, som å optimalisere algoritmer eller analysere data.

#### Eksempel: Kodegenererende agent for dataanalyse

Tenk deg at du designer en kodegenererende agent. Slik kan den fungere:

1. **Oppgave**: Analyser et datasett for å identifisere trender og mønstre.
2. **Steg**:
   - Last inn datasettet i et dataanalyseverktøy.
   - Generer SQL-spørringer for å filtrere og aggregere dataene.
   - Kjør spørringene og hent resultatene.
   - Bruk resultatene til å generere visualiseringer og innsikter.
3. **Nødvendige ressurser**: Tilgang til datasettet, dataanalyseverktøy og SQL-muligheter.
4. **Erfaring**: Bruk tidligere analyseresultater for å forbedre nøyaktigheten og relevansen av fremtidige analyser.

### Eksempel: Kodegenererende agent for reiseagent

I dette eksemplet skal vi designe en kodegenererende agent, Reiseagent, som hjelper brukere med å planlegge reisen ved å generere og kjøre kode. Denne agenten kan håndtere oppgaver som å hente reisevalg, filtrere resultater og sette sammen en reiseplan ved hjelp av generativ AI.

#### Oversikt over kodegenererende agent

1. **Innsamling av brukerpreferanser**: Samler brukerinput som destinasjon, reisedatoer, budsjett og interesser.
2. **Generering av kode for datainnhenting**: Genererer kodestumper for å hente data om flyvninger, hoteller og attraksjoner.
3. **Utføring av generert kode**: Kjører den genererte koden for å hente sanntidsinformasjon.
4. **Generering av reiseplan**: Setter sammen de hentede dataene til en personlig reiseplan.
5. **Justering basert på tilbakemeldinger**: Mottar brukertilbakemeldinger og genererer kode på nytt ved behov for å forbedre resultatene.

#### Trinnvis implementering

1. **Innsamling av brukerpreferanser**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generering av kode for datainnhenting**

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

3. **Utføring av generert kode**

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

4. **Generering av reiseplan**

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

5. **Justering basert på tilbakemeldinger**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Juster preferanser basert på brukerfeedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Generer på nytt og kjør kode med oppdaterte preferanser
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Utnyttelse av miljøbevissthet og resonnement

Basert på skjemaet til tabellen kan dette virkelig forbedre prosessen med spørringsgenerering ved å utnytte miljøbevissthet og resonnement.

Her er et eksempel på hvordan dette kan gjøres:

1. **Forstå skjemaet**: Systemet vil forstå skjemaet i tabellen og bruke denne informasjonen til å grunnfeste spørringsgenereringen.
2. **Justering basert på tilbakemeldinger**: Systemet vil justere brukerpreferanser basert på tilbakemeldinger og resonnere om hvilke felt i skjemaet som må oppdateres.
3. **Generering og utføring av spørringer**: Systemet vil generere og utføre spørringer for å hente oppdaterte fly- og hotellsdata basert på de nye preferansene.

Her er et oppdatert Python-eksempel som inkorporerer disse konseptene:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Juster preferanser basert på brukerfeedback
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
    # Tilpasset logikk for å justere preferanser basert på skjema og tilbakemelding
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

# Regenerer og kjør kode med oppdaterte preferanser
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Forklaring - Booking basert på tilbakemelding

1. **Skjemabevissthet**: `schema`-ordboken definerer hvordan preferanser bør justeres basert på tilbakemelding. Den inkluderer felt som `favorites` og `avoid` med tilhørende justeringer.
2. **Justering av preferanser (`adjust_based_on_feedback` metoden)**: Denne metoden justerer preferanser basert på brukertilbakemeldinger og skjemaet.
3. **Miljøbaserte justeringer (`adjust_based_on_environment` metoden)**: Denne metoden tilpasser justeringene basert på skjemaet og tilbakemeldinger.
4. **Generering og utføring av spørringer**: Systemet genererer kode for å hente oppdaterte fly- og hotellsdata basert på justerte preferanser og simulerer kjøringen av disse spørringene.
5. **Generering av reiseplan**: Systemet lager en oppdatert reiseplan basert på de nye fly-, hotell- og attraksjonsdataene.

Ved å gjøre systemet miljøbevisst og resonnere basert på skjemaet, kan det generere mer nøyaktige og relevante spørringer, noe som fører til bedre reiseanbefalinger og en mer personlig brukeropplevelse.

### Bruke SQL som en Retrival-Augmented Generation (RAG)-teknikk

SQL (Structured Query Language) er et kraftig verktøy for å samhandle med databaser. Når det brukes som del av en Retrieval-Augmented Generation (RAG)-tilnærming, kan SQL hente relevant data fra databaser for å informere og generere svar eller handlinger i AI-agenter. La oss utforske hvordan SQL kan brukes som en RAG-teknikk i sammenheng med Reiseagent.

#### Nøkkelkonsepter

1. **Databaseinteraksjon**:
   - SQL brukes til å spørre databaser, hente relevant informasjon og manipulere data.
   - Eksempel: Hente detaljer om flyvninger, hotellinformasjon og attraksjoner fra en reisedatabase.

2. **Integrasjon med RAG**:
   - SQL-spørringer genereres basert på brukerinput og preferanser.
   - De hentede dataene brukes deretter til å generere personlige anbefalinger eller handlinger.

3. **Dynamisk spørringsgenerering**:
   - AI-agenten genererer dynamiske SQL-spørringer basert på kontekst og brukerbehov.
   - Eksempel: Tilpasse SQL-spørringer for å filtrere resultater basert på budsjett, datoer og interesser.

#### Anvendelser

- **Automatisk kodegenerering**: Generer kodestumper for spesifikke oppgaver.
- **SQL som en RAG**: Bruk SQL-spørringer for å manipulere data.
- **Problemløsning**: Lag og kjør kode for å løse problemer.

**Eksempel**:
En dataanalyseagent:

1. **Oppgave**: Analyser et datasett for å finne trender.
2. **Steg**:
   - Last inn datasettet.
   - Generer SQL-spørringer for å filtrere data.
   - Kjør spørringene og hent resultater.
   - Generer visualiseringer og innsikter.
3. **Ressurser**: Tilgang til datasett, SQL-muligheter.
4. **Erfaring**: Bruk tidligere resultater for å forbedre fremtidige analyser.

#### Praktisk eksempel: Bruke SQL i Reiseagent

1. **Innsamling av brukerpreferanser**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generering av SQL-spørringer**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Utføring av SQL-spørringer**

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

4. **Generering av anbefalinger**

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

#### Eksempel på SQL-spørringer

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

Ved å utnytte SQL som del av Retrieval-Augmented Generation (RAG)-teknikken, kan AI-agenter som Reiseagent dynamisk hente og bruke relevant data for å gi nøyaktige og personlige anbefalinger.

### Eksempel på metakognisjon

For å demonstrere en implementering av metakognisjon, la oss lage en enkel agent som *reflekterer over sin beslutningsprosess* mens den løser et problem. I dette eksemplet bygger vi et system der en agent prøver å optimalisere valget av et hotell, men som deretter evaluerer sitt eget resonnement og justerer strategien når den gjør feil eller suboptimale valg.

Vi skal simulere dette med et grunnleggende eksempel der agenten velger hoteller basert på en kombinasjon av pris og kvalitet, men som "reflekterer" over sine beslutninger og justerer seg deretter.

#### Hvordan dette illustrerer metakognisjon:

1. **Første beslutning**: Agenten velger det billigste hotellet, uten å forstå kvalitetsimplikasjonene.
2. **Refleksjon og evaluering**: Etter det første valget sjekker agenten om hotellet var et "dårlig" valg ved hjelp av brukertilbakemeldinger. Hvis den finner at hotellets kvalitet var for lav, reflekterer den over resonnementet sitt.
3. **Justering av strategi**: Agenten tilpasser strategien basert på refleksjonen og bytter fra "billigst" til "høyest kvalitet", og forbedrer dermed beslutningsprosessen i fremtidige iterasjoner.

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
        # La oss anta at vi har tilbakemeldinger fra brukeren som forteller oss om det siste valget var bra eller ikke
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

# Steg 1: Agenten anbefaler et hotell ved å bruke "billigste" strategi
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Steg 2: Agenten reflekterer over valget og justerer strategien om nødvendig
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Steg 3: Agenten anbefaler igjen, denne gangen ved å bruke den justerte strategien
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Agenters metakognitive evner

Nøkkelen her er agentens evne til å:
- Evaluere sine tidligere valg og beslutningsprosesser.
- Justere sin strategi basert på denne refleksjonen, altså metakognisjon i praksis.

Dette er en enkel form for metakognisjon der systemet er i stand til å justere sin resonnementprosess basert på intern tilbakemelding.

### Konklusjon

Metakognisjon er et kraftfullt verktøy som kan forbedre AI-agenters evner betydelig. Ved å integrere metakognitive prosesser kan du designe agenter som er mer intelligente, tilpasningsdyktige og effektive. Bruk de ekstra ressursene for å utforske den fascinerende verdenen av metakognisjon i AI-agenter videre.

### Har du flere spørsmål om metakognisjonens designmønster?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortimer og få svar på dine spørsmål om AI-agenter.

## Forrige leksjon

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Neste leksjon

[AI Agenter i produksjon](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->