# Ingineria Contextului pentru Agenți AI

[![Ingineria Contextului](../../../translated_images/ro/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

Înțelegerea complexității aplicației pentru care dezvoltați un agent AI este importantă pentru a crea unul fiabil. Trebuie să construim Agenți AI care să gestioneze eficient informațiile pentru a răspunde nevoilor complexe dincolo de ingineria prompturilor.

În această lecție, vom analiza ce este ingineria contextului și rolul său în construirea agenților AI.

## Introducere

Această lecție va acoperi:

• **Ce este Ingineria Contextului** și de ce este diferită de ingineria prompturilor.

• **Strategii pentru Ingineria Contextului eficientă**, inclusiv cum să scrieți, selectați, comprimați și izolați informațiile.

• **Eșecuri comune ale contextului** care pot deraia agentul AI și cum să le remediați.

## Obiective de învățare

După finalizarea acestei lecții, veți înțelege cum să:

• **Definiți ingineria contextului** și să o diferențiați de ingineria prompturilor.

• **Identificați componentele cheie ale contextului** în aplicațiile bazate pe modele lingvistice mari (LLM).

• **Aplicați strategii pentru scrierea, selectarea, comprimarea și izolarea contextului** pentru a îmbunătăți performanța agenților.

• **Recunoașteți eșecurile comune ale contextului** precum intoxicarea, distragerea, confuzia și conflictul și să implementați tehnici de atenuare.

## Ce este Ingineria Contextului?

Pentru Agenții AI, contextul este ceea ce determină planificarea agentului AI pentru a întreprinde anumite acțiuni. Ingineria contextului este practica de a asigura că agentul AI are informațiile corecte pentru a finaliza următorul pas al sarcinii. Fereastra de context este limitată ca dimensiune, așadar, ca dezvoltatori de agenți, trebuie să construim sisteme și procese pentru a gestiona adăugarea, eliminarea și condensarea informațiilor din fereastra de context.

### Ingineria prompturilor vs Ingineria contextului

Ingineria prompturilor se concentrează pe un set unic de instrucțiuni statice pentru a ghida eficient agenții AI cu un set de reguli. Ingineria contextului este despre modul de gestionare a unui set dinamic de informații, inclusiv promptul inițial, pentru a asigura că agentul AI are ce îi trebuie în timp. Ideea principală privind ingineria contextului este de a face acest proces repetabil și fiabil.

### Tipuri de context

[![Tipuri de Context](../../../translated_images/ro/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Este important să reținem că contextul nu este un singur lucru. Informațiile de care agentul AI are nevoie pot proveni din diferite surse și este responsabilitatea noastră să asigurăm accesul agentului la aceste surse:

Tipurile de context pe care un agent AI trebuie să le gestioneze includ:

• **Instrucțiuni:** Acestea sunt ca „regulile” agentului – prompturi, mesaje de sistem, exemple few-shot (arată AI cum să facă ceva) și descrieri ale instrumentelor pe care le poate folosi. Aceasta este zona unde se combină ingineria prompturilor cu ingineria contextului.

• **Cunoștințe:** Acestea acoperă fapte, informații preluate din baze de date sau amintiri pe termen lung acumulate de agent. Aceasta include integrarea unui sistem Retrieval Augmented Generation (RAG) dacă un agent are nevoie de acces la diverse depozite de cunoștințe și baze de date.

• **Instrumente:** Acestea sunt definițiile funcțiilor externe, API-urilor și serverelor MCP pe care agentul le poate apela, împreună cu feedback-ul (rezultatele) obținute din folosirea lor.

• **Istoricul conversației:** Dialogul continuu cu un utilizator. Pe măsură ce timpul trece, aceste conversații devin mai lungi și mai complexe, ceea ce înseamnă că ocupă spațiu în fereastra de context.

• **Preferințele utilizatorului:** Informații învățate despre preferințele sau antipatiile unui utilizator de-a lungul timpului. Acestea ar putea fi stocate și accesate la luarea deciziilor importante pentru a ajuta utilizatorul.

## Strategii pentru Ingineria Contextului Eficientă

### Strategii de planificare

[![Cele mai bune practici pentru Ingineria Contextului](../../../translated_images/ro/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

O inginerie a contextului bună începe cu o planificare bună. Iată o abordare care vă va ajuta să începeți să gândiți modul de aplicare a conceptului de inginerie a contextului:

1. **Definiți Rezultate Clare** - Rezultatele sarcinilor pe care Agenții AI le vor primi trebuie definite clar. Răspundeți la întrebarea - „Cum va arăta lumea când agentul AI își va fi terminat sarcina?” Cu alte cuvinte, ce schimbare, informație sau răspuns ar trebui să primească utilizatorul după interacțiunea cu agentul AI.
2. **Cartografiați Contextul** - Odată ce ați definit rezultatele agentului AI, trebuie să răspundeți întrebării „De ce informații are nevoie agentul AI pentru a finaliza această sarcină?”. Astfel puteți începe să cartografiați contextul unde acele informații pot fi găsite.
3. **Creați conducte de context** - Acum că știți unde este informația, trebuie să răspundeți întrebării „Cum va obține agentul aceste informații?”. Aceasta se poate face în diverse moduri, inclusiv RAG, utilizarea serverelor MCP și alte unelte.

### Strategii practice

Planificarea este importantă, dar odată ce informațiile încep să curgă în fereastra de context a agentului nostru, trebuie să avem strategii practice pentru a le gestiona:

#### Gestionarea Contextului

Deși unele informații vor fi adăugate automat în fereastra de context, ingineria contextului presupune să preluăm un rol mai activ în gestionarea acestor informații, ceea ce se poate face prin câteva strategii:

 1. **Carnetul agentului**
 Aceasta permite unui agent AI să ia notițe despre informațiile relevante legate de sarcinile curente și interacțiunile cu utilizatorul în cadrul unei singure sesiuni. Acesta ar trebui să existe în afara ferestrei de context, într-un fișier sau obiect de runtime pe care agentul îl poate accesa ulterior în cadrul acestei sesiuni dacă este necesar.

 2. **Amintiri**
 Carnetele sunt bune pentru gestionarea informațiilor în afara ferestrei de context a unei singure sesiuni. Amintirile permit agenților să stocheze și să recupereze informații relevante pe mai multe sesiuni. Aceasta poate include rezumate, preferințe ale utilizatorului și feedback pentru îmbunătățiri viitoare.

 3. **Comprimarea Contextului**
  Odată ce fereastra de context crește și se apropie de limită, se pot folosi tehnici precum rezumarea și tăierea. Aceasta include păstrarea doar a informațiilor cele mai relevante sau eliminarea mesajelor mai vechi.
  
 4. **Sisteme multi-agent**
  Dezvoltarea unui sistem multi-agent este o formă de inginerie a contextului deoarece fiecare agent are propria fereastră de context. Modul în care acest context este partajat și transmis diferiților agenți este altceva ce trebuie planificat când se construiesc aceste sisteme.
  
 5. **Mediile sandbox**
  Dacă un agent trebuie să ruleze cod sau să proceseze cantități mari de informații într-un document, acest lucru poate consuma multe tokenuri pentru procesarea rezultatelor. În loc să fie toate stocate în fereastra de context, agentul poate folosi un mediu sandbox capabil să ruleze acest cod și să citească doar rezultatele și alte informații relevante.
  
 6. **Obiecte de stare de runtime**
   Acest lucru se realizează prin crearea de containere de informații pentru a gestiona situații când agentul trebuie să aibă acces la anumite informații. Pentru o sarcină complexă, acest lucru ar permite agentului să stocheze rezultatele fiecărui subtask pas cu pas, permițând ca contextul să rămână conectat doar la acel subtask specific.

#### Inspectarea Contextului

După aplicarea uneia dintre aceste strategii, merită să verificați ce a primit cu adevărat următorul apel al modelului. O întrebare utilă pentru depanare este:

> Agentul a încărcat prea mult context, context greșit sau a ratat contextul de care avea nevoie?

Nu aveți nevoie să înregistrați prompturile brute, rezultatele uneltelor sau conținutul memoriei pentru a răspunde la această întrebare. În producție, folosiți înregistrări mici de inspectare a contextului care surprind numere, ID-uri, hash-uri și etichete de politică:

- **Selecție:** Urmăriți câte bucăți candidate, unelte sau amintiri au fost luate în considerare, câte au fost selectate și care regulă sau scor a cauzat filtrarea celorlalte.
- **Compresie:** Înregistrați intervalul sursă sau ID-ul de trasabilitate, ID-ul rezumatului, un număr estimat de tokenuri înainte și după compresie, și dacă conținutul original a fost exclus din următorul apel.
- **Izolare:** notați care subtask a rulat într-un agent, sesiune sau sandbox separat, ce rezumat limitat a fost returnat și dacă rezultatul mare al uneltelor a rămas în afara contextului agentului părinte.
- **Memorie și RAG:** păstrați ID-urile documentelor de recuperare, ID-uri de memorie, scoruri, ID-uri selectate și starea de redactare în loc de textul complet recuperat.
- **Siguranță și confidențialitate:** preferați hash-uri, ID-uri, token buckets și etichete de politică în loc de text sensibil din prompturi, argumente ale uneltelor, rezultate ale uneltelor sau conținuturi ale memoriei utilizatorului.

Scopul nu este să păstrați mai mult context. Este să lăsați suficiente dovezi pentru ca un dezvoltator să poată spune ce strategie de context a rulat și dacă aceasta a modificat următorul apel al modelului în modul intenționat.

### Exemplu de Inginerie a Contextului

Să spunem că vrem ca un agent AI să **„să-mi rezerve o excursie la Paris.”**

• Un agent simplu care folosește doar ingineria prompturilor ar putea răspunde simplu: **„Ok, când ai vrea să mergi la Paris?**”. A procesat doar întrebarea ta directă în momentul în care utilizatorul a întrebat.

• Un agent care utilizează strategiile de inginerie a contextului acoperite ar face mult mai multe. Înainte de a răspunde, sistemul său ar putea:

  ◦ **Verifica calendarul tău** pentru date disponibile (recuperând date în timp real).

 ◦ **Reaminti preferințele tale pentru călătorii** (din memoria pe termen lung) precum compania aeriană preferată, bugetul sau dacă preferi zboruri directe.

 ◦ **Identifica uneltele disponibile** pentru rezervarea de zboruri și hoteluri.

- Apoi, un răspuns exemplu ar putea fi: „Salut [Numele Tău]! Văd că ești liber în prima săptămână a lunii octombrie. Să caut zboruri directe către Paris cu [Compania Preferată], în limita bugetului tău obișnuit de [Buget]?“. Acest răspuns mai bogat și conștient de context demonstrează puterea ingineriei contextului.

## Eșecuri Comune ale Contextului

### Intoxicarea Contextului

**Ce este:** Când o halucinație (informație falsă generată de LLM) sau o eroare pătrunde în context și este referențiată repetat, determinând agentul să urmărească scopuri imposibile sau să dezvolte strategii absurde.

**Ce să faci:** Implementați **validarea contextului** și **carantină**. Validați informația înainte de a o adăuga în memoria pe termen lung. Dacă se detectează o posibilă intoxicare, începeți fire noi de context pentru a preveni răspândirea informației eronate.

**Exemplu rezervare călătorie:** Agentul tău halucinează un **zbor direct de la un aeroport local mic către un oraș internațional îndepărtat**, care de fapt nu oferă zboruri internaționale. Această detaliere inexistentă a zborului este salvată în context. Mai târziu, când îi ceri agentului să facă rezervarea, acesta continuă să caute bilete pentru această rută imposibilă, ducând la erori repetate.

**Soluție:** Implementați un pas care **validează existența zborului și rutele cu o API în timp real** _înainte_ de a adăuga detaliul zborului în contextul de lucru al agentului. Dacă validarea eșuează, informația eronată este „carantinită” și nu este folosită mai departe.

### Distragerea Contextului

**Ce este:** Când contextul devine atât de mare încât modelul se concentrează prea mult pe istoricul acumulat în loc să folosească ceea ce a învățat în timpul antrenamentului, ducând la acțiuni repetitive sau nefolositoare. Modelele pot începe să facă greșeli chiar înainte ca fereastra de context să fie plină.

**Ce să faci:** Folosește **rezumarea contextului**. Periodic, comprimă informațiile acumulate în rezumate mai scurte, păstrând detaliile importante și eliminând istoricul redundant. Acest lucru ajută la „resetarea” focalizării.

**Exemplu rezervare călătorie:** Ai discutat mult timp despre diverse destinații de vis, inclusiv o relatare detaliată a traseului tău cu rucsacul acum doi ani. Când în sfârșit ceri să **„găsești un zbor ieftin pentru luna viitoare,”** agentul este copleșit de detaliile vechi, irelevante și continuă să întrebe despre echipamentul tău de backpacking sau itinerarii vechi, neglijând cererea curentă.

**Soluție:** După un anumit număr de schimburi sau când contextul devine prea mare, agentul ar trebui să **rezume cele mai recente și relevante părți ale conversației** – concentrându-se pe datele și destinația actuală – și să folosească acest rezumat condensat pentru următorul apel LLM, eliminând istoricul chatului mai puțin relevant.

### Confuzia Contextului

**Ce este:** Când contextul inutil, adesea sub forma unui număr prea mare de unelte disponibile, cauzează generarea unor răspunsuri proaste sau apelarea unor unelte irelevante. Modelele mai mici sunt în special predispuse la acest lucru.

**Ce să faci:** Implementați **gestionarea încărcării uneltelor** folosind tehnici RAG. Stocați descrierile uneltelor într-o bază de date vectorială și selectați _numai_ cele mai relevante unelte pentru fiecare sarcină specifică. Cercetările arată că este indicat să limitați selecțiile la mai puțin de 30 de unelte.

**Exemplu rezervare călătorie:** Agentul tău are acces la zeci de unelte: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` etc. Întrebi, **„Care este cel mai bun mod de a mă deplasa prin Paris?”** Din cauza numărului mare de unelte, agentul se confuzează și încearcă să apeleze `book_flight` _în interiorul_ Parisului, sau `rent_car` deși preferi transportul public, pentru că descrierile uneltelor se pot suprapune sau agentul pur și simplu nu poate determina care este cea mai bună unealtă.

**Soluție:** Folosește **RAG peste descrierile uneltelor**. Când întrebi despre deplasarea prin Paris, sistemul recuperează dinamic _doar_ uneltele cele mai relevante precum `rent_car` sau `public_transport_info` bazate pe întrebarea ta, oferind un set concentrat de unelte pentru LLM.

### Conflictul Contextului

**Ce este:** Când există informații contradictorii în context, ceea ce duce la raționamente inconsistente sau răspunsuri finale proaste. Acest lucru se întâmplă adesea când informațiile vin în etape, iar presupunerile incorecte timpurii rămân în context.

**Ce să faci:** Folosește **înlăturarea informațiilor inutile (pruning)** și **descărcarea contextului (offloading)**. Pruning înseamnă eliminarea informațiilor vechi sau contradictorii pe măsură ce apar detalii noi. Offloading oferă modelului un spațiu de lucru „scratchpad” separat pentru a procesa informațiile fără a încărca contextul principal.


**Exemplu de rezervare călătorie:** Inițial îi spui agentului tău, **„Vreau să zbor la clasa economică.”** Mai târziu în conversație, te răzgândești și spui, **„De fapt, pentru această călătorie, să mergem la clasa business.”** Dacă ambele instrucțiuni rămân în context, agentul ar putea primi rezultate de căutare contradictorii sau să se confunde asupra preferinței care trebuie prioritizată.

**Soluție:** Implementează **tăierea contextului**. Când o instrucțiune nouă contrazice una veche, instrucțiunea mai veche este eliminată sau explicit înlocuită în context. Alternativ, agentul poate folosi un **notepad** pentru a reconcilia preferințele contradictorii înainte de a decide, asigurându-se că doar instrucțiunea finală și coerentă îi ghidează acțiunile.

## Ai Mai Multe Întrebări Despre Ingineria Contextului?

Alătură-te [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la ore de consultanță și a-ți rezolva întrebările despre Agenti AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->