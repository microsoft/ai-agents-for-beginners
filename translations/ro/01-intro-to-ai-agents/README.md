<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-29T20:44:47+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "ro"
}
-->
[![Introducere în Agenți AI](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.ro.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Click pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Introducere în Agenți AI și Utilizări ale Agenților

Bun venit la cursul "Agenți AI pentru Începători"! Acest curs oferă cunoștințe fundamentale și exemple aplicate pentru construirea Agenților AI.

Alătură-te pentru a întâlni alți cursanți și creatori de Agenți AI și pentru a pune orice întrebări legate de acest curs.

Pentru a începe acest curs, vom începe prin a înțelege mai bine ce sunt Agenții AI și cum îi putem folosi în aplicațiile și fluxurile de lucru pe care le construim.

## Introducere

Această lecție acoperă:

- Ce sunt Agenții AI și care sunt diferitele tipuri de agenți?
- Ce utilizări sunt cele mai potrivite pentru Agenții AI și cum ne pot ajuta?
- Care sunt unele dintre elementele de bază atunci când proiectăm soluții bazate pe agenți?

## Obiective de Învățare
După finalizarea acestei lecții, ar trebui să fii capabil să:

- Înțelegi conceptele Agenților AI și cum diferă de alte soluții AI.
- Aplici Agenții AI în mod eficient.
- Proiectezi soluții bazate pe agenți într-un mod productiv pentru utilizatori și clienți.

## Definirea Agenților AI și Tipurile de Agenți AI

### Ce sunt Agenții AI?

Agenții AI sunt **sisteme** care permit **Modele de Limbaj Extins (LLMs)** să **efectueze acțiuni** prin extinderea capacităților lor, oferindu-le acces la **instrumente** și **cunoștințe**.

Să descompunem această definiție în părți mai mici:

- **Sistem** - Este important să considerăm agenții nu doar ca un singur component, ci ca un sistem format din mai multe componente. La nivel de bază, componentele unui Agent AI sunt:
  - **Mediu** - Spațiul definit în care Agentul AI operează. De exemplu, dacă am avea un agent AI pentru rezervări de călătorii, mediul ar putea fi sistemul de rezervări pe care agentul îl folosește pentru a finaliza sarcinile.
  - **Senzori** - Mediile au informații și oferă feedback. Agenții AI folosesc senzori pentru a colecta și interpreta aceste informații despre starea curentă a mediului. În exemplul agentului de rezervări, sistemul de rezervări poate oferi informații precum disponibilitatea hotelurilor sau prețurile zborurilor.
  - **Actuatori** - După ce Agentul AI primește starea curentă a mediului, pentru sarcina curentă, agentul determină ce acțiune să efectueze pentru a schimba mediul. Pentru agentul de rezervări, aceasta ar putea fi rezervarea unei camere disponibile pentru utilizator.

![Ce sunt Agenții AI?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.ro.png)

**Modele de Limbaj Extins** - Conceptul de agenți a existat înainte de crearea LLM-urilor. Avantajul construirii Agenților AI cu LLM-uri este capacitatea lor de a interpreta limbajul uman și datele. Această abilitate permite LLM-urilor să interpreteze informațiile din mediu și să definească un plan pentru a schimba mediul.

**Efectuarea Acțiunilor** - În afara sistemelor de Agenți AI, LLM-urile sunt limitate la situații în care acțiunea constă în generarea de conținut sau informații pe baza unei solicitări a utilizatorului. În cadrul sistemelor de Agenți AI, LLM-urile pot îndeplini sarcini interpretând cererea utilizatorului și folosind instrumentele disponibile în mediul lor.

**Acces la Instrumente** - Instrumentele la care LLM-ul are acces sunt definite de 1) mediul în care operează și 2) dezvoltatorul Agentului AI. În exemplul agentului de călătorii, instrumentele agentului sunt limitate de operațiunile disponibile în sistemul de rezervări și/sau dezvoltatorul poate limita accesul agentului la zboruri.

**Memorie+Cunoștințe** - Memoria poate fi pe termen scurt, în contextul conversației dintre utilizator și agent. Pe termen lung, în afara informațiilor furnizate de mediu, Agenții AI pot, de asemenea, să recupereze cunoștințe din alte sisteme, servicii, instrumente și chiar alți agenți. În exemplul agentului de călătorii, aceste cunoștințe ar putea fi informațiile despre preferințele de călătorie ale utilizatorului aflate într-o bază de date a clienților.

### Diferitele tipuri de agenți

Acum că avem o definiție generală a Agenților AI, să analizăm câteva tipuri specifice de agenți și cum ar fi aplicate unui agent AI pentru rezervări de călătorii.

