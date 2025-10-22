<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T12:54:31+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "it"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.it.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_
# Metacognizione negli Agenti AI

## Introduzione

Benvenuto alla lezione sulla metacognizione negli agenti AI! Questo capitolo è pensato per principianti curiosi di sapere come gli agenti AI possano riflettere sui propri processi di pensiero. Alla fine di questa lezione, comprenderai i concetti chiave e avrai esempi pratici per applicare la metacognizione nella progettazione di agenti AI.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, sarai in grado di:

1. Comprendere le implicazioni dei cicli di ragionamento nelle definizioni degli agenti.
2. Utilizzare tecniche di pianificazione e valutazione per aiutare gli agenti a correggersi autonomamente.
3. Creare agenti capaci di manipolare il codice per svolgere compiti.

## Introduzione alla Metacognizione

La metacognizione si riferisce ai processi cognitivi di ordine superiore che implicano il pensare al proprio pensiero. Per gli agenti AI, questo significa essere in grado di valutare e adattare le proprie azioni basandosi sulla consapevolezza di sé e sulle esperienze passate. La metacognizione, o "pensare al pensiero", è un concetto importante nello sviluppo di sistemi AI agentici. Implica che i sistemi AI siano consapevoli dei propri processi interni e siano in grado di monitorare, regolare e adattare il proprio comportamento di conseguenza. Proprio come facciamo noi quando leggiamo una situazione o affrontiamo un problema. Questa consapevolezza di sé può aiutare i sistemi AI a prendere decisioni migliori, identificare errori e migliorare le proprie prestazioni nel tempo, collegandosi nuovamente al test di Turing e al dibattito sul fatto che l'AI possa prendere il sopravvento.

Nel contesto dei sistemi AI agentici, la metacognizione può aiutare a risolvere diverse sfide, come:
- Trasparenza: Garantire che i sistemi AI possano spiegare il loro ragionamento e le loro decisioni.
- Ragionamento: Migliorare la capacità dei sistemi AI di sintetizzare informazioni e prendere decisioni valide.
- Adattamento: Permettere ai sistemi AI di adattarsi a nuovi ambienti e condizioni mutevoli.
- Percezione: Migliorare l'accuratezza dei sistemi AI nel riconoscere e interpretare i dati provenienti dall'ambiente.

### Cos'è la Metacognizione?

La metacognizione, o "pensare al pensiero", è un processo cognitivo di ordine superiore che implica la consapevolezza di sé e l'autoregolazione dei propri processi cognitivi. Nel campo dell'AI, la metacognizione consente agli agenti di valutare e adattare le proprie strategie e azioni, portando a capacità di risoluzione dei problemi e di decisione migliorate. Comprendendo la metacognizione, puoi progettare agenti AI che siano non solo più intelligenti, ma anche più adattabili ed efficienti. Nella vera metacognizione, l'AI ragionerebbe esplicitamente sul proprio ragionamento.

Esempio: “Ho dato priorità ai voli economici perché... Potrei perdere voli diretti, quindi ricontrollo.”.
Tenere traccia di come o perché ha scelto una certa opzione.
- Notare che ha commesso errori perché si è affidato troppo alle preferenze dell'utente della volta precedente, quindi modifica la sua strategia decisionale, non solo la raccomandazione finale.
- Diagnosticare schemi come: “Ogni volta che l'utente menziona ‘troppo affollato,’ non dovrei solo rimuovere certe attrazioni, ma anche riflettere sul fatto che il mio metodo di selezione delle ‘attrazioni principali’ è difettoso se classifico sempre per popolarità.”

### Importanza della Metacognizione negli Agenti AI

La metacognizione svolge un ruolo cruciale nella progettazione degli agenti AI per diversi motivi:

![Importanza della Metacognizione](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.it.png)

- Auto-riflessione: Gli agenti possono valutare le proprie prestazioni e identificare aree di miglioramento.
- Adattabilità: Gli agenti possono modificare le proprie strategie basandosi su esperienze passate e ambienti mutevoli.
- Correzione degli errori: Gli agenti possono rilevare e correggere errori autonomamente, portando a risultati più accurati.
- Gestione delle risorse: Gli agenti possono ottimizzare l'uso delle risorse, come tempo e potenza computazionale, pianificando e valutando le proprie azioni.

## Componenti di un Agente AI

Prima di approfondire i processi metacognitivi, è essenziale comprendere le componenti di base di un agente AI. Un agente AI è tipicamente composto da:

- Persona: La personalità e le caratteristiche dell'agente, che definiscono come interagisce con gli utenti.
- Strumenti: Le capacità e le funzioni che l'agente può svolgere.
- Competenze: La conoscenza e l'esperienza che l'agente possiede.

Queste componenti lavorano insieme per creare un "unità di competenza" in grado di svolgere compiti specifici.

**Esempio**:
Considera un agente di viaggio, servizi di agenti che non solo pianificano la tua vacanza ma adattano il percorso basandosi su dati in tempo reale e esperienze di viaggio precedenti dei clienti.

### Esempio: Metacognizione in un Servizio di Agente di Viaggio

