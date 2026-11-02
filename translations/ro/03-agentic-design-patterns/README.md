[![Cum să proiectezi agenți AI buni](../../../translated_images/ro/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Click pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_
# Principiile de Design pentru Agenți AI

## Introducere

Există multe moduri de a gândi construcția Sistemelor Agentice AI. Având în vedere că ambiguitatea este o caracteristică și nu o eroare în designul AI Generativ, este uneori dificil pentru ingineri să decidă de unde să înceapă. Am creat un set de Principii de Design UX centrate pe om pentru a permite dezvoltatorilor să construiască sisteme agentice centrate pe client pentru a rezolva nevoile lor de afaceri. Aceste principii de design nu reprezintă o arhitectură prescriptivă, ci mai degrabă un punct de plecare pentru echipele care definesc și construiesc experiențe agentice.

În general, agenții ar trebui să:

- Extindă și să scaleze capacitățile umane (generare de idei, rezolvare de probleme, automatizare etc.)
- Completeze golurile de cunoștințe (să mă pună la curent cu domeniile de cunoștințe, traduceri etc.)
- Faciliteze și să susțină colaborarea în modurile în care noi, ca indivizi, preferăm să lucrăm cu alții
- Să ne facă versiuni mai bune ale noastre înșine (ex. antrenor de viață/stăpân al sarcinilor, ajutându-ne să învățăm reglarea emoțională și abilitățile de mindfulness, să construim reziliență etc.)

## Ce va acoperi această lecție

- Care sunt Principiile de Design Agentice
- Care sunt câteva linii directoare de urmat implementând aceste principii de design
- Care sunt câteva exemple de utilizare a principiilor de design

## Obiectivele de învățare

După ce completați această lecție, veți putea:

1. Explica ce sunt Principiile de Design Agentice
2. Explica liniile directoare pentru utilizarea Principiilor de Design Agentice
3. Înțelege cum să construiți un agent folosind Principiile de Design Agentice

## Principiile de Design Agentice

![Principiile de Design Agentice](../../../translated_images/ro/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Spațiu)

Acesta este mediul în care agentul operează. Aceste principii informează modul în care proiectăm agenți pentru a interacționa în lumi fizice și digitale.

- **Conectarea, nu colapsarea** – ajută la conectarea oamenilor între ei, cu evenimente și cunoștințe acționabile pentru a permite colaborarea și conexiunea.
- Agenții ajută la conectarea evenimentelor, cunoștințelor și oamenilor.
- Agenții apropie oamenii. Nu sunt proiectați să înlocuiască sau să umbrească oamenii.
- **Ușor accesibil, dar ocazional invizibil** – agentul operează în general în fundal și ne împinge ușor doar când este relevant și potrivit.
  - Agentul este ușor de descoperit și accesibil pentru utilizatorii autorizați pe orice dispozitiv sau platformă.
  - Agentul suportă intrări și ieșiri multimodale (sunet, voce, text etc.).
  - Agentul poate trece fără întrerupere între prim-plan și fundal; între proactiv și reactiv, în funcție de percepția nevoilor utilizatorului.
  - Agentul poate opera în formă invizibilă, dar procesul său de fundal și colaborarea cu alți Agenți sunt transparente și controlabile de către utilizator.

### Agent (Timp)

Acesta este modul în care agentul operează în timp. Aceste principii informează modul în care proiectăm agenții care interacționează în trecut, prezent și viitor.

- **Trecut**: Reflectare asupra istoriei care include atât starea, cât și contextul.
  - Agentul oferă rezultate mai relevante bazate pe analiza datelor istorice mai bogate dincolo de eveniment, oameni sau stări.
  - Agentul creează conexiuni din evenimentele trecute și reflectă activ asupra memoriei pentru a se angaja în situațiile actuale.
- **Acum**: Împingând mai mult decât notificând.
  - Agentul întruchipează o abordare cuprinzătoare pentru interacțiunea cu oamenii. Când se întâmplă un eveniment, agentul depășește notificarea statică sau alte formalități statice. Agentul poate simplifica fluxurile sau genera dinamic indicii pentru a direcționa atenția utilizatorului în momentul potrivit.
  - Agentul livrează informații bazate pe mediul contextual, schimbările sociale și culturale și adaptate intenției utilizatorului.
  - Interacțiunea cu agentul poate fi graduală, evoluând/creșterea în complexitate pentru a împuternici utilizatorii pe termen lung.
- **Viitor**: Adaptare și evoluție.
  - Agentul se adaptează la diferite dispozitive, platforme și modalități.
  - Agentul se adaptează la comportamentul utilizatorului, nevoile de accesibilitate și este liber personalizabil.
  - Agentul este modelat de și evoluează prin interacțiune continuă cu utilizatorul.

### Agent (Nucleu)

Acestea sunt elementele cheie în nucleul designului unui agent.

- **Acceptă incertitudinea, dar stabilește încrederea**.
  - Un anumit nivel de incertitudine a agentului este așteptat. Incertitudinea este un element cheie în designul agentului.
  - Încrederea și transparența sunt straturi fundamentale în designul agentului.
  - Oamenii controlează când agentul este pornit/oprit și starea agentului este clar vizibilă în orice moment.

## Liniile Directoare pentru implementarea acestor principii

Când folosiți principiile de design de mai sus, utilizați următoarele linii directoare:

1. **Transparență**: Informați utilizatorul că AI este implicată, cum funcționează (inclusiv acțiunile trecute) și cum să ofere feedback și să modifice sistemul.
2. **Control**: Permiteți utilizatorului să personalizeze, să specifice preferințe și să personalizeze, și să aibă control asupra sistemului și a atributelor sale (inclusiv posibilitatea de a uita).
3. **Consistență**: Vizând experiențe consistente, multimodale, pe dispozitive și puncte finale. Folosiți elemente UI/UX familiare unde este posibil (ex. pictograma microfon pentru interacțiunea vocală) și reduceți încărcătura cognitivă a clientului cât mai mult posibil (ex. răspunsuri concise, ajutoare vizuale și conținut „Află mai multe”).

## Cum să proiectezi un Agent de Călătorii folosind aceste Principii și Linii Directoare

Imaginați-vă că proiectați un Agent de Călătorii, iată cum ați putea gândi utilizarea Principiilor și Liniilor Directoare de Design:

1. **Transparență** – Informați utilizatorul că Agentul de Călătorii este un agent AI. Oferiți câteva indicații de bază pentru începere (ex. un mesaj „Bună”, invitație pentru prompturi). Documentați clar acest lucru pe pagina produsului. Arătați lista prompturilor pe care utilizatorul le-a cerut anterior. Faceți clar cum să oferi feedback (deget în sus și în jos, butonul Trimite Feedback etc.). Precizați clar dacă agentul are restricții de utilizare sau de subiect.
2. **Control** – Asigurați-vă că este clar cum utilizatorul poate modifica agentul după ce a fost creat cu lucruri precum Promptul Sistemului. Permiteți utilizatorului să aleagă cât de detaliat este agentul, stilul său de scriere și orice avertismente despre ce să nu discute agentul. Permiteți utilizatorului să vizualizeze și să șteargă orice fișiere sau date asociate, prompturi și conversații anterioare.
3. **Consistență** – Asigurați-vă că pictogramele pentru Partajare Prompt, adăugarea unui fișier sau fotografie și etichetarea cuiva sau a ceva sunt standard și recunoscute. Folosiți pictograma agrafă pentru încărcarea/partajarea fișierelor cu agentul și o pictogramă imagine pentru încărcarea graficelor.

## Exemple de coduri

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Aveți întrebări suplimentare despre modelele de design pentru agenții AI?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la orele de consultanță și a obține răspunsuri la întrebările despre Agenții AI.

## Resurse suplimentare

- <a href="https://openai.com" target="_blank">Practici pentru Guvernarea Sistemelor Agentice AI | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Proiectul HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Cutia de unelte pentru AI responsabil</a>

## Lecția anterioară

[Explorarea Cadrelor Agentice](../02-explore-agentic-frameworks/README.md)

## Lecția următoare

[Modelul de Design pentru Utilizarea Instrumentelor](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->