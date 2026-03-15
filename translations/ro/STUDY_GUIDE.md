# Agenți AI pentru Începători - Ghid de studiu și sinteză a cursului

Acest ghid oferă un rezumat al cursului "AI Agents for Beginners" și explică conceptele cheie, framework-urile și tiparele de design pentru construirea agenților AI.

## 1. Introducere în agenții AI

**Ce sunt agenții AI?**
Agenții AI sunt sisteme care extind capabilitățile Large Language Models (LLMs) oferindu-le acces la **instrumente**, **cunoștințe** și **memorie**. Spre deosebire de un chatbot LLM standard care doar generează text pe baza datelor de antrenament, un agent AI poate:
- **Percepe** mediul său (prin senzori sau intrări).
- **Raționează** despre cum să rezolve o problemă.
- **Acționează** pentru a schimba mediul (prin actuatoare sau executarea instrumentelor).

**Componente cheie ale unui agent:**
- **Mediu**: Spațiul în care agentul operează (de ex., un sistem de rezervări).
- **Senzori**: Mecanisme pentru a colecta informații (de ex., citirea unui API).
- **Actuatoare**: Mecanisme pentru a efectua acțiuni (de ex., trimiterea unui e-mail).
- **Creier (LLM)**: Motorul de raționament care planifică și decide ce acțiuni să întreprindă.

## 2. Framework-uri pentru agenți

Cursul folosește **Microsoft Agent Framework (MAF)** cu **Azure AI Foundry Agent Service V2** pentru construirea agenților:

| Componentă | Focus | Cel mai potrivit pentru |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Unified Python/C# SDK for agents, tools, and workflows | Building agents with tools, multi-agent workflows, and production patterns. |
| **Azure AI Foundry Agent Service** | Managed cloud runtime | Secure, scalable deployment with built-in state management, observability, and trust. |

## 3. Modele de design agentic

Tiparele de design ajută la structurarea modului în care agenții operează pentru a rezolva probleme în mod fiabil.

### **Pattern de utilizare a instrumentelor** (Lecția 4)
Acest pattern permite agenților să interacționeze cu lumea exterioară.
- **Concept**: Agentului i se oferă o "schema" (o listă de funcții disponibile și parametrii acestora). LLM-ul decide *care* instrument să fie apelat și cu *ce* argumente, pe baza cererii utilizatorului.
- **Flux**: Cererea utilizatorului -> LLM -> **Selecția instrumentului** -> **Executarea instrumentului** -> LLM (cu rezultatul instrumentului) -> Răspuns final.
- **Cazuri de utilizare**: Recuperarea datelor în timp real (vreme, prețuri de acțiuni), efectuarea de calcule, executarea de cod.

### **Pattern de planificare** (Lecția 7)
Acest pattern permite agenților să rezolve sarcini complexe, în mai mulți pași.
- **Concept**: Agentul descompune un obiectiv la nivel înalt într-o secvență de sarcini mai mici.
- **Abordări**:
  - **Decompoziția sarcinilor**: Împărțirea "Plan a trip" în "Book flight", "Book hotel", "Rent car".
  - **Planificare iterativă**: Reevaluarea planului pe baza rezultatului pașilor anteriori (de ex., dacă zborul este plin, alege o altă dată).
- **Implementare**: Implică adesea un agent "Planner" care generează un plan structurat (de ex., JSON) care este apoi executat de alți agenți.

## 4. Principii de proiectare

Când proiectați agenți, luați în considerare trei dimensiuni:
- **Spațiu**: Agenții ar trebui să conecteze oamenii și cunoștințele, să fie accesibili dar neintruzivi.
- **Timp**: Agenții ar trebui să învețe din *Trecut*, să ofere sugestii relevante în *Prezent* și să se adapteze pentru *Viitor*.
- **Nucleu**: Adoptați incertitudinea, dar stabiliți încrederea prin transparență și controlul utilizatorului.

## 5. Rezumatul lecțiilor cheie

- **Lecția 1**: Agenții sunt sisteme, nu doar modele. Ei percep, raționează și acționează.
- **Lecția 2**: Microsoft Agent Framework abstrahează complexitatea apelării instrumentelor și gestionării stării.
- **Lecția 3**: Proiectați având în vedere transparența și controlul utilizatorului.
- **Lecția 4**: Instrumentele sunt „mâinile” agentului. Definirea schemei este crucială pentru ca LLM-ul să înțeleagă cum să le folosească.
- **Lecția 7**: Planificarea este „funcția executivă” a agentului, permițându-i să abordeze fluxuri de lucru complexe.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă o traducere profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->