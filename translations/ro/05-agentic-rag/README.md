<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-29T20:54:12+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "ro"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.ro.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Agentic RAG

Această lecție oferă o prezentare cuprinzătoare a Agentic Retrieval-Augmented Generation (Agentic RAG), un nou paradigm AI în care modelele de limbaj mari (LLMs) planifică autonom pașii următori în timp ce extrag informații din surse externe. Spre deosebire de modelele statice de tip „retrieval-then-read”, Agentic RAG implică apeluri iterative către LLM, intercalate cu utilizarea de instrumente sau funcții și producții structurate. Sistemul evaluează rezultatele, rafinează interogările, invocă instrumente suplimentare dacă este necesar și continuă acest ciclu până când se obține o soluție satisfăcătoare.

## Introducere

Această lecție va acoperi:

- **Înțelegerea Agentic RAG:** Aflați despre noul paradigm în AI, unde modelele de limbaj mari (LLMs) planifică autonom pașii următori în timp ce extrag informații din surse de date externe.
- **Stil Iterativ Maker-Checker:** Înțelegeți bucla apelurilor iterative către LLM, intercalate cu utilizarea de instrumente sau funcții și producții structurate, concepute pentru a îmbunătăți corectitudinea și a gestiona interogările defectuoase.
- **Explorarea Aplicațiilor Practice:** Identificați scenarii în care Agentic RAG excelează, cum ar fi medii orientate spre corectitudine, interacțiuni complexe cu baze de date și fluxuri de lucru extinse.

## Obiective de Învățare

După finalizarea acestei lecții, veți ști cum să/veți înțelege:

- **Înțelegerea Agentic RAG:** Aflați despre noul paradigm în AI, unde modelele de limbaj mari (LLMs) planifică autonom pașii următori în timp ce extrag informații din surse de date externe.
- **Stil Iterativ Maker-Checker:** Înțelegeți conceptul unei bucle de apeluri iterative către LLM, intercalate cu utilizarea de instrumente sau funcții și producții structurate, concepute pentru a îmbunătăți corectitudinea și a gestiona interogările defectuoase.
- **Deținerea Procesului de Raționament:** Înțelegeți capacitatea sistemului de a deține procesul său de raționament, luând decizii despre cum să abordeze problemele fără a se baza pe căi predefinite.
- **Flux de Lucru:** Înțelegeți cum un model agentic decide independent să extragă rapoarte despre tendințele pieței, să identifice date despre competitori, să coreleze metrici interne de vânzări, să sintetizeze concluziile și să evalueze strategia.
- **Bucle Iterative, Integrarea Instrumentelor și Memorie:** Aflați despre dependența sistemului de un model de interacțiune în buclă, menținând starea și memoria între pași pentru a evita buclele repetitive și a lua decizii informate.
- **Gestionarea Modurilor de Eșec și Auto-Corectare:** Explorați mecanismele robuste de auto-corectare ale sistemului, inclusiv iterarea și reinterogarea, utilizarea instrumentelor de diagnostic și revenirea la supravegherea umană.
- **Limitele Autonomiei:** Înțelegeți limitările Agentic RAG, concentrându-vă pe autonomia specifică domeniului, dependența de infrastructură și respectarea limitelor de siguranță.
- **Cazuri Practice și Valoare:** Identificați scenarii în care Agentic RAG excelează, cum ar fi medii orientate spre corectitudine, interacțiuni complexe cu baze de date și fluxuri de lucru extinse.
- **Guvernanță, Transparență și Încredere:** Aflați despre importanța guvernanței și transparenței, inclusiv raționamentul explicabil, controlul prejudecăților și supravegherea umană.

## Ce este Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) este un nou paradigm AI în care modelele de limbaj mari (LLMs) planifică autonom pașii următori în timp ce extrag informații din surse externe. Spre deosebire de modelele statice de tip „retrieval-then-read”, Agentic RAG implică apeluri iterative către LLM, intercalate cu utilizarea de instrumente sau funcții și producții structurate. Sistemul evaluează rezultatele, rafinează interogările, invocă instrumente suplimentare dacă este necesar și continuă acest ciclu până când se obține o soluție satisfăcătoare. Acest stil iterativ „maker-checker” îmbunătățește corectitudinea, gestionează interogările defectuoase și asigură rezultate de înaltă calitate.

