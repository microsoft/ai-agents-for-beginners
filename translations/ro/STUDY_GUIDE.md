# Agenți AI pentru Începători - Ghid de Studiu

Folosește acest ghid ca un companion practic în timp ce parcurgi cursul. Nu este
destinat să înlocuiască lecțiile. Te ajută să decizi de unde să începi, ce să
cauți în fiecare lecție și cum să conectezi ideile într-un mic demo funcțional cu agentul.




2. Termină lecțiile 01-06 în ordine.
3. Ține o mică idee de demo în minte pe măsură ce înveți.
4. După fiecare lecție, întreabă-te: „Ce poate face acum agentul meu ce nu putea
    înainte?”










> ar trebui să citesc primul și dă-mi o sarcină practică scurtă.”




2. **Folosește instrumente** pentru a extrage link-uri către lecții, exemple sau materiale suport.
3. **Planifică** o cale scurtă de învățare în loc de a da un răspuns lung.
4. **Folosește contextul** conversației curente pentru a rămâne concentrat pe scopul învățăcelului.
5. **Ține minte preferințe utile** dacă aplicația suportă memorie.
6. **Arată urme, citări sau jurnale** astfel încât utilizatorul să poată înțelege ce s-a întâmplat.
7. **Aplică reguli de siguranță** înainte să faci acțiuni riscante sau să folosești date sensibile.

Pe măsură ce studiezi fiecare lecție, revino la acest demo și întreabă: ce nouă capacitate


## Spre ce Construiești

Până la finalul cursului, ar trebui să poți explica și construi sisteme de agenți


| Parte | Semnificație în limbaj simplu | În demo |

| Model | Motorul de raționament care interpretează cererea utilizatorului | Înțelege că învățăcelul vrea lecții despre folosirea instrumentelor |
| Instrumente | Funcții, API-uri, fișiere, browsere sau servicii pe care agentul le poate folosi | Caută în depozit sau extrage conținutul lecțiilor |
| Cunoștințe | Documente sau date folosite pentru a fundamenta răspunsul | Fișiere README ale cursului și material de lecție |
| Context | Informații incluse în următoarea apelare a modelului | Scopul utilizatorului și rezultatele instrumentelor |
| Memorie | Informații salvate pentru utilizare ulterioară | Învață pe baza preferinței pentru exemple practice în Python |
| Planificare | Descompunerea unui scop mai mare în pași mai mici | Găsește lecții, rezumă-le, sugerează practică |
| Orchestrare | Direcționarea muncii prin instrumente, pași sau agenți | Un planificator apelează un instrument de căutare, apoi un sumarizator |
| Încredere | Siguranță, securitate, evaluare și observabilitate | Înregistrează apelurile instrumentelor și cere consimțământ pentru acțiuni cu impact mare |

## Modele și Furnizori

Exemplele de cod din curs folosesc **Microsoft Agent Framework (MAF)** și țintesc

finalizările de chat, apelarea instrumentelor, input multimodal și conversații cu stare într-o singură suprafață API. Te conectezi fie printr-un proiect **Microsoft Foundry** (cu `FoundryChatClient`), fie direct la Azure OpenAI (cu `OpenAIChatClient`).

Pe măsură ce parcurgi lecțiile, ai câteva opțiuni de furnizori:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — calea principală folosită pe tot parcursul lecțiilor. Autentifică-te cu `az login` pentru autentificare Entra ID fără chei.
- **Foundry Local** — rulează modelele complet pe dispozitiv printr-un API compatibil OpenAI (fără cloud, fără chei API). Ideal pentru experimentare offline sau gratuită. Vezi [Configurarea cursului](./00-course-setup/README.md).
- **MiniMax** — un furnizor compatibil OpenAI cu modele de context mare, utilizabil ca alternativă plug-in.

> **Notă:** GitHub Models este învechit (se retrage în iulie 2026) și nu suportă Responses API. Exemplele au fost actualizate să folosească Azure OpenAI / Microsoft Foundry.

## Alege-ți Calea de Învățare

Poți urma cursul complet în ordine sau poți sări la o cale bazată pe ceea ce vrei
să construiești.

| Dacă scopul tău este să... | Începe cu | Apoi studiază |
|---------------------------|-----------|------------|
| Înțelegi ce sunt agenții | 01, 02, 03 | 04, 05, 06 |
| Construiești un agent care folosește instrumente | 04 | 05, 07, 14 |
| Construiești un agent bazat pe RAG | 05 | 04, 06, 12 |
| Proiectezi fluxuri de lucru multi-pas | 07 | 08, 09, 14 |
| Înțelegi sistemele multi-agent | 08 | 07, 09, 11 |
| Pregătești agenții pentru producție | 06, 10 | 12, 13, 16, 18 |
| Distribui și scalezi agenții pe Foundry | 10, 16 | 06, 13, 18 |
| Construiești agenți locali / offline-first | 17 | 04, 05, 11 |
| Explorezi protocoale și automatizare browser | 11, 15 | 10, 18 |