Immagina di progettare un servizio di agente di viaggio alimentato da AI. Questo agente, "Agente di Viaggio," aiuta gli utenti a pianificare le loro vacanze. Per incorporare la metacognizione, l'Agente di Viaggio deve valutare e adattare le proprie azioni basandosi sulla consapevolezza di sé e sulle esperienze passate. Ecco come la metacognizione potrebbe giocare un ruolo:

#### Compito Attuale

Il compito attuale è aiutare un utente a pianificare un viaggio a Parigi.

#### Passaggi per Completare il Compito

1. **Raccogliere Preferenze dell'Utente**: Chiedere all'utente le date di viaggio, il budget, gli interessi (es. musei, cucina, shopping) e qualsiasi requisito specifico.
2. **Recuperare Informazioni**: Cercare opzioni di volo, alloggi, attrazioni e ristoranti che corrispondano alle preferenze dell'utente.
3. **Generare Raccomandazioni**: Fornire un itinerario personalizzato con dettagli sui voli, prenotazioni alberghiere e attività suggerite.
4. **Adattarsi in Base al Feedback**: Chiedere all'utente un feedback sulle raccomandazioni e apportare le modifiche necessarie.

#### Risorse Necessarie

- Accesso a database di prenotazione voli e hotel.
- Informazioni sulle attrazioni e ristoranti parigini.
- Dati di feedback degli utenti da interazioni precedenti.

#### Esperienza e Auto-riflessione

L'Agente di Viaggio utilizza la metacognizione per valutare le proprie prestazioni e imparare dalle esperienze passate. Ad esempio:

1. **Analisi del Feedback dell'Utente**: L'Agente di Viaggio esamina il feedback degli utenti per determinare quali raccomandazioni sono state ben accolte e quali no. Adatta le sue future proposte di conseguenza.
2. **Adattabilità**: Se un utente ha precedentemente menzionato una preferenza per luoghi poco affollati, l'Agente di Viaggio eviterà di raccomandare attrazioni turistiche popolari durante le ore di punta in futuro.
3. **Correzione degli Errori**: Se l'Agente di Viaggio ha commesso un errore in una prenotazione precedente, come suggerire un hotel già pieno, impara a controllare la disponibilità in modo più rigoroso prima di fare raccomandazioni.

#### Esempio Pratico per Sviluppatori

Ecco un esempio semplificato di come potrebbe apparire il codice dell'Agente di Viaggio quando incorpora la metacognizione:

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

#### Perché la Metacognizione è Importante

- **Auto-riflessione**: Gli agenti possono analizzare le proprie prestazioni e identificare aree di miglioramento.
- **Adattabilità**: Gli agenti possono modificare strategie basandosi su feedback e condizioni mutevoli.
- **Correzione degli Errori**: Gli agenti possono rilevare e correggere errori autonomamente.
- **Gestione delle Risorse**: Gli agenti possono ottimizzare l'uso delle risorse, come tempo e potenza computazionale.

Incorporando la metacognizione, l'Agente di Viaggio può fornire raccomandazioni di viaggio più personalizzate e accurate, migliorando l'esperienza complessiva dell'utente.

---

## 2. Pianificazione negli Agenti

La pianificazione è una componente critica del comportamento degli agenti AI. Implica delineare i passaggi necessari per raggiungere un obiettivo, considerando lo stato attuale, le risorse e gli ostacoli possibili.

### Elementi della Pianificazione

- **Compito Attuale**: Definire chiaramente il compito.
- **Passaggi per Completare il Compito**: Suddividere il compito in passaggi gestibili.
- **Risorse Necessarie**: Identificare le risorse necessarie.
- **Esperienza**: Utilizzare esperienze passate per informare la pianificazione.

**Esempio**:
Ecco i passaggi che l'Agente di Viaggio deve seguire per aiutare un utente a pianificare efficacemente il proprio viaggio:

### Passaggi per l'Agente di Viaggio

1. **Raccogliere Preferenze dell'Utente**
   - Chiedere all'utente dettagli sulle date di viaggio, il budget, gli interessi e qualsiasi requisito specifico.
   - Esempi: "Quando pensi di viaggiare?" "Qual è il tuo range di budget?" "Quali attività ti piacciono in vacanza?"

2. **Recuperare Informazioni**
   - Cercare opzioni di viaggio pertinenti basandosi sulle preferenze dell'utente.
   - **Voli**: Cercare voli disponibili entro il budget e le date di viaggio preferite dall'utente.
   - **Alloggi**: Trovare hotel o proprietà in affitto che corrispondano alle preferenze dell'utente per posizione, prezzo e servizi.
   - **Attrazioni e Ristoranti**: Identificare attrazioni, attività e opzioni di ristorazione popolari che si allineano agli interessi dell'utente.

3. **Generare Raccomandazioni**
   - Compilare le informazioni recuperate in un itinerario personalizzato.
   - Fornire dettagli come opzioni di volo, prenotazioni alberghiere e attività suggerite, assicurandosi di adattare le raccomandazioni alle preferenze dell'utente.

4. **Presentare l'Itinerario all'Utente**
   - Condividere l'itinerario proposto con l'utente per la revisione.
   - Esempio: "Ecco un itinerario suggerito per il tuo viaggio a Parigi. Include dettagli sui voli, prenotazioni alberghiere e un elenco di attività e ristoranti consigliati. Fammi sapere cosa ne pensi!"

