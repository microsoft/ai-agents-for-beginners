[![Večagentno oblikovanje](../../../translated_images/sl/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Kliknite na sliko zgoraj za ogled videa tega učnega gradiva)_
# Metakognicija pri AI agentih

## Uvod

Dobrodošli na lekciji o metakogniciji pri AI agentih! Ta poglavje je namenjeno začetnikom, ki jih zanima, kako lahko AI agenti razmišljajo o lastnih miselnih procesih. Ob koncu te lekcije boste razumeli ključne pojme in imeli praktične primere za uporabo metakognicije pri oblikovanju AI agentov.

## Cilji učenja

Po končani lekciji boste lahko:

1. Razumeli posledice zanki sklepanja v definicijah agentov.
2. Uporabili tehnike načrtovanja in ocenjevanja za pomoč samopopravnim agentom.
3. Ustvarili lastne agente, sposobne manipulirati kodo za izvajanje nalog.

## Uvod v metakognicijo

Metakognicija se nanaša na kognitivne procese višjega reda, ki vključujejo razmišljanje o lastnem razmišljanju. Za AI agente to pomeni, da lahko ocenjujejo in prilagajajo svoja dejanja na podlagi samospoznanja in preteklih izkušenj. Metakognicija ali "razmišljanje o razmišljanju" je pomemben koncept pri razvoju agentnih AI sistemov. Gre za to, da so AI sistemi zavestni svojih notranjih procesov in lahko spremljajo, regulirajo ter prilagajajo svoje vedenje. Tako kot mi, ko preberemo sobo ali pogledamo problem. Ta samospoznanja lahko pomagajo AI sistemom sprejemati boljše odločitve, odkrivati napake in izboljševati svojo zmogljivost skozi čas - ponovno povezuje z Turingovim testom in razpravo o tem, ali bo AI prevzel nadzor.

V okviru agentnih AI sistemov lahko metakognicija pomaga rešiti več izzivov, kot so:
- Transparentnost: Zagotavljanje, da AI sistemi lahko razložijo svoje sklepe in odločitve.
- Razmišljanje: Izboljšanje sposobnosti AI sistemov za sintetiziranje informacij in sprejemanje razumenih odločitev.
- Prilagajanje: Omogočanje AI sistemom prilagajanja na nova okolja in spreminjajoče se pogoje.
- Percepcija: Izboljšanje natančnosti AI sistemov pri prepoznavanju in interpretaciji podatkov iz okolja.

### Kaj je metakognicija?

Metakognicija ali "razmišljanje o razmišljanju" je kognitivni proces višjega reda, ki vključuje samospoznanje in samoregulacijo kognitivnih procesov. Na področju AI metakognicija omogoča agentom, da ocenjujejo in prilagajajo svoje strategije in dejanja, kar vodi do izboljšanih sposobnosti reševanja problemov in sprejemanja odločitev. Z razumevanjem metakognicije lahko oblikujete AI agente, ki so ne le pametnejši, ampak tudi bolj prilagodljivi in učinkoviti. V pravi metakogniciji bi AI jasno razmišljal o svojem lastnem sklepanju.

Primer: "Prednostno sem izbral cenejše lete, ker ... morda zamujam neposredne lete, zato bom ponovno preveril.".
Sledenje temu, kako in zakaj je izbral določeno pot.
- Opazovanje, da je naredil napake, ker je preveč zaupal uporabniškim preferencam iz prejšnjega časa, zato spremeni svojo strategijo odločanja, ne samo končno priporočilo.
- Diagnostika vzorcev, kot so: "Kadarkoli vidim, da uporabnik omeni 'preveč gneče', ne bi smel le odstraniti določenih znamenitosti, ampak tudi razmisliti, da je moj način izbire 'top znamenitosti' napačen, če vedno razvrščam po priljubljenosti."

### Pomen metakognicije pri AI agentih

Metakognicija igra ključno vlogo pri oblikovanju AI agentov iz več razlogov:

![Pomen metakognicije](../../../translated_images/sl/importance-of-metacognition.b381afe9aae352f7.webp)

- Samorefleksija: Agenti lahko ocenijo svoje lastne uspešnosti in prepoznajo področja za izboljšave.
- Prilagodljivost: Agenti lahko prilagajajo svoje strategije na podlagi preteklih izkušenj in spreminjajočih se okolij.
- Popravljanje napak: Agenti lahko samodejno odkrivajo in popravljajo napake, kar vodi do natančnejših rezultatov.
- Upravljanje z viri: Agenti lahko optimizirajo uporabo virov, kot sta čas in računska moč, s pomočjo načrtovanja in ocenjevanja svojih dejanj.

## Sestavne komponente AI agenta

Preden se poglobite v metakognitivne procese, je pomembno razumeti osnovne sestavne dele AI agenta. AI agent običajno sestavljajo:

- Persona: Osebnost in značilnosti agenta, ki določajo, kako sodeluje z uporabniki.
- Orodja: Sposobnosti in funkcije, ki jih agent lahko izvaja.
- Spretnosti: Znanje in strokovnost, ki jih agent poseduje.

Te sestavine delujejo skupaj in ustvarjajo "enoto strokovnosti", ki lahko izvaja specifične naloge.

**Primer**:
Razmislite o potovalnem agentu, storitvah agentov, ki ne le načrtujejo vaš dopust, ampak prilagajajo svojo pot na podlagi podatkov v realnem času in preteklih izkušenj uporabnikov.

### Primer: Metakognicija v potovalni agenciji

Predstavljajte si, da razvijate potovalno agencijo, poganjano z AI. Ta agent, "Potovalni agent," pomaga uporabnikom načrtovati počitnice. Za vključitev metakognicije mora Potovalni agent ocenjevati in prilagajati svoja dejanja na podlagi samospoznanja in preteklih izkušenj. Tako bi metakognicija lahko delovala:

#### Trenutna naloga

Trenutna naloga je pomagati uporabniku načrtovati potovanje v Pariz.

#### Koraki za dokončanje naloge

1. **Zbiranje uporabniških preferenc**: Povprašajte uporabnika o datumih potovanja, proračunu, interesih (npr. muzeji, kulinarika, nakupovanje) ter morebitnih posebnih zahtevah.
2. **Pridobivanje informacij**: Poiščite možnosti letov, namestitev, znamenitosti in restavracij, ki ustrezajo uporabnikovim preferencam.
3. **Generiranje priporočil**: Ponudite personaliziran itinerar z informacijami o letih, rezervacijah hotelov in predlaganih aktivnostih.
4. **Prilagajanje na podlagi povratnih informacij**: Povprašajte uporabnika po mnenju o priporočilih in izvedite potrebne spremembe.

#### Potrebni viri

- Dostop do baz podatkov s podatki o letih in rezervacijah hotelov.
- Informacije o pariških znamenitostih in restavracijah.
- Podatki o uporabniških mnenjih iz prejšnjih interakcij.

#### Izkušnje in samorefleksija

Potovalni agent uporablja metakognicijo za ocenjevanje svoje uspešnosti in učenje iz preteklih izkušenj. Na primer:

1. **Analiza uporabniških povratnih informacij**: Potovalni agent pregleda povratne informacije uporabnikov, da ugotovi, katera priporočila so bila dobro sprejeta in katera ne. Glede na to prilagodi svoje prihodnje predloge.
2. **Prilagodljivost**: Če je uporabnik prej omenil, da ne mara gneče, se bo Potovalni agent izogibal priporočanju priljubljenih turističnih lokacij v času konic.
3. **Popravljanje napak**: Če je Potovalni agent v preteklosti naredil napako pri rezervaciji, npr. predlagal hotel, ki je bil poln, se nauči strožje preverjati razpoložljivost pred izdelavo priporočil.

#### Praktičen primer za razvijalca

Tukaj je poenostavljen primer kode Travel Agent, ki vključuje metakognicijo:

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
        # Analiza povratnih informacij in prilagajanje prihodnjih priporočil
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

- **Samorefleksija**: Agenti lahko analizirajo svojo uspešnost in ugotavljajo področja za izboljšavo.
- **Prilagodljivost**: Agenti lahko spreminjajo strategije na podlagi povratnih informacij in spreminjajočih se pogojev.
- **Popravljanje napak**: Agenti lahko samostojno odkrivajo in popravljajo napake.
- **Upravljanje z viri**: Agenti lahko optimizirajo uporabo virov, kot sta čas in računska moč.

Z vključevanjem metakognicije lahko Potovalni agent ponudi bolj personalizirana in natančna potovalna priporočila, kar izboljša celotno uporabniško izkušnjo.

---

## 2. Načrtovanje pri agentih

Načrtovanje je ključna sestavina vedenja AI agenta. Vključuje določanje korakov, potrebnih za dosego cilja, pri čemer upošteva trenutno stanje, vire in možne ovire.

### Elementi načrtovanja

- **Trenutna naloga**: Jasno opredelite nalogo.
- **Koraki za dokončanje naloge**: Razdelite nalogo na obvladljive korake.
- **Potrebni viri**: Določite potrebne vire.
- **Izkušnje**: Uporabite pretekle izkušnje za podporo načrtovanju.

**Primer**:
Tu so koraki, ki jih Potovalni agent mora izvesti, da učinkovito pomaga uporabniku pri načrtovanju potovanja:

### Koraki za Potovalni agent

1. **Zbiranje uporabniških preferenc**
   - Povprašajte uporabnika o podrobnostih njegovih potovalnih datumov, proračunu, interesih in morebitnih posebnih zahtevah.
   - Primeri: "Kdaj načrtujete potovati?" "Kakšen je vaš proračun?" "Katere aktivnosti imate radi med počitnicami?"

2. **Pridobivanje informacij**
   - Poiščite ustrezne možnosti potovanj glede na uporabniške preference.
   - **Leti**: Poiščite razpoložljive lete v okviru uporabnikovega proračuna in željenih datumov potovanja.
   - **Namestitve**: Poiščite hotele ali najemne enote, ki ustrezajo uporabnikovim željam glede lokacije, cene in udobja.
   - **Znamenitosti in restavracije**: Prepoznajte priljubljene znamenitosti, aktivnosti in jedilne možnosti, ki se ujemajo z uporabnikovimi interesi.

3. **Generiranje priporočil**
   - Združite pridobljene informacije v personaliziran itinerar.
   - Zagotovite podrobnosti, kot so možnosti letov, rezervacije hotelov in predlagane aktivnosti, prilagojene uporabnikovim interesom.

4. **Predstavitev itinerarja uporabniku**
   - Predstavite predlagani itinerar uporabniku v pregled.
   - Primer: "Tukaj je predlagan itinerar za vaše potovanje v Pariz. Vključuje podatke o letih, rezervacijah hotelov in seznam predlaganih aktivnosti ter restavracij. Sporočite mi vaše mnenje!"

5. **Zbiranje povratnih informacij**
   - Povprašajte uporabnika za povratne informacije o predlaganem itinerarju.
   - Primeri: "Ali vam ustrezajo možnosti letov?" "Ali je hotel primeren za vaše potrebe?" "Ali želite kaj dodati ali odstraniti?"

6. **Prilagoditev na podlagi povratnih informacij**
   - Spremenite itinerar glede na povratne informacije uporabnika.
   - Naredite potrebne spremembe pri letih, namestitvah in priporočilih glede aktivnosti, da bolje ustrezajo uporabnikovi želji.

7. **Končna potrditev**
   - Predstavite posodobljen itinerar uporabniku za končno potrditev.
   - Primer: "Naredil sem spremembe glede na vaše povratne informacije. Tukaj je posodobljen itinerar. Ali je vse v redu?"

8. **Rezervacija in potrditev**
   - Ko uporabnik potrdi itinerar, izvedite rezervacije letov, namestitev in predhodno načrtovanih aktivnosti.
   - Pošljite potrditvene podatke uporabniku.

9. **Nadaljnja podpora**
   - Bodite na voljo za pomoč uporabniku z morebitnimi spremembami ali dodatnimi zahtevami pred in med potovanjem.
   - Primer: "Če potrebujete dodatno pomoč med potovanjem, me lahko kadarkoli kontaktirate!"

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

# Primer uporabe v zahtevi za rezervacijo
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

Najprej začnimo z razumevanjem razlike med RAG orodjem in predhodnim nalaganjem konteksta

![RAG proti nalaganju konteksta](../../../translated_images/sl/rag-vs-context.9eae588520c00921.webp)

### Retrieval-Augmented Generation (RAG)

RAG združuje sistem iskanja z generativnim modelom. Ko je podan poizvedba, sistem iskanja priskrbi ustrezne dokumente ali podatke iz zunanjega vira, pridobljene informacije pa se uporabijo za dopolnitev vhodnih podatkov v generativnem modelu. To pomaga modelu generirati bolj natančne in kontekstualno relevantne odgovore.

V RAG sistemu agent pridobi relevantne informacije iz baze znanja in jih uporabi za generiranje primernih odgovorov ali dejanj.

### Korektivni pristop RAG

Korektivni pristop RAG je osredotočen na uporabo RAG tehnik za popravljanje napak in izboljšanje natančnosti AI agentov. To vključuje:

1. **Tehnika spodbude**: Uporaba specifičnih pozivov za usmerjanje agenta pri iskanju relevantnih informacij.
2. **Orodje**: Implementacija algoritmov in mehanizmov, ki agentu omogočajo ocenjevanje relevantnosti pridobljenih informacij in generiranje natančnih odgovorov.
3. **Vrednotenje**: Nenehno ocenjevanje uspešnosti agenta in sprejemanje prilagoditev za izboljšanje natančnosti in učinkovitosti.

#### Primer: Korektivni RAG v iskalnem agentu

Razmislite o iskalnem agentu, ki pridobiva informacije z interneta za odgovarjanje na uporabniške poizvedbe. Korektivni pristop RAG lahko vključuje:

1. **Tehnika spodbude**: Oblikovanje iskalnih poizvedb glede na uporabnikov vnos.
2. **Orodje**: Uporaba algoritmov za obdelavo naravnega jezika in strojno učenje za razvrščanje in filtriranje rezultatov iskanja.
3. **Vrednotenje**: Analiza uporabniških povratnih informacij za odkrivanje in popravljanje netočnosti v pridobljenih informacijah.

### Korektivni RAG v Potovalnem agentu

Korektivni RAG (Retrieval-Augmented Generation) izboljšuje AI sposobnost pridobivanja in generiranja informacij ob hkratnem popravljanju netočnosti. Poglejmo, kako lahko Potovalni agent uporabi korektivni pristop RAG za zagotavljanje bolj natančnih in relevantnih potovalnih priporočil.

To vključuje:

- **Tehnika spodbude:** Uporaba specifičnih pozivov za usmerjanje agenta pri pridobivanju relevantnih informacij.
- **Orodje:** Implementacija algoritmov in mehanizmov, ki agentu omogočajo ocenjevanje relevantnosti pridobljenih informacij in generiranje natančnih odgovorov.
- **Vrednotenje:** Nenehno ocenjevanje uspešnosti agenta in spreminjanje za izboljšanje natančnosti in učinkovitosti.

#### Koraki za implementacijo korektivnega RAG v Potovalnem agentu

1. **Začetna interakcija z uporabnikom**
   - Potovalni agent zbere začetne preference uporabnika, kot so ciljna destinacija, datumi potovanja, proračun in interesi.
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
   - Potovalni agent pridobi informacije o letih, nastanitvah, znamenitostih in restavracijah glede na uporabniške preference.
   - Primer:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generiranje začetnih priporočil**
   - Potovalni agent uporabi pridobljene informacije za generiranje personaliziranega itinerarja.
   - Primer:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Zbiranje uporabniških povratnih informacij**
   - Potovalni agent povpraša uporabnika za povratne informacije o začetnih priporočilih.
   - Primer:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Postopek korektivnega RAG**
   - **Tehnika spodbude**: Potovalni agent oblikuje nove iskalne poizvedbe na podlagi uporabniških povratnih informacij.
     - Primer:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Orodje**: Potovalni agent uporablja algoritme za razvrščanje in filtriranje novih rezultatov iskanja ter poudarja relevantnost na podlagi povratnih informacij uporabnika.
     - Primer:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Vrednotenje**: Potovalni agent nenehno ocenjuje relevantnost in natančnost svojih priporočil z analizo uporabniških povratnih informacij in izvajanjem potrebnih prilagoditev.
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

#### Praktičen primer

Tukaj je poenostavljen primer kode v Pythonu, ki vključuje korektivni pristop RAG v Potovalnem agentu:

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


Predpriprava konteksta vključuje nalaganje ustreznega konteksta ali ozadja v model pred obdelavo poizvedbe. To pomeni, da ima model dostop do teh informacij že od začetka, kar mu lahko pomaga ustvariti bolj informirane odgovore, ne da bi med procesom moral pridobivati dodatne podatke.

Tukaj je poenostavljen primer, kako bi lahko izgledala predpriprava konteksta za aplikacijo turističnega agenta v Pythonu:

```python
class TravelAgent:
    def __init__(self):
        # Prednaloži priljubljene destinacije in njihove informacije
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Pridobi informacije o destinaciji iz prednaloženega konteksta
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

1. **Inicializacija (metoda `__init__`)**: Razred `TravelAgent` predhodno naloži slovar z informacijami o priljubljenih destinacijah, kot so Pariz, Tokio, New York in Sydney. Ta slovar vključuje podrobnosti, kot so država, valuta, jezik in glavni turistični objekti za vsako destinacijo.

2. **Pridobivanje informacij (metoda `get_destination_info`)**: Ko uporabnik povpraša o določeni destinaciji, metoda `get_destination_info` pridobi ustrezne informacije iz predhodno naloženega slovarja konteksta.

S predhodnim nalaganjem konteksta lahko aplikacija turističnega agenta hitro odgovori na uporabnikove poizvedbe, ne da bi morala te informacije v realnem času pridobivati iz zunanjega vira. To naredi aplikacijo bolj učinkovito in odzivno.

### Zagon načrta z jasnim ciljem pred iteracijo

Zagon načrta z določenim ciljem pomeni, da začnemo z jasnim namenom ali željenim rezultatom. Z definiranjem tega cilja vnaprej lahko model ta cilj uporablja kot vodilo skozi celoten iterativni proces. To pomaga zagotoviti, da se vsaka iteracija premika bližje doseganju želenega rezultata, s čimer je proces bolj učinkovit in osredotočen.

Tukaj je primer, kako bi lahko zagnali potovalni načrt z določenim ciljem pred iteracijo za turističnega agenta v Pythonu:

### Scenarij

Turistični agent želi načrtovati prilagojen dopust za stranko. Cilj je ustvariti potovalni načrt, ki maksimira zadovoljstvo stranke glede na njihove želje in proračun.

### Koraki

1. Določite želje in proračun stranke.
2. Zaženite začetni načrt na podlagi teh želja.
3. Iterirajte za izboljšavo načrta, optimizirajte za zadovoljstvo stranke.

#### Koda v Pythonu

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

1. **Inicializacija (metoda `__init__`)**: Razred `TravelAgent` se inicializira s seznamom potencialnih destinacij, od katerih ima vsaka atributa, kot sta ime, strošek in vrsta aktivnosti.

2. **Zagon načrta (`bootstrap_plan`)**: Ta metoda ustvari začetni potovalni načrt glede na želje in proračun stranke. Prebere seznam destinacij in jih doda v načrt, če ustrezajo strankinim željam in ustrezajo proračunu.

3. **Ujemanje preferenc (`match_preferences`)**: Ta metoda preveri, ali destinacija ustreza željam stranke.

4. **Iteracija načrta (`iterate_plan`)**: Ta metoda izboljša začetni načrt tako, da poskuša vsako destinacijo zamenjati z boljšo izbiro glede na želje in omejitve proračuna stranke.

5. **Izračun stroškov (`calculate_cost`)**: Ta metoda izračuna skupne stroške trenutnega načrta, vključno s potencialno novo destinacijo.

#### Primer uporabe

- **Začetni načrt**: Turistični agent ustvari začetni načrt glede na strankine želje po ogledu znamenitosti in proračun 2000 $.
- **Izboljšan načrt**: Turistični agent iterira načrt, optimizirajoč ga za strankine želje in proračun.

Z zagonom načrta z jasnim ciljem (npr. maksimiranje zadovoljstva stranke) in iteracijo za izboljšavo načrta lahko turistični agent ustvari prilagojen in optimiziran potovalni načrt za stranko. Ta pristop zagotavlja, da se potovalni načrt že od začetka uskladi z željami in proračunom stranke ter se izboljšuje z vsako iteracijo.

### Izraba LLM za ponovno razvrščanje in ocenjevanje

Veliki jezikovni modeli (LLM) se lahko uporabijo za ponovno razvrščanje in ocenjevanje tako, da ocenjujejo relevantnost in kakovost pridobljenih dokumentov ali generiranih odgovorov. Tako deluje:

**Pridobivanje:** Začetni korak pridobivanja dobi nabor kandidatnih dokumentov ali odgovorov na podlagi poizvedbe.

**Ponovno razvrščanje:** LLM oceni te kandidate in jih ponovno razvrsti glede na njihovo relevantnost in kakovost. Ta korak zagotavlja, da se najprej predstavi najbolj relevantne in kakovostne informacije.

**Ocenjevanje:** LLM dodeli ocene za vsakega kandidata, ki odražajo njihovo relevantnost in kakovost. To pomaga izbrati najboljši odgovor ali dokument za uporabnika.

Z uporabo LLM za ponovno razvrščanje in ocenjevanje lahko sistem zagotovi natančnejše in kontekstualno relevantne informacije, izboljšuje celotno uporabniško izkušnjo.

Tukaj je primer, kako lahko turistični agent uporabi velik jezikovni model (LLM) za ponovno razvrščanje in ocenjevanje potovalnih destinacij na podlagi uporabnikovih želja v Pythonu:

#### Scenarij - Potovanje na podlagi želja

Turistični agent želi priporočiti najboljše potovalne destinacije stranki glede na njihove želje. LLM bo pomagal ponovno razvrstiti in oceniti destinacije, da se zagotovi predstavitev najbolj relevantnih možnosti.

#### Koraki:

1. Zberite želje uporabnika.
2. Pridobite seznam potencialnih potovalnih destinacij.
3. Uporabite LLM za ponovno razvrščanje in ocenjevanje destinacij glede na želje uporabnika.

Tukaj je, kako lahko posodobite prejšnji primer za uporabo Azure OpenAI storitev:

#### Zahteve

1. Potrebujete Azure naročnino.
2. Ustvarite Azure OpenAI vir in pridobite svoj API ključ.

#### Primer kode v Pythonu

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Ustvari poziv za Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Določi glave in vsebino za zahtevo
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

#### Razlaga kode - Preference Booker

1. **Inicializacija**: Razred `TravelAgent` je inicializiran s seznamom potencialnih potovalnih destinacij, od katerih ima vsaka atributa, kot sta ime in opis.

2. **Pridobivanje priporočil (metoda `get_recommendations`)**: Ta metoda generira poziv za Azure OpenAI storitev na podlagi uporabnikovih želja in pošlje HTTP POST zahtevek na Azure OpenAI API za ponovno razvrščanje in ocenjevanje destinacij.

3. **Generiranje poziva (metoda `generate_prompt`)**: Ta metoda sestavi poziv za Azure OpenAI, ki vključuje želje uporabnika in seznam destinacij. Poziv usmerja model, da ponovno razvrsti in oceni destinacije na podlagi podanih želja.

4. **Klic API**: Knjižnica `requests` se uporablja za pošiljanje HTTP POST zahtevka na Azure OpenAI API. Odziv vsebuje ponovno razvrščene in ocenjene destinacije.

5. **Primer uporabe**: Turistični agent zbere želje uporabnika (npr. zanimanje za ogled znamenitosti in raznoliko kulturo) in uporabi Azure OpenAI storitev za pridobitev ponovno razvrščenih in ocenjenih priporočil za potovalne destinacije.

Preverite, da zamenjate `your_azure_openai_api_key` z vašim dejanskim Azure OpenAI API ključem in `https://your-endpoint.com/...` z dejansko URL končne točke vaše Azure OpenAI namestitve.

Z izrabo LLM za ponovno razvrščanje in ocenjevanje lahko turistični agent strankam zagotovi bolj personalizirana in relevantna potovalna priporočila, s čimer izboljša njihovo splošno izkušnjo.

### RAG: tehnika pozivanja vs. orodje

Retrieval-Augmented Generation (RAG) je lahko tako tehnika pozivanja kot orodje pri razvoju AI agentov. Razumevanje razlike med njima vam lahko pomaga učinkoviteje izkoristiti RAG v vaših projektih.

#### RAG kot tehnika pozivanja

**Kaj je to?**

- Kot tehnika pozivanja RAG vključuje oblikovanje specifičnih poizvedb ali pozivov za usmerjanje pridobivanja relevantnih informacij iz obsežnega korpusa ali baze podatkov. Te informacije se nato uporabijo za generiranje odgovorov ali ukrepov.

**Kako deluje:**

1. **Oblikovanje pozivov**: Ustvarite dobro strukturirane pozive ali poizvedbe glede na nalogo ali uporabnikov vhod.
2. **Pridobivanje informacij**: Uporabite pozive za iskanje relevantnih podatkov v obstoječi bazi znanja ali naboru podatkov.
3. **Generiranje odgovora**: Združite pridobljene informacije z generativnimi AI modeli, da ustvarite celovit in skladen odgovor.

**Primer v turističnem agentu**:

- Uporabnikov vhod: "Želim obiskati muzeje v Parizu."
- Poziv: "Najdi najboljše muzeje v Parizu."
- Pridobljene informacije: Podrobnosti o muzeju Louvre, Musée d'Orsay itd.
- Generiran odgovor: "Tukaj so nekateri najboljši muzeji v Parizu: Louvre, Musée d'Orsay in Centre Pompidou."

#### RAG kot orodje

**Kaj je to?**

- Kot orodje je RAG integriran sistem, ki avtomatizira proces pridobivanja in generiranja, kar razvijalcem olajša implementacijo kompleksnih AI funkcionalnosti brez ročnega oblikovanja pozivov za vsako poizvedbo.

**Kako deluje:**

1. **Integracija**: Vključi RAG v arhitekturo AI agenta, ki samodejno upravlja naloge pridobivanja in generiranja.
2. **Avtomatizacija**: Orodje obvladuje celoten proces od sprejema uporabnikovega vhoda do generiranja končnega odgovora, brez potrebe po eksplicitnih pozivih za vsak korak.
3. **Učinkovitost**: Izboljša delovanje agenta z optimizacijo procesa pridobivanja in generiranja, kar omogoča hitrejše in natančnejše odgovore.

**Primer v turističnem agentu**:

- Uporabnikov vhod: "Želim obiskati muzeje v Parizu."
- RAG orodje: Samodejno pridobi informacije o muzejih in generira odgovor.
- Generiran odgovor: "Tukaj so nekateri najboljši muzeji v Parizu: Louvre, Musée d'Orsay in Centre Pompidou."

### Primerjava

| Vidik                 | Tehnika pozivanja                                        | Orodje                                              |
|-----------------------|----------------------------------------------------------|-----------------------------------------------------|
| **Ročno vs avtomatsko**| Ročno oblikovanje pozivov za vsako poizvedbo.            | Avtomatiziran proces pridobivanja in generiranja.   |
| **Nadzor**             | Ponuja več nadzora nad procesom pridobivanja.            | Poenostavlja in avtomatizira pridobivanje in generiranje. |
| **Fleksibilnost**      | Omogoča prilagojene pozive glede na specifične potrebe.  | Bolj učinkovito za obsežne implementacije.          |
| **Zapletenost**        | Zahteva oblikovanje in prilagajanje pozivov.              | Lažje za integracijo v arhitekturo AI agenta.       |

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

### Ovrednotenje relevantnosti

Ovrednotenje relevantnosti je ključen vidik delovanja AI agenta. Zagotavlja, da so informacije, pridobljene in generirane s strani agenta, primerne, točne in koristne za uporabnika. Oglejmo si, kako ovrednotiti relevantnost v AI agentih, vključno s praktičnimi primeri in tehnikami.

#### Ključni pojmi pri ovrednotenju relevantnosti

1. **Zavedanje konteksta**:
   - Agent mora razumeti kontekst uporabnikove poizvedbe, da lahko pridobi in generira relevantne informacije.
   - Primer: Če uporabnik vpraša za "najboljše restavracije v Parizu", mora agent upoštevati uporabnikove preference, kot so vrsta kuhinje in proračun.

2. **Natančnost**:
   - Informacije, ki jih agent zagotovi, morajo biti dejansko pravilne in ažurne.
   - Primer: Priporočanje trenutno odprtih restavracij z dobrimi ocenami, ne pa zastarelih ali zaprtih možnosti.

3. **Namen uporabnika**:
   - Agent mora razvozlati uporabnikov namen poizvedbe in ponuditi najbolj relevantne informacije.
   - Primer: Če uporabnik vpraša za "cenovno ugodne hotele", mora agent dati prednost dostopnim možnostim.

4. **Zanka povratnih informacij**:
   - Nenehno zbiranje in analiziranje uporabniških povratnih informacij pomaga agentu izboljšati proces ovrednotenja relevantnosti.
   - Primer: Vključevanje ocen in povratnih informacij uporabnikov o prejšnjih priporočilih za izboljšanje prihodnjih odgovorov.

#### Praktične tehnike za ovrednotenje relevantnosti

1. **Ocena relevantnosti**:
   - Dodelite oceno relevantnosti vsakemu pridobljenemu elementu glede na to, kako dobro ustreza uporabnikovi poizvedbi in željam.
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
   - Odstranite nerelevantne elemente in preostale razporedite glede na njihove ocene relevantnosti.
   - Primer:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Vrni prvih 10 relevantnih elementov
     ```

3. **Obdelava naravnega jezika (NLP)**:
   - Uporabite NLP tehnike za razumevanje uporabnikove poizvedbe in pridobitev relevantnih informacij.
   - Primer:

     ```python
     def process_query(query):
         # Uporabite NPL za izločanje ključnih informacij iz uporabnikovega poizvedovanja
         processed_query = nlp(query)
         return processed_query
     ```

4. **Vključevanje povratnih informacij uporabnikov**:
   - Zbirajte uporabniške povratne informacije o podanih priporočilih in jih uporabite za prilagoditev prihodnjih ovrednotenji relevantnosti.
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

#### Primer: Ovrednotenje relevantnosti v turističnem agentu

Tukaj je praktičen primer, kako lahko turistični agent ovrednoti relevantnost potovalnih priporočil:

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
        return ranked_items[:10]  # Vrni prvih 10 ustreznih elementov

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

Iskanje z namenom vključuje razumevanje in interpretacijo osnovnega namena ali cilja uporabnikove poizvedbe za pridobitev in generiranje najbolj relevantnih in koristnih informacij. Ta pristop presega zgolj ujemanje ključnih besed in se osredotoča na razumevanje dejanskih potreb in konteksta uporabnika.

#### Ključni pojmi pri iskanju z namenom

1. **Razumevanje uporabnikovega namena**:
   - Namen uporabnika lahko razvrstimo v tri glavne vrste: informacijski, navigacijski in transakcijski.
     - **Informacijski namen**: Uporabnik išče informacije o določeni temi (npr. "Kateri so najboljši muzeji v Parizu?").
     - **Navigacijski namen**: Uporabnik želi dostopati do določene spletne strani ali strani (npr. "Uradna spletna stran muzeja Louvre").
     - **Transakcijski namen**: Uporabnik želi opraviti transakcijo, kot je rezervacija leta ali nakup (npr. "Rezerviraj let v Pariz").

2. **Zavedanje konteksta**:
   - Analiza konteksta uporabnikove poizvedbe pomaga natančno identificirati njegov namen. To vključuje upoštevanje prejšnjih interakcij, uporabnikovih želja in specifičnih podrobnosti trenutne poizvedbe.

3. **Obdelava naravnega jezika (NLP)**:
   - NLP tehnike se uporabljajo za razumevanje in interpretacijo poizvedb v naravnem jeziku, ki jih podajo uporabniki. To vključuje naloge, kot so prepoznavanje entitet, analiza sentimenta in razčlenjevanje poizvedb.

4. **Personalizacija**:
   - Prilagajanje rezultatov iskanja glede na uporabnikovo zgodovino, preference in povratne informacije izboljšuje relevantnost pridobljenih informacij.

#### Praktičen primer: Iskanje z namenom v turističnem agentu

Poglejmo si primer turističnega agenta, da vidimo, kako se lahko implementira iskanje z namenom.

1. **Zbiranje želja uporabnika**

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
       # Primer iskalne logike za informacijsko namero
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Primer iskalne logike za navigacijsko namero
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Primer iskalne logike za transakcijsko namero
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

Agentje za generiranje kode uporabljajo AI modele za pisanje in izvajanje kode, reševanje kompleksnih problemov in avtomatizacijo nalog.

### Agentje za generiranje kode

Agentje za generiranje kode uporabljajo generativne AI modele za pisanje in izvajanje kode. Ti agentje lahko rešujejo kompleksne probleme, avtomatizirajo naloge in ponujajo dragocene vpoglede z ustvarjanjem in izvajanjem kode v različnih programskih jezikih.

#### Praktične uporabe

1. **Avtomatizirano generiranje kode**: Ustvarjanje delcev kode za določene naloge, kot so analiza podatkov, spletno strganje ali strojno učenje.
2. **SQL kot RAG**: Uporaba SQL poizvedb za iskanje in manipulacijo podatkov v podatkovnih bazah.
3. **Reševanje problemov**: Pisanje in izvajanje kode za reševanje določenih problemov, kot je optimizacija algoritmov ali analiza podatkov.

#### Primer: Agent za generiranje kode za analizo podatkov

Predstavljajte si, da načrtujete agenta za generiranje kode. Tako bi lahko deloval:

1. **Naloga**: Analizirati podatkovni niz za prepoznavanje trendov in vzorcev.
2. **Koraki**:
   - Naložite podatkovni niz v orodje za analizo podatkov.
   - Ustvarite SQL poizvedbe za filtriranje in agregiranje podatkov.
   - Izvedite poizvedbe in pridobite rezultate.
   - Uporabite rezultate za ustvarjanje vizualizacij in vpogledov.
3. **Potrebni viri**: Dostop do podatkovnega niza, orodij za analizo podatkov in SQL zmožnosti.
4. **Izkušnje**: Uporabite pretekle rezultate za izboljšanje natančnosti in relevantnosti prihodnjih analiz.

### Primer: Agent za generiranje kode za potovalno agencijo

V tem primeru bomo oblikovali agenta za generiranje kode, Potovalna agencija, ki uporabnikom pomaga pri načrtovanju potovanja z ustvarjanjem in izvajanjem kode. Ta agent lahko obvladuje naloge, kot so pridobivanje potovalnih možnosti, filtriranje rezultatov in sestavljanje itinerarja z uporabo generativne AI.

#### Pregled agenta za generiranje kode

1. **Zbiranje uporabniških preferenc**: Zbira uporabniške vnose, kot so destinacija, datumi potovanja, proračun in zanimanja.
2. **Generiranje kode za pridobivanje podatkov**: Ustvarja delce kode za pridobivanje podatkov o letih, hotelih in znamenitostih.
3. **Izvajanje ustvarjene kode**: Izvaja ustvarjeno kodo za pridobitev informacij v realnem času.
4. **Sestavljanje itinerarja**: Združi pridobljene podatke v personaliziran načrt potovanja.
5. **Prilagajanje na povratne informacije**: Prejema povratne informacije uporabnika in po potrebi ponovno generira kodo za izboljšanje rezultatov.

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

3. **Izvajanje ustvarjene kode**

   ```python
   def execute_code(code):
       # Zaženi generirano kodo z uporabo exec
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
   
   # Ponovno ustvarite in izvedite kodo z posodobljenimi nastavitvami
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Izkoriščanje okoljske ozaveščenosti in sklepanja

Na podlagi sheme tabele lahko res izboljšamo postopek generiranja poizvedb z izkoriščanjem okoljske ozaveščenosti in sklepanja.

Tukaj je primer, kako to lahko storimo:

1. **Razumevanje sheme**: Sistem bo razumel shemo tabele in uporabil te informacije kot osnovo za generiranje poizvedb.
2. **Prilagajanje na podlagi povratnih informacij**: Sistem bo prilagodil uporabniške preference glede na povratne informacije in presodil, katera polja v shemi je treba posodobiti.
3. **Generiranje in izvajanje poizvedb**: Sistem bo generiral in izvajal poizvedbe za pridobivanje posodobljenih podatkov o letih in hotelih glede na nove preference.

Tukaj je posodobljen primer kode v Pythonu, ki vključuje te koncepte:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Prilagodite nastavitve na podlagi povratnih informacij uporabnikov
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Razmišljanje na podlagi sheme za prilagoditev drugih povezanih nastavitev
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Po meri izdelana logika za prilagoditev nastavitev na podlagi sheme in povratnih informacij
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Ustvarite kodo za pridobivanje podatkov o letih na podlagi posodobljenih nastavitev
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Ustvarite kodo za pridobivanje podatkov o hotelih na podlagi posodobljenih nastavitev
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulirajte izvajanje kode in vrnite lažne podatke
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Ustvarite načrt poti na podlagi letov, hotelov in znamenitosti
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

# Ponovno ustvarite in izvedite kodo s posodobljenimi nastavitvami
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Pojasnilo - Rezervacija na podlagi povratnih informacij

1. **Ozaveščenost o shemi**: Slovar `schema` določa, kako je treba prilagoditi preference glede na povratne informacije. Vsebuje polja, kot so `favorites` in `avoid` s pripadajočimi prilagoditvami.
2. **Prilagajanje preferenc (`adjust_based_on_feedback` metoda)**: Ta metoda prilagaja preference glede na povratne informacije uporabnika in shemo.
3. **Prilagoditve na podlagi okolja (`adjust_based_on_environment` metoda)**: Ta metoda prilagaja prilagoditve na podlagi sheme in povratnih informacij.
4. **Generiranje in izvajanje poizvedb**: Sistem generira kodo za pridobitev posodobljenih podatkov o letih in hotelih glede na prilagojene preference ter simulira izvajanje teh poizvedb.
5. **Generiranje itinerarja**: Sistem ustvari posodobljen itinerar na podlagi novih podatkov o letih, hotelih in znamenitostih.

S tem, ko sistem naredimo okoljsko ozaveščen in sklepamo na podlagi sheme, lahko generira natančnejše in bolj relevantne poizvedbe, kar vodi do boljših potovalnih priporočil in bolj personalizirane uporabniške izkušnje.

### Uporaba SQL kot tehnike Retrieval-Augmented Generation (RAG)

SQL (Structured Query Language) je močno orodje za interakcijo s podatkovnimi bazami. Ko se uporablja kot del pristopa Retrieval-Augmented Generation (RAG), lahko SQL pridobi relevantne podatke iz podatkovnih baz za informiranje in generiranje odzivov ali dejanj v AI agentih. Raziskujmo, kako se lahko SQL uporablja kot RAG tehnika v kontekstu Potovalne agencije.

#### Ključni koncepti

1. **Interakcija s podatkovno bazo**:
   - SQL se uporablja za poizvedovanje podatkovnih baz, pridobivanje relevantnih informacij in manipulacijo podatkov.
   - Primer: pridobivanje podatkov o letih, informacij o hotelih in znamenitostih iz potovalne baze.

2. **Integracija z RAG**:
   - SQL poizvedbe se generirajo na podlagi uporabniških vnosov in preferenc.
   - Pridobljeni podatki se nato uporabijo za generiranje personaliziranih priporočil ali dejanj.

3. **Dinamično generiranje poizvedb**:
   - AI agent generira dinamične SQL poizvedbe glede na kontekst in potrebe uporabnika.
   - Primer: prilagajanje SQL poizvedb za filtriranje rezultatov glede na proračun, datume in zanimanja.

#### Uporabe

- **Avtomatizirano generiranje kode**: ustvarjanje delcev kode za določene naloge.
- **SQL kot RAG**: uporaba SQL poizvedb za manipulacijo podatkov.
- **Reševanje problemov**: pisanje in izvajanje kode za reševanje problemov.

**Primer**:
Agent za analizo podatkov:

1. **Naloga**: analizirati podatkovni niz za iskanje trendov.
2. **Koraki**:
   - Naloži podatkovni niz.
   - Ustvari SQL poizvedbe za filtriranje podatkov.
   - Izvedi poizvedbe in pridobi rezultate.
   - Ustvari vizualizacije in vpoglede.
3. **Viri**: dostop do podatkovnega niza, SQL zmožnosti.
4. **Izkušnje**: uporabi pretekle rezultate za izboljšanje prihodnjih analiz.

#### Praktičen primer: Uporaba SQL v Potovalni agenciji

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

#### Primeri SQL poizvedb

1. **Poizvedba za let**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Poizvedba za hotel**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Poizvedba za znamenitost**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Z uporabo SQL kot dela tehnike Retrieval-Augmented Generation (RAG), AI agenti kot je Potovalna agencija lahko dinamično pridobivajo in uporabljajo relevantne podatke za zagotavljanje natančnih in personaliziranih priporočil.

### Primer metakognicije

Za demonstracijo implementacije metakognicije ustvarimo preprostega agenta, ki *razmišlja o svojem procesu odločanja* med reševanjem problema. V tem primeru bomo zgradili sistem, kjer agent poskuša optimizirati izbiro hotela, nato pa oceni svoje sklepanje in prilagodi strategijo, ko naredi napake ali podoptimalne izbire.

To bomo simulirali z osnovnim primerom, kjer agent izbira hotele na podlagi kombinacije cene in kakovosti, vendar "razmišlja" o svojih odločitvah in se temu primerno prilagodi.

#### Kako to ilustrira metakognicijo:

1. **Začetna odločitev**: Agent bo izbral najcenejši hotel, brez razumevanja vpliva kakovosti.
2. **Razmislek in ocena**: Po začetni izbiri agent preveri, ali je hotel "slaba" izbira z uporabo povratnih informacij uporabnika. Če ugotovi, da je bila kakovost hotela prenizka, razmišlja o svojem sklepanju.
3. **Prilagoditev strategije**: Agent prilagodi strategijo na podlagi svojih razmislekov in preklopi iz izbire "najcenejšega" na "najvišjo kakovost", s čimer izboljša svoj proces odločanja v prihodnjih iteracijah.

Tukaj je primer:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Shrani prej izbrane hotele
        self.corrected_choices = []  # Shrani popravljene izbire
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Na voljo strategije

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
        # Predpostavimo, da imamo povratne informacije uporabnika, ki nam povedo, ali je bila zadnja izbira dobra ali ne
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

# Simulira seznam hotelov (cena in kakovost)
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

# Korak 2: Agent premisli o izbiri in po potrebi prilagodi strategijo
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Korak 3: Agent ponovno priporoči, tokrat z uporabljeno prilagojeno strategijo
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Zmožnosti metakognicije agentov

Ključno tukaj je sposobnost agenta, da:
- Ocenjuje svoje prejšnje izbire in proces odločanja.
- Prilagaja svojo strategijo na podlagi tega razmisleka, tj. metakognicija v akciji.

To je preprosta oblika metakognicije, kjer sistem lahko prilagodi svoj proces sklepanja na podlagi notranjih povratnih informacij.

### Zaključek

Metakognicija je močno orodje, ki lahko bistveno izboljša sposobnosti AI agentov. Z vključitvijo metakognitivnih procesov lahko oblikujemo agentje, ki so bolj inteligentni, prilagodljivi in učinkoviti. Uporabite dodatne vire, da dalje raziščete fascinanten svet metakognicije v AI agentih.

### Imate več vprašanj o vzorcu oblikovanja metakognicije?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) in se povežite z drugimi učenci, udeležite se ur ure in dobite odgovore na vprašanja o AI agentih.

## Prejšnja lekcija

[Vzorec večagentnega oblikovanja](../08-multi-agent/README.md)

## Naslednja lekcija

[AI agenti v produkciji](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->