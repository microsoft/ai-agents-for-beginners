[![Cum să proiectezi agenți AI buni](../../../translated_images/ro/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Click pe imaginea de mai sus pentru a viziona videoclipul lecției)_
# Principiile Designului Agentic AI

## Introducere

Există multe moduri de a gândi construirea Sistemelor Agentice AI. Având în vedere că ambiguitatea este o caracteristică și nu un defect în designul AI Generative, uneori este dificil pentru ingineri să înțeleagă de unde să înceapă. Am creat un set de Principii de Design UX centrate pe om pentru a permite dezvoltatorilor să construiască sisteme agentice centrate pe client pentru a rezolva nevoile lor de afaceri. Aceste principii de design nu reprezintă o arhitectură prescrisă, ci mai degrabă un punct de plecare pentru echipele care definesc și construiesc experiențe agentice.

În general, agenții ar trebui să:

- Extindă și să scaleze capacitățile umane (brainstorming, rezolvare de probleme, automatizare etc.)
- Completeze lacunele de cunoștințe (să mă aducă la curent cu domenii de cunoaștere, traducere etc.)
- Faciliteze și să susțină colaborarea în modurile în care noi, ca indivizi, preferăm să lucrăm cu alții
- Să ne facă versiuni mai bune ale noastre înșine (de exemplu, antrenor de viață / organizator de sarcini, ajutându-ne să învățăm abilități de reglare emoțională și mindfulness, construind reziliență etc.)

## Această Lecție Va Acoperi

- Ce sunt Principiile de Design Agentic
- Care sunt unele ghiduri de urmat în implementarea acestor principii de design
- Exemple de utilizare a principiilor de design

## Obiective de Învățare

După finalizarea acestei lecții, vei putea:

1. Explica ce sunt Principiile de Design Agentic
2. Explica ghidurile pentru utilizarea Principiilor de Design Agentic
3. Înțelege cum să construiești un agent folosind Principiile de Design Agentic

## Principiile de Design Agentic

![Principiile de Design Agentic](../../../translated_images/ro/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Spațiu)

Acesta este mediul în care agentul operează. Aceste principii informează cum proiectăm agenți pentru a interacționa în lumea fizică și digitală.

- **Conectare, nu colapsare** – ajută la conectarea oamenilor cu alți oameni, evenimente și cunoștințe acționabile pentru a permite colaborarea și conexiunea.
- Agenții ajută la conectarea evenimentelor, cunoștințelor și oamenilor.
- Agenții aduc oamenii mai aproape unul de altul. Nu sunt proiectați pentru a înlocui sau a minimaliza oamenii.
- **Accesibil ușor, dar uneori invizibil** – agentul operează în mare parte în fundal și ne atenționează doar când este relevant și potrivit.
  - Agentul este ușor de descoperit și accesibil pentru utilizatorii autorizați pe orice dispozitiv sau platformă.
  - Agentul suportă intrări și ieșiri multimodale (sunet, voce, text etc.).
  - Agentul poate trece fluid între prim-plan și fundal; între proactive și reactive, în funcție de percepția nevoilor utilizatorului.
  - Agentul poate opera invizibil, dar calea procesului său de fundal și colaborarea cu alți Agenți sunt transparente și controlabile de către utilizator.

### Agent (Timp)

Aceasta este modul în care agentul operează în timp. Aceste principii informează cum proiectăm agenți care interacționează în trecut, prezent și viitor.

- **Trecut**: Reflectând asupra istoriei care include atât starea, cât și contextul.
  - Agentul oferă rezultate mai relevante pe baza analizei datelor istorice mai bogate, dincolo de eveniment, oameni sau stări.
  - Agentul creează conexiuni din evenimentele trecute și reflectă activ asupra memoriei pentru a reacționa la situațiile actuale.
- **Acum**: Sugerează mai mult decât notifică.
  - Agentul întruchipează o abordare cuprinzătoare pentru interacțiunea cu oamenii. Când se întâmplă un eveniment, Agentul merge dincolo de notificarea statică sau alte formalități statice. Agentul poate simplifica fluxurile sau genera dinamic sugestii pentru a direcționa atenția utilizatorului în momentul potrivit.
  - Agentul oferă informații bazate pe mediul contextual, schimbările sociale și culturale și adaptate intenției utilizatorului.
  - Interacțiunea cu agentul poate fi graduală, evoluând/creșterea în complexitate pentru a împuternici utilizatorii pe termen lung.
- **Viitor**: Adaptare și evoluție.
  - Agentul se adaptează la diverse dispozitive, platforme și modalități.
  - Agentul se adaptează la comportamentul utilizatorului, nevoile de accesibilitate și este personalizabil liber.
  - Agentul este modelat și evoluează prin interacțiune continuă cu utilizatorul.

### Agent (Nucleu)

Acestea sunt elementele cheie în nucleul designului agentului.

- **Acceptă incertitudinea, dar stabilește încrederea**.
  - Un anumit nivel de incertitudine a agentului este de așteptat. Incertitudinea este un element esențial al designului agentului.
  - Încrederea și transparența sunt straturi fundamentale ale designului agentului.
  - Oamenii controlează când agentul este activ/inactiv, iar starea agentului este vizibilă clar în orice moment.

## Ghidurile pentru Implementarea Acestor Principii

Când folosești principiile de design anterioare, folosește următoarele ghiduri:

1. **Transparență**: Informează utilizatorul că AI este implicat, cum funcționează (inclusiv acțiunile trecute) și cum să ofere feedback și să modifice sistemul.
2. **Control**: Permite utilizatorului să-și personalizeze, să specifice preferințe și să personalizeze, precum și să aibă control asupra sistemului și atributelor sale (inclusiv abilitatea de a uita).
3. **Consistență**: Ţintește o experienţă consecventă, multimodală, pe dispozitive și puncte finale. Folosește elemente familiare UI/UX unde este posibil (de exemplu, pictograma microfonului pentru interacțiune vocală) și reduce sarcina cognitivă a clientului cât mai mult posibil (de exemplu, răspunsuri concise, ajutoare vizuale și conținut „Află mai mult”).

## Cum să Proiectezi un Agent de Călătorie Folosind Aceste Principii și Ghiduri

Imaginează-ți că proiectezi un Agent de Călătorie, iată cum ai putea gândi să folosești Principiile și Ghidurile de Design:

1. **Transparență** – Informează utilizatorul că Agentul de Călătorie este un agent AI activat. Oferă instrucțiuni de bază pentru a începe (de exemplu, un mesaj „Bună”, exemple de solicitări). Documentează clar acest lucru pe pagina produsului. Afișează lista solicitărilor pe care utilizatorul le-a făcut în trecut. Fă clar cum se oferă feedback (degetul mare sus/jos, butonul Trimite Feedback etc.). Articulează clar dacă Agentul are restricții de utilizare sau subiect.
2. **Control** – Asigură-te că este clar cum utilizatorul poate modifica Agentul după crearea lui folosind, de exemplu, System Prompt. Permite utilizatorului să aleagă cât de detaliat este Agentul, stilul său de scriere și orice avertismente privind ce subiecte Agentul nu trebuie să abordeze. Permite utilizatorului să vadă și să șteargă fișierele sau datele asociate, solicitările și conversațiile anterioare.
3. **Consistență** – Asigură-te că iconițele pentru Share Prompt, adăugarea unui fișier sau foto și etichetarea cuiva sau ceva sunt standard și ușor de recunoscut. Folosește pictograma agrafă pentru a indica încărcarea/partajarea fișierelor cu Agentul și pictograma imagine pentru a indica încărcarea graficelor.

## Exemple de Cod

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Ai Mai Multe Întrebări Despre Modelele de Design Agentic AI?

Alătură-te [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a cunoaște alți cursanți, a participa la ore de consultanță și a primi răspunsuri la întrebările tale despre Agenții AI.

## Resurse Suplimentare

- <a href="https://openai.com" target="_blank">Practici pentru Guvernarea Sistemelor Agentic AI | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Proiectul Toolkit HAX - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Trusa de Instrumente pentru AI Responsabil</a>

## Lecția Anterioară

[Explorarea Cadrelor Agentice](../02-explore-agentic-frameworks/README.md)

## Lecția Următoare

[Modelul de Design pentru Utilizarea Instrumentelor](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->