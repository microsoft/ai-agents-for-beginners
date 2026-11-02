[![Multi-Agent Design](../../../translated_images/ro/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul lecției)_

# Modele de design multi-agent

De îndată ce începeți să lucrați la un proiect care implică mai mulți agenți, va trebui să luați în considerare modelul de design multi-agent. Cu toate acestea, poate să nu fie clar imediat când să treceți la mai mulți agenți și care sunt avantajele.

## Introducere

În această lecție, vom încerca să răspundem la următoarele întrebări:

- Care sunt scenariile în care multi-agentele sunt aplicabile?
- Care sunt avantajele utilizării mai multor agenți față de un singur agent care face mai multe sarcini?
- Care sunt elementele de bază pentru implementarea modelului de design multi-agent?
- Cum putem avea vizibilitate asupra modului în care multiplele agenți interacționează între ei?

## Obiective de învățare

După această lecție, ar trebui să fiți capabil să:

- Identificați scenariile în care multi-agentele sunt aplicabile
- Recunoașteți avantajele utilizării mai multor agenți în locul unui agent singular.
- Înțelegeți elementele de bază pentru implementarea modelului de design multi-agent.

Care este imaginea de ansamblu?

*Multi-agentele sunt un model de design care permite mai multor agenți să lucreze împreună pentru a atinge un scop comun*.

Acest model este larg utilizat în diverse domenii, inclusiv robotică, sisteme autonome și calcul distribuit.

## Scenarii în care multi-agentele sunt aplicabile

Deci, care scenarii sunt un bun caz de utilizare pentru folosirea mai multor agenți? Răspunsul este că există multe scenarii în care folosirea mai multor agenți este benefică, în special în următoarele cazuri:

- **Sarcini mari de lucru**: Sarcinile mari pot fi împărțite în sarcini mai mici și atribuite diferiților agenți, permițând procesare paralelă și finalizare mai rapidă. Un exemplu este în cazul unei sarcini mari de procesare a datelor.
- **Sarcini complexe**: Sarcinile complexe, la fel ca sarcinile mari, pot fi împărțite în sub-sarcini mai mici și atribuite agenților diferiți, fiecare specializat într-un aspect specific al sarcinii. Un exemplu bun este în cazul vehiculelor autonome unde diferiți agenți gestionează navigația, detectarea obstacolelor și comunicarea cu alte vehicule.
- **Expertiză diversă**: Agenții diferiți pot avea expertiză diversă, permițându-le să gestioneze diferite aspecte ale unei sarcini mai eficient decât un singur agent. Un exemplu bun aici este în domeniul sănătății, unde agenții pot gestiona diagnosticarea, planurile de tratament și monitorizarea pacienților.

## Avantajele folosirii mai multor agenți față de un agent singular

Un sistem cu un singur agent ar putea funcționa bine pentru sarcini simple, dar pentru sarcini mai complexe, folosirea mai multor agenți poate oferi mai multe avantaje:

- **Specializare**: Fiecare agent poate fi specializat pentru o anumită sarcină. Lipsa specializării într-un singur agent înseamnă că aveți un agent care poate face de toate, dar care se poate confunda când este confruntat cu o sarcină complexă. De exemplu, ar putea ajunge să realizeze o sarcină pentru care nu este cel mai potrivit.
- **Scalabilitate**: Este mai ușor să scalați sistemele adăugând mai mulți agenți decât să suprasolicitați un singur agent.
- **Toleranță la erori**: Dacă un agent eșuează, alții pot continua să funcționeze, asigurând fiabilitatea sistemului.

Să luăm un exemplu, să rezervăm o călătorie pentru un utilizator. Un sistem cu un singur agent ar trebui să gestioneze toate aspectele procesului de rezervare a călătoriei, de la găsirea zborurilor la rezervarea hotelurilor și a mașinilor de închiriat. Pentru a realiza acest lucru cu un singur agent, agentul ar trebui să aibă instrumente pentru a gestiona toate aceste sarcini. Acest lucru ar putea duce la un sistem complex și monolitic, dificil de întreținut și scalabil. Un sistem multi-agent, pe de altă parte, ar putea avea agenți diferiți specializați în găsirea zborurilor, rezervarea hotelurilor și închirierea mașinilor. Acest lucru ar face sistemul mai modular, mai ușor de întreținut și scalabil.

Comparați asta cu o agenție de turism condusă ca un magazin de familie versus o agenție de turism condusă ca un franciză. Magazinul de familie ar avea un singur agent care gestionează toate aspectele procesului de rezervare a călătoriei, în timp ce franciza ar avea agenți diferiți care gestionează diferite aspecte ale procesului de rezervare.

## Elementele de bază pentru implementarea modelului de design multi-agent

Înainte de a implementa modelul de design multi-agent, trebuie să înțelegeți elementele de bază care compun modelul.

Să facem acest lucru mai concret din nou uitându-ne la exemplul rezervării unei călătorii pentru un utilizator. În acest caz, elementele de bază ar include:

- **Comunicarea agenților**: Agenții pentru găsirea zborurilor, rezervarea hotelurilor și a mașinilor de închiriat trebuie să comunice și să partajeze informații despre preferințele și constrângerile utilizatorului. Trebuie să decideți protocoalele și metodele pentru această comunicare. Ce înseamnă concret asta este că agentul pentru găsirea zborurilor trebuie să comunice cu agentul de rezervare hoteluri pentru a se asigura că hotelul este rezervat pentru aceleași date ca zborul. Asta înseamnă că agenții trebuie să partajeze informații despre datele de călătorie ale utilizatorului, deci trebuie să decideți *care agenți împărtășesc informații și cum le împărtășesc*.
- **Mecanisme de coordonare**: Agenții trebuie să-și coordoneze acțiunile pentru a se asigura că preferințele și constrângerile utilizatorului sunt respectate. O preferință a utilizatorului poate fi că dorește un hotel aproape de aeroport, în timp ce o constrângere poate fi că mașinile de închiriat sunt disponibile doar la aeroport. Asta înseamnă că agentul pentru rezervarea hotelurilor trebuie să se coordoneze cu agentul pentru rezervarea mașinilor de închiriat pentru a asigura respectarea preferințelor și constrângerilor utilizatorului. Aceasta înseamnă că trebuie să decideți *cum agenții își coordonează acțiunile*.
- **Arhitectura agentului**: Agenții trebuie să aibă structura internă pentru a lua decizii și a învăța din interacțiunile cu utilizatorul. Asta înseamnă că agentul pentru găsirea zborurilor trebuie să aibă structura internă de a lua decizii despre ce zboruri să recomande utilizatorului. Trebuie să decideți *cum agenții iau decizii și învață din interacțiunile cu utilizatorul*. Exemple de cum un agent învață și se îmbunătățește ar putea fi că agentul pentru găsirea zborurilor ar putea folosi un model de învățare automată pentru a recomanda zboruri utilizatorului bazat pe preferințele anterioare.
- **Vizibilitate asupra interacțiunilor multi-agent**: Trebuie să aveți vizibilitate asupra modului în care agenții multiple interacționează între ei. Asta înseamnă că trebuie să aveți instrumente și tehnici pentru urmăririi activităților și interacțiunilor agenților. Aceasta poate fi sub forma uneltelor de jurnalizare și monitorizare, uneltelor de vizualizare și metricilor de performanță.
- **Modele multi-agent**: Există modele diferite pentru implementarea sistemelor multi-agent, cum ar fi arhitecturi centralizate, descentralizate și hibride. Trebuie să decideți modelul care se potrivește cel mai bine cazului dumneavoastră.
- **Omul în buclă**: În majoritatea cazurilor, veți avea un om în buclă și trebuie să instruiți agenții când să ceară intervenția umană. Aceasta poate fi sub forma unui utilizator care cere un hotel sau zbor specific pe care agenții nu l-au recomandat sau care cere confirmare înainte de rezervarea unui zbor sau hotel.

## Vizibilitatea asupra interacțiunilor multi-agent

Este important să aveți vizibilitate asupra modului în care mai mulți agenți interacționează între ei. Această vizibilitate este esențială pentru depanare, optimizare și asigurarea eficacității generale a sistemului. Pentru a realiza acest lucru, trebuie să aveți instrumente și tehnici pentru urmărirea activităților și interacțiunilor agenților. Aceasta poate fi sub forma de unelte de înregistrare și monitorizare, unelte de vizualizare și metrici de performanță.

De exemplu, în cazul rezervării unei călătorii pentru un utilizator, ați putea avea un tablou de bord care să arate starea fiecărui agent, preferințele și constrângerile utilizatorului și interacțiunile dintre agenți. Acest tablou de bord ar putea arăta datele de călătorie ale utilizatorului, zborurile recomandate de agentul pentru zboruri, hotelurile recomandate de agentul pentru hoteluri și mașinile de închiriat recomandate de agentul pentru închirieri. Aceasta v-ar oferi o vedere clară asupra modului în care agenții interacționează între ei și dacă preferințele și constrângerile utilizatorului sunt respectate.

Să analizăm fiecare dintre aceste aspecte în mai mare detaliu.

- **Instrumente de înregistrare și monitorizare**: Doriți să aveți înregistrarea fiecărei acțiuni realizate de un agent. O intrare în jurnal poate stoca informații despre agentul care a realizat acțiunea, acțiunea realizată, timpul când a fost efectuată și rezultatul acesteia. Aceste informații pot fi utilizate apoi pentru depanare, optimizare și altele.

- **Instrumente de vizualizare**: Instrumentele de vizualizare vă pot ajuta să vedeți interacțiunile dintre agenți într-un mod mai intuitiv. De exemplu, ați putea avea un grafic care arată fluxul de informații între agenți. Acesta v-ar putea ajuta să identificați blocaje, ineficiențe și alte probleme în sistem.

- **Metrici de performanță**: Metricile de performanță vă pot ajuta să urmăriți eficacitatea sistemului multi-agent. De exemplu, ați putea urmări timpul necesar pentru finalizarea unei sarcini, numărul de sarcini finalizate pe unitate de timp și precizia recomandărilor făcute de agenți. Aceste informații vă pot ajuta să identificați zonele care necesită îmbunătățire și să optimizați sistemul.

## Modele multi-agent

Să analizăm câteva modele concrete pe care le putem folosi pentru a crea aplicații multi-agent. Iată câteva modele interesante care merită luate în considerare:

### Chat de grup

Acest model este util atunci când doriți să creați o aplicație de chat de grup unde mai mulți agenți pot comunica între ei. Cazuri tipice de utilizare pentru acest model includ colaborarea în echipă, suportul pentru clienți și rețele sociale.

În acest model, fiecare agent reprezintă un utilizator în chat-ul de grup, iar mesajele sunt schimbate între agenți folosind un protocol de mesagerie. Agenții pot trimite mesaje către chat-ul de grup, pot primi mesaje din chat-ul de grup și pot răspunde la mesajele altor agenți.

Modelul poate fi implementat folosind o arhitectură centralizată unde toate mesajele sunt rutate printr-un server central sau o arhitectură descentralizată unde mesajele sunt schimbate direct.

![Chat de grup](../../../translated_images/ro/multi-agent-group-chat.ec10f4cde556babd.webp)

### Transfer de sarcini

Acest model este util atunci când doriți să creați o aplicație unde mai mulți agenți pot transfera sarcini între ei.

Cazuri tipice de utilizare pentru acest model includ suportul pentru clienți, gestionarea sarcinilor și automatizarea fluxurilor de lucru.

În acest model, fiecare agent reprezintă o sarcină sau un pas într-un flux de lucru, iar agenții pot transfera sarcini altor agenți pe baza unor reguli predefinite.

![Transfer de sarcini](../../../translated_images/ro/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtrare colaborativă

Acest model este util atunci când doriți să creați o aplicație în care mai mulți agenți pot colabora pentru a face recomandări utilizatorilor.

Motivul pentru care ați dori ca mai mulți agenți să colaboreze este că fiecare agent poate avea expertiză diferită și poate contribui în moduri diferite procesului de recomandare.

Să luăm un exemplu în care un utilizator dorește o recomandare privind cel mai bun acțiune de cumpărat pe piața bursieră.

- **Expert în industrie**: Un agent ar putea fi expert într-o industrie specifică.
- **Analiză tehnică**: Alt agent ar putea fi expert în analiza tehnică.
- **Analiză fundamentală**: iar un alt agent ar putea fi expert în analiza fundamentală. Colaborând, acești agenți pot oferi o recomandare mai cuprinzătoare utilizatorului.

![Recomandare](../../../translated_images/ro/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenariu: Procesul de rambursare

Luați în considerare un scenariu în care un client încearcă să obțină o rambursare pentru un produs, pot fi implicați destul de mulți agenți în acest proces, dar să împărțim între agenți specifici pentru acest proces și agenți generali care pot fi folosiți în alte procese.

**Agenți specifici pentru procesul de rambursare**:

Următorii sunt câțiva agenți care ar putea fi implicați în procesul de rambursare:

- **Agent client**: Acest agent reprezintă clientul și este responsabil pentru inițierea procesului de rambursare.
- **Agent vânzător**: Acest agent reprezintă vânzătorul și este responsabil pentru procesarea rambursării.
- **Agent plată**: Acest agent reprezintă procesul de plată și este responsabil pentru returnarea banilor clientului.
- **Agent rezoluție**: Acest agent reprezintă procesul de rezoluție și este responsabil pentru rezolvarea oricăror probleme care apar în timpul procesului de rambursare.
- **Agent conformitate**: Acest agent reprezintă procesul de conformitate și este responsabil pentru asigurarea conformității procesului de rambursare cu reglementările și politicile.

**Agenți generali**:

Acești agenți pot fi folosiți în alte părți ale afacerii dumneavoastră.

- **Agent de expediere**: Acest agent reprezintă procesul de expediere și este responsabil pentru returnarea produsului către vânzător. Acest agent poate fi folosit atât pentru procesul de rambursare, cât și pentru expedierea generală a unui produs printr-o achiziție, de exemplu.
- **Agent de feedback**: Acest agent reprezintă procesul de colectare a feedback-ului și este responsabil pentru colectarea feedback-ului de la client. Feedback-ul poate fi cerut în orice moment, nu doar în timpul procesului de rambursare.
- **Agent de escaladare**: Acest agent reprezintă procesul de escaladare și este responsabil pentru escaladarea problemelor la un nivel superior de suport. Puteți folosi acest tip de agent pentru orice proces unde este necesar să escaladați o problemă.
- **Agent de notificare**: Acest agent reprezintă procesul de notificare și este responsabil pentru trimiterea notificărilor către client în diferite etape ale procesului de rambursare.
- **Agent de analiză**: Acest agent reprezintă procesul de analiză și este responsabil pentru analizarea datelor legate de procesul de rambursare.
- **Agent de audit**: Acest agent reprezintă procesul de audit și este responsabil pentru auditarea procesului de rambursare pentru a se asigura că se desfășoară corect.
- **Agent de raportare**: Acest agent reprezintă procesul de raportare și este responsabil pentru generarea rapoartelor privind procesul de rambursare.
- **Agent de cunoștințe**: Acest agent reprezintă procesul de gestionare a cunoștințelor și este responsabil pentru menținerea unei baze de cunoștințe legată de procesul de rambursare. Acest agent ar putea fi informat atât despre rambursări, cât și despre alte părți ale afacerii dumneavoastră.
- **Agent de securitate**: Acest agent reprezintă procesul de securitate și este responsabil pentru asigurarea securității procesului de rambursare.
- **Agent de calitate**: Acest agent reprezintă procesul de control al calității și este responsabil pentru asigurarea calității procesului de rambursare.

Există destul de mulți agenți listați anterior, atât pentru procesul specific de rambursare, cât și pentru agenții generali care pot fi folosiți în alte părți ale afacerii dumneavoastră. Sperăm că acest lucru vă oferă o idee despre cum puteți decide ce agenți să folosiți în sistemul dumneavoastră multi-agent.

## Exercițiu

Proiectați un sistem multi-agent pentru un proces de suport clienți. Identificați agenții implicați în proces, rolurile și responsabilitățile lor și modul în care interacționează între ei. Luați în considerare atât agenții specifici pentru procesul de suport clienți, cât și agenții generali care pot fi folosiți în alte părți ale afacerii dumneavoastră.


> Gândește-te puțin înainte să citești soluția următoare, este posibil să ai nevoie de mai mulți agenți decât crezi.

> SUGESTIE: Gândește-te la diferitele etape ale procesului de suport pentru clienți și ia în considerare și agenții necesari pentru orice sistem.

## Soluție

[Soluție](./solution/solution.md)

## Verificări de cunoștințe

### Întrebarea 1

Care scenariu este cel mai potrivit pentru un sistem multi-agent?

- [ ] A1: Un bot de suport răspunde întrebărilor frecvente folosind o singură bază de cunoștințe și un set mic de unelte.
- [ ] A2: Un flux de rambursare necesită roluri separate pentru fraudă, plată și conformitate, fiecare cu propriile unelte, iar rezultatele acestora trebuie coordonate.
- [ ] A3: Același tip simplu de cerere de clasificare ajunge de mii de ori pe oră.

### Întrebarea 2

Când este mai potrivit un singur agent?

- [ ] A1: Sarcina poate fi gestionată cu un singur set de instrucțiuni și unelte, fără transferuri între specialiști.
- [ ] A2: Agentul are acces la mai mult de o unealtă.
- [ ] A3: Fluxul de lucru necesită roluri separate cu permisiuni diferite și trasee independente de audit.

[Soluția quiz-ului](./solution/solution-quiz.md)

## Rezumat

În această lecție, am analizat modelul de design multi-agent, inclusiv scenariile în care sunt aplicabili agenții multipli, avantajele utilizării agenților multipli față de un agent singular, elementele de bază pentru implementarea modelului de design multi-agent și cum să ai vizibilitate asupra modului în care agenții multipli interacționează între ei.

### Ai mai multe întrebări despre modelul de design multi-agent?

Alătură-te Discord-ului [Microsoft Foundry](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, participa la ore de consultanță și pentru a primi răspunsuri la întrebările tale despre Agenții AI.

## Resurse suplimentare

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Documentația Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Modele de design agentice</a>


## Lecția anterioară

[Planning Design](../07-planning-design/README.md)

## Lecția următoare

[Metacognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->