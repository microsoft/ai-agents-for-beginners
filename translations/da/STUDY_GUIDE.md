# AI-agenter for begyndere - Studieguide og kursussammenfatning

Denne guide giver et overblik over kurset "AI Agents for Beginners" og forklarer nøglebegreber, frameworks og designmønstre til opbygning af AI-agenter.

## 1. Introduktion til AI-agenter

**Hvad er AI-agenter?**  
AI-agenter er systemer, der udvider kapaciteterne for Large Language Models (LLMs) ved at give dem adgang til **værktøjer**, **viden** og **hukommelse**. I modsætning til en standard LLM-chatbot, der kun genererer tekst baseret på træningsdata, kan en AI-agent:  
- **Opfatte** sit miljø (via sensorer eller input).  
- **Resonere** om, hvordan et problem skal løses.  
- **Handle** for at ændre miljøet (via aktuatorer eller værktøjsudførelse).  

**Nøglekomponenter i en agent:**  
- **Miljø**: Det rum, hvor agenten opererer (f.eks. et bookingsystem).  
- **Sensorer**: Mekanismer til at indsamle information (f.eks. aflæsning af et API).  
- **Aktuatorer**: Mekanismer til at udføre handlinger (f.eks. sende en e-mail).  
- **Hjerne (LLM)**: Den resonerende motor, der planlægger og beslutter, hvilke handlinger der skal tages.  

## 2. Agentiske frameworks

Kurset dækker tre primære frameworks til opbygning af agenter:  

| Framework | Fokus | Bedst til |  
|-----------|-------|----------|  
| **Semantic Kernel** | Produktionsklar SDK til .NET/Python | Virksomhedsapplikationer, integrering af AI med eksisterende kode. |  
| **AutoGen** | Multi-agent samarbejde | Komplekse scenarier med flere specialiserede agenter, der kommunikerer. |  
| **Azure AI Agent Service** | Administreret cloudtjeneste | Sikker, skalerbar udrulning med indbygget tilstandsstyring. |  

## 3. Agentiske designmønstre

Designmønstre hjælper med at strukturere, hvordan agenter arbejder for at løse problemer pålideligt.  

### **Værktøjsbrugsmønster** (Lesson 4)  
Dette mønster gør det muligt for agenter at interagere med omverdenen.  
- **Koncept**: Agenten får en "skema" (en liste over tilgængelige funktioner og deres parametre). LLM’en beslutter *hvilket* værktøj, der skal kaldes, og med *hvilke* argumenter baseret på brugerens forespørgsel.  
- **Flow**: Brugerforespørgsel -> LLM -> **Værktøjsvalg** -> **Værktøjsudførelse** -> LLM (med værktøjsoutput) -> Endelig svar.  
- **Anvendelsestilfælde**: Indhentning af realtidsdata (vejret, aktiekurser), udførelse af beregninger, kørsel af kode.  

### **Planlægningsmønster** (Lesson 7)  
Dette mønster gør det muligt for agenter at løse komplekse, flertrinsopgaver.  
- **Koncept**: Agenten nedbryder et højniveau-mål til en række mindre delopgaver.  
- **Tilgange**:  
  - **Opgavenedbrydning**: Opdelingen af "Planlæg en rejse" i "Book fly", "Book hotel", "Lej bil".  
  - **Iterativ planlægning**: Genovervejelse af planen baseret på output fra tidligere trin (f.eks. hvis flyet er fuldt, vælg en anden dato).  
- **Implementering**: Indeholder ofte en "Planner"-agent, der genererer en struktureret plan (f.eks. JSON), som derefter udføres af andre agenter.  

## 4. Designprincipper

Når man designer agenter, bør man overveje tre dimensioner:  
- **Rum**: Agenter bør forbinde mennesker og viden, være tilgængelige men ikke påtrængende.  
- **Tid**: Agenter bør lære af *fortiden*, give relevante puf i *nutiden* og tilpasse sig for *fremtiden*.  
- **Kernen**: Omfavn usikkerhed, men etabler tillid gennem gennemsigtighed og brugerens kontrol.  

## 5. Opsummering af nøglelektioner

- **Lektion 1**: Agenter er systemer, ikke bare modeller. De opfatter, resonerer og handler.  
- **Lektion 2**: Frameworks som Semantic Kernel og AutoGen abstraherer kompleksiteten ved værktøjskald og tilstandsstyring.  
- **Lektion 3**: Design med gennemsigtighed og brugerens kontrol for øje.  
- **Lektion 4**: Værktøjer er agentens "hænder". Skemadefinition er afgørende for, at LLM forstår, hvordan de skal bruges.  
- **Lektion 7**: Planlægning er agentens "eksekutive funktion", der gør det muligt at håndtere komplekse arbejdsprocesser.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For vigtig information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->