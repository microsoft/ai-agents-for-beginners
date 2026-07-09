[![Multi-Agent Design](../../../translated_images/hr/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Kliknite sliku gore za pogledati video ove lekcije)_
# Metakognicija u AI agentima

## Uvod

Dobrodošli na lekciju o metakogniciji u AI agentima! Ovo poglavlje je namijenjeno početnicima koji su znatiželjni oko toga kako AI agenti mogu razmišljati o vlastitim procesima razmišljanja. Do kraja ove lekcije razumjet ćete ključne pojmove i bit ćete opremljeni praktičnim primjerima za primjenu metakognicije u dizajnu AI agenata.

## Ciljevi učenja

Nakon što završite ovu lekciju, moći ćete:

1. Razumjeti implikacije petlji rezoniranja u definicijama agenata.
2. Koristiti tehnike planiranja i evaluacije za pomoć agentima koji se samopodržavaju i ispravljaju.
3. Kreirati vlastite agente sposobne za manipulaciju kodom kako bi obavljali zadatke.

## Uvod u metakogniciju

Metakognicija se odnosi na kognitivne procese višeg reda koji uključuju razmišljanje o vlastitom razmišljanju. Za AI agente, to znači biti sposoban evaluirati i prilagoditi svoje radnje na temelju samosvijesti i prošlih iskustava. Metakognicija, ili "razmišljanje o razmišljanju," važan je koncept u razvoju agencijskih AI sustava. Ona uključuje IA sustave koji su svjesni vlastitih unutarnjih procesa i koji mogu pratiti, regulirati i prilagoditi svoje ponašanje u skladu s tim. Baš kao što mi to činimo kada "čitamo prostoriju" ili gledamo problem. Ova samosvijest može pomoći AI sustavima donijeti bolje odluke, identificirati pogreške i poboljšati svoju izvedbu tijekom vremena - opet povezujući se s Turingovim testom i raspravom hoće li AI preuzeti kontrolu.

U kontekstu agencijskih AI sustava, metakognicija može pomoći u rješavanju nekoliko izazova, poput:
- Transparentnosti: Osiguravanje da AI sustavi mogu objasniti svoje rezoniranje i odluke.
- Rezoniranja: Poboljšanje sposobnosti AI sustava da sintetiziraju informacije i donose ispravne odluke.
- Prilagodbe: Omogućavanje AI sustavima da se prilagode novim okruženjima i promjenjivim uvjetima.
- Percepcije: Poboljšanje točnosti AI sustava u prepoznavanju i tumačenju podataka iz okoline.

### Što je metakognicija?

Metakognicija, ili "razmišljanje o razmišljanju," je kognitivni proces višeg reda koji uključuje samosvijest i samoregulaciju kognitivnih procesa. U području AI, metakognicija omogućuje agentima evaluaciju i prilagodbu njihovih strategija i radnji, što dovodi do poboljšanih sposobnosti rješavanja problema i donošenja odluka. Razumijevanjem metakognicije možete dizajnirati AI agente koji nisu samo inteligentniji nego i prilagodljiviji i učinkovitiji. U pravoj metakogniciji, AI bi eksplicitno rezonirao o vlastitom rezoniranju.

Primjer: „Prioritizirao sam jeftinije letove zato što... možda propuštam neposredne letove, pa ću ponovno provjeriti.“.
Praćenje načina ili razloga zbog kojeg je odabrao određeni put.
- Bilježenje da je napravio pogreške jer je previše vjerovao korisničkim preferencijama iz prošlog puta, pa mijenja svoju strategiju donošenja odluka, a ne samo konačnu preporuku.
- Dijagnosticiranje obrazaca poput: „Kad god vidim da korisnik spominje ‘previše gužve,’ ne bih samo uklonio određene atrakcije, već bih također razmotrio da je moja metoda odabira ‘najboljih atrakcija’ pogrešna ako uvijek rangiram prema popularnosti.“

### Važnost metakognicije u AI agentima

Metakognicija igra ključnu ulogu u dizajnu AI agenata iz nekoliko razloga:

![Importance of Metacognition](../../../translated_images/hr/importance-of-metacognition.b381afe9aae352f7.webp)

- Samorefleksija: Agenti mogu procijeniti vlastitu izvedbu i identificirati područja za poboljšanje.
- Prilagodljivost: Agenti mogu mijenjati svoje strategije na temelju prošlih iskustava i promjenjivih okruženja.
- Ispravak pogrešaka: Agenti mogu samostalno otkrivati i ispravljati pogreške, što dovodi do točnijih rezultata.
- Upravljanje resursima: Agenti mogu optimizirati korištenje resursa, poput vremena i računalne snage, planiranjem i evaluacijom svojih radnji.

## Komponente AI agenta

Prije nego što zaronimo u metakognitivne procese, važno je razumjeti osnovne komponente AI agenta. AI agent se obično sastoji od:

- Persona: Osobnost i karakteristike agenta, koje definiraju kako komunicira s korisnicima.
- Alati: Sposobnosti i funkcije koje agent može izvršavati.
- Vještine: Znanje i stručnost koju agent posjeduje.

Ove komponente rade zajedno kako bi stvorile "jedinicu ekspertize" koja može izvršavati specifične zadatke.

**Primjer**:
Zamislite putničkog agenta, uslugu agenta koja ne samo da planira vaš odmor nego i prilagođava svoj put temeljem podataka u stvarnom vremenu i prošlih iskustava putnika.

### Primjer: Metakognicija u putničkoj agentskoj usluzi

Zamislite da dizajnirate uslugu putničkog agenta pokretanog AI-em. Ovaj agent, "Putnički Agent," pomaže korisnicima u planiranju njihovih odmora. Da biste uključili metakogniciju, Putnički Agent treba evaluirati i prilagoditi svoje radnje na temelju samosvijesti i prošlih iskustava. Evo kako bi metakognicija mogla igrati ulogu:

#### Trenutni zadatak

Trenutni zadatak je pomoći korisniku da isplanira putovanje u Pariz.

#### Koraci za izvršenje zadatka

1. **Prikupljanje korisničkih preferencija**: Pitati korisnika o njegovim datumima putovanja, budžetu, interesima (npr. muzeji, kuhinja, kupovina) i posebnim zahtjevima.
2. **Prikupljanje informacija**: Pretraživanje opcija leta, smještaja, atrakcija i restorana koji odgovaraju korisničkim preferencijama.
3. **Generiranje preporuka**: Pružanje personaliziranog itinerera sa detaljima o letu, rezervacijama hotela i predloženim aktivnostima.
4. **Prilagodba na temelju povratnih informacija**: Pitati korisnika za povratne informacije o preporukama i napraviti potrebne prilagodbe.

#### Potrebni resursi

- Pristup bazama podataka za rezervaciju letova i hotela.
- Informacije o pariškim atrakcijama i restoranima.
- Podaci s povratnih informacija korisnika iz prethodnih interakcija.

#### Iskustvo i samorefleksija

Putnički Agent koristi metakogniciju za evaluaciju svoje izvedbe i učenje iz prošlih iskustava. Na primjer:

1. **Analiza povratnih informacija korisnika**: Putnički Agent pregledava povratne informacije korisnika da bi odredio koje su preporuke bile dobro prihvaćene, a koje nisu. Prema tome prilagođava buduće prijedloge.
2. **Prilagodljivost**: Ako je korisnik ranije spomenuo da ne voli pretrpane prostore, Putnički Agent će izbjegavati preporučivati popularna turistička mjesta tijekom vršnih sati u budućnosti.
3. **Ispravak pogrešaka**: Ako je Putnički Agent napravio pogrešku u prethodnoj rezervaciji, poput predlaganja hotela koji je bio popunjen, uči kako provjeravati dostupnost strože prije nego što da preporuke.

#### Praktični primjer za programere

Evo pojednostavljenog primjera kako bi kod Putničkog Agenta mogao izgledati pri uključivanju metakognicije:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Pretražujte letove, hotele i atrakcije na temelju preferencija
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
        # Analizirajte povratne informacije i prilagodite buduće preporuke
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Primjer korištenja
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

#### Zašto je metakognicija važna

- **Samorefleksija**: Agenti mogu analizirati svoju izvedbu i identificirati područja za poboljšanje.
- **Prilagodljivost**: Agenti mogu mijenjati strategije na temelju povratnih informacija i promjenjivih uvjeta.
- **Ispravak pogrešaka**: Agenti mogu samostalno otkrivati i ispravljati pogreške.
- **Upravljanje resursima**: Agenti mogu optimizirati korištenje resursa, poput vremena i računalne snage.

Uključivanjem metakognicije, Putnički Agent može pružiti personaliziranije i točnije preporuke za putovanja, čime se poboljšava cjelokupno korisničko iskustvo.

---

## 2. Planiranje u agentima

Planiranje je ključna komponenta ponašanja AI agenata. To uključuje definiranje koraka potrebnih za postizanje cilja, uzimajući u obzir trenutno stanje, resurse i moguće prepreke.

### Elementi planiranja

- **Trenutni zadatak**: Jasno definirajte zadatak.
- **Koraci za izvršenje zadatka**: Razložite zadatak na upravljive korake.
- **Potrebni resursi**: Identificirajte potrebne resurse.
- **Iskustvo**: Iskoristite prethodna iskustva za planiranje.

**Primjer**:
Evo koraka koje Putnički Agent treba poduzeti kako bi učinkovito pomogao korisniku u planiranju njihovog putovanja:

### Koraci za Putničkog Agenta

1. **Prikupljanje korisničkih preferencija**
   - Pitajte korisnika za detalje o datumima putovanja, budžetu, interesima i posebnim zahtjevima.
   - Primjeri: "Kada planirate putovati?" "Koji je vaš raspon budžeta?" "Koje aktivnosti volite na odmoru?"

2. **Prikupljanje informacija**
   - Pretražite relevantne opcije putovanja na temelju korisničkih preferencija.
   - **Letovi**: Potražite dostupne letove unutar korisničkog budžeta i preferiranih datuma.
   - **Smještaj**: Pronađite hotele ili najmove koji odgovaraju korisnikovim preferencijama vezanim za lokaciju, cijenu i pogodnosti.
   - **Atrakcije i restorani**: Identificirajte popularne atrakcije, aktivnosti i mogućnosti prehrane koje se podudaraju s interesima korisnika.

3. **Generiranje preporuka**
   - Sastavite prikupljene informacije u personalizirani itinerar.
   - Pružite detalje kao što su opcije leta, rezervacije hotela i predložene aktivnosti, pazeći da prilagodite preporuke korisnikovim preferencijama.

4. **Predstavljanje itinerara korisniku**
   - Podijelite predloženi itinerar s korisnikom na pregled.
   - Primjer: "Evo predloženog itinerara za vaše putovanje u Pariz. Uključuje detalje o letu, rezervacije hotela i popis preporučenih aktivnosti i restorana. Javite mi svoje mišljenje!"

5. **Prikupljanje povratnih informacija**
   - Pitajte korisnika za povratne informacije o predloženom itineraru.
   - Primjeri: "Sviđaju li vam se opcije leta?" "Je li hotel prikladan za vaše potrebe?" "Postoje li aktivnosti koje biste željeli dodati ili ukloniti?"

6. **Prilagodba na temelju povratnih informacija**
   - Izmijenite itinerar prema korisnikovim povratnim informacijama.
   - Napravite potrebne promjene u preporukama za letove, smještaj i aktivnosti kako biste bolje zadovoljili korisničke preferencije.

7. **Završna potvrda**
   - Predstavite ažurirani itinerar korisniku na konačnu potvrdu.
   - Primjer: "Napravio sam prilagodbe prema vašim povratnim informacijama. Evo ažuriranog itinerara. Je li sve u redu za vas?"

8. **Rezervirajte i potvrdite rezervacije**
   - Nakon što korisnik odobri itinerar, nastavite s rezervacijom letova, smještaja i bilo kojih prethodno planiranih aktivnosti.
   - Pošaljite potvrde korisniku.

9. **Pružite stalnu podršku**
   - Budite dostupni za pomoć korisniku oko bilo kakvih promjena ili dodatnih zahtjeva prije i tijekom njihovog putovanja.
   - Primjer: "Ako vam zatreba dodatna pomoć tijekom putovanja, slobodno me kontaktirajte u bilo koje vrijeme!"

### Primjer interakcije

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

# Primjer korištenja unutar zahtjeva za rezervacijom
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

## 3. Korektivni RAG sustav

Prvo, započnimo razumijevanjem razlike između RAG alata i preemptivnog učitavanja konteksta

![RAG vs Context Loading](../../../translated_images/hr/rag-vs-context.9eae588520c00921.webp)

### Retrieval-Augmented Generation (RAG)

RAG kombinira sustav dohvat podataka sa generativnim modelom. Kada se postavi upit, sustav dohvaća relevantne dokumente ili podatke iz vanjskog izvora, a te dohvaćene informacije koriste se za povećanje ulaza generativnom modelu. To pomaže modelu generirati točnije i kontekstualno relevantnije odgovore.

U RAG sustavu, agent dohvaća relevantne informacije iz baze znanja i koristi ih za generiranje odgovarajućih odgovora ili radnji.

### Korektivni RAG pristup

Korektivni RAG pristup usredotočen je na korištenje RAG tehnika za ispravljanje pogrešaka i unapređenje točnosti AI agenata. To uključuje:

1. **Tehnika poticanja (prompting)**: Korištenje specifičnih promptova za usmjeravanje agenta u dohvaćanju relevantnih informacija.
2. **Alat**: Implementacija algoritama i mehanizama koji agentu omogućuju evaluaciju relevantnosti dohvaćenih informacija i generiranje točnih odgovora.
3. **Evaluacija**: Kontinuirano procjenjivanje izvedbe agenta i prilagodbe radi poboljšanja točnosti i učinkovitosti.

#### Primjer: Korektivni RAG u tražilu (search agent)

Razmotrite tražilicu koja dohvaća informacije s interneta za odgovaranje na korisničke upite. Korektivni RAG pristup može uključivati:

1. **Tehnika poticanja**: Formuliranje upita za pretraživanje na temelju korisničkog unosa.
2. **Alat**: Korištenje algoritama obrade prirodnog jezika i strojnog učenja za rangiranje i filtriranje rezultata pretraživanja.
3. **Evaluacija**: Analiziranje povratnih informacija korisnika za identificiranje i ispravljanje netočnosti u dohvaćenim informacijama.

### Korektivni RAG u Putničkom Agentu

Korektivni RAG (Retrieval-Augmented Generation) pojačava sposobnost AI da dohvaća i generira informacije dok ispravlja eventualne netočnosti. Pogledajmo kako Putnički Agent može koristiti korektivni RAG pristup za pružanje točnijih i relevantnijih preporuka za putovanja.

To uključuje:

- **Tehniku poticanja:** Korištenje specifičnih promptova za usmjeravanje agenta u dohvaćanju relevantnih informacija.
- **Alat:** Implementaciju algoritama i mehanizama koji agentu omogućuju evaluaciju relevantnosti dohvaćenih informacija i generiranje točnih odgovora.
- **Evaluaciju:** Kontinuirano procjenjivanje izvedbe agenta i prilagođavanje radi povećanja točnosti i učinkovitosti.

#### Koraci za implementaciju korektivnog RAG-a u Putnički Agent

1. **Početna interakcija s korisnikom**
   - Putnički Agent prikuplja početne preferencije od korisnika, poput destinacije, datuma putovanja, budžeta i interesa.
   - Primjer:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Dohvaćanje informacija**
   - Putnički Agent dohvaća informacije o letovima, smještaju, atrakcijama i restoranima na temelju korisničkih preferencija.
   - Primjer:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generiranje početnih preporuka**
   - Putnički Agent koristi dohvaćene informacije za generiranje personaliziranog itinerara.
   - Primjer:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Prikupljanje povratnih informacija korisnika**
   - Putnički Agent traži povratne informacije o početnim preporukama.
   - Primjer:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Proces korektivnog RAG-a**
   - **Tehnika poticanja**: Putnički Agent formulira nove upite za pretraživanje na temelju povratnih informacija korisnika.
     - Primjer:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Alat**: Putnički Agent koristi algoritme za rangiranje i filtriranje novih rezultata pretraživanja, naglašavajući relevantnost na osnovi povratnih informacija.
     - Primjer:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Evaluacija**: Putnički Agent kontinuirano procjenjuje relevantnost i točnost svojih preporuka analizom povratnih informacija i izvršavanjem potrebnih prilagodbi.
     - Primjer:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Praktičan primjer

Evo pojednostavljenog primjera Python koda koji uključuje korektivni RAG pristup u Putničkom Agentu:

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

# Primjer upotrebe
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

### Preemptivno učitavanje konteksta


Pre-emptivno učitavanje konteksta uključuje unaprijed učitavanje relevantnog konteksta ili pozadinskih informacija u model prije obrade upita. To znači da model već od početka ima pristup tim informacijama, što mu može pomoći da generira informiranije odgovore bez potrebe za dohvatom dodatnih podataka tijekom procesa.

Evo pojednostavljenog primjera kako bi pre-emptivno učitavanje konteksta moglo izgledati za aplikaciju putničkog agenta u Pythonu:

```python
class TravelAgent:
    def __init__(self):
        # Unaprijed učitaj popularne destinacije i njihove informacije
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Dohvati informacije o destinaciji iz unaprijed učitanog konteksta
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Primjer korištenja
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Objašnjenje

1. **Inicijalizacija (metoda `__init__`)**: Klasa `TravelAgent` unaprijed učitava rječnik koji sadrži informacije o popularnim destinacijama poput Pariza, Tokija, New Yorka i Sydneya. Taj rječnik uključuje detalje poput zemlje, valute, jezika i glavnih atrakcija za svaku destinaciju.

2. **Dohvaćanje informacija (metoda `get_destination_info`)**: Kada korisnik zatraži informacije o određenoj destinaciji, metoda `get_destination_info` dohvaća relevantne podatke iz unaprijed učitanog rječnika konteksta.

Učitavanjem konteksta unaprijed aplikacija putničkog agenta može brzo odgovoriti na upite korisnika bez potrebe za dohvatom tih informacija iz vanjskog izvora u stvarnom vremenu. To čini aplikaciju učinkovitijom i bržom.

### Pokretanje plana s ciljem prije iteracije

Pokretanje plana s ciljem uključuje započinjanje s jasnim ciljem ili željenim ishodom na umu. Definiranjem tog cilja unaprijed, model ga može koristiti kao vodič tijekom iterativnog procesa. To pomaže osigurati da svaka iteracija približava ostvarivanju željenog ishoda, čineći proces učinkovitijim i fokusiranijim.

Evo primjera kako možete pokrenuti plan putovanja s ciljem prije iteracije za putničkog agenta u Pythonu:

### Scenarij

Putnički agent želi isplanirati prilagođeni odmor za klijenta. Cilj je stvoriti plan putovanja koji maksimalno zadovoljava klijentove preferencije i budžet.

### Koraci

1. Definirati preferencije i budžet klijenta.
2. Pokrenuti početni plan temeljen na tim preferencijama.
3. Iterirati za poboljšanje plana, optimizirajući za zadovoljstvo klijenta.

#### Python kod

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

# Primjer upotrebe
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

#### Objašnjenje koda

1. **Inicijalizacija (metoda `__init__`)**: Klasa `TravelAgent` se inicijalizira s popisom potencijalnih destinacija, svaka sa atributima kao što su ime, cijena i vrsta aktivnosti.

2. **Pokretanje plana (metoda `bootstrap_plan`)**: Ova metoda stvara početni plan putovanja temeljen na preferencijama i budžetu klijenta. Prolazi kroz popis destinacija i dodaje ih u plan ako odgovaraju preferencijama klijenta i stanu u budžet.

3. **Usklađivanje preferencija (metoda `match_preferences`)**: Ova metoda provjerava odgovara li destinacija preferencijama klijenta.

4. **Iteriranje plana (metoda `iterate_plan`)**: Ova metoda poboljšava početni plan pokušavajući zamijeniti svaku destinaciju u planu boljom opcijom, uzimajući u obzir klijentove preferencije i ograničenja budžeta.

5. **Izračun troškova (metoda `calculate_cost`)**: Ova metoda izračunava ukupne troškove trenutnog plana, uključujući potencijalno novu destinaciju.

#### Primjer korištenja

- **Početni plan**: Putnički agent stvara početni plan temeljen na klijentovim preferencijama za razgledavanje i budžetu od 2000 dolara.
- **Poboljšani plan**: Putnički agent iterira plan, optimizirajući prema klijentovim preferencijama i budžetu.

Pokretanjem plana s jasnim ciljem (npr. maksimalno zadovoljstvo klijenta) i iteracijom za njegovo usavršavanje, putnički agent može stvoriti prilagođeni i optimizirani plan putovanja za klijenta. Ovaj pristup osigurava da plan putovanja od početka odgovara klijentovim preferencijama i budžetu te se poboljšava sa svakom iteracijom.

### Iskorištavanje LLM-a za ponovnu rangiranje i dodjelu bodova

Veliki jezični modeli (LLM) mogu se koristiti za ponovnu rangiranje i dodjelu bodova ocjenjujući relevantnost i kvalitetu dohvaćenih dokumenata ili generiranih odgovora. Evo kako to funkcionira:

**Dohvat:** Početni korak dohvaća skup kandidata dokumenata ili odgovora temeljem upita.

**Ponovno rangiranje:** LLM evaluira te kandidate i ponovno ih rangira prema relevantnosti i kvaliteti. Ovaj korak osigurava da se najrelevantnije i najkvalitetnije informacije prikazuju prve.

**Dodjela bodova:** LLM dodjeljuje bodove svakom kandidatu koji odražavaju njihovu relevantnost i kvalitetu. To pomaže u odabiru najboljeg odgovora ili dokumenta za korisnika.

Iskorištavanjem LLM-a za ponovno rangiranje i dodjelu bodova, sustav može pružiti preciznije i kontekstualno relevantne informacije, poboljšavajući sveukupno korisničko iskustvo.

Evo primjera kako putnički agent može koristiti Veliki jezični model (LLM) za ponovno rangiranje i dodjelu bodova destinacija za putovanje na temelju korisničkih preferencija u Pythonu:

#### Scenarij - Putovanje prema preferencijama

Putnički agent želi preporučiti najbolje destinacije za putovanje klijentu na temelju njegovih preferencija. LLM će pomoći pri ponovnom rangiranju i dodjeli bodova destinacijama kako bi se osiguralo da se prikažu najrelevantnije opcije.

#### Koraci:

1. Prikupiti korisničke preferencije.
2. Dohvatiti popis potencijalnih destinacija za putovanje.
3. Koristiti LLM za ponovno rangiranje i dodjelu bodova destinacijama na temelju korisničkih preferencija.

Evo kako možete ažurirati prethodni primjer da koristi Azure OpenAI servise:

#### Zahtjevi

1. Morate imati Azure pretplatu.
2. Kreirati Azure OpenAI resurs i dobiti svoj API ključ.

#### Primjer Python koda

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generiraj prompt za Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Definiraj zaglavlja i sadržaj zahtjeva
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Pozovi Azure OpenAI API za dobivanje ponovno rangiranih i ocijenjenih destinacija
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Izvuci i vrati preporuke
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

# Primjer upotrebe
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

#### Objašnjenje koda - Rezervator preferencija

1. **Inicijalizacija**: Klasa `TravelAgent` se inicijalizira s popisom potencijalnih destinacija, svaka s atributima poput imena i opisa.

2. **Dohvat preporuka (metoda `get_recommendations`)**: Ova metoda generira upit za Azure OpenAI servis na temelju korisničkih preferencija i šalje HTTP POST zahtjev na Azure OpenAI API za dobivanje ponovno rangiranih i ocijenjenih destinacija.

3. **Generiranje upita (metoda `generate_prompt`)**: Ova metoda sastavlja upit za Azure OpenAI, uključujući korisničke preferencije i popis destinacija. Upit usmjerava model da ponovno rangira i ocijeni destinacije na temelju navedenih preferencija.

4. **API poziv**: Korištena je knjižnica `requests` za slanje HTTP POST zahtjeva na Azure OpenAI API endpoint. Odgovor sadrži ponovno rangirane i ocijenjene destinacije.

5. **Primjer korištenja**: Putnički agent prikuplja korisničke preferencije (npr. interes za razgledavanje i raznoliku kulturu) i koristi Azure OpenAI servis za dobivanje ponovno rangiranih i ocijenjenih preporuka za destinacije.

Obavezno zamijenite `your_azure_openai_api_key` svojim stvarnim Azure OpenAI API ključem i `https://your-endpoint.com/...` stvarnim URL-om endpointa vaše Azure OpenAI implementacije.

Iskorištavanjem LLM-a za ponovno rangiranje i dodjelu bodova, putnički agent može pružiti personaliziranije i relevantnije preporuke za putovanja klijentima, poboljšavajući njihovo ukupno iskustvo.

### RAG: Tehnika upita naspram alata

Retrieval-Augmented Generation (RAG) može biti i tehnika upita i alat u razvoju AI agenata. Razumijevanje razlike između ta dva može vam pomoći učinkovitije koristiti RAG u svojim projektima.

#### RAG kao tehnika upita

**Što je to?**

- Kao tehnika upita, RAG uključuje formuliranje specifičnih pitanja ili upita za usmjeravanje dohvaćanja relevantnih informacija iz velikog korpusa ili baze podataka. Te se informacije potom koriste za generiranje odgovora ili radnji.

**Kako funkcionira:**

1. **Formuliranje upita**: Izradite dobro strukturirane upite ili pitanja temeljena na zadatku ili korisničkom unosu.
2. **Dohvat informacija**: Koristite upite za pronalazak relevantnih podataka iz postojeće baze znanja ili skupa podataka.
3. **Generiranje odgovora**: Kombinirajte dohvaćene informacije s generativnim AI modelima kako biste proizveli sveobuhvatan i koherentan odgovor.

**Primjer u putničkom agentu**:

- Korisnički unos: "Želim posjetiti muzeje u Parizu."
- Upit: "Pronađi najbolje muzeje u Parizu."
- Dohvaćene informacije: Detalji o Louvre muzeju, Musée d'Orsay itd.
- Generirani odgovor: "Evo nekoliko najboljih muzeja u Parizu: Louvre muzej, Musée d'Orsay i Centre Pompidou."

#### RAG kao alat

**Što je to?**

- Kao alat, RAG je integrirani sustav koji automatizira postupak dohvaćanja i generiranja, olakšavajući programerima implementaciju složenih AI funkcionalnosti bez ručnog sastavljanja upita za svaki pojedini zahtjev.

**Kako funkcionira:**

1. **Integracija**: Ugradite RAG unutar arhitekture AI agenta, omogućujući mu da automatski upravlja zadacima dohvaćanja i generiranja.
2. **Automatizacija**: Alat upravlja cijelim postupkom, od primanja korisničkog unosa do generiranja konačnog odgovora, bez potrebe za eksplicitnim upitima za svaki korak.
3. **Učinkovitost**: Poboljšava performanse agenta pojednostavljenjem postupka dohvaćanja i generiranja, omogućujući brže i točnije odgovore.

**Primjer u putničkom agentu**:

- Korisnički unos: "Želim posjetiti muzeje u Parizu."
- RAG alat: Automatski dohvaća informacije o muzejima i generira odgovor.
- Generirani odgovor: "Evo nekoliko najboljih muzeja u Parizu: Louvre muzej, Musée d'Orsay i Centre Pompidou."

### Usporedba

| Aspekt                 | Tehnika upita                                             | Alat                                                  |
|------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| **Ručno vs Automatski**| Ručno formuliranje upita za svaki zahtjev.                  | Automatizirani postupak dohvaćanja i generiranja.      |
| **Kontrola**           | Nudi veću kontrolu nad postupkom dohvaćanja.                | Pojednostavljuje i automatizira postupak dohvaćanja i generiranja.|
| **Fleksibilnost**       | Omogućuje prilagođene upite prema specifičnim potrebama.    | Učinkovitiji za implementacije u velikom opsegu.       |
| **Složenost**          | Zahtijeva izradu i podešavanje upita.                        | Lakše se integrira u arhitekturu AI agenta.            |

### Praktični primjeri

**Primjer tehnike upita:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Primjer alata:**

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

### Procjena relevantnosti

Procjena relevantnosti je ključan aspekt performansi AI agenta. Osigurava da su informacije koje agent dohvaća i generira prikladne, točne i korisne za korisnika. Pregledajmo kako procijeniti relevantnost u AI agentima, uključujući praktične primjere i tehnike.

#### Ključni pojmovi u procjeni relevantnosti

1. **Svijest o kontekstu**:
   - Agent mora razumjeti kontekst korisničkog upita kako bi dohvaćao i generirao relevantne informacije.
   - Primjer: Ako korisnik traži "najbolje restorane u Parizu," agent treba uzeti u obzir korisnikove preferencije poput vrste kuhinje i budžeta.

2. **Točnost**:
   - Informacije koje pruža agent trebaju biti činjenicno točne i ažurne.
   - Primjer: Preporučivanje trenutno otvorenih restorana s dobrim recenzijama umjesto zastarjelih ili zatvorenih opcija.

3. **Namera korisnika**:
   - Agent treba iščitati namjeru korisnika iza upita kako bi pružio najrelevantnije informacije.
   - Primjer: Ako korisnik traži "povoljni hoteli," agent treba dati prioritet pristupačnim opcijama.

4. **Petlja povratne informacije**:
   - Kontinuirano prikupljanje i analiza povratnih informacija korisnika pomaže agentu u usavršavanju procesa procjene relevantnosti.
   - Primjer: Uključivanje ocjena korisnika i povratnih informacija o prethodnim preporukama za poboljšanje budućih odgovora.

#### Praktične tehnike za procjenu relevantnosti

1. **Dodjela ocjena relevantnosti**:
   - Dodijelite ocjenu relevantnosti svakom dohvaćenom elementu na temelju koliko dobro odgovara korisničkom upitu i preferencijama.
   - Primjer:

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

2. **Filtriranje i rangiranje**:
   - Izbrišite nerelevantne stavke i rangirajte preostale prema njihovim ocjenama relevantnosti.
   - Primjer:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Vrati prvih 10 relevantnih stavki
     ```

3. **Obrada prirodnog jezika (NLP)**:
   - Iskoristite NLP tehnike za razumijevanje korisničkog upita i dohvaćanje relevantnih informacija.
   - Primjer:

     ```python
     def process_query(query):
         # Koristite NLP za izdvajanje ključnih informacija iz korisnikovog upita
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integracija korisničkog feedbacka**:
   - Prikupite povratne informacije od korisnika o pruženim preporukama i koristite ih za prilagođavanje budućih procjena relevantnosti.
   - Primjer:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Primjer: Procjena relevantnosti u putničkom agentu

Evo praktičnog primjera kako putnički agent može procijeniti relevantnost preporuka za putovanja:

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
        return ranked_items[:10]  # Vrati top 10 relevantnih stavki

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

# Primjer korištenja
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

### Pretraživanje s namjerom

Pretraživanje s namjerom uključuje razumijevanje i tumačenje temeljne svrhe ili cilja iza korisničkog upita kako bi se dohvatilo i generiralo najrelevantnije i najkorisnije informacije. Ovaj pristup nadilazi puko podudaranje ključnih riječi i fokusira se na razumijevanje stvarnih potreba i konteksta korisnika.

#### Ključni pojmovi u pretraživanju s namjerom

1. **Razumijevanje namjere korisnika**:
   - Korisnička namjera može se kategorizirati u tri glavne vrste: informativna, navigacijska i transakcijska.
     - **Informativna namjera**: Korisnik traži informacije o nekoj temi (npr. "Koji su najbolji muzeji u Parizu?").
     - **Navigacijska namjera**: Korisnik želi doći do određene web stranice ili stranice (npr. "Službena stranica Louvre muzeja").
     - **Transakcijska namjera**: Korisnik želi izvršiti neku transakciju, poput rezervacije leta ili kupnje (npr. "Rezerviraj let za Pariz").

2. **Svijest o kontekstu**:
   - Analiza konteksta korisničkog upita pomaže u točnom identificiranju njihove namjere. To uključuje razmatranje prethodnih interakcija, preferencija korisnika i specifičnih detalja trenutnog upita.

3. **Obrada prirodnog jezika (NLP)**:
   - NLP tehnike koriste se za razumijevanje i tumačenje prirodnih jezičnih upita koje daju korisnici. To uključuje zadatke poput prepoznavanja entiteta, analize sentimenta i parsiranja upita.

4. **Personalizacija**:
   - Personalizacija rezultata pretraživanja na temelju korisničke povijesti, preferencija i povratnih informacija poboljšava relevantnost dohvaćenih informacija.

#### Praktični primjer: Pretraživanje s namjerom u putničkom agentu

Uzmi kao primjer putnički agent kako bi vidjeli kako se pretraživanje s namjerom može implementirati.

1. **Prikupljanje korisničkih preferencija**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Razumijevanje korisničke namjere**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Svijest o kontekstu**


   ```python
   def analyze_context(query, user_history):
       # Kombinirajte trenutni upit s poviješću korisnika kako biste razumjeli kontekst
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Pretraživanje i personalizacija rezultata**

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
       # Primjer logike pretraživanja za informativnu namjeru
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Primjer logike pretraživanja za navigacijsku namjeru
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Primjer logike pretraživanja za transakcijsku namjeru
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Primjer logike personalizacije
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Vrati prvih 10 personaliziranih rezultata
   ```

5. **Primjer uporabe**

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

## 4. Generiranje koda kao alat

Agent za generiranje koda koristi AI modele za pisanje i izvršavanje koda, rješavajući složene probleme i automatizirajući zadatke.

### Agent za generiranje koda

Agent za generiranje koda koristi generativne AI modele za pisanje i izvršavanje koda. Ti agenti mogu rješavati složene probleme, automatizirati zadatke i pružiti vrijedne uvide generiranjem i pokretanjem koda u različitim programskim jezicima.

#### Praktične primjene

1. **Automatizirano generiranje koda**: Generiranje isječaka koda za specifične zadatke, kao što su analiza podataka, web scraping ili strojno učenje.
2. **SQL kao RAG**: Korištenje SQL upita za dohvat i manipulaciju podacima iz baza podataka.
3. **Rješavanje problema**: Izrada i izvršavanje koda za rješavanje specifičnih problema, poput optimizacije algoritama ili analize podataka.

#### Primjer: Agent za generiranje koda za analizu podataka

Zamislite da dizajnirate agenta za generiranje koda. Evo kako bi to moglo funkcionirati:

1. **Zadatak**: Analizirati skup podataka kako bi se identificirali trendovi i obrasci.
2. **Koraci**:
   - Učitati skup podataka u alat za analizu podataka.
   - Generirati SQL upite da se filtriraju i agregiraju podaci.
   - Izvršiti upite i dohvatiti rezultate.
   - Koristiti rezultate za generiranje vizualizacija i uvida.
3. **Potreban resurs**: Pristup skupu podataka, alati za analizu podataka i SQL mogućnosti.
4. **Iskustvo**: Koristiti prethodne rezultate analize za poboljšanje točnosti i relevantnosti budućih analiza.

### Primjer: Agent za generiranje koda za putničkog agenta

U ovom primjeru dizajnirat ćemo agenta za generiranje koda, Putničkog agenta, koji pomaže korisnicima u planiranju putovanja generiranjem i izvršavanjem koda. Ovaj agent može obavljati zadatke poput dohvaćanja opcija putovanja, filtriranja rezultata i sastavljanja itinerera koristeći generativnu AI.

#### Pregled agenta za generiranje koda

1. **Prikupljanje korisničkih preferencija**: Prikuplja korisničke unose poput odredišta, datuma putovanja, budžeta i interesa.
2. **Generiranje koda za dohvat podataka**: Generira isječke koda za dohvat podataka o letovima, hotelima i atrakcijama.
3. **Izvršavanje generiranog koda**: Pokreće generirani kod da bi dohvatili informacije u stvarnom vremenu.
4. **Generiranje itinerera**: Sastavlja dohvaćene podatke u personalizirani plan putovanja.
5. **Prilagodba temeljem povratnih informacija**: Prima povratne informacije korisnika i po potrebi ponovno generira kod za poboljšanje rezultata.

#### Implementacija korak po korak

1. **Prikupljanje korisničkih preferencija**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generiranje koda za dohvat podataka**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Primjer: Generiraj kod za pretraživanje letova prema korisničkim željama
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Primjer: Generiraj kod za pretraživanje hotela
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Izvršavanje generiranog koda**

   ```python
   def execute_code(code):
       # Izvrši generirani kod koristeći exec
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

4. **Generiranje itinerera**

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

5. **Prilagodba temeljem povratnih informacija**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Prilagodite postavke na temelju korisničkih povratnih informacija
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Ponovno generirajte i izvršite kôd s ažuriranim postavkama
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Korištenje svijesti o okruženju i rezoniranju

Temeljeno na shemi tablice zaista može unaprijediti proces generiranja upita korištenjem svijesti o okruženju i rezoniranja.

Evo primjera kako se to može napraviti:

1. **Razumijevanje sheme**: Sustav razumije shemu tablice i koristi te informacije za osiguranje temelja u generiranju upita.
2. **Prilagodba temeljem povratnih informacija**: Sustav prilagođava korisničke preferencije na temelju povratnih informacija i razmišlja koje se polja u shemi trebaju ažurirati.
3. **Generiranje i izvršavanje upita**: Sustav generira i izvršava upite kako bi dohvaćao ažurirane podatke o letovima i hotelima na temelju novih preferencija.

Evo ažuriranog primjera Python koda koji uključuje ove koncepte:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Prilagodi postavke na temelju povratnih informacija korisnika
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Razumijevanje temeljeno na shemi za prilagodbu drugih povezanih postavki
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Prilagođena logika za prilagodbu postavki na temelju sheme i povratnih informacija
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generiraj kod za dohvat podataka o letovima na temelju ažuriranih postavki
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generiraj kod za dohvat podataka o hotelima na temelju ažuriranih postavki
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simuliraj izvršavanje koda i vrati lažne podatke
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generiraj itinerar na temelju letova, hotela i atrakcija
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Primjer sheme
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Primjer upotrebe
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Ponovno generiraj i izvrši kod s ažuriranim postavkama
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Objašnjenje - Rezervacija na temelju povratnih informacija

1. **Svijest o shemi**: Rječnik `schema` definira kako se preferencije trebaju prilagoditi na temelju povratnih informacija. Uključuje polja poput `favorites` i `avoid`, sa pripadajućim prilagodbama.
2. **Prilagodba preferencija (`adjust_based_on_feedback` metoda)**: Ova metoda prilagođava preferencije na temelju korisničkih povratnih informacija i sheme.
3. **Prilagodbe temeljem okruženja (`adjust_based_on_environment` metoda)**: Ova metoda prilagođava prilagodbe temeljem sheme i povratnih informacija.
4. **Generiranje i izvršavanje upita**: Sustav generira kod za dohvat ažuriranih podataka o letovima i hotelima temeljem prilagođenih preferencija te simulira izvršavanje tih upita.
5. **Generiranje itinerera**: Sustav stvara ažurirani itinerer temeljen na novim podacima o letovima, hotelima i atrakcijama.

Čineći sustav svjesnim okruženja i rezonirajući na temelju sheme, može se generirati točnije i relevantnije upite, što vodi do boljih preporuka za putovanja i osobnije korisničko iskustvo.

### Korištenje SQL-a kao tehnike Retrieval-Augmented Generation (RAG)

SQL (Strukturirani jezik upita) moćan je alat za interakciju s bazama podataka. Kada se koristi kao dio pristupa Retrieval-Augmented Generation (RAG), SQL može dohvatiti relevantne podatke iz baza podataka kako bi informirao i generirao odgovore ili radnje u AI agentima. Pogledajmo kako se SQL može koristiti kao tehnika RAG u kontekstu Putničkog agenta.

#### Ključni pojmovi

1. **Interakcija s bazom podataka**:
   - SQL se koristi za upite baza podataka, dohvat relevantnih informacija i manipulaciju podacima.
   - Primjer: Dohvaćanje podataka o letovima, hotelima i atrakcijama iz baze putovanja.

2. **Integracija s RAG**:
   - SQL upiti se generiraju na temelju korisničkog unosa i preferencija.
   - Dohvaćeni podaci se zatim koriste za generiranje personaliziranih preporuka ili radnji.

3. **Dinamičko generiranje upita**:
   - AI agent generira dinamičke SQL upite temeljem konteksta i potreba korisnika.
   - Primjer: Prilagođavanje SQL upita za filtriranje rezultata temeljem budžeta, datuma i interesa.

#### Primjene

- **Automatizirano generiranje koda**: Generiranje isječaka koda za određene zadatke.
- **SQL kao RAG**: Korištenje SQL upita za manipulaciju podacima.
- **Rješavanje problema**: Izrada i izvršavanje koda za rješavanje problema.

**Primjer**:
Agent za analizu podataka:

1. **Zadatak**: Analizirati skup podataka radi pronalaska trendova.
2. **Koraci**:
   - Učitati skup podataka.
   - Generirati SQL upite za filtriranje podataka.
   - Izvršiti upite i dohvatiti rezultate.
   - Generirati vizualizacije i uvide.
3. **Resursi**: Pristup skupu podataka, SQL mogućnosti.
4. **Iskustvo**: Koristiti prethodne rezultate za poboljšanje budućih analiza.

#### Praktični primjer: Korištenje SQL-a u Putničkom agentu

1. **Prikupljanje korisničkih preferencija**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generiranje SQL upita**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Izvršavanje SQL upita**

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

4. **Generiranje preporuka**

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

#### Primjer SQL upita

1. **Upit za letove**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Upit za hotele**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Upit za atrakcije**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Korištenjem SQL-a kao dijela tehnike Retrieval-Augmented Generation (RAG), AI agenti poput Putničkog agenta mogu dinamički dohvaćati i koristiti relevantne podatke za pružanje točnih i personaliziranih preporuka.

### Primjer metakognicije

Kako bismo demonstrirali implementaciju metakognicije, kreirajmo jednostavnog agenta koji *reflektira o svom procesu donošenja odluka* dok rješava problem. Za ovaj primjer, izgradit ćemo sustav gdje agent pokušava optimizirati odabir hotela, a zatim evaluira svoje rezoniranje i prilagođava strategiju kada napravi pogreške ili suboptimalne izbore.

To ćemo simulirati koristeći osnovni primjer gdje agent bira hotele temeljeno na kombinaciji cijene i kvalitete, ali će "reflektirati" o svojim odlukama i prilagođavati se sukladno tome.

#### Kako to ilustrira metakogniciju:

1. **Početna odluka**: Agent će izabrati najjeftiniji hotel, bez razumijevanja utjecaja kvalitete.
2. **Refleksija i evaluacija**: Nakon početnog izbora, agent provjerava je li hotel "loš" izbor koristeći povratne informacije korisnika. Ako ustanovi da je kvaliteta hotela bila preslaba, reflektira o svom rezoniranju.
3. **Prilagodba strategije**: Agent prilagođava strategiju na temelju refleksije, prelazeći s "najjeftinijeg" na "najkvalitetnijeg", čime poboljšava proces donošenja odluka u budućim iteracijama.

Evo jednog primjera:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Sprema prethodno odabrane hotele
        self.corrected_choices = []  # Sprema ispravljene odabire
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Dostupne strategije

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
        # Pretpostavimo da imamo povratne informacije korisnika koje nam govore je li posljednji izbor bio dobar ili ne
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Prilagodi strategiju ako je prethodni izbor bio nezadovoljavajući
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

# Simulira popis hotela (cijena i kvaliteta)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Kreiraj agenta
agent = HotelRecommendationAgent()

# Korak 1: Agent preporučuje hotel koristeći strategiju "najjeftiniji"
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Korak 2: Agent razmatra odabir i po potrebi prilagođava strategiju
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Korak 3: Agent ponovno preporučuje, ovaj put koristeći prilagođenu strategiju
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Metakognitivne sposobnosti agenata

Ključ je u sposobnosti agenta da:
- Procijeni svoje prethodne izbore i proces donošenja odluka.
- Prilagodi svoju strategiju na temelju te refleksije, tj. metakognicija na djelu.

Ovo je jednostavan oblik metakognicije gdje je sustav sposoban prilagoditi svoj proces rezoniranja temeljem unutarnjih povratnih informacija.

### Zaključak

Metakognicija je moćan alat koji može značajno poboljšati sposobnosti AI agenata. Uključivanjem metakognitivnih procesa, možete dizajnirati agente koji su inteligentniji, prilagodljiviji i učinkovitiji. Iskoristite dodatne resurse za daljnje istraživanje fascinantnog svijeta metakognicije u AI agentima.

### Imate dodatnih pitanja o obrascu dizajna metakognicije?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) da se povežete s drugim učenicima, sudjelujete na konzultacijama i dobijete odgovore na svoja pitanja o AI agentima.

## Prethodna lekcija

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Sljedeća lekcija

[AI Agents in Production](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->