<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-24T09:02:46+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "ro"
}
-->
# Agenți AI în Producție: Observabilitate și Evaluare

Pe măsură ce agenții AI trec de la prototipuri experimentale la aplicații din lumea reală, abilitatea de a înțelege comportamentul lor, de a le monitoriza performanța și de a le evalua sistematic rezultatele devine esențială.

## Obiective de Învățare

După finalizarea acestei lecții, vei ști cum să/vei înțelege:
- Conceptele de bază ale observabilității și evaluării agenților
- Tehnici pentru îmbunătățirea performanței, costurilor și eficienței agenților
- Ce și cum să evaluezi sistematic agenții AI
- Cum să controlezi costurile atunci când implementezi agenți AI în producție
- Cum să instrumentezi agenții construiți cu AutoGen

Scopul este să te echipezi cu cunoștințele necesare pentru a transforma agenții "cutie neagră" în sisteme transparente, gestionabile și de încredere.

_**Notă:** Este important să implementezi agenți AI care sunt siguri și de încredere. Consultă lecția [Construirea Agenților AI de Încredere](./06-building-trustworthy-agents/README.md) pentru mai multe detalii._

## Trasee și Etape

Instrumentele de observabilitate precum [Langfuse](https://langfuse.com/) sau [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) reprezintă de obicei rulările agenților sub formă de trasee și etape.

- **Traseu** reprezintă o sarcină completă a agentului de la început până la sfârșit (de exemplu, gestionarea unei interogări a utilizatorului).
- **Etape** sunt pașii individuali din cadrul traseului (de exemplu, apelarea unui model lingvistic sau recuperarea datelor).

![Arbore de trasee în Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Fără observabilitate, un agent AI poate părea o "cutie neagră" – starea sa internă și raționamentul sunt opace, ceea ce face dificilă diagnosticarea problemelor sau optimizarea performanței. Cu observabilitate, agenții devin "cutii de sticlă," oferind transparență esențială pentru a construi încredere și a asigura funcționarea lor conform intenției.

## De ce Contează Observabilitatea în Mediile de Producție

Trecerea agenților AI în medii de producție introduce un nou set de provocări și cerințe. Observabilitatea nu mai este un "lux," ci o capacitate critică:

*   **Depanare și Analiză a Cauzei Rădăcină:** Când un agent eșuează sau produce un rezultat neașteptat, instrumentele de observabilitate oferă traseele necesare pentru a identifica sursa erorii. Acest lucru este deosebit de important în cazul agenților complecși care pot implica multiple apeluri LLM, interacțiuni cu instrumente și logică condiționată.
*   **Gestionarea Latentei și a Costurilor:** Agenții AI se bazează adesea pe LLM-uri și alte API-uri externe care sunt taxate pe token sau pe apel. Observabilitatea permite urmărirea precisă a acestor apeluri, ajutând la identificarea operațiunilor excesiv de lente sau costisitoare. Acest lucru permite echipelor să optimizeze prompturile, să selecteze modele mai eficiente sau să reproiecteze fluxurile de lucru pentru a gestiona costurile operaționale și a asigura o experiență bună pentru utilizator.
*   **Încredere, Siguranță și Conformitate:** În multe aplicații, este important să te asiguri că agenții se comportă în siguranță și etic. Observabilitatea oferă o pistă de audit a acțiunilor și deciziilor agentului. Aceasta poate fi utilizată pentru a detecta și a atenua probleme precum injecția de prompturi, generarea de conținut dăunător sau gestionarea necorespunzătoare a informațiilor personale identificabile (PII). De exemplu, poți revizui traseele pentru a înțelege de ce un agent a oferit un anumit răspuns sau a utilizat un anumit instrument.
*   **Buclă de Îmbunătățire Continuă:** Datele de observabilitate sunt fundamentul unui proces de dezvoltare iterativ. Monitorizând modul în care agenții performează în lumea reală, echipele pot identifica zonele de îmbunătățire, colecta date pentru ajustarea fină a modelelor și valida impactul modificărilor. Acest lucru creează o buclă de feedback în care perspectivele din evaluarea online informează experimentarea și rafinarea offline, conducând la o performanță progresiv mai bună a agenților.

## Metrici Cheie de Urmărit

Pentru a monitoriza și înțelege comportamentul agenților, ar trebui urmărită o gamă de metrici și semnale. Deși metricele specifice pot varia în funcție de scopul agentului, unele sunt universal importante.

Iată câteva dintre cele mai comune metrici pe care instrumentele de observabilitate le monitorizează:

**Latenta:** Cât de rapid răspunde agentul? Timpurile lungi de așteptare afectează negativ experiența utilizatorului. Ar trebui să măsori latenta pentru sarcini și pași individuali prin trasarea rulărilor agentului. De exemplu, un agent care durează 20 de secunde pentru toate apelurile modelului ar putea fi accelerat utilizând un model mai rapid sau rulând apelurile modelului în paralel.

**Costuri:** Care este costul per rulare a agentului? Agenții AI se bazează pe apeluri LLM taxate pe token sau API-uri externe. Utilizarea frecventă a instrumentelor sau multiplele prompturi pot crește rapid costurile. De exemplu, dacă un agent apelează un LLM de cinci ori pentru o îmbunătățire marginală a calității, trebuie să evaluezi dacă costul este justificat sau dacă poți reduce numărul de apeluri sau utiliza un model mai ieftin. Monitorizarea în timp real poate ajuta, de asemenea, la identificarea vârfurilor neașteptate (de exemplu, erori care cauzează bucle excesive de API).

**Erori de Cerere:** Câte cereri a eșuat agentul? Acestea pot include erori API sau apeluri de instrumente eșuate. Pentru a face agentul mai robust în producție, poți configura mecanisme de rezervă sau reîncercări. De exemplu, dacă furnizorul LLM A este indisponibil, treci la furnizorul LLM B ca rezervă.

**Feedback-ul Utilizatorului:** Implementarea evaluărilor directe ale utilizatorilor oferă perspective valoroase. Acestea pot include evaluări explicite (👍thumbs-up/👎down, ⭐1-5 stele) sau comentarii textuale. Feedback-ul negativ constant ar trebui să te alerteze, deoarece acesta este un semn că agentul nu funcționează conform așteptărilor.

**Feedback-ul Implicit al Utilizatorului:** Comportamentele utilizatorilor oferă feedback indirect chiar și fără evaluări explicite. Acestea pot include reformularea imediată a întrebărilor, interogări repetate sau apăsarea unui buton de reîncercare. De exemplu, dacă observi că utilizatorii pun aceeași întrebare în mod repetat, acesta este un semn că agentul nu funcționează conform așteptărilor.

**Acuratețe:** Cât de frecvent produce agentul rezultate corecte sau dorite? Definițiile acurateței variază (de exemplu, corectitudinea rezolvării problemelor, acuratețea recuperării informațiilor, satisfacția utilizatorului). Primul pas este să definești cum arată succesul pentru agentul tău. Poți urmări acuratețea prin verificări automate, scoruri de evaluare sau etichete de finalizare a sarcinilor. De exemplu, marcarea traseelor ca "reușite" sau "eșuate."

**Metrici de Evaluare Automată:** Poți configura, de asemenea, evaluări automate. De exemplu, poți utiliza un LLM pentru a evalua rezultatul agentului, de exemplu, dacă este util, precis sau nu. Există, de asemenea, mai multe biblioteci open-source care te ajută să evaluezi diferite aspecte ale agentului. De exemplu, [RAGAS](https://docs.ragas.io/) pentru agenți RAG sau [LLM Guard](https://llm-guard.com/) pentru a detecta limbajul dăunător sau injecția de prompturi.

În practică, o combinație a acestor metrici oferă cea mai bună acoperire a sănătății unui agent AI. În [notebook-ul exemplu](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) din acest capitol, vom arăta cum arată aceste metrici în exemple reale, dar mai întâi vom învăța cum arată un flux de lucru tipic de evaluare.

## Instrumentarea Agentului

Pentru a colecta date de trasare, va trebui să instrumentezi codul. Scopul este să instrumentezi codul agentului pentru a emite trasee și metrici care pot fi capturate, procesate și vizualizate de o platformă de observabilitate.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) a devenit un standard în industrie pentru observabilitatea LLM. Acesta oferă un set de API-uri, SDK-uri și instrumente pentru generarea, colectarea și exportarea datelor de telemetrie.

Există multe biblioteci de instrumentare care înfășoară cadrele existente ale agenților și fac ușoară exportarea etapelor OpenTelemetry către un instrument de observabilitate. Mai jos este un exemplu de instrumentare a unui agent AutoGen cu biblioteca de instrumentare [OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[Notebook-ul exemplu](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) din acest capitol va demonstra cum să instrumentezi un agent AutoGen.

**Crearea Manuală a Etapelor:** Deși bibliotecile de instrumentare oferă o bază bună, există adesea cazuri în care sunt necesare informații mai detaliate sau personalizate. Poți crea manual etape pentru a adăuga logică personalizată a aplicației. Mai important, acestea pot îmbogăți etapele create automat sau manual cu atribute personalizate (cunoscute și sub numele de etichete sau metadate). Aceste atribute pot include date specifice afacerii, calcule intermediare sau orice context care ar putea fi util pentru depanare sau analiză, cum ar fi `user_id`, `session_id` sau `model_version`.

Exemplu de creare manuală a traseelor și etapelor cu [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluarea Agenților

Observabilitatea ne oferă metrici, dar evaluarea este procesul de analizare a acestor date (și efectuarea de teste) pentru a determina cât de bine performează un agent AI și cum poate fi îmbunătățit. Cu alte cuvinte, odată ce ai traseele și metricile, cum le folosești pentru a judeca agentul și a lua decizii?

Evaluarea regulată este importantă deoarece agenții AI sunt adesea nedeterministici și pot evolua (prin actualizări sau modificări ale comportamentului modelului) – fără evaluare, nu ai ști dacă "agentul inteligent" își face treaba bine sau dacă a regresat.

Există două categorii de evaluări pentru agenții AI: **evaluare offline** și **evaluare online**. Ambele sunt valoroase și se completează reciproc. De obicei, începem cu evaluarea offline, deoarece acesta este pasul minim necesar înainte de a implementa orice agent.

### Evaluare Offline

![Elemente ale setului de date în Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Aceasta implică evaluarea agentului într-un mediu controlat, utilizând de obicei seturi de date de testare, nu interogări live ale utilizatorilor. Folosești seturi de date curate unde știi care este rezultatul așteptat sau comportamentul corect și apoi rulezi agentul pe acestea.

De exemplu, dacă ai construit un agent pentru probleme de matematică, ai putea avea un [set de date de testare](https://huggingface.co/datasets/gsm8k) cu 100 de probleme cu răspunsuri cunoscute. Evaluarea offline se face adesea în timpul dezvoltării (și poate face parte din pipeline-urile CI/CD) pentru a verifica îmbunătățirile sau pentru a preveni regresele. Beneficiul este că este **repetabilă și poți obține metrici clare de acuratețe, deoarece ai un adevăr de bază**. De asemenea, ai putea simula interogări ale utilizatorilor și măsura răspunsurile agentului în raport cu răspunsurile ideale sau folosi metrici automate, așa cum s-a descris mai sus.

Provocarea cheie cu evaluarea offline este să te asiguri că setul tău de date de testare este cuprinzător și rămâne relevant – agentul ar putea performa bine pe un set de testare fix, dar să întâmpine interogări foarte diferite în producție. Prin urmare, ar trebui să menții seturile de testare actualizate cu noi cazuri limită și exemple care reflectă scenarii din lumea reală. Un mix de cazuri mici de "testare rapidă" și seturi mai mari de evaluare este util: seturi mici pentru verificări rapide și seturi mai mari pentru metrici mai ample de performanță.

### Evaluare Online 

![Prezentare generală a metricilor de observabilitate](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Aceasta se referă la evaluarea agentului într-un mediu live, din lumea reală, adică în timpul utilizării efective în producție. Evaluarea online implică monitorizarea continuă a performanței agentului pe interacțiunile reale ale utilizatorilor și analiza rezultatelor.

De exemplu, ai putea urmări ratele de succes, scorurile de satisfacție ale utilizatorilor sau alte metrici pe traficul live. Avantajul evaluării online este că **captura lucruri pe care s-ar putea să nu le anticipezi într-un mediu de laborator** – poți observa deriva modelului în timp (dacă eficacitatea agentului scade pe măsură ce modelele de intrare se schimbă) și poți detecta interogări sau situații neașteptate care nu erau în datele tale de testare. Aceasta oferă o imagine reală a modului în care agentul se comportă în mediu real.

Evaluarea online implică adesea colectarea de feedback implicit și explicit al utilizatorilor, așa cum s-a discutat, și posibil rularea de teste shadow sau A/B (unde o versiune nouă a agentului rulează în paralel pentru a fi comparată cu cea veche). Provocarea este că poate fi dificil să obții etichete sau scoruri fiabile pentru interacțiunile live – te-ai putea baza pe feedback-ul utilizatorilor sau pe metrici din aval (de exemplu, dacă utilizatorul a dat click pe rezultat).

### Combinarea celor două

Evaluările online și offline nu se exclud reciproc; ele sunt extrem de complementare. Perspectivele din monitorizarea online (de exemplu, noi tipuri de interogări ale utilizatorilor unde agentul performează slab) pot fi utilizate pentru a completa și îmbunătăți seturile de date de testare offline. Pe de altă parte, agenții care performează bine în testele offline pot fi apoi implementați și monitorizați mai încrezător online.

De fapt, multe echipe adoptă o buclă:

_evaluare offline -> implementare -> monitorizare online -> colectare de noi cazuri de eșec -> adăugare la setul de date offline -> rafinare a agentului -> repetare_.

## Probleme Comune

Pe măsură ce implementezi agenți AI în producție, este posibil să întâmpini diverse provocări. Iată câteva probleme comune și soluțiile lor potențiale:

| **Problemă**    | **Soluție Potențială**   |
| ------------- | ------------------ |
| Agentul AI nu îndeplinește sarcinile în mod constant | - Rafinează promptul oferit agentului AI; fii clar în privința obiectivelor.<br>- Identifică unde împărțirea sarcinilor în subtasks și gestionarea lor de către mai mulți agenți poate ajuta. |
| Agentul AI intră în bucle continue  | - Asigură-te că ai termeni și condiții clare de terminare, astfel încât agentul să știe când să oprească procesul.<br>- Pentru sarcini complexe care necesită raționament și planificare, folosește un model mai mare specializat pentru sarcini de raționament. |
| Apelurile instrumentelor agentului AI nu funcționează bine   | - Testează și validează ieșirea instrumentului în afara sistemului agentului. |

- Rafinează parametrii definiți, prompturile și denumirile uneltelor.  |
| Sistem multi-agent care nu funcționează constant | - Rafinează prompturile oferite fiecărui agent pentru a te asigura că sunt specifice și distincte unul de celălalt.<br>- Construiește un sistem ierarhic folosind un agent „router” sau de control pentru a determina care agent este cel potrivit. |

Multe dintre aceste probleme pot fi identificate mai eficient dacă există un sistem de observabilitate. Urmele și metricile discutate anterior ajută la identificarea exactă a locului în care apar problemele în fluxul de lucru al agentului, făcând procesul de depanare și optimizare mult mai eficient.

## Gestionarea costurilor

Iată câteva strategii pentru a gestiona costurile implementării agenților AI în producție:

**Folosirea modelelor mai mici:** Modelele de limbaj mici (SLM) pot oferi performanțe bune pentru anumite cazuri de utilizare agentice și vor reduce semnificativ costurile. După cum s-a menționat anterior, construirea unui sistem de evaluare pentru a determina și compara performanța față de modelele mai mari este cea mai bună metodă de a înțelege cât de bine se va descurca un SLM pentru cazul tău de utilizare. Ia în considerare utilizarea SLM-urilor pentru sarcini mai simple, cum ar fi clasificarea intențiilor sau extragerea parametrilor, rezervând modelele mai mari pentru raționamente complexe.

**Folosirea unui model router:** O strategie similară este utilizarea unei diversități de modele și dimensiuni. Poți folosi un LLM/SLM sau o funcție serverless pentru a direcționa cererile, în funcție de complexitate, către modelele cele mai potrivite. Aceasta va ajuta la reducerea costurilor, asigurând în același timp performanța pentru sarcinile potrivite. De exemplu, direcționează interogările simple către modele mai mici și mai rapide și folosește modelele mari și costisitoare doar pentru sarcini de raționament complex.

**Stocarea răspunsurilor în cache:** Identificarea cererilor și sarcinilor comune și furnizarea răspunsurilor înainte ca acestea să treacă prin sistemul tău agentic este o metodă bună de a reduce volumul cererilor similare. Poți chiar implementa un flux pentru a identifica cât de similară este o cerere cu cele stocate în cache folosind modele AI mai simple. Această strategie poate reduce semnificativ costurile pentru întrebările frecvente sau fluxurile de lucru comune.

## Să vedem cum funcționează în practică

În [notebook-ul exemplu al acestei secțiuni](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb), vom vedea exemple despre cum putem folosi uneltele de observabilitate pentru a monitoriza și evalua agentul nostru.

## Lecția anterioară

[Modelul de design Metacognition](../09-metacognition/README.md)

## Lecția următoare

[MCP](../11-mcp/README.md)

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru acuratețe, vă rugăm să aveți în vedere că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.