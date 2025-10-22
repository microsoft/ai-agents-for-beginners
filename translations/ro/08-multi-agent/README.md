<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T20:51:37+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "ro"
}
-->
[![Design Multi-Agent](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.ro.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Modele de design multi-agent

De îndată ce începeți să lucrați la un proiect care implică mai mulți agenți, va trebui să luați în considerare modelul de design multi-agent. Totuși, poate să nu fie imediat clar când să treceți la utilizarea mai multor agenți și care sunt avantajele acestora.

## Introducere

În această lecție, ne propunem să răspundem la următoarele întrebări:

- Care sunt scenariile în care sunt aplicabili agenții multipli?
- Care sunt avantajele utilizării mai multor agenți în comparație cu un singur agent care îndeplinește mai multe sarcini?
- Care sunt elementele de bază pentru implementarea modelului de design multi-agent?
- Cum putem avea vizibilitate asupra modului în care interacționează agenții multipli între ei?

## Obiective de învățare

După această lecție, ar trebui să puteți:

- Identifica scenariile în care sunt aplicabili agenții multipli.
- Recunoaște avantajele utilizării mai multor agenți în comparație cu un singur agent.
- Înțelege elementele de bază ale implementării modelului de design multi-agent.

Care este imaginea de ansamblu?

*Agenții multipli reprezintă un model de design care permite mai multor agenți să colaboreze pentru a atinge un scop comun.*

Acest model este utilizat pe scară largă în diverse domenii, inclusiv robotică, sisteme autonome și calcul distribuit.

## Scenarii în care sunt aplicabili agenții multipli

Deci, în ce scenarii este utilă utilizarea agenților multipli? Răspunsul este că există multe situații în care utilizarea mai multor agenți este benefică, în special în următoarele cazuri:

- **Sarcini mari**: Sarcinile mari pot fi împărțite în sarcini mai mici și atribuite diferiților agenți, permițând procesarea în paralel și finalizarea mai rapidă. Un exemplu este procesarea unui volum mare de date.
- **Sarcini complexe**: Sarcinile complexe, la fel ca cele mari, pot fi împărțite în subtasks mai mici și atribuite diferiților agenți, fiecare specializat într-un anumit aspect al sarcinii. Un exemplu bun este cazul vehiculelor autonome, unde diferiți agenți gestionează navigația, detectarea obstacolelor și comunicarea cu alte vehicule.
- **Expertiză diversă**: Agenții diferiți pot avea expertiză diversă, permițându-le să gestioneze diferite aspecte ale unei sarcini mai eficient decât un singur agent. Un exemplu bun este în domeniul sănătății, unde agenții pot gestiona diagnostice, planuri de tratament și monitorizarea pacienților.

## Avantajele utilizării agenților multipli în comparație cu un singur agent

Un sistem cu un singur agent ar putea funcționa bine pentru sarcini simple, dar pentru sarcini mai complexe, utilizarea mai multor agenți poate oferi mai multe avantaje:

- **Specializare**: Fiecare agent poate fi specializat pentru o anumită sarcină. Lipsa specializării într-un singur agent înseamnă că acesta poate face totul, dar s-ar putea să se încurce atunci când se confruntă cu o sarcină complexă. De exemplu, ar putea ajunge să îndeplinească o sarcină pentru care nu este cel mai potrivit.
- **Scalabilitate**: Este mai ușor să scalați sistemele prin adăugarea mai multor agenți decât prin supraîncărcarea unui singur agent.
- **Toleranță la erori**: Dacă un agent eșuează, ceilalți pot continua să funcționeze, asigurând fiabilitatea sistemului.

Să luăm un exemplu: să rezervăm o călătorie pentru un utilizator. Un sistem cu un singur agent ar trebui să gestioneze toate aspectele procesului de rezervare, de la găsirea zborurilor până la rezervarea hotelurilor și a mașinilor de închiriat. Pentru a realiza acest lucru cu un singur agent, acesta ar trebui să aibă instrumente pentru a gestiona toate aceste sarcini. Acest lucru ar putea duce la un sistem complex și monolitic, dificil de întreținut și scalat. Un sistem multi-agent, pe de altă parte, ar putea avea agenți diferiți specializați în găsirea zborurilor, rezervarea hotelurilor și a mașinilor de închiriat. Acest lucru ar face sistemul mai modular, mai ușor de întreținut și scalabil.

Comparați acest lucru cu o agenție de turism condusă ca un magazin de familie versus o agenție de turism condusă ca o franciză. Magazinul de familie ar avea un singur agent care gestionează toate aspectele procesului de rezervare, în timp ce franciza ar avea agenți diferiți care gestionează diferite aspecte ale procesului.

## Elemente de bază ale implementării modelului de design multi-agent

Înainte de a putea implementa modelul de design multi-agent, trebuie să înțelegeți elementele de bază care compun acest model.

Să facem acest lucru mai concret, analizând din nou exemplul rezervării unei călătorii pentru un utilizator. În acest caz, elementele de bază ar include:

- **Comunicarea între agenți**: Agenții pentru găsirea zborurilor, rezervarea hotelurilor și a mașinilor de închiriat trebuie să comunice și să partajeze informații despre preferințele și constrângerile utilizatorului. Trebuie să decideți protocoalele și metodele pentru această comunicare. Concret, aceasta înseamnă că agentul pentru găsirea zborurilor trebuie să comunice cu agentul pentru rezervarea hotelurilor pentru a se asigura că hotelul este rezervat pentru aceleași date ca zborul.
- **Mecanisme de coordonare**: Agenții trebuie să-și coordoneze acțiunile pentru a se asigura că preferințele și constrângerile utilizatorului sunt respectate. O preferință a utilizatorului ar putea fi să aibă un hotel aproape de aeroport, în timp ce o constrângere ar putea fi că mașinile de închiriat sunt disponibile doar la aeroport.
- **Arhitectura agenților**: Agenții trebuie să aibă o structură internă pentru a lua decizii și a învăța din interacțiunile cu utilizatorul. Aceasta înseamnă că agentul pentru găsirea zborurilor trebuie să aibă o structură internă pentru a lua decizii despre ce zboruri să recomande utilizatorului.
- **Vizibilitate asupra interacțiunilor multi-agent**: Trebuie să aveți vizibilitate asupra modului în care agenții multipli interacționează între ei. Aceasta înseamnă că trebuie să aveți instrumente și tehnici pentru a urmări activitățile și interacțiunile agenților.
- **Modele multi-agent**: Există diferite modele pentru implementarea sistemelor multi-agent, cum ar fi arhitecturile centralizate, descentralizate și hibride. Trebuie să decideți modelul care se potrivește cel mai bine cazului dvs. de utilizare.
- **Omul în buclă**: În majoritatea cazurilor, veți avea un om în buclă și trebuie să instruiți agenții când să solicite intervenția umană.

## Vizibilitate asupra interacțiunilor multi-agent

Este important să aveți vizibilitate asupra modului în care agenții multipli interacționează între ei. Această vizibilitate este esențială pentru depanare, optimizare și asigurarea eficienței generale a sistemului. Pentru a realiza acest lucru, trebuie să aveți instrumente și tehnici pentru a urmări activitățile și interacțiunile agenților.

De exemplu, în cazul rezervării unei călătorii pentru un utilizator, ați putea avea un tablou de bord care să arate starea fiecărui agent, preferințele și constrângerile utilizatorului și interacțiunile dintre agenți. Acest tablou de bord ar putea arăta datele de călătorie ale utilizatorului, zborurile recomandate de agentul de zboruri, hotelurile recomandate de agentul de hoteluri și mașinile de închiriat recomandate de agentul de închirieri auto. Acest lucru v-ar oferi o imagine clară asupra modului în care agenții interacționează între ei și dacă preferințele și constrângerile utilizatorului sunt respectate.

Să analizăm fiecare dintre aceste aspecte mai în detaliu.

- **Instrumente de logare și monitorizare**: Doriți să aveți loguri pentru fiecare acțiune întreprinsă de un agent. O intrare în log ar putea stoca informații despre agentul care a întreprins acțiunea, acțiunea întreprinsă, timpul la care a fost întreprinsă acțiunea și rezultatul acesteia.
- **Instrumente de vizualizare**: Instrumentele de vizualizare vă pot ajuta să vedeți interacțiunile dintre agenți într-un mod mai intuitiv. De exemplu, ați putea avea un grafic care să arate fluxul de informații dintre agenți.
- **Metrici de performanță**: Metricile de performanță vă pot ajuta să urmăriți eficiența sistemului multi-agent. De exemplu, ați putea urmări timpul necesar pentru a finaliza o sarcină, numărul de sarcini finalizate pe unitatea de timp și acuratețea recomandărilor făcute de agenți.

## Modele multi-agent

Să explorăm câteva modele concrete pe care le putem folosi pentru a crea aplicații multi-agent. Iată câteva modele interesante care merită luate în considerare:

### Chat de grup

Acest model este util atunci când doriți să creați o aplicație de chat de grup în care mai mulți agenți pot comunica între ei. Cazuri de utilizare tipice pentru acest model includ colaborarea în echipă, suportul pentru clienți și rețelele sociale.

În acest model, fiecare agent reprezintă un utilizator în chatul de grup, iar mesajele sunt schimbate între agenți folosind un protocol de mesagerie. Agenții pot trimite mesaje în chatul de grup, primi mesaje din chatul de grup și răspunde mesajelor altor agenți.

Acest model poate fi implementat folosind o arhitectură centralizată, în care toate mesajele sunt direcționate printr-un server central, sau o arhitectură descentralizată, în care mesajele sunt schimbate direct.

![Chat de grup](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.ro.png)

### Predare de sarcini

Acest model este util atunci când doriți să creați o aplicație în care mai mulți agenți pot preda sarcini unul altuia.

Cazuri de utilizare tipice pentru acest model includ suportul pentru clienți, gestionarea sarcinilor și automatizarea fluxurilor de lucru.

În acest model, fiecare agent reprezintă o sarcină sau un pas într-un flux de lucru, iar agenții pot preda sarcini altor agenți pe baza unor reguli predefinite.

![Predare de sarcini](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.ro.png)

### Filtrare colaborativă

Acest model este util atunci când doriți să creați o aplicație în care mai mulți agenți pot colabora pentru a face recomandări utilizatorilor.

De ce ați dori ca mai mulți agenți să colaboreze? Pentru că fiecare agent poate avea o expertiză diferită și poate contribui la procesul de recomandare în moduri diferite.

Să luăm un exemplu în care un utilizator dorește o recomandare pentru cea mai bună acțiune de cumpărat pe piața bursieră.

- **Expert în industrie**: Un agent ar putea fi expert într-o anumită industrie.
- **Analiză tehnică**: Un alt agent ar putea fi expert în analiza tehnică.
- **Analiză fundamentală**: Un alt agent ar putea fi expert în analiza fundamentală. Prin colaborare, acești agenți pot oferi o recomandare mai cuprinzătoare utilizatorului.

![Recomandare](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.ro.png)

## Scenariu: Procesul de rambursare

Luați în considerare un scenariu în care un client încearcă să obțină o rambursare pentru un produs. Pot exista destul de mulți agenți implicați în acest proces, dar să-i împărțim între agenți specifici pentru acest proces și agenți generali care pot fi utilizați în alte procese.

**Agenți specifici pentru procesul de rambursare**:

Următorii sunt câțiva agenți care ar putea fi implicați în procesul de rambursare:

- **Agentul clientului**: Acest agent reprezintă clientul și este responsabil pentru inițierea procesului de rambursare.
- **Agentul vânzătorului**: Acest agent reprezintă vânzătorul și este responsabil pentru procesarea rambursării.
- **Agentul de plăți**: Acest agent reprezintă procesul de plată și este responsabil pentru rambursarea plății clientului.
- **Agentul de rezolvare**: Acest agent reprezintă procesul de rezolvare și este responsabil pentru rezolvarea oricăror probleme care apar în timpul procesului de rambursare.
- **Agentul de conformitate**: Acest agent reprezintă procesul de conformitate și este responsabil pentru asigurarea faptului că procesul de rambursare respectă reglementările și politicile.

**Agenți generali**:

Acești agenți pot fi utilizați în alte părți ale afacerii dvs.

- **Agentul de expediere**: Acest agent reprezintă procesul de expediere și este responsabil pentru expedierea produsului înapoi la vânzător. Acest agent poate fi utilizat atât pentru procesul de rambursare, cât și pentru expedierea generală a unui produs, de exemplu, în cazul unei achiziții.
- **Agentul de feedback**: Acest agent reprezintă procesul de feedback și este responsabil pentru colectarea feedback-ului de la client. Feedback-ul poate fi colectat în orice moment, nu doar în timpul procesului de rambursare.
- **Agentul de escaladare**: Acest agent reprezintă procesul de escaladare și este responsabil pentru escaladarea problemelor la un nivel superior de suport. Puteți utiliza acest tip de agent pentru orice proces în care trebuie să escaladați o problemă.
- **Agentul de notificare**: Acest agent reprezintă procesul de notificare și este responsabil pentru trimiterea notificărilor către client în diferite etape ale procesului de rambursare.
- **Agentul de analiză**: Acest agent reprezintă procesul de analiză și este responsabil pentru analizarea datelor legate de procesul de rambursare.
- **Agentul de audit**: Acest agent reprezintă procesul de audit și este responsabil pentru auditarea procesului de rambursare pentru a se asigura că este realizat corect.
- **Agentul de raportare**: Acest agent reprezintă procesul de raportare și este responsabil pentru generarea de rapoarte despre procesul de rambursare.
- **Agentul de cunoștințe**: Acest agent reprezintă procesul de cunoștințe și este responsabil pentru menținerea unei baze de cunoștințe despre informațiile legate de procesul de rambursare. Acest agent ar putea fi informat atât despre rambursări, cât și despre alte părți ale afacerii dvs.
- **Agentul de securitate**: Acest agent reprezintă procesul de securitate și este responsabil pentru asigurarea securității procesului de rambursare.
- **Agentul de calitate**: Acest agent reprezintă procesul de calitate și este responsabil pentru asigurarea calității procesului de rambursare.

Există destul de mulți agenți enumerați anterior, atât pentru procesul specific de rambursare, cât și pentru agenții generali care pot fi utilizați în alte părți ale afacerii dvs. Sperăm că acest lucru vă oferă o idee despre cum puteți decide ce agenți să utilizați în sistemul dvs. multi-agent.

## Sarcină
## Proiectarea unui sistem multi-agent pentru un proces de suport clienți

Identificați agenții implicați în proces, rolurile și responsabilitățile lor, precum și modul în care interacționează între ei. Luați în considerare atât agenții specifici procesului de suport clienți, cât și agenții generali care pot fi utilizați în alte părți ale afacerii.

> Gândiți-vă bine înainte de a citi soluția de mai jos, este posibil să aveți nevoie de mai mulți agenți decât credeți.

> TIP: Gândiți-vă la diferitele etape ale procesului de suport clienți și luați în considerare și agenții necesari pentru orice sistem.

## Soluție

[Soluție](./solution/solution.md)

## Verificări de cunoștințe

Întrebare: Când ar trebui să luați în considerare utilizarea mai multor agenți?

- [ ] A1: Când aveți un volum mic de muncă și o sarcină simplă.
- [ ] A2: Când aveți un volum mare de muncă.
- [ ] A3: Când aveți o sarcină simplă.

[Quiz soluție](./solution/solution-quiz.md)

## Rezumat

În această lecție, am analizat modelul de proiectare multi-agent, inclusiv scenariile în care sunt aplicabili mai mulți agenți, avantajele utilizării mai multor agenți în comparație cu un agent singular, elementele de bază ale implementării modelului de proiectare multi-agent și cum să aveți vizibilitate asupra modului în care interacționează agenții între ei.

### Aveți mai multe întrebări despre modelul de proiectare multi-agent?

Alăturați-vă [Discordului Azure AI Foundry](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la ore de consultanță și a obține răspunsuri la întrebările dvs. despre agenții AI.

## Resurse suplimentare

- ## Lecția anterioară

[Proiectarea planificării](../07-planning-design/README.md)

## Lecția următoare

[Metacogniția în agenții AI](../09-metacognition/README.md)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.