| **Tip de Agent**              | **Descriere**                                                                                                                       | **Exemplu**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agenți Reflex Simpli**      | Efectuează acțiuni imediate pe baza unor reguli predefinite.                                                                          | Agentul de călătorii interpretează contextul unui e-mail și redirecționează plângerile legate de călătorii către serviciul pentru clienți.                                                                                      |
| **Agenți Reflex Bazat pe Model** | Efectuează acțiuni pe baza unui model al lumii și a schimbărilor acestuia.                                                           | Agentul de călătorii prioritizează rutele cu schimbări semnificative de preț pe baza accesului la date istorice despre prețuri.                                                                                                 |
| **Agenți Bazat pe Obiective** | Creează planuri pentru a atinge obiective specifice interpretând obiectivul și determinând acțiunile necesare pentru a-l atinge.      | Agentul de călătorii rezervă o călătorie determinând aranjamentele necesare (mașină, transport public, zboruri) de la locația curentă la destinație.                                                                            |
| **Agenți Bazat pe Utilitate** | Ia în considerare preferințele și cântărește compromisurile numeric pentru a determina cum să atingă obiectivele.                     | Agentul de călătorii maximizează utilitatea cântărind conveniența vs. costul atunci când rezervă călătoria.                                                                                                                    |
| **Agenți de Învățare**        | Se îmbunătățesc în timp răspunzând la feedback și ajustând acțiunile în consecință.                                                   | Agentul de călătorii se îmbunătățește folosind feedback-ul clienților din sondajele post-călătorie pentru a face ajustări la rezervările viitoare.                                                                              |
| **Agenți Ierarhici**          | Prezintă mai mulți agenți într-un sistem ierarhic, agenții de nivel superior împărțind sarcinile în subtasks pentru agenții de nivel inferior. | Agentul de călătorii anulează o călătorie împărțind sarcina în subtasks (de exemplu, anularea rezervărilor specifice) și având agenții de nivel inferior să le finalizeze, raportând înapoi agentului de nivel superior.             |
| **Sisteme Multi-Agent (MAS)** | Agenții finalizează sarcini independent, fie cooperativ, fie competitiv.                                                             | Cooperativ: Mai mulți agenți rezervă servicii de călătorie specifice, cum ar fi hoteluri, zboruri și divertisment. Competitiv: Mai mulți agenți gestionează și concurează pentru un calendar comun de rezervări hoteliere pentru a rezerva clienții în hotel. |

## Când să folosești Agenți AI

În secțiunea anterioară, am folosit cazul de utilizare al Agentului de Călătorii pentru a explica cum pot fi folosite diferitele tipuri de agenți în diferite scenarii de rezervare. Vom continua să folosim această aplicație pe parcursul cursului.

Să analizăm tipurile de cazuri de utilizare pentru care Agenții AI sunt cel mai bine folosiți:

![Când să folosești Agenți AI?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.ro.png)

- **Probleme Deschise** - permit LLM-ului să determine pașii necesari pentru a finaliza o sarcină, deoarece nu pot fi întotdeauna codificați într-un flux de lucru.
- **Procese Multi-Pas** - sarcini care necesită un nivel de complexitate în care Agentul AI trebuie să folosească instrumente sau informații pe parcursul mai multor etape, în loc de o singură recuperare.
- **Îmbunătățire în Timp** - sarcini în care agentul se poate îmbunătăți în timp primind feedback fie din mediul său, fie de la utilizatori pentru a oferi o utilitate mai bună.

Acoperim mai multe considerații privind utilizarea Agenților AI în lecția Construirea Agenților AI de Încredere.

## Bazele Soluțiilor Bazate pe Agenți

### Dezvoltarea Agenților

Primul pas în proiectarea unui sistem de Agenți AI este definirea instrumentelor, acțiunilor și comportamentelor. În acest curs, ne concentrăm pe utilizarea **Azure AI Agent Service** pentru a defini agenții noștri. Acesta oferă funcționalități precum:

- Selectarea modelelor deschise, cum ar fi OpenAI, Mistral și Llama
- Utilizarea datelor licențiate prin furnizori precum Tripadvisor
- Utilizarea instrumentelor standardizate OpenAPI 3.0

### Modele Bazate pe Agenți

Comunicarea cu LLM-urile se face prin prompturi. Având în vedere natura semi-autonomă a Agenților AI, nu este întotdeauna posibil sau necesar să re-promptăm manual LLM-ul după o schimbare în mediu. Folosim **Modele Bazate pe Agenți** care ne permit să promptăm LLM-ul pe parcursul mai multor etape într-un mod mai scalabil.

Acest curs este împărțit în unele dintre modelele bazate pe agenți populare în prezent.

### Framework-uri Bazate pe Agenți

Framework-urile bazate pe agenți permit dezvoltatorilor să implementeze modele bazate pe agenți prin cod. Aceste framework-uri oferă șabloane, pluginuri și instrumente pentru o mai bună colaborare între Agenții AI. Aceste beneficii oferă capacități pentru o mai bună observabilitate și depanare a sistemelor de Agenți AI.

În acest curs, vom explora framework-ul AutoGen bazat pe cercetare și framework-ul Agent gata de producție din Semantic Kernel.

### Ai mai multe întrebări despre Agenții AI?

Alătură-te [Discordului Azure AI Foundry](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la ore de consultanță și a obține răspunsuri la întrebările tale despre Agenții AI.

## Lecția Anterioară

[Setarea Cursului](../00-course-setup/README.md)

## Lecția Următoare

[Explorarea Framework-urilor Bazate pe Agenți](../02-explore-agentic-frameworks/README.md)

---

**Declinarea responsabilității**:  
Acest document a fost tradus utilizând serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru a asigura acuratețea, vă rugăm să aveți în vedere că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea realizată de un profesionist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.