5. **Raccogliere Feedback**
   - Chiedere all'utente un feedback sull'itinerario proposto.
   - Esempi: "Ti piacciono le opzioni di volo?" "L'hotel è adatto alle tue esigenze?" "Ci sono attività che vorresti aggiungere o rimuovere?"

6. **Adattarsi in Base al Feedback**
   - Modificare l'itinerario basandosi sul feedback dell'utente.
   - Apportare le modifiche necessarie alle raccomandazioni di volo, alloggio e attività per meglio corrispondere alle preferenze dell'utente.

7. **Conferma Finale**
   - Presentare l'itinerario aggiornato all'utente per la conferma finale.
   - Esempio: "Ho apportato le modifiche basandosi sul tuo feedback. Ecco l'itinerario aggiornato. Ti sembra tutto a posto?"

8. **Prenotare e Confermare le Prenotazioni**
   - Una volta che l'utente approva l'itinerario, procedere con la prenotazione di voli, alloggi e qualsiasi attività pre-pianificata.
   - Inviare i dettagli di conferma all'utente.

9. **Fornire Supporto Continuo**
   - Rimanere disponibile per assistere l'utente con eventuali modifiche o richieste aggiuntive prima e durante il viaggio.
   - Esempio: "Se hai bisogno di ulteriore assistenza durante il viaggio, non esitare a contattarmi in qualsiasi momento!"

### Esempio di Interazione

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

## 3. Sistema RAG Correttivo

Iniziamo comprendendo la differenza tra lo strumento RAG e il caricamento contestuale pre-emptivo.

![RAG vs Context Loading](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.it.png)

### Generazione Augmentata da Recupero (RAG)

RAG combina un sistema di recupero con un modello generativo. Quando viene effettuata una query, il sistema di recupero recupera documenti o dati pertinenti da una fonte esterna, e queste informazioni recuperate vengono utilizzate per arricchire l'input al modello generativo. Questo aiuta il modello a generare risposte più accurate e contestualmente rilevanti.

In un sistema RAG, l'agente recupera informazioni pertinenti da una base di conoscenza e le utilizza per generare risposte o azioni appropriate.

### Approccio RAG Correttivo

L'approccio RAG Correttivo si concentra sull'utilizzo delle tecniche RAG per correggere errori e migliorare l'accuratezza degli agenti AI. Questo implica:

1. **Tecnica di Prompting**: Utilizzare prompt specifici per guidare l'agente nel recupero di informazioni pertinenti.
2. **Strumento**: Implementare algoritmi e meccanismi che consentano all'agente di valutare la rilevanza delle informazioni recuperate e generare risposte accurate.
3. **Valutazione**: Valutare continuamente le prestazioni dell'agente e apportare modifiche per migliorarne l'accuratezza e l'efficienza.

#### Esempio: RAG Correttivo in un Agente di Ricerca

Considera un agente di ricerca che recupera informazioni dal web per rispondere alle query degli utenti. L'approccio RAG Correttivo potrebbe implicare:

1. **Tecnica di Prompting**: Formulare query di ricerca basandosi sull'input dell'utente.
2. **Strumento**: Utilizzare algoritmi di elaborazione del linguaggio naturale e apprendimento automatico per classificare e filtrare i risultati di ricerca.
3. **Valutazione**: Analizzare il feedback degli utenti per identificare e correggere inesattezze nelle informazioni recuperate.

### RAG Correttivo nell'Agente di Viaggio

Il RAG Correttivo (Generazione Augmentata da Recupero) migliora la capacità di un AI di recuperare e generare informazioni correggendo eventuali inesattezze. Vediamo come l'Agente di Viaggio può utilizzare l'approccio RAG Correttivo per fornire raccomandazioni di viaggio più accurate e pertinenti.

Questo implica:

- **Tecnica di Prompting:** Utilizzare prompt specifici per guidare l'agente nel recupero di informazioni pertinenti.
- **Strumento:** Implementare algoritmi e meccanismi che consentano all'agente di valutare la rilevanza delle informazioni recuperate e generare risposte accurate.
- **Valutazione:** Valutare continuamente le prestazioni dell'agente e apportare modifiche per migliorarne l'accuratezza e l'efficienza.

#### Passaggi per Implementare il RAG Correttivo nell'Agente di Viaggio

1. **Interazione Iniziale con l'Utente**
   - L'Agente di Viaggio raccoglie le preferenze iniziali dall'utente, come destinazione, date di viaggio, budget e interessi.
   - Esempio:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Recupero delle Informazioni**
   - L'Agente di Viaggio recupera informazioni su voli, alloggi, attrazioni e ristoranti basandosi sulle preferenze dell'utente.
   - Esempio:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generazione di Raccomandazioni Iniziali**
   - L'Agente di Viaggio utilizza le informazioni recuperate per generare un itinerario personalizzato.
   - Esempio:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Raccolta del Feedback dell'Utente**
   - L'Agente di Viaggio chiede all'utente un feedback sulle raccomandazioni iniziali.
   - Esempio:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Processo RAG Correttivo**
   - **Tecnica di Prompting**: L'Agente di Viaggio formula nuove query di ricerca basandosi sul feedback dell'utente.
     - Esempio:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Strumento**: L'Agente di Viaggio utilizza algoritmi per classificare e filtrare nuovi risultati di ricerca, enfatizzando la rilevanza basandosi sul feedback dell'utente.
     - Esempio:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Valutazione**: L'Agente di Viaggio valuta continuamente la rilevanza e l'accuratezza delle sue raccomandazioni analizzando il feedback dell'utente e apportando le modifiche necessarie.
     - Esempio:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Esempio Pratico

