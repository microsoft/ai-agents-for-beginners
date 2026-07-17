# Agenți AI în Producție: Observabilitate & Evaluare

[![AI Agents in Production](../../../translated_images/ro/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Pe măsură ce agenții AI trec de la prototipuri experimentale la aplicații din lumea reală, capacitatea de a înțelege comportamentul lor, de a monitoriza performanța și de a evalua sistematic rezultatele devine esențială.

## Obiective de Învățare

După ce vei termina această lecție, vei ști cum să/vei înțelege:
- Conceputuri de bază ale observabilității și evaluării agenților
- Tehnici pentru îmbunătățirea performanței, costurilor și eficacității agenților
- Ce și cum să evaluezi sistematic agenții tăi AI
- Cum să controlezi costurile atunci când implementezi agenți AI în producție
- Cum să instrumentezi agenții construiți cu Microsoft Agent Framework

Scopul este să te echipăm cu cunoștințele necesare pentru a transforma agenții tăi „cutii negre” în sisteme transparente, gestionabile și de încredere.

_**Notă:** Este important să implementezi agenți AI care sunt siguri și demni de încredere. Consultă și lecția [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Trasee și Pași

Instrumentele de observabilitate precum [Langfuse](https://langfuse.com/) sau [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) de obicei reprezintă execuțiile agenților sub formă de trasee și pași.

- **Trace (Traseu)** reprezintă o sarcină completă a agentului de la început până la sfârșit (de exemplu, gestionarea unei cereri a utilizatorului).
- **Spans (Pași)** sunt etape individuale în cadrul traseului (de exemplu, apelarea unui model de limbaj sau recuperarea datelor).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Fără observabilitate, un agent AI poate părea o „cutie neagră” - starea internă și raționamentul său sunt opace, făcând dificilă diagnosticarea problemelor sau optimizarea performanței. Cu observabilitatea, agenții devin „cutii de sticlă”, oferind transparența vitală pentru construirea încrederii și asigurarea funcționării conform intenției.

## De ce Este Importantă Observabilitatea în Mediile de Producție

Trecerea agenților AI în mediile de producție introduce un nou set de provocări și cerințe. Observabilitatea nu mai este un „nice-to-have”, ci o capacitate critică:

*   **Depanare și Analiză a Cauzelor**: Când un agent eșuează sau produce un rezultat neașteptat, instrumentele de observabilitate oferă traseele necesare pentru a identifica sursa erorii. Acest lucru este deosebit de important în agenții complexi care pot implica multiple apeluri LLM, interacțiuni cu unelte și logică condițională.
*   **Gestionarea latenței și costurilor**: Agenții AI se bazează adesea pe LLM-uri și alte API-uri externe facturate per token sau per apel. Observabilitatea permite o urmărire precisă a acestor apeluri, ajutând la identificarea operațiunilor excesiv de lente sau costisitoare. Aceasta le permite echipelor să optimizeze prompturile, să selecteze modele mai eficiente sau să reproiecteze fluxurile de lucru pentru a gestiona costurile operaționale și a asigura o experiență bună a utilizatorului.
*   **Încredere, Siguranță și Conformitate**: În multe aplicații este important să se asigure că agenții se comportă în mod sigur și etic. Observabilitatea oferă un traseu de audit al acțiunilor și deciziilor agentului. Acesta poate fi folosit pentru a detecta și atenua probleme precum injectarea de prompturi, generarea de conținut dăunător sau gestionarea necorespunzătoare a informațiilor personale identificabile (PII). De exemplu, poți examina traseele pentru a înțelege de ce un agent a oferit un anumit răspuns sau a folosit un anumit instrument.
*   **Bucle de Îmbunătățire Continuă**: Datele de observabilitate sunt fundamentul unui proces iterativ de dezvoltare. Monitorizând performanța agenților în lumea reală, echipele pot identifica zonele de îmbunătățire, colecta date pentru reglarea fină a modelelor și valida impactul schimbărilor. Aceasta creează un ciclu de feedback în care informațiile din producție obținute prin evaluări online informează experimentarea și rafinarea offline, conducând la performanțe progresiv mai bune ale agenților.

## Metrici Cheie de Monitorizat

Pentru a monitoriza și înțelege comportamentul agentului, trebuie urmărit un set de metrici și semnale. Deși metricile specifice pot varia în funcție de scopul agentului, unele sunt universal importante.

Iată câteva dintre cele mai comune metrici pe care instrumentele de observabilitate le monitorizează:

**Latență:** Cât de rapid răspunde agentul? Timpurile lungi de așteptare afectează negativ experiența utilizatorului. Ar trebui să măsori latența pentru sarcini și pași individuali prin trasarea execuțiilor agentului. De exemplu, un agent care durează 20 de secunde pentru toate apelurile modelelor ar putea fi accelerat folosind un model mai rapid sau executând apelurile modelelor în paralel.

**Costuri:** Care este cheltuiala pe execuție a agentului? Agenții AI se bazează pe apeluri LLM facturate per token sau API-uri externe. Utilizarea frecventă a uneltelor sau multiple prompturi pot crește rapid costurile. De exemplu, dacă un agent apelează un LLM de cinci ori pentru o îmbunătățire marginală a calității, trebuie să evaluezi dacă costul este justificat sau dacă poți reduce numărul apelurilor sau utiliza un model mai ieftin. Monitorizarea în timp real poate ajuta și la identificarea creșterilor neașteptate (de ex. bug-uri care cauzează bucle excesive de API).

**Erori de Cerere:** Câte cereri a eșuat agentul să proceseze? Aceasta poate include erori API sau apeluri de unelte eșuate. Pentru a face agentul mai robust împotriva acestor situații în producție, poți apoi configura soluții alternative sau încercări repetate. De ex. dacă furnizorul LLM A este inaccesibil, treci la furnizorul LLM B ca rezervă.

**Feedback-ul Utilizatorilor:** Implementarea evaluărilor directe ale utilizatorilor oferă perspective valoroase. Aceasta poate include calificative explicite (👍thumbs-up/👎down, ⭐1-5 stele) sau comentarii textuale. Feedback-ul negativ constant ar trebui să te avertizeze deoarece este un semn că agentul nu funcționează conform așteptărilor.

**Feedback Implicit al Utilizatorului:** Comportamentele utilizatorului oferă feedback indirect chiar și fără evaluări explicite. Acest lucru poate include reformularea imediată a întrebărilor, întrebări repetate sau apăsarea unui buton de reîncercare. De ex., dacă vezi că utilizatorii pun în mod repetat aceeași întrebare, este un semn că agentul nu funcționează conform așteptărilor.

**Acuratețe:** Cât de frecvent produce agentul rezultate corecte sau dorite? Definițiile acurateței variază (de ex. corectitudinea soluționării problemelor, acuratețea recuperării informațiilor, satisfacția utilizatorului). Primul pas este să definești cum arată succesul pentru agentul tău. Poți monitoriza acuratețea prin verificări automate, scoruri de evaluare sau etichete de finalizare a sarcinii. De exemplu, marcând traseele ca „reusite” sau „eșuate”.

**Metrici de Evaluare Automată:** De asemenea, poți configura evaluări automate. Spre exemplu, poți folosi un LLM pentru a evalua rezultatul agentului, dacă este util, precis sau nu. Există și mai multe biblioteci open source care te ajută să evaluezi diferite aspecte ale agentului. De ex. [RAGAS](https://docs.ragas.io/) pentru agenți RAG sau [LLM Guard](https://llm-guard.com/) pentru detectarea limbajului dăunător sau a injectării de prompturi.

În practică, o combinație a acestor metrici oferă cea mai bună acoperire a stării unui agent AI. În [notebook-ul exemplu](./code_samples/10-expense_claim-demo.ipynb) din acest capitol, îți vom arăta cum arată aceste metrici în exemple reale, dar mai întâi vom învăța cum arată un flux tipic de evaluare.

## Instrumentează-ți Agentul

Pentru a colecta date de trasare, va trebui să-ți instrumentezi codul. Scopul este să instrumeți codul agentului pentru a genera trasee și metrici care pot fi capturate, procesate și vizualizate de o platformă de observabilitate.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) a devenit un standard industrial pentru observabilitatea LLM. Oferă un set de API-uri, SDK-uri și unelte pentru generarea, colectarea și exportarea datelor de telemetrie.

Există multe biblioteci de instrumentare care înfășoară cadrele existente de agenți și fac simplă exportarea span-urilor OpenTelemetry către un instrument de observabilitate. Microsoft Agent Framework se integrează nativ cu OpenTelemetry. Mai jos este un exemplu de instrumentare a unui agent MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Executarea agentului este urmărită automat
    pass
```

[Notebook-ul exemplu](./code_samples/10-expense_claim-demo.ipynb) din acest capitol va demonstra cum să instrumentezi un agent MAF.

**Creare Manuală de Span-uri:** Deși bibliotecile de instrumentare oferă o bază bună, există adesea cazuri în care sunt necesare informații mai detaliate sau personalizate. Poți crea manual span-uri pentru a adăuga logică personalizată a aplicației. Mai important, ele pot îmbogăți span-urile create automat sau manual cu atribute personalizate (cunoscute și ca tag-uri sau metadate). Aceste atribute pot include date specifice afacerii, calcule intermediare sau orice context util pentru depanare sau analiză, precum `user_id`, `session_id` sau `model_version`.

Exemplu de creare manuală a traseelor și pașilor cu [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluarea Agenților

Observabilitatea ne oferă metrici, dar evaluarea este procesul de analiză a acestor date (și efectuare de teste) pentru a stabili cât de bine performează un agent AI și cum poate fi îmbunătățit. Cu alte cuvinte, odată ce ai trasele și metricile, cum le folosești pentru a judeca agentul și a lua decizii?

Evaluarea regulată este importantă pentru că agenții AI sunt deseori nedeterministici și pot evolua (prin actualizări sau driftul comportamentului modelului) – fără evaluare, nu ai ști dacă „agentul inteligent” chiar își face bine treaba sau dacă a regresat.

Există două categorii de evaluări pentru agenții AI: **evaluarea online** și **evaluarea offline**. Ambele sunt valoroase și se completează reciproc. De obicei începem cu evaluarea offline, deoarece aceasta este pasul minim necesar înainte de a implementa orice agent.

### Evaluare Offline

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Aceasta implică evaluarea agentului într-un mediu controlat, folosind de obicei seturi de date de test, nu cereri live ale utilizatorilor. Folosești seturi de date atent selecționate în care știi care este rezultatul așteptat sau comportamentul corect, apoi rulezi agentul pe acestea.

De exemplu, dacă ai construit un agent pentru probleme matematice în cuvinte, ai putea avea un [set de date de test](https://huggingface.co/datasets/gsm8k) cu 100 de probleme cu răspunsuri cunoscute. Evaluarea offline se face deseori în timpul dezvoltării (și poate face parte din pipeline-urile CI/CD) pentru a verifica îmbunătățirile sau pentru a preveni regresiile. Avantajul este că este **repetabilă și poți obține metrici clare de acuratețe pentru că ai adevărul de bază**. Poți de asemenea simula cereri ale utilizatorilor și măsura răspunsurile agentului față de răspunsuri ideale sau să folosești metrici automate, așa cum am descris mai sus.

Provocarea principală cu evaluarea offline este asigurarea că setul tău de date de test este cuprinzător și rămâne relevant – agentul poate performa bine pe un set fix de teste, dar să întâmpine întrebări foarte diferite în producție. Prin urmare, ar trebui să actualizezi seturile de test cu noi cazuri-limită și exemple care reflectă scenarii din lumea reală. Un amestec de cazuri mici de „smoke test” și seturi mai mari de evaluare este util: seturi mici pentru verificări rapide și seturi mai mari pentru metrici de performanță mai largi.

### Evaluare Online

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Aceasta se referă la evaluarea agentului într-un mediu live, din lumea reală, adică în timpul utilizării efective în producție. Evaluarea online implică monitorizarea performanței agentului pe interacțiuni reale cu utilizatorii și analiza continuă a rezultatelor.

De exemplu, ai putea urmări ratele de succes, scorurile de satisfacție ale utilizatorilor sau alți metrici pe traficul live. Avantajul evaluării online este că **prinde lucruri pe care nu le-ai anticipa într-un laborator** – poți observa driftul modelului în timp (dacă eficiența agentului scade pe măsură ce modelele de intrare se schimbă) și surprinde întrebări sau situații neașteptate care nu erau în datele tale de test. Oferă o imagine reală a modului în care agentul se comportă în mediul natural.

Evaluarea online implică adesea colectarea feedback-ului implicit și explicit al utilizatorilor, așa cum am discutat, și posibil rularea testelor în umbră sau A/B (unde o versiune nouă a agentului rulează în paralel pentru comparație cu cea veche). Provocarea este că poate fi dificil să obții etichete sau scoruri fiabile pentru interacțiunile live – te poți baza pe feedback-ul utilizatorilor sau metrici în aval (de ex. dacă utilizatorul a făcut clic pe rezultat).

### Combinarea celor două

Evaluările online și offline nu sunt mutual exclusive; ele sunt foarte complementare. Informațiile din monitorizarea online (de ex. noi tipuri de întrebări ale utilizatorilor unde agentul performează slab) pot fi folosite pentru a completa și îmbunătăți seturile de date offline. Dimpotrivă, agenții care performează bine în testele offline pot apoi fi implementați mai încrezător și monitorizați online.

De fapt, multe echipe adoptă un ciclu:

_evaluați offline -> implementați -> monitorizați online -> adunați noi cazuri de eșec -> adăugați în setul offline -> rafinați agentul -> repetați_.

## Probleme Comune

Pe măsură ce implementezi agenți AI în producție, poți întâlni diverse provocări. Iată câteva probleme comune și soluțiile lor posibile:

| **Problemă**    | **Soluție Potențială**   |
| ------------- | ------------------ |
| Agentul AI nu execută sarcinile constant | - Perfecționează promptul oferit agentului AI; fii clar asupra obiectivelor.<br>- Identifică unde divizarea sarcinilor în subtasks și gestionarea lor de către mai mulți agenți poate ajuta. |
| Agentul AI intră în bucle continue  | - Asigură-te că ai termeni și condiții clare de terminare pentru ca agentul să știe când să oprească procesul.<br>- Pentru sarcini complexe care necesită raționament și planificare, folosește un model mai mare specializat pentru astfel de sarcini. |
| Apelurile către unelte ale agentului AI nu funcționează bine   | - Testează și validează output-ul uneltelor în afara sistemului agent.<br>- Perfecționează parametrii definiți, prompturile și denumirile uneltelor.  |
| Sistemul Multi-Agent nu performează consistent | - Perfecționează prompturile date fiecărui agent pentru a te asigura că sunt specifice și distincte unul față de altul.<br>- Construiește un sistem ierarhic folosind un agent „de rutare” sau controler pentru a determina care agent este cel corect. |

Multe dintre aceste probleme pot fi identificate mult mai eficient cu observabilitatea implementată. Traseele și metricile discutate mai devreme ajută la localizarea exactă a locului în fluxul de lucru al agentului unde apar problemele, ceea ce face depanarea și optimizarea mult mai eficiente.

## Gestionarea Costurilor


Iată câteva strategii pentru a gestiona costurile implementării agenților AI în producție:

**Folosirea modelelor mai mici:** Modelele mici de limbaj (SLM) pot performa bine în anumite cazuri de utilizare agentică și vor reduce semnificativ costurile. Așa cum am menționat mai devreme, construirea unui sistem de evaluare pentru a determina și compara performanța față de modelele mai mari este cea mai bună modalitate de a înțelege cât de bine va performa un SLM în cazul dvs. de utilizare. Luați în considerare utilizarea SLM-urilor pentru sarcini mai simple, cum ar fi clasificarea intențiilor sau extragerea parametrilor, în timp ce rețineți modelele mai mari pentru raționamente complexe.

**Folosirea unui model router:** O strategie similară este utilizarea unei diversități de modele și dimensiuni. Puteți folosi un LLM/SLM sau o funcție serverless pentru a redirecționa cererile în funcție de complexitate către modelele cele mai potrivite. Aceasta va ajuta, de asemenea, la reducerea costurilor, asigurând în același timp performanța în sarcinile potrivite. De exemplu, redirecționați întrebările simple către modele mai mici și mai rapide și folosiți modelele mari și costisitoare doar pentru sarcini de raționament complexe.

**Stocarea în cache a răspunsurilor:** Identificarea cererilor și a sarcinilor comune și furnizarea răspunsurilor înainte ca acestea să treacă prin sistemul dvs. agentic este o metodă bună de a reduce volumul cererilor similare. Puteți chiar implementa un flux pentru a identifica cât de similară este o cerere cu cele stocate în cache folosind modele AI mai simple. Această strategie poate reduce semnificativ costurile pentru întrebările frecvente sau fluxurile de lucru comune.

## Haideți să vedem cum funcționează asta în practică

În [notebook-ul exemplu al acestei secțiuni](./code_samples/10-expense_claim-demo.ipynb), vom vedea exemple despre cum putem folosi instrumente de observabilitate pentru a monitoriza și evalua agentul nostru.


### Aveți mai multe întrebări despre agenții AI în producție?

Alăturați-vă [Discord Microsoft Foundry](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la ore de consultanță și a primi răspunsuri la întrebările dvs. despre agenții AI.

## Lecția anterioară

[Modelul de proiectare Metacogniție](../09-metacognition/README.md)

## Lecția următoare

[Protocoalele agentice](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->