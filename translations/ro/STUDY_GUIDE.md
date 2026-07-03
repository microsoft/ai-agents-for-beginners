# Agenți AI pentru Începători - Ghid de Studiu

Folosește acest ghid ca un companion practic pe parcursul cursului. Nu este
conceput să înlocuiască lecțiile. Te ajută să decizi de unde să începi, ce să
cauți în fiecare lecție și cum să conectezi ideile într-un mic demo funcțional de
agent.

Dacă este prima ta dată aici, începe simplu:

1. Citește [Configurarea Cursului](./00-course-setup/README.md).
2. Completează lecțiile 01-06 în ordine.
3. Ține în minte o mică idee de demo pe măsură ce înveți.
4. După fiecare lecție, întreabă-te: „Ce poate face agentul meu acum ce nu putea
   face înainte?”

## Un Demo Simplu de Ținut Minte

Un mod bun de a învăța despre agenți este să urmezi o singură idee de demo pe
tot parcursul cursului.

Exemplu demo: **un agent ajutător pentru curs**.

Utilizatorul întreabă:

> „Vreau să învăț cum folosesc agenții unelte. Găsește lecțiile potrivite,
> rezumă ce ar trebui să citesc mai întâi și dă-mi o sarcină scurtă de practică.”

Un chatbot obișnuit poate răspunde din ce știe deja. Un agent poate face mai
mult:

1. **Citește sau caută în fișierele cursului** pentru a găsi lecțiile potrivite.
2. **Folosește unelte** pentru a obține linkuri către lecții, exemple sau materiale
   suport.
3. **Planifică** un traseu scurt de învățare în loc să ofere un răspuns lung.
4. **Folosește contextul** din conversația curentă pentru a rămâne concentrat pe
   obiectivul învățăcelului.
5. **Amintește-și preferințe utile** dacă aplicația suportă memorie.
6. **Arată urme, citări sau jurnale** astfel încât utilizatorul să înțeleagă ce s-a
   întâmplat.
7. **Aplică măsuri de siguranță** înainte de a face acțiuni riscante sau de a folosi
   date sensibile.

Pe măsură ce studiezi fiecare lecție, revino la acest demo și întreabă-te: ce
capacitate nouă aduce această lecție?

## Către Ce Construiești

La finalul cursului, ar trebui să poți explica și construi sisteme de agenți care
combină aceste părți:

| Parte | Semnificație în limbaj simplu | În demo |
|-------|------------------------------|---------|
| Model | Motorul de raționament care interpretează cererea utilizatorului | Înțelege că învățăcelul vrea lecții despre utilizarea uneltelor |
| Unelte | Funcții, API-uri, fișiere, browsere sau servicii pe care agentul le poate
folosi | Caută în depozit sau preia conținutul lecțiilor |
| Cunoaștere | Documente sau date folosite pentru a fundamenta răspunsul | Fișiere README ale cursului și materiale de lecție |
| Context | Informație inclusă în următorul apel la model | Obiectivul utilizatorului și rezultatele uneltelor |
| Memorie | Informație salvată pentru utilizare ulterioară | Preferința învățăcelului pentru exemple practice în Python |
| Planificare | Împărțirea unui obiectiv mare în pași mai mici | Găsește lecții, rezumă-le, sugerează practică |
| Orchestrare | Direcționarea muncii între unelte, pași sau agenți | Un planificator apelează o unealtă de căutare, apoi un rezumator |
| Încredere | Siguranță, securitate, evaluare și observabilitate | Înregistrează apeluri de unelte și cere permisiune pentru acțiuni cu impact mare |

## Alege-ți Traseul de Învățare

Poți parcurge cursul complet în ordine sau să sari la un traseu în funcție de ce
vrei să construiești.

| Dacă obiectivul tău este să... | Începe cu | Apoi studiază |
|-------------------------------|-----------|---------------|
| Înțelegi ce sunt agenții | 01, 02, 03 | 04, 05, 06 |
| Construiești un agent care folosește unelte | 04 | 05, 07, 14 |
| Construiești un agent bazat pe RAG | 05 | 04, 06, 12 |
| Projetezi fluxuri de lucru multi-pași | 07 | 08, 09, 14 |
| Înțelegi sisteme multi-agent | 08 | 07, 09, 11 |
| Pregătești agenți pentru producție | 06, 10 | 12, 13, 18 |
| Explorezi protocoale și automatizare browser | 11, 15 | 10, 18 |