Ecco un esempio semplificato di codice Python che incorpora l'approccio RAG Correttivo nell'Agente di Viaggio:
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

### Caricamento Preventivo del Contesto

Il caricamento preventivo del contesto consiste nel caricare informazioni rilevanti o di background nel modello prima di elaborare una query. Questo significa che il modello ha accesso a queste informazioni fin dall'inizio, il che può aiutarlo a generare risposte più informate senza dover recuperare dati aggiuntivi durante il processo.

Ecco un esempio semplificato di come potrebbe apparire un caricamento preventivo del contesto per un'applicazione di agente di viaggio in Python:

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

#### Spiegazione

1. **Inizializzazione (metodo `__init__`)**: La classe `TravelAgent` pre-carica un dizionario contenente informazioni su destinazioni popolari come Parigi, Tokyo, New York e Sydney. Questo dizionario include dettagli come il paese, la valuta, la lingua e le principali attrazioni di ciascuna destinazione.

2. **Recupero delle Informazioni (metodo `get_destination_info`)**: Quando un utente chiede informazioni su una destinazione specifica, il metodo `get_destination_info` recupera le informazioni rilevanti dal dizionario di contesto pre-caricato.

Caricando preventivamente il contesto, l'applicazione dell'agente di viaggio può rispondere rapidamente alle query degli utenti senza dover recuperare queste informazioni da una fonte esterna in tempo reale. Questo rende l'applicazione più efficiente e reattiva.

### Avvio del Piano con un Obiettivo Prima di Iterare

Avviare un piano con un obiettivo significa iniziare con un chiaro obiettivo o risultato desiderato in mente. Definendo questo obiettivo in anticipo, il modello può usarlo come principio guida durante il processo iterativo. Questo aiuta a garantire che ogni iterazione si avvicini al raggiungimento del risultato desiderato, rendendo il processo più efficiente e mirato.

Ecco un esempio di come si potrebbe avviare un piano di viaggio con un obiettivo prima di iterare per un agente di viaggio in Python:

### Scenario

Un agente di viaggio vuole pianificare una vacanza personalizzata per un cliente. L'obiettivo è creare un itinerario di viaggio che massimizzi la soddisfazione del cliente in base alle sue preferenze e al suo budget.

### Passaggi

1. Definire le preferenze e il budget del cliente.
2. Avviare il piano iniziale basandosi su queste preferenze.
3. Iterare per perfezionare il piano, ottimizzandolo per la soddisfazione del cliente.

#### Codice Python

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

#### Spiegazione del Codice

1. **Inizializzazione (metodo `__init__`)**: La classe `TravelAgent` viene inizializzata con un elenco di destinazioni potenziali, ciascuna con attributi come nome, costo e tipo di attività.

2. **Avvio del Piano (metodo `bootstrap_plan`)**: Questo metodo crea un piano di viaggio iniziale basato sulle preferenze e sul budget del cliente. Itera attraverso l'elenco delle destinazioni e le aggiunge al piano se corrispondono alle preferenze del cliente e rientrano nel budget.

3. **Corrispondenza delle Preferenze (metodo `match_preferences`)**: Questo metodo verifica se una destinazione corrisponde alle preferenze del cliente.

4. **Iterazione del Piano (metodo `iterate_plan`)**: Questo metodo perfeziona il piano iniziale cercando di sostituire ogni destinazione nel piano con una corrispondenza migliore, considerando le preferenze e i vincoli di budget del cliente.

5. **Calcolo del Costo (metodo `calculate_cost`)**: Questo metodo calcola il costo totale del piano attuale, inclusa una potenziale nuova destinazione.

#### Esempio di Utilizzo

- **Piano Iniziale**: L'agente di viaggio crea un piano iniziale basato sulle preferenze del cliente per visite turistiche e un budget di $2000.
- **Piano Perfezionato**: L'agente di viaggio itera il piano, ottimizzandolo per le preferenze e il budget del cliente.

Avviando il piano con un obiettivo chiaro (ad esempio, massimizzare la soddisfazione del cliente) e iterando per perfezionarlo, l'agente di viaggio può creare un itinerario di viaggio personalizzato e ottimizzato per il cliente. Questo approccio garantisce che il piano di viaggio sia allineato alle preferenze e al budget del cliente fin dall'inizio e migliori con ogni iterazione.

### Sfruttare LLM per il Riordino e la Valutazione

I Large Language Models (LLM) possono essere utilizzati per il riordino e la valutazione, valutando la rilevanza e la qualità dei documenti recuperati o delle risposte generate. Ecco come funziona:

**Recupero:** La fase iniziale di recupero ottiene un insieme di documenti o risposte candidati basati sulla query.

**Riordino:** L'LLM valuta questi candidati e li riordina in base alla loro rilevanza e qualità. Questo passaggio garantisce che le informazioni più rilevanti e di alta qualità siano presentate per prime.

**Valutazione:** L'LLM assegna punteggi a ciascun candidato, riflettendo la loro rilevanza e qualità. Questo aiuta a selezionare la migliore risposta o documento per l'utente.

