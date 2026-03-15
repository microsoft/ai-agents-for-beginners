# Agenți AI în Producție: Observabilitate și Evaluare

[![Agenți AI în Producție](../../../translated_images/ro/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Pe măsură ce agenții AI trec de la prototipuri experimentale la aplicații reale, abilitatea de a înțelege comportamentul lor, de a monitoriza performanța și de a evalua sistematic rezultatele devine importantă.

## Obiective de Învățare

După finalizarea acestei lecții, vei ști cum să/vei înțelege:
- Concepte de bază ale observabilității și evaluării agenților
- Tehnici pentru îmbunătățirea performanței, costurilor și eficienței agenților
- Ce și cum să evaluezi sistematic agenții tăi AI
- Cum să controlezi costurile la implementarea agenților AI în producție
- Cum să instrumentezi agenții construiți cu Microsoft Agent Framework

Scopul este să te echipeze cu cunoștințele necesare pentru a transforma agenții tăi „cutii negre” în sisteme transparente, gestionabile și de încredere.

_**Notă:** Este important să implementezi agenți AI care sunt siguri și de încredere. Consultă și lecția [Construirea Agenților AI de Încredere](./06-building-trustworthy-agents/README.md)._

## Trasee și Intervaluri

Instrumentele de observabilitate precum [Langfuse](https://langfuse.com/) sau [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) reprezintă de obicei rulările agentului ca trasee și intervale.

- **Traseul** reprezintă o sarcină completă a agentului de la început până la sfârșit (de exemplu, gestionarea unei interogări a utilizatorului).
- **Intervalele** sunt pași individuali în cadrul traseului (de exemplu, apelarea unui model lingvistic sau extragerea datelor).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Fără observabilitate, un agent AI poate părea o „cutie neagră” — starea și raționamentul intern sunt opace, ceea ce face dificilă diagnosticarea problemelor sau optimizarea performanței. Cu observabilitate, agenții devin „cutii de sticlă”, oferind transparență esențială pentru construirea încrederii și asigurarea faptului că aceștia funcționează conform intențiilor.

## De ce Contează Observabilitatea în Medii de Producție

Trecerea agenților AI în medii de producție introduce o nouă serie de provocări și cerințe. Observabilitatea nu mai este un „opțional” ci o capacitate critică:

*   **Depanare și Analiza Cauzei Rădăcină:** Când un agent eșuează sau produce un rezultat neașteptat, instrumentele de observabilitate oferă traseele necesare pentru a identifica sursa erorii. Acest lucru este crucial mai ales în agenții complexi care pot implica multiple apeluri LLM, interacțiuni cu unelte și logică condiționată.
*   **Gestionarea Latenței și Costurilor:** Agenții AI se bazează adesea pe LLM-uri și alte API-uri externe care sunt taxate pe token sau pe apel. Observabilitatea permite urmărirea precisă a acestor apeluri, ajutând la identificarea operațiunilor excesiv de lente sau costisitoare. Aceasta permite echipelor să optimizeze prompturile, să aleagă modele mai eficiente sau să reproiecteze fluxurile de lucru pentru a gestiona costurile operaționale și a asigura o experiență bună utilizatorului.
*   **Încredere, Siguranță și Conformitate:** În multe aplicații, este important să se asigure că agenții se comportă sigur și etic. Observabilitatea oferă un registru de audit al acțiunilor și deciziilor agentului. Acesta poate fi folosit pentru a detecta și atenua probleme precum injecția de prompt, generarea de conținut dăunător sau manipularea incorectă a informațiilor cu caracter personal (PII). De exemplu, poți analiza traseele pentru a înțelege de ce un agent a oferit un anumit răspuns sau a folosit un anumit instrument.
*   **Bucle de Îmbunătățire Continuă:** Datele de observabilitate stau la baza unui proces iterativ de dezvoltare. Monitorizând performanța agenților în lumea reală, echipele pot identifica zone de îmbunătățire, pot aduna date pentru ajustarea modelului și valida impactul schimbărilor. Aceasta creează un ciclu de feedback în care informațiile din producție din evaluarea online informează experimentarea și rafinarea offline, conducând la o performanță progresiv îmbunătățită a agentului.

## Metrici Cheie de Urmărit

Pentru a monitoriza și înțelege comportamentul agentului, trebuie urmărite o serie de metrici și semnale. Deși metricile specifice pot varia în funcție de scopul agentului, unele sunt universal importante.

Iată câteva dintre cele mai comune metrici pe care instrumentele de observabilitate le monitorizează:

**Latență:** Cât de rapid răspunde agentul? Timpurile lungi de așteptare au un impact negativ asupra experienței utilizatorului. Ar trebui să măsori latența pentru sarcini și pași individuali urmărind rulările agentului. De exemplu, un agent care durează 20 de secunde pentru toate apelurile modelului ar putea fi accelerat folosind un model mai rapid sau rulând apelurile în paralel.

**Costuri:** Care este cheltuiala per rulare a agentului? Agenții AI se bazează pe apeluri LLM taxate per token sau API-uri externe. Utilizarea frecventă a uneltelor sau prompturile multiple pot crește rapid costurile. De exemplu, dacă un agent face cinci apeluri la un LLM pentru o îmbunătățire marginală a calității, trebuie să evaluezi dacă costul este justificat sau dacă poți reduce numărul de apeluri sau folosi un model mai ieftin. Monitorizarea în timp real poate ajuta și la identificarea creșterilor neașteptate (ex: buguri care cauzează bucle excesive API).

**Erori de Cerere:** Câte cereri a eșuat agentul să proceseze? Aceasta poate include erori API sau apeluri de unelte nereușite. Pentru a face agentul mai robust în producție, poți configura fallback-uri sau reîncercări. De exemplu, dacă furnizorul LLM A este jos, poți trece la furnizorul LLM B ca rezervă.

**Feedback de la Utilizatori:** Implementarea evaluărilor directe ale utilizatorilor oferă informații valoroase. Aceasta poate include ratinguri explicite (👍like/👎dislike, ⭐1-5 stele) sau comentarii textuale. Feedback-ul negativ constant ar trebui să te alerteze deoarece este un semn că agentul nu funcționează conform așteptărilor.

**Feedback Implicit de la Utilizatori:** Comportamentele utilizatorilor oferă feedback indirect chiar și fără ratinguri explicite. Acest lucru poate include reformularea imediată a întrebării, interogări repetate sau apăsarea butonului de retry. De exemplu, dacă observi că utilizatorii pun aceeași întrebare în mod repetat, este un semn că agentul nu funcționează cum trebuie.

**Acuratețe:** Cât de frecvent produce agentul rezultate corecte sau dorite? Definițiile acurateței variază (de exemplu, corectitudinea rezolvării problemelor, acuratețea recuperării informațiilor, satisfacția utilizatorului). Primul pas este să definești ce înseamnă succesul pentru agentul tău. Poți urmări acuratețea prin verificări automate, scoruri de evaluare sau etichete de finalizare a sarcinii. De exemplu, marcând trasee ca „reusite” sau „eșuate”.

**Metrici de Evaluare Automată:** Poți configura și evaluări automate. De exemplu, poți folosi un LLM pentru a evalua output-ul agentului, dacă este util, corect sau nu. Există și mai multe librării open source care te ajută să evaluezi diferite aspecte ale agentului. De exemplu, [RAGAS](https://docs.ragas.io/) pentru agenții RAG sau [LLM Guard](https://llm-guard.com/) pentru a detecta limbaj dăunător sau injecții de prompt.

În practică, o combinație a acestor metrici oferă cea mai bună acoperire a stării de sănătate a unui agent AI. În [notebook-ul exemplu din acest capitol](./code_samples/10-expense_claim-demo.ipynb), îți vom arăta cum arată aceste metrici în exemple practice, dar mai întâi vom învăța cum arată un flux tipic de evaluare.

## Instrumentează Agentul Tău

Pentru a colecta date de urmărire (tracing), va trebui să instrumentezi codul. Scopul este să instrumentezi codul agentului pentru a emite trasee și metrici care pot fi capturate, procesate și vizualizate de o platformă de observabilitate.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) a devenit standardul industriei pentru observabilitatea LLM. Oferă un set de API-uri, SDK-uri și instrumente pentru generarea, colectarea și exportarea datelor de telemetrie.

Există multe biblioteci de instrumentare care înfășoară cadrele existente de agenți și facilitează exportul intervalelor OpenTelemetry către un instrument de observabilitate. Microsoft Agent Framework se integrează nativ cu OpenTelemetry. Mai jos este un exemplu de instrumentare a unui agent MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Execuția agentului este urmărită automat
    pass
```

[Notebook-ul exemplu](./code_samples/10-expense_claim-demo.ipynb) din acest capitol va demonstra cum să-ți instrumentezi agentul MAF.

**Crearea Manuală a Intervalelor:** Deși bibliotecile de instrumentare oferă o bază bună, există cazuri în care este nevoie de informații mai detaliate sau personalizate. Poți crea manual intervale pentru a adăuga logică personalizată a aplicației. Mai important, acestea pot îmbogăți intervalele create automat sau manual cu atribute personalizate (cunoscute și ca tag-uri sau metadate). Aceste atribute pot include date specifice de business, calcule intermediare sau orice context util pentru depanare sau analiză, cum ar fi `user_id`, `session_id` sau `model_version`.

Exemplu de creare manuală a traseelor și intervalelor cu [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluarea Agenților

Observabilitatea ne oferă metrici, dar evaluarea este procesul de analiză a datelor respective (și efectuare a testelor) pentru a determina cât de bine performează un agent AI și cum poate fi îmbunătățit. Cu alte cuvinte, odată ce ai trasele și metricile, cum le folosești pentru a judeca agentul și a lua decizii?

Evaluarea regulată este importantă deoarece agenții AI sunt adesea nedeterministici și pot evolua (prin actualizări sau modificări comportamentale ale modelului) — fără evaluare, nu ai ști dacă „agentul inteligent” face cu adevărat o treabă bună sau a regresat.

Există două categorii de evaluări pentru agenții AI: **evaluare online** și **evaluare offline**. Ambele sunt valoroase și se completează reciproc. De obicei, începem cu evaluarea offline, deoarece este pasul minim necesar înainte de a implementa orice agent.

### Evaluarea Offline

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Aceasta implică evaluarea agentului într-un mediu controlat, de obicei folosind seturi de date de testare, nu interogări live ale utilizatorilor. Folosești seturi de date curate unde știi care este output-ul așteptat sau comportamentul corect și apoi rulatezi agentul pe acestea.

De exemplu, dacă ai construit un agent pentru rezolvarea problemelor de matematică sub forma unui text, ai putea avea un [set de date de test](https://huggingface.co/datasets/gsm8k) cu 100 de probleme cu răspunsuri cunoscute. Evaluarea offline se face adesea în timpul dezvoltării (și poate face parte din pipeline-urile CI/CD) pentru a verifica îmbunătățiri sau pentru a preveni regresii. Avantajul este că este **repetabilă și poți obține metrici clare de acuratețe deoarece ai adevărul de bază (ground truth)**. Poți simula, de asemenea, interogări ale utilizatorilor și măsura răspunsurile agentului în raport cu răspunsuri ideale sau folosi metrici automate așa cum am descris mai sus.

Provocarea principală la evaluarea offline este asigurarea că setul tău de date de test este cuprinzător și rămâne relevant — agentul poate performa bine pe un set fix de test, dar poate întâmpina interogări foarte diferite în producție. Prin urmare, ar trebui să menții seturile de test actualizate cu cazuri limită noi și exemple care reflectă scenarii din lumea reală. Un mix de cazuri mici de „test de fum” și seturi mai mari de evaluare este util: seturi mici pentru verificări rapide și seturi mari pentru metrici mai largi de performanță.

### Evaluarea Online

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Aceasta se referă la evaluarea agentului într-un mediu live, real, adică în timpul folosirii efective în producție. Evaluarea online implică monitorizarea performanței agentului pe interacțiuni reale cu utilizatorii și analiza continuă a rezultatelor.

De exemplu, ai putea urmări ratele de succes, scorurile de satisfacție ale utilizatorilor sau alți metrici pe trafic live. Avantajul evaluării online este că **prinde lucruri pe care nu le-ai anticipa în laborator** — poți observa driftul modelului în timp (dacă eficacitatea agentului scade pe măsură ce tiparele de intrare se schimbă) și poți detecta întrebări sau situații neașteptate care nu erau în datele tale de test. Oferă o imagine reală a comportamentului agentului în mediul său natural.

Evaluarea online implică adesea colectarea feedback-ului implicit și explicit al utilizatorilor, după cum am discutat, și posibil rularea unor teste shadow sau A/B (unde o versiune nouă a agentului rulează în paralel pentru comparație cu cea veche). Provocarea este că poate fi dificil să obții etichete sau scoruri fiabile pentru interacțiunile live — s-ar putea să te bazezi pe feedback-ul utilizatorului sau pe metrici din aval (de exemplu, dacă utilizatorul a dat clic pe rezultat).

### Combinarea celor două

Evaluările online și offline nu sunt exclusive; sunt foarte complementare. Informațiile din monitorizarea online (de exemplu, tipuri noi de întrebări utilizator unde agentul performează slab) pot fi folosite pentru a îmbogăți și îmbunătăți seturile de date offline. În schimb, agenții care performează bine la testele offline pot fi implementați cu încredere și monitorizați online.

De fapt, multe echipe adoptă un ciclu:

_evaluează offline -> implementează -> monitorizează online -> colectează cazuri noi de eșec -> adaugă la setul offline -> rafinează agentul -> repetă_.

## Probleme Comune

Pe măsură ce implementezi agenți AI în producție, poți întâlni diverse provocări. Iată câteva probleme comune și posibilele lor soluții:

| **Problemă**    | **Soluție Potențială**   |
| ------------- | ------------------ |
| Agent AI nu execută sarcinile în mod consecvent | - Rafinează promptul dat agentului AI; fii clar în obiective.<br>- Identifică unde împărțirea sarcinilor în subtasks și gestionarea acestora de către agenți multipli poate ajuta. |
| Agent AI intră în bucle continue  | - Asigură-te că ai termeni și condiții clare de oprire astfel încât agentul să știe când să oprească procesul.<br>- Pentru sarcini complexe ce necesită raționament și planificare, folosește un model mai mare specializat pentru astfel de sarcini. |
| Apelurile cu unelte ale agentului nu performează bine  | - Testează și validează output-ul uneltei în afara sistemului agentului.<br>- Rafinează parametrii definiți, prompturile și denumirea uneltelor.  |
| Sistem multi-agent care nu performează consecvent | - Rafinează prompturile date fiecărui agent pentru a te asigura că sunt specifice și distincte între ele.<br>- Construiește un sistem ierarhic folosind un agent „router” sau controller pentru a determina care agent este cel corect. |

Multe dintre aceste probleme pot fi identificate mult mai eficient prin observabilitate. Traseele și metricile discutate anterior ajută la localizarea exactă a problemelor în fluxul de lucru al agentului, făcând depanarea și optimizarea mult mai eficiente.

## Gestionarea Costurilor
Iată câteva strategii pentru a gestiona costurile de implementare a agenților AI în producție:

**Folosirea modelelor mai mici:** Modelele mici de limbaj (SLM) pot performa bine în anumite cazuri de utilizare agentică și vor reduce costurile semnificativ. Așa cum am menționat mai devreme, construirea unui sistem de evaluare pentru a determina și compara performanța față de modelele mai mari este cea mai bună metodă de a înțelege cât de bine va performa un SLM în cazul tău de utilizare. Ia în considerare folosirea SLM-urilor pentru sarcini mai simple precum clasificarea intențiilor sau extragerea parametrilor, rezervând modelele mai mari pentru raționamente complexe.

**Folosirea unui model router:** O strategie similară este să folosești o diversitate de modele și dimensiuni. Poți folosi un LLM/SLM sau o funcție serverless pentru a direcționa cererile în funcție de complexitate către modelele cele mai potrivite. Aceasta va ajuta de asemenea la reducerea costurilor, asigurând în același timp performanța pe sarcinile potrivite. De exemplu, direcționează interogările simple către modele mai mici și mai rapide și folosește doar modelele mari și scumpe pentru sarcini complexe de raționament.

**Stocarea în cache a răspunsurilor:** Identificarea cererilor și sarcinilor comune și oferirea răspunsurilor înainte ca acestea să treacă prin sistemul tău agentic este o metodă bună de a reduce volumul cererilor similare. Poți chiar implementa un flux pentru a identifica cât de similară este o cerere cu cererile tale din cache folosind modele AI mai simple. Această strategie poate reduce semnificativ costurile pentru întrebările frecvente sau fluxurile de lucru comune.

## Să vedem cum funcționează asta în practică

În [notebook-ul exemplu din această secțiune](./code_samples/10-expense_claim-demo.ipynb), vom vedea exemple despre cum putem folosi instrumentele de observabilitate pentru a monitoriza și evalua agentul nostru.

### Ai mai multe întrebări despre agenții AI în producție?

Alătură-te [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la orele de consultanță și a obține răspunsuri la întrebările tale despre Agenții AI.

## Lecția anterioară

[Modelul de design Metacogniție](../09-metacognition/README.md)

## Lecția următoare

[Protocoalele agentice](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere automată [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite cauzate de utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->