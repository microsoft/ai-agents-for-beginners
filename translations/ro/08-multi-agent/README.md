[![Design multi-agent](../../../translated_images/ro/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Faceți clic pe imaginea de mai sus pentru a vizualiza videoclipul acestei lecții)_

# Modele de proiectare multi-agent

De îndată ce începeți să lucrați la un proiect care implică mai mulți agenți, va trebui să luați în considerare modelul de proiectare multi-agent. Cu toate acestea, s-ar putea să nu fie imediat clar când să treceți la mai mulți agenți și care sunt avantajele.

## Introducere

În această lecție, încercăm să răspundem la următoarele întrebări:

- Care sunt scenariile în care se aplică agenții multipli?
- Care sunt avantajele utilizării mai multor agenți față de un singur agent care face mai multe sarcini?
- Care sunt blocurile de construcție pentru implementarea modelului multi-agent?
- Cum avem vizibilitate asupra modului în care agenții multipli interacționează între ei?

## Obiective de învățare

După această lecție, ar trebui să puteți:

- Identifica scenarii în care se aplică agenții multipli
- Recunoaște avantajele utilizării mai multor agenți față de un singur agent.
- Înțelege blocurile de construcție pentru implementarea modelului de proiectare multi-agent.

Care este imaginea de ansamblu?

*Multi-agents sunt un model de proiectare care permite mai multor agenți să lucreze împreună pentru a atinge un obiectiv comun*.

Acest model este utilizat pe scară largă în diverse domenii, inclusiv robotică, sisteme autonome și calcul distribuit.

## Scenarii în care se aplică agenții multipli

Deci, care scenarii sunt un bun caz de utilizare pentru agenți multipli? Răspunsul este că există multe scenarii în care angajarea mai multor agenți este benefică, în special în următoarele cazuri:

- **Sarcini de lucru mari**: Sarcinile de lucru mari pot fi împărțite în sarcini mai mici și atribuite unor agenți diferiți, permițând procesarea în paralel și finalizarea mai rapidă. Un exemplu este în cazul unei sarcini mari de procesare a datelor.
- **Sarcini complexe**: Sarcinile complexe, asemeni sarcinilor de lucru mari, pot fi împărțite în subtasks mai mici și atribuite agenților diferiți, fiecare specializându-se într-un aspect specific al sarcinii. Un bun exemplu este în cazul vehiculelor autonome, unde agenți diferiți gestionează navigația, detectarea obstacolelor și comunicația cu celelalte vehicule.
- **Expertiză diversă**: Agenții diferiți pot avea expertiză diversă, permițându-le să gestioneze aspecte diferite ale unei sarcini mai eficient decât un singur agent. Pentru acest caz, un bun exemplu este în domeniul sănătății, unde agenții pot gestiona diagnosticul, planurile de tratament și monitorizarea pacienților.

## Avantajele utilizării mai multor agenți față de un singur agent

Un sistem cu un singur agent ar putea funcționa bine pentru sarcini simple, dar pentru sarcini mai complexe, utilizarea mai multor agenți poate oferi mai multe avantaje:

- **Specializare**: Fiecare agent poate fi specializat pentru o sarcină specifică. Lipsa specializării într-un singur agent înseamnă că aveți un agent care poate face totul, dar s-ar putea confunda atunci când se confruntă cu o sarcină complexă. De exemplu, s-ar putea ajunge să execute o sarcină pentru care nu este cel mai potrivit.
- **Scalabilitate**: Este mai ușor să scalați sistemele prin adăugarea mai multor agenți decât prin supraîncărcarea unui singur agent.
- **Toleranță la erori**: Dacă un agent eșuează, alții pot continua să funcționeze, asigurând fiabilitatea sistemului.

Să luăm un exemplu: să rezervăm o călătorie pentru un utilizator. Un sistem cu un singur agent ar trebui să gestioneze toate aspectele procesului de rezervare a călătoriei, de la găsirea zborurilor până la rezervarea hotelurilor și a mașinilor de închiriat. Pentru a realiza acest lucru cu un singur agent, agentul ar trebui să aibă instrumente pentru gestionarea tuturor acestor sarcini. Acest lucru ar putea duce la un sistem complex și monolitic, dificil de întreținut și scalat. Un sistem multi-agent, pe de altă parte, ar putea avea agenți diferiți specializați în găsirea zborurilor, rezervarea hotelurilor și a mașinilor de închiriat. Acest lucru ar face sistemul mai modular, mai ușor de întreținut și scalabil.

Comparați acest lucru cu o agenție de turism condusă ca un magazin de familie versus o agenție de turism condusă ca franciză. Magazinul de familie ar avea un singur agent care se ocupă de toate aspectele procesului de rezervare a călătoriei, în timp ce franciza ar avea agenți diferiți care se ocupă de diferite aspecte ale procesului de rezervare a călătoriei.

## Componente ale implementării modelului de proiectare multi-agent

Înainte de a implementa modelul de proiectare multi-agent, trebuie să înțelegeți componentele care alcătuiesc modelul.

Să facem acest lucru mai concret, uitându-ne din nou la exemplul rezervării unei călătorii pentru un utilizator. În acest caz, componentele ar include:

- **Comunicarea agenților**: Agenții pentru găsirea zborurilor, rezervarea hotelurilor și a mașinilor de închiriat trebuie să comunice și să împărtășească informații despre preferințele și constrângerile utilizatorului. Trebuie să decideți protocoalele și metodele pentru această comunicare. Ce înseamnă aceasta concret este că agentul pentru găsirea zborurilor trebuie să comunice cu agentul pentru rezervarea hotelurilor pentru a se asigura că hotelul este rezervat pentru aceleași date ca zborul. Asta înseamnă că agenții trebuie să împărtășească informații despre datele de călătorie ale utilizatorului, ceea ce înseamnă că trebuie să decideți *care agenți partajează informații și cum partajează informațiile*.
- **Mecanisme de coordonare**: Agenții trebuie să își coordoneze acțiunile pentru a se asigura că preferințele și constrângerile utilizatorului sunt îndeplinite. O preferință a utilizatorului ar putea fi că dorește un hotel aproape de aeroport, în timp ce o constrângere ar putea fi că mașinile de închiriat sunt disponibile doar la aeroport. Asta înseamnă că agentul pentru rezervarea hotelurilor trebuie să se coordoneze cu agentul pentru rezervarea mașinilor de închiriat pentru a se asigura că preferințele și constrângerile utilizatorului sunt îndeplinite. Asta înseamnă că trebuie să decideți *cum se coordonează agenții acțiunile lor*.
- **Arhitectura agentului**: Agenții trebuie să aibă structura internă pentru a lua decizii și a învăța din interacțiunile lor cu utilizatorul. Aceasta înseamnă că agentul pentru găsirea zborurilor trebuie să aibă structura internă pentru a lua decizii despre ce zboruri să recomande utilizatorului. Asta înseamnă că trebuie să decideți *cum iau agenții decizii și cum învață din interacțiunile lor cu utilizatorul*. Exemple de cum învață și se îmbunătățesc agenții ar putea fi că agentul pentru găsirea zborurilor ar putea folosi un model de învățare automată pentru a recomanda zboruri utilizatorului pe baza preferințelor anterioare.
- **Vizibilitate asupra interacțiunilor multi-agent**: Trebuie să aveți vizibilitate asupra modului în care agenții multipli interacționează între ei. Aceasta înseamnă că trebuie să aveți instrumente și tehnici pentru urmărirea activităților și interacțiunilor agenților. Acest lucru ar putea fi sub forma instrumentelor de logare și monitorizare, instrumentelor de vizualizare și a metricilor de performanță.
- **Modele multi-agent**: Există diferite modele pentru implementarea sistemelor multi-agent, cum ar fi arhitecturi centralizate, descentralizate și hibride. Trebuie să decideți modelul care se potrivește cel mai bine cazului dvs. de utilizare.
- **Omul în buclă**: În majoritatea cazurilor, veți avea un om în buclă și trebuie să instruiți agenții când să solicite intervenția umană. Acest lucru ar putea fi sub forma unui utilizator care cere un anumit hotel sau zbor pe care agenții nu l-au recomandat sau solicită confirmarea înainte de a rezerva un zbor sau un hotel.

## Vizibilitate asupra interacțiunilor multi-agent

Este important să aveți vizibilitate asupra modului în care agenții multipli interacționează între ei. Această vizibilitate este esențială pentru depanare, optimizare și asigurarea eficacității generale a sistemului. Pentru a realiza acest lucru, trebuie să aveți instrumente și tehnici pentru urmărirea activităților și interacțiunilor agenților. Acest lucru ar putea fi sub forma instrumentelor de logare și monitorizare, instrumentelor de vizualizare și a metricilor de performanță.

De exemplu, în cazul rezervării unei călătorii pentru un utilizator, ați putea avea un tablou de bord care arată starea fiecărui agent, preferințele și constrângerile utilizatorului și interacțiunile dintre agenți. Acest tablou de bord ar putea afișa datele de călătorie ale utilizatorului, zborurile recomandate de agentul de zbor, hotelurile recomandate de agentul de hotel și mașinile de închiriat recomandate de agentul de închirieri auto. Acest lucru v-ar oferi o vedere clară asupra modului în care agenții interacționează între ei și dacă preferințele și constrângerile utilizatorului sunt îndeplinite.

Să analizăm fiecare dintre aceste aspecte în detaliu.

- **Instrumente de logare și monitorizare**: Doriți să aveți logare pentru fiecare acțiune întreprinsă de un agent. O intrare în jurnal ar putea stoca informații despre agentul care a întreprins acțiunea, acțiunea întreprinsă, momentul în care a fost întreprinsă acțiunea și rezultatul acțiunii. Aceste informații pot fi utilizate ulterior pentru depanare, optimizare și altele.
- **Instrumente de vizualizare**: Instrumentele de vizualizare vă pot ajuta să vedeți interacțiunile dintre agenți într-un mod mai intuitiv. De exemplu, ați putea avea un grafic care arată fluxul de informații între agenți. Acest lucru v-ar putea ajuta să identificați blocaje, ineficiențe și alte probleme în sistem.
- **Metrici de performanță**: Metricile de performanță vă pot ajuta să urmăriți eficacitatea sistemului multi-agent. De exemplu, ați putea urmări timpul necesar pentru a finaliza o sarcină, numărul de sarcini finalizate pe unitatea de timp și acuratețea recomandărilor făcute de agenți. Aceste informații vă pot ajuta să identificați zonele pentru îmbunătățire și să optimizați sistemul.

## Modele multi-agent

Să analizăm câteva modele concrete pe care le putem folosi pentru a crea aplicații multi-agent. Iată câteva modele interesante demne de luat în considerare:

### Chat de grup

Acest model este util când doriți să creați o aplicație de chat de grup în care mai mulți agenți pot comunica între ei. Cazuri tipice de utilizare pentru acest model includ colaborarea în echipă, suportul pentru clienți și rețelele sociale.

În acest model, fiecare agent reprezintă un utilizator în chatul de grup, iar mesajele sunt schimbate între agenți folosind un protocol de mesagerie. Agenții pot trimite mesaje în chatul de grup, pot primi mesaje din chatul de grup și pot răspunde la mesajele altor agenți.

Acest model poate fi implementat folosind o arhitectură centralizată, unde toate mesajele sunt rutate printr-un server central, sau o arhitectură descentralizată, în care mesajele sunt schimbate direct.

![Chat de grup](../../../translated_images/ro/multi-agent-group-chat.ec10f4cde556babd.webp)

### Transfer de sarcini

Acest model este util când doriți să creați o aplicație în care mai mulți agenți pot transfera sarcini între ei.

Cazuri tipice de utilizare pentru acest model includ suportul pentru clienți, gestionarea sarcinilor și automatizarea fluxurilor de lucru.

În acest model, fiecare agent reprezintă o sarcină sau un pas într-un flux de lucru, iar agenții pot transfera sarcini către alți agenți pe baza unor reguli predefinite.

![Hand off](../../../translated_images/ro/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtrare colaborativă

Acest model este util când doriți să creați o aplicație în care mai mulți agenți pot colabora pentru a face recomandări utilizatorilor.

Motivul pentru care ați dori ca mai mulți agenți să colaboreze este că fiecare agent poate avea expertiză diferită și poate contribui la procesul de recomandare în moduri diferite.

Să luăm un exemplu în care un utilizator dorește o recomandare pentru cea mai bună acțiune de cumpărat pe piața de capital.

- **Expert în industrie**: Un agent ar putea fi expert într-o industrie specifică.
- **Analiză tehnică**: Un alt agent ar putea fi expert în analiză tehnică.
- **Analiză fundamentală**: și un alt agent ar putea fi expert în analiză fundamentală. Prin colaborare, acești agenți pot oferi o recomandare mai cuprinzătoare utilizatorului.

![Recomandare](../../../translated_images/ro/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenariu: Proces de rambursare

Luați în considerare un scenariu în care un client încearcă să obțină o rambursare pentru un produs; pot fi implicați destul de mulți agenți în acest proces, dar să-i împărțim între agenți specifici pentru acest proces și agenți generali care pot fi folosiți în alte procese.

**Agenți specifici pentru procesul de rambursare**:

Următorii sunt câțiva agenți care ar putea fi implicați în procesul de rambursare:

- **Agent client**: Acest agent reprezintă clientul și este responsabil pentru inițierea procesului de rambursare.
- **Agent vânzător**: Acest agent reprezintă vânzătorul și este responsabil pentru procesarea rambursării.
- **Agent de plată**: Acest agent reprezintă procesul de plată și este responsabil pentru returnarea plății clientului.
- **Agent de rezoluție**: Acest agent reprezintă procesul de rezolvare și este responsabil pentru rezolvarea oricăror probleme care apar în timpul procesului de rambursare.
- **Agent de conformitate**: Acest agent reprezintă procesul de conformitate și este responsabil pentru a se asigura că procesul de rambursare respectă reglementările și politicile.

**Agenți generali**:

Acești agenți pot fi utilizați și în alte părți ale afacerii dvs.

- **Agent de expediere**: Acest agent reprezintă procesul de expediere și este responsabil pentru expedierea produsului înapoi către vânzător. Acest agent poate fi folosit atât pentru procesul de rambursare, cât și pentru expedierea generală a unui produs în urma unei achiziții, de exemplu.
- **Agent de feedback**: Acest agent reprezintă procesul de colectare a feedback-ului și este responsabil pentru colectarea feedback-ului de la client. Feedback-ul poate fi obținut în orice moment, nu doar în timpul procesului de rambursare.
- **Agent de escaladare**: Acest agent reprezintă procesul de escaladare și este responsabil pentru escaladarea problemelor către un nivel superior de suport. Puteți folosi acest tip de agent pentru orice proces în care trebuie să escaladați o problemă.
- **Agent de notificare**: Acest agent reprezintă procesul de notificare și este responsabil pentru trimiterea notificărilor către client în diferite etape ale procesului de rambursare.
- **Agent de analiză**: Acest agent reprezintă procesul de analiză și este responsabil pentru analizarea datelor legate de procesul de rambursare.
- **Agent de audit**: Acest agent reprezintă procesul de audit și este responsabil pentru auditarea procesului de rambursare pentru a se asigura că acesta este efectuat corect.
- **Agent de raportare**: Acest agent reprezintă procesul de raportare și este responsabil pentru generarea de rapoarte privind procesul de rambursare.
- **Agent de cunoștințe**: Acest agent reprezintă procesul de gestionare a cunoștințelor și este responsabil pentru menținerea unei baze de cunoștințe cu informații legate de procesul de rambursare. Acest agent ar putea fi informat atât despre rambursări, cât și despre alte părți ale afacerii dvs.
- **Agent de securitate**: Acest agent reprezintă procesul de securitate și este responsabil pentru asigurarea securității procesului de rambursare.
- **Agent de calitate**: Acest agent reprezintă procesul de asigurare a calității și este responsabil pentru asigurarea calității procesului de rambursare.

Există destul de mulți agenți enumerați anterior, atât pentru procesul specific de rambursare, cât și pentru agenții generali care pot fi folosiți în alte părți ale afacerii dvs. Sperăm că acest lucru vă oferă o idee despre cum puteți decide ce agenți să utilizați în sistemul dvs. multi-agent.

## Sarcină

Proiectați un sistem multi-agent pentru un proces de suport clienți. Identificați agenții implicați în proces, rolurile și responsabilitățile lor și modul în care interacționează între ei. Luați în considerare atât agenții specifici procesului de suport clienți, cât și agenții generali care pot fi folosiți în alte părți ale afacerii dvs.
> Gândește-te înainte de a citi soluția următoare; ai putea avea nevoie de mai mulți agenți decât crezi.
> SFAT: Gândește-te la diferitele etape ale procesului de suport pentru clienți și ia în considerare agenții necesari pentru orice sistem.

## Solution

[Solution](./solution/solution.md)

## Verificări ale cunoștințelor

Question: When should you consider using multi-agents?

- [ ] A1: Când ai o încărcătură de lucru mică și o sarcină simplă.
- [ ] A2: Când ai o încărcătură de lucru mare
- [ ] A3: Când ai o sarcină simplă.

[Solution quiz](./solution/solution-quiz.md)

## Summary

În această lecție, am analizat tiparul de proiectare cu mai mulți agenți, inclusiv scenariile în care se aplică, avantajele utilizării mai multor agenți în locul unui singur agent, elementele de bază pentru implementarea tiparului de proiectare multi-agent și modul în care poți avea vizibilitate asupra modului în care mai mulți agenți interacționează între ei.

### Got More Questions about the Multi-Agent Design Pattern?

Alătură-te the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la orele de birou și a obține răspunsuri la întrebările tale despre agenți AI.

## Additional resources

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Documentația Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Tipare de proiectare agentică</a>


## Previous Lesson

[Planning Design](../07-planning-design/README.md)

## Next Lesson

[Metacognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:
Acest document a fost tradus cu ajutorul serviciului de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa de origine, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă o traducere profesională realizată de un traducător uman. Nu ne asumăm nicio răspundere pentru eventuale neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->