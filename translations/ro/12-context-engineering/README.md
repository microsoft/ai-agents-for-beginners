# Ingineria Contextului pentru Agenții AI

[![Context Engineering](../../../translated_images/ro/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

Înțelegerea complexității aplicației pentru care construiți un agent AI este importantă pentru a crea unul de încredere. Trebuie să construim Agenți AI care gestionează eficient informațiile pentru a răspunde nevoilor complexe dincolo de ingineria promptului.

În această lecție, vom analiza ce este ingineria contextului și rolul său în construirea agenților AI.

## Introducere

Această lecție va acoperi:

• **Ce este Ingineria Contextului** și de ce este diferită de ingineria promptului.

• **Strategii pentru o inginerie eficientă a contextului**, inclusiv cum să scrieți, selectați, comprimați și izolați informațiile.

• **Eșecuri comune ale contextului** care pot deraia agentul AI și cum să le remediați.

## Obiectivele de Învățare

După finalizarea acestei lecții, veți înțelege cum să:

• **Definiți ingineria contextului** și să o diferențiați de ingineria promptului.

• **Identificați componentele cheie ale contextului** în aplicațiile bazate pe Modele Mari de Limbaj (LLM).

• **Aplicați strategii pentru scrierea, selectarea, comprimarea și izolarea contextului** pentru a îmbunătăți performanța agentului.

• **Recunoașteți eșecurile comune ale contextului** cum ar fi intoxicarea, distragerea, confuzia și conflictul, și să implementați tehnici de atenuare.

## Ce este Ingineria Contextului?

Pentru Agenții AI, contextul este ceea ce determină planificarea unui agent AI pentru a întreprinde anumite acțiuni. Ingineria contextului este practica de a asigura că agentul AI are informațiile corecte pentru a finaliza pasul următor al sarcinii. Fereastra de context este limitată ca dimensiune, așa că, în calitate de dezvoltatori de agenți, trebuie să construim sisteme și procese pentru a gestiona adăugarea, eliminarea și condensarea informațiilor din fereastra de context.

### Ingineria Promptului vs Ingineria Contextului

Ingineria promptului se concentrează pe un set unic de instrucțiuni statice pentru a ghida eficient agenții AI cu un set de reguli. Ingineria contextului este modul de a gestiona un set dinamic de informații, inclusiv promptul inițial, pentru a asigura că agentul AI are ceea ce îi trebuie pe parcursul timpului. Ideea principală din jurul ingineriei contextului este de a face acest proces repetabil și de încredere.

### Tipuri de Context

[![Types of Context](../../../translated_images/ro/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Este important să ne amintim că contextul nu este un lucru singular. Informațiile de care agentul AI are nevoie pot proveni dintr-o varietate de surse diferite și depinde de noi să ne asigurăm că agentul are acces la aceste surse:

Tipurile de context pe care un agent AI ar putea trebui să le gestioneze includ:

• **Instrucțiuni:** Acestea sunt ca "regulile" agentului – prompturi, mesaje de sistem, exemple few-shot (aratând AI cum să facă ceva) și descrieri ale instrumentelor pe care le poate folosi. Aici se combină focalizarea ingineriei promptului cu ingineria contextului.

• **Cunoștințe:** Acoperă fapte, informații preluate din baze de date sau amintiri pe termen lung acumulate de agent. Aceasta include integrarea unui sistem Retrieval Augmented Generation (RAG) dacă un agent are nevoie de acces la diferite depozite de cunoștințe și baze de date.

• **Instrumente:** Acestea sunt definițiile funcțiilor externe, API-urilor și serverelor MCP pe care agentul le poate apela, împreună cu feedback-ul (rezultatele) pe care îl primește folosindu-le.

• **Istoricul conversațiilor:** Dialogul continuu cu un utilizator. Pe măsură ce timpul trece, aceste conversații devin mai lungi și mai complexe, ceea ce înseamnă că ocupă spațiu în fereastra de context.

• **Preferințele utilizatorului:** Informații învățate despre gusturile sau neplăcerile unui utilizator în timp. Acestea pot fi stocate și apelate atunci când se iau decizii cheie pentru a ajuta utilizatorul.

## Strategii pentru o Inginerie Eficientă a Contextului

### Strategii de planificare

[![Context Engineering Best Practices](../../../translated_images/ro/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

O inginerie bună a contextului începe cu o planificare bună. Iată o abordare care vă va ajuta să începeți să gândiți cum să aplicați conceptul de inginerie a contextului:

1. **Definiți Rezultate Clare** - Rezultatele sarcinilor ce vor fi atribuite agenților AI ar trebui să fie clar definite. Răspundeți la întrebarea – „Cum va arăta lumea când agentul AI își termină sarcina?” Cu alte cuvinte, ce schimbare, informație sau răspuns ar trebui să aibă utilizatorul după interacțiunea cu agentul AI.
2. **Cartografiați Contextul** - Odată ce ați definit rezultatele agentului AI, trebuie să răspundeți la întrebarea „Ce informații are nevoie agentul AI pentru a finaliza această sarcină?”. Astfel puteți începe să cartografiați contextul în care pot fi localizate aceste informații.
3. **Creați Fluxuri pentru Context** - Acum că știți unde sunt informațiile, trebuie să răspundeți la întrebarea „Cum va obține agentul aceste informații?”. Acest lucru se poate face în diverse moduri, inclusiv RAG, utilizarea serverelor MCP și alte instrumente.

### Strategii practice

Planificarea este importantă, dar odată ce informațiile încep să curgă în fereastra de context a agentului, trebuie să avem strategii practice pentru a le gestiona:

#### Gestionarea contextului

În timp ce unele informații vor fi adăugate automat în fereastra de context, ingineria contextului înseamnă să preluăm un rol mai activ asupra acestor informații, ceea ce poate fi făcut prin câteva strategii:

 1. **Agent Scratchpad**
 Aceasta permite unui agent AI să ia notițe cu informații relevante despre sarcinile curente și interacțiunile cu utilizatorul în timpul unei singure sesiuni. Aceasta ar trebui să existe în afara ferestrei de context, într-un fișier sau obiect de rulare pe care agentul îl poate recupera ulterior în sesiunea respectivă, dacă este necesar.

 2. **Amintiri**
 Scratchpad-urile sunt bune pentru gestionarea informațiilor în afara ferestrei de context a unei singure sesiuni. Amintirile permit agenților să stocheze și să recupereze informații relevante pe parcursul mai multor sesiuni. Acestea pot include rezumate, preferințe ale utilizatorilor și feedback pentru îmbunătățiri viitoare.

 3. **Compresia contextului**
  Odată ce fereastra de context crește și se apropie de limita sa, pot fi folosite tehnici precum rezumarea și tăierea. Aceasta include fie păstrarea doar a celor mai relevante informații, fie eliminarea mesajelor mai vechi.
  
 4. **Sisteme Multi-Agent**
  Dezvoltarea unui sistem multi-agent este o formă de inginerie a contextului deoarece fiecare agent are propria fereastră de context. Modul în care acel context este împărtășit și transmis între diferiți agenți este un alt aspect de planificat când construiți aceste sisteme.
  
 5. **Mediile Sandbox**
  Dacă un agent are nevoie să ruleze cod sau să proceseze cantități mari de informații într-un document, acest lucru poate consuma un număr mare de token-uri pentru a procesa rezultatele. În loc să stocheze tot acest lucru în fereastra de context, agentul poate folosi un mediu sandbox care poate rula acest cod și să citească doar rezultatele și alte informații relevante.
  
 6. **Obiecte de stare la rulare**
   Acest lucru se face prin crearea unor containere de informații pentru a gestiona situațiile când agentul trebuie să aibă acces la anumite informații. Pentru o sarcină complexă, aceasta îi permite agentului să stocheze rezultatele fiecărui subtask pas cu pas, permițând ca contextul să rămână conectat doar la acel subtask specific.

#### Inspectarea contextului

După ce ați aplicat una dintre aceste strategii, merită să verificați ce a primit de fapt următorul apel al modelului. O întrebare utilă pentru depanare este:

> Agentul a încărcat prea mult context, context greșit sau a ratat contextul de care avea nevoie?

Nu este necesar să înregistrați prompturi brute, ieșirile instrumentelor sau conținutul memoriei pentru a răspunde la această întrebare. În producție, se preferă înregistrările mici de inspectare a contextului care capturează numărătoare, ID-uri, hash-uri și etichete de politică:

- **Selecție:** Monitorizați câte fragmente candidate, instrumente sau amintiri au fost luate în considerare, câte au fost selectate și ce regulă sau scor a determinat filtrarea celorlalte.
- **Compresie:** Înregistrați intervalul sursă sau ID-ul traseului, ID-ul rezumatului, o estimare a numărului de token-uri înainte și după compresie și dacă conținutul brut a fost exclus din următorul apel.
- **Izolare:** Notați ce subtask a rulat într-un agent, sesiune sau sandbox separat, ce rezumat limitat a fost returnat și dacă ieșirea mare a instrumentului a rămas în afara contextului agentului părinte.
- **Memorie și RAG:** Stocați ID-uri de documente recuperate, ID-uri de memorie, scoruri, ID-uri selectate și starea redactării în locul textului recuperat complet.
- **Siguranță și confidențialitate:** Se preferă hash-uri, ID-uri, token buckets și etichete de politică în loc de texte sensibile, argumente ale instrumentelor, rezultate ale instrumentelor sau corpuri de memorie ale utilizatorului.

Scopul nu este să păstrați mai mult context. Este să lăsați suficiente dovezi pentru ca un dezvoltator să poată spune ce strategie de context a fost aplicată și dacă a schimbat următorul apel al modelului în modul intenționat.

### Exemplu de Inginerie a Contextului

Să spunem că dorim ca un agent AI să **„Să-mi rezerve o călătorie la Paris.”**

• Un agent simplu care folosește doar ingineria promptului ar putea răspunde doar: **„Bine, când ai dori să mergi la Paris?”**. Acesta a procesat direct întrebarea pe momentul în care utilizatorul a întrebat.

• Un agent care folosește strategiile de inginerie a contextului acoperite ar face mult mai mult. Înainte de a răspunde, sistemul său ar putea:

  ◦ **Să-ți verifice calendarul** pentru date disponibile (recuperând date în timp real).

 ◦ **Să-și amintească preferințele anterioare de călătorie** (din memoria pe termen lung) precum compania aeriană preferată, bugetul sau dacă preferi zboruri directe.

 ◦ **Să identifice instrumentele disponibile** pentru rezervarea zborurilor și hotelurilor.

- Apoi, un răspuns exemplu ar putea fi: „Salut [Numele tău]! Văd că ești liber în prima săptămână din octombrie. Să caut zboruri directe spre Paris cu [Compania Aeriană Preferată] în bugetul tău obișnuit de [Buget]?”. Acest răspuns mai bogat, conștient de context, demonstrează puterea ingineriei contextului.

## Eșecuri Comune ale Contextului

### Intoxicarea Contextului

**Ce este:** Când o halucinație (informație falsă generată de LLM) sau o eroare intră în context și este repetat menționată, determinând agentul să urmărească obiective imposibile sau să dezvolte strategii fără sens.

**Ce să faci:** Implementați **validarea contextului** și **carantina**. Validați informațiile înainte să fie adăugate în memoria pe termen lung. Dacă se detectează o posibilă intoxicare, începeți fire de context noi pentru a preveni răspândirea informațiilor greșite.

**Exemplu de rezervare a călătoriei:** Agentul tău halucinează un **zbor direct de la un aeroport mic local către un oraș internațional îndepărtat** care, de fapt, nu oferă zboruri internaționale. Acest detaliu de zbor inexistent este salvat în context. Mai târziu, când ceri agentului să rezerve, încearcă constant să găsească bilete pentru această rută imposibilă, ducând la repetate erori.

**Soluție:** Implementați un pas care **validă existența zborului și rutele cu o API în timp real** _înainte_ de a adăuga detaliul zborului în contextul de lucru al agentului. Dacă validarea eșuează, informația eronată este „carantinată” și nu este utilizată mai departe.

### Distragerea Contextului

**Ce este:** Când contextul devine atât de mare încât modelul se focusează prea mult pe istoricul acumulat în loc să folosească ceea ce a învățat în timpul antrenamentului, ducând la acțiuni repetitive sau nefolositoare. Modelele pot începe să facă greșeli chiar înainte ca fereastra de context să fie plină.

**Ce să faci:** Folosește **rezumarea contextului**. Periodic, comprimă informațiile acumulate în rezumate mai scurte, păstrând detaliile importante și eliminând istoricul redundant. Acest lucru ajută la „resetarea” focalizării.

**Exemplu de rezervare a călătoriei:** Ai discutat despre diferite destinații de vis pentru o lungă perioadă, inclusiv o relatere detaliată a unei excursii cu rucsacul în urmă cu doi ani. Când în cele din urmă ceri să **„găsești un zbor ieftin pentru luna următoare,”** agentul se blochează în detaliile vechi, nerelevante, și continuă să întrebe despre echipamentul tău de backpacking sau itinerariile anterioare, ignorând cererea ta actuală.

**Soluție:** După un anumit număr de interacțiuni sau când contextul devine prea mare, agentul ar trebui să **rezume cele mai recente și relevante părți ale conversației** – concentrându-se pe datele actuale de călătorie și destinație – și să folosească acest rezumat comprimat pentru următorul apel LLM, eliminând chat-ul istoric mai puțin relevant.

### Confuzia Contextului

**Ce este:** Când contextul inutil, adesea sub formă de prea multe instrumente disponibile, determină modelul să genereze răspunsuri proaste sau să apeleze instrumente irelevante. Modelele mai mici sunt deosebit de predispuse la acest lucru.

**Ce să faci:** Implementați **gestionarea încărcăturii instrumentelor** folosind tehnici RAG. Stocați descrierile instrumentelor într-o bază de date vectorială și selectați _doar_ cele mai relevante instrumente pentru fiecare sarcină specifică. Cercetările arată că este bine să limitați selecția de instrumente la mai puțin de 30.

**Exemplu de rezervare a călătoriei:** Agentul tău are acces la zeci de instrumente: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` etc. Întrebi, **„Care este cel mai bun mod de a te deplasa prin Paris?”** Din cauza numărului mare de instrumente, agentul se confuză și încearcă să apeleze `book_flight` _în_ Paris, sau `rent_car` chiar dacă preferi transportul public, pentru că descrierile instrumentelor se suprapun sau pur și simplu nu poate distinge cel mai bun.

**Soluție:** Folosește **RAG peste descrierile instrumentelor**. Când întrebi despre deplasarea prin Paris, sistemul recuperează dinamic _doar_ cele mai relevante instrumente, precum `rent_car` sau `public_transport_info`, bazat pe întrebarea ta, prezentând un „loadout” concentrat de instrumente către LLM.

### Conflictul Contextului

**Ce este:** Când există informații contradictorii în context, ducând la raționamente inconsistente sau răspunsuri finale proaste. Acest lucru se întâmplă adesea când informațiile sosesc în etape, iar ipoteze incorecte timpurii rămân în context.

**Ce să faci:** Folosește **tăierea (pruning) contextului** și **externalizarea**. Tăierea înseamnă eliminarea informațiilor învechite sau conflictuale pe măsură ce sosesc detalii noi. Externalizarea oferă modelului un spațiu de lucru „scratchpad” separat pentru a procesa informații fără a aglomera contextul principal.


**Exemplu de rezervare pentru călătorie:** Inițial îi spui agentului tău, **"Vreau să zbor la clasa economică."** Mai târziu în conversație, îți schimbi părerea și spui, **"De fapt, pentru această călătorie, să mergem la clasa business."** Dacă ambele instrucțiuni rămân în context, agentul ar putea primi rezultate de căutare contradictorii sau s-ar putea confunda cu privire la ce preferință să acorde prioritate.

**Soluție:** Implementați **pruning-ul contextului**. Când o instrucțiune nouă contrazice pe cea veche, instrucțiunea veche este eliminată sau în mod explicit suprascrisă în context. Alternativ, agentul poate folosi un **scratchpad** pentru a reconcilia preferințele contradictorii înainte de a lua o decizie, asigurându-se că doar instrucțiunea finală și consistentă îi ghidează acțiunile.

## Ai Mai Multe Întrebări Despre Ingineria Contextului?

Alătură-te pe [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la ore de consultații și a primi răspunsuri la întrebările tale despre agenții AI.
## Lecția Anterioară

[Agentic Protocols](../11-agentic-protocols/README.md)

## Lecția Următoare

[Memory for AI Agents](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->