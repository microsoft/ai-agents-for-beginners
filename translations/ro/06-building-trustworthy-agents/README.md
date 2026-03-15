[![Agenți AI de încredere](../../../translated_images/ro/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Construirea agenților AI de încredere

## Introducere

Această lecție va acoperi:

- Cum să construiți și să implementați agenți AI siguri și eficienți
- Considerații importante de securitate la dezvoltarea agenților AI.
- Cum să mențineți confidențialitatea datelor și a utilizatorilor la dezvoltarea agenților AI.

## Obiective de învățare

După parcurgerea acestei lecții, veți ști cum să:

- Identificați și atenuați riscurile atunci când creați agenți AI.
- Implementați măsuri de securitate pentru a vă asigura că datele și accesul sunt gestionate corect.
- Creați agenți AI care mențin confidențialitatea datelor și oferă o experiență utilizatorului de calitate.

## Siguranță

Mai întâi să analizăm construirea aplicațiilor agentice sigure. Siguranța înseamnă că agentul AI funcționează conform proiectului. Ca dezvoltatori de aplicații agentice, avem metode și instrumente pentru a maximiza siguranța:

### Construirea unui cadru pentru mesaje de sistem

Dacă ați construit vreodată o aplicație AI folosind Large Language Models (LLMs), știți cât de important este să proiectați un prompt de sistem robust sau un mesaj de sistem. Aceste prompturi stabilesc regulile meta, instrucțiunile și ghidurile pentru modul în care LLM-ul va interacționa cu utilizatorul și cu datele.

Pentru agenții AI, promptul de sistem este și mai important deoarece aceștia vor avea nevoie de instrucțiuni foarte specifice pentru a îndeplini sarcinile pe care le-am proiectat pentru ei.

Pentru a crea prompturi de sistem scalabile, putem folosi un cadru de mesaje de sistem pentru a construi unul sau mai mulți agenți în aplicația noastră:

![Construirea unui cadru pentru mesaje de sistem](../../../translated_images/ro/system-message-framework.3a97368c92d11d68.webp)

#### Pasul 1: Creați un mesaj meta de sistem 

Meta-promptul va fi folosit de un LLM pentru a genera prompturile de sistem pentru agenții pe care îi creăm. Îl proiectăm ca un șablon, astfel încât să putem crea eficient mai mulți agenți, dacă este necesar.

Iată un exemplu de mesaj meta de sistem pe care l-am oferi LLM-ului:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Pasul 2: Creați un prompt de bază

Următorul pas este să creați un prompt de bază pentru a descrie agentul AI. Ar trebui să includeți rolul agentului, sarcinile pe care agentul le va îndeplini și orice alte responsabilități ale acestuia.

Iată un exemplu:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Pasul 3: Furnizați mesajul de sistem de bază către LLM

Acum putem optimiza acest mesaj de sistem oferind mesajul meta de sistem ca mesaj de sistem și mesajul nostru de sistem de bază.

Acest lucru va produce un mesaj de sistem mai bine conceput pentru a ghida agenții noștri AI:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Pasul 4: Iterați și îmbunătățiți

Valoarea acestui cadru de mesaje de sistem constă în capacitatea de a scala crearea de mesaje de sistem pentru mai mulți agenți mai ușor, precum și de a vă îmbunătăți mesajele de sistem în timp. Este rar să aveți un mesaj de sistem care funcționează din prima pentru întregul caz de utilizare. Posibilitatea de a face mici ajustări și îmbunătățiri prin schimbarea mesajului de sistem de bază și rularea acestuia prin sistem vă va permite să comparați și să evaluați rezultatele.

## Înțelegerea amenințărilor

Pentru a construi agenți AI de încredere, este important să înțelegeți și să atenuați riscurile și amenințările la adresa agentului dvs. AI. Să analizăm doar câteva dintre diferitele amenințări la adresa agenților AI și cum vă puteți planifica și pregăti mai bine pentru ele.

![Înțelegerea amenințărilor](../../../translated_images/ro/understanding-threats.89edeada8a97fc0f.webp)

### Sarcină și instrucțiuni

**Descriere:** Atacatorii încearcă să schimbe instrucțiunile sau obiectivele agentului AI prin prompturi sau manipularea intrărilor.

**Atenuare**: Efectuați verificări de validare și filtre de intrare pentru a detecta prompturi potențial periculoase înainte ca acestea să fie procesate de agentul AI. Deoarece aceste atacuri necesită de obicei interacțiuni frecvente cu agentul, limitarea numărului de schimburi dintr-o conversație este un alt mod de a preveni acest tip de atacuri.

### Accesul la sisteme critice

**Descriere**: Dacă un agent AI are acces la sisteme și servicii care stochează date sensibile, atacatorii pot compromite comunicarea dintre agent și aceste servicii. Acestea pot fi atacuri directe sau încercări indirecte de a obține informații despre aceste sisteme prin intermediul agentului.

**Atenuare**: Agenții AI ar trebui să aibă acces la sisteme doar pe bază de necesitate pentru a preveni acest tip de atacuri. Comunicația dintre agent și sistem ar trebui, de asemenea, să fie securizată. Implementarea autentificării și controlului accesului este o altă modalitate de a proteja aceste informații.

### Supraîncărcarea resurselor și serviciilor

**Descriere:** Agenții AI pot accesa diferite instrumente și servicii pentru a îndeplini sarcini. Atacatorii pot folosi această capacitate pentru a ataca aceste servicii prin trimiterea unui volum mare de solicitări prin intermediul agentului AI, ceea ce poate duce la defectarea sistemelor sau la costuri mari.

**Atenuare:** Implementați politici pentru a limita numărul de solicitări pe care un agent AI le poate face către un serviciu. Limitarea numărului de schimburi din conversație și a solicitărilor către agentul dvs. AI este un alt mod de a preveni acest tip de atacuri.

### Otrăvirea bazei de cunoștințe

**Descriere:** Acest tip de atac nu vizează direct agentul AI, ci vizează baza de cunoștințe și alte servicii pe care le va folosi agentul AI. Acesta poate implica coruperea datelor sau informațiilor pe care agentul AI le va folosi pentru a îndeplini o sarcină, conducând la răspunsuri părtinitoare sau neintenționate către utilizator.

**Atenuare:** Efectuați verificări periodice ale datelor pe care agentul AI le va utiliza în fluxurile sale de lucru. Asigurați-vă că accesul la aceste date este securizat și că acestea sunt modificate numai de persoane de încredere pentru a evita acest tip de atac.

### Erori în cascadă

**Descriere:** Agenții AI accesează diverse instrumente și servicii pentru a îndeplini sarcini. Erorile cauzate de atacatori pot duce la defecțiuni ale altor sisteme la care agentul AI este conectat, ceea ce face ca atacul să devină mai extins și mai greu de depistat.

**Atenuare**: O metodă pentru a evita acest lucru este ca agentul AI să opereze într-un mediu limitat, cum ar fi executarea sarcinilor într-un container Docker, pentru a preveni atacurile directe asupra sistemului. Crearea unor mecanisme de rezervă și a unei logici de reîncercare când anumite sisteme răspund cu o eroare este o altă modalitate de a preveni defecțiuni mai ample ale sistemului.

## Omul în buclă

O altă modalitate eficientă de a construi sisteme de agenți AI de încredere este utilizarea omului în buclă. Acest lucru creează un flux în care utilizatorii pot oferi feedback agenților în timpul execuției. Utilizatorii acționează esențial ca agenți într-un sistem multi-agent și, prin acordarea aprobării sau terminarea procesului în curs, influențează execuția.

![Omul în buclă](../../../translated_images/ro/human-in-the-loop.5f0068a678f62f4f.webp)

Iată un fragment de cod care utilizează Microsoft Agent Framework pentru a arăta cum este implementat acest concept:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Creează furnizorul cu aprobare umană în buclă
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Creează agentul cu o etapă de aprobare umană
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Utilizatorul poate revizui și aproba răspunsul
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Concluzie

Construirea agenților AI de încredere necesită un design atent, măsuri de securitate robuste și iterații continue. Prin implementarea unor sisteme structurate de meta-prompturi, înțelegerea amenințărilor potențiale și aplicarea strategiilor de atenuare, dezvoltatorii pot crea agenți AI care sunt atât siguri, cât și eficienți. În plus, încorporarea unei abordări cu omul în buclă asigură că agenții AI rămân aliniați nevoilor utilizatorilor, reducând în același timp riscurile. Pe măsură ce AI continuă să evolueze, menținerea unei atitudini proactive în privința securității, confidențialității și considerațiilor etice va fi esențială pentru a cultiva încrederea și fiabilitatea în sistemele bazate pe AI.

### Aveți mai multe întrebări despre construirea agenților AI de încredere?

Alăturați-vă [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la ore de consultanță și a obține răspunsuri la întrebările dvs. despre agenții AI.

## Resurse suplimentare

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Prezentare generală despre AI responsabil</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluarea modelelor AI generative și a aplicațiilor AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mesaje de sistem pentru siguranță</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Șablon de evaluare a riscurilor</a>

## Lecția anterioară

[Agentic RAG](../05-agentic-rag/README.md)

## Lecția următoare

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să fim cât mai exacți, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă o traducere profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventuale neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->