Sfat: dacă ești nou în domeniul agenților, nu sări lecțiile 01-06. Ele îți oferă
vocabularul de care vei avea nevoie pentru restul cursului.

## Ghid Lecție cu Lecție

| Lecția | Ce înveți | Încearcă asta după lecție |
|--------|-----------|------------------------|
| [01 - Introducere în Agenți AI](./01-intro-to-ai-agents/README.md) | Ce face un agent diferit de un chatbot simplu. | Explică-ți ideea de demo ca agent, nu doar ca aplicație de chat. |
| [02 - Framework-uri Agentice](./02-explore-agentic-frameworks/README.md) | Cum framework-urile ajută cu modelele, instrumentele, starea și fluxurile de lucru. | Identifică care părți ale demo-ului tău ar gestiona un framework. |
| [03 - Tipare de Design Agentice](./03-agentic-design-patterns/README.md) | Tipare comune pentru proiectarea comportamentului agentului. | Conturează traseul utilizatorului înainte de a scrie cod. |
| [04 - Folosirea Instrumentelor](./04-tool-use/README.md) | Cum agenții apelează instrumente pentru a obține date sau a acționa. | Definiți un instrument de care agentul tău demo ar avea nevoie. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Cum recuperarea fundamentează răspunsurile agenților în documente sau date. | Decide ce sursă de cunoștințe ar trebui să caute demo-ul tău. |

| [06 - Agenți de Încredere](./06-building-trustworthy-agents/README.md) | Cum să adaugi bariere de protecție, supraveghere și comportament mai sigur. | Adaugă o regulă pentru când agentul ar trebui să întrebe utilizatorul mai întâi. |
| [07 - Proiectarea Planificării](./07-planning-design/README.md) | Cum împart agenții obiectivele mai mari în pași mai mici. | Scrie un plan în trei pași pentru cererea ta de demonstrație. |
| [08 - Proiectare Multi-Agent](./08-multi-agent/README.md) | Când să distribui munca între agenți specializați. | Decide dacă demo-ul tău are nevoie de un singur agent sau mai mulți. |
| [09 - Metacogniție](./09-metacognition/README.md) | Cum agenții pot revizui și îmbunătăți propriile rezultate. | Adaugă o verificare finală de autoevaluare înainte ca agentul să răspundă. |
| [10 - Agenți AI în Producție](./10-ai-agents-production/README.md) | Ce se schimbă când un agent trece de la demonstrație la producție. | Listează ce ai monitoriza: calitate, cost, latență, eșecuri. |
| [11 - Protocoale Agentice](./11-agentic-protocols/README.md) | Cum protocoalele conectează agenții la unelte și alți agenți. | Identifică unde un protocol standard ar putea simplifica integrarea. |
| [12 - Ingineria Contextului](./12-context-engineering/README.md) | Cum să selectezi, reduci, izolezi și gestionezi contextul. | Decide ce trebuie inclus în prompt și ce trebuie exclus. |
| [13 - Memoria Agentului](./13-agent-memory/README.md) | Cum agenții pot salva informații utile pe parcursul interacțiunilor. | Alege o preferință sigură pe care demo-ul tău ar putea să o memoreze. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Blocuri de construcție specifice framework-ului pentru agenți și fluxuri de lucru, plus găzduirea agenților LangChain/LangGraph pe Microsoft Foundry. | Asociază pașii demo-ului tău cu conceptele framework-ului. |
| [15 - Agenți pentru Utilizarea Calculatorului](./15-browser-use/README.md) | Cum agenții pot interacționa cu browserul sau interfețele UI, inclusiv exemple din viața reală ca Microsoft Project Opal. | Alege o sarcină de browser care ar trebui să necesite în continuare confirmarea utilizatorului. |
| [16 - Implementarea Agenților Scalabili](./16-deploying-scalable-agents/README.md) | Cum să duci un agent de la prototip la o implementare scalabilă și observabilă în producție pe Microsoft Foundry (agenți găzduiți, rutare model, cache, porți de evaluare, teste de fum). | Listează preocupările de producție pe care demo-ul tău încă trebuie să le gestioneze: găzduire, rutare, cost, evaluare. |
| [17 - Crearea Agenților AI Locali](./17-creating-local-ai-agents/README.md) | Cum să construiești agenți locali care rulează complet pe mașina ta cu Foundry Local și Qwen (unelte locale, RAG local, MCP local). | Decide care părți ale demo-ului tău ar trebui să rămână private și să ruleze local. |
| [18 - Securizarea Agenților AI](./18-securing-ai-agents/README.md) | Cum să faci acțiunile agenților mai auditable și rezistente la manipulări. | Decide ce acțiuni din demo-ul tău ar trebui să fie înregistrate sau să primească o chitanță. |

## Validarea Agenților Implementați cu Teste de Fum

Când implementezi un agent (Lecția 16), un **test de fum** este prima
verificare cea mai ieftină pentru a confirma că implementarea răspunde efectiv. Acest repository oferă cataloage gata de rulat
în [tests/](./tests/README.md) pentru agenții implementabili din Lecțiile
01, 04, 05 și 16, conectați la

