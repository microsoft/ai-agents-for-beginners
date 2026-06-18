# Memoria pentru Agenții AI 
[![Agent Memory](../../../translated_images/ro/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Când discutăm despre beneficiile unice ale creării Agenților AI, două lucruri sunt principale: capacitatea de a apela unelte pentru a finaliza sarcini și capacitatea de a se îmbunătăți în timp. Memoria stă la baza creării agenților care se pot auto-îmbunătăți și pot crea experiențe mai bune pentru utilizatorii noștri.

În această lecție, vom analiza ce este memoria pentru Agenții AI și cum o putem gestiona și folosi în beneficiul aplicațiilor noastre.

## Introducere

Această lecție va acoperi:

• **Înțelegerea Memoriei Agenților AI**: Ce este memoria și de ce este esențială pentru agenți.

• **Implementarea și Stocarea Memoriei**: Metode practice pentru adăugarea capabilităților de memorie agenților AI, concentrându-ne pe memoria pe termen scurt și lung.

• **Transformarea Agenților AI în Agenți Auto-Îmbunătățitori**: Cum memoria permite agenților să învețe din interacțiunile trecute și să se îmbunătățească în timp.

## Implementări Disponibile

Această lecție include două tutoriale cu notebook-uri cuprinzătoare:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementează memoria folosind Mem0 și Azure AI Search cu Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementează memoria structurată folosind Cognee, construind automat un grafic al cunoștințelor susținut de embeddings, vizualizând graficul și făcând recuperarea inteligentă

## Obiective de Învățare

După parcurgerea acestei lecții, veți ști să:

• **Faceți diferența între diverse tipuri de memorie ale agenților AI**, inclusiv memoria de lucru, pe termen scurt și lung, precum și forme specializate precum memoria de persoană și memoria episodică.

• **Implementați și gestionați memoria pe termen scurt și lung pentru agenții AI** folosind Microsoft Agent Framework, utilizând unelte precum Mem0, Cognee, memoria Whiteboard și integrând cu Azure AI Search.

• **Înțelegeți principiile din spatele agenților AI auto-îmbunătățitori** și cum sistemele robuste de gestionare a memoriei contribuie la învățarea și adaptarea continuă.

## Înțelegerea Memoriei Agenților AI

În esență, **memoria pentru agenții AI se referă la mecanismele care le permit să rețină și să reamintească informații**. Aceste informații pot fi detalii specifice despre o conversație, preferințele utilizatorului, acțiuni precedente sau chiar tipare învățate.

Fără memorie, aplicațiile AI sunt adesea fără stare, ceea ce înseamnă că fiecare interacțiune începe de la zero. Acest lucru duce la o experiență utilizator repetitivă și frustrantă, unde agentul „uită” contextul sau preferințele anterioare.

### De ce este Importantă Memoria?

Inteligența unui agent este strâns legată de capacitatea sa de a reaminti și de a utiliza informațiile trecute. Memoria permite agenților să fie:

• **Reflectivi**: Învățând din acțiunile și rezultatele trecute.

• **Interactivi**: Menținând contextul pe durata unei conversații continue.

• **Proactivi și Reacționari**: Anticipând nevoile sau răspunzând adecvat pe baza datelor istorice.

• **Autonomi**: Operând mai independent prin accesarea cunoștințelor stocate.

Scopul implementării memoriei este de a face agenții mai **de încredere și capabili**.

### Tipuri de Memorie

#### Memoria de Lucru

Gândiți-vă la aceasta ca la o bucată de hârtie scratch pe care un agent o folosește în timpul unei sarcini sau a unui proces de gândire în desfășurare. Ea deține informații imediate necesare pentru a calcula următorul pas.

Pentru agenții AI, memoria de lucru captează adesea cele mai relevante informații dintr-o conversație, chiar dacă istoricul complet al chatului este lung sau truncat. Se concentrează pe extragerea elementelor cheie precum cerințe, propuneri, decizii și acțiuni.

**Exemplu Memorie de Lucru**

La un agent de rezervări de călătorie, memoria de lucru ar putea captura cererea curentă a utilizatorului, cum ar fi „Vreau să rezerv o călătorie la Paris”. Această cerință specifică este ținută în contextul imediat al agentului pentru a ghida interacțiunea curentă.

#### Memoria pe Termen Scurt

Acest tip de memorie reține informații pentru durata unei singure conversații sau sesiuni. Ea este contextul chatului curent, permițând agentului să se refere la schimbările anterioare din dialog.

În exemplele Python SDK din [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), aceasta corespunde lui `AgentSession`, creat cu `agent.create_session()`. Sesiunea este memoria pe termen scurt integrată în framework: păstrează contextul conversației disponibil cât timp aceeași sesiune este reutilizată, dar acel context nu este păstrat când sesiunea se termină sau aplicația este repornită. Folosiți memoria pe termen lung pentru fapte și preferințe care trebuie să supraviețuiască peste sesiuni, de obicei printr-o bază de date, index vectorial sau alt depozit persistent.

**Exemplu Memorie pe Termen Scurt**

Dacă un utilizator întreabă „Cât costă un zbor către Paris?” și apoi continuă cu „Dar ce zboruri sunt disponibile?”, memoria pe termen scurt asigură că agentul știe că „aici” se referă la „Paris” în aceeași conversație.

#### Memoria pe Termen Lung

Aceasta este informația care persistă peste multiple conversații sau sesiuni. Permite agenților să-și amintească preferințele utilizatorului, interacțiunile istorice sau cunoștințe generale pe perioade extinse. Acest lucru este important pentru personalizare.

**Exemplu Memorie pe Termen Lung**

O memorie pe termen lung ar putea stoca că „Ben se bucură de schi și activități în aer liber, îi place cafeaua cu vedere la munte și dorește să evite pârtiile dificile din cauza unei accidentări anterioare”. Aceste informații, învățate din interacțiunile anterioare, influențează recomandările în sesiunile viitoare de planificare a călătoriilor, făcându-le foarte personalizate.

#### Memoria de Persoană

Acest tip specializat de memorie ajută un agent să dezvolte o „personalitate” sau „persoană” consistentă. Permite agentului să-și amintească detalii despre sine sau rolul său intenționat, făcând interacțiunile mai fluente și concentrate.

**Exemplu Memorie de Persoană**
Dacă agentul de călătorie este conceput să fie un „expert în planificarea schiului”, memoria de persoană ar putea consolida acest rol, influențând răspunsurile pentru a corespunde tonului și cunoștințelor unui expert.

#### Memoria pentru Flux de Lucru / Episodică

Această memorie stochează succesiunea pașilor pe care un agent îi face în timpul unei sarcini complexe, inclusiv succesele și eșecurile. Este ca și cum ar păstra în memorie „episoade” sau experiențe trecute pentru a învăța din ele.

**Exemplu Memorie Episodică**

Dacă agentul a încercat să rezerve un zbor specific dar a eșuat din cauza indisponibilității, memoria episodică ar putea înregistra acest eșec, permițând agentului să încerce zboruri alternative sau să informeze utilizatorul despre problemă într-un mod mai bine informat la o încercare ulterioară.

#### Memoria Entitate

Aceasta implică extragerea și memorarea entităților specifice (precum persoane, locuri sau lucruri) și evenimente din conversații. Permite agentului să construiască o înțelegere structurată a elementelor cheie discutate.

**Exemplu Memorie Entitate**

Dintr-o conversație despre o călătorie trecută, agentul ar putea extrage „Paris,” „Turnul Eiffel” și „cină la restaurantul Le Chat Noir” ca entități. Într-o viitoare interacțiune, agentul ar putea reaminti „Le Chat Noir” și oferi să facă o nouă rezervare acolo.

#### Structured RAG (Generare Îmbunătățită prin Recuperare Structurată)

Deși RAG este o tehnică mai amplă, „Structured RAG” este evidențiată ca o tehnologie puternică de memorie. Ea extrage informații dense, structurate din diverse surse (conversații, emailuri, imagini) și le folosește pentru a îmbunătăți precizia, capacitatea de recuperare și viteza răspunsurilor. Spre deosebire de RAG clasic care se bazează numai pe similitudinea semantică, Structured RAG lucrează cu structura inerentă a informației.

**Exemplu Structured RAG**

În loc să potrivească doar cuvinte-cheie, Structured RAG ar putea analiza detalii de zbor (destinație, dată, oră, aeroliană) dintr-un email și să le stocheze într-un mod structurat. Aceasta permite interogări precise precum „Ce zbor am rezervat către Paris marți?”

## Implementarea și Stocarea Memoriei

Implementarea memoriei pentru agenții AI implică un proces sistematic de **gestionare a memoriei**, care include generarea, stocarea, recuperarea, integrarea, actualizarea și chiar „uitarea” (sau ștergerea) informațiilor. Recuperarea este un aspect deosebit de important.

### Instrumente Specializate de Memorie

#### Mem0

O modalitate de a stoca și gestiona memoria agentului este folosind unelte specializate precum Mem0. Mem0 funcționează ca un strat persistent de memorie, permițând agenților să reamintească interacțiuni relevante, să stocheze preferințe de utilizator și context factual și să învețe din succese și insuccese în timp. Ideea este că agenții stateless devin stateful.

Funcționează printr-un **proces în două faze de memorie: extragere și actualizare**. Mai întâi, mesajele adăugate într-un fir al agentului sunt trimise către serviciul Mem0, care folosește un Model de Limbaj Mare (LLM) pentru a rezuma istoricul conversației și pentru a extrage noi amintiri. Ulterior, o fază de actualizare condusă de LLM determină dacă să adauge, modifice sau șteargă aceste memorii, stocându-le într-un depozit hibrid de date ce poate include baze de date vectoriale, grafice și de tip cheie-valoare. Acest sistem susține de asemenea diverse tipuri de memorie și poate integra memoria grafică pentru gestionarea relațiilor dintre entități.

#### Cognee

O altă abordare puternică este utilizarea **Cognee**, o memorie semantică open-source pentru agenții AI care transformă date structurate și nestructurate în grafice de cunoștințe interogabile susținute de embeddings. Cognee oferă o **arhitectură cu două depozite** combinând căutarea prin similitudine vectorială cu relațiile grafice, permițând agenților să înțeleagă nu doar ce informație este similară, ci și cum conceptele sunt legate între ele.

Se remarcă în **recuperarea hibridă** care combină similitudinea vectorială, structura graficului și raționamentul LLM — de la căutarea simplă a fragmentelor la răspunsuri bazate pe graf. Sistemul menține o **memorie vie** care evoluează și crește în timp ce rămâne interogabilă ca un grafic conectat, susținând atât contextul de sesiune pe termen scurt cât și memoria persistentă pe termen lung.

Tutorialul cu notebook-ul Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrează construirea acestui strat unificat de memorie, cu exemple practice de ingestie a surselor diverse de date, vizualizarea graficului de cunoștințe și interogarea cu strategii diferite adaptate nevoilor specifice ale agenților.

### Stocarea Memoriei cu RAG

Dincolo de uneltele specializate de memorie precum mem0 , puteți folosi servicii robuste de căutare precum **Azure AI Search ca backend pentru stocarea și recuperarea memoriilor**, în special pentru RAG structurat.

Aceasta vă permite să ancorezi răspunsurile agentului în propriile date, asigurând răspunsuri mai relevante și precise. Azure AI Search poate fi folosit pentru a stoca amintiri specifice utilizatorilor legate de călătorii, cataloage de produse sau orice alt domeniu specific de cunoștințe.

Azure AI Search suportă capabilități precum **Structured RAG**, care excelează în extragerea și recuperarea informațiilor dense, structurate din seturi mari de date, precum istoricul conversațiilor, emailuri sau chiar imagini. Aceasta oferă „precizie și rechemare supra-umană” comparativ cu abordările tradiționale de segmentare a textului și embedding.

## Transformarea Agenților AI în Agenți Auto-Îmbunătățitori

Un model comun pentru agenții care se auto-îmbunătățesc implică introducerea unui **„agent de cunoștințe”**. Acest agent separat observă conversația principală dintre utilizator și agentul primar. Rolul său este să:

1. **Identifice informații valoroase**: Să determine dacă vreo parte a conversației merită salvată ca cunoștințe generale sau o preferință specifică utilizatorului.

2. **Extrage și rezumă**: Să distileze învățătura esențială sau preferința din conversație.

3. **Stocheze în baza de cunoștințe**: Să păstreze această informație extrasă, adesea într-o bază de date vectorială, pentru a putea fi recuperată ulterior.

4. **Completeze interogările viitoare**: Când utilizatorul inițiază o nouă interogare, agentul de cunoștințe recuperează informațiile relevante stocate și le atașează la promptul utilizatorului, oferind context crucial agentului primar (similar cu RAG).

### Optimizări pentru Memorie

• **Gestionarea Întârzierii**: Pentru a evita încetinirea interacțiunilor utilizatorului, se poate folosi inițial un model mai ieftin și mai rapid pentru a verifica rapid dacă informația merită salvată sau recuperată, invocând procesul mai complex de extragere/recuperare doar când este necesar.

• **Întreținerea Bazei de Cunoștințe**: Pentru o bază de cunoștințe în creștere, informațiile mai puțin folosite pot fi mutate într-un „depozit rece” pentru a gestiona costurile.

## Aveți Mai Multe Întrebări Despre Memoria Agenților?

Alăturați-vă [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a vă întâlni cu alți cursanți, a participa la sesiuni de tip office hours și a primi răspunsuri la întrebările despre Agenții AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->