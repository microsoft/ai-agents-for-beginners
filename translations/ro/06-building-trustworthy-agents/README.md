[![Agenți AI de Încredere](../../../translated_images/ro/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Apăsați pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Construirea Agenților AI de Încredere

## Introducere

Această lecție va acoperi:

- Cum să construiești și să implementezi agenți AI siguri și eficienți
- Considerații importante de securitate în dezvoltarea agenților AI.
- Cum să menții confidențialitatea datelor și a utilizatorilor în dezvoltarea agenților AI.

## Obiectivele Învățării

După finalizarea acestei lecții, veți ști cum să:

- Identificați și să atenuați riscurile în crearea agenților AI.
- Implementați măsuri de securitate pentru a asigura gestionarea corectă a datelor și accesului.
- Creați agenți AI care mențin confidențialitatea datelor și oferă o experiență de utilizator de calitate.

## Siguranță

Să începem prin a vedea cum să construim aplicații agentice sigure. Siguranța înseamnă că agentul AI funcționează conform proiectului. Ca dezvoltatori de aplicații agentice, avem metode și unelte pentru a maximiza siguranța:

### Construirea unui Cadru de Mesaje de Sistem

Dacă ați construit vreodată o aplicație AI folosind Modele Mari de Limbaj (LLM-uri), știți importanța proiectării unui prompt robust de sistem sau a unui mesaj de sistem. Aceste prompturi stabilesc regulile meta, instrucțiunile și ghidurile pentru modul în care LLM-ul va interacționa cu utilizatorul și datele.

Pentru agenții AI, promptul de sistem este și mai important deoarece agenții AI vor avea nevoie de instrucțiuni foarte specifice pentru a îndeplini sarcinile pe care le-am proiectat pentru ei.

Pentru a crea prompturi de sistem scalabile, putem folosi un cadru de mesaje de sistem pentru a construi unul sau mai mulți agenți în aplicația noastră:

![Construirea unui Cadru de Mesaje de Sistem](../../../translated_images/ro/system-message-framework.3a97368c92d11d68.webp)

#### Pasul 1: Creați un Mesaj Meta de Sistem 

Meta-promptul va fi folosit de un LLM pentru a genera prompturile de sistem pentru agenții pe care îi creăm. Îl proiectăm ca un șablon astfel încât să putem crea eficient mai mulți agenți dacă este nevoie.

Iată un exemplu de mesaj meta de sistem pe care l-am da LLM-ului:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Pasul 2: Creați un prompt de bază

Următorul pas este să creați un prompt de bază pentru a descrie Agentul AI. Ar trebui să includeți rolul agentului, sarcinile pe care agentul le va îndeplini și orice alte responsabilități ale agentului.

Iată un exemplu:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Pasul 3: Furnizați Mesajul de Sistem de Bază către LLM

Acum putem optimiza acest mesaj de sistem oferind mesajul meta de sistem ca mesaj de sistem împreună cu mesajul nostru de sistem de bază.

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

Valoarea acestui cadru de mesaje de sistem este capacitatea de a scala crearea mesajelor de sistem pentru mai mulți agenți mai ușor, precum și îmbunătățirea mesajelor de sistem în timp. Este rar să ai un mesaj de sistem care să funcționeze perfect de la prima încercare pentru cazul tău complet de utilizare. Posibilitatea de a face mici ajustări și îmbunătățiri schimbând mesajul de bază și rulându-l prin sistem îți va permite să compari și să evaluezi rezultatele.

## Înțelegerea Amenințărilor

Pentru a construi agenți AI de încredere, este important să înțelegi și să atenuezi riscurile și amenințările la care este expus agentul tău AI. Să analizăm doar câteva dintre diferitele amenințări la adresa agenților AI și cum te poți planifica și pregăti mai bine pentru ele.

![Înțelegerea Amenințărilor](../../../translated_images/ro/understanding-threats.89edeada8a97fc0f.webp)

### Sarcină și Instrucțiune

**Descriere:** Atacanții încearcă să schimbe instrucțiunile sau obiectivele agentului AI prin prompting sau manipularea inputurilor.

**Atenuare**: Executați verificări de validare și filtre de intrare pentru a detecta prompturi potențial periculoase înainte ca acestea să fie procesate de Agentul AI. Deoarece aceste atacuri necesită, de obicei, o interacțiune frecventă cu Agentul, limitarea numărului de schimburi într-o conversație este o altă modalitate de a preveni astfel de atacuri.

### Acces la Sisteme Critice

**Descriere**: Dacă un agent AI are acces la sisteme și servicii care stochează date sensibile, atacatorii pot compromite comunicarea dintre agent și aceste servicii. Acestea pot fi atacuri directe sau încercări indirecte de a obține informații despre aceste sisteme prin intermediul agentului.

**Atenuare**: Agenții AI ar trebui să aibă acces la sisteme doar pe bază de necesitate pentru a preveni astfel de atacuri. Comunicarea dintre agent și sistem trebuie, de asemenea, să fie securizată. Implementarea autentificării și controlului accesului este o altă modalitate de a proteja aceste informații.

### Suprasolicitarea Resurselor și Serviciilor

**Descriere:** Agenții AI pot accesa diferite unelte și servicii pentru a îndeplini sarcini. Atacanții pot folosi această abilitate pentru a ataca aceste servicii prin trimiterea unui volum mare de cereri prin intermediul Agentului AI, ceea ce poate duce la defectarea sistemelor sau la costuri ridicate.

**Atenuare:** Implementați politici pentru a limita numărul de cereri pe care un agent AI le poate face către un serviciu. Limitarea numărului de schimburi și cereri către agentul AI este o altă metodă de prevenire a acestor atacuri.

### Înrâurirea Bazei de Cunoștințe

**Descriere:** Acest tip de atac nu vizează direct agentul AI, ci baza de cunoștințe și alte servicii pe care agentul AI le utilizează. Aceasta poate implica coruperea datelor sau informațiilor pe care agentul AI le folosește pentru a îndeplini o sarcină, conducând la răspunsuri părtinitoare sau neintenționate către utilizator.

**Atenuare:** Efectuați verificări regulate ale datelor pe care agentul AI le folosește în fluxurile de lucru. Asigurați-vă că accesul la aceste date este securizat și că modificările sunt făcute doar de persoane de încredere pentru a evita acest tip de atac.

### Erori în Cascadă

**Descriere:** Agenții AI accesează diverse unelte și servicii pentru a finaliza sarcini. Erorile cauzate de atacatori pot duce la defectarea altor sisteme la care agentul AI este conectat, determinând ca atacul să devină mai extins și mai greu de diagnosticat.

**Atenuare**: O metodă de a evita acest lucru este să aveți agentul AI să funcționeze într-un mediu limitat, cum ar fi efectuarea sarcinilor într-un container Docker, pentru a preveni atacurile directe asupra sistemului. Crearea unor mecanisme de rezervă și logica de reîncercare când anumite sisteme răspund cu o eroare este o altă metodă pentru a preveni defectarea sistemului pe scară largă.

## Omul în Buclă

O altă modalitate eficientă de a construi sisteme de agenți AI de încredere este utilizarea Omului în Buclă. Aceasta creează un flux în care utilizatorii pot oferi feedback agenților în timpul execuției. Utilizatorii acționează practic ca agenți într-un sistem multi-agent, oferind aprobarea sau oprirea procesului în desfășurare.

![Omul în Buclă](../../../translated_images/ro/human-in-the-loop.5f0068a678f62f4f.webp)

Iată un fragment de cod care folosește Microsoft Agent Framework pentru a arăta cum este implementat acest concept:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Creează furnizorul cu aprobarea umană în proces
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Creează agentul cu un pas de aprobare umană
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

Construirea agenților AI de încredere necesită o proiectare atentă, măsuri robuste de securitate și iterare continuă. Prin implementarea sistemelor structurate de meta prompting, înțelegerea amenințărilor potențiale și aplicarea strategiilor de atenuare, dezvoltatorii pot crea agenți AI care sunt atât siguri, cât și eficienți. Mai mult, încorporarea unei abordări cu omul în buclă asigură că agenții AI rămân aliniați nevoilor utilizatorilor, reducând în același timp riscurile. Pe măsură ce AI continuă să evolueze, menținerea unei atitudini proactive în ceea ce privește securitatea, confidențialitatea și considerentele etice va fi cheia pentru a cultiva încrederea și fiabilitatea în sistemele conduse de AI.

## Exemple de Cod

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Demonstrație pas cu pas a cadrului de mesaje de sistem cu meta prompt.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Porți de aprobare pre-acțiune, ierarhizarea riscurilor și înregistrarea auditului pentru agenți de încredere.

### Mai Aveți Întrebări despre Construirea Agenților AI de Încredere?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la orele de consultanță și a primi răspunsuri la întrebările despre Agenții AI.

## Resurse Suplimentare

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Prezentare generală a AI responsabil</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluarea modelelor AI generative și a aplicațiilor AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mesaje de siguranță pentru sistem</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Șablon pentru evaluarea riscurilor</a>

## Lecția Anterioară

[Agentic RAG](../05-agentic-rag/README.md)

## Lecția Următoare

[Pattern-ul de Proiectare pentru Planificare](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->