# Utilizarea Protocolurilor Agentice (MCP, A2A și NLWeb)

[![Agentic Protocols](../../../translated_images/ro/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

Pe măsură ce utilizarea agenților AI crește, crește și necesitatea protocoalelor care asigură standardizare, securitate și sprijin pentru inovația deschisă. În această lecție, vom acoperi 3 protocoale care caută să satisfacă această nevoie - Model Context Protocol (MCP), Agent to Agent (A2A) și Natural Language Web (NLWeb).

## Introducere

În această lecție vom aborda:

• Cum **MCP** permite Agenților AI să acceseze instrumente și date externe pentru a finaliza sarcinile utilizatorului.

• Cum **A2A** permite comunicarea și colaborarea între diferiți agenți AI.

• Cum **NLWeb** aduce interfețe în limbaj natural pe orice site web, permițând Agenților AI să descopere și să interacționeze cu conținutul.

## Obiective de învățare

• **Identificați** scopul principal și beneficiile MCP, A2A și NLWeb în contextul agenților AI.

• **Explicați** cum fiecare protocol facilitează comunicarea și interacțiunea între LLM-uri, instrumente și alți agenți.

• **Recunoașteți** rolurile distincte pe care fiecare protocol le joacă în construirea sistemelor agentice complexe.

## Model Context Protocol

**Model Context Protocol (MCP)** este un standard deschis care oferă o modalitate standardizată pentru aplicații de a furniza context și instrumente către LLM-uri. Aceasta permite un „adaptor universal” la diferite surse de date și instrumente la care Agenții AI se pot conecta într-un mod consecvent.

Să analizăm componentele MCP, beneficiile comparativ cu utilizarea directă a API-urilor și un exemplu de cum agenții AI ar putea folosi un server MCP.

### Componentele de bază MCP

MCP funcționează pe o **arhitectură client-server** iar componentele de bază sunt:

• **Host-urile** sunt aplicații LLM (de exemplu, un editor de cod precum VSCode) care inițiază conexiunile către un server MCP.

• **Clienții** sunt componente din cadrul aplicației host care mențin conexiuni unu-la-unu cu serverele.

• **Serverele** sunt programe ușoare care expun capabilități specifice.

Protocolul include trei primitive de bază care sunt capabilitățile unui server MCP:

• **Instrumente**: Acestea sunt acțiuni sau funcții discrete pe care un agent AI le poate apela pentru a executa o acțiune. De exemplu, un serviciu meteo ar putea expune un instrument "get weather", sau un server e-commerce ar putea expune un instrument "purchase product". Serverele MCP listează numele fiecărui instrument, descrierea și schema de intrare/ieșire în capacitățile lor.

• **Resurse**: Acestea sunt elemente de date sau documente doar pentru citire pe care un server MCP le poate furniza, iar clienții le pot accesa la cerere. Exemple includ conținutul fișierelor, înregistrări din baze de date sau fișiere jurnal. Resursele pot fi text (precum cod sau JSON) sau binare (imagini sau PDF-uri).

• **Prompts**: Acestea sunt șabloane predefinite care oferă sugestii de prompturi, permițând fluxuri de lucru mai complexe.

### Beneficiile MCP

MCP oferă avantaje semnificative pentru Agenții AI:

• **Descoperire Dinamică a Instrumentelor**: Agenții pot primi dinamic o listă a instrumentelor disponibile de la un server împreună cu descrieri ale funcționalității acestora. Acest lucru contrastează cu API-urile tradiționale, care deseori necesită codificare statică pentru integrări, ceea ce înseamnă că orice schimbare de API necesită actualizări de cod. MCP oferă o abordare „integrează o dată”, conducând la o adaptabilitate mai mare.

• **Interoperabilitate între LLM-uri**: MCP funcționează cu diferite LLM-uri, oferind flexibilitate pentru a schimba modelele principale pentru a evalua performanțele mai bune.

• **Securitate Standardizată**: MCP include o metodă standard de autentificare, îmbunătățind scalabilitatea atunci când se adaugă acces la servere MCP suplimentare. Este mai simplu decât să gestionezi chei și tipuri de autentificare diferite pentru diverse API-uri tradiționale.

### Exemplu MCP

![MCP Diagram](../../../translated_images/ro/mcp-diagram.e4ca1cbd551444a1.webp)

Imaginați-vă că un utilizator dorește să rezerve un zbor folosind un asistent AI alimentat de MCP.

1. **Conexiunea**: Asistentul AI (clientul MCP) se conectează la un server MCP oferit de o companie aeriană.

2. **Descoperirea Instrumentelor**: Clientul întreabă serverul MCP al companiei aeriene: „Ce instrumente aveți disponibile?” Serverul răspunde cu instrumente precum „căutare zboruri” și „rezervare zboruri”.

3. **Invocarea Instrumentului**: Utilizatorul îi cere asistentului AI: „Te rog, caută un zbor de la Portland la Honolulu.” Asistentul AI, folosind LLM-ul său, identifică că trebuie să apeleze instrumentul „căutare zboruri” și transmite parametrii relevanți (oraș plecare, destinație) serverului MCP.

4. **Executare și Răspuns**: Serverul MCP, acționând ca un înveliș, face apelul real către API-ul intern de rezervări al companiei aeriene. Apoi primește informațiile despre zbor (de exemplu, date JSON) și le trimite înapoi asistentului AI.

5. **Interacțiune ulterioară**: Asistentul AI prezintă opțiunile de zbor. După ce utilizatorul selectează un zbor, asistentul poate invoca instrumentul „rezervare zbor” pe același server MCP pentru a finaliza rezervarea.

## Protocolul Agent-la-Agent (A2A)

În timp ce MCP se concentrează pe conectarea LLM-urilor la instrumente, **protocolul Agent-la-Agent (A2A)** face un pas înainte, permițând comunicarea și colaborarea între diferiți agenți AI. A2A conectează agenți AI din organizații, medii și tehnologii diferite pentru a finaliza o sarcină comună.

Vom examina componentele și beneficiile A2A, împreună cu un exemplu de aplicare în aplicația noastră de călătorii.

### Componentele de bază A2A

A2A se concentrează pe facilitarea comunicării între agenți și colaborarea lor pentru a îndeplini o subtare a utilizatorului. Fiecare componentă a protocolului contribuie la acest lucru:

#### Agent Card

Similar cu modul în care un server MCP partajează o listă de instrumente, un Agent Card conține:
- Numele Agentului.
- O **descriere a sarcinilor generale** pe care le îndeplinește.
- O **listă a abilităților specifice** cu descrieri pentru a ajuta alți agenți (sau chiar utilizatori umani) să înțeleagă când și de ce ar dori să apeleze acel agent.
- **URL-ul Endpoint actual** al agentului
- **versiunea** și **capabilitățile** agentului, cum ar fi răspunsuri prin streaming și notificări push.

#### Executorul Agentului

Executorul Agentului este responsabil de **transmiterea contextului conversației utilizatorului către agentul la distanță**, agentul la distanță are nevoie de acest context pentru a înțelege sarcina ce trebuie realizată. Într-un server A2A, un agent folosește propriul său Model LLM pentru a analiza cererile primite și a executa sarcini folosind instrumentele interne proprii.

#### Artifact (Produsul muncii)

După ce un agent la distanță a finalizat sarcina cerută, produsul său este creat ca un artifact. Un artifact **conține rezultatul muncii agentului**, o **descriere a ceea ce a fost realizat** și contextul textual care este transmis prin protocol. După trimiterea artifactului, conexiunea cu agentul la distanță este închisă până când este necesară din nou.

#### Coada de evenimente

Această componentă este folosită pentru **gestionarea actualizărilor și transmiterea mesajelor**. Este deosebit de importantă în producție pentru sistemele agentice pentru a preveni închiderea conexiunii între agenți înainte de finalizarea sarcinii, mai ales când timpul de finalizare al sarcinii poate dura mai mult.

### Beneficiile A2A

• **Colaborare Îmbunătățită**: Permite agenților de la diferiți furnizori și platforme să interacționeze, să împărtășească context și să lucreze împreună, facilitând automatizarea fără întreruperi peste sisteme tradițional separate.

• **Flexibilitate în Selectarea Modelului**: Fiecare agent A2A poate decide ce LLM folosește pentru a-și deservi cererile, permițând optimizarea sau reglarea fină a modelelor per agent, spre deosebire de o singură conexiune LLM în unele scenarii MCP.

• **Autentificare Integrată**: Autentificarea este integrată direct în protocolul A2A, oferind un cadru robust de securitate pentru interacțiunile agenților.

### Exemplu A2A

![A2A Diagram](../../../translated_images/ro/A2A-Diagram.8666928d648acc26.webp)

Să extindem scenariul nostru de rezervare călătorii, dar de data aceasta folosind A2A.

1. **Cerere utilizator către Multi-Agent**: Un utilizator interacționează cu un client/agent A2A numit „Agent de Călătorii”, poate spunând: „Te rog să rezervi o excursie completă la Honolulu pentru săptămâna viitoare, incluzând zboruri, hotel și mașină de închiriat”.

2. **Orchestrarea de către Agentul de Călătorii**: Agentul de Călătorii primește această cerere complexă. Folosește LLM-ul său pentru a raționa asupra sarcinii și a determina că trebuie să interacționeze cu alți agenți specializați.

3. **Comunicarea între Agenți**: Agentul de Călătorii folosește apoi protocolul A2A pentru a se conecta la agenții aval, cum ar fi „Agentul Companiei Aeriene”, „Agentul Hotelier” și „Agentul de Închirieri Auto” creați de companii diferite.

4. **Executarea Sarcinilor Delegată**: Agentul de Călătorii trimite sarcini specifice acestor agenți specializați (de exemplu, „Găsește zboruri spre Honolulu,” „Rezervă un hotel,” „Închiriază o mașină”). Fiecare dintre acești agenți ale căror modele LLM și instrumente proprii rulează (care ar putea fi ei înșiși servere MCP) execută partea sa specifică a rezervării.

5. **Răspuns Consolidat**: După ce toți agenții aval finalizează sarcinile, Agentul de Călătorii compilează rezultatele (detalii zbor, confirmare hotel, rezervare mașină) și trimite un răspuns cuprinzător, de tip chat, înapoi utilizatorului.

## Natural Language Web (NLWeb)

Site-urile web au fost mult timp modalitatea principală pentru utilizatori de a accesa informații și date pe internet.

Să analizăm diferitele componente ale NLWeb, beneficiile NLWeb și un exemplu de funcționare a NLWeb privind aplicația noastră de călătorii.

### Componentele NLWeb

- **Aplicația NLWeb (Codul de bază al serviciului)**: Sistemul care procesează întrebările în limbaj natural. Leagă diferitele părți ale platformei pentru a crea răspunsuri. Poate fi considerat **motorul care alimentează funcționalitățile în limbaj natural** ale unui site web.

- **Protocolul NLWeb**: Este un **set de reguli fundamentale pentru interacțiunea în limbaj natural** cu un site web. Returnează răspunsuri în format JSON (adesea folosind Schema.org). Scopul său este de a crea o fundație simplă pentru „Web-ul AI”, în același mod în care HTML a făcut posibilă partajarea documentelor online.

- **Server MCP (Punctul final Model Context Protocol)**: Fiecare configurare NLWeb funcționează și ca un **server MCP**. Aceasta înseamnă că poate **partaja instrumente (cum ar fi metoda „ask”) și date** cu alte sisteme AI. În practică, acest lucru face conținutul și capacitățile site-ului utilizabile de agenții AI, permițând site-ului să devină parte a ecosistemului larg al agenților.

- **Modele de embedding**: Aceste modele sunt utilizate pentru a **converti conținutul site-ului web în reprezentări numerice numite vectori** (embedding-uri). Acești vectori capturează sensul într-un mod pe care computerele îl pot compara și căuta. Sunt stocați într-o bază de date specială, iar utilizatorii pot alege ce model de embedding doresc să utilizeze.

- **Baza de date vectorială (Mecanismul de căutare)**: Această bază de date **stochează embedding-urile conținutului site-ului web**. Când cineva pune o întrebare, NLWeb verifică baza de date vectorială pentru a găsi rapid cele mai relevante informații. Oferă o listă rapidă de posibile răspunsuri, clasificate după similaritate. NLWeb funcționează cu diferite sisteme de stocare a vectorilor, precum Qdrant, Snowflake, Milvus, Azure AI Search și Elasticsearch.

### NLWeb prin Exemplu

![NLWeb](../../../translated_images/ro/nlweb-diagram.c1e2390b310e5fe4.webp)

Luați din nou site-ul nostru de rezervări pentru călătorii, dar de această dată este alimentat de NLWeb.

1. **Ingestia datelor**: Catalogurile existente ale site-ului de călătorii (de exemplu, liste de zboruri, descrieri de hoteluri, pachete turistice) sunt formatate folosind Schema.org sau încărcate prin feed-uri RSS. Instrumentele NLWeb preiau aceste date structurate, creează embedding-uri și le stochează într-o bază de date vectorială locală sau remote.

2. **Interogare în limbaj natural (uman)**: Un utilizator vizitează site-ul și, în loc să navigheze prin meniuri, tastează într-o interfață de chat: „Găsește-mi un hotel prietenos pentru familie în Honolulu cu piscină pentru săptămâna viitoare”.

3. **Procesarea NLWeb**: Aplicația NLWeb primește această interogare. O trimite la un LLM pentru înțelegere și simultan caută în baza sa de date vectorială pentru liste relevante de hoteluri.

4. **Rezultate precise**: LLM-ul ajută la interpretarea rezultatelor căutării din baza de date, identifică cele mai bune potriviri pe baza criteriilor „prietenoasă pentru familie”, „piscină” și „Honolulu”, apoi formatează un răspuns în limbaj natural. Esențial, răspunsul face referire la hoteluri reale din catalogul site-ului, evitând informațiile inventate.

5. **Interacțiunea Agentului AI**: Deoarece NLWeb funcționează ca un server MCP, un agent AI extern pentru călătorii se poate conecta de asemenea la instanța NLWeb a acestui site. Agentul AI poate apoi folosi metoda `ask` MCP pentru a interoga direct site-ul: `ask("Există restaurante vegane recomandate de hotel în zona Honolulu?")`. Instanța NLWeb procesează aceasta, valorificând baza sa de date cu informații despre restaurante (dacă este încărcată) și returnează un răspuns structurat JSON.

### Aveți Mai Multe Întrebări despre MCP/A2A/NLWeb?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la sesiuni de birou și a primi răspunsuri la întrebările despre Agenții AI.

## Resurse

- [MCP pentru Începători](https://aka.ms/mcp-for-beginners)  
- [Documentația MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repo NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Lecția Anterioară

[Agenți AI în Producție](../10-ai-agents-production/README.md)

## Lecția Următoare

[Ingineria Contextului pentru Agenții AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->