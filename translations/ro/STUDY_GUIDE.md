# AI Agents for Beginners - Ghid de studiu și rezumat al cursului

Acest ghid oferă un rezumat al cursului "AI Agents for Beginners" și explică conceptele cheie, cadrele și tiparele de proiectare pentru construirea agenților AI.

## 1. Introducere în agenții AI

**Ce sunt agenții AI?**
Agenții AI sunt sisteme care extind capabilitățile Modelelor lingvistice mari (LLMs) oferindu-le acces la **instrumente**, **cunoștințe** și **memorie**. Spre deosebire de un chatbot LLM standard care doar generează text pe baza datelor de antrenament, un agent AI poate:
- **Percepe** mediul său (prin senzori sau intrări).
- **Raționa** despre cum să rezolve o problemă.
- **Acționa** pentru a schimba mediul (prin actuatori sau executarea de instrumente).

**Componente cheie ale unui agent:**
- **Mediu**: Spațiul în care agentul operează (de ex., un sistem de rezervări).
- **Senzori**: Mecanisme pentru colectarea informațiilor (de ex., citirea unui API).
- **Actuatori**: Mecanisme pentru a efectua acțiuni (de ex., trimiterea unui e-mail).
- **Creier (LLM)**: Motorul de raționament care planifică și decide ce acțiuni să întreprindă.

## 2. Cadre agentice

Cursul folosește **Microsoft Agent Framework (MAF)** cu **Azure AI Foundry Agent Service V2** pentru construirea agenților:

| Component | Focus | Best For |
|-----------|-------|----------|
| **Microsoft Agent Framework** | SDK unificat Python/C# pentru agenți, instrumente și fluxuri de lucru | Construirea agenților cu instrumente, fluxuri de lucru multi-agent și tipare pentru producție. |
| **Azure AI Foundry Agent Service** | Runtime cloud gestionat | Implementare securizată și scalabilă cu management al stării, observabilitate și încredere încorporate. |

## 3. Tipare de proiectare agentică

Tiparele de proiectare ajută la structurarea modului în care agenții operează pentru a rezolva probleme în mod fiabil.

### **Tiparul de utilizare a instrumentelor** (Lecția 4)
Acest tipar permite agenților să interacționeze cu lumea exterioară.
- **Concept**: Agentului i se furnizează un "schema" (o listă de funcții disponibile și parametrii lor). LLM decide *care* instrument să fie apelat și cu *ce* argumente pe baza solicitării utilizatorului.
- **Flux**: Cerere utilizator -> LLM -> **Selecție instrument** -> **Executare instrument** -> LLM (cu ieșirea instrumentului) -> Răspuns final.
- **Cazuri de utilizare**: Obținerea datelor în timp real (vreme, prețuri de pe bursă), efectuarea de calcule, executarea de cod.

### **Tiparul de planificare** (Lecția 7)
Acest tipar permite agenților să rezolve sarcini complexe în mai mulți pași.
- **Concept**: Agentul împarte un obiectiv la nivel înalt într-o secvență de subtaskuri mai mici.
- **Abordări**:
  - **Decompoziția sarcinilor**: Împărțirea "Planifică o călătorie" în "Rezervă zbor", "Rezervă hotel", "Închiriază mașină".
  - **Planificare iterativă**: Re-evaluarea planului pe baza rezultatului pașilor anteriori (de ex., dacă zborul este plin, alege o altă dată).
- **Implementare**: Adesea implică un agent "Planner" care generează un plan structurat (de ex., JSON) care este apoi executat de alți agenți.

## 4. Principii de proiectare

La proiectarea agenților, luați în considerare trei dimensiuni:
- **Spațiu**: Agenții ar trebui să conecteze oamenii și cunoștințele, să fie accesibili, dar discreți.
- **Timp**: Agenții ar trebui să învețe din *Trecut*, să ofere sugestii relevante în *Prezent*, și să se adapteze pentru *Viitor*.
- **Nucleu**: Îmbrățișați incertitudinea, dar stabiliți încredere prin transparență și controlul utilizatorului.

## 5. Rezumatul lecțiilor cheie

- **Lecția 1**: Agenții sunt sisteme, nu doar modele. Ei percep, raționează și acționează.
- **Lecția 2**: Microsoft Agent Framework abstrahează complexitatea apelării instrumentelor și gestionării stării.
- **Lecția 3**: Proiectați având în vedere transparența și controlul utilizatorului.
- **Lecția 4**: Instrumentele sunt "mâinile" agentului. Definirea schemei este crucială pentru ca LLM să înțeleagă cum să le folosească.
- **Lecția 7**: Planificarea este "funcția executivă" a agentului, permițându-i să abordeze fluxuri de lucru complexe.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Declinare de responsabilitate:
Acest document a fost tradus folosind serviciul de traducere cu inteligență artificială Co‑op Translator (https://github.com/Azure/co-op-translator). Deși ne străduim să fim cât mai preciși, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa, trebuie considerat sursa oficială. Pentru informații critice, se recomandă o traducere profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventuale neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->