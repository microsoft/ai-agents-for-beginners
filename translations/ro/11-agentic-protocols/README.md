# Utilizarea Protocoalelor Agentice (MCP, A2A și NLWeb)

[![Protocoale Agentice](../../../translated_images/ro/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Faceți clic pe imaginea de mai sus pentru a viziona video-ul acestei lecții)_

Pe măsură ce utilizarea agenților AI crește, crește și necesitatea unor protocoale care să asigure standardizarea, securitatea și să sprijine inovația deschisă. În această lecție, vom acoperi 3 protocoale ce încearcă să răspundă acestei nevoi - Model Context Protocol (MCP), Agent to Agent (A2A) și Natural Language Web (NLWeb).

## Introducere

În această lecție, vom acoperi:

• Cum **MCP** permite agenților AI să acceseze instrumente externe și date pentru a îndeplini sarcinile utilizatorului.

• Cum **A2A** facilitează comunicarea și colaborarea între diferiți agenți AI.

• Cum **NLWeb** aduce interfețe în limbaj natural pe orice site web, permițând agenților AI să descopere și să interacționeze cu conținutul.

## Obiective de Învățare

• **Identificarea** scopului principal și beneficiilor MCP, A2A și NLWeb în contextul agenților AI.

• **Explicarea** modului în care fiecare protocol facilitează comunicarea și interacțiunea între LLM-uri, instrumente și alți agenți.

• **Recunoașterea** rolurilor distincte pe care fiecare protocol le joacă în construirea sistemelor agentice complexe.

## Model Context Protocol

**Model Context Protocol (MCP)** este un standard deschis care oferă o modalitate standardizată pentru aplicații de a furniza context și instrumente către LLM-uri. Acest lucru permite un „adaptator universal” la diverse surse de date și instrumente la care agenții AI se pot conecta într-un mod consecvent.

Să analizăm componentele MCP, beneficiile comparativ cu utilizarea directă a API-urilor și un exemplu despre cum ar putea agenții AI să folosească un server MCP.

### Componentele de Bază ale MCP

MCP funcționează pe o **arhitectură client-server** iar componentele principale sunt:

• **Hosturi** sunt aplicații LLM (de exemplu un editor de cod precum VSCode) care inițiază conexiunile către un server MCP.

• **Clienți** sunt componente din cadrul aplicației host care mențin conexiuni unu-la-unu cu serverele.

• **Servere** sunt programe ușoare care expun capacități specifice.

În protocol sunt incluse trei primitive principale, care sunt capabilitățile unui server MCP:

• **Instrumente**: Acestea sunt acțiuni sau funcții discrete pe care un agent AI le poate apela pentru a efectua o acțiune. De exemplu, un serviciu meteo ar putea expune un instrument „get weather” (obține vremea), sau un server de e-commerce ar putea expune un instrument „purchase product” (cumpără produs). Serverele MCP afișează numele fiecărui instrument, descrierea și schema de intrare/ieșire în lista lor de capacități.

• **Resurse**: Acestea sunt elemente de date sau documente doar pentru citire pe care un server MCP le poate furniza, iar clienții le pot prelua la cerere. Exemple includ conținutul fișierelor, înregistrări de baze de date sau fișiere de jurnal. Resursele pot fi text (precum cod sau JSON) sau binare (precum imagini sau PDF-uri).

• **Prompturi**: Acestea sunt șabloane predefinite care oferă prompturi sugerate, permițând fluxuri de lucru mai complexe.

### Beneficiile MCP

MCP oferă avantaje semnificative pentru agenții AI:

• **Descoperire Dinamică a Instrumentelor**: Agenții pot primi dinamic o listă a instrumentelor disponibile de la un server împreună cu descrierile lor. Acest lucru contrastează cu API-urile tradiționale, care adesea solicită codificare statică pentru integrări, ceea ce înseamnă că orice schimbare de API necesită actualizări de cod. MCP oferă o abordare „integrează o singură dată”, conducând la o adaptabilitate mai mare.

• **Interoperabilitate între LLM-uri**: MCP funcționează între diferite LLM-uri, oferind flexibilitatea de a schimba modelele de bază pentru a evalua performanțe mai bune.

• **Securitate Standardizată**: MCP include o metodă standard de autentificare, îmbunătățind scalabilitatea la adăugarea accesului către servere MCP suplimentare. Este mai simplu decât gestionarea diferitelor chei și tipuri de autentificare pentru numeroasele API-uri tradiționale.

### Exemplu MCP

![Diagramă MCP](../../../translated_images/ro/mcp-diagram.e4ca1cbd551444a1.webp)

Imaginați-vă că un utilizator dorește să rezerve un zbor folosind un asistent AI alimentat de MCP.

1. **Conexiune**: Asistentul AI (clientul MCP) se conectează la un server MCP furnizat de o companie aeriană.

2. **Descoperirea Instrumentelor**: Clientul întreabă serverul MCP al companiei aeriene: „Ce instrumente aveți disponibile?” Serverul răspunde cu instrumente precum „search flights” (căutare zboruri) și „book flights” (rezervă zboruri).

3. **Invocarea Instrumentului**: Apoi îi cereți asistentului AI: „Te rog, caută un zbor de la Portland la Honolulu.” Asistentul AI, folosind LLM-ul său, identifică că trebuie să apeleze instrumentul „search flights” și transmite parametrii relevanți (plecare, destinație) serverului MCP.

4. **Executare și Răspuns**: Serverul MCP, acționând ca un înveliș, face apelul efectiv către API-ul intern de rezervări al companiei aeriene. Apoi primește informațiile despre zbor (de exemplu, date JSON) și le trimite înapoi asistentului AI.

5. **Interacțiune Ulterioară**: Asistentul AI prezintă opțiunile de zbor. Odată ce selectați un zbor, asistentul poate invoca instrumentul „book flight” pe același server MCP, finalizând rezervarea.

## Protocolul Agent-la-Agent (A2A)

În timp ce MCP se concentrează pe conectarea LLM-urilor la instrumente, **protocolul Agent-la-Agent (A2A)** face un pas mai departe, facilitând comunicarea și colaborarea între diferiți agenți AI. A2A conectează agenți AI din organizații, medii și tehnologii diferite pentru a finaliza o sarcină comună.

Vom examina componentele și beneficiile A2A, împreună cu un exemplu despre cum ar putea fi aplicat în aplicația noastră de călătorii.

### Componentele de Bază ale A2A

A2A se concentrează pe facilitarea comunicării între agenți și pe colaborarea lor pentru a îndeplini o sub-sarcină a utilizatorului. Fiecare componentă a protocolului contribuie la acest lucru:

#### Agent Card

Similar modului în care un server MCP partajează o listă de instrumente, un Agent Card conține:
- Numele Agentului.
- O **descriere a sarcinilor generale** pe care le îndeplinește.
- O **listă de abilități specifice** cu descrieri pentru a ajuta alți agenți (sau chiar utilizatori umani) să înțeleagă când și de ce ar dori să apeleze acel agent.
- **URL-ul Endpoint curent** al agentului.
- **Versiunea** și **capabilitățile** agentului, cum ar fi răspunsurile în timp real și notificările push.

#### Executorul Agentului

Executorul Agentului este responsabil pentru **transmiterea contextului conversației utilizatorului către agentul la distanță**, agentul la distanță având nevoie de acest context pentru a înțelege sarcina care trebuie îndeplinită. Într-un server A2A, un agent folosește propriul său Large Language Model (LLM) pentru a analiza cererile primite și a executa sarcini folosind propriile instrumente interne.

#### Artifact (Obiect)

După ce agentul la distanță a finalizat sarcina solicitată, rezultatul muncii sale este creat ca un artifact. Un artifact **conține rezultatul muncii agentului**, o **descriere a ceea ce a fost finalizat** și **contextul text** transmis prin protocol. După ce artifactul este trimis, conexiunea cu agentul la distanță este închisă până când este nevoie din nou.

#### Coada de Evenimente

Această componentă este folosită pentru **gestionarea actualizărilor și transmiterea mesajelor**. Este deosebit de importantă în producție pentru sistemele agentice, pentru a preveni închiderea conexiunii între agenți înainte de finalizarea sarcinii, mai ales când durata sarcinii poate fi mai lungă.

### Beneficiile A2A

• **Colaborare Îmbunătățită**: Permite agenților de la diferiți furnizori și platforme să interacționeze, să partajeze context și să lucreze împreună, facilitând automatizarea perfectă între sisteme tradițional separate.

• **Flexibilitate în Alegerea Modelului**: Fiecare agent A2A poate decide ce LLM folosește pentru a-și procesa cererile, permițând modele optimizate sau specializate pentru fiecare agent, spre deosebire de o singură conexiune LLM în unele scenarii MCP.

• **Autentificare Încorporată**: Autentificarea este integrată direct în protocolul A2A, oferind un cadru robust de securitate pentru interacțiunile între agenți.

### Exemplu A2A

![Diagramă A2A](../../../translated_images/ro/A2A-Diagram.8666928d648acc26.webp)

Să extindem scenariul nostru de rezervare de călătorii, dar de data aceasta folosind A2A.

1. **Cerere Utilizator către Multi-Agent**: Un utilizator interacționează cu un client/agent „Travel Agent” A2A, spunând, de exemplu, „Te rog să rezervi un întreg sejur la Honolulu pentru săptămâna viitoare, inclusiv zboruri, hotel și o mașină de închiriat”.

2. **Orchestrarea de către Travel Agent**: Travel Agent primește această cerere complexă. Folosește LLM-ul său pentru a raționa asupra sarcinii și stabilește că trebuie să interacționeze cu alți agenți specializați.

3. **Comunicare Inter-Agent**: Travel Agent folosește apoi protocolul A2A pentru a se conecta la agenți din aval, precum „Airline Agent”, „Hotel Agent” și „Car Rental Agent”, creați de companii diferite.

4. **Executarea Sarcinii Delegată**: Travel Agent trimite sarcini specifice acestor agenți specializați (ex. „Găsește zboruri către Honolulu”, „Rezervă un hotel”, „Închiriază o mașină”). Fiecare dintre acești agenți specializați, care rulează propriile LLM-uri și utilizează propriile instrumente (care ar putea fi ele însele servere MCP), își îndeplinește partea specifică a rezervării.

5. **Răspuns Consolidat**: Odată ce toți agenții din aval finalizează sarcinile, Travel Agent compilează rezultatele (detalii zbor, confirmare hotel, rezervare mașină) și trimite un răspuns complet, de tip conversație, utilizatorului.

## Natural Language Web (NLWeb)

Site-urile web au fost mult timp principalul mod pentru utilizatori de a accesa informații și date pe internet.

Să analizăm componentele diferite ale NLWeb, beneficiile NLWeb și un exemplu despre cum funcționează NLWeb urmărind aplicația noastră de călătorii.

### Componentele NLWeb

- **Aplicația NLWeb (Codul Serviciului de Bază)**: Sistemul care procesează întrebările în limbaj natural. Leagă diferitele părți ale platformei pentru a crea răspunsuri. Poate fi văzut ca **motorul care alimentează funcțiile în limbaj natural** ale unui site web.

- **Protocolul NLWeb**: Este un **set de reguli de bază pentru interacțiunea în limbaj natural** cu un site web. Trimite înapoi răspunsuri în format JSON (adesea folosind Schema.org). Scopul său este să creeze o fundație simplă pentru „Web-ul AI”, așa cum HTML a făcut posibilă partajarea documentelor online.

- **Server MCP (Punct Final Model Context Protocol)**: Fiecare configurare NLWeb funcționează și ca **server MCP**. Aceasta înseamnă că poate **partaja instrumente (cum ar fi metoda „ask”) și date** cu alte sisteme AI. În practică, acest lucru face conținutul și funcționalitățile site-ului utilizabile de agenți AI, permițând site-ului să devină parte a unui „ecosistem agent”.

- **Modele de Embedding**: Aceste modele sunt folosite pentru a **converti conținutul site-ului în reprezentări numerice numite vectori** (embedding-uri). Acești vectori capturează semnificația într-un mod pe care computerele îl pot compara și căuta. Sunt stocați într-o bază de date specială, iar utilizatorii pot alege ce model embedding doresc să folosească.

- **Baza de Date Vectorială (Mecanism de Recuperare)**: Această bază de date **stochează embedding-urile conținutului site-ului**. Când cineva pune o întrebare, NLWeb verifică baza vectorială pentru a găsi rapid cele mai relevante informații. Oferă o listă rapidă de posibile răspunsuri, ordonate după similaritate. NLWeb funcționează cu diferite sisteme de stocare vectorială precum Qdrant, Snowflake, Milvus, Azure AI Search și Elasticsearch.

### NLWeb prin Exemplu

![NLWeb](../../../translated_images/ro/nlweb-diagram.c1e2390b310e5fe4.webp)

Să luăm din nou site-ul nostru de rezervări de călătorii, dar de data aceasta este alimentat de NLWeb.

1. **Ingestia Datelor**: Cataloagele de produse existente ale site-ului de călătorii (de exemplu, liste de zboruri, descrieri de hoteluri, pachete turistice) sunt formate folosind Schema.org sau încărcate prin RSS feeduri. Instrumentele NLWeb încarcă aceste date structurate, creează embedding-uri și le stochează într-o bază de date vectorială locală sau la distanță.

2. **Interogare în Limbaj Natural (Om)**: Un utilizator vizitează site-ul și, în loc să navigheze prin meniuri, tastează într-o interfață de chat: „Găsește-mi un hotel prietenos cu familiile în Honolulu cu o piscină pentru săptămâna viitoare”.

3. **Procesarea NLWeb**: Aplicația NLWeb primește această interogare. O trimite către un LLM pentru înțelegere și, în același timp, caută în baza sa vectorială pentru listări relevante de hoteluri.

4. **Rezultate Precise**: LLM ajută la interpretarea rezultatelor din baza de date, identifică cele mai bune potriviri pe baza criteriilor „prietenos cu familiile”, „piscină” și „Honolulu”, apoi formulează un răspuns în limbaj natural. Important, răspunsul se referă la hoteluri reale din catalogul site-ului, evitând informațiile inventate.

5. **Interacțiunea Agentului AI**: Deoarece NLWeb funcționează ca un server MCP, un agent AI extern de călătorii ar putea, de asemenea, să se conecteze la instanța NLWeb a acestui site. Agentul AI ar putea apoi folosi metoda MCP `ask` pentru a interoga direct site-ul: `ask("Există restaurante vegane recomandate de hotel în zona Honolulu?")`. Instanța NLWeb ar procesa aceasta, folosindu-se de baza sa de date cu informații despre restaurante (dacă sunt încărcate), și ar răspunde cu un răspuns structurat în JSON.

### Mai Aveți Întrebări despre MCP/A2A/NLWeb?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la sesiuni de birou și a vă rezolva întrebările despre agenții AI.

## Resurse

- [MCP pentru Începători](https://aka.ms/mcp-for-beginners)  
- [Documentația MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repo NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Lecția Anterioară

[Agenți AI în Producție](../10-ai-agents-production/README.md)

## Lecția Următoare

[Inginerie a Contextului pentru Agenți AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->