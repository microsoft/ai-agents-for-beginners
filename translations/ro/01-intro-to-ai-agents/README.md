[![Intro to AI Agents](../../../translated_images/ro/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_


# Introducere în Agenții AI și Cazurile de Utilizare ale Agenților

Bine ați venit la cursul „Agenți AI pentru Începători”! Acest curs oferă cunoștințe fundamentale și exemple aplicate pentru construirea Agenților AI.

Alăturați-vă <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunității Discord Azure AI</a> pentru a întâlni alți cursanți și dezvoltatori de Agenți AI și pentru a pune orice întrebări legate de acest curs.

Pentru a începe acest curs, vom începe prin a înțelege mai bine ce sunt Agenții AI și cum îi putem utiliza în aplicațiile și fluxurile de lucru pe care le construim.

## Introducere

Această lecție acoperă:

- Ce sunt Agenții AI și care sunt diferitele tipuri de agenți?
- Care cazuri de utilizare sunt cele mai potrivite pentru Agenții AI și cum ne pot ajuta?
- Care sunt unele dintre blocurile de bază când se proiectează Soluții Agentice?

## Obiectivele de Învățare
După finalizarea acestei lecții, ar trebui să puteți:

- Înțelege conceptele despre Agenții AI și cum diferă de alte soluții AI.
- Aplica Agenții AI în mod eficient.
- Proiecta soluții agentice productiv pentru utilizatori și clienți.

## Definirea Agenților AI și Tipurile de Agenți AI

### Ce sunt Agenții AI?

Agenții AI sunt **sisteme** care permit **Modelelor Mari de Limbaj (LLMs)** să **execute acțiuni** prin extinderea capacităților lor prin oferirea LLM-urilor de **acces la unelte** și **cunoștințe**.

Să descompunem această definiție în părți mai mici:

- **Sistem** - Este important să ne gândim la agenți nu doar ca la un singur component, ci ca la un sistem alcătuit din multe componente. La nivel de bază, componentele unui Agent AI sunt:
  - **Mediu** - Spațiul definit în care operează Agentul AI. De exemplu, dacă am avea un Agent AI pentru rezervări de călătorii, mediul ar putea fi sistemul de rezervări pe care Agentul AI îl folosește pentru a-și îndeplini sarcinile.
  - **Senzori** - Mediile conțin informații și oferă feedback. Agenții AI folosesc senzori pentru a aduna și interpreta aceste informații despre starea curentă a mediului. În exemplul Agentului de Rezervări, sistemul poate furniza informații precum disponibilitatea hotelurilor sau prețurile zborurilor.
  - **Actuatoare** - Odată ce Agentul AI primește starea curentă a mediului, pentru sarcina curentă agentul determină ce acțiune să execute pentru a modifica mediul. Pentru agentul de rezervări, ar putea fi rezervarea unei camere disponibile pentru utilizator.

![What Are AI Agents?](../../../translated_images/ro/what-are-ai-agents.1ec8c4d548af601a.webp)

**Modele Mari de Limbaj** - Conceptul de agenți exista înainte de crearea LLM-urilor. Avantajul construirii Agenților AI cu LLM-uri constă în capacitatea lor de a interpreta limbajul uman și datele. Această abilitate permite LLM-urilor să interpreteze informațiile din mediu și să definească un plan pentru a schimba mediul.

**Execută Acțiuni** - În afara sistemelor cu Agenți AI, LLM-urile sunt limitate la situații în care acțiunea este generarea de conținut sau informații pe baza unui prompt al utilizatorului. În cadrul sistemelor cu Agenți AI, LLM-urile pot îndeplini sarcini prin interpretarea cererii utilizatorului și folosirea uneltelor disponibile în mediul lor.

**Acces la Unelte** - Uneltele la care LLM-ul are acces sunt definite de 1) mediul în care operează și 2) dezvoltatorul Agentului AI. În exemplul agentului pentru călătorii, uneltele agentului sunt limitate de operațiile disponibile în sistemul de rezervări și/sau dezvoltatorul poate limita accesul agentului la unelte pentru zboruri.

**Memorie + Cunoștințe** - Memoria poate fi pe termen scurt în contextul conversației dintre utilizator și agent. Pe termen lung, în afara informațiilor oferite de mediu, Agenții AI pot de asemenea să acceseze cunoștințe din alte sisteme, servicii, unelte și chiar alți agenți. În exemplul agentului pentru călătorii, această cunoștință ar putea fi informațiile despre preferințele de călătorie ale utilizatorului, stocate într-o bază de date a clienților.

### Diferitele tipuri de agenți

Acum că avem o definiție generală a Agenților AI, să vedem câteva tipuri specifice de agenți și cum s-ar aplica ei unui agent AI de rezervări.

