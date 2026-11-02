[![Agentic RAG](../../../translated_images/ro/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Agentic RAG

Această lecție oferă o prezentare cuprinzătoare a Agentic Retrieval-Augmented Generation (Agentic RAG), un nou paradigm AI în care modelele mari de limbaj (LLM-uri) planifică autonom următorii pași în timp ce extrag informații din surse externe. Spre deosebire de modelele statice de tip "recuperare-și-citire", Agentic RAG implică apeluri iterative către LLM, alternate cu apeluri la instrumente sau funcții și cu ieșiri structurate. Sistemul evaluează rezultatele, rafinează interogările, invocă instrumente suplimentare dacă este necesar și continuă acest ciclu până când se atinge o soluție satisfăcătoare.

## Introducere

Această lecție va acoperi

- **Înțelegerea Agentic RAG:** Aflați despre noul paradigm AI în care modelele mari de limbaj (LLM-uri) planifică autonom următorii pași în timp ce extrag informații din surse de date externe.
- **Înțelegerea stilului iterativ Maker-Checker:** Înțelegeți bucla apelurilor iterative către LLM, alternate cu apeluri la instrumente sau funcții și ieșiri structurate, concepute să îmbunătățească corectitudinea și să gestioneze interogările greșite.
- **Explorarea aplicațiilor practice:** Identificați scenarii în care Agentic RAG excelează, precum medii axate pe corectitudine, interacțiuni complexe cu baze de date și fluxuri de lucru extinse.

## Obiective de învățare

După parcurgerea acestei lecții, veți ști să/veți înțelege:

- **Înțelegerea Agentic RAG:** Aflați despre noul paradigm AI în care modelele mari de limbaj (LLM-uri) planifică autonom următorii pași în timp ce extrag informații din surse de date externe.
- **Stil iterativ Maker-Checker:** Înțelegeți conceptul unei bucle de apeluri iterative către LLM, alternate cu apeluri la instrumente sau funcții și ieșiri structurate, concepute pentru a îmbunătăți corectitudinea și a gestiona interogări greșite.
- **Deținerea procesului de raționament:** Înțelegeți capacitatea sistemului de a-și asuma procesul de raționament, luând decizii privind modul de abordare a problemelor fără a se baza pe căi predefinite.
- **Fluxul de lucru:** Înțelegeți cum un model agentic decide independent să recupereze rapoarte despre tendințele pieței, să identifice date despre concurenți, să coreleze metricile interne de vânzări, să sintetizeze concluziile și să evalueze strategia.
- **Bucle iterative, integrare de instrumente și memorie:** Aflați despre dependența sistemului de un tipar de interacțiune buclată, menținând starea și memoria pe parcursul pașilor pentru a evita bucle repetitive și a lua decizii informate.
- **Gestionarea modurilor de eșec și auto-corecția:** Explorați mecanismele robuste de auto-corecție ale sistemului, inclusiv iterarea și reinterogarea, utilizarea instrumentelor de diagnostic și revenirea la supravegherea umană.
- **Limitele agenției:** Înțelegeți limitările Agentic RAG, concentrându-vă pe autonomie specifică domeniului, dependența de infrastructură și respectarea regulilor de siguranță.
- **Cazuri practice și valoare:** Identificați scenarii în care Agentic RAG excelează, precum medii axate pe corectitudine, interacțiuni complexe cu baze de date și fluxuri de lucru extinse.
- **Guvernanță, transparență și încredere:** Aflați despre importanța guvernanței și transparenței, incluzând raționamentul explicabil, controlul prejudecăților și supravegherea umană.

## Ce este Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) este un nou paradigm AI în care modelele mari de limbaj (LLM-uri) planifică autonom următorii pași în timp ce extrag informații din surse externe. Spre deosebire de modelele statice de tip "recuperare-și-citire", Agentic RAG implică apeluri iterative către LLM, alternate cu apeluri la instrumente sau funcții și ieșiri structurate. Sistemul evaluează rezultatele, rafinează interogările, invocă instrumente suplimentare dacă e nevoie și continuă acest ciclu până când se atinge o soluție satisfăcătoare. Acest stil iterativ „maker-checker” îmbunătățește corectitudinea, gestionează interogările greșite și garantează rezultate de înaltă calitate.

Sistemul își asumă activ procesul de raționament, rescriind interogările care au eșuat, alegând metode diferite de recuperare și integrând mai multe instrumente — cum ar fi căutarea vectorială în Azure AI Search, baze de date SQL sau API-uri personalizate — înainte de a finaliza răspunsul. Calitatea distinctivă a unui sistem agentic este abilitatea sa de a-și asuma procesul de raționament. Implementările tradiționale RAG se bazează pe căi predefinite, însă un sistem agentic determină autonom secvența de pași în funcție de calitatea informațiilor pe care le găsește.

## Definirea Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) este un nou paradigm în dezvoltarea AI în care LLM-urile nu doar extrag informații din surse externe de date, ci și planifică autonom următorii pași. Spre deosebire de modelele statice „recuperare-și-citire” sau de secvențele de prompturi atent scrise, Agentic RAG implică o buclă de apeluri iterative către LLM, alternate cu apeluri la instrumente sau funcții și ieșiri structurate. La fiecare etapă, sistemul evaluează rezultatele obținute, decide dacă trebuie să rafineze interogările, invocă instrumente suplimentare dacă este necesar și continuă acest ciclu până când obține o soluție satisfăcătoare.

Acest stil iterativ „maker-checker” este conceput să îmbunătățească corectitudinea, să gestioneze interogările greșite către baze de date structurate (de exemplu NL2SQL) și să asigure rezultate echilibrate, de înaltă calitate. În loc să se bazeze doar pe lanțuri atent proiectate de prompturi, sistemul își asumă activ procesul de raționament. Poate rescrie interogările care eșuează, alege metode diferite de recuperare și integrează multiple instrumente — cum ar fi căutarea vectorială în Azure AI Search, baze de date SQL sau API-uri personalizate — înainte de a finaliza răspunsul. Acest lucru elimină necesitatea unor cadre de orchestrare prea complexe. În schimb, o buclă relativ simplă de „apel LLM → utilizare instrument → apel LLM → ..." poate genera rezultate sofisticate și bine fundamentate.

![Agentic RAG Core Loop](../../../translated_images/ro/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Asumarea procesului de raționament

Calitatea distinctivă care face ca un sistem să fie „agentic” este abilitatea sa de a-și asuma procesul de raționament. Implementările tradiționale RAG depind adesea de faptul că oamenii stabilesc dinainte o cale pentru model: un lanț de gândire care detaliază ce să recupereze și când.
Însă când un sistem este cu adevărat agentic, el decide intern cum să abordeze problema. Nu doar execută un script; determină autonom secvența de pași în funcție de calitatea informațiilor găsite.
De exemplu, dacă i se cere să creeze o strategie de lansare a unui produs, nu se bazează doar pe un prompt care descrie întregul flux de cercetare și luare a deciziilor. În schimb, modelul agentic decide independent să:

1. Recupereze rapoarte actuale despre tendințele pieței folosind Bing Web Grounding
2. Identifice date relevante despre concurenți folosind Azure AI Search.
3. Coreleze metrice istorice interne de vânzări folosind Azure SQL Database.
4. Sintetizeze concluziile într-o strategie coerentă orchestrat prin serviciul Azure OpenAI.
5. Evalueze strategia pentru lacune sau inconsecvențe, declanșând un nou ciclu de recuperare dacă este necesar.
Toți acești pași — rafinarea interogărilor, alegerea surselor, iterarea până când răspunsul este „mulțumitor” — sunt deciși de model, nu pre-scris de un om.

## Bucle iterative, integrarea instrumentelor și memorie

![Tool Integration Architecture](../../../translated_images/ro/tool-integration.0f569710b5c17c10.webp)

Un sistem agentic se bazează pe un tipar de interacțiune buclată:

- **Apel inițial:** Scopul utilizatorului (cunoscut și ca prompt-ul utilizatorului) este prezentat modelului LLM.
- **Invocarea instrumentului:** Dacă modelul identifică informații lipsă sau instrucțiuni ambigue, selectează un instrument sau o metodă de recuperare — cum ar fi o interogare către baza de date vectorială (ex. căutarea hibridă Azure AI Search în date private) sau un apel SQL structurat — pentru a obține mai mult context.
- **Evaluare și rafinare:** După revizuirea datelor returnate, modelul decide dacă informațiile sunt suficiente. Dacă nu, rafinează interogarea, încearcă un alt instrument sau își ajustează abordarea.
- **Repetă până la satisfacție:** Acest ciclu continuă până ce modelul determină că are suficientă claritate și dovezi pentru a oferi un răspuns final, bine argumentat.
- **Memorie și stare:** Deoarece sistemul menține starea și memoria pe parcursul pașilor, poate reține încercările anterioare și rezultatele acestora, evitând buclele repetitive și luând decizii mai informate pe măsură ce avansează.

În timp, acest lucru creează o senzație de înțelegere evolutivă, permițând modelului să navigheze în sarcini complexe, cu mai mulți pași, fără a necesita intervenția permanentă a unui om sau schimbarea promptului.

## Gestionarea modurilor de eșec și auto-corecția

Autonomia Agentic RAG include și mecanisme robuste de auto-corecție. Când sistemul întâlnește blocaje — cum ar fi recuperarea de documente irelevante sau interogări greșite — poate:

- **Itera și reinteroghează:** În loc să ofere răspunsuri de valoare scăzută, modelul încearcă noi strategii de căutare, rescrie interogările către baza de date sau explorează seturi alternative de date.
- **Utilizează instrumente diagnostice:** Sistemul poate invoca funcții suplimentare concepute pentru a-l ajuta să depaneze pașii de raționament sau să confirme corectitudinea datelor recuperate. Instrumente precum Azure AI Tracing vor fi importante pentru a asigura observabilitate și monitorizare robuste.
- **Revenire la supravegherea umană:** Pentru scenarii cu mize mari sau eșecuri repetate, modelul poate semnala incertitudine și solicita îndrumare umană. După ce omul oferă feedback corectiv, modelul poate integra această lecție pe viitor.

Această abordare iterativă și dinamică permite modelului să se îmbunătățească continuu, asigurând că nu este doar un sistem de tip „un singur apel”, ci unul care învață din greșelile sale în timpul unei sesiuni.

![Self Correction Mechanism](../../../translated_images/ro/self-correction.da87f3783b7f174b.webp)

## Limitele agenției

În ciuda autonomiei în cadrul unei sarcini, Agentic RAG nu este analog cu Inteligența Artificială Generală. Capacitățile sale „agentice” sunt limitate la instrumentele, sursele de date și politicile furnizate de dezvoltatorii umani. Nu poate inventa propriile unelte sau ieși din limitele domeniului stabilite. În schimb, excelează la orchestrarea dinamică a resurselor disponibile.
Diferențele cheie față de formele mai avansate de AI includ:

1. **Autonomie specifică domeniului:** Sistemele Agentic RAG se concentrează pe atingerea obiectivelor definite de utilizator în cadrul unui domeniu cunoscut, folosind strategii precum rescrierea interogărilor sau selecția instrumentelor pentru a îmbunătăți rezultatele.
2. **Dependența de infrastructură:** Capacitățile sistemului depind de instrumentele și datele integrate de dezvoltatori. Nu poate depăși aceste limite fără intervenție umană.
3. **Respectarea regulilor de siguranță:** Ghildinele etice, regulile de conformitate și politicile de afaceri rămân foarte importante. Libertatea agentului este întotdeauna limitată de măsuri de siguranță și mecanisme de supraveghere (sperăm?).

## Cazuri practice și valoare

Agentic RAG excelează în scenarii care necesită rafinare iterativă și precizie:

1. **Mediu axat pe corectitudine:** În verificări de conformitate, analize reglementare sau cercetare juridică, modelul agentic poate verifica repetat faptele, consulta multiple surse și rescrie interogările până produce un răspuns complet verificat.
2. **Interacțiuni complexe cu baze de date:** Atunci când se lucrează cu date structurate, unde interogările pot eșua frecvent sau necesita ajustări, sistemul poate rafina autonom interogările folosind Azure SQL sau Microsoft Fabric OneLake, asigurând că recuperarea finală corespunde intenției utilizatorului.
3. **Fluxuri de lucru extinse:** Sesiunile de durată mai lungă pot evolua pe măsură ce apar informații noi. Agentic RAG poate incorpora continuu date noi, schimbând strategiile pe măsură ce învață mai multe despre problema în cauză.

## Guvernanță, transparență și încredere

Pe măsură ce aceste sisteme devin mai autonome în procesul lor de raționament, guvernanța și transparența sunt cruciale:

- **Raționament explicabil:** Modelul poate oferi un traseu de audit al interogărilor efectuate, surselor consultate și pașilor de raționament parcurși pentru a ajunge la concluzie. Instrumente precum Azure AI Content Safety și Azure AI Tracing / GenAIOps pot ajuta la menținerea transparenței și la diminuarea riscurilor.
- **Controlul prejudecăților și recuperare echilibrată:** Dezvoltatorii pot regla strategiile de recuperare pentru a se asigura că sunt luate în considerare surse de date reprezentative și echilibrate și auditează periodic rezultatele pentru a detecta prejudecăți sau modele distorsionate folosind modele personalizate pentru organizații avansate de știința datelor cu Azure Machine Learning.
- **Supravegherea umană și conformitatea:** Pentru sarcini sensibile, revizuirea umană rămâne esențială. Agentic RAG nu înlocuiește judecata umană în deciziile cu miză mare — o completează prin oferirea unor opțiuni mai bine verificate.

A avea instrumente care oferă un registru clar al acțiunilor este esențial. Fără acestea, depanarea unui proces cu mai mulți pași poate fi foarte dificilă. Vezi următorul exemplu de la Literal AI (compania din spatele Chainlit) pentru o rulare Agent:

![AgentRunExample](../../../translated_images/ro/AgentRunExample.471a94bc40cbdc0c.webp)

## Concluzie

Agentic RAG reprezintă o evoluție naturală în modul în care sistemele AI gestionează sarcini complexe, intensive în date. Prin adoptarea unui tipar de interacțiune buclată, selecția autonomă a instrumentelor și rafinarea interogărilor până la obținerea unui rezultat de calitate înaltă, sistemul trece dincolo de simpla urmărire a prompturilor în direcția unui decident mai adaptiv și conștient de context. Deși rămâne limitat de infrastructurile și liniile directoare etice definite de oameni, aceste capacități agentice permit interacțiuni AI mai bogate, mai dinamice și, în cele din urmă, mai utile atât pentru întreprinderi, cât și pentru utilizatori end-user.

### Aveți mai multe întrebări despre Agentic RAG?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la orele de birou și a primi răspunsuri la întrebările dvs. despre agenții AI.

## Resurse suplimentare

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementarea Retrieval Augmented Generation (RAG) cu Azure OpenAI Service: Aflați cum să folosiți propriile date cu Azure OpenAI Service. Acest modul Microsoft Learn oferă un ghid complet pentru implementarea RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluarea aplicațiilor AI generative cu Microsoft Foundry: Acest articol acoperă evaluarea și compararea modelelor pe seturi de date publice, incluzând aplicații de AI Agentic și arhitecturi RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Ce este Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Un ghid complet pentru Retrieval Augmented Generation bazat pe agenți – Știri din generația RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: accelerează-ți RAG-ul cu reformularea interogărilor și auto-interogare! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Adăugarea straturilor agentice la RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Viitorul asistenților de cunoștințe: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Cum să construiești sisteme Agentic RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Utilizarea Microsoft Foundry Agent Service pentru a scala agenții tăi AI</a>

### Articole academice

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: rafinare iterativă cu auto-feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Agenți de limbaj cu învățare prin întărire verbală</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Modelele mari de limbaj se pot autocorecta prin critică interactivă cu unelte</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Generare augmentată de recuperare agentică: un sondaj asupra Agentic RAG</a>

## Testare rapidă a acestui agent (Opțional)

După ce înveți să implementezi agenți în [Lecția 16](../16-deploying-scalable-agents/README.md), poți testa rapid `TravelRAGAgent` din această lecție — verificând că răspunsurile sale rămân ancorate în baza de cunoștințe — cu fișierul [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Vezi [`tests/README.md`](../tests/README.md) pentru instrucțiuni de rulare.

## Lecția anterioară

[Tipar de proiectare pentru utilizarea uneltelor](../04-tool-use/README.md)

## Lecția următoare

[Construirea agenților AI de încredere](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->