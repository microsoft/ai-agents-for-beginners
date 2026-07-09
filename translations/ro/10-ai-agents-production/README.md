# Agenții AI în Producție: Observabilitate & Evaluare

[![Agenții AI în Producție](../../../translated_images/ro/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Pe măsură ce agenții AI trec de la prototipuri experimentale la aplicații reale, abilitatea de a înțelege comportamentul lor, de a le monitoriza performanța și de a evalua sistematic rezultatele devine importantă.

## Obiective de învățare

După finalizarea acestei lecții, veți ști/cunoaște:
- Concepute de bază ale observabilității și evaluării agenților
- Tehnici pentru îmbunătățirea performanței, costurilor și eficienței agenților
- Ce și cum să evaluați agenții dvs. AI în mod sistematic
- Cum să controlați costurile atunci când implementați agenți AI în producție
- Cum să instrumentați agenții construiți cu Microsoft Agent Framework

Scopul este de a vă dota cu cunoștințele necesare pentru a transforma agenții "cutie neagră" în sisteme transparente, gestionabile și de încredere.

_**Notă:** Este important să implementați agenți AI care sunt siguri și demni de încredere. Consultați și lecția [Construirea Agenților AI Demni de Încredere](../06-building-trustworthy-agents/README.md)._

## Trasee și Intervaluri

Unelte de observabilitate precum [Langfuse](https://langfuse.com/) sau [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) reprezintă de obicei rulările agenților ca trasee și intervaluri.

- **Traseul** reprezintă o sarcină completă a agentului de la început până la sfârșit (cum ar fi gestionarea unei întrebări a utilizatorului).
- **Intervalurile** sunt pași individuali în cadrul traseului (cum ar fi apelarea unui model de limbaj sau recuperarea datelor).

![Arborele traseului în Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Fără observabilitate, un agent AI poate părea o „cutie neagră” - starea internă și raționamentul său sunt opace, ceea ce face dificilă diagnosticarea problemelor sau optimizarea performanței. Cu observabilitatea, agenții devin „cutii de sticlă”, oferind transparență vitală pentru a construi încredere și a asigura funcționarea conform intenției.

## De ce este importantă observabilitatea în mediile de producție

Tranziția agenților AI în mediile de producție introduce un set nou de provocări și cerințe. Observabilitatea nu mai este doar un „lucru plăcut de avut”, ci o capacitate critică:

*   **Depanare și Analiza Cauzei Principale**: Când un agent eșuează sau produce un rezultat neașteptat, uneltele de observabilitate oferă traseele necesare pentru a identifica sursa erorii. Acest lucru este deosebit de important în agenți complexi care pot implica multiple apeluri LLM, interacțiuni cu unelte și logică condiționată.
*   **Gestionarea întârzierilor și a costurilor**: Agenții AI se bazează adesea pe LLM-uri și alte API-uri externe facturate per token sau per apel. Observabilitatea permite urmărirea precisă a acestor apeluri, ajutând la identificarea operațiunilor excesiv de lente sau scumpe. Acest lucru permite echipelor să optimizeze prompturile, să selecteze modele mai eficiente sau să redeseneze fluxurile de lucru pentru a gestiona costurile operaționale și a asigura o experiență bună pentru utilizatori.
*   **Încredere, Siguranță și Conformitate**: În multe aplicații, este esențial să asigurați că agenții se comportă în mod sigur și etic. Observabilitatea furnizează o pistă de audit a acțiunilor și deciziilor agentului. Aceasta poate fi folosită pentru a detecta și atenua probleme precum injectarea de prompturi, generarea de conținut dăunător sau manipularea necorespunzătoare a informațiilor personale identificabile (PII). De exemplu, puteți analiza traseele pentru a înțelege de ce un agent a oferit un anumit răspuns sau a folosit o anumită unealtă.
*   **Bucle de Îmbunătățire Continuă**: Datele de observabilitate stau la baza unui proces de dezvoltare iterativ. Prin monitorizarea performanței agenților în lumea reală, echipele pot identifica zonele care necesită îmbunătățiri, pot colecta date pentru ajustarea fină a modelelor și valida impactul schimbărilor. Aceasta creează un ciclu de feedback prin care informațiile din producție obținute din evaluarea online informează experimentarea și rafinamentul offline, conducând la o performanță progresiv mai bună a agentului.

## Metrii Cheie de Urmărit

Pentru a monitoriza și înțelege comportamentul agentului, trebuie urmărite o gamă de metrii și semnale. Deși metrii specifici pot varia în funcție de scopul agentului, unele sunt universal importante.

Iată câțiva dintre cei mai comuni metrii monitorizați de uneltele de observabilitate:

**Întârziere:** Cât de rapid răspunde agentul? Timpurile lungi de așteptare afectează negativ experiența utilizatorului. Trebuie să măsurați întârzierea pentru sarcini și pași individuali urmărind rulările agentului. De exemplu, un agent care durează 20 de secunde pentru toate apelurile către modele poate fi accelerat folosind un model mai rapid sau prin executarea apelurilor în paralel.

**Costuri:** Care este cheltuiala per rulare a agentului? Agenții AI se bazează pe apeluri LLM facturate per token sau pe API-uri externe. Utilizarea frecventă a uneltelor sau a mai multor prompturi poate crește rapid costurile. De exemplu, dacă un agent apelează un LLM de cinci ori pentru o îmbunătățire marginală a calității, trebuie să evaluați dacă costul este justificat sau dacă puteți reduce numărul apelurilor ori să folosiți un model mai ieftin. Monitorizarea în timp real poate ajuta, de asemenea, la identificarea creșterilor neașteptate (de ex. bug-uri care cauzează bucle excesive de API).

**Erori de solicitare:** Câte solicitări a eșuat agentul să proceseze? Acest lucru poate include erori API sau apeluri eșuate ale uneltelor. Pentru a face agentul mai robust în producție, puteți configura mecanisme de fallback sau reîncercare. De ex. dacă furnizorul LLM A nu funcționează, comutați pe furnizorul LLM B ca rezervă.

**Feedback-ul Utilizatorului:** Implementarea evaluărilor directe oferă informații valoroase. Aceasta poate include ratinguri explicite (👍thumbs-up/👎down, ⭐1-5 stele) sau comentarii textuale. Feedback-ul negativ consecvent ar trebui să vă alerteze, indicând că agentul nu funcționează conform așteptărilor. 

**Feedback-ul Implicit al Utilizatorului:** Comportamentele utilizatorilor oferă feedback indirect chiar și fără ratinguri explicite. Aceasta poate include reformularea imediată a întrebărilor, întrebări repetate sau apăsarea unui buton de retry. De ex. dacă observați că utilizatorii repetă aceeași întrebare, este un semn că agentul nu funcționează cum trebuie.

**Acuratețe:** Cât de frecvent produce agentul rezultate corecte sau dorite? Definițiile acurateței variază (de ex., corectitudinea rezolvării problemelor, precizia recuperării informațiilor, satisfacția utilizatorului). Primul pas este să definiți ce înseamnă succesul pentru agentul dvs. Puteți monitoriza acuratețea prin verificări automate, scoruri de evaluare sau etichete de finalizare a sarcinilor. De exemplu, marcarea traseelor ca „reușite” sau „eșuate”. 

**Metrii de Evaluare Automată:** Puteți, de asemenea, să configurați evaluări automate. De exemplu, puteți folosi un LLM pentru a evalua outputul agentului, dacă acesta este util, precis sau nu. Există și biblioteci open source care vă ajută să evaluați diferite aspecte ale agentului. De ex. [RAGAS](https://docs.ragas.io/) pentru agenți RAG sau [LLM Guard](https://llm-guard.com/) pentru detectarea limbajului dăunător sau a injectării de prompturi.

În practică, o combinație a acestor metrii oferă cea mai bună acoperire a stării de sănătate a unui agent AI. În [notebook-ul exemplu](./code_samples/10-expense_claim-demo.ipynb) din acest capitol, vă vom arăta cum arată acești metrii în exemple reale, dar mai întâi vom învăța cum arată un flux tipic de evaluare.

## Instrumentați Agentul

Pentru a colecta date de trasare, va trebui să instrumentați codul. Scopul este să instrumentați codul agentului pentru a emite trasee și metrii care pot fi capturați, procesați și vizualizați de o platformă de observabilitate.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) a devenit un standard în industrie pentru observabilitatea LLM. Oferă un set de API-uri, SDK-uri și unelte pentru generarea, colectarea și exportul datelor de telemetrie.

Există multe biblioteci de instrumentare care înfășoară framework-uri existente de agenți și facilitează exportul intervalurilor OpenTelemetry către o unealtă de observabilitate. Microsoft Agent Framework se integrează nativ cu OpenTelemetry. Mai jos este un exemplu de instrumentare a unui agent MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Execuția agentului este urmărită automat
    pass
```

Notebook-ul [exemplu](./code_samples/10-expense_claim-demo.ipynb) din acest capitol va demonstra cum să instrumentați agentul MAF.

**Crearea Manuală a Intervalelor:** Deși bibliotecile de instrumentare oferă o bază bună, adesea există situații care necesită informații mai detaliate sau personalizate. Puteți crea manual intervale pentru a adăuga logică personalizată aplicației. Mai important, puteți îmbogăți intervalele create automat sau manual cu atribute personalizate (cunoscut și ca taguri sau metadata). Aceste atribute pot include date specifice afacerii, calcule intermediare sau orice context util pentru depanare sau analiză, cum ar fi `user_id`, `session_id` sau `model_version`.

Exemplu de creare manuală a traseelor și intervalelor cu [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluarea Agentului

Observabilitatea ne oferă metrii, dar evaluarea este procesul de analizare a acestor date (și efectuare a testelor) pentru a determina cât de bine performează un agent AI și cum poate fi îmbunătățit. Cu alte cuvinte, odată ce aveți traseele și metrii, cum îi folosiți pentru a judeca agentul și a lua decizii?

Evaluarea regulată este importantă deoarece agenții AI sunt adesea non-deterministici și pot evolua (prin actualizări sau schimbări în comportamentul modelului) — fără evaluare, nu ați ști dacă „agentul inteligent” își face bine treaba sau dacă a regresat.

Există două categorii de evaluări pentru agenții AI: **evaluare online** și **evaluare offline**. Ambele sunt valoroase și se completează reciproc. De obicei, începem cu evaluarea offline, deoarece este pasul minim necesar înainte de a implementa orice agent.

### Evaluarea offline

![Elemente din setul de date în Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Aceasta implică evaluarea agentului într-un mediu controlat, de obicei folosind seturi de date de test, nu întrebări live ale utilizatorilor. Folosiți seturi de date curate unde știți care este rezultatul așteptat sau comportamentul corect, apoi rulați agentul pe acestea.

De exemplu, dacă ați creat un agent pentru probleme matematice, ați putea avea un [set de date de test](https://huggingface.co/datasets/gsm8k) cu 100 de probleme cu răspunsuri cunoscute. Evaluarea offline se face adesea în timpul dezvoltării (și poate face parte din pipeline-uri CI/CD) pentru a verifica îmbunătățirile sau pentru a preveni regresiile. Avantajul este că este **repetabilă și puteți obține metrii clari de acuratețe deoarece aveți adevărul de bază**. De asemenea, puteți simula întrebările utilizatorilor și măsura răspunsurile agentului în raport cu răspunsurile ideale sau folosi metrii automați, așa cum s-a descris mai sus.

Provocarea principală cu evaluarea offline este asigurarea că setul dvs. de date de test este cuprinzător și rămâne relevant - agentul poate performa bine pe un set fix de test, dar să întâmpine întrebări foarte diferite în producție. Prin urmare, ar trebui să actualizați seturile de test cu noi cazuri limită și exemple care reflectă scenariile din lumea reală​. Un amestec de seturi mici „smoke test” și seturi mai mari de evaluare este util: seturi mici pentru verificări rapide și seturi mai mari pentru metrii mai largi de performanță​.

### Evaluarea online

![Prezentare generală a metricilor de observabilitate](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Aceasta se referă la evaluarea agentului într-un mediu live, din lumea reală, adică în timpul utilizării reale în producție. Evaluarea online implică monitorizarea performanței agentului pe interacțiuni reale cu utilizatorii și analizarea continuă a rezultatelor.

De exemplu, puteți urmări ratele de reușită, scorurile de satisfacție ale utilizatorilor sau alți metri pe traficul live. Avantajul evaluării online este că **prinde aspecte pe care nu le-ați putea anticipa într-un mediu de laborator** – puteți observa deriva modelului în timp (dacă eficiența agentului scade pe măsură ce modelele de intrare se schimbă) și puteți surprinde întrebări sau situații neașteptate care nu erau în datele dvs. de test​. Oferă o imagine reală despre cum se comportă agentul în condiții reale.

Evaluarea online implică adesea colectarea atât a feedback-ului implicit, cât și explicit al utilizatorilor, așa cum s-a discutat, și posibil rularea testelor de tip shadow sau A/B (unde o versiune nouă a agentului rulează în paralel pentru a fi comparată cu cea veche). Provocarea este că poate fi dificil să obțineți etichete sau scoruri fiabile pentru interacțiunile live – s-ar putea să vă bazați pe feedback-ul utilizatorilor sau pe metrii downstream (de exemplu, dacă utilizatorul a dat click pe rezultat).

### Combinarea celor două

Evaluările online și offline nu se exclud reciproc; ele sunt foarte complementare. Informațiile din monitorizarea online (de exemplu, noi tipuri de întrebări ale utilizatorului unde agentul performează slab) pot fi folosite pentru a îmbunătăți seturile de date de test offline. În mod invers, agenții care performează bine în testele offline pot fi implementați și monitorizați cu mai multă încredere online.

De fapt, multe echipe adoptă un ciclu: 

_evaluați offline -> implementați -> monitorizați online -> colectați cazuri noi de eșec -> adăugați la setul de date offline -> rafinați agentul -> repetați_.

## Probleme Comune

Pe măsură ce implementați agenți AI în producție, este posibil să întâmpinați diverse provocări. Iată câteva probleme comune și soluțiile lor potențiale:

| **Problemă**    | **Soluție Potențială**   |
| ------------- | ------------------ |
| Agent AI care nu realizează sarcinile în mod consecvent | - Raționați promptul dat agentului AI; fiți clar cu obiectivele.<br>- Identificați unde fragmentarea sarcinilor în subtasks și gestionarea lor de către agenți multipli poate ajuta. |
| Agent AI prinde bucle continue  | - Asigurați-vă că există termeni și condiții clare de terminare, astfel încât agentul să știe când să oprească procesul.<br>- Pentru sarcini complexe care necesită raționament și planificare, folosiți un model mai mare specializat pentru astfel de sarcini. |
| Apeluri către unelte ale agentului AI care nu performează bine   | - Testați și validați outputul uneltei în afara sistemului agent.<br>- Raționați parametrii definiți, prompturile și denumirile uneltelor.  |
| Sistem Multi-Agent care nu performează consecvent | - Raționați prompturile oferite fiecărui agent pentru a fi specifice și distincte între ele.<br>- Construiți un sistem ierarhic folosind un agent „router” sau controller pentru a determina care agent este cel corect. |

Multe din aceste probleme pot fi identificate mai eficient cu observabilitatea activă. Traseele și metrii discutați anterior ajută la identificarea precisă a punctului din fluxul de lucru al agentului unde apar problemele, făcând depanarea și optimizarea mult mai eficiente.

## Gestionarea Costurilor


Iată câteva strategii pentru gestionarea costurilor de implementare a agenților AI în producție:

**Folosirea modelelor mai mici:** Modelele mici de limbaj (SLM) pot performa bine în anumite cazuri de utilizare agentică și vor reduce semnificativ costurile. După cum s-a menționat mai devreme, construirea unui sistem de evaluare pentru a determina și compara performanța față de modelele mai mari este cea mai bună cale de a înțelege cât de bine se va descurca un SLM pe cazul tău de utilizare. Ia în considerare folosirea SLM-urilor pentru sarcini mai simple, cum ar fi clasificarea intențiilor sau extragerea parametrilor, rezervând modelele mai mari pentru raționamente complexe.

**Folosirea unui model router:** O strategie similară este utilizarea unei diversități de modele și dimensiuni. Poți folosi un LLM/SLM sau o funcție serverless pentru a direcționa cererile în funcție de complexitate către cele mai potrivite modele. Acest lucru va ajuta și la reducerea costurilor, asigurând în același timp performanța optimă pentru sarcinile corespunzătoare. De exemplu, direcționează întrebările simple către modele mai mici și mai rapide și utilizează modele mari, costisitoare, doar pentru sarcini de raționament complex.

**Stocarea în cache a răspunsurilor:** Identificarea cererilor și sarcinilor comune și furnizarea răspunsurilor înainte ca acestea să treacă prin sistemul tău agentic este o modalitate bună de a reduce volumul cererilor similare. Poți chiar implementa un flux pentru a identifica cât de asemănătoare este o cerere cu solicitările tale stocate în cache folosind modele AI mai simple. Această strategie poate reduce semnificativ costurile pentru întrebările frecvente sau fluxurile de lucru comune.

## Să vedem cum funcționează asta în practică

În [notebook-ul exemplu al acestei secțiuni](./code_samples/10-expense_claim-demo.ipynb), vom vedea exemple despre cum putem folosi instrumentele de observabilitate pentru a monitoriza și evalua agentul nostru.


### Ai mai multe întrebări despre agenții AI în producție?

Alătură-te [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la sesiuni de tip office hours și a primi răspunsuri la întrebările tale despre agenții AI.

## Lecția anterioară

[Pattern-ul de Design Metacognition](../09-metacognition/README.md)

## Următoarea lecție

[Protocoalele Agentice](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->