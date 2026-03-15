# AI-agenter for begyndere - Studieguide & kursusoversigt

Denne guide giver et resumé af kurset "AI Agents for Beginners" og forklarer nøglebegreber, rammeværk og designmønstre til at bygge AI-agenter.

## 1. Introduktion til AI-agenter

**Hvad er AI-agenter?**  
AI-agenter er systemer, der udvider kapaciteterne af store sprogmodeller (LLMs) ved at give dem adgang til **værktøjer**, **viden** og **hukommelse**. I modsætning til en standard LLM-chatbot, der kun genererer tekst baseret på træningsdata, kan en AI-agent:  
- **Opleve** sit miljø (via sensorer eller input).  
- **Resonere** over, hvordan et problem skal løses.  
- **Handle** for at ændre miljøet (via aktuatorer eller værktøjsudførelse).

**Nøglekomponenter i en agent:**  
- **Miljø**: Det rum, hvor agenten opererer (f.eks. et bookingsystem).  
- **Sensorer**: Mekanismer til at indsamle information (f.eks. læse et API).  
- **Aktuatorer**: Mekanismer til at udføre handlinger (f.eks. sende en e-mail).  
- **Hjerne (LLM)**: Den ræsonnerende motor, der planlægger og beslutter, hvilke handlinger der skal tages.

## 2. Agentiske rammeværk

Kurset bruger **Microsoft Agent Framework (MAF)** med **Azure AI Foundry Agent Service V2** til at bygge agenter:

| Komponent | Fokus | Bedst til |
|-----------|-------|-----------|
| **Microsoft Agent Framework** | En samlet Python/C# SDK til agenter, værktøjer og workflows | Opbygning af agenter med værktøjer, multi-agent workflows og produktionsmønstre. |
| **Azure AI Foundry Agent Service** | Administreret cloud runtime | Sikker, skalerbar implementering med indbygget tilstands-administration, observabilitet og tillid. |

## 3. Agentiske designmønstre

Designmønstre hjælper med at strukturere, hvordan agenter opererer for pålideligt at løse problemer.

### **Værktøjsbrugs-mønster** (Lesson 4)  
Dette mønster muliggør, at agenter kan interagere med omverdenen.  
- **Koncept**: Agenten får en "skema" (en liste over tilgængelige funktioner og deres parametre). LLM beslutter *hvilket* værktøj der skal kaldes og med *hvilke* argumenter baseret på brugerens anmodning.  
- **Flow**: Brugeranmodning -> LLM -> **Værktøjsvalg** -> **Værktøjsudførelse** -> LLM (med værktøjsoutput) -> Endeligt svar.  
- **Brugsscenarier**: Hente realtidsdata (vejr, aktiekurser), udføre beregninger, køre kode.

### **Planlægningsmønster** (Lesson 7)  
Dette mønster gør det muligt for agenter at løse komplekse, flertrinsopgaver.  
- **Koncept**: Agenten opdeler et overordnet mål i en sekvens af mindre delopgaver.  
- **Tilgange**:  
  - **Opgavedekomponering**: Opdeling af "Planlæg en rejse" i "Book fly", "Book hotel", "Lej bil".  
  - **Iterativ planlægning**: Revurdere planen baseret på output fra tidligere trin (f.eks. hvis flyet er fuldt, vælg en anden dato).  
- **Implementering**: Involverer ofte en "Planner"-agent, som genererer en struktureret plan (f.eks. JSON), der derefter udføres af andre agenter.

## 4. Designprincipper

Ved design af agenter, overvej tre dimensioner:  
- **Rum**: Agenter skal forbinde mennesker og viden, være tilgængelige men ikke påtrængende.  
- **Tid**: Agenter skal lære af *fortiden*, give relevante påmindelser i *nutiden*, og tilpasse sig for *fremtiden*.  
- **Kerne**: Omfavn usikkerhed, men skab tillid gennem transparens og brugerens kontrol.

## 5. Resumé af nøglelektioner

- **Lesson 1**: Agenter er systemer, ikke kun modeller. De oplever, ræsonnerer og handler.  
- **Lesson 2**: Microsoft Agent Framework abstraherer kompleksiteten ved værktøjskald og tilstandsstyring.  
- **Lesson 3**: Design med transparens og brugerens kontrol for øje.  
- **Lesson 4**: Værktøjer er agentens "hænder". Skemadefinition er afgørende for, at LLM kan forstå, hvordan de bruges.  
- **Lesson 7**: Planlægning er agentens "ledende funktion", som gør den i stand til at håndtere komplekse workflows.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->