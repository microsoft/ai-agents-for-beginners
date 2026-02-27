# Agenți AI în producție: Observabilitate și evaluare

[![Agenți AI în producție](../../../translated_images/ro/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Pe măsură ce agenții AI trec de la prototipuri experimentale la aplicații din lumea reală, devine importantă capacitatea de a înțelege comportamentul lor, de a monitoriza performanța și de a evalua sistematic rezultatele acestora.

## Obiective de învățare

După ce vei finaliza această lecție, vei ști cum să/înțelegi:
- Conceputle de bază despre observabilitatea și evaluarea agenților
- Tehnici pentru îmbunătățirea performanței, costurilor și eficienței agenților
- Ce și cum să evaluezi sistematic agenții tăi AI
- Cum să controlezi costurile la implementarea agenților AI în producție
- Cum să instrumentezi agenți construiți cu Microsoft Agent Framework

Scopul este să te echipezi cu cunoștințele necesare pentru a transforma agenții tăi "cutii negre" în sisteme transparente, gestionabile și de încredere.

_**Notă:** Este important să implementezi Agenți AI care sunt siguri și de încredere. Consultă și lecția [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md)._

## Trasee și span-uri

Instrumentele de observabilitate precum [Langfuse](https://langfuse.com/) sau [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) reprezintă de obicei execuțiile agenților ca trasee și span-uri.

- **Traseul** reprezintă o sarcină completă a agentului de la început până la sfârșit (de exemplu, gestionarea unei întrebări a utilizatorului).
- **Span-urile** sunt pași individuali în cadrul traseului (de exemplu, apelarea unui model lingvistic sau recuperarea datelor).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Fără observabilitate, un agent AI poate părea o „cutie neagră” – starea internă și raționamentul său sunt opace, ceea ce face dificilă diagnosticarea problemelor sau optimizarea performanței. Cu observabilitate, agenții devin „cutii de sticlă”, oferind transparență vitală pentru construirea încrederii și asigurarea funcționării conform intențiilor.

## De ce contează observabilitatea în mediile de producție

Trecerea agenților AI în mediile de producție introduce un nou set de provocări și cerințe. Observabilitatea nu mai este un „nice-to-have”, ci o capacitate critică:

*   **Debugging și analiza cauzelor rădăcină**: Când un agent eșuează sau produce un rezultat neașteptat, instrumentele de observabilitate oferă traseele necesare pentru a identifica sursa erorii. Acest lucru este deosebit de important în agenții complexi care pot implica multiple apeluri LLM, interacțiuni cu instrumente și logică condițională.
*   **Gestionarea latenței și costurilor**: Agenții AI se bazează adesea pe LLM-uri și alte API-uri externe care sunt taxate per token sau apel. Observabilitatea permite urmărirea precisă a acestor apeluri, ajutând la identificarea operațiunilor excesiv de lente sau costisitoare. Acest lucru permite echipelor să optimizeze prompturile, să aleagă modele mai eficiente sau să reproiecteze fluxurile de lucru pentru a gestiona costurile operaționale și pentru a asigura o experiență bună utilizatorului.
*   **Încredere, siguranță și conformitate**: În multe aplicații, este important să asiguri că agenții se comportă în siguranță și etic. Observabilitatea oferă o pistă de audit a acțiunilor și deciziilor agentului. Aceasta poate fi folosită pentru a detecta și atenua probleme precum injecția de prompturi, generarea de conținut dăunător sau manipularea necorespunzătoare a informațiilor cu caracter personal (PII). De exemplu, poți analiza traseele pentru a înțelege de ce un agent a furnizat un anumit răspuns sau a folosit un anumit instrument.
*   **Bucla de îmbunătățire continuă**: Datele de observabilitate sunt fundamentul unui proces de dezvoltare iterativ. Prin monitorizarea modului în care agenții performează în lumea reală, echipele pot identifica zonele de îmbunătățire, aduna date pentru ajustarea modelelor și valida impactul schimbărilor. Acest lucru creează o buclă de feedback în care informațiile din producție, obținute prin evaluare online, informează experimentări și rafinări offline, conducând la performanțe progresiv mai bune ale agentului.

## Metrici-cheie de monitorizat

Pentru a monitoriza și înțelege comportamentul agentului, trebuie urmărite o serie de metrici și semnale. Deși metricile specifice pot varia în funcție de scopul agentului, unele sunt universal importante.

Iată câteva dintre cele mai comune metrici monitorizate de instrumentele de observabilitate:

**Latență:** Cât de repede răspunde agentul? Timpii lungi de așteptare afectează negativ experiența utilizatorului. Ar trebui să măsori latența pentru sarcini și pași individuali prin urmărirea execuțiilor agentului. De exemplu, un agent care durează 20 de secunde pentru toate apelurile modelului ar putea fi accelerat folosind un model mai rapid sau rulând apelurile modelului în paralel.

**Costuri:** Care este costul per rulare a agentului? Agenții AI se bazează pe apeluri LLM taxate per token sau pe API-uri externe. Utilizarea frecventă a instrumentelor sau multiple prompturi pot crește rapid costurile. De exemplu, dacă un agent apelează un LLM de cinci ori pentru o îmbunătățire marginală a calității, trebuie să evaluezi dacă costul este justificat sau dacă poți reduce numărul apelurilor sau folosi un model mai ieftin. Monitorizarea în timp real poate ajuta, de asemenea, la identificarea vârfurilor neașteptate (de ex., bug-uri care cauzează bucle excesive de API).

**Erori de cerere:** Câte cereri a eșuat agentul să execute? Aceasta poate include erori API sau apeluri nereușite ale instrumentelor. Pentru a-ți face agentul mai robust împotriva acestora în producție, poți apoi pune în aplicare mecanisme de rezervă sau reîncercări. De ex., dacă furnizorul LLM A este indisponibil, treci la furnizorul LLM B ca backup.

**Feedback-ul utilizatorului:** Implementarea evaluărilor directe de la utilizatori oferă informații valoroase. Aceasta poate include evaluări explicite (👍thumbs-up/👎down, ⭐1-5 stele) sau comentarii textuale. Feedback-ul negativ constant ar trebui să îți atragă atenția deoarece este un semn că agentul nu funcționează conform așteptărilor.

**Feedback implicit al utilizatorului:** Comportamentele utilizatorilor oferă feedback indirect chiar și fără evaluări explicite. Acestea pot include reformularea imediată a întrebărilor, întrebări repetate sau apăsarea unui buton de retry. De ex., dacă observi că utilizatorii repetă aceeași întrebare, acesta este un semn că agentul nu funcționează conform așteptărilor.

**Acuratețe:** Cât de des produce agentul rezultate corecte sau dorite? Definițiile acurateței variază (de ex., corectitudinea rezolvării problemelor, acuratețea recuperării informațiilor, satisfacția utilizatorului). Primul pas este să definești ce înseamnă succes pentru agentul tău. Poți urmări acuratețea prin verificări automate, scoruri de evaluare sau etichete de finalizare a sarcinilor. De exemplu, marcarea traseelor ca „reușite” sau „eșuate”.

**Metrici automate de evaluare:** Poți, de asemenea, configura evaluări automate. De exemplu, poți folosi un LLM pentru a nota output-ul agentului dacă este util, precis sau nu. Există și mai multe biblioteci open source care te ajută să evaluezi diferite aspecte ale agentului. De ex., [RAGAS](https://docs.ragas.io/) pentru agenți RAG sau [LLM Guard](https://llm-guard.com/) pentru a detecta limbaj dăunător sau injecția de prompturi.

În practică, o combinație a acestor metrici oferă cea mai bună acoperire a stării de sănătate a unui agent AI. În [notebookul exemplu](./code_samples/10-expense_claim-demo.ipynb) din acest capitol, îți vom arăta cum arată aceste metrici în exemple reale, dar mai întâi vom învăța cum arată un flux tipic de evaluare.

## Instrumentează-ți agentul

Pentru a colecta date de trasare, va trebui să instrumentezi codul tău. Scopul este să instrumentezi codul agentului pentru a emite trasee și metrici care pot fi capturate, procesate și vizualizate de o platformă de observabilitate.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) a devenit un standard industrial pentru observabilitatea LLM. Oferă un set de API-uri, SDK-uri și unelte pentru generarea, colectarea și exportarea datelor de telemetrie.

Există multe biblioteci de instrumentare care înfășoară cadrele existente de agent și facilitează exportul span-urilor OpenTelemetry către un instrument de observabilitate. Microsoft Agent Framework se integrează nativ cu OpenTelemetry. Mai jos este un exemplu de instrumentare a unui agent MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Executarea agentului este urmărită automat
    pass
```

[Notebookul exemplu](./code_samples/10-expense_claim-demo.ipynb) din acest capitol va demonstra cum să instrumentezi agentul tău MAF.

**Crearea manuală a span-urilor:** Deși bibliotecile de instrumentare oferă un punct de pornire bun, există cazuri în care sunt necesare informații mai detaliate sau personalizate. Poți crea manual span-uri pentru a adăuga logică aplicațională personalizată. Mai important, pot îmbogăți span-urile create automat sau manual cu atribute personalizate (cunoscute și ca tag-uri sau metadate). Aceste atribute pot include date specifice de business, calcule intermediare sau orice context util pentru depanare sau analiză, cum ar fi `user_id`, `session_id` sau `model_version`.

Exemplu de creare manuală a traseelor și span-urilor cu [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluarea agentului

Observabilitatea ne oferă metrici, dar evaluarea este procesul de analiză a acestor date (și de efectuare a testelor) pentru a determina cât de bine performează un agent AI și cum poate fi îmbunătățit. Cu alte cuvinte, odată ce ai aceste trasee și metrici, cum le folosești pentru a judeca agentul și a lua decizii?

Evaluarea regulată este importantă deoarece agenții AI sunt adesea nedeterministici și pot evolua (prin actualizări sau schimbări în comportamentul modelului) – fără evaluare, nu ai ști dacă „agentul tău inteligent” chiar își face bine treaba sau dacă a regresat.

Există două categorii de evaluări pentru agenții AI: **evaluare online** și **evaluare offline**. Ambele sunt valoroase și se completează reciproc. De obicei începem cu evaluarea offline, deoarece este pasul minim necesar înainte de a implementa orice agent.

### Evaluarea offline

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Aceasta presupune evaluarea agentului într-un mediu controlat, de obicei folosind seturi de date de test, nu întrebări live ale utilizatorilor. Folosești seturi de date atent alese în care știi care este rezultatul așteptat sau comportamentul corect și apoi rulezi agentul pe acestea.

De exemplu, dacă ai construit un agent pentru probleme matematice cu text, ai putea avea un [set de date de test](https://huggingface.co/datasets/gsm8k) cu 100 de probleme cu răspunsuri cunoscute. Evaluarea offline este făcută adesea în timpul dezvoltării (și poate face parte din pipeline-urile CI/CD) pentru a verifica îmbunătățirile sau pentru a preveni regresiile. Avantajul este că este **repetabilă și poți obține metrici clare de acuratețe deoarece ai ground truth**. Poți, de asemenea, să simulezi întrebări ale utilizatorilor și să măsori răspunsurile agentului față de răspunsuri ideale sau să folosești metricile automate descrise mai sus.

Provocarea principală a evaluării offline este asigurarea faptului că setul tău de date de test este cuprinzător și rămâne relevant – agentul poate performa bine pe un set fix de test, dar întâlni întrebări foarte diferite în producție. Prin urmare, ar trebui să actualizezi seturile de test cu cazuri noi și exemple care reflectă scenariile reale. Un amestec de seturi mici de „smoke test” și seturi mai mari de evaluare este util: seturi mici pentru verificări rapide și seturi mai mari pentru metrici de performanță mai largi.

### Evaluarea online

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Aceasta se referă la evaluarea agentului într-un mediu live, din lumea reală, adică în timpul utilizării efective în producție. Evaluarea online implică monitorizarea performanței agentului în interacțiunile reale cu utilizatorii și analiza continuă a rezultatelor.

De exemplu, ai putea urmări ratele de succes, scorurile de satisfacție ale utilizatorilor sau alte metrici pe traficul live. Avantajul evaluării online este că **capturarea unor aspecte pe care nu le-ai anticipa într-un mediu de laborator** – poți observa deriva modelului în timp (dacă eficiența agentului scade pe măsură ce diverși factori de intrare se schimbă) și poți prinde întrebări neașteptate sau situații care nu erau în datele de test. Oferă o imagine reală a modului în care se comportă agentul în sălbăticie.

Evaluarea online implică adesea colectarea feedback-ului implicit și explicit de la utilizatori, așa cum am discutat, și posibil rularea de teste shadow sau A/B (unde o nouă versiune a agentului rulează în paralel pentru a fi comparată cu vechea). Provocarea este că poate fi dificil să obții etichete sau scoruri fiabile pentru interacțiunile live – te poți baza pe feedback-ul utilizatorilor sau pe metrici downstream (de exemplu, dacă utilizatorul a făcut clic pe rezultat).

### Combinarea celor două

Evaluările online și offline nu sunt mutual exclusive; ele sunt complementare. Informațiile din monitorizarea online (de exemplu, noi tipuri de întrebări ale utilizatorilor unde agentul performează slab) pot fi folosite pentru a augmenta și îmbunătăți seturile de date de test offline. Invers, agenții care performează bine în testele offline pot fi implementați mai încrezător și monitorizați online.

De fapt, multe echipe adoptă o buclă:

_evaluare offline -> implementare -> monitorizare online -> colectare noi cazuri de eșec -> adăugare în dataset-ul offline -> rafinare agent -> repetare_.

## Probleme comune

Pe măsură ce implementezi agenți AI în producție, poți întâmpina diverse provocări. Iată câteva probleme comune și posibilele lor soluții:

| **Problemă**    | **Soluție potențială**   |
| ------------- | ------------------ |
| Agent AI care nu realizează sarcinile în mod consecvent | - Rafinează promptul dat agentului AI; fii clar cu obiectivele.<br>- Identifică dacă împărțirea sarcinilor în subtask-uri și gestionarea lor de către mai mulți agenți poate ajuta. |
| Agent AI care intră în bucle continue  | - Asigură-te că ai termeni și condiții clare de terminare astfel încât agentul să știe când să oprească procesul.<br>- Pentru sarcini complexe ce necesită raționament și planificare, folosește un model mai mare specializat în astfel de sarcini. |
| Apelurile agentului către instrumente nu funcționează bine   | - Testează și validează ieșirea instrumentului în afara sistemului agentului.<br>- Rafinează parametrii definiți, prompturile și denumirile instrumentelor.  |
| Sistem multi-agent care nu performează consistent | - Rafinează prompturile date fiecărui agent pentru a fi specifice și distincte între ele.<br>- Construiește un sistem ierarhic folosind un agent „de rutare” sau controller pentru a determina care agent este cel corect. |

Multe dintre aceste probleme pot fi identificate mai eficient cu observabilitate activă. Traseele și metricile discutate anterior ajută la localizarea exactă a problemelor în fluxul de lucru al agentului, făcând depanarea și optimizarea mult mai eficiente.

## Gestionarea costurilor
Iată câteva strategii pentru gestionarea costurilor de implementare a agenților AI în producție:

**Folosirea modelelor mai mici:** Modelele de limbaj mici (SLM) pot performa bine în anumite cazuri de utilizare agentică și vor reduce costurile semnificativ. După cum s-a menționat anterior, construirea unui sistem de evaluare pentru a determina și compara performanța față de modelele mai mari este cea mai bună metodă de a înțelege cât de bine va performa un SLM în cazul tău de utilizare. Ia în considerare utilizarea SLM-urilor pentru sarcini mai simple, cum ar fi clasificarea intenției sau extragerea parametrilor, rezervând modelele mai mari pentru raționamente complexe.

**Folosirea unui model de rutare:** O strategie similară este să folosești o diversitate de modele și mărimi. Poți folosi un LLM/SLM sau o funcție serverless pentru a direcționa cererile în funcție de complexitate către modelele cele mai potrivite. Acest lucru va ajuta, de asemenea, la reducerea costurilor, asigurând în același timp performanță pentru sarcinile potrivite. De exemplu, direcționează interogările simple către modele mai mici și mai rapide și utilizează modelele mari și costisitoare doar pentru sarcinile de raționament complexe.

**Stocarea răspunsurilor în cache:** Identificarea cererilor și a sarcinilor comune și furnizarea răspunsurilor înainte ca acestea să ajungă prin sistemul tău agentic este o metodă bună de a reduce volumul cererilor similare. Poți chiar implementa un flux pentru a identifica cât de similară este o cerere față de cele stocate în cache folosind modele AI mai simple. Această strategie poate reduce semnificativ costurile pentru întrebările frecvente sau pentru fluxurile de lucru comune.

## Să vedem cum funcționează asta în practică

În [notebook-ul exemplu din această secțiune](./code_samples/10-expense_claim-demo.ipynb), vom vedea exemple despre cum putem folosi unelte de observabilitate pentru a monitoriza și evalua agentul nostru.


### Ai Mai Multe Întrebări despre Agenții AI în Producție?

Alătură-te [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la sesiuni de întrebări și a primi răspunsuri la întrebările tale despre Agenții AI.

## Lecția Anterioară

[Metacognition Design Pattern](../09-metacognition/README.md)

## Lecția Următoare

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertisment**:
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->