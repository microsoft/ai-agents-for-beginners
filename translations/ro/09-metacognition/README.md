<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T20:47:35+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "ro"
}
-->
[![Design Multi-Agent](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.ro.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_
# Metacogniția în Agenții AI

## Introducere

Bun venit la lecția despre metacogniția în agenții AI! Acest capitol este conceput pentru începători curioși să afle cum agenții AI pot reflecta asupra propriilor procese de gândire. La finalul acestei lecții, veți înțelege conceptele cheie și veți fi echipați cu exemple practice pentru a aplica metacogniția în designul agenților AI.

## Obiective de învățare

După finalizarea acestei lecții, veți putea:

1. Înțelege implicațiile buclelor de raționament în definițiile agenților.
2. Utiliza tehnici de planificare și evaluare pentru a ajuta agenții să se auto-corecteze.
3. Creați proprii agenți capabili să manipuleze codul pentru a îndeplini sarcini.

## Introducere în Metacogniție

Metacogniția se referă la procesele cognitive de ordin superior care implică gândirea asupra propriei gândiri. Pentru agenții AI, aceasta înseamnă să poată evalua și ajusta acțiunile lor pe baza conștientizării de sine și a experiențelor anterioare. Metacogniția, sau "gândirea despre gândire", este un concept important în dezvoltarea sistemelor AI agentice. Implică faptul că sistemele AI sunt conștiente de propriile procese interne și pot monitoriza, reglementa și adapta comportamentul lor în consecință. Exact cum facem noi când analizăm o situație sau abordăm o problemă. Această conștientizare de sine poate ajuta sistemele AI să ia decizii mai bune, să identifice erori și să își îmbunătățească performanța în timp - din nou, legându-se de testul Turing și de dezbaterea despre dacă AI va prelua controlul.

În contextul sistemelor AI agentice, metacogniția poate ajuta la abordarea mai multor provocări, cum ar fi:
- Transparență: Asigurarea că sistemele AI pot explica raționamentul și deciziile lor.
- Raționament: Îmbunătățirea capacității sistemelor AI de a sintetiza informații și de a lua decizii solide.
- Adaptare: Permite sistemelor AI să se ajusteze la medii noi și condiții în schimbare.
- Percepție: Îmbunătățirea acurateței sistemelor AI în recunoașterea și interpretarea datelor din mediul lor.

### Ce este Metacogniția?

Metacogniția, sau "gândirea despre gândire", este un proces cognitiv de ordin superior care implică conștientizarea de sine și autoreglarea proceselor cognitive proprii. În domeniul AI, metacogniția împuternicește agenții să evalueze și să adapteze strategiile și acțiunile lor, conducând la capacități îmbunătățite de rezolvare a problemelor și luare a deciziilor. Prin înțelegerea metacogniției, puteți proiecta agenți AI care nu sunt doar mai inteligenți, ci și mai adaptabili și eficienți. În adevărata metacogniție, veți vedea AI-ul raționând explicit despre propriul raționament.

Exemplu: „Am prioritizat zborurile mai ieftine pentru că... S-ar putea să ratez zborurile directe, așa că să verific din nou.”
Urmărirea modului sau motivului pentru care a ales o anumită rută.
- Observarea că a făcut greșeli deoarece s-a bazat prea mult pe preferințele utilizatorului de data trecută, astfel încât își modifică strategia de luare a deciziilor, nu doar recomandarea finală.
- Diagnosticarea unor tipare precum: „De fiecare dată când utilizatorul menționează „prea aglomerat”, ar trebui să elimin nu doar anumite atracții, ci și să reflectez că metoda mea de a alege „atracțiile de top” este defectuoasă dacă clasific mereu după popularitate.”

### Importanța Metacogniției în Agenții AI

Metacogniția joacă un rol crucial în designul agenților AI din mai multe motive:

![Importanța Metacogniției](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.ro.png)

- Auto-reflecție: Agenții pot evalua propria performanță și identifica zonele care necesită îmbunătățiri.
- Adaptabilitate: Agenții pot modifica strategiile pe baza experiențelor anterioare și a mediilor în schimbare.
- Corectarea erorilor: Agenții pot detecta și corecta erorile în mod autonom, conducând la rezultate mai precise.
- Gestionarea resurselor: Agenții pot optimiza utilizarea resurselor, cum ar fi timpul și puterea de calcul, prin planificarea și evaluarea acțiunilor lor.

## Componentele unui Agent AI

Înainte de a aprofunda procesele metacognitive, este esențial să înțelegem componentele de bază ale unui agent AI. Un agent AI constă, de obicei, din:

- Personalitate: Personalitatea și caracteristicile agentului, care definesc modul în care interacționează cu utilizatorii.
- Instrumente: Capacitățile și funcțiile pe care agentul le poate îndeplini.
- Abilități: Cunoștințele și expertiza pe care agentul le posedă.

Aceste componente lucrează împreună pentru a crea o "unitate de expertiză" care poate îndeplini sarcini specifice.

**Exemplu**:
Luați în considerare un agent de călătorie, servicii de agent care nu doar planifică vacanța dvs., ci și își ajustează traseul pe baza datelor în timp real și a experiențelor anterioare ale clienților.

### Exemplu: Metacogniția într-un Serviciu de Agent de Călătorie

Imaginați-vă că proiectați un serviciu de agent de călătorie alimentat de AI. Acest agent, "Agent de Călătorie", asistă utilizatorii în planificarea vacanțelor lor. Pentru a încorpora metacogniția, Agentul de Călătorie trebuie să evalueze și să ajusteze acțiunile sale pe baza conștientizării de sine și a experiențelor anterioare. Iată cum metacogniția ar putea juca un rol:

#### Sarcina Curentă

Sarcina curentă este să ajute un utilizator să planifice o excursie la Paris.

#### Pași pentru Finalizarea Sarcinii

1. **Colectarea Preferințelor Utilizatorului**: Întrebați utilizatorul despre datele de călătorie, bugetul, interesele (de exemplu, muzee, gastronomie, cumpărături) și orice cerințe specifice.
2. **Recuperarea Informațiilor**: Căutați opțiuni de zbor, cazare, atracții și restaurante care se potrivesc preferințelor utilizatorului.
3. **Generarea Recomandărilor**: Oferiți un itinerar personalizat cu detalii despre zboruri, rezervări de hoteluri și activități sugerate.
4. **Ajustarea pe Baza Feedback-ului**: Solicitați utilizatorului feedback despre recomandări și faceți ajustările necesare.

#### Resurse Necesare

- Acces la baze de date pentru rezervări de zboruri și hoteluri.
- Informații despre atracțiile și restaurantele pariziene.
- Date de feedback de la interacțiunile anterioare cu utilizatorii.

#### Experiență și Auto-reflecție

Agentul de Călătorie folosește metacogniția pentru a evalua performanța sa și pentru a învăța din experiențele anterioare. De exemplu:

1. **Analiza Feedback-ului Utilizatorului**: Agentul de Călătorie analizează feedback-ul utilizatorului pentru a determina ce recomandări au fost bine primite și care nu. Își ajustează sugestiile viitoare în consecință.
2. **Adaptabilitate**: Dacă un utilizator a menționat anterior o aversiune față de locurile aglomerate, Agentul de Călătorie va evita să recomande locuri turistice populare în orele de vârf în viitor.
3. **Corectarea Erorilor**: Dacă Agentul de Călătorie a făcut o eroare într-o rezervare anterioară, cum ar fi sugerarea unui hotel care era complet rezervat, învață să verifice disponibilitatea mai riguros înainte de a face recomandări.

#### Exemplu Practic pentru Dezvoltatori

Iată un exemplu simplificat de cum ar putea arăta codul Agentului de Călătorie atunci când încorporează metacogniția:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
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
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
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

#### De ce Contează Metacogniția

- **Auto-reflecție**: Agenții pot analiza performanța lor și identifica zonele care necesită îmbunătățiri.
- **Adaptabilitate**: Agenții pot modifica strategiile pe baza feedback-ului și a condițiilor în schimbare.
- **Corectarea Erorilor**: Agenții pot detecta și corecta greșelile în mod autonom.
- **Gestionarea Resurselor**: Agenții pot optimiza utilizarea resurselor, cum ar fi timpul și puterea de calcul.

Prin încorporarea metacogniției, Agentul de Călătorie poate oferi recomandări de călătorie mai personalizate și mai precise, îmbunătățind experiența generală a utilizatorului.

---

## 2. Planificarea în Agenți

Planificarea este o componentă critică a comportamentului agenților AI. Implică conturarea pașilor necesari pentru a atinge un obiectiv, luând în considerare starea actuală, resursele și posibilele obstacole.

### Elemente ale Planificării

- **Sarcina Curentă**: Definiți clar sarcina.
- **Pași pentru Finalizarea Sarcinii**: Împărțiți sarcina în pași gestionabili.
- **Resurse Necesare**: Identificați resursele necesare.
- **Experiență**: Utilizați experiențele anterioare pentru a informa planificarea.

**Exemplu**:
Iată pașii pe care Agentul de Călătorie trebuie să îi urmeze pentru a ajuta un utilizator să își planifice excursia în mod eficient:

### Pași pentru Agentul de Călătorie

1. **Colectarea Preferințelor Utilizatorului**
   - Întrebați utilizatorul despre detalii precum datele de călătorie, bugetul, interesele și orice cerințe specifice.
   - Exemple: „Când intenționați să călătoriți?” „Care este intervalul dvs. de buget?” „Ce activități vă plac în vacanță?”

2. **Recuperarea Informațiilor**
   - Căutați opțiuni de călătorie relevante pe baza preferințelor utilizatorului.
   - **Zboruri**: Căutați zboruri disponibile în bugetul utilizatorului și în datele preferate de călătorie.
   - **Cazare**: Găsiți hoteluri sau proprietăți de închiriat care se potrivesc preferințelor utilizatorului pentru locație, preț și facilități.
   - **Atracții și Restaurante**: Identificați atracții populare, activități și opțiuni de luat masa care se aliniază intereselor utilizatorului.

3. **Generarea Recomandărilor**
   - Compilați informațiile recuperate într-un itinerar personalizat.
   - Oferiți detalii precum opțiuni de zbor, rezervări de hoteluri și activități sugerate, asigurându-vă că recomandările sunt adaptate preferințelor utilizatorului.

4. **Prezentarea Itinerarului Utilizatorului**
   - Împărtășiți itinerarul propus utilizatorului pentru revizuire.
   - Exemplu: „Iată un itinerar sugerat pentru excursia dvs. la Paris. Include detalii despre zboruri, rezervări de hoteluri și o listă de activități și restaurante recomandate. Spuneți-mi ce părere aveți!”

5. **Colectarea Feedback-ului**
   - Solicitați utilizatorului feedback despre itinerarul propus.
   - Exemple: „Vă plac opțiunile de zbor?” „Hotelul este potrivit pentru nevoile dvs.?” „Există activități pe care doriți să le adăugați sau să le eliminați?”

6. **Ajustarea pe Baza Feedback-ului**
   - Modificați itinerarul pe baza feedback-ului utilizatorului.
   - Faceți schimbările necesare la recomandările de zbor, cazare și activități pentru a se potrivi mai bine preferințelor utilizatorului.

7. **Confirmarea Finală**
   - Prezentați itinerarul actualizat utilizatorului pentru confirmarea finală.
   - Exemplu: „Am făcut ajustările pe baza feedback-ului dvs. Iată itinerarul actualizat. Totul arată bine pentru dvs.?”

8. **Rezervarea și Confirmarea**
   - După ce utilizatorul aprobă itinerarul, continuați cu rezervarea zborurilor, cazărilor și a oricăror activități pre-planificate.
   - Trimiteți detaliile de confirmare utilizatorului.

9. **Oferirea Suportului Continuu**
   - Rămâneți disponibil pentru a asista utilizatorul cu orice modificări sau cereri suplimentare înainte și în timpul excursiei.
   - Exemplu: „Dacă aveți nevoie de asistență suplimentară în timpul excursiei, nu ezitați să mă contactați oricând!”

### Interacțiune Exemplu

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

# Example usage within a booing request
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

## 3. Sistem Corectiv RAG

Mai întâi, să începem prin a înțelege diferența dintre Instrumentul RAG și Încărcarea Contextului Preemptiv.

![RAG vs Încărcarea Contextului](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.ro.png)

### Generare Augmentată prin Recuperare (RAG)

RAG combină un sistem de recuperare cu un model generativ. Când se face o interogare, sistemul de recuperare preia documente sau date relevante dintr-o sursă externă, iar aceste informații recuperate sunt utilizate pentru a augmenta intrarea modelului generativ. Acest lucru ajută modelul să genereze răspunsuri mai precise și relevante din punct de vedere contextual.

Într-un sistem RAG, agentul recuperează informații relevante dintr-o bază de cunoștințe și le folosește pentru a genera răspunsuri sau acțiuni adecvate.

### Abordarea Corectivă RAG

Abordarea Corectivă RAG se concentrează pe utilizarea tehnicilor RAG pentru a corecta erorile și a îmbunătăți acuratețea agenților AI. Aceasta implică:

1. **Tehnica de Promptare**: Utilizarea unor prompturi specifice pentru a ghida agentul în recuperarea informațiilor relevante.
2. **Instrument**: Implementarea algoritmilor și mecanismelor care permit agentului să evalueze relevanța informațiilor recuperate și să genereze răspunsuri precise.
3. **Evaluare**: Evaluarea continuă a performanței agentului și efectuarea ajustărilor pentru a îmbunătăți acuratețea și eficiența.

#### Exemplu: RAG Corectiv într-un Agent de Căutare

Luați în considerare un agent de căutare care recuperează informații de pe web pentru a răspunde la interogările utilizatorului. Abordarea Corectivă RAG ar putea implica:

1. **Tehnica de Promptare**: Formularea interogărilor de căutare pe baza intrării utilizatorului.
2. **Instrument**: Utilizarea procesării limbajului natural și a algoritmilor de învățare automată pentru a clasifica și filtra rezultatele căutării.
3. **Evaluare**: Analiza feedback-ului utilizatorului pentru a identifica și corecta inexactitățile informațiilor recuperate.

### RAG Corectiv în Agentul de Călătorie

RAG Corectiv (Generare Augmentată prin Recuperare) îmbunătățește capacitatea AI de a recupera și genera informații, corectând în același timp orice inexactități. Să vedem cum Agentul de Călătorie poate utiliza abordarea RAG Corectiv pentru a oferi recomandări de călătorie mai precise și relevante.

Aceasta implică:

- **Tehnica de Promptare:** Utilizarea unor prompturi specifice pentru a ghida agentul în recuperarea informațiilor relevante.
- **Instrument:** Implementarea algoritmilor și mecanismelor care permit agentului să evalueze relevanța informațiilor recuperate și să genereze răspunsuri precise.
- **Evaluare:** Evaluarea continuă a performanței agentului și efectuarea ajustărilor pentru a îmbunătăți acuratețea și eficiența.

#### Pași pentru Implementarea RAG Corectiv în Agentul de Călătorie
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

# Example usage
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

### Încărcarea Contextului Preemptiv

Încărcarea contextului preemptiv implică încărcarea informațiilor relevante sau a contextului de fundal în model înainte de procesarea unei interogări. Acest lucru înseamnă că modelul are acces la aceste informații de la început, ceea ce îl poate ajuta să genereze răspunsuri mai bine informate fără a fi nevoie să recupereze date suplimentare în timpul procesului.

Iată un exemplu simplificat despre cum ar putea arăta o încărcare preemptivă a contextului pentru o aplicație de agenție de turism în Python:

```python
class TravelAgent:
    def __init__(self):
        # Pre-load popular destinations and their information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Fetch destination information from pre-loaded context
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Example usage
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Explicație

1. **Inițializare (metoda `__init__`)**: Clasa `TravelAgent` încarcă anticipat un dicționar care conține informații despre destinații populare precum Paris, Tokyo, New York și Sydney. Acest dicționar include detalii precum țara, moneda, limba și principalele atracții pentru fiecare destinație.

2. **Recuperarea informațiilor (metoda `get_destination_info`)**: Când un utilizator întreabă despre o destinație specifică, metoda `get_destination_info` extrage informațiile relevante din dicționarul de context preîncărcat.

Prin încărcarea preemptivă a contextului, aplicația agenției de turism poate răspunde rapid la interogările utilizatorilor fără a fi nevoie să recupereze aceste informații dintr-o sursă externă în timp real. Acest lucru face aplicația mai eficientă și mai receptivă.

### Inițierea unui Plan cu un Obiectiv înainte de Iterare

Inițierea unui plan cu un obiectiv implică începerea cu un scop clar sau un rezultat dorit în minte. Prin definirea acestui obiectiv de la început, modelul îl poate folosi ca principiu călăuzitor pe parcursul procesului iterativ. Acest lucru ajută la asigurarea faptului că fiecare iterație se apropie de atingerea rezultatului dorit, făcând procesul mai eficient și mai concentrat.

Iată un exemplu despre cum ai putea iniția un plan de călătorie cu un obiectiv înainte de iterare pentru o agenție de turism în Python:

### Scenariu

O agenție de turism dorește să planifice o vacanță personalizată pentru un client. Obiectivul este de a crea un itinerar de călătorie care să maximizeze satisfacția clientului pe baza preferințelor și bugetului acestuia.

### Pași

1. Definirea preferințelor și bugetului clientului.  
2. Inițierea planului inițial pe baza acestor preferințe.  
3. Iterarea pentru rafinarea planului, optimizând satisfacția clientului.  

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

# Example usage
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

#### Explicația Codului

1. **Inițializare (metoda `__init__`)**: Clasa `TravelAgent` este inițializată cu o listă de destinații potențiale, fiecare având atribute precum nume, cost și tip de activitate.

2. **Inițierea Planului (metoda `bootstrap_plan`)**: Această metodă creează un plan de călătorie inițial pe baza preferințelor și bugetului clientului. Parcurge lista de destinații și le adaugă în plan dacă se potrivesc preferințelor clientului și se încadrează în buget.

3. **Potrivirea Preferințelor (metoda `match_preferences`)**: Această metodă verifică dacă o destinație se potrivește preferințelor clientului.

4. **Iterarea Planului (metoda `iterate_plan`)**: Această metodă rafinează planul inițial încercând să înlocuiască fiecare destinație din plan cu o potrivire mai bună, luând în considerare preferințele și constrângerile bugetare ale clientului.

5. **Calcularea Costului (metoda `calculate_cost`)**: Această metodă calculează costul total al planului curent, inclusiv o destinație potențial nouă.

#### Exemplu de Utilizare

- **Plan Inițial**: Agenția de turism creează un plan inițial pe baza preferințelor clientului pentru vizitarea obiectivelor turistice și un buget de 2000$.  
- **Plan Rafinat**: Agenția de turism iterează planul, optimizându-l pentru preferințele și bugetul clientului.  

Prin inițierea planului cu un obiectiv clar (de exemplu, maximizarea satisfacției clientului) și iterarea pentru rafinarea planului, agenția de turism poate crea un itinerar de călătorie personalizat și optimizat pentru client. Această abordare asigură că planul de călătorie se aliniază cu preferințele și bugetul clientului de la început și se îmbunătățește cu fiecare iterație.

### Utilizarea LLM pentru Re-rangare și Scorare

Modelele de limbaj mari (LLM) pot fi utilizate pentru re-rangare și scorare prin evaluarea relevanței și calității documentelor recuperate sau a răspunsurilor generate. Iată cum funcționează:

**Recuperare:** Pasul inițial de recuperare aduce un set de documente candidate sau răspunsuri pe baza interogării.  

**Re-rangare:** LLM evaluează acești candidați și îi re-ranghează pe baza relevanței și calității lor. Acest pas asigură că cele mai relevante și de calitate informații sunt prezentate primele.  

**Scorare:** LLM atribuie scoruri fiecărui candidat, reflectând relevanța și calitatea lor. Acest lucru ajută la selectarea celui mai bun răspuns sau document pentru utilizator.  

Prin utilizarea LLM pentru re-rangare și scorare, sistemul poate oferi informații mai precise și relevante contextual, îmbunătățind experiența generală a utilizatorului.

Iată un exemplu despre cum o agenție de turism ar putea folosi un model de limbaj mare (LLM) pentru re-rangarea și scorarea destinațiilor de călătorie pe baza preferințelor utilizatorului în Python:

#### Scenariu - Călătorii bazate pe Preferințe

O agenție de turism dorește să recomande cele mai bune destinații de călătorie unui client pe baza preferințelor acestuia. LLM va ajuta la re-rangarea și scorarea destinațiilor pentru a se asigura că cele mai relevante opțiuni sunt prezentate.

#### Pași:

1. Colectarea preferințelor utilizatorului.  
2. Recuperarea unei liste de destinații de călătorie potențiale.  
3. Utilizarea LLM pentru re-rangarea și scorarea destinațiilor pe baza preferințelor utilizatorului.  

Iată cum poți actualiza exemplul anterior pentru a utiliza Azure OpenAI Services:

#### Cerințe

1. Trebuie să ai un abonament Azure.  
2. Creează o resursă Azure OpenAI și obține cheia ta API.  

#### Exemplu Cod Python

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generate a prompt for the Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Define headers and payload for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Call the Azure OpenAI API to get the re-ranked and scored destinations
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extract and return the recommendations
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

# Example usage
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

#### Explicația Codului - Recomandări Personalizate

1. **Inițializare**: Clasa `TravelAgent` este inițializată cu o listă de destinații de călătorie potențiale, fiecare având atribute precum nume și descriere.  

2. **Obținerea Recomandărilor (metoda `get_recommendations`)**: Această metodă generează un prompt pentru serviciul Azure OpenAI pe baza preferințelor utilizatorului și face o cerere HTTP POST către API-ul Azure OpenAI pentru a obține destinații re-rangate și scorate.  

3. **Generarea Promptului (metoda `generate_prompt`)**: Această metodă construiește un prompt pentru Azure OpenAI, incluzând preferințele utilizatorului și lista de destinații. Promptul ghidează modelul să re-rangheze și să scoreze destinațiile pe baza preferințelor furnizate.  

4. **Apel API**: Biblioteca `requests` este utilizată pentru a face o cerere HTTP POST către endpoint-ul API Azure OpenAI. Răspunsul conține destinațiile re-rangate și scorate.  

5. **Exemplu de Utilizare**: Agenția de turism colectează preferințele utilizatorului (de exemplu, interes pentru vizitarea obiectivelor turistice și cultură diversă) și folosește serviciul Azure OpenAI pentru a obține recomandări re-rangate și scorate pentru destinații de călătorie.  

Asigură-te că înlocuiești `your_azure_openai_api_key` cu cheia ta API Azure OpenAI și `https://your-endpoint.com/...` cu URL-ul endpoint-ului real al implementării tale Azure OpenAI.  

Prin utilizarea LLM pentru re-rangare și scorare, agenția de turism poate oferi recomandări de călătorie mai personalizate și relevante clienților, îmbunătățind experiența generală a acestora.  

### RAG: Tehnică de Promptare vs Instrument

Generarea augmentată prin recuperare (RAG) poate fi atât o tehnică de promptare, cât și un instrument în dezvoltarea agenților AI. Înțelegerea distincției dintre cele două te poate ajuta să utilizezi RAG mai eficient în proiectele tale.  

#### RAG ca Tehnică de Promptare

**Ce este?**

- Ca tehnică de promptare, RAG implică formularea unor interogări sau prompturi specifice pentru a ghida recuperarea informațiilor relevante dintr-un corpus sau o bază de date mare. Aceste informații sunt apoi utilizate pentru a genera răspunsuri sau acțiuni.  

**Cum funcționează:**  

1. **Formularea Prompturilor**: Creează prompturi sau interogări bine structurate pe baza sarcinii sau a inputului utilizatorului.  
2. **Recuperarea Informațiilor**: Utilizează prompturile pentru a căuta date relevante dintr-o bază de cunoștințe sau un set de date preexistent.  
3. **Generarea Răspunsului**: Combină informațiile recuperate cu modelele generative AI pentru a produce un răspuns complet și coerent.  

**Exemplu în Agenția de Turism**:  

- Input Utilizator: "Vreau să vizitez muzee în Paris."  
- Prompt: "Găsește cele mai bune muzee din Paris."  
- Informații Recuperate: Detalii despre Muzeul Luvru, Musée d'Orsay etc.  
- Răspuns Generat: "Iată câteva dintre cele mai bune muzee din Paris: Muzeul Luvru, Musée d'Orsay și Centrul Pompidou."  

#### RAG ca Instrument

**Ce este?**

- Ca instrument, RAG este un sistem integrat care automatizează procesul de recuperare și generare, făcând mai ușoară implementarea funcționalităților AI complexe fără a crea manual prompturi pentru fiecare interogare.  

**Cum funcționează:**  

1. **Integrare**: Încorporează RAG în arhitectura agentului AI, permițându-i să gestioneze automat sarcinile de recuperare și generare.  
2. **Automatizare**: Instrumentul gestionează întregul proces, de la primirea inputului utilizatorului până la generarea răspunsului final, fără a necesita prompturi explicite pentru fiecare pas.  
3. **Eficiență**: Îmbunătățește performanța agentului prin simplificarea procesului de recuperare și generare, permițând răspunsuri mai rapide și mai precise.  

**Exemplu în Agenția de Turism**:  

- Input Utilizator: "Vreau să vizitez muzee în Paris."  
- Instrument RAG: Recuperează automat informații despre muzee și generează un răspuns.  
- Răspuns Generat: "Iată câteva dintre cele mai bune muzee din Paris: Muzeul Luvru, Musée d'Orsay și Centrul Pompidou."  

### Comparație

| Aspect                 | Tehnică de Promptare                                        | Instrument                                              |
|------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| **Manual vs Automat**  | Formulare manuală a prompturilor pentru fiecare interogare. | Proces automatizat pentru recuperare și generare.     |
| **Control**            | Oferă mai mult control asupra procesului de recuperare.     | Simplifică și automatizează procesul.                 |
| **Flexibilitate**      | Permite prompturi personalizate pe baza nevoilor specifice. | Mai eficient pentru implementări la scară largă.      |
| **Complexitate**       | Necesită crearea și ajustarea prompturilor.                 | Mai ușor de integrat în arhitectura unui agent AI.    |

### Exemple Practice

**Exemplu Tehnică de Promptare:**  

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```  

**Exemplu Instrument:**  

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

### Evaluarea Relevanței

Evaluarea relevanței este un aspect crucial al performanței agenților AI. Aceasta asigură că informațiile recuperate și generate de agent sunt adecvate, corecte și utile utilizatorului. Să explorăm cum să evaluăm relevanța în cazul agenților AI, inclusiv exemple practice și tehnici.  

#### Concepte Cheie în Evaluarea Relevanței

1. **Conștientizarea Contextului**:  
   - Agentul trebuie să înțeleagă contextul interogării utilizatorului pentru a recupera și genera informații relevante.  
   - Exemplu: Dacă un utilizator întreabă despre "cele mai bune restaurante din Paris," agentul ar trebui să ia în considerare preferințele utilizatorului, cum ar fi tipul de bucătărie și bugetul.  

2. **Acuratețe**:  
   - Informațiile furnizate de agent ar trebui să fie corecte din punct de vedere factual și actualizate.  
   - Exemplu: Recomandarea unor restaurante deschise și cu recenzii bune, în loc de opțiuni închise sau depășite.  

3. **Intenția Utilizatorului**:  
   - Agentul ar trebui să deducă intenția utilizatorului din spatele interogării pentru a oferi cele mai relevante informații.  
   - Exemplu: Dacă un utilizator întreabă despre "hoteluri accesibile," agentul ar trebui să prioritizeze opțiunile ieftine.  

4. **Buclă de Feedback**:  
   - Colectarea și analiza continuă a feedback-ului utilizatorului ajută agentul să își rafineze procesul de evaluare a relevanței.  
   - Exemplu: Integrarea evaluărilor și feedback-ului utilizatorilor despre recomandările anterioare pentru a îmbunătăți răspunsurile viitoare.  

#### Tehnici Practice pentru Evaluarea Relevanței

1. **Scorarea Relevanței**:  
   - Atribuie un scor de relevanță fiecărui element recuperat pe baza cât de bine se potrivește cu interogarea și preferințele utilizatorului.  
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

2. **Filtrare și Clasificare**:  
   - Filtrează elementele irelevante și clasifică cele rămase pe baza scorurilor de relevanță.  
   - Exemplu:  

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Return top 10 relevant items
     ```  

3. **Procesare a Limbajului Natural (NLP)**:  
   - Utilizează tehnici NLP pentru a înțelege interogarea utilizatorului și a recupera informații relevante.  
   - Exemplu:  

     ```python
     def process_query(query):
         # Use NLP to extract key information from the user's query
         processed_query = nlp(query)
         return processed_query
     ```  

4. **Integrarea Feedback-ului Utilizatorului**:  
   - Colectează feedback-ul utilizatorului despre recomandările furnizate și îl folosește pentru a ajusta evaluările viitoare ale relevanței.  
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

#### Exemplu: Evaluarea Relevanței în Agenția de Turism

Iată un exemplu practic despre cum agenția de turism poate evalua relevanța recomandărilor de călătorie:  

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
        return ranked_items[:10]  # Return top 10 relevant items

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

# Example usage
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

### Căutarea cu Intenție

Căutarea cu intenție implică înțelegerea și interpretarea scopului sau obiectivului din spatele interogării utilizatorului pentru a recupera și genera cele mai relevante și utile informații. Această abordare merge dincolo de simpla potrivire a cuvintelor cheie și se concentrează pe înțelegerea nevoilor și contextului real al utilizatorului.  

#### Concepte Cheie în Căutarea cu Intenție

1. **Înțelegerea Intenției Utilizatorului**:  
   - Intenția utilizatorului poate fi clasificată în trei tipuri principale: informațională, de navigare și tranzacțională.  
     - **Intenție Informațională**: Utilizatorul caută informații despre un subiect (ex.: "Care sunt cele mai bune muzee din Paris?").  
     - **Intenție de Navigare**: Utilizatorul dorește să acceseze un site web sau o pagină specifică (ex.: "Site-ul oficial al Muzeului Luvru").  
     - **Intenție Tranzacțională**: Utilizatorul dorește să efectueze o tranzacție, cum ar fi rezervarea unui zbor sau efectuarea unei achiziții
#### Exemplu Practic: Căutare cu Intenție în Travel Agent

Să luăm Travel Agent ca exemplu pentru a vedea cum poate fi implementată căutarea cu intenție.

1. **Colectarea Preferințelor Utilizatorului**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Înțelegerea Intenției Utilizatorului**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Conștientizarea Contextului**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
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
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
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

## 4. Generarea de Cod ca Instrument

Agenții care generează cod folosesc modele AI pentru a scrie și executa cod, rezolvând probleme complexe și automatizând sarcini.

### Agenți care Generează Cod

Agenții care generează cod utilizează modele AI generative pentru a scrie și executa cod. Acești agenți pot rezolva probleme complexe, automatiza sarcini și oferi perspective valoroase prin generarea și rularea codului în diverse limbaje de programare.

#### Aplicații Practice

1. **Generare Automată de Cod**: Generarea de fragmente de cod pentru sarcini specifice, cum ar fi analiza datelor, web scraping sau machine learning.
2. **SQL ca RAG**: Utilizarea interogărilor SQL pentru a extrage și manipula date din baze de date.
3. **Rezolvarea Problemelor**: Crearea și rularea codului pentru a rezolva probleme specifice, cum ar fi optimizarea algoritmilor sau analiza datelor.

#### Exemplu: Agent care Generează Cod pentru Analiza Datelor

Imaginează-ți că proiectezi un agent care generează cod. Iată cum ar putea funcționa:

1. **Sarcină**: Analiza unui set de date pentru a identifica tendințe și modele.
2. **Pași**:
   - Încarcă setul de date într-un instrument de analiză a datelor.
   - Generează interogări SQL pentru a filtra și agrega datele.
   - Rulează interogările și extrage rezultatele.
   - Utilizează rezultatele pentru a genera vizualizări și perspective.
3. **Resurse Necesare**: Acces la setul de date, instrumente de analiză a datelor și capabilități SQL.
4. **Experiență**: Utilizează rezultatele analizelor anterioare pentru a îmbunătăți acuratețea și relevanța analizelor viitoare.

### Exemplu: Agent care Generează Cod pentru Travel Agent

În acest exemplu, vom proiecta un agent care generează cod, Travel Agent, pentru a ajuta utilizatorii să-și planifice călătoriile prin generarea și executarea de cod. Acest agent poate gestiona sarcini precum obținerea opțiunilor de călătorie, filtrarea rezultatelor și crearea unui itinerar folosind AI generativ.

#### Prezentare Generală a Agentului care Generează Cod

1. **Colectarea Preferințelor Utilizatorului**: Colectează informații de la utilizator, cum ar fi destinația, datele călătoriei, bugetul și interesele.
2. **Generarea de Cod pentru Obținerea Datelor**: Generează fragmente de cod pentru a extrage date despre zboruri, hoteluri și atracții.
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

2. **Generarea de Cod pentru Obținerea Datelor**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
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
       # Execute the generated code using exec
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
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Utilizarea Conștientizării Mediului și a Raționamentului

Bazarea pe schema tabelului poate îmbunătăți procesul de generare a interogărilor prin utilizarea conștientizării mediului și a raționamentului.

Iată un exemplu despre cum se poate face acest lucru:

1. **Înțelegerea Schemei**: Sistemul va înțelege schema tabelului și va folosi aceste informații pentru a fundamenta generarea interogărilor.
2. **Ajustarea pe Baza Feedback-ului**: Sistemul va ajusta preferințele utilizatorului pe baza feedback-ului și va raționa despre ce câmpuri din schemă trebuie actualizate.
3. **Generarea și Executarea Interogărilor**: Sistemul va genera și executa interogări pentru a obține date actualizate despre zboruri și hoteluri, pe baza noilor preferințe.

Iată un exemplu actualizat de cod Python care încorporează aceste concepte:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Explicație - Rezervare pe Baza Feedback-ului

1. **Conștientizarea Schemei**: Dicționarul `schema` definește modul în care preferințele ar trebui ajustate pe baza feedback-ului. Include câmpuri precum `favorites` și `avoid`, cu ajustări corespunzătoare.
2. **Ajustarea Preferințelor (metoda `adjust_based_on_feedback`)**: Această metodă ajustează preferințele pe baza feedback-ului utilizatorului și a schemei.
3. **Ajustări Bazate pe Mediu (metoda `adjust_based_on_environment`)**: Această metodă personalizează ajustările pe baza schemei și a feedback-ului.
4. **Generarea și Executarea Interogărilor**: Sistemul generează cod pentru a obține date actualizate despre zboruri și hoteluri, pe baza preferințelor ajustate, și simulează executarea acestor interogări.
5. **Generarea Itinerarului**: Sistemul creează un itinerar actualizat pe baza noilor date despre zboruri, hoteluri și atracții.

Prin crearea unui sistem conștient de mediu și care raționează pe baza schemei, acesta poate genera interogări mai precise și relevante, conducând la recomandări de călătorie mai bune și o experiență mai personalizată pentru utilizator.

### Utilizarea SQL ca Tehnică de Generare-Augmentată prin Recuperare (RAG)

SQL (Structured Query Language) este un instrument puternic pentru interacțiunea cu bazele de date. Când este utilizat ca parte a unei abordări de Generare-Augmentată prin Recuperare (RAG), SQL poate extrage date relevante din baze de date pentru a informa și genera răspunsuri sau acțiuni în agenții AI. Să explorăm cum poate fi utilizat SQL ca tehnică RAG în contextul Travel Agent.

#### Concepte Cheie

1. **Interacțiunea cu Baza de Date**:
   - SQL este utilizat pentru a interoga baze de date, a extrage informații relevante și a manipula date.
   - Exemplu: Obținerea detaliilor despre zboruri, informații despre hoteluri și atracții dintr-o bază de date de călătorii.

2. **Integrarea cu RAG**:
   - Interogările SQL sunt generate pe baza intrărilor și preferințelor utilizatorului.
   - Datele extrase sunt apoi utilizate pentru a genera recomandări sau acțiuni personalizate.

3. **Generarea Dinamică a Interogărilor**:
   - Agentul AI generează interogări SQL dinamice pe baza contextului și nevoilor utilizatorului.
   - Exemplu: Personalizarea interogărilor SQL pentru a filtra rezultatele pe baza bugetului, datelor și intereselor.

#### Aplicații

- **Generare Automată de Cod**: Generarea de fragmente de cod pentru sarcini specifice.
- **SQL ca RAG**: Utilizarea interogărilor SQL pentru a manipula date.
- **Rezolvarea Problemelor**: Crearea și rularea codului pentru a rezolva probleme.

**Exemplu**:
Un agent de analiză a datelor:

1. **Sarcină**: Analiza unui set de date pentru a găsi tendințe.
2. **Pași**:
   - Încarcă setul de date.
   - Generează interogări SQL pentru a filtra datele.
   - Rulează interogările și extrage rezultatele.
   - Generează vizualizări și perspective.
3. **Resurse**: Acces la setul de date, capabilități SQL.
4. **Experiență**: Utilizează rezultatele anterioare pentru a îmbunătăți analizele viitoare.

#### Exemplu Practic: Utilizarea SQL în Travel Agent

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

1. **Interogare pentru Zboruri**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Interogare pentru Hoteluri**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Interogare pentru Atracții**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Prin utilizarea SQL ca parte a tehnicii de Generare-Augmentată prin Recuperare (RAG), agenții AI precum Travel Agent pot extrage și utiliza dinamic date relevante pentru a oferi recomandări precise și personalizate.

### Exemplu de Metacogniție

Pentru a demonstra o implementare a metacogniției, să creăm un agent simplu care *reflectează asupra procesului său decizional* în timp ce rezolvă o problemă. În acest exemplu, vom construi un sistem în care un agent încearcă să optimizeze alegerea unui hotel, dar apoi își evaluează propriul raționament și își ajustează strategia atunci când face greșeli sau alegeri suboptime.

Vom simula acest lucru folosind un exemplu de bază în care agentul selectează hoteluri pe baza unei combinații de preț și calitate, dar va "reflecta" asupra deciziilor sale și se va ajusta în consecință.

#### Cum ilustrează acest lucru metacogniția:

1. **Decizia Inițială**: Agentul va alege cel mai ieftin hotel, fără a înțelege impactul asupra calității.
2. **Reflecție și Evaluare**: După alegerea inițială, agentul va verifica dacă hotelul este o alegere "proastă" folosind feedback-ul utilizatorului. Dacă descoperă că calitatea hotelului a fost prea scăzută, reflectează asupra raționamentului său.
3. **Ajustarea Strategiei**: Agentul își ajustează strategia pe baza reflecției, trecând de la "cel mai ieftin" la "cea mai bună calitate", îmbunătățindu-și astfel procesul decizional în iterațiile viitoare.

Iată un exemplu:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stores the hotels chosen previously
        self.corrected_choices = []  # Stores the corrected choices
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Available strategies

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
        # Let's assume we have some user feedback that tells us whether the last choice was good or not
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Adjust strategy if the previous choice was unsatisfactory
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

# Simulate a list of hotels (price and quality)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Create an agent
agent = HotelRecommendationAgent()

# Step 1: The agent recommends a hotel using the "cheapest" strategy
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Step 2: The agent reflects on the choice and adjusts strategy if necessary
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Step 3: The agent recommends again, this time using the adjusted strategy
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Abilitățile de Metacogniție ale Agenților

Elementul cheie aici este abilitatea agentului de a:
- Evalua alegerile și procesul decizional anterior.
- Ajusta strategia pe baza reflecției, adică metacogniția în acțiune.

Aceasta este o formă simplă de metacogniție, în care sistemul este capabil să-și ajusteze procesul de raționament pe baza feedback-ului intern.

### Concluzie

Metacogniția este un instrument puternic care poate îmbunătăți semnificativ capacitățile agenților AI. Prin încorporarea proceselor metacognitive, poți proiecta agenți mai inteligenți, adaptabili și eficienți. Folosește resursele suplimentare pentru a explora mai departe lumea fascinantă a metacogniției în agenții AI.

### Ai Mai Multe Întrebări despre Modelul de Proiectare Metacogniție?

Alătură-te [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la ore de consultanță și a primi răspunsuri la întrebările tale despre agenții AI.

## Lecția Anterioară

[Modelul de Proiectare Multi-Agent](../08-multi-agent/README.md)

## Lecția Următoare

[Agenți AI în Producție](../10-ai-agents-production/README.md)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.