Sfruttando gli LLM per il riordino e la valutazione, il sistema può fornire informazioni più accurate e contestualmente rilevanti, migliorando l'esperienza complessiva dell'utente.

Ecco un esempio di come un agente di viaggio potrebbe utilizzare un Large Language Model (LLM) per riordinare e valutare le destinazioni di viaggio in base alle preferenze dell'utente in Python:

#### Scenario - Viaggio basato sulle Preferenze

Un agente di viaggio vuole raccomandare le migliori destinazioni di viaggio a un cliente in base alle sue preferenze. L'LLM aiuterà a riordinare e valutare le destinazioni per garantire che vengano presentate le opzioni più rilevanti.

#### Passaggi:

1. Raccogliere le preferenze dell'utente.
2. Recuperare un elenco di destinazioni di viaggio potenziali.
3. Utilizzare l'LLM per riordinare e valutare le destinazioni in base alle preferenze dell'utente.

Ecco come aggiornare l'esempio precedente per utilizzare Azure OpenAI Services:

#### Requisiti

1. È necessario avere un abbonamento Azure.
2. Creare una risorsa Azure OpenAI e ottenere la chiave API.

#### Codice Python di Esempio

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

#### Spiegazione del Codice - Preference Booker

1. **Inizializzazione**: La classe `TravelAgent` viene inizializzata con un elenco di destinazioni di viaggio potenziali, ciascuna con attributi come nome e descrizione.

2. **Ottenere Raccomandazioni (metodo `get_recommendations`)**: Questo metodo genera un prompt per il servizio Azure OpenAI basato sulle preferenze dell'utente e invia una richiesta HTTP POST all'API Azure OpenAI per ottenere destinazioni riordinate e valutate.

3. **Generazione del Prompt (metodo `generate_prompt`)**: Questo metodo costruisce un prompt per Azure OpenAI, includendo le preferenze dell'utente e l'elenco delle destinazioni. Il prompt guida il modello a riordinare e valutare le destinazioni in base alle preferenze fornite.

4. **Chiamata API**: La libreria `requests` viene utilizzata per inviare una richiesta HTTP POST all'endpoint API Azure OpenAI. La risposta contiene le destinazioni riordinate e valutate.

5. **Esempio di Utilizzo**: L'agente di viaggio raccoglie le preferenze dell'utente (ad esempio, interesse per visite turistiche e cultura diversificata) e utilizza il servizio Azure OpenAI per ottenere raccomandazioni riordinate e valutate per le destinazioni di viaggio.

Assicurati di sostituire `your_azure_openai_api_key` con la tua chiave API Azure OpenAI effettiva e `https://your-endpoint.com/...` con l'URL dell'endpoint effettivo della tua distribuzione Azure OpenAI.

Sfruttando l'LLM per il riordino e la valutazione, l'agente di viaggio può fornire raccomandazioni di viaggio più personalizzate e rilevanti ai clienti, migliorando la loro esperienza complessiva.

### RAG: Tecnica di Prompting vs Strumento

La Generazione Augmentata dal Recupero (RAG) può essere sia una tecnica di prompting che uno strumento nello sviluppo di agenti AI. Comprendere la distinzione tra i due può aiutarti a sfruttare RAG in modo più efficace nei tuoi progetti.

#### RAG come Tecnica di Prompting

**Cos'è?**

- Come tecnica di prompting, RAG implica la formulazione di query o prompt specifici per guidare il recupero di informazioni rilevanti da un ampio corpus o database. Queste informazioni vengono poi utilizzate per generare risposte o azioni.

**Come funziona:**

1. **Formulare Prompt**: Creare prompt o query ben strutturati basati sul compito da svolgere o sull'input dell'utente.
2. **Recuperare Informazioni**: Utilizzare i prompt per cercare dati rilevanti da una base di conoscenza o dataset preesistente.
3. **Generare Risposta**: Combinare le informazioni recuperate con modelli AI generativi per produrre una risposta completa e coerente.

**Esempio in Agente di Viaggio**:

- Input Utente: "Voglio visitare musei a Parigi."
- Prompt: "Trova i migliori musei a Parigi."
- Informazioni Recuperate: Dettagli su Louvre, Musée d'Orsay, ecc.
- Risposta Generata: "Ecco alcuni dei migliori musei a Parigi: Louvre, Musée d'Orsay e Centre Pompidou."

#### RAG come Strumento

**Cos'è?**

- Come strumento, RAG è un sistema integrato che automatizza il processo di recupero e generazione, rendendo più semplice per gli sviluppatori implementare funzionalità AI complesse senza dover creare manualmente prompt per ogni query.

**Come funziona:**

1. **Integrazione**: Integrare RAG nell'architettura dell'agente AI, permettendogli di gestire automaticamente i compiti di recupero e generazione.
2. **Automazione**: Lo strumento gestisce l'intero processo, dall'input dell'utente alla generazione della risposta finale, senza richiedere prompt espliciti per ogni passaggio.
3. **Efficienza**: Migliora le prestazioni dell'agente semplificando il processo di recupero e generazione, consentendo risposte più rapide e accurate.

**Esempio in Agente di Viaggio**:

