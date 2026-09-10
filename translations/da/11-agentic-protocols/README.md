# Brug af Agentiske Protokoller (MCP, A2A og NLWeb)

[![Agentiske Protokoller](../../../translated_images/da/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_

Efterhånden som brugen af AI-agenter vokser, øges også behovet for protokoller, der sikrer standardisering, sikkerhed og understøtter åben innovation. I denne lektion vil vi dække 3 protokoller, der søger at imødekomme dette behov - Model Context Protocol (MCP), Agent to Agent (A2A) og Natural Language Web (NLWeb).

## Introduktion

I denne lektion vil vi gennemgå:

• Hvordan **MCP** tillader AI-agenter at få adgang til eksterne værktøjer og data for at fuldføre brugeropgaver.

• Hvordan **A2A** muliggør kommunikation og samarbejde mellem forskellige AI-agenter.

• Hvordan **NLWeb** bringer naturlige sproggrænseflader til enhver hjemmeside, hvilket gør det muligt for AI-agenter at opdage og interagere med indholdet.

## Læringsmål

• **Identificere** det centrale formål og fordelene ved MCP, A2A og NLWeb i konteksten af AI-agenter.

• **Forklare** hvordan hver protokol faciliterer kommunikation og interaktion mellem LLM'er, værktøjer og andre agenter.

• **Genkende** de forskellige roller, hver protokol spiller i opbygningen af komplekse agentiske systemer.

## Model Context Protocol

**Model Context Protocol (MCP)** er en åben standard, der giver en standardiseret måde for applikationer at give kontekst og værktøjer til LLM'er. Dette muliggør en "universel adapter" til forskellige datakilder og værktøjer, som AI-agenter kan forbinde til på en ensartet måde.

Lad os se på komponenterne i MCP, fordelene sammenlignet med direkte API-brug, og et eksempel på hvordan AI-agenter kunne bruge en MCP-server.

### MCP Kernekomponenter

MCP fungerer på en **client-server arkitektur**, og kernekomponenterne er:

• **Hosts** er LLM-applikationer (for eksempel en kodeeditor som VSCode), der starter forbindelserne til en MCP-server.

• **Clients** er komponenter inden for host-applikationen, som opretholder en-til-en-forbindelser med servere.

• **Servers** er letvægtsprogrammer, der udstiller specifikke kapabiliteter.

Inkluderet i protokollen er tre kerneprimitive, som er kapabiliteterne for en MCP-server:

• **Værktøjer**: Dette er enkelte handlinger eller funktioner, som en AI-agent kan kalde for at udføre en opgave. For eksempel kunne en vejrservice udstille et "hent vejret"-værktøj, eller en e-handelsserver kunne udstille et "køb produkt"-værktøj. MCP-servere annoncerer hvert værktøjs navn, beskrivelse og input/output-skema i deres kapabilitetsliste.

• **Ressourcer**: Dette er skrivebeskyttede dataelementer eller dokumenter, som en MCP-server kan levere, og som klienter kan hente efter behov. Eksempler inkluderer filindhold, databasenumre eller logfiler. Ressourcer kan være tekst (som kode eller JSON) eller binære filer (som billeder eller PDF'er).

• **Prompter**: Dette er foruddefinerede skabeloner, der giver foreslåede prompts og muliggør mere komplekse arbejdsgange.

### Fordele ved MCP

MCP tilbyder betydelige fordele for AI-agenter:

• **Dynamisk Værktøjsopdagelse**: Agenter kan dynamisk modtage en liste over tilgængelige værktøjer fra en server sammen med beskrivelser af, hvad de gør. Dette står i kontrast til traditionelle API'er, som ofte kræver statisk kodning for integrationer, hvilket betyder, at enhver API-ændring nødvendiggør kodeopdateringer. MCP tilbyder en "integrer én gang" tilgang, hvilket fører til større tilpasningsevne.

• **Interoperabilitet på tværs af LLM'er**: MCP fungerer på tværs af forskellige LLM'er, hvilket giver fleksibilitet til at skifte kerne modeller for at evaluere bedre ydeevne.

• **Standardiseret Sikkerhed**: MCP inkluderer en standard autentificeringsmetode, som forbedrer skalerbarheden, når man tilføjer adgang til flere MCP-servere. Dette er enklere end at håndtere forskellige nøgler og autentificeringstyper for adskillige traditionelle API'er.

### MCP Eksempel

![MCP Diagram](../../../translated_images/da/mcp-diagram.e4ca1cbd551444a1.webp)

Forestil dig, at en bruger ønsker at booke en flyrejse ved hjælp af en AI-assistent drevet af MCP.

1. **Forbindelse**: AI-assistenten (MCP-klienten) forbinder til en MCP-server, som stilles til rådighed af et flyselskab.

2. **Værktøjsopdagelse**: Klienten spørger flyselskabets MCP-server: "Hvilke værktøjer har I tilgængelige?" Serveren svarer med værktøjer som "søg fly" og "book fly".

3. **Værktøjskald**: Du beder så AI-assistenten: "Søg venligst efter en flyrejse fra Portland til Honolulu." AI-assistenten, ved hjælp af sin LLM, identificerer, at den skal kalde værktøjet "søg fly" og sender de relevante parametre (afgangssted, destination) til MCP-serveren.

4. **Udførelse og Svar**: MCP-serveren, som fungerer som en wrapper, foretager det egentlige kald til flyselskabets interne bookings-API. Den modtager derefter flyinformationerne (f.eks. JSON-data) og sender dem tilbage til AI-assistenten.

5. **Yderligere Interaktion**: AI-assistenten præsenterer flymulighederne. Når du vælger en flyrejse, kan assistenten kalde værktøjet "book fly" på den samme MCP-server og fuldføre bookingen.

## Agent-to-Agent Protokol (A2A)

Mens MCP fokuserer på at forbinde LLM'er til værktøjer, tager **Agent-to-Agent (A2A) protokollen** det et skridt videre ved at muliggøre kommunikation og samarbejde mellem forskellige AI-agenter. A2A forbinder AI-agenter på tværs af forskellige organisationer, miljøer og teknologistakke for at fuldføre en fælles opgave.

Vi vil undersøge komponenterne og fordelene ved A2A samt et eksempel på, hvordan det kunne anvendes i vores rejseapplikation.

### A2A Kernekomponenter

A2A fokuserer på at muliggøre kommunikation mellem agenter og at få dem til at arbejde sammen om at fuldføre en delopgave for brugeren. Hver komponent i protokollen bidrager til dette:

#### Agent Kort

På samme måde som en MCP-server deler en liste over værktøjer, har et Agent Kort:
- Agens navn.
- En **beskrivelse af de generelle opgaver**, den fuldfører.
- En **liste over specifikke færdigheder** med beskrivelser for at hjælpe andre agenter (eller endda menneskelige brugere) med at forstå, hvornår og hvorfor de vil kalde den agent.
- Den **aktuelle slutpunkt-URL** for agenten.
- Agentens **version** og **kapaciteter**, såsom streaming af svar og push-notifikationer.

#### Agent Executor

Agent Executor er ansvarlig for **at videregive konteksten af brugerchatten til den fjernstyrede agent**, som har brug for dette for at forstå den opgave, der skal løses. I en A2A-server bruger en agent sin egen Large Language Model (LLM) til at analysere indkommende anmodninger og udføre opgaver ved brug af sine egne interne værktøjer.

#### Artefakt

Når en fjernagent har fuldført den anmodede opgave, bliver det udførte arbejde oprettet som et artefakt. Et artefakt **indeholder resultatet af agentens arbejde**, en **beskrivelse af, hvad der blev fuldført**, og **tekstkonteksten**, der sendes gennem protokollen. Efter artefaktet er sendt, lukkes forbindelsen til den fjernstyrede agent, indtil den igen er nødvendig.

#### Event Kø

Denne komponent bruges til **håndtering af opdateringer og videresendelse af beskeder**. Den er særligt vigtig i produktion for agentiske systemer for at forhindre, at forbindelsen mellem agenter lukkes, før en opgave er fuldført, især når opgaveudførelse kan tage længere tid.

### Fordele ved A2A

• **Forbedret Samarbejde**: Det gør det muligt for agenter fra forskellige leverandører og platforme at interagere, dele kontekst og arbejde sammen, hvilket muliggør sømløs automatisering på tværs af traditionelt adskilte systemer.

• **Fleksibel Modelvalg**: Hver A2A-agent kan beslutte, hvilken LLM den bruger til at servicere sine forespørgsler, hvilket tillader optimerede eller finjusterede modeller per agent, i modsætning til en enkelt LLM-forbindelse i nogle MCP-scenarier.

• **Indbygget Autentificering**: Autentificering er integreret direkte i A2A-protokollen og giver en robust sikkerhedsramme for agentinteraktioner.

### A2A Eksempel

![A2A Diagram](../../../translated_images/da/A2A-Diagram.8666928d648acc26.webp)

Lad os uddybe vores rejsebookingsscenario, men denne gang bruge A2A.

1. **Brugeranmodning til Multi-Agent**: En bruger interagerer med en "Rejse Agent" A2A klient/agent, måske ved at sige: "Book venligst en hel rejse til Honolulu i næste uge, inklusive fly, hotel og lejebil."

2. **Orkestrering af Rejse Agent**: Rejse Agenten modtager denne komplekse anmodning. Den bruger sin LLM til at vurdere opgaven og afgøre, at den skal interagere med andre specialiserede agenter.

3. **Inter-Agent Kommunikation**: Reise Agenten bruger derefter A2A-protokollen til at forbinde til nedstrøms agenter, såsom en "Fly Agent," en "Hotel Agent," og en "Lejebil Agent," som er oprettet af forskellige firmaer.

4. **Delegation af Opgaveudførelse**: Rejse Agenten sender specifikke opgaver til disse specialiserede agenter (f.eks. "Find fly til Honolulu," "Book et hotel," "Lej en bil"). Hver af disse specialiserede agenter, der kører deres egne LLM'er og bruger deres egne værktøjer (som kunne være MCP-servere selv), udfører deres del af bookingen.

5. **Konsolideret Svar**: Når alle nedstrøms agenter har fuldført deres opgaver, samler Rejse Agenten resultaterne (flyoplysninger, hotelbekræftelse, biludlejning) og sender et omfattende, chat-lignende svar tilbage til brugeren.

## Natural Language Web (NLWeb)

Websites har længe været den primære måde for brugere at få adgang til information og data på internettet.

Lad os se på de forskellige komponenter af NLWeb, fordelene ved NLWeb og et eksempel på, hvordan vores NLWeb fungerer ved at se på vores rejseapplikation.

### Komponenter i NLWeb

- **NLWeb Applikation (Kernesoftwarekode)**: Systemet som behandler spørgsmål i naturligt sprog. Det forbinder platformens forskellige dele for at skabe svar. Du kan tænke på det som **motoren, der driver naturlige sprogfunktioner** på en hjemmeside.

- **NLWeb Protokol**: Dette er et **grundlæggende regelsæt for interaktion i naturligt sprog** med en hjemmeside. Den sender svar tilbage i JSON-format (ofte ved brug af Schema.org). Dens formål er at skabe et simpelt fundament for “AI Web,” på samme måde som HTML gjorde det muligt at dele dokumenter online.

- **MCP Server (Model Context Protocol Endpoint)**: Hver NLWeb-opsætning fungerer også som en **MCP-server**. Det betyder, at den kan **dele værktøjer (som en “ask” metode) og data** med andre AI-systemer. I praksis gør dette hjemmesidens indhold og funktionaliteter brugbare for AI-agenter, hvilket giver siden mulighed for at blive en del af det bredere “agentøkosystem.”

- **Embedding Modeller**: Disse modeller bruges til at **omdanne hjemmesideindhold til numeriske repræsentationer kaldet vektorer** (embedding). Disse vektorer indfanger mening på en måde, computere kan sammenligne og søge i. De gemmes i en specialiseret database, og brugere kan vælge, hvilken embedding-model de vil bruge.

- **Vektor Database (Genfinding Mekanisme)**: Denne database **gemmer embeddings af hjemmesideindholdet**. Når nogen stiller et spørgsmål, tjekker NLWeb vektordatabasen for hurtigt at finde den mest relevante information. Den giver en hurtig liste med mulige svar, rangeret efter lighed. NLWeb arbejder med forskellige vektorlagringssystemer som Qdrant, Snowflake, Milvus, Azure AI Search og Elasticsearch.

### NLWeb ved eksempel

![NLWeb](../../../translated_images/da/nlweb-diagram.c1e2390b310e5fe4.webp)

Overvej vores rejsebookingsside igen, men denne gang drevet af NLWeb.

1. **Dataindsamling**: Rejsesidens eksisterende produktkataloger (f.eks. flyoversigter, hotelbeskrivelser, ture) formateres med Schema.org eller indlæses via RSS-feeds. NLWebs værktøjer indlæser disse strukturerede data, opretter embeddings og gemmer dem i en lokal eller fjern vektordatabase.

2. **Forespørgsel i Naturligt Sprog (Menneske)**: En bruger besøger hjemmesiden og i stedet for at navigere i menuer, skriver i en chatgrænseflade: "Find et familievenligt hotel i Honolulu med pool til næste uge."

3. **NLWeb Behandling**: NLWeb-applikationen modtager denne forespørgsel. Den sender forespørgslen til en LLM for forståelse og søger samtidig i sin vektordatabase efter relevante hoteloversigter.

4. **Præcise Resultater**: LLM'en hjælper med at fortolke søgeresultaterne fra databasen, identificere de bedste match baseret på kriterierne "familievenligt," "pool," og "Honolulu," og formaterer derefter et svar i naturligt sprog. Vigtigt er, at svaret refererer til faktiske hoteller fra hjemmesidens katalog og undgår opdigtet information.

5. **AI Agent Interaktion**: Fordi NLWeb fungerer som en MCP-server, kunne en ekstern AI-rejseagent også forbinde til denne hjemmesides NLWeb-instans. AI-agenten kunne derefter bruge `ask` MCP-metoden til at forespørge hjemmesiden direkte: `ask("Er der nogen veganervenlige restauranter i Honolulu-området anbefalet af hotellet?")`. NLWeb-instansen ville behandle dette, udnytte sin database af restaurantinformation (hvis indlæst), og returnere et struktureret JSON-svar.

### Har du flere spørgsmål om MCP/A2A/NLWeb?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få besvaret dine spørgsmål om AI-agenter.

## Ressourcer

- [MCP for Begyndere](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repository](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Forrige Lektion

[AI-agenter i Produktion](../10-ai-agents-production/README.md)

## Næste Lektion

[Kontekst Engineering for AI-agenter](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->