[Teste rapide AI](https://github.com/marketplace/actions/ai-smoke-test) pe GitHub Action. Rulează-le din fila **Actions** după ce ai implementat agentul lecției.
Testele rapide sunt o primă poartă — evaluare offline și online (Lecții 10 și 16)
îți spun cât de *bun* este agentul.


## Idei cheie explicate pe înțelesul începătorilor

### Unelte

O unealtă este ceva ce agentul poate apela pentru a face munca în afara modelului. O unealtă bună
are un nume clar, o sarcină restrânsă, intrări tipizate, un rezultat predictibil și o metodă sigură
de a eșua.

Pentru demo-ul ajutorului cursului, o unealtă ar putea fi:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG și Cunoaștere

RAG ajută agentul să răspundă din materialul sursă în loc să ghicească. În acest
curs, materialul sursă ar putea fi fișierele README ale lecțiilor, exemple de cod sau resurse externe
legate din lecții.

Folosește RAG când răspunsul trebuie să fie fundamentat în documente, date sau fișiere de proiect curente.


### Planificare

Planificarea este utilă când cererea are mai mulți pași. Menține planurile scurte și
suficient de vizibile pentru un dezvoltator sau utilizator să le inspecteze.

Pentru demo, un plan ar putea fi:

1. Găsește lecțiile legate de utilizarea uneltelor.
2. Rezumă cele mai relevante lecții.
3. Recomandă o sarcină de practică.

### Context

Contextul este ceea ce modelul vede acum. Prea puțin context poate face ca agentul
să rateze detalii importante. Prea mult context poate face agentul mai lent, mai costisitor,
sau mai ușor de confundat.

Ingineria bună a contextului înseamnă alegerea informațiilor potrivite pentru următorul apel al modelului.


### Memorie

Memoria este informația salvată pentru mai târziu. Nu salva totul. Salvează informații
doar când sunt utile, sigure și ușor de actualizat sau șters.

De exemplu, reținerea că "participantul preferă exemple în Python" poate fi utilă.
Reținerea datelor personale sensibile, de obicei, nu este.

### Evaluare și Observabilitate

Evaluarea întreabă: agentul a făcut bine ce trebuia?

Observabilitatea întreabă: putem vedea cum s-a întâmplat?

Pentru agenți de producție, urmărește apelurile la model, apelurile uneltelor, contextul preluat,
latența, costul, eșecurile și feedback-ul utilizatorului.

### Încredere și Securitate

Agenții de încredere au nevoie de mai mult decât un prompt util. Folosește unelte cu privilegii minime,
aprobare umană pentru acțiuni cu impact mare, redactarea datelor acolo unde e necesar și jurnale sau
chitanțe pentru acțiunile ce trebuie auditate.

## O rutină de revizuire de 15 minute

Folosește această rutină după fiecare lecție:

1. **Rezuma lecția într-o propoziție.**
2. **Denumește noua capacitate a agentului.** De exemplu: utilizarea uneltelor, recuperare,
   planificare, memorie, observabilitate sau securitate.
3. **Adaug-o în demo-ul ajutorului cursului.** Ce se schimbă acum în demo?
4. **Găsește riscul.** Ce ar putea merge prost dacă această capacitate este folosită greșit?
5. **Scrie o întrebare de test.** Cum ai verifica că agentul se comportă bine?

## Auto-verificare rapidă

Înainte de a continua, încearcă să răspunzi la aceste întrebări:

1. Ce poate face un agent pe care un chatbot obișnuit nu-l poate face singur?
2. Ce unealtă ar avea nevoie mai întâi agentul tău și de ce?
3. Ce sursă de cunoștințe ar trebui să fundamenteze răspunsul agentului?
4. Ce context ar trebui inclus în următorul apel al modelului?

5. Ce ar trebui să rețină agentul și ce ar trebui să evite să stocheze?
6. Când ar trebui ca agentul să ceară aprobarea umană?
7. Ce jurnale, urme sau chitanțe te-ar putea ajuta să depanezi sau să verifici agentul mai târziu?


## Exercițiu Capstone Sugerat

La finalul cursului, construiește un mic agent care să ajute un cursant să navigheze prin acest
depozit.

Versiune minimă:

- Acceptă un subiect de la utilizator.
- Găsește cele mai relevante lecții.
- Rezumă ce trebuie citit mai întâi.
- Sugerează o sarcină practică.
- Arată care fișiere sau linkuri de lecții au fost folosite.

Versiune extinsă:

- Amintește-ți limbajul de programare preferat al cursantului.
- Folosește un plan simplu înainte de a răspunde.
- Adaugă un pas de auto-verificare înainte de răspunsul final.
- Înregistrează apelurile instrumentelor și sursele recuperate.
- Cere confirmarea înainte de a deschide browserul sau de a începe sarcini de automatizare UI.

Aceasta îți oferă o modalitate mică, dar realistă, de a exersa instrumente, RAG, planificare,
context, memorie, observabilitate și încredere într-un singur proiect.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->