- Input Utente: "Voglio visitare musei a Parigi."
- Strumento RAG: Recupera automaticamente informazioni sui musei e genera una risposta.
- Risposta Generata: "Ecco alcuni dei migliori musei a Parigi: Louvre, Musée d'Orsay e Centre Pompidou."

### Confronto

| Aspetto                | Tecnica di Prompting                                      | Strumento                                               |
|------------------------|-----------------------------------------------------------|--------------------------------------------------------|
| **Manuale vs Automatico** | Formulazione manuale di prompt per ogni query.           | Processo automatizzato per recupero e generazione.     |
| **Controllo**          | Offre maggiore controllo sul processo di recupero.         | Semplifica e automatizza il recupero e la generazione. |
| **Flessibilità**       | Consente prompt personalizzati basati su esigenze specifiche.| Più efficiente per implementazioni su larga scala.     |
| **Complessità**        | Richiede la creazione e la modifica di prompt.             | Più facile da integrare nell'architettura di un agente AI.|

### Esempi Pratici

**Esempio di Tecnica di Prompting:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Esempio di Strumento:**

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

### Valutazione della Rilevanza

Valutare la rilevanza è un aspetto cruciale delle prestazioni degli agenti AI. Garantisce che le informazioni recuperate e generate dall'agente siano appropriate, accurate e utili per l'utente. Esploriamo come valutare la rilevanza negli agenti AI, inclusi esempi pratici e tecniche.

#### Concetti Chiave nella Valutazione della Rilevanza

1. **Consapevolezza del Contesto**:
   - L'agente deve comprendere il contesto della query dell'utente per recuperare e generare informazioni rilevanti.
   - Esempio: Se un utente chiede "migliori ristoranti a Parigi", l'agente dovrebbe considerare le preferenze dell'utente, come il tipo di cucina e il budget.

2. **Accuratezza**:
   - Le informazioni fornite dall'agente devono essere corrette e aggiornate.
   - Esempio: Raccomandare ristoranti attualmente aperti con buone recensioni piuttosto che opzioni obsolete o chiuse.

3. **Intento dell'Utente**:
   - L'agente dovrebbe dedurre l'intento dell'utente dietro la query per fornire le informazioni più rilevanti.
   - Esempio: Se un utente chiede "hotel economici", l'agente dovrebbe dare priorità alle opzioni convenienti.

4. **Ciclo di Feedback**:
   - Raccogliere e analizzare continuamente il feedback degli utenti aiuta l'agente a perfezionare il processo di valutazione della rilevanza.
   - Esempio: Incorporare valutazioni e feedback degli utenti sulle raccomandazioni precedenti per migliorare le risposte future.

#### Tecniche Pratiche per Valutare la Rilevanza

1. **Punteggio di Rilevanza**:
   - Assegnare un punteggio di rilevanza a ciascun elemento recuperato in base a quanto bene corrisponde alla query e alle preferenze dell'utente.
   - Esempio:

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

2. **Filtraggio e Classificazione**:
   - Filtrare gli elementi irrilevanti e classificare quelli rimanenti in base ai loro punteggi di rilevanza.
   - Esempio:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Return top 10 relevant items
     ```

3. **Elaborazione del Linguaggio Naturale (NLP)**:
   - Utilizzare tecniche NLP per comprendere la query dell'utente e recuperare informazioni rilevanti.
   - Esempio:

     ```python
     def process_query(query):
         # Use NLP to extract key information from the user's query
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integrazione del Feedback degli Utenti**:
   - Raccogliere il feedback degli utenti sulle raccomandazioni fornite e utilizzarlo per regolare le valutazioni di rilevanza future.
   - Esempio:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Esempio: Valutazione della Rilevanza in Agente di Viaggio

Ecco un esempio pratico di come Travel Agent può valutare la rilevanza delle raccomandazioni di viaggio:

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

### Ricerca con Intento

La ricerca con intento implica comprendere e interpretare lo scopo o l'obiettivo sottostante dietro la query di un utente per recuperare e generare le informazioni più rilevanti e utili. Questo approccio va oltre il semplice abbinamento di parole chiave e si concentra sulla comprensione delle reali esigenze e del contesto dell'utente.

#### Concetti Chiave nella Ricerca con Intento

1. **Comprensione dell'Intento dell'Utente**:
   - L'intento dell'utente può essere categorizzato in tre tipi principali: informativo, navigazionale e transazionale.
     - **Intento Informativo**: L'utente cerca informazioni su un argomento (es. "Quali sono i migliori musei di Parigi?").
     - **Intento Navigazionale**: L'utente vuole navigare verso un sito web o una pagina specifica (es. "Sito ufficiale del Louvre").
     - **Intento Transazionale**: L'utente intende effettuare una transazione, come prenotare un volo o fare un acquisto (es. "Prenota un volo per Parigi").

2. **Consapevolezza del Contesto**:
   - Analizzare il contesto della query dell'utente aiuta a identificare accuratamente il suo intento. Questo include considerare interazioni precedenti, preferenze dell'utente e dettagli specifici della query attuale.

3. **Elaborazione del Linguaggio Naturale (NLP)**:
   - Le tecniche NLP vengono impiegate per comprendere e interpretare le query in linguaggio naturale fornite dagli utenti. Questo include attività come il riconoscimento di entità, l'analisi del sentiment e il parsing delle query.

