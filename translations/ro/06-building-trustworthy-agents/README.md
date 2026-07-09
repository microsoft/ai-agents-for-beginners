[![Agenți AI De Încredere](../../../translated_images/ro/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Construirea Agenților AI De Încredere

## Introducere

Această lecție va acoperi:

- Cum să construiești și să implementezi Agenți AI siguri și eficienți
- Considerații importante de securitate atunci când dezvolți Agenți AI.
- Cum să menții confidențialitatea datelor și a utilizatorilor în dezvoltarea Agenților AI.

## Obiective de Învățare

După finalizarea acestei lecții, vei ști cum să:

- Identifici și să atenuzi riscurile la crearea Agenților AI.
- Implementezi măsuri de securitate pentru a te asigura că datele și accesul sunt gestionate corespunzător.
- Creezi Agenți AI care mențin confidențialitatea datelor și oferă o experiență de utilizare de calitate.

## Siguranță

Să privim mai întâi construirea aplicațiilor agentice sigure. Siguranța înseamnă că agentul AI funcționează conform proiectului. Ca dezvoltatori de aplicații agentice, avem metode și instrumente pentru a maximiza siguranța:

### Construirea unui Cadru de Mesaje de Sistem

Dacă ai construit vreodată o aplicație AI folosind Modele Mari de Limbaj (LLM-uri), știi importanța de a proiecta un prompt de sistem robust sau un mesaj de sistem. Aceste prompturi stabilesc regulile meta, instrucțiunile și ghidurile pentru modul în care LLM-ul va interacționa cu utilizatorul și cu datele.

Pentru Agenții AI, promptul de sistem este și mai important deoarece Agenții AI vor avea nevoie de instrucțiuni foarte specifice pentru a îndeplini sarcinile pe care le-am proiectat pentru ei.

Pentru a crea prompturi de sistem scalabile, putem folosi un cadru de mesaje de sistem pentru a construi unul sau mai mulți agenți în aplicația noastră:

![Construirea unui Cadru de Mesaje de Sistem](../../../translated_images/ro/system-message-framework.3a97368c92d11d68.webp)

#### Pasul 1: Creează un Mesaj Meta de Sistem 

Meta promptul va fi folosit de un LLM pentru a genera prompturile de sistem pentru agenții pe care îi creăm. Îl proiectăm ca un șablon astfel încât să putem crea eficient mai mulți agenți, dacă este necesar.

Iată un exemplu de mesaj meta de sistem pe care l-am oferi LLM-ului:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Pasul 2: Creează un prompt de bază

Pasul următor este să creezi un prompt de bază pentru a descrie Agentul AI. Ar trebui să incluzi rolul agentului, sarcinile pe care le va îndeplini și orice alte responsabilități ale agentului.

Iată un exemplu:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Pasul 3: Furnizează Mesajul de Sistem de Bază către LLM

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

#### Pasul 4: Iterează și Îmbunătățește

Valoarea acestui cadru de mesaje de sistem este să poți scalabil crea mesaje de sistem de la mai mulți agenți mai ușor, precum și să îmbunătățești mesajele de sistem în timp. Este rar să ai un mesaj de sistem care să funcționeze de prima dată pentru cazul tău complet de utilizare. Capacitatea de a face mici ajustări și îmbunătățiri schimbând mesajul de sistem de bază și rulându-l prin sistem îți va permite să compari și să evaluezi rezultatele.

## Înțelegerea Amenințărilor

Pentru a construi agenți AI de încredere, este important să înțelegi și să atenuzi riscurile și amenințările la adresa agentului tău AI. Să analizăm doar câteva dintre diferitele amenințări pentru agenții AI și cum te poți pregăti și planifica mai bine pentru ele.

![Înțelegerea Amenințărilor](../../../translated_images/ro/understanding-threats.89edeada8a97fc0f.webp)

### Sarcină și Instrucțiune

**Descriere:** Atacatorii încearcă să schimbe instrucțiunile sau obiectivele agentului AI prin prompturi sau manipularea inputurilor.

**Atenuare**: Execută verificări de validare și filtre de input pentru a detecta prompturi potențial periculoase înainte de a fi procesate de Agentul AI. Deoarece aceste atacuri necesită de obicei interacțiuni frecvente cu Agentul, limitarea numărului de runde dintr-o conversație este o altă metodă de a preveni acest tip de atacuri.

### Acces la Sisteme Critice

**Descriere**: Dacă un agent AI are acces la sisteme și servicii care stochează date sensibile, atacatorii pot compromite comunicarea între agent și aceste servicii. Acestea pot fi atacuri directe sau încercări indirecte de a obține informații despre aceste sisteme prin intermediul agentului.

**Atenuare**: Agenții AI ar trebui să aibă acces la sisteme doar pe bază de nevoi pentru a preveni acest tip de atacuri. Comunicarea între agent și sistem ar trebui, de asemenea, să fie sigură. Implementarea autentificării și controlului accesului este o altă modalitate de protejare a acestor informații.

### Suprasolicitarea Resurselor și Serviciilor

**Descriere:** Agenții AI pot accesa diferite instrumente și servicii pentru a îndeplini sarcini. Atacatorii pot folosi această abilitate pentru a ataca aceste servicii trimițând un volum mare de cereri prin Agentul AI, ceea ce poate duce la defecte ale sistemului sau costuri ridicate.

**Atenuare:** Implementați politici pentru a limita numărul de cereri pe care un agent AI le poate face către un serviciu. Limitarea numărului de runde de conversație și a cererilor către agentul tău AI este o altă modalitate de a preveni acest tip de atacuri.

### Înrăutățirea Bazei de Cunoștințe

**Descriere:** Acest tip de atac nu vizează direct agentul AI, ci țintește baza de cunoștințe și alte servicii pe care agentul AI le va folosi. Aceasta poate implica coruperea datelor sau informațiilor pe care agentul AI le va folosi pentru a finaliza o sarcină, conducând la răspunsuri părtinitoare sau neintenționate pentru utilizator.

**Atenuare:** Efectuează verificări regulate ale datelor pe care agentul AI le va folosi în fluxurile sale de lucru. Asigură-te că accesul la aceste date este sigur și că acestea sunt modificate doar de persoane de încredere pentru a evita acest tip de atac.

### Erori în Cascadă

**Descriere:** Agenții AI accesează diverse instrumente și servicii pentru a finaliza sarcini. Erorile cauzate de atacatori pot duce la defectarea altor sisteme la care agentul AI este conectat, făcând ca atacul să devină mai extins și mai greu de depanat.

**Atenuare**: O metodă pentru a evita acest lucru este ca Agentul AI să funcționeze într-un mediu limitat, cum ar fi efectuarea sarcinilor într-un container Docker, pentru a preveni atacurile directe asupra sistemului. Crearea mecanismelor de rezervă și a logicii de reîncercare când anumite sisteme răspund cu o eroare este o altă modalitate de a preveni defecțiuni mai mari ale sistemului.

## Omul în Buclă (Human-in-the-Loop)

O altă metodă eficientă de a construi sisteme de agenți AI de încredere este folosirea unui Om în buclă. Aceasta creează un flux în care utilizatorii pot oferi feedback agenților în timpul rulării. Utilizatorii acționează practic ca agenți într-un sistem multi-agent și oferă aprobarea sau terminarea procesului în curs.

![Om în Buclă](../../../translated_images/ro/human-in-the-loop.5f0068a678f62f4f.webp)

Iată un fragment de cod folosind Microsoft Agent Framework pentru a arăta cum este implementat acest concept:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Creează furnizorul cu aprobare umană în buclă
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

Construirea agenților AI de încredere necesită un design atent, măsuri robuste de securitate și o iterație continuă. Prin implementarea sistemelor structurate de meta-prompturi, înțelegerea amenințărilor potențiale și aplicarea strategiilor de atenuare, dezvoltatorii pot crea agenți AI care sunt atât siguri, cât și eficienți. În plus, incorporarea unei abordări cu omul în buclă asigură că agenții AI rămân aliniați cu nevoile utilizatorilor, minimizând în același timp riscurile. Pe măsură ce AI evoluează, menținerea unei poziții proactive privind securitatea, confidențialitatea și considerentele etice va fi cheia pentru a promova încrederea și fiabilitatea în sistemele alimentate de AI.

## Exemple de Cod

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Demonstrație pas cu pas a cadrului sistemului de meta-prompturi.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Porți de aprobare pre-acțiune, clasificarea riscului și înregistrarea auditului pentru agenți de încredere.

### Ai Mai Multe Întrebări despre Construirea Agenților AI De Încredere?

Alătură-te [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la orele de birou și a primi răspunsuri la întrebările tale despre Agenții AI.

## Resurse Suplimentare

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Prezentare generală a AI responsabil</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluarea modelelor AI generative și aplicațiilor AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mesaje de sistem pentru siguranță</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Model de Evaluare a Riscurilor</a>

## Lecția Anterioară

[Agentic RAG](../05-agentic-rag/README.md)

## Lecția Următoare

[Tiparul de Proiectare a Planificării](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->