Sfat: dacă ești nou cu agenții, nu sări peste lecțiile 01-06. Ele îți oferă
vocabularul necesar pentru restul cursului.

## Ghid Lecție cu Lecție

| Lecție | Ce înveți | Încearcă asta după lecție |
|--------|-----------|--------------------------|
| [01 - Introducere în Agenți AI](./01-intro-to-ai-agents/README.md) | Ce face un agent diferit de un chatbot obișnuit. | Explică-ți ideea de demo ca agent, nu doar ca aplicație de chat. |
| [02 - Framework-uri Agentice](./02-explore-agentic-frameworks/README.md) | Cum framework-urile ajută cu modele, unelte, stare și fluxuri. | Identifică ce părți ale demo-ului ar gestiona un framework. |
| [03 - Tipare de Design Agentic](./03-agentic-design-patterns/README.md) | Tipare comune pentru a proiecta comportamentul agentului. | Schițează traseul utilizatorului înainte să scrii cod. |
| [04 - Utilizarea Uneltelor](./04-tool-use/README.md) | Cum agenții apelează unelte pentru a obține date sau a acționa. | Definește o unealtă de care agentul tău în demo ar avea nevoie. |
| [05 - RAG Agentic](./05-agentic-rag/README.md) | Cum extragerea de informații fundamentează răspunsurile agentului. | Decide ce sursă de cunoaștere ar trebui să caute demo-ul tău. |
| [06 - Agenți Demni de Încredere](./06-building-trustworthy-agents/README.md) | Cum să adaugi măsuri de siguranță, supraveghere și comportament mai sigur. | Adaugă o regulă când agentul ar trebui să ceară mai întâi utilizatorului. |
| [07 - Design de Planificare](./07-planning-design/README.md) | Cum agenții împart obiective mari în pași mai mici. | Scrie un plan în trei pași pentru cererea demo-ului tău. |
| [08 - Design Multi-Agent](./08-multi-agent/README.md) | Când să împarți munca între agenți specializați. | Decide dacă demo-ul tău are nevoie de un singur agent sau mai mulți. |
| [09 - Metacogniție](./09-metacognition/README.md) | Cum agenții pot revizui și îmbunătăți propriile rezultate. | Adaugă un pas final de auto-verificare înainte ca agentul să răspundă. |
| [10 - Agenți AI în Producție](./10-ai-agents-production/README.md) | Ce se schimbă când un agent trece din demo în producție. | Listează ce ai monitoriza: calitate, cost, latență, eșecuri. |
| [11 - Protocoale Agentice](./11-agentic-protocols/README.md) | Cum protocoalele conectează agenții la unelte și alți agenți. | Identifică unde un protocol standard ar putea simplifica integrarea. |
| [12 - Ingineria Contextului](./12-context-engineering/README.md) | Cum să selectezi, tai, izolezi și gestionezi contextul. | Decide ce merită în prompt și ce ar trebui exclus. |
| [13 - Memoria Agentului](./13-agent-memory/README.md) | Cum agenții pot salva informații utile între interacțiuni. | Alege o preferință sigură pe care demo-ul tău ar putea să o țină minte. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Blocuri specifice pentru framework pentru agenți și fluxuri de lucru. | Potrivește pașii demo-ului cu conceptele framework-ului. |
| [15 - Agenți care folosesc Calculatorul](./15-browser-use/README.md) | Cum agenții pot interacționa cu browserul sau UI. | Alege o sarcină browser care tot trebuie să solicite confirmare umană. |
| [18 - Securizarea Agenților AI](./18-securing-ai-agents/README.md) | Cum să faci acțiunile agentului auditate și protejate. | Decide ce acțiuni în demo ar trebui înregistrate sau confirmate. |

Lecțiile 16 și 17 sunt menționate în README principal ca fiind în curs de
publicare. Adaugă-le în planul tău de studiu când conținutul va fi disponibil.

## Idei Cheie în Termeni Prietenoși pentru Începători

### Unelte

O unealtă este ceva ce agentul poate apela pentru a face muncă în afara modelului.
O unealtă bună are un nume clar, o sarcină restrânsă, intrări tipizate, un output
predictibil și un mod sigur de a eșua.

