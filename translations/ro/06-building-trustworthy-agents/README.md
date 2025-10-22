<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T20:52:29+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "ro"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.ro.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Construirea Agenților AI de Încredere

## Introducere

Această lecție va acoperi:

- Cum să construiți și să implementați agenți AI siguri și eficienți.
- Considerații importante de securitate în dezvoltarea agenților AI.
- Cum să mențineți confidențialitatea datelor și a utilizatorilor în dezvoltarea agenților AI.

## Obiective de Învățare

După finalizarea acestei lecții, veți ști cum să:

- Identificați și să reduceți riscurile în crearea agenților AI.
- Implementați măsuri de securitate pentru a vă asigura că datele și accesul sunt gestionate corespunzător.
- Creați agenți AI care mențin confidențialitatea datelor și oferă o experiență de utilizare de calitate.

## Siguranță

Să începem prin a analiza cum să construim aplicații agentice sigure. Siguranța înseamnă că agentul AI funcționează conform designului. Ca dezvoltatori de aplicații agentice, avem metode și instrumente pentru a maximiza siguranța:

### Construirea unui Cadru pentru Mesaje de Sistem

Dacă ați construit vreodată o aplicație AI folosind modele mari de limbaj (LLMs), știți cât de important este să proiectați un mesaj de sistem robust. Aceste mesaje stabilesc regulile, instrucțiunile și liniile directoare pentru modul în care LLM va interacționa cu utilizatorul și datele.

Pentru agenții AI, mesajul de sistem este și mai important, deoarece aceștia vor avea nevoie de instrucțiuni foarte specifice pentru a îndeplini sarcinile pentru care au fost proiectați.

Pentru a crea mesaje de sistem scalabile, putem folosi un cadru pentru mesaje de sistem în construirea unuia sau mai multor agenți în aplicația noastră:

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.ro.png)

#### Pasul 1: Creați un Mesaj Meta de Sistem

Mesajul meta va fi utilizat de un LLM pentru a genera mesajele de sistem pentru agenții pe care îi creăm. Îl proiectăm ca pe un șablon, astfel încât să putem crea eficient mai mulți agenți, dacă este necesar.

Iată un exemplu de mesaj meta de sistem pe care l-am oferi LLM-ului:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Pasul 2: Creați un mesaj de bază

Următorul pas este să creați un mesaj de bază pentru a descrie agentul AI. Ar trebui să includeți rolul agentului, sarcinile pe care le va îndeplini și orice alte responsabilități ale acestuia.

Iată un exemplu:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Pasul 3: Furnizați Mesajul de Sistem de Bază către LLM

Acum putem optimiza acest mesaj de sistem oferind mesajul meta de sistem ca mesaj de sistem și mesajul nostru de bază.

Acest lucru va produce un mesaj de sistem mai bine proiectat pentru a ghida agenții noștri AI:

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

#### Pasul 4: Iterați și Îmbunătățiți

Valoarea acestui cadru pentru mesaje de sistem constă în capacitatea de a scala crearea mesajelor de sistem pentru mai mulți agenți, precum și în îmbunătățirea mesajelor de sistem în timp. Este rar ca un mesaj de sistem să funcționeze perfect din prima pentru toate cazurile de utilizare. Posibilitatea de a face ajustări și îmbunătățiri mici prin modificarea mesajului de bază și rularea acestuia prin sistem vă va permite să comparați și să evaluați rezultatele.

## Înțelegerea Amenințărilor

Pentru a construi agenți AI de încredere, este important să înțelegeți și să reduceți riscurile și amenințările la adresa agentului AI. Să analizăm câteva dintre diferitele amenințări la adresa agenților AI și cum puteți planifica și pregăti mai bine pentru acestea.

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.ro.png)

### Sarcini și Instrucțiuni

**Descriere:** Atacatorii încearcă să modifice instrucțiunile sau obiectivele agentului AI prin manipularea comenzilor sau a intrărilor.

**Mitigare**: Efectuați verificări de validare și filtre de intrare pentru a detecta comenzile potențial periculoase înainte ca acestea să fie procesate de agentul AI. Deoarece aceste atacuri necesită de obicei interacțiuni frecvente cu agentul, limitarea numărului de schimburi într-o conversație este o altă metodă de prevenire a acestor tipuri de atacuri.

### Acces la Sisteme Critice

