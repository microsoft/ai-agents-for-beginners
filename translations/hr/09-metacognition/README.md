[![Dizajn s više agenata](../../../translated_images/hr/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Kliknite na gornju sliku za pregled videa ove lekcije)_
# Metakognicija u AI agentima

## Uvod

Dobrodošli na lekciju o metakogniciji u AI agentima! Ovo poglavlje je namijenjeno početnicima koji su znatiželjni kako AI agenti mogu razmišljati o vlastitim procesima razmišljanja. Do kraja ove lekcije razumjet ćete ključne pojmove i bit ćete opremljeni praktičnim primjerima za primjenu metakognicije u dizajnu AI agenata.

## Ciljevi učenja

Nakon što završite ovu lekciju, moći ćete:

1. Razumjeti implikacije petlji rezoniranja u definiranjima agenata.
2. Koristiti tehnike planiranja i evaluacije za pomoć agentima koji se samostalno ispravljaju.
3. Kreirati vlastite agente koji su sposobni manipulirati kodom za izvršavanje zadataka.

## Uvod u metakogniciju

Metakognicija se odnosi na kognitivne procese višeg reda koji uključuju razmišljanje o vlastitom razmišljanju. Za AI agente, to znači sposobnost evaluacije i prilagodbe svojih akcija na temelju samo-svijesti i prošlih iskustava. Metakognicija, ili "razmišljanje o razmišljanju," važan je koncept u razvoju agentnih AI sustava. Uključuje da AI sustavi budu svjesni vlastitih unutarnjih procesa i mogu pratiti, regulirati i prilagođavati svoje ponašanje sukladno tome. Baš kao što mi to radimo kada "čitamo prostoriju" ili promatramo problem. Ova samosvijest može pomoći AI sustavima donositi bolje odluke, prepoznati pogreške i s vremenom poboljšati svoje performanse - opet se povezujući s Turingovim testom i raspravom hoće li AI preuzeti kontrolu.

U kontekstu agentnih AI sustava, metakognicija može pomoći u rješavanju nekoliko izazova, kao što su:
- Transparentnost: Osiguravanje da AI sustavi mogu objasniti svoje rezoniranje i odluke.
- Razumijevanje: Unapređenje sposobnosti AI sustava da sintetiziraju informacije i donesu opravdane odluke.
- Prilagodba: Omogućavanje AI sustavima da se prilagođavaju novim okruženjima i promjenjivim uvjetima.
- Percepcija: Poboljšanje točnosti AI sustava u prepoznavanju i interpretaciji podataka iz svoje okoline.

### Što je metakognicija?

Metakognicija, ili "razmišljanje o razmišljanju," je kognitivni proces višeg reda koji uključuje samo-svijest i samoregulaciju vlastitih kognitivnih procesa. U području AI, metakognicija osnažuje agente da evaluiraju i prilagođavaju svoje strategije i akcije, što dovodi do poboljšanih sposobnosti rješavanja problema i donošenja odluka. Razumijevanjem metakognicije možete dizajnirati AI agente koji nisu samo inteligentniji, već i prilagodljiviji i učinkovitiji. U pravoj metakogniciji, AI bi eksplicitno rezonirao o svom vlastitom rezoniranju.

Primjer: “Prioritizirao sam jeftinije letove jer... možda propustim direktne letove, pa ću ponovno provjeriti.”.
Praćenje kako ili zašto je odabrao određenu rutu.
- Primjećivanje da je napravio pogreške jer je previše vjerovao preferencijama korisnika iz prošlog puta, pa mijenja svoju strategiju donošenja odluka, a ne samo konačnu preporuku.
- Dijagnosticiranje obrazaca poput: „Kad god vidim da korisnik spomene 'previše gužve,' ne bih trebao samo ukloniti određene atrakcije, već i razmisliti da je moj način odabira 'najboljih atrakcija' pogrešan ako ih uvijek rangiram po popularnosti.“

### Važnost metakognicije u AI agentima

Metakognicija igra ključnu ulogu u dizajnu AI agenata iz nekoliko razloga:

![Važnost metakognicije](../../../translated_images/hr/importance-of-metacognition.b381afe9aae352f7.webp)

- Samorefleksija: Agenti mogu procijeniti vlastite performanse i identificirati područja za poboljšanje.
- Prilagodljivost: Agenti mogu mijenjati svoje strategije na temelju prošlih iskustava i promjenjivih okruženja.
- Ispravljanje pogrešaka: Agenti mogu samostalno otkrivati i ispravljati pogreške, što vodi do točnijih rezultata.
- Upravljanje resursima: Agenti mogu optimizirati korištenje resursa, poput vremena i računalne snage, planiranjem i evaluacijom svojih akcija.

## Komponente AI agenta

Prije nego što zaronimo u metakognitivne procese, važno je razumjeti osnovne komponente AI agenta. AI agent se obično sastoji od:

- Persona: Osobnost i karakteristike agenta, koje definiraju kako komunicira s korisnicima.
- Alati: Sposobnosti i funkcije koje agent može izvršavati.
- Vještine: Znanje i stručnost koju agent posjeduje.

Ove komponente zajedno funkcioniraju kako bi stvorile "jedinicu stručnosti" koja može obavljati specifične zadatke.

**Primjer**:
Zamislite putničkog agenta, agenta usluga koji ne samo da planira vaš odmor već i prilagođava svoj put na temelju podataka u stvarnom vremenu i prošlih iskustava korisničkog putovanja.

### Primjer: Metakognicija u usluzi putničkog agenta

Zamislite da dizajnirate uslugu putničkog agenta vođenu AI-jem. Ovaj agent, "Putnički agent," pomaže korisnicima u planiranju njihovih odmora. Za uključivanje metakognicije, Putnički agent treba evaluirati i prilagođavati svoje akcije na temelju samo-svijesti i prošlih iskustava. Evo kako bi metakognicija mogla igrati ulogu:

#### Trenutni zadatak

Trenutni zadatak je pomoći korisniku u planiranju putovanja u Pariz.

#### Koraci za dovršetak zadatka

1. **Prikupljanje korisničkih preferencija**: Pitajte korisnika o datumima putovanja, budžetu, interesima (npr. muzeji, kuhinja, šoping) i bilo kakvim specifičnim zahtjevima.
2. **Prikupljanje informacija**: Pretražite opcije letova, smještaja, atrakcija i restorana koji odgovaraju preferencijama korisnika.
3. **Generiranje preporuka**: Pružite personalizirani itinerar s detaljima o letu, rezervacijama hotela i predloženim aktivnostima.
4. **Prilagodba na temelju povratnih informacija**: Pitajte korisnika za povratne informacije o preporukama i napravite potrebne izmjene.

#### Potrebni resursi

- Pristup bazama podataka za rezervacije letova i hotela.
- Informacije o atrakcijama i restoranima u Parizu.
- Podaci o povratnim informacijama korisnika iz prethodnih interakcija.

#### Iskustvo i samorefleksija

Putnički agent koristi metakogniciju za evaluaciju svoje izvedbe i učenje iz prošlih iskustava. Na primjer:

1. **Analiza povratnih informacija korisnika**: Putnički agent pregledava povratne informacije korisnika kako bi odredio koje su preporuke bile dobro prihvaćene, a koje nisu. Prilagođava svoje buduće prijedloge sukladno tome.
2. **Prilagodljivost**: Ako je korisnik ranije spomenuo da ne voli gužve, Putnički agent će u budućnosti izbjegavati preporučivanje popularnih turističkih mjesta tijekom vršnih sati.
3. **Ispravljanje pogrešaka**: Ako je Putnički agent napravio pogrešku u prethodnoj rezervaciji, poput predlaganja hotela koji je bio potpuno rezerviran, naučit će strože provjeravati dostupnost prije davanja preporuka.

#### Praktični primjer za programere

Evo pojednostavljenog primjera kako bi kod Putničkog agenta mogao izgledati pri uključivanju metakognicije:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Pretraži letove, hotele i atrakcije na temelju preferencija
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
        # Analiziraj povratne informacije i prilagodi buduće preporuke
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

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
travel_agent.adjust_based_on_feedback(feedback)
```

#### Zašto je metakognicija važna

- **Samorefleksija**: Agenti mogu analizirati svoje performanse i identificirati područja za poboljšanje.
- **Prilagodljivost**: Agenti mogu mijenjati strategije na temelju povratnih informacija i promjenjivih uvjeta.
- **Ispravljanje pogrešaka**: Agenti mogu samostalno otkrivati i ispravljati pogreške.
- **Upravljanje resursima**: Agenti mogu optimizirati korištenje resursa, poput vremena i računalne snage.

Uključivanjem metakognicije, Putnički agent može pružiti personaliziranije i točnije preporuke za putovanja, poboljšavajući ukupno korisničko iskustvo.

---

## 2. Planiranje u agentima

Planiranje je ključna komponenta ponašanja AI agenta. Uključuje definiranje koraka potrebnih za postizanje cilja, uzimajući u obzir trenutačno stanje, resurse i moguće prepreke.

### Elementi planiranja

- **Trenutni zadatak**: Jasno definirajte zadatak.
- **Koraci za dovršetak zadatka**: Podijelite zadatak u upravljive korake.
- **Potrebni resursi**: Identificirajte potrebne resurse.
- **Iskustvo**: Iskoristite prethodna iskustva za informiranje planiranja.

**Primjer**:
Ovdje su koraci koje Putnički agent mora poduzeti kako bi učinkovito pomogao korisniku u planiranju putovanja:

### Koraci za Putničkog agenta

1. **Prikupljanje korisničkih preferencija**
   - Pitajte korisnika za detalje o datumima putovanja, budžetu, interesima i specifičnim zahtjevima.
   - Primjeri: "Kada planirate putovati?" "Koji je vaš raspon budžeta?" "Koje aktivnosti volite tijekom odmora?"

2. **Prikupljanje informacija**
   - Tražite relevantne opcije putovanja na temelju korisničkih preferencija.
   - **Letovi**: Pronađite dostupne letove unutar budžeta korisnika i preferiranih datuma putovanja.
   - **Smještaj**: Pronađite hotele ili najmove koji odgovaraju korisnikovim preferencijama vezano za lokaciju, cijenu i pogodnosti.
   - **Atrakcije i restorani**: Identificirajte popularne atrakcije, aktivnosti i restorane koji odgovaraju interesima korisnika.

3. **Generiranje preporuka**
   - Sastavite prikupljene informacije u personalizirani itinerar.
   - Pružite detalje poput opcija letova, rezervacija hotela i predloženih aktivnosti, pazeći da preporuke budu prilagođene korisničkim preferencijama.

4. **Prezentacija itinerara korisniku**
   - Podijelite predloženi itinerar s korisnikom na pregled.
   - Primjer: "Evo predloženi itinerar za vaše putovanje u Pariz. Uključuje detalje o letu, rezervacije hotela i popis preporučenih aktivnosti i restorana. Javite mi vaše mišljenje!"

5. **Prikupljanje povratnih informacija**
   - Pitajte korisnika za povratne informacije o predloženom itineraru.
   - Primjeri: "Sviđaju li vam se opcije letova?" "Odgovara li vam hotel?" "Ima li nekih aktivnosti koje želite dodati ili ukloniti?"

6. **Prilagodba na temelju povratnih informacija**
   - Izmijenite itinerar prema korisničkim povratnim informacijama.
   - Napravite potrebne promjene u preporukama letova, smještaja i aktivnosti kako bi bolje odgovarale korisnikovim željama.

7. **Završna potvrda**
   - Predstavite ažurirani itinerar korisniku za konačnu potvrdu.
   - Primjer: "Napravio sam izmjene na temelju vaših povratnih informacija. Evo ažuriranog itinerara. Je li sve u redu?"

8. **Rezervacija i potvrda**
   - Nakon što korisnik odobri itinerar, nastavite s rezervacijom letova, smještaja i unaprijed planiranih aktivnosti.
   - Pošaljite korisniku detalje o potvrdi.

9. **Pružanje kontinuirane podrške**
   - Budite dostupni za pomoć korisniku s izmjenama ili dodatnim zahtjevima prije i tijekom putovanja.
   - Primjer: "Ako vam tijekom putovanja bude potrebna dodatna pomoć, slobodno mi se obratite u bilo kojem trenutku!"

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

# Primjer upotrebe unutar zahtjeva za rezervaciju
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

Prvo, krenimo s razumijevanjem razlike između RAG alata i unaprijed učitavanja konteksta

![RAG naspram učitavanja konteksta](../../../translated_images/hr/rag-vs-context.9eae588520c00921.webp)

### Retrieval-Augmented Generation (RAG)

RAG kombinira sustav pretraživanja sa generativnim modelom. Kad se postavi upit, sustav za pretraživanje dohvaća relevantne dokumente ili podatke iz izvornog izvora, a te dohvaćene informacije služe za proširenje ulaza generativnom modelu. To pomaže modelu da generira točnije i kontekstualno relevantne odgovore.

U RAG sustavu agent dohvaća relevantne informacije iz baze znanja i koristi ih za generiranje prikladnih odgovora ili akcija.

### Korektivni RAG pristup

Korektivni RAG pristup usredotočuje se na korištenje RAG tehnika za ispravljanje pogrešaka i poboljšanje točnosti AI agenata. To uključuje:

1. **Tehnika poticanja**: Korištenje specifičnih poticaja za usmjeravanje agenta pri dohvaćanju relevantnih informacija.
2. **Alat**: Implementaciju algoritama i mehanizama koji omogućuju agentu evaluaciju relevantnosti dohvaćenih informacija i generiranje točnih odgovora.
3. **Evaluacija**: Kontinuirano ocjenjivanje performansi agenta i prilagodbe za poboljšanje točnosti i učinkovitosti.

#### Primjer: Korektivni RAG u pretraživačkom agentu

Razmislite o pretraživačkom agentu koji dohvaća informacije s weba za odgovaranje na korisničke upite. Korektivni RAG pristup može uključivati:

1. **Tehnika poticanja**: Formuliranje upita za pretraživanje na temelju unosa korisnika.
2. **Alat**: Korištenje obrade prirodnog jezika i algoritama strojog učenja za rangiranje i filtriranje rezultata pretraživanja.
3. **Evaluacija**: Analizu povratnih informacija korisnika radi identifikacije i ispravljanja netočnosti u dohvaćenim informacijama.

### Korektivni RAG u Putničkom agentu

Korektivni RAG (Retrieval-Augmented Generation) poboljšava AI sposobnost dohvaćanja i generiranja informacija, istovremeno ispravljajući nedostatke. Pogledajmo kako Putnički agent može koristiti Korektivni RAG pristup za pružanje točnijih i relevantnijih preporuka za putovanja.

Ovo uključuje:

- **Tehnika poticanja:** Korištenje specifičnih poticaja za usmjeravanje agenta pri dohvaćanju relevantnih informacija.
- **Alat:** Implementaciju algoritama i mehanizama koji omogućuju agentu evaluaciju relevantnosti dohvaćenih informacija i generiranje točnih odgovora.
- **Evaluacija:** Kontinuirano ocjenjivanje performansi agenta i prilagodbe za poboljšanje točnosti i učinkovitosti.

#### Koraci implementacije Korektivnog RAG-a u Putnički agent

1. **Početna interakcija s korisnikom**
   - Putnički agent prikuplja početne preferencije korisnika, poput destinacije, datuma putovanja, budžeta i interesa.
   - Primjer:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Dohvat informacija**
   - Putnički agent dohvaća informacije o letovima, smještaju, atrakcijama i restoranima na temelju korisničkih preferencija.
   - Primjer:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generiranje početnih preporuka**
   - Putnički agent koristi dohvaćene informacije za generiranje personaliziranog itinerara.
   - Primjer:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Prikupljanje povratnih informacija korisnika**
   - Putnički agent traži povratne informacije korisnika o početnim preporukama.
   - Primjer:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Proces Korektivnog RAG-a**
   - **Tehnika poticanja**: Putnički agent formulira nove upite za pretraživanje na temelju povratnih informacija korisnika.
     - Primjer:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Alat**: Putnički agent koristi algoritme za rangiranje i filtriranje novih rezultata pretraživanja, naglašavajući relevantnost na temelju povratnih informacija korisnika.
     - Primjer:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Evaluacija**: Putnički agent kontinuirano procjenjuje relevantnost i točnost svojih preporuka analizom povratnih informacija korisnika i čini potrebne prilagodbe.
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

#### Praktični primjer

Evo pojednostavljenog Python koda koji uključuje Korektivni RAG pristup u Putnički agent:

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
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### Unaprijed učitavanje konteksta


Pre-emptive Context Load uključuje učitavanje relevantnog konteksta ili pozadinskih informacija u model prije obrade upita. To znači da model od početka ima pristup tim informacijama, što mu može pomoći da generira informirane odgovore bez potrebe za preuzimanjem dodatnih podataka tijekom procesa.

Evo pojednostavljenog primjera kako bi pre-emptive context load mogao izgledati za aplikaciju turističkog agenta u Pythonu:

```python
class TravelAgent:
    def __init__(self):
        # Predučitaj popularna odredišta i njihove informacije
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Dohvati informacije o odredištu iz prethodno učitanog konteksta
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

1. **Inicijalizacija (metoda `__init__`)**: Klasa `TravelAgent` unaprijed učitava rječnik koji sadrži informacije o popularnim destinacijama poput Pariza, Tokija, New Yorka i Sydneya. Ovaj rječnik uključuje detalje kao što su država, valuta, jezik i glavne atrakcije za svaku destinaciju.

2. **Dohvaćanje informacija (metoda `get_destination_info`)**: Kada korisnik postavi upit o određenoj destinaciji, metoda `get_destination_info` dohvaća relevantne informacije iz unaprijed učitanog rječnika konteksta.

Učitavanjem konteksta unaprijed, aplikacija turističkog agenta može brzo odgovoriti na korisničke upite bez potrebe za dohvaćanjem tih informacija iz vanjskog izvora u stvarnom vremenu. To aplikaciju čini učinkovitijom i responzivnijom.

### Pokretanje plana s ciljem prije iteracije

Pokretanje plana s ciljem znači započeti s jasnim ciljem ili željenim ishodom na umu. Definiranjem tog cilja unaprijed, model ga može koristiti kao vodilju kroz iterativni proces. To pomaže osigurati da svaka iteracija približava ostvarivanju željenog ishoda, čineći proces učinkovitijim i fokusiranijim.

Evo primjera kako biste mogli pokrenuti plan putovanja s ciljem prije iteracije za turističkog agenta u Pythonu:

### Scenarij

Turistički agent želi isplanirati prilagođeni odmor za klijenta. Cilj je izraditi itinerar putovanja koji maksimizira zadovoljstvo klijenta na temelju njihovih preferencija i budžeta.

### Koraci

1. Definirati preferencije i budžet klijenta.
2. Pokrenuti inicijalni plan temeljen na tim preferencijama.
3. Iterativno usavršavati plan, optimizirajući za zadovoljstvo klijenta.

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

# Primjer uporabe
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

1. **Inicijalizacija (metoda `__init__`)**: Klasa `TravelAgent` se inicijalizira sa popisom potencijalnih destinacija, od kojih svaka ima atribute poput imena, troška i vrste aktivnosti.

2. **Pokretanje plana (metoda `bootstrap_plan`)**: Ova metoda kreira inicijalni plan putovanja na temelju preferencija i budžeta klijenta. Prolazi kroz popis destinacija i dodaje ih u plan ako se slažu s preferencijama klijenta i odgovaraju unutar budžeta.

3. **Usklađivanje preferencija (metoda `match_preferences`)**: Ova metoda provjerava odgovara li destinacija klijentovim preferencijama.

4. **Iteriranje plana (metoda `iterate_plan`)**: Ova metoda usavršava inicijalni plan pokušavajući zamijeniti svaku destinaciju u planu boljim podudaranjem, uzimajući u obzir klijentove preferencije i ograničenja budžeta.

5. **Izračun troška (metoda `calculate_cost`)**: Ova metoda izračunava ukupni trošak trenutnog plana, uključujući potencijalnu novu destinaciju.

#### Primjer korištenja

- **Inicijalni plan**: Turistički agent kreira početni plan temeljen na klijentovim preferencijama za razgledavanje i budžet od 2000$.
- **Usavršeni plan**: Turistički agent iterira plan, optimizirajući za klijentove preferencije i budžet.

Pokretanjem plana s jasnim ciljem (npr. maksimiziranje zadovoljstva klijenta) i iteriranjem za usavršavanje plana, turistički agent može kreirati prilagođeni i optimizirani itinerar putovanja za klijenta. Ovaj pristup osigurava da plan putovanja od početka odgovara klijentovim preferencijama i budžetu te se poboljšava sa svakom iteracijom.

### Iskorištavanje LLM-a za višerangiranje i ocjenjivanje

Veliki jezični modeli (LLM-i) mogu se koristiti za višerangiranje i ocjenjivanje procjenom relevantnosti i kvalitete dohvaćenih dokumenata ili generiranih odgovora. Evo kako to funkcionira:

**Dohvaćanje:** Početni korak dohvaća skup potencijalnih dokumenata ili odgovora na temelju upita.

**Višerangiranje:** LLM procjenjuje te kandidate i ponovno ih rangira na temelju njihove relevantnosti i kvalitete. Ovaj korak osigurava da se najrelevantnije i najkvalitetnije informacije prikažu prve.

**Ocjenjivanje:** LLM dodjeljuje ocjene svakom kandidatu, odražavajući njihovu relevantnost i kvalitetu. Ovo pomaže u odabiru najboljeg odgovora ili dokumenta za korisnika.

Korištenjem LLM-ova za višerangiranje i ocjenjivanje, sustav može pružiti točnije i kontekstualno relevantnije informacije, poboljšavajući ukupno korisničko iskustvo.

Evo primjera kako bi turistički agent mogao koristiti Veliki jezični model (LLM) za višerangiranje i ocjenjivanje destinacija za putovanje na temelju korisničkih preferencija u Pythonu:

#### Scenarij - Putovanje na temelju preferencija

Turistički agent želi preporučiti najbolje destinacije za putovanje klijentu na temelju njihovih preferencija. LLM će pomoći pri višerangiranju i ocjenjivanju destinacija kako bi se osiguralo da se prikažu najrelevantnije opcije.

#### Koraci:

1. Prikupiti korisničke preferencije.
2. Dohvatiti popis potencijalnih destinacija za putovanje.
3. Koristiti LLM za višerangiranje i ocjenjivanje destinacija na temelju korisničkih preferencija.

Evo kako možete ažurirati prethodni primjer za korištenje Azure OpenAI usluga:

#### Zahtjevi

1. Morate imati Azure pretplatu.
2. Kreirajte Azure OpenAI resurs i nabavite svoj API ključ.

#### Primjer Python koda

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generirajte upit za Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Definirajte zaglavlja i sadržaj za zahtjev
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Pozovite Azure OpenAI API za dobivanje ponovno rangiranih i ocijenjenih destinacija
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Izvadite i vratite preporuke
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

#### Objašnjenje koda - Preference Booker

1. **Inicijalizacija**: Klasa `TravelAgent` se inicijalizira s popisom potencijalnih destinacija za putovanje, od kojih svaka ima atribute poput imena i opisa.

2. **Dobivanje preporuka (metoda `get_recommendations`)**: Ova metoda generira prompt za Azure OpenAI uslugu na temelju korisničkih preferencija te šalje HTTP POST zahtjev Azure OpenAI API-ju za dobivanje višerangiranih i ocijenjenih destinacija.

3. **Generiranje prompta (metoda `generate_prompt`)**: Ova metoda konstruira prompt za Azure OpenAI, uključujući korisničke preferencije i popis destinacija. Prompt usmjerava model da višerangira i ocijeni destinacije na temelju danih preferencija.

4. **API poziv**: Koristi se biblioteka `requests` za slanje HTTP POST zahtjeva na Azure OpenAI API endpoint. Odgovor sadrži višerangirane i ocijenjene destinacije.

5. **Primjer korištenja**: Turistički agent prikuplja korisničke preferencije (npr. interes za razgledavanje i raznoliku kulturu) i koristi Azure OpenAI servis za dobivanje višerangiranih i ocijenjenih preporuka za destinacije za putovanje.

Obavezno zamijenite `your_azure_openai_api_key` stvarnim Azure OpenAI API ključem i `https://your-endpoint.com/...` stvarnim URL-om endpointa vaše Azure OpenAI implementacije.

Korištenjem LLM-a za višerangiranje i ocjenjivanje, turistički agent može pružiti personaliziranije i relevantnije preporuke za putovanja klijentima, poboljšavajući njihovo ukupno iskustvo.

### RAG: Tehnika promptanja vs alat

Retrieval-Augmented Generation (RAG) može biti i tehnika promptanja i alat u razvoju AI agenata. Razumijevanje razlike između ta dva može vam pomoći učinkovitije iskoristiti RAG u vašim projektima.

#### RAG kao tehnika promptanja

**Što je to?**

- Kao tehnika promptanja, RAG uključuje formuliranje specifičnih upita ili promptova za vođenje dohvaćanja relevantnih informacija iz velikog korpusa ili baze podataka. Te informacije se zatim koriste za generiranje odgovora ili akcija.

**Kako radi:**

1. **Formuliranje promptova**: Kreirajte dobro strukturirane promptove ili upite na temelju zadatka ili korisničkog unosa.
2. **Dohvaćanje informacija**: Koristite promptove za pretraživanje relevantnih podataka iz postojeće baze znanja ili skupa podataka.
3. **Generiranje odgovora**: Kombinirajte dohvaćene informacije s generativnim AI modelima za proizvodnju sveobuhvatnog i koherentnog odgovora.

**Primjer u turističkom agentu**:

- Korisnički unos: "Želim posjetiti muzeje u Parizu."
- Prompt: "Pronađi najbolje muzeje u Parizu."
- Dohvaćene informacije: Detalji o Louvre muzeju, Musée d'Orsay itd.
- Generirani odgovor: "Evo nekoliko vrhunskih muzeja u Parizu: Louvre muzej, Musée d'Orsay i Centre Pompidou."

#### RAG kao alat

**Što je to?**

- Kao alat, RAG je integrirani sustav koji automatizira proces dohvaćanja i generiranja, olakšavajući programerima implementaciju složenih AI funkcionalnosti bez ručnog kreiranja promptova za svaki upit.

**Kako radi:**

1. **Integracija**: Ugradi RAG u arhitekturu AI agenta, omogućujući mu automatsko upravljanje zadacima dohvaćanja i generiranja.
2. **Automatizacija**: Alat upravlja cijelim procesom, od primanja korisničkog unosa do generiranja konačnog odgovora, bez potrebe za eksplicitnim promptovima za svaki korak.
3. **Učinkovitost**: Povećava performanse agenta pojednostavljivanjem procesa dohvaćanja i generiranja, omogućujući brže i točnije odgovore.

**Primjer u turističkom agentu**:

- Korisnički unos: "Želim posjetiti muzeje u Parizu."
- RAG alat: Automatski dohvaća informacije o muzejima i generira odgovor.
- Generirani odgovor: "Evo nekoliko vrhunskih muzeja u Parizu: Louvre muzej, Musée d'Orsay i Centre Pompidou."

### Usporedba

| Aspekt                 | Tehnika promptanja                                        | Alat                                                  |
|------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| **Ručni vs Automatski**| Ručno formuliranje promptova za svaki upit.                | Automatizirani proces za dohvaćanje i generiranje.     |
| **Kontrola**           | Pruža veću kontrolu nad procesom dohvaćanja.               | Pojednostavljuje i automatizira dohvaćanje i generiranje.|
| **Fleksibilnost**      | Omogućuje prilagođene promptove prema specifičnim potrebama.| Učinkovitiji za velike implementacije.                 |
| **Složeniost**         | Zahtijeva izradu i prilagodbu promptova.                   | Lakše za integraciju u arhitekturu AI agenta.          |

### Praktični primjeri

**Primjer tehnike promptanja:**

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

Procjena relevantnosti ključan je aspekt performansi AI agenta. Osigurava da su informacije koje agent dohvaća i generira prikladne, točne i korisne za korisnika. Pogledajmo kako procijeniti relevantnost u AI agentima, uključujući praktične primjere i tehnike.

#### Ključni pojmovi u procjeni relevantnosti

1. **Svijest o kontekstu**:
   - Agent mora razumjeti kontekst korisničkog upita kako bi dohvaćao i generirao relevantne informacije.
   - Primjer: Ako korisnik pita za "najbolje restorane u Parizu," agent treba uzeti u obzir korisnikove preferencije, poput vrste kuhinje i budžeta.

2. **Točnost**:
   - Informacije koje agent pruža trebaju biti činjenično točne i ažurirane.
   - Primjer: Preporučivanje restorana koji su trenutno otvoreni i imaju dobre ocjene, a ne zastarjelih ili zatvorenih opcija.

3. **Korisnička namjera**:
   - Agent treba zaključiti korisnikovu namjeru iza upita kako bi pružio najrelevantnije informacije.
   - Primjer: Ako korisnik pita za "pristupačne hotele," agent treba prioritetno ponuditi povoljne opcije.

4. **Povratna sprega**:
   - Kontinuirano prikupljanje i analiza korisničkih povratnih informacija pomažu agentu da usavrši procjenu relevantnosti.
   - Primjer: Uključivanje korisničkih ocjena i povratnih informacija o prethodnim preporukama za poboljšanje budućih odgovora.

#### Praktične tehnike za procjenu relevantnosti

1. **Ocjenjivanje relevantnosti**:
   - Dodijelite ocjenu relevantnosti svakom dohvaćenom stavkom na temelju toga koliko dobro odgovara korisničkom upitu i preferencijama.
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
   - Izdvojite nerelevantne stavke i rangirajte preostale prema njihovim ocjenama relevantnosti.
   - Primjer:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Vraća top 10 relevantnih stavki
     ```

3. **Obrada prirodnog jezika (NLP)**:
   - Koristite NLP tehnike za razumijevanje korisničkog upita i dohvaćanje relevantnih informacija.
   - Primjer:

     ```python
     def process_query(query):
         # Koristite NLP za izdvajanje ključnih informacija iz korisničkog upita
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integracija korisničkih povratnih informacija**:
   - Prikupljajte povratne informacije korisnika o danim preporukama i koristite ih za prilagodbu budućih procjena relevantnosti.
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

#### Primjer: Procjena relevantnosti u turističkom agentu

Evo praktičnog primjera kako turistički agent može procijeniti relevantnost preporuka za putovanja:

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
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Pretraživanje s namjerom

Pretraživanje s namjerom podrazumijeva razumijevanje i tumačenje osnovne svrhe ili cilja iza korisničkog upita kako bi se dohvatila i generirala najrelevantnija i najkorisnija informacija. Ovaj pristup ide dalje od pukog podudaranja ključnih riječi i fokusira se na razumijevanje stvarnih potreba i konteksta korisnika.

#### Ključni pojmovi u pretraživanju s namjerom

1. **Razumijevanje korisničke namjere**:
   - Korisnička namjera može se podijeliti u tri glavne vrste: informativna, navigacijska i transakcijska.
     - **Informativna namjera**: Korisnik traži informacije o nekoj temi (npr. "Koji su najbolji muzeji u Parizu?").
     - **Navigacijska namjera**: Korisnik želi doći do određene web stranice ili stranice (npr. "Službena stranica Louvre muzeja").
     - **Transakcijska namjera**: Korisnik želi obaviti transakciju, poput rezervacije leta ili kupovine (npr. "Rezerviraj let za Pariz").

2. **Svijest o kontekstu**:
   - Analiza konteksta korisničkog upita pomaže u preciznom identificiranju njihove namjere. To uključuje razmatranje prethodnih interakcija, korisničkih preferencija i specifičnih detalja trenutnog upita.

3. **Obrada prirodnog jezika (NLP)**:
   - NLP tehnike se koriste za razumijevanje i tumačenje upita na prirodnom jeziku koje korisnici daju. To uključuje zadatke poput prepoznavanja entiteta, analize sentimenta i analize upita.

4. **Personalizacija**:
   - Personalizacija rezultata pretraživanja na temelju povijesti korisnika, preferencija i povratnih informacija poboljšava relevantnost dohvaćenih informacija.

#### Praktični primjer: Pretraživanje s namjerom u turističkom agentu

Pogledajmo primjer turističkog agenta kako bismo vidjeli kako se može implementirati pretraživanje s namjerom.

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
       return personalized[:10]  # Vraćanje 10 najboljih personaliziranih rezultata
   ```

5. **Primjer korištenja**

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

Agent za generiranje koda koristi generativne AI modele za pisanje i izvršavanje koda. Ovi agenti mogu rješavati složene probleme, automatizirati zadatke i pružati vrijedne uvide generiranjem i izvođenjem koda na raznim programskim jezicima.

#### Praktične primjene

1. **Automatizirano generiranje koda**: Generirajte dijelove koda za specifične zadatke, poput analize podataka, web scrapinga ili strojnog učenja.
2. **SQL kao RAG**: Koristite SQL upite za dohvat i manipulaciju podacima iz baza podataka.
3. **Rješavanje problema**: Kreirajte i izvršite kod za rješavanje specifičnih problema, poput optimizacije algoritama ili analize podataka.

#### Primjer: Agent za generiranje koda za analizu podataka

Zamislite da dizajnirate agenta za generiranje koda. Evo kako bi to moglo funkcionirati:

1. **Zadatak**: Analizirati skup podataka kako bi se identificirali trendovi i obrasci.
2. **Koraci**:
   - Učitati skup podataka u alat za analizu podataka.
   - Generirati SQL upite za filtriranje i agregaciju podataka.
   - Izvršiti upite i dohvatiti rezultate.
   - Koristiti rezultate za generiranje vizualizacija i uvida.
3. **Potrebni resursi**: Pristup skupu podataka, alati za analizu podataka i SQL mogućnosti.
4. **Iskustvo**: Koristiti rezultate prethodnih analiza za poboljšanje točnosti i relevantnosti budućih analiza.

### Primjer: Agent za generiranje koda - Putnički agent

U ovom primjeru dizajnirat ćemo agenta za generiranje koda, Putničkog agenta, koji pomaže korisnicima u planiranju putovanja generiranjem i izvršavanjem koda. Ovaj agent može obavljati zadatke poput dohvaćanja opcija za putovanje, filtriranja rezultata i sastavljanja itinerera koristeći generativnu AI.

#### Pregled agenta za generiranje koda

1. **Prikupljanje korisničkih preferencija**: Prikuplja korisničke unose poput odredišta, datuma putovanja, budžeta i interesa.
2. **Generiranje koda za dohvaćanje podataka**: Generira dijelove koda za dohvaćanje podataka o letovima, hotelima i atrakcijama.
3. **Izvršavanje generiranog koda**: Pokreće generirani kod za dohvaćanje informacija u stvarnom vremenu.
4. **Generiranje itinerera**: Sastavlja dohvaćene podatke u personalizirani plan putovanja.
5. **Prilagodba prema povratnim informacijama**: Prima povratne informacije korisnika i po potrebi regenerira kod za preciziranje rezultata.

#### Implementacija korak po korak

1. **Prikupljanje korisničkih preferencija**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generiranje koda za dohvaćanje podataka**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Primjer: Generirajte kod za pretraživanje letova na temelju korisničkih preferencija
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Primjer: Generirajte kod za pretraživanje hotela
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

5. **Prilagodba prema povratnim informacijama**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Prilagodite postavke na temelju povratnih informacija korisnika
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Ponovno generirajte i izvedite kod s ažuriranim postavkama
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Iskorištavanje svijesti o okolini i rezoniranje

Temeljeno na shemi tablice može značajno unaprijediti proces generiranja upita iskorištavanjem svijesti o okolini i rezoniranja.

Evo primjera kako se to može učiniti:

1. **Razumijevanje sheme**: Sustav će razumjeti shemu tablice i koristiti te informacije kao osnovu za generiranje upita.
2. **Prilagodba prema povratnim informacijama**: Sustav će prilagoditi korisničke preferencije na temelju povratnih informacija i razmotriti koja polja u shemi treba ažurirati.
3. **Generiranje i izvršavanje upita**: Sustav će generirati i izvršiti upite za dohvat ažuriranih podataka o letovima i hotelima temeljem novih preferencija.

Evo ažuriranog primjera Python koda koji uključuje ove koncepte:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Prilagodite postavke na temelju povratnih informacija korisnika
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Razumijevanje na temelju sheme za prilagodbu drugih povezanih postavki
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
    # Generirajte kod za dohvat podataka o letovima na temelju ažuriranih postavki
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generirajte kod za dohvat podataka o hotelima na temelju ažuriranih postavki
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulirajte izvršavanje koda i vratite lažne podatke
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generirajte itinerar na temelju letova, hotela i atrakcija
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Primjer sheme
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Primjer korištenja
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Ponovno generirajte i izvršite kod s ažuriranim postavkama
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Objašnjenje - Rezervacija na temelju povratnih informacija

1. **Poznavanje sheme**: Rječnik `schema` definira kako se preferencije trebaju prilagoditi na temelju povratnih informacija. Uključuje polja poput `favorites` i `avoid` s pripadajućim prilagodbama.
2. **Prilagodba preferencija (metoda `adjust_based_on_feedback`)**: Ova metoda prilagođava preferencije na temelju korisničkih povratnih informacija i sheme.
3. **Prilagodbe temeljene na okolini (metoda `adjust_based_on_environment`)**: Ova metoda prilagođava promjene temeljene na shemi i povratnim informacijama.
4. **Generiranje i izvršavanje upita**: Sustav generira kod za dohvat ažuriranih podataka o letovima i hotelima na temelju prilagođenih preferencija i simulira izvođenje tih upita.
5. **Generiranje itinerera**: Sustav stvara ažurirani itinerer na temelju novootkrivenih podataka o letu, hotelu i atrakcijama.

Uključivanjem svijesti o okolini i rezoniranjem temeljenim na shemi, sustav može generirati preciznije i relevantnije upite, što vodi do boljih preporuka za putovanja i personaliziranijeg korisničkog iskustva.

### Korištenje SQL-a kao tehnike Retrieval-Augmented Generation (RAG)

SQL (Strukturirani jezik upita) moćan je alat za interakciju s bazama podataka. Kada se koristi kao dio pristupa Retrieval-Augmented Generation (RAG), SQL može dohvatiti relevantne podatke iz baza kako bi obavijestio i generirao odgovore ili radnje u AI agentima. Pogledajmo kako se SQL može koristiti kao RAG tehnika u kontekstu Putničkog agenta.

#### Ključni pojmovi

1. **Interakcija s bazom podataka**:
   - SQL se koristi za upite prema bazama, dohvat relevantnih informacija i manipulaciju podacima.
   - Primjer: Dohvat detalja o letovima, informacijama o hotelima i atrakcijama iz putničke baze.

2. **Integracija s RAG**:
   - SQL upiti se generiraju na temelju korisničkih unosa i preferencija.
   - Dohvaćeni podaci se zatim koriste za generiranje personaliziranih preporuka ili radnji.

3. **Dinamičko generiranje upita**:
   - AI agent generira dinamičke SQL upite temeljene na kontekstu i potrebama korisnika.
   - Primjer: Prilagođavanje SQL upita za filtriranje rezultata prema budžetu, datumima i interesima.

#### Primjene

- **Automatizirano generiranje koda**: Generiranje dijelova koda za specifične zadatke.
- **SQL kao RAG**: Korištenje SQL upita za manipulaciju podacima.
- **Rješavanje problema**: Kreiranje i izvođenje koda za rješavanje problema.

**Primjer**:
Agent za analizu podataka:

1. **Zadatak**: Analizirati skup podataka kako bi se pronašli trendovi.
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

#### Primjeri SQL upita

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

Iskorištavanjem SQL-a kao dijela tehnike Retrieval-Augmented Generation (RAG), AI agenti poput Putničkog agenta mogu dinamički dohvaćati i koristiti relevantne podatke za pružanje točnih i personaliziranih preporuka.

### Primjer metakognicije

Za demonstraciju implementacije metakognicije, kreirat ćemo jednostavnog agenta koji *reflektira svoj proces donošenja odluka* dok rješava problem. U ovom primjeru izgradit ćemo sustav u kojem agent pokušava optimizirati odabir hotela, ali potom evaluira vlastito rezoniranje i prilagođava strategiju kad napravi pogreške ili donesene odluke nisu optimalne.

Simulirat ćemo to na osnovnom primjeru gdje agent bira hotele na temelju kombinacije cijene i kvalitete, ali „reflektira“ o svojim odlukama i sukladno tome se prilagođava.

#### Kako ovo ilustrira metakogniciju:

1. **Početna odluka**: Agent bira najjeftiniji hotel, bez razumijevanja utjecaja kvalitete.
2. **Refleksija i evaluacija**: Nakon početnog izbora, agent provjerava je li hotel "loš" izbor koristeći povratne informacije korisnika. Ako otkrije da je kvaliteta hotela bila preniska, reflektira o svom rezoniranju.
3. **Prilagodba strategije**: Agent prilagođava svoju strategiju temeljem refleksije i prelazi s "najjeftinijeg" na "najkvalitetniji", čime poboljšava proces donošenja odluka u budućim iteracijama.

Evo jednog primjera:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Sprema prethodno odabrane hotele
        self.corrected_choices = []  # Sprema ispravljene izbore
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
        # Pretpostavimo da imamo povratne informacije korisnika koje nam kažu je li posljednji izbor bio dobar ili ne
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Prilagodi strategiju ako prethodni izbor nije bio zadovoljavajući
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

# Simuliraj popis hotela (cijena i kvaliteta)
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

# Korak 2: Agent razmišlja o izboru i po potrebi prilagođava strategiju
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Korak 3: Agent ponovno preporučuje, ovaj put koristeći prilagođenu strategiju
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Metakognitivne sposobnosti agenata

Ključna točka je sposobnost agenta da:
- Evaluira svoje prethodne izbore i proces donošenja odluka.
- Prilagodi strategiju na temelju te refleksije, tj. metakognicija u akciji.

Ovo je jednostavan oblik metakognicije gdje je sustav sposoban prilagoditi svoj proces rezoniranja na temelju unutarnjih povratnih informacija.

### Zaključak

Metakognicija je moćan alat koji može značajno unaprijediti mogućnosti AI agenata. Uključivanjem metakognitivnih procesa, možete dizajnirati agente koji su inteligentniji, prilagodljiviji i učinkovitiji. Iskoristite dodatne resurse za daljnje istraživanje fascinantnog svijeta metakognicije u AI agentima.

### Imate dodatnih pitanja o obrascu dizajna metakognicije?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) da se povežete s drugim učenicima, sudjelujete na radnim satima i dobijete odgovore na pitanja o AI agentima.

## Prethodna lekcija

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Sljedeća lekcija

[AI Agents in Production](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->