Pentru demo-ul de agent ajutător pentru curs, o unealtă ar putea fi:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG și Cunoaștere

RAG ajută agentul să răspundă din materialul sursă în loc să ghicească. În
acest curs, materialul sursă pot fi README-urile lecțiilor, exemple de cod sau
resurse externe legate din lecții.

Folosește RAG când răspunsul trebuie fundamentat pe documente, date sau fișiere
curente din proiect.

### Planificare

Planificarea este utilă când cererea are mai mulți pași. Păstrează planurile
scurte și suficient de vizibile pentru ca un dezvoltator sau utilizator să
inspecteze.

Pentru demo, un plan ar putea fi:

1. Găsește lecțiile legate de utilizarea uneltelor.
2. Rezumă cele mai relevante lecții.
3. Recomandă o sarcină practică.

### Context

Contextul este ce vede modelul acum. Prea puțin context poate determina agentul să
rateze detalii importante. Prea mult context poate încetini agentul, crește costul
sau favoriza confuzii.

Ingineria bună a contextului înseamnă să alegi informația potrivită pentru următorul
apel la model.

### Memorie

Memoria este informația salvată pentru mai târziu. Nu salva totul. Salvează doar
informația care este utilă, sigură și ușor de actualizat sau șters.

De exemplu, a reține „învățăcelul preferă exemple Python” poate fi util. A
reteni date personale sensibile de obicei nu.

### Evaluare și Observabilitate

Evaluarea întreabă: agentul a făcut ce trebuie?

Observabilitatea întreabă: putem vedea cum s-a întâmplat?

Pentru agenții din producție, urmărește apelurile modelului, apelurile uneltelor,
contextul folosit, latența, costul, eșecurile și feedbackul utilizatorilor.

### Încredere și Securitate

Agenții demni de încredere au nevoie de mai mult decât un prompt de ajutor. Folosește
unelte cu privilegii minime, aprobare umană pentru acțiuni cu impact mare,
redactare de date când este nevoie și jurnale sau chitanțe pentru acțiuni care
trebuie auditate.

## O Rutina de Recapitulare de 15 Minute

Folosește această rutină după fiecare lecție:

1. **Rezuma lecția într-o propoziție.**
2. **Denumeste noua capacitate a agentului.** De exemplu: folosirea uneltelor,
   extragere, planificare, memorie, observabilitate sau securitate.
3. **Adaug-o la demo-ul de ajutor pentru curs.** Ce se schimbă acum în demo?
4. **Găsește riscul.** Ce s-ar putea întâmpla rău dacă această capacitate este
   folosită greșit?
5. **Scrie o întrebare de test.** Cum ai verifica că agentul se comportă corect?

## Verificare Rapidă

Înainte de a continua, încearcă să răspunzi la aceste întrebări:

1. Ce poate face un agent ce un chatbot obișnuit nu poate face singur?
2. Ce unealtă i-ar fi necesară agentului tău prima dată și de ce?
3. Ce sursă de cunoaștere trebuie să fundamenteze răspunsul agentului?
4. Ce context trebuie inclus în următorul apel la model?
5. Ce ar trebui să-și amintească agentul și ce ar trebui să evite să stocheze?
6. Când ar trebui agentul să ceară aprobare umană?
7. Ce jurnale, urme sau chitanțe te-ar ajuta să depanezi sau să auditizezi agentul
   mai târziu?

## Exercițiul Recomandat de Final

La sfârșitul cursului, construiește un mic agent care să ajute un învățăcel să
navigheze în acest depozit.

Versiune minimă:

- Acceptă un subiect de la utilizator.
- Găsește cele mai relevante lecții.
- Rezumă ce să citească mai întâi.
- Sugerează o sarcină practică.
- Arată ce fișiere sau linkuri de lecție au fost folosite.

Versiune extinsă:

- Ține minte limbajul de programare preferat al învățăcelului.
- Folosește un plan simplu înainte de a răspunde.
- Adaugă un pas de auto-verificare înainte de răspunsul final.
- Înregistrează apelurile uneltelor și sursele extrase.
- Cere confirmare înainte de a deschide sarcini de automatizare browser sau UI.

Aceasta îți oferă o modalitate mică, dar realistă, de a exersa unelte, RAG,
planificare, context, memorie, observabilitate și încredere într-un singur proiect.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->