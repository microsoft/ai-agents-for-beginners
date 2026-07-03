# Utilizarea Protocoalelor Agentice (MCP, A2A și NLWeb)

[![Agentic Protocols](../../../translated_images/ro/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

Pe măsură ce utilizarea agenților AI crește, crește și necesitatea unor protocoale care să asigure standardizare, securitate și să susțină inovația deschisă. În această lecție, vom acoperi 3 protocoale care încearcă să răspundă acestei nevoi - Model Context Protocol (MCP), Agent to Agent (A2A) și Natural Language Web (NLWeb).

## Introducere

În această lecție vom acoperi:

• Cum **MCP** permite agenților AI să acceseze unelte și date externe pentru a finaliza sarcinile utilizatorului.

• Cum **A2A** permite comunicarea și colaborarea între diferiți agenți AI.

• Cum **NLWeb** aduce interfețe în limbaj natural pe orice site web, permițând agenților AI să descopere și să interacționeze cu conținutul.

## Obiective de învățare

• **Identificarea** scopului principal și a beneficiilor MCP, A2A și NLWeb în contextul agenților AI.

• **Explicarea** modului în care fiecare protocol facilitează comunicarea și interacțiunea între LLM-uri, unelte și alți agenți.

• **Recunoașterea** rolurilor distincte pe care le joacă fiecare protocol în construirea sistemelor agentice complexe.

## Model Context Protocol

**Model Context Protocol (MCP)** este un standard deschis care oferă o modalitate standardizată pentru aplicații de a pune la dispoziție context și unelte către LLM-uri. Aceasta permite un „adaptor universal” către diferite surse de date și unelte la care agenții AI se pot conecta într-un mod consecvent.

Să analizăm componentele MCP, beneficiile în comparație cu utilizarea directă a API-urilor și un exemplu despre cum agenții AI ar putea folosi un server MCP.

### Componente principale MCP

MCP funcționează pe o **arhitectură client-server** iar componentele de bază sunt:

• **Hosts** sunt aplicații LLM (de exemplu un editor de cod precum VSCode) care inițiază conexiunile către un server MCP.

• **Clienți** sunt componente din aplicația host care mențin conexiuni unu-la-unu cu serverele.

• **Servere** sunt programe ușoare care expun capabilități specifice.

Protocolul include trei primitive de bază, care sunt capabilitățile unui server MCP:

• **Unelte**: Acestea sunt acțiuni sau funcții discrete pe care un agent AI le poate apela pentru a efectua o acțiune. De exemplu, un serviciu meteo ar putea expune o unealtă „get weather”, sau un server de comerț electronic ar putea expune o unealtă „purchase product”. Serverele MCP anunță numele fiecărei unelte, descrierea și schema de intrare/ieșire în lista de capabilități.

• **Resurse**: Acestea sunt elemente de date sau documente doar pentru citire, pe care un server MCP le poate oferi, iar clienții le pot prelua la cerere. Exemple includ conținut de fișiere, înregistrări de baze de date sau fișiere jurnal. Resursele pot fi text (cum ar fi cod sau JSON) sau binare (cum ar fi imagini sau PDF-uri).

• **Prompturi**: Acestea sunt șabloane predefinite care oferă prompturi sugerate, permițând fluxuri de lucru mai complexe.

### Beneficiile MCP

MCP oferă avantaje semnificative pentru agenții AI:

• **Descoperire dinamică a uneltelor**: Agenții pot primi dinamic o listă de unelte disponibile de la un server împreună cu descrieri ale funcțiilor acestora. Acest lucru contrastează cu API-urile tradiționale, care solicită adesea programare statică pentru integrări, ceea ce înseamnă că orice schimbare a API-ului necesită actualizări de cod. MCP oferă o abordare „integrează o dată”, conducând la o adaptabilitate mai mare.

• **Interoperabilitate între LLM-uri**: MCP funcționează cu diferite LLM-uri, oferind flexibilitate pentru a schimba modelele principale pentru a evalua performanța mai bună.

• **Securitate standardizată**: MCP include o metodă standard de autentificare, îmbunătățind scalabilitatea când se adaugă acces la servere MCP suplimentare. Este mai simplu decât gestionarea diferitelor chei și tipuri de autentificare pentru diverse API-uri tradiționale.

### Exemplu MCP

![MCP Diagram](../../../translated_images/ro/mcp-diagram.e4ca1cbd551444a1.webp)

Imaginați-vă că un utilizator dorește să rezerve un zbor folosind un asistent AI alimentat de MCP.

1. **Conexiune**: Asistentul AI (clientul MCP) se conectează la un server MCP furnizat de o companie aeriană.

2. **Descoperire unealtă**: Clientul întreabă serverul MCP al companiei aeriene: „Ce unelte aveți disponibile?” Serverul răspunde cu unelte precum „căutare zboruri” și „rezervare zboruri”.

3. **Invocarea uneltei**: Apoi îi ceri asistentului AI: „Te rog, caută un zbor de la Portland la Honolulu.” Asistentul AI, folosindu-și LLM-ul, identifică faptul că trebuie să apeleze unealta „căutare zboruri” și transmite parametrii relevanți (origine, destinație) serverului MCP.

4. **Executare și răspuns**: Serverul MCP, acționând ca un învelitor, face apelul propriu-zis către API-ul intern de rezervare al companiei aeriene. Apoi primește informațiile despre zbor (de exemplu, date JSON) și le trimite înapoi către asistentul AI.

5. **Interacțiune ulterioară**: Asistentul AI prezintă opțiunile de zbor. Odată ce selectați un zbor, asistentul poate invoca unealta „rezervare zbor” pe același server MCP, finalizând rezervarea.

## Protocolul Agent-la-Agent (A2A)

În timp ce MCP se concentrează pe conectarea LLM-urilor la unelte, **protocolul Agent-to-Agent (A2A)** face un pas mai departe, permițând comunicarea și colaborarea între diferiți agenți AI. A2A conectează agenți AI din organizații, medii și stive tehnologice diferite pentru a finaliza o sarcină comună.

Vom examina componentele și beneficiile A2A, împreună cu un exemplu de aplicare în aplicația noastră de călătorie.

### Componente de bază A2A

A2A se concentrează pe facilitarea comunicării între agenți și pe colaborarea pentru a finaliza o sub-sarcină a utilizatorului. Fiecare componentă a protocolului contribuie la aceasta:

#### Agent Card

Similar modului în care un server MCP oferă o listă de unelte, un Agent Card conține:
- Numele agentului.
- O **descriere a sarcinilor generale** pe care le finalizează.
- O **listă de abilități specifice** cu descrieri pentru a ajuta alți agenți (sau chiar utilizatori umani) să înțeleagă când și de ce ar dori să apeleze acel agent.
- **URL-ul Endpoint** curent al agentului.
- **Versiunea** și **capabilitățile** agentului, cum ar fi răspunsuri streaming și notificări push.

#### Executor Agent

Executorul Agent este responsabil pentru **transmiterea contextului chat-ului utilizatorului către agentul la distanță**, agentul la distanță are nevoie de aceste informații pentru a înțelege sarcina ce trebuie realizată. Într-un server A2A, un agent folosește propriul său Model de Limbaj de Mari Dimensiuni (LLM) pentru a parsa cererile primite și a executa sarcini utilizând uneltele interne proprii.

#### Artificat

Odată ce un agent la distanță a finalizat sarcina cerută, produsul muncii sale este creat ca un artefact. Un artefact **conține rezultatul muncii agentului**, o **descriere a ceea ce a fost finalizat** și **contextul text** care este transmis prin protocol. După trimiterea artefactului, conexiunea cu agentul la distanță se închide până când va fi nevoie din nou.

#### Coada de Evenimente

Această componentă este utilizată pentru **gestionarea actualizărilor și transmiterea mesajelor**. Este deosebit de importantă în producție pentru sistemele agentice, pentru a preveni închiderea conexiunii între agenți înainte ca o sarcină să fie finalizată, mai ales când timpii de completare pot fi mai lungi.

### Beneficiile A2A

• **Colaborare îmbunătățită**: Permite agenților de la diferiți furnizori și platforme să interacționeze, să împărtășească context și să colaboreze, facilitând automatizarea fără întreruperi între sisteme tradițional deconectate.

• **Flexibilitate în alegerea modelului**: Fiecare agent A2A poate decide ce LLM să folosească pentru a răspunde cererilor sale, permițând optimizarea sau specializarea modelelor pe agent, spre deosebire de o conexiune unică LLM în unele scenarii MCP.

• **Autentificare integrată**: Autentificarea este integrată direct în protocolul A2A, oferind un cadru robust de securitate pentru interacțiunile agenților.

### Exemplu A2A

![A2A Diagram](../../../translated_images/ro/A2A-Diagram.8666928d648acc26.webp)

Să extindem scenariul nostru de rezervare călătorii, de data aceasta folosind A2A.

1. **Cererea utilizatorului către multi-agent**: Un utilizator interacționează cu un client/agent A2A „Travel Agent”, poate spunând: „Te rog să rezervi o excursie completă la Honolulu pentru săptămâna viitoare, incluzând zboruri, hotel și închiriere mașină”.

2. **Orchestrarea de către Travel Agent**: Travel Agent primește această cerere complexă. Folosește LLM-ul său pentru a raționa despre sarcină și a determina că trebuie să interacționeze cu alți agenți specializați.

3. **Comunicare între agenți**: Travel Agent folosește apoi protocolul A2A pentru a se conecta la agenții secundari, precum „Agentul Companiei Aeriene”, „Agentul Hotelului” și „Agentul Închirieri Auto” creati de companii diferite.

4. **Executarea delegată a sarcinilor**: Travel Agent trimite sarcini specifice acestor agenți specializați (ex: „Găsește zboruri către Honolulu”, „Rezervă un hotel”, „Închiriază o mașină”). Fiecare agent specializat rulează propriul LLM și utilizează propriile unelte (care ar putea fi servere MCP), realizând partea sa specifică de rezervare.

5. **Răspuns consolidat**: Odată ce toți agenții secundari finalizează sarcinile, Travel Agent compilează rezultatele (detalii zbor, confirmare hotel, rezervare mașină) și trimite un răspuns complet, tip chat, utilizatorului.

## Natural Language Web (NLWeb)

Site-urile web au fost mult timp principalul mod prin care utilizatorii accesează informații și date pe internet.

Să analizăm diferitele componente ale NLWeb, beneficiile NLWeb și un exemplu despre cum funcționează NLWeb în aplicația noastră de călătorie.

### Componentele NLWeb

- **Aplicația NLWeb (codul serviciului de bază)**: Sistemul care procesează întrebările în limbaj natural. Leagă părțile diferite ale platformei pentru a crea răspunsuri. Poate fi considerat **motorul ce alimentează funcțiile în limbaj natural ale unui site**.

- **Protocolul NLWeb**: Este **un set de reguli de bază pentru interacțiunea în limbaj natural** cu un site web. Returnează răspunsuri în format JSON (adesea folosind Schema.org). Scopul său este să creeze o fundație simplă pentru „web-ul AI”, la fel cum HTML a făcut posibilă partajarea documentelor online.

- **Server MCP (Punctul final Model Context Protocol)**: Fiecare configurație NLWeb funcționează și ca un **server MCP**. Aceasta înseamnă că poate **partaja unelte (precum metoda „ask”) și date** cu alte sisteme AI. În practică, face conținutul și capabilitățile site-ului utilizabile de către agenții AI, permițând site-ului să devină parte din ecosistemul mai larg de agenți.

- **Modele de embedding**: Aceste modele sunt utilizate pentru a **converti conținutul site-ului web în reprezentări numerice numite vectori (embedding-uri)**. Acești vectori capturează sensul într-un mod în care computerele pot compara și căuta. Sunt stocați într-o bază de date specială, iar utilizatorii pot alege ce model de embedding doresc să utilizeze.

- **Baza de date vectorială (mecanism de căutare)**: Această bază de date **stochează embedding-urile conținutului site-ului**. Când cineva adresează o întrebare, NLWeb verifică baza de date vectorială pentru a găsi rapid cele mai relevante informații. Oferă o listă rapidă de posibile răspunsuri, clasificate după similitudine. NLWeb funcționează cu diferite sisteme de stocare vectorială precum Qdrant, Snowflake, Milvus, Azure AI Search și Elasticsearch.

### Exemplu NLWeb

![NLWeb](../../../translated_images/ro/nlweb-diagram.c1e2390b310e5fe4.webp)

Luați în considerare din nou site-ul nostru de rezervare călătorii, de data aceasta alimentat de NLWeb.

1. **Ingestia datelor**: Catalogurile existente ale site-ului de călătorii (ex: liste de zboruri, descrieri hoteluri, pachete turistice) sunt formatate folosind Schema.org sau încărcate prin feed-uri RSS. Uneltele NLWeb preiau aceste date structurate, creează embedding-uri și le stochează într-o bază de date vectorială locală sau la distanță.

2. **Interogare în limbaj natural (uman)**: Un utilizator vizitează site-ul și, în loc să navigheze prin meniuri, tastează într-o interfață de chat: „Găsește-mi un hotel prietenos cu familia în Honolulu cu piscină pentru săptămâna viitoare”.

3. **Procesarea NLWeb**: Aplicația NLWeb primește această interogare. O trimite unui LLM pentru înțelegere și, simultan, caută în baza sa de date vectorială listele relevante de hoteluri.

4. **Rezultate precise**: LLM-ul ajută la interpretarea rezultatelor din baza de date, identifică cele mai bune potriviri pe criteriile „prietenos cu familia”, „piscină” și „Honolulu”, apoi formulează un răspuns în limbaj natural. Esențial este că răspunsul se referă la hoteluri reale din catalogul site-ului, evitând informații inventate.

5. **Interacțiunea cu agentul AI**: Deoarece NLWeb servește ca server MCP, un agent AI extern pentru călătorii poate de asemenea să se conecteze la această instanță NLWeb a site-ului. Agentul AI poate folosi metoda `ask` MCP pentru a interoga site-ul direct: `ask("Există restaurante vegane recomandate în zona Honolulu de către hotel?")`. Instanța NLWeb ar procesa aceasta, valorificând baza sa de date despre restaurante (dacă este încărcată) și ar returna un răspuns structurat în JSON.

### Aveți mai multe întrebări despre MCP/A2A/NLWeb?

Alăturați-vă serverului [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la ore de consultanță și a primi răspunsuri despre agenții AI.

## Resurse

- [MCP pentru începători](https://aka.ms/mcp-for-beginners)  
- [Documentația MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->