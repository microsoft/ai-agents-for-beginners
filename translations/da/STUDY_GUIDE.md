# AI-agenter for begyndere - Studieguide og kursussammendrag

Denne guide giver et sammendrag af kurset "AI Agents for Beginners" og forklarer nøglebegreber, frameworks og designmønstre til opbygning af AI-agenter.

## 1. Introduktion til AI-agenter

**Hvad er AI-agenter?**  
AI-agenter er systemer, der udvider mulighederne for store sprogmodeller (LLMs) ved at give dem adgang til **værktøjer**, **viden** og **hukommelse**. I modsætning til en standard LLM-chatbot, der kun genererer tekst baseret på træningsdata, kan en AI-agent:  
- **Opfatte** sit miljø (via sensorer eller input).  
- **Resonere** om, hvordan et problem løses.  
- **Handle** for at ændre miljøet (via aktuatorer eller værktøjsudførelse).

**Nøglekomponenter i en agent:**  
- **Miljø**: Det rum hvor agenten opererer (f.eks. et bookingsystem).  
- **Sensorer**: Mekanismer til at indsamle information (f.eks. læse en API).  
- **Aktuatorer**: Mekanismer til at udføre handlinger (f.eks. sende en e-mail).  
- **Hjerne (LLM)**: Det ræsonnementsmotor, der planlægger og beslutter, hvilke handlinger der skal tages.

## 2. Agentiske frameworks

Kurset bruger **Microsoft Agent Framework (MAF)** med **Azure AI Foundry Agent Service V2** til at bygge agenter:

| Komponent | Fokus | Bedst til |
|-----------|-------|-----------|
| **Microsoft Agent Framework** | Unified Python/C# SDK til agenter, værktøjer og workflows | Opbygning af agenter med værktøjer, multi-agent workflows og produktionsmønstre. |
| **Azure AI Foundry Agent Service** | Administreret cloud runtime | Sikker, skalerbar implementering med indbygget tilstandsadministration, observabilitet og tillid. |

## 3. Agentiske designmønstre

Designmønstre hjælper med at strukturere, hvordan agenter opererer for at løse problemer pålideligt.

### **Tool Use Pattern** (Lektionen 4)  
Dette mønster gør det muligt for agenter at interagere med omverdenen.  
- **Koncept**: Agenten får et "schema" (en liste over tilgængelige funktioner og deres parametre). LLM’en beslutter *hvilket* værktøj der skal kaldes, og med *hvilke* argumenter baseret på brugerens anmodning.  
- **Flow**: Brugeranmodning -> LLM -> **Værktøjsvalg** -> **Værktøjsudførelse** -> LLM (med værktøjsoutput) -> Endeligt svar.  
- **Anvendelsestilfælde**: Hentning af realtidsdata (vejr, aktiekurser), udførelse af beregninger, eksekvering af kode.

### **Planning Pattern** (Lektionen 7)  
Dette mønster gør det muligt for agenter at løse komplekse, flertrinsopgaver.  
- **Koncept**: Agenten nedbryder et overordnet mål i en sekvens af mindre delopgaver.  
- **Tilgange**:  
  - **Opgavedelegation**: Opdeling af "Planlæg en rejse" i "Book fly", "Book hotel", "Lej bil".  
  - **Iterativ planlægning**: Genovervejelse af planen baseret på output fra tidligere trin (f.eks. hvis flyet er fuldt, vælg en anden dato).  
- **Implementering**: Indebærer ofte en "Planner"-agent, der genererer en struktureret plan (f.eks. JSON), som derefter udføres af andre agenter.

## 4. Designprincipper

Ved design af agenter bør man tage højde for tre dimensioner:  
- **Rum**: Agenter skal forbinde mennesker og viden, være tilgængelige men ikke påtrængende.  
- **Tid**: Agenter skal lære af *fortiden*, give relevante input i *nutiden* og tilpasse sig til *fremtiden*.  
- **Kerne**: Omfavn usikkerhed, men etabler tillid gennem gennemsigtighed og brugerfor kontrol.

## 5. Sammendrag af nøglelektioner

- **Lektion 1**: Agenter er systemer, ikke blot modeller. De opfatter, resonerer og handler.  
- **Lektion 2**: Microsoft Agent Framework abstraherer kompleksiteten ved værktøjskald og tilstandsadministration.  
- **Lektion 3**: Design med gennemsigtighed og brugerfor kontrol for øje.  
- **Lektion 4**: Værktøjer er agentens "hænder". Schema-definition er afgørende for, at LLM forstår, hvordan de bruges.  
- **Lektion 7**: Planlægning er agentens "executive funktion", der gør det muligt at tackle komplekse workflows.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. Ved kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->