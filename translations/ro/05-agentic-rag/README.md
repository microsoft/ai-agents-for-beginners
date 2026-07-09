[![Agentic RAG](../../../translated_images/ro/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Agentic RAG

Această lecție oferă o privire de ansamblu cuprinzătoare asupra Generării Augmentate de Recuperare Agentică (Agentic RAG), un paradigmat emergent în AI în care modelele mari de limbaj (LLM-uri) își planifică autonom pașii următori în timp ce extrag informații din surse externe. Spre deosebire de tiparele statice de tip retrieval-then-read, Agentic RAG implică apeluri iterative către LLM, între care sunt inserate apeluri către unelte sau funcții și ieșiri structurate. Sistemul evaluează rezultatele, rafinează interogările, apelează unelte suplimentare dacă este necesar și continuă acest ciclu până la obținerea unei soluții satisfăcătoare.

## Introducere

Această lecție va acoperi

- **Înțelegerea Agentic RAG:** Aflați despre paradigmat emergent în AI în care modelele mari de limbaj (LLM-uri) își planifică în mod autonom pașii următori în timp ce extrag informații din surse externe de date.
- **Însușirea stilului Iterativ Maker-Checker:** Înțelegeți ciclul de apeluri iterative către LLM, intercalate cu apeluri la unelte sau funcții și ieșiri structurate, concepute pentru a îmbunătăți corectitudinea și a gestiona interogările incorecte.
- **Explorați aplicațiile practice:** Identificați scenarii în care Agentic RAG strălucește, cum ar fi mediile orientate spre corectitudine, interacțiunile complexe cu baze de date și fluxurile de lucru extinse.

## Obiectivele de învățare

După finalizarea acestei lecții, veți putea/înțelege:

- **Înțelegerea Agentic RAG:** Aflați despre paradigmat emergent în AI în care modelele mari de limbaj (LLM-uri) își planifică în mod autonom pașii următori în timp ce extrag informații din surse externe de date.
- **Stilul Iterativ Maker-Checker:** Înțelegeți conceptul unui ciclu de apeluri iterative către LLM, intercalate cu apeluri la unelte sau funcții și ieșiri structurate, conceput pentru a îmbunătăți corectitudinea și a gestiona interogările incorecte.
- **Stăpânirea procesului de raționament:** Înțelegeți capacitatea sistemului de a-și asuma procesul de raționament, luând decizii privind abordarea problemelor fără a se baza pe trasee predefinite.
- **Fluxul de lucru:** Înțelegeți cum un model agentic decide independent să recupereze rapoarte despre tendințele pieței, să identifice date despre concurenți, să coreleze metrice interne de vânzări, să sintetizeze concluziile și să evalueze strategia.
- **Bucle iterative, integrarea uneltelor și memorie:** Aflați despre dependența sistemului de un tipar de interacțiune în buclă, menținând starea și memoria pe parcursul pașilor pentru a evita bucle repetitive și a lua decizii informate.
- **Gestionarea modurilor de eșec și autocorecția:** Explorați mecanismele robuste de autocorecție ale sistemului, inclusiv iterarea și reinterogarea, utilizarea uneltelor de diagnostic și apelarea la supravegherea umană.
- **Limitele agenției:** Înțelegeți limitările Agentic RAG, concentrându-vă pe autonomia specifică domeniului, dependența infrastructurii și respectarea limitărilor.
- **Cazuri practice și valoare:** Identificați scenarii în care Agentic RAG strălucește, cum ar fi mediile orientate spre corectitudine, interacțiunile complexe cu baze de date și fluxurile de lucru extinse.
- **Guvernanță, transparență și încredere:** Aflați despre importanța guvernanței și transparenței, inclusiv raționamentul explicabil, controlul biasului și supravegherea umană.

## Ce este Agentic RAG?

Generarea Augmentată de Recuperare Agentică (Agentic RAG) este un paradigmat emergent în AI în care modelele mari de limbaj (LLM) își planifică autonom pașii următori în timp ce extrag informații din surse externe. Spre deosebire de tiparele statice de tip retrieval-then-read, Agentic RAG implică apeluri iterative către LLM, între care sunt inserate apeluri către unelte sau funcții și ieșiri structurate. Sistemul evaluează rezultatele, rafinează interogările, apelează unelte suplimentare dacă este necesar și continuă acest ciclu până la obținerea unei soluții satisfăcătoare. Acest stil iterativ de tip „maker-checker” îmbunătățește corectitudinea, gestionează interogările incorecte și asigură rezultate de înaltă calitate.

Sistemul își asumă în mod activ procesul său de raționament, rescriind interogările eșuate, alegând metode diferite de recuperare și integrând mai multe unelte — cum ar fi căutarea vectorială în Azure AI Search, baze de date SQL sau API-uri personalizate — înainte de a finaliza răspunsul. Calitatea distinctivă a unui sistem agentic este capacitatea sa de a-și asuma procesul de raționament. Implementările tradiționale RAG se bazează pe trasee predefinite, dar un sistem agentic determină în mod autonom secvența pașilor pe baza calității informațiilor găsite.

## Definirea Generării Augmentate de Recuperare Agentică (Agentic RAG)

Generarea Augmentată de Recuperare Agentică (Agentic RAG) este un paradigmat emergent în dezvoltarea AI în care LLM-urile nu doar extrag informații din surse de date externe, ci și planifică în mod autonom pașii următori. Spre deosebire de tiparele statice retrieval-then-read sau secvențele de prompturi atent scriptate, Agentic RAG implică un ciclu de apeluri iterative către LLM, intercalate cu apeluri la unelte sau funcții și ieșiri structurate. La fiecare pas, sistemul evaluează rezultatele obținute, decide dacă să rafineze interogările, apelează unelte suplimentare dacă este nevoie și continuă acest ciclu până când obține o soluție satisfăcătoare.

Acest stil iterativ de operare „maker-checker” este conceput pentru a îmbunătăți corectitudinea, a gestiona interogările incorecte către baze de date structurate (ex. NL2SQL) și a asigura rezultate echilibrate și de înaltă calitate. În loc să se bazeze exclusiv pe lanțuri de prompturi atent proiectate, sistemul își asumă activ procesul de raționament. Poate rescrie interogări care eșuează, alege metode diferite de recuperare și integrează multiple unelte — ca de exemplu căutarea vectorială în Azure AI Search, baze de date SQL sau API-uri personalizate — înainte de a finaliza răspunsul. Aceasta elimină necesitatea unor cadre de orchestrare excesiv de complexe. În schimb, un ciclu relativ simplu de „apel LLM → folosire unealtă → apel LLM → …” poate genera ieșiri sofisticate și bine fundamentate.

![Agentic RAG Core Loop](../../../translated_images/ro/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Asumarea procesului de raționament

Calitatea distinctivă care face un sistem „agentic” este capacitatea sa de a-și asuma procesul de raționament. Implementările tradiționale RAG se bazează adesea pe oameni care predefineasc un traseu pentru model: un lanț de gândire care specifică ce și când să se recupereze.
Dar când un sistem este cu adevărat agentic, el decide intern cum să abordeze problema. Nu execută doar un script; determină în mod autonom secvența de pași în funcție de calitatea informațiilor pe care le găsește.
De exemplu, dacă i se cere să creeze o strategie de lansare a unui produs, nu se bazează exclusiv pe un prompt care descrie întregul flux de lucru de cercetare și luare a deciziilor. În schimb, modelul agentic hotărăște independent să:

1. Recupereze rapoarte actuale despre tendințele pieței folosind Bing Web Grounding
2. Identifice date relevante despre concurenți folosind Azure AI Search.
3. Coreleze metricele istorice interne de vânzări folosind Azure SQL Database.
4. Sintezeze concluziile într-o strategie coerentă orchestrată prin Azure OpenAI Service.
5. Evalueze strategia pentru lacune sau inconsecvențe, inițiind un alt ciclu de recuperare dacă este necesar.
Toți acești pași — rafinarea interogărilor, alegerea surselor, iterarea până la „mulțumirea” față de răspuns — sunt deciziile modelului, nu sunt pre-scriptate de un om.

## Bucle iterative, integrarea uneltelor și memorie

![Tool Integration Architecture](../../../translated_images/ro/tool-integration.0f569710b5c17c10.webp)

Un sistem agentic se bazează pe un tipar de interacțiune în buclă:

- **Apel inițial:** Scopul utilizatorului (aka promptul utilizatorului) este prezentat către LLM.
- **Invocarea uneltei:** Dacă modelul identifică informații lipsă sau instrucțiuni ambigue, selectează o unealtă sau o metodă de recuperare — cum ar fi o interogare în baza de date vectorială (ex. căutare hibridă Azure AI Search peste date private) sau un apel SQL structurat — pentru a aduna mai mult context.
- **Evaluare și rafinare:** După ce revizuiește datele returnate, modelul decide dacă informațiile sunt suficiente. Dacă nu, rafinează interogarea, încearcă altă unealtă sau își ajustează abordarea.
- **Repetare până la satisfacție:** Acest ciclu continuă până când modelul consideră că are suficientă claritate și dovezi pentru a livra un răspuns final și bine argumentat.
- **Memorie și stare:** Deoarece sistemul menține starea și memoria pe parcursul pașilor, poate reaminti încercările anterioare și rezultatele lor, evitând buclele repetitive și luând decizii mai informate pe măsură ce avansează.

În timp, acest lucru creează un sentiment de înțelegere evolutivă, permițând modelului să navigheze sarcini complexe și cu mai mulți pași fără a necesita intervenții constante din partea oamenilor sau rescrierea promptului.

## Gestionarea modurilor de eșec și autocorecția

Autonomia Agentic RAG implică și mecanisme robuste de autocorecție. Când sistemul întâlnește impasuri — cum ar fi recuperarea documentelor irelevante sau interogarea incorectă — acesta poate:

- **Itera și reinterogare:** În loc să returneze răspunsuri cu valoare scăzută, modelul încearcă noi strategii de căutare, rescrie interogări de bază de date sau analizează seturi alternative de date.
- **Folosește unelte de diagnostic:** Sistemul poate invoca funcții suplimentare concepute să îl ajute să depaneze pașii de raționament sau să confirme corectitudinea datelor recuperate. Unelte precum Azure AI Tracing vor fi importante pentru a asigura observabilitate și monitorizare robuste.
- **Apel la supravegherea umană:** Pentru scenarii cu miză mare sau cu eșecuri repetate, modelul poate semnala incertitudinea și poate solicita ghidaj uman. Odată ce omul oferă feedback corectiv, modelul poate încorpora această lecție pe viitor.

Această abordare iterativă și dinamică permite modelului să se îmbunătățească continuu, asigurând că nu este doar un sistem one-shot, ci unul care învață din greșelile sale în timpul unei sesiuni date.

![Self Correction Mechanism](../../../translated_images/ro/self-correction.da87f3783b7f174b.webp)

## Limitele agenției

În ciuda autonomiei în cadrul unei sarcini, Agentic RAG nu este echivalent cu Inteligența Artificială Generală. Capabilitățile sale „agentice” sunt limitate la uneltele, sursele de date și politicile furnizate de dezvoltatori umani. Nu poate să-și inventeze propriile unelte sau să iasă din limitele domeniului stabilite. În schimb, excelează la orchestrarea dinamică a resurselor disponibile.
Diferențele cheie față de formele mai avansate de AI includ:

1. **Autonomie specifică domeniului:** Sistemele Agentic RAG se concentrează pe atingerea obiectivelor definite de utilizator în cadrul unui domeniu cunoscut, folosind strategii precum rescrierea interogărilor sau selecția uneltelor pentru a îmbunătăți rezultatele.
2. **Dependente de infrastructură:** Capacitățile sistemului depind de uneltele și datele integrate de dezvoltatori. Nu poate depăși aceste limite fără intervenția umană.
3. **Respect pentru limitări:** Ghidurile etice, regulile de conformitate și politicile de business rămân foarte importante. Libertatea agentului este întotdeauna constrânsă de măsuri de siguranță și mecanisme de supraveghere (sperăm?).

## Cazuri practice și valoare

Agentic RAG strălucește în scenarii care necesită rafinare iterativă și precizie:

1. **Mediile orientate spre corectitudine:** În verificări de conformitate, analize reglementare sau cercetări juridice, modelul agentic poate verifica repetat faptele, consulta surse multiple și rescrie interogările până generează un răspuns riguros validat.
2. **Interacțiuni complexe cu baze de date:** Când se operează cu date structurate în care interogările eșuează frecvent sau necesită ajustări, sistemul poate rafina autonom interogările folosind Azure SQL sau Microsoft Fabric OneLake, asigurând că recuperarea finală corespunde intenției utilizatorului.
3. **Fluxuri de lucru extinse:** Sesiunile de durată mai lungă pot evolua pe măsură ce apar informații noi. Agentic RAG poate incorpora continuu date noi, schimbând strategiile pe măsură ce învață mai multe despre spațiul problemei.

## Guvernanță, transparență și încredere

Pe măsură ce aceste sisteme devin mai autonome în raționament, guvernanța și transparența devin cruciale:

- **Raționament explicabil:** Modelul poate oferi o pistă de audit a interogărilor realizate, surselor consultate și pașilor de raționament făcuți pentru a ajunge la concluzie. Unelte precum Azure AI Content Safety și Azure AI Tracing / GenAIOps pot ajuta la menținerea transparenței și la diminuarea riscurilor.
- **Controlul biasului și recuperare echilibrată:** Dezvoltatorii pot ajusta strategiile de recuperare pentru a asigura considerarea surselor de date echilibrate și reprezentative, și pot audita periodic ieșirile pentru a detecta bias sau modele distorsionate folosind modele personalizate pentru organizații avansate de știință a datelor care utilizează Azure Machine Learning.
- **Supravegherea umană și conformitatea:** Pentru sarcini sensibile, revizuirea umană rămâne esențială. Agentic RAG nu înlocuiește judecata umană în deciziile cu miză mare — o completează oferind opțiuni atent verificate.

A avea unelte care oferă un registru clar al acțiunilor este esențial. Fără acestea, depanarea unui proces în mai mulți pași poate fi foarte dificilă. Consultați următorul exemplu de la Literal AI (compania din spatele Chainlit) pentru o rulare Agent:

![AgentRunExample](../../../translated_images/ro/AgentRunExample.471a94bc40cbdc0c.webp)

## Concluzie

Agentic RAG reprezintă o evoluție naturală în modul în care sistemele AI gestionează sarcini complexe, intensive din punct de vedere al datelor. Prin adoptarea unui tipar de interacțiune în buclă, selecționarea autonomă a uneltelor și rafinarea interogărilor până la obținerea unui rezultat de înaltă calitate, sistemul depășește urmarea prompturilor statice într-un agent decizional mai adaptiv și conștient de context. Deși încă limitat la infrastructuri și ghiduri etice definite de oameni, aceste capabilități agentice permit interacțiuni AI mai bogate, mai dinamice și, în cele din urmă, mai utile atât pentru întreprinderi, cât și pentru utilizatori finali.

### Aveți mai multe întrebări despre Agentic RAG?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a vă întâlni cu alți cursanți, a participa la orele de consultanță și a obține răspunsuri la întrebările despre Agenții AI.

## Resurse suplimentare

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementați Generarea Augmentată de Recuperare (RAG) cu Azure OpenAI Service: Aflați cum să utilizați propriile date cu Azure OpenAI Service. Acest modul Microsoft Learn oferă un ghid complet despre implementarea RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluarea aplicațiilor AI generative cu Microsoft Foundry: Acest articol acoperă evaluarea și compararea modelelor pe seturi de date publice disponibile, inclusiv aplicații Agentic AI și arhitecturi RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Ce este Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Ghid complet pentru Generarea Augmentată de Recuperare bazată pe agenți – Știri din generarea RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: accelerează-ți RAG-ul cu reformularea interogărilor și auto-interogarea! Găleata AI cu sursă deschisă Hugging Face</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Adăugarea straturilor agentice la RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Viitorul asistenților de cunoaștere: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Cum să construiești sisteme RAG agentice</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Utilizarea serviciului Microsoft Foundry Agent pentru a scala agenții tăi AI</a>

### Articole academice

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: rafinare iterativă cu auto-feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: agenți lingvistici cu învățare prin întărire verbală</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: modele lingvistice mari pot corecta singure cu critici interactive cu unelte</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Generare augmentată cu recuperare agentică: o privire de ansamblu asupra Agentic RAG</a>

## Lecția anterioară

[Pattern de utilizare a uneltelor](../04-tool-use/README.md)

## Următoarea lecție

[Construirea agenților AI de încredere](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->