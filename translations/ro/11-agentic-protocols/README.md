# Utilizarea protocoalelor agentice (MCP, A2A și NLWeb)

[![Agentic Protocols](../../../translated_images/ro/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

Pe măsură ce utilizarea agenților AI crește, crește și necesitatea unor protocoale care să asigure standardizare, securitate și să susțină inovația deschisă. În această lecție, vom aborda 3 protocoale care caută să răspundă acestei nevoi - Model Context Protocol (MCP), Agent to Agent (A2A) și Natural Language Web (NLWeb).

## Introducere

În această lecție, vom acoperi:

• Cum **MCP** permite agenților AI să acceseze instrumente și date externe pentru a îndeplini sarcinile utilizatorilor.

• Cum **A2A** facilitează comunicarea și colaborarea între diferiți agenți AI.

• Cum **NLWeb** aduce interfețe în limbaj natural pe orice site web, permițând agenților AI să descopere și să interacționeze cu conținutul.

## Obiectivele de învățare

• **Identificarea** scopului principal și beneficiile MCP, A2A și NLWeb în contextul agenților AI.

• **Explicarea** modului în care fiecare protocol facilitează comunicarea și interacțiunea între LLM-uri, instrumente și alți agenți.

• **Recunoașterea** rolurilor distincte pe care fiecare protocol le joacă în construirea sistemelor agentice complexe.

## Model Context Protocol

**Model Context Protocol (MCP)** este un standard deschis care oferă o modalitate standardizată pentru aplicații de a furniza context și instrumente către LLM-uri. Aceasta permite un "adaptor universal" către diferite surse de date și instrumente la care agenții AI se pot conecta într-un mod consistent.

Să privim componentele MCP, beneficiile sale comparativ cu utilizarea directă a API-urilor și un exemplu de cum ar putea agenții AI să folosească un server MCP.

### Componentele de bază MCP

MCP operează pe o **arhitectură client-server** iar componentele de bază sunt:

• **Hosts** sunt aplicații LLM (de exemplu un editor de cod precum VSCode) care inițiază conexiunile către un server MCP.

• **Clients** sunt componente din cadrul aplicației host care mențin conexiuni unu-la-unu cu serverele.

• **Servers** sunt programe ușoare care expun capabilități specifice.

Incluse în protocol sunt trei primitive principale, care sunt capabilitățile unui server MCP:

• **Tools (Instrumente)**: Acestea sunt acțiuni sau funcții discrete pe care un agent AI le poate invoca pentru a efectua o acțiune. De exemplu, un serviciu meteo ar putea expune un instrument "obține vremea", sau un server de e-commerce ar putea expune un instrument "achiziționează produs". Serverele MCP publică numele fiecărui instrument, descrierea și schema de intrare/ieșire în listarea capabilităților.

• **Resources (Resurse)**: Acestea sunt elemente de date sau documente disponibile doar pentru citire pe care un server MCP le poate furniza, iar clientul le poate obține la cerere. Exemple includ conținutul fișierelor, înregistrări din baze de date sau fișiere de jurnal. Resursele pot fi text (de exemplu cod sau JSON) sau binare (de exemplu imagini sau PDF-uri).

• **Prompts (Indicații)**: Sunt șabloane predefinite care oferă indicații sugerate, permițând fluxuri de lucru mai complexe.

### Beneficiile MCP

MCP oferă avantaje semnificative pentru agenții AI:

• **Descoperire Dinamică a Instrumentelor**: Agenții pot primi dinamic o listă cu instrumentele disponibile de la un server împreună cu descrierile acestora. Acest lucru contrastează cu API-urile tradiționale, care de multe ori necesită cod statitc pentru integrare, ceea ce înseamnă că orice modificare a API-ului necesită actualizări de cod. MCP oferă o abordare „integrează o dată”, conducând la o adaptabilitate mai mare.

• **Interoperabilitate între diferite LLM-uri**: MCP funcționează peste diferite modele LLM, oferind flexibilitate de a schimba modelele de bază pentru a evalua performanțe mai bune.

• **Securitate Standardizată**: MCP include o metodă standard de autentificare, îmbunătățind scalabilitatea când se adaugă acces la servere MCP suplimentare. Acest lucru este mai simplu decât gestionarea diferitelor chei și tipuri de autentificare pentru diverse API-uri tradiționale.

### Exemplu MCP

![MCP Diagram](../../../translated_images/ro/mcp-diagram.e4ca1cbd551444a1.webp)

Imaginați-vă că un utilizator dorește să rezerve un zbor folosind un asistent AI alimentat de MCP.

1. **Conectare**: Asistentul AI (client MCP) se conectează la un server MCP furnizat de o companie aeriană.

2. **Descoperire instrument**: Clientul întreabă serverul MCP al companiei aeriene: „Ce instrumente aveți disponibile?” Serverul răspunde cu instrumente precum „căutare zboruri” și „rezervare zbor”.

3. **Invocare instrument**: Utilizatorul cere asistentului AI: „Te rog, caută un zbor de la Portland la Honolulu.” Asistentul AI, folosindu-și LLM-ul, identifică că trebuie să invoce instrumentul „căutare zboruri” și transmite parametrii relevanți (origine, destinație) serverului MCP.

4. **Executare și răspuns**: Serverul MCP, funcționând ca un înveliș, efectuează apelul real la API-ul intern de rezervări al companiei aeriene. Primește informațiile despre zbor (de exemplu date JSON) și le trimite înapoi asistentului AI.

5. **Interacțiune ulterioară**: Asistentul AI prezintă opțiunile de zbor. Odată ce utilizatorul selectează un zbor, asistentul poate invoca instrumentul „rezervă zbor” pe același server MCP, finalizând rezervarea.

## Protocolul Agent-la-Agent (A2A)

În timp ce MCP se concentrează pe conectarea LLM-urilor la instrumente, **protocolul Agent-to-Agent (A2A)** face un pas mai departe, permițând comunicarea și colaborarea între diferiți agenți AI. A2A conectează agenți AI din organizații, medii și stive tehnologice diferite pentru a îndeplini o sarcină comună.

Vom examina componentele și beneficiile A2A, împreună cu un exemplu de aplicare în aplicația noastră de călătorie.

### Componentele de bază A2A

A2A se concentrează pe facilitarea comunicării între agenți și pe colaborarea acestora pentru a îndeplini o sub-sarcină a utilizatorului. Fiecare componentă a protocolului contribuie la acest scop:

#### Agent Card

Similar modului în care un server MCP comunică o listă de instrumente, un Agent Card conține:
- Numele Agentului.
- O **descriere a sarcinilor generale** pe care le îndeplinește.
- O **listă de abilități specifice** cu descrieri pentru a ajuta alți agenți (sau chiar utilizatori umani) să înțeleagă când și de ce să invoce acel agent.
- **URL-ul Endpoint curent** al agentului.
- **Versiunea** și **capabilitățile** agentului, precum răspunsuri în streaming și notificări push.

#### Agent Executor

Agent Executor este responsabil pentru **transmiterea contextului conversației utilizatorului către agentul de la distanță**, agentul de la distanță având nevoie de aceste informații pentru a înțelege sarcina ce trebuie îndeplinită. Într-un server A2A, un agent folosește propriul său Model de Limbaj (LLM) pentru a interpreta solicitările și a executa sarcinile folosind propriile sale instrumente interne.

#### Artifact

Când agentul de la distanță finalizează sarcina solicitată, rezultatul său este generat sub forma unui artifact. Un artifact **conține rezultatul muncii agentului**, o **descriere a ceea ce a fost realizat** și **contextul textual** transmis prin protocol. După expedierea artifactului, conexiunea cu agentul de la distanță este închisă până la următoarea nevoie de utilizare.

#### Event Queue

Această componentă este folosită pentru **gestionarea actualizărilor și transmiterea mesajelor**. Este deosebit de importantă în producție pentru sistemele agentice, pentru a preveni închiderea conexiunii între agenți înainte ca o sarcină să fie finalizată, mai ales când timpul de finalizare poate fi mai mare.

### Beneficiile A2A

• **Colaborare îmbunătățită**: Permite agenților din diferiți furnizori și platforme să interacționeze, să împărtășească context și să lucreze împreună, facilitând automatizarea fluidă peste sisteme tradițional separate.

• **Flexibilitate în alegerea modelului**: Fiecare agent A2A poate decide ce LLM utilizează pentru a servi cererile sale, permițând modele optimizate sau ajustate pentru fiecare agent, spre deosebire de o conexiune unică LLM în unele scenarii MCP.

• **Autentificare integrată**: Autentificarea este integrată direct în protocolul A2A, oferind un cadru de securitate robust pentru interacțiunile agenților.

### Exemplu A2A

![A2A Diagram](../../../translated_images/ro/A2A-Diagram.8666928d648acc26.webp)

Să dezvoltăm scenariul nostru de rezervare călătorii, dar de data aceasta folosind A2A.

1. **Cererea utilizatorului către multi-agent**: Un utilizator interacționează cu un client/agent A2A "Agent de Călătorie", poate spunând: „Rezervă, te rog, o excursie completă la Honolulu pentru săptămâna viitoare, inclusiv zboruri, hotel și mașină închiriată”.

2. **Orchestrarea de către Agentul de Călătorie**: Agentul de Călătorie primește această cerere complexă. Folosește LLM-ul său pentru a raționa despre sarcină și stabilește că trebuie să interacționeze cu alți agenți specializați.

3. **Comunicare inter-agent**: Agentul de Călătorie folosește protocolul A2A pentru a se conecta la agenții downstream, precum „Agentul Companiei Aeriene”, „Agentul Hotelului” și „Agentul Închirieri Auto” creați de diferite companii.

4. **Executare delegată a sarcinilor**: Agentul de Călătorie trimite sarcini specifice acestor agenți specializați (de ex., „Găsește zboruri către Honolulu”, „Rezervă un hotel”, „Închiriază o mașină”). Fiecare agent specializat, rulând propriile LLM-uri și folosind propriile instrumente (care pot fi ele însele servere MCP), își realizează partea specifică din rezervare.

5. **Răspuns consolidat**: După ce toți agenții downstream finalizează sarcinile, Agentul de Călătorie compilează rezultatele (detalii zbor, confirmare hotel, rezervare mașină) și trimite un răspuns complet de tip chat către utilizator.

## Natural Language Web (NLWeb)

Site-urile web au fost mult timp principalul mod pentru utilizatori de a accesa informații și date pe internet.

Să analizăm componentele diferite ale NLWeb, beneficiile sale și un exemplu de lucru cu aplicația noastră de călătorie.

### Componentele NLWeb

- **Aplicația NLWeb (Codul serviciului de bază)**: Sistemul care procesează întrebările în limbaj natural. Leagă părțile diferite ale platformei pentru a genera răspunsuri. Poate fi considerat **motorul care alimentează funcționalitățile în limbaj natural** ale unui site.

- **Protocolul NLWeb**: Este un **set simplu de reguli pentru interacțiunea în limbaj natural** cu un site web. Trimite răspunsuri în format JSON (adesea folosind Schema.org). Scopul său este de a crea o bază simplă pentru „web-ul AI”, în aceeași manieră în care HTML a permis partajarea documentelor online.

- **Server MCP (Endpoint Model Context Protocol)**: Fiecare configurare NLWeb funcționează și ca un **server MCP**. Aceasta înseamnă că poate **partaja instrumente (cum ar fi metoda „ask”) și date** cu alte sisteme AI. În practică, aceasta face conținutul și capacitățile site-ului utilizabile de agenți AI, permițând site-ului să devină parte din ecosistemul mai larg de agenți.

- **Modele de embedding**: Aceste modele sunt folosite pentru a **converti conținutul site-ului în reprezentări numerice numite vectori (embedding-uri)**. Acești vectori surprind semnificația într-un mod comparabil și căutabil de către calculatoare. Sunt stocați într-o bază de date specială, iar utilizatorii pot alege modelul de embedding pe care doresc să îl folosească.

- **Baza de date vectorială (mecanism de căutare)**: Această bază de date **stochează embedding-urile conținutului site-ului**. Când cineva pune o întrebare, NLWeb verifică baza de date vectorială pentru a găsi rapid cele mai relevante informații. Returnează o listă rapidă de răspunsuri posibile, clasificate după similaritate. NLWeb funcționează cu sisteme diferite de stocare vectorială, precum Qdrant, Snowflake, Milvus, Azure AI Search și Elasticsearch.

### NLWeb prin exemplu

![NLWeb](../../../translated_images/ro/nlweb-diagram.c1e2390b310e5fe4.webp)

Să luăm din nou site-ul nostru de rezervări de călătorii, de data aceasta alimentat de NLWeb.

1. **Ingestia datelor**: Cataloagele existente de produse ale site-ului (de exemplu listări de zboruri, descrieri de hoteluri, pachete turistice) sunt formate folosind Schema.org sau încărcate prin feed-uri RSS. Instrumentele NLWeb preiau aceste date structurate, creează embedding-uri și le stochează într-o bază de date vectorială locală sau remote.

2. **Interogare în limbaj natural (uman)**: Un utilizator vizitează site-ul și, în loc să navigheze prin meniuri, tastează într-o interfață de chat: „Găsește-mi un hotel potrivit pentru familii în Honolulu cu piscină pentru săptămâna viitoare”.

3. **Procesarea NLWeb**: Aplicația NLWeb primește această întrebare. O trimite către un LLM pentru interpretare și simultan caută în baza sa vectorială pentru listări relevante de hoteluri.

4. **Rezultate de înaltă precizie**: LLM-ul ajută la interpretarea rezultatelor căutării din baza de date, identifică cele mai bune potriviri bazate pe criteriile „potrivite pentru familii”, „piscină” și „Honolulu” și apoi construiește un răspuns în limbaj natural. Esențial, răspunsul se referă la hoteluri reale din catalogul site-ului, evitând informații inventate.

5. **Interacțiune agent AI**: Deoarece NLWeb servește ca server MCP, un agent AI extern de călătorie ar putea să se conecteze la instanța NLWeb a acestui site. Agentul AI ar putea apoi folosi metoda MCP `ask` pentru a interoga direct site-ul: `ask("Există restaurante vegane recomandate în zona Honolulu de către hotel?")`. Instanța NLWeb ar procesa aceasta, folosind baza sa de date cu informații despre restaurante (dacă este încărcată), și ar returna un răspuns structurat JSON.

### Aveți mai multe întrebări despre MCP/A2A/NLWeb?

Alăturați-vă canalului [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la orele de consultanță și pentru a primi răspunsuri la întrebările despre agenții AI.

## Resurse

- [MCP pentru Începători](https://aka.ms/mcp-for-beginners)  
- [Documentație MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repo NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus utilizând serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă tradiucerea profesională realizată de un traducător uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->