4. **Personalizzazione**:
   - Personalizzare i risultati della ricerca in base alla cronologia, alle preferenze e al feedback dell'utente migliora la rilevanza delle informazioni recuperate.
#### Esempio pratico: Ricerca con intento in Travel Agent

Prendiamo Travel Agent come esempio per vedere come implementare la ricerca con intento.

1. **Raccolta delle preferenze dell'utente**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Comprensione dell'intento dell'utente**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Consapevolezza del contesto**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Ricerca e personalizzazione dei risultati**

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

5. **Esempio di utilizzo**

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

## 4. Generazione di codice come strumento

Gli agenti che generano codice utilizzano modelli di intelligenza artificiale per scrivere ed eseguire codice, risolvendo problemi complessi e automatizzando attività.

### Agenti che generano codice

Gli agenti che generano codice utilizzano modelli di intelligenza artificiale generativa per scrivere ed eseguire codice. Questi agenti possono risolvere problemi complessi, automatizzare attività e fornire preziosi approfondimenti generando ed eseguendo codice in vari linguaggi di programmazione.

#### Applicazioni pratiche

1. **Generazione automatica di codice**: Generare frammenti di codice per attività specifiche, come analisi dei dati, web scraping o machine learning.
2. **SQL come RAG**: Utilizzare query SQL per recuperare e manipolare dati dai database.
3. **Risoluzione di problemi**: Creare ed eseguire codice per risolvere problemi specifici, come ottimizzare algoritmi o analizzare dati.

#### Esempio: Agente che genera codice per l'analisi dei dati

Immagina di progettare un agente che genera codice. Ecco come potrebbe funzionare:

1. **Compito**: Analizzare un dataset per identificare tendenze e modelli.
2. **Passaggi**:
   - Caricare il dataset in uno strumento di analisi dei dati.
   - Generare query SQL per filtrare e aggregare i dati.
   - Eseguire le query e recuperare i risultati.
   - Utilizzare i risultati per generare visualizzazioni e approfondimenti.
3. **Risorse necessarie**: Accesso al dataset, strumenti di analisi dei dati e capacità SQL.
4. **Esperienza**: Utilizzare i risultati delle analisi precedenti per migliorare l'accuratezza e la rilevanza delle analisi future.

### Esempio: Agente che genera codice per Travel Agent

In questo esempio, progetteremo un agente che genera codice, Travel Agent, per aiutare gli utenti a pianificare i loro viaggi generando ed eseguendo codice. Questo agente può gestire attività come recuperare opzioni di viaggio, filtrare i risultati e compilare un itinerario utilizzando l'intelligenza artificiale generativa.

#### Panoramica dell'agente che genera codice

1. **Raccolta delle preferenze dell'utente**: Raccoglie input dell'utente come destinazione, date di viaggio, budget e interessi.
2. **Generazione di codice per recuperare dati**: Genera frammenti di codice per recuperare dati su voli, hotel e attrazioni.
3. **Esecuzione del codice generato**: Esegue il codice generato per recuperare informazioni in tempo reale.
4. **Generazione dell'itinerario**: Compila i dati recuperati in un piano di viaggio personalizzato.
5. **Regolazione basata sul feedback**: Riceve feedback dall'utente e rigenera il codice, se necessario, per perfezionare i risultati.

#### Implementazione passo-passo

1. **Raccolta delle preferenze dell'utente**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generazione di codice per recuperare dati**

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

3. **Esecuzione del codice generato**

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

4. **Generazione dell'itinerario**

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

5. **Regolazione basata sul feedback**

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

### Sfruttare la consapevolezza ambientale e il ragionamento

Basarsi sullo schema della tabella può effettivamente migliorare il processo di generazione delle query sfruttando la consapevolezza ambientale e il ragionamento.

Ecco un esempio di come questo può essere fatto:

1. **Comprensione dello schema**: Il sistema comprenderà lo schema della tabella e utilizzerà queste informazioni per fondare la generazione delle query.
2. **Regolazione basata sul feedback**: Il sistema regolerà le preferenze dell'utente basandosi sul feedback e ragionerà su quali campi dello schema devono essere aggiornati.
3. **Generazione ed esecuzione delle query**: Il sistema genererà ed eseguirà query per recuperare dati aggiornati su voli e hotel basandosi sulle nuove preferenze.

Ecco un esempio di codice Python aggiornato che incorpora questi concetti:

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

#### Spiegazione - Prenotazione basata sul feedback

1. **Consapevolezza dello schema**: Il dizionario `schema` definisce come le preferenze dovrebbero essere regolate basandosi sul feedback. Include campi come `favorites` e `avoid`, con corrispondenti regolazioni.
2. **Regolazione delle preferenze (metodo `adjust_based_on_feedback`)**: Questo metodo regola le preferenze basandosi sul feedback dell'utente e sullo schema.
3. **Regolazioni basate sull'ambiente (metodo `adjust_based_on_environment`)**: Questo metodo personalizza le regolazioni basandosi sullo schema e sul feedback.
4. **Generazione ed esecuzione delle query**: Il sistema genera codice per recuperare dati aggiornati su voli e hotel basandosi sulle preferenze regolate e simula l'esecuzione di queste query.
5. **Generazione dell'itinerario**: Il sistema crea un itinerario aggiornato basandosi sui nuovi dati su voli, hotel e attrazioni.

