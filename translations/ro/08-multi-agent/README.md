[![Multi-agent Design](../../../translated_images/ro/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Click pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Modele de proiectare multi-agent

De îndată ce începi să lucrezi la un proiect care implică mai mulți agenți, va trebui să iei în considerare modelul de proiectare multi-agent. Totuși, s-ar putea să nu fie imediat clar când să treci la multi-agenți și care sunt avantajele.

## Introducere

În această lecție, căutăm să răspundem la următoarele întrebări:

- Care sunt scenariile în care multi-agenții sunt aplicabili?
- Care sunt avantajele utilizării multi-agenților în loc de un singur agent care face mai multe sarcini?
- Care sunt componentele de bază pentru implementarea modelului de proiectare multi-agent?
- Cum avem vizibilitate asupra modului în care agenții multipli interacționează între ei?

## Obiective de învățare

După această lecție, ar trebui să poți:

- Identifica scenariile în care sunt aplicabili multi-agenții
- Recunoaște avantajele utilizării multi-agenților față de un singur agent.
- Înțelege componentele de bază pentru implementarea modelului de proiectare multi-agent.

Care este imaginea de ansamblu?

*Multi-agenții sunt un model de proiectare care permite mai multor agenți să colaboreze pentru a atinge un scop comun*.

Acest model este folosit pe scară largă în diverse domenii, inclusiv robotică, sisteme autonome și calcul distribuit.

## Scenarii în care multi-agenții sunt aplicabili

Deci, care scenarii sunt un bun caz de utilizare pentru multi-agenți? Răspunsul este că există multe scenarii în care utilizarea mai multor agenți este benefică, în special în următoarele cazuri:

- **Sarcini mari de lucru**: Sarcinile mari de lucru pot fi împărțite în sarcini mai mici și atribuite diferiților agenți, permițând procesarea paralelă și finalizarea mai rapidă. Un exemplu este cazul unei sarcini mari de procesare a datelor.
- **Sarcini complexe**: Sarcinile complexe, ca și sarcinile mari, pot fi desfăcute în subtask-uri mai mici și atribuite diferiților agenți, fiecare specializându-se într-un aspect specific al sarcinii. Un exemplu bun este cazul vehiculelor autonome unde diferiți agenți gestionează navigația, detectarea obstacolelor și comunicarea cu alte vehicule.
- **Competențe diverse**: Diferiți agenți pot avea expertize diferite, ceea ce le permite să gestioneze aspecte diferite ale unei sarcini mai eficient decât un singur agent. Un exemplu bun în acest caz este domeniul sănătății, unde agenții pot gestiona diagnosticul, planurile de tratament și monitorizarea pacienților.

## Avantajele utilizării multi-agenților față de un singur agent

Un sistem cu un singur agent ar putea funcționa bine pentru sarcini simple, dar pentru sarcini mai complexe, utilizarea mai multor agenți poate oferi mai multe avantaje:

- **Specializare**: Fiecare agent poate fi specializat pentru o sarcină specifică. Lipsa specializării într-un singur agent înseamnă că ai un agent care poate face de toate, dar s-ar putea să se confunde la o sarcină complexă. De exemplu, s-ar putea să execute o sarcină pentru care nu este cel mai bine pregătit.
- **Scalabilitate**: Este mai ușor să scalezi sistemele adăugând mai mulți agenți, în loc să copleșești un singur agent.
- **Toleranță la eroare**: Dacă un agent eșuează, ceilalți pot continua să funcționeze, asigurând fiabilitatea sistemului.

Să luăm un exemplu, să rezervăm o călătorie pentru un utilizator. Un sistem cu un singur agent ar trebui să gestioneze toate aspectele procesului de rezervare – de la găsirea zborurilor până la rezervarea hotelurilor și a mașinilor de închiriat. Pentru a realiza asta cu un singur agent, acesta ar trebui să aibă unelte pentru toate aceste sarcini, ceea ce ar genera un sistem complex și monolitic, greu de întreținut și scalat. În schimb, un sistem multi-agent ar putea avea diferiți agenți specializați în găsirea zborurilor, rezervarea hotelurilor și închirierea mașinilor. Astfel, sistemul devine mai modular, mai ușor de întreținut și scalabil.

Compară asta cu o agenție de turism administrată ca un magazin de cartier versus o agenție care funcționează ca o franciză. Magazinul de cartier ar avea un singur agent care gestionează toate aspectele rezervării, în timp ce franciza ar avea diferiți agenți care gestionează diferite aspecte ale procesului.

## Componente de bază pentru implementarea modelului de proiectare multi-agent

Înainte de a implementa modelul de proiectare multi-agent, trebuie să înțelegi componentele care alcătuiesc modelul.

Să facem asta mai concret, revenind la exemplul rezervării unei călătorii pentru un utilizator. În acest caz, componentele de bază ar include:

- **Comunicarea între agenți**: Agenții pentru găsirea zborurilor, rezervarea hotelurilor și a mașinilor trebuie să comunice și să împărtășească informații despre preferințele și constrângerile utilizatorului. Trebuie să decizi protocoalele și metodele acestei comunicări. Concret, agentul pentru găsirea zborurilor trebuie să comunice cu agentul pentru rezervarea hotelurilor pentru a se asigura că hotelul este rezervat pentru aceleași date ca zborul. Asta înseamnă că agenții trebuie să împărtășească informații despre datele de călătorie ale utilizatorului, adică trebuie să decizi *care agenți împărtășesc informații și cum o fac*.
- **Mecanisme de coordonare**: Agenții trebuie să-și coordoneze acțiunile pentru a asigura că preferințele și constrângerile utilizatorului sunt îndeplinite. O preferință a utilizatorului ar putea fi să dorească un hotel aproape de aeroport, în timp ce o constrângere poate fi ca mașinile de închiriat să fie disponibile doar la aeroport. Asta înseamnă că agentul pentru rezervarea hotelurilor trebuie să se coordoneze cu agentul pentru rezervarea mașinilor pentru a asigura îndeplinirea preferințelor și constrângerilor. Deci trebuie să decizi *cum agenții își coordonează acțiunile*.
- **Arhitectura agenților**: Agenții trebuie să aibă o structură internă pentru a lua decizii și a învăța din interacțiunile cu utilizatorul. Astfel, agentul pentru găsirea zborurilor trebuie să aibă o arhitectură internă care să-i permită să ia decizii privind ce zboruri să recomande utilizatorului. Trebuie să decizi *cum agenții iau decizii și învață din interacțiuni*. Exemplele pentru învățarea unui agent pot include utilizarea unui model de învățare automată de către agentul pentru zboruri pentru a recomanda în funcție de preferințele anterioare ale utilizatorului.
- **Vizibilitatea interacțiunilor multi-agent**: Trebuie să ai vizibilitate asupra modului în care agenții multipli interacționează. Asta înseamnă să ai unelte și tehnici pentru monitorizarea activităților și interacțiunilor agenților. Acest lucru poate fi realizat prin unelte de logare și monitorizare, vizualizare și metrici de performanță.
- **Modele multi-agent**: Există diferite modele pentru implementarea sistemelor multi-agent, cum ar fi arhitecturi centralizate, descentralizate și hibride. Trebuie să alegi modelul care se potrivește cel mai bine cazului tău de utilizare.
- **Omul în buclă**: În majoritatea cazurilor, există un om în buclă și trebuie să instrucți agenții când să ceară intervenția umană. Acest lucru poate fi sub forma unui utilizator care cere un hotel sau zbor anume pe care agenții nu l-au recomandat sau solicită confirmarea înainte de rezervare.

## Vizibilitatea interacțiunilor multi-agent

Este important să ai vizibilitate asupra modului în care agenții multipli interacționează între ei. Această vizibilitate este esențială pentru depanare, optimizare și asigurarea eficacității sistemului în ansamblu. Pentru aceasta ai nevoie de unelte și tehnici pentru monitorizarea activităților și interacțiunilor agenților. Aceasta poate include unelte de logare și monitorizare, unelte de vizualizare și metrici de performanță.

De exemplu, în cazul rezervării unei călătorii, ai putea avea un panou de control care arată starea fiecărui agent, preferințele și constrângerile utilizatorului și interacțiunile între agenți. Acest panou ar putea afișa datele călătoriei, zborurile recomandate de agentul zborurilor, hotelurile recomandate de agentul hotelurilor și mașinile recomandate de agentul mașinilor de închiriat. Astfel ai o imagine clară despre cum interacționează agenții și dacă sunt respectate preferințele și constrângerile utilizatorului.

Să analizăm mai detaliat fiecare dintre aceste aspecte.

- **Unelte de logare și monitorizare**: Vrei să ai logarea fiecărei acțiuni întreprinse de un agent. O înregistrare în jurnal poate stoca informații despre agentul care a executat acțiunea, acțiunea făcută, timpul când a fost executată și rezultatul acțiunii. Aceste informații se pot folosi pentru depanare, optimizare și altele.

- **Unelte de vizualizare**: Aceste unelte te pot ajuta să vezi interacțiunile dintre agenți într-un mod mai intuitiv. De exemplu, ai putea avea un grafic care arată fluxul de informații între agenți. Acest lucru te poate ajuta să identifici blocaje, ineficiențe și alte probleme în sistem.

- **Metrici de performanță**: Aceste metrici te pot ajuta să urmărești eficacitatea sistemului multi-agent. De exemplu, poți urmări timpul necesar pentru a finaliza o sarcină, numărul de sarcini finalizate pe unitate de timp și acuratețea recomandărilor făcute de agenți. Aceste informații te pot ajuta să identifici zonele de îmbunătățire și să optimizezi sistemul.

## Modele multi-agent

Să explorăm câteva modele concrete pe care le putem folosi pentru a crea aplicații multi-agent. Iată câteva modele interesante de luat în considerare:

### Chat de grup

Acest model este util când vrei să creezi o aplicație de chat de grup unde mai mulți agenți pot comunica între ei. Cazurile tipice de utilizare includ colaborarea în echipă, suportul pentru clienți și rețele sociale.

În acest model, fiecare agent reprezintă un utilizator în chat-ul de grup, iar mesajele sunt schimbate între agenți folosind un protocol de mesagerie. Agenții pot trimite mesaje în chat-ul de grup, pot primi mesaje din chat și pot răspunde mesajelor altor agenți.

Acest model poate fi implementat folosind o arhitectură centralizată unde toate mesajele sunt rutate printr-un server central, sau o arhitectură descentralizată unde mesajele sunt schimbate direct.

![Chat de grup](../../../translated_images/ro/multi-agent-group-chat.ec10f4cde556babd.webp)

### Transfer de sarcini

Acest model este util atunci când vrei să creezi o aplicație în care mai mulți agenți pot transfera sarcini între ei.

Cazurile tipice de utilizare includ suportul pentru clienți, gestionarea sarcinilor și automatizarea fluxului de lucru.

În acest model, fiecare agent reprezintă o sarcină sau un pas într-un flux de lucru, iar agenții pot transfera sarcini altor agenți conform regulilor predefinite.

![Transfer de sarcini](../../../translated_images/ro/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtrare colaborativă

Acest model este util când vrei să creezi o aplicație în care mai mulți agenți pot colabora pentru a face recomandări utilizatorilor.

Motivul pentru care vrei ca mai mulți agenți să colaboreze este că fiecare agent poate avea expertize diferite și poate contribui în moduri diferite la procesul de recomandare.

Să luăm un exemplu în care un utilizator dorește o recomandare privind cea mai bună acțiune de cumpărat pe piața bursieră.

- **Expert în industrie**: Un agent ar putea fi expert într-un anumit domeniu industrial.
- **Analiză tehnică**: Un alt agent ar putea fi expert în analiza tehnică.
- **Analiză fundamentală**: iar un alt agent ar putea fi expert în analiza fundamentală. Colaborând, acești agenți pot oferi o recomandare mai cuprinzătoare utilizatorului.

![Recomandare](../../../translated_images/ro/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenariu: Procesul de rambursare

Să considerăm un scenariu în care un client încearcă să obțină o rambursare pentru un produs; pot exista destul de mulți agenți implicați în acest proces, dar să împărțim între agenți specifici acestui proces și agenți generali care pot fi folosiți și în alte procese.

**Agenți specifici pentru procesul de rambursare**:

Următorii agenți ar putea fi implicați în procesul de rambursare:

- **Agent client**: Acest agent reprezintă clientul și este responsabil pentru inițierea procesului de rambursare.
- **Agent vânzător**: Acest agent reprezintă vânzătorul și este responsabil pentru procesarea rambursării.
- **Agent de plată**: Acest agent reprezintă procesul de plată și este responsabil pentru rambursarea plății clientului.
- **Agent de rezolvare**: Acest agent reprezintă procesul de rezolvare și este responsabil pentru soluționarea oricăror probleme ce apar în timpul procesului de rambursare.
- **Agent de conformitate**: Acest agent reprezintă procesul de conformitate și este responsabil să se asigure că procesul de rambursare respectă reglementările și politicile.

**Agenți generali**:

Acești agenți pot fi folosiți în alte părți ale afacerii tale.

- **Agent de livrare**: Acest agent reprezintă procesul de livrare și este responsabil pentru trimiterea produsului înapoi la vânzător. Acest agent poate fi folosit atât pentru procesul de rambursare, cât și pentru livrarea generală a unui produs prin cumpărare, de exemplu.
- **Agent de feedback**: Acest agent reprezintă procesul de colectare a feedback-ului de la client. Feedback-ul poate fi colectat oricând, nu doar în timpul procesului de rambursare.
- **Agent de escaladare**: Acest agent reprezintă procesul de escaladare și este responsabil pentru escaladarea problemelor la un nivel superior de suport. Poți folosi acest tip de agent pentru orice proces în care trebuie să escaladezi o problemă.
- **Agent de notificări**: Acest agent gestionează procesul de notificare și este responsabil pentru trimiterea notificărilor către client în diverse etape ale procesului de rambursare.
- **Agent de analiză**: Acest agent reprezintă procesul de analiză și este responsabil pentru analiza datelor legate de procesul de rambursare.
- **Agent de audit**: Acest agent reprezintă procesul de audit și este responsabil pentru auditul procesului de rambursare pentru a se asigura că se desfășoară corect.
- **Agent de raportare**: Acest agent gestionează procesul de raportare și este responsabil pentru generarea rapoartelor despre procesul de rambursare.
- **Agent de cunoștințe**: Acest agent gestionează procesul de cunoștințe și este responsabil pentru menținerea unei baze de cunoștințe despre procesul de rambursare. Acest agent ar putea fi informat atât despre rambursări cât și despre alte părți ale afacerii tale.
- **Agent de securitate**: Acest agent se ocupă de procesul de securitate și asigură securitatea procesului de rambursare.
- **Agent de calitate**: Acest agent răspunde de procesul de asigurare a calității și se asigură de calitatea procesului de rambursare.

Sunt destul de mulți agenți enumerați mai sus, atât pentru procesul specific de rambursare, cât și pentru agenții generali ce pot fi folosiți în alte părți ale afacerii tale. Sperăm că acest lucru îți oferă o idee despre cum poți decide care agenți să folosești în sistemul tău multi-agent.

## Sarcină

Proiectează un sistem multi-agent pentru un proces de suport clienți. Identifică agenții implicați în proces, rolurile și responsabilitățile lor și modul în care interacționează între ei. Ia în considerare atât agenți specifici procesului de suport clienți, cât și agenți generali care pot fi folosiți în alte părți ale afacerii tale.


> Gândește-te puțin înainte să citești soluția următoare, s-ar putea să ai nevoie de mai mulți agenți decât crezi.

> SUGESTIE: Gândește-te la diferitele etape ale procesului de suport pentru clienți și ia în considerare și agenții necesari pentru orice sistem.

## Soluție

[Soluție](./solution/solution.md)

## Verificări de cunoștințe

### Întrebarea 1

Care scenariu se potrivește cel mai bine pentru un sistem multi-agent?

- [ ] A1: Un bot de suport răspunde la întrebări obișnuite folosind o singură bază de cunoștințe și un set mic de instrumente.
- [ ] A2: Un flux de lucru pentru rambursări necesită roluri separate pentru fraudă, plăți și conformitate, fiecare cu propriile instrumente, iar rezultatele lor trebuie coordonate.
- [ ] A3: Aceeași cerere simplă de clasificare soseste de mii de ori pe oră.

### Întrebarea 2

Când este un agent unic de obicei alegerea mai bună?

- [ ] A1: Sarcina poate fi gestionată cu un singur set de instrucțiuni și instrumente, fără transferuri către specialiști.
- [ ] A2: Agentul are acces la mai mult de un instrument.
- [ ] A3: Fluxul de lucru necesită roluri separate cu permisiuni diferite și trasee de audit independente.

[Quiz soluție](./solution/solution-quiz.md)

## Rezumat

În această lecție, am analizat modelul de proiectare multi-agent, inclusiv scenariile în care multi-agenta sunt aplicabile, avantajele utilizării multi-agentului față de un agent singular, elementele de bază pentru implementarea modelului multi-agent și cum să ai vizibilitate asupra modului în care multiplele agenți interacționează între ei.

### Ai mai multe întrebări despre modelul de proiectare Multi-Agent?

Alătură-te [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, pentru a participa la orele de consultanță și pentru a primi răspunsuri la întrebările tale despre agenții AI.

## Resurse suplimentare

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Documentația Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Modele de proiectare agentic</a>


## Lecția anterioară

[Planificare design](../07-planning-design/README.md)

## Lecția următoare

[Metacogniție în agenții AI](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->