Sistemul deține activ procesul său de raționament, rescriind interogările eșuate, alegând metode diferite de extragere și integrând multiple instrumente—cum ar fi căutarea vectorială în Azure AI Search, baze de date SQL sau API-uri personalizate—înainte de a finaliza răspunsul. Calitatea distinctivă a unui sistem agentic este capacitatea sa de a deține procesul său de raționament. Implementările tradiționale RAG se bazează pe căi predefinite, dar un sistem agentic determină autonom secvența pașilor pe baza calității informațiilor pe care le găsește.

## Definirea Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) este un nou paradigm în dezvoltarea AI, unde LLM-urile nu doar extrag informații din surse de date externe, ci și planifică autonom pașii următori. Spre deosebire de modelele statice de tip „retrieval-then-read” sau secvențele de prompturi atent scriptate, Agentic RAG implică o buclă de apeluri iterative către LLM, intercalate cu utilizarea de instrumente sau funcții și producții structurate. La fiecare pas, sistemul evaluează rezultatele obținute, decide dacă să rafineze interogările, invocă instrumente suplimentare dacă este necesar și continuă acest ciclu până când obține o soluție satisfăcătoare.

Acest stil iterativ „maker-checker” este conceput pentru a îmbunătăți corectitudinea, a gestiona interogările defectuoase către baze de date structurate (de exemplu, NL2SQL) și a asigura rezultate echilibrate și de înaltă calitate. În loc să se bazeze exclusiv pe lanțuri de prompturi atent proiectate, sistemul deține activ procesul său de raționament. Poate rescrie interogările care eșuează, alege metode diferite de extragere și integrează multiple instrumente—cum ar fi căutarea vectorială în Azure AI Search, baze de date SQL sau API-uri personalizate—înainte de a finaliza răspunsul. Acest lucru elimină necesitatea unor cadre de orchestrare excesiv de complexe. În schimb, o buclă relativ simplă de „apel LLM → utilizare instrument → apel LLM → …” poate produce rezultate sofisticate și bine fundamentate.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.ro.png)

## Deținerea Procesului de Raționament

Calitatea distinctivă care face un sistem „agentic” este capacitatea sa de a deține procesul său de raționament. Implementările tradiționale RAG depind adesea de oameni care predefinesc o cale pentru model: un lanț de gândire care conturează ce să extragă și când.
Dar când un sistem este cu adevărat agentic, decide intern cum să abordeze problema. Nu doar execută un script; determină autonom secvența pașilor pe baza calității informațiilor pe care le găsește.
De exemplu, dacă i se cere să creeze o strategie de lansare a unui produs, nu se bazează exclusiv pe un prompt care detaliază întregul flux de cercetare și luare de decizii. În schimb, modelul agentic decide independent să:

1. Extragă rapoarte despre tendințele pieței actuale folosind Bing Web Grounding.
2. Identifice date relevante despre competitori folosind Azure AI Search.
3. Coreleze metrici interne istorice de vânzări folosind Azure SQL Database.
4. Sintetizeze concluziile într-o strategie coerentă orchestrată prin Azure OpenAI Service.
5. Evalueze strategia pentru lacune sau inconsecvențe, inițiind o altă rundă de extragere dacă este necesar.
Toți acești pași—rafinarea interogărilor, alegerea surselor, iterarea până când este „mulțumit” de răspuns—sunt decise de model, nu pre-scriptate de un om.

## Bucle Iterative, Integrarea Instrumentelor și Memorie

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.ro.png)

Un sistem agentic se bazează pe un model de interacțiune în buclă:

- **Apel Inițial:** Obiectivul utilizatorului (aka. promptul utilizatorului) este prezentat LLM-ului.
- **Invocarea Instrumentelor:** Dacă modelul identifică informații lipsă sau instrucțiuni ambigue, selectează un instrument sau o metodă de extragere—cum ar fi o interogare într-o bază de date vectorială (de exemplu, Azure AI Search Hybrid search peste date private) sau un apel SQL structurat—pentru a aduna mai mult context.
- **Evaluare și Rafinare:** După revizuirea datelor returnate, modelul decide dacă informațiile sunt suficiente. Dacă nu, rafinează interogarea, încearcă un instrument diferit sau își ajustează abordarea.
- **Repetare Până la Satisfacție:** Acest ciclu continuă până când modelul determină că are suficientă claritate și dovezi pentru a oferi un răspuns final bine fundamentat.
- **Memorie și Stare:** Deoarece sistemul menține starea și memoria între pași, poate reaminti încercările anterioare și rezultatele acestora, evitând buclele repetitive și luând decizii mai informate pe măsură ce progresează.

