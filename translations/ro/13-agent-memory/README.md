# Memorie pentru Agenții AI 
[![Agent Memory](../../../translated_images/ro/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Când discutăm beneficiile unice ale creării Agenților AI, două lucruri sunt în principal abordate: capacitatea de a apela instrumente pentru a finaliza sarcini și capacitatea de a se îmbunătăți în timp. Memoria este la baza creării unui agent care se poate îmbunătăți singur și care poate crea experiențe mai bune pentru utilizatorii noștri.

În această lecție, vom analiza ce este memoria pentru Agenții AI și cum o putem gestiona și folosi în beneficiul aplicațiilor noastre.

## Introducere

Această lecție va acoperi:

• **Înțelegerea Memoriei Agenților AI**: Ce este memoria și de ce este esențială pentru agenți.

• **Implementarea și Stocarea Memoriei**: Metode practice pentru adăugarea capacităților de memorie agenților AI, concentrându-ne pe memoria pe termen scurt și pe termen lung.

• **Facerea Agenților AI să se Auto-Îmbunătățească**: Cum memoria permite agenților să învețe din interacțiunile anterioare și să se îmbunătățească în timp.

## Implementări Disponibile

Această lecție include două tutoriale cu notebook-uri cuprinzătoare:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementarea memoriei folosind Mem0 și Azure AI Search cu Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementarea memoriei structurate folosind Cognee, construind automat un grafic de cunoștințe susținut de embeddings, vizualizând graficul și efectuând recuperare inteligentă

## Obiective de Învățare

După ce finalizezi această lecție, vei ști cum să:

• **Diferențiezi între diferitele tipuri de memorie ale agenților AI**, inclusiv memoria de lucru, pe termen scurt și pe termen lung, precum și forme specializate precum memoria de persoană și episodică.

• **Implementezi și gestionezi memoria pe termen scurt și lung pentru agenții AI** folosind Microsoft Agent Framework, valorificând instrumente ca Mem0, Cognee, memoria Whiteboard și integrând cu Azure AI Search.

• **Înțelegi principiile din spatele agenților AI care se auto-îmbunătățesc** și cum sistemele robuste de gestionare a memoriei contribuie la învățarea și adaptarea continuă.

## Înțelegerea Memoriei Agenților AI

În esență, **memoria pentru agenții AI se referă la mecanismele care le permit să rețină și să-și amintească informații**. Aceste informații pot fi detalii specifice despre o conversație, preferințele utilizatorului, acțiuni anterioare sau chiar modele învățate.

Fără memorie, aplicațiile AI sunt adesea fără stare, ceea ce înseamnă că fiecare interacțiune începe de la zero. Aceasta duce la o experiență repetitivă și frustrantă în care agentul "uită" contextul sau preferințele anterioare.

### De ce este importantă memoria?

inteligența unui agent este profund legată de capacitatea lui de a-și aminti și utiliza informații din trecut. Memoria permite agenților să fie:

• **Reflectivi**: Învață din acțiunile și rezultatele anterioare.

• **Interactivi**: Mențin contextul pe parcursul unei conversații în derulare.

• **Proactivi și Reacționari**: Anticipează nevoile sau răspund adecvat bazându-se pe date istorice.

• **Autonomi**: Funcționează mai independent extrăgând cunoștințele stocate.

Scopul implementării memoriei este de a face agenții mai **de încredere și capabili**.

### Tipuri de Memorie

#### Memoria de Lucru

Gândește-te la aceasta ca la o foaie de hârtie pe care un agent o folosește în timpul unei singure sarcini sau procese de gândire. Ea reține informații imediate necesare pentru a calcula pasul următor.

Pentru agenții AI, memoria de lucru capturează adesea cele mai relevante informații dintr-o conversație, chiar dacă istoricul complet al chatului este lung sau trunchiat. Se concentrează pe extragerea elementelor cheie precum cerințele, propunerile, deciziile și acțiunile.

**Exemplu de Memorie de Lucru**

Într-un agent de rezervare călătorii, memoria de lucru ar putea captura cererea curentă a utilizatorului, cum ar fi "Vreau să rezerv o călătorie la Paris". Această cerință specifică este menținută în contextul imediat al agentului pentru a ghida interacțiunea actuală.

#### Memoria pe Termen Scurt

Acest tip de memorie reține informații pentru durata unei singure conversații sau sesiuni. Este contextul chatului curent, permițând agentului să se refere la ture anterioare din dialog.

În exemplele SDK Python [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), acest lucru corespunde `AgentSession`, creat cu `agent.create_session()`. Sesiunea este memoria pe termen scurt încorporată în framework: păstrează contextul conversației disponibil în timp ce aceeași sesiune este reutilizată, dar acel context nu este păstrat când sesiunea se încheie sau aplicația este repornită. Folosește memoria pe termen lung pentru fapte și preferințe care trebuie să supraviețuiască între sesiuni, de obicei printr-o bază de date, index vectorial sau alt spațiu persistent de stocare.

**Exemplu de Memorie pe Termen Scurt**

Dacă un utilizator întreabă „Cât costă un zbor către Paris?” și apoi continuă cu „Dar ce zici de cazare acolo?”, memoria pe termen scurt asigură că agentul știe că „acolo” se referă la „Paris” în aceeași conversație.

#### Memoria pe Termen Lung

Aceasta este informația care persistă peste mai multe conversații sau sesiuni. Permite agenților să-și amintească preferințele utilizatorilor, interacțiunile istorice sau cunoștințe generale pe perioade extinse. Este importantă pentru personalizare.

**Exemplu de Memorie pe Termen Lung**

O memorie pe termen lung ar putea stoca că „Ben se bucură de schi și activități în aer liber, îi place cafeaua cu vedere la munte și vrea să evite pârtiile avansate din cauza unei accidentări anterioare”. Aceste informații, învățate din interacțiuni anterioare, influențează recomandările în sesiunile viitoare de planificare a călătoriilor, făcându-le foarte personalizate.

#### Memoria de Persoană

Acest tip specializat de memorie ajută un agent să dezvolte o „personalitate” sau „persoană” consistentă. Permite agentului să își amintească detalii despre sine sau despre rolul său intenționat, făcând interacțiunile mai fluide și concentrate.

**Exemplu de Memorie de Persoană**
Dacă agentul de călătorii este proiectat să fie un „expert în planificarea schiului”, memoria de persoană ar putea consolida acest rol, influențând răspunsurile sale pentru a se alinia tonului și cunoștințelor unui expert.

#### Memoria de Flux de Lucru/Episodică

Această memorie stochează secvența de pași pe care un agent o parcurge în timpul unei sarcini complexe, inclusiv succese și eșecuri. Este ca și cum ar aminti „episoade” sau experiențe anterioare pentru a învăța din ele.

**Exemplu de Memorie Episodică**

Dacă agentul a încercat să rezerve un zbor specific dar a eșuat din cauza indisponibilității, memoria episodică poate înregistra acest eșec, permițând agentului să încerce zboruri alternative sau să informeze utilizatorul despre problemă într-un mod mai informat la o încercare ulterioară.

#### Memoria pentru Entități

Aceasta implică extragerea și memorarea entităților specifice (cum ar fi persoane, locuri sau obiecte) și a evenimentelor din conversații. Permite agentului să construiască o înțelegere structurată a elementelor cheie discutate.

**Exemplu de Memorie pentru Entități**

Dintr-o conversație despre o călătorie trecută, agentul ar putea extrage „Paris,” „Turnul Eiffel” și „cina la restaurantul Le Chat Noir” ca entități. Într-o interacțiune viitoare, agentul ar putea să-și amintească „Le Chat Noir” și să ofere să facă o nouă rezervare acolo.

#### RAG Structurat (Retrieval Augmented Generation)

Deși RAG este o tehnică mai largă, „RAG Structurat” este evidențiată ca o tehnologie puternică de memorie. Extrage informații dense și structurate din diverse surse (conversații, emailuri, imagini) și le folosește pentru a îmbunătăți precizia, recuperarea și rapiditatea răspunsurilor. Spre deosebire de RAG clasic care se bazează doar pe similaritatea semantică, RAG Structurat lucrează cu structura inerentă a informației.

**Exemplu RAG Structurat**

În loc să se bazeze doar pe potrivirea cuvinte-cheie, RAG Structurat ar putea analiza detaliile unui zbor (destinație, dată, oră, companie aeriană) dintr-un email și să le stocheze într-un mod structurat. Acest lucru permite interogări precise cum ar fi „Ce zbor am rezervat către Paris marți?”

## Implementarea și Stocarea Memoriei

Implementarea memoriei pentru agenții AI implică un proces sistematic de **management al memoriei**, care include generarea, stocarea, recuperarea, integrarea, actualizarea și chiar „uitarea” (sau ștergerea) informațiilor. Recuperarea este un aspect deosebit de crucial.

### Instrumente Specializate pentru Memorie

#### Mem0

O modalitate de a stoca și gestiona memoria agentului este folosirea unor instrumente specializate precum Mem0. Mem0 funcționează ca un strat de memorie persistentă, permițând agenților să-și amintească interacțiunile relevante, să stocheze preferințele utilizatorilor și contextul factual și să învețe din succese și eșecuri în timp. Ideea aici este că agenții fără stare devin agenți cu stare.

Funcționează printr-un **pipeline de memorie în două faze: extracție și actualizare**. Mai întâi, mesajele adăugate în firul agentului sunt trimise la serviciul Mem0, care folosește un Model de Limbaj Mare (LLM) pentru a rezuma istoricul conversației și a extrage amintiri noi. Ulterior, o fază de actualizare condusă de LLM determină dacă aceste amintiri trebuie adăugate, modificate sau șterse, stocându-le într-un magazin de date hibrid ce poate include baze vectoriale, pe graf și cheie-valoare. Acest sistem suportă și diverse tipuri de memorie și poate incorpora memoria grafică pentru gestionarea relațiilor dintre entități.

#### Cognee

O altă abordare puternică este folosirea **Cognee**, o memorie semantică open-source pentru agenții AI care transformă datele structurate și nestructurate în grafuri de cunoștințe interogabile susținute de embeddings. Cognee oferă o **arhitectură dual-store** care combină căutarea prin similaritate vectorială cu relațiile grafice, permițând agenților să înțeleagă nu doar ce informație este similară, ci și cum conceptele se raportează unele la altele.

Excelează la o **recuperare hibridă** care îmbină similaritatea vectorială, structura graficului și raționamentul LLM - de la căutarea prin bucăți brute la răspunsuri la întrebări conștiente de grafic. Sistemul menține o **memorie vie** care evoluează și crește în timp ce rămâne interogabilă ca un grafic conex, suportând atât contextul sesiunii pe termen scurt cât și memoria persistentă pe termen lung.

Tutorialul notebook Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrează construirea acestui strat unificat de memorie, cu exemple practice de ingestie a surselor de date diverse, vizualizarea graficului de cunoștințe și interogarea cu diferite strategii de căutare adaptate nevoilor specifice ale agenților.

### Stocarea Memoriei cu RAG

Dincolo de instrumentele specializate de memorie precum Mem0, poți valorifica servicii robuste de căutare precum **Azure AI Search ca backend pentru stocarea și recuperarea amintirilor**, în special pentru RAG structurat.

Acest lucru îți permite să fundamentezi răspunsurile agentului tău cu propriile date, asigurând răspunsuri mai relevante și precise. Azure AI Search poate fi folosit pentru a stoca amintiri specifice utilizatorului legate de călătorii, cataloage de produse sau orice altă cunoaștere domenială.

Azure AI Search suportă capabilități precum **RAG Structurat**, care excelează la extragerea și recuperarea de informații dense, structurate din seturi mari de date precum istoricul conversațiilor, emailuri sau chiar imagini. Aceasta oferă „precizie și rechemare supraumană” comparativ cu abordările tradiționale de împărțire pe bucăți și embedding de text.

## Facerea Agenților AI să se Auto-Îmbunătățească

Un tipar comun pentru agenții care se auto-îmbunătățesc implică introducerea unui **„agent de cunoștințe”**. Acest agent separat observează conversația principală dintre utilizator și agentul principal. Rolul său este să:

1. **Identifice informații valoroase**: Determină dacă vreo parte a conversației merită salvată ca cunoștință generală sau preferință specifică utilizatorului.

2. **Extrage și rezumă**: Distilează învățătura esențială sau preferința din conversație.

3. **Stochează în baza de cunoștințe**: Păstrează aceste informații extrase, de obicei într-o bază de date vectorială, pentru a putea fi recuperate ulterior.

4. **Completează interogările viitoare**: Când utilizatorul inițiază o nouă interogare, agentul de cunoștințe recuperează informațiile relevante stocate și le atașează la promptul utilizatorului, oferind context crucial agentului principal (similar cu RAG).

### Optimizări pentru Memorie

• **Managementul latenței**: Pentru a evita încetinirea interacțiunilor utilizatorului, un model mai ieftin și mai rapid poate fi folosit inițial pentru a verifica rapid dacă informațiile merită stocate sau recuperate, invocând procesul mai complex de extracție/recuperare doar când este necesar.

• **Întreținerea bazei de cunoștințe**: Pentru o bază de cunoștințe în creștere, informațiile folositoare mai rar pot fi mutate în „stocare rece” pentru a gestiona costurile.

## Ai Mai Multe Întrebări Despre Memoria Agenților?

Alătură-te [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la sesiuni de birou și a obține răspunsuri la întrebările tale despre Agenții AI.
## Lecția Anterioară

[Ingineria Contextului pentru Agenții AI](../12-context-engineering/README.md)

## Lecția Următoare

[Explorarea Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->