**Descriere**: Dacă un agent AI are acces la sisteme și servicii care stochează date sensibile, atacatorii pot compromite comunicarea dintre agent și aceste servicii. Acestea pot fi atacuri directe sau încercări indirecte de a obține informații despre aceste sisteme prin intermediul agentului.

**Mitigare**: Agenții AI ar trebui să aibă acces la sisteme doar pe baza necesității pentru a preveni aceste tipuri de atacuri. Comunicarea dintre agent și sistem ar trebui să fie, de asemenea, securizată. Implementarea autentificării și controlului accesului este o altă metodă de protejare a acestor informații.

### Suprasolicitarea Resurselor și Serviciilor

**Descriere:** Agenții AI pot accesa diferite instrumente și servicii pentru a îndeplini sarcini. Atacatorii pot folosi această abilitate pentru a ataca aceste servicii prin trimiterea unui volum mare de cereri prin intermediul agentului AI, ceea ce poate duce la eșecuri ale sistemului sau costuri ridicate.

**Mitigare:** Implementați politici pentru a limita numărul de cereri pe care un agent AI le poate face către un serviciu. Limitarea numărului de schimburi de conversație și cereri către agentul AI este o altă metodă de prevenire a acestor tipuri de atacuri.

### Otrăvirea Bazei de Cunoștințe

**Descriere:** Acest tip de atac nu vizează direct agentul AI, ci baza de cunoștințe și alte servicii pe care agentul AI le va utiliza. Acest lucru ar putea implica coruperea datelor sau informațiilor pe care agentul AI le va folosi pentru a îndeplini o sarcină, ceea ce duce la răspunsuri părtinitoare sau neintenționate către utilizator.

**Mitigare:** Efectuați verificări regulate ale datelor pe care agentul AI le va folosi în fluxurile sale de lucru. Asigurați-vă că accesul la aceste date este securizat și modificat doar de persoane de încredere pentru a evita acest tip de atac.

### Erori în Cascadă

**Descriere:** Agenții AI accesează diverse instrumente și servicii pentru a îndeplini sarcini. Erorile cauzate de atacatori pot duce la eșecuri ale altor sisteme la care agentul AI este conectat, ceea ce face ca atacul să devină mai răspândit și mai greu de rezolvat.

**Mitigare**: O metodă de a evita acest lucru este ca agentul AI să opereze într-un mediu limitat, cum ar fi efectuarea sarcinilor într-un container Docker, pentru a preveni atacurile directe asupra sistemului. Crearea de mecanisme de rezervă și logică de reîncercare atunci când anumite sisteme răspund cu o eroare este o altă metodă de a preveni eșecurile majore ale sistemului.

## Omul în Buclă

O altă metodă eficientă de a construi sisteme de agenți AI de încredere este utilizarea unui om în buclă. Acest lucru creează un flux în care utilizatorii pot oferi feedback agenților în timpul rulării. Utilizatorii acționează practic ca agenți într-un sistem multi-agent, oferind aprobare sau oprirea procesului în desfășurare.

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.ro.png)

Iată un fragment de cod folosind AutoGen pentru a arăta cum este implementat acest concept:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Concluzie

Construirea agenților AI de încredere necesită un design atent, măsuri de securitate robuste și o iterație continuă. Prin implementarea unor sisteme structurate de meta-prompting, înțelegerea amenințărilor potențiale și aplicarea strategiilor de atenuare, dezvoltatorii pot crea agenți AI care sunt atât siguri, cât și eficienți. În plus, integrarea unei abordări cu om în buclă asigură că agenții AI rămân aliniați nevoilor utilizatorilor, reducând în același timp riscurile. Pe măsură ce AI continuă să evolueze, menținerea unei atitudini proactive în ceea ce privește securitatea, confidențialitatea și considerațiile etice va fi esențială pentru a cultiva încrederea și fiabilitatea în sistemele bazate pe AI.

### Aveți mai multe întrebări despre construirea agenților AI de încredere?

Alăturați-vă [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la ore de consultanță și a obține răspunsuri la întrebările despre agenții AI.

## Resurse Suplimentare

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Prezentare generală a utilizării responsabile a AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluarea modelelor generative AI și a aplicațiilor AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mesaje de sistem pentru siguranță</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Șablon de evaluare a riscurilor</a>

## Lecția Anterioară

[Agentic RAG](../05-agentic-rag/README.md)

## Lecția Următoare

[Planning Design Pattern](../07-planning-design/README.md)

---

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru a asigura acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.