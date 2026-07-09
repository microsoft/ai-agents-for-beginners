[![Večagentno oblikovanje](../../../translated_images/sl/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Kliknite na sliko zgoraj za ogled videa te lekcije)_
# Metakognicija v AI agentih

## Uvod

Dobrodošli na lekciji o metakogniciji v AI agentih! To poglavje je namenjeno začetnikom, ki jih zanima, kako lahko AI agenti razmišljajo o lastnih miselnih procesih. Ob koncu te lekcije boste razumeli ključne pojme in boste opremljeni s praktičnimi primeri za uporabo metakognicije pri oblikovanju AI agentov.

## Cilji učenja

Po končani tej lekciji boste znali:

1. Razumeti posledice zank mišljenja v definicijah agentov.
2. Uporabiti tehnike načrtovanja in ocenjevanja za pomoč agentom pri samopopravku.
3. Ustvariti svoje agente, ki so sposobni manipulirati s kodo za opravljanje nalog.

## Uvod v metakognicijo

Metakognicija se nanaša na višje miselne procese, ki vključujejo razmišljanje o lastnem razmišljanju. Za AI agente to pomeni sposobnost ocenjevanja in prilagajanja svojih dejanj na podlagi samo-zavedanja in preteklih izkušenj. Metakognicija ali "razmišljanje o razmišljanju" je pomemben koncept pri razvoju agentnih AI sistemov. Vključuje zavedanje AI sistemov o lastnih notranjih procesih ter sposobnost nadzora, regulacije in prilagajanja svojega vedenja. Tako kot mi, ko "preberemo sobo" ali pogledamo problem. To samo-zavedanje lahko pomaga AI sistemom sprejemati boljše odločitve, prepoznavati napake in izboljševati svojo učinkovitost skozi čas – kar spet povezuje k Turingovemu testu in razpravi, ali bo AI prevzel nadzor.

V kontekstu agentnih AI sistemov lahko metakognicija pomaga reševati več izzivov, kot so:
- Preglednost: Zagotoviti, da lahko AI sistemi pojasnijo svoje razlage in odločitve.
- Razmišljanje: Izboljšati sposobnost AI sistemov za sintezo informacij in sprejemanje tehtnih odločitev.
- Prilagodljivost: Omogočiti AI sistemom prilagajanje novim okoljem in spreminjajočim se razmeram.
- Percepcija: Izboljšati natančnost AI sistemov pri prepoznavanju in interpretaciji podatkov iz okolja.

### Kaj je metakognicija?

Metakognicija ali "razmišljanje o razmišljanju" je višji miselni proces, ki vključuje samo-zavedanje in samo-regulacijo lastnih kognitivnih procesov. Na področju AI metakognicija omogoča agentom, da ocenijo in prilagodijo svoje strategije in dejanja, kar vodi do izboljšanih sposobnosti reševanja problemov in sprejemanja odločitev. Z razumevanjem metakognicije lahko oblikujete AI agente, ki niso samo bolj inteligentni, ampak tudi bolj prilagodljivi in učinkoviti. V pravi metakogniciji bi AI jasno razmišljal o svojem lastnem razmišljanju.

Primer: „Prednostno sem izbral cenejše lete, ker... Morda zamujam na direktne lete, zato bom še enkrat preveril.“
Sledenje temu, kako ali zakaj je izbral določeno pot.
- Ugotavljanje, da je naredil napake, ker je preveč zaupal uporabnikovim preferencam od prej, zato spreminja svojo strategijo odločanja, ne le končnega priporočila.
- Diagnostika vzorcev, kot na primer: „Kadar uporabnik omeni 'preveč gneče', ne bi smel le odstraniti določenih znamenitosti, ampak tudi premisliti, da je moja metoda izbire 'top znamenitosti' napačna, če vedno rangiram po priljubljenosti.“

### Pomen metakognicije v AI agentih

Metakognicija ima ključno vlogo pri oblikovanju AI agentov iz več razlogov:

![Pomen metakognicije](../../../translated_images/sl/importance-of-metacognition.b381afe9aae352f7.webp)

- Samorefleksija: Agenti lahko ocenijo svojo uspešnost in prepoznajo področja za izboljšave.
- Prilagodljivost: Agenti lahko prilagajajo svoje strategije na podlagi preteklih izkušenj in spreminjajočih se okolij.
- Popravljanje napak: Agenti lahko samostojno zaznavajo in popravljajo napake, kar vodi do natančnejših rezultatov.
- Upravljanje virov: Agenti lahko optimizirajo uporabo virov, kot sta čas in računalniška moč, z načrtovanjem in ocenjevanjem svojih dejanj.

## Komponente AI agenta

Preden se poglobimo v metakognitivne procese, je bistveno razumeti osnovne komponente AI agenta. AI agent običajno sestavljajo:

- Persona: Osebnost in značilnosti agenta, ki določajo, kako sodeluje z uporabniki.
- Orodja: Zmožnosti in funkcije, ki jih agent lahko opravlja.
- Spretnosti: Znanje in strokovnost, ki jih agent poseduje.

Te komponente sodelujejo pri ustvarjanju "enote strokovnosti", ki lahko izvaja specifične naloge.

**Primer**:
Predstavljajte si potovalnega agenta, agent storitve, ki ne le načrtuje vaše počitnice, ampak tudi prilagaja svojo pot glede na podatke v realnem času in pretekle izkušnje popotnikov.

### Primer: Metakognicija v potovalnem agentu

Predstavljajte si, da oblikujete potovalno storitev, ki jo poganja AI. Ta agent "Potovalni agent" pomaga uporabnikom pri načrtovanju počitnic. Za vključitev metakognicije potrebuje Potovalni agent sposobnost ocenjevanja in prilagajanja svojih dejanj na podlagi samo-zavedanja in preteklih izkušenj. Tako bi lahko metakognicija igrala vlogo:

#### Trenutna naloga

Trenutna naloga je pomagati uporabniku načrtovati potovanje v Pariz.

#### Koraki za dokončanje naloge

1. **Zbiranje uporabnikovih preferenc**: Vprašajte uporabnika o datumih potovanja, proračunu, zanimanjih (npr. muzeji, kulinarika, nakupovanje) in posebnih zahtevah.
2. **Iskanje informacij**: Poiščite možnosti letov, nastanitev, znamenitosti in restavracij, ki ustrezajo uporabnikovim preferencam.
3. **Generiranje priporočil**: Ponudite personaliziran načrt poti z informacijami o letih, rezervacijah hotela in predlaganimi aktivnostmi.
4. **Prilagoditev na podlagi povratnih informacij**: Povprašajte uporabnika o odzivih na priporočila in naredite potrebne spremembe.

#### Potrebni viri

- Dostop do baz podatkov o letih in hotelskih rezervacijah.
- Informacije o pariških znamenitostih in restavracijah.
- Podatki o povratnih informacijah uporabnikov iz prejšnjih interakcij.

#### Izkušnje in samorefleksija

Potovalni agent uporablja metakognicijo za ocenjevanje svoje uspešnosti in učenje iz preteklih izkušenj. Na primer:

1. **Analiza povratnih informacij uporabnikov**: Potovalni agent pregleda povratne informacije uporabnikov, da ugotovi, katera priporočila so bila dobro sprejeta in katera ne. Nato ustrezno prilagodi svoje prihodnje predloge.
2. **Prilagodljivost**: Če je uporabnik prej izrazila nestrinjanje z gnečo na določenih krajih, bo Potovalni agent v prihodnje izogibal priporočanju priljubljenih turističnih točk v najbolj obremenjenih urah.
3. **Popravljanje napak**: Če je Potovalni agent naredil napako pri prejšnji rezervaciji, na primer predlagal hotel, ki je bil že popolnoma zaseden, se nauči bolj rigorozno preverjati razpoložljivost pred dajanjem priporočil.

#### Praktični primer za razvijalce

Tukaj je poenostavljen primer kode, ki vključuje metakognicijo v Potovalnem agentu:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Iskanje letov, hotelov in znamenitosti glede na preference
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
        # Analiza povratnih informacij in prilagoditev prihodnjih priporočil
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Primer uporabe
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

#### Zakaj je metakognicija pomembna

- **Samorefleksija**: Agenti lahko analizirajo svojo uspešnost in prepoznajo področja za izboljšave.
- **Prilagodljivost**: Agenti lahko spreminjajo strategije glede na povratne informacije in spremenjene razmere.
- **Popravljanje napak**: Agenti lahko samostojno zaznajo in popravijo napake.
- **Upravljanje virov**: Agenti lahko optimizirajo uporabo virov, kot sta čas in računalniška moč.

Z vključitvijo metakognicije lahko Potovalni agent ponudi bolj osebna in natančna potovalna priporočila ter izboljša uporabniško izkušnjo.

---

## 2. Načrtovanje pri agentih

Načrtovanje je ključen del vedenja AI agenta. Vključuje opredelitev korakov, potrebnih za dosego cilja, ob upoštevanju trenutnega stanja, virov in možnih ovir.

### Elementi načrtovanja

- **Trenutna naloga**: Jasno opredelite nalogo.
- **Koraki za dokončanje naloge**: Razdelite nalogo na obvladljive korake.
- **Potrebni viri**: Ugotovite potrebne vire.
- **Izkušnje**: Uporabite pretekle izkušnje za načrtovanje.

**Primer**:
Tukaj so koraki, ki jih mora Potovalni agent opraviti, da učinkovito pomaga uporabniku načrtovati potovanje:

### Koraki za Potovalni agent

1. **Zbiranje uporabnikovih preferenc**
   - Vprašajte uporabnika o podrobnostih glede datumov potovanja, proračun, zanimanj in posebnih zahtevah.
   - Primeri: "Kdaj nameravate potovati?" "Kolikšen je vaš proračun?" "Katere aktivnosti vas zanimajo med počitnicami?"

2. **Iskanje informacij**
   - Poiščite ustrezne možnosti potovanja na podlagi uporabnikovih preferenc.
   - **Leti**: Poiščite razpoložljive lete znotraj uporabnikovega proračuna in želenih datumov potovanja.
   - **Nastanitve**: Najdite hotele ali najemne prostore, ki ustrezajo uporabnikovim preferencam glede lokacije, cene in zmogljivosti.
   - **Znamenitosti in restavracije**: Prepoznajte priljubljene znamenitosti, aktivnosti in restavracije, ki ustrezajo uporabnikovim interesom.

3. **Generiranje priporočil**
   - Združite pridobljene informacije v personaliziran načrt poti.
   - Podajte podrobnosti, kot so možnosti letov, rezervacije hotelov in predlagane aktivnosti, in prilagodite priporočila uporabnikovim željam.

4. **Predstavitev načrta uporabniku**
   - Delite predlagan načrt poti z uporabnikom za pregled.
   - Primer: "Tukaj je predlog načrta za vaše potovanje v Pariz. Vključuje podatke o letih, hotelskih rezervacijah in seznam priporočil za aktivnosti in restavracije. Sporočite mi svoje mnenje!"

5. **Zbiranje povratnih informacij**
   - Povprašajte uporabnika za povratne informacije o predlaganem načrtu.
   - Primeri: "Všeč so vam možnosti letov?" "Ali je hotel primeren za vaše potrebe?" "Ali bi radi dodali ali odstranili katero aktivnost?"

6. **Prilagoditev na podlagi povratnih informacij**
   - Spremenite načrt poti glede na uporabnikove povratne informacije.
   - Naredite potrebne spremembe glede letov, nastanitve in priporočil za aktivnosti, da bolje ustrezajo uporabnikovim željam.

7. **Končna potrditev**
   - Predstavite posodobljen načrt uporabniku za dokončno potrditev.
   - Primer: "Naredil sem prilagoditve glede na vaše povratne informacije. Tukaj je posodobljen načrt. Ali je vse v redu?"

8. **Rezervacija in potrditev**
   - Ko uporabnik potrdi načrt, nadaljujte z rezervacijo letov, nastanitev in morebitnih že načrtovanih aktivnosti.
   - Pošljite uporabniku potrditvene podatke.

9. **Nadaljnja podpora**
   - Bodite na voljo za pomoč uporabniku pri morebitnih spremembah ali dodatnih željah pred in med potovanjem.
   - Primer: "Če boste potrebovali dodatno pomoč med potovanjem, se kadar koli obrnite name!"

### Primer interakcije

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

# Primer uporabe v zahtevi za booanje
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

## 3. Korektivni RAG sistem

Najprej začnimo z razumevanjem razlike med RAG orodjem in predhodnim nalaganjem konteksta.

![RAG proti nalaganju konteksta](../../../translated_images/sl/rag-vs-context.9eae588520c00921.webp)

### Generacija z nadgradnjo s pridobivanjem (RAG)

RAG združuje sistem za pridobivanje informacij z generativnim modelom. Ko se izvede poizvedba, sistem za pridobivanje poišče ustrezne dokumente ali podatke iz zunanjega vira, te pridobljene informacije pa se uporabijo kot dodatek vhodnim podatkom za generativni model. To pomaga modelu ustvarjati bolj natančne in kontekstualno relevantne odgovore.

V RAG sistemu agent pridobi ustrezne informacije iz zbirke znanja in jih uporabi za ustvarjanje primernih odgovorov ali dejanj.

### Korektivni RAG pristop

Korektivni RAG pristop se osredotoča na uporabo RAG tehnik za odpravljanje napak in izboljšanje natančnosti AI agentov. To vključuje:

1. **Tehniko usmerjanja poizvedb**: Uporaba specifičnih pozivov za usmerjanje agenta pri pridobivanju relevantnih informacij.
2. **Orodja**: Uvajanje algoritmov in mehanizmov, ki omogočajo agentu ocenjevanje relevantnosti pridobljenih informacij in ustvarjanje natančnih odgovorov.
3. **Evalvacija**: Neprestano ocenjevanje uspešnosti agenta in prilagajanje za izboljšanje natančnosti in učinkovitosti.

#### Primer: Korektivni RAG v iskalnem agentu

Predstavljajte si iskalni agent, ki pridobiva informacije z interneta za odgovarjanje na uporabniške poizvedbe. Korektivni RAG pristop bi lahko vključeval:

1. **Tehniko usmerjanja poizvedb**: Oblikovanje iskalnih poizvedb na podlagi vnosa uporabnika.
2. **Orodja**: Uporaba algoritmov za obdelavo naravnega jezika in strojno učenje za razvrščanje in filtriranje iskalnih rezultatov.
3. **Evalvacija**: Analiza povratnih informacij uporabnikov za prepoznavanje in odpravo netočnosti v pridobljenih informacijah.

### Korektivni RAG v Potovalnem agentu

Korektivni RAG (Generacija z nadgradnjo s pridobivanjem) izboljšuje sposobnost AI za pridobivanje in ustvarjanje informacij, hkrati pa popravlja morebitne netočnosti. Poglejmo, kako lahko Potovalni agent uporabi pristop Korektivni RAG za zagotavljanje natančnejših in relevantnejših potovalnih priporočil.

To vključuje:

- **Tehnika usmerjanja poizvedb:** Uporaba specifičnih pozivov za usmerjanje agenta pri pridobivanju relevantnih informacij.
- **Orodja:** Uvajanje algoritmov in mehanizmov, ki omogočajo agentu ocenjevanje relevantnosti pridobljenih informacij in ustvarjanje natančnih odgovorov.
- **Evalvacija:** Neprestano ocenjevanje uspešnosti agenta in prilagajanje za izboljšanje natančnosti in učinkovitosti.

#### Koraki za implementacijo Korektivnega RAG v Potovalnem agentu

1. **Začetna interakcija z uporabnikom**
   - Potovalni agent zbere začetne preference uporabnika, kot so cilj, datumi potovanja, proračun in zanimanja.
   - Primer:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Pridobivanje informacij**
   - Potovalni agent pridobi informacije o letih, nastanitvah, znamenitostih in restavracijah glede na uporabnikove preference.
   - Primer:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generiranje začetnih priporočil**
   - Potovalni agent uporabi pridobljene informacije za ustvarjanje personaliziranega načrta poti.
   - Primer:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Zbiranje povratnih informacij uporabnika**
   - Potovalni agent povpraša uporabnika za povratne informacije o začetnih priporočilih.
   - Primer:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Proces Korektivnega RAG**
   - **Tehnika usmerjanja poizvedb**: Potovalni agent oblikuje nove iskalne poizvedbe na podlagi povratnih informacij uporabnika.
     - Primer:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Orodja**: Potovalni agent uporablja algoritme za rangiranje in filtriranje novih iskalnih rezultatov, poudarjajoč relevantnost glede na povratne informacije uporabnika.
     - Primer:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Evalvacija**: Potovalni agent nenehno ocenjuje relevantnost in natančnost svojih priporočil z analizo povratnih informacij uporabnikov ter izvaja potrebne prilagoditve.
     - Primer:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Praktični primer

Tukaj je poenostavljen primer kode v Pythonu, ki vključuje pristop Korektivni RAG v Potovalnem agentu:

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

# Primer uporabe
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

### Predhodno nalaganje konteksta


Prepoznavno nalaganje konteksta vključuje nalaganje ustreznih kontekstualnih ali ozadnih informacij v model pred obdelavo poizvedbe. To pomeni, da ima model dostop do teh informacij že od začetka, kar mu lahko pomaga generirati bolj informirane odgovore, ne da bi moralo med procesom pridobivati dodatne podatke.

Tukaj je poenostavljen primer, kako bi lahko izgledalo prepoznavno nalaganje konteksta za aplikacijo potovalnega agenta v Pythonu:

```python
class TravelAgent:
    def __init__(self):
        # Predhodno naloži priljubljene destinacije in njihove informacije
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Pridobi informacije o destinaciji iz predhodno naloženega konteksta
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Primer uporabe
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Razlaga

1. **Inicializacija (`__init__` metoda)**: Razred `TravelAgent` predhodno naloži slovar, ki vsebuje informacije o priljubljenih destinacijah, kot so Pariz, Tokio, New York in Sydney. Ta slovar vključuje podrobnosti, kot so država, valuta, jezik in glavne znamenitosti vsake destinacije.

2. **Pridobivanje informacij (`get_destination_info` metoda)**: Ko uporabnik vpraša o določeni destinaciji, metoda `get_destination_info` pridobi ustrezne informacije iz predhodno naloženega kontekstualnega slovarja.

S predhodnim nalaganjem konteksta lahko aplikacija potovalnega agenta hitro odgovori na uporabnikove poizvedbe, brez potrebe po pridobivanju teh informacij iz zunanjega vira v realnem času. To naredi aplikacijo bolj učinkovito in odzivno.

### Inicializacija načrta z ciljem pred iteracijo

Inicializacija načrta s ciljem vključuje začetek z jasnim ciljem ali želenim rezultatom. Z opredelitvijo tega cilja vnaprej lahko model uporabi ta cilj kot vodilo skozi iterativni proces. To zagotavlja, da se vsaka iteracija približuje doseganju želenega rezultata, kar proces naredi učinkovitejši in bolj usmerjen.

Tukaj je primer, kako lahko inicializirate potovalni načrt z določenim ciljem pred iteracijo za potovalnega agenta v Pythonu:

### Scenarij

Potovalni agent želi načrtovati prilagojeno počitnice za stranko. Cilj je ustvariti potovalni načrt, ki maksimizira zadovoljstvo stranke glede na njihove preference in proračun.

### Koraki

1. Določite preference in proračun stranke.
2. Inicializirajte začetni načrt na osnovi teh preferenc.
3. Iterirajte za izboljšanje načrta in optimizacijo zadovoljstva stranke.

#### Python koda

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

# Primer uporabe
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

#### Razlaga kode

1. **Inicializacija (`__init__` metoda)**: Razred `TravelAgent` se inicializira s seznamom potencialnih destinacij, kjer ima vsaka destinacija atribute, kot so ime, cena in tip aktivnosti.

2. **Inicializacija načrta (`bootstrap_plan` metoda)**: Ta metoda ustvari začetni potovalni načrt na podlagi strankinih preferenc in proračuna. Preišče seznam destinacij in jih doda v načrt, če ustrezajo preferencam in so znotraj proračuna.

3. **Ujemanje preferenc (`match_preferences` metoda)**: Ta metoda preveri, ali destinacija ustreza strankinim preferencam.

4. **Iteracija načrta (`iterate_plan` metoda)**: Ta metoda izboljša začetni načrt tako, da poskuša zamenjati vsako destinacijo z boljšo možnostjo, pri tem pa upošteva strankine preference in omejitve proračuna.

5. **Izračun stroškov (`calculate_cost` metoda)**: Ta metoda izračuna skupne stroške trenutnega načrta, vključno z morebitno novo destinacijo.

#### Primer uporabe

- **Začetni načrt**: Potovalni agent izdela začetni načrt na podlagi strankinih preferenc glede ogleda znamenitosti in proračuna 2000 $.
- **Izboljšan načrt**: Potovalni agent iterira načrt, da optimizira glede na preference in proračun stranke.

Z inicializacijo načrta z jasnim ciljem (npr. maksimalno zadovoljstvo stranke) in iterativnim izboljševanjem načrta lahko potovalni agent ustvari prilagojen in optimiziran potovalni načrt za stranko. Ta pristop zagotavlja, da se načrt potovanja od začetka usklajuje s strankinimi preferencami in proračunom ter se izboljšuje z vsako iteracijo.

### Izkoristek LLM za ponovno razvrščanje in ocenjevanje

Veliki jezikovni modeli (LLM) se lahko uporabijo za ponovno razvrščanje in ocenjevanje z oceno relevantnosti in kakovosti pridobljenih dokumentov ali generiranih odgovorov. Tako deluje:

**Pridobivanje:** Na začetku se pridobi nabor kandidatskih dokumentov ali odgovorov na podlagi poizvedbe.

**Ponovno razvrščanje:** LLM oceni te kandidate in jih ponovno razvrsti glede na njihovo relevantnost in kakovost. Ta korak zagotovi, da so najpomembnejše in najbolj kakovostne informacije prikazane prve.

**Ocenjevanje:** LLM dodeli ocene posameznim kandidatom, ki odražajo njihovo relevantnost in kakovost. To pomaga pri izbiri najboljšega odgovora ali dokumenta za uporabnika.

Z uporabo LLM za ponovno razvrščanje in ocenjevanje lahko sistem zagotavlja natančnejše in kontekstualno relevantne informacije, kar izboljša celotno uporabniško izkušnjo.

Tukaj je primer, kako bi potovalni agent lahko uporabil Veliki jezikovni model (LLM) za ponovno razvrščanje in ocenjevanje potovalnih destinacij glede na uporabnikove preference v Pythonu:

#### Scenarij - Potovanje glede na preference

Potovalni agent želi priporočiti najboljše potovalne destinacije stranki na podlagi njihovih preferenc. LLM bo pomagal pri ponovnem razvrščanju in ocenjevanju destinacij, da se zagotovi, da so prikazane najustreznejše možnosti.

#### Koraki:

1. Zbira se uporabniške preference.
2. Pridobi se seznam potencialnih potovalnih destinacij.
3. Uporabi se LLM za ponovno razvrščanje in ocenjevanje destinacij na podlagi uporabnikovih preferenc.

Tukaj je, kako lahko posodobite prejšnji primer za uporabo Azure OpenAI storitev:

#### Zahteve

1. Potrebujete naročnino na Azure.
2. Ustvarite Azure OpenAI vir in pridobite svoj API ključ.

#### Primer Python kode

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Ustvari poziv za Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Določi glave in vsebino zahteve
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Pokliči Azure OpenAI API za pridobitev ponovno razvrščenih in ocenjenih destinacij
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Izvleci in vrni priporočila
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

# Primer uporabe
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

#### Razlaga kode - Rezervator preferenc

1. **Inicializacija**: Razred `TravelAgent` je inicializiran s seznamom potencialnih potovalnih destinacij, pri čemer ima vsaka destinacija atribute, kot so ime in opis.

2. **Pridobivanje priporočil (`get_recommendations` metoda)**: Ta metoda generira poziv (prompt) za Azure OpenAI storitev na podlagi uporabnikovih preferenc in pošlje HTTP POST zahtevo na Azure OpenAI API za pridobitev ponovno razvrščenih in ocenjenih destinacij.

3. **Generiranje poziva (`generate_prompt` metoda)**: Ta metoda sestavi poziv za Azure OpenAI, ki vključuje uporabnikove preference ter seznam destinacij. Poziv usmerja model, da ponovno razvrsti in oceni destinacije glede na predložene preference.

4. **Klic API**: Knjižnica `requests` se uporablja za pošiljanje HTTP POST zahteve na končno točko Azure OpenAI API. Odgovor vsebuje ponovno razvrščene in ocenjene destinacije.

5. **Primer uporabe**: Potovalni agent zbira uporabnikove preference (npr. interes za ogled znamenitosti in raznoliko kulturo) in uporabi Azure OpenAI storitev za pridobitev ponovno razvrščenih in ocenjenih priporočil potovalnih destinacij.

Poskrbite, da boste `your_azure_openai_api_key` zamenjali z vašim dejanskim Azure OpenAI API ključem in `https://your-endpoint.com/...` z dejansko URL končno točko vaše Azure OpenAI namestitve.

Z izkoriščanjem LLM za ponovno razvrščanje in ocenjevanje lahko potovalni agent nudi bolj personalizirana in relevantna potovalna priporočila strankam, kar izboljša njihovo celotno izkušnjo.

### RAG: tehnika pozivanja vs orodje

Retrieval-Augmented Generation (RAG) je lahko tako tehnika pozivanja kot orodje pri razvoju AI agentov. Razumevanje razlike med njima vam lahko pomaga bolje izkoristiti RAG v vaših projektih.

#### RAG kot tehnika pozivanja

**Kaj je to?**

- Kot tehnika pozivanja RAG vključuje oblikovanje specifičnih poizvedb ali pozivov za usmerjanje pridobitve relevantnih informacij iz velikega korpusa ali baze podatkov. Te informacije se nato uporabijo za generiranje odgovorov ali dejanj.

**Kako deluje:**

1. **Oblikovanje pozivov**: Ustvarite dobro strukturirane pozive ali poizvedbe, ki temeljijo na nalogi ali uporabnikovih vnosih.
2. **Pridobivanje informacij**: Uporabite pozive za iskanje relevantnih podatkov iz že obstoječe baze znanja ali podatkovnega skladišča.
3. **Generiranje odgovora**: Združite pridobljene informacije z generativnimi modeli AI, da ustvarite celovit in koherenten odgovor.

**Primer v potovalnem agentu**:

- Uporabnikov vnos: "Želim obiskati muzeje v Parizu."
- Poziv: "Poišči najboljše muzeje v Parizu."
- Pridobljene informacije: Podrobnosti o Louvreu, Musée d'Orsay itd.
- Generirani odgovor: "Tukaj so nekateri najboljši muzeji v Parizu: Louvre, Musée d'Orsay in Centre Pompidou."

#### RAG kot orodje

**Kaj je to?**

- Kot orodje je RAG integriran sistem, ki avtomatizira proces pridobivanja in generiranja, kar razvijalcem olajša implementacijo kompleksnih AI funkcionalnosti brez ročnega oblikovanja pozivov za vsako poizvedbo.

**Kako deluje:**

1. **Integracija**: Vgrajen je v arhitekturo AI agenta, omogoča samodejno upravljanje nalog pridobivanja in generiranja.
2. **Avtomatizacija**: Orodje upravlja celoten proces, od sprejema uporabniškega vnosa do generiranja končnega odgovora, brez potrebe po eksplicitnih pozivih za vsak korak.
3. **Učinkovitost**: Izboljša delovanje agenta z racionalizacijo postopkov pridobivanja in generiranja, kar omogoča hitrejše in natančnejše odgovore.

**Primer v potovalnem agentu**:

- Uporabnikov vnos: "Želim obiskati muzeje v Parizu."
- RAG orodje: Samodejno pridobi informacije o muzejih in generira odgovor.
- Generirani odgovor: "Tukaj so nekateri najboljši muzeji v Parizu: Louvre, Musée d'Orsay in Centre Pompidou."

### Primerjava

| Vidik                 | Tehnika pozivanja                                         | Orodje                                                |
|------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| **Ročno vs Avtomatsko**| Ročno oblikovanje pozivov za vsako poizvedbo.              | Avtomatiziran proces pridobivanja in generiranja.     |
| **Nadzor**             | Ponuja večji nadzor nad procesom pridobivanja.              | Poenostavlja in avtomatizira pridobivanje in generiranje.|
| **Prilagodljivost**    | Omogoča prilagojene pozive glede na specifične potrebe.     | Bolj učinkovito za obsežne implementacije.            |
| **Zapletenost**        | Zahteva oblikovanje in prilagajanje pozivov.                 | Lažje za vključitev v arhitekturo AI agentov.         |

### Praktični primeri

**Primer tehnike pozivanja:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Primer orodja:**

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

### Ocena relevantnosti

Ocena relevantnosti je ključen vidik delovanja AI agenta. Zagotavlja, da so informacije, ki jih agent pridobi in generira, ustrezne, natančne in koristne za uporabnika. Raziščimo, kako oceniti relevantnost v AI agentih, vključno s praktičnimi primeri in tehnikami.

#### Ključni pojmi pri oceni relevantnosti

1. **Zavedanje konteksta**:
   - Agent mora razumeti kontekst uporabnikove poizvedbe, da pridobi in generira relevantne informacije.
   - Primer: Če uporabnik vpraša za "najboljše restavracije v Parizu", naj agent upošteva preference uporabnika, kot so tip kuhinje in proračun.

2. **Natančnost**:
   - Informacije, ki jih posreduje agent, naj bodo dejansko pravilne in ažurne.
   - Primer: Priporočanje trenutno odprtih restavracij z dobrimi ocenami namesto zastarelih ali zaprtih možnosti.

3. **Namen uporabnika**:
   - Agent mora sklepati o uporabnikovem namenu za poizvedbo, da zagotovi najbolj relevantne informacije.
   - Primer: Če uporabnik vpraša za "cene hotele", naj agent daje prednost ugodnim možnostim.

4. **Povratna zanka**:
   - Stalno zbiranje in analiza uporabniških povratnih informacij pomaga agentu izpopolniti proces ocenjevanja relevantnosti.
   - Primer: Vključitev ocen uporabnikov in povratnih informacij o prejšnjih priporočilih za izboljšanje prihodnjih odgovorov.

#### Praktične tehnike za ocenjevanje relevantnosti

1. **Ocena ustreznosti**:
   - Dodelite oceno ustreznosti vsakemu pridobljenemu elementu glede na to, kako dobro ustreza uporabnikovi poizvedbi in preferencam.
   - Primer:

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

2. **Filtriranje in razvrščanje**:
   - Izločite irelevantne elemente in preostale razvrstite glede na njihove ocene ustreznosti.
   - Primer:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Vrni top 10 relevantnih elementov
     ```

3. **Obdelava naravnega jezika (NLP)**:
   - Uporabite tehnike NLP za razumevanje uporabnikove poizvedbe in pridobivanje relevantnih informacij.
   - Primer:

     ```python
     def process_query(query):
         # Uporabite NLP za izvlečenje ključnih informacij iz uporabnikove poizvedbe
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integracija uporabniških povratnih informacij**:
   - Zbirajte povratne informacije o posredovanih priporočilih in jih uporabite za prilagoditev prihodnjih ocen relevantnosti.
   - Primer:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Primer: ocenjevanje relevantnosti v potovalnem agentu

Tukaj je praktičen primer, kako lahko potovalni agent oceni relevantnost potovalnih priporočil:

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
        return ranked_items[:10]  # Vrni top 10 relevantnih elementov

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

# Primer uporabe
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

### Iskanje z namenom

Iskanje z namenom vključuje razumevanje in interpretacijo osnovnega cilja ali želje za uporabnikovo poizvedbo, da se pridobijo in generirajo najbolj relevantne in koristne informacije. Ta pristop presega zgolj ujemanje ključnih besed in se osredotoča na razumevanje dejanskih potreb in konteksta uporabnika.

#### Ključni pojmi pri iskanju z namenom

1. **Razumevanje uporabnikovega namena**:
   - Namen uporabnika lahko razdelimo na tri glavne vrste: informacijski, navigacijski in transakcijski.
     - **Informacijski namen**: uporabnik išče informacije o temi (npr. "Kateri so najboljši muzeji v Parizu?").
     - **Navigacijski namen**: uporabnik želi dostopati do specifične spletne strani ali strani (npr. "Uradna spletna stran Louvrea").
     - **Transakcijski namen**: uporabnik želi opraviti transakcijo, kot je rezervacija leta ali nakup (npr. "Rezerviraj let za Pariz").

2. **Zavedanje konteksta**:
   - Analiza konteksta uporabnikove poizvedbe pomaga natančno prepoznati njegov namen. To vključuje upoštevanje prejšnjih interakcij, uporabniških preferenc in specifičnih podrobnosti trenutne poizvedbe.

3. **Obdelava naravnega jezika (NLP)**:
   - NLP tehnike se uporabljajo za razumevanje in interpretacijo naravnih jezikovnih poizvedb uporabnikov. To vključuje naloge, kot so prepoznavanje entitet, analiza čustvenosti in razčlenjevanje poizvedb.

4. **Personalizacija**:
   - Personalizacija rezultatov iskanja na podlagi uporabnikove zgodovine, preferenc in povratnih informacij izboljšuje relevantnost pridobljenih informacij.

#### Praktični primer: iskanje z namenom v potovalnem agentu

Vzemimo potovalnega agenta kot primer, da vidimo, kako se lahko implementira iskanje z namenom.

1. **Zbiranje uporabniških preferenc**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Razumevanje uporabnikovega namena**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Zavedanje konteksta**


   ```python
   def analyze_context(query, user_history):
       # Združite trenutni poizvedbo z uporabnikovo zgodovino za razumevanje konteksta
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Iskanje in personalizacija rezultatov**

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
       # Primer iskalne logike za informativni namen
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Primer iskalne logike za navigacijski namen
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Primer iskalne logike za transakcijski namen
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Primer logike personalizacije
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Vrni top 10 personaliziranih rezultatov
   ```

5. **Primer uporabe**

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

## 4. Generiranje kode kot orodje

Agenti za generiranje kode uporabljajo AI modele za pisanje in izvajanje kode, s čimer rešujejo kompleksne probleme in avtomatizirajo opravila.

### Agenti za generiranje kode

Agenti za generiranje kode uporabljajo generativne AI modele za pisanje in izvajanje kode. Ti agenti lahko rešujejo kompleksne probleme, avtomatizirajo opravila in zagotavljajo dragocene vpoglede z generiranjem in izvajanjem kode v različnih programskih jezikih.

#### Praktične uporabe

1. **Avtomatizirano generiranje kode**: Generiranje koščkov kode za določena opravila, kot so analiza podatkov, spletno strganje ali strojno učenje.
2. **SQL kot RAG**: Uporaba SQL poizvedb za pridobivanje in manipulacijo podatkov iz baz.
3. **Reševanje problemov**: Ustvarjanje in izvajanje kode za reševanje specifičnih problemov, kot je optimizacija algoritmov ali analiza podatkov.

#### Primer: Agent za generiranje kode za analizo podatkov

Predstavljajte si, da oblikujete agenta za generiranje kode. Tako bi lahko deloval:

1. **Opravilo**: Analizirati nabor podatkov za identifikacijo trendov in vzorcev.
2. **Koraki**:
   - Naložite nabor podatkov v orodje za analizo podatkov.
   - Generirajte SQL poizvedbe za filtriranje in agregacijo podatkov.
   - Izvedite poizvedbe in pridobite rezultate.
   - Uporabite rezultate za generiranje vizualizacij in vpogledov.
3. **Potrebni viri**: Dostop do nabora podatkov, orodja za analizo podatkov in SQL zmogljivosti.
4. **Izkušnje**: Uporabite pretekle rezultate analiz za izboljšanje natančnosti in relevantnosti prihodnjih analiz.

### Primer: Agent za generiranje kode za turističnega agenta

V tem primeru bomo oblikovali agenta za generiranje kode, Turističnega agenta, ki uporabnikom pomaga pri načrtovanju potovanja z generiranjem in izvajanjem kode. Ta agent lahko obravnava opravila, kot so pridobivanje možnosti potovanja, filtriranje rezultatov in sestavljanje itinerarja z uporabo generativne AI.

#### Pregled agenta za generiranje kode

1. **Zbiranje uporabniških preferenc**: Zbira uporabniške vnose, kot so ciljna destinacija, datumi potovanja, proračun in zanimanja.
2. **Generiranje kode za pridobivanje podatkov**: Generira koščke kode za pridobivanje podatkov o letih, hotelih in atrakcijah.
3. **Izvajanje generirane kode**: Izvaja generirano kodo za pridobivanje informacij v realnem času.
4. **Generiranje itinerarja**: Združi pridobljene podatke v personaliziran načrt potovanja.
5. **Prilagajanje na podlagi povratnih informacij**: Prejema povratne informacije uporabnika in po potrebi ponovno generira kodo za izboljšanje rezultatov.

#### Implementacija korak za korakom

1. **Zbiranje uporabniških preferenc**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generiranje kode za pridobivanje podatkov**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Primer: Ustvari kodo za iskanje letov glede na uporabniške preference
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Primer: Ustvari kodo za iskanje hotelov
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Izvajanje generirane kode**

   ```python
   def execute_code(code):
       # Izvedite generirano kodo z uporabo exec
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

4. **Generiranje itinerarja**

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

5. **Prilagajanje na podlagi povratnih informacij**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Prilagodite nastavitve glede na povratne informacije uporabnika
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Ponovno ustvarite in zaženite kodo z posodobljenimi nastavitvami
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Izkoriščanje zavedanja okolja in sklepanja

Na podlagi sheme tabele lahko v resnici izboljšate proces generiranja poizvedb z izkoriščanjem zavedanja okolja in sklepanja.

Tukaj je primer, kako to lahko storite:

1. **Razumevanje sheme**: Sistem bo razumel shemo tabele in uporabil te informacije za utemeljitev generiranja poizvedb.
2. **Prilagajanje na podlagi povratnih informacij**: Sistem bo prilagodil uporabniške preference glede na povratne informacije in presodil, katera polja v shemi je treba posodobiti.
3. **Generiranje in izvajanje poizvedb**: Sistem bo generiral in izvajal poizvedbe za pridobivanje posodobljenih podatkov o letih in hotelih na podlagi novih preferenc.

Tukaj je posodobljen primer kode v Pythonu, ki vključuje te koncepte:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Prilagodi nastavitve glede na povratne informacije uporabnika
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Razmišljanje na podlagi sheme za prilagoditev drugih sorodnih nastavitev
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Prilagojena logika za prilagoditev nastavitev na podlagi sheme in povratnih informacij
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Ustvari kodo za pridobivanje podatkov o poletih na podlagi posodobljenih nastavitev
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Ustvari kodo za pridobivanje podatkov o hotelih na podlagi posodobljenih nastavitev
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simuliraj izvajanje kode in vrni lažne podatke
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Ustvari načrt poti na podlagi poletov, hotelov in znamenitosti
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Primer sheme
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Primer uporabe
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Ponovno ustvari in izvedi kodo z posodobljenimi nastavitvami
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Razlaga - Rezervacija na podlagi povratnih informacij

1. **Zavedanje sheme**: Slovar `schema` določa, kako naj se preference prilagodijo glede na povratne informacije. Vključuje polja, kot so `priljubljeni` in `izogibaj`, s pripadajočimi prilagoditvami.
2. **Prilagajanje preferenc (metoda `adjust_based_on_feedback`)**: Ta metoda prilagodi preference glede na uporabniške povratne informacije in shemo.
3. **Prilagoditve glede na okolje (metoda `adjust_based_on_environment`)**: Ta metoda prilagodi prilagoditve na podlagi sheme in povratnih informacij.
4. **Generiranje in izvajanje poizvedb**: Sistem generira kodo za pridobivanje posodobljenih podatkov o letih in hotelih glede na prilagojene preference in simulira izvajanje teh poizvedb.
5. **Generiranje itinerarja**: Sistem ustvari posodobljen itinerar na podlagi novih podatkov o letih, hotelih in atrakcijah.

Z vključitvijo zavedanja okolja in sklepanja na podlagi sheme lahko sistem generira bolj natančne in relevantne poizvedbe, kar vodi do boljših priporočil za potovanja in bolj personalizirane uporabniške izkušnje.

### Uporaba SQL kot tehnike Retrieval-Augmented Generation (RAG)

SQL (Strukturiran poizvedbeni jezik) je zmogljivo orodje za interakcijo z bazami podatkov. Ko se uporablja kot del pristopa Retrieval-Augmented Generation (RAG), lahko SQL pridobiva relevantne podatke iz baz, ki služijo za tvorbo odgovorov ali akcij AI agentov. Raziskajmo, kako se SQL lahko uporablja kot tehnika RAG v kontekstu Turističnega agenta.

#### Ključni pojmi

1. **Interakcija z bazo podatkov**:
   - SQL se uporablja za poizvedovanje baz, pridobivanje relevantnih informacij in manipulacijo podatkov.
   - Primer: Pridobivanje podrobnosti o letih, informacij o hotelih in atrakcijah iz baze potovanj.

2. **Integracija z RAG**:
   - SQL poizvedbe se generirajo na podlagi uporabniških vnosov in preferenc.
   - Pridobljeni podatki se nato uporabijo za generiranje personaliziranih priporočil ali akcij.

3. **Dinamično generiranje poizvedb**:
   - AI agent generira dinamične SQL poizvedbe glede na kontekst in potrebe uporabnika.
   - Primer: Prilagajanje SQL poizvedb za filtriranje rezultatov glede na proračun, datume in zanimanja.

#### Uporabe

- **Avtomatizirano generiranje kode**: Generiranje koščkov kode za specifična opravila.
- **SQL kot RAG**: Uporaba SQL poizvedb za manipulacijo podatkov.
- **Reševanje problemov**: Ustvarjanje in izvajanje kode za reševanje problemov.

**Primer**:
Agent za analizo podatkov:

1. **Opravilo**: Analizirati nabor podatkov za iskanje trendov.
2. **Koraki**:
   - Naložite nabor podatkov.
   - Generirajte SQL poizvedbe za filtriranje podatkov.
   - Izvedite poizvedbe in pridobite rezultate.
   - Generirajte vizualizacije in vpoglede.
3. **Viri**: Dostop do nabora podatkov, SQL zmogljivosti.
4. **Izkušnje**: Uporabite pretekle rezultate za izboljšanje prihodnjih analiz.

#### Praktičen primer: Uporaba SQL v Turističnem agentu

1. **Zbiranje uporabniških preferenc**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generiranje SQL poizvedb**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Izvajanje SQL poizvedb**

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

4. **Generiranje priporočil**

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

#### Primer SQL poizvedb

1. **Poizvedba za lete**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Poizvedba za hotele**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Poizvedba za atrakcije**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Z uporabo SQL kot dela tehnike Retrieval-Augmented Generation (RAG) lahko AI agenti, kot je Turistični agent, dinamično pridobivajo in uporabljajo relevantne podatke za zagotavljanje natančnih in personaliziranih priporočil.

### Primer metazavedanja

Za prikaz implementacije metazavedanja ustvarimo preprostega agenta, ki *razmišlja o svojem procesu odločanja* med reševanjem problema. V tem primeru bomo zgradili sistem, kjer agent poskuša optimizirati izbiro hotela, nato pa oceni lastno sklepanja in po potrebi prilagodi svojo strategijo, ko naredi napake ali podoptimalne izbire.

To simuliramo s preprostim primerom, kjer agent izbira hotele na podlagi kombinacije cene in kakovosti, hkrati pa "razmišlja" o svojih odločitvah in se temu primerno prilagaja.

#### Kako to ilustrira metazavedanje:

1. **Začetna odločitev**: Agent bo izbral najcenejši hotel, ne da bi razumel vpliv kakovosti.
2. **Razmislek in ocena**: Po začetni izbiri agent preveri, ali je bil hotel "slaba" izbira s pomočjo uporabniških povratnih informacij. Če ugotovi, da je bila kakovost hotela prenizka, razmišlja o svojem sklepanju.
3. **Prilagoditev strategije**: Agent prilagodi svojo strategijo na podlagi razmisleka in preklopi iz "najcenejši" na "najvišja kakovost", s čimer izboljša proces odločanja v prihodnjih iteracijah.

Tukaj je primer:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Shrani prej izbrane hotele
        self.corrected_choices = []  # Shrani popravljene izbire
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Razpoložljive strategije

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
        # Predpostavimo, da imamo nekaj povratnih informacij uporabnikov, ki nam povedo, ali je bila zadnja izbira dobra ali ne
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Prilagodi strategijo, če je bila prejšnja izbira nezadovoljiva
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

# Simuliraj seznam hotelov (cena in kakovost)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Ustvari agenta
agent = HotelRecommendationAgent()

# Korak 1: Agent priporoči hotel z uporabo strategije "najcenejši"
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Korak 2: Agent razmisli o izbiri in po potrebi prilagodi strategijo
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Korak 3: Agent ponovno priporoči, tokrat z uporabo prilagojene strategije
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Sposobnosti metazavedanja agentov

Ključno tukaj je zmožnost agenta, da:
- Ocenjuje svoje pretekle odločitve in proces odločanja.
- Prilagodi svojo strategijo na podlagi tega razmisleka, tj. metazavedanje v praksi.

To je preprosta oblika metazavedanja, kjer sistem lahko prilagodi svoj postopek sklepanja na podlagi notranjih povratnih informacij.

### Zaključek

Metazavedanje je močno orodje, ki lahko znatno poveča zmožnosti AI agentov. Z vključitvijo metazavednih procesov lahko oblikujete agente, ki so bolj inteligentni, prilagodljivi in učinkoviti. Uporabite dodatne vire za nadaljnje raziskovanje fascinantnega sveta metazavedanja pri AI agentih.

### Imate več vprašanj o vzorcu oblikovanja metazavedanja?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) in spoznajte druge učence, se udeležite ur uradnih ur in dobite odgovore na vaša vprašanja o AI agentih.

## Prejšnja lekcija

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Naslednja lekcija

[AI Agents in Production](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->