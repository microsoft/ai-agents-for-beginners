[![Proiectare Multi-Agent](../../../translated_images/ro/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_
# Metacogniția în agenții AI

## Introducere

Bine ați venit la lecția despre metacogniția în agenții AI! Acest capitol este conceput pentru începători curioși despre cum agenții AI pot reflecta asupra propriilor lor procese de gândire. La finalul acestei lecții, veți înțelege conceptele cheie și veți fi echipat cu exemple practice pentru a aplica metacogniția în designul agenților AI.

## Obiective de învățare

După finalizarea acestei lecții, veți putea:

1. Să înțelegeți implicațiile buclelor de raționament în definițiile agenților.
2. Să folosiți tehnici de planificare și evaluare pentru a ajuta agenții autcorectivi.
3. Să creați proprii agenți capabili să manipuleze codul pentru a îndeplini sarcini.

## Introducere în Metacogniție

Metacogniția se referă la procesele cognitive de ordin superior care implică gândirea despre propria gândire. Pentru agenții AI, aceasta înseamnă a putea evalua și ajusta acțiunile pe baza conștientizării de sine și a experiențelor trecute. Metacogniția, sau „gândirea despre gândire”, este un concept important în dezvoltarea sistemelor AI agentice. Ea implică faptul că sistemele AI sunt conștiente de propriile lor procese interne și pot să le monitorizeze, să le regleze și să-și adapteze comportamentul în consecință. La fel cum facem noi când citim situația sau analizăm o problemă. Această conștientizare de sine poate ajuta sistemele AI să ia decizii mai bune, să identifice erori și să își îmbunătățească performanța în timp — făcând legătura cu testul Turing și dezbaterea dacă AI va prelua controlul.

În contextul sistemelor AI agentice, metacogniția poate ajuta la rezolvarea mai multor provocări, cum ar fi:
- Transparența: Asigurarea faptului că sistemele AI pot explica raționamentul și deciziile lor.
- Raționamentul: Îmbunătățirea capacității sistemelor AI de a sintetiza informații și a lua decizii corecte.
- Adaptarea: Permiterea sistemelor AI să se ajusteze la medii noi și condiții în schimbare.
- Percepția: Îmbunătățirea acurateței sistemelor AI în recunoașterea și interpretarea datelor din mediul înconjurător.

### Ce este Metacogniția?

Metacogniția, sau „gândirea despre gândire”, este un proces cognitiv de ordin superior care implică conștientizarea de sine și autoreglarea propriilor procese cognitive. În domeniul AI, metacogniția oferă agenților capacitatea de a evalua și adapta strategiile și acțiunile lor, ducând la îmbunătățirea abilităților de rezolvare a problemelor și luare a deciziilor. Prin înțelegerea metacogniției, poți proiecta agenți AI care nu sunt doar mai inteligenți, ci și mai adaptabili și eficienți. În metacogniția adevărată, ai vedea AI raționând explicit despre propriul său raționament.

Exemplu: „Am prioritizat zborurile mai ieftine pentru că… s-ar putea să ratez zborurile directe, așa că să verific din nou.”.
Urmărirea modului sau motivului pentru care a ales o anumită rută.
- Observarea că a făcut greșeli pentru că a avut prea multă încredere în preferințele utilizatorului de data trecută, așa că își modifică strategia de luare a deciziilor, nu doar recomandarea finală.
- Diagnosticarea unor tipare precum, „Ori de câte ori văd că utilizatorul menționează 'prea aglomerat', nu trebuie doar să elimin anumite atracții, ci să reflectez că metoda mea de alegere a ‘atracțiilor principale’ este defectuoasă dacă întotdeauna le clasez după popularitate.”

### Importanța Metacogniției în Agenții AI

Metacogniția joacă un rol crucial în designul agenților AI din mai multe motive:

![Importanța Metacogniției](../../../translated_images/ro/importance-of-metacognition.b381afe9aae352f7.webp)

- Auto-reflecție: Agenții pot evalua propria performanță și identifica zone de îmbunătățire.
- Adaptabilitate: Agenții pot modifica strategiile bazate pe experiențele anterioare și mediile schimbătoare.
- Corectarea erorilor: Agenții pot detecta și corecta autonom erorile, conducând la rezultate mai precise.
- Gestionarea resurselor: Agenții pot optimiza utilizarea resurselor, cum ar fi timpul și puterea de calcul, prin planificarea și evaluarea acțiunilor.

## Componentele unui Agent AI

Înainte de a intra în procesele metacognitive, este esențial să înțelegem componentele de bază ale unui agent AI. Un agent AI constă tipic din:

- Persona: Personalitatea și caracteristicile agentului, care definesc modul în care interacționează cu utilizatorii.
- Instrumente: Capacitățile și funcțiile pe care agentul le poate efectua.
- Abilități: Cunoștințele și expertiza pe care agentul le posedă.

Aceste componente lucrează împreună pentru a crea o „unitate de expertiză” capabilă să realizeze sarcini specifice.

**Exemplu**:
Gândiți-vă la un agent de turism, un serviciu de agenție care nu doar planifică vacanța ta, ci ajustează și traseul bazat pe date în timp real și experiențe anterioare ale clienților.

### Exemplu: Metacogniția într-un Serviciu de Agenție de Turism

Imaginează-ți că proiectezi un serviciu de agenție de turism alimentat de AI. Acest agent, „Agentul de Turism,” asistă utilizatorii în planificarea concediilor. Pentru a încorpora metacogniția, Agentul de Turism trebuie să evalueze și să își ajusteze acțiunile bazate pe conștientizare de sine și experiențe trecute. Iată cum metacogniția ar putea juca un rol:

#### Sarcina Curentă

Sarcina actuală este să ajuți un utilizator să-și planifice o călătorie la Paris.

#### Pași pentru Finalizarea Sarcinii

1. **Colectarea preferințelor utilizatorului**: Întreabă utilizatorul despre datele de călătorie, buget, interese (de exemplu, muzee, gastronomie, cumpărături) și orice cerințe specifice.
2. **Recuperarea informațiilor**: Caută opțiuni de zbor, cazare, atracții și restaurante care corespund preferințelor utilizatorului.
3. **Generarea recomandărilor**: Oferă un itinerar personalizat cu detalii pentru zbor, rezervări la hotel și activități sugerate.
4. **Ajustarea pe baza feedback-ului**: Cere utilizatorului să ofere feedback asupra recomandărilor și fă ajustările necesare.

#### Resurse Necesare

- Acces la baze de date pentru rezervări de zboruri și hoteluri.
- Informații despre atracțiile și restaurantele pariziene.
- Date de feedback ale utilizatorului din interacțiunile anterioare.

#### Experiență și Auto-reflecție

Agentul de Turism folosește metacogniția pentru a evalua performanța și a învăța din experiențele trecute. De exemplu:

1. **Analiza feedback-ului utilizatorului**: Agentul de Turism revizuiește feedback-ul utilizatorului pentru a determina care recomandări au fost bine primite și care nu. Își ajustează sugestiile viitoare în consecință.
2. **Adaptabilitate**: Dacă utilizatorul a menționat anterior că nu-i plac locurile aglomerate, Agentul de Turism va evita să recomande zone turistice populare în orele de vârf.
3. **Corectarea erorilor**: Dacă Agentul de Turism a făcut o greșeală la o rezervare anterioară, cum ar fi sugerarea unui hotel complet rezervat, învață să verifice mai riguros disponibilitatea înainte de a face recomandări.

#### Exemplu practic pentru dezvoltatori

Iată un exemplu simplificat despre cum ar putea arăta codul Agentului de Turism când încorporează metacogniția:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Căutați zboruri, hoteluri și atracții bazate pe preferințe
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
        # Analizați feedback-ul și ajustați recomandările viitoare
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Exemplu de utilizare
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

#### De ce contează Metacogniția

- **Auto-reflecție**: Agenții pot analiza performanța și identifica zone de îmbunătățire.
- **Adaptabilitate**: Agenții pot modifica strategiile în funcție de feedback și condiții în schimbare.
- **Corectarea erorilor**: Agenții pot detecta și corecta autonom greșelile.
- **Gestionarea resurselor**: Agenții pot optimiza utilizarea resurselor, cum ar fi timpul și puterea de calcul.

Prin încorporarea metacogniției, Agentul de Turism poate oferi recomandări mai personalizate și precise pentru călătorii, îmbunătățind experiența generală a utilizatorului.

---

## 2. Planificarea în Agenți

Planificarea este o componentă critică a comportamentului agenților AI. Ea implică detalierea pașilor necesari pentru atingerea unui obiectiv, luând în considerare starea curentă, resursele și posibile obstacole.

### Elemente ale Planificării

- **Sarcina Curentă**: Definirea clară a sarcinii.
- **Pașii pentru Finalizarea Sarcinii**: Împărțirea sarcinii în pași gestionabili.
- **Resursele Necesare**: Identificarea resurselor necesare.
- **Experiența**: Utilizarea experiențelor anterioare pentru a informa planificarea.

**Exemplu**:
Iată pașii pe care Agentul de Turism trebuie să îi urmeze pentru a ajuta eficient un utilizator să își planifice călătoria:

### Pași pentru Agentul de Turism

1. **Colectarea preferințelor utilizatorului**
   - Întreabă utilizatorul detalii despre datele călătoriei, buget, interese și orice cerințe specifice.
   - Exemple: „Când planificați să călătoriți?” „Care este intervalul bugetului dvs.?” „Ce activități vă plac în vacanță?”

2. **Recuperarea informațiilor**
   - Caută opțiuni relevante de călătorie pe baza preferințelor utilizatorului.
   - **Zboruri**: Caută zboruri disponibile în bugetul și datele preferate ale utilizatorului.
   - **Cazări**: Găsește hoteluri sau proprietăți de închiriat care corespund preferințelor de locație, preț și facilități.
   - **Atracții și restaurante**: Identifică atracții populare, activități și opțiuni de luat masa care se potrivesc intereselor utilizatorului.

3. **Generarea Recomandărilor**
   - Compilează informațiile obținute într-un itinerar personalizat.
   - Oferă detalii cum ar fi opțiuni de zbor, rezervări la hotel și activități sugerate, adaptând recomandările la preferințele utilizatorului.

4. **Prezentarea itinerarului utilizatorului**
   - Împărtășește itinerarul propus pentru revizuire.
   - Exemplu: „Iată un itinerar sugerat pentru călătoria dvs. la Paris. Include detalii despre zbor, rezervări la hotel și o listă de activități și restaurante recomandate. Aștept părerea dvs.!”

5. **Colectarea feedback-ului**
   - Cere utilizatorului feedback despre itinerar.
   - Exemple: „Vă plac opțiunile de zbor?” „Este hotelul potrivit pentru nevoile dvs.?” „Sunt activități pe care doriți să le adăugați sau să le eliminați?”

6. **Ajustarea pe baza feedback-ului**
   - Modifică itinerarul conform feedback-ului utilizatorului.
   - Fă schimbările necesare la recomandările despre zbor, cazare și activități pentru a se potrivi mai bine preferințelor utilizatorului.

7. **Confirmarea finală**
   - Prezintă itinerarul actualizat utilizatorului pentru confirmarea finală.
   - Exemplu: „Am făcut ajustările conform feedback-ului dvs. Iată itinerarul actualizat. Este totul în regulă?”

8. **Rezervarea și confirmarea rezervărilor**
   - După aprobarea utilizatorului, continuă cu rezervarea zborurilor, cazărilor și activităților pre-planificate.
   - Trimite detaliile de confirmare utilizatorului.

9. **Asistență continuă**
   - Rămâi disponibil pentru a asista utilizatorul cu orice modificări sau cereri suplimentare înainte și în timpul călătoriei.
   - Exemplu: „Dacă aveți nevoie de asistență suplimentară în timpul călătoriei, nu ezitați să mă contactați oricând!”

### Exemplu de Interacțiune

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

# Exemplu de utilizare într-o solicitare de rezervare
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

## 3. Sistem RAG Corectiv

În primul rând, să înțelegem diferența dintre Instrumentul RAG și Încărcarea Pre-emptivă a Contextului.

![RAG vs Încărcarea Contextului](../../../translated_images/ro/rag-vs-context.9eae588520c00921.webp)

### Generarea cu Suport de Recuperare (RAG)

RAG combină un sistem de recuperare cu un model generativ. Când se face o interogare, sistemul de recuperare aduce documente sau date relevante dintr-o sursă externă, iar aceste informații recuperate sunt folosite pentru a completa intrarea modelului generativ. Acest lucru ajută modelul să genereze răspunsuri mai precise și relevante contextual.

Într-un sistem RAG, agentul recuperează informații relevante dintr-o bază de cunoștințe și le folosește pentru a genera răspunsuri sau acțiuni adecvate.

### Abordarea RAG Corectivă

Abordarea RAG Corectivă se concentrează pe utilizarea tehnicilor RAG pentru corectarea erorilor și îmbunătățirea acurateței agenților AI. Aceasta implică:

1. **Tehnica de promptare**: Folosirea unor indicații specifice pentru a ghida agentul în recuperarea informațiilor relevante.
2. **Instrumentul**: Implementarea algoritmilor și mecanismelor care permit agentului să evalueze relevanța informațiilor recuperate și să genereze răspunsuri corecte.
3. **Evaluarea**: Evaluarea continuă a performanței agentului și efectuarea ajustărilor pentru a-i îmbunătăți precizia și eficiența.

#### Exemplu: RAG Corectiv într-un Agent de Căutare

Luați în considerare un agent de căutare care recuperează informații de pe web pentru a răspunde la întrebările utilizatorului. Abordarea RAG Corectivă ar putea implica:

1. **Tehnica de promptare**: Formularea interogărilor de căutare pe baza inputului utilizatorului.
2. **Instrumentul**: Folosirea procesării limbajului natural și a algoritmilor de învățare automată pentru a clasifica și filtra rezultatele căutării.
3. **Evaluarea**: Analiza feedback-ului utilizatorului pentru a identifica și corecta inexactitățile din informațiile recuperate.

### RAG Corectiv în Agentul de Turism

RAG Corectiv (Generare cu Suport de Recuperare) îmbunătățește abilitatea AI-ului de a recupera și genera informații, corectând orice inexactități. Să vedem cum Agentul de Turism poate folosi abordarea RAG Corectiv pentru a oferi recomandări de călătorie mai precise și relevante.

Aceasta implică:

- **Tehnica de promptare:** Folosirea unor întrebări specifice pentru a ghida agentul în recuperarea informațiilor relevante.
- **Instrumentul:** Implementarea algoritmilor și mecanismelor care permit agentului să evalueze relevanța informațiilor recuperate și să genereze răspunsuri precise.
- **Evaluarea:** Evaluarea continuă a performanței agentului și ajustarea pentru a îmbunătăți precizia și eficiența.

#### Pași pentru implementarea RAG Corectiv în Agentul de Turism

1. **Interacțiunea inițială cu utilizatorul**
   - Agentul de Turism colectează preferințele inițiale ale utilizatorului, cum ar fi destinația, datele de călătorie, bugetul și interesele.
   - Exemplu:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Recuperarea informațiilor**
   - Agentul de Turism recuperează informații despre zboruri, cazare, atracții și restaurante pe baza preferințelor utilizatorului.
   - Exemplu:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generarea recomandărilor inițiale**
   - Agentul de Turism folosește informațiile recuperate pentru a genera un itinerar personalizat.
   - Exemplu:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Colectarea feedback-ului utilizatorului**
   - Agentul de Turism cere utilizatorului să ofere feedback asupra recomandărilor inițiale.
   - Exemplu:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Procesul RAG Corectiv**
   - **Tehnica de promptare**: Agentul de Turism formulează noi interogări de căutare pe baza feedback-ului utilizatorului.
     - Exemplu:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Instrumentul**: Agentul de Turism folosește algoritmi pentru a clasifica și filtra rezultatele noi ale căutării, punând accent pe relevanța bazată pe feedback-ul utilizatorului.
     - Exemplu:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Evaluarea**: Agentul de Turism evaluează continuu relevanța și acuratețea recomandărilor analizând feedback-ul și efectuând ajustările necesare.
     - Exemplu:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Exemplu practic

Iată un exemplu simplificat de cod Python care încorporează abordarea RAG Corectivă în Agentul de Turism:

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

# Exemplu de utilizare
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

### Încărcarea Pre-emptivă a Contextului
Pre-emptive Context Load implică încărcarea prealabilă a contextului relevant sau a informațiilor de fundal în model înainte de procesarea unei interogări. Aceasta înseamnă că modelul are acces la aceste informații încă de la început, ceea ce îl poate ajuta să genereze răspunsuri mai bine informate, fără a necesita să recupereze date suplimentare în timpul procesului.

Iată un exemplu simplificat despre cum ar putea arăta un pre-emptive context load pentru o aplicație de agent de turism în Python:

```python
class TravelAgent:
    def __init__(self):
        # Preîncarcă destinațiile populare și informațiile acestora
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Preia informațiile despre destinație din contextul preîncărcat
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Exemplu de utilizare
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Explicație

1. **Inițializare (metoda `__init__`)**: Clasa `TravelAgent` preîncarcă un dicționar care conține informații despre destinații populare cum ar fi Paris, Tokyo, New York și Sydney. Acest dicționar include detalii precum țara, moneda, limba și atracțiile principale pentru fiecare destinație.

2. **Preluarea informațiilor (metoda `get_destination_info`)**: Când un utilizator întreabă despre o destinație specifică, metoda `get_destination_info` preia informațiile relevante din dicționarul preîncărcat de context.

Prin preîncărcarea contextului, aplicația agentului de turism poate răspunde rapid la întrebările utilizatorilor fără a fi necesară recuperarea acestor informații dintr-o sursă externă în timp real. Acest lucru face aplicația mai eficientă și mai receptivă.

### Bootstrapping-ul planului cu un scop înainte de iterație

Bootstrapping-ul unui plan cu un scop implică începerea cu un obiectiv clar sau un rezultat țintă în minte. Prin definirea acestui scop încă de la început, modelul îl poate folosi ca principiu călăuzitor pe tot parcursul procesului iterativ. Acest lucru ajută la asigurarea că fiecare iterație se apropie de realizarea rezultatului dorit, făcând procesul mai eficient și concentrat.

Iată un exemplu de cum ai putea să bootstrapezi un plan de călătorie cu un scop înainte de a itera, pentru un agent de turism în Python:

### Scenariu

Un agent de turism dorește să planifice o vacanță personalizată pentru un client. Scopul este de a crea un itinerar de călătorie care să maximizeze satisfacția clientului în funcție de preferințele și bugetul acestuia.

### Pași

1. Definirea preferințelor clientului și a bugetului.
2. Bootstrap-ul planului inițial pe baza acestor preferințe.
3. Iterarea pentru rafinarea planului, optimizând pentru satisfacția clientului.

#### Cod Python

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

# Exemplu de utilizare
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

#### Explicația codului

1. **Inițializare (metoda `__init__`)**: Clasa `TravelAgent` este inițializată cu o listă de destinații potențiale, fiecare având atribute precum nume, cost și tip de activitate.

2. **Bootstrapping-ul planului (metoda `bootstrap_plan`)**: Această metodă creează un plan inițial de călătorie pe baza preferințelor clientului și a bugetului. Parcurge lista de destinații și le adaugă în plan dacă se potrivesc cu preferințele clientului și se încadrează în buget.

3. **Potrivirea preferințelor (metoda `match_preferences`)**: Această metodă verifică dacă o destinație corespunde preferințelor clientului.

4. **Iterarea planului (metoda `iterate_plan`)**: Această metodă rafinează planul inițial încercând să înlocuiască fiecare destinație din plan cu o potrivire mai bună, luând în considerare preferințele clientului și constrângerile bugetare.

5. **Calcularea costului (metoda `calculate_cost`)**: Această metodă calculează costul total al planului curent, inclusiv o destinație nouă potențială.

#### Exemplu de utilizare

- **Plan inițial**: Agentul de turism creează un plan inițial bazat pe preferințele clientului pentru obiective turistice și un buget de 2000$.
- **Plan rafinat**: Agentul de turism iterează planul, optimizând în funcție de preferințele și bugetul clientului.

Prin bootstrapping-ul planului cu un scop clar (de exemplu, maximizarea satisfacției clientului) și iterarea pentru rafinarea planului, agentul de turism poate crea un itinerar personalizat și optimizat pentru client. Această abordare asigură că planul de călătorie este în concordanță cu preferințele și bugetul clientului încă de la început și se îmbunătățește cu fiecare iterație.

### Folosirea avantajelor LLM pentru re-evaluare și scorare

Modelele lingvistice mari (LLM-uri) pot fi folosite pentru re-evaluarea și scorarea evaluând relevanța și calitatea documentelor recuperate sau a răspunsurilor generate. Iată cum funcționează:

**Recuperare:** Pasul inițial de recuperare obține un set de documente sau răspunsuri candidate pe baza interogării.

**Re-evaluare:** LLM-ul evaluează aceste candidați și îi reordonează pe baza relevanței și calității lor. Acest pas asigură că cele mai relevante și calitative informații sunt prezentate primele.

**Scorare:** LLM-ul atribuie scoruri fiecărui candidat, reflectând relevanța și calitatea lor. Acest lucru ajută la selectarea celui mai bun răspuns sau document pentru utilizator.

Prin folosirea LLM-urilor pentru re-evaluare și scorare, sistemul poate oferi informații mai precise și relevante contextual, îmbunătățind experiența generală a utilizatorului.

Iată un exemplu de cum un agent de turism poate folosi un Model Lingvistic Mare (LLM) pentru re-evaluarea și scorarea destinațiilor turistice pe baza preferințelor utilizatorului în Python:

#### Scenariu - Călătorie pe baza Preferințelor

Un agent de turism dorește să recomande cele mai bune destinații turistice unui client, pe baza preferințelor acestuia. LLM-ul va ajuta la re-evaluarea și scorarea destinațiilor pentru a asigura că cele mai relevante opțiuni sunt prezentate.

#### Pași:

1. Colectarea preferințelor utilizatorului.
2. Preluarea unei liste de potențiale destinații de călătorie.
3. Folosirea LLM-ului pentru re-evaluarea și scorarea destinațiilor pe baza preferințelor utilizatorului.

Iată cum poți actualiza exemplul anterior pentru a folosi Azure OpenAI Services:

#### Cerințe

1. Trebuie să ai un abonament Azure.
2. Creează o resursă Azure OpenAI și obține cheia ta API.

#### Exemplu cod Python

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generează un prompt pentru Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Definește antetele și conținutul cererii
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Apelează API-ul Azure OpenAI pentru a obține destinațiile reordonate și evaluate
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extrage și returnează recomandările
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

# Exemplu de utilizare
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

#### Explicația codului - Preference Booker

1. **Inițializare**: Clasa `TravelAgent` este inițializată cu o listă de destinații potențiale, fiecare având atribute precum nume și descriere.

2. **Obținerea recomandărilor (metoda `get_recommendations`)**: Această metodă generează un prompt pentru serviciul Azure OpenAI, bazat pe preferințele utilizatorului, și face o cerere HTTP POST către API-ul Azure OpenAI pentru a obține destinații re-evaluate și scorate.

3. **Generarea promptului (metoda `generate_prompt`)**: Această metodă construiește un prompt pentru Azure OpenAI, incluzând preferințele utilizatorului și lista de destinații. Promptul ghidează modelul să re-evalueze și să scorneze destinațiile bazat pe preferințele furnizate.

4. **Apel API**: Biblioteca `requests` este folosită pentru a face o cerere HTTP POST la endpoint-ul API Azure OpenAI. Răspunsul conține destinațiile re-evaluate și scorate.

5. **Exemplu de utilizare**: Agentul de turism colectează preferințele utilizatorului (de exemplu, interes în obiective turistice și cultură diversă) și folosește serviciul Azure OpenAI pentru a obține recomandări re-evaluate și scorate pentru destinațiile turistice.

Asigură-te că înlocuiești `your_azure_openai_api_key` cu cheia ta reală API Azure OpenAI și `https://your-endpoint.com/...` cu URL-ul real al endpoint-ului pentru implementarea Azure OpenAI.

Prin folosirea LLM-ului pentru re-evaluare și scorare, agentul de turism poate oferi recomandări mai personalizate și relevante pentru clienți, îmbunătățindu-le experiența generală.

### RAG: Tehnică de Promptare vs Unealtă

Retrieval-Augmented Generation (RAG) poate fi atât o tehnică de promptare cât și o unealtă în dezvoltarea agenților AI. Înțelegerea distincției între cele două te poate ajuta să folosești RAG mai eficient în proiectele tale.

#### RAG ca tehnică de promptare

**Ce este?**

- Ca tehnică de promptare, RAG implică formularea unor interogări sau prompturi specifice pentru a ghida recuperarea informațiilor relevante dintr-un corpus mare sau dintr-o bază de date. Aceste informații sunt apoi folosite pentru a genera răspunsuri sau acțiuni.

**Cum funcționează:**

1. **Formularea prompturilor**: Creează prompturi sau interogări bine structurate pe baza sarcinii sau a inputului utilizatorului.
2. **Recuperarea informațiilor**: Folosește prompturile pentru a căuta date relevante dintr-o bază de cunoștințe sau dataset preexistent.
3. **Generarea răspunsului**: Combină informațiile recuperate cu modele generative AI pentru a produce un răspuns cuprinzător și coerent.

**Exemplu în agentul de turism**:

- Input utilizator: „Vreau să vizitez muzee în Paris.”
- Prompt: „Găsește principalele muzee din Paris.”
- Informații recuperate: Detalii despre Muzeul Luvru, Musée d'Orsay etc.
- Răspuns generat: „Iată câteva muzee importante din Paris: Muzeul Luvru, Musée d'Orsay și Centre Pompidou.”

#### RAG ca unealtă

**Ce este?**

- Ca unealtă, RAG este un sistem integrat care automatizează procesul de recuperare și generare, făcând mai ușoară implementarea funcționalităților AI complexe de către dezvoltatori, fără a crea manual prompturi pentru fiecare interogare.

**Cum funcționează:**

1. **Integrare**: Încorporează RAG în arhitectura agentului AI, permițându-i să gestioneze automat sarcinile de recuperare și generare.
2. **Automatizare**: Unealta gestionează întregul proces, de la primirea input-ului utilizatorului până la generarea răspunsului final, fără a necesita prompturi explicite pentru fiecare pas.
3. **Eficiență**: Îmbunătățește performanța agentului prin optimizarea procesului de recuperare și generare, oferind răspunsuri mai rapide și mai precise.

**Exemplu în agentul de turism**:

- Input utilizator: „Vreau să vizitez muzee în Paris.”
- Unealta RAG: Recuperează automat informații despre muzee și generează un răspuns.
- Răspuns generat: „Iată câteva muzee importante din Paris: Muzeul Luvru, Musée d'Orsay și Centre Pompidou.”

### Comparatie

| Aspect                | Tehnică de promptare                                    | Unealtă                                              |
|-----------------------|---------------------------------------------------------|-----------------------------------------------------|
| **Manual vs Automat** | Formulare manuală a prompturilor pentru fiecare interogare. | Proces automatizat pentru recuperare și generare.  |
| **Control**           | Oferă mai mult control asupra procesului de recuperare. | Optimizează și automatizează procesul de recuperare și generare. |
| **Flexibilitate**     | Permite prompturi personalizate bazate pe nevoi specifice. | Mai eficient pentru implementări la scară largă.   |
| **Complexitate**      | Necesită elaborarea și ajustarea prompturilor.          | Mai ușor de integrat în arhitectura unui agent AI. |

### Exemple practice

**Exemplu tehnică de promptare:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Exemplu unealtă:**

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

### Evaluarea relevanței

Evaluarea relevanței este un aspect crucial al performanței agenților AI. Asigură că informațiile recuperate și generate de agent sunt adecvate, corecte și utile pentru utilizator. Să explorăm cum să evaluăm relevanța în agenții AI, inclusiv exemple practice și tehnici.

#### Concepte cheie în evaluarea relevanței

1. **Conștientizarea contextului**:
   - Agentul trebuie să înțeleagă contextul interogării utilizatorului pentru a recupera și genera informații relevante.
   - Exemplu: Dacă un utilizator solicită „cele mai bune restaurante din Paris,” agentul ar trebui să ia în considerare preferințele utilizatorului, cum ar fi tipul de bucătărie și bugetul.

2. **Acuratețe**:
   - Informațiile oferite de agent trebuie să fie corecte din punct de vedere factual și actualizate.
   - Exemplu: Recomandarea unor restaurante deschise în prezent și cu recenzii bune, nu opțiuni închise sau demodate.

3. **Intenția utilizatorului**:
   - Agentul trebuie să evalueze intenția utilizatorului în spatele interogării pentru a oferi cele mai relevante informații.
   - Exemplu: Dacă un utilizator cere „hoteluri accesibile ca preț,” agentul ar trebui să prioritizeze opțiunile cu prețuri rezonabile.

4. **Buclă de feedback**:
   - Colectarea și analizarea continuă a feedback-ului utilizatorului ajută agentul să își rafineze procesul de evaluare a relevanței.
   - Exemplu: Incorporarea notelor și feedback-ului utilizatorilor despre recomandările anterioare pentru a îmbunătăți răspunsurile viitoare.

#### Tehnici practice pentru evaluarea relevanței

1. **Scorarea relevanței**:
   - Atribuie un scor de relevanță fiecărui element recuperat, bazat pe cât de bine corespunde acesta interogării și preferințelor utilizatorului.
   - Exemplu:

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

2. **Filtrare și clasificare**:
   - Filtrează elementele irelevante și clasifică pe cele rămase după scorurile lor de relevanță.
   - Exemplu:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Returnează primele 10 elemente relevante
     ```

3. **Prelucrarea limbajului natural (NLP)**:
   - Folosește tehnici NLP pentru a înțelege interogarea utilizatorului și a recupera informații relevante.
   - Exemplu:

     ```python
     def process_query(query):
         # Folosiți NLP pentru a extrage informații cheie din interogarea utilizatorului
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integrarea feedback-ului utilizatorului**:
   - Colectează feedback-ul utilizatorilor despre recomandările oferite și îl folosește pentru ajustarea evaluărilor viitoare ale relevanței.
   - Exemplu:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Exemplu: Evaluarea relevanței în agentul de turism

Iată un exemplu practic despre cum Travel Agent poate evalua relevanța recomandărilor de călătorie:

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
        return ranked_items[:10]  # Returnează primele 10 articole relevante

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

# Exemplu de utilizare
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

### Căutare cu intenție

Căutarea cu intenție implică înțelegerea și interpretarea scopului sau obiectivului din spatele unei interogări a utilizatorului pentru a recupera și genera cele mai relevante și utile informații. Această abordare depășește simpla potrivire a cuvintelor cheie și se concentrează pe înțelegerea nevoilor reale și a contextului utilizatorului.

#### Concepte cheie în căutarea cu intenție

1. **Înțelegerea intenției utilizatorului**:
   - Intenția utilizatorului poate fi clasificată în trei tipuri principale: informațională, navigațională și tranzacțională.
     - **Intenție informațională**: utilizatorul caută informații despre un subiect (ex.: „Care sunt cele mai bune muzee din Paris?”).
     - **Intenție navigațională**: utilizatorul dorește să acceseze un site sau o pagină specifică (ex.: „Site oficial Muzeul Luvru”).
     - **Intenție tranzacțională**: utilizatorul are scopul de a efectua o tranzacție, cum ar fi rezervarea unui zbor sau o achiziție (ex.: „Rezervă un zbor spre Paris”).

2. **Conștientizarea contextului**:
   - Analiza contextului interogării ajută la identificarea corectă a intenției utilizatorului. Aceasta include luarea în considerare a interacțiunilor anterioare, preferințelor utilizatorului și detaliilor specifice ale interogării curente.

3. **Prelucrarea limbajului natural (NLP)**:
   - Tehnicile NLP sunt folosite pentru a înțelege și interpreta interogările în limbaj natural primite de la utilizatori. Include atribuții precum recunoașterea entităților, analiza sentimentelor și parsarea interogărilor.

4. **Personalizare**:
   - Personalizarea rezultatelor căutării pe baza istoricului, preferințelor și feedback-ului utilizatorului sporește relevanța informației recuperate.

#### Exemplu practic: Căutarea cu intenție în agentul de turism

Să luăm Travel Agent ca exemplu pentru a vedea cum poate fi implementată căutarea cu intenție.

1. **Colectarea preferințelor utilizatorului**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Înțelegerea intenției utilizatorului**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Conștientizarea contextului**
   ```python
   def analyze_context(query, user_history):
       # Combină interogarea curentă cu istoricul utilizatorului pentru a înțelege contextul
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Căutare și Personalizare a Rezultatelor**

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
       # Logică de căutare exemplu pentru intenție informațională
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Logică de căutare exemplu pentru intenție navigațională
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Logică de căutare exemplu pentru intenție tranzacțională
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Logică de personalizare exemplu
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Returnează primele 10 rezultate personalizate
   ```

5. **Exemplu de Utilizare**

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

## 4. Generarea Codului ca Instrument

Agenții generativi de cod folosesc modele AI pentru a scrie și executa cod, rezolvând probleme complexe și automatizând sarcini.

### Agenți Generativi de Cod

Agenții generativi de cod folosesc modele AI generative pentru a scrie și executa cod. Acești agenți pot rezolva probleme complexe, automatiza sarcini și oferi perspective valoroase prin generarea și rularea codului în diverse limbaje de programare.

#### Aplicații Practice

1. **Generare Automată de Cod**: Generarea de fragmente de cod pentru sarcini specifice, cum ar fi analiza datelor, web scraping sau machine learning.
2. **SQL ca RAG**: Folosirea interogărilor SQL pentru a extrage și manipula date din baze de date.
3. **Rezolvarea Problemelor**: Crearea și execuția codului pentru a rezolva probleme specifice, cum ar fi optimizarea algoritmilor sau analiza datelor.

#### Exemplu: Agent Generativ de Cod pentru Analiza Datelor

Imaginați-vă că proiectați un agent generativ de cod. Iată cum ar putea funcționa:

1. **Sarcină**: Analiza unui set de date pentru a identifica tendințe și tipare.
2. **Pași**:
   - Încărcarea setului de date într-un instrument de analiză a datelor.
   - Generarea de interogări SQL pentru filtrarea și agregarea datelor.
   - Executarea interogărilor și extragerea rezultatelor.
   - Folosirea rezultatelor pentru generarea de vizualizări și perspective.
3. **Resurse Necesare**: Acces la setul de date, instrumente de analiză a datelor și capabilități SQL.
4. **Experiență**: Folosirea rezultatelor analizei anterioare pentru a îmbunătăți acuratețea și relevanța analizelor viitoare.

### Exemplu: Agent Generativ de Cod pentru Agent de Călătorii

În acest exemplu, vom proiecta un agent generativ de cod, Agentul de Călătorii, pentru a ajuta utilizatorii să-și planifice călătoriile prin generarea și executarea de cod. Acest agent poate gestiona sarcini precum obținerea opțiunilor de călătorie, filtrarea rezultatelor și compilarea unui itinerar folosind AI generativ.

#### Prezentare Generală a Agentului Generativ de Cod

1. **Colectarea Preferințelor Utilizatorului**: Colectează inputul utilizatorului, cum ar fi destinația, datele călătoriei, bugetul și interesele.
2. **Generarea Codului pentru Obținerea Datelor**: Generează fragmente de cod pentru extragerea datelor despre zboruri, hoteluri și atracții.
3. **Executarea Codului Generat**: Rulează codul generat pentru a obține informații în timp real.
4. **Generarea Itinerarului**: Compilează datele obținute într-un plan de călătorie personalizat.
5. **Ajustarea pe Baza Feedback-ului**: Primește feedback de la utilizator și regenerează codul, dacă este necesar, pentru a rafina rezultatele.

#### Implementare Pas cu Pas

1. **Colectarea Preferințelor Utilizatorului**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generarea Codului pentru Obținerea Datelor**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Exemplu: Generează cod pentru a căuta zboruri pe baza preferințelor utilizatorului
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Exemplu: Generează cod pentru a căuta hoteluri
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Executarea Codului Generat**

   ```python
   def execute_code(code):
       # Execută codul generat folosind exec
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

4. **Generarea Itinerarului**

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

5. **Ajustarea pe Baza Feedback-ului**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Ajustați preferințele în funcție de feedback-ul utilizatorului
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerați și executați codul cu preferințele actualizate
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Valorificarea conștientizării mediului și a raționamentului

Pe baza schemei tabelului se poate îmbunătăți într-adevăr procesul de generare a interogărilor prin valorificarea conștientizării mediului și a raționamentului.

Iată un exemplu despre cum se poate face acest lucru:

1. **Înțelegerea Schemei**: Sistemul va înțelege schema tabelului și va folosi aceste informații pentru a fundamenta generarea interogărilor.
2. **Ajustarea pe Baza Feedback-ului**: Sistemul va ajusta preferințele utilizatorului pe baza feedback-ului și va raționa care câmpuri din schema trebuie actualizate.
3. **Generarea și Executarea Interogărilor**: Sistemul va genera și executa interogările pentru a obține date actualizate despre zboruri și hoteluri pe baza noilor preferințe.

Iată un exemplu actualizat de cod Python care încorporează aceste concepte:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Ajustați preferințele pe baza feedback-ului utilizatorului
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Raționament bazat pe schema pentru a ajusta alte preferințe conexe
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Logică personalizată pentru a ajusta preferințele bazate pe schema și feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generați cod pentru a prelua datele zborului pe baza preferințelor actualizate
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generați cod pentru a prelua datele hotelului pe baza preferințelor actualizate
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulați execuția codului și returnați date fictive
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generați itinerariul pe baza zborurilor, hotelurilor și atracțiilor
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Exemplu de schemă
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Exemplu de utilizare
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerați și executați codul cu preferințele actualizate
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Explicație - Rezervare pe Baza Feedback-ului

1. **Conștientizarea Schemei**: Dicționarul `schema` definește modul în care preferințele trebuie ajustate pe baza feedback-ului. Include câmpuri precum `favorites` și `avoid`, cu ajustările corespunzătoare.
2. **Ajustarea Preferințelor (metoda `adjust_based_on_feedback`)**: Această metodă ajustează preferințele în funcție de feedback-ul utilizatorului și schema.
3. **Ajustări Bazate pe Mediu (metoda `adjust_based_on_environment`)**: Această metodă personalizează ajustările pe baza schemei și feedback-ului.
4. **Generarea și Executarea Interogărilor**: Sistemul generează cod pentru a obține date actualizate despre zboruri și hoteluri pe baza preferințelor ajustate și simulează executarea acestor interogări.
5. **Generarea Itinerarului**: Sistemul creează un itinerar actualizat pe baza noilor date despre zbor, hotel și atracții.

Prin făcând sistemul conștient de mediu și raționând pe baza schemei, acesta poate genera interogări mai precise și relevante, conducând la recomandări mai bune pentru călătorii și o experiență a utilizatorului mai personalizată.

### Utilizarea SQL ca Tehnică de Generare Augmentată prin Recuperare (RAG)

SQL (Structured Query Language) este un instrument puternic pentru interacțiunea cu bazele de date. Când este folosit ca parte a abordării de Generare Augmentată prin Recuperare (RAG), SQL poate extrage date relevante din baze de date pentru a informa și genera răspunsuri sau acțiuni în agenții AI. Să explorăm cum poate fi folosit SQL ca tehnică RAG în contextul Agentului de Călătorii.

#### Concepte Cheie

1. **Interacțiunea cu Baza de Date**:
   - SQL este folosit pentru a interoga baze de date, a extrage informații relevante și a manipula date.
   - Exemplu: Obținerea detaliilor despre zboruri, informații despre hoteluri și atracții dintr-o bază de date de călătorii.

2. **Integrarea cu RAG**:
   - Interogările SQL sunt generate pe baza inputului și preferințelor utilizatorului.
   - Datele extrase sunt apoi folosite pentru a genera recomandări sau acțiuni personalizate.

3. **Generarea Dinamică a Interogărilor**:
   - Agentul AI generează interogări SQL dinamice pe baza contextului și nevoilor utilizatorului.
   - Exemplu: Personalizarea interogărilor SQL pentru a filtra rezultatele în funcție de buget, date și interese.

#### Aplicații

- **Generare Automată de Cod**: Generarea de fragmente de cod pentru sarcini specifice.
- **SQL ca RAG**: Folosirea interogărilor SQL pentru manipularea datelor.
- **Rezolvarea Problemelor**: Crearea și execuția codului pentru rezolvare.

**Exemplu**: Un agent de analiză a datelor:

1. **Sarcină**: Analiza unui set de date pentru a găsi tendințe.
2. **Pași**:
   - Încărcarea setului de date.
   - Generarea interogărilor SQL pentru filtrarea datelor.
   - Executarea interogărilor și extragerea rezultatelor.
   - Generarea de vizualizări și perspective.
3. **Resurse**: Acces la setul de date, capabilități SQL.
4. **Experiență**: Folosirea rezultatelor anterioare pentru a îmbunătăți analizele viitoare.

#### Exemplu Practic: Folosirea SQL în Agentul de Călătorii

1. **Colectarea Preferințelor Utilizatorului**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generarea Interogărilor SQL**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Executarea Interogărilor SQL**

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

4. **Generarea Recomandărilor**

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

#### Exemple de Interogări SQL

1. **Interogare Zbor**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Interogare Hotel**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Interogare Atracții**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Prin valorificarea SQL ca parte a tehnicii Generării Augmentate prin Recuperare (RAG), agenții AI precum Agentul de Călătorii pot extrage și utiliza dinamic date relevante pentru a oferi recomandări precise și personalizate.

### Exemplu de Metacogniție

Pentru a demonstra o implementare a metacogniției, să creăm un agent simplu care *reflectă asupra procesului său decizional* în timp ce rezolvă o problemă. Pentru acest exemplu, vom construi un sistem în care un agent încearcă să optimizeze alegerea unui hotel, dar apoi evaluează propriul raționament și își ajustează strategia când face erori sau alegeri suboptime.

Vom simula acest lucru folosind un exemplu de bază în care agentul selectează hoteluri pe baza unei combinații între preț și calitate, dar "reflectă" asupra deciziilor sale și ajustează în consecință.

#### Cum ilustrează acest lucru metacogniția:

1. **Decizia Inițială**: Agentul va alege cel mai ieftin hotel, fără a înțelege impactul calității.
2. **Reflecție și Evaluare**: După alegerea inițială, agentul va verifica dacă hotelul este o alegere „rea” folosind feedback-ul utilizatorului. Dacă descoperă că calitatea hotelului a fost prea scăzută, reflectă asupra raționamentului său.
3. **Ajustarea Strategiei**: Agentul își ajustează strategia pe baza reflecției, trecând de la „cel mai ieftin” la „cea mai bună calitate”, îmbunătățindu-și astfel procesul decizional în iterațiile viitoare.

Iată un exemplu:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stochează hotelurile alese anterior
        self.corrected_choices = []  # Stochează alegerile corectate
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Strategii disponibile

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
        # Să presupunem că avem un feedback de la utilizator care ne spune dacă ultima alegere a fost bună sau nu
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Ajustează strategia dacă alegerea anterioară a fost nesatisfăcătoare
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

# Simulează o listă de hoteluri (preț și calitate)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Creează un agent
agent = HotelRecommendationAgent()

# Pasul 1: Agentul recomandă un hotel folosind strategia „cel mai ieftin”
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Pasul 2: Agentul reflectă asupra alegerii și ajustează strategia dacă este necesar
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Pasul 3: Agentul recomandă din nou, de data aceasta folosind strategia ajustată
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Abilități de Metacogniție ale Agenților

Esential aici este capacitatea agentului de a:
- Evalua alegerile și procesul său decizional anterior.
- Ajusta strategia pe baza acelei reflecții, adică metacogniție în acțiune.

Aceasta este o formă simplă de metacogniție în care sistemul este capabil să-și ajusteze procesul de raționament pe baza feedback-ului intern.

### Concluzie

Metacogniția este un instrument puternic care poate îmbunătăți semnificativ capacitățile agenților AI. Prin încorporarea proceselor metacognitive, puteți proiecta agenți mai inteligenți, adaptabili și eficienți. Folosiți resursele suplimentare pentru a explora mai profund fascinanta lume a metacogniției în agenții AI.

### Aveți Mai Multe Întrebări despre Modelul de Proiectare Metacogniție?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la ore de consultanță și a primi răspunsuri la întrebările despre Agenții AI.

## Lecția Anterioară

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Lecția Următoare

[AI Agents in Production](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->