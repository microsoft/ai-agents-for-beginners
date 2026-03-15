# Memoria pentru Agenții AI 
[![Agent Memory](../../../translated_images/ro/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Când discutăm despre beneficiile unice ale creării de Agenți AI, se discută în principal două lucruri: capacitatea de a apela instrumente pentru a îndeplini sarcini și capacitatea de a se îmbunătăți în timp. Memoria este la baza creării unui agent auto-îmbunătățitor care poate crea experiențe mai bune pentru utilizatorii noștri.

În această lecție, vom vedea ce este memoria pentru Agenții AI și cum o putem gestiona și folosi în beneficiul aplicațiilor noastre.

## Introducere

Această lecție va acoperi:

• **Înțelegerea Memoriei Agenților AI**: Ce este memoria și de ce este esențială pentru agenți.

• **Implementarea și Stocarea Memoriei**: Metode practice pentru adăugarea capacităților de memorie agenților AI, concentrându-se pe memoria pe termen scurt și pe termen lung.

• **Facerea Agenților AI Auto-Îmbunătățitori**: Cum memoria permite agenților să învețe din interacțiunile anterioare și să se îmbunătățească în timp.

## Implementări Disponibile

Această lecție include două tutoriale complete în notebook-uri:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementează memoria folosind Mem0 și Azure AI Search cu Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementează memoria structurată folosind Cognee, construind automat un grafic de cunoștințe susținut de embeddings, vizualizând graficul și realizând recuperare inteligentă

## Obiective de Învățare

După finalizarea acestei lecții, vei ști să:

• **Diferențiezi între diverse tipuri de memorie ale agenților AI**, inclusiv memoria de lucru, pe termen scurt și pe termen lung, precum și forme specializate precum memoria persona și episodică.

• **Implementezi și gestionezi memoria pe termen scurt și pe termen lung pentru agenții AI** folosind Microsoft Agent Framework, utilizând instrumente precum Mem0, Cognee, memoria Whiteboard și integrând cu Azure AI Search.

• **Înțelegi principiile din spatele agenților AI auto-îmbunătățitori** și cum sistemele robuste de gestionare a memoriei contribuie la învățarea și adaptarea continuă.

## Înțelegerea Memoriei Agenților AI

În esență, **memoria pentru agenții AI se referă la mecanismele care le permit să rețină și să reamintească informații**. Această informație poate fi detalii specifice despre o conversație, preferințele utilizatorului, acțiuni anterioare sau chiar tipare învățate.

Fără memorie, aplicațiile AI sunt adesea fără stare (stateless), ceea ce înseamnă că fiecare interacțiune începe de la zero. Aceasta conduce la o experiență repetitivă și frustrantă pentru utilizator, unde agentul „uită” contextul sau preferințele anterioare.

### De ce este Memoria Importantă?

Inteligența unui agent este profund legată de capacitatea sa de a reaminti și utiliza informații din trecut. Memoria permite agenților să fie:

• **Reflectivi**: Să învețe din acțiunile și rezultatele anterioare.

• **Interactivi**: Să mențină contextul pe durata unei conversații în curs.

• **Proactivi și Reacționari**: Să anticipeze nevoile sau să răspundă adecvat bazându-se pe date istorice.

• **Autonomi**: Să opereze mai independent, bazându-se pe cunoștințele stocate.

Scopul implementării memoriei este de a face agenții mai **de încredere și capabili**.

### Tipuri de Memorie

#### Memorie de Lucru

Gândește-te la aceasta ca la o bucată de hârtie de urgență pe care un agent o folosește în timpul unei singure sarcini sau proces de gândire în desfășurare. Ea reține informațiile imediate necesare pentru calcularea următorului pas.

Pentru agenții AI, memoria de lucru captează adesea cele mai relevante informații dintr-o conversație, chiar dacă întreg istoricul chatului este lung sau trunchiat. Se concentrează pe extragerea elementelor cheie precum cerințe, propuneri, decizii și acțiuni.

**Exemplu de Memorie de Lucru**

Într-un agent de rezervare de călătorii, memoria de lucru ar putea reține cererea curentă a utilizatorului, cum ar fi „Vreau să rezerv o călătorie la Paris”. Această cerință specifică este ținută în contextul imediat al agentului pentru a ghida interacțiunea actuală.

#### Memorie pe Termen Scurt

Acest tip de memorie reține informații pentru durata unei singure conversații sau sesiuni. Este contextul chatului curent, permițând agentului să se refere la turele anterioare din dialog.

**Exemplu de Memorie pe Termen Scurt**

Dacă un utilizator întreabă „Cât costă un zbor spre Paris?” și apoi continuă cu „Dar cazarea acolo?”, memoria pe termen scurt asigură că agentul știe că „acolo” se referă la „Paris” în aceeași conversație.

#### Memorie pe Termen Lung

Aceasta este informația care persistă de-a lungul mai multor conversații sau sesiuni. Permite agenților să-și amintească preferințele utilizatorului, interacțiunile istorice sau cunoștințele generale pe perioade extinse. Este importantă pentru personalizare.

**Exemplu de Memorie pe Termen Lung**

O memorie pe termen lung ar putea stoca că „Ben se bucură de schi și activități în aer liber, îi place cafeaua cu vedere la munte și dorește să evite pârtiile avansate din cauza unei accidentări trecute”. Această informație, învățată din interacțiunile anterioare, influențează recomandările în sesiunile viitoare de planificare a călătoriilor, făcându-le foarte personalizate.

#### Memorie Persona

Acest tip specializat de memorie ajută agentul să dezvolte o „personalitate” sau o „persoană” consistentă. Permite agentului să rețină detalii despre sine sau rolul său intenționat, făcând interacțiunile mai fluide și concentrate.

**Exemplu Memorie Persona**

Dacă agentul de călătorie este proiectat să fie un „expert în planificarea schiatului”, memoria persona ar putea întări acest rol, influențând răspunsurile să se alinieze cu tonul și cunoștințele unui expert.

#### Memorie Workflow/Episodică

Această memorie păstrează secvența de pași pe care agentul îi parcurge în timpul unei sarcini complexe, inclusiv succesele și eșecurile. Este ca și cum ar memora „episoade” sau experiențe trecute pentru a învăța din ele.

**Exemplu de Memorie Episodică**

Dacă agentul a încercat să rezerve un zbor specific, dar a eșuat din cauza indisponibilității, memoria episodică poate înregistra acest eșec, permițând agentului să încerce zboruri alternative sau să informeze utilizatorul despre problemă într-un mod mai informat la o încercare ulterioară.

#### Memorie Entitate

Aceasta implică extragerea și memorarea entităților specifice (precum persoane, locuri sau obiecte) și a evenimentelor din conversații. Permite agentului să construiască o înțelegere structurată a elementelor cheie discutate.

**Exemplu de Memorie Entitate**

Dintr-o conversație despre o călătorie anterioară, agentul ar putea extrage „Paris”, „Turnul Eiffel” și „cina la restaurantul Le Chat Noir” ca entități. Într-o interacțiune viitoare, agentul ar putea să-și amintească „Le Chat Noir” și să ofere să facă o nouă rezervare acolo.

#### RAG Structurat (Retrieval Augmented Generation)

Deși RAG este o tehnică mai largă, „Structured RAG” este evidențiată ca o tehnologie puternică de memorie. Ea extrage informații dense, structurate din diverse surse (conversații, emailuri, imagini) și le folosește pentru a îmbunătăți precizia, recuperarea și viteza răspunsurilor. Spre deosebire de RAG clasic, care se bazează doar pe similaritatea semantică, Structured RAG funcționează cu structura inerentă a informației.

**Exemplu Structured RAG**

În loc să potrivească doar cuvinte-cheie, Structured RAG ar putea analiza detaliile unui zbor (destinație, dată, oră, companie aeriană) dintr-un email și să le stocheze într-un mod structurat. Acest lucru permite interogări precise de genul „Ce zbor am rezervat spre Paris marți?”

## Implementarea și Stocarea Memoriei

Implementarea memoriei pentru agenții AI implică un proces sistematic de **gestionare a memoriei**, care include generarea, stocarea, recuperarea, integrarea, actualizarea și chiar „uitarea” (sau ștergerea) informațiilor. Recuperarea este un aspect deosebit de crucial.

### Instrumente Specializate pentru Memorie

#### Mem0

Un mod de a stoca și gestiona memoria agentului este folosirea unor instrumente specializate precum Mem0. Mem0 funcționează ca un strat persistent de memorie, permițând agenților să reamintească interacțiuni relevante, să stocheze preferințele utilizatorilor și contextul factual, și să învețe din succese și eșecuri în timp. Ideea este ca agenții fără stare să devină agenți cu stare.

Funcționează printr-un **proces în două faze: extragerea și actualizarea memoriei**. Mai întâi, mesajele adăugate la firul agentului sunt trimise serviciului Mem0, care folosește un Model de Limbaj Mare (LLM) pentru a rezuma istoricul conversației și a extrage noi amintiri. Ulterior, o fază de actualizare condusă de LLM determină dacă să adauge, modifice sau șteargă aceste memorii, stocându-le într-un depozit de date hibrid care poate include baze vectoriale, de graf și key-value. Sistemul suportă de asemenea diverse tipuri de memorie și poate încorpora memoria grafică pentru gestionarea relațiilor dintre entități.

#### Cognee

O altă abordare puternică este folosirea **Cognee**, o memorie semantică open-source pentru agenții AI care transformă date structurate și nestructurate în grafuri de cunoștințe interogabile susținute de embeddings. Cognee oferă o **arhitectură duală** combinând căutarea pe baza similitudinii vectoriale cu relațiile grafice, permițând agenților să înțeleagă nu doar ce informații sunt similare, ci și cum se relaționează conceptele între ele.

Se remarcă prin **recuperarea hibridă** care îmbină similitudinea vectorială, structura grafică și raționamentul LLM - de la căutarea simplă a fragmentelor până la întrebări conștiente de grafic. Sistemul menține o **memorie vie** care evoluează și crește, rămânând interogabilă ca un graf conectat, suportând atât contextul pe termen scurt al sesiunii, cât și memoria persistentă pe termen lung.

Tutorialul Cognee în notebook ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrează construirea acestui strat unificat de memorie, cu exemple practice de ingestie a surselor diverse de date, vizualizarea graficului de cunoștințe și interogarea cu diferite strategii de căutare adaptate nevoilor specifice ale agenților.

### Stocarea Memoriei cu RAG

Dincolo de instrumentele specializate precum mem0, poți utiliza servicii robuste de căutare precum **Azure AI Search ca backend pentru stocarea și recuperarea memoriilor**, în special pentru RAG structurat.

Aceasta îți permite să ancorezi răspunsurile agentului în propriile tale date, asigurând răspunsuri mai relevante și precise. Azure AI Search poate fi folosit pentru a stoca amintirile de călătorie specifice utilizatorului, cataloage de produse sau orice altă cunoaștere specifică domeniului.

Azure AI Search suportă capacități precum **Structured RAG**, care excelează în extragerea și recuperarea informațiilor dense, structurate din seturi mari de date precum istoricul conversațiilor, emailuri sau chiar imagini. Aceasta oferă „precizie și recuperare superioare omului” comparativ cu abordările tradiționale de segmentare text și embeddings.

## Facerea Agenților AI să se Auto-Îmbunătățească

Un tipar comun pentru agenții auto-îmbunătățitori implică introducerea unui **„agent de cunoaștere”**. Acest agent separat observă conversația principală dintre utilizator și agentul principal. Rolul său este să:

1. **Identifice informațiile valoroase**: Să stabilească dacă vreun segment al conversației merită salvat ca cunoaștere generală sau preferință specifică a utilizatorului.

2. **Extraga și rezume**: Să distileze învățătura sau preferința esențială din conversație.

3. **Stocheze într-o bază de cunoștințe**: Să păstreze această informație extrasă, adesea într-o bază de date vectorială, pentru a putea fi recuperată ulterior.

4. **Completeze interogările viitoare**: Când utilizatorul inițiază o nouă interogare, agentul de cunoaștere recuperează informațiile relevante stocate și le atașează promptului utilizatorului, oferind context esențial agentului principal (asemănător RAG).

### Optimizări pentru Memorie

• **Gestionarea latenței**: Pentru a evita încetinirea interacțiunilor cu utilizatorul, se poate folosi inițial un model mai ieftin și mai rapid pentru a verifica dacă informația merită stocată sau recuperată, apelând procesul mai complex de extragere/recuperare doar când este necesar.

• **Mentenanța bazei de cunoștințe**: Pentru o bază de cunoștințe în creștere, informațiile folosite mai rar pot fi mutate în „cold storage” pentru a gestiona costurile.

## Ai mai multe întrebări despre Memoria Agenților?

Alătură-te [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la ore de birou și a primi răspunsuri la întrebările tale despre Agenții AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să țineți cont că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->