# AI Agents for Beginners - Ghid de studiu și rezumat de curs

Acest ghid oferă un rezumat al cursului „AI Agents for Beginners” și explică conceptele cheie, cadrele și modelele de design pentru construirea Agenților AI.

## 1. Introducere în Agenții AI

**Ce sunt Agenții AI?**  
Agenții AI sunt sisteme care extind capacitățile Modelelor Mari de Limbaj (LLM-uri) prin oferirea accesului la **unelte**, **cunoștințe** și **memorie**. Spre deosebire de un chatbot LLM standard care doar generează text bazat pe datele de antrenament, un Agent AI poate:  
- **Percepe** mediul înconjurător (prin senzori sau inputuri).  
- **Raționa** despre cum să rezolve o problemă.  
- **Acționa** pentru a schimba mediul (prin actuatoare sau execuție de unelte).

**Componente cheie ale unui Agent:**  
- **Mediu**: Spațiul în care agentul operează (ex: un sistem de rezervări).  
- **Senzori**: Mecanisme pentru colectarea informațiilor (ex: citirea unui API).  
- **Actuatoare**: Mecanisme pentru efectuarea acțiunilor (ex: trimiterea unui email).  
- **Creier (LLM)**: Motorul de raționament care planifică și decide ce acțiuni să ia.

## 2. Cadre agentice

Cursul acoperă trei cadre principale pentru construirea agenților:

| Cadru | Focalizare | Cel mai potrivit pentru |
|-----------|-------|----------|
| **Semantic Kernel** | SDK gata pentru producție pentru .NET/Python | Aplicații enterprise, integrarea AI cu cod existent. |
| **AutoGen** | Colaborare multi-agent | Scenarii complexe care necesită mai mulți agenți specializați ce comunică între ei. |
| **Azure AI Agent Service** | Serviciu cloud gestionat | Implementare sigură și scalabilă cu gestionare integrată a stării. |

## 3. Modele de design agentic

Modelele de design ajută la structurarea modului în care agenții operează pentru a rezolva probleme în mod fiabil.

### **Modelul de utilizare a uneltelor** (Lecția 4)  
Acest model permite agenților să interacționeze cu lumea exterioară.  
- **Concept**: Agentului i se oferă un „schema” (o listă cu funcțiile disponibile și parametrii lor). LLM-ul decide *ce* unealtă să apeleze și cu *ce* argumente în funcție de solicitarea utilizatorului.  
- **Flux**: Cerere utilizator -> LLM -> **Selectarea uneltei** -> **Executarea uneltei** -> LLM (cu outputul uneltei) -> Răspuns final.  
- **Cazuri de utilizare**: Obținerea datelor în timp real (vreme, prețuri bursiere), efectuarea de calcule, rularea de cod.

### **Modelul de planificare** (Lecția 7)  
Acest model permite agenților să rezolve sarcini complexe, în mai mulți pași.  
- **Concept**: Agentul descompune un scop de nivel înalt într-o secvență de sub-sarcini mai mici.  
- **Abordări**:  
  - **Decompozarea sarcinii**: Împărțirea „Planifică o excursie” în „Rezervă zbor”, „Rezervă hotel”, „Închiriază mașină”.  
  - **Planificare iterativă**: Reevaluarea planului pe baza rezultatelor pașilor anteriori (ex: dacă zborul e plin, alege o altă dată).  
- **Implementare**: De multe ori implică un agent „Planificator” care generează un plan structurat (ex: JSON) ce este apoi executat de alți agenți.

## 4. Principii de design

La proiectarea agenților, ia în considerare trei dimensiuni:  
- **Spațiu**: Agenții ar trebui să conecteze oamenii și cunoștințele, să fie accesibili, dar discreți.  
- **Timp**: Agenții trebuie să învețe din *Trecut*, să ofere sugestii relevante în *Prezent* și să se adapteze pentru *Viitor*.  
- **Nucleu**: Acceptă incertitudinea, dar stabilește încrederea prin transparență și controlul utilizatorului.

## 5. Rezumatul lecțiilor cheie

- **Lecția 1**: Agenții sunt sisteme, nu doar modele. Ei percep, raționează și acționează.  
- **Lecția 2**: Cadre ca Semantic Kernel și AutoGen ascund complexitatea apelării uneltelor și gestionării stării.  
- **Lecția 3**: Proiectează cu transparență și control asupra utilizatorului în minte.  
- **Lecția 4**: Uneltele sunt „mâinile” agentului. Definirea schema este crucială pentru ca LLM-ul să știe cum să le folosească.  
- **Lecția 7**: Planificarea este „funcția executivă” a agentului, permițându-i să abordeze fluxuri de lucru complexe.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să aveți în vedere că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot rezulta din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->