În timp, acest lucru creează un sentiment de înțelegere evolutivă, permițând modelului să navigheze sarcini complexe, în mai mulți pași, fără a necesita intervenția constantă a unui om sau reformularea promptului.

## Gestionarea Modurilor de Eșec și Auto-Corectare

Autonomia Agentic RAG implică, de asemenea, mecanisme robuste de auto-corectare. Când sistemul întâmpină impasuri—cum ar fi extragerea de documente irelevante sau interogări defectuoase—poate:

- **Itera și Reinteroga:** În loc să returneze răspunsuri de valoare scăzută, modelul încearcă noi strategii de căutare, rescrie interogări către baze de date sau analizează seturi de date alternative.
- **Utiliza Instrumente de Diagnostic:** Sistemul poate invoca funcții suplimentare concepute pentru a-l ajuta să depaneze pașii de raționament sau să confirme corectitudinea datelor extrase. Instrumente precum Azure AI Tracing vor fi importante pentru a permite observabilitate și monitorizare robuste.
- **Reveni la Supravegherea Umană:** Pentru scenarii cu miză mare sau eșecuri repetate, modelul poate semnala incertitudinea și solicita îndrumare umană. Odată ce omul oferă feedback corectiv, modelul poate încorpora acea lecție pe viitor.

Această abordare iterativă și dinamică permite modelului să se îmbunătățească continuu, asigurând că nu este doar un sistem „one-shot”, ci unul care învață din greșelile sale în timpul unei sesiuni date.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.ro.png)

## Limitele Autonomiei

În ciuda autonomiei sale în cadrul unei sarcini, Agentic RAG nu este echivalent cu Inteligența Artificială Generală. Capacitățile sale „agentice” sunt limitate la instrumentele, sursele de date și politicile furnizate de dezvoltatorii umani. Nu poate inventa propriile instrumente sau depăși limitele domeniului stabilite. Mai degrabă, excelează în orchestrarea dinamică a resurselor disponibile.
Diferențele cheie față de formele mai avansate de AI includ:

1. **Autonomie Specifică Domeniului:** Sistemele Agentic RAG sunt concentrate pe atingerea obiectivelor definite de utilizator într-un domeniu cunoscut, utilizând strategii precum rescrierea interogărilor sau selecția instrumentelor pentru a îmbunătăți rezultatele.
2. **Dependent de Infrastructură:** Capacitățile sistemului depind de instrumentele și datele integrate de dezvoltatori. Nu poate depăși aceste limite fără intervenție umană.
3. **Respectarea Limitelor de Siguranță:** Liniile directoare etice, regulile de conformitate și politicile de afaceri rămân foarte importante. Libertatea agentului este întotdeauna constrânsă de măsuri de siguranță și mecanisme de supraveghere (sperăm?).

## Cazuri Practice și Valoare

Agentic RAG excelează în scenarii care necesită rafinare iterativă și precizie:

1. **Mediile Orientate Spre Corectitudine:** În verificări de conformitate, analize de reglementare sau cercetare juridică, modelul agentic poate verifica repetat faptele, consulta multiple surse și rescrie interogările până când produce un răspuns temeinic verificat.
2. **Interacțiuni Complexe cu Baze de Date:** Când se lucrează cu date structurate unde interogările pot eșua frecvent sau necesită ajustare, sistemul poate rafina autonom interogările folosind Azure SQL sau Microsoft Fabric OneLake, asigurând că extragerea finală se aliniază cu intenția utilizatorului.
3. **Fluxuri de Lucru Extinse:** Sesiunile de lungă durată pot evolua pe măsură ce apar informații noi. Agentic RAG poate încorpora continuu date noi, schimbând strategiile pe măsură ce învață mai multe despre spațiul problemei.

## Guvernanță, Transparență și Încredere

Pe măsură ce aceste sisteme devin mai autonome în raționamentul lor, guvernanța și transparența sunt cruciale:

