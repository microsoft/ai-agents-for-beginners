# Brug af Agentiske Protokoller (MCP, A2A og NLWeb)

[![Agentic Protocols](../../../translated_images/da/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_

Efterhånden som brugen af AI-agenter vokser, vokser også behovet for protokoller, der sikrer standardisering, sikkerhed og understøtter åben innovation. I denne lektion vil vi dække 3 protokoller, der søger at imødekomme dette behov - Model Context Protocol (MCP), Agent to Agent (A2A) og Natural Language Web (NLWeb).

## Introduktion

I denne lektion vil vi dække:

• Hvordan **MCP** tillader AI-agenter at få adgang til eksterne værktøjer og data for at fuldføre brugeropgaver.

• Hvordan **A2A** muliggør kommunikation og samarbejde mellem forskellige AI-agenter.

• Hvordan **NLWeb** bringer naturlige sproggrænseflader til enhver hjemmeside, hvilket gør AI-agenter i stand til at opdage og interagere med indholdet.

## Læringsmål

• **Identificere** det centrale formål og fordelene ved MCP, A2A og NLWeb i konteksten af AI-agenter.

• **Forklare** hvordan hver protokol faciliterer kommunikation og interaktion mellem LLMs, værktøjer og andre agenter.

• **Genkende** de forskellige roller, som hver protokol spiller i opbygningen af komplekse agentiske systemer.

## Model Context Protocol

**Model Context Protocol (MCP)** er en åben standard, der giver en standardiseret måde for applikationer til at give kontekst og værktøjer til LLMs. Dette muliggør en "universal adapter" til forskellige datakilder og værktøjer, som AI-agenter kan forbinde til på en ensartet måde.

Lad os se på komponenterne i MCP, fordelene sammenlignet med direkte API-brug, og et eksempel på, hvordan AI-agenter kunne bruge en MCP-server.

### MCP kernekomponenter

MCP opererer på en **client-server arkitektur** og kernekomponenterne er:

• **Hosts** er LLM-applikationer (for eksempel en kode-editor som VSCode), der starter forbindelser til en MCP-server.

• **Clients** er komponenter inden for host-applikationen, som opretholder en-til-en forbindelser med servere.

• **Servers** er letvægtsprogrammer, der eksponerer specifikke kapaciteter.

Inkluderet i protokollen er tre kerneprimitiver, som er kapaciteterne af en MCP-server:

• **Tools**: Disse er diskrete handlinger eller funktioner, som en AI-agent kan kalde for at udføre en handling. For eksempel kunne en vejrtjeneste eksponere et "get weather"-værktøj, eller en e-handelsserver kunne eksponere et "purchase product"-værktøj. MCP-servere annoncerer hvert værktøjs navn, beskrivelse og input/output-skema i deres kapacitetsliste.

• **Resources**: Dette er læse-tilstand dataelementer eller dokumenter, som en MCP-server kan levere, og klienter kan hente dem efter behov. Eksempler inkluderer filindhold, databaseposter eller logfiler. Ressourcer kan være tekst (som kode eller JSON) eller binære (som billeder eller PDF'er).

• **Prompts**: Dette er foruddefinerede skabeloner, der giver foreslåede prompt, som muliggør mere komplekse workflows.

### Fordele ved MCP

MCP tilbyder betydelige fordele for AI-agenter:

• **Dynamisk Værktøjsopdagelse**: Agenter kan dynamisk modtage en liste over tilgængelige værktøjer fra en server sammen med beskrivelser af, hvad de gør. Dette står i kontrast til traditionelle API'er, som ofte kræver statisk kodning for integrationer, hvilket betyder, at enhver API-ændring nødvendiggør kodeopdateringer. MCP tilbyder en "integrer én gang" tilgang, der fører til større tilpasningsevne.

• **Interoperabilitet på tværs af LLMs**: MCP fungerer på tværs af forskellige LLM'er og giver fleksibilitet til at skifte kerne-modeller for at evaluere bedre ydeevne.

• **Standardiseret Sikkerhed**: MCP inkluderer en standard autentificeringsmetode, som forbedrer skalerbarhed, når man tilføjer adgang til flere MCP-servere. Dette er enklere end at håndtere forskellige nøgler og autentificeringstyper for forskellige traditionelle API'er.

### MCP Eksempel

![MCP Diagram](../../../translated_images/da/mcp-diagram.e4ca1cbd551444a1.webp)

Forestil dig, at en bruger ønsker at booke en flyrejse ved hjælp af en AI-assistent drevet af MCP.

1. **Forbindelse**: AI-assistenten (MCP-klienten) forbinder til en MCP-server leveret af et flyselskab.

2. **Værktøjsopdagelse**: Klienten spørger flyselskabets MCP-server: "Hvilke værktøjer har I tilgængelige?" Serveren svarer med værktøjer som "search flights" og "book flights".

3. **Værktøjskald**: Du beder derefter AI-assistenten: "Søg efter en flyrejse fra Portland til Honolulu." AI-assistenten, der bruger sin LLM, identificerer, at den skal kalde værktøjet "search flights" og sender de relevante parametre (afgangssted, destination) til MCP-serveren.

4. **Eksekvering og svar**: MCP-serveren, der fungerer som en wrapper, foretager det faktiske kald til flyselskabets interne booking-API. Den modtager derefter flyoplysningerne (f.eks. JSON-data) og sender dem tilbage til AI-assistenten.

5. **Yderligere interaktion**: AI-assistenten præsenterer flymulighederne. Når du vælger en flyvning, kan assistenten kalde værktøjet "book flight" på samme MCP-server og fuldføre bookingen.

## Agent-til-Agent Protokol (A2A)

Mens MCP fokuserer på at forbinde LLM'er til værktøjer, tager **Agent-to-Agent (A2A) protokollen** det et skridt videre ved at muliggøre kommunikation og samarbejde mellem forskellige AI-agenter. A2A forbinder AI-agenter på tværs af forskellige organisationer, miljøer og teknologistakke for at fuldføre en fælles opgave.

Vi vil undersøge komponenterne og fordelene ved A2A, sammen med et eksempel på, hvordan det kunne anvendes i vores rejseapplikation.

### A2A kernekomponenter

A2A fokuserer på at muliggøre kommunikation mellem agenter og lade dem arbejde sammen om at fuldføre en delopgave for brugeren. Hver komponent i protokollen bidrager til dette:

#### Agentkort

Ligesom en MCP-server deler en liste over værktøjer, har et Agentkort:
- Agentens navn.
- En **beskrivelse af de generelle opgaver**, den løser.
- En **liste over specifikke færdigheder** med beskrivelser for at hjælpe andre agenter (eller endda menneskelige brugere) til at forstå, hvornår og hvorfor de vil kalde den pågældende agent.
- Den **aktuelle Endpoint URL** for agenten.
- Agentens **version** og **kapaciteter** såsom streaming-svar og push-notifikationer.

#### Agent Eksekutor

Agent Eksekutoren er ansvarlig for at **viderebringe konteksten af brugerchatten til den eksterne agent**; den eksterne agent har brug for dette for at forstå opgaven, der skal løses. I en A2A-server bruger en agent sin egen Large Language Model (LLM) til at analysere indkommende anmodninger og udføre opgaver ved hjælp af sine egne interne værktøjer.

#### Artefakt

Når en fjernagent har fuldført den anmodede opgave, oprettes dens arbejdsløsning som et artefakt. Et artefakt **indeholder resultatet af agentens arbejde**, en **beskrivelse af, hvad der er fuldført**, og den **tekstkontekst**, der sendes gennem protokollen. Efter artefaktet er sendt, lukkes forbindelsen til den eksterne agent, indtil den igen er nødvendig.

#### Event Queue

Denne komponent bruges til **håndtering af opdateringer og videresendelse af beskeder**. Den er især vigtig i produktion for agentiske systemer for at forhindre, at forbindelsen mellem agenter lukkes, før en opgave er færdig, især når opgavens fuldførelsestid kan tage længere tid.

### Fordele ved A2A

• **Forbedret Samarbejde**: Den gør det muligt for agenter fra forskellige leverandører og platforme at interagere, dele kontekst og arbejde sammen, hvilket faciliterer sømløs automatisering på tværs af traditionelt adskilte systemer.

• **Fleksibel Modelvalg**: Hver A2A-agent kan beslutte, hvilken LLM den bruger til at servicere sine anmodninger, hvilket tillader optimerede eller finjusterede modeller per agent, i modsætning til en enkelt LLM-forbindelse i nogle MCP-scenarier.

• **Indbygget Autentificering**: Autentificering er integreret direkte i A2A-protokollen og giver et robust sikkerhedsrammeværk for agentinteraktioner.

### A2A Eksempel

![A2A Diagram](../../../translated_images/da/A2A-Diagram.8666928d648acc26.webp)

Lad os udvide vores rejsebooking-scenarie, men denne gang med A2A.

1. **Brugeranmodning til Multi-Agent**: En bruger interagerer med en "Rejseagent" A2A-klient/agent, måske ved at sige: "Book venligst en hel tur til Honolulu til næste uge, inklusive fly, hotel og leje af bil."

2. **Orkestrering af Rejseagent**: Rejseagenten modtager denne komplekse anmodning. Den bruger sin LLM til at ræsonnere over opgaven og fastslå, at den skal interagere med andre specialiserede agenter.

3. **Inter-Agent Kommunikation**: Rejseagenten bruger derefter A2A-protokollen til at forbinde til underordnede agenter, såsom en "Flyagent", en "Hotelagent" og en "Biludlejningsagent" skabt af forskellige virksomheder.

4. **Delegeret Opgaveeksekvering**: Rejseagenten sender specifikke opgaver til disse specialiserede agenter (fx "Find fly til Honolulu", "Book et hotel", "Lej en bil"). Hver af disse specialiserede agenter, kørende med deres egne LLM'er og brugende deres egne værktøjer (som selv kunne være MCP-servere), udfører sin specifikke del af bookingen.

5. **Konsolideret Svar**: Når alle underordnede agenter har fuldført deres opgaver, samler Rejseagenten resultaterne (flydetaljer, hotelbekræftelse, biludlejningsbooking) og sender et omfattende, chat-stil svar tilbage til brugeren.

## Natural Language Web (NLWeb)

Hjemmesider har længe været den primære måde for brugere at tilgå information og data på tværs af internettet.

Lad os se på de forskellige komponenter i NLWeb, fordelene ved NLWeb og et eksempel på, hvordan vores NLWeb fungerer ved at se på vores rejseapplikation.

### Komponenter af NLWeb

- **NLWeb Applikation (Kerne-service kode)**: Systemet, der behandler spørgsmål i naturligt sprog. Det forbinder de forskellige dele af platformen for at skabe svar. Du kan tænke på det som **motoren, der driver de naturlige sprogfunktioner** på en hjemmeside.

- **NLWeb Protokol**: Dette er et **grundlæggende sæt regler for naturlig sproginteraktion** med en hjemmeside. Den sender svar tilbage i JSON-format (ofte ved brug af Schema.org). Formålet er at skabe et simpelt fundament for “AI-webben” på samme måde, som HTML gjorde det muligt at dele dokumenter online.

- **MCP Server (Model Context Protocol Endpoint)**: Hver NLWeb-installation fungerer også som en **MCP-server**. Det betyder, at den kan **dele værktøjer (som en "ask"-metode) og data** med andre AI-systemer. I praksis gør det hjemmesidens indhold og evner brugbare af AI-agenter og tillader siden at blive en del af det bredere “agente økosystem.”

- **Embedding Modeller**: Disse modeller bruges til at **konvertere hjemmesidens indhold til numeriske repræsentationer kaldet vektorer** (embeddings). Disse vektorer indfanger mening på en måde, som computere kan sammenligne og søge i. De gemmes i en særlig database, og brugere kan vælge, hvilken embedding-model de ønsker at bruge.

- **Vector Database (Retrieval Mekanisme)**: Denne database **gemmer embeddings af hjemmesidens indhold**. Når nogen stiller et spørgsmål, tjekker NLWeb vektordatabasen for hurtigt at finde den mest relevante information. Den giver en hurtig liste over mulige svar, rangeret efter lighed. NLWeb arbejder med forskellige vektor-lagringssystemer som Qdrant, Snowflake, Milvus, Azure AI Search og Elasticsearch.

### NLWeb ved Eksempel

![NLWeb](../../../translated_images/da/nlweb-diagram.c1e2390b310e5fe4.webp)

Overvej vores rejsebookingside igen, men denne gang er den drevet af NLWeb.

1. **Dataindtastning**: Rejsesidens eksisterende produktkataloger (f.eks. flyopstillinger, hotelbeskrivelser, turpakker) formateres med Schema.org eller indlæses via RSS-feeds. NLWebs værktøjer indtager disse strukturerede data, opretter embeddings og gemmer dem i en lokal eller ekstern vektordatabasen.

2. **Forespørgsel i Naturligt Sprog (Menneske)**: En bruger besøger hjemmesiden og i stedet for at navigere i menuer, skriver i en chatgrænseflade: "Find mig et familievenligt hotel i Honolulu med pool til næste uge."

3. **NLWeb Behandling**: NLWeb-applikationen modtager denne forespørgsel. Den sender forespørgslen til en LLM for forståelse og søger samtidig i sin vektordatabasen efter relevante hotelopstillinger.

4. **Præcise Resultater**: LLM hjælper med at fortolke søgeresultaterne fra databasen, identificere de bedste match baseret på kriterierne “familievenligt,” “pool” og “Honolulu,” og formaterer derefter et svar i naturligt sprog. Vigtigst af alt henviser svaret til faktiske hoteller fra sidens katalog og undgår opdigtede oplysninger.

5. **AI Agent Interaktion**: Fordi NLWeb fungerer som en MCP-server, kunne en ekstern AI-rejseagent også forbinde til denne hjemmesides NLWeb-instanse. AI-agenten kunne så bruge den `ask` MCP-metode til at spørge hjemmesiden direkte: `ask("Er der nogen veganske restauranter i Honolulu-området, som hotellet anbefaler?")`. NLWeb-instanse ville behandle dette, udnytte sin database med restaurationsinformation (hvis indlæst), og returnere et struktureret JSON-svar.

### Har du flere spørgsmål om MCP/A2A/NLWeb?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få besvaret dine spørgsmål om AI-agenter.

## Ressourcer

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Forrige Lektion

[AI Agents in Production](../10-ai-agents-production/README.md)

## Næste Lektion

[Context Engineering for AI Agents](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->