| **Tipul Agentului**             | **Descriere**                                                                                                                        | **Exemplu**                                                                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agenți Reflex Simpli**        | Execută acțiuni imediate bazate pe reguli predefinite.                                                                              | Agentul de călătorii interpretează contextul unui email și redirecționează plângerile legate de călătorii către serviciul clienți.                                                                                   |
| **Agenți Reflex Bazat pe Model**| Execută acțiuni bazate pe un model al lumii și modificările aduse acelui model.                                                     | Agentul de călătorii prioritizează rutele cu modificări semnificative ale prețurilor bazându-se pe accesul la date istorice de prețuri.                                                                              |
| **Agenți Bazati pe Scop**       | Creează planuri pentru a atinge scopuri specifice prin interpretarea scopului și determinarea acțiunilor necesare pentru atingerea lui.| Agentul de călătorii rezervă o călătorie determinând aranjamentele necesare (mașină, transport public, zboruri) de la locația curentă la destinație.                                                                   |
| **Agenți Bazati pe Utilitate**  | Ia în considerare preferințele și cântărește compromisurile numeric pentru a determina felul în care va atinge scopurile.          | Agentul de călătorii maximizează utilitatea cântărind comoditatea versus costul atunci când face rezervări.                                                                                                         |
| **Agenți de Învățare**           | Se îmbunătățesc în timp prin răspuns la feedback și ajustarea acțiunilor.                                                          | Agentul de călătorii se îmbunătățește folosind feedback-ul clienților din sondaje post-călătorie pentru a face ajustări la rezervările viitoare.                                                                     |
| **Agenți Ierarhici**             | Caracterizați prin mai mulți agenți într-un sistem pe niveluri, agenții de nivel superior împart sarcini în subtasks pentru agenții de nivel inferior.| Agentul de călătorii anulează o călătorie împărțind task-ul în subtasks (de exemplu, anularea rezervărilor specifice) și având agenți de nivel inferior care le finalizează și raportează înapoi agentului de nivel superior. |
| **Sisteme Multi-Agent (MAS)**    | Agenții finalizează sarcini independent, fie cooperativ, fie competitiv.                                                             | Cooperativ: Mai mulți agenți rezervă servicii de călătorie specifice, cum ar fi hoteluri, zboruri și divertisment. Competitiv: Mai mulți agenți gestionează și concurează pentru un calendar comun de rezervări hoteliere.|

## Când să Folosim Agenți AI

În secțiunea anterioară, am folosit exemplul Agentului de Călătorii pentru a explica cum diferitele tipuri de agenți pot fi folosiți în scenarii diferite de rezervări. Vom continua să folosim această aplicație pe tot parcursul cursului.

Să analizăm tipurile de cazuri de utilizare pentru care Agenții AI sunt cei mai potriviți:

![When to use AI Agents?](../../../translated_images/ro/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Probleme Deschise** - permițând LLM-ului să determine pașii necesari pentru a îndeplini o sarcină deoarece nu pot fi întotdeauna codificate rigid într-un flux de lucru.
- **Procese cu Mai Mulți Pași** - sarcini care necesită un nivel de complexitate în care Agentul AI trebuie să folosească unelte sau informații peste multiple interacțiuni în loc de o singură recuperare.
- **Îmbunătățire în Timp** - sarcini în care agentul poate să se îmbunătățească în timp primind feedback fie din mediul său, fie de la utilizatori pentru a oferi o utilitate mai bună.

Abordăm mai multe considerații privind utilizarea Agenților AI în lecția Construind Agenți AI de Încredere.

## Elemente de Bază ale Soluțiilor Agentice

### Dezvoltarea Agentului

Primul pas în proiectarea unui sistem de Agenți AI este definirea uneltelor, acțiunilor și comportamentelor. În acest curs, ne concentrăm pe utilizarea **Serviciului Azure AI Agent** pentru a defini Agenții noștri. Acesta oferă funcții precum:

- Seleția modelelor deschise, cum ar fi OpenAI, Mistral și Llama
- Utilizarea datelor licențiate prin furnizori precum Tripadvisor
- Utilizarea uneltelor standardizate OpenAPI 3.0

### Modele Agentice

Comunicarea cu LLM-urile se face prin prompturi. Dată fiind natura semi-autonomă a Agenților AI, nu este întotdeauna posibil sau necesar să reinițiem manual promptul pentru LLM după o schimbare în mediu. Folosim **Modele Agentice** care ne permit să promptăm LLM-ul în mai mulți pași într-un mod mai scalabil.

Acest curs este împărțit în câteva dintre modelele agentice populare actuale.

### Framework-uri Agentice

Framework-urile Agentice permit dezvoltatorilor să implementeze modelele agentice prin cod. Aceste framework-uri oferă șabloane, pluginuri și unelte pentru o colaborare mai bună între Agenții AI. Aceste beneficii oferă capacități pentru o observabilitate mai bună și depanare a sistemelor cu Agenți AI.

În acest curs vom explora Microsoft Agent Framework (MAF) pentru construirea de agenți AI pregătiți pentru producție.

## Coduri Exemplu

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Ai Mai Multe Întrebări despre Agenții AI?

Alătură-te [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la ore de asistență și a primi răspunsuri la întrebările tale despre Agenții AI.

## Lecția Anterioară

[Configurarea Cursului](../00-course-setup/README.md)

## Lecția Următoare

[Explorarea Framework-urilor Agentice](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa oficială. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot rezulta din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->