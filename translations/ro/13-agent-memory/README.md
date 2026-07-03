# Memorie pentru Agenții AI 
[![Agent Memory](../../../translated_images/ro/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Când discutăm beneficiile unice ale creării Agenților AI, două aspecte sunt în principal dezbătute: capacitatea de a apela instrumente pentru a îndeplini sarcini și capacitatea de a se îmbunătăți în timp. Memoria este la baza creării unui agent auto-îmbunătățitor care poate crea experiențe mai bune pentru utilizatorii noștri.

În această lecție, vom analiza ce este memoria pentru Agenții AI și cum o putem gestiona și folosi în beneficiul aplicațiilor noastre.

## Introducere

Această lecție va acoperi:

• **Înțelegerea Memoriei Agenților AI**: Ce este memoria și de ce este esențială pentru agenți.

• **Implementarea și Stocarea Memoriei**: Metode practice pentru adăugarea capacităților de memorie agenților tăi AI, cu accent pe memoria pe termen scurt și lung.

• **Facerea Agenților AI Auto-Îmbunătățitori**: Cum permite memoria agenților să învețe din interacțiunile anterioare și să se îmbunătățească în timp.

## Implementări Disponibile

Această lecție include două tutoriale complete în notebook-uri:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementează memoria folosind Mem0 și Azure AI Search cu Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementează memoria structurată folosind Cognee, construind automat un grafic de cunoștințe susținut de embeddings, vizualizând graficul și realizând recuperare inteligentă

## Obiective de Învățare

După parcurgerea acestei lecții, vei ști să:

• **Diferențiezi între diverse tipuri de memorie ale agenților AI**, inclusiv memoria de lucru, pe termen scurt și pe termen lung, precum și forme specializate precum memoria de persoană și episodică.

• **Implementezi și gestionezi memoria pe termen scurt și lung pentru agenții AI** folosind Microsoft Agent Framework, valorificând instrumente precum Mem0, Cognee, memoria Whiteboard și integrându-le cu Azure AI Search.

• **Înțelegi principiile din spatele agenților AI auto-îmbunătățitori** și cum contribuie sistemele robuste de gestionare a memoriei la învățarea și adaptarea continuă.

## Înțelegerea Memoriei Agenților AI

La bază, **memoria pentru agenții AI se referă la mecanismele care le permit să rețină și să reamintească informații**. Aceste informații pot fi detalii specifice despre o conversație, preferințele utilizatorului, acțiuni trecute sau chiar modele învățate.

Fără memorie, aplicațiile AI sunt adesea stateless, adică fiecare interacțiune începe de la zero. Aceasta duce la o experiență repetitivă și frustrantă în care agentul „uita” contextul sau preferințele anterioare.

### De ce este Importantă Memoria?

Inteligența unui agent este profund legată de capacitatea sa de a reaminti și utiliza informații din trecut. Memoria permite agenților să fie:

• **Reflectivi**: să învețe din acțiunile și rezultatele anterioare.

• **Interactivi**: să mențină contextul pe durata unei conversații în desfășurare.

• **Proactivi și Reactivi**: să anticipeze nevoi sau să răspundă adecvat bazat pe date istorice.

• **Autonomi**: să opereze mai independent trăgând din cunoștințele stocate.

Scopul implementării memoriei este să facă agenții mai **de încredere și capabili**.

### Tipuri de Memorie

#### Memorie de Lucru

Gândește-te la aceasta ca la o bucată de hârtie de schiță pe care un agent o folosește pe durata unei singure sarcini sau a unui proces de gândire în desfășurare. Reține informațiile imediate necesare pentru a calcula pasul următor.

Pentru agenții AI, memoria de lucru capturează adesea cele mai relevante informații dintr-o conversație, chiar dacă istoricul complet al chat-ului este lung sau trunchiat. Se concentrează pe extragerea elementelor cheie precum cerințe, propuneri, decizii și acțiuni.

**Exemplu de Memorie de Lucru**

În cazul unui agent de rezervări de călătorii, memoria de lucru poate reține cererea curentă a utilizatorului, cum ar fi „Vreau să rezerv o călătorie la Paris”. Această cerință specifică este ținută în contextul imediat al agentului pentru a ghida interacțiunea curentă.

#### Memorie pe Termen Scurt

Acest tip de memorie reține informații pe durata unei singure conversații sau sesiuni. Este contextul chat-ului curent, permițând agentului să se refere la repetițiile anterioare din dialog.

În exemplele din SDK-ul Python al [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), acest lucru corespunde cu `AgentSession`, creat cu `agent.create_session()`. Sesiunea este memoria pe termen scurt construită în framework: păstrează contextul conversației disponibil atâta timp cât aceeași sesiune este reutilizată, dar contextul nu este păstrat când sesiunea se încheie sau aplicația este repornită. Folosește memoria pe termen lung pentru fapte și preferințe care trebuie să supraviețuiască peste sesiuni, de obicei printr-o bază de date, index vectorial sau alt depozit persistent.

**Exemplu de Memorie pe Termen Scurt**

Dacă un utilizator întreabă „Cât ar costa un zbor către Paris?” și apoi continuă cu „Dar cazarea acolo?”, memoria pe termen scurt asigură că agentul știe că „acolo” se referă la „Paris” în cadrul aceleiași conversații.

#### Memorie pe Termen Lung

Aceasta este informația care persistă peste mai multe conversații sau sesiuni. Permite agenților să-și amintească preferințele utilizatorilor, interacțiunile istorice sau cunoștințele generale pe perioade extinse. Este importantă pentru personalizare.

**Exemplu de Memorie pe Termen Lung**

O memorie pe termen lung poate stoca că „Ben se bucură de schi și activități în aer liber, îi place cafeaua cu vedere la munte și dorește să evite pârtiile avansate de schi din cauza unei accidentări anterioare”. Această informație, învățată din interacțiunile anterioare, influențează recomandările în sesiunile viitoare de planificare a călătoriilor, făcându-le foarte personalizate.

#### Memoria de Persoană (Persona Memory)

Acest tip specializat de memorie ajută un agent să dezvolte o „personalitate” sau „persoană” consistentă. Permite agentului să-și amintească detalii despre sine sau rolul său intenționat, făcând interacțiunile mai fluide și concentrate.

**Exemplu de Memorie de Persoană**

Dacă agentul de călătorii este proiectat să fie un „expert în planificarea schiului”, memoria de persoană poate consolida acest rol, influențând răspunsurile să se alinieze cu tonul și cunoștințele unui expert.

#### Memoria de Workflow/Episodică

Această memorie stochează secvența de pași pe care un agent îi parcurge în timpul unei sarcini complexe, inclusiv succese și eșecuri. Este ca o amintire a unor „episoade” sau experiențe trecute pentru a învăța din ele.

**Exemplu de Memorie Episodică**

Dacă agentul a încercat să rezerve un zbor specific, dar acesta a eșuat din cauza indisponibilității, memoria episodică poate înregistra acest eșec, permițând agentului să încerce zboruri alternative sau să informeze utilizatorul despre problemă într-un mod mai informat la o încercare ulterioară.

#### Memoria de Entități

Aceasta implică extragerea și memorarea entităților specifice (cum ar fi persoane, locuri sau obiecte) și a evenimentelor din conversații. Permite agentului să construiască o înțelegere structurată a elementelor cheie discutate.

**Exemplu de Memorie de Entități**

Dintr-o conversație despre o călătorie anterioară, agentul poate extrage „Paris”, „Turnul Eiffel” și „cină la restaurantul Le Chat Noir” ca entități. Într-o interacțiune viitoare, agentul ar putea să-și amintească de „Le Chat Noir” și să ofere să facă o nouă rezervare acolo.

#### RAG Structurat (Retrieval Augmented Generation)

Deși RAG este o tehnică mai largă, „RAG Structurat” este evidențiată ca o tehnologie puternică de memorie. Aceasta extrage informații dense, structurate din diverse surse (conversații, emailuri, imagini) și le folosește pentru a îmbunătăți precizia, recuperarea și viteza răspunsurilor. Spre deosebire de RAG clasic care se bazează numai pe similaritatea semantică, RAG Structurat lucrează cu structura inerentă a informației.

**Exemplu de RAG Structurat**

În loc să potrivească doar cuvinte-cheie, RAG Structurat poate analiza detalii de zbor (destinație, dată, oră, companie aeriană) dintr-un email și să le stocheze într-un mod structurat. Aceasta permite întrebări precise precum „Ce zbor am rezervat către Paris marți?”

## Implementarea și Stocarea Memoriei

Implementarea memoriei pentru agenții AI implică un proces sistematic de **gestionare a memoriei**, care include generarea, stocarea, recuperarea, integrarea, actualizarea și chiar „uitarea” (sau ștergerea) informației. Recuperarea este un aspect deosebit de crucial.

### Instrumente Specializate de Memorie

#### Mem0

Un mod de a stoca și gestiona memoria agenților este folosind instrumente specializate precum Mem0. Mem0 funcționează ca un strat de memorie persistentă, permițând agenților să-și amintească interacțiuni relevante, să stocheze preferințele utilizatorilor și contextul factual, și să învețe din succese și eșecuri în timp. Ideea este ca agenții stateless să devină stateful.

Funcționează printr-un **proces în două faze: extragere și actualizare**. Mai întâi, mesajele adăugate la un fir al agentului sunt trimise serviciului Mem0, care folosește un Large Language Model (LLM) pentru a rezuma istoricul conversației și a extrage noi memorii. Ulterior, o fază de actualizare condusă de LLM determină dacă să adauge, modifice sau șteargă aceste memorii, stocându-le într-un depozit de date hibrid care poate include baze de date vectoriale, grafice și key-value. Acest sistem suportă diverse tipuri de memorie și poate încorpora memoria grafică pentru gestionarea relațiilor între entități.

#### Cognee

O altă abordare puternică este folosirea **Cognee**, o memorie semantică open-source pentru agenții AI care transformă datele structurate și nestructurate în grafice de cunoștințe interogabile, susținute de embeddings. Cognee oferă o **arhitectură duală** ce combină căutarea vectorială pe baza similarității cu relațiile grafice, permițând agenților să înțeleagă nu doar ce informație este similară, ci cum conceptele se relaționează între ele.

Excelează în **recuperare hibridă** care combină similaritatea vectorială, structura grafică și raționamentul LLM - de la căutarea simplă de bucăți brute la răspunsuri la întrebări conștiente de graf. Sistemul menține o **memorie vie** care evoluează și crește, rămânând interogabilă ca un graf conectat, susținând atât contextul pe termen scurt în sesiuni, cât și memoria persistentă pe termen lung.

Tutorialul din notebook-ul Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrează construirea acestui strat unificat de memorie, cu exemple practice de ingestie a diverselor surse de date, vizualizarea graficului de cunoștințe și interogarea cu diferite strategii de căutare adaptate nevoilor specifice ale agentului.

### Stocarea Memoriei cu RAG

Dincolo de instrumentele specializate precum Mem0, poți valorifica servicii robuste de căutare precum **Azure AI Search ca backend pentru stocarea și recuperarea memoriilor**, în special pentru RAG structurat.

Aceasta îți permite să ancorezi răspunsurile agentului în propriile tale date, asigurând răspunsuri mai relevante și precise. Azure AI Search poate fi folosit pentru a stoca amintirile de călătorie specifice utilizatorilor, cataloage de produse sau orice altă cunoaștere specifică domeniului.

Azure AI Search suportă facilități precum **RAG Structurat**, care excellează în extragerea și recuperarea informației dense, structurate din seturi mari de date, cum ar fi istoricul conversațiilor, emailuri sau chiar imagini. Aceasta oferă „precizie și capacitate de recuperare supraumană” comparativ cu metodele tradiționale de fragmentare și embedding text.

## Transformarea Agenților AI în Auto-Îmbunătățitori

Un model comun pentru agenții auto-îmbunătățitori implică introducerea unui **„agent al cunoștințelor”**. Acest agent separat observă conversația principală dintre utilizator și agentul principal. Rolul său este să:

1. **Identifice informații valoroase**: Să determine dacă vreo parte a conversației merită salvată ca cunoaștere generală sau preferință specifică a utilizatorului.

2. **Extraga și rezume**: Să distileze învățătura esențială sau preferința din conversație.

3. **Stocheze într-o bază de cunoștințe**: Să păstreze această informație extrasă, adesea într-o bază de date vectorială, pentru a fi recuperată mai târziu.

4. **Completeze interogările viitoare**: Când utilizatorul inițiază o nouă interogare, agentul cunoștințelor recuperează informațiile stocate relevante și le adaugă în promptul utilizatorului, oferind un context crucial agentului principal (asemănător RAG).

### Optimizări pentru Memorie

• **Gestionarea latenței**: Pentru a evita încetinirea interacțiunilor cu utilizatorul, se poate folosi inițial un model mai ieftin și mai rapid pentru a verifica rapid dacă informația merită stocată sau recuperată, invocând procesul mai complex de extragere/recuperare doar când este necesar.

• **Întreținerea bazei de cunoștințe**: Pentru o bază de cunoștințe în creștere, informațiile mai puțin folosite frecvent pot fi mutate în „stocare la rece” pentru a gestiona costurile.

## Ai Mai Multe Întrebări Despre Memoria Agenților?

Alătură-te comunității [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la sesiuni de consultanță și a primi răspunsuri la întrebările tale despre Agenții AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->