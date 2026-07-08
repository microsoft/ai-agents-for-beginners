# Brug af Agentiske Protokoller (MCP, A2A og NLWeb)

[![Agentiske Protokoller](../../../translated_images/da/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_

Efterhånden som brugen af AI-agenter vokser, gør behovet for protokoller, der sikrer standardisering, sikkerhed og støtter åben innovation, det også. I denne lektion vil vi gennemgå 3 protokoller, der sigter mod at opfylde dette behov - Model Context Protocol (MCP), Agent to Agent (A2A) og Natural Language Web (NLWeb).

## Introduktion

I denne lektion vil vi gennemgå:

• Hvordan **MCP** tillader AI-agenter at få adgang til eksterne værktøjer og data for at udføre brugeropgaver.

• Hvordan **A2A** muliggør kommunikation og samarbejde mellem forskellige AI-agenter.

• Hvordan **NLWeb** bringer naturlige sproggrænseflader til enhver hjemmeside, som gør det muligt for AI-agenter at opdage og interagere med indholdet.

## Læringsmål

• **Identificere** det centrale formål og fordele ved MCP, A2A og NLWeb i konteksten af AI-agenter.

• **Forklare** hvordan hver protokol faciliterer kommunikation og interaktion mellem LLMs, værktøjer og andre agenter.

• **Genkende** de forskellige roller, hver protokol spiller i opbygningen af komplekse agentiske systemer.

## Model Context Protocol

**Model Context Protocol (MCP)** er en åben standard, der giver en standardiseret måde for applikationer at levere kontekst og værktøjer til LLMs. Dette muliggør en "universal adapter" til forskellige datakilder og værktøjer, som AI-agenter kan forbinde til på en konsekvent måde.

Lad os se på komponenterne i MCP, fordelene sammenlignet med direkte API-brug, og et eksempel på, hvordan AI-agenter kan bruge en MCP-server.

### MCP Kernekomponenter

MCP fungerer på en **client-server arkitektur**, og kernekomponenterne er:

• **Hosts** er LLM-applikationer (for eksempel en kodeeditor som VSCode), der opretter forbindelser til en MCP-server.

• **Clients** er komponenter inden for host-applikationen, som opretholder én-til-én forbindelser med servere.

• **Servers** er letvægtsprogrammer, der udstiller specifikke kapaciteter.

Inkluderet i protokollen er tre kerneprimitive, som er kapaciteterne for en MCP-server:

• **Værktøjer**: Disse er diskrete handlinger eller funktioner, som en AI-agent kan kalde for at udføre en handling. For eksempel kan en vejtjeneste udstille et "hent vejr" værktøj, eller en e-handelsserver kan udstille et "køb produkt" værktøj. MCP-servere annoncerer hvert værktøjs navn, beskrivelse og input/output-skema i deres kapacitetsoversigt.

• **Ressourcer**: Disse er skrivebeskyttede dataelementer eller dokumenter, som en MCP-server kan levere, og klienter kan hente dem efter behov. Eksempler inkluderer filindhold, databaseposter eller logfiler. Ressourcer kan være tekst (som kode eller JSON) eller binære (som billeder eller PDF-filer).

• **Prompter**: Disse er foruddefinerede skabeloner, der leverer foreslåede prompts og muliggør mere komplekse arbejdsgange.

### Fordele ved MCP

MCP tilbyder betydelige fordele for AI-agenter:

• **Dynamisk Værktøjsopdagelse**: Agenter kan dynamisk modtage en liste over tilgængelige værktøjer fra en server sammen med beskrivelser af, hvad de gør. Dette står i kontrast til traditionelle API'er, som ofte kræver statisk kodning for integrationer, hvilket betyder, at enhver API-ændring nødvendiggør kodeopdateringer. MCP tilbyder en "integrer én gang" tilgang, hvilket fører til større tilpasningsevne.

• **Interoperabilitet på tværs af LLMs**: MCP fungerer på tværs af forskellige LLMs og giver fleksibilitet til at skifte kerne modeller for at evaluere bedre ydeevne.

• **Standardiseret Sikkerhed**: MCP inkluderer en standard autentifikationsmetode, som forbedrer skalerbarheden ved tilføjelse af adgang til yderligere MCP-servere. Dette er enklere end at håndtere forskellige nøgler og autentifikationstyper for forskellige traditionelle API'er.

### MCP Eksempel

![MCP Diagram](../../../translated_images/da/mcp-diagram.e4ca1cbd551444a1.webp)

Forestil dig, at en bruger vil booke en flyrejse ved hjælp af en AI-assistent drevet af MCP.

1. **Forbindelse**: AI-assistenten (MCP-klienten) forbinder til en MCP-server leveret af et flyselskab.

2. **Værktøjsopdagelse**: Klienten spørger flyselskabets MCP-server: "Hvilke værktøjer har I tilgængelige?" Serveren svarer med værktøjer som "søg flyrejser" og "book flyrejser".

3. **Værktøjskald**: Du beder så AI-assistenten: "Søg venligst efter en flyrejse fra Portland til Honolulu." AI-assistenten, ved hjælp af sin LLM, identificerer, at den skal kalde "søg flyrejser" værktøjet og sender de relevante parametre (afgangssted, destination) til MCP-serveren.

4. **Udførelse og Respons**: MCP-serveren, der fungerer som en wrapper, foretager det egentlige opkald til flyselskabets interne bookings-API. Derefter modtager den flyinformationerne (f.eks. JSON-data) og sender dem tilbage til AI-assistenten.

5. **Yderligere Interaktion**: AI-assistenten præsenterer flymulighederne. Når du vælger en flyrejse, kan assistenten kalde "book flyrejse" værktøjet på den samme MCP-server og fuldføre bookingen.

## Agent-til-Agent Protokol (A2A)

Mens MCP fokuserer på at forbinde LLMs til værktøjer, går **Agent-til-Agent (A2A) protokollen** et skridt videre ved at muliggøre kommunikation og samarbejde mellem forskellige AI-agenter. A2A forbinder AI-agenter på tværs af forskellige organisationer, miljøer og teknologistakke for at fuldføre en fælles opgave.

Vi vil gennemgå komponenterne og fordelene ved A2A samt et eksempel på, hvordan det kunne anvendes i vores rejseapplikation.

### A2A Kernekomponenter

A2A fokuserer på at muliggøre kommunikation mellem agenter og få dem til at arbejde sammen om at fuldføre en delopgave for brugeren. Hver komponent i protokollen bidrager til dette:

#### Agentkort

På samme måde som en MCP-server deler en liste over værktøjer, har et Agentkort:
- Agentens navn.
- En **beskrivelse af de generelle opgaver**, det løser.
- En **liste over specifikke færdigheder** med beskrivelser for at hjælpe andre agenter (eller endda menneskelige brugere) med at forstå, hvornår og hvorfor de ville ønske at kalde på den pågældende agent.
- Den **nuværende Endpoint-URL** for agenten.
- Agentens **version** og **kapaciteter**, såsom streamingresponser og push-notifikationer.

#### Agent Udfører

Agent Udføreren er ansvarlig for **at videregive konteksten fra brugerchatten til den fjernede agent**; den fjernede agent har brug for dette for at forstå den opgave, der skal fuldføres. I en A2A-server bruger en agent sin egen Large Language Model (LLM) til at analysere indkommende forespørgsler og udføre opgaver ved hjælp af sine egne interne værktøjer.

#### Artefakt

Når en fjernagent har fuldført den forespurgte opgave, bliver dens arbejdsprodukt oprettet som et artefakt. Et artefakt **indeholder resultatet af agentens arbejde**, en **beskrivelse af, hvad der er fuldført**, og den **tekstlige kontekst**, som sendes gennem protokollen. Efter artefaktet er sendt, lukkes forbindelsen til den fjernede agent, indtil den er nødvendig igen.

#### Begivenhedskø

Denne komponent bruges til **håndtering af opdateringer og videregivelse af beskeder**. Den er særlig vigtig i produktion for agentiske systemer for at forhindre, at forbindelsen mellem agenter lukkes, før en opgave er fuldført, især når opgavens gennemførelse kan tage længere tid.

### Fordele ved A2A

• **Forbedret Samarbejde**: Det muliggør, at agenter fra forskellige udbydere og platforme kan interagere, dele kontekst og arbejde sammen, hvilket fremmer problemfri automatisering på tværs af traditionelt adskilte systemer.

• **Fleksibilitet i Modelvalg**: Hver A2A-agent kan beslutte, hvilken LLM den bruger til at servicere sine forespørgsler, hvilket gør det muligt at optimere eller finjustere modeller pr. agent, i modsætning til en enkelt LLM-forbindelse i nogle MCP-scenarier.

• **Indbygget Autentifikation**: Autentifikation er integreret direkte i A2A-protokollen, hvilket giver en robust sikkerhedsramme for agentinteraktioner.

### A2A Eksempel

![A2A Diagram](../../../translated_images/da/A2A-Diagram.8666928d648acc26.webp)

Lad os udvide vores rejsebookingsscenarie, men denne gang ved brug af A2A.

1. **Brugerforespørgsel til Multi-Agent**: En bruger interagerer med en "Rejseagent" A2A-klient/agent, muligvis ved at sige: "Book venligst en hel rejse til Honolulu i næste uge, inklusive fly, hotel og leje af bil".

2. **Orkestrering af Rejseagent**: Rejseagenten modtager denne komplekse forespørgsel. Den bruger sin LLM til at ræsonnere om opgaven og afgøre, at den skal interagere med andre specialiserede agenter.

3. **Interagent-Kommunikation**: Rejseagenten bruger derefter A2A-protokollen til at forbinde til underordnede agenter, som en "Flyagent", en "Hotelagents" og en "Biludlejningsagent", der er oprettet af forskellige virksomheder.

4. **Delegation af Opgaver**: Rejseagenten sender specifikke opgaver til disse specialiserede agenter (f.eks. "Find fly til Honolulu," "Book et hotel," "Lej en bil"). Hver af disse specialiserede agenter, som kører deres egne LLMs og bruger deres egne værktøjer (som selv kunne være MCP-servere), udfører sin særlige del af bookingen.

5. **Sammenfattet Respons**: Når alle underordnede agenter har fuldført deres opgaver, samler Rejseagenten resultaterne (flyoplysninger, hotelbekræftelse, biludlejningsbooking) og sender et omfattende, chat-lignende svar tilbage til brugeren.

## Natural Language Web (NLWeb)

Hjemmesider har længe været den primære måde for brugere at få adgang til information og data på internettet.

Lad os se på de forskellige komponenter i NLWeb, fordelene ved NLWeb og et eksempel på, hvordan vores NLWeb fungerer ved at se på vores rejseapplikation.

### Komponenter i NLWeb

- **NLWeb Applikation (Kerne Servicekode)**: Systemet, der behandler spørgsmål i naturligt sprog. Det forbinder de forskellige dele af platformen for at skabe svar. Du kan tænke på det som **motoren, der driver de naturlige sprogfunktioner** på et website.

- **NLWeb Protokol**: Dette er et **grundlæggende sæt regler for naturlig sproginteraktion** med en hjemmeside. Den sender svar tilbage i JSON-format (ofte ved brug af Schema.org). Formålet er at skabe et simpelt fundament for "AI-webben," på samme måde som HTML gjorde det muligt at dele dokumenter online.

- **MCP Server (Model Context Protocol Endpoint)**: Hver NLWeb opsætning fungerer også som en **MCP-server**. Det betyder, at den kan **dele værktøjer (som en "ask" metode) og data** med andre AI-systemer. I praksis gør det hjemmesidens indhold og evner brugbare for AI-agenter, hvilket gør siden til en del af det bredere "agentøkosystem."

- **Embedding Modeller**: Disse modeller bruges til at **omdanne hjemmesideindhold til numeriske repræsentationer kaldet vektorer** (embeddings). Disse vektorer fanger mening på en måde, som computere kan sammenligne og søge i. De gemmes i en særlig database, og brugere kan vælge, hvilken embedding-model de ønsker at bruge.

- **Vektor Database (Hentningsmekanisme)**: Denne database **gemmer embeddings af hjemmesideindholdet**. Når nogen stiller et spørgsmål, tjekker NLWeb vektordatabasen for hurtigt at finde den mest relevante information. Det giver en hurtig liste over mulige svar, rangeret efter lighed. NLWeb arbejder med forskellige vektorlager-systemer såsom Qdrant, Snowflake, Milvus, Azure AI Search og Elasticsearch.

### NLWeb ved Eksempel

![NLWeb](../../../translated_images/da/nlweb-diagram.c1e2390b310e5fe4.webp)

Betragt vores rejsebookingswebsite igen, men denne gang er det drevet af NLWeb.

1. **Dataindtagelse**: Den eksisterende produktkatalog på rejsewebsitet (f.eks. flyliste, hotelbeskrivelser, turpakker) formateres ved brug af Schema.org eller indlæses via RSS-feeds. NLWebs værktøjer indtager disse strukturerede data, opretter embeddings og gemmer dem i en lokal eller fjern vektordatabase.

2. **Forespørgsel i Naturligt Sprog (Menneske)**: En bruger besøger websitet og i stedet for at navigere i menuer, skriver i en chatgrænseflade: "Find mig et familievenligt hotel i Honolulu med pool til næste uge".

3. **NLWeb Behandling**: NLWeb applikationen modtager denne forespørgsel. Den sender forespørgslen til en LLM for forståelse og søger samtidig i sin vektordatabase efter relevante hotellister.

4. **Præcise Resultater**: LLM hjælper med at fortolke søgningeresultaterne fra databasen, identificere de bedste match baseret på kriterierne "familievenlig," "pool" og "Honolulu," og formaterer derefter et svar i naturligt sprog. Vigtigt er, at svaret henviser til faktiske hoteller fra websitets katalog og undgår opdigtet information.

5. **Interaktion med AI-Agent**: Fordi NLWeb fungerer som en MCP-server, kunne en ekstern AI-rejseagent også forbinde til denne hjemmesides NLWeb-instans. AI-agenten kunne derefter bruge MCP-metoden `ask` til direkte at forespørge websitet: `ask("Er der nogen veganske restauranter i Honolulu-området anbefalet af hotellet?")`. NLWeb-instanser ville behandle dette ved at udnytte sin database med restaurationsinformation (hvis indlæst) og returnere et struktureret JSON-svar.

### Har du flere spørgsmål om MCP/A2A/NLWeb?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at mødes med andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Ressourcer

- [MCP for Begyndere](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->