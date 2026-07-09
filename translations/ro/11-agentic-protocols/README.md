# Utilizarea Protocoalelor Agentice (MCP, A2A și NLWeb)

[![Protocoale Agentice](../../../translated_images/ro/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Faceți click pe imaginea de mai sus pentru a viziona videoclipul lecției)_

Pe măsură ce utilizarea agenților AI crește, crește și necesitatea unor protocoale care să asigure standardizare, securitate și să sprijine inovația deschisă. În această lecție, vom aborda 3 protocoale care caută să satisfacă această nevoie - Protocolul Contextului Modelului (MCP), Agent la Agent (A2A) și Web-ul în Limbaj Natural (NLWeb).

## Introducere

În această lecție vom acoperi:

• Cum **MCP** permite agenților AI să acceseze instrumente și date externe pentru a finaliza sarcini ale utilizatorului.

• Cum **A2A** facilitează comunicarea și colaborarea între diferiți agenți AI.

• Cum **NLWeb** aduce interfețe în limbaj natural către orice site web, permițând agenților AI să descopere și să interacționeze cu conținutul.

## Obiective de Învățare

• **Identificarea** scopului principal și a beneficiilor MCP, A2A și NLWeb în contextul agenților AI.

• **Explicarea** modului în care fiecare protocol facilitează comunicarea și interacțiunea între LLM-uri, instrumente și alți agenți.

• **Recunoașterea** rolurilor distincte pe care le joacă fiecare protocol în construirea sistemelor agentice complexe.

## Protocolul Contextului Modelului

**Protocolul Contextului Modelului (MCP)** este un standard deschis care oferă o modalitate standardizată pentru aplicații de a furniza context și instrumente LLM-urilor. Acest lucru permite un „adaptor universal” la diferite surse de date și instrumente la care agenții AI se pot conecta într-un mod consecvent.

Să analizăm componentele MCP, beneficiile față de utilizarea directă a API-urilor și un exemplu de cum agenții AI ar putea folosi un server MCP.

### Componente Core MCP

MCP funcționează pe o **arhitectură client-server** iar componentele de bază sunt:

• **Gazdele (Hosts)** sunt aplicații LLM (de exemplu, un editor de cod precum VSCode) care inițiază conexiunile către un server MCP.

• **Clienții (Clients)** sunt componente din cadrul aplicației gazdă care mențin conexiuni unu-la-unu cu serverele.

• **Serverele (Servers)** sunt programe ușoare care expun capabilități specifice.

Incluse în protocol sunt trei primitive esențiale care sunt capabilitățile unui server MCP:

• **Instrumente (Tools)**: Acestea sunt acțiuni sau funcții discrete pe care agentul AI le poate apela pentru a realiza o acțiune. De exemplu, un serviciu meteo ar putea expune o unealtă "get weather", sau un server de comerț electronic ar putea expune o unealtă "purchase product". Serverele MCP afișează numele, descrierea și schema de intrare/ieșire a fiecărei unelte în lista lor de capabilități.

• **Resurse (Resources)**: Sunt elemente de date sau documente doar în citire pe care un server MCP le poate furniza, iar clienții le pot prelua la cerere. Exemple includ conținutul fișierelor, înregistrări din baze de date sau fișiere de log. Resursele pot fi text (de exemplu, cod sau JSON) sau binare (imagini sau PDF-uri).

• **Indicații (Prompts)**: Sunt șabloane predefinite care oferă sugestii de indicații, permițând fluxuri de lucru mai complexe.

### Beneficiile MCP

MCP oferă avantaje semnificative pentru agenții AI:

• **Descoperirea Dinamică a Uneltelor**: Agenții pot primi dinamic o listă de unelte disponibile de la un server împreună cu descrierile a ceea ce fac acestea. Acest lucru contrastează cu API-urile tradiționale, care deseori necesită codificare statică pentru integrări, însemnând că orice schimbare a API necesită actualizări ale codului. MCP oferă o abordare „integrează o singură dată”, ceea ce conduce la o adaptabilitate mai mare.

• **Interoperabilitate între LLM-uri**: MCP funcționează peste diferite LLM-uri, oferind flexibilitatea de a schimba modelele de bază pentru a evalua performanța mai bună.

• **Securitate Standardizată**: MCP include o metodă standard de autentificare, îmbunătățind scalabilitatea când se adaugă acces la servere MCP suplimentare. Aceasta este mai simplă decât gestionarea diferitelor chei și tipuri de autentificare pentru diverse API-uri tradiționale.

### Exemplu MCP

![Diagramă MCP](../../../translated_images/ro/mcp-diagram.e4ca1cbd551444a1.webp)

Să ne imaginăm că un utilizator dorește să rezerve un zbor folosind un asistent AI alimentat de MCP.

1. **Conexiune**: Asistentul AI (clientul MCP) se conectează la un server MCP furnizat de o companie aeriană.

2. **Descoperirea uneltelor**: Clientul întreabă serverul MCP al companiei aeriene, „Ce unelte aveți disponibile?” Serverul răspunde cu unelte precum „căutare zboruri” și „rezervare zboruri”.

3. **Invocarea uneltei**: Apoi îi ceri asistentului AI „Te rog, caută un zbor de la Portland la Honolulu.” Asistentul AI, folosind LLM-ul său, identifică că trebuie să apeleze unealta „căutare zboruri” și transmite parametrii relevanți (origine, destinație) serverului MCP.

4. **Executare și Răspuns**: Serverul MCP, acționând ca un înveliș, face apelul efectiv la API-ul intern de rezervări al companiei aeriene. Apoi primește informațiile despre zbor (de ex., date JSON) și le trimite înapoi către asistentul AI.

5. **Interacțiune ulterioară**: Asistentul AI prezintă opțiunile de zbor. Odată ce selectezi un zbor, asistentul poate invoca unealta „rezervare zbor” pe același server MCP, finalizând rezervarea.

## Protocolul Agent-la-Agent (A2A)

În timp ce MCP se concentrează pe conectarea LLM-urilor cu instrumente, **protocolul Agent-la-Agent (A2A)** face un pas mai departe permițând comunicarea și colaborarea între diferiți agenți AI. A2A conectează agenți AI din organizații, medii și stive tehnologice diferite pentru a finaliza o sarcină comună.

Vom examina componentele și beneficiile A2A, împreună cu un exemplu de aplicare într-o aplicație de călătorii.

### Componente Core A2A

A2A se concentrează pe facilitarea comunicării între agenți și pe cooperarea lor pentru a îndeplini o sub-sarcină a utilizatorului. Fiecare componentă a protocolului contribuie la acest lucru:

#### Agent Card

Similar modului în care un server MCP partajează o listă de unelte, un Agent Card conține:
- Numele Agentului.
- O **descriere a sarcinilor generale** pe care le realizează.
- O **listă de abilități specifice** cu descrieri pentru a ajuta alți agenți (sau chiar utilizatori umani) să înțeleagă când și de ce ar dori să apeleze acel agent.
- **URL-ul Endpoint curent** al agentului.
- **Versiunea** și **capabilitățile** agentului cum ar fi răspunsurile în flux și notificările push.

#### Agent Executor

Agent Executor este responsabil pentru **transmiterea contextului conversației utilizatorului către agentul de la distanță**, agentul la distanță are nevoie de acesta pentru a înțelege sarcina ce trebuie îndeplinită. Într-un server A2A, un agent folosește propriul său Model Mare de Limbaj (LLM) pentru a interpreta cererile primite și a executa sarcini folosind propriile sale instrumente interne.

#### Artifact

După ce un agent la distanță a finalizat sarcina solicitată, produsul muncii sale este creat ca un artifact. Un artifact **conține rezultatul muncii agentului**, o **descriere a ceea ce a fost realizat** și **contextul text transmis prin protocol**. După trimiterea artifactului, conexiunea cu agentul de la distanță se închide până când este din nou necesară.

#### Event Queue

Această componentă este utilizată pentru **gestionarea actualizărilor și transmiterea mesajelor**. Este deosebit de importantă în producție pentru sistemele agentice pentru a preveni închiderea conexiunii între agenți înainte ca o sarcină să fie finalizată, mai ales când timpii de finalizare a sarcinilor pot fi mai îndelungați.

### Beneficiile A2A

• **Colaborare îmbunătățită**: Permite agenților de la furnizori și platforme diferite să interacționeze, să partajeze context și să lucreze împreună, facilitând o automatizare fără întreruperi între sisteme tradițional deconectate.

• **Flexibilitate la Selectarea Modelului**: Fiecare agent A2A poate decide ce LLM folosește pentru a servi cererile, permițând modele optimizate sau ajustate pentru fiecare agent, spre deosebire de o conexiune unică LLM în unele scenarii MCP.

• **Autentificare Integrată**: Autentificarea este integrată direct în protocolul A2A, oferind un cadru solid de securitate pentru interacțiunile agenților.

### Exemplu A2A

![Diagramă A2A](../../../translated_images/ro/A2A-Diagram.8666928d648acc26.webp)

Să extindem exemplul nostru de rezervare călătorii, de data aceasta utilizând A2A.

1. **Cerere utilizator către Multi-Agent**: Un utilizator interacționează cu un client/agent A2A „Agent de Călătorii”, poate spunând „Te rog să rezervi o călătorie completă la Honolulu pentru săptămâna viitoare, incluzând zboruri, hotel și mașină de închiriat”.

2. **Orchestrare de către Agentul de Călătorii**: Agentul de Călătorii primește această cerere complexă. Folosește LLM-ul său pentru a raționa despre sarcină și a determina că trebuie să interacționeze cu alți agenți specializați.

3. **Comunicare între Agenți**: Agentul de Călătorii folosește apoi protocolul A2A pentru a se conecta la agenții din aval, cum ar fi „Agentul Companiei Aeriene,” „Agentul Hotelului” și „Agentul Închirierii Mașinilor” creați de companii diferite.

4. **Executarea Sarcinilor Delegată**: Agentul de Călătorii trimite sarcini specifice acestor agenți specializați (de exemplu, „Găsește zboruri spre Honolulu,” „Rezervă un hotel,” „Închiriază o mașină”). Fiecare agent specializat, rulând propriile LLM-uri și utilizând propriile unelte (care pot fi însele servere MCP), își realizează partea specifică din rezervare.

5. **Răspuns Consolidat**: Odată ce toți agenții din aval termină sarcinile, Agentul de Călătorii compilează rezultatele (detalii zbor, confirmare hotel, rezervare mașină) și trimite un răspuns complet, stil conversațional, înapoi utilizatorului.

## Web-ul în Limbaj Natural (NLWeb)

Site-urile web au fost de mult principalul mod prin care utilizatorii accesează informații și date pe internet.

Să analizăm componentele diferite ale NLWeb, beneficiile NLWeb și un exemplu cum funcționează NLWeb privind aplicația noastră de călătorii.

### Componentele NLWeb

- **Aplicația NLWeb (Codul Serviciului de Bază)**: Sistemul care procesează întrebările în limbaj natural. Conectează părțile diferite ale platformei pentru a crea răspunsuri. Poate fi considerat **motorul care alimentează caracteristicile în limbaj natural** ale unui site web.

- **Protocolul NLWeb**: Un **set de reguli de bază pentru interacțiunea în limbaj natural** cu un site web. Trimite răspunsuri în format JSON (adesea folosind Schema.org). Scopul său este să creeze o fundație simplă pentru „Web-ul AI”, în același mod în care HTML a făcut posibilă partajarea documentelor online.

- **Server MCP (Endpoint Protocol Context Model)**: Fiecare configurație NLWeb funcționează și ca un **server MCP**. Aceasta înseamnă că poate **partaja unelte (cum ar fi metoda „ask”) și date** cu alte sisteme AI. Practic, aceasta face conținutul și capabilitățile site-ului web utilizabile de agenții AI, permițând site-ului să devină parte a „ecosistemului de agenți” mai larg.

- **Modelele de Embedding**: Aceste modele sunt folosite pentru a **converti conținutul site-ului web în reprezentări numerice denumite vectori** (embedding-uri). Acești vectori captează semnificația într-un mod pe care computerele îl pot compara și căuta. Sunt stocate într-o bază de date specială, iar utilizatorii pot alege modelul de embedding pe care doresc să îl folosească.

- **Baza de date Vectorială (Mecanismul de Regăsire)**: Această bază de date **stochează embedding-urile conținutului site-ului web**. Când cineva pune o întrebare, NLWeb verifică baza de date vectorială pentru a găsi rapid cele mai relevante informații. Oferă o listă rapidă de posibile răspunsuri, clasificate după similaritate. NLWeb funcționează cu diferite sisteme de stocare vectorială cum ar fi Qdrant, Snowflake, Milvus, Azure AI Search și Elasticsearch.

### NLWeb prin Exemplu

![NLWeb](../../../translated_images/ro/nlweb-diagram.c1e2390b310e5fe4.webp)

Să luăm din nou site-ul nostru de rezervări călătorii, dar de data aceasta alimentat de NLWeb.

1. **Ingestia datelor**: Cataloagele existente ale site-ului de călătorii (de ex., liste de zboruri, descrieri de hoteluri, pachete de turism) sunt formatate folosind Schema.org sau încărcate prin fluxuri RSS. Instrumentele NLWeb preiau aceste date structurate, creează embedding-uri și le stochează într-o bază de date vectorială locală sau la distanță.

2. **Interogarea în limbaj natural (Om)**: Un utilizator vizitează site-ul și, în loc să navigheze prin meniuri, scrie în interfața de chat: „Găsește-mi un hotel potrivit pentru familie în Honolulu cu piscină pentru săptămâna viitoare”.

3. **Procesarea NLWeb**: Aplicația NLWeb primește această interogare. O trimite către un LLM pentru înțelegere și, simultan, caută în baza sa de date vectorială pentru listări relevante de hoteluri.

4. **Rezultate Precise**: LLM-ul ajută la interpretarea rezultatelor căutării din baza de date, identifică cele mai bune potriviri bazate pe criteriile "potrivit pentru familie," "piscină" și "Honolulu," apoi formează un răspuns în limbaj natural. În mod crucial, răspunsul face referire la hoteluri reale din catalogul site-ului, evitând informații inventate.

5. **Interacțiunea Agentului AI**: Deoarece NLWeb funcționează ca un server MCP, un agent AI extern de călătorii ar putea, de asemenea, să se conecteze la această instanță NLWeb a site-ului. Agentul AI ar putea folosi metoda `ask` MCP pentru a interoga direct site-ul: `ask("Există restaurante vegane recomandate de hotel în zona Honolulu?")`. Instanța NLWeb ar procesa aceasta, utilizând baza sa de date cu informații despre restaurante (dacă este încărcată), și ar returna un răspuns JSON structurat.

### Ai mai multe întrebări despre MCP/A2A/NLWeb?

Alătură-te [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la ore de birou și a primi răspunsuri la întrebările tale despre Agenți AI.

## Resurse

- [MCP pentru Începători](https://aka.ms/mcp-for-beginners)  
- [Documentația MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repo NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->