Rendendo il sistema consapevole dell'ambiente e ragionando basandosi sullo schema, è possibile generare query più accurate e pertinenti, portando a migliori raccomandazioni di viaggio e a un'esperienza utente più personalizzata.

### Utilizzo di SQL come tecnica di Retrieval-Augmented Generation (RAG)

SQL (Structured Query Language) è uno strumento potente per interagire con i database. Quando utilizzato come parte di un approccio di Retrieval-Augmented Generation (RAG), SQL può recuperare dati pertinenti dai database per informare e generare risposte o azioni negli agenti di intelligenza artificiale. Esploriamo come SQL può essere utilizzato come tecnica RAG nel contesto di Travel Agent.

#### Concetti chiave

1. **Interazione con il database**:
   - SQL viene utilizzato per interrogare i database, recuperare informazioni pertinenti e manipolare i dati.
   - Esempio: Recuperare dettagli sui voli, informazioni sugli hotel e attrazioni da un database di viaggi.

2. **Integrazione con RAG**:
   - Le query SQL vengono generate basandosi sugli input e sulle preferenze dell'utente.
   - I dati recuperati vengono poi utilizzati per generare raccomandazioni o azioni personalizzate.

3. **Generazione dinamica di query**:
   - L'agente di intelligenza artificiale genera query SQL dinamiche basandosi sul contesto e sulle esigenze dell'utente.
   - Esempio: Personalizzare le query SQL per filtrare i risultati basandosi su budget, date e interessi.

#### Applicazioni

- **Generazione automatica di codice**: Generare frammenti di codice per attività specifiche.
- **SQL come RAG**: Utilizzare query SQL per manipolare i dati.
- **Risoluzione di problemi**: Creare ed eseguire codice per risolvere problemi.

**Esempio**:
Un agente di analisi dei dati:

1. **Compito**: Analizzare un dataset per trovare tendenze.
2. **Passaggi**:
   - Caricare il dataset.
   - Generare query SQL per filtrare i dati.
   - Eseguire le query e recuperare i risultati.
   - Generare visualizzazioni e approfondimenti.
3. **Risorse**: Accesso al dataset, capacità SQL.
4. **Esperienza**: Utilizzare i risultati precedenti per migliorare le analisi future.

#### Esempio pratico: Utilizzo di SQL in Travel Agent

1. **Raccolta delle preferenze dell'utente**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generazione di query SQL**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Esecuzione di query SQL**

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

4. **Generazione di raccomandazioni**

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

#### Esempi di query SQL

1. **Query sui voli**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Query sugli hotel**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Query sulle attrazioni**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Sfruttando SQL come parte della tecnica di Retrieval-Augmented Generation (RAG), agenti di intelligenza artificiale come Travel Agent possono recuperare e utilizzare dinamicamente dati pertinenti per fornire raccomandazioni accurate e personalizzate.

### Esempio di metacognizione

Per dimostrare un'implementazione della metacognizione, creiamo un semplice agente che *riflette sul proprio processo decisionale* mentre risolve un problema. In questo esempio, costruiremo un sistema in cui un agente cerca di ottimizzare la scelta di un hotel, ma poi valuta il proprio ragionamento e adatta la propria strategia quando commette errori o fa scelte subottimali.

Simuleremo questo utilizzando un esempio di base in cui l'agente seleziona hotel basandosi su una combinazione di prezzo e qualità, ma "riflette" sulle proprie decisioni e si adatta di conseguenza.

#### Come questo illustra la metacognizione:

1. **Decisione iniziale**: L'agente sceglierà l'hotel più economico, senza considerare l'impatto sulla qualità.
2. **Riflessione e valutazione**: Dopo la scelta iniziale, l'agente verificherà se l'hotel è una scelta "cattiva" utilizzando il feedback dell'utente. Se scopre che la qualità dell'hotel era troppo bassa, riflette sul proprio ragionamento.
3. **Adattamento della strategia**: L'agente adatta la propria strategia basandosi sulla riflessione, passando da "più economico" a "migliore qualità", migliorando così il proprio processo decisionale nelle iterazioni future.

Ecco un esempio:

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

#### Abilità metacognitive degli agenti

Il punto chiave qui è la capacità dell'agente di:
- Valutare le proprie scelte precedenti e il processo decisionale.
- Adattare la propria strategia basandosi su quella riflessione, ovvero la metacognizione in azione.

Questa è una forma semplice di metacognizione in cui il sistema è in grado di adattare il proprio processo di ragionamento basandosi sul feedback interno.

### Conclusione

La metacognizione è uno strumento potente che può migliorare significativamente le capacità degli agenti di intelligenza artificiale. Incorporando processi metacognitivi, è possibile progettare agenti più intelligenti, adattabili ed efficienti. Utilizza le risorse aggiuntive per esplorare ulteriormente il mondo affascinante della metacognizione negli agenti di intelligenza artificiale.

### Hai altre domande sul design pattern della metacognizione?

Unisciti al [Discord di Azure AI Foundry](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare agli orari di ricevimento e ottenere risposte alle tue domande sugli agenti di intelligenza artificiale.

## Lezione precedente

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Prossima lezione

[AI Agents in Production](../10-ai-agents-production/README.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.