- **Raționament Explicabil:** Modelul poate oferi o urmă de audit a interogărilor pe care le-a făcut, sursele pe care le-a consultat și pașii de raționament pe care i-a urmat pentru a ajunge la concluzia sa. Instrumente precum Azure AI Content Safety și Azure AI Tracing / GenAIOps pot ajuta la menținerea transparenței și la reducerea riscurilor.
- **Controlul Prejudecăților și Extragerea Echilibrată:** Dezvoltatorii pot ajusta strategiile de extragere pentru a se asigura că sunt luate în considerare surse de date echilibrate și reprezentative și pot audita regulat rezultatele pentru a detecta prejudecăți sau modele distorsionate folosind modele personalizate pentru organizații avansate de știința datelor utilizând Azure Machine Learning.
- **Supravegherea Umană și Conformitatea:** Pentru sarcini sensibile, revizuirea umană rămâne esențială. Agentic RAG nu înlocuiește judecata umană în deciziile cu miză mare—o completează prin oferirea de opțiuni mai temeinic verificate.

A avea instrumente care oferă un record clar al acțiunilor este esențial. Fără ele, depanarea unui proces în mai mulți pași poate fi foarte dificilă. Vedeți exemplul următor de la Literal AI (compania din spatele Chainlit) pentru un Agent run:

![AgentRunExample](../../../translated_images/AgentRunExample.471a94bc40cbdc0cd04c1f43c8d8c9b751f10d97918c900e29cb3ba0d6aa4c00.ro.png)

## Concluzie

Agentic RAG reprezintă o evoluție naturală în modul în care sistemele AI gestionează sarcini complexe, intensive în date. Prin adoptarea unui model de interacțiune în buclă, selectarea autonomă a instrumentelor și rafinarea interogărilor până la obținerea unui rezultat de înaltă calitate, sistemul depășește urmărirea statică a prompturilor, devenind un decident mai adaptiv și conștient de context. Deși încă limitat de infrastructurile și liniile directoare etice definite de oameni, aceste capacități agentice permit interacțiuni AI mai bogate, mai dinamice și, în cele din urmă, mai utile pentru întreprinderi și utilizatori finali.

### Aveți mai multe întrebări despre Agentic RAG?

Alăturați-vă [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la ore de birou și a obține răspunsuri la întrebările despre AI Agents.

## Resurse
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Implementarea Generării Augmentate prin Recuperare (RAG) cu Azure OpenAI Service: Învață cum să folosești propriile date cu Azure OpenAI Service. Acest modul Microsoft Learn oferă un ghid cuprinzător pentru implementarea RAG</a>  
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluarea aplicațiilor de AI generativ cu Azure AI Foundry: Acest articol acoperă evaluarea și compararea modelelor pe seturi de date disponibile public, inclusiv aplicații Agentic AI și arhitecturi RAG</a>  
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Ce este Agentic RAG | Weaviate</a>  
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Un ghid complet pentru Generarea Augmentată prin Recuperare bazată pe agenți – Știri din lumea RAG</a>  
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: îmbunătățește-ți RAG-ul cu reformularea interogărilor și auto-interogare! Hugging Face Open-Source AI Cookbook</a>  
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Adăugarea straturilor agentice la RAG</a>  
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Viitorul asistenților de cunoștințe: Jerry Liu</a>  
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Cum să construiești sisteme Agentic RAG</a>  
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Utilizarea Azure AI Foundry Agent Service pentru a scala agenții tăi AI</a>  

### Lucrări academice

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Îmbunătățire iterativă cu auto-feedback</a>  
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Agenți lingvistici cu învățare prin întărire verbală</a>  
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Modelele lingvistice mari se pot autocorecta prin critică interactivă cu unelte</a>  
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Generarea Augmentată prin Recuperare Agentică: O analiză a RAG-ului agentic</a>  

## Lecția anterioară

[Modelul de proiectare pentru utilizarea uneltelor](../04-tool-use/README.md)  

## Lecția următoare

[Construirea agenților AI de încredere](../06-building-trustworthy-agents/README.md)  

---

**Declinarea responsabilității**:  
Acest document a fost tradus utilizând serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru a asigura acuratețea, vă rugăm să aveți în vedere că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.